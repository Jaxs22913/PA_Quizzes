#!/usr/bin/env python3
"""Render the CMS I Exam 3 (ear, nose, throat) quizzes.

Palette is the Exam 3 violet, matching the ENT comparison chart, so the exam
reads as one thing and is never mistaken for Exam 2's indigo. Five-option
sets, per the exam standard.

    python3 render_cms_e3.py l15io
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 3")
# Derived from the Exam 2 palette by the same hue rotation the chart uses, so
# the quizzes and the chart are the same violet rather than two near-misses.
PAL = dict(navy="#462d7a", indigo="#7455b5", gold="#c08a2e", ice="#f2eefa")

SPEC = {
 "l15io": dict(sets="cms_e3l15_sets.json",
   files=["external-middle-ear-quiz.html", "external-middle-ear-quiz-version-2.html"],
   title="External and Middle Ear Quiz %d — CMS I Exam 3",
   h1="External and Middle Ear &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 3 &middot; Lecture 15",
   chips=["Otitis media", "Otitis externa", "Cholesteatoma",
          "Ear trauma", "Otosclerosis"]),
 "l15vig": dict(sets="cms_e3l15_vig_sets.json",
   files=["external-middle-ear-vignettes.html", "external-middle-ear-vignettes-version-2.html"],
   title="External and Middle Ear Vignettes %d — CMS I Exam 3",
   h1="External and Middle Ear &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 3 &middot; Lecture 15",
   chips=["Otitis media", "Otitis externa", "Foreign bodies",
          "Barotrauma", "Cholesteatoma"]),
 "l16io": dict(sets="cms_e3l16_sets.json",
   files=["inner-ear-hearing-loss-quiz.html", "inner-ear-hearing-loss-quiz-version-2.html"],
   title="Inner Ear and Hearing Loss Quiz %d — CMS I Exam 3",
   h1="Inner Ear, Balance and Hearing Loss &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 3 &middot; Lecture 16",
   chips=["Weber &amp; Rinne", "Audiometry", "Tympanometry",
          "Vertigo", "Acoustic neuroma"]),
 "l16vig": dict(sets="cms_e3l16_vig_sets.json",
   files=["inner-ear-hearing-loss-vignettes.html",
          "inner-ear-hearing-loss-vignettes-version-2.html"],
   title="Inner Ear and Hearing Loss Vignettes %d — CMS I Exam 3",
   h1="Inner Ear, Balance and Hearing Loss &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 3 &middot; Lecture 16",
   chips=["Weber &amp; Rinne", "M&eacute;ni&egrave;re disease", "Positional vertigo",
          "Sudden hearing loss", "Ototoxicity"]),
 "l17io": dict(sets="cms_e3l17_sets.json",
   files=["nose-sinuses-quiz.html", "nose-sinuses-quiz-version-2.html"],
   title="Nose and Paranasal Sinuses Quiz %d — CMS I Exam 3",
   h1="Nose and Paranasal Sinuses &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 3 &middot; Lecture 17",
   chips=["Sinusitis", "The septum", "Epistaxis", "Polyps &amp; rhinitis", "Nasal trauma"]),
 "l17vig": dict(sets="cms_e3l17_vig_sets.json",
   files=["nose-sinuses-vignettes.html", "nose-sinuses-vignettes-version-2.html"],
   title="Nose and Paranasal Sinuses Vignettes %d — CMS I Exam 3",
   h1="Nose and Paranasal Sinuses &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 3 &middot; Lecture 17",
   chips=["Viral vs bacterial", "Epistaxis", "Foreign body", "Polyps", "Nasal fracture"]),
}[sys.argv[1] if len(sys.argv) > 1 else "l15io"]

S = json.load(open(os.path.join(HERE, SPEC["sets"]), encoding="utf-8"))
for n, (key, fname) in enumerate(zip(("set1", "set2"), SPEC["files"]), start=1):
    qs = S[key]
    html = R.render(title=SPEC["title"] % n, h1=SPEC["h1"] % n, sub=SPEC["sub"],
                    pill="%d questions" % len(qs), chips=SPEC["chips"], intro="",
                    questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-48s %d questions" % (fname, len(qs)))
