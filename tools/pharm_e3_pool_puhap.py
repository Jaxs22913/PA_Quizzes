# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Drugs for Pulmonary Infections, Asthma and COPD (Lecture 11), topic: nosocomial pneumonia
and its antibiotics.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. The key is authored FIRST (c == 0);
pharm_e3_partition.py rotates it (numeric option sets are sorted ascending instead, WRITER.md rule 8).

SOURCE. Pulmonology-2.pptx slides 16-31: nosocomial pneumonia (16), health-care associated pneumonia criteria (17), risk
factors (18), etiology (19), treatment principles (20), the hospital-acquired pneumonia algorithm (21, a picture read by
eye into tools/pharm_e3/ocr.json), limited-spectrum (22) and broad-spectrum (23) empiric coverage, antipseudomonal
cephalosporins (24), carbapenems (25), penicillins (26) and fluoroquinolones (27), aminoglycosides (28), vancomycin
(29), linezolid (30) and further therapy (31). The deck has no speaker notes.

WRITER.md v1 (2026-10-15): every distractor carries its misconception as a third element (mis); slides only; slides win
on conflict. Shared keying decisions: scratchpad L11_KEYING.md (copied into the guide's notes).

HEALTH-CARE ASSOCIATED PNEUMONIA is asked only as the deck's own category (slide 17 criteria, slide 21 algorithm); the
2016 guidelines dropped it, and the study guide says so.

LEFT OUT ON PURPOSE:
  * every dose and the vancomycin trough NUMBER (slide 29; current guidance uses area-under-the-curve dosing): only the
    timing of the trough (before the 3rd-4th dose, steady state) is asked;
  * (changed by the recording pass) ceftazidime "not recommended due to rapid development of resistance" (slide 24) is
    asked ONCE, because Dr. Wood affirmed it aloud; current guidance still lists it, and the guide says so;
  * ticarcillin/clavulanate (slide 26; no longer marketed in the US): no item is built on choosing it;
  * treatment duration 7-8 days / 10-14 for Pseudomonas and others (slide 31; current guidance differs);
  * "Must cover MRSA and pseudomonas" (slide 20) as a universal rule: slides 21-22 give a limited-spectrum regimen that
    is not built to cover them when there are no multidrug-resistant risk factors, so coverage is asked only with risk factors;
  * the HCAP time windows (more than 2 days in the past 90 days, wound care within 30 days) as numeric keys;
  * the fungal pathogens (Candida, Aspergillus) as a key (recognition trivia; used in explanations only);
  * the rank "second most common infection" as a bare ordinal is asked once, framed against urinary tract infection.
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


T_NP = "Nosocomial pneumonia basics"
T_RF = "Nosocomial risk factors"
T_EMP = "Empiric coverage"
T_AP = "Antipseudomonal agents"
T_AGV = "Aminoglycosides and vancomycin"
T_LZ = "Linezolid and further therapy"

QUESTIONS = [

# ---- nosocomial pneumonia basics (slides 16, 19, 20) ---------------------------------------------
Q(T_NP, IO_IND, "physiology",
  "A patient admitted for a hip fracture develops a new pneumonia on hospital day 4; it was not present on admission. How is this pneumonia classified?",
  [["Hospital-acquired pneumonia", "Correct. Nosocomial pneumonia is a lung infection not present at admission and occurring more than 48 hours after admission; it includes hospital-acquired pneumonia."],
   ["Community-acquired pneumonia", "Pneumonia that was not present at admission and begins more than 48 hours into the stay is nosocomial, not community-acquired.", RULED],
   ["Ventilator-associated pneumonia", "Ventilator-associated pneumonia is one nosocomial type, but nothing in this case involves mechanical ventilation; this is hospital-acquired pneumonia.", RULED],
   ["Acute bronchitis", "Acute bronchitis is inflammation of the bronchi that spares the bronchioles and alveoli; a new pneumonia after 48 hours in hospital is nosocomial.", COMP]], 16),

Q(T_NP, IO_IND, "physiology",
  "How does nosocomial pneumonia rank among infections in hospitalized patients?",
  [["Second, after urinary tract infection", "Correct. Nosocomial pneumonia is the second most common infection in hospitalized patients, after urinary tract infection, with higher mortality and costs."],
   ["First, ahead of urinary tract infection", "Urinary tract infection is the more common one; nosocomial pneumonia ranks second, after it.", REV],
   ["Second, after wound infection", "Wound infection is not the comparison given; nosocomial pneumonia is second most common, after urinary tract infection.", ADJ],
   ["Third, after urinary and wound infection", "Nosocomial pneumonia ranks second, not third; the only infection more common in hospitalized patients is urinary tract infection.", REV]], 16),

Q(T_NP, IO_IND, "physiology",
  "Which hospitalized group has a higher incidence of nosocomial pneumonia?",
  [["Mechanically ventilated patients", "Correct. Nosocomial pneumonia has a higher incidence in elderly and mechanically ventilated patients, with higher mortality and hospital costs."],
   ["Young adults after minor surgery", "Youth is not a stated risk; the groups with higher incidence are the elderly and mechanically ventilated patients.", REV],
   ["Patients with recent acute bronchitis", "Recent bronchitis is not a listed risk; the higher incidence is in elderly and mechanically ventilated patients.", ADJ],
   ["Patients discharged within one day", "Nosocomial pneumonia arises more than 48 hours after admission, so a stay under a day is not a risk group; the higher incidence is in elderly and mechanically ventilated patients.", REV]], 16),

Q(T_NP, IO_IND, "physiology",
  "Which gram-negative bacillus is the most common cause of nosocomial pneumonia?",
  [["Pseudomonas aeruginosa", "Correct. Pseudomonas aeruginosa is the most common gram-negative bacillus, and the list also names Escherichia coli, Klebsiella pneumoniae, Acinetobacter, Enterobacter and Serratia; methicillin-resistant Staphylococcus aureus is the most common gram-positive coccus."],
   ["Escherichia coli", "Escherichia coli is on the gram-negative list, but Pseudomonas aeruginosa is the most common gram-negative cause.", ADJ],
   ["Klebsiella pneumoniae", "Klebsiella pneumoniae is listed among the gram-negative bacilli, but Pseudomonas aeruginosa is the most common.", ADJ],
   ["Acinetobacter species", "Acinetobacter is a listed gram-negative bacillus, but the most common gram-negative cause is Pseudomonas aeruginosa.", ADJ]], 19),

Q(T_NP, IO_PROT, "protocol",
  "When should antibiotic therapy for suspected nosocomial pneumonia begin?",
  [["As soon as possible", "Correct. Therapy starts as soon as possible, without waiting on a definitive culture, with broad-spectrum antibiotics that consider multidrug-resistant pathogens."],
   ["After culture results return", "Waiting is exactly what is advised against: therapy starts as soon as possible, without waiting on a definitive culture.", STAGE],
   ["After the sputum gram stain", "A gram stain is not a gate to treatment; therapy for nosocomial pneumonia starts as soon as possible.", STAGE],
   ["After 48 hours of observation", "Forty-eight hours after admission defines nosocomial pneumonia; once it is suspected, therapy starts as soon as possible.", ADJ]], 20),

Q(T_NP, IO_PROT, "protocol",
  "What should happen to empiric nosocomial pneumonia therapy once cultures and sensitivities return?",
  [["Narrow it to the culture results", "Correct. Therapy is streamlined once cultures and sensitivities are available, scaling back antibiotic coverage as the cultures return."],
   ["Keep the full empiric regimen", "Broad empiric coverage is meant to be streamlined; once cultures and sensitivities are available, coverage is scaled back.", STAGE],
   ["Broaden it to cover fungi", "Candida and Aspergillus are listed pathogens, but the rule when cultures return is to streamline therapy, not broaden it.", REV],
   ["Add a second gram-positive drug", "Vancomycin or linezolid is the single gram-positive agent in broad coverage; when cultures return, therapy is streamlined.", REV]], 20),

# ---- risk factors and categories (slides 17, 18, 21) ---------------------------------------------
Q(T_RF, IO_IND, "physiology",
  "Which history meets a listed criterion for health-care associated pneumonia?",
  [["Outpatient hemodialysis", "Correct. Health-care associated pneumonia criteria include hemodialysis, nursing home residence, recent intravenous antibiotics, chemotherapy, wound care in the previous 30 days and a recent hospital stay."],
   ["Wound care six months ago", "Wound care counts only within the previous 30 days; six months ago falls outside the criterion.", REV],
   ["A hospital stay last year", "A hospital stay counts when it was more than 2 days in an acute care facility within the past 90 days, not a year ago.", REV],
   ["A child in day care at home", "Exposure to a child in day care is a risk factor for penicillin-resistant Streptococcus pneumoniae, not a health-care associated pneumonia criterion.", ADJ]], 17),

Q(T_RF, IO_IND, "physiology",
  "Which risk factor for nosocomial pneumonia is modifiable?",
  [["A nasogastric tube", "Correct. Modifiable risk factors are mechanical ventilation, a nasogastric tube, an intracranial pressure monitor, histamine H2 blocker or antacid therapy, previous antibiotics and reintubation."],
   ["Chronic lung disease", "Chronic lung disease is listed as an unmodifiable risk factor, along with age over 70 and depressed consciousness.", REV],
   ["Age over 70 years", "Age over 70 is an unmodifiable risk factor; a nasogastric tube is one of the modifiable ones.", REV],
   ["Depressed consciousness", "Depressed consciousness is listed as unmodifiable; the modifiable list includes devices such as a nasogastric tube.", REV]], 18),

Q(T_RF, IO_IND, "physiology",
  "A hospitalized patient carries several risks for pneumonia. Which of them is one that cannot be changed?",
  [["Hospitalization in winter", "Correct. Unmodifiable risk factors are age over 70, chronic lung disease, depressed consciousness, large-volume aspiration and hospitalization during the winter months."],
   ["Histamine H2 blocker therapy", "Histamine H2 blocker or antacid therapy is a modifiable risk factor, since the therapy can be changed.", REV],
   ["Reintubation", "Reintubation is listed among the modifiable risk factors, with mechanical ventilation and a nasogastric tube.", REV],
   ["An intracranial pressure monitor", "An intracranial pressure monitor is a modifiable risk factor; hospitalization during the winter months is unmodifiable.", REV]], 18),

Q(T_RF, IO_AE, "adverse effect",
  "Which drug's use is a modifiable risk factor for nosocomial pneumonia?",
  [["Famotidine", "Correct. Histamine H2 blocker or antacid therapy is a modifiable risk factor for nosocomial pneumonia, and famotidine is a histamine H2 blocker."],
   ["Albuterol", "Albuterol, a beta-2 agonist bronchodilator, is not on the risk list; the drug therapies listed are histamine H2 blockers or antacids and previous antibiotics.", ADJ],
   ["Montelukast", "Montelukast, a leukotriene receptor antagonist, is not a listed risk factor; histamine H2 blockers such as famotidine are.", ADJ],
   ["Cromolyn sodium", "Cromolyn, a mast cell stabilizer, is not a listed risk factor; histamine H2 blocker or antacid therapy is.", ADJ]], 18),

Q(T_RF, IO_PROT, "protocol",
  "Which history counts as a risk factor for multidrug-resistant pathogens in hospital-acquired pneumonia?",
  [["Immunosuppressive therapy", "Correct. Risk factors for multidrug-resistant pathogens are prior antibiotics, colonization, hospitalization or chronic care, and immunosuppressive disease or therapy."],
   ["Hospitalization in winter", "Winter hospitalization is an unmodifiable risk factor for nosocomial pneumonia itself, not a listed risk factor for multidrug-resistant pathogens.", ADJ],
   ["Depressed consciousness", "Depressed consciousness raises the risk of nosocomial pneumonia, but it is not among the multidrug-resistant risk factors in the algorithm.", ADJ],
   ["Large-volume aspiration", "Large-volume aspiration is an unmodifiable risk factor for nosocomial pneumonia, not one of the multidrug-resistant risk factors.", ADJ]], 21),

Q(T_RF, IO_PROT, "drug choice",
  "A patient develops hospital-acquired pneumonia on hospital day 3 and has no risk factors for multidrug-resistant pathogens. Which initial approach fits?",
  [["Limited-spectrum therapy", "Correct. With early onset (under 5 days) and no multidrug-resistant risk factors, limited-spectrum initial antibiotic therapy is chosen."],
   ["Broad-spectrum therapy", "Broad-spectrum therapy for multidrug-resistant pathogens is for late onset (5 days or more) or multidrug-resistant risk factors, neither present here.", RULED],
   ["Await the sputum culture", "Treatment is not delayed for a culture: therapy starts as soon as possible, here with limited-spectrum antibiotics.", STAGE],
   ["Supportive care alone", "Supportive care alone is for acute bronchitis; hospital-acquired pneumonia is treated at once, here with limited-spectrum therapy.", COMP]], 21),

Q(T_RF, IO_PROT, "drug choice",
  "A patient develops hospital-acquired pneumonia on hospital day 7 and has no other risk factors for multidrug-resistant pathogens. Which initial approach fits?",
  [["Broad-spectrum therapy", "Correct. Late onset, 5 days or more, is enough on its own to call for broad-spectrum initial antibiotic therapy for multidrug-resistant pathogens."],
   ["Limited-spectrum therapy", "Limited-spectrum therapy requires both early onset and no multidrug-resistant risk factors; onset on day 7 is late.", RULED],
   ["Await the sputum culture", "Therapy starts as soon as possible without waiting on a culture, and late onset calls for broad-spectrum coverage.", STAGE],
   ["Supportive care alone", "Supportive care alone is the approach to acute bronchitis; late-onset hospital-acquired pneumonia needs broad-spectrum antibiotics.", COMP]], 21),

# ---- empiric coverage (slides 22-23) -------------------------------------------------------------
Q(T_EMP, IO_IND, "drug choice",
  "Which drug is a limited-spectrum empiric choice for nosocomial pneumonia without multidrug-resistant risk factors?",
  [["Ceftriaxone", "Correct. Limited-spectrum coverage is ceftriaxone, or levofloxacin or moxifloxacin, or ampicillin-sulbactam, or ertapenem."],
   ["Cefepime", "Cefepime is an antipseudomonal cephalosporin, part of broad-spectrum coverage for multidrug-resistant risk; ceftriaxone is the limited-spectrum cephalosporin.", STAGE],
   ["Meropenem", "Meropenem is an antipseudomonal carbapenem used for broad coverage; the limited-spectrum carbapenem is ertapenem.", STAGE],
   ["Vancomycin", "Vancomycin is the gram-positive add-on in broad-spectrum coverage; without multidrug-resistant risk factors, a limited agent such as ceftriaxone is used.", STAGE]], 22),

Q(T_EMP, IO_IND, "drug choice",
  "In limited-spectrum coverage for nosocomial pneumonia, which drug is chosen when atypical pathogens are a concern?",
  [["Levofloxacin", "Correct. Levofloxacin or moxifloxacin is the limited-spectrum choice when atypical pathogens are a worry; fluoroquinolones have good activity against Mycoplasma, Chlamydia and Legionella."],
   ["Ceftriaxone", "Ceftriaxone is a limited-spectrum option, but the group to choose when atypical pathogens are a worry is levofloxacin or moxifloxacin.", ADJ],
   ["Ampicillin-sulbactam", "Ampicillin-sulbactam is a limited-spectrum option, but the fluoroquinolones are the group chosen for atypical pathogens.", ADJ],
   ["Ertapenem", "Ertapenem is a narrow-spectrum carbapenem option; when atypical pathogens are a worry, levofloxacin or moxifloxacin is chosen.", ADJ]], 22),

Q(T_EMP, IO_CLASS, "class",
  "Why is ertapenem a limited-spectrum choice rather than a broad one in nosocomial pneumonia?",
  [["Limited activity against Pseudomonas", "Correct. Ertapenem is a narrow-spectrum carbapenem with limited activity against Pseudomonas aeruginosa, so it belongs to limited-spectrum coverage."],
   ["Rapid development of resistance", "Rapid development of resistance is the concern raised about ceftazidime, not ertapenem; ertapenem is limited by weak Pseudomonas activity.", ADJ],
   ["Poor penetration into lung tissue", "Poor lung penetration is the aminoglycoside problem; ertapenem is limited-spectrum because of its weak activity against Pseudomonas aeruginosa.", ADJ],
   ["A high risk of seizures", "Seizure caution belongs to imipenem-cilastatin; ertapenem is limited-spectrum because of its weak activity against Pseudomonas aeruginosa.", ADJ]], 25),

Q(T_EMP, IO_IND, "drug choice",
  "For broad-spectrum empiric coverage of nosocomial pneumonia, which drugs supply the gram-positive coverage added to the gram-negative combination?",
  [["Vancomycin or linezolid", "Correct. Broad coverage is gram-negative combination therapy plus gram-positive coverage with vancomycin or linezolid, for methicillin-resistant Staphylococcus aureus."],
   ["Ceftriaxone or ertapenem", "Ceftriaxone and ertapenem are limited-spectrum options for patients without multidrug-resistant risk; the gram-positive add-on is vancomycin or linezolid.", STAGE],
   ["Gentamicin or tobramycin", "Aminoglycosides are a second gram-negative agent in the combination, not the gram-positive coverage, which is vancomycin or linezolid.", MECH],
   ["Azithromycin or doxycycline", "Azithromycin or doxycycline partners a beta-lactam in community-acquired pneumonia; the nosocomial gram-positive add-on is vancomycin or linezolid.", ADJ]], 23),

Q(T_EMP, IO_IND, "drug choice",
  "In broad-spectrum coverage, an antipseudomonal beta-lactam is paired with which second gram-negative agent?",
  [["Ciprofloxacin", "Correct. The antipseudomonal beta-lactam is combined with an antipseudomonal fluoroquinolone (levofloxacin or ciprofloxacin) or an aminoglycoside."],
   ["Moxifloxacin", "Moxifloxacin is listed in the limited-spectrum group; the antipseudomonal fluoroquinolones for the combination are levofloxacin and ciprofloxacin.", ADJ],
   ["Ceftriaxone", "Ceftriaxone is a limited-spectrum cephalosporin, not an antipseudomonal partner; the second gram-negative agent is an antipseudomonal fluoroquinolone or an aminoglycoside.", STAGE],
   ["Linezolid", "Linezolid is gram-positive coverage for methicillin-resistant Staphylococcus aureus, not a second gram-negative agent.", MECH]], 23),

Q(T_EMP, IO_IND, "drug choice",
  "Which regimen fits broad-spectrum empiric coverage for nosocomial pneumonia with risk factors for multidrug-resistant pathogens?",
  [["Cefepime, tobramycin and vancomycin", "Correct. Broad coverage is an antipseudomonal beta-lactam (cefepime) plus an antipseudomonal fluoroquinolone or aminoglycoside (tobramycin) plus vancomycin or linezolid."],
   ["Meropenem and ciprofloxacin", "This covers gram-negative organisms twice but leaves out the gram-positive agent, vancomycin or linezolid, that broad coverage requires.", RULED],
   ["Ceftriaxone and azithromycin", "A beta-lactam plus a macrolide is community-acquired pneumonia treatment; it lacks antipseudomonal and methicillin-resistant Staphylococcus aureus coverage.", ADJ],
   ["Ertapenem, levofloxacin and linezolid", "Ertapenem has limited Pseudomonas activity, so it cannot be the antipseudomonal beta-lactam of a broad regimen.", RULED]], 23),

# Dr. Wood, 18:41-18:50 and 22:56-24:27: "There will be a question like this on the test": a list of drug names, name
# each one's class, then judge whether the regimen is valid (slide 23). The items below use their own drug combinations.
Q(T_EMP, IO_IND, "drug choice",
  "A patient on a ventilator develops pneumonia and has risk factors for multidrug-resistant pathogens. Which empiric regimen is appropriate?",
  [["Meropenem, gentamicin and linezolid", "Correct. Meropenem is an antipseudomonal carbapenem, gentamicin an aminoglycoside as the second gram-negative agent, and linezolid the gram-positive coverage."],
   ["Imipenem-cilastatin, cefepime and vancomycin", "Imipenem-cilastatin and cefepime are both antipseudomonal beta-lactams; the second gram-negative agent must be a fluoroquinolone or an aminoglycoside.", MECH],
   ["Vancomycin, linezolid and ciprofloxacin", "Vancomycin and linezolid both cover methicillin-resistant Staphylococcus aureus (MRSA), leaving one gram-negative agent where two are needed.", RULED],
   ["Ceftriaxone, tobramycin and vancomycin", "Ceftriaxone is a limited-spectrum third-generation cephalosporin, not antipseudomonal; the beta-lactam must be antipseudomonal.", STAGE]], 23),

Q(T_EMP, IO_PROT, "drug choice",
  "A proposed empiric regimen for nosocomial pneumonia with multidrug-resistant risk factors is cefepime, piperacillin-tazobactam and vancomycin. What makes it inappropriate?",
  [["It pairs two beta-lactam antibiotics", "Correct. Cefepime and piperacillin-tazobactam are both antipseudomonal beta-lactams; the partner must be an antipseudomonal fluoroquinolone or an aminoglycoside."],
   ["It has no gram-positive coverage", "Vancomycin is in the regimen and is the usual methicillin-resistant Staphylococcus aureus (MRSA) coverage; the flaw is two beta-lactams together.", RULED],
   ["It has no antipseudomonal drug in it", "Cefepime and piperacillin-tazobactam are both antipseudomonal; the problem is that both are beta-lactams, so a fluoroquinolone or aminoglycoside is missing.", RULED],
   ["It needs linezolid in place of vancomycin", "Vancomycin or linezolid is equally acceptable as the gram-positive drug; the regimen fails because it pairs two beta-lactams.", ADJ]], 23),

Q(T_EMP, IO_PROT, "drug choice",
  "A proposed empiric regimen for nosocomial pneumonia with multidrug-resistant risk factors is vancomycin, linezolid and tobramycin. What makes it inappropriate?",
  [["It has only one gram-negative agent", "Correct. Vancomycin and linezolid both cover methicillin-resistant Staphylococcus aureus (MRSA), so only tobramycin covers gram-negative organisms; two are needed."],
   ["It lacks gram-positive coverage", "The reverse: vancomycin and linezolid are both gram-positive coverage, one too many; the regimen needs a second gram-negative agent instead.", REV],
   ["It pairs two beta-lactam antibiotics", "None of these three is a beta-lactam: vancomycin and linezolid are the two gram-positive drugs, and tobramycin is an aminoglycoside.", MECH],
   ["Tobramycin cannot cover Pseudomonas", "An aminoglycoside such as tobramycin is a listed second gram-negative agent; the flaw is that only one gram-negative drug is present.", ADJ]], 23),

# ---- antipseudomonal agents (slides 24-27) -------------------------------------------------------
Q(T_AP, IO_CLASS, "class",
  "Which cephalosporin is a fourth-generation antipseudomonal agent?",
  [["Cefepime", "Correct. Cefepime (Maxipime) is a fourth-generation antipseudomonal cephalosporin, and, like ceftazidime, it requires renal adjustment."],
   ["Ceftriaxone", "Ceftriaxone is a third-generation cephalosporin used in community-acquired pneumonia and limited-spectrum nosocomial coverage, not an antipseudomonal agent.", MECH],
   ["Cefuroxime", "Cefuroxime is a second- or third-generation cephalosporin for outpatient community-acquired pneumonia; cefepime is the fourth-generation antipseudomonal one.", MECH],
   ["Cefotaxime", "Cefotaxime is an intravenous beta-lactam for ward community-acquired pneumonia; the fourth-generation antipseudomonal cephalosporin is cefepime.", MECH]], 24),

Q(T_AP, IO_PROT, "monitoring",
  "What do cefepime and ceftazidime both require?",
  [["Renal adjustment", "Correct. Both antipseudomonal cephalosporins require renal adjustment, as do the antipseudomonal carbapenems, penicillins and fluoroquinolones."],
   ["Seizure precautions", "Seizure caution is stated for imipenem-cilastatin, not the antipseudomonal cephalosporins, which both require renal adjustment.", ADJ],
   ["Trough monitoring", "Trough levels belong to vancomycin, drawn before the third or fourth dose; cefepime and ceftazidime both require renal adjustment.", ADJ],
   ["Hepatic adjustment", "No hepatic adjustment is stated for the antipseudomonal cephalosporins; both require renal adjustment.", MECH]], 24),

# Slide 24 says ceftazidime is not recommended; Dr. Wood affirmed it aloud (24:33-24:39: rapid resistance, "We're going to
# stick with cefepime"; Whisper wrote the drug name as "tetazodine's", read from the slide). Asked once, as the slide says;
# the guide notes that current guidelines still list ceftazidime.
Q(T_AP, IO_PROT, "drug choice",
  "Why is ceftazidime rarely used as the antipseudomonal cephalosporin for nosocomial pneumonia?",
  [["Resistance develops rapidly", "Correct. Ceftazidime (Fortaz) is not recommended because of rapid development of resistance and is rarely used; cefepime is the choice."],
   ["It lowers the seizure threshold", "Seizure caution is stated for imipenem-cilastatin, a carbapenem; ceftazidime is set aside because resistance develops rapidly.", ADJ],
   ["It lacks Pseudomonas activity", "Limited Pseudomonas activity describes ertapenem; ceftazidime is antipseudomonal, but resistance to it develops rapidly.", ADJ],
   ["It needs no renal adjustment", "Both antipseudomonal cephalosporins require renal adjustment; ceftazidime's problem is rapid development of resistance.", REV]], 24),

Q(T_AP, IO_CONTRA, "contraindication",
  "Which antipseudomonal agent is used with caution in a patient with a seizure history?",
  [["Imipenem-cilastatin", "Correct. Imipenem-cilastatin (Primaxin) is used with caution in patients with a seizure history; meropenem carries less seizure risk."],
   ["Meropenem", "Meropenem is the carbapenem with less seizure risk; the caution for a seizure history is attached to imipenem-cilastatin.", REV],
   ["Piperacillin-tazobactam", "Piperacillin-tazobactam carries a renal-adjustment note, not a seizure caution; imipenem-cilastatin is the agent used with caution in seizure history.", ADJ],
   ["Tobramycin", "Tobramycin's listed toxicities are ototoxicity and nephrotoxicity; the seizure caution belongs to imipenem-cilastatin.", ADJ]], 25),

Q(T_AP, IO_AE, "adverse effect",
  "Which statement about meropenem, compared with imipenem-cilastatin, is correct?",
  [["It carries less seizure risk", "Correct. Meropenem (Merrem) carries less risk for seizures than imipenem-cilastatin, which is used with caution in patients with a seizure history."],
   ["It needs no renal adjustment", "The antipseudomonal carbapenems require renal adjustment; meropenem's difference from imipenem is its lower seizure risk.", REV],
   ["It has limited Pseudomonas activity", "Limited activity against Pseudomonas aeruginosa describes ertapenem; meropenem is an antipseudomonal carbapenem with less seizure risk.", ADJ],
   ["It is a fourth-generation cephalosporin", "Cefepime is the fourth-generation cephalosporin; meropenem is a carbapenem, distinguished by its lower seizure risk.", MECH]], 25),

Q(T_AP, IO_CLASS, "class",
  "Which antipseudomonal agent is a penicillin combined with a beta-lactamase inhibitor?",
  [["Piperacillin-tazobactam", "Correct. Piperacillin-tazobactam (Zosyn) is the antipseudomonal penicillin with a beta-lactamase inhibitor, and it requires renal adjustment."],
   ["Ampicillin-sulbactam", "Ampicillin-sulbactam is a penicillin with a beta-lactamase inhibitor, but it is a limited-spectrum option, not an antipseudomonal agent.", ADJ],
   ["Imipenem-cilastatin", "Imipenem-cilastatin is an antipseudomonal carbapenem, not a penicillin with a beta-lactamase inhibitor.", MECH],
   ["Amoxicillin-clavulanate", "Amoxicillin with clavulanic acid is an outpatient community-acquired pneumonia beta-lactam, not an antipseudomonal agent.", ADJ]], 26),

Q(T_AP, IO_IND, "indication",
  "Besides Pseudomonas, the antipseudomonal fluoroquinolones have good activity against which group of pathogens?",
  [["Atypical bacteria", "Correct. Ciprofloxacin and levofloxacin have good activity against the atypicals (Mycoplasma, Chlamydia, Legionella) and good lung tissue penetration."],
   ["Fungal pathogens", "Candida and Aspergillus fumigatus are fungal causes of nosocomial pneumonia, not organisms the fluoroquinolones cover; their strength is the atypicals.", ADJ],
   ["Resistant staphylococci", "Methicillin-resistant Staphylococcus aureus is covered by vancomycin or linezolid; the fluoroquinolones have good activity against the atypicals.", MECH],
   ["Anaerobic bacteria", "Anaerobes are not named for the fluoroquinolones; the stated strength is good activity against the atypicals Mycoplasma, Chlamydia and Legionella.", ADJ]], 27),

Q(T_AP, IO_PROT, "protocol",
  "Why should fluoroquinolones be used judiciously in nosocomial pneumonia?",
  [["Rising gram-negative resistance", "Correct. Increasing use of fluoroquinolones is leading to gram-negative resistance, so they should be used judiciously."],
   ["Poor lung tissue penetration", "Fluoroquinolones have good lung tissue penetration; the reason for judicious use is increasing gram-negative resistance.", REV],
   ["Weak activity against atypicals", "Fluoroquinolones have good activity against the atypicals; the reason for judicious use is rising gram-negative resistance.", REV],
   ["They need no renal adjustment", "The antipseudomonal fluoroquinolones do require renal adjustment; the reason for judicious use is rising gram-negative resistance.", REV]], 27),

# ---- aminoglycosides and vancomycin (slides 28-29) -----------------------------------------------
Q(T_AGV, IO_CLASS, "class",
  "Which drug is an aminoglycoside?",
  [["Amikacin", "Correct. The aminoglycosides are gentamicin, tobramycin and amikacin, used as a second gram-negative agent in broad coverage."],
   ["Azithromycin", "Azithromycin is a macrolide used in community-acquired pneumonia, not an aminoglycoside like gentamicin, tobramycin and amikacin.", MECH],
   ["Ampicillin", "Ampicillin is a penicillin beta-lactam; the aminoglycosides are gentamicin, tobramycin and amikacin.", MECH],
   ["Ertapenem", "Ertapenem is a narrow-spectrum carbapenem; the aminoglycosides are gentamicin, tobramycin and amikacin.", MECH]], 28),

Q(T_AGV, IO_ADME, "mechanism",
  "Which property of aminoglycosides is the reason for extended-interval (once daily or longer) dosing in pneumonia?",
  [["Poor lung penetration", "Correct. Aminoglycosides penetrate the lung poorly, so bigger, less frequent doses give the higher concentrations needed."],
   ["Excellent lung penetration", "The reverse: aminoglycosides penetrate the lung poorly, which is why bigger doses giving higher concentrations are used.", REV],
   ["Minimal kidney toxicity", "Aminoglycosides are nephrotoxic and ototoxic and highly dependent on renal function; extended intervals answer their poor lung penetration.", REV],
   ["Activity against atypicals", "Good activity against atypicals belongs to the fluoroquinolones; aminoglycoside dosing reflects their poor lung penetration.", ADJ]], 28),

Q(T_AGV, IO_TOX, "adverse effect",
  "Which two toxicities are listed for the aminoglycosides?",
  [["Ototoxicity and nephrotoxicity", "Correct. Aminoglycosides cause ototoxicity and nephrotoxicity, and their dosing is highly dependent on renal function."],
   ["Hepatitis and hyperuricemia", "Hepatitis and hyperuricemia are pyrazinamide's adverse effects; aminoglycosides cause ototoxicity and nephrotoxicity.", ADJ],
   ["Neuritis and lupus-like syndrome", "Peripheral neuritis and a lupus-like syndrome are isoniazid's adverse effects; aminoglycosides cause ototoxicity and nephrotoxicity.", ADJ],
   ["Seizures and arrhythmias", "Seizures and arrhythmias are the toxic effects of high theophylline levels; aminoglycosides cause ototoxicity and nephrotoxicity.", ADJ]], 28),

Q(T_AGV, IO_PROT, "monitoring",
  "On what are aminoglycoside dose and frequency adjusted?",
  [["Measured drug levels", "Correct. Aminoglycoside dose and frequency are adjusted based on levels, and they are highly dependent on renal function."],
   ["Liver function tests", "No hepatic basis is given; aminoglycoside dosing is adjusted on drug levels and depends heavily on renal function.", MECH],
   ["Sputum gram stain", "The sputum gram stain is a controversial diagnostic test, not a dosing guide; aminoglycosides are adjusted on measured levels.", ADJ],
   ["White blood cell count", "The white blood cell count does not set the dose; aminoglycoside dose and frequency are adjusted on measured levels.", LAY]], 28),

Q(T_AGV, IO_IND, "indication",
  "Vancomycin is primarily used in nosocomial pneumonia to cover which pathogen?",
  [["Methicillin-resistant S. aureus", "Correct. Vancomycin is primarily used for empiric coverage of methicillin-resistant Staphylococcus aureus, the most common gram-positive cause of nosocomial pneumonia."],
   ["Gram-negative bacilli such as Pseudomonas", "Pseudomonas is covered by the antipseudomonal beta-lactams, fluoroquinolones and aminoglycosides; vancomycin is for methicillin-resistant Staphylococcus aureus.", MECH],
   ["Atypicals such as Legionella", "The atypicals are covered by the fluoroquinolones; vancomycin is primarily for empiric methicillin-resistant Staphylococcus aureus coverage.", MECH],
   ["Fungi such as Aspergillus", "Aspergillus is a fungal pathogen of nosocomial pneumonia and vancomycin is an antibacterial; its use is methicillin-resistant Staphylococcus aureus coverage.", MECH]], 29),

Q(T_AGV, IO_PROT, "monitoring",
  "When is a vancomycin trough level drawn?",
  [["Before the third or fourth dose", "Correct. The trough is drawn prior to the third to fourth dose, when vancomycin is at steady state."],
   ["Before the first dose", "There is no trough before any drug has been given; the vancomycin trough is drawn prior to the third or fourth dose, at steady state.", STAGE],
   ["Right after the first dose", "A level right after the first dose is neither a trough nor at steady state; the trough is drawn before the third or fourth dose.", STAGE],
   ["At the end of the course", "Waiting until the end of therapy defeats the purpose; the trough is drawn before the third or fourth dose, at steady state.", STAGE]], 29),

# ---- linezolid and further therapy (slides 30-31) ------------------------------------------------
Q(T_LZ, IO_ADME, "monitoring",
  "Which drug used for nosocomial pneumonia needs no dose adjustment for renal function?",
  [["Linezolid", "Correct. Linezolid (Zyvox) needs no dose adjustment based on renal function; vancomycin, the aminoglycosides and the antipseudomonal beta-lactams all require renal adjustment."],
   ["Vancomycin", "Vancomycin requires renal adjustment and is nephrotoxic with other nephrotoxins; linezolid needs no renal dose adjustment.", REV],
   ["Tobramycin", "Tobramycin, an aminoglycoside, is highly dependent on renal function; linezolid is the drug with no renal dose adjustment.", REV],
   ["Cefepime", "Cefepime requires renal adjustment like the other antipseudomonal cephalosporin; linezolid needs none.", REV]], 30),

Q(T_LZ, IO_ADME, "drug choice",
  "A patient with methicillin-resistant Staphylococcus aureus pneumonia is ready to finish therapy at home by mouth. Which drug allows this?",
  [["Linezolid", "Correct. Linezolid has great methicillin-resistant Staphylococcus aureus coverage and comes in intravenous and oral forms, with good lung penetration."],
   ["Vancomycin", "Vancomycin covers methicillin-resistant Staphylococcus aureus, but the agent named with both intravenous and oral forms for pneumonia is linezolid.", RULED],
   ["Tobramycin", "Tobramycin is an aminoglycoside second gram-negative agent, not methicillin-resistant Staphylococcus aureus coverage; linezolid is the oral option.", MECH],
   ["Cefepime", "Cefepime is an antipseudomonal cephalosporin and does not cover methicillin-resistant Staphylococcus aureus; linezolid does, by mouth.", MECH]], 30),

Q(T_LZ, IO_EDU, "education",
  "Which drawback is listed for linezolid?",
  [["High cost", "Correct. Linezolid is expensive, though it has great methicillin-resistant Staphylococcus aureus coverage, oral and intravenous forms, good lung penetration and no renal adjustment."],
   ["No oral form", "Linezolid is available in both intravenous and oral forms; its listed drawback is that it is expensive.", REV],
   ["Poor lung penetration", "Linezolid has good lung penetration; poor penetration is the aminoglycoside problem. Linezolid's drawback is cost.", REV],
   ["Renal dose adjustment", "Linezolid needs no dose adjustment for renal function; its listed drawback is that it is expensive.", REV]], 30),

Q(T_LZ, IO_PROT, "protocol",
  "Why is a patient switched to oral antibiotics when possible during pneumonia treatment?",
  [["Lower cost", "Correct. Antibiotics are switched to oral when or if possible because oral therapy is cheaper, as coverage is scaled back to the culture results."],
   ["Better lung penetration", "Lung penetration depends on the drug, not the route; the stated reason to switch to oral therapy is that it is cheaper.", LAY],
   ["Broader coverage", "Coverage is scaled back, not broadened, as cultures return; the reason for the oral switch is that it is cheaper.", REV],
   ["Fewer resistant organisms", "Resistance is not the stated reason; the switch to oral therapy when possible is made because it is cheaper.", LAY]], 31),

Q(T_LZ, IO_PROT, "monitoring",
  "A patient fails therapy for nosocomial pneumonia and is found to have a pulmonary embolus. Which category of treatment failure is this?",
  [["Wrong diagnosis", "Correct. A pulmonary embolus or a neoplasm is a wrong-diagnosis failure; resistant pathogens are wrong therapy, and Clostridioides difficile colitis, empyema or lung abscess are complications."],
   ["Wrong therapy", "Wrong therapy means resistant pathogens or inadequate antimicrobial therapy; a pulmonary embolus means the diagnosis was wrong.", COMP],
   ["A complication", "Complications are Clostridioides difficile colitis, empyema or lung abscess; a pulmonary embolus is a wrong-diagnosis failure.", COMP],
   ["Drug toxicity", "Drug toxicity is not one of the failure categories; a pulmonary embolus found on workup is a wrong diagnosis.", LAY]], 31),

Q(T_LZ, IO_AE, "adverse effect",
  "Which finding is listed as a complication that causes failure of pneumonia therapy?",
  [["Lung abscess", "Correct. Complications causing failure are Clostridioides difficile colitis, empyema or lung abscess; a pulmonary embolus or neoplasm is a wrong diagnosis."],
   ["Neoplasm", "A neoplasm is a wrong-diagnosis failure, not a complication; the complications are Clostridioides difficile colitis, empyema and lung abscess.", COMP],
   ["Pulmonary embolus", "A pulmonary embolus is a wrong-diagnosis failure; the listed complications are Clostridioides difficile colitis, empyema and lung abscess.", COMP],
   ["Resistant pathogens", "Resistant pathogens are a wrong-therapy failure; the listed complications are Clostridioides difficile colitis, empyema and lung abscess.", COMP]], 31),
]
