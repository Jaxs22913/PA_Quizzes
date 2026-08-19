#!/usr/bin/env python3
"""Render CMS I Lecture 8 Set 1 — the two objective-style Pigmented Skin Lesions quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l8_set1.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Ephelides &amp; lentigines", "Seborrheic keratosis", "Vitiligo",
         "Congenital naevi", "Dysplastic naevi"]
INTRO = ("Thirty questions on pigmented skin lesions, drawn from the syllabus instructional objectives. "
         "Covers ephelides, lentigines including solar and photochemotherapy-induced, seborrheic "
         "keratosis, dermatosis papulosa nigrans, vitiligo, and the melanocytic naevi &mdash; congenital, "
         "naevus spilus, common acquired, blue, pigmented spindle cell, Spitz and dysplastic &mdash; plus "
         "care strategies for adult and elderly populations. This is the objective-style set; the "
         "vignettes are separate. Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "pigmented-skin-lesions-quiz.html" if n == 1 else "pigmented-skin-lesions-quiz-version-2.html"
    html = render(title=f"Pigmented Skin Lesions Quiz {n} &mdash; CMS I Exam 1",
                  h1="Pigmented Skin Lesions",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 8 &middot; Objective set",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
