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

RECORDING: (filled in from the transcripts; see the flags file)
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
TOPIC_MINUTES = {}

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
