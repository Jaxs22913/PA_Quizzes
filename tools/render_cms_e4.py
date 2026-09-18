#!/usr/bin/env python3
"""Render the CMS I Exam 4 (cardiovascular) quizzes.

Palette continues the exam sequence by the same hue rotation the earlier exams
used -- Exam 1 teal (182), Exam 2 indigo (226), Exam 3 violet (259), so Exam 4
is plum (292). Four-option sets, per the exam standard.

    python3 render_cms_e4.py l20io
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
}[sys.argv[1] if len(sys.argv) > 1 else "l20io"]

S = json.load(open(os.path.join(HERE, SPEC["sets"]), encoding="utf-8"))
for n, (key, fname) in enumerate(zip(("set1", "set2"), SPEC["files"]), start=1):
    qs = S[key]
    html = R.render(title=SPEC["title"] % n, h1=SPEC["h1"] % n, sub=SPEC["sub"],
                    pill="%d questions" % len(qs), chips=SPEC["chips"], intro="",
                    questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-48s %d questions" % (fname, len(qs)))
