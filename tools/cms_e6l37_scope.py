# -*- coding: utf-8 -*-
"""Lecture 37 scope -- Respiratory Infections and Vaccines Preventing Respiratory Infections (Bobilin), CMS I
Exam 6 (Respiratory Block Exam I, 2026-11-06, Lectures 33-38).

Read by cms_e6_partition.py (guards) and imported by every Lecture 37 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Robert Bobilin, MS, MPAS, PA-C, guest lecturer -- title slide, and the 2026-10-29 Zoom recording
(one file covering Lectures 37 and 38; Lecture 37 runs 0:00 to the break at 2:53:43). calendar-data.js lists
"CMS I - LECTURE #37 - Respiratory Infections and Vaccines Preventing Respiration Infections - Professor
Bobilin GUEST LECTURER", 1-4 PM (3 hours). No conflict. Deck file "37. Respiratory Infections - Bobilin -
10-29-2026 SV.pptx", 131 slides.

Built from the DECK; the recording only sets emphasis and scope (slides-only grounding).

AUDIO SCOPE REMARKS (Zoom transcript, speaker-labelled; ours is the second opinion):
  He writes the exam items himself: "I'm going to finish writing all my questions and try to have them in to
      Professor Jaquith by tomorrow, or at the latest, this weekend, and I will give you all some guidance"
      [0:02:31]; at the end of Lecture 38 he repeats that he will post guidance for both lectures "this
      weekend ... at the end of this PowerPoint" [4:00:15]. Not on disk on 2026-10-30.
  He also says the posted deck had "a few typos and grammatical changes ... not anything that's dramatic"
      [0:02:46]: a revised deck may follow.
  Vaccines: "I'm not going to require a lot of detail on the exam, and if I require anything specific, I will
      give you some guidelines on it" [0:22:53] -- vaccine items stay at the level of the summary slide (s124):
      who gets which vaccine and when; no product-interval minutiae (s9 8-week intervals, PneumoRecs, s12).
  Pneumonia stages: "These aren't cold, hard, fast rules ... don't want to get too caught up" [0:44:24] --
      at most the order of the four stages; day ranges never keyed.
  Chest radiographs: "Don't worry, I'm not going to put these on the exam and say, what is it" [0:59:35] --
      slides 32, 34, 35, 36, 52, 55 (example films) are EXCLUDED; the s33 classification table stays.
  Pneumocystis steroids: the alveolar-arterial gradient "is not going to show up on a test" [1:56:33] -- the
      steroid trigger is keyed only by the room-air arterial oxygen below 70 mm Hg.
  Histoplasmosis: "another one of those things that's going to show up on your PANCE exam" [1:59:21].
  Psittacosis: "a super common medical boards question ... Not common enough to really deserve a lot of
      attention" [2:04:03].
  Influenza vaccine valency: "won't show up on a test" [2:25:38] -- the trivalent composition is not keyed.
  PSI vs CURB-65: "the PSI is what's being used, more than not, and the CURB-65 is simply complementary"
      [0:56:12] -- matches s31.

EMPHASIS (minutes, Zoom timestamps, breaks removed): intro ~4, vaccines ~16 (de-emphasized out loud),
  acute bronchitis ~14, pneumonia overview/types/stages/presentation/workup/severity scores/antibiotics/HAP-VAP
  ~46, aspiration ~6, lung abscess ~4, Pneumocystis ~12, histoplasmosis ~5, psittacosis ~13, Mycoplasma ~2,
  influenza ~15, COVID-19 ~9, cryptococcosis ~2, closing decision slides 124-126 ~5.

SLIDE CONFLICTS (never keyed; the guide notes each):
  s100 lists "Nasal discharge" among influenza symptoms; s102 says "Nasal discharge is absent in most
      patients" on examination. In the recording he corrects his own "not as much congestion" to "there is
      congestion" [2:30:46]. Nasal discharge is never keyed for influenza.
  s92 "three basic types A, B or C" and "trivalent vaccines ... H3N2 and H1N1 and influenza B"; he calls the
      vaccine "basically tetravalent" but says it won't be tested. Not keyed.
  s30 PSI picture is a cropped calculator: the item list stops at "Arterial pH <7.35 (30 points)" and the
      interpretation table gives Class I no point range. PSI totals are keyed only as a given total -> class
      (51-70 II, 71-90 III, 91-130 IV, 131-395 V); no item asks for a PSI total from a vignette.
  s45 severe CAP: the minor criteria are never listed on the slides -- items use only the two major
      criteria (vasopressor-dependent shock, mechanical ventilation) or say "three minor criteria" outright.
  s41 (table) puts Blastomyces at the Mississippi and Ohio River basins; s75 puts Histoplasma in the Ohio and
      Mississippi River valleys. Both are on the slides; geography alone never decides between them.

SPEAKER NOTES ARE NOT SLIDE CONTENT (Jaxon, 2026-10-15).

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 18, "Respiratory Infections and Vaccines
Preventing Respiratory Infections"), the leading letters dropped and the sub-list numbering kept, as Lecture
36 does. The syllabus spelling "pneumocystis jiroveccii" is quoted as written.

EXCLUDED_SLIDES (never cited):
  1, 2              title, objectives
  14                picture only (inflamed bronchi)
  32, 34, 35, 36    example chest films ("not going to put these on the exam")
  52, 55            example aspiration and abscess films
  57, 74, 79, 90, 111   section title slides
  118               COVID-19 radiograph panel (no text)
  127-131           questions, references
"""

DECK = "37. Respiratory Infections - Bobilin - 10-29-2026 SV.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

IO_VAX = "Identify and discuss vaccines which prevent respiratory infections."
IO_B = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis of the following respiratory infections: 1. Acute bronchitis 2. Pneumonia: 3. Bacterial "
        "4. Viral 5. Atypical (including but not limited to chlamydia psittacosis and mycoplasma) 6. Fungal "
        "(including but not limited to cryptococcosis, histoplasmosis, pneumocystis jiroveccii) 7. Aspiration "
        "pneumonia 8. Lung abscess 9. Influenza 10. Coronavirus (COVID-19)")
IO_POP = ("Identify medical care strategies for respiratory infections in the lecture topic list for the following "
          "populations. 1. adult 2. elderly")
IOS = [IO_VAX, IO_B, IO_POP]

EXCLUDED_SLIDES = {1, 2, 14, 32, 34, 35, 36, 52, 55, 57, 74, 79, 90, 111, 118, 127, 128, 129, 130, 131}

SCOPE_BANNED = [
    r"24\.8|250,000|3,000-49,000|3-5 million|88%|70%-80%|70 ?- ?80%|80% of infants|3000 cases|100 outbreaks",
    r"PneumoRecs|cochlear|CSF leak|cerebrospinal fluid leak|8-week",
    r"\btrivalent\b|\btetravalent\b|Victoria|H1N1|H3N2",
    r"alveolar-arterial|A-a gradient|A–a",
    r"\bred hepatization\b.*\bdays?\b|\bdays? 2-3\b|\bdays? 3-6\b|\bdays? 8-10\b",
    r"bulging fissure",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "horder spots": "rose spots",          # s83: macular rashes like typhoid rose spots, but on the face
    "amphoric": "jar",                     # s53: like breathing across an open jar
    "egophony": "E to A",                  # s23: egophony (E to A)
    "reye syndrome": "aspirin",            # s110: aspirin in children is associated with Reye syndrome
}

# Content the slides make a score item out of: every vignette form carries at least one CURB-65 total.
REQUIRED = [
    ("CURB-65 total", r"CURB-65", r".", 1),
]
