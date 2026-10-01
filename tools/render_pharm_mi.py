#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the four Pharmacology I Exam 2 myocardial ischemia quizzes (Lecture 8).

Same shape as render_pharm_lipid.py: one topic, two versions, the Exam 2 palette.
Reads tools/pharm_mi_sets.json, written by pharm_mi_partition.py.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 2")
SETS = json.load(open(os.path.join(HERE, "pharm_mi_sets.json"), encoding="utf-8"))
PALETTE = dict(navy="#2f4f6b", indigo="#4a7fa5", gold="#b8862f", ice="#eef3f7")

NOTE = ("<b>What these do and do not ask.</b> <b>Indications, adverse effects, "
        "contraindications and patient education are in</b>, weighted above mechanism. "
        "<b>Doses are out</b> (the aspirin chew dose, the ointment measure and tablet strengths), "
        "and so are trial percentages, which is why the sets run shorter than the usual 30. "
        "Every option carries its own reason, correct and incorrect alike.")

CONF = [
 ("anginal", "Antianginal Drugs", "mi-antianginals-quiz",
  ["Supply and demand", "Beta blockers", "Calcium channel blockers", "Nitrates", "Add-on therapy"],
  "Angina is an <b>oxygen supply-and-demand</b> problem, and every antianginal lowers demand "
  "(heart rate, contractility, wall tension), raises supply, or both. <b>Beta blockers are first "
  "line.</b> Calcium channel blockers split into the heart-acting <b>non-dihydropyridines</b> and "
  "the vessel-acting <b>dihydropyridines</b>. Nitrates relieve the acute attack and are "
  "adjuncts over the long term, limited by <b>tolerance</b> and by the "
  "<b>phosphodiesterase-5 inhibitor interaction</b>."),
 ("acs", "Acute Coronary Syndrome &amp; Fibrinolytics", "mi-acs-quiz",
  ["Classification", "Thrombus formation", "Aspirin &amp; nitrates", "Beta blockers &amp; morphine",
   "Fibrinolytics", "Other antithrombotics"],
  "Acute coronary syndrome is a <b>thrombus on a ruptured plaque</b>. Know the two branches "
  "(ST-elevation and non-ST-elevation), why <b>aspirin comes first</b>, why nitrates relieve "
  "pain but do not improve survival, and how <b>fibrinolytics</b> work, who they are for "
  "(<b>ST-elevation</b> only) and what they cost in <b>bleeding</b>."),
]

for key, label, stem, chips, blurb in CONF:
    for n in (1, 2):
        qs = SETS["%s%d" % (key, n)]
        fn = "%s.html" % stem if n == 1 else "%s-version-2.html" % stem
        html = render(
            title="%s Quiz %d &mdash; Pharmacology I Exam 2" % (label, n),
            h1=label, sub="Pharmacology I &middot; Exam 2 &middot; Myocardial Ischemia Drug Therapy",
            pill="%d questions" % len(qs), chips=chips,
            intro=blurb + " " + NOTE,
            questions=qs, already_converted=True, **PALETTE)
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
        print("wrote %-50s %d questions" % (fn, len(qs)))
