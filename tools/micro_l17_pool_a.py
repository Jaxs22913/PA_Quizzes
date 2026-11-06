# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 17 — Parasites of Medical Importance (Dr. Webster, 6 November 2026), pool A: deck
# slides 1-54 — the parasitology overview (slides 9, 10, 12, 13 and 14), the amebas (Entamoeba histolytica,
# Naegleria fowleri, Acanthamoeba), the intestinal ciliate (Balantidium coli), the flagellates (Trichomonas
# vaginalis, Giardia lamblia) and the hemoflagellates (Trypanosoma brucei, Trypanosoma cruzi, Leishmania), plus
# these organisms' rows on the summary tables of slides 4-5. The other pool files (tools/micro_l17_pool_b.py and
# onward) hold the apicomplexans and the helminths (slides 55-131).
#
# ATTRIBUTION: the deck file is "Lecture 16 Dr. Webster Parasites of Medical Importance.pptx" (her file name; the
# site calls it Lecture 17), 131 slides; the title slide names no lecturer.
#
# PHASE 1, FROM THE SLIDES, with the recording notes the builder relayed from part 1 of the 6 November recording
# (stage names not tested; the smear picture keyed only to the genus; no drug names; "water treatment is the best
# prevention"; "vector control is the best way"; slides 13, 14 (tables), 25-27 and 30 are charts not to memorize).
# Every key and every explanation is from the VISIBLE slides, text and pictures; the speaker notes are not used. Picture-only content used: slides 4-5 (the
# summary tables: Entamoeba "Fecal oral route", Naegleria "prevalent in Florida's freshwater lakes", Balantidium
# "Pigs and cattle as alternate hosts", Giardia "Common in campers", Trichomonas "Most common curable STD in young
# women", Trypanosoma brucei "Tse tse fly as vector", Trypanosoma cruzi "becoming an issue in Southern US as vector
# expands its range", Leishmania "Dog alternate host, sand fly is vector", Plasmodium "Anopheles Mosquito" and the
# ring-form photo, Toxoplasma "pregnant women should not clean catbox"), 7 (Trichinella "ingestion of undercooked
# pork", used only in explanations), 18 (the Entamoeba cycle: cysts eaten, pass through the stomach, trophozoites
# released in the small intestine, encyst in the large intestine, cysts in feces), 20 (the ameboma photograph),
# 22 (the abdominal-wall abscess; quiz picture l17-fig-01.jpg), 32 (the Acanthamoeba cycle: entry through the eye,
# the nasal passages or broken skin; granulomatous amebic encephalitis in compromised immune systems), 34 (the
# Balantidium drawings with "Cilia tufts"; l17-fig-02.jpg), 36 (the trichomonad drawing: flagella, undulating
# membrane), 38 (l17-fig-03.jpg), 40 (the Giardia drawing; l17-fig-04.jpg), 45 (the tsetse cycle panels: "The saliva
# of a fly infected with T. brucei inoculates the human bloodstream"), 46 (l17-fig-05.jpg), 50 (the reduviid cycle,
# "Cycle in wild animals"), 51 (Romana's sign; l17-fig-06.jpg), 54 (the Leishmania cycle). Facts from slides 55
# (apicomplexans), 75 (Cyclospora, fresh produce and water), 81 and 100 (larvae penetrating skin) and 85 (helminth
# cuticle) appear only in explanations, as the replacing fact for a distractor. No item rests on a cell of the
# slide-13 or slide-14 tables; only the slide-14 bullet text is asked.
#
# Four options throughout. KEYS SHORT and explanations FULL. Every key is authored at position 0 with the only
# "Correct." opener; the partition rotates positions per set (the one QO item, the drug-number comparison, is
# ordered and never rotated). `mis` names the misconception each distractor stands for (review metadata; the
# renderer strips it). About 40% of items are objective 2 (how humans acquire the parasite).
#
# DELIBERATELY NOT ASKED (held), and why:
#   - WHICH DRUG treats what, every dose and every drug mechanism (slides 14, 23, 29-31, 33, 38, 41, 47, 49, 53),
#     including Table 23.2's footnote "Metronidazole ... is selectively toxic to anaerobic protozoa like Entamoeba,
#     Giardia, and Trichomonas, which lack mitochondria": Dr. Webster said in Lectures 10 and 14 she does not test
#     which antibiotics. The general slide-14 facts (relatively few, work against eukaryotic cells, toxicity and
#     severe side effects) ARE asked, as are non-drug methods (water treatment, nose plugs, unchlorinated water,
#     vector control, "must be early", "vaccine under development").
#   - NUMBERS: 20% of infectious diseases (9), 100,000 species and 25 pathogens (12), 10% carriers and 100,000
#     deaths (16), 4 trophozoites per cyst and 90% asymptomatic (19), 10% fatality (21), the Naegleria case lists,
#     maps and statistics (24-27, held whole by the brief, with slide 27's "brain-eating amoeba" nickname), 46% of
#     Florida lakes and death in 3-7 days (29), 2-3% survival (31), the 4 anterior flagella and 3 human species (36),
#     Trichomonas case counts, 60-70% asymptomatic, 4-28 day incubation, 4.3% resistance, 2-3X cervical cancer risk
#     and 50% more HIV transmission (37-38; only the direction "raises cervical cancer risk" is keyed), 10-100 cysts
#     and 2-month survival (39), over 100 antigens and 3-4 weeks (46; keyed only as "weeks" against "years"), the
#     National Institutes of Health Chagas estimates (48), 30-40% of heart disease (49), the leishmaniasis country
#     and case counts (52), the "Small bite, big threat" year (12). A few appear as context in explanations only.
#   - "PAM": slide 29 expands it "Primary Acute Meningoencephalitis" (as does slide 4's table), slide 30 and the
#     slide-24 map "primary amebic meningoencephalitis"; items say "Naegleria meningoencephalitis".
#   - Acanthamoeba and contact lenses: slide 4's table writes "Found in contact lens wearers" in the granulomatous
#     amebic encephalitis row, while slide 31 ties contact lens wearers to amebic keratitis and gives "break in skin
#     or ... nasal passages" for the encephalitis (the slide-32 cycle agrees). Keyed per slides 31-32: contact
#     lenses -> keratitis; broken skin or nasal passages -> encephalitis.
#   - the four hemoflagellate STAGE NAMES (amastigote, promastigote, epimastigote, trypomastigote; slides 42-44 and
#     the slide-43 table): recording, "I am not going to be asking about the names of these four stages". No key or
#     option names a stage, and no stem asks for a stage in other words; the Hemoflagellates topic asks the other
#     slide-42 facts (complicated life cycles with morphological changes; spread by blood-sucking insects that
#     serve as intermediate hosts).
#   - the SPECIES on the trypanosome smear (l17-fig-05): recording, "I would not ask you to differentiate between
#     the picture of cruzi and gambiense. So as long as you knew trypanosoma, I would be a happy camper." The
#     picture item keys the genus Trypanosoma and offers no Trypanosoma species.
#   - the slide-13 table (protozoa, reservoirs and sources) and the slide-14 Table 23.2: recording, "a chart I am
#     not asking you to memorize". Their facts are used only where another slide states them too (slides 4-5, 16,
#     33, 37, 39, 45, 52, 75).
#   - Trypanosoma brucei's route into the human: slide 43 puts one stage in the tsetse SALIVARY GLAND and the
#     infective one in the BITING MOUTHPARTS; slide 45's figure says "the saliva of a fly infected with T. brucei
#     inoculates the human bloodstream"; slide 46 says the bite "inoculates skin". Saliva against mouthparts, and
#     skin against bloodstream, are never asked ("saliva" appears only as the tsetse distractor in the Trypanosoma
#     cruzi transmission item, worded from slide 45).
#   - Trypanosoma cruzi tissue sites: slide 43 "macrophages, liver, heart, spleen", slide 49 "heart muscle and
#     large intestine"; slide 49's pair is used only as a distractor for Trypanosoma brucei's organs.
#   - "Chagoma": slide 49 calls Romana's sign "also called chagoma"; the sign is keyed as "Romana's sign", and
#     chagoma appears only as a distractor described in the slide's own words.
#   - kala azar against the systemic (visceral) form: slide 53 lists them on separate lines and never equates them,
#     so a fever-and-organomegaly vignette is NOT keyed "kala azar"; only "the most severe and fatal form if
#     untreated" is.
#   - Entamoeba "sometimes sexually transmitted" (17): true on the slide, so it is never a distractor; the keyed
#     route is fecal-oral (slides 4, 13, 18, 19).
#   - leishmaniasis-malaria co-infection: only "may make diagnosis difficult" is used, never severity.
#   - the Centers for Disease Control and Prevention list of five neglected diseases is used only in an
#     explanation; the three criteria are asked.
#   - self-contradictions found in this range besides the brief's: Naegleria "only about 200 cases reported
#     worldwide" (slide 4) against "Global confirmed cases through 2018: 381" (slide 27) (numbers, held anyway);
#     the PAM expansion on slide 4 matches slide 29, not slide 30.
# SPELLING: the deck's "Tryponosoma" is written Trypanosoma, "Leishmani" Leishmania, "amoebic", "amoebas",
# "amoebomas" and "Amoebic keratitis" amebic, amebas, amebomas and amebic keratitis (US spelling; the genus names
# Entamoeba and Acanthamoeba are kept); "Tse tse" is tsetse; "Romana's sign" is kept as the slides write it
# (Romaña); "kala azar" as written; no drug name is used, so the misspelled drug names are moot.
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


POOL_A = [

# ============================================================== PARASITOLOGY OVERVIEW (slides 9, 10, 12, 13, 14)
QO("Parasitology overview", IO1,
   "How does the number of antiprotozoan drugs compare with the number of antibacterial agents?",
   [("Relatively few",
     "Correct. Antiprotozoan drugs are relatively few in comparison with antibacterial agents. Protozoa are "
     "single-celled, animal-like eukaryotic parasites, so these drugs must work against eukaryotic cells, and they "
     "bring toxicity problems and severe side effects as well.",
     None),
    ("About as many",
     "The two groups are not matched in size: antiprotozoan drugs are relatively few in comparison with "
     "antibacterial agents. What sets them apart is that they work against eukaryotic cells, the cell type of "
     "protozoa, and carry toxicity problems and severe side effects.",
     "equal supply assumed"),
    ("Somewhat more",
     "Antiprotozoan drugs do not outnumber antibacterial agents at all; they are relatively few by comparison. "
     "Their other defining features are that they work against eukaryotic cells and have toxicity problems with "
     "severe side effects.",
     "supply overestimated"),
    ("Many more",
     "This reverses the comparison: antibacterial agents are the larger group, and antiprotozoan drugs are "
     "relatively few beside them. Antiprotozoan drugs also work against eukaryotic cells and carry toxicity "
     "problems and severe side effects.",
     "comparison reversed")],
   0, c(9, 12, 14)),

Q("Parasitology overview", IO1,
  "Which drawback do antiprotozoan drugs share as a group?",
  ("Toxicity and severe side effects",
   "Correct. Antiprotozoan drugs have toxicity problems and severe side effects. They work against eukaryotic "
   "cells (protozoa are eukaryotic parasites), and they are relatively few in comparison with antibacterial "
   "agents, so both their number and their safety are limited."),
  [("No activity against eukaryotic cells",
    "This reverses a defining feature: antiprotozoan drugs work against eukaryotic cells, which is what protozoa, "
    "single-celled animal-like microbes, are. The drawback they share is toxicity problems and severe side "
    "effects.",
    "target cell type reversed"),
   ("Resistance in most protozoan strains",
    "Drug resistance is noted for particular organisms (increasing in malaria, a small share of Trichomonas "
    "strains), not as a trait of protozoa in general. What antiprotozoan drugs share as a group is toxicity "
    "problems with severe side effects, and they are relatively few in number.",
    "one organism's resistance generalized"),
   ("Loss of effect from antigenic variation",
    "Antigenic variation is how Trypanosoma brucei evades the host's immune response; it describes the parasite "
    "against immunity, not a property of the drugs. Antiprotozoan drugs as a group carry toxicity problems and "
    "severe side effects.",
    "immune evasion confused with drug failure")],
  c(9, 12, 14, 38, 46, 61)),

Q("Parasitology overview", IO1,
  "Parasitic infections are less prevalent in industrialized countries. In which patients are they increasingly "
  "common?",
  ("Immunocompromised patients",
   "Correct. Parasitology, the study of eukaryotic parasites (protozoa and helminths), notes that these infections "
   "are less prevalent in industrialized countries but increasingly common in patients with human "
   "immunodeficiency virus infection and other immunocompromised patients."),
  [("Contact lens wearers",
    "Contact lens wearers are the group at risk of amebic keratitis from Acanthamoeba, one organism and one eye "
    "infection. Across parasitic infections, the rising group is immunocompromised patients, such as those with "
    "human immunodeficiency virus infection.",
    "one organism's risk group generalized"),
   ("Pregnant women",
    "Pregnant women are warned about Toxoplasma gondii because of the danger of transplacental transmission to the "
    "fetus, so they should not clean the cat box; that is a specific danger, not a rising rate. Parasitic "
    "infections are increasingly common in immunocompromised patients.",
    "Toxoplasma warning generalized"),
   ("Young, sexually active women",
    "Trichomoniasis is the most common curable sexually transmitted disease in young, sexually active women, a "
    "fact about one protozoan. Parasitic infections as a whole are increasingly common in human immunodeficiency "
    "virus infection and other immunocompromised patients.",
    "Trichomonas risk group generalized")],
  c(5, 9, 31, 37)),

Q("Parasitology overview", IO1,
  "The Centers for Disease Control and Prevention set priorities among neglected parasitic infections using three "
  "criteria. Which is one of them?",
  ("Severity of the illness",
   "Correct. The Centers for Disease Control and Prevention ranked neglected parasitic infections for public "
   "health action by the number of people infected, the severity of illness, and the ability to prevent and "
   "treat. Chagas disease, cysticercosis, toxocariasis, toxoplasmosis and trichomoniasis made the list."),
  [("Number of species in the group",
    "Species counts describe the protozoa as a whole, of which only a small share are important pathogens; they "
    "were not a criterion. The criteria count people infected, not species, plus severity of illness and the "
    "ability to prevent and treat.",
    "species count confused with people infected"),
   ("Spread by a blood-sucking insect",
    "Vector-borne spread is the threat the World Health Organization stressed with its slogan \"Small bite, big "
    "threat,\" not a priority criterion here, and the list includes trichomoniasis, a sexually transmitted "
    "disease. The criteria are people infected, severity of illness, and ability to prevent and treat.",
    "World Health Organization vector theme borrowed"),
   ("Ability to infect other mammals",
    "Zoonotic spread, as in the hemoflagellates, is not one of the criteria, and trichomoniasis on the list has a "
    "human reservoir. The three criteria are the number of people infected, the severity of illness, and the "
    "ability to prevent and treat.",
    "zoonosis mistaken for a criterion")],
  c(10, 12, 37, 42)),

# ============================================================== ENTAMOEBA HISTOLYTICA (slides 4, 13, 16-23)
Q("Entamoeba histolytica", IO2,
  "How do humans usually acquire Entamoeba histolytica?",
  ("Swallowing cysts in food or water",
   "Correct. Entamoeba histolytica spreads by the fecal-oral route: cysts are eaten with food or water, pass "
   "through the stomach and release trophozoites in the small intestine, and new cysts leave in the feces. Humans "
   "are the primary hosts, spread is tied to fertilization practices and sewage treatment, and water treatment "
   "prevents it."),
  [("Nasal contact with fresh water",
    "Water forced into the nose is how Naegleria fowleri is acquired, by diving, waterskiing or rinsing the "
    "sinuses; its trophozoite then follows the olfactory nerve to the brain. Entamoeba histolytica is swallowed, "
    "as cysts in fecally contaminated food or water.",
    "Naegleria route borrowed"),
   ("The bite of a blood-sucking insect",
    "Blood-sucking insects (tsetse flies, reduviid bugs, sand flies) spread the hemoflagellates, parasites of blood "
    "and tissues. Entamoeba histolytica is an intestinal ameba acquired by swallowing its cysts by the fecal-oral "
    "route.",
    "hemoflagellate route borrowed"),
   ("Eating larvae in undercooked pork",
    "Undercooked pork transmits Trichinella spiralis, a worm whose larvae encyst in muscle. Entamoeba histolytica "
    "is a protozoan with no larval stage; people swallow its cysts in food or water contaminated with feces.",
    "helminth route borrowed")],
  c(4, 7, 16, 17, 18, 19, 23, 28, 42)),

Q("Entamoeba histolytica", IO1,
  "Where do swallowed cysts of Entamoeba histolytica release their trophozoites?",
  ("Small intestine",
   "Correct. Swallowed cysts pass through the stomach and arrive at the small intestine, where alkaline pH and "
   "digestive juices stimulate each cyst to release trophozoites. These attach, multiply, move about and feed; "
   "later trophozoites encyst in the large intestine and the cysts leave in the feces."),
  [("Stomach",
    "The cysts pass through the stomach unchanged; release needs the alkaline pH and digestive juices of the small "
    "intestine. The stomach is a transit point in the cycle, not the place where the trophozoites emerge.",
    "transit point taken for the release site"),
   ("Large intestine",
    "The large intestine is where trophozoites encyst before cysts leave in the feces, and intestinal amebiasis "
    "targets the cecum, appendix, colon and rectum. Release from swallowed cysts happens earlier, in the small "
    "intestine.",
    "encystment site confused with release site"),
   ("Liver",
    "The liver is the organ most often invaded outside the intestine, where trophozoites form abscesses (amebic "
    "hepatitis). That is a later, extraintestinal step after invasion; swallowed cysts release their trophozoites "
    "in the small intestine.",
    "extraintestinal site confused with the cycle")],
  c(18, 19, 20, 21)),

Q("Entamoeba histolytica", IO1,
  "What is the tumorlike growth that can complicate intestinal amebiasis called?",
  ("Ameboma",
   "Correct. The life-threatening manifestations of intestinal amebiasis are hemorrhage, perforation, appendicitis "
   "and tumorlike growths called amebomas. The ameba targets the cecum, appendix, colon and rectum and may secrete "
   "enzymes that dissolve tissue and penetrate deeper layers of the mucosa."),
  [("Chagoma",
    "Chagoma is the name given to the local lesion of Chagas disease, Romana's sign, a swelling of the eyelid with "
    "conjunctivitis. A tumorlike growth in the bowel that complicates intestinal amebiasis is an ameboma.",
    "lesion of another protozoan"),
   ("Primary chancre",
    "A primary chancre develops in the skin where a tsetse fly inoculates Trypanosoma brucei. "
    "The tumorlike growth that complicates intestinal amebiasis, inside the bowel, is an ameboma.",
    "African trypanosome lesion"),
   ("Baghdad boil",
    "A Baghdad boil (oriental sore) is the localized ulcerated skin sore of cutaneous leishmaniasis. It sits on the "
    "skin, whereas the tumorlike growth of intestinal amebiasis is an ameboma, in the bowel the ameba targets "
    "(cecum, appendix, colon, rectum).",
    "Leishmania lesion")],
  c(20, 46, 49, 53)),

Q("Entamoeba histolytica", IO1,
  "Outside the intestine, which organ does Entamoeba histolytica invade most commonly?",
  ("Liver",
   "Correct. In extraintestinal amebiasis the amebas invade the viscera of the peritoneal cavity, most commonly the "
   "liver, where they produce abscesses with active trophozoites (amebic hepatitis). The lungs, spleen, adrenals, "
   "kidneys, skin and brain can also be infected."),
  [("Lungs",
    "The lungs can be infected (pulmonary amebiasis), but they are not the most common site. The organ amebas most "
    "commonly invade outside the intestine is the liver, where abscesses with active trophozoites cause amebic "
    "hepatitis.",
    "possible site taken for the most common"),
   ("Brain",
    "The brain is on the list of organs Entamoeba histolytica can infect, yet it is not the most common; rapid "
    "brain destruction is the hallmark of Naegleria fowleri, which follows the olfactory nerve. The most common "
    "extraintestinal site is the liver.",
    "Naegleria's target borrowed"),
   ("Spleen",
    "The spleen sits with the adrenals, kidneys, skin and brain among the other organs that can be infected. "
    "Extraintestinal amebiasis most commonly invades the liver; an enlarged spleen is a feature of African "
    "sleeping sickness and systemic leishmaniasis.",
    "possible site taken for the most common")],
  c(21, 29, 46, 53)),

Q("Entamoeba histolytica", IO2,
  "Amebiasis epidemics sometimes occur in prisons, hospitals and juvenile care institutions. Which shared condition "
  "explains these outbreaks?",
  ("Polluted water supplies",
   "Correct. Epidemics of amebiasis sometimes occur in concentrated populations where water supplies are polluted, "
   "such as prisons, hospitals and juvenile care institutions. The cysts are swallowed with contaminated water or "
   "food (the fecal-oral route), and prevention rests on water treatment."),
  [("Unchlorinated swimming pools",
    "Unchlorinated swimming pools, hot springs, lakes and streams hold the free-living amebas Naegleria and "
    "Acanthamoeba, which enter through the nose, eye or broken skin. Institutional outbreaks of amebiasis come from "
    "polluted water supplies that people swallow.",
    "free-living ameba habitat borrowed"),
   ("Contact with pigs and cattle",
    "Pigs and cattle are the hosts of Balantidium coli, the intestinal ciliate. Entamoeba histolytica has humans as "
    "its primary hosts, and its institutional outbreaks trace to polluted water supplies in crowded populations.",
    "Balantidium reservoir borrowed"),
   ("Insects biting the residents",
    "Biting insects spread the hemoflagellates (Trypanosoma and Leishmania), blood parasites with insect "
    "intermediate hosts. Entamoeba histolytica is intestinal and fecal-oral, so outbreaks in crowded institutions "
    "come from polluted water supplies.",
    "vector-borne spread assumed")],
  c(4, 16, 17, 23, 24, 31, 32, 33, 42)),

Q("Entamoeba histolytica", IO1,
  "This abscess, which has perforated the abdominal wall, formed after an intestinal protozoan acquired from "
  "swallowed cysts invaded deeper tissue. Which property of its trophozoite allows such invasion?",
  ("Enzymes that dissolve tissue",
   "Correct. The picture shows an amebic abscess perforating the abdominal wall. Entamoeba histolytica (histo, "
   "tissue; lytica, lysis) may secrete enzymes that dissolve tissues and penetrate deeper layers of the mucosa, "
   "leading to perforation and to abscesses with active trophozoites."),
  [("Antigenic variation of its surface",
    "Antigenic variation lets Trypanosoma brucei evade the immune response while it multiplies in the blood; it "
    "does not dissolve tissue. An abscess eating through the abdominal wall after swallowed cysts points to "
    "Entamoeba histolytica and its tissue-dissolving enzymes.",
    "African trypanosome trait borrowed"),
   ("A suction-cup ventral surface",
    "A concave ventral surface that acts like a suction cup belongs to Giardia lamblia, which feeds in the jejunum "
    "and causes diarrhea and abdominal pain. Dissolving tissue to form abscesses is the work of Entamoeba "
    "histolytica's enzymes.",
    "Giardia attachment borrowed"),
   ("Travel along the olfactory nerve",
    "Following the olfactory nerve is how Naegleria fowleri reaches the brain after burrowing through the nasal "
    "mucosa; it is not swallowed. This abscess came from an ingested intestinal protozoan whose enzymes dissolve "
    "tissue: Entamoeba histolytica.",
    "Naegleria route borrowed")],
  ci(22, 19, 20, 21, 29, 39, 41, 46),
  img=IMG + "/l17-fig-01.jpg",
  alt="Photograph of a thin patient's abdomen with a round, deep, open hole in the skin of the abdominal wall, "
      "rimmed with yellow tissue and surrounded by darkened skin.",
  slide="Slide 22"),

# ============================================================== NAEGLERIA FOWLERI (slides 4, 13, 24, 28-29)
Q("Naegleria fowleri", IO2,
  "In what kind of water does Naegleria fowleri ordinarily live?",
  ("Bacteria-rich standing water",
   "Correct. Naegleria fowleri and Acanthamoeba ordinarily inhabit standing water with a high bacterial count: hot "
   "springs, lakes, streams and unchlorinated swimming pools. Naegleria fowleri is prevalent in Florida's "
   "freshwater lakes, and it reaches people through nasal contact with such water."),
  [("Well-chlorinated swimming pools",
    "This reverses the risk: the danger is unchlorinated swimming pools, and the prevention advice is not to swim "
    "or dive in unchlorinated water. Naegleria fowleri ordinarily lives in standing water with a high bacterial "
    "count, such as hot springs, lakes and streams.",
    "chlorination reversed"),
   ("Salt water of the open ocean",
    "The sources of Naegleria fowleri are all fresh water: hot springs, lakes, streams, unchlorinated pools and "
    "even tap water. It ordinarily inhabits standing water with a high bacterial count and is prevalent in "
    "Florida's freshwater lakes.",
    "fresh water confused with salt water"),
   ("The human urogenital tract",
    "The human urogenital tract is the reservoir of Trichomonas vaginalis, a strict parasite that cannot survive "
    "long outside its host. Naegleria fowleri lives in water instead, ordinarily standing water with a high "
    "bacterial count.",
    "Trichomonas reservoir borrowed")],
  c(4, 24, 28, 29, 37)),

Q("Naegleria fowleri", IO2,
  "Besides swimming or diving in lakes, which exposure has transmitted Naegleria fowleri?",
  ("Rinsing the sinuses with tap water",
   "Correct. Naegleria fowleri is acquired through nasal contact with water, so rinsing the sinuses, even with tap "
   "water, can transmit it, as can diving, waterskiing, jet skiing and an indoor surfing facility. The trophozoite "
   "burrows through the nasal mucosa and travels to the brain."),
  [("Drinking unboiled tap water",
    "Swallowing water is the route of the intestinal protozoa such as Giardia lamblia, whose cysts are killed by "
    "boiling. Naegleria fowleri needs nasal contact with water; tap water transmits it when it goes up the nose, as "
    "in sinus rinsing.",
    "ingestion confused with nasal entry"),
   ("Wearing contact lenses while swimming",
    "Contact lens wearers are at risk of amebic keratitis from Acanthamoeba, an eye infection that does not "
    "typically disseminate. Naegleria fowleri enters through the nose, so sinus rinsing with tap water is a "
    "recognized exposure.",
    "Acanthamoeba risk borrowed"),
   ("Eating unwashed fresh produce",
    "Water and fresh produce are the sources of Cyclospora cayetanensis, an intestinal protozoan. Naegleria fowleri "
    "is not eaten; it is acquired through nasal contact with water, including rinsing the sinuses with tap water.",
    "food-borne protozoan route borrowed")],
  c(28, 29, 31, 39, 41, 75)),

Q("Naegleria fowleri", IO1,
  "After entering the body, by which path does Naegleria fowleri reach the brain?",
  ("Along the olfactory nerve",
   "Correct. In Naegleria meningoencephalitis the trophozoite burrows through the nasal mucosa and travels into the "
   "brain through the olfactory nerve. It then rapidly destroys the brain and spinal cord, with confusion, lack of "
   "balance, hallucinations, coma and death."),
  [("Through lymphatics into the blood",
    "Migrating into the lymphatics and disseminating in the blood is the path of Trypanosoma brucei after a tsetse "
    "fly bite, before it reaches the brain. Naegleria fowleri goes directly from the nasal mucosa along the "
    "olfactory nerve.",
    "African trypanosome path borrowed"),
   ("Inside migrating macrophages",
    "Riding in a migrating macrophage is how Leishmania turns a localized infection into a systemic one. "
    "Naegleria fowleri needs no carrier cell: its trophozoite burrows through the nasal mucosa and travels along "
    "the olfactory nerve.",
    "Leishmania spread borrowed"),
   ("Across the wall of the intestine",
    "Penetrating the intestinal mucosa and invading the viscera is how Entamoeba histolytica, swallowed as cysts, "
    "reaches the liver and other organs. Naegleria fowleri is not swallowed; it enters through the nose and follows "
    "the olfactory nerve to the brain.",
    "Entamoeba spread borrowed")],
  c(20, 21, 29, 46, 52)),

Q("Naegleria fowleri", IO1,
  "A previously healthy person develops headache, fever, vomiting and a stiff neck a few days after jet skiing on a "
  "lake, then becomes confused and starts hallucinating. How does this infection typically progress?",
  ("Rapid brain destruction and death",
   "Correct. Headache, fever, vomiting and stiff neck after lake water contact, then confusion and hallucinations, "
   "is Naegleria meningoencephalitis. It causes rapid destruction of the brain and spinal cord, with lack of "
   "balance, coma and death, and its treatment must be early."),
  [("Meningitis with a longer progression",
    "Symptoms of meningitis with a longer progression describe granulomatous amebic encephalitis from Acanthamoeba, "
    "which enters through broken skin or the nasal passages. Jet skiing followed within days by confusion and "
    "hallucinations fits the rapid destruction of Naegleria.",
    "Acanthamoeba encephalitis confused"),
   ("Brain symptoms only years later",
    "Brain symptoms years later mark the chronic Gambian form of African sleeping sickness, spread by tsetse flies. "
    "This patient's brain disease arrived within days of lake water exposure, the rapid destruction typical of "
    "Naegleria fowleri.",
    "Gambian sleeping sickness confused"),
   ("Chronic heart and brain inflammation",
    "Chronic inflammation of organs, especially the heart and brain, is the long-term picture of Chagas disease "
    "from Trypanosoma cruzi. Meningitis signs and hallucinations days after lake water exposure follow the rapid "
    "destruction of Naegleria fowleri.",
    "Chagas disease confused")],
  c(28, 29, 31, 46, 49)),

Q("Naegleria fowleri", IO1,
  "Which measure helps prevent Naegleria fowleri meningoencephalitis?",
  ("Avoiding unchlorinated water",
   "Correct. Prevention of Naegleria meningoencephalitis is not to swim or dive in unchlorinated water, and to use "
   "nose plugs. The ameba lives in standing water with a high bacterial count, including unchlorinated pools, "
   "lakes and hot springs, and enters through nasal contact with water."),
  [("Boiling water before drinking it",
    "Boiling kills Giardia lamblia, an intestinal flagellate swallowed with water or food. Naegleria fowleri is not "
    "swallowed but enters through the nose, so the protection is to avoid swimming or diving in unchlorinated water "
    "and to use nose plugs.",
    "ingestion-route prevention borrowed"),
   ("Controlling the insect vector",
    "Vector control prevents insect-borne infections such as Chagas disease and African sleeping sickness. "
    "Naegleria fowleri has no insect vector; it is free-living in water, so the measure is avoiding unchlorinated "
    "water and using nose plugs.",
    "vector control misapplied"),
   ("Cooking all pork thoroughly",
    "Thorough cooking prevents worms eaten in meat, such as Trichinella spiralis acquired from undercooked pork. "
    "Naegleria fowleri comes from water entering the nose, so prevention means not swimming or diving in "
    "unchlorinated water.",
    "food-borne prevention misapplied")],
  c(7, 24, 28, 29, 41, 47, 51)),

Q("Naegleria fowleri", IO1,
  "Which group accounts for most cases of Naegleria fowleri meningoencephalitis?",
  ("Children and young adults",
   "Correct. Most cases of Naegleria meningoencephalitis occur in children and young adults, through exposure to "
   "freshwater lakes and streams while diving, waterskiing or jet skiing. Water reaching the nose carries the "
   "trophozoites, which travel to the brain through the olfactory nerve."),
  [("Contact lens wearers",
    "Contact lens wearers are the risk group for amebic keratitis caused by Acanthamoeba, with eye pain, redness and "
    "irritation. Naegleria meningoencephalitis strikes mostly children and young adults exposed to freshwater lakes "
    "and streams.",
    "Acanthamoeba keratitis risk group"),
   ("Immunocompromised adults",
    "Compromised immune systems set the stage for Acanthamoeba's granulomatous amebic encephalitis and disseminated "
    "disease. Naegleria fowleri mainly affects children and young adults who are exposed to fresh water.",
    "Acanthamoeba encephalitis host borrowed"),
   ("Young, sexually active women",
    "Young, sexually active women are the group in which trichomoniasis is the most common curable sexually "
    "transmitted disease. Naegleria is acquired from water, and most cases are children and young adults exposed "
    "to freshwater lakes and streams.",
    "Trichomonas risk group borrowed")],
  c(28, 29, 31, 32, 37)),

# ============================================================== ACANTHAMOEBA (slides 4, 24, 31-32)
Q("Acanthamoeba", IO2,
  "Through which portals does Acanthamoeba typically enter to cause granulomatous amebic encephalitis?",
  ("Broken skin or the nasal passages",
   "Correct. Granulomatous amebic encephalitis typically begins when Acanthamoeba enters through a break in the "
   "skin or through the nasal passages. It arises in people with compromised immune systems and gives symptoms of "
   "meningitis but with a longer progression."),
  [("Swallowed cysts in food or water",
    "Swallowed cysts are the fecal-oral route of Entamoeba histolytica, Giardia lamblia and Balantidium coli, "
    "intestinal protozoa. Acanthamoeba is free-living in lakes, hot tubs and pools and reaches the brain after "
    "entering through broken skin or the nasal passages.",
    "intestinal protozoan route borrowed"),
   ("The bite of a female sand fly",
    "Female sand flies inject Leishmania with their bite during a blood meal. Acanthamoeba has no insect vector; this "
    "free-living ameba of freshwater lakes, hot tubs and swimming pools enters through broken skin or the nasal "
    "passages.",
    "Leishmania vector borrowed"),
   ("Sexual contact with a carrier",
    "Sexual contact transmits Trichomonas vaginalis, whose reservoir is the human urogenital tract. Acanthamoeba "
    "lives free in water and typically enters through a break in the skin or through the nasal passages to cause "
    "granulomatous amebic encephalitis.",
    "Trichomonas route borrowed")],
  c(31, 32, 33, 37, 39, 52)),

Q("Acanthamoeba", IO2,
  "Amebic keratitis caused by Acanthamoeba occurs mainly in which group?",
  ("Contact lens wearers",
   "Correct. Acanthamoeba, distributed worldwide in freshwater lakes, hot tubs and swimming pools, causes amebic "
   "keratitis in contact lens wearers, with eye pain, redness and irritation. The eye infection does not typically "
   "disseminate, unlike its granulomatous amebic encephalitis."),
  [("Children and young adults",
    "Children and young adults exposed to freshwater lakes and streams make up most cases of Naegleria "
    "meningoencephalitis, a brain infection. Acanthamoeba keratitis, an eye infection with pain, redness and "
    "irritation, is linked to contact lens wearers.",
    "Naegleria risk group borrowed"),
   ("Young, sexually active women",
    "Young, sexually active women are the group in which trichomoniasis is the most common curable sexually "
    "transmitted disease. Amebic keratitis is an eye infection from Acanthamoeba that occurs in contact lens "
    "wearers.",
    "Trichomonas risk group borrowed"),
   ("Campers",
    "Campers are the group in whom giardiasis is common, from Giardia lamblia cysts swallowed with water or food "
    "(its reservoirs include beavers and coyotes). Acanthamoeba keratitis, with eye pain, redness and irritation, "
    "occurs in contact lens wearers.",
    "Giardia risk group borrowed")],
  c(4, 28, 31, 37, 39)),

# ============================================================== BALANTIDIUM COLI (slides 4, 12, 13, 33-34)
Q("Balantidium coli", IO2,
  "Balantidium coli normally lives in the intestines of which animals?",
  ("Pigs and cattle",
   "Correct. Balantidium coli, the intestinal ciliate, occupies the intestines of domestic animals such as pigs and "
   "cattle, its alternate hosts. Humans acquire it by ingesting cyst-containing food or water; the trophozoite "
   "erodes the intestine, but healthy humans are resistant."),
  [("Beavers and coyotes",
    "Beavers and coyotes, with cattle, cats and humans, are reservoirs of Giardia lamblia, the heart-shaped "
    "flagellate swallowed with water and food. Balantidium coli is the intestinal ciliate of domestic animals, "
    "chiefly pigs and cattle.",
    "Giardia reservoir borrowed"),
   ("Domestic dogs",
    "Dogs are the alternate hosts of Leishmania in equatorial regions, a blood and tissue parasite spread by female "
    "sand flies. Balantidium coli lives in the intestines of pigs and cattle and reaches humans in cyst-containing "
    "food or water.",
    "Leishmania alternate host borrowed"),
   ("House cats",
    "Cats matter for Toxoplasma gondii (pregnant women should not clean the cat box) and are among the reservoirs "
    "of Giardia lamblia. Balantidium coli is the intestinal ciliate of domestic animals such as pigs and cattle.",
    "Toxoplasma and Giardia host borrowed")],
  c(4, 5, 33, 39, 52)),

Q("Balantidium coli", IO1,
  "This protozoan was found in a stool sample from a patient with persistent diarrhea and abdominal pain. Judging "
  "by its surface, to which motility group does it belong?",
  ("Ciliated protozoa",
   "Correct. The fine fringe of short hairlike cilia around this cell marks a ciliate. Balantidium coli is the "
   "intestinal ciliate: acquired from cyst-containing food or water, its trophozoite erodes the intestine, causing "
   "persistent diarrhea, occasionally dysentery, abdominal pain and weight loss."),
  [("Flagellated protozoa",
    "Flagellates such as Giardia lamblia (heart-shaped) and Trichomonas (pear-shaped, with an undulating membrane) "
    "carry a few long whiplike flagella. This cell is fringed all around with short cilia, which marks the ciliate "
    "Balantidium coli.",
    "flagella confused with cilia"),
   ("Ameboid protozoa",
    "Amebas such as Entamoeba histolytica move by means of pseudopods; the trophozoite has a large nucleus and lacks "
    "most other organelles. A fringe of short cilia around an oval cell marks a ciliate instead, Balantidium coli.",
    "ameba confused with ciliate"),
   ("Apicomplexan protozoa",
    "The apicomplexans (Plasmodium, Toxoplasma, Cryptosporidium) lack locomotor organelles in the trophozoite "
    "state; Plasmodium appears as ring forms inside red blood cells. A cell fringed with cilia in stool is the "
    "ciliate Balantidium coli.",
    "apicomplexan group confused")],
  ci(34, 5, 12, 16, 33, 36, 39, 55),
  img=IMG + "/l17-fig-02.jpg",
  alt="Photomicrograph of a single oval cell with granular, yellow-brown contents and a thin fringe of fine, short "
      "hairlike projections around its edge.",
  slide="Slide 34"),

# ============================================================== TRICHOMONAS VAGINALIS (slides 4, 13, 36-38)
Q("Trichomonas vaginalis", IO2,
  "What is the reservoir of Trichomonas vaginalis?",
  ("The human urogenital tract",
   "Correct. The reservoir of Trichomonas vaginalis is the human urogenital tract. It is a strict parasite that "
   "cannot survive long outside the host, exists only as a trophozoite with no cyst, and causes the sexually "
   "transmitted disease trichomoniasis."),
  [("Freshwater lakes and hot tubs",
    "Freshwater lakes, hot tubs and swimming pools hold free-living Acanthamoeba. Trichomonas vaginalis is a strict "
    "parasite that cannot survive long outside the host, and its reservoir is the human urogenital tract.",
    "free-living ameba habitat borrowed"),
   ("Domestic pigs and cattle",
    "Pigs and cattle are the alternate hosts of Balantidium coli, the intestinal ciliate. Trichomoniasis has a human "
    "reservoir, the urogenital tract, and spreads between people as a sexually transmitted disease.",
    "Balantidium hosts borrowed"),
   ("Beavers and other wild mammals",
    "Beavers and coyotes are among the reservoirs of Giardia lamblia, an intestinal flagellate swallowed with water "
    "and food. Trichomonas vaginalis needs no animal host; its reservoir is the human urogenital tract.",
    "Giardia reservoir borrowed")],
  c(4, 31, 33, 36, 37, 39)),

Q("Trichomonas vaginalis", IO1,
  "Which life-cycle forms does Trichomonas have?",
  ("Trophozoite only",
   "Correct. Trichomonads are small, pear-shaped flagellates with anterior flagella and an undulating membrane that "
   "exist only in trophozoite form; there is no cyst. Trichomonas vaginalis is also a strict parasite that cannot "
   "survive long outside the host."),
  [("Cyst only",
    "Trichomonas never forms a cyst; it exists only as the trophozoite, the active feeding cell by whose simple "
    "asexual division most protozoa propagate. Cysts belong to the cycles of Entamoeba, Giardia and Balantidium.",
    "no-cyst fact reversed"),
   ("Trophozoite and cyst",
    "Alternating between a motile trophozoite and a cyst is the cycle of Entamoeba histolytica (large trophozoite, "
    "smaller nonmotile cyst) and of Giardia lamblia. Trichomonas exists only in trophozoite form, with no cyst.",
    "Entamoeba cycle borrowed"),
   ("Sexual and asexual stages",
    "Alternating between sexual and asexual phases is the complex life cycle of the apicomplexan parasites, such as "
    "Plasmodium and Toxoplasma. Trichomonas propagates as the trophozoite alone and never forms a cyst.",
    "apicomplexan cycle borrowed")],
  c(12, 16, 33, 36, 37, 39, 55)),

Q("Trichomonas vaginalis", IO1,
  "A young, sexually active woman has a foul-smelling, green-to-yellow vaginal discharge, vulvitis, and urinary "
  "frequency with pain. How is the suspected protozoan diagnosed?",
  ("Microscopy of a vaginal smear",
   "Correct. Foul-smelling, green-to-yellow discharge with vulvitis and painful, frequent urination in a young, "
   "sexually active woman points to trichomoniasis, the most common curable sexually transmitted disease in this "
   "group. Trichomonas vaginalis is diagnosed by microscopic analysis of a vaginal smear."),
  [("Examination of a fecal smear",
    "A fecal smear, with history and an enzyme-linked immunosorbent assay using monoclonal antibodies, diagnoses "
    "Entamoeba histolytica, an intestinal ameba. Vaginal discharge with vulvitis points to Trichomonas vaginalis, "
    "found by microscopy of a vaginal smear.",
    "amebiasis test borrowed"),
   ("Card agglutination test",
    "The card agglutination test for trypanosomes gives rapid diagnosis of African sleeping sickness, spread by "
    "tsetse flies. This patient's genital symptoms point to Trichomonas vaginalis, diagnosed on a vaginal smear "
    "under the microscope.",
    "sleeping sickness test borrowed"),
   ("Polymerase chain reaction of stool",
    "Polymerase chain reaction is used for Giardia lamblia, because microscopy is difficult when the organism is "
    "shed in feces intermittently. A genital infection with this discharge is Trichomonas vaginalis, seen directly "
    "on a vaginal smear.",
    "giardiasis test borrowed")],
  c(4, 23, 37, 38, 41, 47)),

Q("Trichomonas vaginalis", IO1,
  "Infection with the flagellate shown raises the risk of which further problem?",
  ("Cervical cancer",
   "Correct. The cells shown are small, pear-shaped trichomonads with flagella and an undulating membrane: "
   "Trichomonas vaginalis. Trichomoniasis raises the risk of cervical cancer, may predispose to other sexually "
   "transmitted diseases and increases transmission of human immunodeficiency virus."),
  [("Liver abscess",
    "Liver abscesses with active trophozoites are the extraintestinal disease of Entamoeba histolytica, an ameba "
    "that moves by pseudopods rather than flagella. These flagellated, pear-shaped cells are Trichomonas vaginalis, "
    "which raises cervical cancer risk.",
    "Entamoeba complication borrowed"),
   ("Heart muscle disease",
    "Heart disease follows Chagas disease, in which the heart muscle harbors masses of Trypanosoma cruzi; "
    "trypanosomes are spindle-shaped with eel-like motility. The pear-shaped flagellates here are "
    "Trichomonas vaginalis, linked to cervical cancer.",
    "Chagas complication borrowed"),
   ("Amebic keratitis",
    "Amebic keratitis is an eye infection of contact lens wearers caused by Acanthamoeba, an ameba rather than a "
    "flagellate. The pear-shaped cells with flagella and an undulating membrane are Trichomonas vaginalis, which "
    "raises the risk of cervical cancer.",
    "Acanthamoeba disease borrowed")],
  ci(38, 4, 21, 31, 36, 37, 44, 49),
  img=IMG + "/l17-fig-03.jpg",
  alt="Two stained single cells on a pale green background, each rounded to pear-shaped with a dark purple nucleus, "
      "a wavy edge along one side and thin, curling, whiplike threads at one end.",
  slide="Slide 38"),

# ============================================================== GIARDIA LAMBLIA (slides 4, 13, 39-41)
Q("Giardia lamblia", IO2,
  "Which animals are reservoirs of Giardia lamblia?",
  ("Beavers and coyotes",
   "Correct. Reservoirs of Giardia lamblia include beavers, cattle, coyotes, cats and humans, and giardiasis is "
   "common in campers. Its small, compact, multinucleate cysts survive in the environment and are usually ingested "
   "with water and food."),
  [("Domestic dogs",
    "Dogs are the alternate hosts of Leishmania in equatorial regions, a blood and tissue parasite spread by female "
    "sand flies. Giardia lamblia's reservoirs are beavers, cattle, coyotes, cats and humans.",
    "Leishmania alternate host borrowed"),
   ("Domestic pigs",
    "Pigs are the hosts of Balantidium coli, the intestinal ciliate, and balantidiosis is zoonotic in pigs. Giardia "
    "lamblia, a flagellate, has reservoirs that include beavers, coyotes, cattle, cats and humans.",
    "Balantidium host borrowed"),
   ("Tsetse flies",
    "Tsetse flies transmit Trypanosoma brucei, a blood parasite, by biting. Giardia lamblia needs no insect: it is "
    "harbored by beavers, cattle, coyotes, cats and humans and swallowed with water and food.",
    "vector confused with reservoir")],
  c(4, 33, 39, 45, 52)),

Q("Giardia lamblia", IO2,
  "Giardiasis is common in campers. How is Giardia lamblia usually acquired?",
  ("Swallowed cysts in water or food",
   "Correct. Giardia lamblia cysts, small, compact and multinucleate, survive in the environment and are usually "
   "ingested with water and food; giardiasis is common in campers. The cysts enter the duodenum, germinate, and the "
   "trophozoites feed and multiply in the jejunum. Boiling, ozone and iodine kill the agent."),
  [("Water splashing up into the nose",
    "Water entering the nose is how Naegleria fowleri is acquired from lakes and streams, reaching the brain along "
    "the olfactory nerve. Giardia lamblia is swallowed instead: its cysts are usually ingested with water and food.",
    "Naegleria route borrowed"),
   ("Bites of blood-sucking insects",
    "Blood-sucking insects spread the hemoflagellates, Trypanosoma and Leishmania, which live in the blood and "
    "tissues. Giardia lamblia is an intestinal flagellate whose cysts are ingested with water and food.",
    "hemoflagellate route borrowed"),
   ("Handling infected farm pigs",
    "Pigs are the hosts of Balantidium coli, the intestinal ciliate, and even that organism is acquired by ingesting "
    "cyst-containing food or water. Giardia lamblia reaches people the same way, as cysts ingested with water and "
    "food.",
    "Balantidium host and contact assumed")],
  c(4, 28, 33, 39, 41, 42)),

Q("Giardia lamblia", IO1,
  "Why is microscopic diagnosis of giardiasis difficult?",
  ("It is shed in feces intermittently",
   "Correct. Microscopic diagnosis of giardiasis is difficult because Giardia lamblia is shed in the feces "
   "intermittently, so polymerase chain reaction analysis is also used. The agent is killed by boiling, ozone and "
   "iodine."),
  [("It lives only inside macrophages",
    "Living inside macrophages describes Leishmania and Trypanosoma cruzi in human tissues, not an intestinal "
    "flagellate. Giardia lamblia feeds in the jejunum and passes into the feces, but only intermittently, which is "
    "what hampers microscopy.",
    "hemoflagellate stage borrowed"),
   ("It never forms a cyst",
    "Having no cyst is the feature of Trichomonas, which exists only as a trophozoite. Giardia lamblia does form "
    "cysts, small, compact and multinucleate; microscopy is difficult because the organism is shed in feces "
    "intermittently.",
    "Trichomonas trait borrowed"),
   ("It keeps changing surface antigens",
    "Changing surface antigens (antigenic variation) is how Trypanosoma brucei evades the immune response in the "
    "blood. The obstacle to finding Giardia lamblia under the microscope is that it is shed in feces only "
    "intermittently.",
    "antigenic variation borrowed")],
  c(36, 39, 41, 43, 46)),

Q("Giardia lamblia", IO1,
  "The drawing shows front and side views of the trophozoite of an intestinal flagellate. What does its concave "
  "ventral surface do?",
  ("Acts like a suction cup",
   "Correct. The heart-shaped trophozoite with paired nuclei and long flagella is Giardia lamblia. Its unique "
   "symmetrical heart shape has a concave ventral surface that acts like a suction cup, in the jejunum where it "
   "feeds and multiplies and causes diarrhea and abdominal pain."),
  [("Dissolves intestinal tissue",
    "Dissolving tissue with secreted enzymes is what Entamoeba histolytica, an ameba, may do to penetrate deeper "
    "layers of the mucosa. The concave ventral surface of this heart-shaped flagellate, Giardia lamblia, acts like "
    "a suction cup.",
    "Entamoeba enzymes borrowed"),
   ("Drives eel-like swimming",
    "Eel-like motility belongs to Trypanosoma, an elongate, spindle-shaped cell with tapered ends that lives in "
    "blood. The heart-shaped Giardia lamblia uses its concave ventral surface like a suction "
    "cup.",
    "trypanosome motility borrowed"),
   ("Forms an undulating membrane",
    "An undulating membrane, with anterior flagella, marks the pear-shaped trichomonads such as Trichomonas "
    "vaginalis. The heart-shaped cell drawn here is Giardia lamblia, whose concave ventral surface acts like a "
    "suction cup.",
    "Trichomonas structure borrowed")],
  ci(40, 20, 36, 39, 41, 44),
  img=IMG + "/l17-fig-04.jpg",
  alt="Drawing of two views of one single-celled organism: a front view, broad at the top and tapering to a point, "
      "with two oval nuclei and several long trailing flagella, and a side view showing a hollowed-out underside; "
      "two unlabeled pointer lines.",
  slide="Slide 40"),

# ============================================================== HEMOFLAGELLATES (slides 13, 42-43)
Q("Hemoflagellates", IO1,
  "How are the life cycles of the hemoflagellates described?",
  ("Complicated, with changes in form",
   "Correct. Hemoflagellates, obligate parasites of the blood and tissues of the human host, have complicated life "
   "cycles and undergo morphological changes, and they are categorized by their cellular and infective stages. "
   "They cause life-threatening and debilitating zoonoses."),
  [("Simple division of the feeding cell",
    "Most protozoa propagate by simple asexual division of the active feeding cell, the trophozoite. The "
    "hemoflagellates are the contrasting case: complicated life cycles with morphological changes between stages.",
    "typical protozoan cycle generalized"),
   ("Trophozoite only, with no cyst",
    "Existing only as a trophozoite with no cyst describes the trichomonads, such as Trichomonas vaginalis. "
    "Hemoflagellates pass through several forms instead: complicated life cycles with morphological changes.",
    "Trichomonas cycle borrowed"),
   ("Alternating trophozoite and cyst",
    "Alternating between a large motile trophozoite and a smaller nonmotile cyst is the two-form cycle of Entamoeba "
    "histolytica. Hemoflagellates have complicated life cycles and undergo morphological changes across several "
    "stages.",
    "Entamoeba cycle borrowed")],
  c(12, 16, 36, 42)),

Q("Hemoflagellates", IO2,
  "How are the hemoflagellates spread to humans?",
  ("By blood-sucking insects",
   "Correct. Hemoflagellates are obligate parasites of human blood and tissues, spread in specific tropical regions "
   "by blood-sucking insects that serve as intermediate hosts: the tsetse fly for Trypanosoma brucei, the reduviid "
   "bug for Trypanosoma cruzi and the female sand fly for Leishmania."),
  [("By swallowed cysts in water",
    "Swallowed cysts are the fecal-oral route of the intestinal protozoa: Entamoeba histolytica, Giardia lamblia "
    "and Balantidium coli. Hemoflagellates live in blood and tissues and are zoonoses spread by blood-sucking "
    "insects that serve as intermediate hosts.",
    "intestinal protozoan route borrowed"),
   ("By nasal contact with water",
    "Nasal contact with water is how the free-living ameba Naegleria fowleri reaches the brain along the olfactory "
    "nerve. Hemoflagellates are vector-borne blood parasites, carried by blood-sucking insects that act as "
    "intermediate hosts.",
    "Naegleria route borrowed"),
   ("By sexual contact with carriers",
    "Sexual contact spreads Trichomonas vaginalis, a flagellate of the urogenital tract rather than the blood. The "
    "hemoflagellates are vector-borne: blood-sucking insects serve as their intermediate hosts.",
    "Trichomonas route borrowed")],
  c(16, 28, 33, 37, 39, 42, 45, 49, 52)),

# ============================================================== TRYPANOSOMA BRUCEI (slides 5, 13, 43-47)
Q("Trypanosoma brucei", IO2,
  "Which insect spreads Trypanosoma brucei, the cause of African sleeping sickness?",
  ("The tsetse fly",
   "Correct. African sleeping sickness is spread by tsetse flies and harbored by reservoir mammals. The fly's bite "
   "inoculates the skin, where a primary chancre develops, and the parasite spreads through the lymphatics and "
   "blood; control involves eliminating the tsetse fly."),
  [("The female sand fly",
    "Female sand flies, which need a blood meal to produce eggs, transmit Leishmania with their bite. "
    "Trypanosoma brucei uses a different insect, the tsetse fly of West and East Africa.",
    "Leishmania vector borrowed"),
   ("The reduviid bug",
    "The reduviid (kissing) bug is the vector of Trypanosoma cruzi, which causes Chagas disease (American "
    "trypanosomiasis) through infected bug feces. The African trypanosome, Trypanosoma brucei, is spread by the "
    "tsetse fly.",
    "American trypanosome vector borrowed"),
   ("The Anopheles mosquito",
    "The Anopheles mosquito is the vector of Plasmodium, the cause of malaria, seen as ring forms inside red blood "
    "cells. Trypanosoma brucei is spread by tsetse flies, and control involves eliminating them.",
    "malaria vector borrowed")],
  c(5, 45, 46, 47, 49, 52)),

Q("Trypanosoma brucei", IO1,
  "As Trypanosoma brucei multiplies in the blood, which organs does it damage?",
  ("Spleen, lymph nodes and brain",
   "Correct. After the bite, Trypanosoma brucei migrates into the lymphatics, disseminates in the blood, multiplies "
   "there and damages the spleen, lymph nodes and brain. Early fever, enlarged spleen and swollen lymph nodes give "
   "way to personality and behavioral changes, then sleep disturbances, seizures and coma."),
  [("Heart muscle and large intestine",
    "The heart muscle and large intestine harbor masses of Trypanosoma cruzi in Chagas disease, with chronic "
    "inflammation especially of the heart. Trypanosoma brucei, the African trypanosome, damages the spleen, lymph "
    "nodes and brain.",
    "Chagas organs borrowed"),
   ("Liver, lungs and adrenals",
    "The liver, lungs and adrenals are among the viscera Entamoeba histolytica can invade in extraintestinal "
    "amebiasis, the liver most commonly. Trypanosoma brucei multiplies in the blood and damages the spleen, lymph "
    "nodes and brain.",
    "Entamoeba sites borrowed"),
   ("Duodenum and jejunum",
    "Giardia lamblia germinates in the duodenum and feeds and multiplies in the jejunum, causing diarrhea and "
    "abdominal pain. Trypanosoma brucei is a blood parasite that damages the spleen, lymph nodes and brain.",
    "Giardia sites borrowed")],
  c(21, 39, 41, 46, 47, 49)),

Q("Trypanosoma brucei", IO1,
  "Which genus of protozoa is shown in this stained blood smear?",
  ("Trypanosoma",
   "Correct. Elongate, spindle-shaped flagellates with tapered ends swimming between red blood cells are "
   "trypanosomes, readily demonstrated in blood, spinal fluid or lymph nodes. Trypanosoma brucei causes African "
   "sleeping sickness and Trypanosoma cruzi Chagas disease; both are hemoflagellates."),
  [("Plasmodium",
    "Plasmodium is seen as small ring forms inside the red blood cells, not as long flagellates swimming between "
    "them. The thin, wavy cells lying outside the red cells in this smear are trypanosomes.",
    "intracellular blood parasite confused"),
   ("Leishmania",
    "Leishmania multiplies inside human macrophages, which keep the infection localized or carry it systemically "
    "when they migrate. Free, spindle-shaped flagellates swimming between red blood cells, as here, are "
    "trypanosomes.",
    "other hemoflagellate confused"),
   ("Trichomonas",
    "Trichomonas is a small, pear-shaped flagellate of the urogenital tract, found on a vaginal smear, and it cannot "
    "survive long outside the host. Elongate flagellates among red blood cells in a blood smear are trypanosomes.",
    "other flagellate confused")],
  ci(46, 5, 36, 37, 38, 44, 47, 52),
  img=IMG + "/l17-fig-05.jpg",
  alt="Stained blood smear of round pink red blood cells with several thin, wavy, purple-stained elongated cells "
      "lying between them.",
  slide="Slide 46"),

Q("Trypanosoma brucei", IO1,
  "How does the Rhodesian form of African sleeping sickness differ from the Gambian form?",
  ("It is acute, with brain symptoms in weeks",
   "Correct. Trypanosoma brucei rhodesiense, the Rhodesian strain of East Africa, causes an acute disease with brain "
   "symptoms within weeks. Trypanosoma brucei gambiense, the Gambian strain of West Africa, causes a chronic "
   "disease with brain symptoms years later."),
  [("It is chronic, with brain symptoms years later",
    "This describes the Gambian form, from Trypanosoma brucei gambiense of West Africa. The Rhodesian form is the "
    "reverse: acute, with brain symptoms within weeks. The tell is the pace: Rhodesian is fast, Gambian slow.",
    "Rhodesian and Gambian swapped"),
   ("It occurs mainly in West Africa",
    "West Africa is home to the Gambian strain, Trypanosoma brucei gambiense. The Rhodesian strain, Trypanosoma "
    "brucei rhodesiense, is found in East Africa and causes an acute disease with brain symptoms within weeks.",
    "geography swapped"),
   ("It is spread by the reduviid bug",
    "Both forms of African sleeping sickness are spread by tsetse flies; the reduviid bug spreads Trypanosoma cruzi "
    "and Chagas disease. The Rhodesian form differs from the Gambian form in being acute, with brain symptoms "
    "within weeks.",
    "Chagas vector borrowed")],
  c(45, 46, 49)),

# ============================================================== TRYPANOSOMA CRUZI (slides 5, 43, 48-51)
Q("Trypanosoma cruzi", IO2,
  "Why is Chagas disease becoming more of an issue in the southern United States?",
  ("Its vector is migrating there",
   "Correct. Chagas disease (American trypanosomiasis) has millions of cases in Latin America but is becoming more "
   "of an issue in the southern United States through vector migration: the reduviid (kissing) bug is expanding "
   "its range. Many now consider it endemic in the United States, and control is through control of the vector."),
  [("Freshwater lakes are warming",
    "Lakes, streams and hot springs are the home of the free-living ameba Naegleria fowleri, acquired through the "
    "nose. Chagas disease is insect-borne, and it is rising in the southern United States because its vector, the "
    "reduviid bug, is migrating there.",
    "Naegleria habitat borrowed"),
   ("Imported produce is contaminated",
    "Water and fresh produce are the sources of Cyclospora cayetanensis, an intestinal protozoan. Trypanosoma cruzi "
    "reaches people through the feces of the reduviid bug, and its rise in the southern United States comes from "
    "vector migration.",
    "food-borne protozoan borrowed"),
   ("Sexual spread is increasing",
    "Sexual spread belongs to Trichomonas vaginalis, whose trichomoniasis is a sexually transmitted disease. Chagas "
    "disease is vector-borne; it is becoming an issue in the southern United States because the reduviid bug vector "
    "is expanding its range.",
    "Trichomonas route borrowed")],
  c(5, 24, 37, 48, 49, 51, 75)),

Q("Trypanosoma cruzi", IO2,
  "A lifelong resident of the southern United States who has never traveled abroad is diagnosed with Chagas "
  "disease. What best explains acquiring it at home?",
  ("Range expansion of its vector",
   "Correct. Chagas disease was a tropical disorder of Latin America, but it is becoming an issue in the southern "
   "United States as its vector, the reduviid (kissing) bug, expands its range. Many now consider it endemic in the "
   "United States, so a case can be acquired without travel."),
  [("Spread of the tsetse fly vector",
    "The tsetse fly is the vector of Trypanosoma brucei and African sleeping sickness in West and East Africa, not "
    "of Chagas disease. The migrating vector behind Chagas disease in the southern United States is the reduviid "
    "bug.",
    "African trypanosome vector borrowed"),
   ("Dogs serving as alternate hosts",
    "Dogs are the alternate hosts of Leishmania in equatorial regions, where female sand flies spread it. Chagas "
    "disease in the southern United States is explained by migration of its own vector, the reduviid bug.",
    "Leishmania host borrowed"),
   ("Lake water entering the nose",
    "Water entering the nose transmits Naegleria fowleri and causes meningoencephalitis, not Chagas disease. "
    "Trypanosoma cruzi enters through reduviid bug feces, and that vector's migration explains cases in the "
    "southern United States.",
    "Naegleria route borrowed")],
  c(5, 28, 45, 48, 49, 52)),

Q("Trypanosoma cruzi", IO2,
  "Which material from the reduviid bug carries Trypanosoma cruzi into a person?",
  ("Its feces",
   "Correct. Infection occurs when reduviid (kissing) bug feces are inoculated into a cutaneous portal. Trypanosoma "
   "cruzi may also be transmitted congenitally, through transfusions or organ transplants, or by eating food "
   "contaminated with the bug's urine or feces."),
  [("Its saliva",
    "Saliva carries Trypanosoma brucei: the saliva of an infected tsetse fly inoculates the human bloodstream. The "
    "reduviid bug passes Trypanosoma cruzi in its feces, which are inoculated into a cutaneous portal.",
    "tsetse route borrowed"),
   ("Its eggs",
    "Eggs passed in feces belong to the worm cycles, as when worm eggs are released into soil. Trypanosoma cruzi is "
    "a single-celled protozoan; the bug carries it in its feces, which enter through a cutaneous portal.",
    "helminth eggs borrowed"),
   ("Its larvae",
    "Larvae that penetrate the skin belong to worms such as Strongyloides stercoralis, which then migrate to the "
    "lungs. Trypanosoma cruzi is a protozoan carried in reduviid bug feces inoculated into a cutaneous portal.",
    "helminth larvae borrowed")],
  c(45, 49, 81, 100)),

Q("Trypanosoma cruzi", IO1,
  "This swelling of one eyelid with conjunctivitis appeared with fever and swollen lymph nodes, spleen and liver. "
  "What is this sign called?",
  ("Romana's sign",
   "Correct. Romana's sign, a swelling of the eyelid with conjunctivitis, is the local lesion of Chagas disease, "
   "with fever and swelling of the lymph nodes, spleen and liver. The heart muscle and large intestine harbor "
   "masses of Trypanosoma cruzi, and treatment must be given early."),
  [("Primary chancre",
    "A primary chancre develops where a tsetse fly inoculates Trypanosoma brucei into the skin. "
    "The eyelid swelling with conjunctivitis shown here is Romana's sign, the local lesion of Chagas disease.",
    "African trypanosome lesion"),
   ("Baghdad boil",
    "A Baghdad boil (oriental sore) is the localized ulcerated sore of cutaneous leishmaniasis. The picture shows a "
    "swollen eyelid without an ulcer, Romana's sign of Chagas disease, with fever and enlarged lymph nodes, spleen "
    "and liver.",
    "Leishmania lesion"),
   ("Amebic keratitis",
    "Amebic keratitis from Acanthamoeba gives eye pain, redness and irritation in contact lens wearers and does not "
    "typically disseminate. Eyelid swelling with fever and enlarged lymph nodes, spleen and liver is Romana's sign "
    "of Chagas disease.",
    "Acanthamoeba eye disease")],
  ci(51, 31, 46, 49, 53),
  img=IMG + "/l17-fig-06.jpg",
  alt="Close-up photograph of a face with marked swelling of the upper and lower lids of one eye, which is nearly "
      "closed; the other eye looks normal.",
  slide="Slide 51"),

# ============================================================== LEISHMANIA (slides 5, 13, 43, 52-54)
Q("Leishmania", IO2,
  "Which vector and alternate host belong to the cycle of Leishmania?",
  ("Female sand fly; dogs",
   "Correct. Leishmaniasis is a zoonosis transmitted among mammalian hosts by female sand flies, which need a blood "
   "meal to produce eggs; in equatorial regions dogs are the alternate hosts. The sand fly injects the parasite "
   "with its bite."),
  [("Tsetse fly; reservoir mammals",
    "Tsetse flies with reservoir mammals belong to Trypanosoma brucei and African sleeping sickness. Leishmania is "
    "carried by a different insect, the female sand fly, with dogs as alternate hosts in equatorial regions.",
    "African trypanosome cycle borrowed"),
   ("Reduviid bug; wild animals",
    "The reduviid (kissing) bug, cycling through wild animals and human habitats, carries Trypanosoma cruzi, the "
    "cause of Chagas disease. Leishmania's vector is the female sand fly, and its alternate hosts are dogs.",
    "American trypanosome cycle borrowed"),
   ("Female sand fly; pigs",
    "The female sand fly is the right vector, but pigs, with cattle, are the alternate hosts of Balantidium coli, "
    "the intestinal ciliate. Leishmania's alternate hosts in equatorial regions are dogs.",
    "right vector, Balantidium host borrowed")],
  c(4, 5, 33, 45, 50, 52, 54)),

Q("Leishmania", IO1,
  "Co-infection of leishmaniasis with which disease is an increasing issue that can make diagnosis difficult?",
  ("Malaria",
   "Correct. Co-infection of leishmaniasis and malaria is an increasing issue and may make diagnosis difficult. "
   "Malaria, spread by the Anopheles mosquito, brings regular episodes of chills, fever and sweating, and systemic "
   "leishmaniasis brings high intermittent fever."),
  [("Chagas disease",
    "Chagas disease, from Trypanosoma cruzi spread by reduviid bugs, is another hemoflagellate disease, but it is "
    "not this co-infection. Leishmaniasis with malaria is the co-infection that is an increasing issue and may make "
    "diagnosis difficult.",
    "other hemoflagellate disease assumed"),
   ("Trichomoniasis",
    "Trichomoniasis is a sexually transmitted disease that may predispose to other sexually transmitted diseases; "
    "it is not the partner in this co-infection. The co-infection that can make diagnosis difficult is leishmaniasis "
    "with malaria.",
    "Trichomonas co-infection link borrowed"),
   ("Amebiasis",
    "Amebiasis is the fecal-oral intestinal infection of Entamoeba histolytica, diagnosed by fecal smear and "
    "history. The increasing co-infection issue for leishmaniasis is malaria, which may make diagnosis difficult.",
    "unrelated protozoan disease")],
  c(5, 23, 38, 48, 52, 53)),

Q("Leishmania", IO1,
  "Once Leishmania is multiplying inside a macrophage, what determines whether the infection stays localized or "
  "becomes systemic?",
  ("Whether the macrophage migrates",
   "Correct. The parasite injected with the sand fly bite converts and multiplies inside macrophages. If the "
   "macrophage does not migrate, the infection is localized, as in the cutaneous sore; if it migrates, the "
   "infection is systemic, with high intermittent fever, weight loss and enlarged spleen, liver and lymph nodes."),
  [("Whether the cell forms a cyst",
    "Cyst formation belongs to intestinal protozoa such as Entamoeba histolytica and Giardia lamblia. Leishmania "
    "stays inside macrophages, and spread depends on whether the macrophage migrates: localized if it stays, "
    "systemic if it moves.",
    "intestinal protozoan form borrowed"),
   ("Which subspecies caused it",
    "Subspecies decide the pace of African sleeping sickness: the Rhodesian strain is acute and the Gambian strain "
    "chronic. For Leishmania, localized against systemic disease turns on whether the infected macrophage "
    "migrates.",
    "African trypanosome subspecies borrowed"),
   ("Which insect species delivered it",
    "Leishmaniasis is transmitted among mammalian hosts by female sand flies, so the insect does not separate one "
    "outcome from the other. Whether the disease stays localized or becomes systemic depends on whether the "
    "macrophage migrates.",
    "vector assumed to set severity")],
  c(16, 41, 45, 46, 52, 53)),

Q("Leishmania", IO1,
  "Which form of leishmaniasis is the most severe and fatal if untreated?",
  ("Kala azar",
   "Correct. Leishmaniasis takes cutaneous, mucous membrane and systemic (visceral) forms, and kala azar is the "
   "most severe form, fatal if untreated. The cutaneous oriental sore, or Baghdad boil, is a localized "
   "ulcerated sore, and espundia is a chronic infection of the head."),
  [("Baghdad boil",
    "The Baghdad boil, or oriental sore, is the cutaneous form, a localized ulcerated sore that arises when the "
    "infected macrophage does not migrate. The most severe form, fatal if untreated, is kala azar.",
    "localized form taken for the severe one"),
   ("Espundia",
    "Espundia is a chronic skin and mucous membrane infection of the head that occurs after the cutaneous form; it "
    "is not the most severe form. Kala azar is the most severe form and fatal if untreated.",
    "chronic form taken for the fatal one"),
   ("Primary chancre",
    "A primary chancre is the skin lesion where a tsetse fly inoculates Trypanosoma brucei, not a form of "
    "leishmaniasis. Among the forms of leishmaniasis, kala azar is the most severe and fatal if untreated.",
    "African trypanosome lesion")],
  c(5, 46, 52, 53)),
]


# Near-twins for the partition: at most the stated number of each group per 30-question set.
CLUSTERS_A = [
    (1, ["Why is Chagas disease becoming more of an", "A lifelong resident of the southern United"]),   # starred twins
    (1, ["Besides swimming or diving in lakes, which", "After entering the body, by which path does"]),  # olfactory -> nose
    (1, ["In what kind of water does Naegleria fowle", "A previously healthy person develops headac"]),  # lake in vignette
    (1, ["How do humans usually acquire Entamoeba his", "Amebiasis epidemics sometimes occur in pris"]),  # water -> route
    (1, ["How do humans usually acquire Entamoeba his", "Giardiasis is common in campers. How is Gia"]),  # same route
    (1, ["Balantidium coli normally lives in the inte", "Which animals are reservoirs of Giardia lam"]),  # host lists cross
]
