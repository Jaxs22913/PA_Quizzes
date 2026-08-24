#!/usr/bin/env python3
"""Render CMS I Lecture 9 Set 1 — the two objective-style quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l9_set1.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Actinic keratosis", "Squamous cell carcinoma", "Basal cell carcinoma",
         "Melanoma", "Kaposi sarcoma", "Cutaneous T-cell lymphoma", "Nail unit"]
INTRO = ("Thirty questions on pre-malignant and malignant cutaneous lesions, drawn from the syllabus "
         "instructional objectives. Covers the systematic approach to describing a lesion before naming "
         "it, actinic keratosis and its progression risk, squamous and basal cell carcinoma with their "
         "different ultraviolet exposure patterns and their different Mohs indications, malignant "
         "melanoma with the recognition mnemonic, sentinel node thresholds and re-excision margins, "
         "Kaposi sarcoma by clinical form, cutaneous T-cell lymphoma, and the nail unit neoplasms. "
         "<b>Where the lecture audio and the slide disagree on a fact, the slide wins</b> &mdash; every "
         "question here is grounded in the PowerPoint. Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = ("premalignant-and-malignant-lesions-quiz.html" if n == 1
          else "premalignant-and-malignant-lesions-quiz-version-2.html")
    html = render(title=f"Pre-Malignant and Malignant Cutaneous Lesions Quiz {n} &mdash; CMS I Exam 1",
                  h1="Pre-Malignant and Malignant Cutaneous Lesions",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 9 &middot; Objective set",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
