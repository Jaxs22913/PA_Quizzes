# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 14 — Gram-Negative Bacilli of Medical Importance (Dr. Webster, 23 October 2026),
# pool A: endotoxin, the differentiation scheme and the AEROBIC NONENTERIC bacilli (deck slides 3-42):
# Pseudomonas aeruginosa, its relatives (Burkholderia, Acinetobacter, Stenotrophomonas), Brucella, Francisella,
# Bordetella pertussis and Legionella. Pool B (tools/micro_l14_pool_b.py) holds the enterics, Yersinia pestis,
# Pasteurella and Haemophilus.
#
# ATTRIBUTION: the deck file is "Lecture 14  Dr. Webster Gram Negative Bacilli of Medical Importance.pptx" and the
# calendar row for 23 October 2026 (1-4 pm) names Dr. Webster; the title slide names no lecturer. 101 slides.
#
# PHASE 1, FROM THE DECK ALONE. The recording (a classmate's, three segments, 2:03:43) is being transcribed; until
# it is read, weights are slide counts and nothing here rests on what was said. Every key and every explanation
# is from the VISIBLE slides, text and pictures (the deck has no speaker notes). Picture-only content used:
# slide 5 (lipid A "most responsible for pathogenesis"), slide 6 (smooth, semi-rough and rough
# lipopolysaccharide), slide 12 (Table 20.1, the Gram-negative scheme), slide 16 (the pigment plates), slide 44
# (toxigenic against invasive diarrhea), slide 47 (the enteric biochemical tree), slide 53 (the H, K and O
# antigens), slide 64 (Rainbow agar), slide 67 (the Klebsiella capsule), slide 71 (Proteus swarming), slide 74
# (the typhoid route), slide 82 (Yersinia pestis bipolar staining), slide 84 (the plague cycle).
#
# Four options throughout. KEYS SHORT and explanations FULL. Every key is authored at position 0 with the only
# "Correct:" opener; tools/micro_l14_partition.py rotates positions per set. `mis` names the misconception each
# distractor stands for (review metadata for tools/blind_review.py; the renderer strips it).
#
# DELIBERATELY NOT ASKED (held), and why:
#   - percentages, case counts, infective doses, outbreak dates and the Florida and national tallies (slides 17,
#     22, 29, 30, 33-36, 40, 42, 45, 56, 60-63, 65, 74-78, 83, 85-87, 91-93): trivia, and in her Exam 2 lectures
#     Dr. Webster said percentages are not tested (Lecture 10). Facts on those slides that are not numbers (an
#     outbreak traced to a decorative fountain = aerosols; infants under 2 months cannot be vaccinated) ARE used.
#   - WHICH ANTIBIOTIC treats what: in Lecture 10 she said she would not ask which antibiotics to use, and drug
#     doses (slide 56) are never asked. Non-drug methods (fluid and electrolyte therapy, dialysis, plasmapheresis,
#     vaccines, quarantine, breast feeding, "antibiotic therapy may exacerbate" hemolytic uremic syndrome,
#     combination therapy for multidrug resistance) ARE asked. The recording may change this.
#   - "Motile, oxidase positive" for Burkholderia, Acinetobacter and Stenotrophomonas as a group (slide 21): the
#     slide gives it to all three, but Acinetobacter is in fact nonmotile and oxidase negative, and Lecture 9 taught
#     it among the Gram-negative cocci. "Obligate aerobes; do not ferment sugars" is asked instead.
#   - the WHO "top 3 critical pathogens" line (slide 17): the 2024 list moved Pseudomonas aeruginosa down to "high";
#     guide note only.
#   - Haemophilus parainfluenzae as a cause of "childhood meningitis" (slide 97): slide 100 calls it normal oral
#     flora causing endocarditis and slide 98 gives meningitis to Haemophilus influenzae; the deck contradicts
#     itself.
#   - the lactose status of Serratia and Hafnia: slide 50 lists them as coliforms (lactose fermenters) and slide
#     68 calls Serratia a coliform, but Table 20.1 (slide 12) and the biochemical tree (slide 47) put both on the
#     non-lactose-fermenting branch. Serratia is asked only by its red pigment and diseases.
#   - pertactin as the cause of the age pattern (slide 36 says waning immunity; slide 37 offers pertactin-negative
#     strains as "another possible connection"); each is asked on its own slide's terms, never against the other.
# SPELLING: the deck's "Acinetobacter baumanii" is written Acinetobacter baumannii; "Salmonella typhhi" Salmonella
# typhi; "Mecillianam" is not used; "amoebas" is written amebas (US spelling).
SRC = "Lecture 14  Dr. Webster Gram Negative Bacilli of Medical Importance.pptx"


def c(*n):
    return f"{SRC}, Slide " + (str(n[0]) if len(n) == 1 else ", ".join(map(str, n[:-1])) + " and " + str(n[-1]))


def ci(img, *n):
    """cite with a picture slide: c(n...) + ' and image on Slide img'"""
    return (c(*n) + f" and image on Slide {img}") if n else f"{SRC}, image on Slide {img}"


IO1 = ("1 — Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, "
       "clinical manifestations, methods of treatment, and prevention of Gram-negative bacilli of medical importance")
IO2 = ("2 — Describe the modes of transmission by which humans acquire Gram-negative bacilli of medical importance")
IMG = "micro-exam-3-quiz-images"


def Q(topic, io, q, key, wrong, cite, **kw):
    """key = (text, explanation); wrong = [(text, explanation, misconception), x3]. Key authored at 0."""
    assert len(wrong) == 3, q
    d = dict(topic=topic, io=io, q=q,
             opts=[[key[0], key[1]]] + [[t, e] for t, e, _ in wrong],
             mis={t: m for t, _, m in wrong}, c=0, cite=cite)
    d.update(kw)
    return d


POOL_A = [

# ============================================================== ENDOTOXIN (slides 5-11)
Q("Endotoxin", IO1,
  "Which component of the Gram-negative lipopolysaccharide is its biologically active part?",
  ("Lipid A",
   "Correct: lipid A is the biologically active component of the lipopolysaccharide complex, the part most "
   "responsible for pathogenesis."),
  [("O antigen",
    "The O antigen is the outer polysaccharide, unique for each organism; it identifies the organism, while the "
    "biologically active component is lipid A.", "adjacent part of the molecule (identity marker)"),
   ("Core polysaccharide",
    "The core polysaccharide is identical for large groups of bacteria and links lipid A to the O antigen; the "
    "biologically active part is lipid A.", "adjacent part of the molecule"),
   ("Peptidoglycan",
    "Peptidoglycan is the cell wall layer beneath the outer membrane, not part of the lipopolysaccharide; the "
    "active component of endotoxin is lipid A.", "wall layer confused with the lipopolysaccharide")],
  ci(5, 5, 6)),

Q("Endotoxin", IO1,
  "When is endotoxin released from Gram-negative bacteria?",
  ("On cell lysis and during rapid growth",
   "Correct: endotoxin is released on the lysis of Gram-negative cells, including through antibiotic therapy, and "
   "as cells grow and divide, particularly when they are rapidly proliferating."),
  [("By active secretion from living cells",
    "Endotoxin is a structural component of the outer membrane, not a secreted product; it is freed by lysis and "
    "while the cells grow and divide.", "endotoxin confused with a secreted exotoxin"),
   ("When spores germinate in the tissues",
    "These Gram-negative bacilli are non-spore-forming; endotoxin is released when the cells lyse and as they "
    "grow and divide rapidly.", "spore biology borrowed from the Gram-positive bacilli"),
   ("When the cells enter a resting phase",
    "Release is tied to lysis and to growth and division, particularly rapid proliferation, rather than to a "
    "resting phase.", "reversed relation to growth")],
  c(5, 13)),

Q("Endotoxin", IO1,
  "Why can antibiotic therapy of a Gram-negative infection itself release endotoxin?",
  ("Killing the cells lyses them",
   "Correct: endotoxin is part of the Gram-negative outer membrane and is released on the lysis of the cells, "
   "including lysis brought about by antibiotic therapy."),
  [("The drug switches on toxin genes",
    "Endotoxin is not a gene product switched on by the drug; it is the lipopolysaccharide already in the outer "
    "membrane, freed when the cells lyse.", "endotoxin confused with an induced exotoxin"),
   ("The drug activates the lipid A",
    "Lipid A is already the biologically active component; the drug does not activate it, it frees it by lysing "
    "the cells.", "misplaced mechanism"),
   ("Dying cells secrete it to defend",
    "Endotoxin is not secreted as a defense; it is a structural component of the outer membrane released as the "
    "cells break apart.", "endotoxin confused with a secreted product")],
  c(5)),

Q("Endotoxin", IO1,
  "Through which kind of host receptor does lipopolysaccharide signal the innate immune system?",
  ("A Toll-like receptor",
   "Correct: lipopolysaccharide antigens belong to innate (nonspecific) immunity and interact with host cells "
   "through a lipopolysaccharide binding complex and a Toll-like receptor for signaling."),
  [("The T-cell receptor",
    "The T-cell receptor belongs to specific, adaptive immunity; lipopolysaccharide is an innate antigen that "
    "signals through a Toll-like receptor.", "adaptive receptor confused with an innate one"),
   ("An immunoglobulin E receptor",
    "Immunoglobulin E receptors arm mast cells in allergy; lipopolysaccharide signals the innate system through a "
    "binding complex and a Toll-like receptor.", "allergy receptor"),
   ("The B-cell receptor",
    "The B-cell receptor is antibody on a B cell, part of the specific response; lipopolysaccharide is sensed "
    "innately, through a Toll-like receptor.", "adaptive receptor confused with an innate one")],
  c(7)),

Q("Endotoxin", IO1,
  "Under most circumstances, what does the host response to lipopolysaccharide at a mucosal surface produce?",
  ("A moderated, protective inflammation",
   "Correct: usually it produces a moderated inflammatory response that protects the host, keeping most mucosal "
   "infections mucosal and helping maintain our symbiosis with some Gram-negative bacilli."),
  [("Immediate septic shock",
    "Septic shock follows a large flood of endotoxin, not the usual mucosal contact; under most circumstances the "
    "response is moderated and protective.", "extreme outcome taken as the usual one"),
   ("No response, as it is hidden",
    "The outer membrane and its lipopolysaccharide are the first thing gut and airway epithelium meets; it is "
    "recognized by innate immunity, not hidden.", "reversed: lipopolysaccharide is the first contact"),
   ("Disseminated intravascular coagulation",
    "Coagulation damage is a potential effect when endotoxin interacts with clotting systems, not the usual "
    "mucosal outcome, which is a moderated, protective inflammation.", "potential damage taken as the usual outcome")],
  c(7, 8, 9)),

Q("Endotoxin", IO1,
  "In chronic Gram-negative infections, how have some bacteria adapted to evade the immune system?",
  ("By altering their lipopolysaccharide",
   "Correct: in chronic Gram-negative infections, some bacteria have adapted by modifying their lipopolysaccharide "
   "to evade the immune system."),
  [("By forming endospores",
    "These bacilli are non-spore-forming; the adaptation described for chronic infection is a modified "
    "lipopolysaccharide.", "spore biology borrowed from the Gram-positive bacilli"),
   ("By shedding their outer membrane",
    "The outer membrane holds the lipopolysaccharide and is kept; the adaptation is to modify the "
    "lipopolysaccharide itself.", "structure lost instead of modified"),
   ("By secreting more endotoxin",
    "Endotoxin is a membrane component rather than a secretion, and more of it would provoke more inflammation; the "
    "evasion is a modified lipopolysaccharide.", "endotoxin confused with a secreted product")],
  c(7, 13)),

Q("Endotoxin", IO1,
  "Which change in the circulation marks warm shock, the early stage after a large flood of endotoxin?",
  ("Arterioles dilate and output rises",
   "Correct: arteries and arterioles dilate, peripheral arterial resistance falls and cardiac output initially "
   "increases, called warm shock; later cardiac output decreases and blood pressure falls."),
  [("Arterioles constrict and output falls",
    "Constriction with falling output is not the early picture; in warm shock the vessels dilate and cardiac output "
    "initially increases.", "reversed direction"),
   ("Output falls and pressure drops",
    "A falling cardiac output and blood pressure come later; warm shock is the earlier stage, when dilation lowers "
    "resistance and output initially rises.", "later stage taken for the early one"),
   ("Resistance rises and output rises",
    "Peripheral arterial resistance falls, not rises, as arteries and arterioles dilate; it is cardiac output that "
    "initially increases.", "one variable reversed")],
  c(11)),

Q("Endotoxin", IO1,
  "Which mediator triggered by endotoxin acts as a vasodilator in shock?",
  ("Bradykinin",
   "Correct: endotoxin may trigger production of bradykinin, a vasodilator in shock, alongside its coagulation "
   "effects such as disseminated intravascular coagulation."),
  [("Fibrin",
    "Fibrin is deposited in the lungs, liver and spleen when endotoxin starts coagulation changes; the vasodilator "
    "it triggers is bradykinin.", "coagulation product confused with the vasodilator"),
   ("Collagenase",
    "Collagenase is one of the mediators macrophages release in response to endotoxin; the vasodilator named for "
    "endotoxic shock is bradykinin.", "other macrophage mediator"),
   ("Colony stimulating factor",
    "Colony stimulating factor is a macrophage mediator induced by endotoxin; the vasodilator in shock is "
    "bradykinin.", "other macrophage mediator")],
  c(9, 10)),

Q("Endotoxin", IO1,
  "How do HIGH levels of endotoxin affect neutrophils?",
  ("They interfere with chemotaxis",
   "Correct: low levels of endotoxin may enhance phagocytosis, but higher levels may interfere with the chemotaxis "
   "of neutrophils to the site of infection."),
  [("They enhance phagocytosis",
    "Enhanced phagocytosis is the effect of LOW levels; higher levels interfere with neutrophil chemotaxis to the "
    "site of infection.", "low-dose effect given for high dose"),
   ("They release interleukin 1 and 6",
    "Interleukin 1 and interleukin 6 are among the mediators endotoxin induces from macrophages; in neutrophils, "
    "high levels interfere with chemotaxis.", "cell confusion (macrophage mediators)"),
   ("They aggregate like platelets",
    "Aggregation is endotoxin's effect on platelets, and it differs among species; on neutrophils, high levels "
    "interfere with chemotaxis.", "cell confusion (platelet effect)")],
  c(10)),

# ============================================================== CLASSIFICATION (slides 12-13)
Q("Classification", IO1,
  "Which three properties are used to differentiate the Gram-negative bacilli?",
  ("Oxygen, lactose and oxidase",
   "Correct: Gram-negative bacilli are differentiated by oxygen requirements (aerobic, facultatively anaerobic, "
   "obligate anaerobic), the ability to ferment lactose, and the oxidase enzyme."),
  [("Spores, acid-fastness and capsule",
    "These Gram-negative bacilli are non-spore-forming, and acid-fastness is not on the list; they are sorted by "
    "oxygen requirement, lactose fermentation and oxidase.", "Gram-positive sorting scheme"),
   ("Catalase, coagulase and hemolysis",
    "None of these three is a sorting property here (all enterics are catalase positive); the three are oxygen "
    "requirement, lactose fermentation and oxidase.", "cocci sorting scheme"),
   ("Shape, size and pigment",
    "Pigment marks some species, such as the greenish-blue of Pseudomonas aeruginosa, but is not a sorting axis; the "
    "three are oxygen, lactose fermentation and oxidase.", "identifying traits taken as the scheme")],
  c(12, 13, 46)),

Q("Classification", IO1,
  "In the scheme for Gram-negative pathogens, which genus is the obligate anaerobe?",
  ("Bacteroides",
   "Correct: the obligate anaerobes branch of the Gram-negative rods holds Bacteroides; the aerobes include "
   "Pseudomonas, and the facultative anaerobes include Escherichia and Haemophilus."),
  [("Pseudomonas",
    "Pseudomonas is on the aerobic branch, the rods that do not ferment carbohydrates; the obligate anaerobe in the "
    "scheme is Bacteroides.", "aerobe taken for an anaerobe"),
   ("Escherichia",
    "Escherichia is a facultative anaerobe that ferments lactose; the obligate anaerobe in the scheme is "
    "Bacteroides.", "facultative anaerobe taken for an obligate one"),
   ("Haemophilus",
    "Haemophilus is a facultative anaerobe on the non-lactose-fermenting, oxidase-positive branch; the obligate "
    "anaerobe is Bacteroides.", "facultative anaerobe taken for an obligate one")],
  ci(12)),

Q("Classification", IO1,
  "Which Gram-negative rods belong to the aerobic group that does not ferment carbohydrates?",
  ("Pseudomonas and Bordetella",
   "Correct: the aerobes that do not ferment carbohydrates include Pseudomonas, Burkholderia, Bordetella, "
   "Francisella, Brucella and Alcaligenes."),
  [("Escherichia and Klebsiella",
    "Escherichia and Klebsiella are facultative anaerobes that ferment lactose, the coliforms; the aerobic "
    "non-fermenters include Pseudomonas and Bordetella.", "coliforms taken for aerobic non-fermenters"),
   ("Salmonella and Shigella",
    "Salmonella and Shigella are facultative anaerobes that ferment carbohydrates but not lactose, on the "
    "oxidase-negative branch.", "non-lactose fermenters taken for non-fermenters"),
   ("Haemophilus and Pasteurella",
    "Haemophilus and Pasteurella are facultative anaerobes on the non-lactose-fermenting, oxidase-positive "
    "branch, not aerobic non-fermenters.", "oxidase-positive fermenters")],
  ci(12)),

Q("Classification", IO1,
  "Which two genera of aerobic nonenteric Gram-negative bacilli are zoonotic pathogens?",
  ("Brucella and Francisella",
   "Correct: among the aerobic nonenteric bacilli, Brucella and Francisella are the zoonotic pathogens; Pseudomonas "
   "and Burkholderia are opportunists, and Bordetella and Legionella mainly human pathogens."),
  [("Pseudomonas and Burkholderia",
    "Pseudomonas and Burkholderia are the opportunistic pathogens of this group; the zoonotic pair is Brucella "
    "and Francisella.", "opportunists taken for zoonoses"),
   ("Bordetella and Legionella",
    "Bordetella and Legionella are mainly human pathogens; the zoonotic pair is Brucella and Francisella.",
    "human pathogens taken for zoonoses"),
   ("Escherichia and Klebsiella",
    "Escherichia and Klebsiella are coliform enterics, facultative anaerobes rather than aerobic nonenteric "
    "bacilli; the zoonotic pair is Brucella and Francisella.", "wrong group (enterics)")],
  c(13)),

Q("Classification", IO1,
  "Which offensive weapon do ALL the aerobic Gram-negative nonenteric bacilli use?",
  ("Endotoxin",
   "Correct: this large, diverse group of non-spore-forming bacteria all use endotoxin as one of their offensive "
   "weapons."),
  [("Exotoxin A",
    "Exotoxin A is a Pseudomonas aeruginosa toxin that inhibits protein synthesis, not a weapon of the whole "
    "group; all of them use endotoxin.", "one species' toxin generalized"),
   ("Shiga toxin",
    "Shiga toxin belongs to Shigella and enterohemorrhagic Escherichia coli, which are enterics; the aerobic "
    "nonenteric bacilli all use endotoxin.", "enteric toxin"),
   ("Pyocyanin",
    "Pyocyanin is the greenish-blue pigment of Pseudomonas aeruginosa, not a shared weapon; all the aerobic "
    "nonenteric bacilli use endotoxin.", "one species' pigment generalized")],
  c(13, 17, 18, 59)),

# ============================================================== PSEUDOMONAS AERUGINOSA (slides 14-20)
Q("Pseudomonas aeruginosa", IO1,
  "How is a Pseudomonas cell flagellated?",
  ("One polar flagellum",
   "Correct: pseudomonads are small Gram-negative rods with a single polar flagellum, which also helps cells in "
   "biofilms adhere."),
  [("Peritrichous flagella",
    "Peritrichous flagella, all around the cell, belong to the highly motile Proteus; pseudomonads carry a single "
    "polar flagellum.", "adjacent fact from the same lecture (Proteus)"),
   ("Not flagellated",
    "Pseudomonads are motile: each small rod has a single polar flagellum, and cells in biofilms adhere by flagella "
    "and pili.", "motility denied"),
   ("A tuft at both ends",
    "A tuft at each end is not the pseudomonad pattern; the small rod carries one polar flagellum.",
    "invented arrangement")],
  ci(15, 14, 17, 71)),

Q("Pseudomonas aeruginosa", IO1,
  "Which metabolic profile fits Pseudomonas?",
  ("Aerobic respiration, no fermentation",
   "Correct: pseudomonads use aerobic respiration and do not ferment carbohydrates; they produce oxidase and "
   "catalase."),
  [("Ferments lactose, like coliforms",
    "Lactose fermentation defines the coliform enterics; Pseudomonas does not ferment carbohydrates and relies on "
    "aerobic respiration.", "coliform trait"),
   ("Obligate anaerobic fermentation",
    "The obligate anaerobe of the Gram-negative scheme is Bacteroides; Pseudomonas uses aerobic respiration.",
    "reversed oxygen requirement"),
   ("Ferments glucose, oxidase negative",
    "Glucose fermentation with a negative oxidase describes the Enterobacteriaceae; Pseudomonas does not ferment "
    "carbohydrates and produces oxidase.", "enteric trait")],
  c(14, 46)),

Q("Pseudomonas aeruginosa", IO1,
  "Which pigment gives Pseudomonas aeruginosa its greenish-blue color?",
  ("Pyocyanin",
   "Correct: Pseudomonas aeruginosa produces the greenish-blue pigment pyocyanin, and it has a grapelike odor; many "
   "pseudomonads make water-soluble pigments."),
  [("Prodigiosin",
    "Prodigiosin is the red pigment of Serratia marcescens; the greenish-blue pigment of Pseudomonas aeruginosa is "
    "pyocyanin.", "adjacent fact from the same lecture (Serratia)"),
   ("Methylene blue",
    "Methylene blue is a dye in eosin methylene blue agar, which selects for Gram-negative bacteria; the pigment of "
    "Pseudomonas aeruginosa is pyocyanin.", "culture-medium dye taken for a bacterial pigment"),
   ("Crystal violet",
    "Crystal violet is a selective agent in MacConkey's agar, not a bacterial pigment; Pseudomonas aeruginosa makes "
    "pyocyanin.", "culture-medium dye taken for a bacterial pigment")],
  c(18, 14, 48, 68)),

Q("Pseudomonas aeruginosa", IO1,
  "The colonies on this plate have stained the agar greenish-blue. Which organism makes this pigment?",
  ("Pseudomonas aeruginosa",
   "Correct: the greenish-blue color spreading through the agar is pyocyanin, the pigment of Pseudomonas "
   "aeruginosa; many pseudomonads make water-soluble pigments."),
  [("Serratia marcescens",
    "Serratia marcescens makes a red pigment, prodigiosin, rather than a greenish-blue one; that pigment belongs to "
    "Pseudomonas aeruginosa.", "pigmented organism with the wrong color"),
   ("Klebsiella pneumoniae",
    "Klebsiella pneumoniae is recognized by its large capsule, not a pigment; the greenish-blue pigment is "
    "Pseudomonas aeruginosa's pyocyanin.", "other identifying trait"),
   ("Proteus vulgaris",
    "Proteus vulgaris is recognized by its wavelike swarming growth, not a pigment; greenish-blue agar points to "
    "Pseudomonas aeruginosa.", "other identifying trait")],
  ci(16, 14, 18, 67, 68, 71),
  img=IMG + "/l14-fig-01.jpg", alt="An agar plate with paper disks on it; the agar around the growth is stained green.",
  slide="Slide 16"),

Q("Pseudomonas aeruginosa", IO1,
  "In which hosts is Pseudomonas aeruginosa a common cause of nosocomial infection?",
  ("Burns, neoplasms or cystic fibrosis",
   "Correct: Pseudomonas aeruginosa is a common cause of nosocomial infections in hosts with burns, neoplastic "
   "disease and, above all, cystic fibrosis."),
  [("Smoking men over 50 years old",
    "Smoking, being male and being over 50 mark the hosts of Legionnaires disease; Pseudomonas aeruginosa's hosts "
    "have burns, neoplastic disease or cystic fibrosis.", "adjacent fact from the same lecture (Legionella)"),
   ("Infants under two months old",
    "Infants under 2 months, too young to vaccinate, carry the highest pertussis burden; Pseudomonas aeruginosa's "
    "nosocomial hosts have burns, cancer or cystic fibrosis.", "adjacent fact from the same lecture (pertussis)"),
   ("Veterinarians bitten by animals",
    "Animal bites and scratches, mostly in veterinarians, are how Pasteurella multocida infects; Pseudomonas "
    "aeruginosa targets burn, cancer and cystic fibrosis patients.", "adjacent fact from the same lecture (Pasteurella)")],
  c(18, 30, 35, 40, 96)),

Q("Pseudomonas aeruginosa", IO2,
  "Why is Pseudomonas aeruginosa a frequent contaminant of ventilators, intravenous solutions and anesthesia equipment?",
  ("It forms biofilms",
   "Correct: its ability to produce biofilms lets it contaminate ventilators, intravenous solutions and anesthesia "
   "equipment; cells in biofilms adhere by flagella and pili and form microcolonies."),
  [("It forms endospores",
    "Pseudomonas forms no spores; it persists on equipment by producing biofilms, and it resists soaps, "
    "disinfectants and drying.", "spore biology borrowed from the Gram-positive bacilli"),
   ("It needs rich nutrients",
    "It survives in nutrient-poor environments rather than needing rich ones; on equipment it persists by forming "
    "biofilms.", "reversed nutritional need"),
   ("It lives inside amebas",
    "Living in close association with amebas is how Legionella persists in water systems; Pseudomonas aeruginosa "
    "contaminates equipment by producing biofilms.", "adjacent fact from the same lecture (Legionella)")],
  c(17, 16, 39)),

Q("Pseudomonas aeruginosa", IO1,
  "What does Pseudomonas aeruginosa exotoxin A do?",
  ("Inhibits protein synthesis",
   "Correct: exotoxin A inhibits protein synthesis; exoenzyme S, by contrast, induces apoptosis of T cells, and the "
   "slime layer resists phagocytosis."),
  [("Induces T-cell apoptosis",
    "Inducing apoptosis of T cells is the work of exoenzyme S; exotoxin A inhibits protein synthesis.",
    "swapped virulence factor"),
   ("Blocks phagocytosis",
    "Resistance to phagocytosis comes from the slime layer, which also forms biofilms; exotoxin A inhibits protein "
    "synthesis.", "swapped virulence factor"),
   ("Degrades phospholipid",
    "Degrading phospholipid is done by some of its exoenzymes; exotoxin A inhibits protein synthesis.",
    "swapped virulence factor")],
  c(17)),

Q("Pseudomonas aeruginosa", IO1,
  "Which is one of the mechanisms behind the multidrug resistance of Pseudomonas aeruginosa?",
  ("Restricted outer membrane entry",
   "Correct: its multidrug resistance comes from restricted outer membrane permeability, antibiotic-inactivating "
   "enzymes, efflux pumps, horizontal transfer of resistance genes and biofilm formation."),
  [("A protective endospore coat",
    "It forms no spores; its resistance rests on restricted outer membrane permeability, inactivating enzymes, "
    "efflux pumps, gene transfer and biofilms.", "spore biology borrowed from the Gram-positive bacilli"),
   ("Persistence inside host cells",
    "Intracellular persistence is what lets tularemia relapse; Pseudomonas aeruginosa's resistance comes from its "
    "outer membrane, enzymes, efflux pumps, gene transfer and biofilms.", "adjacent fact from the same lecture (Francisella)"),
   ("Its greenish-blue pigment",
    "Pyocyanin colors its colonies but is not among its resistance mechanisms; restricted outer membrane "
    "permeability is.", "identifying trait taken for a resistance mechanism")],
  c(17, 18, 29)),

Q("Pseudomonas aeruginosa", IO1,
  "Which infection is typical of Pseudomonas aeruginosa in an otherwise healthy person?",
  ("Swimmer's ear",
   "Correct: in healthy people it typically causes skin rashes, urinary tract infection, otitis externa (swimmer's "
   "ear) and corneal ulcers in contact lens wearers."),
  [("Undulant fever",
    "Undulant fever is brucellosis, caught from infected animals or unpasteurized dairy products; Pseudomonas "
    "aeruginosa gives healthy people otitis externa.", "adjacent fact from the same lecture (Brucella)"),
   ("Whooping cough",
    "Whooping cough is pertussis, caused by Bordetella pertussis; Pseudomonas aeruginosa gives healthy people "
    "swimmer's ear, skin rashes and urinary tract infection.", "adjacent fact from the same lecture (Bordetella)"),
   ("Rabbit fever",
    "Rabbit fever is tularemia, caused by Francisella tularensis; Pseudomonas aeruginosa gives healthy people "
    "otitis externa.", "adjacent fact from the same lecture (Francisella)")],
  c(19, 27, 29, 30)),

Q("Pseudomonas aeruginosa", IO1,
  "Why might a Pseudomonas aeruginosa vaccine harm a patient with cystic fibrosis?",
  ("It may worsen lung inflammation",
   "Correct: because patients with cystic fibrosis often have a chronic infection, vaccination may induce "
   "increased pulmonary inflammation and tissue damage."),
  [("No candidate vaccine exists",
    "Many candidate vaccines are in development and testing, mostly built on antibodies against bacterial protein; "
    "the concern in cystic fibrosis is increased lung inflammation.", "development status reversed"),
   ("It causes the infection itself",
    "The candidates rely on bacterial proteins, such as a porin membrane protein, rather than live infection; the "
    "risk is increased pulmonary inflammation and tissue damage.", "vaccine confused with infection"),
   ("It is delivered through the gut",
    "Mucosal delivery by liposomes and nanoparticles is being studied as a route, not a harm; the concern in cystic "
    "fibrosis is increased pulmonary inflammation and tissue damage.", "delivery route confused with the risk")],
  c(20)),

# ============================================================== PSEUDOMONAS RELATIVES (slides 21-26)
Q("Pseudomonas relatives", IO1,
  "Which description fits Burkholderia, Acinetobacter and Stenotrophomonas?",
  ("Obligate aerobes that do not ferment sugars",
   "Correct: these genera are similar to the pseudomonads: obligate aerobes that do not ferment sugars, found in "
   "soil, water and related environments, and opportunistic pathogens."),
  [("Facultative anaerobes that ferment lactose",
    "Facultative anaerobes that ferment lactose are the coliforms; these relatives of Pseudomonas are obligate "
    "aerobes that do not ferment sugars.", "coliform traits"),
   ("Obligate anaerobes of the bowel",
    "The obligate anaerobe of the Gram-negative scheme is Bacteroides; these relatives of Pseudomonas are obligate "
    "aerobes.", "reversed oxygen requirement"),
   ("Spore-formers living in soil",
    "They live in soil and water but form no spores; they are obligate aerobes that do not ferment sugars, like the "
    "pseudomonads.", "spore biology borrowed from the Gram-positive bacilli")],
  ci(12, 21)),

Q("Pseudomonas relatives", IO1,
  "Burkholderia cepacia is a particular problem in which patients?",
  ("Those with cystic fibrosis",
   "Correct: Burkholderia cepacia, a rapidly mutating, multidrug-resistant opportunist, is a particular problem in "
   "cystic fibrosis, where it is a copathogen with Pseudomonas."),
  [("Soldiers with combat wounds",
    "Infections after traumatic combat wounds belong to Acinetobacter baumannii; Burkholderia cepacia is a "
    "particular problem in cystic fibrosis.", "adjacent fact from the same lecture (Acinetobacter)"),
   ("Patients on dialysis",
    "Dialysis equipment is contaminated by Stenotrophomonas maltophilia biofilms; Burkholderia cepacia is a "
    "particular problem in cystic fibrosis.", "adjacent fact from the same lecture (Stenotrophomonas)"),
   ("Travelers to the tropics",
    "Tropical soil and water carry Burkholderia pseudomallei, the cause of melioidosis; Burkholderia cepacia is a "
    "particular problem in cystic fibrosis.", "species confused within the genus")],
  ci(22, 22, 23, 25, 26)),

Q("Pseudomonas relatives", IO2,
  "How is melioidosis generally acquired?",
  ("Penetrating injury or inhalation",
   "Correct: Burkholderia pseudomallei lives in the soil and water of tropical climates, and melioidosis is "
   "generally acquired through a penetrating injury or by inhalation."),
  [("A tick or flea bite",
    "Melioidosis needs no vector; Burkholderia pseudomallei enters from tropical soil and water through a "
    "penetrating injury or the airways.", "vector-borne route"),
   ("Unpasteurized dairy products",
    "Unpasteurized dairy products spread brucellosis; melioidosis is acquired through a penetrating injury or by "
    "inhalation.", "adjacent fact from the same lecture (Brucella)"),
   ("Undercooked ground beef",
    "Contaminated beef spreads enterohemorrhagic Escherichia coli; melioidosis is acquired through a penetrating "
    "injury or by inhalation.", "adjacent fact from the same lecture (EHEC)")],
  ci(24, 23, 27, 60)),

Q("Pseudomonas relatives", IO1,
  "Which organism causes melioidosis?",
  ("Burkholderia pseudomallei",
   "Correct: Burkholderia pseudomallei, from the soil and water of tropical climates, causes melioidosis: wound "
   "infections with nodules, pneumonia, septicemia, endotoxic shock and liver and brain abscesses."),
  [("Burkholderia cepacia",
    "Burkholderia cepacia is the plant pathogen and opportunist that troubles cystic fibrosis patients; melioidosis "
    "is Burkholderia pseudomallei.", "species confused within the genus"),
   ("Brucella abortus",
    "Brucella abortus is the cattle species that causes brucellosis (undulant fever); melioidosis is Burkholderia "
    "pseudomallei.", "similar-sounding zoonosis"),
   ("Francisella tularensis",
    "Francisella tularensis causes tularemia, rabbit fever; melioidosis is Burkholderia pseudomallei.",
    "other aerobic nonenteric pathogen")],
  c(22, 23, 27, 29)),

Q("Pseudomonas relatives", IO2,
  "Which opportunist survives for months on fomites and infects traumatic wounds such as combat injuries?",
  ("Acinetobacter baumannii",
   "Correct: Acinetobacter baumannii causes nosocomial and community-acquired infections, survives months on "
   "fomites, and infects wounds, lungs, the urinary tract, burns and blood, including after traumatic combat wounds."),
  [("Burkholderia cepacia",
    "Burkholderia cepacia is a rapidly mutating opportunist that troubles cystic fibrosis patients; months on "
    "fomites and combat wounds describe Acinetobacter baumannii.", "other Pseudomonas relative"),
   ("Stenotrophomonas maltophilia",
    "Stenotrophomonas maltophilia forms biofilms that contaminate disinfectants and medical equipment; months on "
    "fomites and combat wounds describe Acinetobacter baumannii.", "other Pseudomonas relative"),
   ("Brucella suis",
    "Brucella suis is the pig species of brucellosis, caught from animals; the fomite survivor of combat wounds is "
    "Acinetobacter baumannii.", "zoonotic pathogen")],
  c(25, 22, 26, 27)),

Q("Pseudomonas relatives", IO2,
  "Which opportunist forms biofilms that contaminate disinfectants, dialysis equipment and catheters?",
  ("Stenotrophomonas maltophilia",
   "Correct: Stenotrophomonas maltophilia, from fresh water, soil and fecal flora, forms biofilms and contaminates "
   "disinfectants, dialysis and respiratory equipment, water dispensers and catheters."),
  [("Burkholderia pseudomallei",
    "Burkholderia pseudomallei lives in tropical soil and water and causes melioidosis after injury or inhalation; "
    "the biofilm contaminant of disinfectants is Stenotrophomonas maltophilia.", "other Pseudomonas relative"),
   ("Brucella abortus",
    "Brucella abortus is the cattle species of brucellosis, a zoonosis; the biofilm contaminant of dialysis "
    "equipment is Stenotrophomonas maltophilia.", "zoonotic pathogen"),
   ("Francisella tularensis",
    "Francisella tularensis causes tularemia from animals, water, dust or vector bites; the contaminant of "
    "disinfectants and catheters is Stenotrophomonas maltophilia.", "zoonotic pathogen")],
  c(26, 23, 27, 29)),

# ============================================================== BRUCELLA (slides 27-28)
Q("Brucella", IO2,
  "How do humans usually acquire brucellosis?",
  ("From infected animals or raw dairy",
   "Correct: brucellosis is a zoonosis of animal handling and slaughtering, spread by contact with the blood, urine "
   "or placentas of infected animals or by unpasteurized dairy products; human-to-human spread is rare."),
  [("From person-to-person droplets",
    "Human-to-human transmission of brucellosis is rare; it comes from infected animals and their unpasteurized "
    "dairy products.", "reversed: human spread is rare"),
   ("From the bite of an infected flea",
    "Flea bites transmit plague; brucellosis comes from contact with infected animals' blood, urine or placentas, "
    "or unpasteurized dairy.", "adjacent fact from the same lecture (plague)"),
   ("From aerosols of cooling towers",
    "Cooling-tower aerosols transmit Legionella; brucellosis comes from infected animals or unpasteurized dairy "
    "products.", "adjacent fact from the same lecture (Legionella)")],
  c(27, 40, 83)),

Q("Brucella", IO1,
  "Why is brucellosis called undulant fever?",
  ("Its fever fluctuates for weeks to a year",
   "Correct: brucellosis is a severe febrile illness whose fever follows a fluctuating pattern over weeks to a "
   "year, the undulant fever, with chills, sweating, headache, muscle pain and weight loss."),
  [("Its fever stays high without a break",
    "A sustained high fever belongs to typhoid fever; the brucellosis fever rises and falls over weeks to a year.",
    "adjacent fact from the same lecture (typhoid)"),
   ("Its fever follows a paroxysmal cough",
    "Paroxysms of cough belong to pertussis; brucellosis is named for a fever that fluctuates over weeks to a "
    "year.", "adjacent fact from the same lecture (pertussis)"),
   ("Its fever lasts a single day",
    "Brucellosis is not a one-day fever; its fever fluctuates over weeks to as long as a year.",
    "duration reversed")],
  c(28, 31, 74)),

Q("Brucella", IO1,
  "Which test is used to diagnose brucellosis?",
  ("An agglutination titer",
   "Correct: brucellosis is tested with a serological test, the agglutination titer test."),
  [("Rainbow agar culture",
    "Rainbow agar is for rapid identification of Escherichia coli O157:H7, whose colonies are black; brucellosis is "
    "diagnosed by an agglutination titer.", "adjacent fact from the same lecture (EHEC)"),
   ("Bubo aspiration",
    "Aspirating the buboes is how plague is diagnosed; brucellosis is diagnosed serologically, by an agglutination "
    "titer.", "adjacent fact from the same lecture (plague)"),
   ("Charcoal yeast extract agar",
    "Charcoal yeast extract agar grows Legionella; brucellosis is diagnosed serologically, by an agglutination "
    "titer test.", "adjacent fact from the same lecture (Legionella)")],
  c(28, 41, 64, 90)),

Q("Brucella", IO2,
  "Which animals carry Brucella abortus and Brucella suis?",
  ("Cattle and pigs",
   "Correct: Brucella abortus is the cattle species and Brucella suis the pig species, two species of tiny "
   "Gram-negative coccobacilli."),
  [("Rodents and their fleas",
    "Rodents and their fleas carry Yersinia pestis, the plague; the brucellae are Brucella abortus in cattle and "
    "Brucella suis in pigs.", "adjacent fact from the same lecture (plague)"),
   ("Reptiles and poultry",
    "Reptiles and poultry spread the animal salmonelloses; Brucella abortus is in cattle and Brucella suis in "
    "pigs.", "adjacent fact from the same lecture (Salmonella)"),
   ("Rabbits and hares",
    "Rabbits carry tularemia, rabbit fever; Brucella abortus is in cattle and Brucella suis in pigs.",
    "adjacent fact from the same lecture (Francisella)")],
  c(27, 29, 76, 83)),

Q("Brucella", IO1,
  "Which form of vaccine is available for brucellosis?",
  ("An animal vaccine",
   "Correct: an animal vaccine is available for brucellosis; the disease is also a potential bioweapon."),
  [("A human subunit vaccine",
    "A subunit vaccine is the Haemophilus influenzae type b (Hib) vaccine; for brucellosis, the vaccine available is "
    "for animals.", "adjacent fact from the same lecture (Haemophilus)"),
   ("A human oral vaccine",
    "The oral vaccine in this group protects against typhoid fever; for brucellosis, an animal vaccine is "
    "available.", "adjacent fact from the same lecture (typhoid)"),
   ("A human acellular vaccine",
    "The acellular vaccine is the pertussis component of DTaP (diphtheria, tetanus and acellular pertussis); for "
    "brucellosis, an animal vaccine is available.", "adjacent fact from the same lecture (pertussis)")],
  c(28, 31, 74, 98)),

# ============================================================== FRANCISELLA (slide 29)
Q("Francisella", IO1,
  "Tularemia is also known by which name?",
  ("Rabbit fever",
   "Correct: tularemia, caused by Francisella tularensis, is rabbit fever, a zoonosis of mammals endemic to the "
   "northern hemisphere, particularly rabbits."),
  [("Undulant fever",
    "Undulant fever is brucellosis, named for its fluctuating fever; tularemia is rabbit fever.",
    "adjacent fact from the same lecture (Brucella)"),
   ("Malta fever",
    "Malta fever is another name for brucellosis; tularemia is rabbit fever, caused by Francisella tularensis.",
    "adjacent fact from the same lecture (Brucella)"),
   ("Pontiac fever",
    "Pontiac fever is one of the two illnesses Legionella causes; tularemia is rabbit fever.",
    "adjacent fact from the same lecture (Legionella)")],
  c(29, 27, 40)),

Q("Francisella", IO2,
  "By which routes is tularemia transmitted?",
  ("Animals, water, dust or vector bites",
   "Correct: tularemia is transmitted by contact with infected animals, by water and dust, or by the bites of "
   "vectors."),
  [("Mainly from person to person",
    "Tularemia is a zoonosis of mammals, especially rabbits; it spreads from animals, water and dust or vector "
    "bites, not mainly between people.", "zoonosis taken for a human-to-human disease"),
   ("Unpasteurized milk and cheese",
    "Unpasteurized dairy products spread brucellosis; tularemia comes from infected animals, water and dust or "
    "vector bites.", "adjacent fact from the same lecture (Brucella)"),
   ("Contaminated hospital equipment",
    "Contaminated equipment spreads opportunists such as Pseudomonas aeruginosa and Stenotrophomonas; tularemia "
    "comes from animals, water, dust or vector bites.", "adjacent fact from the same lecture (opportunists)")],
  c(29, 17, 26, 27)),

Q("Francisella", IO1,
  "Why can tularemia relapse?",
  ("It persists inside host cells",
   "Correct: the intracellular persistence of Francisella tularensis can lead to relapse."),
  [("Its spores survive in the soil",
    "Francisella forms no spores, like the other aerobic nonenteric bacilli; relapse comes from its intracellular "
    "persistence.", "spore biology borrowed from the Gram-positive bacilli"),
   ("Its vaccine immunity wanes",
    "Waning vaccine immunity is the pattern behind rising pertussis; tularemia relapses because Francisella "
    "persists inside cells.", "adjacent fact from the same lecture (pertussis)"),
   ("It hides in the gallbladder",
    "Gallbladder carriage is how chronic typhoid carriers shed Salmonella typhi; tularemia relapses because "
    "Francisella persists inside cells.", "adjacent fact from the same lecture (typhoid)")],
  c(29, 13, 36, 73)),

# ============================================================== BORDETELLA PERTUSSIS (slides 30-37)
Q("Bordetella", IO1,
  "What does Bordetella pertussis bind to in the respiratory tract?",
  ("Ciliated epithelial cells",
   "Correct: its receptors recognize and bind ciliated respiratory epithelial cells, and its toxins destroy and "
   "dislodge them."),
  [("Peyer's patches of the gut",
    "Peyer's patches are entered by Shigella in the large intestine; Bordetella pertussis binds ciliated "
    "respiratory epithelial cells.", "adjacent fact from the same lecture (Shigella)"),
   ("Intestinal villus cells",
    "Intestinal villi are the target of enteric bacteria such as Salmonella and Shigella; Bordetella pertussis binds "
    "ciliated respiratory epithelium.", "enteric target"),
   ("Renal tubular cells",
    "Renal tubular epithelial cells are killed by the toxins of enterohemorrhagic Escherichia coli in hemolytic "
    "uremic syndrome; Bordetella pertussis binds ciliated airway cells.", "adjacent fact from the same lecture (EHEC)")],
  c(31, 60, 73, 78)),

Q("Bordetella", IO1,
  "Why does mucus build up and block the airways in pertussis?",
  ("The ciliary mechanism is lost",
   "Correct: the toxins destroy and dislodge ciliated cells, and the loss of the ciliary mechanism leads to a "
   "buildup of mucus and blockage of the airways."),
  [("Its capsule plugs the airways",
    "Bordetella pertussis is encapsulated, but the blockage comes from mucus that builds up once the ciliary "
    "mechanism is destroyed.", "virulence factor misapplied"),
   ("Phagocytes flood the bronchi",
    "Its toxins destroy phagocyte activity rather than drawing phagocytes in; the mucus builds up because the "
    "ciliated cells are lost.", "reversed effect on phagocytes"),
   ("Fibrin coats the airway lining",
    "Fibrin deposition in the lungs is an endotoxin coagulation effect; in pertussis, mucus builds up because the "
    "ciliary mechanism is lost.", "adjacent fact from the same lecture (endotoxin)")],
  c(31, 30, 9)),

Q("Bordetella", IO1,
  "Which stage of pertussis brings a recurrent persistent cough followed by a deep inhalation, the whoop?",
  ("Paroxysmal",
   "Correct: in the paroxysmal stage, a recurrent persistent cough is followed by a deep inhalation, the whoop; the "
   "catarrhal stage before it brings nasal drainage, congestion, sneezing and an occasional cough."),
  [("Catarrhal",
    "The catarrhal stage is the earlier one, with nasal drainage, congestion, sneezing and an occasional cough; "
    "the whoop belongs to the paroxysmal stage.", "earlier stage"),
   ("Septicemic",
    "Septicemic is a form of plague, with massive bacterial growth, purpura and gangrene; the whooping stage of "
    "pertussis is paroxysmal.", "adjacent fact from the same lecture (plague)"),
   ("Pneumonic",
    "Pneumonic is the lung form of plague, spread by aerosol; the whooping stage of pertussis is paroxysmal.",
    "adjacent fact from the same lecture (plague)")],
  c(31, 88)),

Q("Bordetella", IO1,
  "What does the acellular pertussis vaccine in DTaP (diphtheria, tetanus and acellular pertussis) contain?",
  ("Toxoid and other antigens",
   "Correct: DTaP is an acellular vaccine containing toxoid and other antigens, given as a five-dose series between "
   "2 months and 6 years."),
  [("Whole killed bacteria",
    "DTaP is acellular, so it carries no whole cells; it contains toxoid and other antigens.",
    "whole-cell vaccine"),
   ("Live attenuated bacteria",
    "No live organism is in DTaP; it is an acellular vaccine of toxoid and other antigens.",
    "live vaccine"),
   ("Ready-made antitoxin antibody",
    "DTaP stimulates the child's own immunity with toxoid and other antigens; it does not carry ready-made "
    "antibody.", "passive immunization confused with a vaccine")],
  c(31)),

Q("Bordetella", IO1,
  "Why is pertussis incidence highest among babies under 1 year old?",
  ("They are too young to be vaccinated",
   "Correct: average incidence is highest among children under 1 year because infants less than 2 months old "
   "cannot get vaccinated."),
  [("They are the main healthy carriers",
    "The reservoir is apparently healthy carriers in general, not infants in particular; infants suffer most "
    "because the youngest cannot yet be vaccinated.", "reservoir confused with the most affected"),
   ("Their boosters have worn off",
    "Waning immunity after childhood vaccination drives the rise in older children and adolescents; the youngest "
    "infants have had no vaccine yet.", "older-age pattern applied to infants"),
   ("They receive a whole-cell vaccine",
    "Infants are given the acellular DTaP (diphtheria, tetanus and acellular pertussis) series, not a whole-cell vaccine; the highest incidence is in infants too "
    "young (under 2 months) to vaccinate.", "vaccine type confused")],
  c(35, 30, 31, 36)),

Q("Bordetella", IO1,
  "What does the age pattern of rising pertussis cases in older children and adolescents reflect?",
  ("Waning immunity, needing boosters",
   "Correct: the pattern reflects waning immunity from childhood vaccinations and the need for booster doses, such "
   "as Boostrix for ages 10 to 18."),
  [("A new animal reservoir",
    "Pertussis has no animal reservoir; its reservoir is apparently healthy human carriers, and the pattern reflects "
    "waning immunity.", "zoonosis assumed"),
   ("Spread from contaminated water",
    "Pertussis spreads by direct contact or inhaled aerosols, not water; the pattern reflects waning immunity from "
    "childhood vaccination.", "waterborne route assumed"),
   ("Infants being vaccinated late",
    "Infants too young for the vaccine drive the incidence under 1 year; in older children and adolescents, the "
    "pattern reflects waning immunity and the need for boosters.", "infant pattern applied to adolescents")],
  c(36, 30, 31, 35)),

Q("Bordetella", IO1,
  "Which Bordetella pertussis adhesion protein, long a vaccine component, is missing from newly developing strains?",
  ("Pertactin",
   "Correct: pertactin assists the adhesion of the pertussis bacterium to airway linings and has been a component of "
   "vaccines; pertactin-negative strains are developing, a possible connection to the rise of pertussis."),
  [("Exotoxin A",
    "Exotoxin A is the Pseudomonas aeruginosa toxin that inhibits protein synthesis; the pertussis adhesion protein "
    "in vaccines is pertactin.", "adjacent fact from the same lecture (Pseudomonas)"),
   ("Porin OprH",
    "OprH is a Pseudomonas aeruginosa porin membrane protein in a candidate Pseudomonas vaccine; the pertussis "
    "adhesion protein is pertactin.", "adjacent fact from the same lecture (Pseudomonas vaccine)"),
   ("Shiga toxin",
    "Shiga toxin belongs to Shigella and enterohemorrhagic Escherichia coli; the pertussis adhesion protein is "
    "pertactin.", "adjacent fact from the same lecture (Shigella)")],
  c(37, 17, 20, 59)),

Q("Bordetella", IO2,
  "How is Bordetella pertussis transmitted?",
  ("Contact or inhaled aerosols",
   "Correct: from a reservoir of apparently healthy carriers, pertussis is transmitted by direct contact or by "
   "inhaling aerosols."),
  [("Bites of infected fleas",
    "Flea bites transmit plague; pertussis spreads by direct contact or by inhaled aerosols.",
    "adjacent fact from the same lecture (plague)"),
   ("Contaminated food or water",
    "Fecally contaminated food and water spread the enterics such as Salmonella and Shigella; pertussis spreads by "
    "contact or aerosols.", "enteric route"),
   ("Animal bites or scratches",
    "Animal bites and scratches spread Pasteurella multocida; pertussis spreads by direct contact or by inhaled "
    "aerosols.", "adjacent fact from the same lecture (Pasteurella)")],
  c(30, 73, 78, 83, 96)),

Q("Bordetella", IO2,
  "What is the reservoir of Bordetella pertussis?",
  ("Apparently healthy carriers",
   "Correct: the reservoir of pertussis is apparently healthy carriers, from whom it spreads by direct contact or "
   "aerosols."),
  [("Rodents and their fleas",
    "Rodents and their fleas are the reservoir and vectors of Yersinia pestis; pertussis is carried by apparently "
    "healthy people.", "adjacent fact from the same lecture (plague)"),
   ("The intestines of cattle",
    "Cattle intestines are the reservoir of Escherichia coli O157:H7; pertussis is carried by apparently healthy "
    "people.", "adjacent fact from the same lecture (EHEC)"),
   ("Water cooling towers",
    "Cooling towers harbor Legionella; the reservoir of pertussis is apparently healthy carriers.",
    "adjacent fact from the same lecture (Legionella)")],
  c(30, 39, 60, 83)),

# ============================================================== LEGIONELLA (slides 39-42)
Q("Legionella", IO1,
  "With which organisms does Legionella pneumophila live in water systems?",
  ("Amebas",
   "Correct: Legionella is widely distributed in water (tap water, cooling towers, spas, ponds, air conditioning, "
   "supermarket vegetable sprayers) and lives in close association with amebas."),
  [("Fleas",
    "Fleas are the vectors of Yersinia pestis, not partners of Legionella; Legionella lives in close association "
    "with amebas.", "adjacent fact from the same lecture (plague)"),
   ("Turtles",
    "Small pet turtles carry Salmonella, not Legionella; Legionella lives in water in close association with "
    "amebas.", "adjacent fact from the same lecture (Salmonella)"),
   ("Cattle",
    "Cattle intestines are the reservoir of Escherichia coli O157:H7; Legionella lives in water in close "
    "association with amebas.", "adjacent fact from the same lecture (EHEC)")],
  ci(41, 39, 60, 77, 83)),

Q("Legionella", IO2,
  "How is legionellosis transmitted?",
  ("By inhaling aerosols",
   "Correct: legionellosis is transmitted by aerosols from water sources such as cooling towers, spas, air "
   "conditioning and decorative fountains."),
  [("By drinking tap water",
    "Tap water can harbor Legionella, but the disease is transmitted by aerosols, the spray from cooling towers, "
    "spas and fountains.", "source confused with route"),
   ("By tick and flea bites",
    "No vector carries legionellosis; it is transmitted by aerosols from water sources.", "vector-borne route"),
   ("By eating raw vegetables",
    "Supermarket vegetable spraying systems are a source because they make aerosols; legionellosis is "
    "transmitted by inhaling aerosols, not by eating.", "source confused with route")],
  c(40, 39, 42)),

Q("Legionella", IO1,
  "On which medium is Legionella pneumophila grown?",
  ("Charcoal yeast extract agar",
   "Correct: Legionella cannot be easily cultured; its growth is shown on charcoal yeast extract agar."),
  [("Eosin methylene blue agar",
    "Eosin methylene blue agar selects for Gram-negative enterics and differentiates lactose fermenters; Legionella "
    "is grown on charcoal yeast extract agar.", "enteric medium"),
   ("Chocolate agar of cooked blood",
    "Chocolate agar, of cooked blood, is what Haemophilus needs; Legionella is grown on charcoal yeast extract "
    "agar.", "adjacent fact from the same lecture (Haemophilus)"),
   ("MacConkey's bile salt agar",
    "MacConkey's agar, with crystal violet and bile salts, selects for Gram-negative enterics; Legionella grows on "
    "charcoal yeast extract agar.", "enteric medium")],
  ci(41, 39, 48, 97)),

Q("Legionella", IO1,
  "Which people are most prone to Legionnaires disease?",
  ("Men over 50 and smokers",
   "Correct: legionellosis is prevalent in males over 50 and in smokers, and as a nosocomial disease it affects "
   "elderly patients with diabetes, cancer, transplants, chronic alcoholism or chronic lung disease."),
  [("Contact lens wearers",
    "Contact lens wearers get corneal ulcers from Pseudomonas aeruginosa; Legionnaires disease is prevalent in "
    "males over 50 and smokers.", "adjacent fact from the same lecture (Pseudomonas)"),
   ("Infants not yet vaccinated",
    "Unvaccinated infants carry the highest pertussis incidence; Legionnaires disease is prevalent in males over 50 "
    "and smokers.", "adjacent fact from the same lecture (pertussis)"),
   ("Women with urinary catheters",
    "Women and catheterized patients get Escherichia coli urinary tract infections; Legionnaires disease is "
    "prevalent in males over 50 and smokers.", "adjacent fact from the same lecture (E. coli)")],
  c(40, 19, 35, 65)),

Q("Legionella", IO1,
  "Which two illnesses does Legionella cause?",
  ("Legionnaires disease, Pontiac fever",
   "Correct: legionellosis takes two forms, Legionnaires disease and Pontiac fever, with fever, cough, diarrhea, "
   "abdominal pain and pneumonia."),
  [("Undulant fever and Malta fever",
    "Undulant fever and Malta fever are both names for brucellosis; Legionella causes Legionnaires disease and "
    "Pontiac fever.", "adjacent fact from the same lecture (Brucella)"),
   ("Swimmer's ear and corneal ulcers",
    "Swimmer's ear and corneal ulcers are Pseudomonas aeruginosa infections in healthy people; Legionella causes "
    "Legionnaires disease and Pontiac fever.", "adjacent fact from the same lecture (Pseudomonas)"),
   ("Conjunctivitis and chancroid",
    "Conjunctivitis and chancroid are caused by Haemophilus aegyptius and Haemophilus ducreyi; Legionella causes "
    "Legionnaires disease and Pontiac fever.", "adjacent fact from the same lecture (Haemophilus)")],
  c(40, 19, 27, 100)),
]
