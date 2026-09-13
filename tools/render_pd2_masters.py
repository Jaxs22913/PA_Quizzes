#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the PD2 Exam 1 Master Exams — five cumulative 60-question forms."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Physical Diagnosis 2 Exam 1"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
PAL = dict(navy="#3a5a40", indigo="#5f8a68", gold="#c08a2e", ice="#eef4ef")
CHIPS = ["Clinical reasoning &amp; documentation", "Dermatology",
         "Advanced ocular exam", "Advanced ENT exam"]
INTRO = ("Sixty questions drawn from every lecture in the Exam 1 block, in proportion rather than "
         "at random. <b>Dermatology, ocular and ENT contribute nineteen questions each; clinical "
         "reasoning contributes three</b> &mdash; that lecture is a 24-page introduction, much of "
         "it course mechanics, which the house rule keeps out of questions, so three is an honest "
         "share rather than a shortfall. "
         "<b>No question appears in more than one form</b>, so working through all five gives you "
         "300 distinct questions. These are drawn from the full authored pools, not just the two "
         "topic quizzes per lecture &mdash; over half the written material never reaches a topic "
         "quiz, and this is where it goes. "
         "<b>This is a physical diagnosis course</b>, so the questions ask what you find and what "
         "finding it means; the mechanism behind these conditions belongs to Clinical "
         "Pathophysiology and their management to Clinical Medicine and Surgery. The tuning fork "
         "block carries extra weight throughout, because the class was told it is worth three "
         "points on test day. Every question cites its slide.")

for name in ("A", "B", "C", "D", "E"):
    fn = "pd2-exam-1-master-exam-form-%s.html" % name.lower()
    html = render(title="PD2 Exam 1 Master Exam &mdash; Form %s" % name,
                  h1="Physical Diagnosis 2 &mdash; Comprehensive Master Exam",
                  sub="Exam 1 &middot; Lectures 1&ndash;4 &middot; Form %s" % name,
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-42s %d questions" % (fn, len(S[name])))
