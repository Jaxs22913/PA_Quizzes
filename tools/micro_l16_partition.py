#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 16 pool into 2 x 30.

Significant Microorganisms in Food Safety (Dr. Fair, 30 October 2026, 3-5 pm; Exam 3). Pool A
(tools/micro_l16_pool_a.py: microbes in food, the burden, intoxication versus infection, Escherichia coli,
Salmonella, Campylobacter; slides 2-21 and 30-31) + pool B (tools/micro_l16_pool_b.py: Listeria, Clostridium,
Bacillus cereus, Vibrio, fungi, protozoa and worms, viruses, tracking, prevention; slides 22-36).

FOUR NUMBERED OBJECTIVES, but objective 3 (public concern and antibiotic-resistant strains in the food supply) has
NO slide in the deck, so no question asks it and the set guard covers objectives 1, 2 and 4 (guide 16.15 says so).
Objective 4 (laboratory methods and recalls) rests on few slides (14, 34, 35): at least MIN_IO4 per set.

PHASE 1 WEIGHTS ARE SLIDE COUNTS (the recording is not yet transcribed); the audio pass re-weights by minutes
spoken. Pool guards: no percentage, case count or death toll keyed (slide 9's figures carry a disputed
"worldwide" label); exactly one Bacillus cereus heat-stability item, keyed as slide 28 says (guide 16.17).

Engine: tools/micro_l15_l16_partition_lib.py (selection, rotation, guards).
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l16_pool_a import POOL_A
from micro_l16_pool_b import POOL_B
from micro_l15_l16_partition_lib import partition

POOL = POOL_A + POOL_B
FOLDER = "Microbiology Exam 3"
N_IMG = 3          # picture questions in Set 2 (Set 1 has none): every extracted picture ships
MIN_IO4 = 2

TARGET = {
    "Microbes in food production": 5, "Foodborne illness burden": 4, "Intoxication vs infection": 4,
    "Escherichia coli": 5, "Salmonella": 6, "Campylobacter": 4,
    "Listeria": 6, "Clostridium": 4, "Bacillus cereus": 4, "Vibrio": 3, "Fungi, protozoa & worms": 4,
    "Foodborne viruses": 4, "Tracking food safety": 4, "Kitchen prevention": 3,
}


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert ids, "stem not found: " + p
    return ids


def S(*prefixes):
    return [stem(p)[0] for p in prefixes]


# Near-twins: one item's stem or key answers the other, so at most one of each group per set.
CLUSTERS = [(1, S(*g)) for g in (
    ("Which pairing lists a food intoxication agent first", "A chicken dish carrying Salmonella"),
    ("What must happen for a food infection", "How does Listeria monocytogenes cause illness after"),
    ("In food intoxication, what does a person swallow", "After a preformed toxin is swallowed"),
    ("A water sample streaked on this eosin methylene blue", "A laboratory wants to confirm Escherichia coli"),
    ("Which groups are at greatest risk from salmonellosis", "Campylobacter jejuni is a leading cause of bacterial",
     "Which group is named among those at greatest risk for both"),
    ("Which foodborne bacterium is a leading cause of bacterial", "Campylobacter jejuni is a leading cause of bacterial"),
    ("Why can a single drop of raw poultry fluid", "Which food calls for particular care to prevent Campylobacter"),
    ("Why does keeping deli meats chilled fail", "Which set of foods is most vulnerable to Listeria"),
    ("Within a few hours of a summer picnic", "Which food is the diarrheal form of Bacillus cereus",
     "How soon after eating does Bacillus cereus"),
    ("A person with an open cut on the leg wades", "What are the two major routes of vibriosis"),
    ("A person develops foodborne vibriosis", "What is the current standing of the 'R-month' rule",
     "What are the two major routes of vibriosis"),
    ("A brief illness of rapid onset", "Why does norovirus spread so readily"),
    ("A brief illness of rapid onset", "How can shellfish come to carry norovirus"),
    ("Which two hepatitis viruses are typically spread", "When is a person with hepatitis A most contagious"),
    ("Which two hepatitis viruses are typically spread", "Which measure helps prevent hepatitis A"),
    ("These band patterns come from bacterial isolates", "What is collected in PulseNet for each"),
    ("What is collected in PulseNet for each", "How does comparing isolate patterns in PulseNet"),
    ("Which food safety responsibility rests with the Food", "Which agency's website posts updated recalls"),
    ("Spoilage of bread, cereals and acidic juices", "Which statement describes the place of fungi"),
    ("Which animals are the main reservoirs of Salmonella", "Which household exposure is a known source of Salmonella"),
)]
MUST_EACH = []
MUST_ANY = []

# pool guards (pool headers)
for q in POOL:
    key = q["opts"][q["c"]][0]
    assert not q["io"].startswith("3 "), ("objective 3 has no slide content", q["q"])
    assert not re.search(r"\b(75 million|5,?000|250|23 million)\b", key), ("disputed figure keyed", q["q"])
HEAT = [q for q in POOL if q["topic"] == "Bacillus cereus" and re.search(r"heat[- ](stable|labile)", q["q"] + " ".join(o[0] for o in q["opts"]), re.I)]
assert len(HEAT) <= 1, "more than one Bacillus cereus heat-stability item (slide 28 conflicts with references)"

if __name__ == "__main__":
    partition(POOL, TARGET, CLUSTERS, MUST_EACH, MUST_ANY, {"4 ": MIN_IO4}, N_IMG, 20261031,
              os.path.join(HERE, "micro_l16_sets.json"), os.path.dirname(HERE), FOLDER)
