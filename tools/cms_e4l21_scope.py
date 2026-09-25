# -*- coding: utf-8 -*-
"""Lecture 21 Hypotension -- scope for the guarded Exam 4 partition.

The objectives are the SYLLABUS's, verbatim (page 13, "Hypotension"), with the
two lettered sub-lists written inline. They are provenance: the partition checks
every question carries one of them, and the acronym guard does not read them.

Scope caps, from Carter's own words in the recording (emphasis report C1-C5):
  - building a differential (the four-question method and the VINDICATES
    mnemonic) is "not a testing thing";
  - the MDM paragraphs on the worked cases are "not testable";
  - no dosing and no mechanism-of-action questions;
  - shock beyond a one-line list is "a whole other lecture";
  - case DISPOSITIONS were spoken, never written -- not keyed.
Slide 26 (Building a Differential) is therefore hard-excluded, and the terms
that would only come from it are banned. Slide 20's blood-pressure-by-age table
is DEFECTIVE (duplicated age rows), so no question cites it for a number; the
concept on its text ("norms are affected by age", "snapshot in time") is kept.
"""
DECK = "Hypotension CM1 2026 - Carter.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)

IO1 = "Define hypotension"
IO2 = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
       "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
       "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
       "referrals, patient education, and prognosis of the following hypotensive disorders: "
       "a. Orthostatic hypotension b. Vasovagal hypotension")
IO3 = "Distinguish between acute and chronic hypotension"
IO4 = ("Develop a differential diagnosis for a patient presenting with hypotension based on history, "
       "physical examination, and diagnostic findings.")
IO5 = ("Identify medical care strategies for hypotension in the lecture topic list for the following "
       "populations. a. infant b. child c. adolescent d. adult e. elderly")
IOS = [IO1, IO2, IO3, IO4, IO5]

# Slide 26: "Building a Differential" + VINDICATES -- declared not testable (C1).
EXCLUDED_SLIDES = {26}

SCOPE_BANNED = [
    r"\bVINDICATES\b",
    r"\bmedical decision making\b",
    r"\bdisposition\b",               # dispositions are audio-only
    r"\bcan'?t[- ]miss\b",            # the differential-building method
    r"\balpha-1 agonist\b",           # drug mechanisms (C3)
    r"\bmineralocorticoid\b",
    r"\bmetaboli[sz]es? into\b",
    r"\bHEAD[, ]+HEART\b",            # low-weight mnemonic (C6)
]

# A named finding in a vignette stem must carry its description.
NAMED = {
    "supine hypertension": "lying",
}
