#!/usr/bin/env python3
"""Render the two PDM I Lecture 12 (Ectopy, Escape Rhythms and Supraventricular Dysrhythmias) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 3")
SETS = json.load(open(os.path.join(HERE, "pdm_l12_sets.json"), encoding="utf-8"))
# One palette for the whole of Exam 3, kept in tools/pdm_e3/palette.json.
_P = json.load(open(os.path.join(HERE, "pdm_e3", "palette.json"), encoding="utf-8"))
PALETTE = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Premature atrial complexes", "Bigeminy, trigeminy, quadrigeminy", "Premature junctional complexes",
         "Premature ventricular complexes", "Escape beats", "Junctional rhythms", "Idioventricular rhythms",
         "Wandering atrial pacemaker", "Multifocal atrial tachycardia", "Atrial flutter",
         "Atrial fibrillation", "Supraventricular tachycardia"]
INTRO = (
  "Thirty questions on <b>beats and rhythms that start somewhere other than the sinus node</b>, and more "
  "than half of them show you the strip. Early beats (premature atrial, junctional and ventricular "
  "complexes) and late ones (escape beats); the junctional rhythms, told apart only by rate; the "
  "idioventricular rhythms; and the supraventricular dysrhythmias: wandering atrial pacemaker, multifocal "
  "atrial tachycardia, atrial flutter, atrial fibrillation and the reentry tachycardia called "
  "supraventricular tachycardia. Narrow means the impulse used the normal pathway; wide means it started in "
  "the ventricles. <b>Any value in a question comes with its normal range.</b> "
  "<b>Tap any strip to enlarge it.</b>"
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "ectopy-escape-supraventricular-quiz.html" if n == 1 else "ectopy-escape-supraventricular-quiz-version-2.html"
    html = render(
        title="Ectopy, Escape &amp; Supraventricular Rhythms Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Ectopy, Escape Rhythms &amp; Supraventricular Dysrhythmias",
        sub="Principles of Diagnostic Medicine I &middot; Exam 3 &middot; Lecture 12",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-55s %d questions (%d with a strip)" % (fn, len(qs), sum(1 for q in qs if q.get("img"))))
