#!/usr/bin/env python3
"""Render CMS I Lecture 2 Set 1 — the two objective-style General Dermatology I quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l2_set1.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Terminology &amp; description", "Eczema &amp; dermatitis", "Vesiculobullous",
         "Psoriasis", "Alopecia"]
INTRO = ("Thirty questions on General Dermatology I, drawn from the syllabus instructional "
         "objectives. Covers the descriptive vocabulary and diagnostic tools, dermatologic "
         "pharmacology, the eczemas, the dermatitides, vesiculobullous disease, psoriasis, "
         "pityriasis rosea, lichen planus and simplex, the alopecias and xerosis. This is the "
         "objective-style set; the vignette sets are separate. Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "general-dermatology-i-quiz.html" if n == 1 else "general-dermatology-i-quiz-version-2.html"
    html = render(title=f"General Dermatology I Quiz {n} &mdash; CMS I Exam 1",
                  h1="General Dermatology I",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 2 &middot; Objective set",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
