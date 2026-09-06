#!/usr/bin/env python3
"""Render Microbiology Exam 1, Lecture 4 — Transmission of Microorganisms.

Palette and header shape inherited from the Lecture 1 and Lecture 2 quizzes
so the three sit together as one class.
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 1")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Chain of infection", "Reservoirs", "Zoonoses", "Vectors",
         "Modes of transmission", "Fomites", "Nosocomial infection",
         "Antibiotic resistance"]
INTRO = ("Lecture 4 of Microbiology &mdash; Transmission of Microorganisms. Thirty questions "
         "across all three instructional objectives from the syllabus, every one cited to the "
         "slide it came from. Covers the six links of the chain of infection, living and "
         "non-living reservoirs, the carrier states, zoonoses and their vectors, the modes of "
         "transmission, and the two relationships the objectives name by title &mdash; fomites "
         "against nosocomial infection, and fomites against antibiotic resistance. Roughly half "
         "the lecture is published studies, so several questions ask what a study FOUND and what "
         "its authors did NOT do.")

sets = json.load(io.open(os.path.join(HERE, "micro_l4_sets.json"), encoding="utf-8"))
for n, key, fname in ((1, "set1", "transmission-of-microorganisms-quiz.html"),
                      (2, "set2", "transmission-of-microorganisms-quiz-version-2.html")):
    html = render(
        title="Transmission of Microorganisms &mdash; Quiz %d" % n,
        h1="Transmission of Microorganisms",
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
