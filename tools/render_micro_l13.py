#!/usr/bin/env python3
"""Render Microbiology Exam 2, Lecture 13 — Miscellaneous Bacterial Agents of Disease (Dr. Fair).

Palette and header shape inherited from Lectures 7-11 so the class reads as one. Set 1 is text-only (it stays
in Group Study); Set 2 carries the picture questions, whose crops tools/extract_micro_l13_quiz_images.py writes
into micro-exam-2-quiz-images/.
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 2")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Spirochetes", "Syphilis", "Leptospirosis", "Relapsing fever &amp; Lyme", "Vibrio &amp; cholera",
         "<i>Campylobacter</i>", "<i>Helicobacter</i>", "Rickettsias", "<i>Coxiella</i> &amp; <i>Bartonella</i>",
         "Chlamydias", "Mycoplasmas", "Dental disease"]

sets = json.load(io.open(os.path.join(HERE, "micro_l13_sets.json"), encoding="utf-8"))
# `mis` (the misconception each distractor stands for) is review metadata for tools/blind_review.py;
# it stays in the sets file and never reaches the page.
sets = {k: [{f: v for f, v in q.items() if f != "mis"} for q in qs] for k, qs in sets.items()}
from micro_l13_intro import INTRO
for n, key, fname in ((1, "set1", "misc-bacterial-agents-quiz.html"),
                      (2, "set2", "misc-bacterial-agents-quiz-version-2.html")):
    html = render(
        title="Miscellaneous Bacterial Agents &mdash; Quiz %d" % n,
        h1="Miscellaneous Bacterial Agents of Disease",
        sub="Microbiology &middot; Exam 2 &middot; Lecture 13 &middot; Set %d" % n,
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=sets[key], already_converted=True, **PALETTE)
    for q in sets[key]:
        if q.get("img"):
            assert os.path.exists(os.path.join(OUT, q["img"])), q["img"]
    io.open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %s  (%d KB, %d picture questions)"
          % (fname, len(html) // 1024, sum(1 for q in sets[key] if q.get("img"))))
