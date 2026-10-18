#!/usr/bin/env python3
"""Pip launch check: loads a BUILT Cloudflare copy of the site (dist/, written by
cloudflare/build.mjs) in headless Chrome, as pa-quizzes.com and as GitHub Pages, with
every other request blocked. Nothing leaves this Mac: Firebase, analytics, the report
forms and the helper Worker (helper.pa-quizzes.com) are never contacted, so no class
data is written and no Claude credit is spent.

    python3 tools/build_pip_data.py && node cloudflare/build.mjs
    ~/Developer/pa-tools/venv/bin/python tools/check_pip_launch.py [dist]

What it checks (one PASS/FAIL line each; exit 1 on any FAIL):
  - dist/ has Pip's code, sprites and generated data, and no Worker source, docs or tools;
  - every "Pip explains" card source passes tools/pip_explain.py check and ships in pip/data/explain/;
  - on pa-quizzes.com: Pip appears on the homepage, a Semester 2 guide and a quiz, the
    window opens (on a computer that can run his brain, on the brain card: a question waits,
    "Not now" lets him answer; the brain is never downloaded and no model file is requested),
    a guide search answers from pip/data, the hide button hides him (and
    it sticks across a reload) and the tab brings him back; the helper address is
    https://helper.pa-quizzes.com; no page errors;
  - on a Semester 1 page (Pip is on every page since 2026-10-11): Pip loads, with no page errors;
  - on jaxs22913.github.io (GitHub Pages): Pip's code is never even requested.

Pages are fixed Microbiology Exam 2 picks (the Pip tests used them since stage 4);
pass --guide / --quiz to use others.
"""
import argparse, json, mimetypes, os, sys
from urllib.parse import unquote, urlsplit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("check_pip_launch: ERROR: playwright is not installed; run it with ~/Developer/pa-tools/venv/bin/python")

SITE_HOSTS = {"pa-quizzes.com": "https://pa-quizzes.com", "jaxs22913.github.io": "https://jaxs22913.github.io"}
HELPER = "https://helper.pa-quizzes.com"
MODEL_HOSTS = ("huggingface.co", "@mlc-ai/web-llm", "binary-mlc-llm-libs")   # where pip/pip-brain.js would fetch the model
TOURS = "try{['tourSeen:quiz','tourSeen:exammode','tourSeen:home'].forEach(k=>localStorage.setItem(k,'1'))}catch(e){}"

fails = 0


def check(name, ok, detail=""):
    global fails
    if not ok:
        fails += 1
    print("%s  %s%s" % ("PASS" if ok else "FAIL", name, "" if ok or not detail else "  -- " + str(detail)[:300]), flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("dist", nargs="?", default=os.path.join(ROOT, "dist"))
    ap.add_argument("--guide", default="Microbiology Exam 2/micro-exam-2-study-guide.html")
    ap.add_argument("--quiz", default="Microbiology Exam 2/diagnosing-infections-quiz.html")
    ap.add_argument("--ask", default="complement fixation", help="a term the guide answers")
    a = ap.parse_args()
    site = os.path.join(os.path.abspath(a.dist), "PA_Quizzes")
    if not os.path.isdir(site):
        sys.exit("check_pip_launch: ERROR: %s has no PA_Quizzes/ folder; run node cloudflare/build.mjs first" % a.dist)

    # ------------------------------------------------------------------ the files
    for rel in ("pip/pip.js", "pip/pip-window.js", "pip/pip-superbrain.js", "pip/data/index.json", "immutable/pip/v1/manifest.json", a.guide, a.quiz):
        check("dist has %s" % rel, os.path.isfile(os.path.join(site, rel)))
    for rel in ("superbrain", "docs", "tools", ".github", "pip/explain"):
        check("dist leaves out %s/" % rel, not os.path.exists(os.path.join(site, rel)))
    # "Pip explains": every card source passes its checks, and what ships matches the sources
    src_dir = os.path.join(ROOT, "pip", "explain")
    srcs = sorted(f for f in os.listdir(src_dir) if f.endswith(".json")) if os.path.isdir(src_dir) else []
    if srcs:
        import subprocess
        r = subprocess.run([sys.executable, os.path.join(HERE, "pip_explain.py"), "check"], capture_output=True, text=True)
        check("pip/explain cards pass tools/pip_explain.py check", r.returncode == 0, (r.stdout.strip().splitlines() or ["?"])[-1])
        shipped = [f for f in srcs if os.path.isfile(os.path.join(site, "pip", "data", "explain", f))]
        check("dist ships pip/data/explain/ for every pip/explain/ exam (%d)" % len(srcs), len(shipped) == len(srcs), sorted(set(srcs) - set(shipped)))
    import check_exam_standard as ces  # the frozen Semester 1 list (import has no side effects)
    s1 = None
    for folder in sorted(ces.FROZEN):
        d = os.path.join(site, folder)
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.endswith(".html") and "theme.js" in open(os.path.join(d, f), encoding="utf-8", errors="replace").read():
                    s1 = folder + "/" + f
                    break
        if s1:
            break
    check("found a Semester 1 page that loads theme.js", s1 is not None)

    def serve(route):
        u = urlsplit(route.request.url)
        if u.hostname not in SITE_HOSTS:
            return route.abort()                       # Firebase, analytics, forms, the helper: never
        path = unquote(u.path)
        if path.endswith("/"):
            path += "index.html"
        if not path.startswith("/PA_Quizzes/"):
            return route.fulfill(status=404, body="not found")
        fs = os.path.normpath(os.path.join(site, path[len("/PA_Quizzes/"):]))
        if not fs.startswith(site) or not os.path.isfile(fs):
            return route.fulfill(status=404, body="not found")
        ctype = mimetypes.guess_type(fs)[0] or "application/octet-stream"
        if ctype.startswith("text/") or ctype in ("application/javascript", "application/json"):
            ctype += "; charset=utf-8"
        with open(fs, "rb") as fh:
            route.fulfill(status=200, body=fh.read(), headers={"content-type": ctype, "cache-control": "no-store"})

    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome", headless=True)

        def page(host):
            c = b.new_context(viewport={"width": 1280, "height": 900}, service_workers="block")
            c.add_init_script(TOURS)
            c.route("**/*", serve)
            pg = c.new_page()
            pg._errs, pg._reqs = [], []
            pg.on("pageerror", lambda e: pg._errs.append(str(e)))
            pg.on("request", lambda r: pg._reqs.append(r.url))
            pg._base = SITE_HOSTS[host] + "/PA_Quizzes/"
            return c, pg

        def go(pg, rel, want_pip=True):
            pg.goto(pg._base + rel.replace(" ", "%20"), wait_until="load")
            if want_pip:
                try:
                    pg.wait_for_function("() => document.querySelector('#pip-dock canvas')", timeout=15000)
                except Exception:
                    return False
                pg.wait_for_timeout(800)
                return True
            pg.wait_for_timeout(3000)                  # theme.js loads Pip after "load"; give it time to (not) happen
            return pg.evaluate("() => !!document.getElementById('pip-dock')")

        def pip_requests(pg):
            return [r for r in pg._reqs if "/PA_Quizzes/pip/" in r or "/immutable/pip/" in r]

        # ------------------------------------------------------------------ pa-quizzes.com
        c, pg = page("pa-quizzes.com")
        check("pa-quizzes.com homepage: Pip appears", go(pg, ""))
        check("pa-quizzes.com guide: Pip appears", go(pg, a.guide))
        pg.evaluate("() => document.getElementById('pip-dock').classList.remove('away')")
        pg.locator("#pip-dock .pip-open").click(force=True)
        try:
            pg.wait_for_selector("#pip-win", state="visible", timeout=8000)
            opened = True
        except Exception:
            opened = False
        check("tapping Pip opens his window", opened)
        if opened:
            pg.wait_for_timeout(1200)
            # On a computer that can run Pip's brain and has none (headless Chrome on a Mac with WebGPU
            # can), the window opens on the brain card and typed questions wait for the student's pick.
            # This check never downloads it: a question is turned away, then "Not now", then the search.
            # (Every request off the site is aborted by serve() anyway; the model check below proves none
            # was even tried.)
            card = pg.locator("#pip-win .pw-brainask")
            for _ in range(24):
                if card.count() or pg.evaluate("() => document.querySelectorAll('#pip-win .pw-msg.pw-pip').length"):
                    break
                pg.wait_for_timeout(250)
            can = pg.evaluate("() => window.PipBrain ? PipBrain.capable().then(c => !!c.ok) : null")
            check("opening the window asks pip/pip-brain.js whether this computer can run the brain", can is not None, can)
            if card.count():
                t = card.inner_text()
                gb = pg.evaluate("() => PipBrain.tiers.standard.gb")
                first = pg.evaluate("() => { const l = document.querySelector('#pip-win .pw-log'); return !!(l.firstElementChild && l.firstElementChild.classList.contains('pw-brainask')); }")
                check("a computer that can run the brain: the window opens on the brain card (%.1f gigabytes, Download my brain, Not now)" % gb,
                      first and ("%.1f gigabytes" % gb) in t and "Download my brain" in t and "Not now" in t, t)
                pg.fill('#pip-win input[aria-label="Ask Pip"]', a.ask)
                pg.press('#pip-win input[aria-label="Ask Pip"]', "Enter")
                pg.wait_for_timeout(1500)
                guide_cards = "() => document.querySelectorAll('#pip-win .pw-card:not(.pw-brainask) .pw-src').length"
                said = pg.evaluate("() => Array.from(document.querySelectorAll('#pip-win .pw-msg.pw-pip')).map(e => e.textContent).join(' | ')")
                check("a question before the pick is not answered (Pip asks for an answer to the card)",
                      pg.evaluate(guide_cards) == 0 and "answer to the card" in said, said)
                pg.locator("#pip-win .pw-brainask .pw-later").click()
                pg.wait_for_timeout(1200)
                check("Not now takes the card away for this open", card.count() == 0)
            else:
                check("no brain card on a computer that cannot run the brain", can is not True, can)
            before = pg.evaluate("() => document.querySelectorAll('#pip-win .pw-src').length")
            pg.fill("#pip-win .pw-in", a.ask)
            pg.press("#pip-win .pw-in", "Enter")
            found = False
            for _ in range(40):
                if pg.evaluate("() => document.querySelectorAll('#pip-win .pw-src').length") > before:
                    found = True
                    break
                pg.wait_for_timeout(250)
            data_ok = any("/PA_Quizzes/pip/data/guide/" in r for r in pg._reqs)
            check("a guide search answers from pip/data (%r)" % a.ask, found and data_ok, "passage shown: %s, guide data fetched: %s" % (found, data_ok))
        # "Ask Pip" on a guide's highlight tools (2026-10-18): select the term in the guide, tap Ask Pip; his
        # window opens on 'What does "<term>" mean?' (shown once, even behind the brain card) and answers from pip/data.
        c2, pg2 = page("pa-quizzes.com")
        if go(pg2, a.guide):
            placed = pg2.evaluate("""(term) => {
                const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
                let n;
                while ((n = w.nextNode())) {
                    const p = n.parentElement, i = n.data.toLowerCase().indexOf(term);
                    if (i < 0 || !p || p.closest('script,style,nav,button,summary,a,#pip-dock,#pip-win,.hl-toolbar')) continue;
                    for (let d = p.closest('details'); d; d = d.parentElement.closest('details')) d.open = true;
                    p.scrollIntoView({block: 'center'});
                    const r = document.createRange(); r.setStart(n, i); r.setEnd(n, i + term.length);
                    if (!r.getBoundingClientRect().width) continue;
                    const s = getSelection(); s.removeAllRanges(); s.addRange(r);
                    p.dispatchEvent(new MouseEvent('mouseup', {bubbles: true}));
                    return n.data.substr(i, term.length);
                }
                return null;
            }""", a.ask)
            btn = pg2.locator('.hl-toolbar button[aria-label="Ask Pip what this means"]')
            try:
                btn.wait_for(state="visible", timeout=8000)
                shown = True
            except Exception:
                shown = False
            check("a guide selection's highlight tools offer Ask Pip", bool(placed) and shown, "term placed: %r, button: %s" % (placed, shown))
            if placed and shown:
                want = "What does “%s” mean?" % placed
                btn.click()
                try:
                    pg2.wait_for_selector("#pip-win", state="visible", timeout=8000)
                    won = True
                except Exception:
                    won = False
                mine = "() => Array.from(document.querySelectorAll('#pip-win .pw-msg.pw-me')).map(e => e.textContent)"
                card2 = pg2.locator("#pip-win .pw-brainask")
                for _ in range(24):
                    if card2.count() or pg2.evaluate("() => document.querySelectorAll('#pip-win .pw-src').length"):
                        break
                    pg2.wait_for_timeout(250)
                if card2.count():
                    check("Ask Pip behind the brain card: the question shows and waits", pg2.evaluate(mine) == [want], pg2.evaluate(mine))
                    pg2.locator("#pip-win .pw-brainask .pw-later").click()
                answered = False
                for _ in range(40):
                    if pg2.evaluate("() => document.querySelectorAll('#pip-win .pw-src').length"):
                        answered = True
                        break
                    pg2.wait_for_timeout(250)
                check("Ask Pip opens his window on %r, asked once, and answers from the guide" % want,
                      won and pg2.evaluate(mine) == [want] and answered,
                      "window: %s, asked: %s, answered: %s" % (won, pg2.evaluate(mine), answered))
            check("no page errors after Ask Pip", not pg2._errs, pg2._errs[:2])
        else:
            check("a guide selection's highlight tools offer Ask Pip", False, "Pip did not load on the guide")
        c2.close()
        pg.add_script_tag(url=pg._base + "pip/pip-superbrain.js")
        ep = pg.evaluate("() => window.PipSuperbrain && PipSuperbrain.endpoint()")
        check("the helper address on pa-quizzes.com is %s" % HELPER, ep == HELPER, ep)
        check("pa-quizzes.com quiz: Pip appears", go(pg, a.quiz))
        # hide and bring back
        pg.evaluate("() => document.getElementById('pip-dock').classList.remove('away')")
        pg.locator("#pip-dock .pip-hide").click(force=True)
        pg.wait_for_timeout(400)
        hid = pg.evaluate("() => getComputedStyle(document.getElementById('pip-dock')).display === 'none' && getComputedStyle(document.getElementById('pip-tab')).display !== 'none'")
        check("the x hides Pip and shows the Pip tab", hid)
        pg.reload(wait_until="load")
        pg.wait_for_timeout(3000)
        still = pg.evaluate("() => { const d = document.getElementById('pip-dock'); return !d || getComputedStyle(d).display === 'none'; }")
        check("hidden stays hidden after a reload", still)
        tab = pg.locator("#pip-tab")
        if tab.count():
            tab.click(force=True)
            pg.wait_for_timeout(600)
        back = pg.evaluate("() => { const d = document.getElementById('pip-dock'); return !!d && getComputedStyle(d).display !== 'none'; }")
        check("the Pip tab brings him back", back)
        helper_calls = [r for r in pg._reqs if r.startswith(HELPER)]
        check("signed out, nothing was sent to the helper", not helper_calls, helper_calls[:3])
        model = [r for r in pg._reqs if any(h in r for h in MODEL_HOSTS)]
        check("no part of the brain's model was requested (it is never downloaded here)", not model, model[:3])
        check("no page errors on pa-quizzes.com", not pg._errs, pg._errs[:2])
        c.close()

        if s1:
            c, pg = page("pa-quizzes.com")
            shown = go(pg, s1)
            check("Semester 1 page (%s): Pip loads, no page errors" % s1, shown and not pg._errs, pg._errs[:2])
            c.close()

        # ------------------------------------------------------------------ GitHub Pages
        c, pg = page("jaxs22913.github.io")
        shown_home = go(pg, "", want_pip=False)
        shown_guide = go(pg, a.guide, want_pip=False)
        reqs = pip_requests(pg)
        check("GitHub Pages: no Pip on the homepage or a guide, and his code is never requested", not shown_home and not shown_guide and not reqs, reqs[:3])
        check("no page errors on GitHub Pages", not pg._errs, pg._errs[:2])
        c.close()
        b.close()

    print("\n%s" % ("%d check(s) FAILED" % fails if fails else "pip launch: all checks passed"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
