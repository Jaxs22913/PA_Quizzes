#!/usr/bin/env python3
"""Render the two Principles of Diagnostic Medicine I Lecture 2 quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
SETS = json.load(open(os.path.join(HERE, "pdm_l2_sets.json"), encoding="utf-8"))
# Same palette as Lecture 1: one exam, one colour.
PALETTE = dict(navy="#5a3a5e", indigo="#8a5f8d", gold="#b8862f", ice="#f6f1f6")
CHIPS = ["Radiography &amp; densities", "Computed tomography", "Ultrasound &amp; MRI",
         "Positioning", "Contrast media"]
INTRO = ("Thirty questions on the principles of medical imaging: how each modality forms its "
         "image, the five basic radiographic densities and what attenuation means, Hounsfield "
         "numbers and the window, nuclear medicine, ultrasound and magnetic resonance with their "
         "advantages and their limits, the projections and the three imaging planes, and contrast "
         "media &mdash; which agent, which check before giving it, and which one is "
         "contraindicated when perforation is suspected. Numbers always appear with the scale "
         "that makes them readable and no question asks you to calculate anything, matching how "
         "Professor Reynolds said this course is examined. Every question cites the slide it "
         "came from.")

for n, key in ((1, "set1"), (2, "set2")):
    fn = "medical-imaging-quiz.html" if n == 1 else "medical-imaging-quiz-version-2.html"
    html = render(
        title=f"Principles of Medical Imaging Quiz {n} &mdash; PDM I Exam 1",
        h1="Principles of Medical Imaging",
        sub="Principles of Diagnostic Medicine I &middot; Exam 1 &middot; Lecture 2",
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=SETS[key], already_converted=True, **PALETTE)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(SETS[key]))
