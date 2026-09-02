#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render "Guess that Disease" for CMS I Exam 1 (dermatology).

Same engine and the same rotation rule as tools/render_cms_e2_gtd.py -- the
only thing that changes between the two blocks is the bank. Pictures are the
comparison chart's own audited files, so nothing new is extracted here.

ONE PICTURE IS NOT FROM A DECK. The chronic-paronychia photograph is the
chart's Wikimedia Commons substitute, and it carries its own attribution
rather than a slide number; the bank marks it with deck=None.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))

from cms_e1_gtd_bank import ITEMS
from render import render

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 1",
                   "cms-exam-1-guess-that-disease.html")
IMGDIR = "cms-derm-chart-images"
STEM = "Name the condition shown."
EXT_CITE = ("Daifallah M. Al Aboud, MD, via Wikimedia Commons, from StatPearls "
            "· CC BY 4.0")


def build():
    questions = []
    for n, it in enumerate(ITEMS):
        opts = [[it["cond"], "Correct. " + it["why"]]]
        opts += [[w, r] for w, r in it["wrong"]]
        slot = n % 4
        opts.insert(slot, opts.pop(0))
        img = it["img"]
        assert os.path.exists(os.path.join(os.path.dirname(OUT), IMGDIR, img)), img
        if it["deck"] is None:
            cite, caption = EXT_CITE, "Wikimedia Commons \u00b7 CC BY 4.0"
        else:
            cite = "%s, Slide %d" % (it["deck"], it["slide"])
            caption = "Slide %d" % it["slide"]
        questions.append({
            "topic": it["cond"],
            "io": it["io"],
            "q": STEM,
            "img": IMGDIR + "/" + img,
            "alt": it["alt"],
            "slide": caption,
            "opts": opts,
            "c": slot,
            "cite": cite,
        })
    return questions


def main():
    questions = build()
    html = render(
        title="Guess that Disease — Dermatology | CMS I Exam 1",
        h1="Guess that Disease — Dermatology",
        sub="Clinical Medicine and Surgery I &middot; Exam 1",
        pill="%d pictures" % len(questions),
        chips=["Eczema", "Papulosquamous &amp; bullous", "Immune-mediated",
               "Drug &amp; photo", "Bacterial", "Infestations", "Fungal",
               "Viral", "Benign &amp; pigmented", "Malignant"],
        intro="One picture at a time, four condition names underneath. Every wrong choice "
              "is something the block teaches from the same family, and several of the pairs "
              "are the discrimination the lectures build the whole topic around — tense "
              "versus flaccid blisters, a scaly ring versus a scale-free one, a scar that "
              "stays inside the wound versus one that does not. Tap any picture to enlarge it.",
        questions=questions,
        already_converted=True,
        # CMS Exam 1's established palette, taken from the derm topic quizzes --
        # not a new one invented for this page.
        navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4",
    )
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d questions, %.0f KB)" % (os.path.basename(OUT), len(questions),
                                                len(html) / 1024))


if __name__ == "__main__":
    main()
