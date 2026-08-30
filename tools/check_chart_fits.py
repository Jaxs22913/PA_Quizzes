#!/usr/bin/env python3
"""Measure whether a page overflows horizontally at real window widths.

A chart that "fits" is one where the document's scrollWidth never exceeds its
clientWidth -- that is exactly the condition for no left-right scrollbar. Run it
at several widths because a table can fit a desktop and still overflow a laptop.
"""
import json, os, subprocess, sys, time, urllib.request, urllib.parse, websocket

CDP_PORT = 9451
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIDTHS = [1024, 1280, 1440, 1680]

def send(ws, mid, method, params=None):
    ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
    while True:
        m = json.loads(ws.recv())
        if m.get("id") == mid:
            return m

def measure(rel, width):
    url = "http://localhost:8901/" + urllib.parse.quote(rel)
    req = urllib.request.Request(f"http://localhost:{CDP_PORT}/json/new?{urllib.parse.quote(url, safe='')}", method="PUT")
    tab = json.loads(urllib.request.urlopen(req, timeout=10).read())
    ws = websocket.create_connection(tab["webSocketDebuggerUrl"], timeout=15)
    try:
        send(ws, 1, "Emulation.setDeviceMetricsOverride",
             {"width": width, "height": 900, "deviceScaleFactor": 1, "mobile": False})
        send(ws, 2, "Page.enable")
        send(ws, 3, "Page.reload", {"ignoreCache": True})
        time.sleep(2.2)
        r = send(ws, 4, "Runtime.evaluate", {"returnByValue": True, "expression": """
          (function(){
            var d=document.documentElement, t=document.querySelector('table');
            var w=document.querySelector('.wrap')||d;
            return {doc:d.scrollWidth, client:d.clientWidth,
                    tbl: t? Math.round(t.getBoundingClientRect().width):0,
                    tblScroll: t? t.scrollWidth:0,
                    holder: (function(){var h=t&&t.closest('.scroll');
                             return h? h.scrollWidth-h.clientWidth : 0;})()};
          })()"""})
        return r["result"]["result"]["value"]
    finally:
        ws.close()
        try:
            urllib.request.urlopen(urllib.request.Request(
                f"http://localhost:{CDP_PORT}/json/close/{tab['id']}"), timeout=5)
        except Exception:
            pass

def main(argv):
    targets = argv[1:]
    srv = subprocess.Popen([sys.executable, "-m", "http.server", "8901"], cwd=ROOT,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    chrome = subprocess.Popen([
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        f"--remote-debugging-port={CDP_PORT}", "--headless=new", "--disable-gpu",
        "--no-first-run", "--user-data-dir=/tmp/cdp-fit-profile",
        f"--remote-allow-origins=http://localhost:{CDP_PORT}"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)
    bad = 0
    try:
        for rel in targets:
            print("\n%s" % rel)
            for w in WIDTHS:
                m = measure(rel, w)
                over = m["doc"] - m["client"]
                inner = m["holder"]
                flag = ""
                if over > 1:
                    flag = "  <-- PAGE scrolls sideways by %dpx" % over; bad += 1
                elif inner > 1:
                    flag = "  <-- table scrolls inside its holder by %dpx" % inner; bad += 1
                print("   %4dpx window: document %4d / viewport %4d, table %4dpx%s"
                      % (w, m["doc"], m["client"], m["tbl"], flag))
    finally:
        chrome.terminate(); srv.terminate()
    print("\n%s" % ("FITS at every width tested" if not bad else "%d width(s) still overflow" % bad))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
