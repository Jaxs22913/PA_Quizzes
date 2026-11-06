# -*- coding: utf-8 -*-
"""Lecture 40 (Obstructive Sleep Apnea and Obesity Hypoventilation Syndrome, Shah) cram topics, condensed from
guide section 2.

CRITERIA: one table per criteria set, score, classification or cut-off on the slides (memory cram_criteria_tables),
each with a labeled memory aid. Cells are the slide wording; slide conflicts are note rows. The apnea-hypopnea index
severity bands are in the speaker notes only and are left out. Doses are left out.
"""
L40C = "#5e4123"

CRITERIA = [
{"id": "crit-l40-apnea", "label": "Apnea, Hypopnea and the Three Apnea Types", "color": L40C,
 "tag": "Definitions &middot; Lecture 40 &middot; slide 3",
 "cols": ["Term", "Airflow", "Respiratory effort"], "widths": ["24%", "38%", "38%"], "rows": [
  ("<b>Apnea</b>", "Decrease of <b>90% or more</b> (thermistor), lasting <b>at least 10 seconds</b>", "&mdash;"),
  ("<b>Hypopnea</b>", "Slowed, shallow, restricted breathing in episodes of <b>10 seconds or longer</b>", "&mdash;"),
  ("<b>Obstructive</b> apnea", "None", "<b>Continued</b>"),
  ("<b>Central</b> apnea", "None", "<b>None</b>"),
  ("<b>Mixed</b> apnea", "None", "Absent early in the event, <b>resumes later</b>"),
 ], "mnemonic": {"hook": "Ninety for Ten; then ask the chest: Obstructive keeps On trying, Central has Ceased, Mixed Makes up its mind late.",
  "key": [["90 / 10", "apnea: airflow down 90% or more for 10 seconds or more"], ["O", "Obstructive: effort ongoing"],
          ["C", "Central: effort ceased"], ["M", "Mixed: effort missing, then made"]],
  "breaks": "Hypopnea has no percentage on the slide, only the 10-second episodes."}},

{"id": "crit-l40-osa-dx", "label": "Obstructive Sleep Apnea: Diagnostic Criteria and Indices", "color": L40C,
 "tag": "Criteria &middot; Lecture 40 &middot; slide 9",
 "cols": ["Item", "What the slide says"], "widths": ["30%", "70%"], "rows": [
  ("Criterion 1", "<b>5 or more</b> predominantly obstructive respiratory events per hour of sleep <b>plus one symptom</b>: sleepiness, fatigue, insomnia or impaired sleep-related quality of life; waking with breath holding, gasping or choking; habitual snoring or breathing interruptions seen by a bed partner"),
  ("Criterion 2", "<b>15 or more</b> predominantly obstructive respiratory events (no symptom needed; the slide gives no time unit here)"),
  ("And", "Symptoms <b>not explained</b> by another medical or sleep condition, medications or substance use"),
  ("Apnea-hypopnea index", "(apneas + hypopneas) &divide; total sleep time in hours"),
  ("Respiratory disturbance index", "(apneas + hypopneas + respiratory effort-related arousals) &divide; total sleep time in hours"),
  {"note": "Mild, moderate and severe index bands appear only in the speaker notes, not on a slide."},
 ], "mnemonic": {"hook": "Five needs a friend; fifteen stands alone.",
  "key": [["5", "5 or more events per hour needs one symptom"], ["15", "15 or more events is enough on its own (no time unit on the slide)"]],
  "breaks": "Both still need the symptoms to be unexplained by another condition, drug or substance."}},

{"id": "crit-l40-stopbang", "label": "STOP-Bang Questionnaire", "color": L40C,
 "tag": "Score &middot; Lecture 40 &middot; slides 16&ndash;17",
 "cols": ["Letter", "Yes if (1 point each)"], "widths": ["20%", "80%"], "rows": [
  ("<b>S</b>noring", "Snores loudly (through closed doors, or the bed partner elbows you)"),
  ("<b>T</b>ired", "Often tired, fatigued or sleepy in the daytime"),
  ("<b>O</b>bserved", "Someone observed you stop breathing, or choking or gasping, during sleep"),
  ("<b>P</b>ressure", "Have, or being treated for, high blood pressure"),
  ("<b>B</b>MI", "Body mass index <b>more than 35</b> kg/m&sup2;"),
  ("<b>A</b>ge", "<b>Older than 50</b>"),
  ("<b>N</b>eck", "Neck (shirt collar) <b>16 inches / 40 cm or larger</b>"),
  ("<b>G</b>ender", "<b>Male</b>"),
  {"group": "RISK (general population)"},
  ("Low", "Yes to <b>0&ndash;2</b>"),
  ("Intermediate", "Yes to <b>3&ndash;4</b>"),
  ("High", "Yes to <b>5&ndash;8</b>, <b>or</b> 2 or more of the 4 STOP questions <b>plus</b> male gender, <b>or plus</b> body mass index over 35, <b>or plus</b> neck 16 inches / 40 cm"),
  {"note": "Not for routine community screening or asymptomatic patients; used preoperatively; the highest sensitivity of the questionnaires (slide 16). The risk-factor neck size on slides 6&ndash;7 is 17 inches (men) / 16 (women)."},
 ], "mnemonic": {"hook": "The name is the mnemonic: STOP (four symptoms) and Bang (four facts).",
  "key": [["S", "Snoring loudly"], ["T", "Tired in the daytime"], ["O", "Observed apneas, choking or gasping"], ["P", "Pressure: high blood pressure"],
          ["B", "BMI over 35"], ["A", "Age over 50"], ["N", "Neck 16 inches / 40 cm or more"], ["G", "Gender male"]],
  "breaks": "Risk bands 0&ndash;2 / 3&ndash;4 / 5&ndash;8 and the 2-STOP-plus rules are not in the name: learn them from the table."}},

{"id": "crit-l40-home-test", "label": "Home Sleep Test or In-Lab Polysomnogram?", "color": L40C,
 "tag": "Criteria &middot; Lecture 40 &middot; slide 8",
 "cols": ["Use a polysomnogram, NOT a home kit, with:"], "rows": [
  ["<b>S</b>troke"],
  ["<b>N</b>euromuscular weakness"],
  ["Long-term <b>o</b>pioid use"],
  ["Significant <b>c</b>ardiopulmonary disease"],
  ["Awake <b>h</b>ypoventilation or hypoxemia"],
  ["Severe <b>i</b>nsomnia"],
  ["Concern for a <b>n</b>on-obstructive sleep disorder"],
  {"note": "Home kits assess only obstructive sleep apnea and will not always diagnose mild disease (helpful for moderate to severe). Central sleep apnea: home testing is not sufficient (slide 26)."},
 ], "mnemonic": {"hook": "A SNOCHIN (a snoring chin) with any of these sleeps in the lab.",
  "key": [["S", "Stroke"], ["N", "Neuromuscular weakness"], ["O", "Opioids, long term"], ["C", "Cardiopulmonary disease"],
          ["H", "Hypoventilation or hypoxemia while awake"], ["I", "Insomnia, severe"], ["N", "Non-obstructive sleep disorder suspected"]],
  "breaks": "Made up here; the slide lists them in a different order."}},

{"id": "crit-l40-ohs", "label": "Obesity Hypoventilation Syndrome: Screen, Diagnose, Treat", "color": L40C,
 "tag": "Criteria &middot; Lecture 40 &middot; slides 31&ndash;33",
 "cols": ["Step", "What the slides say"], "widths": ["26%", "74%"], "rows": [
  {"group": "SCREEN an obese patient (with or without obstructive sleep apnea) who has"},
  ("Oxygen saturation", "Unexplained awake room-air saturation <b>94% or less</b>, or overnight lowest <b>below 80%</b>"),
  ("Symptoms and signs", "Unexplained dyspnea on exertion; pulmonary hypertension or right-sided heart failure (elevated jugular venous pressure, hepatomegaly, pedal edema); <b>facial plethora</b> (facial swelling, puffiness)"),
  ("Labs", "Raised bicarbonate; when suspicion is low to moderate, serum bicarbonate <b>over 27</b> &rarr; arterial blood gas"),
  {"group": "DIAGNOSE by exclusion: all three"},
  ("1", "Obesity: body mass index <b>over 30</b>"),
  ("2", "Awake alveolar hypoventilation: arterial carbon dioxide pressure <b>over 45 mm Hg</b>"),
  ("3", "Alternative causes of hypercapnia and hypoventilation <b>excluded</b>"),
  ("Gold standard", "Polysomnography with <b>continuous nocturnal carbon dioxide monitoring</b>"),
  {"group": "TREAT"},
  ("Approach", "<b>Multidisciplinary</b>"),
  ("First line", "Weight loss program <b>+</b> positive airway pressure: with obstructive sleep apnea &rarr; <b>CPAP</b>; with sleep-related hypoventilation &rarr; <b>BiPAP</b>"),
  ("Lifestyle", "Diet changes, exercise, behavioral modifications"),
  ("Second line", "<b>Tracheostomy with nocturnal ventilation</b> (very effective); bariatric surgery; medications only after diet and exercise fail"),
 ], "mnemonic": {"hook": "Screen at 94-80-27; diagnose at 30-45-zero.",
  "key": [["94", "awake saturation 94% or less"], ["80", "overnight nadir below 80%"], ["27", "bicarbonate over 27 means get a blood gas"],
          ["30", "body mass index over 30"], ["45", "arterial carbon dioxide over 45 mm Hg"], ["zero", "zero other causes (diagnosis of exclusion)"]],
  "breaks": "The screening signs without numbers (dyspnea, right heart failure, facial plethora) and the treatment rows (multidisciplinary, first line, lifestyle, second line) are not in the numbers."}},

{"id": "crit-l40-untreated", "label": "Untreated Obstructive Sleep Apnea: the Numbers", "color": L40C,
 "tag": "Cut-offs &middot; Lecture 40 &middot; slides 18&ndash;20",
 "cols": ["Outcome", "Risk"], "widths": ["62%", "38%"], "rows": [
  ("Driving accidents", "<b>2.5 times</b>"),
  ("Sudden cardiac death <b>AT NIGHT</b>", "<b>3&ndash;6 times</b>"),
  ("Hypertension", "<b>3 times</b>"),
  ("Nonalcoholic fatty liver disease (prevalence)", "<b>2&ndash;3 times</b>"),
  ("Gastroesophageal or laryngopharyngeal reflux", "<b>75&ndash;100%</b> of patients; improves with CPAP"),
 ], "mnemonic": {"hook": "Count up the night: 2.5 crashes, 2 to 3 livers, 3 pressures, 3 to 6 hearts stop, and nearly all reflux.",
  "key": [["2.5", "driving accidents"], ["2&ndash;3", "fatty liver"], ["3", "hypertension"], ["3&ndash;6", "sudden cardiac death at night"], ["75&ndash;100%", "reflux"]],
  "breaks": "Heart failure mortality, pulmonary hypertension, stroke, arrhythmias and ischemic heart disease carry no number on the slides."}},
]

TOPICS = [
{"id": "l40-emph", "label": "★ Emphasized: Sleep Apnea", "color": "#b8860b", "rows": [
  ["★ AT NIGHT", "Capitals on the slide: untreated obstructive sleep apnea carries <b>3&ndash;6 times the risk of sudden cardiac death AT NIGHT</b>."],
  ["★ ** ASV", "Asterisks on the slide: <b>adaptive servo-ventilation is not used for all patients</b>, especially in <b>heart failure with reduced ejection fraction</b>."],
  ["★ Gold standards", "Split-night and all-night polysomnogram (obstructive apnea); polysomnography with continuous carbon dioxide monitoring (obesity hypoventilation)."],
  ["★ Diagnosis, simply", "&ldquo;As simple as possible&rdquo;: <b>5 or more</b> obstructive events per hour <b>plus a symptom</b>, or <b>15 or more</b>. Home kit = obstructive apnea only; not with cardiopulmonary or neuromuscular disease, and not for central apnea."],
  ["★ Education", "&ldquo;Patient education is like the <b>most important thing</b>&rdquo;: CPAP is the most effective but disliked, so counsel. Severe obstructive apnea: <b>oral appliance not effective</b>, use CPAP."],
  ["★ Central apnea risk factors", "&ldquo;I really want everyone to understand&rdquo;: <b>heart failure, stroke, opioids, hypoxia, high altitude, CPAP use</b>. Treat the cause first, then CPAP, then ASV (not with poor left ventricular function)."],
  ["★ OHS", "<b>Diagnosis of exclusion</b>; male gender is not a risk factor; first line <b>weight loss + BiPAP or CPAP</b> (&ldquo;first line, first line, first line&rdquo;)."],
  ["★ Women", "After menopause more than before: &ldquo;the age will help you a lot.&rdquo;"],
]},
{"id": "l40-osa", "label": "Obstructive Sleep Apnea", "color": L40C, "rows": [
  ["Who and why", "Most common sleep-disordered breathing; rises with age; men &gt; women; post- &gt; premenopausal; <b>upper airway narrowing</b> by soft tissue or structure."],
  ["Risk factors", "Obesity; big tongue, small or set-back jaw; neck <b>17 in (men) / 16 in (women)</b>; big tonsils; age; male; family history; <b>alcohol or sedatives</b>; <b>hypothyroidism</b>."],
  ["History", "Daytime sleepiness, unrefreshing sleep, <b>witnessed apnea</b>, snorting or gasping, <b>loud habitual snoring</b>, morning headache, nocturia, <b>poorly controlled hypertension</b>, poor memory, low libido, night sweats."],
  ["Exam", "Obesity, macroglossia, micrognathia, retrognathia, large neck, enlarged tonsils, <b>crowded posterior oropharynx</b>."],
  ["Tests", "Thyroid-stimulating hormone if hypothyroid; <b>split-night</b> (2 hours, then CPAP titration) or <b>all-night</b> polysomnogram (mild to moderate at baseline); titration study if the diagnosis is known."],
  ["Differential", "Central sleep apnea, nocturnal dyspnea (heart failure), swallowing disorder, panic attacks, nocturnal asthma, reflux, nocturnal seizures, narcolepsy, periodic limb movements."],
]},
{"id": "l40-osa-rx", "label": "Treating Obstructive Sleep Apnea", "color": "#2f5d6b", "rows": [
  ["Most effective", "<b>Continuous positive airway pressure (CPAP)</b>."],
  ["Other devices", "Autotitrating PAP <b>only without significant comorbidities</b>; positional therapy if supine-only; <b>oral appliance not for severe disease or no teeth</b>; nasal expiratory resistance device."],
  ["Drugs", "<b>Modafinil or armodafinil</b>: headache, anxiety, dizziness, nausea, hypersensitivity, many interactions; <b>caution with cardiovascular, hepatic, psychiatric disease</b>; <b>lower doses in the elderly</b>. Nasal steroids for allergic congestion."],
  ["Surgery", "Radiofrequency ablation (mild to moderate, CPAP-intolerant); palatal implants (mild); maxillomandibular advancement; <b>tracheostomy is a cure</b>; bariatric surgery may help."],
  ["Lifestyle and referral", "Diet and exercise for weight loss; <b>avoid alcohol and sedatives</b>; <b>refer to a sleep physician</b>; counseling."],
  ["Older adults", "Lower mortality (they compensate) but <b>drowsiness and nocturia</b>, which improve with CPAP."],
]},
{"id": "l40-complications", "label": "Untreated: Complications &amp; Comorbidities", "color": "#7a3b2e", "rows": [
  ["Heart", "Arrhythmias, bradycardia, sympathetic tone up, blood pressure variability; ischemic heart disease; <b>heart failure mortality</b>; aortic aneurysm and dissection."],
  ["Lungs", "<b>Group 3 pulmonary hypertension</b> (especially with obesity hypoventilation or daytime hypoxemia)."],
  ["Metabolic", "<b>Insulin resistance, type 2 diabetes</b> and its complications; glucose and triglycerides up; worse cardiovascular risk in <b>metabolic syndrome</b>; fatty liver 2&ndash;3 times; gout."],
  ["Other", "Stroke; reflux 75&ndash;100%; C-reactive protein, cortisol, amyloid up; growth hormone, prolactin down; cytokines up (improve with CPAP)."],
]},
{"id": "l40-csa", "label": "Central Sleep Apnea", "color": "#4a5a2a", "rows": [
  ["Mechanism", "Brainstem stops signaling: high carbon dioxide sensitivity &rarr; <b>hyperventilation alternating with apnea</b>; <b>no effort</b> (obstructive: effort against a collapsed airway)."],
  ["Risk factors", "<b>Heart failure</b> (Cheyne-Stokes; circulation delay to the carotid chemoreceptors), <b>stroke</b>, <b>opioids</b>, hypoxia, <b>high altitude</b>, CPAP use."],
  ["Presentation", "Insomnia, awakenings, nocturnal dyspnea, nonrestorative sleep, sleepiness; <b>less snoring</b>."],
  ["Diagnosis", "<b>Polysomnography (home not sufficient)</b>: repetitive apneas <b>without thoracic-abdominal excursion</b>."],
  ["Treatment", "<b>Treat the cause</b> (optimize heart failure therapy, reduce opioids, descend) &rarr; <b>CPAP</b> &rarr; adaptive servo-ventilation if CPAP fails, <b>not in reduced ejection fraction</b>."],
]},
{"id": "l40-ohs", "label": "Obesity Hypoventilation Syndrome", "color": "#5a3a5e", "rows": [
  ["Definition", "<b>Awake</b> alveolar hypoventilation (raised awake carbon dioxide) in an obese person, <b>not explained by anything else</b> (Pickwickian syndrome)."],
  ["Risk factors", "Central obesity, reduced lung function, weak inspiratory muscles, <b>severe obstructive sleep apnea</b>; <b>male sex is NOT a risk factor</b>; 50s and 60s."],
  ["Presentation", "<b>90% have obstructive apnea symptoms (70% severe)</b>; 10% sleep hypoventilation (older women, fewer witnessed apneas); many present late with hypercapnic respiratory failure or right heart failure."],
  ["Complications", "Pulmonary hypertension, right-sided heart failure, sleepiness, hypertension, heart failure, insulin resistance; <b>refer to a sleep specialist</b>."],
  ["Prognosis", "<b>High mortality</b>; <b>cardiovascular disease is the leading cause of death</b>; more hospital and intensive care use; worse with significant awake hypoxemia at diagnosis."],
]},
]
