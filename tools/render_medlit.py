#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Interpretation of Medical Literature quizzes.

Palette is a rose built to the same recipe as the other class accents -- the
lightness and saturation of the established secondary accent, rotated to an
unused hue (340) so the class reads as its own thing. Both accents clear the
4.60:1 contrast bar on white.

    python3 render_medlit.py s1
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Interpretation of Medical Literature Exam 1")
PAL = dict(navy="#7a2d47", indigo="#b55575", gold="#c08a2e", ice="#faeff3")

SPEC = {
 "s1": dict(sets="medlit_s1_sets.json",
   files=["introduction-bias-validity-quiz.html",
          "introduction-bias-validity-quiz-version-2.html"],
   title="Introduction, Bias and Validity Quiz %d — Interpretation of Medical Literature",
   h1="Introduction, Bias and Validity &mdash; Quiz %d",
   sub="Interpretation of Medical Literature &middot; Session 1",
   chips=["Epidemiology", "Data sources", "Evidence-based medicine",
          "Types of bias", "Chance &amp; validity"]),
 "s2evid": dict(sets="medlit_s2evid_sets.json",
   files=["evidence-quiz.html", "evidence-quiz-version-2.html"],
   title="Evidence Quiz %d — Interpretation of Medical Literature",
   h1="Evidence &mdash; Quiz %d",
   sub="Interpretation of Medical Literature &middot; Session 2",
   chips=["Origins of EBM", "Evidence hierarchy", "USPSTF grades",
          "Judging sources", "Databases"]),
 "s2design": dict(sets="medlit_s2design_sets.json",
   files=["study-design-research-methods-quiz.html",
          "study-design-research-methods-quiz-version-2.html"],
   title="Study Design and Research Methods Quiz %d — Interpretation of Medical Literature",
   h1="Study Design and Research Methods &mdash; Quiz %d",
   sub="Interpretation of Medical Literature &middot; Session 2",
   chips=["Qualitative vs quantitative", "Cross-sectional", "Case-control",
          "Cohort", "Randomised trials"]),
 "s3rates": dict(sets="medlit_s3rates_sets.json",
   files=["rates-disease-measurement-quiz.html",
          "rates-disease-measurement-quiz-version-2.html"],
   title="Rates and Disease Measurement Quiz %d — Interpretation of Medical Literature",
   h1="Rates and Disease Measurement &mdash; Quiz %d",
   sub="Interpretation of Medical Literature &middot; Session 3",
   chips=["Mortality rates", "Incidence &amp; prevalence", "Sampling",
          "Surveillance", "Outbreak investigation"]),
 "s3data": dict(sets="medlit_s3data_sets.json",
   files=["data-validity-variation-quiz.html",
          "data-validity-variation-quiz-version-2.html"],
   title="Data, Validity and Variation Quiz %d — Interpretation of Medical Literature",
   h1="Data, Validity and Variation &mdash; Quiz %d",
   sub="Interpretation of Medical Literature &middot; Session 3",
   chips=["Levels of measurement", "Validity", "Reliability",
          "Types of variation", "Normal vs abnormal"]),
 "s4tests": dict(sets="medlit_s4tests_sets.json",
   files=["diagnostic-tests-quiz.html", "diagnostic-tests-quiz-version-2.html"],
   title="Diagnostic Tests Quiz %d — Interpretation of Medical Literature",
   h1="Diagnostic Tests &mdash; Quiz %d",
   sub="Interpretation of Medical Literature &middot; Session 4",
   chips=["Sensitivity &amp; specificity", "The 2&times;2 table", "Predictive values",
          "Likelihood ratios", "Parallel &amp; serial testing"]),
}[sys.argv[1] if len(sys.argv) > 1 else "s1"]

S = json.load(open(os.path.join(HERE, SPEC["sets"]), encoding="utf-8"))
for n, (key, fname) in enumerate(zip(("set1", "set2"), SPEC["files"]), start=1):
    qs = S[key]
    html = R.render(title=SPEC["title"] % n, h1=SPEC["h1"] % n, sub=SPEC["sub"],
                    pill="%d questions" % len(qs), chips=SPEC["chips"], intro="",
                    questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-52s %d questions" % (fname, len(qs)))
