# -*- coding: utf-8 -*-
"""Cram-sheet topics for Pharmacology I Exam 3, Lecture 11 (Drugs for Pulmonary Infections, Asthma and COPD;
added 2026-10-27).

Imported by build_pharm_e3_cram.py, which verifies this module's REG against the Lecture 11 deck
(Pulmonology-2.pptx). Same rules as Lectures 9 and 10: SLIDES WIN on conflict (only what is visible on a slide; this
deck has no speaker notes; picture-slide text read by eye is in tools/pharm_e3/ocr.json). Where a slide differs from
current guidelines or contradicts itself, a row in the closing topic says so and nothing there is asked. No milligram
doses, fluid volumes or epinephrine concentrations. Stars mark what Dr. Wood emphasized in the 2026-10-26 recording
(Whisper transcript only; no caption track exists); a star only sets weight.

VERIFICATION. Each row is R(label, html, slide(s), verify[, quotes]); every `verify` substring must appear on the
cited slide (pharm_e3_lib.slide_text("L11", n)) and every `quotes` substring in the Lecture 11 transcript.
"""
REG = []   # (label, [(slide, [verify])], [quotes])


def R(label, html, slide=None, verify=(), quotes=()):
    if slide is None:
        pairs = []
    elif isinstance(slide, int):
        pairs = [(slide, list(verify))]
    else:
        pairs = [(s, list(v)) for s, v in slide]
    REG.append((label, pairs, list(quotes)))
    return [label, html]


T = []


def topic(tid, label, color, rows):
    T.append({"id": tid, "label": label, "color": color, "rows": rows})



# ----------------------------------------------------------------------------------------------
topic("pu-cap", "Pulmonary &middot; acute bronchitis and community-acquired pneumonia", "#2f4f6b", [
 R("Acute bronchitis: what it is",
   "Inflammation of one or more <b>bronchi</b>, usually infectious; <b>spares the bronchioles and alveoli</b>. Acute: all ages. Chronic: mainly patients with chronic obstructive pulmonary disease. "
   "<b>Mostly viral</b> (rhinovirus, coronavirus, influenza, adenovirus); occasionally <i>Mycoplasma</i>, <i>Chlamydia pneumoniae</i>, <i>Bordetella pertussis</i>.",
   [(5, ["Inflammation of one or more bronchi", "involve bronchioles and alveoli", "Chronic", "primarily affects COPD patients"]),
    (6, ["Common causes", "viruses", "Rhinovirus, coronavirus, influenza, adenovirus", "Mycoplasma pneumoniae, Chlamydia pneumoniae, Bordatella pertussis"])]),
 R("Acute bronchitis: treatment",
   "<b>Self-limited: supportive care</b> (analgesics, antipyretics, antitussives, fluids). <b>Possibly avoid antihistamines and sympathomimetics</b>: they dehydrate secretions and may prolong symptoms. "
   "<b>No routine antibiotics.</b> Symptoms over 5 days: think bacterial; <b>doxycycline preferred if <i>Mycoplasma</i> is documented</b> (macrolide resistance); macrolides; a respiratory fluoroquinolone only after recent antibiotic exposure.",
   [(7, ["Generally self-limited", "Analgesics, antipyretics, antitussives, fluids", "Possibly avoid antihistamines/sympathomimetics", "Dehydrate bronchial secretions, may prolong symptoms"]),
    (8, ["Routine ABX not recommended", "Persistent symptoms > 5 days, consider bacterial involvement", "Preferred if mycoplasma documented due to macrolide resistance", "avoid unless recent antibiotic exposure"])]),
 R("Community-acquired pneumonia: route and diagnosis",
   "Microbes arrive by <b>aspiration from the oropharynx (elderly)</b>, inhaled aerosols, the bloodstream or direct spread (trauma). "
   "<b>Outpatients: empiric antibiotics, no routine tests.</b> <b>Hospitalized: blood and sputum cultures before antibiotics.</b> Sputum Gram stain is controversial (contaminated; pathogen often not found).",
   [(10, ["Aspiration from oropharynx", "Common in elderly", "Inhalation of infectious aerosols", "Hematogenous dissemination"]),
    (11, ["Patients do well with empiric ABX", "Diagnostic tests not routinely performed", "Blood and sputum cultures for hospitalized patients", "Prior to ABX!", "Controversial"])]),
 R("Pathogens by setting",
   "<b>Outpatient:</b> <i>S. pneumoniae</i>, <i>Mycoplasma</i>, <i>H. influenzae</i>, <i>Moraxella</i>, viruses. <b>Ward:</b> adds <i>Chlamydia pneumoniae</i>, <i>Legionella</i>, aspiration. "
   "<b>Intensive care unit:</b> <i>S. pneumoniae</i>, <b><i>Staphylococcus aureus</i></b>, <i>Legionella</i>, <b>gram-negative bacilli</b>, <i>H. influenzae</i>.",
   12, ["Streptococcus pneumoniae, Mycoplasma pneumoniae, Haemophilus influenzae, Moraxella catarrhalis, respiratory viruses", "Legionella species, Aspiration", "Inpatient (ICU)", "Staphylococcus aureus, Legionella spp., Gram-negative bacilli"]),
 R("Risk for resistant pneumococcus",
   "<b>Age over 65</b>; <b>a beta-lactam in the past 3 months</b>; alcoholism; immunosuppression; comorbidities (diabetes, renal insufficiency, heart failure, coronary disease, malignancy); <b>a child in day care</b>.",
   13, ["Penicillin-resistant S. pneumoniae", "Age > 65 years", "Beta-lactam within past 3 months", "Alcoholism", "Immunosuppressed", "Exposure to a child in a day care center"]),
 R("Outpatient regimen",
   "<b>No resistance risk: macrolide first line</b> (azithromycin, clarithromycin); doxycycline or minocycline second line. "
   "<b>Resistance risk: beta-lactam + macrolide</b> (amoxicillin with or without clavulanic acid; cefuroxime, cefpodoxime) <b>or a respiratory fluoroquinolone</b> (levofloxacin, moxifloxacin), <b>good for beta-lactam allergy</b>.",
   14, ["No risk of resistant S. pneumoniae", "1st line: macrolide", "azithromycin, clarithromycin", "2nd line: doxycycline, minocycline", "Beta lactam + macrolide", "Amoxicillin +/- clavulanic acid", "Cefuroxime, cefpodoxime", "levofloxacin, moxifloxacin", "Good for patients with beta-lactam allergy"]),
 R("Inpatient regimen",
   "<b>Ward:</b> intravenous beta-lactam (cefotaxime, ceftriaxone, high-dose ampicillin) <b>plus a macrolide</b>, or doxycycline, or a respiratory fluoroquinolone (beta-lactam allergy). "
   "<b>Intensive care unit:</b> the same, <b>all intravenous</b>; consider methicillin-resistant <i>S. aureus</i> coverage.",
   15, ["Intravenous beta-lactam", "Cefotaxime, ceftriaxone, high-dose ampicillin PLUS intravenous/oral macrolide", "or respiratory fluoroquinolone (beta-lactam allergy)", "Same as above, but begin all IV treatment", "Consider MRSA coverage if warranted"]),
])

# ----------------------------------------------------------------------------------------------
topic("pu-hap", "Pulmonary &middot; nosocomial pneumonia", "#4a4f8c", [
 R("Definition",
   "Lung infection <b>not present on admission, starting more than 48 hours after</b>. Hospital-acquired, ventilator-associated and health-care associated. <b>Second most common hospital infection, after urinary tract infection.</b> Worse in the elderly and ventilated.",
   16, ["Infection of lung not present at time of admission", "Occurring >48 hours after hospital admission", "Second most common infection in hospitalized patients (after UTI)", "Higher incidence in elderly and mechanically ventilated patients"]),
 R("Health-care associated criteria",
   "Hospitalized <b>more than 2 days in the past 90 days</b>; nursing home or long-term care; recent intravenous antibiotics; chemotherapy; <b>wound care in the past 30 days</b>; hemodialysis.",
   17, ["Hospitalized in acute care facility > 2 days in past 90 days", "Nursing home/long term care facility", "Recent IV antibiotics", "Chemotherapy", "Wound care in previous 30 days", "Hemodialysis patient"]),
 R("Risk factors",
   "<b>Unmodifiable:</b> age over 70, chronic lung disease, depressed consciousness, large-volume aspiration, winter admission. "
   "<b>Modifiable:</b> <b>mechanical ventilation</b>, nasogastric tube, intracranial pressure monitor, <b>histamine H2 blocker or antacid</b>, prior antibiotics, reintubation.",
   18, ["Age > 70 years, chronic lung disease, depressed consciousness, large volume aspiration, hospitalized during winter months", "Mechanical ventilation, NG tube, ICP monitor, H-2 blocker or antacid therapy, previous antibiotic exposure, reintubation"]),
 R("Pathogens",
   "<b>Gram-negative: <i>Pseudomonas aeruginosa</i> most common</b> (also <i>E. coli</i>, <i>Klebsiella</i>, <i>Acinetobacter</i>, <i>Enterobacter</i>, <i>Serratia</i>). "
   "<b>Gram-positive: methicillin-resistant <i>S. aureus</i> most common</b>, <i>S. pneumoniae</i>. Fungi: <i>Candida</i>, <i>Aspergillus</i>.",
   19, ["Pseudomonas aeruginosa (most common)", "MRSA (most common)", "Candida spp., Aspergillus fumigatus"]),
 R("&#9733; Treat now, treat wide, then narrow",
   "<b>Start as soon as possible; do not wait for the culture.</b> Broad spectrum; <b>must cover methicillin-resistant <i>S. aureus</i> and <i>Pseudomonas</i></b> when multidrug-resistant pathogens are possible. <b>Streamline once cultures and sensitivities return.</b>",
   20, ["Start therapy as soon as possible", "don't wait on a definitive culture", "Must cover MRSA and pseudomonas", "Streamline therapy once cultures and sensitivities are available"]),
 R("Limited or broad",
   "<b>Late onset (5 days or more) or multidrug-resistance risk factors</b> (prior antibiotics, colonization, hospitalization or chronic care, immunosuppression) &rarr; <b>broad spectrum</b>; neither &rarr; limited spectrum.",
   21, ["Late onset (>=5 days) or risk factors for MDR pathogens", "Limited-spectrum initial antibiotic therapy", "Broad-spectrum initial antibiotic therapy for MDR pathogens"]),
 R("Limited spectrum (no multidrug-resistance risk)",
   "<b>One drug:</b> ceftriaxone, <b>or levofloxacin or moxifloxacin (choose these if worried about atypicals)</b>, or ampicillin/sulbactam, or <b>ertapenem (narrow-spectrum carbapenem)</b>.",
   22, ["No risk factors for MDR pathogens", "Ceftriaxone (3rd gen. cephalosporin)", "Choose this group if worried about atypical pathogens", "OR ampicillin/sulbactam", "Ertapenem (narrow spectrum carbapenem)"]),
 R("Broad spectrum (multidrug-resistance risk)",
   "<b>Antipseudomonal beta-lactam</b> (cephalosporin, carbapenem or penicillin/beta-lactamase inhibitor) <b>plus</b> an antipseudomonal fluoroquinolone (levofloxacin, ciprofloxacin) <b>or an aminoglycoside</b>, <b>plus vancomycin or linezolid</b>.",
   23, ["Gram negative combination therapy", "Antipseudomonal cephalosporin OR", "Antipseudomonal fluoroquinolone (levofloxacin, ciprofloxacin) OR", "Aminoglycoside", "PLUS gram positive coverage", "Vancomycin or linezolid"]),
 R("Afterward",
   "Scale back as cultures return; <b>switch to oral when possible (cheaper)</b>. Failure = <b>wrong therapy</b> (resistance, inadequate drug), <b>wrong diagnosis</b> (pulmonary embolus, neoplasm) or <b>complications</b> (<i>C. difficile</i> colitis, empyema, lung abscess).",
   31, ["Scale back antibiotic coverage as cultures are available", "Switch to PO when/if possible (cheaper)", "Wrong therapy", "Wrong diagnosis", "Pulmonary embolus, neoplasm", "C. difficile colitis, empyema or lung abscess"]),
])

# ----------------------------------------------------------------------------------------------
topic("pu-hapdrugs", "Pulmonary &middot; the hospital pneumonia antibiotics", "#1f6f5c", [
 R("Renal adjustment: everyone but linezolid",
   "Antipseudomonal cephalosporins, carbapenems, penicillins and fluoroquinolones, the aminoglycosides and vancomycin <b>all need renal adjustment</b>; <b>linezolid needs none</b>.",
   [(24, ["Both require renal adjustment!"]), (25, ["Require renal adjustment"]), (26, ["Require renal adjustment!"]), (27, ["Require renal adjustment"]),
    (28, ["Highly dependent on renal function"]), (29, ["Requires renal adjustment"]), (30, ["No dose adjustment based on renal function"])]),
 R("Cephalosporins",
   "<b>Cefepime (Maxipime) = fourth-generation</b>, antipseudomonal. Ceftazidime (Fortaz): rarely used, resistance develops rapidly (see the guideline row).",
   24, ["Cefepime (Maxipime", "4th generation cephalosporin", "Ceftazidime (Fortaz", "Rarely used"]),
 R("Carbapenems and seizures",
   "<b>Imipenem/cilastatin (Primaxin): caution with a seizure history.</b> <b>Meropenem (Merrem): less seizure risk.</b> <b>Ertapenem: limited activity against <i>Pseudomonas</i>.</b>",
   25, ["Imipenem/cilistatin (Primaxin", "Use with caution in patients with seizure history", "Meropenem (Merrem", "Less risk for seizures", "Ertapenem has limited activity against P. aeruginosa"]),
 R("Penicillins",
   "<b>Piperacillin/tazobactam (Zosyn).</b> Ticarcillin/clavulanate (Timentin): not used often (gram-negative resistance).",
   26, ["Piperacillin/tazobactam (Zosyn", "Ticarcillin/clavulanate (Timentin", "Not used very often"]),
 R("Fluoroquinolones",
   "<b>Ciprofloxacin (Cipro), levofloxacin (Levaquin)</b>: good against atypicals (<i>Mycoplasma</i>, <i>Chlamydia</i>, <i>Legionella</i>); <b>good lung penetration</b>; rising gram-negative resistance, so <b>use judiciously</b>.",
   27, ["Ciprofloxacin (Cipro", "Levofloxacin (Levaquin", "Good activity against atypicals", "Mycoplasma, Chlamydia, Legionella", "Good lung tissue penetration", "Use judiciously"]),
 R("&#9733; Aminoglycosides",
   "<b>Gentamicin, tobramycin, amikacin.</b> <b>Extended-interval (once-daily) dosing because of poor lung penetration</b> (bigger doses, higher concentrations). Adjust to <b>levels</b> and renal function. <b>Ototoxicity, nephrotoxicity.</b>",
   28, ["Gentamicin", "Tobramycin", "Amikacin", "Utilize extended interval dosing (once daily or longer)", "Poor lung penetration", "Adjust dose and frequency based on levels", "Ototoxicity/nephrotoxicity"]),
 R("&#9733; Vancomycin",
   "<b>Empiric methicillin-resistant <i>S. aureus</i> coverage.</b> <b>Trough before the third or fourth dose (steady state)</b>; the number itself is not to memorize. Renal adjustment; <b>ototoxicity; nephrotoxic with other nephrotoxins</b>.",
   29, ["Primarily used for empiric MRSA coverage", "Prior to 3rd-4th dose (Steady state)", "Ototoxicity", "Nephrotoxic (w/ other nephrotoxins)"]),
 R("Linezolid",
   "<b>Linezolid (Zyvox): great methicillin-resistant <i>S. aureus</i> coverage, intravenous and oral, good lung penetration, expensive, no renal adjustment.</b>",
   30, ["Linezolid (Zyvox", "Great MRSA coverage", "IV and PO forms available", "Good lung penetration", "Expensive", "No dose adjustment based on renal function"]),
])

# ----------------------------------------------------------------------------------------------
topic("pu-tb", "Pulmonary &middot; tuberculosis drugs", "#8c2f3a", [
 R("The organism",
   "<b>Acid-fast bacilli</b> with a waxy <b>mycolic acid</b> coat; <b>very slow growing and can lie dormant</b>, so drugs that act on cell division work less well.",
   34, ["Acid-fast bacilli", "mycolic acid", "forms waxy cell coat", "very slow growing", "dormant states", "Antimicrobials that affect cell division"]),
 R("&#9733; The regimen",
   "<b>2 months of isoniazid, rifampin, ethambutol and pyrazinamide, then 4 months of isoniazid and rifampin.</b> Pulmonary: 6 to 9 months. <b>Never a single agent in active disease</b> (resistance).",
   [(35, ["Combination Therapy", "Isoniazid", "Rifampin", "Ethambutol", "Pyrazinamide", "Followed by (4 months)"]),
    (36, ["Pulmonary Tuberculosis (6-9 months)", "use single agents in active disease to prevent resistance development"])]),
 R("Isoniazid",
   "<b>Inhibits mycolic acid</b> (waxy coat); bacteriostatic for latent, bactericidal for dividing bacteria; <b>activated by bacterial catalase-peroxidase</b> (mutation = resistance); fast and slow <b>acetylators</b>; enters the brain. "
   "<b>Alone for prophylaxis</b>, combined for active disease.",
   [(37, ["Bacteriostatic for latent, bacteriocidal for dividing bacteria", "Inhibits mycolic acid production", "acetylated metabolite"]),
    (38, ["Metabolically activated by bacterial catalase-perioxidase", "Resistance by mutation in DNA coding for activation enzyme", "Well absorbed, enters CNS"]),
    (39, ["Prophylactic use", "used alone", "Active disease", "combination therapy"])]),
 R("&#9733; Isoniazid adverse effects",
   "<b>Peripheral neuritis from pyridoxine deficiency: give pyridoxine (B6).</b> <b>Hepatitis</b>, worse with alcohol and age. <b>Lupus-like syndrome.</b> Brain: seizures, euphoria, psychosis, memory loss.",
   39, ["Allergic reactions", "Lupus like syndrome", "Hepatitis", "in alcoholics", "Peripheral neuritis", "pyridoxine deficiency", "Give pyridoxine (B6)", "CNS- seizures, euphoria, psychosis memory impairment"]),
 R("Rifampin",
   "<b>Inhibits DNA-dependent RNA polymerase</b> (not the human enzyme). Never alone (rapid tolerance). Uses: tuberculosis, <b>meningococcal prophylaxis</b>, endocarditis.",
   41, ["Inhibits DNA dependent RNA Polymerase", "no effect on human enzyme", "Rarely used alone because of rapid tolerance", "Meningococcal disease", "prophylactic", "Endocarditis"]),
 R("&#9733; Rifampin adverse effects",
   "<b>Induces cytochrome P450</b> (CYP1A2, 2C9, 3A4): <b>anticoagulants, contraceptives</b>, digoxin, ketoconazole, theophylline fall. <b>Orange tears, sweat and urine.</b> Hepatitis, jaundice; flu-like syndrome; gastrointestinal upset.",
   42, ["Induces P450 enzymes", "anticoagulants, contraceptives", "Digoxin, Ketoconazole, Theophylline", "Jaundice, hepatitis", "Secretions colored orange (tears, sweat, urine)", "flu-like syndrome", "GI disturbances"]),
 R("&#9733; Ethambutol",
   "<b>Bacteriostatic</b>; weakens the cell wall so the other drugs get in. <b>75 percent excreted unchanged: adjust in renal disease.</b> <b>Red-green color loss and decreased visual acuity.</b> Raises uric acid.",
   [(43, ["Bacteriostatic", "inhibits mycolic acid incorporation into membranes", "Weakened cell wall allows other agents better access"]),
    (44, ["75% excreted unchanged, adjust dose in renal disease", "Resistance develops quickly if used alone", "Decreased red-green discrimination", "Decreased visual acuity", "Increased uric acid levels"])]),
 R("&#9733; Pyrazinamide",
   "Converted to pyrazinoic acid, <b>lowers the pH</b>, enters macrophages; <b>shortens the course</b>. <b>First 2 months only (liver).</b> <b>Hepatitis: monitor liver enzymes. Hyperuricemia in everyone. Avoid in pregnancy.</b>",
   45, ["Converted to Pyrazinic acid, lowers pH so bacteria can't grow, enters macrophages", "Decrease duration of combined therapy", "Given first two months only, to avoid liver toxicity", "monitor liver enzymes", "Inhibits uric acid excretion, all hyperuricemic", "Avoid in pregnancy"]),
 R("Second-line agents (not tested)",
   "<b>Not tested</b> (&ldquo;I would not memorize this list&rdquo;; know the big four). For reference: <b>Streptomycin</b>: hearing and balance. <b>Aminosalicylic acid</b>: gastrointestinal. <b>Cycloserine</b>: psychosis, seizures. Also rifabutin, macrolides, quinolones, <b>clofazimine (leprosy)</b>, linezolid.",
   46, ["Streptomycin (Auditory/vestibular)", "Aminosalicylic acid (GI problems)", "Cycloserine (CNS, psychosis, seizures)", "Rifabutin, macrolides, Quinolones", "Clofazimine (leprosy)", "Linezolid"]),
])

# ----------------------------------------------------------------------------------------------
topic("pu-ana", "Pulmonary &middot; anaphylaxis", "#a8562f", [
 R("What it is",
   "A <b>severe, systemic allergic reaction</b>: skin, airway, vessels, gut. Can end in <b>airway obstruction, cardiovascular collapse and death</b>.",
   48, ["Severe, systemic allergic reaction", "skin, airway, vascular system, and GI", "complete obstruction of the airway, cardiovascular collapse, and death"]),
 R("&#9733; Epinephrine",
   "<b>Alpha:</b> vasoconstriction, less vascular leak. <b>Beta:</b> bronchial smooth muscle relaxation. Relieves itching, hives, angioedema. "
   "<b>Intramuscular is preferred unless the patient is coding</b> (then intravenous). Adverse effects: anxiety, hypertension, tachycardia, nausea and vomiting, sweating; <b>overdose: cerebral hemorrhage, myocardial infarction, pulmonary edema</b>.",
   [(51, ["Acts on alpha and beta receptors", "Vasoconstriction, decreased vascular permeability", "Bronchial smooth muscle relaxation", "Alleviates pruritus, urticaria, and angioedema"]),
    (52, ["IM generally preferred unless patient is coding", "anxiety, hypertension, tachycardia", "diaphoresis", "cerebrovascular hemorrhage, MI, pulmonary edema"])]),
 R("Fluids",
   "<b>Intravenous crystalloid (0.9 percent saline)</b> for profound vasodilation and hypotension; severe cases need far more. (Volumes are not tested.)",
   50, ["IV crystalloids (0.9% NaCl)", "For profound vasodilation/hypotension", "Increases intravascular volume"]),
 R("Histamine blockers",
   "<b>Histamine H1</b> (diphenhydramine, hydroxyzine): rash, itching, hives. <b>Histamine H2 (famotidine)</b>: the systemic vasodilation and gastrointestinal (acid) effects.",
   53, ["H1 blockers: diphenhydramine, hydroxyzine", "Relieves rash, pruritus, hives (cutaneous effects)", "H2 blockers: famotidine", "Blocks systemic (vasodilation) and GI effects"]),
 R("Albuterol and steroids",
   "<b>Albuterol</b> (beta-2 agonist) relaxes bronchial smooth muscle; anxiousness, tremor, tachycardia. <b>Corticosteroids</b> (methylprednisolone intramuscular or intravenous, prednisone) block mediator production but <b>take several hours</b>.",
   [(54, ["Beta 2 agonist", "Relaxes bronchial smooth muscle", "anxiousness, tremor, tachycardia"]),
    (55, ["Blocks production of inflammatory mediators at the cellular level", "Takes time to work (several hours)", "Methylprednisolone (IM, IV)", "Prednisone"])]),
])

# ----------------------------------------------------------------------------------------------
topic("pu-asthma", "Asthma &middot; the disease and the three approaches", "#4a7fa5", [
 R("Asthma",
   "<b>Widespread, reversible</b> bronchial narrowing; <b>eosinophilic</b> mucosal inflammation; marked bronchial hyperresponsiveness; thickened mucosa. Dyspnea, chest tightness, wheeze, cough.",
   57, ["widespread reversible narrowing of the bronchial airways", "eosinophilic inflammation of the bronchial mucosa", "Marked increase in bronchial responsiveness", "Thickening of the bronchial mucosa"]),
 R("Mast cell timing",
   "Allergen + immunoglobulin E: <b>immediate</b> histamine, proteases, heparin; <b>minutes</b>: prostaglandins, <b>leukotrienes</b>, platelet-activating factor; <b>hours</b>: interleukins. Early and late reactions.",
   [(59, ["Granule Content Release (Immediate): Histamine", "Membrane derived Lipid Mediators (Over minutes): Prostaglandins, Leukotrienes", "Cytokine Production (over hours)"]),
    (60, ["Early reaction", "Late reaction"])]),
 R("&#9733; Triggers",
   "<b>Most attacks are triggered by a viral respiratory infection, not by allergens.</b> Also distilled water, exercise, cold air, rapid breathing. <b>Methacholine challenge</b>: the fall in FEV1 (forced expiratory volume in 1 second).",
   62, ["Most asthma attacks are not triggered by allergens", "Most triggered by viral respiratory infection", "distilled water, exercise, cold air, rapid respiratory maneuvers", "methacholine"]),
 R("Neural pathways",
   "Mediators also fire <b>afferent vagal receptors</b> (reflex bronchoconstriction) and release <b>tachykinins (substance P)</b>, so drugs with different mechanisms all help.",
   63, ["Stimulate afferent vagal receptors in the airways to initiate reflex bronchoconstriction", "Release tachykinins (e.g. substance P)", "asthma may be treated by drugs with differing mechanisms of action"]),
 R("&#9733; Three approaches",
   "<b>1. Reverse bronchospasm:</b> beta-2 agonists, ipratropium, theophylline. <b>2. Remove trigger or antigen:</b> cromolyn, nedocromil. <b>3. Control inflammation:</b> steroids, lipoxygenase inhibitors.",
   64, ["Reverse Bronchospasm (b2 agonist, Ipratropium, Theophylline)", "Remove trigger or antigen (Cromolyn, Nedocromil)", "Control Inflammation (steroids, Lipoxygenase Inhibitors)"]),
 R("&#9733; Quick relief versus controller",
   "<b>Quick relief:</b> short-acting beta-2 agonists, anticholinergics, systemic corticosteroids. "
   "<b>Controllers:</b> long-acting beta-2 agonists, inhaled corticosteroids, leukotriene modifiers, mast cell stabilizers, anti-immunoglobulin E antibody, theophylline.",
   67, ["Quick Relief Medications", "Short acting beta-2 agonists", "Anticholinergics", "Systemic corticosteroids", "Long Term Controller Medications", "Leukotriene modifiers", "Mast cell stabilizers", "Anti-IgE antibody", "Methylxanthines (theophylline)"]),
 R("Severity at a glance",
   "<b>Intermittent:</b> symptoms and rescue use 2 days a week or fewer, night waking 2 a month or fewer, FEV1 over 80 percent. <b>Severe persistent:</b> symptoms all day, rescue several times a day, FEV1 under 60 percent.",
   65, ["Intermittent", "Throughout the day", "Several times per day", "FEV1 <60% predicted"]),
 R("Goals",
   "<b>Long term:</b> lower bronchial responsiveness with anti-inflammatories (inhaled corticosteroids). <b>Acute:</b> avoid triggers and treat bronchospasm with short-acting beta-2 agonists.",
   66, ["Reduce the level of bronchial responsiveness long term", "Reduced with anti-inflammatory agents (e.g. inhaled corticosteroids)", "Prevent or reverse acute bronchospasm", "Treat with short term beta-2 agonists"]),
])

# ----------------------------------------------------------------------------------------------
topic("pu-bd", "Asthma &middot; bronchodilators", "#b8862f", [
 R("&#9733; Beta-2 agonists",
   "<b>Raise cyclic adenosine monophosphate</b> (which inhibits myosin light chain kinase) and relax airway muscle. <b>Short-acting: rapid, 4 to 6 hours</b> (albuterol: ProAir, Ventolin; levalbuterol: Xopenex). "
   "<b>Long-acting: 12 hours or more</b> (formoterol: Foradil; salmeterol: Serevent), <b>never alone for asthma</b>.",
   [(68, ["Increase cyclic adenosine monophosphate (cAMP)", "Relax airway smooth muscle", "Work rapidly and last 4-6 hours", "Last 12 or more hours"]),
    (69, ["cAMP inhibits MLCK"]),
    (70, ["Albuterol (Proair, Ventolin)", "Levalbuterol (Xopenex", "Long acting (Do NOT use alone for asthma)", "Formoterol (Foradil)", "Salmeterol (Serevent)"])]),
 R("Beta-2 agonist adverse effects",
   "<b>Tachycardia, tremor</b>, hypotension, headache, dizziness, insomnia, <b>hyperglycemia</b>.",
   [(68, ["Increased heart rate and tremor"]), (71, ["Tachycardia", "Hypotension", "Headache", "Dizziness", "Insomnia", "Tremors", "Hyperglycemia"])]),
 R("&#9733; Theophylline",
   "<b>Nonspecific phosphodiesterase inhibitor</b> (phosphodiesterase 4 and 5) + <b>adenosine A2B receptor antagonist</b> + anti-inflammatory. <b>Narrow therapeutic index</b>; less effective and less tolerated than long-acting bronchodilators; limited use, <b>used in chronic obstructive pulmonary disease</b>. Intravenous form: aminophylline.",
   [(82, ["Nonspecific phosphodiesterase inhibitor", "Less effective", "Less well tolerated", "Narrow therapeutic index", "Theophylline (Aminophylline IV)"]),
    (83, ["Used in COPD", "Inhibit phosphodiesterase (PDE 4 ,5)", "Adenosine receptor (A2B) antagonist", "Anti-inflammatory actions"])]),
 R("&#9733; Theophylline toxicity",
   "Arrhythmias, <b>convulsions</b>, headache, nausea, insomnia, heartburn; stimulates gastric acid; diuretic. <b>Monitor plasma levels</b>: nausea, vomiting and cardiac effects first, then seizures and arrhythmias.",
   [(82, ["Associated with arrhythmias, convulsions, headaches, nausea, insomnia, heartburn"]),
    (84, ["Stimulant gastric acid", "Diuretic effects", "CNS stimulant", "convulsions", "Cardiac stimulant", "arrhythmias"]),
    (85, ["Monitor Theophylline plasma levels", "Nausea, vomiting, cardiac effects", "toxic effects - seizures, arrhythmias"])]),
 R("Anticholinergics",
   "<b>Block acetylcholine at muscarinic receptors</b> &rarr; bronchodilation. <b>Ipratropium (Atrovent): short-acting, up to 8 hours.</b> <b>Tiotropium (Spiriva): long-acting, 24 hours or more.</b>",
   86, ["Block acetylcholine", "muscarinic receptors", "Last up to 8 hours", "Ipratropium (Atrovent", "Last 24 hours or more", "Tiotropium (Spiriva"]),
 R("Anticholinergic effects",
   "Blind as a bat (blurred vision, dilated pupils); mad as a hatter (delirium, hallucinations); red as a beet (flushing); hot as Hades (fever); dry as a bone (dry mouth and eyes); constipation, urinary retention; tachycardia.",
   87, ["Blind as a bat (blurry vision, mydriasis)", "Mad as a hatter", "flushing", "fever, hyperthermia", "Dry as a bone (dry mouth, dry eyes)", "constipation, urinary retention", "tachycardia, hypertension"]),
])

# ----------------------------------------------------------------------------------------------
topic("pu-ctl", "Asthma &middot; controllers", "#7a4a9c", [
 R("&#9733; Inhaled corticosteroids",
   "Beclomethasone (QVAR), budesonide (Pulmicort), flunisolide (Aerobid), fluticasone (Flovent), mometasone (Asmanex), triamcinolone (Azmacort). "
   "<b>Inhibit the inflammatory cascade; up to 8 weeks for full effect.</b> <b>Thrush</b>; <b>growth suppression in children (high dose)</b>; immune suppression.",
   [(72, ["Beclomethasone  (QVAR", "Budesonide  (Pulmicort", "Fluticasone   (Flovent", "Mometasone (Asmanex", "Triamcinolone  (Azmacort"]),
    (73, ["Inhibit inflammatory cascade", "Up to 8 weeks for maximal effects", "Oral candidiasis  (thrush)", "Suppress growth in children (high dose)", "Inhibit immune system (systemic action)"])]),
 R("Combination inhalers",
   "<b>Symbicort = formoterol/budesonide. Dulera = formoterol/mometasone. Advair = salmeterol/fluticasone.</b>",
   74, ["Formoterol/budesonide", "Formoterol/mometasone", "Salmeterol/fluticasone", "Symbicort", "Dulera", "Advair"]),
 R("&#9733; Montelukast",
   "<b>Oral leukotriene D4 antagonist at the cysteinyl leukotriene 1 receptor</b> (Singulair); that receptor drives inflammation, bronchoconstriction, mucus. <b>Effective in aspirin-induced asthma.</b>",
   75, ["Leukotriene Antagonists (oral)", "Montelukast", "LTD4 antagonist (cysLT1 receptor)", "inflammation, bronchial  constriction, mucous secretion", "Effective in Aspirin Induced asthma"]),
 R("Cromolyn and nedocromil",
   "<b>Stabilize mast cells</b> (limited use). <b>Must be taken before the antigen exposure</b>; <b>up to 4 weeks</b>; <b>taken regularly</b>. Inhaled. Mechanism unknown (calcium?).",
   [(77, ["Stabilize mast cells: limited use", "Cromolyn Sodium (inhalation)", "Nedocromil (inhalation)", "Must be taken before antigen insult"]),
    (78, ["May take up to 4 weeks to work; must be taken regularly"])]),
 R("&#9733; Omalizumab",
   "<b>Anti-immunoglobulin E monoclonal antibody</b> (Xolair), <b>subcutaneous every 2 to 4 weeks</b>. <b>Binds circulating immunoglobulin E</b>, fewer mast cell receptors, <b>no degranulation</b>. "
   "<b>Anaphylaxis</b>, gastrointestinal upset, neutralizing antibodies, secondary malignancies; urticaria, injection site pain, bruising.",
   [(79, ["Omalizumab (Xolair", "SubQ 2 - 4 weeks", "humanized IgE monoclonal antibody", "Binds circulating IgE", "prevents degranulation", "Anaphylaxis", "Secondary Malignancies"]),
    (80, ["Urticaria (0.1%)", "Injection site pain", "Bruising"])]),
 R("Other biologics",
   "For the <b>eosinophilic phenotype</b>. <b>Anti-interleukin-5:</b> mepolizumab (Nucala), benralizumab (Fasenra), <b>reslizumab (Cinqair), intravenous</b>. <b>Anti-interleukin-4: dupilumab (Dupixent).</b> Side effects like omalizumab's.",
   81, ["Used for eosinophilic phenotype", "Mepolizumab (Nucala)", "Benralizumab (Fasenra)", "Given IV", "Dupilumab (Dupixent)", "Similar side effect profile to omalizumab"]),
 R("&#9733; Systemic corticosteroids",
   "<b>Most potent, limited by side effects: for exacerbations.</b> Prednisone (tablet), prednisolone (liquid), methylprednisolone and dexamethasone (oral or parenteral). "
   "<b>Adrenal suppression</b>, growth suppression, thin skin, hypertension, <b>hyperglycemia</b>, mood change, <b>steroid myopathy</b>, immunosuppression.",
   [(88, ["Most potent but limited use due to side effects", "Used in asthma exacerbations", "Prednisone (Deltasone) - oral tablet", "Prednisolone (Ora-Pred) - oral liquid"]),
    (89, ["Adrenal suppression", "Growth suppression", "Dermal thinning", "Hypertension", "Hyperglycemia", "Muscle weakness (steroid myopathy)", "Immunosuppression"])]),
])

# ----------------------------------------------------------------------------------------------
topic("pu-inh", "Asthma &middot; steps, devices and status asthmaticus", "#3d6b52", [
 R("Stepwise therapy",
   "Adjust up and down. Preferred controller: <b>as-needed low-dose inhaled corticosteroid-formoterol (step 1)</b> up to <b>high-dose inhaled corticosteroid plus long-acting beta-2 agonist with phenotype referral (step 5)</b>. "
   "Preferred reliever: as-needed low-dose inhaled corticosteroid-formoterol; other reliever: as-needed short-acting beta-2 agonist.",
   90, ["Adjust treatment up and down", "Step 1 As-needed low-dose ICS-formoterol", "Step 5 High-dose ICS-LABA, Refer for phenotypic assessment", "Preferred reliever: As-needed low-dose ICS-formoterol", "Other reliever option: As-needed SABA"]),
 R("&#9733; Nebulizer",
   "Compressor makes a mist; <b>passive inhalation: children and elderly who cannot use a metered dose inhaler</b>. <b>Bigger dose, more side effects.</b> Clean it (microbial growth).",
   92, ["Compressor forces liquid medication into a fine mist", "Allows for passive inhalation of medications", "Good for children, elderly who can't use MDI", "Bigger dose is administered overall", "May lead to more side effects", "Must be cleaned regularly to prevent microbial growth"]),
 R("Dry powder inhaler",
   "Powder; <b>the patient's own inspiratory force</b> draws it out, so <b>not for poor inspiratory capacity</b>.",
   93, ["Medication in powder form", "Patients provide inspiratory force", "Not good for patients who have poor inspiratory capacity"]),
 R("Metered dose inhaler and spacers",
   "Liquid with a propellant; <b>needs the most coordination</b>; a <b>spacer</b> helps poor coordination. Spacer = open tube; <b>valve holding chamber = one-way valve, no exhaling into it</b>. Both keep the large particles back.",
   [(94, ["Medication in liquid form", "Requires most coordination for proper use", "Spacers used to hold medication for patients with poor coordination"]),
    (95, ["open tube that extends the inhaler away from the patient", "one way valves that do not allow the patient to exhale into the device", "Intended to retain large particles emitted from the inhaler"])]),
 R("&#9733; Technique",
   "Cap off, shake (prime). <b>Breathe out fully.</b> <b>Breathe in slowly as you press</b> (with a holding chamber: press, then breathe within 5 seconds). <b>Hold 10 seconds.</b> Rescue inhaler: <b>15 to 30 seconds between puffs</b>.",
   [(96, ["Take off cap and shake inhaler (may need to be primed)", "Breathe out all the way"]),
    (97, ["Start breathing in slowly as you press down on inhaler", "first press down on inhaler and then begin breathing within 5 seconds", "Hold your breath for 10 seconds", "wait 15-30 seconds between puffs"])]),
 R("&#9733; Albuterol overuse",
   "<b>Albuterol is short-term relief, used sparingly; excessive use means poor control and the long-term therapy needs adjusting.</b> Controllers daily.",
   98, ["Albuterol only provides short term relief and should be used sparingly", "Excessive use indicates poor control and need for adjustment in long-term therapy", "Long-term controller medications need to be used daily"]),
 R("Status asthmaticus",
   "An exacerbation <b>unresponsive to the first bronchodilator treatment</b>. <b>Continuous nebulized albuterol; steroids (intravenous preferred); magnesium; ketamine if intubated</b> (NMDA, N-methyl-D-aspartate, antagonist; releases catecholamines; emergence phenomenon, hypertension, tachycardia, vomiting).",
   99, ["acute exacerbation that remains unresponsive to initial bronchodilator treatment", "Continuous albuterol", "Steroids (IV preferred)", "Magnesium (bolus followed by continuous infusion)", "Ketamine (if intubated)", "NMDA receptor antagonist", "Increases catecholamine release", "emergence phenomenon, hypertension, tachycardia, vomiting"]),
])

# ----------------------------------------------------------------------------------------------
topic("pu-copd", "Chronic obstructive pulmonary disease &middot; drugs, smoking cessation, vaccines", "#6b3524", [
 R("The disease",
   "<b>Chronic airway and parenchymal inflammation, generally not fully reversible</b>; FEV1 (forced expiratory volume in 1 second) falls faster than normal, and <b>symptoms appear only after a big fall</b>.",
   [(101, ["Chronic inflammation of airways and lung parenchyma", "generally not fully reversible", "Accelerated decline in FEV1", "Symptoms generally develop only after a significant decline"])]),
 R("&#9733; Groups A to D",
   "<b>All:</b> stop smoking, <b>yearly influenza and pneumococcal vaccines</b>, activity, <b>check inhaler technique</b>, oxygen if chronically hypoxemic, rehabilitation. "
   "<b>A:</b> short-acting bronchodilator as needed. <b>B:</b> long-acting muscarinic antagonist or long-acting beta-2 agonist. <b>C:</b> long-acting muscarinic antagonist. "
   "<b>D:</b> long-acting muscarinic antagonist, or both long-acting classes if very breathless; inhaled corticosteroid plus long-acting beta-2 agonist if asthma overlaps.",
   102, ["Annual influenza vaccination", "Pneumococcal vaccination", "Regular review/correction of inhaler technique", "Short-acting bronchodilator (SABA, SAMA, or combination of SABA-SAMA), as needed", "either LAMA or LABA, based on patient preference", "Regular treatment with a LAMA; SABA available", "combination LABA plus LAMA", "Combination glucocorticoid-LABA inhaler may be preferred, if features of asthma/COPD overlap"]),
 R("&#9733; Smoking",
   "Cigarette smoke causes most cases; <b>quitting returns the decline in lung function to the normal age-related rate</b>. <b>Combine medication with counseling</b>; more counseling, more success.",
   103, ["Smoking - a major contributor to COPD", "return to the normal age-related rate of decline in ventilatory function", "Effective programs should combine pharmacologic intervention with counseling", "Intensity and frequency of counseling directly correlates with the success of quitting"]),
 R("&#9733; Bupropion SR (Zyban)",
   "<b>Inhibits norepinephrine and dopamine uptake</b> (mimics nicotine's effects). <b>Avoid with seizure disorders and monoamine oxidase inhibitors</b>; caution with tricyclic antidepressants and venlafaxine.",
   105, ["inhibits the uptake of norepinephrine and dopamine", "patients with seizure disorders", "patients taking MAOIs", "use caution in patients taking noradrenergic antidepressants (TCA and venlafaxine)"]),
 R("Nicotine replacement",
   "Patch, gum (polacrilex), spray, inhaler. <b>Less craving and withdrawal</b>; 6 to 12 weeks; <b>patch and gum over the counter</b>; <b>caution in cardiovascular disease</b> (tachyarrhythmias, hypertension).",
   [(104, ["Nicotine Transdermal system (Patches)", "Nicotine polacrilex (Gum)", "Nicotine spray", "Nicotine inhaler"]),
    (106, ["Reduces craving to smoke, minimize physical withdrawal", "duration of therapy is between 6-12 weeks", "Patches and Gum are available OTC", "Caution in patients with cardiovascular problems due to chance of tachyarrhythmias and hypertension"])]),
 R("&#9733; Varenicline (Chantix)",
   "<b>Partial nicotine receptor agonist.</b> <b>Start one week before the quit date</b>, 12 weeks. Nausea, sleep disturbance, headache. <b>Black box warning: neuropsychiatric events (depression, suicidal ideation).</b>",
   107, ["partial nicotine receptor agonist", "start one week before quit date and continue for 12 weeks", "nausea, sleep disturbance, HA", "Black box warning: neuropsychiatric events (depression, suicidal ideations)"]),
 R("Vaccines",
   "Influenza pneumonia is a major threat: <b>annual influenza vaccine highly recommended</b>, plus <b>the pneumococcal vaccine</b>.",
   108, ["Annual influenza vaccination is highly recommended", "pneumococcal vaccine (Pneumovax)"]),
])

# ----------------------------------------------------------------------------------------------
topic("pu-lookup", "Pulmonary &middot; which drug causes it", "#2f4f6b", [
 R("Seizures",
   "<b>Imipenem</b> (caution with a seizure history; meropenem less), <b>isoniazid</b>, <b>cycloserine</b>, <b>theophylline</b> (convulsions); <b>bupropion</b> is avoided in seizure disorders.",
   [(25, ["Use with caution in patients with seizure history"]), (39, ["seizures"]), (46, ["Cycloserine (CNS, psychosis, seizures)"]), (84, ["convulsions"]), (105, ["patients with seizure disorders"])]),
 R("Liver",
   "<b>Isoniazid</b> (alcohol, age), <b>rifampin</b> (jaundice, hepatitis), <b>pyrazinamide</b> (15 percent; monitor enzymes; first 2 months only).",
   [(39, ["Hepatitis"]), (42, ["Jaundice, hepatitis"]), (45, ["Hepatitis 15%, monitor liver enzymes"])]),
 R("Uric acid",
   "<b>Ethambutol</b> raises it; <b>pyrazinamide</b> makes everyone hyperuricemic.",
   [(44, ["Increased uric acid levels"]), (45, ["all hyperuricemic"])]),
 R("Ears, eyes, nerves",
   "<b>Ototoxicity:</b> aminoglycosides, vancomycin, streptomycin. <b>Red-green loss:</b> ethambutol. <b>Peripheral neuritis:</b> isoniazid. <b>Blurred vision, dilated pupils:</b> anticholinergics.",
   [(28, ["Ototoxicity/nephrotoxicity"]), (29, ["Ototoxicity"]), (46, ["Streptomycin (Auditory/vestibular)"]), (44, ["Decreased red-green discrimination"]), (39, ["Peripheral neuritis"]), (87, ["blurry vision, mydriasis"])]),
 R("Kidneys",
   "<b>Nephrotoxicity:</b> aminoglycosides; vancomycin with other nephrotoxins. <b>Ethambutol</b> is mostly excreted unchanged.",
   [(28, ["Ototoxicity/nephrotoxicity"]), (29, ["Nephrotoxic (w/ other nephrotoxins)"]), (44, ["75% excreted unchanged"])]),
 R("Heart rate and pressure",
   "<b>Tachycardia:</b> epinephrine, albuterol and the beta-2 agonists, anticholinergics, ketamine, nicotine replacement (tachyarrhythmias). <b>Arrhythmias:</b> theophylline.",
   [(52, ["tachycardia"]), (54, ["tachycardia"]), (71, ["Tachycardia"]), (87, ["tachycardia, hypertension"]), (99, ["hypertension, tachycardia"]), (106, ["tachyarrhythmias"]), (82, ["arrhythmias"])]),
 R("Mouth and growth",
   "<b>Thrush</b> and <b>growth suppression in children</b>: inhaled corticosteroids; growth suppression also with systemic corticosteroids.",
   [(73, ["Oral candidiasis  (thrush)", "Suppress growth in children (high dose)"]), (89, ["Growth suppression"])]),
 R("Anaphylaxis from the treatment",
   "<b>Omalizumab</b> (and the other asthma biologics, with a similar profile).",
   [(79, ["Anaphylaxis"]), (80, ["Anaphylaxis (0.1%)"]), (81, ["Similar side effect profile to omalizumab"])]),
 R("Orange, lupus, flu",
   "<b>Orange secretions</b> and a <b>flu-like syndrome</b>: rifampin. <b>Lupus-like syndrome</b>: isoniazid.",
   [(42, ["Secretions colored orange", "flu-like syndrome"]), (39, ["Lupus like syndrome"])]),
 R("Mind",
   "<b>Psychosis:</b> isoniazid, cycloserine. <b>Emergence phenomenon:</b> ketamine. <b>Neuropsychiatric black box warning:</b> varenicline. <b>Delirium, hallucinations:</b> anticholinergics.",
   [(39, ["psychosis"]), (46, ["psychosis"]), (99, ["emergence phenomenon"]), (107, ["neuropsychiatric events"]), (87, ["hallucinations, delirium"])]),
])

# ----------------------------------------------------------------------------------------------
topic("pu-guidelines", "Pulmonary &middot; slide versus guideline", "#8c1d12", [
 R("Tested from the slides",
   "These rows say where current practice or the slides themselves differ. <b>The slide wording is what you are tested on;</b> the points marked &ldquo;not asked&rdquo; are not asked as questions here."),
 R("Current guidelines differ: outpatient pneumonia",
   "Slide 14: macrolide first line. The 2019 guideline prefers <b>amoxicillin or doxycycline</b> for a healthy outpatient and a macrolide alone only where pneumococcal resistance is low.",
   14, ["1st line: macrolide"]),
 R("Current guidelines differ: health-care associated pneumonia",
   "Slide 17 defines it; the 2016 hospital pneumonia guideline <b>dropped the category</b>. Durations: slide 31 gives 7 to 8 days (10 to 14 for <i>Pseudomonas</i> and others); the guideline gives about 7 for most (not asked).",
   [(17, ["Health-Care Associated Pneumonia"]), (31, ["Treatment duration"])]),
 R("Current guidelines differ: ceftazidime and vancomycin",
   "Ceftazidime is <b>still an option</b> for hospital pneumonia (slide 24 says not recommended; Dr. Wood affirmed it aloud, so it is asked once). Vancomycin is now dosed to an area-under-the-curve target; the trough number on slide 29 is not asked.",
   [(24, ["No recommended due to rapid development of resistance"]), (29, ["Goal trough"])]),
 R("Slides wrong: rifampin spectrum",
   "Slide 40 lists <i>Neisseria</i> and <i>Legionella</i> as gram-positive; <b>both are gram-negative</b>. Not asked.",
   40, ["Gram + (Neisseria, Staph A, Legionella)"]),
 R("Current guidelines differ: tuberculosis",
   "Most HIV (human immunodeficiency virus) co-infection now gets the standard 6 months; most tuberculosis outside the lungs 6 to 12 months; drug-resistant regimens are shorter than 18 to 24 months (not asked). The World Health Organization allows pyrazinamide in pregnancy (slide 45 says avoid; that is keyed).",
   [(36, ["HIV patients with tuberculosis (9-12 months)"]), (45, ["Avoid in pregnancy"])]),
 R("Slides wrong: theophylline elimination",
   "Slide 85 says <b>renally eliminated</b>; theophylline is mainly <b>metabolized by the liver</b> (rifampin's enzyme induction lowers it, slide 42). The units differ between slides 84 and 85 (mcg/ml against mg/ml). Neither the route nor a level is asked.",
   [(85, ["Renally eliminated!"]), (42, ["Theophylline"])]),
 R("Slides disagree: tiotropium",
   "Slide 86: tiotropium &ldquo;COPD only&rdquo; (chronic obstructive pulmonary disease). Slide 90 lists <b>add-on tiotropium at asthma steps 4 and 5</b>; aloud he said &ldquo;mostly for COPD only, occasionally for more difficult to control asthma.&rdquo; Not asked.",
   [(86, ["(COPD only)"]), (90, ["add-on tiotropium"])]),
 R("Current labeling differs: montelukast",
   "Slide 75: side effects minimal (he repeated it aloud). Since 2020 montelukast carries a <b>boxed warning for neuropsychiatric events</b>. Its side effects are not asked.",
   75, ["Side effects minimal and well tolerated"]),
 R("Current guidelines differ: steroids",
   "Slide 89: taper after more than 5 days (Dr. Wood affirmed it aloud; asked once). Short bursts for an exacerbation are usually <b>stopped without a taper</b>. Slide 99: intravenous steroids preferred in status asthmaticus; <b>oral works as well</b> when the patient can swallow.",
   [(89, ["taper is duration is > 5 days"]), (99, ["Steroids (IV preferred)"])]),
 R("Current guidelines differ: chronic obstructive pulmonary disease",
   "Since 2023 groups C and D are <b>one group E</b>. The varenicline (and bupropion) boxed warning was <b>removed in 2016</b>. Pneumococcal vaccination now usually starts with a <b>conjugate vaccine</b>. The slides are keyed.",
   [(102, ["Groups"]), (107, ["Black box warning"]), (108, ["pneumococcal vaccine (Pneumovax)"])]),
 R("Boxed warnings (not on the slides)",
   "<b>Fluoroquinolones</b> (tendon rupture, neuropathy, central nervous system effects), <b>aminoglycosides</b> (kidney, ear, neuromuscular), <b>isoniazid</b> (hepatitis), <b>omalizumab</b> (anaphylaxis). Varenicline's is the only one the slides state."),
])

# ---------------------------------------------------------------------------------------------- what he stressed
# Written after the recording pass (Whisper transcript only). Defined last, then moved to the front of the Lecture 11
# topics, as Lecture 10's "what he stressed" topic is.
topic("pu-rules", "Pulmonary &middot; what he stressed", "#8c1d12", [
 R("&#9733;&#9733; The broad nosocomial regimen (&ldquo;there will be a question like this&rdquo;)",
   "Name each drug's class, then check: <b>ONE antipseudomonal beta-lactam</b> (cefepime or ceftazidime; imipenem/cilastatin or meropenem; piperacillin/tazobactam) "
   "<b>+ ONE antipseudomonal fluoroquinolone or aminoglycoside</b> (levofloxacin, ciprofloxacin; gentamicin, tobramycin, amikacin) <b>+ vancomycin or linezolid</b>. "
   "<b>Fails:</b> two beta-lactams (same mechanism); two gram-positive drugs with one gram-negative; ertapenem (limited <i>Pseudomonas</i> activity) or ceftriaxone in the beta-lactam slot.",
   [(23, ["Antipseudomonal cephalosporin OR", "Antipseudomonal carbapenem OR", "PLUS", "Aminoglycoside", "Vancomycin or linezolid"]),
    (25, ["Ertapenem has limited activity against P. aeruginosa"]), (22, ["Ceftriaxone (3rd gen. cephalosporin)"])],
   quotes=["There will be a question like this on the test and you're going to get a bunch of", "then is that an appropriate regimen?",
           "We are shooting for synergy, so we want different mechanisms."]),
 R("&#9733;&#9733; Quick relief or controller, for every asthma drug",
   "<b>Quick relief:</b> short-acting beta-2 agonists, anticholinergics, systemic corticosteroids. <b>Long-term controllers:</b> long-acting beta-2 agonists, inhaled corticosteroids, "
   "leukotriene modifiers, mast cell stabilizers, anti-immunoglobulin E antibody, theophylline. Burning through the rescue inhaler = poor control.",
   [(67, ["Quick Relief Medications", "Long Term Controller Medications"]), (98, ["Excessive use indicates poor control"])],
   quotes=["it for, right? Because those are easy test questions I can ask. I say which", "one of these is good for quick relief? Which one of these is good as a"]),
 R("&#9733;&#9733; Stepwise asthma therapy: what to start, what comes next",
   "Preferred controllers step up: <b>daily low-dose inhaled corticosteroid &rarr; low-dose inhaled corticosteroid + long-acting beta-2 agonist &rarr; medium dose &rarr; high dose + referral for phenotypic assessment</b> "
   "(add-on tiotropium or a biologic). Albuterol is a reliever, not a controller; theophylline and biologics are not first line. Either reliever (as-needed inhaled corticosteroid-formoterol or a short-acting beta-2 agonist) is acceptable.",
   90, ["Step 2 Daily low-dose ICS", "Step 3 Low-dose ICS-LABA", "Step 4 Medium-dose ICS-LABA", "Refer for phenotypic assessment", "Other reliever option: As-needed SABA"],
   quotes=["further up the line and say, hey, they're on this already, what would you want to",
           "So either of these would be a perfectly fine answer if I was saying which would"]),
 R("&#9733; Never a long-acting beta-2 agonist alone in asthma",
   "Formoterol and salmeterol are <b>always paired with an inhaled corticosteroid</b> for asthma (Symbicort, Dulera, Advair). He noted chronic obstructive pulmonary disease is different.",
   [(70, ["Long acting (Do NOT use alone for asthma)"]), (74, ["Formoterol/budesonide", "Salmeterol/fluticasone"])],
   quotes=["acting beta agonist by itself they've actually found the studies that that increased risk for"]),
 R("&#9733; Inhaled corticosteroids: the mainstay",
   "The gold-standard controller; <b>up to 8 weeks</b> for maximal effect, so keep taking it; <b>rinse the mouth</b> (thrush).",
   73, ["Up to 8 weeks for maximal effects", "Oral candidiasis  (thrush)"],
   quotes=["the gold standard for prevention of asthma symptoms are going to be the inhaled corticosteroids",
           "rinse their mouth out after using their inhaled corticosteroids"]),
 R("&#9733; Rifampin is an inducer",
   "<b>Not an inhibitor: an inducer.</b> Anticoagulants, contraceptives and digoxin fall (counsel on contraception). Then liver injury and orange secretions.",
   42, ["Induces P450 enzymes", "anticoagulants, contraceptives"],
   quotes=["not an inhibitor, this is an inducer, so it's gonna cause levels of other drugs like"]),
 R("&#9733; Cultures before antibiotics; linezolid without renal adjustment",
   "Hospitalized pneumonia: <b>blood and sputum cultures before the first antibiotic</b>. Every hospital pneumonia antibiotic needs renal adjustment <b>except linezolid</b>.",
   [(11, ["Prior to ABX!"]), (30, ["No dose adjustment based on renal function"])],
   quotes=["And this needs to be done prior to antibiotics.", "Finally, the one thing that doesn't require"]),
 R("&#9733; Anaphylaxis: epinephrine first when airway or circulation fail",
   "Airway or cardiovascular compromise: <b>epinephrine right away</b> (intramuscular or subcutaneous; intravenous only if coding). It acts at once; <b>corticosteroids take hours</b>.",
   [(52, ["IM generally preferred unless patient is coding"]), (55, ["Takes time to work (several hours)"])],
   quotes=["any sort of airway compromise, absolutely use the epinephrine right away.",
           "Things like corticosteroids, they take some time to work. They take hours"]),
 R("Not tested",
   "The pathogen lists by setting (slide 12: learn the trend), the <b>second-line tuberculosis list</b> (slide 46), the vancomycin trough number (slide 29), "
   "classifying a patient's asthma severity (slide 65), <b>which interleukin</b> each biologic targets (slide 81: know interleukin against immunoglobulin E), and doses.",
   quotes=["I'm not having you to memorize this exact list, right, but it's how we kind of link back", "I would not memorize this list.",
           "You don't have to memorize the specific gold trough level.", "test question from me at least.",
           "I'm not going to really care if you know the difference between the two, I would just"]),
])
_rules = T.pop()
T.insert(0, _rules)

assert len({t["id"] for t in T}) == len(T), "duplicate topic id"
