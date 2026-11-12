#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Clinical Pathophysiology I blood disorders quizzes (Lecture 10)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 2")
SETS = json.load(open(os.path.join(HERE, "clinpath_blood_sets.json"), encoding="utf-8"))
PALETTE = dict(navy="#3b2a5e", indigo="#6a4fa3", gold="#c08a2e", ice="#efeaf8")
CHIPS = ["White cells", "Marrow neoplasms", "Leukemia &amp; lymphoma", "Red cells &amp; anemia",
         "Coagulation", "Platelets"]

INTRO = (
  "Mechanism only, which is the line this course draws against Clinical Medicine and Surgery: "
  "why the blood fails belongs here, what is done about it belongs there. "
  "<b>Ask where the problem sits in the lineage.</b> Every circulating cell starts from one stem cell "
  "and splits into myeloid and lymphoid branches, so the cell lines that are affected point to where the "
  "defect arises. Lymphoid neoplasms are sorted by lineage and stage: <b>precursor</b> (acute "
  "lymphoblastic leukemia), <b>mature</b> (chronic lymphocytic leukemia) or <b>differentiated</b> "
  "(plasma-cell myeloma). "
  "<b>Sort every anemia two ways:</b> by size (microcytic below 80, normocytic 80 to 100, macrocytic above "
  "100 femtoliters) and by mechanism &mdash; loss, destruction or diminished production. "
  "<b>Weighted by the lecture.</b> The questions follow the minutes spent on each topic, with the slides "
  "the lecturer flagged counted more. Every fact comes from the slides."
)
for n in (1, 2):
    # Distractor `mis` tags stay in the sets (tools/blind_review.py reads them); pages carry
    # text + explanation only.
    qs = [dict({k: v for k, v in q.items() if k not in ("mis", "ordered", "core")},
               opts=[o[:2] for o in q["opts"]]) for q in SETS["set%d" % n]]
    fn = "blood-disorders-quiz.html" if n == 1 \
        else "blood-disorders-quiz-version-2.html"
    html = render(
        title="Blood Disorders Quiz %d &mdash; Clinical Pathophysiology I" % n,
        h1="Pathophysiology of Blood Disorders",
        sub="Clinical Pathophysiology I &middot; Exam 2 &middot; Lecture 10",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-46s %d questions" % (fn, len(qs)))
