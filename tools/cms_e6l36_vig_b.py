# -*- coding: utf-8 -*-
"""Lecture 36 vignette pool B -- Chronic obstructive pulmonary disease: starting and adjusting treatment by
group, comorbidities and age that change the drug or device, smoking cessation and vaccines, rehabilitation,
referral and oxygen.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md (2026-10-29). Contraindication items say why the
key is safe for this patient when the obvious choice is not.

Generic drug names only; no doses; no vaccine product names. Oxygen saturations are kept clearly away from
the 88% boundary (s63 and s64 disagree on "<" versus "<="); no saturation target is keyed.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e6l36_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


TRT = "Treatment by group"
SAF = "Drug safety and devices"
CES = "Smoking cessation and vaccines"
REH = "Rehabilitation and referral"
OXY = "Oxygen"

QUESTIONS = [

# ---------------------------------------------------------------- treatment by group
V(TRT, IO_A,
  "A 56-year-old man with newly confirmed chronic obstructive pulmonary disease has a symptom assessment test score of 6, a modified Medical Research Council dyspnea grade of 1, and no exacerbations in the past year. Which initial medication is most appropriate?",
  [["A single bronchodilator",
    "Correct. A score of 6 and a dyspnea grade of 1 mean few symptoms, and no exacerbations means low risk, so he is group A, which starts with 1 bronchodilator, short- or long-acting. He still needs smoking cessation if he smokes, and physical activity."],
   ["Dual long-acting bronchodilators",
    "A long-acting beta agonist plus a long-acting antimuscarinic is the start for group B or E. His few symptoms and no exacerbations make him group A. Tell: the combination is for more symptoms or high risk.", "wrong stage or severity"],
   ["An inhaled corticosteroid alone",
    "Inhaled corticosteroids cannot be used alone in this disease; they must be combined with a long-acting beta agonist and they raise pneumonia risk. Tell: group A starts with a single bronchodilator.", "confused mechanism or drug class"],
   ["Daily oral corticosteroids",
    "Oral corticosteroids are for acute exacerbations only in this disease, and he has had none. Tell: a low-symptom, low-risk patient starts on 1 bronchodilator, not systemic steroids.", "confused mechanism or drug class"]],
  CS(37, 40, 49), "first-line", "treatment"),

V(TRT, IO_A,
  "A 64-year-old woman with chronic obstructive pulmonary disease has a symptom assessment test score of 17 and a modified Medical Research Council dyspnea grade of 2. She has had no exacerbations in the past year. Which initial maintenance regimen is most appropriate?",
  [["Long-acting beta agonist plus antimuscarinic",
    "Correct. A score of 17 and a dyspnea grade of 2 mean more symptoms, and no exacerbations means low risk, which is group B. Group B starts on a long-acting beta agonist plus a long-acting antimuscarinic, ideally in a single inhaler for convenience."],
   ["A single short-acting bronchodilator",
    "One bronchodilator is the start for group A, with fewer symptoms. Her score of 17 and dyspnea grade of 2 put her in group B. Tell: more symptoms call for both long-acting bronchodilators.", "wrong stage or severity"],
   ["Inhaled corticosteroid plus beta agonist",
    "An inhaled corticosteroid adds pneumonia risk and is considered in group E with eosinophils of 300 or more. She is group B, low risk. Tell: group B's start is the 2 long-acting bronchodilators, without a steroid.", "wrong stage or severity"],
   ["Long-term azithromycin",
    "Long-term azithromycin is used rarely and increases resistance and side effects. Tell: a symptomatic, low-risk patient starts on dual long-acting bronchodilators.", "adjacent fact"]],
  CS(37, 40), "first-line", "treatment"),

V(TRT, IO_A,
  "A 69-year-old man with chronic obstructive pulmonary disease had 2 moderate exacerbations and 1 hospital admission in the past year. His blood eosinophil count is 350. He is starting maintenance therapy. Which regimen is most appropriate?",
  [["Triple inhaled therapy",
    "Correct. Two moderate exacerbations and an admission make him high risk, group E. Group E starts on a long-acting beta agonist plus a long-acting antimuscarinic, and adding an inhaled corticosteroid is considered when blood eosinophils are 300 or more, as his 350 are."],
   ["A single bronchodilator",
    "A single bronchodilator is the group A start, for few symptoms and low risk. His exacerbations and admission make him group E. Tell: high risk calls for both long-acting bronchodilators, plus a steroid with eosinophils of 300 or more.", "wrong stage or severity"],
   ["An inhaled corticosteroid alone",
    "An inhaled corticosteroid is never used alone in this disease; it must be combined with a long-acting beta agonist. Tell: his eosinophils justify adding it to dual bronchodilators, not using it by itself.", "confused mechanism or drug class"],
   ["Daily oral corticosteroids",
    "Oral corticosteroids are for acute exacerbations only, not maintenance. Tell: frequent exacerbations are prevented with inhaled long-acting therapy, here triple therapy because of his eosinophils.", "confused mechanism or drug class"]],
  CS(37, 42), "escalation", "treatment"),

V(TRT, IO_A,
  "A 66-year-old woman with chronic obstructive pulmonary disease had 3 moderate exacerbations in the past year. Her blood eosinophil count is 110. She is starting maintenance therapy. Which regimen is most appropriate?",
  [["Dual long-acting bronchodilators",
    "Correct. Three moderate exacerbations make her high risk, group E, which starts on a long-acting beta agonist plus a long-acting antimuscarinic. Her eosinophil count of 110 is below 300, so an inhaled corticosteroid, with its pneumonia risk, is not added."],
   ["Triple inhaled therapy",
    "Adding an inhaled corticosteroid is considered in group E when eosinophils are 300 or more. Hers are 110. Tell: without that eosinophil count, the steroid's pneumonia risk is not justified.", "wrong stage or severity"],
   ["A single bronchodilator",
    "A single bronchodilator is the group A start, for low risk and few symptoms. Three exacerbations make her group E. Tell: high risk calls for both long-acting bronchodilators.", "wrong stage or severity"],
   ["Daily oral corticosteroids",
    "Oral corticosteroids are for acute exacerbations only in this disease, not daily maintenance. Tell: exacerbation prevention comes from long-acting inhaled bronchodilators.", "confused mechanism or drug class"]],
  C(37), "escalation", "treatment"),

V(TRT, IO_A,
  "A 71-year-old man with chronic obstructive pulmonary disease was started on daily oral prednisone by another clinic 6 months ago as maintenance therapy. He has had no recent exacerbation. Which part of his regimen should be stopped or avoided?",
  [["Maintenance oral corticosteroids",
    "Correct. Oral corticosteroids are for acute exacerbations only in this disease, which is why they are missing from the list of common chronic therapies. Maintenance is built from albuterol as needed and long-acting inhaled bronchodilators, with an inhaled corticosteroid only when indicated."],
   ["An albuterol rescue inhaler",
    "Every patient should have an albuterol inhaler to prevent or reduce symptoms, as needed. Tell: the rescue inhaler stays; daily oral steroids, meant for exacerbations, are what does not belong.", "reversed direction or value"],
   ["A long-acting antimuscarinic",
    "Long-acting antimuscarinics such as tiotropium limit bronchoconstriction, help prevent exacerbations, and are poorly absorbed with mainly dry mouth. Tell: they are standard maintenance; the oral steroid is not.", "reversed direction or value"],
   ["A yearly influenza vaccine",
    "The yearly influenza vaccine is proven to reduce hospitalizations and death and is given to every patient. Tell: it stays in his plan; the drug to stop is the maintenance oral steroid.", "reversed direction or value"]],
  C(49), "avoid", "avoid"),

# ---------------------------------------------------------------- drug safety and devices
V(SAF, IO_POP,
  "A 74-year-old man with chronic obstructive pulmonary disease and paroxysmal atrial fibrillation takes a long-acting beta agonist, a long-acting antimuscarinic and an inhaled corticosteroid; he rarely uses albuterol. His atrial fibrillation episodes and palpitations have become more frequent since his regimen was started. Which component is most likely contributing?",
  [["The long-acting beta agonist",
    "Correct. Long-acting beta agonists produce sympathetic stimulation that can cause tachycardia and arrhythmias and can make atrial fibrillation worse; their cardiac effects are a listed concern in older adults. With rare albuterol use, the daily beta agonist is the likely driver."],
   ["The long-acting antimuscarinic",
    "Long-acting antimuscarinics are poorly absorbed, and their adverse effects are limited mainly to dry mouth. Tell: worsening atrial fibrillation fits the sympathetic stimulation of the beta agonist.", "confused mechanism or drug class"],
   ["The inhaled corticosteroid",
    "The inhaled corticosteroid's listed risks in older adults are pneumonia and fractures, not arrhythmias. Tell: palpitations and more atrial fibrillation point to the beta agonist.", "confused mechanism or drug class"],
   ["His occasional albuterol",
    "Excessive albuterol carries cardiac risk, but he rarely uses it. Tell: the daily long-acting beta agonist delivers continuous sympathetic stimulation, the likelier cause.", "ruled out by a stated finding"]],
  CS(38, 53), "complication", "complication"),

V(SAF, IO_POP,
  "A 77-year-old woman with chronic obstructive pulmonary disease and osteoporosis takes triple inhaled therapy. She has had 2 pneumonias this year and a wrist fracture after a fall. Which component of her regimen is linked to both pneumonia and fracture risk?",
  [["The inhaled corticosteroid",
    "Correct. Inhaled corticosteroids increase the risk of pneumonia, and in older adults the concerns include inhaled corticosteroid-related pneumonia and fracture risk. Her repeated pneumonias and fracture make that component the one to reassess."],
   ["The long-acting beta agonist",
    "Long-acting beta agonists carry cardiac risk, such as tachycardia, arrhythmias and worsening atrial fibrillation, not pneumonia or fractures. Tell: pneumonia and fracture together point to the steroid component.", "confused mechanism or drug class"],
   ["The long-acting antimuscarinic",
    "Long-acting antimuscarinics are poorly absorbed, with mainly dry mouth. Tell: in older adults the drug tied to pneumonia and fractures is the inhaled corticosteroid.", "confused mechanism or drug class"],
   ["Her as-needed albuterol",
    "Excessive albuterol risks cardiac and psychiatric side effects, not pneumonia or fractures. Tell: her 2 pneumonias and fracture fit the inhaled corticosteroid's risks.", "confused mechanism or drug class"]],
  CS(42, 53), "complication", "complication"),

V(SAF, IO_A,
  "A 60-year-old man with chronic obstructive pulmonary disease and few symptoms asks to be started on an inhaled corticosteroid by itself because a friend with asthma uses one. Which regimen should be avoided in him?",
  [["An inhaled corticosteroid alone",
    "Correct. In this disease, inhaled corticosteroids must be combined with a long-acting beta agonist, and then with a long-acting antimuscarinic as triple therapy, and cannot be used on their own. They also raise pneumonia risk. Alone, they are an asthma treatment."],
   ["A single short-acting bronchodilator",
    "A single bronchodilator is the appropriate start for group A, few symptoms and low risk. Tell: it suits him; the regimen to avoid is a steroid inhaler used by itself.", "reversed direction or value"],
   ["Smoking cessation with counseling",
    "Smoking cessation is essential for every group and is the only treatment that slows progression. Tell: it belongs in his plan; the steroid alone does not.", "reversed direction or value"],
   ["A yearly influenza vaccine",
    "Every patient should get the yearly influenza vaccine, which reduces hospitalizations and death. Tell: vaccination fits him; an inhaled corticosteroid alone is the regimen to avoid.", "reversed direction or value"]],
  C(42), "avoid", "avoid"),

V(SAF, IO_POP,
  "An 81-year-old woman with chronic obstructive pulmonary disease has severe hand arthritis, a tremor and mild cognitive impairment. Testing shows a low peak inspiratory flow. Which inhaler device should be avoided?",
  [["A dry powder inhaler",
    "Correct. In older adults, arthritis, tremor, cognitive impairment and low peak inspiratory flow limit dry powder inhalers, which need a strong, fast breath and dexterity. A pressurized metered-dose inhaler with a spacer, a soft mist inhaler or a nebulizer is considered instead."],
   ["A nebulizer",
    "A nebulizer is one of the listed alternatives for older adults whose arthritis, tremor or cognition limit other devices. Tell: it needs no forceful inhalation, so it suits her low inspiratory flow.", "reversed direction or value"],
   ["A soft mist inhaler",
    "A soft mist inhaler is listed as an alternative when a dry powder inhaler is limited by arthritis, tremor, cognitive impairment or low inspiratory flow. Tell: it suits her; the dry powder device does not.", "reversed direction or value"],
   ["A metered-dose inhaler with a spacer",
    "A pressurized metered-dose inhaler with a spacer is a listed alternative for older adults who cannot manage a dry powder inhaler. Tell: the spacer eases coordination; the device to avoid is the dry powder inhaler.", "reversed direction or value"]],
  C(53), "avoid", "avoid"),

V(SAF, IO_POP,
  "A 79-year-old man with chronic obstructive pulmonary disease cannot generate a strong inhalation, and his rheumatoid arthritis makes it hard to load and handle his current dry powder inhaler. Which device is most appropriate for him?",
  [["Metered-dose inhaler with a spacer",
    "Correct. Arthritis and low peak inspiratory flow limit dry powder inhalers in older adults, so a pressurized metered-dose inhaler with a spacer, a soft mist inhaler or a nebulizer is considered. The spacer reduces the need for a forceful, well-timed breath."],
   ["A different dry powder inhaler",
    "Every dry powder inhaler depends on a strong inspiratory flow and hand dexterity, the 2 things he lacks. Tell: switching brands within the same device type does not solve the problem.", "ruled out by a stated finding"],
   ["Daily oral corticosteroids",
    "Oral corticosteroids are for acute exacerbations only in this disease and are not a substitute for inhaled maintenance. Tell: the fix is a device he can use, such as a metered-dose inhaler with a spacer.", "confused mechanism or drug class"],
   ["Stopping inhaled therapy",
    "Stopping maintenance would remove the drugs that prevent exacerbations. Tell: a device problem is solved by changing the device, not by stopping treatment.", "common lay belief"]],
  C(53), "agent/regimen", "treatment"),

# ---------------------------------------------------------------- smoking cessation and vaccines
V(CES, IO_A,
  "A 55-year-old woman with group B chronic obstructive pulmonary disease still smokes a pack a day. She asks what single step would do the most to slow her disease. Which intervention is most appropriate?",
  [["Smoking cessation with counseling",
    "Correct. Smoking cessation is the only treatment that can slow progression, and every attempt should be combined with counseling to increase efficacy; nicotine replacement, bupropion or varenicline can be added. It is essential for every group."],
   ["Adding an inhaled corticosteroid",
    "An inhaled corticosteroid adds pneumonia risk and is considered only in group E with eosinophils of 300 or more. Tell: no inhaler slows progression; stopping smoking does.", "confused mechanism or drug class"],
   ["Long-term azithromycin",
    "Long-term azithromycin is used rarely and increases resistance and side effects; it does not slow progression. Tell: the one intervention that slows the disease is smoking cessation.", "adjacent fact"],
   ["A chest computed tomography scan",
    "Chest computed tomography can categorize emphysema but is generally not needed, and imaging changes nothing about progression. Tell: her most powerful step is quitting smoking with counseling.", "adjacent fact"]],
  CS(9, 43, 46), "first-line", "treatment"),

V(CES, IO_A,
  "A 62-year-old man with chronic obstructive pulmonary disease who smokes is asked about his smoking and is clearly advised to quit, with a link to his diabetes and heart risk. Using the Five A's approach, which step should come next?",
  [["Assess his readiness to change",
    "Correct. After Ask and Advise, the Five A's continue with Assess, evaluating the person's readiness and willingness to change, then Assist with actionable steps, and Arrange follow-up. Readiness shapes how the clinician helps."],
   ["Arrange a follow-up visit",
    "Arrange is the fifth and last step, setting up follow-up to monitor progress. Tell: before arranging follow-up, the clinician assesses readiness and then assists with a plan.", "adjacent fact"],
   ["Assist with a quit plan",
    "Assist, helping set realistic steps and strategies, is the fourth step and depends on knowing his readiness. Tell: Assess comes between Advise and Assist.", "adjacent fact"],
   ["Ask about his smoking again",
    "Ask has already been done; it opens a nonjudgmental conversation about the behavior. Tell: the sequence is Ask, Advise, Assess, Assist, Arrange, so Assess comes next.", "adjacent fact"]],
  C(47), "education", "next step"),

V(CES, IO_POP,
  "A 66-year-old woman with chronic obstructive pulmonary disease comes for a routine visit in October. She has not had any vaccines in the past 5 years. Which vaccines are due now?",
  [["Influenza and pneumococcal vaccines",
    "Correct. Every patient should get a yearly influenza shot, proven to reduce hospitalizations and death, and every patient should receive the pneumococcal vaccine at age 65 to reduce community-acquired pneumonia. At 66 and unvaccinated, she needs both."],
   ["Influenza vaccine alone",
    "The yearly influenza vaccine is due, but at 66 she has also passed the age-65 point for the pneumococcal vaccine. Tell: both vaccines are due in a 66-year-old who has had neither.", "adjacent fact"],
   ["Pneumococcal vaccine alone",
    "The pneumococcal vaccine is due at 65, but the yearly influenza shot is the vaccine proven to reduce hospitalizations and death. Tell: it is October, and she needs both.", "adjacent fact"],
   ["Wait until her next exacerbation",
    "Vaccines prevent exacerbations and pneumonia and are given routinely, not after an exacerbation. Tell: yearly influenza and age-65 pneumococcal vaccination are both due now.", "common lay belief"]],
  C(48), "first-line", "next step"),

V(CES, IO_POP,
  "A 54-year-old man is newly diagnosed with chronic obstructive pulmonary disease, with a forced expiratory volume in 1 second of 35% predicted. He has never had a pneumococcal vaccine. When should he receive it?",
  [["Now, at diagnosis",
    "Correct. The pneumococcal vaccine is routine at 65, but patients with severe disease (1-second volume below 40%) or cardiac comorbidities should get it earlier, essentially when diagnosed and recognized at that severity. At 35% he qualifies now."],
   ["At age 65",
    "Age 65 is the default, but his 1-second volume of 35% is below the 40% severity line that moves vaccination earlier. Tell: severity overrides age here.", "wrong stage or severity"],
   ["After his first exacerbation",
    "The vaccine is meant to prevent community-acquired pneumonia, so waiting for an exacerbation defeats its purpose. Tell: severe disease below 40% calls for vaccination at diagnosis.", "common lay belief"],
   ["Once heart disease develops",
    "Cardiac comorbidity is one reason to vaccinate early, but severe disease below 40% is a separate reason that stands on its own. Tell: his 35% already qualifies him.", "adjacent fact"]],
  C(48), "first-line", "next step"),

# ---------------------------------------------------------------- rehabilitation and referral
V(REH, IO_POP,
  "A 76-year-old woman with group E chronic obstructive pulmonary disease is recovering from a hospitalization. She is breathless walking around her home and has never been referred for rehabilitation. Which referral is most appropriate?",
  [["Pulmonary rehabilitation",
    "Correct. Pulmonary rehabilitation is essential for groups B and E and, next to smoking cessation, tends to be the most effective therapy, reducing dyspnea and readmissions. Older adults are less often referred, so she should be referred actively."],
   ["Thoracic surgery",
    "Possible surgical need is a pulmonology referral reason, but nothing in her story suggests a surgical lesion. Tell: her breathlessness and recent admission call for rehabilitation, essential in group E.", "wrong stage or severity"],
   ["Behavioral health alone",
    "Behavioral health is among the other resources, and anxiety and depression are screened for, but it does not treat her exertional breathlessness. Tell: rehabilitation trains breathing, strength and energy conservation.", "adjacent fact"],
   ["No referral because of her age",
    "Age is not a reason to withhold rehabilitation; older adults are under-referred and should be referred actively. Tell: her group E disease makes rehabilitation essential.", "common lay belief"]],
  CS(43, 53, 55), "referral", "referral"),

V(REH, IO_A,
  "A 58-year-old man with chronic obstructive pulmonary disease has had 4 exacerbations this year despite correct technique and adherence to triple inhaled therapy, completed pulmonary rehabilitation and smoking cessation. Which step is most appropriate?",
  [["Referral to pulmonology",
    "Correct. Frequent exacerbations despite optimal therapy is a listed reason for pulmonology referral, alongside diagnostic uncertainty, early onset, long-term oxygen, evaluation for noninvasive ventilation, possible surgery, and symptoms out of proportion to testing."],
   ["Daily oral corticosteroids",
    "Oral corticosteroids are for acute exacerbations only in this disease, not chronic prevention. Tell: refractory exacerbations on optimal therapy call for a specialist.", "confused mechanism or drug class"],
   ["Stopping the inhaled corticosteroid",
    "Withdrawing an inhaled corticosteroid produces consequences and would not explain his exacerbations. Tell: exacerbations despite optimal therapy are a referral indication.", "common lay belief"],
   ["Repeat spirometry in 1 year",
    "Annual spirometry monitors progression, but waiting a year leaves 4-exacerbation disease without a specialist plan. Tell: frequent exacerbations despite optimal therapy are a reason to refer now.", "adjacent fact"]],
  C(54), "referral", "referral"),

V(REH, IO_PFT,
  "A 52-year-old woman reports severe breathlessness, stopping after about 100 meters on level ground, but her post-bronchodilator forced expiratory volume in 1 second is 82% predicted with a ratio of 0.68. Her heart evaluation is normal. Which step is most appropriate?",
  [["Referral to pulmonology",
    "Correct. Her dyspnea grade of 3 is far worse than her near-normal airflow (grade 1, 82%) would explain. Symptoms out of proportion to pulmonary function tests, like diagnostic uncertainty, is a listed reason for pulmonology referral."],
   ["Triple inhaled therapy",
    "Triple therapy is considered for group E with eosinophils of 300 or more; she has no exacerbations or eosinophil count given. Tell: when symptoms outrun the test results, the next step is a specialist's evaluation.", "wrong stage or severity"],
   ["Reassurance with no follow-up",
    "Her symptoms are real and unexplained by her spirometry, which calls for further evaluation, not reassurance. Tell: symptoms out of proportion to testing are a referral indication.", "common lay belief"],
   ["Long-term oxygen",
    "Long-term oxygen requires a resting arterial oxygen pressure below 55 mmHg or saturation below 88%; nothing shows that here. Tell: the mismatch between symptoms and spirometry calls for referral.", "adjacent fact"]],
  CS(24, 34, 54), "referral", "referral"),

# ---------------------------------------------------------------- oxygen
V(OXY, IO_A,
  "A 70-year-old man with chronic obstructive pulmonary disease has a resting oxygen saturation of 85% on room air on 2 visits, with no cor pulmonale (right heart failure). Which treatment is indicated?",
  [["Long-term oxygen for over 15 hours a day",
    "Correct. Severe resting desaturation, a saturation of 88% or less at rest, qualifies for long-term oxygen therapy for more than 15 hours a day. Oxygen for severe resting hypoxemia decreases the risk of death, prolongs life and improves quality of life."],
   ["Oxygen just during exercise",
    "Exertion-only oxygen is for patients who desaturate to 88% or less with exertion but not at rest. Tell: his saturation is 85% at rest, which qualifies him for oxygen most of the day.", "wrong stage or severity"],
   ["No oxygen until saturation falls below 80%",
    "The threshold is a resting saturation of 88% or less (or an arterial oxygen pressure under 55 mmHg), not 80%. Tell: 85% at rest already qualifies, and waiting forfeits a survival benefit.", "reversed direction or value"],
   ["A sleep study for apnea",
    "Evaluation for obstructive sleep apnea is the step when desaturation happens at night only. Tell: his desaturation is at rest while awake, which calls for long-term oxygen.", "adjacent fact"]],
  CS(63, 64, 66), "first-line", "treatment"),

V(OXY, IO_A,
  "A 67-year-old woman with chronic obstructive pulmonary disease has a resting oxygen saturation of 91% on room air, and she stays at 91% during a walking test. She asks for home oxygen. Which statement is accurate?",
  [["No long-term oxygen is indicated",
    "Correct. A resting saturation of 89% to 93% is moderate resting desaturation, with no indication for long-term oxygen, and her saturation stays at 91% with exertion. Oxygen is indicated with severe hypoxemia, an arterial oxygen pressure under 55 mmHg or saturation of 88% or less."],
   ["She needs oxygen over 15 hours a day",
    "Long-term oxygen for more than 15 hours a day requires severe resting desaturation, 88% or less. Tell: her 91% is moderate desaturation, which does not qualify.", "wrong stage or severity"],
   ["She needs oxygen during exertion",
    "Exertional oxygen is for desaturation to 88% or less with exertion. She stays at 91% while walking. Tell: moderate exertional desaturation, 89% to 93%, gives no indication.", "ruled out by a stated finding"],
   ["She needs a sleep study first",
    "A sleep apnea evaluation is for desaturation at night only. Tell: her daytime readings are moderate, and nothing suggests nocturnal-only desaturation.", "adjacent fact"]],
  C(64), "first-line", "treatment"),

V(OXY, IO_A,
  "A 63-year-old man with chronic obstructive pulmonary disease has a daytime resting oxygen saturation of 94% and normal saturation while walking, but overnight oximetry shows saturations of 86% at night only. Which step is most appropriate?",
  [["Evaluate for obstructive sleep apnea",
    "Correct. Desaturation to 88% or less at night only calls for evaluation for obstructive sleep apnea and screening for other causes, rather than long-term oxygen. His daytime resting and exertional saturations are normal."],
   ["Long-term oxygen over 15 hours a day",
    "Long-term oxygen for more than 15 hours a day is for severe resting desaturation while awake, 88% or less. His daytime resting value is 94%. Tell: night-only drops lead to a sleep evaluation first.", "ruled out by a stated finding"],
   ["Oxygen during exertion",
    "Exertional oxygen is for desaturation to 88% or less with exercise, and his saturation stays normal while walking. Tell: his only drop is overnight, which points to a sleep evaluation.", "ruled out by a stated finding"],
   ["No further evaluation",
    "Nighttime desaturation is not ignored; it prompts evaluation for obstructive sleep apnea and other causes. Tell: night-only desaturation has its own branch of the oxygen pathway.", "common lay belief"]],
  C(64), "initial test", "test"),

V(OXY, IO_A,
  "A 68-year-old woman with chronic obstructive pulmonary disease has a resting oxygen saturation of 93%, but during a walking test she drops to 85%. She is mobile and reports exertional breathlessness. Which oxygen plan is indicated?",
  [["Oxygen during exertion",
    "Correct. Severe exertional desaturation, 88% or less with exertion, qualifies for long-term oxygen during exertion. Her resting saturation of 93% is moderate desaturation, without a resting indication, so oxygen is used with activity."],
   ["Oxygen over 15 hours a day",
    "Oxygen for more than 15 hours a day requires severe resting desaturation, 88% or less at rest. She is 93% at rest. Tell: her drop happens with exertion, so oxygen is given during exertion.", "ruled out by a stated finding"],
   ["No oxygen for now",
    "Her drop to 85% while walking is severe exertional desaturation, which qualifies for oxygen during exertion. Tell: a normal-looking resting value does not rule out an exertional indication.", "reversed direction or value"],
   ["Oxygen just at night",
    "Night-only desaturation leads to an evaluation for obstructive sleep apnea, and her drop happens while walking. Tell: oxygen should match the setting where she desaturates, exertion.", "adjacent fact"]],
  C(64), "first-line", "treatment"),
]
