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
}[sys.argv[1] if len(sys.argv) > 1 else "s1"]

S = json.load(open(os.path.join(HERE, SPEC["sets"]), encoding="utf-8"))
for n, (key, fname) in enumerate(zip(("set1", "set2"), SPEC["files"]), start=1):
    qs = S[key]
    html = R.render(title=SPEC["title"] % n, h1=SPEC["h1"] % n, sub=SPEC["sub"],
                    pill="%d questions" % len(qs), chips=SPEC["chips"], intro="",
                    questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-52s %d questions" % (fname, len(qs)))
