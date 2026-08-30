#!/usr/bin/env python3
"""Render the Pharmacology I Exam 1 Master Exams -- five cumulative 60-question forms."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Pharmacology I Exam 1"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))

# inherited from the existing Pharmacology I Exam 1 quizzes, not invented
PAL = dict(navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
CHIPS = ["Antibacterials", "Antivirals", "Antifungals", "Dermatology medications",
         "ANS &amp; cholinergic", "Adrenergic"]
INTRO = ("Sixty questions drawn from every topic in the Exam 1 block, in proportion rather than at "
         "random &mdash; all six contribute to every form, so this is a genuine cumulative rehearsal "
         "and not a sample of whichever topic had the most questions written for it. Questions are "
         "reused verbatim from the topic quizzes, so nothing here can drift from the material it is "
         "summarising. <b>No question appears in more than one form</b>, so working through all five "
         "gives you 300 distinct questions. Every question cites its slide. "
         "<b>Weighted the way the course asked for</b>: Dr. McInnis told the class that mechanism is "
         "over-studied, so indications, patient education, side effects and contraindications carry "
         "the count. <b>No question turns on a drug dose</b>, per Dr. Wood. "
         "This rebuild (v2, 30 August) folds in the new <b>short clinical vignettes</b> and is "
         "written to be more to the point &mdash; brief stems, and answer choices short enough "
         "to scan, with the reasoning moved into the explanation. The five v1 forms are kept "
         "under Archived quizzes for extra practice.")

for name in ("A", "B", "C", "D", "E"):
    fn = "pharm-exam-1-master-exam-form-%s.html" % name.lower()
    html = render(title="Pharmacology I Exam 1 Master Exam &mdash; Form %s" % name,
                  h1="Pharmacology I &mdash; Comprehensive Master Exam",
                  sub="Exam 1 &middot; Lectures 1&ndash;3 &middot; Form %s" % name,
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-44s %d questions" % (fn, len(S[name])))
