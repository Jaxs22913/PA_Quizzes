#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two CMS I Exam 5 "Infective Endocarditis - Case Vignettes" quizzes from
tools/cms_e5l32_cases_sets.json (written by tools/cms_e5l32_cases_partition.py; never render straight
from the pool). Same template and Exam 5 palette as render_cms_e5x2.py and the other Exam 5 pages.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
D = "Clinical Medicine and Surgery I Exam 5"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(HERE, "cms_e5l32_cases_sets.json"), encoding="utf-8"))
PAL = dict(navy="#7a2d5a", indigo="#b4538c", gold="#c08a2e", ice="#faeef4")
CHIPS = ["Recommended initial treatment", "Most important next step", "Modified Duke classification",
         "Who needs prophylaxis", "Comorbidities: what instead", "Surgery"]
INTRO = (
  "Written in the shape of Professor Reynolds' own practice cases for this lecture: a short case "
  "with the age, the risk history, vital signs, the findings described rather than named, and the "
  "culture or echocardiogram result, then <b>one</b> question: the recommended initial treatment, "
  "the most important next step, who needs prophylaxis, the modified Duke classification, the likely "
  "organism, the surgical indication, or what to use instead when a comorbidity or allergy rules out "
  "the usual drug.<br><br>"
  "Her four practice cases are included (two in each quiz), keyed as she keyed them; one of them had "
  "five choices and is shown here with four. Everything else is new. <b>Four options, A&ndash;D</b>. "
  "Each choice explains why it fits or fails <i>this</i> patient, and every question cites its slide.")
FILES = {"1": "infective-endocarditis-case-vignettes.html",
         "2": "infective-endocarditis-case-vignettes-version-2.html"}

for name, fn in FILES.items():
    n = len(S[name])
    qs = [dict(q, opts=[o[:2] for o in q["opts"]]) for q in S[name]]     # misconception tags stay in the JSON
    html = render(title="Infective Endocarditis Case Vignettes %s &mdash; CMS I Exam 5" % name,
                  h1="Infective Endocarditis &mdash; Case Vignettes %s" % name,
                  sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 32 &middot; "
                      "Professor Reynolds' case style",
                  pill="%d questions" % n, chips=CHIPS, intro=INTRO,
                  questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % n)
