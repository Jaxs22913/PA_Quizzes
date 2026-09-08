#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the five CMS I Exam 3 (ENT) Master Exams -- 50 questions each.

Run tools/cmsent_partition.py first: it writes the JSON these read, and it is
what moves the correct answer off position A.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Clinical Medicine and Surgery I Exam 3"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
# The Exam 3 palette, taken from render_cms_e3.py rather than invented -- see
# [[site_design_tokens]]: never introduce a new accent hex.
PAL = dict(navy="#462d7a", indigo="#7455b5", gold="#c08a2e", ice="#f2eefa")
CHIPS = ["Clinical reasoning", "External &amp; middle ear", "Inner ear &amp; hearing",
         "Nose &amp; sinuses", "Neck masses", "Oral cavity &amp; throat"]
INTRO = (
  "Fifty newly written questions drawn from all five lectures of the ear, nose and throat block "
  "&mdash; <b>ten from each</b>, so every form is a genuine cumulative rehearsal rather than a "
  "sample of whichever lecture had the most questions written for it. Patient vignettes in the "
  "style of the worked examples, with the lead-in varied: what finding is expected, what is the "
  "most likely cause, what is the most direct method, what is the next step, what additional "
  "finding is likely.<br><br>"
  "<b>Four options, A&ndash;D.</b> Every option carries a real explanation &mdash; the correct "
  "answer gets the mechanism, and each wrong answer gets the specific reason it fails rather than "
  "a restatement of itself. That is enforced rather than intended: the build rejects any "
  "explanation under 90 characters, and any that merely repeats its own option.<br><br>"
  "<b>No question appears in more than one form</b>, so working through all five gives you 250 "
  "distinct questions. Every question cites the lecture and slide it came from.")

for name in ("A", "B", "C", "D", "E"):
    fn = "cms-exam-3-master-exam-form-%s.html" % name.lower()
    html = render(title="CMS I Exam 3 Master Exam &mdash; Form %s" % name,
                  h1="Clinical Medicine and Surgery I &mdash; Comprehensive Master Exam",
                  sub="Exam 3 &middot; Ear, nose and throat block, Lectures 15&ndash;19 &middot; "
                      "Form %s" % name,
                  pill="50 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[name]))
