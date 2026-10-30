# -*- coding: utf-8 -*-
"""Lecture 35 (Asthma, Finck) cram topics, condensed from guide section 3.

CRITERIA (2026-10-30, memory cram_criteria_tables): one table per criteria set or cut-off table on the slides,
each with a labeled memory aid; cells are the slide wording (s62, s88 and s89 read from the slide pictures);
slide conflicts are note rows, never resolved. Generic drug names only; the s62 age-normal ratio column and
treatment-step row are left out (out of scope on the recording). The builder puts them at the top.
"""

_C = "#1f5c3a"
CRITERIA = [
{"id": "crit-l35-severity", "label": "Classification of Asthma Severity (12 Years and Older)", "color": _C,
 "tag": "Criteria &middot; Lecture 35 &middot; slide 62 (picture s62-c725c812.png)",
 "cols": ["Component", "Intermittent", "Mild persistent", "Moderate persistent", "Severe persistent"],
 "widths": ["20%", "20%", "20%", "20%", "20%"], "rows": [
 ("Symptoms", "&le; 2 days/week", "&gt; 2 days/week but not daily", "Daily", "Throughout the day"),
 ("Nighttime awakenings", "&le; 2&times;/month", "3&ndash;4&times;/month", "&gt; 1&times;/week but not nightly", "Often 7&times;/week"),
 ("Short-acting beta-2 agonist use for symptom control (not prevention of exercise-induced bronchospasm)", "&le; 2 days/week", "&gt; 2 days/week but not daily, and not more than 1&times; on any day", "Daily", "Several times per day"),
 ("Interference with normal activity", "None", "Minor limitation", "Some limitation", "Extremely limited"),
 ("Lung function: FEV1 (forced expiratory volume in 1 second) and its ratio to FVC (forced vital capacity)", "Normal FEV1 between exacerbations; FEV1 &gt; 80% predicted; ratio normal", "FEV1 &gt; 80% predicted; ratio normal", "FEV1 &gt; 60% but &lt; 80% predicted; ratio reduced 5%", "FEV1 &lt; 60% predicted; ratio reduced &gt; 5%"),
 ("Risk: exacerbations requiring oral systemic corticosteroids", "0&ndash;1/year", "&ge; 2/year", "&ge; 2/year", "&ge; 2/year"),
 {"note": "Slide 62 notes: severity is set by both impairment and risk; impairment is assessed by the patient&rsquo;s recall of the previous 2&ndash;4 weeks and spirometry; <b>assign severity to the most severe category in which any feature occurs</b>. Patients with &ge; 2 exacerbations requiring oral systemic corticosteroids in the past year may be considered the same as persistent asthma, even without matching impairment."},
 {"note": "The slide&rsquo;s normal-ratio-by-age column and its treatment row are left out: the recording put them out of scope."},
 ], "mnemonic": {"hook": "Intermittent plays the rule of twos; then symptoms go not-daily, daily, all day, and FEV1 drops past 80 and 60.",
  "key": [["Symptoms", "&le; 2 days &rarr; not daily &rarr; daily &rarr; all day"], ["Nights", "&le; 2/month &rarr; 3&ndash;4/month &rarr; weekly, not nightly &rarr; often nightly"],
          ["Rescue inhaler", "&le; 2 days &rarr; not daily &rarr; daily &rarr; several times a day"], ["Activity", "none &rarr; minor &rarr; some &rarr; extreme limitation"],
          ["FEV1", "&gt; 80 (intermittent and mild) &rarr; 60&ndash;80 &rarr; &lt; 60"], ["Steroid bursts", "0&ndash;1/year intermittent; &ge; 2/year persistent"]],
  "breaks": "Mild and intermittent share the same FEV1 (above 80% with a normal ratio): tell them apart by symptoms, nights and rescue use. Nights break the pattern too: intermittent counts per month, moderate per week."}},
{"id": "crit-l35-action-plan", "label": "Asthma Action Plan Zones", "color": _C,
 "tag": "Criteria &middot; Lecture 35 &middot; slides 88&ndash;89 (pictures s88-59d3f609.png, s89-400e8d7c.png)",
 "cols": ["Zone", "Signs", "Peak flow (slide 88)", "Action"], "widths": ["16%", "48%", "16%", "20%"], "rows": [
 ("<b>Green</b>: &ldquo;Doing well&rdquo; / Go", "<b>Slide 88:</b> no cough, wheeze, chest tightness, or shortness of breath during the day or night; can do usual activities. <b>Slide 89 (all of these):</b> breathing is good; no cough or wheeze; sleep through the night; can work and play", "<b>&ge; 80%</b> of my best peak flow", "Take long-term control medicines each day (include an anti-inflammatory); slide 89: use preventive medicine"),
 ("<b>Yellow</b>: &ldquo;Asthma is getting worse&rdquo; / Caution", "<b>Slide 88:</b> cough, wheeze, chest tightness, or shortness of breath; or waking at night due to asthma; or can do some, but not all, usual activities. <b>Slide 89 (any of these):</b> first signs of a cold; exposure to known trigger; cough; mild wheeze; tight chest; coughing at night", "<b>50&ndash;79%</b>", "Add quick-relief medicine (short-acting beta-2 agonist) and keep taking green zone medicine; slide 89: call your primary care provider"),
 ("<b>Red</b>: &ldquo;Medical alert!&rdquo; / Danger", "<b>Slide 88:</b> very short of breath; or quick-relief medicines have not helped; or cannot do usual activities; or symptoms are same or get worse after 24 hours in yellow zone. <b>Slide 89 (getting worse fast):</b> medicine is not helping; breathing is hard and fast; nose opens wide; ribs show; can&rsquo;t talk well", "<b>&lt; 50%</b>", "Take quick-relief medicine and oral steroid, then call your doctor now; slide 89: get help from a doctor"),
 ("<b>Danger signs</b> (slide 88)", "Trouble walking and talking due to shortness of breath; lips or fingernails are blue", "&mdash;", "Take 4 or 6 puffs of quick-relief medicine and go to the hospital or call an ambulance now"),
 ], "mnemonic": {"hook": "Traffic light at 80 and 50: green 80 and up, yellow 50&ndash;79, red under 50.",
  "key": [["Green", "&ge; 80%, no symptoms day or night, usual activities: daily controller"], ["Yellow", "50&ndash;79%, symptoms or night waking or some activities: add quick-relief"],
          ["Red", "&lt; 50%, very short of breath, quick-relief failing, or 24 hours in yellow without improving"], ["Danger signs", "cannot walk and talk; blue lips or nails"]],
  "breaks": "Slide 89&rsquo;s traffic light has no percentages, and the danger signs are judged by sight, not by peak flow. Yellow that lasts 24 hours without improving becomes red."}},
{"id": "crit-l35-test-cutoffs", "label": "Asthma Test Cut-Offs", "color": _C,
 "tag": "Criteria &middot; Lecture 35 &middot; slides 53, 58, 60, 94",
 "cols": ["Test", "Cut-off", "Meaning"], "widths": ["28%", "32%", "40%"], "rows": [
 ("Spirometry before and after a bronchodilator (slide 53)", "FEV1 (forced expiratory volume in 1 second) improves <b>&ge; 12%</b>", "Supports asthma (before the bronchodilator: reduced FEV1 and reduced ratio)"),
 ("Bronchial provocation: methacholine or histamine (slide 58)", "<b>Not recommended if FEV1 &lt; 65% predicted</b>", "Useful if spirometry is not diagnostic; exercise challenge if exercise-induced bronchospasm is suspected"),
 ("Peak expiratory flow at home (slide 60)", "<b>20% change</b> morning vs afternoon, <i>or</i> 20% change day to day", "Poor control (measured in the morning before and the afternoon after the bronchodilator)"),
 ("Exercise-induced bronchospasm (slide 94)", "Begins during or <b>within 3 minutes</b> after exercise; peaks in <b>10&ndash;15 minutes</b>; resolves by <b>60 minutes</b>", "Common in children and adolescents"),
 {"note": "Slide 53 reads &ldquo;FEV1 &ge;12% or &ge; 10% improvement in predicted FEV1&rdquo;; questions use the 12%."},
 ], "mnemonic": {"hook": "Up 12 to diagnose, 65 is the floor for provoking, a 20% swing means poor control, and exercise runs on a 3-15-60 clock.",
  "key": [["12", "bronchodilator response that supports asthma"], ["65", "no provocation test below 65% predicted"],
          ["20", "peak flow swing (morning to afternoon or day to day) = poor control"], ["3-15-60", "exercise bronchospasm: starts by 3, peaks 10&ndash;15, gone by 60 minutes"]],
  "breaks": "The 15 in the clock is the top of a 10&ndash;15 minute peak, not a single time."}},
{"id": "crit-l35-types", "label": "Extrinsic vs Intrinsic Asthma", "color": _C,
 "tag": "Criteria &middot; Lecture 35 &middot; slides 34&ndash;35",
 "cols": ["Feature", "Extrinsic (slide 35)", "Intrinsic (slides 34&ndash;35)"], "widths": ["24%", "38%", "38%"], "rows": [
 ("Trigger", "Triggered by allergen exposure", "Not triggered by allergen exposure"),
 ("How common", "<b>Most common</b> form of asthma", "Minority (<b>~10%</b>)"),
 ("Atopy and tests", "&mdash;", "Not atopic; <b>negative skin allergy tests</b> and <b>normal serum IgE (immunoglobulin E)</b>"),
 ("Onset and course", "&mdash;", "<b>Later onset (adulthood)</b>; usually more severe, persistent"),
 ("Associations", "&mdash;", "<b>Nasal polyps</b> common; <b>may be aspirin sensitive</b>"),
 ("Pathology", "Same in both", "Same in both"),
 ], "mnemonic": {"hook": "Intrinsic is the Late Adult with Polyps and Aspirin and clean allergy tests (LAPA).",
  "key": [["Allergen", "extrinsic is triggered by it, intrinsic is not"], ["Most common", "extrinsic; intrinsic only about 10%"], ["Clean tests", "intrinsic: negative skin tests, normal IgE"],
          ["L, A", "Late onset in Adulthood, more severe and persistent"], ["P, A", "Polyps, Aspirin sensitivity"], ["Same", "pathology does not differ"]],
  "breaks": "The slides describe intrinsic in detail and extrinsic only by its trigger and frequency; the dashes are blanks on the slides, not negatives."}},
{"id": "crit-l35-death-risk", "label": "Asthma: Risk of Death", "color": _C,
 "tag": "Criteria &middot; Lecture 35 &middot; slide 14",
 "cols": ["Risk factor (slide 14)"], "widths": ["100%"], "rows": [
 ("Poorly controlled asthma: frequent bronchodilator use",), ("No inhaled corticosteroids",),
 ("Poor compliance with inhaled corticosteroids",), ("Previous admissions for near-fatal attacks",),
 ], "mnemonic": {"hook": "Too much rescue, too little steroid (none or skipped), and a near-death before.",
  "key": [["Too much rescue", "frequent bronchodilator use"], ["None", "no inhaled corticosteroid"], ["Skipped", "poor compliance with the inhaled corticosteroid"], ["Near-death before", "previous admission for a near-fatal attack"]],
  "breaks": "Two of the four are the same drug: the inhaled corticosteroid either never prescribed or not taken."}},
{"id": "crit-l35-atopic-triad", "label": "Atopic Triad", "color": _C,
 "tag": "Criteria &middot; Lecture 35 &middot; slide 25",
 "cols": ["Triad member (slide 25)"], "widths": ["100%"], "rows": [
 ("Allergic rhinitis",), ("Asthma",), ("Atopic dermatitis",),
 {"note": "Slide 25: atopy = genetic disposition for developing allergic reaction, with elevated IgE (immunoglobulin E) on exposure to allergen; non-atopic individuals have a low risk of asthma, and not all atopic individuals develop it."},
 ], "mnemonic": {"hook": "Sneeze, wheeze, itch.",
  "key": [["Sneeze", "allergic rhinitis"], ["Wheeze", "asthma"], ["Itch", "atopic dermatitis"]],
  "breaks": "Do not confuse it with the intrinsic picture (nasal polyps, aspirin sensitivity), which is not atopic."}},
{"id": "crit-l35-nsaids", "label": "Aspirin-Sensitive Asthma: Which Anti-Inflammatory Drugs", "color": _C,
 "tag": "Criteria &middot; Lecture 35 &middot; slide 93",
 "cols": ["Group (slide 93)", "Drugs"], "widths": ["40%", "60%"], "rows": [
 ("<b>Avoid</b>: non-selective NSAIDs (nonsteroidal anti-inflammatory drugs)", "Diclofenac &middot; ibuprofen &middot; naproxen &middot; indomethacin"),
 ("<b>May use</b>: selective NSAIDs", "Celecoxib &middot; meloxicam"),
 ], "mnemonic": {"hook": "Avoid the DINI; you Can Manage with the selective two.",
  "key": [["D", "diclofenac"], ["I", "ibuprofen"], ["N", "naproxen"], ["I", "indomethacin"], ["C", "celecoxib"], ["M", "meloxicam"]],
  "breaks": "The slide lists brand names beside the selective drugs; only the generic names are used here."}},
]

TOPICS = [
{"id": "l35-emph", "label": "★ Professor Emphasized — Severity, Education, Classes", "color": "#b8860b", "rows": [
 ["★ Severity from a description", "Table for <b>12 years and older</b>; severity goes to the <b>most severe category in which any feature occurs</b>. Intermittent = &ldquo;rule of twos&rdquo; (2 or fewer days/week, 2 or fewer nights/month). Focus on <b>mild and moderate</b>."],
 ["★ Persistent cut-offs", "<b>Mild:</b> symptoms more than 2 days/week but not daily; 3&ndash;4 nights/month; 1-second volume above 80%. <b>Moderate:</b> daily; more than once/week but not nightly; 60&ndash;80%. <b>Severe:</b> all day; often 7/week; below 60%."],
 ["★ Patient education", "Written action plan; inhaler, spacer and nebulizer technique; peak flow zones; triggers; rinse the mouth after an inhaled steroid; vaccines. &ldquo;Really important is the patient education.&rdquo;"],
 ["★ Classes, not brands", "Know the <b>class</b>: short-acting beta-2 agonist (rescue), inhaled corticosteroid (first-line controller), long-acting beta-2 agonist (never alone), leukotriene modifier (add-on)."],
 ["Not tested", "Epidemiology numbers; emergency management (slides 97&ndash;105); age-normal ratio values; any question with conflicting rescue-inhaler guidance."],
]},
{"id": "l35-basics", "label": "Definition, Types &amp; Triggers", "color": "#7a2d30", "rows": [
 ["Definition", "Chronic inflammatory airway disorder, <b>reversible</b> obstruction (some long-standing cases irreversible); trouble getting air <b>out</b>. Hyper-responsiveness: excessive constriction to a trigger a normal airway ignores."],
 ["Course", "Any age, peak 3 years; may quiet in adolescence and return. Severity rarely changes: <b>mild rarely becomes severe; severe usually severe at onset</b>."],
 ["Death risk", "Frequent bronchodilator use; no or poorly taken inhaled steroid; previous near-fatal admission."],
 ["Extrinsic vs intrinsic", "<b>Extrinsic:</b> allergen-triggered, atopic, most common (atopic triad: rhinitis, asthma, eczema). <b>Intrinsic:</b> about 10%, adult onset, negative skin tests, normal immunoglobulin E, <b>nasal polyps, may be aspirin sensitive</b>."],
 ["Other types", "Occupational (better weekends and vacations); catamenial (menstrual cycle); &ldquo;cardiac&rdquo; (decompensated heart failure); exercise-induced (starts within 3 minutes, peaks 10&ndash;15, gone by 60); aspirin-sensitive (1&ndash;5%, minutes to 12 hours)."],
 ["Triggers", "Dust mites (most common), pet dander, cockroaches, pollens, fungal spores; viruses; <b>aspirin and beta blockers</b>; exercise; cold air; pollution; smoke; stress; occupational agents."],
 ["Risk factors", "Atopy; obesity (body mass index above 30); early viral infection. Allergen avoidance does <b>not</b> prevent asthma; early exposure may protect."],
]},
{"id": "l35-dx", "label": "Diagnosis &amp; Monitoring", "color": "#2f5d6b", "rows": [
 ["Exam", "Often normal between attacks. Exacerbation: accessory muscles, leaning forward; <b>wheeze may vanish</b> (decreased breath sounds, prolonged expiration). Worse at night (peak 3&ndash;4 am)."],
 ["Spirometry", "Before and after a short-acting bronchodilator; reduced 1-second volume and ratio; <b>12% or more improvement</b> supports asthma. Effort-dependent: coach. Repeat <b>yearly</b>."],
 ["Other tests", "Provocation (methacholine, histamine) if spirometry is not diagnostic, <b>not below 65% predicted</b>; exercise challenge for exercise-induced bronchospasm; allergy testing for triggers; exhaled nitric oxide = inflammation; chest x-ray normal or hyperinflated."],
 ["Peak flow", "Home baseline; <b>morning before, afternoon after</b> the bronchodilator; <b>20% change</b> between them or day to day = poor control."],
 ["Action plan", "<b>Green</b> 80% or more of personal best; <b>yellow</b> 50&ndash;79% (add quick-relief, keep controller); <b>red</b> under 50%, very short of breath or quick-relief failing (medical alert). Danger signs: cannot walk or talk, blue lips or nails."],
 ["Visit sequence", "Initial: diagnose, classify, start medicine and demonstrate, written plan, schedule follow-up. Follow-up: control, compliance, adjust, update plan."],
 ["Differential", "Vocal fold dysfunction or paralysis, foreign body, laryngotracheal mass; chronic obstructive pulmonary disease, bronchiectasis, cystic fibrosis; conversion disorder, emotional laryngeal wheezing, factitious disorder; aspergillosis."],
 ["Aspergillosis", "Allergic bronchopulmonary aspergillosis: hypersensitivity to <i>Aspergillus fumigatus</i>, almost only in asthma or cystic fibrosis; vigorous immunoglobulin E and G response; exacerbations."],
]},
{"id": "l35-rx", "label": "Treatment by Class", "color": "#1f5c3a", "rows": [
 ["Rescue", "Every patient needs a <b>short-acting beta-2 agonist</b> (albuterol); 3&ndash;6 hours; before exercise prevents exercise-induced bronchospasm; rising use = poor control; tremor, palpitations."],
 ["Inhaled corticosteroid", "<b>Preferred first-line</b> for persistent asthma; twice daily; full effect takes months; hoarseness, cough, thrush &rarr; <b>spacer, rinse and spit</b>."],
 ["Systemic steroid", "Exacerbations: short course, <b>no taper</b>. Long-term only if refractory, minimum dose, with calcium and vitamin D. Side effects: truncal obesity, osteoporosis, bruising, ulcers, depression, hypertension."],
 ["Long-acting beta-2 agonist", "Up to 12 hours; <b>never alone</b> (no anti-inflammatory effect); pair with inhaled steroid."],
 ["Other controllers", "Cromolyn: prevents, does not relieve. Tiotropium: slow, weak, few side effects. Theophylline: narrow range; nausea, vomiting, arrhythmias, seizures, high glucose, low potassium. Leukotriene modifiers: add-on, helpful for exercise-induced. Monoclonal antibodies: specialist, spare steroids."],
 ["Avoid", "<b>Aspirin and non-selective anti-inflammatory drugs</b> (ibuprofen, naproxen, diclofenac, indomethacin) in aspirin-sensitive asthma; selective ones (celecoxib, meloxicam) allowed. <b>Beta blockers.</b>"],
 ["Immunotherapy &amp; vaccines", "Immunotherapy: allergic triggers, single allergen, <b>controlled setting only</b>. Influenza yearly and pneumococcal; <b>caution with intranasal influenza vaccine</b>."],
 ["Poor control", "Check <b>compliance and technique first</b> (most common reason); steroid resistance is very rare; refractory asthma &rarr; specialist."],
]},
]
