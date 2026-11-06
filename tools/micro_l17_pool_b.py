# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 17 — Parasites of Medical Importance (Dr. Webster, 6 November 2026), pool B: the
# APICOMPLEXANS, deck slides 55-77 — Plasmodium and malaria, the coccidian parasites (Toxoplasma gondii,
# Sarcocystis, Cryptosporidium, Isospora belli, Cyclospora cayetanensis) and Babesia — plus these organisms' rows
# on the summary-table pictures (slides 5 and 6) and the protozoa-and-sources table picture (slide 13). Pool A holds
# the amebas, ciliate and flagellates (and the general and drug slides); pool C holds the helminths. Facts from
# those organisms appear here only inside explanations, as the replacing fact for a distractor.
#
# ATTRIBUTION: her file is "Lecture 16 Dr. Webster Parasites of Medical Importance.pptx"; the site calls it
# Lecture 17. 131 slides.
#
# PHASE 1, FROM THE SLIDES ALONE (the recording is not yet transcribed). Every key and every explanation is from
# the VISIBLE slides, text and pictures; speaker notes are not used. Picture-only content used: slide 5 (Plasmodium
# row: Anopheles vector, ring form inside erythrocytes; Toxoplasma row: pregnant women should not clean the cat box
# because of transplacental transmission, danger of central nervous system involvement for patients with acquired
# immunodeficiency syndrome; Trypanosoma brucei photo of flagellates swimming between blood cells), slide 6
# (Cryptosporidium row: gastroenteritis, Wisconsin outbreak from unpurified water), slide 13 (malaria "Human/
# vector-borne"; cyclosporiasis "Water/fresh produce"), slide 59 (the Plasmodium cycle: sporozoites enter a
# capillary with the saliva of a feeding mosquito, liver schizogony, ring trophozoite, "Symptoms" at red-cell
# rupture), slide 60 (ring trophozoites in red blood cells; quiz picture l17-fig-07.jpg), slide 66 (the Toxoplasma
# cycle: sexual phase in the cat, oocysts in feces, pseudocysts with tachyzoites, pseudocysts in the muscle of
# cattle, sheep and chickens), slide 67 (brain computed tomography ring lesion, l17-fig-08.jpg; chorioretinitis,
# l17-fig-09.jpg), slide 73 (Cryptosporidium at a human intestinal cell), slide 76 (acid-fast fecal smear with
# oocysts, l17-fig-10.jpg).
#
# Four options throughout. KEYS SHORT and explanations FULL. Every key is authored at position 0 with the only
# "Correct." opener; the partition rotates positions per set. `mis` names the misconception each distractor
# stands for (review metadata; the renderer strips it).
#
# NOT KEYED FOR COUNT (in scope, but the topic caps of 6 left no room; several appear inside explanations):
# Plasmodium's apicomplexan traits (trophozoites lack locomotor organelles, slide 55), the sickle cell trait and
# mosquito control (61; mosquito control appears in one explanation), the vaccine challenges (62); Toxoplasma's
# coccidian stages (63), serological diagnosis (65; one explanation), vaccine hurdles (65) and the mental-disorder
# links (68, optional "at most once"; not used).
#
# DELIBERATELY NOT ASKED (held), and why:
#   - WHICH DRUG treats what (phase-1 hold): quinine's action and chloroquine, mefloquine, artemether (61);
#     pyrimethamine and sulfadiazine (65, 74); albendazole and corticosteroids (71); trimethoprim and
#     sulfamethoxazole (75); clindamycin, quinine, atovaquone, azithromycin (77). "Increasing drug resistance" (61)
#     is not asked either. Only the general "few effective drugs" for Cryptosporidium (73) appears, in one
#     explanation.
#   - NUMBERS (phase-1 hold): 40% of the world's population, case and death counts, United States and Florida tallies
#     (56, 62); the incubation periods, 5-16 days and 48-72 hour intervals (58, 60); one third seroprevalence (64);
#     the 33% transmission chance (65); the doubled schizophrenia risk (68); shedding counts and infectious dose,
#     the Milwaukee tally (72); 748,000 a year and under 2% (73); the Cyclospora outbreak figures (76; "linked to
#     iceberg lettuce" is used); "older than 50" (77); the vaccine's dose count, cost and effectiveness (62).
#   - HOW MANY Plasmodium species infect humans: slide 13 lists three (vivax, falciparum, malariae), slide 56 lists
#     four (adds ovale). Only "falciparum is the most malignant" is asked; ovale appears as a distractor without any
#     claim about the count.
#   - Toxoplasma as "Zoonotic/vector-borne" (slide 13): contradicts slide 64 (acquired by ingesting raw meats or
#     substances contaminated by cat feces) and slide 66 (no vector in the cycle). No Toxoplasma item keys or
#     offers a vector route.
#   - Cryptosporidium as "Free-living/water, food" (slide 13): slide 72 calls it an intestinal pathogen of mammals,
#     birds and reptiles with tissue and oocyst phases. "Free-living" is never used, and no distractor claims the
#     organism grows in pool water.
#   - Isospora's "Dogs, other mammals" reservoir (slide 13): stated nowhere else; the route asked is slide 74's
#     "fecally contaminated food or drink".
#   - Babesia's risk list (77) is partly hidden behind the tick photograph ("have pre-existing live..."); only the
#     visible "without a spleen" and "immunocompromised" are used.
#   - Gametes or gametocytes in the human blood: slide 58 says merozoites "differentiate into gametes", slide 59
#     says red blood cells give rise to "male and female gametocytes". Neither word is keyed.
#   - the hyena and lion study (70) and the cat-lady cartoons (69): not asked.
# SPELLING: the deck's "Tse tse" is written tsetse; "Amoebic" amebic; "catbox" cat box / litter box; "muscles
# aches" muscle aches; "sarcosystosis" (71, drug line, not used) would be sarcocystosis; "Leishmani" Leishmania;
# "Romana's sign" kept as the deck writes it. RBCs, AIDS, CNS, GI, STD and WHO are written out.
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


POOL_B = [

# ============================================================== PLASMODIUM (slides 55-62, 5, 13)
Q("Plasmodium", IO2,
  "Which vector transmits Plasmodium, the agent of malaria, to humans?",
  ("Female Anopheles mosquito",
   "Correct. The female Anopheles mosquito is the primary vector of Plasmodium. As it feeds, sporozoites from its "
   "salivary glands enter a capillary with its saliva; a mosquito that later draws infected red blood cells hosts "
   "the sexual phase. That is why mosquito control is key."),
  [("Tsetse fly",
    "The tsetse fly spreads Trypanosoma brucei, the cause of African sleeping sickness; its bite inoculates the "
    "skin with trypomastigotes and leaves a primary chancre. Malaria comes from a different insect, the female "
    "Anopheles mosquito, whose bite injects sporozoites.",
    "vector of African sleeping sickness"),
   ("Female sand fly",
    "Female sand flies, which need a blood meal to produce eggs, transmit Leishmania by injecting promastigotes, "
    "with dogs as alternate hosts. Plasmodium is carried by the female Anopheles mosquito, which injects "
    "sporozoites that head first for the liver.",
    "Leishmania vector swapped in"),
   ("Reduviid (kissing) bug",
    "The reduviid or kissing bug is the vector of Trypanosoma cruzi and Chagas disease, and infection occurs when "
    "its feces are inoculated into a cutaneous portal. Plasmodium instead enters a capillary with the saliva of a "
    "feeding female Anopheles mosquito.",
    "Chagas vector swapped in")],
  c(56, 58, 59, 61, 5, 45, 46, 49, 52)),

Q("Plasmodium", IO2,
  "Apart from the bite of its insect vector, by which route can a person acquire Plasmodium?",
  ("Receiving a blood transfusion",
   "Correct. Besides the bite of the female Anopheles mosquito, its primary vector, Plasmodium is transmitted by "
   "blood transfusions and from mother to fetus. That fits a parasite whose erythrocytic phase lives inside red "
   "blood cells, where merozoites become ring trophozoites and multiply."),
  [("Eating undercooked meat",
    "Undercooked meat is how people acquire Sarcocystis from cattle or pigs, and raw meat is one way they acquire "
    "Toxoplasma, whose pseudocysts sit in the muscle of food animals. Plasmodium is a blood parasite passed by "
    "blood transfusion and from mother to fetus.",
    "foodborne coccidian route"),
   ("Nasal contact with lake water",
    "Nasal contact with fresh water is the route of Naegleria fowleri, whose trophozoite burrows through the "
    "nasal mucosa and follows the olfactory nerve into the brain. Plasmodium lives in the blood, so apart from "
    "the mosquito it spreads by blood transfusion and from mother to fetus.",
    "Naegleria route"),
   ("Swallowing oocysts in pool water",
    "Swallowing oocysts in recreational water is how Cryptosporidium spreads, since it can tolerate chlorine in "
    "swimming pools. Plasmodium is a blood parasite: besides the mosquito's bite, it passes by blood transfusion "
    "and from mother to fetus.",
    "Cryptosporidium route")],
  c(56, 58, 64, 66, 71, 28, 29, 72, 73)),

Q("Plasmodium", IO1,
  "After Plasmodium sporozoites enter a capillary with the vector's saliva, where do they localize first?",
  ("The liver",
   "Correct. The injected sporozoite localizes in the liver, invades liver cells and undergoes schizogony, "
   "generating numerous merozoites; this is the exoerythrocytic phase. Only afterward do the merozoites enter the "
   "circulation and invade red blood cells (the erythrocytic phase)."),
  [("Red blood cells",
    "Red blood cells are the second stop, not the first: merozoites released from the liver attach to and enter "
    "them, become ring trophozoites and multiply in the erythrocytic phase. The sporozoite itself goes first to "
    "the liver for schizogony.",
    "erythrocytic phase placed first"),
   ("The intestinal lining",
    "Penetrating intestinal cells is what Cryptosporidium sporozoites do after swallowed oocysts release them. "
    "Plasmodium sporozoites arrive in the blood, not the gut, and localize first in the liver, where schizogony "
    "produces merozoites.",
    "Cryptosporidium sporozoite behavior borrowed"),
   ("The spleen",
    "Enlargement of the spleen, liver and kidneys is a complication of malaria, not the sporozoite's first stop. "
    "The sporozoite invades liver cells and divides there, releasing large numbers of merozoites into the "
    "circulation.",
    "complication mistaken for the first stage")],
  c(58, 59, 60, 73)),

Q("Plasmodium", IO1,
  "What produces the regular episodes of chills, fever and sweating in malaria?",
  ("Infected red blood cells bursting",
   "Correct. In the erythrocytic phase, merozoites enter red blood cells, become ring trophozoites and multiply "
   "until the cell bursts and releases more merozoites. The symptoms recur at intervals as the red blood cells "
   "rupture, and the interval depends on the species."),
  [("Sporozoites dividing in the liver",
    "Schizogony in the liver is the exoerythrocytic phase: it comes first and generates the merozoites that later "
    "enter the circulation. The recurring chills, fever and sweating are timed to red blood cells rupturing, not "
    "to the liver stage.",
    "exoerythrocytic phase blamed"),
   ("Gametes fusing in the bloodstream",
    "Gametes do not fuse in the human: merozoites differentiate into gametes in the blood, but fertilization "
    "happens in the mosquito after it draws infected red blood cells. The cyclic symptoms come from red blood "
    "cells rupturing in the human host.",
    "sexual phase placed in the human host"),
   ("Shifting surface antigens",
    "Changing surface antigens (antigenic variation) is how Trypanosoma brucei evades the immune response in "
    "African sleeping sickness. Malaria's regular chills-fever-sweating episodes follow the cycle of red blood "
    "cells rupturing and releasing merozoites.",
    "trypanosome antigenic variation borrowed")],
  c(58, 59, 60, 46)),

Q("Plasmodium", IO1,
  "Which Plasmodium species causes the most malignant malaria, with the highest death rate in children?",
  ("Plasmodium falciparum",
   "Correct. Plasmodium falciparum is the most malignant type of malaria and has the highest death rate in "
   "children. The malaria species share the regular episodes of chills, fever and sweating as red blood cells "
   "rupture, though the interval between episodes depends on the species."),
  [("Plasmodium vivax",
    "Plasmodium vivax is another malaria species spread by the female Anopheles mosquito, but it is not the one "
    "singled out as the most malignant. That is Plasmodium falciparum, which also carries the highest death rate "
    "in children.",
    "another malaria species (vivax)"),
   ("Plasmodium malariae",
    "Plasmodium malariae causes malaria with the same chills-fever-sweating episodes as red blood cells rupture, "
    "but it is not named the most malignant type. Plasmodium falciparum holds that place, with the highest death "
    "rate in children.",
    "another malaria species (malariae)"),
   ("Plasmodium ovale",
    "Plasmodium ovale is named among the species that cause malaria, but it is not the malignant one. The most "
    "malignant type, with the highest death rate in children, is Plasmodium falciparum; the other species differ "
    "in the interval between episodes.",
    "another malaria species (ovale)")],
  c(56, 60)),

Q("Plasmodium", IO1,
  "Diagnosis rests on finding the small stained forms seen inside these red blood cells. Which stage of the "
  "parasite are they?",
  ("Trophozoites",
   "Correct. These are ring trophozoites of Plasmodium inside red blood cells: merozoites that enter red cells "
   "convert to circular ring trophozoites and multiply. Malaria is diagnosed by the presence of trophozoites in "
   "red blood cells, together with the symptoms."),
  [("Sporozoites",
    "Sporozoites are the stage the mosquito injects; they localize in the liver, not inside red blood cells, and "
    "undergo schizogony there. The forms seen within red cells on a blood smear are trophozoites, the stage used "
    "for diagnosis.",
    "injected stage confused with the blood stage"),
   ("Trypomastigotes",
    "Trypomastigotes are the large, fully formed, spindle-shaped trypanosome stage; on a blood smear they are "
    "flagellates swimming between the cells, not forms inside them. Small forms within red blood cells are "
    "Plasmodium trophozoites.",
    "trypanosome blood form confused"),
   ("Tachyzoites",
    "Tachyzoites are Toxoplasma gondii forms packed inside pseudocysts, and toxoplasmosis is diagnosed by "
    "serological tests, culture and histological analysis. Forms inside red blood cells on a blood smear are "
    "Plasmodium trophozoites.",
    "Toxoplasma stage confused")],
  ci(60, 5, 58, 59, 42, 44, 65, 66),
  img=IMG + "/l17-fig-07.jpg",
  alt="Stained blood smear: many pale, closely packed red blood cells, several holding small purple loop-shaped "
      "forms; unlabeled pointer lines at the right edge",
  slide="Slide 60"),

# ============================================================== TOXOPLASMA GONDII (slides 63-68, 5)
Q("Toxoplasma gondii", IO2,
  "Which pair of sources can transmit Toxoplasma gondii to humans?",
  ("Raw meat and cat feces",
   "Correct. Toxoplasma lives naturally in cats, which harbor oocysts in the gastrointestinal tract and release "
   "them in feces; people acquire it by ingesting raw meats or substances contaminated by cat feces. Food animals "
   "such as cattle, sheep and chickens carry its pseudocysts in their muscle."),
  [("Raw fish and crustaceans",
    "Inadequately cooked fish carries the Chinese liver fluke, Opisthorchis sinensis, and undercooked crustaceans "
    "carry the lung fluke Paragonimus westermani. Toxoplasma comes instead from raw meat or from substances "
    "contaminated by the feces of cats, its natural host.",
    "fluke sources swapped in"),
   ("Snails and raw aquatic plants",
    "Snails (with contaminated water and vegetables) give rat lungworm, Angiostrongylus cantonensis, and raw "
    "aquatic plants give the liver fluke Fasciola hepatica. Toxoplasma is acquired by ingesting raw meats or "
    "anything contaminated by cat feces.",
    "snail and plant sources swapped in"),
   ("Soil contact with bare feet",
    "Bare feet on contaminated soil let hookworm larvae burrow into the skin. Toxoplasma is ingested instead: in "
    "raw meat holding its pseudocysts, or in substances contaminated by the oocyst-bearing feces of cats.",
    "hookworm skin route")],
  c(64, 66, 5, 96, 99, 116, 117)),

Q("Toxoplasma gondii", IO1,
  "How does infection with Toxoplasma gondii present in most people?",
  ("Unnoticed, or mild sore throat and fever",
   "Correct. Most cases of toxoplasmosis go unnoticed or cause mild symptoms: sore throat, fever and enlarged "
   "lymph nodes. Serious complications arise in immunocompromised individuals, who can suffer brain and heart "
   "damage (Toxoplasma encephalitis), and in a fetus infected across the placenta."),
  [("Rapid brain destruction within days",
    "Rapid destruction of the brain and spinal cord, with death within days, is the meningoencephalitis of "
    "Naegleria fowleri entering through the nose. Toxoplasma infection usually goes unnoticed; brain damage is a "
    "complication in immunocompromised individuals.",
    "Naegleria course borrowed"),
   ("Regular bouts of chills, fever and sweating",
    "Regular episodes of chills, fever and sweating mark malaria, timed to red blood cells rupturing. "
    "Toxoplasmosis in most people goes unnoticed or is mild, with sore throat, fever and enlarged lymph nodes.",
    "malaria pattern borrowed"),
   ("Chronic persistent diarrhea",
    "Chronic persistent diarrhea is what Cryptosporidium can cause in patients with acquired immunodeficiency "
    "syndrome and other immunocompromised hosts. Most Toxoplasma infections pass unnoticed or with a mild sore "
    "throat, fever and enlarged lymph nodes.",
    "Cryptosporidium course in the immunocompromised")],
  c(64, 65, 29, 60, 73)),

Q("Toxoplasma gondii", IO1,
  "A patient with acquired immunodeficiency syndrome has the brain computed tomography scan shown. Which parasite "
  "most likely caused this lesion?",
  ("Toxoplasma gondii",
   "Correct. A brain lesion in a patient with acquired immunodeficiency syndrome is the picture of Toxoplasma "
   "encephalitis. Toxoplasma infection is usually mild, but immunocompromised individuals can suffer brain and "
   "heart damage, so central nervous system involvement is a danger for these patients."),
  [("Naegleria fowleri",
    "Naegleria fowleri enters through the nose, most often in children and young adults exposed to fresh water, "
    "and rapidly destroys the brain and spinal cord. The danger of central nervous system involvement in acquired "
    "immunodeficiency syndrome belongs to Toxoplasma.",
    "brain parasite of swimmers"),
   ("Trypanosoma brucei",
    "Trypanosoma brucei reaches the brain in African sleeping sickness after a tsetse fly bite, bringing "
    "personality changes, sleep disturbances and coma. The clue here is acquired immunodeficiency syndrome, the "
    "setting in which Toxoplasma causes encephalitis.",
    "another protozoan with brain involvement"),
   ("Cryptosporidium",
    "Cryptosporidium is also a danger in acquired immunodeficiency syndrome, but it is an intestinal pathogen "
    "that causes chronic persistent diarrhea. A lesion in the brain of such a patient points to Toxoplasma "
    "encephalitis.",
    "right host, wrong organ")],
  ci(67, 5, 64, 28, 29, 46, 47, 72, 73),
  img=IMG + "/l17-fig-08.jpg",
  alt="Black-and-white axial computed tomography slice of the head showing a single round lesion with a bright "
      "rim on the left side of the image",
  slide="Slide 67"),

Q("Toxoplasma gondii", IO1,
  "This fundus photograph shows a parasitic eye lesion. Which finding is it?",
  ("Chorioretinitis",
   "Correct. The photograph shows the back of the eye with dark, scarred patches: toxoplasmosis chorioretinitis, "
   "an ocular manifestation. With hydrocephalus and intracranial calcifications, it is among the severe findings "
   "in a newborn infected across the placenta from a mother with toxoplasmosis."),
  [("Amebic keratitis",
    "Amebic keratitis is the Acanthamoeba eye infection of contact lens wearers, with eye pain, redness and "
    "irritation, and it does not typically disseminate. The lesion in this photograph lies at the back of the "
    "eye: toxoplasmosis chorioretinitis.",
    "contact-lens eye infection"),
   ("Romana's sign",
    "Romana's sign, or chagoma, is the local lesion of Chagas disease: a swelling of the eyelid with "
    "conjunctivitis. This photograph shows the inside of the eye rather than the lid, and the lesion is "
    "toxoplasmosis chorioretinitis.",
    "Chagas eyelid sign"),
   ("A migrating eye worm",
    "A migrating eye worm is Loa loa, a temperature-sensitive worm that moves around and under the skin and may "
    "enter the eye; it is pulled out through a small hole in the conjunctiva. The lesion here is chorioretinitis, "
    "an ocular manifestation of toxoplasmosis.",
    "Loa loa eye worm")],
  ci(67, 65, 31, 49, 107),
  img=IMG + "/l17-fig-09.jpg",
  alt="Color photograph of the back of the eye: the bright optic disc at the right edge, the dark central spot, "
      "and a cluster of dark pigmented and pale scarred patches below the center",
  slide="Slide 67"),

Q("Toxoplasma gondii", IO1,
  "A woman acquires toxoplasmosis during pregnancy, and the parasite crosses the placenta. Which findings may her "
  "newborn show?",
  ("Hydrocephalus and intracranial calcifications",
   "Correct. Transplacental transmission from a pregnant woman with toxoplasmosis can cause spontaneous abortion, "
   "stillbirth, or severe neurological and ocular manifestations in the newborn, including hydrocephalus, "
   "intracranial calcifications and chorioretinitis. Hence pregnant women should not clean the cat box."),
  [("Eyelid swelling with conjunctivitis and fever",
    "A swelling of the eyelid with conjunctivitis (Romana's sign), with fever, marks Chagas disease from "
    "Trypanosoma cruzi, which can also be transmitted congenitally. Congenital toxoplasmosis brings "
    "hydrocephalus, intracranial calcifications and chorioretinitis.",
    "Chagas findings borrowed"),
   ("Anemia with an enlarged spleen and liver",
    "Anemia and enlargement of the spleen, liver and kidneys are complications of malaria, and Plasmodium can "
    "also pass from mother to fetus. The newborn findings of toxoplasmosis acquired across the placenta are "
    "hydrocephalus, intracranial calcifications and chorioretinitis.",
    "malaria complications borrowed"),
   ("Personality changes and sleep disturbances",
    "Personality and behavioral changes progressing to sleep disturbances belong to African sleeping sickness, "
    "once Trypanosoma brucei reaches the central nervous system after a tsetse fly bite. Toxoplasmosis passed "
    "across the placenta gives hydrocephalus and intracranial calcifications.",
    "sleeping sickness neurological signs")],
  c(65, 5, 49, 56, 60, 46, 47)),

Q("Toxoplasma gondii", IO2,
  "Which group is advised not to clean a cat's litter box because of Toxoplasma gondii?",
  ("Pregnant women",
   "Correct. Cats harbor Toxoplasma oocysts and release them in their feces, and a pregnant woman who acquires "
   "toxoplasmosis can transmit it across the placenta to her fetus. So pregnant women should not clean the cat "
   "box, because of the danger of transplacental transmission."),
  [("Contact lens wearers",
    "Contact lens wearers are the group at risk for amebic keratitis from Acanthamoeba, which lives in freshwater "
    "lakes, hot tubs and swimming pools. The cat box warning concerns Toxoplasma and pregnant women, because the "
    "parasite can cross the placenta.",
    "Acanthamoeba risk group"),
   ("Children in daycare",
    "Daycare is the classic setting for pinworm, Enterobius vermicularis, spread by direct contact and fomites. "
    "The advice to avoid cleaning the cat box is aimed at pregnant women, since Toxoplasma from cat feces can "
    "pass across the placenta to the fetus.",
    "pinworm risk group"),
   ("People without a spleen",
    "People without a spleen face serious babesiosis, a tick-borne infection of red blood cells by Babesia "
    "microti. The cat box warning is for pregnant women, because Toxoplasma shed in cat feces can be transmitted "
    "across the placenta.",
    "Babesia risk group")],
  c(5, 64, 65, 31, 6, 77)),

# ============================================================== OTHER COCCIDIA (slides 63, 71, 77)
Q("Other coccidia", IO2,
  "Cattle and pigs pick up Sarcocystis cysts while grazing on grass contaminated with human feces, and people are "
  "infected by eating their undercooked meat. What role do these animals play in the parasite's life cycle?",
  ("Intermediate hosts",
   "Correct. For Sarcocystis, domestic animals are the intermediate hosts: they pick up infective cysts while "
   "grazing on grass contaminated with human feces, and humans are infected when the undercooked meat is eaten. "
   "Sarcocystis hominis comes from cattle and Sarcocystis suihominis from pigs."),
  [("Definitive hosts",
    "The definitive host is where adulthood and mating occur. The grazing cattle and pigs are named the "
    "intermediate hosts of Sarcocystis: they pick up the cysts from contaminated grass and pass the infection on "
    "to people in their meat.",
    "host roles reversed"),
   ("Transport hosts",
    "A transport host experiences no parasitic development and simply carries a parasite on toward its definitive "
    "host. Cattle and pigs are called the intermediate hosts of Sarcocystis: they acquire infective cysts while "
    "grazing, and people catch it from their undercooked meat.",
    "transport host confused"),
   ("Dead-end hosts",
    "It is humans, not the grazing animals, who can be dead-end hosts for other Sarcocystis species, and then "
    "they develop muscle cysts, myalgia, weakness and edema. Cattle and pigs are the intermediate hosts whose "
    "undercooked meat infects people.",
    "dead-end role reversed")],
  c(71, 79, 108)),

Q("Other coccidia", IO2,
  "Which vector carries Babesia microti, the cause of human babesiosis?",
  ("Blacklegged deer tick",
   "Correct. Human babesiosis is caused by Babesia microti carried by the blacklegged deer tick; Babesia was the "
   "first protozoan found to be associated with a vector, the tick. The parasite attacks red blood cells and can "
   "cause hemolytic anemia; babesiosis is serious for people without a spleen."),
  [("Female Anopheles mosquito",
    "The female Anopheles mosquito carries Plasmodium, which also invades red blood cells and causes anemia, so "
    "the two are easy to confuse. Babesia microti is carried by the blacklegged deer tick, and Babesia was the "
    "first protozoan linked to a vector at all.",
    "malaria vector swapped in"),
   ("Reduviid (kissing) bug",
    "The reduviid or kissing bug is the vector of Trypanosoma cruzi and Chagas disease, which is becoming more of "
    "an issue in the southern United States as the vector migrates. Babesia microti reaches people through the "
    "blacklegged deer tick.",
    "Chagas vector swapped in"),
   ("Female sand fly",
    "Female sand flies, which need a blood meal to make eggs, transmit Leishmania among mammals, with dogs as "
    "alternate hosts. Babesiosis is a tick-borne zoonosis: Babesia microti is carried by the blacklegged deer "
    "tick and attacks red blood cells.",
    "Leishmania vector swapped in")],
  c(77, 56, 60, 48, 49, 52)),

# ============================================================== CRYPTOSPORIDIUM (slides 72-73, 6, 13)
Q("Cryptosporidium", IO2,
  "A swimmer develops diarrhea, vomiting and abdominal cramps after swimming in a properly chlorinated public pool. "
  "Which protozoan is the most likely cause?",
  ("Cryptosporidium",
   "Correct. Cryptosporidium is the leading cause of recreational waterborne disease and can tolerate the "
   "chlorine in swimming pools. Swallowed oocysts release sporozoites that penetrate intestinal cells, causing "
   "gastroenteritis with headache, sweating, vomiting, abdominal cramps and diarrhea."),
  [("Naegleria fowleri",
    "Naegleria fowleri inhabits unchlorinated pools, lakes and hot springs, enters through the nose and destroys "
    "the brain and spinal cord, with headache, fever, vomiting and a stiff neck. A chlorinated pool and "
    "gastroenteritis point to Cryptosporidium, which tolerates chlorine.",
    "pool organism with brain disease"),
   ("Acanthamoeba",
    "Acanthamoeba lives in swimming pools, hot tubs and freshwater lakes, but its diseases are amebic keratitis "
    "in contact lens wearers and granulomatous amebic encephalitis. Vomiting, cramps and diarrhea after pool "
    "water fit Cryptosporidium, which tolerates chlorine.",
    "pool organism with eye or brain disease"),
   ("Balantidium coli",
    "Balantidium coli does cause diarrhea and abdominal pain, but it comes from the intestines of pigs and cattle "
    "in cyst-containing food or water, and healthy humans are resistant. Illness after a chlorinated pool fits "
    "Cryptosporidium, which tolerates chlorine.",
    "intestinal protozoan from pigs")],
  c(72, 73, 24, 29, 31, 33)),

Q("Cryptosporidium", IO1,
  "Which groups are most likely to be infected with Cryptosporidium?",
  ("Young children, the elderly",
   "Correct. Young children and the elderly are likely to be infected with Cryptosporidium, which spreads in "
   "recreational water and in contaminated water, ice and foodstuffs. Patients with acquired immunodeficiency "
   "syndrome and other immunocompromised hosts may suffer chronic persistent diarrhea."),
  [("Young, sexually active women",
    "Young, sexually active women are the group in whom Trichomonas vaginalis causes the most common curable "
    "sexually transmitted disease. Cryptosporidium is swallowed in water or food, and young children and the "
    "elderly are the groups likely to be infected.",
    "Trichomonas risk group"),
   ("Pregnant women who keep cats",
    "Pregnant women are warned away from the cat box because Toxoplasma from cat feces can cross the placenta. "
    "Cryptosporidium's at-risk groups are young children and the elderly, along with immunocompromised patients, "
    "who may suffer chronic persistent diarrhea.",
    "Toxoplasma risk group"),
   ("Contact lens wearers",
    "Contact lens wearers are at risk for amebic keratitis from Acanthamoeba in pools, hot tubs and lakes. "
    "Cryptosporidium also spreads in pools, but it causes gastroenteritis, and young children and the elderly "
    "are the groups likely to be infected.",
    "Acanthamoeba risk group")],
  c(72, 73, 37, 5, 65, 31)),

Q("Cryptosporidium", IO1,
  "What can Cryptosporidium cause in a patient with acquired immunodeficiency syndrome?",
  ("Chronic persistent diarrhea",
   "Correct. Cryptosporidium is an intestinal pathogen: swallowed oocysts release sporozoites that penetrate "
   "intestinal cells and cause gastroenteritis. Patients with acquired immunodeficiency syndrome and other "
   "immunocompromised hosts may suffer chronic persistent diarrhea, and few drugs are effective against it."),
  [("Encephalitis with brain damage",
    "Brain and heart damage, Toxoplasma encephalitis, is the serious complication of toxoplasmosis in "
    "immunocompromised individuals. Cryptosporidium is an intestinal pathogen, and in acquired immunodeficiency "
    "syndrome its danger is chronic persistent diarrhea.",
    "Toxoplasma complication borrowed"),
   ("Severe hemolytic anemia",
    "Hemolytic anemia results when Babesia microti, carried by the blacklegged deer tick, attacks red blood "
    "cells, and babesiosis is serious in the immunocompromised. Cryptosporidium invades intestinal cells "
    "instead, causing chronic persistent diarrhea in these patients.",
    "Babesia complication borrowed"),
   ("Cyclic chills, fever and sweating",
    "Regular episodes of chills, fever and sweating come from Plasmodium as red blood cells rupture in malaria. "
    "Cryptosporidium is an intestinal pathogen; in acquired immunodeficiency syndrome it may cause chronic "
    "persistent diarrhea.",
    "malaria pattern borrowed")],
  c(72, 73, 64, 77, 60)),

Q("Cryptosporidium", IO1,
  "After Cryptosporidium oocysts are swallowed, what do the sporozoites they release do?",
  ("Penetrate intestinal cells",
   "Correct. Ingestion of Cryptosporidium oocysts gives rise to sporozoites that penetrate intestinal cells; the "
   "organism exists in tissue and oocyst phases. This intestinal invasion produces gastroenteritis, with "
   "headache, sweating, vomiting, abdominal cramps and diarrhea."),
  [("Localize in the liver",
    "Localizing in the liver is what Plasmodium sporozoites do after a mosquito injects them, before schizogony "
    "releases merozoites into the blood. Cryptosporidium arrives by mouth, and its sporozoites penetrate "
    "intestinal cells.",
    "Plasmodium sporozoite route borrowed"),
   ("Enter red blood cells",
    "Entering red blood cells is the work of Plasmodium merozoites, which become ring trophozoites, and Babesia "
    "also attacks red cells. Cryptosporidium is an intestinal pathogen whose sporozoites penetrate the cells of "
    "the intestine.",
    "blood-stage parasites borrowed"),
   ("Travel up the olfactory nerve",
    "Traveling along the olfactory nerve into the brain is how Naegleria fowleri trophozoites reach the central "
    "nervous system after burrowing through the nasal mucosa. Swallowed Cryptosporidium oocysts release "
    "sporozoites that penetrate intestinal cells.",
    "Naegleria route borrowed")],
  ci(73, 72, 58, 59, 77, 29)),

# ============================================================== ISOSPORA BELLI (slide 74, 6, 13)
Q("Isospora belli", IO2,
  "By which route is Isospora belli transmitted to humans?",
  ("Fecally contaminated food or drink",
   "Correct. Isospora belli, an intracellular intestinal parasite with an oocyst stage, is transmitted in fecally "
   "contaminated food or drink. Infection is usually asymptomatic or self-limited and is primarily associated "
   "with immunocompromised hosts."),
  [("The bite of a blacklegged deer tick",
    "The blacklegged deer tick carries Babesia microti, a parasite that attacks red blood cells. Isospora belli "
    "is an intracellular intestinal parasite, transmitted in fecally contaminated food or drink and causing "
    "diarrhea, fatty stools and weight loss.",
    "Babesia vector borrowed"),
   ("Undercooked beef or pork",
    "Undercooked beef or pork is the source of Sarcocystis hominis and Sarcocystis suihominis, whose cysts the "
    "grazing cattle and pigs carry in their meat. Isospora belli is transmitted in fecally contaminated food or "
    "drink.",
    "Sarcocystis route borrowed"),
   ("Sexual contact with a partner",
    "Sexual contact transmits Trichomonas vaginalis, whose reservoir is the human urogenital tract; it causes the "
    "most common curable sexually transmitted disease in young women. Isospora belli is an intestinal parasite "
    "carried in fecally contaminated food or drink.",
    "Trichomonas route borrowed")],
  c(74, 77, 71, 37)),

Q("Isospora belli", IO1,
  "With which hosts is Isospora belli infection primarily associated?",
  ("Immunocompromised hosts",
   "Correct. Isospora belli infection is usually asymptomatic or self-limited, but it is primarily associated with "
   "immunocompromised hosts. Symptoms include malaise, nausea and vomiting, diarrhea, fatty stools, abdominal "
   "cramping and weight loss."),
  [("Children in temperate zones",
    "Children in temperate zones are the group for enterobiasis, the most common worm disease of children there, "
    "spread when pinworm eggs are picked up and swallowed. Isospora belli is primarily associated with "
    "immunocompromised hosts.",
    "pinworm group borrowed"),
   ("Pregnant women",
    "Pregnant women are the concern with Toxoplasma gondii, which can cross the placenta and harm the fetus. "
    "Isospora belli, spread in fecally contaminated food or drink, is primarily associated with "
    "immunocompromised hosts.",
    "Toxoplasma group borrowed"),
   ("Contact lens wearers",
    "Contact lens wearers are at risk for amebic keratitis, an Acanthamoeba eye infection with pain, redness and "
    "irritation. Isospora belli is an intestinal parasite primarily associated with immunocompromised hosts, "
    "causing diarrhea, fatty stools and weight loss.",
    "Acanthamoeba group borrowed")],
  c(74, 94, 65, 31)),

# ============================================================== CYCLOSPORA CAYETANENSIS (slides 75-76, 6, 13)
Q("Cyclospora cayetanensis", IO2,
  "Through which vehicles is Cyclospora cayetanensis transmitted?",
  ("Fresh produce and water",
   "Correct. Cyclospora cayetanensis, an emerging protozoan pathogen, has oral-fecal transmission through fresh "
   "produce and water, and a widespread outbreak was linked to iceberg lettuce. Swallowed oocysts enter the small "
   "intestine and invade the mucosa, causing watery diarrhea, stomach cramps and bloating."),
  [("Undercooked beef and pork",
    "Undercooked beef and pork carry Sarcocystis hominis and Sarcocystis suihominis, and pork or bear meat "
    "carries Trichinella. Cyclospora's vehicles are fresh produce and water, by the oral-fecal route, as in an "
    "outbreak linked to iceberg lettuce.",
    "meat-borne parasites borrowed"),
   ("Raw fish and crustaceans",
    "Inadequately cooked fish transmits the Chinese liver fluke, Opisthorchis sinensis, and undercooked "
    "crustaceans the lung fluke Paragonimus westermani. Cyclospora cayetanensis spreads instead through fresh "
    "produce and water, by the oral-fecal route.",
    "fluke vehicles borrowed"),
   ("Mosquito bites and transfusions",
    "Mosquito bites and blood transfusions transmit Plasmodium, a parasite of red blood cells. Cyclospora is an "
    "intestinal parasite with oral-fecal transmission through fresh produce and water; its oocysts invade the "
    "mucosa of the small intestine.",
    "malaria routes borrowed")],
  c(75, 76, 13, 71, 101, 116, 56)),

Q("Cyclospora cayetanensis", IO1,
  "An acid-fast stained fecal smear from a patient with watery diarrhea, bloating and stomach cramps shows the "
  "round red-staining bodies seen here. Which parasite is it?",
  ("Cyclospora cayetanensis",
   "Correct. Round oocysts that take up the acid-fast stain in a fecal smear are Cyclospora cayetanensis, the "
   "cause of cyclosporiasis, with watery diarrhea, stomach cramps, bloating, fever and muscle aches. Diagnosis can "
   "be complicated, so multiple stool samples must be tested."),
  [("Giardia lamblia",
    "Giardia lamblia is recognized by its trophozoite's symmetrical heart shape, with a concave ventral surface "
    "that acts like a suction cup, and microscopy is difficult because it is shed intermittently. Round "
    "acid-fast-staining oocysts point to Cyclospora.",
    "intestinal flagellate confused"),
   ("Entamoeba histolytica",
    "Entamoeba histolytica is also sought in a fecal smear, but it shows a large trophozoite moving by pseudopods "
    "or a smaller nonmotile cyst, and it causes dysentery. Round oocysts staining with the acid-fast method are "
    "Cyclospora cayetanensis.",
    "ameba confused"),
   ("Balantidium coli",
    "Balantidium coli is a ciliate from the intestines of pigs and cattle that causes persistent diarrhea and "
    "occasionally dysentery. The bodies in this acid-fast fecal smear are oocysts, the form of Cyclospora "
    "cayetanensis that invades the small intestinal mucosa.",
    "intestinal ciliate confused")],
  ci(76, 75, 39, 41, 16, 23, 33),
  img=IMG + "/l17-fig-10.jpg",
  alt="Fecal smear stained blue with scattered round bodies stained pink to deep red, a 20 micrometer scale bar, "
      "and unlabeled pointer lines",
  slide="Slide 76"),
]


# Near-twins for the partition: at most N of each group per 30-question set.
CLUSTERS_B = [
    (1, ["Which pair of sources can transmit Toxoplasma",          # its key (cat feces) is hinted by the
         "Which group is advised not to clean a cat's litter"]),  # cat-box stem
    (1, ["A woman acquires toxoplasmosis during pregnancy",      # stem hands over "pregnant women"
         "Which group is advised not to clean a cat's litter"]),
    (1, ["After Plasmodium sporozoites enter a capillary",       # mirrored sporozoite destinations
         "After Cryptosporidium oocysts are swallowed"]),
    (1, ["A patient with acquired immunodeficiency syndrome has",  # Cryptosporidium's role in the immunocompromised
         "What can Cryptosporidium cause in a patient with"]),     # eliminates a distractor of the brain-scan item
]
