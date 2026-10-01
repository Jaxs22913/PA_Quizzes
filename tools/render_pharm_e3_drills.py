#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Pharmacology I Exam 3 rapid drill (Lecture 9, Diuretics and Heart Failure Drugs).

Same format as the Exam 1 and Exam 2 drills (pharmacology_exam_spec, RAPID DRILLS): one fact, four DRUG NAMES underneath,
no vignette, no doses, one drug per choice (a class name is offered only when the stem itself asks for a class, and then
every choice is a class). Bank: tools/pharm_drill_hf.py (ITEMS). Answer positions rotate through A-D, never chosen while
authoring. One set for now; a master drill is added when Lectures 10-13 give Exam 3 a second set.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
import pharm_drill_hf as hf

OUT = os.path.join(ROOT, "Pharmacology I Exam 3")
DECK = {"HF": "Diuretics and Heart Failure Drugs.pptx", "MI": "Myocardial Ischemia Drugs.pptx", "HTN": "Antihypertensives.pptx",
        "OPH": "Ophthalmology-2.pptx"}
IO = "Topic — Diuretics and heart failure drugs"
CHIPS = ["Loop diuretics", "Thiazides", "Potassium-sparing", "Aldosterone antagonists", "Carbonic anhydrase inhibitors",
         "Heart failure drugs", "Digoxin"]
INTRO = ("One fact, four drug names. No patient, no story &mdash; just the thing that drug or class is known for, and "
         "<b>no doses</b>. Every wrong choice is another drug from the same family, so it is a real discrimination "
         "rather than a category guess.")


def build(items):
    out = []
    for n, it in enumerate(items):
        opts = [[it["ans"], "Correct. " + it["why"]]] + [[w, r] for w, r in it["wrong"]]
        slot = n % 4
        opts.insert(slot, opts.pop(0))
        lect, slide = it["src"]
        out.append({"topic": it["ans"], "io": IO, "q": it["q"], "opts": opts, "c": slot,
                    "cite": "%s, Slide %d" % (DECK[lect], slide)})
    return out


def main():
    qs = build(hf.ITEMS)
    html = render(title="Diuretics & Heart Failure Drugs Drill | Pharmacology I Exam 3",
                  h1="Diuretics &amp; Heart Failure Drugs Drill", sub="Pharmacology I &middot; Exam 3 &middot; rapid drill",
                  pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO, questions=qs, already_converted=True,
                  navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
    open(os.path.join(OUT, "pharm-e3-drill-diuretics-heart-failure.html"), "w", encoding="utf-8").write(html)
    print("wrote pharm-e3-drill-diuretics-heart-failure.html  %d questions" % len(qs))


if __name__ == "__main__":
    main()
