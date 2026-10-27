# -*- coding: utf-8 -*-
"""Rapid-drill bank: pulmonary infections, asthma and chronic obstructive pulmonary disease (Lecture 11,
Pulmonology-2.pptx, deck key PU).

One fact, four names, no doses. One drug per choice; a class name is offered only when the stem itself asks for a
class, and then every choice is a class. Every wrong choice is another real drug (or class) from the same deck, and
never a second defensible answer: a fact the deck gives to two drugs (levofloxacin and moxifloxacin; gentamicin,
tobramycin and amikacin; diphenhydramine and hydroxyzine; prednisone and methylprednisolone; the uric acid rise of
ethambutol and pyrazinamide; the hepatitis of isoniazid, rifampin and pyrazinamide) is either asked of the group or
keyed to one of them with the other never offered beside it.

Slides only (the deck has no speaker notes); picture slides were read by eye into tools/pharm_e3/ocr.json under
"L11". Shared keying decisions: the build's L11_KEYING notes (summarized here).

Left out on purpose (Jaxon's standing rules and the Lecture 11 keying decisions):
  * every dose: tuberculosis milligram amounts (slide 35), crystalloid volumes (slide 50), epinephrine concentrations
    (slide 52), the bupropion schedule (slide 105), nebulized albuterol per hour (slide 99);
  * drug levels as the thing asked: theophylline ranges (slides 84-85) and the vancomycin trough number (slide 29);
  * theophylline "renally eliminated" (slide 85): it is mainly hepatically metabolized;
  * rifampin's gram-positive and gram-negative lists (slide 40): Neisseria and Legionella are gram-negative;
  * tiotropium "COPD only" (slide 86): the stepwise asthma chart (slide 90) lists add-on tiotropium;
  * montelukast "side effects minimal" (slide 75): current labeling carries a boxed warning;
  * the systemic steroid taper rule (slide 89), held until the recording pass;
  * ceftazidime "not recommended" (slide 24), ticarcillin/clavulanate as a choice (slide 26), cromolyn's brand
    (slide 78), benralizumab's target against mepolizumab's (slide 81);
  * the extended treatment duration for Pseudomonas and the other named organisms (slide 31);
  * the pneumococcal vaccine brand (slide 108) and the epinephrine auto-injector picture (slide 52);
  * bupropion as a distractor beside the varenicline boxed-warning item (bupropion has its own antidepressant
    warning in practice, so it could be defended there).
"""
ITEMS = [
# ---- acute bronchitis and community-acquired pneumonia (slides 6-15) ----
dict(q="Which antibiotic is preferred for acute bronchitis when Mycoplasma is documented, because of macrolide resistance?",
     ans="Doxycycline", src=("PU", 8),
     why="Doxycycline is the preferred choice when Mycoplasma is documented in acute bronchitis, because of macrolide resistance.",
     wrong=[("Azithromycin", "Azithromycin is a macrolide; macrolide resistance is the reason doxycycline is preferred when Mycoplasma is documented."),
            ("Levofloxacin", "Respiratory fluoroquinolones such as levofloxacin are avoided in bronchitis unless there was recent antibiotic exposure."),
            ("Ceftriaxone", "Ceftriaxone is an intravenous beta-lactam for inpatient pneumonia; doxycycline is preferred for documented Mycoplasma bronchitis.")]),

dict(q="Which drug is listed with doxycycline as second-line outpatient therapy for community-acquired pneumonia without resistance risk?",
     ans="Minocycline", src=("PU", 14),
     why="With no risk of resistant Streptococcus pneumoniae, a macrolide is first line and doxycycline or minocycline is second line.",
     wrong=[("Clarithromycin", "Clarithromycin is a macrolide, the first-line choice (with azithromycin) when there is no risk of resistant pneumococcus."),
            ("Cefpodoxime", "Cefpodoxime is a beta-lactam given with a macrolide when there ARE risk factors for resistant Streptococcus pneumoniae."),
            ("Moxifloxacin", "Moxifloxacin is a respiratory fluoroquinolone used when there ARE risk factors for resistant Streptococcus pneumoniae.")]),

dict(q="Which respiratory fluoroquinolone is an outpatient choice for community-acquired pneumonia with risk factors for resistant pneumococcus?",
     ans="Moxifloxacin", src=("PU", 14),
     why="With risk factors for resistant Streptococcus pneumoniae, a beta-lactam plus a macrolide or a respiratory fluoroquinolone (levofloxacin, moxifloxacin) is used.",
     wrong=[("Ciprofloxacin", "Ciprofloxacin is listed as an antipseudomonal fluoroquinolone for nosocomial pneumonia, not as a respiratory fluoroquinolone."),
            ("Minocycline", "Minocycline is a second-line choice only when there is NO risk of resistant Streptococcus pneumoniae."),
            ("Azithromycin", "Azithromycin alone is first line only without resistance risk; with risk factors it is paired with a beta-lactam.")]),

dict(q="Which penicillin, given intravenously in high dose, is a beta-lactam choice for inpatient community-acquired pneumonia?",
     ans="Ampicillin", src=("PU", 15),
     why="Inpatient (non-intensive care) pneumonia gets an intravenous beta-lactam: cefotaxime, ceftriaxone or high-dose ampicillin, plus a macrolide.",
     wrong=[("Piperacillin/tazobactam", "Piperacillin/tazobactam is an antipseudomonal penicillin for broad-spectrum nosocomial coverage, not inpatient community pneumonia."),
            ("Amoxicillin", "Amoxicillin, with or without clavulanic acid, is the outpatient beta-lactam for patients with resistance risk factors."),
            ("Ertapenem", "Ertapenem is a narrow-spectrum carbapenem listed for limited-spectrum nosocomial coverage, not for community pneumonia.")]),

# ---- nosocomial pneumonia and its antibiotics (slides 22-30) ----
dict(q="Which third-generation cephalosporin is a limited-spectrum choice for nosocomial pneumonia without multidrug-resistant risk factors?",
     ans="Ceftriaxone", src=("PU", 22),
     why="With no risk factors for multidrug-resistant pathogens, ceftriaxone (a third-generation cephalosporin) is a limited-spectrum option.",
     wrong=[("Cefepime", "Cefepime is a fourth-generation antipseudomonal cephalosporin used for broad-spectrum coverage when resistance risks exist."),
            ("Ceftazidime", "Ceftazidime is listed among the antipseudomonal cephalosporins, the broad-spectrum group, and is rarely used."),
            ("Cefuroxime", "Cefuroxime is a second- or third-generation cephalosporin listed for outpatient community-acquired pneumonia.")]),

dict(q="Which carbapenem has limited activity against Pseudomonas aeruginosa?",
     ans="Ertapenem", src=("PU", 25),
     why="Ertapenem has limited activity against Pseudomonas aeruginosa, which is why it is listed as a narrow-spectrum carbapenem.",
     wrong=[("Meropenem", "Meropenem is an antipseudomonal carbapenem, listed with less risk of seizures than imipenem/cilastatin."),
            ("Imipenem/cilastatin", "Imipenem/cilastatin is an antipseudomonal carbapenem; its caution is a seizure history, not weak Pseudomonas activity."),
            ("Cefepime", "Cefepime is an antipseudomonal fourth-generation cephalosporin; the carbapenem with weak Pseudomonas activity is ertapenem.")]),

dict(q="Which antipseudomonal carbapenem is used with caution in patients with a seizure history?",
     ans="Imipenem/cilastatin", src=("PU", 25),
     why="Imipenem/cilastatin (Primaxin) is used with caution in patients with a seizure history; meropenem carries less seizure risk.",
     wrong=[("Meropenem", "Meropenem (Merrem) is the carbapenem listed with LESS risk for seizures, the alternative to imipenem/cilastatin."),
            ("Ertapenem", "Ertapenem is noted for limited activity against Pseudomonas aeruginosa; the seizure caution belongs to imipenem/cilastatin."),
            ("Piperacillin/tazobactam", "Piperacillin/tazobactam is an antipseudomonal penicillin needing renal adjustment; the seizure caution is imipenem's.")]),

dict(q="Which carbapenem is listed with less risk for seizures?",
     ans="Meropenem", src=("PU", 25),
     why="Meropenem (Merrem) is the antipseudomonal carbapenem with less risk for seizures than imipenem/cilastatin.",
     wrong=[("Imipenem/cilastatin", "Imipenem/cilastatin is the carbapenem that needs caution in a seizure history, the opposite of this point."),
            ("Ertapenem", "Ertapenem's listed point is limited activity against Pseudomonas aeruginosa, not a lower seizure risk."),
            ("Ceftazidime", "Ceftazidime is an antipseudomonal cephalosporin, not a carbapenem; the low-seizure carbapenem is meropenem.")]),

dict(q="Which antipseudomonal cephalosporin is a fourth-generation cephalosporin?",
     ans="Cefepime", src=("PU", 24),
     why="Cefepime (Maxipime) is the fourth-generation antipseudomonal cephalosporin; like ceftazidime, it requires renal adjustment.",
     wrong=[("Ceftazidime", "Ceftazidime (Fortaz) is the other antipseudomonal cephalosporin; fourth generation is the label given to cefepime."),
            ("Ceftriaxone", "Ceftriaxone is a third-generation cephalosporin used for limited-spectrum coverage, not an antipseudomonal agent."),
            ("Cefotaxime", "Cefotaxime is an intravenous beta-lactam for inpatient community pneumonia; cefepime is the fourth-generation agent.")]),

dict(q="Which antipseudomonal penicillin combination is sold as Zosyn?",
     ans="Piperacillin/tazobactam", src=("PU", 26),
     why="Piperacillin/tazobactam (Zosyn) is an antipseudomonal penicillin with a beta-lactamase inhibitor; it requires renal adjustment.",
     wrong=[("Ticarcillin/clavulanate", "Ticarcillin/clavulanate is sold as Timentin and is not used very often because of gram-negative resistance."),
            ("Imipenem/cilastatin", "Imipenem/cilastatin is sold as Primaxin; it is an antipseudomonal carbapenem, not a penicillin."),
            ("Ampicillin/sulbactam", "Ampicillin/sulbactam is a limited-spectrum option for nosocomial pneumonia, not the antipseudomonal Zosyn.")]),

dict(q="Which antipseudomonal fluoroquinolone is not listed as a respiratory fluoroquinolone for community-acquired pneumonia?",
     ans="Ciprofloxacin", src=("PU", 27, 14),     # 14: the respiratory fluoroquinolone list (levofloxacin, moxifloxacin)
     why="Ciprofloxacin (Cipro) and levofloxacin are the antipseudomonal fluoroquinolones; only levofloxacin also appears with moxifloxacin as a respiratory fluoroquinolone.",
     wrong=[("Levofloxacin", "Levofloxacin is both antipseudomonal and listed with moxifloxacin as a respiratory fluoroquinolone for pneumonia."),
            ("Moxifloxacin", "Moxifloxacin is a respiratory fluoroquinolone for community pneumonia but is not on the antipseudomonal list."),
            ("Tobramycin", "Tobramycin is an aminoglycoside, the other gram-negative partner in combination therapy, not a fluoroquinolone.")]),

dict(q="Which antibiotic gives great methicillin-resistant Staphylococcus aureus coverage with no dose adjustment for renal function?",
     ans="Linezolid", src=("PU", 30),
     why="Linezolid (Zyvox) has great methicillin-resistant Staphylococcus aureus coverage, intravenous and oral forms, good lung penetration and no renal adjustment.",
     wrong=[("Vancomycin", "Vancomycin also covers methicillin-resistant Staphylococcus aureus but requires renal adjustment and trough monitoring."),
            ("Gentamicin", "Gentamicin is an aminoglycoside whose dosing is highly dependent on renal function, with ototoxicity and nephrotoxicity."),
            ("Cefepime", "Cefepime is an antipseudomonal cephalosporin that requires renal adjustment; gram-positive coverage is vancomycin or linezolid.")]),

dict(q="Which drug is primarily used for empiric methicillin-resistant Staphylococcus aureus coverage, with a trough drawn before the third or fourth dose?",
     ans="Vancomycin", src=("PU", 29),
     why="Vancomycin is primarily used for empiric methicillin-resistant Staphylococcus aureus coverage; its trough is drawn before the third or fourth dose, at steady state.",
     wrong=[("Linezolid", "Linezolid also covers methicillin-resistant Staphylococcus aureus but needs no renal dose adjustment, and no trough is listed for it."),
            ("Amikacin", "Amikacin is an aminoglycoside for gram-negative combination therapy, adjusted on levels; gram-positive coverage is vancomycin or linezolid."),
            ("Meropenem", "Meropenem is an antipseudomonal carbapenem for gram-negative coverage; gram-positive coverage is vancomycin or linezolid.")]),

dict(q="Which antibiotic class uses extended-interval (once daily or longer) dosing because of poor lung penetration?",
     ans="Aminoglycosides", src=("PU", 28),
     why="Aminoglycosides (gentamicin, tobramycin, amikacin) use extended-interval dosing: poor lung penetration means bigger doses for higher concentrations.",
     wrong=[("Antipseudomonal fluoroquinolones", "Antipseudomonal fluoroquinolones are listed with GOOD lung tissue penetration, the opposite of the aminoglycosides."),
            ("Antipseudomonal carbapenems", "Antipseudomonal carbapenems are listed for renal adjustment and seizure risk, not extended-interval dosing."),
            ("Antipseudomonal cephalosporins", "Antipseudomonal cephalosporins (ceftazidime, cefepime) are listed for renal adjustment, not extended-interval dosing.")]),

# Dr. Wood: a regimen-validity question "will be on the test" (name each drug's class, then judge the regimen).
dict(q="Broad nosocomial coverage pairs an antipseudomonal beta-lactam with which second gram-negative class?",
     ans="Aminoglycosides", src=("PU", 23),
     why="Broad coverage is an antipseudomonal beta-lactam PLUS an antipseudomonal fluoroquinolone or an aminoglycoside, PLUS vancomycin or linezolid.",
     wrong=[("Antipseudomonal carbapenems", "Carbapenems are themselves beta-lactams; two beta-lactams together do not make the gram-negative pair."),
            ("Third-generation cephalosporins", "Third-generation cephalosporins are beta-lactams, like the one already in the regimen; the second gram-negative class is an antipseudomonal fluoroquinolone or an aminoglycoside."),
            ("Macrolides", "Macrolides partner a beta-lactam in community-acquired pneumonia, not in broad nosocomial coverage.")]),

dict(q="Which drug supplies the gram-positive coverage in a broad regimen of meropenem plus amikacin?",
     ans="Vancomycin", src=("PU", 23),
     why="Meropenem (antipseudomonal carbapenem) plus amikacin (aminoglycoside) is the gram-negative pair; vancomycin or linezolid adds gram-positive coverage.",
     wrong=[("Piperacillin-tazobactam", "Piperacillin-tazobactam is another antipseudomonal beta-lactam, a gram-negative agent like meropenem; the gram-positive drug is vancomycin or linezolid."),
            ("Gentamicin", "Gentamicin is another aminoglycoside, a gram-negative agent; the gram-positive drug is vancomycin or linezolid."),
            ("Levofloxacin", "Levofloxacin is an antipseudomonal fluoroquinolone, a gram-negative agent; the gram-positive drug is vancomycin or linezolid.")]),

# ---- tuberculosis (slides 37-45; the slide 46 second-line list is out of scope) ----
dict(q="Which tuberculosis drug causes peripheral neuritis from pyridoxine deficiency, so pyridoxine (vitamin B6) is given?",
     ans="Isoniazid", src=("PU", 39),
     why="Isoniazid causes peripheral neuritis through pyridoxine deficiency, so pyridoxine (vitamin B6) is given with it.",
     wrong=[("Rifampin", "Rifampin's signature effects are orange secretions, enzyme induction and a flu-like syndrome, not pyridoxine deficiency."),
            ("Ethambutol", "Ethambutol's signature effects are visual: decreased red-green discrimination and visual acuity."),
            ("Pyrazinamide", "Pyrazinamide's signature effects are hepatitis and hyperuricemia from blocked uric acid excretion.")]),

# Repair 2026-10-27: rifampin is no longer offered (rifampin alone is a current latent-tuberculosis regimen, so it could be
# defended); ethambutol and pyrazinamide are already choices, so doxycycline stands in, as in the vignette pool's version.
dict(q="Which tuberculosis drug is used alone for prophylaxis?",
     ans="Isoniazid", src=("PU", 39),
     why="Isoniazid is used alone for prophylaxis and in combination for active disease.",
     wrong=[("Doxycycline", "Doxycycline is not a tuberculosis drug; it is a second-line outpatient choice for community-acquired pneumonia, while isoniazid alone is the prophylactic drug."),
            ("Ethambutol", "Ethambutol develops resistance quickly if used alone, so it is not the drug listed for single-agent prophylaxis."),
            ("Pyrazinamide", "Pyrazinamide is given only in the first two months of combined therapy, to avoid liver toxicity.")]),

dict(q="Which tuberculosis drug is metabolically activated by bacterial catalase-peroxidase?",
     ans="Isoniazid", src=("PU", 38),
     why="Isoniazid is metabolically activated by bacterial catalase-peroxidase; resistance comes from a mutation in the gene for that enzyme.",
     wrong=[("Pyrazinamide", "Pyrazinamide is converted to pyrazinoic acid, which lowers the pH so the bacteria cannot grow."),
            ("Rifampin", "Rifampin acts directly by forming a complex with bacterial DNA-dependent RNA polymerase, with no activation step."),
            ("Ethambutol", "Ethambutol inhibits mycolic acid incorporation into membranes; no bacterial activating enzyme is listed for it.")]),

dict(q="Which tuberculosis drug can cause a lupus-like syndrome?",
     ans="Isoniazid", src=("PU", 39),
     why="Isoniazid's allergic reactions include a lupus-like syndrome, alongside hepatitis, peripheral neuritis and central nervous system effects.",
     wrong=[("Rifampin", "Rifampin's hypersensitivity is a flu-like syndrome in 20 percent of patients, not a lupus-like syndrome."),
            ("Ethambutol", "Ethambutol's adverse effects are visual disturbances and increased uric acid, not a lupus-like syndrome."),
            ("Pyrazinamide", "Pyrazinamide's adverse effects are hepatitis and hyperuricemia, and it is avoided in pregnancy.")]),

dict(q="Which tuberculosis drug is excreted mostly as an acetylated metabolite, with fast and slow acetylators?",
     ans="Isoniazid", src=("PU", 37),
     why="Isoniazid is 75 to 95 percent excreted as an acetylated metabolite, and its half-life differs between fast and slow acetylators.",
     wrong=[("Ethambutol", "Ethambutol is 75 percent excreted unchanged, so its dose is adjusted in renal disease; it is not acetylated."),
            ("Rifampin", "Rifampin's metabolic point is induction of cytochrome P450 enzymes, not acetylation."),
            ("Pyrazinamide", "Pyrazinamide is converted to pyrazinoic acid; acetylator status is listed for isoniazid.")]),

dict(q="Which tuberculosis drug colors tears, sweat and urine orange?",
     ans="Rifampin", src=("PU", 42),
     why="Rifampin colors secretions orange (tears, sweat, urine); patients should be told to expect it.",
     wrong=[("Isoniazid", "Isoniazid's signature effect is peripheral neuritis from pyridoxine deficiency, not discolored secretions."),
            ("Ethambutol", "Ethambutol's signature effect is decreased red-green color discrimination, not orange secretions."),
            ("Pyrazinamide", "Pyrazinamide's signature effect is hyperuricemia from blocked uric acid excretion, not orange secretions.")]),

dict(q="Which tuberculosis drug induces cytochrome P450 enzymes, lowering anticoagulants and contraceptives?",
     ans="Rifampin", src=("PU", 42),
     why="Rifampin induces cytochrome P450 enzymes (CYP1A2, CYP2C9, CYP3A4), affecting anticoagulants, contraceptives, digoxin, ketoconazole and theophylline.",
     wrong=[("Isoniazid", "Isoniazid's listed problems are hepatitis, peripheral neuritis and central nervous system effects, not enzyme induction."),
            ("Ethambutol", "Ethambutol is mostly excreted unchanged by the kidneys and is not listed as an enzyme inducer."),
            ("Pyrazinamide", "Pyrazinamide's listed problems are hepatitis, hyperuricemia and avoidance in pregnancy, not enzyme induction.")]),

dict(q="Which tuberculosis drug inhibits bacterial DNA-dependent RNA polymerase?",
     ans="Rifampin", src=("PU", 41),
     why="Rifampin inhibits DNA-dependent RNA polymerase by forming a complex with the enzyme, with no effect on the human enzyme.",
     wrong=[("Isoniazid", "Isoniazid inhibits mycolic acid production, the waxy cell coat, rather than RNA polymerase."),
            ("Ethambutol", "Ethambutol inhibits mycolic acid incorporation into membranes, weakening the cell wall."),
            ("Pyrazinamide", "Pyrazinamide is converted to pyrazinoic acid, lowering the pH so the bacteria cannot grow.")]),

dict(q="Which tuberculosis drug is also used for prophylaxis of meningococcal disease?",
     ans="Rifampin", src=("PU", 41),
     why="Rifampin's primary use is tuberculosis, with meningococcal disease prophylaxis and endocarditis also listed.",
     wrong=[("Isoniazid", "Isoniazid's prophylactic use is for tuberculosis itself, given alone; meningococcal prophylaxis is rifampin's."),
            ("Ethambutol", "Ethambutol is a bacteriostatic tuberculosis drug with no listed use outside tuberculosis."),
            ("Pyrazinamide", "Pyrazinamide is given only in the first two months of tuberculosis therapy and has no listed meningococcal use.")]),

dict(q="Which tuberculosis drug causes a flu-like hypersensitivity syndrome in about 20 percent of patients?",
     ans="Rifampin", src=("PU", 42),
     why="Rifampin's hypersensitivity is a flu-like syndrome in about 20 percent of patients; it also causes jaundice, hepatitis and gastrointestinal upset.",
     wrong=[("Isoniazid", "Isoniazid's allergic reaction is a lupus-like syndrome, not a flu-like syndrome."),
            ("Ethambutol", "Ethambutol's adverse effects are visual disturbances and increased uric acid levels."),
            ("Pyrazinamide", "Pyrazinamide's adverse effects are hepatitis and hyperuricemia in nearly all patients, not a flu-like syndrome.")]),

dict(q="Which tuberculosis drug decreases red-green color discrimination?",
     ans="Ethambutol", src=("PU", 44),
     why="Ethambutol causes visual disturbances, decreased red-green discrimination and decreased visual acuity.",
     wrong=[("Isoniazid", "Isoniazid causes peripheral neuritis from pyridoxine deficiency, not loss of red-green discrimination."),
            ("Rifampin", "Rifampin colors tears, sweat and urine orange but does not reduce red-green discrimination."),
            ("Pyrazinamide", "Pyrazinamide causes hepatitis and hyperuricemia, not visual disturbances.")]),

dict(q="Which tuberculosis drug is 75 percent excreted unchanged, so its dose is adjusted in renal disease?",
     ans="Ethambutol", src=("PU", 44),
     why="Ethambutol is 75 percent excreted unchanged, so the dose is adjusted in renal disease; resistance develops quickly if it is used alone.",
     wrong=[("Isoniazid", "Isoniazid is 75 to 95 percent excreted as an ACETYLATED metabolite, not unchanged."),
            ("Rifampin", "Rifampin is listed for enzyme induction and liver effects; renal adjustment for unchanged excretion is ethambutol's."),
            ("Pyrazinamide", "Pyrazinamide is converted to pyrazinoic acid and limited to two months to spare the liver.")]),

dict(q="Which drug weakens the mycobacterial cell wall so other tuberculosis agents gain better access?",
     ans="Ethambutol", src=("PU", 43),
     why="Ethambutol inhibits mycolic acid incorporation into membranes; the weakened cell wall lets other agents in more easily.",
     wrong=[("Rifampin", "Rifampin inhibits DNA-dependent RNA polymerase rather than weakening the cell wall for other drugs."),
            ("Pyrazinamide", "Pyrazinamide lowers the pH through pyrazinoic acid and enters macrophages; it does not weaken the wall."),
            ("Gentamicin", "Gentamicin is an aminoglycoside for gram-negative pneumonia coverage, dosed by levels; it does not act on the mycobacterial wall.")]),

dict(q="Which tuberculosis drug is converted to pyrazinoic acid, lowering the pH so bacteria cannot grow?",
     ans="Pyrazinamide", src=("PU", 45),
     why="Pyrazinamide is converted to pyrazinoic acid, which lowers the pH so the bacteria cannot grow; it also enters macrophages.",
     wrong=[("Isoniazid", "Isoniazid is activated by bacterial catalase-peroxidase and inhibits mycolic acid production."),
            ("Ethambutol", "Ethambutol inhibits mycolic acid incorporation into membranes; it is not converted to an acid."),
            ("Rifampin", "Rifampin inhibits DNA-dependent RNA polymerase and is not converted to pyrazinoic acid.")]),

dict(q="Which tuberculosis drug is stopped after two months specifically to avoid liver toxicity?",
     ans="Pyrazinamide", src=("PU", 45),
     why="Pyrazinamide shortens combined therapy and is given for the first two months only, to avoid liver toxicity.",
     wrong=[("Isoniazid", "Isoniazid continues for the whole course: two months with three other drugs, then four months with rifampin."),
            ("Rifampin", "Rifampin continues with isoniazid for the four months that follow the first two."),
            ("Ethambutol", "Ethambutol also leaves the regimen after two months, but its concerns are vision and renal dosing, not the liver.")]),

dict(q="Which tuberculosis drug is to be avoided in pregnancy?",
     ans="Pyrazinamide", src=("PU", 45),
     why="Pyrazinamide's adverse effect list ends with avoid in pregnancy, after hepatitis and hyperuricemia.",
     wrong=[("Isoniazid", "Isoniazid's listed problems are hepatitis, peripheral neuritis, lupus-like reactions and central nervous system effects."),
            ("Rifampin", "Rifampin's listed problems are enzyme induction, hepatitis, orange secretions and a flu-like syndrome."),
            ("Ethambutol", "Ethambutol's listed problems are visual disturbances and increased uric acid; avoidance in pregnancy is listed for pyrazinamide.")]),

dict(q="Which drug inhibits uric acid excretion so that all patients taking it become hyperuricemic?",
     ans="Pyrazinamide", src=("PU", 45),
     why="Pyrazinamide inhibits uric acid excretion, and all patients become hyperuricemic; it also causes hepatitis in about 15 percent.",
     wrong=[("Isoniazid", "Isoniazid's signature effect is peripheral neuritis from pyridoxine deficiency, not hyperuricemia."),
            ("Rifampin", "Rifampin's signature effects are orange secretions and cytochrome P450 induction, not hyperuricemia."),
            ("Vancomycin", "Vancomycin's listed adverse effects are ototoxicity and nephrotoxicity with other nephrotoxins, not hyperuricemia.")]),


# ---- anaphylaxis (slides 51-55) ----
dict(q="Which anaphylaxis drug acts on both alpha and beta receptors?",
     ans="Epinephrine", src=("PU", 51),
     why="Epinephrine, an endogenous catecholamine, acts on alpha receptors (vasoconstriction, less vascular permeability) and beta receptors (bronchial relaxation).",
     wrong=[("Albuterol", "Albuterol is a beta-2 agonist that relaxes bronchial smooth muscle; it has no listed alpha effect."),
            ("Diphenhydramine", "Diphenhydramine is a histamine H1 blocker that relieves rash, pruritus and hives, not an adrenergic agonist."),
            ("Famotidine", "Famotidine is a histamine H2 blocker for the systemic and gastrointestinal effects, not an adrenergic agonist.")]),

dict(q="Which anaphylaxis drug, in overdose, can cause cerebrovascular hemorrhage, myocardial infarction and pulmonary edema?",
     ans="Epinephrine", src=("PU", 52),
     why="Epinephrine overdose can lead to cerebrovascular hemorrhage, myocardial infarction and pulmonary edema; the intramuscular route is preferred unless the patient is coding.",
     wrong=[("Methylprednisolone", "Methylprednisolone is a corticosteroid that takes several hours to work; it is not listed with these overdose effects."),
            ("Hydroxyzine", "Hydroxyzine is a histamine H1 blocker for the cutaneous effects; it is not listed with these overdose effects."),
            ("Famotidine", "Famotidine is a histamine H2 blocker for systemic and gastrointestinal effects, with no listed overdose effects.")]),

dict(q="Which drug used in anaphylaxis is a histamine H2 blocker?",
     ans="Famotidine", src=("PU", 53),
     why="Famotidine is the histamine H2 blocker; it blocks the systemic (vasodilation) and gastrointestinal effects such as increased gastric acid.",
     wrong=[("Diphenhydramine", "Diphenhydramine is a histamine H1 blocker that relieves the cutaneous effects: rash, pruritus and hives."),
            ("Hydroxyzine", "Hydroxyzine is a histamine H1 blocker, listed with diphenhydramine for the cutaneous effects."),
            ("Albuterol", "Albuterol is a beta-2 agonist bronchodilator, not a histamine blocker.")]),

dict(q="Which histamine H1 blocker is listed with diphenhydramine for anaphylaxis?",
     ans="Hydroxyzine", src=("PU", 53),
     why="The histamine H1 blockers are diphenhydramine and hydroxyzine; they relieve rash, pruritus and hives.",
     wrong=[("Famotidine", "Famotidine is the histamine H2 blocker, for the systemic and gastrointestinal effects."),
            ("Albuterol", "Albuterol is a beta-2 agonist that relaxes bronchial smooth muscle, not a histamine blocker."),
            ("Prednisone", "Prednisone is a corticosteroid that blocks inflammatory mediators over several hours, not a histamine blocker.")]),

dict(q="Which anaphylaxis drug blocks inflammatory mediators at the cellular level but takes several hours to work?",
     ans="Methylprednisolone", src=("PU", 55),
     why="Corticosteroids such as methylprednisolone (intramuscular, intravenous) block inflammatory mediator production and work on all aspects, but take several hours.",
     wrong=[("Epinephrine", "Epinephrine acts at once on alpha and beta receptors; it is the fast drug, not the one that takes hours."),
            ("Diphenhydramine", "Diphenhydramine blocks histamine H1 receptors to relieve the cutaneous effects; it does not block mediator production."),
            ("Albuterol", "Albuterol is a beta-2 agonist that relaxes bronchial smooth muscle, not an anti-inflammatory agent.")]),

# ---- asthma bronchodilators (slides 68-87) ----
dict(q="Which short-acting beta-2 agonist is sold as Xopenex?",
     ans="Levalbuterol", src=("PU", 70),
     why="Levalbuterol (Xopenex) is the short-acting beta-2 agonist listed with albuterol (ProAir, Ventolin).",
     wrong=[("Albuterol", "Albuterol is the other short-acting beta-2 agonist, sold as ProAir and Ventolin."),
            ("Formoterol", "Formoterol (Foradil) is a long-acting beta-2 agonist, never used alone for asthma."),
            ("Salmeterol", "Salmeterol (Serevent) is a long-acting beta-2 agonist, never used alone for asthma.")]),

dict(q="Which long-acting beta-2 agonist is sold as Serevent?",
     ans="Salmeterol", src=("PU", 70),
     why="Salmeterol (Serevent) is a long-acting beta-2 agonist; long-acting agents are not to be used alone for asthma.",
     wrong=[("Formoterol", "Formoterol is the other long-acting beta-2 agonist, sold as Foradil."),
            ("Levalbuterol", "Levalbuterol is a short-acting beta-2 agonist sold as Xopenex."),
            ("Albuterol", "Albuterol is a short-acting beta-2 agonist sold as ProAir and Ventolin.")]),

dict(q="Foradil is the brand name of which long-acting beta-2 agonist?",
     ans="Formoterol", src=("PU", 70),
     why="Formoterol (Foradil) is a long-acting beta-2 agonist; it is paired with budesonide (Symbicort) and mometasone (Dulera).",
     wrong=[("Salmeterol", "Salmeterol is the other long-acting beta-2 agonist, sold as Serevent and paired with fluticasone in Advair."),
            ("Levalbuterol", "Levalbuterol is a short-acting beta-2 agonist sold as Xopenex."),
            ("Tiotropium", "Tiotropium is a long-acting anticholinergic sold as Spiriva, not a beta-2 agonist.")]),

dict(q="Which beta-2 agonist is sold as ProAir and Ventolin?",
     ans="Albuterol", src=("PU", 70),
     why="Albuterol (ProAir, Ventolin) is a short-acting beta-2 agonist, listed with levalbuterol (Xopenex).",
     wrong=[("Levalbuterol", "Levalbuterol is the other short-acting beta-2 agonist, sold as Xopenex."),
            ("Salmeterol", "Salmeterol is a long-acting beta-2 agonist sold as Serevent."),
            ("Ipratropium", "Ipratropium is a short-acting anticholinergic sold as Atrovent, not a beta-2 agonist.")]),

dict(q="Which drug class must never be used alone for asthma?",
     ans="Long-acting beta-2 agonists", src=("PU", 70, 67),     # 67: the long-term controller list
     why="Long-acting beta-2 agonists (formoterol, salmeterol) are not to be used alone for asthma; they are paired with an inhaled corticosteroid.",
     wrong=[("Inhaled corticosteroids", "Inhaled corticosteroids are long-term controller medications; the no-monotherapy rule is for long-acting beta-2 agonists, which are paired with them."),
            ("Leukotriene modifiers", "Leukotriene modifiers are long-term controller medications too; the no-monotherapy rule is for long-acting beta-2 agonists."),
            ("Short-acting beta-2 agonists", "Short-acting beta-2 agonists are used as needed for quick relief; the no-monotherapy rule is for the long-acting ones.")]),

dict(q="Which bronchodilator class raises cyclic adenosine monophosphate (cAMP) by stimulating a receptor on airway smooth muscle?",
     ans="Beta-2 agonists", src=("PU", 68),
     why="Beta-2 agonists stimulate the beta-2 receptor, increasing cyclic adenosine monophosphate (cAMP) and relaxing airway smooth muscle.",
     wrong=[("Methylxanthines", "Methylxanthines such as theophylline raise cyclic adenosine monophosphate by inhibiting phosphodiesterase, not via a receptor."),
            ("Anticholinergics", "Anticholinergics block acetylcholine at muscarinic receptors; they do not stimulate a receptor."),
            ("Leukotriene modifiers", "Leukotriene modifiers block the leukotriene D4 receptor; they are long-term controllers, not receptor-stimulating bronchodilators.")]),

dict(q="Which bronchodilator is a nonspecific phosphodiesterase inhibitor with a narrow therapeutic index?",
     ans="Theophylline", src=("PU", 82),
     why="Theophylline, a methylxanthine, is a nonspecific phosphodiesterase inhibitor with a narrow therapeutic index, so its plasma level is monitored.",
     wrong=[("Albuterol", "Albuterol is a short-acting beta-2 agonist that raises cyclic adenosine monophosphate through the beta-2 receptor."),
            ("Ipratropium", "Ipratropium is a short-acting anticholinergic that blocks muscarinic receptors."),
            ("Montelukast", "Montelukast is a leukotriene receptor antagonist taken by mouth, not a phosphodiesterase inhibitor.")]),

dict(q="Which bronchodilator antagonizes the adenosine A2B receptor?",
     ans="Theophylline", src=("PU", 83),
     why="Theophylline inhibits phosphodiesterase (raising cyclic adenosine and guanosine monophosphate), antagonizes the adenosine A2B receptor and has anti-inflammatory actions.",
     wrong=[("Tiotropium", "Tiotropium is a long-acting anticholinergic that blocks muscarinic receptors, not adenosine receptors."),
            ("Salmeterol", "Salmeterol is a long-acting beta-2 agonist that stimulates beta-2 receptors, not an adenosine antagonist."),
            ("Ketamine", "Ketamine is an NMDA (N-methyl-D-aspartate) receptor antagonist that increases catecholamine release.")]),

dict(q="Which drug is the intravenous form of theophylline?",
     ans="Aminophylline", src=("PU", 82),
     why="Aminophylline is the intravenous form of theophylline, the methylxanthine.",
     wrong=[("Ipratropium", "Ipratropium is a short-acting inhaled anticholinergic, not a methylxanthine."),
            ("Levalbuterol", "Levalbuterol is a short-acting inhaled beta-2 agonist, not a form of theophylline."),
            ("Magnesium", "Magnesium is given as a bolus and infusion in status asthmaticus; it is not a form of theophylline.")]),

dict(q="Which short-acting anticholinergic lasts up to 8 hours?",
     ans="Ipratropium", src=("PU", 86),
     why="Ipratropium (Atrovent) is the short-acting anticholinergic, lasting up to 8 hours; it blocks acetylcholine at muscarinic receptors.",
     wrong=[("Tiotropium", "Tiotropium (Spiriva) is the LONG-acting anticholinergic, lasting 24 hours or more."),
            ("Albuterol", "Albuterol is a short-acting beta-2 agonist lasting 4 to 6 hours, not an anticholinergic."),
            ("Salmeterol", "Salmeterol is a long-acting beta-2 agonist lasting 12 or more hours, not an anticholinergic.")]),

dict(q="Which long-acting anticholinergic is sold as Spiriva?",
     ans="Tiotropium", src=("PU", 86),
     why="Tiotropium (Spiriva) is the long-acting anticholinergic, lasting 24 hours or more.",
     wrong=[("Ipratropium", "Ipratropium is the short-acting anticholinergic, sold as Atrovent and lasting up to 8 hours."),
            ("Formoterol", "Formoterol is a long-acting beta-2 agonist sold as Foradil, not an anticholinergic."),
            ("Mometasone", "Mometasone is an inhaled corticosteroid sold as Asmanex, not an anticholinergic.")]),

dict(q="Which drug class causes the side effects remembered as dry as a bone, blind as a bat and red as a beet?",
     ans="Anticholinergics", src=("PU", 87),
     why="Anticholinergic side effects: dry mouth and eyes, blurry vision and mydriasis, flushing, fever, delirium, constipation, urinary retention and tachycardia.",
     wrong=[("Beta-2 agonists", "Beta-2 agonist adverse effects are tachycardia, tremor, headache, dizziness, insomnia and hyperglycemia, not dryness."),
            ("Methylxanthines", "Methylxanthines cause arrhythmias, convulsions, headaches, nausea, insomnia and heartburn, not this pattern."),
            ("Inhaled corticosteroids", "Inhaled corticosteroids cause oral candidiasis, growth suppression in children and immune suppression.")]),

# ---- asthma controllers (slides 72-89) ----
dict(q="Which leukotriene modifier antagonizes the leukotriene D4 (cysteinyl leukotriene 1) receptor?",
     ans="Montelukast", src=("PU", 75),
     why="Montelukast (Singulair), an oral leukotriene antagonist, blocks the leukotriene D4 receptor that mediates inflammation, bronchoconstriction and mucus.",
     wrong=[("Cromolyn sodium", "Cromolyn sodium is an inhaled mast cell stabilizer whose mechanism is unknown (it may interfere with calcium)."),
            ("Nedocromil", "Nedocromil is an inhaled mast cell stabilizer that must be taken before the antigen insult."),
            ("Omalizumab", "Omalizumab is a monoclonal antibody that binds circulating immunoglobulin E (IgE), not a leukotriene antagonist.")]),

dict(q="Which asthma controller is effective in aspirin-induced asthma?",
     ans="Montelukast", src=("PU", 75),
     why="Montelukast, the leukotriene D4 receptor antagonist, is listed as effective in aspirin-induced asthma.",
     wrong=[("Omalizumab", "Omalizumab binds circulating immunoglobulin E (IgE) to prevent mast cell degranulation; it is not listed for aspirin-induced asthma."),
            ("Theophylline", "Theophylline is a phosphodiesterase inhibitor of limited use, mainly in chronic obstructive pulmonary disease."),
            ("Nedocromil", "Nedocromil is a mast cell stabilizer that must be taken before the antigen insult; it is not listed for aspirin-induced asthma.")]),

dict(q="Which inhaled mast cell stabilizer is sold as Tilade?",
     ans="Nedocromil", src=("PU", 78),
     why="Nedocromil (Tilade) is an inhaled mast cell stabilizer that may take up to 4 weeks to work and must be taken regularly.",
     wrong=[("Cromolyn sodium", "Cromolyn sodium is the other mast cell stabilizer; the Tilade brand belongs to nedocromil."),
            ("Montelukast", "Montelukast is an oral leukotriene antagonist sold as Singulair, not a mast cell stabilizer."),
            ("Mometasone", "Mometasone is an inhaled corticosteroid sold as Asmanex, not a mast cell stabilizer.")]),

dict(q="Which asthma controller class must be taken before the antigen insult and may take up to 4 weeks to work?",
     ans="Mast cell stabilizers", src=("PU", 78),
     why="Mast cell stabilizers (cromolyn sodium, nedocromil) must be taken before the antigen insult and regularly; they may take up to 4 weeks to work.",
     wrong=[("Inhaled corticosteroids", "Inhaled corticosteroids inhibit the inflammatory cascade and take up to 8 weeks for maximal effect."),
            ("Leukotriene modifiers", "Leukotriene modifiers block the leukotriene D4 receptor; the before-the-insult rule is for mast cell stabilizers."),
            ("Short-acting beta-2 agonists", "Short-acting beta-2 agonists work rapidly and last 4 to 6 hours; they are quick relief, not pretreatment.")]),

dict(q="Which asthma drug is a humanized monoclonal antibody that binds circulating immunoglobulin E (IgE)?",
     ans="Omalizumab", src=("PU", 79),
     why="Omalizumab (Xolair), given subcutaneously, binds circulating immunoglobulin E, which decreases high-affinity receptors on mast cells and prevents degranulation.",
     wrong=[("Mepolizumab", "Mepolizumab (Nucala) is in the anti-interleukin-5 group for the eosinophilic phenotype, not an anti-immunoglobulin E antibody."),
            ("Dupilumab", "Dupilumab (Dupixent) is the anti-interleukin-4 biologic, not an anti-immunoglobulin E antibody."),
            ("Reslizumab", "Reslizumab (Cinqair) is an anti-interleukin-5 biologic given intravenously, not an anti-immunoglobulin E antibody.")]),

# Repair 2026-10-27: replaces "Which biologic for eosinophilic asthma is given intravenously?" (slide 81 sets "Given IV"
# under the whole anti-interleukin-5 list, so mepolizumab was defensible from the slide). The brand is unambiguous.
dict(q="Which asthma biologic is sold as Dupixent?",
     ans="Dupilumab", src=("PU", 81),
     why="Dupilumab (Dupixent) is the anti-interleukin-4 biologic, used with the anti-interleukin-5 drugs for the eosinophilic phenotype.",
     wrong=[("Mepolizumab", "Mepolizumab is the anti-interleukin-5 biologic sold as Nucala; Dupixent is dupilumab."),
            ("Reslizumab", "Reslizumab is the anti-interleukin-5 biologic sold as Cinqair; Dupixent is dupilumab."),
            ("Omalizumab", "Omalizumab is the anti-immunoglobulin E antibody sold as Xolair; Dupixent is dupilumab.")]),

dict(q="Which asthma biologic is sold as Nucala?",
     ans="Mepolizumab", src=("PU", 81),
     why="Mepolizumab (Nucala) is in the anti-interleukin-5 group, used for the eosinophilic phenotype.",
     wrong=[("Dupilumab", "Dupilumab is sold as Dupixent and is the anti-interleukin-4 biologic."),
            ("Omalizumab", "Omalizumab is sold as Xolair and is the anti-immunoglobulin E antibody."),
            ("Reslizumab", "Reslizumab is sold as Cinqair and is the anti-interleukin-5 biologic given intravenously.")]),

dict(q="Which asthma biologic is sold as Fasenra?",
     ans="Benralizumab", src=("PU", 81),
     why="Benralizumab (Fasenra) is listed in the anti-interleukin-5 group for the eosinophilic phenotype.",
     wrong=[("Dupilumab", "Dupilumab is sold as Dupixent and is the anti-interleukin-4 biologic."),
            ("Omalizumab", "Omalizumab is sold as Xolair and binds circulating immunoglobulin E."),
            ("Reslizumab", "Reslizumab is sold as Cinqair and is the anti-interleukin-5 biologic given intravenously.")]),

dict(q="Which inhaled corticosteroid is sold as Flovent?",
     ans="Fluticasone", src=("PU", 72),
     why="Fluticasone (Flovent) is an inhaled corticosteroid; with salmeterol it makes Advair.",
     wrong=[("Budesonide", "Budesonide is sold as Pulmicort and, with formoterol, makes Symbicort."),
            ("Beclomethasone", "Beclomethasone is the inhaled corticosteroid sold as QVAR, a different brand."),
            ("Mometasone", "Mometasone is sold as Asmanex and, with formoterol, makes Dulera.")]),

dict(q="Which inhaled corticosteroid is sold as Pulmicort?",
     ans="Budesonide", src=("PU", 72),
     why="Budesonide (Pulmicort) is an inhaled corticosteroid; with formoterol it makes Symbicort.",
     wrong=[("Fluticasone", "Fluticasone is sold as Flovent and, with salmeterol, makes Advair."),
            ("Flunisolide", "Flunisolide is the inhaled corticosteroid sold as Aerobid, a different brand."),
            ("Triamcinolone", "Triamcinolone is the inhaled corticosteroid sold as Azmacort, a different brand.")]),

dict(q="Which inhaled corticosteroid is sold as QVAR?",
     ans="Beclomethasone", src=("PU", 72),
     why="Beclomethasone (QVAR) is an inhaled corticosteroid; like the others it can cause oral candidiasis (thrush).",
     wrong=[("Budesonide", "Budesonide is the inhaled corticosteroid sold as Pulmicort, a different brand."),
            ("Mometasone", "Mometasone is the inhaled corticosteroid sold as Asmanex, a different brand."),
            ("Fluticasone", "Fluticasone is the inhaled corticosteroid sold as Flovent, a different brand.")]),

dict(q="Which inhaled corticosteroid is sold as Asmanex?",
     ans="Mometasone", src=("PU", 72),
     why="Mometasone (Asmanex) is an inhaled corticosteroid; with formoterol it makes Dulera.",
     wrong=[("Fluticasone", "Fluticasone is the inhaled corticosteroid sold as Flovent, a different brand."),
            ("Flunisolide", "Flunisolide is the inhaled corticosteroid sold as Aerobid, a different brand."),
            ("Beclomethasone", "Beclomethasone is the inhaled corticosteroid sold as QVAR, a different brand.")]),

dict(q="Which combination inhaler pairs salmeterol with fluticasone?",
     ans="Advair", src=("PU", 74),
     why="Advair is salmeterol/fluticasone, a long-acting beta-2 agonist with an inhaled corticosteroid.",
     wrong=[("Symbicort", "Symbicort is formoterol/budesonide, a different long-acting beta-2 agonist and corticosteroid pair."),
            ("Dulera", "Dulera is formoterol/mometasone, a different long-acting beta-2 agonist and corticosteroid pair."),
            ("Serevent", "Serevent is salmeterol alone, which must not be used alone for asthma.")]),

dict(q="Which combination inhaler pairs formoterol with budesonide?",
     ans="Symbicort", src=("PU", 74),
     why="Symbicort is formoterol/budesonide, a long-acting beta-2 agonist with an inhaled corticosteroid.",
     wrong=[("Dulera", "Dulera pairs formoterol with mometasone rather than with budesonide."),
            ("Advair", "Advair pairs salmeterol with fluticasone rather than formoterol with budesonide."),
            ("Pulmicort", "Pulmicort is budesonide alone, an inhaled corticosteroid without a beta-2 agonist.")]),

dict(q="Which combination inhaler pairs formoterol with mometasone?",
     ans="Dulera", src=("PU", 74),
     why="Dulera is formoterol/mometasone, a long-acting beta-2 agonist with an inhaled corticosteroid.",
     wrong=[("Symbicort", "Symbicort pairs formoterol with budesonide rather than with mometasone."),
            ("Advair", "Advair pairs salmeterol with fluticasone rather than formoterol with mometasone."),
            ("Asmanex", "Asmanex is mometasone alone, an inhaled corticosteroid without a beta-2 agonist.")]),

dict(q="Which asthma drug class causes oral candidiasis (thrush) and, at high dose, suppresses growth in children?",
     ans="Inhaled corticosteroids", src=("PU", 73),
     why="Inhaled corticosteroids cause oral candidiasis (thrush), suppress growth in children at high dose and can inhibit the immune system.",
     wrong=[("Leukotriene modifiers", "Leukotriene modifiers are oral receptor antagonists; thrush and growth suppression belong to the corticosteroids."),
            ("Mast cell stabilizers", "Mast cell stabilizers must be taken before the antigen insult; thrush and growth suppression are not listed for them."),
            ("Long-acting beta-2 agonists", "Long-acting beta-2 agonists cause tachycardia and tremor; thrush is the inhaled corticosteroid effect.")]),

dict(q="Which systemic corticosteroid comes as an oral liquid, sold as Ora-Pred?",
     ans="Prednisolone", src=("PU", 88),
     why="Prednisolone (Ora-Pred) is the oral liquid; prednisone (Deltasone) is the oral tablet.",
     wrong=[("Prednisone", "Prednisone (Deltasone) is listed as the oral tablet, not the oral liquid."),
            ("Methylprednisolone", "Methylprednisolone (Solu-Medrol) is listed as oral or parenteral, not as the liquid."),
            ("Dexamethasone", "Dexamethasone (Decadron) is listed as oral or parenteral, not as the oral liquid.")]),

dict(q="Which systemic corticosteroid is sold as Decadron?",
     ans="Dexamethasone", src=("PU", 88),
     why="Dexamethasone (Decadron) is given by mouth or parenterally; systemic steroids are kept for exacerbations.",
     wrong=[("Methylprednisolone", "Methylprednisolone is sold as Solu-Medrol, given by mouth or parenterally."),
            ("Prednisolone", "Prednisolone is sold as Ora-Pred, the oral liquid form, not as Decadron."),
            ("Prednisone", "Prednisone is sold as Deltasone, the oral tablet form, not as Decadron.")]),

# ---- status asthmaticus (slide 99) ----
dict(q="Which drug used in status asthmaticus for an intubated patient is an NMDA (N-methyl-D-aspartate) receptor antagonist?",
     ans="Ketamine", src=("PU", 99),
     why="Ketamine, a dissociative anesthetic used if the patient is intubated, antagonizes the N-methyl-D-aspartate receptor and increases catecholamine release, causing bronchodilation.",
     wrong=[("Methylprednisolone", "Methylprednisolone is a systemic corticosteroid; intravenous steroids are part of the status asthmaticus algorithm, but it is not an N-methyl-D-aspartate antagonist."),
            ("Albuterol", "Albuterol is a beta-2 agonist given continuously by nebulizer in status asthmaticus, not an N-methyl-D-aspartate antagonist."),
            ("Aminophylline", "Aminophylline is the intravenous form of theophylline, a phosphodiesterase inhibitor; it is not an N-methyl-D-aspartate antagonist.")]),

dict(q="Which drug used in status asthmaticus can cause an emergence phenomenon?",
     ans="Ketamine", src=("PU", 99),
     why="Ketamine's adverse reactions are emergence phenomenon, hypertension, tachycardia and vomiting.",
     wrong=[("Albuterol", "Albuterol causes tachycardia, tremor and hyperglycemia; emergence phenomenon belongs to ketamine."),
            ("Methylprednisolone", "Methylprednisolone is a systemic corticosteroid whose effects include hyperglycemia and mood change, not emergence."),
            ("Aminophylline", "Aminophylline (intravenous theophylline) causes arrhythmias and convulsions; emergence phenomenon is ketamine's.")]),

# ---- chronic obstructive pulmonary disease, smoking cessation (slides 102-107) ----
dict(q="Which drug class is the regular treatment for chronic obstructive pulmonary disease group C?",
     ans="Long-acting muscarinic antagonists", src=("PU", 102),
     why="Group C (less symptomatic, high risk) gets regular treatment with a long-acting muscarinic antagonist, with a short-acting beta-2 agonist for relief.",
     wrong=[("Long-acting beta-2 agonists", "A long-acting beta-2 agonist is an option in group B (either it or a muscarinic antagonist), not the group C choice."),
            ("Short-acting bronchodilators", "Short-acting bronchodilators as needed are the treatment for group A, the less symptomatic, low-risk group."),
            ("Inhaled corticosteroids", "A combination glucocorticoid inhaler is considered in group D when asthma features overlap, not for group C.")]),

dict(q="Which smoking cessation drug is a partial nicotine receptor agonist?",
     ans="Varenicline", src=("PU", 107),
     why="Varenicline (Chantix) is a partial nicotine receptor agonist, acting to a lesser degree than nicotine.",
     wrong=[("Bupropion", "Bupropion SR (sustained release) is thought to work by inhibiting norepinephrine and dopamine uptake, not as a nicotine agonist."),
            ("Nicotine patch", "The nicotine patch is replacement with nicotine itself, a full agonist, to reduce craving and withdrawal."),
            ("Nicotine gum", "Nicotine gum (polacrilex) replaces nicotine itself to reduce craving and withdrawal.")]),

dict(q="Which smoking cessation drug is listed with a black box warning for neuropsychiatric events?",
     ans="Varenicline", src=("PU", 107),
     why="Varenicline is listed with a black box warning for neuropsychiatric events (depression, suicidal ideation), plus nausea, sleep disturbance and headache.",
     wrong=[("Nicotine patch", "The nicotine patch is available over the counter; its listed caution is cardiovascular (tachyarrhythmias, hypertension)."),
            ("Nicotine gum", "Nicotine gum is available over the counter; its listed caution is cardiovascular disease."),
            ("Nicotine inhaler", "The nicotine inhaler is a nicotine replacement product; no boxed warning is listed for nicotine replacement.")]),

dict(q="Which smoking cessation drug is started one week before the quit date and continued for 12 weeks?",
     ans="Varenicline", src=("PU", 107),
     why="Varenicline is started one week before the quit date and continued for 12 weeks.",
     wrong=[("Nicotine patch", "Nicotine replacement duration depends on dependence, between 6 and 12 weeks; the one-week lead-in is varenicline's."),
            ("Nicotine spray", "Nicotine spray is a replacement product whose duration depends on the patient's level of dependence."),
            ("Bupropion", "Bupropion is avoided in seizure disorders and with monoamine oxidase inhibitors; the one-week lead-in is varenicline's.")]),

dict(q="Which smoking cessation drug inhibits the uptake of norepinephrine and dopamine?",
     ans="Bupropion", src=("PU", 105),
     why="Bupropion SR (sustained release; Zyban) is postulated to mimic nicotine's effects because it inhibits norepinephrine and dopamine uptake.",
     wrong=[("Varenicline", "Varenicline is a partial nicotine receptor agonist rather than an uptake inhibitor."),
            ("Nicotine patch", "The nicotine patch replaces nicotine itself to reduce craving and physical withdrawal."),
            ("Nicotine inhaler", "The nicotine inhaler replaces nicotine itself; it is not an uptake inhibitor.")]),

dict(q="Which smoking cessation drug is avoided in seizure disorders and in patients taking monoamine oxidase inhibitors?",
     ans="Bupropion", src=("PU", 105),
     why="Bupropion SR (sustained release) is avoided in seizure disorders and with monoamine oxidase inhibitors, and used with caution with tricyclic antidepressants and venlafaxine.",
     wrong=[("Varenicline", "Varenicline's listed issues are nausea, sleep disturbance, headache and a neuropsychiatric black box warning."),
            ("Nicotine patch", "Nicotine replacement's listed caution is cardiovascular disease (tachyarrhythmias, hypertension), not seizures."),
            ("Nicotine gum", "Nicotine gum is available over the counter; its caution is cardiovascular disease, not seizures.")]),

dict(q="Which nicotine replacement product is nicotine polacrilex?",
     ans="Nicotine gum", src=("PU", 104),
     why="Nicotine polacrilex is the gum; the transdermal system is the patch, with a spray and an inhaler also available.",
     wrong=[("Nicotine patch", "The patch is the nicotine transdermal system, not nicotine polacrilex."),
            ("Nicotine spray", "Nicotine spray is a separate replacement product from nicotine polacrilex (the gum)."),
            ("Nicotine inhaler", "The nicotine inhaler is a separate replacement product from nicotine polacrilex (the gum).")]),
]
