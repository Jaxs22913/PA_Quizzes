# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 17 — Parasites of Medical Importance (Dr. Webster, 6 November 2026), pool E: items
# added AFTER the recording was read (phase 2), for what she signposted aloud that pools A-D asked too thinly.
#
#   [part 2, 37:25] helminth PATHOLOGY (slide 85): "Why do we have pathology for worms? This is something you should
#   know. ... it's important. This is an important thing." Pools A-D asked only defense, diagnosis and drug action
#   (slide 86); these two ask where the damage comes from and what it does.
#   [part 1, 12:02] Entamoeba: "water treatment is the best prevention, water treatment is the best prevention"
#   (slide 23's prevention line). Pools A-D asked how Entamoeba spreads, never how it is prevented.
#   [part 1, 38:19 and 43:07; part 2, 9:06] "vector control is one of the best ways of controlling these
#   hemoflagellate diseases" (slides 47 and 51; slide 61 for malaria). Pools A-D asked the vectors, never the control.
#
# Same rules as pools A-D (see tools/micro_l17_pool_c.py): visible slides only, four options, key authored at 0 with
# the only "Correct." opener, `mis` per distractor, explanations refute and supply the replacing fact.
from micro_l17_pool_c import Q, c, IO1

PATH = "Helminth pathology & diagnosis"
ENT = "Entamoeba histolytica"
HEMO = "Hemoflagellates"

POOL_E = [

Q(PATH, IO1,
  "Which is one way helminths cause disease in their human hosts?",
  ("Feeding on and migrating through tissues",
   "Correct. Helminth pathology arises from worms feeding on and migrating through tissues, from the accumulation "
   "of worms in organs, causing blockages, and from toxic worm secretions. The effects are enlargement and swelling "
   "of organs, hemorrhage, weight loss and anemia."),
  [("Provoking immune attack on their cuticle",
    "The cuticle is one of the worms' adaptations to parasitism: it protects them against immune defense rather "
    "than drawing an attack. The damage comes from worms feeding on and migrating through tissues, accumulating in "
    "organs and causing blockages, and from toxic worm secretions.",
    "an adaptation read as the source of pathology"),
   ("Multiplying inside red blood cells",
    "Multiplying inside red blood cells is how malaria parasites do harm: merozoites enter red cells, multiply and "
    "burst them, and Babesia also attacks red blood cells. Helminths are large multicellular animals whose damage "
    "comes from feeding on and migrating through tissues, blockages and toxic secretions.",
    "a protozoan red-cell mechanism"),
   ("Growing within the host cells they infect",
    "Living inside host cells describes intracellular protozoa such as Plasmodium, an obligate intracellular "
    "sporozoan. Adult helminths are large multicellular animals with specialized tissues and organs; their "
    "pathology comes from feeding on and migrating through tissues, accumulating in organs and toxic secretions.",
    "intracellular protozoa")],
  c(56, 58, 77, 79, 85)),

Q(PATH, IO1,
  "Which list gives the effects of helminth pathology on the human host?",
  ("Organ swelling, hemorrhage, weight loss, anemia",
   "Correct. Worms feeding on and migrating through tissues, worms accumulating in organs and causing blockages, "
   "and toxic worm secretions produce enlargement and swelling of organs, hemorrhage, weight loss and anemia."),
  [("Specialized mouthparts, enzymes and a cuticle",
    "Specialized mouthparts for attachment, enzymes to hydrolyze tissue and a cuticle for protection against immune "
    "defense are the worms' adaptations to parasitism, not effects on the host. The effects are enlargement and "
    "swelling of organs, hemorrhage, weight loss and anemia.",
    "adaptations to parasitism read as effects"),
   ("Eosinophilia, positive serology and eggs in feces",
    "A raised eosinophil count, serological tests and eggs, larvae or adult worms in feces, sputum, urine, blood or "
    "tissue biopsies are the basis of diagnosis. The effects of helminth pathology are enlargement and swelling of "
    "organs, hemorrhage, weight loss and anemia.",
    "diagnostic findings read as effects"),
   ("Halted movement, lost grip and local gut action",
    "Inhibiting the worm's movement, preventing it from holding its position and acting locally in the intestine "
    "describe what antihelminthic drugs do to the worm. Helminth pathology in the host shows as enlargement and "
    "swelling of organs, hemorrhage, weight loss and anemia.",
    "antihelminthic drug actions read as effects")],
  c(85, 86)),


Q(ENT, IO1,
  "Which measure prevents amebiasis caused by Entamoeba histolytica?",
  ("Treating the water supply",
   "Correct. Water treatment is the prevention for amebiasis (a vaccine is under development). Entamoeba "
   "histolytica cysts are swallowed, and epidemics occur in concentrated populations where water supplies are "
   "polluted, such as prisons, hospitals and juvenile care institutions."),
  [("Using nose plugs when swimming",
    "Nose plugs prevent primary amebic meningoencephalitis, because Naegleria fowleri burrows through the nasal "
    "mucosa from freshwater. Entamoeba histolytica is swallowed as cysts, and its prevention is water treatment.",
    "Naegleria's prevention"),
   ("Cooking pork thoroughly",
    "Thorough cooking of pork guards against Trichinella spiralis, which is acquired from undercooked pork or bear "
    "meat. Amebiasis comes from swallowed Entamoeba cysts, with epidemics where water supplies are polluted, so "
    "water treatment is its prevention.",
    "a meat-borne worm's prevention"),
   ("Controlling freshwater snails",
    "Snail control prevents schistosomiasis, whose larvae develop in freshwater snails. Entamoeba histolytica has "
    "no snail stage: its cysts are swallowed, and water treatment is the prevention.",
    "a fluke's prevention")],
  c(16, 17, 19, 23, 29, 101, 112, 113)),

Q(HEMO, IO1,
  "Which measure controls both African sleeping sickness and Chagas disease?",
  ("Controlling the insect vector",
   "Correct. African sleeping sickness is spread by tsetse flies, and its control involves eliminating the tsetse "
   "fly. Chagas disease is spread by the reduviid bug, and its control is through control of the vector; a "
   "Chagas vaccine is still under development."),
  [("Avoiding undercooked meat",
    "Avoiding undercooked meat guards against meat-borne parasites such as Trichinella spiralis and Sarcocystis. "
    "The trypanosomes reach people through insects, the tsetse fly and the reduviid bug, so both diseases are "
    "controlled by controlling the vector.",
    "a meat-borne parasite's prevention"),
   ("Controlling freshwater snails",
    "Snail control prevents schistosomiasis, whose larvae develop in freshwater snails. The trypanosomes have no "
    "snail stage: they are carried by the tsetse fly and the reduviid bug, so control is aimed at the vector.",
    "a fluke's prevention"),
   ("Washing fruits and vegetables",
    "Washing produce, with snail and slug control, prevents rat lungworm (Angiostrongylus cantonensis). The "
    "trypanosomes are carried by blood-sucking insects, so African sleeping sickness and Chagas disease are "
    "controlled through the vector.",
    "rat lungworm's prevention")],
  c(42, 45, 47, 49, 51, 71, 99, 101, 112, 113)),

]

CLUSTERS_E = []
