#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the five CMS I Exam 5 (Cardiology Block II) EXAM-STYLE forms -- 70 questions each,
shaped like the real paper as faculty described it on 2026-10-25 (70 questions, a couple of
ECG tracings, many more rhythms described inside clinical vignettes).

Reads Clinical Medicine and Surgery I Exam 5/exam-style-forms.json, written by
tools/cms_e5_examstyle_partition.py (keys on an 18/18/17/17 A-D split per form -- never render
straight from a pool). Same template and palette as the 5 x 60 masters
(render_cms_e5_masters.py), which stay as they are.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Clinical Medicine and Surgery I Exam 5"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "exam-style-forms.json"), encoding="utf-8"))
PAL = dict(navy="#7a2d5a", indigo="#b4538c", gold="#c08a2e", ice="#faeef4")
CHIPS = ["Rhythm strips", "Rhythms in clinical vignettes", "Venous disorders",
         "Arterial occlusive disease &amp; aneurysm", "Cardiomyopathy", "Pericardial disease",
         "Infective endocarditis"]
INTRO = (
  "Seventy questions, <b>shaped like the real exam</b> as the course described it: a couple of "
  "<b>rhythm strips</b>, and a much larger share of <b>patient cases that describe a heart rhythm in "
  "words</b> (rate, regularity, P waves, PR interval, QRS width) and then ask for the diagnosis or "
  "its cause, the right test, or the next step in management.<br><br>"
  "<b>Twenty-eight of the seventy are rhythm questions</b> (three strips in every form); the other "
  "forty-two come from venous disorders, arterial disease and aneurysms, cardiomyopathy, pericardial "
  "disease and infective endocarditis. Fifty-six are patient vignettes.<br><br>"
  "These forms favor questions you have not met in the 60-question master exams. <b>Four options, "
  "A&ndash;D</b>, every wrong choice explained, and every question cites the slide it came from.")

for name in ("A", "B", "C", "D", "E"):
    fn = "cms-exam-5-exam-style-form-%s.html" % name.lower()
    assert len(S[name]) == 70, "Form %s has %d questions" % (name, len(S[name]))
    qs = [dict(q, opts=[o[:2] for o in q["opts"]]) for q in S[name]]     # misconception tags stay in the JSON
    html = render(title="CMS I Exam 5 Exam-Style Practice &mdash; Form %s" % name,
                  h1="Clinical Medicine and Surgery I &mdash; Exam-Style Practice Exam",
                  sub="Exam 5 &middot; Cardiology block II, Lectures 26&ndash;32 &middot; "
                      "70 questions like the real exam &middot; Form %s" % name,
                  pill="70 questions", chips=CHIPS, intro=INTRO,
                  questions=qs, already_converted=True,
                  progress_sig_strict=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions, %d strips)" % (len(S[name]), sum(1 for q in S[name] if q.get("img"))))
