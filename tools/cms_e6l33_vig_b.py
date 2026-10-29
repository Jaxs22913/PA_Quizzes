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
    "Correct. His resting room-air saturation is 87%, at or below 88%, which is the Group I qualification (conditional Group II needs a comorbidity such as pulmonary hypertension, cor pulmonale or a hematocrit above 56%). Group I patients are recertified every 12 months."],
   ["Every 3 months",
    "Every 3 months applies to Group II, the conditional group with a saturation of 89% plus pulmonary hypertension, cor pulmonale or a hematocrit above 56%. He has none of those and a saturation of 87% qualifies him as Group I. Tell: earlier recertification goes with a chronic complication.", "adjacent fact"],
   ["Every 1 month",
    "An interval of every 1 month is not one of the stated intervals. The two are 12 months for Group I and 3 months for Group II. Tell: only 12 months and 3 months appear as recertification intervals, and his criteria give 12.", "reversed direction or value"],
   ["Every 24 months",
    "An interval of every 24 months is not stated either; Group I is recertified at 12 months and Group II at 3 months. Tell: with an uncomplicated resting saturation of 87%, the answer is the longer listed interval, 12 months.", "reversed direction or value"]],
  C(6), "prognosis", "test"),

V(HOME, IO_F,
  "A 70-year-old woman with chronic obstructive pulmonary disease and an echocardiogram showing pulmonary hypertension has a resting room-air saturation of 89%. Which statement about home oxygen applies to her?",
  [["She qualifies in Group II",
    "Correct. Her resting saturation of 89% is above the Group I cutoff of 88% or less, so on its own it would not qualify. The echocardiogram showing pulmonary hypertension adds the comorbidity that makes a saturation of 89% qualify, which is Group II (recertified at 3 months)."],
   ["She qualifies in Group I",
    "Group I requires a saturation of 88% or less (or arterial oxygen pressure of 55 mm Hg or less) at rest. At 89% she is just above that, so she falls into the conditional group. Tell: 88% or less is Group I; 89% needs a comorbidity and is Group II.", "wrong stage or severity"],
   ["She does not qualify at 89%",
    "She does qualify: a saturation of 89% plus pulmonary hypertension meets Group II criteria. The 89% alone would not, but the comorbidity changes the answer. Tell: 89% by itself fails, but 89% plus pulmonary hypertension, cor pulmonale or a hematocrit above 56% qualifies.", "ruled out by a stated finding"],
   ["She qualifies for sleep oxygen alone",
    "Her qualifying finding is at rest, not during sleep. The sleep criterion is a saturation of 88% or less with a drop of 5% or more from baseline, and nothing here describes sleep. Tell: sleep oxygen requires a documented overnight drop; her stem gives a resting value.", "adjacent fact"]],
  C(6), "test finding", "test"),

V(HOME, IO_F,
  "A 66-year-old man with heart disease and type 2 diabetes has a resting room-air saturation of 89%. He has no pulmonary hypertension, no cor pulmonale (right-sided heart failure from lung disease), and his hematocrit is 44%. Does he qualify for home oxygen at rest?",
  [["No, 89% needs a listed comorbidity",
    "Correct. A resting saturation of 89% is above the 88% cutoff, so it needs a listed comorbidity: pulmonary hypertension, cor pulmonale or a hematocrit above 56%. He has none, and his hematocrit is only 44%. Heart disease and diabetes are not on the list, so he does not qualify at rest."],
   ["Yes, in Group I",
    "Group I needs a saturation of 88% or less (or arterial oxygen pressure of 55 mm Hg or less) at rest. At 89% he is above the cutoff. Tell: Group I starts at 88%; his 89% does not meet it.", "wrong stage or severity"],
   ["Yes, in Group II because of diabetes",
    "Diabetes is not one of the qualifying comorbidities. Group II requires pulmonary hypertension, cor pulmonale or a hematocrit above 56% together with a saturation of 89%. Tell: look for a lung-related complication or polycythemia, not general comorbidities.", "adjacent fact"],
   ["Yes, because his hematocrit is high",
    "His hematocrit is 44%, well below the 56% needed for polycythemia to count. The comorbidity criterion needs a hematocrit above 56%. Tell: a high hematocrit would help, but 44% is not high.", "reversed direction or value"]],
  C(6), "test finding", "test"),

V(HOME, IO_F,
  "A 68-year-old woman who smoked for 40 years has an arterial oxygen pressure of 57 mm Hg at rest on room air and a hematocrit of 58%. Which recertification interval applies to her home oxygen?",
  [["Every 3 months",
    "Correct. Her arterial oxygen pressure of 57 mm Hg lies in the 56-59 range, above the Group I limit of 55 mm Hg, so she needs a comorbidity. Her hematocrit of 58% is above 56%, which is polycythemia. That puts her in Group II, which is recertified every 3 months."],
   ["Every 12 months",
    "Every 12 months is the Group I interval, which needs a pressure of 55 mm Hg or less. Hers is 57 mm Hg, above that, and she qualifies only because of her high hematocrit. Tell: the comorbidity-dependent group recertifies sooner.", "adjacent fact"],
   ["Every 1 month",
    "An interval of every 1 month is not one of the stated intervals. Group I is recertified at 12 months and Group II at 3 months, and her profile is Group II. Tell: only 12 and 3 appear, and a complication shifts the answer to 3.", "reversed direction or value"],
   ["Every 24 months",
    "An interval of every 24 months is not stated; the longest is 12 months, for Group I. She is Group II with polycythemia, so her interval is shorter, not longer. Tell: complications shorten the interval.", "reversed direction or value"]],
  C(6), "prognosis", "test"),

V(HOME, IO_F,
  "A 61-year-old man with interstitial lung disease has a resting room-air saturation of 93%. When he walks the hallway it falls to 85%, and with 2 L/min by nasal cannula it rises to 92% while walking. What does he qualify for?",
  [["Oxygen during exertion",
    "Correct. At rest his saturation of 93% is above 88%, but walking drops it to 85%, at or below 88%, and with 2 L/min by cannula it rises to 92%. The exertion criterion is a saturation of 88% or less that improves when oxygen is given, so he qualifies for oxygen during exertion."],
   ["Oxygen at rest",
    "Oxygen at rest requires a resting saturation of 88% or less on room air. His resting value is 93%, so he does not qualify at rest. Tell: the drop happens only while walking, so the qualification is for exertion.", "ruled out by a stated finding"],
   ["Nothing, since rest is normal",
    "A normal resting value does not end the evaluation, because qualification is documented at rest, with exertion and with sleep. His saturation falls to 85% when he walks and improves with oxygen, which meets the exertion criterion. Tell: always test exertion when rest is normal.", "wrong stage or severity"],
   ["Oxygen during sleep",
    "The sleep criterion needs a saturation of 88% or less with a drop of 5% or more from baseline. Nothing in his stem describes sleep testing; his drop was while walking. Tell: sleep oxygen needs a nocturnal drop; his drop was with walking.", "adjacent fact"]],
  C(5), "test finding", "test"),

V(HOME, IO_F,
  "A 69-year-old woman with chronic lung disease drops from 94% to 86% while walking. Oxygen at 2 and then 4 L/min is added, but her saturation stays at 86% while walking. How does this result bear on ambulatory oxygen?",
  [["It does not meet the exertion criterion",
    "Correct. Her saturation falls from 94% to 86% on walking, which is at or below 88%. But the exertion criterion also requires that the saturation improves when oxygen is given, and at 2 and 4 L/min it stays at 86%, so she does not meet the exertion criterion."],
   ["It qualifies her for ambulatory oxygen",
    "The drop to 86% satisfies only half the criterion. Exertion qualification needs the saturation to improve with oxygen, and hers did not improve at 2 or 4 L/min. Tell: a drop alone does not qualify; the improvement with oxygen is required.", "ruled out by a stated finding"],
   ["It qualifies her in Group I at rest",
    "Group I is for a resting saturation of 88% or less on room air. Her resting value was 94%, and her problem is only on exertion, so she does not qualify at rest. Tell: Group I is about rest; her low value appears only with walking.", "adjacent fact"],
   ["It qualifies her for sleep oxygen",
    "The sleep criterion is a saturation of 88% or less with a drop of 5% or more from baseline. Her stem describes walking, not sleep. Tell: the exertion test is the one that applies here, and it was not met.", "adjacent fact"]],
  C(5), "test finding", "test"),

V(HOME, IO_F,
  "A 72-year-old man with chronic obstructive pulmonary disease has a daytime saturation of 93%. Overnight oximetry shows his saturation falling to 87% for long stretches. What does he qualify for?",
  [["Nocturnal oxygen",
    "Correct. His daytime saturation of 93% is normal, but overnight it falls to 87%. The sleep criterion is a saturation of 88% or less with a drop of 5% or more from baseline: 87% is under 88%, and 93 minus 87 is a 6% drop. He qualifies for nocturnal oxygen."],
   ["Continuous oxygen at rest",
    "Continuous oxygen at rest requires a resting room-air saturation of 88% or less. His daytime value is 93%, so he does not qualify for that. Tell: the abnormal reading occurs only overnight, so the qualification is for sleep.", "ruled out by a stated finding"],
   ["Nothing, since daytime is normal",
    "A normal daytime reading does not close the question, because qualification is documented at rest, with exertion and with sleep. His overnight values meet the sleep criterion. Tell: a normal day value with a low overnight value points to sleep qualification.", "wrong stage or severity"],
   ["Oxygen during exertion",
    "The exertion criterion needs a saturation of 88% or less with activity that improves with oxygen. His problem was documented overnight, not with walking. Tell: look at when the low value was recorded; here it was during sleep.", "adjacent fact"]],
  C(5), "test finding", "test"),

V(HOME, IO_F,
  "A 65-year-old woman has a daytime saturation of 95%. Overnight oximetry shows her falling to 91% at the lowest. Does she qualify for nocturnal oxygen?",
  [["No, her sleep value stays above 88%",
    "Correct. Sleep qualification needs a saturation of 88% or less with a drop of 5% or more from baseline. Her lowest value of 91% is above 88%, and 95 minus 91 is only a 4% drop. She fails both parts, so she does not qualify."],
   ["Yes, since she drops during sleep",
    "Dropping during sleep is not enough. The criterion needs a saturation of 88% or less and a drop of 5% or more. Hers falls only 4%, to 91%, which is still above 88%. Tell: both the level and the size of the drop must be met.", "ruled out by a stated finding"],
   ["Yes, in Group II",
    "Group II is the resting category for a saturation of 89% (or arterial oxygen pressure of 56-59 mm Hg) plus pulmonary hypertension, cor pulmonale or a hematocrit above 56%. It does not turn a sleep value of 91% into a qualification. Tell: Group II is about resting values with a comorbidity.", "adjacent fact"],
   ["Yes, if she also has diabetes",
    "Diabetes is not a qualifying comorbidity on the list, which names pulmonary hypertension, cor pulmonale and polycythemia. It would not change a sleep value that fails both thresholds. Tell: her numbers decide, and they fall short.", "adjacent fact"]],
  C(5), "test finding", "test"),

V(HOME, IO_F,
  "A 70-year-old man admitted with a heart failure exacerbation still needs 2 L/min of oxygen on hospital day 1. His team plans to discharge him in a few days. When should his home oxygen qualification be performed?",
  [["At the time of need, before discharge",
    "Correct. The qualification is documented at the time of need, and he still needs 2 L/min with discharge planned in a few days. So the qualification is performed while he is in the hospital, before he leaves, so that home oxygen can be arranged."],
   ["Once he no longer needs oxygen",
    "Once he no longer needs oxygen there is no hypoxia left to document, and qualification rests on documented hypoxia at rest, with exertion or during sleep, performed at the time of need. He still needs 2 L/min now. Tell: qualify while the need is present, not after it resolves.", "wrong stage or severity"],
   ["After a year on home oxygen",
    "Waiting a year is the interval for recertification in Group I, not for the first qualification. He needs his oxygen now and is going home soon, so qualification cannot wait. Tell: the 12-month mark is for renewing, not for starting.", "reversed direction or value"],
   ["At his first outpatient visit",
    "His first outpatient visit comes after discharge, which would leave him without qualified oxygen at home. Documentation is performed at the time of need. Tell: the need arises as he leaves the hospital, so the qualification comes first.", "wrong stage or severity"]],
  C(5), "initial test", "next step"),

V(HOME, IO_F,
  "A 67-year-old woman with lung disease is being assessed for home oxygen. Her resting room-air saturation is 92%. Which is the next step in her qualification?",
  [["Check her saturation with exertion",
    "Correct. A resting saturation of 92% is above the 88% rest cutoff, so rest alone does not qualify her. Qualification is documented during rest, exertion and/or sleep, so the next step is to check her saturation with exertion (and sleep if indicated)."],
   ["Stop: she does not qualify",
    "Stopping at the resting value ignores that hypoxia can be documented with exertion or during sleep. A resting 92% only means she does not meet the rest criterion. Tell: a normal rest value leaves exertion and sleep to be tested.", "wrong stage or severity"],
   ["Prescribe oxygen at 2 L/min now",
    "Prescribing oxygen now has no documented hypoxia behind it. A saturation of 92% at rest does not meet the rest criterion of 88% or less, and a qualifying low value must first be documented. Tell: document first, then prescribe.", "wrong stage or severity"],
   ["Order a complete blood count",
    "A complete blood count would give a hematocrit, which matters only as a comorbidity for a resting saturation of 89% or an arterial oxygen pressure of 56-59 mm Hg. Her resting value of 92% is above both, so the hematocrit is not the next step. Tell: test exertion before looking for comorbidities.", "adjacent fact"]],
  C(5), "initial test", "next step"),

V(HOME, IO_F,
  "A 71-year-old man with chronic obstructive pulmonary disease and cor pulmonale (right-sided heart failure from lung disease) has an arterial oxygen pressure of 58 mm Hg at rest. What is his qualification status?",
  [["Group II, recertified at 3 months",
    "Correct. His arterial oxygen pressure of 58 mm Hg is above the Group I limit of 55 mm Hg but within the 56-59 range, which qualifies only with a comorbidity. He has cor pulmonale, so he is Group II, and Group II is recertified at 3 months."],
   ["Group I, recertified at 12 months",
    "Group I requires an arterial oxygen pressure of 55 mm Hg or less (or a saturation of 88% or less) at rest and is recertified at 12 months. His 58 mm Hg is above that, so he qualifies only through his comorbidity. Tell: 55 or less is Group I; 56-59 plus a comorbidity is Group II.", "adjacent fact"],
   ["Not qualified at 58 mm Hg",
    "He does qualify: 58 mm Hg falls in the 56-59 range, and cor pulmonale is a qualifying comorbidity. The pressure alone would fall short, but together they meet Group II. Tell: the middle range qualifies once a listed comorbidity is present.", "ruled out by a stated finding"],
   ["Qualified for sleep oxygen",
    "His data are resting values, and sleep qualification needs a saturation of 88% or less with a drop of 5% or more from baseline. Nothing about sleep is described. Tell: this is a resting qualification with a comorbidity.", "adjacent fact"]],
  C(6), "test finding", "test"),

# ---------------------------------------------------------------- safety at home
V(SAFE, IO_G,
  "A 72-year-old man starting home oxygen says he smokes on his back porch and that his wife smokes in the kitchen. Which teaching applies?",
  [["No one should smoke in the home",
    "Correct. Home oxygen teaching is that oxygen is highly flammable, and no one should smoke in the home. His wife smokes in the kitchen, inside the home, so the rule applies to her, and the fire danger is the same whoever lights the cigarette."],
   ["His wife may smoke if he is in another room",
    "Her smoking in another room does not remove the hazard. The teaching is no smoking in the home, because oxygen is highly flammable and fire is a listed hazard. Tell: the rule covers the home, not just the room with the tank.", "common lay belief"],
   ["Smoking is fine if the tank is turned off",
    "A tank turned off still holds compressed gas, and oxygen tanks contain compressed gas. The teaching covers the home, not whether the flow is running. Tell: the rule is about the home environment, so flow status does not matter.", "common lay belief"],
   ["He must stop; visitors are exempt",
    "Visitors are not exempt, since the rule is no smoking in the home. The hazard is that oxygen is highly flammable, and a visitor's cigarette ignites it the same way. Tell: the rule has no exemption for anyone who lights a flame in the home.", "common lay belief"]],
  C(7), "education", "education"),

V(SAFE, IO_G,
  "A 69-year-old woman on home oxygen has dry, cracked lips and uses a petroleum jelly lip balm several times a day. Which teaching applies?",
  [["Stop using petroleum-based products",
    "Correct. Petroleum-based products such as lip balms, lotions, oils and grease are to be avoided with home oxygen. Her petroleum jelly lip balm, used several times a day, is exactly that, so she should stop it. Her dry lips are not a reason to keep using it."],
   ["Use more balm to protect the lips",
    "Using more balm adds more of what home oxygen teaching says to avoid: petroleum-based lip balms, lotions, oils and grease. Dry lips do not change that. Tell: protecting the lips with a petroleum product conflicts with oxygen safety.", "reversed direction or value"],
   ["Switch her oxygen to a non-rebreather",
    "A non-rebreather mask is a high-fraction device for severely hypoxic patients who are still ventilating well. Dry lips are not an indication to switch, and the mask would not address the balm. Tell: her issue is a product, not the delivery device.", "adjacent fact"],
   ["Stop her home oxygen",
    "Stopping her oxygen is not called for. The teaching is to avoid petroleum-based products while keeping oxygen use safe, not to discontinue oxygen. Tell: remove the hazard, which is the balm, and keep the oxygen.", "wrong stage or severity"]],
  Cs(7, 15), "education", "education"),

V(SAFE, IO_G,
  "A 74-year-old man on home oxygen has a gas water heater with a pilot light in the hallway where he likes to sit. How far from it should his oxygen be kept?",
  [["At least 10 feet",
    "Correct. Home oxygen teaching is to keep oxygen at least 10 feet from heat sources, which include pilot lights, electric appliances and candles. A gas water heater with a pilot light sits in the hallway where he sits, so his oxygen must be kept at least 10 feet away."],
   ["At least 2 feet",
    "Two feet is far short of the stated distance. Oxygen is highly flammable, and the minimum from heat sources such as pilot lights is at least 10 feet. Tell: the distance in the teaching is 10, not 2.", "reversed direction or value"],
   ["At least 5 feet",
    "Five feet is only half the stated minimum. The teaching specifies at least 10 feet from heat sources, and a pilot light is a flame. Tell: if the number is smaller than 10 feet, it is too close.", "reversed direction or value"],
   ["At least 50 feet",
    "Fifty feet is farther than the stated minimum, and it would be impractical inside a home. The teaching gives at least 10 feet from heat sources. Tell: the guideline is a minimum of 10 feet, not a vague large distance.", "reversed direction or value"]],
  C(7), "education", "education"),

V(SAFE, IO_G,
  "A 77-year-old woman is going home on oxygen tanks. Her son asks what to do with the tanks and how to store them. Which property of the tanks drives the storage and disposal teaching?",
  [["They hold compressed gas",
    "Correct. Oxygen tanks contain compressed gas, and that property drives the teaching on proper storage and disposal. Her son should store the tanks as the teaching directs and not discard them as ordinary trash."],
   ["They hold a liquid fuel",
    "The tanks hold compressed oxygen gas, not a liquid fuel. The flammability teaching is about oxygen supporting a fire, and storage and disposal rules follow from the compressed gas. Tell: the tank holds gas under pressure.", "confused mechanism or drug class"],
   ["They emit carbon monoxide",
    "The tanks do not emit carbon monoxide. Carbon monoxide appears in the teaching only as a reason to have working carbon monoxide alarms. Tell: alarms detect it; tanks hold oxygen.", "confused mechanism or drug class"],
   ["They spoil within a week",
    "Tanks do not spoil. The teaching is about proper storage and disposal because they contain compressed gas. Tell: the concern is pressure and flammability, not a shelf life.", "common lay belief"]],
  C(7), "education", "education"),

V(SAFE, IO_G,
  "A 70-year-old man is setting up home oxygen in a house with old smoke detectors. Which home safety step is taught?",
  [["Working smoke and carbon monoxide alarms, tested monthly",
    "Correct. Home oxygen safety includes working smoke and carbon monoxide alarms, tested monthly. His house has old smoke detectors, so the step is to make sure the alarms work and are tested every month."],
   ["Removing the smoke alarms near the oxygen",
    "Removing the smoke alarms near the oxygen would take away warning of a fire, which is a listed hazard of oxygen. The teaching is for working alarms in the home. Tell: safety adds alarms and keeps them working.", "reversed direction or value"],
   ["Testing the alarms once a year",
    "Testing the alarms once a year is far too infrequent. Home oxygen safety calls for working smoke and carbon monoxide alarms that are tested monthly. Tell: the testing interval is monthly, not yearly.", "reversed direction or value"],
   ["Keeping a candle lit as a warning light",
    "A lit candle is a heat source and a fire hazard near oxygen, not a warning light. Candles are listed among the heat sources to keep at least 10 feet from the oxygen. Tell: candles are something to keep away from oxygen, not a safety measure.", "reversed direction or value"]],
  C(7), "education", "education"),

V(SAFE, IO_G,
  "A 68-year-old woman going home on oxygen asks what signs to post. Which signage is taught?",
  [["No Smoking and Oxygen in Use signs",
    "Correct. Home oxygen teaching is to post No Smoking signage, and potentially Oxygen in Use signs, within the home. Oxygen is highly flammable, and the signs warn everyone who enters, including visitors and firefighters."],
   ["A sign with her oxygen flow rate",
    "A sign with her oxygen flow rate is not part of the signage taught. The taught signs warn about smoking and oxygen use because of the fire hazard. Tell: signs are for warning others, not for recording her prescription.", "adjacent fact"],
   ["A sign with her pharmacy's number",
    "The pharmacy's number is not part of the signage taught. The signs are No Smoking and, potentially, Oxygen in Use. Tell: signage addresses the fire hazard, not contact information.", "common lay belief"],
   ["A sign with her recertification date",
    "Her recertification date is not a posted sign. Recertification is about keeping home oxygen qualified at 12 or 3 months, whereas signs are about safety in the home. Tell: dates belong in her chart; warnings belong on the wall.", "adjacent fact"]],
  C(7), "education", "education"),

# ---------------------------------------------------------------- reading the fraction from the flow
V(FLOW, IO_D,
  "A 63-year-old woman with pneumonia is on a nasal cannula at 2 L/min. Her flow is increased to 5 L/min. About what fraction of inspired oxygen is she receiving now?",
  [["40%",
    "Correct. A nasal cannula at 2 L/min gives about 28%, and each added liter raises the fraction by about 4%. Going from 2 to 5 L/min adds 3 liters, which is 3 x 4% = 12%, so 28% + 12% = 40%. This matches the listed value of 40% at 5 L/min."],
   ["28%",
    "28% is her fraction at the old setting of 2 L/min. Her flow was increased by 3 liters, and each liter adds about 4%, so the new value is 12 points higher. Tell: 28% is the starting point, not the result.", "adjacent fact"],
   ["44%",
    "44% is the cannula's maximum, reached at 6 L/min. She is at 5 L/min, one liter below, so she is about 4% under that cap. Tell: 44% is the ceiling, not her setting.", "adjacent fact"],
   ["60%",
    "60% is above the nasal cannula's range, which tops out at 44%. Fractions of 60% and above come from reservoir-bag masks such as the non-rebreather at 10-15 L/min. Tell: a cannula cannot reach 60%, whatever the knob says.", "reversed direction or value"]],
  Cs(9, 11, 14, 15), "agent/regimen", "test"),

V(FLOW, IO_D,
  "A 75-year-old man's family turned his home nasal cannula up to 9 L/min because he felt short of breath. About what fraction of inspired oxygen does he receive at that setting?",
  [["44%",
    "Correct. A nasal cannula can be turned to any setting, but the fraction stops at 44% (reached at 6 L/min). At 9 L/min he gets no more than that, so the extra 3 liters add oxygen to his nose but not to his fraction."],
   ["56%",
    "56% would follow from continuing to add 4% per liter, but the cannula's fraction maxes out at 44%. The knob can turn over 6 L/min, yet the fraction does not rise. Tell: the cannula has a ceiling; the arithmetic stops at 6 L/min.", "reversed direction or value"],
   ["60%",
    "60% belongs to the low end of a non-rebreather mask's 60-100% range at 10-15 L/min. A cannula does not reach it. Tell: you need a reservoir bag device to get above 44%.", "reversed direction or value"],
   ["100%",
    "100% is the top of the non-rebreather's range, requiring a reservoir bag and 10-15 L/min. A cannula at 9 L/min cannot reach it. Tell: the cannula is a low flow device with a hard ceiling of 44%.", "reversed direction or value"]],
  Cs(9, 11, 14, 15), "agent/regimen", "test"),

V(FLOW, IO_D,
  "A 57-year-old man with bronchitis is placed on a simple mask at 6 to 7 L/min. About what fraction of inspired oxygen is he receiving?",
  [["40%",
    "Correct. A simple mask is a low flow device set at 5-10 L/min, and its fraction depends on the flow: 5-6 L/min gives 35%, 6-7 L/min gives 40%, and 7-8 L/min gives 50%. At 6 to 7 L/min he is receiving about 40%."],
   ["28%",
    "28% is a nasal cannula value at 2 L/min. A simple mask at 6 to 7 L/min delivers more, and the listed value for that flow is 40%. Tell: 28% is a low cannula setting; the mask is higher.", "adjacent fact"],
   ["50%",
    "50% is the simple mask's value at 7-8 L/min, one step higher than his setting. His 6 to 7 L/min corresponds to 40%. Tell: match the flow row; each row steps up by 5 or 10 points.", "adjacent fact"],
   ["80%",
    "80% is far above a simple mask's range of 35-50%. Those values belong to higher-flow, reservoir-bag devices such as the non-rebreather mask at 10-15 L/min. Tell: a simple mask cannot approach 80%.", "reversed direction or value"]],
  Cs(9, 13, 14, 15), "agent/regimen", "test"),
]
