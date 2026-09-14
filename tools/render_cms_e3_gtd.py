#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render "Guess that Disease" for CMS I Exam 3, ear, nose and throat.

Same shape as the ophthalmology and dermatology renderers; the palette is the
purple this exam's own quizzes already use, so the game looks like the block it
belongs to rather than like the other two games.

Grouping is by REGION rather than by instructional objective, which the engine
supports via the ioLabel pass-through: the ENT block is organised
anatomically -- ear, nose, neck, oral cavity, pharynx and larynx -- and a
results breakdown along those lines is the one a student can act on.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))

from cms_e3_gtd_bank import ITEMS
from render import render

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 3",
                   "cms-exam-3-guess-that-disease.html")
IMGDIR = "cms-ent-chart-images"
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
        title="Guess that Disease — Ear, Nose and Throat | CMS I Exam 3",
        h1="Guess that Disease — Ear, Nose and Throat",
        sub="Clinical Medicine and Surgery I &middot; Exam 3",
        pill="%d pictures" % len(questions),
        chips=["Ear", "Nose &amp; sinuses", "Neck", "Oral cavity",
               "Pharynx &amp; larynx"],
        intro="One picture at a time, four condition names underneath. Every wrong choice "
              "is something the block teaches from the same region, so the picture has to "
              "be read rather than the list. Tap any picture to enlarge it.",
        questions=questions,
        already_converted=True,
        navy="#462d7a", indigo="#7455b5", gold="#c08a2e", ice="#f2eefa",
    )
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d questions, %.0f KB)" % (os.path.basename(OUT), len(questions),
                                                len(html) / 1024))

    by_region = {}
    for q in questions:
        by_region[q["io"]] = by_region.get(q["io"], 0) + 1
    for region, n in sorted(by_region.items(), key=lambda kv: -kv[1]):
        print("  %-28s %2d" % (region, n))
    pos = {}
    for q in questions:
        pos[q["c"]] = pos.get(q["c"], 0) + 1
    print("  answer positions A/B/C/D: %s"
          % "/".join(str(pos.get(i, 0)) for i in range(4)))


if __name__ == "__main__":
    main()
