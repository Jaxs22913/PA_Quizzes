# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- Antihypertensives (Lecture 6), topic 4: alpha-1
blockers, central sympatholytics and direct vasodilators.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

SOURCE. Antihypertensives.pptx slides 76-107. Slides 88 (clonidine pathway) and
98 (vasodilator comparison) are embedded Word objects and were read from their
rendered pictures.

DECK CONTRADICTION RESOLVED: slide 75 calls clonidine an "a2 blocker"; slides 86
and 92 say it stimulates alpha-2 receptors (an agonist). Every key uses the
agonist wording, and the one item that offers "blocks central alpha-2 receptors"
offers it as a distractor whose explanation says why it is wrong.

EMPHASIS (weight only): class identification by suffix ("-zosin"); clonidine and
beta blockers as the drugs never stopped abruptly; hydralazine N-acetylation
("highlight that") and the black-stool warning ("let them know ahead of time");
nitroprusside cyanide and its antidote.

SLIDE WINS: prazosin's reflex tachycardia is "mild" (slide 80), not the
"stronger than dihydropyridines" said aloud; topical minoxidil "may have
cardiovascular effects" (slide 105), not "no blood pressure effects".

SCOPE CAPS: terazosin and doxazosin are asked for class identity and the
class-level uses only ("nothing notable"); no clonidine overdose numbers (the
slide says only "narrow therapeutic range"); no doses.
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

# ---- alpha-1 blockers ------------------------------------------------------------
{"topic": "Alpha-1 blockers", "io": IO_CLASS, "slot": "class",
 "q": "Which of these drugs is an alpha-1 blocker?",
 "opts": [
  ["Doxazosin", "Correct. The -zosin suffix marks the alpha-1 selective antagonists: prazosin, terazosin and doxazosin, with tamsulosin as the alpha-1A selective agent."],
  ["Diltiazem", "Diltiazem is a non-dihydropyridine calcium channel blocker that slows the atrioventricular node. The -zosin suffix identifies alpha-1 blockers."],
  ["Guanfacine", "Guanfacine is a central alpha-2 agonist that reduces sympathetic outflow. Alpha-1 blockers carry the -zosin suffix, as doxazosin does."],
  ["Hydralazine", "Hydralazine is a direct arteriolar vasodilator whose mechanism is not fully clear. Doxazosin is the alpha-1 blocker here."]],
 "c": 0, "cite": D + ", Slide 82"},

{"topic": "Alpha-1 blockers", "io": IO_MOA, "slot": "mechanism",
 "q": "How does prazosin lower blood pressure?",
 "opts": [
  ["Blocks vascular alpha-1 receptors", "Correct. Reversible blockade of vascular alpha-1 receptors dilates precapillary arterioles and lowers total peripheral resistance, with a reflex rise in heart rate."],
  ["Stimulates central alpha-2 receptors", "Central alpha-2 stimulation is how clonidine and guanfacine reduce sympathetic outflow. Prazosin blocks peripheral alpha-1 receptors."],
  ["Opens arteriolar potassium channels", "Opening ATP-modulated potassium channels is minoxidil's mechanism. Prazosin reversibly blocks vascular alpha-1 receptors."],
  ["Blocks cardiac beta-1 receptors", "Beta-1 blockade lowers cardiac output and is the beta blocker mechanism. Prazosin acts on vascular alpha-1 receptors instead."]],
 "c": 0, "cite": D + ", Slide 77"},

{"topic": "Alpha-1 blockers", "io": IO_AE, "slot": "adverse effect",
 "q": "A patient recently started on prazosin feels lightheaded every time he stands up. What is the most likely cause?",
 "opts": [
  ["Orthostatic hypotension", "Correct. Orthostatic hypotension with postural dizziness is the leading prazosin side effect, alongside headache, drowsiness and lack of energy."],
  ["Reflex bradycardia", "Prazosin produces a mild reflex tachycardia, not bradycardia. Dizziness on standing is orthostatic hypotension."],
  ["First-dose hyperkalemia", "Hyperkalemia belongs to ACE (angiotensin-converting enzyme) inhibitors and angiotensin receptor blockers, not prazosin, whose standing dizziness is orthostatic."],
  ["Central sedation", "Drowsiness can occur, but dizziness specifically on standing is orthostatic hypotension from alpha-1 blockade."]],
 "c": 0, "cite": D + ", Slide 79"},

{"topic": "Alpha-1 blockers", "io": IO_INTER, "slot": "interaction",
 "q": "Which drug added to prazosin may enhance its postural hypotension?",
 "opts": [
  ["A beta blocker", "Correct. Beta blockers may enhance prazosin's postural hypotension; NSAIDs (nonsteroidal anti-inflammatory drugs) attenuate its response, and caution is needed in cardiac and renal failure."],
  ["An NSAID", "NSAIDs (nonsteroidal anti-inflammatory drugs) attenuate prazosin's response rather than enhancing its hypotension. Beta blockers enhance postural hypotension."],
  ["A potassium supplement", "Potassium supplements matter with ACE inhibitors and angiotensin receptor blockers. With prazosin, beta blockers enhance postural hypotension."],
  ["A bile acid resin", "Bile acid sequestrants bind oral drugs in the gut and are not the listed prazosin interaction; beta blockers enhance its postural hypotension."]],
 "c": 0, "cite": D + ", Slide 81"},

{"topic": "Alpha-1 blockers", "io": IO_INTER, "slot": "interaction",
 "q": "A patient on prazosin begins daily naproxen. What effect do NSAIDs (nonsteroidal anti-inflammatory drugs) have on prazosin?",
 "opts": [
  ["They attenuate its response", "Correct. NSAIDs attenuate the response to prazosin, as they also reduce the effect of ACE (angiotensin-converting enzyme) inhibitors."],
  ["They enhance its hypotension", "Enhanced postural hypotension is the beta blocker interaction. NSAIDs attenuate prazosin's response."],
  ["They raise its blood levels", "No pharmacokinetic rise is described. The listed interaction is that NSAIDs attenuate prazosin's blood pressure response."],
  ["They have no interaction", "There is a listed interaction: NSAIDs attenuate the response to prazosin."]],
 "c": 0, "cite": D + ", Slide 81"},

{"topic": "Alpha-1 blockers", "io": IO_AE, "slot": "adverse effect",
 "q": "Which effect on blood lipids has been reported with prazosin?",
 "opts": [
  ["A mild rise in HDL", "Correct. Prazosin shows evidence of a mild reduction in LDL (low-density lipoprotein) and triglycerides and increased HDL (high-density lipoprotein)."],
  ["A rise in triglycerides", "Raised triglycerides are listed as a beta blocker adverse effect. Prazosin mildly lowers triglycerides and LDL (low-density lipoprotein)."],
  ["A rise in LDL", "Prazosin is reported to mildly reduce LDL (low-density lipoprotein), not raise it, while increasing HDL (high-density lipoprotein)."],
  ["A large fall in HDL", "The reported change is a mild increase in HDL (high-density lipoprotein), not a fall."]],
 "c": 0, "cite": D + ", Slide 78"},

{"topic": "Alpha-1 blockers", "io": IO_AE, "slot": "adverse effect",
 "q": "How is the reflex tachycardia seen with prazosin described?",
 "opts": [
  ["Mild", "Correct. Prazosin causes only mild reflex tachycardia, possibly because of some central sympatholytic activity and because it dilates both arteries and veins."],
  ["Marked, like minoxidil", "Minoxidil's reflex effects are the most severe (cardiac output up 2 to 3 times). Prazosin's reflex tachycardia is mild."],
  ["Absent altogether", "It is present but mild. Prazosin lowers peripheral resistance and triggers a mild reflex rise in heart rate."],
  ["Severe and dose limiting", "It is described as mild, not severe or dose limiting; the dose-limiting problem is orthostatic hypotension."]],
 "c": 0, "cite": D + ", Slide 80"},

{"topic": "Alpha-1 blockers", "io": IO_MOA, "slot": "mechanism",
 "q": "Why does tamsulosin have limited effects on blood pressure?",
 "opts": [
  ["It is alpha-1A selective", "Correct. Tamsulosin selectively blocks alpha-1A receptors of the prostate, whereas vascular receptors are alpha-1B, so vascular effects are limited."],
  ["It does not reach the blood", "Tamsulosin is absorbed and reaches the circulation. Its vascular sparing comes from alpha-1A selectivity."],
  ["It blocks beta-1 receptors too", "Tamsulosin has no beta-1 blocking action. Its limited effect on blood pressure reflects selectivity for alpha-1A receptors."],
  ["It is an alpha-2 agonist", "Tamsulosin is an alpha-1A selective antagonist, not an alpha-2 agonist like clonidine."]],
 "c": 0, "cite": D + ", Slide 84"},

{"topic": "Alpha-1 blockers", "io": IO_IND, "slot": "drug choice",
 "q": "A 68-year-old man has benign prostatic hyperplasia and hypertension. Which single drug treats both?",
 "opts": [
  ["Terazosin", "Correct. The other alpha-1 selective agents, terazosin and doxazosin, are used both as antihypertensives and for benign prostatic hyperplasia."],
  ["Tamsulosin", "Tamsulosin treats benign prostatic hyperplasia but has limited vascular effects because it is alpha-1A selective, so it is not the antihypertensive choice."],
  ["Clonidine", "Clonidine lowers blood pressure centrally but has no prostate indication. Terazosin treats both conditions."],
  ["Amlodipine", "Amlodipine treats hypertension and angina but not prostatic hyperplasia. An alpha-1 blocker such as terazosin treats both."]],
 "c": 0, "cite": D + ", Slide 83"},

# ---- central sympatholytics ------------------------------------------------------
{"topic": "Central sympatholytics", "io": IO_MOA, "slot": "mechanism",
 "q": "How does clonidine lower blood pressure?",
 "opts": [
  ["Stimulates central alpha-2 receptors", "Correct. Clonidine is an alpha-2 and imidazoline agonist; stimulating central alpha-2A receptors inhibits sympathetic outflow and increases parasympathetic activity."],
  ["Blocks central alpha-2 receptors", "Clonidine activates rather than blocks these receptors; it is an alpha-2 agonist, and stimulation is what reduces sympathetic outflow."],
  ["Blocks vascular alpha-1 receptors", "Peripheral alpha-1 blockade is the prazosin mechanism. Clonidine acts centrally by stimulating alpha-2 receptors."],
  ["Blocks renal beta-1 receptors", "Blocking beta-1 receptors to reduce renin is a beta blocker action. Clonidine stimulates central alpha-2 receptors."]],
 "c": 0, "cite": D + ", Slide 92"},

{"topic": "Central sympatholytics", "io": IO_EDU, "slot": "education",
 "q": "A patient on clonidine runs out of tablets over a long weekend. What is the main danger?",
 "opts": [
  ["Rebound hypertension", "Correct. Abrupt withdrawal hypertension is a class side effect, and clonidine withdrawal reactions may be severe, so the drug must not be stopped suddenly."],
  ["Profound bradycardia", "Bradycardia occurs while taking clonidine. Stopping it abruptly does the opposite: blood pressure rebounds sharply."],
  ["Prolonged hypoglycemia", "Clonidine raises rather than lowers blood glucose, and stopping it does not cause hypoglycemia. The danger is rebound hypertension."],
  ["Marked hyperkalemia", "Potassium is not the withdrawal risk. Sudden cessation of clonidine causes rebound hypertension."]],
 "c": 0, "cite": D + ", Slide 94"},

{"topic": "Central sympatholytics", "io": IO_INTER, "slot": "interaction",
 "q": "A patient takes clonidine together with a beta blocker. What happens to blood pressure if the clonidine is stopped abruptly?",
 "opts": [
  ["It rises sharply", "Correct. While both are taken they lower pressure together, but abrupt clonidine withdrawal in this combination produces a dramatic rise in blood pressure."],
  ["It falls sharply", "The fall in pressure is what the two drugs do together. Abrupt clonidine withdrawal makes blood pressure rise dramatically."],
  ["It stays the same", "The beta blocker does not protect against clonidine withdrawal; blood pressure rises dramatically."],
  ["It rises only slightly", "The listed effect is a marked rise, not a slight one, which is why clonidine is never stopped abruptly."]],
 "c": 0, "cite": D + ", Slide 75"},

{"topic": "Central sympatholytics", "io": IO_AE, "slot": "adverse effect",
 "q": "Which pair of side effects is typical of central sympatholytics?",
 "opts": [
  ["Sedation and dry mouth", "Correct. Drowsiness or sedation and dry mouth are central effects; sexual dysfunction, a narrow therapeutic range and abrupt withdrawal hypertension complete the list."],
  ["Cough and angioedema", "Cough and angioedema are bradykinin effects of ACE (angiotensin-converting enzyme) inhibitors, not central sympatholytics."],
  ["Flushing and tachycardia", "Flushing with reflex tachycardia belongs to vasodilators such as dihydropyridines and hydralazine. Central agents cause sedation and dry mouth."],
  ["Hair growth and edema", "Hypertrichosis with fluid retention points to minoxidil. The central sympatholytic pair is sedation and dry mouth."]],
 "c": 0, "cite": D + ", Slide 91"},

{"topic": "Central sympatholytics", "io": IO_AE, "slot": "adverse effect",
 "q": "Why is clonidine often given with a diuretic?",
 "opts": [
  ["It causes sodium retention", "Correct. Clonidine causes sodium retention, so it is often given with a diuretic; it also decreases antidiuretic hormone (vasopressin) secretion."],
  ["It causes hyperkalemia", "Hyperkalemia is an ACE (angiotensin-converting enzyme) inhibitor and angiotensin receptor blocker concern. Clonidine is paired with a diuretic because it retains sodium."],
  ["It raises renin sharply", "Raised renin is a feature of direct vasodilators and prazosin. Clonidine is combined with a diuretic because it causes sodium retention."],
  ["It causes rebound edema", "No rebound edema is described. The reason for the diuretic is that clonidine causes sodium retention."]],
 "c": 0, "cite": D + ", Slide 93"},

{"topic": "Central sympatholytics", "io": IO_IND, "slot": "indication",
 "q": "Clonidine has analgesic activity. What additional use does this support?",
 "opts": [
  ["Blunting opiate withdrawal", "Correct. Clonidine's analgesic activity blunts opiate withdrawal reactions."],
  ["Migraine prophylaxis", "Migraine prophylaxis is an indication for propranolol, timolol and calcium channel blockers. Clonidine's extra use is blunting opiate withdrawal."],
  ["Prostatic hyperplasia", "Benign prostatic hyperplasia is treated with alpha-1 blockers such as tamsulosin. Clonidine blunts opiate withdrawal reactions."],
  ["Essential tremor", "Benign essential tremor responds to beta blockers through skeletal muscle beta-2 blockade. Clonidine's extra use is opiate withdrawal."]],
 "c": 0, "cite": D + ", Slide 93"},

{"topic": "Central sympatholytics", "io": IO_AE, "slot": "adverse effect",
 "q": "What effect does clonidine have on blood glucose?",
 "opts": [
  ["It raises it", "Correct. Clonidine increases blood glucose by inhibiting insulin secretion."],
  ["It lowers it", "The direction is the reverse: clonidine inhibits insulin secretion, so blood glucose rises."],
  ["It masks lows only", "Masking hypoglycemic warning signs is a beta blocker effect. Clonidine raises blood glucose by inhibiting insulin secretion."],
  ["It has no effect", "It does affect glucose: by inhibiting insulin secretion, clonidine raises blood glucose."]],
 "c": 0, "cite": D + ", Slide 92"},

{"topic": "Central sympatholytics", "io": IO_CLASS, "slot": "class",
 "q": "How does guanfacine compare with clonidine?",
 "opts": [
  ["Less sedation", "Correct. Guanfacine is less potent but the most selective (alpha-2 far more than alpha-1), causes less sedation, and has only an occasional withdrawal syndrome."],
  ["More potent", "Guanfacine is less potent than clonidine. Its advantages are greater alpha-2 selectivity and less sedation."],
  ["Less alpha-2 selective", "Guanfacine is the most selective for alpha-2 over alpha-1 receptors, not less selective."],
  ["More withdrawal", "Guanfacine has only an occasional withdrawal syndrome, whereas clonidine withdrawal reactions may be severe."]],
 "c": 0, "cite": D + ", Slide 95"},

{"topic": "Central sympatholytics", "io": IO_IND, "slot": "indication",
 "q": "Which is listed as an advantage of central sympatholytics?",
 "opts": [
  ["No negative effect on lipids", "Correct. Advantages include no negative effects on lipids, efficacy independent of age, race and gender, suitability for monotherapy, and good effect in the elderly."],
  ["No sedation at all", "Sedation is a typical side effect of the class, along with dry mouth. The lipid-neutral profile is an advantage."],
  ["No withdrawal reactions", "Abrupt withdrawal hypertension is a class side effect. The advantage is that they have no negative effects on lipids."],
  ["A wide therapeutic range", "The class has a narrow therapeutic range, which is listed as a side effect, not an advantage."]],
 "c": 0, "cite": D + ", Slide 90"},

# ---- direct vasodilators -------------------------------------------------------------
{"topic": "Direct vasodilators", "io": IO_MOA, "slot": "mechanism",
 "q": "Why do direct vasodilators lose their effect over time when used alone?",
 "opts": [
  ["Reflex responses cause tachyphylaxis", "Correct. Arteriolar dilation triggers reflex sympathetic activation (tachycardia, higher cardiac output, fluid retention, raised renin), producing tachyphylaxis."],
  ["They induce their own metabolism", "Enzyme induction is not the explanation. The loss of effect is tachyphylaxis from reflex sympathetic activation."],
  ["They block their own receptor", "They do not act by receptor blockade. Reflex tachycardia, fluid retention and raised renin blunt the effect."],
  ["They cause hypokalemia", "Potassium loss is not the reason. Reflex sympathetic activation and fluid retention cause tachyphylaxis."]],
 "c": 0, "cite": D + ", Slide 97"},

{"topic": "Direct vasodilators", "io": IO_PROT, "slot": "protocol",
 "q": "Hydralazine for chronic hypertension is combined with a beta blocker and a diuretic. What is the reason?",
 "opts": [
  ["To offset reflex tachycardia and fluid", "Correct. Direct vasodilators trigger reflex tachycardia, higher cardiac output, fluid retention and raised renin, which the beta blocker and diuretic counter."],
  ["To prevent hydralazine lupus syndrome", "Lupus syndrome risk depends on dose, duration, sex and acetylator status, not on co-therapy. The partners counter reflex tachycardia and fluid retention."],
  ["To slow its hepatic acetylation", "Neither partner changes N-acetylation. They are there to counter the reflex tachycardia and fluid retention hydralazine provokes."],
  ["To block its cyanide metabolite", "Cyanide is a nitroprusside metabolite, not a hydralazine one. The partners counter reflex tachycardia and fluid retention."]],
 "c": 0, "cite": D + ", Slide 99"},

{"topic": "Hydralazine", "io": IO_MOA, "slot": "mechanism",
 "q": "Which statement about hydralazine's mechanism of action is accurate?",
 "opts": [
  ["It is not fully understood", "Correct. The mechanism is not clear; proposed actions include increased cyclic GMP (via nitric oxide), renal prostaglandins and interference with calcium movement."],
  ["It opens potassium channels", "Opening ATP-modulated potassium channels is minoxidil's mechanism. Hydralazine's mechanism is not clear."],
  ["It releases nitric oxide and cyanide", "Nitric oxide with bound cyanide describes nitroprusside. Hydralazine's mechanism remains unclear."],
  ["It blocks alpha-1 receptors", "Alpha-1 blockade is the prazosin mechanism. Hydralazine acts directly on arterioles by a mechanism that is not clear."]],
 "c": 0, "cite": D + ", Slide 100"},

{"topic": "Hydralazine", "io": IO_ADME, "slot": "adverse effect",
 "q": "Hydralazine is N-acetylated in the liver. Which patients are at higher risk of its lupus syndrome?",
 "opts": [
  ["Slow acetylators", "Correct. Slow acetylators clear hydralazine more slowly; with high doses, long-term use, female sex and Caucasian ancestry, this raises the risk of lupus syndrome."],
  ["Fast acetylators", "Fast acetylators clear the drug quickly. The listed risk factor for hydralazine lupus is being a slow acetylator."],
  ["Patients on low doses", "Low doses are protective; high doses are the risk factor, along with long-term use and slow acetylation."],
  ["Patients on short courses", "Short-term use is not a risk factor; long-term therapy is, together with high dose and slow acetylation."]],
 "c": 0, "cite": D + ", Slide 101"},

{"topic": "Hydralazine", "io": IO_TOX, "slot": "adverse effect",
 "q": "Which patient is at greatest risk of hydralazine lupus syndrome?",
 "opts": [
  ["A woman on high doses long term", "Correct. The risk factors are high dose, long-term therapy, female sex, slow acetylator status and Caucasian ancestry."],
  ["A man on a short low-dose course", "Male sex, short courses and low doses are the opposite of the listed risk factors: high dose, long term, women and slow acetylators."],
  ["A fast acetylator on low doses", "Fast acetylators on low doses are at the lowest risk. High dose, long-term use and slow acetylation raise it."],
  ["A child on a single dose", "A single dose does not carry the risk. Lupus syndrome follows high-dose, long-term use, especially in women and slow acetylators."]],
 "c": 0, "cite": D + ", Slide 101"},

{"topic": "Hydralazine", "io": IO_EDU, "slot": "education",
 "q": "What should a patient starting hydralazine be told about stool color?",
 "opts": [
  ["Stools may turn black", "Correct. Stools may turn black on hydralazine, so the patient is warned ahead of time rather than being alarmed by it."],
  ["Stools may turn orange", "Orange discoloration is not listed for hydralazine. The warning is that stools may turn black."],
  ["Stools may turn pale", "Pale stools are not a listed hydralazine effect. Patients are told their stools may turn black."],
  ["Stools will not change", "Stool color can change: patients should be warned that stools may turn black."]],
 "c": 0, "cite": D + ", Slide 102"},

{"topic": "Hydralazine", "io": IO_CONTRA, "slot": "contraindication",
 "q": "In which patient is hydralazine contraindicated?",
 "opts": [
  ["An older adult with coronary disease", "Correct. Hydralazine is contraindicated in coronary artery disease, the elderly and ischemia, because vasodilation with reflex sympathetic activation raises cardiac workload."],
  ["A young adult with severe hypertension", "Chronic or severe hypertension is where hydralazine is used, with a diuretic and a beta blocker. The contraindication is coronary disease in the elderly."],
  ["A patient already taking a diuretic", "A diuretic is a recommended partner, not a contraindication. Hydralazine is contraindicated in coronary artery disease and ischemia."],
  ["A patient already on a beta blocker", "A beta blocker is a recommended partner that blunts the reflex tachycardia. The contraindications are coronary disease, older age and ischemia."]],
 "c": 0, "cite": D + ", Slide 102"},

{"topic": "Minoxidil", "io": IO_MOA, "slot": "mechanism",
 "q": "How does minoxidil relax arteriolar smooth muscle?",
 "opts": [
  ["Opens ATP-modulated potassium channels", "Correct. Increased potassium efflux hyperpolarizes the cell and relaxes the muscle; its action on potassium channels also causes arrhythmias."],
  ["Raises nitric oxide and cyclic GMP", "Nitric oxide activating cyclic GMP is nitroprusside's mechanism (and a proposed one for hydralazine). Minoxidil opens potassium channels."],
  ["Blocks L-type calcium channels", "L-type calcium channel blockade is the calcium channel blocker mechanism. Minoxidil hyperpolarizes cells by opening potassium channels."],
  ["Blocks vascular alpha-1 receptors", "Alpha-1 blockade is prazosin's mechanism. Minoxidil opens ATP-modulated potassium channels."]],
 "c": 0, "cite": D + ", Slide 103"},

{"topic": "Minoxidil", "io": IO_AE, "slot": "adverse effect",
 "q": "Which adverse effect is characteristic of oral minoxidil?",
 "opts": [
  ["Hypertrichosis", "Correct. Oral minoxidil causes hair growth on the face, back, arms and legs; it also causes myocardial ischemia and arrhythmias."],
  ["Lupus syndrome", "Drug-induced lupus syndrome belongs to hydralazine, especially in slow acetylators. Minoxidil's characteristic effect is hypertrichosis."],
  ["Cyanide toxicity", "Cyanide toxicity comes from nitroprusside infusion. Minoxidil causes hypertrichosis."],
  ["Dry cough", "A dry cough from bradykinin is an ACE (angiotensin-converting enzyme) inhibitor effect. Minoxidil's hallmark is hypertrichosis."]],
 "c": 0, "cite": D + ", Slide 105"},

{"topic": "Minoxidil", "io": IO_IND, "slot": "indication",
 "q": "When is oral minoxidil used for hypertension?",
 "opts": [
  ["Severe or refractory hypertension", "Correct. Minoxidil is used in triple therapy, with a diuretic and a beta blocker, for severe or refractory hypertension."],
  ["Hypertensive crisis by infusion", "The crisis agent given by intravenous infusion is nitroprusside. Minoxidil is an oral triple-therapy agent for severe or refractory hypertension."],
  ["First line in young patients", "Minoxidil is never first line; the first-line agents are ACE inhibitors or angiotensin receptor blockers and dihydropyridines."],
  ["Hypertension in pregnancy", "Pregnancy is not its listed use. Minoxidil is reserved for severe or refractory hypertension as part of triple therapy."]],
 "c": 0, "cite": D + ", Slide 99"},

{"topic": "Minoxidil", "io": IO_EDU, "slot": "education",
 "q": "A patient using topical minoxidil (Rogaine) for hair growth asks whether it can affect the heart. What is accurate?",
 "opts": [
  ["It may have cardiovascular effects", "Correct. The topical form is used for hair growth, and it may have cardiovascular effects, so the question is a fair one."],
  ["It cannot reach the circulation", "It is not described as entirely local. Topical minoxidil may have cardiovascular effects."],
  ["It only acts on scalp arteries", "Its effects are not described as confined to the scalp; the topical form may have cardiovascular effects."],
  ["It lowers blood pressure reliably", "It is not used as an antihypertensive. The caution is simply that the topical form may have cardiovascular effects."]],
 "c": 0, "cite": D + ", Slide 105"},

{"topic": "Nitroprusside", "io": IO_IND, "slot": "drug choice",
 "q": "Which drug is given by intravenous infusion for hypertensive crisis?",
 "opts": [
  ["Nitroprusside", "Correct. Nitroprusside is the hypertensive crisis agent, given by intravenous infusion; it dilates both veins and arterioles."],
  ["Hydralazine", "Hydralazine is listed for chronic hypertension with a diuretic and a beta blocker. Nitroprusside is the crisis infusion."],
  ["Minoxidil", "Minoxidil is an oral agent for severe or refractory chronic hypertension. The crisis infusion is nitroprusside."],
  ["Clonidine", "Clonidine is an oral central sympatholytic for chronic hypertension. Nitroprusside is given by infusion in a crisis."]],
 "c": 0, "cite": D + ", Slide 99"},

{"topic": "Nitroprusside", "io": IO_MOA, "slot": "mechanism",
 "q": "Which vessels does nitroprusside dilate?",
 "opts": [
  ["Veins and arterioles", "Correct. Nitric oxide released from nitroprusside activates cyclic GMP and lowers intracellular calcium in both veins and arterioles."],
  ["Arterioles only", "Arteriole-only dilation describes hydralazine and minoxidil. Nitroprusside acts on veins as well as arterioles."],
  ["Veins only", "Nitroprusside dilates arterioles as well as veins; it is not a venous-only agent."],
  ["Coronary arteries only", "Its action is not limited to the coronaries: nitroprusside dilates veins and arterioles generally."]],
 "c": 0, "cite": D + ", Slide 106"},

{"topic": "Nitroprusside", "io": IO_TOX, "slot": "adverse effect",
 "q": "During a nitroprusside infusion, a patient develops trembling, vomiting and convulsions. Sodium thiosulfate is given. Which toxicity does it limit?",
 "opts": [
  ["Cyanide toxicity", "Correct. Each nitroprusside molecule carries five cyanide groups; cyanide toxicity causes trembling, vomiting and convulsions, and sodium thiosulfate limits it."],
  ["Thiocyanate toxicity", "Thiocyanate toxicity causes weakness, anoxia, tinnitus, muscle spasms and toxic psychosis with long infusions or renal failure; thiosulfate is given for cyanide."],
  ["Lupus syndrome", "Lupus syndrome is a hydralazine toxicity of long-term, high-dose use. The infusion toxicity that thiosulfate limits is cyanide."],
  ["Hyperkalemia", "Hyperkalemia is not a nitroprusside toxicity. Sodium thiosulfate is given to limit cyanide toxicity."]],
 "c": 0, "cite": D + ", Slide 107"},

{"topic": "Nitroprusside", "io": IO_TOX, "slot": "adverse effect",
 "q": "When is thiocyanate toxicity most likely during nitroprusside therapy?",
 "opts": [
  ["Long infusions or renal failure", "Correct. Thiocyanate accumulates with long-term infusions or renal failure, causing weakness, anoxia, tinnitus, muscle spasms and toxic psychosis."],
  ["The first minutes of infusion", "Early toxicity is not thiocyanate. It accumulates with long infusions or in renal failure."],
  ["Only in slow acetylators", "Acetylator status matters for hydralazine, not nitroprusside. Thiocyanate builds up with long infusions or renal failure."],
  ["Only after oral dosing", "Nitroprusside is given by intravenous infusion. Thiocyanate toxicity follows long infusions or renal failure."]],
 "c": 0, "cite": D + ", Slide 107"},
]
