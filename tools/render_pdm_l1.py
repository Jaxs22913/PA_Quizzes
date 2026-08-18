#!/usr/bin/env python3
"""Render the two Principles of Diagnostic Medicine I Lecture 1 quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
SETS = json.load(open(os.path.join(HERE, "pdm_l1_sets.json"), encoding="utf-8"))
# New palette for this exam. #5a3a5e sits 45 RGB units from its nearest
# neighbour (#33235c, PD1 Exam 3), the largest separation available.
PALETTE = dict(navy="#5a3a5e", indigo="#8a5f8d", gold="#b8862f", ice="#f6f1f6")
CHIPS = ["Phases of testing", "Collection tubes", "Cultures &amp; stool studies",
         "Point-of-care testing", "Sensitivity &amp; specificity"]
INTRO = ("Thirty questions on the principles of laboratory diagnostics: the role of testing and "
         "patient counseling, the pretest, intratest and posttest phases, the order of draw and "
         "which tube goes with which test, stool, blood, sputum and throat studies, point-of-care "
         "testing with its regulation, and the statistics &mdash; sensitivity, specificity, "
         "predictive values and pre-test probability. Reference ranges are always supplied and no "
         "question asks you to calculate a predictive value, matching how Professor Reynolds said "
         "this course is examined. Every question cites the slide it came from.")

for n, key in ((1, "set1"), (2, "set2")):
    fn = "lab-diagnostics-quiz.html" if n == 1 else "lab-diagnostics-quiz-version-2.html"
    html = render(
        title=f"Principles of Laboratory Diagnostics Quiz {n} &mdash; PDM I Exam 1",
        h1="Principles of Laboratory Diagnostics",
        sub="Principles of Diagnostic Medicine I &middot; Exam 1 &middot; Lecture 1",
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=SETS[key], already_converted=True, **PALETTE)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(SETS[key]))
