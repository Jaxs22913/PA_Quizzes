"""Pip's anonymous counts (private track until the reveal): the fake Firestore from fakefb.js, real Firebase
blocked. Opens Pip on a study guide, asks a question his cards answer, taps "Helpful?", asks a follow-up
nothing can serve offline, and checks metrics_pip/{today} holds exactly those counts and nothing else.
Usage: venv/bin/python test_pip_metrics.py http://127.0.0.1:8792/ [--shot FILE]"""
import sys, json, pathlib, datetime
from playwright.sync_api import sync_playwright
BASE = sys.argv[1]
SHOT = sys.argv[sys.argv.index('--shot') + 1] if '--shot' in sys.argv else None
FAKE = (pathlib.Path(__file__).parent / 'fakefb.js').read_text()
GS = 'https://www.gstatic.com/firebasejs/'
BLOCK = ('googleapis', 'identitytoolkit', 'formspree', 'firebaseio', 'jsdelivr', 'huggingface', 'helper.pa-quizzes.com', ':8787')
def route(r):
    u = r.request.url
    if u.startswith(GS): return r.fulfill(status=200, content_type='application/javascript', body=FAKE if 'firebase-app-compat' in u else '')
    if any(h in u for h in BLOCK): return r.abort()
    return r.continue_()
GUIDE = 'Microbiology%20Exam%202/micro-exam-2-study-guide.html'
results = []
def check(n, c, d=''): results.append((n, bool(c), d))
with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome', headless=True)
    ctx = b.new_context(viewport={'width': 1280, 'height': 900}); ctx.route('**/*', route)
    ctx.add_init_script('window.__PA_METRICS_TEST = true; if (!sessionStorage.getItem("__seeded")) { sessionStorage.setItem("__seeded","1"); localStorage.clear(); ["home","quiz","planner"].forEach(k => localStorage.setItem("tourSeen:"+k,"1")); localStorage.setItem("metrics:notice","1"); }')
    pg = ctx.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + GUIDE, wait_until='load'); pg.wait_for_timeout(3000)
    check('Pip family registered', pg.evaluate('() => window.PAMetrics.__real === true'))
    pg.evaluate('() => document.querySelector("#pip-dock .pip-open").click()'); pg.wait_for_selector('#pip-win .pw-in', timeout=8000); pg.wait_for_timeout(800)
    pg.fill('#pip-win .pw-in', 'what is type 3 hypersensitivity'); pg.press('#pip-win .pw-in', 'Enter')
    pg.wait_for_selector('#pip-win .pw-explain .pw-help', timeout=10000); pg.wait_for_timeout(600)
    if SHOT: pg.locator('#pip-win').screenshot(path=SHOT)
    pg.click('#pip-win .pw-explain .pw-help .pw-thumb:not(.pw-down)'); pg.wait_for_timeout(300)
    check('thumbs row thanks the student', 'Glad it helped' in pg.evaluate('() => document.querySelector("#pip-win .pw-help").textContent'))
    pg.fill('#pip-win .pw-in', "i still don't get it"); pg.press('#pip-win .pw-in', 'Enter'); pg.wait_for_timeout(2500)
    # send now: pretend the last send was long ago, then one more count triggers it
    pg.evaluate('() => { localStorage.setItem("local:metrics:last", "0"); window.PAMetrics.add("pip_ask", 0); window.PAMetrics.mark("pip_users"); }')
    pg.wait_for_timeout(1500)
    st = pg.evaluate('() => JSON.parse(sessionStorage.getItem("__fakestore") || "{}")')
    day = datetime.date.today().isoformat()
    pip = st.get('metrics_pip/' + day, {})
    print('metrics_pip/%s = %s' % (day, json.dumps(pip, sort_keys=True)))
    print('metrics_daily/%s = %s' % (day, json.dumps(st.get('metrics_daily/' + day, {}), sort_keys=True)))
    want = {'pip_open': 1, 'pip_ask': 2, 'explain_card': 1, 'thumb_up': 1, 'followup': 1, 'pip_users_d': 1, 'pip_users_w': 1, 'pip_users_m': 1}
    got = {k: v for k, v in pip.items() if k not in ('fallback', 'error', 'claude_ask')}
    check('metrics_pip holds the session (the offline follow-up may add a fallback)', got == want, json.dumps(pip))
    check('no text anywhere in the day documents', all(isinstance(v, int) for k, d in st.items() if k.startswith('metrics') for v in d.values()))
    check('guide open counted on the site family', st.get('metrics_daily/' + day, {}).get('guide_open') == 1)
    check('no page errors', not errs, str(errs[:2]))
    b.close()
for n, ok, d in results: print(('PASS ' if ok else 'FAIL ') + n + ('' if ok else '   <- ' + d))
print('%d of %d passed' % (sum(r[1] for r in results), len(results)))
sys.exit(0 if all(r[1] for r in results) else 1)
