# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Antiarrhythmic Drugs (Lecture 10), topic: class III (potassium channel blockers):
amiodarone, dofetilide and sotalol.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. Key authored FIRST (c == 0).

SOURCE. Antiarrhythmics.pptx slides 30 (class III actions with the action potential picture), 31-33 (amiodarone),
34 (dofetilide), 35-36 (sotalol). Slide 5 for the class names, slide 6 for the class indications.

LEFT OUT ON PURPOSE:
  * amiodarone "IV - terminate acute ventricular tachycardia or fibrillation replacing lidocaine in MI" (slide 31):
    current resuscitation guidance lists amiodarone or lidocaine, so the study guide carries a "Current guidelines
    differ" note and no question turns on "replacing lidocaine";
  * amiodarone "maintain normal rate in atrial fibrillation" (slide 31): the lecturer called amiodarone rhythm control,
    so the rate-versus-rhythm wording is not keyed;
  * numbers (the 40-day half-life range, the torsades percentage) are never bare keys;
  * the lecturer's spoken asides (lung-function and vision checks, starting dofetilide in hospital, sotalol being
    nonselective, the absolute and relative refractory periods).
mis = misconception tag on every distractor (WRITER.md rule 5)
"""

D = "Antiarrhythmics.pptx"
IO_CLASS = "Identify antiarrhythmic drug classes and commonly prescribed antiarrhythmic drugs"
IO_MOA = "Describe the molecular mechanism of action of antiarrhythmic drugs"
IO_IND = "Identify indications for commonly used antiarrhythmic drugs"
IO_ADME = "Describe absorption, distribution, metabolism, and excretion of antiarrhythmic drugs"
IO_TOX = "Summarize side effects and toxic manifestations of antiarrhythmic drugs"
IO_AE = "Describe adverse effects of antiarrhythmic drugs"
IO_CONTRA = "Identify contraindications for antiarrhythmic drugs"
IO_INTER = "Discuss potential drug-drug, drug-food, and drug-herb interactions with antiarrhythmic drugs"
IO_PROT = "List commonly used protocols and patient monitoring for antiarrhythmic drugs"
IO_EDU = "Outline appropriate patient education for antiarrhythmic drugs"

MECH, ADJ, REV, LAY, STAGE, RULED, COMP = ("confused mechanism or drug class", "adjacent fact", "reversed direction or value",
                                           "common lay belief", "wrong stage or severity", "ruled out by a stated finding",
                                           "competing diagnosis")


def Q(topic, io, slot, q, opts, slide):
    return {"topic": topic, "io": io, "slot": slot, "q": q, "opts": opts, "c": 0, "cite": "%s, Slide %d" % (D, slide)}


QUESTIONS = [

# ---- class III actions (slide 30, picture) -----------------------------------------------------------
Q("Class III actions", IO_CLASS, "class",
  "Which antiarrhythmic class prolongs repolarization by blocking potassium channels?",
  [["Class III", "Correct. Class 3 drugs are the potassium channel blockers that prolong repolarization: amiodarone, dofetilide and sotalol."],
   ["Class I", "Class I drugs block sodium channels and act on phase 0; the potassium channel blockers that prolong repolarization are class III.", MECH],
   ["Class II", "Class II drugs are the beta receptor antagonists, which flatten phase 4; potassium channel blockers are class III.", MECH],
   ["Class IV", "Class IV drugs block L-type calcium channels in the nodes; the potassium channel blockers are class III.", MECH]], 5),

Q("Class III actions", IO_MOA, "mechanism",
  "Class III antiarrhythmics prolong repolarization through which ion effect?",
  [["Reduced potassium efflux", "Correct. Class III drugs reduce potassium efflux, which prolongs phase 3 repolarization and the refractory period."],
   ["Increased potassium efflux", "More potassium leaving the cell would speed repolarization; class III drugs reduce potassium efflux to prolong it.", REV],
   ["Reduced sodium influx", "Reducing sodium influx in phase 0 is the class I mechanism; class III drugs reduce potassium efflux.", MECH],
   ["Reduced calcium influx", "Blocking calcium influx through the L-type channel is the class IV mechanism; class III drugs reduce potassium efflux.", MECH]], 30),

Q("Class III actions", IO_MOA, "mechanism",
  "Which change in the cardiac action potential is the signature of class III drugs?",
  [["Delayed phase 3 repolarization", "Correct. Class III drugs prolong phase 3, so the action potential and the refractory period both last longer."],
   ["Slower phase 0 upstroke", "A slower, lower phase 0 upstroke is the class IA and IC picture; class III leaves the upstroke and delays phase 3.", MECH],
   ["Earlier phase 3 repolarization", "Earlier repolarization (a shortened phase 3) is the class IB picture; class III delays phase 3.", REV],
   ["Flatter phase 4 depolarization", "A flatter phase 4 in pacemaker cells is the class II and class IV picture; class III delays phase 3.", MECH]], 30),

# ---- amiodarone (slides 31-33) -----------------------------------------------------------------------
Q("Amiodarone", IO_MOA, "mechanism",
  "Which drug blocks potassium, sodium and calcium channels as well as alpha and beta receptors?",
  [["Amiodarone", "Correct. Amiodarone blocks potassium channels, inactivated sodium channels, calcium channels and alpha and beta receptors."],
   ["Dofetilide", "Dofetilide is a potent pure potassium channel blocker; the drug that blocks all of these is amiodarone.", MECH],
   ["Sotalol", "Sotalol combines beta-blocking activity with potassium channel block only; amiodarone blocks all four targets.", MECH],
   ["Propafenone", "Propafenone is a class IC sodium channel blocker with beta-blocking activity; amiodarone blocks all four targets.", MECH]], 32),

Q("Amiodarone", IO_TOX, "adverse effect",
  "Why can amiodarone cause hyperthyroidism or hypothyroidism?",
  [["It is a thyroid hormone analog", "Correct. Amiodarone is an analog of thyroid hormone, and both hyperthyroidism and hypothyroidism are on its toxicity list."],
   ["It blocks alpha and beta receptors", "Amiodarone does block alpha and beta receptors, but its thyroid effects come from being an analog of thyroid hormone.", MECH],
   ["It is cleared unchanged by the kidneys", "Elimination unchanged by the kidneys describes dofetilide; amiodarone's thyroid effects come from its thyroid hormone structure.", ADJ],
   ["It inhibits the sodium-potassium pump", "Sodium-potassium ATPase inhibition is digoxin's mechanism; amiodarone affects the thyroid because it is a thyroid hormone analog.", MECH]], 31),

Q("Amiodarone", IO_TOX, "adverse effect",
  "Which amiodarone toxicity is listed as potentially fatal?",
  [["Pulmonary fibrosis", "Correct. Pneumonitis and pulmonary fibrosis are amiodarone's potentially fatal toxicity."],
   ["Corneal deposits", "Corneal deposits are an amiodarone eye toxicity, but the one listed as potentially fatal is pulmonary fibrosis.", STAGE],
   ["Photosensitivity", "Photosensitivity is an amiodarone skin effect, but the toxicity listed as potentially fatal is pulmonary fibrosis.", STAGE],
   ["Blue-gray skin", "Blue-gray skin color is a visible amiodarone effect, but the toxicity listed as potentially fatal is pulmonary fibrosis.", STAGE]], 33),

Q("Amiodarone", IO_EDU, "education",
  "A patient starting long-term amiodarone should be told to protect the skin from sunlight because of which effect?",
  [["Photosensitivity", "Correct. Photosensitivity is on amiodarone's toxicity list, along with a blue-gray skin color."],
   ["Flushing", "Flushing is listed for adenosine and magnesium sulfate, and sunlight does not trigger it; amiodarone causes photosensitivity.", ADJ],
   ["Hypersensitivity", "Hypersensitivity is listed for lidocaine; the sun-related amiodarone effect is photosensitivity.", ADJ],
   ["Lupus-like rash", "A lupus-like syndrome is procainamide's, more often in slow acetylators; amiodarone's sun-related effect is photosensitivity.", ADJ]], 33),

Q("Amiodarone", IO_TOX, "adverse effect",
  "Which antiarrhythmic can turn the skin blue-gray?",
  [["Amiodarone", "Correct. Blue-gray skin color, with photosensitivity, is on amiodarone's toxicity list."],
   ["Dofetilide", "Dofetilide's listed adverse effects are torsades de pointes and marked QT prolongation; blue-gray skin is amiodarone's.", ADJ],
   ["Sotalol", "Sotalol's listed toxicities are torsades de pointes and bronchospasm; blue-gray skin is amiodarone's.", ADJ],
   ["Quinidine", "Quinidine's listed toxicities include cinchonism and thrombocytopenia; blue-gray skin is amiodarone's.", ADJ]], 33),

Q("Amiodarone", IO_TOX, "adverse effect",
  "Which eye finding is listed among amiodarone's toxicities?",
  [["Corneal deposits", "Correct. Corneal deposits are on amiodarone's toxicity list."],
   ["Nystagmus", "Nystagmus is the early sign of lidocaine toxicity; amiodarone's listed eye finding is corneal deposits.", ADJ],
   ["Glaucoma", "Glaucoma is a contraindication to disopyramide because of its anticholinergic action; amiodarone causes corneal deposits.", ADJ],
   ["Blurred vision with tinnitus", "Blurred vision with tinnitus and dizziness is cinchonism from quinidine; amiodarone's listed eye finding is corneal deposits.", ADJ]], 33),

Q("Amiodarone", IO_TOX, "adverse effect",
  "Which neurologic effects are listed for amiodarone?",
  [["Neuropathy and ataxia", "Correct. Amiodarone's neurotoxicity includes neuropathy, muscle weakness and ataxia."],
   ["Seizures and nystagmus", "Seizures and nystagmus are part of lidocaine's central nervous system toxicity; amiodarone causes neuropathy and ataxia.", ADJ],
   ["Tinnitus and dizziness", "Tinnitus, dizziness and blurred vision are quinidine's cinchonism; amiodarone causes neuropathy and ataxia.", ADJ],
   ["Sedation and fatigue", "Sedation and fatigue are listed for metoprolol and acebutolol; amiodarone causes neuropathy and ataxia.", ADJ]], 33),

Q("Amiodarone", IO_TOX, "adverse effect",
  "Besides the lungs, thyroid, skin and eyes, which organ's dysfunction is listed for amiodarone?",
  [["Liver", "Correct. Hepatic dysfunction is on amiodarone's toxicity list."],
   ["Kidney", "The kidneys are where dofetilide is mainly eliminated unchanged; amiodarone's listed organ dysfunction is hepatic.", ADJ],
   ["Pancreas", "Pancreatic injury is not on amiodarone's list; its organ toxicities are lung, thyroid, skin, eye, nerve and liver.", LAY],
   ["Bone marrow", "Bone marrow suppression is listed for procainamide; amiodarone's listed organ dysfunction is hepatic.", ADJ]], 33),

Q("Amiodarone", IO_ADME, "protocol",
  "Why may amiodarone require loading doses?",
  [["Its half-life is very long", "Correct. Amiodarone's half-life averages about 40 days, with slow onset and slow elimination, so loading doses may be needed."],
   ["Its half-life is very short", "A very short half-life (about 10 seconds) describes adenosine; amiodarone's half-life is very long.", REV],
   ["It has extensive first-pass metabolism", "Extensive first-pass metabolism is why lidocaine is given intravenously; amiodarone needs loading because of its long half-life.", ADJ],
   ["It is eliminated unchanged by the kidneys", "Elimination unchanged by the kidneys is dofetilide's; amiodarone needs loading because of its long half-life.", ADJ]], 31),

Q("Amiodarone", IO_IND, "indication",
  "Which ventricular arrhythmia is a listed indication for amiodarone?",
  [["Refractory ventricular tachycardia", "Correct. Amiodarone is listed for recurrent ventricular tachycardia or fibrillation resistant to other drugs."],
   ["Ventricular ectopic beats", "Ventricular ectopic beats are listed for propranolol; amiodarone is for ventricular tachycardia resistant to other drugs.", ADJ],
   ["Wolff-Parkinson-White syndrome", "Wolff-Parkinson-White syndrome is listed for lidocaine and adenosine, and it is not a ventricular arrhythmia; amiodarone is for refractory ventricular tachycardia.", ADJ],
   ["Torsades de pointes", "Torsades de pointes is treated with magnesium sulfate, and prolonging repolarization can provoke it; amiodarone is for refractory ventricular tachycardia.", REV]], 31),

Q("Amiodarone", IO_INTER, "interaction",
  "Amiodarone raises the levels of which pair of drugs?",
  [["Digoxin and warfarin", "Correct. Amiodarone increases digoxin, warfarin, flecainide, phenytoin and procainamide."],
   ["Codeine and morphine", "Codeine and morphine are the opioids named for quinidine's cytochrome P450 2D6 inhibition; amiodarone raises digoxin and warfarin.", ADJ],
   ["Verapamil and diltiazem", "Verapamil and diltiazem are calcium channel blockers to avoid alongside digoxin; amiodarone raises digoxin and warfarin.", ADJ],
   ["Lidocaine and esmolol", "Lidocaine and esmolol are intravenous agents outside amiodarone's list, which is digoxin, warfarin, flecainide, phenytoin and procainamide.", ADJ]], 33),

Q("Amiodarone", IO_INTER, "interaction",
  "Which antiarrhythmic's level rises when amiodarone is added?",
  [["Flecainide", "Correct. Amiodarone increases flecainide and procainamide, as well as digoxin, warfarin and phenytoin."],
   ["Adenosine", "Adenosine is outside amiodarone's interaction list; amiodarone raises flecainide, procainamide, digoxin, warfarin and phenytoin.", ADJ],
   ["Esmolol", "Esmolol is outside amiodarone's interaction list; amiodarone raises flecainide, procainamide, digoxin, warfarin and phenytoin.", ADJ],
   ["Magnesium sulfate", "Magnesium sulfate is outside amiodarone's interaction list; amiodarone raises flecainide, procainamide, digoxin, warfarin and phenytoin.", ADJ]], 33),

# ---- dofetilide (slide 34) ---------------------------------------------------------------------------
Q("Dofetilide", IO_MOA, "mechanism",
  "Which antiarrhythmic is a potent pure potassium channel blocker?",
  [["Dofetilide", "Correct. Dofetilide is a potent pure potassium channel blocker, used for normal rhythm in atrial fibrillation."],
   ["Amiodarone", "Amiodarone blocks potassium, sodium and calcium channels and alpha and beta receptors, so it is not a pure blocker.", MECH],
   ["Sotalol", "Sotalol adds beta-blocking activity to its potassium channel block; the pure potassium channel blocker is dofetilide.", MECH],
   ["Flecainide", "Flecainide blocks sodium and potassium channels in the ventricles and is class IC; the pure potassium channel blocker is dofetilide.", MECH]], 34),

Q("Dofetilide", IO_IND, "indication",
  "Dofetilide is listed for which use?",
  [["Normal rhythm in atrial fibrillation", "Correct. Dofetilide's listed indication is normal rhythm in atrial fibrillation."],
   ["Slowing the ventricular rate", "Slowing the ventricular rate in atrial flutter or fibrillation is digoxin's listed use; dofetilide is for normal rhythm.", MECH],
   ["Terminating torsades de pointes", "Torsades de pointes is treated with intravenous magnesium sulfate, and dofetilide can cause it.", REV],
   ["Paroxysmal supraventricular tachycardia", "Paroxysmal supraventricular tachycardia is listed for adenosine; dofetilide is for normal rhythm in atrial fibrillation.", ADJ]], 34),

Q("Dofetilide", IO_AE, "adverse effect",
  "Which adverse effect is the main danger of dofetilide?",
  [["Torsades de pointes", "Correct. Dofetilide's listed adverse effects are torsades de pointes and marked QT prolongation."],
   ["Pulmonary fibrosis", "Pulmonary fibrosis is amiodarone's potentially fatal toxicity; dofetilide's danger is torsades de pointes.", ADJ],
   ["Agranulocytosis", "Agranulocytosis is listed for propafenone; dofetilide's danger is torsades de pointes.", ADJ],
   ["Lupus-like syndrome", "A lupus-like syndrome is procainamide's, more often in slow acetylators; dofetilide's danger is torsades de pointes.", ADJ]], 34),

Q("Dofetilide", IO_ADME, "mechanism",
  "How is dofetilide mainly eliminated?",
  [["Unchanged by the kidneys", "Correct. Dofetilide is mainly eliminated unchanged in the kidneys."],
   ["By hepatic metabolism", "Hepatic metabolism describes verapamil and diltiazem, hence caution in liver damage; dofetilide leaves unchanged by the kidneys.", ADJ],
   ["By first-pass metabolism", "Extensive first-pass metabolism describes lidocaine, which is why it is given intravenously; dofetilide leaves by the kidneys.", ADJ],
   ["By hepatic acetylation", "Acetylation describes procainamide, whose fast acetylators make more of its active metabolite; dofetilide leaves by the kidneys.", ADJ]], 34),

Q("Dofetilide", IO_PROT, "monitoring",
  "Which restriction applies to prescribing dofetilide?",
  [["Prescribers need special training", "Correct. Dofetilide has limited availability, restricted to those with special training."],
   ["It must be given intravenously", "Intravenous-only use describes lidocaine, because of extensive first-pass metabolism; dofetilide needs special training.", ADJ],
   ["It needs loading doses", "Loading doses are for amiodarone, with its 40-day half-life; dofetilide's restriction is special prescriber training.", ADJ],
   ["It is avoided with beta blockers", "Avoiding beta blockers and calcium channel blockers is a digoxin caution; dofetilide's restriction is special prescriber training.", ADJ]], 34),

# ---- sotalol (slides 35-36) --------------------------------------------------------------------------
Q("Sotalol", IO_CLASS, "class",
  "Sotalol combines the actions of which two antiarrhythmic classes?",
  [["Classes II and III", "Correct. Sotalol has beta-blocking (class II) activity and inhibits potassium channels (class III)."],
   ["Classes I and II", "Sodium channel block with beta-blocking activity is propafenone, a class IC drug; sotalol is classes II and III.", MECH],
   ["Classes I and III", "Blocking sodium and potassium channels describes flecainide, a class IC drug; sotalol is classes II and III.", MECH],
   ["Classes II and IV", "Classes II and IV are separate drug groups (beta blockers and calcium channel blockers) that act on the nodes; sotalol is classes II and III.", MECH]], 35),

Q("Sotalol", IO_IND, "indication",
  "Which is a listed indication for sotalol?",
  [["Atrial flutter and fibrillation", "Correct. Sotalol is listed for atrial flutter and fibrillation and for ventricular tachyarrhythmia."],
   ["Torsades de pointes", "Torsades de pointes is on sotalol's toxicity list; it is treated with magnesium sulfate.", REV],
   ["Wolff-Parkinson-White syndrome", "Wolff-Parkinson-White syndrome is listed for lidocaine and adenosine; sotalol is for atrial flutter and fibrillation.", ADJ],
   ["Sick sinus syndrome", "Sick sinus syndrome is on the avoid list for verapamil and diltiazem; sotalol is for atrial flutter and fibrillation.", ADJ]], 35),

Q("Sotalol", IO_TOX, "adverse effect",
  "Which pair of toxicities is listed for sotalol?",
  [["Torsades and bronchospasm", "Correct. Sotalol's toxicities are torsades de pointes (from potassium channel block) and bronchospasm (from beta blockade)."],
   ["Lupus and marrow suppression", "Lupus-like syndrome and bone marrow suppression are procainamide's; sotalol causes torsades and bronchospasm.", ADJ],
   ["Cinchonism and thrombocytopenia", "Cinchonism and thrombocytopenia are quinidine's; sotalol causes torsades and bronchospasm.", ADJ],
   ["Hypotension and edema", "Hypotension and edema are listed for verapamil and diltiazem; sotalol causes torsades and bronchospasm.", ADJ]], 36),

Q("Sotalol", IO_CONTRA, "drug choice",
  "A patient with asthma needs a drug for atrial fibrillation. Which listed drug carries a bronchospasm risk?",
  [["Sotalol", "Correct. Sotalol has beta-blocking activity, and bronchospasm is on its toxicity list."],
   ["Dofetilide", "Dofetilide is a pure potassium channel blocker whose danger is torsades de pointes, not bronchospasm.", ADJ],
   ["Amiodarone", "Amiodarone's lung toxicity is pneumonitis and pulmonary fibrosis over time; bronchospasm is listed for sotalol.", ADJ],
   ["Digoxin", "Digoxin's listed toxicities are gastrointestinal and central nervous system effects; bronchospasm is listed for sotalol.", ADJ]], 36),
]
