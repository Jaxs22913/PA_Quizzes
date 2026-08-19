#!/usr/bin/env python3
"""Render CMS I Lecture 4 Set 1 — the two objective-style Cutaneous Bacterial Infections quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l4_set1.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Acne &amp; folliculitis", "Furuncles &amp; abscesses", "Impetigo",
         "Erysipelas &amp; cellulitis", "Necrotizing fasciitis"]
INTRO = ("Thirty questions on cutaneous bacterial infections, drawn from the syllabus instructional "
         "objectives. Covers acne vulgaris and its treatment ladder, folliculitis in its bacterial, "
         "Pseudomonas and pseudofolliculitis forms, furuncles and carbuncles, hidradenitis suppurativa, "
         "erythrasma, impetigo, erysipelas, cellulitis, abscess, acute and chronic paronychia, and "
         "necrotizing fasciitis &mdash; plus the three narrower objectives: methicillin-resistant "
         "Staphylococcus aureus, primary against secondary infection, and care across the age range. "
         "This is the objective-style set; the vignettes are separate. Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "cutaneous-bacterial-infections-quiz.html" if n == 1 else "cutaneous-bacterial-infections-quiz-version-2.html"
    html = render(title=f"Cutaneous Bacterial Infections Quiz {n} &mdash; CMS I Exam 1",
                  h1="Cutaneous Bacterial Infections",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 4 &middot; Objective set",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
