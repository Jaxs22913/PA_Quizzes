# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- Myocardial Ischemia Drugs (Lecture 8), topic 1: antianginals.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

SOURCE. Myocardial Ischemia Drugs.pptx slides 3-39: the oxygen supply-and-demand frame, the types of angina,
beta blockers, calcium channel blockers, short- and long-acting nitrates, the nitrate-free interval, the
comorbidity table, the add-on drugs (angiotensin-converting enzyme inhibitors, aspirin, clopidogrel) and the
variant-angina rule. The picture-only slides (5, 15, 16, 20, 21, 25, 26, 34) are read from tools/pharm_e2/ocr.json.

EMPHASIS (weight only): none yet -- the recording is not transcribed. Weighted by Dr. McInnis's rule instead:
indications, patient education, adverse effects, contraindications and drug choice outnumber mechanism and
physiology, and the pool asks what unites or separates the three classes before it asks about a single agent.

DECK CONFLICTS AVOIDED (truth wins; none of these is keyed):
  * slide 13 "aspirin, clopidogrel increase coronary blood flow" is not asked, and no distractor says aspirin
    fails to dilate the coronary arteries.
  * slide 34 "prior myocardial infarction: avoid calcium channel blockers" and the diabetes row are contested; only
    the uncontested cells are keyed (beta blocker first line after infarction, amlodipine for decreased left
    ventricular function, dihydropyridine first line with bradycardia or atrioventricular block, non-selective beta
    blockers avoided in asthma).
  * slide 22 "non-dihydropyridine for initial therapy, dihydropyridine only with a beta blocker" is contested
    (amlodipine is a reasonable first calcium channel blocker); the keyed facts are the uncontroversial ones: avoid
    short-acting nifedipine, caution with a non-dihydropyridine plus a beta blocker, amlodipine added to a beta
    blocker, amlodipine for decreased left ventricular function.
  * slide 28 "replace tablets 3-6 months after opening": current labeling keeps tablets potent in the original
    container until the expiration date, so the replacement interval is not keyed.
  * slide 37's "30% reduction", slide 7's stenosis percentages and the ejection-fraction figure on slide 23 are
    numbers; none is a key.

SCOPE CAPS: no doses (no ointment inches, no tablet strengths); the five-minute nitroglycerin instruction is asked
as an ACTION (call emergency services), never as the number; no risk-factor age arithmetic; slides 40-68 belong to
the acute coronary syndrome pool.
"""

D = "Myocardial Ischemia Drugs.pptx"
IO_CLASS = "Identify drug classes and commonly prescribed drugs used to treat myocardial ischemia"
IO_MOA = "Describe the molecular mechanism of action of drugs used to treat myocardial ischemia"
IO_IND = "Identify indications for drugs used to treat myocardial ischemia"
IO_ADME = "Describe absorption, distribution, metabolism, and excretion of drugs used to treat myocardial ischemia"
IO_TOX = "Summarize side effects and toxic manifestations of drugs used to treat myocardial ischemia"
IO_AE = "Describe adverse effects of drugs used to treat myocardial ischemia"
IO_CONTRA = "Identify contraindications for drugs used to treat myocardial ischemia"
IO_INTER = "Discuss potential drug-drug, drug-food, and drug-herb interactions with drugs used to treat myocardial ischemia"
IO_PROT = "List commonly used protocols and patient monitoring for myocardial ischemia drug therapy"
IO_EDU = "Outline appropriate patient education for drugs used to treat myocardial ischemia"

QUESTIONS = [

# ---- supply and demand -----------------------------------------------------------
{"topic": "Supply and demand", "io": IO_MOA, "slot": "physiology",
 "q": "Which three factors set myocardial oxygen demand?",
 "opts": [
  ["Heart rate, contractility, and wall tension", "Correct. Demand rises with a faster heart rate, stronger contraction and greater systolic wall tension; wall tension reflects ventricular volume and pressure (preload and afterload)."],
  ["Arterial oxygen pressure, hemoglobin, and coronary flow", "Those set oxygen supply, not demand: arterial oxygen pressure, hemoglobin concentration and coronary flow and distribution decide how much oxygen arrives."],
  ["Heart rate, hemoglobin level, and coronary flow", "This mixes the two sides. Hemoglobin and coronary flow govern supply; only heart rate, contractility and wall tension set demand."],
  ["Contractility, oxygen extraction, and coronary flow", "Oxygen extraction and coronary flow belong to supply. Demand is set by heart rate, contractility and systolic wall tension."]],
 "c": 0, "cite": D + ", Slide 6"},

{"topic": "Supply and demand", "io": IO_MOA, "slot": "mechanism",
 "q": "How do beta blockers directly change myocardial oxygen supply?",
 "opts": [
  ["They have no effect on supply", "Correct. Beta blockers act on the demand side, lowering heart rate and contractility; they do not dilate the coronary arteries, so other antianginals are needed to raise supply."],
  ["They dilate the coronary arteries", "Coronary dilation is a nitrate effect (calcium channel blockers also dilate). Beta blockers leave oxygen supply unchanged and only lower demand."],
  ["They relieve coronary vasospasm", "Relief of vasospasm belongs to calcium channel blockers and nitrates; beta blockers leave supply unchanged and only lower demand; they may worsen vasospastic angina."],
  ["They dilate areas of fixed stenosis", "Mild dilation at fixed stenoses is a calcium channel blocker effect. Beta blockers do not change coronary flow; they lower demand."]],
 "c": 0, "cite": D + ", Slide 16"},

{"topic": "Supply and demand", "io": IO_MOA, "slot": "mechanism",
 "q": "Which action of calcium channel blockers improves myocardial oxygen supply?",
 "opts": [
  ["Relief of coronary vasospasm", "Correct. Calcium channel blockers relieve vasospasm and mildly dilate areas of fixed stenosis, raising supply, and they also lower demand."],
  ["Stabilizing atherosclerotic plaque", "Plaque stabilization is a vasculoprotective effect of drugs such as statins; calcium channel blockers raise supply by relieving vasospasm."],
  ["Blocking platelet aggregation", "Blocking platelet aggregation is the antiplatelet effect of aspirin and clopidogrel, not a calcium channel blocker action."],
  ["Reducing ventricular volume", "Lower ventricular volume reduces wall tension, a demand-side effect (strongest with nitrates). The supply effect of these drugs is relief of vasospasm."]],
 "c": 0, "cite": D + ", Slide 20"},

{"topic": "Supply and demand", "io": IO_MOA, "slot": "physiology",
 "q": "Which calcium channel blocker typically raises heart rate?",
 "opts": [
  ["Nifedipine", "Correct. Nifedipine is a strong dihydropyridine vasodilator, and the drop in pressure prompts a reflex rise in heart rate."],
  ["Verapamil", "Verapamil is a non-dihydropyridine agent that lowers heart rate and slows atrioventricular conduction instead of raising the rate."],
  ["Diltiazem", "Diltiazem is a non-dihydropyridine agent that lowers heart rate; the reflex tachycardia belongs to the dihydropyridine vasodilators."],
  ["Amlodipine", "Amlodipine leaves heart rate essentially unchanged, unlike nifedipine and felodipine, which raise it through reflex tachycardia."]],
 "c": 0, "cite": D + ", Slide 21"},

# ---- angina types, goals and risk factors ----------------------------------------
{"topic": "Angina types and goals", "io": IO_CLASS, "slot": "class",
 "q": "Which type of angina is caused by a transient, abrupt narrowing of a coronary artery, often at night or in the early morning?",
 "opts": [
  ["Variant (Prinzmetal) angina", "Correct. Vasospastic angina is a transient, abrupt reduction in vessel diameter; it affects younger patients with fewer risk factors and often occurs at night."],
  ["Chronic stable angina", "Chronic stable angina is the exertional pattern graded I to IV by the activity that provokes it; it is not a night-time vasospastic event."],
  ["Unstable angina", "Unstable angina belongs to acute coronary syndrome and signals plaque disruption, not a spasm of the vessel wall in a young patient."],
  ["Class I angina", "Class I angina means no limitation of ordinary activity and comfort at rest; it says nothing about a night-time vessel spasm, which defines variant angina."]],
 "c": 0, "cite": D + ", Slide 8"},

{"topic": "Angina types and goals", "io": IO_EDU, "slot": "education",
 "q": "Which risk factor for coronary heart disease can a patient change?",
 "opts": [
  ["Tobacco use", "Correct. Tobacco use, a sedentary lifestyle, diabetes, overweight, hypertension and dyslipidemia are modifiable risk factors that therapy targets."],
  ["Age older than 45 in men", "Age is fixed. Male age over 45 and female age over 55 are non-modifiable risk factors."],
  ["Age older than 55 in women", "Age cannot be changed. Female age over 55 is a non-modifiable risk factor, unlike tobacco use, which can be stopped."],
  ["Family history of premature events", "A family history of a premature cardiovascular event is non-modifiable, unlike tobacco use, diabetes or hypertension."]],
 "c": 0, "cite": D + ", Slide 9"},

{"topic": "Angina types and goals", "io": IO_IND, "slot": "indication",
 "q": "Which benefit do antianginal drugs provide?",
 "opts": [
  ["Better exercise capacity", "Correct. Antianginals improve exercise capacity, reduce exercise-induced ST-segment changes and lower the frequency of symptoms."],
  ["Regression of coronary plaque", "Antianginals relieve and prevent symptoms; they do not shrink plaque. Plaque stabilization is the job of vasculoprotective drugs such as statins."],
  ["Removal of coronary stenosis", "A fixed narrowing is treated by revascularization (stent or bypass graft). Antianginals improve exercise capacity and reduce symptoms."],
  ["Prevention of clot formation", "Clot prevention is the role of antiplatelet drugs such as aspirin. Antianginals improve exercise capacity and symptom frequency."]],
 "c": 0, "cite": D + ", Slide 14"},

# ---- variant angina --------------------------------------------------------------
{"topic": "Variant angina", "io": IO_CONTRA, "slot": "drug choice",
 "q": "A 34-year-old nonsmoker has chest pain that wakes her at 4 a.m., with ST-segment elevation that resolves. Which antianginal class is best avoided?",
 "opts": [
  ["Beta blockers", "Correct. This is vasospastic (variant) angina; beta blockers may worsen symptoms, while calcium channel blockers and nitrates reduce them."],
  ["Non-dihydropyridine calcium channel blockers", "Calcium channel blockers relieve vasospasm and are a mainstay of variant angina; beta blockers are the class to avoid."],
  ["Dihydropyridine calcium channel blockers", "Dihydropyridines relieve vasospasm and reduce symptoms in variant angina. The class that may worsen it is beta blockers."],
  ["Long-acting nitrates", "Nitrates relieve vasospasm and are used with calcium channel blockers in variant angina; beta blockers are the class to avoid."]],
 "c": 0, "cite": D + ", Slide 39"},

{"topic": "Variant angina", "io": IO_IND, "slot": "drug choice",
 "q": "Which combination reduces symptoms of vasospastic angina?",
 "opts": [
  ["Calcium channel blocker and nitrate", "Correct. Both classes relieve vasospasm and reduce symptoms; beta blockers are avoided because they may worsen them."],
  ["Beta blocker and nitrate", "The nitrate helps, but the beta blocker may worsen vasospastic angina; the calcium channel blocker is the partner to use."],
  ["Beta blocker and calcium channel blocker", "The calcium channel blocker helps, but a beta blocker may worsen vasospasm, so it should not be part of the regimen."],
  ["Beta blocker and aspirin", "A beta blocker may worsen vasospastic angina and aspirin prevents events rather than relieving symptoms; calcium channel blockers and nitrates reduce symptoms."]],
 "c": 0, "cite": D + ", Slide 39"},

# ---- beta blocker use ------------------------------------------------------------
{"topic": "Beta blocker use", "io": IO_IND, "slot": "drug choice",
 "q": "Which drug class is first line for chronic stable angina when no contraindication is present?",
 "opts": [
  ["Beta blockers", "Correct. Beta blockers are first-line therapy absent a contraindication; they lower heart rate and contractility and so lower oxygen demand."],
  ["Long-acting nitrates", "Long-acting nitrates are mostly added on or used when beta blockers and calcium channel blockers cannot be used; they are not first line."],
  ["Dihydropyridine calcium channel blockers", "Dihydropyridines are mainly added to a beta blocker when it is not enough, so they are not the first-line class."],
  ["Non-dihydropyridine calcium channel blockers", "Non-dihydropyridines are used when beta blockers are contraindicated or not tolerated, which makes them the alternative rather than the first choice."]],
 "c": 0, "cite": D + ", Slide 17"},

{"topic": "Beta blocker use", "io": IO_CLASS, "slot": "class",
 "q": "Which beta blocker is beta-1 selective?",
 "opts": [
  ["Metoprolol", "Correct. Metoprolol and atenolol are beta-1 selective beta blockers."],
  ["Propranolol", "Propranolol is a non-selective beta blocker, blocking beta-2 as well as beta-1 receptors; metoprolol and atenolol are the beta-1 selective agents."],
  ["Nadolol", "Nadolol is a non-selective beta blocker. The beta-1 selective beta blockers are metoprolol and atenolol."],
  ["Carvedilol", "Carvedilol is classed as a third-generation agent, along with labetalol, and not as a beta-1 selective one; metoprolol and atenolol are selective."]],
 "c": 0, "cite": D + ", Slide 17"},

{"topic": "Beta blocker use", "io": IO_IND, "slot": "indication",
 "q": "Which history makes a beta blocker the preferred antianginal?",
 "opts": [
  ["Prior myocardial infarction", "Correct. A beta blocker is given after a myocardial infarction unless contraindicated, and is the first-line antianginal in that setting."],
  ["Sinus bradycardia", "A slow heart rate is a reason to avoid beta blockers; a dihydropyridine calcium channel blocker is first line with bradycardia."],
  ["Reactive airway disease", "Reactive airway disease is a caution for beta blockers, especially non-selective ones; it is a reason for care, not the history that favors them."],
  ["Second-degree atrioventricular block", "Atrioventricular block is a contraindication to beta blockers, so they are not preferred; the post-infarction history is what favors them."]],
 "c": 0, "cite": D + ", Slide 38"},

# ---- beta blocker safety ---------------------------------------------------------

{"topic": "Beta blocker safety", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which heart condition is a contraindication to beta blockers?",
 "opts": [
  ["Acute decompensated heart failure", "Correct. Beta blockers can worsen an acutely decompensated heart; they are contraindicated there, along with bradycardia, low pressure and heart block."],
  ["Anxiety with angina", "Anxiety is listed among the conditions where beta blockers are useful, so it does not contraindicate them."],
  ["Supraventricular arrhythmia", "A supraventricular arrhythmia is an indication for a beta blocker, not a reason to avoid one."],
  ["Prior myocardial infarction", "A prior infarction is an indication for a beta blocker; the contraindication is acute decompensated heart failure."]],
 "c": 0, "cite": D + ", Slide 18"},

{"topic": "Beta blocker safety", "io": IO_AE, "slot": "adverse effect",
 "q": "A patient with peripheral vascular disease starts a beta blocker. Which symptom may worsen?",
 "opts": [
  ["Leg pain with walking", "Correct. Claudication is listed as a possible beta blocker adverse reaction, which is why peripheral vascular disease is a precaution."],
  ["Ankle swelling", "Ankle swelling (peripheral edema) is typical of dihydropyridine calcium channel blockers; the beta blocker precaution in vascular disease is claudication."],
  ["Facial flushing", "Flushing is an effect of nitrates and dihydropyridine calcium channel blockers; the beta blocker problem in vascular disease is claudication."],
  ["Constipation", "Constipation is counseled with calcium channel blockers. The beta blocker precaution in peripheral vascular disease is claudication."]],
 "c": 0, "cite": D + ", Slide 19"},

{"topic": "Beta blocker safety", "io": IO_PROT, "slot": "monitoring",
 "q": "Which set of parameters is monitored during beta blocker therapy?",
 "opts": [
  ["Heart rate, glucose, lipids", "Correct. Beta blockers can cause bradycardia, hyperglycemia and dyslipidemia, so heart rate, blood sugar and lipids are followed."],
  ["Potassium, creatinine, sodium", "Those chemistry tests are not the ones tied to beta blocker adverse effects; heart rate, blood sugar and lipids are."],
  ["Liver enzymes, bilirubin, albumin", "Liver tests are not the monitoring focus; beta blockers call for heart rate, blood sugar and lipid checks."],
  ["Platelets, clotting time, hemoglobin", "Bleeding and clotting measures relate to antiplatelet and antithrombotic drugs, whereas beta blockers need heart rate, sugar and lipid monitoring."]],
 "c": 0, "cite": D + ", Slide 19"},

{"topic": "Beta blocker safety", "io": IO_AE, "slot": "adverse effect",
 "q": "Which adverse effect do beta blockers, calcium channel blockers, and nitrates share?",
 "opts": [
  ["Hypotension", "Correct. All three antianginal classes lower systolic pressure, and hypotension is listed for each."],
  ["Bradycardia", "Bradycardia occurs with beta blockers and non-dihydropyridines, but nitrates raise heart rate through a reflex response."],
  ["Peripheral edema", "Peripheral edema is a dihydropyridine effect; it is not shared by beta blockers or nitrates."],
  ["Sexual dysfunction", "Sexual dysfunction is listed for beta blockers only; the effect all three classes share is hypotension."]],
 "c": 0, "cite": D + ", Slide 19"},

{"topic": "Beta blocker safety", "io": IO_EDU, "slot": "education",
 "q": "A patient taking a beta blocker feels well and wants to stop it. What should he be told?",
 "opts": [
  ["Avoid stopping it abruptly", "Correct. Rapid discontinuation of a beta blocker must be avoided, so the patient should not stop it on his own."],
  ["Stop it once symptoms resolve", "Stopping because he feels well is the error; beta blockers are prophylactic, and rapid discontinuation must be avoided."],
  ["Take it only when chest pain starts", "Beta blockers prevent symptoms and are taken on a schedule; as-needed use is the pattern for sublingual nitroglycerin."],
  ["Skip it on days without exertion", "Beta blockers work as regular prophylaxis and are not skipped on quiet days; stopping rapidly is what must be avoided."]],
 "c": 0, "cite": D + ", Slide 19"},

{"topic": "Beta blocker safety", "io": IO_AE, "slot": "adverse effect",
 "q": "Which class is most likely responsible for nightmares and sexual dysfunction?",
 "opts": [
  ["Beta blockers", "Correct. Fatigue, sexual dysfunction, nightmares and worsened claudication are listed adverse reactions of beta blockers."],
  ["Dihydropyridine calcium channel blockers", "Dihydropyridines cause headache, flushing and peripheral edema, not nightmares or sexual dysfunction."],
  ["Long-acting nitrates", "Nitrates cause headache, flushing, postural hypotension and reflex tachycardia; nightmares and sexual dysfunction point to beta blockers."],
  ["Non-dihydropyridine calcium channel blockers", "Non-dihydropyridines are counseled for dizziness and constipation; nightmares and sexual dysfunction are beta blocker effects."]],
 "c": 0, "cite": D + ", Slide 19"},

# ---- calcium channel blocker split -----------------------------------------------
{"topic": "Calcium channel blocker split", "io": IO_CLASS, "slot": "class",
 "q": "Which drug is a non-dihydropyridine calcium channel blocker?",
 "opts": [
  ["Diltiazem", "Correct. Diltiazem and verapamil are the non-dihydropyridines, which lower heart rate and slow atrioventricular conduction."],
  ["Amlodipine", "Amlodipine is a dihydropyridine, a mainly vasodilating agent with little effect on heart rate or atrioventricular conduction."],
  ["Nifedipine", "Nifedipine is a dihydropyridine; the non-dihydropyridine agents are diltiazem and verapamil."],
  ["Felodipine", "Felodipine is a dihydropyridine vasodilator; diltiazem and verapamil make up the non-dihydropyridine group."]],
 "c": 0, "cite": D + ", Slide 21"},

{"topic": "Calcium channel blocker split", "io": IO_CONTRA, "slot": "drug choice",
 "q": "Which calcium channel blocker formulation should be avoided in angina?",
 "opts": [
  ["Short-acting nifedipine", "Correct. Short-acting agents, nifedipine in particular, should be avoided; long-acting agents are used."],
  ["Long-acting amlodipine", "Long-acting amlodipine is an accepted choice, often added to a beta blocker; the agent to avoid is short-acting nifedipine."],
  ["Sustained-release verapamil", "Verapamil is an accepted non-dihydropyridine choice; the formulation to avoid is short-acting nifedipine."],
  ["Extended-release diltiazem", "Diltiazem is an accepted non-dihydropyridine choice; short-acting nifedipine is the one to avoid."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Calcium channel blocker split", "io": IO_INTER, "slot": "interaction",
 "q": "Why do verapamil and diltiazem call for caution with a beta blocker?",
 "opts": [
  ["Additive bradycardia and conduction delay", "Correct. Both lower heart rate and slow atrioventricular conduction, so combining them with a beta blocker adds to these effects."],
  ["Additive reflex tachycardia", "Reflex tachycardia is a dihydropyridine effect. Verapamil and diltiazem lower heart rate, which is why they add to a beta blocker."],
  ["Reduced absorption of the beta blocker", "The concern is the additive effect on heart rate and conduction, not absorption: both drugs slow the heart and the atrioventricular node, so the effects add."],
  ["Loss of blood pressure lowering effect", "Both drug types lower pressure, so the effect is not lost; the concern is additive slowing of heart rate and conduction."]],
 "c": 0, "cite": D + ", Slide 23"},

{"topic": "Calcium channel blocker split", "io": IO_IND, "slot": "indication",
 "q": "Which condition favors choosing a calcium channel blocker over a beta blocker?",
 "opts": [
  ["Vasospastic angina", "Correct. Calcium channel blockers relieve vasospasm, while beta blockers may worsen vasospastic angina."],
  ["Prior myocardial infarction", "A prior infarction favors a beta blocker, which is first line after a myocardial infarction."],
  ["Hypertension with angina", "Beta blockers are first line for hypertension with angina; a calcium channel blocker is only the alternative."],
  ["Anxiety with angina", "Anxiety is one of the conditions where a beta blocker is useful, so it does not push toward a calcium channel blocker; vasospastic angina does."]],
 "c": 0, "cite": D + ", Slide 22"},

# ---- comorbid conditions ---------------------------------------------------------
{"topic": "Comorbid conditions", "io": IO_IND, "slot": "drug choice",
 "q": "A patient with angina has a heart rate of 50 beats per minute and atrioventricular block. Which class is first line?",
 "opts": [
  ["Dihydropyridine calcium channel blockers", "Correct. With bradycardia or atrioventricular block, a dihydropyridine is first line; it does not slow atrioventricular conduction."],
  ["Beta blockers", "Beta blockers slow the heart and conduction and are contraindicated with bradycardia or atrioventricular block."],
  ["Non-dihydropyridine calcium channel blockers", "Verapamil and diltiazem slow heart rate and atrioventricular conduction, so they are avoided with bradycardia or heart block."],
  ["Long-acting nitrates", "Long-acting nitrates are the alternative here, not first line; a dihydropyridine is preferred."]],
 "c": 0, "cite": D + ", Slide 34"},

{"topic": "Comorbid conditions", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which antianginal type is best avoided in a patient with angina and asthma?",
 "opts": [
  ["Non-selective beta blockers", "Correct. In asthma, non-selective beta blockers are avoided; cardioselective beta blockers and calcium channel blockers remain options."],
  ["Beta-1 selective beta blockers", "Beta-1 selective agents have less airway effect and are the beta blocker choice if one is needed; the non-selective ones are the problem."],
  ["Non-dihydropyridine calcium channel blockers", "Non-dihydropyridines are first line in asthma; they do not block airway beta receptors."],
  ["Dihydropyridine calcium channel blockers", "Calcium channel blockers are a suitable choice in asthma; the class to avoid is the non-selective beta blockers."]],
 "c": 0, "cite": D + ", Slide 34"},

{"topic": "Comorbid conditions", "io": IO_IND, "slot": "drug choice",
 "q": "When left ventricular function is decreased and a beta blocker cannot be used, which calcium channel blocker is the alternative?",
 "opts": [
  ["Amlodipine", "Correct. Beta blockers are first line with decreased left ventricular function; amlodipine is the calcium channel blocker alternative."],
  ["Verapamil", "Non-dihydropyridines such as verapamil are avoided when left ventricular function is decreased, since they depress contractility."],
  ["Diltiazem", "Diltiazem lowers contractility and heart rate, so it is avoided with decreased left ventricular function; amlodipine is the alternative."],
  ["Nifedipine", "Calcium channel blockers other than amlodipine are avoided with decreased left ventricular function, and nifedipine's short-acting form is avoided in angina anyway."]],
 "c": 0, "cite": D + ", Slide 34"},

# ---- calcium channel blocker safety ----------------------------------------------
{"topic": "Calcium channel blocker safety", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which condition is a contraindication to non-dihydropyridine calcium channel blockers?",
 "opts": [
  ["Acute heart failure", "Correct. Verapamil and diltiazem depress contractility, so acute heart failure, low ejection fraction, bradycardia and heart block contraindicate them."],
  ["Vasospastic angina", "Vasospastic angina is a reason to choose a calcium channel blocker, which relieves vasospasm."],
  ["Severe peripheral vascular disease", "Severe peripheral vascular disease favors calcium channel blockers over beta blockers rather than contraindicating them."],
  ["Asthma", "Asthma does not contraindicate calcium channel blockers; they do not block airway beta receptors and are a first-line choice there."]],
 "c": 0, "cite": D + ", Slide 23"},

{"topic": "Calcium channel blocker safety", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which blood pressure reading contraindicates starting a beta blocker or calcium channel blocker?",
 "opts": [
  ["Systolic pressure below 100 mmHg", "Correct. Both classes lower blood pressure, so a systolic pressure below 100 mmHg contraindicates them."],
  ["Systolic pressure above 140 mmHg", "High pressure is not a contraindication; hypertension with angina is a reason to use a beta blocker."],
  ["Diastolic pressure above 90 mmHg", "An elevated diastolic pressure is no reason to withhold these drugs; the concern is pressure too low, not too high."],
  ["Systolic pressure below 130 mmHg", "A systolic pressure below 130 mmHg is not a contraindication; the limit for starting these drugs is a systolic pressure below 100 mmHg."]],
 "c": 0, "cite": D + ", Slide 23"},

{"topic": "Calcium channel blocker safety", "io": IO_AE, "slot": "adverse effect",
 "q": "Which adverse effect is typical of dihydropyridine calcium channel blockers?",
 "opts": [
  ["Peripheral edema", "Correct. Headache, flushing and peripheral edema are the characteristic dihydropyridine effects, reflecting strong vasodilation."],
  ["Bradycardia", "Bradycardia belongs to beta blockers and non-dihydropyridines; dihydropyridines tend to raise or leave heart rate unchanged."],
  ["Nightmares", "Nightmares are a beta blocker effect, not a dihydropyridine one."],
  ["Hyperglycemia", "Hyperglycemia is a beta blocker effect; dihydropyridines cause headache, flushing and peripheral edema."]],
 "c": 0, "cite": D + ", Slide 24"},

{"topic": "Calcium channel blocker safety", "io": IO_INTER, "slot": "interaction",
 "q": "Which enzyme's interactions call for caution with calcium channel blockers?",
 "opts": [
  ["Cytochrome P450 3A4", "Correct. Calcium channel blockers are subject to cytochrome P450 3A4 interactions, so drugs that inhibit or induce it change their levels."],
  ["Cytochrome P450 2D6", "Cytochrome P450 2D6 is not the enzyme flagged for calcium channel blockers; the precaution is cytochrome P450 3A4."],
  ["Cytochrome P450 2C9", "Cytochrome P450 2C9 is not the enzyme flagged for this class; the precaution is cytochrome P450 3A4."],
  ["Cytochrome P450 1A2", "Cytochrome P450 1A2 is not the enzyme flagged for this class; the precaution is cytochrome P450 3A4."]],
 "c": 0, "cite": D + ", Slide 23"},

{"topic": "Calcium channel blocker safety", "io": IO_EDU, "slot": "education",
 "q": "Patients starting a calcium channel blocker are counseled about dizziness and which other problem?",
 "opts": [
  ["Constipation", "Correct. Dizziness and constipation are the counseling points for calcium channel blockers."],
  ["Nightmares", "Nightmares are a beta blocker adverse effect; constipation is the second counseling point for calcium channel blockers."],
  ["Hyperglycemia", "Hyperglycemia is a beta blocker effect; calcium channel blocker counseling covers dizziness and constipation."],
  ["Sexual dysfunction", "Sexual dysfunction is listed for beta blockers; calcium channel blocker counseling covers dizziness and constipation."]],
 "c": 0, "cite": D + ", Slide 24"},

# ---- nitrate use -----------------------------------------------------------------
{"topic": "Nitrate use", "io": IO_IND, "slot": "drug choice",
 "q": "Which nitrate formulation is used to relieve an acute attack of angina?",
 "opts": [
  ["Sublingual nitroglycerin", "Correct. Short-acting nitroglycerin (tablet or spray under the tongue) relieves acute symptoms and can prevent effort-induced angina."],
  ["Isosorbide mononitrate", "Isosorbide mononitrate is a long-acting agent lasting about 12 hours, used for prevention rather than rescue."],
  ["Isosorbide dinitrate", "Isosorbide dinitrate is long-acting, lasting 3 to 6 hours, and used for prophylaxis, not for an acute attack."],
  ["Nitroglycerin ointment", "Nitroglycerin ointment is a long-acting form spread on the chest for prevention; sublingual nitroglycerin is used for an acute attack."]],
 "c": 0, "cite": D + ", Slide 27"},


{"topic": "Nitrate use", "io": IO_IND, "slot": "drug choice",
 "q": "How are long-acting nitrates usually used?",
 "opts": [
  ["As add-on therapy", "Correct. They are usually adjunctive, added when a beta blocker or calcium channel blocker is not enough; monotherapy is not recommended."],
  ["As first-line monotherapy", "Long-acting nitrates are not recommended as monotherapy; beta blockers are first line, with nitrates usually added on."],
  ["Only for acute attacks", "Acute attacks are treated with short-acting sublingual nitroglycerin. Long-acting forms are for prevention, usually as add-on therapy."],
  ["Only after an infarction", "Long-acting nitrates are not limited to a post-infarction role; they are adjunctive antianginals added to other drugs."]],
 "c": 0, "cite": D + ", Slide 29"},

{"topic": "Nitrate use", "io": IO_IND, "slot": "indication",
 "q": "Besides relieving an acute attack, what is short-acting nitroglycerin used for?",
 "opts": [
  ["Preventing effort-induced angina", "Correct. Short-acting nitrates are taken before activity to prevent effort-induced angina as well as to relieve acute symptoms."],
  ["Preventing acute coronary syndromes", "Preventing acute coronary syndromes is the role of vasculoprotective drugs such as aspirin and statins, not of nitrates."],
  ["Lowering mortality after infarction", "Nitrates give no mortality benefit, only relief of chest pain; beta blockers are the drug that lowers mortality after infarction."],
  ["Replacing daily beta blockers", "Short-acting nitroglycerin is a rescue and pre-exertion drug, not a daily replacement for prophylactic therapy."]],
 "c": 0, "cite": D + ", Slide 27"},

{"topic": "Nitrate use", "io": IO_IND, "slot": "drug choice",
 "q": "Long-acting nitrates become initial therapy when which drugs cannot be used?",
 "opts": [
  ["Beta blockers and calcium channel blockers", "Correct. A long-acting nitrate is initial therapy only when both beta blockers and calcium channel blockers are contraindicated or not tolerated."],
  ["Beta blockers alone", "If only beta blockers are unsuitable, a calcium channel blocker is the next choice; nitrates are used when both classes fail."],
  ["Calcium channel blockers alone", "Beta blockers are first line, so losing calcium channel blockers alone does not make a nitrate the initial drug."],
  ["Aspirin and clopidogrel", "Antiplatelets are vasculoprotective rather than antianginal, so their absence does not make a nitrate initial therapy."]],
 "c": 0, "cite": D + ", Slide 29"},

{"topic": "Nitrate use", "io": IO_PROT, "slot": "protocol",
 "q": "Angina persists despite two antianginal drugs. What is the usual next step?",
 "opts": [
  ["Further workup, such as angiography", "Correct. If a third agent seems needed, the patient probably needs further workup such as angiography rather than another drug."],
  ["Lifestyle counseling alone", "Lifestyle change is part of care for everyone, but persistent angina on two drugs calls for further workup such as angiography, not counseling alone."],
  ["Adding an antiplatelet for symptoms", "Antiplatelet drugs do not relieve angina symptoms; they help prevent events. Persistent angina calls for further workup."],
  ["Adding a third drug without reassessment", "A third agent probably signals the need for further workup such as angiography first, rather than adding another drug without reassessment."]],
 "c": 0, "cite": D + ", Slide 36"},

{"topic": "Nitrate use", "io": IO_MOA, "slot": "mechanism",
 "q": "Which second messenger do nitrates increase to relax vascular smooth muscle?",
 "opts": [
  ["Cyclic guanosine monophosphate", "Correct. Nitric oxide from nitrates stimulates conversion of guanosine triphosphate to cyclic guanosine monophosphate, which lowers calcium and relaxes smooth muscle."],
  ["Cyclic adenosine monophosphate", "Cyclic adenosine monophosphate is the messenger of beta receptor signaling, not the nitrate pathway, which raises cyclic guanosine monophosphate."],
  ["Inositol trisphosphate", "Inositol trisphosphate releases calcium and promotes contraction, the opposite of the nitrate effect, which runs through cyclic guanosine monophosphate."],
  ["Cytosolic calcium", "Nitrates lower cytosolic calcium to relax smooth muscle; the messenger they raise is cyclic guanosine monophosphate."]],
 "c": 0, "cite": D + ", Slide 26"},

# ---- add-on therapy --------------------------------------------------------------
{"topic": "Add-on therapy", "io": IO_IND, "slot": "indication",
 "q": "What role do angiotensin-converting enzyme inhibitors play in stable coronary artery disease?",
 "opts": [
  ["They may slow disease progression", "Correct. They do not relieve angina, but may slow progression and are used in coronary disease with diabetes or left ventricular systolic dysfunction."],
  ["They relieve acute angina attacks", "They do not relieve angina symptoms; sublingual nitroglycerin relieves an acute attack."],
  ["They lower myocardial oxygen consumption", "They do not significantly change myocardial oxygen consumption, unlike beta blockers, calcium channel blockers and nitrates."],
  ["They prevent effort-induced angina", "Because they do not relieve angina, they are not antianginal prophylaxis; their role is to slow disease progression."]],
 "c": 0, "cite": D + ", Slide 35"},

{"topic": "Add-on therapy", "io": IO_IND, "slot": "indication",
 "q": "What is aspirin used for in ischemic heart disease?",
 "opts": [
  ["Preventing acute coronary syndromes", "Correct. Aspirin is given to all patients with ischemic heart disease without contraindications to prevent acute coronary syndromes."],
  ["Relieving effort-induced angina", "Aspirin does not relieve angina symptoms; nitrates, beta blockers and calcium channel blockers do that."],
  ["Lowering heart rate", "Lowering heart rate is a beta blocker and non-dihydropyridine effect; aspirin is an antiplatelet that prevents acute coronary syndromes."],
  ["Lowering wall tension", "Lowering wall tension is done by nitrates and other vasodilators; aspirin's role is preventing acute coronary syndromes."]],
 "c": 0, "cite": D + ", Slide 37"},

{"topic": "Add-on therapy", "io": IO_IND, "slot": "drug choice",
 "q": "Which drug is recommended for patients allergic to aspirin?",
 "opts": [
  ["Clopidogrel", "Correct. Clopidogrel is as efficacious as aspirin in secondary prevention and is recommended when aspirin cannot be used because of allergy."],
  ["Heparin", "Heparin is an anticoagulant used alongside fibrinolysis or antiplatelet agents, not a substitute for aspirin; clopidogrel is the antiplatelet used for aspirin allergy."],
  ["Enoxaparin", "Enoxaparin is a low-molecular-weight heparin, an anticoagulant, not the antiplatelet substitute for aspirin allergy; that is clopidogrel."],
  ["Alteplase", "Alteplase is a fibrinolytic that dissolves a clot in an acute infarction; it is not used as chronic antiplatelet therapy."]],
 "c": 0, "cite": D + ", Slide 37"},

{"topic": "Add-on therapy", "io": IO_CLASS, "slot": "class",
 "q": "Which drug is vasculoprotective rather than antianginal?",
 "opts": [
  ["Aspirin", "Correct. Aspirin, statins and angiotensin-converting enzyme inhibitors are the vasculoprotective group; beta blockers, calcium channel blockers and nitrates are the antianginals."],
  ["Metoprolol", "Metoprolol is a beta blocker, an antianginal that lowers heart rate and contractility."],
  ["Amlodipine", "Amlodipine is a calcium channel blocker, an antianginal; aspirin is the vasculoprotective option in this list."],
  ["Isosorbide mononitrate", "Isosorbide mononitrate is a long-acting nitrate, an antianginal; aspirin is the vasculoprotective option."]],
 "c": 0, "cite": D + ", Slide 12"},

# ---- nitrate education -----------------------------------------------------------
{"topic": "Nitrate education", "io": IO_EDU, "slot": "education",
 "q": "Where should nitroglycerin tablets be stored?",
 "opts": [
  ["In the original container", "Correct. Tablets belong in the original packaging in a cool, dry place."],
  ["In a daily pill organizer", "Tablets should stay in the original packaging in a cool, dry place, not be moved to a daily pill organizer."],
  ["In the bathroom cabinet", "A bathroom is warm and humid; tablets need their original packaging and a cool, dry place."],
  ["In the refrigerator", "Nitroglycerin tablets are kept in the original packaging in a cool, dry place, not refrigerated."]],
 "c": 0, "cite": D + ", Slide 28"},

{"topic": "Nitrate education", "io": IO_EDU, "slot": "education",
 "q": "How is nitroglycerin taken for an acute attack?",
 "opts": [
  ["Under the tongue", "Correct. A sublingual tablet or spray is placed under the tongue for rapid absorption."],
  ["Swallowed whole with water", "Nitroglycerin for an acute attack is used under the tongue; swallowing it would delay relief."],
  ["Chewed and swallowed", "Chewing and swallowing is the instruction for aspirin at the first signs of chest pain, not for nitroglycerin."],
  ["Applied to the chest", "Chest application describes nitroglycerin ointment, a long-acting form; the acute attack form is placed under the tongue."]],
 "c": 0, "cite": D + ", Slide 28"},

{"topic": "Nitrate education", "io": IO_EDU, "slot": "education",
 "q": "A patient's chest pain is not relieved 5 minutes after the first nitroglycerin dose. What should he do?",
 "opts": [
  ["Call emergency services", "Correct. No relief after the first dose means he should call emergency services, while repeat doses continue until help arrives."],
  ["Wait 30 minutes before repeating", "Waiting is unsafe; unrelieved pain may signal an infarction, so emergency services are called at once and repeat doses continue."],
  ["Switch to a long-acting nitrate", "Long-acting nitrates are preventive and act too slowly for an unrelieved attack; emergency services must be called."],
  ["Rest and see if the pain settles", "Pain not relieved by the first dose needs emergency services; waiting passively risks delaying care for a possible infarction."]],
 "c": 0, "cite": D + ", Slide 27"},

{"topic": "Nitrate education", "io": IO_EDU, "slot": "education",
 "q": "What should patients starting a nitrate be warned about?",
 "opts": [
  ["Dizziness when standing up", "Correct. Nitrates cause orthostatic hypotension, so patients are warned about light-headedness on standing."],
  ["Constipation after each dose", "Constipation is counseled with calcium channel blockers; the nitrate warning is orthostatic hypotension."],
  ["Slow heart rate at rest", "Nitrates raise heart rate reflexively; slow heart rate is a beta blocker effect. The nitrate warning is orthostatic hypotension."],
  ["Persistent dry cough", "Dry cough is not a nitrate effect; the warning is orthostatic hypotension, which causes dizziness on standing."]],
 "c": 0, "cite": D + ", Slide 28"},

{"topic": "Nitrate education", "io": IO_EDU, "slot": "education",
 "q": "How is a nitroglycerin patch or ointment scheduled through the day?",
 "opts": [
  ["12 hours on, then 12 hours off", "Correct. The patch or ointment is worn for 12 hours and left off for 12 hours each day."],
  ["Worn continuously, changed daily", "Continuous exposure leads to loss of effect; a daily gap without the drug preserves it."],
  ["Applied only when pain starts", "Patches and ointment are slowly absorbed preventive forms, not rescue drugs; sublingual nitroglycerin treats an attack."],
  ["6 hours on, then 18 hours off", "The taught schedule is 12 hours on and 12 hours off; 6 hours on would leave most of the day without antianginal coverage."]],
 "c": 0, "cite": D + ", Slide 31"},

# ---- nitrate tolerance -----------------------------------------------------------
{"topic": "Nitrate tolerance", "io": IO_AE, "slot": "adverse effect",
 "q": "What is the loss of nitrate effect with continuous use called?",
 "opts": [
  ["Tachyphylaxis", "Correct. Tachyphylaxis is rapid tolerance to a nitrate's effect, handled with a nitrate-free interval."],
  ["Anaphylaxis", "Anaphylaxis is a severe allergic reaction; the loss of nitrate effect with continuous use is tachyphylaxis."],
  ["Reflex tachycardia", "Reflex tachycardia is a nitrate adverse effect from vasodilation, not loss of response."],
  ["Rebound angina", "Rebound angina describes symptoms returning after a drug is withdrawn; the loss of effect during continuous use is tachyphylaxis."]],
 "c": 0, "cite": D + ", Slide 32"},


# ---- nitrate safety --------------------------------------------------------------
{"topic": "Nitrate safety", "io": IO_INTER, "slot": "interaction",
 "q": "Which drug class must not be combined with nitrates?",
 "opts": [
  ["Phosphodiesterase-5 inhibitors", "Correct. Sildenafil, tadalafil and vardenafil with a nitrate can cause hypotension, myocardial infarction or stroke."],
  ["Beta blockers", "Beta blockers are routinely combined with nitrates in angina; the dangerous partner is a phosphodiesterase-5 inhibitor."],
  ["Calcium channel blockers", "Calcium channel blockers are used with long-acting nitrates; the contraindicated combination is a phosphodiesterase-5 inhibitor."],
  ["Angiotensin-converting enzyme inhibitors", "These are not contraindicated with nitrates; the unsafe combination is a phosphodiesterase-5 inhibitor."]],
 "c": 0, "cite": D + ", Slide 33"},


{"topic": "Nitrate safety", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which condition is a contraindication to nitrates?",
 "opts": [
  ["Obstructive cardiomyopathy", "Correct. Nitrates are contraindicated in obstructive cardiomyopathy, as well as in aortic valve stenosis and with phosphodiesterase-5 inhibitors."],
  ["Vasospastic angina", "Vasospastic angina is treated with nitrates, which relieve vasospasm."],
  ["Effort-induced angina", "Effort-induced angina is an indication for nitrates, which are taken to prevent it."],
  ["Prior myocardial infarction", "A prior infarction is not a nitrate contraindication; obstructive cardiomyopathy is."]],
 "c": 0, "cite": D + ", Slide 33"},

{"topic": "Nitrate safety", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which valve lesion contraindicates nitrates?",
 "opts": [
  ["Aortic valve stenosis", "Correct. Aortic valve stenosis is a nitrate contraindication, alongside obstructive cardiomyopathy and phosphodiesterase-5 inhibitor use."],
  ["Mitral valve prolapse", "Mitral valve prolapse is not among the nitrate contraindications; aortic valve stenosis is the valve lesion listed."],
  ["Aortic regurgitation", "Aortic regurgitation is not listed as a nitrate contraindication; the valve lesion listed is aortic valve stenosis."],
  ["Tricuspid regurgitation", "Tricuspid regurgitation is not listed as a nitrate contraindication; aortic valve stenosis is."]],
 "c": 0, "cite": D + ", Slide 33"},

{"topic": "Nitrate safety", "io": IO_EDU, "slot": "education",
 "q": "A man taking isosorbide mononitrate asks about erectile dysfunction drugs. What is the counseling?",
 "opts": [
  ["Avoid combining them with nitrates", "Correct. Sildenafil, tadalafil and vardenafil with any nitrate can cause hypotension, myocardial infarction or stroke."],
  ["Safe if the nitrate is a skin patch", "The route does not matter; any nitrate combined with a phosphodiesterase-5 inhibitor can cause dangerous hypotension."],
  ["Safe if taken with a meal", "A meal does not remove the interaction; the combination can still cause hypotension, myocardial infarction or stroke."],
  ["Safe if the nitrate is short-acting", "Short-acting nitrates interact too; the combination is contraindicated regardless of nitrate formulation."]],
 "c": 0, "cite": D + ", Slide 33"},

{"topic": "Nitrate safety", "io": IO_AE, "slot": "adverse effect",
 "q": "Which adverse effects do nitrates and dihydropyridine calcium channel blockers share?",
 "opts": [
  ["Headache and flushing", "Correct. Nitrates and dihydropyridines both cause headache and flushing, reflecting vasodilation."],
  ["Bradycardia and fatigue", "Bradycardia and fatigue are beta blocker effects; nitrates and dihydropyridines instead cause headache and flushing."],
  ["Constipation and cough", "Constipation is a calcium channel blocker counseling point, but cough is not listed; the shared effects are headache and flushing."],
  ["Nightmares and dyslipidemia", "Both are beta blocker effects; nitrates and dihydropyridines share headache and flushing from vasodilation."]],
 "c": 0, "cite": D + ", Slide 31"},

{"topic": "Nitrate safety", "io": IO_AE, "slot": "adverse effect",
 "q": "Which adverse effect of nitrates is a compensatory response to vasodilation?",
 "opts": [
  ["Reflex tachycardia", "Correct. Falling pressure from vasodilation prompts a reflex rise in heart rate; it is listed with headache, flushing and postural hypotension."],
  ["Bradycardia", "Nitrates raise heart rate reflexively rather than slowing it; bradycardia is a beta blocker effect."],
  ["Heart block", "Nitrates do not slow atrioventricular conduction; heart block is a concern with beta blockers and non-dihydropyridines."],
  ["Hyperglycemia", "Hyperglycemia is a beta blocker effect; the nitrate compensatory response is reflex tachycardia."]],
 "c": 0, "cite": D + ", Slide 31"},

{"topic": "Supply and demand", "io": IO_MOA, "slot": "physiology",
 "q": "Which antianginal class lowers oxygen demand mainly by reducing ventricular volume?",
 "opts": [
  ["Nitrates", "Correct. Nitrates lower left ventricular volume the most, which lowers wall tension; they raise heart rate reflexively rather than lowering it."],
  ["Beta blockers", "Beta blockers lower heart rate and contractility, and ventricular volume actually rises; they do not reduce it."],
  ["Non-dihydropyridine calcium channel blockers", "Verapamil and diltiazem act mainly through lower heart rate and contractility, leaving ventricular volume unchanged or slightly lower."],
  ["Dihydropyridine calcium channel blockers", "Dihydropyridines act mainly by lowering systolic pressure through arterial vasodilation; ventricular volume is unchanged or slightly lower."]],
 "c": 0, "cite": D + ", Slide 25"},

{"topic": "Angina types and goals", "io": IO_IND, "slot": "indication",
 "q": "Which treatment goal extends life rather than improving quality of life?",
 "opts": [
  ["Preventing acute coronary syndromes", "Correct. Preventing acute coronary syndromes increases the quantity of life; relieving and preventing symptoms improves its quality."],
  ["Relieving symptoms", "Relieving symptoms improves quality of life; preventing acute coronary syndromes is the goal that increases its quantity."],
  ["Preventing symptoms", "Preventing symptoms improves quality of life, not its length; preventing acute coronary syndromes increases quantity of life."],
  ["Improving exercise capacity", "Better exercise capacity is a quality-of-life benefit of antianginal drugs; preventing acute coronary syndromes is the goal that extends life."]],
 "c": 0, "cite": D + ", Slide 10"},

# ---- cytochrome P450 3A4 (emphasized), intolerance switch, prevention against quick relief ----
{"topic": "Calcium channel blocker safety", "io": IO_INTER, "slot": "interaction",
 "q": "Which calcium channel blocker both inhibits and is a substrate of cytochrome P450 3A4?",
 "opts": [
  ["Verapamil", "Correct. Verapamil (like diltiazem) is both a substrate and an inhibitor of cytochrome P450 3A4, so it raises levels of other drugs cleared by that enzyme."],
  ["Amlodipine", "Amlodipine is a dihydropyridine, taught as a cytochrome P450 3A4 substrate only, not a meaningful inhibitor like verapamil and diltiazem."],
  ["Nifedipine", "Nifedipine is a dihydropyridine, taught as a cytochrome P450 3A4 substrate only, not a meaningful inhibitor; the non-dihydropyridines, verapamil and diltiazem, are the inhibitors."],
  ["Felodipine", "Felodipine is a dihydropyridine, taught as a cytochrome P450 3A4 substrate only, not a meaningful inhibitor, so it does not raise levels of other drugs the way verapamil does."]],
 "c": 0, "cite": "Antihypertensives.pptx, Slide 47"},

{"topic": "Calcium channel blocker safety", "io": IO_INTER, "slot": "interaction",
 "q": "A patient taking verapamil is started on a statin. Which statin's level rises most?",
 "opts": [
  ["Simvastatin", "Correct. Simvastatin is a cytochrome P450 3A4 substrate, and verapamil inhibits that enzyme, so simvastatin levels climb (statin metabolism is covered with the lipid-lowering drugs)."],
  ["Rosuvastatin", "Rosuvastatin undergoes minimal cytochrome P450 metabolism, so a 3A4 inhibitor such as verapamil barely changes its level."],
  ["Pravastatin", "Pravastatin is cleared by enzymatic and nonenzymatic routes rather than by cytochrome P450 3A4, so verapamil has little effect on it."],
  ["Pitavastatin", "Pitavastatin is cleared mainly by glucuronidation, not cytochrome P450 3A4, so verapamil does not raise its level much."]],
 "c": 0, "cite": "Antihypertensives.pptx, Slide 47"},

{"topic": "Calcium channel blocker safety", "io": IO_INTER, "slot": "interaction",
 "q": "What is the main risk of adding simvastatin to a patient who takes verapamil?",
 "opts": [
  ["Statin muscle and liver toxicity", "Correct. Verapamil inhibits cytochrome P450 3A4, which clears simvastatin, so higher simvastatin levels raise the risk of muscle and liver toxicity."],
  ["Loss of the verapamil effect", "Simvastatin does not blunt verapamil; the interaction runs the other way, with verapamil raising simvastatin levels."],
  ["Excess slowing of the heart", "Simvastatin has no effect on heart rate or conduction; the hazard is the higher statin level caused by cytochrome P450 3A4 inhibition."],
  ["Reduced absorption of simvastatin", "Verapamil does not reduce simvastatin absorption; by blocking cytochrome P450 3A4 it raises simvastatin levels."]],
 "c": 0, "cite": "Antihypertensives.pptx, Slide 47"},

{"topic": "Calcium channel blocker split", "io": IO_IND, "slot": "drug choice",
 "q": "A patient started on a beta blocker for angina cannot tolerate it because of nightmares. Which drug is the usual substitute?",
 "opts": [
  ["Diltiazem", "Correct. A non-dihydropyridine calcium channel blocker is the usual substitute when a beta blocker is not tolerated, since it also lowers heart rate and contractility."],
  ["Isosorbide mononitrate", "A long-acting nitrate is used when beta blockers and calcium channel blockers cannot be used, so it is not the first substitute."],
  ["Sublingual nitroglycerin", "Sublingual nitroglycerin is a rescue drug for acute attacks; it cannot replace a daily preventive such as a beta blocker."],
  ["Lisinopril", "Angiotensin-converting enzyme inhibitors do not relieve angina symptoms, so they cannot substitute for a beta blocker; a non-dihydropyridine such as diltiazem can."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Nitrate use", "io": IO_IND, "slot": "drug choice",
 "q": "Which drug is taken every day to prevent anginal attacks rather than to relieve an acute one?",
 "opts": [
  ["Metoprolol", "Correct. Beta blockers, calcium channel blockers and long-acting nitrates are taken to prevent attacks; they are not rescue drugs."],
  ["Sublingual nitroglycerin", "Sublingual nitroglycerin is the quick-relief drug for an acute attack; it can be taken before exertion to prevent effort-induced angina, but it is not a daily preventive."],
  ["Nitroglycerin lingual spray", "The lingual spray is a short-acting rescue form; it can be used before exertion to prevent effort-induced angina, but the daily preventives are beta blockers, calcium channel blockers and long-acting nitrates."],
  ["Aspirin", "Aspirin prevents acute coronary syndromes; it neither prevents nor relieves attacks of angina, which is the job of antianginal drugs."]],
 "c": 0, "cite": D + ", Slide 27"},

]
