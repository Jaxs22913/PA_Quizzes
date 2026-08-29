#!/usr/bin/env python3
"""Render the two Pharmacology I Lecture 2 dermatology quizzes.

Palette is INHERITED from the Pharmacology I Exam 1 quizzes already on the site
(navy #6b3524 / indigo #9c5230 / gold #c9a227 / ice #fbf1e6), per the design
system's rule that a new quiz takes its exam's existing colours rather than
inventing new ones -- the exam should read as one thing across all its files.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Pharmacology I Exam 1")
SETS = json.load(open(os.path.join(HERE, "pharm_l2_derm_sets.json"), encoding="utf-8"))

PALETTE = dict(navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
CHIPS = ["Vehicles and penetration", "Acne", "Topical retinoids",
         "Topical corticosteroids", "Antifungals and antivirals"]
SUB = ("Pharmacology I &middot; Exam 1 &middot; Lecture 2: Dermatology Medications")

for n, (key, fname) in enumerate(
        [("set1", "dermatology-medications-quiz.html"),
         ("set2", "dermatology-medications-quiz-version-2.html")], start=1):
    qs = SETS[key]
    html = R.render(
        title="Dermatology Medications Quiz %d — Pharmacology I Exam 1" % n,
        h1="Dermatology Medications &mdash; Quiz %d" % n,
        sub=SUB,
        pill="%d questions" % len(qs),
        chips=CHIPS,
        intro="",
        questions=qs,
        already_converted=True,
        **PALETTE)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-46s %d questions, %d KB" % (fname, len(qs), len(html) // 1024))
