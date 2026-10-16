# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Antiarrhythmic Drugs (Lecture 10), topic: the miscellaneous agents adenosine, digoxin
(digitalis) and magnesium sulfate.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. Key authored FIRST (c == 0).

SOURCE. Antiarrhythmics.pptx slides 5 and 40 (the "others" group), 41-42 (adenosine), 43-44 (digoxin), 45 (magnesium
sulfate).

LEFT OUT ON PURPOSE:
  * adenosine for Wolff-Parkinson-White syndrome (slide 42): current guidance warns against atrioventricular nodal
    blockers in pre-excited atrial fibrillation, so the study guide carries a "Current guidelines differ" note and no
    question turns on it;
  * digoxin "inhibits Ca channels in AV node" (slide 43) is not keyed as its mechanism; the sodium-potassium ATPase is;
  * the magnesium gram amount and the 20% flushing figure are never bare keys (no doses, no bare numbers);
  * the lecturer's spoken asides (the saline flush after an adenosine push, yellow-green halos, drug level monitoring,
    "the two-gram slam").
KEYED TO THE SLIDE WITH A GUIDE NOTE: digoxin "Avoid calcium blockers, beta-blockers" (slide 44). The lecturer read and
affirmed it; current rate-control practice does combine these drugs, which the study guide says in one note.
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

Q("Other agents", IO_CLASS, "class",
  "Outside classes I to IV, which two drugs make up the antiarrhythmic \"others\" group?",
  [["Adenosine and digitalis", "Correct. The classification lists adenosine and digitalis (digoxin) as the others; magnesium sulfate joins them as a miscellaneous agent."],
   ["Amiodarone and sotalol", "Amiodarone and sotalol are class III drugs (sotalol adds class II activity); the others are adenosine and digitalis.", MECH],
   ["Esmolol and verapamil", "Esmolol is a class II beta blocker and verapamil a class IV calcium channel blocker; the others are adenosine and digitalis.", MECH],
   ["Lidocaine and flecainide", "Lidocaine is class IB and flecainide class IC, both sodium channel blockers; the others are adenosine and digitalis.", MECH]], 5),

# ---- adenosine (slides 41-42) ------------------------------------------------------------------------
Q("Adenosine", IO_MOA, "mechanism",
  "How does adenosine act on potassium channels in the atria?",
  [["It activates them", "Correct. Adenosine activates potassium channels in the atria and blocks calcium channels, which hyperpolarizes the cells."],
   ["It blocks them", "Blocking potassium channels is the class III mechanism, which prolongs repolarization; adenosine activates them.", REV],
   ["It inactivates them slowly", "Slow recovery of channels describes class IC sodium channel block; adenosine activates atrial potassium channels.", MECH],
   ["It leaves them unchanged", "Adenosine's action starts at these channels: it activates atrial potassium channels and blocks calcium channels.", REV]], 41),

Q("Adenosine", IO_MOA, "mechanism",
  "What does adenosine do to the membrane potential of atrial and nodal cells?",
  [["Hyperpolarizes the cells", "Correct. Adenosine hyperpolarizes the cells, which decreases conduction velocity and automaticity."],
   ["Depolarizes the cells", "Depolarizing the cells would make firing easier; adenosine hyperpolarizes them and slows conduction.", REV],
   ["Slows the phase 0 upstroke", "Slowing the phase 0 upstroke is the class IA and IC sodium channel effect; adenosine hyperpolarizes the cells.", MECH],
   ["Delays phase 3 repolarization", "Delaying phase 3 is the class III effect; adenosine hyperpolarizes the cells.", MECH]], 41),

Q("Adenosine", IO_MOA, "mechanism",
  "Which antiarrhythmic may stop the heart for 2 to 3 seconds?",
  [["Adenosine", "Correct. Adenosine decreases conduction velocity and may stop the heart for 2 to 3 seconds; its half-life is about 10 seconds."],
   ["Esmolol", "Esmolol is the intravenous, short-acting beta blocker; the drug that may stop the heart for seconds is adenosine.", ADJ],
   ["Digoxin", "Digoxin slows atrioventricular conduction and can induce heart block, but the brief pause is adenosine's.", ADJ],
   ["Magnesium sulfate", "Magnesium sulfate treats torsades de pointes and can cause bradycardia; the brief pause is adenosine's.", ADJ]], 41),

Q("Adenosine", IO_EDU, "education",
  "What should a patient be warned about just before receiving adenosine?",
  [["The heart may stop for a few seconds", "Correct. Adenosine may stop the heart for 2 to 3 seconds, and flushing, shortness of breath and chest burning can follow."],
   ["The skin may turn blue-gray", "Blue-gray skin with photosensitivity is an amiodarone effect over time; adenosine may stop the heart for seconds.", ADJ],
   ["The ears may ring with dizziness", "Tinnitus, dizziness and blurred vision are quinidine's cinchonism; adenosine may stop the heart for seconds.", ADJ],
   ["The hands may shake with blurred vision", "Blurred vision and tremor are listed for flecainide; adenosine may stop the heart for a few seconds.", ADJ]], 41),

Q("Adenosine", IO_ADME, "mechanism",
  "Why is adenosine's effect so brief?",
  [["Its half-life is about 10 seconds", "Correct. Adenosine's half-life is about 10 seconds, so the pause it causes is brief."],
   ["It is cleared unchanged by the kidneys", "Elimination unchanged by the kidneys describes dofetilide; adenosine's effect is brief because of its 10-second half-life.", ADJ],
   ["It undergoes hepatic acetylation", "Acetylation describes procainamide and its active metabolite; adenosine's effect is brief because of its 10-second half-life.", ADJ],
   ["It has extensive first-pass metabolism", "Extensive first-pass metabolism is why lidocaine is given intravenously; adenosine's effect is brief because of its half-life.", ADJ]], 41),

Q("Adenosine", IO_IND, "indication",
  "Which arrhythmia is the main listed indication for adenosine?",
  [["Paroxysmal supraventricular tachycardia", "Correct. Adenosine is listed for paroxysmal supraventricular tachycardia."],
   ["Refractory ventricular tachycardia", "Ventricular tachycardia resistant to other drugs is an amiodarone indication; adenosine is for paroxysmal supraventricular tachycardia.", ADJ],
   ["Ventricular fibrillation", "Ventricular fibrillation is listed for lidocaine and amiodarone; adenosine is for paroxysmal supraventricular tachycardia.", ADJ],
   ["Torsades de pointes", "Torsades de pointes is treated with intravenous magnesium sulfate; adenosine is for paroxysmal supraventricular tachycardia.", ADJ]], 42),

Q("Adenosine", IO_AE, "adverse effect",
  "Which adverse effect occurs in about one in five patients given adenosine?",
  [["Flushing", "Correct. Flushing occurs in about 20% of patients given adenosine, with shortness of breath and chest burning also listed."],
   ["Nystagmus", "Nystagmus is the early sign of lidocaine toxicity; the common adenosine effect is flushing.", ADJ],
   ["Thrombocytopenia", "Thrombocytopenia is listed for quinidine and flecainide; the common adenosine effect is flushing.", ADJ],
   ["Corneal deposits", "Corneal deposits are an amiodarone toxicity of long-term use; the common adenosine effect is flushing.", ADJ]], 42),

Q("Adenosine", IO_TOX, "adverse effect",
  "Which set of adverse effects is listed for adenosine?",
  [["Flushing, shortness of breath, chest burning", "Correct. Adenosine's listed toxicities are flushing (20%), shortness of breath and burning in the chest."],
   ["Bradycardia, flushing, respiratory paralysis", "Bradycardia, flushing, headache and respiratory paralysis are listed for magnesium sulfate; adenosine adds dyspnea and chest burning.", ADJ],
   ["Nausea, confusion, visual disturbances", "Gastrointestinal upset, confusion and visual disturbances are digoxin toxicity; adenosine causes flushing, dyspnea and chest burning.", ADJ],
   ["Tinnitus, dizziness, blurred vision", "Tinnitus, dizziness and blurred vision are quinidine's cinchonism; adenosine causes flushing, dyspnea and chest burning.", ADJ]], 42),

# ---- digoxin (slides 43-44) --------------------------------------------------------------------------
Q("Digoxin", IO_MOA, "mechanism",
  "What is digoxin's primary molecular action?",
  [["Sodium-potassium ATPase inhibition", "Correct. Digoxin (digitalis) inhibits the sodium-potassium ATPase, slows atrioventricular conduction and can induce heart block."],
   ["Potassium channel activation", "Activating atrial potassium channels is adenosine's action; digoxin inhibits the sodium-potassium ATPase.", MECH],
   ["Potassium channel blockade", "Blocking potassium channels is the class III mechanism; digoxin inhibits the sodium-potassium ATPase.", MECH],
   ["Beta-1 receptor blockade", "Beta-1 receptor blockade is the class II mechanism of metoprolol; digoxin inhibits the sodium-potassium ATPase.", MECH]], 43),

Q("Digoxin", IO_MOA, "mechanism",
  "What does digoxin do to autonomic tone on the heart?",
  [["Raises parasympathetic, lowers sympathetic", "Correct. Digoxin indirectly increases parasympathetic tone and decreases sympathetic tone, slowing atrioventricular conduction."],
   ["Lowers parasympathetic, raises sympathetic", "This reverses both directions; digoxin indirectly raises parasympathetic tone and lowers sympathetic tone.", REV],
   ["Raises both parasympathetic and sympathetic", "Digoxin lowers sympathetic tone rather than raising it, while it indirectly raises parasympathetic tone.", REV],
   ["Lowers both parasympathetic and sympathetic", "Digoxin raises parasympathetic tone rather than lowering it, while it lowers sympathetic tone.", REV]], 43),

Q("Digoxin", IO_IND, "indication",
  "In atrial flutter or fibrillation, what is digoxin used to do?",
  [["Slow the ventricular rate", "Correct. Digoxin is listed to slow the ventricular rate, inducing a degree of heart block in atrial flutter and fibrillation."],
   ["Restore normal rhythm", "Normal rhythm in atrial fibrillation is dofetilide's listed indication; digoxin slows the ventricular rate.", MECH],
   ["Terminate torsades de pointes", "Torsades de pointes is treated with intravenous magnesium sulfate; digoxin slows the ventricular rate.", ADJ],
   ["Speed atrioventricular conduction", "Digoxin slows atrioventricular conduction and can induce heart block, which is how it slows the ventricular rate.", REV]], 44),

Q("Digoxin", IO_INTER, "interaction",
  "Which drugs are listed to avoid alongside digoxin?",
  [["Calcium blockers and beta blockers", "Correct. Calcium blockers and beta blockers are listed to avoid with digoxin; they add to its slowing of atrioventricular conduction."],
   ["Opioids such as codeine and morphine", "Codeine and morphine are the opioids affected by quinidine's cytochrome P450 2D6 inhibition; digoxin is to be avoided with calcium blockers and beta blockers.", ADJ],
   ["Anticoagulants such as warfarin", "Warfarin is a drug whose level amiodarone raises; digoxin is to be avoided with calcium blockers and beta blockers.", ADJ],
   ["Sodium channel blockers such as lidocaine", "Lidocaine is the intravenous class IB sodium channel blocker; digoxin is to be avoided with calcium blockers and beta blockers.", ADJ]], 44),

Q("Digoxin", IO_TOX, "adverse effect",
  "Which central nervous system effects are listed for digoxin toxicity?",
  [["Confusion and visual disturbances", "Correct. Digoxin's central nervous system toxicity includes confusion, delirium, headache, seizures and visual disturbances."],
   ["Neuropathy and ataxia", "Neuropathy, muscle weakness and ataxia belong to amiodarone; digoxin causes confusion and visual disturbances.", ADJ],
   ["Tinnitus and blurred vision", "Tinnitus, dizziness and blurred vision are quinidine's cinchonism; digoxin causes confusion and visual disturbances.", ADJ],
   ["Nystagmus and muscle twitches", "Nystagmus and muscle twitches belong to lidocaine's toxicity; digoxin causes confusion and visual disturbances.", ADJ]], 44),

Q("Digoxin", IO_TOX, "adverse effect",
  "Anorexia, nausea and vomiting with confusion and delirium point to toxicity from which drug?",
  [["Digoxin", "Correct. Digoxin toxicity lists nausea, vomiting, diarrhea and anorexia with confusion, delirium, headache, seizures and visual disturbances."],
   ["Quinidine", "Quinidine also causes nausea, vomiting and diarrhea, but its central effects are cinchonism (tinnitus, dizziness, blurred vision), not delirium.", RULED],
   ["Amiodarone", "Amiodarone's nervous system toxicity is neuropathy, muscle weakness and ataxia; the delirium picture is digoxin's.", RULED],
   ["Magnesium sulfate", "Magnesium sulfate's listed effects are bradycardia, flushing, headache and respiratory paralysis; the delirium picture is digoxin's.", RULED]], 44),

# ---- magnesium sulfate (slide 45) --------------------------------------------------------------------
Q("Magnesium sulfate", IO_IND, "indication",
  "Which agent is given intravenously for torsades de pointes?",
  [["Magnesium sulfate", "Correct. Intravenous magnesium sulfate is the listed treatment for torsades de pointes."],
   ["Dofetilide", "Dofetilide causes torsades de pointes (with marked QT prolongation) rather than treating it; magnesium sulfate treats it.", REV],
   ["Amiodarone", "Amiodarone prolongs repolarization as a class III drug; the listed treatment for torsades de pointes is magnesium sulfate.", REV],
   ["Procainamide", "Procainamide lists torsades de pointes among its adverse effects; the listed treatment for torsades is magnesium sulfate.", REV]], 45),

Q("Magnesium sulfate", IO_TOX, "adverse effect",
  "Which serious toxicity is listed for magnesium sulfate?",
  [["Respiratory paralysis", "Correct. Magnesium sulfate's listed toxicities are bradycardia, flushing, headache and respiratory paralysis."],
   ["Pulmonary fibrosis", "Pulmonary fibrosis (potentially fatal) is amiodarone's lung toxicity; magnesium sulfate can cause respiratory paralysis.", ADJ],
   ["Bronchospasm", "Bronchospasm is listed for propranolol, sotalol and the class IC drugs; magnesium sulfate can cause respiratory paralysis.", ADJ],
   ["Pneumonitis", "Pneumonitis is amiodarone's lung toxicity; magnesium sulfate can cause respiratory paralysis.", ADJ]], 45),

Q("Magnesium sulfate", IO_AE, "adverse effect",
  "Which heart rate effect is listed for magnesium sulfate?",
  [["Bradycardia", "Correct. Bradycardia is on magnesium sulfate's toxicity list, with flushing, headache and respiratory paralysis."],
   ["Tachycardia", "Magnesium sulfate slows rather than speeds the heart; bradycardia is on its toxicity list.", REV],
   ["Torsades de pointes", "Torsades de pointes is what magnesium sulfate treats, not a toxicity of it; bradycardia is on its list.", REV],
   ["Faster conduction", "Increased atrioventricular conduction is listed for lidocaine; magnesium sulfate's heart rate effect is bradycardia.", ADJ]], 45),
]
