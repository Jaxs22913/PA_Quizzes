# -*- coding: utf-8 -*-
"""CMS I Exam 6, Lectures 37-38: the lecturer's STUDY-FOCUS points and which questions practise each one.

Prof. Bobilin posted revised decks on 2026-10-31 with one study-focus slide per lecture:
  L37 "37. Respiratory Infections - Bobilin - 10-29-2026 SV.pptx", Slide 127 (Slide 128 repeats it with the
      footer "Covers Questions 1-25"; he told the class about 20 questions on this lecture)
  L38 "38. Mycobacterial Infections including Tuberculosis - Bobilin - 10-29-2025 SV.pptx", Slide 41
      ("Covers Questions 1-10"; about 10 questions)

POINTS   every focus point, split at the grain the slide lists them, with the slide's own words (`slide`).
EXISTING the already-built L37/L38 pool questions that practise a point, keyed by the opening of the stem
         (unique within the lecture's pools; asserted by tools/cms_e6_focus_coverage.py). A question may
         practise two points when it genuinely exercises both (green sputum + bronchitis vs pneumonia).
NEW items (tools/cms_e6l37_focus_pool.py / _focus_vig.py, cms_e6l38_focus_*.py) carry their points in a
         "focus" list on the question itself.

Used by tools/cms_e6_focus_coverage.py (writes tools/cms_e6_focus_coverage.json), tools/cms_e6_focus_partition.py
(the two Study Focus sets) and tools/cms_e6_masters_partition.py (focus items preferred for the L37/L38 slots).
"""

POINTS = [
 # ---------------------------------------------------------------- Lecture 37, slide 127
 ("l37-flu-vax", "l37", "Prevention & vaccines", "Influenza vaccine product selection",
  "Know influenza product selection"),
 ("l37-rsv", "l37", "Prevention & vaccines", "RSV vaccine age/risk eligibility",
  "RSV age/risk eligibility"),
 ("l37-pneumo-seq", "l37", "Prevention & vaccines", "Pneumococcal sequencing, incl. when PCV15 requires PPSV23",
  "pneumococcal sequencing—especially when PCV15 requires PPSV23"),
 ("l37-bronch-vs-pna", "l37", "Bronchitis & stewardship", "Uncomplicated viral bronchitis vs pneumonia",
  "Distinguish uncomplicated viral bronchitis from pneumonia."),
 ("l37-sputum-color", "l37", "Bronchitis & stewardship", "Sputum color alone does not justify antibiotics",
  "Sputum color alone does not justify antibiotics."),
 ("l37-cap-confirm", "l37", "CAP severity & treatment", "CAP diagnostic confirmation",
  "Review diagnostic confirmation"),
 ("l37-psi", "l37", "CAP severity & treatment", "Pneumonia Severity Index (PSI)", "PSI"),
 ("l37-severe-cap", "l37", "CAP severity & treatment", "Severe-CAP criteria", "severe-CAP criteria"),
 ("l37-op-nocomorb", "l37", "CAP severity & treatment", "Outpatient CAP regimen without comorbidities",
  "outpatient regimens with and without comorbidities"),
 ("l37-op-comorb", "l37", "CAP severity & treatment", "Outpatient CAP regimen with comorbidities",
  "outpatient regimens with and without comorbidities"),
 ("l37-resistant", "l37", "CAP severity & treatment", "Risk-based resistant (MRSA/Pseudomonas) coverage",
  "risk-based resistant coverage"),
 ("l37-hap-timing", "l37", "HAP, VAP & aspiration", "HAP/VAP acquisition timing", "Use acquisition timing"),
 ("l37-hap-cultures", "l37", "HAP, VAP & aspiration", "HAP/VAP cultures", "cultures"),
 ("l37-antibiogram", "l37", "HAP, VAP & aspiration", "Local antibiograms", "local antibiograms"),
 ("l37-deescalate", "l37", "HAP, VAP & aspiration", "De-escalation", "de-escalation"),
 ("l37-pneumonitis", "l37", "HAP, VAP & aspiration", "Chemical pneumonitis vs aspiration pneumonia",
  "Separate chemical pneumonitis from aspiration pneumonia"),
 ("l37-anaerobes", "l37", "HAP, VAP & aspiration", "Anaerobic coverage only for abscess/empyema",
  "reserve anaerobic coverage for abscess/empyema"),
 ("l37-pjp-sampling", "l37", "Opportunistic & atypical infection", "Pneumocystis (PJP) sampling", "PJP sampling"),
 ("l37-pcr-limits", "l37", "Opportunistic & atypical infection", "PCR limitations", "PCR limitations"),
 ("l37-steroid-threshold", "l37", "Opportunistic & atypical infection",
  "Steroid thresholds (Pneumocystis: room-air PaO2 below 70 mm Hg)", "steroid thresholds"),
 ("l37-histo-severity", "l37", "Opportunistic & atypical infection", "Histoplasmosis treatment by severity",
  "histoplasmosis treatment by severity"),
 ("l37-psittacosis", "l37", "Opportunistic & atypical infection", "Psittacosis: bird exposure, doxycycline",
  "bird exposure with doxycycline for psittacosis"),
 ("l37-rapid-flu", "l37", "Influenza & COVID-19", "Interpreting a negative rapid influenza test",
  "Interpret negative rapid influenza tests"),
 ("l37-flu-48h", "l37", "Influenza & COVID-19", "Treat high-risk influenza even after 48 hours",
  "treat high-risk influenza even after 48 hours"),
 ("l37-covid-outpt", "l37", "Influenza & COVID-19", "Early outpatient COVID-19 antivirals",
  "early outpatient COVID antivirals"),
 ("l37-covid-hypox", "l37", "Influenza & COVID-19", "Hypoxemic inpatient COVID-19 care",
  "hypoxemic inpatient care"),
 # ---------------------------------------------------------------- Lecture 38, slide 41
 ("l38-smear", "l38", "Smear ≠ species identification", "An acid-fast smear cannot tell TB from NTM",
  "An AFB-positive smear supports mycobacteria but cannot distinguish TB from NTM. Confirm species with molecular testing and culture."),
 ("l38-igra-bcg", "l38", "Choose the right infection test", "Prefer IGRA after BCG", "Prefer IGRA after BCG."),
 ("l38-tst5", "l38", "Choose the right infection test", "TST ≥5 mm positive in HIV or recent close contact",
  "In HIV or recent close contact, TST induration ≥5 mm is positive and requires evaluation for active disease."),
 ("l38-rule-out", "l38", "Rule out active TB first",
  "TST/IGRA show infection, not latent vs active; rule out active TB before preventive therapy",
  "TST and IGRA show infection—not latent versus active TB. Complete clinical evaluation and chest imaging before preventive therapy."),
 ("l38-sputum", "l38", "Collect the right specimens",
  "Three sputa 8-24 h apart incl. early morning; AFB smear/culture + one rapid molecular test",
  "Collect three sputum specimens 8–24 hours apart, including one early-morning sample. Send AFB smear/culture and one rapid molecular test."),
 ("l38-retest", "l38", "Act on exposure and suspicion", "Repeat an early negative test 8-10 weeks after last exposure",
  "Repeat an early negative test 8–10 weeks after the last exposure."),
 ("l38-isolation", "l38", "Act on exposure and suspicion", "Immediate airborne isolation + TB-program coordination",
  "Suspected pulmonary TB requires immediate airborne isolation and TB-program coordination."),
 ("l38-mac-dx", "l38", "Diagnose and treat MAC correctly",
  "MAC diagnosis: symptoms + imaging + usually ≥2 same-species cultures",
  "One isolate is insufficient: confirm symptoms, imaging, and usually ≥2 same-species sputum cultures."),
 ("l38-mac-rx", "l38", "Diagnose and treat MAC correctly",
  "MAC treatment: azithromycin + ethambutol + rifamycin ≥12 months after culture conversion",
  "Use azithromycin + ethambutol + rifamycin for ≥12 months after culture conversion."),
]
POINT_IDS = [p[0] for p in POINTS]

# stem opening -> focus point ids (existing L37/L38 pool questions; review state is read at run time). The three
# coronavirus items whose options set the outpatient antiviral against the hospital (dexamethasone) pathway carry both.
EXISTING = {
 # ---- L37 vaccines
 "Which is the broadest group recommended to receive an influenza vaccine every year?": ["l37-flu-vax"],
 "Which influenza vaccine types are preferred for adults aged 65 or older?": ["l37-flu-vax"],
 "Which influenza vaccine type should be avoided during pregnancy?": ["l37-flu-vax"],
 "What does a history of egg allergy require before influenza vaccination?": ["l37-flu-vax"],
 "A 26-year-old woman who is 14 weeks pregnant comes in during October": ["l37-flu-vax"],
 "A 45-year-old man gets hives whenever he eats eggs": ["l37-flu-vax"],
 "Which adults should receive a respiratory syncytial virus vaccine?": ["l37-rsv"],
 "A 78-year-old woman received a respiratory syncytial virus vaccine last year": ["l37-rsv"],
 "For an eligible adult who has never had a pneumococcal conjugate vaccine": ["l37-pneumo-seq"],
 "A 55-year-old man with no medical conditions has never received a pneumococcal vaccine": ["l37-pneumo-seq"],
 # ---- L37 bronchitis
 "Which test is needed to diagnose uncomplicated acute bronchitis?": ["l37-bronch-vs-pna"],
 "In acute bronchitis, what does green or yellow sputum indicate?": ["l37-sputum-color"],
 "What is the role of antibiotics in uncomplicated acute bronchitis?": ["l37-sputum-color"],
 "In a patient with suspected acute bronchitis, which lung finding should make you think of pneumonia": ["l37-bronch-vs-pna"],
 "Which presentation separates pneumonia from acute bronchitis?": ["l37-bronch-vs-pna"],
 "A 34-year-old woman has had a cough for 10 days that began with a cold. Her sputum is green": ["l37-sputum-color", "l37-bronch-vs-pna"],
 "A 41-year-old man has had a cough for 5 days. His temperature is 102.4": ["l37-bronch-vs-pna", "l37-cap-confirm"],
 "A 52-year-old woman with acute bronchitis was managed with supportive care 10 days ago": ["l37-bronch-vs-pna", "l37-cap-confirm"],
 # ---- L37 CAP
 "Which test confirms suspected pneumonia?": ["l37-cap-confirm"],
 "Alongside clinical judgment, which tool is preferred to support the admission decision": ["l37-psi"],
 "A Pneumonia Severity Index total of 95 points falls in which risk class?": ["l37-psi"],
 "Which Pneumonia Severity Index finding adds the most points?": ["l37-psi"],
 "A 77-year-old man with community-acquired pneumonia has a PSI (Pneumonia Severity Index) total of 104": ["l37-psi"],
 "Which finding by itself marks community-acquired pneumonia as severe?": ["l37-severe-cap"],
 "A 63-year-old man with community-acquired pneumonia remains hypotensive after intravenous fluids": ["l37-severe-cap"],
 "A 57-year-old man with community-acquired pneumonia is intubated for respiratory failure": ["l37-severe-cap", "l37-resistant"],
 "What is the minimum antibiotic duration for severe community-acquired pneumonia?": ["l37-severe-cap"],
 "Which oral regimen fits an adult outpatient with community-acquired pneumonia and no comorbidities": ["l37-op-nocomorb"],
 "When may a macrolide alone be used for a healthy outpatient": ["l37-op-nocomorb"],
 "A 32-year-old woman with no medical conditions has community-acquired pneumonia and is stable for outpatient": ["l37-op-nocomorb"],
 "A 28-year-old man with no medical conditions has community-acquired pneumonia and is stable for outpatient": ["l37-op-nocomorb"],
 "A 30-year-old man with no medical conditions has community-acquired pneumonia confirmed on chest radiograph": ["l37-op-nocomorb"],
 "A 64-year-old woman with type 2 diabetes and chronic heart failure has community-acquired pneumonia": ["l37-op-comorb"],
 "A 59-year-old man with alcoholism and chronic liver disease has community-acquired pneumonia": ["l37-op-comorb"],
 "A 70-year-old woman with chronic obstructive pulmonary disease and diabetes has community-acquired pneumonia": ["l37-op-comorb"],
 "Which agent provides coverage for methicillin-resistant Staphylococcus aureus in pneumonia?": ["l37-resistant"],
 "Which regimen fits a hospitalized adult with nonsevere community-acquired pneumonia and no risk": ["l37-resistant"],
 "A 64-year-old woman with severe community-acquired pneumonia in the intensive care unit had methicillin": ["l37-resistant"],
 "A 68-year-old man with severe chronic obstructive pulmonary disease is admitted to the intensive care unit": ["l37-resistant"],
 "A 60-year-old woman is admitted to a general ward with nonsevere community-acquired pneumonia": ["l37-resistant"],
 "A 66-year-old man admitted with nonsevere community-acquired pneumonia is improving on ceftriaxone": ["l37-deescalate"],
 # ---- L37 HAP / VAP / aspiration
 "How is hospital-acquired pneumonia defined?": ["l37-hap-timing"],
 "A 68-year-old woman is admitted for repair of a hip fracture.": ["l37-hap-timing"],
 "A 59-year-old man has been intubated and mechanically ventilated for 3 days": ["l37-hap-timing"],
 "A 70-year-old man hospitalized for 6 days after a stroke develops hospital-acquired pneumonia": ["l37-antibiogram"],
 "A 63-year-old woman develops ventilator-associated pneumonia on day 5 of mechanical ventilation. Methicillin-resistant": ["l37-antibiogram"],
 "A 58-year-old man with ventilator-associated pneumonia has had an adequate response to culture-directed": ["l37-deescalate"],
 "What is the core problem in aspiration pneumonitis?": ["l37-pneumonitis"],
 "How is aspiration pneumonitis managed when bacterial infection is not suspected?": ["l37-pneumonitis"],
 "When is anaerobic coverage added in aspiration pneumonia?": ["l37-anaerobes"],
 "A 54-year-old woman vomits and aspirates during a witnessed seizure": ["l37-pneumonitis"],
 "A 47-year-old man who aspirated gastric contents during a witnessed seizure": ["l37-pneumonitis"],
 "A 79-year-old man with dysphagia after a stroke lives at home": ["l37-anaerobes"],
 # ---- L37 opportunistic and atypical
 "For suspected Pneumocystis pneumonia with a negative induced sputum": ["l37-pjp-sampling"],
 "A 54-year-old woman who had a kidney transplant takes long-term prednisone": ["l37-pjp-sampling"],
 "In Pneumocystis pneumonia associated with human immunodeficiency virus, which room-air arterial oxygen": ["l37-steroid-threshold"],
 "A 36-year-old woman with human immunodeficiency virus infection starts trimethoprim-sulfamethoxazole": ["l37-steroid-threshold"],
 "How is mild acute histoplasmosis in an immunocompetent adult usually managed?": ["l37-histo-severity"],
 "For at least how long is chronic cavitary histoplasmosis treated?": ["l37-histo-severity"],
 "A healthy 29-year-old woman has acute histoplasmosis confirmed by urine antigen": ["l37-histo-severity"],
 "How is psittacosis primarily acquired?": ["l37-psittacosis"],
 "What is the preferred treatment for psittacosis in adults?": ["l37-psittacosis"],
 "A 36-year-old pet-shop employee has had a week of fever": ["l37-psittacosis"],
 "A 52-year-old woman who keeps several parakeets at home is diagnosed with psittacosis": ["l37-psittacosis"],
 # ---- L37 influenza and COVID-19
 "A rapid influenza antigen test is negative during high community activity": ["l37-rapid-flu"],
 "A 52-year-old woman has had a sudden fever, myalgias, a frontal headache and a dry cough": ["l37-rapid-flu"],
 "For a high-risk patient whose influenza symptoms began more than 48 hours ago": ["l37-flu-48h"],
 "A 29-year-old woman who is 24 weeks pregnant has had 3 days of fever": ["l37-flu-48h"],
 "A 71-year-old man with chronic obstructive pulmonary disease and heart failure is hospitalized on day 5 of influenza": ["l37-flu-48h"],
 "Which treatment fits a high-risk outpatient with mild coronavirus disease 2019": ["l37-covid-outpt", "l37-covid-hypox"],
 "Which treatment is avoided in coronavirus disease 2019 without hypoxemia": ["l37-covid-outpt"],
 "A 70-year-old unvaccinated man with diabetes and heart failure has mild coronavirus disease 2019": ["l37-covid-outpt", "l37-covid-hypox"],
 "A 30-year-old woman who is 20 weeks pregnant and has diabetes tests positive for both influenza": ["l37-covid-outpt"],
 "A 68-year-old man with diabetes has mild coronavirus disease 2019 that began 2 days ago": ["l37-covid-outpt"],
 "A 58-year-old man is admitted with coronavirus disease 2019. His oxygen saturation is 90%": ["l37-covid-hypox", "l37-covid-outpt"],
 "A 61-year-old woman hospitalized with coronavirus disease 2019 and hypoxemia has an elevated D-dimer": ["l37-covid-hypox"],
 "A 63-year-old woman hospitalized with coronavirus disease 2019 and hypoxemia is on dexamethasone": ["l37-covid-hypox"],
 # ---- L38
 "What does a positive acid-fast smear of sputum establish?": ["l38-smear"],
 "Why does identifying the mycobacterial species matter once acid-fast bacilli are found?": ["l38-smear"],
 "A 66-year-old woman with bronchiectasis has had a chronic cough with sputum for months. Her sputum acid-fast": ["l38-smear"],
 "Why is an interferon-gamma release assay preferred over the tuberculin skin test for most BCG": ["l38-igra-bcg"],
 "A 32-year-old man who received BCG (bacille Calmette-Guérin) vaccine in infancy": ["l38-igra-bcg"],
 "Which group uses a tuberculin skin test induration cut-off of 5 mm or more?": ["l38-tst5"],
 "A 35-year-old man with human immunodeficiency virus infection has a tuberculin skin test read at 60 hours": ["l38-tst5"],
 "A 45-year-old man's wife was diagnosed with infectious pulmonary tuberculosis last month": ["l38-tst5"],
 "After a positive tuberculin skin test, what separates latent infection from tuberculosis disease?": ["l38-rule-out"],
 "What must be done before starting treatment for latent tuberculosis infection?": ["l38-rule-out"],
 "A 34-year-old woman who works in a setting with ongoing tuberculosis transmission has a positive interferon": ["l38-rule-out"],
 "A 38-year-old man has a positive interferon-gamma release assay on targeted testing": ["l38-rule-out"],
 "A 52-year-old man has 12 mm of induration on a tuberculin skin test. His chest radiograph shows": ["l38-rule-out"],
 "A 44-year-old woman has a positive interferon-gamma release assay. She also reports 5 weeks of cough": ["l38-rule-out"],
 "How many sputum specimens are collected when pulmonary tuberculosis is suspected?": ["l38-sputum"],
 "How far apart are the sputum specimens for suspected pulmonary tuberculosis collected?": ["l38-sputum"],
 "Which requirement applies to the sputum specimens collected for suspected pulmonary tuberculosis?": ["l38-sputum"],
 "Which tests are requested on the sputum specimens in suspected pulmonary tuberculosis?": ["l38-sputum"],
 "A 51-year-old man has 5 weeks of cough, night sweats and weight loss, and pulmonary tuberculosis is suspected": ["l38-sputum"],
 "A 43-year-old woman with suspected pulmonary tuberculosis has three sputum specimens collected": ["l38-sputum"],
 "After a recent tuberculosis exposure, a first tuberculin skin test is negative": ["l38-retest"],
 "A 28-year-old woman shared an office with a coworker diagnosed with infectious pulmonary tuberculosis": ["l38-retest"],
 "When is the local or state tuberculosis program notified?": ["l38-isolation"],
 "Where is a hospitalized patient with possible infectious pulmonary tuberculosis placed?": ["l38-isolation"],
 "A 48-year-old man is admitted with cough, night sweats and weight loss, and his sputum smear shows": ["l38-isolation"],
 "A 62-year-old man's chest radiograph and sputum smear lead his clinician to presume pulmonary tuberculosis": ["l38-isolation"],
 "What does a single respiratory isolate of nontuberculous mycobacteria establish?": ["l38-mac-dx"],
 "Which microbiologic result usually meets the criteria for nontuberculous mycobacterial lung disease?": ["l38-mac-dx"],
 "Besides compatible symptoms, compatible imaging and microbiology, which domain is required": ["l38-mac-dx"],
 "A 68-year-old woman with bronchiectasis has a year of chronic cough with sputum, fatigue and weight loss": ["l38-mac-dx"],
 "A 70-year-old man with chronic obstructive pulmonary disease has a single sputum culture that grows": ["l38-mac-dx"],
 "A 64-year-old woman has chronic cough, sputum, fatigue and weight loss. Computed tomography shows fibrocavitary": ["l38-mac-dx"],
 "Which regimen treats macrolide-susceptible Mycobacterium avium complex lung disease?": ["l38-mac-rx"],
 "When does the minimum 12-month course for Mycobacterium avium complex lung disease start counting?": ["l38-mac-rx"],
 "A 67-year-old woman meets the criteria for macrolide-susceptible Mycobacterium avium complex": ["l38-mac-rx"],
 "A 66-year-old man starts treatment for macrolide-susceptible Mycobacterium avium complex": ["l38-mac-rx"],
}


def focus_of(q):
    """The focus points a question practises: its own "focus" list (new items) or the EXISTING map."""
    if q.get("focus"):
        return list(q["focus"])
    hits = [v for k, v in EXISTING.items() if q["q"].startswith(k)]
    assert len(hits) <= 1, "two EXISTING keys match %r" % q["q"][:70]
    return list(hits[0]) if hits else []
