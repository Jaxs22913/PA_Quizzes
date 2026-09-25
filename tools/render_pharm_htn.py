#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the eight Pharmacology I Exam 2 antihypertensive quizzes (Lecture 6).

Same shape as render_pharm_ent.py: one topic, two versions, the Exam 2 palette.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 2")
SETS = json.load(open(os.path.join(HERE, "pharm_htn_sets.json"), encoding="utf-8"))
# The Exam 2 palette, taken from render_pharm_oph.py rather than invented.
PALETTE = dict(navy="#2f4f6b", indigo="#4a7fa5", gold="#b8862f", ice="#eef3f7")

NOTE = ("<b>What these do and do not ask.</b> <b>Indications, adverse effects, "
        "contraindications and patient education are in</b>, weighted above mechanism. "
        "<b>Doses are out</b>, so nothing here turns on a milligram, which is why the sets "
        "run 14 to 18 rather than the usual 30. Diuretics belong to a later exam and appear "
        "only as the add-on step of the treatment algorithm. Every option carries its own "
        "reason, correct and incorrect alike.")

CONF = [
 ("raas", "Renin-Angiotensin Inhibitors &amp; First-Line Choice", "htn-raas-inhibitors-quiz",
  ["ACE inhibitors", "Angiotensin receptor blockers", "Potassium", "Cough &amp; angioedema",
   "Treatment algorithm"],
  "Two drug classes that block the same system at different points, and the differences "
  "that follow. ACE (angiotensin-converting enzyme) inhibitors also stop bradykinin being "
  "broken down, which is where the <b>dry cough and angioedema</b> come from and why an "
  "angiotensin receptor blocker is the switch. Both classes <b>raise potassium</b> &mdash; "
  "know who is at risk &mdash; and both are avoided in the second and third trimesters. "
  "Then the algorithm: what to start for a given comorbidity, and what to add next."),
 ("ccb", "Calcium Channel Blockers", "htn-calcium-channel-blockers-quiz",
  ["Dihydropyridines", "Non-dihydropyridines", "Nodal effects", "CYP3A4", "Contraindications"],
  "One distinction organizes the whole class: <b>only diltiazem and verapamil act on the "
  "heart</b>, slowing the rate and atrioventricular conduction, so only they treat "
  "supraventricular tachycardia &mdash; and their bradycardia, heart block and worsening "
  "heart failure follow from the same action. Dihydropyridines act on vessels, so their "
  "problems are reflex tachycardia and edema. The non-dihydropyridines also <b>inhibit "
  "CYP3A4</b>, which raises three statins."),
 ("beta", "Beta Blockers", "htn-beta-blockers-quiz",
  ["Selectivity", "Heart failure agents", "Indications", "Hypoglycemia", "Withdrawal"],
  "Know the groups: non-selective, beta-1 selective, and the two that also block alpha-1 "
  "(carvedilol and labetalol). Selectivity decides who can safely take one &mdash; "
  "bronchospasm is less likely with beta-1 selective agents. Then the indications beyond "
  "blood pressure, the three agents used in heart failure, and the patient education: "
  "<b>masked hypoglycemia</b> and <b>never stopping abruptly</b>."),
 ("other", "Alpha-1 Blockers, Central Agents &amp; Vasodilators", "htn-alpha-central-vasodilators-quiz",
  ["Prazosin &amp; tamsulosin", "Clonidine", "Hydralazine", "Minoxidil", "Nitroprusside"],
  "The specialty agents, each with one or two facts that define it. Alpha-1 blockers cause "
  "orthostatic hypotension and treat the prostate. Clonidine <b>stimulates</b> central "
  "alpha-2 receptors and rebounds dangerously if stopped. Hydralazine is N-acetylated "
  "(slow acetylators risk lupus) and can turn stools black; minoxidil opens potassium "
  "channels and grows hair; nitroprusside releases cyanide."),
]

for key, label, stem, chips, blurb in CONF:
    for n in (1, 2):
        qs = SETS["%s%d" % (key, n)]
        fn = "%s.html" % stem if n == 1 else "%s-version-2.html" % stem
        html = render(
            title="%s Quiz %d &mdash; Pharmacology I Exam 2" % (label, n),
            h1=label, sub="Pharmacology I &middot; Exam 2 &middot; Antihypertensives",
            pill="%d questions" % len(qs), chips=chips,
            intro=blurb + " " + NOTE,
            questions=qs, already_converted=True, **PALETTE)
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
        print("wrote %-50s %d questions" % (fn, len(qs)))
