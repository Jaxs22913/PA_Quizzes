#!/usr/bin/env python3
"""Render the two Principles of Diagnostic Medicine I Lecture 3 quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
SETS = json.load(open(os.path.join(HERE, "pdm_l3_sets.json"), encoding="utf-8"))
# Same palette as Lectures 1 and 2: one exam, one colour.
PALETTE = dict(navy="#5a3a5e", indigo="#8a5f8d", gold="#b8862f", ice="#f6f1f6")
CHIPS = ["Skin testing &amp; KOH", "Biopsy &amp; cultures", "Ophthalmology",
         "Ear, nose &amp; throat", "Head &amp; neck imaging"]
INTRO = ("Thirty questions on diagnostic testing for dermatologic, ophthalmologic and ear, nose "
         "and throat disorders: which question each test actually answers, reading a potassium "
         "hydroxide preparation, the biopsy techniques and the melanoma rule that protects "
         "Breslow depth, ultrasound for abscess versus cellulitis, the Levine method for wound "
         "culture, the four ophthalmic tests and what each finding means, rapid streptococcal "
         "testing against throat culture, audiometry and the tympanogram types, and computed "
         "tomography against magnetic resonance in the head and neck. Numbers always appear with "
         "the scale that makes them readable and no question asks you to calculate anything, "
         "matching how Professor Reynolds said this course is examined. "
         "<b>This is the student version of the deck, and its licensed figures have been "
         "stripped</b> &mdash; several slides carry a title and speaker notes but no picture. "
         "Where the notes describe the missing figure, the question cites the notes so you can "
         "see where the fact came from. Every question cites its slide.")

for n, key in ((1, "set1"), (2, "set2")):
    fn = "derm-ent-ophtho-testing-quiz.html" if n == 1 else "derm-ent-ophtho-testing-quiz-version-2.html"
    html = render(
        title=f"Diagnostic Testing for Derm, Ophtho &amp; ENT Quiz {n} &mdash; PDM I Exam 1",
        h1="Diagnostic Testing for Dermatologic, Ophthalmologic and ENT Disorders",
        sub="Principles of Diagnostic Medicine I &middot; Exam 1 &middot; Lecture 3",
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=SETS[key], already_converted=True, **PALETTE)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(SETS[key]))
