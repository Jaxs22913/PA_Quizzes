"""Load-only console sweep with the fake Firestore (no real Firebase): every top-level page plus one guide,
cram sheet, quiz and master of each Semester 2 folder and a sample of Semester 1. Reports page errors and
console.error lines, and that PAMetrics is the real module on each page that loads theme.js."""
import sys, json, pathlib, random, urllib.parse
from playwright.sync_api import sync_playwright
REPO = pathlib.Path.home() / 'Developer/PA_Quizzes'
BASE = sys.argv[1]
FAKE = (pathlib.Path(__file__).parent / 'fakefb.js').read_text()
GS = 'https://www.gstatic.com/firebasejs/'
BLOCK = ('googleapis', 'identitytoolkit', 'formspree', 'firebaseio', 'google-analytics', 'googletagmanager')
def route(r):
    u = r.request.url
    if u.startswith(GS): return r.fulfill(status=200, content_type='application/javascript', body=FAKE if 'firebase-app-compat' in u else '')
    if any(h in u for h in BLOCK): return r.abort()
    return r.continue_()
random.seed(7)
pages = sorted(p.name for p in REPO.glob('*.html'))
pages += ['arcade-match.html?deck=anatomy-endocrine-glands', 'arcade-study.html?deck=anatomy-endocrine-glands', 'arcade-sprint.html?deck=anatomy-endocrine-glands', 'arcade-learn.html?deck=anatomy-endocrine-glands']
for d in sorted(x for x in REPO.iterdir() if x.is_dir() and any(x.glob('*.html')) and x.name not in ('tools', 'cloudflare', 'docs', 'group-quizzes', 'icons', 'audio')):
    hs = sorted(d.glob('*.html'))
    pick = [h for h in hs if 'study-guide' in h.name][:1] + [h for h in hs if 'cram-sheet' in h.name][:1]
    pick += [h for h in hs if 'master' in h.name.lower()][:1]
    rest = [h for h in hs if h not in pick]
    pick += random.sample(rest, min(2, len(rest)))
    pages += [str(h.relative_to(REPO)) for h in pick]
bad, real, total = [], 0, 0
with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome', headless=True)
    ctx = b.new_context(); ctx.route('**/*', route)
    ctx.add_init_script('window.__PA_METRICS_TEST = true; try { ["home","quiz","planner"].forEach(k => localStorage.setItem("tourSeen:"+k, "1")); } catch (e) {}')
    for pth in pages:
        pg = ctx.new_page(); errs = []
        pg.on('pageerror', lambda e: errs.append('pageerror: ' + str(e)[:160]))
        pg.on('console', lambda m: errs.append('console.error: ' + m.text[:160]) if m.type == 'error' else None)
        try:
            pg.goto(BASE + urllib.parse.quote(pth, safe='/?=&'), wait_until='load', timeout=30000); pg.wait_for_timeout(1800)
        except Exception as e:
            errs.append('load: ' + str(e)[:120])
        st = pg.evaluate('() => ({ theme: !!document.querySelector(\'script[src$="theme.js"]\'), real: !!(window.PAMetrics && window.PAMetrics.__real) })')
        total += 1
        if st['theme']: real += 1 if st['real'] else 0
        errs = [e for e in errs if 'net::ERR_FAILED' not in e and 'Failed to load resource' not in e]
        if st['theme'] and not st['real']: errs.append('PAMetrics is still the queue')
        if errs: bad.append((pth, errs[:3]))
        pg.close()
    b.close()
print('%d pages loaded; PAMetrics live on %d of the pages that load theme.js' % (total, real))
for pth, e in bad: print('ISSUE', pth, e)
print('pages with issues:', len(bad))
