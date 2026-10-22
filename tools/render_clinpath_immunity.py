#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Clinical Pathophysiology I immunity quizzes (Lecture 8)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 2")
SETS = json.load(open(os.path.join(HERE, "clinpath_immunity_sets.json"), encoding="utf-8"))
PALETTE = dict(navy="#3b2a5e", indigo="#6a4fa3", gold="#c08a2e", ice="#efeaf8")
CHIPS = ["Blood cells", "B and T cells", "Antibodies", "Hypersensitivity", "Complement",
         "Immunodeficiency"]

INTRO = (
  "Mechanism only, which is the line this course draws against Clinical Medicine and Surgery: "
  "how the immune system works and how it injures belongs here, what is done about it belongs there. "
  "<b>One idea organizes the antibody half.</b> An antibody has two ends that do different jobs: the "
  "Fab arms recognize the antigen, and the Fc stem decides what happens next &mdash; which cell it "
  "recruits, whether complement starts, where the molecule can travel. The five classes differ in "
  "that constant region, which is why IgM agglutinates, IgG crosses the placenta, IgA guards the "
  "mucosa and IgE arms the mast cell. "
  "<b>Hypersensitivity is sorted by mechanism, not by severity.</b> Type I is IgE on mast cells, "
  "type II is antibody bound to a cell or tissue antigen, type III is deposited immune complexes, "
  "and type IV is sensitized T cells. Ask which of the four is doing the damage and the examples "
  "follow. "
  "<b>Weighted by the narration.</b> This was a narrated deck, so the minutes spent on each slide are "
  "exact; the questions follow those minutes, and every fact comes from the slides themselves."
)

for n in (1, 2):
    # The sets keep each distractor's misconception tag as a third option element
    # (WRITER.md; tools/blind_review.py reads it there); pages carry text + explanation only.
    qs = [dict({k: v for k, v in q.items() if k not in ("mis", "ordered", "core")},
               opts=[o[:2] for o in q["opts"]]) for q in SETS["set%d" % n]]
    fn = "immunity-quiz.html" if n == 1 else "immunity-quiz-version-2.html"
    html = render(
        title="Immunity Quiz %d &mdash; Clinical Pathophysiology I" % n,
        h1="Immunity",
        sub="Clinical Pathophysiology I &middot; Exam 2 &middot; Lecture 8",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-46s %d questions" % (fn, len(qs)))
