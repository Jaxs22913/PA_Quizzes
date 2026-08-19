#!/usr/bin/env python3
"""Render CMS I Lecture 5 Set 1 — the two objective-style Dermatological Infestations quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l5_set1.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Scabies &amp; lice", "Bedbugs &amp; fleas", "Stings &amp; bites",
         "Spiders", "Tick-borne illness"]
INTRO = ("Thirty questions on dermatological infestations, drawn from the syllabus instructional "
         "objectives. Covers scabies and the three forms of pediculosis, bedbugs, fleas and tungiasis, "
         "Hymenoptera stings, caterpillars, cutaneous larva migrans, the black widow, brown recluse, "
         "hobo and tarantula spiders, the tick-borne illnesses Lyme disease and Rocky Mountain spotted "
         "fever, and cercarial dermatitis &mdash; plus the primary against secondary lesion distinction "
         "and care across the age range. This is the objective-style set; the vignettes are separate. "
         "Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "dermatological-infestations-quiz.html" if n == 1 else "dermatological-infestations-quiz-version-2.html"
    html = render(title=f"Dermatological Infestations Quiz {n} &mdash; CMS I Exam 1",
                  h1="Dermatological Infestations",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 5 &middot; Objective set",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
