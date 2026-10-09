#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 15 (Ischemia, Injury, and Infarction) pool into two 30s.

House format is 2x30 for the lecture (one topic per lecture, as Lectures 1-10). The remainder is
held back for the Exam 3 master exams (Lectures 11-16; Lab 3 is not built, Jaxon 2026-10-08).
Shared logic and the asserted rules live in tools/pdm_l1516_partlib.py.

EMPHASIS GROUPS come from the 7 October recording (three parts, 109 minutes): distinct minutes in
which each subject was spoken -- ST-elevation infarction and acute coronary syndrome context 44,
ST elevation 30, localization by leads 28, coronary anatomy 25, ST depression 24, J point and
baseline 18, reciprocal changes 14, right ventricular involvement and V4R 14, posterior infarction
11, hyperacute T waves 8, Q waves 7. Each group is (topics, minimum per set, maximum per set).
Time spoken only re-weights; it never adds a question the deck cannot ground.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_l15_pool_a import POOL_A, SRC
from pdm_l15_pool_b import POOL_B
from pdm_l1516_partlib import run

GROUPS = [
  ({"Localization", "ST-elevation criteria", "Artery and territory"}, 6, 10),
  ({"Coronary anatomy"}, 2, 4),
  ({"Reciprocal changes"}, 1, 4),
  ({"Posterior infarction"}, 1, 4),
  ({"Right ventricular involvement"}, 1, 4),
  ({"ST depression", "Subendocardial ischemia", "Transmural ischemia"}, 2, 4),
  ({"Pathologic Q waves"}, 2, 5),
  ({"Hyperacute T waves"}, 2, 4),
  ({"J point and baseline"}, 2, 3),
]
POOL = POOL_A + POOL_B

# TWINS: questions that ask the same fact (or where one stem hands over the other's answer). The
# search is penalized for putting two of a twin group in one set. Matched by stem substring.
TWINS = {
  "first-sign":       ["very first sign of his cardiac ischemia", "Why does this finding matter",
                       "If ischemia began"],
  "hyperacute-name":  ["What are these T waves", "which early ischemic finding is visible", "How are these T waves described"],
  "posterior-next":   ["isolated ST depression in V1 to V4 and no ST elevation in any lead. Which test",
                       "with ST depression in V1 to V3 and no ST elevation anywhere. Which is the next",
                       "Until proven otherwise"],
  "posterior-confirm":["Which finding confirms a posterior wall", "V8 and V9 show ST elevation"],
  "high-lateral":     ["ST elevation in I and aVL with reciprocal depression in III and aVF. Which region",
                       "Which region does the ST elevation localize to?"],
  "rv-artery":        ["also involves her right ventricle", "Occlusion of which artery explains this?"],
  "rv-confirm":       ["Which finding confirms right ventricular involvement", "What does this confirm?"],
  "reciprocal-rule":  ["How should the ST depression be considered", "How should the ST depression in leads I and aVL",
                       "Which leads carry the reciprocal ST depression"],
  "q-criteria":       ["Which duration makes a Q wave pathologic", "What is the deep first deflection?",
                       "Which depth relative to the R wave"],
  "q-meaning":        ["What do they indicate?", "What does the deep first deflection represent",
                       "What has happened to the tissue", "Which finding indicates infarction rather",
                       "Which finding in leads III and aVF indicates death"],
  "subendo":          ["Which layer of the heart does this pattern", "ST-segment depression across nearly every lead",
                       "Which finding is present across most leads"],
  "tp":               ["what should his J point be compared with", "Which usual baseline has disappeared",
                       "with no visible TP segment"],
  "inferior-artery":  ["Which artery most likely supplies the affected wall", "bottom portion of her left ventricle"],
}
for q in POOL:
    for label, subs in TWINS.items():
        if any(x in q["q"] for x in subs):
            assert "twin" not in q, "two twin groups match: " + q["q"][:60]
            q["twin"] = label
for label, subs in TWINS.items():
    got = sum(1 for q in POOL if q.get("twin") == label)
    assert got >= 2, "twin group %s matched %d stems" % (label, got)
# CONFLICTS: one family's stems hand over the other family's answers (any A with any B).
POST_A = ["isolated ST depression in V1 to V4 and no ST elevation in any lead. Which test",
          "with ST depression in V1 to V3 and no ST elevation anywhere. Which is the next",
          "Until proven otherwise", "has an infarction with no facing lead"]
POST_B = ["V8 and V9 show ST elevation", "had V4, V5 and V6 moved to her back", "needs a posterior tracing",
          "posterior tracing has been recorded", "has an isolated posterior wall infarction"]
CONFLICTS = [
  (POST_A, POST_B),
  (["hypotension, clear lungs and distended neck veins. His 12-lead"],
   ["Which findings should raise suspicion of right ventricular", "needs lead V4R", "has a right-sided tracing recorded",
    "had V4 moved to the right fifth", "right-sided tracing is shown"]),
  (["had V4 moved to the right fifth"], ["needs lead V4R", "has a right-sided tracing recorded"]),
  (["right-sided tracing is shown"], ["has a right-sided tracing recorded"]),
  (["no standard lead faces directly"], ["has an infarction with no facing lead"] + POST_B),
  # the anterior-wall artery picture question and the text question that names its supply
  (["with ST elevation in V1 to V3. Occlusion of which artery"],
   ["supplies the front of the left ventricle and the front of the septum"]),
]
OUT = os.path.join(HERE, "pdm_l15_sets.json")

if __name__ == "__main__":
    run(POOL, GROUPS, n_io=7, out=OUT, seed=20261008, min_img=13, src=SRC, conflicts=CONFLICTS)
