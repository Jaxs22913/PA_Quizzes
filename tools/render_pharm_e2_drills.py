#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Pharmacology I Exam 2 rapid-drill quizzes.

Same format as the Exam 1 drills: one fact, four DRUG NAMES underneath, no
vignette and no doses. Every wrong choice is another drug from the same family,
so the question is a real discrimination rather than a category guess.

Exam 2 had no drills at all until now, though [[pharmacology_exam_spec]] calls
for them and Exam 1 carries six.

Answer positions rotate through A-D, never chosen while authoring.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))

from render import render
import pharm_drill_oph_antiinfective as ai
import pharm_drill_oph_allergy as al
import pharm_drill_oph_glaucoma as gl

OUT = os.path.join(ROOT, "Pharmacology I Exam 2")
DECK = {"OPH": "Ophthalmology-2.pptx"}

SETS = [
    (ai, "pharm-e2-drill-anti-infectives.html", "Ocular Anti-infectives Drill",
     "Topic — Ocular antibacterials, antivirals and antifungals",
     ["Macrolides", "Fluoroquinolones", "Aminoglycosides", "Antivirals",
      "Antifungals", "Delivery &amp; kinetics"]),
    (al, "pharm-e2-drill-allergy-inflammation.html",
     "Allergy, Inflammation &amp; Dry Eye Drill",
     "Topic — Ocular allergy, inflammation and dry eye",
     ["Antihistamines", "Mast cell stabilisers", "Vasoconstrictors",
      "Non-steroidals", "Glucocorticoids", "Dry eye"]),
    (gl, "pharm-e2-drill-glaucoma-diagnostics.html",
     "Glaucoma &amp; Diagnostics Drill",
     "Topic — Glaucoma agents, anaesthetics, cycloplegics and stains",
     ["Prostaglandins", "Beta blockers", "Alpha-2 agonists",
      "Carbonic anhydrase inhibitors", "Cholinergics", "Diagnostics"]),
]

INTRO = ("One fact, four drug names. No patient, no story &mdash; just the thing that drug "
         "or class is known for, and <b>no doses</b>. Every wrong choice is another drug from "
         "the same family, so it is a real discrimination rather than a category guess.")


def build(items, io):
    out = []
    for n, it in enumerate(items):
        opts = [[it["ans"], "Correct. " + it["why"]]]
        opts += [[w, r] for w, r in it["wrong"]]
        slot = n % 4
        opts.insert(slot, opts.pop(0))
        lect, slide = it["src"]
        out.append({"topic": it["ans"], "io": io, "q": it["q"], "opts": opts,
                    "c": slot, "cite": "%s, Slide %d" % (DECK[lect], slide)})
    return out


def master(all_items):
    """Every Exam 2 drill question in one paper, interleaved across the sets so
    an unshuffled run does not spend the first 26 questions on antibiotics."""
    rows = []
    for i in range(max(len(items) for items, _io in all_items)):
        for items, io in all_items:
            if i < len(items):
                rows.append((items[i], io))
    out = []
    for n, (it, io) in enumerate(rows):
        opts = [[it["ans"], "Correct. " + it["why"]]]
        opts += [[w, r] for w, r in it["wrong"]]
        slot = n % 4
        opts.insert(slot, opts.pop(0))
        lect, slide = it["src"]
        out.append({"topic": it["ans"], "io": io, "q": it["q"], "opts": opts,
                    "c": slot, "cite": "%s, Slide %d" % (DECK[lect], slide)})
    return out


def main():
    total = 0
    for mod, fname, title, io, chips in SETS:
        qs = build(mod.ITEMS, io)
        html = render(
            title="%s | Pharmacology I Exam 2" % title.replace("&amp;", "&"),
            h1=title,
            sub="Pharmacology I &middot; Exam 2 &middot; rapid drill",
            pill="%d questions" % len(qs),
            chips=chips, intro=INTRO,
            questions=qs, already_converted=True,
            navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6",
        )
        open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
        print("  %-46s %3d questions" % (fname, len(qs)))
        total += len(qs)
    print("%d drill questions across %d sets" % (total, len(SETS)))

    qs = master([(m.ITEMS, io) for m, _f, _t, io, _c in SETS])
    html = render(
        title="Master Drill | Pharmacology I Exam 2",
        h1="Master Drill &mdash; every Exam 2 drill question",
        sub="Pharmacology I &middot; Exam 2 &middot; rapid drill",
        pill="%d questions" % len(qs),
        chips=["Anti-infectives", "Allergy &amp; inflammation", "Glaucoma",
               "Diagnostics"],
        intro="All %d rapid-drill questions in one sitting, interleaved across the three "
              "sets. Same format throughout &mdash; one fact, four names, no doses. Set a "
              "shorter length on this screen if you want a sample rather than the whole "
              "thing." % len(qs),
        questions=qs, already_converted=True,
        navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6",
    )
    open(os.path.join(OUT, "pharm-e2-master-drill.html"), "w", encoding="utf-8").write(html)
    print("  %-46s %3d questions" % ("pharm-e2-master-drill.html", len(qs)))


if __name__ == "__main__":
    main()
