#!/usr/bin/env python3
"""Render the two PDM I Lecture 17 (Pulmonary Imaging) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 4")
SETS = json.load(open(os.path.join(HERE, "pdm_l17_sets.json"), encoding="utf-8"))
# One palette for the whole of Exam 4, kept in tools/pdm_e4/palette.json (film-viewer slate to x-ray blue).
_P = json.load(open(os.path.join(HERE, "pdm_e4", "palette.json"), encoding="utf-8"))
PALETTE = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Surface landmarks", "Upper airway films", "The normal chest film", "Film quality", "Systematic read",
         "Computed tomography", "Contrast", "Ultrasound", "Nuclear scans", "Magnetic resonance",
         "Pneumonia", "Pleural effusion", "Pulmonary edema", "Pneumothorax", "Interstitial lung disease"]
INTRO = (
  "Thirty questions on <b>pulmonary imaging</b>, and about a third of them show you the film or the scan. "
  "Find the normal structures and the bony landmarks, tell a technique problem (exposure, inspiration, "
  "rotation, the anteroposterior view) from real disease, pick the right study and know its cautions "
  "(radiograph, ultrasound, computed tomography with or without contrast, the angiogram, the "
  "ventilation/perfusion scan, positron emission tomography, magnetic resonance), and recognize pneumonia, "
  "pleural effusion, pulmonary edema, pneumothorax and interstitial lung disease. "
  "<b>Any value in a question comes with its normal range.</b> <b>Tap any image to enlarge it.</b>"
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "pulmonary-imaging-quiz.html" if n == 1 else "pulmonary-imaging-quiz-version-2.html"
    html = render(
        title="Pulmonary Imaging Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Pulmonary Imaging",
        sub="Principles of Diagnostic Medicine I &middot; Exam 4 &middot; Lecture 17",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-45s %d questions (%d with an image)" % (fn, len(qs), sum(1 for q in qs if q.get("img"))))
