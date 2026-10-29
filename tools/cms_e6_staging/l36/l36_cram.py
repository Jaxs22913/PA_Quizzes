# -*- coding: utf-8 -*-
"""Lecture 36 (COPD, Reynolds) cram topics, condensed from the staged guide section 4. Same row format as
tools/cms_e6_cram/l34.py; builder A splices this in as tools/cms_e6_cram/l36.py."""

TOPICS = [
{"id": "l36-emph", "label": "★ Key Numbers", "color": "#b8860b", "rows": [
 ["★ Diagnosis", "Spirometry before and after a bronchodilator: ratio of 1-second volume to forced vital capacity <b>below 0.70</b>; response <b>under 12%</b> = irreversible. Chronic bronchitis <b>without obstruction is not</b> this disease."],
 ["★ Airflow grade", "Post-bronchodilator 1-second volume: <b>1 mild &ge;80%</b>; <b>2 moderate 50&ndash;79%</b>; <b>3 severe 30&ndash;49%</b>; <b>4 very severe &lt;30%</b>."],
 ["★ Symptoms &amp; risk", "Assessment test <b>&ge;10</b> or dyspnea grade <b>&ge;2</b> = more symptoms. High risk = <b>2 or more moderate exacerbations or 1 hospitalization</b>."],
 ["★ Groups", "2020: A low/low, B high symptoms/low risk, C low symptoms/high risk, D high/high. 2023&ndash;2026: A, B, and <b>E = any high risk</b>. &ldquo;S &times; R = group.&rdquo;"],
 ["★ Start", "A: one bronchodilator. B: long-acting beta agonist + long-acting antimuscarinic. E: that pair, <b>add inhaled steroid if eosinophils &ge;300</b>."],
 ["★ Survival", "Only <b>smoking cessation</b>, <b>long-term oxygen</b> (severe resting hypoxemia) and <b>noninvasive ventilation</b> (hypercapnic exacerbation) improve survival."],
]},
{"id": "l36-basics", "label": "Subtypes, Causes &amp; Presentation", "color": "#7a2d30", "rows": [
 ["Definition", "Persistent airflow obstruction + respiratory symptoms from inhaled particles; umbrella of chronic bronchitis (cough &ge;3 months/year for 2 years) and emphysema (alveolar destruction)."],
 ["Blue bloater", "Chronic bronchitis: sputum, rhonchi, cyanosis, edema; early hypoxemia and hypercapnia; normal diffusing capacity; bronchial wall thickening."],
 ["Pink puffer", "Emphysema: thin, pursed lips, barrel chest, distant sounds, hyperresonance; gas exchange late; <b>reduced diffusing capacity</b>; flat diaphragm, bullae."],
 ["Causes", "Tobacco ~90% (primary); biomass smoke (low-income countries, never-smokers); coal, gold mining, welding; inactivity. Cessation is the key treatment."],
 ["Alpha-1 antitrypsin deficiency", "Age &le;45, nonsmoker, <b>basilar panlobular</b> emphysema, family history; level &lt;11 micromol/L + deficient genotype. Smokers: centrilobular, upper lobe."],
 ["Early sign", "<b>Dyspnea on exertion</b>. Not always thin; not always productive. Pursed lips keep airways open. Screen: heart disease, lung cancer, osteoporosis, depression, reflux, anemia."],
 ["Exam extras", "Flat diaphragm &rarr; lower intercostal retraction on inspiration; neck veins distend in expiration; cor pulmonale; syncope and falls (poor perfusion)."],
]},
{"id": "l36-dx", "label": "Tests", "color": "#2f5d6b", "rows": [
 ["Patterns", "Low ratio = obstruction. Obstruction + low forced vital capacity = possible mixed (confirm with total lung capacity). Normal ratio + low forced vital capacity = possible restriction."],
 ["Physiology", "Air trapping (residual volume up), hyperinflation, dynamic hyperinflation with exertion; <b>scooped</b> expiratory limb."],
 ["Other tests", "Blood gas only if deteriorating (carbon dioxide &gt;45, bicarbonate up = compensatory metabolic alkalosis); blood count (anemia, eosinophils); B-type natriuretic peptide for heart failure; chest film rules out other causes; computed tomography rarely needed."],
 ["Scores", "<b>BODE</b> (body mass index, obstruction, dyspnea, exercise) &rarr; 4-year survival: 0&ndash;2 = 80%, 3&ndash;4 = 67%, 5&ndash;6 = 57%, 7&ndash;10 = 18%. 1-second volume &ge;65 = 0, 50&ndash;64 = 1, 36&ndash;49 = 2, &le;35 = 3; walk &ge;350 m = 0, 150&ndash;249 = 2, &le;149 = 3; dyspnea 0&ndash;1 = 0, 2 = 1, 3 = 2, 4 = 3; body mass index &le;21 = 1."],
]},
{"id": "l36-rx", "label": "Management", "color": "#1f5c3a", "rows": [
 ["Non-drug", "Cessation (essential, all groups, <b>with counseling</b>); <b>rehabilitation essential for B and E</b>; activity; yearly influenza vaccine; pneumococcal at 65 (earlier if 1-second volume &lt;40% or cardiac disease)."],
 ["Five A's / FRAMES", "Ask, Advise, Assess, Assist, Arrange. Feedback, Responsibility, Advice, Menu, Empathy, Self-efficacy."],
 ["Drug cautions", "Long-acting beta agonist: arrhythmia, worse atrial fibrillation. Antimuscarinic: dry mouth, anticholinergic burden in elders. Inhaled steroid: <b>never alone</b>, pneumonia, fractures. Albuterol: not excessively. <b>Oral steroids: exacerbations only.</b>"],
 ["Older adults", "Fixed 0.70 ratio may overdiagnose; arthritis, tremor, cognition, low flow limit dry powder inhalers &rarr; spacer, soft mist, nebulizer; refer to rehabilitation actively; palliative care early."],
 ["Oxygen", "Treat arterial oxygen &lt;55 mmHg or saturation &lt;88%. Rest &le;88% &rarr; long-term oxygen &gt;15 hours/day; rest 89&ndash;93% &rarr; none; exertion &le;88% &rarr; with exertion; night only &rarr; sleep apnea workup."],
 ["Refer to pulmonology", "Uncertain diagnosis, early onset or deficiency, exacerbations despite optimal therapy, oxygen, noninvasive ventilation, surgery, symptoms out of proportion."],
]},
{"id": "l36-exac", "label": "Exacerbations", "color": "#5a3d8a", "rows": [
 ["Definition", "Acute worsening over <b>14 days or less</b>; exclude pneumonia, embolism, acute heart failure, pneumothorax. <b>&gt;80% outpatient.</b>"],
 ["Admit / ICU", "Admit: marked symptoms, noninvasive ventilation, new edema, arrhythmia, comorbidity, no home support. ICU: unstable, major infection, invasive ventilation, sepsis, altered mental status, acidosis."],
 ["Treat", "Bronchodilators, steroids, oxygen; <b>antibiotics if more and purulent sputum</b> (doxycycline, macrolide, trimethoprim-sulfamethoxazole, amoxicillin-clavulanate; <b>levofloxacin for pseudomonal concern</b>); high-flow for hypoxia; <b>noninvasive ventilation for hypercapnia</b>."],
 ["Discharge", "Albuterol no more than every 4 hours; stable 12&ndash;24 hours; walks across room; eats and sleeps; home arrangements. Recovery <b>4&ndash;6 weeks</b>."],
]},
]
