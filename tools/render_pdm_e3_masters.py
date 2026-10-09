#!/usr/bin/env python3
"""Render the PDM I Exam 3 Master Exams -- five cumulative 60-question forms, 10 per lecture.

Reads Principles of Diagnostic Medicine I Exam 3/master-exams.json, written by
tools/pdm_e3_masters_partition.py (which also puts the keys on an exact 15/15/15/15 A-D cycle
per form -- never render straight from a pool). Run tools/add_stable_qids.py afterwards.

LECTURE CONTENT ONLY. Exam 3 covers Lectures 11-16 AND Lab 3; Jaxon decided on 2026-10-08 that this
build is "Lectures only", so these forms rehearse the six lectures and the page says so rather than
implying a coverage it does not have.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Principles of Diagnostic Medicine I Exam 3"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
# One palette for the whole of Exam 3 (tools/pdm_e3/palette.json), as the topic quizzes
_P = json.load(open(os.path.join(HERE, "pdm_e3", "palette.json"), encoding="utf-8"))
PAL = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Rhythm analysis &amp; sinus rhythms", "Ectopy, escape &amp; supraventricular rhythms",
         "Ventricular rhythms &amp; atrioventricular blocks", "Axis, bundle branch blocks &amp; enlargement",
         "Ischemia, injury &amp; infarction", "Pericardial disease, electrolytes, drugs &amp; special patterns"]
INTRO = ("Sixty questions drawn from all six lectures of the Exam 3 block, in exam proportions rather than at "
         "random: <b>each lecture is two scheduled hours, so each contributes ten questions to every form</b>. "
         "<b>More than half of every form shows you a rhythm strip or a 12-lead</b> and asks you to name the "
         "rhythm, read the finding or choose the next step, and the rest cover the rules behind those readings. "
         "Every form reaches every lecture's objectives as evenly as five forms allow. "
         "<b>No question appears in more than one form</b>, so working through all five gives you 300 distinct "
         "questions, all taken word for word from the topic quizzes. <b>These forms cover the six LECTURES.</b> "
         "The exam also covers Lab 3, which is not included here. "
         "<b>You are not expected to recall reference ranges</b> &mdash; where a value matters, its normal range "
         "is given in the question. Four options, A&ndash;D, and every wrong choice gets its own explanation. "
         "Every question cites its slide. <b>Tap any strip to enlarge it.</b>")

for name in ("A", "B", "C", "D", "E"):
    fn = "pdm-exam-3-master-exam-form-%s.html" % name.lower()
    assert len(S[name]) == 60, "Form %s has %d questions" % (name, len(S[name]))
    html = render(title=f"PDM I Exam 3 Master Exam &mdash; Form {name}",
                  h1="Principles of Diagnostic Medicine I &mdash; Comprehensive Master Exam",
                  sub=f"Exam 3 &middot; Lectures 11&ndash;16 &middot; Form {name}",
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions, %d with a picture)" % (len(S[name]), sum(1 for q in S[name] if q.get("img"))))
