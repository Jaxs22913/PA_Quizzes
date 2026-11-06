#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 17 pool into 2 x 30.

Parasites of Medical Importance (Dr. Webster, 6 November 2026, 1-4 pm; Exam 3). The deck file is "Lecture 16 Dr.
Webster Parasites of Medical Importance.pptx" (her own count); the syllabus and the calendar call it Lecture 17,
and so does the site. Four pools, by slide range:
  A tools/micro_l17_pool_a.py  slides 1-54    overview, protozoan drugs, amebas, Balantidium, flagellates,
                                              hemoflagellates (Trypanosoma brucei and cruzi, Leishmania)
  B tools/micro_l17_pool_b.py  slides 55-77   the apicomplexans (Plasmodium, Toxoplasma, Sarcocystis,
                                              Cryptosporidium, Isospora, Cyclospora, Babesia)
  C tools/micro_l17_pool_c.py  slides 78-109  helminth biology and life cycles, the intestinal and tissue nematodes
  D tools/micro_l17_pool_d.py  slides 111-131 flukes, tapeworms, arthropod vectors
  E tools/micro_l17_pool_e.py  added after the recording: helminth pathology (slide 85), Entamoeba prevention
                                              (slide 23), control of the trypanosomes (slides 47 and 51)

THE SYLLABUS GIVES TWO NUMBERED OBJECTIVES and points to Appendix 2's list of 33 organisms. Objective 1 is nearly
the whole deck, so the real coverage axis is the TOPIC field (one per organism, plus the general topics); every set
carries objective 2 (how humans acquire each parasite) at least MIN_IO2 times. Thirty-three organisms do not fit in
one set of 30, so: every topic weighted 2 or more is in EVERY set, and every topic weighted 1 is in at least ONE of
the two sets (MUST_ANY below), so the pair of quizzes covers every syllabus organism.

WEIGHTS ARE MINUTES SPOKEN (recording of 6 November 2026, three parts, read the same day; flags file
micro-l17-parasites-2026-11-06.flags.md in the inbox; transcript_emphasis_measurement). About 105 content minutes,
stories out (her amebic dysentery cruise, a friend's sleeping sickness, the hyena, the Hopkins snail tank, the Food
Network, the Loa loa stick, "brain worms": about 13 minutes); Dirofilaria (1.2, not on the syllabus list) and slide
126's tapeworm-cell tumors (0.8) are not topics. Slides 1-8 were not recorded. Minutes per topic: Plasmodium 10.5,
helminth biology and the four life cycles 8.9, Entamoeba 6.0, Toxoplasma 6.0, Trypanosoma brucei 5.3, T. cruzi
4.8, Trichomonas 4.6, overview and the protozoan drug principle 4.3, Naegleria 4.2, helminth pathology, defense,
diagnosis and drugs 4.0, Sarcocystis + Babesia 3.9, Cryptosporidium 3.2, Enterobius 2.7, Cyclospora 2.6, Giardia
2.5, Leishmania 2.5, Trichinella 2.2, Balantidium 1.9, Ascaris 1.9, Schistosoma 1.6, Acanthamoeba 1.5,
Angiostrongylus 1.5, arthropods 1.5, the hemoflagellate group 1.4, Toxocara 1.4, Taenia saginata 1.4,
Echinococcus 1.4, Taenia solium 1.3, Wuchereria 1.2, Onchocerca 1.2, Opisthorchis 1.1, hookworms 1.0 (the part
before the break was not recorded), Strongyloides 0.8, Loa loa 0.8, Trichuris 0.7, Isospora 0.6, Fasciola 0.6,
Paragonimus 0.5. Scaled to 60 (largest remainders, every syllabus organism at least 1), then two moves for her
signposts: Enterobius 1 -> 2 ("the one that you will almost surely see in your clinical life", slide 94's star) and
the hemoflagellate group 1 -> 2 ("vector control is one of the best ways of controlling these hemoflagellate
diseases", said three times), paid by Plasmodium 6 -> 5 and helminth biology 5 -> 4.

WHAT SHE STRESSED goes in EVERY set (MUST_EACH): slide 14's stars (antiprotozoan drugs are few and toxic); slide
79's star (the definitive host); helminth PATHOLOGY ("Why do we have pathology for worms? This is something you
should know", pool E); Toxoplasma and pregnancy ("pregnant women should never clean the litter box"); Chagas
vector migration (slide 48's star, and "the one that you are more likely to see in your clinical work"). In at
least ONE set (MUST_ANY): water treatment for Entamoeba ("the best prevention", said twice; pool E), vector control
of the trypanosomes (pool E), the trypanosome blood-smear picture ("It would not be a bad thing for you to remember
this lovely picture"), Giardia and campers, Cryptosporidium and recreational water, Trichinella "You cannot cure
it", Opisthorchis and freshwater fish ("never eat freshwater fish as sushi"), raw beef for Taenia saginata ("cook
your beef. Please, please"), Echinococcus from handling dogs.

WHAT SHE SAID NOT TO MEMORIZE stays out: the slide 13, 14 (Table 23.2), 30, 84 (Table 23.4), 87 (Table 23.5) and
129 (Table 23.6) charts, the Naegleria case lists and statistics (25-27), the four hemoflagellate stage names, telling
T. cruzi from T. brucei gambiense by picture, and specific treatments. The pools already keep to that; the items
resting on Table 23.4 alone, and one offering a hemoflagellate stage name, are EXCLUDED below. She corrected no slide.

AUDIT REPAIRS (2026-11-06, after the recording): four items still leaned on Table 23.4 and were rewritten from other
slides, then blind- and audit-reviewed again: the eye-worm picture (it keyed "Deer flies", a name only that chart
gives; it now asks how the worm is acquired, keyed "The bite of small flies", slide 107, against three non-fly routes
from slides 96, 116 and 117), the river-blindness item (its "mangrove or deer fly" distractor is now tsetse flies,
slides 45-47), the lung-fluke item (the stem says "undercooked crustaceans", slide 116, not "freshwater crabs") and
one Strongyloides distractor (egg ingestion in food or water, slides 80 and 91, not "fecally polluted soil").

Engine: tools/micro_l15_l16_partition_lib.py (selection, rotation, guards).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l17_pool_a import POOL_A, CLUSTERS_A
from micro_l17_pool_b import POOL_B, CLUSTERS_B
from micro_l17_pool_c import POOL_C, CLUSTERS_C
from micro_l17_pool_d import POOL_D, CLUSTERS_D
from micro_l17_pool_e import POOL_E, CLUSTERS_E
from micro_l15_l16_partition_lib import partition, shipped

# Left out after the recording (kept in the pool files):
#   - Table 23.4 (slide 84), "a chart that I'm not asking you to memorize" (part 2, 36:35): the "New World hookworm"
#     name and the table's infective-in-egg against infective-in-larval-stage grouping rest on that chart alone.
#   - "I am not going to be asking about the names of these four stages" (part 1, 31:04): the malaria-smear item
#     offers "Trypomastigotes", a hemoflagellate stage name, as a distractor.
EXCLUDE = ("Which hookworm is known as the New World hookworm?",
           "Which intestinal nematode is infective in its larval stage rather than in its egg stage?",
           "Diagnosis rests on finding the small stained forms seen inside these red blood cells. Which stage of the "
           "parasite are they?")
POOL = [q for q in POOL_A + POOL_B + POOL_C + POOL_D + POOL_E if q["q"] not in EXCLUDE]
assert len(POOL) == 121
FOLDER = "Microbiology Exam 3"
N_IMG = 8          # picture questions in Set 2 (Set 1 has none, so it stays in Group Study)
MIN_IO2 = 8

TARGET = {
    # protozoa (pool A; pool E adds Entamoeba prevention and hemoflagellate control)
    "Parasitology overview": 2, "Entamoeba histolytica": 3, "Naegleria fowleri": 2, "Acanthamoeba": 1,
    "Balantidium coli": 1, "Trichomonas vaginalis": 2, "Giardia lamblia": 1, "Hemoflagellates": 2,
    "Trypanosoma brucei": 3, "Trypanosoma cruzi": 2, "Leishmania": 1,
    # apicomplexans (pool B)
    "Plasmodium": 5, "Toxoplasma gondii": 3, "Other coccidia": 2, "Cryptosporidium": 2, "Isospora belli": 1,
    "Cyclospora cayetanensis": 1,
    # helminths and nematodes (pool C; pool E adds helminth pathology)
    "Helminth biology & life cycles": 4, "Helminth pathology & diagnosis": 2, "Ascaris lumbricoides": 1,
    "Trichuris trichiura": 1, "Enterobius vermicularis": 2, "Hookworms": 1, "Angiostrongylus cantonensis": 1,
    "Strongyloides stercoralis": 1, "Trichinella spiralis": 1, "Wuchereria bancrofti": 1, "Onchocerca volvulus": 1,
    "Loa loa": 1, "Toxocara": 1,
    # flukes, tapeworms, vectors (pool D)
    "Schistosoma": 1, "Opisthorchis sinensis": 1, "Paragonimus westermani": 1, "Fasciola hepatica": 1,
    "Taenia saginata": 1, "Taenia solium": 1, "Echinococcus": 1, "Arthropod vectors": 1,
}
assert sum(TARGET.values()) == 60, sum(TARGET.values())


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert len(ids) == 1, "stem prefix matches %d items: %s" % (len(ids), p)
    return ids[0]


def S(*prefixes):
    return [stem(p) for p in prefixes]


# Near-twins, as each pool writer listed them (one item's stem or key gives another away): at most N per set.
CLUSTERS = [(n, S(*ps)) for n, ps in CLUSTERS_A + CLUSTERS_B + CLUSTERS_C + CLUSTERS_D + CLUSTERS_E]


def about(*words):
    """Pool items whose stem or key mentions every word (case-insensitive)."""
    out = []
    for i, q in enumerate(POOL):
        text = (q["q"] + " " + q["opts"][q["c"]][0]).lower()
        if all(w.lower() in text for w in words):
            out.append(i)
    return out


MUST_EACH = [
    S("How does the number of antiprotozoan drugs compare", "Which drawback do antiprotozoan drugs share"),
    S("Which event defines a helminth's definitive host", "Adult Toxocara canis worms live and mate in"),
    S("Which is one way helminths cause disease", "Which list gives the effects of helminth pathology"),
    S("A woman acquires toxoplasmosis during pregnancy", "Which group is advised not to clean a cat's litter"),
    S("Why is Chagas disease becoming more of an issue", "A lifelong resident of the southern United States"),
]
MUST_ANY = [[i for i, q in enumerate(POOL) if q["topic"] == t] for t, n in TARGET.items() if n == 1] + [
    S("Which measure prevents amebiasis caused by Entamoeba"),
    S("Which measure controls both African sleeping sickness"),
    S("Which genus of protozoa is shown in this stained blood smear"),
    S("Giardiasis is common in campers"),
    S("A swimmer develops diarrhea, vomiting and abdominal cramps"),
    S("What can treatment achieve once Trichinella spiralis larvae"),
    S("How do humans acquire Opisthorchis sinensis"),
    S("How do humans acquire Taenia saginata?"),
    S("How do people typically acquire Echinococcus?"),
]

if __name__ == "__main__":
    out = os.path.join(HERE, "micro_l17_sets.json")
    partition(POOL, TARGET, CLUSTERS, MUST_EACH, MUST_ANY, {"2 ": MIN_IO2}, N_IMG, 20261106,
              out, os.path.dirname(HERE), FOLDER, keep=shipped(POOL, out))
