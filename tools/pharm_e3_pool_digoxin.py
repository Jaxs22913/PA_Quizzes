# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Diuretics and Heart Failure Drugs (Lecture 9), topic: digoxin.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

SOURCE. Diuretics and Heart Failure Drugs.pptx slides 61-72 (structure, inotropic and neurohormonal action, clinical
benefits, place in therapy, toxicity, contraindications, digoxin immune Fab) plus the two interaction lines about
digitalis on slides 19 and 29. Picture-only slides 62 (digitalis and the sodium-potassium pump) and 70 (electrocardiogram
with premature ventricular beats) were read by eye into tools/pharm_e3/ocr.json.

WEIGHTING (Dr. McInnis): indications, patient education, adverse effects, contraindications and drug choice outnumber
mechanism. Mechanism items are kept to recognition level.

LEFT OUT ON PURPOSE (no key built on them):
  * the target concentration (slide 65): Dr. Wood said he will not quiz the level; only the qualitative statements that
    a concentration is followed and that higher concentrations may do worse are used (monitoring slot);
  * "hyperkalemia" as a contraindication (slide 71) -- TRUTH WINS: low potassium (slides 19 and 29), low magnesium and
    high calcium raise toxicity; hyperkalemia is never keyed and never offered as an option;
  * "first line for atrial fibrillation with heart failure" (slide 67) -- overstated; keyed only as "useful for rate
    control";
  * the wording "binds the antigen-binding site of Ig" (slide 72) -- keyed as antibody fragments from sheep;
  * what the slides do not say about the antidote (unmasking of the arrhythmia it was treating).

NOTE ON HALOS: ivabradine (slide 80) also causes halos, so no question claims that yellow-green halos occur with
digoxin alone; ivabradine is never offered as an option beside them.
"""

D = "Diuretics and Heart Failure Drugs.pptx"
IO_CLASS = "Identify diuretics and heart failure drug classes and commonly prescribed diuretics and heart failure drugs"
IO_MOA = "Describe the molecular mechanism of action of diuretics and heart failure drugs"
IO_IND = "Identify indications for commonly used diuretics and heart failure drugs"
IO_ADME = "Describe absorption, distribution, metabolism, and excretion of diuretics and heart failure drugs"
IO_TOX = "Summarize side effects and toxic manifestations of diuretics and heart failure drugs"
IO_AE = "Describe adverse effects of diuretics and heart failure drugs"
IO_CONTRA = "Identify contraindications for diuretics and heart failure drugs"
IO_INTER = "Discuss potential drug-drug, drug-food, and drug-herb interactions with diuretics and heart failure drugs"
IO_PROT = "List commonly used protocols and patient monitoring for diuretics and heart failure drugs"
IO_EDU = "Outline appropriate patient education for diuretics and heart failure drugs"


def Q(topic, io, slot, q, opts, slide):
    return {"topic": topic, "io": io, "slot": slot, "q": q, "opts": opts, "c": 0, "cite": "%s, Slide %d" % (D, slide)}


QUESTIONS = [

# ---- structure and class ----------------------------------------------------------
Q("Structure and class", IO_CLASS, "class",
  "Which structural features of digoxin are essential for its activity?",
  [["A lactone ring and a steroid nucleus", "Correct. The lactone ring and the steroid nucleus are essential for activity; the attached sugar molecules only modify absorption, half-life and metabolism."],
   ["A lactone ring and the sugar molecules", "The steroid nucleus is also essential, and the sugar molecules are not: they only influence absorption, half-life and metabolism."],
   ["A steroid nucleus and the sugar molecules", "The lactone ring is also essential for activity, and the sugar molecules are not; they influence absorption, half-life and metabolism."],
   ["The sugar molecules and a benzene ring", "Neither is the essential part. Activity depends on the lactone ring and the steroid nucleus; the sugars only change absorption and half-life."]], 61),

Q("Structure and class", IO_ADME, "class",
  "Which properties of digoxin do its attached sugar molecules influence?",
  [["Absorption, half-life and metabolism", "Correct. The sugar molecules shape how digoxin is absorbed, how long it lasts and how it is metabolized; activity comes from the lactone ring and steroid nucleus."],
   ["Activation of beta-1 receptors", "Digoxin does not act through beta-1 receptors at all; its activity depends on the lactone ring and steroid nucleus, and the sugars change absorption, half-life and metabolism."],
   ["Selectivity for atrial over ventricular cells", "No such selectivity is attributed to the sugars; they influence absorption, half-life and metabolism, while activity depends on the ring and nucleus."],
   ["Affinity for digoxin immune Fab fragments", "Antibody fragment affinity is not a function of the sugars; they influence absorption, half-life and metabolism of the drug."]], 61),

Q("Structure and class", IO_CLASS, "class",
  "Which drug family does digoxin belong to?",
  [["Digitalis glycoside", "Correct. Digoxin is a digitalis glycoside: a lactone ring and steroid nucleus with attached sugars, acting on the sodium-potassium pump of cardiac cells."],
   ["Phosphodiesterase 3 inhibitor", "Phosphodiesterase 3 inhibitors are milrinone and inamrinone, which raise cyclic adenosine monophosphate; digoxin is a digitalis glycoside that blocks the sodium-potassium pump."],
   ["Beta-1 receptor agonist", "Stimulating beta-1 receptors is what dobutamine does; digoxin is a digitalis glycoside that raises contractility by blocking the sodium-potassium pump."],
   ["Hyperpolarization-activated channel blocker", "Blocking the hyperpolarization-activated channel is what ivabradine does; digoxin is a digitalis glycoside that inhibits the sodium-potassium pump."]], 61),

# ---- mechanism --------------------------------------------------------------------
Q("Mechanism", IO_MOA, "mechanism",
  "Which enzyme does digoxin inhibit?",
  [["Sodium-potassium ATPase", "Correct. Digoxin inhibits the sodium-potassium ATPase pump, which is the starting point of both its inotropic and its neurohormonal actions."],
   ["Phosphodiesterase 3", "Phosphodiesterase 3 is inhibited by milrinone and inamrinone, not by digoxin, which acts on the sodium-potassium ATPase pump."],
   ["Neprilysin", "Neprilysin is inhibited by sacubitril, which keeps natriuretic peptides and bradykinin from being broken down; digoxin inhibits sodium-potassium ATPase."],
   ["Carbonic anhydrase", "Carbonic anhydrase is inhibited by acetazolamide and related diuretics; digoxin inhibits the sodium-potassium ATPase pump of cardiac cells."]], 62),

Q("Mechanism", IO_MOA, "mechanism",
  "Which intracellular ion rises first when digoxin blocks the sodium-potassium pump, and then raises intracellular calcium?",
  [["Sodium", "Correct. Pump inhibition traps sodium in the cell, and the sodium-calcium exchanger then raises intracellular calcium, so the fibers shorten with more force."],
   ["Potassium", "Intracellular potassium falls rather than rises when the pump is blocked, because the pump is what carries potassium into the cell."],
   ["Chloride", "Chloride is not the ion trapped by the pump; blocking the pump raises intracellular sodium, which then raises calcium through the exchanger."],
   ["Magnesium", "Magnesium is not the ion that accumulates; pump inhibition raises intracellular sodium, which in turn raises intracellular calcium."]], 62),

Q("Mechanism", IO_MOA, "mechanism",
  "Which effect describes the older, inotropic understanding of how digoxin works?",
  [["Greater force of cardiac muscle contraction", "Correct. The older view is a positive inotropic action, a stronger contraction; the newer view adds neurohormonal effects."],
   ["Lower preload through increased urine flow", "Lowering preload through urine flow is a diuretic action; digoxin is described as increasing the force of contraction."],
   ["Blocked pacemaker current in the sinoatrial node", "Blocking the pacemaker current describes ivabradine; digoxin is described as increasing the force of contraction."],
   ["Balanced dilation of arteries and veins", "Balanced arterial and venous dilation is described for milrinone and inamrinone; digoxin is described as increasing contraction force."]], 63),

Q("Mechanism", IO_MOA, "mechanism",
  "Which autonomic change is part of the newer, neurohormonal action of digoxin?",
  [["Lower sympathetic and higher parasympathetic activity", "Correct. Digoxin lowers sympathetic and raises parasympathetic nervous system activity, which slows the heart and resensitizes the baroreflex."],
   ["Higher sympathetic and lower parasympathetic activity", "That is the reverse; sympathetic activity falls and parasympathetic activity rises, which lowers blood pressure and heart rate."],
   ["Higher sympathetic and higher parasympathetic activity", "Sympathetic activity does not rise; it falls with digoxin while parasympathetic activity rises."],
   ["Lower sympathetic and lower parasympathetic activity", "Parasympathetic activity does not fall; it rises, particularly in the atrioventricular node and conduction system."]], 63),

Q("Mechanism", IO_MOA, "mechanism",
  "Which neurohormonal system does digoxin suppress in heart failure?",
  [["Renin-angiotensin-aldosterone system", "Correct. Digoxin lowers renin-angiotensin-aldosterone activity, which reduces remodeling and structural change and improves tissue perfusion."],
   ["Parasympathetic nervous system", "The parasympathetic system is increased by digoxin, not suppressed; the system it suppresses is the renin-angiotensin-aldosterone system."],
   ["Baroreflex sensing system", "Digoxin resensitizes the baroreflex rather than suppressing it; the suppressed system is renin-angiotensin-aldosterone."],
   ["Natriuretic peptide system", "Raising natriuretic peptides is the effect of sacubitril, not digoxin; digoxin suppresses renin-angiotensin-aldosterone activity."]], 65),

Q("Mechanism", IO_MOA, "mechanism",
  "In which part of the heart does digoxin raise parasympathetic activity?",
  [["Atrioventricular node", "Correct. Parasympathetic activity rises in the atrioventricular node and conduction system, which slows conduction and heart rate."],
   ["Ventricular contractile muscle", "Parasympathetic activity rises in the atrioventricular node and conduction system; ventricular muscle gains force from the pump effect instead."],
   ["Coronary artery walls", "The parasympathetic rise is described in the atrioventricular node and conduction system, not in the coronary vessels."],
   ["Pulmonary vein sleeves", "No parasympathetic effect is described there; it occurs in the atrioventricular node and conduction system."]], 64),

Q("Mechanism", IO_MOA, "mechanism",
  "Which inotropic drug lowers heart rate instead of raising it?",
  [["Digoxin", "Correct. Resetting the baroreflex and raising parasympathetic activity slow the heart rate, while the contraction becomes stronger."],
   ["Dobutamine", "Dobutamine is a beta-1 agonist that stimulates the force of contraction more than the rate, and it does not slow the heart."],
   ["Milrinone", "Milrinone adds contractility plus vasodilation and carries a risk of ventricular arrhythmia; it is not described as slowing the heart."],
   ["Dopamine", "Dopamine acts through dopamine and beta receptors to support output; it is not the inotrope that lowers heart rate."]], 64),

# ---- clinical benefit and place in therapy ----------------------------------------
Q("Benefits and place", IO_IND, "indication",
  "Which clinical benefit does digoxin provide in heart failure?",
  [["Fewer hospitalizations", "Correct. Digoxin improves symptoms, exercise tolerance and quality of life and lowers the number of hospitalizations."],
   ["Longer survival", "Digoxin has no survival benefit; it improves symptoms, exercise tolerance, quality of life and hospitalization rates."],
   ["Slower disease progression", "There is no evidence that digoxin slows disease progression; its benefits are symptomatic and fewer hospitalizations."],
   ["Reversal of the underlying cardiomyopathy", "Digoxin does not reverse the disease or slow its progression; its benefits are better symptoms, exercise tolerance and fewer hospitalizations."]], 66),

Q("Benefits and place", IO_IND, "indication",
  "Why is digoxin an add-on rather than a mandatory drug in heart failure?",
  [["It gives no survival benefit", "Correct. Mandatory drugs are the ones that prolong life; digoxin only relieves symptoms and reduces hospitalizations, so it is optional."],
   ["It shortens survival", "Digoxin is not shown to shorten survival; it is optional because it gives no survival benefit while relieving symptoms."],
   ["It does not relieve symptoms", "Digoxin does relieve symptoms and improve exercise tolerance; it is optional because it does not improve survival."],
   ["It cannot be given with diuretics", "Digoxin is given on top of diuretics; it is optional because it provides no survival benefit."]], 66),

Q("Benefits and place", IO_IND, "indication",
  "Which statement about digoxin and the course of heart failure is correct?",
  [["It has no evidence of slowing progression", "Correct. There is no evidence that digoxin slows disease progression; it improves symptoms but is not disease-modifying."],
   ["It slows progression as angiotensin-converting enzyme inhibitors do", "Angiotensin-converting enzyme inhibitors slow progression and prolong survival; for digoxin there is no evidence of slowed progression."],
   ["It halts progression when added to a diuretic", "Pairing it with a diuretic relieves symptoms; there is no evidence that digoxin slows disease progression."],
   ["It slows progression at higher concentrations", "Higher concentrations may be linked to worse outcomes, not slower progression; there is no evidence that digoxin slows disease progression."]], 67),

Q("Benefits and place", IO_IND, "indication",
  "In which patient with heart failure is digoxin mainly added?",
  [["One still symptomatic on optimal standard drugs", "Correct. Digoxin is mainly added for patients who remain symptomatic despite optimal doses of angiotensin-converting enzyme inhibitors, beta blockers and diuretics."],
   ["One newly diagnosed and without symptoms", "Digoxin is not a starting drug; it is added when symptoms persist despite optimal angiotensin-converting enzyme inhibitor, beta blocker and diuretic therapy."],
   ["One in whom survival benefit is the only goal", "Digoxin gives no survival benefit, so it is added for persistent symptoms, not to prolong life; other drugs do that."],
   ["One whose pulse is already very slow", "A slow pulse or severe bradycardia is a contraindication; digoxin is for persistent symptoms on standard therapy."]], 67),

Q("Benefits and place", IO_IND, "indication",
  "Which rhythm disorder alongside heart failure makes digoxin useful for rate control?",
  [["Atrial fibrillation", "Correct. Digoxin's rate-slowing properties make it useful for rate control in atrial fibrillation together with heart failure."],
   ["Ventricular tachycardia", "Ventricular tachycardia is a contraindication to digoxin, which can itself provoke ventricular arrhythmias."],
   ["Sick sinus syndrome", "Sick sinus syndrome is a contraindication; digoxin is used for rate control in atrial fibrillation with heart failure."],
   ["Advanced atrioventricular block", "Advanced atrioventricular block is a contraindication, because digoxin slows nodal conduction further; atrial fibrillation is the rate-control use."]], 67),

Q("Benefits and place", IO_IND, "indication",
  "Which type of ventricular dysfunction in symptomatic heart failure is digoxin considered for?",
  [["Systolic dysfunction", "Correct. Digoxin is considered for symptomatic heart failure with systolic dysfunction, where contractility is reduced."],
   ["Diastolic dysfunction", "Diastolic dysfunction is impaired relaxation with preserved ejection fraction; digoxin is considered for systolic dysfunction, where contraction is weak."],
   ["Right atrial enlargement", "That is not a heart failure category; digoxin is considered for symptomatic heart failure with systolic dysfunction."],
   ["Isolated pericardial effusion", "That is not an indication; digoxin is considered for symptomatic heart failure with systolic dysfunction."]], 67),

# ---- monitoring --------------------------------------------------------------------
Q("Monitoring", IO_PROT, "monitoring",
  "Which measurement is followed against a target range during digoxin therapy?",
  [["Serum digoxin concentration", "Correct. A serum digoxin concentration is followed against a target range, and higher concentrations may be linked to worse outcomes in heart failure."],
   ["Plasma renin activity", "Plasma renin activity is not the monitored measure; digoxin itself has a target concentration that is followed."],
   ["Serum creatine kinase", "Creatine kinase is not followed for digoxin; the drug has its own serum concentration target."],
   ["Platelet count", "Thrombocytopenia is a concern with milrinone, not digoxin; digoxin has its own serum concentration that is followed against a target range."]], 65),

Q("Monitoring", IO_PROT, "monitoring",
  "Why is the digoxin concentration kept in a target range rather than pushed higher?",
  [["Higher concentrations may give worse outcomes", "Correct. Higher concentrations in heart failure may be associated with worse outcomes, and they raise toxicity risk without added benefit."],
   ["Higher concentrations remove the survival gap", "Digoxin has no survival benefit at any concentration; higher concentrations may be associated with worse outcomes."],
   ["Lower concentrations cause toxicity first", "Toxicity comes with higher concentrations; lower targets are chosen because higher ones may be associated with worse outcomes."],
   ["Higher concentrations lose inotropic effect", "Inotropic effect does not vanish at higher concentrations; the concern is that higher concentrations may give worse outcomes."]], 65),

Q("Monitoring", IO_PROT, "monitoring",
  "Which serum potassium goal protects a patient taking digoxin together with a thiazide diuretic?",
  [["Above 4.0 milliequivalents per liter", "Correct. Thiazides lower potassium and raise digitalis toxicity, so potassium should be kept above 4.0 milliequivalents per liter."],
   ["Below 3.5 milliequivalents per liter", "A low potassium is the hazard, because hypokalemia raises digitalis toxicity; potassium should stay above 4.0 milliequivalents per liter."],
   ["Between 3.0 and 3.5 milliequivalents per liter", "That range is hypokalemia, which raises digitalis toxicity; the goal is above 4.0 milliequivalents per liter."],
   ["Any value if magnesium is normal", "Normal magnesium does not remove the risk; potassium itself should be kept above 4.0 milliequivalents per liter with a thiazide."]], 29),

# ---- interactions ------------------------------------------------------------------
Q("Interactions", IO_INTER, "interaction",
  "A patient taking digoxin is started on furosemide. Which concern does the combination raise?",
  [["Arrhythmias from electrolyte loss", "Correct. Loop diuretics waste potassium and magnesium, and low levels of both with digitalis produce arrhythmias."],
   ["Loss of the digoxin inotropic effect", "Loop diuretics do not cancel the inotropic effect; they lower potassium and magnesium, which makes digitalis arrhythmias more likely."],
   ["Hyperkalemia with conduction block", "Loop diuretics lower rather than raise potassium; the concern is hypokalemia and hypomagnesemia causing arrhythmias."],
   ["Faster renal clearance of digoxin", "Clearance is not what changes; the interaction is hypokalemia and hypomagnesemia with digitalis, causing arrhythmias."]], 19),

Q("Interactions", IO_INTER, "interaction",
  "Potassium loss from a thiazide diuretic increases the toxicity of which heart failure drug?",
  [["Digoxin", "Correct. Thiazides increase digitalis toxicity through potassium loss, so potassium must be kept above 4.0 milliequivalents per liter."],
   ["Carvedilol", "Carvedilol toxicity is not raised through potassium loss; the thiazide potassium-loss interaction of concern is with digoxin."],
   ["Spironolactone", "Spironolactone holds on to potassium, so a thiazide's potassium loss offsets it rather than raising its toxicity; the interaction of concern is with digoxin."],
   ["Sacubitril-valsartan", "Sacubitril-valsartan tends to raise potassium, so a thiazide's potassium loss offsets it rather than raising its toxicity; the concern is digoxin."]], 29),

Q("Interactions", IO_INTER, "interaction",
  "Which diuretic-related abnormality raises the risk of digoxin toxicity?",
  [["Hypokalemia", "Correct. Hypokalemia, especially from loop or thiazide diuretics, raises digitalis toxicity and arrhythmia risk, together with hypomagnesemia."],
   ["Hyperuricemia", "Hyperuricemia from diuretics causes gout but does not raise digitalis toxicity; potassium and magnesium loss does."],
   ["Hyponatremia", "Hyponatremia from loop diuretics can cause seizures but is not the electrolyte problem that raises digitalis toxicity; hypokalemia is."],
   ["Hypophosphatemia", "Phosphate is not the electrolyte named; the diuretic interaction with digitalis is hypokalemia and hypomagnesemia causing arrhythmias."]], 19),

# ---- toxicity -----------------------------------------------------------------------
Q("Toxicity", IO_TOX, "adverse effect",
  "Which gastrointestinal symptoms are early signs of digoxin toxicity?",
  [["Anorexia and nausea", "Correct. Anorexia and nausea are the gastrointestinal signs listed for digoxin toxicity."],
   ["Constipation and bloating", "Constipation is listed for thiazides, not digoxin; the gastrointestinal signs of digoxin toxicity are anorexia and nausea."],
   ["Heartburn and belching", "These are not the listed signs; digoxin toxicity causes anorexia and nausea."],
   ["Abdominal cramps with bloody stool", "Bloody stool is not part of digoxin toxicity; anorexia and nausea are the gastrointestinal signs."]], 68),

Q("Toxicity", IO_TOX, "adverse effect",
  "Which term names the yellow-green vision of digoxin toxicity?",
  [["Xanthopsia", "Correct. Xanthopsia is yellow vision, with yellow-green halos and shining lights around objects, a visual sign of digoxin toxicity."],
   ["Nyctalopia", "Nyctalopia is poor vision in dim light; the yellow-green vision of digoxin toxicity is xanthopsia."],
   ["Diplopia", "Diplopia is double vision; the yellow-green tint of digoxin toxicity is called xanthopsia."],
   ["Scotoma", "A scotoma is a blind spot in the visual field; the yellow-green tint of digoxin toxicity is called xanthopsia."]], 68),

Q("Toxicity", IO_TOX, "adverse effect",
  "A patient with heart failure reports seeing yellow-green halos around streetlights. Which drug is the likely cause?",
  [["Digoxin", "Correct. Yellow-green halos and blurred vision are visual signs of digoxin toxicity, which calls for checking a serum concentration."],
   ["Carvedilol", "Carvedilol's adverse effects are not visual halos; yellow-green halos point to digoxin toxicity."],
   ["Spironolactone", "Spironolactone causes hyperkalemia, gynecomastia and menstrual changes, not yellow-green halos, which point to digoxin."],
   ["Furosemide", "Furosemide causes volume depletion, hypokalemia and ototoxicity, not yellow-green halos, which point to digoxin."]], 68),

Q("Toxicity", IO_TOX, "adverse effect",
  "Which symptom of digoxin toxicity arises from the central nervous system?",
  [["Abnormal dreams", "Correct. Delirium, fatigue, confusion, dizziness and abnormal dreams are the central symptoms of digoxin toxicity."],
   ["Hearing loss", "Hearing damage is an ototoxicity of loop diuretics, not a central symptom of digoxin toxicity."],
   ["Gynecomastia", "Gynecomastia is an androgen-receptor effect of spironolactone, not a central symptom of digoxin toxicity."],
   ["Dry cough", "Dry cough is an effect of angiotensin-converting enzyme inhibitors; digoxin's central symptoms include confusion and abnormal dreams."]], 69),

Q("Toxicity", IO_TOX, "adverse effect",
  "Which electrocardiogram change accompanies digoxin toxicity?",
  [["Lengthened PR interval", "Correct. Nodal slowing lengthens the PR interval, shortens the QT interval and depresses the ST segment."],
   ["Shortened PR interval", "The PR interval lengthens, not shortens, because digoxin slows nodal conduction."],
   ["Lengthened QT interval", "The QT interval shortens rather than lengthens in digoxin toxicity."],
   ["Elevated ST segment", "The ST segment is depressed, not elevated, in digoxin toxicity."]], 70),

Q("Toxicity", IO_TOX, "adverse effect",
  "Which heart rate change is the most typical cardiac sign of digoxin toxicity?",
  [["Bradycardia", "Correct. Nodal slowing makes bradycardia the typical cardiac sign, although digoxin can provoke almost any arrhythmia."],
   ["Sinus tachycardia", "Digoxin slows the heart through nodal slowing and parasympathetic action; bradycardia is the typical rate change."],
   ["A fixed rapid regular rate", "Digoxin does not lock in a rapid rate; nodal slowing makes bradycardia the typical change."],
   ["Heart rate with no change", "Digoxin toxicity slows nodal conduction and typically causes bradycardia, which can progress to block."]], 70),

Q("Toxicity", IO_TOX, "adverse effect",
  "Which process underlies the ventricular arrhythmias of digoxin toxicity?",
  [["Digoxin-induced afterdepolarization", "Correct. Digoxin-induced afterdepolarization makes ventricular cells fire extra beats, seen as premature ventricular beats and ventricular arrhythmia."],
   ["Accelerated pacemaker current in the sinoatrial node", "That would raise sinus rate; the ventricular arrhythmias come from digoxin-induced afterdepolarization, while the nodes are slowed."],
   ["Loss of sodium-potassium ATPase from the cell", "The pump is inhibited, not lost; the arrhythmia mechanism is digoxin-induced afterdepolarization."],
   ["Direct calcium channel blockade", "Digoxin does not block calcium channels; it raises intracellular calcium and causes afterdepolarization."]], 70),

# ---- contraindications ----------------------------------------------------------------
Q("Contraindications", IO_CONTRA, "contraindication",
  "Which conduction disorder contraindicates digoxin?",
  [["Advanced atrioventricular block", "Correct. Digoxin slows nodal conduction, so advanced atrioventricular block is a contraindication."],
   ["Atrial fibrillation with heart failure", "Atrial fibrillation with heart failure is a use of digoxin for rate control, not a contraindication."],
   ["Normal sinus rhythm", "A normal sinus rhythm is not a contraindication; digoxin slows nodal conduction, so advanced atrioventricular block is."],
   ["Sinus tachycardia", "Sinus tachycardia is not a contraindication; the conduction disorder that contraindicates digoxin is advanced atrioventricular block."]], 71),

Q("Contraindications", IO_CONTRA, "contraindication",
  "Which heart rate disorder contraindicates digoxin?",
  [["Severe bradycardia or sick sinus syndrome", "Correct. Digoxin slows the nodes further, so severe bradycardia and sick sinus syndrome are contraindications."],
   ["Atrial fibrillation with a rapid rate", "A rapid atrial fibrillation rate with heart failure is a use of digoxin for rate control, not a contraindication."],
   ["Mild sinus tachycardia", "Mild tachycardia is not listed; digoxin is contraindicated in severe bradycardia and sick sinus syndrome, where it slows the nodes further."],
   ["Normal sinus rhythm", "A normal sinus rhythm is not a contraindication; digoxin is contraindicated in severe bradycardia and sick sinus syndrome."]], 71),

Q("Contraindications", IO_CONTRA, "contraindication",
  "Which ventricular rhythm problem contraindicates digoxin?",
  [["Ventricular tachycardia", "Correct. Premature ventricular beats and ventricular tachycardia are contraindications, because digoxin makes the ventricles more irritable."],
   ["Atrial fibrillation", "Atrial fibrillation with heart failure is a use of digoxin, not a contraindication."],
   ["Normal sinus rhythm", "A normal sinus rhythm is not a contraindication; ventricular tachycardia and premature ventricular beats are."],
   ["Sinus tachycardia", "Sinus tachycardia is not the listed contraindication; ventricular tachycardia and premature ventricular beats are."]], 71),

Q("Contraindications", IO_CONTRA, "contraindication",
  "Which cardiac syndrome contraindicates digoxin?",
  [["Wolff-Parkinson-White", "Correct. Wolff-Parkinson-White syndrome is listed among the contraindications to digoxin."],
   ["Long QT syndrome", "Long QT syndrome is not the listed contraindication; Wolff-Parkinson-White syndrome is."],
   ["Brugada syndrome", "Brugada syndrome is not the listed contraindication; Wolff-Parkinson-White syndrome is."],
   ["Mitral valve prolapse", "Mitral valve prolapse is not listed as a contraindication; Wolff-Parkinson-White syndrome is."]], 71),

Q("Contraindications", IO_CONTRA, "contraindication",
  "Which combination of electrolyte disturbances raises the risk of digoxin toxicity?",
  [["Low potassium, low magnesium and high calcium", "Correct. Hypokalemia, hypomagnesemia and hypercalcemia all make digoxin toxicity more likely and are cautions for its use."],
   ["Low potassium, high magnesium and low calcium", "High magnesium and low calcium are not the risks; low magnesium and high calcium raise digoxin toxicity."],
   ["High sodium, high magnesium and low calcium", "None of these is the pattern; digoxin toxicity is raised by low potassium, low magnesium and high calcium."],
   ["Low potassium, high magnesium and high calcium", "Magnesium is a risk when it is low, not high; digoxin toxicity is raised by low potassium, low magnesium and high calcium."]], 71),

# ---- antidote ------------------------------------------------------------------------
Q("Antidote", IO_TOX, "drug choice",
  "Which drug rapidly reverses life-threatening digoxin toxicity?",
  [["Digoxin immune Fab", "Correct. Digoxin immune Fab is an antibody that binds digoxin and rapidly reverses toxicity."],
   ["Atropine", "Atropine can raise a slow heart rate but does not neutralize digoxin; the antibody fragment does."],
   ["Protamine sulfate", "Protamine sulfate reverses heparin; digoxin toxicity is reversed by digoxin immune Fab."],
   ["Naloxone", "Naloxone reverses opioids; digoxin toxicity is reversed by digoxin immune Fab."]], 72),

Q("Antidote", IO_TOX, "drug choice",
  "From which animal is digoxin immune Fab produced?",
  [["Sheep", "Correct. Healthy sheep are immunized with digoxin coupled to human serum albumin, and their antibody is the source of the antidote."],
   ["Rabbits", "The antibody source is sheep, immunized with digoxin coupled to human serum albumin, not rabbits."],
   ["Horses", "The antibody source is sheep immunized with digoxin coupled to human serum albumin, not horses."],
   ["Goats", "The antibody source is sheep immunized with digoxin coupled to human serum albumin, not goats."]], 72),

Q("Antidote", IO_MOA, "mechanism",
  "How does digoxin immune Fab reverse toxicity?",
  [["It binds digoxin more tightly than the pump does", "Correct. Its affinity for digoxin exceeds that of the sodium-potassium pump, so it pulls digoxin away and reverses toxicity rapidly."],
   ["It blocks the sodium-calcium exchanger", "It does not act on the exchanger; it binds digoxin with a higher affinity than the pump has."],
   ["It stimulates the sodium-potassium pump", "It does not stimulate the pump; it neutralizes digoxin by binding it with a higher affinity than the sodium-potassium pump has."],
   ["It restores potassium in the heart muscle", "It does not give potassium; it neutralizes digoxin by binding it with higher affinity than the pump."]], 72),

]
