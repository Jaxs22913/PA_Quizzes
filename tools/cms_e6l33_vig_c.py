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
  [["It risks carbon dioxide retention",
    "Correct. Hypercapnia, carbon dioxide retention, is a listed hazard of oxygen therapy, and a non-rebreather gives 60% to 100%, far more than his mild hypoxia needs. His disease is why a precise, lower fraction (the Venturi mask) is often used instead."],
   ["It cannot raise his saturation",
    "A non-rebreather can raise saturation powerfully, 60% to 100% at 10 to 15 L/min. The problem is the opposite: too much oxygen for mild hypoxia, risking carbon dioxide retention in a patient with this disease.", "reversed direction or value"],
   ["It causes vasoconstriction in the lungs",
    "Vasoconstriction is the hazard behind withholding oxygen in myocardial infarction, not the concern here. The concern for him is carbon dioxide retention from excess oxygen.", "adjacent fact"],
   ["It is a fire hazard in hospitals",
    "Fire is a hazard wherever oxygen is used, home included, and it is not why this device is wrong for him. The issue is carbon dioxide retention from an unnecessarily high fraction.", "adjacent fact"]],
  C(3), "avoid", "avoid"),

V(AVOID, IO_A,
  "A 71-year-old woman with chronic obstructive pulmonary disease has a myocardial infarction. Her saturation is 93% on room air. A colleague wants to start oxygen by nasal cannula. Which is the right call?",
  [["Hold oxygen at a saturation of 93%",
    "Correct. Oxygen causes vasoconstriction, so in myocardial infarction it is not given unless saturation is below 91%; at 93% she is above the threshold, and her lung disease adds the risk of carbon dioxide retention."],
   ["Start the nasal cannula at 2 L/min",
    "Low flow is still oxygen. In myocardial infarction oxygen is held unless saturation is below 91%; her 93% is above that, so it would add vasoconstriction without correcting hypoxia.", "ruled out by a stated finding"],
   ["Start a Venturi mask for her lung disease",
    "Her lung disease is a reason to choose precision when she needs oxygen, not a reason to start it. In infarction, oxygen waits until saturation is below 91%.", "adjacent fact"],
   ["Start a non-rebreather mask",
    "A non-rebreather is for severe hypoxia in a patient ventilating well, and she is not hypoxic by the infarction rule. It would also risk carbon dioxide retention with her lung disease.", "wrong stage or severity"]],
  C(3), "avoid", "avoid"),

V(AVOID, IO_A,
  "A 67-year-old man has a myocardial infarction and is placed on oxygen in the ambulance although his saturation was 98%. Which effect of oxygen makes this a problem?",
  [["Vasoconstriction",
    "Correct. Vasoconstriction is a listed hazard of oxygen therapy and the reason oxygen is not given in myocardial infarction unless saturation is below 91%; at 98% he gains nothing while his vessels constrict."],
   ["Carbon dioxide retention",
    "Carbon dioxide retention is an oxygen hazard, typically in a patient prone to retaining it, but it is not the reason given for the infarction rule. That rule rests on vasoconstriction.", "adjacent fact"],
   ["Mucosal irritation",
    "Mucosal irritation is a nuisance hazard of dry oxygen, not the infarction concern. Oxygen in a non-hypoxic infarction patient is a problem because of vasoconstriction.", "adjacent fact"],
   ["Fire risk",
    "Fire is oxygen's biggest safety hazard but is unrelated to the infarction rule. The physiologic problem in a non-hypoxic infarction is vasoconstriction.", "adjacent fact"]],
  C(3), "complication", "complication"),

V(AVOID, IO_D,
  "A 54-year-old man with severe pneumonia is on an aerosol mask from an air-entrainment nebulizer. The team wants to raise its fraction to 0.80. Why is that setting a concern?",
  [["It is not recommended above 0.50",
    "Correct. An air-entrainment nebulizer (aerosol mask, open face mask, T-piece, trach collar) can deliver a higher fraction, but it is not recommended above 0.50; a patient needing about 0.80 needs a different device."],
   ["It cannot go above 0.28",
    "The air-entrainment nebulizer can deliver well above 0.28; the limit is a recommendation not to exceed 0.50. Setting 0.80 is the concern.", "reversed direction or value"],
   ["It is recommended above 0.50",
    "The recommendation runs the other way: an air-entrainment nebulizer is not recommended above 0.50. At 0.80 it is outside that advice.", "reversed direction or value"],
   ["It changes with his breathing rate",
    "A varying fraction describes the nasal cannula and simple mask. The air-entrainment issue at 0.80 is that it is not recommended above 0.50.", "confused mechanism or drug class"]],
  C(17), "avoid", "avoid"),

V(AVOID, IO_G,
  "A 72-year-old woman starting home oxygen loves candlelit dinners and keeps several candles on her dining table, where she sits with her concentrator tubing. Which teaching applies?",
  [["Keep oxygen at least 10 feet from the candles",
    "Correct. Home oxygen must be kept at least 10 feet from heat sources such as pilot lights, electric appliances and candles, because oxygen is highly flammable; her habit puts the flame at her tubing."],
   ["Candles are safe if the flow is low",
    "Any flow of oxygen feeds a flame; a low flow does not make candles safe. Oxygen should be kept at least 10 feet from candles and other heat sources.", "common lay belief"],
   ["Use scented candles instead",
    "The scent changes nothing about the flame. The rule is at least 10 feet between oxygen and heat sources like candles.", "common lay belief"],
   ["Keep the candles 2 feet away",
    "Two feet is far inside the safety distance. Oxygen should be at least 10 feet from candles.", "reversed direction or value"]],
  C(7), "education", "avoid"),

V(AVOID, IO_G,
  "A 66-year-old man on home oxygen restores old cars in his garage and rubs grease off his hands with an oil-based cleanser while wearing his cannula. Which teaching applies?",
  [["Avoid petroleum-based oils and grease",
    "Correct. Patients on oxygen should avoid petroleum-based products, including oils and grease as well as lip balms and lotions, because oxygen is highly flammable and these products can feed a fire."],
   ["Turn the flow up while working",
    "More oxygen near grease adds fuel to a possible fire. The teaching is to avoid petroleum-based oils and grease while using oxygen.", "reversed direction or value"],
   ["Wear a simple mask in the garage",
    "Changing the device does not remove the fire risk from petroleum products. The teaching is to avoid oils and grease with oxygen.", "adjacent fact"],
   ["Use a Venturi mask when working",
    "A Venturi mask sets a precise fraction; it does not make grease safe. Petroleum-based oils and grease should be avoided with oxygen.", "adjacent fact"]],
  C(7), "education", "avoid"),

# ---------------------------------------------------------------- escalating oxygen
V(ESC, IO_F,
  "A 70-year-old man with chronic obstructive pulmonary disease is on a Venturi mask set at 28%. His saturation is still below his target, and he is comfortable and alert. Which adjustment raises his fraction precisely?",
  [["Change to a higher-fraction port",
    "Correct. On a Venturi mask, different ports change the fraction delivered, from 24% to 50%; moving up a port raises his fraction precisely, keeping the advantage that makes it a common choice in this disease."],
   ["Switch to a non-rebreather at 15 L/min",
    "A non-rebreather jumps to 60% to 100% and its delivery varies with demand, losing the precision his disease calls for. A higher Venturi port raises the fraction in a controlled step.", "wrong stage or severity"],
   ["Add a reservoir bag to the mask",
    "Reservoir bags belong to the partial and non-rebreather masks, not the Venturi mask. The Venturi fraction is changed by its ports.", "confused mechanism or drug class"],
   ["Switch to a nasal cannula at 2 L/min",
    "A cannula at 2 L/min gives about 28%, no higher than now, and its fraction varies with breathing. The precise step up is a higher Venturi port.", "reversed direction or value"]],
  C(16), "escalation", "next step"),

V(ESC, IO_F,
  "A 62-year-old woman with pneumonia is on a Venturi mask. She is breathing fast and deep, and her saturation dips each time she takes a big breath. Which dosing principle is being violated?",
  [["Total flow must exceed inspiratory demand",
    "Correct. For a Venturi mask, the total flow should be higher than the patient's inspiratory demand; her fast, deep breaths outstrip it, so room air dilutes the set fraction and her saturation dips."],
   ["The bag must not collapse on inspiration",
    "Preventing bag collapse is the non-rebreather's dosing rule; a Venturi mask has no reservoir bag. Her dips mean total flow is below her inspiratory demand.", "adjacent fact"],
   ["Humidity is needed above 4 L/min",
    "Humidity above 4 L/min applies to the nasal cannula and prevents mucosal irritation; it does not explain saturation dips with big breaths. The Venturi rule is total flow above inspiratory demand.", "adjacent fact"],
   ["The fraction must stay under 0.50",
    "The 0.50 ceiling is the air-entrainment nebulizer's recommendation. Her problem is total flow below her inspiratory demand on the Venturi mask.", "adjacent fact"]],
  C(17), "agent/regimen", "next step"),

V(ESC, IO_F,
  "A 58-year-old man with bronchitis is on a nasal cannula at 6 L/min with a saturation of 89%. He now has mild to moderate respiratory distress but is ventilating well. Which step fits his severity?",
  [["Change to a simple mask at 5 to 10 L/min",
    "Correct. The cannula is at its 6 L/min, 44% ceiling, and he now has mild to moderate respiratory distress, the simple mask's indication; at 5 to 10 L/min it gives about 35% to 50%."],
   ["Turn the cannula to 10 L/min",
    "Above 6 L/min the cannula stays at about 44%, so more flow adds nothing. His mild to moderate distress fits a simple mask.", "reversed direction or value"],
   ["Go straight to a bag-valve mask",
    "A bag-valve mask gives assisted breaths to a patient who cannot ventilate; he is ventilating well. A simple mask matches mild to moderate distress.", "wrong stage or severity"],
   ["Stop oxygen and recheck in an hour",
    "Stopping oxygen in a patient who is hypoxic and in distress leaves him worse. He needs escalation from the maxed-out cannula to a simple mask.", "wrong stage or severity"]],
  C(13), "escalation", "next step"),

V(ESC, IO_B,
  "A 46-year-old woman with mild hypoxia, saturation 89%, had both nostrils packed for a severe nosebleed. She is comfortable otherwise. Which low flow device can still deliver her oxygen?",
  [["Simple mask",
    "Correct. With both nostrils packed, a nasal cannula has no open path; a simple mask covers nose and mouth and is a low flow device (5 to 10 L/min, about 35% to 50%) suitable while she breathes through her mouth."],
   ["Nasal cannula at 2 L/min",
    "A nasal cannula delivers through the nostrils, and hers are packed. A simple mask over nose and mouth reaches her mouth-breathing.", "ruled out by a stated finding"],
   ["Trach collar",
    "A trach collar is for a tracheostomy, which she does not have. A simple mask delivers oxygen to a mouth-breathing patient.", "ruled out by a stated finding"],
   ["Non-rebreather at 15 L/min",
    "A non-rebreather is for severe hypoxia; her 89% is mild. A simple mask gives a modest fraction through the mouth.", "wrong stage or severity"]],
  C(13), "agent/regimen", "treatment"),

V(ESC, IO_B,
  "A 57-year-old man with a chronic lung disease flare needs both inhaled medication by nebulizer and supplemental oxygen. He has no tracheostomy. Which air-entrainment interface over his face suits him?",
  [["Aerosol mask",
    "Correct. The air-entrainment nebulizer is delivered over the face by an aerosol mask or open face mask (and to an airway by a T-piece or trach collar); with no tracheostomy, an aerosol mask fits him."],
   ["Trach collar",
    "A trach collar delivers air-entrainment nebulizer oxygen to a tracheostomy, which he does not have. Over his face, an aerosol mask is used.", "ruled out by a stated finding"],
   ["Non-rebreather mask",
    "A non-rebreather delivers high-fraction oxygen through a reservoir bag; it is not an air-entrainment nebulizer interface. The aerosol mask delivers the nebulized system over the face.", "adjacent fact"],
   ["Nasal cannula",
    "A nasal cannula delivers oxygen through the nostrils but is not an air-entrainment nebulizer interface. An aerosol mask over the face is.", "adjacent fact"]],
  C(18), "agent/regimen", "treatment"),

# ---------------------------------------------------------------- hazards with comorbidities
V(HAZ, IO_A,
  "A 76-year-old woman with chronic obstructive pulmonary disease is put on a simple mask at 10 L/min overnight. By morning she is hard to wake and her arterial carbon dioxide is much higher than her baseline. Which hazard of oxygen therapy occurred?",
  [["Hypercapnia from carbon dioxide retention",
    "Correct. Hypercapnia is a listed hazard of oxygen therapy; she became hard to wake as her carbon dioxide rose on oxygen, the change a good response avoids (oxygen up without carbon dioxide up)."],
   ["Mucosal irritation",
    "Mucosal irritation dries the nose and airway; it does not raise carbon dioxide or cause drowsiness. Her rising carbon dioxide is hypercapnia.", "adjacent fact"],
   ["Vasoconstriction",
    "Vasoconstriction is the infarction caution, not a cause of rising carbon dioxide. Her picture is carbon dioxide retention.", "adjacent fact"],
   ["Hypoxia from too little flow",
    "At 10 L/min she was getting more oxygen, not less; hypoxia would not raise carbon dioxide this way. Her drowsiness with rising carbon dioxide is hypercapnia.", "reversed direction or value"]],
  C(3), "complication", "complication"),

V(HAZ, IO_A,
  "An 80-year-old man on home oxygen at 5 L/min by nasal cannula with no humidifier complains of a sore, dry nose and occasional bleeding. Which change addresses the cause?",
  [["Add humidity to the oxygen",
    "Correct. His dry, bleeding nose is mucosal irritation, a listed hazard; humidity is used with nasal cannula flows greater than 4 L/min, and he is at 5 without it."],
   ["Increase the flow to 6 L/min",
    "More dry flow would worsen the irritation. Above 4 L/min, the cannula's oxygen should be humidified.", "reversed direction or value"],
   ["Apply a petroleum lip and nose balm",
    "Petroleum products are to be avoided with oxygen because of fire. The fix for his irritation is humidity at flows above 4 L/min.", "ruled out by a stated finding"],
   ["Switch to a non-rebreather mask",
    "A non-rebreather is for severe hypoxia and does not cure irritation from dry gas. Humidifying his cannula oxygen above 4 L/min does.", "wrong stage or severity"]],
  C(9), "complication", "treatment"),

# ---------------------------------------------------------------- qualification at the edge
V(HOME, IO_F,
  "A 69-year-old woman with chronic lung disease is assessed for home oxygen before discharge. Her resting room-air saturation is exactly 88%, and she has no other findings. What is her qualification?",
  [["Group I, recertified at 12 months",
    "Correct. The resting criterion is a saturation of 88% or lower, so exactly 88% qualifies outright with no comorbidity: Group I, recertified every 12 months."],
   ["Group II, recertified at 3 months",
    "Group II is the conditional group for a saturation of 89% (or oxygen pressure 56 to 59) with a comorbidity. Her 88% meets Group I on its own.", "adjacent fact"],
   ["Not qualified without a comorbidity",
    "A comorbidity is needed only at 89%; at 88% the resting criterion is met by itself. She qualifies in Group I.", "wrong stage or severity"],
   ["Qualified for exertion oxygen",
    "Her qualifying value is at rest, so she qualifies for resting oxygen in Group I, not only during exertion.", "adjacent fact"]],
  C(6), "test finding", "test"),

V(HOME, IO_F,
  "A 74-year-old man with chronic obstructive pulmonary disease has poor finger perfusion, and the pulse oximeter will not give a steady reading. His arterial oxygen pressure is 55 mm Hg on room air at rest. What is his home oxygen status?",
  [["Qualifies in Group I",
    "Correct. Hypoxia can be documented by arterial blood gas as well as by oximetry, and an oxygen pressure of 55 mm Hg or lower at rest qualifies outright, Group I, recertified at 12 months."],
   ["Qualifies in Group II",
    "Group II is for an oxygen pressure of 56 to 59 mm Hg with a comorbidity. At exactly 55 he meets the Group I cutoff on his own.", "adjacent fact"],
   ["Cannot qualify without oximetry",
    "Qualification accepts an arterial blood gas or pulse oximetry. His blood gas oxygen pressure of 55 documents the hypoxia.", "ruled out by a stated finding"],
   ["Does not qualify at 55 mm Hg",
    "The cutoff is 55 mm Hg or lower, so 55 qualifies. He meets the Group I criterion.", "reversed direction or value"]],
  C(5), "test finding", "test"),

V(HOME, IO_F,
  "A 70-year-old woman with interstitial lung disease, pulmonary hypertension and a hematocrit of 52% has a resting room-air saturation of 89%. Which finding makes her qualify?",
  [["Her pulmonary hypertension",
    "Correct. At 89% she qualifies only conditionally (Group II), with pulmonary hypertension, cor pulmonale or a hematocrit over 56%. Her pulmonary hypertension qualifies her; her hematocrit of 52% does not reach 56%."],
   ["Her hematocrit of 52%",
    "The hematocrit criterion is over 56%, and 52% falls short. Her qualifying finding is pulmonary hypertension.", "reversed direction or value"],
   ["Her interstitial lung disease",
    "The underlying lung disease is not one of the three Group II findings. Pulmonary hypertension, cor pulmonale or a hematocrit over 56% are; she has pulmonary hypertension.", "adjacent fact"],
   ["Nothing; 89% does not qualify",
    "89% does qualify when a listed finding is present. Her pulmonary hypertension is one, so she qualifies in Group II.", "ruled out by a stated finding"]],
  C(6), "risk factors", "test"),

# ---------------------------------------------------------------- safety teaching
V(SAFE, IO_G,
  "A 79-year-old woman using home oxygen keeps an electric space heater beside her recliner, where she sits with her tubing. Which teaching applies?",
  [["Keep oxygen at least 10 feet from the heater",
    "Correct. Electric appliances are heat sources, and home oxygen should be kept at least 10 feet from heat sources such as pilot lights, electric appliances and candles because oxygen is highly flammable."],
   ["A heater is safe because it has no flame",
    "Electric appliances are named among the heat sources to keep away from oxygen; no open flame is needed for the hazard. Keep at least 10 feet away.", "common lay belief"],
   ["Lower her flow while the heater runs",
    "Lower flow still feeds a fire. The rule is distance: at least 10 feet from heat sources, electric appliances included.", "common lay belief"],
   ["Keep the heater 3 feet away",
    "Three feet is well inside the safety distance. Oxygen should be at least 10 feet from heat sources.", "reversed direction or value"]],
  C(7), "education", "education"),

V(SAFE, IO_G,
  "A 71-year-old man starting home oxygen asks why he must be so careful at home if oxygen is \"just air.\" Which property of oxygen underlies the safety teaching?",
  [["It is highly flammable",
    "Correct. Oxygen is highly flammable, and tanks hold it as compressed gas, so patients are taught no smoking, distance from heat sources, avoiding petroleum products, signage and working alarms."],
   ["It is toxic to breathe for visitors",
    "Visitors are not harmed by breathing near it; the teaching is about fire. Oxygen is highly flammable, which drives every home safety rule.", "common lay belief"],
   ["It is heavier than water",
    "The weight of the gas is not the issue. The safety teaching rests on oxygen being highly flammable and stored as compressed gas.", "common lay belief"],
   ["It turns into carbon monoxide",
    "Oxygen does not become carbon monoxide; carbon monoxide alarms are part of general fire safety. The core property is that oxygen is highly flammable.", "confused mechanism or drug class"]],
  C(7), "education", "education"),

# ---------------------------------------------------------------- judging the response
V(EVAL, IO_E,
  "A 64-year-old man with pneumonia has an arterial blood gas before and after starting oxygen. After oxygen, his arterial oxygen pressure is higher, his carbon dioxide is unchanged, and his pH has returned toward normal. How is this response read?",
  [["A good response",
    "Correct. A good response on the blood gas is a higher arterial oxygen without a rise in carbon dioxide and with correction of the pH; all three are present for him."],
   ["Carbon dioxide retention",
    "Retention would show a rising carbon dioxide; his is unchanged. Higher oxygen with steady carbon dioxide and pH correction is a good response.", "ruled out by a stated finding"],
   ["No response",
    "His oxygen pressure rose and his pH corrected, so there was a response. With carbon dioxide unchanged, it is a good one.", "reversed direction or value"],
   ["A response if saturation reaches 100%",
    "There is no single 100% target; the saturation target varies with the patient. His blood gas already shows a good response.", "common lay belief"]],
  C(25), "test finding", "test"),

V(EVAL, IO_E,
  "A 52-year-old woman with asthma is started on oxygen. She says she feels better, but her lips remain dusky, her accessory muscles are still working hard, and her saturation has not moved. How should her response be judged?",
  [["Not yet adequate on clinical and objective measures",
    "Correct. Response is judged by symptoms, work of breathing and color/perfusion together with objective data. Her persistent dusky color, heavy work of breathing and unchanged saturation outweigh her saying she feels better."],
   ["Adequate, because she feels better",
    "Feeling better is one measure, but her work of breathing, color and saturation have not improved. Judged on all of them, the response is not yet adequate.", "ruled out by a stated finding"],
   ["Adequate, because oxygen is running",
    "Running oxygen is not a response. The measures are symptoms, work of breathing, color/perfusion and objective data, and hers show no improvement.", "common lay belief"],
   ["Cannot be judged without a chest film",
    "A chest film is not among the listed measures. Her symptoms, work of breathing, color and saturation already show the response is inadequate.", "adjacent fact"]],
  C(25), "manifestation", "test"),

V(EVAL, IO_E,
  "A 60-year-old man with heart failure is on oxygen while his fluid overload is treated. Over two days his breathing eases, his saturation stays at target, and his vital signs settle. Which ongoing step is part of evaluating his oxygen therapy?",
  [["Keep monitoring for complications",
    "Correct. Evaluating the response includes clinical assessment, objective data, vital signs and further monitoring for complications of oxygen therapy, such as carbon dioxide retention or mucosal irritation, while the cause is treated."],
   ["Stop checking his saturation",
    "Saturation is part of the objective data and keeps guiding his oxygen as he improves. Monitoring continues, including for complications.", "wrong stage or severity"],
   ["Raise his flow to secure the gains",
    "More oxygen than needed risks carbon dioxide retention; he is already at target. The step is continued monitoring for complications.", "reversed direction or value"],
   ["Start home oxygen qualification today",
    "He is still improving on treatment; qualification documents need at the time of need, near discharge. Now the step is monitoring for complications.", "wrong stage or severity"]],
  C(25), "complication", "next step"),
]
