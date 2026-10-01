#!/usr/bin/env python3
"""Render the PDM I Exam 2 Master Exams -- five cumulative 60-question forms, 15 per lecture.

Reads Principles of Diagnostic Medicine I Exam 2/master-exams.json, written by
tools/pdm_e2_masters_partition.py (which also puts the keys on an exact 15/15/15/15 A-D cycle
per form -- never render straight from a pool).

LECTURE CONTENT ONLY. Exam 2 covers Lectures 7-10 AND Lab 2, but no lab material has been handed out
(the PDM inbox has no lab folder or file), so, exactly as the Exam 1 forms (render_pdm_masters.py), these
rehearse the four lectures and the page says so rather than implying a coverage it does not have.
Re-run the partition and this if Lab 2 material lands and gets folded in.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Principles of Diagnostic Medicine I Exam 2"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
# the Exam 2 palette, copied from render_pdm_l7..l10 rather than invented
PAL = dict(navy="#2f5d50", indigo="#4e8a76", gold="#b8862f", ice="#eef5f1")
CHIPS = ["Electrocardiography", "Cardiac imaging &amp; vascular studies",
         "Cardiac biomarkers &amp; lipid testing", "Coagulation &amp; hemostasis testing"]
INTRO = ("Sixty questions drawn from all four lectures of the Exam 2 block, in exam proportions rather than at "
         "random: <b>each lecture is two scheduled hours, so each contributes fifteen questions to every "
         "form</b>. The lead-ins are spread across what a test shows, which test to order, how to read a result, "
         "why a finding happens, and the limits of a study, and every form carries all of them. About a quarter "
         "of the questions are not in the topic quizzes, so these forms are worth working even after those. "
         "<b>No question appears in more than one form</b>, so working through all five gives you 300 distinct "
         "questions. <b>These forms cover the four LECTURES.</b> The exam also covers Lab 2, for which no "
         "material has been handed out; when it is, it gets folded in and these are rebuilt. "
         "<b>You are not expected to recall reference ranges</b> &mdash; where a value matters, its scale is "
         "given in the question. Four options, A&ndash;D, and every wrong choice gets its own explanation. "
         "Every question cites its slide.")

for name in ("A", "B", "C", "D", "E"):
    fn = "pdm-exam-2-master-exam-form-%s.html" % name.lower()
    assert len(S[name]) == 60, "Form %s has %d questions" % (name, len(S[name]))
    html = render(title=f"PDM I Exam 2 Master Exam &mdash; Form {name}",
                  h1="Principles of Diagnostic Medicine I &mdash; Comprehensive Master Exam",
                  sub=f"Exam 2 &middot; Lectures 7&ndash;10 &middot; Form {name}",
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[name]))
