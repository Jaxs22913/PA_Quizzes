#!/usr/bin/env python3
"""Render CMS I Lecture 9 Set 2 — the two vignette quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l9_set2.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Actinic keratosis", "Squamous cell carcinoma", "Basal cell carcinoma",
         "Melanoma", "Kaposi sarcoma", "Cutaneous T-cell lymphoma", "Nail unit"]
INTRO = ("Thirty patient vignettes on pre-malignant and malignant cutaneous lesions. Each gives you a "
         "presentation and asks for the diagnosis, the next step, the test, the treatment or the "
         "counselling point &mdash; and the lead-in decides the answer, so read it before the choices. "
         "The wrong options are the neighbouring lesion in the same differential or the right lesion at "
         "the wrong stage: the pearly border against the conical hard nodule, the intermittent against "
         "the cumulative sun exposure pattern, the Breslow threshold that shifts when the report notes "
         "ulceration. <b>Where the lecture audio and the slide disagree on a fact, the slide wins.</b> "
         "Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = ("premalignant-and-malignant-lesions-vignettes.html" if n == 1
          else "premalignant-and-malignant-lesions-vignettes-version-2.html")
    html = render(title=f"Pre-Malignant and Malignant Cutaneous Lesions Vignettes {n} &mdash; CMS I Exam 1",
                  h1="Pre-Malignant and Malignant Cutaneous Lesions",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 9 &middot; Vignettes",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
