#!/usr/bin/env python3
"""Render Microbiology Exam 2, Lecture 11 — Novel Antimicrobial Therapy (Dr. Fair).

Palette and header shape inherited from Lectures 7-10 so the class reads as one. The one picture
question (Set 2 only) points at micro-exam-2-quiz-images/l11-s09-disk-diffusion.jpg, the deck's own
photograph of two disk-diffusion plates.
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 2")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Resistance &amp; stewardship", "Antibiograms", "Empiric therapy", "Prophylaxis",
         "Adverse effects", "Fecal microbiota transplant", "Phage therapy", "Probiotics &amp; prebiotics",
         "Plant essential oils"]

sets = json.load(io.open(os.path.join(HERE, "micro_l11_sets.json"), encoding="utf-8"))
from micro_l11_intro import INTRO
for n, key, fname in ((1, "set1", "novel-antimicrobial-therapy-quiz.html"),
                      (2, "set2", "novel-antimicrobial-therapy-quiz-version-2.html")):
    html = render(
        title="Novel Antimicrobial Therapy &mdash; Quiz %d" % n,
        h1="Novel Antimicrobial Therapy",
        sub="Microbiology &middot; Exam 2 &middot; Lecture 11 &middot; Set %d" % n,
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=sets[key], already_converted=True, **PALETTE)
    for q in sets[key]:
        if q.get("img"):
            assert os.path.exists(os.path.join(OUT, q["img"])), q["img"]
    io.open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %s  (%d KB, %d picture questions)"
          % (fname, len(html) // 1024, sum(1 for q in sets[key] if q.get("img"))))
