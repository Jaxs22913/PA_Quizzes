#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render 'Pharmacology I Exam 2: Most Likely 45 (Version 3: Drug Names)' from tools/pharm_e2_most_likely_45_v3_sets.json, which
tools/build_pharm_e2_most_likely_45_v3.py writes (selection, evidence and rationale live there).
Same brown Exam 2 palette as the master exams and the Exam 2 guide; one version only."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 2")
S = json.load(open(os.path.join(HERE, "pharm_e2_most_likely_45_v3_sets.json"), encoding="utf-8"))["set1"]
PAL = dict(navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
CHIPS = ["Ophthalmic drugs", "Ear, nose and throat drugs", "Antihypertensives", "Lipid-lowering drugs",
         "Myocardial ischemia"]
INTRO = ("Forty-five questions, nine per lecture, asked the way Versions 1 and 2 ask them, but every answer choice is a "
         "specific drug name rather than a class, so you drill the drugs inside the classes. It uses the same most "
         "stressed facts and repeats concepts from the first two versions on purpose; no one can know what will be "
         "asked. The questions follow the order of the lectures (4 to 8) and carry no dosages.")

fn = "pharm-e2-most-likely-45-version-3.html"
html = render(title="Pharmacology I Exam 2: Most Likely 45 (Version 3: Drug Names)",
              h1="Pharmacology I Exam 2: Most Likely 45 (Version 3: Drug Names)",
              sub="Pharmacology I &middot; Exam 2 &middot; Lectures 4&ndash;8 &middot; nine per lecture",
              pill="%d questions" % len(S), chips=CHIPS, intro=INTRO,
              questions=S, already_converted=True, **PAL)
open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
print("wrote %-44s %d questions" % (fn, len(S)))
