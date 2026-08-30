# -*- coding: utf-8 -*-
"""Side effects and monitoring for Pharmacology I Exam 1.

Third of the three reference charts, and the third item on Dr. McInnis's list.
Same provenance contract: (..., deck, slide, verify).

SYS groups the effect by the system it hits, because that is how a stem gives
it to you -- "a patient on X develops ringing in the ears" is an ototoxicity
question, not a drug-name question.
"""
L1 = "Antibiotics, Antivirals, and Antifungals"
L2 = "02. Dermatology Medications"
L3 = "03. ANS Pharmacology"

# (drug, side effects, monitoring / what to watch, system, deck, slide, verify)
ROWS = [
 # ---------------- ANTIBACTERIALS ----------------
 ("Aminopenicillins<br><span class=g>ampicillin, amoxicillin</span>",
  "<b>Hepatic dysfunction, hepatitis, jaundice</b> with raised AST, ALT, bilirubin and alkaline phosphatase. "
  "<b><i>C. difficile</i> infection.</b> <b>Stevens-Johnson syndrome and toxic epidermal necrolysis.</b> "
  "<b>Interstitial nephritis, haematuria, crystalluria.</b> Anaemia and thrombocytopenia.",
  "Monitor <b>liver enzymes and bilirubin</b>; watch for rash progressing to blistering.",
  "Multi-system", L1, 21, ["Hepatic dysfunction", "jaundice", "Clostridium difficile",
                           "Stevens-Johnson", "Interstitial nephritis", "Anemia, thrombocytopenia"]),
 ("Penicillins &mdash; class",
  "<b>Hypersensitivity reaction</b>, rash and diarrhoea.",
  "Monitor <b>renal and hepatic function and platelets</b>; dosing frequency drops with renal impairment.",
  "Allergy", L1, 22, ["Hypersensitivity Reaction", "Rash", "Diarrhea", "Renal and Hepatic function"]),
 ("Piperacillin/tazobactam<br><span class=g>Zosyn</span>",
  "<b>Hypersensitivity reaction</b>, rash and diarrhoea.",
  "Monitor for <b>signs and symptoms of anaphylaxis</b>, renal function and full blood count.",
  "Allergy", L1, 28, ["Hypersensitivity Reaction", "Rash", "Diarrhea",
                      "Signs/symptoms of anaphylaxis"]),
 ("Nafcillin, oxacillin, dicloxacillin",
  "Monitored for <b>hepatic</b> rather than renal toxicity &mdash; the exception in the beta-lactams.",
  "<b>Monitor hepatic function and full blood count</b>, plus signs and symptoms of anaphylaxis. <b>Dosing "
  "considerations are hepatic function.</b>",
  "Hepatic", L1, 26, ["Dosing Considerations", "Hepatic Function", "Monitoring", "CBC",
                      "Signs/symptoms of anaphylaxis"]),
 ("Aztreonam<br><span class=g>monobactam</span>",
  "<b>Diarrhoea.</b>",
  "Monitor <b>liver function and signs or symptoms of anaphylaxis</b>; dosing consideration is <b>renal</b>.",
  "Gastrointestinal / Hepatic", L1, 41, ["Dosing Considerations", "Renal", "Liver function",
                                         "signs/symptoms of anaphylaxis", "Diarrhea"]),
 ("Cephalosporins &mdash; class",
  "Signs and symptoms of <b>allergic reaction</b>; nausea, vomiting and diarrhoea.",
  "<b>Penicillin cross-sensitivity is approximately less than 1%.</b> Mostly renally eliminated.",
  "Allergy", L1, 30, ["allergic reaction", "Nausea/Vomiting/Diarrhea", "Penicillin cross-sensitivity"]),
 ("Carbapenems<br><span class=g>imipenem especially</span>",
  "<b>SEIZURES &mdash; specifically with imipenem.</b>",
  "Monitor <b>renal and hepatic function</b>, <b>full blood count for bleeding</b>, and signs of anaphylaxis.",
  "Neurologic", L1, 44, ["Monitoring", "Renal", "hepatic function", "CBC for bleeding", "Seizures",
                         "Imipenem"]),
 ("Vancomycin",
  "<b>&ldquo;Red Man Syndrome&rdquo;</b> as an infusion reaction, with <b>fever, chills and phlebitis</b>. "
  "<b>Ototoxicity and nephrotoxicity.</b>",
  "Requires <b>therapeutic drug monitoring</b>. Trough drawn <b>15&ndash;30 minutes before the next dose</b>, "
  "around the <b>3rd or 4th dose</b>. Random levels in unstable or severe renal impairment.",
  "Infusion / Renal / Ear", L1, 51, ["Red Man Syndrome", "Fever/chills", "Phlebitis", "Ototoxicity",
                                     "Nephrotoxicity", "Requires TDM"]),
 ("Macrolides<br><span class=g>erythromycin, clarithromycin, azithromycin</span>",
  "<b>Nausea, diarrhoea, abdominal pain &mdash; more with erythromycin and especially in children and young "
  "adults</b>, because it stimulates motility. <b>Cholestatic hepatitis</b> (rare, more with estolate). "
  "<b>Transient hearing loss</b> with large intravenous doses or renal insufficiency. <b>QT prolongation and "
  "Torsades de pointes.</b>",
  "Worse with <b>class Ia and III antiarrhythmics</b> and <b>electrolyte abnormalities</b>. Check the ECG risk "
  "before adding.",
  "Gastrointestinal / Cardiac", L1, 57, ["Nausea, diarrhea, abdominal pain", "Stimulates motility",
                                         "Cholestatic hepatitis", "Transient hearing loss",
                                         "QT prolongation"]),
 ("Tetracyclines<br><span class=g>doxycycline, minocycline</span>",
  "<b>Photosensitivity.</b> <b>Discoloration of teeth &mdash; doxycycline more than the others.</b> "
  "<b>Depression of skeletal growth.</b>",
  "<b>Must be renally dose adjusted.</b> Counsel on sun protection and on separating doses from iron, calcium "
  "and dairy.",
  "Skin / Teeth / Bone", L1, 63, ["Photosensitivity", "Discoloration of teeth", "Doxycycline",
                                  "Depression of skeletal growth", "Must be renally dose adjusted"]),
 ("Tigecycline<br><span class=g>Tygacil</span>",
  "<b>Vomiting, nausea, diarrhoea and fever.</b>",
  "Dosing consideration is <b>hepatic dysfunction</b>, not renal &mdash; the opposite of most of this lecture.",
  "Gastrointestinal", L1, 66, ["Vomiting", "Nausea", "Diarrhea", "Fever", "Hepatic dysfunction"]),
 ("Aminoglycosides<br><span class=g>gentamicin, tobramycin, amikacin</span>",
  "<b>Renal toxicity</b> and <b>ototoxicity</b>.",
  "<b>Renally adjusted</b>, and requires therapeutic drug monitoring: <b>peaks 30 minutes after the end of the "
  "infusion, troughs 15&ndash;30 minutes before the next dose</b>, around the 3rd or 4th dose.",
  "Renal / Ear", L1, 68, ["Renal toxicity", "Ototoxic", "Renally adjusted"]),
 ("Linezolid<br><span class=g>Zyvox</span>",
  "<b>Thrombocytopenia.</b> <b>Serotonin syndrome</b> with SSRIs, tyramine-containing foods and pseudoephedrine.",
  "Check the medication list for serotonergic agents before starting; watch the <b>platelet count</b>.",
  "Haematologic / Neurologic", L1, 71, ["Thrombocytopenia", "SSRI Interactions", "tyramine",
                                        "Serotonin Syndrome"]),
 ("Fluoroquinolones<br><span class=g>class</span>",
  "<b>Tendonitis and Achilles tendon rupture.</b> <b>QT prolongation and Torsades de Pointes.</b> "
  "<b>Photosensitivity.</b> <b>Peripheral neuropathies.</b> <b>CNS toxicity &mdash; dizziness, insomnia, "
  "somnolence.</b>",
  "<b>Caution under 18 years.</b> Inhibits <b>CYP1A2</b>; complexes with cations; renally eliminated.",
  "Musculoskeletal / Cardiac / Neurologic", L1, 79, ["Tendonitis/Tendon", "achilles", "QT prolongation",
                                                     "Photosensitivity", "Peripheral neuropathies",
                                                     "CNS Toxicity"]),
 ("Clindamycin<br><span class=g>Cleocin</span>",
  "<b><i>Clostridium difficile</i> and pseudomembranous colitis</b> &mdash; the reaction this drug is known "
  "for. Also <b>rash, neutropenia and thrombocytopenia</b>.",
  "New diarrhoea on clindamycin is <i>C. difficile</i> until proven otherwise.",
  "Gastrointestinal / Haematologic", L1, 81, ["Rash", "Neutropenia", "Thrombocytopenia",
                                              "Clostridium difficile", "Pseudomembranous colitis"]),
 ("Trimethoprim/sulfamethoxazole<br><span class=g>Septra, Bactrim</span>",
  "<b>Hypersensitivity &mdash; rash, Stevens-Johnson syndrome, toxic epidermal necrolysis.</b> <b>Blood "
  "dyscrasias &mdash; thrombocytopenia, agranulocytosis, megaloblastic anaemia.</b> <b>Hepatotoxicity and "
  "hyperbilirubinaemia.</b> Nausea, vomiting, diarrhoea, anorexia.",
  "Interactions matter as much as the toxicity: raises <b>phenytoin, rifampin, digoxin</b>; reduces renal "
  "clearance of <b>methotrexate (pancytopenia)</b>; <b>hypoglycaemia with sulfonylureas</b>; <b>significantly "
  "increases INR with warfarin</b>.",
  "Skin / Haematologic / Hepatic", L1, 85, ["Hypersensitivity-rash", "SJS", "TEN", "Blood dyscrasias",
                                            "agranulocytosis", "hepatotoxicity"]),
 ("Metronidazole<br><span class=g>Flagyl</span>",
  "<b>Disulfiram-like reaction with ethanol.</b> Headache, nausea and vomiting.",
  "The alcohol counselling is the whole of the patient education for this drug.",
  "Gastrointestinal", L1, 86, ["Disulfiram-like reaction with ethanol", "Headache", "Nausea", "Vomiting"]),
 ("Polymyxin B and E",
  "<b>BLACK BOX WARNINGS for nephrotoxicity, neurotoxicity and neuromuscular blockade.</b>",
  "Three black boxes on one slide &mdash; the most heavily warned agent in the lecture.",
  "Renal / Neurologic", L1, 88, ["Black box warnings", "nephrotoxicity", "neurotoxicity",
                                 "neuromuscular blockade"]),

 # ---------------- ANTIFUNGALS ----------------
 ("Amphotericin B",
  "<b>Fever and chills</b> from interleukin-1 and tumour necrosis factor. <b>Side effects limit treatment.</b>",
  "<b>Pre-treat with paracetamol, antihistamines and corticosteroids.</b>",
  "Infusion", L1, 98, ["Fever/chills", "IL-1", "TNF", "Pretreat", "Side effects limit treatment"]),
 ("Amphotericin B",
  "<b>Electrolyte abnormalities &mdash; hypokalaemia and hypomagnesaemia.</b> <b>Hypotension.</b> <b>Uraemia in "
  "80% with decreased filtration.</b> <b>Renal tubule damage.</b>",
  "<b>Hydrate with normal saline</b> for the renal tubule damage. Lipid formulations cost 20&ndash;50 times more "
  "but have <b>reduced toxicity</b>.",
  "Renal / Electrolyte", L1, 99, ["hypokalemia", "hypomagnesemia", "Hypotension", "Uremia",
                                  "Renal tubule damage", "normal saline"]),
 ("Flucytosine<br><span class=g>Ancobon</span>",
  "<b>Bone marrow suppression.</b> <b>Hepatotoxicity.</b> Gastrointestinal disturbance and rash.",
  "Available orally only.",
  "Haematologic / Hepatic", L1, 101, ["Bone marrow suppression", "Hepatotoxicity", "GI disturbances",
                                      "Rash"]),
 ("Ketoconazole",
  "Nausea, vomiting and anorexia.",
  "<b>Inhibits CYP3A4 &mdash; significant drug interactions</b>, which is a large part of why it is now rarely "
  "used.",
  "Gastrointestinal", L1, 103, ["Nausea, vomiting, anorexia", "Inhibits CYP3A4",
                                "significant drug interactions"]),
 ("Posaconazole<br><span class=g>Noxafil</span>",
  "<b>QT prolongation</b>, fever, diarrhoea, <b>hypokalaemia, hypomagnesaemia</b> and <b>thrombocytopenia</b>.",
  "Same electrolyte pattern as amphotericin &mdash; check potassium and magnesium.",
  "Cardiac / Electrolyte", L1, 105, ["QT prolongation", "fever", "diarrhea", "Hypokalemia",
                                     "hypomagnesemia", "thrombocytopenia"]),
 ("Voriconazole<br><span class=g>Vfend</span>",
  "<b>Effects on vision in 30%</b>, plus liver and renal effects. <b>Teratogenic in animals.</b>",
  "The <b>intravenous vehicle cyclodextrin accumulates in renal failure</b> &mdash; a reason to switch to oral.",
  "Ocular / Hepatic / Renal", L1, 107, ["Effects on vision", "30%", "liver and renal function",
                                        "cyclodextrin", "accumulate in renal failure"]),
 ("Echinocandins<br><span class=g>caspofungin, micafungin, anidulafungin</span>",
  "<b>Tachycardia, headache, insomnia, hypokalaemia, hypomagnesaemia and blood dyscrasias.</b>",
  "The best-tolerated systemic antifungal class in the deck.",
  "Cardiac / Electrolyte", L1, 109, ["Tachycardia", "headache", "insomnia", "hypokalemia",
                                     "hypomagnesemia", "blood dyscrasias"]),
 ("Griseofulvin",
  "<b>Headache in 15%</b>, mental confusion, fatigue and <b>blurred vision</b>.",
  "<b>Induces CYP1A2 and CYP2C9</b> &mdash; an inducer, where most antifungals here are inhibitors.",
  "Neurologic / Ocular", L1, 111, ["Headache 15%", "Mental confusion, fatigue", "Blurred vision",
                                   "Induces microsomal enzymes"]),

 # ---------------- ANTIVIRALS / ANTHELMINTHICS ----------------
 ("Aciclovir, valaciclovir<br><span class=g>Zovirax, Valtrex</span>",
  "Nausea, vomiting, rash. <b>CNS &mdash; seizures, delirium, tremor.</b> <b>Bone marrow suppression.</b> "
  "<b>Crystallizes in the renal tubule.</b>",
  "<b>Maintain hydration and renal function</b> &mdash; the counselling point that prevents the renal injury.",
  "Renal / Neurologic", L1, 123, ["nausea, vomiting, rash", "maintain hydration", "seizures",
                                  "delirium", "bone marrow suppression", "crystallizes in renal tubule"]),
 ("Ganciclovir, valganciclovir<br><span class=g>Cytovene, Valcyte</span>",
  "<b>Neutropenia in 15&ndash;40%.</b> <b>Thrombocytopenia.</b> <b>CNS in 5&ndash;15% &mdash; confusion, ataxia, "
  "seizures, coma.</b>",
  "<b>33% of patients must stop intravenous treatment because of side effects</b> &mdash; the highest "
  "discontinuation rate in the lecture.",
  "Haematologic / Neurologic", L1, 125, ["neutropenia", "thrombocytopenia", "confusion, ataxia, seizures",
                                         "33%", "stop intravenous treatment"]),
 ("Penciclovir, famciclovir<br><span class=g>Denavir, Famvir</span>",
  "<b>Actions and toxicity similar to aciclovir</b> &mdash; the deck does not list a separate profile.",
  "Bioavailability differs sharply: <b>penciclovir 5% (intravenous), famciclovir 77% (oral prodrug)</b>.",
  "Renal / Neurologic", L1, 124, ["Actions and toxicity similar to acyclovir", "Penciclovir (5%)",
                                  "Famciclovir"]),
 ("Albendazole, mebendazole",
  "<b>Very well tolerated</b> &mdash; gastrointestinal upset, hypersensitivity, and rash including "
  "<b>Stevens-Johnson syndrome and toxic epidermal necrolysis</b>.",
  "The SJS/TEN note is the only serious entry for an otherwise benign class.",
  "Gastrointestinal / Skin", L1, 115, ["very well tolerated", "GI upset", "hypersensitivity", "SJS", "TEN"]),
 ("Pyrantel pamoate<br><span class=g>Pin-X</span>",
  "<b>Dizziness, headache and gastrointestinal upset.</b>",
  "Acts as a depolarizing neuromuscular blocker on the parasite &mdash; paralysis and death.",
  "Neurologic / Gastrointestinal", L1, 116, ["Dizziness, headache, GI upset"]),

 # ---------------- DERMATOLOGY ----------------
 ("Benzoyl peroxide",
  "<b>Bleaches hair, clothes.</b> Skin and mucous membrane irritation.",
  "Start at <b>2.5% once daily</b> and build up as tolerated.",
  "Skin", L2, 21, ["can bleach hair, clothes", "skin/mucous membrane irritation"]),
 ("Azelaic acid<br><span class=g>Azelex</span>",
  "<b>Mild skin irritation and dryness.</b> <b>Hypopigmentation.</b>",
  "<b>Improves over 6 to 8 weeks with continuous therapy</b> &mdash; tell the patient not to quit at week two.",
  "Skin", L2, 22, ["mild skin irritation/dryness", "Hypopigmentation", "6-8 weeks"]),
 ("Topical retinoids",
  "<b>Erythema, desquamation, burning and stinging</b> &mdash; these <b>decrease with time and with the use of "
  "emollients</b>. <b>Photosensitivity and severe sunburn.</b>",
  "Warning them the irritation settles is what keeps them on the drug.",
  "Skin", L2, 24, ["Erythema, desquamation", "burning/stinging", "Decrease with time",
                   "emollients", "Photosensitivity"]),
 ("Isotretinoin<br><span class=g>Accutane</span>",
  "<b>Retinoid dermatitis &mdash; erythema, pruritus, scaling.</b> <b>Photophobia.</b> <b>Arthralgia, headaches, "
  "alopecia, brittle nails.</b> <b>Increased serum lipids.</b>",
  "<b>Monitor for signs of developing depression</b> &mdash; the one that changes management.",
  "Skin / Multi-system", L2, 27, ["Retinoid dermatitis", "Photophobia", "Arthralgia, headaches, alopecia",
                                  "Increased serum lipids", "developing depression"]),
 ("Topical corticosteroids",
  "<b>Local: skin atrophy, acne, rosacea, allergic dermatitis</b> (the last related to the vehicle). "
  "<b>Systemic: adrenal suppression, infections, hyperglycaemia, glaucoma, cataracts, and growth retardation in "
  "children.</b>",
  "Risk scales with <b>potency, duration, area covered and occlusiveness &mdash; ointment &gt; cream &gt; "
  "lotion</b>.",
  "Skin / Endocrine / Ocular", L2, 38, ["skin atrophy, acne, rosacea", "adrenal suppression",
                                        "hyperglycemia", "glaucoma, cataracts", "growth retardation"]),
 ("Tacrolimus, pimecrolimus",
  "<b>Burning sensation.</b> <b>Possible cancer risk.</b>",
  "<b>Use a high-SPF sunscreen.</b> Avoid in immunosuppressed patients.",
  "Skin", L2, 43, ["Possible cancer risk", "burning sensation", "Use high SP"]),
 ("Topical azoles<br><span class=g>clotrimazole, miconazole, sertaconazole</span>",
  "<b>Local irritation.</b>",
  "Treatment is prolonged, <b>2 to 3 weeks</b> &mdash; the irritation has to be tolerable for that long.",
  "Skin", L2, 51, ["Adverse reactions", "local irritation", "2-3 weeks"]),
 ("Topical allylamines<br><span class=g>naftifine, terbinafine</span>",
  "<b>Local irritation</b> &mdash; the only adverse reaction the deck records for the topical form.",
  "No systemic contraindication is given for this class.",
  "Skin", L2, 53, ["Adverse reactions", "local irritation"]),
 ("Topical aciclovir, penciclovir",
  "<b>Local irritation.</b>",
  "Used for recurrent orolabial herpes simplex.",
  "Skin", L2, 56, ["Adverse reactions", "local irritation", "recurrent orolabial herpes"]),
 ("Bacitracin",
  "<b>Allergic dermatitis, rarely.</b> <b>No systemic toxicity.</b>",
  "The safest topical antibiotic on the slide &mdash; a useful contrast with neomycin.",
  "Skin", L2, 46, ["allergic dermatitis rarely", "No systemic toxicity"]),
 ("Neomycin",
  "<b>Frequently causes sensitization.</b> Can have <b>systemic accumulation</b>.",
  "This is why a patient using triple antibiotic ointment can develop a contact dermatitis over the wound.",
  "Skin", L2, 49, ["Neomycin frequently causes sensitization", "systemic accumulation"]),
 ("Polymyxin B<br><span class=g>topical</span>",
  "Allergic reactions are <b>uncommon</b>, but high doses on <b>open wounds or denuded skin</b> risk "
  "<b>neurotoxicity and nephrotoxicity</b>.",
  "The intact-skin restriction is the point.",
  "Skin / Renal", L2, 48, ["Allergic reactions uncommon", "open wounds/denuded skin",
                           "neuro/nephrotoxicity"]),
 ("Imiquimod<br><span class=g>Aldara</span>",
  "<b>Skin irritation in virtually all patients</b> &mdash; oedema, vesicles, erosions, ulcers.",
  "<b>The degree of inflammation parallels efficacy</b>, so the reaction is a sign it is working. Say so before "
  "they stop using it.",
  "Skin", L2, 57, ["skin irritation in virtually all patients", "Edema, vesicles, erosions, ulcers",
                   "parallels efficacy"]),

 # ---------------- ANS: CHOLINERGIC ----------------
 ("Bethanechol<br><span class=g>Urecholine</span>",
  "<b>Sweating, salivation, flushing, decreased blood pressure, nausea, abdominal pain, diarrhoea and "
  "bronchospasm.</b>",
  "This is the muscarinic excess pattern &mdash; it recurs for every cholinergic agonist in the lecture.",
  "Cholinergic excess", L3, 31, ["Sweating", "Salivation", "Flushing", "Decreased blood pressure",
                                 "Abdominal pain", "Bronchospasm"]),
 ("Physostigmine<br><span class=g>Antilirium</span>",
  "<b>Convulsions at high doses.</b> <b>Bradycardia and decreased cardiac output.</b> <b>Paralysis of skeletal "
  "muscle</b> from acetylcholine accumulation.",
  "The only one in the class with convulsions listed &mdash; it is the one that enters the central nervous "
  "system.",
  "Neurologic / Cardiac", L3, 37, ["Convulsions at high doses", "Bradycardia",
                                   "Decreased cardiac output", "Paralysis of skeletal muscle"]),
 ("Neostigmine, pyridostigmine",
  "<b>Salivation, flushing, decreased blood pressure, nausea, abdominal pain, diarrhoea, bronchospasm.</b>",
  "Identical profile for both agents &mdash; the deck repeats the list verbatim.",
  "Cholinergic excess", L3, 39, ["Salivation, flushing, decreased BP", "abdominal pain", "bronchospasm"]),
 ("Donepezil, rivastigmine, galantamine",
  "<b>Gastrointestinal distress.</b>",
  "The limiting side effect of the Alzheimer agents.",
  "Gastrointestinal", L3, 40, ["Slow progression of Alzheimer", "GI distress"]),
 ("Organophosphates<br><span class=g>AChE inhibitor toxicity</span>",
  "Toxicity shows as <b>nicotinic OR muscarinic signs and symptoms</b>. These agents are <b>commonly used as "
  "agricultural insecticides</b>, and also for suicidal or homicidal purposes.",
  "<b>Pralidoxime (Protopam) reactivates inhibited acetylcholinesterase</b> &mdash; but it <b>does not penetrate "
  "the central nervous system</b> and <b>cannot overcome reversible inhibitors such as physostigmine</b>.",
  "Cholinergic excess", L3, 42, ["agricultural insecticides", "nicotinic or muscarinic",
                                 "Pralidoxime", "Does not penetrate CNS"]),
 ("Atropine",
  "<b>Dry mouth, blurred vision, &ldquo;sandy eyes&rdquo;.</b> <b>Bradycardia at lower doses, tachycardia at "
  "higher doses.</b> <b>Urinary retention and constipation.</b> <b>CNS &mdash; restlessness, confusion, "
  "hallucinations, delirium.</b>",
  "The dose-dependent heart rate reversal is the trap: low dose slows, high dose speeds.",
  "Anticholinergic", L3, 52, ["Dry mouth", "Blurred vision", "Sandy eyes", "Bradycardia (lower doses)",
                              "Tachycardia (higher doses)", "Urinary retention", "hallucinations, delirium"]),
 ("Succinylcholine",
  "<b>Malignant hyperthermia</b> with halothane &mdash; muscular rigidity, metabolic acidosis, tachycardia, "
  "hyperpyrexia. <b>Apnoea</b> with plasma cholinesterase deficiency. <b>Hyperkalaemia.</b>",
  "<b>Treat malignant hyperthermia by rapid cooling and dantrolene (Dantrium)</b>, which blocks calcium release "
  "from the sarcoplasmic reticulum.",
  "Muscle / Electrolyte", L3, 70, ["Malignant Hyperthermia", "muscular rigidity, metabolic acidosis",
                                   "dantrolene", "Apnea", "Hyperkalemia"]),
 ("Atracurium",
  "<b>Releases histamine</b> &mdash; fall in blood pressure, flushing and <b>bronchoconstriction</b>.",
  "<b>Replaced by its isomer cisatracurium (Nimbex) because of fewer adverse effects.</b>",
  "Histamine", L3, 65, ["release histamine", "fall in BP", "flushing", "bronchoconstriction"]),

 # ---------------- ANS: ADRENERGIC ----------------
 ("Epinephrine",
  "<b>CNS &mdash; anxiety, fear, tension, headache, tremor.</b> <b>Cerebral haemorrhage from the rise in blood "
  "pressure.</b> <b>Cardiac arrhythmias.</b> <b>Pulmonary oedema.</b>",
  "<b>Oral is ineffective</b> &mdash; inactivated by intestinal enzymes. Rapid onset, brief duration.",
  "Cardiac / Neurologic", L3, 86, ["anxiety, fear, tension, headache, tremor", "cerebral hemorrhage",
                                   "Cardiac arrhythmias", "Pulmonary edema", "Oral ineffective"]),
 ("Catecholamines &mdash; class<br><span class=g>epinephrine, norepinephrine, isoproterenol, dopamine</span>",
  "<b>Anxiety, tremor and headache</b> &mdash; CNS-like adverse effects despite <b>poor penetration into the "
  "central nervous system</b>, because they are too polar to enter it.",
  "Rapidly inactivated by <b>COMT postsynaptically and MAO intraneuronally</b>, which is why they are infusions "
  "rather than tablets.",
  "Neurologic", L3, 79, ["Poor penetration into CNS", "Too polar", "Anxiety, tremor, headache",
                         "Monoamine oxidase"]),
 ("Norepinephrine",
  "Similar to epinephrine, plus <b>extravasation causing blanching and sloughing of the skin</b> from extreme "
  "vasoconstriction.",
  "<b>Treat extravasation with the alpha antagonist phentolamine.</b>",
  "Vascular", L3, 90, ["Similar to epinephrine", "Extravasation", "blanching and sloughing",
                       "phentolamine"]),
 ("Dopamine",
  "<b>Nausea, hypertension and arrhythmias.</b>",
  "Watch the rhythm as the rate climbs into the alpha-1 range.",
  "Cardiac / Gastrointestinal", L3, 93, ["Nausea", "Hypertension", "Arrhythmias"]),
 ("Dobutamine",
  "<b>Increases AV conduction &mdash; caution in atrial fibrillation.</b> Otherwise the same as epinephrine.",
  "<b>Tolerance may develop with prolonged use.</b>",
  "Cardiac", L3, 94, ["Increases AV conduction", "caution use in atrial fibrillation", "Tolerance"]),
 ("Albuterol",
  "<b>Tremor, restlessness, apprehension and anxiety.</b>",
  "Beta-2 effects outside the lung &mdash; expected, not a reason to stop.",
  "Neurologic", L3, 98, ["Tremor, restlessness, apprehension, anxiety"]),
 ("Clonidine<br><span class=g>Catapres</span>",
  "<b>Lethargy, sedation, constipation, xerostomia.</b> <b>Rebound hypertension with abrupt discontinuance.</b>",
  "The rebound is the one that is dangerous; the rest merely reduce adherence.",
  "Neurologic / Cardiac", L3, 97, ["Lethargy, sedation, constipation", "Rebound hypertension",
                                   "abrupt discontinuance"]),
 ("Oxymetazoline<br><span class=g>Afrin</span>",
  "<b>RHINITIS MEDICAMENTOSA &mdash; rebound congestion &mdash; if used longer than THREE DAYS.</b>",
  "The three-day limit is the entire safety message for this over-the-counter product.",
  "Nasal", L3, 95, ["Rhinitis", "rebound congestion", "longer than three days"]),
 ("Phenylephrine<br><span class=g>Neo-Synephrine</span>",
  "<b>Induces REFLEX BRADYCARDIA</b> as it raises systolic and diastolic blood pressure.",
  "A pure alpha-1 agonist, so the slowing is a baroreceptor response rather than a direct cardiac effect.",
  "Cardiovascular", L3, 96, ["Increases systolic and diastolic BP", "reflex", "bradycardia"]),
 ("Amphetamine",
  "<b>Increases blood pressure</b> (alpha-1), <b>stimulates the heart</b> (beta-1) and <b>increases central "
  "nervous system activity</b>.",
  "Acts indirectly &mdash; blocks norepinephrine uptake and releases stored catecholamines.",
  "Cardiac / Neurologic", L3, 100, ["Increases BP", "Increases stimulation of heart",
                                    "Increases CNS activity"]),
 ("Tyramine",
  "<b>May cause serious vasopressor effects if the patient is taking a monoamine oxidase inhibitor.</b>",
  "Normally oxidised by MAO in the gastrointestinal tract; on an MAOI it <b>enters the nerve terminal and "
  "displaces stored norepinephrine</b>. Found in <b>fermented foods such as cheese and wine</b>.",
  "Cardiovascular", L3, 101, ["serious vasopressor effects", "MAOI", "displaces stored norepinephrine",
                              "cheese and wine"]),
 ("Alpha-1 blockers<br><span class=g>prazosin, terazosin, doxazosin, tamsulosin, alfuzosin</span>",
  "<b>Dizziness, lack of energy, nasal congestion, headache, drowsiness</b> and <b>orthostatic hypotension</b>.",
  "Combined with <b>first-dose syncope</b>, this is why the first dose is given at bedtime.",
  "Cardiovascular", L3, 112, ["Dizziness", "Lack of energy", "Nasal congestion", "Headache",
                              "Drowsiness", "Orthostatic hypotension"]),
 ("Propranolol",
  "<b>Bronchoconstriction.</b> <b>Arrhythmias if stopped abruptly</b>, from beta receptor up-regulation. "
  "<b>Sexual impairment.</b> <b>Fasting hypoglycaemia, increased LDL cholesterol, increased triglycerides.</b>",
  "The metabolic disturbances are easy to forget and easy to ask about.",
  "Respiratory / Cardiac / Metabolic", L3, 117, ["Bronchoconstriction", "Arrhythmias if stopped abruptly",
                                                 "up-regulation", "Sexual impairment",
                                                 "Fasting hypoglycemia", "increased LDL"]),
 ("Propranolol<br><span class=g>central effects</span>",
  "<b>Depression, dizziness, lethargy, fatigue, weakness, visual disturbances, hallucinations, short-term memory "
  "loss, emotional lability, vivid dreams including nightmares</b>, and decreased performance.",
  "<b>Cimetidine, fluoxetine, paroxetine and ritonavir inhibit its metabolism</b>; <b>barbiturates, phenytoin "
  "and rifampin induce it</b>.",
  "Neurologic / Psychiatric", L3, 118, ["Depression, dizziness, lethargy", "hallucinations",
                                        "short-term memory loss", "vivid dreams", "Cimetidine",
                                        "rifampin induce metabolism"]),
 ("Labetalol, carvedilol",
  "<b>Orthostatic hypotension due to alpha-1 blockade.</b>",
  "Both produce peripheral vasodilation, which is where the postural drop comes from.",
  "Cardiovascular", L3, 122, ["orthostatic hypotension", "blockade"]),
 ("Nicotine",
  "Increases blood pressure, heart rate, peristalsis and secretions; <b>at higher doses blood pressure falls</b> "
  "from ganglionic blockade and <b>GI and bladder activity ceases</b>.",
  "Biphasic &mdash; stimulation first, then paralysis of all ganglia.",
  "Autonomic", L3, 59, ["increased BP, HR, peristalsis", "BP falls", "ganglionic blockade", "ceases"]),
]
