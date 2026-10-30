#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the five CMS I Exam 6 (Respiratory Block Exam I) Master Exams -- 60 questions each,
cumulative over Lectures 33-38 and weighted by scheduled lecture hours (see
tools/cms_e6_masters_partition.py).

Reads Clinical Medicine and Surgery I Exam 6/master-exams.json, written by
tools/cms_e6_masters_partition.py (which puts the keys on a 15/15/15/15 A-D cycle per form -- never
render straight from a pool). Same template, naming and heading as the Exam 5 masters.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Clinical Medicine and Surgery I Exam 6"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
# The Exam 6 palette, taken from render_cms_e6.py ([[site_design_tokens]]: never a new accent hex).
PAL = dict(navy="#7a2d30", indigo="#b45357", gold="#c08a2e", ice="#faefee")
CHIPS = ["Oxygen delivery", "Acid-base", "Asthma", "Chronic obstructive pulmonary disease",
         "Respiratory infections and vaccines", "Tuberculosis and other mycobacteria"]
INTRO = (
  "Sixty questions drawn from all six lectures of the first respiratory block, <b>weighted by "
  "scheduled lecture hours</b>: the three-hour respiratory infections lecture gives sixteen questions "
  "per form, the two-hour acid-base, asthma and chronic obstructive pulmonary disease lectures eleven "
  "each, and the one-hour oxygen delivery and mycobacterial lectures five or six (that slot alternates "
  "from form to form). <b>Forty-eight are patient vignettes</b> and twelve are direct recall, with the "
  "lead-in spread across classifying severity and scores, testing, treatment, next step, patient "
  "education and what to avoid.<br><br>"
  "Many of the questions are not in the topic quizzes, so these forms are worth working even after "
  "those. <b>Four options, A&ndash;D</b>, and every wrong choice gets its own explanation saying why "
  "it is wrong.<br><br>"
  "<b>No question appears in more than one form</b>, so working through all five gives you 300 "
  "distinct questions. Every question cites the slide it came from.")

for name in ("A", "B", "C", "D", "E"):
    fn = "cms-exam-6-master-exam-form-%s.html" % name.lower()
    assert len(S[name]) == 60, "Form %s has %d questions" % (name, len(S[name]))
    qs = [dict(q, opts=[o[:2] for o in q["opts"]]) for q in S[name]]     # misconception tags stay in the JSON
    html = render(title="CMS I Exam 6 Master Exam &mdash; Form %s" % name,
                  h1="Clinical Medicine and Surgery I &mdash; Comprehensive Master Exam",
                  sub="Exam 6 &middot; Respiratory block I, Lectures 33&ndash;38 &middot; "
                      "Form %s" % name,
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=qs, already_converted=True,
                  progress_sig_strict=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[name]))
