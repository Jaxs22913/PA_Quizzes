# -*- coding: utf-8 -*-
"""Shortened replacements for the long Pharmacology I answer options.

Jaxon, 2026-08-30: "shorten the questions and make them more to the point".
The bank's median option ran 48 characters and a quarter passed 66, because the
reasoning had been written INTO the choice. The explanation already carries the
reasoning, so the choice only has to be identifiable.

Every replacement keeps the option's meaning and its truth value -- a distractor
stays wrong for the same reason it was wrong before. Paired options that a
question turns on (the two folate-pathway orderings, the two killing kinetics)
stay distinguishable from each other after shortening, which is asserted.
"""
SHORTEN = {
 # --- kinetics ---
 "In concentration-dependent killing, higher drug concentration produces greater killing and there is a post-antibiotic effect; in time-dependent killing the extent of killing plateaus and the time above the minimal inhibitory concentration governs the result":
   "More drug kills more, against time above the level",
 "In concentration-dependent killing the drug must be given by continuous infusion to hold a steady level; in time-dependent killing a single large daily dose is preferred because the post-antibiotic effect carries the interval":
   "Continuous infusion, against one large daily dose",
 "In concentration-dependent killing, activity depends on renal clearance; in time-dependent killing it depends on hepatic metabolism":
   "Renal clearance, against hepatic metabolism",
 "In concentration-dependent killing, the drug is bacteriostatic; in time-dependent killing the drug is bactericidal":
   "Static, against cidal",
 "They show a post-antibiotic effect, so killing persists after the level falls, and concentration-dependent killing favours a large single dose":
   "Post-antibiotic effect and concentration-dependent killing",
 "They show time-dependent killing, so a longer interval keeps the level above the minimal inhibitory concentration for a greater share of the dosing period":
   "Time-dependent killing over a longer interval",
 "Continuous or frequent infusions, keeping the concentration above the minimal inhibitory concentration for 40 to 70 percent of the dosing interval":
   "Frequent infusions, level up 40 to 70% of the interval",
 "A loading dose followed by widely spaced maintenance doses, with the interval guided by trough levels alone rather than by time above the minimal inhibitory concentration":
   "A loading dose, then widely spaced doses by trough alone",
 # --- macrolide CYP ---
 "Metabolites bind CYP3A subclass enzymes forming an inactive complex, raising levels of substrates such as carbamazepine, cyclosporine, digoxin, midazolam and theophylline, with erythromycin greater than clarithromycin greater than azithromycin":
   "Metabolites inactivate CYP3A, raising substrate levels",
 "They induce CYP3A subclass enzymes, lowering levels of substrates such as carbamazepine, cyclosporine, digoxin, midazolam and theophylline, with azithromycin greater than clarithromycin greater than erythromycin":
   "They induce CYP3A, lowering substrate levels",
 # --- folate pathway (three orderings, kept distinguishable) ---
 "Sulfamethoxazole inhibits conversion of para-aminobenzoic acid to dihydrofolic acid via tetrahydropteroic acid synthetase; trimethoprim inhibits conversion of dihydrofolic acid to tetrahydrofolic acid via dihydrofolate reductase":
   "Sulfa at the PABA step, trimethoprim at the reductase",
 "Sulfamethoxazole inhibits the conversion of dihydrofolic acid to tetrahydrofolic acid via dihydrofolate reductase; trimethoprim inhibits the conversion of para-aminobenzoic acid to dihydrofolic acid via tetrahydropteroic acid synthetase":
   "Sulfa at the reductase, trimethoprim at the PABA step",
 "Sulfamethoxazole inhibits dihydrofolate reductase and blocks conversion of dihydrofolic acid to tetrahydrofolic acid; trimethoprim inhibits tetrahydropteroic acid synthetase upstream of it":
   "Sulfa at the reductase, trimethoprim upstream of it",
 # --- indications ---
 "Bacterial meningitis, cerebral abscess and ventriculitis requiring reliable central nervous system penetration, together with neurosurgical prophylaxis after craniotomy":
   "Meningitis, cerebral abscess and neurosurgical prophylaxis",
 "Toxin-mediated disease, skin and soft tissue infection, osteomyelitis, surgical prophylaxis in penicillin allergy, and as part of intra-abdominal combination therapy":
   "Toxin-mediated disease, skin, bone, penicillin allergy",
 "Oesophageal candidiasis, systemic aspergillosis not responding to itraconazole or amphotericin B, and febrile neutropenic patients not responding to antibiotics":
   "Oesophageal candidiasis and refractory aspergillosis",
 "Cryptococcal meningitis, oral and vaginal candidiasis, and prophylaxis in advanced human immunodeficiency virus infection, together with urinary candidiasis":
   "Cryptococcal meningitis and oral or vaginal candidiasis",
 "Community-acquired pneumonia and skin and soft tissue infection in the outpatient setting, together with uncomplicated urinary tract infection":
   "Community-acquired pneumonia and skin infection",
 "Methicillin-resistant Staphylococcus aureus bacteraemia, infective endocarditis, vertebral osteomyelitis, and prosthetic joint infection":
   "MRSA bacteraemia, endocarditis and osteomyelitis",
 "Multidrug-resistant Gram-negative infections, extended-spectrum beta-lactamase producing bacteria, nosocomial infections, and meningitis":
   "Resistant Gram-negatives, ESBL producers, meningitis",
 "Neutropenic fever, nosocomial infections including hospital-acquired and ventilator-associated pneumonia, and pseudomonal infections":
   "Neutropenic fever, nosocomial pneumonia and Pseudomonas",
 "Enterococcus, Listeria, endocarditis prophylaxis, upper respiratory tract infection, and community-acquired pneumonia at high dose":
   "Enterococcus, Listeria, endocarditis prophylaxis and pneumonia",
 "Pseudomonas aeruginosa pneumonia, nosocomial intra-abdominal infection, and polymicrobial infection in the critically ill patient":
   "Pseudomonal, nosocomial and polymicrobial infection",
 "Hospital-acquired and community-acquired methicillin-resistant Staphylococcus aureus; it covers no Gram-negatives or anaerobes":
   "Hospital and community MRSA, with no Gram-negative cover",
 "Cryptococcus, Blastomyces, Histoplasma, Candida, Coccidioides and Aspergillus, the last reserved for invasive infection":
   "The systemic mycoses; Aspergillus if invasive",
 "Dermatophyte infections of the skin, hair and nails only, with no activity against any of the systemic fungal organisms":
   "Dermatophytes of skin, hair and nails only",
 "Blastomycosis, histoplasmosis, onychomycosis, and febrile neutropenic patients not responding to antibiotics":
   "Blastomycosis, histoplasmosis and onychomycosis",
 "Surgical prophylaxis, methicillin-susceptible Staphylococcus aureus infection, and urinary tract infection":
   "Surgical prophylaxis, MSSA and urinary tract infection",
 "Complicated intra-abdominal infection with Bacteroides fragilis, anaerobic abscess and biliary sepsis":
   "Complicated intra-abdominal and anaerobic infection",
 "Cryptococcal meningitis and prophylaxis against relapse in advanced acquired immunodeficiency syndrome":
   "Cryptococcal meningitis and relapse prophylaxis",
 "Pseudomonal and multidrug-resistant Gram-negative infection; it covers no Gram-positive organisms and no atypicals":
   "Pseudomonal and resistant Gram-negative infection only",
 "Atypicals and animal-borne organisms — Yersinia pestis, Brucella, Borrelia burgdorferi and rickettsiae":
   "Atypicals and animal-borne organisms",
 # --- coverage / spectrum ---
 "Excellent Gram-negative activity including Pseudomonas aeruginosa, with limited Gram-positive coverage and reliable activity against Enterococcus":
   "Gram-negatives including Pseudomonas, plus Enterococcus",
 "Excellent Gram-positive activity with no Enterococcus coverage, and some Gram-negative coverage of Escherichia coli, Proteus and Klebsiella":
   "Gram-positives without Enterococcus, some Gram-negative cover",
 # --- mechanisms ---
 "Inhibition of bacterial DNA gyrase, also called topoisomerase II, forming a quinolone-DNA-gyrase complex with induced DNA cleavage, plus inhibition of topoisomerase IV":
   "Inhibits DNA gyrase and topoisomerase IV",
 "Binding the 30S ribosomal subunit and preventing transfer RNA from occupying the A site of the bacterial ribosome during chain elongation and protein assembly":
   "Binds 30S and blocks transfer RNA at the A site",
 "A detergent-like interaction with the lipopolysaccharide of the Gram-negative outer membrane, displacing magnesium and calcium and disrupting the membrane":
   "A detergent action on the Gram-negative outer membrane",
 "It forms channels in ergosterol-containing membranes that let potassium and magnesium leak out, and causes oxidative damage to the membrane":
   "Forms pores in ergosterol membranes, leaking ions",
 "It is converted to a fluorinated nucleotide by a fungal enzyme and then blocks thymidylate synthase, halting deoxyribonucleic acid synthesis":
   "A fungal enzyme converts it, then it blocks thymidylate synthase",
 "It is converted to 5-fluorouridine by cytosine deaminase, an enzyme human cells lack, and then inhibits thymidylate synthase":
   "Cytosine deaminase converts it; human cells lack that enzyme",
 "It inhibits squalene epoxidase in the parasite, progressively depleting the membrane of ergosterol until it loses integrity":
   "Inhibits squalene epoxidase, depleting ergosterol",
 "It binds the two D-alanine residues on the peptide to block cross-linking, rather than inactivating the cross-linking enzyme":
   "Binds the D-alanine residues to block cross-linking",
 "It inactivates the penicillin-binding protein by forming a covalent bond at its active site, exactly as a penicillin does":
   "Covalently inactivates the penicillin-binding protein",
 "It is selectively phosphorylated by viral thymidine kinase, so it is only activated where the virus is replicating":
   "Viral thymidine kinase activates it only in infected cells",
 "It inhibits influenza virus neuraminidase, preventing budding progeny from being cleaved free of the host cell":
   "Inhibits neuraminidase so progeny cannot be released",
 "It inhibits a viral protease, preventing cleavage of polypeptide precursors into mature viral proteins":
   "Inhibits a viral protease",
 "It stimulates peripheral mononuclear cells to release interferon alpha and macrophages to produce tumour necrosis factor alpha and interleukins":
   "Drives interferon alpha and tumour necrosis factor release",
 "It causes bacterial depolarization inhibiting DNA, RNA and protein synthesis, and it cannot be used in pneumonia":
   "Depolarizes the membrane; cannot be used in pneumonia",
 "It releases acetylcholine and inhibits cholinesterase, acting as a depolarizing neuromuscular blocker that causes paralysis and death":
   "Releases acetylcholine and blocks cholinesterase",
 "They release acetylcholine and inhibit cholinesterase, acting as a depolarizing neuromuscular blocker":
   "Release acetylcholine and block cholinesterase",
 "It corrects abnormal follicular keratinization, reduces bacterial counts within the follicle, and dampens the inflammatory response":
   "Corrects keratinization, cuts bacteria and inflammation",
 "Corrects abnormal follicular keratinization, reduces Propionibacterium acnes counts, and reduces inflammation":
   "Corrects keratinization and reduces P. acnes and inflammation",
 "Conversion to benzoic acid within the stratum corneum together with a direct comedolytic peeling effect":
   "Converts to benzoic acid, with a comedolytic peeling effect",
 "Converts to benzoic acid after penetration, bleaches surface pigment, and suppresses sebum production":
   "Converts to benzoic acid, bleaches pigment, cuts sebum",
 "It is actively pumped into fungal cells by a membrane transporter that is entirely absent from human cells and tissues":
   "A fungal transporter pumps it in; human cells lack it",
 "Their target is a fungal cytochrome P450 enzyme, and they inhibit human cytochrome P450 enzymes such as 3A4 as well":
   "They hit a fungal CYP450 and inhibit human CYP3A4 too",
 "Inhibition of cytochrome P450 3A4, producing raised plasma levels of co-administered substrate drugs and a risk of toxicity":
   "CYP3A4 inhibition, raising substrate levels",
 "They induce cytochrome P450 1A2 and 2C9, accelerating the clearance of co-administered drugs and lowering their levels":
   "They induce CYP1A2 and 2C9, lowering drug levels",
 "It does not enter the central nervous system and it inhibits cytochrome P450 3A4, producing significant drug interactions":
   "No CNS entry, and it inhibits CYP3A4",
 "Nystatin and tolnaftate, which bind fungal membrane sterols directly and cause leakage of cell contents":
   "Nystatin and tolnaftate, binding membrane sterols",
 # --- adverse effects ---
 "Hypokalaemia and hypomagnesaemia, hypotension, uraemia in about 80 percent with decreased filtration, and renal tubule damage mitigated by hydration with normal saline":
   "Low potassium and magnesium, hypotension, renal tubule damage",
 "Hyperkalaemia and hypercalcaemia with a rising glomerular filtration rate, hypertension, and tubular hypertrophy that resolves without any need for hydration":
   "High potassium and calcium with a rising filtration rate",
 "They are driven by interleukin-1 and tumour necrosis factor, and patients are pretreated with acetaminophen, antihistamines and corticosteroids":
   "Interleukin-1 and tumour necrosis factor; pre-medicate",
 "They are caused by rapid fungal lysis releasing endotoxin into the circulation, and are prevented by slowing the rate of the infusion alone":
   "Fungal lysis releasing endotoxin, fixed by slowing the rate",
 "They reflect an immunoglobulin E mediated allergic reaction, and the drug must be stopped permanently":
   "An IgE allergic reaction; stop the drug permanently",
 "Headache in about 15 percent, mental confusion, fatigue and blurred vision, with induction of cytochrome P450 1A2 and 2C9":
   "Headache, confusion, fatigue and blurred vision",
 "Marked neutropenia and thrombocytopenia, with about a third of patients stopping intravenous treatment":
   "Neutropenia and thrombocytopenia; a third stop treatment",
 "Adrenal suppression, infections, hyperglycaemia, glaucoma, cataracts and growth retardation in children":
   "Adrenal suppression, hyperglycaemia, glaucoma, cataracts",
 "Photosensitivity, severe sunburn, desquamation, burning and stinging that decrease with continued use":
   "Photosensitivity, sunburn, desquamation and stinging",
 "Nikolsky sign, mucosal erosion at two or more sites, and fever preceding the rash by one to three days":
   "Nikolsky sign, mucosal erosion and a preceding fever",
 "Discoloration of teeth and depression of skeletal growth — avoid under 8 years old and in the second and third trimesters":
   "Teeth discoloration and skeletal effects; avoid under 8",
 "Kernicterus from bilirubin displacement — avoid in the first 30 days of life and throughout the third trimester of pregnancy":
   "Kernicterus; avoid in the first 30 days of life",
 "Avoid using it on open wounds or denuded skin in high doses, because of neurotoxicity and nephrotoxicity risk":
   "Not on open wounds in high doses; neuro and nephrotoxicity",
 "It is available only intravenously and causes severe infusion reactions requiring routine premedication before every dose":
   "Intravenous only, with severe infusion reactions",
 "It is contraindicated in pregnancy and breastfeeding, and the lecture adds that men should avoid it as well":
   "Contraindicated in pregnancy and breastfeeding; men too",
 "Avoid it in pregnancy and in breastfeeding, because systemic absorption through inflamed skin is teratogenic":
   "Avoid in pregnancy; absorption through inflamed skin",
 "It is safe in the second and third trimesters, and only the first trimester requires contraceptive cover":
   "Safe after the first trimester",
 # --- microbiology / cell biology ---
 "They are prokaryotic, with a peptidoglycan cell wall and a 70S ribosome that antibacterial agents cannot reach, and a nuclear region without a surrounding membrane":
   "Prokaryotic: peptidoglycan wall, 70S ribosome",
 "They are eukaryotic, with a rigid cell wall containing chitin, a cell membrane built on ergosterol, different ribosomes and a distinct nuclear membrane":
   "Eukaryotic: chitin wall, ergosterol membrane, nuclear membrane",
 "It contains chitin and glucans rather than peptidoglycan, so agents such as the echinocandins are needed":
   "Chitin and glucans rather than peptidoglycan",
 "They lack a cell wall entirely and rely on a cholesterol membrane, so cell wall agents have no target":
   "No cell wall at all, so wall agents have no target",
 "At high levels the drug may interact with mammalian 80S ribosomes rather than only the bacterial 70S ribosome":
   "At high levels it can reach the mammalian 80S ribosome",
 "Mammalian mitochondria use a 90S ribosome that binds these drugs preferentially at therapeutic levels":
   "Mitochondria use a 90S ribosome that binds these drugs",
 "Bacteriostatic inhibits a vital growth pathway without directly causing death; bactericidal disrupts function enough that death occurs":
   "Static halts growth; cidal disrupts enough to kill",
 "Bacteriostatic works only on Gram-positive organisms; bactericidal works on both Gram-positive and Gram-negative organisms":
   "Static is Gram-positive only; cidal covers both",
 "Bacteriostatic requires a higher concentration to act; bactericidal acts at any concentration above zero":
   "Static needs a higher concentration than cidal",
 "The mechanism is impossible for bacteria to circumvent, and newer formulations have removed the nephrotoxicity and neurotoxicity entirely":
   "Bacteria cannot circumvent it and the toxicity is gone",
 "The class went largely unused for the last 50 years, and rising multidrug resistance is bringing it back despite optimal regimens not being well studied":
   "Unused for 50 years; resistance is bringing it back",
 "Into the afferent system, carrying signals to the centre, and the enteric system, acting independently":
   "Into the afferent and enteric systems",
 # --- duration / practical ---
 "About one month for the scalp, six to nine months for fingernails, and up to twelve months for toenails":
   "Scalp a month, fingernails 6 to 9, toenails up to 12",
 "Approximately one week for the scalp, one month for the fingernails, and three months for the toenails":
   "Scalp a week, fingernails a month, toenails three",
 "The drug is stored in subcutaneous fat and released during exercise, which is why activity increases absorption":
   "Stored in fat and released on exercise",
 "Wash with a high pH soap several times daily, since a raised pH increases the activity of other topical agents":
   "Wash often with a high pH soap",
 "Frequent hot baths with a high pH soap, air drying afterwards, and occlusive dressings left on overnight":
   "Hot baths, high pH soap, air drying, occlusive dressings",
 "It requires an immediate switch to systemic therapy, because irritation means the topical agent has failed":
   "Switch straight to systemic therapy",
 "Mupirocin is the preferred agent for acne; bacitracin is losing efficacy to Propionibacterium acnes resistance":
   "Mupirocin preferred; bacitracin losing efficacy",
 "Acyclovir's indications are herpes simplex and varicella-zoster; cytomegalovirus requires ganciclovir or valganciclovir":
   "Acyclovir for simplex and zoster; ganciclovir for CMV",
 "Acyclovir is available only intravenously and cannot safely be given to a transplant recipient on immunosuppression":
   "Acyclovir is intravenous only and unsafe in transplant",
 "Acyclovir targets viral neuraminidase directly; oseltamivir depends on thymidine kinase for activation":
   "Acyclovir hits neuraminidase; oseltamivir needs thymidine kinase",
 "50S — macrolides, clindamycin, chloramphenicol, streptogramins; 30S — aminoglycosides, tetracyclines":
   "50S: macrolides, clindamycin. 30S: aminoglycosides, tetracyclines",
 "50S — aminoglycosides, tetracyclines; 30S — macrolides, clindamycin, chloramphenicol, streptogramins":
   "50S: aminoglycosides, tetracyclines. 30S: macrolides, clindamycin",
 "Pseudomonas aeruginosa, Acinetobacter species, Burkholderia cepacia and Stenotrophomonas maltophilia":
   "Pseudomonas, Acinetobacter, Burkholderia, Stenotrophomonas",
 "Forming channels within the cell membrane that allow potassium and magnesium to leak out of the cell":
   "Channels that let potassium and magnesium leak out",
 "It is concentrated by a membrane transporter that is expressed only on the surface of infected cells":
   "A transporter on infected cells concentrates it",
 "Acyclovir depends on viral thymidine kinase to be activated; oseltamivir targets viral neuraminidase":
   "Acyclovir needs thymidine kinase; oseltamivir hits neuraminidase",
 "Bleaching of hair and clothing, together with staining of the surrounding skin at the injection site":
   "Bleaching of hair and clothing",
 "They are a disulfiram-like reaction to the infusion vehicle, and are avoided by withholding alcohol":
   "A disulfiram-like reaction to the vehicle",
 "They inhibit formation of helminth microtubules and block glucose uptake, leading to parasite death":
   "Block helminth microtubules and glucose uptake",
 "It contains peptidoglycan in a considerably thicker layer, so higher beta-lactam doses are required":
   "A much thicker peptidoglycan layer, needing higher doses",
 "Skin irritation occurs in virtually all patients, and the degree of inflammation parallels efficacy":
   "Irritation in nearly all; inflammation parallels efficacy",
 "It inhibits protein synthesis at the 50S ribosomal subunit, and it cannot be used in renal failure":
   "Inhibits the 50S subunit; unusable in renal failure",
 "Sulfamethoxazole blocks folate absorption from the gut; trimethoprim blocks its renal reabsorption":
   "Sulfa blocks gut folate; trimethoprim blocks reabsorption",
 "Inhibition of 1,3-beta-D-glucan synthase, lowering formation of 1,3-beta-D-glucan in the cell wall":
   "Inhibits 1,3-beta-D-glucan synthase in the cell wall",
 "A single myelinated neuron running from the central nervous system directly to the effector organ":
   "One myelinated neuron straight to the effector organ",
 "Acute disease as nodular and pustular lesions; chronic disease as open and closed comedones alone":
   "Acute as nodules and pustules; chronic as comedones",
 "A preganglionic neuron in the central nervous system and a postganglionic neuron from a ganglion":
   "A preganglionic neuron centrally, then a postganglionic one",
 "Binding 16S ribosomal RNA of the 30S subunit, preventing transfer RNA from binding in the A site":
   "Binds 16S RNA of the 30S subunit, blocking the A site",
 "Pruritus, rash in areas typical of the disease, chronic or repeated symptoms, and family history":
   "Pruritus, typical distribution, chronicity, family history",
 "Noninflammatory as open and closed comedones; inflammatory as papulopustular and nodular lesions":
   "Noninflammatory comedones; inflammatory papules and nodules",
 "It means the applied dose is too low and the frequency should be increased until the skin clears":
   "The dose is too low; increase the frequency",
 "Synthesis, release, reuptake into the presynaptic terminal, and repackaging without degradation":
   "Synthesis, release, reuptake, repackaging",
 "The broadest spectrum of any beta-lactam, covering Gram-positives, Gram-negatives and anaerobes":
   "The broadest beta-lactam spectrum, including anaerobes",
 "Pseudomonas aeruginosa, Clostridium difficile, Enterococcus faecium and Acinetobacter baumannii":
   "Pseudomonas, C. difficile, E. faecium, Acinetobacter",
 "Skin acts as a reservoir for the drug, which may permit once daily dosing of short acting drugs":
   "Skin acts as a reservoir, allowing once daily dosing",
 "Clindamycin is preferred; erythromycin is losing efficacy to Propionibacterium acnes resistance":
   "Clindamycin preferred; erythromycin losing efficacy",
 "No cross-reactivity with beta-lactams, so it can be used in truly penicillin-allergic patients":
   "No beta-lactam cross-reactivity; safe in true allergy",
 "Inhibition of lanosterol demethylase, progressively reducing ergosterol in the fungal membrane":
   "Inhibits lanosterol demethylase, cutting ergosterol",
 "Flucytosine, through conversion to a fluorinated nucleotide that inhibits thymidylate synthase":
   "Flucytosine, via a nucleotide blocking thymidylate synthase",
 "Terbinafine, by inhibiting squalene epoxidase early in the fungal ergosterol synthesis pathway":
   "Terbinafine, by inhibiting squalene epoxidase",
 "Valacyclovir with acyclovir, famciclovir with penciclovir, and valganciclovir with ganciclovir":
   "Valacyclovir-acyclovir, famciclovir-penciclovir, valganciclovir-ganciclovir",
 "Valacyclovir with ganciclovir, famciclovir with acyclovir, and valganciclovir with penciclovir":
   "Valacyclovir-ganciclovir, famciclovir-acyclovir, valganciclovir-penciclovir",
 "Actinic keratoses and superficial basal cell carcinoma; they are topical retinoid preparations":
   "Actinic keratoses and basal cell carcinoma; retinoids",
 "Antimicrobial activity and inhibition of the conversion of testosterone to dihydrotestosterone":
   "Antimicrobial, and blocks testosterone conversion",
 "Naftifine and terbinafine, which inhibit ergosterol production and prevent cell wall synthesis":
   "Naftifine and terbinafine, inhibiting ergosterol",
 "Legionella species, Mycoplasma pneumoniae, Chlamydophila pneumoniae and Chlamydia trachomatis":
   "Legionella, Mycoplasma, Chlamydophila, Chlamydia",
 "It is a peptide antibiotic that prevents cell wall synthesis, and it has no systemic toxicity":
   "A peptide antibiotic; no systemic toxicity",
 "Lukewarm baths with lubricant applied afterwards, short fingernails, and avoiding overheating":
   "Lukewarm baths, lubricant after, short nails, no overheating",
 "Methicillin-resistant Staphylococcus aureus, for which vancomycin is the treatment of choice":
   "MRSA, for which vancomycin is the treatment of choice",
 "It binds the 50S ribosomal subunit and blocks the transpeptidation step of protein synthesis":
   "Binds 50S and blocks transpeptidation",
 "With amphotericin B in cryptococcal meningitis, and with itraconazole in chromoblastomycosis":
   "With amphotericin in cryptococcal meningitis",
 "Crystallisation within the renal tubule, requiring aggressive hydration throughout treatment":
   "Crystals in the renal tubule; hydrate throughout",
 "Do not wash too frequently; twice a day, balancing cleanliness against drying and irritation":
   "Twice a day only, balancing cleanliness against drying",
 "It is effective against tinea pedis, tinea cruris and tinea corporis, but not tinea unguium":
   "Works on pedis, cruris and corporis, but not unguium",
 "Oseltamivir with acyclovir, valacyclovir with penciclovir, and famciclovir with ganciclovir":
   "Oseltamivir-acyclovir, valacyclovir-penciclovir, famciclovir-ganciclovir",
 "It can lead to patient discontinuation, so start with lower strength and increase gradually":
   "Patients stop; start low and increase gradually",
 "Aspergillus, Blastomyces, Candida, Coccidioides, Cryptococcus, Histoplasma and Zygomycetes":
   "Aspergillus, Candida, Cryptococcus, Histoplasma, Zygomycetes",
 "It binds bacterial transfer RNA to stop protein synthesis, and it accumulates systemically":
   "Binds transfer RNA; accumulates systemically",
}
