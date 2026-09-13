#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Clinical Pathophysiology I Exam 1 Master Exams — five cumulative 60s.

Held back until the whole block was in, per [[master_exam_sizing]]. The syllabus
puts Exam 1 at Lectures 1-5, and the fifth (ENT) was built on 11 September, which
is what unblocks this.

BUILDING THESE IS WHAT CAUGHT THE ENT TOPIC BEING UNDER-SIZED. It had 2 x 23
where the course spec calls for 2 x 30, so the pool came to 286 rather than 300
and the fifth form came up 14 questions short. The topic was brought up to 60
rather than the forms being quietly shrunk.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Clinical Pathophysiology I Exam 1"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
PAL = dict(navy="#3b2a5e", indigo="#6a4fa3", gold="#c08a2e", ice="#efeaf8")
CHIPS = ["Inflammation", "Dermatology", "Abnormal cell growth",
         "Ophthalmic", "ENT"]
INTRO = ("Sixty questions drawn from every lecture in the Exam 1 block, in exam proportions rather "
         "than at random &mdash; <b>each of the five lectures contributes twelve questions to "
         "every form</b>, so this is a genuine cumulative rehearsal and not a sample of whichever "
         "topic had the most questions written for it. Questions are reused verbatim from the "
         "topic quizzes, so nothing here can drift from the material it is summarising. "
         "<b>No question appears in more than one form</b>, so working through all five gives you "
         "300 distinct questions. "
         "<b>Mechanism only.</b> This course draws its line against Clinical Medicine and Surgery "
         "at pathophysiology against management, and these forms hold that line throughout "
         "&mdash; the ENT lecture's epistaxis slide carries a management column and not one "
         "question is built on it. <b>No vignettes</b>, per the same spec. "
         "One deck error is corrected in place: the slide calls the vertigo of labyrinthitis "
         "&ldquo;episodic&rdquo; and the lecturer corrected that aloud to <b>continuous</b>. "
         "Every question cites its slide.")

for name in ("A", "B", "C", "D", "E"):
    fn = "cp-exam-1-master-exam-form-%s.html" % name.lower()
    html = render(title="Clin Path I Exam 1 Master Exam &mdash; Form %s" % name,
                  h1="Clinical Pathophysiology I &mdash; Comprehensive Master Exam",
                  sub="Exam 1 &middot; Lectures 1&ndash;5 &middot; Form %s" % name,
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-44s %d questions" % (fn, len(S[name])))
