#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two PDM I lab-panel interpretation quizzes.

Two DIFFERENT topics, not two versions of one set, so they do not take the
house "-version-2" filename: the complete blood count quiz and the chemistry
and urinalysis quiz test different panels and share no questions.

Palettes are borrowed rather than invented -- the blood count set uses Lecture
4's plum, the chemistry and urinalysis set uses Lecture 5's green, so each
quiz already looks like the lecture it came from. See [[site_design_tokens]].
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE),
                   "Principles of Diagnostic Medicine I Exam 1")
SETS = json.load(open(os.path.join(HERE, "pdm_lab_sets.json"), encoding="utf-8"))

COMMON = ("Every question gives you a panel with the reference ranges printed beside the "
          "values, and asks what it shows. <b>Nothing here is a recall question</b> &mdash; the "
          "numbers are on the page, and the work is reading them. That is also how the exam "
          "itself behaves: reference ranges are supplied, and they are taught as approximate and "
          "lab-dependent on purpose, so what is being tested is the DIRECTION of an abnormality "
          "and the pattern several values make together.")

CONF = {
 "cbc": dict(
   fn="lab-interpretation-hematology-quiz.html",
   title="Lab Interpretation 1: Complete Blood Count &mdash; PDM I Exam 1",
   h1="Reading the Panel: Complete Blood Count",
   sub="Principles of Diagnostic Medicine I &middot; Exam 1 &middot; Lecture 4",
   chips=["Microcytic", "Macrocytic", "Normocytic", "White cells &amp; platelets",
          "Morphology"],
   palette=dict(navy="#5a3a5e", indigo="#8a5f8d", gold="#b8862f", ice="#f6f1f6"),
   intro=COMMON + (" <b>This set is the anemia algorithm run backwards.</b> Instead of being "
     "asked what iron studies show in iron deficiency, you are given the ferritin and the "
     "binding capacity and asked which anemia they belong to. The three volume bands sort the "
     "first move, the reticulocyte count separates a marrow that is responding from one that is "
     "not, and the smear findings &mdash; stippling, Howell-Jolly bodies, Heinz bodies, "
     "schistocytes, rouleaux &mdash; each name one condition. One question is deliberately "
     "normal, because recognising a panel with nothing wrong with it is its own skill.")),
 "chem": dict(
   fn="lab-interpretation-chemistry-urinalysis-quiz.html",
   title="Lab Interpretation 2: Chemistry &amp; Urinalysis &mdash; PDM I Exam 1",
   h1="Reading the Panel: Chemistry and Urinalysis",
   sub="Principles of Diagnostic Medicine I &middot; Exam 1 &middot; Lectures 5 and 6",
   chips=["Renal", "Hepatic", "Acid-base", "Fluid &amp; electrolytes", "Urinalysis"],
   palette=dict(navy="#2f5d50", indigo="#4e8a76", gold="#b8862f", ice="#eef5f1"),
   intro=COMMON + (" <b>Chemistry and urinalysis are together because they answer the same "
     "questions from two directions</b> &mdash; the serum sodium and the urine specific gravity "
     "are both about water, the bicarbonate and the urine pH are both about acid, and the "
     "rhabdomyolysis and haemolysis items only resolve when you read the dipstick and the serum "
     "at once. <b>There is no arithmetic beyond the anion gap</b>, which is the one calculation "
     "the lecture asks for out loud.")),
}

for key, c in CONF.items():
    qs = SETS[key]
    html = render(
        title=c["title"], h1=c["h1"], sub=c["sub"],
        pill="%d questions" % len(qs), chips=c["chips"], intro=c["intro"],
        questions=qs, already_converted=True, **c["palette"])
    open(os.path.join(OUT, c["fn"]), "w", encoding="utf-8").write(html)
    print("wrote %-52s %d questions" % (c["fn"], len(qs)))
