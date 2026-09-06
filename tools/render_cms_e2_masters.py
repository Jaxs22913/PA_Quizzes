#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the five CMS I Exam 2 ophthalmology Master Exams -- 65 questions each.

Built the same way as the Updated Exam 1 derm masters: newly written five-option
items in the reference-question style, not recycled topic-quiz questions. Run
tools/cmsophtho_partition.py first -- it writes the JSON these read, and it is
what puts the correct answer somewhere other than position A.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Clinical Medicine and Surgery I Exam 2"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams-updated.json"), encoding="utf-8"))
PAL = dict(navy="#2d3f7a", indigo="#5566b5", gold="#c08a2e", ice="#eef0fa")
CHIPS = ["Clinical reasoning", "Common disorders", "Neuro-ophthalmology",
         "Acute vision loss", "Chronic vision loss &amp; tumors", "Ocular trauma"]
INTRO = ("Sixty-five newly written questions drawn from all five ophthalmology lectures, in exam "
         "proportions rather than at random &mdash; every lecture contributes to every form, so "
         "this is a genuine cumulative rehearsal and not a sample of whichever deck happened to be "
         "the longest. Mostly patient vignettes, weighted towards <b>diagnosis and treatment</b>. "
         "<b>Five options, A&ndash;E</b>, and every wrong choice gets its own explanation saying why "
         "it is wrong rather than a shared note. <b>No question appears in more than one form</b>, "
         "so working through all five gives you 325 distinct questions. Every question comes from "
         "the slides and cites the one it came from.")

for name in ("A", "B", "C", "D", "E"):
    fn = "cms-exam-2-master-exam-form-%s.html" % name.lower()
    html = render(title="CMS I Exam 2 Master Exam &mdash; Form %s" % name,
                  h1="Clinical Medicine and Surgery I &mdash; Comprehensive Master Exam",
                  sub="Exam 2 &middot; Ophthalmology block, Lectures 10&ndash;14 &middot; Form %s" % name,
                  pill="65 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[name]))
