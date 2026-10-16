# -*- coding: utf-8 -*-
"""Rapid-drill bank: antiarrhythmic drugs (Lecture 10, Antiarrhythmics.pptx, deck key AA).

One fact, four names, no doses. One drug per choice; a class name is offered only when the stem itself asks for a
class, and then every choice is a class (never a set of bare Roman numerals, which would have to be shown in order).
Every wrong choice is another real antiarrhythmic from the same deck, and never a second defensible answer: a fact
the deck gives to two drugs (verapamil and diltiazem; metoprolol and acebutolol) is keyed to one of them and the
other is never offered beside it.

Slides only (the deck has no speaker notes); picture slides 7, 8, 16, 20, 25, 30 and 37 were read by eye into
tools/pharm_e3/ocr.json.

Left out on purpose (Jaxon's standing rules and the keying decisions of the Lecture 10 build):
  * every dose (the magnesium sulfate amount on slide 45) and every bare number as the thing asked;
  * channel affinity (open or inactivated) and dissociation rate: the lecturer said he will not test them;
  * lidocaine and adenosine for Wolff-Parkinson-White (slides 17 and 42; current guidelines differ);
  * propranolol and blood glucose (slide 28 says hyperglycemia; the two transcripts of the recording disagree);
  * propranolol's "Heart failure, Digitalis toxicity" line (slide 28): its meaning is unclear and was not explained;
  * amiodarone "replacing lidocaine" (slide 31; current resuscitation guidance lists either drug);
  * seizures as unique to lidocaine (the flecainide slide also lists seizures);
  * "Anticoagulants and Digitalis" under quinidine conversion (slide 10 does not say what they are for);
  * digoxin "inhibits calcium channels in the atrioventricular node" (slide 43) as a key;
  * amiodarone "maintain normal rate in atrial fibrillation" (slide 31) as a rate-or-rhythm key;
  * propranolol's ventricular ectopic beats and myocardial infarction indications as a drill (a real-world reader could
    defend another beta blocker there), and metoprolol/acebutolol sedation (shared by both on one slide);
  * the chemical structures (twelve pictures).
"""
ITEMS = [
# ---- class-level stems (every choice a class) ----
dict(q="Which antiarrhythmic class shortens phase 3 and decreases the automaticity of ectopic foci?",
     ans="Class IB", src=("AA", 16),
     why="Class IB (lidocaine) shortens phase 3, giving a shorter action potential, and decreases ectopic foci automaticity, acting mainly in ischemic tissue.",
     wrong=[("Class IA", "Class IA (quinidine, procainamide, disopyramide) slows phase 0 and prolongs the action potential rather than shortening phase 3."),
            ("Class IC", "Class IC (flecainide, propafenone) markedly slows phase 0 and prolongs the refractory period; it does not shorten phase 3."),
            ("Class III", "Class III prolongs phase 3 repolarization by reducing potassium efflux, the opposite of the class IB effect.")]),

dict(q="Which antiarrhythmic class affects the normal heart, slowing phase 0 and conduction?",
     ans="Class IC", src=("AA", 20),
     why="Class IC slows phase 0, slows conduction, prolongs the refractory period and affects the normal heart, unlike class IB.",
     wrong=[("Class IB", "Class IB has little effect in normal tissue; it works mainly in ischemic tissue and shortens phase 3 instead of slowing phase 0."),
            ("Class II", "Class II beta blockers decrease phase 4 depolarization and prolong atrioventricular conduction; slowing phase 0 is a sodium channel effect."),
            ("Class IV", "Class IV calcium channel blockers block the L-type channel and slow atrioventricular node conduction; they do not slow phase 0.")]),

dict(q="Which antiarrhythmic class decreases phase 4 depolarization by blocking beta receptors?",
     ans="Class II", src=("AA", 25),
     why="Class II drugs are beta receptor antagonists: they slow conduction, decrease automaticity, prolong atrioventricular conduction and decrease phase 4 depolarization.",
     wrong=[("Class IB", "Class IB blocks sodium channels in ischemic tissue and shortens phase 3; it does not act through beta receptors."),
            ("Class IA", "Class IA slows phase 0 and prolongs the action potential through sodium channel blockade; beta receptor blockade defines class II."),
            ("Class IV", "Class IV decreases automaticity by blocking L-type calcium channels, not beta receptors, and slows atrioventricular node conduction.")]),

dict(q="Which antiarrhythmic class prolongs phase 3 repolarization by reducing potassium efflux?",
     ans="Class III", src=("AA", 30),
     why="Class III drugs reduce potassium efflux, prolonging phase 3 repolarization, the refractory period and the duration of the action potential.",
     wrong=[("Class II", "Class II beta blockers decrease phase 4 depolarization and prolong atrioventricular conduction; they do not reduce potassium efflux."),
            ("Class IB", "Class IB shortens phase 3 rather than prolonging it, and it blocks sodium channels, not potassium efflux."),
            ("Class IV", "Class IV blocks L-type calcium channels and slows atrioventricular node conduction; it does not reduce potassium efflux.")]),

dict(q="Which antiarrhythmic class blocks L-type calcium channels and slows atrioventricular node conduction?",
     ans="Class IV", src=("AA", 37),
     why="Class IV calcium channel blockers (verapamil, diltiazem) block the L-type channel, decrease automaticity, slow atrioventricular node conduction and are negative inotropes.",
     wrong=[("Class IA", "Class IA drugs are sodium channel blockers that slow phase 0 and prolong the action potential, not L-type calcium channel blockers."),
            ("Class IC", "Class IC drugs are sodium channel blockers that markedly slow phase 0 in normal heart tissue; they do not block L-type calcium channels."),
            ("Class IB", "Class IB drugs block sodium channels mainly in ischemic tissue and shorten phase 3; the L-type calcium channel is the class IV target.")]),

# ---- class IA: quinidine ----
dict(q="Which antiarrhythmic causes cinchonism: tinnitus, dizziness and blurred vision?",
     ans="Quinidine", src=("AA", 11),
     why="Cinchonism (tinnitus, dizziness, blurred vision) is on quinidine's toxicity list; quinidine is the D-isomer of quinine.",
     wrong=[("Procainamide", "Procainamide's signature effect is a lupus-like syndrome, more often in slow acetylators, not cinchonism."),
            ("Disopyramide", "Disopyramide's toxicity is antimuscarinic effects, heart failure and torsades de pointes; cinchonism belongs to quinidine."),
            ("Lidocaine", "Lidocaine toxicity is central nervous system toxicity with nystagmus as its early sign; cinchonism belongs to quinidine.")]),

dict(q="Which antiarrhythmic is the D-isomer of quinine?",
     ans="Quinidine", src=("AA", 9),
     why="Quinidine is the D-isomer of quinine (brands Quinalan, Cardioquin, Quinidex), which is why it can cause cinchonism.",
     wrong=[("Procainamide", "Procainamide is an amide derivative of procaine, the local anesthetic, not an isomer of quinine."),
            ("Disopyramide", "Disopyramide (Norpace) has effects similar to quinidine but is not an isomer of quinine; quinidine is."),
            ("Flecainide", "Flecainide (Tambocor) is a class IC sodium and potassium channel blocker, not an isomer of quinine.")]),

dict(q="Which antiarrhythmic inhibits cytochrome P450 2D6 (CYP2D6), affecting codeine and morphine?",
     ans="Quinidine", src=("AA", 10),
     why="Quinidine's listed clinical interaction is inhibition of cytochrome P450 2D6 (CYP2D6), with codeine and morphine as the named examples.",
     wrong=[("Procainamide", "Procainamide's listed metabolic point is acetylation to an active metabolite with class III activity, not CYP2D6 inhibition."),
            ("Disopyramide", "Disopyramide's listed problems are anticholinergic effects and negative inotropy; CYP2D6 inhibition is listed for quinidine."),
            ("Lidocaine", "Lidocaine's listed metabolic point is extensive first-pass metabolism, which is why it is given intravenously.")]),

dict(q="Which antiarrhythmic causes nausea, vomiting and diarrhea in 30 to 50 percent of patients?",
     ans="Quinidine", src=("AA", 11),
     why="Nausea, vomiting and diarrhea occur in 30 to 50 percent of patients on quinidine, its most frequent toxicity.",
     wrong=[("Lidocaine", "Lidocaine's toxicity is central: drowsiness, confusion, restlessness, muscle twitches, seizures and nystagmus."),
            ("Flecainide", "Flecainide's listed toxicity is blurred vision, tremor, resistant ventricular tachycardia, bronchospasm, seizures and thrombocytopenia."),
            ("Disopyramide", "Disopyramide's listed toxicity is hypotension, antimuscarinic effects, conduction disturbances, heart failure and torsades de pointes.")]),

dict(q="Which antiarrhythmic acts as an alpha blocker at higher doses?",
     ans="Quinidine", src=("AA", 9),
     why="Quinidine's indirect actions are anticholinergic effects and alpha blockade at higher doses, which contributes to hypotension.",
     wrong=[("Procainamide", "Procainamide has no alpha-blocking activity and less anticholinergic activity than quinidine."),
            ("Flecainide", "Flecainide blocks sodium and potassium channels in the ventricles; alpha blockade is listed for quinidine."),
            ("Lidocaine", "Lidocaine blocks sodium channels mainly in ischemic tissue; alpha blockade at higher doses is quinidine's indirect action.")]),

dict(q="Which antiarrhythmic can cause thrombocytopenia that may be fatal?",
     ans="Quinidine", src=("AA", 11),
     why="Quinidine's toxicity list includes thrombocytopenia, marked as potentially fatal, alongside immunological reactions.",
     wrong=[("Lidocaine", "Lidocaine's listed toxicity is central nervous system toxicity, hypersensitivity and increased atrioventricular conduction, not thrombocytopenia."),
            ("Disopyramide", "Disopyramide's toxicity list has no blood disorder; it lists hypotension, antimuscarinic effects, heart failure and torsades."),
            ("Dofetilide", "Dofetilide's adverse effects are torsades de pointes and marked QT prolongation, not a fall in platelets.")]),

# ---- class IA: procainamide ----
dict(q="Which antiarrhythmic causes a lupus-like syndrome, more often in slow acetylators?",
     ans="Procainamide", src=("AA", 13),
     why="A lupus-like syndrome occurs in 25 to 50 percent of patients on procainamide, more often in slow acetylators.",
     wrong=[("Quinidine", "Quinidine's named effects are cinchonism and quinidine sudden death; the lupus-like syndrome belongs to procainamide."),
            ("Disopyramide", "Disopyramide's notable effects are antimuscarinic actions and heart failure, not a lupus-like syndrome."),
            ("Flecainide", "Flecainide's notable risk is increased mortality after myocardial infarction, not a lupus-like syndrome.")]),

dict(q="Which antiarrhythmic forms an active acetylated metabolite with class III activity?",
     ans="Procainamide", src=("AA", 12),
     why="Procainamide has an active acetylated metabolite (N-acetylprocainamide, NAPA) with class III activity; fast acetylators may increase it.",
     wrong=[("Quinidine", "Quinidine is the D-isomer of quinine and inhibits cytochrome P450 2D6; no acetylated class III metabolite is listed for it."),
            ("Disopyramide", "Disopyramide is a class IA drug with stronger anticholinergic action; it has no listed acetylated metabolite."),
            ("Lidocaine", "Lidocaine undergoes extensive first-pass metabolism, which is why it is given intravenously; it forms no listed class III metabolite.")]),

dict(q="Which antiarrhythmic has a short 3 to 4 hour duration of action, so a slow-release preparation is used?",
     ans="Procainamide", src=("AA", 12),
     why="Procainamide has a short duration of action of 3 to 4 hours, so it comes as a slow-release preparation.",
     wrong=[("Flecainide", "Flecainide has a long half-life of 14 hours, given orally or intravenously, so it is not the short-acting drug."),
            ("Amiodarone", "Amiodarone has a half-life of about 40 days, with slow onset and slow elimination, the opposite of a short duration."),
            ("Adenosine", "Adenosine's half-life is about 10 seconds; it is given for paroxysmal supraventricular tachycardia, not as a slow-release product.")]),

dict(q="Which antiarrhythmic is an amide derivative of procaine?",
     ans="Procainamide", src=("AA", 12),
     why="Procainamide (Procan, Pronestyl) is an amide derivative of procaine, with less anticholinergic activity than quinidine.",
     wrong=[("Quinidine", "Quinidine is the D-isomer of quinine, not a derivative of procaine."),
            ("Disopyramide", "Disopyramide (Norpace) is a class IA drug with effects similar to quinidine, not a derivative of procaine."),
            ("Flecainide", "Flecainide (Tambocor) is a class IC drug that blocks sodium and potassium channels, not a derivative of procaine.")]),

dict(q="Which antiarrhythmic can cause bone marrow suppression in 0.2 percent of patients?",
     ans="Procainamide", src=("AA", 13),
     why="Procainamide's adverse effects include bone marrow suppression (0.2 percent), with the lupus-like syndrome and torsades de pointes.",
     wrong=[("Quinidine", "Quinidine's listed blood effect is thrombocytopenia, which may be fatal, not bone marrow suppression."),
            ("Lidocaine", "Lidocaine's listed toxicity is in the central nervous system, with nystagmus as the early sign, not the bone marrow."),
            ("Amiodarone", "Amiodarone's listed toxicities are lung, thyroid, skin, eye, liver and nerve problems, not bone marrow suppression.")]),

# ---- class IA: disopyramide ----
dict(q="Which antiarrhythmic has effects similar to quinidine but more anticholinergic action?",
     ans="Disopyramide", src=("AA", 14),
     why="Disopyramide's effects are similar to quinidine, with more anticholinergic actions and a negative inotropic effect.",
     wrong=[("Procainamide", "Procainamide has less anticholinergic activity than quinidine and no alpha-blocking activity, the reverse."),
            ("Lidocaine", "Lidocaine is the class IB drug acting mainly on ischemic tissue; it is not described as anticholinergic."),
            ("Propafenone", "Propafenone shares flecainide's mechanism and adds beta-blocking activity, not anticholinergic action.")]),

dict(q="Which antiarrhythmic is contraindicated in glaucoma?",
     ans="Disopyramide", src=("AA", 15),
     why="Disopyramide is contraindicated in heart block, hypersensitivity and glaucoma; its strong anticholinergic action explains the glaucoma.",
     wrong=[("Procainamide", "Procainamide's listed problems are a lupus-like syndrome, bone marrow suppression and torsades de pointes, not glaucoma."),
            ("Lidocaine", "Lidocaine's listed contraindications are seizures and age, not heart block and glaucoma."),
            ("Amiodarone", "Amiodarone causes corneal deposits and thyroid abnormalities; glaucoma is listed as a contraindication only for disopyramide.")]),

dict(q="Which antiarrhythmic can cause congestive heart failure by decreasing contractility?",
     ans="Disopyramide", src=("AA", 15),
     why="Disopyramide has negative inotropic effects, and its toxicity list includes congestive heart failure from decreased contractility.",
     wrong=[("Quinidine", "Quinidine's listed toxicities are gastrointestinal upset, arrhythmias, hypotension, thrombocytopenia and cinchonism, not heart failure."),
            ("Procainamide", "Procainamide's listed adverse effects are hypotension, slowed conduction, nausea, lupus-like syndrome and torsades, not heart failure."),
            ("Lidocaine", "Lidocaine's listed toxicity is central nervous system toxicity and hypersensitivity, not congestive heart failure.")]),

# ---- class IB: lidocaine ----
dict(q="Which antiarrhythmic has nystagmus as an early sign of toxicity?",
     ans="Lidocaine", src=("AA", 19),
     why="Lidocaine's central nervous system toxicity includes drowsiness, confusion, restlessness, muscle twitches and seizures, with nystagmus as an early sign.",
     wrong=[("Quinidine", "Quinidine's nervous system effect is cinchonism (tinnitus, dizziness, blurred vision), not nystagmus."),
            ("Flecainide", "Flecainide's listed nervous system effects are blurred vision and tremor, not nystagmus."),
            ("Amiodarone", "Amiodarone's listed nervous system effects are neurotoxicity, neuropathy, muscle weakness and ataxia, not nystagmus.")]),

dict(q="Which antiarrhythmic is given intravenously because of extensive first-pass metabolism?",
     ans="Lidocaine", src=("AA", 18),
     why="Lidocaine is given intravenously because of extensive first-pass metabolism, so it is not taken by mouth.",
     wrong=[("Flecainide", "Flecainide is given orally or intravenously and has a long half-life of 14 hours; first-pass metabolism is lidocaine's problem."),
            ("Amiodarone", "Amiodarone is given orally and intravenously; its notable kinetics are a half-life of about 40 days, not first-pass loss."),
            ("Procainamide", "Procainamide comes as a slow-release preparation because its action lasts only 3 to 4 hours, not because of first-pass metabolism.")]),

dict(q="Which antiarrhythmic works best on sodium channels in ischemic tissue, with less effect on normal tissue?",
     ans="Lidocaine", src=("AA", 18),
     why="Lidocaine is most effective on sodium channels in ischemic tissue and has less effect on normal tissue; acute myocardial infarction is among its indications.",
     wrong=[("Flecainide", "Flecainide is class IC, which affects the normal heart; working mainly in ischemic tissue is the class IB (lidocaine) property."),
            ("Quinidine", "Quinidine is class IA, slowing phase 0 and prolonging the action potential; the ischemic-tissue preference belongs to lidocaine."),
            ("Procainamide", "Procainamide is class IA with an active class III metabolite; the ischemic-tissue preference belongs to lidocaine.")]),

dict(q="Which sodium channel blocker is not effective against atrial arrhythmias?",
     ans="Lidocaine", src=("AA", 18),
     why="Lidocaine is not effective against atrial arrhythmias; its indications are ventricular tachycardia, premature beats, ventricular fibrillation and acute myocardial infarction.",
     wrong=[("Quinidine", "Quinidine is used to maintain rhythm with atrial flutter or fibrillation, so it does act on atrial arrhythmias."),
            ("Flecainide", "Flecainide's indications include supraventricular arrhythmias as well as life-threatening ventricular arrhythmias."),
            ("Disopyramide", "Disopyramide's indications include supraventricular arrhythmias (flutter, fibrillation) as well as ventricular tachycardia.")]),

dict(q="Which antiarrhythmic has seizures and age as contraindications?",
     ans="Lidocaine", src=("AA", 19),
     why="Lidocaine's listed contraindications are seizures and age; its central nervous system toxicity itself can progress to seizures.",
     wrong=[("Quinidine", "Quinidine's listed problems are gastrointestinal upset, arrhythmias, thrombocytopenia and cinchonism, with no seizure or age contraindication."),
            ("Disopyramide", "Disopyramide's listed contraindications are heart block, hypersensitivity and glaucoma, not seizures and age."),
            ("Amiodarone", "Amiodarone's listed problems are pulmonary, thyroid, skin, eye, liver and nerve toxicity, not a seizure or age contraindication.")]),

# ---- class IC: flecainide, propafenone ----
dict(q="Which antiarrhythmic increases mortality in myocardial infarction?",
     ans="Flecainide", src=("AA", 23),
     why="Flecainide's toxicity list includes increased mortality in myocardial infarction, and it is used only without significant structural heart damage.",
     wrong=[("Lidocaine", "Lidocaine is listed for use in acute myocardial infarction, where it acts on sodium channels in ischemic tissue."),
            ("Propranolol", "Propranolol is listed as an indication for myocardial infarction, not as a drug that increases its mortality."),
            ("Amiodarone", "Amiodarone is listed for recurrent ventricular tachycardia or fibrillation resistant to other drugs; the mortality increase in myocardial infarction is flecainide's.")]),

dict(q="Which antiarrhythmic should be used only in patients without significant structural damage to the heart?",
     ans="Flecainide", src=("AA", 22),
     why="Flecainide is used only in patients without significant structural damage to the heart, because it increases mortality in myocardial infarction.",
     wrong=[("Lidocaine", "Lidocaine works best in ischemic tissue and is listed for acute myocardial infarction, so damaged hearts are its setting."),
            ("Amiodarone", "Amiodarone is listed for recurrent ventricular tachycardia or fibrillation resistant to other drugs, with no structural-damage restriction."),
            ("Dofetilide", "Dofetilide's restriction is limited availability to those with special training, not structural heart damage.")]),

dict(q="Which antiarrhythmic prolongs the PR, QRS and QT intervals?",
     ans="Flecainide", src=("AA", 21),
     why="Flecainide blocks sodium and potassium channels in the ventricles and prolongs the PR, QRS and QT intervals.",
     wrong=[("Lidocaine", "Lidocaine (class IB) shortens phase 3 and has little effect on normal tissue, so it does not prolong these intervals."),
            ("Magnesium sulfate", "Magnesium sulfate treats torsades de pointes; its listed effects are bradycardia, flushing, headache and respiratory paralysis."),
            ("Adenosine", "Adenosine hyperpolarizes cells and may stop the heart for 2 to 3 seconds; its half-life is about 10 seconds.")]),

dict(q="Which antiarrhythmic can cause tremor?",
     ans="Flecainide", src=("AA", 23),
     why="Flecainide's toxicity list begins with blurred vision and tremor, then resistant ventricular tachycardia, bronchospasm, seizures and thrombocytopenia.",
     wrong=[("Disopyramide", "Disopyramide's toxicity is hypotension, antimuscarinic effects, conduction disturbances, heart failure and torsades; tremor is flecainide's."),
            ("Metoprolol", "Metoprolol's listed central effects are sedation and fatigue, not tremor."),
            ("Dofetilide", "Dofetilide's adverse effects are torsades de pointes and marked QT prolongation, not tremor.")]),

dict(q="Which antiarrhythmic blocks sodium and potassium channels in the ventricles and slows recovery of the sodium channel?",
     ans="Flecainide", src=("AA", 21),
     why="Flecainide blocks sodium and potassium channels in the ventricles and slows recovery of the sodium channel, prolonging the PR, QRS and QT intervals.",
     wrong=[("Lidocaine", "Lidocaine blocks sodium channels mainly in ischemic tissue and has less effect on normal tissue; it does not block potassium channels."),
            ("Dofetilide", "Dofetilide is a potent pure potassium channel blocker, with no sodium channel action."),
            ("Diltiazem", "Diltiazem blocks the L-type calcium channel and slows atrioventricular node conduction.")]),

dict(q="Which antiarrhythmic has the same mechanism as flecainide plus beta-blocking activity?",
     ans="Propafenone", src=("AA", 24),
     why="Propafenone has the same mechanism as flecainide plus beta-blocking activity, which brings bradycardia, bronchospasm and worse heart failure.",
     wrong=[("Sotalol", "Sotalol combines beta-blocking activity with potassium channel inhibition, not flecainide's sodium channel mechanism."),
            ("Disopyramide", "Disopyramide is class IA with effects similar to quinidine and more anticholinergic action, not beta blockade."),
            ("Lidocaine", "Lidocaine is class IB, acting mainly on ischemic tissue; it has no beta-blocking activity.")]),

dict(q="Which antiarrhythmic can cause agranulocytosis?",
     ans="Propafenone", src=("AA", 24),
     why="Propafenone's toxicity list includes agranulocytosis, anemia and thrombocytopenia, along with proarrhythmia and bronchospasm.",
     wrong=[("Sotalol", "Sotalol's listed toxicity is torsades de pointes and bronchospasm from its beta-blocking activity, not a blood disorder."),
            ("Lidocaine", "Lidocaine's listed toxicity is central nervous system toxicity and hypersensitivity, not a blood disorder."),
            ("Amiodarone", "Amiodarone's listed toxicities are pulmonary, thyroid, skin, corneal, hepatic and nerve effects, not agranulocytosis.")]),

# ---- class II: beta blockers ----
dict(q="Which beta blocker is nonselective and membrane stabilizing?",
     ans="Propranolol", src=("AA", 26),
     why="Propranolol is a nonselective beta blocker that reduces phase 4 activation, slows atrioventricular conduction and is membrane stabilizing.",
     wrong=[("Metoprolol", "Metoprolol is a beta-1 selective blocker with less bronchospasm, not a nonselective one."),
            ("Acebutolol", "Acebutolol is a beta-1 selective blocker, listed with metoprolol, not a nonselective one."),
            ("Esmolol", "Esmolol is the intravenous, short-acting beta blocker; nonselective, membrane-stabilizing action is listed for propranolol.")]),

dict(q="Which beta blocker is given intravenously and is short acting?",
     ans="Esmolol", src=("AA", 29),
     why="Esmolol is the intravenous, short-acting beta blocker listed beside the beta-1 selective agents metoprolol and acebutolol.",
     wrong=[("Propranolol", "Propranolol is the nonselective, membrane-stabilizing beta blocker; the intravenous short-acting agent is esmolol."),
            ("Acebutolol", "Acebutolol is a beta-1 selective blocker with less bronchospasm; the intravenous short-acting agent is esmolol."),
            ("Sotalol", "Sotalol is a beta blocker that also inhibits potassium channels and causes torsades de pointes; it is not the short-acting one.")]),

dict(q="Which beta blocker is beta-1 selective, with less bronchospasm than propranolol?",
     ans="Metoprolol", src=("AA", 29),
     why="Metoprolol is a beta-1 selective blocker similar to propranolol but with less bronchospasm; it can still cause heart failure.",
     wrong=[("Propranolol", "Propranolol is nonselective, and bronchospasm is on its toxicity list, so it is the comparison, not the answer."),
            ("Sotalol", "Sotalol's beta-blocking activity brings bronchospasm, and it also inhibits potassium channels and causes torsades de pointes."),
            ("Propafenone", "Propafenone's beta-adrenergic blockade causes bronchospasm; it is a class IC drug, not a beta-1 selective blocker.")]),

# ---- class III ----
dict(q="Which antiarrhythmic is an analog of thyroid hormone?",
     ans="Amiodarone", src=("AA", 31),
     why="Amiodarone is an analog of thyroid hormone, given orally and intravenously, which explains its thyroid abnormalities (hyper or hypo).",
     wrong=[("Dofetilide", "Dofetilide is a potent pure potassium channel blocker, not a thyroid hormone analog."),
            ("Sotalol", "Sotalol is a beta blocker that also inhibits potassium channels, not a thyroid hormone analog."),
            ("Digoxin", "Digoxin inhibits the sodium-potassium ATPase and increases parasympathetic tone; it is not a thyroid hormone analog.")]),

dict(q="Which antiarrhythmic has a half-life of about 40 days, so loading doses may be needed?",
     ans="Amiodarone", src=("AA", 31),
     why="Amiodarone's half-life is about 40 days (26 to 107), with slow onset and slow elimination, so it may require loading doses.",
     wrong=[("Flecainide", "Flecainide's long half-life is 14 hours, far shorter than amiodarone's, and loading doses are not listed for it."),
            ("Procainamide", "Procainamide acts for only 3 to 4 hours, so it comes as a slow-release preparation rather than needing loading doses."),
            ("Adenosine", "Adenosine's half-life is about 10 seconds, with effects that pass in moments, the opposite of amiodarone.")]),

dict(q="Which antiarrhythmic causes a blue-gray skin color and photosensitivity?",
     ans="Amiodarone", src=("AA", 33),
     why="Amiodarone's toxicity list includes blue-gray skin color with photosensitivity, plus corneal deposits and thyroid abnormalities.",
     wrong=[("Quinidine", "Quinidine's listed effects are gastrointestinal upset, cinchonism and thrombocytopenia, not skin color change."),
            ("Procainamide", "Procainamide's notable effect is a lupus-like syndrome, not blue-gray skin or photosensitivity."),
            ("Dofetilide", "Dofetilide's adverse effects are torsades de pointes and marked QT prolongation, not skin changes.")]),

dict(q="Which antiarrhythmic causes corneal deposits?",
     ans="Amiodarone", src=("AA", 33),
     why="Corneal deposits are on amiodarone's toxicity list, with blue-gray skin, photosensitivity and thyroid abnormalities.",
     wrong=[("Quinidine", "Quinidine affects vision through cinchonism (blurred vision with tinnitus and dizziness), not corneal deposits."),
            ("Disopyramide", "Disopyramide's eye issue is that glaucoma is a contraindication, because of its anticholinergic action."),
            ("Lidocaine", "Lidocaine's eye sign is nystagmus, the early sign of its toxicity, not corneal deposits.")]),

dict(q="Which antiarrhythmic can cause potentially fatal pneumonitis and pulmonary fibrosis?",
     ans="Amiodarone", src=("AA", 33),
     why="Amiodarone's toxicity list includes pneumonitis and pulmonary fibrosis, marked as potentially fatal, alongside hepatic dysfunction.",
     wrong=[("Sotalol", "Sotalol's lung effect is bronchospasm from its beta-blocking activity, not pneumonitis or fibrosis."),
            ("Propranolol", "Propranolol's lung effect is bronchospasm, because it is nonselective, not pulmonary fibrosis."),
            ("Dofetilide", "Dofetilide's adverse effects are torsades de pointes and marked QT prolongation, not lung toxicity.")]),

dict(q="Which antiarrhythmic increases digoxin, warfarin, flecainide, phenytoin and procainamide?",
     ans="Amiodarone", src=("AA", 33),
     why="Amiodarone's listed interactions are increases in digoxin, warfarin, flecainide, phenytoin and procainamide.",
     wrong=[("Dofetilide", "Dofetilide's listed points are special-training prescribing and elimination unchanged by the kidneys, not these interactions."),
            ("Sotalol", "Sotalol's listed problems are torsades de pointes and bronchospasm; no interaction list is given for it."),
            ("Lidocaine", "Lidocaine's listed points are intravenous use, ischemic-tissue action and central nervous system toxicity, not these interactions.")]),

dict(q="Which antiarrhythmic blocks potassium, sodium and calcium channels plus alpha and beta receptors?",
     ans="Amiodarone", src=("AA", 32),
     why="Amiodarone blocks potassium, sodium and calcium channels and alpha and beta receptors, decreasing automaticity and conduction and prolonging refractory periods.",
     wrong=[("Sotalol", "Sotalol combines beta-blocking activity with potassium channel inhibition only; it does not block sodium or calcium channels."),
            ("Dofetilide", "Dofetilide is a pure potassium channel blocker, the opposite of amiodarone's broad action."),
            ("Propafenone", "Propafenone blocks sodium channels like flecainide and adds beta-blocking activity, not this full list.")]),

dict(q="Which drug, given intravenously, terminates acute ventricular tachycardia or fibrillation?",
     ans="Amiodarone", src=("AA", 31),
     why="Intravenous amiodarone terminates acute ventricular tachycardia or fibrillation; it is also listed for recurrent ventricular arrhythmias resistant to other drugs.",
     wrong=[("Flecainide", "Flecainide increases mortality in myocardial infarction and is used only without significant structural heart damage."),
            ("Verapamil", "Verapamil is to be avoided in ventricular arrhythmias; it is listed for paroxysmal supraventricular tachycardia and atrial fibrillation."),
            ("Adenosine", "Adenosine is listed for paroxysmal supraventricular tachycardia, not for ventricular tachycardia or fibrillation.")]),

dict(q="Which antiarrhythmic is a potent, pure potassium channel blocker?",
     ans="Dofetilide", src=("AA", 34),
     why="Dofetilide (Tikosyn) is a potent pure potassium channel blocker, used for normal rhythm in atrial fibrillation.",
     wrong=[("Amiodarone", "Amiodarone blocks potassium channels but also sodium and calcium channels and alpha and beta receptors, so it is not pure."),
            ("Sotalol", "Sotalol inhibits potassium channels but also has beta-blocking activity, so it is not a pure potassium channel blocker."),
            ("Flecainide", "Flecainide blocks sodium as well as potassium channels in the ventricles; it is class IC, not a pure potassium channel blocker.")]),

dict(q="Which antiarrhythmic has limited availability, restricted to those with special training?",
     ans="Dofetilide", src=("AA", 34),
     why="Dofetilide has limited availability to those with special training; its adverse effects are torsades de pointes and marked QT prolongation.",
     wrong=[("Amiodarone", "Amiodarone's listed practical point is that its 40-day half-life may require loading doses, not restricted prescribing."),
            ("Sotalol", "Sotalol's listed points are its beta-blocking and potassium channel actions and its torsades and bronchospasm, not restricted prescribing."),
            ("Flecainide", "Flecainide's restriction is use only in patients without significant structural heart damage, not prescriber training.")]),

dict(q="Which antiarrhythmic is mainly eliminated unchanged by the kidneys?",
     ans="Dofetilide", src=("AA", 34),
     why="Dofetilide is mainly eliminated unchanged in the kidneys, so kidney function matters when it is used.",
     wrong=[("Amiodarone", "Amiodarone's listed elimination is slow (half-life about 40 days); it is not described as eliminated unchanged by the kidneys."),
            ("Lidocaine", "Lidocaine undergoes extensive first-pass metabolism, which is why it is given intravenously."),
            ("Verapamil", "Verapamil undergoes hepatic metabolism, which is why it calls for caution in liver damage.")]),

dict(q="Which antiarrhythmic causes marked QT prolongation, with torsades de pointes in 1 to 3 percent?",
     ans="Dofetilide", src=("AA", 34),
     why="Dofetilide's adverse effects are torsades de pointes (1 to 3 percent) and marked QT prolongation, from pure potassium channel block.",
     wrong=[("Lidocaine", "Lidocaine shortens phase 3 and causes central nervous system toxicity, not marked QT prolongation."),
            ("Esmolol", "Esmolol is the intravenous, short-acting beta blocker; marked QT prolongation is listed for dofetilide, not for esmolol."),
            ("Diltiazem", "Diltiazem's listed adverse effects are hypotension and edema, not marked QT prolongation.")]),

dict(q="Which beta blocker also inhibits potassium channels?",
     ans="Sotalol", src=("AA", 35),
     why="Sotalol (Betapace) has beta-blocking activity and inhibits potassium channels, so it carries both class II and class III action.",
     wrong=[("Propranolol", "Propranolol is a nonselective, membrane-stabilizing beta blocker; potassium channel inhibition belongs to sotalol."),
            ("Metoprolol", "Metoprolol is a beta-1 selective blocker with less bronchospasm; it does not inhibit potassium channels."),
            ("Esmolol", "Esmolol is the intravenous, short-acting beta blocker; potassium channel inhibition belongs to sotalol.")]),

dict(q="Which antiarrhythmic causes both torsades de pointes and bronchospasm?",
     ans="Sotalol", src=("AA", 36),
     why="Sotalol's toxicity is torsades de pointes from potassium channel block plus bronchospasm from its beta-blocking activity.",
     wrong=[("Dofetilide", "Dofetilide causes torsades de pointes and marked QT prolongation, but it is a pure potassium channel blocker without bronchospasm."),
            ("Propranolol", "Propranolol causes bronchospasm, but torsades de pointes is not on its toxicity list."),
            ("Procainamide", "Procainamide causes torsades de pointes, but its list has no bronchospasm; it has a lupus-like syndrome instead.")]),

# ---- class IV ----
dict(q="Which antiarrhythmic undergoes hepatic metabolism, so it calls for caution in liver damage?",
     ans="Verapamil", src=("AA", 39),
     why="Verapamil undergoes hepatic metabolism, so caution is needed in liver damage; hypotension and edema are its adverse effects.",
     wrong=[("Dofetilide", "Dofetilide is mainly eliminated unchanged by the kidneys, so kidney function, not the liver, is its concern."),
            ("Adenosine", "Adenosine's listed kinetics are a half-life of about 10 seconds; no liver caution is listed for it."),
            ("Magnesium sulfate", "Magnesium sulfate's listed problems are bradycardia, flushing, headache and respiratory paralysis, not liver damage.")]),

dict(q="Which antiarrhythmic should be avoided in ventricular arrhythmias, sick sinus syndrome and depressed cardiac function?",
     ans="Diltiazem", src=("AA", 39),
     why="Diltiazem, like verapamil, is to be avoided in ventricular arrhythmias, sick sinus syndrome and depressed cardiac function.",
     wrong=[("Amiodarone", "Amiodarone is used for recurrent ventricular tachycardia or fibrillation, so ventricular arrhythmias are its indication."),
            ("Lidocaine", "Lidocaine is used for ventricular tachycardia, premature beats and ventricular fibrillation, the reverse of an avoid list."),
            ("Procainamide", "Procainamide is a class IA drug, a class listed for ventricular tachycardia and prevention of ventricular fibrillation.")]),

dict(q="Which antiarrhythmic is a calcium channel blocker that suppresses the sinoatrial node?",
     ans="Verapamil", src=("AA", 38),
     why="Verapamil is a calcium channel blocker that is most effective in the most active tissue, decreases atrioventricular conduction and suppresses the sinoatrial node.",
     wrong=[("Propranolol", "Propranolol slows the node by blocking beta receptors, a nonselective beta blocker, not by blocking calcium channels."),
            ("Lidocaine", "Lidocaine blocks sodium channels mainly in ischemic ventricular tissue and is not effective against atrial arrhythmias."),
            ("Dofetilide", "Dofetilide is a pure potassium channel blocker used for normal rhythm in atrial fibrillation, not a calcium channel blocker.")]),

# ---- miscellaneous ----
dict(q="Which antiarrhythmic may stop the heart for 2 to 3 seconds?",
     ans="Adenosine", src=("AA", 41),
     why="Adenosine hyperpolarizes cells and decreases conduction velocity, and it may stop the heart for 2 to 3 seconds.",
     wrong=[("Digoxin", "Digoxin slows atrioventricular conduction and can induce heart block, but a brief stop of the heart is listed for adenosine."),
            ("Magnesium sulfate", "Magnesium sulfate treats torsades de pointes; its listed effects are bradycardia, flushing, headache and respiratory paralysis."),
            ("Esmolol", "Esmolol is the intravenous, short-acting beta blocker; stopping the heart for seconds is the adenosine effect.")]),

dict(q="Which antiarrhythmic has a half-life of about 10 seconds?",
     ans="Adenosine", src=("AA", 41),
     why="Adenosine's half-life is about 10 seconds, so its effects (and its flushing and chest burning) pass quickly.",
     wrong=[("Lidocaine", "Lidocaine's listed kinetics are extensive first-pass metabolism and intravenous use, not a 10-second half-life."),
            ("Flecainide", "Flecainide has a long half-life of 14 hours, suited to oral use."),
            ("Digoxin", "Digoxin's listed points are sodium-potassium ATPase inhibition and slowed atrioventricular conduction; a 10-second half-life is adenosine's.")]),

dict(q="Which antiarrhythmic causes flushing in about 20 percent, with shortness of breath and burning in the chest?",
     ans="Adenosine", src=("AA", 42),
     why="Adenosine's listed toxicity is flushing (20 percent), shortness of breath and burning in the chest.",
     wrong=[("Digoxin", "Digoxin's listed toxicity is nausea, vomiting, diarrhea, anorexia and central effects such as confusion and visual disturbances."),
            ("Lidocaine", "Lidocaine's listed toxicity is central nervous system toxicity, with nystagmus as the early sign."),
            ("Procainamide", "Procainamide's listed adverse effects are hypotension, slowed conduction, nausea, a lupus-like syndrome and torsades, not flushing.")]),

dict(q="Which antiarrhythmic activates potassium channels in the atria and hyperpolarizes cells?",
     ans="Adenosine", src=("AA", 41),
     why="Adenosine activates potassium channels in the atria and blocks calcium channels, hyperpolarizing cells and decreasing conduction velocity.",
     wrong=[("Dofetilide", "Dofetilide blocks potassium channels rather than activating them, which prolongs the QT interval."),
            ("Amiodarone", "Amiodarone blocks potassium channels (and sodium and calcium channels), prolonging refractory periods; it does not activate them."),
            ("Digoxin", "Digoxin inhibits the sodium-potassium ATPase and increases parasympathetic tone; it does not activate atrial potassium channels.")]),

dict(q="Which antiarrhythmic inhibits the sodium-potassium ATPase and indirectly increases parasympathetic tone?",
     ans="Digoxin", src=("AA", 43),
     why="Digoxin (digitalis) inhibits the sodium-potassium ATPase, slows atrioventricular conduction and indirectly increases parasympathetic tone while decreasing sympathetic tone.",
     wrong=[("Adenosine", "Adenosine activates atrial potassium channels and blocks calcium channels, hyperpolarizing cells; it does not inhibit the sodium-potassium ATPase."),
            ("Verapamil", "Verapamil blocks the L-type calcium channel and suppresses the sinoatrial node; it does not inhibit the sodium-potassium ATPase."),
            ("Propranolol", "Propranolol blocks beta receptors nonselectively; it does not inhibit the sodium-potassium ATPase.")]),

dict(q="Which antiarrhythmic is used to induce heart block in atrial flutter or fibrillation?",
     ans="Digoxin", src=("AA", 44),
     why="Digoxin's indications are to slow the ventricular rate and to induce heart block in atrial flutter and fibrillation.",
     wrong=[("Dofetilide", "Dofetilide is used to maintain normal rhythm in atrial fibrillation, not to slow the ventricular rate by heart block."),
            ("Quinidine", "Quinidine is used to maintain rhythm with atrial flutter or fibrillation, not to induce heart block."),
            ("Adenosine", "Adenosine is listed for paroxysmal supraventricular tachycardia, briefly stopping the heart; it is not used to induce heart block.")]),

dict(q="Which antiarrhythmic should be avoided with calcium channel blockers and beta blockers?",
     ans="Digoxin", src=("AA", 44),
     why="Calcium channel blockers and beta blockers are to be avoided with digoxin, which already slows atrioventricular conduction and can induce heart block.",
     wrong=[("Lidocaine", "Lidocaine's listed cautions are seizures and age; no beta blocker or calcium channel blocker restriction is given for it."),
            ("Magnesium sulfate", "Magnesium sulfate's listed problems are bradycardia, flushing, headache and respiratory paralysis, with no such combination warning."),
            ("Adenosine", "Adenosine's listed points are a half-life of about 10 seconds and flushing, shortness of breath and chest burning, not this warning.")]),

dict(q="Which drug is the listed treatment for torsades de pointes?",
     ans="Magnesium sulfate", src=("AA", 45),
     why="Magnesium sulfate, given intravenously, is the listed indication for torsades de pointes.",
     wrong=[("Amiodarone", "Amiodarone is listed for recurrent or acute ventricular tachycardia and fibrillation; torsades de pointes is treated with magnesium sulfate."),
            ("Adenosine", "Adenosine is listed for paroxysmal supraventricular tachycardia; torsades de pointes is treated with magnesium sulfate."),
            ("Digoxin", "Digoxin is used to slow the ventricular rate and induce heart block in atrial flutter or fibrillation, not for torsades de pointes.")]),

dict(q="Which antiarrhythmic can cause respiratory paralysis?",
     ans="Magnesium sulfate", src=("AA", 45),
     why="Magnesium sulfate's toxicities are bradycardia, flushing, headache and respiratory paralysis.",
     wrong=[("Amiodarone", "Amiodarone's lung toxicity is pneumonitis and pulmonary fibrosis (potentially fatal), not respiratory paralysis."),
            ("Sotalol", "Sotalol's respiratory effect is bronchospasm from its beta-blocking activity, not respiratory paralysis."),
            ("Adenosine", "Adenosine causes shortness of breath with flushing and burning in the chest, not respiratory paralysis.")]),
]
