# -*- coding: utf-8 -*-
"""Lecture 50 scope -- Hematologic Malignancies Part II (Gannon), CMS I Exam 8 (Hematology Block Exam, Monday
2026-11-30 10 AM, Lectures 46-51; Lecture 47 is not tested).

Read by cms_e8_partition.py (guards) and imported by every Lecture 50 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Nicole Gannon, PA-C, guest lecturer. calendar-data.js lists Lecture 50 Wednesday 2026-11-18, 3-5 PM
(2 hours), straight after Lecture 49 (Part I). Deck file "50. Hematologic Malignancies Part II - Gannon.pptx",
58 slides; every slide was viewed at 1920 px (Keynote PDF render). Slide 58 is a cartoon (excluded).

SYLLABUS vs DECK SPLIT: see the Lecture 49 scope docstring. This deck teaches CLL (syllabus II), lymphoma Hodgkin and
non-Hodgkin (syllabus I) and multiple myeloma with the other plasma cell disorders (syllabus II). Each question
carries the syllabus objective that names its disease, verbatim.

Overlap trap: CMS L46 (Ward), Clin Path L10 and PD2 L7 cover nearby blood topics; Lecture 49 covers the acute
leukemias, MDS, MPN and CML. These questions come from THIS deck only.

SLIDE CONFLICTS AND LOOSE SLIDES (slides win unless she corrected the slide out loud):
  s4/s6 vs L49 s31  CLL "Most common adult form of leukemia" (s4) and "Most common leukemia in Western Hemisphere" (s6)
              against Lecture 49's AML "Most common form of leukemia, comprising 80% of all cases". Never keyed.
  s41         titled "Management of NHL" but teaches Hodgkin lymphoma (stage I and IIA, bulky, ABVD): keyed as Hodgkin
              management (the slide sits in the Hodgkin section, s35-42). "Decarbazine" = dacarbazine; "Adriamycin"
              is the brand of doxorubicin: questions say doxorubicin (Adriamycin is scope-banned as a brand).
  s47 vs s57  the s47 SLiM picture reads ">= Sixty (60%)" bone marrow plasma cells; s57 smoldering myeloma
              "10-60%". A smoldering stem stays well inside 10-60%; no stem sits at 60%.
  s57         smoldering myeloma "M-protein > 3 g/dl AND 10-60% bone marrow plasma cells" (the AND is the slide's): a
              smoldering stem gives BOTH an M-protein above 3 g/dL and plasma cells inside 10-60%, so the item holds
              under either reading.
  s56/s57     MGUS M-protein "< 3 g/dl", smoldering "> 3 g/dl": no stem gives exactly 3 g/dL or exactly 10%.
  s50 vs s51  s50 "Serum beta-2 macroglobulin"; s51's R-ISS table "beta2-microglobulin": questions say beta-2
              microglobulin.
  s8 vs s9    CLL "ALC > 5K x 3 months or ALC < 5K with lymphadenopathy or other symptoms" (s8) and monoclonal B
              lymphocytosis "Elevated ALC but <5K ... with absence of lymphadenopathy, organomegaly, cytopenias" (s9):
              stems never sit at exactly 5,000.
  s10         Rai picture: stage II reads "Lymphocytosis, lymphadenopathy, organomegaly*" (*hepatomegaly and/or
              splenomegaly); keyed as the table reads.
  s26/s40     the staging picture is titled "Stages of Non-Hodgkin's Lymphoma" and is reused for Hodgkin (s40):
              stages 1-4 keyed as the picture captions read for both.
  s38         Hodgkin "painless asymptomatic lymphadenopathy (70%)" and "Pain may worsen with alcohol consumption":
              keyed as the slide reads (node pain with alcohol).
  s9 "harry cell" (hairy cell), s21 "Hodkin", s22/s24/s38 "Pruritis", s53 "proteosome", s42 "may required":
              slide typos; questions use the correct spelling.
  s25         "Reserve for significant enlargement (2 cm)": keyed as the slide reads.

RECORDING: see RECORDING below (filled after the transcripts are read).

Deliberately NOT keyed: doses and cycle schedules, CLL-IPI items (named on s10 but not shown), CAR-T and bispecific
details, the cytogenetic list of R-ISS beyond the slide's table, survival months on s51 as exact numbers, brand names.
"""

DECK = "50. Hematologic Malignancies Part II - Gannon.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

# Syllabus objectives (CMS syllabus p. 22-23), verbatim (see the Lecture 49 scope).
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

T_CLL = "Chronic lymphocytic leukemia: who and why"
T_CLL_DX = "Chronic lymphocytic leukemia: presentation and diagnosis"
T_CLL_STAGE = "Chronic lymphocytic leukemia: Rai staging"
T_CLL_TX = "Chronic lymphocytic leukemia: management and prognosis"
T_NHL_INDOLENT = "Non-Hodgkin lymphoma: definition and indolent types"
T_NHL_AGGR = "Non-Hodgkin lymphoma: aggressive and T-cell types"
T_NHL_DX = "Non-Hodgkin lymphoma: risk, presentation, work-up and staging"
T_NHL_TX = "Non-Hodgkin lymphoma: treatment, tumor lysis and prognosis"
T_BURKITT = "Burkitt lymphoma"
T_HL = "Hodgkin lymphoma: who, presentation and diagnosis"
T_HL_TX = "Hodgkin lymphoma: management and prognosis"
T_MM = "Multiple myeloma: pathogenesis, risk and CRAB"
T_MM_DX = "Multiple myeloma: diagnosis and staging"
T_MM_TX = "Multiple myeloma: management and prognosis"
T_MGUS = "MGUS and smoldering myeloma"

TOPIC_SLIDES = {
    T_CLL: (4, 6),
    T_CLL_DX: (7, 9),
    T_CLL_STAGE: (10, 10),
    T_CLL_TX: (11, 13),
    T_NHL_INDOLENT: (15, 18),
    T_NHL_AGGR: (19, 22),
    T_NHL_DX: (23, 26),
    T_NHL_TX: (27, 30),       # plus s34 patient education
    T_BURKITT: (31, 33),
    T_HL: (36, 40),
    T_HL_TX: (41, 42),
    T_MM: (44, 48),
    T_MM_DX: (49, 51),
    T_MM_TX: (52, 55),
    T_MGUS: (56, 57),
}

EXCLUDED_SLIDES = {1, 2, 3, 14, 35, 43, 58}

SCOPE_BANNED = [
    r"most common (?:form of |adult form of |type of )?leukemia",   # s4/s6 vs Lecture 49 s31
    r"Adriamycin",                                                   # brand of doxorubicin (s41)
    r"CLL-IPI|International Prognostic Index",                       # named on s10 but its items are not shown
    r"WebPathology|healthline|CORE IM|Terese Winslow",               # sources on the pictures
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "reed-sternberg": "binucleated",        # s36: binucleated, neoplastic B cells
    "starry sky": "macrophage",             # s32: sheets of lymphoma with benign macrophages
    "punched out": "",                      # s48 picture; described as lytic
    "bence jones": "urine",                 # s50: positive urine monoclonal protein
    "sezary": "erythroderma",               # s22: widespread red itchy rash (erythroderma)
    "b symptom": "sweats",
    "b-symptom": "sweats",
}
NAMED = {k: v for k, v in NAMED.items() if v}

TOPIC_MINUTES = {}

REQUIRED_IO = []
REQUIRED_VIG = [
    # s10: Rai stage from the stem's lymphocytosis, nodes, organs, hemoglobin and platelets
    ("Rai stage from the vignette", r"lymphocyt", r"\b(?:0|I|II|III|IV)\b|stage", 1),
    # s26 / s40: Lugano (Ann Arbor) stage from where the nodes sit relative to the diaphragm
    ("Lymphoma stage from the node map", r"diaphragm|node|nodes", r"stage", 1),
    # s50 / s56 / s57: MGUS vs smoldering vs myeloma from M-protein, marrow plasma cells and CRAB
    ("Plasma cell disorder from the numbers", r"plasma cells", r"MGUS|monoclonal gammopathy|smoldering|myeloma", 1),
]

HELD = []
