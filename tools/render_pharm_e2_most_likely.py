#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render 'Pharmacology I Exam 2: Most Likely 40' from tools/pharm_e2_most_likely_sets.json, which
tools/build_pharm_e2_most_likely.py writes (selection, evidence and rationale live there).
Same brown Exam 2 palette as the master exams and the Exam 2 guide; one version only."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 2")
S = json.load(open(os.path.join(HERE, "pharm_e2_most_likely_sets.json"), encoding="utf-8"))["set1"]
PAL = dict(navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
CHIPS = ["Ophthalmic drugs", "Ear, nose and throat drugs", "Antihypertensives", "Lipid-lowering drugs",
         "Myocardial ischemia"]
INTRO = ("Forty questions, eight per lecture, picked from the facts the lecturer stressed most and the question "
         "styles the course uses; no one can know what will be asked. They follow the order of the lectures "
         "(4 to 8), reuse questions already in the topic quizzes and vignettes, and carry no dosages.")

fn = "pharm-e2-most-likely-40.html"
html = render(title="Pharmacology I Exam 2: Most Likely 40",
              h1="Pharmacology I Exam 2: Most Likely 40",
              sub="Pharmacology I &middot; Exam 2 &middot; Lectures 4&ndash;8 &middot; eight per lecture",
              pill="%d questions" % len(S), chips=CHIPS, intro=INTRO,
              questions=S, already_converted=True, **PAL)
open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
print("wrote %-44s %d questions" % (fn, len(S)))
