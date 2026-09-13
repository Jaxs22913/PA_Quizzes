#!/usr/bin/env python3
"""Render Microbiology Exam 1, Lecture 6 — The Acquisition of Specific Immunity.

Palette and header shape inherited from Lectures 1 to 5 so the class reads as one.
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 1")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Acquired immunity", "Leukocytes", "MHC &amp; HLA", "Clonal selection",
         "Antigens", "Antibody classes", "T cells", "Vaccines &amp; immunotherapy"]
INTRO = ("Lecture 6 of Microbiology &mdash; The Acquisition of Specific Immunity and Its "
         "Applications. Thirty questions, every one cited to the slide it came from. "
         "Covers the four kinds of acquired immunity and how to tell them apart; the leukocyte "
         "order and its mnemonic; the major histocompatibility complex, its two classes and the "
         "chromosome it sits on; clonal selection and why specificity exists before any antigen "
         "arrives; the special antigen categories &mdash; auto, allo, heterophilic, super and "
         "allergen; the five immunoglobulin classes with the features that separate them; the "
         "four antibody&ndash;antigen reactions; primary against secondary response; the four "
         "T-cell types; and the applications &mdash; passive immunotherapy, the monoclonal "
         "antibody naming endings, vaccine composition and criteria, and marrow donation. "
         "<b>Built from the deck.</b> This lecture was delivered on 11 September but no "
         "recording has surfaced, so nothing here depends on one. Where the deck is thin against "
         "an objective &mdash; laboratory tests appear only as titres, and the complement "
         "pathway comparison belongs to Lecture 5 &mdash; the questions follow the slides rather "
         "than filling the gap with invented content.")

sets = json.load(io.open(os.path.join(HERE, "micro_l6_sets.json"), encoding="utf-8"))
for n, key, fname in ((1, "set1", "specific-immunity-quiz.html"),
                      (2, "set2", "specific-immunity-quiz-version-2.html")):
    html = render(
        title="The Acquisition of Specific Immunity &mdash; Quiz %d" % n,
        h1="The Acquisition of Specific Immunity",
        sub="Microbiology &middot; Exam 1 &middot; Lecture 6 &middot; Set %d" % n,
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=sets[key], already_converted=True, **PALETTE)
    p = os.path.join(OUT, fname)
    io.open(p, "w", encoding="utf-8").write(html)
    print("wrote %s  (%d KB)" % (fname, len(html) // 1024))
