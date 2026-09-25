#!/usr/bin/env python3
"""Render the CMS I Exam 5 (Cardiology Block Exam II) quizzes.

Palette continues the exam sequence by the same hue rotation the earlier exams
used -- Exam 1 teal (182), Exam 2 indigo (226), Exam 3 violet (259), Exam 4
plum (292), so Exam 5 is rose (325): the Exam 4 plum colors rotated +33 degrees
in hue. Four-option sets, per the exam standard.

    python3 render_cms_e5.py l27io | l27vig | l28io | l28vig
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 5")
PAL = dict(navy="#7a2d5a", indigo="#b4538c", gold="#c08a2e", ice="#faeef4")

SPEC = {
 "l27io": dict(sets="cms_e5l27_sets.json",
   files=["arterial-occlusive-aneurysm-quiz.html", "arterial-occlusive-aneurysm-quiz-version-2.html"],
   title="Arterial Occlusive Disease and Aortic Aneurysm Quiz %d — CMS I Exam 5",
   h1="Arterial Occlusive Disease &amp; Aortic Aneurysm &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 27",
   chips=["Peripheral artery disease", "Acute limb ischemia", "Carotid disease",
          "Aortic aneurysms", "Aortic dissection"]),
 "l27vig": dict(sets="cms_e5l27_vig_sets.json",
   files=["arterial-occlusive-aneurysm-vignettes.html", "arterial-occlusive-aneurysm-vignettes-version-2.html"],
   title="Arterial Occlusive Disease and Aortic Aneurysm Vignettes %d — CMS I Exam 5",
   h1="Arterial Occlusive Disease &amp; Aortic Aneurysm &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 27",
   chips=["Claudication", "Ankle-brachial index", "Acute limb ischemia", "Aneurysm size and repair",
          "Dissection"]),
 "l28io": dict(sets="cms_e5l28_sets.json",
   files=["cardiomyopathy-quiz.html", "cardiomyopathy-quiz-version-2.html"],
   title="Cardiomyopathy Quiz %d — CMS I Exam 5",
   h1="Cardiomyopathy &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 28",
   chips=["Dilated", "Myocarditis", "Hypertrophic", "Restrictive", "Stress (Takotsubo)"]),
 "l28vig": dict(sets="cms_e5l28_vig_sets.json",
   files=["cardiomyopathy-vignettes.html", "cardiomyopathy-vignettes-version-2.html"],
   title="Cardiomyopathy Vignettes %d — CMS I Exam 5",
   h1="Cardiomyopathy &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 28",
   chips=["Dilated", "Myocarditis", "Outflow obstruction", "Restrictive vs constrictive",
          "Stress (Takotsubo)"]),
}[sys.argv[1] if len(sys.argv) > 1 else "l27io"]

S = json.load(open(os.path.join(HERE, SPEC["sets"]), encoding="utf-8"))
for n, (key, fname) in enumerate(zip(("set1", "set2"), SPEC["files"]), start=1):
    qs = S[key]
    html = R.render(title=SPEC["title"] % n, h1=SPEC["h1"] % n, sub=SPEC["sub"],
                    pill="%d questions" % len(qs), chips=SPEC["chips"], intro="",
                    questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-52s %d questions" % (fname, len(qs)))
