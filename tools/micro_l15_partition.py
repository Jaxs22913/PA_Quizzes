#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 15 pool into 2 x 30.

Fungi of Medical Importance (Dr. Fair, 30 October 2026, 1-3 pm; Exam 3). Pool A (tools/micro_l15_pool_a.py: fungi
as pathogens, dimorphism, the priority list, epidemiology, diagnosis, control and the four true pathogens, slides
3-37) + pool B (tools/micro_l15_pool_b.py: Sporothrix, the dermatophytes, superficial mycoses, the opportunists and
the mycotoxins, slides 38-65 and 9).

THE SYLLABUS GIVES TWO NUMBERED OBJECTIVES; objective 1 is nearly the whole deck, so the real coverage axis is the
TOPIC field, and every set carries objective 2 (how people acquire each fungus) at least MIN_IO2 times. The
syllabus appendix lists seven organisms for this lecture (Candida, Aspergillus, Cryptococcus, Histoplasma,
Blastomyces, Coccidioides, Paracoccidioides): each is a topic weighted 2 or more, so each is in every set.

PHASE 1 WEIGHTS ARE SLIDE COUNTS (the recording is not yet transcribed): about 60 questions over 63 content
slides, the seven appendix organisms nudged up, the joke and picture-repeat slides (1, 2, 8, 21, 46 and the four
repeats of the map) counted out. The audio pass re-weights by minutes spoken (transcript_emphasis_measurement).
The deck's own flag, "Focus on the Latin names for each body part/region" (slide 43), puts a tinea-by-site item in
EVERY set (MUST_EACH).

Engine: tools/micro_l15_l16_partition_lib.py (selection, rotation, guards).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l15_pool_a import POOL_A
from micro_l15_pool_b import POOL_B
from micro_l15_l16_partition_lib import partition

POOL = POOL_A + POOL_B
FOLDER = "Microbiology Exam 3"
N_IMG = 6          # picture questions in Set 2 (Set 1 has none): every extracted picture ships
MIN_IO2 = 5

TARGET = {
    "Fungal pathogenicity": 4, "Thermal dimorphism": 3, "WHO priority list": 2, "Epidemiology & portals": 3,
    "Diagnosis": 4, "Antifungal control": 3, "Histoplasma": 3, "Coccidioides": 3, "Blastomyces": 3,
    "Paracoccidioides": 2,
    "Sporothrix": 3, "Dermatophytes": 6, "Superficial mycoses": 2, "Candida": 5, "Cryptococcus": 4,
    "Pneumocystis": 3, "Aspergillus": 3, "Mucormycosis & other opportunists": 2, "Fungal allergies & toxins": 2,
}


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert ids, "stem not found: " + p
    return ids


def S(*prefixes):
    return [stem(p)[0] for p in prefixes]


# Near-twins: one item's stem or key answers the other, so at most N of each group per set.
CLUSTERS = [
    (1, S("At which temperature does a thermally dimorphic", "These two colonies are the same fungal")),
    (1, S("What is the main portal of entry for the primary", "After shoveling soil thick with bird",
          "Blastomyces dermatitidis lives in forest soil")),
    (1, S("Why are most fungal infections generally not communicable", "A man is hospitalized with disseminated")),
    (1, S("A woman has had several episodes of vaginal", "Why is immunization typically ineffective")),
    (2, S("Which treatment is used for systemic sporotrichosis", "Which treatment is commonly used for systemic candid",
          "Which regimen does systemic cryptococcal", "Along with amphotericin B, what does treatment")),
    (1, S("How is sporotrichosis usually acquired", "Contaminated plant material pierces",
          "A gardener has the forearm lesions shown")),
    (1, S("Which factor may lead to white or black piedra", "Under the microscope, a hair from a patient")),
    (1, S("In a patient with leukemia, what do Aspergillus", "Which pair of predisposing conditions is associated")),
    (1, S("Which patients are at increased risk of invasive", "Which pair of predisposing conditions is associated")),
]
# Slide 43, "Focus on the Latin names for each body part/region": an item keyed with a tinea name in every set.
MUST_EACH = [S("A 9-year-old has the scaly patch shown", "Which form of ringworm is contracted mainly",
               "A student who shares bedding develops", "A wrestler living in a crowded dormitory",
               "In which form of ringworm may nail extensions")]
MUST_ANY = []

if __name__ == "__main__":
    partition(POOL, TARGET, CLUSTERS, MUST_EACH, MUST_ANY, {"2 ": MIN_IO2}, N_IMG, 20261030,
              os.path.join(HERE, "micro_l15_sets.json"), os.path.dirname(HERE), FOLDER)
