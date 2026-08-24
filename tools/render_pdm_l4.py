#!/usr/bin/env python3
"""Render the two Principles of Diagnostic Medicine I Lecture 4 quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
SETS = json.load(open(os.path.join(HERE, "pdm_l4_sets.json"), encoding="utf-8"))
PALETTE = dict(navy="#5a3a5e", indigo="#8a5f8d", gold="#b8862f", ice="#f6f1f6")
CHIPS = ["Components &amp; ordering", "White cells", "Absolute counts &amp; platelets",
         "Red cell morphology", "Anemia workup"]
INTRO = ("Thirty questions on the complete blood count: what is on the panel and what the "
         "differential adds, each white cell line with its range and what raises and lowers it, "
         "calculating an absolute neutrophil count and grading neutropenia, platelets and mean "
         "platelet volume, hemoglobin against hematocrit, the four red cell indices and their "
         "formulas, the whole shape-and-inclusion vocabulary from acanthocyte to Heinz body, and "
         "the microcytic, normocytic and macrocytic anemia patterns with their iron studies. "
         "<b>Unlike Lectures 1 to 3, this one does ask you to calculate</b> &mdash; objective (d) "
         "is an arithmetic objective. "
         "<b>A great deal of this lecture exists only inside a picture</b>: the neutropenia "
         "severity table, the schistocyte types, the iron comparison table, the anemia algorithm, "
         "the index formulas and the fishbone diagram are all figures with no text version in the "
         "deck. Those questions are marked as image-only in their citation. "
         "<b>Where the deck gives a reference range two different ways</b> &mdash; lymphocytes, "
         "platelets and red cell distribution width all appear twice with different numbers "
         "&mdash; no question is built on the disputed figure. The 24 August lecture explains "
         "why that happens: Professor Shah teaches reference ranges as <b>approximate and "
         "lab-dependent on purpose</b> &mdash; <i>&ldquo;it doesn&rsquo;t matter what the range "
         "is, it just matters what the range is for where you&rsquo;re working&rdquo;</i> "
         "&mdash; so the disagreement is her position rather than a mistake. Learn the "
         "approximate figure and the direction of abnormality. The study guide sets every "
         "version side by side. Every question cites its slide.")

for n, key in ((1, "set1"), (2, "set2")):
    fn = "cbc-hematology-quiz.html" if n == 1 else "cbc-hematology-quiz-version-2.html"
    html = render(
        title=f"Complete Blood Count &amp; Hematology Diagnostics Quiz {n} &mdash; PDM I Exam 1",
        h1="Complete Blood Count and Hematology Diagnostics",
        sub="Principles of Diagnostic Medicine I &middot; Exam 1 &middot; Lecture 4",
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=SETS[key], already_converted=True, **PALETTE)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(SETS[key]))
