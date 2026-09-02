#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render "Guess that Disease" for CMS I Exam 2 (ophthalmology).

The picture is the question; the four choices are bare condition names. Runs on
the standard exam-navigator engine (tools/quiz-template) rather than a bespoke
page, so it inherits Exam Mode, the timer, cross-out, resume, the per-region
results breakdown and the missed-question review -- and so the derm version
gets the same treatment by changing one bank. Picture support was added to the
shared template for this; `img`, `alt` and `slide` are optional on any question.

ANSWER POSITIONS ARE ROTATED, never chosen while authoring: the bank writes the
correct condition first and this assigns its slot round-robin through A-D,
walking the regions in order so no region ends up with all its answers in one
column. [[answer_position_bias_check]]
"""
import os, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))

from cms_e2_gtd_bank import ITEMS
from render import render

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2",
                   "cms-exam-2-guess-that-disease.html")
IMGDIR = "cms-ophtho-chart-images"
STEM = "Name the condition shown."


def build():
    questions = []
    for n, it in enumerate(ITEMS):
        opts = [[it["cond"], "Correct. " + it["why"]]]
        opts += [[w, r] for w, r in it["wrong"]]
        # Rotate the key through A-D. The distractors keep their authored order
        # around it, so the strongest look-alike is not always adjacent.
        slot = n % 4
        key = opts.pop(0)
        opts.insert(slot, key)
        img = it["img"]
        assert os.path.exists(os.path.join(os.path.dirname(OUT), IMGDIR, img)), img
        questions.append({
            "topic": it["cond"],
            "io": it["io"],
            "q": STEM,
            "img": IMGDIR + "/" + img,
            "alt": it["alt"],
            "slide": "Slide %d" % it["slide"],
            "opts": opts,
            "c": slot,
            "cite": "%s, Slide %d" % (it["deck"], it["slide"]),
        })
    return questions


def main():
    questions = build()
    html = render(
        title="Guess that Disease — Ophthalmology | CMS I Exam 2",
        h1="Guess that Disease — Ophthalmology",
        sub="Clinical Medicine and Surgery I &middot; Exam 2",
        pill="%d pictures" % len(questions),
        chips=["Eyelid &amp; lacrimal", "Ocular surface", "Sclera &amp; orbit",
               "Cornea", "Retina &amp; optic nerve", "Pupil &amp; movements",
               "Tumours", "Trauma"],
        intro="One picture at a time, four condition names underneath. Every wrong choice "
              "is something the block teaches from the same part of the eye, so the picture "
              "has to be read rather than the list. Tap any picture to enlarge it.",
        questions=questions,
        already_converted=True,
        navy="#2d3f7a", indigo="#5566b5", gold="#c08a2e", ice="#eef0fa",
    )
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d questions, %.0f KB)" % (os.path.basename(OUT), len(questions),
                                                len(html) / 1024))


if __name__ == "__main__":
    main()
