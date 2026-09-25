# -*- coding: utf-8 -*-
"""Lecture 21 objective-style pool C -- corrective pool for the slot floors.

KEYS ARE WRITTEN SHORT ON PURPOSE — detail lives in the explanation.

check_slot_coverage.py --floors found pools A and B short on initial test (3/5),
agent/regimen (2/3) and manifestation (9/10). These fill them from slides that
state the fact outright: the bedside tests used to sort a faint (13, 16, 27, 31),
the syndrome's presentation (18), and the role of each outpatient drug (23).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e4l21_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


QUESTIONS = [

S("Orthostatic diagnosis", IO2,
  "Which bedside measurement confirms orthostatic hypotension?",
  [["Supine and standing vital signs",
    "Correct. Pressure and heart rate are measured supine and again after up to 3 minutes of standing; the pressure fall meets the criteria and the heart rate response points to the type."],
   ["A single seated blood pressure",
    "One seated reading is a snapshot and cannot show a postural change. The criteria compare supine with standing readings."],
   ["A tilt-table test",
    "The tilt-table test is the listed test for postural orthostatic tachycardia syndrome, with a sensitivity of only about 40%."],
   ["A resting electrocardiogram",
    "A resting electrocardiogram looks for an arrhythmia behind cardiogenic syncope; it does not measure a postural pressure fall."]],
  C(13), "initial test"),

S("Non-hypotensive syncope", IO4,
  "Which quick test excludes hypoglycemia as the cause of a faint?",
  [["A blood glucose level",
    "Correct. A normal blood glucose rules out hypoglycemia, one of the non-hypotensive causes of syncope, alongside blood counts and a metabolic panel for infection or metabolic causes."],
   ["A tilt-table test",
    "Tilt-table testing is for postural orthostatic tachycardia syndrome and tells nothing about the blood sugar at the time of a faint."],
   ["An echocardiogram",
    "Echocardiography evaluates structural cardiogenic syncope, such as cardiomyopathy or valve disease, not hypoglycemia."],
   ["Orthostatic vital signs",
    "Supine and standing vital signs diagnose orthostatic hypotension; a low sugar is excluded with a blood glucose measurement."]],
  C(27), "initial test"),

S("Cardiogenic syncope", IO4,
  "When a faint follows palpitations, which test comes first?",
  [["An electrocardiogram",
    "Correct. A suspected arrhythmia is investigated first with an electrocardiogram, then monitoring, a stress test and cardiology consultation."],
   ["A tilt-table test",
    "Tilt-table testing belongs to postural orthostatic tachycardia syndrome, not to the first look for an arrhythmia behind a faint."],
   ["A symptom log",
    "An episode log supports the history in reflex syncope; palpitations before a faint call for a tracing of the rhythm."],
   ["A stress echocardiogram",
    "Stress echocardiography is part of the structural work-up rather than the first test for a suspected arrhythmia."]],
  C(16), "initial test"),

S("Drug therapy", IO2,
  "Which drug used for hypotension has only mild efficacy?",
  [["Droxidopa",
    "Correct. Droxidopa has mild efficacy, is better with supine hypertension, and is usually used as an adjunct with midodrine or fludrocortisone."],
   ["Midodrine",
    "Midodrine is described as best with neurogenic syncope, the first choice there unless supine hypertension, severe heart disease or kidney disease is present."],
   ["Fludrocortisone",
    "Fludrocortisone is described as best with postural orthostatic tachycardia syndrome, and it is avoided in heart failure."],
   ["Vasopressin",
    "Vasopressin is a pressor reserved, with epinephrine, norepinephrine, dopamine and phenylephrine, for the emergency department and intensive care."]],
  C(23), "agent/regimen"),

S("Postural tachycardia syndrome", IO2,
  "How do the symptoms of postural orthostatic tachycardia syndrome change on lying down?",
  [["They usually improve",
    "Correct. The heart rate rise and symptoms appear within 10 minutes of standing and usually improve when the patient lies down."],
   ["They usually worsen",
    "Worsening on lying down would not fit a syndrome defined by what happens on standing; symptoms usually improve supine."],
   ["They are unchanged",
    "Position is the whole point of the syndrome: the tachycardia comes on standing and usually eases when lying down."],
   ["They turn into seizures",
    "Seizure is a separate non-hypotensive cause of loss of consciousness, not a change the syndrome undergoes when lying down."]],
  C(18), "manifestation"),

S("Postural tachycardia syndrome", IO2,
  "Which symptoms occur on standing in postural orthostatic tachycardia syndrome?",
  [["Palpitations and lightheadedness",
    "Correct. Tachycardia with or without lightheadedness, dizziness, fainting and palpitations appears on standing and usually eases when lying down."],
   ["Tongue biting and confusion",
    "Tongue biting and prolonged confusion afterward point toward seizure, a separate non-hypotensive cause of loss of consciousness."],
   ["Numb feet and dry mouth",
    "Reduced sensation in the feet suggests diabetic neuropathy behind neurogenic orthostatic hypotension; a dry mouth suggests volume depletion."],
   ["Warmth and nausea while voiding",
    "Warmth and nausea while voiding at night are the prodrome of situational micturition syncope, a reflex type."]],
  C(18), "manifestation"),

S("Neurogenic orthostatic", IO2,
  "Which examination finding supports diabetic autonomic neuropathy in a patient with orthostatic syncope?",
  [["Reduced sensation in both feet",
    "Correct. Decreased vibration and light-touch sensation in both feet marks long-standing diabetes with peripheral neuropathy, which supports diabetic autonomic neuropathy as the cause."],
   ["Dry oral mucous membranes",
    "Dry mucous membranes point to volume depletion, the usual cause of non-neurogenic orthostatic hypotension."],
   ["A rapid, regular rhythm",
    "A rapid regular rhythm with hypotension raises concern for an arrhythmia and cardiogenic syncope rather than autonomic neuropathy."],
   ["A heart rate above 120 standing",
    "A heart rate exceeding 120 within 10 minutes of standing is a criterion for postural orthostatic tachycardia syndrome, not an examination sign of neuropathy."]],
  C(31), "manifestation"),

]
