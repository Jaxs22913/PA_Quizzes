# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Drugs for Pulmonary Infections, Asthma and COPD (Lecture 11), topic: tuberculosis drugs.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. The key is authored FIRST (c == 0);
pharm_e3_partition.py rotates it (numeric option sets are sorted ascending instead, WRITER.md rule 8).

SOURCE. Pulmonology-2.pptx slides 32-46: mycobacteria (34) and the drug-target picture (33, read by eye into
tools/pharm_e3/ocr.json under "L11"), combination therapy (35) and durations (36), isoniazid (37-39), rifampin (40-42),
ethambutol (43-44), pyrazinamide (45), resistance (46; the second-line list is out of scope, below). Slide 32 is a poster (no content).

WRITER.md v1 (2026-10-15): every distractor carries its misconception as a third element (mis); slides only (this deck
has no speaker notes); slides win on conflict. Shared keying decisions: scratchpad L11_KEYING.md.

LEFT OUT ON PURPOSE:
  * the slide 46 "other agents" list (streptomycin, aminosalicylic acid, cycloserine, rifabutin, clofazimine,
    linezolid): Dr. Wood, 45:56-46:10, "I would not memorize this list ... I'm not going to quiz you on them so
    specifically. I'd rather you know those big four." No item keys them or offers them as distractors;
  * every dose (slide 35's milligram and milligram-per-kilogram amounts); the regimen STRUCTURE is kept;
  * every bare percentage or half-life as a key (75-95% acetylated, 70 minutes versus 2.5 hours, 20% flu-like
    syndrome, 75% excreted unchanged, 15% hepatitis appear only inside stems or explanations);
  * rifampin's gram-positive and gram-negative lists (slide 40): Neisseria and Legionella are gram-negative;
  * the human immunodeficiency virus (9-12 months), complicated-disease (18-24 months) and isoniazid- or
    rifampin-resistance (18-24 months) durations as keys: current guidance treats most of these differently;
  * "Visual disturbances (limited in children)" (slide 44) as a key: it can be read as "use is limited in children"
    or "the disturbance is limited in children";
  * "bacteriostatic" as a stem that asks which drug is bacteriostatic: isoniazid is bacteriostatic for latent
    bacteria and ethambutol is bacteriostatic, so two answers fit;
  * isoniazid "enters the central nervous system" as a drug-identification key (other first-line drugs reach the
    central nervous system in practice) and isoniazid seizures beside pyridoxine (pyridoxine also treats
    isoniazid seizures in practice);
  * the chemical structures (slides 37, 40, 43).
mis = misconception tag on every distractor (WRITER.md rule 5)
"""

D = "Pulmonology-2.pptx"
IO_CLASS = "Identify respiratory drug classes and commonly prescribed drugs for pulmonary infections, asthma, and COPD/COLD"
IO_MOA = "Describe the molecular mechanism of action of drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_IND = "Identify indications for drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_ADME = "Describe absorption, distribution, metabolism, and excretion of drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_TOX = "Summarize side effects and toxic manifestations of respiratory drugs"
IO_AE = "Describe adverse effects of drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_CONTRA = "Identify contraindications for drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_INTER = "Discuss potential drug-drug, drug-food, and drug-herb interactions with drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_PROT = "List commonly used protocols and patient monitoring for pulmonary infections, asthma, and COPD/COLD"
IO_EDU = "Outline appropriate patient education for drugs used for pulmonary infections, asthma, and COPD/COLD"

MECH, ADJ, REV, LAY, STAGE, RULED, COMP = ("confused mechanism or drug class", "adjacent fact", "reversed direction or value",
                                           "common lay belief", "wrong stage or severity", "ruled out by a stated finding",
                                           "competing diagnosis")


def Q(topic, io, slot, q, opts, slide):
    return {"topic": topic, "io": io, "slot": slot, "q": q, "opts": opts, "c": 0, "cite": "%s, Slide %d" % (D, slide)}


QUESTIONS = [

# ---- mycobacteria (slides 33 and 34) -------------------------------------------------------------
Q("Mycobacteria", IO_MOA, "physiology",
  "Which component of the mycobacterial cell wall forms its waxy coat?",
  [["Mycolic acid", "Correct. Mycobacteria are acid-fast bacilli whose distinct phosphoglycolipid layer, mycolic acid, forms the waxy cell coat."],
   ["Peptidoglycan", "Peptidoglycan sits beneath the arabinogalactan layer of the mycobacterial wall; the waxy coat is formed by the mycolic acid layer.", ADJ],
   ["Arabinogalactan", "Arabinogalactan is the layer between peptidoglycan and mycolic acid, where ethambutol acts; the waxy coat itself is mycolic acid.", ADJ],
   ["Plasma membrane", "The plasma membrane lies inside the cell wall and is one of pyrazinamide's possible targets; the waxy coat is the mycolic acid layer.", ADJ]], 34),

Q("Mycobacteria", IO_MOA, "physiology",
  "Why do antimicrobials that act on cell division work less well against Mycobacterium tuberculosis?",
  [["It grows slowly and can lie dormant", "Correct. Mycobacterium tuberculosis is very slow growing and can exist in dormant states for long periods, so drugs that act on dividing cells work less well."],
   ["It divides faster than drugs can act", "The reverse is true: Mycobacterium tuberculosis is very slow growing and can stay dormant for long periods, which blunts drugs that act on division.", REV],
   ["It has no cell wall for drugs to target", "Mycobacteria have a distinct cell wall whose mycolic acid layer forms a waxy coat; the problem for these drugs is slow growth and dormancy.", MECH],
   ["It is a gram-negative rod", "Mycobacteria are classed as acid-fast bacilli with a waxy mycolic acid coat; drugs acting on division fail because the organism grows slowly and lies dormant.", MECH]], 34),

# ---- combination therapy and durations (slides 35 and 36) -------------------------------------------
Q("Combination therapy", IO_PROT, "protocol",
  "Which four drugs make up the first two months of combination therapy for tuberculosis?",
  [["Isoniazid, rifampin, ethambutol, pyrazinamide", "Correct. The first two months combine isoniazid, rifampin, ethambutol and pyrazinamide, followed by four months of isoniazid and rifampin."],
   ["Isoniazid, rifampin, ethambutol, vancomycin", "Vancomycin is the empiric methicillin-resistant Staphylococcus aureus (MRSA) pneumonia drug; pyrazinamide completes the first-phase four with isoniazid, rifampin and ethambutol.", ADJ],
   ["Isoniazid, rifampin, pyrazinamide, amikacin", "Amikacin is an aminoglycoside dosed by levels and limited by ototoxicity and nephrotoxicity; ethambutol completes the first-phase four with the other three.", ADJ],
   ["Rifampin, ethambutol, pyrazinamide, doxycycline", "Doxycycline is a second-line outpatient choice for community-acquired pneumonia; isoniazid completes the first-phase four with rifampin, ethambutol and pyrazinamide.", ADJ]], 35),

Q("Combination therapy", IO_PROT, "protocol",
  "After the first two months of tuberculosis treatment, which two drugs continue for the next four months?",
  [["Isoniazid and rifampin", "Correct. After two months of four drugs, isoniazid and rifampin continue for four more months."],
   ["Ethambutol and pyrazinamide", "These two belong to the first two months only; pyrazinamide is limited to the first two months to avoid liver toxicity, and isoniazid and rifampin continue.", STAGE],
   ["Isoniazid and ethambutol", "Ethambutol is part of the first two months; the four-month continuation pairs isoniazid with rifampin.", STAGE],
   ["Rifampin and pyrazinamide", "Pyrazinamide is given in the first two months only, to avoid liver toxicity; rifampin continues with isoniazid for four months.", STAGE]], 35),

Q("Combination therapy", IO_PROT, "protocol",
  "How long is the course of treatment for pulmonary tuberculosis?",
  [["6-9 months", "Correct. Pulmonary tuberculosis is treated for 6 to 9 months, beginning with two months of four drugs and continuing with isoniazid and rifampin."],
   ["2 months", "Two months is only the first, four-drug phase; it is followed by four months of isoniazid and rifampin, for 6 to 9 months in all.", STAGE],
   ["9-12 months", "Nine to 12 months is the course given for patients with human immunodeficiency virus and tuberculosis; pulmonary tuberculosis is 6 to 9 months.", ADJ],
   ["18-24 months", "Eighteen to 24 months is for complicated disease in other body parts or for isoniazid or rifampin resistance; pulmonary tuberculosis is 6 to 9 months.", ADJ]], 36),

Q("Combination therapy", IO_PROT, "protocol",
  "Why is active tuberculosis never treated with a single drug?",
  [["To prevent resistance", "Correct. Single agents are not used in active disease, to prevent resistance; rifampin and ethambutol in particular lose effect quickly when given alone."],
   ["To prevent liver toxicity", "Liver toxicity is why pyrazinamide is limited to the first two months, not why drugs are combined; combination therapy prevents resistance.", ADJ],
   ["To reach the central nervous system", "Isoniazid on its own is well absorbed and enters the central nervous system; single agents are avoided in active disease to prevent resistance.", MECH],
   ["To shorten the dormant phase", "Dormancy explains why drugs acting on cell division work less well; drugs are combined in active disease to prevent resistance.", MECH]], 36),

Q("Combination therapy", IO_IND, "indication",
  "In which situation is isoniazid used as a single drug?",
  [["Tuberculosis prophylaxis", "Correct. Isoniazid is used alone for prophylaxis; in active disease it is always part of combination therapy."],
   ["Active tuberculosis", "Active disease needs combination therapy, because single agents breed resistance; isoniazid alone is the prophylactic use.", STAGE],
   ["Meningococcal prophylaxis", "Meningococcal prophylaxis is a use of rifampin, not isoniazid; isoniazid alone is used for tuberculosis prophylaxis.", ADJ],
   ["Infective endocarditis", "Endocarditis is listed among rifampin's uses; isoniazid as a single drug is reserved for tuberculosis prophylaxis.", ADJ]], 39),

# ---- isoniazid (slides 37-39) ---------------------------------------------------------------------------
Q("Isoniazid", IO_MOA, "mechanism",
  "What does isoniazid inhibit in Mycobacterium tuberculosis?",
  [["Mycolic acid production", "Correct. Isoniazid inhibits mycolic acid production and so the waxy cell coat; it is bacteriostatic for latent and bactericidal for dividing bacteria."],
   ["DNA-dependent RNA polymerase", "Inhibiting the DNA-dependent RNA polymerase is rifampin's mechanism; isoniazid inhibits mycolic acid production.", MECH],
   ["Mycolic acid incorporation", "Blocking the incorporation of mycolic acid into membranes is ethambutol's action; isoniazid inhibits mycolic acid production itself.", MECH],
   ["Growth at normal pH", "Lowering the pH so bacteria cannot grow is pyrazinamide's action, through pyrazinoic acid; isoniazid inhibits mycolic acid production.", MECH]], 37),

Q("Isoniazid", IO_MOA, "mechanism",
  "Isoniazid is activated by which bacterial enzyme?",
  [["Catalase-peroxidase", "Correct. Isoniazid is metabolically activated by the bacterial catalase-peroxidase; mutation in the DNA coding for this enzyme produces resistance."],
   ["RNA polymerase", "The DNA-dependent RNA polymerase is the enzyme rifampin inhibits; isoniazid is activated by the bacterial catalase-peroxidase.", MECH],
   ["Cytochrome P450 3A4", "Cytochrome P450 3A4 (CYP3A4) is a human enzyme that rifampin induces; isoniazid is activated by the bacterial catalase-peroxidase.", MECH],
   ["Phosphodiesterase", "Phosphodiesterase is the enzyme theophylline inhibits; isoniazid is activated by the bacterial catalase-peroxidase.", MECH]], 38),

Q("Isoniazid", IO_MOA, "mechanism",
  "How does Mycobacterium tuberculosis become resistant to isoniazid?",
  [["Mutation in the gene for its activating enzyme", "Correct. Resistance comes from mutation in the DNA coding for the activating enzyme, the bacterial catalase-peroxidase, so isoniazid is never activated."],
   ["Faster acetylation of the drug by the patient", "Fast or slow acetylation is a trait of the patient that changes isoniazid's half-life; bacterial resistance comes from mutation in the activating enzyme's gene.", MECH],
   ["Loss of the waxy mycolic acid layer of its wall", "Isoniazid works by inhibiting mycolic acid production, so losing that layer is its effect, not resistance; resistance comes from mutation in the activating enzyme's gene.", REV],
   ["Long periods of dormancy inside the host", "Dormancy explains why drugs that act on cell division work less well; isoniazid resistance comes from mutation in the activating enzyme's gene.", ADJ]], 38),

Q("Isoniazid", IO_ADME, "monitoring",
  "Isoniazid's half-life varies widely between patients (about 70 minutes versus 2.5 hours). What explains the difference?",
  [["Fast or slow acetylation", "Correct. Most isoniazid (75 to 95 percent) is excreted as an acetylated metabolite, and fast acetylators clear it in about 70 minutes against 2.5 hours in slow acetylators."],
   ["Renal function", "Renal function governs ethambutol, which is about 75 percent excreted unchanged; isoniazid's half-life split follows fast or slow acetylation.", ADJ],
   ["Bacterial catalase-peroxidase", "The bacterial catalase-peroxidase activates isoniazid inside the organism; the patient's half-life split follows fast or slow acetylation.", MECH],
   ["Cytochrome P450 induction", "Cytochrome P450 induction is rifampin's interaction effect; isoniazid's 70-minute versus 2.5-hour half-life follows fast or slow acetylation.", ADJ]], 37),

Q("Isoniazid", IO_EDU, "education",
  "A patient starting isoniazid is also given pyridoxine (vitamin B6). Which adverse effect does the pyridoxine prevent?",
  [["Peripheral neuritis", "Correct. Isoniazid's peripheral neuritis comes from pyridoxine deficiency, so pyridoxine (vitamin B6) is given with it."],
   ["Hepatitis", "Isoniazid hepatitis rises in alcoholics and with age and is not prevented by pyridoxine; pyridoxine prevents the peripheral neuritis of pyridoxine deficiency.", ADJ],
   ["Lupus-like syndrome", "The lupus-like syndrome is isoniazid's allergic reaction and is not a vitamin deficiency; pyridoxine prevents peripheral neuritis.", ADJ],
   ["Red-green color loss", "Decreased red-green discrimination is ethambutol's visual adverse effect; pyridoxine given with isoniazid prevents peripheral neuritis.", ADJ]], 39),

Q("Isoniazid", IO_AE, "adverse effect",
  "Which patient factor raises the risk of isoniazid hepatitis?",
  [["Alcoholism", "Correct. Isoniazid hepatitis is increased in alcoholics and increases with age."],
   ["Younger age", "The risk runs the other way: isoniazid hepatitis increases with age, and it is also increased in alcoholics.", REV],
   ["Renal disease", "Renal disease calls for adjusting ethambutol, which is mostly excreted unchanged; isoniazid hepatitis is increased in alcoholics and with age.", ADJ],
   ["Hyperuricemia", "Raised uric acid is an effect of pyrazinamide and ethambutol, not a risk factor for liver injury; isoniazid hepatitis is increased in alcoholics.", ADJ]], 39),

Q("Isoniazid", IO_AE, "adverse effect",
  "Which allergic reaction is listed for isoniazid?",
  [["Lupus-like syndrome", "Correct. Isoniazid's allergic reactions include a lupus-like syndrome."],
   ["Flu-like syndrome", "A flu-like syndrome is rifampin's hypersensitivity reaction, seen in about 20 percent of patients; isoniazid's is a lupus-like syndrome.", ADJ],
   ["Peripheral neuritis", "Peripheral neuritis is isoniazid's pyridoxine-deficiency effect, not an allergic reaction; the allergic reaction is a lupus-like syndrome.", ADJ],
   ["Hepatitis", "Hepatitis is an isoniazid adverse effect tied to alcohol and age, not its allergic reaction; the allergic reaction is a lupus-like syndrome.", ADJ]], 39),

# ---- rifampin (slides 41 and 42) ------------------------------------------------------------------------
Q("Rifampin", IO_MOA, "mechanism",
  "What does rifampin inhibit in Mycobacterium tuberculosis?",
  [["DNA-dependent RNA polymerase", "Correct. Rifampin inhibits the bacterial DNA-dependent RNA polymerase by forming a complex with the enzyme, with no effect on the human enzyme."],
   ["Mycolic acid production", "Inhibiting mycolic acid production is isoniazid's mechanism; rifampin inhibits the DNA-dependent RNA polymerase.", MECH],
   ["Bacterial catalase-peroxidase", "Catalase-peroxidase is the bacterial enzyme that activates isoniazid; rifampin inhibits the DNA-dependent RNA polymerase.", MECH],
   ["Cytochrome P450 enzymes", "Rifampin induces cytochrome P450 enzymes rather than inhibiting them, and that is its interaction effect; its antibacterial target is the RNA polymerase.", REV]], 41),

Q("Rifampin", IO_AE, "adverse effect",
  "A patient notices orange tears and orange urine after starting tuberculosis therapy. Which drug explains this?",
  [["Rifampin", "Correct. Rifampin colors secretions orange: tears, sweat and urine."],
   ["Isoniazid", "Isoniazid causes a lupus-like syndrome, hepatitis and peripheral neuritis, not colored secretions; rifampin turns tears, sweat and urine orange.", ADJ],
   ["Ethambutol", "Ethambutol affects vision (red-green discrimination and acuity) and raises uric acid; orange tears and urine come from rifampin.", ADJ],
   ["Pyrazinamide", "Pyrazinamide causes hepatitis and hyperuricemia; orange tears, sweat and urine come from rifampin.", ADJ]], 42),

Q("Rifampin", IO_INTER, "interaction",
  "Rifampin interacts with anticoagulants, contraceptives, digoxin and theophylline through which action?",
  [["Induction of cytochrome P450 enzymes", "Correct. Rifampin induces cytochrome P450 enzymes (CYP1A2, CYP2C9 and CYP3A4), which is how it interacts with anticoagulants, contraceptives, digoxin, ketoconazole and theophylline."],
   ["Inhibition of cytochrome P450 enzymes", "The direction is reversed: rifampin induces cytochrome P450 enzymes such as CYP3A4 (cytochrome P450 3A4), and that drives its interactions.", REV],
   ["Inhibition of human RNA polymerase", "Rifampin inhibits the bacterial DNA-dependent RNA polymerase and has no effect on the human enzyme; its interactions come from cytochrome P450 induction.", MECH],
   ["Inhibition of mycolic acid synthesis", "Inhibiting mycolic acid production is isoniazid's antibacterial action; rifampin's drug interactions come from inducing cytochrome P450 enzymes.", MECH]], 42),

# Dr. Wood, 45:12-45:23: rifampin lowering contraceptive levels is "a lot of important education".
Q("Rifampin", IO_EDU, "education",
  "A woman who takes an oral contraceptive is starting rifampin for tuberculosis. What should she be told about the combination?",
  [["Her contraceptive may work less well", "Correct. Rifampin induces cytochrome P450 enzymes and lowers contraceptive levels, so the contraceptive may fail; she needs counseling about pregnancy risk."],
   ["Her contraceptive levels will rise", "The direction is reversed: rifampin INDUCES cytochrome P450 enzymes, which lowers contraceptive levels rather than raising them.", REV],
   ["Her contraceptive will weaken rifampin", "The interaction runs the other way: rifampin, an enzyme inducer, lowers the contraceptive's levels; it is not weakened by the contraceptive.", REV],
   ["The two drugs do not interact", "Contraceptives are on rifampin's listed interactions, through cytochrome P450 induction, so the contraceptive may work less well.", RULED]], 42),

Q("Rifampin", IO_IND, "indication",
  "Besides tuberculosis, rifampin is used as prophylaxis against which infection?",
  [["Meningococcal disease", "Correct. Rifampin's primary use is tuberculosis, and it is also used prophylactically for meningococcal disease; endocarditis is listed as a use without the prophylactic label."],
   ["Influenza", "Influenza is prevented with the annual influenza vaccine; rifampin's prophylactic use is against meningococcal disease.", ADJ],
   ["Pneumococcal pneumonia", "Pneumococcal disease is prevented with the pneumococcal vaccine; rifampin's prophylactic use is against meningococcal disease.", ADJ],
   ["Endocarditis", "Endocarditis appears among rifampin's uses without the prophylactic label; the use marked prophylactic is meningococcal disease.", ADJ]], 41),

Q("Rifampin", IO_PROT, "protocol",
  "Why is rifampin rarely used alone?",
  [["Tolerance develops rapidly", "Correct. Rifampin is rarely used alone because rapid tolerance develops; in tuberculosis it is always combined."],
   ["Its spectrum is narrow", "Rifampin is broad spectrum, so a narrow spectrum is not the problem; it is rarely used alone because tolerance develops rapidly.", REV],
   ["It causes jaundice", "Jaundice and hepatitis are rifampin adverse effects, a concern in chronic liver disease; it is rarely used alone because tolerance develops rapidly.", ADJ],
   ["It turns urine orange", "Orange secretions are a harmless rifampin effect to warn about; the reason it is rarely used alone is rapid tolerance.", ADJ]], 41),

Q("Rifampin", IO_AE, "adverse effect",
  "Which hypersensitivity reaction occurs in about 20 percent of patients taking rifampin?",
  [["Flu-like syndrome", "Correct. Rifampin hypersensitivity takes the form of a flu-like syndrome in about 20 percent of patients."],
   ["Lupus-like syndrome", "A lupus-like syndrome is isoniazid's allergic reaction; rifampin's hypersensitivity is a flu-like syndrome.", ADJ],
   ["Peripheral neuritis", "Peripheral neuritis is isoniazid's effect from pyridoxine deficiency; rifampin's hypersensitivity is a flu-like syndrome.", ADJ],
   ["Visual disturbance", "Visual disturbances belong to ethambutol (red-green discrimination, acuity); rifampin's hypersensitivity is a flu-like syndrome.", ADJ]], 42),

Q("Rifampin", IO_CONTRA, "contraindication",
  "Rifampin's jaundice and hepatitis are a particular concern in which patients?",
  [["Chronic liver disease", "Correct. Rifampin can cause jaundice and hepatitis, a particular concern in chronic liver disease."],
   ["Chronic kidney disease", "Renal disease calls for adjusting ethambutol, which is mostly excreted unchanged; rifampin's liver effects matter most in chronic liver disease.", ADJ],
   ["Pregnancy in any trimester", "Pregnancy is the listed reason to avoid pyrazinamide; rifampin's jaundice and hepatitis are the concern in chronic liver disease.", ADJ],
   ["Gout or high uric acid", "Raised uric acid is a pyrazinamide and ethambutol effect; rifampin's jaundice and hepatitis are the concern in chronic liver disease.", ADJ]], 42),

# ---- ethambutol (slides 43 and 44) ------------------------------------------------------------------
Q("Ethambutol", IO_AE, "adverse effect",
  "Which visual change is a classic adverse effect of ethambutol?",
  [["Decreased red-green discrimination", "Correct. Ethambutol's visual disturbances are decreased red-green discrimination and decreased visual acuity."],
   ["Orange discoloration of tears", "Orange tears, sweat and urine come from rifampin; ethambutol decreases red-green discrimination and visual acuity.", ADJ],
   ["Dilated pupils with blurry vision", "Blurry vision with mydriasis is an anticholinergic effect (blind as a bat); ethambutol decreases red-green discrimination.", ADJ],
   ["Yellowing of the whites of the eyes", "Yellow eyes signal jaundice, listed with rifampin's hepatitis; ethambutol's visual effect is decreased red-green discrimination and visual acuity.", ADJ]], 44),

Q("Ethambutol", IO_ADME, "monitoring",
  "Which first-line tuberculosis drug needs its dose adjusted in renal disease because about 75 percent is excreted unchanged?",
  [["Ethambutol", "Correct. About 75 percent of ethambutol is excreted unchanged, so its dose is adjusted in renal disease."],
   ["Isoniazid", "Isoniazid is mostly (75 to 95 percent) excreted as an acetylated metabolite, so acetylation, not unchanged renal excretion, sets its half-life.", ADJ],
   ["Rifampin", "Rifampin's listed concern is the liver (jaundice, hepatitis in chronic liver disease) and enzyme induction; ethambutol is the one excreted unchanged.", ADJ],
   ["Pyrazinamide", "Pyrazinamide is limited to two months for liver toxicity and is monitored with liver enzymes; ethambutol is the one adjusted in renal disease.", ADJ]], 44),

Q("Ethambutol", IO_MOA, "mechanism",
  "What does ethambutol's weakening of the mycobacterial cell wall do for combination therapy?",
  [["It lets other agents in more easily", "Correct. Ethambutol inhibits mycolic acid incorporation into membranes, and the weakened cell wall allows other agents better access."],
   ["It kills the bacteria outright", "Ethambutol is bacteriostatic, so it does not kill outright; its weakened cell wall lets the other agents in more easily.", REV],
   ["It shortens the treatment course", "Shortening combined therapy is pyrazinamide's contribution; ethambutol's weakened cell wall gives other agents better access.", ADJ],
   ["It keeps resistance from forming", "Resistance to ethambutol develops quickly if it is used alone; its weakened cell wall helps by letting other agents in.", REV]], 43),

# ---- pyrazinamide (slides 33 and 45) ----------------------------------------------------------------
Q("Pyrazinamide", IO_TOX, "adverse effect",
  "Which drug inhibits uric acid excretion, so that nearly all patients taking it become hyperuricemic?",
  [["Pyrazinamide", "Correct. Pyrazinamide inhibits uric acid excretion, and all patients taking it are hyperuricemic."],
   ["Isoniazid", "Isoniazid's adverse effects are a lupus-like syndrome, hepatitis, peripheral neuritis and central nervous system effects; pyrazinamide inhibits uric acid excretion.", ADJ],
   ["Rifampin", "Rifampin induces cytochrome P450 enzymes, colors secretions orange and causes a flu-like syndrome; pyrazinamide inhibits uric acid excretion.", ADJ],
   ["Vancomycin", "Vancomycin's listed adverse effects are ototoxicity and nephrotoxicity with other nephrotoxins; pyrazinamide inhibits uric acid excretion.", ADJ]], 45),

Q("Pyrazinamide", IO_PROT, "protocol",
  "Why is pyrazinamide given only during the first two months of tuberculosis treatment?",
  [["To avoid liver toxicity", "Correct. Pyrazinamide is given for the first two months only, to avoid liver toxicity; it causes hepatitis in about 15 percent of patients."],
   ["To avoid hyperuricemia", "Pyrazinamide does make all patients hyperuricemic, but the stated reason for stopping after two months is to avoid liver toxicity.", ADJ],
   ["Because resistance is rapid", "Rapid resistance when used alone is noted for ethambutol and rifampin; pyrazinamide is limited to two months to avoid liver toxicity.", ADJ],
   ["Because it stains secretions", "Orange secretions are a rifampin effect; pyrazinamide is limited to the first two months to avoid liver toxicity.", ADJ]], 45),

# Dr. Wood, 44:54-44:59: isoniazid, rifampin and pyrazinamide are all "rough on the liver"; monitor closely.
Q("Pyrazinamide", IO_AE, "adverse effect",
  "A patient with chronic liver disease needs tuberculosis therapy. Which first-line drug has no listed liver toxicity?",
  [["Ethambutol", "Correct. Ethambutol's listed adverse effects are visual disturbances and raised uric acid; isoniazid, rifampin and pyrazinamide all list hepatitis."],
   ["Isoniazid", "Isoniazid lists hepatitis, more likely with age and alcohol use; ethambutol is the first-line drug without a listed liver toxicity.", ADJ],
   ["Rifampin", "Rifampin lists jaundice and hepatitis, a particular concern in chronic liver disease; ethambutol has no listed liver toxicity.", ADJ],
   ["Pyrazinamide", "Pyrazinamide causes hepatitis in about 15 percent and needs liver enzyme monitoring; ethambutol has no listed liver toxicity.", ADJ]], 44),

Q("Pyrazinamide", IO_PROT, "monitoring",
  "Which laboratory monitoring does pyrazinamide require?",
  [["Liver enzymes", "Correct. Pyrazinamide causes hepatitis in about 15 percent of patients, so liver enzymes are monitored."],
   ["Drug trough levels", "Trough levels are drawn for vancomycin, and aminoglycoside doses follow levels; pyrazinamide is monitored with liver enzymes.", ADJ],
   ["Red-green color vision", "Red-green discrimination is tested for ethambutol's visual effects and is not a laboratory test; pyrazinamide needs liver enzymes.", ADJ],
   ["Kidney function", "Kidney function is watched with aminoglycosides and vancomycin, which are nephrotoxic; pyrazinamide causes hepatitis, so liver enzymes are monitored.", ADJ]], 45),

Q("Pyrazinamide", IO_MOA, "mechanism",
  "How does pyrazinamide stop mycobacterial growth?",
  [["Its acid product lowers the pH", "Correct. Pyrazinamide is converted to pyrazinoic acid, which lowers the pH so the bacteria cannot grow; it also enters macrophages."],
   ["It inhibits RNA polymerase", "Inhibiting the DNA-dependent RNA polymerase is rifampin's mechanism; pyrazinamide is converted to pyrazinoic acid, which lowers the pH.", MECH],
   ["It blocks mycolic acid synthesis", "Inhibiting mycolic acid production is isoniazid's mechanism; pyrazinamide works through pyrazinoic acid lowering the pH.", MECH],
   ["It weakens the cell wall", "Weakening the cell wall to let other agents in is ethambutol's action; pyrazinamide's pyrazinoic acid lowers the pH so bacteria cannot grow.", MECH]], 45),

Q("Pyrazinamide", IO_CONTRA, "contraindication",
  "Which first-line tuberculosis drug should be avoided in pregnancy?",
  [["Pyrazinamide", "Correct. Pyrazinamide is to be avoided in pregnancy; it also causes hepatitis and hyperuricemia."],
   ["Isoniazid", "No pregnancy warning is given for isoniazid; its concerns are hepatitis, peripheral neuritis and a lupus-like syndrome. Pyrazinamide is the one to avoid.", ADJ],
   ["Rifampin", "No pregnancy warning is given for rifampin; its concerns are enzyme induction, liver injury and orange secretions. Pyrazinamide is the one to avoid.", ADJ],
   ["Ethambutol", "No pregnancy warning is given for ethambutol; its concerns are vision, uric acid and renal dosing. Pyrazinamide is the one to avoid in pregnancy.", ADJ]], 45),

Q("Pyrazinamide", IO_IND, "drug choice",
  "What does pyrazinamide add to combined tuberculosis therapy?",
  [["It shortens the treatment course", "Correct. Pyrazinamide decreases the duration of combined therapy; it is given during the first two months only."],
   ["It prevents peripheral neuritis", "Peripheral neuritis is prevented by giving pyridoxine (vitamin B6) with isoniazid; pyrazinamide shortens combined therapy.", ADJ],
   ["It weakens the cell wall", "Weakening the cell wall to give other agents better access is ethambutol's contribution; pyrazinamide shortens combined therapy.", ADJ],
   ["It induces liver enzymes", "Inducing cytochrome P450 enzymes is rifampin's interaction effect, not a benefit; pyrazinamide's contribution is a shorter course.", ADJ]], 45),
]
