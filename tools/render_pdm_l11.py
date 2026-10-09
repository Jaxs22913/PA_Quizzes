#!/usr/bin/env python3
"""Render the two PDM I Lecture 11 (Rhythm Analysis and Sinus Rhythms) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 3")
SETS = json.load(open(os.path.join(HERE, "pdm_l11_sets.json"), encoding="utf-8"))
# One palette for the whole of Exam 3, kept in tools/pdm_e3/palette.json.
_P = json.load(open(os.path.join(HERE, "pdm_e3", "palette.json"), encoding="utf-8"))
PALETTE = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Conduction system", "Action potential", "Paper &amp; waves", "Leads", "Heart rate",
         "Regularity", "Systematic approach", "Normal sinus rhythm", "Sinus bradycardia",
         "Sinus tachycardia", "Sinus arrhythmia", "Sinus exit block", "Sinus pause &amp; arrest",
         "Sick sinus syndrome"]
INTRO = (
  "Thirty questions on <b>reading a rhythm strip and the rhythms that come from the sinus node</b>, and "
  "about half of them show you the strip. The first part reviews the foundation the rhythms rest on: the "
  "conduction system and its three pacemakers, the action potential, the paper, every wave and interval, "
  "and where the leads go. Then the strips: count the rate, decide whether it is regular, check the P waves "
  "and the PR interval, look at the QRS, and name the rhythm. Normal sinus rhythm, sinus bradycardia and "
  "sinus tachycardia differ only in rate; sinus arrhythmia only in regularity; sinus exit block, sinus pause "
  "and sinus arrest by whether the missing beats march out and how many are missed. "
  "<b>Any value in a question comes with its normal range.</b> <b>Tap any strip to enlarge it.</b>"
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "rhythm-analysis-sinus-rhythms-quiz.html" if n == 1 else "rhythm-analysis-sinus-rhythms-quiz-version-2.html"
    html = render(
        title="Rhythm Analysis &amp; Sinus Rhythms Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Rhythm Analysis &amp; Sinus Rhythms",
        sub="Principles of Diagnostic Medicine I &middot; Exam 3 &middot; Lecture 11",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-55s %d questions (%d with a strip)" % (fn, len(qs), sum(1 for q in qs if q.get("img"))))
