#!/usr/bin/env python3
"""Render the CMS I Exam 6 (Respiratory Block Exam I, Lectures 33-38) quizzes.

Palette continues the exam sequence by the same hue rotation the earlier exams
used -- Exam 1 teal (182), Exam 2 indigo (226), Exam 3 violet (259), Exam 4
plum (292), Exam 5 rose (325), so Exam 6 is crimson (358): the Exam 5 rose
colors rotated +33 degrees in hue, the gold kept. Four-option sets, per the
exam standard.

    python3 render_cms_e6.py l33io | l33vig | l34io | l34vig | l35io | l35vig | l36io | l36vig

A later lecture adds its two SPEC entries here (see tools/cms_e6_README.md).
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 6")
PAL = dict(navy="#7a2d30", indigo="#b45357", gold="#c08a2e", ice="#faefee")

SPEC = {
 "l33io": dict(sets="cms_e6l33_sets.json",
   files=["oxygen-delivery-quiz.html", "oxygen-delivery-quiz-version-2.html"],
   title="Oxygen Delivery Quiz %d — CMS I Exam 6",
   h1="Oxygen Delivery &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 6 &middot; Lecture 33",
   chips=["Indications and hazards", "Home oxygen qualification", "Delivery devices", "Flow rates",
          "Nebulizers", "Evaluating the response"]),
 "l33vig": dict(sets="cms_e6l33_vig_sets.json",
   files=["oxygen-delivery-vignettes.html", "oxygen-delivery-vignettes-version-2.html"],
   title="Oxygen Delivery Vignettes %d — CMS I Exam 6",
   h1="Oxygen Delivery &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 6 &middot; Lecture 33",
   chips=["Choosing a device", "Who qualifies for home oxygen", "Oxygen safety", "Nebulizer or inhaler",
          "Is it working?"]),
 "l34io": dict(sets="cms_e6l34_sets.json",
   files=["acid-base-part-1-quiz.html", "acid-base-part-1-quiz-version-2.html"],
   title="Acid-Base Part I Quiz %d — CMS I Exam 6",
   h1="Acid-Base Part I &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 6 &middot; Lecture 34",
   chips=["Normal values and buffers", "Potassium and oxygen", "Respiratory acidosis", "Respiratory alkalosis",
          "Metabolic alkalosis", "Metabolic acidosis and the anion gap", "Compensation"]),
 "l34vig": dict(sets="cms_e6l34_vig_sets.json",
   files=["acid-base-part-1-vignettes.html", "acid-base-part-1-vignettes-version-2.html"],
   title="Acid-Base Part I Vignettes %d — CMS I Exam 6",
   h1="Acid-Base Part I &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 6 &middot; Lecture 34",
   chips=["Read the blood gas", "Anion gap", "Winter formula", "Saline responsive or not",
          "Find the cause", "Treat the cause"],
   intro="Every value comes with its normal range. Work each case the same way: the pH first, then which "
         "of the carbon dioxide or the bicarbonate matches it, then the compensation, then the patient."),
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
}[sys.argv[1] if len(sys.argv) > 1 else "l33io"]

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
