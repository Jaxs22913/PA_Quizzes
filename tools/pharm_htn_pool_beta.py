# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- Antihypertensives (Lecture 6), topic 3: beta blockers.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

SOURCE. Antihypertensives.pptx slides 55-75 plus the algorithm inset on 108.
Slide 60 (the first-generation table) exists only as an embedded Word object;
its content was read from the rendered object, not the slide text.

EMPHASIS FROM THE RECORDING (weight only): "distinguish between your different
groups of beta blockers" -- non-selective, beta-1 selective, and the two
third-generation agents that also block alpha-1 (carvedilol, labetalol); the
heart-failure trio ("just know these three"); propranolol's high lipid
solubility and its central effects; and the adverse effects that carry patient
education -- masked hypoglycemia, never stopping abruptly, cold extremities.

SLIDE WINS
  * "Works best in young patients" (slide 63) is keyed, although the recording
    first said the opposite and then corrected itself.
  * The recording's "third generation is still non-selective" is not keyed:
    betaxolol is labeled beta-1 selective on slide 62.

SCOPE CAPS: no membrane-stabilizing or intrinsic sympathomimetic columns, no
renal/hepatic elimination tags, nothing specific to carteolol or betaxolol
(both de-scoped), no doses. Propranolol's lipid solubility is the one table
property kept, because it was singled out.
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

# ---- groups ------------------------------------------------------------------
{"topic": "Beta blocker groups", "io": IO_CLASS, "slot": "class",
 "q": "A patient takes nadolol. How is it classified?",
 "opts": [
  ["Non-selective beta blocker", "Correct. Nadolol is one of the first-generation, non-selective agents, with propranolol, penbutolol, pindolol, sotalol and timolol."],
  ["Beta-1 selective blocker", "The beta-1 selective (second-generation) agents are acebutolol, atenolol, bisoprolol, esmolol and metoprolol. Nadolol is non-selective."],
  ["Alpha-1 and beta blocker", "The agents that add alpha-1 blockade are the third-generation carvedilol and labetalol. Nadolol is a first-generation, non-selective beta blocker."],
  ["Central alpha-2 agonist", "Central alpha-2 agonists are clonidine and guanfacine. Nadolol ends in -lol and is a non-selective beta blocker."]],
 "c": 0, "cite": D + ", Slide 60"},

{"topic": "Beta blocker groups", "io": IO_CLASS, "slot": "class",
 "q": "Which beta blocker is beta-1 selective?",
 "opts": [
  ["Atenolol", "Correct. Atenolol is a second-generation, beta-1 selective agent, alongside acebutolol, bisoprolol, esmolol and metoprolol."],
  ["Propranolol", "Propranolol is first-generation and non-selective, blocking beta-1 and beta-2 receptors alike."],
  ["Nadolol", "Nadolol is a first-generation, non-selective beta blocker. The beta-1 selective choice here is atenolol."],
  ["Timolol", "Timolol is a non-selective, first-generation agent, used in glaucoma and migraine prophylaxis. Atenolol is the beta-1 selective one."]],
 "c": 0, "cite": D + ", Slide 61"},

{"topic": "Beta blocker groups", "io": IO_CLASS, "slot": "class",
 "q": "Which beta blocker also blocks alpha-1 receptors?",
 "opts": [
  ["Carvedilol", "Correct. Carvedilol and labetalol are the third-generation exceptions that add alpha-1 blockade; carvedilol is also antioxidant and antiproliferative."],
  ["Metoprolol", "Metoprolol is a beta-1 selective, second-generation agent without alpha-1 blockade. Carvedilol and labetalol add alpha-1 blockade."],
  ["Atenolol", "Atenolol is beta-1 selective and has no alpha-1 action. The alpha-1 blocking beta blockers are carvedilol and labetalol."],
  ["Propranolol", "Propranolol is non-selective for beta receptors but does not block alpha-1. Carvedilol and labetalol do."]],
 "c": 0, "cite": D + ", Slide 62"},

{"topic": "Beta blocker groups", "io": IO_MOA, "slot": "mechanism",
 "q": "Besides beta blockade, what additional action does labetalol have?",
 "opts": [
  ["Alpha-1 blockade", "Correct. Labetalol is a third-generation agent that blocks alpha-1 receptors and has beta-2 agonist activity, giving direct vasodilation."],
  ["ACE inhibition", "Angiotensin-converting enzyme inhibition belongs to the -pril drugs. Labetalol's extra action is alpha-1 blockade."],
  ["Central alpha-2 stimulation", "Stimulating central alpha-2 receptors is how clonidine works. Labetalol adds peripheral alpha-1 blockade."],
  ["Potassium channel opening", "Opening ATP-modulated potassium channels is minoxidil's mechanism. Labetalol's additional action is alpha-1 blockade."]],
 "c": 0, "cite": D + ", Slide 62"},

{"topic": "Beta blocker agents", "io": IO_ADME, "slot": "class",
 "q": "Which beta-1 selective blocker is given intravenously?",
 "opts": [
  ["Esmolol", "Correct. Esmolol is the second-generation, beta-1 selective agent marked for intravenous use."],
  ["Atenolol", "Atenolol is an oral beta-1 selective agent. The intravenous beta-1 selective blocker is esmolol."],
  ["Bisoprolol", "Bisoprolol is an oral beta-1 selective agent, one of the three used for heart failure. Esmolol is the intravenous one."],
  ["Acebutolol", "Acebutolol is an oral beta-1 selective agent. Esmolol is the beta-1 selective blocker given intravenously."]],
 "c": 0, "cite": D + ", Slide 61"},

# ---- mechanism -----------------------------------------------------------------
{"topic": "Beta blocker mechanism", "io": IO_MOA, "slot": "mechanism",
 "q": "How do beta blockers lower angiotensin II?",
 "opts": [
  ["Blocking renal beta-1 receptors", "Correct. Beta-1 receptors on the juxtaglomerular cells mediate renin release, so blocking them reduces renin and therefore angiotensin II."],
  ["Inhibiting the converting enzyme", "That is the ACE (angiotensin-converting enzyme) inhibitor mechanism. Beta blockers act upstream, by blocking the beta-1 receptors that release renin."],
  ["Blocking the AT1 receptor", "AT1 (angiotensin II type 1) receptor blockade belongs to angiotensin receptor blockers. Beta blockers reduce renin release through beta-1 blockade."],
  ["Blocking lung beta-2 receptors", "Blocking pulmonary beta-2 receptors causes bronchospasm; it does not lower angiotensin II. The renin effect is through beta-1 receptors."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": "Beta blocker mechanism", "io": IO_MOA, "slot": "mechanism",
 "q": "When a non-selective beta blocker is first started, what happens to total peripheral resistance?",
 "opts": [
  ["It rises by reflex", "Correct. Cardiac output falls, so peripheral resistance rises reflexly at first; mean arterial pressure falls only with chronic therapy as the baroreflex adjusts."],
  ["It falls immediately", "Resistance does not fall at first. With cardiac output reduced, total peripheral resistance rises acutely by reflex."],
  ["It does not change", "It does change: the acute fall in cardiac output produces a reflex rise in total peripheral resistance."],
  ["It falls, then rises", "The sequence is the other way: an acute reflex rise, with blood pressure falling only over chronic therapy."]],
 "c": 0, "cite": D + ", Slide 56"},

# ---- indications ------------------------------------------------------------------
{"topic": "Beta blockers in hypertension", "io": IO_PROT, "slot": "drug choice",
 "q": "Where do beta blockers sit in the management of uncomplicated hypertension?",
 "opts": [
  ["Not recommended first line", "Correct. They are not recommended for first-line management; first line is an ACE (angiotensin-converting enzyme) inhibitor or angiotensin receptor blocker, or a dihydropyridine."],
  ["First line for most patients", "Beta blockers are specifically not recommended first line. They are started early only for a compelling indication such as a prior myocardial infarction."],
  ["First line in diabetes", "In diabetes the preferred agent is an ACE inhibitor for its kidney protection; beta blockers can prolong and mask hypoglycemia."],
  ["Only for hypertensive crisis", "Hypertensive crisis is treated with intravenous nitroprusside. Beta blockers are used for chronic hypertension but not as first line."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "Beta blockers in hypertension", "io": IO_IND, "slot": "drug choice",
 "q": "For hypertension, which patient is a beta blocker expected to work best in?",
 "opts": [
  ["A young patient with resting tachycardia", "Correct. They work best in young patients with resting tachycardia, raised catecholamines and raised renin, though fatigue and limited exercise are common complaints."],
  ["An older patient with asthma", "Asthma is where beta blockers cause bronchospasm. The group they work best in is young patients with resting tachycardia and high renin."],
  ["A patient with intermittent claudication", "Claudication worsens with beta-2 blockade of vessels. Beta blockers work best in young patients with resting tachycardia."],
  ["A patient with frequent hypoglycemia", "Beta blockers prolong hypoglycemia and mask its warning signs. They work best in young patients with resting tachycardia."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "Beta blockers in hypertension", "io": IO_PROT, "slot": "drug choice",
 "q": "A 61-year-old with hypertension had a myocardial infarction last year. Which class should generally be used initially?",
 "opts": [
  ["A beta blocker", "Correct. A history of myocardial infarction is a reason to start a beta blocker early; beta blockade protects ischemic myocardium and protects against recurrent infarction."],
  ["An alpha-1 blocker", "Alpha-1 blockers are specialty add-ons with no post-infarction role. After a myocardial infarction a beta blocker is generally used initially."],
  ["Hydralazine", "Hydralazine is contraindicated in coronary artery disease and ischemia because reflex sympathetic activation increases cardiac workload."],
  ["Clonidine", "Clonidine has no post-infarction indication and causes rebound hypertension if stopped. A beta blocker is the initial choice after infarction."]],
 "c": 0, "cite": D + ", Slide 108"},

{"topic": "Beta blocker indications", "io": IO_IND, "slot": "drug choice",
 "q": "Which beta blocker is indicated for heart failure?",
 "opts": [
  ["Bisoprolol", "Correct. The three beta blockers used for heart failure are carvedilol, metoprolol succinate and bisoprolol."],
  ["Propranolol", "Propranolol is a non-selective agent used for migraine prophylaxis; it is not one of the heart failure three (carvedilol, metoprolol succinate, bisoprolol)."],
  ["Atenolol", "Atenolol is beta-1 selective but not one of the heart failure agents. Those are carvedilol, metoprolol succinate and bisoprolol."],
  ["Nadolol", "Nadolol is a non-selective, first-generation agent. The heart failure beta blockers are carvedilol, metoprolol succinate and bisoprolol."]],
 "c": 0, "cite": D + ", Slide 70"},

{"topic": "Beta blocker indications", "io": IO_PROT, "slot": "protocol",
 "q": "How should a beta blocker be started in a patient with heart failure?",
 "opts": [
  ["Very low dose, increased slowly", "Correct. Beta blockers initially worsen heart failure symptoms, so they are started at a very low dose and increased slowly."],
  ["Full dose from the first day", "A full starting dose risks decompensation, because symptoms initially worsen. The approach is a very low dose increased slowly."],
  ["Only once symptoms have gone", "Treatment is not delayed until symptoms resolve. The drug is started at a very low dose and titrated slowly because it first worsens symptoms."],
  ["Intravenously for the first week", "Intravenous loading is not the approach. Heart failure patients start at a very low oral dose that is increased slowly."]],
 "c": 0, "cite": D + ", Slide 70"},

{"topic": "Beta blocker indications", "io": IO_IND, "slot": "indication",
 "q": "Which beta blocker is used for glaucoma?",
 "opts": [
  ["Timolol", "Correct. Timolol reduces production of aqueous humor in the ciliary body; systemic effects from the eye drops are notable."],
  ["Atenolol", "Atenolol is an oral beta-1 selective agent for cardiovascular use. The glaucoma beta blocker here is timolol."],
  ["Esmolol", "Esmolol is the intravenous beta-1 selective agent. Timolol is the one used for glaucoma, where it reduces aqueous humor production."],
  ["Carvedilol", "Carvedilol is a third-generation agent used for heart failure. Timolol is used for glaucoma."]],
 "c": 0, "cite": D + ", Slide 65"},

{"topic": "Beta blocker indications", "io": IO_IND, "slot": "indication",
 "q": "Which beta blocker is used for migraine prophylaxis?",
 "opts": [
  ["Propranolol", "Correct. Propranolol and timolol are used for migraine prophylaxis; the mechanism is uncertain (central or vascular), and low doses are used."],
  ["Esmolol", "Esmolol is an intravenous beta-1 selective agent with no prophylactic role. Propranolol and timolol are used for migraine prevention."],
  ["Labetalol", "Labetalol is a third-generation agent with alpha-1 blockade, not a migraine prophylactic. Propranolol is."],
  ["Bisoprolol", "Bisoprolol is one of the heart failure agents. Migraine prophylaxis uses propranolol or timolol."]],
 "c": 0, "cite": D + ", Slide 65"},

{"topic": "Beta blocker indications", "io": IO_MOA, "slot": "indication",
 "q": "In thyrotoxicosis, beta blockers relieve tachycardia, tremor and anxiety. What additional effect do they have on thyroxine (T4) and triiodothyronine (T3)?",
 "opts": [
  ["Less peripheral T4-to-T3 conversion", "Correct. They reduce the peripheral conversion of thyroxine (T4) to the more active triiodothyronine (T3), besides blunting the adrenergic symptoms."],
  ["Less thyroid hormone synthesis", "Blocking hormone synthesis in the gland is not the effect described. Beta blockers reduce peripheral conversion of thyroxine (T4) to triiodothyronine (T3)."],
  ["More thyroid-stimulating hormone", "Beta blockers are not described as raising thyroid-stimulating hormone. Their extra action is reduced peripheral thyroxine-to-triiodothyronine conversion."],
  ["Less iodine uptake by the gland", "Iodine uptake is not affected by beta blockers. They act peripherally, reducing conversion of thyroxine (T4) to triiodothyronine (T3)."]],
 "c": 0, "cite": D + ", Slide 66"},

{"topic": "Beta blocker indications", "io": IO_MOA, "slot": "indication",
 "q": "How do beta blockers relieve benign essential tremor?",
 "opts": [
  ["Skeletal muscle beta-2 blockade", "Correct. Blocking beta-2 receptors on skeletal muscle is the mechanism given for benign essential tremor; panic attacks respond through sympathetic and central effects."],
  ["Cardiac beta-1 blockade", "Cardiac beta-1 blockade slows the heart but does not explain tremor relief, which comes from blocking skeletal muscle beta-2 receptors."],
  ["Vascular alpha-1 blockade", "Alpha-1 blockade dilates vessels; it is not the tremor mechanism. Beta blockers relieve tremor by blocking beta-2 receptors on skeletal muscle."],
  ["Central alpha-2 stimulation", "Central alpha-2 stimulation is clonidine's mechanism. Tremor relief comes from skeletal muscle beta-2 blockade."]],
 "c": 0, "cite": D + ", Slide 69"},

{"topic": "Beta blocker indications", "io": IO_IND, "slot": "indication",
 "q": "How does beta blockade help a patient with exertional angina?",
 "opts": [
  ["It prolongs time to symptoms", "Correct. By blunting the rise in heart rate and contractility, beta blockade lengthens the time to the angina-provoking heart rate and prolongs exercise time."],
  ["It dilates the coronary arteries", "Coronary dilation is not the mechanism described. Beta blockade lowers oxygen demand, so exercise time before symptoms is prolonged."],
  ["It raises myocardial contractility", "Beta blockade lowers contractility and heart rate, reducing oxygen demand; raising contractility would worsen ischemia."],
  ["It dissolves coronary thrombus", "Beta blockers have no thrombolytic action. They help angina by reducing oxygen demand and prolonging exercise time."]],
 "c": 0, "cite": D + ", Slide 67"},

{"topic": "Beta blocker indications", "io": IO_IND, "slot": "indication",
 "q": "Which is a listed indication for beta blockers?",
 "opts": [
  ["Acute panic attacks", "Correct. Beta blockers help acute panic attacks through sympathetic and central effects; the list also includes glaucoma, migraine prophylaxis, thyrotoxicosis and essential tremor."],
  ["Opiate withdrawal", "Blunting opiate withdrawal is attributed to clonidine's analgesic activity, not beta blockers."],
  ["Hypertensive crisis", "Hypertensive crisis is treated with intravenous nitroprusside. Beta blocker indications include panic attacks and essential tremor."],
  ["Prostatic hyperplasia", "Benign prostatic hyperplasia is treated with alpha-1 blockers such as tamsulosin, terazosin and doxazosin, not beta blockers."]],
 "c": 0, "cite": D + ", Slide 69"},

# ---- adverse effects and education -------------------------------------------------
{"topic": "Beta blocker adverse effects", "io": IO_CONTRA, "slot": "drug choice",
 "q": "A patient with mild asthma needs a beta blocker after a myocardial infarction. Which choice carries the lowest risk of bronchospasm?",
 "opts": [
  ["Metoprolol", "Correct. Bronchospasm is less likely with beta-1 selective agents such as metoprolol, because pulmonary beta-2 receptors are relatively spared."],
  ["Propranolol", "Propranolol is non-selective and blocks pulmonary beta-2 receptors, the mechanism of bronchospasm in asthma."],
  ["Nadolol", "Nadolol is non-selective, so it blocks the airway beta-2 receptors that keep bronchi relaxed. A beta-1 selective agent is safer."],
  ["Timolol", "Timolol is non-selective; even as an eye drop its systemic beta-2 blockade can provoke bronchospasm. Metoprolol is beta-1 selective."]],
 "c": 0, "cite": D + ", Slide 71"},

{"topic": "Beta blocker adverse effects", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Why are beta blockers contraindicated in a patient with COPD (chronic obstructive pulmonary disease) who has bronchospasm?",
 "opts": [
  ["They block airway beta-2 receptors", "Correct. Blocking pulmonary beta-2 receptors reduces bronchial smooth muscle relaxation; about a third of COPD patients develop bronchospasm."],
  ["They cause bradykinin-induced cough", "Bradykinin cough belongs to ACE (angiotensin-converting enzyme) inhibitors. Beta blockers cause bronchospasm by blocking airway beta-2 receptors."],
  ["They cause sodium and water retention", "Fluid retention is not the reason. The problem in lung disease is beta-2 blockade in the airways, which causes bronchospasm."],
  ["They raise blood carbon dioxide", "Carbon dioxide retention is not the described mechanism. Blocking pulmonary beta-2 receptors impairs bronchial relaxation."]],
 "c": 0, "cite": D + ", Slide 71"},

{"topic": "Beta blocker adverse effects", "io": IO_EDU, "slot": "education",
 "q": "A patient with type 1 diabetes is starting propranolol. What should he be told about hypoglycemia?",
 "opts": [
  ["Warning signs may be masked", "Correct. Beta blockers inhibit glycogenolysis, so hypoglycemia lasts longer, and they mask its adrenergic warning symptoms."],
  ["It will become less frequent", "Beta blockers do not protect against hypoglycemia; by inhibiting glycogenolysis they prolong it and hide its warning signs."],
  ["Insulin will no longer be needed", "Beta blockers do not replace insulin. The warning is that hypoglycemia may be prolonged and its symptoms masked."],
  ["Blood sugar will run high only", "In type 2 diabetes reduced insulin can raise glucose, but the danger stressed for any diabetic is prolonged, masked hypoglycemia."]],
 "c": 0, "cite": D + ", Slide 72"},

{"topic": "Beta blocker adverse effects", "io": IO_MOA, "slot": "adverse effect",
 "q": "Why do beta blockers prolong hypoglycemia?",
 "opts": [
  ["They inhibit glycogenolysis", "Correct. Low glucose normally triggers epinephrine-driven glycogenolysis; blocking it slows recovery and masks the symptoms."],
  ["They increase insulin secretion", "Beta blockers reduce rather than increase insulin, which is why glucose can rise in type 2 diabetes. Hypoglycemia is prolonged because glycogenolysis is blocked."],
  ["They block glucose absorption", "Glucose absorption from the gut is not affected. The recovery from a low is slowed because glycogenolysis is inhibited."],
  ["They activate hepatic glucokinase", "Glucokinase is not involved in the described mechanism. Beta blockers prolong hypoglycemia by inhibiting glycogenolysis."]],
 "c": 0, "cite": D + ", Slide 72"},

{"topic": "Beta blocker adverse effects", "io": IO_EDU, "slot": "education",
 "q": "A patient wants to stop his metoprolol abruptly before a trip. What is the danger?",
 "opts": [
  ["Angina, infarction or a pressure surge", "Correct. Sudden withdrawal can cause acute angina, myocardial infarction or a marked rise in blood pressure, so the drug is withdrawn slowly."],
  ["Hypoglycemia, sweating or confusion", "Hypoglycemia is prolonged while taking a beta blocker, not provoked by stopping one. The withdrawal risk is angina, infarction or marked hypertension."],
  ["Bronchospasm, wheeze or cough", "Bronchospasm comes from taking a beta blocker, especially a non-selective one. Stopping abruptly risks angina, infarction or a marked rise in pressure."],
  ["Hyperkalemia, weakness or palpitations", "Potassium is not the withdrawal concern. Abrupt cessation risks acute angina, infarction and a marked rise in blood pressure."]],
 "c": 0, "cite": D + ", Slide 73"},

{"topic": "Beta blocker adverse effects", "io": IO_MOA, "slot": "adverse effect",
 "q": "Why does stopping a beta blocker abruptly provoke a rebound?",
 "opts": [
  ["Receptors upregulate during blockade", "Correct. Chronic blockade upregulates beta receptors, so sudden removal exposes more receptors to catecholamines; the drug is withdrawn slowly."],
  ["Catecholamine synthesis stops", "Catecholamine synthesis does not stop during therapy. The rebound comes from receptors upregulated while they were blocked."],
  ["Renin release is permanently lost", "Renin is suppressed while beta-1 receptors are blocked, not permanently lost. Rebound reflects receptor upregulation."],
  ["The drug has a long half-life", "A long half-life would soften withdrawal, not cause it. The rebound comes from receptor upregulation during blockade."]],
 "c": 0, "cite": D + ", Slide 73"},

{"topic": "Beta blocker adverse effects", "io": IO_AE, "slot": "adverse effect",
 "q": "A patient on propranolol reports cold fingers and calf pain when walking. What is the mechanism?",
 "opts": [
  ["Vascular beta-2 blockade", "Correct. Blocking beta-2 receptors in blood vessels impairs peripheral circulation: cold extremities (Raynaud's phenomenon), muscle fatigue and intermittent claudication."],
  ["Vascular alpha-1 blockade", "Alpha-1 blockade dilates vessels and would warm the extremities; it causes orthostatic hypotension, not cold fingers."],
  ["Cardiac beta-1 stimulation", "Propranolol blocks rather than stimulates beta-1 receptors. The cold extremities come from blocking vascular beta-2 receptors."],
  ["Calcium channel blockade", "Calcium channel blockade dilates arteries rather than constricting them. Impaired peripheral circulation here is a beta-2 blockade effect."]],
 "c": 0, "cite": D + ", Slide 73"},

{"topic": "Beta blocker adverse effects", "io": IO_AE, "slot": "adverse effect",
 "q": "A patient on propranolol develops vivid nightmares and low mood. Which property of the drug explains this?",
 "opts": [
  ["High lipid solubility", "Correct. Highly lipid-soluble beta blockers such as propranolol cause more central effects: depression, nightmares and vivid dreams, hallucinations and fatigue."],
  ["Beta-1 selectivity", "Propranolol is non-selective, and selectivity is not what drives central effects. Lipid solubility determines how much reaches the brain."],
  ["Alpha-1 blockade", "Propranolol does not block alpha-1 receptors; carvedilol and labetalol do. Its central effects come from high lipid solubility."],
  ["Intravenous use", "Propranolol here is oral; the intravenous beta blocker is esmolol. Central effects are linked to high lipid solubility."]],
 "c": 0, "cite": D + ", Slide 74"},

{"topic": "Beta blocker adverse effects", "io": IO_AE, "slot": "adverse effect",
 "q": "Which effect on blood lipids is listed as an adverse effect of beta blockers?",
 "opts": [
  ["Elevated triglycerides", "Correct. Elevated triglycerides are listed among beta blocker adverse effects; by contrast, prazosin mildly lowers triglycerides and raises HDL (high-density lipoprotein)."],
  ["Lowered triglycerides", "The listed effect is the reverse: beta blockers raise triglycerides. The mild triglyceride fall belongs to prazosin."],
  ["Raised HDL cholesterol", "A rise in HDL (high-density lipoprotein) is reported with prazosin, not beta blockers, whose listed lipid effect is raised triglycerides."],
  ["Lowered LDL cholesterol", "Lowering LDL (low-density lipoprotein) is not a beta blocker effect; the listed adverse lipid effect is elevated triglycerides."]],
 "c": 0, "cite": D + ", Slide 74"},

{"topic": "Beta blocker adverse effects", "io": IO_TOX, "slot": "adverse effect",
 "q": "Which conduction problem can beta blockers cause?",
 "opts": [
  ["Atrioventricular block", "Correct. Cardiodepressive effects include bradycardia (heart rate under 60) and first-, second- or third-degree atrioventricular block, as well as negative inotropy and fatigue."],
  ["Reflex tachycardia", "Reflex tachycardia comes from vasodilators such as dihydropyridines and hydralazine. Beta blockers slow the heart and can cause heart block."],
  ["Supraventricular tachycardia", "Supraventricular arrhythmias are an indication: beta blockers block the atrioventricular node and slow transmission. The conduction problem they cause is heart block."],
  ["Ventricular tachycardia", "Beta blockers are cardio-depressive; the conduction effect they cause is atrioventricular block, with bradycardia."]],
 "c": 0, "cite": D + ", Slide 71"},
]
