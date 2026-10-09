#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 16 (Pericardial Disease, Electrolytes, Drug Effects, and Special ECG
Patterns) pool into two 30s. Shared logic and asserted rules: tools/pdm_l1516_partlib.py.

EMPHASIS GROUPS come from the 7 October afternoon recording (two parts, 83 minutes): distinct
minutes in which each subject was spoken -- preexcitation and Wolff-Parkinson-White 18, bundle
branch block and paced rhythms 14, early repolarization 12, Sgarbossa 10, hyperkalemia 10, calcium
10, QT and QTc 10, pericarditis 9, reentrant tachycardias 8, hypothermia 7, Brugada 4 (but flagged
aloud: "for a test question ... which leads ... V1 through V3"), hypokalemia 4, thyroid 4,
amiodarone 4, tricyclic 4, pulmonary embolism 4, digoxin 3, magnesium and sodium 2. COPD and long QT
syndrome are syllabus objectives with no slide and no spoken minute; they get no question.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_l16_pool_a import POOL_A, SRC
from pdm_l16_pool_b import POOL_B
from pdm_l1516_partlib import run

GROUPS = [
  ({"Wolff-Parkinson-White", "Atrioventricular reentrant tachycardia"}, 5, 7),
  ({"Paced rhythms", "Left bundle branch block and pacing", "Sgarbossa's criteria"}, 3, 5),
  ({"Pericarditis", "Benign early repolarization", "Pericarditis versus early repolarization"}, 5, 7),
  ({"Brugada syndrome"}, 2, 3),
  ({"Hyperkalemia"}, 2, 3),
  ({"Hypokalemia"}, 1, 2),
  ({"Calcium disorders"}, 2, 3),
  ({"Hypothermia"}, 2, 3),
  ({"Thyroid disorders"}, 1, 2),
  ({"Digoxin toxicity"}, 1, 2),
  ({"Amiodarone toxicity"}, 1, 2),
  ({"Tricyclic antidepressant toxicity"}, 1, 2),
  ({"Pulmonary embolism"}, 1, 2),
  ({"Electrolytes without changes"}, 0, 1),
]
POOL = POOL_A + POOL_B

# TWINS: same fact asked twice, or one stem handing over another's answer (matched by stem substring).
TWINS = {
  "pericarditis-avr":  ["Which finding in lead aVR supports pericarditis", "has suspected acute pericarditis. Which tracing finding",
                        "Which diagnosis best fits the tracing"],
  "pericarditis-q":    ["but also ST depression in leads II and III", "Why can this not be called pericarditis"],
  "ber-signif":        ["What clinical significance does this pattern carry", "Which other name does this pattern carry",
                        "reads normal variant ST elevation"],
  "ber-name":          ["has a routine 12-lead, shown here. Which interpretation", "has benign early repolarization. Which set",
                        "What is the circled notch"],
  "v6-lead":           ["Which lead is used to tell them apart", "the blue box marks the ST elevation",
                        "with the ST elevation boxed in blue"],
  "v6-ratio":          ["Which ST-to-T ratio suggests pericarditis", "shows much more T wave than ST elevation"],
  "brugada-a":         ["In which leads are its findings seen", "show convex, coved ST elevation. Which Brugada type",
                        "right precordial leads are shown", "Which diagnosis fits the pattern in V1 and V2",
                        "In whom is it most commonly seen"],
  "sgarbossa-what":    ["Which finding meets Sgarbossa's criteria", "Which ST change in V1 to V3 counts",
                        "How much DISCORDANT".replace("DISCORDANT", "discordant")],
  "sgarbossa-why":     ["Why are Sgarbossa's criteria needed", "Why is an ST-elevation infarction hard to locate",
                        "Which criteria are used to identify an acute infarction"],
  "paced":             ["has a ventricular paced rhythm. Which set of features", "Which rhythm is it?",
                        "What are the sharp, narrow vertical lines"],
  "osborn":            ["Which diagnosis are they frequently mistaken for", "What are the notches at the end of each QRS",
                        "Which condition most likely produced it"],
  "wpw-name":          ["Which triad defines it", "What is his accessory pathway called", "Which is the most common one",
                       "Which pattern does it show?"],
  "wpw-delta":         ["What is the slurred upstroke at the start of each QRS", "What causes the slurring"],
  "avrt-anti":         ["has antidromic reentrant tachycardia. How does the circuit run",
                        "Which rhythm can it be impossible to tell apart", "Which rhythm is most likely?"],
  "hyperk":            ["Which finding on it is the early sign", "Without treatment, which pattern comes next",
                        "Which set lists its classic tracing signs", "with tall, peaked T waves and a slow rate"],
  "hypok":             ["What are the arrowed waves that follow each T wave", "2.9 mEq/L",
                        "with flattened T waves and the arrowed waves after them", "3.1 mEq/L"],
  "hypoca":            ["a long, flat ST segment before a normally shaped T wave", "Which interval change accompanies his long ST",
                        "What does it look like in hypocalcemia"],
  "hyperca":           ["with almost no ST segment", "Which phase of the cardiac action potential is shortened",
                        "12.8 mg/dL", "Why does her ST segment lengthen"],
  "hypothyroid":       ["Which endocrine disorder best fits it", "has hypothyroidism. Which tracing finding"],
  "hyperthyroid":      ["has hyperthyroidism. Which tracing finding is the most commonly", "does not have sinus tachycardia"],
  "tca-qt":            ["Which interval change fits the overdose", "Which pair of tracing changes does the overdose produce"],
}
for q in POOL:
    for label, subs in TWINS.items():
        if any(x in q["q"] for x in subs):
            assert "twin" not in q, "two twin groups match: " + q["q"][:60]
            q["twin"] = label
for label, subs in TWINS.items():
    got = sum(1 for q in POOL if q.get("twin") == label)
    assert got >= 2, "twin group %s matched %d stems" % (label, got)
# CONFLICTS: any A-stem with any B-stem hands over an answer.
CONFLICTS = [
  (["Which triad defines it"], ["has a short PR interval. Why is it short", "shows a delta wave. What causes",
                                "What is the slurred upstroke at the start"]),
  (["Which criteria are used to identify an acute infarction"],
   ["Which finding meets Sgarbossa's criteria", "Which ST change in V1 to V3 counts", "How much discordant"]),
  (["Which rhythm is it?"], ["Which finding meets Sgarbossa's criteria"]),
  (["Below which core temperature"], ["Which condition most likely produced it"]),
  (["has a routine 12-lead, shown here. Which interpretation"], ["Which lead is used to tell them apart"]),
]
OUT = os.path.join(HERE, "pdm_l16_sets.json")

if __name__ == "__main__":
    run(POOL, GROUPS, n_io=9, out=OUT, seed=20261008, min_img=15, src=SRC, conflicts=CONFLICTS)
