#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Pharmacology I Exam 3 rapid drills (Lecture 9, Diuretics and Heart Failure Drugs; Lecture 10, Antiarrhythmics;
Lecture 11, Pulmonary Infections, Asthma and Chronic Obstructive Pulmonary Disease).

Same format as the Exam 1 and Exam 2 drills (pharmacology_exam_spec, RAPID DRILLS): one fact, four DRUG NAMES underneath,
no vignette, no doses, one drug per choice (a class name is offered only when the stem itself asks for a class, and then
every choice is a class). Banks: tools/pharm_drill_hf.py, tools/pharm_drill_aa.py and tools/pharm_drill_pulm.py (ITEMS). Answer positions rotate
through A-D, never chosen while authoring. A master drill is added once Lectures 12-13 are in.

  python3 tools/render_pharm_e3_drills.py        # Lecture 9 drill
  python3 tools/render_pharm_e3_drills.py aa     # Lecture 10 drill only
  python3 tools/render_pharm_e3_drills.py pu     # Lecture 11 drill only
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
import pharm_drill_hf as hf
import pharm_drill_aa as aa
import pharm_drill_pulm as pu

OUT = os.path.join(ROOT, "Pharmacology I Exam 3")
DECK = {"HF": "Diuretics and Heart Failure Drugs.pptx", "MI": "Myocardial Ischemia Drugs.pptx", "HTN": "Antihypertensives.pptx",
        "OPH": "Ophthalmology-2.pptx", "AA": "Antiarrhythmics.pptx",
        "PU": "Pulmonology-2.pptx"}
IO = "Topic — Diuretics and heart failure drugs"
CHIPS = ["Loop diuretics", "Thiazides", "Potassium-sparing", "Aldosterone antagonists", "Carbonic anhydrase inhibitors",
         "Heart failure drugs", "Digoxin"]
IO_AA = "Topic — Antiarrhythmic drugs"
CHIPS_AA = ["Class IA", "Class IB", "Class IC", "Class II beta blockers", "Class III potassium channel blockers",
            "Class IV calcium channel blockers", "Adenosine, digoxin, magnesium"]
IO_PU = "Topic — Pulmonary infections, asthma and chronic obstructive pulmonary disease"
CHIPS_PU = ["Pneumonia antibiotics", "Tuberculosis drugs", "Anaphylaxis", "Beta-2 agonists", "Anticholinergics and theophylline",
            "Inhaled corticosteroids and combinations", "Leukotriene, mast cell and biologic agents", "Smoking cessation"]
INTRO = ("One fact, four drug names. No patient, no story &mdash; just the thing that drug or class is known for, and "
         "<b>no doses</b>. Every wrong choice is another drug from the same family, so it is a real discrimination "
         "rather than a category guess.")


def build(items, io=IO):
    out = []
    for n, it in enumerate(items):
        opts = [[it["ans"], "Correct. " + it["why"]]] + [[w, r] for w, r in it["wrong"]]
        slot = n % 4
        opts.insert(slot, opts.pop(0))
        lect, slide = it["src"]
        out.append({"topic": it["ans"], "io": io, "q": it["q"], "opts": opts, "c": slot,
                    "cite": "%s, Slide %d" % (DECK[lect], slide)})
    return out


def main_aa():
    qs = build(aa.ITEMS, IO_AA)
    html = render(title="Antiarrhythmic Drugs Drill | Pharmacology I Exam 3",
                  h1="Antiarrhythmic Drugs Drill", sub="Pharmacology I &middot; Exam 3 &middot; rapid drill",
                  pill="%d questions" % len(qs), chips=CHIPS_AA, intro=INTRO, questions=qs, already_converted=True,
                  navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
    open(os.path.join(OUT, "pharm-e3-drill-antiarrhythmics.html"), "w", encoding="utf-8").write(html)
    print("wrote pharm-e3-drill-antiarrhythmics.html  %d questions" % len(qs))


def main_pu():
    qs = build(pu.ITEMS, IO_PU)
    html = render(title="Pulmonary Drugs Drill | Pharmacology I Exam 3",
                  h1="Pulmonary Drugs Drill", sub="Pharmacology I &middot; Exam 3 &middot; rapid drill",
                  pill="%d questions" % len(qs), chips=CHIPS_PU, intro=INTRO, questions=qs, already_converted=True,
                  navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
    open(os.path.join(OUT, "pharm-e3-drill-pulmonary.html"), "w", encoding="utf-8").write(html)
    print("wrote pharm-e3-drill-pulmonary.html  %d questions" % len(qs))


def main():
    qs = build(hf.ITEMS)
    html = render(title="Diuretics & Heart Failure Drugs Drill | Pharmacology I Exam 3",
                  h1="Diuretics &amp; Heart Failure Drugs Drill", sub="Pharmacology I &middot; Exam 3 &middot; rapid drill",
                  pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO, questions=qs, already_converted=True,
                  navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")
    open(os.path.join(OUT, "pharm-e3-drill-diuretics-heart-failure.html"), "w", encoding="utf-8").write(html)
    print("wrote pharm-e3-drill-diuretics-heart-failure.html  %d questions" % len(qs))


if __name__ == "__main__":
    {"aa": main_aa, "pu": main_pu}.get((sys.argv[1:] or [""])[0], main)()
