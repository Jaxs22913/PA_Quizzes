#!/usr/bin/env python3
"""Render the two PDM I Lecture 20 (Pulmonary Function Testing and Oxygenation) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 4")
SETS = json.load(open(os.path.join(HERE, "pdm_l20_sets.json"), encoding="utf-8"))
# One palette for the whole of Exam 4, kept in tools/pdm_e4/palette.json (film-viewer slate to x-ray blue).
_P = json.load(open(os.path.join(HERE, "pdm_e4", "palette.json"), encoding="utf-8"))
PALETTE = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Equipment", "Lung volumes", "Lung capacities", "Spirometry", "The forced values", "Indications",
         "Obstructive physiology", "Restrictive physiology", "Volume-time curves", "Flow-volume loops",
         "The stepwise read", "Reports", "Standard and specialized tests", "Oximetry"]
INTRO = (
  "Thirty questions on <b>pulmonary function testing and oxygenation</b>, and about a third of them show you a "
  "tracing, a loop, a film or a report. Know the equipment and what each test measures, the four lung volumes "
  "and four capacities, how spirometry is done and its forced values, why the tests are ordered, how "
  "obstruction and restriction differ on the curves and loops, how to read a report step by step, the role of "
  "each standard test, and how oxygenation is checked. Reports use FEV1 (forced expiratory volume in one second), "
  "FVC (forced vital capacity), TLC (total lung capacity) and DLCO (diffusing capacity of the lung for carbon "
  "monoxide). <b>Any value in a question comes with its normal range or reference value.</b> "
  "<b>Tap any image to enlarge it.</b>"
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "pulmonary-function-testing-quiz.html" if n == 1 else "pulmonary-function-testing-quiz-version-2.html"
    html = render(
        title="Pulmonary Function Testing Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Pulmonary Function Testing and Oxygenation",
        sub="Principles of Diagnostic Medicine I &middot; Exam 4 &middot; Lecture 20",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-50s %d questions (%d with an image)" % (fn, len(qs), sum(1 for q in qs if q.get("img"))))
