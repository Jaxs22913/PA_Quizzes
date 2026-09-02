# -*- coding: utf-8 -*-
"""Rapid-drill bank: antibacterials. One fact, four drug names, no vignette.

Jaxon, 2026-09-02: "make the Pharm questions really simple and drill, like
'Which of the following drugs causes body flushing (Red Man Syndrome)?' I want
simple sets to really drill the need to know stuff that are particular for each
drug and class and stuff that stands out."

WHAT COUNTS AS "STANDS OUT" IS NOT A JUDGEMENT CALL HERE. The three reference
sheets (indications, side effects, contraindications) already carry the
lecture's own emphasis as <b> markup, and a phrase was only made into a
question if it belongs to EXACTLY ONE drug or class across all 255 rows. That
is what keeps "hypersensitivity, rash and diarrhoea" -- true of half the
penicillins -- out, and keeps Red Man Syndrome, Achilles tendon rupture and
the imipenem seizure in.

Distractors are drugs from the same family, so the item is a real
discrimination rather than a category guess. No doses anywhere, per Dr Wood.

src is (lecture, slide) and the renderer turns it into the deck citation.
"""
L1 = "Topic — Antibacterials"

ITEMS = [
dict(q="Which drug causes body flushing, fever and chills during a rapid infusion — Red Man Syndrome?",
     ans="Vancomycin", src=("L1", 51),
     why="Red Man Syndrome, also called Vancomycin Infusion Syndrome. It is an infusion-rate reaction, not an allergy, so the answer is to slow the infusion.",
     wrong=[("Linezolid", "Its signature interaction is serotonin syndrome, not an infusion flush."),
            ("Clindamycin", "Known for Clostridium difficile and pseudomembranous colitis."),
            ("Gentamicin", "Known for renal toxicity and ototoxicity, not an infusion flush.")]),

dict(q="Which antibiotic class causes tendonitis and Achilles tendon rupture?",
     ans="Fluoroquinolones", src=("L1", 79),
     why="Tendonitis and Achilles rupture, with caution under 18 years old. Peripheral neuropathy belongs to the same class.",
     wrong=[("Macrolides", "Known for QT prolongation and cholestatic hepatitis."),
            ("Tetracyclines", "Known for tooth discolouration and depressed skeletal growth."),
            ("Aminoglycosides", "Known for renal toxicity and ototoxicity.")]),

dict(q="Which antibiotic causes a disulfiram-like reaction if the patient drinks alcohol?",
     ans="Metronidazole", src=("L1", 86),
     why="A disulfiram-like reaction with ethanol — the patient must be told not to drink.",
     wrong=[("Clindamycin", "No alcohol interaction; its problem is Clostridium difficile."),
            ("Vancomycin", "Its infusion reaction is rate-related, not alcohol-related."),
            ("Linezolid", "Its food interaction is with tyramine, not ethanol.")]),

dict(q="Which antibiotic can cause serotonin syndrome with selective serotonin reuptake inhibitors?",
     ans="Linezolid", src=("L1", 71),
     why="Serotonin syndrome with SSRIs, and it also interacts with tyramine-containing foods and pseudoephedrine.",
     wrong=[("Vancomycin", "No serotonergic activity."),
            ("Metronidazole", "Its interaction is with ethanol."),
            ("Tigecycline", "Its problems are nausea, vomiting and diarrhoea.")]),

dict(q="Seizures are the warning attached to which antibiotic class, and to imipenem in particular?",
     ans="Carbapenems", src=("L1", 44),
     why="Seizures, specifically with imipenem.",
     wrong=[("Cephalosporins", "The class warning is allergic reaction, with under 1% penicillin cross-sensitivity."),
            ("Monobactams", "Aztreonam is notable for the opposite — no cross-reactivity and few warnings."),
            ("Penicillins", "The class warning is hypersensitivity, not seizures.")]),

dict(q="Which class discolours the teeth and depresses skeletal growth?",
     ans="Tetracyclines", src=("L1", 63),
     why="Tooth discolouration, doxycycline more than the others, and depression of skeletal growth.",
     wrong=[("Macrolides", "Cause gastrointestinal upset and cholestatic hepatitis."),
            ("Fluoroquinolones", "Affect tendons and peripheral nerves, not teeth."),
            ("Aminoglycosides", "Affect the kidney and the ear.")]),

dict(q="Which antibiotic is the one classically named for Clostridium difficile and pseudomembranous colitis?",
     ans="Clindamycin", src=("L1", 80),
     why="Clostridium difficile and pseudomembranous colitis, plus rash, neutropenia and thrombocytopenia.",
     wrong=[("Aztreonam", "Its listed side effect is diarrhoea, without this association."),
            ("Linezolid", "Named for serotonin syndrome."),
            ("Vancomycin", "Named for its infusion reaction — and oral vancomycin treats C. difficile.")]),

dict(q="Which class prolongs the QT interval and risks Torsades de pointes, worse with class Ia and III antiarrhythmics?",
     ans="Macrolides", src=("L1", 57),
     why="QT prolongation and Torsades de pointes, and the combination with class Ia and III antiarrhythmics makes it worse.",
     wrong=[("Penicillins", "No QT effect; the class problem is hypersensitivity."),
            ("Aminoglycosides", "Renal toxicity and ototoxicity."),
            ("Carbapenems", "Seizures, particularly imipenem.")]),

dict(q="Renal toxicity and ototoxicity together point to which class?",
     ans="Aminoglycosides", src=("L1", 68),
     why="Both at once — the kidney and the eighth nerve.",
     wrong=[("Macrolides", "Can cause transient hearing loss but not nephrotoxicity."),
            ("Cephalosporins", "Mostly renally eliminated, but not characteristically toxic to the kidney or ear."),
            ("Clindamycin", "Its problem is the colon.")]),

dict(q="Stevens-Johnson syndrome with thrombocytopenia and agranulocytosis is the warning on which agent?",
     ans="Trimethoprim / sulfamethoxazole", src=("L1", 85),
     why="Hypersensitivity through to Stevens-Johnson syndrome and toxic epidermal necrolysis, plus blood dyscrasias.",
     wrong=[("Amoxicillin / clavulanate", "Causes rash and diarrhoea, but not this hypersensitivity spectrum."),
            ("Piperacillin / tazobactam", "Hypersensitivity is possible, but the blood dyscrasias belong elsewhere."),
            ("Nitrofurantoin", "Not the agent this warning is attached to.")]),

dict(q="Which class carries black box warnings for nephrotoxicity, neurotoxicity and neuromuscular blockade?",
     ans="Polymyxins", src=("L1", 88),
     why="Polymyxin B and E (colistin) — all three warnings, and use is rising because of multidrug resistance.",
     wrong=[("Aminoglycosides", "Nephrotoxic and ototoxic, but without this black box set."),
            ("Vancomycin", "Ototoxic and nephrotoxic, but not a neuromuscular blocker."),
            ("Tigecycline", "Chiefly gastrointestinal.")]),

dict(q="Which antibiotic can be given to a genuinely penicillin-allergic patient because it has no cross-reactivity with beta-lactams?",
     ans="Aztreonam", src=("L1", 40),
     why="No cross-reactivity with the beta-lactams, so it is usable in true penicillin allergy. Gram-negative cover only.",
     wrong=[("Cefazolin", "A cephalosporin — cross-sensitivity is low but not zero."),
            ("Meropenem", "A carbapenem, and still a beta-lactam."),
            ("Ampicillin", "A penicillin, so exactly what must be avoided.")]),

dict(q="Which penicillin group was designed solely to cover methicillin-sensitive Staphylococcus aureus?",
     ans="Nafcillin", src=("L1", 26),
     why="Designed solely for MSSA — and monitored for hepatic rather than renal toxicity, the exception among the beta-lactams.",
     wrong=[("Trimethoprim / sulfamethoxazole", "Covers MRSA and Pneumocystis, but it is not a penicillin."),
            ("Ampicillin", "Aminopenicillins, extended to gram-negatives."),
            ("Piperacillin/tazobactam", "Antipseudomonal, for polymicrobial and nosocomial infection.")]),

dict(q="Which is the drug of choice for syphilis, gas gangrene and meningococcus?",
     ans="Penicillin G", src=("L1", 17),
     why="Drug of choice for all three. Good against gram-positives, with no staphylococcal cover.",
     wrong=[("Doxycycline", "An alternative in penicillin allergy, but not the drug of choice."),
            ("Azithromycin", "A macrolide, used for atypicals."),
            ("Ceftriaxone", "The drug of choice for gonorrhoea, not syphilis.")]),

dict(q="Which is the drug of choice for neutropenic fever?",
     ans="Cefepime", src=("L1", 36),
     why="The fourth-generation cephalosporin, drug of choice for neutropenic fever.",
     wrong=[("Cefazolin", "First generation — surgical prophylaxis, MSSA and urinary tract infection."),
            ("Ceftriaxone", "Third generation, with good streptococcal cover."),
            ("Cephalexin", "First generation, oral, for skin and urinary infection.")]),

dict(q="Which cephalosporin cannot be used during the first thirty days of life?",
     ans="Ceftriaxone", src=("L1", 34),
     why="Not in the first 30 days of life; cefotaxime is preferred for neonatal fever or sepsis.",
     wrong=[("Cefotaxime", "The one that IS preferred in the neonate."),
            ("Cefazolin", "Not the agent carrying this restriction."),
            ("Cefepime", "Reserved for neutropenic fever.")]),

dict(q="Penicillin cross-sensitivity of roughly less than one per cent belongs to which class?",
     ans="Cephalosporins", src=("L1", 30),
     why="Cross-sensitivity of approximately less than 1%, and mostly renally eliminated.",
     wrong=[("Carbapenems", "Beta-lactams too, but the figure quoted is for the cephalosporins."),
            ("Monobactams", "Aztreonam has NO cross-reactivity at all."),
            ("Macrolides", "Not beta-lactams, so the question does not arise.")]),

dict(q="Which agent significantly raises the international normalised ratio in a patient on warfarin, and causes hypoglycaemia with sulfonylureas?",
     ans="Trimethoprim / sulfamethoxazole", src=("L1", 85),
     why="Both interactions belong to it, which is why the warfarin patient needs closer monitoring.",
     wrong=[("Amoxicillin / clavulanate", "No clinically important warfarin or sulfonylurea interaction."),
            ("Piperacillin / tazobactam", "No clinically important warfarin or sulfonylurea interaction."),
            ("Clindamycin", "No such interaction.")]),

dict(q="Which class must be avoided in the second and third trimesters of pregnancy?",
     ans="Tetracyclines", src=("L1", 63),
     why="Avoided in the second and third trimesters, and in children, because of tooth discolouration and skeletal effects.",
     wrong=[("Penicillins", "Generally regarded as safe in pregnancy."),
            ("Cephalosporins", "Generally regarded as safe in pregnancy."),
            ("Macrolides", "Not the class carrying this restriction.")]),

dict(q="Transient hearing loss and cholestatic hepatitis belong to which class?",
     ans="Macrolides", src=("L1", 57),
     why="Both, alongside the gastrointestinal upset that is worst with erythromycin.",
     wrong=[("Aminoglycosides", "Cause permanent ototoxicity, not transient hearing loss with hepatitis."),
            ("Tetracyclines", "Affect teeth and bone."),
            ("Fluoroquinolones", "Affect tendons and nerves.")]),

dict(q="Which agent does NOT cover vancomycin-resistant Enterococcus?",
     ans="Tigecycline", src=("L1", 73),
     why="Covers complicated skin and intra-abdominal infection but NOT VRE — the exception worth remembering.",
     wrong=[("Linezolid", "Does cover VRE."),
            ("Vancomycin", "By definition VRE is resistant to it, but the question is about the agent listed as not covering it."),
            ("Clindamycin", "Not the agent this point is made about.")]),

dict(q="Which is the drug of choice for polymicrobial and nosocomial infections, especially pneumonia and intra-abdominal sepsis?",
     ans="Piperacillin/tazobactam", src=("L1", 27),
     why="Drug of choice for polymicrobial and nosocomial infection, including hospital pneumonia.",
     wrong=[("Amoxicillin/clavulanate", "The choice for bites and diabetic foot, not for nosocomial pneumonia."),
            ("Cefazolin", "Surgical prophylaxis and MSSA."),
            ("Aztreonam", "Gram-negatives only.")]),

dict(q="Which is the drug of choice for skin and soft tissue infection, diabetic foot, and animal or human bites?",
     ans="Amoxicillin/clavulanate", src=("L1", 25),
     why="Drug of choice for exactly those, because the clavulanate covers the mouth flora in a bite.",
     wrong=[("Piperacillin/tazobactam", "The choice for nosocomial and polymicrobial infection, not an outpatient bite."),
            ("Ceftriaxone", "Good streptococcal cover but not the choice for a bite."),
            ("Metronidazole", "Anaerobes only.")]),

dict(q="Which class is the drug of choice for multidrug-resistant gram-negative and extended-spectrum beta-lactamase infections?",
     ans="Carbapenems", src=("L1", 43),
     why="Drug of choice for MDR gram-negatives and ESBL producers.",
     wrong=[("Aminopenicillins", "Hydrolysed by those beta-lactamases."),
            ("First-generation cephalosporins", "Far too narrow."),
            ("Macrolides", "Wrong spectrum entirely.")]),

dict(q="Which antibiotic covers gram-negative organisms only?",
     ans="Aztreonam", src=("L1", 40),
     why="Gram-negative only — and no cross-reactivity with the other beta-lactams.",
     wrong=[("Vancomycin", "Gram-positive only, the mirror image."),
            ("Ceftaroline", "The cephalosporin with MRSA cover, so gram-positive included."),
            ("Piperacillin/tazobactam", "Broad, covering both.")]),

dict(q="Which fluoroquinolone must not be used for a urinary tract infection and has no Pseudomonas cover?",
     ans="Moxifloxacin", src=("L1", 78),
     why="Not for urinary tract infection, and no Pseudomonas cover — levofloxacin is the one with it.",
     wrong=[("Levofloxacin", "The one that DOES have Pseudomonas cover."),
            ("Ciprofloxacin", "Used for urinary infection."),
            ("Ofloxacin", "Not the agent this restriction is attached to.")]),

dict(q="Which class is the drug of choice for febrile neutropenia, sepsis and enterococcal synergy?",
     ans="Aminoglycosides", src=("L1", 68),
     why="Drug of choice for all three, which is why the renal and ear monitoring matters.",
     wrong=[("Macrolides", "Used for atypical respiratory infection."),
            ("Tetracyclines", "Used for atypicals and acne."),
            ("Clindamycin", "Used for anaerobes and gram-positives.")]),

dict(q="Which class causes photosensitivity and complexes with cations such as antacids and dairy?",
     ans="Fluoroquinolones", src=("L1", 79),
     why="Photosensitivity, and they chelate with cations — so they must be separated from antacids, iron and dairy.",
     wrong=[("Macrolides", "No cation chelation."),
            ("Penicillins", "No cation chelation."),
            ("Clindamycin", "Not affected this way.")]),

dict(q="Which is the drug of choice for Pneumocystis jirovecii pneumonia, both to treat and to prevent it?",
     ans="Trimethoprim / sulfamethoxazole", src=("L1", 85),
     why="Treatment AND prophylaxis, which is why it is used long term in immunosuppressed patients.",
     wrong=[("Clindamycin with primaquine", "A second-line alternative, not the drug of choice."),
            ("Azithromycin", "Used for atypical bacterial pneumonia."),
            ("Fluconazole", "An antifungal, and Pneumocystis does not respond to it.")]),

dict(q="Which cephalosporin generation carries MRSA cover?",
     ans="Ceftaroline", src=("L1", 37),
     why="The fifth generation, used for skin and soft tissue infection WITH MRSA cover — the only cephalosporin that has it.",
     wrong=[("Cefazolin", "MSSA only."),
            ("Ceftriaxone", "Good streptococcal cover, no MRSA."),
            ("Cefepime", "Antipseudomonal, for neutropenic fever.")]),
]
