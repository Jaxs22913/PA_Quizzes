#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Microbiology Exam 1 Master Exams — five cumulative 60s.

Held back until the whole block was in, per [[master_exam_sizing]]. The syllabus
puts Exam 1 at Lectures 1-6, and the sixth (Specific Immunity) was the last to
arrive -- its deck landed on 13 September, which is what unblocks this.

Ten questions per lecture per form, so all six are represented equally in every
sitting.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Microbiology Exam 1"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
PAL = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["General microbiology", "Antibiotics &amp; resistance",
         "Microbe-human interactions", "Transmission", "Nonspecific immunity",
         "Specific immunity"]
INTRO = ("Sixty questions drawn from every lecture in the Exam 1 block, in exam proportions "
         "rather than at random &mdash; <b>each of the six lectures contributes ten questions to "
         "every form</b>, so this is a genuine cumulative rehearsal and not a sample of whichever "
         "topic had the most questions written for it. Questions are reused verbatim from the "
         "topic quizzes, so nothing here can drift from the material it is summarising. "
         "<b>No question appears in more than one form</b>, so working through all five gives you "
         "300 distinct questions. "
         "The two immunity lectures are the heaviest in the block &mdash; Lecture 5 alone runs 93 "
         "slides against eleven objectives &mdash; but they get the same ten slots as everything "
         "else, which is the point of building the forms this way. Every question cites its slide.")

for name in ("A", "B", "C", "D", "E"):
    fn = "micro-exam-1-master-exam-form-%s.html" % name.lower()
    html = render(title="Microbiology Exam 1 Master Exam &mdash; Form %s" % name,
                  h1="Microbiology &mdash; Comprehensive Master Exam",
                  sub="Exam 1 &middot; Lectures 1&ndash;6 &middot; Form %s" % name,
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-46s %d questions" % (fn, len(S[name])))
