#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Drive review.html in a real browser and prove the semester/exam grouping works.

The page only shows anything when localStorage holds `qm:` records, so a plain
console sweep sees the empty state and proves nothing. This injects synthetic
records that span two semesters, three classes and four exams, reloads, then
asserts the tree, the counts, and what the tick boxes actually do.
"""
import json, os, subprocess, sys, time, urllib.parse, urllib.request, websocket

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTTP_PORT, CDP_PORT = 8767, 9333

# Real slugs from the manifest, chosen to span two semesters and several exams.
RECORDS = [
    ("anatomy-exam-1-brain-ans-quiz", 3),
    ("anatomy-exam-4-prof-shah-style-quiz", 2),
    ("physiology-exam-3-gi-quiz", 4),
    ("clinical-medicine-and-surgery-i-exam-2-acute-vision-loss-quiz", 5),
    ("microbiology-exam-1-microbe-human-interactions-quiz", 1),
    ("pharmacology-i-exam-1-ans-cholinergic-quiz", 2),
    # deliberately not in the manifest -- the page must bucket it rather than
    # drop it or throw, since a renamed quiz leaves records like this behind
    ("some-quiz-that-no-longer-exists", 1),
]


def main():
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(HTTP_PORT)], cwd=ROOT,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    chrome = subprocess.Popen([
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        f"--remote-debugging-port={CDP_PORT}", "--headless=new", "--disable-gpu",
        "--no-first-run", "--no-default-browser-check",
        f"--remote-allow-origins=http://localhost:{CDP_PORT}",
        "--user-data-dir=/tmp/review-test-chrome"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    deadline = time.time() + 30
    while time.time() < deadline:
        try:
            urllib.request.urlopen(f"http://localhost:{CDP_PORT}/json/version", timeout=1); break
        except Exception:
            if chrome.poll() is not None:
                srv.terminate(); sys.exit("chrome exited during startup")
            time.sleep(0.4)
    else:
        chrome.terminate(); srv.terminate(); sys.exit("chrome never opened the debugging port")

    url = f"http://localhost:{HTTP_PORT}/review.html"
    # /json/new needs PUT on current Chrome; GET returns 405.
    req = urllib.request.Request(
        f"http://localhost:{CDP_PORT}/json/new?{urllib.parse.quote(url, safe=':/')}", method="PUT")
    tab = json.loads(urllib.request.urlopen(req, timeout=10).read())
    ws = websocket.create_connection(tab["webSocketDebuggerUrl"], timeout=15)
    state = {"id": 0}

    def call(method, params=None):
        state["id"] += 1
        ws.send(json.dumps({"id": state["id"], "method": method, "params": params or {}}))
        while True:
            m = json.loads(ws.recv())
            if m.get("id") == state["id"]:
                return m

    def js(expr):
        r = call("Runtime.evaluate",
                 {"expression": expr, "returnByValue": True, "awaitPromise": True})
        res = r.get("result", {})
        if res.get("exceptionDetails"):
            raise RuntimeError(str(res["exceptionDetails"])[:300])
        return res.get("result", {}).get("value")

    call("Runtime.enable")
    time.sleep(1.2)

    seed = ";".join(
        "localStorage.setItem('qm:/x/%s.html', JSON.stringify(%s))" % (
            slug, json.dumps({"t": 1756000000000, "slug": slug, "title": slug,
                              "total": 30, "m": [[i, 0] for i in range(n)]}))
        for slug, n in RECORDS)
    js("localStorage.clear();" + seed + ";'ok'")
    call("Page.enable"); call("Page.reload")
    time.sleep(3.0)

    fails = []
    def check(label, got, want):
        ok = got == want
        print("  %-52s %s%s" % (label, "OK" if ok else "FAIL",
                                "" if ok else "  got %r want %r" % (got, want)))
        if not ok: fails.append(label)

    total = sum(n for _, n in RECORDS)
    print("review.html grouping:")
    check("semester sections rendered", js("document.querySelectorAll('.sem-group').length"), 3)
    check("exam groups rendered", js("document.querySelectorAll('.exam-group').length"), 7)
    check("every exam group has a tick box",
          js("document.querySelectorAll('.exam-head input[type=checkbox]').length"), 7)
    check("all ticked by default",
          js("[].every.call(document.querySelectorAll('.exam-head input'),c=>c.checked)"), True)
    check("drill button counts every missed question",
          js("document.getElementById('drill-btn').textContent.trim()"),
          "Drill %d questions" % total)
    check("newest semester first",
          js("document.querySelector('.sem-group .sem-name').textContent.indexOf('Semester 2')"), 0)
    check("semester labels come from the registry",
          js("[].map.call(document.querySelectorAll('.sem-name'),n=>n.firstChild.textContent).join('|')"),
          "Semester 2|Semester 1|Other quizzes")
    check("exam labels present",
          js("[...new Set([].map.call(document.querySelectorAll('.exam-label'),n=>n.textContent))].sort().join(',')"),
          "Exam 1,Exam 2,Exam 3,Exam 4,General")

    print("\nselection behaviour:")
    js("document.querySelectorAll('.exam-head input')[0].click()")
    time.sleep(0.3)
    first_n = RECORDS[4][1]  # the first rendered exam group is Semester 2 / Micro Exam 1
    got = js("document.getElementById('drill-btn').textContent.trim()")
    check("unticking one exam drops its questions",
          got.startswith("Drill ") and int(got.split()[1]) < total, True)
    js("[].find.call(document.querySelectorAll('.btn-ghost'),b=>b.textContent=='Select none').click()")
    time.sleep(0.3)
    check("select none disables the button",
          js("document.getElementById('drill-btn').textContent.trim()"), "Nothing selected")
    check("select none really disables it", js("document.getElementById('drill-btn').disabled"), True)
    js("[].find.call(document.querySelectorAll('.btn-ghost'),b=>b.textContent=='Select all').click()")
    time.sleep(0.3)
    check("select all restores the full count",
          js("document.getElementById('drill-btn').textContent.trim()"),
          "Drill %d questions" % total)
    js("document.querySelectorAll('.mini')[0].click()")
    time.sleep(0.3)
    sem2 = sum(n for s, n in RECORDS if s.startswith(("clinical-medicine", "microbiology", "pharmacology")))
    check("'Only this term' selects just that semester",
          js("document.getElementById('drill-btn').textContent.trim()"),
          "Drill %d questions" % sem2)

    errs = js("(window.__errs||[]).length") or 0
    check("no runtime errors", errs, 0)

    ws.close()
    urllib.request.urlopen(f"http://localhost:{CDP_PORT}/json/close/{tab['id']}").read()
    chrome.terminate(); srv.terminate()
    print("\n%d check(s) failed" % len(fails) if fails else "\nall checks passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
