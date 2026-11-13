# -*- coding: utf-8 -*-
"""Lecture 46 scope -- Cytopenias and Hemochromatosis (Ward), CMS I Exam 8 (Hematology Block Exam, Monday
2026-11-30 10 AM, Lectures 46-51; Lecture 47, the AHEC smoking-cessation session, is not tested).

Read by cms_e8_partition.py (guards) and imported by every Lecture 46 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Matt Ward, DMSc, MBA, PA-C ("Modified and presented by", title slide). calendar-data.js lists the lecture
Thursday 2026-11-12, 1-4 PM (3 hours). Deck file "Cytopenias_Hemochromatosis_Objectives_Enhanced.pptx", 107 slides;
every slide was viewed at 1920 px (Keynote PDF render). The "Objectives Enhanced" deck adds the objective slides 2-5
and the guideline-summary slides 53, 59, 60, 98, 104-107 (plain text boxes, a different typeface, a "Source:" line).

Ward's own rule (his PD2 Lecture 7 the same morning): "on my tests you only get tested on things on the slide".
Overlap trap: PD2 Lecture 7 (Anemia, the hematological exam) and Clinical Pathophysiology Lecture 10 (Blood Disorders),
both Ward, cover the same diseases. These questions come from THIS deck only.

RECORDING: three Notability parts in the Exam 8 inbox recordings/ (45.2 + 46.7 + 42.0 min). See RECORDING below and
recordings/cms-l46-cytopenias-hemochromatosis-ward-2026-11-12.flags.md.

SLIDE CONFLICTS AND LOOSE SLIDES (slides win unless he corrected the slide out loud; memory truth_wins_on_conflict):
  s13 vs s27  s13 (differential of iron deficiency): anemia of chronic disease has LOW serum iron and transferrin
              saturation, normal or low TIBC, normal or increased ferritin. s27's comparison table gives the chronic
              disease column serum iron as "up or down" and TIBC "down" (s13: "normal or low"). Keyed: ferritin normal
              or up (both slides agree) and TIBC low/decreased (s27, inside s13's "normal or low"; never keyed as
              "normal"); never the serum iron direction of chronic disease alone.
  s13 vs s87  thalassemia: s13 "reticulocytosis"; s87 "decreased reticulocyte index (marrow failure)". Never keyed.
  s79 vs s83  s79 lists antimalarials "(chloroquine, etc)" as a G6PD trigger; the s83 UpToDate table lists chloroquine
              under "safe for class II and III variants" (and s83 is a partial list from another source). Keyed:
              "antimalarials" as a class only; chloroquine is scope-banned. s83 is excluded from citation.
  s79         calls G6PD an "erythrocyte membrane enzyme"; s77 places it in the glutathione pathway inside the cell.
              Never key where the enzyme sits.
  s86         puts beta thalassemia "generally in patients of African origin" and alpha thalassemia in Southern China,
              Malaysia, Thailand and the Mediterranean. Keyed as the slide reads only for alpha (Asian ancestry: the
              alpha thalassemia 1 trait, aa/--, and higher risk of hydrops fetalis; African ancestry: the alpha
              thalassemia-2 trait, a-/a-). Beta thalassemia ancestry is never keyed.
  s92         chorionic villus sampling "at 9wk gestation" -- the number is never keyed (the testing PERIODS are).
  s101        "Fatigue in combination with s" -- truncated on the slide; nothing keyed from that line.
  s105        footer says "Source: EASL haemochromatosis guidelines (2022)" on the lifespan table (a copied footer).
  s32         "Increased zinc level if caused by copper deficiency" -- keyed as the slide reads.
  s57         "benzine" (benzene) and s62 "akyrin" (ankyrin), s71 "de nova", "EBC" (EBV), "CARS-CoV-2": slide typos;
              questions use the correct spelling.
  s76         "Females can only be homozygous dominant or heterozygous" -- keyed only as "carrier females are generally
              unaffected; X-linked recessive, so generally only males are affected" (s76, s79).
  s93         "humoral heads" (humeral). Questions say humeral head.

RECORDING: three Notability parts, our faster-whisper transcripts (medium.en) cms-l46-...-part{1,2,3}.transcript.txt
(45:11 + 46:42 + 42:02). Notability's own ASR was not available for these notes (dump_notability_asr finds no plist),
so there is no second transcript to cross-examine; quotes below are from ours, placed against the slide being taught.
Part 1 starts at about 13:06 inside the iron deficiency material (slides 6-8 are only partly on tape). Lecture ended
early ("We got out of here a little early"). Flags file: recordings/cms-l46-cytopenias-hemochromatosis-ward-2026-11-12.flags.md.
He teaches well beyond the slides (hepcidin/ferroportin, linezolid, copper/zinc, chelation at a lead level of 45,
CKD iron thresholds, B12 and folate dosing schedules, aplastic severity criteria, immunosuppressive therapy, the
newborn-to-adult ferritin cut-offs by sex): none of that is keyed (slides only).

  Slide flags he gave out loud ([part m]):
    s15 IDA diagnosis       [p1 7]  "All right, you guys want to know this slide here?"
    s23 ACD mechanism       [p1 24] "Want to pay attention to this slide?"
    s47 homocysteine / MMA  [p2 11] "This slide is definitely one that you guys want to pay attention to."
    s58 aplastic treatment  [p2 26] "All right, be familiar with this slide here."
    s75 genetic causes      [p2 45] "Be familiar with this slide." (names the upper smear's cells spherocytes)
    s77-78 G6PD             [p3 1]  "Be familiar with Heinz bodies, what they are, what they represent, and know how ...
                                     intravascular and extravascular." (left = bite cells, right = Heinz bodies)
    s88 thalassemia labs    [p3 12-14] "Be familiar with our lab testing." ... "Did I tell you guys to pay attention to slide 88? Yeah"
    s94 acute chest         [p3 22-23] "Be familiar with our treatments" ... "A chest x-ray is the first imaging study if you're
                                     suspecting acute chest syndrome."
    s98 sickle management   [p3 29] "Be familiar with the management here."
    s104 hemochromatosis tx [p3 34] "Be familiar with treatments here." (therapeutic phlebotomy)
    s105 lifespan table     [p3 36] "I want to be familiar with this slide, too."
  Spoken corrections / caveats:
    s79 vs s83 chloroquine  [p3 2-3] "Chloroquine is a standard regimen. Does not have the same risk as the other medications,
                                     so don't just assume all anti-malarial medications carry that same risk." He sided with the
                                     s83 table: chloroquine stays banned, and the one vignette keyed "Antimalarials" (as a class)
                                     is HELD (below); antimalarials are never keyed as a class trigger.
    s86 beta thalassemia    [p3 10] "Beta is common in Mediterranean, Middle Eastern, South Asian" (the slide says African origin):
                                     beta ancestry stays unkeyed.
    s27 serum iron          [p1 31] "Serum iron's low in both" (the table's chronic disease "up or down"): still unkeyed.
    s34 stippling           [p2 0]  "You also can see stippling in thalassemia ... absence of basophilic stippling does not ...
                                     exclude lead exposure."
    s33 luspatercept        [p1 43] "Sorry, don't know that drug." (de-emphasized; no item keys it)
  Minutes taught per topic: TOPIC_MINUTES below (teaching minutes, digressions on history-taking removed).
"""

DECK = "Cytopenias_Hemochromatosis_Objectives_Enhanced.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

# Syllabus objectives (CMS syllabus p. 20-21, "HEMATOLOGY / Cytopenias and Hemochromatosis"), verbatim. The syllabus
# prints the first two objectives as "1." and "9." with their lists numbered 2-8 and 10-15, then "c." and "d." (the
# population list restarting at 1). Kept as printed, the leading "1." and "9." dropped (the Exam 7 convention).
IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis of the following anemias: 2. Anemia due to deficient production of red blood cells 3. Iron "
        "deficiency 4. Anemia of chronic disease 5. Sideroblastic anemia 6. Megaloblastic anemia 7. Aplastic anemia "
        "8. Anemia due to renal failure")
IO_B = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis of the following anemias and hemochromatosis: 10. Anemia due to increased destruction of red blood "
        "cells 11. Sickle cell anemia 12. Thalassemia 13. G6PD (glucose-6-phosphate dehydrogenase) deficiency "
        "14. Autoimmune hemolytic anemias 15. Hemochromatosis: primary and secondary")
IO_C = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis for leukopenia")
IO_POP = ("Identify medical care strategies for cytopenias and hemochromatosis in the lecture topic list for the "
          "following populations. 1. infants 2. child 3. adolescent 4. adult 5. elderly")
IOS = [IO_A, IO_B, IO_C, IO_POP]

# Topic names the pools use (quiz chips) and their slide ranges.
T_APPROACH = "Anemia: indices and first approach"
T_IDA = "Iron deficiency: causes and presentation"
T_IDA_DX = "Iron deficiency: diagnosis"
T_IDA_TX = "Iron deficiency: iron replacement"
T_ACD = "Anemia of chronic disease"
T_SIDERO = "Sideroblastic anemia and lead poisoning"
T_MACRO = "Macrocytic anemia and folate"
T_B12 = "Vitamin B12 and pernicious anemia"
T_CKD = "Anemia of chronic kidney disease"
T_APLASTIC = "Aplastic anemia"
T_LEUKO = "Leukopenia and neutropenia"
T_HEMOLYSIS = "Hemolysis: labs and workup"
T_AIHA = "Autoimmune hemolytic anemia"
T_G6PD = "G6PD deficiency"
T_THAL = "Thalassemia"
T_SICKLE = "Sickle cell disease"
T_HEMOCHROM = "Hemochromatosis"
T_LIFESPAN = "Across the lifespan and follow-up"

TOPIC_SLIDES = {
    T_APPROACH: (6, 8),
    T_IDA: (9, 13),
    T_IDA_DX: (14, 16),
    T_IDA_TX: (17, 21),
    T_ACD: (22, 27),          # s27 comparison table with iron deficiency
    T_SIDERO: (28, 36),       # s34-36 lead poisoning (s36 = picture of the gum lead line)
    T_MACRO: (37, 42),
    T_B12: (43, 50),          # s50 = summary of the labs "discussed so far"
    T_CKD: (51, 53),
    T_APLASTIC: (54, 58),
    T_LEUKO: (59, 60),
    T_HEMOLYSIS: (61, 70),
    T_AIHA: (71, 74),
    T_G6PD: (75, 83),
    T_THAL: (84, 89),
    T_SICKLE: (90, 98),
    T_HEMOCHROM: (99, 104),
    T_LIFESPAN: (105, 107),   # also s106-107 education / referral / prognosis per condition
}

# Title, objective and section-divider slides, the s83 table (conflict above), and picture-only slides with no text
# to cite (s36 lead line and s46 glossitis pictures are cited together with s35 and s45 instead; s40 smear pictures
# with s39; s78 bite-cell / Heinz-body smears with s77 and s82; s95 complication diagram with s93).
EXCLUDED_SLIDES = {1, 2, 3, 4, 5, 9, 22, 28, 37, 51, 54, 84, 99, 83}

SCOPE_BANNED = [
    # s79 vs s83 conflict: chloroquine is listed as a trigger on one slide and as safe on the other
    r"chloroquine",
    # s92: the gestational week of chorionic villus sampling is not keyed
    r"\b9 ?(?:-| )?(?:wk|week)",
    # s86: beta thalassemia ancestry (the slide's claim is loose)
    r"beta thalass\w+.{0,60}(?:african|mediterranean|asian)|(?:african|mediterranean|asian).{0,60}beta thalass",
    # outside sources named on the slides' pictures and footers
    r"UpToDate|Medscape|Nature Reviews|PathPedia|DrJockers|KDIGO|EASL|EuNet|INNOCHRON",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "koilonychia": "spoon",                 # s12 picture: spoon-shaped, concave nail
    "schistocyte": "fragment",              # s68: red blood cell fragments
    "ring sideroblast": "nucleus",          # s32: iron-containing mitochondria form a ring around the nucleus
    "basophilic stippling": "nucleic",      # s34: abnormal collection of nucleic acids in cells
    "bite cell": "chunk",                   # s77: the spleen takes a chunk out of the cell
    "heinz bod": "inside",                  # s77: Heinz bodies form inside the red blood cell
    "stocking and glove": "hands and feet", # s45: numbness, tingling, burning to the hands and feet
    "lead line": "gum",                     # s35-36: a lead line in the gums
    "glossitis": "tongue",                  # s45-46: smooth, red tongue (pictures)
    "pica": "eat",                          # s12: pica (the urge to eat non-food things; describe it)
}

# Minutes taught per pool topic: filled from the recording (see RECORDING); weights the forms.
TOPIC_MINUTES = {
    T_APPROACH: 1.5,     # p1 0-1 (the opening minutes before 13:06 are not on tape)
    T_IDA: 5.0,          # p1 1-6
    T_IDA_DX: 3.5,       # p1 6-12 less ~3 min on asking about blood thinners
    T_IDA_TX: 10.5,      # p1 12-24 less ~1.5 min on heavy menses / quality of life
    T_ACD: 6.0,          # p1 24-32 less ~2 min on vague answers ("a while")
    T_SIDERO: 16.0,      # p1 32-45 sideroblastic + p2 0-3 lead
    T_MACRO: 4.0,        # p2 3-7
    T_B12: 8.0,          # p2 7-15
    T_CKD: 5.0,          # p2 15-20
    T_APLASTIC: 8.0,     # p2 20-28
    T_LEUKO: 3.5,        # p2 28-31.5
    T_HEMOLYSIS: 8.5,    # p2 31.5-40
    T_AIHA: 5.0,         # p2 40-45
    T_G6PD: 10.0,        # p2 45-47 (s75) + p3 0-8
    T_THAL: 8.0,         # p3 8-16
    T_SICKLE: 13.5,      # p3 16-29.5
    T_HEMOCHROM: 6.5,    # p3 29.5-36
    T_LIFESPAN: 6.0,     # p3 36-42
}

# (label, stem regex, key regex, minimum per form). The pool must hold at least twice the minimum of each.
REQUIRED_IO = [
    # s13 / s14 / s25 / s27: telling anemia of chronic disease from iron deficiency by ferritin and TIBC
    ("Iron deficiency versus chronic disease (ferritin, TIBC)", r"ferritin|total iron.binding|chronic disease",
     r"ferritin|total iron.binding|chronic disease|iron deficiency|inflammation|acute phase", 2),
    # s47: methylmalonic acid separates B12 from folate deficiency
    ("Methylmalonic acid and homocysteine", r"methylmalonic|homocysteine|folate|B12", r"methylmalonic|homocysteine", 1),
    # s59: neutropenia severity from the absolute neutrophil count
    ("Neutropenia severity cut-offs", r"neutrophil", r"500|1,?000|1,?500|mild|moderate|severe", 1),
]
REQUIRED_VIG = [
    # s59: absolute neutrophil count worked from the stem's white count and differential, then classified
    ("Absolute neutrophil count from the differential", r"band", r"\d|mild|moderate|severe", 2),
    # s79 (+ comorbidity): a G6PD-deficient patient with an infection -- which drug to avoid / pick instead
    ("G6PD trigger in a comorbid patient", r"glucose-6-phosphate",
     r"nitrofurantoin|trimethoprim|sulfamethoxazole|quinolone|floxacin|phenazopyridine|methylene blue|antimalarial|fava|naphthalene|mothball", 1),
    # s103: iron-overload thresholds read from the stem's ferritin and transferrin saturation
    ("Hemochromatosis cut-offs from the iron panel", r"transferrin saturation", r".", 1),
]

# Review holds (stem prefixes): flagged again by the audit after their one repair (memory question_quality_pipeline:
# one repair, then drop). The partition skips them; they stay in the pools for the record.
HELD = [
    "A 64-year-old man has had neutropenia on three complete blood counts over 4 months",   # 8664085c: explanation D claim
    "A 34-year-old woman with acute leukemia on chemotherapy has an absolute neutrophil count of 300",  # ce51733b: stem gives D away
    "A 35-year-old man with known glucose-6-phosphate dehydrogenase deficiency is planning a trip to a malaria-endemic region",  # keys antimalarials as a class; Ward [p3 2-3] said not all antimalarials carry the risk
]
