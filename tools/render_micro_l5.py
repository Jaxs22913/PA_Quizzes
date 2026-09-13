#!/usr/bin/env python3
"""Render Microbiology Exam 1, Lecture 5 — Host Defenses: Nonspecific Mechanisms.

Palette and header shape inherited from Lectures 1 to 4 so the class reads as one.
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 1")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Lines of defense", "Barriers &amp; normal flora", "Plasma proteins",
         "Recognition &mdash; PAMPs &amp; DAMPs", "Inflammation &amp; fever",
         "Complement", "Interferon", "Leukocytes &amp; phagocytosis",
         "Natural killer cells"]
INTRO = ("Lecture 5 of Microbiology &mdash; Host Defenses: Nonspecific Mechanisms. Thirty "
         "questions, every one cited to the slide it came from. "
         "<b>This is the largest lecture of the block by some distance</b>: 93 slides against "
         "<b>eleven</b> instructional objectives, where Lectures 1 to 4 carry three or four "
         "each. The selection is spread deliberately across all eleven rather than letting the "
         "big topics crowd out the small ones &mdash; complement alone could have filled a set. "
         "Covers the three lines of defense; the physical, chemical, microbiological and genetic "
         "barriers of the first line; normal flora; the plasma proteins that limit infection, "
         "including defensins and the pentraxins; the acute-phase response; pattern recognition "
         "and the PAMP against DAMP distinction; inflammation from the inflammasome through "
         "extravasation; the mechanism of fever and its beneficial effects; the complement "
         "system end to end, from the thioester bond to the membrane attack complex and the "
         "regulators that keep it off your own cells; the three interferons; the leukocyte "
         "classes with their percentages and the differential white count; phagocytosis and the "
         "respiratory burst; and natural killer cells.")

sets = json.load(io.open(os.path.join(HERE, "micro_l5_sets.json"), encoding="utf-8"))
for n, key, fname in ((1, "set1", "host-defenses-nonspecific-quiz.html"),
                      (2, "set2", "host-defenses-nonspecific-quiz-version-2.html")):
    html = render(
        title="Host Defenses: Nonspecific Mechanisms &mdash; Quiz %d" % n,
        h1="Host Defenses: Nonspecific Mechanisms",
        sub="Microbiology &middot; Exam 1 &middot; Lecture 5 &middot; Set %d" % n,
        pill="30 questions",
        chips=CHIPS,
        intro=INTRO,
        questions=sets[key],
        already_converted=True,
        **PALETTE)
    p = os.path.join(OUT, fname)
    io.open(p, "w", encoding="utf-8").write(html)
    print("wrote %s  (%d KB)" % (fname, len(html) // 1024))
