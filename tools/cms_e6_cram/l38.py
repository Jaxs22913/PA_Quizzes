# -*- coding: utf-8 -*-
"""Lecture 38 (Mycobacterial Infections, Including Tuberculosis, Bobilin) cram topics, condensed from guide
section 6.

CRITERIA: one table per criteria set, classification, staging, regimen or cut-off table on the slides (Jaxon's
standing rule, memory cram_criteria_tables), each with a labeled memory aid. Cells are the slide wording.
"""
L38C = "#1f5c3a"

CRITERIA = [
{"id": "crit-l38-stages", "label": "Tuberculosis: Stages", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slides 9&ndash;10, 12",
 "cols": ["Stage", "What the slides say"], "widths": ["30%", "70%"], "rows": [
  ("Primary infection", "Initial infection may remain <b>contained without clinical disease</b>"),
  ("Progressive primary tuberculosis", "Disease develops <b>soon after</b> initial infection when immune containment fails"),
  ("Latent tuberculosis infection", "Infected but <b>asymptomatic</b>; <b>not infectious</b>, cannot spread it; no evidence of disease after evaluation"),
  ("Reactivation (secondary) tuberculosis", "Latent infection progresses to disease, <b>often with impaired immunity</b>; reinfection is a separate event"),
 ], "mnemonic": {"hook": "Caught, Crashed early, Caged, Came back.",
  "key": [["Caught", "primary infection, contained"], ["Crashed early", "progressive primary tuberculosis"], ["Caged", "latent infection: no symptoms, no spread"], ["Came back", "reactivation (secondary), with impaired immunity"]]}},

{"id": "crit-l38-three", "label": "Latent Infection vs Tuberculosis Disease vs Nontuberculous Disease", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slides 4, 10, 13, 16, 19, 23, 25&ndash;29, 33&ndash;34, 37&ndash;40",
 "cols": ["", "Latent tuberculosis infection", "Tuberculosis disease", "Nontuberculous mycobacterial disease"], "widths": ["16%", "28%", "28%", "28%"], "rows": [
  ("Symptoms", "None", "Persistent cough, fever, night sweats, weight loss (may be mild or absent)", "Chronic cough and sputum, fatigue, weight loss, dyspnea or hemoptysis"),
  ("Spreads?", "<b>No</b>", "<b>Yes</b> if pulmonary or laryngeal (airborne)", "Person-to-person spread uncommon (environmental)"),
  ("Skin or blood test", "Positive (shows infection only)", "Can be falsely negative (immunosuppression, severe tuberculosis); a negative never rules disease out", "&mdash;"),
  ("Chest imaging", "<b>Usually normal</b>", "Infiltrates, cavities (upper lobes after primary), adenopathy, effusion, miliary nodules", "Nodular bronchiectasis or fibrocavitary disease on computed tomography"),
  ("Microbiology", "No evidence of disease", "3 sputum specimens: smear, culture, rapid molecular test, susceptibility", "Same species in 2 or more sputum cultures, or 1 wash or lavage or biopsy"),
  ("Treatment", "3HP, 4R or 3HR (6H or 9H if rifamycins unsuitable) after excluding disease", "2 months HRZE, then 4 months HR; isolation and notification", "Macrolide-susceptible Mycobacterium avium complex: azithromycin, ethambutol, rifamycin, at least 12 months after culture conversion"),
  {"note": "An acid-fast smear cannot tell tuberculosis from nontuberculous mycobacteria (slide 4). Regimen letters are expanded in the regimen tables below."},
 ], "mnemonic": {"hook": "Latent is Locked (no symptoms, no spread, normal film); Disease Disperses (symptoms, sputum, isolation); Nontuberculous comes from Nature (environment, needs repeat cultures).",
  "key": [["Locked", "latent infection"], ["Disperses", "tuberculosis disease"], ["Nature", "nontuberculous mycobacterial disease"]]}},

{"id": "crit-l38-progression", "label": "Risk of Progression After Infection", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slide 15",
 "cols": ["Tier", "Letter", "Risk factor"], "widths": ["22%", "12%", "66%"], "rows": [
  ("Higher", "H", "<b>HIV (human immunodeficiency virus)</b> infection or major immunosuppression"),
  ("Higher", "I", "<b>Immunosuppressive treatment</b>: TNF (tumor necrosis factor) inhibitors, transplantation, prolonged corticosteroids"),
  ("Higher", "R", "<b>Recent infection</b>, especially within 2 years"),
  ("Higher", "E", "<b>Early life</b>: infancy and young childhood"),
  ("Additional", "D", "Diabetes mellitus"),
  ("Additional", "K", "Chronic kidney disease or dialysis"),
  ("Additional", "M", "Silicosis, low body weight or malnutrition (the lungs and the meal)"),
  ("Additional", "S", "Smoking (tobacco) and harmful alcohol use"),
 ], "mnemonic": {"hook": "Higher risk HIREs it; Don&rsquo;t Keep Missing Smokers.",
  "key": [["H", "HIV or major immunosuppression"], ["I", "TNF inhibitors, transplant, prolonged steroids"], ["R", "recent infection within 2 years"], ["E", "infancy and young childhood"],
          ["D", "diabetes"], ["K", "kidney disease or dialysis"], ["M", "silicosis, low weight, malnutrition"], ["S", "tobacco and harmful alcohol"]],
  "breaks": "M packs three slide items (silicosis, low body weight, malnutrition) and S packs two (tobacco, alcohol)."}},

{"id": "crit-l38-tst", "label": "Tuberculin Skin Test: Placing and Reading", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slides 20&ndash;21",
 "cols": ["Step", "Rule (slide 20)"], "widths": ["24%", "76%"], "rows": [
  ("Place", "<b>0.1 mL</b> purified protein derivative <b>intradermally on the forearm</b>"),
  ("Read", "A <b>trained reader at 48&ndash;72 hours</b>"),
  ("Measure", "<b>Transverse induration in millimeters</b>; <b>do not measure erythema</b>"),
  ("Interpret", "By the patient&rsquo;s <b>risk category</b> (the 5, 10, 15 mm table)"),
  ("BCG (bacille Calmette-Gu&eacute;rin) history", "Can cause a false-positive skin test; <b>use the same thresholds regardless</b>; <b>interferon-gamma release assay preferred</b> for most vaccinated patients (slide 21)"),
 ], "mnemonic": {"hook": "Point-one in, two to three days, feel the bump not the blush.",
  "key": [["Point-one", "0.1 mL intradermal, forearm"], ["Two to three days", "read at 48&ndash;72 hours"], ["Bump not blush", "measure induration, not erythema"], ["Risk group", "interpret by category"], ["BCG", "same thresholds; prefer the blood test"]]}},

{"id": "crit-l38-cutoffs", "label": "Tuberculin Skin Test: Positivity Thresholds", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slide 22",
 "cols": ["Induration", "Positive in"], "widths": ["20%", "80%"], "rows": [
  ("<b>5 mm or more</b>", "HIV, <b>recent close contact</b>, transplant, <b>major immunosuppression</b>, or <b>imaging suggesting prior tuberculosis</b>"),
  ("<b>10 mm or more</b>", "<b>Increased exposure risk</b>, selected medical risks, <b>high-risk congregate settings</b>, <b>children under 5</b> or children exposed to high-risk adults"),
  ("<b>15 mm or more</b>", "<b>No known tuberculosis risk factors</b>"),
 ], "mnemonic": {"hook": "5 for the Sick and the Close, 10 for the Risky, 15 for the Rest.",
  "key": [["5", "immune-weak (HIV, transplant, immunosuppressed), close contacts, imaging suggesting prior tuberculosis"], ["10", "exposure risk, medical risk, congregate settings, children under 5"], ["15", "no risk factors"]],
  "breaks": "&ldquo;Selected medical risks&rdquo; is all the slide says for the 10 mm group; major immunosuppression is a 5 mm group."}},

{"id": "crit-l38-negative", "label": "When a Negative Test Does Not Reassure", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slides 19, 23, 25",
 "cols": ["Situation", "What to do"], "widths": ["44%", "56%"], "rows": [
  ("Recent exposure (early infection)", "<b>Repeat 8&ndash;10 weeks after the last exposure</b> when indicated"),
  ("Immunosuppression or severe tuberculosis", "False negatives possible"),
  ("Symptoms or high clinical suspicion", "<b>Evaluate for disease now</b>; symptoms or suspicious imaging need microbiologic testing even with a negative skin or blood test"),
  ("Young child or immunocompromised contact", "Prompt public-health assessment"),
  ("Blood test indeterminate, invalid or borderline", "Repeat it, or use a skin test"),
  ("Blood test negative", "Infection less likely, but disease still possible"),
 ], "mnemonic": {"hook": "Too Early, Too Weak, Too Sick, Too Young: a negative is not the end.",
  "key": [["Too early", "repeat 8&ndash;10 weeks after exposure"], ["Too weak", "immunosuppression or severe tuberculosis: false negative"], ["Too sick", "symptoms or high clinical suspicion: evaluate for disease now"], ["Too young", "young or immunocompromised contacts: public health now"], ["Unclear blood test", "repeat or use the skin test"], ["Negative blood test", "disease still possible"]]}},

{"id": "crit-l38-igra", "label": "Skin Test vs Blood Test (Interferon-Gamma Release Assay)", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slides 19&ndash;25",
 "cols": ["", "Tuberculin skin test", "Interferon-gamma release assay"], "widths": ["20%", "40%", "40%"], "rows": [
  ("Detects", "Immune response to infection", "Immune response to tuberculosis-specific antigens (blood)"),
  ("Latent vs disease?", "<b>Cannot tell</b>", "<b>Cannot tell</b>"),
  ("BCG vaccine", "Can cause a false positive", "<b>Does not cause a positive</b>: preferred after BCG"),
  ("Visits", "Placement, then a reading at 48&ndash;72 hours", "<b>One visit</b>"),
  ("After treatment", "May stay positive", "May stay positive: monitor by clinical and microbiologic response"),
 ], "mnemonic": {"hook": "Both only say &ldquo;infected&rdquo;; the Blood test Beats BCG in one visit.",
  "key": [["Infected only", "neither separates latent from disease"], ["Blood beats BCG", "no false positive after BCG"], ["One visit", "blood test"], ["Stays positive", "do not use either to monitor treatment"]]}},

{"id": "crit-l38-sputum", "label": "Suspected Pulmonary Tuberculosis: Microbiology", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slide 26",
 "cols": ["Step", "Rule"], "widths": ["28%", "72%"], "rows": [
  ("Collect", "<b>3 sputum specimens, 8&ndash;24 hours apart, at least one early morning</b>"),
  ("Smear and culture", "Acid-fast bacilli smear and mycobacterial culture"),
  ("Molecular", "A <b>rapid molecular test on at least one</b> respiratory specimen"),
  ("Susceptibility", "Molecular and culture-based drug-susceptibility testing"),
  ("HIV", "Offer HIV testing when status is unknown"),
 ], "mnemonic": {"hook": "3-8-1, then SMASH: 3 specimens, 8&ndash;24 hours apart, 1 in the morning; Smear (and culture), Molecular, Susceptibility, HIV.",
  "key": [["3-8-1", "3 specimens, 8&ndash;24 hours apart, 1 early morning"], ["S", "smear (and culture)"], ["M", "rapid molecular test"], ["S", "susceptibility testing"], ["H", "HIV test"]]}},

{"id": "crit-l38-imaging", "label": "Chest Imaging Patterns", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slides 27&ndash;29",
 "cols": ["Picture", "Typical findings"], "widths": ["30%", "70%"], "rows": [
  ("Primary disease", "<b>Hilar or mediastinal adenopathy</b>, infiltrates or effusion"),
  ("Post-primary disease", "<b>Upper lobes</b>, may <b>cavitate</b>"),
  ("Miliary disease", "Diffuse tiny nodules"),
  ("HIV or other immunosuppression", "Atypical patterns"),
  ("Latent infection", "Usually a <b>normal</b> film"),
  ("Prior tuberculosis", "Scarring, volume loss, calcified granulomas (review prior treatment, exclude active disease)"),
  {"note": "Imaging supports suspicion but cannot confirm tuberculosis or reliably determine activity, and cannot tell recent infection, reactivation or reinfection apart."},
 ], "mnemonic": {"hook": "Primary Puffs the hilum; Post-primary Punches holes up top; Miliary is Millet seeds.",
  "key": [["Primary", "hilar or mediastinal nodes, infiltrates, effusion"], ["Post-primary", "upper-lobe cavities"], ["Miliary", "diffuse tiny nodules"], ["Immunosuppressed", "atypical"], ["Latent", "normal film"], ["Old", "scar, volume loss, calcified granulomas"]]}},

{"id": "crit-l38-isolation", "label": "Immediate Management of Pulmonary Tuberculosis", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slide 33",
 "cols": ["Letter", "Action"], "widths": ["12%", "88%"], "rows": [
  ("N", "<b>Notify</b> the local or state tuberculosis program of presumed or confirmed tuberculosis"),
  ("A", "<b>Airborne</b> infection isolation room when indicated"),
  ("N", "Staff wear a fit-tested <b>N95</b> or higher-level respirator"),
  ("S", "Patient <b>source control</b> during transport"),
  ("E", "<b>End</b> isolation by clinical, laboratory and public-health criteria, <b>not a fixed treatment interval</b>"),
 ], "mnemonic": {"hook": "NANSE: Notify, Airborne room, N95, Source control, End by criteria.",
  "key": [["N", "notify the program"], ["A", "airborne isolation room"], ["N", "N95 respirator"], ["S", "source control in transport"], ["E", "end by criteria, not by a calendar"]]}},

{"id": "crit-l38-regimen", "label": "Drug-Susceptible Tuberculosis: Regimens", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slides 34&ndash;36",
 "cols": ["Regimen", "Drugs and length"], "widths": ["30%", "70%"], "rows": [
  ("Standard (slide 34)", "<b>2 months HRZE</b>: isoniazid (H), rifampin (R), pyrazinamide (Z), ethambutol (E); then <b>4 months HR</b>; <b>ethambutol stops once isoniazid and rifampin susceptibility is established</b>; daily therapy with directly observed therapy (in person or by video) supports completion"),
  ("17-week (slide 35)", "<b>Age 12 or older</b>, susceptible pulmonary disease: 8 weeks isoniazid, rifapentine, pyrazinamide, moxifloxacin; then 9 weeks isoniazid, rifapentine, moxifloxacin"),
  ("Selected children, nonsevere (slide 35)", "4 months: 2 months isoniazid, rifampin, pyrazinamide (with or without ethambutol), then 2 months isoniazid and rifampin"),
  ("Resistance and monitoring (slide 36)", "<b>Rifampin resistance: rapid susceptibility testing and expert management</b>; review at least monthly; sputum cultures until conversion, response documented at 2 months; watch liver injury, interactions, toxicity"),
 ], "mnemonic": {"hook": "RIPE for 2, then RI for 4; E Exits early once susceptibility is known.",
  "key": [["R", "rifampin"], ["I", "isoniazid (H)"], ["P", "pyrazinamide (Z)"], ["E", "ethambutol, stops after susceptibility"], ["2 + 4", "6 months total"], ["17 weeks", "8 + 9, age 12 or older"]],
  "breaks": "The slide writes the regimen as HRZE; RIPE is the same four drugs in a different order."}},

{"id": "crit-l38-ltbi", "label": "Latent Tuberculosis Infection: Regimens", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slide 37",
 "cols": ["Code", "Regimen", "Use"], "widths": ["14%", "54%", "32%"], "rows": [
  ("3HP", "<b>Weekly</b> isoniazid plus rifapentine for <b>3 months</b>", "Preferred short regimen"),
  ("4R", "<b>Daily</b> rifampin for <b>4 months</b>", "Preferred short regimen"),
  ("3HR", "<b>Daily</b> isoniazid plus rifampin for <b>3 months</b>", "Preferred short regimen"),
  ("6H or 9H", "Isoniazid for 6 or 9 months", "<b>When rifamycin regimens are unsuitable</b>"),
  {"note": "First exclude tuberculosis disease; check interactions, pregnancy considerations and source-case resistance."},
 ], "mnemonic": {"hook": "The number is the months; H = isoniazid, R = rifampin, P = rifapentine; drop the rifamycin and the months go up (6H, 9H).",
  "key": [["3HP", "3 months, weekly isoniazid + rifapentine"], ["4R", "4 months, daily rifampin"], ["3HR", "3 months, daily isoniazid + rifampin"], ["6H / 9H", "isoniazid alone, rifamycin unsuitable"]]}},

{"id": "crit-l38-ntm", "label": "Nontuberculous Mycobacterial Lung Disease: Diagnosis and MAC Treatment", "color": L38C,
 "tag": "Criteria &middot; Lecture 38 &middot; slides 38&ndash;40",
 "cols": ["Domain", "Requirement"], "widths": ["30%", "70%"], "rows": [
  ("Symptoms and imaging", "Compatible symptoms <b>and</b> imaging (nodular bronchiectasis or fibrocavitary disease)"),
  ("Something else excluded", "Alternative diagnoses excluded"),
  ("Same species", "Usually <b>2 or more sputum cultures with the same species</b>, or <b>one positive bronchial wash or lavage</b> or qualifying biopsy"),
  ("MAC (Mycobacterium avium complex) treatment", "Macrolide-susceptible: <b>azithromycin, ethambutol and a rifamycin</b>, at least <b>12 months after culture conversion</b>; cavitary or severe: <i>may need</i> daily therapy and initial intravenous amikacin; still positive after 6 months or more: <i>may warrant</i> inhaled liposomal amikacin"),
  {"note": "A respiratory isolate alone does not prove disease (slide 38): all domains are required."},
 ], "mnemonic": {"hook": "Three S&rsquo;s to diagnose (Symptoms and Scan, Something else excluded, Same species twice); A-E-R for 12 after conversion.",
  "key": [["S", "symptoms and scan"], ["S", "something else excluded"], ["S", "same species twice, or one wash, lavage or biopsy"], ["A-E-R", "azithromycin, ethambutol, rifamycin"], ["12", "months after culture conversion"]]}},
]

TOPICS = [
{"id": "l38-emph", "label": "★ Professor Emphasized — Infection vs Disease", "color": "#b8860b", "rows": [
 ["★ Three decisions", "Is disease plausible? Could the patient be infectious? Which diagnostic and treatment pathway, and when to involve the health department or a specialist (3:09)."],
 ["★ The distinction", "Infection versus disease &ldquo;determines infectiousness, evaluation, and treatment&rdquo; (3:07): latent infection is <b>asymptomatic and not infectious</b>."],
 ["★ Guidance coming", "Posted &ldquo;this weekend&rdquo; at the end of the slides for respiratory infections and tuberculosis (4:00)."],
 ["Watch out", "He called fever and night sweats &ldquo;pathognomonic&rdquo;; the slide lists them as manifestations only, and symptoms may be absent."],
]},
{"id": "l38-basics", "label": "Mycobacteria, Spread &amp; Presentation", "color": "#7a2d30", "rows": [
 ["Biology", "<b>Acid-fast bacilli</b>, lipid-rich walls with <b>mycolic acids</b>; slow growth (culture takes weeks, molecular tests are rapid); a smear <b>cannot tell</b> tuberculosis from nontuberculous species."],
 ["Species", "<i>M. tuberculosis</i> complex (<i>M. tuberculosis</i>, <i>M. bovis</i>, <i>M. africanum</i>); nontuberculous: <i>M. avium</i> complex, <i>M. kansasii</i>, <i>M. abscessus</i>."],
 ["Spread", "<b>Pulmonary and laryngeal</b> disease, by coughing, speaking, singing; shared indoor air, poor ventilation. Latent infection does not spread; extrapulmonary usually does not."],
 ["Pulmonary disease", "Persistent cough, hemoptysis or pleuritic pain, fever, night sweats, weight loss; <b>don&rsquo;t wait 3 weeks</b> in high-risk patients; <b>a normal exam does not exclude it</b>; children, elders and the immunocompromised present atypically."],
 ["Extrapulmonary", "Nodes (painless enlargement), pleura (effusion), central nervous system (headache, altered mental status), spine (back pain, vertebral destruction), disseminated (fever, weight loss)."],
 ["Differential", "Nontuberculous mycobacteria, bacterial pneumonia or abscess, histoplasmosis and other endemic fungi, bronchiectasis, aspergillosis, lung cancer and other cavities."],
]},
{"id": "l38-rx", "label": "Treatment &amp; Follow-Up", "color": "#2f5d6b", "rows": [
 ["Before latent treatment", "<b>Exclude disease</b>; a positive skin or blood test still needs evaluation for disease."],
 ["During treatment", "Monthly review of adherence, symptoms, adverse effects; <b>liver injury</b>; cultures until conversion; skin and blood tests may stay positive (don&rsquo;t use them to monitor)."],
 ["After tuberculosis", "Persistent dyspnea may be <b>bronchiectasis</b>; fibrotic lesions mean review prior treatment and exclude active disease; new symptoms mean reassess for recurrence."],
 ["Nontuberculous", "Risk with <b>bronchiectasis, chronic obstructive pulmonary disease, immune dysfunction</b>; environmental; an isolate alone is not disease; other species need susceptibility-guided regimens."],
]},
]
