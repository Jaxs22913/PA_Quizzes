#!/usr/bin/env python3
"""Remove length bias from the Microbiology Lecture 3 pool.

This pool is mostly ENUMERATIVE: the correct answer is a list of items the
lecture names, so it is naturally the longest string on the page. Shortening
the answer would delete the content, so the fix is structural — the wrong
choices are rewritten as lists of comparable weight. Two questions whose
distractors all carried one shared explanation are given distinct ones.
"""
import io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))

# (file, old, new) — each must appear exactly once.
EDITS = [
 # ---- pool A: lengthen distractors ----
 ("a", '["Any deviation from health caused by microbes"',
       '["Any deviation from health, whether or not a microbe is involved"'),
 ("a", '["Large intestine", "It carries the highest bacterial numbers in the body."]',
       '["The lumen of the large intestine", "It carries the highest bacterial numbers in the body."]'),
 ("a", '["Skin surface", "It has its own characteristic flora."]',
       '["The skin surface and hair follicles", "It has its own characteristic flora."]'),
 ("a", '["Oral cavity", "Aerobic streptococci are its most common residents."]',
       '["The oral cavity and pharynx", "Aerobic streptococci are its most common residents."]'),
 ("a", '["Aerobic streptococci", "Those are the most common oral residents."]',
       '["Aerobic streptococcal species", "Those are the most common oral residents."]'),
 ("a", '["Any exposure, regardless of host status"',
       '["Any exposure at all, regardless of the host\'s status"'),
 ("a", '["A low infectious dose"', '["A naturally low infectious dose for the organism"'),
 ("a", '["Blood, lymph, bone marrow and spleen"', '["Blood, lymph, bone marrow, spleen and thymus"'),
 ("a", '["Only broken skin and mucous membranes"',
       '["Broken skin and mucous membranes only, never intact skin"'),
 ("a", '["Adhesive slimes"', '["Adhesive slimes and capsules"'),
 ("a", '["Bind the host cell surface"', '["Bind tightly to the surface of the host cell"'),
 ("a", '["Exoenzymes and leukocidins"', '["Exoenzymes, leukocidins and antiphagocytic factors"'),
 ("a", '["A second infection after flora disruption"',
       '["A second infection following disruption of the flora"'),
 ("a", '["It is the first infection in a sequence"',
       '["It is the first infection in the sequence of events"'),
 # ---- pool B: lengthen distractors ----
 ("b", '["Soil and water", "Those are nonliving reservoirs."]',
       '["Soil and water sources", "Those are nonliving reservoirs."]'),
 ("b", '["Fomites", "Those are inanimate vehicles."]',
       '["Fomites and vehicles", "Those are inanimate rather than living."]'),
 ("b", '["Droplet nuclei", "Those are the airborne route."]',
       '["Airborne droplet nuclei", "Those are a route rather than a carrier."]'),
 ("b", '["It is eliminated by vaccination of humans alone"',
       '["It is eliminated by vaccinating the human population alone"'),
 ("b", '["Bloodstream and central nervous system"',
       '["Bloodstream and central nervous system infections"'),
 ("b", '["It always requires surgical drainage"',
       '["It always requires surgical drainage of the site"'),
 ("b", '["New cases over a time period", "That is incidence."]',
       '["New cases over a defined time period", "That is incidence."]'),
 ("b", '["The World Health Organization", "That is the international counterpart."]',
       '["The World Health Organization in Geneva", "That is the international counterpart."]'),
 ("b", '["One with a high mortality rate"', '["One with a high mortality rate in the population"'),
 ("b", '["Some pathogens are too small to see"',
       '["Some pathogens are too small to see under a microscope"'),
 ("b", '["Those with resident flora intact"', '["Those whose resident flora remain fully intact"'),
 # ---- pool B: distractors that all shared one explanation ----
 ("b", '''     ["Only viruses", "The lecture is explicitly broader."],
     ["Only bacteria", "The lecture is explicitly broader."],
     ["Only parasites", "The lecture is explicitly broader."]],''',
       '''     ["Only viruses and bacteria", "Fungi and protozoa are included as well."],
     ["Only bacterial and fungal agents", "Viruses and protozoa are included as well."],
     ["Only parasitic protozoa", "Bacteria, viruses and fungi are included as well."]],'''),
 ("b", '''     ["Rabies virus", "That is a true pathogen."],
     ["Plague bacterium", "That is a true pathogen."],
     ["Malarial protozoan", "That is a true pathogen."]],''',
       '''     ["Rabies virus", "Rabies is a true pathogen, infecting healthy hosts."],
     ["Plague bacterium", "Plague is a true pathogen, not a member of the flora."],
     ["Malarial protozoan", "Malaria is a true pathogen spread by a vector."]],'''),
 # ---- pool B: nosocomial organisms, restructured so every choice is a pair ----
 ("b", '''     ["Only gram-positive cocci", "Gram-negatives lead the list."],
     ["Only anaerobes", "Not the organisms named."],
     ["Only viruses", "Bacteria and yeasts are named."]],''',
       '''     ["Staphylococci and streptococci only", "Both are named, but the gram-negatives lead the list."],
     ["Strict anaerobes and spore formers", "Not among the organisms the lecture names."],
     ["Respiratory viruses and yeasts by themselves", "Yeasts are named; viruses are not."]],'''),
]

if __name__ == "__main__":
    paths = {"a": os.path.join(HERE, "micro_l3_pool_a.py"),
             "b": os.path.join(HERE, "micro_l3_pool_b.py")}
    text = {k: io.open(p, encoding="utf-8").read() for k, p in paths.items()}
    for i, (which, old, new) in enumerate(EDITS):
        n = text[which].count(old)
        if n != 1:
            sys.exit("edit %d matched %d times in pool %s: %.60s" % (i, n, which, old))
        text[which] = text[which].replace(old, new)
    for k, p in paths.items():
        io.open(p, "w", encoding="utf-8").write(text[k])
    print("applied %d edits" % len(EDITS))
