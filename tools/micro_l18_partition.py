#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 18 pool into 2 x 30.

DNA Viruses of Medical Importance (Dr. Webster, 13 November 2026; Exam 3). Deck "Lecture 18  Dr. Webster -  DNA
viruses of medical importance.pptx", 106 slides. Four pools, by slide range:
  A tools/micro_l18_pool_a.py  slides 1-30 (+31, 92)  structure, phage cycles, animal virus replication, acute /
                                                      chronic / latent, oncogenic and teratogenic, the DNA virus groups
  B tools/micro_l18_pool_b.py  slides 31-54 (+ chart 4) poxviruses: smallpox, molluscum, mpox, cowpox, orf
  C tools/micro_l18_pool_c.py  slides 55-84 (+ chart 4-6) the herpesviruses
  D tools/micro_l18_pool_d.py  slides 85-106 (+ chart 6-7) hepatitis B, adenovirus, papilloma, polyoma, parvovirus,
                                                      adeno-associated virus

FIVE NUMBERED OBJECTIVES; every set carries every one (minimums below). The 17 syllabus viruses (Appendix 2) are
the topic axis for objectives 4 and 5; every topic weighted 2 or more is in EVERY set, and every topic weighted 1
in at least ONE (MUST_ANY), so the pair covers every topic.

WEIGHTS ARE MINUTES SPOKEN (recording of 13 November 2026, parts 1 and 2 to [55:10]; flags file
micro-l18-dna-viruses-2026-11-13.flags.md in the inbox; transcript_emphasis_measurement), about 93 content minutes,
stories out. Minutes: phage cycles 8.8 (+ slide 13 1.4), smallpox history and variolation 8.3 (history: dates and
people are not asked, so it buys little), mpox 5.2, hepatitis B 4.5 (+ intro 0.9), cytomegalovirus 4.3, Epstein-Barr
4.3, acute / chronic / latent 3.7, phage-gut-immune 3.1, animal virus replication 3.1, polyomaviruses 3.1, viral
structure 2.6, varicella zoster 2.6, HPV 2.5, adenovirus 2.3, herpes simplex (shared 2.3, type 1 2.1, type 2 0.6,
newborn 1.2, diagnosis 0.6), herpesvirus family 2.2, course of disease 2.2 + host range 1.7 + autoimmune 1.5,
smallpox disease 2.1 + eradication 0.7, parvovirus 1.9, HHV-6/7 1.5, smallpox vaccine 1.5, oncogenic/teratogenic
1.3 + diagnosis 0.9, poxvirus structure 1.3, HHV-8 1.2, molluscum 1.1, cowpox 1.1, AAV 0.8, orf 0.7, survey 0.6.
Scaled to 60, then moved for her signposts: animal virus versus phage replication ("This you need to know ... You
need to know these differences", 2 -> 4), the kinds of viral infection ("you need to know", 2 -> 4), the eight
herpesviruses (slide 57, "Put a star on this little slide", 1 -> 3), hepatitis B ("you need to know that one",
3 -> 5), poxviruses in the cytoplasm (1 -> 2); paid by the phage cycles (6 -> 3), the smallpox history (no
askable history) and the phage-gut and course-of-disease minutes.

WHAT SHE SAID NOT TO NEED stays out: slide 44's three stockpile vaccines ("you don't need"), the chronic fatigue
alternative names. Specific drugs are not asked (standing rule from Lectures 10, 14, 17). No item keys a date, a
person or a number; the one numeric item (herpes simplex type 2, ages 14-29) is EXCLUDED below.
SPOKEN versus SLIDE (no correction; the slide is keyed and the point is not asked): adenovirus oncogenic in humans
(slide 93 says not), EBV incubation, C-section rule, AAV approvals, parvovirus animal diseases.

Engine: tools/micro_l15_l16_partition_lib.py (selection, rotation, guards).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l18_pool_a import POOL_A, CLUSTERS_A
from micro_l18_pool_b import POOL_B, CLUSTERS_B
from micro_l18_pool_c import POOL_C, CLUSTERS_C
from micro_l18_pool_d import POOL_D, CLUSTERS_D
from micro_l15_l16_partition_lib import partition, shipped

EXCLUDE = ("Herpes simplex virus type 2 infection typically occurs in which age group?",)
POOL = [q for q in POOL_A + POOL_B + POOL_C + POOL_D if q["q"] not in EXCLUDE]
assert len(POOL) == 140, len(POOL)
FOLDER = "Microbiology Exam 3"
N_IMG = 8          # picture questions in Set 2 (Set 1 has none, so it stays in Group Study)

TARGET = {
    # pool A
    "Viral structure": 2, "Phage replication cycles": 3, "Phages, the gut and immunity": 1,
    "Animal virus replication": 4, "Course of viral disease": 1, "Acute, chronic and latent infections": 4,
    "Oncogenic and teratogenic viruses": 2, "DNA (deoxyribonucleic acid) virus groups": 1,
    # pool B
    "Poxviruses": 2, "Variola and smallpox": 3, "Smallpox prevention": 1, "Molluscum contagiosum": 1, "Mpox": 2,
    "Cowpox": 1, "Orf virus": 1,
    # pool C
    "Herpesvirus family": 3, "Herpes simplex virus type 1": 2, "Herpes simplex virus type 2": 1,
    "Herpes of the newborn": 1, "Herpes simplex diagnosis": 1, "Varicella zoster virus": 2, "Cytomegalovirus": 3,
    "Epstein-Barr virus": 2, "Human herpesviruses 6 and 7": 1, "Human herpesvirus 8": 1,
    # pool D
    "Hepatitis B virus": 5, "Adenovirus": 2, "Human papillomavirus": 2, "Polyomaviruses": 2, "Parvovirus B19": 2,
    "Adeno-associated virus": 1,
}
assert sum(TARGET.values()) == 60, sum(TARGET.values())


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert len(ids) == 1, "stem prefix matches %d items: %s" % (len(ids), p)
    return ids[0]


def S(*prefixes):
    return [stem(p) for p in prefixes]


CLUSTERS = [(n, S(*ps)) for n, ps in CLUSTERS_A + CLUSTERS_B + CLUSTERS_C + CLUSTERS_D]
MUST_EACH = []
MUST_ANY = [[i for i, q in enumerate(POOL) if q["topic"] == t] for t, n in TARGET.items() if n == 1]

if __name__ == "__main__":
    out = os.path.join(HERE, "micro_l18_sets.json")
    partition(POOL, TARGET, CLUSTERS, MUST_EACH, MUST_ANY, {"1 ": 4, "2 ": 3, "3 ": 2, "5 ": 5}, N_IMG, 20261113,
              out, os.path.dirname(HERE), FOLDER, keep=shipped(POOL, out) if os.path.exists(out) else None)
