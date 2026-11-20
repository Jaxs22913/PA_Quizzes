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

RECORDING: Notability parts 3 (30:54, slides 4-25; slides 1-3 not on tape) and 4 (35:26, slides 26-57, after an
18-minute break) of recordings/cms-l49-l50-heme-malignancies-gannon-2026-11-18-part{3,4}; ours (faster-whisper
medium.en) and Notability's own ASR both read and cross-examined. Flags file:
recordings/cms-l50-heme-malignancies-ii-gannon-2026-11-18.flags.md.
  Stressed out loud ([part m:ss]):
    s47 CRAB               [p4 23:08] "You absolutely need to know this, write this down ... it will 100% be on a test in
                           some form."
    s50 10% plasma cells   [p4 26:30] "Myeloma though, you only need 10. So remember that for your test too."
    s32 starry sky         [p4 11:25] "If a pathologist ever says starry sky, you think Burkitt's ... you'll definitely see
                           that on a test."
    s32 endemic Burkitt    [p4 10:43] sub-Saharan Africa, "You'll probably see this on a test"; EBV "strongly" associated
    s36 Reed-Sternberg     [p4 13:17] "Highlight, underline, star ... automatically think of Hodgkin's lymphoma."
    s28 tumor lysis        [p4 3:09, 5:17] "Very important to know this ... you need to recognize it for your testing"
    s41 ABVD               [p4 17:42] ABVD with painless lymphadenopathy means Hodgkin
    s7 CLL                 [p3 2:55] "High white count, painless lymphadenopathy, underline, underline, star, star."
    s12 Richter            [p3 11:52] "you should highlight or know about this"
    s23 infections         [p3 26:51] HIV, EBV, HTLV-1, H. pylori; s50 Bence Jones [p4 26:45] with anemia, bone pain and
                           renal failure means myeloma; s25 excisional biopsy, not fine-needle aspiration; LDH "super important"
  De-emphasized: CD numbers [p3 9:22] ("you won't have to know that one"), follicular t(14;18)/BCL-2 [p3 17:56] ("You
    probably don't need to know this"), nodal/splenic marginal zone [p3 20:03], mantle cell [p3 23:02] ("surprised it's
    even on here"), the T-cell subtype list [p3 24:38], Lyme/HHV-8 [p3 27:14], myeloma risk factors [p4 22:24], myeloma
    staging [p4 27:54] ("we don't use staging too much"). Slide 34 barely taught.
  CORRECTED aloud (keyed as she said, i.e. the slide figure is NOT keyed):
    s30/s34 cure rate      [p4 12:48] "This says 50%. I think we're curing more than this ... closer to 70%" (and [p4 8:42]
                           aggressive lymphomas "70, 80%"): the 50% cure figure for aggressive lymphomas / DLBCL is never keyed
                           or stated as fact (scope-banned below); no replacement number is keyed either.
  Audio slips / soft disagreements (slides keyed): CLL median age "seven" [p3 1:03] (slide 70); CLL B symptoms "pretty
    common" (slide 5-10%); Rai III/IV said as "cytopenias" (slide: III anemia, IV thrombocytopenia); nodular lesions
    attributed to Sezary (slide: mycosis fungoides progression; Sezary = erythroderma); Waldenstrom "stroke-like" and
    kidney failure (slide: blurred vision, headache, rarely CVA); s49 said Hodgkin where the slide says NHL; TLS "low
    phosphorus" [p4 3:52] self-corrected to high [p4 5:35]; Burkitt ">90%" without the slide's child/adult split; Hodgkin
    CBC and marrow played down (slide lists both).
  Minutes taught per topic: TOPIC_MINUTES below.

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
    r"50% (?:are )?cured|cure rate.{0,40}\b50%|\b50% cur",          # s30/s34 cure rate corrected aloud
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

TOPIC_MINUTES = {
    T_CLL: 2.5,            # p3 0:04-2:34
    T_CLL_DX: 7.0,         # p3 2:34-9:25 incl. the flow cytometry explainer
    T_CLL_STAGE: 1.0,      # p3 9:28-10:27
    T_CLL_TX: 4.5,         # p3 10:27-16:22 less half the CAR-T tangent
    T_NHL_INDOLENT: 4.7,   # p3 16:29-21:15
    T_NHL_AGGR: 3.9,       # p3 21:15-22:00 + 23:02-26:12
    T_NHL_DX: 5.7,         # p3 22:00-23:02 staging + 26:12-30:47
    T_NHL_TX: 8.4,         # p4 0:08-9:00 + the s34 remark
    T_BURKITT: 3.7,        # p4 9:00-12:45
    T_HL: 3.1,             # p4 13:05-16:11
    T_HL_TX: 3.2,          # p4 16:11-20:15 less a story
    T_MM: 4.6,             # p4 20:18-24:54
    T_MM_DX: 3.7,          # p4 24:54-28:34
    T_MM_TX: 3.0,          # p4 28:34-32:52 less the tandem-transplant Q&A
    T_MGUS: 2.3,           # p4 32:59-35:19
}

REQUIRED_IO = []
REQUIRED_VIG = [
    # s10: Rai stage from the stem's lymphocytosis, nodes, organs, hemoglobin and platelets
    ("Rai stage from the vignette", r"lymphocyt", r"\b(?:0|I|II|III|IV)\b|stage", 1),
    # s26 / s40: Lugano (Ann Arbor) stage from where the nodes sit relative to the diaphragm
    ("Lymphoma stage from the node map", r"diaphragm|node|nodes", r"stage", 1),
    # s50 / s56 / s57: MGUS vs smoldering vs myeloma from M-protein, marrow plasma cells and CRAB
    ("Plasma cell disorder from the numbers", r"plasma cells", r"MGUS|monoclonal gammopathy|smoldering|myeloma", 1),
]

HELD = [
    # d8ec9ba5a0ca2d4a: held after final audit round (explanation defect; no further repair this build).
    "About 80% of chronic lymphocytic leukemia cases arise from one of four chromosomal changes. Which is one of them?",
    # 91385c528fc84978: held after final audit round (explanation defect; no further repair this build).
    "A 73-year-old man with symptomatic chronic lymphocytic leukemia is starting a Bruton tyrosine kinase inhibitor alone. He asks what treatment will be like. Which counseling point is accurate?",
    # 5b51a1dfd5ff5fe5: held after final audit round (explanation defect; no further repair this build).
    "Excess immunoglobulin M in lymphoplasmacytic lymphoma causes which complication?",
    # 8bcebbad9dcbaa61: held after final audit round (explanation defect; no further repair this build).
    "Why is rituximab left out of treatment for T-cell lymphomas?",
    # cc51cbbd43b1a1bb: held after final audit round (explanation defect; no further repair this build).
    "How does tumor lysis syndrome cause acute renal failure?",
    # 4a7bfca0f2278be0: held after final audit round (explanation defect; no further repair this build).
    "Plasma cell disorders arise from which cell?",
    # c3b254aff3bec529: held after final audit round (explanation defect; no further repair this build).
    "What is the approximate yearly rate of smoldering myeloma progressing to multiple myeloma?",
    # e8d309fe39290812: s6 says CLL has no known environmental risk, but s23 lists radiation, DDT farming and EBV for
    # non-Hodgkin lymphoma and s15 places CLL/SLL inside NHL, so three options are defensible.
    "Which statement about environmental risk factors for chronic lymphocytic leukemia is accurate?",
    # d3635344ea9ac8c4: lymphoplasmacytic lymphoma is an NHL, so s23's NHL risks (prior radiation, family history)
    # make the radiation and sibling options defensible alongside farming/pesticides.
    "Which exposure is a risk factor for lymphoplasmacytic lymphoma?",
    # f320c15f8d1aa37d: hepatitis C also raises serum globulins (polyclonal hypergammaglobulinemia), so two options
    # are defensible; s49 names only cirrhosis and chronic inflammation.
    "Which condition can raise serum globulins and must be separated from a plasma cell disorder?",
    # f339a57aee75f56d: failed audit after one repair.
    'A 72-year-old man with chronic lymphocytic leukemia has drenching night sweats, fevers and a 7-kg weight loss over 3 months',
    # 279297f118cd1586: failed audit after one repair.
    'Which non-Hodgkin lymphoma patients may need hospitalization for treatment?',
    # 2b41c930af49ca6f: failed audit after one repair.
    'What is the typical presentation of follicular lymphoma?',
    # 41aaa0be1cacaf3e: failed audit after one repair.
    'Gastric mucosa-associated lymphoid tissue lymphoma is linked in about two thirds of cases to which infection?',
    # 518c55e9efd94859: failed audit after one repair.
    'Endemic Burkitt lymphoma is strongly associated with which virus?',
    # a1203380890de489: failed audit after one repair.
    'A 25-year-old woman has classical Hodgkin lymphoma. Staging imaging shows involved right cervical lymph nodes',
    # 14a98c51c8f494ec: failed audit after one repair.
    'A 26-year-old woman has stage I classical Hodgkin lymphoma in one cervical node region.',
    # 0001e068d03d8154: failed audit after one repair.
    'A 67-year-old man has a monoclonal protein found incidentally. The M-protein is 1.3 g/dL',
    # 89a1b0c1337f3ede: failed audit after one repair.
    'A 71-year-old woman has a painful rib mass; biopsy of the mass proves a plasmacytoma.',
]
