# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- Antihypertensives (Lecture 6), topic 1: RAAS
inhibitors and the first-line choice.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. A key that
carries the whole fact while the distractors stay terse is guessable by length
([[distractor_style_matching]]); the target is under 10 per cent per file.

SOURCE. Antihypertensives.pptx only (slides 3-30 and the algorithm on 108). The
recording set the weighting, never a keyed fact:
  * potassium is the strongest single exam cue of the two lectures, so the
    hyperkalemia risk groups get several items (slides 20, 29);
  * ACE inhibitor against angiotensin receptor blocker -- cough, angioedema,
    the switch -- was called "great for test questions" (slides 19, 22, 26, 30);
  * the algorithm question shape is "the patient is on this, what next" or
    "this comorbidity, what to start" (slide 108, slide 16).

DECK PROBLEMS RESOLVED BEFORE WRITING
  * Slide 7 prints the macula densa line without its "decreased" arrow. No item
    asks the sodium/chloride direction (pending Jaxon).
  * Pregnancy is keyed to the slide wording (2nd and 3rd trimesters), never to
    the "category X" said aloud.
  * The NSAID interaction is keyed to the slide's prostaglandin/bradykinin
    wording, never the renin explanation given aloud.

SCOPE CAPS (said aloud, respected): no prodrug exceptions, no elimination
routes (fosinopril, renal-plus-bile), nothing on AT2, no doses. Diuretics are
Lecture 9 / Exam 3: they appear only as the algorithm's add-on step and the
two on-slide combination facts (slides 28, 29).
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

# ---- class identification -------------------------------------------------
{"topic": "ACE inhibitors", "io": IO_CLASS, "slot": "class",
 "q": "A patient's medication list includes ramipril. To which drug class does it belong?",
 "opts": [
  ["ACE inhibitors", "Correct. The -pril suffix marks an ACE (angiotensin-converting enzyme) inhibitor; ramipril sits alongside lisinopril, enalapril, benazepril and quinapril."],
  ["Angiotensin receptor blockers", "Angiotensin receptor blockers end in -sartan (losartan, valsartan). A -pril ending identifies an angiotensin-converting enzyme inhibitor instead."],
  ["Dihydropyridine blockers", "Dihydropyridine calcium channel blockers end in -dipine (amlodipine, nifedipine). Ramipril's -pril ending marks an ACE inhibitor."],
  ["Beta blockers", "Beta blockers end in -lol (metoprolol, atenolol). The -pril suffix belongs to the angiotensin-converting enzyme inhibitors."]],
 "c": 0, "cite": D + ", Slide 14"},

{"topic": "Angiotensin receptor blockers", "io": IO_CLASS, "slot": "class",
 "q": "Which of these drugs is an angiotensin receptor blocker?",
 "opts": [
  ["Valsartan", "Correct. The -sartan suffix identifies an angiotensin receptor blocker, the same family as losartan, candesartan, irbesartan and telmisartan."],
  ["Benazepril", "Benazepril is an angiotensin-converting enzyme inhibitor (-pril). It lowers angiotensin II production rather than blocking its receptor."],
  ["Nisoldipine", "Nisoldipine is a dihydropyridine calcium channel blocker (-dipine) approved for hypertension, not a blocker of angiotensin receptors."],
  ["Nadolol", "Nadolol is a non-selective beta blocker (-lol). Angiotensin receptor blockers carry the -sartan suffix, as valsartan does."]],
 "c": 0, "cite": D + ", Slide 27"},

# ---- mechanism --------------------------------------------------------------
{"topic": "ACE inhibitors", "io": IO_MOA, "slot": "mechanism",
 "q": "Besides lowering angiotensin II, what does blocking angiotensin-converting enzyme do to bradykinin?",
 "opts": [
  ["Slows its breakdown", "Correct. The same enzyme that makes angiotensin II also inactivates bradykinin, so bradykinin accumulates -- the root of both the dry cough and angioedema."],
  ["Speeds its breakdown", "The reverse. Angiotensin-converting enzyme normally inactivates bradykinin, so blocking the enzyme lets bradykinin build up rather than clearing it faster."],
  ["Blocks its receptor", "ACE inhibitors do not act on a bradykinin receptor. They stop the enzyme that degrades bradykinin, so its level rises."],
  ["Leaves it unchanged", "Bradykinin is directly affected: the enzyme that is blocked is the one that breaks it down, so bradykinin accumulates."]],
 "c": 0, "cite": D + ", Slide 11"},

{"topic": "Angiotensin receptor blockers", "io": IO_MOA, "slot": "mechanism",
 "q": "How do angiotensin receptor blockers lower blood pressure?",
 "opts": [
  ["By blocking AT1 receptors", "Correct. They bind the AT1 (angiotensin II type 1) receptor with high affinity and dissociate slowly, giving sustained blockade: vasodilation, less aldosterone and less sodium reabsorption."],
  ["By inhibiting renin release", "Reduced renin release is how beta blockers lower angiotensin II (beta-1 blockade at the kidney). Angiotensin receptor blockers act at the AT1 receptor itself."],
  ["By inhibiting the converting enzyme", "That is the ACE inhibitor mechanism. Angiotensin receptor blockers leave angiotensin II production alone and block its AT1 receptor instead."],
  ["By stimulating central alpha-2 sites", "Central alpha-2 stimulation is how clonidine and guanfacine work. Angiotensin receptor blockers act peripherally at the AT1 receptor."]],
 "c": 0, "cite": D + ", Slide 25"},

{"topic": "Angiotensin receptor blockers", "io": IO_MOA, "slot": "mechanism",
 "q": "Why can angiotensin II still be produced in a patient taking an ACE (angiotensin-converting enzyme) inhibitor?",
 "opts": [
  ["Other enzymes such as chymase", "Correct. Trypsin, cathepsin and chymase provide alternative routes to angiotensin II -- the limiting factor of ACE inhibitors that angiotensin receptor blockers get around."],
  ["Renin makes it directly", "Renin cleaves angiotensinogen to angiotensin I; it does not make angiotensin II. The escape route is other enzymes such as chymase, trypsin and cathepsin."],
  ["The adrenal gland secretes it", "The adrenal cortex responds to angiotensin II by releasing aldosterone; it is not a source of angiotensin II. Chymase and similar enzymes are."],
  ["Bradykinin converts into it", "Bradykinin is degraded to inactive products, not converted to angiotensin II. The alternative production comes from chymase, trypsin and cathepsin."]],
 "c": 0, "cite": D + ", Slide 23"},

{"topic": "Renin-angiotensin system", "io": IO_MOA, "slot": "mechanism",
 "q": "Which action belongs to angiotensin II?",
 "opts": [
  ["Stimulating aldosterone secretion", "Correct. Angiotensin II also constricts arterioles and renal vessels, raises sympathetic outflow, and stimulates thirst and antidiuretic hormone release."],
  ["Stimulating renin release", "Angiotensin II inhibits renin release as negative feedback. That is why blocking its production lets renin and angiotensin I rise."],
  ["Dilating renal arterioles", "Angiotensin II causes renal vasoconstriction. Renal vasodilation is what the angiotensin receptor blockers produce by blocking it."],
  ["Suppressing thirst centrally", "The reverse: angiotensin II stimulates thirst, sodium appetite and antidiuretic hormone secretion through its central actions."]],
 "c": 0, "cite": D + ", Slide 8"},

{"topic": "Renin-angiotensin system", "io": IO_MOA, "slot": "mechanism",
 "q": "What happens to renin release when renal perfusion falls?",
 "opts": [
  ["It increases", "Correct. The renal baroreceptor responds to stretch of the afferent arteriole: less perfusion, more renin. Sympathetic activity at beta-1 receptors raises it too."],
  ["It decreases", "Falling renal perfusion is sensed by the renal baroreceptor as reduced stretch of the afferent arteriole, and renin release rises rather than falls."],
  ["It stays constant", "Renin release is actively controlled; the renal baroreceptor raises it when afferent arteriolar stretch falls with poor perfusion."],
  ["It stops completely", "Low renal perfusion is one of the main stimuli for renin release. The renal baroreceptor increases secretion when the afferent arteriole is less stretched."]],
 "c": 0, "cite": D + ", Slide 7"},

# ---- indications ------------------------------------------------------------
{"topic": "ACE inhibitors", "io": IO_IND, "slot": "indication",
 "q": "A 52-year-old with type 2 diabetes and newly diagnosed hypertension needs a first agent. Which class is preferred for its kidney-protective effect?",
 "opts": [
  ["An ACE inhibitor", "Correct. ACE (angiotensin-converting enzyme) inhibitors are preferred in diabetics because they lower glomerular pressure and slow diabetic nephropathy; an angiotensin receptor blocker is the equivalent choice."],
  ["A beta blocker", "Beta blockers are not first line for hypertension and can mask or prolong hypoglycemia in a diabetic. The kidney-protective choice is an ACE inhibitor."],
  ["An alpha-1 blocker", "Prazosin and its relatives are add-on or prostate agents, not the preferred first choice in diabetes. ACE inhibitors carry the kidney protection."],
  ["A direct vasodilator", "Hydralazine and minoxidil are reserved for severe or resistant hypertension with other agents. The diabetic's first choice is an ACE inhibitor."]],
 "c": 0, "cite": D + ", Slide 16"},

{"topic": "ACE inhibitors", "io": IO_IND, "slot": "indication",
 "q": "Which statement describes ACE (angiotensin-converting enzyme) inhibitors in left ventricular dysfunction?",
 "opts": [
  ["Give to all unless contraindicated", "Correct. They reduce remodeling, afterload and preload, delay progression of heart failure, and reduce myocardial infarction and hospitalization."],
  ["Avoid, as they worsen remodeling", "ACE inhibitors reduce ventricular remodeling and hypertrophy rather than worsening them; they should be given to all with left ventricular dysfunction unless contraindicated."],
  ["Use only after beta blockers fail", "They are not held in reserve. The recommendation is that every patient with left ventricular dysfunction receives one unless it is contraindicated."],
  ["Use only when blood pressure is high", "The benefit in left ventricular dysfunction is not limited to hypertension: reduced afterload and remodeling help regardless, so all should receive one unless contraindicated."]],
 "c": 0, "cite": D + ", Slide 17"},

{"topic": "ACE inhibitors", "io": IO_IND, "slot": "indication",
 "q": "What benefit do ACE (angiotensin-converting enzyme) inhibitors provide when given after a myocardial infarction?",
 "opts": [
  ["Less remodeling, lower mortality", "Correct. After infarction they reduce myocardial remodeling and lower overall mortality; angiotensin II otherwise drives hypertrophy and remodeling."],
  ["Dissolution of the thrombus", "ACE inhibitors have no thrombolytic action. Their post-infarction benefit is reduced myocardial remodeling and lower overall mortality."],
  ["Faster heart rate recovery", "They do not act to speed the heart. After infarction the benefit is less remodeling of the damaged myocardium and reduced mortality."],
  ["Prevention of reflex tachycardia", "Reflex tachycardia is a problem of dihydropyridines and direct vasodilators, not what ACE inhibitors are given for after infarction; they reduce remodeling and mortality."]],
 "c": 0, "cite": D + ", Slide 18"},

{"topic": "Angiotensin receptor blockers", "io": IO_IND, "slot": "indication",
 "q": "When is an angiotensin receptor blocker used for left ventricular dysfunction?",
 "opts": [
  ["When an ACE inhibitor is not tolerated", "Correct. The ACE (angiotensin-converting enzyme) inhibitor is the default in left ventricular dysfunction; the receptor blocker is the replacement when the patient cannot tolerate it."],
  ["Only after a beta blocker fails", "Beta blocker failure is not the trigger. An angiotensin receptor blocker is used in left ventricular dysfunction when an ACE inhibitor cannot be tolerated."],
  ["Only with a potassium supplement", "Potassium supplements raise the risk of hyperkalemia with these drugs and are not required. The indication is intolerance of an ACE inhibitor."],
  ["Never, as it worsens heart failure", "It is used in left ventricular dysfunction, started low and titrated upward, whenever an ACE inhibitor cannot be tolerated."]],
 "c": 0, "cite": D + ", Slide 28"},

{"topic": "Angiotensin receptor blockers", "io": IO_ADME, "slot": "protocol",
 "q": "Why does raising an angiotensin receptor blocker's dose change blood pressure only a little?",
 "opts": [
  ["Receptors saturate at starting doses", "Correct. AT1 (angiotensin II type 1) receptors are saturated at starting doses for most agents, so the dose response is nonlinear; adding a diuretic increases the effect more than a dose increase."],
  ["Higher doses induce its metabolism", "Enzyme induction is not the explanation. The AT1 receptors are already saturated at starting doses, so extra drug has little left to block."],
  ["It is converted to an inactive form", "Inactivation is not the reason. With AT1 receptors already saturated at starting doses, higher doses produce only small further changes."],
  ["Higher doses block the receptor less", "More drug does not block less. The receptors are nearly all occupied at starting doses, so there is little additional blockade to gain."]],
 "c": 0, "cite": D + ", Slide 28"},

{"topic": "Angiotensin receptor blockers", "io": IO_INTER, "slot": "interaction",
 "q": "A patient with salt-sensitive hypertension responds poorly to losartan. What improves the response?",
 "opts": [
  ["Adding a diuretic", "Correct. Angiotensin receptor blockers are less effective in the salt-sensitive form; adding a diuretic improves outcomes, which is why most come as combination products."],
  ["Doubling the losartan dose", "Receptors are saturated at starting doses, so dose increases change blood pressure only slightly. Adding a diuretic is what improves salt-sensitive hypertension."],
  ["Adding an ACE inhibitor", "Pairing an ACE (angiotensin-converting enzyme) inhibitor with an angiotensin receptor blocker is not the step; the recommended combinations add a diuretic or a dihydropyridine."],
  ["Adding a potassium supplement", "Potassium supplements raise the hyperkalemia risk with this class and do nothing for the salt-sensitive response. Adding a diuretic does."]],
 "c": 0, "cite": D + ", Slide 28"},

# ---- adverse effects: cough, angioedema --------------------------------------
{"topic": "ACE inhibitors", "io": IO_AE, "slot": "adverse effect",
 "q": "A patient develops a persistent dry cough six weeks after starting lisinopril. What is the likely cause?",
 "opts": [
  ["Bradykinin accumulating in the lungs", "Correct. Bradykinin and substance P accumulate because the converting enzyme no longer breaks them down; the cough appears between 1 week and 6 months."],
  ["Angiotensin II acting on the airways", "Angiotensin II falls on an ACE inhibitor, so it cannot be the cause. The cough comes from bradykinin and substance P accumulating in the lungs."],
  ["Aldosterone excess retaining fluid", "Aldosterone synthesis falls on this drug. The dry cough is a bradykinin and substance P effect in the lungs."],
  ["Beta-2 blockade in the bronchi", "Bronchospasm from beta-2 blockade belongs to beta blockers. The ACE inhibitor cough comes from bradykinin accumulating in the lungs."]],
 "c": 0, "cite": D + ", Slide 19"},

{"topic": "ACE inhibitors", "io": IO_EDU, "slot": "education",
 "q": "A patient asks whether the dry cough from her ACE (angiotensin-converting enzyme) inhibitor will stop if the dose is lowered. What is accurate?",
 "opts": [
  ["It is not related to dose or agent", "Correct. The cough is not dose- or agent-related, is more frequent in women, and may require removing the ACE inhibitor if it is bothersome."],
  ["It resolves with a lower dose", "The cough is not related to dose, so lowering it does not reliably help; if it is bothersome the ACE inhibitor may need to be removed."],
  ["It stops on switching to captopril", "The cough is not specific to one agent: every ACE inhibitor raises bradykinin, so switching within the class does not solve it."],
  ["It occurs only in the first day", "It usually appears between 1 week and 6 months after starting, not only on the first day."]],
 "c": 0, "cite": D + ", Slide 19"},

{"topic": "ACE vs angiotensin receptor blockers", "io": IO_PROT, "slot": "drug choice",
 "q": "A patient on enalapril has a bothersome dry cough but well-controlled blood pressure. Which change is most appropriate?",
 "opts": [
  ["Switch to an angiotensin receptor blocker", "Correct. Angiotensin receptor blockers do not affect bradykinin metabolism, so they do not cause cough, and they keep the benefit of blocking angiotensin II."],
  ["Switch to a different ACE inhibitor", "The cough is not related to the specific agent: every ACE (angiotensin-converting enzyme) inhibitor lets bradykinin build up, so a switch within the class keeps the cough."],
  ["Halve the dose of enalapril", "The cough is not dose-related, so halving the dose does not remove it. Moving to an angiotensin receptor blocker does."],
  ["Add a beta blocker to suppress it", "Beta blockers have no antitussive role and can cause bronchospasm. The fix is to change to a drug that spares bradykinin."]],
 "c": 0, "cite": D + ", Slide 30"},

{"topic": "ACE inhibitors", "io": IO_TOX, "slot": "adverse effect",
 "q": "Four days after starting lisinopril, a patient develops rapid swelling of the lips, tongue and throat. What is the most likely cause?",
 "opts": [
  ["Bradykinin-mediated angioedema", "Correct. ACE (angiotensin-converting enzyme) inhibitor angioedema is rare, usually appears in the first week, and is reversible when the drug is removed."],
  ["Hyperkalemia from low aldosterone", "Hyperkalemia is a real risk of this class but does not cause facial and airway swelling. This is angioedema from bradykinin accumulation."],
  ["First-dose hypotension", "First-dose hypotension causes dizziness or fainting, not swelling of the lips and larynx. That picture is bradykinin-mediated angioedema."],
  ["Sodium and water retention", "Sodium retention is a clonidine or direct vasodilator problem and produces generalized fluid gain, not rapid swelling of the lips and tongue."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "ACE inhibitors", "io": IO_EDU, "slot": "education",
 "q": "When should a patient starting an ACE (angiotensin-converting enzyme) inhibitor be most alert for angioedema?",
 "opts": [
  ["During the first week", "Correct. Angioedema usually develops in the first week of therapy and is reversible if the drug is removed."],
  ["After six months or more", "Six months marks the late end of the window for the dry cough, not angioedema. Angioedema usually appears in the first week."],
  ["Only after a dose increase", "Angioedema is not tied to titration. It usually develops in the first week of therapy, whatever the dose."],
  ["Only after stopping the drug", "Angioedema occurs while the drug is being taken, usually in the first week, and resolves once the drug is removed."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "ACE vs angiotensin receptor blockers", "io": IO_AE, "slot": "adverse effect",
 "q": "Compared with ACE (angiotensin-converting enzyme) inhibitors, which statement about angiotensin receptor blockers is accurate?",
 "opts": [
  ["They do not cause the dry cough", "Correct. They do not affect bradykinin metabolism, so cough does not occur and angioedema is less frequent, which is why patients may be switched to them."],
  ["They cause more angioedema", "The reverse: angiotensin receptor blockers have a lower incidence of angioedema, which is one reason a patient may be switched to one."],
  ["They raise bradykinin further", "Angiotensin receptor blockers do not inhibit bradykinin breakdown at all; that is why they avoid the cough."],
  ["They are safe late in pregnancy", "Like ACE inhibitors, they are not given in the second and third trimesters because of fetal morbidity and mortality."]],
 "c": 0, "cite": D + ", Slide 30"},

# ---- adverse effects: potassium (strongest cue) ------------------------------
{"topic": "ACE inhibitors", "io": IO_TOX, "slot": "adverse effect",
 "q": "A 64-year-old with chronic kidney disease who uses a salt substitute is started on lisinopril. Which laboratory abnormality is most important to anticipate?",
 "opts": [
  ["Hyperkalemia", "Correct. Hyperkalemia is most often seen with renal disease and in those taking potassium-sparing diuretics, potassium supplements or salt substitutes; this patient has two of those."],
  ["Hypokalemia", "The direction is wrong: less aldosterone means potassium is retained, so potassium rises rather than falls, especially with kidney disease and a salt substitute."],
  ["Hypercalcemia", "Calcium is not the concern with ACE inhibitors. Renal disease plus a potassium-containing salt substitute makes hyperkalemia the one to watch."],
  ["Hypoglycemia", "Masked or prolonged hypoglycemia is a beta blocker problem. With an ACE inhibitor, renal disease and a salt substitute, potassium rises."]],
 "c": 0, "cite": D + ", Slide 20"},

{"topic": "Angiotensin receptor blockers", "io": IO_INTER, "slot": "interaction",
 "q": "Which drug added to losartan most increases the risk of hyperkalemia?",
 "opts": [
  ["A potassium-sparing diuretic", "Correct. Hyperkalemia with angiotensin receptor blockers is linked to renal disease and potassium-sparing diuretics, both of which keep potassium in."],
  ["A dihydropyridine", "A dihydropyridine calcium channel blocker is a standard partner for losartan and does not raise potassium; the risk comes from potassium-sparing diuretics."],
  ["A beta-1 selective blocker", "Beta-1 selective blockers are not linked to hyperkalemia here. The drug that adds to losartan's potassium retention is a potassium-sparing diuretic."],
  ["An alpha-1 blocker", "Alpha-1 blockers cause orthostatic hypotension, not hyperkalemia. The potassium danger with losartan is a potassium-sparing diuretic."]],
 "c": 0, "cite": D + ", Slide 29"},

{"topic": "ACE inhibitors", "io": IO_EDU, "slot": "education",
 "q": "What should a patient starting benazepril be told about potassium?",
 "opts": [
  ["Avoid potassium supplements and salt substitutes", "Correct. ACE (angiotensin-converting enzyme) inhibitors raise potassium, and supplements or potassium-based salt substitutes add to it; renal disease raises the risk further."],
  ["Take a daily potassium supplement to replace losses", "The drug retains potassium rather than wasting it, so a supplement risks hyperkalemia. Supplements and salt substitutes should be avoided."],
  ["Potassium is not affected by this medicine", "Potassium is affected: less aldosterone means potassium rises, which is why supplements and salt substitutes are a problem."],
  ["Expect low potassium, so watch for cramps", "The expected change is a rise, not a fall. Hyperkalemia is the risk, made worse by supplements and salt substitutes."]],
 "c": 0, "cite": D + ", Slide 20"},

# ---- first-dose hypotension, renal function ----------------------------------
{"topic": "ACE inhibitors", "io": IO_AE, "slot": "adverse effect",
 "q": "First-dose hypotension with an ACE (angiotensin-converting enzyme) inhibitor is most common in which patient?",
 "opts": [
  ["One who is sodium depleted", "Correct. It is most common in sodium-depleted patients, in heart failure and in those on several antihypertensive drugs, and occurs with the first dose or an upward titration."],
  ["One with mild, untreated hypertension", "Mild untreated hypertension is not a listed risk group. Sodium depletion, heart failure and multiple antihypertensives are."],
  ["One with type 2 diabetes alone", "Diabetes makes an ACE inhibitor the preferred agent but is not a first-dose hypotension risk group; sodium depletion is."],
  ["One younger than 40 years", "Youth is not a risk factor listed for this. First-dose hypotension is most common with sodium depletion, heart failure or multiple antihypertensives."]],
 "c": 0, "cite": D + ", Slide 20"},

{"topic": "ACE inhibitors", "io": IO_TOX, "slot": "adverse effect",
 "q": "In a patient with renal disease whose renal blood flow depends on angiotensin II, what can happen when an ACE (angiotensin-converting enzyme) inhibitor is started?",
 "opts": [
  ["Filtration rate drops sharply", "Correct. Where renal blood flow depends on angiotensin II, ACE inhibitors can dramatically decrease the glomerular filtration rate, so they are used cautiously and titrated slowly."],
  ["Filtration rate rises sharply", "The change is a fall, not a rise: removing angiotensin II takes away the support that kept glomerular pressure up in these kidneys."],
  ["Renal blood flow is unchanged", "Renal blood flow is not spared in these patients; the loss of angiotensin II can dramatically decrease glomerular filtration."],
  ["Potassium falls sharply", "Potassium tends to rise on this class, especially with renal disease. The kidney-specific danger is a dramatic fall in filtration."]],
 "c": 0, "cite": D + ", Slide 21"},

{"topic": "ACE inhibitors", "io": IO_PROT, "slot": "protocol",
 "q": "How should an ACE (angiotensin-converting enzyme) inhibitor be started in a patient with renal disease?",
 "opts": [
  ["Low dose, increased slowly", "Correct. Because glomerular filtration can fall dramatically where renal blood flow depends on angiotensin II, the drug is used cautiously: low doses moved upward slowly."],
  ["Full dose, reduced if needed", "Starting at full dose risks an abrupt fall in filtration in a kidney that depends on angiotensin II. The approach is low doses moved up slowly."],
  ["A loading dose, then daily doses", "No loading dose is used. In renal disease the drug is started low and increased slowly because filtration can drop sharply."],
  ["It is never used in renal disease", "It is not banned: it slows diabetic and other nephropathies. It is used cautiously, starting low and titrating slowly."]],
 "c": 0, "cite": D + ", Slide 21"},

# ---- pregnancy, NSAIDs -------------------------------------------------------
{"topic": "ACE inhibitors", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which statement about ACE (angiotensin-converting enzyme) inhibitors in pregnancy is accurate?",
 "opts": [
  ["Contraindicated in the second and third trimesters", "Correct. They cause fetal morbidity and mortality, including birth defects and fetal death, so they are contraindicated in the second and third trimesters."],
  ["Safe once the first trimester has ended", "The danger is greatest after the first trimester: they are contraindicated in the second and third trimesters because of birth defects and fetal death."],
  ["Contraindicated in the first trimester only", "The trimesters named are the second and third, when fetal morbidity and mortality occur, not the first alone."],
  ["Preferred for hypertension throughout pregnancy", "They cause birth defects and fetal death and are contraindicated in the second and third trimesters, so they are never the preferred pregnancy agent."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Angiotensin receptor blockers", "io": IO_CONTRA, "slot": "contraindication",
 "q": "A patient in her third trimester cannot take an ACE (angiotensin-converting enzyme) inhibitor. Is an angiotensin receptor blocker an acceptable substitute?",
 "opts": [
  ["No, it is also avoided then", "Correct. Angiotensin receptor blockers share the fetal morbidity and mortality and are not given in the second and third trimesters."],
  ["Yes, it spares the fetus", "It does not spare the fetus. Angiotensin receptor blockers carry the same fetal morbidity and mortality and are not given in trimesters two and three."],
  ["Yes, at a reduced dose", "Dose reduction does not make it safe. The class is not given in the second and third trimesters because of fetal harm."],
  ["Only if potassium is normal", "Potassium is not the deciding factor. The class is avoided in the second and third trimesters because of fetal morbidity and mortality."]],
 "c": 0, "cite": D + ", Slide 29"},

{"topic": "ACE inhibitors", "io": IO_INTER, "slot": "interaction",
 "q": "A patient on lisinopril begins taking ibuprofen daily for knee pain. How do NSAIDs (nonsteroidal anti-inflammatory drugs) affect the ACE inhibitor?",
 "opts": [
  ["They reduce its effect", "Correct. NSAIDs block the prostaglandin-dependent, bradykinin-mediated relaxation that contributes to the ACE (angiotensin-converting enzyme) inhibitor's effect, so blood pressure control weakens."],
  ["They increase its effect", "The direction is wrong. NSAIDs blunt the drug, because they block prostaglandin-driven relaxation that bradykinin produces."],
  ["They have no interaction", "There is a listed interaction: NSAIDs decrease the effect of ACE inhibitors by blocking bradykinin-mediated relaxation that depends on prostaglandins."],
  ["They cause its cough", "The cough comes from bradykinin and substance P accumulating in the lungs, not from NSAIDs; NSAIDs instead reduce the drug's effect."]],
 "c": 0, "cite": D + ", Slide 22"},

# ---- agents ------------------------------------------------------------------
{"topic": "ACE inhibitors", "io": IO_ADME, "slot": "class",
 "q": "Which ACE (angiotensin-converting enzyme) inhibitor has a short half-life, making it the exception to once-daily dosing?",
 "opts": [
  ["Captopril", "Correct. Captopril's short half-life sets it apart; most other ACE inhibitors are given once daily, though some lose effect near the end of the interval."],
  ["Lisinopril", "Lisinopril is a once-daily agent. The short half-life exception to once-daily dosing is captopril."],
  ["Ramipril", "Ramipril is dosed once daily like most of the class. Captopril is the short half-life exception."],
  ["Trandolapril", "Trandolapril follows the once-daily pattern of most of the class. The exception with a short half-life is captopril."]],
 "c": 0, "cite": D + ", Slide 15"},

{"topic": "ACE inhibitors", "io": IO_ADME, "slot": "class",
 "q": "Which ACE (angiotensin-converting enzyme) inhibitor has an intravenous active form?",
 "opts": [
  ["Enalapril", "Correct. Enalapril is converted to enalaprilat, which is available as the intravenous form."],
  ["Lisinopril", "Lisinopril is an oral agent without a separate intravenous form. Enalapril's active form, enalaprilat, is the intravenous one."],
  ["Benazepril", "Benazepril is given orally. The ACE inhibitor with an intravenous active form is enalapril, as enalaprilat."],
  ["Quinapril", "Quinapril is an oral agent. Enalaprilat, the active form of enalapril, is the intravenous option."]],
 "c": 0, "cite": D + ", Slide 13"},

# ---- algorithm (slide 108) ---------------------------------------------------
{"topic": "Hypertension algorithm", "io": IO_PROT, "slot": "drug choice",
 "q": "A 58-year-old without diabetes has blood pressure 8/4 mmHg above goal and a urine albumin-to-creatinine ratio below 300 mg/g. Lifestyle counseling is under way. Which is an appropriate first drug?",
 "opts": [
  ["An ACE inhibitor or a dihydropyridine", "Correct. Below the combination threshold and without albuminuria, first line is an ACE (angiotensin-converting enzyme) inhibitor or angiotensin receptor blocker, or a dihydropyridine calcium channel blocker."],
  ["A beta blocker or an alpha-1 blocker", "Neither is first line. Beta blockers are not recommended for first-line management of hypertension, and alpha-1 blockers are specialty add-ons."],
  ["Hydralazine or minoxidil", "Direct vasodilators are kept for severe or refractory hypertension alongside other agents. The algorithm starts with an ACE inhibitor or angiotensin receptor blocker, or a dihydropyridine."],
  ["Clonidine or guanfacine", "Central sympatholytics are not in the first-line step. The algorithm begins with an ACE inhibitor or angiotensin receptor blocker, or a dihydropyridine."]],
 "c": 0, "cite": D + ", Slide 108"},

{"topic": "Hypertension algorithm", "io": IO_PROT, "slot": "drug choice",
 "q": "A patient with hypertension mildly above goal has a urine albumin-to-creatinine ratio of 450 mg/g. Which initial therapy is recommended?",
 "opts": [
  ["An ACE inhibitor or receptor blocker", "Correct. With an albumin-to-creatinine ratio of 300 mg/g or more, the algorithm starts an ACE (angiotensin-converting enzyme) inhibitor or an angiotensin receptor blocker, consistent with their kidney-protective effect."],
  ["A dihydropyridine calcium channel blocker", "A dihydropyridine is a first-line option only when there is no albuminuria. At a ratio of 300 mg/g or more, the choice is an ACE inhibitor or angiotensin receptor blocker."],
  ["A beta blocker or an alpha-1 blocker", "Beta blockers are not first line, alpha-1 blockers are specialty add-ons, and neither offers kidney protection. Albuminuria of this degree calls for an ACE inhibitor or angiotensin receptor blocker."],
  ["Hydralazine or minoxidil", "Direct vasodilators are for severe or resistant hypertension with other agents. Albuminuria points to an ACE inhibitor or angiotensin receptor blocker."]],
 "c": 0, "cite": D + ", Slide 108"},

{"topic": "Hypertension algorithm", "io": IO_PROT, "slot": "drug choice",
 "q": "At diagnosis, a patient's systolic pressure is 24 mmHg above goal. Which starting regimen is recommended?",
 "opts": [
  ["ACE inhibitor plus a dihydropyridine", "Correct. When systolic pressure is more than 20 mmHg (or diastolic more than 10 mmHg) above goal, start an ACE (angiotensin-converting enzyme) inhibitor or angiotensin receptor blocker plus a dihydropyridine."],
  ["ACE inhibitor plus a receptor blocker", "The pairing is an ACE inhibitor OR an angiotensin receptor blocker, combined with a dihydropyridine calcium channel blocker, not the two renin-angiotensin drugs together."],
  ["Beta blocker plus clonidine", "Neither is a first-step agent. Pressure this far above goal starts an ACE inhibitor or angiotensin receptor blocker with a dihydropyridine."],
  ["A dihydropyridine by itself", "Monotherapy fits pressure that is only modestly above goal. At more than 20 mmHg systolic above goal, the algorithm starts a two-drug combination."]],
 "c": 0, "cite": D + ", Slide 108"},

{"topic": "Hypertension algorithm", "io": IO_PROT, "slot": "drug choice",
 "q": "A patient taking lisinopril and amlodipine remains above goal after titration, and adherence and measurement have been confirmed. What is the next step?",
 "opts": [
  ["Add a thiazide-like diuretic", "Correct. After an ACE (angiotensin-converting enzyme) inhibitor or angiotensin receptor blocker plus a dihydropyridine, the next step is a thiazide-like diuretic; if pressure is still uncontrolled, it is apparent resistant hypertension."],
  ["Add losartan", "Adding an angiotensin receptor blocker to an ACE inhibitor doubles up on the same system and is not the next step; a thiazide-like diuretic is."],
  ["Add hydralazine", "Direct vasodilators are not the third step. The algorithm adds a thiazide-like diuretic after the ACE inhibitor plus dihydropyridine combination."],
  ["Swap amlodipine for verapamil", "Swapping to a non-dihydropyridine is not a step in the algorithm; after the two-drug combination, a thiazide-like diuretic is added."]],
 "c": 0, "cite": D + ", Slide 108"},

{"topic": "Hypertension algorithm", "io": IO_PROT, "slot": "protocol",
 "q": "Blood pressure has not improved after two titration steps. What is the most common cause of a lack of response?",
 "opts": [
  ["Medication nonadherence", "Correct. Nonadherence is listed first, ahead of the white coat effect and improper measurement, so it is considered before assuming the drugs have failed."],
  ["The white coat effect", "The white coat effect is on the list, but second; the most common cause of lack of response is medication nonadherence."],
  ["Tolerance to the drug", "Drug tolerance is not among the listed causes. The most common are nonadherence, the white coat effect and improper blood pressure measurement, in that order."],
  ["Excess dietary potassium", "Dietary potassium is not a cause of treatment failure on the list. Medication nonadherence is the most common cause."]],
 "c": 0, "cite": D + ", Slide 108"},

{"topic": "Hypertension algorithm", "io": IO_PROT, "slot": "protocol",
 "q": "After an antihypertensive is started or titrated, when should blood pressure control be reassessed?",
 "opts": [
  ["About 4 weeks later", "Correct. Control is reassessed about 4 weeks after starting or titrating, and one or two titration steps are appropriate before modifying or adding medication."],
  ["About 3 days later", "Three days is too soon to judge the effect of a change; the recommended reassessment is about 4 weeks after starting or titrating."],
  ["About 6 months later", "Six months leaves a patient uncontrolled for too long; reassessment is recommended about 4 weeks after each change."],
  ["Only at the annual visit", "Annual review is far too infrequent after a change. Blood pressure is reassessed about 4 weeks after starting or titrating therapy."]],
 "c": 0, "cite": D + ", Slide 108"},
]
