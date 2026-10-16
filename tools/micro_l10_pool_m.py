# -*- coding: utf-8 -*-
# Microbiology Exam 2, Lecture 10 — Gram-Positive Bacilli of Medical Importance
# (Dr. Webster), pool M: questions written for the Exam 2 Master Exams only
# (tools/micro_e2_masters_partition.py). No topic quiz ships them.
#
# Why: in her Exam 2 review Dr. Webster put spore position (central spore in
# Bacillus anthracis, terminal spore in Clostridium) at "Know cold", and every
# master form carries one spore-position question. Pools A and B hold three,
# so these two complete the five. Grounding: slide 8 ("Large, block-shaped
# rods / Central spores") and the Clostridium tetani picture on slide 28 (the
# terminal spore swelling one end of the rod); the distractors' facts are on
# slides 53 (Listeria, non-spore-forming), 59 (Corynebacterium, irregular
# non-spore-former) and 67 (mycobacteria: no capsules, flagella or spores).
SRC = "Lecture 9 Dr. Webster Gram positive Bacilli.pptx"

from micro_l10_pool_a import IO1

POOL_M = [

dict(topic="Classification", io=IO1,
  q="Which Gram-positive rod forms a central spore?",
  opts=[["Bacillus anthracis",
         "Correct: Bacillus anthracis, the anthrax agent, is a large, block-shaped rod with central spores; Clostridium tetani, by contrast, carries a terminal spore."],
        ["Clostridium tetani",
         "Clostridium tetani carries its spore at one end of the rod, a terminal spore that swells it; the central spore belongs to Bacillus anthracis."],
        ["Listeria monocytogenes",
         "Listeria monocytogenes is a non-spore-forming regular rod; the Gram-positive rod with a central spore is Bacillus anthracis."],
        ["Mycobacterium tuberculosis",
         "Mycobacteria form no capsules, flagella or spores; they are acid-fast, and the rod with a central spore is Bacillus anthracis."]],
  mis={"Clostridium tetani": "reversed spore position (terminal)",
       "Listeria monocytogenes": "non-spore-former",
       "Mycobacterium tuberculosis": "non-spore-former (acid-fast)"},
  c=0, cite=f"{SRC}, Slide 8, 53, 67 and image on Slide 28"),

dict(topic="Classification", io=IO1,
  q="Which Gram-positive rod forms a terminal spore that swells one end of the cell?",
  opts=[["Clostridium tetani",
         "Correct: the Clostridium tetani spore sits at one end of the rod, a terminal spore that swells it; Bacillus anthracis has a central spore instead."],
        ["Bacillus anthracis",
         "Bacillus anthracis is a large, block-shaped rod with a central spore; the terminal spore that swells one end is Clostridium tetani."],
        ["Listeria monocytogenes",
         "Listeria monocytogenes is a non-spore-forming regular rod; the rod with a terminal spore swelling one end is Clostridium tetani."],
        ["Corynebacterium diphtheriae",
         "Corynebacterium diphtheriae is an irregular, non-spore-forming rod; the terminal spore that swells one end of the rod belongs to Clostridium tetani."]],
  mis={"Bacillus anthracis": "reversed spore position (central)",
       "Listeria monocytogenes": "non-spore-former",
       "Corynebacterium diphtheriae": "non-spore-former (irregular)"},
  c=0, cite=f"{SRC}, Slide 8, 53, 59 and image on Slide 28"),
]
