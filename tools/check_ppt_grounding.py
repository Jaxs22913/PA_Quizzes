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

Reads the PowerPoints from the Desktop inbox for each repo "<Class> Exam <N>"
folder, in either layout (see inbox_dir):
    ~/Desktop/Semester <n>/<Class> Inbox/Exam <N>/     (Fall 2026 onward)
    ~/Desktop/<Class> Inbox/Exam <N>/                  (Semester 1, flat)
Decks are found RECURSIVELY under Exam <N>/, skipping any recordings/ folder:
Interpretation of Medical Literature keeps its five decks in
Exam 1/Powerpoints/, and a top-level-only glob screened 0 of its questions
while the run looked clean (audit of 2026-09-22). No pip deps (reads pptx XML).
Paths resolve from the repo root, whatever the cwd.

    python3 tools/check_ppt_grounding.py            # whole site
    python3 tools/check_ppt_grounding.py "Anatomy Exam 4"
"""
import zipfile, re, glob, os, json, sys
from collections import Counter

HOME = os.path.expanduser("~")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
            if decks_in(p):
                return p
            empty.append(p)
    if empty:
        print("  NOTE: %s -- found inbox dir(s) with no .pptx, ignored: %s"
              % (repo_folder, ", ".join(empty)), file=sys.stderr)
    return None

def decks_in(p):
    """Every .pptx under an Exam N/ inbox folder, at any depth, except inside a
    recordings/ folder and Office's "~$" lock files."""
    out = []
    for dirpath, dirnames, filenames in os.walk(p):
        dirnames[:] = [d for d in dirnames if d.lower() != "recordings"]
        out += [os.path.join(dirpath, f) for f in filenames
                if f.lower().endswith(".pptx") and not f.startswith("~$")]
    return sorted(out)

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

# Reviewed and excluded. Each was checked against the slide by hand and the fact
# IS there -- the checker cannot see it because PowerPoint split the text into
# separate runs, so the answer never appears as one literal string.
#   ANS slide 23 prints "Only M(1), M(2), M(3) functionally characterized" with
#   every subscript as its own run, leaving no matchable token.
REVIEWED = {
    ("pharm-exam-1-master-exam-form-h.html", "M1, M2 and M3"),
    ("pharm-exam-1-master-exam-form-f.html", "M1, M2 and M3"),
    ("pharm-exam-1-master-exam-form-g.html", "M1, M2 and M3"),
    ("pharm-exam-1-master-exam-form-i.html", "M1, M2 and M3"),
    ("pharm-exam-1-master-exam-form-j.html", "M1, M2 and M3"),
}

def main(argv):
    roots = argv[1:]
    excluded = 0
    exam_corpus = {}
    decks_read = Counter()
    for folder in sorted(os.listdir(ROOT)):
        if not os.path.isdir(os.path.join(ROOT, folder)) or folder.startswith('.'):
            continue
        if roots and folder not in roots:
            continue
        ib = inbox_dir(folder)
        if ib and os.path.isdir(ib):
            decks = decks_in(ib)
            decks_read[folder] = len(decks)
            txt = ' '.join(deck_text(p) for p in decks)
            if txt.strip():
                exam_corpus[folder] = re.sub(r'\s+', ' ', txt.lower())
    flags = []; screened = Counter(); unparseable = []
    for path in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        f = os.path.relpath(path, ROOT)
        folder = f.split(os.sep)[0]
        if folder not in exam_corpus:
            continue
        text = open(path, encoding='utf-8').read()
        m = re.search(r'const QUESTIONS\s*=\s*', text)
        if not m:
            continue
        # raw_decode, not a non-greedy "(\[.*?\]);" -- that stopped at the first
        # "];" inside a string and the file silently dropped out of the screen.
        try: arr = json.JSONDecoder().raw_decode(text, m.end())[0]
        except ValueError as e:
            unparseable.append((f, str(e)[:70]))
            continue
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
                if (os.path.basename(f), o[c][0]) in REVIEWED:
                    excluded += 1
                    continue
                flags.append((f, qi + 1, o[c][0][:50], q.get('q', '')[:55]))
    print("decks read per exam:", dict(decks_read))
    print("screened per exam:", dict(screened))
    if excluded:
        print(f"reviewed and excluded (verified on the slide by hand): {excluded}")
    for f, err in unparseable:
        print(f"UNPARSEABLE -- NOT SCREENED: {f}  {err}")
    print(f"\nflags to eyeball (correct absent from all decks + a distractor present): {len(flags)}")
    for f, qi, ans, stem in flags:
        print(f"  {f}  Q{qi}: '{ans}'  ::  {stem}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
