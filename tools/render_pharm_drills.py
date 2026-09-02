#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the five Pharmacology rapid-drill quizzes.

Jaxon, 2026-09-02: "make the Pharm questions really simple and drill ... I want
simple sets to really drill the need to know stuff that are particular for each
drug and class and stuff that stands out."

One fact per question, four drug names underneath, no vignette and no doses.
The banks explain how "stands out" was decided; see tools/pharm_drill_*.py.

Answer positions rotate through A-D, never chosen while authoring.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))

from render import render
import pharm_drill_antibacterials as ab
import pharm_drill_antifungals as af
import pharm_drill_cholinergic as ch
import pharm_drill_adrenergic as ad
import pharm_drill_dermatology as dm
import pharm_drill_classes as cl

OUT = os.path.join(ROOT, "Pharmacology I Exam 1")
DECK = {"L1": "Antibiotics, Antivirals, and Antifungals.pptx",
        "L2": "02. Dermatology Medications(1).pptx",
        "L3": "03. ANS Pharmacology(1).pptx"}

SETS = [
    (ab, "pharm-drill-antibacterials.html", "Antibacterials Drill",
     "Topic — Antibacterials",
     ["Penicillins", "Cephalosporins", "Macrolides", "Fluoroquinolones",
      "Aminoglycosides", "Vancomycin"]),
    (af, "pharm-drill-antifungals-antivirals.html", "Antifungals &amp; Antivirals Drill",
     "Topic — Antifungals, antivirals and antiparasitics",
     ["Azoles", "Amphotericin B", "Echinocandins", "Antivirals", "Topical antifungals"]),
    (ch, "pharm-drill-cholinergic.html", "Cholinergic &amp; Anticholinergic Drill",
     "Topic — Cholinergic, anticholinergic and neuromuscular",
     ["Cholinergic agonists", "Cholinesterase inhibitors", "Antimuscarinics",
      "Neuromuscular blockers"]),
    (ad, "pharm-drill-adrenergic.html", "Adrenergic &amp; Blockers Drill",
     "Topic — Adrenergic agonists and the alpha and beta blockers",
     ["Catecholamines", "Alpha blockers", "Beta blockers", "Decongestants"]),
    (dm, "pharm-drill-dermatology.html", "Dermatology Medications Drill",
     "Topic — Dermatology medications",
     ["Acne", "Retinoids", "Topical steroids", "Topical antimicrobials"]),
    # Jaxon, 2026-09-02: "If theres stuff specific to a whole class you can make
    # drill questions for those." Every option here is a class, which is the one
    # case where the one-drug-per-choice rule does not apply.
    (cl, "pharm-drill-classes.html", "Drug Classes Drill",
     "Topic — Facts that belong to a whole class",
     ["Antibacterial classes", "Antifungal classes", "Autonomic classes",
      "Topical classes"]),
]

INTRO = ("One fact, four drug names. No patient, no story &mdash; just the thing that drug "
         "or class is known for. Every wrong choice is another drug from the same family, "
         "so it is a real discrimination rather than a category guess.")


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


def main():
    total = 0
    for mod, fname, title, io, chips in SETS:
        qs = build(mod.ITEMS, io)
        html = render(
            title="%s | Pharmacology I Exam 1" % title.replace("&amp;", "&"),
            h1=title,
            sub="Pharmacology I &middot; Exam 1 &middot; rapid drill",
            pill="%d questions" % len(qs),
            chips=chips, intro=INTRO,
            questions=qs, already_converted=True,
            # Pharmacology I Exam 1's established palette.
            navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6",
        )
        open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
        print("  %-44s %3d questions" % (fname, len(qs)))
        total += len(qs)
    print("%d drill questions across %d sets" % (total, len(SETS)))


if __name__ == "__main__":
    main()
