#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Pharmacology I Exam 2 rapid-drill quizzes.

Same format as the Exam 1 drills: one fact, four DRUG NAMES underneath, no
vignette and no doses. Every wrong choice is another drug from the same family,
so the question is a real discrimination rather than a category guess.

Exam 2 had no drills at all until now, though [[pharmacology_exam_spec]] calls
for them and Exam 1 carries six.

2026-09-24: Lecture 6 (Antihypertensives.pptx, deck key HTN) and Lecture 7
(Lipids.pptx, deck key LIP) added as two more sets. Their banks are
pharm_drill_htn.py and pharm_drill_lipid.py; the master drill now interleaves
five sets instead of three. ENT (Lecture 5) still has no drill.

2026-09-30: Lecture 8 (Myocardial Ischemia Drugs.pptx, deck key MI) added as a
sixth set (pharm_drill_mi.py); the master drill now interleaves six sets.

2026-10-03 (Jaxon: "separate the drill quiz by lecture also so I can hone each lecture
individually"): one drill per lecture, L4-L8, each titled "Lecture N ... Drill".
  * Lecture 5 (ENT Jax Pharmacology.pptx, deck key ENT) finally gets a drill (pharm_drill_ent.py);
  * Lecture 4 gets ONE combined drill built from the three ocular banks, interleaved; the three
    ocular topic drills stay as they were;
  * Lectures 6, 7, 8 keep their file names and URLs and are only retitled;
  * the master drill now interleaves the ENT set as well.

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
import pharm_drill_ent as en
import pharm_drill_htn as ht
import pharm_drill_lipid as lp
import pharm_drill_mi as mi

OUT = os.path.join(ROOT, "Pharmacology I Exam 2")
DECK = {"OPH": "Ophthalmology-2.pptx", "ENT": "ENT Jax Pharmacology.pptx", "HTN": "Antihypertensives.pptx",
        "LIP": "Lipids.pptx", "MI": "Myocardial Ischemia Drugs.pptx"}

SETS = [
    (ai, "pharm-e2-drill-anti-infectives.html", "Ocular Anti-infectives Drill",
     "Lecture 4 — Ocular antibacterials, antivirals and antifungals",
     ["Macrolides", "Fluoroquinolones", "Aminoglycosides", "Antivirals",
      "Antifungals", "Delivery &amp; kinetics"]),
    (al, "pharm-e2-drill-allergy-inflammation.html",
     "Allergy, Inflammation &amp; Dry Eye Drill",
     "Lecture 4 — Ocular allergy, inflammation and dry eye",
     ["Antihistamines", "Mast cell stabilizers", "Vasoconstrictors",
      "Non-steroidals", "Glucocorticoids", "Dry eye"]),
    (gl, "pharm-e2-drill-glaucoma-diagnostics.html",
     "Glaucoma &amp; Diagnostics Drill",
     "Lecture 4 — Glaucoma agents, anesthetics, cycloplegics and stains",
     ["Prostaglandins", "Beta blockers", "Alpha-2 agonists",
      "Carbonic anhydrase inhibitors", "Cholinergics", "Diagnostics"]),
    (en, "pharm-e2-drill-ent.html", "Lecture 5 Ear, Nose and Throat Drugs Drill",
     "Lecture 5 — Ear, nose and throat drugs",
     ["Ear, sinus and throat antibiotics", "Ear drops and antifungals",
      "Pain and fever relievers", "Antihistamines", "Corticosteroids",
      "Decongestants", "Cough and mucus agents"]),
    (ht, "pharm-e2-drill-antihypertensives.html", "Lecture 6 Antihypertensives Drill",
     "Lecture 6 — Antihypertensive drug classes and agents",
     ["ACE inhibitors &amp; receptor blockers", "Calcium channel blockers",
      "Beta blockers", "Alpha &amp; central agents", "Vasodilators"]),
    (lp, "pharm-e2-drill-lipids.html", "Lecture 7 Lipid-Lowering Drugs Drill",
     "Lecture 7 — Drugs that lower cholesterol and triglyceride levels",
     ["Statins", "Ezetimibe", "Fibrates", "Bile acid sequestrants", "Niacin",
      "PCSK9 inhibitors"]),
    (mi, "pharm-e2-drill-myocardial-ischemia.html", "Lecture 8 Myocardial Ischemia Drill",
     "Lecture 8 — Drugs used to treat myocardial ischemia",
     ["Beta blockers", "Calcium channel blockers", "Nitrates", "Antiplatelets",
      "Fibrinolytics"]),
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


LECTURE4 = ("pharm-e2-drill-ophthalmic.html", "Lecture 4 Ophthalmic Drugs Drill",
            "Lecture 4 — Ophthalmic drugs",
            ["Ocular anti-infectives", "Allergy &amp; inflammation", "Glaucoma",
             "Anesthetics, cycloplegics &amp; stains", "Dry eye"])


def interleave(banks):
    """Round-robin across several banks (smallest bank runs out first)."""
    out = []
    for i in range(max(len(b) for b in banks)):
        for b in banks:
            if i < len(b):
                out.append(b[i])
    return out


def page(qs, title, h1, chips, intro, name):
    html = render(
        title="%s | Pharmacology I Exam 2" % title.replace("&amp;", "&"),
        h1=h1,
        sub="Pharmacology I &middot; Exam 2 &middot; rapid drill",
        pill="%d questions" % len(qs),
        chips=chips, intro=intro,
        questions=qs, already_converted=True,
        navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6",
    )
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
    print("  %-46s %3d questions" % (name, len(qs)))


def main():
    total = 0
    for mod, fname, title, io, chips in SETS:
        qs = build(mod.ITEMS, io)
        page(qs, title, title, chips, INTRO, fname)
        total += len(qs)
    print("%d drill questions across %d sets" % (total, len(SETS)))

    # Lecture 4 in one drill: every item of the three ocular banks, interleaved.
    fname, title, io, chips = LECTURE4
    ocular = [ai.ITEMS, al.ITEMS, gl.ITEMS]
    qs = build(interleave(ocular), io)
    page(qs, title, title, chips,
         INTRO + " This one covers the whole Lecture 4 deck: the three ocular topic drills "
         "(anti-infectives; allergy, inflammation and dry eye; glaucoma and diagnostics) "
         "interleaved in one set.", fname)

    qs = master([(m.ITEMS, io) for m, _f, _t, io, _c in SETS])
    page(qs, "Master Drill", "Master Drill &mdash; every Exam 2 drill question",
         ["Lecture 4 Ophthalmic", "Lecture 5 Ear, nose and throat", "Lecture 6 Antihypertensives",
          "Lecture 7 Lipids", "Lecture 8 Myocardial ischemia"],
         "All %d rapid-drill questions in one sitting, interleaved across the %d "
         "topic sets (the five lectures). Same format throughout &mdash; one fact, four names, no "
         "doses. Set a shorter length on this screen if you want a sample rather than the whole "
         "thing." % (len(qs), len(SETS)),
         "pharm-e2-master-drill.html")


if __name__ == "__main__":
    main()
