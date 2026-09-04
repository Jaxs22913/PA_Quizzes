#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Clinical Medicine and Surgery I, Exam 3 cram sheet (ENT block).

The guide carries the reasoning; this carries only what has to come back cold.

THE FIRST TWO SECTIONS ARE THE TESTS AND THE DURATIONS, not a condition list.
Weber and Rinne is a syllabus objective in its own right AND the question
Jaquith said outright is on the paper; the vertigo durations are the fastest
sort in the block. Everything after them is disease detail.

THE LISTS ARE GENERATED FROM THE CHART DATA. Which conditions are conductive,
which are sensorineural, which are emergent -- all read off the same rows the
chart and guide use. Hand-writing those lists is exactly how the Exam 2 sheet
drifted from its chart within the hour.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
sys.path.insert(0, HERE)
from render import render
from _cms_e3_chart_l15 import ROWS_L15, DIFF_L15
from _cms_e3_chart_l16 import ROWS_L16, DIFF_L16

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 3", "cms-exam-3-cram-sheet.html")
ROWS = ROWS_L15 + ROWS_L16
DIFF = dict(DIFF_L15, **DIFF_L16)


def strip(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def by_hearing(kind):
    """Every condition whose hearing-loss cell names this type -- from the chart."""
    out = []
    for n, *_ in ROWS:
        h = strip(DIFF[n][1]).lower()
        if kind == "cond" and "conductive" in h and "sensorineural" not in h:
            out.append(n)
        elif kind == "snhl" and "sensorineural" in h and "conductive" not in h:
            out.append(n)
        elif kind == "none" and h.startswith(("none", "not affected")):
            out.append(n)
    return out


def by_urgency(level):
    return [r[0] for r in ROWS if level in r[6].upper()]


def lst(names):
    return " &middot; ".join(strip(n).upper() for n in names)


topics = [
 dict(id="tests", label="The tests", color="#6a4fa3", tag="objectives b to f", rows=[
  ["WEBER", "Tuning fork on the MIDLINE. Compares BONE conduction between the two ears. Asks WHICH SIDE IS LOUDER."],
  ["RINNE", "Tuning fork at the EAR then the MASTOID. Compares AIR against BONE in ONE ear."],
  ["CONDUCTIVE", "Weber lateralises <b>TO the BAD ear</b>. Rinne: <b>BC &ge; AC</b>. Voice stays SOFT. Hearing BETTER in noise."],
  ["SENSORINEURAL", "Weber lateralises <b>AWAY, to the GOOD ear</b>. Rinne: <b>AC &gt; BC &mdash; SAME AS NORMAL</b>. Voice LOUD. Hearing WORSE in noise."],
  ["WHY WEBER DECIDES", "A sensorineural Rinne looks exactly like a normal ear. Only WEBER separates them."],
  ["THE QUESTION SHE PROMISED", "Fullness + reduced hearing AFTER A COLD, AMBER effusion behind an INTACT drum with REDUCED MOBILITY &rarr; conductive &rarr; <b>Weber TO that ear, BC &ge; AC</b>. She also asks it BACKWARDS: given the fork findings, name the diagnosis &mdash; the distractors die on LOSS TYPE."],
  ["AUDIOMETRY &mdash; ALL BY 20s", "Normal 0&ndash;20 &middot; MILD 20&ndash;40 &middot; MODERATE 40&ndash;60 &middot; SEVERE 60&ndash;80 &middot; <b>PROFOUND &gt;80 dB</b>. The prevalence percentages are explicitly NOT to be memorised."],
  ["TYMPANOGRAM", "<b>A</b> normal &middot; <b>B</b> FLAT = fluid or perforation &middot; <b>C</b> peak NEGATIVE = eustachian tube dysfunction &middot; <b>As</b> SHALLOW/stiff = ossicular FIXATION, tympanosclerosis &middot; <b>Ad</b> DEEP = ossicular DISCONTINUITY, monomeric drum."],
  ["VESTIBULAR", "<b>ELECTRONYSTAGMOGRAPHY</b> = gold standard, one ear at a time. <b>MRI WITH GADOLINIUM</b> = gold standard for RETROCOCHLEAR. <b>DIX-HALLPIKE</b> diagnoses positional vertigo; <b>EPLEY</b> treats it."],
 ]),
 dict(id="vertigo", label="Vertigo, by how long it lasts", color="#15707f",
      tag="she said definitely know this", rows=[
  ["SECONDS (10&ndash;60)", "<b>BENIGN PAROXYSMAL POSITIONAL VERTIGO.</b> On rolling over. Hearing NOT affected, NO tinnitus. Beyond a MINUTE &rarr; think again. Dix-Hallpike diagnoses, EPLEY treats."],
  ["MINUTES TO HOURS", "<b>M&Eacute;NI&Egrave;RE&rsquo;S.</b> Tetrad: vertigo + FLUCTUATING LOW-FREQUENCY sensorineural loss + LOW-TONE tinnitus + FULLNESS. Hearing IS affected. RULE OUT SYPHILIS &mdash; indistinguishable."],
  ["DAYS TO WEEKS, hearing AFFECTED", "<b>LABYRINTHITIS.</b> Inflammation of the membranous labyrinth. Viral. Meclizine or diazepam, steroids, antibiotics ONLY if bacterial features."],
  ["DAYS TO WEEKS, hearing NORMAL", "<b>VESTIBULAR NEURONITIS.</b> Inflammation of the VESTIBULAR portion of CN VIII. BENIGN and SELF-LIMITING. No hearing change, NO focal neurology."],
  ["THE ONE WORD", "Labyrinthitis vs vestibular neuronitis = <b>does it affect HEARING</b>. That is the whole difference."],
  ["CENTRAL &mdash; STOP", "Vertigo + FACIAL PARALYSIS, CROSSED sensory loss, GAZE palsy or HORNER = <b>VERTEBROBASILAR</b>. Vertigo + ATAXIA, HEADACHE or facial numbness = <b>CEREBELLAR INFARCT</b>. Both EMERGENT."],
 ]),
 dict(id="sort", label="Sort the whole block", color="#3a3a6b", tag="generated from the chart",
      rows=[
  ["CONDUCTIVE", lst(by_hearing("cond"))],
  ["SENSORINEURAL", lst(by_hearing("snhl"))],
  ["HEARING NOT AFFECTED", lst(by_hearing("none"))],
  ["EMERGENT", lst(by_urgency("EMERGENT"))],
 ]),
 dict(id="om", label="The otitis media family", color="#8f5aa8", rows=[
  ["ACUTE OTITIS MEDIA", "BULGING ERYTHEMATOUS drum, reduced mobility. Otalgia + FEVER + hearing loss. Peak age ~<b>2 YEARS</b>; adults only 3&ndash;15%."],
  ["ITS CAUSE &mdash; the slide is incomplete", "<b>FAR AND AWAY MOST ARE VIRAL.</b> Bacterial three: <b>S. PNEUMONIAE, H. INFLUENZAE, M. CATARRHALIS</b>. M. catarrhalis has OVERTAKEN H. influenzae because of VACCINATION &mdash; ask IMMUNISATION STATUS."],
  ["ITS TREATMENT", "MOST RESOLVE SPONTANEOUSLY. Bacterial &rarr; <b>AMOXICILLIN</b>. RECURRENT = 3 in 6 months or &gt;4 in 12 &rarr; TYMPANOSTOMY TUBES."],
  ["OTITIS MEDIA WITH EFFUSION", "DULL drum, AIR&ndash;FLUID LEVEL, reduced mobility. OFTEN ASYMPTOMATIC, found incidentally. Treat on <b>DURATION + degree of hearing loss + effect on SPEECH AND LANGUAGE</b>."],
  ["CHRONIC OTITIS MEDIA", "<b>NON-HEALING PERFORATION.</b> Benign = dry. With effusion = serous drainage. SUPPURATIVE = pus. Refer to ENT."],
  ["MASTOIDITIS", "Spread into the MASTOID AIR CELLS. Complication of acute otitis media &mdash; alongside PERFORATION, LABYRINTHITIS, rarely MENINGITIS."],
 ]),
 dict(id="canal", label="The canal", color="#a4502a", rows=[
  ["OTITIS EXTERNA", "<b>PAIN ON MOVING THE TRAGUS.</b> Swimmer. <b>P. AERUGINOSA 38%</b>. Remove debris FIRST, then drops &plusmn; steroid. WICK if the canal is closed."],
  ["MALIGNANT (NECROTIZING)", "<b>ELDERLY DIABETIC</b> + <b>PAIN OUT OF PROPORTION</b> + <b>FACIAL NERVE WEAKNESS</b>. &gt;95% P. aeruginosa. IMAGING shows BONY involvement. <b>ANTIPSEUDOMONAL</b> &mdash; ciprofloxacin. EMERGENT."],
  ["OTOMYCOSIS", "ITCH &gt; pain. <b>ASPERGILLUS = &ldquo;WET NEWSPAPER&rdquo;</b>. <b>CANDIDA = WHITE CURD</b>. Debris removal + topical antifungal."],
  ["CERUMEN IMPACTION", "MOST OFTEN <b>SELF-INDUCED BY CLEANING</b>. Irrigate ONLY if the drum is INTACT, body-temperature water. TUBES or PERFORATION &rarr; ENT."],
  ["FOREIGN BODY", "DO NOT PUSH DEEPER. Firm &rarr; loop/hook. Soft &rarr; alligator forceps. <b>ORGANIC SWELLS WHEN WET</b> &mdash; no irrigation. INSECT &rarr; LIDOCAINE first."],
  ["CARCINOMA OF THE CANAL", "<b>OTITIS EXTERNA THAT WILL NOT RESPOND</b> + BLOODY otorrhoea + FRIABLE canal. Often MISDIAGNOSED. <b>BIOPSY.</b> EMERGENT."],
 ]),
 dict(id="drum", label="The drum, pressure and fixation", color="#7a5a2e", rows=[
  ["EUSTACHIAN TUBE DYSFUNCTION", "<b>RETRACTED</b> drum, reduced mobility. Fullness + CRACKLING/POPPING after a cold. Decongestant + intranasal steroid. <b>NO FLYING until it resolves.</b>"],
  ["BAROTRAUMA", "Flying or DIVING. <b>HAEMOTYMPANUM.</b> Window rupture adds VERTIGO + TINNITUS + SENSORINEURAL loss. MYRINGOTOMY gives instant relief."],
  ["TM PERFORATION", "<b>THE PAIN STOPS</b> when it ruptures. CENTRAL vs MARGINAL. Most heal; after acute otitis media as fast as <b>48&ndash;72 HOURS</b>."],
  ["CHOLESTEATOMA", "<b>KERATIN in a RETRACTION POCKET</b> + <b>RECURRENT OTORRHOEA WITH NO OTITIS EXTERNA</b>. Not a neoplasm, no cholesterol. CT for extent. <b>SURGERY</b> &mdash; it erodes bone."],
  ["OTOSCLEROSIS", "<b>STAPES fixation.</b> Gradual CONDUCTIVE loss with a <b>NORMAL DRUM</b>. <b>HEARS BETTER IN NOISE.</b> Weber TO the affected ear. CT first-line imaging. Stapes prosthesis."],
  ["AURICULAR HAEMATOMA", "Sub-perichondrial. Landmarks LOST. <b>DRAIN WITHIN 7 DAYS</b> &mdash; then splint. Re-check at 12&ndash;24h because it can appear LATE. Otherwise CAULIFLOWER EAR."],
 ]),
 dict(id="snhl", label="Sensorineural causes worth knowing cold", color="#2a5f8f", rows=[
  ["PRESBYCUSIS", "Commonest sensorineural loss. BILATERAL, SYMMETRICAL, GRADUAL, <b>HIGH FREQUENCY FIRST</b>. &ldquo;Hears but cannot make out words.&rdquo; Screen from <b>65</b>."],
  ["OTOTOXICITY", "<b>AMINOGLYCOSIDES</b> most ototoxic and most common &mdash; monitor peaks. Also FUROSEMIDE, ASPIRIN, PLATINUM. <b>Ototoxic drugs are frequently NEPHROTOXIC too.</b>"],
  ["NOISE-INDUCED", "TEMPORARY threshold shift recovers in <b>24&ndash;48h</b>; repeated exposure makes it PERMANENT. Damage from ~80 dB; PAIN at 120."],
  ["SUDDEN SNHL", "<b>UNILATERAL. A SYNDROME, NOT A DISEASE.</b> Viral or vascular. <b>SAME-DAY ENT REFERRAL</b> &mdash; steroids work only in the first weeks."],
  ["ACOUSTIC NEUROMA", "UNILATERAL loss with <b>SPEECH DISCRIMINATION WORSE THAN THE TONES PREDICT</b>. May involve CN V and VII. <b>MRI WITH GADOLINIUM.</b>"],
  ["PERILYMPHATIC FISTULA", "<b>AUDIBLE POP</b> then sudden loss + vertigo after STRAINING, DIVING or a BLOW. Round or oval window."],
  ["SYPHILIS", "<b>INDISTINGUISHABLE FROM M&Eacute;NI&Egrave;RE&rsquo;S</b> and TREATABLE. Order <b>FTA-ABS and MHA-TP</b>; <b>VDRL IS NOT HELPFUL</b>. Antibiotic + systemic steroid."],
  ["GLOMUS TUMOUR", "<b>PULSATILE TINNITUS</b> + vascular middle ear mass. Can paralyse CN IX, X, XI."],
  ["TINNITUS RED FLAG", "<b>UNILATERAL or PULSATILE</b> is investigated. No drug beats placebo; masking and biofeedback may help."],
 ]),
]

html = render(
    title="Clinical Medicine and Surgery I &middot; Exam 3 &mdash; Cram Sheet",
    kicker="PAJ 5500 &middot; Class of 2028",
    h1="Clinical Medicine and Surgery I &middot; Exam 3",
    sub="Ear, nose and throat block &mdash; Lectures 15 and 16, everything that has to be "
        "recallable cold",
    topics=topics,
    guide_href="cms-exam-3-study-guide.html",
    footer_note=("The study guide carries the reasoning; this is the night-before sheet. "
                 "Lectures 17 to 19 are added as they are delivered. Where a slide is incomplete "
                 "and the lecturer corrected it out loud, the correction is what is written."),
    primary="#6a4fa3")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB, %d sections, %d rows)"
      % (os.path.basename(OUT), len(html) // 1024, len(topics),
         sum(len(t["rows"]) for t in topics)))
