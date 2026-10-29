# -*- coding: utf-8 -*-
"""Lecture 33 vignette pool C -- Oxygen Delivery: what to avoid, escalating within and between devices,
complications on a patient with comorbidities, documenting qualification at the edge of a cutoff, and
home safety teaching (slides 3, 5-9, 11, 13, 15-18, 25).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

Written to tools/question_writing/EXPLAIN_DEEP.md: the key names the deciding clue; each wrong choice
says why it fails THIS patient, what it actually is, and a tell.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e6l33_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


AVOID = "What to avoid"
ESC = "Escalating oxygen"
HAZ = "Hazards on the patient"
HOME = "Who qualifies for home oxygen"
SAFE = "Oxygen safety at home"
EVAL = "Judging the response"

QUESTIONS = [

# ---------------------------------------------------------------- what to avoid
V(AVOID, IO_A,
  "A 78-year-old man with chronic obstructive pulmonary disease has mild hypoxia, saturation 87%, during a cold. A student suggests a non-rebreather mask at 15 L/min \"to be safe.\" Why should that be avoided?",
  [["It is meant for severe hypoxia",
    "Correct. His hypoxia is mild at 87%, and a non-rebreather mask is used in severely hypoxic patients who are still ventilating well, delivering 60-100% at 10-15 L/min. For mild hypoxia the nasal cannula is the most commonly used device, so the non-rebreather overshoots his need."],
   ["It cannot raise his saturation",
    "A non-rebreather can raise his saturation; at 10-15 L/min it delivers 60-100%. The problem is that its high fraction is meant for severe hypoxia, and his is mild at 87%. Tell: this mask is powerful, which is why it is kept for severe hypoxia.", "reversed direction or value"],
   ["It causes vasoconstriction in the lungs",
    "Vasoconstriction is a risk of oxygen therapy in general, flagged for myocardial infarction, not a reason tied to this mask. He has no cardiac event, and his issue is a device too strong for mild hypoxia. Tell: vasoconstriction goes with a myocardial infarction; severity decides the device.", "adjacent fact"],
   ["It is a fire hazard in hospitals",
    "Fire is a listed hazard of any oxygen therapy, whichever device is used, so it is not a reason to avoid this mask in particular. The reason here is that the non-rebreather is for severe hypoxia and his is mild. Tell: a hazard shared by every device cannot single out one of them.", "adjacent fact"]],
  Cs(3, 11, 15), "avoid", "avoid"),

V(AVOID, IO_A,
  "A 71-year-old woman with chronic obstructive pulmonary disease has a myocardial infarction. Her saturation is 93% on room air. A colleague wants to start oxygen by nasal cannula. Which is the right call?",
  [["Hold oxygen at a saturation of 93%",
    "Correct. Oxygen is not given in a myocardial infarction unless the saturation is below 91%, because of vasoconstriction. Her saturation of 93% is above that, so oxygen is held."],
   ["Start the nasal cannula at 2 L/min",
    "A cannula at 2 L/min (about 28%) is a low dose, but the dose is not the issue. In a myocardial infarction oxygen is withheld unless the saturation is below 91%, and hers is 93%. Tell: the threshold decides first, then the device.", "ruled out by a stated finding"],
   ["Start a Venturi mask for her lung disease",
    "A Venturi mask is often used in chronic obstructive pulmonary disease for its precision, but precision matters only when oxygen is needed. Her saturation of 93% is above the 91% line in a myocardial infarction. Tell: choosing a device comes after deciding that oxygen is needed.", "adjacent fact"],
   ["Start a non-rebreather mask",
    "A non-rebreather delivers 60-100% and is used in severely hypoxic patients. She is at 93%, above the 91% line in a myocardial infarction, so no device is called for. Tell: no hypoxia means no oxygen, and certainly not a high-fraction mask.", "wrong stage or severity"]],
  Cs(3, 9, 15, 16), "avoid", "avoid"),

V(AVOID, IO_A,
  "A 67-year-old man has a myocardial infarction and is placed on oxygen in the ambulance although his saturation was 98%. Which effect of oxygen makes this a problem?",
  [["Vasoconstriction",
    "Correct. His saturation was 98%, so he was not hypoxic. Oxygen is not given in a myocardial infarction unless the saturation is below 91%, because oxygen causes vasoconstriction. Giving it to a man with a normal saturation exposes him to that effect without benefit."],
   ["Carbon dioxide retention",
    "Carbon dioxide retention is a listed hazard of oxygen, but it is not the reason oxygen is withheld in a myocardial infarction; that reason is vasoconstriction. Tell: the myocardial infarction rule points to vasoconstriction.", "adjacent fact"],
   ["Mucosal irritation",
    "Mucosal irritation is the dryness and soreness of the nose from oxygen, especially without humidity at higher flows. It does not explain why oxygen is avoided in a myocardial infarction. Tell: irritation is local; vasoconstriction is the cardiac concern.", "adjacent fact"],
   ["Fire risk",
    "Fire risk is real around any oxygen, but it does not explain why oxygen is withheld at a saturation of 98% in a myocardial infarction. Tell: the myocardial infarction caution is about vasoconstriction, not ignition.", "adjacent fact"]],
  Cs(3, 9), "complication", "complication"),

V(AVOID, IO_D,
  "A 54-year-old man with severe pneumonia is on an aerosol mask from an air-entrainment nebulizer. The team wants to raise its fraction to 0.80. Why is that setting a concern?",
  [["It is not recommended above 0.50",
    "Correct. A fixed-fraction air-entrainment nebulizer can deliver higher fractions, but setting above 0.50 is not recommended. His team wants 0.80, which is beyond that ceiling, so it is a concern even though his pneumonia is severe."],
   ["It cannot go above 0.28",
    "This device is not capped at 0.28. It can deliver higher fractions, and the concern is the specific recommendation not to go above 0.50. Tell: the limit is a recommended ceiling of 0.50, not 0.28.", "reversed direction or value"],
   ["It is recommended above 0.50",
    "The recommendation is the opposite: use above 0.50 is not recommended. Reading it as recommended would invert the ceiling. Tell: 0.50 is a ceiling, not a floor.", "reversed direction or value"],
   ["It changes with his breathing rate",
    "An air-entrainment system gives a fixed fraction that does not fluctuate with patient demand. A fraction that follows breathing rate describes the cannula, simple mask or non-rebreather. Tell: air entrainment is steady; the concern with 0.80 is the recommended ceiling.", "confused mechanism or drug class"]],
  C(17), "avoid", "avoid"),

V(AVOID, IO_G,
  "A 72-year-old woman starting home oxygen loves candlelit dinners and keeps several candles on her dining table, where she sits with her concentrator tubing. Which teaching applies?",
  [["Keep oxygen at least 10 feet from the candles",
    "Correct. Home oxygen teaching is to keep oxygen at least 10 feet from heat sources, and candles are listed alongside pilot lights and electric appliances. She sits at the table with her concentrator tubing, so the candles must be at least 10 feet away."],
   ["Candles are safe if the flow is low",
    "A low flow does not remove the hazard. Oxygen is highly flammable, and candles are a heat source to keep at least 10 feet away. Tell: the distance rule does not depend on the flow setting.", "common lay belief"],
   ["Use scented candles instead",
    "Scented candles are still candles. They are a flame and a heat source, and the teaching is to keep oxygen at least 10 feet away from candles. Tell: the type of candle is irrelevant; any flame counts.", "common lay belief"],
   ["Keep the candles 2 feet away",
    "Two feet is too close. The minimum distance from heat sources, including candles, is at least 10 feet. Tell: the number is 10 feet, so a smaller number fails.", "reversed direction or value"]],
  C(7), "education", "avoid"),

V(AVOID, IO_G,
  "A 66-year-old man on home oxygen restores old cars in his garage and rubs grease off his hands with an oil-based cleanser while wearing his cannula. Which teaching applies?",
  [["Avoid petroleum-based oils and grease",
    "Correct. Home oxygen teaching is to avoid petroleum-based products such as lip balms, lotions, oils and grease. He is wearing his cannula while rubbing grease off with an oil-based cleanser, so he should avoid those petroleum oils and grease."],
   ["Turn the flow up while working",
    "Turning the flow up does not remove the petroleum product; the teaching is to avoid petroleum-based oils and grease, not to change the flow. Tell: the fix is to change the product, not the oxygen setting.", "reversed direction or value"],
   ["Wear a simple mask in the garage",
    "A simple mask is a low flow device for mild to moderate respiratory distress. He has no respiratory problem described, and changing the mask would not address the grease. Tell: his hazard is the product on his hands.", "adjacent fact"],
   ["Use a Venturi mask when working",
    "A Venturi mask is a high flow device that gives a precise fraction, often used in chronic obstructive pulmonary disease. It would not remove the petroleum product hazard. Tell: the teaching concerns what touches the oxygen, not which mask he wears.", "adjacent fact"]],
  Cs(7, 13, 16), "education", "avoid"),

# ---------------------------------------------------------------- escalating oxygen
V(ESC, IO_F,
  "A 70-year-old man with chronic obstructive pulmonary disease is on a Venturi mask set at 28%. His saturation is still below his target, and he is comfortable and alert. Which adjustment raises his fraction precisely?",
  [["Change to a higher-fraction port",
    "Correct. A Venturi mask changes its fraction through different ports (24-50% when flow is adjusted from 4-10 L/min). He is stable and comfortable at 28% but below his target, so the precise adjustment is a higher-fraction port. It keeps the fraction fixed."],
   ["Switch to a non-rebreather at 15 L/min",
    "A non-rebreather at 15 L/min would jump to 60-100% and vary with his demand. He is alert and comfortable with chronic obstructive pulmonary disease, so he needs a small, precise step. Tell: the Venturi mask adjusts in small fixed steps; the non-rebreather jumps.", "wrong stage or severity"],
   ["Add a reservoir bag to the mask",
    "A reservoir bag converts a mask into a non-rebreather, which varies with demand and is for severe hypoxia. Adding one to a Venturi mask would not give a precise fraction. Tell: ports set a fixed fraction; a bag raises the fraction unpredictably.", "confused mechanism or drug class"],
   ["Switch to a nasal cannula at 2 L/min",
    "A nasal cannula at 2 L/min delivers about 28%, which is the fraction he is already getting, and it varies with his breathing. It would not raise his fraction precisely. Tell: a cannula varies with breathing; a Venturi port is fixed.", "reversed direction or value"]],
  C(16), "escalation", "next step"),

V(ESC, IO_F,
  "A 62-year-old woman with pneumonia is on a Venturi mask. She is breathing fast and deep, and her saturation dips each time she takes a big breath. Which dosing principle is being violated?",
  [["Total flow must exceed inspiratory demand",
    "Correct. The Venturi mask is an air-entrainment device that delivers a fixed fraction only if the total flow stays higher than her inspiratory demand. She is breathing fast and deep and her saturation dips with big breaths, which suggests her demand exceeds the flow."],
   ["The bag must not collapse on inspiration",
    "Preventing bag collapse on inspiration is the dosing principle for the non-rebreather mask. A Venturi mask has no reservoir bag. Tell: bag collapse belongs to the non-rebreather; total flow versus demand belongs to the Venturi mask.", "adjacent fact"],
   ["Humidity is needed above 4 L/min",
    "Humidity is used with nasal cannula flow rates greater than 4 L/min. It is a nasal cannula principle and does not explain her saturation dipping on deep breaths. Tell: humidity protects the nose; flow versus demand keeps the fraction fixed.", "adjacent fact"],
   ["The fraction must stay under 0.50",
    "Staying under 0.50 is the recommendation for the air-entrainment nebulizer. The Venturi mask's own range is 24-50%, and her problem is the dips with each breath, not the fraction setting. Tell: the ceiling of 0.50 is about the nebulizer; her dips point to flow versus demand.", "adjacent fact"]],
  C(17), "agent/regimen", "next step"),

V(ESC, IO_F,
  "A 58-year-old man with bronchitis is on a nasal cannula at 6 L/min with a saturation of 89%. He now has mild to moderate respiratory distress but is ventilating well. Which step fits his severity?",
  [["Change to a simple mask at 5 to 10 L/min",
    "Correct. He has mild to moderate respiratory distress, and his saturation of 89% persists on a cannula at 6 L/min, near the cannula's limit of 44%. A simple mask, a low flow device set at 5-10 L/min, is the step for this severity."],
   ["Turn the cannula to 10 L/min",
    "Turning a cannula to 10 L/min does not raise the fraction past its maximum of 44%, which is reached at 6 L/min. He is already there. Tell: if the cannula is at its ceiling, change the device.", "reversed direction or value"],
   ["Go straight to a bag-valve mask",
    "A bag-valve mask is a resuscitator for a patient who is not ventilating. He is ventilating well, with only mild to moderate distress. Tell: the resuscitator is for failed ventilation, not for this severity.", "wrong stage or severity"],
   ["Stop oxygen and recheck in an hour",
    "Stopping oxygen at 89% with distress would leave him hypoxic. He needs more oxygen, not less, and should move to the next device. Tell: persistent hypoxia with distress calls for escalation, not for a pause.", "wrong stage or severity"]],
  C(13), "escalation", "next step"),

V(ESC, IO_B,
  "A 46-year-old woman with mild hypoxia, saturation 89%, had both nostrils packed for a severe nosebleed. She is comfortable otherwise. Which device suits her mild hypoxia with her nose blocked?",
  [["Simple mask",
    "Correct. Both nostrils are packed, so a nasal cannula would not deliver. Her hypoxia is mild at 89%, and she is comfortable otherwise. A simple mask, a low flow device that covers the nose and mouth, can still deliver oxygen, at 5-10 L/min."],
   ["Nasal cannula at 2 L/min",
    "A nasal cannula delivers through the nostrils, and both are packed, so oxygen cannot enter. The cannula is a common choice for mild hypoxia, but it relies on a patent nose. Tell: when the nose is blocked, use a device that covers the mouth.", "ruled out by a stated finding"],
   ["Trach collar",
    "A trach collar is an air-entrainment nebulizer interface for a patient with a tracheostomy. She has no tracheostomy. Tell: the collar fits a stoma; the mask fits the face.", "ruled out by a stated finding"],
   ["Non-rebreather at 15 L/min",
    "A non-rebreather at 15 L/min also covers the face, but it is for severely hypoxic patients who are still ventilating well. Her hypoxia is mild at 89%, so it overshoots. Tell: match the device to severity: mild to moderate points to the simple mask.", "wrong stage or severity"]],
  Cs(11, 13, 15, 19), "agent/regimen", "treatment"),

V(ESC, IO_B,
  "A 57-year-old man with a chronic lung disease flare needs both inhaled medication by nebulizer and supplemental oxygen. He has no tracheostomy. Which air-entrainment interface over his face suits him?",
  [["Aerosol mask",
    "Correct. He needs a nebulizer for his inhaled medication along with oxygen, and he has no tracheostomy. The aerosol mask is an air-entrainment nebulizer interface that fits over the face, so it delivers oxygen and nebulized medication together."],
   ["Trach collar",
    "A trach collar is the air-entrainment nebulizer interface that fits a tracheostomy. He has no tracheostomy, so the collar would not suit his face. Tell: the collar goes on a stoma; the aerosol mask goes over the face.", "ruled out by a stated finding"],
   ["Non-rebreather mask",
    "A non-rebreather mask delivers oxygen through a reservoir bag and one-way valve, but it is not an air-entrainment nebulizer interface. It does not deliver nebulized medication. Tell: the reservoir bag means no nebulizer; the aerosol mask is the nebulizer interface.", "adjacent fact"],
   ["Nasal cannula",
    "A nasal cannula is a low flow device that delivers oxygen only, and it is not an air-entrainment nebulizer interface. Tell: the cannula supplies oxygen; the aerosol mask supplies oxygen and nebulized medication.", "adjacent fact"]],
  C(18), "agent/regimen", "treatment"),

# ---------------------------------------------------------------- hazards with comorbidities
V(HAZ, IO_A,
  "A 76-year-old woman with chronic obstructive pulmonary disease is put on a simple mask at 10 L/min overnight. By morning she is hard to wake and her arterial carbon dioxide is much higher than her baseline. Which hazard of oxygen therapy occurred?",
  [["Hypercapnia from carbon dioxide retention",
    "Correct. A woman with chronic obstructive pulmonary disease on a simple mask at 10 L/min becomes hard to wake overnight with arterial carbon dioxide far above her baseline. That is carbon dioxide retention (hypercapnia), a listed hazard of oxygen therapy."],
   ["Mucosal irritation",
    "Mucosal irritation is dryness or soreness of the nose and airway from oxygen. It would not make her hard to wake or raise her arterial carbon dioxide. Tell: irritation is local; hypercapnia causes sleepiness with a rising carbon dioxide.", "adjacent fact"],
   ["Vasoconstriction",
    "Vasoconstriction is the listed concern when oxygen is given in a myocardial infarction. She has no cardiac event, and vasoconstriction would not raise her carbon dioxide. Tell: vasoconstriction goes with a myocardial infarction; chronic lung disease goes with hypercapnia.", "adjacent fact"],
   ["Hypoxia from too little flow",
    "Hypoxia from too little flow would be a falling saturation, not a rising carbon dioxide. A simple mask at 10 L/min is the top of its range and delivers a fraction of 35-50%. Tell: her carbon dioxide rose, so oxygen delivery caused the problem.", "reversed direction or value"]],
  C(3), "complication", "complication"),

V(HAZ, IO_A,
  "An 80-year-old man on home oxygen at 5 L/min by nasal cannula with no humidifier complains of a sore, dry nose and occasional bleeding. Which change addresses the cause?",
  [["Add humidity to the oxygen",
    "Correct. He is on 5 L/min by nasal cannula with no humidifier, and has a sore, dry nose with bleeding. That is mucosal irritation. Humidity is used with cannula flow rates greater than 4 L/min, so adding humidity to the oxygen treats the cause."],
   ["Increase the flow to 6 L/min",
    "Raising the flow to 6 L/min keeps him above 4 L/min, where humidity is already needed and he has none. A higher flow leaves the missing humidity in place. Tell: fix the humidity, not the flow.", "reversed direction or value"],
   ["Apply a petroleum lip and nose balm",
    "A petroleum-based balm is on the list of products to avoid with home oxygen, because oxygen is highly flammable. It would not be an appropriate treatment for his nose. Tell: petroleum products stay away from oxygen.", "ruled out by a stated finding"],
   ["Switch to a non-rebreather mask",
    "A non-rebreather mask is a high-fraction device for severely hypoxic patients who are still ventilating well. He has a sore nose, not worsening hypoxia, and the mask would not solve it. Tell: his problem is dryness at a flow above 4 L/min.", "wrong stage or severity"]],
  Cs(3, 7, 9, 15), "complication", "treatment"),

# ---------------------------------------------------------------- qualification at the edge
V(HOME, IO_F,
  "A 69-year-old woman with chronic lung disease is assessed for home oxygen before discharge. Her resting room-air saturation is exactly 88%, and she has no other findings. What is her qualification?",
  [["Group I, recertified at 12 months",
    "Correct. Group I qualifies at a resting room-air saturation of 88% or less, and hers is exactly 88%, which meets the cutoff. Group I patients are recertified at 12 months, and no comorbidity is needed."],
   ["Group II, recertified at 3 months",
    "Group II is for a saturation of 89% (or arterial oxygen pressure of 56-59 mm Hg) plus pulmonary hypertension, cor pulmonale or a hematocrit above 56%, recertified at 3 months. Her 88% already meets Group I. Tell: 88% or less is Group I; 89% needs a comorbidity.", "adjacent fact"],
   ["Not qualified without a comorbidity",
    "A comorbidity is needed only when the saturation is 89%. At 88% she meets the Group I rest criterion as is. Tell: the boundary 88% counts; the comorbidity requirement begins at 89%.", "wrong stage or severity"],
   ["Qualified for exertion oxygen",
    "Exertion oxygen requires a saturation of 88% or less with activity that improves with oxygen. No exertion testing is described, and her resting value already qualifies her at rest. Tell: she qualifies at rest, which is a stronger finding.", "adjacent fact"]],
  C(6), "test finding", "test"),

V(HOME, IO_F,
  "A 74-year-old man with chronic obstructive pulmonary disease has poor finger perfusion, and the pulse oximeter will not give a steady reading. His arterial oxygen pressure is 55 mm Hg on room air at rest. What is his home oxygen status?",
  [["Qualifies in Group I",
    "Correct. Documentation can use an arterial blood gas or pulse oximetry. An arterial oxygen pressure of 55 mm Hg or less qualifies at Group I, and his is 55, so he qualifies without the oximeter. Group I is recertified at 12 months."],
   ["Qualifies in Group II",
    "Group II is for an arterial oxygen pressure of 56-59 mm Hg plus a comorbidity. His is 55, so he meets the Group I threshold directly. Tell: 55 or less is Group I; 56-59 is Group II.", "adjacent fact"],
   ["Cannot qualify without oximetry",
    "The pulse oximeter is only one way to document hypoxia. The arterial blood gas is the other, and an arterial oxygen pressure of 55 mm Hg or less is the qualifying value. Tell: when oximetry fails, the blood gas can qualify him.", "ruled out by a stated finding"],
   ["Does not qualify at 55 mm Hg",
    "His arterial oxygen pressure of 55 mm Hg is exactly at the qualifying value, since the criterion is 55 mm Hg or less, which includes 55. Tell: the cutoff includes the number 55, so he qualifies in Group I.", "reversed direction or value"]],
  C(5), "test finding", "test"),

V(HOME, IO_F,
  "A 70-year-old woman with interstitial lung disease, pulmonary hypertension and a hematocrit of 52% has a resting room-air saturation of 89%. Which finding makes her qualify?",
  [["Her pulmonary hypertension",
    "Correct. Her resting saturation of 89% is just above the Group I cutoff of 88%, so she needs a comorbidity. Pulmonary hypertension is one of the listed qualifying findings, so it makes her qualify as Group II."],
   ["Her hematocrit of 52%",
    "A hematocrit of 52% is below the threshold of above 56% needed for polycythemia to count. It does not qualify her. Tell: the hematocrit must be above 56%.", "reversed direction or value"],
   ["Her interstitial lung disease",
    "Interstitial lung disease is not one of the qualifying comorbidities. The list is pulmonary hypertension, cor pulmonale and a hematocrit above 56%. Tell: it is the complications, not the lung diagnosis, that count.", "adjacent fact"],
   ["Nothing; 89% does not qualify",
    "At 89% alone she would not qualify, but she does not stand on 89% alone. Her pulmonary hypertension adds the comorbidity that makes the saturation qualify. Tell: 89% plus a listed comorbidity qualifies.", "ruled out by a stated finding"]],
  C(6), "risk factors", "test"),

# ---------------------------------------------------------------- safety teaching
V(SAFE, IO_G,
  "A 79-year-old woman using home oxygen keeps an electric space heater beside her recliner, where she sits with her tubing. Which teaching applies?",
  [["Keep oxygen at least 10 feet from the heater",
    "Correct. Home oxygen teaching is to keep oxygen at least 10 feet from heat sources, including electric appliances as well as pilot lights and candles. A space heater beside her recliner is a heat source, so she must keep her oxygen at least 10 feet away."],
   ["A heater is safe because it has no flame",
    "Lacking a flame does not make a heater safe. Electric appliances are listed heat sources, and oxygen is highly flammable. Tell: the rule covers electric appliances, not just flames.", "common lay belief"],
   ["Lower her flow while the heater runs",
    "Lowering her flow does not address the hazard. The teaching is about distance, at least 10 feet from heat sources, and has nothing to do with the flow rate. Tell: distance protects, not the knob.", "common lay belief"],
   ["Keep the heater 3 feet away",
    "Three feet is far too close to an electric heater. The minimum distance from heat sources is at least 10 feet. Tell: the number to remember is 10 feet, so any smaller distance fails the teaching.", "reversed direction or value"]],
  C(7), "education", "education"),

V(SAFE, IO_G,
  "A 71-year-old man starting home oxygen asks why he must be so careful at home if oxygen is \"just air.\" Which property of oxygen underlies the safety teaching?",
  [["It is highly flammable",
    "Correct. Oxygen is highly flammable, which is why home oxygen teaching includes no smoking in the home, staying away from heat sources, avoiding petroleum products and posting signs. Oxygen is not just air, and fire is a listed hazard."],
   ["It is toxic to breathe for visitors",
    "Oxygen is not described as toxic to visitors. The hazards listed are carbon dioxide retention, fire, mucosal irritation and vasoconstriction. Tell: the home safety teaching rests on flammability.", "common lay belief"],
   ["It is heavier than water",
    "Oxygen being heavier than water is not a property stated and has no bearing on the teaching. The reason for the care is that oxygen is highly flammable. Tell: the key property is flammability.", "common lay belief"],
   ["It turns into carbon monoxide",
    "Oxygen does not turn into carbon monoxide. Carbon monoxide appears in the teaching only as a reason for working carbon monoxide alarms. Tell: alarms detect carbon monoxide; flammability is the property of oxygen.", "confused mechanism or drug class"]],
  C(7), "education", "education"),

# ---------------------------------------------------------------- judging the response
V(EVAL, IO_E,
  "A 64-year-old man with pneumonia has an arterial blood gas before and after starting oxygen. After oxygen, his arterial oxygen pressure is higher, his carbon dioxide is unchanged, and his pH has returned toward normal. How is this response read?",
  [["A good response",
    "Correct. A good response is an increase in arterial oxygen pressure without an increase in arterial carbon dioxide, plus correction of the pH. His oxygen pressure rose, his carbon dioxide stayed unchanged, and his pH moved back toward normal, which meets all three."],
   ["Carbon dioxide retention",
    "Carbon dioxide retention would show a rising arterial carbon dioxide. His carbon dioxide is unchanged, so there is no sign of retention. Tell: unchanged carbon dioxide is what a good response requires.", "ruled out by a stated finding"],
   ["No response",
    "His arterial oxygen pressure rose and his pH corrected, which are the objective signs of response. There is a response. Tell: rising oxygen pressure with correcting pH is the pattern of a good response.", "reversed direction or value"],
   ["A response if saturation reaches 100%",
    "A saturation of 100% is not required. The saturation is judged against a target that varies with the patient, and his gas already shows a good response. Tell: the target varies, so 100% is not the goal.", "common lay belief"]],
  C(25), "test finding", "test"),

V(EVAL, IO_E,
  "A 52-year-old woman with asthma is started on oxygen. She says she feels better, but her lips remain dusky, her accessory muscles are still working hard, and her saturation has not moved. How should her response be judged?",
  [["Not yet adequate on clinical and objective measures",
    "Correct. She feels better, but her lips are still dusky, her accessory muscles still work hard, and her saturation has not moved. Response is judged by symptoms, work of breathing, color and perfusion plus objective data. Most of those have not improved, so it is not yet adequate."],
   ["Adequate, because she feels better",
    "Feeling better is only one of the clinical measures. Work of breathing and color have not improved, and the saturation has not moved. Tell: symptom relief alone does not make a response adequate.", "ruled out by a stated finding"],
   ["Adequate, because oxygen is running",
    "Oxygen running is not a response. The response is judged by what happens to the patient: symptoms, work of breathing, color and objective saturation. Tell: delivery is not the same as effect.", "common lay belief"],
   ["Cannot be judged without a chest film",
    "A chest film is not part of the listed response measures. The clinical and objective data she already has show the response is inadequate. Tell: the measures are symptoms, work of breathing, color, saturation and blood gas values.", "adjacent fact"]],
  C(25), "manifestation", "test"),

V(EVAL, IO_E,
  "A 60-year-old man with heart failure is on oxygen while his fluid overload is treated. Over two days his breathing eases, his saturation stays at target, and his vital signs settle. Which ongoing step is part of evaluating his oxygen therapy?",
  [["Keep monitoring for complications",
    "Correct. Evaluating response ends with vital signs and further monitoring for complications. His breathing has eased and his saturation holds, but he remains on oxygen, so the hazards of oxygen therapy still need watching."],
   ["Stop checking his saturation",
    "Stopping saturation checks would drop the objective data used to judge response. The target varies, but the measurement continues. Tell: stable results are a reason to keep monitoring, not to stop.", "wrong stage or severity"],
   ["Raise his flow to secure the gains",
    "Raising the flow when he is already at target would add oxygen he does not need and risk its hazards. His saturation stays at target. Tell: at target, the plan is to monitor, not to increase.", "reversed direction or value"],
   ["Start home oxygen qualification today",
    "Home oxygen qualification is performed at the time of need, with documentation of hypoxia at rest, exertion or sleep, when a patient is going home. He is still in treatment for fluid overload. Tell: qualification is about home coverage, not about evaluating his current response.", "wrong stage or severity"]],
  C(25), "complication", "next step"),
]
