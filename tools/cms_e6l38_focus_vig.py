# -*- coding: utf-8 -*-
"""Lecture 38 STUDY-FOCUS pool, vignettes -- written 2026-10-31 for the focus points the existing Lecture 38
pools left thin (tools/cms_e6_focus_coverage.json): a tuberculin skin test of 5 mm or more in human
immunodeficiency virus infection or a recent close contact (the existing vignettes for both were flagged in
review), and what identifies the species after a positive acid-fast smear.

NOT a topic-quiz pool (the name does not match cms_e6l38_vig_*.py). Read by tools/cms_e6_focus_partition.py
and tools/cms_e6_masters_partition.py through the Lecture 38 vignette guards. "focus" = the study-focus point
ids each question practises (tools/cms_e6_focus_points.py).

WRITER.md v1 + EXPLAIN_DEEP.md; every claim on a slide of the cited deck (the study-focus slide 41 counts).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e6l38_scope import *


def V(topic, io, q, opts, cite, slot, lead, focus):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; d["lead"] = lead; d["focus"] = list(focus); return d


BIO = "Mycobacterial biology"
TST = "Tuberculin skin test"

QUESTIONS = [

V(TST, IO_A,
  "A 37-year-old woman with human immunodeficiency virus infection has a tuberculin skin test read at 48 hours, showing 6 mm of transverse induration. She has no cough, fever or weight loss. Which is the most appropriate next step?",
  [["Evaluate for active tuberculosis disease",
    "Correct. In human immunodeficiency virus infection the skin test cut-off is 5 mm, so 6 mm is positive. A positive test shows infection, not whether it is latent or active, so clinical evaluation and chest imaging come next to rule out active disease before any preventive therapy."],
   ["Start latent-infection treatment now",
    "The test is positive, but neither the skin test nor the blood test separates latent infection from disease. Tell: tuberculosis disease must be excluded with clinical evaluation and chest imaging before latent-infection treatment starts.", "wrong stage or severity"],
   ["No action; below the 10 mm cut-off",
    "10 mm is the cut-off for increased exposure risk, selected medical risks, high-risk congregate settings and children under 5. Tell: human immunodeficiency virus infection puts her in the 5 mm group, and her 6 mm meets it.", "wrong stage or severity"],
   ["Repeat the skin test in 8 to 10 weeks",
    "Repeating a test 8 to 10 weeks after the last exposure is for an early negative result after a recent exposure. Tell: her result is already positive at her 5 mm cut-off, so the next step is evaluation for disease, not a retest.", "adjacent fact"]],
  CS(19, 22, 41), "test finding", "next step", ["l38-tst5", "l38-rule-out"]),

V(TST, IO_A,
  "A 29-year-old woman's roommate was diagnosed with infectious pulmonary tuberculosis 10 weeks ago, and they have lived apart since. She has no symptoms. Her tuberculin skin test, read at 72 hours, shows 7 mm of induration. How should this result be interpreted?",
  [["Positive; recent close contacts use 5 mm",
    "Correct. A recent close contact of infectious tuberculosis is in the 5 mm group, with human immunodeficiency virus infection, transplant, major immunosuppression and imaging suggesting prior tuberculosis. 7 mm is at least 5 mm, so the test is positive and she needs evaluation for active disease."],
   ["Positive; any measurable induration counts",
    "The result is positive, but not because any induration counts: the skin test is read against the patient's risk-based cut-off of 5, 10 or 15 mm. Tell: her positive result comes from the 5 mm threshold for recent close contacts.", "common lay belief"],
   ["Negative; her cut-off is 10 mm",
    "10 mm applies to increased exposure risk, selected medical risks, high-risk congregate settings and children under 5. Tell: living with a person who has infectious pulmonary tuberculosis makes her a recent close contact, whose cut-off is 5 mm.", "wrong stage or severity"],
   ["Negative; her cut-off is 15 mm",
    "15 mm is the cut-off for a person with no known tuberculosis risk factors, which does not describe her. Tell: a recent close contact has a major risk, so her cut-off is 5 mm and her 7 mm of induration is positive.", "wrong stage or severity"]],
  CS(20, 22, 41), "test finding", "classify", ["l38-tst5"]),

V(BIO, IO_A,
  "A 71-year-old woman with bronchiectasis has had a chronic productive cough and weight loss. Her sputum acid-fast smear is positive. Which testing will identify the mycobacterial species?",
  [["Molecular testing and culture",
    "Correct. A positive acid-fast smear supports mycobacteria but cannot distinguish tuberculosis from nontuberculous mycobacteria. The species is confirmed with molecular testing and culture, and it matters because transmission and treatment differ."],
   ["A repeat acid-fast smear",
    "A smear identifies a group of organisms, the acid-fast bacilli, however often it is repeated; it does not distinguish tuberculosis from nontuberculous mycobacteria. Tell: species identification needs molecular testing and culture.", "adjacent fact"],
   ["An interferon-gamma release assay",
    "An interferon-gamma release assay is a blood test of the immune response to tuberculosis infection; it does not identify the organism growing in her sputum. Tell: the isolate's species comes from molecular testing and culture of the specimen.", "confused mechanism or drug class"],
   ["Chest computed tomography",
    "Computed tomography can show patterns such as nodular bronchiectasis or fibrocavitary disease, but imaging supports suspicion and cannot confirm the organism. Tell: only microbiology, molecular testing and culture, names the species.", "adjacent fact"]],
  CS(4, 5, 24, 27, 39, 41), "test finding", "test", ["l38-smear"]),
]
