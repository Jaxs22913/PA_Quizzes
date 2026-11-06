# -*- coding: utf-8 -*-
"""Lecture 43 vignette pool B -- Pulmonary Nodules and Neoplasms (Gray): benign versus concerning nodules
(slides 16-17), screening and nodule follow-up (slides 18-21), and lung cancer staging (slides 22-29).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md: the key names the decisive clue and the slide fact;
each wrong choice says why it fails for THIS patient, the replacing fact, and a "Tell:".

Narration scope (cms_e7l43_scope.py):
  Screening (slide 18, keyed as the slide states it: 55-80 years, at least 30 pack-years, smoking now or quit within
  15 years, annual low-dose chest computed tomography). Every screening patient is eligible or ineligible under BOTH
  that rule and the later 50-80 / 20 pack-year rule: no patient aged 50-54 and no history of 20-29 pack-years.
  Pack-year arithmetic (packs per day x years, slide 3 "PPD and years") is shown in the key explanation.
  Fleischner: exactly two solid-nodule (slide 19) items, both incidental nodules outside screening; the subsolid
  table (slide 20) is never used.
  Benign appearance: slide 16 text and the slide 21 captions; a nodule beside a fissure is keyed as usually benign,
  pleural contact never as reassuring.
  Staging (slides 22-29) is keyed only in clean cells of the stage pictures: 1A, 1B, 2B by hilar node or by a
  5-7 cm tumor invading the chest wall (both on slides 24-25), 3A by same-side mediastinal nodes with a tumor of
  5 cm or less (slide 26 note), 3B by a supraclavicular node with a small tumor (slide 27), 4A by malignant
  effusion, 4B by adrenal plus bone spread (slide 29). Stage labels use Arabic numerals. Treatment by stage 3A/3B is
  never asked (slide 35 text against its own table).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e7l43_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


def ORD(d, asc):
    d["ordered"] = True; d["asc"] = asc; return d


QUESTIONS = [

# ---------------------------------------------------------------- benign versus concerning nodules
V(T_CONCERN, IO_A,
  "A 47-year-old woman who has never smoked has a 1.5-cm nodule on computed tomography done after a fall. It has smooth, well-defined borders, contains fat and shows popcorn calcification (clumped, lobulated calcium deposits). It is unchanged from a scan 3 years ago. Which is the most likely diagnosis?",
  [["Hamartoma",
    "Correct. Benign nodules tend to have well-defined borders and may contain fatty tissue or popcorn-looking calcifications, both pointing to a hamartoma, a connective tissue growth. A smoothly marginated solid nodule with internal fat and calcification is consistent with a hamartoma, and her nodule has not enlarged over 3 years."],
   ["Healed granuloma",
    "A healed granuloma is a smoothly marginated solid nodule with central calcification and no fat. Tell: internal fat with popcorn calcification marks a hamartoma, not a granuloma.", "competing diagnosis"],
   ["Adenocarcinoma",
    "Adenocarcinoma typically appears as a peripheral spiculated nodule, a spiky border being a concerning feature. Tell: her nodule has smooth, well-defined borders, fat and popcorn calcification, and has not grown in 3 years, all benign features.", "competing diagnosis"],
   ["Large cell carcinoma",
    "Large cell carcinoma shows a large, cavitated peripheral mass that forms necrosis and hemorrhage readily. Tell: a small, smooth, fat-containing nodule with popcorn calcification that is stable for years is benign.", "competing diagnosis"]],
  CS(12, 16, 21), "test finding", "diagnosis"),

V(T_CONCERN, IO_A,
  "A 58-year-old man who quit smoking 30 years ago has an 8-mm nodule on computed tomography done for a rib fracture. It is a smoothly marginated solid nodule with dense calcification in its center and no fat. Which is the most likely diagnosis?",
  [["Healed granuloma",
    "Correct. A smoothly marginated solid nodule with central calcification is typical of a healed granuloma, an inflammatory nodule and one of the main examples of benign nodules. Central calcification is a benign pattern, whereas eccentric or stippled ground-glass calcification is a malignant pattern."],
   ["Hamartoma",
    "A hamartoma is a smoothly marginated nodule with internal fat and calcification, classically popcorn-looking. Tell: his nodule has central calcification and no fat, the healed granuloma pattern.", "competing diagnosis"],
   ["Squamous cell carcinoma",
    "Squamous cell carcinoma is a central bronchial tumor, often large and cavitated with a spiky border. Tell: a small, smooth nodule with centrally placed calcification shows a benign pattern rather than malignant features.", "competing diagnosis"],
   ["Linear scar",
    "A linear scar or lymphoid tissue appears as a nodular opacity next to the minor fissure. Tell: his finding is a rounded solid nodule with central calcification, the picture of a healed granuloma.", "competing diagnosis"]],
  CS(12, 16, 21), "test finding", "diagnosis"),

V(T_CONCERN, IO_A,
  "A 63-year-old woman with a 35 pack-year history has a 9-mm solid nodule in the right upper lobe found on computed tomography for abdominal pain. Which additional feature of the nodule would most raise concern for malignancy?",
  [["Spiculated border",
    "Correct. Concerning nodules are greater than 6 mm, sit in the upper lobes or hilar structures, have a spiculated appearance (spikes, deviations or lobulations in the border), number more than 3, enlarge over time, enhance with contrast, appear cavitated or nonsolid, or occur in high-risk patients. A spiky border would add to her size, location and smoking."],
   ["Popcorn calcification",
    "Popcorn-looking calcification points to a hamartoma, a benign connective tissue growth. Tell: it is a benign pattern, so it would lower concern; the concerning border is spiky or lobulated.", "reversed direction or value"],
   ["Internal fat",
    "Fatty tissue inside a nodule points to a hamartoma and is a benign feature. Tell: fat reassures rather than alarms, while a spiculated border is a classic sign of a concerning nodule.", "reversed direction or value"],
   ["Central calcification",
    "Central calcification is a benign pattern, typical of a healed granuloma. Tell: malignant calcification patterns are eccentric or stippled ground-glass, and a spiky border is the feature that raises concern most here.", "reversed direction or value"]],
  CS(16, 21), "test finding", "test"),

V(T_CONCERN, IO_A,
  "A 59-year-old man with active pulmonary sarcoidosis and a 30 pack-year history has a new 16-mm solid nodule. Positron emission tomography shows high uptake in the nodule. He asks whether this result proves he has cancer. Which is the most appropriate next step?",
  [["Tissue biopsy of the nodule",
    "Correct. Positron emission tomography uses a radioactive sugar that highly metabolic cells take up, suggesting malignancy, but high uptake does not rule out inflammatory conditions, which may also take it up. With an active inflammatory lung disease his uptake cannot prove cancer, so tissue is needed; moderate or intense uptake leads to biopsy or resection."],
   ["Start chemotherapy now",
    "Treating before tissue confirms cancer assumes the scan is proof, yet inflammatory conditions may also show high uptake. Tell: uptake raises suspicion and a biopsy decides it; chemotherapy for non-small cell cancer is an adjunct or stage 4 therapy anyway.", "wrong stage or severity"],
   ["Reassure: it is inflammation",
    "Dismissing the uptake as inflammation is as unsafe as calling it cancer: highly metabolic cells take up the sugar, suggesting malignancy. Tell: inflammation is a possible explanation, not a proven one, so the nodule needs a biopsy.", "common lay belief"],
   ["Annual screening scans",
    "Screening is for high-risk people without symptoms or a known nodule. Tell: he already has a nodule with high uptake, so he needs diagnostic tissue sampling rather than yearly screening.", "adjacent fact"]],
  CS(11, 17, 18), "differential", "next step"),

V(T_CONCERN, IO_A,
  "A 61-year-old woman with a 12-mm solid nodule, judged low to moderate probability of malignancy, has positron emission tomography showing mild uptake in the nodule. She asks what this result means for her. Which response is accurate?",
  [["Reassuring; keep surveillance scans",
    "Correct. Low or normal uptake in a nodule is a good sign, because highly metabolic malignant cells take up more of the radioactive sugar. In the nodule pathway, negative or mild uptake leads to computed tomography surveillance at 3 to 6, 9 to 12 and 18 to 24 months rather than biopsy."],
   ["It confirms cancer",
    "Mild uptake points the other way: highly metabolic cells take up the sugar strongly, so low uptake is a good sign. Tell: moderate or intense uptake is the result that pushes toward biopsy or resection.", "reversed direction or value"],
   ["It proves the nodule is benign",
    "Mild uptake is reassuring but not proof, which is why the pathway still tracks the nodule with serial scans out to 18 to 24 months. Tell: a good sign earns surveillance, not discharge.", "common lay belief"],
   ["She needs resection now",
    "Video-assisted thoracoscopic resection follows a high probability without metastases, or moderate or intense uptake. Tell: her uptake was mild, which sends her to computed tomography surveillance instead.", "wrong stage or severity"]],
  CS(11, 17), "test finding", "test"),

V(T_CONCERN, IO_A,
  "A 67-year-old man with a 45 pack-year history has a solid nodule in the left upper lobe that has enlarged from 7 mm to 13 mm over 12 months, and it enhances strongly with contrast on computed tomography. How should this nodule be classified?",
  [["Concerning for malignancy",
    "Correct. Concerning nodules are greater than 6 mm, sit in the upper lobes, enlarge over time, enhance with contrast on computed tomography and occur in patients at high risk. His nodule has every one of these features: 13 mm, upper lobe, growing over a year, contrast-enhancing, in a heavy smoker."],
   ["Benign hamartoma",
    "A hamartoma is suggested by well-defined borders, internal fat or popcorn calcification. Tell: his nodule is growing and contrast-enhancing in the upper lobe, all concerning features rather than benign ones.", "competing diagnosis"],
   ["Healed granuloma",
    "A healed granuloma is a smooth solid nodule with central calcification. Tell: steady growth from 7 to 13 mm and contrast enhancement are signs of concern, not of a healed inflammatory nodule.", "competing diagnosis"],
   ["Too small to matter",
    "The 6-mm threshold is the line for concern, and his nodule has passed it, now measuring 13 mm. Tell: nodules smaller than 6 mm are generally not concerning unless the patient is high risk, and he is both larger and high risk.", "ruled out by a stated finding"]],
  CS(12, 16, 21), "test finding", "classify"),

V(T_CONCERN, IO_A,
  "A 46-year-old woman who has never smoked has a small, flat nodular opacity lying along the minor fissure on computed tomography done after chest trauma. She asks whether it could be cancer. Which response is accurate?",
  [["Likely scar or lymphoid tissue",
    "Correct. A nodule close to a fissure usually indicates something benign, and a nodular opacity adjacent to the minor fissure is typical of a linear scar or lymphoid tissue. She is a never-smoker without other risk factors, which also lowers concern."],
   ["Fissure location signals cancer",
    "This reverses the rule: a nodule close to a fissure usually indicates something benign. Tell: concerning locations are the upper lobes or hilar structures, and an opacity along the minor fissure is typical of a linear scar or lymphoid tissue.", "reversed direction or value"],
   ["It needs removal now",
    "Resection is reserved for nodules with a high probability of malignancy or intense uptake on positron emission tomography. Tell: an opacity hugging the minor fissure in a never-smoker is a typical benign finding.", "wrong stage or severity"],
   ["It is a hamartoma",
    "A hamartoma is a smoothly marginated solid nodule with internal fat and popcorn calcification. Tell: a flat opacity lying along the minor fissure, with no fat or calcification described, is typical of a linear scar or lymphoid tissue.", "competing diagnosis"]],
  CS(16, 21), "test finding", "education"),

# ---------------------------------------------------------------- screening (slide 18)
V(T_SCREEN, IO_POP,
  "A 67-year-old woman smoked 2 packs a day for 20 years and quit 8 years ago. She has no cough, hemoptysis or weight loss, and no lung nodule has ever been found. She asks about lung cancer screening. Which is the most appropriate recommendation?",
  [["Annual low-dose computed tomography",
    "Correct. Screening is recommended for high-risk adults without symptoms or a known nodule who are 55 to 80 years old, with at least a 30 pack-year history, who smoke now or quit within the last 15 years. She is 67, has 2 packs a day x 20 years = 40 pack-years, and quit 8 years ago, so she qualifies for an annual low-dose chest scan."],
   ["No screening, since she quit",
    "Quitting does not disqualify her: people who quit within the last 15 years still qualify. Tell: she quit 8 years ago, at 67 years old with 40 pack-years, so she meets every screening criterion.", "common lay belief"],
   ["Yearly sputum cytology",
    "Sputum cytology is not sensitive and is not the screening test. Tell: eligible patients are screened annually with low-dose chest computed tomography, which works because air and nodules contrast sharply.", "adjacent fact"],
   ["Yearly standard-dose computed tomography",
    "Screening uses a lower radiation dose than a standard chest scan to reduce radiation exposure, which works because lung tissue gives high contrast between air and nodules. Tell: the screening study is the low-dose scan, not a standard-dose one.", "wrong stage or severity"]],
  CS(3, 14, 18), "initial test", "next step"),

V(T_SCREEN, IO_POP,
  "A 72-year-old man smoked 1.5 packs a day for 30 years and quit 22 years ago. He has no symptoms and no known lung nodule, and he asks about lung cancer screening scans. Which describes his eligibility for screening?",
  [["Not eligible: quit too long ago",
    "Correct. Screening covers adults 55 to 80 with at least a 30 pack-year history who smoke now or quit within the last 15 years. He is 72 with 1.5 packs a day x 30 years = 45 pack-years, but he quit 22 years ago, beyond the 15-year window, so he does not qualify."],
   ["Eligible for yearly screening",
    "His age and 45 pack-years fit, but the criteria also require current smoking or quitting within the last 15 years. Tell: he quit 22 years ago, which places him outside the screening window.", "ruled out by a stated finding"],
   ["Eligible on pack-years alone",
    "Pack-years are one criterion; age 55 to 80 and smoking now or within the last 15 years must also be met. Tell: his 45 pack-years pass, but quitting 22 years ago fails the timing rule.", "adjacent fact"],
   ["Not eligible: too old",
    "His age is not the problem: the screening range runs from 55 to 80 years, and he is 72. Tell: the criterion he fails is time since quitting, 22 years against a limit of 15.", "reversed direction or value"]],
  CS(3, 18), "risk factors", "classify"),

V(T_SCREEN, IO_A,
  "A 63-year-old woman who still smokes and has a 50 pack-year history has had 6 weeks of hemoptysis and has lost 4 kg. She saw an advertisement and asks to enroll in a lung cancer screening program. Which plan should be avoided?",
  [["Enrolling her in annual screening",
    "Correct. Screening is for high-risk individuals without symptoms or a known nodule. Hemoptysis and weight loss are symptoms that should be worked up for possible lung cancer now, with computed tomography with contrast of the chest and upper abdomen followed by biopsy, so screening would delay her diagnosis."],
   ["Contrast chest computed tomography",
    "Computed tomography with contrast of the chest and upper abdomen is the standard study for symptoms of possible lung cancer. Tell: she needs exactly this diagnostic scan, so it is not the plan to avoid.", "reversed direction or value"],
   ["Biopsy of any lesion found",
    "Biopsy follows the contrast scan in the standard workup, by bronchoscopy, a transthoracic approach or thoracoscopy depending on location. Tell: tissue diagnosis is a needed step for a symptomatic patient, not one to avoid.", "reversed direction or value"],
   ["Metabolic panel with calcium",
    "A comprehensive metabolic panel including calcium is part of the laboratory workup, beside a complete blood count with differential and alkaline phosphatase. Tell: these laboratory studies support her diagnostic workup and are appropriate.", "reversed direction or value"]],
  CS(12, 14, 18), "avoid", "avoid"),

V(T_SCREEN, IO_POP,
  "A 58-year-old man has smoked 1 pack of cigarettes a day since age 18 and still smokes. He has no cough, hemoptysis or weight loss, and no lung nodule has been found. Which describes his eligibility for lung cancer screening?",
  [["Eligible for yearly screening",
    "Correct. He has smoked 1 pack a day x 40 years (from 18 to 58) = 40 pack-years, above the 30 pack-year minimum; at 58 he is within the 55-to-80 range; he currently smokes; and he has no symptoms or known nodule. He qualifies for annual low-dose chest computed tomography."],
   ["Too young to screen",
    "Screening covers adults from 55 to 80 years old, and he is 58, inside that range. Tell: with 40 pack-years and current smoking, nothing about his age keeps him out of yearly low-dose screening.", "ruled out by a stated finding"],
   ["Too few pack-years",
    "One pack a day for 40 years gives 40 pack-years, above the 30 pack-year minimum. Tell: multiply packs per day by years smoked; undercounting the years from 18 to 58 is the usual slip.", "ruled out by a stated finding"],
   ["Eligible once he quits",
    "Current smokers already qualify: the criteria include people who smoke now or who quit within the last 15 years. Tell: quitting is strongly advised, but it is not a condition for screening.", "reversed direction or value"]],
  CS(3, 18), "risk factors", "classify"),

V(T_SCREEN, IO_POP,
  "An 83-year-old woman who still smokes has a 60 pack-year history. She has no symptoms and no known lung nodule. Her daughter asks whether she should start yearly lung cancer screening scans. Which describes her eligibility?",
  [["Not eligible because of age",
    "Correct. Screening is recommended for adults 55 to 80 with at least a 30 pack-year history who smoke now or quit within the last 15 years. Her 60 pack-years and current smoking would qualify, but at 83 she is beyond the upper age limit of 80."],
   ["Eligible as a current smoker",
    "Current smoking and 60 pack-years meet two criteria, but the age range ends at 80. Tell: at 83 she falls outside the screening window despite her heavy smoking.", "ruled out by a stated finding"],
   ["Not eligible while she smokes",
    "Smoking now does not disqualify anyone: the criteria include current smokers and those who quit within the last 15 years. Tell: her age, 83, is what places her outside the range.", "reversed direction or value"],
   ["Eligible every 5 years",
    "There is no 5-year screening interval: eligible people are screened annually with low-dose chest computed tomography. Tell: she is not eligible at all, because the age range stops at 80.", "adjacent fact"]],
  C(18), "risk factors", "classify"),

V(T_SCREEN, IO_A,
  "A 60-year-old man who quit smoking 5 years ago after a 35 pack-year history is starting annual low-dose computed tomography screening. He asks about the main downside of being screened. Which response is accurate?",
  [["False positives prompting workup",
    "Correct. The upside of screening is early detection leading to rapid intervention and a better prognosis. The downside is a high incidence of false positives that turn out to be benign, so patients receive an unnecessary workup that could have complications, such as a biopsy."],
   ["A high radiation dose each year",
    "Screening uses a lower dose of radiation than a standard chest scan, chosen to reduce radiation exposure. Tell: the documented downside is false-positive findings and the workup they trigger, not a high dose.", "reversed direction or value"],
   ["Cancers are found too late",
    "Early detection is the upside of screening, leading to rapid intervention and an improved prognosis. Tell: the concern runs the other way, toward benign findings that look suspicious.", "reversed direction or value"],
   ["Scans miss most nodules",
    "Low-dose scans work because lung tissue gives high contrast between air and nodules, so nodules show well. Tell: the problem is too many benign findings flagged, not too few nodules seen.", "reversed direction or value"]],
  C(18), "education", "education"),

# ---------------------------------------------------------------- Fleischner solid nodules (slide 19): two items only
V(T_SCREEN, IO_A,
  "A 44-year-old man who has never smoked and has no other lung cancer risk factors has a single, solid 7-mm nodule found incidentally on computed tomography after a car crash. Using the Fleischner Society guidance for incidental solid nodules, which follow-up is recommended?",
  [["Computed tomography at 6-12 months",
    "Correct. For a single solid nodule of 6 to 8 mm in a low-risk patient, the Fleischner Society table gives computed tomography at 6 to 12 months, then considering another scan at 18 to 24 months. He has never smoked and has no other risk factors, so he is low risk."],
   ["No routine follow-up",
    "No routine follow-up applies to solid nodules smaller than 6 mm in low-risk patients. Tell: his nodule measures 7 mm, which moves him into the 6-to-8-mm row with a scan at 6 to 12 months.", "wrong stage or severity"],
   ["Optional computed tomography at 12 months",
    "An optional scan at 12 months is the entry for a nodule smaller than 6 mm in a high-risk patient. Tell: he is low risk with a 7-mm nodule, which calls for a scan at 6 to 12 months.", "adjacent fact"],
   ["Computed tomography at 3 months",
    "Considering a scan at 3 months, positron emission tomography or tissue sampling applies to single nodules larger than 8 mm. Tell: his nodule is 7 mm, so he follows the 6-to-8-mm schedule instead.", "wrong stage or severity"]],
  C(19), "initial test", "next step"),

V(T_SCREEN, IO_A,
  "A 66-year-old woman with a 45 pack-year smoking history, which makes her high risk, has two solid nodules of 6 mm and 7 mm found incidentally on computed tomography done for abdominal pain. Using the Fleischner Society guidance for incidental solid nodules, which follow-up is recommended?",
  [["Computed tomography at 3-6 months",
    "Correct. For multiple solid nodules of 6 to 8 mm in a high-risk patient, the Fleischner Society table gives computed tomography at 3 to 6 months, then again at 18 to 24 months, using the most suspicious nodule to guide management. Her heavy smoking history makes her high risk."],
   ["No routine follow-up",
    "No routine follow-up is the entry for nodules smaller than 6 mm in low-risk patients. Tell: she is high risk and her nodules measure 6 and 7 mm, so she needs a scan at 3 to 6 months.", "wrong stage or severity"],
   ["Optional computed tomography at 12 months",
    "An optional scan at 12 months fits nodules smaller than 6 mm in a high-risk patient. Tell: her nodules are 6 to 8 mm and multiple, which calls for an earlier scan at 3 to 6 months.", "wrong stage or severity"],
   ["Computed tomography at 6-12 months",
    "A scan at 6 to 12 months is the schedule for a single nodule of 6 to 8 mm. Tell: she has two nodules, and multiple nodules of this size in a high-risk patient are rescanned sooner, at 3 to 6 months.", "adjacent fact"]],
  C(19), "initial test", "next step"),

# ---------------------------------------------------------------- staging (slides 22-29)
V(T_STAGE, IO_A,
  "A 66-year-old woman has a biopsy-proven 3.5-cm lung adenocarcinoma. Computed tomography has shown its size and location. Which study in her staging workup looks for lymph node involvement?",
  [["Positron emission tomography",
    "Correct. Lung cancer is staged once computed tomography, positron emission tomography and biopsy results are back: computed tomography identifies location and size, positron emission tomography looks at lymph involvement, and biopsy classes the tumor type. Tumor size, node involvement and distant metastasis then set the stage."],
   ["Repeat biopsy of the primary",
    "Biopsy classes the type of tumor, which hers already has as adenocarcinoma. Tell: lymph node involvement in staging is assessed by positron emission tomography, while computed tomography gives size and location.", "adjacent fact"],
   ["Pulmonary function testing",
    "Pulmonary function tests are part of the additional workup and measure how well the lungs work. Tell: they do not image the lymph nodes; positron emission tomography looks at lymph involvement, and computed tomography gives size and location.", "adjacent fact"],
   ["Chest radiograph",
    "A chest film is not a good tool here; at most it first shows a nodule or rules out other pathology. Tell: node involvement for staging comes from positron emission tomography.", "adjacent fact"]],
  CS(14, 22), "initial test", "test"),

ORD(V(T_STAGE, IO_A,
  "A 69-year-old woman has a biopsy-proven 2.5-cm adenocarcinoma in the right upper lobe. Positron emission tomography and computed tomography show no lymph node involvement and no distant metastasis. Which stage is her cancer?",
  [["Stage 1A",
    "Correct. Staging combines tumor size, lymph node involvement and distant metastasis. A tumor no more than 3 cm in its greatest dimension with no lymph node spread and no metastasis is stage 1A. Her 2.5-cm tumor with clear nodes and no distant spread fits exactly."],
   ["Stage 1B",
    "Stage 1B is a tumor more than 3 cm but no more than 4 cm with no lymph node spread. Tell: her tumor is 2.5 cm, under the 3-cm line, so it stays in stage 1A.", "wrong stage or severity"],
   ["Stage 2A",
    "Stage 2A is a tumor more than 4 cm but no more than 5 cm without node involvement. Tell: at 2.5 cm with no nodes, her tumor is far below the stage 2A size range.", "wrong stage or severity"],
   ["Stage 2B",
    "Stage 2B needs a tumor of more than 5 cm up to 7 cm, or a tumor of 5 cm or less that has spread to peribronchial or hilar nodes. Tell: her nodes are clear and the tumor is 2.5 cm, so neither route applies.", "wrong stage or severity"]],
  CS(22, 23, 24, 25), "test finding", "classify"), [0, 1, 2, 3]),

ORD(V(T_STAGE, IO_A,
  "A 72-year-old man has a biopsy-proven 3.6-cm non-small cell carcinoma in the left lower lobe. Staging shows no lymph node involvement and no distant metastasis. Which stage is his cancer?",
  [["Stage 1B",
    "Correct. A tumor more than 3 cm but no more than 4 cm in its greatest dimension, with no lymph node spread and no metastasis, is stage 1B. His 3.6-cm tumor with clear nodes sits in that band; at this stage the tumor may or may not involve the main bronchus or the lung's inner lining."],
   ["Stage 1A",
    "Stage 1A is a tumor no more than 3 cm in its greatest dimension with no lymph node spread. Tell: his tumor measures 3.6 cm, past the 3-cm limit, which moves it up to stage 1B even though his nodes are clear.", "wrong stage or severity"],
   ["Stage 2A",
    "Stage 2A is a tumor more than 4 cm but no more than 5 cm with no lymph node spread. Tell: his 3.6-cm tumor has not reached 4 cm, so with clear nodes and no metastasis it remains stage 1B.", "wrong stage or severity"],
   ["Stage 3A",
    "Stage 3A needs a tumor larger than 7 cm or one invading structures such as the diaphragm or mediastinum, or spread to mediastinal or subcarinal nodes. Tell: he has a 3.6-cm tumor with clear nodes, none of those.", "wrong stage or severity"]],
  CS(22, 23, 24, 26), "test finding", "classify"), [1, 0, 2, 3]),

ORD(V(T_STAGE, IO_A,
  "A 64-year-old woman has a biopsy-proven 2.8-cm non-small cell carcinoma in the right upper lobe. Positron emission tomography shows uptake in a hilar lymph node on the same side, but no mediastinal or other nodes are involved, and there is no distant metastasis. Which stage is her cancer?",
  [["Stage 2B",
    "Correct. A tumor no more than 5 cm that has spread to the peribronchial, hilar or intrapulmonary nodes is stage 2B. Her 2.8-cm tumor would be stage 1A without nodes, but the involved same-side hilar node, scored N1, moves it to stage 2B; mediastinal nodes would have made it stage 3."],
   ["Stage 1A",
    "Stage 1A is a tumor no more than 3 cm with no lymph node spread. Tell: her tumor size fits stage 1A, but the involved hilar node rules out any stage that requires clear nodes.", "wrong stage or severity"],
   ["Stage 2A",
    "Stage 2A is a tumor more than 4 cm but no more than 5 cm with no lymph node spread. Tell: her tumor is smaller than that and her hilar node is involved, which is the other route into stage 2B.", "wrong stage or severity"],
   ["Stage 3A",
    "Stage 3A with a small tumor needs spread to the mediastinal or subcarinal nodes, because N2 or N3 involvement moves a cancer to stage 3. Tell: her involved node is hilar on the same side, N1, which stops at stage 2B.", "wrong stage or severity"]],
  CS(22, 23, 24, 25, 26), "test finding", "classify"), [1, 2, 0, 3]),

ORD(V(T_STAGE, IO_A,
  "A 67-year-old man has a biopsy-proven 2.5-cm non-small cell carcinoma in the left upper lobe. Positron emission tomography shows uptake in mediastinal and subcarinal lymph nodes on the same side as the tumor, and there is no distant metastasis. Which stage is his cancer?",
  [["Stage 3A",
    "Correct. Mediastinal or subcarinal node involvement (N2) automatically moves a cancer to stage 3, and a tumor no more than 5 cm that has spread to the mediastinal and subcarinal nodes is stage 3A. His tumor is only 2.5 cm, but the same-side mediastinal nodes set the stage."],
   ["Stage 2B",
    "Stage 2B with a small tumor allows spread only to peribronchial, hilar or intrapulmonary nodes. Tell: his nodes are mediastinal and subcarinal, N2, which pushes any cancer into stage 3.", "wrong stage or severity"],
   ["Stage 3B",
    "Stage 3B with a tumor of 5 cm or less needs mediastinal or hilar nodes on the side without the tumor, or supraclavicular or scalene nodes. Tell: his nodes are on the same side as a 2.5-cm tumor, which is stage 3A.", "wrong stage or severity"],
   ["Stage 4A",
    "Stage 4A needs spread to the other lung, the pleura or pericardium, the fluid around the lungs or heart, or one site outside the chest. Tell: he has no distant metastasis, and every stage 1 to 3 cancer is M0.", "wrong stage or severity"]],
  CS(22, 25, 26, 27, 29), "test finding", "classify"), [1, 0, 2, 3]),

ORD(V(T_STAGE, IO_A,
  "A 63-year-old woman has a biopsy-proven 2-cm non-small cell carcinoma in the right upper lobe. On exam a firm right supraclavicular lymph node is palpable, and its biopsy shows the same cancer. Imaging shows no metastasis to other organs. Which stage is her cancer?",
  [["Stage 3B",
    "Correct. Spread to any supraclavicular or scalene node is N3, which moves a cancer to stage 3. With a tumor no more than 5 cm, spread to supraclavicular or scalene nodes, or to mediastinal or hilar nodes on the side without the tumor, is stage 3B. Her 2-cm tumor with a positive supraclavicular node fits."],
   ["Stage 2B",
    "Stage 2B with a small tumor allows spread only to peribronchial, hilar or intrapulmonary nodes on the same side. Tell: a supraclavicular node is N3, and N2 or N3 involvement automatically moves a cancer to stage 3.", "wrong stage or severity"],
   ["Stage 3A",
    "Stage 3A with a small tumor means spread to the same-side mediastinal or subcarinal nodes. Tell: a supraclavicular node reaches farther, N3, which places a tumor of 5 cm or less in stage 3B.", "wrong stage or severity"],
   ["Stage 4A",
    "Stage 4A is spread to the other lung, the pleura or pericardium, the fluid around the lungs or heart, or one site outside the chest. Tell: a supraclavicular node counts as lymph node involvement, not distant metastasis, and no other organ is involved.", "wrong stage or severity"]],
  CS(22, 25, 27, 29), "test finding", "classify"), [1, 2, 0, 3]),

ORD(V(T_STAGE, IO_A,
  "A 70-year-old man has a biopsy-proven 3-cm adenocarcinoma in the left lower lobe and a new left pleural effusion. Analysis of the fluid shows malignant cells. There is no spread outside the chest. Which stage is his cancer?",
  [["Stage 4A",
    "Correct. A malignant pleural effusion is scored M1a, distant metastasis, along with a tumor in the other lung or a pleural or pericardial nodule. Stage 4A covers spread into the other lung, the lung's lining, the heart's lining or the fluid around the lungs or heart, or a single site outside the chest. His malignant effusion makes him stage 4A whatever the tumor size."],
   ["Stage 2B",
    "Stage 2B covers tumors of more than 5 cm up to 7 cm without nodes, or smaller tumors with hilar node spread, all without metastasis. Tell: malignant cells in his pleural fluid are distant metastasis, and every stage 1 to 3 cancer is M0.", "wrong stage or severity"],
   ["Stage 3B",
    "Stage 3B rests on node spread, to supraclavicular or scalene nodes or the far side's mediastinal or hilar nodes, or same-side mediastinal nodes with a larger tumor, and has no metastasis. Tell: a malignant effusion is M1a, which leaves stage 3 behind.", "wrong stage or severity"],
   ["Stage 4B",
    "Stage 4B is spread to multiple sites outside the chest, such as the adrenal gland and bones. Tell: his spread is into the pleural fluid within the chest, with nothing outside it, which is stage 4A.", "wrong stage or severity"]],
  CS(22, 25, 29), "test finding", "classify"), [1, 2, 0, 3]),

ORD(V(T_STAGE, IO_A,
  "A 65-year-old woman with a biopsy-proven 4-cm non-small cell carcinoma has a staging scan showing metastases in the right adrenal gland and in several vertebrae. Which stage is her cancer?",
  [["Stage 4B",
    "Correct. Multiple extrathoracic metastases, in one or more organs, are scored M1c, and spread to multiple sites outside the chest, such as the adrenal gland and bones, is stage 4B. Any tumor size and any node status still give stage 4B once the cancer has reached several sites beyond the chest."],
   ["Stage 3C",
    "Stage 3C is a tumor larger than 5 cm with spread to supraclavicular or scalene nodes or the far side's nodes, but no metastasis. Tell: her adrenal and bone lesions are distant spread, and every stage 1 to 3 cancer is M0.", "wrong stage or severity"],
   ["Stage 4A",
    "Stage 4A allows spread within the chest to the other lung, pleura, pericardium or surrounding fluid, or to just one site outside the chest, such as one adrenal gland. Tell: she has two sites outside the chest, adrenal and bone, which is stage 4B.", "wrong stage or severity"],
   ["Stage 3B",
    "Stage 3B rests on lymph node spread, such as supraclavicular or scalene nodes with a smaller tumor, without metastasis. Tell: adrenal and bone lesions are distant metastases, which place her in stage 4.", "wrong stage or severity"]],
  CS(22, 25, 28, 29), "test finding", "classify"), [3, 1, 2, 0]),

ORD(V(T_STAGE, IO_A,
  "A 66-year-old man has a biopsy-proven 6-cm non-small cell carcinoma that has grown into the adjacent chest wall. Staging shows no lymph node involvement and no distant metastasis. Which stage is his cancer?",
  [["Stage 2B",
    "Correct. A tumor more than 5 cm but no more than 7 cm, or one of any size that has grown into the chest wall, is T3, and a T3 tumor without lymph node spread or metastasis is stage 2B. His 6-cm tumor invading the chest wall, with clear nodes and no metastasis, fits that picture."],
   ["Stage 1B",
    "Stage 1B is a tumor more than 3 cm but no more than 4 cm with no node spread. Tell: his tumor is 6 cm and already into the chest wall, two features that place it beyond stage 1.", "wrong stage or severity"],
   ["Stage 3A",
    "Without nodes, stage 3A needs a tumor larger than 7 cm or invasion of structures such as the diaphragm, mediastinum, heart or great vessels. Tell: chest wall invasion and a 6-cm size are T3 features, which stop at stage 2B when the nodes are clear.", "wrong stage or severity"],
   ["Stage 4A",
    "Stage 4A requires spread to the other lung, the pleura or pericardium, the surrounding fluid or one site outside the chest. Tell: growth into the adjacent chest wall is local invasion by the primary tumor, not metastasis.", "wrong stage or severity"]],
  CS(22, 24, 25, 26, 29), "test finding", "classify"), [1, 0, 2, 3]),
]
