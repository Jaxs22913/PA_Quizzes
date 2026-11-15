# -*- coding: utf-8 -*-
# Microbiology Exam 3 — "Webster Review" master exams, forms A and B, Lecture 14 (Gram-Negative Bacilli of Medical
# Importance, Dr. Webster). Her review of this lecture: part 3 of the 13 Nov 2026 recording [0:00-15:01]. Her words
# only WEIGHT what is asked; every fact is from the visible slides (text + pictures), never speaker notes.
#
# COUNTS: 20 per form (40 total). Per form: one item each for 1.1-1.16 (16) plus extras:
#   1.8 (the four Escherichia coli types) x4 in BOTH forms, each form covering all four types:
#       A = enterotoxigenic (traveler with watery diarrhea, cramping, little or no fever), enteroinvasive (large-
#           intestine disease similar to shigellosis), enteropathogenic (infant wasting diarrhea, microvilli
#           destroyed), enterohemorrhagic (bloody diarrhea then hemolytic uremic syndrome after beef);
#       B = enterotoxigenic (fimbriae to the small intestine + heat-labile/heat-stable toxins), enteroinvasive (the
#           very young and very old most susceptible), enteropathogenic (greatest single cause of infant mortality
#           worldwide), enterohemorrhagic (reservoir in the intestines of cattle).
#   1.16 endotoxin x2 in form A (low level = fever/malaise; lipopolysaccharide of the outer membrane), x1 in B
#       (large flood = septic shock).
#   1.14 Yersinia pestis x1 in A (recognition from flea bite + bubo), x2 in B (rodent reservoir; septicemic form).
# Forms A and B ask different facts for every item. Stems are written to avoid the topic-quiz stems in
# micro_l14_pool_a.py / micro_l14_pool_b.py (mostly by asking in the other direction: findings -> organism).
#
# PICTURES (each used once): A 1.7 = wr3-fig-01 (green-sheen colonies on eosin methylene blue agar, image on slide
#   48; the item asks which genus is a lactose fermenter, so it never relies on reading the sheen itself);
#   A 1.10 = wr3-fig-02 (swarming plate, image on slide 71; asks the PROPERTY behind it, high motility, not the
#   genus). Both viewed, with slides 44, 48 and 71.
#
# HER WORDS VERSUS THE SLIDES (the slide is keyed; her wording never is):
#   - "rotten grape odor" vs slide 18 "Grapelike odor": keyed "grapelike odor".
#   - endotoxin "released when the organism dies" vs slide 5 (on lysis, including antibiotic therapy, AND as cells
#     grow and divide): no item keys release timing (the topic quiz already asks it); explanations quote slide 5.
#   - septicemic plague "the black death" vs slide 88 "black plague": neither name is keyed; the septicemic item is
#     keyed from the findings (intravascular coagulation, purpura, necrosis, gangrene).
#   - "rat flea" vs slides 83/84 flea vectors and rodents: stems say "fleas" and "rodents"; "rat flea" not keyed.
#   - pneumonic plague "directly transmitted person to person" vs slide 88 "highly contagious by aerosol" and slide
#     83 (from infected humans rare): no item keys person-to-person spread; pneumonic appears only as a distractor
#     explained as "localized to the lungs, highly contagious by aerosol".
#   - tularemia "breaks in your skin" not on slide 29: not used (the tularemia items use contact with infected
#     animals, ulcerative skin lesions, swollen lymph nodes).
#   - Typhoid Mary / bile in every bowel movement: not on a slide; the carrier item uses slide 73 only
#     ("some chronic carriers shed bacilli from gallbladder").
# DECK CONTRADICTION: slide 97 lists H. parainfluenzae as responsible for childhood meningitis, slide 100 gives it
#   endocarditis: Haemophilus parainfluenzae is kept out of every option.
# CONTENT BOUNDARY: nothing on bioweapons/bioterrorism or infective doses (slides 28, 29, 88 mention them; left out).
# HELD: drug names and doses, case counts, percentages, outbreak dates, years; Burkholderia, Acinetobacter and
#   Stenotrophomonas appear only as distractors (light touch, never keyed).
# SPELLING / ABBREVIATIONS: written in full (Escherichia coli types, hemolytic uremic syndrome); deck "Salmonella
#   typhi" kept as written. KEYS AUTHORED AT INDEX 0 (c=0); positions are permuted by the renderer.

SRC = "Lecture 14  Dr. Webster Gram Negative Bacilli of Medical Importance.pptx"
LEC = 14
IMG = "micro-exam-3-quiz-images"


def cl(*n):
    return f"{SRC}, Slide {n[0]}" if len(n) == 1 else f"{SRC}, Slides " + ", ".join(map(str, n[:-1])) + " and " + str(n[-1])


def ci(img, *n):
    return (cl(*n) + f" and image on Slide {img}") if n else f"{SRC}, image on Slide {img}"


IO = {
    1: ("1 — Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, clinical "
        "manifestations, methods of treatment, and prevention of Gram-negative bacilli of medical importance"),
    2: "2 — Describe the modes of transmission by which humans acquire Gram-negative bacilli of medical importance",
}


def Q(item, tier, form, topic, io, q, key, wrongs, cite, **extra):
    """key = (text, explanation); wrongs = [(text, explanation, misconception) x3]"""
    d = dict(lecture=LEC, item=item, tier=tier, form=form, topic=topic, io=IO[io], q=q,
             opts=[[key[0], key[1]]] + [[w[0], w[1]] for w in wrongs],
             mis={w[0]: w[2] for w in wrongs}, c=0, cite=cite)
    d.update(extra)
    return d


POOL = [

# ============================================================ 1.1 (cold) Pseudomonas aeruginosa
Q("1.1", "cold", "A", "Pseudomonas aeruginosa: persisting despite cleaning", 1,
  ("A burn unit keeps finding Pseudomonas aeruginosa on sinks and equipment despite routine cleaning. Which property "
   "of the organism best explains this?"),
  ("It resists soaps and disinfectants",
   "Correct: Pseudomonas aeruginosa is resistant to soaps, dyes, quaternary ammonium disinfectants, drugs and drying, "
   "and it survives in nutrient-poor environments, so routine cleaning fails to clear it. That is why it is a major "
   "agent of nosocomial infections, including in hosts with burns."),
  [("It forms heat-resistant spores",
    "The aerobic Gram-negative nonenteric bacilli are non-spore-forming, so spores cannot explain its persistence. "
    "Pseudomonas aeruginosa persists because it resists soaps, disinfectants, drugs and drying.",
    "gives a Gram-negative rod the spores of Gram-positive genera"),
   ("It must live inside amebas",
    "Living in close association with amebas in water is a Legionella trait. Pseudomonas aeruginosa is free living "
    "and survives in nutrient-poor environments; it persists because it resists soaps and disinfectants.",
    "adjacent fact from the same lecture (Legionella)"),
   ("It needs blood-rich surfaces",
    "Needing chocolate agar and hemin is Haemophilus, a fastidious genus sensitive to drying, temperature extremes "
    "and disinfectants. Pseudomonas aeruginosa survives nutrient-poor places and resists disinfectants.",
    "confuses a hardy organism with a fastidious one")],
  cl(13, 16, 18, 39, 97)),

Q("1.1", "cold", "B", "Pseudomonas aeruginosa: recognizing it in the laboratory", 1,
  ("A sputum culture from a patient with cystic fibrosis grows a Gram-negative rod with a grapelike odor and a "
   "greenish-blue pigment. Which organism is it?"),
  ("Pseudomonas aeruginosa",
   "Correct: a grapelike odor and the greenish-blue pigment pyocyanin mark Pseudomonas aeruginosa, a common cause of "
   "nosocomial infection in hosts with cystic fibrosis, burns or neoplastic disease."),
  [("Burkholderia cepacia",
    "Burkholderia cepacia is a relative of the pseudomonads and is also a particular problem in cystic fibrosis, but "
    "the grapelike odor and greenish-blue pyocyanin are the laboratory marks of Pseudomonas aeruginosa.",
    "adjacent organism with the same host group (cystic fibrosis)"),
   ("Serratia marcescens",
    "Serratia marcescens is a coliform that makes a RED pigment, prodigiosin, and causes pneumonia in chronic "
    "alcoholics. A greenish-blue pigment with a grapelike odor points to Pseudomonas aeruginosa.",
    "confuses one pigment-producing Gram-negative rod with another"),
   ("Klebsiella pneumoniae",
    "Klebsiella pneumoniae is a coliform recognized by its large capsule and is a cause of nosocomial pneumonia; it "
    "is not described with a pigment. Greenish-blue pyocyanin and a grapelike odor point to Pseudomonas aeruginosa.",
    "competing nosocomial respiratory Gram-negative rod")],
  cl(18, 22, 66, 68)),

# ============================================================ 1.2 (it) Brucella
Q("1.2", "it", "A", "Brucellosis: recognizing undulant fever", 2,
  ("A slaughterhouse worker has had a fever that rises and falls over several months, with chills, sweating, "
   "headache, muscle pain and weight loss. Which organism is the most likely cause?"),
  ("Brucella abortus",
   "Correct: brucellosis is a zoonosis caught by animal handling or slaughtering, through contact with the blood, "
   "urine or placentas of infected animals (Brucella abortus is the cattle species). Its fever fluctuates for weeks "
   "to a year, the undulant fever, with chills, sweating, headache, muscle pain and weight loss."),
  [("Francisella tularensis",
    "Francisella tularensis causes tularemia (rabbit fever), caught from infected animals, water, dust or vector "
    "bites, with ulcerative skin lesions and swollen lymph nodes. A fever that undulates for months is brucellosis.",
    "competing zoonosis from animal contact"),
   ("Salmonella typhi",
    "Salmonella typhi causes typhoid fever, with a SUSTAINED fever of 103-104 degrees and rose-colored spots, from "
    "fecally contaminated food or water; humans are its only hosts. A rising-and-falling fever after slaughter work "
    "is brucellosis.",
    "confuses a sustained fever with a fluctuating one"),
   ("Legionella pneumophila",
    "Legionella pneumophila is caught by inhaling aerosols from water sources such as cooling towers and causes "
    "pneumonia with fever and cough. A months-long undulant fever in a slaughterhouse worker is brucellosis.",
    "competing febrile illness with a different source")],
  cl(27, 28, 29, 40, 73, 74)),

Q("1.2", "it", "B", "Brucellosis: its other names", 1,
  "Which of these is another name for brucellosis?",
  ("Malta fever",
   "Correct: brucellosis, the zoonosis caused by Brucella species, is also called Malta fever, undulant fever (for "
   "its fluctuating fever) and Bang disease."),
  [("Rabbit fever",
    "Rabbit fever is tularemia, caused by Francisella tularensis, a zoonosis of mammals of the northern hemisphere, "
    "particularly rabbits. Brucellosis is Malta fever, undulant fever or Bang disease.",
    "adjacent zoonosis name from the same lecture (tularemia)"),
   ("Pontiac fever",
    "Pontiac fever is one of the two illnesses Legionella causes, along with Legionnaires disease, from inhaled water "
    "aerosols. Brucellosis is also called Malta fever, undulant fever or Bang disease.",
    "adjacent disease name from the same lecture (Legionella)"),
   ("Typhoid fever",
    "Typhoid fever is caused by Salmonella typhi, with humans as its only hosts and a sustained high fever. "
    "Brucellosis, a zoonosis from cattle or pigs, is called Malta fever, undulant fever or Bang disease.",
    "confuses two febrile diseases by name")],
  cl(27, 29, 40, 73, 74)),

# ============================================================ 1.3 (cold) Francisella tularensis
Q("1.3", "cold", "A", "Tularemia: recognizing rabbit fever", 2,
  ("A hunter who skinned several wild rabbits develops fever, chills and headache, an ulcerating skin lesion and "
   "swollen lymph nodes. Which organism is the most likely cause?"),
  ("Francisella tularensis",
   "Correct: tularemia (rabbit fever) is a zoonosis of mammals of the northern hemisphere, particularly rabbits, "
   "transmitted by contact with infected animals. It brings fever, chills and headache with ulcerative skin lesions "
   "and swollen lymph nodes."),
  [("Brucella abortus",
    "Brucella abortus is the cattle species of brucellosis, caught by handling cattle or drinking unpasteurized "
    "dairy, with a fever that fluctuates for weeks to a year. Rabbit contact with ulcerative skin lesions is tularemia.",
    "competing zoonosis with a different animal reservoir"),
   ("Burkholderia pseudomallei",
    "Burkholderia pseudomallei causes melioidosis, acquired from soil and water of tropical climates by penetrating "
    "injury or inhalation, with wound nodules. Skinning wild rabbits points to Francisella tularensis.",
    "wound infection from soil confused with an animal-contact zoonosis"),
   ("Legionella pneumophila",
    "Legionella pneumophila lives in water and is inhaled as aerosols, causing pneumonia; it is not described with "
    "ulcerative skin lesions. Rabbit contact with an ulcer and swollen nodes points to tularemia.",
    "competing Gram-negative cause of fever with a water source")],
  cl(23, 27, 28, 29, 39, 40)),

Q("1.3", "cold", "B", "Tularemia: skin finding", 1,
  ("A patient with tularemia has fever, chills, malaise and swollen lymph nodes. Which skin finding also fits this "
   "disease?"),
  ("Ulcerative skin lesions",
   "Correct: tularemia (rabbit fever, Francisella tularensis) brings headache, fever, chills, malaise and weakness "
   "with ulcerative skin lesions and swollen lymph nodes."),
  [("Rose-colored spots",
    "A rash of rose-colored spots, with a sustained fever of 103-104 degrees, marks typhoid fever from Salmonella "
    "typhi. The skin finding of tularemia is an ulcerative skin lesion.",
    "adjacent rash from the same lecture (typhoid fever)"),
   ("Purpura turning to gangrene",
    "Subcutaneous hemorrhage and purpura that degenerate into necrosis and gangrene mark septicemic plague from "
    "Yersinia pestis. Tularemia gives ulcerative skin lesions with swollen lymph nodes.",
    "adjacent skin finding from the same lecture (septicemic plague)"),
   ("Nodules in a soil wound",
    "Wound infections with localized nodules, after a penetrating injury in tropical soil or water, are melioidosis "
    "from Burkholderia pseudomallei. Tularemia gives ulcerative skin lesions with swollen lymph nodes.",
    "adjacent skin finding from the same lecture (melioidosis)")],
  cl(23, 29, 74, 88)),

# ============================================================ 1.4 (cold) Bordetella pertussis
Q("1.4", "cold", "A", "Pertussis: recognizing the two stages", 1,
  ("A child's cough illness began like a cold, with nasal drainage, congestion and sneezing. It has become fits of "
   "persistent coughing, each followed by a deep, noisy inhalation. Which organism is the cause?"),
  ("Bordetella pertussis",
   "Correct: Bordetella pertussis causes pertussis (whooping cough). Its catarrhal stage brings nasal drainage, "
   "congestion, sneezing and an occasional cough; the paroxysmal stage brings a recurrent persistent cough followed "
   "by a deep inhalation, the whoop."),
  [("Haemophilus influenzae",
    "Haemophilus influenzae causes acute bacterial meningitis, epiglottitis, otitis media, sinusitis, pneumonia and "
    "bronchitis, but not a cold-like stage followed by coughing fits and a whoop, which is pertussis.",
    "competing childhood respiratory pathogen"),
   ("Legionella pneumophila",
    "Legionella pneumophila is inhaled in water aerosols and causes Legionnaires disease (fever, cough, pneumonia), "
    "mostly in older adults and smokers. A catarrhal stage then a whooping cough is Bordetella pertussis.",
    "competing respiratory Gram-negative rod"),
   ("Klebsiella pneumoniae",
    "Klebsiella pneumoniae, a normal inhabitant of the respiratory tract with a large capsule, causes nosocomial "
    "pneumonia. A cold-like start followed by paroxysms and a whoop is pertussis from Bordetella pertussis.",
    "competing respiratory Gram-negative rod")],
  cl(30, 31, 40, 66, 98)),

Q("1.4", "cold", "B", "Pertussis: the catarrhal stage", 1,
  "Which finding marks the catarrhal stage of pertussis?",
  ("Nasal drainage and sneezing",
   "Correct: the catarrhal stage of pertussis brings nasal drainage, congestion, sneezing and an occasional cough. "
   "Only in the later paroxysmal stage does the recurrent persistent cough end in a deep inhalation, the whoop."),
  [("Coughing fits ending in a whoop",
    "A recurrent persistent cough followed by a deep inhalation, the whoop, is the paroxysmal stage, which comes "
    "after the catarrhal stage. The catarrhal stage is nasal drainage, congestion and sneezing.",
    "confuses the two stages of pertussis (reversed order)"),
   ("A fever that comes and goes",
    "A fever that fluctuates for weeks to a year is the undulant fever of brucellosis, not a stage of pertussis. The "
    "catarrhal stage of pertussis is nasal drainage, congestion, sneezing and an occasional cough.",
    "adjacent fact from the same lecture (brucellosis)"),
   ("Fever, diarrhea, pneumonia",
    "Fever, cough, diarrhea, abdominal pain and pneumonia describe legionellosis, caught from water aerosols. The "
    "catarrhal stage of pertussis is nasal drainage, congestion, sneezing and an occasional cough.",
    "adjacent fact from the same lecture (Legionella)")],
  cl(28, 31, 40)),

# ============================================================ 1.5 (cold) Legionella
Q("1.5", "cold", "A", "Legionella: recognizing it from a water spray", 2,
  ("Several shoppers who stood near a supermarket's vegetable spraying system develop fever, cough and pneumonia. "
   "The sickest is an older man who smokes. Which organism is the most likely cause?"),
  ("Legionella pneumophila",
   "Correct: Legionella is widely distributed in water, including supermarket vegetable spraying systems, and is "
   "transmitted by aerosols. Legionellosis brings fever, cough and pneumonia and is prevalent in males over 50 and "
   "in smokers."),
  [("Bordetella pertussis",
    "Bordetella pertussis spreads by direct contact or inhaled aerosols from apparently healthy carriers, not from "
    "water systems, and causes whooping cough, a childhood affliction. A water spray outbreak is legionellosis.",
    "competing aerosol-borne respiratory pathogen"),
   ("Haemophilus influenzae",
    "Haemophilus influenzae causes meningitis, epiglottitis, otitis media, sinusitis, pneumonia and bronchitis, but "
    "it is fastidious and sensitive to drying, not a water-system organism. A spray-system outbreak is Legionella.",
    "competing respiratory Gram-negative rod"),
   ("Klebsiella pneumoniae",
    "Klebsiella pneumoniae is a normal inhabitant of the respiratory tract and a cause of nosocomial pneumonia, not "
    "an organism spread from water sprays. Pneumonia after exposure to a vegetable sprayer points to Legionella.",
    "competing cause of Gram-negative pneumonia")],
  cl(30, 39, 40, 66, 97, 98)),

Q("1.5", "cold", "B", "Legionella: the source of an outbreak", 2,
  ("Investigators trace a cluster of Legionnaires disease among hotel guests. Which source fits the way this "
   "organism reaches people?"),
  ("Mist from a decorative fountain",
   "Correct: Legionella lives in water (tap water, cooling towers, spas, ponds, air conditioning, vegetable sprayers) "
   "and is transmitted by aerosols; tourists have contracted it from the spray of a decorative fountain."),
  [("Undercooked hamburger patties",
    "Contaminated beef, water and vegetables spread enterohemorrhagic Escherichia coli O157:H7, whose reservoir is "
    "the intestines of cattle. Legionella is inhaled in aerosols from water, such as a fountain's spray.",
    "foodborne enteric source confused with an aerosol source"),
   ("Unpasteurized dairy products",
    "Unpasteurized dairy products, or contact with infected animals, spread brucellosis. Legionnaires disease is "
    "acquired by inhaling aerosols from water sources such as cooling towers and fountains.",
    "adjacent transmission route from the same lecture (Brucella)"),
   ("Bites of infected fleas",
    "Flea vectors transmit Yersinia pestis, the cause of plague, from rodents. Legionella has no vector; it is "
    "inhaled in aerosols from water sources such as cooling towers, spas and fountains.",
    "adjacent transmission route from the same lecture (plague)")],
  cl(27, 39, 40, 42, 60, 83)),

# ============================================================ 1.6 (cold) toxigenic versus invasive diarrhea
Q("1.6", "cold", "A", "Diarrheal disease: where the blood comes from", 1,
  ("Diarrheal disease is grouped as toxigenic or invasive. In the invasive type, what produces the blood in the "
   "stool?"),
  ("Bacteria damaging the epithelium",
   "Correct: in invasive diarrheal disease (example: Shigella) the bacteria enter the intestinal epithelium and "
   "damage it, so blood appears. In the toxigenic type (example: enterotoxigenic Escherichia coli) the bacteria "
   "stay on the surface and cause oversecretion of fluid."),
  [("Toxins driving fluid secretion",
    "Toxins driving oversecretion of fluid mark the toxigenic type (example: enterotoxigenic Escherichia coli), "
    "with diarrhea, cramping and low-grade or no fever. The invasive type bleeds because bacteria damage the "
    "epithelium.",
    "the other kind of diarrheal disease (toxigenic)"),
   ("Blocked vitamin B1 uptake",
    "Inhibiting vitamin B1 (thiamin) uptake, with adherence that destroys microvilli, belongs to enteropathogenic "
    "Escherichia coli and its infant wasting diarrhea. Invasive disease bleeds because bacteria damage the "
    "epithelium.",
    "borrows enteropathogenic Escherichia coli's effect"),
   ("Low-level endotoxin release",
    "Low levels of endotoxin cause a low-level inflammatory response, with fever, malaise, aches and pains, not "
    "bleeding into the bowel. Invasive disease bleeds because bacteria enter and damage the epithelium.",
    "general endotoxin effect taken for the bowel mechanism")],
  cl(11, 44, 56, 58)),

Q("1.6", "cold", "B", "Diarrheal disease: Shigella against the toxigenic type", 1,
  ("Compared with the diarrhea of enterotoxigenic Escherichia coli, what marks the diarrhea caused by Shigella?"),
  ("Blood, from invaded mucosa",
   "Correct: Shigella is the example of invasive diarrheal disease: it invades the villus of the large intestine and "
   "its enterotoxin damages mucosa and villi, so the watery stool contains blood. Enterotoxigenic Escherichia coli is "
   "toxigenic: its toxins promote secretion of fluid and electrolytes."),
  [("Watery fluid from oversecretion",
    "Oversecretion of fluid and electrolytes, with no invasion, is the toxigenic diarrhea of enterotoxigenic "
    "Escherichia coli itself. Shigella is invasive, and its stool contains blood.",
    "the other kind of diarrheal disease (toxigenic)"),
   ("Spread from bowel into blood",
    "Shigella invades the villus of the large intestine but does not invade the blood; it is Salmonella typhi that "
    "goes from invasive diarrhea to septicemia. The mark of shigellosis is blood in the stool from invaded mucosa.",
    "confuses Shigella with Salmonella typhi"),
   ("Perforation of the bowel wall",
    "Shigella does not perforate the intestine; it invades the villus of the large intestine and enters Peyer's "
    "patches, causing inflammation. The mark of its diarrhea is blood from the invaded mucosa.",
    "overstates the depth of invasion")],
  cl(44, 56, 74, 78)),

# ============================================================ 1.7 (cold) coliform versus non-coliform
Q("1.7", "cold", "A", "Lactose fermenters on eosin methylene blue agar", 1,
  ("A stool sample is plated on eosin methylene blue agar, a medium selective for Gram-negative bacteria and "
   "differential for lactose fermenters. The colonies shown grow as lactose fermenters. Which genus fits?"),
  ("Escherichia",
   "Correct: the enterics are divided into coliforms (lactose fermenters) and non-coliforms (non-lactose fermenters). "
   "Escherichia coli is a coliform, the lactose-positive organism that eosin methylene blue and MacConkey's agar "
   "pick out as a lactose fermenter."),
  [("Proteus",
    "Proteus is a non-coliform: a lactose-negative, highly motile opportunist recognized by its swarming growth. A "
    "lactose fermenter on eosin methylene blue agar fits a coliform such as Escherichia.",
    "non-coliform taken for a lactose fermenter"),
   ("Salmonella",
    "Salmonella is a non-coliform, lactose-negative enteric and a true pathogen. A lactose fermenter on eosin "
    "methylene blue agar fits a coliform such as Escherichia.",
    "true pathogen taken for a lactose fermenter"),
   ("Shigella",
    "Shigella is a non-coliform, lactose-negative enteric and a true pathogen that causes bacillary dysentery. A "
    "lactose fermenter on eosin methylene blue agar fits a coliform such as Escherichia.",
    "true pathogen taken for a lactose fermenter")],
  ci(48, 46, 50, 69, 71),
  img=IMG + "/wr3-fig-01.jpg",
  alt=("A petri dish of dark red agar streaked in sections; the heavy growth of small colonies has a shiny, "
       "yellow-green metallic sheen")),

Q("1.7", "cold", "B", "Choosing a medium to separate coliforms", 1,
  ("A laboratory wants to screen enteric isolates and separate the coliforms from the non-coliforms. Which plating "
   "medium does this?"),
  ("MacConkey's agar",
   "Correct: coliforms are lactose fermenters and non-coliforms are not. MacConkey's agar is selective for "
   "Gram-negative bacteria (crystal violet and bile salts) and differential for lactose fermenters, so it separates "
   "the two groups; eosin methylene blue agar does the same."),
  [("Chocolate agar",
    "Chocolate agar (cooked blood) is used to grow the fastidious Haemophilus, which cannot grow on blood agar "
    "without special techniques. It does not differentiate lactose fermenters; MacConkey's agar does.",
    "adjacent medium from the same lecture (Haemophilus)"),
   ("Charcoal yeast extract agar",
    "Charcoal yeast extract agar is the medium on which Legionella pneumophila is grown. It does not differentiate "
    "lactose fermenters from non-fermenters; MacConkey's agar does.",
    "adjacent medium from the same lecture (Legionella)"),
   ("Rainbow agar",
    "Rainbow agar contains chromogenic substrates for two enzymes and is used to identify Escherichia coli O157:H7 "
    "rapidly (its colonies are black). Separating coliforms from non-coliforms by lactose uses MacConkey's agar.",
    "adjacent medium from the same lecture (O157:H7 identification)")],
  cl(41, 46, 48, 64, 97)),

# ============================================================ 1.8 (cold) the four Escherichia coli types
Q("1.8", "cold", "A", "Escherichia coli types: traveler's watery diarrhea", 1,
  ("A traveler develops watery diarrhea with cramping and little or no fever. The strain's toxins make the intestinal "
   "epithelium secrete fluid and electrolytes. Which type of Escherichia coli is it?"),
  ("Enterotoxigenic Escherichia coli",
   "Correct: enterotoxigenic Escherichia coli makes heat-labile and heat-stable toxins that promote secretion of "
   "fluid and electrolytes, giving diarrhea, cramping and low-grade to no fever; it causes most traveler's diarrhea."),
  [("Enteroinvasive Escherichia coli",
    "Enteroinvasive Escherichia coli has no toxins; it damages the large intestinal wall mechanically, giving profuse "
    "bloody diarrhea and high fever. Watery, toxin-driven diarrhea with little fever is enterotoxigenic.",
    "invasive type taken for the toxigenic type"),
   ("Enteropathogenic Escherichia coli",
    "Enteropathogenic Escherichia coli adheres to the intestinal lining and destroys microvilli, causing the wasting "
    "form of infantile diarrhea. A traveler's toxin-driven watery diarrhea is enterotoxigenic.",
    "infant wasting type taken for the traveler's type"),
   ("Enterohemorrhagic Escherichia coli",
    "Enterohemorrhagic Escherichia coli (O157:H7) causes hemorrhagic colitis and can lead to hemolytic uremic "
    "syndrome. Watery diarrhea with cramping and little or no fever in a traveler is enterotoxigenic.",
    "hemorrhagic type taken for the watery type")],
  cl(56, 57, 58, 59)),

Q("1.8", "cold", "A", "Escherichia coli types: disease like shigellosis", 1,
  ("Which type of Escherichia coli causes an inflammatory disease of the large intestine similar to shigellosis?"),
  ("Enteroinvasive Escherichia coli",
   "Correct: enteroinvasive Escherichia coli binds the intestinal wall with adhesin proteins and causes an "
   "inflammatory disease of the large intestine similar to shigellosis, with profuse bloody diarrhea and high fever."),
  [("Enterotoxigenic Escherichia coli",
    "Enterotoxigenic Escherichia coli adheres to the SMALL intestine by fimbriae and causes watery, toxin-driven "
    "diarrhea with low-grade or no fever. The shigellosis-like large-intestine disease is enteroinvasive.",
    "toxigenic type taken for the invasive type"),
   ("Enteropathogenic Escherichia coli",
    "Enteropathogenic Escherichia coli adheres to the intestinal lining and destroys microvilli, causing wasting "
    "infantile diarrhea. The shigellosis-like inflammatory disease of the large intestine is enteroinvasive.",
    "infant wasting type taken for the invasive type"),
   ("Enterohemorrhagic Escherichia coli",
    "Enterohemorrhagic Escherichia coli carries Shiga toxin and is feared for hemolytic uremic syndrome. The type "
    "described as similar to shigellosis, with no toxins, is enteroinvasive Escherichia coli.",
    "Shiga toxin link taken for the shigellosis-like type")],
  cl(56, 57, 58, 59, 60)),

Q("1.8", "cold", "A", "Escherichia coli types: infant wasting diarrhea", 1,
  ("An infant has a wasting form of diarrhea. The strain adheres to the intestinal lining and "
   "destroys the microvilli. Which type of Escherichia coli is it?"),
  ("Enteropathogenic Escherichia coli",
   "Correct: enteropathogenic Escherichia coli is the leading cause of the wasting form of infantile diarrhea; it "
   "adheres to the intestinal lining and destroys microvilli, and breast feeding helps prevent it."),
  [("Enterotoxigenic Escherichia coli",
    "Enterotoxigenic Escherichia coli acts through heat-labile and heat-stable toxins that cause fluid secretion; it "
    "is the traveler's diarrhea strain. Destruction of microvilli with infant wasting is enteropathogenic.",
    "toxigenic type taken for the adherent infant type"),
   ("Enteroinvasive Escherichia coli",
    "Enteroinvasive Escherichia coli causes a shigellosis-like inflammatory disease of the large intestine with "
    "profuse bloody diarrhea and high fever. Infant wasting with microvilli destroyed is enteropathogenic.",
    "invasive type taken for the adherent infant type"),
   ("Enterohemorrhagic Escherichia coli",
    "Enterohemorrhagic Escherichia coli comes from cattle and causes hemorrhagic colitis and hemolytic uremic "
    "syndrome. Wasting infantile diarrhea with destroyed microvilli is enteropathogenic.",
    "hemorrhagic type taken for the adherent infant type")],
  cl(56, 57, 58, 59, 60)),

Q("1.8", "cold", "A", "Escherichia coli types: kidney failure after bloody diarrhea", 1,
  ("A child develops bloody diarrhea after eating an undercooked hamburger, then hemolytic uremic syndrome. Which "
   "type of Escherichia coli is the most likely cause?"),
  ("Enterohemorrhagic Escherichia coli",
   "Correct: enterohemorrhagic Escherichia coli (the O157:H7 strain) has its reservoir in the intestines of cattle "
   "and is spread by contaminated beef, water and vegetables. It causes diarrhea and hemorrhagic colitis, and its "
   "toxins can lead to hemolytic uremic syndrome."),
  [("Enterotoxigenic Escherichia coli",
    "Enterotoxigenic Escherichia coli causes watery traveler's diarrhea with cramping and low-grade or no fever, "
    "through fluid-secreting toxins. Hemolytic uremic syndrome after contaminated beef is enterohemorrhagic.",
    "toxigenic type taken for the hemorrhagic type"),
   ("Enteroinvasive Escherichia coli",
    "Enteroinvasive Escherichia coli gives a bloody, shigellosis-like illness but has no toxins and is not tied to "
    "beef or hemolytic uremic syndrome. Bloody diarrhea after beef followed by that syndrome is enterohemorrhagic.",
    "the other bloody-diarrhea type"),
   ("Enteropathogenic Escherichia coli",
    "Enteropathogenic Escherichia coli causes wasting infantile diarrhea by destroying microvilli. Bloody diarrhea "
    "after undercooked beef, followed by hemolytic uremic syndrome, is enterohemorrhagic Escherichia coli.",
    "infant wasting type taken for the hemorrhagic type")],
  cl(56, 57, 58, 59, 60)),

Q("1.8", "cold", "B", "Escherichia coli types: fimbriae and two toxins", 1,
  ("Which type of Escherichia coli attaches to the small intestine by fimbriae and causes diarrhea with a "
   "heat-labile and a heat-stable toxin?"),
  ("Enterotoxigenic Escherichia coli",
   "Correct: enterotoxigenic Escherichia coli uses fimbriae for adhesion to the small intestine, and its heat-labile "
   "and heat-stable toxins promote secretion of fluid and electrolytes, causing diarrhea and cramping with low-grade "
   "or no fever."),
  [("Enteroinvasive Escherichia coli",
    "Enteroinvasive Escherichia coli has no toxins: it binds by adhesin proteins and damages the wall of the LARGE "
    "intestine mechanically. A strain with heat-labile and heat-stable toxins is enterotoxigenic.",
    "invasive type given the toxigenic type's toxins"),
   ("Enteropathogenic Escherichia coli",
    "Enteropathogenic Escherichia coli adheres to the intestinal lining and destroys microvilli, causing wasting "
    "infantile diarrhea; no heat-labile or heat-stable toxins are described. Those toxins mark enterotoxigenic.",
    "adherent infant type given the toxigenic type's toxins"),
   ("Enterohemorrhagic Escherichia coli",
    "Enterohemorrhagic Escherichia coli carries Shiga toxin, which halts protein synthesis in endothelial cells and "
    "can lead to hemolytic uremic syndrome. The heat-labile and heat-stable toxins belong to enterotoxigenic.",
    "confuses Shiga toxin with the heat-labile and heat-stable toxins")],
  cl(56, 57, 58, 59)),

Q("1.8", "cold", "B", "Escherichia coli types: who is most susceptible to the invasive type", 1,
  "Which patients are most susceptible to enteroinvasive Escherichia coli?",
  ("The very young and the very old",
   "Correct: the very young and the very old are most susceptible to enteroinvasive Escherichia coli, which causes "
   "a shigellosis-like inflammatory disease of the large intestine with profuse bloody diarrhea and high fever."),
  [("Infants with wasting diarrhea",
    "Infants with the wasting form of diarrhea, the greatest single cause of infant mortality worldwide, are the "
    "enteropathogenic Escherichia coli picture. For enteroinvasive, the very young and very old are most susceptible.",
    "adjacent fact from the same lecture (enteropathogenic type)"),
   ("Travelers to other countries",
    "Travelers are the classic victims of enterotoxigenic Escherichia coli, the cause of most traveler's diarrhea. "
    "For enteroinvasive Escherichia coli, the very young and very old are most susceptible.",
    "adjacent fact from the same lecture (enterotoxigenic type)"),
   ("Patients with cystic fibrosis",
    "Patients with cystic fibrosis are the classic hosts of Pseudomonas aeruginosa and Burkholderia cepacia "
    "infections, not of an intestinal Escherichia coli. The very young and very old are most susceptible here.",
    "adjacent host group from the same lecture (Pseudomonas)")],
  cl(18, 22, 56, 57, 58)),

Q("1.8", "cold", "B", "Escherichia coli types: infant mortality worldwide", 1,
  "Which type of Escherichia coli is the greatest single cause of infant mortality worldwide?",
  ("Enteropathogenic Escherichia coli",
   "Correct: enteropathogenic Escherichia coli is the leading cause of the wasting form of infantile diarrhea and "
   "the greatest single cause of infant mortality worldwide; breast feeding is its prevention."),
  [("Enterotoxigenic Escherichia coli",
    "Enterotoxigenic Escherichia coli is best known as the cause of most traveler's diarrhea, with watery stool and "
    "little fever. The greatest single cause of infant mortality worldwide is enteropathogenic.",
    "traveler's diarrhea type taken for the infant type"),
   ("Enteroinvasive Escherichia coli",
    "Enteroinvasive Escherichia coli causes a shigellosis-like disease of the large intestine in the very young and "
    "very old. The greatest single cause of infant mortality worldwide is enteropathogenic.",
    "invasive type taken for the infant type"),
   ("Enterohemorrhagic Escherichia coli",
    "Enterohemorrhagic Escherichia coli (O157:H7) is feared for hemolytic uremic syndrome after contaminated beef, "
    "water or vegetables. The greatest single cause of infant mortality worldwide is enteropathogenic.",
    "the most-feared type taken for the most deadly to infants")],
  cl(56, 57, 58, 59, 60)),

Q("1.8", "cold", "B", "Escherichia coli types: the one carried by cattle", 2,
  ("Which type of Escherichia coli has its reservoir in the intestines of cattle and reaches people through "
   "contaminated beef, water and vegetables?"),
  ("Enterohemorrhagic Escherichia coli",
   "Correct: enterohemorrhagic Escherichia coli, the O157:H7 strain, has its reservoir in the intestines of cattle "
   "and spreads through contaminated beef, water and vegetables; it can lead to hemolytic uremic syndrome."),
  [("Enterotoxigenic Escherichia coli",
    "Enterotoxigenic Escherichia coli is the traveler's diarrhea strain, with heat-labile and heat-stable toxins; "
    "no cattle reservoir is described for it. The type carried in cattle intestines is enterohemorrhagic.",
    "traveler's diarrhea type taken for the cattle-borne type"),
   ("Enteroinvasive Escherichia coli",
    "Enteroinvasive Escherichia coli causes a shigellosis-like disease of the large intestine and has no toxins; no "
    "cattle reservoir is described for it. The O157:H7 type carried by cattle is enterohemorrhagic.",
    "invasive type taken for the cattle-borne type"),
   ("Enteropathogenic Escherichia coli",
    "Enteropathogenic Escherichia coli causes wasting infantile diarrhea and is prevented by breast feeding; no "
    "cattle reservoir is described for it. The type carried in cattle intestines is enterohemorrhagic.",
    "infant type taken for the cattle-borne type")],
  cl(56, 57, 58, 59, 60)),

# ============================================================ 1.9 (cold) O157:H7
Q("1.9", "cold", "A", "O157:H7: what the H7 identifies", 1,
  "In the name Escherichia coli O157:H7, what does the H7 identify?",
  ("Its flagellar antigen type",
   "Correct: the enteric surface antigens are H (flagellar), K (capsule and/or fimbrial) and O (somatic, cell wall). "
   "O157:H7 means O (somatic) type antigen 157 and H (flagellar) type antigen 7; these antigens identify the strain."),
  [("Its cell wall antigen type",
    "The cell wall (somatic) antigen is the O antigen, here type 157, which all enterics have. H7 names the flagellar "
    "antigen type.",
    "confuses the H antigen with the O antigen"),
   ("Its capsule antigen type",
    "The capsule and/or fimbrial antigen is the K antigen, which is not part of the name O157:H7. H7 names the "
    "flagellar antigen type of the strain.",
    "confuses the H antigen with the K antigen"),
   ("Its Shiga toxin type",
    "Shiga toxin is a toxin the strain carries (hence Shiga toxin-producing Escherichia coli), not a letter in the "
    "name. The H in O157:H7 is the flagellar antigen, type 7.",
    "reads the antigen label as a toxin label")],
  cl(52, 53, 59)),

Q("1.9", "cold", "B", "O157:H7: where the 157 antigen sits", 1,
  "In Escherichia coli O157:H7, which part of the cell carries the antigen numbered 157?",
  ("The cell wall (somatic antigen)",
   "Correct: O is the somatic or cell wall antigen, which all enterics have; in O157:H7 it is O type antigen 157. "
   "The H7 is the flagellar antigen, type 7."),
  [("The flagella (H antigen)",
    "The flagella carry the H antigen, which in this strain is type 7, not 157. The 157 is the O (somatic, cell "
    "wall) antigen.",
    "confuses the O antigen with the H antigen"),
   ("The capsule (K antigen)",
    "The capsule and/or fimbriae carry the K antigen, which is not part of the name O157:H7. The 157 is the O "
    "(somatic, cell wall) antigen.",
    "confuses the O antigen with the K antigen"),
   ("The fimbriae (adhesin)",
    "Fimbriae are attachment structures and carry, with the capsule, the K antigen; the strain name does not list "
    "them. The 157 in O157:H7 is the O (somatic, cell wall) antigen.",
    "confuses the O antigen with fimbrial structures")],
  cl(52, 53, 59)),

# ============================================================ 1.10 (cold) Proteus
Q("1.10", "cold", "A", "Proteus: the property behind swarming", 1,
  ("A urine culture from a patient with a urinary tract infection spreads across the agar in the wavelike rings "
   "shown. Which property of the organism produces this growth?"),
  ("It is highly motile",
   "Correct: this wavelike, swarming growth is the diagnostic pattern of Proteus, an agent of urinary tract "
   "infection. Proteus is highly motile, with peritrichous flagella, so it swarms over the plate."),
  [("It ferments lactose",
    "Proteus is a non-coliform, a lactose-NEGATIVE enteric; lactose fermentation is what coliforms such as "
    "Escherichia show on differential media. The swarming comes from its high motility.",
    "confuses the lactose test with motility"),
   ("It has a large capsule",
    "A large capsule marks Klebsiella pneumoniae, a coliform seen on a capsule stain. The wavelike swarming growth "
    "comes from the high motility and peritrichous flagella of Proteus.",
    "adjacent trait from the same lecture (Klebsiella)"),
   ("It makes a soluble pigment",
    "Water-soluble pigments, such as the greenish-blue pyocyanin of Pseudomonas aeruginosa, color the agar; they do "
    "not spread growth in waves. Swarming comes from the high motility of Proteus.",
    "adjacent trait from the same lecture (Pseudomonas)")],
  ci(71, 14, 18, 50, 66, 67, 69, 70),
  img=IMG + "/wr3-fig-02.jpg",
  alt=("A culture plate in which the growth spreads outward from two central spots as overlapping concentric "
       "rings and waves that cover the agar")),

Q("1.10", "cold", "B", "Proteus: recognizing it from a urine culture", 1,
  ("A urine culture from a patient with a urinary tract infection grows a non-lactose-fermenting enteric that is "
   "highly motile, with flagella all around the cell (peritrichous). Which genus is it?"),
  ("Proteus",
   "Correct: Proteus is a non-coliform, lactose-negative enteric opportunist that causes urinary tract infections; "
   "it is highly motile, with peritrichous flagella, and swarms across the agar in waves."),
  [("Escherichia",
    "Escherichia coli causes most urinary tract infections, but it is a coliform, a lactose FERMENTER. A "
    "lactose-negative, highly motile enteric with peritrichous flagella is Proteus.",
    "lactose fermenter taken for a non-fermenter"),
   ("Klebsiella",
    "Klebsiella is a coliform (lactose fermenter) recognized by its large capsule, a cause of nosocomial pneumonia "
    "and urinary tract infection. A lactose-negative, swarming enteric with peritrichous flagella is Proteus.",
    "coliform with a capsule taken for a motile non-coliform"),
   ("Pseudomonas",
    "Pseudomonas does not ferment lactose either and is motile, but it is not an enteric and carries a single polar "
    "flagellum. An enteric with flagella all around the cell (peritrichous) is Proteus.",
    "single polar flagellum confused with peritrichous flagella")],
  cl(14, 50, 65, 66, 69, 70, 71)),

# ============================================================ 1.11 (cold) Salmonella typhi
Q("1.11", "cold", "A", "Typhoid fever: recognizing it", 1,
  ("A patient has a sustained fever of 103-104 degrees, weakness, stomach pains, loss of appetite and a rash of "
   "rose-colored spots. Which organism is the most likely cause?"),
  ("Salmonella typhi",
   "Correct: Salmonella typhi causes typhoid fever. The bacilli adhere to the small intestine and cause an invasive "
   "diarrhea that leads to septicemia, with a sustained fever of 103-104 degrees, rose-colored spots, weakness, "
   "stomach pains and loss of appetite."),
  [("Brucella abortus",
    "Brucella abortus causes brucellosis, whose fever FLUCTUATES for weeks to a year (undulant fever), caught from "
    "infected animals or unpasteurized dairy. A sustained fever with rose-colored spots is typhoid fever.",
    "fluctuating fever confused with a sustained one"),
   ("Shigella dysenteriae",
    "Shigella dysenteriae causes bacillary dysentery with cramps and bloody stool; it invades the large intestine "
    "but does not invade the blood. A sustained high fever with rose-colored spots is typhoid fever.",
    "competing invasive enteric that stays in the bowel"),
   ("Francisella tularensis",
    "Francisella tularensis causes tularemia (rabbit fever), with fever, ulcerative skin lesions and swollen lymph "
    "nodes after contact with infected animals. Rose-colored spots with a sustained fever mark typhoid fever.",
    "competing febrile illness with a different skin finding")],
  cl(27, 28, 29, 73, 74, 78)),

Q("1.11", "cold", "B", "Typhoid fever: the healthy carrier", 2,
  ("A cook who has never been ill is traced as the source of several cases of a severe febrile illness. She is a "
   "chronic carrier who sheds the bacilli from her gallbladder. Which organism does she carry?"),
  ("Salmonella typhi",
   "Correct: Salmonella typhi has humans as its exclusive hosts and is spread by fecally contaminated food or water. "
   "Some people become asymptomatic carriers, and some chronic carriers shed the bacilli from the gallbladder."),
  [("Shigella dysenteriae",
    "Shigella dysenteriae is also spread by fecally contaminated food, but it causes dysentery by invading the large "
    "intestine and is not described with gallbladder carriage. Chronic gallbladder carriers shed Salmonella typhi.",
    "competing foodborne enteric pathogen"),
   ("Enterohemorrhagic Escherichia coli",
    "Enterohemorrhagic Escherichia coli has its reservoir in the intestines of cattle and spreads in contaminated "
    "beef, water and vegetables, not from human gallbladder carriers. That carrier state belongs to Salmonella typhi.",
    "animal reservoir confused with a human carrier"),
   ("Yersinia enterocolitica",
    "Yersinia enterocolitica comes from domestic and wild animals, fish, fruits, vegetables and water, and can mimic "
    "appendicitis. Shedding from the gallbladder of a healthy human carrier is Salmonella typhi.",
    "environmental and animal source confused with a human carrier")],
  cl(60, 73, 78, 80)),

# ============================================================ 1.12 (it) other salmonelloses
Q("1.12", "it", "A", "Salmonella gastroenteritis from a pet turtle", 2,
  ("A child who keeps a small pet turtle develops vomiting, diarrhea and fluid loss. Which organism is the most "
   "likely cause?"),
  ("Salmonella enteritidis",
   "Correct: the salmonelloses other than typhoid fever, such as Salmonella enteritidis, are zoonotic in origin and "
   "are acquired by ingestion from cattle, poultry, eggs, rodents and reptiles (pet turtles). Gastroenteritis brings "
   "vomiting, diarrhea and fluid loss."),
  [("Salmonella typhi",
    "Salmonella typhi causes typhoid fever, and humans are its exclusive hosts, so a pet reptile is not its source. "
    "Gastroenteritis after contact with a pet turtle is an animal salmonellosis such as Salmonella enteritidis.",
    "confuses the human-only typhoid organism with the zoonotic salmonellae"),
   ("Shigella sonnei",
    "Shigella sonnei causes shigellosis, transmitted by ingestion of fecally contaminated food, with cramps and "
    "bloody stool; reptiles are not its source. A pet turtle points to an animal salmonellosis.",
    "competing enteric pathogen without the reptile link"),
   ("Francisella tularensis",
    "Francisella tularensis is caught by contact with infected mammals, particularly rabbits, and gives skin ulcers "
    "and swollen lymph nodes, and is caught from mammals such as rabbits, not from pet reptiles. A pet turtle and "
    "vomiting point to an animal salmonellosis.",
    "animal contact taken as any zoonosis")],
  cl(29, 73, 76, 77, 78)),

Q("1.12", "it", "B", "Salmonella gastroenteritis: how it is acquired", 2,
  ("A child who helps care for the family's backyard chickens develops Salmonella gastroenteritis. By which route "
   "did the bacteria most likely reach the child?"),
  ("By ingestion",
   "Correct: animal salmonelloses are acquired by ingestion, from cattle, poultry, eggs, rodents, reptiles, animal "
   "and dairy products, and fomites contaminated with animal intestinal flora; backyard flocks are an animal-borne "
   "source."),
  [("By inhaling aerosols",
    "Inhaled aerosols transmit Legionella (from water sources) and Bordetella pertussis. Salmonella from backyard "
    "chickens is acquired by ingestion, for example from contaminated fomites or eggs.",
    "adjacent transmission route from the same lecture (Legionella, pertussis)"),
   ("By the bite of a flea",
    "Flea bites transmit Yersinia pestis, the plague organism, from rodents. Salmonella from backyard chickens is "
    "acquired by ingestion, for example from fomites contaminated with animal intestinal flora.",
    "adjacent transmission route from the same lecture (plague)"),
   ("Through damaged skin",
    "Entry through damaged skin or mucous membranes is how Brucella starts brucellosis. Salmonella gastroenteritis "
    "from backyard chickens is acquired by ingestion.",
    "adjacent transmission route from the same lecture (Brucella)")],
  cl(28, 30, 40, 76, 77, 83)),

# ============================================================ 1.13 (it) Shigella
Q("1.13", "it", "A", "Shigella: recognizing bacillary dysentery", 1,
  ("A child has abdominal cramps and watery stool with blood. The isolate is a non-lactose-fermenting enteric that "
   "invades the villus of the large intestine but does not invade the blood. Which genus is it?"),
  ("Shigella",
   "Correct: Shigella causes shigellosis (bacillary dysentery), with abdominal cramps and watery stool with blood. "
   "It invades the villus of the large intestine and enters Peyer's patches, but does not perforate the intestine or "
   "invade the blood."),
  [("Salmonella",
    "Salmonella typhi is also a non-lactose-fermenting true pathogen, but its invasive diarrhea, from the small "
    "intestine, leads to septicemia. An enteric that invades the large intestine but not the blood is Shigella.",
    "competing invasive non-coliform that does reach the blood"),
   ("Proteus",
    "Proteus is a non-lactose-fermenting opportunist known for urinary tract infections and swarming growth, not "
    "for invasive bloody dysentery. Invasion of the large intestinal villus is Shigella.",
    "competing non-coliform with a different disease"),
   ("Yersinia",
    "Yersinia enterocolitica enters the SMALL intestinal mucosa and lymphatics, and inflammation of the ileum can "
    "mimic appendicitis. Bloody dysentery from invasion of the large intestinal villus is Shigella.",
    "confuses small-intestine invasion with large-intestine invasion")],
  cl(69, 70, 74, 78, 80)),

Q("1.13", "it", "B", "Shigella: what causes the fever", 1,
  "In shigellosis, which bacterial product initiates the fever?",
  ("Endotoxin",
   "Correct: in shigellosis, endotoxin initiates the fever, while the enterotoxin damages the mucosa and villi, "
   "causing bleeding and mucus secretion as Shigella invades the villus of the large intestine."),
  [("Enterotoxin",
    "The Shigella enterotoxin damages the mucosa and villi, causing bleeding and mucus secretion, not the fever. "
    "The fever is initiated by endotoxin.",
    "swaps the roles of the two Shigella products"),
   ("Heat-labile toxin",
    "Heat-labile toxin, with heat-stable toxin, is the enterotoxigenic Escherichia coli toxin that drives fluid "
    "secretion with low-grade or no fever. In shigellosis, endotoxin initiates the fever.",
    "adjacent toxin from the same lecture (enterotoxigenic Escherichia coli)"),
   ("Exotoxin A",
    "Exotoxin A is the Pseudomonas aeruginosa toxin that inhibits protein synthesis. In shigellosis, endotoxin "
    "initiates the fever and the enterotoxin damages the mucosa and villi.",
    "adjacent toxin from the same lecture (Pseudomonas)")],
  cl(17, 56, 78)),

# ============================================================ 1.14 (cold) Yersinia pestis
Q("1.14", "cold", "A", "Plague: recognizing the bubonic form", 2,
  ("A camper in the western United States is bitten by fleas after handling a dead wild rodent. Days later he has "
   "fever and a swollen, necrotic lymph node in the groin. Which organism is the most likely cause?"),
  ("Yersinia pestis",
   "Correct: Yersinia pestis lives in rodents and is carried by flea vectors; in bubonic plague the bacillus "
   "multiplies in the flea bite, enters the lymph and causes necrosis and swelling called a bubo, in the groin or "
   "axilla. United States cases occur west of the Mississippi."),
  [("Yersinia enterocolitica",
    "Yersinia enterocolitica is an enteric Yersinia caught from animals, fish, produce and water; it enters the "
    "small intestinal mucosa and can mimic appendicitis. Flea bites and a groin bubo point to Yersinia pestis.",
    "confuses the enteric Yersinia with the nonenteric plague organism"),
   ("Brucella suis",
    "Brucella suis is the pig species of brucellosis, caught by animal handling or unpasteurized dairy, with an "
    "undulant fever. A flea bite followed by a necrotic groin lymph node is bubonic plague.",
    "competing zoonosis without a flea vector"),
   ("Pseudomonas aeruginosa",
    "Pseudomonas aeruginosa is a soil and water opportunist that infects burns, wounds and hosts with cystic "
    "fibrosis; it has no flea vector. A bubo after flea bites points to Yersinia pestis.",
    "opportunist taken for a vector-borne zoonosis")],
  cl(16, 18, 27, 80, 83, 88)),

Q("1.14", "cold", "B", "Plague: the animal reservoir", 2,
  "In which animals is Yersinia pestis found, without causing them disease, before fleas carry it to humans?",
  ("Rodents",
   "Correct: Yersinia pestis is found in 200 species of mammals, rodents, without causing disease; flea "
   "vectors acquire it, and their regurgitated material transmits the bacterium to new hosts."),
  [("Cattle",
    "The intestines of cattle are the reservoir of enterohemorrhagic Escherichia coli O157:H7, and cattle carry "
    "Brucella abortus. The plague organism is carried by rodents and spread by fleas.",
    "adjacent reservoir from the same lecture (O157:H7, Brucella)"),
   ("Pet turtles",
    "Reptiles such as pet turtles carry the animal salmonelloses, acquired by ingestion. Yersinia pestis is found "
    "in rodents without causing disease and is transmitted by fleas.",
    "adjacent reservoir from the same lecture (salmonellosis)"),
   ("Wild rabbits",
    "Rabbits are the classic source of tularemia (rabbit fever) from Francisella tularensis. Yersinia pestis is "
    "found in rodents without causing disease and reaches humans through flea vectors.",
    "adjacent reservoir from the same lecture (tularemia)")],
  cl(27, 29, 60, 76, 83)),

Q("1.14", "cold", "B", "Plague: the septicemic form", 1,
  ("A patient with plague develops intravascular coagulation, with subcutaneous hemorrhage and purpura that "
   "degenerate into necrosis and gangrene. Which form of plague is this?"),
  ("Septicemic plague",
   "Correct: septicemic plague is progression to massive bacterial growth; the virulence factors cause intravascular "
   "coagulation, subcutaneous hemorrhage and purpura that degenerate into necrosis and gangrene."),
  [("Bubonic plague",
    "In bubonic plague the bacillus multiplies in the flea bite and enters the lymph, causing a necrotic, swollen "
    "lymph node, the bubo, in the groin or axilla. Purpura that turns to gangrene is septicemic plague.",
    "confuses the localized lymph-node form with the blood-borne form"),
   ("Pneumonic plague",
    "Pneumonic plague is infection localized to the lungs, highly contagious by aerosol and fatal without treatment. "
    "Intravascular coagulation with purpura and gangrene is septicemic plague.",
    "confuses the lung form with the blood-borne form"),
   ("Sylvatic plague",
    "Sylvatic plague names the SOURCE (contact with wild animals), as urban plague names domestic animals; it is not "
    "a clinical form. Purpura degenerating into gangrene is septicemic plague.",
    "confuses a source category with a clinical form")],
  cl(83, 88)),

# ============================================================ 1.15 (cold) Haemophilus
Q("1.15", "cold", "A", "Haemophilus influenzae: recognizing meningitis", 1,
  ("A child has fever, vomiting and a stiff neck. Spinal fluid grows tiny, pleomorphic Gram-negative rods that grow "
   "only on chocolate agar. A subunit vaccine prevents this infection. Which organism is it?"),
  ("Haemophilus influenzae",
   "Correct: Haemophilus are tiny pleomorphic Gram-negative rods that need chocolate agar (cooked blood). "
   "Haemophilus influenzae causes acute bacterial meningitis (fever, vomiting, stiff neck, neurological impairment) "
   "and is prevented by the Hib (Haemophilus influenzae type b) subunit vaccine."),
  [("Haemophilus ducreyi",
    "Haemophilus ducreyi also needs chocolate agar, but it causes chancroid, a sexually transmitted disease seen "
    "mainly in the tropics and in males. A child with meningitis and a subunit vaccine is Haemophilus influenzae.",
    "same genus, different disease (chancroid)"),
   ("Haemophilus aegyptius",
    "Haemophilus aegyptius causes conjunctivitis (pink eye), mainly in children, spread by contaminated fingers and "
    "insects. Childhood meningitis prevented by a subunit vaccine is Haemophilus influenzae.",
    "same genus, different disease (pink eye)"),
   ("Pasteurella multocida",
    "Pasteurella multocida is an oxidase-positive zoonotic rod caught from animal bites or scratches, causing local "
    "abscesses. Meningitis from chocolate-agar rods prevented by a subunit vaccine is Haemophilus influenzae.",
    "adjacent oxidase-positive organism from the same lecture")],
  cl(95, 96, 97, 98, 100)),

Q("1.15", "cold", "B", "Haemophilus influenzae: the diseases it does cause", 1,
  "Which illness is caused by Haemophilus influenzae?",
  ("Epiglottitis",
   "Correct: Haemophilus influenzae causes acute bacterial meningitis, epiglottitis, otitis media, sinusitis, "
   "pneumonia and bronchitis. Despite its name, it was misnamed as the causative agent of flu."),
  [("Influenza",
    "Haemophilus influenzae was misnamed as the causative agent of flu; it does not cause influenza. It causes "
    "meningitis, epiglottitis, otitis media, sinusitis, pneumonia and bronchitis.",
    "takes the misleading name literally"),
   ("Chancroid",
    "Chancroid, a sexually transmitted disease mainly of the tropics, is caused by Haemophilus ducreyi. Haemophilus "
    "influenzae causes meningitis, epiglottitis, otitis media, sinusitis, pneumonia and bronchitis.",
    "same genus, different species (Haemophilus ducreyi)"),
   ("Pink eye",
    "Conjunctivitis (pink eye), mainly in children, is caused by Haemophilus aegyptius. Haemophilus influenzae "
    "causes meningitis, epiglottitis, otitis media, sinusitis, pneumonia and bronchitis.",
    "same genus, different species (Haemophilus aegyptius)")],
  cl(98, 100)),

# ============================================================ 1.16 (cold) endotoxin
Q("1.16", "cold", "A", "Endotoxin: the effect of a low level", 1,
  "What does a LOW level of Gram-negative endotoxin in the body typically produce?",
  ("Fever, malaise, aches and pains",
   "Correct: low levels of endotoxin cause a low-level inflammatory response with generalized symptoms of fever, "
   "malaise, aches and pains. Only a large flood of endotoxin releases enough mediators to contribute to septic "
   "shock."),
  [("Septic shock and organ failure",
    "Septic shock, with microthrombi, falling blood pressure, tissue hypoxia and multisystem organ failure, follows "
    "a LARGE flood of endotoxin. A low level gives fever, malaise, aches and pains.",
    "reverses the dose: flood effect given to a low level"),
   ("Bloody, invasive diarrhea",
    "Bloody diarrhea comes from bacteria invading the intestinal mucosa, as in Shigella, not from a general "
    "endotoxin effect. A low level of endotoxin gives fever, malaise, aches and pains.",
    "local bowel invasion confused with a general endotoxin effect"),
   ("Hemolytic uremic syndrome",
    "Hemolytic uremic syndrome is a complication of enterohemorrhagic Escherichia coli, whose toxins damage renal "
    "tubular cells and trigger coagulation. A low level of endotoxin gives fever, malaise, aches and pains.",
    "adjacent complication from the same lecture (O157:H7)")],
  cl(11, 44, 59, 60)),

Q("1.16", "cold", "A", "Endotoxin: what it is", 1,
  ("All the Gram-negative bacilli use endotoxin as an offensive weapon. What is endotoxin, chemically and "
   "structurally?"),
  ("Outer-membrane lipopolysaccharide",
   "Correct: endotoxin is a structural component of the Gram-negative outer membrane; chemically it is a "
   "lipopolysaccharide, with lipid A as its biologically active component. It is released when the cells lyse "
   "(including through antibiotic therapy) and as they grow and divide."),
  [("A protein secreted by the cell",
    "A secreted protein toxin describes exotoxins, such as exotoxin A of Pseudomonas aeruginosa. Endotoxin is not "
    "secreted; it is the lipopolysaccharide built into the outer membrane.",
    "confuses endotoxin with an exotoxin"),
   ("A polysaccharide capsule",
    "A capsule is a separate surface layer and virulence factor (the K antigen, large in Klebsiella pneumoniae). "
    "Endotoxin is the lipopolysaccharide of the outer membrane, active through lipid A.",
    "confuses the outer membrane with the capsule"),
   ("A flagellar protein antigen",
    "Flagellar proteins carry the H antigen used to type enterics such as O157:H7. Endotoxin is the "
    "lipopolysaccharide of the outer membrane, whose O antigen polysaccharide is the somatic antigen.",
    "confuses the H antigen with the lipopolysaccharide")],
  cl(5, 6, 13, 17, 52, 66, 67)),

Q("1.16", "cold", "B", "Endotoxin: the effect of a large flood", 1,
  "What can a large flood of Gram-negative endotoxin into the circulation lead to?",
  ("Septic shock",
   "Correct: a large flood of endotoxin releases mediators (tumor necrosis factor, interleukin 1) that contribute to "
   "septic shock: microthrombi, dilated arterioles, then falling cardiac output and blood pressure, tissue hypoxia "
   "and multisystem organ failure."),
  [("Only fever and malaise",
    "Fever, malaise, aches and pains are the generalized symptoms of LOW levels of endotoxin. A large flood releases "
    "mediators that contribute to septic shock.",
    "reverses the dose: low-level effect given to a flood"),
   ("A protective inflammation",
    "A moderated, protective inflammatory response is what mucosal contact with lipopolysaccharide produces under "
    "most circumstances. A large flood of endotoxin contributes to septic shock.",
    "mucosal response taken for the systemic flood response"),
   ("Coughing fits and a whoop",
    "Paroxysms of coughing followed by a whoop are the paroxysmal stage of pertussis, from loss of the ciliary "
    "mechanism in the airway. A large flood of endotoxin contributes to septic shock.",
    "adjacent clinical picture from the same lecture (pertussis)")],
  cl(7, 11, 31)),

]
