# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- Antihypertensives (Lecture 6), topic 2: calcium
channel blockers.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

SOURCE. Antihypertensives.pptx slides 31-54 (and 75 for the beta blocker
combination). The spine is the one distinction the recording repeated "for
emphasis" and tied to two explicit test-question statements: ONLY the
non-dihydropyridines (diltiazem, verapamil) act on the heart -- rate,
contractility, AV conduction -- so only they treat supraventricular tachycardia,
and their adverse effects and contraindications follow from it. Dihydropyridines
act on vessels, so their problems are reflex tachycardia and edema.

The second emphasis is the CYP3A4 pair: non-dihydropyridines INHIBIT CYP3A4 and
P-glycoprotein (statins, digoxin); dihydropyridines are only substrates. This
links forward to the Lipids lecture's CYP3A4 statins.

SCOPE CAPS: the comparison table is asked for its pattern, never its plus
counts ("I don't care" which one has three pluses). No doses. Where the
recording said dihydropyridines do "nothing" to the heart, the slide's "0/+"
wins -- no key says zero effect on contractility. Where the recording said a
beta blocker with a non-dihydropyridine "should not be used together", the
slide's "use lower doses of each" wins.
"""

D = "Antihypertensives.pptx"
IO_CLASS = "Identify antihypertensive drug classes and commonly prescribed antihypertensive drugs"
IO_MOA = "Describe the molecular mechanism of action of antihypertensive drugs"
IO_IND = "Identify indications for commonly used antihypertensive drugs"
IO_ADME = "Describe absorption, distribution, metabolism, and excretion of antihypertensive drugs"
IO_TOX = "Summarize side effects and toxic manifestations of antihypertensive drugs"
IO_AE = "Describe adverse effects of antihypertensive drugs"
IO_CONTRA = "Identify contraindications for antihypertensive drugs"
IO_INTER = "Discuss potential drug-drug, drug-food, and drug-herb interactions with antihypertensive drugs"
IO_PROT = "List commonly used protocols and patient monitoring for antihypertensive drugs"
IO_EDU = "Outline appropriate patient education for antihypertensive drugs"

QUESTIONS = [

# ---- class and the DHP / non-DHP split ------------------------------------
{"topic": "Non-dihydropyridines", "io": IO_CLASS, "slot": "class",
 "q": "Which pair of calcium channel blockers lowers heart rate and slows atrioventricular conduction?",
 "opts": [
  ["Diltiazem and verapamil", "Correct. Only the non-dihydropyridines strongly suppress the sinoatrial and atrioventricular nodes; this one distinction drives their indications, adverse effects and contraindications."],
  ["Amlodipine and nifedipine", "These are dihydropyridines, which act mainly on vascular smooth muscle and have no effect on atrioventricular conduction."],
  ["Felodipine and isradipine", "These are dihydropyridines approved for hypertension; they dilate arteries rather than slowing the heart. Diltiazem and verapamil slow it."],
  ["Nicardipine and nimodipine", "Both are dihydropyridines: nicardipine is the intravenous one and nimodipine is for subarachnoid hemorrhage. Neither slows atrioventricular conduction."]],
 "c": 0, "cite": D + ", Slide 42"},

{"topic": "Dihydropyridines", "io": IO_CLASS, "slot": "class",
 "q": "Which of these drugs is a dihydropyridine calcium channel blocker?",
 "opts": [
  ["Felodipine", "Correct. The -dipine suffix marks a dihydropyridine; felodipine, isradipine and nisoldipine are approved for hypertension."],
  ["Diltiazem", "Diltiazem is a non-dihydropyridine, one of the two that act on the sinoatrial and atrioventricular nodes. The -dipine suffix marks the dihydropyridines."],
  ["Verapamil", "Verapamil is the other non-dihydropyridine, with the strongest cardiac suppression. Dihydropyridines carry the -dipine suffix, like felodipine."],
  ["Fosinopril", "Fosinopril is an ACE (angiotensin-converting enzyme) inhibitor, as its -pril suffix shows. Felodipine is the dihydropyridine here."]],
 "c": 0, "cite": D + ", Slide 49"},

{"topic": "Non-dihydropyridines", "io": IO_MOA, "slot": "mechanism",
 "q": "Why do non-dihydropyridines slow atrioventricular conduction while dihydropyridines do not?",
 "opts": [
  ["They also delay slow-channel recovery", "Correct. Both reduce the slow inward calcium current, but only the non-dihydropyridines also decrease the channel's rate of recovery, which slows atrioventricular conduction."],
  ["They block T-type channels only", "T-type channels handle pacemaker depolarization and are not how these drugs differ. The difference is that non-dihydropyridines also delay slow-channel recovery."],
  ["They also block sodium channels", "Sodium channel blockade is not described for either group. What separates them is whether the drug delays recovery of the slow calcium channel."],
  ["They also block beta-1 receptors", "Neither group blocks beta receptors. Non-dihydropyridines slow conduction because they delay recovery of the slow calcium channel as well as reducing its current."]],
 "c": 0, "cite": D + ", Slide 40"},

{"topic": "Calcium channel blockers", "io": IO_MOA, "slot": "mechanism",
 "q": "Why are arterial vessels 3 to 10 times more sensitive to calcium channel blockers than myocardial cells?",
 "opts": [
  ["Arteries rely on outside calcium entry", "Correct. Arterial smooth muscle depends on exogenous calcium through L-type channels, whereas myocytes also draw on a recirculating store in the sarcoplasmic reticulum."],
  ["Myocytes lack L-type calcium channels", "Myocytes do have L-type channels; they supply the trigger calcium. The difference is that myocytes also recycle calcium from the sarcoplasmic reticulum."],
  ["Arteries store more internal calcium", "It is the reverse: myocytes have the recirculating internal store, while arteries depend on calcium entering through L-type channels."],
  ["Arteries carry more beta-2 receptors", "Beta receptors are not how calcium channel blockers act. The sensitivity comes from arteries depending on calcium entry through L-type channels."]],
 "c": 0, "cite": D + ", Slide 39"},

{"topic": "Calcium channel blockers", "io": IO_MOA, "slot": "mechanism",
 "q": "At therapeutic doses, how do calcium channel blockers affect preload and afterload?",
 "opts": [
  ["Lower afterload, no change in preload", "Correct. At therapeutic doses they do not reduce venous tone, so they decrease afterload without affecting preload."],
  ["Lower preload, no change in afterload", "The reverse. They are ineffective at decreasing venous tone, so preload is unaffected, while arterial dilation lowers afterload."],
  ["Lower preload and afterload equally", "Veins are not dilated at therapeutic doses, so only afterload falls. Nitroprusside is the drug that acts on both veins and arterioles."],
  ["Raise preload and lower afterload", "Preload does not rise; it is simply unaffected because venous tone is not reduced. Afterload falls through arterial dilation."]],
 "c": 0, "cite": D + ", Slide 38"},

{"topic": "Calcium channel blockers", "io": IO_IND, "slot": "indication",
 "q": "Which is a listed therapeutic use of calcium channel blockers as a class?",
 "opts": [
  ["Migraine prophylaxis", "Correct. Class uses are angina, hypertension, supraventricular arrhythmias, diastolic heart failure, cerebral ischemia and migraine prophylaxis."],
  ["Benign prostatic hyperplasia", "Prostatic hyperplasia is treated with alpha-1 blockers such as terazosin, doxazosin and tamsulosin, not calcium channel blockers."],
  ["Hypertensive crisis by infusion", "The crisis agent given by intravenous infusion is nitroprusside. Calcium channel blocker uses include angina, arrhythmias and migraine prophylaxis."],
  ["Benign essential tremor", "Essential tremor is a beta blocker indication, from blocking beta-2 receptors on skeletal muscle. Calcium channel blockers are used for migraine prophylaxis."]],
 "c": 0, "cite": D + ", Slide 41"},

# ---- non-DHP indications -------------------------------------------------------
{"topic": "Non-dihydropyridines", "io": IO_IND, "slot": "drug choice",
 "q": "A patient has paroxysmal supraventricular tachycardia. Which calcium channel blocker is appropriate?",
 "opts": [
  ["Verapamil", "Correct. Supraventricular tachycardia -- atrial fibrillation or flutter and paroxysmal supraventricular tachycardia -- is an approved indication for the non-dihydropyridines."],
  ["Amlodipine", "Amlodipine is a dihydropyridine approved for angina and hypertension. It does not slow atrioventricular conduction, so it cannot treat supraventricular tachycardia."],
  ["Nifedipine", "Nifedipine is a dihydropyridine: vasodilation with reflex tachycardia, not nodal slowing. Supraventricular tachycardia needs verapamil or diltiazem."],
  ["Felodipine", "Felodipine is a dihydropyridine approved only for hypertension. Only the non-dihydropyridines act on the nodes to treat supraventricular tachycardia."]],
 "c": 0, "cite": D + ", Slide 44"},

{"topic": "Non-dihydropyridines", "io": IO_IND, "slot": "drug choice",
 "q": "Which calcium channel blocker would be used to slow the ventricular rate in atrial fibrillation?",
 "opts": [
  ["Diltiazem", "Correct. Diltiazem strongly suppresses the sinoatrial node and atrioventricular conduction; atrial fibrillation or flutter is an approved non-dihydropyridine indication."],
  ["Nicardipine", "Nicardipine is the intravenous dihydropyridine; it lowers blood pressure but has no effect on atrioventricular conduction, so it cannot control the rate."],
  ["Nimodipine", "Nimodipine is the dihydropyridine approved for subarachnoid hemorrhage and does not slow atrioventricular conduction."],
  ["Isradipine", "Isradipine is a dihydropyridine approved for hypertension. Rate control needs a non-dihydropyridine such as diltiazem."]],
 "c": 0, "cite": D + ", Slide 44"},

{"topic": "Non-dihydropyridines", "io": IO_IND, "slot": "indication",
 "q": "Which approved indication belongs to verapamil but not to amlodipine?",
 "opts": [
  ["Supraventricular tachycardia", "Correct. Both treat angina and hypertension; only the non-dihydropyridines slow the atrioventricular node enough to treat supraventricular tachycardia."],
  ["Chronic stable angina", "Angina is approved for both: verapamil and amlodipine (with nifedipine and nicardipine) are all used for it. The difference is supraventricular tachycardia."],
  ["Essential hypertension", "Hypertension is an approved indication for both drugs. Only verapamil adds supraventricular tachycardia."],
  ["Subarachnoid hemorrhage", "Subarachnoid hemorrhage is nimodipine's indication, not verapamil's. Verapamil's extra indication is supraventricular tachycardia."]],
 "c": 0, "cite": D + ", Slide 44"},

# ---- DHP agents -------------------------------------------------------------
{"topic": "Dihydropyridines", "io": IO_IND, "slot": "indication",
 "q": "Which dihydropyridine is approved for subarachnoid hemorrhage?",
 "opts": [
  ["Nimodipine", "Correct. Nimodipine's approved indication is subarachnoid hemorrhage, unlike the other dihydropyridines, which are approved for hypertension with or without angina."],
  ["Nifedipine", "Nifedipine is approved for angina and hypertension. The subarachnoid hemorrhage agent is nimodipine."],
  ["Nicardipine", "Nicardipine is approved for angina and hypertension and is the one available intravenously. Nimodipine is the subarachnoid hemorrhage agent."],
  ["Nisoldipine", "Nisoldipine is approved for hypertension only. Nimodipine is the dihydropyridine used for subarachnoid hemorrhage."]],
 "c": 0, "cite": D + ", Slide 49"},

{"topic": "Dihydropyridines", "io": IO_ADME, "slot": "class",
 "q": "Most dihydropyridines are taken by mouth only. Which one is available intravenously?",
 "opts": [
  ["Nicardipine", "Correct. The dihydropyridines are oral only, except nicardipine, which is available intravenously; it is approved for angina and hypertension."],
  ["Amlodipine", "Amlodipine is an oral dihydropyridine for angina and hypertension. The intravenous exception is nicardipine."],
  ["Felodipine", "Felodipine is oral only and approved for hypertension. Nicardipine is the dihydropyridine available intravenously."],
  ["Nisoldipine", "Nisoldipine is taken by mouth for hypertension. The only intravenous dihydropyridine is nicardipine."]],
 "c": 0, "cite": D + ", Slide 49"},

# ---- adverse effects -------------------------------------------------------
{"topic": "Dihydropyridines", "io": IO_AE, "slot": "adverse effect",
 "q": "A patient started on nifedipine reports a pounding, rapid heartbeat. What explains it?",
 "opts": [
  ["Reflex tachycardia from vasodilation", "Correct. Strong arterial dilation drops resistance abruptly and the heart compensates by speeding up; rebound tachycardia is a listed dihydropyridine effect."],
  ["Direct stimulation of the sinus node", "Dihydropyridines do not stimulate the sinoatrial node; the fast rate is a reflex response to the fall in vascular resistance."],
  ["Blockade of cardiac beta-1 receptors", "Beta-1 blockade slows the heart rather than speeding it, and nifedipine does not block beta receptors. This is reflex tachycardia from vasodilation."],
  ["Hyperkalemia from renal effects", "Hyperkalemia belongs to ACE inhibitors and angiotensin receptor blockers. A rapid heartbeat on nifedipine is reflex tachycardia."]],
 "c": 0, "cite": D + ", Slide 51"},

{"topic": "Dihydropyridines", "io": IO_AE, "slot": "adverse effect",
 "q": "A patient on amlodipine develops ankle swelling. What is the mechanism?",
 "opts": [
  ["Peripheral vasodilation", "Correct. Peripheral edema is listed under the peripheral vasodilation effects of dihydropyridines, together with dyspnea, wheezing and rebound tachycardia."],
  ["Heart failure from negative inotropy", "Dihydropyridines have little effect on contractility (0 to +). Worsening heart failure from negative inotropy is a non-dihydropyridine problem."],
  ["Sodium retention by aldosterone", "Aldosterone-driven retention is not the explanation offered for dihydropyridine edema; it is a consequence of peripheral vasodilation."],
  ["Low albumin from liver injury", "Dihydropyridine edema is not explained by liver injury or albumin loss. It is listed as a peripheral vasodilation effect."]],
 "c": 0, "cite": D + ", Slide 51"},

{"topic": "Non-dihydropyridines", "io": IO_TOX, "slot": "adverse effect",
 "q": "An older patient on verapamil has a heart rate of 48 beats per minute. Which other adverse effects follow from the same cardiac action?",
 "opts": [
  ["First-degree block and worse heart failure", "Correct. Negative inotropic and nodal effects produce first-degree atrioventricular block, bradycardia, and exacerbation of heart failure or pulmonary edema."],
  ["Reflex tachycardia and palpitations", "Reflex tachycardia is a dihydropyridine effect. Verapamil suppresses the nodes and contractility instead, causing bradycardia and heart block."],
  ["Hypertrichosis and pericardial effusion", "Hypertrichosis belongs to minoxidil. Verapamil's cardiac action causes atrioventricular block, bradycardia and worsening heart failure."],
  ["Dry cough and angioedema", "Cough and angioedema are bradykinin effects of ACE inhibitors, not consequences of verapamil's cardiac suppression."]],
 "c": 0, "cite": D + ", Slide 45"},

{"topic": "Non-dihydropyridines", "io": IO_EDU, "slot": "education",
 "q": "A 72-year-old starting verapamil asks which change in bowel habit to watch for. What should she be told?",
 "opts": [
  ["Constipation", "Correct. Constipation is among the listed gastrointestinal effects of non-dihydropyridines, so bowel habits are worth asking about at follow-up."],
  ["Black stools", "Stools that may turn black are listed for hydralazine, not verapamil. Verapamil's bowel effect to warn about is constipation."],
  ["Oily, fatty stools", "Fatty stools are not a verapamil effect; the listed gastrointestinal problem to watch for is constipation."],
  ["Bloody diarrhea", "Bloody diarrhea is not a listed effect. The non-dihydropyridine bowel effect patients should know about is constipation."]],
 "c": 0, "cite": D + ", Slide 45"},

{"topic": "Calcium channel blockers", "io": IO_AE, "slot": "adverse effect",
 "q": "Which adverse effect is listed for both diltiazem and amlodipine?",
 "opts": [
  ["Gingival hyperplasia", "Correct. Gingival hyperplasia appears in the adverse effect lists of both the non-dihydropyridines and the dihydropyridines."],
  ["First-degree heart block", "Atrioventricular block follows from non-dihydropyridine nodal suppression. Dihydropyridines such as amlodipine have no effect on atrioventricular conduction."],
  ["Dry cough", "Dry cough is an ACE inhibitor effect from bradykinin, not a calcium channel blocker effect. Gingival hyperplasia is the shared one."],
  ["Hypertrichosis", "Hypertrichosis is characteristic of minoxidil. The effect shared by diltiazem and amlodipine is gingival hyperplasia."]],
 "c": 0, "cite": D + ", Slide 51"},

# ---- contraindications --------------------------------------------------------
{"topic": "Non-dihydropyridines", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which condition is a contraindication to diltiazem?",
 "opts": [
  ["Advanced heart block", "Correct. Advanced heart block and hypotension are contraindications; heart failure, liver disease and gastroesophageal reflux disease are relative contraindications."],
  ["Supraventricular tachycardia", "Supraventricular tachycardia is an approved indication for diltiazem, not a contraindication; nodal slowing is what treats it."],
  ["Chronic stable angina", "Angina is an approved indication for diltiazem. The contraindication is advanced heart block, which its nodal suppression would worsen."],
  ["Uncomplicated hypertension", "Hypertension is an approved indication. Diltiazem is contraindicated in advanced heart block and hypotension."]],
 "c": 0, "cite": D + ", Slide 46"},

{"topic": "Non-dihydropyridines", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which is listed as a relative contraindication to non-dihydropyridine calcium channel blockers?",
 "opts": [
  ["Gastroesophageal reflux disease", "Correct. Heart failure, liver disease and gastroesophageal reflux disease are relative contraindications; the drugs relax smooth muscle, including the lower esophageal sphincter."],
  ["Asthma with frequent wheeze", "Asthma is a concern with non-selective beta blockers because of bronchospasm; it is not listed for non-dihydropyridines, whose relative list includes reflux disease."],
  ["Gout with raised uric acid", "Gout is a relative contraindication to niacin because it raises uric acid; the non-dihydropyridine relative list is heart failure, liver disease and reflux disease."],
  ["Hypokalemia on a diuretic", "Low potassium is not a listed contraindication for these drugs. The relative contraindications are heart failure, liver disease and reflux disease."]],
 "c": 0, "cite": D + ", Slide 46"},

{"topic": "Dihydropyridines", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which condition is a contraindication to a dihydropyridine calcium channel blocker?",
 "opts": [
  ["Severe aortic stenosis", "Correct. Severe aortic stenosis is a contraindication, as are unstable angina or recent myocardial infarction when an immediate-release formulation would be used."],
  ["Chronic stable angina", "Stable angina is an approved indication for amlodipine, nifedipine and nicardipine, not a contraindication."],
  ["Essential hypertension", "Hypertension is the main indication for dihydropyridines. The contraindication is severe aortic stenosis."],
  ["First-degree heart block", "Dihydropyridines have no effect on atrioventricular conduction, so heart block is a problem for diltiazem and verapamil rather than for them."]],
 "c": 0, "cite": D + ", Slide 52"},

{"topic": "Dihydropyridines", "io": IO_CONTRA, "slot": "contraindication",
 "q": "A patient was admitted last week with unstable angina. Which calcium channel blocker formulation should be avoided?",
 "opts": [
  ["Immediate-release dihydropyridine", "Correct. Unstable angina or recent myocardial infarction contraindicates immediate-release dihydropyridines, and short-acting formulations are to be avoided in general."],
  ["Extended-release non-dihydropyridine", "The listed contraindication in unstable angina or recent infarction is the immediate-release dihydropyridine formulation, not an extended-release non-dihydropyridine."],
  ["Intravenous non-dihydropyridine", "Intravenous diltiazem or verapamil is not the formulation named for this situation; immediate-release dihydropyridines are."],
  ["Any oral non-dihydropyridine", "The unstable angina contraindication is written for immediate-release dihydropyridines, whose abrupt vasodilation provokes reflex tachycardia."]],
 "c": 0, "cite": D + ", Slide 52"},

# ---- interactions (the CYP3A4 pair) ------------------------------------------
{"topic": "Non-dihydropyridines", "io": IO_INTER, "slot": "interaction",
 "q": "A patient on simvastatin is started on verapamil and develops muscle aches. By what mechanism does verapamil raise simvastatin levels?",
 "opts": [
  ["CYP3A4 inhibition", "Correct. Non-dihydropyridines inhibit CYP3A4, raising atorvastatin, lovastatin and simvastatin, as well as carbamazepine, propranolol, tacrolimus and cyclosporine."],
  ["CYP3A4 induction", "Induction would lower simvastatin levels. Verapamil is an inhibitor of CYP3A4, which is why the statin accumulates."],
  ["P-glycoprotein induction", "Verapamil inhibits P-glycoprotein (raising digoxin); it does not induce it. The statin interaction is through CYP3A4 inhibition."],
  ["Protein binding displacement", "Displacement from proteins is not the listed mechanism. Non-dihydropyridines raise these statins by inhibiting CYP3A4."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": "Non-dihydropyridines", "io": IO_INTER, "slot": "interaction",
 "q": "A patient on diltiazem needs a statin. Which statin's levels would diltiazem's CYP3A4 inhibition raise?",
 "opts": [
  ["Atorvastatin", "Correct. The statins raised by non-dihydropyridine CYP3A4 inhibition are atorvastatin, lovastatin and simvastatin."],
  ["Rosuvastatin", "Rosuvastatin undergoes minimal CYP metabolism, so it is not on the list of statins raised by non-dihydropyridines."],
  ["Pravastatin", "Pravastatin is metabolized by enzymatic and nonenzymatic routes rather than CYP3A4, so diltiazem's inhibition does not raise it the same way."],
  ["Pitavastatin", "Pitavastatin is cleared by glucuronidation rather than CYP3A4. The CYP3A4 statins are atorvastatin, lovastatin and simvastatin."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": "Non-dihydropyridines", "io": IO_INTER, "slot": "interaction",
 "q": "How does verapamil raise digoxin levels?",
 "opts": [
  ["P-glycoprotein inhibition", "Correct. Non-dihydropyridines inhibit P-glycoprotein, raising digoxin, tacrolimus, cyclosporine and carbamazepine; digoxin also adds a pharmacodynamic interaction."],
  ["CYP3A4 induction", "Verapamil inhibits rather than induces CYP3A4, and digoxin is listed under P-glycoprotein. Inhibition of that transporter is the route."],
  ["Reduced renal blood flow", "Changes in renal blood flow are not the listed mechanism. Verapamil raises digoxin by inhibiting P-glycoprotein."],
  ["Binding digoxin in the gut", "Binding in the gut lowers absorption, as bile acid sequestrants do. Verapamil raises digoxin by inhibiting P-glycoprotein."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": "Dihydropyridines", "io": IO_ADME, "slot": "interaction",
 "q": "How do dihydropyridines differ from non-dihydropyridines with respect to CYP3A4?",
 "opts": [
  ["Substrates, not inhibitors", "Correct. CYP3A4 inhibitors lengthen the half-life of both groups, but only the non-dihydropyridines inhibit CYP3A4 and alter other drugs through it."],
  ["Stronger CYP3A4 inhibitors", "It is the non-dihydropyridines that inhibit CYP3A4. Dihydropyridines affect other drugs only pharmacodynamically."],
  ["Inducers of CYP3A4", "Dihydropyridines are not described as inducers. They are substrates, so CYP3A4 inhibitors increase their half-life."],
  ["Unaffected by CYP3A4", "They are affected: CYP3A4 inhibitors increase the dihydropyridine half-life. What they lack is the non-dihydropyridines' inhibitory effect."]],
 "c": 0, "cite": D + ", Slide 54"},

{"topic": "Non-dihydropyridines", "io": IO_INTER, "slot": "interaction",
 "q": "A patient on diltiazem is started on amiodarone. What pharmacodynamic risk does the combination carry?",
 "opts": [
  ["Excess slowing of the heart", "Correct. Amiodarone with a non-dihydropyridine can slow the sinus rate or worsen atrioventricular block; digoxin and beta blockers are listed alongside it."],
  ["Reflex tachycardia", "Reflex tachycardia comes from dihydropyridine vasodilation. Amiodarone added to diltiazem slows the heart further rather than speeding it."],
  ["Hyperkalemia", "Potassium is not the concern of this pair. The risk is additive nodal suppression: a slower sinus rate or worsened atrioventricular block."],
  ["Loss of diltiazem effect", "The effects add rather than cancel. The combination slows the sinus rate or worsens atrioventricular block."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": "Non-dihydropyridines", "io": IO_INTER, "slot": "interaction",
 "q": "What is advised when verapamil is combined with a beta blocker?",
 "opts": [
  ["Use lower doses of each", "Correct. The two are synergistic in lowering blood pressure, heart rate and contractility, so lower doses of each are used when they are combined."],
  ["Use higher doses of each", "Their effects add, so higher doses would compound the fall in heart rate and contractility. Lower doses of each are advised."],
  ["Separate doses by 4 hours", "Timing separation is the rule for bile acid sequestrants. For this pharmacodynamic synergy the advice is lower doses of each."],
  ["Give only intravenously", "The route does not solve additive cardiac depression. The advice for the combination is lower doses of each."]],
 "c": 0, "cite": D + ", Slide 75"},

# ---- added for depth on the most-taught class --------------------------------------
{"topic": "Calcium channel blockers", "io": IO_MOA, "slot": "mechanism",
 "q": "Which calcium channel type do these drugs block in vascular smooth muscle, cardiac myocytes and nodal tissue?",
 "opts": [
  ["L-type channels", "Correct. L-type channels sit in vascular smooth muscle, cardiac myocytes and the sinoatrial and atrioventricular nodes, and all three drug groups bind them."],
  ["T-type channels", "T-type channels mediate pacemaker depolarization and are the mibefradil target, not the channel these drugs block across all three tissues."],
  ["Ryanodine receptors", "Ryanodine receptors release calcium from the sarcoplasmic reticulum; calcium channel blockers act on the L-type channel in the cell membrane."],
  ["IP3 receptors", "Inositol triphosphate (IP3) receptors modulate sarcoplasmic reticulum calcium release; the drug target is the L-type membrane channel."]],
 "c": 0, "cite": D + ", Slide 33"},

{"topic": "Dihydropyridines", "io": IO_CONTRA, "slot": "drug choice",
 "q": "A patient with hypertension also has heart failure. Which calcium channel blocker avoids the relative contraindication in heart failure?",
 "opts": [
  ["Amlodipine", "Correct. Heart failure is a relative contraindication to the non-dihydropyridines because they suppress contractility; amlodipine, a dihydropyridine approved for hypertension, has little effect on contractility."],
  ["Verapamil", "Verapamil has the strongest suppression of contractility and can exacerbate heart failure; heart failure is a relative contraindication to it."],
  ["Diltiazem", "Diltiazem is a non-dihydropyridine; heart failure is a relative contraindication because of its negative inotropic effect."],
  ["Nimodipine", "Nimodipine is a dihydropyridine, but its approved indication is subarachnoid hemorrhage, not hypertension. Amlodipine is the hypertension choice."]],
 "c": 0, "cite": D + ", Slide 46"},

{"topic": "Non-dihydropyridines", "io": IO_AE, "slot": "adverse effect",
 "q": "Which laboratory change is listed among the adverse effects of non-dihydropyridines?",
 "opts": [
  ["Raised liver function tests", "Correct. Elevations in liver function tests are listed, and liver disease is a relative contraindication to diltiazem and verapamil."],
  ["Raised serum potassium", "Raised potassium belongs to ACE (angiotensin-converting enzyme) inhibitors and angiotensin receptor blockers, not calcium channel blockers."],
  ["Raised serum uric acid", "Raised uric acid is a niacin effect. The listed laboratory change for non-dihydropyridines is elevated liver function tests."],
  ["Raised blood glucose", "Raised glucose is listed for clonidine (and for beta blockers in type 2 diabetes), not for non-dihydropyridines, which raise liver function tests."]],
 "c": 0, "cite": D + ", Slide 45"},

{"topic": "Non-dihydropyridines", "io": IO_INTER, "slot": "interaction",
 "q": "A transplant recipient taking tacrolimus is started on diltiazem. What is expected to happen to the tacrolimus level?",
 "opts": [
  ["It rises", "Correct. Non-dihydropyridines inhibit CYP3A4 and P-glycoprotein, and tacrolimus and cyclosporine are on both lists, so their levels rise."],
  ["It falls", "The direction is the reverse: diltiazem inhibits the CYP3A4 and P-glycoprotein routes that clear tacrolimus, so the level rises."],
  ["It is unchanged", "Tacrolimus is on the CYP3A4 and P-glycoprotein lists for non-dihydropyridines, so its level is not expected to stay unchanged; it rises."],
  ["It becomes unmeasurable", "Nothing makes tacrolimus unmeasurable here. Diltiazem's CYP3A4 and P-glycoprotein inhibition raises it."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": "Non-dihydropyridines", "io": IO_ADME, "slot": "interaction",
 "q": "What effect does adding a CYP3A4 inhibitor have on a non-dihydropyridine such as verapamil?",
 "opts": [
  ["It lengthens its half-life", "Correct. CYP3A4 inhibitors increase the half-life of non-dihydropyridines, and of dihydropyridines as well."],
  ["It shortens its half-life", "Inhibiting the enzyme that clears the drug prolongs it rather than shortening it. CYP3A4 inhibitors increase the half-life."],
  ["It blocks its absorption", "Absorption is not the listed effect. CYP3A4 inhibitors increase the half-life of non-dihydropyridines."],
  ["It has no effect on it", "There is a listed effect: CYP3A4 inhibitors increase the non-dihydropyridine half-life."]],
 "c": 0, "cite": D + ", Slide 48"},

{"topic": "Dihydropyridines", "io": IO_AE, "slot": "adverse effect",
 "q": "Which calcium channel blocker is more likely than diltiazem to cause gynecomastia?",
 "opts": [
  ["Nifedipine", "Correct. Gynecomastia is listed with the comparison that nifedipine exceeds diltiazem; gingival hyperplasia is shared across the class."],
  ["Verapamil", "Verapamil is not the agent named in the gynecomastia comparison, which lists nifedipine as more likely than diltiazem."],
  ["Nimodipine", "Nimodipine is the subarachnoid hemorrhage agent and is not named in the gynecomastia comparison; nifedipine is."],
  ["Nicardipine", "Nicardipine is the intravenous dihydropyridine; the gynecomastia comparison names nifedipine over diltiazem."]],
 "c": 0, "cite": D + ", Slide 51"},
]
