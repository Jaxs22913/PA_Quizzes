#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Clinical Pathophysiology I vascular quizzes (Lecture 7)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 2")
SETS = json.load(open(os.path.join(HERE, "clinpath_vascular_sets.json"), encoding="utf-8"))
PALETTE = dict(navy="#3b2a5e", indigo="#6a4fa3", gold="#c08a2e", ice="#efeaf8")
CHIPS = ["Vessel wall layers", "Endothelium", "Blood pressure", "Atherosclerosis",
         "Aneurysm &amp; dissection", "Venous disease"]

INTRO = (
  "Mechanism only, which is the line this course draws against Clinical Medicine and Surgery: "
  "how the disease works belongs here, what is done about it belongs there. "
  "<b>One idea organises most of the arterial half.</b> Each artery type is built for a different "
  "job, so each fails differently &mdash; the elastic aorta loses elastic tissue and DILATES into "
  "an aneurysm, the muscular coronary and renal arteries NARROW through atherosclerosis, and the "
  "small arteries and arterioles STIFFEN under hypertension. Reasoning from the structure gets you "
  "the disease. "
  "<b>The neointimal response is the second organising idea.</b> Injure the endothelium anywhere, "
  "by any mechanism, and the same thing happens: smooth muscle migrates into the intima, "
  "proliferates, lays down matrix, platelets activate and leukocytes arrive. The wall has a "
  "limited repertoire, which is why one process explains in-stent restenosis, transplant "
  "vasculopathy and the beginning of every atherosclerotic plaque. "
  "<b>No recording exists for this lecture</b>, so every question comes off the slides and every "
  "one cites the slide it came from."
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "vascular-pathophysiology-quiz.html" if n == 1 \
        else "vascular-pathophysiology-quiz-version-2.html"
    html = render(
        title="Vascular Pathophysiology Quiz %d &mdash; Clinical Pathophysiology I" % n,
        h1="Vascular Pathophysiology",
        sub="Clinical Pathophysiology I &middot; Exam 2 &middot; Lecture 7",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-46s %d questions" % (fn, len(qs)))
