#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the five CMS I Exam 4 (cardiology block I) Master Exams -- 60 questions each.

Reads Clinical Medicine and Surgery I Exam 4/master-exams.json, written by
tools/cms_e4_masters_partition.py (which puts the keys on a 15/15/15/15 A-D
cycle per form -- never render straight from a pool). Same template, naming
and heading as the Exam 2 and Exam 3 masters (render_cms_e2_masters.py,
render_cms_e3_masters.py).
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Clinical Medicine and Surgery I Exam 4"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
# The Exam 4 palette, taken from render_cms_e4.py rather than invented -- see
# [[site_design_tokens]]: never introduce a new accent hex.
PAL = dict(navy="#702d7a", indigo="#a753b4", gold="#c08a2e", ice="#f9eefa")
CHIPS = ["Hypertension", "Hypotension", "Atherosclerosis &amp; lipids",
         "Valvular heart disease", "Coronary artery disease", "Heart failure"]
INTRO = (
  "Sixty questions drawn from all six lectures of the first cardiology block &mdash; <b>ten from "
  "each</b>, so every form is a genuine cumulative rehearsal rather than a sample of whichever "
  "lecture had the most questions written for it. <b>Forty-eight are patient vignettes</b> and "
  "twelve are direct recall, eight and two from every lecture, with the lead-in spread across "
  "diagnosis, testing, treatment, next step, patient education and what to avoid.<br><br>"
  "About half of the questions are not in the topic quizzes, so these forms are worth working "
  "even after those. <b>Four options, A&ndash;D</b>, and every wrong choice gets its own "
  "explanation saying why it is wrong.<br><br>"
  "<b>No question appears in more than one form</b>, so working through all five gives you 300 "
  "distinct questions. Every question cites the slide it came from.")

for name in ("A", "B", "C", "D", "E"):
    fn = "cms-exam-4-master-exam-form-%s.html" % name.lower()
    assert len(S[name]) == 60, "Form %s has %d questions" % (name, len(S[name]))
    html = render(title="CMS I Exam 4 Master Exam &mdash; Form %s" % name,
                  h1="Clinical Medicine and Surgery I &mdash; Comprehensive Master Exam",
                  sub="Exam 4 &middot; Cardiology block I, Lectures 20&ndash;25 &middot; "
                      "Form %s" % name,
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[name]))
