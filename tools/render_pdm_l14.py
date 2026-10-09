#!/usr/bin/env python3
"""Render the two PDM I Lecture 14 (Axis, Bundle Branch Blocks, and Chamber Enlargement) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 3")
SETS = json.load(open(os.path.join(HERE, "pdm_l14_sets.json"), encoding="utf-8"))
# One palette for the whole of Exam 3, kept in tools/pdm_e3/palette.json (charcoal monitor to ECG red).
_P = json.load(open(os.path.join(HERE, "pdm_e3", "palette.json"), encoding="utf-8"))
PALETTE = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Normal axis", "Left and right axis deviation", "Extreme axis deviation", "Fascicular blocks",
         "Left bundle branch block", "Right bundle branch block", "Right atrial enlargement",
         "Left atrial enlargement", "Right ventricular hypertrophy", "Left ventricular hypertrophy",
         "The systematic 12-lead read"]
INTRO = (
  "Thirty questions on <b>the axis, the bundle branch blocks and chamber enlargement</b>, and about half of "
  "them show you the 12-lead or the lead in question. Read the axis from lead I and aVF; tell a right from a "
  "left bundle branch block by tracing back from the J point in V1; spot P pulmonale and P mitrale; and "
  "apply the right and left ventricular hypertrophy criteria, including the hypertrophy pattern that "
  "mimics an infarction. <b>Any value in a question comes with its normal range.</b> "
  "<b>Tap any tracing to enlarge it.</b>"
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "axis-bundle-branch-blocks-enlargement-quiz.html" if n == 1 else "axis-bundle-branch-blocks-enlargement-quiz-version-2.html"
    html = render(
        title="Axis, Bundle Branch Blocks &amp; Chamber Enlargement Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Axis, Bundle Branch Blocks &amp; Chamber Enlargement",
        sub="Principles of Diagnostic Medicine I &middot; Exam 3 &middot; Lecture 14",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-60s %d questions (%d with a tracing)" % (fn, len(qs), sum(1 for q in qs if q.get("img"))))
