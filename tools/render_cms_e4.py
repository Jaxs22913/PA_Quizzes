#!/usr/bin/env python3
"""Render the CMS I Exam 4 (cardiovascular) quizzes.

Palette continues the exam sequence by the same hue rotation the earlier exams
used -- Exam 1 teal (182), Exam 2 indigo (226), Exam 3 violet (259), so Exam 4
is plum (292). Four-option sets, per the exam standard.

    python3 render_cms_e4.py l20io
    python3 render_cms_e4.py l21io | l21vig | l22io | l22vig | l25io | l25vig
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 4")
PAL = dict(navy="#702d7a", indigo="#a753b4", gold="#c08a2e", ice="#f9eefa")

SPEC = {
 "l20io": dict(sets="cms_e4l20_sets.json",
   files=["hypertension-quiz.html", "hypertension-quiz-version-2.html"],
   title="Hypertension Quiz %d — CMS I Exam 4",
   h1="Hypertension &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 4 &middot; Lecture 20",
   chips=["Classification", "Secondary causes", "Target organ damage",
          "Assessment", "Treatment"]),
 "l20vig": dict(sets="cms_e4l20_vig_sets.json",
   files=["hypertension-vignettes.html", "hypertension-vignettes-version-2.html"],
   title="Hypertension Vignettes %d — CMS I Exam 4",
   h1="Hypertension &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 4 &middot; Lecture 20",
   chips=["Secondary causes", "Emergency vs urgency", "Agent selection",
          "Adverse effects", "Resistant hypertension"]),
 # ---- Carter's lectures (2026-09-24). Same palette, same naming as hypertension-*.
 "l21io": dict(sets="cms_e4l21_sets.json",
   files=["hypotension-quiz.html", "hypotension-quiz-version-2.html"],
   title="Hypotension Quiz %d — CMS I Exam 4",
   h1="Hypotension &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 4 &middot; Lecture 21",
   chips=["Definitions", "Orthostatic", "Reflex syncope", "Cardiogenic syncope",
          "Management"]),
 "l21vig": dict(sets="cms_e4l21_vig_sets.json",
   files=["hypotension-vignettes.html", "hypotension-vignettes-version-2.html"],
   title="Hypotension Vignettes %d — CMS I Exam 4",
   h1="Hypotension &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 4 &middot; Lecture 21",
   chips=["Orthostatic vitals", "Neurogenic vs volume", "Vasovagal", "Cardiogenic red flags",
          "Management"]),
 "l22io": dict(sets="cms_e4l22_sets.json",
   files=["atherosclerosis-lipids-quiz.html", "atherosclerosis-lipids-quiz-version-2.html"],
   title="Atherosclerosis and Lipid Disorders Quiz %d — CMS I Exam 4",
   h1="Atherosclerosis &amp; Lipid Disorders &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 4 &middot; Lecture 22",
   chips=["Lipoproteins", "Risk assessment", "Genetic dyslipidemias", "Secondary causes",
          "Lipid-lowering therapy"]),
 "l22vig": dict(sets="cms_e4l22_vig_sets.json",
   files=["atherosclerosis-lipids-vignettes.html", "atherosclerosis-lipids-vignettes-version-2.html"],
   title="Atherosclerosis and Lipid Disorders Vignettes %d — CMS I Exam 4",
   h1="Atherosclerosis &amp; Lipid Disorders &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 4 &middot; Lecture 22",
   chips=["Statin decisions", "Hypertriglyceridemia", "Familial hypercholesterolemia",
          "Secondary causes", "Drug selection"]),
 "l25io": dict(sets="cms_e4l25_sets.json",
   files=["heart-failure-quiz.html", "heart-failure-quiz-version-2.html"],
   title="Heart Failure Quiz %d — CMS I Exam 4",
   h1="Heart Failure &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 4 &middot; Lecture 25",
   chips=["Systolic vs diastolic", "Ejection fraction groups", "Classes and stages",
          "Natriuretic peptides", "Guideline-directed therapy"]),
 "l25vig": dict(sets="cms_e4l25_vig_sets.json",
   files=["heart-failure-vignettes.html", "heart-failure-vignettes-version-2.html"],
   title="Heart Failure Vignettes %d — CMS I Exam 4",
   h1="Heart Failure &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 4 &middot; Lecture 25",
   chips=["Left vs right", "Ejection fraction groups", "Staging", "Natriuretic peptides",
          "Guideline-directed therapy"]),
}[sys.argv[1] if len(sys.argv) > 1 else "l20io"]

S = json.load(open(os.path.join(HERE, SPEC["sets"]), encoding="utf-8"))
for n, (key, fname) in enumerate(zip(("set1", "set2"), SPEC["files"]), start=1):
    qs = S[key]
    html = R.render(title=SPEC["title"] % n, h1=SPEC["h1"] % n, sub=SPEC["sub"],
                    pill="%d questions" % len(qs), chips=SPEC["chips"], intro="",
                    questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-48s %d questions" % (fname, len(qs)))
