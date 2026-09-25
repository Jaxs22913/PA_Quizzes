#!/usr/bin/env python3
"""Render the two Clinical Pathophysiology I Lecture 3 quizzes.

DEFAULT MODE IS SPLICE (2026-09-25). The shipped pages were rendered from an
older tools/quiz-template engine. A full render now also swaps in the current
engine (class picks, "You vs the class" bars, picture-stem CSS), so it no
longer reproduces the shipped page outside the question data (about 980 diff
lines on 2026-09-25), and the guarded full mode below refuses to write. So by
default this script only replaces the `const QUESTIONS = [...]` literal inside
each existing page with the questions from cp_l3_sets.json (json.dumps
indent=2, ensure_ascii=False, the pages' own format), after asserting the
existing literal round-trips in that format. Everything else on the page is
left byte-for-byte alone. Same design as render_cp_l4.py.

    python3 render_cp_l3.py                 # splice sets into the existing pages
    python3 render_cp_l3.py --full          # full template render; refuses on engine drift
    python3 render_cp_l3.py --full --force  # full render regardless (engine upgrade!)

Chain: cp_l3_pool_[a-d].py -> cp_l3_partition.py -> cp_l3_sets.json -> this.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1")
S = json.load(open(os.path.join(HERE, "cp_l3_sets.json"), encoding="utf-8"))
PAL = dict(navy="#3b2a5e", indigo="#6a4fa3", gold="#c08a2e", ice="#f2eefb")
CHIPS = ["Non-neoplastic growth", "Neoplasia &amp; grading", "Routes of spread",
         "Carcinogenesis", "TNM staging"]
INTRO = ("Thirty questions on abnormal cell growth and differentiation, drawn from the syllabus "
         "instructional objectives. Covers the non-neoplastic abnormalities &mdash; agenesis, "
         "aplasia, hypoplasia, atrophy, hypertrophy, metaplasia and dysplasia &mdash; then what a "
         "neoplasm is, histological grading by differentiation, benign against malignant, the three "
         "routes of tumor spread, the naming rule that turns tissue of origin into sarcoma or "
         "carcinoma, the four categories of gene alteration, chemical carcinogenesis, the "
         "microbial causes with their exact mechanisms, heredity, and the TNM system. "
         "<b>Pathophysiology only</b> &mdash; every question asks what is happening in the tissue "
         "and why, never what you would do about it. Every question is grounded in the slides and cites the slide it came from.")
PFX = "const QUESTIONS = "


def splice(path, questions):
    txt = open(path, encoding="utf-8").read()
    assert txt.count(PFX) == 1, "expected exactly one QUESTIONS literal in %s" % path
    start = txt.index(PFX) + len(PFX)
    old, end = json.JSONDecoder().raw_decode(txt, start)
    assert txt[end] == ";", "QUESTIONS literal not terminated by ';' in %s" % path
    assert json.dumps(old, ensure_ascii=False, indent=2) == txt[start:end], (
        "QUESTIONS literal in %s is not in json.dumps(indent=2) form; refusing to splice" % path)
    new = txt[:start] + json.dumps(questions, ensure_ascii=False, indent=2) + txt[end:]
    # round-trip: the spliced page must parse back to exactly the sets' questions
    back, _ = json.JSONDecoder().raw_decode(new, start)
    assert back == questions, "splice round-trip failed for %s" % path
    if new != txt:
        open(path, "w", encoding="utf-8").write(new)
    return new != txt


if "--full" not in sys.argv:
    for n, key in ((1, "set1"), (2, "set2")):
        fn = "abnormal-cell-growth-quiz.html" if n == 1 else "abnormal-cell-growth-quiz-version-2.html"
        changed = splice(os.path.join(OUT, fn), S[key])
        print("spliced" if changed else "unchanged", fn, "(%d questions)" % len(S[key]))
    sys.exit(0)

for n, key in ((1, "set1"), (2, "set2")):
    fn = "abnormal-cell-growth-quiz.html" if n == 1 else "abnormal-cell-growth-quiz-version-2.html"
    html = render(title=f"Abnormal Cell Growth and Differentiation Quiz {n} &mdash; Clin Path I Exam 1",
                  h1=f"Abnormal Cell Growth and Differentiation &mdash; Quiz {n}",
                  sub="Clinical Pathophysiology I &middot; Exam 1 &middot; Lecture 3",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    dest = os.path.join(OUT, fn)
    if os.path.exists(dest) and "--force" not in sys.argv:
        # GUARD (2026-09-24): the shipped pages were rendered by an older
        # tools/quiz-template engine. Rendering now also swaps in the current
        # engine (class-picks bars, picture-stem CSS, ...), which is a site
        # behaviour change, not a text fix. So compare everything OUTSIDE the
        # QUESTIONS literal and refuse if it differs; question-text changes
        # belong in cp_l3_sets.json + the pools, and are spliced into the page's
        # QUESTIONS literal directly (json.dumps(indent=2, ensure_ascii=False)).
        def _chrome(s):
            i = s.find("const QUESTIONS = ")
            j = s.find("\nconst LTR", i)
            return s if i < 0 or j < 0 else s[:i] + s[j:]
        if _chrome(open(dest, encoding="utf-8").read()) != _chrome(html):
            print("REFUSING to overwrite %s: the rendered page differs from the shipped one outside "
                  "the QUESTIONS literal (engine/template drift). Re-run with --force only if you "
                  "intend to upgrade the engine on this page, then run the load-only checks." % fn)
            continue
    open(dest, "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
