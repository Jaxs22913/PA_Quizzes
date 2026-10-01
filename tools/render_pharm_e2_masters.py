#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the five Pharmacology I Exam 2 Master Exams (Forms A-E) from Pharmacology I Exam 2/master-exams.json,
which tools/build_pharm_e2_masters.py writes. Same palette as the Exam 1 masters and the Exam 2 guide."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Pharmacology I Exam 2"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))

PAL = dict(navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
CHIPS = ["Ophthalmic drugs", "ENT drugs", "Antihypertensives", "Lipid-lowering drugs",
         "Myocardial ischemia"]
INTRO = ("Sixty questions drawn from every lecture in the Exam 2 block (Lectures 4 to 8), so each form is a "
         "genuine cumulative rehearsal. <b>Weighted by the timetable</b>: these practice exams follow the "
         "convention of five questions per scheduled lecture hour, and Lectures 4, 5, 6 and 7 were two hours "
         "each while Lecture 8 was one, so each "
         "form carries <b>14 ophthalmic, 13 ENT, 13 antihypertensive, 13 lipid-lowering and 7 myocardial "
         "ischemia</b> questions. Nine hours at five per hour is 45, not 60, so the sixty are apportioned "
         "across those hours rather than invented. "
         "Questions are reused verbatim from the topic quizzes and clinical vignettes, so nothing here can drift "
         "from the material it summarizes, and <b>no question appears in more than one form</b>: all five give "
         "you 300 distinct questions. "
         "<b>Weighted the way the course asked for</b>: mechanism is capped at a fifth of each lecture, so "
         "indications, drug choice, side effects, contraindications and patient education carry the count. "
         "<b>No question turns on a drug dose</b>, per Dr. Wood. Answer positions are balanced inside every "
         "form (fifteen of each letter), and every wrong answer says what it actually belongs to.")

for name in "ABCDE":
    fn = "pharm-exam-2-master-exam-form-%s.html" % name.lower()
    html = render(title="Pharmacology I Exam 2 Master Exam &mdash; Form %s" % name,
                  h1="Pharmacology I &mdash; Comprehensive Master Exam",
                  sub="Exam 2 &middot; Lectures 4&ndash;8 &middot; Form %s" % name,
                  pill="%d questions" % len(S[name]), chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-44s %d questions" % (fn, len(S[name])))
