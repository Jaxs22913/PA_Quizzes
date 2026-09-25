#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the six Pharmacology I Exam 2 lipid quizzes (Lecture 7).

Same shape as render_pharm_ent.py: one topic, two versions, the Exam 2 palette.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 2")
SETS = json.load(open(os.path.join(HERE, "pharm_lipid_sets.json"), encoding="utf-8"))
PALETTE = dict(navy="#2f4f6b", indigo="#4a7fa5", gold="#b8862f", ice="#eef3f7")

NOTE = ("<b>What these do and do not ask.</b> <b>Indications, adverse effects, "
        "contraindications and patient education are in</b>, weighted above mechanism. "
        "<b>Doses are out</b>, and so are risk calculations and choosing a statin intensity "
        "for a given patient, which is why the sets run 14 to 16 rather than the usual 30. "
        "Every option carries its own reason, correct and incorrect alike.")

CONF = [
 ("statin", "Statins &amp; Statin Guidelines", "lipid-statins-quiz",
  ["Mechanism", "CYP3A4 statins", "Muscle &amp; liver", "Benefit groups", "Intensity"],
  "Statins are first line because they are the most effective and best tolerated, and they "
  "work by making the liver <b>pull more LDL (low-density lipoprotein) out of the blood</b> "
  "through extra LDL receptors. Know which three are <b>CYP3A4 substrates</b> (atorvastatin, "
  "lovastatin, simvastatin) and which one barely uses CYP; how muscle toxicity and liver "
  "enzyme rises are handled; the four benefit groups; and the two statins that reach high "
  "intensity."),
 ("ldl", "Resins, Ezetimibe &amp; PCSK9 Inhibitors", "lipid-resins-ezetimibe-pcsk9-quiz",
  ["Bile acid sequestrants", "Triglyceride limits", "Administration", "Ezetimibe", "PCSK9"],
  "Three more ways to the statins' end point &mdash; more active LDL receptors on the liver. "
  "The resins carry most of the patient education: mix the powder, take it with a meal, and "
  "<b>separate other drugs by 1 hour before or 4 hours after</b>. They are safe enough for "
  "pregnancy but <b>can raise triglycerides</b>, so a high level contraindicates them. "
  "Ezetimibe blocks absorption and rides along with a statin; the PCSK9 inhibitors are "
  "injectable antibodies."),
 ("tg", "Fibrates, Niacin &amp; Lipid Profiles", "lipid-fibrates-niacin-quiz",
  ["Fibrates", "Niacin", "Flushing", "Contraindications", "Class lipid profiles"],
  "The two classes that <b>lower triglycerides and raise HDL (high-density lipoprotein)</b>, "
  "and how to tell every class apart on the lipid profile. Fibrates activate PPAR-alpha and "
  "cause gallstones; niacin flushes (take aspirin first) and raises uric acid and glucose. "
  "Watch the flip: the class that treats very high triglycerides is not the one that is "
  "contraindicated by them."),
]

for key, label, stem, chips, blurb in CONF:
    for n in (1, 2):
        qs = SETS["%s%d" % (key, n)]
        fn = "%s.html" % stem if n == 1 else "%s-version-2.html" % stem
        html = render(
            title="%s Quiz %d &mdash; Pharmacology I Exam 2" % (label, n),
            h1=label, sub="Pharmacology I &middot; Exam 2 &middot; Lipid-Lowering Drugs",
            pill="%d questions" % len(qs), chips=chips,
            intro=blurb + " " + NOTE,
            questions=qs, already_converted=True, **PALETTE)
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
        print("wrote %-50s %d questions" % (fn, len(qs)))
