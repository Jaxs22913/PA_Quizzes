#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Physical Diagnosis 2 Lecture 7 (hematological examination) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 2")
S = json.load(open(os.path.join(HERE, "pd2_l7_sets.json"), encoding="utf-8"))
# `mis` (the misconception each distractor stands for) is review metadata for
# tools/blind_review.py; it stays in the sets file and out of the page.
S = {k: [{f: v for f, v in q.items() if f != "mis"} for q in qs] for k, qs in S.items()}
PAL = dict(navy="#3a5a40", indigo="#5f8a68", gold="#c08a2e", ice="#eef4ef")
CHIPS = ["Causes &amp; thresholds", "History", "Bleeding &amp; menstrual history", "Skin, nails &amp; mucosa",
         "Petechiae &amp; purpura", "Heart &amp; lungs", "Abdomen &amp; internal bleeding", "B12 neurologic exam",
         "Emergency"]
INTRO = (
  "Thirty questions on the advanced hematological history and examination. "
  "<b>Sort the anemia first</b>: blood loss (trauma, menstrual, gastrointestinal), destruction (hemolysis) "
  "or impaired production (deficiency, renal failure, chronic disease, marrow disease). "
  "<b>Severity is not fatigue</b>: fatigue is the most common symptom and appears even in mild anemia; "
  "symptoms at rest, chest pain and syncope mark severity, and the rate of onset and cardiopulmonary "
  "disease decide how badly it is tolerated. "
  "<b>Most signs are clues, not proof</b>: pallor is an unreliable hemoglobin estimate, nail findings, "
  "glossitis and angular cheilitis are nonspecific, and a normal look, a negative stool blood test or absent "
  "Cullen and Grey Turner signs never rule anything out. Pulse oximetry stays normal in anemia. "
  "Covers the history (bleeding, iron and B12 clues, diet, medications, menstrual, family and exposure "
  "history), the skin, nail, mouth and node examination, the cardiovascular, pulmonary and abdominal "
  "findings, clubbing, the B12 neurologic examination with Romberg, and the bleeding emergency."
)

for n in (1, 2):
    qs = S["set%d" % n]
    fn = "anemia-exam-quiz.html" if n == 1 else "anemia-exam-quiz-version-2.html"
    html = render(title="Advanced Hematological Examination Quiz %d &mdash; PD2 Exam 2" % n,
                  h1="Advanced Hematological Examination &mdash; Quiz %d" % n,
                  sub="Physical Diagnosis 2 &middot; Exam 2 &middot; Lecture 7",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=qs, already_converted=True, **PAL)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-44s %d questions" % (fn, len(qs)))
