#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Interpretation of Medical Literature Exam 1 master exams (five cumulative forms)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Interpretation of Medical Literature Exam 1"
OUT = os.path.join(ROOT, D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
PAL = dict(navy="#7a2d47", indigo="#b55575", gold="#c08a2e", ice="#faeff3")
CHIPS = ["Bias &amp; validity", "Study designs", "Diagnostic tests", "Risk &amp; ratios", "Trials &amp; statistics", "Reviews &amp; evidence"]
TOTAL = sum(len(v) for v in S.values())
for name in "ABCDE":
    qs = S[name]
    topics = len({q["topic"] for q in qs})
    intro = ("%d questions covering every lecture deck in the Exam 1 block, the same number from each topic. "
             "<b>No question appears in more than one form</b>, so working through all five gives you %d distinct "
             "questions. The live sessions (small groups, journal days and project time) have no deck and are not "
             "included. Every question cites the slide it is built on." % (len(qs), TOTAL))
    fn = "medical-literature-master-exam-form-%s.html" % name.lower()
    html = render(title="Medical Literature Master Exam &mdash; Form %s" % name,
                  h1="Interpretation of Medical Literature &mdash; Comprehensive Master Exam",
                  sub="Exam 1 &middot; Lectures 1&ndash;13 &middot; Form %s" % name,
                  pill="%d questions" % len(qs), chips=CHIPS, intro=intro,
                  questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-46s %d questions" % (fn, len(qs)))
