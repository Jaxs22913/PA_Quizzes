# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Drugs for Pulmonary Infections, Asthma and COPD (Lecture 11), topic: acute bronchitis and
community-acquired pneumonia.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. The key is authored FIRST (c == 0);
pharm_e3_partition.py rotates it (numeric option sets are sorted ascending instead, WRITER.md rule 8).

SOURCE. Pulmonology-2.pptx slides 4-15: bronchitis (5, with a picture of a normal and an inflamed bronchial tube), acute
bronchitis causes (6) and treatment (7-8), community-acquired pneumonia pathophysiology (10), diagnosis (11), etiology by
setting (12), risk factors for penicillin-resistant Streptococcus pneumoniae (13), outpatient treatment (14) and
inpatient treatment (15). The deck has no speaker notes.

WRITER.md v1 (2026-10-15): every distractor carries its misconception as a third element (mis); slides only; slides win
on conflict. Shared keying decisions: scratchpad L11_KEYING.md (copied into the guide's notes).

KEYED WITH A GUIDE NOTE: outpatient first line = a macrolide (azithromycin, clarithromycin), second line = doxycycline or
minocycline (slide 14). Current guidance prefers amoxicillin or doxycycline and limits macrolides to areas of low
pneumococcal macrolide resistance; the study guide carries the "Current guidelines differ" line.

LEFT OUT ON PURPOSE:
  * every dose ("high-dose ampicillin" appears only as the slide's drug name, never as a key);
  * bare numbers as keys (age over 65 and the 3-month beta-lactam window appear inside stems and explanations only);
  * the ambiguous fluoroquinolone line on slide 8 ("avoid unless recent antibiotic exposure / Risk for resistant
    S. pneumoniae") is asked only as its plain rule (avoid unless recent antibiotic exposure), never as WHY;
  * cephalosporin generations of cefuroxime and cefpodoxime as a key (recognition trivia);
  * which comorbidities count ("etc." on slide 13 makes the list open), so no comorbidity is offered as a wrong answer.
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


T_BR = "Acute bronchitis"
T_DX = "Pneumonia: entry and diagnosis"
T_ET = "Pathogens by setting"
T_OUT = "Outpatient pneumonia treatment"
T_IN = "Inpatient pneumonia treatment"

QUESTIONS = [

# ---- bronchitis (slides 5-8) ---------------------------------------------------------------------
Q(T_BR, IO_IND, "physiology",
  "Which patients does chronic bronchitis primarily affect?",
  [["Those with chronic obstructive pulmonary disease", "Correct. Acute bronchitis affects all ages, while chronic bronchitis primarily affects patients with chronic obstructive pulmonary disease."],
   ["Children exposed to a day care center", "Exposure to a child in day care is a risk factor for penicillin-resistant Streptococcus pneumoniae; chronic bronchitis primarily affects patients with chronic obstructive pulmonary disease.", ADJ],
   ["Patients receiving mechanical ventilation", "Mechanical ventilation raises the risk of nosocomial pneumonia; chronic bronchitis is the form that primarily affects patients with chronic obstructive pulmonary disease.", ADJ],
   ["Previously healthy adults of every age", "Every age is affected by ACUTE bronchitis; the chronic form primarily affects patients with chronic obstructive pulmonary disease.", STAGE]], 5),

Q(T_BR, IO_IND, "physiology",
  "Which group of pathogens is the common cause of acute bronchitis?",
  [["Respiratory viruses", "Correct. The common causes are viruses (rhinovirus, coronavirus, influenza, adenovirus); bacteria are only occasional causes, sometimes secondary to a viral illness."],
   ["Atypical bacteria", "Mycoplasma pneumoniae, Chlamydia pneumoniae and Bordetella pertussis cause acute bronchitis only occasionally; the common causes are respiratory viruses.", STAGE],
   ["Gram-positive cocci", "Streptococcus and Staphylococcus species are occasional bacterial causes, sometimes secondary to a viral illness; most acute bronchitis is viral.", STAGE],
   ["Gram-negative bacilli", "Gram-negative bacilli are named among the intensive care unit pneumonia pathogens; the common cause of acute bronchitis is respiratory viruses.", ADJ]], 6),

Q(T_BR, IO_PROT, "drug choice",
  "A previously healthy adult has had a cough for three days after a cold and is diagnosed with acute bronchitis. What is the appropriate antibiotic plan?",
  [["No antibiotic", "Correct. Acute bronchitis is generally self-limited and treated with symptomatic, supportive care only; routine antibiotics are not recommended and are a common unnecessary prescription."],
   ["Azithromycin", "A macrolide is considered only when symptoms persist beyond 5 days and bacterial involvement is suspected; at day three, supportive care alone is appropriate.", STAGE],
   ["Doxycycline", "Doxycycline is preferred only when Mycoplasma is documented; uncomplicated acute bronchitis at day three gets supportive care and no routine antibiotic.", STAGE],
   ["Levofloxacin", "A respiratory fluoroquinolone is avoided in acute bronchitis unless there was recent antibiotic exposure; this patient needs supportive care only.", RULED]], 8),

Q(T_BR, IO_EDU, "education",
  "Why may antihistamines be avoided in acute bronchitis?",
  [["They dry out bronchial secretions", "Correct. Antihistamines and sympathomimetics may be avoided because they dehydrate bronchial secretions and may prolong symptoms."],
   ["They increase mucus production", "The concern runs the other way: antihistamines dehydrate bronchial secretions, which may prolong the symptoms of acute bronchitis.", REV],
   ["They suppress the cough reflex", "Cough suppression is the role of the antitussives, which are part of supportive care; antihistamines are avoided because they dehydrate bronchial secretions.", MECH],
   ["They promote antibiotic resistance", "Resistance is a concern with unnecessary antibiotics, not antihistamines; antihistamines may be avoided because they dry bronchial secretions and prolong symptoms.", ADJ]], 7),

Q(T_BR, IO_IND, "drug choice",
  "Which drug group is part of the supportive care for acute bronchitis?",
  [["Antitussives", "Correct. Supportive care for acute bronchitis is analgesics, antipyretics, antitussives and fluids."],
   ["Antihistamines", "Antihistamines may be avoided in acute bronchitis because they dehydrate bronchial secretions and may prolong symptoms; antitussives are part of supportive care.", REV],
   ["Sympathomimetics", "Sympathomimetics may be avoided because they dehydrate bronchial secretions and may prolong symptoms; antitussives are part of supportive care.", REV],
   ["Macrolides", "Routine antibiotics such as macrolides are not recommended for acute bronchitis; supportive care is analgesics, antipyretics, antitussives and fluids.", STAGE]], 7),

Q(T_BR, IO_PROT, "protocol",
  "In acute bronchitis, symptoms that persist beyond five days should prompt consideration of what?",
  [["Bacterial involvement", "Correct. Routine antibiotics are not recommended, but persistent symptoms beyond 5 days should prompt consideration of bacterial involvement."],
   ["Chronic bronchitis", "Chronic bronchitis primarily affects patients with chronic obstructive pulmonary disease; persistence beyond 5 days in acute bronchitis raises bacterial involvement.", COMP],
   ["Antihistamine therapy", "Antihistamines may be avoided because they dehydrate bronchial secretions and prolong symptoms; persistence beyond 5 days raises the question of bacterial involvement.", REV],
   ["A resistant virus", "Acute bronchitis is usually viral and self-limited; when symptoms persist beyond 5 days, the consideration is bacterial involvement.", LAY]], 8),

Q(T_BR, IO_IND, "drug choice",
  "A patient with acute bronchitis has documented Mycoplasma infection. Which antibiotic is preferred?",
  [["Doxycycline", "Correct. Doxycycline is preferred when Mycoplasma is documented, because of macrolide resistance."],
   ["Azithromycin", "Azithromycin is a macrolide, and macrolide resistance is the reason doxycycline is preferred for documented Mycoplasma.", RULED],
   ["Erythromycin", "Erythromycin is a macrolide; because of macrolide resistance, doxycycline is preferred when Mycoplasma is documented.", RULED],
   ["Levofloxacin", "A respiratory fluoroquinolone is avoided in acute bronchitis unless there was recent antibiotic exposure; doxycycline is preferred for Mycoplasma.", RULED]], 8),

Q(T_BR, IO_CONTRA, "contraindication",
  "In acute bronchitis, a respiratory fluoroquinolone is avoided unless which history is present?",
  [["Recent antibiotic exposure", "Correct. In acute bronchitis a respiratory fluoroquinolone is to be avoided unless the patient has had recent antibiotic exposure."],
   ["Documented Mycoplasma infection", "Documented Mycoplasma calls for doxycycline, preferred because of macrolide resistance, not for a fluoroquinolone.", ADJ],
   ["A viral cause such as influenza", "Influenza is one of the common viral causes, and viral acute bronchitis gets supportive care, not a fluoroquinolone.", RULED],
   ["Fever along with the cough", "Fever is treated with antipyretics as part of supportive care; the exception for a fluoroquinolone is recent antibiotic exposure.", LAY]], 8),

# ---- pneumonia: entry and diagnosis (slides 10-11) -----------------------------------------------
Q(T_DX, IO_IND, "physiology",
  "Which route by which microbes reach the lung is common in elderly patients?",
  [["Aspiration from the oropharynx", "Correct. Microbes enter the lung by aspiration from the oropharynx (common in the elderly), inhalation of aerosols, hematogenous spread or direct inoculation."],
   ["Inhalation of infectious aerosols", "Inhalation of infectious aerosols is a route of entry, but the one singled out as common in the elderly is aspiration from the oropharynx.", ADJ],
   ["Hematogenous dissemination", "Hematogenous dissemination is a route of entry, but aspiration from the oropharynx is the route noted as common in the elderly.", ADJ],
   ["Direct inoculation by trauma", "Direct inoculation, as after trauma, is a route of entry; aspiration from the oropharynx is the one noted as common in the elderly.", ADJ]], 10),

Q(T_DX, IO_IND, "physiology",
  "Trauma is the example given for which route by which microbes reach the lung?",
  [["Direct inoculation", "Correct. Direct inoculation is the route of entry given with trauma as its example, alongside aspiration, inhalation and hematogenous spread."],
   ["Oropharyngeal aspiration", "Aspiration from the oropharynx is the route common in the elderly; trauma is the example given for direct inoculation.", ADJ],
   ["Aerosol inhalation", "Inhalation of infectious aerosols is airborne entry; trauma is the example given for direct inoculation.", ADJ],
   ["Hematogenous spread", "Hematogenous dissemination reaches the lung through the blood; trauma is the example given for direct inoculation.", ADJ]], 10),

Q(T_DX, IO_PROT, "protocol",
  "For a patient hospitalized with community-acquired pneumonia, when should blood and sputum cultures be obtained?",
  [["Before antibiotics are started", "Correct. Blood and sputum cultures are obtained for hospitalized patients, and they are drawn prior to antibiotics."],
   ["After 48 hours of antibiotics", "Forty-eight hours is the threshold that defines nosocomial pneumonia, not culture timing; cultures are drawn before antibiotics are given.", ADJ],
   ["When empiric therapy fails", "Cultures are not saved for failure; for hospitalized patients they are drawn at the start, prior to antibiotics.", STAGE],
   ["At discharge from the hospital", "Cultures guide therapy, so for hospitalized patients they are drawn prior to antibiotics, not at discharge.", STAGE]], 11),

Q(T_DX, IO_PROT, "protocol",
  "How is community-acquired pneumonia usually managed in the outpatient setting?",
  [["Empiric antibiotics, no routine tests", "Correct. Outpatients do well with empiric antibiotics, and diagnostic tests are not routinely performed."],
   ["Blood cultures before antibiotics", "Blood and sputum cultures before antibiotics are for hospitalized patients; outpatients are treated empirically without routine tests.", ADJ],
   ["Sputum culture to choose the drug", "Sputum gram stain and culture is controversial (frequent contamination); outpatients do well with empiric antibiotics.", RULED],
   ["Sputum gram stain before treating", "The sputum gram stain is controversial because samples are often contaminated; outpatient pneumonia is treated empirically.", RULED]], 11),

Q(T_DX, IO_PROT, "monitoring",
  "Why is the sputum gram stain and culture in pneumonia considered controversial?",
  [["Expectorated samples are often contaminated", "Correct. Sputum gram stain and culture is controversial: expectorated sputum is frequently contaminated and the responsible pathogen is not always identified."],
   ["It must follow the first antibiotic", "The timing rule is the reverse: cultures for hospitalized patients are obtained prior to antibiotics. The controversy is contamination and missed pathogens.", REV],
   ["It cannot be done in hospitalized patients", "Sputum cultures are in fact obtained for hospitalized patients; the controversy is that expectorated sputum is often contaminated.", REV],
   ["It replaces the need for blood cultures", "Hospitalized patients get both blood and sputum cultures; the controversy is that expectorated sputum is frequently contaminated.", ADJ]], 11),

# ---- pathogens by setting (slides 12-13) ---------------------------------------------------------
Q(T_ET, IO_IND, "physiology",
  "Which pathogen is listed for intensive care unit pneumonia but not for outpatient pneumonia?",
  [["Staphylococcus aureus", "Correct. Staphylococcus aureus appears on the intensive care unit list (with Legionella and gram-negative bacilli), not on the outpatient list."],
   ["Streptococcus pneumoniae", "Streptococcus pneumoniae is listed in all three settings: outpatient, inpatient ward and intensive care unit.", ADJ],
   ["Haemophilus influenzae", "Haemophilus influenzae is listed in all three settings, including outpatient pneumonia; Staphylococcus aureus is the intensive care unit addition.", ADJ],
   ["Moraxella catarrhalis", "Moraxella catarrhalis is listed only for outpatient pneumonia, the reverse of what is asked; Staphylococcus aureus is the intensive care unit pathogen.", REV]], 12),

Q(T_ET, IO_IND, "physiology",
  "Which exposure is a listed risk factor for penicillin-resistant Streptococcus pneumoniae?",
  [["A child who attends day care", "Correct. Exposure to a child in a day care center is listed with age over 65, a beta-lactam within 3 months, alcoholism, immunosuppression and medical comorbidities."],
   ["Living in a nursing home", "Nursing home residence is a criterion for health-care associated pneumonia; the listed exposure for resistant Streptococcus pneumoniae is a child in day care.", ADJ],
   ["Attending hemodialysis", "Hemodialysis is a criterion for health-care associated pneumonia; the exposure listed for penicillin-resistant Streptococcus pneumoniae is a child in day care.", ADJ],
   ["Living in a college dormitory", "Crowded adult housing is not on the list; the exposure listed for penicillin-resistant Streptococcus pneumoniae is a child in a day care center.", LAY]], 13),

Q(T_ET, IO_IND, "physiology",
  "Which medication history is a risk factor for penicillin-resistant Streptococcus pneumoniae?",
  [["A beta-lactam within the past 3 months", "Correct. A beta-lactam within the past 3 months is listed with age over 65, alcoholism, immunosuppression, comorbidities and day care exposure."],
   ["A known allergy to beta-lactams", "A beta-lactam allergy steers the choice toward a respiratory fluoroquinolone; it is not a risk factor for resistant pneumococcus. Recent beta-lactam use is.", ADJ],
   ["A beta-lactam taken 2 years ago", "The listed window is a beta-lactam within the past 3 months; a course 2 years ago falls outside it.", REV],
   ["Daily antitussive use for a cough", "Antitussives are part of supportive care for bronchitis and are not a resistance risk; a beta-lactam within the past 3 months is.", LAY]], 13),

# ---- outpatient treatment (slide 14) -------------------------------------------------------------
Q(T_OUT, IO_IND, "drug choice",
  "An outpatient with community-acquired pneumonia has no risk factors for resistant Streptococcus pneumoniae. Which drug is first line?",
  [["Azithromycin", "Correct. With no risk of resistant Streptococcus pneumoniae, first line is a macrolide (azithromycin or clarithromycin); doxycycline and minocycline are second line."],
   ["Doxycycline", "Doxycycline is the second-line choice for an outpatient without risk factors; the first-line drug is a macrolide such as azithromycin.", STAGE],
   ["Levofloxacin", "A respiratory fluoroquinolone is an option when risk factors for resistant Streptococcus pneumoniae are present; without them a macrolide is first line.", STAGE],
   ["Cefpodoxime", "Cefpodoxime is the beta-lactam half of the beta-lactam-plus-macrolide regimen used when resistance risk factors are present; first line here is a macrolide.", STAGE]], 14),

Q(T_OUT, IO_IND, "drug choice",
  "An outpatient with community-acquired pneumonia and no resistance risk factors needs a second-line option. Which drug is listed?",
  [["Minocycline", "Correct. Without risk of resistant Streptococcus pneumoniae, first line is a macrolide and second line is doxycycline or minocycline."],
   ["Moxifloxacin", "A respiratory fluoroquinolone such as moxifloxacin is used when risk factors for resistant Streptococcus pneumoniae are present; second line here is doxycycline or minocycline.", STAGE],
   ["Cefuroxime", "Cefuroxime is paired with a macrolide when resistance risk factors are present; the second-line drug without them is doxycycline or minocycline.", STAGE],
   ["Ceftriaxone", "Ceftriaxone is an intravenous beta-lactam for hospitalized patients; the outpatient second-line drug without risk factors is doxycycline or minocycline.", ADJ]], 14),

Q(T_OUT, IO_IND, "drug choice",
  "An outpatient with community-acquired pneumonia has risk factors for resistant Streptococcus pneumoniae. Which beta-lactam is paired with a macrolide?",
  [["Cefuroxime", "Correct. With resistance risk factors, a beta-lactam (amoxicillin with or without clavulanic acid, cefuroxime or cefpodoxime) is combined with a macrolide."],
   ["Cefepime", "Cefepime is a fourth-generation antipseudomonal cephalosporin used for nosocomial pneumonia; the outpatient beta-lactams are amoxicillin, cefuroxime and cefpodoxime.", ADJ],
   ["Ertapenem", "Ertapenem is a narrow-spectrum carbapenem in the limited-spectrum nosocomial regimen; the outpatient beta-lactams are amoxicillin, cefuroxime and cefpodoxime.", ADJ],
   ["Ceftazidime", "Ceftazidime is an antipseudomonal cephalosporin that is rarely used; the outpatient beta-lactams paired with a macrolide are amoxicillin, cefuroxime and cefpodoxime.", ADJ]], 14),

Q(T_OUT, IO_CONTRA, "drug choice",
  "An outpatient with community-acquired pneumonia has risk factors for resistant Streptococcus pneumoniae and a beta-lactam allergy. Which drug fits?",
  [["Moxifloxacin", "Correct. A respiratory fluoroquinolone (levofloxacin or moxifloxacin) is the alternative to beta-lactam plus macrolide and is good for patients with a beta-lactam allergy."],
   ["Cefpodoxime", "Cefpodoxime is a cephalosporin, a beta-lactam, so the allergy rules it out; a respiratory fluoroquinolone is the choice.", RULED],
   ["Amoxicillin", "Amoxicillin is a beta-lactam and is ruled out by the allergy; with resistance risk factors and an allergy, a respiratory fluoroquinolone fits.", RULED],
   ["Azithromycin", "A macrolide alone is first line only when there is no resistance risk; with risk factors and a beta-lactam allergy, a respiratory fluoroquinolone fits.", RULED]], 14),

Q(T_OUT, IO_IND, "drug choice",
  "A 70-year-old outpatient with community-acquired pneumonia took amoxicillin 2 months ago. Which single drug is an appropriate regimen?",
  [["Levofloxacin", "Correct. Age over 65 and a beta-lactam within 3 months are risk factors for resistant Streptococcus pneumoniae, so the options are beta-lactam plus macrolide or a respiratory fluoroquinolone alone."],
   ["Azithromycin", "A macrolide alone is first line only when there is no risk of resistant Streptococcus pneumoniae; this patient has two risk factors.", RULED],
   ["Doxycycline", "Doxycycline is second line for patients without resistance risk; age over 65 and a recent beta-lactam call for a respiratory fluoroquinolone or a combination.", RULED],
   ["Minocycline", "Minocycline is second line only without resistance risk factors; age over 65 and recent amoxicillin call for a respiratory fluoroquinolone or a combination.", RULED]], 13),

# ---- inpatient treatment (slide 15) --------------------------------------------------------------
Q(T_IN, IO_IND, "drug choice",
  "A patient is admitted to a medical ward, outside the intensive care unit, with community-acquired pneumonia. Which regimen fits?",
  [["Ceftriaxone plus azithromycin", "Correct. Non-intensive care inpatients get an intravenous beta-lactam (cefotaxime, ceftriaxone or high-dose ampicillin) plus an intravenous or oral macrolide."],
   ["Azithromycin by mouth alone", "A macrolide alone is the outpatient first-line choice without resistance risk; hospitalized patients get an intravenous beta-lactam plus a macrolide.", STAGE],
   ["Cefepime plus tobramycin", "An antipseudomonal cephalosporin plus an aminoglycoside is broad gram-negative coverage for nosocomial pneumonia; the ward regimen is an intravenous beta-lactam plus a macrolide.", ADJ],
   ["Doxycycline by mouth alone", "Doxycycline alone is the outpatient second-line choice; on the ward, doxycycline may replace the macrolide but is given alongside an intravenous beta-lactam.", STAGE]], 15),

Q(T_IN, IO_PROT, "protocol",
  "How does treatment of community-acquired pneumonia in the intensive care unit differ from treatment on the ward?",
  [["Every drug is started intravenously", "Correct. Intensive care unit treatment uses the same regimens, but all treatment begins intravenously, and coverage for methicillin-resistant Staphylococcus aureus is considered if warranted."],
   ["The beta-lactam is given by mouth", "The beta-lactam is intravenous even on the ward; in the intensive care unit every drug is started intravenously.", REV],
   ["Antibiotics wait for culture results", "Cultures are drawn before antibiotics, but treatment does not wait for them; in the intensive care unit all treatment begins intravenously.", STAGE],
   ["Staphylococcal coverage is mandatory", "Coverage for methicillin-resistant Staphylococcus aureus is only considered if warranted; the stated difference is that all treatment begins intravenously.", REV]], 15),

Q(T_IN, IO_CONTRA, "drug choice",
  "A patient admitted to a ward with community-acquired pneumonia has a beta-lactam allergy. Which drug can be used in place of the beta-lactam-based regimen?",
  [["Levofloxacin", "Correct. For hospitalized patients, a respiratory fluoroquinolone replaces the intravenous beta-lactam plus macrolide regimen when there is a beta-lactam allergy."],
   ["Cefotaxime", "Cefotaxime is one of the intravenous beta-lactams on the ward regimen, so a beta-lactam allergy rules it out.", RULED],
   ["Ampicillin", "Ampicillin is a beta-lactam (given high-dose on the ward regimen), so the allergy rules it out; a respiratory fluoroquinolone is used instead.", RULED],
   ["Doxycycline", "Doxycycline can replace the macrolide, but it is still paired with an intravenous beta-lactam; the allergy alternative is a respiratory fluoroquinolone.", MECH]], 15),

Q(T_IN, IO_IND, "drug choice",
  "Alongside an intravenous beta-lactam for a hospitalized ward patient with pneumonia, which drug may stand in for the macrolide?",
  [["Doxycycline", "Correct. The ward regimen is an intravenous beta-lactam plus an intravenous or oral macrolide, or doxycycline in place of the macrolide."],
   ["Vancomycin", "Vancomycin covers methicillin-resistant Staphylococcus aureus, which is considered in the intensive care unit; doxycycline is the macrolide alternative.", ADJ],
   ["Gentamicin", "Gentamicin is an aminoglycoside used as a second gram-negative agent in broad nosocomial coverage; doxycycline is the macrolide alternative.", ADJ],
   ["Linezolid", "Linezolid is gram-positive coverage for methicillin-resistant Staphylococcus aureus; the drug that may replace the macrolide on the ward is doxycycline.", ADJ]], 15),

Q(T_IN, IO_CLASS, "drug choice",
  "Which beta-lactam is listed for intravenous use in hospitalized patients with community-acquired pneumonia outside the intensive care unit?",
  [["Cefotaxime", "Correct. The intravenous beta-lactams for ward patients are cefotaxime, ceftriaxone and high-dose ampicillin, each given with a macrolide or doxycycline."],
   ["Cefpodoxime", "Cefpodoxime is an outpatient beta-lactam for patients with resistance risk factors; the ward choices are cefotaxime, ceftriaxone and high-dose ampicillin.", ADJ],
   ["Cefepime", "Cefepime is an antipseudomonal fourth-generation cephalosporin for broad nosocomial coverage, not a listed community-acquired ward choice.", ADJ],
   ["Ceftazidime", "Ceftazidime is an antipseudomonal cephalosporin that is rarely used; the ward beta-lactams are cefotaxime, ceftriaxone and high-dose ampicillin.", ADJ]], 15),
]
