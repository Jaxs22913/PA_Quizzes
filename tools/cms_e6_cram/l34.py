# -*- coding: utf-8 -*-
"""Lecture 34 (Acid-Base Part I, Finck) cram topics, condensed from guide section 2."""

TOPICS = [
{"id": "l34-emph", "label": "★ Professor Emphasized — Normals, Winter Formula, Anion Gap", "color": "#b8860b", "rows": [
 ["★ Normal values", "pH <b>7.35&ndash;7.45</b> (&ldquo;burn this into your eyeballs&rdquo;); carbon dioxide <b>36&ndash;44</b> mm Hg (midpoint 40); bicarbonate <b>22&ndash;26</b> mEq/L (midpoint 24). Acidemia below 7.35, alkalemia above 7.45."],
 ["★ Winter formula", "Metabolic acidosis: expected carbon dioxide = <b>1.5 &times; bicarbonate + 8, &plusmn; 2</b>. Higher than expected = <b>added respiratory acidosis</b>, can signal impending respiratory failure."],
 ["★ Anion gap", "<b>Sodium &minus; (chloride + bicarbonate)</b>, normal <b>9&ndash;15</b>. Above 15 = elevated-gap acidosis."],
 ["★ Treatment", "&ldquo;Always going to be correct the underlying disorder.&rdquo; Therapy aimed at the pH itself only when it is unsustainable: <b>below 6.7 or above 7.6</b>."],
 ["★ Frequent questions", "Obesity hypoventilation triad; paper bag = placebo; saline responsive is the common alkalosis; carbon dioxide rarely above 55 in compensation; urine chloride splits the alkaloses."],
]},
{"id": "l34-read", "label": "Reading the Gas &amp; Compensation", "color": "#7a2d30", "rows": [
 ["Steps", "1. pH: acidosis or alkalosis. 2. Which value (carbon dioxide or bicarbonate) matches the pH. 3. Mixed? pH more or less than expected. 4. Compensation: respiratory disorder &rarr; expected <b>bicarbonate</b>; metabolic disorder &rarr; expected <b>carbon dioxide</b>. 5. Don&rsquo;t neglect the patient."],
 ["Rules", "Compensation <b>never returns pH to normal</b> and never past it; respiratory cause &rarr; renal compensation; metabolic cause &rarr; respiratory compensation. Normal pH with abnormal values = <b>mixed disorder</b>."],
 ["Ratios (given in questions)", "Respiratory acidosis: bicarbonate +<b>1</b> per 10 mm Hg acute, +<b>3.5</b> chronic. Respiratory alkalosis: &minus;<b>2</b> per 10 acute, &minus;<b>5</b> chronic. Metabolic acidosis: carbon dioxide &minus;1.3 per 1 mEq/L (use Winter). Metabolic alkalosis: +<b>0.75</b> per 1 mEq/L, <b>rarely above 55</b> (above = concurrent respiratory acidosis)."],
 ["Timing", "Renal compensation <b>begins 6&ndash;12 hours</b> after onset, complete over <b>days</b>: small bicarbonate change = acute, large = chronic."],
 ["Algorithm", "pH below 7.4 + carbon dioxide above 40 = respiratory acidosis (acute or chronic?); below 40 = compensating metabolic acidosis (check the gap). pH above 7.4 + carbon dioxide above 40 = compensating metabolic alkalosis; below 40 = respiratory alkalosis."],
]},
{"id": "l34-resp", "label": "Respiratory Acidosis &amp; Alkalosis", "color": "#2f5d6b", "rows": [
 ["Respiratory acidosis", "Hypoventilation &rarr; carbon dioxide above 40 &rarr; low pH, &plusmn; hypoxemia. Somnolence, confusion, altered mental status, asterixis, myoclonus; severe: raised cerebral blood flow and intracranial pressure, papilledema. Labs: low pH, high carbon dioxide, high bicarbonate, <b>hypochloremia if chronic</b> (ammonium chloride excretion)."],
 ["Acute causes", "Airway obstruction; pneumonia, asthma, pulmonary edema, aspiration pneumonitis; central nervous system depression (recreational drugs, intracranial catastrophe, intravenous sedation); myasthenia gravis, Guillain-Barr&eacute; syndrome; pneumothorax, flail chest."],
 ["Chronic causes", "<b>Chronic obstructive pulmonary disease</b> (&ldquo;first thing that comes to mind&rdquo;), interstitial lung disease, idiopathic pulmonary fibrosis; muscular dystrophy, amyotrophic lateral sclerosis; <b>★ obesity hypoventilation (Pickwickian) syndrome: obesity + sleep disordered breathing + chronic hypercapnia</b>."],
 ["Treat", "Underlying cause. Acute: <b>restore ventilation</b>. Chronic: <b>careful oxygen titration</b>; avoid rapid carbon dioxide reduction &rarr; <b>post-hypercapnic metabolic alkalosis</b>."],
 ["Respiratory alkalosis", "Hyperventilation &rarr; low carbon dioxide &rarr; high pH. Light-headedness, anxiety, perioral numbness, paresthesias; severe: <b>tetany</b> (high pH binds calcium to albumin). Compensation: cells trade hydrogen ions for potassium, then kidneys excrete bicarbonate and keep chloride (low bicarbonate, hypokalemia, hyperchloremia)."],
 ["Alkalosis causes", "Psychogenic, stroke, raised intracranial pressure; hypoxia (high altitude, severe anemia, ventilation-perfusion mismatch, hypotension); salicylates, caffeine, nicotine, catecholamines, thyroxine; pulmonary embolism, pneumonia, pulmonary edema, mechanical hyperventilation, interstitial lung disease; pregnancy, hyperthyroidism; septicemia, heat exposure, hepatic failure."],
 ["Treat", "Underlying cause; usually self-limited. <b>★ Paper bag not necessary</b>: does not correct carbon dioxide, may lower oxygen, placebo. Rapid correction of chronic alkalosis &rarr; post-hypocapnia metabolic acidosis."],
]},
{"id": "l34-metab", "label": "Metabolic Alkalosis &amp; Acidosis", "color": "#5a3d8a", "rows": [
 ["Metabolic alkalosis", "High bicarbonate &rarr; high pH. No characteristic findings; orthostatic hypotension; hypokalemia &rarr; weakness, hyporeflexia. Labs: high pH and bicarbonate, raised carbon dioxide, low potassium, low chloride."],
 ["★ Urine chloride", "<b>Below 25 mEq/L = saline responsive</b> (more common; volume contraction): diuretics, post-hypercapnia, vomiting or nasogastric suction, antacids, volume contraction. <b>Above 40 = saline unresponsive</b> (euvolemic or hypervolemic) &rarr; check <b>blood pressure</b>."],
 ["Unresponsive groups", "<b>Normotensive:</b> severe potassium depletion; hypoparathyroidism and hypercalcemia. <b>Hypertensive:</b> primary aldosteronism, exogenous alkali, mineralocorticoids, <b>licorice</b> (&ldquo;a unicorn&rdquo;)."],
 ["Treat alkalosis", "Underlying cause; saline responsive: <b>isotonic saline</b> and <b>stop diuretics</b>."],
 ["Metabolic acidosis", "Low bicarbonate &rarr; low pH, low carbon dioxide; hyperkalemia may be present. Signs of the cause + compensatory hyperventilation; <b>Kussmaul respirations</b> (increased tidal volume and tachypnea) in diabetic ketoacidosis. Normal gap = hyperchloremic; elevated gap = normochloremic."],
 ["Elevated gap: MUDPILES", "Methanol, metformin &middot; uremia &middot; diabetic ketoacidosis &middot; paraldehyde &middot; isoniazid, iron &middot; lactic acidosis &middot; ethylene glycol &middot; salicylates, starvation."],
 ["Normal gap: USEDCAR", "Ureteral diversion &middot; saline infusion &middot; exogenous acid &middot; diarrhea &middot; carbonic anhydrase inhibitors &middot; adrenal insufficiency &middot; renal tubular acidosis (bicarbonate loss, chloride retention)."],
 ["Gap pitfalls", "Albumin makes most of the normal gap; <b>hypoalbuminemia</b>, sodium extremes and antibiotics distort it. A normal gap does not exclude acidosis and should not override clinical concern. Fewer unmeasured cations (calcium, magnesium, potassium) raise it."],
]},
{"id": "l34-lytes", "label": "Electrolytes &amp; Oxygen", "color": "#1f5c3a", "rows": [
 ["Potassium", "<b>Acidosis</b>: hydrogen into cells, potassium out &rarr; <b>hyperkalemia</b>. <b>Alkalosis</b>: potassium into cells &rarr; <b>hypokalemia</b>."],
 ["Oxygen", "<b>Acidosis</b>: lower hemoglobin affinity, curve <b>right</b>, <b>more</b> oxygen to tissues. <b>Alkalosis</b>: higher affinity, curve <b>left</b>, <b>less</b> oxygen to tissues."],
 ["Unsustainable pH", "<b>Below 6.7 or above 7.6</b>: cardiac hypocontractility and irritability, seizures, cerebral edema, metabolic disturbances."],
 ["Buffers", "Chemical buffering (extracellular, intracellular), respiratory (carbon dioxide, fast), renal (bicarbonate, hours to days). Water + carbon dioxide &harr; carbonic acid &harr; hydrogen ion + bicarbonate. Brainstem chemoreceptor: more carbon dioxide &rarr; lower cerebral pH &rarr; more breathing. Hypercapnia usually from <b>under-excretion</b>."],
]},
]
