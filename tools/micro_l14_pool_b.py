# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 14 — Gram-Negative Bacilli of Medical Importance (Dr. Webster), pool B: the
# ENTERICS (Enterobacteriaceae, deck slides 43-80: the family, media and antigens, Escherichia coli and its four
# pathotypes, the other coliforms, Proteus and its relatives, Salmonella, Shigella, the enteric yersinias), then
# Yersinia pestis and plague (slides 81-94), Pasteurella and Haemophilus (slides 95-101).
#
# Same rules, helpers and held points as pool A (tools/micro_l14_pool_a.py): written from the visible slides,
# four options, key at position 0 with the only "Correct:" opener, `mis` per distractor, no percentage, case
# count or dose keyed, no "which antibiotic" key.
from micro_l14_pool_a import SRC, c, ci, IO1, IO2, IMG, Q

POOL_B = [

# ============================================================== ENTERIC FEATURES (slides 43-53, 69)
Q("Enteric features", IO1,
  "Which traits do ALL members of the Enterobacteriaceae share?",
  ("Ferment glucose, oxidase negative",
   "Correct: all enterics ferment glucose, reduce nitrates to nitrites, are oxidase negative and catalase positive; "
   "they are facultative anaerobes that grow best in air."),
  [("Ferment lactose, oxidase positive",
    "Lactose fermentation splits the coliforms from the non-coliforms, so not all enterics ferment it, and enterics "
    "are oxidase negative.", "dividing trait taken for a shared one"),
   ("Obligate aerobes, oxidase positive",
    "Obligate aerobes with oxidase describe Pseudomonas and its relatives; enterics are facultative anaerobes and "
    "oxidase negative.", "adjacent fact from the same lecture (Pseudomonas)"),
   ("Catalase negative, spore-forming",
    "Enterics are catalase positive and non-spore-forming small rods; all of them ferment glucose and are oxidase "
    "negative.", "reversed traits")],
  c(46, 43, 14)),

Q("Enteric features", IO1,
  "What divides the Enterobacteriaceae into coliforms and non-coliforms?",
  ("Lactose fermentation",
   "Correct: the enterics are divided into coliforms, the lactose fermenters, and non-coliforms, the non-lactose "
   "fermenters."),
  [("Oxidase activity",
    "All enterics are oxidase negative, so oxidase does not divide them; lactose fermentation does.",
    "shared trait taken for a dividing one"),
   ("Glucose fermentation",
    "All enterics ferment glucose, so it cannot divide them; coliforms are the lactose fermenters.",
    "shared trait taken for a dividing one"),
   ("Nitrate reduction",
    "All enterics reduce nitrates to nitrites; the coliform split rests on lactose fermentation.",
    "shared trait taken for a dividing one")],
  c(46)),

Q("Enteric features", IO1,
  "What makes MacConkey's agar selective for Gram-negative bacteria?",
  ("Crystal violet and bile salts",
   "Correct: MacConkey's agar selects for Gram-negative bacteria with crystal violet and bile salts and is "
   "differential for lactose fermenters."),
  [("Eosin and methylene blue",
    "Eosin and methylene blue are the selective dyes of eosin methylene blue agar; MacConkey's agar uses crystal "
    "violet and bile salts.", "the other isolation medium"),
   ("Charcoal and yeast extract",
    "Charcoal yeast extract agar is the medium for growing Legionella; MacConkey's agar selects with crystal violet "
    "and bile salts.", "adjacent fact from the same lecture (Legionella)"),
   ("Heated, cooked blood cells",
    "Cooked blood is chocolate agar, the enriched medium Haemophilus needs; MacConkey's agar selects with crystal "
    "violet and bile salts.", "adjacent fact from the same lecture (Haemophilus)")],
  c(48, 41, 97)),

Q("Enteric features", IO1,
  "What does eosin methylene blue agar DIFFERENTIATE among enterics?",
  ("Lactose fermenters from others",
   "Correct: eosin methylene blue agar is selective for Gram-negative bacteria and differential for lactose "
   "fermenters."),
  [("Gram-positives from Gram-negatives",
    "Eosin methylene blue agar SELECTS for Gram-negative bacteria rather than telling the two apart; what it "
    "differentiates is lactose fermentation.", "selective function confused with differential"),
   ("Oxidase positives from negatives",
    "All enterics are oxidase negative, and the medium does not test oxidase; it differentiates lactose "
    "fermenters.", "wrong biochemical test"),
   ("Motile rods from nonmotile rods",
    "Motility is a separate test in the biochemical tree; eosin methylene blue agar differentiates lactose "
    "fermenters.", "wrong biochemical test")],
  ci(47, 48, 46)),

Q("Enteric features", IO1,
  "Which surface antigen of the enterics is carried on their flagella?",
  ("The H antigen",
   "Correct: H is the flagellar antigen; K is the capsule and/or fimbrial antigen, and O the somatic (cell wall) "
   "antigen that all enterics have."),
  [("The O antigen",
    "O is the somatic, cell wall antigen, which all enterics have; the flagellar antigen is H.",
    "somatic antigen confused with the flagellar one"),
   ("The K antigen",
    "K is the capsule and/or fimbrial antigen; the flagellar antigen is H.",
    "capsular antigen confused with the flagellar one"),
   ("The Vi antigen",
    "Vi is the capsular antigen of Salmonella, its form of the K antigen; the flagellar antigen is H.",
    "capsular antigen confused with the flagellar one")],
  ci(53, 52)),

Q("Enteric features", IO1,
  "Which surface antigen do ALL the enterics have?",
  ("The O (somatic) antigen",
   "Correct: O is the somatic or cell wall antigen, and all enterics have it; H (flagellar) and K (capsule and/or "
   "fimbrial) antigens vary."),
  [("The H (flagellar) antigen",
    "H is the flagellar antigen, and not every enteric is motile; the antigen all of them have is O, the somatic "
    "antigen.", "variable antigen taken for a universal one"),
   ("The K (capsule) antigen",
    "K is the capsule and/or fimbrial antigen, present only where there is a capsule or fimbriae; all enterics have "
    "the O antigen.", "variable antigen taken for a universal one"),
   ("The Vi antigen",
    "Vi is the capsular antigen of Salmonella alone; the antigen all enterics have is O.",
    "one genus's antigen generalized")],
  ci(53, 47, 52)),

Q("Enteric features", IO1,
  "In toxigenic diarrheal disease, what do the bacteria cause at the intestinal epithelium?",
  ("Oversecretion of fluid",
   "Correct: in toxigenic disease (example: enterotoxigenic Escherichia coli) bacteria on the epithelium cause an "
   "oversecretion of fluids; in invasive disease (example: Shigella) they enter the tissue and cause bleeding."),
  [("Invasion with bleeding",
    "Invasion of the tissue with bleeding is the invasive pattern, as in Shigella; toxigenic disease causes an "
    "oversecretion of fluid.", "the other diarrheal pattern"),
   ("Perforation of the wall",
    "Ulcers and perforations of the intestinal wall are a typhoid feature; toxigenic disease causes an "
    "oversecretion of fluid.", "adjacent fact from the same lecture (typhoid)"),
   ("Destruction of microvilli",
    "Destroying the microvilli is how enteropathogenic Escherichia coli damages the lining; toxigenic disease "
    "causes an oversecretion of fluid.", "adjacent fact from the same lecture (EPEC)")],
  ci(44, 43, 58, 74)),

Q("Enteric features", IO1,
  "The diagram shows enteric bacteria invading the intestinal epithelium, with bleeding. Which organism is the "
  "example of this invasive diarrheal disease?",
  ("Shigella dysenteriae",
   "Correct: invasive diarrheal disease, with bacteria entering the epithelium and causing bleeding, is "
   "exemplified by Shigella; the toxigenic pattern, an oversecretion of fluid, by enterotoxigenic Escherichia coli."),
  [("Enterotoxigenic Escherichia coli",
    "Enterotoxigenic Escherichia coli is the example of TOXIGENIC disease, an oversecretion of fluid without "
    "invasion; the invasive example is Shigella.", "the other diarrheal pattern"),
   ("Klebsiella pneumoniae",
    "Klebsiella pneumoniae is a respiratory-tract coliform causing nosocomial pneumonia and urinary tract "
    "infection, not invasive diarrhea; that pattern is Shigella's.", "wrong organism (respiratory coliform)"),
   ("Proteus vulgaris",
    "Proteus vulgaris is an opportunist of urinary tract and wound infections, known for swarming; the invasive "
    "diarrhea example is Shigella.", "wrong organism (opportunist)")],
  ci(44, 66, 70, 71, 78),
  img=IMG + "/l14-fig-02.jpg",
  alt="Drawing of intestinal epithelium in which rod-shaped bacteria have entered the lining, with red blood "
      "spilling out.",
  slide="Slide 44"),

Q("Enteric features", IO1,
  "Which enteric is a true pathogen rather than a member of the normal flora?",
  ("Salmonella typhi",
   "Correct: Salmonella typhi is one of the true pathogenic enterics, with the shigellas and the enteric yersinias; "
   "Klebsiella, Enterobacter and Proteus belong to the normal flora."),
  [("Klebsiella pneumoniae",
    "Klebsiella is a coliform of the normal flora (a normal inhabitant of the respiratory tract), important mainly as "
    "an opportunist; Salmonella typhi is a true pathogen.", "normal flora taken for a true pathogen"),
   ("Enterobacter species",
    "Enterobacter is a coliform of the normal flora, an opportunist; the true pathogen among these is Salmonella "
    "typhi.", "normal flora taken for a true pathogen"),
   ("Proteus vulgaris",
    "Proteus is a non-coliform of the normal flora, an opportunistic pathogen; the true pathogen among these is "
    "Salmonella typhi.", "normal flora taken for a true pathogen")],
  c(51, 50, 66, 69)),

Q("Enteric features", IO1,
  "Which non-lactose-fermenting enterics are TRUE pathogens, with true virulence factors, rather than opportunists?",
  ("Salmonella and Shigella",
   "Correct: among the noncoliform, lactose-negative enterics, Proteus, Morganella and Providencia are "
   "opportunists, while Salmonella and Shigella are true pathogens with true virulence factors, not normal flora."),
  [("Proteus and Morganella",
    "Proteus and Morganella are the opportunistic noncoliforms, ordinarily harmless; the true pathogens are "
    "Salmonella and Shigella.", "opportunists taken for true pathogens"),
   ("Providencia and Proteus",
    "Providencia and Proteus are opportunists of the normal flora; the true pathogens among the noncoliforms are "
    "Salmonella and Shigella.", "opportunists taken for true pathogens"),
   ("Klebsiella and Enterobacter",
    "Klebsiella and Enterobacter are coliforms, lactose fermenters and opportunists; the true noncoliform pathogens "
    "are Salmonella and Shigella.", "coliforms taken for noncoliforms")],
  c(69, 66, 70)),

# ============================================================== ESCHERICHIA COLI, GENERAL (slides 55, 65)
Q("Escherichia coli", IO1,
  "Which bacteria are actually more prevalent in the gut than Escherichia coli?",
  ("Bacteroides and Bifidobacterium",
   "Correct: Escherichia coli is the common aerobic, non-fastidious gut bacterium, but it is not the most "
   "prevalent; the anaerobic Bacteroides and Bifidobacterium are."),
  [("Klebsiella and Enterobacter",
    "Klebsiella and Enterobacter are other coliforms of the normal flora; the gut bacteria more prevalent than "
    "Escherichia coli are the anaerobes Bacteroides and Bifidobacterium.", "other coliforms"),
   ("Proteus and Providencia",
    "Proteus and Providencia are noncoliform opportunists; the bacteria more prevalent than Escherichia coli are "
    "the anaerobes Bacteroides and Bifidobacterium.", "noncoliform opportunists"),
   ("Salmonella and Shigella",
    "Salmonella and Shigella are true pathogens, not normal flora; the gut's more prevalent anaerobes are "
    "Bacteroides and Bifidobacterium.", "true pathogens taken for normal flora")],
  c(55, 50, 51, 69)),

Q("Escherichia coli", IO1,
  "How have some Escherichia coli strains developed virulence?",
  ("Through plasmid transfer",
   "Correct: of about 150 strains, some have developed virulence through plasmid transfer, while others are "
   "opportunists."),
  [("Through spore formation",
    "Escherichia coli, like all enterics, is non-spore-forming; virulent strains acquired it through plasmid "
    "transfer.", "spore biology borrowed from the Gram-positive bacilli"),
   ("By shedding their O antigen",
    "All enterics carry the O (somatic) antigen; virulence in Escherichia coli strains came through plasmid "
    "transfer.", "universal antigen taken as lost"),
   ("By living inside amebas",
    "Living in close association with amebas is the Legionella story; virulent Escherichia coli strains acquired "
    "virulence by plasmid transfer.", "adjacent fact from the same lecture (Legionella)")],
  c(55, 43, 52, 39)),

Q("Escherichia coli", IO2,
  "In water testing, what does a coliform count indicate?",
  ("Fecal contamination",
   "Correct: the coliform count, with Escherichia coli the classic coliform, is the indicator of fecal "
   "contamination in water."),
  [("Legionella in the water",
    "Legionella in water systems is found by culturing it on charcoal yeast extract agar; a coliform count "
    "indicates fecal contamination.", "adjacent fact from the same lecture (Legionella)"),
   ("Biofilms on the pipes",
    "Biofilms are how Pseudomonas and Stenotrophomonas persist on equipment; a coliform count indicates fecal "
    "contamination.", "adjacent fact from the same lecture (biofilms)"),
   ("Tropical soil runoff",
    "Tropical soil and water carry Burkholderia pseudomallei; a coliform count indicates fecal contamination in "
    "water.", "adjacent fact from the same lecture (Burkholderia)")],
  c(65, 17, 23, 26, 41)),

Q("Escherichia coli", IO1,
  "Which extraintestinal infection does Escherichia coli cause most often, more frequently in women?",
  ("Urinary tract infection",
   "Correct: Escherichia coli causes most urinary tract infections, more frequently in women and in catheterized "
   "patients; it also causes neonatal meningitis, pneumonia, septicemia and wound infections."),
  [("Infective endocarditis",
    "Infective endocarditis after dental procedures is caused by Haemophilus parainfluenzae and Haemophilus "
    "aphrophilus; Escherichia coli most often causes urinary tract infection.", "adjacent fact from the same lecture (Haemophilus)"),
   ("Acute conjunctivitis",
    "Acute conjunctivitis (pink eye) is Haemophilus aegyptius, mainly in children; Escherichia coli most often "
    "causes urinary tract infection.", "adjacent fact from the same lecture (Haemophilus)"),
   ("Swimmer's ear infection",
    "Swimmer's ear (otitis externa) is a Pseudomonas aeruginosa infection; Escherichia coli most often causes "
    "urinary tract infection.", "adjacent fact from the same lecture (Pseudomonas)")],
  c(65, 19, 100)),

# ============================================================== ENTEROTOXIGENIC E. COLI (slide 56)
Q("ETEC", IO1,
  "Which pair of toxins does enterotoxigenic Escherichia coli produce?",
  ("Heat-labile and heat-stable",
   "Correct: enterotoxigenic Escherichia coli makes a heat-labile toxin and a heat-stable toxin, which promote "
   "secretion of fluid and electrolytes by the intestinal epithelium."),
  [("Shiga toxin and endotoxin",
    "Shiga toxin is carried by enterohemorrhagic Escherichia coli O157:H7 (from Shigella); the enterotoxigenic "
    "strain makes heat-labile and heat-stable toxins.", "adjacent fact from the same lecture (EHEC)"),
   ("Exotoxin A and exoenzyme S",
    "Exotoxin A and exoenzyme S are Pseudomonas aeruginosa virulence factors; enterotoxigenic Escherichia coli "
    "makes heat-labile and heat-stable toxins.", "adjacent fact from the same lecture (Pseudomonas)"),
   ("Coagulase and murine toxin",
    "Coagulase and murine toxin are Yersinia pestis virulence factors; enterotoxigenic Escherichia coli makes "
    "heat-labile and heat-stable toxins.", "adjacent fact from the same lecture (Yersinia pestis)")],
  c(56, 17, 59, 81)),

Q("ETEC", IO1,
  "How do the toxins of enterotoxigenic Escherichia coli cause diarrhea?",
  ("Fluid and electrolyte secretion",
   "Correct: the heat-labile and heat-stable toxins promote secretion of fluid and electrolytes in the intestinal "
   "epithelium, giving diarrhea, cramping and a low-grade to no fever."),
  [("Mechanical damage of the wall",
    "Mechanical cell damage without toxins is how enteroinvasive Escherichia coli harms the wall; the "
    "enterotoxigenic toxins drive fluid and electrolyte secretion.", "adjacent pathotype (EIEC)"),
   ("Destruction of microvilli",
    "Destroying the microvilli is the enteropathogenic Escherichia coli mechanism; the enterotoxigenic toxins drive "
    "fluid and electrolyte secretion.", "adjacent pathotype (EPEC)"),
   ("Apoptosis of renal tubule cells",
    "Apoptosis of renal tubular epithelial cells is the hemolytic uremic syndrome of enterohemorrhagic Escherichia "
    "coli; the enterotoxigenic toxins drive fluid secretion.", "adjacent pathotype (EHEC)")],
  c(56, 57, 58, 60)),

Q("ETEC", IO1,
  "Enterotoxigenic Escherichia coli is the leading cause of which illness?",
  ("Traveler's diarrhea",
   "Correct: enterotoxigenic Escherichia coli accounts for most cases of traveler's diarrhea: watery diarrhea, "
   "cramping and a low-grade to no fever."),
  [("Wasting infantile diarrhea",
    "The wasting form of infantile diarrhea is caused by enteropathogenic Escherichia coli; the enterotoxigenic "
    "strain causes traveler's diarrhea.", "adjacent pathotype (EPEC)"),
   ("Hemolytic uremic syndrome",
    "Hemolytic uremic syndrome is the kidney complication of enterohemorrhagic Escherichia coli O157:H7; the "
    "enterotoxigenic strain causes traveler's diarrhea.", "adjacent pathotype (EHEC)"),
   ("Bacillary dysentery",
    "Bacillary dysentery is shigellosis, an invasive disease of the large intestine; the enterotoxigenic strain "
    "causes traveler's diarrhea.", "adjacent fact from the same lecture (Shigella)")],
  c(56, 58, 60, 78)),

Q("ETEC", IO1,
  "In enterotoxigenic Escherichia coli diarrhea, what does bismuth salicylate do?",
  ("Counteracts the enterotoxin",
   "Correct: bismuth salicylate counteracts the enterotoxin and serves as an antimicrobial; kaolin or Lomotil slow "
   "gut motility, and fluid and electrolyte therapy replaces the losses."),
  [("Slows gut motility",
    "Slowing gut motility is the role of kaolin or Lomotil; bismuth salicylate counteracts the enterotoxin.",
    "other treatment's role"),
   ("Replaces lost fluid",
    "Replacing losses is fluid and electrolyte therapy; bismuth salicylate counteracts the enterotoxin and acts as "
    "an antimicrobial.", "other treatment's role"),
   ("Prevents fimbrial adhesion",
    "The fimbriae attach the bacteria to the small intestine, but bismuth salicylate is described as counteracting "
    "the enterotoxin.", "virulence factor confused with the drug target")],
  c(56)),

Q("ETEC", IO1,
  "What do the fimbriae of enterotoxigenic Escherichia coli do?",
  ("Adhere it to the small intestine",
   "Correct: its fimbriae provide adhesion to the small intestine, where its heat-labile and heat-stable toxins "
   "promote fluid and electrolyte secretion."),
  [("Invade the large intestine",
    "Invading the large intestine is what the enteroinvasive strain and Shigella do; enterotoxigenic fimbriae "
    "adhere to the small intestine.", "adjacent pathotype (EIEC)"),
   ("Carry its flagellar antigen",
    "The flagellar antigen is H, on the flagella; fimbriae carry the K antigen and, in this strain, attach it to the "
    "small intestine.", "antigen location confused"),
   ("Deliver Shiga toxin to cells",
    "Shiga toxin is delivered by enterohemorrhagic Escherichia coli through a cell wall receptor that fuses with the "
    "host membrane; enterotoxigenic fimbriae adhere to the small intestine.", "adjacent pathotype (EHEC)")],
  c(56, 52, 57, 59)),

# ============================================================== ENTEROINVASIVE E. COLI (slide 57)
Q("EIEC", IO1,
  "Which infection does enteroinvasive Escherichia coli resemble?",
  ("Shigellosis",
   "Correct: enteroinvasive Escherichia coli causes an inflammatory disease of the large intestine similar to "
   "shigellosis, with profuse bloody diarrhea and high fever."),
  [("Typhoid fever",
    "Typhoid fever is Salmonella typhi's invasive disease of the small intestine leading to septicemia; "
    "enteroinvasive Escherichia coli resembles shigellosis.", "adjacent fact from the same lecture (typhoid)"),
   ("Traveler's diarrhea",
    "Traveler's diarrhea is the toxigenic disease of enterotoxigenic Escherichia coli; the enteroinvasive strain "
    "resembles shigellosis.", "adjacent pathotype (ETEC)"),
   ("Melioidosis",
    "Melioidosis is Burkholderia pseudomallei infection from tropical soil and water; enteroinvasive Escherichia coli "
    "resembles shigellosis.", "unrelated disease from the same lecture")],
  c(57, 23, 56, 74)),

Q("EIEC", IO1,
  "How does enteroinvasive Escherichia coli damage the intestinal wall?",
  ("Mechanically, without toxins",
   "Correct: it binds the intestinal wall with adhesin proteins and damages it through mechanical cell damage; it "
   "produces no toxins."),
  [("With heat-labile toxin",
    "The heat-labile and heat-stable toxins belong to enterotoxigenic Escherichia coli; the enteroinvasive strain "
    "makes no toxins.", "adjacent pathotype (ETEC)"),
   ("Through Shiga toxin release",
    "Shiga toxin belongs to enterohemorrhagic Escherichia coli and Shigella; the enteroinvasive strain has no "
    "toxins and damages cells mechanically.", "adjacent pathotype (EHEC)"),
   ("By blocking thiamin uptake",
    "Inhibiting thiamin (vitamin B1) uptake is an enteropathogenic Escherichia coli effect; the enteroinvasive "
    "strain causes mechanical cell damage.", "adjacent pathotype (EPEC)")],
  c(57, 56, 58, 59)),

Q("EIEC", IO1,
  "Which pair of findings marks enteroinvasive Escherichia coli infection?",
  ("Bloody diarrhea and high fever",
   "Correct: it causes profuse bloody diarrhea and high fever, from inflammatory disease of the large intestine; "
   "the very young and very old are most susceptible."),
  [("Watery diarrhea, little fever",
    "Diarrhea and cramping with a low-grade to no fever describe enterotoxigenic Escherichia coli; the "
    "enteroinvasive strain gives bloody diarrhea and high fever.", "adjacent pathotype (ETEC)"),
   ("Wasting diarrhea in infants",
    "The wasting form of infantile diarrhea is enteropathogenic Escherichia coli; the enteroinvasive strain gives "
    "bloody diarrhea and high fever.", "adjacent pathotype (EPEC)"),
   ("Rose spots and sustained fever",
    "Rose-colored spots with a sustained fever mark typhoid fever; enteroinvasive Escherichia coli gives profuse "
    "bloody diarrhea and high fever.", "adjacent fact from the same lecture (typhoid)")],
  c(57, 56, 58, 74)),

Q("EIEC", IO1,
  "How is enteroinvasive Escherichia coli diagnosed?",
  ("Immunochemistry and gene probes",
   "Correct: diagnosis is through immunochemical tests, tissue culture and gene probes."),
  [("Black colonies on Rainbow agar",
    "Black colonies on Rainbow agar identify Escherichia coli O157:H7, the enterohemorrhagic strain; the "
    "enteroinvasive strain is diagnosed by immunochemical tests, tissue culture and gene probes.", "adjacent pathotype (EHEC)"),
   ("An agglutination titer test",
    "The agglutination titer is the serological test for brucellosis; enteroinvasive Escherichia coli is diagnosed "
    "by immunochemical tests, tissue culture and gene probes.", "adjacent fact from the same lecture (Brucella)"),
   ("Aspirating a swollen bubo",
    "Aspirating buboes is how plague is diagnosed; enteroinvasive Escherichia coli is diagnosed by immunochemical "
    "tests, tissue culture and gene probes.", "adjacent fact from the same lecture (plague)")],
  c(57, 28, 64, 90)),

# ============================================================== ENTEROPATHOGENIC E. COLI (slide 58)
Q("EPEC", IO1,
  "Enteropathogenic Escherichia coli is the leading cause of which disease?",
  ("Wasting infantile diarrhea",
   "Correct: enteropathogenic Escherichia coli is the leading cause of the wasting form of infantile diarrhea and "
   "the greatest single cause of infant mortality worldwide."),
  [("Traveler's diarrhea",
    "Traveler's diarrhea is the disease of enterotoxigenic Escherichia coli; the enteropathogenic strain causes "
    "wasting infantile diarrhea.", "adjacent pathotype (ETEC)"),
   ("Hemorrhagic colitis",
    "Hemorrhagic colitis is caused by enterohemorrhagic Escherichia coli O157:H7; the enteropathogenic strain causes "
    "wasting infantile diarrhea.", "adjacent pathotype (EHEC)"),
   ("Bacillary dysentery",
    "Bacillary dysentery is shigellosis; the enteropathogenic strain causes the wasting form of infantile "
    "diarrhea.", "adjacent fact from the same lecture (Shigella)")],
  c(58, 56, 59, 78)),

Q("EPEC", IO1,
  "How does enteropathogenic Escherichia coli damage the intestine?",
  ("Adheres and destroys microvilli",
   "Correct: the bacteria adhere to the intestinal lining and destroy the microvilli; they also inhibit the uptake "
   "of vitamin B1 (thiamin)."),
  [("Invades the villi of the colon",
    "Invading the villi of the large intestine is what Shigella does; enteropathogenic Escherichia coli adheres to "
    "the lining and destroys microvilli.", "adjacent fact from the same lecture (Shigella)"),
   ("Secretes heat-stable toxin",
    "The heat-stable and heat-labile toxins belong to enterotoxigenic Escherichia coli; the enteropathogenic strain "
    "adheres and destroys microvilli.", "adjacent pathotype (ETEC)"),
   ("Releases Shiga toxin into vessels",
    "Shiga toxin damaging the endothelium is the enterohemorrhagic mechanism; enteropathogenic Escherichia coli "
    "adheres and destroys microvilli.", "adjacent pathotype (EHEC)")],
  c(58, 56, 59, 78)),

Q("EPEC", IO1,
  "Which measure is given to prevent enteropathogenic Escherichia coli infection?",
  ("Breast feeding",
   "Correct: breast feeding is the prevention given for this wasting infantile diarrhea; treatment is fluid and "
   "electrolyte therapy."),
  [("A Haemophilus subunit vaccine",
    "The subunit Hib vaccine protects against Haemophilus influenzae type b (Hib); enteropathogenic Escherichia coli is "
    "prevented by breast feeding.", "adjacent fact from the same lecture (Haemophilus)"),
   ("Quarantine and rodent control",
    "Quarantine and rodent control prevent plague; enteropathogenic Escherichia coli is prevented by breast "
    "feeding.", "adjacent fact from the same lecture (plague)"),
   ("Pasteurizing dairy",
    "Avoiding unpasteurized dairy protects against brucellosis; enteropathogenic Escherichia coli is prevented by "
    "breast feeding.", "adjacent fact from the same lecture (Brucella)")],
  c(58, 27, 90, 98)),

# ============================================================== ENTEROHEMORRHAGIC E. COLI (slides 59-64)
Q("EHEC", IO1,
  "What do the O157 and H7 in Escherichia coli O157:H7 name?",
  ("Somatic and flagellar antigens",
   "Correct: O157 is the somatic (O, cell wall) antigen type 157 and H7 the flagellar (H) antigen type 7."),
  [("Flagellar and capsule antigens",
    "H is indeed the flagellar antigen, but O is the somatic (cell wall) antigen, not the capsule; the capsule "
    "antigen is K.", "one antigen letter confused"),
   ("Capsule and somatic antigens",
    "The capsule antigen is K, which this name does not use; O157 is the somatic antigen and H7 the flagellar "
    "antigen.", "one antigen letter confused"),
   ("Toxin and plasmid types",
    "The letters name surface antigens, not a toxin or a plasmid; O157 is somatic and H7 flagellar.",
    "antigen naming confused with virulence factors")],
  c(59, 52)),

Q("EHEC", IO1,
  "Which complication of enterohemorrhagic Escherichia coli infection damages the kidneys?",
  ("Hemolytic uremic syndrome",
   "Correct: in a minority of cases, toxins produce apoptosis of renal tubular epithelial cells and coagulation, the "
   "hemolytic uremic syndrome."),
  [("Bladder and kidney stones",
    "Bladder and kidney stones are related to Proteus infection; the kidney complication of enterohemorrhagic "
    "Escherichia coli is hemolytic uremic syndrome.", "adjacent fact from the same lecture (Proteus)"),
   ("Infective endocarditis",
    "Infective endocarditis is a heart infection, from Haemophilus parainfluenzae and aphrophilus after dental "
    "procedures; the enterohemorrhagic complication is hemolytic uremic syndrome.", "adjacent fact from the same lecture (Haemophilus)"),
   ("Rose-spot enteric fever",
    "Rose spots with a sustained fever mark typhoid fever; the kidney complication of enterohemorrhagic "
    "Escherichia coli is hemolytic uremic syndrome.", "adjacent fact from the same lecture (typhoid)")],
  c(60, 59, 70, 74, 100)),

Q("EHEC", IO2,
  "What is the reservoir of Escherichia coli O157:H7?",
  ("The intestines of cattle",
   "Correct: the reservoir is the intestines of cattle; people are infected through contaminated beef, water and "
   "vegetables."),
  [("Wild rodents and fleas",
    "Wild rodents and their fleas carry Yersinia pestis; Escherichia coli O157:H7 lives in the intestines of "
    "cattle.", "adjacent fact from the same lecture (plague)"),
   ("Pet turtles and reptiles",
    "Pet turtles and other reptiles spread the animal salmonelloses; Escherichia coli O157:H7 lives in the "
    "intestines of cattle.", "adjacent fact from the same lecture (Salmonella)"),
   ("Rabbits and other mammals",
    "Rabbits carry tularemia, rabbit fever; the reservoir of Escherichia coli O157:H7 is the intestines of cattle.",
    "adjacent fact from the same lecture (Francisella)")],
  c(60, 29, 76, 83)),

Q("EHEC", IO2,
  "Which foods transmit Escherichia coli O157:H7?",
  ("Contaminated beef, water, vegetables",
   "Correct: from its reservoir in cattle intestines, Escherichia coli O157:H7 reaches people through contaminated "
   "beef, water and vegetables."),
  [("Raw oysters and other shellfish",
    "Shellfish are not named for this strain; Escherichia coli O157:H7 comes from cattle and reaches people in "
    "contaminated beef, water and vegetables.", "seafood route assumed"),
   ("Honey given to young infants",
    "Honey is not a source named for any Gram-negative bacillus here; Escherichia coli O157:H7 spreads through "
    "contaminated beef, water and vegetables.", "Gram-positive source borrowed"),
   ("Eggs from backyard flocks",
    "Eggs and backyard flocks spread Salmonella; Escherichia coli O157:H7 spreads through contaminated beef, water "
    "and vegetables.", "adjacent fact from the same lecture (Salmonella)")],
  c(60, 76, 77)),

Q("EHEC", IO1,
  "Why is antibiotic therapy approached with caution in enterohemorrhagic Escherichia coli infection?",
  ("It may worsen hemolytic uremic syndrome",
   "Correct: antibiotic therapy may exacerbate hemolytic uremic syndrome; treatment relies on dialysis, "
   "transfusions and plasmapheresis, with corticosteroids if diarrhea is not involved."),
  [("It destroys the intestinal microvilli",
    "Destroying microvilli is what enteropathogenic Escherichia coli itself does; the caution with antibiotics in "
    "enterohemorrhagic infection is that they may worsen hemolytic uremic syndrome.", "adjacent pathotype (EPEC)"),
   ("It spreads the infection to the lungs",
    "No spread to the lungs is described; the caution is that antibiotic therapy may exacerbate hemolytic uremic "
    "syndrome.", "invented complication"),
   ("It triggers relapse from the gallbladder",
    "Gallbladder shedding is how chronic typhoid carriers spread Salmonella typhi; for enterohemorrhagic "
    "Escherichia coli, antibiotics may worsen hemolytic uremic syndrome.", "adjacent fact from the same lecture (typhoid)")],
  c(63, 58, 73)),

Q("EHEC", IO1,
  "How does the Shiga toxin carried by Escherichia coli O157:H7 damage endothelial cells?",
  ("It halts their protein synthesis",
   "Correct: Shiga toxin binds ribosomes and disrupts protein synthesis, so endothelial cells detach, exposing "
   "platelets to the subendothelium and initiating coagulation."),
  [("It blocks their thiamin uptake",
    "Blocking thiamin uptake is an enteropathogenic Escherichia coli effect; Shiga toxin binds ribosomes and "
    "disrupts protein synthesis.", "adjacent pathotype (EPEC)"),
   ("It drives their fluid secretion",
    "Fluid and electrolyte secretion is driven by the enterotoxigenic heat-labile and heat-stable toxins; Shiga "
    "toxin halts protein synthesis.", "adjacent pathotype (ETEC)"),
   ("It digests their collagen",
    "Collagenase is a mediator macrophages release under endotoxin; Shiga toxin binds ribosomes and disrupts "
    "protein synthesis in endothelial cells.", "adjacent fact from the same lecture (endotoxin)")],
  c(59, 10, 56, 58)),

Q("EHEC", IO1,
  "The chromogenic agar shown is used for rapid identification. Which strain forms its black colonies?",
  ("Escherichia coli O157:H7",
   "Correct: on Rainbow agar, Escherichia coli O157:H7 colonies are black; the agar carries chromogenic substrates "
   "for beta-galactosidase (blue-black) and beta-glucuronidase (red), and O157:H7 is glucuronidase negative."),
  [("Proteus vulgaris",
    "Proteus vulgaris is recognized by its wavelike, swarming growth; the black colonies on Rainbow agar are "
    "Escherichia coli O157:H7.", "other identifying growth pattern"),
   ("Serratia marcescens",
    "Serratia marcescens is recognized by its red pigment, prodigiosin; the black colonies on Rainbow agar are "
    "Escherichia coli O157:H7.", "other identifying color"),
   ("Klebsiella pneumoniae",
    "Klebsiella pneumoniae is recognized by its large capsule; the black colonies on Rainbow agar are Escherichia "
    "coli O157:H7.", "other identifying trait")],
  ci(64, 66, 68, 71),
  img=IMG + "/l14-fig-03.jpg",
  alt="Close view of an agar plate scattered with small black colonies and pink-purple colonies.",
  slide="Slide 64"),

Q("EHEC", IO1,
  "Why do Escherichia coli O157:H7 colonies look black on Rainbow agar?",
  ("It lacks glucuronidase",
   "Correct: Rainbow agar carries chromogenic substrates for beta-galactosidase (blue/black) and beta-glucuronidase "
   "(red); O157:H7 is glucuronidase negative, so its colonies are black."),
  [("It lacks galactosidase",
    "Beta-galactosidase gives the blue-black color, so lacking it would not make colonies black; O157:H7 is "
    "glucuronidase negative.", "enzymes reversed"),
   ("It makes a black pigment",
    "The black comes from a chromogenic substrate in the agar, not a pigment the bacterium makes; O157:H7 is "
    "glucuronidase negative.", "medium color confused with a bacterial pigment"),
   ("It produces hydrogen sulfide",
    "Hydrogen sulfide is a branch of the biochemical tree (Proteus is positive), not the basis of Rainbow agar; "
    "O157:H7 is glucuronidase negative.", "other biochemical test")],
  ci(47, 64)),

# ============================================================== OTHER COLIFORMS (slides 66-68)
Q("Other coliforms", IO1,
  "Which coliform has a large capsule and is a normal inhabitant of the respiratory tract?",
  ("Klebsiella pneumoniae",
   "Correct: Klebsiella pneumoniae, a normal inhabitant of the respiratory tract with a large capsule, causes "
   "nosocomial pneumonia, meningitis, bacteremia, wound infections and urinary tract infections."),
  [("Enterobacter species",
    "Enterobacter causes urinary tract and surgical wound infections and is serious in the bloodstream; the "
    "encapsulated respiratory inhabitant is Klebsiella pneumoniae.", "other coliform"),
   ("Citrobacter species",
    "Citrobacter causes opportunistic urinary tract infections and bacteremia; the encapsulated respiratory "
    "inhabitant is Klebsiella pneumoniae.", "other coliform"),
   ("Escherichia coli",
    "Escherichia coli is the common aerobic gut coliform; the coliform with a large capsule that inhabits the "
    "respiratory tract is Klebsiella pneumoniae.", "other coliform")],
  ci(67, 66, 55)),

Q("Other coliforms", IO1,
  "The capsule stain shows rods ringed by large capsules, from a patient with nosocomial pneumonia. Which coliform "
  "is it?",
  ("Klebsiella pneumoniae",
   "Correct: Klebsiella pneumoniae has a large capsule, shown by a capsule stain, and is a cause of nosocomial "
   "pneumonia; it is a normal inhabitant of the respiratory tract."),
  [("Citrobacter species",
    "Citrobacter is an opportunist of urinary tract infections and bacteremia, not known for a large capsule; that "
    "is Klebsiella pneumoniae.", "other coliform"),
   ("Enterobacter species",
    "Enterobacter infects urinary tract, surgical wounds, spinal fluid, sputum and blood, but the large capsule "
    "belongs to Klebsiella pneumoniae.", "other coliform"),
   ("Escherichia coli",
    "Escherichia coli is the gut coliform behind most urinary tract infections; the large capsule in nosocomial "
    "pneumonia marks Klebsiella pneumoniae.", "other coliform")],
  ci(67, 65, 66),
  img=IMG + "/l14-fig-04.jpg",
  alt="Capsule stain on a dark magenta background: pale rods each surrounded by a wide clear halo.",
  slide="Slide 67"),

Q("Other coliforms", IO1,
  "Which enteric produces the red pigment prodigiosin?",
  ("Serratia marcescens",
   "Correct: Serratia marcescens produces the red pigment prodigiosin; it causes pneumonia in chronic alcoholics, "
   "burn and wound infections, urinary tract infections, and septicemia and meningitis in the immunocompromised."),
  [("Klebsiella pneumoniae",
    "Klebsiella pneumoniae is known for its large capsule, not a pigment; prodigiosin is the red pigment of Serratia "
    "marcescens.", "other coliform"),
   ("Pseudomonas aeruginosa",
    "Pseudomonas aeruginosa makes the greenish-blue pigment pyocyanin and is not an enteric; the red pigment is "
    "Serratia marcescens's prodigiosin.", "other pigmented organism"),
   ("Proteus vulgaris",
    "Proteus vulgaris is known for wavelike swarming growth, not a red pigment; prodigiosin belongs to Serratia "
    "marcescens.", "other identifying trait")],
  ci(68, 18, 67, 71)),

Q("Other coliforms", IO1,
  "Serratia marcescens pneumonia is typical in which hosts?",
  ("Chronic alcoholics",
   "Correct: Serratia marcescens causes pneumonia in chronic alcoholics, as well as burn and wound infections, "
   "urinary tract infections, and septicemia and meningitis in immunocompromised hosts."),
  [("Cystic fibrosis patients",
    "Cystic fibrosis is where Pseudomonas aeruginosa and Burkholderia cepacia are a particular problem; Serratia "
    "pneumonia is typical in chronic alcoholics.", "adjacent fact from the same lecture (Pseudomonas)"),
   ("Contact lens wearers",
    "Contact lens wearers get Pseudomonas aeruginosa corneal ulcers; Serratia pneumonia is typical in chronic "
    "alcoholics.", "adjacent fact from the same lecture (Pseudomonas)"),
   ("Unvaccinated infants",
    "Unvaccinated infants carry the highest pertussis incidence; Serratia pneumonia is typical in chronic "
    "alcoholics.", "adjacent fact from the same lecture (pertussis)")],
  c(68, 18, 19, 22, 35)),

# ============================================================== PROTEUS AND RELATIVES (slides 69-72)
Q("Proteus & relatives", IO1,
  "Which finding on agar is diagnostic for Proteus vulgaris?",
  ("A wavelike swarming pattern",
   "Correct: Proteus is highly motile, with peritrichous flagella, and its diagnostic growth pattern is a wavelike, "
   "swarming spread across the agar."),
  [("Black colonies on Rainbow agar",
    "Black colonies on Rainbow agar identify Escherichia coli O157:H7; Proteus vulgaris is diagnosed by its "
    "wavelike swarming.", "adjacent fact from the same lecture (EHEC)"),
   ("Red-pigmented colonies",
    "Red colonies, from prodigiosin, mark Serratia marcescens; Proteus vulgaris spreads in a wavelike swarming "
    "pattern.", "adjacent fact from the same lecture (Serratia)"),
   ("Growth on cooked-blood agar",
    "Needing chocolate agar (cooked blood) is the Haemophilus trait; Proteus vulgaris is recognized by wavelike "
    "swarming.", "adjacent fact from the same lecture (Haemophilus)")],
  ci(71, 64, 68, 70, 97)),

Q("Proteus & relatives", IO1,
  "Which genus produces the wavelike growth shown on this plate?",
  ("Proteus",
   "Correct: the wavelike, swarming pattern is the diagnostic growth of Proteus vulgaris, a highly motile rod with "
   "peritrichous flagella."),
  [("Klebsiella",
    "Klebsiella is recognized by its large capsule and is nonmotile in the biochemical tree; swarming growth is "
    "Proteus.", "other coliform"),
   ("Serratia",
    "Serratia marcescens is recognized by its red pigment, prodigiosin; wavelike swarming is Proteus.",
    "other identifying trait"),
   ("Haemophilus",
    "Haemophilus is fastidious and needs chocolate agar; it does not swarm across a plate. Wavelike swarming is "
    "Proteus.", "fastidious organism")],
  ci(71, 47, 67, 68, 97),
  img=IMG + "/l14-fig-05.jpg",
  alt="Agar surface covered by concentric rings of growth spreading outward from two central points.",
  slide="Slide 71"),

Q("Proteus & relatives", IO1,
  "Which condition is related to Proteus infection?",
  ("Bladder and kidney stones",
   "Correct: Proteus, an opportunist causing urinary tract and wound infections, pneumonia, septicemia and infant "
   "diarrhea, is related to the development of bladder and kidney stones and associated with Crohn's disease."),
  [("Hemolytic uremic syndrome",
    "Hemolytic uremic syndrome is the kidney complication of enterohemorrhagic Escherichia coli; Proteus is related "
    "to bladder and kidney stones.", "adjacent fact from the same lecture (EHEC)"),
   ("Wasting infantile diarrhea",
    "The wasting form of infantile diarrhea is enteropathogenic Escherichia coli; Proteus is related to bladder and "
    "kidney stones.", "adjacent fact from the same lecture (EPEC)"),
   ("Ileitis mimicking appendicitis",
    "Inflammation of the ileum that mimics appendicitis is Yersinia enterocolitica; Proteus is related to bladder "
    "and kidney stones.", "adjacent fact from the same lecture (Yersinia enterocolitica)")],
  c(70, 58, 60, 80)),

Q("Proteus & relatives", IO2,
  "Which opportunist has multiple animal reservoirs and causes catheter-related urinary tract infections?",
  ("Providencia species",
   "Correct: Providencia has multiple animal reservoirs and causes nosocomial infections, urinary tract infections "
   "with catheters, and gastroenteritis."),
  [("Pasteurella multocida",
    "Pasteurella is normal flora in animals, but it infects through animal bites and scratches, not catheters; the "
    "catheter opportunist with animal reservoirs is Providencia.", "zoonotic organism with the wrong route"),
   ("Klebsiella pneumoniae",
    "Klebsiella pneumoniae is a normal inhabitant of the human respiratory tract, known for nosocomial pneumonia; the "
    "opportunist with animal reservoirs is Providencia.", "other nosocomial enteric"),
   ("Haemophilus ducreyi",
    "Haemophilus ducreyi causes chancroid, a sexually transmitted disease of the tropics; the catheter opportunist "
    "is Providencia.", "unrelated organism from the same lecture")],
  c(72, 66, 96, 100)),

# ============================================================== SALMONELLA (slides 73-77)
Q("Salmonella", IO2,
  "Who are the hosts of Salmonella typhi?",
  ("Humans exclusively",
   "Correct: humans are the exclusive hosts of Salmonella typhi and Salmonella paratyphi, the most serious pathogens "
   "of the genus, causing typhoid and paratyphoid fever."),
  [("Poultry and their eggs",
    "Poultry and eggs carry the animal salmonelloses such as Salmonella enteritidis; Salmonella typhi infects humans "
    "only.", "animal salmonellosis source"),
   ("Reptiles such as turtles",
    "Pet turtles and bearded dragons spread the animal salmonelloses; the hosts of Salmonella typhi are humans "
    "exclusively.", "animal salmonellosis source"),
   ("Cattle and dairy herds",
    "Cattle and dairy products carry animal salmonelloses (and Escherichia coli O157:H7); Salmonella typhi's hosts "
    "are humans exclusively.", "animal reservoir")],
  c(73, 60, 76, 77)),

Q("Salmonella", IO2,
  "How is Salmonella typhi usually acquired?",
  ("Fecally contaminated food or water",
   "Correct: the bacillus enters by ingestion of fecally contaminated food or water, occasionally by close personal "
   "contact; hence 'Boil it, cook it, peel it, or forget it.'"),
  [("Bites of infected fleas",
    "Flea bites transmit plague; Salmonella typhi is swallowed in fecally contaminated food or water.",
    "adjacent fact from the same lecture (plague)"),
   ("Inhaled aerosols",
    "Inhaled aerosols spread Legionella and pertussis; Salmonella typhi is acquired by ingesting fecally "
    "contaminated food or water.", "adjacent fact from the same lecture (respiratory spread)"),
   ("Contact with animal placentas",
    "Contact with the blood, urine and placentas of infected animals spreads brucellosis; humans are the only hosts "
    "of Salmonella typhi, which is swallowed in fecally contaminated food or water.", "adjacent fact from the same lecture (Brucella)")],
  c(73, 27, 30, 40, 83)),

Q("Salmonella", IO2,
  "From which organ do some chronic carriers shed Salmonella typhi?",
  ("The gallbladder",
   "Correct: typhoid has asymptomatic carriers, and some chronic carriers shed the bacilli from the gallbladder."),
  [("The lungs",
    "Shedding from the lungs by aerosol is the pneumonic plague pattern; chronic typhoid carriers shed from the "
    "gallbladder.", "adjacent fact from the same lecture (pneumonic plague)"),
   ("The skin",
    "Rose spots are a typhoid rash, not the carrier's source; chronic carriers shed Salmonella typhi from the "
    "gallbladder.", "symptom site taken for carriage site"),
   ("The kidneys",
    "The kidneys are the target of hemolytic uremic syndrome, not a typhoid carrier site; chronic carriers shed from "
    "the gallbladder.", "adjacent fact from the same lecture (EHEC)")],
  c(73, 60, 74, 88)),

Q("Salmonella", IO1,
  "Which rash marks typhoid fever?",
  ("Rose-colored spots",
   "Correct: typhoid fever brings a sustained fever (103-104 degrees), a rash of rose-colored spots, weakness, "
   "stomach pains and loss of appetite."),
  [("Purpura with necrosis",
    "Purpura that degenerates into necrosis and gangrene marks septicemic plague; typhoid gives rose-colored spots.",
    "adjacent fact from the same lecture (septicemic plague)"),
   ("An ulcer with swollen nodes",
    "Ulcerative skin lesions with swollen lymph nodes mark tularemia; typhoid gives a rash of rose-colored spots.",
    "adjacent fact from the same lecture (tularemia)"),
   ("A follicular skin rash",
    "Skin rashes in healthy people are typical of Pseudomonas aeruginosa; typhoid gives rose-colored spots.",
    "adjacent fact from the same lecture (Pseudomonas)")],
  c(74, 19, 29, 88)),

Q("Salmonella", IO1,
  "How does Salmonella typhi spread through the body in typhoid fever?",
  ("From the small intestine into the blood",
   "Correct: the bacilli adhere to the small intestine and cause an invasive diarrhea that leads to septicemia; "
   "they are carried to the liver and spleen, and the intestinal wall can ulcerate and perforate."),
  [("Via the lymph from a flea bite",
    "Spread from a flea bite into the lymph, forming a bubo, is bubonic plague; typhoid bacilli go from the small "
    "intestine into the blood.", "adjacent fact from the same lecture (bubonic plague)"),
   ("It stays in the large-bowel villi",
    "Staying in the villi of the large intestine without invading the blood is Shigella; typhoid bacilli enter the "
    "blood from the small intestine.", "adjacent fact from the same lecture (Shigella)"),
   ("Through damaged skin into phagocytes",
    "Entry through damaged skin, carried by phagocytes to the organs, is brucellosis; typhoid bacilli invade from "
    "the small intestine into the blood.", "adjacent fact from the same lecture (Brucella)")],
  ci(74, 74, 28, 78, 88)),

Q("Salmonella", IO1,
  "Which vaccines give temporary protection against typhoid fever?",
  ("An oral and an injected vaccine",
   "Correct: two vaccines give temporary protection, an oral vaccine (4 doses) and an injected vaccine (1 dose)."),
  [("An acellular toxoid vaccine",
    "An acellular vaccine of toxoid and other antigens is the pertussis component of DTaP (diphtheria, tetanus and acellular pertussis); typhoid has an oral and "
    "an injected vaccine.", "adjacent fact from the same lecture (pertussis)"),
   ("A subunit capsule vaccine",
    "The subunit vaccine in this group is against Haemophilus influenzae type b (Hib); typhoid has an oral and an "
    "injected vaccine.", "adjacent fact from the same lecture (Haemophilus)"),
   ("A vaccine given to animals",
    "An animal vaccine is what exists for brucellosis; typhoid has two human vaccines, one oral and one injected.",
    "adjacent fact from the same lecture (Brucella)")],
  c(74, 28, 31, 98)),

Q("Salmonella", IO2,
  "Which sources spread the animal salmonelloses?",
  ("Poultry, eggs and pet reptiles",
   "Correct: the animal salmonelloses are acquired by ingestion from cattle, poultry and eggs, rodents, reptiles "
   "(pet turtles, bearded dragons), animal and dairy products, and fomites contaminated with animal intestinal "
   "flora; backyard flocks are a source."),
  [("Fleas from wild rodents",
    "Fleas from wild rodents spread plague; the animal salmonelloses come from poultry, eggs, reptiles, cattle and "
    "other animal sources.", "adjacent fact from the same lecture (plague)"),
   ("Aerosols from cooling towers",
    "Cooling-tower aerosols spread Legionella; the animal salmonelloses are swallowed from poultry, eggs, reptiles "
    "and other animal sources.", "adjacent fact from the same lecture (Legionella)"),
   ("Animal bites and scratches",
    "Animal bites and scratches spread Pasteurella multocida; the animal salmonelloses are acquired by ingestion.",
    "adjacent fact from the same lecture (Pasteurella)")],
  c(76, 77, 40, 83, 96)),

Q("Salmonella", IO1,
  "How do the salmonelloses other than typhoid fever compare with typhoid fever?",
  ("Less severe but more prevalent",
   "Correct: salmonelloses other than typhoid fever (enteric fevers, Salmonella food poisoning and gastroenteritis) "
   "are usually less severe than typhoid fever but more prevalent."),
  [("More severe and more prevalent",
    "They are more prevalent but usually LESS severe than typhoid fever, the most serious Salmonella disease.",
    "severity reversed"),
   ("Less severe and less prevalent",
    "They are usually less severe, but MORE prevalent than typhoid fever, not less.", "prevalence reversed"),
   ("More severe but less prevalent",
    "Both directions are reversed: the animal salmonelloses are usually less severe than typhoid fever but more "
    "prevalent.", "both directions reversed")],
  c(76, 73)),

Q("Salmonella", IO2,
  "Salmonella cholerae-suis is a zoonosis of which animal?",
  ("Swine",
   "Correct: Salmonella cholerae-suis is a zoonosis of swine; Salmonella enteritidis covers about 1,700 serotypes, "
   "all zoonotic in origin."),
  [("Cattle",
    "Cattle carry Brucella abortus and, in their intestines, Escherichia coli O157:H7; Salmonella cholerae-suis is a "
    "zoonosis of swine.", "adjacent fact from the same lecture (cattle organisms)"),
   ("Rabbits",
    "Rabbits carry tularemia, rabbit fever; Salmonella cholerae-suis is a zoonosis of swine.",
    "adjacent fact from the same lecture (Francisella)"),
   ("Rodents",
    "Rodents are the reservoir of plague; Salmonella cholerae-suis is a zoonosis of swine.",
    "adjacent fact from the same lecture (plague)")],
  c(76, 27, 29, 60, 83)),

# ============================================================== SHIGELLA (slides 78-79)
Q("Shigella", IO1,
  "How does Shigella cause dysentery?",
  ("It invades the large-bowel villi",
   "Correct: Shigella invades the villi of the large intestine and enters Peyer's patches to set off inflammation; "
   "it does not perforate the intestine or invade the blood."),
  [("It spreads into the bloodstream",
    "Shigella does not invade the blood; it is Salmonella typhi whose invasive diarrhea leads to septicemia.",
    "adjacent fact from the same lecture (typhoid)"),
   ("It perforates the bowel wall",
    "Shigella does not perforate the intestine; perforation of the intestinal wall is a typhoid feature.",
    "adjacent fact from the same lecture (typhoid)"),
   ("It sticks to small-bowel cells",
    "Adhesion to the small intestine by fimbriae is enterotoxigenic Escherichia coli; Shigella invades the villi of "
    "the large intestine.", "adjacent fact from the same lecture (ETEC)")],
  c(78, 56, 74)),

Q("Shigella", IO1,
  "In shigellosis, what does the enterotoxin do?",
  ("Damages mucosa and villi",
   "Correct: the enterotoxin damages the mucosa and villi, causing bleeding and mucus secretion; the endotoxin "
   "initiates the fever."),
  [("Initiates the fever",
    "Initiating the fever is the job of the endotoxin; the enterotoxin damages the mucosa and villi, with bleeding "
    "and mucus.", "the other Shigella toxin's role"),
   ("Blocks thiamin uptake",
    "Inhibiting thiamin uptake is an enteropathogenic Escherichia coli effect; the Shigella enterotoxin damages the "
    "mucosa and villi.", "adjacent fact from the same lecture (EPEC)"),
   ("Destroys ciliated cells",
    "Destroying ciliated respiratory cells is what the pertussis toxins do; the Shigella enterotoxin damages the "
    "intestinal mucosa and villi.", "adjacent fact from the same lecture (pertussis)")],
  c(78, 31, 58)),

Q("Shigella", IO2,
  "How is Shigella transmitted?",
  ("By swallowing contaminated food",
   "Correct: Shigella is transmitted by ingestion of fecally contaminated food; it then invades the villi of the "
   "large intestine."),
  [("By inhaling contaminated aerosols",
    "Aerosols spread Legionella, pertussis and pneumonic plague; Shigella is swallowed in fecally contaminated "
    "food.", "respiratory route"),
   ("By the bite of an infected flea",
    "Flea bites spread plague; Shigella is transmitted by ingestion of fecally contaminated food.",
    "adjacent fact from the same lecture (plague)"),
   ("By animal bites and scratches",
    "Animal bites and scratches spread Pasteurella multocida; Shigella is transmitted by eating fecally "
    "contaminated food.", "adjacent fact from the same lecture (Pasteurella)")],
  c(78, 30, 40, 83, 96)),

# ============================================================== ENTERIC YERSINIA (slide 80)
Q("Enteric Yersinia", IO1,
  "Which condition can Yersinia enterocolitica infection mimic?",
  ("Appendicitis",
   "Correct: the bacteria enter the small intestinal mucosa, some enter the lymphatics and survive in phagocytes, "
   "and inflammation of the ileum can mimic appendicitis."),
  [("Shigellosis",
    "Resembling shigellosis is said of enteroinvasive Escherichia coli; Yersinia enterocolitica's ileitis can mimic "
    "appendicitis.", "adjacent fact from the same lecture (EIEC)"),
   ("Crohn's disease",
    "An association with Crohn's disease is given for Proteus; Yersinia enterocolitica's ileitis can mimic "
    "appendicitis.", "adjacent fact from the same lecture (Proteus)"),
   ("Typhoid fever",
    "Typhoid fever is Salmonella typhi infection leading to septicemia; Yersinia enterocolitica can mimic "
    "appendicitis.", "adjacent fact from the same lecture (typhoid)")],
  c(80, 57, 70, 73)),

Q("Enteric Yersinia", IO1,
  "How does Yersinia pseudotuberculosis infection differ from Yersinia enterocolitica infection?",
  ("More lymph node inflammation",
   "Correct: Yersinia pseudotuberculosis causes an infection similar to Yersinia enterocolitica, with more lymph "
   "node inflammation; treatment is mostly supportive."),
  [("It is spread by fleas",
    "Flea transmission belongs to the nonenteric Yersinia pestis; Yersinia pseudotuberculosis is an enteric with "
    "more lymph node inflammation.", "adjacent fact from the same lecture (Yersinia pestis)"),
   ("It forms buboes in the groin",
    "Buboes in the groin or axilla mark bubonic plague, Yersinia pestis; Yersinia pseudotuberculosis gives more "
    "lymph node inflammation than its enteric cousin.", "adjacent fact from the same lecture (plague)"),
   ("It causes bloody dysentery",
    "Bloody dysentery is shigellosis; Yersinia pseudotuberculosis resembles Yersinia enterocolitica with more lymph "
    "node inflammation.", "adjacent fact from the same lecture (Shigella)")],
  c(80, 83, 88, 78)),

Q("Enteric Yersinia", IO2,
  "Where does Yersinia enterocolitica come from?",
  ("Animals, fish, produce and water",
   "Correct: Yersinia enterocolitica comes from domestic and wild animals, fish, fruits, vegetables and water."),
  [("Humans, its exclusive host",
    "Humans are the exclusive hosts of Salmonella typhi; Yersinia enterocolitica comes from animals, fish, fruits, "
    "vegetables and water.", "adjacent fact from the same lecture (typhoid)"),
   ("Fleas from wild rodents",
    "Fleas from wild rodents carry the nonenteric Yersinia pestis; Yersinia enterocolitica comes from animals, fish, "
    "produce and water.", "adjacent fact from the same lecture (Yersinia pestis)"),
   ("Cooling towers and spas",
    "Cooling towers and spas harbor Legionella; Yersinia enterocolitica comes from animals, fish, fruits, "
    "vegetables and water.", "adjacent fact from the same lecture (Legionella)")],
  c(80, 39, 73, 83)),

# ============================================================== YERSINIA PESTIS AND PLAGUE (slides 81-94)
Q("Yersinia pestis", IO1,
  "Which staining feature does Yersinia pestis show?",
  ("Unusual bipolar staining",
   "Correct: Yersinia pestis is a tiny, Gram-negative rod with unusual bipolar staining and capsules."),
  [("Weakly Gram-negative stain",
    "Weak Gram-negative staining describes Legionella; Yersinia pestis is a tiny Gram-negative rod with unusual "
    "bipolar staining.", "adjacent fact from the same lecture (Legionella)"),
   ("Gram-positive purple rods",
    "Yersinia pestis is a Gram-negative rod, not Gram-positive; its distinctive feature is unusual bipolar "
    "staining.", "reversed Gram reaction"),
   ("A wide capsule halo stain",
    "A capsule stain with wide halos is the Klebsiella pneumoniae picture; Yersinia pestis is recognized by "
    "unusual bipolar staining.", "adjacent fact from the same lecture (Klebsiella)")],
  ci(82, 81, 39, 67)),

Q("Yersinia pestis", IO1,
  "The tiny Gram-negative rods among the white blood cells in this smear show unusual bipolar staining. Which "
  "organism are they?",
  ("Yersinia pestis",
   "Correct: tiny Gram-negative rods with unusual bipolar staining are Yersinia pestis, the agent of plague; the "
   "inset shows the stain concentrated at each end of the rod."),
  [("Klebsiella pneumoniae",
    "Klebsiella pneumoniae is recognized by its large capsule; the bipolar-staining tiny rods are Yersinia pestis.",
    "other enteric"),
   ("Legionella pneumophila",
    "Legionella is weakly Gram-negative and pleomorphic, coccobacilli to filaments; bipolar staining marks "
    "Yersinia pestis.", "other Gram-negative rod"),
   ("Haemophilus influenzae",
    "Haemophilus are tiny pleomorphic Gram-negative rods but are not described with bipolar staining; that is "
    "Yersinia pestis.", "other tiny Gram-negative rod")],
  ci(82, 39, 67, 81, 97),
  img=IMG + "/l14-fig-06.jpg",
  alt="Stained smear with several large red-purple white blood cells and many tiny pink rods; an inset circle "
      "magnifies four rods, darker at both ends.",
  slide="Slide 82"),

Q("Yersinia pestis", IO2,
  "How does an infected flea pass Yersinia pestis to a new host?",
  ("By regurgitating while it bites",
   "Correct: the bacteria replicate in the flea's gut and coagulase clots the blood, blocking its esophagus; the "
   "ravenous flea bites more hosts and transmits the bacterium in regurgitated material."),
  [("By injecting it from saliva glands",
    "The bacteria multiply in the flea's gut, not its salivary glands; they are passed on in material the "
    "blocked flea regurgitates as it bites.", "vector mechanism confused"),
   ("By leaving infected feces on skin",
    "Plague is passed in regurgitated material during the bite, after coagulase blocks the flea's esophagus, not in "
    "its feces.", "vector mechanism confused"),
   ("By laying eggs in the host's skin",
    "Fleas do not pass plague through eggs in the skin; the blocked, ravenous flea regurgitates the bacteria while "
    "biting.", "vector mechanism confused")],
  ci(84, 83)),

Q("Yersinia pestis", IO1,
  "What makes a plague-infected flea ravenous?",
  ("Clotted blood blocks its esophagus",
   "Correct: bacterial coagulase causes blood clotting that blocks the flea's esophagus, so the flea becomes "
   "ravenous and tries to bite more hosts."),
  [("Endotoxin raises its body heat",
    "Endotoxin is not what changes the flea's behavior; coagulase clots blood that blocks its esophagus, so it "
    "keeps biting.", "wrong virulence factor"),
   ("Bacteria digest its blood meal",
    "The bacteria replicate in the gut, but the hunger comes from coagulase clotting the blood and blocking the "
    "esophagus.", "misplaced mechanism"),
   ("Murine toxin paralyzes its gut",
    "Murine toxin is listed among the virulence factors, but the flea's hunger comes from coagulase clotting "
    "blood in its esophagus.", "wrong virulence factor")],
  c(83, 81)),

Q("Yersinia pestis", IO1,
  "What is the bubo of bubonic plague?",
  ("A swollen, necrotic lymph node",
   "Correct: the bacillus multiplies in the flea bite, enters the lymph and causes necrosis and swelling of a node, "
   "the bubo, in the groin or axilla."),
  [("A gangrenous patch of skin",
    "Purpura that degenerates into necrosis and gangrene is septicemic plague; the bubo is a swollen, necrotic lymph "
    "node.", "other plague form"),
   ("An ulcer at the bite site",
    "An ulcerative skin lesion is a tularemia sign; the plague bubo is a swollen lymph node in the groin or axilla.",
    "adjacent fact from the same lecture (tularemia)"),
   ("A pus-filled lung cavity",
    "Plague in the lungs is the pneumonic form, spread by aerosol; the bubo is a swollen, necrotic lymph node.",
    "other plague form")],
  c(88, 29, 89)),

Q("Yersinia pestis", IO2,
  "Which form of plague is highly contagious by aerosol?",
  ("Pneumonic",
   "Correct: in pneumonic plague the infection is localized to the lungs, highly contagious by aerosol infection, "
   "and fatal without treatment."),
  [("Bubonic",
    "Bubonic plague starts in a flea bite and spreads through the lymph to form a bubo; the aerosol-spread form is "
    "pneumonic.", "other plague form"),
   ("Septicemic",
    "Septicemic plague is the progression to massive bacterial growth with purpura and gangrene; the aerosol-spread "
    "form is pneumonic.", "other plague form"),
   ("Sylvatic",
    "Sylvatic names plague caught from wild animals, a source rather than a clinical form; the aerosol-spread form "
    "is pneumonic.", "source confused with form")],
  ci(84, 83, 88)),

Q("Yersinia pestis", IO1,
  "Why is septicemic plague called the black plague?",
  ("Purpura turns to gangrene",
   "Correct: in septicemic plague, massive bacterial growth and virulence factors cause intravascular coagulation, "
   "subcutaneous hemorrhage and purpura that degenerates into necrosis and gangrene, the black plague."),
  [("Its buboes turn black",
    "Buboes are the swollen nodes of bubonic plague; the black of septicemic plague is purpura degenerating into "
    "gangrene.", "other plague form"),
   ("The bacteria make black pigment",
    "Yersinia pestis makes no black pigment; the black comes from purpura that degenerates into necrosis and "
    "gangrene.", "pigment assumed"),
   ("The lungs fill with dark blood",
    "Lung involvement is the pneumonic form; the black of septicemic plague is gangrene of the skin after purpura.",
    "other plague form")],
  c(88)),

Q("Yersinia pestis", IO2,
  "What distinguishes sylvatic plague from urban plague?",
  ("Wild versus domestic animal source",
   "Correct: humans develop plague through contact with wild animals (sylvatic plague) or with domestic or "
   "semidomestic animals (urban plague), or, rarely, infected humans."),
  [("Bubonic versus pneumonic illness",
    "Bubonic and pneumonic are clinical forms; sylvatic and urban name the animal source, wild or domestic.",
    "clinical form confused with source"),
   ("Flea bite versus inhaled aerosol",
    "Both kinds of plague involve fleas; sylvatic and urban name the source, wild animals or domestic and "
    "semidomestic ones.", "route confused with source"),
   ("Western versus eastern states",
    "United States cases occur west of the Mississippi either way; sylvatic and urban name the source, wild or "
    "domestic animals.", "geography confused with source")],
  c(83, 88)),

Q("Yersinia pestis", IO2,
  "Where in the United States do human plague cases occur?",
  ("West of the Mississippi",
   "Correct: United States cases occur west of the Mississippi, where Yersinia pestis lives in about 200 species of "
   "mammals, rodents, without causing them disease."),
  [("Along the Gulf Coast",
    "The Gulf Coast is not where plague occurs; United States cases are west of the Mississippi, in wild rodents.",
    "wrong region"),
   ("Across New England",
    "New England is not where plague occurs; United States cases are west of the Mississippi.",
    "wrong region"),
   ("Throughout Florida",
    "Florida is not a plague region; United States cases occur west of the Mississippi.",
    "wrong region")],
  ci(85, 83)),

Q("Yersinia pestis", IO1,
  "Which measures prevent plague?",
  ("Quarantine and rodent control",
   "Correct: plague is prevented by quarantine and control of the rodent population in human habitats; a killed or "
   "attenuated vaccine is available for military personnel, veterinarians and laboratory workers."),
  [("Breast feeding infants",
    "Breast feeding prevents enteropathogenic Escherichia coli infection; plague is prevented by quarantine and "
    "rodent control.", "adjacent fact from the same lecture (EPEC)"),
   ("Boosters for adolescents",
    "Booster doses for children and adolescents answer waning pertussis immunity; plague is prevented by "
    "quarantine and rodent control.", "adjacent fact from the same lecture (pertussis)"),
   ("Pasteurizing dairy products",
    "Avoiding unpasteurized dairy prevents brucellosis; plague is prevented by quarantine and rodent control.",
    "adjacent fact from the same lecture (Brucella)")],
  c(90, 27, 36, 58)),

Q("Yersinia pestis", IO1,
  "How is plague diagnosed?",
  ("History, symptoms, bubo aspirate",
   "Correct: diagnosis depends on history, symptoms and laboratory findings from aspiration of the buboes, and it "
   "must be quick, because death can occur within 2 days of symptoms."),
  [("Charcoal yeast extract culture",
    "Charcoal yeast extract agar grows Legionella; plague is diagnosed from history, symptoms and an aspirate of "
    "the buboes.", "adjacent fact from the same lecture (Legionella)"),
   ("An agglutination titer test",
    "An agglutination titer is the serological test for brucellosis; plague is diagnosed from history, symptoms "
    "and bubo aspirates.", "adjacent fact from the same lecture (Brucella)"),
   ("Black colonies on Rainbow agar",
    "Black colonies on Rainbow agar identify Escherichia coli O157:H7; plague is diagnosed from history, symptoms "
    "and bubo aspirates.", "adjacent fact from the same lecture (EHEC)")],
  c(90, 28, 41, 64)),

Q("Yersinia pestis", IO1,
  "What has examination of deoxyribonucleic acid from Black Death victims and survivors shown about the plague "
  "immunity variants?",
  ("They overlap autoimmune-risk alleles",
   "Correct: the variants that conferred immunity to plague overlap with alleles now known to be associated with "
   "increased susceptibility to autoimmune diseases."),
  [("They were lost after the pandemic",
    "Variants conferring immunity were under strong selective pressure, so later outbreaks had far less mortality; "
    "they were favored, not lost.", "reversed selection"),
   ("They raise the risk of plague",
    "These are the variants that conferred immunity to plague, not susceptibility; they overlap alleles linked to "
    "autoimmune disease.", "reversed effect"),
   ("They protect against autoimmunity",
    "The overlap runs the other way: the plague-immunity variants match alleles associated with increased "
    "susceptibility to autoimmune diseases.", "reversed effect")],
  c(94)),

# ============================================================== PASTEURELLA (slides 95-96)
Q("Pasteurella", IO2,
  "How is Pasteurella multocida usually acquired?",
  ("Animal bites or scratches",
   "Correct: Pasteurella is a zoonotic genus, normal flora in animals; animal bites or scratches cause a local "
   "abscess that can spread to joints, bones and lymph nodes, mostly in veterinarians but also from domestic "
   "animals."),
  [("Bites from infected fleas",
    "Flea bites spread plague; Pasteurella multocida enters through animal bites or scratches.",
    "adjacent fact from the same lecture (plague)"),
   ("Inhaling cooling-tower mist",
    "Cooling-tower aerosols spread Legionella; Pasteurella multocida enters through animal bites or scratches.",
    "adjacent fact from the same lecture (Legionella)"),
   ("Eating undercooked beef",
    "Undercooked beef spreads Escherichia coli O157:H7; Pasteurella multocida enters through animal bites or "
    "scratches.", "adjacent fact from the same lecture (EHEC)")],
  c(96, 40, 60, 83)),

Q("Pasteurella", IO1,
  "Which patients are at risk of septicemia from Pasteurella multocida?",
  ("The immunocompromised",
   "Correct: after a bite or scratch, the immunocompromised are at risk for septicemia and complications involving "
   "the central nervous system and heart."),
  [("Burn patients",
    "Burns are a classic setting for nosocomial Pseudomonas aeruginosa; Pasteurella septicemia threatens the "
    "immunocompromised.", "adjacent fact from the same lecture (Pseudomonas)"),
   ("Chronic alcoholics",
    "Chronic alcoholics are prone to Serratia marcescens pneumonia; Pasteurella septicemia threatens the "
    "immunocompromised.", "adjacent fact from the same lecture (Serratia)"),
   ("Contact lens wearers",
    "Contact lens wearers get Pseudomonas aeruginosa corneal ulcers; Pasteurella septicemia threatens the "
    "immunocompromised.", "adjacent fact from the same lecture (Pseudomonas)")],
  c(96, 18, 19, 68)),

# ============================================================== HAEMOPHILUS (slides 97-101)
Q("Haemophilus", IO1,
  "Why is Haemophilus grown on chocolate agar rather than blood agar?",
  ("It needs hemin from cooked blood",
   "Correct: Haemophilus is fastidious, and none can grow on blood agar without special techniques; chocolate agar "
   "(cooked blood) supplies the hemin or nicotinamide adenine dinucleotide it requires."),
  [("It needs low oxygen to survive",
    "The requirement is for blood factors (hemin, nicotinamide adenine dinucleotide or its phosphate), not low "
    "oxygen; chocolate agar is cooked blood.", "oxygen need assumed"),
   ("It ferments lactose only there",
    "Lactose fermentation is read on MacConkey's and eosin methylene blue agar; chocolate agar is used because "
    "Haemophilus needs hemin from cooked blood.", "differential medium confused"),
   ("It is killed by bile salts",
    "Bile salts are the selective agent of MacConkey's agar; chocolate agar is chosen because Haemophilus needs "
    "blood factors such as hemin.", "selective agent confused")],
  c(97, 48)),

Q("Haemophilus", IO1,
  "Which disease was Haemophilus influenzae once mistakenly thought to cause?",
  ("Influenza (the flu)",
   "Correct: Haemophilus influenzae was misnamed as the causative agent of the flu; it causes acute bacterial "
   "meningitis, epiglottitis, otitis media, sinusitis, pneumonia and bronchitis."),
  [("Whooping cough",
    "Whooping cough is pertussis, caused by Bordetella pertussis; Haemophilus influenzae was misnamed as the cause "
    "of the flu.", "adjacent fact from the same lecture (pertussis)"),
   ("Pink eye",
    "Pink eye (acute conjunctivitis) is caused by Haemophilus aegyptius; Haemophilus influenzae was misnamed as the "
    "cause of the flu.", "other Haemophilus species"),
   ("Chancroid",
    "Chancroid is caused by Haemophilus ducreyi; Haemophilus influenzae was misnamed as the cause of the flu.",
    "other Haemophilus species")],
  c(98, 30, 100)),

Q("Haemophilus", IO1,
  "Which kind of vaccine prevents Haemophilus influenzae type b disease?",
  ("A subunit vaccine",
   "Correct: the vaccine against Haemophilus influenzae type b (Hib) is a subunit vaccine."),
  [("An acellular toxoid vaccine",
    "An acellular vaccine of toxoid and other antigens is the pertussis component of DTaP (diphtheria, tetanus and acellular pertussis); Hib is a subunit "
    "vaccine.", "adjacent fact from the same lecture (pertussis)"),
   ("An oral four-dose vaccine",
    "An oral vaccine given in 4 doses protects against typhoid fever; the Hib vaccine is a subunit vaccine.",
    "adjacent fact from the same lecture (typhoid)"),
   ("An attenuated vaccine",
    "An attenuated vaccine exists for tularemia; the Haemophilus influenzae type b vaccine is a subunit vaccine.",
    "adjacent fact from the same lecture (tularemia)")],
  c(98, 29, 31, 74)),

Q("Haemophilus", IO1,
  "Which Haemophilus species causes chancroid?",
  ("Haemophilus ducreyi",
   "Correct: Haemophilus ducreyi causes chancroid, a sexually transmitted disease seen primarily in the tropics and "
   "primarily in males."),
  [("Haemophilus aegyptius",
    "Haemophilus aegyptius causes conjunctivitis (pink eye), primarily in children; chancroid is Haemophilus "
    "ducreyi.", "other Haemophilus species"),
   ("Haemophilus influenzae",
    "Haemophilus influenzae causes acute bacterial meningitis, epiglottitis, otitis media and pneumonia; chancroid "
    "is Haemophilus ducreyi.", "other Haemophilus species"),
   ("Haemophilus parainfluenzae",
    "Haemophilus parainfluenzae is normal oral and nasopharyngeal flora that can cause infective endocarditis; "
    "chancroid is Haemophilus ducreyi.", "other Haemophilus species")],
  c(100, 98)),

Q("Haemophilus", IO2,
  "How is the acute conjunctivitis of Haemophilus aegyptius spread?",
  ("By contaminated fingers and insects",
   "Correct: Haemophilus aegyptius conjunctivitis (pink eye), primarily in children, is spread by contaminated "
   "fingers and insects and treated with antibiotic eyedrops."),
  [("By sexual contact in the tropics",
    "Sexual spread, primarily in the tropics, is chancroid from Haemophilus ducreyi; pink eye is spread by "
    "contaminated fingers and insects.", "other Haemophilus species"),
   ("By dental procedures",
    "Routine dental procedures let the oral Haemophilus parainfluenzae and aphrophilus cause endocarditis; pink eye "
    "is spread by fingers and insects.", "other Haemophilus species"),
   ("By swimming in fresh water",
    "Swimming is linked to Pseudomonas aeruginosa otitis externa, swimmer's ear; Haemophilus aegyptius pink eye is "
    "spread by fingers and insects.", "adjacent fact from the same lecture (Pseudomonas)")],
  ci(101, 100, 19)),

Q("Haemophilus", IO2,
  "How do Haemophilus parainfluenzae and Haemophilus aphrophilus reach the heart to cause infective endocarditis?",
  ("From the mouth during dental work",
   "Correct: these normal oral and nasopharyngeal flora can cause infective endocarditis in congenital and "
   "rheumatic heart disease, arising from routine dental procedures."),
  [("Through bites of household pets",
    "Animal bites and scratches spread Pasteurella multocida; these Haemophilus species come from the mouth during "
    "routine dental procedures.", "adjacent fact from the same lecture (Pasteurella)"),
   ("From contaminated catheters",
    "Catheters are linked to Providencia and Escherichia coli urinary tract infections; these Haemophilus species "
    "come from the mouth during dental work.", "adjacent fact from the same lecture (catheter infections)"),
   ("Through sexual contact",
    "Sexual contact spreads chancroid, Haemophilus ducreyi; these two species are oral flora carried in during "
    "routine dental procedures.", "other Haemophilus species")],
  c(100, 65, 72, 96)),
]
