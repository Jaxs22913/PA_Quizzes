#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Clinical Pathophysiology I ENT quizzes (Lecture 5)."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1")
SETS = json.load(open(os.path.join(HERE, "clinpath_ent_sets.json"), encoding="utf-8"))
PALETTE = dict(navy="#3b2a5e", indigo="#6a4fa3", gold="#c08a2e", ice="#efeaf8")
CHIPS = ["Hearing loss", "Ototoxicity", "Vertigo &amp; balance", "Rhinology", "Larynx &amp; neck"]

INTRO = ("Mechanism only. This course draws its line against Clinical Medicine and Surgery at "
         "pathophysiology against management, and this lecture tests that line &mdash; the "
         "epistaxis table has a management column sitting right beside the pathophysiology, and "
         "not one question here is built on it. The vascular source and the aetiology are "
         "pathophysiology; what you do about it belongs to the other course. "
         "<b>Vertigo carries extra weight.</b> The lecturer put it plainly: <i>&ldquo;on my board "
         "exams, a third of my neurology questions were vertigo related. So know this, know these "
         "things.&rdquo;</i> The four peripheral causes are separated here on the axes that "
         "actually distinguish them &mdash; how long the vertigo lasts, whether hearing goes with "
         "it, and whether a viral infection came first. "
         "<b>One correction is baked in.</b> The slide gives labyrinthitis &ldquo;episodic&rdquo; "
         "vertigo; the lecturer corrected that aloud &mdash; <i>&ldquo;this is not episodic. This "
         "is continuous vertigo.&rdquo;</i> The questions teach continuous, and the study guide "
         "records where the deck disagrees.")

for n, key in ((1, "set1"), (2, "set2")):
    qs = SETS[key]
    fn = "ent-pathophysiology-quiz.html" if n == 1 else "ent-pathophysiology-quiz-version-2.html"
    html = render(
        title="ENT Pathophysiology Quiz %d &mdash; Clinical Pathophysiology I" % n,
        h1="ENT Pathophysiology",
        sub="Clinical Pathophysiology I &middot; Exam 1 &middot; Lecture 5",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-42s %d questions" % (fn, len(qs)))
