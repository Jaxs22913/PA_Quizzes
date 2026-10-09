#!/usr/bin/env python3
"""Render the two PDM I Lecture 15 (Ischemia, Injury, and Infarction) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 3")
SETS = json.load(open(os.path.join(HERE, "pdm_l15_sets.json"), encoding="utf-8"))
# One palette for the whole of Exam 3, kept in tools/pdm_e3/palette.json (charcoal monitor to ECG red).
_P = json.load(open(os.path.join(HERE, "pdm_e3", "palette.json"), encoding="utf-8"))
PALETTE = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Coronary arteries", "J point and baseline", "Hyperacute T waves", "ST depression",
         "ST elevation", "Pathologic Q waves", "Reciprocal changes", "Lead localization",
         "Posterior infarction", "Right ventricular involvement"]
INTRO = (
  "Thirty questions on <b>reading ischemia, injury and infarction on the 12-lead</b>, and about half of "
  "them show you the tracing. Hyperacute T waves come first, ST depression means the subendocardium "
  "is ischemic, ST elevation means the full wall is injured, and pathologic Q waves mean tissue has died. "
  "Expect the coronary arteries and what each supplies, the J point and the baseline you measure it "
  "against, reciprocal changes, which leads look at which wall, and the two extra tracings: posterior "
  "leads (V7 to V9) for isolated ST depression in V1 to V4, and V4R for an inferior infarction that may "
  "involve the right ventricle. <b>Tap any tracing to enlarge it.</b>"
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "ischemia-infarction-quiz.html" if n == 1 else "ischemia-infarction-quiz-version-2.html"
    html = render(
        title="Ischemia, Injury &amp; Infarction Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Ischemia, Injury &amp; Infarction",
        sub="Principles of Diagnostic Medicine I &middot; Exam 3 &middot; Lecture 15",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-50s %d questions (%d with a tracing)" % (fn, len(qs), sum(1 for q in qs if q.get("img"))))
