#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the eight Pharmacology I Exam 2 ENT quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 2")
SETS = json.load(open(os.path.join(HERE, "pharm_ent_sets.json"), encoding="utf-8"))
# The Exam 2 palette, taken from render_pharm_oph.py rather than invented.
PALETTE = dict(navy="#2f4f6b", indigo="#4a7fa5", gold="#b8862f", ice="#eef3f7")

# Deliberately NOT the note carried by the ophthalmology quizzes. That one says
# indications and adverse effects are not examinable; Jaxon corrected that on
# 2026-09-18. Dosing and formulations remain out, so the sets are smaller than
# the house 30, but the drug frames are asked in full.
NOTE = ("<b>What these do and do not ask.</b> <b>Indications and adverse effects are in</b> "
        "&mdash; each agent is asked for what it is used for and what it does to the patient. "
        "<b>Dosing and formulations are out</b>, so nothing here turns on a milligram or a "
        "strength, which is why the sets are 17 to 19 rather than the usual 30. Every option "
        "carries its own reason, correct and incorrect alike.")

CONF = [
 ("anti", "ENT Anti-infectives &amp; Antifungals", "ent-anti-infectives-quiz",
  ["Otitis media", "Rhinosinusitis", "Pharyngitis", "Otic drops", "Antifungals"],
  "The three infections share three organisms, so the reasoning repeats with one change each "
  "time: the ear starts on high-dose amoxicillin and the sinuses start a step further along, "
  "because beta-lactamase producing <i>Haemophilus influenzae</i> is common there. The throat is "
  "different again &mdash; the antibiotic is given to prevent rheumatic fever rather than to "
  "shorten the sore throat. Then the otic drops, where <b>polymyxin B through a perforation "
  "costs hearing</b>, and the two antifungals, which differ by whether they are absorbed at all."),
 ("inflam", "Analgesics &amp; Anti-inflammatories", "ent-analgesics-quiz",
  ["Salicylates", "Reye&rsquo;s syndrome", "Ibuprofen", "Interactions", "Acetaminophen"],
  "Aspirin against ibuprofen is the pairing that organizes this: <b>irreversible against "
  "reversible</b> at cyclooxygenase, which is why one disables a platelet for its lifetime and "
  "the other wears off. Aspirin then stacks three different jobs by exposure, with tinnitus as "
  "the audible marker of the top of that ladder. <b>Reye&rsquo;s syndrome gets its own run of "
  "questions</b> &mdash; the preceding viral illness, the five stages and the mortality &mdash; "
  "because it is the reason a cheap and useful drug is kept away from children."),
 ("hist", "Antihistamines &amp; Corticosteroids", "ent-antihistamines-steroids-quiz",
  ["Histamine", "H1 vs H2", "Generations", "Nasal sprays", "Steroid effects"],
  "One distinction explains most of the antihistamine half: first generation agents enter the "
  "central nervous system and hit other receptor systems on the way, second generation ones do "
  "not. Sedation, the motion sickness use, the dry mouth and the sleep-aid shelf all fall out of "
  "it. The steroid half is about the price of the drug rather than its effect &mdash; the eye "
  "findings, the bone and tendon damage, and the interactions that run through potassium."),
 ("cough", "Decongestants, Antitussives &amp; Expectorants", "ent-decongestants-cough-quiz",
  ["Decongestants", "Rebound", "Cough reflex", "Antitussives", "Mucolytics"],
  "The topical decongestant has a hard time limit and a specific consequence for exceeding it: "
  "<b>rebound congestion sends the patient back to the same bottle</b>. The two antitussives then "
  "work at opposite ends of one reflex &mdash; benzonatate numbs the receptors where a cough "
  "starts, dextromethorphan suppresses the center in the medulla that organizes it &mdash; and "
  "that difference decides which one a patient on an antidepressant can safely have."),
]

for key, label, stem, chips, blurb in CONF:
    for n in (1, 2):
        qs = SETS["%s%d" % (key, n)]
        fn = "%s.html" % stem if n == 1 else "%s-version-2.html" % stem
        html = render(
            title="%s Quiz %d &mdash; Pharmacology I Exam 2" % (label, n),
            h1=label, sub="Pharmacology I &middot; Exam 2 &middot; Ear, Nose and Throat",
            pill="%d questions" % len(qs), chips=chips,
            intro=blurb + " " + NOTE,
            questions=qs, already_converted=True, **PALETTE)
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
        print("wrote %-46s %d questions" % (fn, len(qs)))
