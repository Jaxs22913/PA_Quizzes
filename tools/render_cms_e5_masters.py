#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the five CMS I Exam 5 (Cardiology Block II) Master Exams -- 60 questions each,
cumulative over Lectures 26-32 and weighted by scheduled lecture hours (every lecture
two hours, so 8-9 questions each per form; see tools/cms_e5_masters_partition.py).

Reads Clinical Medicine and Surgery I Exam 5/master-exams.json, written by
tools/cms_e5_masters_partition.py (which puts the keys on a 15/15/15/15 A-D cycle per
form -- never render straight from a pool). Same template, naming and heading as the
Exam 4 masters (render_cms_e4_masters.py).
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Clinical Medicine and Surgery I Exam 5"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
# The Exam 5 palette, taken from render_cms_e5.py rather than invented -- see
# [[site_design_tokens]]: never introduce a new accent hex.
PAL = dict(navy="#7a2d5a", indigo="#b4538c", gold="#c08a2e", ice="#faeef4")
CHIPS = ["Venous disorders", "Arterial occlusive disease &amp; aneurysm", "Cardiomyopathy",
         "Supraventricular arrhythmias", "Blocks &amp; ventricular arrhythmias",
         "Pericardial disease", "Infective endocarditis"]
INTRO = (
  "Sixty questions drawn from all seven lectures of the second cardiology block, <b>weighted by "
  "scheduled lecture hours</b>: every lecture was two hours, so each gives eight or nine questions "
  "per form (the extra slots rotate from form to form). <b>Forty-eight are patient vignettes</b> and "
  "twelve are direct recall, with the lead-in spread across diagnosis, testing, treatment, next step, "
  "patient education and what to avoid.<br><br>"
  "Many of the questions are not in the topic quizzes, so these forms are worth working even after "
  "those. <b>Four options, A&ndash;D</b>, and every wrong choice gets its own explanation saying why "
  "it is wrong.<br><br>"
  "<b>No question appears in more than one form</b>, so working through all five gives you 300 "
  "distinct questions. Every question cites the slide it came from.")

for name in ("A", "B", "C", "D", "E"):
    fn = "cms-exam-5-master-exam-form-%s.html" % name.lower()
    assert len(S[name]) == 60, "Form %s has %d questions" % (name, len(S[name]))
    qs = [dict(q, opts=[o[:2] for o in q["opts"]]) for q in S[name]]     # misconception tags stay in the JSON
    html = render(title="CMS I Exam 5 Master Exam &mdash; Form %s" % name,
                  h1="Clinical Medicine and Surgery I &mdash; Comprehensive Master Exam",
                  sub="Exam 5 &middot; Cardiology block II, Lectures 26&ndash;32 &middot; "
                      "Form %s" % name,
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=qs, already_converted=True,
                  progress_sig_strict=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[name]))
