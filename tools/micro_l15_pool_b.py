# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 15 — Fungi of Medical Importance (Dr. Fair, 30 October 2026), pool B: deck slides
# 38-65 plus slide 9 (Table 22.3): the subcutaneous mycoses (Sporothrix), the dermatophytes and the Latin name of
# each tinea, the superficial mycoses (tinea versicolor and the piedras), the opportunists (Candida, Cryptococcus,
# Pneumocystis, Aspergillus, the Zygomycota, Fusarium and eumycetoma) and fungal allergies and toxins. Pool A
# (tools/micro_l15_pool_a.py) holds slides 3-37.
# PHASE 1, FROM THE SLIDES ALONE (the recording is not yet transcribed). Every key and every explanation is from
# the VISIBLE slide text or pictures; the speaker notes are never used. Picture content used: slide 9 (Table 22.3,
# opportunists and predisposing conditions), 17 (identification flowchart: Wood's light on hairs, negative stain
# for capsule, animal inoculation only when other methods fail), 18 (branched septate hyphae of Aspergillus), 23
# (levels of invasion), 41 (lymphocutaneous sporotrichosis), 47 (scalp ringworm), 50 (black piedra on a hair
# shaft), 54 (thrush in an adult male with diabetes), 59 (Pneumocystis cysts "containing several bodies").
#
# Four options throughout; keys authored at position 0 and kept short; `mis` names the misconception each
# distractor stands for. No numeric option sets (QO is kept for the format but unused).
#
# DELIBERATELY NOT ASKED (held), and why:
#   - percentages, species counts and dates (39 dermatophyte species, Candida as flora of 20% of humans and 70% of
#     nosocomial fungal infections, 600 Aspergillus species with 8 in disease, Candida auris first found in 2009):
#     trivia; 20% appears once as context in an explanation, never keyed.
#   - Aspergillus TREATMENT (slide 60 lists amphotericin B and nystatin; nystatin is not used for invasive disease
#     in current practice). Nystatin is never used as an option or in an explanation here.
#   - the route by which Cryptococcus and Pneumocystis are acquired: the slides give Cryptococcus's habitat (soil
#     around urban pigeon roosts, decaying wood) and that it infects the lungs, and give only the EXTENT of human
#     contact with Pneumocystis (antibody titers), never a route. Items ask the habitat and the extent, not
#     "inhaled".
#   - slide 40 (Sporothrix microscopic morphology, two uncaptioned panels) and slide 61 (eyelid, brain slices and a
#     chest X-ray under "Clinical aspects of aspergillosis", uncaptioned): no labelled fact to ask. Sporothrix is
#     never called dimorphic or not dimorphic.
#   - slide 46 (the Lamisil "Digger the dermatophyte" commercial): trivia.
#   - lasting immunity: slides 15 and 24 disagree about which true pathogens give immunity (blueprint note), so no
#     distractor or explanation here leans on immunity after infection; "immunization is typically ineffective"
#     (slide 19) is used.
#   - the sporotrichosis picture item avoids Blastomyces as a distractor: Blastomyces lives in decaying wood and
#     causes cutaneous nodules (slides 33, 35), and slide 24 says true-pathogen spores may be inoculated into broken
#     skin, so a wood-splinter vignette could defend it. The vignette uses a thorn.
#   - Table 22.3 items avoid pitting Candida's "catheters" against the Zygomycota's "IV therapy" (an intravenous
#     line is a catheter); Aspergillus's pairing is keyed instead, and Candida's item uses Fusarium as the fourth
#     option.
#   - "dominant opportunistic pathogen" (Candida, slide 51) and "most prominent opportunistic infection in HIV/AIDS"
#     (Pneumocystis, slide 58) are never set against each other in one item.
#   - Candida auris case trends (slide 52's sentence is garbled: "increasing over the last decade but case numbers
#     have increased in recent years").
# SPELLING: the deck's "black mould" (mucormycosis) is written black mold (US spelling); the deck's own note that
# it is "very different" from the Stachybotrys "black mold" is used. Slide 59's label "boides" is read as bodies.
# Slide 39 lists heat packs and/or super-saturated potassium iodide for infection of the "appendages and lungs";
# the items only key amphotericin B and/or itraconazole for SYSTEMIC disease and never ask lung treatment.
SRC = "PAJ5200.Fungi of Medical importance.pptx"


def c(*n):
    return f"{SRC}, Slide " + (str(n[0]) if len(n) == 1 else ", ".join(map(str, n[:-1])) + " and " + str(n[-1]))


def ci(img, *n):
    """cite with a picture slide: c(n...) + ' and image on Slide img'"""
    return (c(*n) + f" and image on Slide {img}") if n else f"{SRC}, image on Slide {img}"


IO1 = ("1 — Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, "
       "clinical manifestations, methods of treatment, and prevention of fungi of medical importance")
IO2 = "2 — Describe the modes of transmission by which humans acquire fungi of medical importance"
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


POOL_B = [

# ============================================================== SPOROTHRIX (slides 38-41)
Q("Sporothrix", IO2,
  "How is sporotrichosis usually acquired?",
  ("A puncture wound from a thorn or wood",
   "Correct. Sporotrichosis, the rose-gardener's disease, usually comes from a puncture wound by a thorn, wood or "
   "bare roots. Like the other subcutaneous mycoses, it begins when the fungus is transferred directly into "
   "traumatized skin and invades the damaged site."),
  [("Sexual contact with an infected partner",
    "Sexual contact is one of the ways Candida albicans spreads, along with surgery, childbirth and breast-feeding. "
    "Sporothrix schenckii is a soil saprobe on decaying plant matter; it gets under the skin through a thorn, wood "
    "or root puncture, not from another person.", "Candida route borrowed"),
   ("Eating grain contaminated by the mold",
    "Eating or inhaling fungal toxins, such as aflatoxin in grains, corn and peanuts, causes a mycotoxicosis, an "
    "intoxication rather than an infection. Sporotrichosis is an infection planted in the skin by a puncture from a "
    "thorn, wood or bare roots.", "mycotoxicosis route confused with infection"),
   ("Sharing contaminated gym equipment",
    "Shared exercise equipment and other fomites spread the dermatophytes and Candida, fungi that live on the human "
    "body. Sporothrix schenckii lives in soil on decaying plant matter and needs a puncture wound, such as a thorn, "
    "to get beneath the skin.", "dermatophyte fomite route")],
  c(12, 38, 39, 52, 65)),

Q("Sporothrix", IO2,
  "Which worker's job most raises the risk of sporotrichosis?",
  ("A plant-nursery worker handling hay bales",
   "Correct. Sporothrix schenckii is a very common saprobe that decomposes plant matter in soil, so garden-center "
   "and plant-nursery workers and people who handle pine straw or hay bales may be at risk. Contaminated plant "
   "material punctures the skin and carries the fungus in."),
  [("An archaeologist on a southwestern dig",
    "Archaeological digs, farming and road work raise dust carrying Coccidioides immitis in the hot, semiarid "
    "southwestern United States, and Valley fever follows inhalation of its arthrospores. Sporotrichosis follows a "
    "puncture by thorns, wood or roots in people who handle plants.", "Coccidioides exposure"),
   ("A worker shoveling bird and bat guano",
    "Moist, nitrogen-rich soil holding bird and bat guano is where Histoplasma capsulatum grows, and its conidia "
    "are inhaled. Sporothrix schenckii instead decomposes plant matter and enters through a thorn, wood or root "
    "puncture, the hazard of nursery and garden-center work.", "Histoplasma exposure"),
   ("A city worker cleaning pigeon roosts",
    "Soil around urban pigeon roosts harbors Cryptococcus neoformans, which healthy people strongly resist. "
    "Sporotrichosis is a plant handler's infection: garden-center and nursery workers and people handling pine "
    "straw or hay bales are the ones at risk.", "Cryptococcus exposure")],
  c(26, 30, 39, 56)),

Q("Sporothrix", IO1,
  "Why do subcutaneous mycoses rarely spread throughout the body?",
  ("Warmth of blood and viscera inhibits them",
   "Correct. Most species that cause subcutaneous mycoses are greatly inhibited by the higher temperatures of the "
   "blood and viscera, so they rarely disseminate. They stay near the site where trauma introduced them, where "
   "the disease is progressive and can destroy skin and underlying tissue."),
  [("Their capsules block entry into blood",
    "A capsule is one of the fungal virulence factors and the mark of Cryptococcus neoformans, which does spread "
    "from the lungs to the meninges and brain. Subcutaneous fungi stay local for a different reason: the warmer "
    "blood and viscera inhibit them.", "Cryptococcus capsule borrowed"),
   ("They cannot get past keratinized skin",
    "Being confined to keratinized epidermis describes the dermatophytes of skin, hair and nails. Subcutaneous "
    "fungi go deeper, through traumatized skin into the tissue below, yet still rarely disseminate because the "
    "warmer blood and viscera inhibit them.", "dermatophyte level confused with subcutaneous"),
   ("Cell-mediated immunity clears them early",
    "Cell-mediated immunity is the host's most important antifungal defense, but subcutaneous mycoses are "
    "progressive and can destroy skin and underlying tissue, so they are not cleared early. Their spread is limited "
    "by the higher temperature of the blood and viscera.", "host defense overestimated")],
  c(14, 15, 38, 42, 56)),

Q("Sporothrix", IO1,
  "Sporothrix schenckii is a saprobic fungus. What does saprobic mean?",
  ("It feeds on dead or decaying matter",
   "Correct. A saprobe derives its nutrition from dead or decaying matter. Sporothrix schenckii is a very common "
   "saprobic fungus that decomposes plant matter in soil, which is why thorns, wood, bare roots, pine straw and hay "
   "carry it to people."),
  [("It must live on a living host",
    "Most fungal pathogens do not require a host to complete their life cycles, and a saprobe lives free in nature. "
    "Sporothrix schenckii decomposes plant matter in soil and infects people only incidentally, through puncture "
    "wounds.", "saprobe confused with an obligate parasite"),
   ("It switches from mold to yeast at 37 C",
    "Growing as a mold at 30 C and as a yeast at 37 C is thermal dimorphism, the most striking adaptation of true "
    "fungal pathogens, not the meaning of saprobic. A saprobe feeds on dead or decaying matter, as Sporothrix does on "
    "plant matter in soil.", "saprobic confused with thermal dimorphism"),
   ("It lives as normal flora on human skin",
    "Living as normal flora of the mouth, genitalia, large intestine or skin describes Candida albicans, whose "
    "infections are usually endogenous. A saprobe such as Sporothrix schenckii lives in soil on dead or decaying "
    "plant matter.", "saprobe confused with resident flora")],
  c(5, 12, 39, 53)),

Q("Sporothrix", IO1,
  "Which treatment is used for systemic sporotrichosis?",
  ("Amphotericin B and/or itraconazole",
   "Correct. Systemic sporotrichosis is treated with amphotericin B and/or itraconazole. Heat packs and/or "
   "super-saturated potassium iodide are the treatment given for infection of the appendages and lungs; once the "
   "disease is systemic, the drug pair is used."),
  [("Heat packs and/or potassium iodide",
    "Heat packs and/or super-saturated potassium iodide are the treatment given for sporotrichosis of the "
    "appendages and lungs. For the systemic infection asked about here, the choice is amphotericin B and/or "
    "itraconazole.", "local treatment applied to systemic disease"),
   ("Pentamidine and/or co-trimoxazole",
    "Pentamidine, an antiprotozoal, and co-trimoxazole (trimethoprim-sulfamethoxazole), an antibacterial, treat "
    "Pneumocystis pneumonia and are not traditional antifungals. Systemic sporotrichosis is treated with the "
    "antifungals amphotericin B and/or itraconazole.", "Pneumocystis treatment"),
   ("Topical azoles and debridement",
    "Topical azoles for several weeks, sometimes with debridement or ultraviolet light, treat dermatophytoses that "
    "stay in keratinized skin. A systemic fungal infection needs systemic drugs: amphotericin B and/or itraconazole "
    "for sporotrichosis.", "dermatophyte treatment")],
  c(39, 45, 58)),

Q("Sporothrix", IO1,
  "Contaminated plant material pierces a gardener's skin, and Sporothrix schenckii forms a nodule at the site. "
  "Where does the infection typically spread next?",
  ("To nearby lymph nodes",
   "Correct. In the lymphocutaneous variety, contaminated plant material penetrates the skin, the fungus forms a "
   "nodule at the site, and the infection then spreads to nearby lymph nodes. It rarely disseminates further, "
   "because the warmer blood and viscera inhibit subcutaneous fungi."),
  [("To the meninges and brain",
    "Spread from the lungs to the meninges and brain, with severe neurological disturbance and death, is the path "
    "of Cryptococcus neoformans in compromised hosts. Sporothrix schenckii in the skin moves from its nodule to "
    "nearby lymph nodes and seldom goes deeper.", "Cryptococcus spread"),
   ("Into the blood and viscera",
    "Subcutaneous fungi are greatly inhibited by the higher temperatures of the blood and viscera, so they rarely "
    "disseminate that way. The usual path from a Sporothrix nodule is to the nearby lymph nodes.",
    "dissemination overestimated"),
   ("Into the sinuses and ear canals",
    "Colonizing the sinuses, ear canals, eyelids and conjunctiva is a feature of Aspergillus, an airborne soil "
    "fungus. A Sporothrix nodule from a skin puncture spreads instead to the nearby lymph nodes.",
    "Aspergillus sites")],
  c(38, 39, 56, 60)),

Q("Sporothrix", IO1,
  "A gardener has the forearm lesions shown, which began as a single nodule where a thorn pierced the hand. "
  "Which organism most likely caused them?",
  ("Sporothrix schenckii",
   "Correct. A thorn puncture, a nodule at the entry site, then a line of lesions up the forearm is "
   "lymphocutaneous sporotrichosis: Sporothrix schenckii forms a nodule where contaminated plant material "
   "penetrated the skin and spreads to nearby lymph nodes."),
  [("Trichophyton species",
    "Trichophyton is a dermatophyte: tinea corporis forms inflamed, red rings on smooth skin after contact with "
    "people, clothing or bedding, and stays in keratinized epidermis. A nodule at a thorn prick that spreads toward "
    "the lymph nodes is subcutaneous sporotrichosis.", "tinea corporis look-alike"),
   ("Malassezia furfur",
    "Malassezia furfur is the yeast of tinea versicolor, a superficial mycosis with mild, chronic scaling and "
    "mottling of the skin rather than nodules. A thorn wound followed by a nodule and spreading lesions marks "
    "Sporothrix schenckii.", "other skin fungus (superficial)"),
   ("Candida albicans",
    "Cutaneous candidiasis develops in chronically moist skin, such as the armpits, groin and under the breasts, "
    "and in burn patients; a thorn does not plant it. A nodule at a puncture site that spreads to nearby lymph "
    "nodes is Sporothrix schenckii.", "other skin fungus (moist skin)")],
  ci(41, 39, 44, 49, 53, 54),
  img=IMG + "/l15-fig-02.jpg",
  alt="A forearm with a crusted red nodule and smaller red lesions spaced out in a line along the skin.",
  slide="Slide 41"),

# ============================================================== DERMATOPHYTES (slides 42-48)
Q("Dermatophytes", IO1,
  "Which tissues do dermatophytes infect?",
  ("Keratinized skin, hair and nails",
   "Correct. Dermatophytoses (ringworm or tinea) are infections strictly confined to the keratinized epidermis: "
   "skin, hair, scalp and nails. They begin with contamination of the skin or hair surface rather than with "
   "inhaled spores or a deep puncture."),
  [("Subcutaneous tissue after trauma",
    "Subcutaneous tissue is reached when a puncture wound carries fungi such as Sporothrix schenckii through "
    "traumatized skin. Dermatophytes stay in the keratinized layer: skin, hair, scalp and nails.",
    "subcutaneous level"),
   ("Mucous membranes of mouth and throat",
    "A thick, white, adherent growth on the mucous membranes of the mouth and throat is thrush, caused by Candida "
    "albicans. Dermatophytes are confined to keratinized epidermis: skin, hair, scalp and nails.",
    "Candida site"),
   ("The lungs after inhaled spores",
    "The lungs, reached by inhaled spores through the respiratory portal, are where the primary mycoses such as "
    "histoplasmosis begin. Dermatophytes infect keratinized epidermis after contamination of the skin or hair "
    "surface.", "primary mycosis portal")],
  c(14, 26, 38, 42, 53)),

Q("Dermatophytes", IO1,
  "Which three genera cause ringworm?",
  ("Trichophyton, Microsporum, Epidermophyton",
   "Correct. The dermatophytes belong to the genera Trichophyton, Microsporum and Epidermophyton. They are closely "
   "related and morphologically similar to one another, and the actual causative agent of ringworm (tinea) varies "
   "from case to case."),
  [("Trichosporon, Piedraia, Malassezia",
    "These are the agents of the superficial mycoses: Trichosporon causes white piedra, Piedraia black piedra, and "
    "the yeast Malassezia furfur tinea versicolor despite its tinea name. Ringworm comes from Trichophyton, "
    "Microsporum and Epidermophyton.", "superficial mycosis agents (tinea versicolor name trap)"),
   ("Rhizopus, Mucor, Fusarium",
    "Rhizopus and Mucor cause mucormycosis, and Fusarium infects eyes, toenails, feet and burned skin; all three "
    "are opportunists of compromised hosts. Ringworm is caused by the dermatophyte genera Trichophyton, Microsporum "
    "and Epidermophyton.", "opportunist genera"),
   ("Histoplasma, Blastomyces, Coccidioides",
    "These are true fungal pathogens, caught by inhaling conidia from disturbed soil and causing lung disease that "
    "can become systemic. Ringworm is a cutaneous mycosis caused by Trichophyton, Microsporum and Epidermophyton.",
    "true systemic pathogens")],
  c(13, 24, 42, 49, 63, 64)),

Q("Dermatophytes", IO2,
  "Which conditions promote dermatophyte infection?",
  ("Abraded skin and close contact",
   "Correct. Hardy dermatophyte spores, abraded skin and close person-to-person or person-to-fomite contact promote "
   "infection. The natural reservoirs are humans, animals and soil, and shared items such as exercise equipment "
   "can carry the fungus from one person to the next."),
  [("Corticosteroids and diabetes",
    "Corticosteroids, diabetes and other impaired defenses predispose to the opportunistic mycoses, such as "
    "candidiasis and cryptococcosis. Dermatophyte infection is promoted instead by hardy spores, abraded skin and "
    "close contact with people or fomites.", "opportunist predisposing factors"),
   ("Inhaling dust from disturbed soil",
    "Dust from disturbed soil carries the conidia of the true fungal pathogens into the lungs. Dermatophytes are "
    "not inhaled; their hardy spores infect abraded skin through close contact with people or fomites.",
    "primary mycosis route"),
   ("Puncture wounds from plant thorns",
    "A thorn puncture carries subcutaneous fungi such as Sporothrix schenckii into deeper tissue. Dermatophytes "
    "stay in keratinized epidermis and spread by close contact with people or fomites onto abraded skin.",
    "subcutaneous route")],
  c(12, 22, 24, 39, 43)),

Q("Dermatophytes", IO1,
  "A 9-year-old has the scaly patch shown, with hair lost over it. Which name fits this ringworm?",
  ("Tinea capitis",
   "Correct. Ringworm of the scalp, tinea capitis, affects the scalp and hair-bearing regions of the head; hair may "
   "be lost, and it is common in children. The child's age, the scalp location and the hair loss over the lesion "
   "all fit."),
  [("Tinea barbae",
    "Tinea barbae is ringworm of the chin and beard of adult males, contracted mainly from animals, so a child's "
    "age already argues against it. A scaly patch on the scalp with hair loss in a child is tinea capitis.",
    "wrong hair-bearing site"),
   ("Tinea corporis",
    "Tinea corporis forms inflamed, red ring lesions anywhere on smooth skin and spreads by contact, clothing and "
    "bedding. The hair-bearing scalp of a child, with hair loss, is the territory of tinea capitis.",
    "body form confused with scalp form"),
   ("Tinea versicolor",
    "Tinea versicolor, despite its name, is a superficial mycosis caused by the yeast Malassezia furfur, with mild, "
    "chronic scaling and mottling of the skin. Scalp ringworm with hair loss in a child is tinea capitis, a "
    "dermatophytosis.", "tinea name trap")],
  ci(47, 44, 49),
  img=IMG + "/l15-fig-03.jpg",
  alt="The back of a child's head with a large gray-white scaly patch and thinned hair around it.",
  slide="Slide 47"),

Q("Dermatophytes", IO2,
  "Which form of ringworm is contracted mainly from animals?",
  ("Tinea barbae",
   "Correct. Tinea barbae, ringworm of the beard, affects the chin and beard of adult males and is contracted "
   "mainly from animals. The other forms are tied to other sources: public surfaces, clothing and bedding, or "
   "crowded living."),
  [("Tinea pedis",
    "Tinea pedis, ringworm of the foot, is spread by exposure to public surfaces and occurs between the digits and "
    "on the soles. The beard form, tinea barbae, is the one contracted mainly from animals.",
    "public-surface form"),
   ("Tinea corporis",
    "Tinea corporis, ringworm of the body, spreads by contact, clothing and bedding and forms inflamed, red rings on "
    "smooth skin. Tinea barbae of the chin and beard is the form caught mainly from animals.", "fomite form"),
   ("Tinea cruris",
    "Tinea cruris, the jock itch of the groin and scrotal regions, is pervasive among athletes and in crowded "
    "living conditions. Ringworm caught mainly from animals is tinea barbae, of the chin and beard of adult males.",
    "crowded-living form")],
  c(43, 44, 45)),

Q("Dermatophytes", IO1,
  "A student who shares bedding develops inflamed, red ring-shaped lesions on the smooth skin of the trunk. Which "
  "name fits this ringworm?",
  ("Tinea corporis",
   "Correct. Tinea corporis, ringworm of the body, occurs as inflamed, red ring lesions anywhere on smooth skin and "
   "spreads by contact, clothing and bedding. Rings on smooth trunk skin after shared bedding are the decisive "
   "clues."),
  [("Tinea cruris",
    "Tinea cruris (jock itch) affects the groin and scrotal regions and is pervasive among athletes and in crowded "
    "living conditions. Ring lesions on smooth skin elsewhere, such as the trunk, are tinea corporis.",
    "adjacent site"),
   ("Tinea capitis",
    "Tinea capitis involves the scalp and hair-bearing regions of the head, may cause hair loss and is common in "
    "children. Rings on the smooth skin of the trunk are tinea corporis.", "scalp form"),
   ("Tinea unguium",
    "Tinea unguium is a persistent colonization of the nails of the hands and feet that distorts the nail bed. "
    "Inflamed, red rings on smooth skin after shared bedding are tinea corporis.", "nail form")],
  c(44, 45)),

Q("Dermatophytes", IO1,
  "A wrestler living in a crowded dormitory has ringworm of the groin and scrotal skin. Which name fits?",
  ("Tinea cruris",
   "Correct. Tinea cruris, the jock itch, affects the groin and scrotal regions and is pervasive among athletes and "
   "in crowded living conditions. An athlete in crowded housing with groin and scrotal involvement fits it "
   "exactly."),
  [("Tinea pedis",
    "Tinea pedis is ringworm of the foot, between the digits and on the soles, spread by exposure to public "
    "surfaces. Ringworm of the groin and scrotum is tinea cruris.", "athlete's site confusion"),
   ("Tinea barbae",
    "Tinea barbae affects the chin and beard of adult males and comes mainly from animals, not from crowded living. "
    "The groin and scrotal regions, in an athlete sharing close quarters, are the territory of tinea cruris.",
    "wrong male-pattern site"),
   ("Tinea manuum",
    "Tinea manuum is ringworm of the hand, spread like tinea pedis by public surfaces and found between the digits "
    "and on the soles. Groin and scrotal ringworm in a crowded-living athlete is tinea cruris.", "hand form")],
  c(44, 45)),

Q("Dermatophytes", IO2,
  "How is tinea pedis mainly spread?",
  ("Exposure to public surfaces",
   "Correct. Tinea pedis (foot) and tinea manuum (hand) are spread by exposure to public surfaces and occur between "
   "the digits and on the soles. Tellingly, tinea pedis is rare where people usually go barefoot, so it is the "
   "shared surfaces, not bare feet, that matter."),
  [("Contact with infected animals",
    "Contact with animals is the main source of tinea barbae, ringworm of the chin and beard of adult males. The "
    "foot form, tinea pedis, comes from exposure to public surfaces.", "barbae source"),
   ("Puncture by thorns or splinters",
    "A thorn or splinter puncture introduces subcutaneous fungi such as Sporothrix schenckii into deeper tissue. "
    "Tinea pedis is a cutaneous infection of the keratinized skin of the foot, picked up from public surfaces.",
    "subcutaneous route"),
   ("Going barefoot as a daily habit",
    "Tinea pedis is rare where people usually go barefoot, so daily bare feet are not its source. It spreads by "
    "exposure to public surfaces and settles between the digits and on the soles.",
    "reversed: bare feet assumed to cause it")],
  c(39, 43, 44, 45)),

Q("Dermatophytes", IO2,
  "In which form of ringworm may nail extensions provide a portal of entry?",
  ("Tinea unguium",
   "Correct. Tinea unguium, ringworm of the nails, is a persistent colonization of the nails of the hands and feet "
   "that distorts the nail bed, and nail extensions may provide a portal of entry to the nail bed."),
  [("Tinea manuum",
    "Tinea manuum is ringworm of the hand, found between the digits and spread by exposure to public surfaces. The "
    "nails, entered by way of nail extensions, belong to tinea unguium.", "hand form confused with nail form"),
   ("Tinea pedis",
    "Tinea pedis is ringworm of the foot, between the digits and on the soles, picked up from public surfaces. The "
    "nail-bed form that nail extensions can open to the fungus is tinea unguium.", "foot form confused with nail form"),
   ("Tinea capitis",
    "Tinea capitis involves the scalp and hair-bearing regions of the head, with possible hair loss, and is common "
    "in children. Persistent nail colonization that distorts the nail bed is tinea unguium.",
    "other keratin site")],
  c(44, 45)),

Q("Dermatophytes", IO1,
  "What is the usual treatment for dermatophytoses?",
  ("Topical azoles for several weeks",
   "Correct. Treatment of dermatophytoses most often uses topical antifungal agents, azoles applied for several "
   "weeks, sometimes partnered with oral antifungal drugs if needed. Debridement of the skin and ultraviolet light "
   "treatments have also been successful."),
  [("Super-saturated potassium iodide",
    "Super-saturated potassium iodide, with heat packs, treats sporotrichosis, a subcutaneous mycosis. Ringworm of "
    "the keratinized skin, hair and nails is treated mainly with topical azoles for several weeks.",
    "sporotrichosis treatment"),
   ("Removal of tissue and amphotericin B",
    "Removal of affected tissues plus amphotericin B is the treatment for mucormycosis invading the nose, eyes, "
    "heart and brain. Dermatophytoses stay in the keratinized epidermis and respond to topical azoles over several "
    "weeks.", "mucormycosis treatment"),
   ("Immunization against the fungus",
    "Immunization is typically ineffective against fungal infections because reinfection is exceedingly common. "
    "Dermatophytoses are treated, most often with topical azoles for several weeks, rather than prevented by a "
    "vaccine.", "vaccine belief")],
  c(19, 39, 45, 63)),

# ============================================================== SUPERFICIAL MYCOSES (slides 49-50)
Q("Superficial mycoses", IO1,
  "Which organism causes tinea versicolor?",
  ("Malassezia furfur, a yeast",
   "Correct. Tinea versicolor is caused by a yeast, Malassezia furfur, and elicits mild, chronic scaling and "
   "mottling of the skin. The same yeast is also implicated in folliculitis, psoriasis and seborrheic dermatitis."),
  [("Trichophyton, a dermatophyte",
    "Trichophyton is a dermatophyte genus that causes ringworm of keratinized skin, hair and nails. Despite its tinea "
    "name, tinea versicolor is a superficial mycosis caused by the yeast Malassezia furfur.",
    "tinea name implies a dermatophyte"),
   ("Piedraia, a piedra agent",
    "Piedraia causes black piedra, dark-brown to black gritty nodules on scalp hairs. The mild scaling and mottling "
    "of the skin in tinea versicolor come from the yeast Malassezia furfur.", "other superficial agent"),
   ("Candida albicans, a yeast",
    "Candida albicans is also a yeast, but on the skin it causes cutaneous candidiasis in chronically moist areas "
    "and in burn patients. The chronic scaling and mottling of tinea versicolor are caused by Malassezia furfur.",
    "other skin yeast")],
  c(42, 49, 53)),

Q("Superficial mycoses", IO2,
  "Which factor may lead to white or black piedra?",
  ("Poor hygiene, such as oily hair products",
   "Correct. Both piedras are considered non-contagious and may result from poor personal hygiene, such as oily "
   "hair products and tight hats or veils. They are superficial mycoses of the hair shaft, and neither is common "
   "in the United States."),
  [("Close contact with an infected person",
    "Both piedras are considered non-contagious, so close contact with an infected person is not how they arise. "
    "Person-to-person spread is a feature of the dermatophytes and Candida, which live on the human body.",
    "assumed contagious"),
   ("Handling infected household animals",
    "Animals are the main source of tinea barbae, a dermatophytosis of the chin and beard. The piedras are "
    "non-contagious and are linked to poor hygiene, such as oily hair products and tight hats or veils.",
    "barbae source"),
   ("Inhaling spores from bird guano",
    "Spores from soil rich in bird and bat guano are inhaled in histoplasmosis, a lung infection. The piedras sit on "
    "the hair shaft and are linked to poor hygiene: oily hair products, tight hats or veils.",
    "primary mycosis route")],
  c(12, 26, 44, 49, 50)),

Q("Superficial mycoses", IO1,
  "Whitish or colored masses form on a patient's pubic and axillary hairs. Which genus is responsible?",
  ("Trichosporon",
   "Correct. White piedra (piedra means stone) is caused by Trichosporon species: whitish or colored masses develop "
   "on pubic or axillary hair and can also involve body, beard, mustache or eyebrow hair."),
  [("Piedraia",
    "Piedraia causes black piedra, dark-brown to black gritty nodules mainly on scalp hairs. Whitish masses on pubic "
    "or axillary hair are white piedra, caused by Trichosporon.", "the other piedra"),
   ("Malassezia",
    "Malassezia furfur is the yeast of tinea versicolor, which causes scaling and mottling of the skin rather than "
    "masses on hair shafts. White piedra is caused by Trichosporon.", "other superficial agent"),
   ("Microsporum",
    "Microsporum is a dermatophyte that causes ringworm, such as tinea capitis with possible hair loss. Stony, "
    "whitish masses clinging to pubic or axillary hairs are white piedra from Trichosporon.",
    "dermatophyte of hair")],
  c(42, 44, 49)),

Q("Superficial mycoses", IO1,
  "Under the microscope, a hair from a patient's scalp carries the dark, gritty nodule shown. What is this "
  "infection?",
  ("Black piedra",
   "Correct. Black piedra, caused by Piedraia species, forms dark-brown to black gritty nodules mainly on scalp "
   "hairs, as on this hair shaft. It is considered non-contagious, may follow poor hygiene and is not common in the "
   "United States."),
  [("White piedra",
    "White piedra, caused by Trichosporon, forms whitish or colored masses mainly on pubic or axillary hair. A dark, "
    "gritty nodule on a scalp hair is black piedra, caused by Piedraia.", "the other piedra"),
   ("Tinea capitis",
    "Tinea capitis is a dermatophyte infection of the scalp and hair-bearing head that may cause hair loss and is "
    "common in children. A discrete gritty nodule stuck to the hair shaft is black piedra, a superficial mycosis.",
    "scalp ringworm"),
   ("Tinea versicolor",
    "Tinea versicolor is a skin infection by the yeast Malassezia furfur, with mild, chronic scaling and mottling. A "
    "nodule on a hair shaft, not a change in the skin, marks black piedra.", "other superficial mycosis")],
  ci(50, 44, 49),
  img=IMG + "/l15-fig-04.jpg",
  alt="A microscope view of a single hair shaft with a dense, brown, granular nodule wrapped around it.",
  slide="Slide 50"),

# ============================================================== CANDIDA (slides 9, 17, 18, 51-55)
Q("Candida", IO1,
  "Which traits make hospital outbreaks of Candida auris hard to eradicate?",
  ("Drug, heat and disinfectant resistance",
   "Correct. Candida auris is emerging as a serious cause of invasive candidiasis, with hospital outbreaks that are "
   "difficult to eradicate: it shows antifungal drug resistance, is thermoresistant and is partially resistant to "
   "common disinfectants. It was first identified in an ear infection, hence its name."),
  [("A capsule shown by negative stain",
    "An encapsulated budding yeast on negative stain is Cryptococcus neoformans, and capsules are a fungal virulence "
    "factor. Candida auris outbreaks persist because the yeast resists antifungal drugs, tolerates heat and partly "
    "resists common disinfectants.", "Cryptococcus trait"),
   ("Arthroconidia spread by windstorms",
    "Windstorms after cycles of drought and heavy rain spread Coccidioides from alkaline, salty soils in hot, "
    "semiarid climates. Candida auris is a hospital problem whose outbreaks resist eradication through drug, heat "
    "and partial disinfectant resistance.", "Coccidioides trait"),
   ("Switching between mold and yeast forms",
    "Switching between a mold at 30 C and a yeast at 37 C is thermal dimorphism, the adaptation of the true fungal "
    "pathogens to the human host. Candida auris outbreaks persist because of drug resistance, heat tolerance and "
    "partial disinfectant resistance.", "dimorphism taken as the hospital trait")],
  c(5, 14, 30, 52, 56, 57)),

Q("Candida", IO2,
  "Besides arising from a person's own flora, how can Candida albicans be spread?",
  ("Childbirth, breast-feeding and sex",
   "Correct. Candida albicans is a widespread yeast that is usually endogenous and not always considered contagious, "
   "yet it can be spread through surgery, childbirth, breast-feeding and sexual contact. Vulvovaginal infection may "
   "pass to unprotected sexual partners, especially uncircumcised males."),
  [("Soil around urban pigeon roosts",
    "Soil around urban pigeon roosts and soil with decaying wood are the home of Cryptococcus neoformans, an "
    "environmental yeast. Candida albicans lives on people and is spread through surgery, childbirth, "
    "breast-feeding and sexual contact.", "Cryptococcus source"),
   ("Thorn and wood splinter punctures",
    "A thorn or wood puncture plants Sporothrix schenckii, a soil saprobe, under the skin. Candida albicans passes "
    "between people through surgery, childbirth, breast-feeding and sexual contact.", "Sporothrix route"),
   ("Eating moldy grain or peanuts",
    "Eating grains, corn or peanuts carrying aflatoxin causes a mycotoxicosis, a poisoning by a fungal toxin. Candida "
    "albicans infection spreads from person to person through surgery, childbirth, breast-feeding and sexual "
    "contact.", "mycotoxin route")],
  c(39, 52, 53, 56, 65)),

Q("Candida", IO2,
  "Where does Candida albicans live as part of the normal flora?",
  ("Oral cavity, genitalia and skin",
   "Correct. Candida albicans is normal flora of the oral cavity, genitalia, large intestine or skin in about 20% of "
   "humans, which is why its infections are usually endogenous. When host defenses fail, this resident yeast "
   "becomes the dominant opportunistic pathogen."),
  [("Moist soil rich in bat guano",
    "Moist, nitrogen-rich soil with bird and bat guano is where Histoplasma capsulatum grows, and people inhale its "
    "conidia. Candida albicans needs no outside source: it is resident flora of the mouth, genitalia, large "
    "intestine and skin.", "Histoplasma reservoir"),
   ("Decaying plant matter in soil",
    "Decaying plant matter in soil is the home of the saprobe Sporothrix schenckii, which enters through puncture "
    "wounds. Candida albicans lives on and in people, as normal flora of the mouth, genitalia, large intestine and "
    "skin.", "Sporothrix reservoir"),
   ("Alkaline, salty semiarid soils",
    "Alkaline, salty soils in semiarid, hot climates hold Coccidioides immitis, the cause of Valley fever. Candida "
    "albicans is a human resident, part of the normal flora of the mouth, genitalia, large intestine and skin.",
    "Coccidioides reservoir")],
  c(26, 30, 39, 51, 52, 53)),

Q("Candida", IO1,
  "A man with diabetes has the thick, white, adherent growth on the tongue shown. Which finding in a scraping "
  "would support a presumptive diagnosis?",
  ("Budding yeast cells and pseudohyphae",
   "Correct. A thick, white, adherent growth on the mucous membranes of the mouth in a man with diabetes is thrush, "
   "from Candida albicans. A presumptive diagnosis is made when budding yeast cells and pseudohyphae are found; "
   "growth on selective, differential media then tells the Candida species apart."),
  [("Encapsulated yeast on negative stain",
    "An encapsulated budding yeast on negative stain identifies Cryptococcus neoformans, which infects the lungs and "
    "meninges. Thrush on the tongue is Candida albicans, presumptively diagnosed by budding yeast cells with "
    "pseudohyphae.", "Cryptococcus finding"),
   ("Branched septate hyphae in sputum",
    "Branched septate hyphae, as seen in a sputum specimen, point to Aspergillus, whose spores form fungal balls in "
    "the lungs. A white oral growth calls for Candida's own finding: budding yeast cells and pseudohyphae.",
    "Aspergillus finding"),
   ("Cysts containing several bodies",
    "Cysts containing several bodies are the tissue form of Pneumocystis jirovecii, a cause of pneumonia in "
    "immunocompromised hosts. Thrush is a Candida albicans infection, supported by budding yeast cells and "
    "pseudohyphae.", "Pneumocystis finding")],
  c(18, 53, 55, 57, 59, 60) + " and image on Slide 54",
  img=IMG + "/l15-fig-05.jpg",
  alt="A tongue covered with thick, creamy white patches against red tissue.",
  slide="Slide 54"),

Q("Candida", IO1,
  "In which setting does cutaneous candidiasis typically occur?",
  ("Chronically moist skin and burns",
   "Correct. Cutaneous candidiasis occurs in chronically moist areas of skin and in burn patients; intertriginous "
   "lesions in the armpits, groin and under the breasts are common in obese patients. The resident yeast takes "
   "hold where skin stays damp or damaged."),
  [("Gritty nodules on scalp hairs",
    "Gritty, dark nodules on scalp hairs are black piedra, a superficial mycosis caused by Piedraia. Candida infects "
    "chronically moist skin, such as skin folds, and burned skin instead.", "black piedra site"),
   ("Skin punctured by thorns or wood",
    "A thorn or wood puncture introduces Sporothrix schenckii, which forms a nodule and spreads to nearby lymph "
    "nodes. Cutaneous candidiasis needs no puncture; it develops in chronically moist skin and in burn patients.",
    "Sporothrix entry"),
   ("Nail beds under nail extensions",
    "Nail extensions may give a dermatophyte a portal to the nail bed in tinea unguium. Cutaneous candidiasis is a "
    "disease of chronically moist skin, such as skin folds in obese patients, and of burns.",
    "tinea unguium portal")],
  c(39, 45, 49, 53, 54)),

Q("Candida", IO1,
  "Antibiotic therapy and catheters predispose patients to which opportunistic fungus?",
  ("Candida species",
   "Correct. Among the common opportunistic fungi, Candida is the one associated with antibiotic therapy and "
   "catheters, alongside diabetes, corticosteroids and immunosuppression. It is the dominant opportunistic pathogen "
   "and its infections are usually endogenous."),
  [("Aspergillus species",
    "Aspergillus is associated with leukemia, corticosteroids, tuberculosis, immunosuppression and intravenous drug "
    "abuse, not with antibiotic therapy or catheters. Those two predisposing conditions belong to Candida.",
    "Aspergillus predisposing list"),
   ("Cryptococcus species",
    "Cryptococcus is associated with diabetes, tuberculosis, cancer, corticosteroids and immunosuppression. "
    "Antibiotic therapy and catheters are the predisposing conditions tied to Candida.",
    "Cryptococcus predisposing list"),
   ("Fusarium species",
    "Fusarium is a mainly tropical soil mold that infects eyes through contaminated contact lenses, toenails, feet "
    "and burned skin. Antibiotic therapy and catheters are the predisposing conditions tied to Candida.",
    "other opportunist")],
  ci(9, 51, 52, 64)),

Q("Candida", IO1,
  "Which treatment is commonly used for systemic candidiasis?",
  ("Amphotericin B and azoles",
   "Correct. Topical antifungals are used for superficial Candida infections, while amphotericin B and azoles are "
   "commonly used for systemic infections. Systemic candidiasis is the overwhelming, potentially fatal form seen in "
   "seriously compromised hosts."),
  [("Topical antifungals alone",
    "Topical antifungals are used for superficial Candida infections such as skin irritation, not for systemic "
    "disease. A systemic infection in a seriously compromised host calls for amphotericin B and azoles.",
    "superficial treatment for systemic disease"),
   ("Pentamidine and co-trimoxazole",
    "Pentamidine and co-trimoxazole (trimethoprim-sulfamethoxazole) treat Pneumocystis pneumonia and are not "
    "traditional antifungal drugs. Systemic candidiasis is treated with antifungals, amphotericin B and azoles.",
    "Pneumocystis treatment"),
   ("Ultraviolet light treatment",
    "Ultraviolet light treatments, like debridement, have helped in dermatophytoses of keratinized skin. Systemic "
    "candidiasis is a deep, potentially fatal infection treated with amphotericin B and azoles.",
    "dermatophyte treatment")],
  c(45, 52, 55, 58)),

Q("Candida", IO1,
  "After a presumptive diagnosis of candidiasis, how are the Candida species told apart?",
  ("Selective, differential media",
   "Correct. A presumptive diagnosis rests on budding yeast cells and pseudohyphae, but growth on selective, "
   "differential media differentiates the Candida species. The smear shows a Candida infection; culture on these "
   "media names the species."),
  [("A negative stain for a capsule",
    "A negative stain demonstrates the capsule of an encapsulated budding yeast, the sign of Cryptococcus neoformans. "
    "Candida species are told apart by growth on selective, differential media.", "Cryptococcus test"),
   ("Wood's light on infected hairs",
    "Wood's light on hairs is a step in working up hair, skin and nail specimens, the territory of the "
    "dermatophytes. Candida species are separated by growth on selective, differential media.",
    "hair specimen test"),
   ("A potassium hydroxide mount",
    "A potassium hydroxide mount lyses human epithelial cells and leaves the thicker-walled fungal cells intact, "
    "showing that fungus is present. It reveals the yeast, but growth on selective, differential media is what "
    "differentiates the Candida species.", "detection confused with species identification")],
  ci(17, 18, 42, 55, 57)),

Q("Candida", IO1,
  "Which fungus is the dominant opportunistic pathogen?",
  ("Candida species",
   "Correct. Among the opportunistic mycoses, caused by fungi once considered harmless skin or air contaminants, "
   "Candida species are the dominant opportunistic pathogen. Candida albicans is the familiar one, and Candida "
   "auris is emerging as a serious cause of invasive candidiasis."),
  [("Aspergillus fumigatus",
    "Aspergillus fumigatus holds a narrower title: among the opportunists it accounts for most lung infections, and "
    "it is third on the World Health Organization critical list. The dominant opportunistic pathogen overall is "
    "Candida.", "lung superlative taken as overall"),
   ("Cryptococcus neoformans",
    "Cryptococcus neoformans holds a different title, the number one critical fungal pathogen on the World Health "
    "Organization priority list. As an opportunist overall, Candida species dominate.",
    "priority rank taken as dominance"),
   ("Rhizopus species",
    "Rhizopus, with Mucor, causes mucormycosis: usually harmless air contaminants that invade the nose, eyes, heart "
    "and brain in diabetes, leukemia or malnutrition. The dominant opportunistic pathogen is Candida.",
    "other listed opportunist")],
  c(51, 52, 56, 60, 63)),

# ============================================================== CRYPTOCOCCUS (slides 9, 56, 57)
Q("Cryptococcus", IO2,
  "Where is Cryptococcus neoformans found in the environment?",
  ("Soil near urban pigeon roosts",
   "Correct. Cryptococcus neoformans is a widespread encapsulated yeast that inhabits soil around pigeon roosts in "
   "urban areas, as well as soil containing decaying wood. Healthy humans are strongly resistant, so frank "
   "infection occurs in immunocompromised patients."),
  [("Alkaline, salty semiarid soil",
    "Alkaline, salty soils in semiarid, hot climates hold Coccidioides immitis, spread by drought, rain and "
    "windstorms. Cryptococcus neoformans lives instead in soil around urban pigeon roosts and in soil containing "
    "decaying wood.", "Coccidioides habitat"),
   ("Normal flora of mouth and skin",
    "Living as normal flora of the mouth and skin describes Candida albicans, whose infections are usually "
    "endogenous. Cryptococcus neoformans comes from the environment: soil around urban pigeon roosts and soil with "
    "decaying wood.", "Candida reservoir"),
   ("Rye and other cereal grains",
    "Rye and other grains contaminated by Claviceps fungi carry ergot, a cause of mycotoxicosis. Cryptococcus "
    "neoformans is an encapsulated yeast of the soil around urban pigeon roosts and decaying wood.",
    "toxin source")],
  c(30, 53, 56, 65)),

Q("Cryptococcus", IO1,
  "Why is frank cryptococcal infection seen mainly in immunocompromised patients?",
  ("Healthy humans strongly resist it",
   "Correct. Healthy humans are strongly resistant to Cryptococcus neoformans, so frank infection occurs in "
   "immunocompromised patients: those with human immunodeficiency virus infection or acquired immunodeficiency "
   "syndrome, cancer, immunosuppression, autoimmune disease, diabetes or cirrhosis."),
  [("It is confined to rural farmland",
    "Cryptococcus neoformans is widespread and inhabits soil around pigeon roosts in urban areas, so city dwellers "
    "are exposed too. Infection is limited to compromised hosts because healthy humans strongly resist it.",
    "exposure-limited"),
   ("It cannot grow at body temperature",
    "Being inhibited by the warmth of blood and viscera describes most subcutaneous fungi. Cryptococcus neoformans "
    "spreads from the lungs to the meninges and brain in compromised hosts; healthy people are protected by strong "
    "resistance.", "subcutaneous temperature limit borrowed"),
   ("A vaccine protects most people",
    "Immunization is typically ineffective against fungal infections because reinfection is exceedingly common. "
    "Protection against Cryptococcus neoformans comes from the strong natural resistance of healthy humans.",
    "vaccine belief")],
  c(19, 38, 56)),

Q("Cryptococcus", IO1,
  "In an immunocompromised patient, where does Cryptococcus neoformans spread after the lungs, with the gravest "
  "results?",
  ("The meninges and brain",
   "Correct. Lung infection by Cryptococcus neoformans brings cough, fever and lung nodules; dissemination to the "
   "meninges and the brain can cause severe neurological disturbance and death in compromised hosts."),
  [("Nearby lymph nodes",
    "Spread from a skin nodule to nearby lymph nodes is the lymphocutaneous form of sporotrichosis, which starts at a "
    "puncture wound. Cryptococcus neoformans moves from the lungs to the meninges and brain.",
    "Sporothrix spread"),
   ("The sinuses and ear canals",
    "Colonizing the sinuses, ear canals, eyelids and conjunctiva is typical of Aspergillus, alongside fungal balls in "
    "the lungs. Cryptococcus neoformans is feared for spreading to the meninges and brain.", "Aspergillus sites"),
   ("The nail beds of hands and feet",
    "Persistent colonization of the nails of the hands and feet, distorting the nail bed, is tinea unguium, a "
    "dermatophyte infection. Cryptococcus neoformans disseminates from the lungs to the meninges and brain.",
    "dermatophyte site")],
  c(39, 45, 56, 60)),

Q("Cryptococcus", IO1,
  "A negative stain of a specimen shows encapsulated budding yeast. Which organism does this demonstrate?",
  ("Cryptococcus neoformans",
   "Correct. A negative stain demonstrating encapsulated budding yeast is the picture of Cryptococcus neoformans, "
   "the widespread encapsulated yeast of pigeon-roost soil. Biochemical and serological testing are the best "
   "diagnostic tools for it."),
  [("Candida albicans",
    "Candida albicans also buds, but its presumptive diagnosis rests on budding yeast cells with pseudohyphae, not a "
    "capsule. The capsule outlined by a negative stain marks Cryptococcus neoformans.", "Candida morphology"),
   ("Aspergillus fumigatus",
    "Aspergillus is seen as branched septate hyphae, for example in a sputum specimen, not as a budding yeast. An "
    "encapsulated budding yeast on negative stain is Cryptococcus neoformans.", "Aspergillus morphology"),
   ("Pneumocystis jirovecii",
    "Pneumocystis jirovecii is a small, unicellular fungus seen in tissue as cysts containing several bodies. "
    "Encapsulated budding yeast on negative stain is Cryptococcus neoformans.", "Pneumocystis morphology")],
  ci(59, 17, 18, 55, 56, 57, 58)),

Q("Cryptococcus", IO1,
  "Which methods are the best tools for diagnosing cryptococcosis?",
  ("Biochemical and serological tests",
   "Correct. For cryptococcosis, biochemical and serological testing are the best diagnostic tools. A negative "
   "stain can demonstrate the encapsulated budding yeast, and systemic infection generally requires amphotericin B "
   "with fluconazole or another azole."),
  [("Inoculation of laboratory animals",
    "Animal inoculation is performed only to help diagnose systemic mycoses when other methods are unavailable or "
    "indeterminate. For cryptococcosis, the best tools are biochemical and serological tests.",
    "last-resort method"),
   ("Wood's light examination of hair",
    "Wood's light is used on hairs when working up hair, skin and nail specimens. Cryptococcosis, a lung and "
    "meningeal infection, is best diagnosed by biochemical and serological tests.", "hair specimen test"),
   ("A chest X-ray showing lung nodules",
    "A chest X-ray can mislead: Blastomyces multiplying in the lungs may be mistaken for lung cancer on it. "
    "Cryptococcus also causes lung nodules, but biochemical and serological tests are the best tools for diagnosis.",
    "imaging taken as diagnosis")],
  ci(17, 33, 56, 57)),

Q("Cryptococcus", IO1,
  "Which regimen does systemic cryptococcal infection generally require?",
  ("Amphotericin B plus an azole",
   "Correct. Systemic cryptococcal infection generally requires amphotericin B and fluconazole or another "
   "azole-type drug. Treatment protocols are well established for patients with human immunodeficiency virus "
   "infection, though the drugs may be unavailable in many countries."),
  [("Pentamidine plus co-trimoxazole",
    "Pentamidine, an antiprotozoal, and co-trimoxazole, an antibacterial, treat Pneumocystis pneumonia and are not "
    "traditional antifungals. Cryptococcosis is treated with the antifungals amphotericin B and fluconazole or "
    "another azole.", "Pneumocystis treatment"),
   ("Heat packs plus potassium iodide",
    "Heat packs and/or super-saturated potassium iodide treat sporotrichosis of the appendages and lungs, a "
    "subcutaneous mycosis. Systemic cryptococcosis, which can reach the brain, needs amphotericin B and an azole "
    "such as fluconazole.", "Sporothrix treatment"),
   ("Topical azoles for weeks",
    "Topical azoles applied for several weeks are the usual treatment for dermatophytoses of keratinized skin, hair "
    "and nails. A systemic infection such as cryptococcosis needs amphotericin B with fluconazole or another azole.",
    "dermatophyte treatment")],
  c(39, 45, 56, 57, 58)),

# ============================================================== PNEUMOCYSTIS (slides 58, 59)
Q("Pneumocystis", IO1,
  "Which drugs are common treatment options for Pneumocystis pneumonia?",
  ("Pentamidine and co-trimoxazole",
   "Correct. Pentamidine, an antiprotozoal, and the antibacterial co-trimoxazole (trimethoprim-sulfamethoxazole) "
   "are common treatment options, and neither is a traditional antifungal drug. Without such medication the "
   "pneumonia can be rapidly fatal."),
  [("Amphotericin B and azoles",
    "Amphotericin B and azoles are traditional antifungals, used for systemic candidiasis and, as amphotericin B "
    "with an azole, for cryptococcosis. Pneumocystis pneumonia is unusual: it is treated with pentamidine and "
    "co-trimoxazole, which are not traditional antifungals.", "standard antifungal assumed"),
   ("Topical azoles for several weeks",
    "Topical azoles for several weeks treat dermatophytoses of the skin, hair and nails. Pneumocystis pneumonia "
    "fills the lungs with secretions and is treated with pentamidine or co-trimoxazole.",
    "dermatophyte treatment"),
   ("Tissue removal and amphotericin B",
    "Removal of affected tissues plus amphotericin B is the treatment for mucormycosis invading the nose, eyes, heart "
    "and brain. Pneumocystis pneumonia is treated medically with pentamidine and co-trimoxazole.",
    "mucormycosis treatment")],
  c(45, 55, 57, 58, 63)),

Q("Pneumocystis", IO1,
  "On what basis do most scientists now classify Pneumocystis as a fungus rather than a protozoan?",
  ("Its genetic analysis",
   "Correct. The taxonomy of Pneumocystis is still debated, fungus or protozoan, but most scientists lean toward a "
   "fungal classification because of genetic analysis. Its usual drugs do not settle the question: one is an "
   "antiprotozoal and the other an antibacterial."),
  [("Its response to antifungals",
    "Pneumocystis is treated with pentamidine (antiprotozoal) and co-trimoxazole (antibacterial), which are not "
    "traditional antifungal drugs, so drug response cannot be the basis. Genetic analysis is what places it among "
    "the fungi.", "treatment taken as taxonomy"),
   ("Its growth as hyphae",
    "Pneumocystis is a small, unicellular fungus, seen in tissue as cysts containing several bodies, not as hyphae. "
    "Its fungal classification rests on genetic analysis.", "wrong morphology"),
   ("Its antibody titers",
    "Antibody titers show that human contact with Pneumocystis is very widespread and mostly asymptomatic; they do "
    "not show whether it is a fungus. The classification rests on genetic analysis.",
    "true fact answering a different question")],
  ci(59, 58)),

Q("Pneumocystis", IO1,
  "How does Pneumocystis pneumonia become rapidly fatal when it is not controlled?",
  ("Secretions in the lungs block breathing",
   "Correct. Pneumocystis pneumonia forms secretions in the lungs that block breathing; with cough, fever, shallow "
   "respiration and cyanosis, it can be rapidly fatal if not controlled with medication."),
  [("Fungal balls form in the lungs",
    "Fungal balls form when Aspergillus spores germinate in the lungs, and invasive aspergillosis can add necrotic "
    "pneumonia. Pneumocystis kills by filling the lungs with secretions that block breathing.",
    "Aspergillus lesion"),
   ("Spherules with endospores form nodules",
    "Spherules containing endospores and lung nodules come from inhaled Coccidioides arthrospores, and most such "
    "cases need no treatment at all. Pneumocystis pneumonia is deadly because its secretions block breathing.",
    "Coccidioides lesion"),
   ("Spread to the meninges and brain",
    "Dissemination to the meninges and brain is how Cryptococcus neoformans causes severe neurological disturbance "
    "and death. Pneumocystis does its damage in the lungs, where secretions block breathing.",
    "Cryptococcus spread")],
  c(30, 56, 58, 60)),

Q("Pneumocystis", IO2,
  "What does antibody-titer evidence suggest about human contact with Pneumocystis?",
  ("Widespread, mostly without symptoms",
   "Correct. Immunological evidence such as antibody titers suggests that human contact with Pneumocystis is very "
   "widespread and that most people remain asymptomatic. Disease develops in hosts at high risk, such as patients "
   "with acquired immunodeficiency syndrome or a kidney transplant."),
  [("Rare, mostly via kidney transplants",
    "Kidney transplant patients are at high risk for Pneumocystis pneumonia, which says who becomes ill, not where "
    "contact comes from. Antibody titers show that contact is very widespread and mostly asymptomatic.",
    "risk group confused with source"),
   ("Common, and usually causes pneumonia",
    "Most people in contact with Pneumocystis remain asymptomatic. Pneumonia, with secretions that block breathing, "
    "is the disease of high-risk hosts such as patients with acquired immunodeficiency syndrome.",
    "contact equated with disease"),
   ("Confined to immunocompromised hosts",
    "Contact is not confined to the immunocompromised: antibody titers show very widespread contact, mostly without "
    "symptoms. Patients with acquired immunodeficiency syndrome or kidney transplants are the ones at high risk of "
    "pneumonia.", "exposure confused with disease risk")],
  c(58)),

Q("Pneumocystis", IO1,
  "A kidney transplant recipient has cough, fever, shallow respiration and cyanosis. A tissue section shows the "
  "cysts seen here, each containing several bodies. Which organism is most likely?",
  ("Pneumocystis jirovecii",
   "Correct. Cysts containing several bodies are the tissue form of Pneumocystis jirovecii, a small, unicellular "
   "fungus. Kidney transplant patients are at high risk, and cough, fever, shallow respiration and cyanosis are its "
   "pneumonia, in which secretions block breathing."),
  [("Cryptococcus neoformans",
    "Cryptococcus neoformans appears as an encapsulated budding yeast on negative stain and causes cough, fever and "
    "lung nodules before spreading to the meninges. Cysts each holding several bodies identify Pneumocystis "
    "jirovecii.", "Cryptococcus morphology"),
   ("Aspergillus fumigatus",
    "Aspergillus grows as branched septate hyphae with conidial heads and forms fungal balls in the lungs. Rounded "
    "cysts containing several bodies, not hyphae, point to Pneumocystis jirovecii.", "Aspergillus morphology"),
   ("Blastomyces dermatitidis",
    "Blastomyces dermatitidis is a dimorphic true pathogen whose inhaled conidia become yeasts in the lungs, at times "
    "mistaken for lung cancer on chest X-ray. Cysts holding several bodies in a transplant recipient point to "
    "Pneumocystis jirovecii.", "true pathogen of the lungs")],
  ci(59, 18, 33, 36, 56, 57, 58, 62),
  img=IMG + "/l15-fig-06.jpg",
  alt="A stained tissue section crowded with round structures, each holding several small dark bodies.",
  slide="Slide 59"),

# ============================================================== ASPERGILLUS (slides 9, 18, 51, 60-62)
Q("Aspergillus", IO2,
  "How do people usually acquire Aspergillus infection of the lungs?",
  ("Breathing in airborne spores",
   "Correct. Aspergillus is a very common airborne soil fungus, and infection usually occurs in the lungs, where its "
   "spores germinate and form fungal balls. People at serious risk include those with human immunodeficiency virus "
   "infection, leukemia or a transplant."),
  [("Thorn or wood puncture wounds",
    "A thorn or wood puncture carries Sporothrix schenckii into the skin, where it forms a nodule and spreads to "
    "nearby lymph nodes. Aspergillus is airborne, and its spores germinate in the lungs.", "Sporothrix route"),
   ("Childbirth and breast-feeding",
    "Childbirth and breast-feeding, along with surgery and sexual contact, spread Candida albicans from person to "
    "person. Aspergillus comes from the air and soil; its spores reach the lungs and germinate there.",
    "Candida route"),
   ("Contact with public surfaces",
    "Public surfaces spread tinea pedis and tinea manuum, ringworm of the foot and hand. Aspergillus infection "
    "begins in the lungs, where its airborne spores germinate.", "dermatophyte route")],
  c(39, 45, 52, 60)),

Q("Aspergillus", IO1,
  "To what practice can the resistance of Aspergillus to azole fungicides be attributed?",
  ("Agricultural crop spraying",
   "Correct. Aspergillus is a very common airborne soil fungus, and its resistance to azole fungicides can be "
   "attributed to agricultural practices: spraying crops to prevent losses due to fungi."),
  [("Hospital disinfectant overuse",
    "Partial resistance to common disinfectants is a trait of Candida auris that keeps its hospital outbreaks going. "
    "Azole resistance in Aspergillus, an airborne soil fungus, traces to agricultural crop spraying.",
    "Candida auris trait"),
   ("Long topical courses for ringworm",
    "Topical azoles for several weeks are the usual treatment for dermatophytoses, but they are not where Aspergillus "
    "resistance is traced. That resistance is attributed to agricultural crop spraying.",
    "clinical azole use blamed"),
   ("Amphotericin B in transplant care",
    "Amphotericin B is not an azole; it forms complexes with fungal cell membrane lipids. Aspergillus resistance to "
    "azole fungicides is attributed to agricultural crop spraying.", "drug confusion")],
  c(19, 20, 45, 52, 60)),

Q("Aspergillus", IO1,
  "In a patient with leukemia, what do Aspergillus spores typically form in the lungs?",
  ("Fungal balls",
   "Correct. Aspergillus is a serious opportunistic threat in leukemia; infection usually occurs in the lungs, where "
   "spores germinate and form fungal balls. The fungus can also colonize the sinuses, ear canals, eyelids and "
   "conjunctiva."),
  [("Spherules with endospores",
    "Spherules containing endospores form in the lungs from inhaled arthrospores of Coccidioides immitis, the Valley "
    "fever fungus. Aspergillus spores germinating in the lungs form fungal balls.", "Coccidioides lesion"),
   ("Cysts with several bodies",
    "Cysts containing several bodies are the tissue form of Pneumocystis jirovecii, whose pneumonia fills the lungs "
    "with secretions. Aspergillus spores germinate in the lungs into fungal balls.", "Pneumocystis lesion"),
   ("Encapsulated yeast nodules",
    "Cough, fever and lung nodules with an encapsulated budding yeast describe Cryptococcus neoformans. Aspergillus "
    "grows as branched septate hyphae, and its spores germinating in the lungs form fungal balls.",
    "Cryptococcus lesion")],
  ci(59, 18, 30, 56, 57, 58, 60)),

Q("Aspergillus", IO1,
  "Which patients are at increased risk of invasive aspergillosis?",
  ("Transplant and cystic fibrosis patients",
   "Correct. Invasive aspergillosis can produce necrotic pneumonia and infection of the brain, heart and other "
   "organs, and transplant recipients (organ and bone marrow) are at increased risk, as are patients with cystic "
   "fibrosis."),
  [("Barefoot young male farmers",
    "Male farmers aged 11 to 30 who do not wear shoes fit the risk profile for eumycetoma, a deep tissue infection "
    "of poor countries. Invasive aspergillosis threatens transplant recipients and cystic fibrosis patients.",
    "eumycetoma profile"),
   ("Children lacking dietary protein",
    "Children with too little protein intake (kwashiorkor) can develop a gastrointestinal form of mucormycosis. "
    "Invasive aspergillosis is a risk for organ and bone marrow transplant recipients and cystic fibrosis patients.",
    "mucormycosis profile"),
   ("Obese patients with moist skin folds",
    "Obese patients develop intertriginous Candida lesions in the armpits, groin and under the breasts, where skin "
    "stays moist. Invasive aspergillosis targets transplant recipients and cystic fibrosis patients.",
    "Candida profile")],
  c(53, 54, 60, 63, 64)),

Q("Aspergillus", IO1,
  "Which pair of predisposing conditions is associated with Aspergillus?",
  ("Leukemia and intravenous drug abuse",
   "Correct. Aspergillus is associated with leukemia, corticosteroids, tuberculosis, immunosuppression and "
   "intravenous drug abuse. Leukemia also appears among the patients for whom Aspergillus is a serious "
   "opportunistic threat, with human immunodeficiency virus infection and transplants."),
  [("Antibiotic therapy and catheters",
    "Antibiotic therapy and catheters are the predisposing conditions tied to Candida, along with diabetes, "
    "corticosteroids and immunosuppression. Aspergillus is linked to leukemia, tuberculosis and intravenous drug "
    "abuse.", "Candida predisposing list"),
   ("Third-degree burns and intravenous therapy",
    "Third-degree burns and intravenous therapy predispose to the Zygomycota species, together with diabetes, cancer "
    "and corticosteroids. Aspergillus is linked to leukemia and intravenous drug abuse.",
    "Zygomycota predisposing list"),
   ("Kwashiorkor and malnutrition",
    "Malnutrition, including the protein deficiency kwashiorkor in children, sets the stage for mucormycosis. "
    "Aspergillus is associated with leukemia, corticosteroids, tuberculosis, immunosuppression and intravenous drug "
    "abuse.", "mucormycosis setting")],
  ci(9, 60, 63)),

Q("Aspergillus", IO1,
  "Besides the lungs, which sites can Aspergillus colonize?",
  ("Sinuses, ear canals, eyelids",
   "Correct. Aspergillus infection usually occurs in the lungs, but the fungus can also colonize the sinuses, ear "
   "canals, eyelids and conjunctiva. Invasive disease goes further, to the brain, heart and other organs."),
  [("Pubic and axillary hair shafts",
    "Whitish masses on pubic and axillary hair shafts are white piedra, caused by Trichosporon. Aspergillus, an "
    "airborne fungus, colonizes the sinuses, ear canals, eyelids and conjunctiva.", "white piedra site"),
   ("Lymph nodes near a thorn wound",
    "Lymph nodes near a puncture wound are reached by Sporothrix schenckii in lymphocutaneous sporotrichosis. "
    "Aspergillus colonizes the sinuses, ear canals, eyelids and conjunctiva besides the lungs.",
    "Sporothrix spread"),
   ("Moist skin folds under breasts",
    "Moist skin folds under the breasts, in the armpits and in the groin are where intertriginous Candida lesions "
    "form in obese patients. Aspergillus colonizes the sinuses, ear canals, eyelids and conjunctiva.",
    "Candida site")],
  c(39, 49, 54, 60)),

# ============================================================== MUCORMYCOSIS & OTHER OPPORTUNISTS (slides 9, 63, 64)
Q("Mucormycosis & other opportunists", IO1,
  "Which fungi are most often involved in mucormycosis?",
  ("Rhizopus and Mucor species",
   "Correct. Mucormycosis (zygomycosis) is caused most often by Rhizopus and Mucor species, members of the Division "
   "Zygomycota: extremely abundant saprobes in soil, water, organic debris and spoiled food that are usually "
   "harmless air contaminants."),
  [("Trichosporon and Piedraia species",
    "Trichosporon and Piedraia cause the white and black piedras, superficial masses and nodules on hair shafts. "
    "Mucormycosis, an invasive opportunistic infection, comes from the Zygomycota genera Rhizopus and Mucor.",
    "piedra agents"),
   ("Trichophyton and Microsporum",
    "Trichophyton and Microsporum are dermatophytes confined to keratinized skin, hair and nails. Mucormycosis "
    "invades the membranes of the nose, eyes, heart and brain and is caused mostly by Rhizopus and Mucor.",
    "dermatophyte genera"),
   ("Claviceps and Stachybotrys",
    "Claviceps makes ergot on rye, and Stachybotrys chartarum is the black mold of sick building syndrome, very "
    "different from mucormycosis despite a shared black mold nickname. Mucormycosis is caused by Rhizopus and "
    "Mucor.", "black mold nickname confusion")],
  c(42, 49, 63, 65)),

Q("Mucormycosis & other opportunists", IO2,
  "Where do the Zygomycota fungi behind mucormycosis live?",
  ("Soil, water, debris, spoiled food",
   "Correct. Members of the Division Zygomycota, including Rhizopus and Mucor, are extremely abundant saprobic fungi "
   "in soil, water, organic debris and spoiled food. They are usually harmless air contaminants that may invade the "
   "membranes of people with diabetes, leukemia or malnutrition."),
  [("Mouth, genitals, gut and skin",
    "Living as normal flora of the mouth, genitalia, large intestine or skin describes Candida albicans. The "
    "Zygomycota live in the environment, in soil, water, organic debris and spoiled food, and reach people as air "
    "contaminants.", "Candida reservoir"),
   ("Keratinized skin, hair and nails",
    "Keratinized skin, hair and nails are the home ground of the dermatophytes. The Zygomycota that cause "
    "mucormycosis are environmental saprobes of soil, water, organic debris and spoiled food.",
    "dermatophyte habitat"),
   ("Scalp and axillary hair shafts",
    "Hair shafts carry the piedras: black piedra on scalp hairs and white piedra on pubic or axillary hair. The "
    "Zygomycota are abundant saprobes of soil, water, organic debris and spoiled food.", "piedra habitat")],
  c(42, 49, 53, 63)),

Q("Mucormycosis & other opportunists", IO1,
  "Which factors may have contributed to the rise of mucormycosis in India?",
  ("Steroid misuse and uncontrolled diabetes",
   "Correct. Mucormycosis has become a big concern in India over the last few years, and injudicious use of "
   "respiratory steroids and uncontrolled diabetes may have contributed. Rhino-orbital-oral-cerebral disease has "
   "been documented."),
  [("Agricultural spraying of azole fungicides",
    "Crop spraying is blamed for azole resistance in Aspergillus, a different airborne soil fungus. The rise of "
    "mucormycosis in India is linked to injudicious respiratory steroid use and uncontrolled diabetes.",
    "Aspergillus resistance driver"),
   ("Contaminated contact lenses in the eye",
    "Contaminated contact lenses let Fusarium, a mainly tropical soil mold, infect the eye. Mucormycosis in India is "
    "tied to respiratory steroids used injudiciously and to uncontrolled diabetes.", "Fusarium route"),
   ("Damp buildings harboring toxic mold",
    "Damp buildings are linked to Stachybotrys chartarum and sick building syndrome, which carries a black mold "
    "nickname but is very different from mucormycosis. In India, steroid misuse and uncontrolled diabetes are the "
    "suspected contributors.", "black mold nickname confusion")],
  c(60, 63, 64, 65)),

Q("Mucormycosis & other opportunists", IO1,
  "Along with amphotericin B, what does treatment of mucormycosis involve?",
  ("Removal of affected tissues",
   "Correct. Treatment of mucormycosis involves removal of affected tissues plus amphotericin B. Surgical removal of "
   "damaged tissue is necessary in some fungal infections, and mucormycosis, which invades the nose, eyes, heart and "
   "brain with severe consequences, is one of them."),
  [("Heat packs over the lesions",
    "Heat packs, with or without super-saturated potassium iodide, are used for sporotrichosis of the appendages and "
    "lungs. Invasive mucormycosis is treated by removing affected tissues and giving amphotericin B.",
    "Sporothrix treatment"),
   ("Ultraviolet light treatments",
    "Ultraviolet light treatments, like debridement, have helped in dermatophytoses of the keratinized skin. "
    "Mucormycosis invades deep membranes and needs removal of affected tissue with amphotericin B.",
    "dermatophyte treatment"),
   ("Immunizing close contacts",
    "Immunization is typically ineffective against fungal infections because reinfection is exceedingly common, and "
    "most fungal infections are not communicable to other persons. Treatment combines tissue removal with "
    "amphotericin B.", "vaccine belief")],
  c(12, 19, 39, 45, 63)),

Q("Mucormycosis & other opportunists", IO2,
  "How can Fusarium reach and infect the eye?",
  ("Through contaminated contact lenses",
   "Correct. Fusarium species, a mainly tropical soil mold, occasionally infect the eyes, for example through "
   "contaminated contact lenses, as well as toenails, feet and burned skin, and can result in severe disability and "
   "death."),
  [("From close person-to-person contact",
    "Most fungal infections are not communicable; person-to-person spread is the pattern of the dermatophytes and "
    "Candida, which live on the human body. Fusarium, a soil mold, reaches the eye through contaminated contact "
    "lenses.", "assumed contagious"),
   ("Spread from the nose in diabetes",
    "Invasion of the nose, eyes, heart and brain in people with diabetes, leukemia or malnutrition is the pattern of "
    "mucormycosis from Rhizopus and Mucor. Fusarium reaches the eye through contaminated contact lenses.",
    "mucormycosis pattern"),
   ("Eating grain contaminated by it",
    "Eating grains, corn or peanuts contaminated by fungi causes mycotoxicoses such as aflatoxin poisoning, an "
    "intoxication rather than an eye infection. Fusarium infects the eye through contaminated contact lenses.",
    "mycotoxin route")],
  c(12, 63, 64, 65)),

Q("Mucormycosis & other opportunists", IO1,
  "Which person best fits the risk profile for eumycetoma?",
  ("A barefoot 20-year-old male farmer",
   "Correct. Eumycetomas, deep tissue infections, are especially prevalent in poor countries, with risk factors of "
   "male sex, age 11 to 30 years, farming and not wearing shoes. Long-term antifungal drug therapy and amputation "
   "may be required for full resolution."),
  [("A 60-year-old road worker in dust",
    "Increasing age and occupational exposure to dust or soil, as in road construction, are risk factors for "
    "Coccidioides immitis in the southwestern United States. Eumycetoma favors young male farmers, 11 to 30 years "
    "old, who go without shoes.", "Coccidioides profile"),
   ("A 45-year-old poorly fed harvester",
    "A poorly nourished harvester over 40 fits paracoccidioidomycosis of Central and South America. "
    "Eumycetoma's profile is younger: male, 11 to 30 years old, farming and not wearing shoes.",
    "Paracoccidioides profile"),
   ("A kidney transplant recipient",
    "Kidney transplant patients are at high risk for Pneumocystis pneumonia, an opportunist of the lungs. Eumycetoma "
    "is a deep tissue infection of young male farmers, 11 to 30 years old, who do not wear shoes.",
    "Pneumocystis profile")],
  c(30, 37, 58, 64)),

# ============================================================== FUNGAL ALLERGIES & TOXINS (slide 65)
Q("Fungal allergies & toxins", IO1,
  "Farmer's lung, teapicker's lung and bark stripper's disease are examples of which kind of illness?",
  ("Hypersensitivity to fungal spores",
   "Correct. Fungal spores are common sources of atopic allergies or hypersensitivities, and farmer's lung, "
   "teapicker's lung and bark stripper's disease are grouped with seasonal allergies and asthma rather than with "
   "infections or the toxin-caused mycotoxicoses."),
  [("Mycotoxicosis from eaten toxins",
    "Mycotoxicoses come from ingesting or inhaling fungal toxins, such as aflatoxin in grains, corn and peanuts or "
    "ergot on rye. Farmer's lung and its relatives are atopic allergies (hypersensitivities) to fungal spores.",
    "toxin illness confused with allergy"),
   ("Invasive opportunistic mycosis",
    "Invasive opportunistic mycoses, such as aspergillosis or mucormycosis, need impaired host defenses and tissue "
    "invasion. Farmer's lung, teapicker's lung and bark stripper's disease are hypersensitivities to fungal spores.",
    "infection confused with allergy"),
   ("Subcutaneous mycosis from trauma",
    "Subcutaneous mycoses follow trauma that carries fungi into the skin, as with sporotrichosis from thorns. These "
    "occupational lung conditions are hypersensitivity reactions to fungal spores, grouped with seasonal allergies "
    "and asthma.", "infection confused with allergy")],
  c(38, 60, 63, 65)),

Q("Fungal allergies & toxins", IO2,
  "How do mycotoxicoses usually arise?",
  ("Ingesting or inhaling fungal toxins",
   "Correct. Mycotoxicoses are usually caused by ingesting or inhaling fungal toxins. Examples are aflatoxin on "
   "grains, corn and peanuts and ergot on rye or other grains contaminated by Claviceps fungi; they are "
   "intoxications, not infections."),
  [("Fungi invading through broken skin",
    "Fungi entering through traumatized skin cause subcutaneous mycoses such as sporotrichosis, which are "
    "infections. Mycotoxicoses are intoxications by fungal toxins that are ingested or inhaled.",
    "infection route"),
   ("Spores provoking a hypersensitivity",
    "Fungal spores provoking hypersensitivity, as in farmer's lung, cause atopic allergies, a separate category. "
    "Mycotoxicoses are poisonings by fungal toxins taken in by ingestion or inhalation, such as aflatoxin and "
    "ergot.", "allergy confused with intoxication"),
   ("Overgrowth of resident yeast flora",
    "Overgrowth of resident yeast is the usual, endogenous origin of Candida albicans infection. A mycotoxicosis is "
    "an intoxication: the person ingests or inhales a fungal toxin, as with aflatoxin or ergot.",
    "endogenous infection")],
  c(38, 52, 65)),

Q("Fungal allergies & toxins", IO1,
  "Which effects characterize aflatoxin, the toxin found on grains, corn and peanuts?",
  ("Hepatotoxic and carcinogenic",
   "Correct. Aflatoxin, found on grains, corn and peanuts, is hepatotoxic and carcinogenic. It is lethal to poultry "
   "and livestock, especially turkeys, ducklings, pigs and calves, and in humans it may be a co-factor in liver "
   "cancer."),
  [("Mind-altering, like lysergic acid",
    "Mind-altering lysergic acid is linked to ergot, found on rye and other grains contaminated by Claviceps fungi. "
    "Aflatoxin's harm falls on the liver: it is hepatotoxic, carcinogenic and a possible co-factor in liver cancer.",
    "ergot effect"),
   ("Hematologic and neurological harm",
    "Severe hematologic and neurological damage is attributed to Stachybotrys chartarum, the black mold of sick "
    "building syndrome. Aflatoxin from grains, corn and peanuts is hepatotoxic and carcinogenic.",
    "Stachybotrys effect"),
   ("Hypersensitivity of the lungs",
    "Lung hypersensitivity, as in farmer's lung, is an atopic allergy to fungal spores rather than a toxin effect. "
    "Aflatoxin is a fungal toxin that is hepatotoxic and carcinogenic.", "allergy effect")],
  c(65)),

Q("Fungal allergies & toxins", IO1,
  "Which fungus is linked to sick building syndrome?",
  ("Stachybotrys chartarum",
   "Correct. Stachybotrys chartarum is linked to sick building syndrome (damp building-related illness) and can "
   "cause severe hematologic and neurological damage; it is nicknamed black mold but is very different from "
   "mucormycosis. Not all molds in buildings are toxic, and not all illnesses in buildings are due to fungi."),
  [("Rhizopus and Mucor species",
    "Rhizopus, with Mucor, causes mucormycosis, which also goes by a black mold nickname but is a very different "
    "disease: invasion of the nose, eyes, heart and brain in compromised hosts. Sick building syndrome is tied to "
    "Stachybotrys chartarum.", "black mold nickname confusion"),
   ("Claviceps species on rye",
    "Claviceps fungi contaminate rye and other grains with ergot, the source of mind-altering lysergic acid. The "
    "damp-building illness is tied to Stachybotrys chartarum.", "ergot fungus"),
   ("Fusarium, a tropical mold",
    "Fusarium is a mainly tropical soil mold that infects eyes through contaminated contact lenses, toenails, feet "
    "and burned skin. Sick building syndrome is linked to Stachybotrys chartarum.", "other mold")],
  c(63, 64, 65)),

]
