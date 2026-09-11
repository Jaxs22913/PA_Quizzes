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

NOTE = ("<b>What this lecture does not test.</b> Dr. Wood rules four things out in as many words: "
        "<b>dosing</b> (&ldquo;not for memorization sake&hellip; you can always look up the dosing "
        "if you know which drug you actually want to use in the first place&rdquo;), "
        "<b>formulations</b>, the <b>indications table</b> (&ldquo;don&rsquo;t worry so much about "
        "indications for use&hellip; a lot of them have a lot of crossover&rdquo;), and "
        "<b>which agent causes which adverse effect</b> (&ldquo;any of these can do that&rdquo;). "
        "Nothing here is built on any of it. What is left is mechanism, drug CHOICE, and the "
        "handful of facts he stops to make &mdash; which is why these sets are 20 and 16 rather "
        "than the usual 30.")

CONF = [
 ("anti", "Ocular Delivery &amp; Anti-infectives", "anti-infectives-quiz",
  ["Delivery &amp; kinetics", "Antibiotics", "Antivirals", "Antifungals", "Precautions"],
  "How a drop gets into the eye and out again, and the six anti-infective classes. The two "
  "ribosomal classes are the pairing worth holding &mdash; macrolides at the 50S, aminoglycosides "
  "at the 30S &mdash; and drug choice turns on a small number of rules: fluoroquinolones for "
  "corneal ulcers and suspected <i>Pseudomonas</i>, erythromycin as the common and soothing one, "
  "and sulfacetamide off the table in sulfonamide allergy."),
 ("inflam", "Allergy, Inflammation &amp; Dry Eye", "allergy-inflammation-quiz",
  ["Allergy", "Antihistamines", "Mast cell stabilisers", "NSAIDs &amp; steroids", "Dry eye"],
  "<b>Rebound hyperaemia is the question he promised to ask</b> &mdash; &ldquo;I will tell you, I "
  "will ask this question&rdquo; &mdash; so it is here three times over, from the mechanism, the "
  "counselling point and the toddler who swallows the bottle. Beyond it: antihistamines work in "
  "minutes and mast cell stabilisers take 5 to 14 days, which decides which one an acute "
  "presentation gets; and the steroids sit one step above the nonsteroidals in the same cascade."),
 ("glauc", "Glaucoma &amp; Diagnostic Agents", "glaucoma-diagnostics-quiz",
  ["Definitions", "Prostaglandins", "Beta blockers", "Alpha agonists &amp; inhibitors",
   "Anaesthetics &amp; cycloplegics"],
  "Every glaucoma drug sorts by whether it reduces aqueous PRODUCTION or increases OUTFLOW, and "
  "the alpha agonists sit on both sides, which is where most errors come from. Each class then "
  "carries one fact that decides whether a given patient can have it &mdash; asthma for the "
  "non-selective beta blockers, age under two for the alpha agonists, visual blurring for the "
  "cholinergics. Anaesthetics, cycloplegics and fluorescein close the lecture."),
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
