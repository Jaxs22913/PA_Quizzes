#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split and guard the Clinical Pathophysiology Lecture 8 pool into 2 x 30.

Immunity (Dr. Matthew Ward, guest lecture, 2026-10-19). A narrated deck: each
slide carries its own narration clip, transcribed per slide, so the minutes each
slide was narrated are exact. Those minutes weight the 60 questions by topic
(clinpath_e2_weighted.py); the pool is larger than 60 on purpose -- the surplus is
what the cumulative master exams draw on once Lecture 10 is in.

Guards (clinpath_e2_weighted.check): four options, stems ask something, cite
nothing and are no vignette; NO MANAGEMENT in any stem, option or explanation
(slide 62's first-line anaphylaxis treatment is never used); 60+ character
explanations; a `mis` tag on every distractor; ordered Type I-IV and numeric
option sets kept ascending; positions even; key not guessable by length.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from clinpath_immunity_pool_a import QUESTIONS as POOL_A
from clinpath_immunity_pool_b import QUESTIONS as POOL_B
from clinpath_e2_weighted import split

POOL = POOL_A + POOL_B
SEED = 20261022

# Minutes of narration per slide, from the per-slide transcript of the narrated deck
# (Exam 2/recordings/cp-l8-immunity-2026-10-19.slides.jsonl, "seconds" / 60; 118.4 min
# in all). Slides 2-3 (objectives) carry no narration. Kept here so the split is
# reproducible without the inbox.
MINUTES = {
    1: 1.18, 4: 1.62, 5: 0.89, 6: 1.49, 7: 1.04, 8: 1.25, 9: 1.73, 10: 2.39, 11: 2.09, 12: 1.74,
    13: 1.96, 14: 2.62, 15: 3.31, 16: 1.43, 17: 1.29, 18: 2.57, 19: 2.08, 20: 0.76, 21: 2.18,
    22: 3.12, 23: 1.14, 24: 1.75, 25: 2.23, 26: 1.23, 27: 0.80, 28: 0.83, 29: 0.24, 30: 3.07,
    31: 1.50, 32: 1.60, 33: 0.33, 34: 0.37, 35: 2.21, 36: 1.68, 37: 0.41, 38: 2.26, 39: 2.21,
    40: 1.07, 41: 2.17, 42: 0.91, 43: 1.24, 44: 4.30, 45: 1.57, 46: 2.03, 47: 1.91, 48: 0.30,
    49: 2.44, 50: 1.51, 51: 0.43, 52: 0.64, 53: 0.72, 54: 1.88, 55: 1.59, 56: 1.06, 57: 0.55,
    58: 0.84, 59: 0.51, 60: 1.44, 61: 1.83, 62: 2.11, 63: 2.19, 64: 2.09, 65: 2.56, 66: 1.39,
    67: 0.98, 68: 1.19, 69: 1.68, 70: 2.06, 71: 1.55, 72: 0.41, 73: 0.49, 74: 0.52, 75: 0.94,
    76: 3.40, 77: 3.28,
}

# Topic -> the slides it was taught on (title slide 1 is not a topic).
TOPICS = {
    "Lymphatic system": [4, 5, 6, 7, 8],
    "Immunity and specificity": [9, 10],
    "Active, passive and innate immunity": [11, 12, 13],
    "Blood cells in immunity": [14, 15, 16, 17, 18, 19, 20, 21],
    "B cells and plasma cells": [22, 23],
    "T cells and cellular immunity": [24, 25, 30, 31, 32, 33, 34],
    "Phagocytosis": [26, 27, 28, 29],
    "Primary and secondary response": [35, 36, 37],
    "Electrophoresis": [38],
    "Antibody structure": [39, 40, 41, 42, 43],
    "Antibody classes": [44, 45, 46],
    "Antibody functions": [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
    "Hypersensitivity": [60, 61, 62, 63, 64, 65],
    "Complement": [66, 67, 68, 69, 70, 71, 72, 73, 74, 75],
    "Immunodeficiency and aging": [76, 77],
}

if __name__ == "__main__":
    split(POOL, TOPICS, MINUTES, SEED, "clinpath_immunity_sets.json", "Lecture 8 Immunity")
