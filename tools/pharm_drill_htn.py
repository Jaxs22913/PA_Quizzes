# -*- coding: utf-8 -*-
"""Rapid-drill bank: antihypertensives (Lecture 6, Antihypertensives.pptx).

One fact, four drug names, no doses. One drug per choice, and every wrong
choice is another antihypertensive, so the question is a discrimination rather
than a category guess ([[pharmacology_exam_spec]], Rapid Drills 2026-09-02).

A fact becomes an item only if it belongs to exactly one agent (or one small
group whose other members are kept out of the options). Clonidine is keyed as
an alpha-2 AGONIST (slides 86, 92); slide 75's "a2 blocker" is a deck error.
Nothing on plus counts, elimination routes, ISA/MSA columns, carteolol or
betaxolol, or doses.
"""
ITEMS = [
dict(q="Which drug causes a DRY COUGH from bradykinin accumulating in the lungs?",
     ans="Lisinopril", src=("HTN", 19),
     why="ACE (angiotensin-converting enzyme) inhibitors stop bradykinin breakdown; the cough is not dose- or agent-related.",
     wrong=[("Losartan", "An angiotensin receptor blocker: it does not affect bradykinin metabolism, so it does not cause the cough."),
            ("Amlodipine", "A dihydropyridine calcium channel blocker; its vasodilator effects are edema and reflex tachycardia, not cough."),
            ("Metoprolol", "A beta-1 selective blocker; bronchospasm is a beta blocker concern, but a bradykinin cough is not.")]),

dict(q="A patient cannot tolerate an ACE (angiotensin-converting enzyme) inhibitor's cough. Which drug is the SWITCH?",
     ans="Valsartan", src=("HTN", 30),
     why="Angiotensin receptor blockers do not cause cough and have a lower incidence of angioedema, so patients may be switched to them.",
     wrong=[("Enalapril", "Another ACE (angiotensin-converting enzyme) inhibitor: the cough is a class effect, so switching within the class does not help."),
            ("Captopril", "An ACE (angiotensin-converting enzyme) inhibitor; every agent in the class lets bradykinin build up and cause the cough."),
            ("Ramipril", "Also an ACE (angiotensin-converting enzyme) inhibitor, so it carries the same bradykinin cough as the one being stopped.")]),

dict(q="Which ACE (angiotensin-converting enzyme) inhibitor has an INTRAVENOUS active form?",
     ans="Enalapril", src=("HTN", 13),
     why="Enalapril is converted to enalaprilat, which is the intravenous form.",
     wrong=[("Lisinopril", "Lisinopril is an oral once-daily ACE (angiotensin-converting enzyme) inhibitor with no separate intravenous form."),
            ("Benazepril", "Benazepril is an oral ACE (angiotensin-converting enzyme) inhibitor; enalaprilat is the intravenous one."),
            ("Quinapril", "Quinapril is taken by mouth; the intravenous ACE (angiotensin-converting enzyme) inhibitor is enalaprilat.")]),

dict(q="Which ACE (angiotensin-converting enzyme) inhibitor has a SHORT half-life, the exception to once-daily dosing?",
     ans="Captopril", src=("HTN", 15),
     why="Most ACE (angiotensin-converting enzyme) inhibitors are once daily; captopril's short half-life is the exception.",
     wrong=[("Lisinopril", "Lisinopril follows the class pattern of once-daily dosing; captopril is the short half-life exception."),
            ("Ramipril", "Ramipril is a once-daily agent like most of the class; the exception is captopril."),
            ("Trandolapril", "Trandolapril is dosed once daily; captopril's short half-life makes it the exception.")]),

dict(q="Which drug raises POTASSIUM, especially with renal disease or a potassium-sparing diuretic?",
     ans="Candesartan", src=("HTN", 29),
     why="Angiotensin receptor blockers (like ACE inhibitors) cause hyperkalemia, most often with renal disease or potassium-sparing diuretics.",
     wrong=[("Nifedipine", "A dihydropyridine calcium channel blocker; its adverse effects are edema and reflex tachycardia, not hyperkalemia."),
            ("Doxazosin", "An alpha-1 blocker; its concern is orthostatic hypotension, not potassium retention."),
            ("Clonidine", "A central alpha-2 agonist; it causes sedation, dry mouth and sodium retention rather than hyperkalemia.")]),

dict(q="Which calcium channel blocker treats PAROXYSMAL SUPRAVENTRICULAR TACHYCARDIA?",
     ans="Verapamil", src=("HTN", 44),
     why="Only the non-dihydropyridines slow atrioventricular conduction, so only they treat supraventricular tachycardia.",
     wrong=[("Amlodipine", "A dihydropyridine: it has no effect on atrioventricular conduction, so it cannot treat supraventricular tachycardia."),
            ("Felodipine", "A dihydropyridine approved for hypertension only; it dilates vessels rather than slowing the nodes."),
            ("Nisoldipine", "A dihydropyridine approved for hypertension; nodal slowing requires diltiazem or verapamil.")]),

dict(q="Which dihydropyridine is approved for SUBARACHNOID HEMORRHAGE?",
     ans="Nimodipine", src=("HTN", 49),
     why="Nimodipine's approved indication is subarachnoid hemorrhage.",
     wrong=[("Nifedipine", "Nifedipine is approved for angina and hypertension, and is the gynecomastia comparator against diltiazem."),
            ("Nicardipine", "Nicardipine is approved for angina and hypertension and is the dihydropyridine available intravenously."),
            ("Isradipine", "Isradipine is approved for hypertension only, not subarachnoid hemorrhage.")]),

dict(q="Which dihydropyridine is available INTRAVENOUSLY?",
     ans="Nicardipine", src=("HTN", 49),
     why="Dihydropyridines are oral only, except nicardipine.",
     wrong=[("Amlodipine", "Amlodipine is an oral dihydropyridine for angina and hypertension; nicardipine is the intravenous exception."),
            ("Felodipine", "Felodipine is oral only and approved for hypertension; the intravenous dihydropyridine is nicardipine."),
            ("Nimodipine", "Nimodipine is oral and approved for subarachnoid hemorrhage; nicardipine is the intravenous one.")]),

dict(q="Which calcium channel blocker raises DIGOXIN levels by inhibiting P-glycoprotein?",
     ans="Verapamil", src=("HTN", 47),
     why="Non-dihydropyridines inhibit P-glycoprotein (raising digoxin) and CYP3A4 (raising three statins).",
     wrong=[("Amlodipine", "Dihydropyridines have only pharmacodynamic interactions with digoxin; they do not inhibit P-glycoprotein."),
            ("Nifedipine", "A dihydropyridine; it is a CYP3A4 substrate but not a P-glycoprotein inhibitor that raises digoxin."),
            ("Felodipine", "A dihydropyridine without the P-glycoprotein inhibition that lets verapamil raise digoxin levels.")]),

dict(q="Which calcium channel blocker RAISES SIMVASTATIN levels by inhibiting CYP3A4?",
     ans="Diltiazem", src=("HTN", 47),
     why="Non-dihydropyridines inhibit CYP3A4, raising atorvastatin, lovastatin and simvastatin.",
     wrong=[("Amlodipine", "Dihydropyridines are CYP3A4 substrates, not inhibitors, so amlodipine does not raise simvastatin this way."),
            ("Nifedipine", "Nifedipine is metabolized by CYP3A4 but does not inhibit it; only diltiazem and verapamil do."),
            ("Felodipine", "Felodipine is a CYP3A4 substrate rather than an inhibitor, so it does not raise statin levels.")]),

dict(q="Which drug is most likely to cause REFLEX TACHYCARDIA?",
     ans="Nifedipine", src=("HTN", 51),
     why="Dihydropyridines dilate arteries strongly and provoke rebound tachycardia; immediate-release forms are avoided in unstable angina.",
     wrong=[("Verapamil", "Verapamil suppresses the sinoatrial and atrioventricular nodes, causing bradycardia rather than tachycardia."),
            ("Diltiazem", "Diltiazem strongly suppresses the sinoatrial node, so it slows the heart rather than speeding it."),
            ("Metoprolol", "A beta-1 selective blocker, not a calcium channel blocker; it slows the heart rate.")]),

dict(q="Which beta blocker is beta-1 selective and given INTRAVENOUSLY?",
     ans="Esmolol", src=("HTN", 61),
     why="Esmolol is the second-generation, beta-1 selective agent marked for intravenous use.",
     wrong=[("Atenolol", "Atenolol is beta-1 selective but taken orally; esmolol is the intravenous agent."),
            ("Bisoprolol", "Bisoprolol is an oral beta-1 selective agent, one of the three used in heart failure."),
            ("Acebutolol", "Acebutolol is an oral beta-1 selective agent; the intravenous one is esmolol.")]),

dict(q="Which beta blocker's HIGH LIPID SOLUBILITY brings nightmares and depression?",
     ans="Propranolol", src=("HTN", 74),
     why="Highly lipid-soluble agents cause more central effects: depression, nightmares, vivid dreams and hallucinations.",
     wrong=[("Atenolol", "Atenolol has low lipid solubility, so it causes fewer central effects than propranolol."),
            ("Nadolol", "Nadolol is non-selective but has low lipid solubility, so central effects are less prominent."),
            ("Sotalol", "Sotalol has low lipid solubility; propranolol is the highly lipid-soluble agent with central effects.")]),

dict(q="Which beta blocker ALSO BLOCKS ALPHA-1 and is used in heart failure?",
     ans="Carvedilol", src=("HTN", 62),
     why="Carvedilol is a third-generation agent with alpha-1 blockade, antioxidant and antiproliferative actions; it is a heart failure agent.",
     wrong=[("Metoprolol", "Metoprolol succinate is a heart failure agent, but metoprolol is beta-1 selective with no alpha-1 blockade."),
            ("Atenolol", "Atenolol is beta-1 selective without alpha-1 blockade, and it is not one of the heart failure agents."),
            ("Nadolol", "Nadolol is a first-generation non-selective agent without alpha-1 blockade.")]),

dict(q="Which beta blocker blocks alpha-1 AND acts as a BETA-2 AGONIST?",
     ans="Labetalol", src=("HTN", 62),
     why="Labetalol is a third-generation agent with alpha-1 blockade and beta-2 agonist activity.",
     wrong=[("Propranolol", "Propranolol is a first-generation non-selective blocker with no alpha-1 or beta-2 agonist action."),
            ("Bisoprolol", "Bisoprolol is a beta-1 selective, second-generation agent used in heart failure, without those actions."),
            ("Esmolol", "Esmolol is an intravenous beta-1 selective blocker with no alpha-1 blockade.")]),

dict(q="Which beta blocker is one of the three used for HEART FAILURE?",
     ans="Bisoprolol", src=("HTN", 70),
     why="The heart failure beta blockers are carvedilol, metoprolol succinate and bisoprolol, started very low and increased slowly.",
     wrong=[("Propranolol", "Propranolol is used for migraine prophylaxis, not as one of the heart failure agents."),
            ("Atenolol", "Atenolol is beta-1 selective but not one of the three heart failure agents."),
            ("Timolol", "Timolol is used for glaucoma and migraine prophylaxis, not heart failure.")]),

dict(q="Which beta blocker is used for GLAUCOMA, reducing aqueous humor production?",
     ans="Timolol", src=("HTN", 65),
     why="Timolol reduces aqueous humor production in the ciliary body; systemic effects of the drops are notable.",
     wrong=[("Esmolol", "Esmolol is an intravenous beta-1 selective agent with no role in glaucoma."),
            ("Atenolol", "Atenolol is an oral beta-1 selective agent for cardiovascular use, not glaucoma."),
            ("Labetalol", "Labetalol is a third-generation agent with alpha-1 blockade, not a glaucoma drug.")]),

dict(q="Which beta blocker is used for MIGRAINE PROPHYLAXIS?",
     ans="Propranolol", src=("HTN", 65),
     why="Propranolol (with timolol) is used for migraine prophylaxis at low dose; the mechanism is uncertain.",
     wrong=[("Esmolol", "Esmolol is an intravenous beta-1 selective blocker with no prophylactic role."),
            ("Bisoprolol", "Bisoprolol is one of the heart failure beta blockers, not a migraine prophylactic."),
            ("Atenolol", "Atenolol is beta-1 selective and not the migraine agent; propranolol and timolol are.")]),

dict(q="Which beta blocker is NON-SELECTIVE (first generation)?",
     ans="Nadolol", src=("HTN", 60),
     why="The first-generation non-selective agents are nadolol, penbutolol, pindolol, propranolol, sotalol and timolol.",
     wrong=[("Metoprolol", "Metoprolol is second-generation and beta-1 selective, not non-selective."),
            ("Atenolol", "Atenolol is a beta-1 selective, second-generation agent, so it is not non-selective."),
            ("Bisoprolol", "Bisoprolol is a beta-1 selective, second-generation agent used in heart failure.")]),

dict(q="Which alpha-1 blocker is ALPHA-1A SELECTIVE, treating the prostate with little vascular effect?",
     ans="Tamsulosin", src=("HTN", 84),
     why="Tamsulosin selectively blocks alpha-1A receptors; vascular receptors are alpha-1B, so blood pressure effects are limited.",
     wrong=[("Prazosin", "Prazosin is a selective alpha-1 antagonist used for hypertension, with orthostatic hypotension as its main effect."),
            ("Terazosin", "Terazosin is used both as an antihypertensive and for prostatic hyperplasia, so it does affect blood pressure."),
            ("Doxazosin", "Doxazosin lowers blood pressure and treats prostatic hyperplasia; it is not the alpha-1A selective agent.")]),

dict(q="Which antihypertensive MILDLY LOWERS LDL (low-density lipoprotein) AND TRIGLYCERIDES and raises HDL (high-density lipoprotein)?",
     ans="Prazosin", src=("HTN", 78),
     why="Prazosin shows evidence of a mild fall in LDL (low-density lipoprotein) and triglycerides with a rise in HDL (high-density lipoprotein).",
     wrong=[("Propranolol", "Beta blockers list elevated triglycerides among their adverse effects, the opposite direction."),
            ("Clonidine", "Central sympatholytics have no negative effect on lipids, but no lipid improvement is claimed for them."),
            ("Hydralazine", "No lipid effect is described for hydralazine; prazosin carries the favorable lipid profile.")]),

dict(q="Which drug is a central ALPHA-2 AGONIST that BLUNTS OPIATE WITHDRAWAL?",
     ans="Clonidine", src=("HTN", 93),
     why="Clonidine's analgesic activity blunts opiate withdrawal reactions; it stimulates central alpha-2 and imidazoline receptors.",
     wrong=[("Guanfacine", "Guanfacine is also a central alpha-2 agonist, but the opiate withdrawal use is attributed to clonidine."),
            ("Prazosin", "Prazosin is a peripheral alpha-1 antagonist with no role in opiate withdrawal."),
            ("Hydralazine", "Hydralazine is a direct vasodilator and has no role in opiate withdrawal.")]),

dict(q="Which central agent is the MOST ALPHA-2 SELECTIVE, with LESS SEDATION?",
     ans="Guanfacine", src=("HTN", 95),
     why="Guanfacine is less potent than clonidine, the most selective for alpha-2 over alpha-1, less sedating, with occasional withdrawal.",
     wrong=[("Clonidine", "Clonidine is more sedating, and its withdrawal reactions may be severe."),
            ("Prazosin", "Prazosin blocks peripheral alpha-1 receptors; it is not a central alpha-2 agonist."),
            ("Tamsulosin", "Tamsulosin is an alpha-1A selective antagonist for the prostate, not a central agent.")]),

dict(q="Which drug RAISES BLOOD GLUCOSE by inhibiting insulin secretion and retains sodium?",
     ans="Clonidine", src=("HTN", 92),
     why="Clonidine increases blood glucose by inhibiting insulin secretion and causes sodium retention, so it is often given with a diuretic.",
     wrong=[("Lisinopril", "An ACE (angiotensin-converting enzyme) inhibitor; it is preferred in diabetes for kidney protection."),
            ("Amlodipine", "A dihydropyridine calcium channel blocker; no effect on insulin secretion is described."),
            ("Hydralazine", "A direct vasodilator causing fluid retention by reflex, but no effect on insulin secretion.")]),

dict(q="Which drug is N-ACETYLATED, with LUPUS SYNDROME in slow acetylators?",
     ans="Hydralazine", src=("HTN", 101),
     why="Hydralazine lupus syndrome risk: high dose, long term, women, slow acetylators and Caucasian ancestry.",
     wrong=[("Minoxidil", "Minoxidil opens potassium channels and causes hypertrichosis, not lupus syndrome."),
            ("Nitroprusside", "Nitroprusside's toxicity is cyanide and thiocyanate, not a lupus syndrome."),
            ("Prazosin", "Prazosin is an alpha-1 blocker causing orthostatic hypotension, not lupus syndrome.")]),

dict(q="Which drug should come with the warning that STOOLS MAY TURN BLACK?",
     ans="Hydralazine", src=("HTN", 102),
     why="Stools may turn black on hydralazine; the patient is told ahead of time.",
     wrong=[("Minoxidil", "Minoxidil's characteristic warning is hypertrichosis, not a change in stool color."),
            ("Clonidine", "Clonidine's warnings are sedation, dry mouth and never stopping abruptly, not stool color."),
            ("Verapamil", "Verapamil's bowel warning is constipation, not black stools.")]),

dict(q="Which drug OPENS ATP-MODULATED POTASSIUM CHANNELS and causes HYPERTRICHOSIS?",
     ans="Minoxidil", src=("HTN", 103),
     why="Minoxidil hyperpolarizes arteriolar smooth muscle through potassium efflux and grows hair on the face, back, arms and legs.",
     wrong=[("Hydralazine", "Hydralazine's mechanism is not clear, and its signature toxicity is lupus syndrome, not hair growth."),
            ("Nitroprusside", "Nitroprusside releases nitric oxide (raising cyclic GMP) and causes cyanide toxicity."),
            ("Diltiazem", "Diltiazem blocks L-type calcium channels; gingival hyperplasia, not hypertrichosis, is its growth effect.")]),

dict(q="Which drug given by INFUSION for HYPERTENSIVE CRISIS can cause CYANIDE toxicity?",
     ans="Nitroprusside", src=("HTN", 107),
     why="Nitroprusside carries five cyanide groups; sodium thiosulfate limits cyanide toxicity, and thiocyanate builds up with long infusions or renal failure.",
     wrong=[("Hydralazine", "Hydralazine is used for chronic hypertension with a diuretic and beta blocker; its toxicity is lupus syndrome."),
            ("Minoxidil", "Minoxidil is an oral triple-therapy agent for refractory hypertension; hypertrichosis is its hallmark."),
            ("Nicardipine", "Nicardipine is the intravenous dihydropyridine; cyanide is not among its toxicities.")]),

dict(q="Which drug is CONTRAINDICATED in CORONARY ARTERY DISEASE and the ELDERLY because of reflex sympathetic workload?",
     ans="Hydralazine", src=("HTN", 102),
     why="Hydralazine is contraindicated in coronary artery disease, the elderly and ischemia: vasodilation plus sympathetic activation raises cardiac work.",
     wrong=[("Metoprolol", "Beta blockers protect ischemic myocardium and are used after myocardial infarction, not contraindicated in it."),
            ("Lisinopril", "ACE (angiotensin-converting enzyme) inhibitors reduce remodeling and mortality after infarction."),
            ("Amlodipine", "Amlodipine is approved for angina; its contraindications are severe aortic stenosis and unstable angina with immediate release.")]),
]
