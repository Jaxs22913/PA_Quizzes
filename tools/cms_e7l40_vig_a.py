# -*- coding: utf-8 -*-
"""Lecture 40 vignette pool A -- STOP-Bang totals and risk groups worked from the vignette (s17), when the
questionnaire is and is not used (s16), and polysomnogram event classification (s3).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md: the key names the decisive clue and the fact; each
wrong choice says why it fails for THIS patient, the replacing fact, and a "Tell:". Score items show the
arithmetic letter by letter; every wrong total names the item it missed or wrongly counted.

STOP-Bang rules are the questionnaire picture's own (s17): body mass index MORE than 35, age OLDER than 50, neck
16 inches / 40 cm or larger for anyone, gender male; low 0-2, intermediate 3-4, high 5-8, or yes to 2 or more
of the 4 STOP questions + male gender, + body mass index > 35, or + neck 16 inches / 40 cm = high risk.
The sex-specific risk-factor neck sizes (s6, s7) are never used here (scope SLIDE CONFLICTS).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e7l40_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


def ORD(d, asc):
    d["ordered"] = True; d["asc"] = asc; return d


SDB = "Sleep-disordered breathing"
RISK = "Obstructive sleep apnea: risk and presentation"
DX = "Obstructive sleep apnea: diagnosis"
SB = "STOP-Bang screening"
MGT = "Obstructive sleep apnea: management"
UNT = "Untreated obstructive sleep apnea"
CSA = "Central sleep apnea"
OHSD = "Obesity hypoventilation syndrome: diagnosis"
OHSM = "Obesity hypoventilation syndrome: management and prognosis"

SBX = "STOP-Bang (snoring, tiredness, observed apnea, pressure, body mass index, age, neck, gender)"

QUESTIONS = [

# ---------------------------------------------------------------- STOP-Bang totals and risk groups
V(SB, IO_SCREEN,
  "A 56-year-old man is seen for evaluation before elective knee surgery and has no known sleep disorder. His wife says he snores loudly enough to be heard through closed doors and has seen him stop breathing during sleep. He denies daytime tiredness. He is treated for high blood pressure. His body mass index is 33 kg/m2 and his neck (shirt collar) measures 16.5 inches. What is his " + SBX + " score?",
  [["Score of 6",
    "Correct. Snoring 1 + tired 0 + observed apnea 1 + treated pressure 1 + body mass index 33 (not more than 35) 0 + age 56 (older than 50) 1 + neck 16.5 inches (16 or larger) 1 + male 1 = 6. A score of 5 to 8 places him in the high-risk group for obstructive sleep apnea before his surgery."],
   ["Score of 4",
    "A score of 4 drops two yes answers, such as age and neck: 56 is older than 50, and a 16.5-inch collar meets the 16-inch item. Tell: he meets three of the four Bang items (age, neck, male), on top of three yes answers to the first 4 questions (snoring, observed apnea, pressure).", "adjacent fact"],
   ["Score of 5",
    "A score of 5 misses one yes answer, most often the neck: the questionnaire counts a collar of 16 inches / 40 cm or larger for anyone, so 16.5 inches scores 1. Tell: the neck item has a single cut-off, 16 inches, whatever the patient's sex.", "adjacent fact"],
   ["Score of 7",
    "A score of 7 adds a point for body mass index, but the item asks for more than 35 kg/m2, and his 33 does not qualify. Tell: being obese is not enough for the B item; it needs a body mass index above 35, and his tiredness item is also a no.", "reversed direction or value"]],
  CS(16, 17), "test finding", "classify"),

V(SB, IO_SCREEN,
  "A 50-year-old woman reports loud snoring and feeling tired most days. No one has seen her stop breathing during sleep, and she is not treated for high blood pressure. Her body mass index is 38 kg/m2 and her neck (shirt collar) measures 15 inches. What is her " + SBX + " score?",
  [["Score of 3",
    "Correct. Snoring 1 + tired 1 + observed apnea 0 + pressure 0 + body mass index 38 (more than 35) 1 + age 50 (not older than 50) 0 + neck 15 inches 0 + female 0 = 3. The count alone is intermediate (3 to 4), and her 2 yes answers to the first 4 questions plus a body mass index above 35 meet the questionnaire's added high-risk rule."],
   ["Score of 2",
    "A score of 2 leaves out her body mass index: the B item is yes above 35 kg/m2, and 38 qualifies. Tell: she scores snoring, tiredness and body mass index; only her age, neck, sex, pressure and observed apnea items are no.", "adjacent fact"],
   ["Score of 4",
    "A score of 4 counts her age, but the item asks for age older than 50, and she is exactly 50. Tell: at 50 the age item is still a no; it turns yes at 51, so her total stays at 3.", "reversed direction or value"],
   ["Score of 5",
    "A score of 5 adds both age and neck, and neither qualifies: she is not older than 50, and a 15-inch collar is under the 16-inch item. Tell: her three yes answers are snoring, tiredness and a body mass index above 35.", "reversed direction or value"]],
  CS(16, 17), "risk factors", "classify"),

ORD(V(SB, IO_SCREEN,
  "A 44-year-old man reports loud snoring and daytime sleepiness. His partner has not seen him stop breathing, he is not treated for high blood pressure, his body mass index is 31 kg/m2 and his neck (shirt collar) measures 15 inches. Using the " + SBX + " questionnaire, which result fits him?",
  [["Score 3, high risk",
    "Correct. Snoring 1 + tired 1 + observed 0 + pressure 0 + body mass index 31 (not above 35) 0 + age 44 0 + neck 15 inches 0 + male 1 = 3, which by count alone is intermediate. Yes to 2 or more of the first 4 questions (snoring, tiredness, observed apnea, pressure) plus male gender is its own high-risk rule, so he is high risk."],
   ["Score 2, low risk",
    "A score of 2 leaves out male gender, the G item, which is a yes for him. Tell: with male gender counted his total is 3, and his 2 yes answers to the first 4 questions plus male gender then make him high risk, not low.", "adjacent fact"],
   ["Score 3, intermediate risk",
    "The total of 3 is right, but the band is not the last step: yes to 2 or more of the first 4 questions plus male gender moves a patient to high risk whatever the count. Tell: check the add-on rules before settling on the 3-to-4 band.", "wrong stage or severity"],
   ["Score 4, high risk",
    "A score of 4 counts his body mass index, but the B item asks for more than 35 kg/m2, and 31 does not qualify. Tell: his total is 3, and he is high risk through the male add-on rule, not through a higher count.", "reversed direction or value"]],
  CS(16, 17), "test finding", "classify"), [1, 2, 0, 3]),

ORD(V(SB, IO_SCREEN,
  "A 46-year-old woman feels tired and sleepy most days, and her husband has seen her stop breathing and gasp during sleep. She does not snore loudly and is not treated for high blood pressure. Her body mass index is 37 kg/m2 and her neck (shirt collar) measures 15 inches. Using the " + SBX + " questionnaire, which result fits her?",
  [["Score 3, high risk",
    "Correct. Snoring 0 + tired 1 + observed apnea 1 + pressure 0 + body mass index 37 (more than 35) 1 + age 46 0 + neck 15 inches 0 + female 0 = 3. By count that is intermediate, but yes to 2 or more of the first 4 questions plus a body mass index above 35 is a high-risk rule, so she is high risk."],
   ["Score 2, low risk",
    "A score of 2 misses the body mass index item: 37 kg/m2 is more than 35, so B is a yes. Tell: counting it gives 3, and that same body mass index, with her 2 yes answers to the first 4 questions, lifts her to high risk.", "adjacent fact"],
   ["Score 3, intermediate risk",
    "Her total of 3 is right, but 2 or more yes answers to the first 4 questions plus a body mass index above 35 is a separate high-risk rule. Tell: the 3-to-4 band applies only when none of the add-on rules is met, and she meets the body mass index one.", "wrong stage or severity"],
   ["Score 4, intermediate risk",
    "A score of 4 adds a yes she does not have, such as snoring or neck size: she does not snore loudly, and her 15-inch collar is under 16 inches. Tell: her total is 3, and the risk group still rises to high through the body mass index rule.", "reversed direction or value"]],
  CS(16, 17), "risk factors", "classify"), [1, 2, 0, 3]),

ORD(V(SB, IO_SCREEN,
  "A 42-year-old woman snores loudly and is treated for high blood pressure. She denies daytime tiredness, and no one has seen her stop breathing. Her body mass index is 32 kg/m2 and her neck (shirt collar) measures 16 inches. Using the " + SBX + " questionnaire, which result fits her?",
  [["Score 3, high risk",
    "Correct. Snoring 1 + tired 0 + observed 0 + treated pressure 1 + body mass index 32 (not above 35) 0 + age 42 0 + neck 16 inches 1 + female 0 = 3. By count that is intermediate, but yes to 2 or more of the first 4 questions plus a neck of 16 inches / 40 cm is a high-risk rule, so she is high risk."],
   ["Score 2, low risk",
    "A score of 2 misses the neck item: the questionnaire counts a collar of 16 inches / 40 cm or larger, and hers is 16 inches. Tell: with the neck counted she has 3, and the neck with 2 yes answers to the first 4 questions makes her high risk.", "adjacent fact"],
   ["Score 3, intermediate risk",
    "The total of 3 is right, but 2 or more yes answers to the first 4 questions plus a neck of 16 inches / 40 cm is a separate high-risk rule. Tell: the 3-to-4 band holds only when no add-on rule is met, and her neck meets one.", "wrong stage or severity"],
   ["Score 4, high risk",
    "A score of 4 counts her body mass index, but the B item asks for more than 35 kg/m2, and 32 does not qualify. Tell: her total is 3; she reaches high risk through the neck rule, not through a higher count.", "reversed direction or value"]],
  CS(16, 17), "test finding", "classify"), [1, 2, 0, 3]),

ORD(V(SB, IO_SCREEN,
  "A 35-year-old woman snores loudly. She feels rested during the day, no one has seen her stop breathing, and she is not treated for high blood pressure. Her body mass index is 36 kg/m2 and her neck (shirt collar) measures 14 inches. Using the " + SBX + " questionnaire, which result fits her?",
  [["Score 2, low risk",
    "Correct. Snoring 1 + tired 0 + observed 0 + pressure 0 + body mass index 36 (more than 35) 1 + age 35 0 + neck 14 inches 0 + female 0 = 2, the low-risk band (0 to 2). The body mass index rule needs 2 or more yes answers to the first 4 questions, and she has 1, so she stays low risk."],
   ["Score 1, low risk",
    "A score of 1 leaves out her body mass index: 36 kg/m2 is more than 35, so the B item is a yes. Tell: her two yes answers are snoring and body mass index, which still sit in the 0-to-2 band.", "adjacent fact"],
   ["Score 2, high risk",
    "The body mass index rule moves a patient to high risk only with yes to 2 or more of the first 4 questions (snoring, tiredness, observed apnea, pressure). Tell: snoring is her single yes among the first 4 questions, so the rule is not met and her total of 2 stays low risk.", "wrong stage or severity"],
   ["Score 3, intermediate risk",
    "A score of 3 adds a yes she does not have: she feels rested, has no observed apneas, no treated pressure, is under 50 and has a 14-inch collar. Tell: her total is 2, snoring plus body mass index above 35.", "reversed direction or value"]],
  CS(16, 17), "risk factors", "classify"), [1, 0, 2, 3]),

ORD(V(SB, IO_SCREEN,
  "A 63-year-old woman snores loudly, feels tired during the day and is treated for high blood pressure. No one has seen her stop breathing. Her body mass index is 34 kg/m2 and her neck (shirt collar) measures 15.5 inches. Using the " + SBX + " questionnaire, which result fits her?",
  [["Score 4, intermediate risk",
    "Correct. Snoring 1 + tired 1 + observed 0 + treated pressure 1 + body mass index 34 (not above 35) 0 + age 63 (older than 50) 1 + neck 15.5 inches 0 + female 0 = 4, the intermediate band (3 to 4). She has 3 yes answers to the first 4 questions, but none of the add-ons (male, body mass index above 35, neck 16 inches) applies."],
   ["Score 3, intermediate risk",
    "A score of 3 misses her age: she is 63, older than 50, so the A item is a yes. Tell: her four yes answers are snoring, tiredness, treated pressure and age, and the band stays intermediate either way.", "adjacent fact"],
   ["Score 4, high risk",
    "The add-on rules need 2 or more yes answers to the first 4 questions plus male gender, a body mass index above 35 or a 16-inch neck. Tell: she is female, her body mass index is 34 and her collar is 15.5 inches, so she stays in the 3-to-4 band.", "wrong stage or severity"],
   ["Score 5, high risk",
    "A score of 5 counts her body mass index, but 34 kg/m2 is not more than 35. Tell: without the B item her total is 4, and her neck of 15.5 inches is also under the 16-inch item.", "reversed direction or value"]],
  CS(16, 17), "test finding", "classify"), [1, 0, 2, 3]),

V(SB, IO_SCREEN,
  "A 51-year-old man is evaluated before elective surgery. He snores loudly and is treated for high blood pressure. He feels rested during the day, and his wife has not seen him stop breathing. His body mass index is 35 kg/m2 and his neck (shirt collar) measures 17 inches. What is his " + SBX + " score?",
  [["Score of 5",
    "Correct. Snoring 1 + tired 0 + observed 0 + treated pressure 1 + body mass index 35 (not more than 35) 0 + age 51 (older than 50) 1 + neck 17 inches 1 + male 1 = 5, the high-risk band (5 to 8). He would also be high risk through 2 yes answers to the first 4 questions plus male gender."],
   ["Score of 4",
    "A score of 4 drops a yes he meets, such as age: 51 is older than 50, so the A item counts. Tell: his yes answers are snoring, pressure, age, neck and male gender, five in all.", "adjacent fact"],
   ["Score of 6",
    "A score of 6 counts his body mass index, but the item asks for more than 35 kg/m2, and exactly 35 is not more. Tell: the B item stays a no at 35; his five yes answers come from snoring, pressure, age, neck and male gender.", "reversed direction or value"],
   ["Score of 7",
    "A score of 7 adds two items he does not meet: a body mass index of exactly 35 (the item needs more than 35) and daytime tiredness, which he denies. Tell: the total is 5, already in the high-risk band.", "reversed direction or value"]],
  CS(16, 17), "risk factors", "classify"),
# ---------------------------------------------------------------- when the questionnaire is used
V(SB, IO_SCREEN,
  "A 39-year-old woman with no sleep complaints asks, at a community health fair, to fill out a sleep apnea screening questionnaire to learn whether she has obstructive sleep apnea. What should she be told?",
  [["It cannot accurately screen her",
    "Correct. Screening questionnaires should not be routinely used to screen for obstructive sleep apnea in the community, and the questionnaire cannot serve as a true, accurate screening tool in asymptomatic patients. Its value lies in highly symptomatic patients in high-risk settings, such as a preoperative evaluation."],
   ["A low score rules the disease out",
    "The questionnaire is not an accurate screen in people without symptoms, so a reassuring score in a woman with no complaints does not settle the question. Tell: its use is limited to highly symptomatic patients in high-risk settings such as preoperative evaluation.", "common lay belief"],
   ["A high score confirms the disease",
    "A questionnaire sorts patients into low, intermediate or high risk; the diagnosis comes from a polysomnogram showing 5 or more obstructive events per hour with symptoms, or 15 or more. Tell: a score names a risk group, not a diagnosis.", "adjacent fact"],
   ["It is the routine community screen",
    "Screening questionnaires should not be routinely used in the community. Tell: the questionnaire's place is preoperative evaluation of people without a known diagnosis who may be at risk for perioperative complications, not community screening.", "reversed direction or value"]],
  CS(16, 17, 9), "education", "education"),

V(SB, IO_SCREEN,
  "A 58-year-old man with loud snoring, witnessed apneas and daytime sleepiness is seen for evaluation before elective surgery. He has never been tested for sleep apnea. Which property makes the " + SBX + " questionnaire suited to this visit?",
  [["Highest sensitivity of the questionnaires",
    "Correct. The questionnaire has been used as a preoperative evaluation tool for people without a known diagnosis of obstructive sleep apnea who may be at risk for perioperative complications, and it has the highest sensitivity among the questionnaires. A highly symptomatic patient in a high-risk setting is where it has value."],
   ["Highest specificity of the questionnaires",
    "The questionnaire is singled out for the highest sensitivity among the questionnaires, the property that suits catching at-risk patients before surgery. Tell: its strength is not missing people at risk, which is sensitivity, not specificity.", "reversed direction or value"],
   ["It confirms the diagnosis before surgery",
    "A questionnaire estimates risk; obstructive sleep apnea is confirmed on a polysomnogram, with 5 or more obstructive events per hour plus symptoms, or 15 or more. Tell: the score places him in a risk group and does not replace the sleep study.", "adjacent fact"],
   ["It grades his disease severity",
    "Severity is measured during a sleep study: a split-night polysomnogram records the first 2 hours of sleep to determine severity. Tell: the questionnaire gives a low, intermediate or high risk of having the disease, not a grade of disease he has.", "confused mechanism or drug class"]],
  CS(16, 17, 8, 9), "initial test", "test"),

# ---------------------------------------------------------------- polysomnogram event types
V(SDB, IO_A,
  "A 52-year-old man's polysomnogram shows repeated events in which thermistor airflow falls by 90% or more for 15 seconds while chest and abdominal respiratory effort continue. How is each event classified?",
  [["Obstructive apnea",
    "Correct. An apnea is a 90% or greater fall in airflow on the thermistor lasting at least 10 seconds, and when airflow stops but respiratory effort continues, the apnea is obstructive. The airway collapses while the patient still tries to breathe, the event pattern of obstructive sleep apnea."],
   ["Central apnea",
    "A central apnea has no airflow and no respiratory effort, because the brainstem stops sending the signal to breathe. Tell: his chest and abdomen keep moving throughout each event, so effort is present and the event is not central.", "ruled out by a stated finding"],
   ["Mixed apnea",
    "A mixed apnea opens with no respiratory effort, and effort resumes only during the latter part of the event. Tell: his effort is present from the start of each event to its end, which is the obstructive pattern rather than the mixed one.", "adjacent fact"],
   ["Hypopnea",
    "A hypopnea is slowed, shallow, restricted breathing in repeated episodes of 10 seconds or longer, short of a near-total stop. Tell: a fall in airflow of 90% or more is near or total cessation of breathing, which defines an apnea.", "wrong stage or severity"]],
  CS(3, 24), "test finding", "classify"),

V(SDB, IO_A,
  "A 64-year-old woman's polysomnogram shows events with no airflow. In each, there is no respiratory effort during the first part of the event, and effort resumes during the latter part while airflow is still absent. How are these events classified?",
  [["Mixed apnea",
    "Correct. A mixed apnea has no airflow, with a lack of respiratory effort during the first part of the event and resumption of effort during the latter part. Her events begin like central apneas and end like obstructive ones, which is exactly the mixed pattern."],
   ["Obstructive apnea",
    "An obstructive apnea has no airflow with continued respiratory effort throughout, the airway collapsing while the patient tries to breathe. Tell: her events open with no effort at all, which an obstructive event does not show.", "ruled out by a stated finding"],
   ["Central apnea",
    "A central apnea has no airflow and no respiratory effort for the whole event. Tell: effort comes back during the latter part of each of her events, so the event does not stay central from start to finish.", "ruled out by a stated finding"],
   ["Hypopnea",
    "A hypopnea is slowed, shallow, restricted breathing in repeated episodes of 10 seconds or longer, with airflow reduced rather than absent. Tell: her airflow is absent, so these are apneas, and the effort pattern makes them mixed.", "wrong stage or severity"]],
  C(3), "test finding", "classify"),

V(SDB, IO_A,
  "A 47-year-old man's polysomnogram shows repeated episodes, each 10 seconds or longer, of slowed, shallow, restricted breathing. Airflow is reduced but does not fall by 90%. How are these episodes classified?",
  [["Hypopneas",
    "Correct. A hypopnea is slowed, shallow, restricted breathing that occurs repeatedly during sleep in episodes of 10 seconds or longer. An apnea needs a fall in airflow of 90% or more for at least 10 seconds, which his episodes do not reach, so these are hypopneas."],
   ["Obstructive apneas",
    "An obstructive apnea is a fall in airflow of 90% or more for at least 10 seconds with continued respiratory effort. Tell: his airflow stays above that threshold, so the episodes are hypopneas whatever the effort channel shows.", "wrong stage or severity"],
   ["Central apneas",
    "A central apnea has no airflow and no respiratory effort, because the brainstem stops signaling. Tell: he keeps breathing, slowly and shallowly, so neither airflow nor effort has stopped during these episodes.", "ruled out by a stated finding"],
   ["Mixed apneas",
    "A mixed apnea has no airflow, with effort absent at first and resuming during the latter part of the event. Tell: his airflow is reduced, not absent, so there is no apnea here to classify as mixed.", "ruled out by a stated finding"]],
  C(3), "test finding", "classify"),

# ---------------------------------------------------------------- obstructive sleep apnea: risk and presentation
V(RISK, IO_A,
  "A 48-year-old man has loud, habitual snoring, unrefreshing sleep, morning headaches and nocturia. His wife has seen him stop breathing and wake gasping. His blood pressure is poorly controlled on two medicines. His neck circumference is 18 inches, and his posterior oropharynx is crowded. What is the most likely diagnosis?",
  [["Obstructive sleep apnea",
    "Correct. Loud habitual snoring, witnessed apneas, awakening with gasping, unrefreshing sleep, morning headaches, nocturia and poorly controlled hypertension are its history findings, and a large neck and a crowded posterior oropharynx are its examination findings. Narrowing of the upper airway by soft tissue or structure causes it."],
   ["Central sleep apnea",
    "Central sleep apnea sounds very similar, with insomnia, frequent awakenings and daytime sleepiness, but snoring is less common and it clusters with heart failure, stroke, opioids or high altitude. Tell: loud habitual snoring and a crowded oropharynx point to an obstructed airway.", "competing diagnosis"],
   ["Obesity hypoventilation syndrome",
    "Obesity hypoventilation syndrome needs obesity (body mass index above 30) plus awake hypoventilation, an arterial carbon dioxide pressure above 45 mm Hg, with other causes excluded. Tell: nothing here shows awake hypercapnia; his findings are those of an airway that obstructs at night.", "competing diagnosis"],
   ["Narcolepsy",
    "Narcolepsy is listed with the other causes of daytime sleepiness in the differential. Tell: it does not explain witnessed apneas, gasping awakenings and loud snoring, which are events of an airway obstructing during sleep.", "competing diagnosis"]],
  CS(5, 7, 10, 24, 25, 32), "manifestation", "diagnosis"),

V(RISK, IO_A,
  "A 49-year-old woman has loud snoring, daytime sleepiness and witnessed apneas. She also reports fatigue and weight gain, and her clinician suspects hypothyroidism as a concomitant condition. Which blood test is added to her sleep evaluation?",
  [["Thyroid-stimulating hormone",
    "Correct. Hypothyroidism is a concomitant medical condition listed among the risk factors for obstructive sleep apnea, and a thyroid-stimulating hormone level is part of the diagnostic workup when hypothyroidism is suspected, alongside the polysomnogram that diagnoses the sleep disorder."],
   ["Serum bicarbonate",
    "A raised serum bicarbonate is a screening clue for obesity hypoventilation syndrome; above 27 it calls for an arterial blood gas. Tell: the suspicion here is thyroid disease, which a thyroid-stimulating hormone level addresses.", "adjacent fact"],
   ["C-reactive protein",
    "C-reactive protein rises as an endocrine effect of untreated obstructive sleep apnea; it does not test for a concomitant condition. Tell: the condition suspected here is hypothyroidism, which is checked with a thyroid-stimulating hormone level.", "adjacent fact"],
   ["Arterial blood gas",
    "An arterial blood gas shows awake hypoventilation, an arterial carbon dioxide pressure above 45 mm Hg, when obesity hypoventilation syndrome is suspected. Tell: thyroid disease is the concern here, and the thyroid-stimulating hormone level is the test named for it.", "adjacent fact"]],
  CS(6, 8, 21, 32), "initial test", "test"),

V(RISK, IO_A,
  "A 57-year-old man with newly diagnosed obstructive sleep apnea drinks several glasses of wine each night and takes an over-the-counter sedative to fall asleep. Which advice addresses these modifiable risk factors?",
  [["Avoid alcohol and other sedatives",
    "Correct. Use of alcohol or sedatives is a risk factor for obstructive sleep apnea, and the risk modifications are to avoid alcohol and other sedatives, along with diet and exercise for weight loss. Both his nightly wine and his sleep aid fall under that advice."],
   ["Keep the sedative, stop the wine",
    "Stopping the wine while keeping the sedative leaves one of the two named risk factors in place. Tell: the advice covers alcohol and other sedatives together, so the over-the-counter sleep aid has to go as well as the wine.", "adjacent fact"],
   ["Keep the wine, stop the sedative",
    "Stopping the sedative while keeping the wine leaves alcohol, itself a listed risk factor, in his nightly routine. Tell: risk modification names alcohol together with other sedatives, so the wine is part of the problem too.", "common lay belief"],
   ["Take both earlier in the evening",
    "Changing the timing still leaves alcohol and a sedative in his routine, and the risk modification is to avoid them. Tell: the advice is avoidance of alcohol and other sedatives, not rescheduling them around bedtime.", "common lay belief"]],
  CS(6, 15), "education", "education"),

V(RISK, IO_A,
  "A 45-year-old man with obstructive sleep apnea has a body mass index of 36 kg/m2. He asks what he can do himself, in addition to using his positive airway pressure device. Which risk modification fits him?",
  [["Diet and exercise for weight loss",
    "Correct. Obesity heads the risk factors for obstructive sleep apnea, and diet and exercise for weight loss is a named risk modification, together with avoiding alcohol and other sedatives. Bariatric surgery for weight loss may also be helpful."],
   ["Sleeping on his back each night",
    "Positional therapy keeps the patient on his side, with a sleep belt or sleep shirt, when events occur while supine. Tell: lying on his back is the position the therapy avoids; for his obesity the self-care step is weight loss.", "reversed direction or value"],
   ["A nightly sedative to deepen sleep",
    "Sedatives are a risk factor for obstructive sleep apnea, and the advice is to avoid them. Tell: a sedative works against him; diet and exercise for weight loss is the change that addresses his body mass index of 36.", "reversed direction or value"],
   ["An evening glass of wine to relax",
    "Alcohol is a risk factor, and avoiding alcohol and other sedatives is a named risk modification. Tell: relaxing with wine works against him; diet and exercise for weight loss target his obesity.", "common lay belief"]],
  CS(6, 12, 13, 15), "education", "treatment"),

]
