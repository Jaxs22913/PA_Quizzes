#!/usr/bin/env python3
"""Guide annotations check: highlights, text-box notes and "Add to Pip" (theme.js) in headless Chrome.

    ~/Developer/pa-tools/venv/bin/python tools/check_guide_annotations.py
    (needs pip/data for the review-guide part: python3 tools/build_pip_data.py first)

Pages are served straight from this checkout as https://pa-quizzes.com/PA_Quizzes/...; every other
request (Firebase, analytics, fonts, the helper) is blocked, so nothing is written anywhere.

A positive (one FAIL line each, exit 1):
  - a selection that starts in plain text and ends inside <strong>, one inside a table cell, one
    across two list items, one in a <dd> with <b>, one in a <th>, and a triple-click style selection
    (ending at offset 0 of the next block) do not all produce a highlight whose marks cover the
    selected words;
  - after a reload the highlights do not come back with exactly the same words;
  - a highlight saved in the pre-2026-10-15 format ({idx, start, end, color, note}, offsets into the
    legacy unit list) does not restore to the same words it covered under the old engine;
  - an ordinary click makes a note; "Add a note" then a click, or "Note" on the selection toolbar,
    does not make one; a note does not persist, update or delete across reloads; Enter on a focused
    note does not open its editor;
  - on a guide with accordions, a reload leaves any accordion open, or the highlight and note made
    inside one are not inside it after the reload;
  - at 390 px the page scrolls sideways, a note box overflows, or a toolbar button is under 44 px;
  - dark mode does not give the note box its dark colors;
  - "Add to Pip" does not land in pipReview:<exam>, or my-review-guide.html does not show it;
  - a new note (the tool, or "Note" on the selection toolbar) is not pinned at the end of the sentence
    that holds the spot ("e.g.", "E. coli", "37.5" and "vs." are not ends), or its b/a context is not;
  - deleting a note shows no polite toast with a real Undo button, or Undo does not put the note back
    at its exact spot together with its review item (text, note, position); from the keyboard, focus
    does not go to Undo and then to the restored note; removing the review item deletes the note;
  - window.SyncList.merge does not join two devices' lists by id, keep the newer change, honor and
    expire tombstones, or settle (merging the result again changes nothing);
  - after a keyboard selection the toolbar takes focus by itself, no polite hint names the key, Tab
    does not enter it as one tab stop, the arrow keys / Home / End do not move between buttons, or
    Escape does not close it and put focus and the selection back;
  - openGuidePanel({quote}) does not mark and show the cited sentence (light and dark), or a quote
    that is not in the guide changes what the panel did before;
  - any page error (on a guide, a Semester 1 guide, the homepage, a quiz or the review guide page).
"""
import argparse, json, mimetypes, os, re, sys
from urllib.parse import unquote, urlsplit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("check_guide_annotations: ERROR: playwright is not installed; run it with ~/Developer/pa-tools/venv/bin/python")

BASE = "https://pa-quizzes.com/PA_Quizzes/"
TOURS = "try{['tourSeen:quiz','tourSeen:exammode','tourSeen:home','tourSeen:guide'].forEach(k=>localStorage.setItem(k,'1'));localStorage.setItem('local:pip:hidden','1')}catch(e){}"
fails = 0


def check(name, ok, detail=""):
    global fails
    if not ok:
        fails += 1
    print("%s  %s%s" % ("PASS" if ok else "FAIL", name, "" if ok or not detail else "  -- " + str(detail)[:400]), flush=True)


def serve(route):
    u = urlsplit(route.request.url)
    if u.hostname != "pa-quizzes.com" or not u.path.startswith("/PA_Quizzes/"):
        return route.abort()
    path = unquote(u.path)[len("/PA_Quizzes/"):] or "index.html"
    fs = os.path.normpath(os.path.join(ROOT, path))
    if not fs.startswith(ROOT) or not os.path.isfile(fs):
        return route.fulfill(status=404, body="not found")
    ctype = mimetypes.guess_type(fs)[0] or "application/octet-stream"
    if ctype.startswith("text/") or ctype in ("application/javascript", "application/json"):
        ctype += "; charset=utf-8"
    with open(fs, "rb") as fh:
        route.fulfill(status=200, body=fh.read(), headers={"content-type": ctype, "cache-control": "no-store"})


# In-page helpers: find a text spot by its words, select between two spots, read marks and notes.
HELP = r"""
window.__t = {
  flat: function (root) {
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT), n, text = "", nodes = [];
    while ((n = w.nextNode())) { nodes.push([n, text.length]); text += n.data; }
    return { text: text.replace(/\s/g, " "), nodes: nodes };
  },
  at: function (root, needle, delta) {
    var f = __t.flat(root), i = f.text.indexOf(needle);
    if (i < 0) return null;
    var p = i + delta;
    for (var k = 0; k < f.nodes.length; k++) { var nd = f.nodes[k][0], b = f.nodes[k][1]; if (p >= b && p <= b + nd.data.length) return [nd, p - b]; }
    return null;
  },
  select: function (a, b) {
    var r = document.createRange(); r.setStart(a[0], a[1]); r.setEnd(b[0], b[1]);
    var s = getSelection(); s.removeAllRanges(); s.addRange(r);
    return r;
  },
  mouseup: function (el) { (el || document.body).dispatchEvent(new MouseEvent("mouseup", { bubbles: true })); },
  marks: function () {
    var by = {}, keys = [];
    document.querySelectorAll("mark.user-hl").forEach(function (m) {
      var k = m.getAttribute("data-hlk"); if (!by[k]) { by[k] = []; keys.push(k); } by[k].push(m.textContent);
    });
    return keys.map(function (k) { return [k, by[k].join("")]; });
  },
  squash: function (s) { return String(s).replace(/\s+/g, ""); }
};
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--guide", default="Clinical Medicine and Surgery I Exam 4/cms-exam-4-study-guide.html")
    ap.add_argument("--accordion-guide", default="Clinical Medicine and Surgery I Exam 4/cms-exam-4-clin-med-pro-guide.html")
    ap.add_argument("--s1-guide", default="Anatomy Exam 3/anatomy-exam-3-study-guide.html")
    ap.add_argument("--quiz", default="Clinical Medicine and Surgery I Exam 4/hypertension-quiz.html")
    a = ap.parse_args()
    guide_url = BASE + a.guide.replace(" ", "%20")
    guide_path = "/PA_Quizzes/" + a.guide.replace(" ", "%20")
    folder = a.guide.split("/")[0]
    have_pip_data = os.path.isfile(os.path.join(ROOT, "pip", "data", "index.json"))
    slug = None
    if have_pip_data:
        ix = json.load(open(os.path.join(ROOT, "pip", "data", "index.json"), encoding="utf-8"))
        slug = next((f["s"] for f in ix.get("folders", []) if f["f"] == folder), None)

    errs = []
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(channel="chrome", headless=True)

            def ctx(**kw):
                o = dict(viewport={"width": 1280, "height": 900}, service_workers="block")
                o.update(kw)
                c = b.new_context(**o)
                c.add_init_script(TOURS)
                c.route("**/*", serve)
                return c

            def open_page(c, url):
                pg = c.new_page()
                pg.on("pageerror", lambda e, u=url: errs.append("%s: %s" % (u.split("/PA_Quizzes/")[-1], e)))
                pg.goto(url, wait_until="load")
                pg.wait_for_timeout(600)
                pg.evaluate(HELP)
                return pg

            def reload(pg):
                pg.reload(wait_until="load")
                pg.wait_for_timeout(600)
                pg.evaluate(HELP)

            def clear_ui(pg):
                pg.keyboard.press("Escape")
                pg.evaluate("getSelection().removeAllRanges()")

            # ------------------------------------------------------------------ 1. highlights
            c = ctx()
            pg = open_page(c, guide_url)
            check("guide: highlighter units cover dd/th text (extra units numbered)", pg.evaluate("document.querySelectorAll('[data-hl-x]').length") > 100)

            # old-format record: the legacy engine stored textContent offsets into the legacy unit list
            legacy = pg.evaluate(r"""() => {
              var u = Array.from(document.querySelectorAll('[data-hl-idx]')).find(function (x) {
                var s = x.querySelector('strong, b'); return s && x.tagName === 'P' && x.textContent.indexOf(s.textContent) > 12; });
              var s = u.querySelector('strong, b'), t = u.textContent, j = t.indexOf(s.textContent);
              var start = Math.max(0, t.lastIndexOf(' ', j - 6) + 1), end = j + Math.min(s.textContent.length, 8);
              while (end < t.length && /[A-Za-z0-9]/.test(t[end])) end++;
              return { idx: Number(u.getAttribute('data-hl-idx')), start: start, end: end, words: t.slice(start, end), len: t.length };
            }""")
            # a second unit whose words are stored with offsets that no longer match (as after a guide edit)
            moved = pg.evaluate(r"""(skip) => { var u = Array.from(document.querySelectorAll('[data-hl-idx]')).find(function (x) {
                return Number(x.getAttribute('data-hl-idx')) !== skip && x.textContent.length > 80 && !x.querySelector('a'); });
              var t = u.textContent, q = t.slice(30, 60);
              return { idx: Number(u.getAttribute('data-hl-idx')), q: q, len: t.length, unique: t.indexOf(q) === t.lastIndexOf(q) }; }""", legacy["idx"])
            seed = json.dumps([
                {"idx": legacy["idx"], "start": legacy["start"], "end": legacy["end"], "color": "green", "note": "old note"},
                {"idx": legacy["idx"], "start": legacy["len"] - 3, "end": legacy["len"] + 5, "color": "pink", "note": ""},
                {"idx": moved["idx"], "start": 2, "end": 32, "color": "blue", "note": "", "q": moved["q"]}])
            pg.evaluate("([k, v]) => localStorage.setItem(k, v)", ["guideHl:" + guide_path, seed])
            reload(pg)
            got = pg.evaluate("__t.marks()")
            old = [g for g in got if g[0].startswith("%d:" % legacy["idx"])]
            check("old-format saved highlight restores to the same words",
                  len(old) == 1 and re.sub(r"\s+", "", old[0][1]) == re.sub(r"\s+", "", legacy["words"]), (got, legacy["words"]))
            check("old-format record that no longer fits its unit is skipped, not clipped",
                  not pg.query_selector("mark.user-hl-pink"), got)
            check("old-format highlight keeps its note indicator",
                  pg.evaluate("!!document.querySelector('mark.user-hl.has-note') && document.querySelector('mark.user-hl.has-note').dataset.note === 'old note'"))
            mv = [g for g in got if g[0].startswith("%d:" % moved["idx"])]
            check("a highlight whose words moved shows on its words", moved["unique"] and len(mv) == 1 and re.sub(r"\s+", "", mv[0][1]) == re.sub(r"\s+", "", moved["q"]), (mv, moved["q"]))
            check("restoring writes nothing on page load (even after moving one)",
                  pg.evaluate("localStorage.getItem(%s)" % json.dumps("guideHl:" + guide_path)) == seed)
            pg.click("mark.user-hl-blue")
            pg.click(".hl-note-popover .hl-note-remove")
            pg.wait_for_timeout(100)
            left = json.loads(pg.evaluate("localStorage.getItem(%s)" % json.dumps("guideHl:" + guide_path)))
            check("the moved highlight can still be removed", len(left) == 2 and not pg.query_selector("mark.user-hl-blue"), left)

            cases = [
                ("plain text into <strong> (p)", r"""() => { var u = Array.from(document.querySelectorAll('p')).find(function (x) {
                     var s = x.querySelector('strong'); return s && !x.closest('mark.user-hl') && !x.querySelector('mark.user-hl') && x.textContent.indexOf(s.textContent) > 15; });
                   var s = u.querySelector('strong'), t = __t.flat(u).text, j = t.indexOf(s.textContent.replace(/\s/g, ' '));
                   var a = __t.at(u, t.slice(j - 12, j), 0), b = __t.at(u, s.textContent.replace(/\s/g, ' '), Math.min(4, s.textContent.length));
                   return [a, b, u]; }"""),
                ("inside a table cell, into <strong>", r"""() => { var u = Array.from(document.querySelectorAll('td')).find(function (x) {
                     var s = x.querySelector('strong'); return s && !x.querySelector('mark.user-hl') && x.textContent.indexOf(s.textContent) > 4; });
                   var s = u.querySelector('strong'), t = __t.flat(u).text, j = t.indexOf(s.textContent.replace(/\s/g, ' '));
                   return [__t.at(u, t.slice(0, 4), 0), __t.at(u, s.textContent.replace(/\s/g, ' '), Math.min(3, s.textContent.length)), u]; }"""),
                ("across two list items", r"""() => { var u = Array.from(document.querySelectorAll('li[data-hl-idx]')).find(function (x) {
                     var n = x.nextElementSibling; return n && n.tagName === 'LI' && n.hasAttribute('data-hl-idx') && x.textContent.length > 30 && n.textContent.length > 30 && !x.querySelector('mark.user-hl'); });
                   var n = u.nextElementSibling, t1 = __t.flat(u).text, t2 = __t.flat(n).text;
                   return [__t.at(u, t1.slice(10, 20), 0), __t.at(n, t2.slice(5, 15), 4), n]; }"""),
                ("in a <dd> with <b>", r"""() => { var u = Array.from(document.querySelectorAll('dd')).find(function (x) {
                     var s = x.querySelector('b, strong'); return s && x.textContent.indexOf(s.textContent) > 10; });
                   var s = u.querySelector('b, strong'), t = __t.flat(u).text, j = t.indexOf(s.textContent.replace(/\s/g, ' '));
                   return [__t.at(u, t.slice(j - 8, j), 0), __t.at(u, s.textContent.replace(/\s/g, ' '), s.textContent.length), u]; }"""),
                ("a table header <th>", r"""() => { var u = Array.from(document.querySelectorAll('th')).find(function (x) { return x.textContent.trim().length > 12; });
                   var t = __t.flat(u).text.trim(); return [__t.at(u, t.slice(0, 6), 0), __t.at(u, t.slice(-6), 6), u]; }"""),
                ("triple-click style (ends at the next block)", r"""() => { var u = Array.from(document.querySelectorAll('p[data-hl-idx]')).find(function (x) {
                     return x.nextElementSibling && x.textContent.length > 40 && !x.querySelector('mark.user-hl') && !x.closest('li'); });
                   return [[u, 0], [u.nextElementSibling, 0], u]; }"""),
            ]
            made = []
            for name, js in cases:
                clear_ui(pg)
                before = dict(pg.evaluate("__t.marks()"))
                # do the selection in-page (Range objects cannot cross the bridge)
                txt = pg.evaluate("""() => { var r = (%s)(); if (!r[0] || !r[1]) return null;
                    var range = __t.select(r[0], r[1]); __t.mouseup(r[2]); return range.toString(); }""" % js)
                pg.wait_for_timeout(120)
                sw = pg.query_selector(".hl-toolbar .hl-swatch-yellow")
                if not txt or not sw:
                    check("highlight %s: toolbar appears" % name, False, "selection=%r toolbar=%s" % (txt, bool(sw)))
                    continue
                sw.click()
                pg.wait_for_timeout(120)
                clear_ui(pg)
                after = pg.evaluate("__t.marks()")
                new = [(k, v) for k, v in after if k not in before]
                covered = new and re.sub(r"\s+", "", txt) in re.sub(r"\s+", "", "".join(v for _, v in new))
                check("highlight %s" % name, bool(covered), "selected=%r marked=%r" % (txt[:80], [v[:60] for _, v in new]))
                made += new
            snapshot = sorted(pg.evaluate("__t.marks()"))
            reload(pg)
            check("after a reload all %d highlights restore with the same words" % len(snapshot),
                  sorted(pg.evaluate("__t.marks()")) == snapshot, set(map(tuple, snapshot)) ^ set(map(tuple, pg.evaluate("__t.marks()"))))

            # ------------------------------------------------------------------ 2. text-box notes
            def note_count():       # notes only: a deleted note leaves a tombstone {id, x} (no text) since 2026-10-15
                return pg.evaluate("(JSON.parse(localStorage.getItem(%s) || '[]')).filter(function (n) { return n && n.t; }).length" % json.dumps("guideNote:" + guide_path))

            # an ordinary click in the text never makes a note
            pos = pg.evaluate(r"""() => { var u = Array.from(document.querySelectorAll('dd')).find(function (x) { return x.textContent.length > 80 && !x.querySelector('mark'); });
                u.scrollIntoView({block: 'center', behavior: 'instant'}); var r = document.createRange(), t = __t.at(u, __t.flat(u).text.slice(20, 30), 3);
                r.setStart(t[0], t[1]); r.setEnd(t[0], t[1] + 1); var b = r.getBoundingClientRect(); return [b.left + 1, b.top + b.height / 2]; }""")
            pg.mouse.click(pos[0], pos[1])
            pg.wait_for_timeout(150)
            check("an ordinary click in the guide makes no note", note_count() == 0 and not pg.query_selector(".gnote"))
            # "Add a note" tool, then click the spot
            pg.click("#gnote-btn")
            check("Add a note tool arms (aria-pressed)", pg.get_attribute("#gnote-btn", "aria-pressed") == "true")
            pg.mouse.click(pos[0], pos[1])
            pg.wait_for_timeout(150)
            ed = pg.query_selector(".gnote-editor textarea")
            check("clicking a spot opens the new-note editor", bool(ed))
            if ed:
                ed.fill("Check orthostatic vitals first")
                pg.click(".gnote-editor .hl-note-save")
                pg.wait_for_timeout(150)
            check("saved note shows as a box with its text", pg.evaluate("!!document.querySelector('.gnote[data-text=\"Check orthostatic vitals first\"]')"))
            check("note saved to guideNote:<page>", note_count() == 1)
            check("the note box adds no text to the guide (unit text unchanged)", pg.evaluate("""() => { var h = document.querySelector('.gnote'); return h.textContent === '' && h.childNodes.length === 0; }"""))
            # "Note" on the selection toolbar
            clear_ui(pg)
            pg.evaluate(r"""() => { var u = Array.from(document.querySelectorAll('p[data-hl-idx]')).find(function (x) { return x.textContent.length > 60 && !x.querySelector('mark, .gnote'); });
                u.scrollIntoView({block: 'center', behavior: 'instant'}); var t = __t.flat(u).text;
                __t.select(__t.at(u, t.slice(5, 15), 0), __t.at(u, t.slice(20, 30), 5)); __t.mouseup(u); }""")
            pg.wait_for_timeout(120)
            nb = pg.query_selector(".hl-toolbar .hl-tbtext")
            check("selection toolbar has a Note button", bool(nb) and nb.inner_text().strip() == "Note")
            if nb:
                nb.click()
                pg.wait_for_timeout(120)
                pg.keyboard.type("Second note")
                pg.keyboard.press("Control+Enter")
                pg.wait_for_timeout(120)
            check("Note from the selection toolbar saves (Ctrl+Enter)", note_count() == 2)
            reload(pg)
            texts = pg.evaluate("Array.from(document.querySelectorAll('.gnote')).map(function (h) { return h.getAttribute('data-text'); })")
            check("both notes come back after a reload", sorted(texts) == ["Check orthostatic vitals first", "Second note"], texts)
            check("highlights still restore exactly with notes on the page", sorted(pg.evaluate("__t.marks()")) == snapshot)
            # keyboard: focus a note, Enter opens its editor; Escape closes and returns focus
            pg.focus(".gnote[data-text='Second note']")
            pg.keyboard.press("Enter")
            pg.wait_for_timeout(100)
            check("Enter on a focused note opens its editor", bool(pg.query_selector(".gnote-editor textarea")))
            pg.keyboard.press("Escape")
            pg.wait_for_timeout(100)
            check("Escape closes the editor and returns focus to the note",
                  not pg.query_selector(".gnote-editor") and pg.evaluate("document.activeElement && document.activeElement.classList.contains('gnote')"))
            # edit by click, commit by clicking elsewhere
            pg.click(".gnote[data-text='Second note']")
            pg.fill(".gnote-editor textarea", "Second note, edited")
            pg.mouse.click(5, 300)
            pg.wait_for_timeout(100)
            reload(pg)
            check("an edit (committed by clicking away) persists", pg.evaluate("!!document.querySelector('.gnote[data-text=\"Second note, edited\"]')"))
            pg.click(".gnote[data-text='Second note, edited']")
            pg.click(".gnote-editor .hl-note-remove")
            pg.wait_for_timeout(100)
            reload(pg)
            check("a deleted note stays deleted", note_count() == 1 and len(pg.query_selector_all(".gnote")) == 1)
            # keyboard: Enter on the tool pins a new note where you are reading; Escape abandons it unsaved
            pg.focus("#gnote-btn")
            pg.keyboard.press("Enter")
            pg.wait_for_timeout(150)
            kb = bool(pg.query_selector(".gnote-editor textarea")) and pg.evaluate("document.activeElement && document.activeElement.tagName === 'TEXTAREA'")
            pg.keyboard.press("Escape")
            pg.wait_for_timeout(100)
            check("keyboard: Enter on Add a note opens a new note's editor, Escape leaves nothing behind",
                  kb and note_count() == 1 and len(pg.query_selector_all(".gnote")) == 1)
            # an iPhone backgrounding the tab (visibilitychange, no pagehide) keeps what was typed
            pg.click(".gnote")
            pg.fill(".gnote-editor textarea", "Typed then the phone locked")
            pg.evaluate("Object.defineProperty(document, 'visibilityState', { configurable: true, get: function () { return 'hidden'; } }); document.dispatchEvent(new Event('visibilitychange'))")
            kept = pg.evaluate("localStorage.getItem(%s)" % json.dumps("guideNote:" + guide_path)) or ""
            check("typed note text is saved when the tab goes to the background (editor still open)",
                  "Typed then the phone locked" in kept and bool(pg.query_selector(".gnote-editor")))
            pg.evaluate("delete document.visibilityState")
            pg.keyboard.press("Escape")
            notes_json = pg.evaluate("localStorage.getItem(%s)" % json.dumps("guideNote:" + guide_path))
            hl_json = pg.evaluate("localStorage.getItem(%s)" % json.dumps("guideHl:" + guide_path))

            # ------------------------------------------------------------------ 3. Add to Pip -> My Review Guide
            if slug:
                clear_ui(pg)
                pg.evaluate(r"""() => { var u = Array.from(document.querySelectorAll('dd')).find(function (x) { return x.textContent.length > 60 && !x.querySelector('mark, .gnote'); });
                    u.scrollIntoView({block: 'center', behavior: 'instant'}); var t = __t.flat(u).text;
                    __t.select(__t.at(u, t.slice(0, 10), 0), __t.at(u, t.slice(30, 40), 10)); __t.mouseup(u); }""")
                try:
                    pg.wait_for_selector(".hl-toolbar .hl-pipbtn", timeout=5000)
                    pg.click(".hl-toolbar .hl-pipbtn")
                    pg.wait_for_timeout(300)
                except Exception:
                    pass
                items = pg.evaluate("JSON.parse(localStorage.getItem('pipReview:%s') || '[]')" % slug)
                check("Add to Pip (selection) saves to pipReview:%s" % slug, len(items) == 1 and items[0].get("t") and items[0].get("a"), items)
                # from a note's editor
                ntext = pg.get_attribute(".gnote", "data-text")
                pg.click(".gnote")
                try:
                    pg.wait_for_selector(".gnote-editor .hl-note-pip:not([hidden])", timeout=5000)
                    pg.click(".gnote-editor .hl-note-pip")
                    pg.wait_for_timeout(300)
                except Exception:
                    pass
                items = pg.evaluate("JSON.parse(localStorage.getItem('pipReview:%s') || '[]')" % slug)
                check("Add to Pip (note) saves the guide sentence plus the note", len(items) == 2 and items[1].get("n") == ntext and items[1].get("t"), items[-1:])
                clear_ui(pg)
                pg.evaluate("""(k) => { var v = JSON.parse(localStorage.getItem(k)); v.unshift({ id: 'bad', t: 5, f: 1 }, null, 'x');
                    localStorage.setItem(k, JSON.stringify(v)); }""", "pipReview:" + slug)
                rv = open_page(c, BASE + "my-review-guide.html?exam=" + slug)
                rv.wait_for_timeout(800)
                body = rv.inner_text("#guide")
                check("my-review-guide.html shows both saved passages", items and all(re.sub(r"\s+", " ", it["t"])[:40] in re.sub(r"\s+", " ", body) for it in items), body[:300])
                check("my-review-guide.html shows the note", ntext in body)
                check("my-review-guide.html has Open in the guide, Quiz me and Print",
                      rv.evaluate("document.querySelectorAll('#guide .bit .btn').length >= 2 && !!document.getElementById('quizAll') && !!document.getElementById('printBtn')"))
                rv.click("#guide .bit .btn")
                rv.wait_for_timeout(600)
                check("Open in the guide opens the study-guide panel", bool(rv.query_selector(".gl-root")))
                rv.close()
            else:
                print("SKIP  Add to Pip / review guide (no pip/data/index.json or folder not in it; run tools/build_pip_data.py)")
            c.close()

            # ------------------------------------------------------------------ 4. accordions
            c = ctx()
            acc_url = BASE + a.accordion_guide.replace(" ", "%20")
            pg = open_page(c, acc_url)
            check("accordion titles (<summary>) are not highlight units", pg.evaluate("document.querySelectorAll('summary[data-hl-x], summary [data-hl-x]').length") == 0)
            dr = pg.evaluate(r"""() => { var sm = Array.from(document.querySelectorAll('details > summary')).find(function (x) { return x.textContent.trim().length > 14; });
                sm.scrollIntoView({block: 'center', behavior: 'instant'}); var t = __t.flat(sm).text, i = t.search(/\S/);
                var a = __t.at(sm, t.slice(i, i + 12), 0), r = document.createRange(); r.setStart(a[0], a[1]); r.setEnd(a[0], a[1] + 1);
                var b = __t.at(sm, t.slice(i, i + 12), 10), r2 = document.createRange(); r2.setStart(b[0], b[1]); r2.setEnd(b[0], b[1] + 1);
                var p = r.getBoundingClientRect(), q = r2.getBoundingClientRect(); sm.id = sm.id || 'dragsum';
                return [p.left + 1, p.top + p.height / 2, q.right - 1, q.top + q.height / 2, sm.id]; }""")
            pg.mouse.move(dr[0], dr[1]); pg.mouse.down(); pg.mouse.move((dr[0] + dr[2]) / 2, dr[3], steps=4); pg.mouse.move(dr[2], dr[3], steps=4); pg.mouse.up()
            pg.wait_for_timeout(200)
            check("a drag that selects words in an accordion title does not open it",
                  pg.evaluate("(id) => !document.getElementById(id).parentElement.open && !!getSelection().toString().trim()", dr[4]))
            clear_ui(pg)
            pg.evaluate("document.querySelector('details > summary').scrollIntoView({block: 'center', behavior: 'instant'})")
            pg.click("details > summary")
            pg.wait_for_timeout(200)
            ok = pg.evaluate(r"""() => { var d = document.querySelector('details[open]'); if (!d) return false;
                var u = Array.from(d.querySelectorAll('[data-hl-idx], [data-hl-x]')).find(function (x) { return x.textContent.length > 40 && !x.querySelector('[data-hl-idx], [data-hl-x]'); });
                if (!u) return false; u.scrollIntoView({block: 'center', behavior: 'instant'}); var t = __t.flat(u).text;
                __t.select(__t.at(u, t.slice(3, 12), 0), __t.at(u, t.slice(20, 30), 6)); __t.mouseup(u); return true; }""")
            pg.wait_for_timeout(120)
            if ok and pg.query_selector(".hl-toolbar .hl-swatch-pink"):
                pg.click(".hl-toolbar .hl-swatch-pink")
                pg.wait_for_timeout(100)
                clear_ui(pg)
                pg.evaluate(r"""() => { var d = document.querySelector('details[open]'), m = d.querySelector('mark.user-hl'), u = m.closest('[data-hl-idx], [data-hl-x]');
                    var t = __t.flat(u).text; __t.select(__t.at(u, t.slice(-12), 0), __t.at(u, t.slice(-12), 8)); __t.mouseup(u); }""")
                pg.wait_for_timeout(120)
                nb = pg.query_selector(".hl-toolbar .hl-tbtext")
                if nb:
                    nb.click(); pg.wait_for_timeout(100); pg.keyboard.type("inside an accordion"); pg.keyboard.press("Control+Enter")
            reload(pg)
            state = pg.evaluate("""() => ({ open: document.querySelectorAll('details[open]').length,
                mark: !!document.querySelector('details mark.user-hl-pink'), note: !!document.querySelector('details .gnote[data-text="inside an accordion"]') })""")
            check("accordions all closed after a reload", state["open"] == 0, state)
            check("a highlight and a note made inside an accordion restore inside it", state["mark"] and state["note"], state)
            c.close()

            # ------------------------------------------------------------------ 5. phone, 390 px
            c = ctx(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True, device_scale_factor=2)
            c.add_init_script("try{localStorage.setItem(%s, %s);localStorage.setItem(%s, %s)}catch(e){}" % (
                json.dumps("guideNote:" + guide_path), json.dumps(notes_json or "[]"), json.dumps("guideHl:" + guide_path), json.dumps(hl_json or "[]")))
            pg = open_page(c, guide_url)
            pg.evaluate("document.querySelector('.gnote').scrollIntoView({block: 'center', behavior: 'instant'})")
            pg.wait_for_timeout(200)
            m = pg.evaluate("""() => { var h = document.querySelector('.gnote'), r = h.getBoundingClientRect();
                return { sw: document.documentElement.scrollWidth, left: r.left, right: r.right, h: r.height }; }""")
            check("phone: no sideways scroll with notes and highlights", m["sw"] <= 390, m)
            check("phone: note box inside the screen and at least 44 px tall", m["left"] >= 0 and m["right"] <= 390 and m["h"] >= 44, m)
            # a touch selection: no mouseup on phones, the toolbar comes from selectionchange
            pg.evaluate(r"""() => { document.dispatchEvent(new PointerEvent('pointerdown', { pointerType: 'touch', bubbles: true }));
                var u = Array.from(document.querySelectorAll('p[data-hl-idx]')).find(function (x) { return x.textContent.length > 60 && !x.querySelector('mark, .gnote') && x.getBoundingClientRect().width > 0; });
                u.scrollIntoView({block: 'center', behavior: 'instant'}); var t = __t.flat(u).text;
                __t.select(__t.at(u, t.slice(0, 8), 0), __t.at(u, t.slice(20, 30), 6)); }""")
            pg.wait_for_timeout(900)
            tb = pg.evaluate("""() => { var t = document.querySelector('.hl-toolbar'); if (!t) return null;
                var r = t.getBoundingClientRect(), small = Array.from(t.querySelectorAll('button')).filter(function (b) { var q = b.getBoundingClientRect(); return q.height < 44 || q.width < 44; }).length;
                return { left: r.left, right: r.right, small: small, n: t.querySelectorAll('button').length }; }""")
            check("phone: a touch selection shows the toolbar (no mouseup needed)", bool(tb), tb)
            check("phone: toolbar fits the screen, every button at least 44 px", bool(tb) and tb["left"] >= 0 and tb["right"] <= 390 and tb["small"] == 0, tb)
            # Add a note from the More menu, then tap a spot
            pg.evaluate("getSelection().removeAllRanges(); document.querySelectorAll('.hl-toolbar').forEach(function (t) { t.remove(); })")
            pg.tap("#more-btn")
            pg.wait_for_timeout(150)
            pg.tap("#gnote-btn")
            pg.wait_for_timeout(150)
            spot = pg.evaluate(r"""() => { var u = Array.from(document.querySelectorAll('dd')).find(function (x) { return x.textContent.length > 80 && !x.querySelector('mark, .gnote'); });
                u.scrollIntoView({block: 'center', behavior: 'instant'}); var t = __t.at(u, __t.flat(u).text.slice(10, 20), 2), r = document.createRange();
                r.setStart(t[0], t[1]); r.setEnd(t[0], t[1] + 1); var b = r.getBoundingClientRect(); return [b.left + 1, b.top + b.height / 2]; }""")
            pg.wait_for_timeout(100)
            pg.touchscreen.tap(spot[0], spot[1])
            pg.wait_for_timeout(200)
            check("phone: More > Add a note, then a tap on the text, opens a new note", bool(pg.query_selector(".gnote-editor textarea")))
            pg.keyboard.press("Escape")
            c.close()

            # ------------------------------------------------------------------ 6. dark mode
            c = ctx()
            c.add_init_script("try{localStorage.setItem('siteTheme','dark');localStorage.setItem(%s, %s);localStorage.setItem(%s, %s)}catch(e){}" % (
                json.dumps("guideNote:" + guide_path), json.dumps(notes_json or "[]"), json.dumps("guideHl:" + guide_path), json.dumps(hl_json or "[]")))
            pg = open_page(c, guide_url)
            bg = pg.evaluate("getComputedStyle(document.querySelector('.gnote')).backgroundColor")
            check("dark mode: note box uses its dark colors", bg == "rgb(46, 39, 18)", bg)
            c.close()

            # ------------------------------------------------------------------ 8. where a new note goes (2026-10-15)
            # the end of the sentence that holds the spot; "e.g.", initials, decimals and "vs." are not ends
            c = ctx()
            c.add_init_script(r"""(function () {
              var T = 'Gram-negative rods, e.g. E. coli and K. pneumoniae, grow at 37.5 degrees vs. 30 in the lab. Second part here; third part follows. Last words without an end';
              new MutationObserver(function (ms, mo) {
                var q = document.querySelector('body > .wrap main p, body > .wrap p');      // beside the guide's first paragraph
                if (!q || document.getElementById('t-sent')) return;
                var p = document.createElement('p'); p.id = 't-sent'; p.textContent = T; q.parentNode.insertBefore(p, q); mo.disconnect();
              }).observe(document, { childList: true, subtree: true });
            })();""")
            pg = open_page(c, guide_url)
            WORD_XY = r"""(w) => { var p = document.getElementById('t-sent'); p.scrollIntoView({block: 'center', behavior: 'instant'});
                var a = __t.at(p, w, 1), r = document.createRange(); r.setStart(a[0], a[1]); r.setEnd(a[0], a[1] + 1);
                var b = r.getBoundingClientRect(); return [b.left + 1, b.top + b.height / 2]; }"""
            AROUND = r"""() => { var p = document.getElementById('t-sent'), h = p.querySelector('.gnote'); if (!h) return null;
                var r = document.createRange(); r.setStart(p, 0); r.setEndBefore(h); var r2 = document.createRange(); r2.setStartAfter(h); r2.setEnd(p, p.childNodes.length);
                return [r.toString(), r2.toString()]; }"""
            for word, before, after in (("coli", "vs. 30 in the lab.", " Second part"), ("Second", "Second part here;", " third part"),
                                        ("without", "without an end", "")):
                clear_ui(pg)
                pg.click("#gnote-btn")
                xy = pg.evaluate(WORD_XY, word)
                pg.mouse.click(xy[0], xy[1])
                pg.wait_for_timeout(150)
                got = pg.evaluate(AROUND)
                check("note placed from inside %r goes to the end of its sentence" % word,
                      bool(got) and got[0].endswith(before) and got[1].startswith(after) and (after or got[1] == ""), got)
                if word == "coli":
                    pg.fill(".gnote-editor textarea", "end of sentence")
                    pg.keyboard.press("Control+Enter")
                    pg.wait_for_timeout(120)
                    rec = pg.evaluate("(JSON.parse(localStorage.getItem(%s) || '[]')).filter(function (n) { return n.t; })[0]" % json.dumps("guideNote:" + guide_path))
                    check("the saved note's before/after context is that of the sentence end", bool(rec) and rec.get("b", "").endswith("in the lab.") and rec.get("a", "").startswith(" Second"), rec)
                    pg.evaluate("document.querySelectorAll('#t-sent .gnote').forEach(function (h) { h.remove(); })")
                else:
                    pg.keyboard.press("Escape")
                    pg.wait_for_timeout(80)
            clear_ui(pg)
            pg.evaluate(r"""() => { var p = document.getElementById('t-sent'); __t.select(__t.at(p, 'third', 0), __t.at(p, 'third', 5)); __t.mouseup(p); }""")
            pg.wait_for_timeout(120)
            if pg.query_selector(".hl-toolbar .hl-tbtext"):
                pg.click(".hl-toolbar .hl-tbtext")
                pg.wait_for_timeout(120)
            got = pg.evaluate(AROUND)
            check("Note on the selection toolbar pins at the end of the sentence the selection ends in",
                  bool(got) and got[0].endswith("third part follows.") and got[1].startswith(" Last"), got)
            pg.keyboard.press("Escape")
            c.close()

            # ------------------------------------------------------------------ 9. Undo after deleting a note (2026-10-15)
            if slug:
                c = ctx()
                pg = open_page(c, guide_url)
                NOTES = "(JSON.parse(localStorage.getItem(%s) || '[]'))" % json.dumps("guideNote:" + guide_path)
                REVIEW = "(JSON.parse(localStorage.getItem('pipReview:%s') || '[]'))" % slug
                NEAR = r"""() => { var h = document.querySelector('.gnote'); if (!h) return null; var u = h.parentElement.closest('[data-hl-idx], [data-hl-x]');
                    var r = document.createRange(); r.setStart(u, 0); r.setEndBefore(h); var r2 = document.createRange(); r2.setStartAfter(h); r2.setEnd(u, u.childNodes.length);
                    return [r.toString().slice(-30), r2.toString().slice(0, 30), h.getAttribute('data-gnote')]; }"""
                xy = pg.evaluate(r"""() => { var u = Array.from(document.querySelectorAll('p[data-hl-idx]')).find(function (x) { return x.textContent.length > 80 && !x.querySelector('mark, .gnote') && x.getClientRects().length; });
                    u.scrollIntoView({block: 'center', behavior: 'instant'}); var a = __t.at(u, __t.flat(u).text.slice(10, 20), 2), r = document.createRange();
                    r.setStart(a[0], a[1]); r.setEnd(a[0], a[1] + 1); var b = r.getBoundingClientRect(); return [b.left + 1, b.top + b.height / 2]; }""")
                pg.click("#gnote-btn")
                pg.mouse.click(xy[0], xy[1])
                pg.wait_for_timeout(150)
                pg.fill(".gnote-editor textarea", "Undo me")
                pg.click(".gnote-editor .hl-note-save")
                pg.wait_for_timeout(120)
                near = pg.evaluate(NEAR)
                pg.click(".gnote")
                try:
                    pg.wait_for_selector(".gnote-editor .hl-note-pip:not([hidden])", timeout=5000)
                    pg.click(".gnote-editor .hl-note-pip")
                    pg.wait_for_timeout(200)
                except Exception:
                    pass
                item = pg.evaluate("(id) => %s.filter(function (x) { return x.id === 'n:' + id; })[0] || null" % REVIEW, near[2] if near else "")
                check("undo setup: the note is in the review list", bool(item) and item.get("n") == "Undo me", item)
                clear_ui(pg)
                pg.click(".gnote")
                pg.click(".gnote-editor .hl-note-remove")
                pg.wait_for_timeout(150)
                t = pg.evaluate("""() => { var t = document.getElementById('site-toast'), b = t && t.querySelector('.site-toast-btn');
                    return t ? { text: t.textContent, role: t.getAttribute('role'), live: t.getAttribute('aria-live'), btn: b ? b.textContent : null,
                                 tag: b ? b.tagName : null, focused: document.activeElement === b } : null; }""")
                check("deleting a note shows 'Note deleted' with a real Undo button in a polite status toast",
                      bool(t) and "Note deleted" in t["text"] and t["btn"] == "Undo" and t["tag"] == "BUTTON" and t["role"] == "status" and t["live"] == "polite", t)
                check("a mouse delete leaves focus alone (Undo not focused)", bool(t) and not t["focused"], t)
                gone = pg.evaluate("(id) => ({ note: !!document.querySelector('.gnote'), rec: %s.some(function (n) { return n.id === id && n.t; }),"
                                   " tomb: %s.some(function (n) { return n.id === id && typeof n.x === 'number' && !n.t; }),"
                                   " item: %s.some(function (x) { return x.id === 'n:' + id && x.t; }) })" % (NOTES, NOTES, REVIEW), near[2])
                check("the delete removes the note and its review item and keeps a tombstone", gone == {"note": False, "rec": False, "tomb": True, "item": False}, gone)
                pg.click("#site-toast .site-toast-btn")
                pg.wait_for_timeout(200)
                back = pg.evaluate(NEAR)
                item2 = pg.evaluate("(id) => %s.filter(function (x) { return x.id === 'n:' + id; })[0] || null" % REVIEW, near[2])
                check("Undo puts the note back at its exact spot", back == near, (near, back))
                check("Undo puts the review item back with its text, note and position",
                      bool(item2) and all(item2.get(k) == item.get(k) for k in ("t", "n", "u", "o", "a", "d")), (item, item2))
                check("Undo leaves no tombstone for the restored note",
                      pg.evaluate("(id) => !%s.some(function (n) { return n.id === id && !n.t; })" % NOTES, near[2]))
                reload(pg)
                check("the restored note survives a reload", pg.evaluate(NEAR) == near)
                # keyboard: Delete note from the keyboard puts focus on Undo; Enter restores and focuses the note
                pg.focus(".gnote")
                pg.keyboard.press("Enter")
                pg.wait_for_timeout(100)
                pg.focus(".gnote-editor .hl-note-remove")
                pg.keyboard.press("Enter")
                pg.wait_for_timeout(150)
                check("keyboard delete: focus goes to Undo", pg.evaluate("document.activeElement && document.activeElement.classList.contains('site-toast-btn')"))
                pg.keyboard.press("Enter")
                pg.wait_for_timeout(200)
                check("keyboard Undo: the note is back and has focus",
                      pg.evaluate(NEAR) == near and pg.evaluate("document.activeElement && document.activeElement.classList.contains('gnote')"))
                # an emptied note committed from the keyboard (here: Enter on the highlights button) is deleted
                # with Undo offered, but focus stays where the student took it
                pg.focus(".gnote")
                pg.keyboard.press("Enter")
                pg.wait_for_timeout(100)
                pg.fill(".gnote-editor textarea", "")
                pg.focus("#hl-panel-btn")
                pg.keyboard.press("Enter")
                pg.wait_for_timeout(200)
                st1 = pg.evaluate("""() => ({ undo: !!document.querySelector('#site-toast .site-toast-btn'), note: !!document.querySelector('.gnote'),
                    onUndo: !!(document.activeElement && document.activeElement.classList.contains('site-toast-btn')),
                    inPanel: !!(document.activeElement && document.activeElement.closest('.hl-panel')) })""")
                check("emptied note committed from the keyboard: deleted with Undo, focus not moved to Undo",
                      st1["undo"] and not st1["note"] and not st1["onUndo"] and st1["inPanel"], st1)
                pg.keyboard.press("Escape")
                pg.click("#site-toast .site-toast-btn")
                pg.wait_for_timeout(200)
                check("...and its Undo still restores it", pg.evaluate(NEAR) == near)
                # removing the item from the review list never deletes the note
                pg.evaluate("(id) => window.PipReview.remove(%s, 'n:' + id)" % json.dumps(slug), near[2])
                reload(pg)
                check("removing the review item keeps the note", pg.evaluate(NEAR) == near)
                c.close()

            # ------------------------------------------------------------------ 10. synced lists merge per item (2026-10-15)
            c = ctx()
            pg = open_page(c, guide_url)
            res = pg.evaluate(r"""() => {
              var M = window.SyncList.merge, out = {}, D = 86400000, now = Date.now();
              function iso(ms) { return new Date(ms).toISOString(); }
              function ids(v) { return JSON.parse(v).filter(function (x) { return x.t; }).map(function (x) { return x.id; }).sort().join(","); }
              var a1 = { id: 'a', t: 'A', at: iso(now - 5 * D) }, a2 = { id: 'a', t: 'A', n: 'edited', at: iso(now - 5 * D), m: iso(now - D) };
              var b = { id: 'b', t: 'B', at: iso(now - 4 * D) }, c2 = { id: 'c', t: 'C', at: iso(now - 2 * D) };
              var L = JSON.stringify([a1, b]), C = JSON.stringify([a2, c2]);
              var r = M(L, C), r2 = M(C, L);
              out.union = ids(r.value) === 'a,b,c' && r.local && r.cloud;
              out.newest = JSON.parse(r.value).filter(function (x) { return x.id === 'a'; })[0].n === 'edited';
              out.symmetric = ids(r2.value) === ids(r.value) && JSON.parse(r2.value).filter(function (x) { return x.id === 'a'; })[0].n === 'edited';
              var again = M(r.value, r2.value); out.settled = !again.local && !again.cloud;
              var del = M(JSON.stringify([a1, b]), JSON.stringify([a1, { id: 'b', x: now - 3600000 }]));
              out.tombstone = ids(del.value) === 'a' && del.local && !del.cloud;
              var readd = M(JSON.stringify([a1, { id: 'b', t: 'B', at: iso(now - 4 * D), m: iso(now) }]), JSON.stringify([a1, { id: 'b', x: now - 3600000 }]));
              out.readd = ids(readd.value) === 'a,b' && !readd.local && readd.cloud;
              var old = M(JSON.stringify([a1]), JSON.stringify([a1, { id: 'z', x: now - 31 * D }]));
              out.prune = !old.local && !old.cloud && JSON.parse(old.value).length === 1;
              out.garbage = M('not json', '[]') === null && M('{}', '[]') === null;
              var s = 'x-test-merge'; localStorage.removeItem('pipReview:' + s);
              var it = { id: 'r1', t: 'a passage', f: 'F', d: 'd.html', at: iso(now) };
              window.PipReview.add(s, it); window.PipReview.remove(s, 'r1');
              var raw = JSON.parse(localStorage.getItem('pipReview:' + s));
              out.removeTomb = window.PipReview.count(s) === 0 && raw.length === 1 && raw[0].id === 'r1' && typeof raw[0].x === 'number' && window.PipReview.slugs().indexOf(s) < 0;
              window.PipReview.add(s, { id: 'r1', t: 'a passage', f: 'F', d: 'd.html', at: iso(now) });
              raw = JSON.parse(localStorage.getItem('pipReview:' + s));
              out.readdClears = window.PipReview.count(s) === 1 && raw.length === 1 && !!raw[0].m;
              localStorage.removeItem('pipReview:' + s);
              out.hooks = typeof window.CloudSyncMerge['pipReview:'] === 'function' && typeof window.CloudSyncMerge['guideNote:'] === 'function';
              return out; }""")
            for k in ("union", "newest", "symmetric", "settled", "tombstone", "readd", "prune", "garbage", "removeTomb", "readdClears", "hooks"):
                check("synced list merge: %s" % k, res.get(k) is True, res)
            c.close()

            # ------------------------------------------------------------------ 11. the selection toolbar from the keyboard (2026-10-15)
            c = ctx()
            pg = open_page(c, guide_url)
            start = pg.evaluate(r"""() => { var u = Array.from(document.querySelectorAll('p[data-hl-idx]')).find(function (x) { return x.textContent.length > 80 && !x.querySelector('mark, .gnote, a') && x.getClientRects().length; });
                u.scrollIntoView({block: 'center', behavior: 'instant'}); u.id = u.id || 'kb-unit'; var t = __t.flat(u).text;
                __t.select(__t.at(u, t.slice(10, 20), 0), __t.at(u, t.slice(10, 20), 6)); return u.id; }""")
            pg.keyboard.press("Shift+ArrowRight")
            pg.wait_for_timeout(250)
            st = pg.evaluate("""() => ({ bar: !!document.querySelector('.hl-toolbar[role=toolbar]'), inBar: !!(document.querySelector('.hl-toolbar') && document.querySelector('.hl-toolbar').contains(document.activeElement)),
                live: Array.from(document.querySelectorAll('.sr-only[aria-live=polite]')).map(function (x) { return x.textContent; }).join(' '), sel: getSelection().toString() })""")
            check("keyboard selection shows the toolbar without taking focus", st["bar"] and not st["inBar"], st)
            check("keyboard selection: a polite live region says how to reach the toolbar", "Tab" in st["live"], st)
            pg.keyboard.press("Tab")
            pg.wait_for_timeout(80)
            f1 = pg.evaluate("""() => { var b = Array.from(document.querySelectorAll('.hl-toolbar button')); return { i: b.indexOf(document.activeElement),
                stops: b.filter(function (x) { return x.tabIndex === 0; }).length }; }""")
            check("Tab moves into the toolbar (first button, one tab stop)", f1 == {"i": 0, "stops": 1}, f1)
            pg.keyboard.press("ArrowRight"); pg.keyboard.press("ArrowRight")
            i2 = pg.evaluate("Array.from(document.querySelectorAll('.hl-toolbar button')).indexOf(document.activeElement)")
            pg.keyboard.press("End")
            iend = pg.evaluate("(function(){var b=Array.from(document.querySelectorAll('.hl-toolbar button'));return [b.indexOf(document.activeElement), b.length];})()")
            pg.keyboard.press("Home")
            ihome = pg.evaluate("Array.from(document.querySelectorAll('.hl-toolbar button')).indexOf(document.activeElement)")
            check("arrow keys, End and Home move between the toolbar's buttons", i2 == 2 and iend[0] == iend[1] - 1 and ihome == 0, (i2, iend, ihome))
            pg.keyboard.press("Escape")
            pg.wait_for_timeout(80)
            esc = pg.evaluate("""(id) => ({ bar: !!document.querySelector('.hl-toolbar'), sel: getSelection().toString(), focus: document.activeElement && document.activeElement.id === id })""", start)
            check("Escape closes the toolbar and returns focus and the selection to where they were",
                  not esc["bar"] and esc["focus"] and esc["sel"].strip() == st["sel"].strip() and bool(esc["sel"].strip()), esc)
            pg.keyboard.press("Shift+ArrowRight")
            pg.wait_for_timeout(250)
            pg.keyboard.press("Tab")
            pg.keyboard.press("Enter")
            pg.wait_for_timeout(200)
            made = pg.evaluate("""() => ({ marks: document.querySelectorAll('mark.user-hl').length, ta: !!(document.activeElement && document.activeElement.classList.contains('hl-note-textarea')) })""")
            check("Enter on a color in the toolbar highlights and opens the note box", made["marks"] >= 1 and made["ta"], made)
            pg.keyboard.press("Escape")
            pg.wait_for_timeout(80)
            check("Escape from that note box puts focus on the new highlight",
                  pg.evaluate("document.activeElement && document.activeElement.matches('mark.user-hl')"))
            # Shift + arrows inside the search box, then a mouse selection: a bare Shift tap must not reopen
            # the toolbar as a keyboard one (no announcement)
            pg.keyboard.press("Escape")
            pg.evaluate("getSelection().removeAllRanges()")
            pg.keyboard.press("/")
            pg.keyboard.type("blood")
            pg.keyboard.press("Shift+ArrowLeft")
            pg.keyboard.press("Escape")
            pg.evaluate(r"""(id) => { var u = document.getElementById(id); var t = __t.flat(u).text;
                __t.select(__t.at(u, t.slice(30, 40), 0), __t.at(u, t.slice(30, 40), 8)); __t.mouseup(u);
                document.querySelectorAll('.sr-only[aria-live=polite]').forEach(function (x) { x.textContent = ''; }); }""", start)
            pg.wait_for_timeout(150)
            pg.keyboard.press("Shift")
            pg.wait_for_timeout(250)
            st2 = pg.evaluate("""() => ({ bar: !!document.querySelector('.hl-toolbar'), kbd: !!(document.querySelector('.hl-toolbar') || {}).__kbd,
                live: Array.from(document.querySelectorAll('.sr-only[aria-live=polite]')).map(function (x) { return x.textContent; }).join('') })""")
            check("Shift + arrows in the search box leave no keyboard-selection state behind", st2["bar"] and not st2["kbd"] and st2["live"] == "", st2)
            pg.keyboard.press("Escape")
            pg.evaluate("getSelection().removeAllRanges()")
            pg.keyboard.press("ControlOrMeta+a")
            pg.wait_for_timeout(250)
            check("select-all on a long guide shows no 'too long' message",
                  pg.evaluate("getSelection().toString().length > 1000") and
                  not pg.evaluate("(function(){var t=document.getElementById('site-toast');return !!t && t.style.opacity==='1' && /too long/.test(t.textContent);})()"))
            c.close()

            c = ctx()
            pg = open_page(c, guide_url)
            ft = pg.evaluate("""() => new Promise(function (res) { var old = document.getElementById('site-toast'); if (old) old.remove();
                window.showToast('First message here', 3000); var t = document.getElementById('site-toast');
                var first = { inPage: !!t && document.body.contains(t), role: t && t.getAttribute('role'), live: t && t.getAttribute('aria-live'), text: t ? t.textContent : null };
                requestAnimationFrame(function () { requestAnimationFrame(function () { res({ first: first, later: t.textContent }); }); }); })""")
            check("a page's first toast: a polite status region already in the page, its text set a frame later",
                  ft["first"] == {"inPage": True, "role": "status", "live": "polite", "text": ""} and ft["later"] == "First message here", ft)
            c.close()

            # ------------------------------------------------------------------ 12. openGuidePanel({quote}) marks the cited sentence (2026-10-15)
            for dark in (False, True):
                c = ctx()
                if dark:
                    c.add_init_script("try{localStorage.setItem('siteTheme','dark')}catch(e){}")
                pg = open_page(c, guide_url)
                pick = pg.evaluate(r"""() => { var hs = Array.from(document.querySelectorAll('h2[id], h3[id]'));
                    for (var i = 0; i < hs.length; i++) { var n = hs[i].nextElementSibling;
                      for (var k = 0; n && k < 6; k++, n = n.nextElementSibling) {
                        if (/^H[1-3]$/.test(n.tagName)) break;
                        var p = n.matches('p') ? n : n.querySelector('p, li');
                        if (!p) continue; var t = p.textContent.replace(/\s+/g, ' ').trim(), m = t.match(/[A-Z][^.!?]{40,160}[.!?]/);
                        if (m) return { id: hs[i].id, s: m[0] }; } }
                    return null; }""")
                if not pick:
                    check("guide panel quote: found a sentence to test with", False)
                    c.close()
                    continue
                quote = "  " + pick["s"].upper().replace(" ", "  ").replace("'", "’") + " "
                rel = a.guide.split("/")[-1]
                def open_q(q):
                    pg.evaluate("(o) => { window.openGuidePanel(o); }",       # an open panel is replaced, as when Pip opens another
                                {"url": rel + "#" + pick["id"], "anchor": pick["id"], "title": "t", "quote": q})
                    pg.wait_for_function("() => { var f = document.querySelector('.gl-frame'); return f && f.closest('.gl-panel').classList.contains('is-ready'); }", timeout=8000)
                    pg.wait_for_timeout(200)
                    return pg.evaluate("""() => { var d = document.querySelector('.gl-frame').contentDocument, ms = Array.from(d.querySelectorAll('mark.gl-quote'));
                        var cs = ms[0] ? d.defaultView.getComputedStyle(ms[0]) : null, r = ms[0] ? ms[0].getBoundingClientRect() : null;
                        return { n: ms.length, text: ms.map(function (m) { return m.textContent; }).join('').replace(/\\s+/g, ' ').trim(),
                                 bg: cs ? cs.backgroundColor : '', shadow: cs ? cs.boxShadow : '', seen: !!r && r.top >= 0 && r.bottom <= d.defaultView.innerHeight,
                                 old: d.querySelectorAll('.gl-mark, .gl-head-mark').length }; }""")
                got = open_q(quote)
                tag = " (dark)" if dark else ""
                qn = lambda x: re.sub(r"\s+", " ", x.replace("\u2019", "'")).strip().lower()
                check("openGuidePanel quote: the cited sentence is marked (case, spaces, curly quotes ignored)%s" % tag,
                      got["n"] >= 1 and qn(got["text"]) == qn(pick["s"]), (got, pick))
                check("openGuidePanel quote: the mark is visible, scrolled into view, not color alone%s" % tag,
                      got["seen"] and got["bg"] not in ("", "rgba(0, 0, 0, 0)", "transparent") and "inset" in got["shadow"], got)
                miss = open_q("this sentence is nowhere in the guide at all, qqq")
                check("openGuidePanel quote not found: no quote mark, the old passage/heading mark as before%s" % tag, miss["n"] == 0 and miss["old"] >= 1, miss)
                c.close()

            # ------------------------------------------------------------------ 7. other pages: no errors, nothing added
            c = ctx()
            for rel, want_tool in ((a.s1_guide, True), ("index.html", False), (a.quiz, False), ("my-review-guide.html", False)):
                pg = open_page(c, BASE + rel.replace(" ", "%20"))
                pg.wait_for_timeout(400)
                check("%s: note tool %s" % (rel, "present" if want_tool else "absent"), bool(pg.query_selector("#gnote-btn")) == want_tool)
                if rel == a.s1_guide:
                    ok = pg.evaluate(r"""() => { var u = Array.from(document.querySelectorAll('[data-hl-idx]')).find(function (x) { return x.textContent.length > 40 && x.getClientRects().length; });
                        u.scrollIntoView({block: 'center', behavior: 'instant'}); var t = __t.flat(u).text; __t.select(__t.at(u, t.slice(0, 6), 0), __t.at(u, t.slice(12, 20), 4)); __t.mouseup(u); return true; }""")
                    pg.wait_for_timeout(120)
                    sw = pg.query_selector(".hl-toolbar .hl-swatch-blue")
                    if sw:
                        sw.click(); pg.wait_for_timeout(100)
                    check("Semester 1 guide: highlighting still works", bool(sw) and len(pg.evaluate("__t.marks()")) == 1)
                pg.close()
            c.close()
            # the homepage's My Review Guide link: hidden in a fresh browser, shown once something is saved
            c = ctx()
            pg = open_page(c, BASE + "index.html")
            check("homepage: My Review Guide link hidden with nothing saved",
                  pg.evaluate("(function(){var l=document.getElementById('myreview-link');return !!l && l.getClientRects().length===0;})()"))
            c.close()
            c = ctx()
            c.add_init_script("try{localStorage.setItem('pipReview:x-test', JSON.stringify([{id:'r1', t:'a passage', f:'F', d:'d.html'}]))}catch(e){}")
            pg = open_page(c, BASE + "index.html")
            check("homepage: My Review Guide link shows once something is saved",
                  pg.evaluate("(function(){var l=document.getElementById('myreview-link');return !!l && !l.hidden && l.getClientRects().length>0;})()"))
            c.close()
            b.close()

    except Exception as e:                 # a step that could not even run is a failure, not a crash
        check("check ran to the end", False, repr(e).splitlines()[0])
    check("no page errors on any page", not errs, errs[:5])
    print("\n%s: %d failure(s)" % ("FAIL" if fails else "PASS", fails))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
