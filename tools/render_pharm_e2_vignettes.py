#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Pharmacology I Exam 2 clinical vignette sets."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 2")
S = json.load(open(os.path.join(HERE, "pharm_e2_vignette_sets.json"), encoding="utf-8"))
PAL = dict(navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
CHIPS = ["Vasoconstrictors", "Anti-infectives", "Allergy &amp; inflammation",
         "Dry eye", "Glaucoma", "Diagnostics", "Administration"]
INTRO = ("Twenty-one questions that open with a patient rather than a fact. The topic quizzes "
         "and drills between them ask 177 questions about this lecture and <b>not one of them "
         "names a patient</b> &mdash; recall is well covered here, application was not. "
         "These ask what you would choose, what you would warn about, and what you would avoid. "
         "<b>No doses</b>, which Dr. Wood does not ask for, and nothing is built on the four "
         "things he took off the table &mdash; individual antibiotic indications, formulations, "
         "which agent causes irritation, and the specific combination products. "
         "The one item he promised to ask is here: <b>rebound hyperaemia</b>, the two-week "
         "limit, and the 72-hour review point. Every question cites its slide.")

for n, key in ((1, "set1"), (2, "set2")):
    fn = "pharm-e2-vignettes.html" if n == 1 else "pharm-e2-vignettes-version-2.html"
    html = render(title="Ophthalmic Drugs &mdash; Clinical Vignettes %d | Pharmacology I Exam 2" % n,
                  h1="Ophthalmic Drugs &mdash; Clinical Vignettes %d" % n,
                  sub="Pharmacology I &middot; Exam 2 &middot; apply it to a patient",
                  pill="%d questions" % len(S[key]), chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-40s %d questions" % (fn, len(S[key])))
