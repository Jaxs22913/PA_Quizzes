#!/usr/bin/env python3
"""Render the two Physical Diagnosis 2 Dermatology quizzes.

Palette is the olive already established for Physical Diagnosis 2 Exam 1 by the
Lecture 1 quiz -- one palette per exam folder, shared by every quiz in it.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 1")
SETS = json.load(open(os.path.join(HERE, "pd2_l2_sets.json"), encoding="utf-8"))

PALETTE = dict(navy="#3d4a1f", indigo="#6b7f35", gold="#c2913a", ice="#f4f6ea")
CHIPS = ["Skin structure", "Dermatological history", "Examination technique",
         "Primary &amp; secondary morphology", "Hair &amp; nails"]
INTRO = ("Thirty questions on the dermatological history and physical examination: the "
         "structure and function of the skin, the questions that identify a skin disorder, "
         "the technique of the examination itself, the descriptive vocabulary of distribution, "
         "configuration and morphology, and the abnormal findings of skin, hair and nails. "
         "Every question cites the slide it came from.")

for n, key in ((1, "set1"), (2, "set2")):
    fn = "dermatology-quiz.html" if n == 1 else "dermatology-quiz-version-2.html"
    html = render(
        title=f"Dermatology Quiz {n} &mdash; Physical Diagnosis 2 Exam 1",
        h1="Dermatology",
        sub="Physical Diagnosis 2 &middot; Exam 1 &middot; Lecture 2: Dermatological History &amp; Examination",
        pill="30 questions",
        chips=CHIPS,
        intro=INTRO,
        questions=SETS[key],
        already_converted=True,
        **PALETTE)
    path = os.path.join(OUT, fn)
    open(path, "w", encoding="utf-8").write(html)
    print("wrote", path, "(%d questions)" % len(SETS[key]))
