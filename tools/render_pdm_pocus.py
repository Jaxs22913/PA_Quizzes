#!/usr/bin/env python3
"""Render the two PDM I Lecture 20 (Point-of-Care Ultrasound and Diagnostic Integration) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 4")
SETS = json.load(open(os.path.join(HERE, "pdm_pocus_sets.json"), encoding="utf-8"))
# One palette for the whole of Exam 4, kept in tools/pdm_e4/palette.json (film-viewer slate to x-ray blue).
_P = json.load(open(os.path.join(HERE, "pdm_e4", "palette.json"), encoding="utf-8"))
PALETTE = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Focused against comprehensive", "Indications and contraindications", "Procedural uses", "How ultrasound works",
         "Frequency and probes", "Knobology", "The indicator", "Planes", "Echogenicity", "Artifacts", "Modes",
         "Color Doppler", "Lung findings", "Gallbladder", "Free fluid", "Soft tissue", "Vessels", "Cardiac windows",
         "Lung probes and protocol", "Inferior vena cava", "Protocols", "Integration"]
INTRO = (
  "Thirty questions on <b>point-of-care ultrasound</b>, and about a third of them show you an ultrasound image. "
  "Know how a focused bedside scan differs from a comprehensive study and when it helps, how the machine works "
  "(frequency, depth, gain, the indicator, the planes), the echogenicity words, the artifacts, the modes and color "
  "Doppler, the four cardiac windows, the lung patterns (A lines, B lines, the barcode, the lung point, the spine "
  "sign), the gallbladder, inferior vena cava, free fluid, soft tissue and vein findings, and how a bedside answer "
  "feeds a decision. <b>Tap any image to enlarge it.</b>"
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "point-of-care-ultrasound-quiz.html" if n == 1 else "point-of-care-ultrasound-quiz-version-2.html"
    html = render(
        title="Point-of-Care Ultrasound Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Point-of-Care Ultrasound and Diagnostic Integration",
        sub="Principles of Diagnostic Medicine I &middot; Exam 4 &middot; Lecture 20",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-50s %d questions (%d with an image)" % (fn, len(qs), sum(1 for q in qs if q.get("img"))))
