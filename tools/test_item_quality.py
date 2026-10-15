#!/usr/bin/env python3
"""Unit tests for the deterministic flags in tools/check_item_quality.py (2026-10-15).
Run: python3 tools/test_item_quality.py -- synthetic items, no quiz page is read."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blind_review as R
import check_item_quality as C


def item(stem, texts, key=0, mis=None):
    q = {"q": stem, "c": key, "opts": [[t, "expl " + t] + ([mis[i]] if mis else []) for i, t in enumerate(texts)], "cite": "D.pptx, Slide 1"}
    return R.Q("F", "F/x.html", 0, q)


def kinds(q, scoped=False):
    f, w = C.check_question(q, scoped)
    return {k for k, _ in f}, {k for k, _ in w}


F = C.KINDS_FAIL
W = C.KINDS_WARN
ok = ["Aspirin", "Heparin", "Warfarin", "Apixaban"]
assert kinds(item("Which drug?", ok)) == (set(), set())
# FAIL kinds
assert F[0] in kinds(item("Q?", ["Aspirin", "aspirin.", "Heparin", "Warfarin"]))[0]
assert F[1] in kinds(item("Q?", ["Oral anticoagulation with warfarin", "Oral anticoagulation with warfarin and aspirin", "Heparin", "Rest"]))[0]
assert F[1] not in kinds(item("Q?", ["Aspirin", "Aspirin therapy daily", "Heparin", "Warfarin"]))[0]      # contained part is <= 3 words
assert F[2] in kinds(item("Q?", ["Aspirin", "Heparin", "All of the above", "Warfarin"]))[0]
assert F[2] in kinds(item("Q?", ["Aspirin", "Both A and B", "Heparin", "Warfarin"]))[0]
assert F[2] in kinds(item("Q?", ["Aspirin", "None of the above", "Heparin", "Warfarin"]))[0]
# a/an clue: key is the only vowel-initial answer after "an"; fine when every option fits
assert F[3] in kinds(item("The patient most likely has an", ["Aneurysm", "Stroke", "Tumor", "Cyst"]))[0]
assert F[3] in kinds(item("This is an", ["Stroke", "Embolus", "Tumor", "Cyst"]))[0]                  # key is the odd one out
assert F[3] in kinds(item("This is a", ["Stroke", "Embolus", "Tumor", "Cyst"], key=1))[0]            # key vowel after "a"
assert F[3] not in kinds(item("The patient most likely has an", ["Aneurysm", "Embolus", "Infarct", "Ulcer"]))[0]
assert F[3] not in kinds(item("Which is the cause?", ["Aneurysm", "Stroke", "Tumor", "Cyst"]))[0]
assert C.starts_vowel_sound("Hour-glass") and not C.starts_vowel_sound("Uterine") and C.starts_vowel_sound("MRI scan")
assert not C.starts_vowel_sound("Unilateral") and C.starts_vowel_sound("8 weeks") and C.starts_vowel_sound("Umbilical")
# numeric order
assert F[4] in kinds(item("Q?", ["10 mm", "2 mm", "7 mm", "5 mm"]))[0]
assert F[4] not in kinds(item("Q?", ["2 mm", "5 mm", "7 mm", "10 mm"]))[0]
assert F[4] not in kinds(item("Q?", ["10 mm", "7 mm", "5 mm", "2 mm"]))[0]
# WARN kinds
assert W[0] in kinds(item("Q?", ["Rest", "Always give aspirin", "Heparin", "Warfarin"]))[1]
assert W[0] not in kinds(item("Q?", ["Never smoke", "Always give aspirin", "Heparin", "Warfarin"]))[1]
assert W[1] in kinds(item("Which organism causes cholecystitis?", ["Bacterial cholecystitis", "Heparin", "Warfarin", "Rest"]))[1]
assert W[1] not in kinds(item("Which organism causes cholecystitis?", ["Bacterial cholecystitis", "Heparin cholecystitis", "Warfarin", "Rest"]))[1]
assert W[3] in kinds(item("A 60-year-old Black man has pain. Which test?", ok))[1]
assert W[3] not in kinds(item("Her heart race increased. Which test?", ok))[1]
assert W[3] not in kinds(item("White blood cells are raised. Which test?", ok))[1]
assert W[4] in kinds(item("Q?", ok), scoped=True)[1]
assert W[4] not in kinds(item("Q?", ok, mis=["m", "m", "m", "m"]), scoped=True)[1]
assert W[4] not in kinds(item("Q?", ok), scoped=False)[1]
# near-duplicate stems (word 5-gram Jaccard >= 0.6)
a = item("Which of the following is the most likely cause of acute chest pain after surgery?", ok)
b = item("Which of the following is the most likely cause of acute chest pain after surgery now?", ok)
c = item("What drug lowers blood pressure by blocking the angiotensin converting enzyme in kidneys?", ok)
assert len(C.near_duplicates([a, b, c])) == 1
print("test_item_quality: all assertions passed")
