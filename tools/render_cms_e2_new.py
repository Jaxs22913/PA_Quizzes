#!/usr/bin/env python3
"""Render the CMS I Exam 2 Lecture 11 and 12 quizzes.

Palette inherited from the existing Exam 2 ophthalmology quizzes so the exam
reads as one thing. Five-option sets, per the exam standard.

    python3 render_cms_e2_new.py l2vig
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2")
PAL = dict(navy="#2d3f7a", indigo="#5566b5", gold="#c08a2e", ice="#eef0fa")

SPEC = {
 "l2vig": dict(sets="cms_e2l2_vig_sets.json",
   files=["neuro-ophthalmology-vignettes.html", "neuro-ophthalmology-vignettes-version-2.html"],
   title="Neuro-Ophthalmology Vignettes %d — CMS I Exam 2",
   h1="Neuro-Ophthalmology &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 2 &middot; Lecture 11",
   chips=["Pupillary pathways", "Horner syndrome", "Tonic &amp; Argyll Robertson pupils",
          "Cranial nerve palsies", "Visual fields"]),
 "l2io": dict(sets="cms_e2l2_sets.json",
   files=["neuro-ophthalmology-quiz.html", "neuro-ophthalmology-quiz-version-2.html"],
   title="Neuro-Ophthalmology Quiz %d — CMS I Exam 2",
   h1="Neuro-Ophthalmology &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 2 &middot; Lecture 11",
   chips=["Nystagmus", "Pupillary pathways", "Horner syndrome",
          "Cranial nerve palsies", "Chiasmal lesions"]),
 "l3vig": dict(sets="cms_e2l3_vig_sets.json",
   files=["acute-vision-loss-vignettes.html", "acute-vision-loss-vignettes-version-2.html"],
   title="Acute Vision Loss Vignettes %d — CMS I Exam 2",
   h1="Acute Vision Loss &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 2 &middot; Lecture 12",
   chips=["Amaurosis fugax", "Angle-closure glaucoma", "Retinal detachment",
          "Vascular occlusion", "Optic neuropathy"]),
 "l3io": dict(sets="cms_e2l3_sets.json",
   files=["acute-vision-loss-quiz.html", "acute-vision-loss-quiz-version-2.html"],
   title="Acute Vision Loss Quiz %d — CMS I Exam 2",
   h1="Acute Vision Loss &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 2 &middot; Lecture 12",
   chips=["Amaurosis fugax", "Glaucoma", "Optic neuritis",
          "Retinal detachment", "CRAO &amp; CRVO"]),
 "l4vig": dict(sets="cms_e2l13_vig_sets.json",
   files=["chronic-vision-loss-vignettes.html", "chronic-vision-loss-vignettes-version-2.html"],
   title="Chronic Vision Loss Vignettes %d — CMS I Exam 2",
   h1="Chronic Vision Loss &amp; Tumors &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 2 &middot; Lecture 13",
   chips=["Cataract", "Macular degeneration", "Open-angle glaucoma",
          "Amblyopia &amp; strabismus", "Ocular tumors"]),
 "l4io": dict(sets="cms_e2l13_sets.json",
   files=["chronic-vision-loss-quiz.html", "chronic-vision-loss-quiz-version-2.html"],
   title="Chronic Vision Loss Quiz %d — CMS I Exam 2",
   h1="Chronic Vision Loss &amp; Tumors &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 2 &middot; Lecture 13",
   chips=["Cataract", "Macular degeneration", "Glaucoma",
          "Refractive errors", "Retinoblastoma &amp; melanoma"]),
}[sys.argv[1] if len(sys.argv) > 1 else "l2vig"]

S = json.load(open(os.path.join(HERE, SPEC["sets"]), encoding="utf-8"))
for n, (key, fname) in enumerate(zip(("set1", "set2"), SPEC["files"]), start=1):
    qs = S[key]
    html = R.render(title=SPEC["title"] % n, h1=SPEC["h1"] % n, sub=SPEC["sub"],
                    pill="%d questions" % len(qs), chips=SPEC["chips"], intro="",
                    questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-46s %d questions" % (fname, len(qs)))
