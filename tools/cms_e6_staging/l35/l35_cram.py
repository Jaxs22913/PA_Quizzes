# -*- coding: utf-8 -*-
"""Lecture 35 (Asthma, Finck) cram topics, condensed from the staged guide section 3. Same row format as
tools/cms_e6_cram/l34.py; the exam-level builder (builder A) splices this in as tools/cms_e6_cram/l35.py."""

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
