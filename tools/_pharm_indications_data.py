# -*- coding: utf-8 -*-
"""Indications and patient education for Pharmacology I Exam 1.

Same provenance contract as _pharm_contra_data.py: every row carries the deck
and slide it came from plus `verify` substrings that must appear on that slide,
so check_pharm_ref.py can prove the row before the page is written.

DOC = the deck literally says "drug of choice" for that indication. That phrase
is all over Lecture 1 and is the single most answerable thing in it, so it gets
its own tier rather than being flattened into "indication".
"""
L1 = "Antibiotics, Antivirals, and Antifungals"
L2 = "02. Dermatology Medications"
L3 = "03. ANS Pharmacology"

# (drug, indications, patient education / practical note, tier, deck, slide, verify)
ROWS = [
 # ---------------- BETA-LACTAMS ----------------
 ("Penicillin G<br><span class=g>natural penicillin</span>",
  "<b>DRUG OF CHOICE for syphilis, gas gangrene and meningococcus.</b> Good against gram-positive cocci; "
  "<b>no staph coverage</b>; anaerobic activity except Bacteroides; no aerobic gram-negative activity.",
  "Monitor for <b>signs and symptoms of anaphylaxis</b>.",
  "DOC", L1, 17, ["Drug of choice for syphilis", "gas gangrene", "meningococcus", "No Staph Coverage"]),
 ("Aminopenicillins<br><span class=g>ampicillin, amoxicillin</span>",
  "<b>DRUG OF CHOICE for Enterococcus, Listeria, endocarditis prophylaxis</b>, upper respiratory tract infection "
  "(sinusitis, otitis, bronchitis) and <b>community-acquired pneumonia (high-dose amoxicillin)</b>.",
  "<b>Reduces the effectiveness of oral contraceptives &mdash; use backup birth control.</b> Ampicillin is IV or "
  "oral; amoxicillin is oral only.",
  "DOC", L1, 19, ["Drug of choice for Enterococcus", "Listeria", "endocarditis prophylaxis", "CAP"]),
 ("Amoxicillin/clavulanate, ampicillin/sulbactam<br><span class=g>Augmentin, Unasyn</span>",
  "<b>DRUG OF CHOICE for skin and soft tissue infection, diabetic foot, and animal or human bites.</b> The "
  "beta-lactamase inhibitor adds anaerobe coverage (Bacteroides) and MSSA.",
  "The bite indication is the one to remember &mdash; it is why Augmentin is the reflex answer for a cat bite.",
  "DOC", L1, 25, ["Drug of choice for skin/soft tissue", "diabetic foot", "animal/human bites"]),
 ("Piperacillin/tazobactam<br><span class=g>Zosyn</span>",
  "<b>DRUG OF CHOICE for polymicrobial infections, nosocomial infections (especially pneumonia), "
  "intra-abdominal infections and pseudomonal infections.</b>",
  "Broad spectrum with <b>anti-pseudomonal activity</b>; keeps gram-positive cover for MSSA only.",
  "DOC", L1, 27, ["Drug of choice", "Polymicrobial", "Nosocomial infections", "Intra-abdominal",
                  "Pseudomonal"]),
 ("Cefazolin, cephalexin<br><span class=g>1st generation &mdash; Ancef, Keflex</span>",
  "Cefazolin for <b>surgical prophylaxis, MSSA and urinary tract infection</b>. Cephalexin for <b>skin and soft "
  "tissue infection (cellulitis) and urinary tract infection</b>.",
  "Great gram-positive activity but <b>no Enterococcus coverage</b>; some gram-negative cover.",
  "IND", L1, 32, ["Surgical prophylaxis", "Cellulitis", "No Enterococcus coverage"]),
 ("Ceftriaxone, cefotaxime<br><span class=g>3rd generation</span>",
  "Ceftriaxone has <b>good Strep coverage</b> and needs <b>no dose adjustment in renal insufficiency</b>. "
  "<b>Cefotaxime is preferred in neonatal fever or sepsis.</b>",
  "<b>Ceftriaxone cannot be used in the first 30 days of life</b> &mdash; reach for cefotaxime instead.",
  "IND", L1, 34, ["Good Strep coverage", "No dosage adjustment in renal insufficiency",
                  "Preferred in neonatal fever/sepsis"]),
 ("Nafcillin, oxacillin, dicloxacillin<br><span class=g>penicillinase-resistant</span>",
  "<b>Designed SOLELY to cover <i>S. aureus</i> (MSSA)</b>, with decreased activity against other organisms.",
  "<i>S. aureus</i> is increasingly resistant to this class (MRSA), and <b>vancomycin is the treatment of choice "
  "for MRSA</b>. Dosing considerations are <b>hepatic</b>, not renal.",
  "IND", L1, 26, ["Designed solely to cover S. aureus", "Vancomycin treatment of choice for MRSA",
                  "Hepatic Function"]),
 ("Ceftolozane/tazobactam<br><span class=g>Zerbaxa</span>",
  "FDA approved for <b>complicated intra-abdominal infections (plus metronidazole)</b> and <b>complicated "
  "urinary tract infections</b>.",
  "Anti-pseudomonal with some anaerobic activity, but <b>no MRSA and no Enterococcus</b>. The "
  "&ldquo;plus metronidazole&rdquo; pairing is the detail to carry.",
  "IND", L1, 38, ["Complicated Intra-abdominal infections", "plus metronidazole",
                  "Complicated urinary tract infections"]),
 ("Cefepime<br><span class=g>4th generation &mdash; Maxipime</span>",
  "<b>DRUG OF CHOICE for neutropenic fever</b>, nosocomial infections (hospital- and ventilator-acquired "
  "pneumonia) and pseudomonal infections.",
  "Broad spectrum with anti-pseudomonal activity, but <b>no MRSA, no Enterococcus and no anaerobes</b>.",
  "DOC", L1, 36, ["Drug of Choice", "Neutropenic fever", "Nosocomial infections", "Pseudomonal"]),
 ("Ceftaroline<br><span class=g>5th generation &mdash; Teflaro</span>",
  "FDA approved for <b>community-acquired pneumonia</b> and <b>skin and soft tissue infections</b>. Notable as "
  "the cephalosporin <b>with MRSA coverage</b>.",
  "<b>Must be renally adjusted.</b>",
  "IND", L1, 37, ["MRSA coverage", "Community acquired pneumonia", "Skin/soft tissue",
                  "Must be renally adjusted"]),
 ("Aztreonam<br><span class=g>monobactam</span>",
  "<b>Gram-negative only</b> &mdash; the spectrum resembles the aminoglycosides, with activity against "
  "<i>Pseudomonas aeruginosa</i> and Enterobacteriaceae. No gram-positive or anaerobic activity.",
  "The reason it exists on the exam: <b>no cross-reactivity with beta-lactams, so it can be used in a truly "
  "penicillin-allergic patient</b>.",
  "IND", L1, 40, ["Only Gram - coverage", "resembles aminoglycosides", "P. aeruginosa"]),
 ("Carbapenems<br><span class=g>imipenem, meropenem, ertapenem</span>",
  "<b>DRUG OF CHOICE for multidrug-resistant gram-negative infections, extended-spectrum beta-lactamase "
  "producers, nosocomial infections, and meningitis</b> (they penetrate the central nervous system).",
  "Very broad, but <b>no MRSA</b>, and <b>ertapenem is the one without Pseudomonas coverage</b>.",
  "DOC", L1, 43, ["Drug of choice", "MDR Gram-negative", "ESBL", "Meningitis", "except ertapenem"]),

 # ---------------- VANCOMYCIN ----------------
 ("Vancomycin",
  "<b>DRUG OF CHOICE for penicillin-allergy infections, MRSA, <i>C. difficile</i> (oral), endocarditis, "
  "osteomyelitis, and surgical prophylaxis in allergy.</b> <b>Gram-positive coverage ONLY.</b>",
  "<b>Oral for <i>C. difficile</i>, intravenous for everything else</b> &mdash; the route changes with the "
  "indication, which is a favourite question.",
  "DOC", L1, 47, ["Drug of Choice", "Pen-allergy", "MRSA", "C. Diff (PO)", "Endocarditis", "Osteomyelitis"]),
 ("Vancomycin",
  "Target trough <b>10&ndash;15 or 15&ndash;20 mcg/mL depending on the indication</b>. A loading dose of "
  "25&ndash;30 mg/kg may be used to reach target quickly.",
  "If the <b>MIC is 2 mg/L or above</b>, the target is hard to achieve and <b>alternative therapy such as "
  "linezolid may be needed</b>.",
  "MON", L1, 48, ["Goal trough", "Depends on indication", "loading dose", "alternative therapy", "linezolid"]),

 # ---------------- PROTEIN SYNTHESIS ----------------
 ("Macrolides<br><span class=g>erythromycin, clarithromycin, azithromycin</span>",
  "<b>Respiratory tract infections</b> (community-acquired pneumonia, acute otitis media, pharyngitis, "
  "sinusitis, chronic bronchitis), skin infections, <b><i>Mycobacterium avium</i> complex</b> prophylaxis and "
  "treatment, <b><i>Chlamydia trachomatis</i></b>, and <b><i>H. pylori</i></b>.",
  "<i>H. pylori</i> regimen is <b>Prevpac &mdash; clarithromycin + amoxicillin + lansoprazole</b>. Erythromycin "
  "is the one used for <b>conjunctivitis or pneumonia in an infant</b>.",
  "IND", L1, 56, ["Respiratory Tract Infections", "Mycobacterium avium", "Chlamydia trachomatis",
                  "H. pylori", "Prevpac"]),
 ("Tetracyclines<br><span class=g>doxycycline, minocycline</span>",
  "<b>Acne, atypical pneumonia, animal-borne disease, Rocky Mountain spotted fever, Lyme disease</b> and "
  "sexually transmitted disease &mdash; <b>doxycycline for chlamydia</b>.",
  "<b>They chelate with cations</b> &mdash; counsel the patient to separate doses from <b>iron, calcium and "
  "dairy</b>. Warn about <b>photosensitivity</b>.",
  "IND", L1, 63, ["Acne", "Rocky mountain spotted fever", "Lyme Disease", "Chlamydia (doxy)",
                  "Chelate with cations"]),
 ("Tigecycline<br><span class=g>Tygacil</span>",
  "<b>Complicated skin infections</b> and <b>complicated intra-abdominal infections</b>. Covers MRSA and "
  "<i>E. faecalis</i>, but <b>NOT VRE</b>.",
  "Bacteriostatic. The &ldquo;not VRE&rdquo; exclusion is stated twice on the slide.",
  "IND", L1, 65, ["Complicated skin infections", "Complicated intra-abdominal", "not VRE", "MRSA"]),
 ("Aminoglycosides<br><span class=g>gentamicin, tobramycin, amikacin</span>",
  "<b>DRUG OF CHOICE for febrile neutropenia, sepsis, and enterococcal synergy.</b> Gram-negative activity "
  "including Pseudomonas.",
  "<b>Traditionally dosed every 8 hours, now every 24 hours</b> because of the <b>post-antibiotic effect</b>. "
  "Renally adjusted, with peak and trough monitoring.",
  "DOC", L1, 68, ["Drug of Choice", "Febrile neutropenia", "Sepsis", "Enterococcal synergy",
                  "Post antibiotic effect"]),
 ("Linezolid<br><span class=g>Zyvox</span>",
  "<b>DRUG OF CHOICE for hospital-acquired and community-acquired MRSA.</b> Covers resistant gram-positives "
  "including multidrug-resistant pneumococcus, MRSA and <b>VRE</b>. <b>No gram-negative or anaerobic cover.</b>",
  "Counsel on <b>tyramine-containing foods</b> and check for <b>SSRIs and pseudoephedrine</b> &mdash; serotonin "
  "syndrome risk.",
  "DOC", L1, 71, ["Drug of Choice", "HAP-MRSA", "CA-MRSA", "VRE", "No gram - or anaerobes"]),
 ("Clindamycin<br><span class=g>Cleocin</span>",
  "<b>DRUG OF CHOICE for toxin-mediated diseases, skin and soft tissue infection, osteomyelitis, surgical "
  "prophylaxis in penicillin allergy, and intra-abdominal combination therapy.</b>",
  "Covers gram-positive aerobes <b>including MRSA</b> and both gram-positive and gram-negative anaerobes, but "
  "<b>NO gram-negative aerobic coverage</b>.",
  "DOC", L1, 80, ["Drug of Choice", "Toxin-mediated diseases", "Osteomyelitis", "pen-allergy",
                  "NO gram - aerobic coverage"]),

 # ---------------- FLUOROQUINOLONES ----------------
 ("Fluoroquinolones<br><span class=g>class</span>",
  "<b>DRUG OF CHOICE for community-acquired pneumonia, sinusitis and otitis, hospital-acquired pneumonia (higher "
  "dose), urinary tract infection, infectious diarrhoeas, skin infection and osteomyelitis.</b>",
  "<b>Separate from iron, antacids, multivitamins, calcium and dairy.</b> The deck flags <b>OVERUSE = "
  "RESISTANCE</b> and collateral damage with <i>C. difficile</i>. Watch the <b>QTc</b> and central nervous "
  "system effects <b>in the elderly</b>.",
  "DOC", L1, 75, ["Drug of Choice", "CAP", "Sinusitis/otitis", "Osteomyelitis", "OVERUSE = RESISTANCE"]),
 ("Levofloxacin, moxifloxacin<br><span class=g>3rd generation</span>",
  "Both are used in <b>community-acquired pneumonia</b> with strep and atypical coverage. "
  "<b>Levofloxacin has Pseudomonas coverage; moxifloxacin does not.</b>",
  "<b>Moxifloxacin must not be used for urinary tract infections</b> &mdash; the one fluoroquinolone that fails "
  "there. Moxifloxacin needs no dosing adjustment; levofloxacin is renally adjusted.",
  "IND", L1, 78, ["Do not use for urinary tract infections", "Pseudomonas coverage",
                  "community acquired pneumonia"]),

 # ---------------- OTHER ANTIBACTERIALS ----------------
 ("Trimethoprim/sulfamethoxazole<br><span class=g>Septra, Bactrim</span>",
  "<b><i>Pneumocystis jirovecii</i> pneumonia &mdash; treatment AND prophylaxis.</b> Urinary tract infection, "
  "bacterial prostatitis, orchitis and epididymitis; respiratory tract infection; and gastrointestinal infection "
  "including <b>traveller's diarrhoea</b> and <i>Shigella</i> enteritis.",
  "The PJP indication is the flagship one. Check for <b>warfarin (raises INR), phenytoin, digoxin and "
  "sulfonylureas (hypoglycaemia)</b>.",
  "IND", L1, 84, ["PJP", "Pneumocystic jiroveci", "prophylaxis", "prostatitis", "Traveler’s diarrhea"]),
 ("Metronidazole<br><span class=g>Flagyl</span>",
  "<b>DRUG OF CHOICE for <i>Clostridium difficile</i> (intravenous or oral)</b>, intra-abdominal combination "
  "therapy, and sexually transmitted infections. Covers gram-positive and gram-negative <b>anaerobes</b> and "
  "parasites.",
  "<b>Counsel the patient not to drink alcohol</b> &mdash; disulfiram-like reaction with ethanol.",
  "DOC", L1, 86, ["Drug of Choice", "Clostridium difficile", "Intra-abdominal combination", "STIs",
                  "Disulfiram-like reaction"]),
 ("Polymyxin B and E<br><span class=g>colistin</span>",
  "Broad <b>gram-negative</b> coverage. Use is <b>likely to increase because of rising multidrug resistance</b>, "
  "after 50 years of disuse.",
  "<b>Optimal dosing regimens have not been thoroughly studied</b> &mdash; the deck is explicit that this is a "
  "salvage agent with three black box warnings.",
  "IND", L1, 88, ["Use is likely to increase", "MDR", "Optimal dosage regimens",
                  "have not been thoroughly studied"]),

 # ---------------- ANTIFUNGALS ----------------
 ("Amphotericin B<br><span class=g>polyene</span>",
  "<b><i>Cryptococcus</i>, <i>Blastomyces</i>, <i>Histoplasma</i>, <i>Candida</i>, <i>Coccidioides</i> and "
  "<i>Aspergillus</i></b> &mdash; <b>reserved for invasive infections</b>.",
  "<b>Pre-treat with paracetamol, antihistamines and corticosteroids</b> for the fever and chills, and "
  "<b>hydrate with normal saline</b> for the renal tubule damage. Infused over 4 hours.",
  "IND", L1, 98, ["Cryptococcus", "Blastomyces", "Histoplasma", "reserved for invasive infections",
                  "Pretreat"]),
 ("Flucytosine<br><span class=g>Ancobon</span>",
  "<b><i>Cryptococcus neoformans</i> and <i>Candida</i>.</b> Used <b>with amphotericin B in cryptococcal "
  "meningitis</b>, and with itraconazole in chromoblastomycosis.",
  "Almost always a <b>combination</b> agent &mdash; the slide never gives it alone.",
  "IND", L1, 100, ["Cryptococcus neoformans", "Candida", "Used with amphotericin B",
                   "cryptococcal meningitis"]),
 ("Azoles &mdash; class",
  "<b><i>Candida</i>, <i>Cryptococcus</i>, <i>Blastomyces</i>, <i>Histoplasma</i>, <i>Coccidioides</i>, "
  "<i>Aspergillus</i></b>, plus the tineas: <b>tinea pedis (athlete's foot), tinea corporis (ringworm), tinea "
  "cruris (jock itch), tinea unguium (onychomycosis)</b>.",
  "The four tinea names and their plain-English equivalents are the most quotable thing on this slide.",
  "IND", L1, 102, ["Tinea pedis", "athletes foot", "Tinea corporis", "ringworm", "Tinea cruris",
                   "Tinea unguium"]),
 ("Fluconazole<br><span class=g>Diflucan</span>",
  "<b>Best oral absorption</b> of the azoles. <b>Penetrates the central nervous system &mdash; cryptococcal "
  "meningitis</b>, and preventative in AIDS. Oral and vaginal <b>candidiasis</b>.",
  "<b>Single dose for vaginal candidiasis</b> &mdash; excreted in urine. Available intravenously and orally.",
  "IND", L1, 106, ["best oral absorption", "Penetrates CNS", "cryptococcal meningitis",
                   "single dose for vaginal candidiasis"]),
 ("Posaconazole<br><span class=g>Noxafil</span>",
  "<i>Aspergillus</i> and <i>Candida</i>, and <b>the ONLY azole effective against Zygomycetes (<i>Mucor</i>, "
  "<i>Rhizopus</i>)</b>. Effective in <b>refractory</b> fungal infection.",
  "The Zygomycetes exclusivity is the fact worth carrying.",
  "IND", L1, 105, ["only azole effective against Zygomycetes", "Mucor", "Rhizopus", "refractory"]),
 ("Voriconazole<br><span class=g>Vfend</span>",
  "<b>Systemic <i>Aspergillus</i> and <i>Candida</i></b> &mdash; it <b>replaced amphotericin for systemic "
  "aspergillus infections</b>.",
  "Warn about <b>visual effects, which occur in 30%</b>.",
  "IND", L1, 107, ["systemic aspergillus", "replacing Amphotericin"]),
 ("Echinocandins<br><span class=g>caspofungin, micafungin, anidulafungin</span>",
  "<b>Oesophageal candidiasis</b>, <b>systemic aspergillus not responding to itraconazole or amphotericin</b>, "
  "and <b>febrile neutropenic patients not responding to antibiotics</b>.",
  "Positioned as the salvage option after the azoles and amphotericin fail.",
  "IND", L1, 109, ["Esophageal candidiasis", "not responding to itraconazole", "febrile neutropenic"]),
 ("Griseofulvin<br><span class=g>mitotic inhibitor</span>",
  "<b>Dermatophytes only &mdash; not <i>Candida</i>.</b> Deposited in keratin precursor cells of skin, hair and "
  "nails.",
  "<b>Absorption increases with a high-fat meal.</b> Treatment is long: <b>scalp 1 month, fingernails 6&ndash;9 "
  "months, toenails up to 12 months</b> &mdash; set that expectation up front.",
  "EDU", L1, 110, ["Scalp infections", "Fingernails", "Toenails", "onychomycosis"]),
 ("Terbinafine, naftifine<br><span class=g>allylamines &mdash; Lamisil, Naftin</span>",
  "<b>Superficial dermatophyte infections.</b> Naftifine topical; <b>terbinafine oral or topical</b>.",
  "Duration again: <b>fingernails 6&ndash;12 weeks, toenails up to 12 months</b>.",
  "EDU", L1, 112, ["Superficial dermatophyte", "Fingernails", "Toenails", "12 months"]),

 # ---------------- ANTIVIRALS ----------------
 ("Aciclovir, valaciclovir<br><span class=g>Zovirax, Valtrex</span>",
  "<b>Herpes simplex and varicella-zoster.</b>",
  "<b>Valaciclovir is the prodrug with far better bioavailability &mdash; 70% against aciclovir's 22%</b>, which "
  "is why it is dosed less often. <b>Maintain hydration</b>: it crystallizes in the renal tubule.",
  "EDU", L1, 122, ["Herpes simplex", "Varicella-zoster", "Acyclovir (22%)", "Valacyclovir", "prodrug"]),
 ("Aciclovir<br><span class=g>chickenpox timing</span>",
  "For chickenpox, <b>if given in the first 24 hours it shortens the acute illness &mdash; but it does not cure "
  "the infection.</b>",
  "That distinction (shortens, does not cure) is exactly the kind of patient-education wording a stem will test.",
  "EDU", L1, 123, ["first 24 hours", "shortens acute illness", "doesn’t cure infection"]),
 ("Ganciclovir, valganciclovir<br><span class=g>Cytovene, Valcyte</span>",
  "<b>Cytomegalovirus in transplant and immunocompromised patients.</b>",
  "Valganciclovir's bioavailability is <b>61% against ganciclovir's 6&ndash;9%</b>. Warn that <b>33% of patients "
  "must stop intravenous treatment because of side effects</b>.",
  "EDU", L1, 125, ["CMV in transplant", "immunocompromised", "Valganciclovir (61%)"]),
 ("Oseltamivir<br><span class=g>Tamiflu</span>",
  "<b>Influenza A and B.</b> A prodrug that inhibits <b>influenza neuraminidase</b>, preventing budding progeny "
  "from being cleaved.",
  "<b>MUST be started as soon as possible &mdash; within 48 hours.</b> Flu season is roughly <b>October to "
  "March</b>. Resistance is becoming a problem.",
  "EDU", L1, 126, ["influenza A and B", "within 48 hours", "October to March", "neuraminidase"]),
 ("Albendazole, mebendazole<br><span class=g>Albenza, Emverm</span>",
  "<b>Hookworms, roundworms, pinworms and whipworms.</b>",
  "Very well tolerated; expect only gastrointestinal upset in most patients.",
  "IND", L1, 115, ["Hookworms", "roundworms", "pinworms", "whipworms"]),

 # ---------------- DERMATOLOGY ----------------
 ("Benzoyl peroxide",
  "<b>Acne</b> &mdash; converted to benzoic acid in the stratum corneum, active against <i>P. acnes</i>, with "
  "peeling and comedolytic effects. Available over the counter.",
  "<b>Start at 2.5% once daily</b> and increase as tolerated. <b>Warn that it bleaches hair, clothes and "
  "bedding.</b>",
  "EDU", L2, 21, ["Start at low concentration (2.5%)", "Available OTC", "bleach hair", "clothes"]),
 ("Topical retinoids<br><span class=g>tretinoin, adapalene, tazarotene</span>",
  "<b>First-line for noninflammatory (comedonal) acne</b>; combined with other agents for inflammatory acne. "
  "Also useful for <b>wrinkles and dyspigmentation</b>.",
  "<b>Tretinoin is photolabile &mdash; apply at night.</b> <b>Benzoyl peroxide inactivates tretinoin</b>, so do "
  "not layer them. <b>Adapalene is stable in sunlight and with benzoyl peroxide, and is less irritating.</b>",
  "EDU", L2, 25, ["Adapalene", "Stable in sunlight", "stable with benzoyl peroxide", "less irritating"]),
 ("Isotretinoin<br><span class=g>Accutane</span>",
  "<b>Severe acne when topical treatment is not enough &mdash; effective in 1 to 3 months.</b>",
  "<b>iPledge enrolment.</b> Contraindicated in pregnancy and breastfeeding, and <b>men should avoid as well</b>. "
  "<b>Monitor for signs of developing depression</b> and for raised serum lipids.",
  "EDU", L2, 27, ["effective in 1-3 months", "iPledge", "Monitor for signs of developing depression"]),
 ("Topical antibiotics for acne<br><span class=g>clindamycin, erythromycin</span>",
  "<b>Clindamycin is the preferred agent.</b> Erythromycin is <b>losing efficacy over time due to <i>P. acnes</i> "
  "resistance</b>.",
  "<b>They lack systemic side effects</b> &mdash; the advantage of the topical route.",
  "IND", L2, 26, ["Clindamycin", "preferred agent", "Losing efficacy", "Lack systemic side effects"]),
 ("Spironolactone, oral contraceptives<br><span class=g>antiandrogens for acne</span>",
  "<b>Useful in some women</b> with acne. Ethinyl estradiol with norethindrone.",
  "The deck is explicit that this is a <b>women-only</b> option in the acne algorithm.",
  "IND", L2, 29, ["Antiandrogens", "Spironolactone", "Oral contraceptives", "Useful in some women"]),
 ("Topical corticosteroids<br><span class=g>atopic dermatitis</span>",
  "<b>The gold standard for atopic dermatitis.</b> <b>Low potency for face, intertriginous areas and infants</b>; "
  "medium potency for the body; <b>medium-high for exacerbations</b>.",
  "<b>Use the higher potency for 1 to 2 weeks, then step down.</b> Choice depends on severity <b>and site</b>.",
  "EDU", L2, 37, ["gold standard", "Low potency", "face, intertriginous areas, infants",
                  "1-2 weeks"]),
 ("Tacrolimus, pimecrolimus<br><span class=g>Protopic, Elidel</span>",
  "<b>Second-line agents after topical steroids</b> for atopic dermatitis &mdash; they reduce extent, severity "
  "and symptoms by inhibiting T cells, mast cells and keratinocytes.",
  "<b>Use a high-SPF sunscreen.</b> Expect a <b>burning sensation</b>. Avoid in immunosuppressed patients.",
  "EDU", L2, 43, ["Second line agents after topical steroids", "Use high SP", "burning sensation"]),
 ("Topical azoles<br><span class=g>clotrimazole, miconazole, sertaconazole</span>",
  "<b>Topical and vaginal use &mdash; vulvovaginal candidiasis.</b> Sometimes combined with corticosteroids for "
  "more rapid symptom relief.",
  "<b>Treatment is generally prolonged &mdash; 2 to 3 weeks.</b> Tell them to finish the course.",
  "EDU", L2, 51, ["topical and vaginal uses", "vulvovaginal candidiasis", "combined with corticosteroids",
                  "2-3 weeks"]),
 ("Topical aciclovir, penciclovir<br><span class=g>Zovirax, Denavir</span>",
  "<b>Recurrent orolabial herpes simplex infection.</b> Active against herpesvirus simplex 1 and 2.",
  "Expect local irritation.",
  "IND", L2, 56, ["recurrent orolabial herpes simplex", "simplex 1 and 2", "local irritation"]),
 ("Mupirocin<br><span class=g>Bactroban</span>",
  "Most gram-positive aerobes, <b>especially MRSA</b>. <b>Used to eliminate nasal carriage of <i>S. aureus</i>.</b>",
  "<b>Not absorbed</b>, but may irritate mucous membranes.",
  "IND", L2, 47, ["esp. MRSA", "eliminate nasal carriage", "Not absorbed"]),
 ("Imiquimod<br><span class=g>Aldara</span>",
  "<b>External and perianal warts, actinic keratoses, and basal cell carcinoma.</b> An immunomodulator that "
  "drives interferon-alpha, tumour necrosis factor and interleukins.",
  "Applied <b>two to five times per week</b>. <b>Skin irritation occurs in virtually all patients &mdash; and "
  "the degree of inflammation parallels efficacy</b>, so warn them it is expected.",
  "EDU", L2, 57, ["external and perianal warts", "actinic keratoses", "basal cell carcinoma",
                  "two to five times per week", "parallels efficacy"]),
 ("Ciclopirox<br><span class=g>Penlac nail lacquer</span>",
  "Dermatomycosis, candidiasis and tinea versicolor; marketed as a <b>nail lacquer for onychomycosis</b>.",
  "Set expectations honestly: the nail lacquer is <b>less than 12% effective</b>.",
  "EDU", L2, 52, ["nail lacquer", "onychomycosis", "12% effective"]),
 ("Nystatin, tolnaftate<br><span class=g>topical antifungals</span>",
  "<b>Nystatin for candidal infections</b>, cutaneous and mucosal. <b>Tolnaftate has NO candida activity.</b>",
  "Tolnaftate <b>must be used long term to prevent recurrence</b>. Nystatin has <b>no oral absorption</b>.",
  "EDU", L2, 54, ["Tolnaftate", "long term therapy to prevent recurrence", "No candida activity",
                  "Nystatin", "No oral absorption"]),

 # ---------------- ANS: CHOLINERGIC ----------------
 ("Bethanechol<br><span class=g>Urecholine</span>",
  "<b>Stimulates a postpartum or postoperative atonic bladder.</b> Strong muscarinic activity, <b>no nicotinic "
  "activity</b>; increases voiding pressure and decreases bladder capacity.",
  "Not hydrolyzed by acetylcholinesterase, so its action is sustained.",
  "IND", L3, 30, ["Stimulate postpartum or postoperative atonic bladder", "Lacks nicotinic activity"]),
 ("Pilocarpine<br><span class=g>Salagen, Isopto Carpine</span>",
  "<b>Decreases intraocular pressure</b> &mdash; miosis and ciliary muscle contraction. Also <b>stimulates "
  "salivation in xerostomia (dry mouth)</b>.",
  "<b>Onset within minutes, duration 4 to 8 hours.</b> A potent stimulator of sweat, tears and saliva.",
  "EDU", L3, 33, ["Decreases intraocular pressure", "Onset within minutes", "Duration 4 to 8 hours",
                  "xerostomia"]),
 ("Carbachol<br><span class=g>Miostat</span>",
  "<b>Decreases intraocular pressure in glaucoma.</b> Has <b>both muscarinic and nicotinic</b> activity.",
  "Causes <b>miosis and spasm of accommodation</b> &mdash; warn about the near-vision blur.",
  "IND", L3, 32, ["decrease intraocular", "glaucoma", "muscarinic and nicotinic",
                  "spasm of accommodation"]),
 ("Edrophonium",
  "<b>Diagnosing myasthenia gravis</b>, assessing cholinesterase therapy, and <b>reversing nondepolarizing "
  "neuromuscular blockers after surgery</b>.",
  "The <b>short-acting</b> prototype &mdash; short duration is what makes it a diagnostic rather than a "
  "treatment agent.",
  "IND", L3, 35, ["Diagnosing myasthenia gravis", "short-acting", "Reversing effects of nondepolarizing"]),
 ("Neostigmine, pyridostigmine<br><span class=g>Prostigmin, Mestinon</span>",
  "Neostigmine <b>stimulates the bladder and gastrointestinal tract</b>, is the <b>antidote for competitive "
  "neuromuscular blockers</b>, and treats myasthenia gravis symptomatically. <b>Pyridostigmine is for CHRONIC "
  "management of myasthenia gravis.</b>",
  "Neostigmine is <b>poorly absorbed from the gut and does not enter the central nervous system</b> &mdash; which "
  "is why it is safe peripherally.",
  "IND", L3, 38, ["Stimulate bladder and GI tract", "Antidote for competitive neuromuscular",
                  "does not enter CNS"]),
 ("Physostigmine<br><span class=g>Antilirium</span>",
  "<b>Treatment of overdoses of anticholinergic drugs</b> &mdash; atropine, phenothiazines and tricyclic "
  "antidepressants. Also increases intestinal and bladder motility in atony and decreases intraocular pressure.",
  "It is the one that <b>does</b> enter the central nervous system, which is exactly why it works for a central "
  "anticholinergic overdose.",
  "IND", L3, 36, ["Treatment of overdoses of anticholinergic", "atropine", "tricyclic antidepressants"]),
 ("Donepezil, rivastigmine, galantamine<br><span class=g>Aricept, Exelon, Razadyne</span>",
  "<b>Slow the progression of Alzheimer's disease</b>, which is associated with a deficiency of cholinergic "
  "neurons in the central nervous system.",
  "Expect <b>gastrointestinal distress</b> &mdash; the limiting side effect of the class.",
  "IND", L3, 40, ["Slow progression of Alzheimer", "deficiency of cholinergic neurons", "GI distress"]),
 ("Pralidoxime<br><span class=g>Protopam</span>",
  "<b>Reactivates inhibited acetylcholinesterase</b> after organophosphate (insecticide) poisoning.",
  "Two limits to know: it <b>does not penetrate the central nervous system</b>, and it <b>cannot overcome "
  "reversible inhibitors such as physostigmine</b>.",
  "IND", L3, 42, ["Pralidoxime", "reactivate inhibited AChE", "Does not penetrate CNS"]),
 ("Atropine",
  "<b>Antisecretory</b> before surgery or in end-of-life care; <b>ophthalmic</b> pupil dilation; "
  "<b>gastrointestinal antispasmodic</b>; and the <b>antidote for cholinesterase inhibitor insecticides and some "
  "mushroom poisoning</b>. <b>Given during a Code Blue for bradycardia.</b>",
  "Dose-dependent and counterintuitive: <b>bradycardia at LOWER doses, tachycardia at HIGHER doses</b>.",
  "IND", L3, 51, ["Antisecretory", "Antidote for cholinergic agonists", "mushroom poisoning",
                  "Antispasmodic"]),
 ("Scopolamine<br><span class=g>Transderm Scop</span>",
  "<b>Prevention of motion sickness</b>, adjunct in anaesthesia, short-term memory blocking, and reducing "
  "secretions.",
  "<b>Wash hands thoroughly after placing the patch</b> &mdash; touching an eye afterwards causes blurred vision.",
  "EDU", L3, 54, ["Prevention of motion sickness", "Transderm Scop", "wash hands thoroughly"]),
 ("Ipratropium, tiotropium, glycopyrrolate<br><span class=g>Atrovent, Spiriva, Robinul</span>",
  "<b>Inhaled bronchodilators for maintenance treatment of bronchospasm in COPD.</b> Glycopyrrolate also reduces "
  "pre-surgical secretions, <b>excessive drooling in cerebral palsy</b>, stomach acid, and <b>hyperhidrosis</b>.",
  "<b>Adverse effects are limited because they cannot enter the systemic circulation or the central nervous "
  "system</b> &mdash; the reason inhaled antimuscarinics are well tolerated.",
  "EDU", L3, 55, ["Inhaled bronchodilators for maintenance", "chronic obstructive pulmonary disease",
                  "drooling", "hyperhidrosis", "unable to enter systemic circulation"]),
 ("Oxybutynin, tolterodine, solifenacin<br><span class=g>bladder antimuscarinics</span>",
  "<b>Lower intravesicular pressure, increase bladder capacity, and reduce the frequency of bladder "
  "contractions</b> in overactive bladder.",
  "<b>Newer agents cause fewer central effects because they are designed not to cross the blood-brain "
  "barrier</b> &mdash; the reason to switch an older patient off oxybutynin.",
  "EDU", L3, 56, ["Lower intravesicular pressure", "Increase bladder capacity",
                  "not to cross blood-brain barrier"]),
 ("Succinylcholine",
  "<b>Endotracheal intubation during induction of anaesthesia</b>, and <b>rapid sequence intubation in the "
  "emergency department</b> &mdash; because of its rapid onset and short duration.",
  "<b>Give a small dose of a nondepolarizing blocker first</b> to reduce the fasciculations that cause muscle "
  "soreness. <b>Respiratory muscles are paralysed LAST.</b>",
  "EDU", L3, 66, ["endotracheal intubation", "rapid sequence intubation", "rapid onset",
                  "short duration"]),

 # ---------------- ANS: ADRENERGIC ----------------
 ("Epinephrine",
  "<b>ANAPHYLACTIC SHOCK. CARDIAC ARREST.</b> And as an additive to <b>local anaesthetic solutions &mdash; "
  "usually 1:100,000 parts</b>.",
  "In local anaesthesia it <b>greatly increases the duration</b> by producing <b>vasoconstriction at the "
  "injection site</b>, and applied topically it <b>helps control oozing of capillary blood</b>.",
  "IND", L3, 85, ["Anaphylactic shock", "Cardiac arrest", "1:100,000", "Greatly increases duration",
                  "control oozing of capillary blood"]),
 ("Epinephrine<br><span class=g>respiratory and metabolic</span>",
  "<b>Bronchospasm &mdash; ACUTE reversal.</b> Also drives hyperglycaemia: increases hepatic glycogenolysis and "
  "glucagon release (beta-2) and decreases insulin release (alpha-1).",
  "<b>Selective beta-2 agonists such as albuterol are used for CHRONIC treatment instead</b>, because of their "
  "longer duration and less cardiac stimulation. Acute versus chronic is the whole distinction.",
  "EDU", L3, 84, ["Bronchospasm", "Acute reversal", "albuterol used for chronic treatment",
                  "less cardiac stimulation"]),
 ("Epinephrine<br><span class=g>the dose-response</span>",
  "<b>LOW doses: beta effects predominate &mdash; vasodilation.</b> <b>HIGH doses: alpha effects predominate "
  "&mdash; vasoconstriction.</b> Increases cardiac output and systolic pressure while <b>decreasing diastolic "
  "pressure</b>.",
  "The low-versus-high reversal is the same trap as atropine's heart rate, and gets asked the same way.",
  "IND", L3, 83, ["Low doses", "vasodilation", "High doses", "vasoconstriction",
                  "Decreased diastolic BP"]),
 ("Isoproterenol",
  "<b>Stimulate the heart in an emergency.</b> Predominantly beta-1 and beta-2; a positive inotrope and "
  "chronotrope that increases cardiac output.",
  "<b>Inhaled products are no longer available in the United States.</b>",
  "IND", L3, 91, ["Stimulate heart in emergency", "Inhaled products no longer available"]),
 ("Oxymetazoline<br><span class=g>Afrin</span>",
  "<b>Nasal decongestant</b> and <b>relief of redness in the eyes</b>. An alpha-1 and alpha-2 agonist producing "
  "vasoconstriction.",
  "<b>DO NOT USE LONGER THAN THREE DAYS &mdash; rhinitis medicamentosa (rebound congestion) may occur.</b> The "
  "single most useful counselling point on any over-the-counter product in this lecture.",
  "EDU", L3, 95, ["Nasal decongestant", "Rhinitis", "rebound congestion", "longer than three days"]),
 ("Phenylephrine<br><span class=g>Neo-Synephrine</span>",
  "<b>Nasal decongestant, relief of redness in the eyes, and septic shock.</b> A selective alpha-1 agonist.",
  "It raises systolic and diastolic pressure and <b>induces REFLEX BRADYCARDIA</b> &mdash; the heart slows even "
  "though the drug is a stimulant.",
  "IND", L3, 96, ["Nasal decongestant", "Septic shock", "reflex", "bradycardia"]),
 ("Amphetamine",
  "<b>Hyperactivity, narcolepsy, and appetite control.</b> Blocks norepinephrine uptake and increases cellular "
  "release of stored catecholamines.",
  "Raises blood pressure (alpha-1), stimulates the heart (beta-1) and increases central nervous system activity.",
  "IND", L3, 100, ["Treatment of hyperactivity, narcolepsy", "appetite control",
                   "Blocks norepinephrine uptake"]),
 ("Tyramine",
  "<b>NO therapeutic use.</b> A normal by-product of tyrosine metabolism, <b>found in fermented foods such as "
  "cheese and wine</b>.",
  "<b>May cause serious vasopressor effects if the patient is taking a monoamine oxidase inhibitor</b> &mdash; "
  "normally it is oxidised by MAO in the gut. This is the food-interaction counselling point.",
  "EDU", L3, 101, ["Normal by-product of tyrosine metabolism", "serious vasopressor effects",
                   "MAOI", "fermented foods", "cheese and wine"]),
 ("Cocaine",
  "<b>Local anaesthetic</b> &mdash; it blocks neuronal sodium channels. It also blocks norepinephrine reuptake, "
  "potentiating norepinephrine and epinephrine.",
  "Raises blood pressure, stimulates the heart and increases central nervous system activity &mdash; which is "
  "why it exaggerates the cardiovascular actions of epinephrine.",
  "IND", L3, 102, ["Blocks reuptake of norepinephrine", "Anesthetic", "Blocks neuronal sodium channels",
                   "Local anesthetic"]),
 ("Nondepolarizing blockers<br><span class=g>pancuronium, vecuronium, rocuronium, cisatracurium</span>",
  "<b>Adjuvant drugs in anaesthesia to relax skeletal muscle</b>, to <b>facilitate intubation</b>, and <b>during "
  "orthopaedic surgery for fracture alignment and dislocation correction</b>.",
  "<b>Atracurium was replaced by its isomer cisatracurium (Nimbex) because of fewer adverse effects.</b>",
  "IND", L3, 63, ["adjuvant drugs in anesthesia", "Facilitate intubation", "orthopedic surgery",
                  "cisatracurium", "fewer adverse effects"]),
 ("Norepinephrine",
  "<b>Shock</b> &mdash; it increases vascular resistance.",
  "Given as a <b>continuous intravenous infusion titrated to effect</b>. If it extravasates, treat with "
  "<b>phentolamine</b>.",
  "IND", L3, 90, ["Shock", "increases vascular resistance", "continuous IV infusion", "phentolamine"]),
 ("Dopamine",
  "<b>Cardiogenic and septic shock.</b>",
  "Adverse effects to expect: nausea, hypertension and arrhythmias.",
  "IND", L3, 93, ["Cardiogenic and septic shock", "Nausea", "Hypertension", "Arrhythmias"]),
 ("Dopamine<br><span class=g>the dose-response</span>",
  "Dose-dependent across three receptor families: <b>beta-1 inotrope and chronotrope</b>; <b>alpha-1 "
  "vasoconstriction only at VERY HIGH doses</b>; and it <b>dilates renal and splanchnic arteries</b> through "
  "dopaminergic receptors.",
  "The three-tier dose response is the point of the drug &mdash; the same agent does different things as the "
  "rate climbs.",
  "IND", L3, 92, ["positive inotrope", "vasoconstriction", "very high doses",
                  "dilates renal and splanchnic"]),
 ("Dobutamine",
  "<b>Increase cardiac output in acute heart failure</b>, and inotropic support after cardiac surgery.",
  "Its selling point: <b>it does not significantly increase myocardial oxygen demand</b> the way other "
  "sympathomimetics do. <b>Caution in atrial fibrillation</b> &mdash; it increases AV conduction.",
  "IND", L3, 94, ["acute heart failure", "Inotropic support after cardiac surgery",
                  "Does not significantly increase oxygen demand"]),
 ("Albuterol",
  "<b>Asthma and COPD</b> &mdash; a synthetic beta-2 agonist producing bronchodilation.",
  "Expect <b>tremor, restlessness, apprehension and anxiety</b> and warn the patient, or they will think the "
  "inhaler is harming them.",
  "IND", L3, 98, ["Asthma/COPD", "Bronchodilation", "Tremor, restlessness"]),
 ("Clonidine<br><span class=g>Catapres</span>",
  "<b>Hypertension</b>, and <b>minimising withdrawal symptoms from opiates, tobacco and benzodiazepines</b>.",
  "<b>Never stop it abruptly &mdash; rebound hypertension.</b> Expect lethargy, sedation, constipation and dry "
  "mouth.",
  "EDU", L3, 97, ["Hypertension", "Minimize symptoms of withdrawal", "opiates, tobacco",
                  "Rebound hypertension"]),
 ("Pseudoephedrine, ephedrine",
  "<b>Pseudoephedrine relieves nasal and sinus congestion.</b> Ephedrine was once used to prevent asthma attacks; "
  "<b>ephedra-containing herbal products were banned by the FDA in 2004</b>.",
  "<b>Kept behind the pharmacy counter because it can be converted to methamphetamine</b> &mdash; the reason a "
  "patient needs ID to buy it.",
  "EDU", L3, 104, ["Pseudoephedrine used to relieve nasal", "banned by FDA in 2004",
                   "converted to methamphetamine", "behind pharmacy counter"]),
 ("Phenoxybenzamine",
  "<b>Pheochromocytoma</b> (a catecholamine-secreting tumour of adrenal medulla origin) and <b>autonomic "
  "hyperreflexia in paraplegic patients</b>.",
  "The block is <b>irreversible</b> &mdash; the body must synthesise new receptors, which takes <b>at least 24 "
  "hours</b>.",
  "IND", L3, 109, ["pheochromocytoma", "catecholamine-secreting tumor", "hyperreflexia", "paraplegic"]),
 ("Phentolamine",
  "<b>Short-term management of pheochromocytoma</b>; <b>preventing dermal necrosis from norepinephrine "
  "extravasation</b>; <b>hypertensive crisis after abrupt clonidine withdrawal</b>; and impotence.",
  "Actions last about <b>4 hours</b> and it produces <b>postural hypotension</b>.",
  "IND", L3, 110, ["Short-term management of pheochromocytoma", "extravasation",
                   "abrupt clonidine withdrawal", "impotence"]),
 ("Prazosin, terazosin, doxazosin<br><span class=g>alpha-1 blockers</span>",
  "<b>Hypertension</b> &mdash; they decrease peripheral vascular resistance. <b>Tamsulosin and alfuzosin are for "
  "benign prostatic hyperplasia</b>, decreasing tone in the bladder neck and prostate.",
  "<b>Warn about first-dose syncope.</b> A bonus worth knowing: they <b>improve lipid profiles and glucose "
  "metabolism</b>.",
  "EDU", L3, 111, ["Hypertension", "Benign prostatic hyperplasia", "first-dose", "syncope",
                   "Improve lipid profiles"]),
 ("Propranolol",
  "<b>Antihypertensive, migraine prevention, hyperthyroidism, angina pectoris, and myocardial infarction</b> "
  "&mdash; it <b>prevents a second MI, reduces infarct size, and reduces post-MI sudden death</b>.",
  "In hyperthyroidism it works by <b>blunting the widespread sympathetic stimulation</b>, not by treating the "
  "thyroid.",
  "IND", L3, 116, ["Antihypertensive", "Migraine prevention", "Hyperthyroidism", "Angina pectoris",
                   "prevent second MI"]),
 ("Timolol, nadolol",
  "<b>Timolol reduces production of aqueous humour &mdash; used in chronic open-angle glaucoma.</b> "
  "Occasionally used for hypertension.",
  "<b>More potent than propranolol</b>, and nonselective.",
  "IND", L3, 119, ["reduces production of aqueous humor", "chronic open-angle glaucoma",
                   "More potent than propranolol"]),
 ("Atenolol, metoprolol, bisoprolol, esmolol<br><span class=g>selective beta-1</span>",
  "<b>Useful to treat hypertension in patients with impaired pulmonary function</b> &mdash; the reason "
  "cardioselectivity matters clinically.",
  "<b>Cardioselectivity is LOST at higher doses</b>, so it is not a free pass in airway disease.",
  "IND", L3, 120, ["Useful to treat hypertension", "impaired pulmonary function", "Cardioselectivity"]),
 ("Labetalol, carvedilol",
  "<b>Labetalol intravenously for hypertensive emergencies.</b> <b>Carvedilol prevents cardiovascular mortality "
  "in heart failure</b> and decreases lipid peroxidation and vascular wall thickening.",
  "Both produce peripheral vasodilation and <b>may cause orthostatic hypotension from alpha-1 blockade</b>.",
  "IND", L3, 122, ["Labetalol", "hypertensive emergencies", "Carvedilol",
                   "prevent cardiovascular mortality"]),
]
