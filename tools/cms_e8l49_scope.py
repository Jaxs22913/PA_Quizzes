# -*- coding: utf-8 -*-
"""Lecture 49 scope -- Hematologic Malignancies Part I (Gannon), CMS I Exam 8 (Hematology Block Exam, Monday
2026-11-30 10 AM, Lectures 46-51; Lecture 47, the AHEC smoking-cessation session, is not tested).

Read by cms_e8_partition.py (guards) and imported by every Lecture 49 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Nicole Gannon, PA-C, guest lecturer (Program Director of Mayo's Hematology/Oncology NP/PA fellowship,
slide 3). calendar-data.js lists Lecture 49 Wednesday 2026-11-18, 1-3 PM (2 hours), and Lecture 50 3-5 PM.
Deck file "49. Hematologic Malignancies Part I - Gannon.pptx", 67 slides; every slide was viewed at 1920 px (Keynote
PDF render). Slides 26 and 39 ("Management for PA Students ... Just kidding....") are pictures of full treatment
protocols shown as a joke: excluded, nothing keyed from them.

SYLLABUS vs DECK SPLIT. The syllabus (p. 22-23) splits the two lectures differently from the decks:
  syllabus "Hematological Malignancies 1": acute lymphocytic leukemia, acute myelogenous leukemia, lymphoma
    (Hodgkin, non-Hodgkin);
  syllabus "Hematologic Malignancies II": chronic lymphocytic leukemia, chronic myelogenous leukemia, polycythemia
    vera (primary, secondary), multiple myeloma, myelodysplasia.
  deck Part I (this lecture, slide 2 objectives): hematopoiesis + overview, ALL, AML, MDS, MPN, CML.
  deck Part II (Lecture 50): CLL, lymphoma (Hodgkin and non-Hodgkin), multiple myeloma and other plasma cell disorders.
Each question carries the syllabus objective that names its disease (IO_I or IO_II, verbatim); the overview items
carry IO_I. Secondary polycythemia (a syllabus item) is not on either deck: nothing keyed.

Overlap trap: CMS L46 (Ward, cytopenias), Clin Path L10 (blood disorders) and PD2 L7 (anemia) cover nearby blood
topics. These questions come from THIS deck only.

SLIDE CONFLICTS AND LOOSE SLIDES (slides win unless she corrected the slide out loud; memory truth_wins_on_conflict):
  s31 vs L50 s4/s6  s31 calls AML the "Most common form of leukemia, comprising 80% of all cases"; Lecture 50 s4
              calls CLL the "Most common adult form of leukemia" and s6 the "Most common leukemia in Western
              Hemisphere"; s58 gives CML "15-20% of all leukemias". The decks contradict each other: "most common
              leukemia" is never keyed for any leukemia.
  s62         chronic phase "<5%" blasts, accelerated "often 10-19%": no stem gives 5-9% blasts; no stem sits on a
              boundary (5, 10, 19, 20%).
  s64         milestone table (failure / warning / optimal / treatment-free remission by BCR-ABL1 level at 3, 6, 12 and
              >18 months): stems never sit on a boundary value (10%, 1%, 0.1%, 0.01%).
  s38         AML: "Historically ... myeloid blasts >= 20%, new guidelines note that certain genetic mutations may
              diagnosis with only 10% or higher": keyed as >= 20% (the definition), the 10% exception only as the slide
              words it.
  s61         names "CMML" with no expansion anywhere in the deck: CMML is never keyed or named.
  s21 vs s18  ALL ages: s21 "children under 5 and adults over age of 50"; s18 "most common malignancy under the age of
              15", adult peak "around 50". Keyed as each slide reads; no stem turns on age 5-15 alone.
  s28 vs s18  adult ALL survival: s28 "~40%" five-year overall survival; s18 "~30-40% ... long term remission". Neither
              number is keyed as a precise figure.
  s33         "myelokaryocytic" (megakaryocytic, as s32's M7 row reads); s36 "fused lysomes" (lysosomes); s48
              "allogenic"; s52 "Pruritis"; s54 "Willebrand" -- slide typos, questions use the correct spelling.
  s52         "call a friendly vampire, I mean phlebotomist": phlebotomy is keyed, not the joke.

RECORDING: Notability, four parts covering BOTH lectures (recordings/cms-l49-l50-heme-malignancies-gannon-2026-11-18-
part{1,2,3,4}); Lecture 49 = part 1 (51:47, slides 5-43, the tape misses slides 1-4) + part 2 (30:10, slides 44-66).
Two transcripts read and cross-examined: ours (faster-whisper medium.en) and Notability's own ASR (.notability.txt).
Flags file: recordings/cms-l49-heme-malignancies-i-gannon-2026-11-18.flags.md. No "this is on the test" sentence;
her cues are "write this down", "star, highlight, underline", "I want you to remember".
  Stressed out loud ([part m:ss]):
    s31/s36 Auer rods      [p1 33:10] "highlight, star, underline this ... pathognomonic for AML" (again 33:59)
    s25/s38 20% blasts     [p1 26:25] "This is important, write this down ... 20% or greater blast in the bone marrow"
                           (again 41:12; drilled against MDS [p2 5:09-5:31]: "20%? That's leukemia")
    s20 BCR-ABL            [p1 17:55] "star, highlight, underline"; [p1 19:21] "chromosome nine and 22 ... Write it down"
    s15 Reed-Sternberg     [p1 12:29] "if you're ever taking a test and you see a Reed Sternberg cell ... Hodgkin lymphoma"
    s15 B symptoms         [p1 13:12] "make sure you're writing down what are B symptoms"
    s5 hematopoiesis       [p1 1:08] "cannot emphasize enough, learn this"
    s23 lumbar puncture    [p1 24:12] "Lumbar punctures is kind of the big one I would want you to remember"
    s43 APL                [p1 51:22] "the thing I want you to remember about APL: bleeding, DIC, coagulopathy, and that it
                           does not need chemotherapy. ATRA and arsenic"
    s36 work-up            [p1 41:06] "bone marrow and flow cytometry are your backbone testing"
    s52 JAK2               [p2 10:17] "you may come across this on your testing"
  De-emphasized: s11 flow markers ("You don't have to know all that"), s26 protocol ("not expected to memorize"),
    s33 FAB M0-M7 ("You don't have to know anything about this, really, except ... APL"), s38 subgroup modifiers
    ("don't worry about that"), s52 platelets in PV ("probably won't be on your test"), s63 TKI side effects, s8
    epidemiology numbers. Slides 37 and 61 (differentials) barely taught.
  Audio vs slide (she never called a slide wrong; the slide is keyed, the point left unkeyed where they differ):
    s62 chronic phase "<5%" vs "five to 6% ... chronic phase" [p2 21:58]: no stem gives 5-9% blasts;
    s62/s63 accelerated phase "treat this the same way" [p2 22:32] vs s63 "different considerations": accelerated-phase
      treatment never keyed; blast phase ">20%" [p2 22:45] is not on the slide: no blast-phase number keyed;
    s63 treatment-free remission "MMR for 2 years" vs "three years ... two years of deep molecular remission" and "five
      years": no duration keyed;
    s18/s28 ALL survival ">95%" vs ">90%": no precise figure keyed;
    s22 ">50% present w/ lymphadenopathy" vs "in clinical practice I don't see a lot": lymphadenopathy share not keyed;
    s49 very high-risk MDS "median OS of 9 months" (slide) vs "nine months, and it's gonna develop into leukemia": slide.
  Minutes taught per topic: TOPIC_MINUTES below.

Deliberately NOT keyed: any dose or schedule (s26 and s39 protocols, "7+3" is named only as the slide names the
regimen), the six tyrosine kinase inhibitor names (the deck names none), FAB subtype numbers beyond what s32-33 say,
epidemiology percentages on s8 (case counts, deaths), the s6 source journal, brand names.
"""

DECK = "49. Hematologic Malignancies Part I - Gannon.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

# Syllabus objectives (CMS syllabus p. 22-23), verbatim as printed (the population list of Hematological Malignancies
# 1 prints "Infant" at the end of item 6's line and then letters a-d; kept as printed).
IO_I = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis of the following hematological malignancies: 1. Acute lymphocytic leukemia 2. Acute myelogenous "
        "leukemia 3. Lymphoma 4. Hodgkin 5. Non-Hodgkin")
IO_I_POP = ("Identify medical care strategies for disorders of hematological malignancies in the lecture topic list "
            "for the following populations. Infant a. child b. adolescent c. adult d. elderly")
IO_II = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
         "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
         "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
         "prognosis of the following hematological malignancies: 1. Chronic lymphocytic leukemia 2. Chronic "
         "myelogenous leukemia 3. Polycythemia vera a. primary b. secondary 4. Multiple myeloma 5. Myelodysplasia "
         "(myelodysplastic syndromes)")
IO_II_POP = ("Identify medical care strategies for disorders of hematological malignancies in the lecture topic list "
             "for the following populations. a. infant b. child c. adolescent d. adult e. elderly")
IOS = [IO_I, IO_I_POP, IO_II, IO_II_POP]

# Topic names the pools use (quiz chips) and their slide ranges.
T_OVERVIEW = "Hematopoiesis and the malignancy families"
T_FITNESS = "Performance status, work-up and transplant terms"
T_ALL_PATH = "Acute lymphoblastic leukemia: who and why"
T_ALL_DX = "Acute lymphoblastic leukemia: presentation and diagnosis"
T_ALL_TX = "Acute lymphoblastic leukemia: management and prognosis"
T_AML_PATH = "Acute myeloid leukemia: who and why"
T_AML_DX = "Acute myeloid leukemia: presentation and diagnosis"
T_AML_TX = "Acute myeloid leukemia: management and prognosis"
T_APL = "Acute promyelocytic leukemia"
T_MDS = "Myelodysplastic syndrome"
T_PV = "Polycythemia vera"
T_MF = "Myelofibrosis"
T_ET = "Essential thrombocythemia"
T_CML_PATH = "Chronic myelogenous leukemia: who and why"
T_CML_DX = "Chronic myelogenous leukemia: presentation, diagnosis and phases"
T_CML_TX = "Chronic myelogenous leukemia: management and prognosis"

TOPIC_SLIDES = {
    T_OVERVIEW: (5, 16),      # s5 hematopoiesis, s6 clonality, s7 definition, s8 epidemiology, s9 risk factors, s14-16 families
    T_FITNESS: (10, 12),      # s10 ECOG table, s11 presentation and work-up, s12 transplant terms
    T_ALL_PATH: (18, 21),
    T_ALL_DX: (22, 25),
    T_ALL_TX: (27, 29),
    T_AML_PATH: (31, 34),
    T_AML_DX: (35, 38),
    T_AML_TX: (40, 42),
    T_APL: (43, 43),
    T_MDS: (45, 49),
    T_PV: (51, 52),
    T_MF: (53, 53),
    T_ET: (54, 54),
    T_CML_PATH: (56, 58),
    T_CML_DX: (59, 62),
    T_CML_TX: (63, 66),
}

# Title, objective, disclosure and divider slides, the two "Just kidding" protocol pictures, the closing meme.
EXCLUDED_SLIDES = {1, 2, 3, 4, 13, 17, 26, 30, 39, 44, 50, 55, 67}

SCOPE_BANNED = [
    r"most common (?:form of |adult form of |type of )?leukemia",   # s31 vs Lecture 50 s4/s6 conflict
    r"\bCMML\b|chronic myelomonocytic",                             # s61 never expands it
    r"7 ?\+ ?3 regimen.{0,40}day|days? of cytarabine",              # no schedules
    r"MDedge|ascopubs|bloodcancerunited|icahn|Cleveland Clinic|Mayo Foundation",   # sources on the pictures
    r"\bimatinib|dasatinib|nilotinib|bosutinib|ponatinib|asciminib",  # TKIs the deck never names
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "auer rod": "fused",                    # s36: Auer rods (fused lysosomes)
    "philadelphia chromosome": "9",         # s20/s56/s57: translocation of chromosomes 9 and 22
    "b-symptom": "sweats",                  # s22/s35/s59: weight loss, fever, night sweats
    "b symptom": "sweats",
    "petechiae": "",                        # described on s22 as bruising; no gloss forced
}
NAMED = {k: v for k, v in NAMED.items() if v}

# Minutes taught per pool topic: filled from the recording (see RECORDING); weights the forms.
TOPIC_MINUTES = {
    T_OVERVIEW: 10.5,    # p1 0-5.4 (s5-9) + 10.4-15.5 (s14-16)
    T_FITNESS: 4.3,      # p1 5.4-10.3 less biopsy anecdotes
    T_ALL_PATH: 4.7,     # p1 15.6-20.3
    T_ALL_DX: 6.3,       # p1 20.3-27.0
    T_ALL_TX: 4.2,       # p1 27.0-30.2 + part of the Q&A
    T_AML_PATH: 5.7,     # p1 32.9-39.7 less a patient story
    T_AML_DX: 1.8,       # p1 39.7-41.5
    T_AML_TX: 7.7,       # p1 41.5-49.7 (incl. Q&A on intensity)
    T_APL: 1.9,          # p1 49.7-51.5
    T_MDS: 7.7,          # p2 0-8.2
    T_PV: 5.4,           # p2 8.3-13.7 (s51 overview + s52)
    T_MF: 1.9,           # p2 13.7-15.6
    T_ET: 1.7,           # p2 15.7-17.4
    T_CML_PATH: 2.7,     # p2 17.5-20.2
    T_CML_DX: 5.4,       # p2 20.2-23.8 + part of the blasts Q&A
    T_CML_TX: 2.5,       # p2 27.4-29.8
}

# (label, stem regex, key regex, minimum per form). The pool must hold at least twice the minimum of each.
REQUIRED_IO = []
REQUIRED_VIG = [
    # s10: ECOG performance status grade read from the stem's description of the patient's day
    ("ECOG grade from the vignette", r"Eastern Cooperative Oncology Group|performance status",
     r"\b[0-5]\b|grade", 1),
    # s62 / s64: CML phase from the blast percentage, or the milestone response from the BCR-ABL1 level
    ("CML phase or milestone from the numbers", r"blasts|BCR-ABL1",
     r"chronic|accelerated|blast|optimal|warning|failure|treatment-free", 1),
]

# Review holds (stem prefixes): flagged again by the audit after their one repair. The partition skips them.
HELD = []
