#!/usr/bin/env python3
"""Render Master Exam set 2 for Pharmacology I Exam 1 -- forms F to J."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Pharmacology I Exam 1"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams-set2.json"), encoding="utf-8"))

PAL = dict(navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
CHIPS = ["Antibacterials", "Antivirals", "Antifungals", "Dermatology medications",
         "ANS &amp; cholinergic", "Adrenergic"]
INTRO = ("A second set of five cumulative forms, <b>written from scratch</b> rather than resampled. "
         "Forms A to E had already used 300 of the 400 questions in the topic quizzes, so drawing "
         "another five from the same pool would mostly have repeated them. Every one of these 300 "
         "questions is new &mdash; none appears in any topic quiz, vignette set or earlier master "
         "form, and none repeats within these five. "
         "<b>They deliberately go after what the first set left alone</b>: dosing schedules and "
         "monitoring, the drug-of-choice lists, spectrum gaps, and the vehicle and potency detail "
         "from the dermatology lecture. "
         "Each form draws from all three lectures in proportion, so all five are genuine cumulative "
         "rehearsals. Every question cites its slide, every wrong answer explains what it actually "
         "belongs to, and <b>no question turns on a drug dose being memorised</b> where the deck "
         "does not state one. Answer positions were assigned by rotation after writing, so no "
         "position is favoured.")

for name in "FGHIJ":
    fn = "pharm-exam-1-master-exam-form-%s.html" % name.lower()
    html = render(title="Pharmacology I Exam 1 Master Exam &mdash; Form %s" % name,
                  h1="Pharmacology I &mdash; Comprehensive Master Exam",
                  sub="Exam 1 &middot; Lectures 1&ndash;3 &middot; Form %s &middot; Set 2" % name,
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-46s %d questions" % (fn, len(S[name])))
