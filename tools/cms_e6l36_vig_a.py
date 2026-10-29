# -*- coding: utf-8 -*-
"""Lecture 36 vignette pool A -- Chronic obstructive pulmonary disease: recognizing the disease and its
subtypes, and scoring the patient (airflow grade, symptom test total, dyspnea grade, group in both schemes,
and the survival index).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md (2026-10-29). Score items show the arithmetic
item by item; numeric options are ascending.

Exacerbation histories are 0, or 2 or more, or a hospitalization -- never the single moderate exacerbation
that the slides and the recording disagree on (cms_e6l36_scope.py). Survival-index walk distances avoid
250-349 meters (the slide's "250-249" typo).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e6l36_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


def ORD(d, asc):
    d["ordered"] = True; d["asc"] = asc; return d


REC = "Recognizing the disease"
AAT = "Alpha-1 antitrypsin deficiency"
GRD = "Airflow grade"
SYM = "Symptom scores"
GRP = "Group assignment"
PRG = "Prognosis"

QUESTIONS = [

# ---------------------------------------------------------------- recognizing the disease
V(REC, IO_PFT,
  "A 58-year-old woman with a 35 pack-year smoking history has 3 years of slowly worsening shortness of breath on exertion and a morning cough. Post-bronchodilator spirometry shows a ratio of forced expiratory volume in 1 second to forced vital capacity of 0.62, and the 1-second volume improved 5% after albuterol. Which diagnosis is most likely?",
  [["Chronic obstructive lung disease",
    "Correct. Progressive exertional dyspnea and cough in a heavy smoker, with a post-bronchodilator ratio of 0.62 (below 0.70) and only a 5% response (under 12%), confirm persistent, irreversible obstruction, the spirometric definition of this disease."],
   ["Asthma",
    "Asthma's obstruction is reversible, with an improvement of 12% or more after a bronchodilator. Her response was only 5%. Tell: a small response plus a ratio below 0.70 in a long-time smoker points to fixed obstruction.", "ruled out by a stated finding"],
   ["Heart failure",
    "Heart failure is on the differential for dyspnea on exertion, but it does not produce a ratio below 0.70 on spirometry. Tell: obstruction confirmed after the bronchodilator places the problem in the airways.", "competing diagnosis"],
   ["Pulmonary fibrosis",
    "Pulmonary fibrosis is restrictive: the ratio is normal and the forced vital capacity low. Her ratio is 0.62. Tell: a low ratio means obstruction, the opposite of fibrosis.", "ruled out by a stated finding"]],
  CS(4, 26), "test finding", "diagnosis"),

V(REC, IO_A,
  "A 66-year-old thin man with a long smoking history breathes through pursed lips. He has a barrel chest, distant breath sounds and hyperresonance to percussion. His diffusing capacity is reduced, and he produces little sputum. Which subtype best describes his disease?",
  [["Emphysema subtype",
    "Correct. A thin patient with pursed-lip breathing, barrel chest, distant breath sounds and hyperresonance, little sputum, and a reduced diffusing capacity is the classic emphysema picture (the pink puffer), from alveolar destruction and loss of elastic recoil."],
   ["Chronic bronchitis subtype",
    "The chronic bronchitis subtype brings cough with sputum, rhonchi, possible cyanosis and edema, and a normal or near-normal diffusing capacity. He has little sputum and a reduced diffusing capacity. Tell: the reduced diffusing capacity singles out emphysema.", "ruled out by a stated finding"],
   ["Asthma",
    "Asthma's exam is often normal between exacerbations, and it does not destroy alveoli or lower diffusing capacity. Tell: a barrel chest with a reduced diffusing capacity in a long-time smoker is emphysema.", "competing diagnosis"],
   ["Pulmonary fibrosis",
    "Fibrosis is restrictive and shrinks the lungs, so hyperresonance and a barrel chest from hyperinflation do not fit. Tell: his findings show too much air in the chest, not too little.", "competing diagnosis"]],
  CS(14, 15, 20), "manifestation", "diagnosis"),

V(REC, IO_A,
  "A 61-year-old man who smokes has coughed up thick sputum most days for 4 months of each of the last 3 years. He has rhonchi, bluish lips and swelling of both ankles. His blood gas shows low oxygen and raised carbon dioxide, and his diffusing capacity is near normal. Post-bronchodilator spirometry shows a ratio of 0.64. Which subtype best describes his disease?",
  [["Chronic bronchitis subtype",
    "Correct. Productive cough for at least 3 months a year over 2 years, rhonchi, cyanosis, edema, early hypoxemia and hypercapnia, and a near-normal diffusing capacity, with confirmed obstruction (ratio 0.64), are the chronic bronchitis picture (the blue bloater)."],
   ["Emphysema subtype",
    "Emphysema brings a thin, pursed-lip breather with preserved gas exchange until late and a reduced diffusing capacity. He has early hypoxemia and hypercapnia with a near-normal diffusing capacity. Tell: sputum, cyanosis and edema point to bronchitis.", "ruled out by a stated finding"],
   ["Chronic bronchitis without obstruction",
    "Chronic bronchitis without airflow obstruction is not this disease, but his ratio of 0.64 confirms obstruction. Tell: once the ratio is below 0.70, his chronic cough places him in the chronic bronchitis subtype.", "ruled out by a stated finding"],
   ["Asthma",
    "Asthma does not usually bring years of daily sputum, cyanosis, edema and chronic carbon dioxide retention in a smoker. Tell: his cough history meets the chronic bronchitis definition, with persistent obstruction.", "competing diagnosis"]],
  CS(6, 14, 15), "manifestation", "diagnosis"),

V(AAT, IO_A,
  "A 38-year-old woman who has never smoked has progressive exertional dyspnea. Post-bronchodilator spirometry shows a ratio of 0.58, and her chest x-ray shows emphysema mainly at the lung bases. Her father had emphysema in his 40s. Which underlying cause is most likely?",
  [["Alpha-1 antitrypsin deficiency",
    "Correct. Emphysema in a young person (45 or under), in a nonsmoker, predominantly basilar on the chest x-ray, and with a family history of emphysema are the suggestive features of alpha-1 antitrypsin deficiency, which causes panlobular, lower-lobe disease."],
   ["Tobacco smoke exposure",
    "Smoking is the primary cause overall, but she has never smoked, and smoking causes centrilobular, upper-lobe emphysema. Tell: basal emphysema in a young nonsmoker with an affected father points to the inherited deficiency.", "ruled out by a stated finding"],
   ["Household biomass smoke",
    "Biomass burning is a major risk in low- and middle-income countries, but nothing in her history mentions it, and it would not explain an affected father or basal emphysema at 38. Tell: the family history and lower-lobe pattern suggest a genetic cause.", "competing diagnosis"],
   ["Asthma with remodeling",
    "Asthma can occasionally become irreversible, but it does not destroy the lung bases or run with a family history of early emphysema. Tell: basilar emphysema in a young nonsmoker is the deficiency pattern.", "competing diagnosis"]],
  CS(10, 14, 19), "risk factors", "diagnosis"),

V(AAT, IO_PFT,
  "A 41-year-old man with minimal smoking history has emphysema with a post-bronchodilator ratio of 0.61. His chest x-ray shows the changes mainly in the lower lobes. Which test is most appropriate to find the cause?",
  [["Alpha-1 antitrypsin level and genotype",
    "Correct. Patients under 45, or without significant exposure, should be evaluated for alpha-1 antitrypsin deficiency, and basilar emphysema adds to the suspicion. A level below 11 micromol/L with a severely deficient genotype is diagnostic."],
   ["Computed tomography of the chest",
    "Chest computed tomography can categorize emphysema but is generally not needed and does not identify the cause. Tell: the deficiency is diagnosed by the enzyme level and genotype.", "adjacent fact"],
   ["Arterial blood gas",
    "An arterial blood gas is usually done only in a deteriorating or severe exacerbation. Tell: it describes gas exchange, not why a 41-year-old with little exposure has basal emphysema.", "adjacent fact"],
   ["B-type natriuretic peptide",
    "B-type natriuretic peptide is checked when associated heart failure is suspected. Tell: his age, minimal smoking and lower-lobe emphysema call for an alpha-1 antitrypsin level.", "adjacent fact"]],
  CS(10, 19, 30), "initial test", "test"),

# ---------------------------------------------------------------- airflow grade
ORD(V(GRD, IO_OBS,
  "A 67-year-old man has a post-bronchodilator ratio of 0.55 and a forced expiratory volume in 1 second of 34% predicted. Which airflow grade fits?",
  [["Grade 3 (severe)",
    "Correct. With the ratio below 0.70, the grade comes from the post-bronchodilator 1-second volume: 34% sits in the 30% to 49% band, grade 3, severe. Grade 4 would need less than 30%."],
   ["Grade 1 (mild)",
    "Grade 1, mild, needs 80% predicted or more; at 34% he is far below. Tell: grade 1 is near-normal airflow, and he has about a third of predicted. His ratio confirms obstruction; the grade then depends on the 1-second volume.", "wrong stage or severity"],
   ["Grade 2 (moderate)",
    "Grade 2, moderate, covers 50% up to 80% predicted; 34% is below that range. Tell: under 50% the grade is at least severe. Moderate means at least half of predicted airflow, which he does not have.", "wrong stage or severity"],
   ["Grade 4 (very severe)",
    "Grade 4, very severe, is below 30% predicted. At 34% he is just above that cutoff. Tell: 30% to 49% is grade 3, so 34% stays severe. A 4-point margin still counts; the bands do not round.", "wrong stage or severity"]],
  C(34), "test finding", "classify"), [1, 2, 0, 3]),

ORD(V(GRD, IO_OBS,
  "A 59-year-old woman has a post-bronchodilator ratio of 0.66 and a forced expiratory volume in 1 second of 83% predicted. Which airflow grade fits?",
  [["Grade 1 (mild)",
    "Correct. Her ratio of 0.66 confirms obstruction, and a post-bronchodilator 1-second volume of 83% predicted meets the grade 1 (mild) threshold of 80% or more. Her airflow is near normal even though the ratio is abnormal."],
   ["Grade 2 (moderate)",
    "Grade 2, moderate, covers 50% up to 80% predicted. At 83% she is above it. Tell: 80% or more is grade 1. Her ratio confirms the disease, but her airflow is near normal, so the mildest grade applies.", "wrong stage or severity"],
   ["Grade 3 (severe)",
    "Grade 3, severe, covers 30% to 49% predicted, far below her 83%. Tell: a near-normal 1-second volume cannot be severe, whatever the ratio. The ratio confirms obstruction; it does not set the grade.", "wrong stage or severity"],
   ["Grade 4 (very severe)",
    "Grade 4, very severe, is below 30% predicted; she has 83%. Tell: very severe means less than a third of predicted airflow. Her low ratio alone does not raise the grade; only the 1-second volume does.", "wrong stage or severity"]],
  C(34), "test finding", "classify"), [0, 1, 2, 3]),

ORD(V(GRD, IO_OBS,
  "A 72-year-old man has a post-bronchodilator ratio of 0.48 and a forced expiratory volume in 1 second of 26% predicted. Which airflow grade fits?",
  [["Grade 4 (very severe)",
    "Correct. With the ratio below 0.70, a post-bronchodilator 1-second volume of 26% predicted is below 30%, grade 4, very severe. Grade 3 covers 30% to 49%."],
   ["Grade 1 (mild)",
    "Grade 1, mild, needs 80% predicted or more. At 26% he is far below. Tell: his airflow is about a quarter of predicted. His very low ratio and 26% airflow both show advanced obstruction.", "wrong stage or severity"],
   ["Grade 2 (moderate)",
    "Grade 2, moderate, covers 50% up to 80% predicted. At 26% he is well under it. Tell: under 30% is the very severe band. Moderate means at least half of predicted airflow.", "wrong stage or severity"],
   ["Grade 3 (severe)",
    "Grade 3, severe, is 30% to 49% predicted. At 26% he has dropped below its lower limit. Tell: below 30% is grade 4. Severe stops at 30%; anything lower is very severe.", "wrong stage or severity"]],
  C(34), "test finding", "classify"), [1, 2, 3, 0]),

# ---------------------------------------------------------------- symptom scores
ORD(V(SYM, IO_OBS,
  "A 64-year-old woman completes the 8-item symptom assessment test, each item scored 0 to 5: cough 2, phlegm 1, chest tightness 1, breathlessness on a hill or flight of stairs 3, limitation of home activities 2, confidence leaving home 1, sleep 1, and energy 2. What is her total score?",
  [["13",
    "Correct. Cough 2 + phlegm 1 + chest tightness 1 + breathlessness on stairs 3 + home activities 2 + confidence leaving home 1 + sleep 1 + energy 2 = 13. A total of 10 or more counts as more symptoms when assigning her group."],
   ["11",
    "Eleven drops 2 points, as if the energy item (2) were left out. Tell: all 8 items count, so add energy back: 11 + 2 = 13. Either way, her total of 13 is above the line of 10.", "reversed direction or value"],
   ["12",
    "Twelve misses 1 point, as if one of the 1-point items (phlegm, chest tightness, confidence or sleep) were skipped. Tell: there are four 1-point items, and all of them count.", "reversed direction or value"],
   ["14",
    "Fourteen adds a point that is not there, as if breathlessness on stairs were scored 4 instead of 3. Tell: recheck each item; the correct sum is 13. An extra point would not change her group, but it is not the sum.", "reversed direction or value"]],
  C(23), "test finding", "classify"), [1, 2, 0, 3]),

ORD(V(SYM, IO_OBS,
  "A 69-year-old man with chronic obstructive pulmonary disease says that, walking on level ground, he has to stop for breath after about 100 meters or after a few minutes. Which modified Medical Research Council dyspnea grade fits?",
  [["Grade 3",
    "Correct. Grade 3 is stopping for breath after walking about 100 meters or after a few minutes on the level. A grade of 2 or more counts as more symptoms, which places him in group B or E depending on exacerbation risk."],
   ["Grade 1",
    "Grade 1 is shortness of breath when hurrying on the level or walking up a slight hill. Tell: he stops on level ground after about 100 meters, a heavier limitation.", "wrong stage or severity"],
   ["Grade 2",
    "Grade 2 is walking slower than people of the same age on the level, or stopping for breath at one's own pace. Tell: a defined stop at about 100 meters or a few minutes is grade 3.", "wrong stage or severity"],
   ["Grade 4",
    "Grade 4 is being too breathless to leave the house, or breathless when dressing or undressing. Tell: he still walks outside, stopping after 100 meters, which is grade 3.", "wrong stage or severity"]],
  C(24), "test finding", "classify"), [1, 2, 0, 3]),

ORD(V(SYM, IO_OBS,
  "A 62-year-old woman with chronic obstructive pulmonary disease says she walks slower than friends her age on level ground because of breathlessness, but she does not need to stop. Which modified Medical Research Council dyspnea grade fits?",
  [["Grade 2",
    "Correct. Grade 2 is walking slower than people of the same age on the level because of breathlessness, or having to stop for breath at one's own pace on the level. A grade of 2 or more counts as more symptoms."],
   ["Grade 0",
    "Grade 0 is breathlessness only with strenuous exercise. Tell: she is slowed on ordinary level walking, which is beyond grade 0. Grade 0 counts as fewer symptoms; she has more.", "wrong stage or severity"],
   ["Grade 1",
    "Grade 1 is shortness of breath when hurrying on the level or walking up a slight hill. Tell: she is slowed at a normal pace, not only when hurrying, which is grade 2.", "wrong stage or severity"],
   ["Grade 3",
    "Grade 3 is stopping for breath after about 100 meters or a few minutes on the level. Tell: she does not need to stop, so she has not reached grade 3. Grade 2 already counts as more symptoms.", "wrong stage or severity"]],
  C(24), "test finding", "classify"), [1, 2, 0, 3]),

# ---------------------------------------------------------------- group assignment
V(GRP, IO_OBS,
  "A 57-year-old man with confirmed chronic obstructive pulmonary disease has a symptom assessment test score of 7 and a modified Medical Research Council dyspnea grade of 1. He has had no exacerbations in the past year. Under the current three-group scheme, which group is he in?",
  [["Group A",
    "Correct. A symptom score of 7 (under 10) and a dyspnea grade of 1 (0 to 1) mean fewer symptoms, and no exacerbations means low risk. Low symptoms with low risk is group A, which starts with a single bronchodilator."],
   ["Group B",
    "Group B is low risk with more symptoms: a symptom score of 10 or more or a dyspnea grade of 2 or more. His 7 and grade 1 are below both. Tell: fewer symptoms keep him in A.", "wrong stage or severity"],
   ["Group E",
    "Group E is high risk: 2 or more moderate exacerbations or 1 hospitalization in the past year. He had none. Tell: without exacerbations, his group is set by symptoms alone.", "wrong stage or severity"],
   ["Group C",
    "Group C belongs to the 2020 four-group scheme (few symptoms, high risk), and he is low risk anyway. Tell: the current scheme has only A, B and E. Without high risk, he cannot be C in either scheme.", "adjacent fact"]],
  CS(37, 40, 41), "test finding", "classify"),

V(GRP, IO_OBS,
  "A 63-year-old woman with confirmed chronic obstructive pulmonary disease has a symptom assessment test score of 18 and a modified Medical Research Council dyspnea grade of 2. She has had no exacerbations in the past year. Under the current three-group scheme, which group is she in?",
  [["Group B",
    "Correct. A symptom score of 18 (10 or more) and a dyspnea grade of 2 (2 or more) mean more symptoms, and no exacerbations means low risk. More symptoms with low risk is group B, which starts on a long-acting beta agonist plus a long-acting antimuscarinic."],
   ["Group A",
    "Group A requires fewer symptoms, a symptom score under 10 and a dyspnea grade of 0 to 1. Her 18 and grade 2 exceed both. Tell: a score of 10 or more moves her out of A.", "wrong stage or severity"],
   ["Group E",
    "Group E needs high exacerbation risk, 2 or more moderate exacerbations or a hospitalization. She had none. Tell: symptoms alone, however heavy, cannot make a patient E.", "wrong stage or severity"],
   ["Group D",
    "Group D belongs to the 2020 scheme and needs both more symptoms and high risk. Tell: with low risk she is B in either scheme. Her low risk keeps her out of D.", "adjacent fact"]],
  CS(37, 40, 41), "test finding", "classify"),

V(GRP, IO_OBS,
  "A 70-year-old man with confirmed chronic obstructive pulmonary disease has a symptom assessment test score of 6 and a modified Medical Research Council dyspnea grade of 1. He had 2 moderate exacerbations treated at home in the past year. Under the current three-group scheme, which group is he in?",
  [["Group E",
    "Correct. Two moderate exacerbations in the past year make him high risk, and any high-risk patient is group E regardless of symptoms. His low symptom score of 6 does not change that; group E starts on a long-acting beta agonist plus a long-acting antimuscarinic."],
   ["Group A",
    "His symptoms (score 6, dyspnea grade 1) would fit group A, but 2 moderate exacerbations make him high risk. Tell: exacerbation risk overrides symptoms in the current scheme.", "wrong stage or severity"],
   ["Group B",
    "Group B is low risk with more symptoms; he has few symptoms and high risk. Tell: 2 moderate exacerbations put him in E. B also requires more symptoms, and his score is 6.", "wrong stage or severity"],
   ["Group C",
    "Few symptoms with high risk would be C in the 2020 four-group scheme. Tell: in the current scheme C and D merged into E, so 2 moderate exacerbations make him E whatever his symptoms.", "adjacent fact"]],
  CS(37, 40, 41), "test finding", "classify"),

V(GRP, IO_OBS,
  "A 66-year-old woman with confirmed chronic obstructive pulmonary disease has a symptom assessment test score of 8 and a modified Medical Research Council dyspnea grade of 1. She was admitted to the hospital once in the past year for an exacerbation. Using the 2020 four-group scheme, which group is she in?",
  [["Group C",
    "Correct. A symptom score of 8 and a dyspnea grade of 1 mean fewer symptoms, and 1 exacerbation leading to hospitalization means high risk. In the 2020 scheme, few symptoms with high risk is group C (in the current scheme she would be E)."],
   ["Group A",
    "Group A is few symptoms with low risk, but her hospitalization makes her high risk. Tell: 1 admission alone moves her to the high-risk row. Her symptom score of 8 alone would fit A, but risk decides the row.", "wrong stage or severity"],
   ["Group B",
    "Group B is more symptoms with low risk; she has few symptoms and high risk. Tell: she sits in the opposite corner of the grid from B. Her symptom score of 8 is under 10 and her dyspnea grade is 1.", "wrong stage or severity"],
   ["Group D",
    "Group D needs more symptoms (score 10 or more, or dyspnea grade 2 or more) as well as high risk. Her score is 8 with grade 1. Tell: few symptoms plus high risk is C.", "wrong stage or severity"]],
  CS(35, 36, 41), "test finding", "classify"),

V(GRP, IO_OBS,
  "A 73-year-old man with confirmed chronic obstructive pulmonary disease has a symptom assessment test score of 24 and a modified Medical Research Council dyspnea grade of 3. He had 3 moderate exacerbations in the past year. Using the 2020 four-group scheme, which group is he in?",
  [["Group D",
    "Correct. A symptom score of 24 and a dyspnea grade of 3 mean more symptoms, and 3 moderate exacerbations mean high risk. In the 2020 scheme, more symptoms with high risk is group D (group E in the current scheme)."],
   ["Group B",
    "Group B has more symptoms but low risk. With 3 exacerbations he is high risk. Tell: high risk moves a symptomatic patient from B to D. B would fit only if he had 0 or 1 exacerbation without admission.", "wrong stage or severity"],
   ["Group C",
    "Group C is high risk with few symptoms; his score of 24 and grade 3 are heavy symptoms. Tell: high risk plus more symptoms is D. Both of his symptom measures are above the line.", "wrong stage or severity"],
   ["Group E",
    "Group E is the current three-group label for any high-risk patient. Tell: the question asks for the 2020 scheme, where he is D. In the 2020 scheme, the high-risk row splits into C and D by symptoms.", "adjacent fact"]],
  CS(35, 36, 41), "test finding", "classify"),

# ---------------------------------------------------------------- prognosis (survival index)
ORD(V(PRG, IO_A,
  "A 68-year-old man with chronic obstructive pulmonary disease has a forced expiratory volume in 1 second of 45% predicted, a 6-minute walk distance of 200 meters, a modified Medical Research Council dyspnea grade of 3, and a body mass index of 20. What is his BODE (body mass index, obstruction, dyspnea, exercise) index score?",
  [["7",
    "Correct. 1-second volume 45% (36 to 49) = 2 + walk 200 meters (150 to 249) = 2 + dyspnea grade 3 = 2 + body mass index 20 (21 or less) = 1, for a total of 7. A score of 7 to 10 predicts about 18% 4-year survival."],
   ["5",
    "Five undercounts by 2, as if the walk distance were scored 0 or the dyspnea grade missed. Tell: 200 meters scores 2 and a dyspnea grade of 3 scores 2.", "reversed direction or value"],
   ["6",
    "Six misses 1 point, most often the body mass index: a value of 21 or less scores 1. Tell: his body mass index of 20 adds the final point to reach 7. A total of 7 predicts about 18% 4-year survival.", "reversed direction or value"],
   ["8",
    "Eight overcounts by 1, as if the 1-second volume of 45% scored 3. Tell: 3 points is for 35% or less; 36% to 49% scores 2. His total stays at 7. Recount: 2 + 2 + 2 + 1.", "reversed direction or value"]],
  C(52), "prognosis", "classify"), [1, 2, 0, 3]),

ORD(V(PRG, IO_A,
  "A 60-year-old woman with chronic obstructive pulmonary disease has a forced expiratory volume in 1 second of 70% predicted, a 6-minute walk distance of 420 meters, a modified Medical Research Council dyspnea grade of 2, and a body mass index of 25. Based on her BODE (body mass index, obstruction, dyspnea, exercise) index, what is her estimated 4-year survival?",
  [["80%",
    "Correct. 1-second volume 70% (65 or more) = 0 + walk 420 meters (350 or more) = 0 + dyspnea grade 2 = 1 + body mass index 25 (over 21) = 0, for a total of 1. Scores of 0 to 2 predict about 80% 4-year survival."],
   ["18%",
    "About 18% belongs to scores of 7 to 10. Her total is only 1. Tell: only the dyspnea grade of 2 earns a point. Her walk distance of 420 meters and 1-second volume of 70% both score 0.", "wrong stage or severity"],
   ["57%",
    "About 57% belongs to scores of 5 to 6. Her total is 1. Tell: a 1-second volume of 70% and a walk of 420 meters each score 0. Her body mass index of 25 scores 0 as well.", "wrong stage or severity"],
   ["67%",
    "About 67% belongs to scores of 3 to 4. Her total is 1, from the dyspnea grade alone. Tell: 0 to 2 points predicts about 80%. She would need 2 more points to reach 3.", "wrong stage or severity"]],
  C(52), "prognosis", "classify"), [1, 2, 3, 0]),

ORD(V(PRG, IO_A,
  "A 65-year-old man with chronic obstructive pulmonary disease has a forced expiratory volume in 1 second of 55% predicted, a 6-minute walk distance of 160 meters, a modified Medical Research Council dyspnea grade of 1, and a body mass index of 27. Based on his BODE (body mass index, obstruction, dyspnea, exercise) index, what is his estimated 4-year survival?",
  [["67%",
    "Correct. 1-second volume 55% (50 to 64) = 1 + walk 160 meters (150 to 249) = 2 + dyspnea grade 1 = 0 + body mass index 27 (over 21) = 0, for a total of 3. Scores of 3 to 4 predict about 67% 4-year survival."],
   ["18%",
    "About 18% belongs to scores of 7 to 10. His total is 3. Tell: his dyspnea grade of 1 and body mass index of 27 score nothing. His total of 3 is far below 7.", "wrong stage or severity"],
   ["57%",
    "About 57% belongs to scores of 5 to 6, which would need 2 more points. Tell: his total is 1 (airflow) + 2 (walk) = 3. A total of 3 sits in the 3-to-4 band.", "wrong stage or severity"],
   ["80%",
    "About 80% needs a total of 0 to 2. His walk of 160 meters alone scores 2 and his 1-second volume adds 1. Tell: 3 points moves him to the 67% band. Walk distance under 250 meters costs him 2 points.", "wrong stage or severity"]],
  C(52), "prognosis", "classify"), [1, 2, 0, 3]),
]
