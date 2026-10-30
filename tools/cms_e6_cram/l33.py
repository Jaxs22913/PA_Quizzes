# -*- coding: utf-8 -*-
"""Lecture 33 (Oxygen Delivery, Reynolds) cram topics, condensed from guide section 1.

CRITERIA (2026-10-30, memory cram_criteria_tables): one table per criteria set or cut-off table on the slides,
each with a labeled memory aid; cells are the slide wording (pictures read from the slide images: s6 is a table
picture); slide conflicts are note rows, never resolved. tools/build_cms_e6_cram.py puts them at the top.
"""

_C = "#7a2d30"
CRITERIA = [
{"id": "crit-l33-indications", "label": "Oxygen Therapy: Indications, Benefits &amp; Risks", "color": _C,
 "tag": "Criteria &middot; Lecture 33 &middot; slide 3",
 "cols": ["Side", "What slide 3 lists"], "widths": ["20%", "80%"], "rows": [
 ("Indications", "<b>Hypoxia</b> &middot; acute medical/surgical needs (perioperative/postoperative period) &middot; respiratory conditions (<b>carbon monoxide poisoning</b>) &middot; special indications: <b>air hunger</b>, <b>cluster headache</b>"),
 ("Benefits", "Correction of hypoxia &middot; symptom relief &middot; therapeutic benefits"),
 ("Risks", "Hypercapnia/carbon dioxide retention &middot; <b>fire hazard!</b> &middot; mucosal irritation &middot; vasoconstriction (remember, <b>not given in myocardial infarction unless oxygen saturation &lt; 91%</b>)"),
 {"note": "Slide 3 gives the myocardial infarction cut-off as below 91%; the slide&rsquo;s 91% is the value tested."},
 ], "mnemonic": {"hook": "Hypoxic Patients Can Accept Cannulas &mdash; but Fire Has Many Victims.",
  "key": [["H", "Hypoxia"], ["P", "Perioperative/postoperative (acute medical or surgical need)"], ["C", "Carbon monoxide poisoning"],
          ["A", "Air hunger"], ["C", "Cluster headache"], ["F", "Fire hazard"], ["H", "Hypercapnia (carbon dioxide retention)"],
          ["M", "Mucosal irritation"], ["V", "Vasoconstriction: not in myocardial infarction unless saturation is below 91%"]],
  "breaks": "The benefits row (correction of hypoxia, symptom relief, therapeutic benefit) is not in the aid. Air hunger and cluster headache are listed apart, as the special indications."}},
{"id": "crit-l33-home-oxygen", "label": "Home Oxygen Qualification (Medicare)", "color": _C,
 "tag": "Criteria &middot; Lecture 33 &middot; slides 5&ndash;6",
 "cols": ["Situation (slide 6)", "Qualifying criteria (arterial oxygen = partial pressure of oxygen in arterial blood)", "Result"],
 "widths": ["20%", "58%", "22%"], "rows": [
 ("Resting (room air)", "Arterial oxygen <b>&le; 55 mm Hg</b> <i>or</i> saturation <b>&le; 88%</b>", "<b>Group I</b> qualification"),
 ("Resting (conditional)", "Arterial oxygen <b>56&ndash;59 mm Hg</b> <i>or</i> saturation <b>= 89%</b> + evidence of pulmonary hypertension, cor pulmonale, or hematocrit &gt; 56%", "<b>Group II</b> qualification"),
 ("During sleep", "Arterial oxygen &le; 55 mm Hg <i>or</i> saturation &le; 88% with a <b>&ge; 5% drop</b> from baseline", "Qualifies for nocturnal oxygen"),
 ("During exertion", "Arterial oxygen &le; 55 mm Hg <i>or</i> saturation &le; 88% during exercise <b>and improves with oxygen</b>", "Qualifies for ambulatory oxygen"),
 ("Recertification", "Group I: <b>12 months</b> &middot; Group II: <b>3 months</b>", "Repeat testing required"),
 {"note": "Slide 5: document hypoxia by arterial blood gas or pulse oximetry during rest, exertion and/or sleep, performed at the time of need; saturation values are on room air. Slide 5 names the Group II blood finding &ldquo;polycythemia&rdquo; and lists only saturation for sleep and exertion; slide 6&rsquo;s picture gives hematocrit &gt; 56% and adds the arterial oxygen alternative."},
 ], "mnemonic": {"hook": "55 and 88 qualify outright (Group I, renew yearly); 56&ndash;59 or 89 need a second finding (Group II, renew every 3 months).",
  "key": [["55 / 88", "Group I at rest: arterial oxygen 55 or less, or saturation 88% or less"],
          ["56&ndash;59 / 89 + sign", "Group II: plus pulmonary hypertension, cor pulmonale or hematocrit above 56%"],
          ["Sleep", "88% or less with a drop of 5% or more"], ["Exertion", "88% or less and improves with oxygen"],
          ["12 vs 3", "Group I recertifies at 12 months, Group II at 3"]],
  "breaks": "The sleep and exertion rows use the Group I numbers but add a condition: a drop of 5% or more from baseline during sleep, improvement with oxygen during exertion."}},
{"id": "crit-l33-nasal-cannula", "label": "Nasal Cannula: Liters to Oxygen Fraction", "color": _C,
 "tag": "Criteria &middot; Lecture 33 &middot; slides 9, 11",
 "cols": ["Flow (L/min)", "Fraction of inspired oxygen (slide 9)"], "widths": ["40%", "60%"], "rows": [
 ("Room air", ".21 or 21%"), ("1", ".24 or 24%"), ("2", ".28 or 28%"), ("3", ".32 or 32%"),
 ("4", ".36 or 36%"), ("5", ".40 or 40%"), ("6", ".44 or 44%"),
 {"note": "Slide 11: low flow device, most commonly used in mild hypoxia; each 1 L increase adds 4%; the knob turns above 6 L/min but the fraction maxes out at 44%. Slide 9: <b>humidity is used with flow rates greater than 4 L/min</b>. Slide 9 prints the range as &ldquo;.24% to .44%&rdquo;; its own list shows .24 to .44, that is 24% to 44%."},
 ], "mnemonic": {"hook": "Start at 20 and add 4 per liter: 24, 28, 32, 36, 40, 44.",
  "key": [["21", "room air"], ["+4", "each liter adds 4%"], ["6 L = 44%", "the ceiling: no gain above 6 L/min"], ["&gt; 4 L", "add humidity"]],
  "breaks": "The count starts from 20, not room air&rsquo;s 21: 1 L/min is 24%, not 25%."}},
{"id": "crit-l33-simple-mask", "label": "Simple Mask: Setting to Oxygen Fraction", "color": _C,
 "tag": "Criteria &middot; Lecture 33 &middot; slide 13",
 "cols": ["Oxygen setting (slide 13)", "Fraction of inspired oxygen"], "widths": ["50%", "50%"], "rows": [
 ("5&ndash;6 L/min", "35%"), ("6&ndash;7 L/min", "40%"), ("7&ndash;8 L/min", "50%"),
 {"note": "Slide 13: low flow device, set between 5 and 10 L/min, used in mild to moderate respiratory distress. The slide 20 table gives the simple mask .35&ndash;.50 at 5&ndash;10 L/min."},
 ], "mnemonic": {"hook": "35, 40, 50: the mask&rsquo;s three steps sit between 5 and 8 L/min.",
  "key": [["5&ndash;6", "35%"], ["6&ndash;7", "40%"], ["7&ndash;8", "50%"]],
  "breaks": "The steps are uneven (+5, then +10), and the mask starts at 5 L/min, inside the cannula&rsquo;s 1&ndash;6 L/min range."}},
{"id": "crit-l33-devices", "label": "Oxygen Delivery Devices Compared", "color": _C,
 "tag": "Criteria &middot; Lecture 33 &middot; slides 8&ndash;9, 11, 13&ndash;17, 19&ndash;20",
 "cols": ["Device", "Flow type", "Fraction (slide 20)", "Flow (slide 20)", "Delivered fraction (slide 8)"],
 "widths": ["20%", "20%", "16%", "22%", "22%"], "rows": [
 ("Nasal cannula", "Low flow (slide 11)", ".24&ndash;.44 (slide 9)", "1&ndash;6 L/min (slide 9)", "Varies with respiration rate, inspiratory flow and tidal volume"),
 ("Simple mask", "Low flow (slide 13)", ".35&ndash;.50", "5&ndash;10 L/min", "Varies with respiration rate, inspiratory flow and tidal volume"),
 ("Partial rebreather mask", "&mdash;", ".40&ndash;.70", "At least 10 L/min", "Varies with patient demand"),
 ("Non-rebreather mask", "Low flow device, but with high fraction (slide 15)", ".60&ndash;1.0", "At least 10 L/min (slide 15: 10&ndash;15 L/min = 60&ndash;100%)", "Varies with patient demand"),
 ("Venturi mask", "High flow (slide 16)", ".24&ndash;.50", "Variable (slide 16: 4&ndash;10 L/min)", "<b>Precise</b>: the port chosen sets the fraction (slide 16)"),
 ("Air-entrainment nebulizer", "&mdash;", ".21&ndash;1.0", "Variable", "<b>Fixed</b> (air entrainment): does not fluctuate"),
 {"note": "Partial rebreather: slide 14 says it delivers 60&ndash;80%; the slide 20 table says .40&ndash;.70. Not tested either way."},
 {"note": "Air-entrainment nebulizer (aerosol mask, open face mask, T-piece, tracheostomy collar): slide 17 says .28&ndash;1.0, can deliver higher but <b>not recommended above .50</b>; slide 20 says .21&ndash;1.0."},
 {"note": "Slide 17: non-rebreather flow must prevent bag collapse on inspiration; Venturi total flow should be higher than inspiratory demand. Non-rebreather = severely hypoxic patients still ventilating well (slide 15); Venturi = often chronic obstructive pulmonary disease, for precision (slide 16)."},
 ], "mnemonic": {"hook": "Venturi is Precise and the entrainment nebulizer Fixed; everything else Varies. Ceiling ladder: cannula 44, mask 50, partial 70, non-rebreather 100.",
  "key": [["Cannula", ".24&ndash;.44 at 1&ndash;6 L/min"], ["Simple mask", ".35&ndash;.50 at 5&ndash;10 L/min"],
          ["Partial rebreather", ".40&ndash;.70, at least 10 L/min"], ["Non-rebreather", ".60&ndash;1.0, at least 10 L/min"],
          ["Venturi", ".24&ndash;.50, precise (ports), high flow"], ["Air-entrainment nebulizer", ".21&ndash;1.0, fixed, not above .50 (slide 17)"]],
  "breaks": "The Venturi mask and the air-entrainment nebulizer sit off the ladder: the Venturi mask is set precisely by its ports (slide 16), and the air-entrainment system gives a fixed fraction (slide 8)."}},
]

TOPICS = [
{"id": "l33-emph", "label": "★ Professor Emphasized — Who Gets Oxygen, Who Qualifies, Fire", "color": "#b8860b", "rows": [
 ["★ Indications", "<b>Hypoxia</b>; acute medical or surgical needs (perioperative, postoperative); respiratory conditions (<b>carbon monoxide poisoning</b>); special indications without hypoxia: <b>air hunger</b> (end of life) and <b>cluster headache</b>. &ldquo;One of the big things.&rdquo;"],
 ["★ Fire", "Benefit: correction of hypoxia, symptom relief, therapeutic benefit. Risk: <b>fire hazard</b> &mdash; &ldquo;probably one of the biggest risks.&rdquo; Also hypercapnia (carbon dioxide retention), mucosal irritation, vasoconstriction."],
 ["Myocardial infarction", "Vasoconstriction: <b>not given unless saturation is below 91%</b> (the slide&rsquo;s value; current guidelines use 90%)."],
 ["★ Home qualification", "Documented hypoxia by arterial blood gas or pulse oximetry at rest, with exertion and/or during sleep, <b>performed at the time of need</b>. Rest: saturation <b>&le; 88%</b> on room air or partial pressure of oxygen <b>&le; 55 mm Hg</b>. Exertion: <b>&le; 88% and improves with oxygen</b>. Sleep: <b>&le; 88% with a drop of 5% or more</b>."],
 ["Group I vs II", "<b>Group I</b> (qualifies): &le; 55 mm Hg or &le; 88% &rarr; recertify at <b>12 months</b>. <b>Group II</b> (conditional): 56&ndash;59 mm Hg or 89% <b>plus</b> pulmonary hypertension, cor pulmonale (right heart failure) or polycythemia (hematocrit above 56%) &rarr; recertify at <b>3 months</b>."],
]},
{"id": "l33-devices", "label": "Delivery Devices", "color": "#7a2d30", "rows": [
 ["Varies or fixed", "Nasal cannula, simple mask: fraction varies with respiratory rate, inspiratory flow, tidal volume. Partial rebreather, non-rebreather: varies with patient demand. <b>Air entrainment (Venturi, air-entrainment nebulizer): fixed</b>, does not fluctuate."],
 ["Nasal cannula", "<b>Low flow</b>, 1&ndash;6 L/min, <b>24&ndash;44%</b> (room air 21%; about <b>+4% per liter</b>: 1 = 24, 2 = 28, 3 = 32, 4 = 36, 5 = 40, 6 = 44). Maxes at 44% even above 6 L/min. <b>Humidity above 4 L/min.</b> Mild hypoxia; most commonly used."],
 ["Simple mask", "<b>Low flow</b>, 5&ndash;10 L/min, .35&ndash;.50 (5&ndash;6 L/min 35%, 6&ndash;7 40%, 7&ndash;8 50%). Mild to moderate respiratory distress."],
 ["Partial rebreather", "Some exhaled gas gets into the reservoir bag; <b>not commonly used</b>. Its fraction differs between slides (60&ndash;80% vs .40&ndash;.70): never tested."],
 ["Non-rebreather", "<b>Low flow device, but with a high fraction</b>: 10&ndash;15 L/min = <b>60&ndash;100%</b>. Reservoir bag + one-way valve (no inhaling exhaled air). Flow set to <b>keep the bag from collapsing</b>. <b>Severely hypoxic patients still ventilating well.</b>"],
 ["Venturi mask", "<b>High flow</b>, precise; ports change the fraction; 4&ndash;10 L/min &rarr; <b>24&ndash;50%</b>; total flow above inspiratory demand. <b>Chronic obstructive pulmonary disease</b> (precision)."],
 ["Air-entrainment nebulizer", "Aerosol mask, open face mask, T-piece, tracheostomy collar. Can deliver higher but <b>not recommended above .50</b>."],
 ["Advanced airways", "Bag-valve mask (resuscitator bag); oropharyngeal and nasopharyngeal airways; endotracheal tube, tracheostomy; tube changer and bougie; laryngeal mask airway."],
]},
{"id": "l33-neb", "label": "Nebulizers, Response &amp; Education", "color": "#b45357", "rows": [
 ["Why a nebulizer", "Liquid medication <b>directly to the airways</b>; medication chosen for the specific treatment; <b>secretion clearance</b>; <b>inhalers are challenging</b> in certain situations; <b>severe exacerbations</b> of respiratory illness."],
 ["Is it working?", "Clinical: symptoms, work of breathing, color and perfusion. Objective: saturation improves (target varies); blood gas shows a <b>higher oxygen without a higher carbon dioxide</b> and a corrected pH. Vital signs; watch for complications."],
 ["★ Home safety", "Highly flammable, compressed gas. <b>No smoking</b>; &ldquo;No Smoking&rdquo; and &ldquo;Oxygen in Use&rdquo; signs. <b>At least 10 feet</b> from heat sources (pilot lights, electric appliances, candles). <b>No petroleum products</b> (lip balms, lotions, oils, grease). Smoke and carbon monoxide alarms <b>tested monthly</b>. Proper storage and disposal."],
]},
]
