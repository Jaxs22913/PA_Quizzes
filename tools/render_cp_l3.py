#!/usr/bin/env python3
"""Render the two Clinical Pathophysiology I Lecture 3 quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1")
S = json.load(open(os.path.join(HERE, "cp_l3_sets.json"), encoding="utf-8"))
PAL = dict(navy="#3b2a5e", indigo="#6a4fa3", gold="#c08a2e", ice="#f2eefb")
CHIPS = ["Non-neoplastic growth", "Neoplasia &amp; grading", "Routes of spread",
         "Carcinogenesis", "TNM staging"]
INTRO = ("Thirty questions on abnormal cell growth and differentiation, drawn from the syllabus "
         "instructional objectives. Covers the non-neoplastic abnormalities &mdash; agenesis, "
         "aplasia, hypoplasia, atrophy, hypertrophy, metaplasia and dysplasia &mdash; then what a "
         "neoplasm is, histological grading by differentiation, benign against malignant, the three "
         "routes of tumour spread, the naming rule that turns tissue of origin into sarcoma or "
         "carcinoma, the four categories of gene alteration, chemical carcinogenesis, the "
         "microbial causes with their exact mechanisms, heredity, and the TNM system. "
         "<b>Pathophysiology only</b> &mdash; every question asks what is happening in the tissue "
         "and why, never what you would do about it. <b>The 20 August lecture recording is folded in</b> &mdash; this lecture signposts nothing about the exam, so those questions carry the teaching that never reaches a slide instead: Barrett&rsquo;s oesophagus for metaplasia, cervical dysplasia for dysplasia, weight training for hypertrophy, and the vascular reasoning that predicts where a cancer will spread. Every question cites its slide, or the recording timestamp it came from.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "abnormal-cell-growth-quiz.html" if n == 1 else "abnormal-cell-growth-quiz-version-2.html"
    html = render(title=f"Abnormal Cell Growth and Differentiation Quiz {n} &mdash; Clin Path I Exam 1",
                  h1=f"Abnormal Cell Growth and Differentiation &mdash; Quiz {n}",
                  sub="Clinical Pathophysiology I &middot; Exam 1 &middot; Lecture 3",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
