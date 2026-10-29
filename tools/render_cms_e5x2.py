#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two CMS I Exam 5 "comorbidities, contraindications and scores" quizzes from
tools/cms_e5x2_sets.json (written by tools/cms_e5x2_partition.py -- never render straight from a
pool). Same template and palette as the Exam 5 exam-style forms (render_cms_e5_examstyle.py).
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
D = "Clinical Medicine and Surgery I Exam 5"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(HERE, "cms_e5x2_sets.json"), encoding="utf-8"))
PAL = dict(navy="#7a2d5a", indigo="#b4538c", gold="#c08a2e", ice="#faeef4")
CHIPS = ["Venous disorders", "Arterial occlusive disease &amp; aneurysm", "Cardiomyopathy",
         "Supraventricular arrhythmias", "Blocks &amp; ventricular arrhythmias", "Pericardial disease",
         "Infective endocarditis"]
INTRO = (
  "Built from what the class reported about the real Exam 5: <b>patients with several conditions at "
  "once</b>, where two similar drugs or diagnoses are separated by a <b>contraindication</b> and you "
  "have to pick <b>what to use instead</b>, and <b>guideline scores worked out from the vignette</b> "
  "(CHA<sub>2</sub>DS<sub>2</sub>-VASc, HAS-BLED, Wells, Duke, ankle-brachial index, New York Heart "
  "Association class).<br><br>"
  "Every question is new: none appears in the topic quizzes, the master exams or the exam-style "
  "forms. <b>Four options, A&ndash;D</b>. Each choice explains why it fits or fails <i>this</i> patient, "
  "and score questions show the arithmetic point by point. Every question cites the slide it came from.")
FILES = {"1": "comorbidities-contraindications-scores-quiz.html",
         "2": "comorbidities-contraindications-scores-quiz-version-2.html"}

for name, fn in FILES.items():
    n = len(S[name])
    qs = [dict(q, opts=[o[:2] for o in q["opts"]]) for q in S[name]]     # misconception tags stay in the JSON
    html = render(title="CMS I Exam 5 Comorbidities, Contraindications &amp; Scores &mdash; Quiz %s" % name,
                  h1="Comorbidities, Contraindications &amp; Scores",
                  sub="Exam 5 &middot; Cardiology block II, Lectures 26&ndash;32 &middot; "
                      "real-exam style &middot; Quiz %s" % name,
                  pill="%d questions" % n, chips=CHIPS, intro=INTRO,
                  questions=qs, already_converted=True,
                  progress_sig_strict=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % n)
