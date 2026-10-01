# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Diuretics and Heart Failure Drugs (Lecture 9), topic: other heart failure drugs.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

SOURCE. Diuretics and Heart Failure Drugs.pptx slides 73-82: aldosterone antagonists in heart failure, milrinone and
inamrinone, dobutamine and dopamine, ivabradine, sacubitril-valsartan, SGLT2 inhibitors. Picture-only slide 74 (the
structures of milrinone and inamrinone) was read by eye into tools/pharm_e3/ocr.json.

WEIGHTING (Dr. McInnis): indications, patient education, adverse effects, contraindications, drug choice and interactions
outnumber mechanism.

LEFT OUT ON PURPOSE (no key built on them):
  * "class IV" (slide 37) versus "grade III or IV" (slide 73) for aldosterone antagonists in heart failure -- the two
    slides disagree and current practice is broader, so the key is "advanced heart failure" only;
  * the ~10 percent gynecomastia figure (slide 73), kept qualitative;
  * dopamine "maintains renal function" (slide 77) -- not supported by outcome trials; dopamine is asked only as an
    agent acting through dopamine and beta receptors;
  * the brand name Procoralan, and anything beyond the slide text about dobutamine and dopamine (Dr. Wood's remark that
    higher doses of dopamine constrict arteries is not on a slide);
  * which of milrinone or dobutamine suits a LOW blood pressure -- only the milrinone-with-vasodilation, high blood
    pressure shape is keyed, because it follows from slide 75;
  * euglycemic ketoacidosis, genital infections other than fungal infection, and angioedema history as a contraindication
    to sacubitril-valsartan are true but not on the slides.
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

# ---- aldosterone antagonists in heart failure -------------------------------------
Q("Aldosterone antagonists", IO_IND, "indication",
  "Which type of diuretic reduces mortality in advanced heart failure?",
  [["An aldosterone antagonist", "Correct. Spironolactone reduces mortality in advanced heart failure; the other diuretic classes relieve symptoms only."],
   ["A loop diuretic", "Loop diuretics are the mainstay for symptoms but show no evidence of decreasing progression or mortality."],
   ["A thiazide diuretic", "Thiazides are not potent enough for most heart failure patients and give no mortality benefit."],
   ["A carbonic anhydrase inhibitor", "Carbonic anhydrase inhibitors are weak diuretics with no role in lowering heart failure mortality; aldosterone antagonists reduce it."]], 73),

Q("Aldosterone antagonists", IO_CONTRA, "contraindication",
  "Which laboratory finding makes a heart failure patient ineligible for spironolactone?",
  [["Potassium above 5 milliequivalents per liter", "Correct. Spironolactone holds on to potassium, so a potassium above 5 milliequivalents per liter excludes it, as does a high serum creatinine."],
   ["Potassium below 3.5 milliequivalents per liter", "Low potassium is not the exclusion; spironolactone spares potassium, so the danger is a potassium above 5."],
   ["Sodium above 145 milliequivalents per liter", "Sodium is not the exclusion; the findings that exclude spironolactone are high potassium and high serum creatinine."],
   ["Chloride above 110 milliequivalents per liter", "Chloride is not the exclusion; the findings that exclude spironolactone are high potassium and high serum creatinine."]], 73),

Q("Aldosterone antagonists", IO_AE, "adverse effect",
  "Which adverse effect of spironolactone in men may respond to a lower dose?",
  [["Gynecomastia", "Correct. Gynecomastia occurs in a notable share of men on spironolactone and may respond to a lower dose; eplerenone avoids it."],
   ["Hearing loss", "Hearing loss is an ototoxicity of loop diuretics, not an effect of spironolactone; its androgen-receptor effect is gynecomastia."],
   ["Yellow-green halos", "Yellow-green halos are a sign of digoxin toxicity; spironolactone's androgen-receptor effect is gynecomastia in men."],
   ["Dry cough", "Dry cough is an effect of angiotensin-converting enzyme inhibitors; spironolactone causes gynecomastia in men."]], 73),

Q("Aldosterone antagonists", IO_EDU, "drug choice",
  "A man taking spironolactone for heart failure develops breast enlargement. Which change to his therapy fits?",
  [["Switch to eplerenone", "Correct. Eplerenone has far less androgen-receptor activity, so it avoids gynecomastia while keeping the aldosterone blockade."],
   ["Add a loop diuretic", "A loop diuretic does not treat breast enlargement; the androgen-receptor effect is avoided by switching to eplerenone."],
   ["Add a potassium supplement", "Potassium supplements are dangerous with an aldosterone antagonist because of hyperkalemia, and they do not treat gynecomastia."],
   ["Stop all heart failure drugs", "Stopping everything is not needed; eplerenone gives the aldosterone blockade without the androgen-receptor effect."]], 73),

Q("Aldosterone antagonists", IO_MOA, "mechanism",
  "Why do aldosterone antagonists slow progression of heart failure?",
  [["They slow left ventricular remodeling", "Correct. Neurohormonal inhibition of aldosterone slows remodeling of the left ventricle and so slows heart failure progression."],
   ["They raise preload through sodium retention", "Aldosterone antagonists promote sodium loss and potassium retention; their benefit is slower remodeling."],
   ["They stimulate the sympathetic system", "Neurohormonal inhibition lowers harmful activation; aldosterone antagonists slow remodeling of the left ventricle."],
   ["They block neprilysin", "Neprilysin is inhibited by sacubitril; aldosterone antagonists slow progression through neurohormonal inhibition and slower remodeling."]], 73),

# ---- milrinone and inamrinone -------------------------------------------------------
Q("Milrinone and inamrinone", IO_MOA, "mechanism",
  "Which enzyme do milrinone and inamrinone inhibit?",
  [["Phosphodiesterase 3", "Correct. They inhibit cyclic adenosine monophosphate phosphodiesterase 3, raising cyclic adenosine monophosphate in the heart and giving direct stimulation of contraction."],
   ["Phosphodiesterase 5", "Phosphodiesterase 5 breaks down cyclic guanosine monophosphate and is the target of drugs such as sildenafil; milrinone acts on isoform 3."],
   ["Neprilysin", "Neprilysin is inhibited by sacubitril, not milrinone; milrinone and inamrinone inhibit phosphodiesterase 3."],
   ["Sodium-potassium ATPase", "The sodium-potassium pump is inhibited by digoxin; milrinone and inamrinone inhibit phosphodiesterase 3."]], 74),

Q("Milrinone and inamrinone", IO_MOA, "mechanism",
  "Which messenger rises in heart muscle when phosphodiesterase 3 is inhibited?",
  [["Cyclic adenosine monophosphate", "Correct. Blocking phosphodiesterase 3 prevents breakdown of cyclic adenosine monophosphate, which stimulates contraction."],
   ["Cyclic guanosine monophosphate", "Cyclic guanosine monophosphate is broken down by phosphodiesterase 5; phosphodiesterase 3 breaks down cyclic adenosine monophosphate."],
   ["Inositol trisphosphate", "Inositol trisphosphate is not the messenger involved; phosphodiesterase 3 inhibition raises cyclic adenosine monophosphate."],
   ["Nitric oxide in the myocardium", "Nitric oxide is not the messenger; phosphodiesterase 3 inhibition raises cyclic adenosine monophosphate."]], 74),

Q("Milrinone and inamrinone", IO_MOA, "mechanism",
  "Which pair of actions describes milrinone and inamrinone?",
  [["Inotropic and vasodilator", "Correct. They directly stimulate myocardial contraction and also dilate arteries and veins in a balanced way."],
   ["Inotropic and vasoconstrictor", "They dilate rather than constrict vessels, which lowers afterload while raising contractility."],
   ["Negative inotropic and vasodilator", "They raise contractility rather than lowering it; the vasodilation is combined with a direct stimulation of contraction."],
   ["Inotropic and diuretic", "They are not diuretics; their actions are direct stimulation of contraction and balanced arterial and venous dilation."]], 75),

Q("Milrinone and inamrinone", IO_IND, "indication",
  "For which use are milrinone and inamrinone approved?",
  [["Short-term use in acute decompensated failure", "Correct. They are approved for short-term intravenous use in acute decompensated heart failure and then withdrawn once the patient stabilizes."],
   ["Long-term maintenance in stable failure", "Long-term use is associated with higher mortality and morbidity than placebo, so they are not maintenance drugs."],
   ["Prevention of failure in healthy adults", "They are not preventive; they support the failing heart in acute decompensation for a short time."],
   ["Outpatient rate control in atrial fibrillation", "Rate control is not their use; they are approved for short-term intravenous use in acute decompensated heart failure."]], 76),

Q("Milrinone and inamrinone", IO_AE, "adverse effect",
  "Which risk comes with long-term use of milrinone or inamrinone?",
  [["Higher mortality and morbidity than placebo", "Correct. Long-term use is associated with higher mortality and morbidity than placebo, so use stays short term."],
   ["Better survival with more edema", "Survival is worse, not better, with long-term use; it is associated with higher mortality and morbidity than placebo."],
   ["No difference from placebo", "Long-term use is not neutral; it is associated with higher mortality and morbidity than placebo."],
   ["Slower progression of the disease", "There is no slowing of progression; long-term use is associated with higher mortality and morbidity than placebo."]], 76),

Q("Milrinone and inamrinone", IO_AE, "adverse effect",
  "Which hematologic adverse effect do milrinone and inamrinone cause?",
  [["Thrombocytopenia", "Correct. Thrombocytopenia is the hematologic adverse effect listed for these phosphodiesterase 3 inhibitors."],
   ["Megaloblastic anemia", "Megaloblastic anemia is an oddity of triamterene, not of the phosphodiesterase 3 inhibitors, which cause thrombocytopenia."],
   ["Agranulocytosis", "Agranulocytosis is not the listed effect; thrombocytopenia is."],
   ["Polycythemia", "Polycythemia is not listed; thrombocytopenia is the hematologic effect of these drugs."]], 76),

Q("Milrinone and inamrinone", IO_AE, "adverse effect",
  "Which phosphodiesterase 3 inhibitor causes less thrombocytopenia?",
  [["Milrinone", "Correct. Thrombocytopenia occurs with both drugs, but milrinone causes less of it than inamrinone."],
   ["Inamrinone", "Inamrinone is the one that causes more thrombocytopenia, which is part of why milrinone is the more common choice."],
   ["Dobutamine", "Dobutamine is a beta-1 agonist, not a phosphodiesterase 3 inhibitor; milrinone is the inhibitor with less thrombocytopenia."],
   ["Dopamine", "Dopamine acts through dopamine and beta receptors, not phosphodiesterase 3; milrinone is the inhibitor with less thrombocytopenia."]], 76),

Q("Milrinone and inamrinone", IO_AE, "adverse effect",
  "Which cardiac adverse effect do milrinone and inamrinone share?",
  [["Ventricular arrhythmias", "Correct. Ventricular arrhythmias are listed for these drugs."],
   ["Symptomatic bradycardia", "Symptomatic bradycardia is an effect of ivabradine; these drugs raise contractility and risk ventricular arrhythmias."],
   ["Complete heart block", "Heart block is not their listed effect; ventricular arrhythmias are."],
   ["Sinus arrest", "Sinus arrest is not their listed effect; ventricular arrhythmias are."]], 76),

Q("Milrinone and inamrinone", IO_IND, "drug choice",
  "A patient in acute decompensated failure has high blood pressure and poor output. Which drug adds contractility and lowers afterload by dilating both arteries and veins?",
  [["Milrinone", "Correct. Milrinone stimulates contraction directly and dilates arteries and veins, lowering afterload while raising output."],
   ["Dobutamine", "Dobutamine is a beta-1 agonist that stimulates force without balanced arterial and venous dilation; that vasodilation comes from milrinone."],
   ["Digoxin", "Digoxin is for symptoms in chronic failure and is not used to lower afterload in acute decompensation."],
   ["Ivabradine", "Ivabradine slows the heart without adding contractility and is for chronic use; it does not lower afterload."]], 75),

# ---- dobutamine and dopamine ---------------------------------------------------------
Q("Dobutamine and dopamine", IO_MOA, "mechanism",
  "Which receptor does dobutamine selectively stimulate?",
  [["Beta-1 adrenergic receptor", "Correct. Dobutamine is a selective beta-1 agonist, so it stimulates the force of contraction."],
   ["Beta-2 adrenergic receptor", "Beta-2 receptors are not the selective target; dobutamine stimulates beta-1 receptors in the heart."],
   ["Alpha-1 adrenergic receptor", "Alpha-1 receptors are not the selective target; dobutamine stimulates beta-1 receptors."],
   ["Muscarinic receptor", "Muscarinic receptors are not the target; dobutamine is a selective beta-1 agonist."]], 77),

Q("Dobutamine and dopamine", IO_MOA, "physiology",
  "What does a dobutamine infusion increase more?",
  [["Force of contraction more than rate", "Correct. Dobutamine stimulates the force of contraction more than the rate of contraction."],
   ["Rate of contraction more than force", "It is the reverse: dobutamine, a beta-1 agonist, raises the force of contraction more than the rate."],
   ["Venous tone more than force", "Dobutamine's main effect is on force of contraction rather than venous tone."],
   ["Urine output more than force", "Its main effect is force of contraction; urine output is not its main action."]], 77),

Q("Dobutamine and dopamine", IO_PROT, "protocol",
  "How is dobutamine used in heart failure?",
  [["Short-term infusion to stabilize patients", "Correct. Dobutamine is given as a short-term intravenous infusion to stabilize patients."],
   ["Long-term oral maintenance therapy", "Dobutamine is an intravenous infusion for short-term stabilization, not long-term oral therapy."],
   ["Lifelong daily subcutaneous injection", "Dobutamine is not injected under the skin for life; it is a short-term intravenous infusion."],
   ["A single dose to reverse toxicity", "It does not reverse toxicity; it is a short-term infusion to stabilize patients."]], 77),

Q("Dobutamine and dopamine", IO_MOA, "mechanism",
  "Through which receptors does dopamine act?",
  [["Dopamine and beta receptors", "Correct. Dopamine infusions act through dopamine and beta receptors."],
   ["Muscarinic and nicotinic receptors", "Those are acetylcholine receptors; dopamine acts through dopamine and beta receptors."],
   ["Angiotensin and endothelin receptors", "Those are not its receptors; dopamine acts through dopamine and beta receptors."],
   ["Imidazoline and alpha-2 receptors", "Those are central sympatholytic targets; dopamine acts through dopamine and beta receptors."]], 77),

# ---- ivabradine ------------------------------------------------------------------------
Q("Ivabradine", IO_MOA, "mechanism",
  "Which channel does ivabradine block?",
  [["Hyperpolarization-activated channel", "Correct. Ivabradine blocks the hyperpolarization-activated cyclic nucleotide-gated channel, inhibiting the pacemaker current."],
   ["Voltage-gated calcium channel", "Calcium channels are blocked by verapamil and diltiazem; ivabradine blocks the hyperpolarization-activated channel."],
   ["Epithelial sodium channel", "Epithelial sodium channels are blocked by amiloride and triamterene; ivabradine blocks the hyperpolarization-activated channel."],
   ["Delayed rectifier potassium channel", "Potassium channel blockade is not its action; ivabradine blocks the hyperpolarization-activated channel."]], 79),

Q("Ivabradine", IO_MOA, "mechanism",
  "In which structure does ivabradine inhibit the pacemaker current?",
  [["Sinoatrial node", "Correct. Ivabradine inhibits the pacemaker current in the sinoatrial node, lowering heart rate."],
   ["Atrioventricular node", "The atrioventricular node is slowed by digoxin and beta blockers; ivabradine acts on the pacemaker current of the sinoatrial node."],
   ["Purkinje fibers", "Purkinje fibers are not where ivabradine acts; it inhibits the pacemaker current of the sinoatrial node."],
   ["Ventricular myocardium", "Ventricular muscle is not the target; ivabradine acts in the sinoatrial node and leaves contractility unchanged."]], 79),

Q("Ivabradine", IO_MOA, "physiology",
  "What distinguishes the effect of ivabradine from that of a beta blocker?",
  [["It slows the rate but not contractility", "Correct. Ivabradine reduces heart rate without affecting contractility, whereas beta blockers reduce both."],
   ["It slows contractility but not the rate", "It is the reverse: ivabradine lowers heart rate and does not affect contractility."],
   ["It raises the rate and lowers contractility", "It does not raise the rate; it reduces heart rate and leaves contractility alone."],
   ["It lowers both rate and contractility", "That describes beta blockers; ivabradine lowers only the heart rate."]], 79),

Q("Ivabradine", IO_IND, "indication",
  "Which heart failure patient is a candidate for ivabradine?",
  [["Sinus rhythm and rate above 70 on beta blockers", "Correct. Ivabradine is for patients maxed out on beta blockers who remain in normal sinus rhythm with a heart rate above 70."],
   ["Atrial fibrillation with a rapid ventricular rate", "Ivabradine is for normal sinus rhythm, and it raises the risk of atrial fibrillation; it is not used for atrial fibrillation."],
   ["Heart block with a very slow heart rate", "Heart block and bradycardia are contraindications, as with beta blockers."],
   ["Acute decompensation needing inotropic support", "Ivabradine adds no contractility and is not for acute support; it is for sinus rhythm with a rate above 70 on beta blockers."]], 79),

Q("Ivabradine", IO_IND, "indication",
  "Which outcomes does ivabradine reduce in heart failure?",
  [["Hospitalization and heart failure death", "Correct. Ivabradine has been shown to decrease hospitalization and heart failure related death."],
   ["Blood pressure and sodium retention", "Lowering blood pressure and sodium retention are not its benefits; it reduces hospitalization and heart failure related death."],
   ["Preload and afterload", "Ivabradine lowers heart rate only, without vasodilation; its shown benefit is fewer hospitalizations and heart failure deaths."],
   ["Glucose and uric acid levels", "Metabolic changes are not its benefit; it reduces hospitalization and heart failure related death."]], 79),

Q("Ivabradine", IO_AE, "adverse effect",
  "Which arrhythmia risk is increased by ivabradine?",
  [["Atrial fibrillation", "Correct. Ivabradine increases the risk of atrial fibrillation, and it can also cause symptomatic bradycardia."],
   ["Ventricular arrhythmias", "Ventricular arrhythmias are listed for milrinone and inamrinone; ivabradine raises the risk of atrial fibrillation."],
   ["Torsades de pointes", "Torsades is not the listed risk; ivabradine raises the risk of atrial fibrillation."],
   ["Asystole", "Asystole is not the listed risk; ivabradine raises the risk of atrial fibrillation and symptomatic bradycardia."]], 80),

Q("Ivabradine", IO_AE, "adverse effect",
  "Which visual adverse effect is described for ivabradine?",
  [["Phosphenes", "Correct. Phosphenes are transient brightness in a limited area of the visual field, from effects on retinal photoreceptors."],
   ["Xanthopsia", "Xanthopsia, a yellow-green tint, is a sign of digoxin toxicity; ivabradine causes phosphenes."],
   ["Cataract formation", "Cataracts are not described; ivabradine causes phosphenes, transient brightness in part of the visual field."],
   ["Optic neuritis", "Optic neuritis is not described; ivabradine causes phosphenes, transient brightness in part of the visual field."]], 80),

Q("Ivabradine", IO_EDU, "education",
  "A patient on ivabradine notices brief brightness in part of the visual field. What should the patient be told?",
  [["It may resolve on its own", "Correct. Visual phosphenes can resolve on their own, so the patient can be reassured and told to report persistent symptoms."],
   ["It is permanent retinal damage", "The effect is retinal persistency that can resolve on its own, not permanent damage."],
   ["It means digoxin toxicity", "Digoxin toxicity gives yellow-green halos; the brightness is a known effect of ivabradine on retinal photoreceptors."],
   ["It requires stopping all heart failure drugs", "No such step is needed; the visual effect can resolve on its own."]], 80),

Q("Ivabradine", IO_CONTRA, "contraindication",
  "Which finding makes ivabradine inappropriate?",
  [["Heart block", "Correct. Ivabradine has contraindications like those of beta blockers: hypotension, heart block and a pacemaker."],
   ["A heart rate above 70", "A heart rate above 70 in sinus rhythm is the reason to add it, not a contraindication."],
   ["Normal sinus rhythm", "Normal sinus rhythm is required for its use, not a contraindication."],
   ["Maximal beta blocker therapy", "Being maxed out on beta blockers is the setting for ivabradine, not a contraindication."]], 80),

# ---- sacubitril-valsartan ---------------------------------------------------------------
Q("Sacubitril-valsartan", IO_MOA, "mechanism",
  "Which enzyme does sacubitril inhibit?",
  [["Neprilysin", "Correct. Sacubitril inhibits neprilysin, which normally degrades vasoactive peptides."],
   ["Angiotensin-converting enzyme", "Angiotensin-converting enzyme is inhibited by drugs such as lisinopril; sacubitril inhibits neprilysin."],
   ["Phosphodiesterase 3", "Phosphodiesterase 3 is inhibited by milrinone and inamrinone; sacubitril inhibits neprilysin."],
   ["Carbonic anhydrase", "Carbonic anhydrase is inhibited by acetazolamide; sacubitril inhibits neprilysin."]], 81),

Q("Sacubitril-valsartan", IO_CLASS, "class",
  "Which drug is sacubitril formulated with?",
  [["Valsartan", "Correct. Sacubitril is combined with valsartan, an angiotensin receptor blocker, in one product."],
   ["Lisinopril", "Lisinopril is an angiotensin-converting enzyme inhibitor and must not be combined with sacubitril; valsartan is the partner."],
   ["Spironolactone", "Spironolactone is an aldosterone antagonist and is not the formulated partner; valsartan is."],
   ["Metoprolol", "Metoprolol is a beta blocker and is not the formulated partner; valsartan is."]], 81),

Q("Sacubitril-valsartan", IO_MOA, "mechanism",
  "Which peptides does neprilysin normally degrade?",
  [["Natriuretic peptide and bradykinin", "Correct. Neprilysin degrades vasoactive peptides such as natriuretic peptide and bradykinin, which build up when it is inhibited."],
   ["Aldosterone and cortisol", "Those are steroid hormones rather than peptides; the vasoactive peptides neprilysin degrades are natriuretic peptide and bradykinin."],
   ["Epinephrine and norepinephrine", "Those are catecholamines rather than peptides; the vasoactive peptides neprilysin degrades are natriuretic peptide and bradykinin."],
   ["Renin and thrombin", "Those are enzymes rather than the vasoactive peptides in question; neprilysin degrades natriuretic peptide and bradykinin."]], 81),

Q("Sacubitril-valsartan", IO_MOA, "mechanism",
  "Which effects result from neprilysin inhibition?",
  [["Vasodilation, natriuresis and diuresis", "Correct. Higher levels of natriuretic peptide and bradykinin cause vasodilation, natriuresis and diuresis."],
   ["Vasoconstriction, sodium retention and antidiuresis", "These are the opposite; inhibition causes vasodilation, natriuresis and diuresis."],
   ["Vasodilation, sodium retention and antidiuresis", "Sodium retention and antidiuresis are the opposite of the effect; natriuresis and diuresis occur."],
   ["Vasoconstriction, natriuresis and diuresis", "Vessels dilate rather than constrict when neprilysin is inhibited."]], 81),

Q("Sacubitril-valsartan", IO_MOA, "physiology",
  "What does neprilysin inhibition do to myocardial tissue?",
  [["It inhibits growth and fibrosis", "Correct. Inhibiting neprilysin inhibits growth and fibrosis of myocardial tissue."],
   ["It promotes hypertrophy and fibrosis", "The effect is the opposite; neprilysin inhibition inhibits growth and fibrosis."],
   ["It increases collagen deposition", "Collagen deposition (fibrosis) is reduced, not increased, because neprilysin inhibition inhibits fibrosis."],
   ["It has no effect on tissue structure", "It does affect tissue structure: it inhibits growth and fibrosis of myocardial tissue."]], 81),

Q("Sacubitril-valsartan", IO_IND, "indication",
  "What is sacubitril-valsartan used to reduce in heart failure?",
  [["Cardiovascular death and hospitalization", "Correct. It is used to reduce the risk of cardiovascular death and hospitalization in patients with heart failure."],
   ["Blood glucose and glycated hemoglobin", "Glucose lowering is not its use; it reduces cardiovascular death and hospitalization."],
   ["Intraocular pressure", "Pressure in the eye is not its target; it reduces cardiovascular death and hospitalization in heart failure."],
   ["Serum potassium", "It can raise potassium rather than reduce it; its benefit is lower cardiovascular death and hospitalization."]], 81),

Q("Sacubitril-valsartan", IO_INTER, "interaction",
  "Which drug must not be taken together with sacubitril-valsartan?",
  [["Lisinopril", "Correct. An angiotensin-converting enzyme inhibitor is not used with sacubitril-valsartan, and a washout period separates them."],
   ["Carvedilol", "Carvedilol is a beta blocker used alongside it; the drug to avoid is an angiotensin-converting enzyme inhibitor."],
   ["Furosemide", "Furosemide is a loop diuretic used alongside it for fluid status; the drug to avoid is an angiotensin-converting enzyme inhibitor."],
   ["Digoxin", "Digoxin is not the drug to avoid; an angiotensin-converting enzyme inhibitor must not be taken with sacubitril-valsartan."]], 81),

Q("Sacubitril-valsartan", IO_PROT, "protocol",
  "What is the shortest washout advised when switching from an angiotensin-converting enzyme inhibitor to sacubitril-valsartan?",
  [["36 hours", "Correct. A 36 hour washout between the two drug classes avoids overlapping adverse effects."],
   ["12 hours", "Twelve hours is shorter than the advised washout; 36 hours is the shortest period that avoids overlapping adverse effects."],
   ["6 hours", "Six hours is shorter than the advised washout; 36 hours is the shortest period that avoids overlapping adverse effects."],
   ["72 hours", "Seventy-two hours is longer than the minimum; the shortest advised washout is 36 hours."]], 81),

Q("Sacubitril-valsartan", IO_AE, "adverse effect",
  "Which pair of adverse effects is common with sacubitril-valsartan?",
  [["Hypotension and hyperkalemia", "Correct. Hypotension and hyperkalemia are among the most common effects, along with cough and renal insufficiency."],
   ["Hypertension and hypokalemia", "Both are reversed; hypotension and hyperkalemia are the common effects."],
   ["Gynecomastia and hirsutism", "Those androgen-receptor effects belong to spironolactone; sacubitril-valsartan causes hypotension and hyperkalemia."],
   ["Phosphenes and bradycardia", "Those belong to ivabradine; sacubitril-valsartan causes hypotension and hyperkalemia."]], 81),

# ---- sodium-glucose cotransporter 2 (SGLT2) inhibitors -------------------------------------------------------------------------
Q("sodium-glucose cotransporter 2 (SGLT2) inhibitors", IO_CLASS, "class",
  "Which two drugs are sodium-glucose cotransporter 2 (SGLT2) inhibitors?",
  [["Dapagliflozin and empagliflozin", "Correct. Dapagliflozin and empagliflozin are the sodium-glucose cotransporter 2 (SGLT2) inhibitors listed for heart failure."],
   ["Sacubitril and valsartan", "Sacubitril is a neprilysin inhibitor and valsartan an angiotensin receptor blocker; the sodium-glucose cotransporter 2 (SGLT2) inhibitors are dapagliflozin and empagliflozin."],
   ["Milrinone and inamrinone", "These are phosphodiesterase 3 inhibitors; the sodium-glucose cotransporter 2 (SGLT2) inhibitors are dapagliflozin and empagliflozin."],
   ["Spironolactone and eplerenone", "These are aldosterone antagonists; the sodium-glucose cotransporter 2 (SGLT2) inhibitors are dapagliflozin and empagliflozin."]], 82),

Q("sodium-glucose cotransporter 2 (SGLT2) inhibitors", IO_MOA, "mechanism",
  "How do sodium-glucose cotransporter 2 (SGLT2) inhibitors lower blood glucose?",
  [["The kidneys stop reabsorbing glucose", "Correct. Blocking the sodium-glucose transporter means glucose is lost in the urine instead of reabsorbed."],
   ["The pancreas releases more insulin", "They do not act on insulin release; they cause the kidneys not to reabsorb glucose."],
   ["The gut absorbs less glucose", "Intestinal absorption is not the target; the kidneys stop reabsorbing glucose."],
   ["The liver makes less glucose", "Liver production is not the target; the kidneys stop reabsorbing glucose."]], 82),

Q("sodium-glucose cotransporter 2 (SGLT2) inhibitors", IO_IND, "indication",
  "For which type of heart failure are sodium-glucose cotransporter 2 (SGLT2) inhibitors used?",
  [["Stable, chronic reduced ejection fraction", "Correct. They are used in stable, chronic heart failure with reduced ejection fraction."],
   ["Acute decompensation with shock", "They are not acute rescue drugs; they are for stable, chronic reduced ejection fraction."],
   ["Failure with severe low blood pressure", "They risk hypotension, so they are not for severe low blood pressure; they are for stable, chronic reduced ejection fraction."],
   ["Failure from advanced heart block", "Heart block is not an indication; they are for stable, chronic reduced ejection fraction."]], 82),

Q("sodium-glucose cotransporter 2 (SGLT2) inhibitors", IO_IND, "indication",
  "What do sodium-glucose cotransporter 2 (SGLT2) inhibitors reduce in chronic heart failure?",
  [["Mortality and hospitalizations", "Correct. In stable, chronic reduced ejection fraction heart failure, they reduce mortality and hospitalizations."],
   ["Heart rate and contractility", "They do not act on rate or contractility; they reduce mortality and hospitalizations."],
   ["Serum potassium and magnesium", "They are not electrolyte-lowering drugs; they reduce mortality and hospitalizations."],
   ["Preload only", "Their benefit is lower mortality and fewer hospitalizations, not just a preload change."]], 82),

Q("sodium-glucose cotransporter 2 (SGLT2) inhibitors", IO_IND, "indication",
  "For which condition were sodium-glucose cotransporter 2 (SGLT2) inhibitors originally developed?",
  [["Diabetes", "Correct. They were originally developed for diabetes, since they cause the kidneys not to reabsorb glucose."],
   ["Hypertension", "Hypertension is not their original use; they were developed for diabetes."],
   ["Hyperlipidemia", "Lipid lowering is not their original use; they were developed for diabetes."],
   ["Gout", "Gout is not their original use; they were developed for diabetes."]], 82),

Q("sodium-glucose cotransporter 2 (SGLT2) inhibitors", IO_AE, "adverse effect",
  "Which infection risk rises with sodium-glucose cotransporter 2 (SGLT2) inhibitors?",
  [["Fungal urinary tract infection", "Correct. Sugar in the urine promotes fungal growth, so fungal urinary tract infections are a unique adverse effect."],
   ["Bacterial pneumonia", "Pneumonia is not the listed risk; glucose in the urine promotes fungal infection."],
   ["Cytomegalovirus retinitis", "That is not the listed risk; glucose in the urine promotes fungal urinary tract infection."],
   ["Clostridioides difficile colitis", "That is not the listed risk; glucose in the urine promotes fungal urinary tract infection."]], 82),

Q("sodium-glucose cotransporter 2 (SGLT2) inhibitors", IO_AE, "adverse effect",
  "Why do sodium-glucose cotransporter 2 (SGLT2) inhibitors cause hypotension?",
  [["Fluid lost in urine lowers blood volume", "Correct. The kidneys excrete extra glucose with fluid, so blood volume falls and blood pressure can drop."],
   ["They block beta-1 receptors in the heart", "They do not block beta-1 receptors; the fall in pressure comes from fluid lost in the urine."],
   ["They dilate veins through nitric oxide", "They do not act through nitric oxide; the fall in pressure comes from fluid lost in the urine."],
   ["They inhibit neprilysin in vessels", "Neprilysin inhibition is sacubitril's action; sodium-glucose cotransporter 2 (SGLT2) inhibitors lower pressure by lowering blood volume."]], 82),

Q("sodium-glucose cotransporter 2 (SGLT2) inhibitors", IO_EDU, "education",
  "Which counseling point applies to a patient starting a sodium-glucose cotransporter 2 (SGLT2) inhibitor?",
  [["Report urinary or genital fungal symptoms", "Correct. Glucose in the urine encourages fungal growth, so symptoms of a urinary or genital fungal infection should be reported."],
   ["Avoid all fluids", "Fluids should not be avoided entirely; the drug already lowers blood volume, which can cause hypotension."],
   ["Add a potassium supplement", "A potassium supplement is not part of therapy; fungal infection and hypotension are the points to counsel."],
   ["Stop the drug if urine contains glucose", "Glucose in the urine is the drug's expected action; the point to report is a fungal infection."]], 82),

]
