# -*- coding: utf-8 -*-
# Microbiology Exam 3 — "Webster Review" forms A and B, Lecture 17 (Parasites of Medical Importance).
# Her file is "Lecture 16 Dr. Webster Parasites of Medical Importance.pptx"; the site calls it Lecture 17.
#
# COUNTS: 20 per form, 40 in all. One question per review item (2.1-2.18, 17 items) in each form, plus extras:
#   A: 2.1 (Entamoeba histolytica, second fact), 2.9 (Plasmodium, second fact), 2.12 (worm damage, second fact);
#   B: 2.2 (Acanthamoeba alongside Naegleria), 2.7 (Trypanosoma cruzi, second fact), 2.14 (Trichinella, second fact).
#   Alternating pairs: 2.11 A = Cyclospora, B = Cryptosporidium; 2.15 A = Loa loa, B = Toxocara;
#   2.16 A = Schistosoma, B = Opisthorchis sinensis; 2.17 A = Taenia solium (cysticercosis), B = Echinococcus.
#   Light touch keyed nowhere: Balantidium coli, Isospora belli (Isospora is never a key, nor a distractor here).
#
# PICTURE ITEMS (her "if I give you a picture, be able to recognize it"): 6 per form, each picture used once.
#   A: wr3-fig-07 (Giardia cysts, 2.4), 05 (Trichomonas, 2.5), 09 (Plasmodium rings, 2.9), 10 (Cyclospora acid-fast
#      smear, 2.11), 13 (Loa loa in the eye, 2.15), 14 (cysticercosis brain slice, 2.17).
#   B: wr3-fig-04 (Naegleria trophozoites, 2.2), 06 (Giardia trophozoite, 2.4), 08 (Trypanosoma brucei between red
#      cells, 2.6), 11 (pinworm eggs, 2.13), 12 (Trichinella larvae in muscle, 2.14), 15 (hydatid cyst, 2.17).
#   Labels come from the slides: slide 4 (Naegleria photo, Giardia cyst photo, Trichomonas photo), slide 5
#   (Trypanosoma brucei "flagellates swimming between cells"; Plasmodium "ring form inside erythrocytes"), slide 7
#   (Trichinella muscle photo), slide 8 (cysticercosis and Echinococcus photos), slide 40 ("Identification of
#   trophozoites": drawn trophozoite and cyst beside the two photos), slide 76 caption ("Cyclospora in fecal smear with
#   acid fast stain"), slide 95 (pinworm eggs beside the Enterobius cycle), slide 107 (Loa loa), slide 123
#   ("Cysticercosis"), slide 125 (Echinococcus surgery photo).
#   HELD: wr3-fig-03 (slide 15, amebas in tissue). Slide 15 is titled only "Infective Amebas" and names no organism
#   or stage, so no defensible single answer can be built on it.
#
# HER WORDS vs THE SLIDES (slide keyed every time):
#   - Plasmodium "does not have a trophozoite form": slides 58 and 60 describe ring trophozoites in red cells and
#     diagnosis "by presence of trophozoite in RBCs". Keyed: ring trophozoites in red blood cells (B 2.9).
#   - Leishmania "sand fleas": slides 5 and 52 say sand flies. Keyed: the female sand fly (A 2.8).
#   - Chagas "reduva beetle or kissing bug": slides 5 and 49 say reduviid (kissing) bug. Keyed: bug (A/B 2.7).
#   - Trichomonas seen in "vaginal secretions, or semen": slide 38 says "microscopic analysis of vaginal smear";
#     semen is never used.
#   - Trichinella damages "skeletal muscle, but also smooth muscle ... cardiac muscle": slide 101 says larvae go to
#     "muscle, heart, and brain". Keyed the slide's list (A 2.14); smooth muscle not used.
#   - Acanthamoeba "the same thing, only a longer incubation time": slide 31 says "Symptoms of meningitis—but longer
#     progression" and entry "through break in skin or through nasal passages". Keyed "longer progression" (B 2.2).
#   - Naegleria fatal "if you do not treat it within the first few days": slide 29 says "Treatment—Must be early" and
#     death in days. No item keys a treatment window.
#   - Trypanosoma brucei: her "saliva containing the anticoagulant" is on no slide; slide 46 says the fly's bite
#     inoculates the skin with trypomastigotes. Not used.
#   - Toxoplasma transmission to the baby "can be fatal": slide 65 says spontaneous abortion, stillbirth or severe
#     neurological and ocular problems. Explanations use the slide's words.
#   - Leishmania "alternate host the dog" and the Chinese liver fluke "fresh water sushi": both match the slides
#     (52 and 5: "alternate hosts dogs"; 8: "don't eat freshwater sushi", 116: "inadequately cooked fish").
#   - 2.18 "why fewer drugs ... because they're eukaryotic": slide 14 supports it ("Relatively few in comparison with
#     antibacterial agents / Work against eukaryotic cells / Toxicity problems, severe side effects"), so form A asks
#     it directly; form B uses slide 86 ("Many antihelminthic drugs have toxic side effects").
#
# Other slide-internal notes: slide 8 says the beef tapeworm causes "weight loss and wasting", slide 119 says "few
# symptoms"; the A 2.12 item (repaired) asks only how the tapeworm obtains food, keyed "absorption through its body"
# from slide 118 ("No mouth—nutrients absorbed through body"), and claims no harm or severity. Onchocerca volvulus was kept out of the Loa loa picture
# item (slide 106: its adult females migrate to the eyes, a possible second answer); Echinococcus was kept out of the
# cysticercosis item (slide 124: alveolar form causes parasitic tumors in the brain); Entamoeba histolytica was kept
# out of the hydatid-cyst item (slide 21: liver abscesses).
#
# She said "I'm not going to ask you a picky detail": items stay at organism identity, vector or source, disease and
# signature finding. No drug names, doses, case counts or years are asked.
# Grounding: visible slide text and pictures only (no speaker notes, no spoken asides).
# Stems avoid the existing Lecture 17 topic-quiz stems (scratchpad existing_l17_stems.txt); where the same picture
# appears in a topic quiz, this pool asks a different fact of it.
# KEYS ARE WRITTEN SHORT ON PURPOSE — detail lives in the explanation. Key authored at index 0 (c=0); positions are
# permuted later by the renderer.

SRC = "Lecture 16 Dr. Webster Parasites of Medical Importance.pptx"   # her file name; the site calls it Lecture 17
IMG = "micro-exam-3-quiz-images"


def c(*n):
    return f"{SRC}, Slide" + (" " + str(n[0]) if len(n) == 1 else "s " + ", ".join(map(str, n[:-1])) + " and " + str(n[-1]))


def ci(img, *n):
    """cite with a picture slide: c(n...) + ' and image on Slide img'"""
    return (c(*n) + f" and image on Slide {img}") if n else f"{SRC}, image on Slide {img}"


IO1 = ("1 — Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, "
       "clinical manifestations, methods of treatment, and prevention of parasites of medical importance")
IO2 = "2 — Describe the modes of transmission by which humans acquire parasites of medical importance"


def Q(item, tier, form, topic, io, q, key, others, cite, img=None, alt=None):
    d = dict(lecture=17, item=item, tier=tier, form=form, topic=topic, io=io, q=q,
             opts=[[key[0], key[1]]] + [[t, e] for t, e, _ in others],
             mis={t: m for t, _, m in others}, c=0, cite=cite)
    if img:
        d["img"] = f"{IMG}/{img}"
        d["alt"] = alt
    return d


POOL = [

# =============================================================================================== FORM A
# ---------------------------------------------------------------- 2.1 (cold) Entamoeba histolytica, x2
Q("2.1", "cold", "A", "Entamoeba histolytica: the trophozoite", IO1,
  "Entamoeba histolytica alternates between two forms. Which form attaches in the bowel, actively moves about and "
  "feeds?",
  ("The trophozoite",
   "Correct: the trophozoite is the large form, motile by means of pseudopods. After cysts are swallowed, the "
   "trophozoites they release attach, multiply, actively move about and feed, and active trophozoites also fill the "
   "liver abscesses of extraintestinal amebiasis."),
  [("The cyst",
    "The cyst is the smaller, nonmotile form: it is the form swallowed to start infection and is produced after the "
    "active phase of disease. The form that attaches, moves and feeds, released from the cyst in the small "
    "intestine, is the trophozoite.",
    "reverses the motile feeding form and the nonmotile resting form"),
   ("The merozoite",
    "Merozoites are Plasmodium forms released from the liver that enter red blood cells; they are not an Entamoeba "
    "stage. Entamoeba histolytica alternates only between a motile, feeding trophozoite and a smaller nonmotile cyst.",
    "borrows a malaria stage name"),
   ("The oocyst",
    "Oocysts are the dormant stage of coccidian parasites such as Cryptosporidium and Cyclospora, swallowed in "
    "contaminated water or food. Entamoeba histolytica's feeding form in the bowel is the trophozoite, not an oocyst.",
    "borrows a coccidian stage name")],
  c(16, 19, 21, 58, 63)),

Q("2.1", "cold", "A", "Entamoeba histolytica: amebic dysentery", IO1,
  "A person in a tropical region with poor sewage treatment develops dysentery, abdominal pain, fever and weight "
  "loss. Amebas that secrete tissue-dissolving enzymes are eroding the colon. Which organism is the cause?",
  ("Entamoeba histolytica",
   "Correct: Entamoeba histolytica causes amebiasis, or amebic dysentery, spread by the fecal-oral route and "
   "prevalent in tropical countries where fertilization practices and sewage treatment allow it. It targets the "
   "cecum, appendix, colon and rectum, secreting enzymes that dissolve tissue, with dysentery, pain, fever and weight "
   "loss."),
  [("Giardia lamblia",
    "Giardia lamblia is a heart-shaped flagellate, not an ameba; its trophozoites feed and multiply in the jejunum "
    "and cause giardiasis with diarrhea and abdominal pain. Amebas eroding the colon with dysentery point to "
    "Entamoeba histolytica.",
    "confuses the intestinal flagellate with the intestinal ameba"),
   ("Naegleria fowleri",
    "Naegleria fowleri is an ameba, but it is acquired through nasal contact with fresh water and travels along the "
    "olfactory nerve to the brain, causing primary acute meningoencephalitis. The colon-eroding ameba that causes "
    "dysentery is Entamoeba histolytica.",
    "right group (ameba), wrong organ"),
   ("Cryptosporidium",
    "Cryptosporidium is an apicomplexan, not an ameba; its sporozoites penetrate intestinal cells and cause "
    "gastroenteritis with cramps and diarrhea, chronic in immunocompromised people. Amebas dissolving the colon wall "
    "with dysentery are Entamoeba histolytica.",
    "picks another waterborne intestinal protozoan")],
  c(4, 16, 17, 20, 29, 39, 41, 72, 73)),

# ---------------------------------------------------------------- 2.2 (cold) Naegleria fowleri
Q("2.2", "cold", "A", "Naegleria fowleri: path to the brain", IO2,
  "A child develops meningoencephalitis after diving into a freshwater lake, and Naegleria fowleri is found. By "
  "which path did the organism reach the brain?",
  ("Through the nose, along the olfactory nerve",
   "Correct: Naegleria fowleri is acquired through nasal contact with water, as in diving, waterskiing or rinsing the "
   "sinuses. The trophozoite burrows through the nasal mucosa and travels into the brain along the olfactory nerve, "
   "causing rapid destruction of the brain and spinal cord."),
  [("From the gut through the bloodstream",
    "Spread from the gut to other organs fits Entamoeba histolytica, whose swallowed cysts release trophozoites "
    "that can invade the liver and other viscera. Naegleria is not swallowed: it enters through nasal contact with "
    "water and follows the olfactory nerve.",
    "pictures every ameba as swallowed"),
   ("Through a break in the skin",
    "Entry through a break in the skin is typical of Acanthamoeba, whose granulomatous amoebic encephalitis has a "
    "longer progression. Naegleria fowleri burrows through the nasal mucosa after water enters the nose and reaches "
    "the brain along the olfactory nerve.",
    "confuses Naegleria with Acanthamoeba"),
   ("Through an insect bite and the blood",
    "An insect bite followed by spread in the blood describes Trypanosoma brucei, inoculated by the tsetse fly before "
    "it reaches the brain. Naegleria fowleri has no vector: it lives in warm fresh water and enters through the nose.",
    "assumes a vector carries every brain parasite")],
  c(24, 28, 29, 31, 21, 45, 46)),

# ---------------------------------------------------------------- 2.4 (cold) Giardia lamblia — PICTURE (cysts)
Q("2.4", "cold", "A", "Giardia lamblia: cysts in stool (picture)", IO1,
  "A stool specimen from a camper with diarrhea and abdominal pain shows the oval bodies pictured. What are they?",
  ("Giardia lamblia cysts",
   "Correct: these oval, thick-walled bodies with internal nuclei are Giardia lamblia cysts, which are small, compact "
   "and multinucleate. Cysts survive in the environment and are ingested with water and food; in the duodenum they "
   "germinate, and the trophozoites feed and multiply in the jejunum."),
  [("Giardia lamblia trophozoites",
    "The Giardia trophozoite is a symmetrical heart shape with flagella and a concave ventral surface that acts like "
    "a suction cup, not an oval walled body. These oval, compact, multinucleate forms are the cysts the camper "
    "swallowed and later shed.",
    "confuses the two Giardia forms"),
   ("Entamoeba histolytica trophozoites",
    "Entamoeba histolytica trophozoites are large, move by pseudopods and have one large nucleus; they invade the "
    "colon and cause amebic dysentery. Small oval walled bodies in a camper's stool, each holding several nuclei, "
    "are Giardia lamblia cysts.",
    "picks the other intestinal protozoan"),
   ("Cyclospora oocysts",
    "Cyclospora oocysts are found with an acid-fast stain of a fecal smear, where they show as round red-staining "
    "bodies. The oval, multinucleate bodies here are Giardia lamblia cysts.",
    "picks another cyst-forming waterborne protozoan")],
  ci(40, 4, 39, 41, 16, 76),
  img="wr3-fig-07.jpg",
  alt="Stained stool specimen: two oval, thick-walled bodies with purple internal structures, lying among pink and "
      "blue debris"),

# ---------------------------------------------------------------- 2.5 (cold) Trichomonas vaginalis — PICTURE
Q("2.5", "cold", "A", "Trichomonas vaginalis: transmission (picture)", IO2,
  "A vaginal smear shows the flagellates pictured. How is this organism transmitted?",
  ("By sexual contact",
   "Correct: these pear-shaped cells with anterior flagella and an undulating membrane are Trichomonas vaginalis, "
   "which causes trichomoniasis, a sexually transmitted disease. Its reservoir is the human urogenital tract; it "
   "exists only as a trophozoite with no cyst and cannot survive long outside the host."),
  [("By swallowing cysts in water",
    "Swallowed cysts in water spread Giardia lamblia, an intestinal flagellate found in stool. Trichomonas has no cyst "
    "form and cannot survive long outside its host, so it passes by sexual contact from the urogenital tract.",
    "assumes every flagellate spreads by cysts in water"),
   ("By the bite of a fly",
    "A fly bite spreads the blood flagellate Trypanosoma brucei, seen swimming between cells on a blood smear. "
    "Flagellates in a vaginal smear are Trichomonas vaginalis, which lives in the urogenital tract and spreads by "
    "sexual contact.",
    "confuses the genital flagellate with a blood flagellate"),
   ("By water entering the nose",
    "Water entering the nose transmits Naegleria fowleri, an ameba that travels to the brain. The pear-shaped "
    "flagellates in a vaginal smear are Trichomonas vaginalis, a strict parasite of the urogenital tract spread by "
    "sexual contact.",
    "picks a free-living organism's route")],
  ci(38, 4, 36, 37, 39, 45, 28),
  img="wr3-fig-05.jpg",
  alt="Stained smear on a pale green background: two pear-shaped cells, each with a dark nucleus, a wavy membrane "
      "along one side and thin whip-like strands"),

# ---------------------------------------------------------------- 2.6 (it) Trypanosoma brucei gambiense
Q("2.6", "it", "A", "African sleeping sickness: late course", IO1,
  "A patient with African sleeping sickness from Trypanosoma brucei gambiense goes untreated, and personality and "
  "behavioral changes appear as the organism reaches the nervous system. How does the disease then progress?",
  ("Sleep disturbance, then coma",
   "Correct: once Trypanosoma brucei moves to the nervous system, personality and behavioral changes progress to "
   "sleep disturbances, tremors, seizures, paralysis and coma. The Gambian form is chronic, with brain symptoms "
   "years after the tsetse fly bite."),
  [("Elephantiasis of the limbs",
    "Elephantiasis follows chronic Wuchereria bancrofti infection, whose worms block lymphatic circulation and cause "
    "massive swelling of the extremities. Trypanosoma brucei damages the spleen, lymph nodes and brain, ending in "
    "sleep disturbances and coma.",
    "confuses a tropical worm disease with the trypanosome"),
   ("Chronic heart inflammation",
    "Chronic inflammation of the heart is the hallmark of Chagas disease, from Trypanosoma cruzi, whose amastigotes "
    "mass in heart muscle. Its African cousin, Trypanosoma brucei, attacks the brain and progresses to sleep "
    "disturbances, seizures and coma.",
    "swaps the two trypanosomes"),
   ("Watery diarrhea and bloating",
    "Watery diarrhea, stomach cramps and bloating describe cyclosporiasis, an intestinal infection from fresh produce "
    "and water. Trypanosoma brucei is a blood flagellate that reaches the nervous system and leads to sleep "
    "disturbances and coma.",
    "assigns an intestinal course to a blood parasite")],
  c(45, 46, 47, 104, 49, 75)),

# ---------------------------------------------------------------- 2.7 (cold) Trypanosoma cruzi
Q("2.7", "cold", "A", "Chagas disease: how the bug transmits it", IO2,
  "Chagas disease is spread by the reduviid (kissing) bug. How does Trypanosoma cruzi enter the person during an "
  "encounter with the bug?",
  ("Its feces inoculated into the skin",
   "Correct: infection occurs when the bug's feces are inoculated into a cutaneous portal such as the bite. A local "
   "lesion can follow, such as Romana's sign, a swelling of the eyelid with conjunctivitis, then fever and swelling "
   "of the lymph nodes, spleen and liver."),
  [("Its saliva injected with the bite",
    "Organisms in vector saliva describe malaria: the female Anopheles mosquito injects sporozoites as it feeds, and "
    "the tsetse fly's bite inoculates Trypanosoma brucei. The kissing bug spreads Trypanosoma cruzi in its feces, "
    "which are inoculated into the skin.",
    "assumes every insect vector infects through its bite"),
   ("Larvae burrowing into bare feet",
    "Larvae burrowing into the skin of bare feet is how hookworms such as Necator americanus enter, from soil "
    "contaminated with feces. Trypanosoma cruzi is a protozoan with no larvae; it enters when kissing-bug feces are "
    "inoculated into a break in the skin.",
    "borrows a worm's skin-penetration route"),
   ("Water forced up into the nose",
    "Water forced up the nose transmits Naegleria fowleri, a free-living ameba of warm fresh water. Trypanosoma cruzi "
    "has an insect vector, the reduviid bug, and enters when the bug's feces are inoculated into the skin.",
    "picks a free-living ameba's route")],
  c(49, 5, 46, 58, 96, 28)),

# ---------------------------------------------------------------- 2.8 (it) Leishmania: vector
Q("2.8", "it", "A", "Leishmania: the vector", IO2,
  "Leishmaniasis is a zoonosis of equatorial regions. Which insect transmits Leishmania among its mammal hosts?",
  ("The female sand fly",
   "Correct: female sand flies, which need a blood meal to produce eggs, transmit leishmaniasis among mammalian "
   "hosts, with dogs as alternate hosts. Promastigotes are injected with the bite and convert to amastigotes, giving "
   "cutaneous sores, espundia or the systemic form, kala azar."),
  [("The tsetse fly",
    "The tsetse fly spreads Trypanosoma brucei, the cause of African sleeping sickness. Leishmania is a different "
    "hemoflagellate, carried among mammals in equatorial regions by the female sand fly.",
    "swaps the vectors of two hemoflagellates"),
   ("The kissing bug",
    "The reduviid, or kissing, bug is the vector of Trypanosoma cruzi and Chagas disease, spreading it in its feces. "
    "Leishmania promastigotes are injected with the bite of a female sand fly.",
    "swaps the vectors of two hemoflagellates"),
   ("The Anopheles mosquito",
    "The female Anopheles mosquito is the primary vector of Plasmodium, the agent of malaria. Leishmaniasis, with "
    "the dog as an alternate host, is transmitted by the female sand fly.",
    "names the best-known insect vector")],
  c(52, 5, 45, 49, 56)),

# ---------------------------------------------------------------- 2.9 (cold) Plasmodium, x2 — PICTURE (rings)
Q("2.9", "cold", "A", "Plasmodium: vector (picture)", IO2,
  "The forms seen inside these red blood cells cause a disease with regular episodes of chills, fever and sweating. "
  "Which vector transmits the organism?",
  ("Anopheles mosquito",
   "Correct: ring forms inside red blood cells are Plasmodium trophozoites, the agent of malaria. The female "
   "Anopheles mosquito is the primary vector, injecting sporozoites that settle in the liver before merozoites invade "
   "red cells; chills and fever recur as the red cells rupture."),
  [("Blacklegged deer tick",
    "The blacklegged deer tick carries Babesia microti, which also attacks red blood cells but causes flu-like "
    "symptoms and hemolytic anemia. Ring forms inside red cells with regular chills-fever-sweating episodes are "
    "Plasmodium, spread by the Anopheles mosquito.",
    "picks the other red-cell parasite's vector"),
   ("Female sand fly",
    "The female sand fly transmits Leishmania, whose promastigotes become amastigotes and multiply, causing sores or "
    "kala azar. Ring-shaped trophozoites inside red blood cells are Plasmodium, carried by the Anopheles mosquito.",
    "picks another hemoparasite's vector"),
   ("Tsetse fly",
    "The tsetse fly spreads Trypanosoma brucei, a flagellate that swims between blood cells rather than living inside "
    "them. Small rings within red blood cells mark Plasmodium, carried by the female Anopheles mosquito.",
    "confuses forms inside red cells with flagellates between them")],
  ci(60, 5, 56, 58, 77, 45, 52),
  img="wr3-fig-09.jpg",
  alt="Stained blood smear: closely packed pale red blood cells, many holding a small purple loop-shaped form; "
      "unlabeled pointer lines at the right edge"),

Q("2.9", "cold", "A", "Plasmodium: liver, then red cells", IO1,
  "After Plasmodium multiplies in the liver, merozoites enter the circulation. Which cells do they invade next?",
  ("Red blood cells",
   "Correct: merozoites from the liver attach to and enter red blood cells, convert to circular ring trophozoites and "
   "multiply; the red cell then bursts, releasing more merozoites. These bursts, at intervals set by the species, "
   "bring the chills, fever and sweating of malaria."),
  [("Macrophages",
    "Macrophages hold Leishmania, whose promastigotes convert to amastigotes and multiply; the infection spreads "
    "systemically if the macrophage migrates. Plasmodium merozoites leave the liver and invade red blood cells.",
    "borrows Leishmania's host cell"),
   ("Intestinal cells",
    "Intestinal cells are penetrated by Cryptosporidium sporozoites after oocysts are swallowed, causing "
    "gastroenteritis. Plasmodium is injected by a mosquito, multiplies in the liver, and its merozoites then enter red "
    "blood cells.",
    "borrows a coccidian's target cell"),
   ("Heart muscle cells",
    "Masses of amastigotes in heart muscle belong to Trypanosoma cruzi and chronic Chagas disease. Plasmodium "
    "merozoites, released from the liver, attach to and enter red blood cells, where they become ring trophozoites.",
    "borrows Trypanosoma cruzi's target")],
  c(58, 59, 60, 52, 73, 49)),

# ---------------------------------------------------------------- 2.10 (cold) Toxoplasma gondii: cats
Q("2.10", "cold", "A", "Toxoplasma gondii: its natural host", IO2,
  "Toxoplasma gondii can infect virtually all warm-blooded animals. In which animal does it live naturally, "
  "shedding oocysts in its feces?",
  ("The cat",
   "Correct: Toxoplasma gondii lives naturally in cats, which harbor oocysts in the gastrointestinal tract and release "
   "them in feces. People acquire it by ingesting raw meats or substances contaminated by cat feces."),
  [("The dog",
    "Dogs are the definitive host of Echinococcus and an alternate host of Leishmania, not the source of Toxoplasma. "
    "Toxoplasma's oocysts come from cats, which harbor them in the gastrointestinal tract and shed them in feces.",
    "picks the other household pet"),
   ("The pig",
    "Pigs carry Trichinella spiralis and the pork tapeworm, Taenia solium, in their meat. Toxoplasma can sit in food "
    "animals' muscle, but it lives naturally in cats, which shed its oocysts in feces.",
    "confuses a meat source with the natural host"),
   ("The snail",
    "Snails are the intermediate host of Schistosoma and of the other flukes. "
    "Toxoplasma gondii has no snail stage; it lives naturally in cats, which release its oocysts through feces.",
    "borrows the flukes' intermediate host")],
  c(64, 66, 5, 124, 52, 101, 121, 112)),

# ---------------------------------------------------------------- 2.11 (cold) Cyclospora — PICTURE
Q("2.11", "cold", "A", "Cyclospora: source (picture)", IO2,
  "An acid-fast stained fecal smear from a patient with watery diarrhea shows the round, red-staining bodies "
  "pictured. How is this parasite usually acquired?",
  ("Contaminated produce or water",
   "Correct: red-staining bodies on an acid-fast fecal smear are Cyclospora cayetanensis oocysts. Cyclospora spreads "
   "by the oral-fecal route in fresh produce and water, as in the widespread outbreak linked to iceberg lettuce; its "
   "oocysts invade the small intestine and cause watery diarrhea."),
  [("Undercooked pork or bear meat",
    "Undercooked pork or bear meat transmits Trichinella spiralis, whose larvae encyst in muscle. Acid-fast "
    "red-staining oocysts in feces with watery diarrhea are Cyclospora, which comes from fresh produce and water.",
    "picks a meat-borne worm's source"),
   ("Sexual contact with a carrier",
    "Sexual contact spreads Trichomonas vaginalis, diagnosed in a vaginal smear rather than in feces. Cyclospora "
    "oocysts in a fecal smear come by the oral-fecal route from contaminated fresh produce and water.",
    "picks a sexually transmitted protozoan's route"),
   ("The bite of a mosquito",
    "A mosquito bite transmits Plasmodium, diagnosed by ring trophozoites in red cells, not oocysts in feces. "
    "Cyclospora is an intestinal parasite acquired by the oral-fecal route from fresh produce and water.",
    "assumes an apicomplexan needs a vector")],
  ci(76, 75, 13, 101, 37, 38, 56, 60),
  img="wr3-fig-10.jpg",
  alt="Stained fecal smear: round bodies stained bright pink to red against a blue background, with a 20 micrometer "
      "scale bar and unlabeled pointer lines"),

# ---------------------------------------------------------------- 2.12 (cold) what worms do, x2
Q("2.12", "cold", "A", "Worm damage: blockage", IO1,
  "A child with a heavy Ascaris lumbricoides load develops abdominal pain and intestinal obstruction. Which mechanism "
  "of worm pathology explains the obstruction?",
  ("Masses of worms blocking the bowel",
   "Correct: one way helminths cause disease is the accumulation of worms in organs, causing blockages. Ascaris "
   "worms keep their motility and do not attach, and heavy worm loads cause abdominal pain and intestinal "
   "obstruction."),
  [("Toxic secretions from the worms",
    "Toxic worm secretions are a real source of helminth pathology, but they do not plug the bowel. An obstruction "
    "under a heavy Ascaris load comes from the accumulation of worms in the intestine, causing a blockage.",
    "names a real mechanism that does not fit this finding"),
   ("Blood loss at attachment sites",
    "Significant blood loss and anemia come from hookworms, which hook into the small intestine. Ascaris worms do not "
    "attach; under a heavy load the mass of worms blocks the intestine.",
    "borrows the hookworm's damage"),
   ("Larvae encysting in muscle",
    "Larvae encysting in muscle, heart and brain describe Trichinella spiralis after undercooked pork. Intestinal "
    "obstruction in a heavy Ascaris infection comes from worms accumulating in the bowel.",
    "borrows Trichinella's damage")],
  c(85, 92, 96, 101)),

Q("2.12", "cold", "A", "Tapeworms: how they obtain food", IO1,
  "An adult beef tapeworm lives attached in a person's small intestine. How does it obtain its food?",
  ("Absorption through its body",
   "Correct: a tapeworm has no mouth, so nutrients are absorbed through its body; its scolex grips the intestine and "
   "each proglottid is an independent unit adapted to absorbing food. In the beef tapeworm, the larva attaches to "
   "the small intestine and becomes an adult."),
  [("Ingesting food through its mouth",
    "A tapeworm has no mouth at all; nutrients are absorbed through its body, and each proglottid is adapted to "
    "absorbing food. Specialized mouthparts for attachment are an adaptation of other helminths.",
    "assumes every worm eats through a mouth"),
   ("Feeding on the host's blood",
    "Feeding on blood is what adult Schistosoma flukes do after they migrate to the intestine or bladder. The beef "
    "tapeworm has no mouth and absorbs nutrients through its body.",
    "borrows the blood flukes' feeding"),
   ("Biting with its hooked mouth",
    "Curved ends and hooked mouths mark the hookworms, whose infection brings significant blood loss and anemia. A "
    "tapeworm has no mouth; it absorbs nutrients through its body.",
    "borrows the hookworms' mouthparts")],
  c(118, 119, 85, 96, 112)),

# ---------------------------------------------------------------- 2.13 (cold) Enterobius vermicularis
Q("2.13", "cold", "A", "Pinworm: the daycare child", IO1,
  "A child at a daycare center has anal itching that is worst at night, and other children there soon have it too. "
  "Which worm is the most likely cause?",
  ("Enterobius vermicularis",
   "Correct: Enterobius vermicularis, the pinworm, is very common in daycare and spreads by direct contact and "
   "fomites. Anal itching occurs when mature females emerge from the intestine at night to lay eggs on the perianal "
   "folds, and self-inoculation is common; the tape test diagnoses it."),
  [("Trichuris trichiura",
    "Trichuris trichiura, the whipworm, attaches in the intestine and can pierce capillaries; heavy infestations "
    "cause dysentery and rectal prolapse. Night-time anal itching spreading through a daycare points to the pinworm.",
    "picks another intestinal worm of children"),
   ("Ascaris lumbricoides",
    "Ascaris lumbricoides is a large roundworm whose heavy loads cause abdominal pain and intestinal obstruction. "
    "Anal itching as females emerge to lay eggs, passing child to child in daycare, is Enterobius vermicularis.",
    "picks the best-known roundworm"),
   ("Strongyloides stercoralis",
    "Strongyloides stercoralis larvae penetrate the skin and migrate to the lungs, and the worm can reinfect the same "
    "host. Night-time anal itching spreading in daycare is the pinworm, Enterobius vermicularis.",
    "confuses autoinfection with the pinworm's self-inoculation")],
  c(6, 94, 95, 93, 92, 100)),

# ---------------------------------------------------------------- 2.14 (cold) Trichinella spiralis
Q("2.14", "cold", "A", "Trichinella spiralis: where larvae encyst", IO1,
  "After a person eats undercooked pork, Trichinella spiralis larvae migrate from the intestine into blood vessels. "
  "Where do they form cysts?",
  ("Muscle, heart, brain",
   "Correct: Trichinella larvae migrate from the intestine to blood vessels, muscle, heart and brain, where they form "
   "cysts. Muscle and joint pain with pronounced eosinophilia follow, and myocarditis or central nervous system "
   "involvement can be life-threatening."),
  [("The liver and lungs",
    "Slowly enlarging cysts in the liver and lungs are cystic echinococcosis, or hydatid disease, from Echinococcus. "
    "Trichinella larvae from undercooked pork encyst in muscle, heart and brain.",
    "confuses Trichinella with the hydatid tapeworm"),
   ("Inside the bile ducts",
    "The bile ducts are where Opisthorchis sinensis larvae mature after inadequately cooked fish. Trichinella larvae "
    "from undercooked pork leave the intestine and encyst in muscle, heart and brain.",
    "borrows the Chinese liver fluke's site"),
   ("The lymphatic vessels",
    "The lymphatics are home to Wuchereria bancrofti, whose blockage of lymphatic circulation causes elephantiasis. "
    "Trichinella larvae from undercooked pork encyst in muscle, heart and brain instead.",
    "borrows a filarial worm's site")],
  c(101, 102, 7, 124, 116, 104)),

# ---------------------------------------------------------------- 2.15 (it) Loa loa — PICTURE
Q("2.15", "it", "A", "Loa loa: the eye worm (picture)", IO1,
  "The worm pictured is being drawn out of the eye of a patient from Africa through a small opening in the "
  "conjunctiva. Which worm is it?",
  ("Loa loa",
   "Correct: Loa loa, the African eye worm, is spread by the bite of small flies. This temperature-sensitive worm "
   "migrates around and under the skin and may enter the eye, where it can be pulled out through a small hole in the "
   "conjunctiva."),
  [("Wuchereria bancrofti",
    "Wuchereria bancrofti is a mosquito-borne filarial worm that lives in the lymphatics and causes elephantiasis, "
    "massive swelling of the extremities. The worm crossing the eye under the conjunctiva is Loa loa.",
    "picks another filarial worm"),
   ("Angiostrongylus cantonensis",
    "Angiostrongylus cantonensis, the rat lungworm, comes from snails and causes eosinophilic meningitis, with "
    "eosinophils in the spinal fluid. A worm moving under the conjunctiva of the eye is Loa loa, the eye worm.",
    "picks a worm of the nervous system"),
   ("Trichinella spiralis",
    "Trichinella spiralis larvae from undercooked pork encyst in muscle, heart and brain as small coiled forms. A "
    "single long worm drawn from the eye is Loa loa, which migrates under the skin and may enter the eye.",
    "picks a tissue-invading worm")],
  ci(107, 8, 103, 104, 98, 99, 101),
  img="wr3-fig-13.jpg",
  alt="Close-up of an eye held open with a metal instrument: a thin white coiled worm lies on the reddened surface of "
      "the eye"),

# ---------------------------------------------------------------- 2.16 (it) Schistosoma
Q("2.16", "it", "A", "Schistosoma: how it is acquired", IO2,
  "Schistosoma is a blood fluke whose early larva develops in a freshwater snail. How do people acquire "
  "schistosomiasis?",
  ("Larvae penetrating skin in water",
   "Correct: eggs released into water hatch an early larva that develops in a freshwater snail into a second larva, "
   "the cercaria, which penetrates human skin. People acquire it by contact with water in which the snail lives, "
   "with itchiness at the entry site; snail control prevents it."),
  [("Eating inadequately cooked fish",
    "Inadequately cooked fish carrying cercariae transmits the Chinese liver fluke, Opisthorchis sinensis. "
    "Schistosoma cercariae leave the snail and penetrate the skin of people in contact with the water.",
    "swaps in another fluke's food source"),
   ("Eating raw aquatic plants",
    "Raw aquatic plants transmit the liver fluke Fasciola hepatica, which cycles between herbivores, snails and "
    "plants. Schistosoma reaches people through the skin, as cercariae from snails penetrate it in water.",
    "swaps in another fluke's food source"),
   ("Eating undercooked crustaceans",
    "Undercooked crustaceans transmit the lung fluke Paragonimus westermani. Schistosomiasis is not eaten: the "
    "cercaria released by the freshwater snail penetrates human skin during contact with the water.",
    "swaps in another fluke's food source")],
  c(112, 113, 8, 116, 117)),

# ---------------------------------------------------------------- 2.17 (it) Taenia solium cysticercosis — PICTURE
Q("2.17", "it", "A", "Cysticercosis: how it is acquired (picture)", IO2,
  "The brain slice pictured is filled with cysts formed by tapeworm larvae. How did this person acquire the "
  "infection?",
  ("Swallowing pork tapeworm eggs",
   "Correct: these brain cysts are cysticercosis from Taenia solium, the pork tapeworm, which follows ingestion of "
   "embryonated eggs. The eggs hatch in the intestine and release larvae that migrate to all tissues and encyst, "
   "most damaging in heart muscle, eye or brain, with seizures."),
  [("Eating cysts in undercooked pork",
    "Eating cysts in undercooked pork gives taeniasis: the cysts release larvae that become tapeworms attached to the "
    "intestine. Cysticercosis in the brain comes from swallowing Taenia solium's embryonated eggs instead.",
    "confuses the meat route (taeniasis) with the egg route (cysticercosis)"),
   ("Eating cysts in undercooked beef",
    "Raw beef with encysted larvae gives Taenia saginata, the beef tapeworm, which becomes an adult in the small "
    "intestine with few symptoms. Brain cysts are cysticercosis, from swallowing pork tapeworm eggs.",
    "swaps the beef and pork tapeworms"),
   ("Eating snails or raw vegetables",
    "Snails, contaminated water or vegetables transmit Angiostrongylus cantonensis, which causes eosinophilic "
    "meningitis rather than brain cysts. Cysts filling the brain are cysticercosis, from Taenia solium eggs.",
    "picks the other parasite of the nervous system")],
  ci(123, 8, 121, 119, 98, 99),
  img="wr3-fig-14.jpg",
  alt="Cut slice of a brain on a blue background: several small round dark cavities clustered in one region, with a "
      "dark patch above them"),

# ---------------------------------------------------------------- 2.18 (cold) why few antiparasitic drugs
Q("2.18", "cold", "A", "Antiprotozoan drugs: why few and toxic", IO1,
  "Antiprotozoan drugs are relatively few compared with antibacterial agents and often bring severe side effects. "
  "Which feature of protozoa underlies this?",
  ("They are eukaryotic cells",
   "Correct: protozoa are eukaryotic parasites, like the cells of their human host, and antiprotozoan drugs must work "
   "against eukaryotic cells. That is why they are relatively few in comparison with antibacterial agents and carry "
   "toxicity problems and severe side effects."),
  [("They are prokaryotic cells",
    "Prokaryotic cells are bacteria, the targets of the many antibacterial agents. Parasitology is the study of "
    "eukaryotic parasites, and drugs against eukaryotic cells are few and toxic because the host's cells are "
    "eukaryotic too.",
    "reverses the cell type"),
   ("Many form dormant cysts",
    "Many protozoa do form cysts, but that is a life-cycle feature, not why the drugs are few and toxic. The drugs "
    "must work against eukaryotic cells, like the host's own, which causes toxicity problems and severe side "
    "effects.",
    "names a true feature that is not the reason"),
   ("Most are spread by vectors",
    "Vectors spread the hemoflagellates and Plasmodium, but amebas, Giardia and the coccidians come in water and "
    "food. Drug scarcity and toxicity come from protozoa being eukaryotic, like the cells of the host.",
    "overgeneralizes the vector-borne protozoa")],
  c(14, 9, 12, 42, 55, 39, 72)),

# =============================================================================================== FORM B
# ---------------------------------------------------------------- 2.1 (cold) Entamoeba histolytica: the cyst
Q("2.1", "cold", "B", "Entamoeba histolytica: the swallowed cyst", IO2,
  "Entamoeba histolytica is ingested, and in the small intestine alkaline pH and digestive juices stimulate each "
  "swallowed form to release four trophozoites. Which form is swallowed?",
  ("The cyst",
   "Correct: cysts are swallowed and arrive at the small intestine, where alkaline pH and digestive juices stimulate "
   "each one to release four trophozoites. The cyst is the smaller, nonmotile form, produced after the active phase "
   "of disease and spread by the fecal-oral route."),
  [("The trophozoite",
    "The trophozoite is the product, not the swallowed form: it is released from the cyst, then attaches, moves by "
    "pseudopods and feeds. The form that is ingested and triggered to release four trophozoites is the cyst.",
    "reverses the order of the two forms"),
   ("The sporozoite",
    "Sporozoites are apicomplexan forms: Plasmodium sporozoites are injected by the mosquito, and Cryptosporidium "
    "oocysts give rise to sporozoites. Entamoeba histolytica has only a cyst and a trophozoite, and the cyst is "
    "swallowed.",
    "borrows an apicomplexan stage name"),
   ("The egg",
    "Eggs belong to helminths, whose adults mate and produce fertilized eggs that hatch into larvae. Entamoeba "
    "histolytica is a single-celled protozoan; the swallowed form that releases trophozoites is the cyst.",
    "confuses a protozoan with a worm")],
  c(16, 19, 23, 4, 58, 73, 79)),

# ---------------------------------------------------------------- 2.2 (cold) Naegleria — PICTURE; Acanthamoeba
Q("2.2", "cold", "B", "Naegleria fowleri: disease (picture)", IO1,
  ("Amebas like those pictured are found in a teenager who, days after waterskiing on a freshwater lake, has "
   "headache, fever, vomiting and a stiff neck and rapidly slips into a coma. Which disease is this?"),
  ("Primary acute meningoencephalitis",
   "Correct: this is Naegleria fowleri, acquired through nasal contact with water while diving or waterskiing. The "
   "trophozoite burrows through the nasal mucosa and travels along the olfactory nerve, causing primary acute "
   "meningoencephalitis with rapid destruction of the brain and coma or death in 3 to 7 days."),
  [("Granulomatous amoebic encephalitis",
    "Granulomatous amoebic encephalitis is caused by Acanthamoeba, which typically enters through a break in the skin "
    "or the nasal passages, with meningitis symptoms but a longer progression. A coma within days of waterskiing fits "
    "Naegleria fowleri and primary acute meningoencephalitis.",
    "confuses the two free-living amebas"),
   ("Amebic dysentery",
    "Amebic dysentery is caused by Entamoeba histolytica, swallowed as cysts by the fecal-oral route, invading the "
    "colon. Water forced into the nose while waterskiing carries Naegleria fowleri, which causes "
    "primary acute meningoencephalitis.",
    "picks the intestinal ameba's disease"),
   ("Amebic keratitis",
    "Amebic keratitis, with eye pain and redness in contact lens wearers, is caused by Acanthamoeba and does not "
    "typically disseminate. Naegleria fowleri travels from the nose to the brain and causes primary acute "
    "meningoencephalitis.",
    "picks Acanthamoeba's eye disease")],
  ci(28, 4, 24, 29, 31, 20),
  img="wr3-fig-04.jpg",
  alt="Stained preparation on a white background: five irregular, blue-staining single cells with blunt projections, "
      "each with one dark round nucleus"),

Q("2.2", "cold", "B", "Acanthamoeba encephalitis versus Naegleria", IO1,
  "A person develops symptoms of meningitis from Acanthamoeba, which entered through a break in the skin. How does "
  "this granulomatous amoebic encephalitis compare with Naegleria meningoencephalitis?",
  ("It has a longer progression",
   "Correct: Acanthamoeba granulomatous amoebic encephalitis produces symptoms of meningitis, but with a longer "
   "progression. Naegleria primary acute meningoencephalitis destroys the brain and spinal cord rapidly, with death "
   "within days, which is why its treatment must be early."),
  [("It progresses more rapidly",
    "Rapid progression is the mark of Naegleria fowleri, which destroys the brain and spinal cord with coma and death "
    "within days. Acanthamoeba's granulomatous amoebic encephalitis gives meningitis symptoms with a longer "
    "progression.",
    "reverses which ameba moves faster"),
   ("Most patients survive it",
    "Survival from Acanthamoeba granulomatous amoebic encephalitis is very rare, and its listed drugs are only "
    "tentatively successful. What sets it apart from Naegleria infection is a longer progression, not a better "
    "outcome.",
    "mistakes a slower course for a milder one"),
   ("It comes from swallowed cysts",
    "Swallowed cysts start Entamoeba histolytica infection in the intestine. Acanthamoeba typically enters through a "
    "break in the skin or the nasal passages, and its encephalitis has a longer progression than Naegleria's.",
    "borrows the intestinal ameba's route")],
  c(31, 29, 24, 16, 19)),

# ---------------------------------------------------------------- 2.4 (cold) Giardia lamblia — PICTURE (trophozoite)
Q("2.4", "cold", "B", "Giardia lamblia: trophozoite in stool (picture)", IO1,
  "A stool specimen from a patient with diarrhea and abdominal pain shows the symmetrical flagellate pictured. Which "
  "organism is it?",
  ("Giardia lamblia",
   "Correct: a symmetrical, heart-shaped flagellate in stool is the Giardia lamblia trophozoite, whose concave ventral "
   "surface acts like a suction cup. Its cysts, ingested with water and food, germinate in the duodenum, and the "
   "trophozoites feed and multiply in the jejunum, causing diarrhea and abdominal pain."),
  [("Trichomonas vaginalis",
    "Trichomonas vaginalis is a small, pear-shaped flagellate, but its reservoir is the urogenital tract and it "
    "is diagnosed in a vaginal smear. A symmetrical flagellate in stool with diarrhea is Giardia lamblia.",
    "confuses the two flagellates"),
   ("Trypanosoma cruzi",
    "Trypanosoma cruzi is a hemoflagellate spread by the kissing bug; its amastigotes mass in heart muscle and the "
    "large intestine. A symmetrical, heart-shaped flagellate swimming in a stool specimen is the Giardia lamblia "
    "trophozoite.",
    "picks a flagellate that lives in blood and tissue"),
   ("Entamoeba histolytica",
    "Entamoeba histolytica is an ameba that moves by pseudopods and has no flagella; it erodes the colon and causes "
    "dysentery. A heart-shaped flagellate in stool is Giardia lamblia.",
    "confuses an intestinal ameba with an intestinal flagellate")],
  ci(40, 39, 41, 4, 36, 38, 44, 49, 16),
  img="wr3-fig-06.jpg",
  alt="Stained stool smear: one symmetrical cell with a rounded front end and a tapered tail, among blue "
      "and purple debris"),

# ---------------------------------------------------------------- 2.5 (cold) Trichomonas vaginalis
Q("2.5", "cold", "B", "Trichomonas vaginalis: most common curable", IO1,
  "Which protozoan causes the most common curable sexually transmitted disease in young, sexually active women?",
  ("Trichomonas vaginalis",
   "Correct: Trichomonas vaginalis, a flagellate, causes trichomoniasis, the most common curable sexually transmitted "
   "disease in young, sexually active women. Its reservoir is the human urogenital tract, many infected people have "
   "no symptoms, and it is diagnosed by microscopic analysis of a vaginal smear."),
  [("Entamoeba histolytica",
    "Entamoeba histolytica is sometimes sexually transmitted, but it is an intestinal ameba spread mainly by the "
    "fecal-oral route, causing amebic dysentery. The most common curable sexually transmitted protozoan is "
    "Trichomonas vaginalis.",
    "overweights a minor route of the intestinal ameba"),
   ("Giardia lamblia",
    "Giardia lamblia is a flagellate, but it is ingested as cysts with water and food and causes giardiasis, with "
    "diarrhea and abdominal pain. The flagellate of the urogenital tract, spread sexually, is Trichomonas vaginalis.",
    "picks the wrong flagellate"),
   ("Toxoplasma gondii",
    "Toxoplasma gondii comes from cat feces and raw meat, and a pregnant woman can pass it across the placenta; it is "
    "not sexually transmitted. The common curable sexually transmitted protozoan is Trichomonas vaginalis.",
    "links a women's-health parasite to sexual spread")],
  c(37, 38, 4, 17, 39, 64, 65)),

# ---------------------------------------------------------------- 2.6 (it) Trypanosoma brucei — PICTURE
Q("2.6", "it", "B", "Trypanosoma brucei: blood smear (picture)", IO1,
  "A blood smear from a traveler returning from West Africa with fever, an enlarged spleen and swollen lymph nodes "
  "shows the forms pictured, swimming between the cells. Which disease is this?",
  ("African sleeping sickness",
   "Correct: elongate, spindle-shaped flagellates swimming between blood cells are Trypanosoma brucei, readily "
   "demonstrated in blood. Spread by tsetse flies, the Gambian strain is found in West Africa; early fever, an "
   "enlarged spleen and swollen lymph nodes give way to nervous system disease."),
  [("Falciparum malaria",
    "Malaria, including the falciparum type, is diagnosed by Plasmodium trophozoites inside red blood cells, seen as small ring forms. These "
    "organisms are long flagellates lying between the cells, the picture of Trypanosoma brucei and African sleeping "
    "sickness.",
    "confuses parasites between red cells with parasites inside them"),
   ("Chagas disease",
    "Chagas disease is also caused by a trypanosome, Trypanosoma cruzi, but it is endemic to Central and South "
    "America and spread by the kissing bug. A trypanosome in the blood after travel to West Africa is Trypanosoma "
    "brucei.",
    "swaps the two trypanosomes"),
   ("Visceral leishmaniasis",
    "Visceral leishmaniasis, or kala azar, with fever and an enlarged spleen, comes from Leishmania, whose promastigotes "
    "become amastigotes, the form lacking a free flagellum. Free-swimming flagellates in a West African traveler's "
    "blood are Trypanosoma brucei.",
    "picks the other hemoflagellate with fever and splenomegaly")],
  ci(46, 5, 44, 45, 47, 42, 48, 52, 53, 60),
  img="wr3-fig-08.jpg",
  alt="Stained blood smear: pale round red blood cells with several slender, wavy, purple-staining organisms lying "
      "between them"),

# ---------------------------------------------------------------- 2.7 (cold) Trypanosoma cruzi, x2
Q("2.7", "cold", "B", "Chagas disease: the heart", IO1,
  "A patient infected years earlier with Trypanosoma cruzi now has chronic organ inflammation. Which organ is "
  "especially affected, with masses of amastigotes in its muscle?",
  ("The heart",
   "Correct: in Chagas disease, heart muscle and the large intestine harbor masses of amastigotes, and chronic "
   "inflammation occurs especially in the heart and brain. It accounts for a large share of heart disease in endemic "
   "regions, and amastigotes in cardiac muscle are a marker condition."),
  [("The liver",
    "The liver is where Entamoeba histolytica most commonly forms abscesses and where Opisthorchis sinensis matures in "
    "the bile ducts. Trypanosoma cruzi's amastigotes mass in heart muscle, causing chronic cardiac inflammation.",
    "picks the classic parasitic abscess organ"),
   ("The lungs",
    "The lungs are the home of the lung fluke Paragonimus westermani, from undercooked crustaceans, with cough and "
    "pleural pain. Chronic Chagas disease inflames the heart, where masses of amastigotes lodge in the muscle.",
    "picks a fluke's organ"),
   ("The eye",
    "The eye is reached by Loa loa, the eye worm, and inflamed in river blindness; in Chagas disease the eye shows "
    "only the early local lesion, Romana's sign. The chronic damage of Trypanosoma cruzi falls on the heart.",
    "confuses the early eyelid lesion with the chronic organ damage")],
  c(49, 51, 48, 21, 116, 107, 106)),

Q("2.7", "cold", "B", "Chagas disease: the vector", IO2,
  "Trypanosoma cruzi, the cause of Chagas disease, is spreading in the southern United States as its vector expands "
  "its range. Which insect is the vector?",
  ("The reduviid (kissing) bug",
   "Correct: the reduviid, or kissing, bug is the vector of Trypanosoma cruzi; infection occurs when the bug's feces "
   "are inoculated into a cutaneous portal. Once a tropical disorder of Latin America, Chagas disease is becoming an "
   "issue in the southern United States as the vector migrates."),
  [("The tsetse fly",
    "The tsetse fly spreads Trypanosoma brucei, the African trypanosome that causes African sleeping sickness. The "
    "American trypanosome, Trypanosoma cruzi, is carried by the reduviid, or kissing, bug.",
    "swaps the two trypanosomes' vectors"),
   ("The female sand fly",
    "The female sand fly transmits Leishmania, with dogs as alternate hosts, in equatorial regions. Trypanosoma cruzi "
    "is carried by the reduviid bug, whose range is expanding into the southern United States.",
    "picks another hemoflagellate's vector"),
   ("The Anopheles mosquito",
    "The female Anopheles mosquito is the primary vector of Plasmodium and malaria. Chagas disease spreads through the "
    "reduviid, or kissing, bug, which inoculates Trypanosoma cruzi in its feces.",
    "names the best-known insect vector")],
  c(49, 5, 48, 45, 52, 56)),

# ---------------------------------------------------------------- 2.8 (it) Leishmania: the dog
Q("2.8", "it", "B", "Leishmania: alternate host", IO2,
  "Leishmaniasis is transmitted among mammal hosts by sand flies in equatorial regions. Which animal serves as an "
  "alternate host?",
  ("The dog",
   "Correct: leishmaniasis is a zoonosis endemic to equatorial regions with dogs as alternate hosts; female sand "
   "flies carry it among mammals. Promastigotes injected with the bite convert to amastigotes, giving cutaneous "
   "sores, espundia or kala azar."),
  [("The cat",
    "The cat is the natural host of Toxoplasma gondii, shedding its oocysts in feces. Leishmania is carried by sand "
    "flies among mammals, with the dog as its alternate host.",
    "picks the other household pet"),
   ("The pig",
    "Pigs carry Trichinella spiralis and Taenia solium in undercooked pork. Leishmania is a sand fly-borne zoonosis of "
    "equatorial regions whose alternate host is the dog.",
    "picks a meat animal"),
   ("The snail",
    "Snails are the intermediate host of Schistosoma and of the other flukes. "
    "Leishmania has no snail stage: sand flies carry it, and dogs are its alternate hosts.",
    "borrows the flukes' intermediate host")],
  c(52, 5, 64, 101, 121, 112)),

# ---------------------------------------------------------------- 2.9 (cold) Plasmodium: diagnosis
Q("2.9", "cold", "B", "Malaria: the diagnostic smear", IO1,
  "A traveler has regular episodes of chills, fever and sweating after mosquito bites abroad. Which blood smear "
  "finding confirms malaria?",
  ("Ring trophozoites in red cells",
   "Correct: malaria is diagnosed by the presence of trophozoites in red blood cells, together with symptoms. "
   "Merozoites enter red cells and convert to circular ring trophozoites; the chills and fever recur at intervals as "
   "the red cells rupture."),
  [("Flagellates between red cells",
    "Flagellates swimming between the cells on a blood smear are Trypanosoma brucei, the cause of African sleeping "
    "sickness, spread by tsetse flies. Malaria shows small ring trophozoites inside the red blood cells.",
    "confuses Plasmodium with the blood trypanosome"),
   ("Amastigotes in macrophages",
    "Amastigotes multiplying in macrophages belong to Leishmania, carried by the sand fly. Malaria is confirmed by "
    "Plasmodium ring trophozoites within red blood cells.",
    "confuses Plasmodium with Leishmania"),
   ("Oocysts in a stool smear",
    "Oocysts in a fecal smear with an acid-fast stain identify intestinal coccidians such as Cyclospora. Plasmodium "
    "is diagnosed in the blood, by ring trophozoites inside red blood cells.",
    "confuses Plasmodium with the intestinal apicomplexans")],
  c(60, 58, 5, 46, 47, 52, 76)),

# ---------------------------------------------------------------- 2.10 (cold) Toxoplasma: placenta
Q("2.10", "cold", "B", "Toxoplasma gondii: reaching the fetus", IO2,
  "Toxoplasmosis in a pregnant woman can lead to spontaneous abortion or stillbirth. How does the parasite reach the "
  "fetus?",
  ("By crossing the placenta",
   "Correct: a pregnant woman with toxoplasmosis can pass Toxoplasma gondii to the fetus by transplacental "
   "transmission, causing spontaneous abortion, stillbirth or severe neurological and ocular problems in the newborn. "
   "This is why pregnant women should not clean the cat box."),
  [("Through cat feces at birth",
    "Cat feces are how the mother herself acquires Toxoplasma, by ingesting substances they contaminate. The fetus is "
    "infected before birth, when the parasite crosses the placenta from the infected mother.",
    "confuses the mother's source with the fetus's route"),
   ("Through raw meat she eats",
    "Raw meat is a source of the mother's own infection, not the route to the fetus. Once she has toxoplasmosis, "
    "Toxoplasma gondii reaches the fetus by transplacental transmission.",
    "confuses the mother's source with the fetus's route"),
   ("Through a mosquito bite",
    "A mosquito bite transmits Plasmodium; Toxoplasma has no insect vector, passing from cats through feces and raw "
    "meat. From an infected pregnant woman it reaches the fetus by crossing the placenta.",
    "assigns a vector to Toxoplasma")],
  c(65, 5, 64, 66, 56)),

# ---------------------------------------------------------------- 2.11 (cold) Cryptosporidium
Q("2.11", "cold", "B", "Cryptosporidium: how it is acquired", IO2,
  "By which route do people most often acquire Cryptosporidium, an intestinal pathogen whose oocysts are shed in "
  "feces?",
  ("Swallowing contaminated water",
   "Correct: Cryptosporidium infection frequently comes from consuming water in recreational settings or contaminated "
   "water, ice and foodstuffs; it tolerates chlorine in swimming pools. A 1990s Milwaukee outbreak came from "
   "contaminated water, and it is the leading cause of recreational waterborne disease."),
  [("The bite of an infected tick",
    "A tick bite transmits Babesia microti, carried by the blacklegged deer tick, which attacks red blood cells. "
    "Cryptosporidium has no vector: its oocysts are swallowed in contaminated water, ice or food.",
    "assigns a vector to an intestinal apicomplexan"),
   ("Sexual contact with a carrier",
    "Sexual contact is the route of Trichomonas vaginalis, a flagellate of the urogenital tract. Cryptosporidium is an "
    "intestinal pathogen acquired mostly by swallowing contaminated water, including recreational water.",
    "picks a sexually transmitted protozoan's route"),
   ("Eating raw freshwater fish",
    "Raw or inadequately cooked freshwater fish transmits the Chinese liver fluke, Opisthorchis sinensis. "
    "Cryptosporidium oocysts are swallowed most often in contaminated water, often in recreational settings.",
    "picks a fluke's food source")],
  c(72, 73, 6, 77, 37, 116)),

# ---------------------------------------------------------------- 2.12 (cold) worm damage: migration
Q("2.12", "cold", "B", "Worm damage: migration through tissues", IO1,
  "Ascaris lumbricoides larvae burrow through the intestine into the circulation and travel to the lungs, and severe "
  "inflammatory reactions, sometimes with eosinophilic pneumonitis, mark their route. Which mechanism of worm "
  "pathology is this?",
  ("Migration through tissues",
   "Correct: helminth pathology arises from worms feeding on and migrating through tissues. Ascaris larvae burrow "
   "through the intestine into the circulation, reach the lungs and pharynx and are swallowed; severe inflammatory "
   "reactions mark the migratory route, and lung migration can cause eosinophilic pneumonitis."),
  [("Blockage by masses of worms",
    "Blockage by accumulated worms is real pathology, and heavy Ascaris loads can obstruct the intestine. Damage along "
    "the larvae's route from the intestine to the lungs, though, comes from migration through tissues.",
    "names Ascaris's other mechanism, not this one"),
   ("Toxic worm secretions",
    "Toxic worm secretions are a separate source of helminth pathology. Inflammation tracing the path of Ascaris "
    "larvae through the circulation to the lungs is damage from worms migrating through tissues.",
    "names a real mechanism that does not fit this finding"),
   ("Absorbing host nutrients",
    "Absorbing the host's nutrients through the body is the tapeworm's way, since it has no mouth. Ascaris larvae "
    "harm the lungs by migrating through tissues, leaving inflammation along their route.",
    "borrows the tapeworm's damage")],
  c(85, 91, 92, 118, 8)),

# ---------------------------------------------------------------- 2.13 (cold) Enterobius — PICTURE (eggs)
Q("2.13", "cold", "B", "Pinworm: the tape test (picture)", IO1,
  "Eggs like those pictured come from a worm that commonly spreads among children in daycare. Which test collects "
  "them for diagnosis?",
  ("The tape test",
   "Correct: these oval eggs, flattened on one side, belong to Enterobius vermicularis, the pinworm. Mature females "
   "emerge from the intestine to lay eggs on the perianal folds, causing anal itching, so the tape test, or Scotch "
   "tape test, collects them there."),
  [("A thin blood smear",
    "A blood smear shows blood parasites such as Plasmodium in red cells or Trypanosoma brucei between them. Pinworm "
    "eggs are laid on the perianal folds, so they are collected with the tape test.",
    "picks the blood parasites' test"),
   ("An acid-fast stool smear",
    "An acid-fast stain of a fecal smear identifies Cyclospora oocysts. Pinworm females lay their eggs outside the "
    "intestine on the perianal folds, where the tape test picks them up.",
    "picks the coccidian test"),
   ("A lumbar puncture",
    "A lumbar puncture showing elevated eosinophils helps identify rat lungworm, Angiostrongylus cantonensis, as "
    "eosinophilic meningitis. Pinworm eggs on the perianal folds are collected by the tape test.",
    "picks a worm test for the nervous system")],
  ci(95, 6, 94, 60, 76, 99),
  img="wr3-fig-11.jpg",
  alt="Three oval, colorless eggs side by side, each slightly flattened on one side, with a granular interior"),

# ---------------------------------------------------------------- 2.14 (cold) Trichinella — PICTURE + symptoms
Q("2.14", "cold", "B", "Trichinella spiralis: the food (picture)", IO2,
  "The muscle section pictured shows coiled larvae walled off within the fibers. Eating which food most often "
  "transmits this worm?",
  ("Undercooked pork",
   "Correct: coiled larvae encysted in muscle are Trichinella spiralis, acquired from eating undercooked pork or bear "
   "meat. The person eats the encysted worm, gastric passage releases the larva, and new larvae migrate to muscle, "
   "heart and brain to form cysts."),
  [("Raw freshwater fish",
    "Raw or inadequately cooked freshwater fish transmits Opisthorchis sinensis, whose larvae mature in the bile duct. "
    "Larvae encysted in muscle fibers are Trichinella spiralis, from undercooked pork.",
    "picks a fluke's food source"),
   ("Unwashed fresh produce",
    "Fresh produce and water transmit Cyclospora, and contaminated food carries Ascaris eggs; neither encysts in "
    "muscle. Coiled larvae walled off in muscle are Trichinella spiralis, eaten in undercooked pork.",
    "picks a fecal-oral source"),
   ("Undercooked crustaceans",
    "Undercooked crustaceans transmit the lung fluke Paragonimus westermani, with cough and pleural pain. Larvae "
    "encysted in skeletal muscle are Trichinella spiralis, acquired from undercooked pork or bear meat.",
    "picks a fluke's food source")],
  ci(101, 7, 82, 102, 116, 75, 92),
  img="wr3-fig-12.jpg",
  alt="Stained section of muscle tissue: pink muscle fibers containing several small coiled worms, each inside an "
      "oval capsule"),

Q("2.14", "cold", "B", "Trichinella spiralis: the two-stage illness", IO1,
  "After a flulike illness with diarrhea, a person who ate undercooked bear meat develops muscle and joint pain, "
  "shortness of breath and pronounced eosinophilia. Which worm is the most likely cause?",
  ("Trichinella spiralis",
   "Correct: Trichinella spiralis comes from undercooked pork or bear meat. The first symptoms are flulike with "
   "diarrhea; the second, as larvae migrate and encyst in muscle, are muscle and joint pain, shortness of breath and "
   "pronounced eosinophilia."),
  [("Taenia saginata",
    "Taenia saginata, the beef tapeworm, comes from raw beef and causes few symptoms, mainly vague abdominal pain, "
    "nausea and proglottids in stool. Muscle pain with eosinophilia after bear meat is Trichinella spiralis.",
    "picks another meat-borne worm"),
   ("Ascaris lumbricoides",
    "Ascaris lumbricoides eggs are swallowed in food or drink, not meat, and lung migration can cause eosinophilic "
    "pneumonitis. Muscle and joint pain after undercooked bear meat points to Trichinella spiralis.",
    "matches on eosinophilia and breathing symptoms alone"),
   ("Angiostrongylus cantonensis",
    "Angiostrongylus cantonensis comes from snails, water or vegetables and causes eosinophilic meningitis with a "
    "stiff neck. A flulike illness followed by muscle pain after bear meat is Trichinella spiralis.",
    "matches on eosinophilia alone")],
  c(101, 119, 91, 92, 98, 99)),

# ---------------------------------------------------------------- 2.15 (it) Toxocara
Q("2.15", "it", "B", "Toxocara: how humans are infected", IO2,
  "Toxocara canis and Toxocara cati are the roundworms of dogs and cats. How do humans, their accidental hosts, "
  "usually become infected?",
  ("Ingesting eggs from pet feces",
   "Correct: humans are accidental hosts of the dog and cat roundworms, infected by ingesting infective eggs from "
   "feces or by eating undercooked meat of a transport host. The larvae migrate through tissues, and reaching the eye "
   "or liver gives ocular or visceral toxocariasis."),
  [("Larvae penetrating bare feet",
    "Larvae penetrating the skin of bare feet is the hookworm's route, from soil contaminated with feces. Toxocara is "
    "swallowed: humans ingest infective eggs from dog or cat feces.",
    "borrows the hookworm's route"),
   ("Bite of an infected fly",
    "A fly bite spreads tissue nematodes such as Loa loa, the eye worm. Toxocara has no insect vector; people swallow "
    "infective eggs from the feces of dogs and cats.",
    "assigns a vector to an intestinal roundworm"),
   ("Eating raw freshwater fish",
    "Raw freshwater fish transmits the Chinese liver fluke, Opisthorchis sinensis. Toxocara reaches humans from their "
    "pets, by ingestion of infective eggs from dog or cat feces.",
    "picks a fluke's food source")],
  c(108, 8, 96, 107, 116)),

# ---------------------------------------------------------------- 2.16 (it) Opisthorchis sinensis
Q("2.16", "it", "B", "Opisthorchis sinensis: the raw-fish fluke", IO2,
  "A person who often eats raw freshwater fish develops a fluke infection; the larvae crawl into the bile duct and "
  "mature there. Which fluke is it?",
  ("Opisthorchis sinensis",
   "Correct: Opisthorchis sinensis, the Chinese liver fluke, cycles between mammals, snails and fish. Humans are "
   "infected by eating inadequately cooked fish containing cercariae, as in freshwater sushi; the larvae crawl into "
   "the bile duct, mature and shed eggs into feces."),
  [("Fasciola hepatica",
    "Fasciola hepatica also lodges in the liver, but it cycles between herbivores, snails and aquatic plants, and "
    "humans acquire it by eating raw aquatic plants. A liver fluke from raw freshwater fish is Opisthorchis sinensis.",
    "picks the other liver fluke"),
   ("Paragonimus westermani",
    "Paragonimus westermani is the lung fluke, acquired by eating undercooked crustaceans, with cough and pleural "
    "pain. A fluke from raw freshwater fish that matures in the bile duct is Opisthorchis sinensis.",
    "picks the fluke from seafood"),
   ("Schistosoma mansoni",
    "Schistosoma mansoni is a blood fluke whose larvae penetrate the skin in snail-infested water; it is not eaten. A "
    "fluke from raw freshwater fish that lives in the bile duct is Opisthorchis sinensis.",
    "picks the best-known fluke")],
  c(116, 8, 117, 112)),

# ---------------------------------------------------------------- 2.17 (it) Echinococcus — PICTURE
Q("2.17", "it", "B", "Echinococcus: hydatid cyst (picture)", IO1,
  "At surgery, a large, slowly enlarging cyst like the one pictured is removed from beside a patient's liver. Which "
  "parasite causes it?",
  ("Echinococcus",
   "Correct: Echinococcus, a tiny tapeworm acquired from dogs, causes cystic echinococcosis, or hydatid disease, with "
   "slowly enlarging cysts in the liver and lungs. Treatment often involves surgical removal of the parasitic masses, "
   "though chemotherapy is also used."),
  [("Taenia saginata",
    "Taenia saginata, the beef tapeworm, lives as an adult in the small intestine and sheds proglottids in stool; it "
    "does not form liver cysts. A large hydatid cyst removed at surgery is Echinococcus.",
    "picks the best-known tapeworm"),
   ("Fasciola hepatica",
    "Fasciola hepatica is a liver fluke from raw aquatic plants that lodges in the liver and later inflames or blocks "
    "the bile duct; it does not form a large cyst. Hydatid cysts in the liver are Echinococcus.",
    "picks another liver parasite"),
   ("Trichinella spiralis",
    "Trichinella spiralis forms tiny cysts of coiled larvae inside muscle, heart and brain, not a large liver mass. "
    "A large, slowly enlarging cyst removed from the liver is a hydatid cyst of Echinococcus.",
    "picks another cyst-forming worm")],
  ci(125, 8, 124, 119, 117, 101),
  img="wr3-fig-15.jpg",
  alt="Open abdominal surgery: a large, smooth, glistening white cyst with red blood vessels on its surface, bulging "
      "beside the liver"),

# ---------------------------------------------------------------- 2.18 (cold) antihelminthic drugs
Q("2.18", "cold", "B", "Antihelminthic drugs: shared drawback", IO1,
  "Worm infections are often difficult to eliminate without drugs. Which drawback do many antihelminthic drugs share?",
  ("Toxic side effects",
   "Correct: many antihelminthic drugs have toxic side effects, much as antiprotozoan drugs, which work against "
   "eukaryotic cells, carry toxicity problems. They act by suppressing a helminthic metabolic process that differs "
   "from the human one, inhibiting the worm's movement or acting locally in the intestine."),
  [("Action only in the blood",
    "Antihelminthic drugs are not limited to the blood; some act locally in the intestine, and others prevent the "
    "worm holding its position. The drawback many of them share is toxic side effects.",
    "reverses the drugs' local intestinal action"),
   ("No effect on worm movement",
    "Inhibiting the worm's movement is one way antihelminthic drugs work, not a drawback they lack. The shared "
    "drawback of many antihelminthic drugs is their toxic side effects.",
    "reverses a listed mechanism of action"),
   ("Blocking processes humans share",
    "Antihelminthic drugs aim at a helminthic metabolic process that differs from the human process, not one humans "
    "share. Even so, many carry toxic side effects, the drawback they have in common.",
    "reverses the drugs' selective target")],
  c(86, 14)),
]
