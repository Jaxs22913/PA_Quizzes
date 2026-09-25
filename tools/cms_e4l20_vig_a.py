# -*- coding: utf-8 -*-
"""Lecture 20 vignette pool A -- Hypertension: diagnosis, classification and secondary causes.

Patient vignettes with a varied lead-in, per [[vignette_question_style]]. The
lead-in decides the answer, so the same scenario can ask for the diagnosis, the
next step, the initial test or the education point and get a different key each
time. Distractors are right-disease/wrong-phase wherever the material allows.

Sourcing as in the objective pools: slides only. The lecture WAS recorded (two
parts, 17 September) but sits behind the transcription queue, which runs in
exam-date order and has not reached Exam 4.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Hypertension: classification, subtypes, effects on target organs, etiologies, "
      "epidemiology, risk factors, clinical manifestations, differential diagnosis, "
      "diagnostic testing, management, referrals, patient education, and prognosis")
C = lambda n: "20. Hypertension - Jaquith.pptx, Slide %d" % n

QUESTIONS = [

Q("Measurement technique", IO,
  "A 54-year-old arrives late for a routine visit, is taken straight to the room and has her blood pressure measured immediately while she describes her morning. The cuff is placed over her sleeve and her legs are crossed. The reading is 152/94. What is the most appropriate next step?",
  [["Repeat it after five minutes of quiet rest",
    "Correct. Every departure here inflates the reading: no rest period, talking during the measurement, a sleeved arm and crossed legs. A diagnosis rests on readings taken to standard, and acting on this one would start treatment on an artifact. Correct technique matters as much as the rest period."],
   ["Diagnose stage 2 hypertension and start two agents",
    "Two complementary agents are reasonable when pressure is substantially above goal, but not on "
    "a single reading taken outside standard conditions."],
   ["Order plasma metanephrines to exclude pheochromocytoma",
    "Metanephrines are ordered when the history suggests episodic headache, sweating and "
    "palpitations, not because one office reading was high."],
   ["Reassure her that a single elevated reading is meaningless",
    "It is not meaningless; it needs repeating under proper conditions. At least two readings are "
    "obtained, with any deviation from standard technique documented."]], C(38)),

Q("Measurement technique", IO,
  "A 61-year-old man's blood pressure is 148/88 in the right arm and 132/80 in the left at his first visit. He has no chest pain and his pulses are symmetric and normal. Which arm should be used at follow-up visits?",
  [["Use the right arm for all subsequent measurements",
    "Correct. Both arms are measured at the initial visit precisely to find a difference, and the "
    "higher consistent arm becomes the one used for follow-up. Averaging the two would systematically "
    "understate his pressure."],
   ["Average the two readings and record 140/84",
    "The higher consistent arm is used rather than an average, since the lower arm underestimates "
    "the central pressure."],
   ["Image immediately for aortic dissection",
    "Asymmetric pressures raise concern for dissection when they are NEW and accompanied by abrupt "
    "severe pain. Neither is present here."],
   ["Compare arm and leg pressures to exclude coarctation",
    "Coarctation is suggested by weak or delayed femoral pulses with upper limb hypertension, not by "
    "a difference between the two arms."]], C(39)),

Q("Coarctation of the aorta", IO,
  "A 22-year-old man is found to have a blood pressure of 158/92 in both arms. His femoral pulses are weak and delayed relative to the radial pulses, and his leg systolic pressure is lower than his arm pressure. What is the most likely diagnosis?",
  [["Coarctation of the aorta",
    "Correct. Leg systolic normally EXCEEDS arm systolic, so a reversal is the abnormal finding, and "
    "radial-femoral delay places a structural obstruction between the two territories. Early onset "
    "hypertension is itself a clue to a secondary cause."],
   ["Renovascular disease from fibromuscular dysplasia",
    "Fibromuscular dysplasia causes early-onset hypertension in young patients, but through renal "
    "artery narrowing, which produces an abdominal bruit rather than radial-femoral delay."],
   ["Primary aldosteronism",
    "Aldosteronism is screened for in early or resistant hypertension, but it does not alter the "
    "femoral pulses or the arm-to-leg pressure relationship."],
   ["Primary hypertension",
    "Onset this early, with an abnormal pulse examination, points away from primary hypertension and "
    "toward a structural cause."]], C(40)),

Q("Coarctation of the aorta", IO,
  "A 24-year-old woman with hypertension has weak delayed femoral pulses and a leg pressure lower "
  "than her arm pressure. Which study establishes the diagnosis?",
  [["Echocardiography",
    "Correct, and the referral that follows is to a vascular surgeon or a structural cardiologist. "
    "The bedside findings raise the question; the echocardiogram answers it."],
   ["Renal duplex ultrasound",
    "Renal duplex investigates renovascular disease, which is suggested by an abdominal bruit and "
    "asymmetric kidneys rather than by femoral pulse delay."],
   ["A morning aldosterone to renin ratio",
    "That screens for primary aldosteronism, which does not produce an arm-to-leg pressure gradient."],
   ["Polysomnography",
    "Sleep study investigates obstructive sleep apnea, suggested by snoring and witnessed apneas."]],
  C(34)),

Q("Renovascular disease", IO,
  "A 68-year-old smoker with peripheral arterial disease has blood pressure of 168/94 despite three agents. An abdominal bruit is audible, ultrasound shows a right kidney 2 cm smaller than the left, and he has had two episodes of sudden pulmonary edema. What is the most likely underlying cause?",
  [["Renovascular disease",
    "Correct. The cluster is characteristic: resistant pressure, an abdominal bruit, asymmetric "
    "kidneys and recurrent flash pulmonary edema. In an older patient with established vascular "
    "disease the mechanism is atherosclerotic stenosis, often bilateral and progressive."],
   ["Primary aldosteronism",
    "Aldosteronism also presents with resistant hypertension, but with unexplained hypokalemia "
    "rather than asymmetric kidneys and an abdominal bruit."],
   ["Chronic kidney disease from diabetes",
    "Diabetic kidney disease reduces both kidneys' function together rather than producing a 2 cm "
    "size discrepancy with a bruit."],
   ["Obstructive sleep apnea",
    "Sleep apnea contributes to resistant hypertension, but through nocturnal sympathetic "
    "activation, without bruits or asymmetric kidneys."]], C(15)),

Q("Renovascular disease", IO,
  "A 71-year-old woman with resistant hypertension is started on lisinopril. Her creatinine rises "
  "markedly within a week. What does this suggest?",
  [["Bilateral renal artery stenosis",
    "Correct. Where perfusion depends on angiotensin-mediated efferent arteriolar tone, blocking it drops the filtration pressure sharply. This is one of the recognized clues to renovascular disease, and it is why the agent is contraindicated in bilateral stenosis. A hemodynamically significant unilateral stenosis does the same."],
   ["Expected drug effect requiring no change in approach",
    "A small early creatinine rise can be acceptable, but a MARKED rise specifically points toward "
    "renovascular disease rather than being dismissed."],
   ["Progression of underlying diabetic nephropathy",
    "Diabetic nephropathy declines over months to years rather than jumping within a week of "
    "starting a renin-angiotensin blocker."],
   ["Acute interstitial nephritis from the medication",
    "Interstitial nephritis is not the mechanism described for this pattern; the abrupt rise on "
    "renin-angiotensin blockade points to renal artery stenosis."]], C(14)),

Q("Renovascular disease", IO,
  "A 66-year-old with confirmed renal artery stenosis has recurrent flash pulmonary edema and "
  "progressive renal decline despite optimal medical therapy. What is the appropriate step?",
  [["Early referral for revascularization assessment",
    "Correct. Recurrent flash pulmonary edema, progressive renal decline despite optimal therapy, "
    "and truly refractory control are the three features that trigger early referral, rather than "
    "the mere presence of narrowing on imaging."],
   ["Continue medical therapy; revascularization is never indicated",
    "Those three specific features are exactly the situations in which referral is indicated."],
   ["Refer any patient in whom screening finds renal artery narrowing",
    "Narrowing found on screening does not by itself warrant intervention; the clinical features "
    "listed do."],
   ["Add a second dihydropyridine calcium channel blocker",
    "Adding a second agent of the same class does not address the anatomic problem and is not among "
    "the described steps."]], C(17)),

Q("Primary aldosteronism", IO,
  "A 47-year-old man has blood pressure of 162/98 on three agents. His potassium is 3.1 mmol/L "
  "without diuretic use. Which screening test is appropriate?",
  [["A morning aldosterone to renin ratio",
    "Correct. Resistant hypertension with unexplained hypokalemia is a classic trigger to screen, "
    "and the ratio is positive above roughly 20:1 provided the aldosterone concentration itself is "
    "adequate."],
   ["Plasma free metanephrines",
    "Metanephrines screen for pheochromocytoma, suggested by episodic headache, sweating and "
    "palpitations rather than by hypokalemia."],
   ["A low-dose dexamethasone suppression test",
    "That screens for Cushing syndrome, suggested by proximal muscle weakness, easy bruising, thin "
    "skin and broad purple striae."],
   ["Renal duplex ultrasound",
    "Renal duplex investigates renovascular disease, suggested by an abdominal bruit and asymmetric "
    "kidneys."]], C(20)),

Q("Primary aldosteronism", IO,
  "A 39-year-old woman is referred with hypertension diagnosed at 32 and an adrenal nodule found "
  "incidentally on imaging. What is the underlying abnormality if aldosteronism is confirmed?",
  [["Autonomous aldosterone production independent of renin",
    "Correct. The adrenal gland secretes aldosterone without the usual renin-angiotensin signal, so "
    "sodium is retained and potassium wasted regardless of volume status."],
   ["Excess renin driving aldosterone production",
    "Renin-driven aldosterone excess is secondary rather than primary aldosteronism, and occurs in "
    "renovascular disease."],
   ["Glucocorticoid excess promoting sodium retention",
    "That is Cushing syndrome, which carries proximal weakness, bruising, thin skin and purple "
    "striae."],
   ["Catecholamine excess from an adrenal medullary tumor",
    "That is pheochromocytoma, which produces the paroxysmal five Ps rather than sustained "
    "aldosterone-driven sodium retention."]], C(18)),

Q("Pheochromocytoma", IO,
  "A 44-year-old man describes episodes of pounding headache, drenching sweats, palpitations and pallor, each lasting about twenty minutes. Between episodes he feels well. His blood pressure is 176/104 during an episode. What is the most likely diagnosis?",
  [["Pheochromocytoma",
    "Correct. The five Ps are pressure, perspiration, palpitations, pallor and tremor, and the "
    "paroxysmal pattern with well intervals is what distinguishes it from sustained hypertension."],
   ["Primary aldosteronism",
    "Aldosteronism raises pressure steadily with hypokalemia rather than producing discrete "
    "symptomatic paroxysms."],
   ["Obstructive sleep apnea",
    "Sleep apnea drives sustained sympathetic activation through nocturnal hypoxemia, presenting "
    "with snoring and daytime sleepiness rather than daytime paroxysms."],
   ["Hyperthyroidism",
    "Thyroid excess raises cardiac output with predominantly systolic elevation and persistent "
    "symptoms rather than episodic pallor and sweating."]], C(29)),

Q("Pheochromocytoma", IO,
  "A 44-year-old man with episodic headache, sweating, palpitations and pallor has raised plasma "
  "free metanephrines and an adrenal mass. He is scheduled for resection. What must be established "
  "before surgery?",
  [["Alpha blockade first, then beta blockade",
    "Correct, and the order is not negotiable: isolated beta blockade leaves alpha-mediated "
    "vasoconstriction unopposed and can precipitate a hypertensive crisis."],
   ["Beta blockade first, then alpha blockade",
    "This reversal is the dangerous one. Beta blockade without prior alpha blockade leaves "
    "vasoconstriction unopposed."],
   ["Either order, provided both are established before surgery",
    "The sequence itself matters, which is why alpha blockade is specified first and beta blockade only afterwards."],
   ["Neither, provided the tumor is resected promptly",
    "Blockade is required before resection to prevent catecholamine surge during manipulation."]],
  C(32)),

Q("Cushing syndrome", IO,
  "A 51-year-old woman with newly diagnosed hypertension has proximal muscle weakness, easy bruising, thin skin and broad purple abdominal striae with central adiposity. What is the most likely underlying cause?",
  [["Cushing syndrome",
    "Correct. The cluster of proximal weakness, bruising, thin skin, broad purple striae and central "
    "adiposity points to glucocorticoid excess as the secondary cause of her hypertension."],
   ["Pheochromocytoma",
    "Pheochromocytoma produces episodic headache, sweating, palpitations and pallor rather than the "
    "skin and muscle changes described."],
   ["Primary aldosteronism",
    "Aldosteronism presents with resistant hypertension and unexplained hypokalemia rather than "
    "striae and proximal weakness."],
   ["Obstructive sleep apnea",
    "Sleep apnea is suggested by loud snoring, witnessed apneas and daytime sleepiness."]], C(28)),

Q("Obstructive sleep apnea", IO,
  "A 55-year-old man with obesity has blood pressure of 158/96 on three agents. His partner reports "
  "loud snoring and witnessed pauses in breathing, and he is sleepy during the day. What confirms "
  "the suspected cause?",
  [["Polysomnography or validated home sleep apnea testing",
    "Correct. The history raises the suspicion and the sleep study establishes it. Undiagnosed sleep "
    "apnea is one of the causes to exclude before labeling hypertension as resistant."],
   ["The STOP-BANG questionnaire alone",
    "A questionnaire identifies who should be tested rather than confirming the diagnosis."],
   ["Overnight ambulatory blood pressure monitoring",
    "Ambulatory monitoring characterizes the pressure pattern but does not establish apnea."],
   ["A morning aldosterone to renin ratio",
    "That screens for primary aldosteronism, which is suggested by resistant pressure with unexplained hypokalemia."]], C(23)),

Q("Obstructive sleep apnea", IO,
  "By what mechanism does obstructive sleep apnea raise blood pressure?",
  [["Intermittent hypoxemia drives sympathetic activation",
    "Correct. Recurrent airway obstruction produces repeated hypoxemia and arousal, and the "
    "resulting sympathetic drive persists into waking hours rather than resolving with the night."],
   ["Impaired sodium excretion expands extracellular volume",
    "Impaired sodium excretion is the mechanism in chronic kidney disease rather than in obstructive sleep apnea."],
   ["Autonomous aldosterone secretion",
    "Autonomous aldosterone secretion is primary aldosteronism, a separate secondary cause with its own screening test."],
   ["Mechanical compression of the renal arteries",
    "No such compression is described; the mechanism is neurohormonal rather than anatomic."]], C(22)),

Q("Chronic kidney disease", IO,
  "A 63-year-old with long-standing hypertension has an estimated filtration rate that has fallen over eighteen months and a rising urine albumin-to-creatinine ratio. He also has type 2 diabetes. What should be done next?",
  [["Evaluate for alternative renal causes too",
    "Correct. Not all chronic kidney disease in a hypertensive patient is hypertensive, and diabetes "
    "must be evaluated. The relationship is bidirectional, so the presence of both does not establish "
    "which came first."],
   ["Attribute it all to hypertension and intensify control",
    "Control matters, but attributing everything to the pressure risks missing a second treatable "
    "disease."],
   ["Attribute it all to diabetes and stop antihypertensives",
    "Hypertension injures renal vessels, glomeruli and interstitium, and withdrawing therapy would "
    "accelerate the decline."],
   ["Conclude the albuminuria is a laboratory artifact",
    "Rising albuminuria and falling filtration are the earliest measurable markers of renal damage "
    "and are tracked as trends rather than dismissed."]], C(28)),

Q("Chronic kidney disease", IO,
  "A 58-year-old man is found to have a raised creatinine. What is required before chronic kidney "
  "disease can be diagnosed?",
  [["A kidney abnormality persisting three months",
    "Correct. A single raised value may reflect a reversible insult, so duration is part of the "
    "definition rather than an optional confirmation."],
   ["A single raised creatinine measurement",
    "One measurement does not establish chronicity, which is what the three-month requirement tests."],
   ["Structural renal disease demonstrated on imaging",
    "Imaging may support a cause, but the definition turns on a persisting abnormality rather than "
    "a structural finding."],
   ["Albuminuria alone, regardless of duration",
    "Albuminuria is one marker of kidney damage, but the three-month persistence requirement still "
    "applies."]], C(12)),

Q("Drug-induced hypertension", IO,
  "A 43-year-old woman's previously well-controlled blood pressure has risen over two months. She "
  "denies missing doses. What should the medication review specifically cover beyond her prescriptions?",
  [["Over-the-counter drugs, licorice and supplements",
    "Correct, and patients frequently do not volunteer any of these because they do not regard them as medication. A sudden loss of previously stable control is itself a clue to a secondary cause. Recreational substances belong in the same review."],
   ["Only agents started within the past week",
    "The review is not bounded that tightly; a substance taken for months can be responsible."],
   ["Only intravenous medications given in hospital",
    "The categories named are over-the-counter, recreational, licorice and herbal supplements."],
   ["Only her antihypertensive agents",
    "Reviewing the antihypertensives addresses adherence, but the question is what else may be "
    "raising the pressure."]], C(25)),

Q("Alcohol", IO,
  "A 49-year-old man who drinks heavily is admitted for an unrelated procedure. On the second day "
  "his blood pressure rises sharply. What explains this?",
  [["Alcohol withdrawal can produce acute severe hypertension",
    "Correct, and the relationship runs both ways: excess alcohol raises blood pressure chronically, "
    "and withdrawal from it can raise it acutely."],
   ["Alcohol lowers pressure, so stopping returns him to baseline",
    "Excess alcohol raises rather than lowers blood pressure, so this reverses the relationship."],
   ["Only chronic excess raises pressure; withdrawal has no effect",
    "Withdrawal is specifically capable of producing acute severe hypertension, which is what is happening here."],
   ["Moderate alcohol should be resumed for cardiovascular benefit",
    "Starting or resuming alcohol for cardiovascular benefit is specifically not recommended; intake "
    "is limited to low-risk thresholds."]], C(26)),

Q("Thyroid disease", IO,
  "A 58-year-old woman with fatigue, cold intolerance and constipation is found to have blood "
  "pressure of 146/96 with a predominantly diastolic elevation. Which mechanism fits?",
  [["Hypothyroidism raising vascular resistance",
    "Correct. Hypothyroidism raises systemic vascular resistance, which lifts the diastolic pressure, "
    "whereas hyperthyroidism raises cardiac output and lifts the systolic."],
   ["Hyperthyroidism raising cardiac output",
    "That produces a predominantly SYSTOLIC elevation with tachycardia, and her symptoms point the "
    "other way."],
   ["Catecholamine excess from an adrenal tumor",
    "Pheochromocytoma causes paroxysmal symptoms rather than the sustained hypothyroid picture "
    "described."],
   ["Autonomous aldosterone secretion",
    "Aldosteronism produces resistant hypertension with hypokalemia rather than cold intolerance "
    "and constipation."]], C(27)),

Q("Secondary hypertension", IO,
  "Which pattern of hypertension should prompt a search for a secondary cause?",
  [["Early or abrupt onset, resistance, or lost control",
    "Correct. Each departs from the gradual course expected of primary hypertension, which is what "
    "makes the pattern itself the clue rather than any single reading."],
   ["Gradual elevation over many years in an older adult",
    "That is the expected course of primary hypertension, which accounts for the vast majority of "
    "adult cases."],
   ["Blood pressure that responds well to a single first-line agent",
    "A good response to one agent is reassuring rather than a trigger for further investigation."],
   ["Elevated readings confined to the clinic setting",
    "That describes white coat hypertension, which is characterized by out-of-office monitoring "
    "rather than by a secondary workup."]], C(8)),

Q("White coat hypertension", IO,
  "A 46-year-old woman consistently reads 150/92 in clinic but her seven-day home average is 118/74 with a validated upper-arm device and correct technique. Which pattern does this represent?",
  [["White coat hypertension",
    "Correct: raised office readings with normal out-of-office readings. Recognizing it avoids "
    "treating a patient whose true pressure is normal."],
   ["Masked hypertension",
    "Masked hypertension is the reverse pattern, with normal office readings and raised out-of-office "
    "readings, and it carries clinically important cardiovascular risk."],
   ["Resistant hypertension",
    "Resistance means pressure above goal despite three complementary drugs at maximally tolerated "
    "doses, which is not the situation here."],
   ["Stage 2 hypertension",
    "Her out-of-office readings are normal, so the office values do not establish a stage."]], C(48)),

Q("Masked hypertension", IO,
  "A 52-year-old man reads 124/78 in clinic, but his home average over seven days is 142/90. Why "
  "does this matter?",
  [["It carries real risk despite normal office readings",
    "Correct. This is masked hypertension, and it is the reason out-of-office measurement is not "
    "merely a way of avoiding overtreatment: it also finds the patients whose risk the clinic reading "
    "conceals."],
   ["It is a benign pattern requiring no follow-up",
    "It carries clinically important cardiovascular risk, which is precisely why identifying it "
    "matters."],
   ["It indicates his home device is miscalibrated",
    "A validated upper-arm device used to the standard schedule is the reference, not the office "
    "reading."],
   ["It means he has white coat hypertension",
    "White coat hypertension is the opposite pattern, with high office and normal home readings."]],
  C(48)),

Q("Home monitoring", IO,
  "A 50-year-old man starting home monitoring asks how to do it. What should he be told?",
  [["Two readings morning and evening for seven days",
    "Correct, and the accompanying instruction matters as much: do not overreact to the highest single reading, because acting on outliers generates anxiety and unnecessary changes in therapy. They are taken at least a minute apart and the average is reported."],
   ["One reading each morning for three days",
    "That collects far less data than the standard schedule and is more vulnerable to a single odd "
    "value."],
   ["Readings only when he feels unwell",
    "Most patients with mild to moderate hypertension have no reliable blood pressure-related "
    "symptoms, so symptom-triggered readings would miss the point."],
   ["Continuous monitoring over twenty-four hours at home",
    "That describes ambulatory monitoring rather than the home schedule with a validated upper-arm "
    "device."]], C(45)),

Q("Baseline evaluation", IO,
  "A 45-year-old man is newly diagnosed with hypertension. Which baseline studies are obtained?",
  [["Renal function, electrolytes, glucose, lipids and urinalysis",
    "Correct, with a urine albumin-to-creatinine ratio alongside the creatinine. The panel does three jobs at once: screens for secondary causes, measures organ damage, and establishes a baseline before drugs that alter potassium and renal function are started. Thyroid-stimulating hormone and a full blood count complete it."],
   ["Creatinine alone, with nothing further",
    "The panel is considerably broader, covering renal assessment, electrolytes, metabolic studies, "
    "thyroid screening and urinalysis."],
   ["Plasma free metanephrines in every patient",
    "Metanephrines are ordered when the history suggests pheochromocytoma rather than as a universal "
    "baseline study."],
   ["A chest radiograph and echocardiogram in every patient",
    "Neither is routine: chest radiography is specifically not indicated for uncomplicated "
    "hypertension, and echocardiography is reserved for defined indications."]], C(41)),

Q("Electrocardiography", IO,
  "A 60-year-old hypertensive man has an electrocardiogram that does not meet voltage criteria for left ventricular hypertrophy, but he is breathless on exertion and has a significant murmur. What is the most appropriate next step?",
  [["Proceed to echocardiography",
    "Correct. The voltage criteria are specific but NOT sensitive, so false negatives are common. Unexplained dyspnea and a significant murmur are both indications for echocardiography in their own right. A normal tracing does not exclude hypertrophy."],
   ["Conclude that hypertensive heart disease is excluded",
    "A normal electrocardiogram specifically does not exclude hypertensive heart disease, which is "
    "the practical consequence of poor sensitivity."],
   ["Repeat the electrocardiogram in six months",
    "Repeating an insensitive test does not answer the question that echocardiography would."],
   ["Order a chest radiograph to measure the cardiac size",
    "Radiography is appropriate when pulmonary edema or cardiomegaly is suspected, but it does not "
    "assess ventricular mass, geometry or function."]], C(43)),

Q("Fundoscopy", IO,
  "A 49-year-old newly diagnosed hypertensive patient has fundoscopy showing generalized arteriolar "
  "narrowing and arteriovenous nicking, with no hemorrhages or exudates. What does this tell you?",
  [["They reflect current and previous pressure",
    "Correct. Generalized narrowing and nicking record the accumulated burden, whereas focal "
    "narrowing, hemorrhages and exudates relate to CURRENT pressure only."],
   ["These changes reflect current blood pressure only",
    "Focal narrowing, hemorrhages and exudates are the findings tied to current pressure; these two "
    "relate to current and previous."],
   ["These findings indicate a hypertensive emergency",
    "Optic disc edema marks acute hypertensive injury; chronic arteriolar changes do not."],
   ["These findings carry no prognostic weight",
    "Hypertensive retinopathy predicts long-term stroke risk independently of the blood pressure "
    "level."]], C(31)),

Q("Fundoscopy", IO,
  "Why is fundoscopy performed in every newly diagnosed hypertensive patient?",
  [["It allows direct visualization of the microvasculature",
    "Correct, and the findings carry prognostic weight beyond the reading itself: retinopathy "
    "predicts long-term stroke risk, retinal arterial narrowing predicts future hypertension, and "
    "control can produce regression."],
   ["It distinguishes primary from secondary hypertension",
    "That distinction rests on clues in the history, examination and laboratory work. Fundoscopy "
    "assesses damage rather than cause."],
   ["It replaces the need for renal and cardiac assessment",
    "A normal fundus does not exclude injury elsewhere, so it supplements rather than replaces the "
    "other target organ assessments."],
   ["It determines which antihypertensive class to start",
    "Agent selection follows comorbidities and patient factors rather than retinal findings."]],
  C(31)),

Q("Definitions", IO,
  "A 58-year-old woman has a blood pressure of 224/126 with no headache, no visual change, no chest pain, a normal neurological examination and a normal creatinine. How should this be classified?",
  [["Severe asymptomatic hypertension",
    "Correct. An emergency is defined by acute hypertension-mediated ORGAN INJURY, not by crossing a numeric threshold. A very high pressure with no acute organ involvement is not an emergency, and that distinction decides how fast the pressure is brought down. It is not a hypertensive emergency."],
   ["A hypertensive emergency, because the systolic exceeds 220",
    "No absolute numeric cutoff defines an emergency; acute hypertension-mediated organ injury is what does."],
   ["Resistant hypertension",
    "Resistance means pressure above goal despite three complementary drugs at maximally tolerated "
    "doses, which is not what is described."],
   ["Hypertensive encephalopathy",
    "Encephalopathy would require confusion, seizures or a neurological deficit, and her examination "
    "is normal."]], C(26)),

Q("Hypertensive emergency", IO,
  "A 62-year-old man arrives with blood pressure 232/128, confusion and blurred vision. Over the "
  "first hour, how far should his mean arterial pressure be reduced?",
  [["By no more than about twenty to twenty-five percent",
    "Correct, targeting around 160/100 to 110 over two to six hours and gradual normalization over a "
    "day or two. Autoregulation has adapted to the higher pressure, so dropping it to a chronic goal "
    "acutely can cause ischemic stroke, myocardial injury or renal failure."],
   ["To below 130/80 within the first hour",
    "Reducing to the chronic goal within an hour risks precisely the ischemic injury the controlled "
    "approach exists to avoid."],
   ["By at least half, to remove the immediate danger",
    "Overly rapid reduction is specifically harmful; the first-hour limit is about a fifth to a "
    "quarter of the mean arterial pressure."],
   ["No reduction until imaging is complete",
    "Stabilization and controlled reduction begin promptly alongside the focused assessment."]],
  C(69)),

Q("Acute stroke", IO,
  "A 74-year-old woman presents with acute right hemiparesis and aphasia of two hours' duration. Her blood pressure is 196/104. How should her blood pressure be managed?",
  [["Follow the acute stroke protocol, not chronic targets",
    "Correct. Acute stroke is specifically excepted from the general emergency reduction approach, "
    "because driving the pressure to a chronic target can extend the ischemic injury."],
   ["Reduce the pressure to below 130/80 immediately",
    "Applying a chronic prevention target acutely is exactly what the caution warns against."],
   ["Reduce the mean arterial pressure by a quarter in an hour",
    "That is the general hypertensive emergency approach, and acute stroke follows a distinct "
    "protocol instead."],
   ["Leave the blood pressure entirely untreated",
    "A distinct protocol applies rather than no management at all, so the pressure is managed by different rules."]], C(27)),

Q("Aortic dissection", IO,
  "A 58-year-old hypertensive man has abrupt severe tearing chest pain radiating to his back, maximal at onset. His right arm pressure is 176/92 and his left is 138/78. A chest radiograph is reported as normal. What is the most appropriate next step?",
  [["Obtain immediate cross-sectional vascular imaging",
    "Correct. A normal chest radiograph does NOT exclude dissection, so a normal film must not end "
    "the workup. The pain that is maximal at onset and the asymmetric arm pressures both point to it, "
    "and surgical involvement is urgent."],
   ["Reassure him, since the chest radiograph is normal",
    "The radiograph may show a widened mediastinum but cannot rule the diagnosis out."],
   ["Obtain an echocardiogram to establish the diagnosis",
    "Echocardiography establishes coarctation; immediate cross-sectional vascular imaging is what is "
    "required here."],
   ["Delay imaging until the blood pressure is controlled",
    "Imaging is immediate, because the diagnosis determines both the pressure target and the "
    "operation."]], C(29)),

Q("Aortic dissection", IO,
  "A 61-year-old with abrupt severe interscapular pain has symmetric, normal-volume pulses in all "
  "four limbs. What follows?",
  [["Normal pulses do not exclude dissection",
    "Correct. Absent pulse findings specifically do not exclude the diagnosis, which is why a normal pulse examination must not close the question. Imaging is still driven by the clinical suspicion."],
   ["Dissection is excluded and another cause should be sought",
    "Symmetric pulses do not exclude it; the clinical suspicion still drives imaging."],
   ["A normal chest radiograph would then exclude it",
    "A normal chest radiograph does not exclude dissection either, so neither finding can close the question."],
   ["An aortic regurgitation murmur would be required to proceed",
    "A murmur is one supporting finding among several, not a prerequisite for imaging."]], C(29)),
]
