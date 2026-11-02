# -*- coding: utf-8 -*-
"""Lecture 40 scope -- Obstructive Sleep Apnea and Obesity Hypoventilation Syndrome (Shah), CMS I Exam 7
(Respiratory Block Exam II, Monday 2026-11-16, Lectures 39-45).

Read by cms_e7_partition.py (guards) and imported by every Lecture 40 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Chand Shah, MPAS, PA-C, Assistant Professor -- title slide. calendar-data.js lists "CMS I - LECTURE
#40 - Obstructive Sleep Apnea and Obesity Hypoventilation Syndrome - Professor Shah", Monday 2026-11-02,
11 AM-12 PM (1 hour). No conflict. Deck file "CMS I Obstructive Sleep Apnea & Obesity Hypoventilation Syndrome -
Shah Fallsv.pptx", 38 slides.

PHASE 1 (2026-11-02) = SLIDES ONLY. The live recording is not in yet; when it arrives it sets emphasis and scope.

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 19, "Obstructive Sleep Apnea and Obesity
Hypoventilation Syndrome"), the leading letters dropped and the sub-list lettering kept (the syllabus prints a
stray empty "a." before the disease list; it is left out). The deck's objectives slide (s2) adds three of its
own ("Explain why obesity hypoventilation syndrome is a diagnosis of exclusion", "Discuss central sleep apnea as
a differential diagnosis for obstructive sleep apnea", "Discuss STOP-Bang questionnaire as a screening tool");
they sit inside the syllabus objectives and the guide answers them there.

THE STOP-BANG PICTURE (s17) is the whole questionnaire as an image: S snore loudly; T tired, fatigued or sleepy
in the daytime; O observed to stop breathing or choking/gasping; P being treated for high blood pressure;
B body mass index more than 35 kg/m2; A age older than 50; N neck size (shirt collar) 16 inches / 40 cm or
larger; G gender male. General population: low risk yes to 0-2, intermediate 3-4, high 5-8; OR yes to 2 or more
of the 4 STOP questions + male gender, + body mass index > 35, or + neck circumference 16 inches / 40 cm.
STOP-Bang totals are keyed from a vignette (Jaxon: the real exam asks "what is the score from the vignette").

SLIDE CONFLICTS (never keyed one way or the other; the guide notes each):
  Neck size: s6 and s7 give the OSA risk-factor neck circumference by sex (>= 17 in men, 16 in women; s7 writes
      ">17in"); the STOP-Bang item (s17) is 16 inches / 40 cm for anyone. A neck-size item says which tool it
      uses; a STOP-Bang item scores the neck at 16 inches regardless of sex.
  Body mass index: STOP-Bang counts > 35 kg/m2 (s17); obesity for obesity hypoventilation syndrome is > 30 (s30,
      s32). Each is keyed only inside its own tool.
  Sex: s6 "Male > women" (OSA); s5 post-menopausal women have more sleep-disordered breathing than premenopausal;
      s29 "Male gender is not a risk factor" (OHS); s30 the sleep-hypoventilation subgroup is "Older females".
  "Gold standard": s8 calls BOTH the split-night and the all-night polysomnogram the gold standard; s32 calls
      polysomnography with continuous nocturnal carbon dioxide monitoring the gold standard for obesity
      hypoventilation syndrome. Never ask split-night versus all-night as "the" gold standard.
  s21 lists both "Increased sympathetic tone" and "Bradycardia" as cardiovascular effects: both are keyable as
      listed; never ask for the heart-rate direction alone.

SPEAKER NOTES ARE NOT SLIDE CONTENT (Jaxon, 2026-10-15): the s9 note (AHI 5 mild / 15 moderate / 30 severe), the
s10 note (central sleep apnea detail), the s12 and s14 notes (CPAP versus BiPAP), the s6 note (micrognathia and
retrognathia definitions) are never used. OSA SEVERITY CATEGORIES BY INDEX ARE NOT ON A SLIDE: never key
mild/moderate/severe from an apnea-hypopnea index number.

EXCLUDED_SLIDES (never cited):
  1, 2            title, objectives
  4, 23, 27       section title slides
  14              three photographs of positive airway pressure devices, no text
  36              "Case Studies" title, no content
  37, 38          resources, questions
"""

DECK = "CMS I Obstructive Sleep Apnea & Obesity Hypoventilation Syndrome - Shah Fallsv.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis for obstructive sleep apnea and obesity hypoventilation syndrome: a. Obstructive sleep apnea "
        "b. Central sleep apnea c. Obesity hypoventilation syndrome (also known as Pickwickian Syndrome)")
IO_SCREEN = "Discuss screening tools for obstructive sleep apnea"
IO_COMP = ("Discuss the following complications of untreated obstructive sleep apnea and comorbidities of "
           "obstructive sleep apnea, including: a. Atrial fibrillation and cardiac arrythmias b. Pulmonary "
           "hypertension and right heart failure c. Heart failure d. Systemic hypertension e. Coronary artery "
           "disease f. Type 2 diabetes mellitus and metabolic syndrome g. Nonalcoholic fatty liver disease")
IO_POP = ("Identify medical care strategies for obstructive sleep apnea and obesity hypoventilation syndrome for "
          "the following populations. 1. adult 2. elderly")
IOS = [IO_A, IO_SCREEN, IO_COMP, IO_POP]

EXCLUDED_SLIDES = {1, 2, 4, 14, 23, 27, 36, 37, 38}

SCOPE_BANNED = [
    r"\b30 (?:or more )?(?:events|per hour)|severe (?:obstructive sleep apnea|OSA) (?:is|=|means) ",
    r"Lecturio|UpToDate|Pasha|Guyton",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "facial plethora": "swelling",        # s31: facial plethora (facial swelling, puffiness)
    "cheyne-stokes": "alternating",       # s24: hyperventilation alternating with apnea
}

# Every form carries at least one STOP-Bang total worked from the stem (s17).
REQUIRED = [
    ("STOP-Bang total", r"STOP-Bang", r".", 1),
]
