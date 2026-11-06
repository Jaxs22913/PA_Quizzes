# -*- coding: utf-8 -*-
"""Patient case scripts for the voice-based Pulmonary OSCE practice station (2026-11-06).

Each case is the ground truth the simulated patient answers from (door card, persona, opening line, facts),
the physical-examination findings (overrides of the maneuver catalog in tools/_osce_pulm_catalog.py; every
maneuver not overridden returns the catalog's NORMAL finding), the tests a student can order, and the
grader's answer key.

Case list: nine common and high-stakes pulmonary presentations from the Clinical Medicine and Surgery I
pulmonary lectures (Exam 6, Lectures 33-38; Exam 7, Lectures 39-44), with the examination findings from the
Physical Diagnosis 2 thorax lecture. They are listed alphabetically by the patient's surname.

Grounding: every clinical fact that bears on the diagnosis (findings, results, plan) comes from the decks on
the case's `cites` line (visible slide text and pictures only, never speaker notes). Names, jobs, families and
speech are invented. Review-of-systems answers the decks do not cover are realistic negatives consistent with
the case.

Schema of each case: the same as tools/_osce_cardiac_cases.py; the self-check at the bottom enforces it.
"""

CASES = [

# =====================================================================================================
# CHRONIC OBSTRUCTIVE PULMONARY DISEASE (acute exacerbation, emergency department)
# =====================================================================================================
dict(
  id="pulmonary-chronic-obstructive-pulmonary-disease",
  condition="Chronic obstructive pulmonary disease",
  cites=("CMS L36 Chronic Obstructive Pulmonary Disease, slides 9, 12, 14, 16, 18, 20-21, 24, 26-28, 30-32, 34, "
         "37-38, 40, 43-44, 46, 48-49, 53-64, 66; CMS L33 Oxygen Delivery slides 16, 25; CMS L34 Acid-Base slides 5, "
         "19, 21-23, 25, 27-28, 59; CMS L42 Pulmonary Vascular Disorders slides 53-54; PD2 Thorax slides 16-17, "
         "22, 32-35, 40, 42-44, 47-48, 56"),
  door=dict(
    name="Walter Abernathy", sex="male", age=61, dob="February 19, 1965",
    setting="Emergency department",
    cc="\"My breathing is worse.\"",
    vitals=[("Blood pressure", "148/86 mmHg"),
            ("Heart rate", "108 beats per minute, regular"),
            ("Respiratory rate", "28 breaths per minute"),
            ("Temperature", "99.8 °F (37.7 °C)"),
            ("Oxygen saturation", "86% on room air"),
            ("Height and weight", "6 feet 3 inches, 175 pounds (body mass index 21.9)")],
  ),
  persona=("A 61-year-old shipyard welder, tall and thin, gruff but polite, sitting bolt upright and leaning on his knees, "
           "breathing out through pursed lips. He can only get out a few words at a time and gets irritated by "
           "long questions. He plays it down ('just my emphysema acting up') but is privately frightened of ending "
           "up on oxygen and of losing his job. He is honest about his smoking and a little ashamed of it."),
  opening="Can't get my breath. This cold went to my chest, and my inhaler isn't touching it.",
  facts=[
    ("Full name", "Walter Abernathy."),
    ("Date of birth", "February 19, 1965."),
    ("Onset", "My grandson gave me a cold last Friday. By Monday it went to my chest. Harder to breathe every day "
              "since."),
    ("Location", "My whole chest. Both sides."),
    ("Duration", "Four days, getting worse. Doesn't let up now, even sitting still."),
    ("Character", "Like I can't get the air out before I need the next breath. Tight and heavy."),
    ("Alleviating factors", "Sitting up, leaning on something. The albuterol used to help. Now it barely does."),
    ("Aggravating factors", "Any walking. Talking. Lying down. The coughing fits."),
    ("Radiation", "No. It doesn't go anywhere."),
    ("Severity", "Eight out of ten. Worst it's ever been."),
    ("Temporal pattern", "Worse every day since Monday. Mornings are bad till I cough the junk up."),
    ("Prior episodes", "A flare in February. My doctor gave me prednisone and an antibiotic, and I got over it at "
                       "home. Never been in the hospital for my lungs."),
    ("Cough", "Every morning for years. My smoker's cough. Since Monday it's all day, and I can't stop once I "
              "start."),
    ("Sputum", "Usually a little white stuff in the morning. Now it's thick, yellow-green, a lot more. Maybe half "
               "a cup a day."),
    ("Coughing up blood", "No blood."),
    ("Shortness of breath", "Even sitting here. Had to stop twice walking in from the car."),
    ("How far they can walk", "Before this cold, about a block on flat ground, then I'd have to stop for breath. "
                              "Now I can barely get to the bathroom."),
    ("Wheezing", "Yes. My wife says I sound like a squeaky toy."),
    ("Chest pain with breathing", "No sharp pain when I breathe. My chest muscles are sore from coughing, that's "
                                  "all."),
    ("Fever, chills or night sweats", "Felt hot and had chills last night. We don't have a thermometer. No "
                                      "sweats."),
    ("Weight loss", "No. About 175 for years."),
    ("Orthopnea and waking up short of breath", "Slept in the recliner the last two nights. Easier to breathe and "
                                                "cough sitting up. I don't wake up gasping. Before this I slept "
                                                "flat on one pillow."),
    ("Leg swelling or calf pain", "No. Ankles skinny as ever. No calf pain."),
    ("Recent travel, immobility or surgery", "No trips, no surgery. Sitting around more since Monday, but I get "
                                             "up."),
    ("Sick contacts", "My grandson, he's six, had a bad cold last week. My wife's got the sniffles now too."),
    ("Constitutional", "Wiped out. Not hungry. No weight loss before this."),
    ("Heart symptoms", "Heart's racing since the cold, and the albuterol makes it worse. No chest pressure. No "
                       "fainting."),
    ("Ear, nose and throat", "Stuffy nose and a sore throat last weekend. Mostly gone."),
    ("Heartburn or reflux", "A little heartburn now and then. Tums take care of it."),
    ("Anything else", "No. It's the breathing. My wife made me come. She says I look gray."),
    ("Chronic conditions", "Emphysema, high blood pressure and high cholesterol."),
    ("Known lung disease", "Emphysema. They found it six years ago with the breathing test. I did the test again in "
                           "March, and the lung doctor said my lungs move less than half the air they should."),
    ("Surgeries and procedures", "Hernia repair in 2010. A colonoscopy a few years back."),
    ("Hospitalizations", "Just the hernia. Never for my lungs. Never on a breathing machine."),
    ("Prescription medications", "Tiotropium, the Spiriva, every morning for about five years. Albuterol inhaler "
                                 "when I need it. Lisinopril 20 milligrams for my blood pressure, and atorvastatin "
                                 "40 at night."),
    ("Taking them as prescribed", "Every day. But since Tuesday I've used the albuterol every two hours, more than "
                                  "they told me."),
    ("Over-the-counter medicines and supplements", "Tums sometimes. A cough syrup this week. No supplements."),
    ("Allergies", "No drug allergies."),
    ("Tobacco", "Since I was sixteen. A pack a day until two years ago, then half a pack. Had two this "
                "morning."),
    ("Vaping and marijuana", "No. Never tried them."),
    ("Alcohol", "A couple of beers on a Saturday, watching the game."),
    ("Recreational drugs", "No."),
    ("Occupation and exposures", "Welder at the shipyard, thirty-nine years, still working. Lots of fumes and "
                                 "smoke. We didn't wear masks for most of it. I wear one now, mostly."),
    ("Home and environment", "One-story house. Gas heat. No wood stove. No pets."),
    ("Living situation", "With my wife, Carol. Thirty-five years married. She drove me in."),
    ("Immunizations", "Flu shot last year. Not yet this year. Never had the pneumonia shot."),
    ("Tuberculosis exposure or testing", "They tested me at the shipyard years ago. It was fine. Nobody I know has "
                                         "had it."),
    ("Family history, mother", "My mother died of a stroke at 80."),
    ("Family history, father", "My father had emphysema. He smoked. Died at 72."),
    ("Family history, siblings", "My older brother had a heart attack at 66. He's alive. My sister's healthy."),
    ("What they think it is", "My emphysema acting up from this cold. Same as February, but worse."),
    ("Concerns", "That I'll end up on oxygen for good. That I'll lose my job. And I don't want to be a burden on "
                 "Carol."),
    ("Rescue inhaler use this week", "Every two hours since Tuesday. It used to last four hours. Now I barely feel "
                                     "it."),
    ("Last albuterol dose", "Four puffs in the car on the way here."),
    ("Flare-ups in the past year", "Just the one in February, treated at home. This is the second."),
    ("Home oxygen", "No. Never been on oxygen."),
    ("Confusion or sleepiness", "No. Tired, but my head's clear. Carol says I'm making sense."),
    ("Trying to quit smoking", "Tried the patch once, ten years ago, for a week. I know I should quit. Maybe this "
                               "is the time."),
    ("Breathing class", "The lung doctor mentioned a breathing class. I never went."),
  ],
  questions=["Am I going to need oxygen at home for good?",
             "Do I have to stay in the hospital?",
             "When can I go back to work?"],
  # CMS L36 slides 20-21 (vitals, barrel chest, pursed lips, accessory muscles, tripoding; cyanosis of the lips,
  # jugular veins distended in expiration, decreased sounds with wheezes and crackles, paradoxical lower intercostal
  # retraction, distant heart sounds heard at the epigastrium); PD2 Thorax slides 34 (barrel chest above 0.9), 35
  # (retraction in chronic obstructive disease), 40 (decreased fremitus), 42 (generalized hyperresonance), 47 (coarse
  # crackles), 48 (rhonchi clear with coughing), 56 (decreased voice sounds in the hyperinflated lung)
  exam={
    "position": ("He sits bolt upright on the edge of the stretcher, leaning forward with his hands braced on his "
                 "knees (tripod position), and cannot lie back."),
    "general-survey": ("Tall, thin man in moderate respiratory distress. Alert and oriented and answering "
                       "appropriately, but speaking only in short phrases of four or five words. Breathing out "
                       "through pursed lips, with an audible expiratory wheeze. A faint bluish tinge to the lips. No "
                       "sweating."),
    "thorax-inspect": ("The chest is barrel shaped and symmetric, with no deformities, lesions or bruising. Both "
                       "sides rise together with no lag. The lower intercostal spaces draw inward with each breath "
                       "in (paradoxical retraction from the flattened diaphragm)."),
    "breathing-pattern": ("Respiratory rate 28, regular and labored, with pursed-lip breathing and a markedly "
                          "prolonged expiratory phase."),
    "accessory-muscles": ("The sternocleidomastoid and scalene muscles contract with every breath in, and the "
                          "abdominal muscles tighten with every breath out."),
    "lips-cyanosis": "A faint bluish tinge to the lips and tongue: central cyanosis.",
    "nails": ("The nail beds are dusky. No clubbing: the normal angle at the nail base is kept, and the nail bed "
              "is firm."),
    "ap-diameter": ("Increased: the front-to-back depth of the chest nearly equals its width (a ratio of about 1.0, "
                    "above 0.9). Barrel chest."),
    "fremitus": "Tactile fremitus is diminished and symmetric posteriorly, laterally and anteriorly.",
    "percuss-posterior": "Posterior chest: diffusely hyperresonant and symmetric.",
    "percuss-lateral": "Lateral chest: hyperresonant and symmetric on both sides.",
    "percuss-anterior": "Anterior chest: hyperresonant and symmetric over both upper lobes.",
    "diaphragm-excursion": ("Decreased: about 2 centimeters on each side, with the level of dullness low on both "
                            "sides."),
    "ausc-posterior": ("Posterior chest: breath sounds diminished and distant throughout both lungs, with diffuse "
                       "expiratory wheezes, a markedly prolonged expiratory phase, scattered coarse crackles at both "
                       "bases, and low-pitched rhonchi that partly clear after he coughs. No pleural rub."),
    "ausc-lateral": ("Lateral chest: distant breath sounds with expiratory wheezes on both sides, and a few coarse "
                     "crackles low in both axillae."),
    "ausc-anterior": ("Anterior chest: distant breath sounds over both upper lobes, with expiratory wheezes and a "
                      "prolonged expiratory phase. No crackles anteriorly."),
    "bronchophony": ("Transmitted voice sounds are decreased: \"ninety-nine\" is faint and muffled over both lungs. "
                     "No bronchophony."),
    "heart-ausc": ("Distant heart sounds, heard best below the xiphoid in the epigastrium. Regular tachycardia at "
                   "about 108. No murmur, rub or extra heart sound."),
  },
  # neck veins: CMS L36 slide 21; mental status and asterixis: CMS L34 slide 23 (somnolence, confusion, asterixis in
  # respiratory acidosis)
  special=[
    ("neck-veins", "Neck vein inspection",
     "looks at the jugular veins with the head of the bed raised, through several breaths",
     "The jugular veins distend with each forced breath out and collapse with each breath in."),
    ("mental-status", "Mental status and asterixis",
     "checks alertness and orientation, then has the patient hold both arms out with the wrists bent back",
     "Alert and oriented to person, place and time, answering appropriately. No asterixis: the outstretched hands "
     "hold steady without flapping."),
  ],
  must_exam=['ap-diameter', 'accessory-muscles', 'breathing-pattern', 'percuss-posterior', 'ausc-posterior',
             'mental-status'],
  # CMS L36 slide 56: evaluation of an exacerbation is saturation, blood gas, chest X-ray, electrocardiogram,
  # natriuretic peptide and troponin
  tests=[
    # CMS L36 slide 30 (chronic hypercapnia above 45 with raised bicarbonate); CMS L34 slide 59: for a carbon dioxide
    # of 58 an acute rise predicts a bicarbonate of about 26 (1 per 10) and a chronic one about 30 (3.5 per 10), so 29
    # is acute on chronic; slide 19: compensation never brings the pH back to normal. 6.1 + log(29 / 1.74) = 7.32.
    # L36 slide 57: respiratory acidosis is an intensive care criterion.
    dict(id="abg", name="Arterial blood gas",
         aka=["ABG", "arterial blood gas", "blood gas", "VBG", "venous blood gas", "bicarbonate"],
         result=("Drawn on room air: pH 7.32 (low), partial pressure of carbon dioxide 58 mmHg, partial pressure of "
                 "oxygen 52 mmHg, bicarbonate 29 mEq/L (high), oxygen saturation 86%. After the first nebulized "
                 "albuterol and oxygen, he still breathes about 28 times a minute with accessory muscle use."),
         here=True),
    # CMS L36 slides 31-32
    dict(id="cxr", name="Chest X-ray",
         aka=["CXR", "chest film", "chest radiograph", "chest x ray", "chest x-ray", "chest imaging"],
         result=("Hyperinflated, hyperlucent lungs with flattened diaphragms on both sides and a narrow, vertical "
                 "heart. No infiltrate, pneumothorax, pulmonary edema, effusion or mass."),
         here=True),
    dict(id="ecg", name="Electrocardiogram (12-lead)",
         aka=["EKG", "ECG", "12-lead", "12 lead", "electrocardiogram", "heart tracing"],
         result="Sinus tachycardia at 108. No arrhythmia and no ischemic changes.",
         here=True),
    dict(id="bnp", name="B-type natriuretic peptide (BNP)",
         aka=["BNP", "B-type natriuretic peptide", "brain natriuretic peptide", "natriuretic peptide",
              "NT-proBNP"],
         result="Normal: 62 picograms per milliliter.",
         here=True),
    dict(id="troponin", name="Troponin",
         aka=["troponin", "trop", "TnI", "cardiac enzymes", "cardiac markers", "high-sensitivity troponin"],
         result="Normal: no rise.",
         here=True),
    # CMS L36 slides 26-28 and 34: post-bronchodilator ratio below 0.70 confirms it; under 12% improvement means
    # irreversible obstruction; 47% of predicted (NHANES III, 61-year-old man, 6 feet 3 inches) is grade 3, severe
    dict(id="spirometry", name="Spirometry before and after a bronchodilator (most recent, from his chart)",
         aka=["spirometry", "PFT", "PFTs", "pulmonary function tests", "lung function test", "FEV1",
              "breathing test", "pre and post bronchodilator spirometry"],
         result=("From his clinic chart, March of this year (spirometry is not done during a flare). After the "
                 "bronchodilator: forced expiratory volume in 1 second (FEV1) 2.0 L (47% of predicted), forced "
                 "vital capacity (FVC) 3.9 L, ratio 0.51; improvement after the bronchodilator under 12%."),
         here=True),
    # CMS L36 slides 30, 37, 61: blood count for anemia and eosinophils; inhaled corticosteroid considered at 300 or more
    dict(id="cbc", name="Complete blood count with differential",
         aka=["CBC", "CBC with diff", "complete blood count", "blood count", "white count", "differential",
              "eosinophils"],
         result=("White blood cell count normal at 9,800. Hemoglobin normal at 15.4 grams per deciliter, no anemia. "
                 "Eosinophils 150 per microliter."),
         here=True),
    # CMS L42 slides 53-54: Wells 1.5 (heart rate only), so unlikely; he does not pass the rule-out criteria, so a
    # D-dimer, which is negative
    dict(id="d-dimer", name="D-dimer",
         aka=["D-dimer", "d dimer", "dimer", "ddimer"],
         result="Negative.",
         here=True),
  ],
  key=dict(
    diagnosis=("Acute exacerbation of chronic obstructive pulmonary disease (known severe airflow obstruction: "
               "ratio 0.51, forced expiratory volume in 1 second 47% of predicted, grade 3), triggered by a viral "
               "cold, with more breathlessness and more, purulent sputum; acute-on-chronic hypercapnic respiratory "
               "acidosis (pH 7.32, carbon dioxide 58, bicarbonate 29) with resting hypoxemia (saturation 86%, "
               "arterial oxygen 52 mmHg), in moderate respiratory distress and still about 28 breaths a minute with "
               "accessory muscle use after the first treatments: intensive care admission with noninvasive "
               "ventilation"),
    must_not_miss=["Worsening hypercapnic respiratory failure: drowsiness, confusion, asterixis, hemodynamic "
                   "instability, or a falling pH or rising carbon dioxide despite noninvasive ventilation means "
                   "intubation and invasive ventilation",
                   "A second cause hiding behind the exacerbation: pneumonia, pulmonary embolism, acute heart "
                   "failure or a pneumothorax (the chest X-ray, electrocardiogram, natriuretic peptide, troponin "
                   "and D-dimer look for them)"],
    ddx=[
      dict(name="Chronic obstructive pulmonary disease, acute exacerbation",
           support=("Known severe disease (ratio 0.51, 47% of predicted), about 44 pack-years and still smoking, "
                    "39 years of welding fumes; a "
                    "cold, then four days of worsening breathlessness (now at rest) with more sputum that turned "
                    "yellow-green, and albuterol no longer helping. Tripod position, pursed lips, accessory muscle "
                    "use, barrel chest, central cyanosis, hyperresonance, diminished fremitus and distant breath "
                    "sounds with wheezes and coarse crackles; saturation 86%, a blood gas with acute-on-chronic "
                    "respiratory acidosis, and a hyperinflated chest X-ray."),
           against=("Little against it: the low-grade temperature and basal crackles raise pneumonia, which the "
                    "clear chest X-ray answers.")),
      dict(name="Pneumonia",
           support="A cold, then chills, a temperature of 99.8, purulent sputum and coarse crackles at both bases.",
           against=("No focal dullness, increased fremitus, bronchial breath sounds or egophony (fremitus and "
                    "voice sounds are decreased everywhere), and no infiltrate on the chest X-ray.")),
      dict(name="Acute decompensated heart failure",
           support=("Breathlessness, sleeping in a recliner, basal crackles, high blood pressure and a fast heart "
                    "rate."),
           against=("He sits up to breathe and cough, not because he wakes gasping; no leg edema; no third heart "
                    "sound; neck veins fill only on forced expiration; a normal natriuretic peptide and troponin, "
                    "and no edema on the chest X-ray.")),
      dict(name="Pulmonary embolism",
           support="Tachycardia and hypoxemia; he does not pass the pulmonary embolism rule-out criteria.",
           against=("A gradual start after a cold, with purulent sputum; no pleuritic pain, coughing up blood, "
                    "calf swelling, immobility or surgery; Wells score 1.5 (heart rate only), so unlikely, and the "
                    "D-dimer is negative.")),
    ],
    studies=[
      dict(test="Arterial blood gas",
           why=("Usually done only in a deteriorating or severe exacerbation: measures oxygenation and carbon "
                "dioxide retention, and is repeated after oxygen is started to confirm the oxygen rises without the "
                "carbon dioxide rising."),
           expect=("pH 7.32, carbon dioxide 58 mmHg, bicarbonate 29, arterial oxygen 52 mmHg: respiratory "
                   "acidosis, acute on chronic (for this carbon dioxide the bicarbonate would be about 26 if acute and "
                   "about 30 if chronic; 29 lies between, and compensation never brings the pH back to normal). "
                   "Respiratory acidosis is an intensive care criterion, and an arterial oxygen under 55 mmHg needs "
                   "oxygen.")),
      dict(test="Chest X-ray",
           why=("Not diagnostic of the disease, but rules out pneumonia, heart failure and pneumothorax as the "
                "cause."),
           expect=("Overinflated, hyperlucent lungs with flattened diaphragms and a narrow, vertical heart; no "
                   "infiltrate, pneumothorax, edema or effusion.")),
      dict(test="Electrocardiogram",
           why=("Looks for an arrhythmia (a reason to admit) or ischemia behind the breathlessness; long-acting "
                "beta agonists can worsen atrial fibrillation."),
           expect="Sinus tachycardia at 108; no arrhythmia or ischemic change."),
      dict(test="B-type natriuretic peptide and troponin",
           why=("Part of the evaluation of every exacerbation: heart failure or a heart attack as the cause of, or a "
                "partner in, the breathlessness."),
           expect="Both normal: natriuretic peptide 62 picograms per milliliter, no troponin rise."),
      dict(test="Complete blood count with differential",
           why=("Checks for anemia and measures the blood eosinophils, which decide whether an inhaled "
                "corticosteroid is added (300 or more)."),
           expect="No anemia, white count normal, eosinophils 150: no inhaled corticosteroid for now."),
    ],
    plan=[
      ("Oxygen by Venturi mask, which delivers a precise concentration, titrated carefully to a saturation of "
       "about 88 to 92% (societies differ; some say at least 90%), since his arterial oxygen is under 55 mmHg and "
       "his saturation under 88%; repeat the blood gas to confirm the oxygen rises without the carbon dioxide "
       "rising."),
      "Short-acting bronchodilator by nebulizer: albuterol, repeated; continue his tiotropium.",
      ("A systemic corticosteroid (oral, or injectable while he is on the mask) and an antibiotic, because the "
       "breathlessness came with more sputum that turned purulent. Intravenous, because he needs ventilatory "
       "support, even though there is no systemic infection (temperature 99.8, normal white count, clear chest "
       "X-ray): doxycycline or a macrolide such as azithromycin, both given intravenously."),
      ("Admit to the intensive care unit: respiratory acidosis is an intensive care criterion, and he also meets "
       "the admission criteria (marked symptoms despite acute management, still about 28 breaths a minute with "
       "accessory muscle use, and a need for noninvasive ventilatory support). Start noninvasive ventilation "
       "(bilevel positive airway pressure), which reduces intubation rates and mortality in hypercapnic "
       "respiratory failure; he is alert with no asterixis and hemodynamically stable. Repeat the blood gas, "
       "intubate only if he worsens, and give prophylaxis against venous clots."),
      "Smoking cessation now: counseling with nicotine replacement, bupropion or varenicline.",
      ("Before discharge: add a long-acting beta agonist to his tiotropium (group E after a hospitalized "
       "exacerbation), check his inhaler technique, refer to pulmonary rehabilitation, give the yearly influenza "
       "vaccine (pneumococcal at 65, or sooner if his lung function falls below 40% or heart disease develops), "
       "and arrange follow-up."),
    ],
    education=[
      ("This is a flare-up of your emphysema. The cold inflamed your already damaged airways, so they are narrower "
       "and full of mucus; your oxygen is low and carbon dioxide is building up. A breathing machine with a snug "
       "mask will help you blow it off and lowers the chance you need a breathing tube, so you'll stay in "
       "intensive care while you're on it."),
      ("Stopping smoking, and keeping the welding fumes away from your lungs, are the only things that slow the "
       "damage. We will help you quit with counseling and a patch, gum or a medicine."),
      ("You will go home on a daily inhaler with two long-acting medicines, plus albuterol for rescue, and we will "
       "check how you use them. Don't overuse the albuterol: it strains the heart."),
      ("Recovery can take 4 to 6 weeks, and you may not get all the way back to where you were. The breathing class "
       "(pulmonary rehabilitation) helps you breathe and move better and keeps you out of the hospital."),
      ("Get a flu shot every year. Call 911 for breathlessness at rest that your inhaler doesn't help, blue lips, "
       "confusion or sleepiness, or chest pain."),
    ],
    red_flags=["Drowsiness, confusion or asterixis (carbon dioxide climbing)",
               "A falling pH or rising carbon dioxide on the repeat gas despite noninvasive ventilation",
               "Hemodynamic instability or a new arrhythmia",
               "After discharge: breathlessness at rest despite the rescue inhaler, blue lips, chest pain or new leg "
               "swelling"],
    follow_up=("Intensive care now, stepping down to the ward once he is off the mask and stable; after discharge, "
               "follow-up with his lung specialist and pulmonary rehabilitation, including a talk about limiting his "
               "welding-fume exposure and returning to work; recovery can take 4 to 6 weeks."),
    presentation=(
      "Mr. Abernathy is a 61-year-old welder with severe chronic obstructive pulmonary disease, hypertension "
      "and about 44 pack-years, still smoking, presenting with four days of worsening breathlessness after a "
      "cold, now at rest. His sputum has increased and turned yellow-green, and albuterol every two hours no "
      "longer helps. He denies coughing up blood, chest pain, leg swelling and confusion. Heart rate 108, "
      "respiratory rate 28, temperature 99.8, room-air saturation 86%. He sits in the tripod position with "
      "pursed lips and accessory muscle use. He has a barrel chest, central cyanosis, diffuse hyperresonance, "
      "diminished fremitus, and distant breath sounds with wheezes and basal coarse crackles; he is alert, "
      "without asterixis or edema. My differential is an exacerbation, pneumonia, heart failure and pulmonary "
      "embolism. The blood gas shows acute-on-chronic respiratory acidosis, pH 7.32 with carbon dioxide 58, and "
      "an arterial oxygen of 52; the X-ray shows hyperinflation only. My working diagnosis is an exacerbation "
      "with hypercapnic respiratory failure. Plan: intensive care, noninvasive ventilation, controlled oxygen, "
      "albuterol, steroids and an antibiotic."),
    high_yield=[
      dict(item="Ask how the sputum has changed: amount and color",
           why=("More breathlessness with more sputum that has turned purulent is the indication for an "
                "antibiotic.")),
      dict(item="Count the pack-years and ask about work exposures",
           why="About 44 pack-years and still smoking, plus 39 years of welding fumes he still breathes at work."),
      dict(item="Ask about past flare-ups, hospital stays, breathing machines and home oxygen",
           why=("One flare this year treated at home; this admission makes him high risk (group E), which sets "
                "the inhalers he goes home on.")),
      dict(item="Inspect posture, pursed lips, accessory muscles, the anterior-posterior diameter and the lips",
           why=("Tripod position, pursed-lip breathing, accessory muscle use and cyanosis show how hard he is "
                "working (seen in more severe exacerbations or late-stage disease); the barrel chest above 0.9 is "
                "the chronic hyperinflation.")),
      dict(item="Percuss, palpate fremitus and listen side to side",
           why=("Diffuse hyperresonance, diminished fremitus and distant breath sounds with wheezes and coarse "
                "crackles fit hyperinflation; focal dullness with increased fremitus and bronchial breath sounds "
                "would mean pneumonia.")),
      dict(item="Check alertness and look for asterixis",
           why=("He is alert with no asterixis, so there is no altered mental status; drowsiness, confusion or a "
                "flapping tremor would mean the carbon dioxide is climbing despite the mask and he may need "
                "intubation.")),
      dict(item="Look at the neck veins and legs, and listen to the heart",
           why=("No leg edema and a normal natriuretic peptide argue against heart failure; distant heart sounds "
                "heard at the epigastrium are the hyperinflated chest.")),
      dict(item="Interpret the saturation and the blood gas out loud, then titrate oxygen",
           why=("Saturation 86% and arterial oxygen 52 mmHg need oxygen; pH 7.32 with carbon dioxide 58 and "
                "bicarbonate 29 is acute-on-chronic respiratory acidosis, which means intensive care and "
                "noninvasive ventilation, with oxygen titrated carefully by Venturi mask and a repeat "
                "gas.")),
    ],
  ),
),

# =====================================================================================================
# ACUTE BRONCHITIS (uncomplicated, viral, after a cold)
# =====================================================================================================
dict(
  id="pulmonary-acute-bronchitis",
  condition="Acute bronchitis",
  cites=("CMS L37 Respiratory Infections, slides 3-4, 9-11, 13, 15-22, 126; PD2 Thorax slides 14, 16, 18, 20-22, "
         "40, 42, 44-45, 47-48, 52-57"),
  door=dict(
    name="Colleen Brennan", sex="female", age=41, dob="March 14, 1985",
    setting="Outpatient primary care clinic",
    cc="\"I can't shake this cough.\"",
    vitals=[("Blood pressure", "118/76 mmHg"),
            ("Heart rate", "82 beats per minute, regular"),
            ("Respiratory rate", "16 breaths per minute"),
            ("Temperature", "99.0 °F (37.2 °C)"),
            ("Oxygen saturation", "98% on room air"),
            ("Height and weight", "5 feet 6 inches, 150 pounds (body mass index 24.2)")],
  ),
  persona=("A 41-year-old second-grade teacher, upbeat and talkative, a little hoarse, who coughs into a tissue now "
           "and then. She has already decided she needs antibiotics because her mucus is green, and she asks for "
           "them politely but firmly. She is a little embarrassed about smoking and quick to say she has cut down."),
  opening="I've had this cough for a week and a half. It started as a cold, and now I'm bringing up green stuff.",
  facts=[
    ("Full name", "Colleen Brennan."),
    ("Date of birth", "March 14, 1985."),
    # CMS L37 slide 16: starts with cold symptoms (low-grade fever, chills, aches, fatigue, postnasal drip)
    ("Onset", "About ten days ago, the Tuesday before last. It started as a cold: runny nose, scratchy throat, "
              "achy all over, and the cough came with it right from the start."),
    # slide 16: chest tightness or substernal discomfort; chest-wall pain from frequent coughing
    ("Location", "In my chest, right in the middle behind my breastbone. And my ribs are sore from all the "
                 "coughing."),
    ("Duration", "Ten days of cough now. I cough on and off all day, a few coughs at a time."),
    # slide 16: tickle in the back of the throat
    ("Character", "A deep, rattly, chesty cough. My chest feels tight, and a tickle in the back of my throat sets "
                  "it off."),
    ("Alleviating factors", "A hot shower in the morning loosens it up. The cold medicine takes the edge off for a "
                            "few hours."),
    ("Aggravating factors", "Talking all day to my class, cold air, and being near my husband when he smokes on the "
                            "porch. My own cigarettes too, honestly."),
    ("Radiation", "No, it doesn't go anywhere."),
    ("Severity", "Maybe a four out of ten. It's more annoying than painful. The sore ribs are about a three."),
    # slide 16: cough with mucus worst in the morning
    ("Temporal pattern", "Worst first thing in the morning. The cold part is getting better, but the cough isn't."),
    ("Prior episodes", "I get a chest cold every other winter or so. Two years ago the urgent care gave me a Z-Pak, "
                       "and it went away."),
    ("Cough", "Yes, for ten days. It was dry at first, and now it's wet."),
    # slide 16: mucus can be green or yellow but does not tell viral from bacterial
    ("Sputum", "Yellow, sometimes green, mostly in the morning. About a teaspoon at a time. It doesn't smell."),
    ("Coughing up blood", "No, never any blood."),
    ("Shortness of breath", "Not really. My chest feels a little tight after I've coughed a lot, but I can do my "
                            "whole day."),
    ("How far they can walk", "As far as I want. I walk the dog a mile every evening, just a bit slower this week."),
    # slide 16: shortness of breath with possible wheezing
    ("Wheezing", "Sometimes a little whistle in my chest at night when I lie down, and after I've coughed a lot."),
    ("Chest pain with breathing", "No pain when I breathe in. Just the sore ribs from coughing."),
    ("Fever, chills or night sweats", "A low fever the first couple of days, 99.8, maybe 100.2 once, with chills and "
                                      "aches. Nothing for a week now. No night sweats."),
    ("Weight loss", "No, my weight's the same."),
    ("Orthopnea and waking up short of breath", "I sleep on one pillow. The cough wakes me sometimes, but I don't "
                                                "wake up short of breath."),
    ("Leg swelling or calf pain", "No."),
    ("Recent travel, immobility or surgery", "No trips, no surgery. I'm on my feet all day in the classroom."),
    ("Sick contacts", "Half my second graders have had runny noses, and my son had a cold right before I got this "
                      "one."),
    ("Constitutional", "Tired from not sleeping well. The aches went away after the first few days. No sweats, no "
                       "weight loss."),
    ("Heart symptoms", "No chest pressure, no racing heart, no swelling."),
    # slide 16: postnasal drip; localized viral signs
    ("Ear, nose and throat", "Still a little stuffy, with a drip down the back of my throat. The sore throat is "
                             "better. No ear pain."),
    ("Heartburn or reflux", "No heartburn, no sour taste."),
    ("Anything else", "No, I just want this cough gone."),
    ("Chronic conditions", "An underactive thyroid. That's it."),
    ("Known lung disease", "No asthma, never used an inhaler. No emphysema or anything like that."),
    ("Surgeries and procedures", "A cesarean section with my son nine years ago."),
    ("Hospitalizations", "Just for having my son."),
    ("Prescription medications", "Levothyroxine, 75 micrograms every morning, for about six years."),
    ("Taking them as prescribed", "Every morning, before my coffee."),
    # slide 19: review combination-product ingredients to prevent duplicate acetaminophen
    ("Over-the-counter medicines and supplements", "DayQuil during the day and NyQuil at night, and Tylenol on top "
                                                   "when my ribs hurt, two or three times a day. And cough drops."),
    ("Allergies", "No drug allergies."),
    ("Tobacco", "About half a pack a day since I was twenty-two. I've cut back to a few a day this week because it "
                "makes me cough."),
    ("Vaping and marijuana", "No vaping, no marijuana."),
    ("Alcohol", "A glass of wine on Friday nights."),
    ("Recreational drugs", "No."),
    ("Occupation and exposures", "I teach second grade. No dust or chemicals, just a lot of germs."),
    ("Home and environment", "A house in town. No mold that I know of. My husband smokes, but only out on the "
                             "porch. We have a dog, no birds."),
    ("Living situation", "My husband, Dan, and our son, Owen. He's nine."),
    # slide 13: Tdap during every pregnancy, then Td or Tdap every 10 years; slides 4, 11: influenza and COVID-19
    ("Immunizations", "I had the tetanus and whooping cough shot when I was pregnant with Owen. I usually get my "
                      "flu shot at school, but I missed the clinic day this year. I had the COVID shots when they "
                      "first came out. I've never had a pneumonia shot."),
    ("Tuberculosis exposure or testing", "They did a skin test when I started teaching. It was negative. Nobody I "
                                         "know has had tuberculosis."),
    ("Family history, mother", "My mom is 68. High blood pressure and an underactive thyroid like me."),
    ("Family history, father", "My dad is 72. He had a heart attack at 66 and pneumonia a few years ago. He smoked "
                               "for years too."),
    ("Family history, siblings", "One sister, 38, healthy."),
    ("What they think it is", "Bronchitis. It's always bronchitis with me, and it always needs antibiotics."),
    ("Concerns", "That it turns into pneumonia like my dad's did. And I can't keep missing school."),
    # slides 17-18: pertussis with paroxysmal cough, post-tussive vomiting, whoop or exposure
    ("Coughing fits, whooping or vomiting after coughing", "No, it's not like that. I don't get coughing fits where "
                                                           "I can't catch my breath, no whooping sound, and I've "
                                                           "never thrown up from it. No notes home about whooping "
                                                           "cough at school."),
    ("Sore ribs", "Along both sides of my breastbone. It hurts to press there, and when I cough."),
    ("Sleep", "The cough wakes me a couple of times a night. The NyQuil helps me sleep."),
    ("Antibiotics", "Honestly, I was hoping you'd give me a Z-Pak. The green stuff means infection, right?"),
    # slide 20: avoid routine opioid cough suppressants
    ("Codeine cough syrup", "My husband had a cough syrup with codeine last winter that worked great for him. He "
                            "still has some."),
  ],
  questions=["Can I get an antibiotic? It's green now.",
             "Could I take the codeine cough syrup my husband has?",
             "How long is this cough going to last?"],
  exam={
    "position": "She sits on the edge of the exam table with the gown open at the back, a tissue in her hand.",
    "general-survey": ("Alert and comfortable, in no respiratory distress. Speaks in full sentences, interrupted now "
                       "and then by a loose cough. No audible wheeze or stridor. Normal color."),
    "breathing-pattern": ("Quiet, regular and unlabored at about 16 breaths a minute, with a normal expiratory "
                          "phase."),
    # CMS L37 slide 16: palpable pain on the chest wall or costochondral areas from frequent coughing
    "chest-wall-palp": ("Mild tenderness over the costochondral junctions on both sides of the sternum, which she "
                        "says is the soreness she feels when she coughs. No deformity, masses or crepitus. The "
                        "posterior and lateral chest wall are not tender."),
    # slide 16: subtle rhonchi from mucus; PD2 slide 48: rhonchi are low-pitched
    "ausc-posterior": ("Posterior chest: vesicular breath sounds, equal on both sides, with a few low-pitched "
                       "rhonchi between the scapulae over the large airways. No crackles, no bronchial breath "
                       "sounds, no pleural rub."),
    # slide 16: wheezing more central (substernal) over the bronchial airways
    "ausc-anterior": ("Anterior chest: vesicular breath sounds over both upper lobes, bronchovesicular near the "
                      "sternum, with scattered low-pitched rhonchi and a faint expiratory wheeze over the sternum "
                      "(the central airways). No crackles and no pleural rub."),
  },
  special=[
    # CMS L37 slide 16: pharyngeal injection or other localized viral signs (rhinorrhea); postnasal drip
    ("throat-nose", "Throat and nose inspection",
     "looks at the back of the throat and inside the nose with a light",
     "Mild redness of the back of the throat (pharyngeal injection) and a little clear drainage down the back of "
     "the throat and in the nose."),
    # slide 16: rhonchi will clear with cough; PD2 slide 48: rhonchi may disappear with coughing
    ("cough-relisten", "Listening again after a cough",
     "asks the patient to cough hard a few times, then listens again over the same areas",
     "The rhonchi are gone after she coughs. A faint expiratory wheeze over the sternum remains; still no "
     "crackles."),
  ],
  must_exam=['ausc-posterior', 'ausc-anterior', 'percuss-posterior', 'fremitus', 'egophony', 'cough-relisten'],
  tests=[
    # CMS L37 slide 15: routine chest radiography unnecessary in uncomplicated cases
    dict(id="cxr", name="Chest X-ray",
         aka=["CXR", "chest film", "chest radiograph", "chest x ray", "chest x-ray", "chest imaging"],
         result=("Clear lungs with no infiltrate or consolidation, and sharp costophrenic angles. Heart size "
                 "normal."),
         here=True),
    # slide 17: test for influenza or COVID-19 when the result will guide treatment or infection prevention
    dict(id="flu-covid", name="Influenza and COVID-19 rapid molecular test",
         aka=["flu test", "flu swab", "influenza test", "COVID test", "COVID swab", "flu/COVID", "rapid flu",
              "respiratory viral panel", "viral PCR", "SARS-CoV-2 PCR", "multiplex"],
         result="Negative for influenza A, influenza B and SARS-CoV-2.", here=True),
    # slide 15: a complete blood count cannot reliably distinguish viral from bacterial bronchitis
    dict(id="cbc", name="Complete blood count (CBC) with differential",
         aka=["CBC", "complete blood count", "blood count", "white count", "differential", "CBC with diff"],
         result="White blood cell count, differential, hemoglobin and platelets all normal.", here=True),
    # slide 15: routine sputum culture unnecessary in uncomplicated cases
    dict(id="sputum-culture", name="Sputum culture",
         aka=["sputum culture", "sputum gram stain", "gram stain", "sputum sample", "phlegm culture"],
         result="Normal respiratory flora; no single organism predominates.", here=True),
    # slides 17-18: targeted pertussis testing when suspected
    dict(id="pertussis-pcr", name="Pertussis polymerase chain reaction (PCR) swab",
         aka=["pertussis", "pertussis PCR", "pertussis swab", "whooping cough test", "Bordetella",
              "Bordetella PCR", "nasopharyngeal swab for pertussis"],
         result="Negative for Bordetella pertussis.", here=True),
    # Not on the cited slides: a normal office peak flow (incidental, normal)
    dict(id="peak-flow", name="Peak expiratory flow",
         aka=["peak flow", "PEF", "PEFR", "peak expiratory flow rate", "peak flow meter"],
         result="Best of three blows: 430 liters per minute, about 95% of predicted for her age, sex and height.",
         here=True),
    # Not on the cited slides (slide 20 only says to reassess for asthma or chronic obstructive pulmonary disease):
    # a normal result
    dict(id="spirometry", name="Spirometry",
         aka=["spirometry", "PFTs", "pulmonary function tests", "lung function test", "FEV1", "FEV1/FVC"],
         result=("Normal: the ratio of forced expiratory volume in 1 second to forced vital capacity is normal, with "
                 "no airflow obstruction."),
         here=True),
    dict(id="ct-chest", name="Chest computed tomography (CT)",
         aka=["CT", "CT chest", "chest CT", "CAT scan", "computed tomography"],
         result="Clear lungs with no consolidation, nodule or effusion.", here=True),
  ],
  key=dict(
    diagnosis=("Acute bronchitis, uncomplicated and most likely viral, after a cold: normal vital signs and "
               "oxygen, no focal lung findings; supportive care without antibiotics"),
    must_not_miss=["Pneumonia: abnormal vital signs, low oxygen or focal consolidation (dullness, increased "
                   "fremitus, bronchial breath sounds, egophony) calls for a chest X-ray",
                   "Pertussis: coughing fits, a whoop, vomiting after coughing or an exposure needs targeted "
                   "testing and treatment to protect her students and family"],
    ddx=[
      dict(name="Acute bronchitis (uncomplicated, viral)",
           support=("A cough that began with a cold caught from her son and her class, now ten days of "
                    "yellow-green mucus worst in the morning, chest tightness, a throat tickle and an occasional "
                    "wheeze; low-grade fever only at the start; normal vital signs and 98% saturation; throat "
                    "redness, costochondral tenderness, central rhonchi that clear with a cough and a faint central "
                    "wheeze, with resonant percussion, normal fremitus and no egophony."),
           against=("Nothing against it. Colored mucus does not mean a bacterial infection; the diagnosis is "
                    "clinical once pneumonia, pertussis, asthma, influenza and COVID-19 have been considered.")),
      dict(name="Community-acquired pneumonia",
           support="A productive cough with colored mucus, chest discomfort and a low-grade fever at the start.",
           against=("No fever for a week, normal heart and breathing rates, 98% saturation and no consolidation: "
                    "percussion resonant, fremitus normal, no bronchial breath sounds, crackles or egophony.")),
      dict(name="Pertussis",
           support="Ten days of cough in a teacher of young children.",
           against=("No coughing fits, whoop or vomiting after coughing and no known exposure; the cough began "
                    "with an ordinary cold, and she had the tetanus, diphtheria and pertussis vaccine in "
                    "pregnancy.")),
      dict(name="Asthma",
           support="Wheeze and chest tightness, worse lying down at night.",
           against=("No asthma diagnosis and never an inhaler; her earlier winter chest colds cleared without any "
                    "wheeze treatment; this wheeze is central and came with the infection. Reassess for asthma only "
                    "if it persists after the illness.")),
    ],
    studies=[
      dict(test="Chest X-ray",
           why=("Only when vital signs, focal lung findings or clinical risk raise concern for pneumonia; routine "
                "films are unnecessary in uncomplicated bronchitis, and she has none of those."),
           expect="Not needed; if taken, clear lungs with no infiltrate."),
      dict(test="Complete blood count",
           why="Not routinely needed: it cannot reliably tell viral from bacterial bronchitis.",
           expect="Not needed; if done, normal."),
      dict(test="Influenza and COVID-19 molecular test",
           why="Only when the result will guide treatment or infection prevention.",
           expect="Negative for influenza and COVID-19."),
      dict(test="Pertussis testing",
           why=("Targeted testing only with coughing fits, a whoop, vomiting after coughing or a known exposure; "
                "she has none, so it is not needed now."),
           expect="Not needed; if done, negative."),
    ],
    plan=[
      ("Clinical diagnosis of uncomplicated acute bronchitis: normal vital signs and oxygen and no focal findings, "
       "so no routine chest X-ray, blood count or sputum culture."),
      ("No antibiotic, including the azithromycin she asks for, regardless of sputum color or cough duration: "
       "call it a chest cold, set the expected course of two to three weeks, and explain that antibiotics do not "
       "shorten it and bring side effects, Clostridioides difficile infection and resistance."),
      ("Supportive care: rest, fluids and avoiding smoke; acetaminophen for discomfort, with a check of her "
       "combination cold products so it is not doubled; no codeine cough syrup and no corticosteroids; pelargonium "
       "may ease the cough."),
      ("A short trial of a bronchodilator inhaler if the wheeze bothers her; reconsider asthma or chronic "
       "obstructive pulmonary disease if the wheeze or cough persists."),
      "Smoking cessation: advise her to quit and offer support; keep away from her husband's smoke.",
      ("Vaccines: one dose of 20- or 21-valent pneumococcal conjugate vaccine (cigarette smoking is a risk "
       "condition at 19 to 49), the annual influenza vaccine and the updated COVID-19 vaccine."),
    ],
    education=[
      ("This is a chest cold: a virus irritating the big airways in your chest. Green or yellow mucus does not "
       "mean bacteria."),
      ("An antibiotic will not make it go away faster, and it can cause side effects, a serious bowel infection "
       "and resistance. The cough usually lasts two to three weeks, sometimes longer."),
      ("Rest, drink fluids and stay away from smoke. Your DayQuil and NyQuil already contain acetaminophen, the "
       "same medicine as Tylenol, so do not take Tylenol on top of them."),
      ("Codeine cough syrup barely helps and can make you drowsy and slow your breathing, so please don't take "
       "your husband's. This is a good time to quit smoking, and we can help."),
      ("Come back if you get short of breath, cough up blood, have a fever that won't go away, or start to get "
       "better and then get worse."),
    ],
    red_flags=["Shortness of breath or a low oxygen level", "Coughing up blood", "Fever that persists",
               "Getting better, then worse"],
    follow_up=("Routine: no visit needed if she improves as expected; return if the cough lasts beyond about three "
               "weeks or worsens (reconsider the diagnosis, including asthma), and at once for any red flag."),
    presentation=(
      "Ms. Brennan is a 41-year-old second-grade teacher who smokes, about 10 pack-years, presenting with ten "
      "days of cough that began with a cold: runny nose, sore throat, aches and a low-grade fever for two days. "
      "The cough now brings up yellow-green mucus, worst in the morning, with chest tightness, an occasional "
      "wheeze and sore ribs. She denies breathlessness at rest, coughing up blood, coughing fits, whooping, "
      "vomiting after coughing, night sweats and leg swelling. She takes day and night cold products plus extra "
      "acetaminophen. Temperature 99.0, heart rate 82, respiratory rate 16, saturation 98% on room air. "
      "Examination shows throat redness, costochondral tenderness, central rhonchi that clear with coughing and a "
      "faint central wheeze; percussion is resonant, fremitus normal, no egophony. My differential is acute "
      "bronchitis, pneumonia, pertussis and asthma. No routine X-ray, blood count or culture. My working diagnosis "
      "is acute bronchitis. Plan: supportive care without antibiotics, stop the doubled acetaminophen, smoking "
      "cessation and vaccines."),
    high_yield=[
      dict(item="Ask how the illness started and how long the cough has lasted",
           why=("A cold first, then a cough under 3 weeks: an acute cough. Bronchitis cough commonly lasts 2 to 3 "
                "weeks, so ten days is expected.")),
      dict(item="Ask the color of the sputum, and say what it does not mean",
           why="Yellow-green mucus does not tell viral from bacterial and does not justify an antibiotic."),
      dict(item="Screen for pertussis: coughing fits, a whoop, vomiting after coughing, exposures",
           why="Suspected pertussis needs targeted testing and treatment, without waiting for 4 weeks of cough."),
      dict(item="Interpret the vital signs and saturation as a pneumonia screen",
           why=("Normal rates, no fever for a week and 98% saturation argue against pneumonia; abnormal ones "
                "would call for a chest X-ray.")),
      dict(item="Percuss, check fremitus and listen for bronchial breath sounds and egophony over every lobe",
           why="No consolidation should be found in bronchitis; finding it means pneumonia."),
      dict(item="Have her cough, then listen again",
           why=("Rhonchi from mucus clear with a cough, and the wheeze is central over the large airways: both fit "
                "bronchitis.")),
      dict(item="Ask about every over-the-counter product",
           why=("Her combination cold products contain acetaminophen, so the extra Tylenol doubles the dose; "
                "codeine cough syrup is not recommended.")),
      dict(item="Address smoking",
           why=("Avoiding smoke eases the illness, and cigarette smoking makes her eligible for a pneumococcal "
                "conjugate vaccine at 41.")),
    ],
  ),
),

# =====================================================================================================
# PULMONARY EMBOLISM (provoked, right main pulmonary artery, submassive, emergency department)
# =====================================================================================================
dict(
  id="pulmonary-pulmonary-embolism",
  condition="Pulmonary embolism",
  cites=("CMS L42 Pulmonary Vascular Disorders, slides 9, 14, 43, 48-62; CMS L26 Venous Disorders slides 47, "
         "51, 57, 61, 63-65, 68; CMS L44 Pleural Disorders slides 12-13, 25; CMS L33 Oxygen Delivery slide 3; "
         "PD2 Thorax slides 10, 14, 17, 24, 35, 40, 50, 61"),
  door=dict(
    name="Daniela Castillo", sex="female", age=34, dob="January 30, 1992",
    setting="Emergency department",
    cc="\"It hurts to breathe and I can't get enough air.\"",
    # CMS L42 slides 43, 58: tachycardia, hypoxemia; normotensive (systolic above 90)
    vitals=[("Blood pressure", "128/78 mmHg"),
            ("Heart rate", "110 beats per minute, regular"),
            ("Respiratory rate", "22 breaths per minute"),
            ("Temperature", "99.0 °F (37.2 °C)"),
            ("Oxygen saturation", "93% on room air"),
            ("Height and weight", "5 feet 5 inches, 164 pounds (body mass index 27.3)")],
  ),
  persona=("A 34-year-old middle school Spanish teacher, organized and articulate, frightened but trying to stay "
           "composed. She takes small breaths, pauses between sentences when the pain catches, and keeps one hand "
           "pressed to her right side. She plays down her sore calf until asked, because she was sure it was a "
           "pulled muscle. Her six-year-old son is her first worry."),
  opening=("This morning I got a sharp pain on the right side of my chest every time I breathe in, and I can't "
           "get enough air."),
  facts=[
    ("Full name", "Daniela Castillo."),
    ("Date of birth", "January 30, 1992."),
    # CMS L42 slide 50: sudden onset over minutes to hours
    ("Onset", "This morning, about six hours ago. I was getting my son ready for school, and all of a sudden I "
              "got a sharp pain on the right side when I breathed in, and I couldn't catch my breath."),
    ("Location", "The right side, low, under my breast and around toward my side. (She points to the right "
                 "lower ribs at the side.)"),
    ("Duration", "Since this morning, the whole time. It stabs every time I breathe in."),
    ("Character", "Sharp, like a knife, every time I take a breath in. And like I can't get enough air."),
    ("Alleviating factors", "Taking small breaths and holding still. Nothing else helps."),
    ("Aggravating factors", "Deep breaths, coughing and walking. The stairs this morning were awful."),
    ("Radiation", "No, it stays on the right side."),
    ("Severity", "A seven. A ten was labor with my son, before the epidural."),
    ("Temporal pattern", "The same since it started, maybe a little worse. Position and time of day don't "
                         "change it."),
    ("Prior episodes", "Never."),
    ("Cough", "A little cough since this morning."),
    ("Sputum", "Just a little, mostly clear."),
    # CMS L42 slide 50 and PD2 Thorax slides 17, 24: hemoptysis
    ("Coughing up blood", "Twice this morning there were streaks of bright red blood in what I coughed up. That "
                          "scared me."),
    ("Shortness of breath", "Yes, since this morning. Even sitting here I feel like I can't get enough air, and "
                            "walking makes it worse."),
    ("How far they can walk", "I usually walk three miles with a friend. This morning I had to stop halfway up "
                              "our stairs, and the walk in from the parking lot winded me."),
    ("Wheezing", "No."),
    ("Chest pain with breathing", "Yes, it stabs every time I breathe in."),
    ("Fever, chills or night sweats", "No fever that I know of. No chills or sweats."),
    ("Weight loss", "No."),
    ("Orthopnea and waking up short of breath", "No. Lying down doesn't make the breathing worse, and I haven't "
                                                "woken up short of breath."),
    # PD2 Thorax slide 17: unilateral leg symptoms; CMS L26 slide 51: swelling, pain, warmth, a persisting cramp
    ("Leg swelling or calf pain", "Actually, yes. My left calf has been sore and tight for about five days, and "
                                  "my left ankle is a little puffy. I thought I pulled a muscle walking so much "
                                  "on vacation. The right leg is fine."),
    # CMS L42 slide 49: prolonged immobilization (flights over 8 hours)
    ("Recent travel, immobility or surgery", "I flew back from visiting family in Santiago, Chile, nine days ago. "
                                             "Ten hours overnight in a window seat; I slept most of the way and "
                                             "barely got up. No surgery, no injuries."),
    ("Sick contacts", "My nephew in Chile had a cold, but that was three weeks ago. Nobody at home is sick."),
    ("Constitutional", "Tired from the trip, but fine until this morning. No fevers, no sweats, no weight loss."),
    ("Heart symptoms", "My heart's been racing since this morning. No chest pressure, no fainting."),
    ("Ear, nose and throat", "No sore throat, no stuffy nose."),
    ("Heartburn or reflux", "No."),
    ("Anything else", "No, that's everything."),
    ("Chronic conditions", "None. I'm healthy."),
    ("Known lung disease", "No asthma, nothing."),
    ("Surgeries and procedures", "Just my wisdom teeth when I was nineteen."),
    ("Hospitalizations", "Only when I had my son, six years ago. A normal delivery."),
    # CMS L42 slide 49: estrogen therapy
    ("Prescription medications", "Just my birth control pill, Sprintec, one every night. I started it about four "
                                 "months ago."),
    ("Taking them as prescribed", "Every night. I don't miss it."),
    ("Over-the-counter medicines and supplements", "Ibuprofen a couple of times for my calf, and a vitamin D pill. "
                                                   "No herbal products."),
    # CMS L42 slide 55: a severe contrast allergy points to a ventilation-perfusion scan instead
    ("Allergies", "No allergies to any medicine. I've never had the dye they use for scans."),
    ("Tobacco", "I've never smoked."),
    ("Vaping and marijuana", "No."),
    ("Alcohol", "A glass of wine on the weekend."),
    ("Recreational drugs", "No."),
    ("Occupation and exposures", "I teach Spanish at a middle school. No dust or chemicals."),
    ("Home and environment", "A house. No mold. We have a dog."),
    ("Living situation", "My husband, Marco, and our six-year-old, Mateo. Marco drove me here; he's in the "
                         "waiting room."),
    ("Immunizations", "Up to date. I had my flu shot in October."),
    ("Tuberculosis exposure or testing", "Never around it that I know of. The school did a skin test when I was "
                                         "hired three years ago, and it was negative."),
    ("Family history, mother", "My mom has high blood pressure. She's never had a blood clot."),
    ("Family history, father", "My dad has type 2 diabetes."),
    ("Family history, siblings", "One brother, thirty, healthy."),
    ("What they think it is", "I thought I pulled a muscle in my leg, and maybe now in my chest. Marco looked it "
                              "up and thinks it could be a blood clot."),
    ("Concerns", "Is it a clot in my lung? Am I going to be okay? I have a six-year-old."),
    # CMS L42 slide 49: estrogen therapy, pregnancy
    ("Birth control", "It's a combination pill. The doctor said it has estrogen in it."),
    ("Last period and pregnancy", "My period ended about two weeks ago, normal. I don't think I'm pregnant."),
    # CMS L42 slides 53-54: previous clot; CMS L42 slide 49: genetic thrombophilias
    ("Prior blood clots", "Never."),
    ("Blood clots or bleeding problems in the family", "Nobody in my family has had a blood clot that I know of, "
                                                       "and no bleeding problems."),
    # CMS L26 slide 62: contraindications to anticoagulation (active bleeding, bleeding disorders)
    ("Bleeding problems", "No. I don't bruise easily, my periods aren't heavy, and I've never had an ulcer or "
                          "bleeding from my stomach."),
    # CMS L42 slides 49, 53: malignancy
    ("Cancer history", "No cancer. My Pap smears have always been normal."),
    # CMS L42 slide 50: syncope marks circulatory collapse
    ("Fainting or lightheadedness", "No, I haven't fainted or felt like I would."),
  ],
  questions=["Is this a blood clot in my lung?",
             "Will I have to be on blood thinners forever?",
             "Can I keep taking my birth control pill?"],
  # CMS L42 slide 50: pleuritic pain and hemoptysis mean a distal, pleural-based infarction, often with a
  # localized friction rub; PD2 Thorax slide 50: the rub is best heard in the axilla and lower bases, louder
  # with firm pressure, not affected by coughing, gone on breath-holding; CMS L26 slide 51: calf swelling, pain,
  # warmth
  exam={
    "position": ("She sits upright on the stretcher with the gown open at the back, holding her right side when "
                 "she breathes in."),
    "general-survey": ("Alert, oriented and anxious, mildly short of breath at rest but speaking in full "
                       "sentences; she stops short of a deep breath because of pain. No audible wheeze or "
                       "stridor. Normal color, no sweating."),
    "breathing-pattern": ("Fast at 22 breaths per minute, regular and shallow, with a normal expiratory phase; "
                          "she splints, taking small breaths because a deep one hurts on the right."),
    "thorax-inspect": ("No deformity, wound or bruising. The right lower chest moves a little less than the left "
                       "because she splints against the pain. No retractions."),
    "expansion": ("Decreased on the right: the right thumb moves less than the left with a deep breath, because a "
                  "deep breath hurts on that side."),
    "chest-wall-palp": ("No tenderness, deformity or crepitus over the posterior, lateral or anterior chest wall. "
                        "Pressing over the right lower ribs where she points does not reproduce the pain."),
    "ausc-lateral": ("Lateral chest: vesicular breath sounds, equal on both sides. Over the right lower lateral "
                     "chest, a localized, low-pitched grating, creaking sound in both inspiration and expiration "
                     "(a pleural friction rub), louder with firm stethoscope pressure and unchanged after a "
                     "cough. No crackles or wheezes."),
    "ausc-posterior": ("Posterior chest: vesicular breath sounds, equal on both sides; the rub is faintly heard "
                       "at the right base. No crackles, wheezes or rhonchi."),
    "heart-ausc": ("Regular rhythm, fast at about 110. Normal first and second heart sounds, with no murmur, "
                   "extra heart sound or pericardial rub."),
    "legs": ("The left calf is swollen, warm and tender along the back, about 3 centimeters larger around than "
             "the right at the same level, with 1+ pitting edema at the left ankle. No redness tracking along a "
             "vein. The right leg is normal."),
  },
  special=[
    # PD2 Thorax slide 50 and CMS L44 slide 12: a pleural rub disappears when the patient holds the breath
    ("rub-breath-hold", "Breath-hold test over the rub",
     "listens over the rub at the right lower lateral chest while the patient holds her breath for a few seconds",
     "The grating sound stops while she holds her breath and returns when she breathes again; the heart sounds go "
     "on unchanged. It is a pleural friction rub, not a pericardial rub."),
  ],
  must_exam=["legs", "ausc-lateral", "rub-breath-hold", "heart-ausc", "breathing-pattern"],
  tests=[
    # CMS L42 slides 55, 57: computed tomographic pulmonary angiography is first-line, the gold standard;
    # slide 58: right ventricular dysfunction on the scan defines submassive; slide 50: pleural-based infarction
    dict(id="ctpa", name="Computed tomographic pulmonary angiography (CTPA)",
         aka=["CTPA", "CT angiogram", "CT angio", "CTA chest", "PE protocol CT", "CT PE study", "CT chest with contrast",
              "computed tomographic pulmonary angiography", "CT"],
         result=("A large filling defect in the right main pulmonary artery, extending into the right lower lobe "
                 "arteries, with a small wedge-shaped, pleural-based opacity at the right base (an infarction). "
                 "The right ventricle is larger than the left, with the septum bowing toward the left ventricle. "
                 "No pneumonia, pneumothorax or effusion."),
         here=True),
    # CMS L42 slides 54, 57: positive D-dimer means imaging; bypassed when the Wells score is above 4
    dict(id="d-dimer", name="D-dimer",
         aka=["D-dimer", "d dimer", "dimer", "clot test"],
         result="Elevated: 2,400 nanograms per milliliter (normal below 500).",
         here=True),
    # CMS L42 slides 14, 51: abnormal in 70% of acute embolism; the S1Q3T3 pattern suggests severe right
    # ventricular strain (highly specific, low sensitivity)
    dict(id="ecg", name="Electrocardiogram (12-lead)",
         aka=["EKG", "ECG", "12-lead", "12 lead", "electrocardiogram", "heart tracing"],
         result=("Sinus tachycardia at 110 with the S1Q3T3 pattern: a deep S wave in lead I, and a Q wave and an "
                 "inverted T wave in lead III. No ST elevation."),
         here=True),
    # CMS L42 slide 51: most have an abnormal but nonspecific film (atelectasis, effusion); classic signs infrequent
    dict(id="cxr", name="Chest X-ray",
         aka=["CXR", "chest film", "chest radiograph", "chest x ray", "chest x-ray", "chest imaging", "portable chest"],
         result=("Mild atelectasis at the right base. Otherwise clear: no pneumothorax, consolidation, effusion "
                 "or wedge-shaped opacity; heart size and pulmonary vessels normal."),
         here=True),
    # CMS L42 slide 58: elevated troponin (myocardial necrosis) is a submassive criterion
    dict(id="troponin", name="Troponin (high-sensitivity)",
         aka=["troponin", "trop", "cardiac enzymes", "cardiac markers", "high-sensitivity troponin", "hs-troponin"],
         result="Elevated: mildly above the upper reference limit on arrival, and higher on the repeat 2 hours later.",
         here=True),
    # CMS L42 slide 43: B-type natriuretic peptide normal initially in embolism
    dict(id="bnp", name="B-type natriuretic peptide (BNP)",
         aka=["BNP", "B-type natriuretic peptide", "brain natriuretic peptide", "natriuretic peptide", "NT-proBNP"],
         result="Normal: 38 picograms per milliliter.",
         here=True),
    # CMS L42 slides 14, 56, 62: the echocardiogram is for risk stratification (right ventricular strain, the
    # D-shaped septum), not diagnosis; slide 60: a clot in transit in the right heart changes treatment
    dict(id="echo", name="Echocardiogram (transthoracic)",
         aka=["echo", "echocardiogram", "TTE", "transthoracic echo", "heart ultrasound", "cardiac ultrasound",
              "bedside echo"],
         result=("Dilated right ventricle with reduced function and a flattened, D-shaped septum (right "
                 "ventricular strain); the left ventricle is small but squeezes normally. Pulmonary artery "
                 "systolic pressure estimated as raised. No clot in the right heart."),
         here=True),
    # CMS L26 slide 57: venous duplex ultrasound has replaced venography; slide 47: begins in the calf and moves
    # proximally to the popliteal and femoral veins
    dict(id="leg-ultrasound", name="Venous duplex ultrasound of the legs",
         aka=["leg ultrasound", "venous duplex", "duplex", "duplex ultrasound", "lower extremity doppler", "doppler",
              "DVT scan", "DVT ultrasound", "venous ultrasound", "compression ultrasound", "leg doppler"],
         result=("Left leg: the femoral and popliteal veins do not compress and contain thrombus: acute deep vein "
                 "thrombosis. Right leg veins compress normally."),
         here=True),
  ],
  key=dict(
    diagnosis=("Acute submassive (intermediate-risk) pulmonary embolism: a clot in the right main pulmonary artery "
               "extending into the right lower lobe, with right ventricular strain and a raised troponin but a "
               "normal blood pressure; from a left femoral and popliteal deep vein thrombosis, provoked by an "
               "estrogen pill and a long flight"),
    must_not_miss=["Deterioration to massive (high-risk) embolism: fainting, a systolic pressure under 90 for more "
                   "than 15 minutes or circulatory collapse needs immediate thrombolysis, or thrombectomy if "
                   "thrombolysis is contraindicated",
                   "Calling it low risk because the blood pressure is normal: right ventricular strain on the scan "
                   "and echocardiogram and a raised troponin make it submassive, at high risk of sudden "
                   "deterioration"],
    ddx=[
      dict(name="Pulmonary embolism (acute, submassive, right main pulmonary artery) from a left leg deep vein thrombosis",
           support=("Sudden pleuritic right-sided pain with breathlessness and blood-streaked sputum, five days of "
                    "left calf pain and ankle swelling, an estrogen pill and a ten-hour flight nine days ago. "
                    "Heart rate 110, saturation 93%, splinting on the right, a localized right lower pleural rub "
                    "that stops on breath-holding, and a swollen, warm, tender left calf. Wells score 8.5. The "
                    "electrocardiogram shows the S1Q3T3 pattern, the scan a clot in the right main pulmonary "
                    "artery with a strained right ventricle, and the ultrasound a left femoral and popliteal "
                    "clot."),
           against=("Nothing against it; a nonspecific chest X-ray (mild atelectasis only) and a normal "
                    "natriuretic peptide are typical early in embolism.")),
      dict(name="Pneumonia",
           support="Pleuritic pain, a cough, a temperature of 99.0 and blood-streaked sputum.",
           against=("Onset over minutes, no fever or purulent sputum, no crackles, bronchial breath sounds or "
                    "egophony, and no consolidation on the chest X-ray.")),
      dict(name="Pneumothorax",
           support="Sudden pleuritic pain and breathlessness.",
           against=("Resonant percussion, preserved fremitus and equal breath sounds, and no pleural line on the "
                    "X-ray.")),
      dict(name="Pericarditis",
           support="Sharp chest pain that is worse on inspiration, with a fast heart rate.",
           against=("Not positional and not eased by sitting forward; the rub stops when she holds her breath, so "
                    "it is pleural, not pericardial; no ST elevation.")),
    ],
    studies=[
      dict(test="Computed tomographic pulmonary angiography",
           why=("Wells score above 4 (8.5): skip the D-dimer and go straight to imaging. First-line and the gold "
                "standard, and it shows the right ventricle; a ventilation-perfusion scan is for kidney failure "
                "or a severe contrast allergy."),
           expect=("A filling defect in the right main pulmonary artery extending into the right lower lobe, a "
                   "small pleural-based infarction, and a right ventricle larger than the left with septal "
                   "bowing.")),
      dict(test="Electrocardiogram",
           why=("Abnormal in about 70% of acute embolism; the S1Q3T3 pattern suggests severe right ventricular "
                "strain (highly specific, low sensitivity). It also looks for a heart attack."),
           expect="Sinus tachycardia at 110 with the S1Q3T3 pattern; no ST elevation."),
      dict(test="Chest X-ray",
           why=("Most patients with embolism have an abnormal but nonspecific film (atelectasis, effusion), and "
                "the classic signs (focal oligemia, a wedge-shaped opacity, an enlarged descending pulmonary "
                "artery) are infrequent; it rules out pneumothorax and pneumonia."),
           expect="Mild atelectasis at the right base only; no pneumothorax, consolidation or effusion."),
      dict(test="Troponin and B-type natriuretic peptide",
           why=("Risk stratification: a raised troponin or natriuretic peptide in a patient with a normal blood "
                "pressure makes it submassive."),
           expect="Troponin elevated and rising; natriuretic peptide still normal this early."),
      dict(test="Echocardiogram",
           why=("Poor for diagnosing embolism but highly specific for right ventricular strain: a tool for risk "
                "stratification. It looks for the D-shaped septum and a clot in the right heart."),
           expect="Dilated, poorly moving right ventricle with a D-shaped septum; no clot in the right heart."),
    ],
    plan=[
      ("Start anticoagulation now, on high clinical suspicion while the scan is arranged, unless she is "
       "bleeding; confirm with computed tomographic pulmonary angiography (a ventilation-perfusion scan only for "
       "kidney failure or a severe contrast allergy)."),
      ("Risk-stratify: a normal blood pressure, but right ventricular strain on the scan and echocardiogram and a "
       "raised troponin make it submassive (intermediate risk). Admit her to a monitored bed: she is at high "
       "risk of sudden deterioration, and outpatient treatment is not appropriate with a symptomatic "
       "embolism."),
      ("Anticoagulation by one of the standard strategies: heparin first (unfractionated by continuous infusion, "
       "or low molecular weight heparin), switched after 5 days to dabigatran or edoxaban, or overlapped with "
       "warfarin; or rivaroxaban or apixaban alone, starting with a loading dose. Provoked by minor transient "
       "risks (estrogen, prolonged travel): 3 to 6 months, with the decision point at 3 months."),
      ("Thrombolysis is not routine: in submassive embolism it is controversial, weighing faster right "
       "ventricular recovery against major and intracranial bleeding, so a student who weighs it that way is "
       "reasoning correctly. It becomes the treatment if she turns massive (systolic pressure under 90 for more "
       "than 15 minutes), with thrombectomy if thrombolysis is contraindicated."),
      "Stop the estrogen-containing pill.",
      ("Oxygen for her air hunger and mild hypoxemia (saturation 93%), adjusted to her saturation, and pain "
       "control."),
    ],
    education=[
      ("A blood clot formed in your left leg after the long flight, and a large piece of it broke off and "
       "lodged in the main artery to your right lung. The estrogen in your pill and sitting still on the plane "
       "both made a clot more likely."),
      ("The clot is straining the right side of your heart, so you will stay in the hospital on a heart monitor "
       "while the blood thinner starts working. Your blood pressure is holding well, and we will watch it "
       "closely."),
      ("The blood thinner stops the clot from growing and lets your body dissolve it. Because this clot had "
       "clear triggers, you will take it for 3 to 6 months, and we will decide at 3 months. Stop your birth "
       "control pill: its estrogen raises your risk of another clot."),
      ("If you are still short of breath 3 months from now, tell us: the strain on your heart today makes "
       "lasting damage to the lung arteries more likely, and we will check for it."),
      ("Tell the nurse at once, and later come straight back, for feeling faint, worse breathlessness, more than "
       "streaks of blood when you cough, or serious bleeding such as black stools, vomiting blood or a sudden "
       "severe headache."),
    ],
    red_flags=["Fainting, lightheadedness or a falling blood pressure (circulatory collapse)",
               "Worsening breathlessness or a falling oxygen level",
               "Coughing up more than streaks of blood, or serious bleeding on the blood thinner"],
    follow_up=("Admission to a monitored bed now; then the 3-month decision point on anticoagulation (provoked by "
               "minor transient risks: 3 to 6 months in all), with screening for chronic thromboembolic "
               "pulmonary hypertension if she is still breathless at 3 months, since right ventricular strain on "
               "her first scan is a risk factor for it."),
    presentation=(
      "Ms. Castillo is a 34-year-old woman on an estrogen birth control pill, who flew ten hours from Chile nine "
      "days ago, presenting with sudden sharp right-sided chest pain with every breath and breathlessness since "
      "this morning. She has coughed up blood-streaked sputum twice and has had five days of left calf pain and "
      "ankle swelling. She denies fainting, fever, wheeze, prior clots, cancer and surgery. Heart rate 110, "
      "respiratory rate 22, saturation 93% on room air, blood pressure 128/78. She is splinting on the right, "
      "with a right lower lateral pleural rub that stops on breath-holding and a swollen, warm, tender left "
      "calf. My differential is pulmonary embolism, pneumonia, pneumothorax and pericarditis. Her Wells score is "
      "8.5, so I would go straight to computed tomographic pulmonary angiography, with an electrocardiogram, "
      "chest X-ray, troponin, natriuretic peptide and echocardiogram. Diagnosis: submassive pulmonary embolism "
      "in the right main pulmonary artery, with right ventricular strain. Plan: heparin, a monitored bed, and "
      "stop the estrogen."),
    high_yield=[
      dict(item="Ask about leg swelling or calf pain, out loud",
           why=("It is the pulmonary embolism question: one-sided leg symptoms. Signs of a deep vein thrombosis "
                "are worth 3 Wells points, and she did not mention her calf until asked.")),
      dict(item="Ask the clotting risks: travel, immobility, surgery, estrogen, pregnancy, cancer and prior clots",
           why=("Virchow's triad: a flight over 8 hours and an estrogen pill are hers. Not finding a risk factor "
                "should never stop the workup when the picture fits.")),
      dict(item="Ask about coughing up blood and fainting",
           why=("Pleuritic pain with coughing up blood means a small, pleural-based infarction; fainting would "
                "mean circulatory collapse from a massive embolism.")),
      dict(item="Examine both legs",
           why="A swollen, warm, tender left calf is the source of the clot and adds 3 Wells points."),
      dict(item="Listen at the right lower lateral chest, then have her hold her breath",
           why=("A localized pleural rub goes with the infarction; it stops when she holds her breath, which "
                "separates it from a pericardial rub.")),
      dict(item="Calculate the Wells score out loud",
           why=("Deep vein thrombosis signs 3, embolism as the leading diagnosis 3, heart rate above 100 1.5, "
                "coughing up blood 1: 8.5, above 4, so straight to imaging. The pulmonary embolism rule-out "
                "criteria and the D-dimer are for scores of 4 or less.")),
      dict(item="Risk-stratify before choosing treatment",
           why=("Normal blood pressure with right ventricular strain or a raised troponin or natriuretic peptide "
                "is submassive, at high risk of sudden deterioration, where thrombolysis is controversial; a "
                "systolic pressure under 90 for more than 15 minutes is massive and needs thrombolysis.")),
      dict(item="Stop the estrogen and set the length of anticoagulation",
           why="Provoked by minor transient risks (estrogen, a long flight): 3 to 6 months, decided at 3 months."),
    ],
  ),
),

# =====================================================================================================
# LUNG CANCER (peripheral cavitating left upper lobe mass, no nodal or distant spread; no pleural effusion)
# =====================================================================================================
dict(
  id="pulmonary-lung-cancer",
  condition="Lung cancer",
  cites=("CMS L43 Pulmonary Nodules and Neoplasms, slides 3-4, 9, 12-14, 16-18, 22, 24, 31-35, 46, 48; CMS L38 "
         "Mycobacterial Infections including Tuberculosis slides 18-19, 26, 28, 33, 41; CMS L36 Chronic Obstructive "
         "Pulmonary Disease slides 21, 46; PD2 Thorax slides 17, 20-24, 26, 33, 40-42, 54, 60"),
  door=dict(
    name="Raymond Dunmore", sex="male", age=66, dob="August 23, 1960",
    setting="Outpatient primary care clinic",
    cc="\"My cough won't go away.\"",
    vitals=[("Blood pressure", "134/82 mmHg"),
            ("Heart rate", "84 beats per minute, regular"),
            ("Respiratory rate", "16 breaths per minute"),
            ("Temperature", "98.2 °F (36.8 °C)"),
            ("Oxygen saturation", "95% on room air"),
            ("Height and weight", "5 feet 11 inches, 162 pounds (body mass index 22.6)")],
  ),
  persona=("A 66-year-old retired long-haul truck driver, quiet and matter-of-fact, who smells of cigarette smoke "
           "and keeps clearing his throat. He plays it down ('probably just bronchitis') because he is afraid: his "
           "father died of lung cancer. He answers questions directly but does not mention the weight loss unless "
           "asked. His wife pushed him to come."),
  opening="This cough won't quit, and my wife made me come in because I've been seeing some blood.",
  facts=[
    ("Full name", "Raymond Dunmore."),
    ("Date of birth", "August 23, 1960."),
    ("Onset", "I've had a smoker's cough for years, but three or four months ago it changed. It's there all day "
              "now. Then about a month ago I started seeing blood in what I cough up."),
    ("Location", "It feels like it comes from deep in my chest, maybe more on the left."),
    ("Duration", "The cough is all day, every day now. The blood shows up a few times a week, usually first thing "
                 "in the morning."),
    ("Character", "A hacking cough. Some white phlegm, and lately little streaks of bright red blood in it."),
    ("Alleviating factors", "Nothing really. Cough drops help my throat."),
    ("Aggravating factors", "Mornings, and the first cigarette of the day. Cold air."),
    ("Radiation", "No pain going anywhere. It's a cough, not a pain."),
    ("Severity", "The cough bothers me maybe a four out of ten. The blood is what scares me. A ten was a kidney "
                 "stone in 2015."),
    ("Temporal pattern", "Worst in the morning. A little worse each month."),
    ("Prior episodes", "Never had blood before. Never a cough like this, just the usual morning one."),
    ("Cough", "Yes, all day for three or four months now. Before that, just mornings, for years."),
    ("Sputum", "Mostly white, not much. Never yellow or green, and it doesn't smell bad."),
    ("Coughing up blood", "Yes, for about a month. Streaks of bright red in the phlegm, a few times a week, never "
                          "more than a teaspoon. It comes up with the cough. It's not from my nose, and I'm not "
                          "throwing up."),
    ("Shortness of breath", "A little on stairs. Two flights winds me now. It didn't used to."),
    ("How far they can walk", "On flat ground, as far as I want. Two flights of stairs and I have to catch my "
                              "breath."),
    ("Wheezing", "No wheezing that I've noticed."),
    ("Chest pain with breathing", "No, no pain when I breathe."),
    ("Fever, chills or night sweats", "No fevers, no chills, no sweats at night."),
    ("Weight loss", "Yes, eighteen pounds since the summer without trying. I was 180, now I'm about 162. My belt's "
                    "on a new notch."),
    ("Orthopnea and waking up short of breath", "No, I sleep flat on one pillow and don't wake up short of "
                                                "breath."),
    ("Leg swelling or calf pain", "No, none."),
    ("Recent travel, immobility or surgery", "No. I stopped driving two years ago. No long trips, no surgery."),
    ("Sick contacts", "Nobody sick around me."),
    ("Constitutional", "Tired all the time the last couple of months, and not hungry like I used to be. And the "
                       "weight. No fevers or sweats."),
    ("Heart symptoms", "No chest pain, no racing heart, no fainting."),
    ("Ear, nose and throat", "My throat's raw from coughing. No stuffy nose, no drip down the back of my throat."),
    ("Heartburn or reflux", "No heartburn."),
    ("Anything else", "No, that's about it. My wife made me come because of the blood."),
    ("Chronic conditions", "High blood pressure. That's it, that I know of."),
    ("Known lung disease", "Nobody's ever told me I have lung disease. I've never had a breathing test."),
    ("Surgeries and procedures", "A knee scope in 2008. They broke up a kidney stone in 2015."),
    ("Hospitalizations", "Just one night for the kidney stone."),
    ("Prescription medications", "Amlodipine 5 milligrams every morning for my blood pressure, about six years."),
    ("Taking them as prescribed", "Yes, most days."),
    ("Over-the-counter medicines and supplements", "Cough drops. A cough syrup a while back that didn't do "
                                                   "anything. No aspirin, no blood thinners."),
    ("Allergies", "No drug allergies."),
    ("Tobacco", "Since I was eighteen, a pack a day, sometimes more on the road. I still smoke about a pack a "
                "day."),
    ("Vaping and marijuana", "No vaping. Some marijuana in my twenties, nothing since."),
    ("Alcohol", "Three or four beers a week."),
    ("Recreational drugs", "No."),
    ("Occupation and exposures", "Long-haul truck driver for thirty-five years. Retired two years ago. Lots of "
                                 "diesel fumes at the truck stops."),
    ("Home and environment", "A 1970s house with a finished basement, where I spend most evenings. Gas heat. No "
                             "pets. Nobody's ever tested the house for anything."),
    ("Living situation", "With my wife, Linda. Our daughter lives in town."),
    ("Immunizations", "I don't do flu shots. Never had a pneumonia shot."),
    ("Tuberculosis exposure or testing", "Not that I know of. Nobody around me has had it. I've never been "
                                         "tested."),
    ("Family history, mother", "My mother had a stroke at 78 and passed at 80."),
    ("Family history, father", "My father smoked, and he died of lung cancer at 70."),
    ("Family history, siblings", "My brother has emphysema. My sister is healthy."),
    ("What they think it is", "Linda thinks it's cancer, like my dad. I'm hoping it's bronchitis."),
    ("Concerns", "Honestly, that it's cancer. I watched what it did to my father."),
    ("Lung cancer screening", "A doctor mentioned a yearly scan for smokers once, maybe eight years ago. I never "
                              "went."),
    ("Last checkup", "About three years ago, for blood pressure refills. The pharmacy's been refilling it since."),
    ("Headaches or vision changes", "No headaches, no trouble with my vision."),
    ("Bone pain", "No bone pain, no back pain."),
    ("Confusion or unsteadiness", "No. I'm thinking straight and walking fine."),
    ("Belly pain or yellow skin", "No pain in my belly on the right. My skin isn't yellow."),
    ("Voice and swallowing", "My voice is the same as always, and food goes down fine."),
    ("Fingertips", "Linda says my fingertips look kind of puffy lately. I hadn't noticed."),
  ],
  questions=["Is it cancer?",
             "Can't you just give me an antibiotic and see if it clears up?",
             "Do I really have to quit smoking now?"],
  # The mass sits in the periphery of the left upper lobe, as in the CMS L43 slide 34 computed tomography. PD2 Thorax
  # slides 26 and 33 (clubbing in lung cancer and malignancy), 40 (decreased fremitus over an infiltrating tumor;
  # asymmetric decrease concerning for neoplasm), 42 (dullness over tumor). A solid mass is not consolidation, so no
  # egophony or bronchophony (slides 54, 60), and it is in the upper lobe, so the diaphragm is normal (no effusion).
  exam={
    "general-survey": ("Thin man who looks older than his age, alert and comfortable at rest, speaking in full "
                       "sentences with an occasional cough. His clothes hang loose and his belt is cinched to a new "
                       "hole. Normal color. He smells of cigarette smoke."),
    "nails": ("Clubbing of the fingers: bulbous swelling of the soft tissue at the nail base, the normal angle "
              "between the nail and the proximal nail fold is lost, and the nail beds feel spongy. Nail beds pink, "
              "no cyanosis."),
    "fremitus": ("Tactile fremitus is decreased over the left upper chest, anteriorly below the outer part of the "
                 "left clavicle and high in the left axilla, compared with the right. Symmetric and normal "
                 "posteriorly and elsewhere."),
    "percuss-anterior": ("Anterior chest: dull over the outer part of the left upper chest below the clavicle; "
                         "resonant over the right upper lobe and elsewhere."),
    "percuss-lateral": "Lateral chest: dull high in the left axilla; resonant lower down and on the right.",
    "ausc-anterior": ("Anterior chest: decreased breath sounds over the dull area of the left upper chest. "
                      "Vesicular over the right upper lobe. No crackles, wheezes or pleural rub."),
    "ausc-lateral": ("Lateral chest: decreased breath sounds high in the left axilla; vesicular lower down and on "
                     "the right. No crackles."),
  },
  # CMS L43 slide 13: liver metastasis (hepatomegaly with a firm edge); brain metastasis (papilledema)
  special=[
    ("liver-palp", "Liver palpation",
     "palpates the right upper abdomen for the liver edge and tenderness",
     "The liver edge is not palpable below the right costal margin, and the right upper abdomen is not tender."),
    ("fundoscopy", "Fundoscopic examination",
     "looks at both optic discs with the ophthalmoscope",
     "Both optic discs have sharp margins. No papilledema."),
  ],
  must_exam=['nails', 'fremitus', 'percuss-anterior', 'ausc-anterior', 'lymph-nodes'],
  # CMS L43 slide 14: chest X-ray may first show the mass; the standard is computed tomography of the chest and upper
  # abdomen with contrast, then biopsy (bronchoscopic, transthoracic or thoracoscopic by location, can be guided by
  # computed tomography), positron emission tomography and genetic testing; laboratory work is a blood count with
  # differential, a metabolic panel with calcium and alkaline phosphatase, and pulmonary function tests (slide 35:
  # he must be able to tolerate surgery).
  # Slides 16 (concerning nodules), 17 (uptake), 33-34 (large cell: peripheral, cavitated), 24 (stage IIA: more than
  # 4 and no more than 5 centimeters, no lymph nodes).
  tests=[
    dict(id="cxr", name="Chest X-ray",
         aka=["CXR", "chest film", "chest radiograph", "chest x ray", "chest x-ray", "chest imaging"],
         result=("A 4.5-centimeter mass in the periphery of the left upper lobe with a central lucency (a cavity). "
                 "No pleural effusion. The right lung is clear."),
         here=True),
    dict(id="ct-chest", name="Computed tomography of the chest and upper abdomen with contrast",
         aka=["CT", "CT chest", "chest CT", "CT scan", "CT with contrast", "CAT scan", "CT chest abdomen",
              "computed tomography"],
         result=("A 4.6-centimeter thick-walled, cavitating mass with irregular, spiculated borders in the periphery "
                 "of the left upper lobe. No enlarged hilar or mediastinal lymph nodes, no pleural effusion, and the "
                 "liver and adrenal glands are clear."),
         here=True),
    dict(id="pet-ct", name="Positron emission tomography with computed tomography (PET-CT)",
         aka=["PET", "PET scan", "PET-CT", "PET CT", "positron emission tomography"],
         result=("High uptake in the left upper lobe mass. No uptake in any lymph node or anywhere else in the "
                 "body."),
         here=True),
    dict(id="biopsy", name="Biopsy of the mass",
         aka=["biopsy", "bronchoscopy", "tissue biopsy", "lung biopsy", "needle biopsy", "transthoracic biopsy",
              "CT-guided biopsy", "EBUS"],
         result=("Not available in this clinic: a specialist takes the biopsy with a needle through the chest wall, "
                 "guided by computed tomography."),
         here=False),
    dict(id="cbc", name="Complete blood count with differential",
         aka=["CBC", "CBC with diff", "complete blood count", "blood count", "white count", "hemoglobin"],
         result="Normal: white blood cell count, differential, hemoglobin and platelets normal. No anemia.",
         here=True),
    dict(id="cmp", name="Comprehensive metabolic panel with calcium and alkaline phosphatase",
         aka=["CMP", "BMP", "comprehensive metabolic panel", "metabolic panel", "chemistry", "calcium", "sodium",
              "electrolytes", "alkaline phosphatase", "ALP", "liver function tests", "LFTs"],
         result=("Calcium normal at 9.4 milligrams per deciliter. Sodium normal at 139 mEq/L. Alkaline phosphatase, "
                 "liver tests, potassium, glucose and kidney function normal."),
         here=True),
    dict(id="pft", name="Pulmonary function tests",
         aka=["PFT", "PFTs", "pulmonary function tests", "spirometry", "lung function test", "breathing test",
              "DLCO", "diffusing capacity"],
         result="Not available in this clinic: it is done in a pulmonary function laboratory.",
         here=False),
    # CMS L38 slides 19 and 26: symptoms or suspicious imaging need microbiologic testing; three sputum specimens
    # 8-24 hours apart for smear and culture, with a rapid molecular test
    dict(id="sputum-afb", name="Sputum acid-fast bacilli smears, mycobacterial culture and rapid molecular test",
         aka=["AFB", "sputum AFB", "acid-fast", "acid fast bacilli", "sputum smear", "TB sputum",
              "sputum for TB", "mycobacterial culture", "NAAT", "TB PCR"],
         result=("Three sputum specimens collected 8 to 24 hours apart: acid-fast bacilli smears negative and the "
                 "rapid molecular test for tuberculosis negative. Mycobacterial cultures pending."),
         here=True),
  ],
  key=dict(
    diagnosis=("Lung cancer until the biopsy proves otherwise: a 4.6-centimeter peripheral, cavitating, spiculated "
               "left upper lobe mass with high uptake and no lymph node or distant spread, in a 48 pack-year current "
               "smoker with coughing up blood, weight loss and clubbing. Most likely a non-small cell cancer (a "
               "large, peripheral, cavitated tumor fits large cell carcinoma); if confirmed, stage IIA and a "
               "candidate for surgery"),
    must_not_miss=["Massive hemoptysis: more than 600 mL in 24 hours is life threatening and needs the emergency "
                   "department now",
                   "Spread beyond the chest or a paraneoplastic syndrome: ask about headache, vision change, bone "
                   "pain, right upper abdominal pain and confusion, and check the calcium, sodium and alkaline "
                   "phosphatase"],
    ddx=[
      dict(name="Lung cancer (most likely non-small cell; peripheral cavitating mass)",
           support=("Over 50, 48 pack-years and still smoking, a father with lung cancer; a chronic cough that "
                    "changed three to four months ago, a month of blood-streaked sputum, 18 pounds of unintended "
                    "weight loss, fatigue and new breathlessness on stairs. Clubbing; dullness, decreased fremitus "
                    "and decreased breath sounds over the left upper lobe. A spiculated, cavitating upper lobe mass "
                    "over 6 millimeters with high uptake on positron emission tomography."),
           against=("Not proven until the biopsy: inflammation can also take up the tracer.")),
      dict(name="Tuberculosis",
           support=("A cough over 8 weeks, coughing up blood, weight loss, fatigue, and a cavity in an upper lobe, "
                    "where reactivated tuberculosis tends to cavitate."),
           against=("No fevers or night sweats, no exposure, a spiculated, thick-walled mass, and negative smears "
                    "and rapid molecular test (cultures pending).")),
      dict(name="Lung abscess",
           support="A cavitating lesion with cough and coughing up blood.",
           against=("No fever, and the sputum is scant, white and not foul smelling; months of weight loss and a "
                    "spiculated mass point to a tumor.")),
      dict(name="Pulmonary embolism",
           support="Coughing up blood with some breathlessness.",
           against=("Months of gradual symptoms, no sudden breathlessness, pleuritic pain or leg swelling, a heart "
                    "rate of 84 and a saturation of 95%; it explains neither the mass nor the clubbing.")),
    ],
    studies=[
      dict(test="Chest X-ray",
           why=("Often the first test to show the mass, but not a good tool for working it up; it also rules out "
                "other disease."),
           expect="A 4.5-centimeter peripheral left upper lobe mass with a cavity; no effusion."),
      dict(test="Computed tomography of the chest and upper abdomen with contrast",
           why=("The standard next step: size, borders and location of the mass, the lymph nodes, and the liver "
                "and adrenal glands for spread."),
           expect=("A 4.6-centimeter spiculated, cavitating mass in the periphery of the left upper lobe (over 6 "
                   "millimeters, upper lobe, spiculated, cavitated: all concerning); no enlarged nodes, no "
                   "effusion, liver and adrenal glands clear.")),
      dict(test="Positron emission tomography with computed tomography",
           why=("Highly metabolic tissue takes up the tracer, suggesting malignancy, and it shows lymph node "
                "involvement for staging; inflammation can take it up too."),
           expect="High uptake in the mass only: no lymph node or distant spread."),
      dict(test="Biopsy of the mass",
           why=("The biopsy classes the tumor; this peripheral mass is reached with a needle through the chest wall "
                "guided by computed tomography, and molecular testing of the tissue follows."),
           expect=("A non-small cell lung cancer; anaplastic, undifferentiated large cells with a negative mucin "
                   "stain would make it large cell carcinoma.")),
      dict(test="Comprehensive metabolic panel with calcium and alkaline phosphatase",
           why=("Calcium for the hypercalcemia of squamous cell cancer, sodium for the low sodium of inappropriate "
                "antidiuretic hormone secretion, and alkaline phosphatase and liver tests for spread to bone or "
                "liver."),
           expect="Normal calcium, sodium, alkaline phosphatase and liver tests."),
    ],
    plan=[
      ("Urgent referral for a biopsy of the peripheral mass with a needle guided by computed tomography, with "
       "molecular testing of the tissue."),
      ("Pulmonary function tests to judge whether he can tolerate surgery. His blood count with differential and "
       "metabolic panel with calcium and alkaline phosphatase are already done and normal."),
      ("Until tuberculosis is excluded (a cavitating upper-lobe lesion with coughing up blood and weight loss): a "
       "mask on him, airborne precautions with N95 respirators for staff, and isolation ended only on clinical and "
       "laboratory criteria; his sputum smears and rapid molecular test are negative, with cultures pending."),
      ("Refer to thoracic surgery and oncology: a non-small cell cancer of more than 4 and no more than 5 "
       "centimeters without lymph node spread is stage IIA, and stages I to IIIB are resected (lobectomy, or a "
       "wedge or segment) if he can tolerate surgery, with chemotherapy, targeted therapy or immunotherapy as "
       "adjuncts guided by the tumor's markers."),
      "Smoking cessation today: counseling with nicotine replacement, bupropion or varenicline.",
      ("Emergency department for heavy bleeding (more than 600 mL in 24 hours), breathlessness at rest, chest pain "
       "or confusion."),
    ],
    education=[
      ("The scans show a mass in the outer part of your left lung with a hollow center, and it lights up on the "
       "special scan the way cancer often does. With your smoking, the blood and the weight loss, I'm worried it is "
       "lung cancer, but we can't call it cancer until a small sample is looked at under the microscope."),
      ("A specialist will take that sample with a thin needle through your chest wall, using the scanner to guide "
       "it."),
      ("The scans show no spread to the lymph nodes or anywhere else. If it is cancer, one this size that hasn't "
       "spread can often be removed with surgery."),
      ("Stopping smoking now matters, and you don't have to do it alone: we have counseling and medicines that "
       "help."),
      ("Go to the emergency room right away if you cough up more than a few spoonfuls of blood, get short of "
       "breath or chest pain, or become confused."),
    ],
    red_flags=["Coughing up a large amount of blood (more than 600 mL in 24 hours)",
               "Breathlessness at rest or chest pain",
               "Confusion, seizures or unsteadiness",
               "New bone pain, headache or vision change"],
    follow_up=("Promptly, with the biopsy arranged as soon as possible and the pulmonary function tests reviewed; "
               "then shared care with thoracic surgery and oncology once the biopsy is back."),
    presentation=(
      "Mr. Dunmore is a 66-year-old retired truck driver with hypertension and 48 pack-years, still smoking, "
      "presenting with three to four months of a changed, persistent cough and a month of blood-streaked sputum, "
      "never more than a teaspoon. He has lost 18 pounds without trying and is newly winded on two flights of "
      "stairs. He denies fever, night sweats, chest pain, voice change, headaches, bone pain and tuberculosis "
      "exposure, and was never screened. His father died of lung cancer. Vital signs are normal, saturation 95%. "
      "He has clubbing, and dullness, decreased fremitus and decreased breath sounds over the left upper lobe, "
      "without egophony; no lymph nodes. My differential is lung cancer, tuberculosis, lung abscess and pulmonary "
      "embolism. Computed tomography shows a 4.6-centimeter spiculated, cavitating peripheral left upper lobe mass "
      "with high uptake on positron emission tomography and no nodal spread; sputum tests for tuberculosis are "
      "negative. My working diagnosis is lung cancer, likely non-small cell. Plan: guided needle biopsy, "
      "pulmonary function tests, surgical referral and smoking cessation."),
    high_yield=[
      dict(item="Characterize the blood: how much, how often, and where it comes from",
           why=("Streaks, never more than a teaspoon, coughed up, not from the nose or stomach; more than 600 mL "
                "in 24 hours is massive and life threatening.")),
      dict(item="Ask about weight loss and put a number on it",
           why=("18 pounds in four months without trying is a systemic symptom of cancer; tuberculosis would "
                "usually bring fevers and night sweats as well.")),
      dict(item="Count the pack-years and ask about lung cancer screening",
           why=("48 pack-years and still smoking: he has qualified for a yearly low-dose computed tomography since "
                "55 (ages 55 to 80, 30 or more pack-years, smoking now or quit within 15 years) and never had "
                "one.")),
      dict(item="Inspect the nails for clubbing",
           why=("Loss of the nail-fold angle with a spongy nail bed points to lung cancer; it is rare in chronic "
                "obstructive pulmonary disease.")),
      dict(item="Percuss, palpate fremitus and listen side to side over the upper lobes",
           why=("Dullness with decreased fremitus and breath sounds over the left upper lobe and no egophony fit a "
                "solid mass at the chest wall; consolidation would raise the fremitus and give egophony, and an "
                "effusion would sit at the base.")),
      dict(item="Palpate the cervical and supraclavicular lymph nodes",
           why="Spread to lymph nodes changes the stage and the treatment; his are not palpable."),
      dict(item="Ask about symptoms of spread and of paraneoplastic syndromes",
           why=("Headaches, vision change, bone pain, right upper abdominal pain or confusion would mean "
                "metastases or low sodium; he has none.")),
      dict(item="Ask about tuberculosis exposure, fevers and night sweats",
           why=("A cavitating upper lobe lesion keeps tuberculosis on the differential until the sputum smears, "
                "rapid molecular test and cultures are back.")),
    ],
  ),
),

# =====================================================================================================
# ASTHMA (moderate acute exacerbation, viral trigger, stopped inhaled corticosteroid)
# =====================================================================================================
dict(
  id="pulmonary-asthma",
  condition="Asthma",
  cites=("CMS L35 Asthma, slides 5, 10, 12, 14, 24-25, 30, 38-39, 41, 45-54, 56, 59-63, 69, 71, 74-76, 86, "
         "88, 90-93, 99-101; CMS L42 Pulmonary Vascular Disorders slides 53-54, 57; PD2 Thorax slides 16-18, "
         "31-33, 35, 42-43, 48-49, 57-58, 60"),
  door=dict(
    name="Megan Kowalski", sex="female", age=27, dob="April 14, 1999",
    setting="Urgent care",
    cc="\"I can't catch my breath.\"",
    vitals=[("Blood pressure", "128/78 mmHg"),
            ("Heart rate", "108 beats per minute, regular"),
            ("Respiratory rate", "24 breaths per minute"),
            ("Temperature", "99.0 °F (37.2 °C)"),
            ("Oxygen saturation", "94% on room air"),
            ("Height and weight", "5 feet 5 inches, 140 pounds (body mass index 23.3)")],
  ),
  persona=("A 27-year-old kindergarten teacher, friendly and talkative by nature but now pausing to breathe "
           "between short sentences, sitting forward with her hands on her knees. She knows her asthma and her "
           "inhalers well. She is a little embarrassed that she stopped her daily inhaler and admits it when asked "
           "directly, and she is worried about missing work."),
  opening="I've had a cold all week, and now my asthma's really bad. My inhaler only helps for an hour.",
  facts=[
    ("Full name", "Megan Kowalski."),
    ("Date of birth", "April 14, 1999."),
    ("Onset", "It started with a cold last Sunday, a stuffy nose and a scratchy throat. On Wednesday it went to "
              "my chest, and since yesterday the wheezing has been really bad."),
    ("Location", "Across my whole chest. It's tight, like a band around it."),
    ("Duration", "It's been there all the time since yesterday. The inhaler loosens it for about an hour, then "
                 "it's right back."),
    ("Character", "Tight, like I can't get the air back out. Like breathing out through a straw, and I'm "
                  "wheezing."),
    ("Alleviating factors", "My albuterol helps for a while. Sitting up and leaning forward helps a little."),
    ("Aggravating factors", "Talking a lot, walking, the cold air outside, and lying down at night. Laughing sets "
                            "off the coughing."),
    ("Radiation", "No, it doesn't go anywhere. It's just my chest."),
    ("Severity", "A seven out of ten. A ten was the attack when I was sixteen, when the ambulance took me in."),
    ("Temporal pattern", "Worst at night and early in the morning. I've woken up around three in the morning the "
                         "last two nights."),
    ("Prior episodes", "I've had attacks like this, but not this bad since I was a teenager. Last February I had "
                       "one with a cold, and urgent care gave me prednisone."),
    ("Cough", "Yes, since Wednesday. Mostly dry and tight, and worse at night."),
    ("Sputum", "A little clear or white stuff in the morning. Not yellow or green."),
    ("Coughing up blood", "No, never."),
    ("Shortness of breath", "Yes. Even sitting here I'm a little short of breath, and I have to stop and breathe "
                            "when I talk a lot."),
    ("How far they can walk", "Normally I run three miles. This morning I had to stop halfway across the parking "
                              "lot to catch my breath."),
    ("Wheezing", "Yes, I can hear it myself, a whistle when I breathe out. My roommate heard it from the other "
                 "room last night."),
    ("Chest pain with breathing", "No sharp pain when I breathe in. Just the tightness."),
    ("Fever, chills or night sweats", "No real fevers, just felt a little warm once. No chills or sweats."),
    ("Weight loss", "No, my weight's the same."),
    ("Orthopnea and waking up short of breath", "I can lie flat. But the last two nights I woke up around three, "
                                                "coughing and wheezing, and had to sit up and use my inhaler."),
    ("Leg swelling or calf pain", "No, my legs are fine. No swelling or pain."),
    ("Recent travel, immobility or surgery", "No travel, no long drives or flights, no surgery. I've been on my "
                                             "feet at work all week."),
    ("Sick contacts", "Half my kindergarten class has had runny noses and coughs for two weeks."),
    ("Constitutional", "I'm tired from not sleeping well. No fevers, no sweats, no weight change."),
    ("Heart symptoms", "My heart's been beating fast, especially after I use the inhaler, and it makes me a little "
                       "shaky. No chest pain, no fainting."),
    ("Ear, nose and throat", "A stuffy nose and a scratchy throat with the cold. My nose is always a bit stuffy in "
                             "the spring with my allergies. No ear pain."),
    ("Heartburn or reflux", "No heartburn."),
    ("Anything else", "No, I think that's it. I just want to be able to breathe."),
    ("Chronic conditions", "Just the asthma and my allergies. I had eczema as a kid, and I still get it in my "
                           "elbows."),
    ("Known lung disease", "Asthma since I was four. It mostly went away after I finished high school, then came "
                           "back when I "
                           "was about twenty-four after a bad cold. Last year they did the breathing test where I "
                           "blew into a tube before and after the inhaler, and it got a lot better with the "
                           "inhaler."),
    ("Surgeries and procedures", "My wisdom teeth out at eighteen. That's all."),
    ("Hospitalizations", "One night at sixteen for an asthma attack. They gave me breathing treatments and "
                         "steroids. I never needed the intensive care unit or a breathing tube."),
    ("Prescription medications", "Albuterol, two puffs when I need it. Fluticasone, the orange inhaler, two puffs "
                                 "twice a day, but I stopped it in August. And my birth control pill, the "
                                 "combined kind with estrogen, for about five years."),
    ("Taking them as prescribed", "Honestly, no. I stopped the fluticasone in August when it ran out. I felt fine, "
                                  "and it's fifty dollars a month."),
    ("Over-the-counter medicines and supplements", "A daytime cold medicine and some acetaminophen this week. "
                                                   "Cetirizine in the spring for allergies. No supplements."),
    ("Allergies", "No drug allergies. I'm allergic to dust mites and grass pollen. They tested me as a kid."),
    ("Tobacco", "Never. I can't be around smoke at all."),
    ("Vaping and marijuana", "No, neither."),
    ("Alcohol", "A glass of wine or two on the weekend."),
    ("Recreational drugs", "No."),
    ("Occupation and exposures", "I teach kindergarten. No chemicals or dust at work. My breathing isn't any "
                                 "better on weekends or vacations."),
    ("Home and environment", "An apartment. No pets. We have carpet, and I use the dust mite covers on my pillows. "
                             "No mold that I know of, and nobody smokes."),
    ("Living situation", "I live with my roommate, Jess. She drove me here."),
    ("Immunizations", "I had all my childhood shots. I haven't gotten a flu shot yet this year, and I've never had "
                      "a pneumonia shot."),
    ("Tuberculosis exposure or testing", "I had a skin test for my teaching job three years ago. It was negative. "
                                         "No exposure that I know of."),
    ("Family history, mother", "My mom has asthma and bad hay fever."),
    ("Family history, father", "My dad has high blood pressure. Otherwise he's healthy."),
    ("Family history, siblings", "My younger brother had eczema as a kid. No asthma."),
    ("What they think it is", "My asthma, from this cold. I probably shouldn't have stopped the orange inhaler."),
    ("Concerns", "I'm scared because it feels like when I was sixteen. And I can't miss more work. The kids need "
                 "me."),
    ("Rescue inhaler use this week", "Every three to four hours since yesterday, two puffs, sometimes four. "
                                     "Before the cold, maybe three days a week since August."),
    ("Last rescue inhaler dose", "Four puffs about an hour before I came in. It helped for maybe thirty "
                                 "minutes."),
    ("Peak flow at home", "I have the meter. My best is 440. This morning I blew 250. I don't check it every day, "
                          "honestly."),
    ("Waking at night before this cold", "Three or four times a month since I stopped the fluticasone."),
    ("Inhaler technique", "I just spray it in my mouth and breathe in. I lost the spacer a while ago."),
    ("Steroid courses in the past year", "Just the one last February, five days of prednisone."),
    ("Usual triggers", "Colds are the worst. Dust, cold air and running in the winter, too. Cats make me itchy and "
                       "wheezy."),
    ("Aspirin and ibuprofen", "I take ibuprofen for cramps sometimes. It's never made my breathing worse."),
  ],
  questions=["Do I have to go to the hospital?",
             "Why should I take the orange inhaler every day if I feel fine most of the time?",
             "Can I go back to work on Monday?"],
  # PD2 Thorax slide 58 (asthma): tachypnea, decreased excursion, diminished fremitus, resonant to diffusely
  # hyperresonant, wheezes, prolonged expiration. CMS L35 slide 50: leaning forward, hunched shoulders. No accessory
  # muscle use or retraction: CMS L35 slide 101 puts those in the severe grade, and this exacerbation is moderate.
  exam={
    "position": "She sits on the edge of the table leaning forward with her hands on her knees and does not want "
                "to lie back.",
    "general-survey": ("Alert, anxious young woman, mildly short of breath at rest, sitting forward with her "
                       "shoulders hunched. She speaks in short sentences and pauses for a breath between them. "
                       "Audible expiratory wheeze. Normal color, no cyanosis, no sweating."),
    "breathing-pattern": ("Respiratory rate 24 and regular, with a markedly prolonged expiratory phase, about twice "
                          "as long as inspiration. Breathing effort is mildly increased."),
    "fremitus": "Tactile fremitus is diminished and symmetric posteriorly, laterally and anteriorly.",
    "percuss-posterior": "Posterior chest: diffusely hyperresonant and symmetric.",
    "percuss-lateral": "Lateral chest: hyperresonant and symmetric on both sides.",
    "percuss-anterior": "Anterior chest: hyperresonant and symmetric over both upper lobes.",
    "diaphragm-excursion": "Decreased: about 2 centimeters on each side, with the diaphragm at the same level on "
                           "both sides.",
    "ausc-posterior": ("Posterior chest: diffuse high-pitched expiratory wheezes over both lungs with a prolonged "
                       "expiratory phase. Air movement is reduced but heard at every level. No crackles, rhonchi or "
                       "pleural rub."),
    "ausc-lateral": ("Lateral chest: expiratory wheezes on both sides with a prolonged expiratory phase. No "
                     "crackles."),
    "ausc-anterior": ("Anterior chest: expiratory wheezes over both upper lobes with a prolonged expiratory phase. "
                      "No crackles. No inspiratory sound over the neck (no stridor)."),
    "heart-ausc": ("Regular tachycardia at about 108. Normal first and second heart sounds, with no murmur, rub or "
                   "extra heart sound."),
  },
  # CMS L35 slide 49: extrinsic (allergic) asthma may show swollen nasal mucosa, increased secretions, eczema,
  # nasal polyps
  special=[
    ("nasal-inspect", "Nasal mucosa inspection",
     "looks inside each nostril with a light",
     "The nasal mucosa is swollen on both sides with increased clear secretions. No nasal polyps."),
    ("skin-eczema", "Skin inspection for eczema",
     "looks at the skin of the elbow creases, wrists and backs of the knees",
     "Dry, slightly thickened patches of eczema in both elbow creases. No rash elsewhere."),
  ],
  must_exam=['general-survey', 'accessory-muscles', 'breathing-pattern', 'percuss-posterior', 'ausc-posterior',
             'legs'],
  # CMS L35 slide 101: initial assessment is peak flow or forced expiratory volume in 1 second plus saturation;
  # 40-69% moderate, under 40% severe; a good response is 70% or more sustained 60 minutes after the last treatment.
  tests=[
    dict(id="peak-flow", name="Peak expiratory flow",
         aka=["peak flow", "PEF", "PEFR", "peak expiratory flow", "peak flow meter", "peak flow rate"],
         result=("Before treatment: 240 liters per minute, 55% of her personal best of 440. After three albuterol "
                 "and ipratropium nebulizer treatments in the first hour: 330 liters per minute (75%), still 75% "
                 "an hour after the last treatment. At that recheck she is breathing comfortably and speaking in "
                 "full sentences, and her lungs are clear with no wheeze."),
         here=True),
    # CMS L35 slide 59: usually normal or may show hyperinflation
    dict(id="cxr", name="Chest X-ray",
         aka=["CXR", "chest film", "chest radiograph", "chest x ray", "chest x-ray", "chest imaging"],
         result="Hyperinflated lungs. No infiltrate, no pneumothorax and no effusion. Normal heart size.",
         here=True),
    # CMS L35 slides 52-54: before and after a short-acting bronchodilator; reduced forced expiratory volume in 1
    # second and ratio, improvement of 12% or more. Values from the slide 56 graph: 2.2 L against a normal 3.5 L (63%),
    # forced vital capacity 3.6 L, ratio 61%.
    dict(id="spirometry", name="Spirometry before and after a bronchodilator",
         aka=["spirometry", "PFT", "PFTs", "pulmonary function tests", "lung function test", "FEV1",
              "breathing test", "pre and post bronchodilator spirometry"],
         result=("On file from last year, when her asthma was confirmed as an adult; not repeated during the "
                 "attack. Before the bronchodilator: forced expiratory volume in 1 second (FEV1) 2.2 L (63% of "
                 "predicted), forced vital capacity (FVC) 3.6 L, ratio 0.61 (reduced). After albuterol: forced "
                 "expiratory volume in 1 second 2.5 L, a 14% improvement (reversible)."),
         here=True),
    dict(id="abg", name="Arterial blood gas",
         aka=["ABG", "arterial blood gas", "blood gas", "VBG", "venous blood gas"],
         result="Not available in this clinic: it is done in a hospital emergency department.",
         here=False),
    # CMS L35 slide 39: influenza and coronavirus among the viral triggers
    dict(id="flu-covid", name="Influenza and coronavirus disease 2019 (COVID-19) swab",
         aka=["flu test", "flu swab", "influenza test", "COVID test", "COVID swab", "rapid flu", "viral swab",
              "respiratory viral panel"],
         result="Negative for influenza A, influenza B and coronavirus disease 2019.",
         here=True),
    dict(id="cbc", name="Complete blood count (CBC)",
         aka=["CBC", "complete blood count", "blood count", "white count", "hemoglobin"],
         result="Normal: white blood cell count, hemoglobin and platelets normal.",
         here=True),
    dict(id="ecg", name="Electrocardiogram (12-lead)",
         aka=["EKG", "ECG", "12-lead", "12 lead", "electrocardiogram", "heart tracing"],
         result="Sinus tachycardia at 108. Normal intervals and no ischemic changes.",
         here=True),
    # CMS L42 slides 53-54, 57: she fails the rule-out criteria (heart rate, saturation, estrogen) with a Wells score
    # of 1.5 (unlikely), so a D-dimer is the next step; a negative one excludes the clot
    dict(id="d-dimer", name="D-dimer",
         aka=["D-dimer", "d dimer", "dimer", "ddimer"],
         result="Negative.",
         here=True),
  ],
  key=dict(
    diagnosis=("Acute exacerbation of asthma, moderate (peak flow 55% of her personal best, in the 40 to 69% "
               "band), triggered by a viral cold in a patient whose control slipped after she stopped her daily "
               "inhaled corticosteroid; good response to treatment, safe for discharge with an action plan"),
    must_not_miss=["A severe or life-threatening exacerbation: peak flow under 40%, accessory muscle use or chest "
                   "retraction at rest, a quiet chest, drowsiness or confusion means oxygen, continuous treatment "
                   "and transfer to the emergency department",
                   "Pulmonary embolism in a breathless, tachycardic woman taking an estrogen pill: ask about sudden "
                   "onset, pleuritic pain, coughing up blood and a swollen leg"],
    ddx=[
      dict(name="Asthma, moderate acute exacerbation",
           support=("Known asthma with a classic trigger (a cold from her class) after stopping her inhaled "
                    "corticosteroid in August; albuterol every 3 to 4 hours with brief relief, waking at 3 in the "
                    "morning, wheeze, chest tightness and a mostly dry cough. Respiratory rate 24, a prolonged "
                    "expiratory phase, diffuse expiratory wheezes, diffuse hyperresonance, diminished fremitus and "
                    "reduced diaphragmatic excursion; swollen nasal mucosa and elbow eczema mark allergic asthma. "
                    "Peak flow 55% of her best."),
           against=("Nothing against asthma. Against a severe grade: no accessory muscle use or chest "
                    "retraction, symptoms only mild at rest, and a peak flow of 55% (the 40 to 69% band), so "
                    "moderate.")),
      dict(name="Vocal fold dysfunction",
           support="Episodes of noisy, breathless breathing in a young woman.",
           against=("The noise is an expiratory wheeze over the chest, not an inspiratory stridor over the neck; "
                    "the hyperresonance and diminished fremitus are air trapping, and her peak flow rose with "
                    "albuterol.")),
      dict(name="Pneumonia",
           support="Started with a cold; cough, a temperature of 99.0 and a fast heart rate.",
           against=("Clear-to-white sputum, no fever or chills, no pleuritic pain; no dullness, increased fremitus, "
                    "bronchial breath sounds or egophony over any area, and no infiltrate on the chest X-ray.")),
      dict(name="Pulmonary embolism",
           support=("A heart rate of 108, a saturation of 94% and an estrogen birth control pill: she does not "
                    "pass the pulmonary embolism rule-out criteria."),
           against=("A gradual start with a cold, a diffuse wheeze that eased with albuterol, and no pleuritic "
                    "pain, coughing up blood, leg swelling, travel, immobility or surgery; Wells score 1.5 (only "
                    "the heart rate), so unlikely, and the D-dimer is negative.")),
    ],
    studies=[
      dict(test="Peak expiratory flow",
           why=("Grades the exacerbation against her personal best (70% or more good, 40 to 69% moderate, under "
                "40% severe) and is repeated after the first hour of treatment to decide discharge or admission."),
           expect=("240 liters per minute, 55% of her best of 440: moderate. After three treatments in the first "
                   "hour, 330 (75%), holding an hour later: a good response.")),
      dict(test="Chest X-ray",
           why=("Usually normal or shows hyperinflation in asthma; it looks for another cause of the "
                "breathlessness, such as pneumonia or a pneumothorax."),
           expect="Hyperinflation; no infiltrate, pneumothorax or effusion."),
      dict(test="Spirometry before and after a bronchodilator",
           why=("The objective measure of airflow, read from her chart rather than repeated during the attack: "
                "reversible obstruction (an improvement of 12% or more in the forced expiratory volume in 1 second "
                "after albuterol) strongly supports asthma; repeated yearly to monitor."),
           expect=("On file: forced expiratory volume in 1 second 2.2 L (63% of predicted) with a reduced ratio of "
                   "0.61, rising 14% to 2.5 L after albuterol: reversible obstruction.")),
    ],
    plan=[
      ("Albuterol by nebulizer, or by metered-dose inhaler with a valved holding chamber, up to three doses in the "
       "first hour, with ipratropium added for a moderate exacerbation."),
      "An oral systemic corticosteroid (prednisone) now: a short course, no taper needed.",
      "Oxygen only to keep the saturation at 90% or more; at 94% on room air she needs none now.",
      ("Repeat the assessment after the first hour (symptoms, examination, peak flow, saturation): 70% or more of "
       "her best, sustained 60 minutes after the last treatment with no distress, means discharge; 40 to 69% is "
       "an individual decision about admission; under 40%, drowsiness or confusion means the emergency "
       "department and admission."),
      ("Discharge on albuterol as needed and the rest of the prednisone course; restart the daily inhaled "
       "corticosteroid (fluticasone) with a spacer, check her inhaler technique, and give a written asthma action "
       "plan."),
      ("The yearly influenza vaccine (caution with the nasal spray in younger patients) and the pneumococcal "
       "vaccine; follow-up with primary care or an asthma specialist in 1 to 4 weeks."),
    ],
    education=[
      ("Your airways are swollen and squeezed tight, and the cold set it off. Stopping the orange inhaler left the "
       "swelling untreated, so the albuterol has to work harder and wears off sooner."),
      ("Use the orange inhaler every day, even when you feel well: it calms the swelling, and its full effect "
       "builds over weeks to months. Use it with a spacer and rinse your mouth afterward to prevent hoarseness and "
       "thrush."),
      ("Albuterol is your rescue inhaler. Needing it more often than usual means your asthma is out of control, so "
       "call us."),
      ("Check your peak flow every morning and follow your action plan: 352 or more (80% of your best) is green; "
       "220 to 351 is yellow, so add albuterol and call; under 220 (under 50%) is red, so take your rescue "
       "medicine and get help now."),
      ("Call 911 if you have trouble walking or talking because of your breathing, if your lips or fingernails "
       "turn blue, or if the albuterol is not helping."),
    ],
    red_flags=["Trouble walking or talking because of breathlessness",
               "Blue lips or fingernails",
               "Rescue inhaler not helping, or peak flow under 50% of her best",
               "Drowsiness or confusion"],
    follow_up=("Primary care or an asthma specialist in 1 to 4 weeks to review control, inhaler technique and the "
               "action plan; spirometry repeated yearly."),
    presentation=(
      "Ms. Kowalski is a 27-year-old teacher with asthma since childhood, presenting with two days of worsening "
      "breathlessness, wheeze and chest tightness after a cold. She stopped her daily fluticasone in August and "
      "has needed albuterol every three to four hours since yesterday, waking at 3 a.m. two nights running. She "
      "denies fever, chest pain, coughing up blood, leg swelling and travel; she takes an estrogen pill and has "
      "never smoked. Heart rate 108, respiratory rate 24, saturation 94% on room air. She speaks in short "
      "sentences, leaning forward, without accessory muscle use. She has diffuse hyperresonance, diminished "
      "fremitus, decreased excursion and diffuse expiratory wheezes with a prolonged expiratory phase. My "
      "differential is an asthma exacerbation, vocal fold dysfunction, pneumonia and pulmonary embolism. Peak "
      "flow is 55% of her best, a moderate exacerbation; the chest X-ray shows only hyperinflation. Plan: "
      "albuterol with ipratropium, oral prednisone, repeat peak flow, then restart her inhaled steroid with an "
      "action plan."),
    high_yield=[
      dict(item="Ask how often she uses her rescue inhaler and whether she takes a daily controller",
           why=("Albuterol every 3 to 4 hours and no inhaled corticosteroid since August: frequent bronchodilator "
                "use and not taking the inhaled steroid both raise the risk of death, and stopping it is the "
                "commonest reason for poor control.")),
      dict(item="Ask about past attacks: hospital stays, intensive care, a breathing tube, steroid courses",
           why=("A previous near-fatal attack marks the highest risk; hers is one overnight stay at 16 and one "
                "prednisone course in February.")),
      dict(item="Measure the peak flow and compare it with her personal best",
           why=("55% of her best grades a moderate exacerbation (40 to 69%); 70% or more after treatment, "
                "sustained for an hour, allows discharge.")),
      dict(item="Look for accessory muscle use and chest retraction, and say how breathless she is at rest",
           why=("No accessory muscle use or chest retraction, symptoms only mild at rest and a peak flow of 55% "
                "(the 40 to 69% band) make this moderate; severe is symptoms at rest with accessory muscle use, "
                "retraction and a peak flow under 40%.")),
      dict(item="Listen front and back, side to side, and say what a quiet chest would mean",
           why=("Diffuse expiratory wheezes with a prolonged expiratory phase; wheezing fades as the airways close, "
                "so a quiet chest in a breathless patient signals a severe exacerbation.")),
      dict(item="Percuss and palpate fremitus",
           why=("Diffuse hyperresonance, diminished fremitus and reduced excursion are the air trapping of asthma; "
                "focal dullness with increased fremitus would point to pneumonia instead.")),
      dict(item="Ask about triggers and allergies, and look in the nose and at the skin",
           why=("A cold, dust mites, cold air and cats; swollen nasal mucosa and elbow eczema mark allergic "
                "(extrinsic) asthma.")),
      dict(item="Ask about leg swelling, travel, surgery and estrogen, and examine both legs",
           why=("Keeps pulmonary embolism on the differential: she takes an estrogen pill and is tachycardic, so it "
                "is weighed and set aside with the history, soft, equal calves with no swelling, and a negative "
                "D-dimer.")),
    ],
  ),
),

# =====================================================================================================
# PLEURAL EFFUSION (transudate from newly diagnosed heart failure with reduced ejection fraction)
# =====================================================================================================
dict(
  id="pulmonary-pleural-effusion",
  condition="Pleural effusion",
  cites=("CMS L44 Pleural Disorders, slides 5, 17, 82, 84-91, 93, 95-99, 101-102, 107-108, 110-113; CMS L25 "
         "Heart Failure slides 8, 16, 32, 38-40, 53, 56-57; CMS L42 Pulmonary Vascular Disorders slides 23, 35, "
         "43; CMS L33 Oxygen Delivery slide 3; PD2 Thorax slides 10, 15-17, 20, 34-35, 40, 42-44, 47, 53-55, 62"),
  door=dict(
    name="Erik Lindqvist", sex="male", age=67, dob="February 11, 1959",
    setting="Emergency department",
    cc="\"I've been getting more and more winded.\"",
    # CMS L25 slide 39: systolic heart failure with a normal or low blood pressure (his hypertension is treated)
    vitals=[("Blood pressure", "132/80 mmHg"),
            ("Heart rate", "96 beats per minute, regular"),
            ("Respiratory rate", "22 breaths per minute"),
            ("Temperature", "98.2 °F (36.8 °C)"),
            ("Oxygen saturation", "93% on room air"),
            ("Height and weight", "5 feet 11 inches, 198 pounds (body mass index 27.6)")],
  ),
  persona=("A 67-year-old retired mail carrier, gruff, matter-of-fact and slow to complain, who calls himself "
           "'just out of shape'. He sits upright, pauses for breath in long answers, and his wife, who drove him "
           "in after a bad night, is in the waiting room. Anything about his heart makes him go quiet: the heart "
           "attack scared him more than he admits."),
  opening=("I've been getting more winded for a few weeks, and last night I woke up gasping and couldn't catch "
           "my breath for a long time."),
  facts=[
    ("Full name", "Erik Lindqvist."),
    ("Date of birth", "February 11, 1959."),
    ("Onset", "About three weeks ago. I noticed it on my walk with the dog, and it's gotten worse every week "
              "since."),
    ("Location", "It's my breathing mostly, but there's a heaviness low on the right side of my chest. (He "
                 "rests a hand on his right lower ribs.)"),
    ("Duration", "It's there all the time now, a little, and a lot worse when I move around or lie down."),
    ("Character", "Like I can't get a full breath, like the bottom of my right lung is full of something."),
    ("Alleviating factors", "Sitting up and resting. Propping myself up at night."),
    ("Aggravating factors", "Walking, the steps, carrying the groceries, and lying flat."),
    ("Radiation", "No, it doesn't go anywhere."),
    ("Severity", "A five out of ten sitting here. Last night it was an eight. A ten was my heart attack."),
    ("Temporal pattern", "Worse at night when I lie down, and worse each week than the week before. Last night "
                         "was the worst yet."),
    ("Prior episodes", "Never had this before."),
    # CMS L44 slide 85: dyspnea, dry cough, chest pain are the commonest symptoms
    ("Cough", "A dry cough, mostly at night, for about two weeks."),
    ("Sputum", "Nothing comes up."),
    ("Coughing up blood", "No, never."),
    ("Shortness of breath", "When I move and when I lie flat. Sitting up here I'm all right, mostly."),
    ("How far they can walk", "Half a block, then I have to stop. Last summer I walked two miles a day with the "
                              "dog."),
    ("Wheezing", "No."),
    ("Chest pain with breathing", "Not sharp. Just that heaviness on the right when I take a big breath."),
    ("Fever, chills or night sweats", "No."),
    # PD2 Thorax slide 16: left-sided heart failure, weight gain
    ("Weight loss", "No, the opposite. I'm up about nine pounds in three weeks, and I'm not eating any more than "
                    "usual."),
    # CMS L44 slide 86 and CMS L42 slide 23: orthopnea and paroxysmal nocturnal dyspnea point to heart failure
    ("Orthopnea and waking up short of breath", "I'm up to three pillows; I used to sleep on one. I've woken up "
                                                "gasping three times this week, and last night it took a good half "
                                                "hour sitting on the edge of the bed to settle."),
    ("Leg swelling or calf pain", "Both ankles swell by evening, and my socks leave deep marks. No calf pain; "
                                  "both legs are the same."),
    ("Recent travel, immobility or surgery", "No. No trips, no surgery."),
    ("Sick contacts", "Nobody around me has been sick."),
    ("Constitutional", "Tired. No fevers, no night sweats. I've gained weight, not lost it."),
    ("Heart symptoms", "No chest pressure like the heart attack. No racing or skipping, no fainting."),
    ("Ear, nose and throat", "No sore throat, no stuffy nose."),
    ("Heartburn or reflux", "No."),
    ("Anything else", "No, I think that's all of it."),
    ("Chronic conditions", "High blood pressure for about twenty years, high cholesterol, and the heart attack "
                           "eight years ago."),
    ("Known lung disease", "No. Nobody ever told me I had emphysema or asthma."),
    ("Surgeries and procedures", "The stent in my heart eight years ago, and a scope on my right knee."),
    ("Hospitalizations", "Three days for the heart attack."),
    ("Prescription medications", "Aspirin 81 milligrams, atorvastatin 40 milligrams at night, metoprolol "
                                 "succinate 25 milligrams and lisinopril 10 milligrams in the morning, all for "
                                 "years now."),
    ("Taking them as prescribed", "Every day. My wife fills my pill box."),
    ("Over-the-counter medicines and supplements", "Tylenol for my knees now and then, and a fish oil pill."),
    ("Allergies", "Codeine upsets my stomach. No other allergies."),
    # PD2 Thorax slide 16 and CMS L44 slide 84: smoking, cancer history
    ("Tobacco", "A pack a day from eighteen until the heart attack at fifty-nine. I quit cold turkey and haven't "
                "had one since."),
    ("Vaping and marijuana", "No."),
    ("Alcohol", "A couple of beers on a Saturday."),
    ("Recreational drugs", "No."),
    # CMS L44 slide 84: occupational history, asbestos
    ("Occupation and exposures", "Retired mail carrier, thirty-five years walking a route. No asbestos, dust or "
                                 "chemicals that I know of."),
    ("Home and environment", "A house we've had for thirty years. No mold, no birds."),
    ("Living situation", "With my wife, Karin. She drove me here this morning; she's in the waiting room."),
    ("Immunizations", "A flu shot last month, and the pneumonia shot when I turned sixty-five."),
    ("Tuberculosis exposure or testing", "Not that I know of. They tested my skin when I started at the post "
                                         "office, and it was negative."),
    ("Family history, mother", "My mother died of a stroke at seventy-nine."),
    ("Family history, father", "My father had two heart attacks and died at seventy-one with a weak heart."),
    ("Family history, siblings", "A brother, sixty-four, with diabetes, and a sister, seventy, who's healthy."),
    ("What they think it is", "Karin thinks it's pneumonia. I figured I was just getting old and out of shape."),
    ("Concerns", "That it's my heart again. I don't want to go through that again."),
    ("Why he came in today", "Last night was the worst. I woke up gasping and couldn't settle for half an hour, "
                             "and Karin said that was enough and drove me in this morning."),
    # CMS L25 slides 8, 16: ischemic cardiomyopathy after a myocardial infarction
    ("Heart attack and stent", "Eight years ago, crushing pain in the middle of my chest. They put a stent in the "
                               "front artery. They said the heart muscle took a hit."),
    ("Heart follow-up since then", "I saw the heart doctor for a few years, then he retired, and I never found a "
                                   "new one. Nobody's done an ultrasound of my heart in about five years."),
    # CMS L44 slides 82, 84, 111: hepatic disease, cirrhosis, nephrotic syndrome
    ("Liver or kidney problems", "Never had liver or kidney trouble that I know of. My belly isn't swollen, my "
                                 "eyes aren't yellow, and my urine looks normal, not foamy."),
    ("Cancer history", "No cancer. My last colonoscopy was fine."),
    # CMS L44 slide 84: trauma
    ("Injury to the chest", "No falls, no injuries."),
    ("Diet", "A lot of canned soup and deli meat since I retired. I like my salt."),
  ],
  questions=["Is this my heart again?",
             "Is it cancer? I smoked for forty years.",
             "Will that fluid come back?"],
  # PD2 Thorax slide 62 and CMS L44 slides 87-88: asymmetric expansion, decreased fremitus (increased toward the
  # top), dullness, high diaphragm, absent breath sounds with bronchial sounds near the top, transmitted voice
  # sounds decreased to absent over the fluid and increased toward its top; slide 87: effusions under 300 mL give
  # no findings (the small left one), the trachea shifts above 1,000 mL; CMS L42 slide 23 and CMS L25 slide 39:
  # bibasilar crackles and a third heart sound in left systolic heart failure
  exam={
    "position": ("He sits up on the edge of the stretcher with the gown open at the back, and says he could not "
                 "lie flat."),
    "general-survey": ("Alert and oriented, sitting upright, a little short of breath after moving onto the "
                       "stretcher but speaking in full sentences. No audible wheeze. Normal color, no sweating."),
    "breathing-pattern": ("Slightly fast at 22 breaths per minute, regular and a little shallow, with a normal "
                          "expiratory phase."),
    "thorax-inspect": ("Symmetric shape with no deformity, lesions or bruising. The right lower chest moves a "
                       "little less than the left with deep breaths. No retractions."),
    "expansion": "Decreased and delayed on the right: the right thumb moves less than the left.",
    "fremitus": ("Decreased to absent over the right lower back and right lower lateral chest below the tip of "
                 "the scapula, and slightly increased in a band just above that level. Normal and symmetric "
                 "elsewhere and over the whole left side."),
    "percuss-posterior": ("Posterior chest: dull over the right lower back from the tip of the scapula down; "
                          "resonant above that level and over the whole left back."),
    "percuss-lateral": "Lateral chest: dull over the right lower lateral chest; resonant above it and on the left.",
    "diaphragm-excursion": ("Left: about 4 centimeters. Right: the level of dullness is high, at about the tip of "
                            "the scapula, and moves only about 1 centimeter between full expiration and full "
                            "inspiration."),
    "ausc-posterior": ("Posterior chest: breath sounds absent over the right lower back below the tip of the "
                       "scapula, with bronchial breath sounds in a band just above that level; vesicular above. "
                       "A few coarse crackles at the left base that do not clear with a cough. No wheezes or "
                       "rub."),
    "ausc-lateral": ("Lateral chest: breath sounds absent over the right lower lateral chest; vesicular above it "
                     "and on the left. No wheezes or rub."),
    "egophony": ("Over the right back just above the fluid level, \"ee\" sounds like \"ay\" (egophony). Over the "
                 "fluid itself the voice is faint or absent. No egophony on the left."),
    "bronchophony": ("Over the fluid at the right base, \"ninety-nine\" is faint or absent; just above the fluid "
                     "level it is louder and clearer (bronchophony). Muffled and indistinct over the left."),
    "whispered-pectoriloquy": ("Over the fluid at the right base the whisper is not heard; just above the fluid "
                               "level it is louder and clearer (whispered pectoriloquy). Faint and indistinct "
                               "over the left."),
    "heart-ausc": ("Regular rhythm at about 96. Normal first and second heart sounds followed by a soft, "
                   "low-pitched third heart sound at the apex. No murmur or rub."),
    "legs": ("2+ pitting edema over both ankles and up both shins to mid-shin, symmetric, with deep sock marks. "
             "Both calves are soft, nontender and equal in size."),
  },
  special=[],
  must_exam=["fremitus", "percuss-posterior", "diaphragm-excursion", "ausc-posterior", "egophony", "trachea"],
  tests=[
    # CMS L44 slides 90-91: upright film; 75 mL blunts the posterior angle, 175 mL the lateral angle;
    # CMS L42 slides 23, 43: Kerley B lines and effusions in left heart failure
    dict(id="cxr", name="Chest X-ray (upright, frontal and lateral)",
         aka=["CXR", "chest film", "chest radiograph", "chest x ray", "chest x-ray", "chest imaging", "PA and lateral"],
         result=("Moderate right pleural effusion with a meniscus over the lower third of the right chest; "
                 "blunting of the left costophrenic angle (a small left effusion). Kerley B lines at both bases; "
                 "the heart is enlarged. Trachea midline. No consolidation, nodule or mass."),
         here=True),
    # CMS L44 slides 92, 95, 97: free-flowing versus loculated; ultrasound guides thoracentesis
    dict(id="chest-ultrasound", name="Chest ultrasound (pleural)",
         aka=["ultrasound", "chest ultrasound", "pleural ultrasound", "lung ultrasound", "POCUS", "bedside ultrasound",
              "thoracic ultrasound"],
         result=("A moderate, free-flowing, anechoic right pleural effusion, about 6 centimeters deep at the "
                 "base, with no septations or loculations and compressed lung above it; a small free-flowing "
                 "left effusion. A safe site is marked on the right back for thoracentesis."),
         here=True),
    # CMS L44 slides 96, 99, 101, 110, 112: fluid tests and Light's criteria (transudate when none is met)
    dict(id="thoracentesis", name="Thoracentesis with pleural fluid analysis (ultrasound-guided)",
         aka=["thoracentesis", "tap", "pleural tap", "pleural fluid", "pleural fluid analysis", "Light's criteria",
              "diagnostic thoracentesis", "therapeutic thoracentesis", "fluid analysis"],
         result=("Right side, 800 milliliters of clear, straw-colored fluid removed; breathing easier afterward. "
                 "Protein 1.8 g/dL, serum 6.8 (ratio 0.26). Lactate dehydrogenase 72 U/L, serum 190 (ratio "
                 "0.38); two-thirds of the upper limit of normal serum value is 148. No Light's criterion met: a "
                 "transudate. White cells 420 per microliter, mostly macrophages and lymphocytes. Gram stain: no "
                 "organisms. Culture: no growth. Cytology: no malignant cells. Chest X-ray afterward: no "
                 "pneumothorax."),
         here=True),
    # CMS L25 slide 32: metabolic panel (potassium, kidney function) in the heart failure workup
    dict(id="cmp", name="Comprehensive metabolic panel with serum protein and lactate dehydrogenase",
         aka=["CMP", "BMP", "metabolic panel", "chem panel", "chemistry", "electrolytes", "kidney function",
              "liver function", "LFTs", "albumin", "serum protein", "serum LDH", "LDH", "lactate dehydrogenase"],
         result=("Drawn with the tap: total protein 6.8 g/dL, lactate dehydrogenase 190 U/L (upper limit of "
                 "normal 222). Albumin 3.9 g/dL, normal. Sodium 136, potassium 4.2, creatinine 1.1 mg/dL; liver "
                 "tests normal."),
         here=True),
    # CMS L25 slide 38: above 900 likely acute heart failure; CMS L42 slide 43: highly elevated in heart failure
    dict(id="bnp", name="B-type natriuretic peptide (BNP)",
         aka=["BNP", "B-type natriuretic peptide", "brain natriuretic peptide", "natriuretic peptide", "NT-proBNP"],
         result="Highly elevated: about 1,100 picograms per milliliter.",
         here=True),
    # CMS L25 slides 32, 39: the echocardiogram sets the ejection fraction (systolic failure below 40%)
    dict(id="echo", name="Echocardiogram (transthoracic)",
         aka=["echo", "echocardiogram", "TTE", "transthoracic echo", "heart ultrasound", "cardiac ultrasound"],
         result=("Dilated left ventricle with an akinetic anterior wall and apex; ejection fraction about 30%. "
                 "Normal right ventricle; no significant valve disease. Moderate right and small left pleural "
                 "effusions."),
         here=True),
    # CMS L25 slide 32: ischemic changes on the electrocardiogram
    dict(id="ecg", name="Electrocardiogram (12-lead)",
         aka=["EKG", "ECG", "12-lead", "12 lead", "electrocardiogram", "heart tracing"],
         result=("Sinus rhythm at 96. Q waves in V1 to V4 from an old anterior infarction; no acute ST elevation "
                 "or depression."),
         here=True),
    dict(id="cbc", name="Complete blood count (CBC)",
         aka=["CBC", "complete blood count", "blood count", "white count", "hemoglobin", "CBC with diff"],
         result="Normal: white blood cell count 7,400 with a normal differential, hemoglobin 14.1 g/dL, platelets normal.",
         here=True),
  ],
  key=dict(
    diagnosis=("Moderate right pleural effusion with a small left effusion, a transudate by Light's criteria, from "
               "newly diagnosed, decompensated heart failure with a reduced ejection fraction (ischemic "
               "cardiomyopathy after his old heart attack)"),
    must_not_miss=["Infected fluid (a complicated parapneumonic effusion or empyema): fever, sharp pleuritic pain "
                   "or cloudy, purulent fluid needs prompt drainage and antibiotics",
                   "Malignant pleural effusion in a 41 pack-year former smoker: the cytology is checked, and an "
                   "effusion that persists despite treatment of the heart failure is looked at again"],
    ddx=[
      dict(name="Pleural effusion (transudate) from heart failure with reduced ejection fraction",
           support=("Three weeks of worsening exertional breathlessness, now at half a block, three-pillow "
                    "orthopnea, waking up gasping, a nine-pound weight gain and symmetric ankle edema after a "
                    "heart attack eight years ago. A third heart sound and left basal crackles. The right base "
                    "lags, with absent fremitus, dullness, a high, barely moving diaphragm, absent breath sounds "
                    "and voice sounds that return just above the fluid. Kerley B lines, a transudate by Light's "
                    "criteria, a natriuretic peptide above 900 and an ejection fraction of 30%."),
           against=("Nothing on the examination or in the fluid. His effusion is mostly on the right with a small "
                    "left one, which is why the fluid was tapped rather than assumed.")),
      dict(name="Malignant pleural effusion",
           support="A 41 pack-year smoking history with a new effusion and a cough.",
           against=("No weight loss, coughing up blood or night sweats; no mass on the X-ray; the fluid is a "
                    "transudate (cancer gives an exudate) with no malignant cells.")),
      dict(name="Parapneumonic effusion from pneumonia",
           support="A cough with a new effusion.",
           against=("No fever, chills, purulent sputum or sharp pleuritic pain; a normal white count; a transudate "
                    "with a negative Gram stain and culture.")),
      dict(name="Low-albumin transudate (cirrhosis or nephrotic syndrome)",
           support="A transudate with leg swelling.",
           against=("Normal albumin, no liver disease, little alcohol, no belly swelling or foamy urine; "
                    "orthopnea, waking up gasping and a third heart sound point to the heart.")),
    ],
    studies=[
      dict(test="Chest X-ray, upright frontal and lateral",
           why=("Confirms the effusion, its side and size (75 milliliters blunts the posterior angle, 175 the "
                "lateral), and looks for a cause: Kerley B lines, a mass or pneumonia."),
           expect=("Moderate right effusion, small left effusion, Kerley B lines, an enlarged heart; no "
                   "consolidation or mass.")),
      dict(test="Chest ultrasound",
           why=("Has replaced the lateral decubitus film: shows whether the fluid is free-flowing or loculated "
                "and guides the thoracentesis."),
           expect="Free-flowing right effusion about 6 centimeters deep, no loculations; small left effusion."),
      dict(test="Thoracentesis with fluid analysis, plus serum protein and lactate dehydrogenase the same day",
           why=("Tapped because the effusion is new and lopsided and he has no known heart failure, so there is "
                "no established cause yet; it also relieves his breathing. Send protein, lactate dehydrogenase, "
                "white count with differential, Gram stain, cytology and culture. Light's criteria: exudate if "
                "any one of fluid-to-serum protein above 0.5, fluid-to-serum lactate dehydrogenase above 0.6, or "
                "fluid lactate dehydrogenase above two-thirds of the upper limit of normal serum; transudate if "
                "none."),
           expect=("Clear, straw-colored fluid; protein ratio 0.26, lactate dehydrogenase ratio 0.38, fluid "
                   "lactate dehydrogenase 72 (below 148): a transudate. Gram stain, culture and cytology "
                   "negative.")),
      dict(test="B-type natriuretic peptide",
           why=("Below 100 rules out acute heart failure; above 400 makes heart failure likely, and above 900 "
                "acute heart failure."),
           expect="About 1,100: acute heart failure likely."),
      dict(test="Echocardiogram",
           why="Sets the ejection fraction (below 40% is systolic, reduced-ejection-fraction failure) and the cause.",
           expect=("Dilated left ventricle with an akinetic anterior wall; ejection fraction about 30%; normal "
                   "right ventricle and valves.")),
    ],
    plan=[
      ("Ultrasound-guided right thoracentesis, diagnostic and therapeutic: drain enough to ease his breathing, "
       "send the fluid tests with serum protein and lactate dehydrogenase the same day, and take a chest X-ray "
       "afterward for a pneumothorax."),
      ("A transudate is managed by treating the underlying disorder. Admit him: new reduced-ejection-fraction "
       "failure, decompensated (natriuretic peptide above 900, saturation 93%, waking up gasping). Give a loop "
       "diuretic (furosemide or bumetanide) through a vein, and oxygen for his hypoxemia."),
      ("Optimize his reduced-ejection-fraction medicines as he is hemodynamically stable: keep the beta blocker "
       "(metoprolol succinate); replace lisinopril with an angiotensin receptor-neprilysin inhibitor "
       "(sacubitril-valsartan), which is prioritized; add a mineralocorticoid receptor antagonist "
       "(spironolactone or eplerenone) and a sodium-glucose cotransporter 2 inhibitor (dapagliflozin or "
       "empagliflozin)."),
      "Follow potassium and kidney function daily on the diuretic and the new medicines.",
      ("Cardiology: cardiac rehabilitation, and a repeat echocardiogram once his medicines are optimized; an "
       "implantable defibrillator if the ejection fraction stays at 35% or less."),
      ("Repeat chest X-ray once he is diuresed: an effusion that stays or grows despite treatment of the heart "
       "failure needs another look for another cause."),
    ],
    education=[
      ("Your heart muscle is pumping weakly, most likely from the damage your heart attack left, so fluid backs "
       "up into your lungs, your legs and the space around your right lung. That fluid presses on the lung, "
       "which is why you get winded and cannot lie flat."),
      ("The fluid we drained was the thin, watery kind that comes from pressure. The tests on it found no "
       "infection and no cancer cells."),
      ("You will stay in the hospital for a few days while medicine through a vein pulls the extra fluid off, "
       "and we start the heart medicines that help a weak heart work better and help you live longer."),
      ("Once you are home, take every heart medicine every day, weigh yourself every morning, go easy on salt, "
       "and call us if your weight climbs or your ankles swell again."),
      ("Come back at once for breathlessness at rest, waking up gasping again, chest pain like your heart "
       "attack, fainting, or a fever with sharp chest pain."),
    ],
    red_flags=["Breathlessness at rest, or at night that does not settle on sitting up",
               "Fever, chills or sharp chest pain with breathing (possible infected fluid)",
               "Chest pain like his heart attack, or fainting"],
    follow_up=("Admission now for diuresis through a vein and medicine optimization; after discharge, cardiology "
               "follow-up with cardiac rehabilitation, a repeat echocardiogram once his medicines are optimized "
               "(a defibrillator if the ejection fraction stays at 35% or less), and a repeat chest X-ray to "
               "confirm the effusions have cleared."),
    presentation=(
      "Mr. Lindqvist is a 67-year-old man with hypertension, a heart attack with a stent eight years ago and a "
      "41 pack-year former smoking history, presenting with three weeks of worsening exertional breathlessness, "
      "now after half a block. He sleeps on three pillows, woke up gasping last night, and has a dry night "
      "cough, ankle swelling and a nine-pound weight gain. He denies fever, sputum, coughing up blood, night "
      "sweats, liver disease and cancer. Saturation is 93%, respiratory rate 22, blood pressure 132/80. The "
      "right base lags, with absent fremitus, dullness, a high, barely moving diaphragm, absent breath sounds "
      "and egophony above the fluid; the trachea is midline. He has a third heart sound and 2+ ankle edema. My "
      "differential is a heart failure effusion, malignant and parapneumonic effusions, and a low-albumin "
      "transudate. X-ray, ultrasound, thoracentesis, natriuretic peptide and echocardiogram show a transudate "
      "and an ejection fraction of 30%. Diagnosis: transudative effusion from heart failure. Plan: admit, loop "
      "diuretic, optimize heart failure medicines."),
    high_yield=[
      dict(item="Ask about orthopnea, waking up short of breath, leg swelling and weight gain",
           why="Leg swelling, orthopnea and waking up short of breath point to heart failure as the cause of an effusion."),
      dict(item="Ask the effusion history: heart disease, liver disease, cancer, trauma and asbestos",
           why="Each points to a cause; malignant effusions can appear years after a cancer diagnosis."),
      dict(item="Ask about fever, purulent sputum, coughing up blood, night sweats and weight loss",
           why=("Fever, purulent sputum and pleuritic pain suggest pneumonia; coughing up blood suggests "
                "malignancy; night sweats, coughing up blood and weight loss suggest tuberculosis.")),
      dict(item="Percuss the back side to side, then measure diaphragmatic excursion",
           why=("Dullness over the fluid and a high level that barely moves (normal excursion is about 3 to 5.5 "
                "centimeters) mark the effusion and its top.")),
      dict(item="Palpate fremitus and listen over and just above the fluid, with the voice sounds",
           why=("Over fluid, fremitus, breath sounds and voice sounds are decreased or absent; at the top, "
                "bronchial breath sounds and louder voice sounds may appear. Effusions under 300 milliliters "
                "give no findings, which is why the small left one is silent.")),
      dict(item="Check the trachea",
           why="A shift away from the effusion means a large one, over 1,000 milliliters; his is midline."),
      dict(item="Apply Light's criteria out loud",
           why=("Exudate if any one is met: fluid-to-serum protein above 0.5, fluid-to-serum lactate "
                "dehydrogenase above 0.6, or fluid lactate dehydrogenase above two-thirds of the upper limit of "
                "normal serum; transudate if none. Heart failure causes more than 90% of transudates.")),
      dict(item="Listen to the heart and check the legs",
           why=("A third heart sound with a normal or low blood pressure fits systolic failure, and symmetric "
                "pitting edema keeps the heart on a respiratory differential.")),
    ],
  ),
),

# =====================================================================================================
# COMMUNITY-ACQUIRED PNEUMONIA (right upper lobe, nonsevere: outpatient)
# =====================================================================================================
dict(
  id="pulmonary-community-acquired-pneumonia",
  condition="Community-acquired pneumonia",
  cites=("CMS L37 Respiratory Infections, slides 9, 24-25, 27-31, 33, 38, 40-41, 43, 45, 47, 125; PD2 Thorax "
         "slides 8, 14, 17, 20-22, 35, 40, 42, 44-45, 47-48, 52-56, 60"),
  door=dict(
    name="Kwame Mensah", sex="male", age=58, dob="February 19, 1968",
    setting="Urgent care",
    cc="\"I've been running a fever and coughing.\"",
    # Pneumonia Severity Index (slide 30): male 0 + age 58 = 58, nothing else (respiratory rate under 30, systolic
    # 90 or more, temperature under 40 °C, pulse under 125, no listed comorbidity) = class II.
    # CURB-65 (slide 31): no confusion, urea 15, respiratory rate under 30, pressure 134/82, age under 65 = 0.
    vitals=[("Blood pressure", "134/82 mmHg"),
            ("Heart rate", "104 beats per minute, regular"),
            ("Respiratory rate", "24 breaths per minute"),
            ("Temperature", "102.2 °F (39.0 °C)"),
            ("Oxygen saturation", "95% on room air"),
            ("Height and weight", "5 feet 10 inches, 196 pounds (body mass index 28.1)")],
  ),
  persona=("A 58-year-old letter carrier, friendly and stoic, who is not used to being sick and keeps apologizing "
           "for coughing. He takes small, careful breaths, presses a hand to his right chest when he coughs, and "
           "answers in short sentences between breaths. His wife drove him in; he worries more about his "
           "grandson and his route than about himself."),
  opening=("I've been burning up with fever since Tuesday, and this cough won't quit. The right side of my chest "
           "hurts every time I breathe in deep."),
  facts=[
    ("Full name", "Kwame Mensah."),
    ("Date of birth", "February 19, 1968."),
    # PD2 slide 17: pneumonia, acute onset after a recent illness; CMS L37 slide 27: higher fevers and chills
    ("Onset", "Tuesday afternoon, three days ago. I'd had a head cold the week before that was getting better. "
              "Then on my route Tuesday I got the shakes, and by that night I had a fever of 102."),
    ("Location", "Here, high on the right side of my chest, under my collarbone. (Points to the right upper "
                 "chest.)"),
    ("Duration", "The pain stabs with every deep breath or cough, then eases off. The fever and the cough have "
                 "been going nonstop since Tuesday."),
    # CMS L37 slide 27: chest pain described as stabbing or a deep ache
    ("Character", "Sharp, like a knife, when I breathe in deep. In between it's a dull ache."),
    ("Alleviating factors", "Taking small breaths. Hugging a pillow against my side when I cough. Tylenol brings "
                            "the fever down for a few hours."),
    ("Aggravating factors", "Deep breaths, coughing, and the stairs."),
    ("Radiation", "It goes through to the top of my right shoulder blade sometimes. Not into my arm or my jaw."),
    ("Severity", "A six out of ten when I cough or breathe deep. A kidney stone years ago was my ten."),
    ("Temporal pattern", "Worse every day since Tuesday. The fever spikes in the afternoon and evening."),
    ("Prior episodes", "Never. I've never had pneumonia or anything like this."),
    ("Cough", "A little tickle with the cold last week, but since Tuesday it's deep and wet and won't stop."),
    # PD2 slide 22: purulent yellow or green sputum, bacterial pneumonia; no foul smell (abscess)
    ("Sputum", "Thick yellow-green stuff, a spoonful at a time, more in the morning. It doesn't smell bad."),
    ("Coughing up blood", "No, no blood."),
    # CMS L37 slide 27: shortness of breath with tachypnea
    ("Shortness of breath", "When I move around. Sitting here I'm okay, just breathing faster than usual."),
    ("How far they can walk", "From the parking lot to in here I had to slow down. Yesterday I stopped halfway up "
                              "my stairs at home. Normally I walk ten miles a day on my route."),
    ("Wheezing", "No whistling or wheezing."),
    # PD2 slide 14: sharp, worse with inspiration or cough: pneumonia, embolism, pneumothorax, pleuritis
    ("Chest pain with breathing", "Yes, that's the pain in my right chest. Every deep breath and every cough."),
    ("Fever, chills or night sweats", "Fever up to 102.6 last night. Teeth-chattering chills on Tuesday, and I "
                                      "sweat when the fever breaks."),
    ("Weight loss", "No. I haven't been hungry for three days, but my weight's the same."),
    ("Orthopnea and waking up short of breath", "I sleep on one pillow, same as always. The cough wakes me up, but "
                                                "I don't wake up gasping."),
    ("Leg swelling or calf pain", "No swelling, no calf pain."),
    ("Recent travel, immobility or surgery", "No trips, no long car rides, no surgery. I was walking my route until "
                                             "Tuesday."),
    # CMS L37 slide 28: exposure to sick patients
    ("Sick contacts", "My grandson had a cold two weeks ago, and then my wife and I both caught it. Nobody's had "
                      "pneumonia."),
    # CMS L37 slide 27: fatigue, body pain, headache, nausea
    ("Constitutional", "Wiped out. Achy all over, and a headache with the fever. No weight loss, no sweats before "
                       "this week."),
    ("Heart symptoms", "My heart pounds when the fever's up, but no chest pressure, no skipping, no fainting, no "
                       "swelling."),
    ("Ear, nose and throat", "The stuffy nose and scratchy throat from last week are gone. No ear pain."),
    ("Heartburn or reflux", "No heartburn."),
    ("Anything else", "A little queasy, but I haven't thrown up. That's about it."),
    # CMS L37 slide 43: diabetes is an outpatient comorbidity; slide 30: none of the index's listed comorbidities
    ("Chronic conditions", "Type 2 diabetes for about eight years, and high blood pressure for about six. No heart "
                           "trouble, no liver or kidney problems, no cancer, no stroke."),
    ("Known lung disease", "No asthma, no emphysema. My lungs have always been fine."),
    ("Surgeries and procedures", "A scope on my right knee in 2015."),
    ("Hospitalizations", "Never been admitted overnight."),
    ("Prescription medications", "Metformin 1,000 milligrams twice a day, and lisinopril 20 milligrams in the "
                                 "morning."),
    ("Taking them as prescribed", "Every day. My wife fills my pill box."),
    ("Over-the-counter medicines and supplements", "Tylenol, two of the 500s every six hours or so since Tuesday. "
                                                   "The last was about four hours ago. And honey and lemon tea."),
    ("Allergies", "No allergies to any medicines."),
    ("Tobacco", "I smoked a pack a day from eighteen to thirty-eight. I quit twenty years ago, when my daughter "
                "was born."),
    ("Vaping and marijuana", "Neither."),
    ("Alcohol", "A couple of beers watching football on Sundays."),
    ("Recreational drugs", "No."),
    ("Occupation and exposures", "Letter carrier for the post office, twenty-seven years. I walk my route. No dust "
                                 "or chemicals, just dogs."),
    ("Home and environment", "A house we've owned for twenty years. No mold, no birds, no hot tub."),
    ("Living situation", "My wife, Abena. Our daughter and my grandson, he's four, come over most days."),
    # CMS L37 slides 9, 124: all adults 50 or older who never had a pneumococcal conjugate vaccine
    ("Immunizations", "I haven't had my flu shot yet this year; I usually get it at the pharmacy around "
                      "Thanksgiving. I had the COVID shots when they first came out. Never had a pneumonia shot."),
    ("Tuberculosis exposure or testing", "They did a skin test when I got hired at the post office. Negative. I "
                                         "don't know anyone who's had tuberculosis."),
    ("Family history, mother", "My mother had high blood pressure and died of a stroke at 79."),
    ("Family history, father", "My father is 84, with diabetes. He's doing okay."),
    ("Family history, siblings", "My brother is 61, with high blood pressure. My sister is 55 and healthy."),
    ("What they think it is", "I figured bronchitis or the flu that's going around. My wife says pneumonia."),
    ("Concerns", "I don't want to end up in the hospital. And I don't want to give this to my grandson."),
    # CMS L37 slides 27, 31: confusion is a sign of systemic illness and a CURB-65 point
    ("Confusion", "No, my head's clear. My wife says I'm grumpy, not confused."),
    # CMS L37 slide 38: correct dehydration; slide 27: decreased urine output when systemic
    ("Eating, drinking and keeping things down", "Not eating much, but I'm drinking water and ginger ale and "
                                                 "keeping it all down."),
    ("Urination", "Going about as usual, maybe a little darker."),
    ("Blood sugar at home", "Usually in the 120s in the morning. The last two days it's been 190 to 220."),
    # CMS L37 slides 24, 41: Legionella with cruise, hotel or circulating water
    ("Cruise, hotel or hot tub", "No cruises, no hotels, no hot tubs."),
    # CMS L37 slides 41, 81: bird or farm-animal exposure
    ("Birds or farm animals", "No birds, no farm animals. Just the neighbors' dogs on my route."),
    ("Help at home", "My wife is retired and home with me. She drove me here."),
  ],
  questions=["Do I have to go to the hospital?",
             "Is this the flu, or do I need antibiotics?",
             "How long will I have to take the antibiotics?"],
  exam={
    "position": ("He sits on the edge of the exam table with the gown open at the back, leaning a little to the "
                 "right and pressing a hand to his right upper chest when he coughs."),
    # CMS L37 slide 28: appears ill, warm, diaphoretic, increased work of breathing
    "general-survey": ("Ill-appearing man, flushed, warm to the touch and slightly sweaty. Alert and oriented, "
                       "answering clearly. Breathing fast and shallow, holding his right chest when he coughs; "
                       "speaks in short sentences, pausing to breathe and cough. No audible wheeze or stridor. No "
                       "cyanosis."),
    # PD2 slide 35: unilateral lag in movement
    "thorax-inspect": ("The chest is symmetric, with no deformities, lesions or bruising, but the right upper "
                       "chest moves less than the left with each breath. No retractions."),
    "breathing-pattern": ("Fast and shallow at about 24 breaths a minute, regular, cutting each deep breath short "
                          "because of right-sided pain. Normal expiratory phase."),
    # PD2 slide 60: unilateral decrease or delay in chest expansion; slide 40: lobar pneumonia, pleural splinting
    "expansion": ("Asymmetric: the right thumb moves less and lags behind the left when he takes a deep breath, "
                  "and the breath catches with pain on the right."),
    # PD2 slides 40, 60: increased tactile fremitus in unilateral pneumonia
    "fremitus": ("Increased tactile fremitus over the right upper chest, below the clavicle in front and over the "
                 "upper right back. Normal and symmetric over the rest of the chest, including both bases."),
    # PD2 slides 42, 60: dullness over the airless area
    # PD2 slide 8: the right horizontal fissure follows the 4th rib, the lower edge of the upper lobe in front;
    # the oblique fissure starts at about T3 posteriorly
    "percuss-anterior": ("Dull over the right upper anterior chest, from the clavicle down to about the 4th rib. "
                         "Resonant below that and over the whole left side."),
    "percuss-posterior": ("Dull over the upper right back, above the level of the spine of the scapula. Resonant "
                          "below that, at both bases and over the whole left side."),
    # PD2 slide 60: bronchial breath sounds and late inspiratory crackles over the involved area; slide 45: bronchial
    # sounds, expiration as long as or longer than inspiration, loud and high-pitched
    "ausc-anterior": ("Right upper anterior chest, below the clavicle down to about the 4th rib: bronchial breath "
                      "sounds (loud, high-pitched, with expiration longer than inspiration) and late inspiratory "
                      "crackles. Vesicular and clear below that and over the left upper lobe. No wheeze, no pleural "
                      "rub."),
    "ausc-posterior": ("Upper right back: bronchial breath sounds with late inspiratory crackles. Vesicular and "
                       "clear at both bases and over the whole left side. No wheeze, no pleural rub."),
    # PD2 slides 53-56, 60: egophony, bronchophony and whispered pectoriloquy over the involved area
    "egophony": ("Present over the right upper lobe, front and back: \"ee\" is heard as \"ay\". Absent "
                 "elsewhere."),
    "bronchophony": ("Present over the right upper lobe, front and back: \"ninety-nine\" is louder and clearer. "
                     "Muffled and indistinct elsewhere."),
    "whispered-pectoriloquy": ("Present over the right upper lobe, front and back: the whispered words are louder "
                               "and clearer. Faint and indistinct elsewhere."),
    "heart-ausc": ("Fast, regular rhythm at about 104. Normal first and second heart sounds, with no murmur, rub or "
                   "extra heart sound."),
  },
  special=[],
  must_exam=['fremitus', 'percuss-anterior', 'percuss-posterior', 'ausc-anterior', 'ausc-posterior', 'egophony'],
  tests=[
    # CMS L37 slide 29: confirm suspected pneumonia with chest radiography; slide 33: lobar pneumonia signs
    # (homogeneous consolidation, air bronchogram, sharply marginated fissure); PD2 slide 60: trachea midline
    dict(id="cxr", name="Chest X-ray (two views)",
         aka=["CXR", "chest film", "chest radiograph", "chest x ray", "chest x-ray", "chest imaging",
              "PA and lateral"],
         result=("Right upper lobe consolidation: a homogeneous opacity with air bronchograms, sharply bounded "
                 "below by the horizontal fissure. No tracheal deviation. No pleural effusion and no cavity. Heart "
                 "size normal."),
         here=True),
    # slide 29: molecular viral testing can guide antiviral and antibiotic decisions
    dict(id="flu-covid", name="Influenza and COVID-19 rapid molecular test",
         aka=["flu test", "flu swab", "influenza test", "COVID test", "COVID swab", "flu/COVID", "rapid flu",
              "respiratory viral panel", "viral PCR", "SARS-CoV-2 PCR", "multiplex"],
         result="Negative for influenza A, influenza B and SARS-CoV-2.", here=True),
    # slide 29: organ dysfunction; slide 31: urea above 20 mg/dL is a CURB-65 point
    dict(id="bmp", name="Basic metabolic panel",
         aka=["BMP", "CMP", "chem 7", "metabolic panel", "electrolytes", "BUN", "urea", "creatinine",
              "kidney function", "renal function", "glucose", "chemistry"],
         result=("Blood urea nitrogen 15 mg/dL and creatinine 0.9 mg/dL. Sodium 138 and potassium 4.1 mmol/L. "
                 "Glucose 188 mg/dL."),
         here=True),
    # Not on the cited slides (slide 125: routine blood counts do not help every stable outpatient): an expected
    # neutrophil leukocytosis
    dict(id="cbc", name="Complete blood count (CBC) with differential",
         aka=["CBC", "complete blood count", "blood count", "white count", "differential", "CBC with diff"],
         result="White blood cell count 14,800 per microliter, mostly neutrophils. Hemoglobin and platelets normal.",
         here=True),
    # Not on the cited slides: a tracing a student may order for chest pain and a fast rate (sinus tachycardia only)
    dict(id="ecg", name="Electrocardiogram (12-lead)",
         aka=["EKG", "ECG", "12-lead", "12 lead", "electrocardiogram", "heart tracing"],
         result="Sinus tachycardia at 104. Normal intervals and no ST-segment changes.", here=True),
    # slide 29: cultures selectively for severe pneumonia, resistant-pathogen risk or treatment failure
    dict(id="blood-cultures", name="Blood cultures (two sets)",
         aka=["blood cultures", "blood culture", "cultures", "BCx"],
         result="Not available in this urgent care: blood cultures are drawn in the emergency department or hospital.",
         here=False),
    dict(id="sputum-culture", name="Sputum Gram stain and culture",
         aka=["sputum culture", "sputum gram stain", "gram stain", "sputum sample", "phlegm culture"],
         result="Not available in this urgent care: sputum is cultured in a hospital laboratory.", here=False),
    # slide 30: arterial pH below 7.35 is an index item
    dict(id="abg", name="Arterial blood gas (ABG)",
         aka=["ABG", "arterial blood gas", "blood gas", "arterial pH", "VBG"],
         result="Not available in this urgent care: arterial blood gases are drawn in a hospital.", here=False),
  ],
  key=dict(
    diagnosis=("Community-acquired pneumonia of the right upper lobe, nonsevere (Pneumonia Severity Index 58 "
               "points, class II; CURB-65 (confusion, urea, respiratory rate, blood pressure, age 65 or older) "
               "score 0), most likely Streptococcus pneumoniae, in a man with diabetes: "
               "outpatient treatment at home"),
    must_not_miss=["Severe pneumonia or sepsis: low blood pressure, low oxygen, confusion or less urine means the "
                   "emergency department now",
                   "A complication (parapneumonic effusion, empyema or abscess) or another diagnosis if he worsens "
                   "or does not improve on treatment"],
    ddx=[
      dict(name="Community-acquired pneumonia (right upper lobe, nonsevere)",
           support=("Abrupt fever to 102.6 with shaking chills after a cold, a cough with yellow-green sputum, "
                    "sharp right-sided pain on breathing in and breathlessness on stairs; temperature 102.2, heart "
                    "rate 104, respiratory rate 24; over the right upper lobe, increased fremitus, dullness, "
                    "bronchial breath sounds, late inspiratory crackles and egophony, with the right side lagging; "
                    "right upper lobe consolidation on the chest X-ray."),
           against=("Nothing against it. No sign of severe disease: alert, blood pressure 134/82, saturation 95%, "
                    "blood urea nitrogen 15 and no effusion.")),
      dict(name="Acute bronchitis",
           support="A cough with colored sputum after a cold.",
           against=("High fever, fast breathing and focal consolidation on examination and X-ray; bronchitis should "
                    "not have consolidation.")),
      dict(name="Influenza",
           support="November, an abrupt fever with aches, headache and cough.",
           against="Focal consolidation of one lobe, and a negative molecular test."),
      dict(name="Pulmonary embolism",
           support="Pleuritic chest pain, breathlessness and a fast heart rate.",
           against=("Fever with chills and purulent sputum after a cold; no leg swelling, calf pain, travel, "
                    "immobility or surgery; consolidation with crackles and egophony on examination and X-ray.")),
    ],
    studies=[
      dict(test="Chest X-ray",
           why="Confirms suspected pneumonia and shows its extent and any effusion or cavity.",
           expect=("Right upper lobe consolidation with air bronchograms, bounded by the horizontal fissure; "
                   "trachea midline; no effusion or cavity.")),
      dict(test="Basic metabolic panel",
           why=("Looks for organ dysfunction: a blood urea nitrogen above 20 mg/dL is a point on the CURB-65 "
                "(confusion, urea, respiratory rate, blood pressure, age 65 or older) score; also his kidney "
                "function and glucose."),
           expect="Blood urea nitrogen 15, creatinine 0.9, glucose 188."),
      dict(test="Influenza and COVID-19 molecular test",
           why="Molecular viral testing guides antiviral and antibiotic decisions.",
           expect=("Negative; with diabetes he would still need an antibiotic even if it were positive.")),
      dict(test="Blood and sputum cultures",
           why=("Only for severe pneumonia, a resistant-pathogen risk or treatment failure; he has none."),
           expect="Not needed now."),
    ],
    plan=[
      ("Severity: no major criterion for severe pneumonia (no shock needing vasopressors, no need for "
       "ventilation). Pneumonia Severity Index 58 points (male, age 58, nothing else), class II with 0.6% "
       "mortality; CURB-65 (confusion, urea, respiratory rate, blood pressure, age 65 or older) 0, low "
       "severity. With clinical judgment (saturation 95%, alert, drinking, his wife at "
       "home), treat as an outpatient."),
      ("Outpatient regimen for a patient with a comorbidity (diabetes): amoxicillin/clavulanate, cefpodoxime or "
       "cefuroxime plus azithromycin or doxycycline, or a respiratory fluoroquinolone (levofloxacin or "
       "moxifloxacin) alone; review allergies, the QT interval, interactions and fluoroquinolone risks."),
      ("At least 3 days and until clinically stable; a course shorter than 5 days may be enough in nonsevere "
       "pneumonia. No routine corticosteroids and no routine cultures."),
      ("Supportive care: fluids, acetaminophen for fever and pain, rest, and closer blood sugar checks while he is "
       "sick."),
      ("Vaccines once he has recovered from this illness: one dose of 20- or 21-valent pneumococcal conjugate "
       "vaccine (all adults 50 or older who never had one), the annual influenza vaccine and the updated COVID-19 "
       "vaccine."),
      ("Close follow-up (for example a recheck in 2 to 3 days) with return precautions: emergency department for "
       "breathlessness at rest, confusion, fainting, less urine or not keeping fluids or pills down."),
    ],
    education=[
      ("You have pneumonia, an infection in the upper part of your right lung. The X-ray shows it, and it matches "
       "what I hear with the stethoscope."),
      ("Your severity scores are low, so you can be treated at home with antibiotic pills. Take every dose, even "
       "once you feel better."),
      ("Drink plenty, rest, use acetaminophen for the fever and the side pain, and check your sugar more often "
       "while you're sick, because infection pushes it up."),
      ("Once you're over this, get the pneumonia shot and this year's flu and COVID shots: they protect against "
       "severe illness."),
      ("We'll check on you closely, for example in 2 to 3 days. Come back sooner or go to the emergency "
       "department if your breathing gets harder, you get confused, you can't keep fluids or pills down, or you "
       "are not improving or get better and then worse."),
    ],
    red_flags=["Breathlessness at rest or a falling oxygen level", "Confusion, fainting or less urine",
               "Unable to keep fluids or the antibiotic down",
               "Not improving, or better and then worse"],
    follow_up=("Close follow-up with return precautions, for example a recheck in 2 to 3 days by phone or in "
               "clinic, to confirm he is improving and taking the antibiotics; if he worsens, reassess the "
               "diagnosis, adherence and resistance and look for an effusion, empyema or abscess."),
    presentation=(
      "Mr. Mensah is a 58-year-old letter carrier with type 2 diabetes, hypertension and a 20 pack-year former "
      "smoking history, presenting with three days of fever to 102.6, shaking chills, a cough with yellow-green "
      "sputum and sharp right-sided pain on deep breaths, after a cold from his grandson. He is winded on stairs. "
      "He denies coughing up blood, leg swelling, travel, orthopnea and confusion. "
      "Temperature 102.2, heart rate 104, respiratory rate 24, blood pressure 134/82, saturation 95% on room air. "
      "He looks ill and splints his right side. Over the right upper lobe, front and back, fremitus is increased "
      "and percussion is dull, with bronchial breath sounds, late inspiratory crackles and egophony. My "
      "differential is community-acquired pneumonia, bronchitis, influenza and pulmonary embolism. I would order a "
      "chest X-ray, metabolic panel and influenza and COVID-19 test. Pneumonia Severity Index 58, class II; "
      "CURB-65 (confusion, urea, respiratory rate, blood pressure, age 65 or older) zero. Working diagnosis: "
      "nonsevere right upper lobe pneumonia, treated at home with amoxicillin/clavulanate plus azithromycin."),
    high_yield=[
      dict(item="Ask whether the chest pain is worse with a deep breath or a cough",
           why=("Sharp pain on breathing in points to pneumonia, embolism, pneumothorax or pleuritis rather than "
                "angina.")),
      dict(item="Ask the color of the sputum and whether there is blood",
           why="Purulent yellow-green sputum fits bacterial pneumonia; foul-smelling sputum would suggest an abscess."),
      dict(item="Ask about leg swelling, calf pain, travel, immobility, surgery and orthopnea",
           why="Keeps pulmonary embolism and heart failure on the differential of breathlessness with chest pain."),
      dict(item="Ask the chronic conditions and check his mental status",
           why=("They feed the severity scores (confusion, the index's comorbidities) and the antibiotic choice: "
                "diabetes moves him to the comorbidity regimen.")),
      dict(item="Palpate expansion and tactile fremitus, side to side",
           why="A lagging right side with increased fremitus over the right upper lobe means consolidation."),
      dict(item="Percuss and listen over the upper lobes front and back, then test egophony, bronchophony and "
                "whispered pectoriloquy",
           why=("Dullness, bronchial breath sounds, late inspiratory crackles and positive voice sounds over one "
                "lobe; with fever and cough, bronchial breath sounds and egophony more than triple the likelihood "
                "of pneumonia.")),
      dict(item="Interpret the vital signs and score the severity out loud",
           why=("Pneumonia Severity Index 58 (class II, 0.6% mortality), CURB-65 (confusion, urea, respiratory "
                "rate, blood pressure, age 65 or older) 0, saturation 95%: nonsevere, "
                "suitable for treatment at home with clinical judgment.")),
      dict(item="Choose the outpatient regimen for a patient with comorbidities",
           why=("Diabetes calls for a beta-lactam plus azithromycin or doxycycline, or a respiratory "
                "fluoroquinolone, not amoxicillin alone.")),
    ],
  ),
),

# =====================================================================================================
# PULMONARY TUBERCULOSIS (both upper lobes, worse on the right, possible cavity; work exposure; diabetes, smoking)
# =====================================================================================================
dict(
  id="pulmonary-pulmonary-tuberculosis",
  condition="Pulmonary tuberculosis",
  cites=("CMS L38 Mycobacterial Infections including Tuberculosis, slides 4-5, 8, 12-29, 31, 33-34, 36, 41; PD2 Thorax "
         "slides 12, 20-24, 26, 33, 40, 42, 44-45, 52-56"),
  door=dict(
    name="Diane Novak", sex="female", age=52, dob="August 23, 1974",
    setting="Outpatient primary care clinic",
    cc="\"I've had a cough for a couple of months.\"",
    vitals=[("Blood pressure", "118/72 mmHg"),
            ("Heart rate", "96 beats per minute, regular"),
            ("Respiratory rate", "18 breaths per minute"),
            ("Temperature", "100.4 °F (38.0 °C)"),
            ("Oxygen saturation", "96% on room air"),
            ("Height and weight", "5 feet 5 inches, 128 pounds (body mass index 21.3)")],
  ),
  persona=("A 52-year-old county jail corrections officer, direct and no-nonsense, who plays her symptoms down "
           "('it's just a smoker's cough') and gets a little defensive about smoking. She coughs into a tissue "
           "every minute or two. The blood in her phlegm frightened her, and she is quietly terrified that it is "
           "cancer, or that she has passed something to her grandchildren."),
  opening=("This cough just won't go away. It's been about two months, and now I'm sweating through my sheets at "
           "night."),
  facts=[
    ("Full name", "Diane Novak."),
    ("Date of birth", "August 23, 1974."),
    # CMS L38 slide 16: persistent cough
    ("Onset", "Right after Labor Day, so about two months. I thought it was a cold that hung on."),
    ("Location", "In my chest. If I had to pick, the upper right, up under my collarbone."),
    ("Duration", "Every day for two months. All day, worse in the morning."),
    ("Character", "A deep, rattly cough. Some mornings I can't stop until I bring something up."),
    ("Alleviating factors", "A hot shower loosens it. Cough drops don't do a thing."),
    ("Aggravating factors", "Mornings, talking a lot at work, and my cigarettes."),
    ("Radiation", "No, there's no pain going anywhere."),
    ("Severity", "The cough itself maybe a five. It's the sweats and being so tired that are wearing me down."),
    ("Temporal pattern", "Slowly getting worse, not better. I feel feverish in the evenings and sweat at night."),
    ("Prior episodes", "Never had a cough like this. I get one cold a year, and it's gone in a week."),
    # slide 16: persistent cough, with or without sputum
    ("Cough", "Yes, every day for two months. Dry at first, wet the last few weeks."),
    ("Sputum", "Yellowish phlegm, mostly in the morning, a spoonful or two. It doesn't smell."),
    # slide 16: hemoptysis may occur; dramatic hemoptysis is not required; PD2 slide 24: pulmonary tuberculosis
    ("Coughing up blood", "Twice this week there were streaks of blood in it, like little red threads. Not a lot. "
                          "That's what scared me into coming."),
    ("Shortness of breath", "A bit winded on the stairs at work lately. Sitting, I'm fine."),
    ("How far they can walk", "I can do my rounds at work, just slower, and the two flights of stairs wind me now."),
    ("Wheezing", "No wheezing."),
    ("Chest pain with breathing", "No sharp pain when I breathe. My chest is a little sore from coughing."),
    # slide 16: fever and night sweats
    ("Fever, chills or night sweats", "I feel feverish in the evenings; I've seen 100.6 a couple of times. And "
                                      "night sweats, bad ones. I've had to change my T-shirt and the sheets."),
    # slide 16: weight loss, reduced appetite and fatigue
    ("Weight loss", "About fourteen pounds since the summer. I was 142, and this morning I was 128, and I haven't "
                    "been trying."),
    ("Orthopnea and waking up short of breath", "No, I sleep flat on one pillow. The sweats wake me, not my "
                                                "breathing."),
    ("Leg swelling or calf pain", "No."),
    # slide 14: travel to or residence in high-incidence areas (none)
    ("Recent travel, immobility or surgery", "No travel, no surgery. I've never been out of the country."),
    ("Sick contacts", "Nobody at home is sick. At work, people cough all the time. It's a jail."),
    ("Constitutional", "Tired all the time, no appetite, the sweats and the weight loss."),
    ("Heart symptoms", "No chest pressure, no racing heart, no swelling."),
    ("Ear, nose and throat", "No sore throat, no stuffy nose. My voice is fine."),
    ("Heartburn or reflux", "No heartburn."),
    # slide 8: lymph nodes, persistent and often painless enlargement
    ("Anything else", "Just a little lump I noticed on the right side of my neck a few weeks ago. It doesn't hurt."),
    # slide 15: diabetes mellitus raises the risk of progression
    ("Chronic conditions", "Type 2 diabetes for about six years, and high cholesterol. That's it."),
    ("Known lung disease", "No asthma, no emphysema. Nobody's ever told me anything about my lungs."),
    ("Surgeries and procedures", "My gallbladder out about ten years ago."),
    ("Hospitalizations", "Just for the gallbladder."),
    ("Prescription medications", "Metformin 1,000 milligrams twice a day, and atorvastatin 20 milligrams at night."),
    ("Taking them as prescribed", "Mostly. I forget the evening metformin sometimes, with my shifts."),
    ("Over-the-counter medicines and supplements", "Ibuprofen when I feel feverish, and cough drops. No "
                                                   "supplements."),
    ("Allergies", "No allergies."),
    # slide 15: tobacco use
    ("Tobacco", "About a pack a day since I was twenty-two, so thirty years. I know, I know."),
    ("Vaping and marijuana", "No vaping, no marijuana."),
    ("Alcohol", "A glass or two of wine on the weekend."),
    ("Recreational drugs", "Never."),
    # slide 14: prolonged exposure in enclosed, poorly ventilated spaces; work in settings with ongoing transmission
    ("Occupation and exposures", "I'm a corrections officer at the county jail, sixteen years. Twelve-hour shifts "
                                 "inside, and the air in those units is stale. The ventilation is terrible."),
    ("Home and environment", "A house in town with my husband. I smoke out on the back step. No mold, no birds."),
    # slide 23: young children who are contacts need prompt public-health assessment
    ("Living situation", "My husband, Mark. Our son and his two kids, they're three and six, come every Sunday, "
                         "and the kids sleep over some weekends."),
    ("Immunizations", "Flu shot every October at work; I got it this year. The COVID shots when they came out. I "
                      "never had that tuberculosis vaccine they give in other countries; I was born here in Ohio."),
    # slides 14-15, 23: close contact; recent infection within 2 years; early infection can give a negative skin
    # test, repeat 8-10 weeks after the last exposure
    ("Tuberculosis exposure or testing", "Yes. In August of last year an inmate on my unit coughed for weeks "
                                         "before they took him to the hospital, and it turned out he had "
                                         "tuberculosis. Employee health skin-tested all of us, and mine was "
                                         "negative. They told me to come back in two months for a second one, and "
                                         "I never went."),
    ("Family history, mother", "My mother is 78. She had breast cancer at 65 and did fine."),
    ("Family history, father", "My father had a heart attack and died at 66. He smoked."),
    ("Family history, siblings", "My sister is 49 and has diabetes like me."),
    ("What they think it is", "I told myself it was a smoker's cough and I was run down. But the blood, and the "
                              "sweats..."),
    ("Concerns", "That it's cancer. Or that it's the tuberculosis from work and I've given it to my grandkids. They "
                 "were here Sunday."),
    ("Appetite", "I'm just not hungry. Half a sandwich and I'm done."),
    ("Neck lump", "About the size of a marble, on the right side toward the back of my neck. It doesn't hurt, it "
                  "isn't red, and it hasn't gone away."),
    ("Blood sugars at home", "Running high, in the 200s. My last three-month sugar test was almost 9."),
    # slide 8: central nervous system and spine involvement (none)
    ("Headache, stiff neck or back pain", "No headaches, no stiff neck, no back pain."),
    # slide 29: prior films and scarring
    ("Prior chest X-ray", "I had one when I was hired, sixteen years ago. They said it was fine."),
    # slide 15: tumor necrosis factor inhibitors, transplantation or prolonged corticosteroids (none)
    ("Medicines that lower immunity", "No steroids, no injections for arthritis, nothing like that. No transplant."),
    # slide 26: offer human immunodeficiency virus testing when the status is unknown
    ("Human immunodeficiency virus testing", "I've never been tested for human immunodeficiency virus. I've been "
                                             "with Mark thirty years, and I've never used needles."),
  ],
  questions=["Is this tuberculosis? Did I catch it at work?",
             "Could I have given it to my grandkids?",
             "How long do I have to stay away from everyone?"],
  exam={
    # CMS L38 slide 17: fever and wasting may provide clues
    "general-survey": ("Thin, tired-looking woman whose clothes hang loosely. Alert, in no respiratory distress, "
                       "speaking in full sentences; she coughs every minute or two into a tissue. No audible wheeze. "
                       "Normal color."),
    # slide 28: post-primary disease often involves the upper lobes; PD2 slide 42: dullness over consolidated tissue
    "percuss-anterior": ("Dull below the right clavicle, over the right upper lobe. Resonant over the left upper "
                         "lobe and the rest of the anterior chest."),
    "percuss-posterior": ("Dull at the right apex, above the spine of the scapula. Resonant below it and over the "
                          "whole left side."),
    # PD2 slide 40: asymmetric increased fremitus over consolidated lung
    "fremitus": ("Increased tactile fremitus over the right upper chest, below the clavicle in front and at the "
                 "apex behind. Normal and symmetric elsewhere."),
    # CMS L38 slide 17: crackles or bronchial breath sounds; PD2 slide 44: bronchial sounds in unexpected places
    "ausc-anterior": ("Below the right clavicle: bronchial breath sounds with scattered crackles. Below the left "
                      "clavicle: vesicular breath sounds with a few crackles. Bronchovesicular near the "
                      "sternum; clear lower down. No wheeze, no pleural rub."),
    "ausc-posterior": ("Right apex, above the scapula: bronchial breath sounds with a few crackles. Left apex: a few "
                       "crackles over vesicular breath sounds. Vesicular and clear below the apices on both sides."),
    # PD2 slides 52-56: transmitted voice sounds over consolidated lung
    "egophony": "Present over the right upper lobe, front and back: \"ee\" is heard as \"ay\". Absent elsewhere.",
    "bronchophony": ("Present over the right upper lobe, front and back: \"ninety-nine\" is louder and clearer. "
                     "Muffled and indistinct elsewhere."),
    "whispered-pectoriloquy": ("Present over the right upper lobe, front and back: the whispered words are louder "
                               "and clearer. Faint and indistinct elsewhere."),
    # CMS L38 slides 8, 17: lymphadenopathy, persistent and often painless
    "lymph-nodes": ("One firm, nontender, mobile lymph node about 1.5 centimeters across in the right posterior "
                    "cervical chain. No supraclavicular nodes, and none on the left."),
  },
  special=[],
  must_exam=['ausc-anterior', 'ausc-posterior', 'percuss-anterior', 'fremitus', 'lymph-nodes'],
  tests=[
    # CMS L38 slides 27-28, 31: infiltrates and cavities; post-primary disease favors the upper lobes and may
    # cavitate; bilateral abnormalities with possible cavitation; CMS L37 slide 54: an abscess has an air-fluid level
    dict(id="cxr", name="Chest X-ray (two views)",
         aka=["CXR", "chest film", "chest radiograph", "chest x ray", "chest x-ray", "chest imaging",
              "PA and lateral"],
         result=("Patchy infiltrates in both upper lobes, worse on the right, with a possible cavity in the right "
                 "upper lobe and no air-fluid level. No pleural effusion and no enlarged hilar nodes. The lower "
                 "lungs are clear; heart size normal."),
         here=True),
    # slide 26: 3 specimens 8-24 hours apart, one early-morning; smear and mycobacterial culture; slide 4: culture
    # takes weeks
    dict(id="sputum-afb", name="Sputum acid-fast bacilli (AFB) smear and mycobacterial culture, three specimens",
         aka=["AFB", "AFB smear", "sputum AFB", "acid-fast smear", "acid fast bacilli", "sputum culture",
              "mycobacterial culture", "TB culture", "sputum for TB", "three sputums", "sputum smear",
              "AFB culture"],
         result=("Three specimens 8 to 24 hours apart, one early-morning: acid-fast bacilli seen on all three "
                 "smears. Mycobacterial culture pending: it takes weeks."),
         here=True),
    # slide 26: a rapid molecular test on at least one specimen; molecular drug-susceptibility testing;
    # slide 36: rifampin resistance
    dict(id="sputum-naat", name="Nucleic acid amplification test on sputum (NAAT)",
         aka=["NAAT", "PCR", "TB PCR", "GeneXpert", "Xpert", "molecular test", "rapid molecular test",
              "nucleic acid amplification test", "MTB/RIF"],
         result=("Mycobacterium tuberculosis complex detected. Molecular drug-susceptibility testing: no rifampin "
                 "resistance detected."),
         here=True),
    # slides 24-25: a positive result indicates infection and requires evaluation for disease
    dict(id="igra", name="Interferon-gamma release assay (IGRA)",
         aka=["IGRA", "QuantiFERON", "QuantiFERON-TB Gold Plus", "Quantiferon", "T-SPOT", "T-SPOT.TB",
              "interferon gamma release assay", "TB blood test", "gold test"],
         result="Positive.", here=True),
    # slides 20, 22, 41: transverse induration in millimeters read at 48-72 hours; 5 mm or more is positive for a
    # recent close contact; 10 mm for high-risk congregate settings or selected medical risks
    dict(id="tst", name="Tuberculin skin test (TST)",
         aka=["TST", "PPD", "Mantoux", "tuberculin skin test", "TB skin test", "skin test"],
         result=("17 millimeters of transverse induration, read at 48 hours: positive. Her cut-off is 5 "
                 "millimeters as a recent close contact (10 for her congregate workplace or diabetes); 17 exceeds "
                 "both."),
         here=True),
    # slide 26: offer human immunodeficiency virus testing when the status is unknown
    dict(id="hiv", name="Human immunodeficiency virus (HIV) test",
         aka=["HIV", "HIV test", "HIV screen", "HIV antigen antibody", "fourth-generation HIV test"],
         result="Negative.", here=True),
    # slide 36: monitor liver injury (a normal baseline)
    dict(id="liver-panel", name="Liver function tests (baseline)",
         aka=["LFTs", "liver function tests", "liver panel", "hepatic function panel", "AST", "ALT",
              "liver enzymes", "CMP", "comprehensive metabolic panel"],
         result="Liver enzymes and bilirubin normal.", here=True),
    # slide 27: computed tomography can clarify findings or complications
    dict(id="ct-chest", name="Chest computed tomography (CT)",
         aka=["CT", "CT chest", "chest CT", "CAT scan", "computed tomography"],
         result=("Patchy consolidation and nodules in both upper lobes, worse on the right, with a thick-walled "
                 "cavity about 3 centimeters across in the right upper lobe and no air-fluid level. No pleural "
                 "effusion and no enlarged mediastinal nodes."),
         here=True),
  ],
  key=dict(
    diagnosis=("Active pulmonary tuberculosis of both upper lobes, worse on the right with a cavity, presumed "
               "infectious "
               "(acid-fast smears positive, Mycobacterium tuberculosis complex on the rapid molecular test, no "
               "rifampin resistance detected), after a work exposure with a missed repeat test, in a woman with "
               "diabetes who smokes: airborne precautions and a report to the tuberculosis program now"),
    must_not_miss=["Transmission: infectious pulmonary tuberculosis needs airborne precautions now, and her young "
                   "grandchildren and other close contacts need prompt public-health assessment",
                   "Lung cancer: a cavity with weight loss and blood-streaked sputum in a 30 pack-year smoker stays "
                   "on the list until tuberculosis is confirmed"],
    ddx=[
      dict(name="Pulmonary tuberculosis (active, both upper lobes, cavitary)",
           support=("Two months of daily cough, now with blood streaks; evening fevers, drenching night sweats, "
                    "fatigue and a 14-pound weight loss; a close contact with an inmate with infectious "
                    "tuberculosis about 15 months ago, a negative first skin test and a missed repeat; years in a "
                    "crowded, poorly ventilated jail; diabetes and smoking raise the risk of progression; dullness, "
                    "increased fremitus, bronchial breath sounds and crackles over the right upper lobe and crackles "
                    "at the left apex; a painless cervical node; infiltrates in both upper lobes with a possible "
                    "cavity."),
           against=("Nothing against it. The skin and blood tests show infection only, and imaging cannot confirm "
                    "it: the sputum smears, culture and rapid molecular test make the diagnosis.")),
      dict(name="Lung cancer",
           support="A 30 pack-year smoker with weight loss, blood-streaked sputum and an upper-lobe cavity.",
           against=("Evening fevers and drenching sweats after a known exposure, patchy disease in both upper "
                    "lobes, no clubbing, and acid-fast bacilli with Mycobacterium tuberculosis complex in the "
                    "sputum.")),
      dict(name="Nontuberculous mycobacterial lung disease",
           support=("Chronic cough, sputum, weight loss and a cavity; an acid-fast smear cannot tell tuberculosis "
                    "from nontuberculous species."),
           against=("No known bronchiectasis or chronic obstructive pulmonary disease, a known tuberculosis "
                    "contact, and the rapid molecular test detects the Mycobacterium tuberculosis complex.")),
      dict(name="Lung abscess",
           support="Fever, a productive cough and a cavity.",
           against=("Two months of gradual illness, no foul-smelling sputum, no aspiration risk, and no air-fluid "
                    "level in the cavity.")),
    ],
    studies=[
      dict(test="Chest X-ray",
           why=("Part of the initial evaluation: infiltrates, cavities, nodules, adenopathy or effusion; "
                "post-primary disease favors the upper lobes and may cavitate. It supports suspicion but cannot "
                "confirm tuberculosis."),
           expect=("Patchy infiltrates in both upper lobes, worse on the right, with a possible right upper lobe "
                   "cavity; no effusion.")),
      dict(test="Three sputum specimens for acid-fast smear and mycobacterial culture",
           why=("Collected 8 to 24 hours apart, at least one early-morning. A positive smear supports mycobacteria "
                "but cannot tell tuberculosis from nontuberculous species; culture takes weeks."),
           expect="Acid-fast bacilli on all three smears; culture pending."),
      dict(test="Rapid molecular test with drug-susceptibility testing",
           why=("On at least one specimen: identifies the Mycobacterium tuberculosis complex quickly and checks "
                "for rifampin resistance; culture-based susceptibility testing follows."),
           expect="Mycobacterium tuberculosis complex detected; no rifampin resistance detected."),
      dict(test="Interferon-gamma release assay (or tuberculin skin test)",
           why=("Shows infection but not latent versus active disease; a negative result would not have excluded "
                "disease in a patient with these symptoms."),
           expect=("Positive; a skin test reads 17 millimeters, positive at her 5-millimeter cut-off as a recent "
                   "close contact.")),
      dict(test="Human immunodeficiency virus test",
           why="Offered whenever the status is unknown in suspected tuberculosis.",
           expect="Negative."),
    ],
    plan=[
      ("Infection control now: a mask on her, fit-tested N95 respirators for staff, an airborne infection "
       "isolation room if the clinic has one; she stays isolated, away from work and visitors, until the "
       "tuberculosis program ends isolation by clinical, laboratory and public-health criteria."),
      ("Notify the local or state tuberculosis program of presumed tuberculosis today; her grandchildren and other "
       "close contacts need prompt public-health assessment."),
      ("Microbiology: three sputum specimens 8 to 24 hours apart (one early-morning) for acid-fast smear and "
       "mycobacterial culture, a rapid molecular test on at least one, molecular and culture-based "
       "drug-susceptibility testing, and a human immunodeficiency virus test; the persistent, painless cervical "
       "node can be extrapulmonary tuberculosis and may need its own specimen."),
      ("Treatment with the program: 2 months of isoniazid, rifampin, pyrazinamide and ethambutol, then 4 months of "
       "isoniazid and rifampin; ethambutol stops once susceptibility to isoniazid and rifampin is established; "
       "daily directly observed therapy, in person or by video."),
      ("Monitoring: at least monthly review of adherence, symptoms and side effects; sputum cultures until they "
       "convert, with the response documented at 2 months; watch for liver injury and drug interactions."),
      "Address her risks for progression: smoking cessation and better control of her diabetes.",
    ],
    education=[
      ("This looks like tuberculosis, a lung infection that spreads through the air when you cough, talk or sing. "
       "It is curable."),
      ("Until the health department says you can't spread it, stay home from work, keep visitors away, "
       "especially your grandkids, and wear a mask around anyone else."),
      ("Treatment is several pills every day for about six months, and a nurse watches you take them, in person "
       "or by video. Taking every dose is what cures it."),
      ("The health department will check your family and other close contacts, and the little ones will be seen "
       "quickly."),
      ("Tell us right away if you cough up more than streaks of blood, get short of breath, get a bad headache or "
       "stiff neck, or your skin or eyes turn yellow on the medicines."),
    ],
    red_flags=["Coughing up more than streaks of blood", "Breathlessness at rest",
               "Headache, stiff neck or confusion", "Signs of liver injury on treatment"],
    follow_up=("Close and long: the tuberculosis program and the clinic see her at least monthly through six months "
               "of directly observed therapy, with sputum cultures until they convert and the response documented at "
               "2 months; isolation ends only when the program clears her."),
    presentation=(
      "Ms. Novak is a 52-year-old corrections officer with type 2 diabetes and a 30 pack-year current smoking "
      "history, presenting with two months of daily cough, blood-streaked twice this week, evening fevers, "
      "drenching night sweats and a 14-pound weight loss. About 15 months ago an inmate on her unit had "
      "tuberculosis; her skin test then was negative and she missed the repeat. She denies travel and "
      "immunosuppressing medicines. Temperature 100.4, heart rate 96, respiratory rate 18, saturation 96% on room "
      "air; she looks thin. Over the right upper lobe, front and back, percussion is dull and fremitus increased, "
      "with bronchial breath sounds and crackles; there are crackles at the left apex and a right cervical node. My "
      "differential is pulmonary tuberculosis, lung cancer, nontuberculous mycobacterial disease and lung abscess. "
      "I would mask her and order a chest X-ray, three sputum specimens for smear, culture and rapid molecular "
      "testing, an interferon-gamma release assay and a human immunodeficiency virus test. Working diagnosis: active "
      "pulmonary tuberculosis; notify the tuberculosis program."),
    high_yield=[
      dict(item="Ask how long the cough has lasted and whether there is blood",
           why=("Two months of daily cough is chronic; blood streaks are enough, since dramatic hemoptysis is not "
                "required for tuberculosis.")),
      dict(item="Ask about fevers, night sweats, weight loss and appetite",
           why="Fever, night sweats and weight loss with fatigue are the systemic picture of pulmonary tuberculosis."),
      dict(item="Take the exposure history: the jail, the inmate with tuberculosis and the repeat test she missed",
           why=("Close contact and enclosed, poorly ventilated workplaces are exposure risks; early infection can "
                "give a negative test, so it is repeated 8 to 10 weeks after the last exposure.")),
      dict(item="Ask the risks for progression: human immunodeficiency virus, immunosuppressing drugs, diabetes, "
                "smoking, alcohol",
           why="Recent infection within 2 years, diabetes and tobacco use all raise her risk of progressing to disease."),
      dict(item="Mask her and wear an N95 as soon as tuberculosis is suspected",
           why="Infectious pulmonary tuberculosis needs immediate airborne precautions."),
      dict(item="Percuss and listen over the upper lobes front and back, and feel for lymph nodes",
           why=("Post-primary disease favors the upper lobes; crackles, bronchial breath sounds and "
                "lymphadenopathy are clues, though a normal examination does not exclude tuberculosis. A "
                "persistent, painless node can be extrapulmonary tuberculosis and may need its own specimen.")),
      dict(item="Order three sputum specimens, not only a skin or blood test",
           why=("The skin and blood tests show infection, not disease; the sputum smears, culture and rapid "
                "molecular test make the diagnosis.")),
      dict(item="Report to the tuberculosis program and ask who lives with or visits her",
           why="Presumed tuberculosis is reported; young children who are contacts need prompt assessment."),
    ],
  ),
),

# =====================================================================================================
# PNEUMOTHORAX (large left primary spontaneous, clinically stable, urgent care)
# =====================================================================================================
dict(
  id="pulmonary-pneumothorax",
  condition="Pneumothorax",
  cites=("CMS L44 Pleural Disorders, slides 9-13, 16-19, 21-23, 25-28, 33, 35, 38-39, 41, 49, 51, 53-55, 58-60, 63-68, 77; "
         "PD2 Thorax slides 14, 17, 22, 34, 40, 42, 44, 50-51, 61"),
  door=dict(
    name="Tyler Whitfield", sex="male", age=27, dob="March 14, 1999",
    setting="Urgent care",
    cc="\"My chest hurts and I can't catch my breath.\"",
    # CMS L44 slide 51: stable = respiratory rate under 24, heart rate 60-120, normal blood pressure, room-air
    # saturation above 90%, whole sentences; slide 22: mild tachycardia
    vitals=[("Blood pressure", "124/76 mmHg"),
            ("Heart rate", "104 beats per minute, regular"),
            ("Respiratory rate", "22 breaths per minute"),
            ("Temperature", "98.4 °F (36.9 °C)"),
            ("Oxygen saturation", "94% on room air"),
            ("Height and weight", "6 feet 3 inches, 158 pounds (body mass index 19.7)")],
  ),
  persona=("A 27-year-old computer support worker, tall and lanky, polite and a little embarrassed to be here, "
           "who keeps saying he 'probably just pulled something'. He sits very still, takes small breaths, keeps "
           "his left arm close to his side, and pauses briefly between sentences when a breath catches. His father's old story "
           "has him quietly worried, and he keeps coming back to a wedding trip he has planned."),
  opening=("I got this sharp pain in the left side of my chest last night, and I still can't take a full "
           "breath."),
  facts=[
    ("Full name", "Tyler Whitfield."),
    ("Date of birth", "March 14, 1999."),
    # CMS L44 slide 21: often occurs at rest; acute dyspnea; ipsilateral acute pleuritic pain
    ("Onset", "Last night around nine. I was just sitting on the couch playing video games, not doing anything, "
              "and all of a sudden I got a sharp, stabbing pain in my left chest and couldn't get a full breath."),
    ("Location", "The left side of my chest, up front and kind of under my arm. (He points to the upper left "
                 "chest.)"),
    ("Duration", "It's been there since last night, about fourteen hours now. It never really goes away; it's "
                 "worse every time I breathe in."),
    ("Character", "Sharp and stabbing, like a knife when I take a deep breath. And my left side feels like it "
                  "won't fill up."),
    ("Alleviating factors", "Taking small breaths and sitting still. Two ibuprofen last night took the edge off a "
                            "little."),
    ("Aggravating factors", "Deep breaths, coughing and moving around. The stairs to my apartment this morning "
                            "wiped me out."),
    ("Radiation", "No, it stays in my left chest."),
    ("Severity", "A seven when it hit, maybe a five or six now. A ten was breaking my wrist snowboarding."),
    ("Temporal pattern", "About the same since last night, not better and not really worse. I slept propped up "
                         "because lying down hurt more."),
    ("Prior episodes", "Never had anything like this."),
    # CMS L44 slide 21: cough less commonly observed
    ("Cough", "A little dry cough once in a while since last night, and it hurts when I do it."),
    ("Sputum", "Nothing comes up."),
    ("Coughing up blood", "No, no blood."),
    ("Shortness of breath", "Yes, I can't get a full breath. Sitting here I'm sort of okay, but walking makes it "
                            "worse."),
    ("How far they can walk", "I had to stop halfway up the one flight of stairs to my apartment this morning. "
                              "Normally I take them two at a time."),
    ("Wheezing", "No."),
    ("Chest pain with breathing", "Yes, that's the main thing. Every deep breath stabs."),
    ("Fever, chills or night sweats", "No."),
    ("Weight loss", "No. I've always been skinny, and my weight hasn't changed."),
    ("Orthopnea and waking up short of breath", "Lying flat hurt, so I propped myself up, but it wasn't my "
                                                "breathing. I never woke up gasping."),
    ("Leg swelling or calf pain", "No, my legs are fine."),
    ("Recent travel, immobility or surgery", "No flights or long drives lately, and no surgery."),
    ("Sick contacts", "Nobody around me has been sick."),
    ("Constitutional", "Before last night I felt totally fine. No fevers, no sweats, no weight change."),
    ("Heart symptoms", "My heart's been beating a little fast since this started, but it's steady. No pressure in "
                       "my chest, no fainting, no swelling."),
    ("Ear, nose and throat", "No sore throat, no stuffy nose."),
    ("Heartburn or reflux", "No."),
    ("Anything else", "No, that's everything."),
    ("Chronic conditions", "None. I'm healthy."),
    ("Known lung disease", "No asthma or anything like that. Nobody's ever told me something was wrong with my "
                           "lungs."),
    ("Surgeries and procedures", "None. My wrist was just a cast."),
    ("Hospitalizations", "Never."),
    ("Prescription medications", "None."),
    ("Taking them as prescribed", "I don't take any regular medicines."),
    ("Over-the-counter medicines and supplements", "Two ibuprofen last night, around ten. Nothing else, no "
                                                   "supplements."),
    ("Allergies", "None that I know of."),
    # CMS L44 slide 19: smoking is a significant risk factor
    ("Tobacco", "About half a pack a day since I was eighteen, so nine years. I keep meaning to quit."),
    ("Vaping and marijuana", "I vaped for a while in college but stopped. No weed."),
    ("Alcohol", "A few beers on the weekend."),
    ("Recreational drugs", "No."),
    ("Occupation and exposures", "I do computer support for an insurance company, at a desk. No dust or "
                                 "chemicals."),
    ("Home and environment", "A second-floor apartment. No mold, no pets."),
    ("Living situation", "I live with my girlfriend, Maya. She's at work; she's the one who told me to come in."),
    ("Immunizations", "I think I'm up to date. I got a flu shot at work last month."),
    ("Tuberculosis exposure or testing", "Never been around it that I know of, and I've never been tested."),
    ("Family history, mother", "My mom's healthy. She takes a pill for her thyroid."),
    # CMS L44 slide 19: family history
    ("Family history, father", "My dad had a collapsed lung when he was in his twenties. They put a tube in his "
                               "chest. He's fine now."),
    ("Family history, siblings", "One younger sister, nineteen. She's healthy."),
    ("What they think it is", "I figured I pulled something. My dad said it sounds like what happened to him."),
    ("Concerns", "That something's really wrong with my lung. And I'm supposed to fly to a friend's wedding in "
                 "three weeks."),
    # CMS L44 slide 61: "Have you had any trauma?"
    ("Injury to the chest", "No. Nobody hit me, I didn't fall, nothing like that."),
    # CMS L44 slide 17: iatrogenic causes
    ("Needles or procedures on the chest", "Never. No needles, no tubes, no scopes, nothing like that."),
    # CMS L44 slide 19: classically tall, thin young males
    ("Body build", "I'm six-three and I've always been skinny. My dad's built the same way."),
    ("Lightheadedness or fainting", "No, I haven't felt faint."),
    ("Exercise", "Pickup basketball on Sundays. I haven't played since this past Sunday, and I felt fine then."),
    # CMS L44 slide 60: delay air travel, avoid scuba diving
    ("Flying or diving plans", "The wedding's in Denver, so I'd fly. I don't scuba dive."),
  ],
  questions=["Is my lung going to be okay?",
             "Do I really have to go to the hospital?",
             "Can I still fly to my friend's wedding in three weeks?"],
  # PD2 Thorax slide 61 and CMS L44 slides 22-23: lag, decreased or absent fremitus, hyperresonance, decreased
  # or absent breath and voice sounds on the affected side; trachea shifts only with tension
  exam={
    "position": ("He sits up on the edge of the exam table with the gown open at the back, holding his left arm "
                 "close to his side."),
    "general-survey": ("Alert, tall and thin, in mild distress from pain, breathing a little fast but speaking in "
                       "full sentences. No audible wheeze or stridor. Normal color, no sweating."),
    "thorax-inspect": ("The chest has no deformity, wound or bruising. The left side moves less than the right "
                       "with each breath (a left-sided lag). No retractions."),
    "breathing-pattern": ("Slightly fast at 22 breaths per minute, regular and shallow; he takes small breaths "
                          "because a deep one hurts. Normal expiratory phase."),
    "chest-wall-palp": ("No tenderness, deformity, masses or crepitus over the posterior, lateral or anterior "
                        "chest wall, and no crackling under the skin of the chest or neck. Pressing on the left "
                        "chest wall does not reproduce his pain."),
    "expansion": "Asymmetric: the left thumb moves less than the right with a deep breath.",
    "fremitus": ("Decreased to absent over the left chest posteriorly, laterally and anteriorly, most of all over "
                 "the upper left chest. Normal on the right."),
    "percuss-posterior": ("Posterior chest: hyperresonant over the whole left back, most over the upper and "
                          "middle part; resonant over the right back."),
    "percuss-lateral": "Lateral chest: hyperresonant on the left; resonant on the right.",
    "percuss-anterior": ("Anterior chest: hyperresonant, almost drum-like (tympanic), over the left upper chest; "
                         "resonant over the right upper lobe."),
    "ausc-posterior": ("Posterior chest: breath sounds markedly diminished over the upper and middle left back and "
                       "distant at the left base; vesicular over the right back. No crackles, wheezes or rub."),
    "ausc-lateral": ("Lateral chest: breath sounds markedly diminished on the left; vesicular on the right. No "
                     "crackles, wheezes or rub."),
    "ausc-anterior": ("Anterior chest: breath sounds nearly absent over the left upper chest; vesicular over the "
                      "right upper lobe. No crackles, wheezes or rub."),
    "bronchophony": ("Voice sounds are decreased over the left chest: \"ninety-nine\" is fainter on the left than "
                     "the right. No bronchophony."),
    "trachea": "The trachea is midline, with no shift to the right. The neck veins are not distended.",
    # PD2 Thorax slide 51 and CMS L44 slide 77: no mediastinal crunch (pneumomediastinum)
    "heart-ausc": ("Regular rhythm, fast at about 104. Normal first and second heart sounds, with no murmur, rub, "
                   "extra heart sound or crunching sound in time with the heartbeat."),
  },
  special=[],
  must_exam=["trachea", "expansion", "fremitus", "percuss-anterior", "ausc-anterior"],
  tests=[
    # CMS L44 slides 26-28: upright film first; visceral pleural line; apex-to-cupola under 3 cm small, 3 or more large
    dict(id="cxr", name="Chest X-ray (upright)",
         aka=["CXR", "chest film", "chest radiograph", "chest x ray", "chest x-ray", "chest imaging", "upright chest x-ray"],
         result=("A thin, sharp visceral pleural line at the left apex, convex toward the chest wall and running "
                 "down the left lateral chest, with no lung markings beyond it. Apex-to-cupola distance 4 "
                 "centimeters: a large pneumothorax. Trachea and mediastinum midline; right lung clear; no "
                 "effusion or rib fracture."),
         here=True),
    dict(id="ecg", name="Electrocardiogram (12-lead)",
         aka=["EKG", "ECG", "12-lead", "12 lead", "electrocardiogram", "heart tracing"],
         result="Sinus tachycardia at 104. Normal axis and intervals; no ST elevation or depression.",
         here=True),
    dict(id="cbc", name="Complete blood count (CBC)",
         aka=["CBC", "complete blood count", "blood count", "white count", "hemoglobin"],
         result="Normal: white blood cell count 7,900, hemoglobin 15.1 g/dL, platelets normal.",
         here=True),
    # CMS L44 slide 33: best for presence, size and location; assesses underlying disease; impractical when time-critical
    dict(id="ct-chest", name="Computed tomography (CT) of the chest",
         aka=["CT", "CT chest", "chest CT", "CAT scan", "computed tomography", "thoracic CT"],
         result="Not available in this urgent care: it is done in a hospital imaging department.",
         here=False),
    # CMS L44 slide 30: bedside tool for rapid diagnosis; does not assess size
    dict(id="chest-ultrasound", name="Point-of-care chest ultrasound",
         aka=["POCUS", "ultrasound", "lung ultrasound", "chest ultrasound", "bedside ultrasound", "lung sliding"],
         result="Not available in this urgent care: there is no bedside ultrasound machine here.",
         here=False),
    # CMS L44 slide 35: often unnecessary
    dict(id="abg", name="Arterial blood gas",
         aka=["ABG", "arterial blood gas", "blood gas", "arterial gas"],
         result="Not available in this urgent care: arterial blood gases are run in a hospital laboratory.",
         here=False),
    dict(id="troponin", name="Troponin",
         aka=["troponin", "trop", "cardiac enzymes", "cardiac markers", "high-sensitivity troponin"],
         result="Not available in this urgent care: it is sent to a hospital laboratory.",
         here=False),
    dict(id="d-dimer", name="D-dimer",
         aka=["D-dimer", "d dimer", "dimer", "clot test"],
         result="Normal: below 500 nanograms per milliliter.",
         here=True),
  ],
  key=dict(
    diagnosis=("Large left primary spontaneous pneumothorax (apex-to-cupola distance 4 centimeters), clinically "
               "stable: it needs a chest tube, which this urgent care cannot place, so he goes to the emergency "
               "department now"),
    must_not_miss=["Tension pneumothorax: a trachea shifting to the right, a falling blood pressure or distended "
                   "neck veins means needle decompression at once, without waiting for an X-ray",
                   "Pulmonary embolism, the other cause of sudden pleuritic pain and breathlessness: it is set aside "
                   "only because the X-ray shows the pleural line that explains everything"],
    ddx=[
      dict(name="Pneumothorax (primary spontaneous, large, left-sided, clinically stable)",
           support=("Sudden sharp left pleuritic pain and breathlessness that began at rest, in a tall, thin "
                    "27-year-old man who smokes and whose father had a collapsed lung. Heart rate 104 and "
                    "saturation 94%. The left side lags, with decreased fremitus, hyperresonance and diminished "
                    "breath and voice sounds, and the upright X-ray shows a visceral pleural line 4 centimeters "
                    "from the apex."),
           against=("Nothing against it. No lung disease, so it is primary; no trauma or procedure; the trachea "
                    "is midline and the blood pressure normal, so it is not under tension.")),
      dict(name="Pulmonary embolism",
           support="Sudden breathlessness with pleuritic chest pain, a heart rate of 104 and a saturation of 94%.",
           against=("No leg swelling, travel, surgery or coughing up blood; hyperresonance with absent fremitus "
                    "is air in the pleural space, and the X-ray shows the pneumothorax.")),
      dict(name="Myocardial infarction",
           support="Sudden chest pain with breathlessness and a fast heart rate in a smoker.",
           against=("He is 27; the pain is sharp, one-sided and worse with each breath rather than pressure with "
                    "exertion, and the electrocardiogram has no ST changes.")),
      dict(name="Costochondritis or chest wall strain",
           support="Sharp, localized chest pain that is worse with movement.",
           against=("Pressing on the chest wall does not reproduce the pain, and the lag, hyperresonance and "
                    "absent breath sounds point inside the chest.")),
    ],
    studies=[
      dict(test="Chest X-ray, upright",
           why=("The initial test: it shows the visceral pleural line (thin, sharp, convex toward the chest wall, "
                "no lung markings beyond it) and sizes the pneumothorax by the apex-to-cupola distance, under 3 "
                "centimeters small and 3 or more large, which sets the treatment."),
           expect=("A left visceral pleural line with no lung markings beyond it; apex-to-cupola distance 4 "
                   "centimeters (large); trachea and mediastinum midline.")),
      dict(test="Electrocardiogram",
           why="Myocardial infarction and pericarditis are on every sudden chest pain differential.",
           expect="Sinus tachycardia at 104; no ST elevation or depression."),
      dict(test="Computed tomography of the chest, later in the hospital",
           why=("The best test for the presence, size and location of the air, and it finds apical blebs or "
                "bullae and any underlying lung disease; impractical when time is critical, so not first."),
           expect="Large left pneumothorax with small blebs at the left apex; no underlying lung disease."),
    ],
    plan=[
      ("Stable by the stability definition (respiratory rate under 24, heart rate between 60 and 120, normal blood "
       "pressure, room-air saturation above 90%, whole sentences), but large (4 centimeters at the apex) with "
       "significant pain and breathlessness: it needs chest tube insertion. Catheter aspiration or a small-bore "
       "catheter is also accepted for a symptomatic primary spontaneous pneumothorax with no contraindication. "
       "This urgent care can do none of them."),
      ("Transfer to the emergency department now by ambulance; until it arrives, oxygen at 100% by non-rebreather "
       "mask (it speeds resorption of the air), pain control, and repeated checks of his vital signs and "
       "trachea."),
      ("In the emergency department: a chest tube at the fourth or fifth intercostal space in the midaxillary "
       "line, a chest X-ray afterward to confirm the lung has re-expanded, chest computed tomography for apical "
       "blebs, and video-assisted thoracoscopic surgery if the air leak persists or the lung will not expand."),
      ("If he turns unstable (falling blood pressure, trachea shifting to the right, distended neck veins), it is "
       "a tension pneumothorax: needle decompression in the left second intercostal space, midclavicular line, "
       "over the third rib, then a chest tube."),
      ("Smoking cessation, with help if he is willing to quit; video-assisted thoracoscopic surgery with "
       "pleurodesis if it ever comes back."),
    ],
    education=[
      ("A small blister on the top of your left lung popped and let air leak into the space around the lung, so "
       "part of the lung has collapsed. You did not cause it; it happens most in tall, thin young men, and "
       "smoking makes it more likely."),
      ("It is too big to wait out. The emergency department will put a small tube between your ribs to let the "
       "air out so the lung can open back up. We cannot do that here, so an ambulance will take you now."),
      ("It comes back in close to half of people within three years, usually on the same side. Quitting smoking "
       "is the biggest thing you can do to lower that risk, and if it does come back, a keyhole operation can "
       "seal the lung so it stops happening."),
      ("No flying until a chest X-ray shows your lung is fully back up, and then wait another 1 to 2 weeks; ask "
       "before you book the wedding flight. Do not scuba dive."),
      ("Call 911 or come straight back if your breathing suddenly gets worse, you feel faint, or the pain gets "
       "much worse."),
    ],
    red_flags=["Breathing that suddenly gets worse",
               "Feeling faint or a falling blood pressure",
               "The trachea shifting to the right or the neck veins swelling (tension pneumothorax)"],
    follow_up=("Emergency: ambulance to the emergency department now for a chest tube; then follow-up chest "
               "X-rays to confirm the lung has fully re-expanded, a surgical evaluation if the air leak lasts more "
               "than 4 days, and surgery to prevent recurrence if it ever comes back."),
    presentation=(
      "Mr. Whitfield is a 27-year-old man who smokes half a pack a day, whose father had a collapsed lung, "
      "presenting with sudden sharp left-sided chest pain and breathlessness that began at rest last night. The "
      "pain stabs with every deep breath and cough, and one flight of stairs now winds him. He denies trauma, "
      "fever, sputum, coughing up blood, leg swelling, travel, prior episodes and fainting. Heart rate is 104, "
      "respiratory rate 22, saturation 94% on room air, blood pressure 124/76: stable. He is tall and thin and "
      "speaks in full sentences. The left chest lags, with decreased fremitus, hyperresonance and diminished "
      "breath and voice sounds; the trachea is midline. My differential is pneumothorax, pulmonary embolism, "
      "myocardial infarction and chest wall pain. The upright chest X-ray shows a large left pneumothorax, 4 "
      "centimeters apex to cupola, and the electrocardiogram sinus tachycardia only. Diagnosis: large left "
      "primary spontaneous pneumothorax. Plan: oxygen, pain control, ambulance to the emergency department for a "
      "chest tube, and smoking cessation."),
    high_yield=[
      dict(item="Ask what he was doing when it started, and about any trauma or chest procedure",
           why=("Primary spontaneous pneumothorax often starts at rest; trauma or a procedure makes it traumatic "
                "or iatrogenic, which changes the treatment.")),
      dict(item="Ask about smoking, body build, family history and prior episodes",
           why=("Tall, thin men aged 20 to 40, smoking (a significant risk factor) and family history; recurrence "
                "is common, and a recurrence goes to surgery.")),
      dict(item="Ask about underlying lung disease",
           why=("Chronic obstructive pulmonary disease or another lung disease makes it secondary: less reserve, "
                "more dangerous, a chest tube and hospital admission.")),
      dict(item="Compare the two sides: expansion, fremitus, percussion and breath and voice sounds",
           why=("Decreased expansion, decreased or absent fremitus, hyperresonance and diminished breath and voice "
                "sounds on one side are the pneumothorax pattern; dullness would mean fluid instead.")),
      dict(item="Check the trachea and neck veins and recheck the blood pressure",
           why=("Tension pneumothorax shifts the trachea away from the collapsed lung, distends the neck veins and "
                "drops the blood pressure: a clinical diagnosis treated by needle decompression at the second "
                "intercostal space, midclavicular line.")),
      dict(item="Apply the stability definition out loud",
           why=("Respiratory rate under 24, heart rate 60 to 120, normal blood pressure, room-air saturation above "
                "90% and whole sentences: he meets all five, so he is stable for transfer.")),
      dict(item="Size it on the upright X-ray and match the treatment to the size and symptoms",
           why=("Small (under 3 centimeters) with few symptoms is observed with oxygen and a repeat film; large "
                "with significant symptoms needs a chest tube, which means the emergency department.")),
      dict(item="Counsel on recurrence, smoking and flying",
           why=("Recurrence approaches 50% within three years; quitting smoking lowers the risk; air travel waits "
                "until an X-ray confirms full re-expansion, then 1 to 2 weeks; no scuba diving.")),
    ],
  ),
),

]


# =========================================================================================== test pictures
# Only the Pulmonary OSCE Disease Chart's vetted pictures (tools/_pd2_pulm_osce_images.py; files in
# Physical Diagnosis 2 Exam 2/pd2-pulm-osce-images/, yellow boxes drawn in), each on a test the case's setting can do.
# A picture that is not the patient's own says so. Credits come from the chart's sources (build_osce_practice.py).
# case id -> test id -> (picture, caption)
TEST_PICTURES = {
    "pulmonary-chronic-obstructive-pulmonary-disease": {
        "spirometry": ("spirometry-obstructive-copd.png",
                       "An example graph, not his own tracing, with the same numbers as his chart: forced expiratory volume in 1"
                       " second (FEV1) 2.0 L of a forced vital capacity (FVC) of 3.9 L, a ratio of 0.51, below 0.70: "
                       "obstruction. Yellow box: the volume-time curve and its ratio."),
        "cxr": ("cxr-copd-hyperinflation.jpg",
                "An example of his pattern, not his own film: overinflated, dark lungs with fewer markings, a saber-"
                "sheath trachea and a flattened, tented diaphragm (yellow boxes; the labels are the film's own). His film"
                " also shows no infiltrate and no pneumothorax."),
    },
    "pulmonary-acute-bronchitis": {
        "cxr": ("cxr-normal.jpg",
                "A normal chest X-ray like hers, not her own film: clear lungs and sharp costophrenic angles. In "
                "uncomplicated bronchitis the film is normal; a consolidation would mean pneumonia instead."),
        "peak-flow": ("peak-flow-meter-and-normal-values.png",
                      "A: the hand-held peak flow meter. B: normal readings by age and height, men above, women below. Her best"
                      " of 430 liters per minute is about 95% of predicted for her age, sex and height: no airflow obstruction."),
    },
    "pulmonary-pulmonary-embolism": {
        "ecg": ("ecg-pulmonary-embolism.jpg",
                "An example, not her own tracing, from a source titled Pulmonary Embolism that lists tachycardia and the "
                "S1Q3T3 pattern but points to no lead. Hers: sinus tachycardia at 110, a deep S wave in lead I, a Q wave "
                "and inverted T wave in lead III. It suggests right ventricular strain, not a proven clot."),
        "ctpa": ("vq-scan-and-ct-angiogram.jpg",
                 "An example, not her own scan. C (boxed): contrast computed tomography with the clot at the arrow in the "
                 "right main pulmonary artery, where hers is. B (boxed): a perfusion scan with less flow to the right "
                 "lung. A: a normal ventilation scan."),
    },
    "pulmonary-lung-cancer": {
        "ct-chest": ("ct-lung-tumor.jpg",
                     "An example, not his own scan: a large cell carcinoma, a thick-walled cavitating mass in the periphery of"
                     " the left lung (yellow box). His is also a thick-walled, cavitating mass with spiculated borders, 4.6 "
                     "centimeters, in the left upper lobe."),
        "pet-ct": ("pet-ct-nodule.jpg",
                   "An example, not his own scan. The four panels are unlabeled, but a round opacity (top right, boxed) sits"
                   " where a bright focus shows in the two lower panels (boxed). High uptake suggests cancer; inflammation "
                   "can take it up too. This one is in the right lung; his mass is in the left upper lobe."),
    },
    "pulmonary-asthma": {
        "spirometry": ("spirometry-normal-vs-asthma.png",
                       "An example graph, not her own tracing: normal (blue, dashed) against asthma (red), with the same numbers"
                       " as her test on file: forced expiratory volume in 1 second (FEV1) 2.2 L against a normal 3.5 L, forced "
                       "vital capacity 3.6 L, ratio 61%. The asthma loop falls away early (yellow boxes)."),
        "peak-flow": ("peak-flow-meter-and-normal-values.png",
                      "A: the hand-held peak flow meter. B: normal readings by age and height, men above, women below. Her own "
                      "best (440 liters per minute) is the number to compare with: 240 before treatment is 55% of it, 330 after"
                      " treatment is 75%."),
    },
    "pulmonary-pleural-effusion": {
        "cxr": ("cxr-pleural-effusion.jpg",
                "An example, not his own film: both costophrenic angles blunted (arrows, yellow boxes), the sign of fluid"
                " in the pleural space on an upright film. His shows a moderate right effusion with a meniscus and a "
                "small left one."),
    },
    "pulmonary-community-acquired-pneumonia": {
        "cxr": ("cxr-right-upper-lobe-consolidation.jpg",
                "An example of right upper lobe consolidation, not his own film: the right upper lobe is uniformly white "
                "and the trachea is not shifted. This film is labeled Klebsiella pneumonia with a bulging fissure (red "
                "line). His consolidation is sharply bounded below by the horizontal fissure."),
    },
    "pulmonary-pulmonary-tuberculosis": {
        "tst": ("tuberculin-skin-test-reading.jpg",
                "An example, not her own arm. A tuberculin skin test is read 48 to 72 hours after the injection: measure "
                "the firm, raised swelling (induration) across the forearm in millimeters, never the redness (ruler "
                "boxed). Hers measured 17 millimeters at 48 hours: positive."),
        "cxr": ("cxr-tuberculosis-bilateral.jpg",
                "An example, not her own film: abnormalities in both upper lungs (arrows, yellow boxes) with possible "
                "cavitation; hers has the same upper-lobe pattern, worse on the right. A film cannot confirm "
                "tuberculosis: the sputum tests do."),
    },
    "pulmonary-pneumothorax": {
        "cxr": ("cxr-pneumothorax.jpg",
                "An example, not his own film. The yellow box holds three small arrows at the left apex, which its source"
                " labels apical subpleural blebs. A pneumothorax shows as a thin visceral pleural line with no lung "
                "markings beyond it; his left one is 4 centimeters from the apex to the top of the chest cavity."),
    },
}
for _c in CASES:
    for _t in _c["tests"]:
        _pic = TEST_PICTURES.get(_c["id"], {}).get(_t["id"])
        if _pic:
            _t["img"], _t["cap"] = _pic



# =========================================================================================== self-check
# Every case answers the same history: the run-sheet's questions (tools/build_pd2_osce.py PULMONARY), in this
# order, then any facts of its own.
REQUIRED_TOPICS = [
    "Full name", "Date of birth",
    "Onset", "Location", "Duration", "Character", "Alleviating factors", "Aggravating factors", "Radiation",
    "Severity", "Temporal pattern", "Prior episodes",
    "Cough", "Sputum", "Coughing up blood", "Shortness of breath", "How far they can walk", "Wheezing",
    "Chest pain with breathing", "Fever, chills or night sweats", "Weight loss",
    "Orthopnea and waking up short of breath", "Leg swelling or calf pain", "Recent travel, immobility or surgery",
    "Sick contacts",
    "Constitutional", "Heart symptoms", "Ear, nose and throat", "Heartburn or reflux", "Anything else",
    "Chronic conditions", "Known lung disease", "Surgeries and procedures", "Hospitalizations",
    "Prescription medications", "Taking them as prescribed", "Over-the-counter medicines and supplements",
    "Allergies",
    "Tobacco", "Vaping and marijuana", "Alcohol", "Recreational drugs", "Occupation and exposures",
    "Home and environment", "Living situation", "Immunizations", "Tuberculosis exposure or testing",
    "Family history, mother", "Family history, father", "Family history, siblings",
    "What they think it is", "Concerns",
]
SETTINGS = ("Outpatient primary care clinic", "Urgent care", "Emergency department")
VITALS = ["Blood pressure", "Heart rate", "Respiratory rate", "Temperature", "Oxygen saturation",
          "Height and weight"]
TESTS_PER_CASE = 8
TODAY = (2026, 11, 6)


def check(cases, whole=True):
    """Assert the schema and the house rules; whole=False checks a draft subset (no count, order or balance)."""
    import datetime
    import re
    from _osce_pulm_catalog import CATALOG
    from _pd2_pulm_osce_images import IMAGES as PULM_IMAGES

    abbrev = re.compile(
        r"\b(COPD|COLD|CAP|PE|TB|AFB|IGRA|TST|PPD|CXR|CTA|CTPA|CT|ABG|VBG|PEFR?|FEV1|FVC|SABA|LABA|LAMA|ICS|DVT|"
        r"VTE|BNP|CBC|BMP|CMP|LDH|NSCLC|SCLC|PET|PFTs?|SpO2|ECG|EKG|ED|ER|ICU|IV|PO|VQ|PERC|RIPE|HIV|MDI|DOT|"
        r"NSAIDs?|SOB|DOE|PND|URI|RSV|PPI|GERD|CHF|HF|MI|ACS|BP|HR|RR|O2|CO2|PaO2|PaCO2|OSA|ILD|IPF|BMI|PCR|"
        r"NAAT|INR|DOACs?|LMWH|tPA|RUL|RML|RLL|LUL|LLL|ICS|AP|TSH|LFTs?|CRP|ESR|SIADH|SVC|NIPPV|BiPAP|CPAP)\b")

    def strings(obj, skip=("cites",)):
        if isinstance(obj, str):
            yield obj
        elif isinstance(obj, dict):
            for k, v in obj.items():
                if k not in skip:
                    yield from strings(v, skip)
        elif isinstance(obj, (list, tuple)):
            for v in obj:
                yield from strings(v, skip)

    def slug(s):
        return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

    today = datetime.date(*TODAY)
    ids = [c["id"] for c in cases]
    assert len(set(ids)) == len(ids), "duplicate ids"
    if whole:
        assert len(cases) == 9, len(cases)
        surnames = [c["door"]["name"].split()[-1] for c in cases]
        assert surnames == sorted(surnames), ("cases are listed by the patient's surname", surnames)
        sexes = [c["door"]["sex"] for c in cases]
        assert sexes.count("female") >= 3 and sexes.count("male") >= 3, sexes
    rows = []
    if whole:
        known = {(c["id"], t["id"]) for c in cases for t in c["tests"]}
        missing = [(cid, tid) for cid, m in TEST_PICTURES.items() for tid in m if (cid, tid) not in known]
        assert not missing, ("a picture for a test no case has", missing)
    for c in cases:
        cond, d, k = c["condition"], c["door"], c["key"]
        where = c["id"]
        assert set(c) == {"id", "condition", "cites", "door", "persona", "opening", "facts", "questions", "exam",
                          "special", "must_exam", "tests", "key"}, (where, "case fields", sorted(c))
        assert c["id"] == "pulmonary-" + slug(cond), where
        assert c["cites"] and "slide" in c["cites"], (where, "cites")
        assert set(d) == {"name", "sex", "age", "dob", "setting", "cc", "vitals"}, (where, "door fields")
        assert d["sex"] in ("male", "female"), where
        assert d["setting"] in SETTINGS, (where, d["setting"])
        assert isinstance(d["age"], int) and 18 <= d["age"] <= 95, where
        born = datetime.datetime.strptime(d["dob"], "%B %d, %Y").date()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        assert age == d["age"], (where, "dob gives", age)
        assert d["cc"].startswith('"') and d["cc"].endswith('"') and len(d["cc"]) < 90, (where, d["cc"])
        assert [v[0] for v in d["vitals"]] == VITALS, where
        assert len(c["opening"]) < 160, (where, len(c["opening"]))
        topics = [f[0] for f in c["facts"]]
        assert len(set(topics)) == len(topics), (where, "duplicate fact topic")
        assert topics[:len(REQUIRED_TOPICS)] == REQUIRED_TOPICS, (
            where, "the run-sheet's history topics first, in order",
            [t for t in REQUIRED_TOPICS if t not in topics] or "order")
        assert 3 <= len(topics) - len(REQUIRED_TOPICS) <= 12, (where, "facts of its own", len(topics))
        assert all(len(f) == 2 and all(isinstance(x, str) and x for x in f) for f in c["facts"]), where
        assert 2 <= len(c["questions"]) <= 3, where
        for mid in c["exam"]:
            assert mid in CATALOG, (where, "unknown maneuver", mid)
        assert 6 <= len(c["exam"]) <= 18, (where, "exam overrides", len(c["exam"]))
        assert len(c["special"]) <= 3, where
        for sp in c["special"]:
            assert len(sp) == 4 and sp[0] not in CATALOG, (where, sp[0])
        known = set(CATALOG) | {sp[0] for sp in c["special"]}
        must = c["must_exam"]
        assert 4 <= len(must) <= 6 and len(set(must)) == len(must), (where, "must_exam")
        assert all(m in known for m in must), (where, "must_exam id not a maneuver", [m for m in must if m not in known])
        tests = c["tests"]
        assert len(tests) == TESTS_PER_CASE, (where, "tests", len(tests))
        tids = [t["id"] for t in tests]
        assert len(set(tids)) == len(tids) and "other" not in tids, (where, "test ids")
        assert not set(tids) & known, (where, "a test id is also a maneuver id", set(tids) & known)
        for t in tests:
            assert set(t) <= {"id", "name", "aka", "result", "here", "img", "cap"}, (where, t["id"], "unknown test field")
            assert re.match(r"^[a-z0-9][a-z0-9-]{1,30}$", t["id"]), (where, t["id"])
            assert isinstance(t["here"], bool) and t["result"].strip(), (where, t["id"])
            assert t.get("aka"), (where, t["id"], "a test needs the words students use for it")
            assert 2 <= len(t["name"]) <= 80, (where, t["id"], "test name over 80 characters", len(t["name"]))
            assert all(isinstance(a, str) and 1 <= len(a) <= 60 for a in t["aka"]), (where, t["id"], "each aka 1-60 characters")
            assert 8 <= len(t["result"]) <= 600, (where, t["id"], "result 8-600 characters", len(t["result"]))
            assert bool(t.get("img")) == bool(t.get("cap")), (where, t["id"], "picture and caption go together")
            if not t["here"]:
                assert t["result"].startswith("Not available") and t["result"].count(".") == 1, (where, t["id"], "one short sentence")
                assert not t.get("img"), (where, t["id"], "a picture for a test the setting can't do")
        pics = [t for t in tests if t.get("img")]
        assert len(pics) <= 2 and all(t["here"] for t in pics), (where, "at most two pictures, on tests done here")
        for t in pics:
            assert t["img"] in PULM_IMAGES, (where, t["id"], "not one of the chart's vetted pictures", t["img"])
            assert 10 <= len(t["cap"]) <= 300, (where, t["id"], "caption 10-300 characters", len(t["cap"]))
        assert 1 <= len(k["must_not_miss"]) <= 2, where
        assert len(k["ddx"]) == 4, where
        assert cond.lower() in k["ddx"][0]["name"].lower(), (where, "own condition not first")
        assert all(set(x) == {"name", "support", "against"} for x in k["ddx"]), where
        assert 3 <= len(k["studies"]) <= 5, where
        assert all(set(x) == {"test", "why", "expect"} for x in k["studies"]), where
        assert 3 <= len(k["plan"]) <= 6, where
        assert 3 <= len(k["education"]) <= 5, where
        assert 2 <= len(k["red_flags"]) <= 4, where
        assert 5 <= len(k["high_yield"]) <= 8, where
        assert all(set(x) == {"item", "why"} for x in k["high_yield"]), where
        assert isinstance(k["follow_up"], str) and k["follow_up"], where
        assert set(k) == {"diagnosis", "must_not_miss", "ddx", "studies", "plan", "education", "red_flags",
                          "follow_up", "presentation", "high_yield"}, (where, "key fields", sorted(k))
        words = len(k["presentation"].split())
        assert 120 <= words <= 170, (where, "presentation words", words)
        for s in strings(c, skip=("cites", "aka")):
            low = s.lower()
            for bad in ("slide", "lecture", "professor", "deck"):
                assert bad not in low, (where, bad, s[:80])
            m = abbrev.search(re.sub(r"\([A-Za-z0-9-]+\)", "", s))   # "Full term (ABBREV)" is the policy's own form
            assert not m, (where, "abbreviation", m.group(0) if m else "", s[:80])
        rows.append("%-50s %-6s %3d  %-30s facts %2d  exam %2d  special %d  tests %d  pictures %d  presentation %3d words"
                    % (c["id"], d["sex"], d["age"], d["setting"], len(c["facts"]), len(c["exam"]),
                       len(c["special"]), len(tests), len(pics), words))
    return rows


if __name__ == "__main__":
    for r in check(CASES):
        print(r)
    print("OK: %d cases" % len(CASES))
