#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split and guard the Clinical Pathophysiology Lecture 9 pool into 2 x 30.

Pulmonary Pathophysiology (Dr. Matthew Ward, 2026-10-20). No deck was posted; the
deck is Jaxon's rebuild from the lecture video (109 slides, numbering below), and the
minutes each slide was ON SCREEN in the video weight the 60 questions by topic
(clinpath_e2_weighted.py). The pool is larger than 60 on purpose -- the surplus is
what the cumulative master exams draw on once Lecture 10 is in.

Guards (clinpath_e2_weighted.check): four options, stems ask something, cite nothing
and are no vignette; NO MANAGEMENT in any stem, option or explanation; 60+ character
explanations; a `mis` tag on every distractor; numeric and ordered option sets kept
ascending; positions even; key not guessable by length; every syllabus objective
(including each of objective d's nine diseases) in at least one set.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from clinpath_pulmonary_pool_a import QUESTIONS as POOL_A
from clinpath_pulmonary_pool_b import QUESTIONS as POOL_B
from clinpath_e2_weighted import split

POOL = POOL_A + POOL_B
SEED = 20261022

# Minutes each slide of the rebuilt deck was on screen in the two-part lecture video
# (Exam 2/recordings/cp-l9-pulmonary-2026-10-20.slides-timing.json, "min"; 176.8 min in
# all). Kept here so the split is reproducible without the inbox.
MINUTES = {
    1: 1.27, 2: 0.10, 3: 2.10, 4: 4.40, 5: 0.80, 6: 0.30, 7: 4.83, 8: 2.20, 9: 3.70, 10: 4.20,
    11: 0.60, 12: 0.83, 13: 0.53, 14: 2.47, 15: 0.33, 16: 0.80, 17: 2.20, 18: 0.60, 19: 0.47,
    20: 3.80, 21: 2.07, 22: 1.87, 23: 2.40, 24: 0.37, 25: 1.97, 26: 2.13, 27: 1.97, 28: 0.47,
    29: 0.47, 30: 1.70, 31: 0.53, 32: 0.63, 33: 2.03, 34: 2.30, 35: 3.03, 36: 0.43, 37: 1.00,
    38: 0.60, 39: 2.40, 40: 2.73, 41: 0.77, 42: 0.53, 43: 1.17, 44: 1.93, 45: 0.90, 46: 0.70,
    47: 2.00, 48: 2.27, 49: 2.27, 50: 2.37, 51: 2.07, 52: 0.33, 53: 1.97, 54: 2.53, 55: 3.57,
    56: 0.60, 57: 0.83, 58: 0.50, 59: 2.27, 60: 1.97, 61: 2.73, 62: 0.60, 63: 0.53, 64: 2.02,
    65: 0.33, 66: 4.13, 67: 0.67, 68: 1.03, 69: 2.13, 70: 0.07, 71: 2.10, 72: 0.67, 73: 0.67,
    74: 2.30, 75: 1.27, 76: 2.27, 77: 0.63, 78: 0.87, 79: 2.17, 80: 1.07, 81: 0.83, 82: 2.43,
    83: 2.77, 84: 2.30, 85: 3.63, 86: 0.37, 87: 0.77, 88: 2.03, 89: 2.20, 90: 3.03, 91: 0.63,
    92: 1.93, 93: 2.23, 94: 1.33, 95: 3.20, 96: 1.63, 97: 0.57, 98: 1.90, 99: 0.63, 100: 1.90,
    101: 1.50, 102: 1.30, 103: 1.10, 104: 0.07, 105: 2.60, 106: 2.07, 107: 0.67, 108: 1.07,
    109: 2.66,
}

# Topic -> the slides it was taught on (title and objectives slides are not topics;
# slides 11-13, the acute respiratory distress syndrome pictures shown inside the acute
# respiratory failure section, count with that section).
TOPICS = {
    "Anatomy and function": [3, 4, 5],
    "Acute respiratory failure": [6, 7, 8, 9, 10, 11, 12, 13, 14],
    "Pulmonary hypertension": [15, 16, 20, 21, 22, 23],
    "Capillary fluid pressures": [17, 18, 19],
    "Pulmonary malignancies": [24, 25, 26, 27, 28],
    "Obstructive diseases overview": [29, 30, 31, 32, 33, 34],
    "Asthma": [35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
    "Acute bronchitis": [45, 46, 47],
    "Chronic bronchitis": [48, 49, 50, 51],
    "Emphysema and the obstructive pattern": [52, 53, 54, 55, 56, 57, 58, 59],
    "Bronchiectasis": [60, 61, 62, 63, 64],
    "Restrictive diseases overview": [65, 66, 67, 68, 82],
    "Interstitial lung disease": [69, 70, 71, 72, 73, 74],
    "Sarcoidosis, hypersensitivity and occupational disease": [75, 76, 77, 78, 79, 80, 81],
    "Acute respiratory distress syndrome": [83, 84, 85],
    "Pneumothorax": [86, 87, 88, 89, 90, 91],
    "Pleural effusion": [92, 93, 94, 95, 96, 97, 98],
    "Obstructive sleep apnea": [99, 100, 101, 102, 103],
    "Pneumonia": [104, 105, 106, 107, 108, 109],
}

if __name__ == "__main__":
    split(POOL, TOPICS, MINUTES, SEED, "clinpath_pulmonary_sets.json", "Lecture 9 Pulmonary")
