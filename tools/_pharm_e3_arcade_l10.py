# -*- coding: utf-8 -*-
"""Arcade decks for Pharmacology I Exam 3, Lecture 10 (Antiarrhythmics), drafted 2026-10-16.

Imported by add_pharm_e3_arcade.py next to _pharm_e3_arcade_l9.py. Five decks, one per drug group of the deck,
atomic question -> short answer cards per [[arcade_content_policy]], slide facts only (the deck has no speaker notes),
no doses, US spelling, abbreviations written out (a drug-name suffix or a chemical name is not an abbreviation).

Same contract as Lecture 9: every card is written with C(deck, question, answer, slide(s), verify...) and the adder
PROVES each verify substring is on the cited Lecture 10 slide (pharm_e3_lib.slide_text("L10", n)). No recording
quotes are carried (tf stays empty).

Deliberately NOT carried: every dose (the magnesium sulfate amount); channel affinity (open or inactivated) and
dissociation rate, which the lecturer said he will not test; lidocaine and adenosine for Wolff-Parkinson-White (slides
17 and 42; current guidelines differ); propranolol and blood glucose (slide 28 says hyperglycemia, the recording says
hypoglycemia); "Anticoagulants and Digitalis" under quinidine conversion; digoxin "inhibits calcium channels in the
atrioventricular node"; amiodarone "maintain normal rate in atrial fibrillation"; bare numbers as answers (half-lives
and percentages appear only inside a question or beside the fact they belong to); the chemical structures.

NOT YET IN arcade.js until the integrator runs `python3 tools/add_pharm_e3_arcade.py`.
"""
REG = []     # (deck id, question, [(slide, [verify])], [quotes])


def C(deck, q, a, slide, verify=(), tf=()):
    pairs = [(slide, list(verify))] if isinstance(slide, int) else [(s, list(v)) for s, v in slide]
    REG.append((deck, q, pairs, list(tf)))
    return (q, a)


PULSE_ICON = '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>'

CLS1A, CLS1BC, CLS24 = "pharm-aa-classes-1a", "pharm-aa-1b-1c", "pharm-aa-2-4"
CLS3, MISC = "pharm-aa-3", "pharm-aa-misc"

DECKS = [
 (CLS1A, "Antiarrhythmic Classes &amp; Class IA", "accent1", PULSE_ICON, [
  # ---- principles and classes
  C(CLS1A, "Which precipitating factors should be identified and removed before antiarrhythmic therapy?", "Hypoxia, ischemia and electrolyte problems.", 3, ["hypoxia, ischemia, electrolytes"]),
  C(CLS1A, "Which risk do all antiarrhythmics share?", "They may all induce arrhythmias.", 3, ["all Antiarrhythmics may induce arrhythmias"]),
  C(CLS1A, "Which drugs make up class I antiarrhythmics?", "Sodium channel blockers.", 5, ["Sodium Channel Blockers"]),
  C(CLS1A, "Which drugs make up class II antiarrhythmics?", "Beta receptor antagonists (beta blockers).", 5, ["Beta Receptor Antagonists"]),
  C(CLS1A, "What do class III antiarrhythmics do?", "Prolong repolarization by blocking potassium channels.", 5, ["Prolong Repolarization (K+)"]),
  C(CLS1A, "Which drugs make up class IV antiarrhythmics?", "Calcium channel blockers.", 5, ["Calcium Channel Blockers"]),
  # ---- class IA
  C(CLS1A, "What do class IA drugs do to phase 0, conduction and the action potential?", "Slow phase 0 and conduction, and prolong the action potential.", 8, ["Slow Phase 0", "slow conduction", "prolong action potential"]),
  C(CLS1A, "What is quinidine chemically?", "The D-isomer of quinine.", 9, ["D - Isomer of Quinine"]),
  C(CLS1A, "Which two indirect actions does quinidine have?", "Anticholinergic action and alpha blockade at higher doses.", 9, ["Indirect actions", "Anticholinergic", "blocker at higher doses"]),
  C(CLS1A, "Which enzyme does quinidine inhibit?", "Cytochrome P450 2D6 (CYP2D6), affecting codeine and morphine.", 10, ["CYP 2D6 inhibitor (codeine, morphine)"]),
  C(CLS1A, "Which gastrointestinal effects does quinidine cause in 30 to 50 percent of patients?", "Nausea, vomiting and diarrhea.", 11, ["Nausea, vomiting, Diarrhea (30-50%)"]),
  C(CLS1A, "What is cinchonism, a quinidine toxicity?", "Tinnitus, dizziness and blurred vision.", 11, ["Cinchonism - tinnitus, dizziness, blurred vision"]),
  C(CLS1A, "Which blood disorder can quinidine cause?", "Thrombocytopenia, which may be fatal.", 11, ["Thrombocytopenia (may be fatal)"]),
  C(CLS1A, "Why does procainamide come as a slow-release preparation?", "Its duration of action is short, only 3 to 4 hours.", 12, ["Short duration of action (3 - 4 hours)", "Slow release preparation"]),
  C(CLS1A, "Which class of activity does procainamide's active acetylated metabolite have?", "Class III activity.", 12, ["Active acetylated metabolite", "Class Three activity"]),
  C(CLS1A, "Which syndrome does procainamide cause, more often in slow acetylators?", "A lupus-like syndrome.", 13, ["Lupus like syndrome (25-50%, more often in slow acetylators)"]),
  C(CLS1A, "How does disopyramide differ from quinidine?", "More anticholinergic action, plus a negative inotropic effect.", 14, ["Effects similar to Quinidine", "More Anticholinergic actions", "Negative inotropic effects"]),
  C(CLS1A, "Which eye condition contraindicates disopyramide?", "Glaucoma.", 15, ["Contraindicated: heart block, hypersensitivity, glaucoma"]),
 ]),

 (CLS1BC, "Class IB &amp; IC Sodium Channel Blockers", "accent2", PULSE_ICON, [
  # ---- class IB: lidocaine
  C(CLS1BC, "What do class IB drugs do to phase 3?", "Shorten it.", 16, ["Shorten Phase 3"]),
  C(CLS1BC, "Whose automaticity do class IB drugs decrease?", "That of ectopic foci.", 16, ["Decrease ectopic foci automaticity"]),
  C(CLS1BC, "Why is lidocaine given intravenously?", "It undergoes extensive first-pass metabolism.", 18, ["Given IV (Extensive first pass metabolism)"]),
  C(CLS1BC, "In which tissue is lidocaine most effective on sodium channels?", "Ischemic tissue, with less effect on normal tissue.", 18, ["Most effective on Na channels in ischemic tissue", "Less effect on normal tissue"]),
  C(CLS1BC, "Which arrhythmias does lidocaine not treat effectively?", "Atrial arrhythmias.", 18, ["Not effective against atrial arrhythmias"]),
  C(CLS1BC, "Which ventricular rhythms is lidocaine used for?", "Ventricular tachycardia, premature beats and ventricular fibrillation.", 17, ["Ventricular tachycardia, premature beats", "Ventricular fibrillation"]),
  C(CLS1BC, "What is the early sign of lidocaine toxicity?", "Nystagmus.", 19, ["Nystagmus (early sign of toxicity)"]),
  C(CLS1BC, "What are lidocaine's contraindications?", "Seizures and age.", 19, ["Contraindications: seizures, age"]),
  C(CLS1BC, "What does lidocaine toxicity do to atrioventricular conduction?", "It increases atrioventricular conduction.", 19, ["Increases AV conduction"]),
  # ---- class IC: flecainide, propafenone
  C(CLS1BC, "Which class I subgroup affects the normal heart?", "Class IC.", 20, ["Class 1C", "Affect normal heart"]),
  C(CLS1BC, "Which channels does flecainide block in the ventricles?", "Sodium and potassium channels.", 21, ["Blocks Na+ channels and K+ channels in ventricles"]),
  C(CLS1BC, "Which electrocardiogram intervals does flecainide prolong?", "The PR, QRS and QT intervals.", 21, ["Prolongs PR, QRS and QT intervals"]),
  C(CLS1BC, "Which patients should receive flecainide?", "Only patients without significant structural damage to the heart.", 22, ["Use only in patients without significant structural damage to heart"]),
  C(CLS1BC, "What does flecainide do to mortality in myocardial infarction?", "It increases it.", 23, ["mortality in MI"]),
  C(CLS1BC, "Which ventricular rhythm toxicity does flecainide cause?", "Ventricular tachycardia resistant to treatment.", 23, ["Ventricular tachycardia resistant to treatment"]),
  C(CLS1BC, "How does propafenone differ from flecainide?", "Same mechanism, plus beta-blocking activity.", 24, ["Same mechanism as Flecainide", "blocking activity"]),
  C(CLS1BC, "Which blood disorders can propafenone cause?", "Agranulocytosis, anemia and thrombocytopenia.", 24, ["Agranulocytosis, anemia, thrombocytopenia"]),
  C(CLS1BC, "What can propafenone do to congestive heart failure?", "Worsen it.", 24, ["worsen CHF"]),
 ]),

 (CLS24, "Class II &amp; IV: Beta Blockers and Calcium Channel Blockers", "accent3", PULSE_ICON, [
  # ---- class II
  C(CLS24, "What do class II drugs do to phase 4 depolarization?", "Decrease it.", 25, ["Decrease Phase 4 depolarization"]),
  C(CLS24, "What kind of beta blocker is propranolol?", "A nonselective, membrane-stabilizing beta blocker.", 26, ["Nonselective Beta blocker", "Membrane stabilizing"]),
  C(CLS24, "Which ectopic beats does propranolol suppress?", "Premature ventricular beats.", 26, ["Suppress premature ventricular beats"]),
  C(CLS24, "What are propranolol's antiarrhythmic indications?", "Supraventricular arrhythmias, ventricular ectopic beats and myocardial infarction.", 27, ["Supraventricular arrhythmias", "Ventricular ectopic beats", "Myocardial Infarction"]),
  C(CLS24, "Which airway toxicity does propranolol cause?", "Bronchospasm.", 28, ["Bronchospasm"]),
  C(CLS24, "Which conduction problem is on propranolol's toxicity list?", "Heart block.", 28, ["Heart block"]),
  C(CLS24, "Which two beta-1 selective blockers are listed with propranolol?", "Metoprolol and acebutolol.", 29, ["Metoprolol, Acebutolol", "selective blocker"]),
  C(CLS24, "What advantage do metoprolol and acebutolol have over propranolol?", "Less bronchospasm.", 29, ["Less Bronchospasm"]),
  C(CLS24, "Which central effects do metoprolol and acebutolol cause?", "Sedation and fatigue.", 29, ["CNS sedation and fatigue"]),
  C(CLS24, "Which beta blocker is intravenous and short acting?", "Esmolol.", 29, ["Esmolol, IV short acting"]),
  # ---- class IV
  C(CLS24, "Which calcium channel do class IV drugs block?", "The L-type channel.", 37, ["Blocks L-type channel"]),
  C(CLS24, "What do class IV drugs do to atrioventricular node conduction?", "Slow it.", 37, ["Slow AV node conduction"]),
  C(CLS24, "Which two calcium channel blockers are used as antiarrhythmics?", "Verapamil and diltiazem.", 38, ["Verapamil, Diltiazem"]),
  C(CLS24, "In which tissue are verapamil and diltiazem most effective?", "The most active tissue.", 38, ["Most effective in most active tissue"]),
  C(CLS24, "What do verapamil and diltiazem do to the sinoatrial node?", "Suppress it.", 38, ["Suppresses SA node"]),
  C(CLS24, "What are the indications for verapamil and diltiazem?", "Paroxysmal supraventricular tachycardia and atrial fibrillation.", 39, ["Supraventricular Tachycardia (PSVT)", "Atrial fibrillation"]),
  C(CLS24, "Why do verapamil and diltiazem call for caution in liver damage?", "They undergo hepatic metabolism.", 39, ["Hepatic metabolism, caution in liver damage"]),
  C(CLS24, "When should verapamil and diltiazem be avoided?", "Ventricular arrhythmias, sick sinus syndrome and depressed cardiac function.", 39, ["Avoid in ventricular arrhythmias, sick sinus syndrome, depressed cardiac function"]),
 ]),

 (CLS3, "Class III Potassium Channel Blockers", "accent4", PULSE_ICON, [
  C(CLS3, "How do class III drugs prolong phase 3 repolarization?", "By reducing potassium efflux.", 30, ["Reduces potassium efflux", "Prolongs phase 3 repolarization"]),
  # ---- amiodarone
  C(CLS3, "Amiodarone is an analog of which hormone?", "Thyroid hormone.", 31, ["Analog of Thyroid hormone"]),
  C(CLS3, "Why may amiodarone require loading doses?", "Its half-life is about 40 days, with slow onset and slow elimination.", 31, ["T1/2 40 days", "Slow onset. Slow elimination", "may require loading doses"]),
  C(CLS3, "Which ventricular arrhythmias is amiodarone used for?", "Recurrent ventricular tachycardia or fibrillation resistant to other drugs.", 31, ["Recurrent ventricular tachycardia or fibrillation resistant to other drugs"]),
  C(CLS3, "What does intravenous amiodarone terminate?", "Acute ventricular tachycardia or fibrillation.", 31, ["IV - terminate acute ventricular tachycardia or fibrillation"]),
  C(CLS3, "Which channels and receptors does amiodarone block?", "Potassium, sodium and calcium channels, plus alpha and beta receptors.", 32, ["blocks potassium channels", "sodium channels", "blocks calcium channels", "receptors"]),
  C(CLS3, "Which potentially fatal lung toxicity does amiodarone cause?", "Pneumonitis and pulmonary fibrosis.", 33, ["Pneumonitis, pulmonary fibrosis (potentially fatal)"]),
  C(CLS3, "Which skin changes does amiodarone cause?", "Blue-gray skin color and photosensitivity.", 33, ["Blue-Grey skin color, photosensitivity"]),
  C(CLS3, "Which eye finding does amiodarone cause?", "Corneal deposits.", 33, ["Corneal deposits"]),
  C(CLS3, "Which thyroid problems can amiodarone cause?", "Hyperthyroidism or hypothyroidism.", 33, ["Thyroid abnormalities (hyper,hypo)"]),
  C(CLS3, "Which drugs does amiodarone increase?", "Digoxin, warfarin, flecainide, phenytoin and procainamide.", 33, ["increases digoxin, warfarin, flecainide, phenytoin, procainamide"]),
  # ---- dofetilide
  C(CLS3, "What kind of potassium channel blocker is dofetilide?", "A potent, pure potassium channel blocker.", 34, ["Potent pure K channel blocker"]),
  C(CLS3, "What is dofetilide used for?", "Normal rhythm in atrial fibrillation.", 34, ["Normal rhythm in atrial fibrillation"]),
  C(CLS3, "Who may prescribe dofetilide?", "Only those with special training; its availability is limited.", 34, ["Limited availability to those with special training"]),
  C(CLS3, "How is dofetilide eliminated?", "Mainly unchanged by the kidneys.", 34, ["Mainly eliminated unchanged in kidneys"]),
  # ---- sotalol
  C(CLS3, "Which two actions does sotalol combine?", "Beta-blocking activity and potassium channel inhibition.", 35, ["blocking activity", "Inhibits K+ channels"]),
  C(CLS3, "What are sotalol's indications?", "Atrial flutter and fibrillation, and ventricular tachyarrhythmia.", 35, ["atrial flutter and fibrillation, ventricular tachyarrhythmia"]),
  C(CLS3, "Which two toxicities does sotalol cause?", "Torsades de pointes and bronchospasm.", 36, ["Torsades de Pointes", "Bronchospasm"]),
 ]),

 (MISC, "Adenosine, Digoxin &amp; Magnesium Sulfate", "accent2", PULSE_ICON, [
  C(MISC, "Which three drugs are the miscellaneous antiarrhythmic agents?", "Adenosine, digitalis (digoxin) and magnesium sulfate.", 40, ["Adenosine", "Digitalis", "Magnesium Sulfate"]),
  # ---- adenosine
  C(MISC, "Which channels does adenosine activate in the atria?", "Potassium channels.", 41, ["Activates potassium channels in atria"]),
  C(MISC, "Which channels does adenosine block?", "Calcium channels.", 41, ["blocks Ca++ channels"]),
  C(MISC, "What does adenosine do to cells?", "It hyperpolarizes them.", 41, ["Hyperpolarizes cells"]),
  C(MISC, "What dramatic effect may adenosine have on the heart?", "It may stop the heart for 2 to 3 seconds.", 41, ["may stop heart for 2-3 seconds"]),
  C(MISC, "Which antiarrhythmic has a half-life of about 10 seconds?", "Adenosine.", 41, ["10 seconds"]),
  C(MISC, "Which tachycardia is adenosine used for?", "Paroxysmal supraventricular tachycardia.", 42, ["Paroxysmal supraventricular tachycardia"]),
  C(MISC, "What are adenosine's toxicities?", "Flushing, shortness of breath and burning in the chest.", 42, ["Flushing 20%", "of breath", "Burning in chest"]),
  # ---- digoxin
  C(MISC, "Which pump does digoxin inhibit?", "The sodium-potassium ATPase.", 43, ["Na/K ATPase inhibition"]),
  C(MISC, "What does digoxin do to autonomic tone?", "Indirectly increases parasympathetic tone and decreases sympathetic tone.", 43, ["Indirectly increases Parasympathetic tone decreases sympathetic"]),
  C(MISC, "What does digoxin do to atrioventricular conduction?", "Slows it, and it can induce heart block.", 43, ["Slows AV conduction", "Can induce heart block"]),
  C(MISC, "What are digoxin's antiarrhythmic indications?", "Slowing the ventricular rate and inducing heart block in atrial flutter or fibrillation.", 44, ["Slow ventricular rate", "Induce Heart Block (Atrial flutter, fibrillation)"]),
  C(MISC, "Which gastrointestinal toxicities does digoxin cause?", "Nausea, vomiting, diarrhea and anorexia.", 44, ["nausea, vomiting, diarrhea, anorexia"]),
  C(MISC, "Which central nervous system toxicities does digoxin cause?", "Confusion, delirium, headache, seizures and visual disturbances.", 44, ["confusion, delirium, headache seizures, visual disturbances"]),
  C(MISC, "Which drug classes should be avoided with digoxin?", "Calcium channel blockers and beta blockers.", 44, ["Avoid calcium blockers", "blockers"]),
  # ---- magnesium sulfate
  C(MISC, "What is magnesium sulfate's antiarrhythmic indication?", "Torsades de pointes, given intravenously.", 45, ["Indication: Torsades de Pointes IV"]),
  C(MISC, "What are magnesium sulfate's toxicities?", "Bradycardia, flushing, headache and respiratory paralysis.", 45, ["Bradycardia", "Flushing", "Headache", "Respiratory paralysis"]),
 ]),
]
