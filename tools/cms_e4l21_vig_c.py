# -*- coding: utf-8 -*-
"""Lecture 21 vignette pool C -- Hypotension: cardiogenic syncope, acute versus
chronic hypotension, causes, pressors and age-specific norms.

KEYS ARE WRITTEN SHORT ON PURPOSE — detail lives in the explanation.

Cardiogenic syncope is taught as three types, each with its own work-up and a
cardiology consultation, so these stems ask for the test, the referral or the
setting rather than a treatment the slides never give. Dispositions from the
worked cases were spoken, not written, so no stem asks for one.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e4l21_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


QUESTIONS = [

V("Cardiogenic syncope", IO4,
  "A 74-year-old man with a prior heart attack and reduced ejection fraction collapsed abruptly while walking, with no warning except a brief racing heartbeat. He is pale, his pressure is 86/52 and his heart rate is 150 and regular. What is the most likely diagnosis?",
  [["Cardiogenic syncope from an arrhythmia",
    "Correct. Abrupt collapse with minimal prodrome after palpitations, in a patient with coronary disease and reduced ejection fraction, with a rapid regular rhythm, points to an arrhythmic cardiac cause."],
   ["Vasovagal reflex syncope",
    "Vasovagal syncope follows triggers such as fear or heat with a warm, nauseated prodrome and a slow rather than fast heart rate."],
   ["Non-neurogenic orthostatic hypotension",
    "Non-neurogenic orthostatic hypotension follows standing, often with volume loss; he collapsed abruptly mid-walk after palpitations."],
   ["Situational reflex syncope",
    "Situational syncope follows a bodily function such as urination, with a reflex prodrome and quick recovery."]],
  C(40), "differential", "diagnosis"),

V("Cardiogenic syncope", IO4,
  "A 68-year-old woman with coronary disease felt her heart race and then collapsed without warning in a store. She has recovered and is stable in the office. Which test should be obtained first?",
  [["An electrocardiogram",
    "Correct. A suspected arrhythmia is investigated first with an electrocardiogram, then monitoring, a stress test and cardiology consultation."],
   ["A tilt-table test",
    "Tilt-table testing is listed for postural orthostatic tachycardia syndrome, not for a suspected arrhythmia."],
   ["An episode log",
    "An episode log supports the history in reflex syncope; palpitations before an abrupt collapse call for a rhythm tracing."],
   ["Orthostatic vital signs",
    "Orthostatic readings look for a postural fall; her abrupt collapse with palpitations points to the heart rhythm."]],
  C(16), "initial test", "test"),

V("Cardiogenic syncope", IO4,
  "A 72-year-old man's electrocardiogram shows runs of nonsustained ventricular tachycardia after an abrupt faint preceded by palpitations. Which referral is most appropriate?",
  [["Cardiology consultation",
    "Correct. Every type of cardiogenic syncope, arrhythmic, structural and vascular, lists cardiology consultation alongside its tests."],
   ["Neurology consultation",
    "Neurologic input suits autonomic failure or suspected seizure; an arrhythmic faint is referred to cardiology."],
   ["Endocrinology referral",
    "Endocrine disease such as diabetes causes neurogenic orthostatic hypotension, not a ventricular arrhythmia."],
   ["Physical therapy referral",
    "Physical therapy has no listed role in cardiogenic syncope, whose work-up pairs cardiac testing with cardiology."]],
  C(16), "referral", "referral"),

V("Cardiogenic syncope", IO4,
  "A 69-year-old man with a known aortic aneurysm faints suddenly in the clinic waiting room and now has severe chest pain. Which is the most appropriate next step?",
  [["Emergent testing in the emergency department",
    "Correct. Vascular causes of cardiogenic syncope, dissection, aneurysm, stroke and pulmonary embolism, call for emergent testing in the emergency department plus cardiology consultation."],
   ["An outpatient echocardiogram next week",
    "Outpatient echocardiography suits a stable structural question; a suspected vascular catastrophe cannot wait."],
   ["A symptom log for a month",
    "A log supports the history in reflex syncope and has no place when a vascular emergency is suspected."],
   ["Orthostatic vitals and reassurance",
    "Orthostatic readings test for postural hypotension; a faint with a known aneurysm and chest pain needs emergent testing."]],
  C(16), "referral", "next step"),

V("Cardiogenic syncope", IO4,
  "A 71-year-old woman with a known cardiomyopathy has had two faints on exertion. Her electrocardiogram shows no arrhythmia. Which test best evaluates a structural cause?",
  [["An echocardiogram",
    "Correct. Structural causes, infarction, cardiomyopathy, heart failure and valve disease, are evaluated with echocardiography or stress echocardiography plus cardiology consultation."],
   ["A tilt-table test",
    "Tilt-table testing is for postural orthostatic tachycardia syndrome, not the evaluation of a cardiomyopathy."],
   ["A blood glucose level",
    "Glucose excludes hypoglycemia, a non-hypotensive cause, but does not image the heart's structure."],
   ["An episode log",
    "A log supports reflex syncope; exertional faints with a cardiomyopathy need cardiac imaging."]],
  C(16), "gold standard", "test"),

V("Cardiogenic syncope", IO4,
  "A 70-year-old man with valve disease faints on exertion, and his echocardiogram confirms a structural cause. Which referral is appropriate?",
  [["Cardiology consultation",
    "Correct. Structural cardiogenic syncope is worked up with echocardiography or stress echocardiography together with cardiology consultation."],
   ["Neurology consultation",
    "Neurology suits autonomic failure or suspected seizure, not structural heart disease."],
   ["Endocrinology referral",
    "Endocrine referral fits diabetes-related autonomic neuropathy, which is an orthostatic, not structural, cause."],
   ["No referral is needed",
    "Each type of cardiogenic syncope lists cardiology consultation, so a structural cause is not managed without it."]],
  C(16), "referral", "referral"),


V("Causes of hypotension", IO3,
  "A 66-year-old woman in a clinic has hypotension from a suspected overwhelming infection and is awaiting transfer. Which therapy should not be started in the clinic?",
  [["A norepinephrine infusion",
    "Correct. Epinephrine, norepinephrine, dopamine, phenylephrine and vasopressin are listed for the emergency department and intensive care only."],
   ["Arranging urgent transfer",
    "Arranging transfer is appropriate, because the drugs her hypotension may need are used only in the emergency department and intensive care."],
   ["Repeating her vital signs",
    "Repeated readings are appropriate, since each reading is only a snapshot in time."],
   ["Reviewing her medications",
    "Reviewing medications is appropriate, since medication-mediated hypotension is treated by reducing the offending drug."]],
  C(23), "avoid", "avoid"),

V("Acute versus chronic", IO3,
  "A 79-year-old woman with cardiomyopathy has had pressures around 92/58 for many months. She has intermittent lightheadedness that comes and goes. How is her hypotension best classified?",
  [["Chronic cardiogenic hypotension",
    "Correct. Cardiogenic causes such as cardiomyopathy and reduced ejection fraction heart failure produce chronic hypotension, which waxes and wanes and is intermittently symptomatic."],
   ["Acute toxic hypotension",
    "Toxic or medication-mediated overdose causes acute hypotension of sudden onset with a specific trigger."],
   ["Long-lasting acute infectious hypotension",
    "Infection from bacteremia to septic shock causes long-lasting acute hypotension, not months of waxing symptoms."],
   ["Acute reflex hypotension",
    "Reflex hypotension is triggered and transient, not a pressure that runs low for months."]],
  C(22), "manifestation", "diagnosis"),

V("Acute versus chronic", IO3,
  "A 34-year-old man is brought in after taking a large quantity of a relative's blood pressure pills. His pressure dropped suddenly over the past hour and he is dizzy. How is his hypotension best classified?",
  [["Acute hypotension from a toxic cause",
    "Correct. Medication-mediated overdose is a toxic cause of acute hypotension, which is of sudden onset, usually symptomatic and tied to a specific trigger."],
   ["Chronic hypotension from a cardiac cause",
    "Chronic hypotension comes from cardiogenic causes such as cardiomyopathy and waxes and wanes over time."],
   ["Long-lasting acute infectious hypotension",
    "Infection causes long-lasting acute hypotension, and nothing here suggests bacteremia or sepsis."],
   ["Neurogenic orthostatic hypotension",
    "Neurogenic orthostatic hypotension is a postural fall from autonomic failure, not a sudden drop after an overdose."]],
  C(22), "etiology", "diagnosis"),

V("Acute versus chronic", IO3,
  "A 76-year-old man with reduced ejection fraction heart failure has run low pressures for a year and asks whether his low pressure will simply go away. What is the most accurate answer?",
  [["Its cause may not be removable",
    "Correct. Chronic hypotension waxes and wanes, and its underlying cause, here heart failure, may be unavoidable, unlike an acute trigger that can be removed."],
   ["It will end once a trigger is found",
    "Removing a trigger fits acute or reflex hypotension; chronic cardiogenic hypotension may have an unavoidable cause."],
   ["It always resolves within weeks",
    "Chronic hypotension persists and waxes and wanes rather than resolving within weeks."],
   ["It needs a vasopressor at home",
    "Vasopressors are for the emergency department and intensive care only, not home management of chronic hypotension."]],
  C(21), "prognosis", "complication"),

V("Non-hypotensive syncope", IO4,
  "A 70-year-old man fainted at home and has recovered. His electrocardiogram and glucose are normal. Which tests look for an infectious or metabolic contributor?",
  [["A blood count and metabolic panel",
    "Correct. Unremarkable blood counts and a metabolic panel lower suspicion of an infectious or metabolic source, as glucose and the electrocardiogram address hypoglycemia and dysrhythmia."],
   ["A tilt-table test and a log",
    "A tilt-table test belongs to the tachycardia syndrome and a log to reflex syncope; neither screens for infection."],
   ["An echocardiogram and stress test",
    "These evaluate structural and arrhythmic cardiac causes rather than infection or metabolic disturbance."],
   ["Orthostatic vitals only",
    "Orthostatic readings test for a postural fall and cannot detect an infectious or metabolic source."]],
  C(27), "initial test", "test"),

V("Cardiogenic syncope", IO2,
  "A 72-year-old man has diabetic autonomic neuropathy and also congestive heart failure. He faints on standing. Which of the following should be avoided?",
  [["Fludrocortisone",
    "Correct. Fludrocortisone causes salt and water retention and is avoided in congestive heart failure, even though it is best with the tachycardia syndrome."],
   ["Slow position changes",
    "Slow positional changes are first-line for orthostatic syncope and are safe alongside heart failure."],
   ["Treating the underlying cause",
    "Treating the underlying condition is the central principle for orthostasis and is never avoided."],
   ["A careful history",
    "History is the most important part of diagnosing the source of orthostatic syncope and is always appropriate."]],
  C(23), "avoid", "avoid"),


V("Blood pressure norms", IO5,
  "A 3-year-old boy has his pressure recorded at a well visit, and a new staff member flags it as low by comparing it with an adult's normal range. Which is the most appropriate next step?",
  [["Compare it with norms for his age",
    "Correct. Blood pressure norms are affected by age, so a child's reading is judged against the normal range for his age rather than an adult's."],
   ["Start a vasopressor for hypotension",
    "Vasopressors are for the emergency department and intensive care, and a reading has not yet been shown to be low for his age."],
   ["Order an echocardiogram at once",
    "Echocardiography evaluates structural heart disease; the first step is judging the reading against age-specific norms."],
   ["Measure it again in adult units",
    "The units are not the issue; the reference range is, because norms change with age."]],
  C(20), "test finding", "test"),

V("Cardiogenic syncope", IO4,
  "A 66-year-old woman with prior heart attacks collapsed without any prodrome while climbing stairs and woke within 20 seconds. Which referral should accompany her cardiac testing?",
  [["Cardiology consultation",
    "Correct. Arrhythmic, structural and vascular cardiogenic syncope each pair their tests with cardiology consultation."],
   ["Physical therapy referral",
    "Physical therapy is not part of the listed cardiogenic work-up, which pairs cardiac tests with cardiology."],
   ["Neurology consultation",
    "Neurology suits autonomic failure or seizure; an abrupt collapse with cardiac history points to cardiology."],
   ["Dietitian referral",
    "A dietitian has no listed role in cardiogenic syncope, whose work-up pairs cardiac tests with cardiology consultation."]],
  C(16), "referral", "referral"),

V("Cardiogenic syncope", IO4,
  "A 75-year-old man with reduced ejection fraction heart failure faints abruptly while walking after a brief racing heartbeat. After his electrocardiogram, which further test helps capture an intermittent arrhythmia?",
  [["Cardiac monitoring",
    "Correct. The arrhythmia work-up is an electrocardiogram, cardiac monitoring and a stress test, together with cardiology consultation."],
   ["A tilt-table test",
    "Tilt-table testing is listed for postural orthostatic tachycardia syndrome, not for capturing an arrhythmia."],
   ["A patient log alone",
    "A log supports reflex syncope; an intermittent arrhythmia is captured by monitoring the rhythm."],
   ["Orthostatic vitals",
    "Orthostatic readings test for a postural fall; an abrupt faint after palpitations needs rhythm monitoring."]],
  C(16), "initial test", "test"),

V("Drug therapy", IO2,
  "A 67-year-old woman with neurogenic orthostatic hypotension asks whether she can keep a vasopressor at home for bad days. What should she be told?",
  [["Pressors are hospital-only drugs",
    "Correct. Epinephrine, norepinephrine, dopamine, phenylephrine and vasopressin are listed for the emergency department and intensive care only."],
   ["A home supply is reasonable",
    "Pressors are not outpatient drugs; home options for neurogenic syncope are midodrine or droxidopa with slow position changes."],
   ["Only if she avoids salt",
    "Salt is not the issue; pressors are used only in the emergency department and intensive care."],
   ["Only after a tilt-table test",
    "A tilt-table test is for the tachycardia syndrome and would not make a pressor safe for home use."]],
  C(23), "avoid", "education"),

V("Hypotension definition", IO1,
  "A 58-year-old man's pressure is 100/64, which is normal for many adults but far below his usual 150/90, and he now feels lightheaded. How should this reading be interpreted?",
  [["As relative hypotension for him",
    "Correct. Hypotension is a fall below normal, and normal is judged against the patient's age, comorbidities and own baseline, so a relative fall can be significant."],
   ["As normal, since it is above 90",
    "No single fixed number defines hypotension; relative hypotension must be considered against the patient's usual pressure."],
   ["As a measurement artifact",
    "A reading consistent with his symptoms should not be dismissed; each reading is a snapshot to interpret, not to discard."],
   ["As proof of autonomic failure",
    "Autonomic failure is shown by a postural fall with a minimal heart rate rise, not by one resting reading."]],
  C(20), "test finding", "test"),

]
