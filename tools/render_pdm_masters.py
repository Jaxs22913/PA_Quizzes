#!/usr/bin/env python3
"""Render the PDM I Exam 1 Master Exams — five cumulative 60-question forms.

LECTURE CONTENT ONLY. Exam 1 covers Lectures 1-6 AND Lab 1, but no lab material
has been given out (Jaxon, 2026-09-01: "theres no content to give for the labs
today"), so these forms rehearse the six lectures and say so on the page rather
than implying a coverage they do not have. Re-run this if lab material lands
and gets folded in.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Principles of Diagnostic Medicine I Exam 1"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
PAL = dict(navy="#243b6b", indigo="#4d6bb0", gold="#b8862f", ice="#eef1f8")
CHIPS = ["Laboratory diagnostics", "Medical imaging", "Derm, ENT &amp; ophtho testing",
         "Complete blood count", "Chemistry panels", "Urinalysis"]
INTRO = ("Sixty questions drawn from every lecture in the Exam 1 block, in exam proportions rather "
         "than at random &mdash; each of the six lectures contributes ten questions to every form, "
         "so this is a genuine cumulative rehearsal and not a sample of whichever topic had the most "
         "questions written for it. Questions are reused verbatim from the topic quizzes, so nothing "
         "here can drift from the material it is summarising. <b>No question appears in more than "
         "one form</b>, so working through all five gives you 300 distinct questions. "
         "<b>These forms cover the six LECTURES.</b> The exam also covers Lab 1, for which no "
         "material has been handed out; when it is, it gets folded in and these are rebuilt. "
         "<b>You are not expected to recall reference ranges</b> &mdash; where a value matters, its "
         "scale is given in the question. Every question cites its slide.")

for name in ("A", "B", "C", "D", "E"):
    fn = "pdm-exam-1-master-exam-form-%s.html" % name.lower()
    html = render(title=f"PDM I Exam 1 Master Exam &mdash; Form {name}",
                  h1="Principles of Diagnostic Medicine I &mdash; Comprehensive Master Exam",
                  sub=f"Exam 1 &middot; Lectures 1&ndash;6 &middot; Form {name}",
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[name]))
