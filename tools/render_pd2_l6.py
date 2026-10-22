#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Physical Diagnosis 2 Lecture 6 (thorax and lungs) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 2")
S = json.load(open(os.path.join(HERE, "pd2_l6_sets.json"), encoding="utf-8"))
# `mis` (the misconception each distractor stands for) is review metadata for
# tools/blind_review.py; it stays in the sets file and out of the page.
S = {k: [{f: v for f, v in q.items() if f != "mis"} for q in qs] for k, qs in S.items()}
PAL = dict(navy="#3a5a40", indigo="#5f8a68", gold="#c08a2e", ice="#eef4ef")
CHIPS = ["Landmarks", "History", "Clubbing &amp; hemoptysis", "Dyspnea", "Inspection &amp; palpation",
         "Percussion", "Breath sounds", "Adventitious sounds", "Five conditions"]
INTRO = (
  "Thirty questions on the advanced thorax and lung examination. "
  "<b>The five conditions are told apart by four findings read together</b>: the trachea, tactile "
  "fremitus, the percussion note and the breath sounds. Pneumonia is dull with INCREASED fremitus, "
  "bronchial sounds and egophony; pleural effusion is dull with DECREASED fremitus and sounds; "
  "pneumothorax is hyperresonant with decreased fremitus and sounds; asthma is diffusely "
  "hyperresonant with wheezes and a prolonged expiration. "
  "<b>Watch which way the trachea goes</b>: atelectasis pulls it toward the affected side, while a "
  "tension pneumothorax or a large effusion pushes it toward the unaffected side. "
  "<b>Three sounds need immediate action</b>: stridor over the neck on inspiration, the silent chest of "
  "asthma, and massive hemoptysis. A pleural rub disappears when the breath is held; a pericardial "
  "friction rub does not. "
  "Covers the landmarks and the procedures tied to them, the respiratory history (chest pain patterns, "
  "dyspnea, cough, sputum, hemoptysis and disordered sleep), clubbing, sudden against gradual or "
  "episodic dyspnea, the breathing patterns and chest wall deformities, palpation, percussion, the "
  "four breath sounds, crackles, wheezes, rhonchi and the other adventitious sounds, and the "
  "transmitted voice tests."
)

for n in (1, 2):
    qs = S["set%d" % n]
    fn = "thorax-lung-exam-quiz.html" if n == 1 else "thorax-lung-exam-quiz-version-2.html"
    html = render(title="Advanced Thorax and Lung Examination Quiz %d &mdash; PD2 Exam 2" % n,
                  h1="Advanced Thorax and Lung Examination &mdash; Quiz %d" % n,
                  sub="Physical Diagnosis 2 &middot; Exam 2 &middot; Lecture 6",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=qs, already_converted=True, **PAL)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-44s %d questions" % (fn, len(qs)))
