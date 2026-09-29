# -*- coding: utf-8 -*-
"""Lecture 26 scope -- Venous Disorders (Shah), CMS I Exam 5.

Read by cms_e5_partition.py (guards) and imported by every Lecture 26 pool.
Not a question bank: check_pool_cites does not glob it.

Built from the deck AND the 2026-09-29 recording (both clips, transcribed the same day; Prof. Shah).
The recording adds emphasis, never content the deck lacks (slides-only grounding), and where the
speech-to-text mangles a term ("workhouse triad" = Virchow triad) the deck's spelling wins.

WHAT SHAH EMPHASIZED (REQUIRED below weights these in every form):
  Virchow triad -- venous stasis, hypercoagulable state, endothelial trauma. "This is so important because
      these are big overarching categories" (said three times in a row). Jaxon's own steer the same day: she
      emphasized it heavily.
  Wells criteria for DVT -- "very familiar": outpatient / emergency department only; low likelihood -> D-dimer
      first, moderate (1-2) -> D-dimer, high (>= 3) -> skip the D-dimer and order the ultrasound. Jaxon: we need
      to know it. She also told the class the RISK FACTORS are what to know best ("the criteria come straight
      from there"). Immobilization in the score means bedridden after surgery or cast/plaster, NOT travel.
  D-dimer -- sensitive but nonspecific: positive means fibrinolysis somewhere, not necessarily a DVT.
  "Most common" facts she flagged: prior DVT is the most common cause of chronic venous insufficiency;
      family history is the most common predisposing factor for varicose veins; heavy, achy dull discomfort
      on standing is their most common symptom; factor V Leiden is the most common inherited
      hypercoagulable state; upper-extremity fistulas are the ones created for vascular access.
  Instructional objectives: "anytime you see these in the instructional objectives, your expectation is that
      you know everything about all of them" -- etiology through prognosis for all five conditions.

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 15, "Venous Disorders", read with PyMuPDF on
2026-09-29), with the syllabus's own broken numbering kept and only the leading "1." dropped. The syllabus
lists NO populations under its second objective; the deck's own slide 2 names adult and elderly, and the deck
has no infant, child or adolescent content, so IO_POP questions test only what the deck says about age.

EXCLUDED_SLIDES (never cited):
  4, 16-20, 22, 24-26   clinical photographs and image plates with no text (the guide reuses them)
  58                    the electrocardiogram slide: pulmonary embolism material ("more to come next week")
  59                    a picture with a one-line note
  87, 88, 89            references, "Case Studies", "Questions?"
  (21 and 23 carry a speaker note that describes stasis dermatitis and lipodermatosclerosis: citable.)

CONTESTED or outside the deck, so NEVER KEYED:
  Wells score of exactly 0: slide 55's note says "< 0" and its table says "0 or less"; stems use -1, 1, 2 or
      3 and above, never 0.
  How often PE and DVT co-occur (s48: ~50% of DVT patients have an occult PE, ~30% of PE patients have a
      DVT; audio agrees): the second figure is low against the literature. Never keyed. The site-of-DVT
      figures (s47: PE in up to 6% of upper-extremity vs 15-30% of lower-extremity DVT) are keyed.
  Any compression-stocking cutoff: s30's note says an ankle-brachial index under 0.7 rules them out, s28
      says 0.9 or less is peripheral artery disease, the audio says 25 to 30 mmHg (not on a slide).
      Only "rule out peripheral artery disease with an ankle-brachial index BEFORE compression" is keyed.
  Wound care visit frequency, and "lipodermatosclerosis is unilateral" (audio only), never keyed.
  The dabigatran/edoxaban "waning strategy" wording (s61) and the reversal-agent list (s68) are keyed as
      the slides give them, class first; never a brand name in a stem.
  Slide 27's medication list: "calcium channel blockers, NSAIDs, thiazolidinediones" stays a class list.
"""

DECK = "CMS I - Venous Disorders - Shah Fallsv UPDATED.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
        "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
        "referrals, patient education, and prognosis of the following venous disorders: 2. Deep vein "
        "thrombosis 3. Phlebitis a. Thrombophlebitis Septic thrombophlebitis 4. Arteriovenous fistula of "
        "the extremity a. Acquired (e.g. trauma, iatrogenic) b. Created (i.e. for hemodialysis) 5. Chronic "
        "venous insufficiency 6. Varicose veins")
IO_POP = ("Identify medical care strategies for venous disorders in the lecture topic list for the "
          "following populations.")
IOS = [IO_A, IO_POP]

EXCLUDED_SLIDES = {4, 16, 17, 18, 19, 20, 22, 24, 25, 26, 58, 59, 87, 88, 89}

SCOPE_BANNED = [
    r"\bscore (?:of |is |was )?(?:exactly )?(?:0|zero)\b", r"\b(?:0|zero) points?\b",
    r"\b(?:25|30)\s?(?:to|-)\s?(?:30|40)\s?mm\s?Hg\b", r"\bankle-brachial index[^?.;]{0,50}\b0\.7\b",
    r"\b30%[^?.;]{0,60}(?:pulmonary embol)[^?.;]{0,60}deep vein", r"deep vein[^?.;]{0,60}30%[^?.;]{0,60}pulmonary embol",
    r"S1Q3T3|inverted T wave in lead III",
    r"twice a week|three times a week|two to three times",
    r"\bDove\b|\bCetaphil\b|\bVaseline\b|\bAquaphor\b|\bLubriderm\b|\bAveeno\b|\bOlay\b|\bNeutrogena\b",
]

# Named findings in vignette stems carry their description in parentheses (taken from the deck).
NAMED = {
    "lipodermatosclerosis": "scar",             # s9/s23 note: skin and fat tissue scarring in the lower legs
    "hemosiderin": "brown",                     # s7/s14: brown or blue-gray discoloration from hemosiderin
    "homan": "dorsiflexion",                    # s51 note: calf pain on dorsiflexion of the foot
    "stasis dermatitis": "eczematous",          # s21 note: eczematous rash, erythema, scaling, weeping
    "baker": "popliteal",                       # s52: ruptured popliteal (Baker's) cyst
    "nicoladoni-branham": "heart rate",         # s85: slowing of the heart rate on compressing a large fistula
    "post-thrombotic": "chronic venous insufficiency",   # s52
    "thrill": "vibration",                      # s83: diffuse thrill and soft bruit -- palpable vibration
}

# The two things Shah stressed hardest, plus the D-dimer step that follows Wells: every form must carry them.
#            label                         stem regex                key regex   min per form
REQUIRED = [("Virchow triad",              r"virchow",               r".",       3),
            ("Wells criteria for DVT",     r"wells",                 r".",       3),
            ("D-dimer versus ultrasound",  r"d-dimer",               r".",       2)]
