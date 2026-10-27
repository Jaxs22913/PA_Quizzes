# -*- coding: utf-8 -*-
"""Arcade decks for Pharmacology I Exam 3, Lecture 11 (Pulmonology-2.pptx: pulmonary infections, asthma and chronic
obstructive pulmonary disease), drafted 2026-10-27.

Imported by add_pharm_e3_arcade.py next to the Lecture 9 and 10 modules. Eight decks, one per topic of the build
(bronchitis and community-acquired pneumonia; nosocomial pneumonia and its antibiotics; tuberculosis; anaphylaxis;
asthma and the bronchodilators; asthma controllers; asthma steps, inhalers and status asthmaticus; chronic obstructive
pulmonary disease and smoking cessation). Atomic question -> short answer cards per [[arcade_content_policy]], slide
facts only (the deck has no speaker notes; picture-slide text read by eye is in tools/pharm_e3/ocr.json under "L11"),
no doses, US spelling, abbreviations written out (a drug-name suffix or a receptor label such as H1 is not one).

Same contract as Lectures 9 and 10: every card is written with C(deck, question, answer, slide(s), verify...) and the
adder PROVES each verify substring is on the cited Lecture 11 slide (pharm_e3_lib.slide_text("L11", n)). No recording
quotes are carried (tf stays empty).

Deliberately NOT carried (the Lecture 11 keying decisions): every dose (tuberculosis milligram amounts, fluid volumes,
epinephrine concentrations, the bupropion schedule, nebulized albuterol per hour, the ketamine and magnesium regimens);
drug levels as answers (theophylline ranges, the vancomycin trough number); theophylline "renally eliminated";
rifampin's gram-positive and gram-negative lists; tiotropium "COPD only"; montelukast "side effects minimal"; the
systemic steroid taper rule (held until the recording pass); ceftazidime "not recommended"; ticarcillin/clavulanate as
a choice; cromolyn's brand; benralizumab's target set against mepolizumab's; the extended treatment duration for
Pseudomonas and the other named organisms; the pneumococcal vaccine brand; bare numbers or percentages as answers.

NOT YET IN arcade.js until the integrator runs `python3 tools/add_pharm_e3_arcade.py`.
"""
REG = []     # (deck id, question, [(slide, [verify])], [quotes])


def C(deck, q, a, slide, verify=(), tf=()):
    pairs = [(slide, list(verify))] if isinstance(slide, int) else [(s, list(v)) for s, v in slide]
    REG.append((deck, q, pairs, list(tf)))
    return (q, a)


WIND_ICON = '<path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/>'

CAP, HAP, TB, ANA = "pharm-pu-cap", "pharm-pu-hap", "pharm-pu-tb", "pharm-pu-anaphylaxis"
BD, CTL, INH, COPD = "pharm-pu-bronchodilators", "pharm-pu-controllers", "pharm-pu-inhalers", "pharm-pu-copd"

DECKS = [
 (CAP, "Acute Bronchitis &amp; Community-Acquired Pneumonia", "accent1", WIND_ICON, [
  C(CAP, "What is bronchitis?", "Inflammation of one or more bronchi, generally secondary to infection.", 5, ["Inflammation of one or more bronchi", "Secondary to infection generally"]),
  C(CAP, "Which parts of the lung does bronchitis not involve?", "The bronchioles and the alveoli.", 5, ["Doesn't involve bronchioles and alveoli"]),
  C(CAP, "Which patients does chronic bronchitis primarily affect?", "Patients with chronic obstructive pulmonary disease.", 5, ["primarily affects COPD patients"]),
  C(CAP, "What usually causes acute bronchitis?", "Viruses: rhinovirus, coronavirus, influenza and adenovirus.", 6, ["Common causes", "viruses", "Rhinovirus, coronavirus, influenza, adenovirus"]),
  C(CAP, "How is acute bronchitis generally treated?", "Symptomatic and supportive care: analgesics, antipyretics, antitussives and fluids.", 7, ["Generally self-limited", "Symptomatic/supportive care only", "Analgesics, antipyretics, antitussives, fluids"]),
  C(CAP, "Why might antihistamines and sympathomimetics be avoided in acute bronchitis?", "They dehydrate bronchial secretions and may prolong symptoms.", 7, ["Possibly avoid antihistamines/sympathomimetics", "Dehydrate bronchial secretions, may prolong symptoms"]),
  C(CAP, "Are routine antibiotics recommended for acute bronchitis?", "No; it is a common cause of unnecessary antibiotic prescription.", 8, ["Routine ABX not recommended", "Common cause for unnecessary antibiotic prescription"]),
  C(CAP, "When should bacterial involvement be considered in acute bronchitis?", "When symptoms persist for more than 5 days.", 8, ["Persistent symptoms > 5 days, consider bacterial involvement"]),
  C(CAP, "Which antibiotic is preferred in bronchitis when Mycoplasma is documented?", "Doxycycline, because of macrolide resistance.", 8, ["Doxycycline", "Preferred if mycoplasma documented due to macrolide resistance"]),
  C(CAP, "How do microbes most commonly reach the lungs of elderly patients?", "By aspiration from the oropharynx.", 10, ["Aspiration from oropharynx", "Common in elderly"]),
  C(CAP, "When are blood and sputum cultures drawn in community-acquired pneumonia?", "In hospitalized patients, before antibiotics are given.", 11, ["Blood and sputum cultures for hospitalized patients", "Prior to ABX!"]),
  C(CAP, "Why is the sputum gram stain and culture controversial?", "Expectorated sputum is often contaminated and the pathogen is not always identified.", 11, ["Controversial", "Expectorated sputum frequently contaminated", "Responsible pathogen not always identified"]),
  C(CAP, "How do the likely pneumonia pathogens change from outpatient care to the intensive care unit?", "They get tougher as patients get sicker: the intensive care unit list adds Staphylococcus aureus and gram-negative bacilli.", 12, ["Outpatient", "Inpatient (ICU)", "Staphylococcus aureus", "Gram-negative bacilli"]),
  C(CAP, "Which factors raise the risk of penicillin-resistant Streptococcus pneumoniae?", "Age over 65, a recent beta-lactam, alcoholism, immunosuppression, comorbidities and day-care exposure.", 13, ["Penicillin-resistant S. pneumoniae", "Age > 65 years", "Beta-lactam within past 3 months", "Alcoholism", "Immunosuppressed", "Exposure to a child in a day care center"]),
  C(CAP, "What is first-line outpatient therapy for pneumonia without resistance risk?", "A macrolide: azithromycin or clarithromycin.", 14, ["No risk of resistant S. pneumoniae", "1st line: macrolide", "azithromycin, clarithromycin"]),
  C(CAP, "What is second-line outpatient therapy for pneumonia without resistance risk?", "Doxycycline or minocycline.", 14, ["2nd line: doxycycline, minocycline"]),
  C(CAP, "How is outpatient pneumonia treated when there are risk factors for resistant pneumococcus?", "A beta-lactam plus a macrolide, or a respiratory fluoroquinolone.", 14, ["Risk factors for resistant S. pneumoniae", "Beta lactam + macrolide", "OR respiratory fluoroquinolone (levofloxacin, moxifloxacin)"]),
  C(CAP, "Which outpatient pneumonia option suits a patient with beta-lactam allergy?", "A respiratory fluoroquinolone (levofloxacin or moxifloxacin).", 14, ["respiratory fluoroquinolone (levofloxacin, moxifloxacin)", "Good for patients with beta-lactam allergy"]),
  C(CAP, "How is inpatient pneumonia outside the intensive care unit treated?", "An intravenous beta-lactam plus a macrolide or doxycycline, or a respiratory fluoroquinolone.", 15, ["Non-ICU", "Intravenous beta-lactam", "PLUS intravenous/oral macrolide", "or doxycycline", "or respiratory fluoroquinolone (beta-lactam allergy)"]),
  C(CAP, "How does pneumonia treatment change in the intensive care unit?", "All treatment is intravenous; consider methicillin-resistant Staphylococcus aureus coverage.", 15, ["Same as above, but begin all IV treatment", "Consider MRSA coverage if warranted"]),
 ]),

 (HAP, "Nosocomial Pneumonia &amp; Its Antibiotics", "accent2", WIND_ICON, [
  C(HAP, "When does nosocomial pneumonia occur?", "More than 48 hours after hospital admission.", 16, ["Infection of lung not present at time of admission", "Occurring >48 hours after hospital admission"]),
  C(HAP, "How common is nosocomial pneumonia among hospital infections?", "The second most common, after urinary tract infection.", 16, ["Second most common infection in hospitalized patients (after UTI)"]),
  C(HAP, "Which patients have a higher incidence of nosocomial pneumonia?", "The elderly and mechanically ventilated patients.", 16, ["Higher incidence in elderly and mechanically ventilated patients"]),
  C(HAP, "Which patients meet the criteria for health-care associated pneumonia?", "Recent hospitalization, nursing home residence, recent intravenous antibiotics, chemotherapy, recent wound care or hemodialysis.", 17, ["Hospitalized in acute care facility > 2 days in past 90 days", "Nursing home/long term care facility", "Recent IV antibiotics", "Chemotherapy", "Wound care in previous 30 days", "Hemodialysis patient"]),
  C(HAP, "Which risk factors for nosocomial pneumonia are modifiable?", "Mechanical ventilation, nasogastric tube, histamine H2 blocker or antacid therapy, previous antibiotics, reintubation.", 18, ["Modifiable", "Mechanical ventilation, NG tube, ICP monitor, H-2 blocker or antacid therapy, previous antibiotic exposure, reintubation"]),
  C(HAP, "What is the most common gram-negative cause of nosocomial pneumonia?", "Pseudomonas aeruginosa.", 19, ["Gram-negative bacilli", "Pseudomonas aeruginosa (most common)"]),
  C(HAP, "What is the most common gram-positive cause of nosocomial pneumonia?", "Methicillin-resistant Staphylococcus aureus.", 19, ["Gram-positive cocci", "MRSA (most common)"]),
  C(HAP, "When should nosocomial pneumonia treatment start?", "As soon as possible, without waiting for a definitive culture.", 20, ["Start therapy as soon as possible", "don't wait on a definitive culture"]),
  C(HAP, "Which two organisms must broad-spectrum nosocomial coverage include?", "Methicillin-resistant Staphylococcus aureus and Pseudomonas.", 20, ["Must cover MRSA and pseudomonas"]),
  C(HAP, "What sends a suspected nosocomial pneumonia to broad-spectrum therapy?", "Late onset (5 days or more) or risk factors for multidrug-resistant pathogens.", 21, ["Late onset (>=5 days) or risk factors for MDR pathogens", "Broad-spectrum initial antibiotic therapy for MDR pathogens"]),
  C(HAP, "What are the limited-spectrum choices when there are no multidrug-resistant risk factors?", "Ceftriaxone, levofloxacin or moxifloxacin, ampicillin/sulbactam, or ertapenem.", 22, ["No risk factors for MDR pathogens", "Ceftriaxone (3rd gen. cephalosporin)", "OR levofloxacin, moxifloxacin", "OR ampicillin/sulbactam", "OR Ertapenem (narrow spectrum carbapenem)"]),
  C(HAP, "When are levofloxacin or moxifloxacin chosen for limited-spectrum coverage?", "When atypical pathogens are a worry.", 22, ["Choose this group if worried about atypical pathogens"]),
  C(HAP, "What does broad-spectrum nosocomial coverage combine?", "An antipseudomonal beta-lactam, plus a fluoroquinolone or aminoglycoside, plus vancomycin or linezolid.", 23, ["Gram negative combination therapy", "Antipseudomonal fluoroquinolone (levofloxacin, ciprofloxacin) OR", "Aminoglycoside", "PLUS gram positive coverage", "Vancomycin or linezolid"]),
  C(HAP, "Which antipseudomonal cephalosporin is fourth generation?", "Cefepime (Maxipime).", 24, ["Cefepime (Maxipime®)", "4th generation cephalosporin"]),
  C(HAP, "Which carbapenem needs caution in patients with a seizure history?", "Imipenem/cilastatin (Primaxin).", 25, ["Imipenem/cilistatin (Primaxin®)", "Use with caution in patients with seizure history"]),
  C(HAP, "Which carbapenem has limited activity against Pseudomonas aeruginosa?", "Ertapenem.", 25, ["Ertapenem has limited activity against P. aeruginosa"]),
  C(HAP, "What do the antipseudomonal fluoroquinolones cover well?", "The atypicals: Mycoplasma, Chlamydia and Legionella.", 27, ["Good activity against atypicals", "Mycoplasma, Chlamydia, Legionella"]),
  C(HAP, "Why are aminoglycosides given by extended-interval dosing in pneumonia?", "Poor lung penetration: bigger doses give higher concentrations.", 28, ["Utilize extended interval dosing (once daily or longer)", "Poor lung penetration", "bigger doses = higher conc."]),
  C(HAP, "Which toxicities do aminoglycosides cause?", "Ototoxicity and nephrotoxicity.", 28, ["Ototoxicity/nephrotoxicity"]),
  C(HAP, "When is the vancomycin trough drawn?", "Before the third or fourth dose, at steady state.", 29, ["Prior to 3rd-4th dose (Steady state)"]),
  C(HAP, "Which drug for methicillin-resistant Staphylococcus aureus needs no renal dose adjustment?", "Linezolid (Zyvox).", 30, ["Linezolid (Zyvox®)", "Great MRSA coverage", "No dose adjustment based on renal function"]),
  C(HAP, "What should happen to antibiotic coverage as cultures return?", "Scale it back, and switch to oral therapy when possible.", 31, ["Scale back antibiotic coverage as cultures are available", "Switch to PO when/if possible (cheaper)"]),
  C(HAP, "What are the three reasons pneumonia therapy fails?", "Wrong therapy, wrong diagnosis or complications.", 31, ["Failure of therapy", "Wrong therapy", "Wrong diagnosis", "Complications"]),
 ]),

 (TB, "Tuberculosis Drugs", "accent3", WIND_ICON, [
  C(TB, "What forms the waxy cell coat of mycobacteria?", "Mycolic acid, a distinct phosphoglycolipid layer.", 34, ["Distinct phosphoglycolipid layer (mycolic acid) forms waxy cell coat"]),
  C(TB, "Why do drugs that act on cell division work poorly against tuberculosis?", "It grows very slowly and can stay dormant for long periods.", 34, ["very slow growing, can exist in dormant states for long periods of time", "Antimicrobials that affect cell division don't work as well"]),
  C(TB, "What is the first phase of tuberculosis combination therapy?", "Isoniazid, rifampin, ethambutol and pyrazinamide for 2 months.", 35, ["Combination Therapy", "(2 month)", "Isoniazid", "Rifampin", "Ethambutol", "Pyrazinamide"]),
  C(TB, "What follows the first two months of tuberculosis therapy?", "Isoniazid and rifampin for 4 more months.", 35, ["Followed by (4 months)"]),
  C(TB, "Why are single agents never used in active tuberculosis?", "To prevent resistance from developing.", 36, ["Don't use single agents in active disease to prevent resistance development"]),
  C(TB, "What is the mechanism of isoniazid?", "It inhibits mycolic acid production, the waxy cell coat.", 37, ["Inhibits mycolic acid production", "Inhibits waxy cell coat"]),
  C(TB, "Is isoniazid bacteriostatic or bactericidal?", "Bacteriostatic for latent bacteria, bactericidal for dividing bacteria.", 37, ["Bacteriostatic for latent, bacteriocidal for dividing bacteria"]),
  C(TB, "What activates isoniazid?", "Bacterial catalase-peroxidase.", 38, ["Metabolically activated by bacterial catalase-perioxidase"]),
  C(TB, "When is isoniazid used alone?", "For prophylaxis.", 39, ["Prophylactic use", "used alone"]),
  C(TB, "What causes isoniazid peripheral neuritis, and how is it prevented?", "Pyridoxine deficiency; give pyridoxine (vitamin B6).", 39, ["Peripheral neuritis", "pyridoxine deficiency", "Give pyridoxine (B6)"]),
  C(TB, "In whom is isoniazid hepatitis more likely?", "In alcoholics, and it rises with age.", 39, ["Hepatitis", "in alcoholics and", "with age"]),
  C(TB, "What is the mechanism of rifampin?", "It inhibits bacterial DNA-dependent RNA polymerase.", 41, ["Inhibits DNA dependent RNA Polymerase", "no effect on human enzyme"]),
  C(TB, "Besides tuberculosis, what is rifampin used for?", "Meningococcal disease prophylaxis and endocarditis.", 41, ["Meningococcal disease  - prophylactic", "Endocarditis"]),
  C(TB, "What color does rifampin turn tears, sweat and urine?", "Orange.", 42, ["Secretions colored orange (tears, sweat, urine)"]),
  C(TB, "Which enzymes does rifampin induce?", "Cytochrome P450 enzymes, affecting anticoagulants, contraceptives, digoxin and theophylline.", 42, ["Induces P450 enzymes", "anticoagulants, contraceptives", "Digoxin", "Theophylline"]),
  C(TB, "What is the mechanism of ethambutol?", "It inhibits mycolic acid incorporation into membranes, weakening the cell wall.", 43, ["inhibits mycolic acid incorporation into membranes", "Weakened cell wall allows other agents better access"]),
  C(TB, "Which visual effects does ethambutol cause?", "Decreased red-green discrimination and decreased visual acuity.", 44, ["Visual disturbances", "Decreased red-green discrimination", "Decreased visual acuity"]),
  C(TB, "Why is the ethambutol dose adjusted in renal disease?", "Most of it is excreted unchanged.", 44, ["75% excreted unchanged, adjust dose in renal disease"]),
  C(TB, "What is pyrazinamide converted to, and what does that do?", "Pyrazinoic acid, which lowers the pH so bacteria cannot grow.", 45, ["Converted to Pyrazinic acid, lowers pH so bacteria can't grow"]),
  C(TB, "Why is pyrazinamide given for the first two months only?", "To avoid liver toxicity.", 45, ["Given first two months only, to avoid liver toxicity"]),
  C(TB, "What does pyrazinamide do to uric acid?", "It inhibits uric acid excretion; all patients become hyperuricemic.", 45, ["Inhibits uric acid excretion, all hyperuricemic"]),
 ]),

 (ANA, "Anaphylaxis Treatment", "accent4", WIND_ICON, [
  C(ANA, "What is anaphylaxis?", "A severe, systemic allergic reaction.", 48, ["Severe, systemic allergic reaction"]),
  C(ANA, "Which systems does anaphylaxis involve?", "The skin, airway, vascular system and gastrointestinal tract.", 48, ["Multisystem involvement, including the skin, airway, vascular system, and GI"]),
  C(ANA, "What can severe anaphylaxis cause?", "Complete airway obstruction, cardiovascular collapse and death.", 48, ["complete obstruction of the airway, cardiovascular collapse, and death"]),
  C(ANA, "Which fluid is used for volume expansion in anaphylaxis?", "Intravenous crystalloid: 0.9% sodium chloride.", 50, ["IV crystalloids (0.9% NaCl)"]),
  C(ANA, "Why are intravenous crystalloids given in anaphylaxis?", "For profound vasodilation and hypotension; they increase intravascular volume.", 50, ["For profound vasodilation/hypotension", "Increases intravascular volume"]),
  C(ANA, "Which receptors does epinephrine act on?", "Alpha and beta receptors.", 51, ["Acts on alpha and beta receptors"]),
  C(ANA, "What do epinephrine's alpha effects do in anaphylaxis?", "Vasoconstriction and decreased vascular permeability.", 51, ["Alpha effects", "Vasoconstriction, decreased vascular permeability"]),
  C(ANA, "What do epinephrine's beta effects do in anaphylaxis?", "Relax bronchial smooth muscle.", 51, ["Beta effects", "Bronchial smooth muscle relaxation"]),
  C(ANA, "Which skin findings does epinephrine alleviate?", "Pruritus, urticaria and angioedema.", 51, ["Alleviates pruritus, urticaria, and angioedema"]),
  C(ANA, "Which epinephrine route is generally preferred?", "Intramuscular, unless the patient is coding.", 52, ["IM generally preferred unless patient is coding"]),
  C(ANA, "What are the adverse effects of epinephrine?", "Anxiety, hypertension, tachycardia, nausea and vomiting, and diaphoresis.", 52, ["Adverse effects: anxiety, hypertension, tachycardia, N/V, diaphoresis"]),
  C(ANA, "What can an epinephrine overdose cause?", "Cerebrovascular hemorrhage, myocardial infarction and pulmonary edema.", 52, ["Overdose can lead to cerebrovascular hemorrhage, MI, pulmonary edema"]),
  C(ANA, "Which histamine H1 blockers are used in anaphylaxis?", "Diphenhydramine and hydroxyzine.", 53, ["H1 blockers: diphenhydramine, hydroxyzine"]),
  C(ANA, "What do histamine H1 blockers relieve in anaphylaxis?", "The cutaneous effects: rash, pruritus and hives.", 53, ["Relieves rash, pruritus, hives (cutaneous effects)"]),
  C(ANA, "What does the histamine H2 blocker famotidine block in anaphylaxis?", "The systemic (vasodilation) and gastrointestinal effects, such as increased gastric acid.", 53, ["H2 blockers: famotidine", "Blocks systemic (vasodilation) and GI effects (increased gastric acid secretion, etc.)"]),
  C(ANA, "What does albuterol do in anaphylaxis?", "As a beta-2 agonist, it relaxes bronchial smooth muscle.", 54, ["Albuterol", "Beta 2 agonist", "Relaxes bronchial smooth muscle"]),
  C(ANA, "What are albuterol's adverse effects?", "Anxiousness, tremor and tachycardia.", 54, ["Adverse effects: anxiousness, tremor, tachycardia"]),
  C(ANA, "How do corticosteroids work in anaphylaxis?", "They block production of inflammatory mediators at the cellular level.", 55, ["Blocks production of inflammatory mediators at the cellular level"]),
  C(ANA, "What is the drawback of corticosteroids in anaphylaxis?", "They take several hours to work.", 55, ["Takes time to work (several hours)"]),
  C(ANA, "Which corticosteroids are used in anaphylaxis?", "Methylprednisolone (intramuscular or intravenous) and prednisone.", 55, ["Methylprednisolone (IM, IV)", "Prednisone"]),
 ]),

 (BD, "Asthma &amp; the Bronchodilators", "accent5", WIND_ICON, [
  C(BD, "What characterizes asthma?", "Widespread reversible narrowing of the bronchial airways.", 57, ["Characterized by widespread reversible narrowing of the bronchial airways"]),
  C(BD, "What kind of inflammation marks asthma?", "Eosinophilic inflammation of the bronchial mucosa.", 57, ["eosinophilic inflammation of the bronchial mucosa"]),
  C(BD, "What are the symptoms of asthma?", "Shortness of breath, chest tightness, wheezing and coughing.", 57, ["Shortness of breath, chest tightness, wheezing, and coughing"]),
  C(BD, "What triggers most asthma attacks?", "Viral respiratory infection, not allergens.", 62, ["Most asthma attacks are not triggered by allergens", "Most triggered by viral respiratory infection"]),
  C(BD, "How is bronchial reactivity assessed?", "By the fall in forced expiratory volume in 1 second after inhaling increasing methacholine.", 62, ["Bronchial reactivity assessed by measuring the fall in forced expiratory volume over 1 second", "After inhaling increasing concentrations of methacholine"]),
  C(BD, "What are the three therapeutic approaches to asthma?", "Reverse bronchospasm, remove the trigger or antigen, and control inflammation.", 64, ["Reverse Bronchospasm", "Remove trigger or antigen", "Control Inflammation"]),
  C(BD, "Which asthma medications are quick relief medications?", "Short-acting beta-2 agonists, anticholinergics and systemic corticosteroids.", 67, ["Quick Relief Medications", "Short acting beta-2 agonists", "Anticholinergics", "Systemic corticosteroids"]),
  C(BD, "What do beta-2 agonists increase in airway smooth muscle?", "Cyclic adenosine monophosphate.", 68, ["Increase cyclic adenosine monophosphate (cAMP)", "Relax airway smooth muscle"]),
  C(BD, "Which enzyme does cyclic adenosine monophosphate inhibit to relax airway smooth muscle?", "Myosin light chain kinase.", 69, ["camp inhibits mlck (myosin light chain kinase)"]),
  C(BD, "How quickly do short-acting beta-2 agonists work, and how long do they last?", "They work rapidly and last 4 to 6 hours.", 68, ["Short-acting", "Work rapidly and last 4-6 hours"]),
  C(BD, "Which long-acting beta-2 agonists are listed?", "Formoterol (Foradil) and salmeterol (Serevent).", 70, ["Formoterol (Foradil)", "Salmeterol (Serevent)"]),
  C(BD, "What is the rule for long-acting beta-2 agonists in asthma?", "Never use them alone.", 70, ["Long acting (Do NOT use alone for asthma)"]),
  C(BD, "Which short-acting beta-2 agonist is sold as Xopenex?", "Levalbuterol.", 70, ["Levalbuterol (Xopenex®)"]),
  C(BD, "What are the adverse effects of beta-2 agonists?", "Tachycardia, hypotension, headache, dizziness, insomnia, tremors and hyperglycemia.", 71, ["Tachycardia", "Hypotension", "Headache", "Dizziness", "Insomnia", "Tremors", "Hyperglycemia"]),
  C(BD, "What kind of inhibitor are the methylxanthines?", "Nonspecific phosphodiesterase inhibitors.", 82, ["Nonspecific phosphodiesterase inhibitor"]),
  C(BD, "How does theophylline compare with long-acting bronchodilators?", "It is less effective and less well tolerated.", 82, ["Compared to long-acting bronchodilators", "Less effective", "Less well tolerated"]),
  C(BD, "Why are theophylline plasma levels monitored?", "It has a narrow therapeutic index.", [(82, ["Narrow therapeutic index"]), (85, ["Monitor Theophylline plasma levels"])]),
  C(BD, "Which receptor does theophylline antagonize?", "The adenosine A2B receptor.", 83, ["Adenosine receptor (A2B) antagonist"]),
  C(BD, "What is the intravenous form of theophylline?", "Aminophylline.", 82, ["Theophylline (Aminophylline IV)"]),
  C(BD, "How do anticholinergics cause bronchodilation?", "They block acetylcholine's effect on muscarinic receptors.", 86, ["Block acetylcholine's effect on muscarinic receptors"]),
  C(BD, "Which anticholinergic is short-acting, lasting up to 8 hours?", "Ipratropium (Atrovent).", 86, ["Last up to 8 hours", "Ipratropium (Atrovent®)"]),
  C(BD, "Which anticholinergic is long-acting, lasting 24 hours or more?", "Tiotropium (Spiriva).", 86, ["Last 24 hours or more", "Tiotropium (Spiriva®)"]),
  C(BD, "In the anticholinergic mnemonic, what does dry as a bone mean?", "Dry mouth and dry eyes.", 87, ["Dry as a bone (dry mouth, dry eyes)"]),
  C(BD, "In the anticholinergic mnemonic, what does the heart runs alone mean?", "Tachycardia and hypertension.", 87, ["And the heart runs alone (tachycardia, hypertension)"]),
 ]),

 (CTL, "Asthma Controllers: Steroids, Montelukast, Mast Cell Stabilizers &amp; Biologics", "accent1", WIND_ICON, [
  C(CTL, "Which asthma medications are long-term controller medications?", "Long-acting beta-2 agonists, inhaled corticosteroids, leukotriene modifiers, mast cell stabilizers, anti-immunoglobulin E antibody, methylxanthines.", 67, ["Long Term Controller Medications", "Long acting beta-2 agonists", "Inhaled corticosteroids", "Leukotriene modifiers", "Mast cell stabilizers", "Anti-IgE antibody", "Methylxanthines (theophylline)"]),
  C(CTL, "Which inhaled corticosteroid is sold as Flovent?", "Fluticasone.", 72, ["Fluticasone   (Flovent®)"]),
  C(CTL, "Which inhaled corticosteroid is sold as Pulmicort?", "Budesonide.", 72, ["Budesonide  (Pulmicort®)"]),
  C(CTL, "Which inhaled corticosteroid is sold as QVAR?", "Beclomethasone.", 72, ["Beclomethasone  (QVAR® )"]),
  C(CTL, "How long can inhaled corticosteroids take to reach maximal effect?", "Up to 8 weeks.", 73, ["Up to 8 weeks for maximal effects"]),
  C(CTL, "What are the adverse effects of inhaled corticosteroids?", "Oral thrush, growth suppression in children at high dose, and immune suppression.", 73, ["Oral candidiasis  (thrush)", "Suppress growth in children (high dose)", "Inhibit immune system (systemic action)"]),
  C(CTL, "What is in Advair?", "Salmeterol and fluticasone.", 74, ["Salmeterol/fluticasone", "Advair®"]),
  C(CTL, "What is in Symbicort?", "Formoterol and budesonide.", 74, ["Formoterol/budesonide", "Symbicort®"]),
  C(CTL, "What is in Dulera?", "Formoterol and mometasone.", 74, ["Formoterol/mometasone", "Dulera"]),
  C(CTL, "Which receptor does montelukast antagonize?", "The leukotriene D4 receptor (cysteinyl leukotriene 1 receptor).", 75, ["Montelukast", "LTD4 antagonist (cysLT1 receptor)"]),
  C(CTL, "What does the receptor montelukast blocks mediate?", "Inflammation, bronchial constriction and mucus secretion.", 75, ["receptor mediates inflammation, bronchial  constriction, mucous secretion"]),
  C(CTL, "In which kind of asthma is montelukast effective?", "Aspirin-induced asthma.", 75, ["Effective in Aspirin Induced asthma"]),
  C(CTL, "When must cromolyn and nedocromil be taken?", "Before the antigen insult.", 77, ["Must be taken before antigen insult"]),
  C(CTL, "What is the mechanism of cromolyn and nedocromil?", "Unknown; they may interfere with calcium.", 77, ["Mechanism unknown, (may interfere with Ca++)"]),
  C(CTL, "How long can the mast cell stabilizers take to work?", "Up to 4 weeks, and they must be taken regularly.", 78, ["May take up to 4 weeks to work; must be taken regularly"]),
  C(CTL, "What kind of drug is omalizumab?", "A recombinant humanized monoclonal antibody against immunoglobulin E.", 79, ["Omalizumab (Xolair®)", "Recombinant DNA derived humanized IgE monoclonal antibody"]),
  C(CTL, "How does omalizumab prevent mast cell degranulation?", "It binds circulating immunoglobulin E, decreasing high-affinity receptors on mast cells.", 79, ["Binds circulating IgE which decreases high affinity receptors on mast cells, prevents degranulation"]),
  C(CTL, "What are the adverse effects of omalizumab?", "Gastrointestinal upset, anaphylaxis, neutralizing antibodies and secondary malignancies.", 79, ["GI disturbances", "Anaphylaxis", "May develop neutralizing antibodies", "Secondary Malignancies"]),
  C(CTL, "Which asthma phenotype are the anti-interleukin-5 and anti-interleukin-4 biologics for?", "The eosinophilic phenotype.", 81, ["Used for eosinophilic phenotype"]),
  C(CTL, "What kind of target do the biologics for eosinophilic asthma block?", "Interleukins (interleukin-5 or interleukin-4), not immunoglobulin E.", 81, ["Anti-IL-5", "Anti-IL-4", "Used for eosinophilic phenotype"]),
  C(CTL, "Which anti-interleukin-5 biologic is given intravenously?", "Reslizumab (Cinqair).", 81, ["Resilzumab (Cinqair)", "Given IV"]),
  C(CTL, "Why are oral systemic corticosteroids of limited use in asthma?", "They are the most potent but have side effects; they are used for exacerbations.", 88, ["Most potent but limited use due to side effects", "Used in asthma exacerbations"]),
  C(CTL, "Which systemic corticosteroid is an oral liquid?", "Prednisolone (Ora-Pred).", 88, ["Prednisolone (Ora-Pred) - oral liquid"]),
  C(CTL, "What are the side effects of systemic corticosteroids?", "Adrenal and growth suppression, dermal thinning, hypertension, hyperglycemia, mood change, myopathy and immunosuppression.", 89, ["Adrenal suppression", "Growth suppression", "Dermal thinning", "Hypertension", "Hyperglycemia", "Altered mood/mental status", "Muscle weakness (steroid myopathy)", "Immunosuppression"]),
 ]),

 (INH, "Asthma Steps, Inhaler Devices &amp; Status Asthmaticus", "accent2", WIND_ICON, [
  C(INH, "What is the preferred reliever in stepwise asthma therapy?", "As-needed low-dose inhaled corticosteroid with formoterol.", 90, ["Preferred reliever: As-needed low-dose ICS-formoterol"]),
  C(INH, "What is the other reliever option in stepwise asthma therapy?", "An as-needed short-acting beta-2 agonist.", 90, ["Other reliever option: As-needed SABA"]),
  C(INH, "Daily low-dose inhaled corticosteroid is not enough. What is the next preferred controller?", "Low-dose inhaled corticosteroid with a long-acting beta-2 agonist.", 90, ["Step 2 Daily low-dose ICS", "Step 3 Low-dose ICS-LABA"]),
  C(INH, "Low-dose inhaled corticosteroid with a long-acting beta-2 agonist is not enough. What comes next?", "The same combination at medium dose.", 90, ["Step 3 Low-dose ICS-LABA", "Step 4 Medium-dose ICS-LABA"]),
  C(INH, "What does the top step add beyond high-dose inhaled corticosteroid with a long-acting beta-2 agonist?", "Referral for phenotypic assessment, with or without add-on therapy.", 90, ["Step 5 High-dose ICS-LABA, Refer for phenotypic assessment"]),
  C(INH, "How does a nebulizer deliver medication?", "A compressor forces liquid medication into a fine mist for passive inhalation.", 92, ["Compressor forces liquid medication into a fine mist", "Allows for passive inhalation of medications"]),
  C(INH, "Who benefits most from a nebulizer?", "Children and elderly patients who cannot use a metered dose inhaler.", 92, ["Good for children, elderly who can't use MDI"]),
  C(INH, "What is the drawback of the bigger nebulizer dose?", "It may lead to more side effects.", 92, ["Bigger dose is administered overall", "May lead to more side effects"]),
  C(INH, "How does a dry powder inhaler deliver its drug?", "The patient's own inspiratory force draws the powder out of the device.", 93, ["Medication in powder form", "Patients provide inspiratory force to draw medications out of device"]),
  C(INH, "Who should not use a dry powder inhaler?", "Patients with poor inspiratory capacity.", 93, ["Not good for patients who have poor inspiratory capacity"]),
  C(INH, "Which inhaler device requires the most coordination?", "The metered dose inhaler.", 94, ["Metered dose inhalers", "Requires most coordination for proper use"]),
  C(INH, "What is a spacer for?", "Holding the medication for patients with poor coordination.", 94, ["Spacers used to hold medication for patients with poor coordination"]),
  C(INH, "How does a valve holding chamber differ from a plain spacer?", "Its one-way valves stop the patient from exhaling into the device.", 95, ["Have one way valves that do not allow the patient to exhale into the device"]),
  C(INH, "What do spacers and valve holding chambers retain?", "Large particles, leaving a higher proportion of small, respirable particles.", 95, ["Intended to retain large particles emitted from the inhaler", "Higher proportion of smaller, respirable particles"]),
  C(INH, "What are the first steps of metered dose inhaler technique?", "Take off the cap, shake (prime if needed), then breathe out all the way.", 96, ["Take off cap and shake inhaler (may need to be primed)", "Breathe out all the way"]),
  C(INH, "When is the inhaler pressed during a metered dose inhaler breath?", "As you start breathing in slowly.", 97, ["Start breathing in slowly as you press down on inhaler"]),
  C(INH, "With a holding chamber, how soon after pressing should the patient breathe in?", "Within 5 seconds.", 97, ["With a holding chamber, first press down on inhaler and then begin breathing within 5 seconds"]),
  C(INH, "How long should the patient hold the breath after an inhaled dose?", "For 10 seconds, or as long as comfortable.", 97, ["Hold your breath for 10 seconds or as long as comfortable"]),
  C(INH, "How long should a patient wait between puffs of a quick-relief beta-2 agonist?", "Wait 15 to 30 seconds between puffs.", 97, ["For inhaled quick relief medicines (beta-2 agonists), wait 15-30 seconds between puffs"]),
  C(INH, "What does excessive albuterol use indicate?", "Poor control and a need to adjust long-term therapy.", 98, ["Excessive use indicates poor control and need for adjustment in long-term therapy"]),
  C(INH, "What is status asthmaticus?", "An acute exacerbation that stays unresponsive to initial bronchodilator treatment; a medical emergency.", 99, ["Medical emergency", "acute exacerbation that remains unresponsive to initial bronchodilator treatment"]),
  C(INH, "Which drugs make up the status asthmaticus algorithm?", "Continuous nebulized albuterol, intravenous steroids, magnesium, and ketamine if intubated.", 99, ["Continuous albuterol", "nebulized", "Steroids (IV preferred)", "Magnesium (bolus followed by continuous infusion)", "Ketamine (if intubated)"]),
  C(INH, "How does ketamine produce bronchodilation?", "It increases catecholamine release.", 99, ["Increases catecholamine release"]),
  C(INH, "What are ketamine's adverse reactions?", "Emergence phenomenon, hypertension, tachycardia and vomiting.", 99, ["ADR: emergence phenomenon, hypertension, tachycardia, vomiting"]),
 ]),

 (COPD, "Chronic Obstructive Pulmonary Disease &amp; Smoking Cessation", "accent3", WIND_ICON, [
  C(COPD, "What is chronic obstructive pulmonary disease?", "Chronic inflammation of the airways and lung parenchyma, generally not fully reversible.", 101, ["Chronic inflammation of airways and lung parenchyma", "generally not fully reversible"]),
  C(COPD, "What happens to forced expiratory volume in 1 second in chronic obstructive pulmonary disease?", "It declines at an accelerated rate.", 101, ["Accelerated decline in FEV1"]),
  C(COPD, "When do symptoms of chronic obstructive pulmonary disease appear?", "Only after a significant decline in forced expiratory volume in 1 second.", 101, ["Symptoms generally develop only after a significant decline in forced expiratory volume in one second (FEV1) has occurred"]),
  C(COPD, "What does every chronic obstructive pulmonary disease group receive?", "Risk-factor avoidance, influenza and pneumococcal vaccines, activity, inhaler-technique review, rehabilitation, oxygen if hypoxemic.", 102, ["Avoidance of risk factor(s), such as smoking", "Annual influenza vaccination", "Pneumococcal vaccination", "Regular review/correction of inhaler technique", "Long-term oxygen therapy if chronic hypoxemia", "Pulmonary rehabilitation"]),
  C(COPD, "What is the treatment for chronic obstructive pulmonary disease group A?", "A short-acting bronchodilator, as needed.", 102, ["Short-acting bronchodilator (SABA, SAMA, or combination of SABA-SAMA), as needed."]),
  C(COPD, "What is the treatment for chronic obstructive pulmonary disease group B?", "A regular long-acting bronchodilator: a muscarinic antagonist or a beta-2 agonist.", 102, ["Regular treatment with a long-acting bronchodilator, either LAMA or LABA"]),
  C(COPD, "What is the treatment for chronic obstructive pulmonary disease group C?", "A regular long-acting muscarinic antagonist, with a short-acting beta-2 agonist for relief.", 102, ["Regular treatment with a LAMA; SABA available for symptom relief as needed."]),
  C(COPD, "What does group D get when breathlessness is severe?", "A long-acting beta-2 agonist plus a long-acting muscarinic antagonist.", 102, ["if severe breathlessness (eg, CAT >20), combination LABA plus LAMA"]),
  C(COPD, "When may a combination glucocorticoid inhaler be preferred in group D?", "When features of asthma and chronic obstructive pulmonary disease overlap.", 102, ["Combination glucocorticoid-LABA inhaler may be preferred, if features of asthma/COPD overlap"]),
  C(COPD, "What is the major contributor to chronic obstructive pulmonary disease?", "Smoking.", 103, ["Smoking - a major contributor to COPD"]),
  C(COPD, "What does smoking cessation do to the decline in ventilatory function?", "It can return it to the normal age-related rate.", 103, ["Can result in return to the normal age-related rate of decline in ventilatory function"]),
  C(COPD, "What should an effective smoking cessation program combine?", "Pharmacologic intervention with counseling.", 103, ["Effective programs should combine pharmacologic intervention with counseling"]),
  C(COPD, "What correlates with success at quitting smoking?", "The intensity and frequency of counseling.", 103, ["Intensity and frequency of counseling directly correlates with the success of quitting"]),
  C(COPD, "How is bupropion thought to aid smoking cessation?", "It inhibits norepinephrine and dopamine uptake, mimicking nicotine's effects.", 105, ["postulated that bupropion mimics these effects because it inhibits the uptake of norepinephrine and dopamine"]),
  C(COPD, "In whom should bupropion be avoided?", "Patients with seizure disorders and patients taking monoamine oxidase inhibitors.", 105, ["patients with seizure disorders", "patients taking MAOIs"]),
  C(COPD, "What does nicotine replacement do?", "Reduces the craving to smoke and minimizes physical withdrawal.", 106, ["Reduces craving to smoke, minimize physical withdrawal"]),
  C(COPD, "Which nicotine replacement products are available over the counter?", "Patches and gum.", 106, ["Patches and Gum are available OTC"]),
  C(COPD, "Why is nicotine replacement used with caution in cardiovascular disease?", "Because of the chance of tachyarrhythmias and hypertension.", 106, ["Caution in patients with cardiovascular problems due to chance of tachyarrhythmias and hypertension"]),
  C(COPD, "What is the mechanism of varenicline?", "A partial nicotine receptor agonist, acting to a lesser degree than nicotine.", 107, ["partial nicotine receptor agonist (lesser degree than nicotine)"]),
  C(COPD, "When is varenicline started and how long is it continued?", "One week before the quit date, continued for 12 weeks.", 107, ["start one week before quit date and continue for 12 weeks"]),
  C(COPD, "Which black box warning is listed for varenicline?", "Neuropsychiatric events: depression and suicidal ideation.", 107, ["Black box warning: neuropsychiatric events (depression, suicidal ideations)"]),
  C(COPD, "Which vaccines should patients with chronic obstructive pulmonary disease receive?", "The annual influenza vaccine and the pneumococcal vaccine.", 108, ["Annual influenza vaccination is highly recommended in these patients", "Should also receive the pneumococcal vaccine"]),
 ]),
]
