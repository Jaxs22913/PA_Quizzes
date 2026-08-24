#!/usr/bin/env python3
"""Render the CMS I Exam 1 Master Exams — five cumulative 60-question forms."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
D = "Clinical Medicine and Surgery I Exam 1"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Clinical reasoning", "General Derm I", "Derm II", "Bacterial", "Infestations",
         "Viral &amp; fungal", "Benign lesions", "Pigmented lesions", "Pre-malignant &amp; malignant"]
INTRO = ("Sixty questions drawn from every lecture in the Exam 1 dermatology block, in exam "
         "proportions rather than at random &mdash; each of the nine lectures contributes to every "
         "form, so this is a genuine cumulative rehearsal and not a sample of whichever topic had the "
         "most questions written for it. Questions are reused verbatim from the topic quizzes, so "
         "nothing here can drift from the material it is summarising. <b>No question appears in more "
         "than one form</b>, so working through all five gives you 300 distinct questions. Every "
         "question cites its slide.")
for name in ("A", "B", "C", "D", "E"):
    fn = "cms-exam-1-master-exam-form-%s.html" % name.lower()
    html = render(title=f"CMS I Exam 1 Master Exam &mdash; Form {name}",
                  h1="Clinical Medicine and Surgery I &mdash; Comprehensive Master Exam",
                  sub=f"Exam 1 &middot; Dermatology block, Lectures 1&ndash;9 &middot; Form {name}",
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[name]))
