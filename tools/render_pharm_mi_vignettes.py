#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Pharmacology I Exam 2 myocardial ischemia clinical vignette sets (Lecture 8).

Same shape as render_pharm_e2_vignettes.py (the ophthalmic pair) and the same brown Exam 2 vignette
palette. Reads tools/pharm_mi_vignette_sets.json, written by pharm_mi_vignette_partition.py.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 2")
S = json.load(open(os.path.join(HERE, "pharm_mi_vignette_sets.json"), encoding="utf-8"))
PAL = dict(navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
CHIPS = ["Beta blockers", "Calcium channel blockers", "Nitrates", "Variant angina",
         "Add-on therapy", "Acute coronary syndrome", "Fibrinolytics"]
INTRO = ("Clinical vignettes that open with a patient rather than a fact. The two topic quizzes on "
         "myocardial ischemia test the drugs one at a time; these ask what you would <b>choose</b>, what you "
         "would <b>avoid</b>, what you would <b>warn the patient about</b> and what would go wrong if "
         "two drugs were combined. The stem always gives you the patient, and the last sentence decides "
         "the answer, so read it twice: the same man with angina can need a beta blocker, a calcium "
         "channel blocker or a call for emergency help depending on what you are asked. "
         "Expect the classic contrasts: <b>beta blocker first line</b> and when it is forbidden "
         "(asthma, bradycardia, heart block, decompensated heart failure), the two calcium channel "
         "blocker families, <b>nitrates</b> (how to take them, the nitrate-free interval, the "
         "phosphodiesterase-5 inhibitor danger), variant angina, aspirin first in an acute coronary "
         "syndrome, and who is and is not a candidate for a fibrinolytic. "
         "<b>No doses</b> are asked. Every option carries its own reason, correct and incorrect "
         "alike, and every question cites its slide.")

for n, key in ((1, "set1"), (2, "set2")):
    fn = "pharm-e2-mi-vignettes.html" if n == 1 else "pharm-e2-mi-vignettes-version-2.html"
    html = render(title="Myocardial Ischemia Drugs &mdash; Clinical Vignettes %d | Pharmacology I Exam 2" % n,
                  h1="Myocardial Ischemia Drugs &mdash; Clinical Vignettes %d" % n,
                  sub="Pharmacology I &middot; Exam 2 &middot; apply it to a patient",
                  pill="%d questions" % len(S[key]), chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-44s %d questions" % (fn, len(S[key])))
