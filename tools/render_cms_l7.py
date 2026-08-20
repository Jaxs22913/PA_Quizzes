#!/usr/bin/env python3
"""Render CMS I Lecture 7 Set 1 — the two objective-style Benign Skin Lesions quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l7_set1.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Corns &amp; calluses", "Keloid vs hypertrophic scar", "Pressure injury staging",
         "Cysts &amp; keratoacanthoma", "Vascular lesions"]
INTRO = ("Thirty questions on benign skin lesions, drawn from the syllabus instructional objectives. "
         "Covers corns and calluses against the wart that mimics them, abnormal wound healing as keloid "
         "and hypertrophic scar, cutaneous horn, skin tags, pressure injury with its full staging, "
         "pilonidal disease, dermatofibroma, keratoacanthoma, epidermoid cyst, syringoma, every one of "
         "the vascular lesions, neurofibromatosis, xanthelasma, lipoma, digital mucous cyst and "
         "sebaceous hyperplasia. <b>Three of this deck&rsquo;s slides are pictures of tables</b> &mdash; "
         "the pressure injury staging system, the sinus-versus-fistula distinction and the keratolytic "
         "products &mdash; and their content is in no text version of the file. Those are asked here. "
         "This is the objective-style set; the vignettes are separate. Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "benign-skin-lesions-quiz.html" if n == 1 else "benign-skin-lesions-quiz-version-2.html"
    html = render(title=f"Benign Skin Lesions Quiz {n} &mdash; CMS I Exam 1",
                  h1="Benign Skin Lesions",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 7 &middot; Objective set",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
