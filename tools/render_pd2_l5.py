#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Physical Diagnosis 2 Lecture 5 (cardiovascular) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 2")
S = json.load(open(os.path.join(HERE, "pd2_l5_sets.json"), encoding="utf-8"))
PAL = dict(navy="#3a5a40", indigo="#5f8a68", gold="#c08a2e", ice="#eef4ef")
CHIPS = ["Cardiac history", "Heart sounds", "Apical impulse", "Murmurs",
         "Manoeuvres", "Peripheral vascular"]
INTRO = (
  "Thirty questions on the advanced cardiovascular and peripheral vascular examination. "
  "<b>The manoeuvres are the block worth getting right, and the deck says why.</b> Valsalva and "
  "standing DROP preload; squatting and leg raise RAISE it. Hypertrophic cardiomyopathy gets "
  "louder when preload falls and softer when it rises; aortic stenosis does the exact opposite. "
  "That one reversal is what separates the two, and the deck flags it in capitals &mdash; "
  "<i>so you don't sign off incorrectly on a sports physical</i>. "
  "<b>Two sounds are easy to swap.</b> S3 is early diastolic with the cadence Ken-TUC-ky, and it "
  "is physiologic in children, young adults and late pregnancy but pathologic over 40. S4 is just "
  "before S1 with the cadence Ten-nes-SEE, and it runs the other way &mdash; normal in trained "
  "athletes and older patients. Both are low-pitched and need the bell at the apex in left "
  "lateral decubitus. "
  "<b>Bell for low, diaphragm for high</b> &mdash; S3, S4 and mitral stenosis on the bell, "
  "applied lightly; S1, S2, rubs and the regurgitant murmurs on the diaphragm, pressed firmly. "
  "<b>One radiation is a discriminator</b>: mitral regurgitation goes to the axilla, tricuspid "
  "regurgitation specifically does NOT, and hypertrophic cardiomyopathy never goes to the neck. "
  "Covers the cardiac history through chest pain, palpitations, orthopnoea, paroxysmal nocturnal "
  "dyspnoea, oedema and syncope; the cardiac cycle and what makes each sound; the apical impulse "
  "and the hyperkinetic, sustained and diffuse patterns; auscultation technique; the extra "
  "systolic and diastolic sounds; the seven characteristics of a murmur and each named murmur in "
  "turn; the manoeuvres; and the whole peripheral vascular examination from capillary refill and "
  "pulse amplitude through the arterial against venous insufficiency comparison, the pulses, "
  "bruits, the Allen test, the ankle brachial index and Homan's sign."
)

for n in (1, 2):
    qs = S["set%d" % n]
    fn = "cardiovascular-exam-quiz.html" if n == 1 \
        else "cardiovascular-exam-quiz-version-2.html"
    html = render(title="Advanced Cardiovascular Examination Quiz %d &mdash; PD2 Exam 2" % n,
                  h1="Advanced Cardiovascular and Peripheral Vascular Examination &mdash; Quiz %d" % n,
                  sub="Physical Diagnosis 2 &middot; Exam 2 &middot; Lecture 5",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=qs, already_converted=True, **PAL)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-44s %d questions" % (fn, len(qs)))
