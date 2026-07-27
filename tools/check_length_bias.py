"""Flag quizzes where the correct answer is gameable by length alone.

A student who can't answer a question can still beat it if the correct
choice is reliably the longest one. This sweeps every quiz file, reads its
real QUESTIONS array with a JS engine (many files use unquoted-key object
literals, which json.loads cannot parse), and reports two things per file:

  longest%   how often the correct answer is the UNIQUELY longest choice
             (~25% is what chance looks like with 4 options)
  gameable%  how often it is longest by a MEANINGFUL margin -- at least
             MARGIN_CHARS characters and MARGIN_FRAC longer than the next
             longest. This is the number that matters: nobody eyeballs a
             two-character difference, so a bare "is longest" flag
             overstates the problem.

Usage:
    python3 tools/check_length_bias.py                # whole site
    python3 tools/check_length_bias.py "Anatomy Exam 4"  # a folder or files
    python3 tools/check_length_bias.py --json out.json   # machine-readable

Exits non-zero if any file exceeds THRESHOLD on gameable%.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
import urllib.parse
import urllib.request

MARGIN_CHARS = 8      # absolute characters longer than the runner-up
MARGIN_FRAC = 0.18    # ...and at least this much longer, proportionally
THRESHOLD = 0.35      # flag a file above this gameable rate
PORT = 8791
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

EXTRACT = r"""
(function () {
  // A top-level `const QUESTIONS = [...]` lives in the global LEXICAL
  // environment, not on window -- window.QUESTIONS is undefined for every
  // quiz on this site. Probe the bare identifier instead.
  var arr = null;
  var probes = ['QUESTIONS','questions','Q','DECK','BANK','ITEMS'];
  for (var i = 0; i < probes.length; i++) {
    try {
      var v = eval('typeof ' + probes[i] + ' !== "undefined" ? ' + probes[i] + ' : null');
      if (v && v.length) { arr = v; break; }
    } catch (e) {}
  }
  if (!arr) return null;
  var out = [];
  for (var j = 0; j < arr.length; j++) {
    var q = arr[j];
    var opts = q.opts || q.choices || q.options || q.o;
    var c = (q.c !== undefined) ? q.c : (q.answer !== undefined ? q.answer : q.a);
    if (!opts) continue;
    var texts = [];
    if (Object.prototype.toString.call(opts) === '[object Array]') {
      for (var k = 0; k < opts.length; k++) {
        var o = opts[k];
        texts.push(typeof o === 'string' ? o : (o && (o[0] || o.t || o.text)) || '');
      }
    } else {
      var keys = Object.keys(opts).sort();
      for (var m = 0; m < keys.length; m++) texts.push(String(opts[keys[m]]));
      if (typeof c === 'string') c = keys.indexOf(c.toUpperCase());
    }
    if (typeof c === 'string') c = c.charCodeAt(0) - 65;
    if (typeof c !== 'number' || c < 0 || c >= texts.length) continue;
    out.push({ c: c, lens: texts.map(function (t) { return String(t).trim().length; }) });
  }
  return out;
})()
"""


def serve(root):
    import http.server, functools
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=root)
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def classify(q):
    """-> (is_longest, is_gameable)"""
    lens = q["lens"]
    correct = lens[q["c"]]
    others = [l for i, l in enumerate(lens) if i != q["c"]]
    if not others:
        return False, False
    runner = max(others)
    is_longest = correct > runner
    gameable = is_longest and (correct - runner) >= MARGIN_CHARS and \
        runner > 0 and (correct - runner) / runner >= MARGIN_FRAC
    return is_longest, gameable


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=[])
    ap.add_argument("--json", dest="json_out")
    ap.add_argument("--threshold", type=float, default=THRESHOLD)
    args = ap.parse_args()

    root = os.getcwd()
    files = []
    targets = args.paths or ["."]
    for t in targets:
        if os.path.isfile(t):
            files.append(t)
            continue
        for dirpath, dirnames, filenames in os.walk(t):
            dirnames[:] = [d for d in dirnames if d not in ("rpg", "tools", ".git", "node_modules")]
            for fn in filenames:
                if fn.endswith(".html"):
                    files.append(os.path.relpath(os.path.join(dirpath, fn), root))
    files = sorted(set(files))

    httpd = serve(root)
    profile = tempfile.mkdtemp(prefix="lenbias-")
    proc = subprocess.Popen(
        [CHROME, "--headless=new", "--remote-debugging-port=9777", "--remote-allow-origins=*",
         f"--user-data-dir={profile}", "--no-first-run", "--disable-gpu", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(120):
        try:
            urllib.request.urlopen("http://127.0.0.1:9777/json/version", timeout=1); break
        except Exception:
            time.sleep(0.25)

    import websocket
    tab = [t for t in json.loads(urllib.request.urlopen("http://127.0.0.1:9777/json/list").read())
           if t["type"] == "page"][0]
    ws = websocket.create_connection(tab["webSocketDebuggerUrl"], timeout=60)
    mid = [0]

    def send(method, params=None):
        mid[0] += 1
        ws.send(json.dumps({"id": mid[0], "method": method, "params": params or {}}))
        while True:
            msg = json.loads(ws.recv())
            if msg.get("id") == mid[0]:
                return msg

    send("Page.enable"); send("Runtime.enable")

    results = []
    tot_q = tot_long = tot_game = 0
    print(f"Scanning {len(files)} file(s)...")
    for n, rel in enumerate(files, 1):
        url = "http://127.0.0.1:%d/%s" % (PORT, urllib.parse.quote(rel))
        send("Page.navigate", {"url": url})
        time.sleep(0.55)
        try:
            r = send("Runtime.evaluate", {"expression": EXTRACT, "returnByValue": True})
            qs = r.get("result", {}).get("result", {}).get("value")
        except Exception:
            qs = None
        if not qs:
            continue
        nl = ng = 0
        for q in qs:
            L, G = classify(q)
            nl += L; ng += G
        results.append({"file": rel, "n": len(qs), "longest": nl, "gameable": ng,
                        "longest_pct": nl / len(qs), "gameable_pct": ng / len(qs)})
        tot_q += len(qs); tot_long += nl; tot_game += ng
        if n % 50 == 0:
            print(f"  ...{n}/{len(files)}")

    ws.close(); proc.terminate(); httpd.shutdown()

    flagged = [r for r in results if r["gameable_pct"] > args.threshold]
    flagged.sort(key=lambda r: -r["gameable_pct"])
    print("\n" + "=" * 62)
    print(f"files with a question bank : {len(results)}")
    print(f"questions                  : {tot_q}")
    if tot_q:
        print(f"correct answer is longest  : {tot_long} ({tot_long/tot_q*100:.1f}%)   [~25% = chance]")
        print(f"  ...by a gameable margin  : {tot_game} ({tot_game/tot_q*100:.1f}%)"
              f"   [>={MARGIN_CHARS} chars and >={MARGIN_FRAC:.0%} longer]")
    print(f"files over {args.threshold:.0%} gameable      : {len(flagged)}")
    for r in flagged[:25]:
        print(f"   {r['gameable_pct']*100:5.1f}%  {r['gameable']:3d}/{r['n']:3d}  {r['file']}")
    if args.json_out:
        with open(args.json_out, "w") as f:
            json.dump({"totals": {"questions": tot_q, "longest": tot_long, "gameable": tot_game},
                       "files": results}, f, indent=1)
        print(f"\nwrote {args.json_out}")
    sys.exit(1 if flagged else 0)


if __name__ == "__main__":
    main()
