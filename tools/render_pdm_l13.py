#!/usr/bin/env python3
"""Render the two PDM I Lecture 13 (Ventricular Dysrhythmias and Atrioventricular Blocks) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 3")
SETS = json.load(open(os.path.join(HERE, "pdm_l13_sets.json"), encoding="utf-8"))
# One palette for the whole of Exam 3, kept in tools/pdm_e3/palette.json (charcoal monitor to ECG red).
_P = json.load(open(os.path.join(HERE, "pdm_e3", "palette.json"), encoding="utf-8"))
PALETTE = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Ventricular tachycardia", "Torsades de pointes", "Ventricular fibrillation", "Asystole",
         "Pulseless electrical activity", "Ventricular standstill", "Paced rhythms",
         "First-degree block", "Second-degree type I", "Second-degree type II", "Third-degree block"]
INTRO = (
  "Thirty questions on <b>the ventricular rhythms and the atrioventricular heart blocks</b>, and about half "
  "of them show you the rhythm strip. Name the rhythm, find the feature that decides it, and connect it to "
  "what it means for the patient: ventricular tachycardia (with or without a pulse), torsades de pointes "
  "and the prolonged QT interval behind it, ventricular fibrillation, asystole, pulseless electrical "
  "activity, ventricular standstill and the paced rhythms; then the four blocks, told apart by what the "
  "PR interval does. <b>Any value in a question comes with its normal range.</b> "
  "<b>Tap any strip to enlarge it.</b>"
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "ventricular-dysrhythmias-heart-blocks-quiz.html" if n == 1 else "ventricular-dysrhythmias-heart-blocks-quiz-version-2.html"
    html = render(
        title="Ventricular Dysrhythmias &amp; Heart Blocks Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Ventricular Dysrhythmias &amp; Atrioventricular Blocks",
        sub="Principles of Diagnostic Medicine I &middot; Exam 3 &middot; Lecture 13",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-60s %d questions (%d with a strip)" % (fn, len(qs), sum(1 for q in qs if q.get("img"))))
