# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 17 — Parasites of Medical Importance (Dr. Webster, 6 November 2026), pool D: deck
# slides 111-131 — the trematodes (Schistosoma, the liver fluke Opisthorchis sinensis, the lung fluke Paragonimus
# westermani, Fasciola hepatica), the cestodes (Taenia saginata, Taenia solium and cysticercosis, Echinococcus) and
# the arthropod vectors (slides 128-131, Table 23.6 on slide 129); plus these organisms' rows on her summary-table
# slide 8 and the trematode and cestode rows of Table 23.4 (slide 84). Pools A-C (tools/micro_l17_pool_a.py, _b, _c)
# hold the protozoa, the apicomplexans and the nematodes (slides 1-109).
#
# ATTRIBUTION: the deck file is "Lecture 16 Dr. Webster Parasites of Medical Importance.pptx" (her own count); the
# syllabus and the calendar call it Lecture 17, and so does the site.
#
# PHASE 1, FROM THE SLIDES ALONE (the recording is not yet transcribed). Every key and every explanation is from the
# VISIBLE slides, text and pictures; the speaker notes are not used. Picture-only content used: slide 8 (the summary
# table: Schistosoma "alternate host of a freshwater snail"; Opisthorchis "don't eat freshwater sushi"; Taenia
# solium taeniasis from undercooked meat, cysticercosis from embryonated eggs; Echinococcus "acquired from dogs",
# hydatid cysts "may need to be surgically removed"), slide 84 (Table 23.4: life-cycle requirements, "Humans and
# snails" for Schistosoma, "Consumption of fish / crabs / water and water plants", Fasciola = sheep liver fluke with
# herbivore hosts, Paragonimus = Oriental lung fluke, Taenia saginata = cattle, Taenia solium = swine), slide 114
# (the Schistosoma cycle: miracidia enter the snail, sporocysts develop there, free-swimming cercariae leave it,
# maturation in the liver, paired adults in the mesenteric venules of the bowel or the venous plexus of the bladder;
# photo (b) is the quiz picture l17-fig-20.jpg), slide 115 (snails under lock and chain = snail control), slide 117
# (the Fasciola cycle), slide 120 (scolex with sucker and hooklets = l17-fig-21.jpg; encysted larva in beef muscle),
# slide 122 (the Taenia solium cycle), slide 123 (cysticercosis: the neurocysticercosis scan = l17-fig-22.jpg, the
# heart = l17-fig-23.jpg), slide 125 (operative photo of the cyst = l17-fig-24.jpg), slide 129 (Table 23.6). Slide
# 79's starred "Adulthood and mating occur in the definitive host***" is used for the Echinococcus host item.
#
# Four options throughout. KEYS SHORT and explanations FULL. Every key is authored at position 0 with the only
# "Correct." opener; tools/micro_l17_partition.py rotates positions per set. `mis` names the misconception each
# distractor stands for (review metadata for tools/blind_review.py; the renderer strips it).
#
# DELIBERATELY NOT ASKED (held), and why:
#   - HOW HUMANS ACQUIRE SCHISTOSOMA: Table 23.4 (slide 84) says "Ingestion of fresh water containing larval stage"
#     for all three species; slides 8, 112 and 114 say the larva penetrates or burrows into the skin / contact with
#     water. No Schistosoma item asks the human route, no option says swallowing water or penetrating skin, and the
#     symptom "itchiness at entry site" (slide 113) is not used because it rests on the contested route. The snail,
#     the miracidium and cercaria, where the adults live, how eggs leave and snail control ARE asked.
#   - Taenia saginata's symptoms: slide 8 "Causes weight loss and wasting in host" against slide 119 "Causes few
#     symptoms; vague abdominal pain and nausea".
#   - WHICH DRUG: praziquantel, oxamniquine (113), triclabendazole, bithionol (116), praziquantel (116, 119),
#     "antiparasitic drugs in combination with antiinflammatory drugs" (121), "chemotherapy is also used" (125); no
#     drug is a key or a distractor. Surgical removal of the Echinococcus masses (non-drug) appears in an
#     explanation.
#   - numbers: "100 million people", "up to 2,000 proglottids", the 5-meter strobila, 2-7 mm and 1-4 mm worm
#     lengths, magnifications; the geographic distributions of schistosomiasis and the distribution column of Table
#     23.6 (trivia).
#   - life-cycle letters ("Life cycle D", "Cycle C and modified A").
#   - WHICH HOST IS DEFINITIVE FOR FASCIOLA: slide 111 says humans are the definitive hosts of flukes, while slide
#     117's cycle picture says "Ruminants are the typical definitive hosts". Fasciola is asked only by its source
#     (raw aquatic plants) and its phases.
#   - the larval stage in Opisthorchis fish: slide 116 says "fish containing cercariae"; the items say only that the
#     fish carry its larvae.
#   - Paragonimus slide 116 ends with a stray word ("...eating undercooked crustaceans; intestinal"); nothing rests on
#     it, and abdominal symptoms are never a Paragonimus distractor.
#   - which SITE cysticerci reach most often (slide 122 "most commonly in subcutaneous tissues, brain, and eyes")
#     against where they do the most damage (slide 121 "heart muscle, eye, or brain"): only "most damaging" is keyed
#     and subcutaneous tissue is never an option.
#   - which species' scolex carries hooklets: slide 8 puts the hooked scolex photo in the Taenia saginata row and
#     slide 120 shows it beside the adult beef tapeworm, captioned only "Tapeworm scolex showing sucker and
#     hooklets". The picture item asks the scolex's job and never ties hooklets to a species.
#   - the vector GENUS for dengue (Table 23.6 gives Culex; slide 130 says only "mosquitoes") and the spelling slips
#     "erhlichosis" and "Babesosis" in Table 23.6; relapsing fever is never the sole keyed fact for one arthropod (lice
#     and soft ticks both carry it, slides 129-130).
#   - Echinococcus "reduce[s] activity of Natural Killer Cells" (125), the trematode body plan (111: digestive,
#     excretory, neuromuscular and reproductive systems; no circulatory or respiratory systems) and alveolar
#     echinococcosis's foxes and coyotes: supportable, left out for count; they can fill a later pool.
#   - Hymenolepis (126-127, and its Table 23.4 row) and Diphyllobothrium latum (Table 23.4): not in this range's
#     organism list. Slide 87 (Table 23.5) is drug content.
# SPELLING: "Shistosoma" (8) is written Schistosoma; "Paragoniumus" (8) Paragonimus; "Echinococcocus" (124)
# Echinococcus; "gall bladder" (117) gallbladder; "Taeniasis" and "Dengue fever" are lower-cased.
SRC = "Lecture 16 Dr. Webster Parasites of Medical Importance.pptx"   # her file name; the site calls it Lecture 17


def c(*n):
    return f"{SRC}, Slide " + (str(n[0]) if len(n) == 1 else ", ".join(map(str, n[:-1])) + " and " + str(n[-1]))


def ci(img, *n):
    """cite with a picture slide: c(n...) + ' and image on Slide img'"""
    return (c(*n) + f" and image on Slide {img}") if n else f"{SRC}, image on Slide {img}"


IO1 = ("1 — Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, "
       "clinical manifestations, methods of treatment, and prevention of parasites of medical importance")
IO2 = "2 — Describe the modes of transmission by which humans acquire parasites of medical importance"
IMG = "micro-exam-3-quiz-images"


def Q(topic, io, q, key, wrong, cite, **kw):
    """key = (text, explanation); wrong = [(text, explanation, misconception), x3]. Key authored at 0."""
    assert len(wrong) == 3, q
    d = dict(topic=topic, io=io, q=q,
             opts=[[key[0], key[1]]] + [[t, e] for t, e, _ in wrong],
             mis={t: m for t, _, m in wrong}, c=0, cite=cite)
    d.update(kw)
    return d


def QO(topic, io, q, options, key_index, cite, **kw):
    """ORDERED (numeric) options, listed ASCENDING: options = [(text, explanation, misconception or None) x4];
    the key's misconception is None. Never rotated by the partition."""
    assert len(options) == 4 and options[key_index][2] is None, q
    d = dict(topic=topic, io=io, q=q, opts=[[t, e] for t, e, _ in options],
             mis={t: m for i, (t, _, m) in enumerate(options) if i != key_index}, c=key_index, cite=cite,
             ordered=True)
    d.update(kw)
    return d


POOL_D = [

# ============================================================== SCHISTOSOMA (slides 8, 84, 111-115)
Q("Schistosoma", IO1,
  "Which larval stage of a fluke is shown?",
  ("Cercaria",
   "Correct. The slender body ending in a forked tail is the cercaria, the second larva. The early larva (miracidium) "
   "develops inside a freshwater snail into the cercaria, and free-swimming cercariae are then released from the "
   "snail into the water. The adult flukes that follow pair up and shed eggs that restart the cycle."),
  [("Miracidium",
    "The miracidium is the early larva that hatches from eggs released into water and goes on to infect the snail; "
    "it is the stage before the one shown. Inside the snail the miracidium develops into the cercaria, the "
    "free-swimming second larva with the forked tail.",
    "earlier larval stage swapped in"),
   ("Sporocyst",
    "Sporocysts develop inside the snail's tissue in successive generations and stay there, so they are never the "
    "free-swimming form shown. The larva the snail releases into the water, with a long forked tail, is the "
    "cercaria.",
    "stage inside the snail confused with the released larva"),
   ("Cysticercus",
    "A cysticercus is a tapeworm larva encysted in muscle, as in beef muscle for the beef tapeworm; it sits enclosed "
    "in a cyst rather than swimming free. A free larva with a forked tail is a fluke's cercaria, the second larva "
    "released by the snail.",
    "tapeworm larva confused with a fluke larva")],
  ci(114, 112),
  img=IMG + "/l17-fig-20.jpg",
  alt="Black-and-white electron micrograph of a slender larva with a club-shaped head end and a long tail that "
      "splits into two forks at its tip.",
  slide="Slide 114"),

Q("Schistosoma", IO2,
  "Schistosome eggs released into water hatch into a larva, the miracidium. Which host must this larva enter to "
  "continue the life cycle?",
  ("A freshwater snail",
   "Correct. Adult flukes live in humans, who release eggs into water; the early larva (miracidium) develops in a "
   "freshwater snail into the second larva (cercaria), which the snail releases into the water. The snail is the "
   "source of the larvae that reach people, and the life cycle requires both humans and snails."),
  [("A freshwater fish",
    "Fish are a host of the Chinese liver fluke, Opisthorchis sinensis, which cycles between mammals, snails and "
    "fish and reaches humans in inadequately cooked fish. The schistosome cycle requires only humans and snails, "
    "and the miracidium develops in the snail.",
    "Opisthorchis host borrowed"),
   ("A freshwater crab",
    "Crabs and other crustaceans belong to the cycle of the lung fluke, Paragonimus westermani, which humans "
    "acquire by eating undercooked crustaceans. The schistosome miracidium instead develops in a freshwater snail "
    "into the cercaria.",
    "Paragonimus host borrowed"),
   ("A grazing cow",
    "Cattle are the intermediate host of the beef tapeworm, Taenia saginata, infected by grazing on land "
    "contaminated with human feces. Schistosomes are flukes whose miracidium must develop in a freshwater snail; "
    "their cycle requires humans and snails.",
    "tapeworm intermediate host borrowed")],
  c(84, 112, 114, 116, 119)),

Q("Schistosoma", IO1,
  "Where do adult schistosomes live and feed on blood?",
  ("Veins of the bowel or bladder",
   "Correct. Schistosomes are blood flukes: after maturing in the liver, the adults migrate to the intestine or "
   "bladder, feed on blood and shed eggs into urine and feces. The paired adults sit in the mesenteric venules of "
   "the bowel or rectum, or in the venous plexus of the bladder."),
  [("Bile ducts draining the liver",
    "The bile duct is where the larvae of the Chinese liver fluke, Opisthorchis sinensis, mature and shed eggs into "
    "the feces. Young schistosomes do mature in the liver, but the adults then move on to the veins of the bowel or "
    "bladder to feed on blood.",
    "Opisthorchis site borrowed"),
   ("The lungs, causing an abscess",
    "Migration to the lungs, with cough, pleural pain and abscess, marks the lung fluke, Paragonimus westermani. "
    "Schistosomiasis can bring a cough, yet its adults live in the veins of the bowel or bladder and shed eggs into "
    "urine and feces.",
    "Paragonimus site borrowed"),
   ("Cysts in heart muscle or eye",
    "Cysts in heart muscle, eye or brain are the encysted larvae of the pork tapeworm in cysticercosis. Adult "
    "schistosomes are not encysted: they are paired blood flukes feeding on blood in the veins of the bowel or "
    "bladder.",
    "cysticercosis site borrowed")],
  c(112, 114, 116, 121)),

Q("Schistosoma", IO1,
  "Which measure prevents schistosomiasis by breaking the parasite's life cycle?",
  ("Controlling freshwater snails",
   "Correct. Snail control is the prevention for schistosomiasis. The early larva (miracidium) must develop in a "
   "freshwater snail into the second larva (cercaria), so removing the snails breaks a life cycle that requires "
   "both humans and snails."),
  [("Cooking freshwater fish well",
    "Cooking fish thoroughly protects against the Chinese liver fluke, Opisthorchis sinensis (don't eat freshwater "
    "sushi), which cycles through snails and fish. Fish play no part in the schistosome cycle, which requires only "
    "humans and snails.",
    "Opisthorchis prevention borrowed"),
   ("Not eating raw aquatic plants",
    "Avoiding raw aquatic plants prevents Fasciola hepatica, which cycles between herbivores, snails and aquatic "
    "plants and reaches humans when the plants are eaten raw. The schistosome cycle runs through freshwater snails, "
    "so its prevention is snail control.",
    "Fasciola prevention borrowed"),
   ("Avoiding contact with dogs",
    "Avoiding infected dogs protects against Echinococcus, which people typically acquire by handling dogs who have "
    "the infection. Dogs have no role in the schistosome cycle; its larvae develop in freshwater snails, the target "
    "of snail control.",
    "Echinococcus prevention borrowed")],
  ci(115, 8, 84, 112, 113, 116, 117, 125)),

# ============================================================== OPISTHORCHIS SINENSIS (slides 8, 84, 116)
Q("Opisthorchis sinensis", IO2,
  "How do humans acquire Opisthorchis sinensis, the Chinese liver fluke?",
  ("Eating undercooked freshwater fish",
   "Correct. The Chinese liver fluke cycles between mammals, snails and fish, and humans are infected by eating "
   "inadequately cooked fish that carry its larvae; hence the warning not to eat freshwater sushi. Its eggs leave "
   "in the feces, reach water and infect snails."),
  [("Eating undercooked freshwater crabs",
    "Undercooked crabs and other crustaceans transmit the lung fluke, Paragonimus westermani, whose worms migrate "
    "to the lungs. The Chinese liver fluke reaches humans in inadequately cooked fish instead, as in freshwater "
    "sushi.",
    "Paragonimus source borrowed"),
   ("Eating raw aquatic plants",
    "Raw aquatic plants transmit Fasciola hepatica, which cycles between herbivores, snails and aquatic plants and "
    "lodges in the liver. The Chinese liver fluke is caught from inadequately cooked freshwater fish, which carry "
    "its larvae.",
    "Fasciola source borrowed"),
   ("Eating raw or undercooked pork",
    "Raw or undercooked pork transmits the pork tapeworm, Taenia solium, causing taeniasis. The Chinese liver fluke "
    "is a fluke whose larvae reach humans in inadequately cooked freshwater fish, not in meat from swine.",
    "tapeworm source borrowed")],
  c(8, 84, 116, 117, 121)),

Q("Opisthorchis sinensis", IO1,
  "In which site do Opisthorchis sinensis larvae mature into egg-shedding adults?",
  ("The bile duct",
   "Correct. Once swallowed, the larvae of the Chinese liver fluke crawl into the bile duct, mature, and shed eggs "
   "into the feces. The feces go into water, where snails are infected, so the bile duct is where this liver "
   "fluke both matures and lays the eggs that continue its cycle."),
  [("The lungs",
    "The lungs are where the worms of the lung fluke, Paragonimus westermani, migrate, causing cough, pleural pain "
    "and abscess. The Chinese liver fluke, as its name suggests, matures in the bile duct and sheds its eggs into "
    "the feces.",
    "Paragonimus site borrowed"),
   ("The bladder veins",
    "The veins of the bladder hold adult Schistosoma haematobium, a blood fluke whose eggs are shed in urine. "
    "Opisthorchis sinensis larvae crawl into the bile duct to mature, and the adults shed their eggs into feces, "
    "not urine.",
    "Schistosoma site borrowed"),
   ("The heart muscle",
    "Heart muscle is one of the sites where pork tapeworm larvae encyst in cysticercosis and do the most damage. "
    "Opisthorchis sinensis is a fluke, not a tapeworm; its larvae crawl into the bile duct, mature and shed eggs "
    "into the feces.",
    "cysticercosis site borrowed")],
  c(84, 114, 116, 121)),

# ============================================================== PARAGONIMUS WESTERMANI (slides 8, 84, 116)
Q("Paragonimus westermani", IO1,
  "Which signs mark infection with Paragonimus westermani?",
  ("Cough, pleural pain and an abscess",
   "Correct. Paragonimus westermani is the lung fluke, also called the Oriental lung fluke: its worms migrate to the "
   "lungs, producing cough, pleural pain and abscess. Its cycle runs between carnivorous animals, snails and "
   "crustaceans before it reaches humans."),
  [("Seizures and psychiatric disturbances",
    "Seizures and psychiatric disturbances come from cysticercosis, when pork tapeworm larvae encyst in the brain. "
    "Paragonimus westermani is a fluke whose worms migrate to the lungs, so its signs are cough, pleural pain and "
    "abscess.",
    "cysticercosis signs borrowed"),
   ("Blockage of the bile duct or pancreas",
    "Inflammation or blockage of the bile duct, gallbladder or pancreas is the chronic phase of fascioliasis, from "
    "the liver fluke Fasciola hepatica. The lung fluke Paragonimus westermani instead causes cough, pleural pain and "
    "abscess.",
    "Fasciola signs borrowed"),
   ("Enlarged, inflamed liver and spleen",
    "Enlargement and inflammation of the liver, spleen and bladder are signs of schistosomiasis, caused by blood "
    "flukes in the veins of the bowel or bladder. Paragonimus westermani migrates to the lungs instead, causing "
    "cough, pleural pain and abscess.",
    "schistosomiasis signs borrowed")],
  c(84, 113, 116, 117, 121)),

Q("Paragonimus westermani", IO2,
  "A person who often eats undercooked crustaceans is at risk for which parasite?",
  ("Paragonimus westermani",
   "Correct. The lung fluke Paragonimus westermani cycles between carnivorous animals, snails and crustaceans. "
   "Humans are infected by eating undercooked crustaceans, and the worms migrate to the lungs."),
  [("Opisthorchis sinensis",
    "Opisthorchis sinensis, the Chinese liver fluke, is caught from inadequately cooked freshwater fish, hence the "
    "warning against freshwater sushi. Undercooked crustaceans are the source of the lung fluke, Paragonimus "
    "westermani.",
    "fish source confused with crustaceans"),
   ("Fasciola hepatica",
    "Fasciola hepatica cycles between herbivores, snails and aquatic plants, and humans are infected by eating raw "
    "aquatic plants, not crustaceans. Undercooked crustaceans carry the lung fluke, Paragonimus westermani.",
    "plant source confused with crustaceans"),
   ("Taenia solium",
    "Taenia solium, the pork tapeworm, reaches humans as cysts in undercooked pork or as embryonated eggs in "
    "contaminated food or water. Undercooked crustaceans are the source of the lung fluke, Paragonimus "
    "westermani.",
    "tapeworm source confused with crustaceans")],
  c(8, 116, 117, 121)),

# ============================================================== FASCIOLA HEPATICA (slides 8, 84, 117)
Q("Fasciola hepatica", IO2,
  "How do humans acquire Fasciola hepatica?",
  ("Eating raw aquatic plants",
   "Correct. Fasciola hepatica, the sheep liver fluke, cycles between herbivores such as sheep and cattle, snails, "
   "and aquatic plants. Humans are infected by eating raw aquatic plants (water plants), after which the fluke "
   "lodges in the liver."),
  [("Eating undercooked fish",
    "Inadequately cooked freshwater fish transmit the Chinese liver fluke, Opisthorchis sinensis, the reason for the "
    "warning against freshwater sushi. Fasciola hepatica reaches humans on raw aquatic plants, the third host in its "
    "cycle with herbivores and snails.",
    "Opisthorchis source borrowed"),
   ("Eating undercooked crabs",
    "Undercooked crabs and other crustaceans transmit the lung fluke, Paragonimus westermani. Fasciola hepatica "
    "cycles between herbivores, snails and aquatic plants, so humans catch it by eating the plants raw.",
    "Paragonimus source borrowed"),
   ("Eating raw or undercooked beef",
    "Raw beef in which the larval form has encysted transmits the beef tapeworm, Taenia saginata. Cattle are "
    "herbivore hosts of Fasciola hepatica too, but humans acquire this fluke by eating raw aquatic plants, not beef.",
    "herbivore host mistaken for the human source")],
  c(8, 84, 116, 117, 119)),

Q("Fasciola hepatica", IO1,
  "What marks the chronic phase of fascioliasis, months or years after infection?",
  ("Blockage of bile duct or gallbladder",
   "Correct. Fasciola hepatica lodges in the liver, and fascioliasis runs in two phases: an acute phase of "
   "nonspecific symptoms, then, months or years later, a chronic phase of inflammation or blockage of the bile "
   "duct, gallbladder or pancreas."),
  [("Abdominal pain, nausea and vomiting",
    "Abdominal pain, nausea and vomiting are the nonspecific symptoms of the acute phase of fascioliasis, not the "
    "chronic one. Months or years later, the chronic phase brings inflammation or blockage of the bile duct, "
    "gallbladder or pancreas.",
    "acute phase swapped for chronic"),
   ("Slowly enlarging cysts in the liver",
    "Slowly enlarging cysts in the liver and lungs are cystic echinococcosis (hydatid disease), from the tiny "
    "tapeworm Echinococcus. Fasciola hepatica is a fluke that lodges in the liver, and its chronic phase inflames or "
    "blocks the bile duct, gallbladder or pancreas.",
    "hydatid disease confused with fascioliasis"),
   ("Seizures and psychiatric disturbances",
    "Seizures and psychiatric disturbances come from cysticercosis, when pork tapeworm larvae encyst in the brain. "
    "The chronic phase of fascioliasis instead inflames or blocks the bile duct, gallbladder or pancreas, months or "
    "years after infection.",
    "cysticercosis signs borrowed")],
  c(117, 121, 124)),

# ============================================================== TAENIA SAGINATA (slides 8, 84, 118-120)
Q("Taenia saginata", IO2,
  "How do humans acquire Taenia saginata?",
  ("Eating raw beef holding encysted larvae",
   "Correct. Taenia saginata is the beef tapeworm, and humans are its definitive host. Infection occurs from eating "
   "raw beef in which the larval form has encysted; in the human, the larva attaches to the small intestine and "
   "becomes an adult."),
  [("Swallowing eggs from feces-tainted land",
    "Grazing on land contaminated with human feces is how cattle, the intermediate host, become infected, not how "
    "humans do. Humans, the definitive host, acquire the beef tapeworm by eating raw beef in which the larval form "
    "has encysted.",
    "the intermediate host's route given to humans"),
   ("Eating cysts in undercooked pork",
    "Cysts in undercooked pork transmit the pork tapeworm, Taenia solium, causing taeniasis. Taenia saginata is the "
    "beef tapeworm, acquired from raw beef in which the larval form has encysted; cattle, not swine, are its "
    "intermediate host.",
    "pork tapeworm source borrowed"),
   ("Handling dogs that carry the worm",
    "Handling dogs who have the infection is how people typically acquire Echinococcus, a tiny tapeworm found in "
    "dogs. Taenia saginata uses humans as the definitive host and cattle as the intermediate host, so infection comes "
    "from raw beef.",
    "Echinococcus source borrowed")],
  c(84, 118, 119, 121, 124, 125)),

Q("Taenia saginata", IO1,
  "What does the tapeworm structure shown do for the worm?",
  ("Grips the intestinal wall",
   "Correct. The pictured head end, with suckers and a crown of hooklets, is the scolex, which grips the intestine. "
   "Behind it the long, ribbonlike body is a chain of proglottids; in humans the larva attaches to the small "
   "intestine and becomes an adult there."),
  [("Takes in food through a mouth",
    "Tapeworms have no mouth: nutrients are absorbed through the body, and each proglottid is adapted to absorbing "
    "food. The structure shown, with suckers and hooklets, is the scolex, whose job is to grip the intestine.",
    "a mouth assumed; tapeworms have none"),
   ("Makes and releases eggs",
    "Making and releasing eggs is the work of the proglottids, each an independent unit in the ribbonlike chain "
    "behind the head. The pictured head end with suckers and hooklets is the scolex, which grips the intestine.",
    "proglottid role given to the scolex"),
   ("Encysts in muscle tissue",
    "Encysting in muscle is what the larval form does, as in raw beef in which the larva has encysted (the "
    "cysticercus). The pictured structure belongs to the adult worm: the scolex, which grips the intestine with "
    "suckers and hooklets.",
    "larval stage confused with the adult's attachment organ")],
  ci(120, 118, 119),
  img=IMG + "/l17-fig-21.jpg",
  alt="Magnified, false-colored view of a rounded worm head end with cup-shaped suckers at its corners and a "
      "central crown of small hooks.",
  slide="Slide 120"),

# ============================================================== TAENIA SOLIUM (slides 8, 84, 121-123)
Q("Taenia solium", IO2,
  "Which exposure causes cysticercosis?",
  ("Swallowing embryonated pork tapeworm eggs",
   "Correct. The pork tapeworm causes taeniasis if contaminated meat is eaten, but cysticercosis if embryonated eggs "
   "are swallowed, from contaminated food or water. The eggs hatch in the intestine, releasing larvae that migrate "
   "to all tissues and encyst."),
  [("Eating larval cysts in undercooked pork",
    "Eating cysts in undercooked pork causes taeniasis, not cysticercosis: the cysts release larvae that develop into "
    "tapeworms, which attach to the intestine and may remain for years. Cysticercosis follows swallowing the "
    "embryonated eggs.",
    "taeniasis route confused with cysticercosis"),
   ("Eating raw beef holding encysted larvae",
    "Raw beef in which the larval form has encysted transmits the beef tapeworm, Taenia saginata, causing taeniasis: "
    "the larva attaches to the small intestine and becomes an adult. Cysticercosis comes from swallowing embryonated "
    "pork tapeworm eggs.",
    "beef tapeworm route borrowed"),
   ("Handling dogs carrying tiny tapeworms",
    "Handling infected dogs is how people typically acquire Echinococcus, which forms hydatid cysts in the liver and "
    "lungs, a different cyst disease. Cysticercosis follows swallowing the embryonated eggs of the pork tapeworm.",
    "hydatid cysts confused with cysticerci")],
  c(8, 119, 121, 124, 125)),

Q("Taenia solium", IO1,
  "Where are the cysts of cysticercosis most damaging?",
  ("Heart muscle, eye or brain",
   "Correct. In cysticercosis, eggs hatch in the intestine and release larvae that migrate to all tissues and "
   "encyst. The cysts are most damaging if they lodge in heart muscle, eye or brain, and in the brain they may cause "
   "seizures and psychiatric disturbances."),
  [("The liver and the lungs",
    "Slowly enlarging cysts in the liver and lungs are cystic echinococcosis (hydatid disease), from the tiny "
    "tapeworm Echinococcus. Pork tapeworm larvae can encyst in any tissue, but their cysts do the most damage in "
    "heart muscle, eye or brain.",
    "hydatid cyst sites borrowed"),
   ("Bile duct, gallbladder or pancreas",
    "Inflammation or blockage of the bile duct, gallbladder or pancreas is the chronic phase of fascioliasis, from "
    "the liver fluke Fasciola hepatica. The cysts of cysticercosis are most damaging in heart muscle, eye or brain.",
    "Fasciola sites borrowed"),
   ("The spleen and the bladder",
    "Enlargement and inflammation of the liver, spleen and bladder are signs of schistosomiasis, a blood fluke "
    "disease of the veins of the bowel or bladder. The cysts of cysticercosis, the encysted larvae of the pork "
    "tapeworm, are most damaging in heart muscle, eye or brain.",
    "schistosomiasis sites borrowed")],
  c(113, 117, 121, 124)),

Q("Taenia solium", IO1,
  "Which disease does this brain scan show?",
  ("Cysticercosis",
   "Correct. Countless small cysts scattered through the brain are neurocysticercosis: swallowed pork tapeworm eggs "
   "hatch and release larvae that migrate to all tissues and encyst. Cysts in the brain are among the most damaging "
   "and may cause seizures and psychiatric disturbances."),
  [("Hydatid disease",
    "Hydatid disease (cystic echinococcosis) forms slowly enlarging cysts in the liver and lungs, from a tiny "
    "tapeworm found in dogs. The scan instead shows many small cysts spread through the brain, the picture of "
    "cysticercosis from the pork tapeworm.",
    "hydatid cysts confused with cysticerci"),
   ("Taeniasis",
    "Taeniasis is the intestinal form: cysts eaten in meat release larvae that develop into tapeworms attached to "
    "the intestine. Tissue cysts such as these in the brain mean the eggs were swallowed, and that causes "
    "cysticercosis instead.",
    "intestinal form confused with the tissue form"),
   ("Schistosomiasis",
    "Schistosomiasis is a blood fluke disease that enlarges and inflames the liver, spleen and bladder. Many small "
    "cysts throughout the brain point instead to cysticercosis, the encysted larvae of the pork tapeworm.",
    "fluke disease confused with tapeworm cysts")],
  ci(123, 113, 121, 124),
  img=IMG + "/l17-fig-22.jpg",
  alt="Axial brain scan in which numerous small bright spots are scattered evenly throughout the brain tissue.",
  slide="Slide 123"),

Q("Taenia solium", IO1,
  "What are the pale nodules studding the heart shown?",
  ("Encysted tapeworm larvae",
   "Correct. The nodules are the cysts of cysticercosis: swallowed pork tapeworm eggs hatch in the intestine, "
   "releasing larvae that migrate to all tissues and encyst. Cysts lodged in heart muscle, as here, are among the "
   "most damaging."),
  [("Embryonated tapeworm eggs",
    "Embryonated eggs are the form that is swallowed; they hatch in the intestine and release the larvae. What "
    "lodges in tissues such as heart muscle is the larva, which encysts there, and that is cysticercosis.",
    "swallowed stage confused with the tissue stage"),
   ("Detached tapeworm proglottids",
    "Proglottids are the egg-making sacs of the adult tapeworm's ribbonlike body in the intestine, and they pass in "
    "the stool. The nodules in this heart are cysts formed by migrating larvae, the encysted stage of cysticercosis.",
    "adult segments confused with larval cysts"),
   ("Attached adult tapeworms",
    "Adult tapeworms develop from larvae released by eaten cysts and attach to the intestine, where they may remain "
    "for years. These heart nodules are larvae that migrated from swallowed eggs and encysted in the tissue.",
    "adult stage confused with larval cysts")],
  ci(123, 118, 119, 121, 122),
  img=IMG + "/l17-fig-23.jpg",
  alt="A whole heart with dozens of pale, rounded nodules bulging from its surface.",
  slide="Slide 123"),

# ============================================================== ECHINOCOCCUS (slides 8, 124, 125)
Q("Echinococcus", IO2,
  "How do people typically acquire Echinococcus?",
  ("Handling infected dogs",
   "Correct. People typically acquire echinococcosis by handling dogs who have the infection; these tiny tapeworms "
   "are found in dogs. The disease is most prevalent where dogs interact with the intermediate hosts: sheep, cattle, "
   "goats and pigs."),
  [("Eating undercooked pork",
    "Undercooked or raw pork transmits the pork tapeworm, Taenia solium, causing taeniasis. Pigs are only "
    "intermediate hosts of Echinococcus; people typically acquire it by handling dogs who have the infection.",
    "intermediate host mistaken for the source"),
   ("Being bitten by fleas",
    "Fleas feed on warm-blooded animals and carry the zoonotic diseases plague and murine typhus. Echinococcus is "
    "instead acquired by handling dogs who have the infection, most often where dogs mix with sheep, cattle, goats "
    "or pigs.",
    "an arthropod vector assumed"),
   ("Eating undercooked crabs",
    "Undercooked crabs and other crustaceans transmit the lung fluke, Paragonimus westermani. Echinococcus is a tiny "
    "tapeworm that people typically acquire by handling dogs who have the infection.",
    "fluke source borrowed")],
  c(8, 84, 116, 124, 125, 130)),

Q("Echinococcus", IO1,
  "Which animal is the definitive host of the parasite that formed the cyst shown?",
  ("Dogs",
   "Correct. The large cyst exposed at surgery is a hydatid cyst of Echinococcus, a tiny tapeworm whose definitive "
   "host is the dog, while sheep, cattle, goats and pigs are its intermediate hosts. Treatment often involves "
   "surgical removal of these parasitic masses."),
  [("Sheep",
    "Sheep are intermediate hosts of Echinococcus, alongside cattle, goats and pigs. Adulthood and mating occur in the "
    "definitive host, and for this tiny tapeworm that host is the dog, which is also how people typically acquire "
    "it.",
    "intermediate host mistaken for definitive"),
   ("Cattle",
    "Cattle are intermediate hosts of Echinococcus, and of the beef tapeworm, Taenia saginata, for which humans are "
    "the definitive host. The definitive host of Echinococcus, where adulthood and mating occur, is the dog.",
    "intermediate host mistaken for definitive"),
   ("Pigs",
    "Pigs are intermediate hosts here, as swine are for the pork tapeworm, Taenia solium, whose definitive host is "
    "the human. Adulthood and mating occur in the definitive host, and for Echinococcus that host is the dog.",
    "intermediate host mistaken for definitive")],
  ci(125, 8, 79, 84, 118, 124),
  img=IMG + "/l17-fig-24.jpg",
  alt="Operative photograph of an opened abdomen showing a large, smooth, white cyst laced with red vessels, "
      "lying against a dark red organ.",
  slide="Slide 125"),

# ============================================================== ARTHROPOD VECTORS (slides 128-131)
Q("Arthropod vectors", IO2,
  "Which diseases do fleas carry as they feed on warm-blooded animals?",
  ("Plague and murine typhus",
   "Correct. Fleas are highly motile insects with flattened bodies that feed on warm-blooded animals and carry "
   "zoonotic diseases: plague and murine typhus. Like other arthropods of medical importance, they transmit the "
   "microbes in the process of feeding, which makes them biological vectors."),
  [("Epidemic typhus and relapsing fever",
    "Epidemic typhus and relapsing fever are spread by lice, which feed on blood and tissue fluid in head and body "
    "hair and release feces that contaminate the wound. The typhus that fleas carry is murine typhus, along with "
    "plague.",
    "lice diseases borrowed"),
   ("Malaria and filariasis",
    "Malaria and filariasis are transmitted by mosquitoes, whose females take the blood meal; mosquitoes require an "
    "aquatic habitat. Fleas, with their flattened bodies, carry the zoonotic diseases plague and murine typhus.",
    "mosquito diseases borrowed"),
   ("Lyme disease and tularemia",
    "Lyme disease and tularemia are carried by hard (ixodid) ticks, arachnids that cling on vegetation and attach to "
    "a host on contact. Fleas are insects that carry the zoonotic diseases plague and murine typhus.",
    "tick diseases borrowed")],
  c(128, 129, 130)),

Q("Arthropod vectors", IO2,
  "Which arthropod spreads epidemic typhus when its feces contaminate the feeding wound?",
  ("Body lice",
   "Correct. Lice are small, soft insects that attach to head and body hair, feed inconspicuously on blood and "
   "tissue fluid, and release feces that contaminate the wound. Body lice (Pediculus) transmit epidemic typhus, "
   "along with trench fever and relapsing fever."),
  [("Fleas",
    "Fleas carry murine typhus and plague, zoonotic diseases they pick up as they feed on warm-blooded animals. "
    "Epidemic typhus, spread when feces contaminate the feeding wound, belongs to body lice.",
    "murine typhus confused with epidemic typhus"),
   ("Soft ticks",
    "Soft (argasid) ticks, with their flexible outer bodies, transmit relapsing fever, a disease lice also carry. "
    "Epidemic typhus, spread when feces contaminate the feeding wound, comes from body lice.",
    "shared relapsing fever leads to the wrong vector"),
   ("Mosquitoes",
    "Mosquitoes require an aquatic habitat, and their females transmit malaria, filariasis and dengue fever with the "
    "blood meal. Epidemic typhus spreads when the feces of body lice contaminate the wound.",
    "wrong insect vector")],
  c(129, 130)),
]

CLUSTERS_D = [
    (1, ["Schistosome eggs released into water hatch",          # the snail host gives away snail control
         "Which measure prevents schistosomiasis by"]),
    (1, ["How do humans acquire Opisthorchis sinensis",         # mirrored option sets (fish / crabs / plants)
         "How do humans acquire Fasciola hepatica?"]),
    (1, ["Which signs mark infection with Paragonimus",         # each holds the other's key as a distractor
         "What marks the chronic phase of fascioliasis"]),
    (1, ["How do humans acquire Taenia saginata?",              # pork-cyst and raw-beef options in both
         "Which exposure causes cysticercosis?"]),
    (1, ["Where are the cysts of cysticercosis most",           # brain is in the key; the scan shows brain cysts
         "Which disease does this brain scan show?"]),
    (1, ["Where are the cysts of cysticercosis most",           # heart is in the key; the picture is a heart
         "What are the pale nodules studding the heart"]),
    (1, ["How do people typically acquire Echinococcus",        # both keyed on the dog
         "Which animal is the definitive host of the"]),
    (1, ["Which diseases do fleas carry as they feed",          # each holds the other's key
         "Which arthropod spreads epidemic typhus when"]),
]
