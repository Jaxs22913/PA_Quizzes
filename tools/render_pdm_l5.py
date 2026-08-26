#!/usr/bin/env python3
"""Render the two Principles of Diagnostic Medicine I Lecture 5 quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
SETS = json.load(open(os.path.join(HERE, "pdm_l5_sets.json"), encoding="utf-8"))
PALETTE = dict(navy="#5a3a5e", indigo="#8a5f8d", gold="#b8862f", ice="#f6f1f6")
CHIPS = ["Panels &amp; ordering", "Electrolytes", "Kidney &amp; glucose",
         "Liver studies", "Acid-base &amp; the anion gap", "Fluid balance"]
INTRO = ("Thirty questions on the chemistry panel: what is on a basic panel against a "
         "comprehensive one and when to order each, the physiological role of sodium, potassium, "
         "chloride and bicarbonate, glucose, blood urea nitrogen and creatinine, the liver "
         "studies and the four patterns of hepatic abnormality, the renal, hepatic and metabolic "
         "laboratory patterns side by side, the anion gap, and the laboratory evaluation of fluid "
         "and electrolyte balance. "
         "<b>This lecture does ask you to calculate the anion gap.</b> Professor Reynolds walked "
         "through it in the lecture and gave the normal range aloud, so the worked examples here "
         "are deliberate. She was equally clear about the two she does <i>not</i> want computed: "
         "the glomerular filtration rate &mdash; <i>&ldquo;I don&rsquo;t need you to calculate "
         "that or know that just yet, but know <b>of</b> it&rdquo;</i> &mdash; and the corrected "
         "sodium, which she does with a clinical calculator. Neither is asked for here. "
         "<b>You are not expected to recall reference ranges.</b> Her words: <i>&ldquo;the hard "
         "and fast memorize these numbers, we don&rsquo;t do that to you &hellip; we always give "
         "you reference ranges.&rdquo;</i> That matters, because this deck states three ranges "
         "two different ways &mdash; bicarbonate, glucose and blood urea nitrogen each differ "
         "between the text slides and her own fishbone diagram. No question is built on a "
         "disputed figure; learn the direction of abnormality and the approximate value. "
         "<b>The fishbone itself is a picture with no text.</b> Slide 4 extracts as completely "
         "blank and carries the entire reference set, so anything drawn from it is marked as "
         "image-only. Every question cites its slide.")

for n, key in ((1, "set1"), (2, "set2")):
    fn = "chemistry-panels-quiz.html" if n == 1 else "chemistry-panels-quiz-version-2.html"
    html = render(
        title=f"Chemistry Panels, Renal Function &amp; Electrolytes Quiz {n} &mdash; PDM I Exam 1",
        h1="Chemistry Panels, Renal Function and Electrolytes",
        sub="Principles of Diagnostic Medicine I &middot; Exam 1 &middot; Lecture 5",
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=SETS[key], already_converted=True, **PALETTE)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(SETS[key]))
