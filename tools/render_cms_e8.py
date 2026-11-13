#!/usr/bin/env python3
"""Render the CMS I Exam 8 (Hematology Block Exam, Lectures 46-51; Lecture 47 is not tested) quizzes.

Palette continues the exam sequence by the same hue rotation the earlier exams used -- Exam 1 teal (182), Exam 2
indigo (226), Exam 3 violet (259), Exam 4 plum (292), Exam 5 rose (325), Exam 6 crimson (358), Exam 7 bronze (31) --
so Exam 8 is olive (64): Exam 7's bronze rotated +33 degrees in hue and re-solved to the same contrast against white
(navy 9.42:1, indigo 4.89:1); the gold slot stays an amber (the flagged-question chip puts dark text on it).
Four-option sets, per the exam standard.

    python3 render_cms_e8.py l46io | l46vig

A later lecture (48-51) adds its two SPEC entries here (see tools/cms_e8_README.md).
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 8")
PAL = dict(navy="#46491c", indigo="#717533", gold="#c9962a", ice="#f8f8ee")

SUB = "Clinical Medicine and Surgery I &middot; Exam 8 &middot; Lecture %d"
SPEC = {
 "l46io": dict(sets="cms_e8l46_sets.json",
   files=["cytopenias-hemochromatosis-quiz.html", "cytopenias-hemochromatosis-quiz-version-2.html"],
   title="Cytopenias and Hemochromatosis Quiz %d — CMS I Exam 8",
   h1="Cytopenias &amp; Hemochromatosis &mdash; Quiz %d",
   sub=SUB % 46,
   chips=["Red cell indices", "Iron deficiency", "Chronic disease", "Sideroblastic and lead", "Macrocytic and B12",
          "Kidney disease", "Aplastic anemia", "Leukopenia", "Hemolysis", "Autoimmune hemolysis", "G6PD deficiency",
          "Thalassemia", "Sickle cell", "Hemochromatosis"]),
 "l46vig": dict(sets="cms_e8l46_vig_sets.json",
   files=["cytopenias-hemochromatosis-vignettes.html", "cytopenias-hemochromatosis-vignettes-version-2.html"],
   title="Cytopenias and Hemochromatosis Vignettes %d — CMS I Exam 8",
   h1="Cytopenias &amp; Hemochromatosis &mdash; Vignettes %d",
   sub=SUB % 46,
   chips=["Read the iron panel", "Small or large cells", "Count the neutrophils", "Drugs to avoid",
          "Hemolysis labs", "Comorbidities", "Across the lifespan"],
   intro="Size the cells first (the mean corpuscular volume), then read the iron panel or the hemolysis labs, then "
         "check the medication list for anything that caused it or must be avoided. Every laboratory value comes "
         "with its normal range; work the absolute neutrophil count from the white count and differential yourself."),
}[sys.argv[1] if len(sys.argv) > 1 else "l46io"]

S = json.load(open(os.path.join(HERE, SPEC["sets"]), encoding="utf-8"))
os.makedirs(OUT, exist_ok=True)
for n, (key, fname) in enumerate(zip(("set1", "set2"), SPEC["files"]), start=1):
    # the sets keep each distractor's misconception tag as a third option element
    # (WRITER.md; tools/blind_review.py reads it there); the pages carry text + explanation only
    qs = [dict({k: v for k, v in q.items() if k not in ("mis", "ordered", "asc")},
               opts=[o[:2] for o in q["opts"]]) for q in S[key]]
    html = R.render(title=SPEC["title"] % n, h1=SPEC["h1"] % n, sub=SPEC["sub"],
                    pill="%d questions" % len(qs), chips=SPEC["chips"], intro=SPEC.get("intro", ""),
                    questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-52s %d questions" % (fname, len(qs)))
