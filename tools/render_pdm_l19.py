#!/usr/bin/env python3
"""Render the two PDM I Lecture 19 (Acid-Base Balance and Blood Gas Interpretation) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 4")
SETS = json.load(open(os.path.join(HERE, "pdm_l19_sets.json"), encoding="utf-8"))
# One palette for the whole of Exam 4, kept in tools/pdm_e4/palette.json (film-viewer slate to x-ray blue).
_P = json.load(open(os.path.join(HERE, "pdm_e4", "palette.json"), encoding="utf-8"))
PALETTE = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Indications", "Arterial against venous", "The arterial sample", "The blood gas order",
         "Carbon dioxide pressure", "Oxygen pressure and saturation", "The dissociation curve", "Base excess",
         "The step-wise read", "Compensation", "The four disorders", "Potassium", "Calculating the anion gap",
         "An abnormal anion gap"]
INTRO = (
  "Thirty questions on <b>acid-base balance and the arterial blood gas</b>. Know when to order the gas and what "
  "it cannot tell you, why the sample is arterial and how it is handled, what each value on the order measures, "
  "how to read a gas step by step, the expected "
  "findings and causes of the four disorders with their compensation, how pH moves potassium, and the anion gap: "
  "how to work it out and what a high or low gap means. "
  "<b>Every value in a question comes with its normal range</b>; some ask you to work out an anion gap "
  "from the electrolytes given. <b>Tap any image to enlarge it.</b>"
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "acid-base-blood-gas-quiz.html" if n == 1 else "acid-base-blood-gas-quiz-version-2.html"
    html = render(
        title="Acid-Base and Blood Gas Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Acid-Base Balance and Blood Gas Interpretation",
        sub="Principles of Diagnostic Medicine I &middot; Exam 4 &middot; Lecture 19",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-50s %d questions (%d with an image)" % (fn, len(qs), sum(1 for q in qs if q.get("img"))))
