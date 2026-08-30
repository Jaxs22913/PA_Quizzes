#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Measure real rendered heading contrast in dark mode.

theme.css implements dark mode by INVERTING body > .wrap
(filter: invert(1) hue-rotate(180deg)). A page is therefore meant to be
authored in LIGHT colours and let the filter flip them. A page that also
declares its own :root[data-theme="dark"] palette gets dark mode applied
TWICE, and the two do not cancel cleanly because the <body> background sits
outside .wrap and is not inverted.

That is not visible to a CSS reader and not visible to getComputedStyle --
the computed colour looks correct; only the painted pixels are wrong. So this
renders each page in dark mode, screenshots the heading, and measures the
actual contrast ratio between its lightest and darkest pixels.

Found review.html's headings at 1.1:1 (invisible) on 2026-08-30.

    python3 tools/check_dark_contrast.py                 # the default page set
    python3 tools/check_dark_contrast.py path.html ...   # specific pages
"""
import base64, io as _io, json, os, subprocess, sys, time, urllib.parse, urllib.request
import websocket
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTTP_PORT, CDP_PORT = 8772, 9338
FAIL_BELOW = 4.5   # WCAG AA for large text; a real heading should clear this easily

DEFAULT = [
    "review.html", "guides.html",
    "Pharmacology I Exam 1/pharm-exam-1-contraindications.html",
    "Pharmacology I Exam 1/pharm-exam-1-indications.html",
    "Pharmacology I Exam 1/pharm-exam-1-side-effects.html",
    "Physiology Exam 3/physiology-exam-3-hormones.html",
    "Clinical Medicine and Surgery I Exam 2/cms-ophtho-comparison-chart.html",
]


def lum(p):
    def f(c):
        c /= 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(p[0]) + 0.7152 * f(p[1]) + 0.0722 * f(p[2])


def main():
    pages = sys.argv[1:] or DEFAULT
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(HTTP_PORT)], cwd=ROOT,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    chrome = subprocess.Popen([
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        f"--remote-debugging-port={CDP_PORT}", "--headless=new", "--disable-gpu",
        "--no-first-run", "--hide-scrollbars", "--window-size=1100,900",
        f"--remote-allow-origins=http://localhost:{CDP_PORT}",
        "--user-data-dir=/tmp/dark-contrast-chrome"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(75):
        try:
            urllib.request.urlopen(f"http://localhost:{CDP_PORT}/json/version", timeout=1); break
        except Exception:
            if chrome.poll() is not None:
                srv.terminate(); sys.exit("chrome exited during startup")
            time.sleep(0.4)
    else:
        chrome.terminate(); srv.terminate(); sys.exit("chrome never opened the debugging port")

    bad = 0
    print("%-56s %-9s %s" % ("page (dark mode)", "contrast", "verdict"))
    for rel in pages:
        url = f"http://localhost:{HTTP_PORT}/" + urllib.parse.quote(rel)
        req = urllib.request.Request(
            f"http://localhost:{CDP_PORT}/json/new?{urllib.parse.quote(url, safe=':/%')}",
            method="PUT")
        tab = json.loads(urllib.request.urlopen(req, timeout=10).read())
        ws = websocket.create_connection(tab["webSocketDebuggerUrl"], timeout=15)
        n = [0]

        def call(m, p=None):
            n[0] += 1
            ws.send(json.dumps({"id": n[0], "method": m, "params": p or {}}))
            while True:
                r = json.loads(ws.recv())
                if r.get("id") == n[0]:
                    return r

        call("Runtime.enable"); call("Page.enable")
        call("Runtime.evaluate", {"expression": "localStorage.setItem('siteTheme','dark')",
                                  "returnByValue": True})
        call("Page.reload"); time.sleep(2.4)
        call("Runtime.evaluate", {"expression":
            "(function(){var b=[].find.call(document.querySelectorAll('button'),"
            "x=>/maybe later/i.test(x.textContent));if(b)b.click();})()", "returnByValue": True})
        time.sleep(0.6)
        box = call("Runtime.evaluate", {"expression":
            "(function(){var e=document.querySelector('h1');if(!e)return null;"
            "var r=e.getBoundingClientRect();"
            "return {x:Math.max(0,r.x),y:Math.max(0,r.y),w:r.width,h:r.height};})()",
            "returnByValue": True})["result"]["result"].get("value")
        if not box or box["h"] < 4:
            print("%-56s %-9s %s" % (rel[:56], "-", "no h1 -- skipped"))
            ws.close(); continue
        shot = call("Page.captureScreenshot", {"format": "png", "clip": {
            "x": box["x"], "y": box["y"], "width": min(box["w"], 900),
            "height": box["h"], "scale": 1}})
        im = Image.open(_io.BytesIO(base64.b64decode(shot["result"]["data"]))).convert("RGB")
        ls = [lum(im.getpixel((x, y))) for y in range(im.size[1]) for x in range(im.size[0])]
        ratio = (max(ls) + 0.05) / (min(ls) + 0.05)
        ok = ratio >= FAIL_BELOW
        if not ok:
            bad += 1
        print("%-56s %-9s %s" % (rel[:56], "%.1f:1" % ratio,
                                 "ok" if ok else "FAIL -- heading is unreadable in dark mode"))
        ws.close()
        urllib.request.urlopen(f"http://localhost:{CDP_PORT}/json/close/{tab['id']}").read()

    chrome.terminate(); srv.terminate()
    print("\n%d page(s) below %.1f:1" % (bad, FAIL_BELOW) if bad else "\nall pages readable in dark mode")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
