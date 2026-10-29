# -*- coding: utf-8 -*-
"""Lecture 33 vignette pool B -- Oxygen Delivery: who qualifies for home oxygen (resting, conditional
Group II, sleep, exertion, recertification), home safety teaching, and reading a device's fraction from
its flow (slides 5-7, 9, 11, 13, 20).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

Criteria items work like a score: the stem gives the patient's values and comorbidities, the key
explanation walks the criteria (tools/question_writing/EXPLAIN_DEEP.md), and each wrong choice names the
criterion it misreads. Flow items show the 4%-per-liter arithmetic from room air's 21%.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e6l33_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


HOME = "Who qualifies for home oxygen"
SAFE = "Oxygen safety at home"
FLOW = "Reading the fraction from the flow"

QUESTIONS = [

# ---------------------------------------------------------------- who qualifies
V(HOME, IO_F,
  "A 73-year-old man with chronic obstructive pulmonary disease is ready for discharge after his treatment is optimized. His resting saturation on room air is 87%, and he has no pulmonary hypertension, cor pulmonale (right-sided heart failure from lung disease) or high hematocrit. How often will his home oxygen be recertified?",
  [["Every 12 months",
    "Correct. A resting room-air saturation of 87% is at or below 88%, so he qualifies outright in Group I with no comorbidity needed; Group I home oxygen is recertified every 12 months."],
   ["Every 3 months",
    "Three months is the Group II interval, for a borderline value (saturation 89% or oxygen pressure 56 to 59) that qualifies only with a comorbidity. His 87% qualifies outright in Group I, rechecked at 12 months. Tell: no comorbidity was needed.", "adjacent fact"],
   ["Every 1 month",
    "One month is not a recertification interval in the criteria. His saturation of 87% at rest places him in Group I, recertified every 12 months; Group II, the conditional group, is the one rechecked sooner, at 3 months.", "reversed direction or value"],
   ["Every 24 months",
    "Two years is longer than any interval in the criteria. Group I, which his resting 87% meets, is recertified every 12 months, and the conditional Group II every 3 months.", "reversed direction or value"]],
  C(6), "prognosis", "test"),

V(HOME, IO_F,
  "A 70-year-old woman with chronic obstructive pulmonary disease and an echocardiogram showing pulmonary hypertension has a resting room-air saturation of 89%. Which statement about home oxygen applies to her?",
  [["She qualifies in Group II",
    "Correct. A saturation of exactly 89% qualifies only conditionally, Group II, when there is evidence of pulmonary hypertension, cor pulmonale or a hematocrit over 56%; her pulmonary hypertension is that evidence, and Group II is recertified at 3 months."],
   ["She qualifies in Group I",
    "Group I needs a resting saturation of 88% or lower (or oxygen pressure 55 or lower). Her 89% misses that cutoff by one point, so she qualifies only through her pulmonary hypertension, in Group II. Tell: 89% is never Group I.", "wrong stage or severity"],
   ["She does not qualify at 89%",
    "89% alone would not qualify, but she has pulmonary hypertension, one of the three findings (with cor pulmonale and hematocrit over 56%) that make 89% qualify in Group II. Reading the saturation without the comorbidity misses it.", "ruled out by a stated finding"],
   ["She qualifies for sleep oxygen alone",
    "Nocturnal oxygen depends on a sleep study showing 88% or lower with a drop of 5% or more, which she has not had. Her resting 89% with pulmonary hypertension qualifies her in Group II for resting oxygen.", "adjacent fact"]],
  C(6), "test finding", "test"),

V(HOME, IO_F,
  "A 66-year-old man with heart disease and type 2 diabetes has a resting room-air saturation of 89%. He has no pulmonary hypertension, no cor pulmonale (right-sided heart failure from lung disease), and his hematocrit is 44%. Does he qualify for home oxygen at rest?",
  [["No, 89% needs a listed comorbidity",
    "Correct. A resting saturation of 89% qualifies only with pulmonary hypertension, cor pulmonale or a hematocrit over 56% (Group II). He has none of the three, and his hematocrit of 44% is well under 56%, so he does not qualify at rest."],
   ["Yes, in Group I",
    "Group I requires 88% or lower at rest, and he is at 89%. The borderline value would need a qualifying comorbidity, which he lacks. Tell: Group I is 88% or lower, never 89%.", "wrong stage or severity"],
   ["Yes, in Group II because of diabetes",
    "Diabetes is not one of the Group II findings; only pulmonary hypertension, cor pulmonale or a hematocrit over 56% make 89% qualify. Heart disease in general does not count either.", "adjacent fact"],
   ["Yes, because his hematocrit is high",
    "A hematocrit of 44% is not high by the criteria; Group II needs a hematocrit over 56%. With no qualifying finding, his 89% does not qualify at rest.", "reversed direction or value"]],
  C(6), "test finding", "test"),

V(HOME, IO_F,
  "A 68-year-old woman who smoked for 40 years has an arterial oxygen pressure of 57 mm Hg at rest on room air and a hematocrit of 58%. Which recertification interval applies to her home oxygen?",
  [["Every 3 months",
    "Correct. An oxygen pressure of 57 sits in the conditional 56 to 59 mm Hg range, and her hematocrit of 58% is over 56% (polycythemia (a hematocrit above 56%)), so she qualifies in Group II, which is recertified every 3 months."],
   ["Every 12 months",
    "Twelve months is Group I, which needs an oxygen pressure of 55 or lower. Her 57 is in the 56 to 59 range and qualifies only because of her hematocrit over 56%, so she is Group II, rechecked at 3 months.", "adjacent fact"],
   ["Every 1 month",
    "One month is not an interval in the criteria. Her oxygen pressure of 57 with a hematocrit of 58% is Group II, which is recertified every 3 months.", "reversed direction or value"],
   ["Every 24 months",
    "Two years is longer than any listed interval. A conditional qualifier like her (oxygen pressure 57 with hematocrit over 56%) is recertified sooner, every 3 months.", "reversed direction or value"]],
  C(6), "prognosis", "test"),

V(HOME, IO_F,
  "A 61-year-old man with interstitial lung disease has a resting room-air saturation of 93%. When he walks the hallway it falls to 85%, and with 2 L/min by nasal cannula it rises to 92% while walking. What does he qualify for?",
  [["Oxygen during exertion",
    "Correct. At rest (93%) he does not qualify, but with exertion his saturation falls to 85%, at or below 88%, and improves when oxygen is given (to 92%). That meets the exertion criterion, so he qualifies for ambulatory oxygen, documented with the flow that corrected it."],
   ["Oxygen at rest",
    "His resting saturation of 93% is above the 88% cutoff, so he does not qualify at rest. The fall to 85% with walking that improves on oxygen qualifies him for oxygen during exertion.", "ruled out by a stated finding"],
   ["Nothing, since rest is normal",
    "A normal resting value does not end the assessment. Qualification also tests exertion and sleep; his exertional 85% that improves on oxygen meets the exertion criterion.", "wrong stage or severity"],
   ["Oxygen during sleep",
    "Sleep oxygen requires a sleep measurement of 88% or lower with a drop of 5% or more, which was not done. His documented qualifier is exertional desaturation that improves on oxygen.", "adjacent fact"]],
  C(5), "test finding", "test"),

V(HOME, IO_F,
  "A 69-year-old woman with chronic lung disease drops from 94% to 86% while walking. Oxygen at 2 and then 4 L/min is added, but her saturation stays at 86% while walking. How does this result bear on ambulatory oxygen?",
  [["It does not meet the exertion criterion",
    "Correct. The exertion criterion needs a saturation of 88% or lower that improves when oxygen is given. She drops to 86%, but oxygen at 2 and 4 L/min does not raise it, so the improvement half of the criterion is not met."],
   ["It qualifies her for ambulatory oxygen",
    "Desaturating to 86% is only half the criterion; the saturation must also improve on oxygen. Hers stays at 86% on 2 and 4 L/min, so exertional qualification is not met.", "ruled out by a stated finding"],
   ["It qualifies her in Group I at rest",
    "Group I at rest needs 88% or lower at rest, and her resting value is 94%. Her test was during walking, and it lacked the improvement on oxygen the exertion criterion needs.", "adjacent fact"],
   ["It qualifies her for sleep oxygen",
    "A walking test says nothing about sleep; nocturnal oxygen needs a sleep value of 88% or lower with a drop of 5% or more. Her exertional result fails because oxygen did not improve it.", "adjacent fact"]],
  C(5), "test finding", "test"),

V(HOME, IO_F,
  "A 72-year-old man with chronic obstructive pulmonary disease has a daytime saturation of 93%. Overnight oximetry shows his saturation falling to 87% for long stretches. What does he qualify for?",
  [["Nocturnal oxygen",
    "Correct. During sleep his saturation falls to 87% (88% or lower) and drops 6 points from his 93% baseline (5% or more), meeting the sleep criterion; he qualifies for nocturnal oxygen."],
   ["Continuous oxygen at rest",
    "His resting daytime saturation of 93% is above 88%, so he does not qualify at rest. The sleep values, 87% with a 6-point drop, qualify him for nocturnal oxygen.", "ruled out by a stated finding"],
   ["Nothing, since daytime is normal",
    "A normal daytime value does not end the assessment; qualification also tests sleep. His overnight fall to 87% with a drop of 5% or more meets the sleep criterion.", "wrong stage or severity"],
   ["Oxygen during exertion",
    "Exertional qualification needs a walking test showing 88% or lower that improves on oxygen; none was done. His overnight result qualifies him for nocturnal oxygen.", "adjacent fact"]],
  C(5), "test finding", "test"),

V(HOME, IO_F,
  "A 65-year-old woman has a daytime saturation of 95%. Overnight oximetry shows her falling to 91% at the lowest. Does she qualify for nocturnal oxygen?",
  [["No, her sleep value stays above 88%",
    "Correct. The sleep criterion needs a saturation of 88% or lower with a drop of 5% or more from baseline. Her 4-point drop to 91% fails on both counts, so she does not qualify for nocturnal oxygen."],
   ["Yes, since she drops during sleep",
    "Any drop is not enough; the sleep criterion needs 88% or lower with a fall of 5% or more. Her lowest of 91% (a 4-point fall from 95%) does not meet it.", "ruled out by a stated finding"],
   ["Yes, in Group II",
    "Group II is the conditional resting group (89% or 56 to 59 mm Hg with pulmonary hypertension, cor pulmonale or hematocrit over 56%). Her sleep value of 91% meets neither the sleep nor the Group II criteria.", "adjacent fact"],
   ["Yes, if she also has diabetes",
    "Diabetes is not a qualifying finding. The sleep criterion is a value of 88% or lower with a drop of 5% or more, and her 91% does not reach it.", "adjacent fact"]],
  C(5), "test finding", "test"),

V(HOME, IO_F,
  "A 70-year-old man admitted with a heart failure exacerbation still needs 2 L/min of oxygen on hospital day 1. His team plans to discharge him in a few days. When should his home oxygen qualification be performed?",
  [["At the time of need, before discharge",
    "Correct. Qualification is performed at the time of need: once he is treated and ready for discharge but still needs oxygen, his hypoxia is documented by pulse oximetry or arterial blood gas at rest, exertion or sleep."],
   ["On admission day, while he is acutely ill",
    "On day 1 he is still being treated and may improve off oxygen. Qualification documents need at the time of need, when he is otherwise ready to go home but still hypoxic.", "wrong stage or severity"],
   ["After a year on home oxygen",
    "He cannot go home on oxygen without first qualifying. The documentation is done at the time of need, before discharge; recertification comes later at 3 or 12 months.", "reversed direction or value"],
   ["At his first outpatient visit",
    "Waiting for clinic would send him home without the oxygen he needs. Qualification is done at the time of need, before discharge, by oximetry or blood gas.", "wrong stage or severity"]],
  C(5), "initial test", "next step"),

V(HOME, IO_F,
  "A 67-year-old woman with lung disease is being assessed for home oxygen. Her resting room-air saturation is 92%. Which is the next step in her qualification?",
  [["Check her saturation with exertion",
    "Correct. Qualification documents hypoxia at rest, with exertion and/or during sleep. At rest she is above 88%, so the next step is to measure her saturation while she walks and, if it falls to 88% or lower, show it improves with oxygen."],
   ["Stop: she does not qualify",
    "A resting 92% only rules out the resting criterion. Exertion and sleep are also tested, so stopping here could miss an exertional qualifier.", "wrong stage or severity"],
   ["Prescribe oxygen at 2 L/min now",
    "She has not met any criterion yet; at rest she is 92%. Oxygen is prescribed after hypoxia is documented, so the exertional measurement comes first.", "wrong stage or severity"],
   ["Order a complete blood count",
    "A hematocrit over 56% matters only for a borderline Group II value. With a resting 92%, the next step is to test her saturation with exertion.", "adjacent fact"]],
  C(5), "initial test", "next step"),

V(HOME, IO_F,
  "A 71-year-old man with chronic obstructive pulmonary disease and cor pulmonale (right-sided heart failure from lung disease) has an arterial oxygen pressure of 58 mm Hg at rest. What is his qualification status?",
  [["Group II, recertified at 3 months",
    "Correct. An oxygen pressure of 58 is in the conditional 56 to 59 mm Hg range, and cor pulmonale is one of the three findings that make it qualify; that is Group II, recertified every 3 months."],
   ["Group I, recertified at 12 months",
    "Group I needs an oxygen pressure of 55 or lower; his 58 is above it and qualifies only because of cor pulmonale, which makes him Group II, rechecked at 3 months. Tell: a value in 56 to 59 is always the conditional group.", "adjacent fact"],
   ["Not qualified at 58 mm Hg",
    "58 alone would not qualify, but cor pulmonale is a listed qualifying finding for the 56 to 59 range. Missing the comorbidity misreads him as unqualified.", "ruled out by a stated finding"],
   ["Qualified for sleep oxygen",
    "No sleep study was done; his qualifying value is a resting oxygen pressure of 58 with cor pulmonale, which is Group II resting oxygen.", "adjacent fact"]],
  C(6), "test finding", "test"),

# ---------------------------------------------------------------- safety at home
V(SAFE, IO_G,
  "A 72-year-old man starting home oxygen says he smokes on his back porch and that his wife smokes in the kitchen. Which teaching applies?",
  [["No one should smoke in the home",
    "Correct. Oxygen is highly flammable, so no one should smoke in the home of a patient on oxygen; the fire danger is too great. That covers his wife in the kitchen, and the home is posted with No Smoking signs."],
   ["His wife may smoke if he is in another room",
    "Another room is still the home, and oxygen and its tanks are throughout it. The teaching is that no one smokes in the home, because the fire danger is too great.", "common lay belief"],
   ["Smoking is fine if the tank is turned off",
    "Turning off the flow does not make the home safe; tanks hold compressed, highly flammable oxygen. No one should smoke in the home.", "common lay belief"],
   ["He must stop; visitors are exempt",
    "Visitors are not exempt; signage (No Smoking, Oxygen in Use) exists to warn everyone in the home. No one smokes in the home of an oxygen user.", "common lay belief"]],
  C(7), "education", "education"),

V(SAFE, IO_G,
  "A 69-year-old woman on home oxygen has dry, cracked lips and uses a petroleum jelly lip balm several times a day. Which teaching applies?",
  [["Stop using petroleum-based products",
    "Correct. Patients on oxygen should avoid petroleum-based products (lip balms, lotions, oils, grease), because oxygen is highly flammable and these products can feed a fire on the face where the oxygen flows."],
   ["Use more balm to protect the lips",
    "More petroleum balm increases the fire risk where oxygen flows over her face. The teaching is to avoid petroleum-based products altogether.", "reversed direction or value"],
   ["Switch her oxygen to a non-rebreather",
    "Changing the device does not remove a petroleum product from her face; a non-rebreather is for severe hypoxia. The teaching is to avoid petroleum-based products.", "adjacent fact"],
   ["Stop her home oxygen",
    "Stopping needed oxygen would leave her hypoxic. The fix is to avoid petroleum-based products while continuing oxygen safely.", "wrong stage or severity"]],
  C(7), "education", "education"),

V(SAFE, IO_G,
  "A 74-year-old man on home oxygen has a gas water heater with a pilot light in the hallway where he likes to sit. How far from it should his oxygen be kept?",
  [["At least 10 feet",
    "Correct. Home oxygen should be kept at least 10 feet from heat sources such as pilot lights, electric appliances and candles, because oxygen is highly flammable."],
   ["At least 2 feet",
    "Two feet is far too close to a flame. The safety rule is at least 10 feet from heat sources such as a pilot light.", "reversed direction or value"],
   ["At least 5 feet",
    "Five feet is still inside the danger zone. Oxygen should be kept at least 10 feet from heat sources like pilot lights, appliances and candles.", "reversed direction or value"],
   ["At least 50 feet",
    "Fifty feet is not the rule and would be unworkable at home. The safety distance from heat sources is at least 10 feet.", "reversed direction or value"]],
  C(7), "education", "education"),

V(SAFE, IO_G,
  "A 77-year-old woman is going home on oxygen tanks. Her son asks what to do with the tanks and how to store them. Which property of the tanks drives the storage and disposal teaching?",
  [["They hold compressed gas",
    "Correct. Oxygen tanks contain compressed gas, so the teaching covers proper storage and disposal, in addition to the warning that oxygen is highly flammable."],
   ["They hold a liquid fuel",
    "Oxygen tanks do not hold fuel. They hold compressed gas, which is why storage and disposal are taught, alongside oxygen's flammability.", "confused mechanism or drug class"],
   ["They emit carbon monoxide",
    "Oxygen tanks do not produce carbon monoxide. They hold compressed gas, so storage and disposal are taught; separately, homes need working carbon monoxide alarms.", "confused mechanism or drug class"],
   ["They spoil within a week",
    "Spoilage is not the issue. The tanks contain compressed gas, so proper storage and disposal are part of the teaching.", "common lay belief"]],
  C(7), "education", "education"),

V(SAFE, IO_G,
  "A 70-year-old man is setting up home oxygen in a house with old smoke detectors. Which home safety step is taught?",
  [["Working smoke and carbon monoxide alarms, tested monthly",
    "Correct. Home oxygen safety teaching includes making sure the home has working smoke and carbon monoxide alarms and testing them monthly, because oxygen is a fire hazard."],
   ["Removing the smoke alarms near the oxygen",
    "Removing alarms is the opposite of the teaching. Homes with oxygen need working smoke and carbon monoxide alarms, tested monthly.", "reversed direction or value"],
   ["Testing the alarms once a year",
    "Yearly testing is too infrequent. The teaching is to test the smoke and carbon monoxide alarms monthly.", "reversed direction or value"],
   ["Keeping a candle lit as a warning light",
    "A lit candle is a heat source to keep at least 10 feet from oxygen. The safety step is working smoke and carbon monoxide alarms tested monthly.", "reversed direction or value"]],
  C(7), "education", "education"),

V(SAFE, IO_G,
  "A 68-year-old woman going home on oxygen asks what signs to post. Which signage is taught?",
  [["No Smoking and Oxygen in Use signs",
    "Correct. Patients are taught to post No Smoking signage and, potentially, Oxygen in Use signs within the home, because oxygen is highly flammable and compressed."],
   ["A sign with her oxygen flow rate",
    "The flow rate is part of the prescription, not a safety sign. The signage taught is No Smoking and Oxygen in Use.", "adjacent fact"],
   ["A sign with her pharmacy's number",
    "A pharmacy number is not the safety signage. The home should carry No Smoking and Oxygen in Use signs.", "common lay belief"],
   ["A sign with her recertification date",
    "Recertification is paperwork, not a safety warning. The teaching is No Smoking and Oxygen in Use signage.", "adjacent fact"]],
  C(7), "education", "education"),

# ---------------------------------------------------------------- reading the fraction from the flow
V(FLOW, IO_D,
  "A 63-year-old woman with pneumonia is on a nasal cannula at 2 L/min. Her flow is increased to 5 L/min. About what fraction of inspired oxygen is she receiving now?",
  [["40%",
    "Correct. Room air is 21%; a nasal cannula gives about 24% at 1 L/min and adds about 4% per liter: 28% at 2, 32% at 3, 36% at 4 and 40% at 5 L/min."],
   ["28%",
    "28% is what she received at 2 L/min, before the change. At 5 L/min the cannula delivers about 40%, three 4% steps higher.", "adjacent fact"],
   ["44%",
    "44% is the cannula at 6 L/min, its maximum setting. At 5 L/min she receives about 40%, one 4% step lower.", "adjacent fact"],
   ["60%",
    "60% is the bottom of the non-rebreather's range; a nasal cannula never exceeds about 44%. At 5 L/min she receives about 40%.", "reversed direction or value"]],
  C(9), "agent/regimen", "test"),

V(FLOW, IO_D,
  "A 75-year-old man's family turned his home nasal cannula up to 9 L/min because he felt short of breath. About what fraction of inspired oxygen does he receive at that setting?",
  [["44%",
    "Correct. A nasal cannula can be turned above 6 L/min, but the fraction maxes out at about 44%; at 9 L/min he receives no more than at 6 L/min, so more flow will not help."],
   ["56%",
    "Adding 4% per liter past 6 L/min would give 56%, but the cannula does not keep climbing; it maxes out at about 44%. Tell: the 4%-per-liter rule stops at 6 L/min.", "reversed direction or value"],
   ["60%",
    "60% needs a reservoir device such as the non-rebreather. A nasal cannula turned to 9 L/min still delivers only about 44%.", "reversed direction or value"],
   ["100%",
    "100% is the top of the non-rebreather's range. A nasal cannula's fraction caps at about 44%, whatever the flow above 6 L/min.", "reversed direction or value"]],
  C(11), "agent/regimen", "test"),

V(FLOW, IO_D,
  "A 57-year-old man with bronchitis is placed on a simple mask at 6 to 7 L/min. About what fraction of inspired oxygen is he receiving?",
  [["40%",
    "Correct. A simple mask delivers about 35% at 5 to 6 L/min, 40% at 6 to 7 L/min and 50% at 7 to 8 L/min, within its 35% to 50% range."],
   ["28%",
    "28% is a nasal cannula at 2 L/min, below any simple mask setting. At 6 to 7 L/min the simple mask gives about 40%.", "adjacent fact"],
   ["50%",
    "50% is the simple mask at 7 to 8 L/min, one step higher. At 6 to 7 L/min it gives about 40%.", "adjacent fact"],
   ["80%",
    "80% is beyond a simple mask; reservoir devices such as the non-rebreather reach that range. At 6 to 7 L/min the simple mask gives about 40%.", "reversed direction or value"]],
  C(13), "agent/regimen", "test"),
]
