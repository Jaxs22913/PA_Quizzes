#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the six Pharmacology I Exam 2 ophthalmology quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 2")
SETS = json.load(open(os.path.join(HERE, "pharm_oph_sets.json"), encoding="utf-8"))
PALETTE = dict(navy="#2f4f6b", indigo="#4a7fa5", gold="#b8862f", ice="#eef3f7")

# CORRECTED 2026-09-18. This note used to say indications and adverse effects
# were not examinable, which over-read what was actually said. Both quotes are
# narrower than that: one is about a specific table of OVERLAPPING antibiotic
# indications, the other about which agents cause ocular IRRITATION, since any
# of them can. Neither rules out an agent's indications or the adverse effects
# that name one drug and no other, and the pools were always full of both.
NOTE = ("<b>What this lecture does not test.</b> <b>Dosing</b> &mdash; &ldquo;not for "
        "memorization sake&hellip; you can always look up the dosing if you know which drug you "
        "actually want to use in the first place&rdquo; &mdash; and <b>formulations</b>, and the "
        "specific <b>combination products</b> (&ldquo;the specific combinations, I don&rsquo;t "
        "care that you memorize, <b>BUT</b>&hellip; what would be a helpful second line agent to "
        "add on?&rdquo; &mdash; products out, reasoning in). "
        "Two things are narrower than they sound. &ldquo;Don&rsquo;t worry so much about "
        "indications for use&hellip; a lot of them have a lot of crossover&rdquo; is about the "
        "<b>table of overlapping antibiotic indications</b>, not about what an agent is for. And "
        "&ldquo;don&rsquo;t memorize which ones cause eye irritation or hypersensitivity&hellip; "
        "any of these can do that&rdquo; is about the <b>generic</b> irritation, not about the "
        "effects that name one drug &mdash; ciprofloxacin&rsquo;s white precipitate, the bitter "
        "taste of the carbonic anhydrase inhibitors, the iris color change of the "
        "prostaglandins. <b>Indications and agent-specific adverse effects are asked here.</b>")

CONF = [
 ("anti", "Ocular Delivery &amp; Anti-infectives", "anti-infectives-quiz",
  ["Delivery &amp; kinetics", "Antibiotics", "Antivirals", "Antifungals", "Precautions"],
  "How a drop gets into the eye and out again, and the six anti-infective classes. The two "
  "ribosomal classes are the pairing worth holding &mdash; macrolides at the 50S, aminoglycosides "
  "at the 30S &mdash; and drug choice turns on a small number of rules: fluoroquinolones for "
  "corneal ulcers and suspected <i>Pseudomonas</i>, erythromycin as the common and soothing one, "
  "and sulfacetamide off the table in sulfonamide allergy."),
 ("inflam", "Allergy, Inflammation &amp; Dry Eye", "allergy-inflammation-quiz",
  ["Allergy", "Antihistamines", "Mast cell stabilizers", "NSAIDs &amp; steroids", "Dry eye"],
  "<b>Rebound hyperemia is the question he promised to ask</b> &mdash; &ldquo;I will tell you, I "
  "will ask this question&rdquo; &mdash; so it is here three times over, from the mechanism, the "
  "counseling point and the toddler who swallows the bottle. Beyond it: antihistamines work in "
  "minutes and mast cell stabilizers take 5 to 14 days, which decides which one an acute "
  "presentation gets; and the steroids sit one step above the nonsteroidals in the same cascade."),
 ("glauc", "Glaucoma &amp; Diagnostic Agents", "glaucoma-diagnostics-quiz",
  ["Definitions", "Prostaglandins", "Beta blockers", "Alpha agonists &amp; inhibitors",
   "Anesthetics &amp; cycloplegics"],
  "Every glaucoma drug sorts by whether it reduces aqueous PRODUCTION or increases OUTFLOW, and "
  "the alpha agonists sit on both sides, which is where most errors come from. Each class then "
  "carries one fact that decides whether a given patient can have it &mdash; asthma for the "
  "non-selective beta blockers, age under two for the alpha agonists, visual blurring for the "
  "cholinergics. Anesthetics, cycloplegics and fluorescein close the lecture."),
]

for key, label, stem, chips, blurb in CONF:
    for n in (1, 2):
        qs = SETS["%s%d" % (key, n)]
        fn = "%s.html" % stem if n == 1 else "%s-version-2.html" % stem
        html = render(
            title="%s Quiz %d &mdash; Pharmacology I Exam 2" % (label, n),
            h1=label, sub="Pharmacology I &middot; Exam 2 &middot; Ophthalmology",
            pill="%d questions" % len(qs), chips=chips,
            intro=blurb + " " + NOTE,
            questions=qs, already_converted=True, **PALETTE)
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
        print("wrote %-44s %d questions" % (fn, len(qs)))
