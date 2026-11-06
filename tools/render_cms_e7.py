#!/usr/bin/env python3
"""Render the CMS I Exam 7 (Respiratory Block Exam II, Lectures 39-45) quizzes.

Palette continues the exam sequence by the same hue rotation the earlier exams used -- Exam 1 teal (182),
Exam 2 indigo (226), Exam 3 violet (259), Exam 4 plum (292), Exam 5 rose (325), Exam 6 crimson (358) -- so
Exam 7 is bronze (31): the Exam 6 crimson rotated +33 degrees in hue and re-solved to Exam 6's contrast against
white (navy 9.35:1, indigo 4.87:1), the gold kept. Four-option sets, per the exam standard.

    python3 render_cms_e7.py l39io | l39vig | l40io | l40vig | l41io | l41vig | l42io | l42vig | l43io | l43vig
                             | l44io | l44vig

A later lecture (42-45) adds its two SPEC entries here (see tools/cms_e7_README.md).
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 7")
PAL = dict(navy="#5e4123", indigo="#92693f", gold="#c08a2e", ice="#faf6ee")

SUB = "Clinical Medicine and Surgery I &middot; Exam 7 &middot; Lecture %d"
SPEC = {
 "l39io": dict(sets="cms_e7l39_sets.json",
   files=["phases-of-sleep-quiz.html", "phases-of-sleep-quiz-version-2.html"],
   title="Phases of Sleep Quiz %d — CMS I Exam 7",
   h1="Phases of Sleep &mdash; Quiz %d",
   sub=SUB % 39,
   chips=["Sleep versus coma", "Sleep cycles", "Rapid eye movement sleep", "Non-rapid eye movement sleep",
          "Why we sleep", "Brain waves", "The stages on the electroencephalogram"]),
 "l39vig": dict(sets="cms_e7l39_vig_sets.json",
   files=["phases-of-sleep-vignettes.html", "phases-of-sleep-vignettes-version-2.html"],
   title="Phases of Sleep Vignettes %d — CMS I Exam 7",
   h1="Phases of Sleep &mdash; Vignettes %d",
   sub=SUB % 39,
   chips=["Asleep or unresponsive?", "Which stage is this?", "Which wave is this?", "What the body does",
          "Sleep loss"],
   intro="Each case describes a patient or a sleep recording. Decide first whether the person can be aroused, "
         "then read the waveform (its frequency and voltage), then the body's state (muscle tone, heart and "
         "breathing)."),
 "l40io": dict(sets="cms_e7l40_sets.json",
   files=["sleep-apnea-ohs-quiz.html", "sleep-apnea-ohs-quiz-version-2.html"],
   title="Obstructive Sleep Apnea and Obesity Hypoventilation Quiz %d — CMS I Exam 7",
   h1="Obstructive Sleep Apnea &amp; Obesity Hypoventilation &mdash; Quiz %d",
   sub=SUB % 40,
   chips=["Apnea and hypopnea", "Risk factors", "Sleep studies", "STOP-Bang", "Treatment",
          "Untreated sleep apnea", "Central sleep apnea", "Obesity hypoventilation"]),
 "l40vig": dict(sets="cms_e7l40_vig_sets.json",
   files=["sleep-apnea-ohs-vignettes.html", "sleep-apnea-ohs-vignettes-version-2.html"],
   title="Obstructive Sleep Apnea and Obesity Hypoventilation Vignettes %d — CMS I Exam 7",
   h1="Obstructive Sleep Apnea &amp; Obesity Hypoventilation &mdash; Vignettes %d",
   sub=SUB % 40,
   chips=["Score the STOP-Bang", "Which sleep study", "Choosing therapy", "Comorbidities",
          "Central or obstructive", "Hypoventilation in obesity", "Older adults"]),
 "l41io": dict(sets="cms_e7l41_sets.json",
   files=["inflammatory-lung-disease-quiz.html", "inflammatory-lung-disease-quiz-version-2.html"],
   title="Inflammatory Lung Diseases Quiz %d — CMS I Exam 7",
   h1="Inflammatory Lung Diseases &mdash; Quiz %d",
   sub=SUB % 41,
   chips=["Interstitial lung disease", "Workup and imaging", "Idiopathic pulmonary fibrosis", "Sarcoidosis",
          "Pneumoconiosis", "Asbestosis and silicosis", "Hypersensitivity pneumonitis",
          "Acute respiratory distress syndrome"]),
 "l41vig": dict(sets="cms_e7l41_vig_sets.json",
   files=["inflammatory-lung-disease-vignettes.html", "inflammatory-lung-disease-vignettes-version-2.html"],
   title="Inflammatory Lung Diseases Vignettes %d — CMS I Exam 7",
   h1="Inflammatory Lung Diseases &mdash; Vignettes %d",
   sub=SUB % 41,
   chips=["Exposure history", "Restrictive lungs", "Staging sarcoidosis", "When to give steroids",
          "Drug-induced disease", "Grading oxygenation", "Older adults"],
   intro="Take the occupational and exposure history first: the job, the dust and the years since exposure "
         "point to the disease before the imaging does. Every laboratory value comes with its normal range."),
 "l42io": dict(sets="cms_e7l42_sets.json",
   files=["pulmonary-vascular-disorders-quiz.html", "pulmonary-vascular-disorders-quiz-version-2.html"],
   title="Pulmonary Vascular Disorders Quiz %d — CMS I Exam 7",
   h1="Pulmonary Vascular Disorders &mdash; Quiz %d",
   sub=SUB % 42,
   chips=["Cor pulmonale", "Right ventricle under pressure", "Pulmonary hypertension groups", "Signs and workup",
          "Pulmonary hypertension treatment", "Pulmonary edema", "Pulmonary embolism", "Wells and PERC",
          "Risk and treatment"]),
 "l42vig": dict(sets="cms_e7l42_vig_sets.json",
   files=["pulmonary-vascular-disorders-vignettes.html", "pulmonary-vascular-disorders-vignettes-version-2.html"],
   title="Pulmonary Vascular Disorders Vignettes %d — CMS I Exam 7",
   h1="Pulmonary Vascular Disorders &mdash; Vignettes %d",
   sub=SUB % 42,
   chips=["Score the Wells", "Apply PERC", "Which test", "Contraindications", "Risk category",
          "Cardiogenic or not", "Older adults"],
   intro="Count every Wells and PERC (Pulmonary Embolism Rule-out Criteria) item the case gives you before "
         "choosing a test, and check for anything that rules out contrast or clot-busting drugs. Every laboratory "
         "value comes with its normal range."),
 "l43io": dict(sets="cms_e7l43_sets.json",
   files=["pulmonary-nodules-neoplasms-quiz.html", "pulmonary-nodules-neoplasms-quiz-version-2.html"],
   title="Pulmonary Nodules and Neoplasms Quiz %d — CMS I Exam 7",
   h1="Pulmonary Nodules &amp; Neoplasms &mdash; Quiz %d",
   sub=SUB % 43,
   chips=["Epidemiology and risk", "Incidental nodules", "Workup and biopsy", "Benign or concerning", "Screening",
          "Staging", "Central or peripheral", "Cell types", "Paraneoplastic syndromes"]),
 "l43vig": dict(sets="cms_e7l43_vig_sets.json",
   files=["pulmonary-nodules-neoplasms-vignettes.html", "pulmonary-nodules-neoplasms-vignettes-version-2.html"],
   title="Pulmonary Nodules and Neoplasms Vignettes %d — CMS I Exam 7",
   h1="Pulmonary Nodules &amp; Neoplasms &mdash; Vignettes %d",
   sub=SUB % 43,
   chips=["Who gets screened", "Benign or concerning", "Stage from the findings", "Treatment by stage",
          "Which cell type", "Paraneoplastic signs"],
   intro="Read the nodule first (its size, edge, calcification and growth), then the patient (smoking history, "
         "symptoms, where the mass sits). Every laboratory value comes with its normal range."),
 "l44io": dict(sets="cms_e7l44_sets.json",
   files=["pleural-disorders-quiz.html", "pleural-disorders-quiz-version-2.html"],
   title="Pleural Disorders Quiz %d — CMS I Exam 7",
   h1="Pleural Disorders &mdash; Quiz %d",
   sub=SUB % 44,
   chips=["Pleura and pleurisy", "Pneumothorax types", "Imaging and size", "Procedures", "Spontaneous pneumothorax",
          "Tension pneumothorax", "Hemothorax", "Pneumomediastinum", "Pleural effusion", "Light's criteria",
          "Pleurodynia"]),
 "l44vig": dict(sets="cms_e7l44_vig_sets.json",
   files=["pleural-disorders-vignettes.html", "pleural-disorders-vignettes-version-2.html"],
   title="Pleural Disorders Vignettes %d — CMS I Exam 7",
   h1="Pleural Disorders &mdash; Vignettes %d",
   sub=SUB % 44,
   chips=["Stable or unstable", "How big is it", "Needle or tube", "Light's criteria", "What to avoid",
          "Patient education"],
   intro="Decide first whether the patient is stable, then what the film shows and how big the air or fluid is. "
         "Pleural fluid results come with the serum values you need for Light's criteria."),
}[sys.argv[1] if len(sys.argv) > 1 else "l39io"]

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
