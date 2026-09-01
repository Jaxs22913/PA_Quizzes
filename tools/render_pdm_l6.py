#!/usr/bin/env python3
"""Render the two Principles of Diagnostic Medicine I Lecture 6 quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
SETS = json.load(open(os.path.join(HERE, "pdm_l6_sets.json"), encoding="utf-8"))
PALETTE = dict(navy="#2f5d50", indigo="#4e8a76", gold="#b8862f", ice="#eef5f1")
CHIPS = ["Inspection &amp; the dipstick", "pH &amp; stones", "Infection pads",
         "Ketones &amp; glucose", "Blood, bilirubin &amp; protein",
         "Specific gravity", "Clinical correlation"]
INTRO = ("Thirty questions on urinalysis: what the test covers and when to order it, the "
         "physical examination of urine &mdash; colour, transparency and odour &mdash; reagent "
         "strip technique, and each of the nine parameters in turn. Specific gravity, pH, "
         "protein, glucose, ketones, leukocyte esterase, nitrites, blood and bilirubin. Then the "
         "differentiation objective: telling hematuria, hemoglobinuria and myoglobinuria apart "
         "when the pad cannot, and correlating a set of findings with the patient in front of you. "
         "<b>You are not asked to recall reference ranges.</b> Professor Gopal was explicit: "
         "<i>&ldquo;I&rsquo;m not asking that you memorize ranges &hellip; but I do want you to "
         "know if there should just be none present at all. If there&rsquo;s a range involved, "
         "it&rsquo;ll be provided for you.&rdquo;</i> So knowing which pads read negative in a "
         "healthy person is fair game, and no question here turns on a number you have to have "
         "memorised. Nothing asks you to calculate. "
         "<b>The blood pad detects heme</b>, which sits in red cells, free hemoglobin and "
         "myoglobin alike, so a positive result never tells you which. What separates them is "
         "what else is true &mdash; intact cells on microscopy, a raised unconjugated bilirubin, "
         "or a raised creatine phosphokinase. That distinction carries a whole objective. "
         "Every question cites its slide, and the handful drawn from the recording say so.")

for n, key in ((1, "set1"), (2, "set2")):
    fn = "urinalysis-quiz.html" if n == 1 else "urinalysis-quiz-version-2.html"
    html = render(
        title=f"Urinalysis Quiz {n} &mdash; PDM I Exam 1",
        h1="Urinalysis",
        sub="Principles of Diagnostic Medicine I &middot; Exam 1 &middot; Lecture 6",
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=SETS[key], already_converted=True, **PALETTE)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(SETS[key]))
