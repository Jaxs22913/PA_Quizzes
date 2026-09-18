#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Clinical Pathophysiology I cardiac quizzes (Lecture 6)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 2")
SETS = json.load(open(os.path.join(HERE, "clinpath_cardiac_sets.json"), encoding="utf-8"))
# The Clinical Pathophysiology palette, taken from render_clinpath_ent.py.
PALETTE = dict(navy="#3b2a5e", indigo="#6a4fa3", gold="#c08a2e", ice="#efeaf8")
CHIPS = ["Coronary disease", "Plaque", "Ischaemia &amp; infarction", "Valves",
         "Myocardium &amp; pericardium"]

INTRO = (
  "Mechanism only, which is the line this course draws against Clinical Medicine and Surgery: "
  "how the disease works belongs here, what is done about it belongs there. A cardiac lecture is "
  "the hardest place to hold that line, because every condition in it has an obvious treatment "
  "&mdash; so the build rejects a management term in ANY option, not just in the correct one. "
  "<b>One idea organises the valve half.</b> Stenosis makes the heart do PRESSURE work and "
  "regurgitation makes it do VOLUME work, and which chamber hypertrophies, which dilates, and "
  "where the pressure backs up to all follow from that. It is worth reasoning from rather than "
  "learning valve by valve. "
  "<b>Three numbers are worth holding, and they are easy to swap.</b> Seventy-five per cent "
  "occlusion before coronary flow is compromised; about fifty per cent closure before a stenotic "
  "valve affects haemodynamics; and thirty minutes from complete coronary occlusion to "
  "irreversible necrosis, with inability to contract arriving within a few minutes of that clock "
  "starting. "
  "<b>No recording exists for this lecture</b>, so every question comes off the slides and every "
  "one cites the slide it came from."
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "cardiac-pathophysiology-quiz.html" if n == 1 \
        else "cardiac-pathophysiology-quiz-version-2.html"
    html = render(
        title="Cardiac Pathophysiology Quiz %d &mdash; Clinical Pathophysiology I" % n,
        h1="Cardiac Pathophysiology",
        sub="Clinical Pathophysiology I &middot; Exam 2 &middot; Lecture 6",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-46s %d questions" % (fn, len(qs)))
