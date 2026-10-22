#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Clinical Pathophysiology I pulmonary quizzes (Lecture 9)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 2")
SETS = json.load(open(os.path.join(HERE, "clinpath_pulmonary_sets.json"), encoding="utf-8"))
PALETTE = dict(navy="#3b2a5e", indigo="#6a4fa3", gold="#c08a2e", ice="#efeaf8")
CHIPS = ["Respiratory failure", "Pulmonary hypertension", "Lung cancer", "Obstructive",
         "Restrictive", "Pleura &amp; pneumonia"]

INTRO = (
  "Mechanism only, which is the line this course draws against Clinical Medicine and Surgery: "
  "why the lung fails belongs here, what is done about it belongs there. "
  "<b>Sort every disease into one of two bins first.</b> Obstructive diseases raise airflow "
  "resistance &mdash; from the airway wall (asthma, bronchitis), from lost parenchyma that held the "
  "airways open (emphysema) or from material in the lumen (bronchiectasis). Restrictive diseases "
  "stop the lungs expanding &mdash; from the parenchyma, the pleura, the chest wall or the "
  "neuromuscular pump. The bin predicts the test pattern: a low FEV1/FVC (forced expiratory volume "
  "in 1 second to forced vital capacity) ratio for obstruction, a low total lung capacity for "
  "restriction. "
  "<b>Hypoxia drives the right heart.</b> Hypoxic vasoconstriction raises pulmonary pressure, the "
  "right ventricle dilates, and that is cor pulmonale. "
  "<b>Weighted by the lecture.</b> No deck was posted; this one was rebuilt from the lecture video, "
  "and the questions follow the minutes each slide was on screen. Every fact comes from the slides."
)

for n in (1, 2):
    # Distractor `mis` tags stay in the sets (tools/blind_review.py reads them); pages carry
    # text + explanation only.
    qs = [dict({k: v for k, v in q.items() if k not in ("mis", "ordered", "core")},
               opts=[o[:2] for o in q["opts"]]) for q in SETS["set%d" % n]]
    fn = "pulmonary-pathophysiology-quiz.html" if n == 1 \
        else "pulmonary-pathophysiology-quiz-version-2.html"
    html = render(
        title="Pulmonary Pathophysiology Quiz %d &mdash; Clinical Pathophysiology I" % n,
        h1="Pulmonary Pathophysiology",
        sub="Clinical Pathophysiology I &middot; Exam 2 &middot; Lecture 9",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-46s %d questions" % (fn, len(qs)))
