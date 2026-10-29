#!/usr/bin/env python3
"""Render the CMS I Exam 6 (Respiratory Block Exam I) quizzes for Lectures 35 and 36.

Palette continues the exam sequence by the same hue rotation the earlier exams used -- Exam 1 teal (182),
Exam 2 indigo (226), Exam 3 violet (259), Exam 4 plum (292), Exam 5 rose (325) -- so Exam 6 is the Exam 5
colors rotated +33 degrees in hue (brick red). Four-option sets, per the exam standard.

    python3 render_cms_e6l35.py l35io | l35vig | l36io | l36vig
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 6")
PAL = dict(navy="#7a2d30", indigo="#b45357", gold="#c08a2e", ice="#faefee")

SPEC = {
 "l35io": dict(sets="cms_e6l35_sets.json",
   files=["asthma-quiz.html", "asthma-quiz-version-2.html"],
   title="Asthma Quiz %d — CMS I Exam 6",
   h1="Asthma &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 6 &middot; Lecture 35",
   chips=["Definition and pathophysiology", "Etiology and triggers", "Spirometry and peak flow",
          "Severity classification", "Medications", "Patient education"]),
 "l35vig": dict(sets="cms_e6l35_vig_sets.json",
   files=["asthma-vignettes.html", "asthma-vignettes-version-2.html"],
   title="Asthma Vignettes %d — CMS I Exam 6",
   h1="Asthma &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 6 &middot; Lecture 35",
   chips=["Wheeze and cough", "Classifying severity", "Controller choice", "Drugs to avoid",
          "Aspirin and exercise", "Action plans"]),
 "l36io": dict(sets="cms_e6l36_sets.json",
   files=["copd-quiz.html", "copd-quiz-version-2.html"],
   title="Chronic Obstructive Pulmonary Disease Quiz %d — CMS I Exam 6",
   h1="Chronic Obstructive Pulmonary Disease &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 6 &middot; Lecture 36",
   chips=["Chronic bronchitis and emphysema", "Alpha-1 antitrypsin", "Spirometry", "Severity grades and groups",
          "Inhalers and oxygen", "Exacerbations"]),
 "l36vig": dict(sets="cms_e6l36_vig_sets.json",
   files=["copd-vignettes.html", "copd-vignettes-version-2.html"],
   title="Chronic Obstructive Pulmonary Disease Vignettes %d — CMS I Exam 6",
   h1="Chronic Obstructive Pulmonary Disease &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 6 &middot; Lecture 36",
   chips=["Smokers with dyspnea", "Symptom and survival scores", "Choosing inhalers", "Comorbidities",
          "Exacerbations", "Older adults"]),
}[sys.argv[1] if len(sys.argv) > 1 else "l35io"]

os.makedirs(OUT, exist_ok=True)
S = json.load(open(os.path.join(HERE, SPEC["sets"]), encoding="utf-8"))
for n, (key, fname) in enumerate(zip(("set1", "set2"), SPEC["files"]), start=1):
    # the sets keep each distractor's misconception tag as a third option element
    # (WRITER.md; tools/blind_review.py reads it there); the pages carry text + explanation only
    qs = [dict({k: v for k, v in q.items() if k not in ("mis", "ordered", "asc")},
               opts=[o[:2] for o in q["opts"]]) for q in S[key]]
    html = R.render(title=SPEC["title"] % n, h1=SPEC["h1"] % n, sub=SPEC["sub"],
                    pill="%d questions" % len(qs), chips=SPEC["chips"], intro=SPEC.get("intro", ""),
                    questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-40s %d questions" % (fname, len(qs)))
