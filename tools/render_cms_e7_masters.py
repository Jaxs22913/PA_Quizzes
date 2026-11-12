#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the five CMS I Exam 7 (Respiratory Block Exam II) Master Exams -- 60 questions each,
cumulative over Lectures 39-45, weighted by scheduled lecture hours (5 per hour; see
tools/cms_e7_masters_partition.py).

Reads Clinical Medicine and Surgery I Exam 7/master-exams.json, written by
tools/cms_e7_masters_partition.py (which puts the keys on a 15/15/15/15 A-D cycle per form -- never
render straight from a pool). Same template, naming and heading as the Exam 6 masters.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Clinical Medicine and Surgery I Exam 7"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
# The Exam 7 palette, taken from render_cms_e7.py ([[site_design_tokens]]: never a new accent hex).
PAL = dict(navy="#5e4123", indigo="#92693f", gold="#c08a2e", ice="#faf6ee")
CHIPS = ["Phases of sleep", "Sleep apnea and hypoventilation", "Inflammatory lung diseases",
         "Pulmonary vascular disease", "Nodules and neoplasms", "Pleural disorders", "Acid-base II"]
INTRO = (
  "Sixty questions drawn from all seven lectures of the second respiratory block, <b>weighted by scheduled "
  "lecture hours</b>: five questions per hour, so ten each from inflammatory lung diseases, pulmonary "
  "vascular disease, nodules and neoplasms, pleural disorders and acid-base II, and five each from the two "
  "one-hour sleep lectures. <b>Forty-eight are patient vignettes</b> and twelve are direct recall, with the "
  "lead-in spread across scores and classification, testing, treatment, next step, compensation, patient "
  "education and what to avoid.<br><br>"
  "Some of the questions are not in the topic quizzes, so these forms are worth working even after "
  "those. <b>Four options, A&ndash;D</b>, and every wrong choice gets its own explanation saying why "
  "it is wrong.<br><br>"
  "<b>No question appears in more than one form</b>, so working through all five gives you 300 "
  "distinct questions. Every question cites the slide it came from.")

for name in ("A", "B", "C", "D", "E"):
    fn = "cms-exam-7-master-exam-form-%s.html" % name.lower()
    assert len(S[name]) == 60, "Form %s has %d questions" % (name, len(S[name]))
    qs = [dict(q, opts=[o[:2] for o in q["opts"]]) for q in S[name]]     # misconception tags stay in the JSON
    html = render(title="CMS I Exam 7 Master Exam &mdash; Form %s" % name,
                  h1="Clinical Medicine and Surgery I &mdash; Comprehensive Master Exam",
                  sub="Exam 7 &middot; Respiratory block II, Lectures 39&ndash;45 &middot; "
                      "Form %s" % name,
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=qs, already_converted=True,
                  progress_sig_strict=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[name]))
