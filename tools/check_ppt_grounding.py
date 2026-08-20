"""Screen quiz answers against the course PowerPoints (a factual sanity check).

For every quiz question it scores how well the KEYED correct answer's content
words appear in that exam's slide decks, versus the distractors. It surfaces
high-confidence cases where the correct answer is absent from every deck for
that exam while a distractor is fully present -- i.e. a possible wrong key or
out-of-scope answer -- for a human to eyeball.

Reality check on the signal: it is a screen, not proof. Numbers/measurements
("60 mm Hg to 150 mm Hg"), Greek/symbol terms ("11B-HSD2"), and facts drawn
as slide images or tables routinely flag as false positives even when correct
(verified 2026-07-21: every sampled numeric flag matched its slide exactly).
Treat flags as "go read this slide," never as "this is wrong."

Requires the PowerPoints in the Desktop inbox layout:
    ~/Desktop/<Class> Inbox/Exam <N>/*.pptx
mapped to the repo's "<Class> Exam <N>" folders. No pip deps (reads pptx XML).

    python3 tools/check_ppt_grounding.py            # whole site
    python3 tools/check_ppt_grounding.py "Anatomy Exam 4"
"""
import zipfile, re, glob, os, json, sys
from collections import Counter

HOME = os.path.expanduser("~")
INBOX = {"Anatomy": "Anatomy Inbox", "Physiology": "Physiology Inbox",
         "Physical Diagnosis 1": "Physical Diagnosis 1 Inbox", "CAM Nutrition": "CAM-Nutrition Inbox"}
STOP = set(("the a an of and or to in on at by with for from that which this these those is are was were be as it "
 "its their they them into within between not no only also both each more most than then when where what how why "
 "during over under above below near primary function located include includes structure structures body region "
 "part parts point area surface used serve help form found contains along across around due lies main major minor "
 "left right side upper lower anterior posterior medial lateral superior inferior distal proximal deep small large").split())

def deck_text(path):
    z = zipfile.ZipFile(path)
    sl = [n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)]
    return ' '.join(' '.join(re.findall(r'<a:t>(.*?)</a:t>', z.read(n).decode('utf-8', 'ignore'))) for n in sl)

def inbox_dir(repo_folder):
    """Locate the source deck folder for a repo exam folder.

    Two layouts exist. Semester 1 sat flat at ~/Desktop/<X> Inbox/Exam N, with
    a couple of irregular names (CAM-Nutrition) that INBOX still maps. From
    Fall 2026 the inboxes moved under ~/Desktop/Semester <n>/. The old
    hardcoded map silently returned None for every Fall class, so grounding
    screened 0 questions and still printed a clean result -- a check that
    passes by doing nothing is worse than no check.
    """
    m = re.match(r'(.+?)\s*Exam\s*(\d+)\s*$', repo_folder)
    if not m:
        return None
    cls, num = m.group(1).strip(), m.group(2)
    names = [INBOX.get(cls, cls + " Inbox"), cls + " Inbox"]
    roots = [os.path.join(HOME, "Desktop")] + sorted(
        glob.glob(os.path.join(HOME, "Desktop", "Semester *")))
    # A directory EXISTING is not enough -- it has to contain slides. Found
    # 2026-08-20: ~/Desktop/<Class> Inbox/Exam 1/ still existed from the
    # Semester-1 flat layout but held only a "recordings" folder, and because
    # ~/Desktop is searched before ~/Desktop/Semester */, it shadowed the real
    # inbox. Grounding then screened ZERO slides and printed a clean result --
    # exactly the "passes by doing nothing" failure this function was written to
    # stop, reintroduced by an empty leftover directory.
    empty = []
    for root in roots:
        for name in names:
            p = os.path.join(root, name, "Exam " + num)
            if not os.path.isdir(p):
                continue
            if glob.glob(os.path.join(p, "*.pptx")):
                return p
            empty.append(p)
    if empty:
        print("  NOTE: %s -- found inbox dir(s) with no .pptx, ignored: %s"
              % (repo_folder, ", ".join(empty)), file=sys.stderr)
    return None

def toks(s):
    return [w for w in re.findall(r'[a-z]{4,}', s.lower()) if w not in STOP] + re.findall(r'\d+', s)

def found(t, d):
    for st in {t, t.rstrip('s'), re.sub(r'ies$', 'y', t), re.sub(r'es$', '', t), t[:6]}:
        if len(st) >= 4 and st in d:
            return True
    return False

def cov(opt, d):
    t = set(toks(opt))
    return 1.0 if not t else sum(1 for w in t if found(w, d)) / len(t)

def main(argv):
    roots = argv[1:]
    exam_corpus = {}
    for repo in glob.glob("*/"):
        folder = repo.rstrip('/')
        if roots and folder not in roots:
            continue
        ib = inbox_dir(folder)
        if ib and os.path.isdir(ib):
            txt = ' '.join(deck_text(p) for p in glob.glob(ib + '/*.pptx')
                           if not os.path.basename(p).startswith('~$'))
            if txt.strip():
                exam_corpus[folder] = re.sub(r'\s+', ' ', txt.lower())
    flags = []; screened = Counter()
    for f in glob.glob("**/*.html", recursive=True):
        folder = f.split('/')[0]
        if folder not in exam_corpus:
            continue
        m = re.search(r'const QUESTIONS\s*=\s*(\[.*?\]);', open(f, encoding='utf-8').read(), re.S)
        if not m:
            continue
        try: arr = json.loads(m.group(1))
        except Exception: continue
        d = exam_corpus[folder]
        for qi, q in enumerate(arr):
            o, c = q.get('opts'), q.get('c')
            if not (isinstance(o, list) and len(o) == 4 and isinstance(c, int)):
                continue
            screened[folder] += 1
            ct = list(set(toks(o[c][0])))
            if len(ct) < 2:
                continue
            cc = sum(1 for w in ct if found(w, d)) / len(ct)
            best = max((cov(o[j][0], d) for j in range(4) if j != c), default=0)
            if cc == 0 and best >= 0.75:
                flags.append((f, qi + 1, o[c][0][:50], q.get('q', '')[:55]))
    print("screened per exam:", dict(screened))
    print(f"\nflags to eyeball (correct absent from all decks + a distractor present): {len(flags)}")
    for f, qi, ans, stem in flags:
        print(f"  {f}  Q{qi}: '{ans}'  ::  {stem}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
