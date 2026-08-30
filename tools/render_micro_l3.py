#!/usr/bin/env python3
"""Render Microbiology Exam 1, Lecture 3 — Microbe-Human Interactions.

Palette and header shape inherited from the Lecture 1 and Lecture 2 quizzes
so the three sit together as one class.
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 1")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Resident flora", "Progression of infection", "Virulence factors",
         "Endotoxins & exotoxins", "Patterns of infection", "Reservoirs & transmission",
         "Nosocomial infection", "Epidemiology"]
INTRO = ("Lecture 3 of Microbiology &mdash; Microbe-Human Interactions. Thirty questions across "
         "all seven instructional objectives from the syllabus, every one cited to the slide it "
         "came from. Covers the flora of each body region, the stages an infection passes through, "
         "the endotoxin&ndash;exotoxin distinction objective 3 asks for by name, and the sources "
         "and mitigation of hospital-acquired infection.")

sets = json.load(io.open(os.path.join(HERE, "micro_l3_sets.json"), encoding="utf-8"))
for n, key, fname in ((1, "set1", "microbe-human-interactions-quiz.html"),
                      (2, "set2", "microbe-human-interactions-quiz-version-2.html")):
    html = render(
        title="Microbe-Human Interactions &mdash; Quiz %d" % n,
        h1="Microbe-Human Interactions",
        sub="Microbiology &middot; Exam 1 &middot; Lecture 3 &middot; Set %d" % n,
        pill="30 questions",
        chips=CHIPS,
        intro=INTRO,
        questions=sets[key],
        already_converted=True,
        **PALETTE)
    p = os.path.join(OUT, fname)
    io.open(p, "w", encoding="utf-8").write(html)
    print("wrote %s  (%d KB)" % (fname, len(html) // 1024))
