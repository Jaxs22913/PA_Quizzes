#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Lecture 3 quiz built to the exam review's guidance.

Answer positions rotate through A-D, never chosen while authoring -- the bug
recorded in [[answer_position_bias_check]] shipped once already on this site.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
from pharm_l3_review_quiz import ITEMS

OUT = os.path.join(ROOT, "Pharmacology I Exam 1", "pharm-l3-review-guided-quiz.html")
DECK = "03. ANS Pharmacology(1).pptx"
IO = "Review guidance — autonomic nervous system pharmacology"

qs = []
for n, it in enumerate(ITEMS):
    opts = [[it["ans"], "Correct. " + it["why"]]] + [[w, r] for w, r in it["wrong"]]
    slot = n % 4
    opts.insert(slot, opts.pop(0))
    qs.append({"topic": it["ans"], "io": IO, "q": it["q"], "opts": opts, "c": slot,
               "cite": "%s, Slide %d" % (DECK, it["src"][1])})

html = render(
    title="ANS Quiz — Built to the Review Guidance | Pharmacology I Exam 1",
    h1="Autonomic Nervous System &mdash; Built to the Review Guidance",
    sub="Pharmacology I &middot; Exam 1 &middot; Lecture 3",
    pill="%d questions" % len(qs),
    chips=["Receptors &amp; effects", "Mechanism &rarr; indication",
           "More than one route", "Name &rarr; class", "Toxidromes"],
    intro="<b>Dr. Wood gave no scope cut for Lecture 3</b> &mdash; everything he narrowed at the "
          "review was aimed at Lecture 1. What he gave instead was a <b>shape</b>, and these 30 "
          "questions are built to it.<br><br>"
          "He said knowing which drugs are beta-1, beta-2, alpha-1 and alpha-2 plus the "
          "mnemonics is <i>&ldquo;part of it, certainly&rdquo;</i> &mdash; but that what he wants "
          "is the chain: <b>which receptors do which actions &rarr; how the drug affects those "
          "receptors &rarr; what do you expect to SEE</b>. So almost nothing here asks which "
          "receptor a drug binds; it asks what happens as a result.<br><br>"
          "The rest follows his other steers: <b>mechanism gives you the indication</b> rather "
          "than being learned separately; <b>more than one route can reach the same goal</b> "
          "(his own example was slowing a heart rate); and <b>a named drug has to go back in its "
          "class</b>, because that is what the answer choices give you. <b>There is not a single "
          "dose or numerical value in the bank</b>, because he said he supplies any value in the "
          "stem.",
    questions=qs, already_converted=True,
    navy="#7a3b12", indigo="#9c5230", gold="#c08a2e", ice="#faf1e8")
open(OUT, "w", encoding="utf-8").write(html)
from collections import Counter
print("wrote %s (%d questions, key positions %s)"
      % (os.path.basename(OUT), len(qs),
         "/".join(str(Counter(q["c"] for q in qs).get(i, 0)) for i in range(4))))
