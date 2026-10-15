# -*- coding: utf-8 -*-
"""Lecture 31 scope -- Pericardial Disease (Reynolds), CMS I Exam 5.

Read by cms_e5_partition.py (guards) and imported by every Lecture 31 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Lauren Reynolds, MSPA, PA-C -- title slide ("Modified and Presented by"), and the 2026-10-14
recording (Notability, three clips, 108.5 min): the speaker announces "next lecture at one o'clock ...
infective endocarditis", which is Lecture 32, "Presented by Professor L. Reynolds". Agrees with
calendar-data.js. No conflict.

Built from the DECK; the recording only sets emphasis and scope (slides-only grounding). Two slides carry
their content in SmartArt graphic frames that neither the text extractor nor the slide renderer shows: s14
(diagnosis is clinical; two of four criteria -- sharp substernal chest pain, pericardial friction rub,
widespread ST elevation, new or worsening effusion) and s30 (no response to a nonsteroidal anti-inflammatory
drug plus colchicine within 1 week suggests another cause; what treatment failure means). Both are cited.

AUDIO SCOPE REMARKS (Notability transcript; ours still to come):
  Doses: "please don't memorize doses. Just know the meds ... the names" -- no dose is ever keyed (the
      partition's dose guard enforces it); the s29 table is used for drug ORDER and names only.
  s29 fourth-line row: "I want you to cross off fourth line therapy ... that is not entirely accurate
      anymore" -- anakinra/rilonacept are keyed per s35 (2025 guidance), never as fourth line.
  Tamponade: "I'm not gonna ask you to name a pressor ... the fluid bolus rate", but stabilize (fluids,
      pressors) until pericardiocentesis -- no pressor name or rate is keyed.
  No item was announced as "on the exam", so REQUIRED is empty.

EMPHASIS (minutes, Notability segment timing): definitions/epidemiology ~12, etiology ~20, acute diagnosis
  ~20 (friction rub twice, "beat this into you"; two-of-four criteria; ST elevation everywhere with reciprocal
  aVR depression), acute treatment/recurrence/counseling ~12 (aspirin not other NSAIDs after myocardial
  infarction; heart rate under 100; GI protection; anti-interleukin-1 earlier), populations and consults ~6,
  constrictive ~15 (calcification "slam dunk" but absence does not exclude), effusion and tamponade ~22
  (emergency, Beck triad "classic" but rarely complete, clinical diagnosis confirmed by drainage).

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 17, "Pericardial Disease", read with PyMuPDF on
2026-10-15), the syllabus's own broken numbering kept and only the leading "1." / "8." dropped, as L26-L28 do.

EXCLUDED_SLIDES (never cited):
  1, 2          title, references
  10, 38        section title slides with nothing else
  18            embedded YouTube video only (pressure tracings poster frame)
  37            personal photograph (decoration)
  51            audio clip ("Under Pressure") on a section title
  72            scanned textbook page (Medicine at a Glance); it files the Kussmaul sign under TAMPONADE.
                Every other fact on it is on a deck slide, so nothing is lost.

CONTESTED or WRONG on the slides, so NEVER KEYED the contested way (truth wins; the guide notes each):
  s11 lists "HIB" among VIRAL causes -- Haemophilus influenzae type b is a bacterium (s11 also lists
      Haemophilus under bacterial). Never keyed as viral; the bare "HIB" is banned.
  s39 "pericardial knock (mid-frequency heart sound ...)" -- it is a high-pitched early diastolic sound.
      Keyed only as "slightly earlier than a third heart sound".
  s44 lists pulsus paradoxus among the CONSTRICTION exam findings -- pulsus paradoxus is the hallmark of
      tamponade and appears in only a minority of constriction. Never keyed as a constriction
      discriminator; the Kussmaul sign is.
  s72 (excluded) lists the Kussmaul sign under tamponade -- it belongs to constriction. Never keyed.
  s29 "fourth-line" anakinra/rilonacept -- the lecturer struck it; s35's 2025 guidance is keyed:
      anti-interleukin-1 therapy preferred over corticosteroids for recurrent, colchicine-resistant or
      steroid-dependent disease with an inflammatory phenotype (C-reactive protein over 10 mg/L, fever,
      pericardial inflammation on imaging).
  ECG stage DURATIONS: s22 says stage 1 lasts "the first two weeks", the s23 picture says "< 1 week". Stage
      ORDER is keyed; no stage duration ever is.
  s71 calls echocardiography the "gold standard" for tamponade; s57 (and the lecturer: "your treatment confirms
      your diagnosis") says tamponade is a clinical diagnosis confirmed only by the response to drainage.
      Keyed per s57; echo is keyed as confirming an EFFUSION and showing right ventricular diastolic collapse.
  s7 constrictive pericarditis "<0.05% of pts w/ viral pericarditis" -- the literature figure is well under
      1% but larger than this; the number is never keyed, only "uncommon after viral pericarditis".
  s17 "pleural rubs can only be heard during inspiratory phase" overstates it (a pleural rub can span the
      respiratory cycle); keyed as the robust discriminator both deck and truth support: a pleural rub is tied
      to breathing and stops when the breath is held, while the pericardial rub persists.
  s8 files post-cardiotomy pericarditis under "Dressler syndrome" (strictly, post-pericardiotomy syndrome).
      The "no NSAIDs, use aspirin" rule (s28, s29 footnote) is for POST-INFARCTION pericarditis only, so every
      drug-choice vignette is set after a myocardial infarction, never after cardiac surgery alone.
  Audio misstatement (seg 2 ~29 min): "electrical alternans and pulsus paradoxus and Kussmaul's, that's the
      triad, Beck triad" -- Beck triad is hypotension, distended jugular veins and muffled heart sounds (s54).
      Keyed per the slide.
"""

DECK = "31. Pericardial Disease 2026.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
        "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
        "referrals, patient education, and prognosis of the following pericardial disease: 2. Pericarditis "
        "3. Acute 4. Recurrent 5. Constrictive pericarditis 6. Pericardial effusion 7. Cardiac tamponade")
IO_POP = ("Identify medical care strategies for pericardial disease in the lecture topic list for the "
          "following populations. 9. adult 10. elderly")
IOS = [IO_A, IO_POP]

EXCLUDED_SLIDES = {1, 2, 10, 18, 37, 38, 51, 72}

SCOPE_BANNED = [
    r"\bHIB\b",
    r"\bviral\b[^?.;]{0,60}Haemophilus|Haemophilus[^?.;]{0,60}\bvir(?:us|al)\b",
    r"mid-frequency",
    r"gold standard",
    r"fourth[- ]line",
    r"stage (?:1|2|3|4|one|two|three|four)\b[^?.;]{0,80}\bweeks?\b",
    r"<\s?0\.05|less than 0\.05",
    r"norepinephrine|vasopressin|dopamine|phenylephrine|bolus rate|mL/kg",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "friction rub": "scratch",                 # s17: superficial scratchy or squeaking
    "kussmaul": "inspiration",                 # s39: rises during inspiration rather than falling
    "pulsus paradoxus": "systolic",            # s59 notes: >10 mmHg fall in systolic pressure on inspiration
    "pericardial knock": "earlier",            # s39: slightly earlier than a third heart sound
    "electrical alternans": "alternat",        # s60: QRS amplitude alternates
    "beck": "muffled",                         # s54
    "water bottle": "globular",                # s65
    "water-bottle": "globular",
    "low voltage": "small",                    # s45 / s60
    "pleuritic": "breath",                     # s13: sharp, worse on inspiration
    "anasarca": "generalized",                 # s39
    "cachexia": "wasting",                     # s44
    "third heart sound": "early diastol",
    "swinging": "fluid",                       # s63: heart swinging in the effusion
}
