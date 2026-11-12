#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split and guard the Clinical Pathophysiology Lecture 10 pool into 2 x 30.

Pathophysiology of Blood Disorders (Dr. Matthew Ward, 2026-11-10), deck "Pathophysiology
of Blood Disorders SV Fall 2026.pptx" (51 slides). The two-part Notability recording
(47.7 + 48.8 min, one transcript; Notability kept no ASR of its own for it) was read
against the slides and the MINUTES each topic was spoken weight the 60 questions
(clinpath_e2_weighted.py). Part 1 opens on slide 3 and ends on slide 26; part 2 opens on
slide 27. The pool is larger than 60 on purpose -- the surplus is held for repairs.

Guards (clinpath_e2_weighted.check): four options, stems ask something, cite nothing
and are no vignette; NO MANAGEMENT in any stem, option or explanation; 60+ character
explanations; a `mis` tag on every distractor; numeric and ordered option sets kept
ascending; positions even; key not guessable by length; every syllabus objective (a-j)
in at least one set.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from clinpath_blood_pool_a import QUESTIONS as POOL_A
from clinpath_blood_pool_b import QUESTIONS as POOL_B
from clinpath_e2_weighted import split

POOL = POOL_A + POOL_B
SEED = 20261112

# Minutes spoken per topic, from the transcript timestamps of the two parts
# (Exam 2/recordings/cp-l10-blood-disorders-2026-11-10-part{1,2}.transcript.txt; boundaries in
# the .flags.md beside them). Each topic's minutes sit on its first slide so the split stays
# reproducible without the inbox. Slides 1-2 (title, objectives) were not recorded.
MINUTES = {
    3: 5.5, 6: 5.5, 9: 6.1, 11: 4.3, 14: 7.3, 18: 3.3, 19: 7.9, 23: 5.1, 25: 2.8,
    27: 4.9, 29: 8.3, 33: 6.2, 35: 4.9, 37: 6.9, 40: 1.8, 41: 4.0, 42: 7.1, 45: 3.1, 49: 1.6,
}

# STATED EMPHASIS. Ward named five places outright ("These are the only lab values that you
# guys should have memorized" -- the neutropenia grades, slide 9; "important for you guys to know
# the different diagnoses here and how to differentiate between them" -- slide 18; "Definitely
# important to know this slide" -- slide 23; "you guys need to know your cascade ... Make sure you
# know thrombin generation ... know your extrinsic, intrinsic" -- slides 43-44; "Definitely know
# this slide here" -- slide 46). Minutes alone under-weight a slide he flagged and then moved
# through quickly, so a flagged topic's minutes count one and a half times.
STATED = {9: 1.5, 18: 1.5, 23: 1.5, 42: 1.5, 45: 1.5}
MINUTES = {s: m * STATED.get(s, 1.0) for s, m in MINUTES.items()}

TOPICS = {
    "Blood composition and hematopoiesis": [3, 4, 5],
    "Leukocytes and their counts": [6, 7, 8],
    "Neutrophils and bands": [9, 10],
    "Monocytes, eosinophils and basophils": [11, 12, 13],
    "B cells and clonality": [14, 15, 16, 17],
    "Bone marrow neoplasms": [18],
    "Leukemia": [19, 20, 21, 22],
    "Lymphoid neoplasms": [23, 24],
    "Risk factors and neoplasm lineages": [25, 26],
    "Multiple myeloma": [27, 28],
    "Red-cell indices and morphology": [29, 30, 31, 32],
    "Anemia by cell size and marrow response": [33, 34],
    "Anemia definition and blood loss": [35, 36],
    "Hemolytic anemia": [37, 38, 39],
    "Diminished erythropoiesis": [40],
    "Polycythemia": [41],
    "Coagulation reactions": [42, 43, 44],
    "Coagulation disorders": [45, 46, 47, 48],
    "Platelet disorders": [49, 50, 51],
}

if __name__ == "__main__":
    split(POOL, TOPICS, MINUTES, SEED, "clinpath_blood_sets.json", "Lecture 10 Blood Disorders")
