# -*- coding: utf-8 -*-
"""Contraindication data for Pharmacology I Exam 1, with per-row provenance.

Every row carries (deck, slide, verify) so build_pharm_contraindications.py can
check the claim against the slide it cites before the page is written. `verify`
lists substrings that MUST appear in that slide's own text -- if a row drifts
from the deck, the build fails rather than shipping.

TIERS, and the distinction matters because the decks are uneven:
  ABS   the deck literally says "contraindicated"
  AVOID the deck says avoid / do not use / cannot use
  BBW   the deck says black box warning
  NAMED a named reaction or syndrome -- rendered bold + underlined
  CAUT  a caution the deck states, NOT worded as a contraindication
Nothing is promoted a tier above what the slide actually says.
"""

L1 = "Antibiotics, Antivirals, and Antifungals"
L2 = "02. Dermatology Medications"
L3 = "03. ANS Pharmacology"

# (drug or class, what, tier, deck, slide, [verify substrings])
ROWS = [
 # ---------------- BETA-LACTAMS ----------------
 ("Aminopenicillins<br><span class=g>amoxicillin, ampicillin</span>",
  "<b>Contraindicated</b> in patients <b>allergic to penicillin</b>, and in a patient with a past history of "
  "<b>cholestatic jaundice or hepatic dysfunction</b>.",
  "ABS", L1, 21, ["Contraindications", "allergic to penicillin", "cholestatic jaundice"]),
 ("Aminopenicillins<br><span class=g>amoxicillin, ampicillin</span>",
  "Reduces the effectiveness of <b>oral contraceptives</b> &mdash; use backup birth control. Prolongs prothrombin "
  "time with anticoagulants.",
  "CAUT", L1, 20, ["oral contraceptives", "backup birth control", "prothrombin time"]),
 ("Penicillins &mdash; class",
  "Adverse reactions are <b>hypersensitivity reaction</b>, rash and diarrhoea. Dosing is adjusted for "
  "<b>renal function</b>. Monitor renal and hepatic function and platelets.",
  "CAUT", L1, 22, ["Hypersensitivity", "Renal Function", "Platelets"]),
 ("Cephalosporins &mdash; class",
  "<b>Penicillin cross-sensitivity of approximately less than 1%</b> &mdash; the number to know when a stem "
  "gives you a penicillin-allergic patient.",
  "CAUT", L1, 30, ["Penicillin cross-sensitivity", "1%"]),
 ("Ceftriaxone<br><span class=g>Rocephin</span>",
  "<b>Cannot be used during the first 30 days of life.</b> Cefotaxime is preferred in neonatal fever or sepsis. "
  "No dosage adjustment is needed in renal insufficiency.",
  "AVOID", L1, 34, ["Can’t use during first 30 days of life", "Cefotaxime", "neonatal"]),
 ("Carbapenems<br><span class=g>imipenem, meropenem, ertapenem, doripenem</span>",
  "Monitor renal and hepatic function, full blood count for bleeding, signs of anaphylaxis &mdash; and "
  "<u><b>SEIZURES, specifically with imipenem</b></u>. That pairing is the one carbapenem fact most likely to be "
  "asked.",
  "NAMED", L1, 44, ["Monitoring", "Renal", "hepatic function", "Seizures", "Imipenem"]),
 ("Echinocandins<br><span class=g>caspofungin, micafungin, anidulafungin</span>",
  "Adverse reactions: <b>tachycardia, headache, insomnia, hypokalaemia, hypomagnesaemia and blood dyscrasias</b>.",
  "CAUT", L1, 109, ["Tachycardia", "headache", "insomnia", "hypokalemia", "hypomagnesemia", "blood dyscrasias"]),
 ("Allylamines<br><span class=g>naftifine, terbinafine (Lamisil)</span>",
  "The deck records only <b>local irritation</b> &mdash; no systemic contraindication is given for this class.",
  "CAUT", L2, 53, ["Adverse reactions", "local irritation"]),
 ("Aztreonam<br><span class=g>monobactam</span>",
  "The exception worth memorising: <b>NO cross-reactivity with beta-lactams</b>, so it <b>can be used in truly "
  "penicillin-allergic patients</b>.",
  "EXCEPT", L1, 41, ["NO cross-reactivity", "true PCN allergic"]),

 # ---------------- VANCOMYCIN ----------------
 ("Vancomycin",
  "Infusion-related reaction &mdash; <u><b>&ldquo;Red Man Syndrome&rdquo;</b></u>, with fever, chills and phlebitis. "
  "The deck also titles a slide <u><b>&ldquo;Vancomycin Infusion Syndrome&rdquo;</b></u>. It is an "
  "<b>infusion-rate</b> problem, which is why the drug is infused over 60 minutes.",
  "NAMED", L1, 51, ["Red Man Syndrome", "Infusion related reactions", "Fever/chills", "Phlebitis"]),
 ("Vancomycin",
  "Monitor for <b>ototoxicity and nephrotoxicity</b>, and follow renal clearance. Requires therapeutic drug "
  "monitoring &mdash; trough drawn <b>15&ndash;30 minutes before the next dose</b>, around the 3rd or 4th dose.",
  "CAUT", L1, 51, ["Ototoxicity", "Nephrotoxicity", "Trough"]),

 # ---------------- MACROLIDES ----------------
 ("Macrolides<br><span class=g>erythromycin, clarithromycin, azithromycin</span>",
  "<u><b>QT prolongation and Torsades de pointes</b></u> &mdash; worse in combination with <b>class Ia and III "
  "antiarrhythmics</b> and with electrolyte abnormalities.",
  "NAMED", L1, 57, ["QT prolongation", "Torsades de pointes", "Class Ia"]),
 ("Macrolides<br><span class=g>erythromycin, clarithromycin, azithromycin</span>",
  "<b>Cholestatic hepatitis</b> (rare, more with the estolate salt) and <b>transient hearing loss</b> with large "
  "intravenous doses or in renal insufficiency.",
  "CAUT", L1, 57, ["Cholestatic hepatitis", "estolate", "Transient hearing loss"]),
 ("Macrolides<br><span class=g>erythromycin, clarithromycin, azithromycin</span>",
  "<b>CYP3A4 interaction</b> raises levels of carbamazepine, cyclosporine, digoxin, midazolam and theophylline. "
  "Erythromycin &gt; clarithromycin &gt; azithromycin. <b>Check the drug profile before prescribing.</b>",
  "CAUT", L1, 59, ["CYP3A", "carbamazepine", "cyclosporine", "digoxin"]),

 # ---------------- TETRACYCLINES ----------------
 ("Tetracyclines<br><span class=g>tetracycline, doxycycline, minocycline</span>",
  "<b>Avoid under 8 years old</b> &mdash; causes <b>discoloration of teeth</b> (doxycycline more than the others) "
  "and <b>depression of skeletal growth</b>.",
  "AVOID", L1, 63, ["Avoid", "8 years old", "Discoloration of teeth", "skeletal growth"]),
 ("Tetracyclines<br><span class=g>tetracycline, doxycycline, minocycline</span>",
  "<b>Avoid in the 2nd and 3rd trimester of pregnancy.</b> Also <b>photosensitivity</b>, and they <b>chelate with "
  "cations</b> &mdash; iron, calcium and dairy block absorption.",
  "AVOID", L1, 63, ["Avoid in 2", "Trimester of Pregnancy", "Photosensitivity", "Chelate with cations"]),
 ("Tetracyclines &mdash; for acne<br><span class=g>Lecture 2 restates it harder</span>",
  "<b>Contraindicated in children under 8 years and in pregnant women.</b> Lecture 2 words this as an outright "
  "contraindication where Lecture 1 says &ldquo;avoid&rdquo;.",
  "ABS", L2, 28, ["Contraindicated in children", "8 years", "pregnant women"]),

 # ---------------- FLUOROQUINOLONES ----------------
 ("Fluoroquinolones<br><span class=g>ciprofloxacin, levofloxacin, moxifloxacin</span>",
  "<u><b>Tendonitis and Achilles tendon rupture.</b></u> <b>Caution if under 18 years old.</b> Also peripheral "
  "neuropathy and central nervous system toxicity &mdash; dizziness, insomnia, somnolence.",
  "NAMED", L1, 79, ["Tendonitis/Tendon", "achilles", "rupture", "18"]),
 ("Fluoroquinolones<br><span class=g>ciprofloxacin, levofloxacin, moxifloxacin</span>",
  "<u><b>QT prolongation and Torsades de Pointes.</b></u> Photosensitivity, and they <b>complex with cations</b> "
  "&mdash; iron, antacids, multivitamins, calcium and dairy.",
  "NAMED", L1, 79, ["QT prolongation", "Torsades de Pointes", "Complexes with cations", "Photosensitivity"]),
 ("Moxifloxacin<br><span class=g>Avelox</span>",
  "<b>Do not use for urinary tract infections</b> &mdash; the one fluoroquinolone that does not cover them. It "
  "also has <b>no pseudomonas coverage</b>.",
  "AVOID", L1, 78, ["Do not use for urinary tract infections", "Pseudomonas"]),

 # ---------------- OTHER ANTIBACTERIALS ----------------
 ("Clindamycin<br><span class=g>Cleocin</span>",
  "<b>Clostridium difficile</b> and <b>pseudomembranous colitis</b> &mdash; the reaction this drug is known for. "
  "Also rash, neutropenia and thrombocytopenia.",
  "CAUT", L1, 81, ["Clostridium difficile", "Pseudomembranous colitis", "Neutropenia"]),
 ("Trimethoprim / sulfamethoxazole<br><span class=g>Septra, Bactrim</span>",
  "<u><b>Stevens-Johnson syndrome and toxic epidermal necrolysis.</b></u> Blood dyscrasias &mdash; "
  "thrombocytopenia, agranulocytosis, megaloblastic anaemia. Hepatotoxicity and hyperbilirubinaemia.",
  "NAMED", L1, 85, ["SJS", "TEN", "agranulocytosis", "megaloblastic anemia"]),
 ("Trimethoprim / sulfamethoxazole<br><span class=g>Septra, Bactrim</span>",
  "Raises phenytoin, rifampin and digoxin levels; causes <b>hypoglycaemia with sulfonylureas</b>; and "
  "<b>significantly increases INR (international normalised ratio) with warfarin</b> by inhibiting CYP2C9.",
  "CAUT", L1, 85, ["phenytoin", "Hypoglycemia with sulfonylureas", "INR", "warfarin"]),
 ("Metronidazole<br><span class=g>Flagyl</span>",
  "<u><b>Disulfiram-like reaction with ethanol.</b></u> The single most testable fact about this drug &mdash; "
  "counsel the patient not to drink.",
  "NAMED", L1, 86, ["Disulfiram-like reaction with ethanol"]),
 ("Linezolid<br><span class=g>Zyvox</span>",
  "<u><b>Serotonin syndrome</b></u> with <b>SSRIs, tyramine-containing foods and pseudoephedrine</b>. Also "
  "<b>thrombocytopenia</b>.",
  "NAMED", L1, 71, ["Serotonin Syndrome", "SSRI", "tyramine", "pseudoephedrine", "Thrombocytopenia"]),
 ("Polymyxin B and Polymyxin E<br><span class=g>colistin</span>",
  "<b>BLACK BOX WARNINGS</b> for <b>nephrotoxicity, neurotoxicity and neuromuscular blockade</b>.",
  "BBW", L1, 88, ["Black box warnings", "nephrotoxicity", "neurotoxicity", "neuromuscular blockade"]),
 ("Aminoglycosides<br><span class=g>gentamicin, tobramycin, amikacin</span>",
  "<b>Renal toxicity and ototoxicity</b> &mdash; renally adjusted, and they require therapeutic drug monitoring "
  "with peak and trough levels.",
  "CAUT", L1, 68, ["Renal toxicity", "Ototoxic", "Renally adjusted"]),

 # ---------------- ANTIFUNGALS ----------------
 ("Amphotericin B",
  "<b>Fever and chills</b> from interleukin-1 and tumour necrosis factor &mdash; <b>pre-treat with paracetamol, "
  "antihistamines and corticosteroids</b>. Infused over 4 hours; <b>side effects limit treatment</b>.",
  "CAUT", L1, 98, ["Fever/chills", "IL-1", "TNF", "Pretreat"]),
 ("Amphotericin B",
  "<b>Electrolyte abnormalities &mdash; hypokalaemia and hypomagnesaemia</b>, hypotension, uraemia in 80% with "
  "decreased filtration, and <b>renal tubule damage &mdash; hydrate with normal saline</b>.",
  "CAUT", L1, 99, ["hypokalemia", "hypomagnesemia", "Renal tubule damage", "normal saline"]),
 ("Itraconazole<br><span class=g>Sporanox</span>",
  "<b>Teratogenic.</b> Substrate for and inhibitor of <b>CYP3A4</b>.",
  "AVOID", L1, 104, ["Teratogenic", "CYP3A4"]),
 ("Fluconazole<br><span class=g>Diflucan</span>",
  "<b>Teratogenic in animals.</b> Inhibits CYP3A4 and CYP2A4.",
  "AVOID", L1, 106, ["teratogenic in animals", "Inhibits CYP3A4"]),
 ("Voriconazole<br><span class=g>Vfend</span>",
  "<b>Teratogenic in animals.</b> <b>Visual effects in 30%</b>, plus liver and renal effects. The intravenous "
  "vehicle <b>cyclodextrin accumulates in renal failure</b>.",
  "AVOID", L1, 107, ["teratogenic in animals", "vision", "cyclodextrin", "renal failure"]),
 ("Posaconazole<br><span class=g>Noxafil</span>",
  "<b>QT prolongation</b>, fever, diarrhoea, hypokalaemia, hypomagnesaemia and thrombocytopenia.",
  "CAUT", L1, 105, ["QT prolongation", "Hypokalemia", "thrombocytopenia"]),
 ("Ketoconazole",
  "<b>Inhibits CYP3A4 &mdash; significant drug interactions.</b> Does not enter the central nervous system, and "
  "is now rarely used.",
  "CAUT", L1, 103, ["Inhibits CYP3A4", "significant drug interactions"]),
 ("Flucytosine<br><span class=g>5-flucytosine, Ancobon</span>",
  "<b>Bone marrow suppression</b> and <b>hepatotoxicity</b>.",
  "CAUT", L1, 101, ["Bone marrow suppression", "Hepatotoxicity"]),
 ("Griseofulvin",
  "<b>Induces CYP1A2 and CYP2C9.</b> Headache in 15%, mental confusion, fatigue and blurred vision. Absorption "
  "increases with a <b>high-fat meal</b>.",
  "CAUT", L1, 111, ["Induces microsomal enzymes", "1A2", "Headache", "high-fat meal"]),

 # ---------------- ANTIVIRALS / ANTHELMINTHICS ----------------
 ("Acyclovir, valacyclovir<br><span class=g>Zovirax, Valtrex</span>",
  "<b>Crystallizes in the renal tubule &mdash; maintain hydration and renal function.</b> Central nervous system "
  "effects include seizures, delirium and tremor; also bone marrow suppression.",
  "CAUT", L1, 123, ["crystallizes in renal tubule", "maintain hydration", "seizures", "delirium"]),
 ("Ganciclovir, valganciclovir<br><span class=g>Cytovene, Valcyte</span>",
  "<b>Neutropenia in 15&ndash;40%</b> and thrombocytopenia. <b>33% of patients must stop intravenous treatment "
  "because of side effects.</b>",
  "CAUT", L1, 125, ["neutropenia", "thrombocytopenia", "33%", "stop intravenous treatment"]),
 ("Oseltamivir<br><span class=g>Tamiflu</span>",
  "<b>Requires renal dose adjustment.</b> Oral only.",
  "CAUT", L1, 127, ["Requires renal dose adjustment"]),
 ("Albendazole, mebendazole<br><span class=g>Albenza, Emverm</span>",
  "Very well tolerated, but rash including <u><b>Stevens-Johnson syndrome and toxic epidermal necrolysis</b></u> "
  "is described.",
  "NAMED", L1, 115, ["SJS", "TEN", "hypersensitivity"]),

 # ---------------- DERMATOLOGY ----------------
 ("Isotretinoin<br><span class=g>Accutane</span>",
  "<b>CONTRAINDICATED in pregnancy and breastfeeding &mdash; men should avoid as well.</b> Enrolment in "
  "<u><b>iPledge</b></u> is required. <b>Monitor for signs of developing depression</b> and for raised serum lipids.",
  "ABS", L2, 27, ["CONTRAINDICATED in pregnancy", "breastfeeding", "Men should avoid", "iPledge", "depression"]),
 ("Topical retinoids<br><span class=g>tretinoin, adapalene, tazarotene</span>",
  "<b>Avoid during pregnancy.</b> <b>Photosensitivity and severe sunburn.</b> <b>Benzoyl peroxide inactivates "
  "tretinoin</b>, and tretinoin is photolabile so it is applied nightly.",
  "AVOID", L2, 24, ["Avoid during pregnancy", "Photosensitivity", "severe sunburn",
                    "Benzoyl peroxide inactivates tretinoin"]),
 ("Topical corticosteroids",
  "Local: <b>skin atrophy, acne, rosacea, allergic dermatitis</b>. Systemic: <b>adrenal suppression, infections, "
  "hyperglycaemia, glaucoma, cataracts, and growth retardation in children</b>. Risk rises with potency, duration, "
  "area covered and occlusiveness &mdash; <b>ointment &gt; cream &gt; lotion</b>.",
  "CAUT", L2, 38, ["skin atrophy", "adrenal suppression", "glaucoma", "cataracts",
                   "growth retardation", "ointment"]),
 ("Topical immunomodulators<br><span class=g>tacrolimus (Protopic), pimecrolimus (Elidel)</span>",
  "<b>Possible cancer risk.</b> <b>Avoid in patients with weakened immune systems.</b> Second line after topical "
  "steroids; use a high-SPF (sun protection factor) sunscreen.",
  "AVOID", L2, 43, ["Possible cancer risk", "Avoid in patients", "weakened immune systems", "SPF"]),
 ("Polymyxin B<br><span class=g>topical</span>",
  "<b>Avoid using on open wounds or denuded skin in high doses</b> &mdash; risk of <b>neurotoxicity and "
  "nephrotoxicity</b>.",
  "AVOID", L2, 48, ["Avoid using on open wounds", "denuded skin", "neuro/nephrotoxicity"]),
 ("Neomycin<br><span class=g>topical aminoglycoside</span>",
  "<b>Frequently causes sensitization</b>, and topical aminoglycosides <b>can accumulate systemically</b>.",
  "CAUT", L2, 49, ["Neomycin frequently causes sensitization", "systemic accumulation"]),
 ("Benzoyl peroxide",
  "<b>Can bleach hair, clothes</b>, and irritates skin and mucous membranes. Start at 2.5% once daily.",
  "CAUT", L2, 21, ["bleach hair", "clothes", "irritation"]),
 ("Intralesional and oral corticosteroids<br><span class=g>acne</span>",
  "Systemic absorption can occur &rarr; <b>adrenal suppression</b> and <b>local tissue atrophy</b>. Oral courses "
  "need <b>tapering to prevent flare-up</b>.",
  "CAUT", L2, 30, ["Systemic absorption", "adrenal suppression", "Local tissue atrophy"]),

 # ---------------- ANS: CHOLINERGIC ----------------
 ("Cholinergic agonists &mdash; class<br><span class=g>bethanechol, carbachol, pilocarpine</span>",
  "Muscarinic excess causes <b>bronchospasm</b>, decreased blood pressure, salivation, sweating, flushing, nausea, "
  "abdominal pain and diarrhoea &mdash; which is why these are a problem in <b>reactive airway disease</b>.",
  "CAUT", L3, 31, ["Bronchospasm", "Decreased blood pressure", "Salivation", "Diarrhea"]),
 ("Acetylcholinesterase inhibitors<br><span class=g>neostigmine, pyridostigmine</span>",
  "Same muscarinic burden &mdash; <b>salivation, flushing, decreased blood pressure, nausea, abdominal pain, "
  "diarrhoea and bronchospasm</b>.",
  "CAUT", L3, 38, ["Salivation", "flushing", "decreased BP", "bronchospasm"]),
 ("Physostigmine<br><span class=g>Antilirium</span>",
  "<b>Convulsions at high doses</b>, bradycardia, decreased cardiac output, and <b>paralysis of skeletal muscle</b> "
  "from acetylcholine accumulation.",
  "CAUT", L3, 37, ["Convulsions at high doses", "Bradycardia", "Paralysis of skeletal muscle"]),
 ("Organophosphate poisoning<br><span class=g>irreversible AChE inhibitors</span>",
  "<b>Pralidoxime (Protopam) reactivates inhibited acetylcholinesterase</b> &mdash; but it <b>does not penetrate "
  "the central nervous system</b> and <b>cannot overcome reversible inhibitors such as physostigmine</b>.",
  "CAUT", L3, 42, ["Pralidoxime", "reactivate", "Does not penetrate CNS", "Cannot overcome reversible"]),
 ("Atropine and antimuscarinics",
  "The <u><b>anticholinergic toxidrome</b></u>: <b>mad as a hatter</b> (sedation, anxiety, hallucinations, "
  "seizures), <b>blind as a bat</b> (mydriasis, blurry vision), <b>red as a beet</b> (flushing), <b>dry as a "
  "bone</b> (decreased secretions), <b>hot as Hades</b> (hyperthermia), plus constipation, urinary retention and "
  "tachycardia.",
  "NAMED", L3, 50, ["Mad as a hatter", "Blind as a bat", "Red as a beet", "Dry as a bone", "Hot as Hades"]),
 ("Atropine",
  "Adverse effects: <b>dry mouth, blurred vision, &ldquo;sandy eyes&rdquo;, urinary retention, constipation</b>, "
  "and central effects &mdash; <b>restlessness, confusion, hallucinations, delirium</b>. Dose-dependent heart rate: "
  "<b>bradycardia at lower doses, tachycardia at higher doses</b>.",
  "CAUT", L3, 52, ["Dry mouth", "Blurred vision", "Sandy eyes", "Urinary retention",
                   "Bradycardia (lower doses)", "Tachycardia (higher doses)"]),
 ("Scopolamine<br><span class=g>Transderm Scop patch</span>",
  "<b>Wash hands thoroughly after placing the patch</b> &mdash; touching the eye afterwards causes blurred vision. "
  "Effects otherwise similar to atropine.",
  "CAUT", L3, 54, ["wash hands thoroughly", "blurred vision", "patch"]),
 ("Succinylcholine",
  "<u><b>Malignant hyperthermia</b></u> with halothane in genetically susceptible people &mdash; muscular rigidity, "
  "metabolic acidosis, tachycardia and hyperpyrexia. <b>Treat by rapid cooling and dantrolene (Dantrium)</b>.",
  "NAMED", L3, 70, ["Malignant Hyperthermia", "halothane", "dantrolene", "rigidity"]),
 ("Succinylcholine",
  "<b>Hyperkalaemia</b>, and <b>prolonged paralysis (apnoea)</b> in patients <b>genetically deficient in plasma "
  "cholinesterase</b> or with electrolyte imbalance.",
  "CAUT", L3, 70, ["Apnea", "genetically deficient in plasma cholinesterase", "Hyperkalemia"]),
 ("Atracurium<br><span class=g>nondepolarizing blocker</span>",
  "<b>Releases histamine</b> &mdash; can produce a fall in blood pressure, flushing and <b>bronchoconstriction</b>.",
  "CAUT", L3, 65, ["release histamine", "fall in BP", "bronchoconstriction"]),

 # ---------------- ANS: ADRENERGIC ----------------
 ("Epinephrine",
  "<b>Hyperthyroidism</b> &mdash; enhanced cardiovascular actions. <b>Cocaine</b> &mdash; exaggerated "
  "cardiovascular actions because reuptake is prevented. <b>Diabetes</b> &mdash; increases release of endogenous "
  "glucose stores.",
  "CAUT", L3, 87, ["Hyperthyroidism", "Cocaine", "exaggerated cardiovascular", "Diabetes"]),
 ("Epinephrine",
  "Adverse effects: anxiety, fear, tension, headache, tremor; <b>cerebral haemorrhage from the rise in blood "
  "pressure</b>; <b>cardiac arrhythmias</b>; and pulmonary oedema.",
  "CAUT", L3, 86, ["cerebral hemorrhage", "Cardiac arrhythmias", "Pulmonary edema"]),
 ("Norepinephrine",
  "<b>Extravasation causes blanching and sloughing of skin</b> from extreme vasoconstriction &mdash; "
  "<b>treated with the alpha antagonist phentolamine</b>.",
  "CAUT", L3, 90, ["Extravasation", "blanching and sloughing", "phentolamine"]),
 ("Dobutamine",
  "<b>Increases atrioventricular conduction &mdash; caution in atrial fibrillation.</b> Tolerance may develop with "
  "prolonged use.",
  "CAUT", L3, 94, ["Increases AV conduction", "caution use in atrial fibrillation", "Tolerance"]),
 ("Clonidine<br><span class=g>Catapres</span>",
  "<u><b>Rebound hypertension with abrupt discontinuance.</b></u> Also lethargy, sedation, constipation and "
  "xerostomia.",
  "NAMED", L3, 97, ["Rebound hypertension with abrupt discontinuance", "sedation"]),
 ("Alpha-1 blockers<br><span class=g>prazosin, terazosin, doxazosin, tamsulosin, alfuzosin</span>",
  "<u><b>&ldquo;First-dose&rdquo; syncope.</b></u> Also dizziness, lack of energy, nasal congestion, headache, "
  "drowsiness and <b>orthostatic hypotension</b>.",
  "NAMED", L3, 111, ["first-dose", "syncope"]),
 ("Phenoxybenzamine",
  "<u><b>Epinephrine reversal</b></u> &mdash; it blocks the alpha vasoconstriction of epinephrine but not its beta "
  "vasodilation, so blood pressure falls. Block is <b>irreversible</b>; the body must synthesise new receptors, "
  "taking <b>at least 24 hours</b>.",
  "NAMED", L3, 109, ["Epinephrine reversal", "Blocks vasoconstriction", "but not vasodilation"]),
 ("Propranolol<br><span class=g>non-selective beta blocker</span>",
  "<b>CONTRAINDICATED in patients with chronic obstructive pulmonary disease or asthma</b> &mdash; beta-2 "
  "blockade causes <b>bronchoconstriction</b>. This is the deck's clearest contraindication in Lecture 3.",
  "ABS", L3, 115, ["Contraindicated in patients with chronic obstructive pulmonary disease",
                   "Bronchoconstriction"]),
 ("Propranolol<br><span class=g>non-selective beta blocker</span>",
  "<b>Attenuates the normal physiologic response to hypoglycaemia</b> and causes <b>fasting hypoglycaemia</b> "
  "&mdash; the reason for care in diabetics. Decreases glycogenolysis and glucagon secretion; raises LDL "
  "cholesterol and triglycerides.",
  "CAUT", L3, 115, ["Attenuate normal physiologic response to hypoglycemia", "glycogenolysis", "glucagon"]),
 ("Propranolol<br><span class=g>non-selective beta blocker</span>",
  "<u><b>Arrhythmias if stopped abruptly</b></u>, from up-regulation of beta receptors &mdash; never stop a beta "
  "blocker suddenly. Also central effects: depression, hallucinations, vivid dreams and nightmares.",
  "NAMED", L3, 117, ["Arrhythmias if stopped abruptly", "up-regulation", "Sexual impairment"]),
 ("Selective beta-1 antagonists<br><span class=g>atenolol, metoprolol, bisoprolol, esmolol</span>",
  "<b>Cardioselectivity is LOST at higher doses</b> &mdash; which is why &ldquo;cardioselective&rdquo; is not a "
  "free pass in a patient with airway disease. Useful for hypertension in <b>impaired pulmonary function</b>.",
  "CAUT", L3, 120, ["Cardioselectivity", "lost at higher doses", "impaired pulmonary function"]),
 ("Labetalol and carvedilol",
  "<b>May cause orthostatic hypotension due to alpha-1 blockade.</b>",
  "CAUT", L3, 122, ["orthostatic hypotension", "blockade"]),
 ("Nicotine",
  "Depolarizes autonomic ganglia &mdash; <b>stimulation first, then paralysis of all ganglia</b>. At higher doses "
  "<b>blood pressure falls</b> and gastrointestinal and bladder activity <b>ceases</b>.",
  "CAUT", L3, 59, ["stimulation, then paralysis", "BP falls", "ceases"]),
]
