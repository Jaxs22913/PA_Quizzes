# -*- coding: utf-8 -*-
"""Lecture 35 vignette pool A -- Asthma: recognizing the type of asthma or mimic, and classifying severity,
risk and action-plan zone from a patient description.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md (2026-10-29): the key names the stem's decisive
clues; each wrong choice says why it fails THIS patient, the replacing fact, and a tell. Classification items
walk the features against the severity table (most severe category in which any feature falls).

Patients are 12 or older (adult columns only). Classification follows the s62 table for 12 years and older,
never the age-normal ratio column. No emergency management (not testable for CMS I).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e6l35_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


def ORD(d, asc):
    d["ordered"] = True; d["asc"] = asc; return d


TYP = "Types of asthma"
DDX = "Differential diagnosis"
ASP = "Aspergillosis"
SEV = "Severity classification"
EDU = "Education and action plans"

SEVOPTS = ["Intermittent", "Mild persistent", "Moderate persistent", "Severe persistent"]

QUESTIONS = [

# ---------------------------------------------------------------- recognizing the type or mimic
V(TYP, IO_A,
  "A 19-year-old college student has had episodes of wheezing, chest tightness and cough for 2 years, worse at night and after cleaning his dusty dorm room. He has allergic rhinitis and atopic dermatitis (eczema). Between episodes his lung exam is normal. Spirometry shows a reduced forced expiratory volume in 1 second that improves 18% after albuterol. Which diagnosis is most likely?",
  [["Extrinsic asthma",
    "Correct. Episodic wheeze, chest tightness and cough worse at night, a dust trigger, allergic rhinitis and eczema (the atopic triad), a normal exam between episodes, and an 18% rise in the 1-second volume after albuterol (12% or more is a positive response) make allergic, extrinsic asthma the diagnosis."],
   ["Intrinsic asthma",
    "Intrinsic asthma is non-atopic and of later, adult onset, often with nasal polyps and aspirin sensitivity. This 19-year-old has rhinitis, eczema and a dust trigger, an atopic picture. Tell: the atopic triad and an allergen trigger point to extrinsic, not intrinsic, asthma.", "ruled out by a stated finding"],
   ["Chronic obstructive pulmonary disease",
    "Chronic obstructive pulmonary disease is a lower airway mimic, but its obstruction is largely irreversible and it follows years of smoke exposure. This student's obstruction reversed by 18% after albuterol. Tell: a large bronchodilator response in a young atopic patient supports asthma.", "ruled out by a stated finding"],
   ["Vocal fold dysfunction",
    "Vocal fold dysfunction is an upper airway mimic in the differential, but it would not produce reversible lower airway obstruction on spirometry or travel with eczema and rhinitis. Tell: reversible obstruction plus atopy places the problem in the lower airways, not the larynx.", "competing diagnosis"]],
  CS(25, 35, 53), "manifestation", "diagnosis"),

V(TYP, IO_A,
  "A 46-year-old woman has new-onset persistent wheezing and cough that began last year. She has nasal polyps. Allergy skin tests are negative and her serum immunoglobulin E is normal. She had a wheezing episode after taking aspirin for a headache. Which type of asthma is most likely?",
  [["Intrinsic asthma",
    "Correct. Adult onset, persistent symptoms, nasal polyps, negative skin tests with a normal immunoglobulin E, and aspirin sensitivity all fit intrinsic asthma, the non-atopic form seen in about 10% of patients, which is usually more severe and persistent."],
   ["Extrinsic asthma",
    "Extrinsic asthma is allergen-triggered and atopic, so skin tests would be positive and immunoglobulin E raised. Her tests are negative and immunoglobulin E normal. Tell: negative allergy testing rules out the allergic, extrinsic form.", "ruled out by a stated finding"],
   ["Occupational asthma",
    "Occupational asthma follows workplace sensitization and improves on weekends and vacations; nothing in her history points to work. Tell: polyps, aspirin sensitivity and negative allergy tests describe intrinsic asthma, while occupational asthma is defined by its work pattern.", "competing diagnosis"],
   ["Catamenial asthma",
    "Catamenial asthma is timed to predictable points of the menstrual cycle, and her history gives no cyclic pattern. Tell: her clues are polyps, adult onset and an aspirin reaction, the intrinsic profile, not a monthly rhythm.", "competing diagnosis"]],
  CS(34, 35), "manifestation", "diagnosis"),

V(TYP, IO_A,
  "A 34-year-old woman who works in a furniture-finishing plant has had cough and wheezing for 6 months. She notes the symptoms ease on weekends and nearly vanish during a 2-week vacation, then return within days of going back to work. She has no history of allergies. Which diagnosis best explains her pattern?",
  [["Occupational asthma",
    "Correct. Symptoms that improve on weekends and vacations and return at work point to occupational asthma from a workplace sensitizer, here chemicals in furniture finishing. Occupational sensitization is independent of atopy, so her lack of allergies does not argue against it."],
   ["Extrinsic allergic asthma",
    "Extrinsic asthma is atopic and allergen-triggered, and she has no allergy history. Tell: the weekly work-linked rhythm, with improvement away from the plant, is the occupational pattern, and occupational sensitization does not require atopy.", "ruled out by a stated finding"],
   ["Catamenial asthma",
    "Catamenial asthma follows the menstrual cycle, a monthly rhythm. Her symptoms follow her work schedule, easing on weekends and vacations. Tell: a weekly on-off pattern tied to the job points to the workplace, not to hormones.", "competing diagnosis"],
   ["Exercise-induced bronchospasm",
    "Exercise-induced bronchospasm starts during or within 3 minutes after exercise and resolves within an hour. Her symptoms persist through the work week and clear only away from work. Tell: the trigger is a place, not an activity.", "competing diagnosis"]],
  CS(30, 36), "risk factors", "diagnosis"),

V(ASP, IO_ASP,
  "A 29-year-old man with long-standing asthma has had several exacerbations this year despite good inhaler technique and compliance. Testing shows a strong hypersensitivity to Aspergillus fumigatus with markedly raised immunoglobulin E and immunoglobulin G antibodies to the mold. Which diagnosis explains his worsening?",
  [["Allergic bronchopulmonary aspergillosis",
    "Correct. Allergic bronchopulmonary aspergillosis is a hypersensitivity reaction to Aspergillus fumigatus that occurs almost exclusively in asthma or cystic fibrosis; exposure causes a vigorous immunoglobulin E and G response that produces acute asthma symptoms and exacerbations, as in this patient."],
   ["Steroid-resistant asthma",
    "Steroid-resistant asthma is very uncommon, and nothing here shows a failed steroid response. His specific antibody response to Aspergillus explains the exacerbations. Tell: a named mold with raised immunoglobulin E and G points to aspergillosis, not to drug resistance.", "competing diagnosis"],
   ["Occupational asthma",
    "Occupational asthma comes from workplace chemicals and improves away from work. His trigger is an identified mold with a vigorous antibody response. Tell: the stem names Aspergillus and the antibodies, the hallmark of allergic bronchopulmonary aspergillosis.", "competing diagnosis"],
   ["Non-compliance with the controller",
    "Non-compliance is the most common reason for poor control, but the stem states good technique and compliance. Tell: once compliance is confirmed, the antibody response to Aspergillus is the stated explanation for his exacerbations.", "ruled out by a stated finding"]],
  C(65), "complication", "diagnosis"),

V(DDX, IO_A,
  "A 74-year-old man with long-standing heart disease has 3 days of worsening shortness of breath, swelling of both legs, and new wheezing. He has no history of asthma or allergies, and his wheeze began as his heart failure decompensated. Which explanation for his wheezing is most likely?",
  [["Cardiac asthma",
    "Correct. Cardiac asthma is wheezing caused by decompensated heart failure. A 74-year-old with heart disease, leg swelling and wheeze that began with the decompensation, and no asthma or atopy, fits it; the heart failure, not the airway, needs treatment."],
   ["Late-onset intrinsic asthma",
    "Intrinsic asthma does start in adulthood, but it is not tied to heart failure decompensation and usually comes with nasal polyps or aspirin sensitivity. Tell: wheeze appearing with leg swelling as the heart fails points to cardiac asthma.", "competing diagnosis"],
   ["Exercise-induced bronchospasm",
    "Exercise-induced bronchospasm is common in children and adolescents and resolves within an hour of exercise. His wheeze is continuous over 3 days with edema. Tell: an older patient with edema and decompensated heart failure is the cardiac asthma setting.", "competing diagnosis"],
   ["Extrinsic allergic asthma",
    "Extrinsic asthma is atopic and allergen-triggered; he has no allergies or asthma history. Tell: the timing with his heart failure and the leg swelling identify a cardiac cause of wheezing.", "ruled out by a stated finding"]],
  C(36), "differential", "diagnosis"),

V(TYP, IO_POP,
  "A 15-year-old soccer player has cough, chest tightness and wheezing that start within 3 minutes after hard running, peak about 10 to 15 minutes later, and clear within an hour. She has no symptoms at rest or at night. Which diagnosis is most likely?",
  [["Exercise-induced bronchospasm",
    "Correct. Exercise-induced bronchospasm is common in children and adolescents, begins during or within 3 minutes after exercise, peaks in 10 to 15 minutes and resolves by 60 minutes, exactly this player's pattern, with no symptoms at rest or at night."],
   ["Moderate persistent asthma",
    "Moderate persistent asthma brings daily symptoms and night awakenings more than once a week. She has none at rest or at night. Tell: symptoms tied only to exercise and gone within an hour fit exercise-induced bronchospasm.", "ruled out by a stated finding"],
   ["Vocal fold dysfunction",
    "Vocal fold dysfunction is an upper airway mimic, but the pattern of onset within 3 minutes, a 10-to-15-minute peak and resolution by an hour is the exercise-induced bronchospasm timeline. Tell: the precise post-exercise timing is the decisive clue.", "competing diagnosis"],
   ["Catamenial asthma",
    "Catamenial asthma follows the menstrual cycle. Her symptoms follow exercise, appearing within minutes and clearing within the hour. Tell: the trigger is running, not a point in a monthly cycle.", "competing diagnosis"]],
  CS(94, 95), "manifestation", "diagnosis"),

V(TYP, IO_A,
  "A 27-year-old woman with asthma notices that her wheezing and chest tightness flare at the same predictable point in every menstrual cycle and are mild the rest of the month. Which type of asthma describes this pattern?",
  [["Catamenial asthma",
    "Correct. Catamenial asthma is asthma whose symptoms occur at predictable times during the menstrual cycle, as with this woman's monthly flares. It is one of the other types of asthma alongside occupational, cardiac, exercise-induced and aspirin-sensitive patterns."],
   ["Occupational asthma",
    "Occupational asthma follows the work week, improving on weekends and vacations. Her flares follow her menstrual cycle. Tell: a monthly rhythm points to hormones, a weekly rhythm to the workplace.", "competing diagnosis"],
   ["Intrinsic asthma",
    "Intrinsic asthma is defined by negative allergy testing, adult onset and often nasal polyps, not by cyclic timing. Tell: the decisive clue here is the predictable menstrual timing, the definition of catamenial asthma.", "competing diagnosis"],
   ["Aspirin-sensitive asthma",
    "Aspirin-sensitive asthma flares within minutes to 12 hours of taking aspirin, and the stem mentions no drug. Tell: her flares are tied to the menstrual cycle, not to a medication.", "ruled out by a stated finding"]],
  C(36), "manifestation", "diagnosis"),

V(TYP, IO_A,
  "A 39-year-old man with asthma takes ibuprofen for a sprained ankle. Within 20 minutes he develops a runny nose, red irritated eyes, facial flushing and wheezing. Which diagnosis explains the reaction?",
  [["Aspirin-sensitive asthma",
    "Correct. About 1 to 5% of asthmatics worsen with aspirin, and patients with true aspirin sensitivity cross-react with non-selective anti-inflammatory drugs such as ibuprofen. Rhinorrhea, conjunctival irritation, facial flushing and wheezing within minutes of the dose is the described reaction."],
   ["Exercise-induced bronchospasm",
    "Exercise-induced bronchospasm follows exertion, and a sprained ankle is not exercise. Tell: the reaction followed a non-selective anti-inflammatory drug and included flushing, rhinorrhea and eye irritation, the aspirin-sensitive picture.", "ruled out by a stated finding"],
   ["Cardiac asthma",
    "Cardiac asthma is wheezing from decompensated heart failure, and he has no heart failure. Tell: wheeze with flushing, a runny nose and eye irritation minutes after ibuprofen is a drug reaction, not a cardiac cause.", "ruled out by a stated finding"],
   ["Allergic bronchopulmonary aspergillosis",
    "Allergic bronchopulmonary aspergillosis is a hypersensitivity to the Aspergillus mold, not to a drug. Tell: the timing after ibuprofen and the flushing and eye symptoms identify aspirin sensitivity with cross-reactivity to a non-selective agent.", "competing diagnosis"]],
  CS(92, 93), "manifestation", "diagnosis"),

# ---------------------------------------------------------------- classifying severity
ORD(V(SEV, IO_PLAN,
  "A 24-year-old woman has asthma symptoms 2 days a week, wakes at night with cough twice a month, uses albuterol 2 days a week, and has no limitation of activity. Her forced expiratory volume in 1 second is 88% predicted with a normal ratio, and she had no exacerbations requiring oral steroids this year. Which severity classification fits?",
  [["Intermittent",
    "Correct. Symptoms on 2 or fewer days a week, night awakenings 2 or fewer times a month, rescue use on 2 or fewer days a week, no interference, a 1-second volume above 80% with a normal ratio, and 0 to 1 steroid-requiring exacerbations a year all sit in the intermittent column."],
   ["Mild persistent",
    "Mild persistent asthma needs symptoms or rescue use on more than 2 days a week, or 3 to 4 night awakenings a month. She is at exactly 2 days and 2 nights. Tell: the intermittent limits are 2 or fewer, so reaching but not exceeding 2 stays intermittent.", "wrong stage or severity"],
   ["Moderate persistent",
    "Moderate persistent asthma means daily symptoms, daily rescue use and a 1-second volume of 60% to 80%. Her symptoms are 2 days a week and her function is 88%. Tell: nothing in her history is daily.", "wrong stage or severity"],
   ["Severe persistent",
    "Severe persistent asthma brings symptoms throughout the day, near-nightly waking and a 1-second volume under 60%. Every feature she has is at the mildest level. Tell: no feature reaches even the mild persistent column.", "wrong stage or severity"]],
  C(62), "test finding", "classify"), [0, 1, 2, 3]),

ORD(V(SEV, IO_PLAN,
  "A 31-year-old man reports asthma symptoms 4 days a week but not every day, wakes at night 3 times a month, uses albuterol 4 days a week but not daily, and notes minor limitation when hiking. His forced expiratory volume in 1 second is 84% predicted with a normal ratio. Which severity classification fits?",
  [["Mild persistent",
    "Correct. Symptoms and rescue use on more than 2 days a week but not daily, 3 to 4 night awakenings a month, minor limitation, and a 1-second volume above 80% with a normal ratio all fall in the mild persistent column."],
   ["Intermittent",
    "Intermittent asthma allows symptoms and rescue use on only 2 or fewer days a week and night waking 2 or fewer times a month. He has 4 days and 3 nights. Tell: crossing either 2-a-week line moves him into persistent asthma.", "wrong stage or severity"],
   ["Moderate persistent",
    "Moderate persistent asthma requires daily symptoms and daily rescue use, night waking more than once a week, and a 1-second volume of 60% to 80%. His symptoms are not daily and his function is 84%. Tell: not daily keeps him below moderate.", "wrong stage or severity"],
   ["Severe persistent",
    "Severe persistent asthma brings symptoms throughout the day, rescue use several times a day and a 1-second volume below 60%. His features are all mild persistent. Tell: minor limitation and 84% function are far from extremely limited and under 60%.", "wrong stage or severity"]],
  C(62), "test finding", "classify"), [1, 0, 2, 3]),

ORD(V(SEV, IO_PLAN,
  "A 42-year-old woman has asthma symptoms every day, uses her albuterol inhaler daily, wakes at night with symptoms twice a week, and has had to cut back some activities. Her forced expiratory volume in 1 second is 68% predicted with a reduced ratio. Which severity classification fits?",
  [["Moderate persistent",
    "Correct. Daily symptoms, daily short-acting beta-2 agonist use, night awakenings more than once a week but not nightly, some limitation of activity, and a 1-second volume between 60% and 80% predicted with a reduced ratio all fall in the moderate persistent column."],
   ["Mild persistent",
    "Mild persistent asthma has symptoms on more than 2 days a week but not daily, 3 to 4 night awakenings a month, and a 1-second volume above 80%. She has daily symptoms and 68% function. Tell: daily symptoms move her past mild.", "wrong stage or severity"],
   ["Intermittent",
    "Intermittent asthma allows symptoms on 2 or fewer days a week and normal function between exacerbations. She is symptomatic daily with 68% function. Tell: every one of her features is above the intermittent limits.", "wrong stage or severity"],
   ["Severe persistent",
    "Severe persistent asthma has symptoms throughout the day, waking often 7 times a week, rescue use several times a day, extreme limitation and a 1-second volume below 60%. She wakes twice a week with 68% function. Tell: 68% sits in the 60% to 80% moderate band.", "wrong stage or severity"]],
  C(62), "test finding", "classify"), [2, 1, 0, 3]),

ORD(V(SEV, IO_PLAN,
  "A 55-year-old man has asthma symptoms throughout every day, uses his rescue inhaler several times a day, wakes with symptoms nearly every night, and is extremely limited in daily activities. His forced expiratory volume in 1 second is 52% predicted. Which severity classification fits?",
  [["Severe persistent",
    "Correct. Symptoms throughout the day, rescue use several times a day, night awakenings often 7 times a week, extreme limitation and a 1-second volume below 60% predicted define severe persistent asthma."],
   ["Moderate persistent",
    "Moderate persistent asthma has daily but not continuous symptoms, waking more than once a week but not nightly, some limitation, and a 1-second volume of 60% to 80%. His 52% and nightly waking exceed that. Tell: under 60% is severe.", "wrong stage or severity"],
   ["Mild persistent",
    "Mild persistent asthma means symptoms on more than 2 days a week but not daily, with a 1-second volume above 80%. Every feature he has is far worse. Tell: extreme limitation and 52% function are severe-column findings.", "wrong stage or severity"],
   ["Intermittent",
    "Intermittent asthma allows symptoms on 2 or fewer days a week and normal function between exacerbations. He is symptomatic all day with 52% function. Tell: no feature here is near the intermittent column.", "wrong stage or severity"]],
  C(62), "test finding", "classify"), [3, 2, 1, 0]),

ORD(V(SEV, IO_PLAN,
  "A 26-year-old woman has asthma symptoms only 1 day a week and uses albuterol 1 day a week, but she wakes at night with cough twice a week. She has no activity limitation, and her forced expiratory volume in 1 second is 86% predicted. Which severity classification fits?",
  [["Moderate persistent",
    "Correct. Severity is assigned to the most severe category in which any feature occurs. Her daytime symptoms and lung function are intermittent-level, but night awakenings more than once a week (twice weekly) are a moderate persistent feature, so she is moderate persistent."],
   ["Intermittent",
    "Her daytime symptoms, rescue use and 86% function would fit intermittent, but severity follows the worst feature, and waking twice a week exceeds the intermittent limit of 2 or fewer times a month. Tell: one moderate feature outranks several mild ones.", "wrong stage or severity"],
   ["Mild persistent",
    "Mild persistent asthma allows night waking 3 to 4 times a month. She wakes twice a week, which is more than once a week, the moderate persistent level. Tell: twice weekly is roughly 8 times a month, past the mild limit.", "wrong stage or severity"],
   ["Severe persistent",
    "Severe persistent asthma brings waking often 7 times a week with symptoms throughout the day and function under 60%. She wakes twice a week with 86% function. Tell: her worst feature reaches moderate, not severe.", "wrong stage or severity"]],
  C(62), "test finding", "classify"), [1, 2, 0, 3]),

ORD(V(SEV, IO_PLAN,
  "A 33-year-old man with asthma has symptoms 1 day a week, wakes at night once a month, uses albuterol 1 day a week, and has a forced expiratory volume in 1 second of 91% predicted. In the past year, however, he needed 3 separate courses of oral corticosteroids for exacerbations. How should his asthma be classified?",
  [["As persistent asthma",
    "Correct. His impairment is intermittent-level, but patients with 2 or more exacerbations requiring oral systemic corticosteroids in the past year may be considered the same as patients with persistent asthma, even without persistent-level impairment. Three steroid courses put him in the persistent risk row."],
   ["As intermittent asthma",
    "His day-to-day impairment alone fits intermittent asthma, but the risk domain counts too, and intermittent allows only 0 to 1 steroid-requiring exacerbation a year. He had 3. Tell: the risk domain can move a quiet patient into persistent asthma.", "wrong stage or severity"],
   ["As well-controlled with no change",
    "Three steroid-requiring exacerbations in a year are not well controlled; the risk domain treats 2 or more as persistent asthma. Tell: a good week-to-week picture does not cancel repeated exacerbations.", "common lay belief"],
   ["As exercise-induced bronchospasm",
    "Nothing ties his symptoms to exercise, and exercise-induced bronchospasm does not explain repeated steroid-requiring exacerbations. Tell: the decisive fact is the count of oral steroid courses, 3 in a year, which defines persistent risk.", "competing diagnosis"]],
  C(62), "test finding", "classify"), [1, 0, 2, 3]),

ORD(V(SEV, IO_PLAN,
  "A 47-year-old woman has asthma symptoms 3 days a week, wakes at night 3 times a month, and uses albuterol 3 days a week but not daily. She has minor limitation of activity. Her forced expiratory volume in 1 second is 72% predicted with a ratio reduced by 4%. Which severity classification fits?",
  [["Moderate persistent",
    "Correct. Her symptoms, night waking, rescue use and minor limitation fit mild persistent, but a 1-second volume between 60% and 80% predicted (72%) is a moderate persistent feature, and severity follows the most severe category in which any feature occurs."],
   ["Mild persistent",
    "Most of her features are mild persistent, but mild persistent requires a 1-second volume above 80%; hers is 72%. Severity follows the worst feature. Tell: lung function between 60% and 80% sets her one class higher.", "wrong stage or severity"],
   ["Intermittent",
    "Intermittent asthma allows symptoms on 2 or fewer days a week and a 1-second volume above 80%. She has 3 days a week and 72% function. Tell: both her symptoms and her spirometry exceed the intermittent column.", "wrong stage or severity"],
   ["Severe persistent",
    "Severe persistent asthma needs a 1-second volume below 60% or features such as symptoms throughout the day. Her worst feature, 72%, sits in the moderate band. Tell: 72% is above the 60% line that marks severe disease.", "wrong stage or severity"]],
  C(62), "test finding", "classify"), [1, 0, 2, 3]),

ORD(V(SEV, IO_PLAN,
  "A 20-year-old man has daily asthma symptoms and uses albuterol daily, but he wakes at night only once a month and has a forced expiratory volume in 1 second of 85% predicted. He has some limitation playing pickup basketball. Which severity classification fits?",
  [["Moderate persistent",
    "Correct. Daily symptoms, daily short-acting beta-2 agonist use and some limitation of activity are moderate persistent features. Even though his night waking and 85% function are milder, severity is assigned to the most severe category in which any feature occurs."],
   ["Mild persistent",
    "Mild persistent asthma allows symptoms and rescue use on more than 2 days a week but not daily. His are daily. Tell: the word daily is the line between mild and moderate persistent asthma.", "wrong stage or severity"],
   ["Intermittent",
    "His night waking and lung function look intermittent, but daily symptoms and daily rescue use far exceed the intermittent limit of 2 or fewer days a week. Tell: severity follows the worst feature, not the best ones.", "wrong stage or severity"],
   ["Severe persistent",
    "Severe persistent asthma requires symptoms throughout the day, rescue use several times a day, extreme limitation or function below 60%. He uses albuterol daily with some limitation and 85% function. Tell: daily rescue use is moderate; several times a day is severe.", "wrong stage or severity"]],
  C(62), "test finding", "classify"), [1, 0, 2, 3]),

# ---------------------------------------------------------------- action plan zones
V(EDU, IO_EDU,
  "A 23-year-old woman with asthma has a personal best peak flow of 450 L/min. This morning she has cough and chest tightness, and her peak flow is 300 L/min (67% of her best). According to her written asthma action plan, which zone is she in?",
  [["Yellow zone",
    "Correct. Her reading of 300 of a best 450 is 67%, inside the yellow zone of 50% to 79% of personal best, where asthma is getting worse. The plan adds quick-relief medicine (a short-acting beta-2 agonist) while she keeps taking her green-zone controller."],
   ["Green zone",
    "The green zone, doing well, requires 80% or more of personal best, which for her is 360 or higher. At 300 she is below it and symptomatic. Tell: cough and chest tightness alone rule out the doing-well zone.", "wrong stage or severity"],
   ["Red zone",
    "The red zone is below 50% of personal best, under 225 for her, with symptoms such as being very short of breath. At 300 (67%) she is above it. Tell: the red line is half of personal best.", "wrong stage or severity"],
   ["Not classifiable without spirometry",
    "Action plans are built on peak flow against personal best, not office spirometry, so her zone can be set now: 67% is yellow. Tell: home peak flow monitoring exists precisely so patients can act on their own readings.", "adjacent fact"]],
  CS(88, 89), "education", "classify"),

V(EDU, IO_EDU,
  "A 30-year-old man with asthma follows a written action plan. His personal best peak flow is 600 L/min. Today he is very short of breath, his quick-relief medicine has not helped, and his peak flow is 260 L/min. Which action-plan zone is he in?",
  [["Red zone",
    "Correct. A peak flow of 260 out of a personal best of 600 is about 43%, below 50% of personal best, and he is very short of breath despite quick-relief medicine. Those are red-zone, medical-alert findings: take the rescue medicine and call the doctor or get help now."],
   ["Yellow zone",
    "The yellow zone is 50% to 79% of personal best, 300 to 474 for him. At 260 he is below it, and quick-relief medicine has failed. Tell: failure of the quick-relief medicine is itself a red-zone criterion.", "wrong stage or severity"],
   ["Green zone",
    "Green requires 80% or more of personal best (480 or higher) and no symptoms. He is far below that and very short of breath. Tell: he has none of the doing-well features.", "wrong stage or severity"],
   ["Between zones, so recheck tomorrow",
    "Waiting is unsafe: under 50% of personal best with failed quick-relief medicine is the red, medical-alert zone, which calls for action now. Tell: action plans are built so that a red reading leads to immediate action, not a delay.", "wrong stage or severity"]],
  CS(88, 89), "education", "classify"),

V(SEV, IO_PLAN,
  "A 37-year-old woman with asthma records her peak flow at home. Over the past week her morning readings before albuterol have been about 280 L/min and her afternoon readings after albuterol about 380 L/min. What does this pattern indicate?",
  [["Poor asthma control",
    "Correct. Peak flow is measured in the morning before and the afternoon after the bronchodilator, and a 20% change between them, or day to day, indicates poor control. A rise from 280 to 380 is about 36% of the afternoon value, well over the 20% line."],
   ["Good asthma control",
    "Good control would keep morning-to-afternoon variation under 20%. Her readings swing by about 36%. Tell: a large morning-to-afternoon gap is the hallmark of poor control, not good control.", "reversed direction or value"],
   ["A faulty peak flow meter",
    "A consistent pattern every morning and afternoon for a week, with higher readings after albuterol, fits real airway variation, not a broken device. Tell: the readings rise exactly when the bronchodilator works.", "common lay belief"],
   ["Normal circadian variation needing no action",
    "Bronchial reactivity does vary through the day, but a swing of more than 20% between morning and afternoon is defined as poor control and needs review. Tell: the 20% threshold separates expected variation from poor control.", "wrong stage or severity"]],
  C(60), "test finding", "classify"),
]
