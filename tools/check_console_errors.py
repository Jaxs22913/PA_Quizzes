"""
Site-wide console-error sweep: loads every .html file in the repo via headless
Chrome and reports any console.error / uncaught exception on load.
Usage: python3 check_console_errors.py [path-prefix-filter]
"""
import json, os, subprocess, sys, time, urllib.request, urllib.parse, websocket

# derived, not hardcoded: the repo moved once already (out of iCloud)
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTTP_PORT = 8850
CDP_PORT = 9450

# tools/ contains template files with unrendered __PLACEHOLDER__ tokens (quiz-template,
# cram-sheet-template) -- expected to error if loaded directly, not real bugs.
EXCLUDE_DIRS = ("tools",)

def find_html_files(prefix_filter=None):
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith(".git")]
        rel_dir = os.path.relpath(dirpath, ROOT)
        if rel_dir == "." :
            rel_dir = ""
        if any(rel_dir == d or rel_dir.startswith(d + os.sep) for d in EXCLUDE_DIRS):
            continue
        for fn in filenames:
            if fn.endswith(".html"):
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
                if prefix_filter and not rel.startswith(prefix_filter):
                    continue
                files.append(rel)
    return sorted(files)

def new_tab(url_enc):
    req = urllib.request.Request(f"http://localhost:{CDP_PORT}/json/new?{url_enc}", method="PUT")
    r = urllib.request.urlopen(req, timeout=5)
    return json.loads(r.read())["webSocketDebuggerUrl"]

def close_tab(tid):
    try:
        urllib.request.urlopen(urllib.request.Request(f"http://localhost:{CDP_PORT}/json/close/{tid}"), timeout=5)
    except Exception:
        pass

def check_page(rel_path):
    url = f"http://localhost:{HTTP_PORT}/" + rel_path
    url_enc = urllib.parse.quote(url, safe=":/")
    try:
        ws_url = new_tab(url_enc)
    except Exception as e:
        return ["tab-open-failed: " + str(e)[:150]]
    tab_id = ws_url.rsplit("/", 1)[-1]
    errors = []
    try:
        ws = websocket.create_connection(ws_url, timeout=10)
    except Exception as e:
        close_tab(tab_id)
        return ["ws-connect-failed: " + str(e)[:150]]
    _id = 0
    def send(method, params=None):
        nonlocal _id
        _id += 1
        ws.send(json.dumps({"id": _id, "method": method, "params": params or {}}))
        return _id
    def recv_until(target_id, timeout=8):
        ws.settimeout(timeout)
        while True:
            msg = json.loads(ws.recv())
            if msg.get("method") == "Console.messageAdded":
                m = msg["params"]["message"]
                if m.get("level") == "error":
                    errors.append(("console.error", m.get("text", "")[:200]))
            if msg.get("method") == "Runtime.exceptionThrown":
                d = msg["params"]["exceptionDetails"]
                text = d.get("exception", {}).get("description") or d.get("text", "")
                errors.append(("exception", str(text)[:200]))
            if msg.get("id") == target_id:
                return msg
    try:
        send("Runtime.enable"); recv_until(_id)
        send("Console.enable"); recv_until(_id)
        send("Page.enable"); recv_until(_id)
        recv_until(send("Page.navigate", {"url": url_enc}), timeout=10)
        time.sleep(0.5)
        ws.settimeout(0.4)
        try:
            while True:
                msg = json.loads(ws.recv())
                if msg.get("method") == "Console.messageAdded":
                    m = msg["params"]["message"]
                    if m.get("level") == "error":
                        errors.append(("console.error", m.get("text", "")[:200]))
                if msg.get("method") == "Runtime.exceptionThrown":
                    d = msg["params"]["exceptionDetails"]
                    text = d.get("exception", {}).get("description") or d.get("text", "")
                    errors.append(("exception", str(text)[:200]))
        except Exception:
            pass
    except Exception as e:
        errors.append(("nav-error", str(e)[:150]))
    finally:
        try: ws.close()
        except Exception: pass
        close_tab(tab_id)
    # dedupe
    seen = set(); uniq = []
    for e in errors:
        if e not in seen:
            seen.add(e); uniq.append(e)
    return uniq

if __name__ == "__main__":
    prefix = sys.argv[1] if len(sys.argv) > 1 else None
    files = find_html_files(prefix)
    print(f"Checking {len(files)} file(s)...")

    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(HTTP_PORT)], cwd=ROOT,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    chrome = subprocess.Popen([
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        f"--remote-debugging-port={CDP_PORT}", "--headless=new", "--disable-gpu",
        "--no-first-run", "--no-default-browser-check",
        f"--remote-allow-origins=http://localhost:{CDP_PORT}",
        "--user-data-dir=/tmp/console-sweep-chrome-profile"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Wait for Chrome to actually bind the debugging port instead of guessing.
    # This used to be time.sleep(1.5), which is fine on an idle machine and not
    # fine on a busy one -- every page then failed with "tab-open-failed:
    # Connection refused" and the whole sweep reported garbage. A sweep that
    # fails loudly is recoverable; one that reports every page as flagged for an
    # environmental reason is worse than not running, because it looks like a
    # finding. Poll instead, and abort with a clear message if it never comes up.
    deadline = time.time() + 30
    while True:
        try:
            urllib.request.urlopen(f"http://localhost:{CDP_PORT}/json/version", timeout=1).read()
            break
        except Exception as e:
            if chrome.poll() is not None:
                sys.exit("chrome exited during startup (code %s) -- sweep aborted, "
                         "nothing was checked" % chrome.poll())
            if time.time() > deadline:
                chrome.terminate(); srv.terminate()
                sys.exit("chrome never opened the debugging port on %d after 30s (%s) -- "
                         "sweep aborted, nothing was checked" % (CDP_PORT, e))
            time.sleep(0.25)

    results = {}
    try:
        for i, f in enumerate(files, 1):
            errs = check_page(f)
            if errs:
                results[f] = errs
                print(f"[{i}/{len(files)}] FLAG   {f}  ->  {errs[0]}")
            if i % 50 == 0:
                print(f"  ...{i}/{len(files)} checked, {len(results)} flagged so far")
    finally:
        chrome.terminate(); srv.terminate()

    print("\n" + "="*60)
    print(f"clean: {len(files)-len(results)}   flagged: {len(results)}   total: {len(files)}")
    if results:
        print("\n--- FLAGGED ---")
        for f, errs in results.items():
            print(f"  {f}")
            # entries are (kind, text) pairs, but be defensive: a malformed one
            # used to crash the whole report AFTER the 20-minute sweep, losing
            # every result -- the one moment the report actually matters
            for e in errs[:3]:
                if isinstance(e, (list, tuple)) and len(e) == 2:
                    print(f"      [{e[0]}] {e[1]}")
                else:
                    print(f"      {e!r}")
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "console_errors.json")
    json.dump(results, open(out_path, "w"), indent=1)
    print(f"\nwrote {out_path}")
