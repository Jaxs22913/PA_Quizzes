"""Browser tests for metrics.js + class-stats.js + cloud-sync.js against a fake Firestore (fakefb.js).
Real Firebase hosts are blocked; nothing reaches production. One browser context = one device.
Usage: venv/bin/python test_metrics.py http://127.0.0.1:8791/ [--shots DIR]"""
import sys, json, pathlib, datetime
from playwright.sync_api import sync_playwright

BASE = sys.argv[1]
SHOTS = sys.argv[sys.argv.index('--shots') + 1] if '--shots' in sys.argv else None
HERE = pathlib.Path(__file__).parent
FAKE = (HERE / 'fakefb.js').read_text()
GS = 'https://www.gstatic.com/firebasejs/'
BLOCK = ('googleapis', 'firestore.googleapis', 'identitytoolkit', 'formspree', 'firebaseio', 'google-analytics', 'googletagmanager')
GUIDE = 'Microbiology%20Exam%202/micro-exam-2-study-guide.html'
CRAM = 'Microbiology%20Exam%202/micro-exam-2-cram-sheet.html'
QUIZ = 'Microbiology%20Exam%202/cocci-of-medical-importance-quiz.html'
ARCADE = 'arcade-match.html?deck=anatomy-endocrine-glands'

def route(r):
    u = r.request.url
    if u.startswith(GS):
        return r.fulfill(status=200, content_type='application/javascript', body=FAKE if 'firebase-app-compat' in u else '')
    if any(h in u for h in BLOCK): return r.abort()
    return r.continue_()

CLOCK = """(function(){var off=(+sessionStorage.getItem('__clock')||0)*60000;if(!off)return;var RD=Date,rn=RD.now.bind(RD);
function D(){var a=[].slice.call(arguments);if(!(this instanceof D))return new RD(rn()+off).toString();
return a.length?new (Function.prototype.bind.apply(RD,[null].concat(a)))():new RD(rn()+off);}
D.prototype=RD.prototype;D.now=function(){return rn()+off};D.UTC=RD.UTC;D.parse=RD.parse;window.Date=D;})();"""

def device(b, name, user=None, cloud=None, local=None, test=True, mobile=False, dark=False):
    ctx = b.new_context(viewport={'width': 390, 'height': 844} if mobile else {'width': 1280, 'height': 860}, color_scheme='dark' if dark else 'light')
    ctx.route('**/*', route)
    init = 'window.__FAKE_USER = %s; window.__CLOUD_SEED = %s;' % (json.dumps(user), json.dumps(cloud or {}))
    if test: init += 'window.__PA_METRICS_TEST = true;'
    L = dict({'tourSeen:home': '1', 'tourSeen:quiz': '1', 'tourSeen:planner': '1', 'siteTheme': 'dark' if dark else 'light'}, **(local or {}))
    init += 'if (!sessionStorage.getItem("__seeded")) { sessionStorage.setItem("__seeded","1"); localStorage.clear(); var L = %s; for (var k in L) localStorage.setItem(k, L[k]); }' % json.dumps(L)
    ctx.add_init_script(CLOCK + init)
    pg = ctx.new_page()
    pg.errs = []
    pg.on('pageerror', lambda e: pg.errs.append(str(e)))
    pg.loads = 0
    pg.on('load', lambda: setattr(pg, 'loads', pg.loads + 1))
    pg.dev_name = name
    return ctx, pg

def visit(pg, path, minute, wait=2600):
    pg.evaluate('m => sessionStorage.setItem("__clock", String(m))', minute) if pg.url.startswith('http') else None
    pg.goto(BASE + path, wait_until='domcontentloaded')
    if minute and not pg.evaluate('() => sessionStorage.getItem("__clock")'):
        pg.evaluate('m => sessionStorage.setItem("__clock", String(m))', minute); pg.reload(wait_until='domcontentloaded')
    pg.wait_for_timeout(wait)

def ops(pg):
    return pg.evaluate('() => JSON.parse(sessionStorage.getItem("__fakeops") || "[]")')
def store(pg):
    return pg.evaluate('() => JSON.parse(sessionStorage.getItem("__fakestore") || "{}")')
def lsget(pg, k):
    return pg.evaluate('k => localStorage.getItem(k)', k)
def hide(pg, wait=900):
    pg.evaluate("() => { Object.defineProperty(document, 'visibilityState', { value: 'hidden', configurable: true }); document.dispatchEvent(new Event('visibilitychange')); }")
    pg.wait_for_timeout(wait)

def tally(o):
    w = [x for x in o if x['k'] == 'write']; r = [x for x in o if x['k'] == 'read']; d = [x for x in o if x['k'] == 'denied']
    def coll(x): return x['p'].split('/')[0] + ('/' + x['p'].split('/')[2] if x['p'].startswith('users/') else '')
    by = {}
    for x in w: by.setdefault('write ' + coll(x), 0); by['write ' + coll(x)] += 1
    for x in r: by.setdefault('read ' + coll(x), 0); by['read ' + coll(x)] += x['n']
    for x in d: by.setdefault('denied ' + coll(x), 0); by['denied ' + coll(x)] += 1
    return by

results = []
def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))

def today(minute=0):
    d = datetime.datetime.now() + datetime.timedelta(minutes=minute)
    return d.strftime('%Y-%m-%d')

with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome', headless=True)

    # ---------------------------------------------------------------- S1: a signed-out student's 31-minute session
    ctx, pg = device(b, 'S1')
    timeline = [('index.html', 0), (GUIDE, 2), (CRAM, 5), (ARCADE, 8), ('calendar.html', 12), (QUIZ, 15)]
    for path, m in timeline: visit(pg, path, m)
    pg.evaluate('() => window.markCompleted(20, 25, 600000)')       # the engine's finish hook, under the fake
    pg.wait_for_timeout(600)
    visit(pg, 'review.html', 22)
    pg.evaluate('() => window.PAMetrics.add("review_drill")')       # what startDrill() does (hook checked in source)
    pg.wait_for_timeout(400)
    visit(pg, 'index.html', 31)
    hide(pg)                                                          # the student leaves the tab
    o = ops(pg); t = tally(o); s = store(pg)
    doc = s.get('metrics_daily/' + today(31), {}) or {}
    mw = [x for x in o if x['k'] == 'write' and x['p'].startswith('metrics_daily/')]
    check('S1 metrics writes in a 31-min, 8-page session', len(mw) == 4, '%d writes on pages %s' % (len(mw), [x['page'] for x in mw]))
    check('S1 no metrics reads', not any(x['k'] == 'read' and x['p'].startswith('metrics') for x in o))
    want = {'active_d': 1, 'active_w': 1, 'active_m': 1, 'guide_open': 1, 'cram_open': 1, 'arcade_session': 1, 'planner_day': 1, 'quiz_done': 1, 'q_answered': 25, 'review_drill': 1}
    check('S1 day document holds exactly the session', doc == want, json.dumps(doc))
    check('S1 buffer empty after leaving', lsget(pg, 'local:metrics:buf') is None, str(lsget(pg, 'local:metrics:buf')))
    check('S1 one anonymous sign-in', pg.evaluate('() => +sessionStorage.getItem("__fakeanon")') == 1)
    check('S1 class counter still +25', (s.get('stats/global') or {}).get('questionsCompleted') == 25, str(s.get('stats/global')))
    check('S1 stats_events row still written', sum(1 for k in s if k.startswith('stats_events/')) == 1)
    check('S1 doc has only integer fields', all(isinstance(v, int) for v in doc.values()))
    check('S1 no page errors', not pg.errs, str(pg.errs[:2]))
    S1_TALLY = t
    ctx.close()

    # ---------------------------------------------------------------- S2: opted out (Settings switch / note button)
    ctx, pg = device(b, 'S2', local={'metrics:off': '1'})
    for path, m in [('index.html', 0), (GUIDE, 3), (QUIZ, 11)]: visit(pg, path, m)
    pg.evaluate('() => window.markCompleted(20, 25, 600000)'); pg.wait_for_timeout(600)
    visit(pg, 'index.html', 25); hide(pg)
    o = ops(pg)
    bad = [x['p'] for x in o if x['k'] == 'write' and x['p'].split('/')[0] in ('metrics_daily', 'stats', 'stats_events', 'answer_picks')]
    check('S2 opted out: no counting writes at all', not bad, str(bad[:5]))
    check('S2 opted out: no anonymous sign-in', pg.evaluate('() => +sessionStorage.getItem("__fakeanon")') == 0)
    check('S2 opted out: nothing buffered', lsget(pg, 'local:metrics:buf') is None)
    check('S2 Settings switch shows off', pg.evaluate('''() => { var r = [...document.querySelectorAll(".settings-row")].find(x => /anonymous totals/.test(x.textContent)); return r ? r.querySelector("input").checked : "missing"; }''') is False)
    check('S2 Settings note present', pg.evaluate('() => (document.querySelector(".settings-note") || {}).textContent || ""').startswith('PA Quizzes counts anonymous totals'))
    ctx.close()

    # ---------------------------------------------------------------- S3: developer flag via ?metrics=dev, then ?metrics=on
    ctx, pg = device(b, 'S3')
    visit(pg, 'index.html?metrics=dev', 0)
    check('S3 dev flag stored', lsget(pg, 'metrics:dev') == '1')
    check('S3 URL cleaned', 'metrics=' not in pg.url, pg.url)
    for path, m in [(GUIDE, 3), (QUIZ, 12)]: visit(pg, path, m)
    pg.evaluate('() => window.markCompleted(10, 10, 60000)'); pg.wait_for_timeout(600)
    visit(pg, 'index.html', 25); hide(pg)
    o = ops(pg)
    bad = [x['p'] for x in o if x['k'] == 'write' and x['p'].split('/')[0] in ('metrics_daily', 'stats', 'stats_events', 'answer_picks')]
    check('S3 developer device: no counting writes', not bad, str(bad[:5]))
    check('S3 developer device: no note shown', pg.evaluate('() => !document.getElementById("metrics-note")'))
    visit(pg, 'index.html?metrics=on', 40)
    o = ops(pg)
    check('S3 ?metrics=on resumes counting', any(x['k'] == 'write' and x['p'].startswith('metrics_daily/') for x in o) and lsget(pg, 'metrics:dev') == '0')
    ctx.close()

    # ---------------------------------------------------------------- S4: a Google account's second device (already counted today)
    wk = None
    ctx, pg = device(b, 'S4a')
    visit(pg, 'index.html', 0)
    wk = pg.evaluate('d => window.PAMetrics._weekKey(d)', today())
    ctx.close()
    seen = json.dumps({'active.d': today(), 'active.w': wk, 'active.m': today()[:7]})
    google = {'uid': 'g1', 'isAnonymous': False, 'displayName': 'Test', 'email': 't@example.com'}
    cloud = {'users/g1/kv/metrics%3Aseen': {'value': seen, 'updatedAt': 9e12}}
    ctx, pg = device(b, 'S4', user=google, cloud=cloud)
    visit(pg, 'index.html', 0, wait=3500)
    o = ops(pg)
    check('S4 marker pulled without a reload', pg.loads == 1 and lsget(pg, 'metrics:seen') == seen, 'loads=%d seen=%s' % (pg.loads, lsget(pg, 'metrics:seen')))
    check('S4 already counted today: no write for the visit', not any(x['k'] == 'write' and x['p'].startswith('metrics_daily/') for x in o))
    visit(pg, GUIDE, 12)
    s = store(pg); doc = s.get('metrics_daily/' + today(12), {}) or {}
    check('S4 guide counted, active not counted twice', doc == {'guide_open': 1}, json.dumps(doc))
    check('S4 no metrics:seen re-upload (unchanged)', not any(x['k'] == 'write' and 'metrics%3Aseen' in x['p'] for x in ops(pg)))
    ctx.close()
    # and the account's FIRST device of the day: counted, and the marker goes up to the account
    ctx, pg = device(b, 'S4b', user=google, cloud={})
    visit(pg, 'index.html', 0, wait=3500)
    s = store(pg); doc = s.get('metrics_daily/' + today(), {}) or {}
    check('S4b first device: active counted once', doc == {'active_d': 1, 'active_w': 1, 'active_m': 1}, json.dumps(doc))
    pg.wait_for_timeout(5500)   # cloud-sync's 5 s push throttle
    check('S4b marker pushed to the account', any(x['k'] == 'write' and 'metrics%3Aseen' in x['p'] for x in ops(pg)))
    ctx.close()

    # ---------------------------------------------------------------- S5: rules not published yet, then published
    ctx, pg = device(b, 'S5')
    pg.goto(BASE + 'metrics-test-404.html'); pg.evaluate('() => sessionStorage.setItem("__failcolls", JSON.stringify(["metrics_daily"]))')
    visit(pg, 'index.html', 0)
    visit(pg, GUIDE, 3)
    o = ops(pg)
    check('S5 refused write recorded', any(x['k'] == 'denied' for x in o))
    buf = json.loads(lsget(pg, 'local:metrics:buf') or '{}')
    check('S5 counts kept for later', (buf.get(today(), {}).get('site') or {}).get('active_d') == 1 and (buf.get(today(), {}).get('site') or {}).get('guide_open') == 1, json.dumps(buf))
    pg.evaluate('() => sessionStorage.setItem("__failcolls", "[]")')
    visit(pg, CRAM, 25)   # after the backed-off gap (20 minutes after one failure)
    s = store(pg); doc = s.get('metrics_daily/' + today(25), {}) or {}
    check('S5 everything lands exactly once after publishing', doc == {'active_d': 1, 'active_w': 1, 'active_m': 1, 'guide_open': 1, 'cram_open': 1}, json.dumps(doc))
    check('S5 failure counter reset', lsget(pg, 'local:metrics:fail') is None)
    ctx.close()

    # ---------------------------------------------------------------- S6: automated browser (no test flag) and localhost are never counted
    ctx, pg = device(b, 'S6', test=False)
    for path, m in [('index.html', 0), (GUIDE, 12)]: visit(pg, path, m)
    o = ops(pg)
    check('S6 automated/local browser: no metrics writes, no buffer', not any(x['p'].startswith('metrics') for x in o) and lsget(pg, 'local:metrics:buf') is None)
    ctx.close()

    # ---------------------------------------------------------------- S7: the one-time note
    for dark, mobile in [(False, False), (True, False), (False, True)]:
        ctx, pg = device(b, 'S7', dark=dark, mobile=mobile)
        visit(pg, 'index.html', 0, wait=2600)
        shown = pg.evaluate('() => { var n = document.getElementById("metrics-note"); if (!n) return null; var r = n.getBoundingClientRect(); return { text: n.querySelector("p").textContent, w: r.width, h: r.height, right: r.right, bottom: r.bottom, vw: innerWidth, vh: innerHeight }; }')
        check('S7 note shown on the homepage (%s%s)' % ('dark' if dark else 'light', ' phone' if mobile else ''), shown and shown['right'] <= shown['vw'] and shown['bottom'] <= shown['vh'], json.dumps(shown))
        if SHOTS: pg.screenshot(path='%s/note_%s%s.png' % (SHOTS, 'dark' if dark else 'light', '_phone' if mobile else ''))
        if not dark and not mobile:
            pg.click('#metrics-note .mn-ok'); pg.wait_for_timeout(200)
            check('S7 Got it hides it and remembers', pg.evaluate('() => !document.getElementById("metrics-note")') and lsget(pg, 'metrics:notice') == '1')
            visit(pg, GUIDE, 1)
            check('S7 not shown again', pg.evaluate('() => !document.getElementById("metrics-note")'))
        if mobile:
            pg.click('#metrics-note .mn-off'); pg.wait_for_timeout(300)
            check('S7 Turn off sets the flag and drops the buffer', lsget(pg, 'metrics:off') == '1' and lsget(pg, 'local:metrics:buf') is None and lsget(pg, 'metrics:notice') == '1')
        ctx.close()
    ctx, pg = device(b, 'S7q')
    visit(pg, QUIZ, 0)
    check('S7 note never shown on a quiz page', pg.evaluate('() => !document.getElementById("metrics-note")'))
    ctx.close()

    b.close()

print('\nS1 all Firestore operations in the 31-minute signed-out session:')
for k, v in sorted(S1_TALLY.items()): print('   %-34s %d' % (k, v))
print()
for name, ok, detail in results:
    print(('PASS ' if ok else 'FAIL ') + name + ('' if ok else '   <- ' + detail))
print('\n%d of %d passed' % (sum(1 for r in results if r[1]), len(results)))
sys.exit(0 if all(r[1] for r in results) else 1)
