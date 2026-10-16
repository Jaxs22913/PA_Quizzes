# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Antiarrhythmic Drugs (Lecture 10), topic: principles, the four classes, class IA.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. The key is authored FIRST (c == 0);
pharm_e3_partition.py rotates it (numeric option sets are sorted ascending instead, WRITER.md rule 8).

SOURCE. Antiarrhythmics.pptx slides 3-15: principles of therapy (3), classification by mechanism (4) and by class (5),
indications by class (6), the sodium channel (7, picture), class IA actions (8, picture), quinidine (9-11),
procainamide (12-13), disopyramide (14-15). Picture slides were read by eye into tools/pharm_e3/ocr.json.

WRITER.md v1 (2026-10-15): every distractor carries its misconception as a third element (mis); slides only (this deck
has no speaker notes); slides win on conflict.

LEFT OUT ON PURPOSE:
  * channel affinity (open > inactivated) and dissociation rate: the lecturer said he will not test them;
  * every dose, and every bare percentage as a key (percentages appear only inside a stem or an explanation);
  * "Anticoagulants and Digitalis" under quinidine conversion (slide 10): the slide does not say what they are for;
  * the QRS / QT wording for class IA (spoken, not on these slides); rate versus rhythm control as a key (spoken).
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

# ---- principles of therapy (slide 3) -------------------------------------------------------------
Q("Principles of therapy", IO_PROT, "protocol",
  "A patient has a new arrhythmia along with hypoxia and an electrolyte disturbance. Which step comes first in the principles of antiarrhythmic therapy?",
  [["Correct the precipitating factors", "Correct. The first principle is to identify and remove precipitating factors such as hypoxia, ischemia and electrolyte disturbances before the goal of drug therapy is set."],
   ["Start a class III drug to prevent recurrence", "Prevention of arrhythmia is a goal set only after precipitating factors are removed; hypoxia and an electrolyte disturbance are the first things to correct here.", STAGE],
   ["Start a beta blocker to control the rate", "A beta blocker may come later, but the first principle of therapy is to identify and remove precipitating factors such as hypoxia and electrolytes.", STAGE],
   ["Start a class IA drug to restore rhythm", "Terminating the arrhythmia is a goal chosen after the precipitating factors (hypoxia, ischemia, electrolytes) are identified and removed.", STAGE]], 3),

Q("Principles of therapy", IO_AE, "adverse effect",
  "Which risk is shared by every antiarrhythmic drug?",
  [["They may induce arrhythmias", "Correct. Minimizing risk is a principle of therapy because all antiarrhythmics may induce arrhythmias, so the mechanism has to be understood before one is chosen."],
   ["They prolong the action potential", "Not every class does: class IB shortens phase 3 and the action potential. The risk shared by all antiarrhythmics is that they may induce arrhythmias.", MECH],
   ["They cause bronchospasm", "Bronchospasm is listed for propranolol, sotalol, flecainide and propafenone, not for every antiarrhythmic; the shared risk is that any of them may induce arrhythmias.", ADJ],
   ["They decrease contractility", "Negative inotropy is listed for disopyramide, beta blockers and class IV drugs, not for all; what every antiarrhythmic shares is the risk of inducing arrhythmias.", ADJ]], 3),

# ---- classification (slides 4 and 5) -------------------------------------------------------------
Q("Classification", IO_MOA, "mechanism",
  "Increasing the energy required for fibrillation is attributed to which antiarrhythmic mechanism?",
  [["Beta receptor blockade", "Correct. Beta receptor blockade prolongs atrioventricular refractoriness, prolongs conduction and increases the energy required for fibrillation."],
   ["Sodium channel blockade", "Sodium channel blockers act by decreasing excitability; raising the energy needed for fibrillation is the effect attributed to beta receptor blockade.", MECH],
   ["Potassium channel blockade", "Blocking potassium channels prolongs the action potential; the increased energy required for fibrillation is attributed to beta receptor blockade.", MECH],
   ["Calcium channel blockade", "Calcium channel blockers decrease the excitability of slow-response cells; increasing the fibrillation energy is attributed to beta receptor blockade.", MECH]], 4),

Q("Classification", IO_MOA, "mechanism",
  "Class IA, IB and IC antiarrhythmics all act on which target?",
  [["Sodium channels", "Correct. Class 1 drugs are the sodium channel blockers; the subclasses A, B and C differ in how they affect the channel and the action potential."],
   ["Potassium channels", "Potassium channels are the target of class III, which prolongs repolarization; all three class I subgroups are sodium channel blockers.", MECH],
   ["Calcium channels", "Calcium channels are blocked by class IV drugs (verapamil, diltiazem); classes IA, IB and IC are all sodium channel blockers.", MECH],
   ["Beta receptors", "Beta receptors are blocked by class II drugs; classes IA, IB and IC all block sodium channels.", MECH]], 5),

Q("Classification", IO_CLASS, "class",
  "Which antiarrhythmic class prolongs repolarization by acting on potassium?",
  [["Class III", "Correct. Class 3 drugs prolong repolarization by acting on potassium (they reduce potassium efflux), which lengthens the action potential."],
   ["Class I", "Class I drugs are sodium channel blockers (subgroups IA, IB and IC); prolonging repolarization through potassium is class III.", MECH],
   ["Class II", "Class II drugs are beta receptor antagonists; the class that prolongs repolarization through potassium is class III.", MECH],
   ["Class IV", "Class IV drugs are calcium channel blockers such as verapamil and diltiazem; prolonging repolarization through potassium is class III.", MECH]], 5),

Q("Classification", IO_CLASS, "class",
  "Which three drugs make up class IA?",
  [["Quinidine, procainamide, disopyramide", "Correct. The class IA drugs are quinidine, procainamide and disopyramide (remembered as PDQ)."],
   ["Quinidine, lidocaine, flecainide", "Lidocaine is the class IB drug and flecainide is class IC; the class IA group is quinidine, procainamide and disopyramide.", MECH],
   ["Procainamide, propafenone, sotalol", "Propafenone is class IC and sotalol is a beta blocker with class III action; class IA is quinidine, procainamide and disopyramide.", MECH],
   ["Disopyramide, diltiazem, dofetilide", "Diltiazem is class IV and dofetilide is class III; the class IA drugs are quinidine, procainamide and disopyramide.", MECH]], 5),

Q("Classification", IO_CLASS, "class",
  "Which antiarrhythmic class does disopyramide belong to?",
  [["Class IA", "Correct. Disopyramide is a class IA sodium channel blocker with effects similar to quinidine, more anticholinergic action and a negative inotropic effect."],
   ["Class IB", "Class IB contains lidocaine, which works mainly in ischemic tissue; disopyramide is class IA, alongside quinidine and procainamide.", MECH],
   ["Class IC", "Class IC contains flecainide and propafenone; disopyramide is class IA, a group whose effects resemble quinidine.", MECH],
   ["Class III", "Class III contains the potassium channel blockers amiodarone, dofetilide and sotalol; disopyramide is a class IA sodium channel blocker.", MECH]], 14),

# ---- indications by class (slide 6) ---------------------------------------------------------------
Q("Indications by class", IO_IND, "indication",
  "Which antiarrhythmic class has only ventricular arrhythmias among its listed indications?",
  [["Class IB", "Correct. Class IB is listed for ventricular tachycardia, ventricular fibrillation prevention and symptomatic ventricular beats, all ventricular."],
   ["Class IA", "Class IA also covers supraventricular tachycardia, alongside ventricular tachycardia and the prevention of ventricular fibrillation and premature ventricular contractions.", ADJ],
   ["Class III", "Class III covers refractory ventricular tachycardia but also atrial fibrillation, flutter and supraventricular tachycardia.", ADJ],
   ["Class IV", "Class IV is listed for supraventricular tachycardia, the opposite end; the class whose list is entirely ventricular is class IB.", REV]], 6),

Q("Indications by class", IO_IND, "indication",
  "Which antiarrhythmic class is listed for supraventricular tachycardia alone?",
  [["Class IV", "Correct. Class IV (verapamil, diltiazem) is listed for supraventricular tachycardia, and verapamil and diltiazem are to be avoided in ventricular arrhythmias."],
   ["Class IB", "Class IB is listed only for ventricular arrhythmias (ventricular tachycardia, fibrillation prevention, symptomatic ventricular beats), the opposite of class IV.", REV],
   ["Class III", "Class III covers both sides: refractory ventricular tachycardia as well as atrial fibrillation, flutter and supraventricular tachycardia.", ADJ],
   ["Class IA", "Class IA covers both sides: supraventricular tachycardia plus ventricular tachycardia and prevention of ventricular fibrillation and premature contractions.", ADJ]], 6),

Q("Indications by class", IO_IND, "indication",
  "Which antiarrhythmic class is listed for life-threatening ventricular tachycardia or fibrillation and for refractory supraventricular tachycardia?",
  [["Class IC", "Correct. Class IC (flecainide, propafenone) is reserved for life-threatening ventricular tachycardia or fibrillation and refractory supraventricular tachycardia."],
   ["Class IB", "Class IB is listed for ventricular arrhythmias only (ventricular tachycardia, fibrillation prevention, symptomatic ventricular beats), with no supraventricular use.", ADJ],
   ["Class IV", "Class IV is listed for supraventricular tachycardia only and is avoided in ventricular arrhythmias, so it cannot treat ventricular fibrillation.", RULED],
   ["Class II", "Class II is listed for supraventricular tachycardia and fibrillation; the class reserved for life-threatening ventricular arrhythmias and refractory supraventricular tachycardia is class IC.", ADJ]], 6),

Q("Indications by class", IO_IND, "indication",
  "Which antiarrhythmic class is listed for refractory ventricular tachycardia as well as atrial fibrillation and flutter?",
  [["Class III", "Correct. Class III is listed for refractory ventricular tachycardia, atrial fibrillation, flutter and supraventricular tachycardia, so it covers both sides."],
   ["Class IB", "Class IB is listed only for ventricular arrhythmias; it has no atrial fibrillation or flutter indication.", ADJ],
   ["Class IV", "Class IV is listed only for supraventricular tachycardia and is avoided in ventricular arrhythmias.", RULED],
   ["Class II", "Class II is listed for supraventricular tachycardia and fibrillation, not for refractory ventricular tachycardia; that combination belongs to class III.", ADJ]], 6),

# ---- the sodium channel (slide 7, picture) -------------------------------------------------------
Q("Sodium channel states", IO_MOA, "physiology",
  "In which state of the cardiac sodium channel does sodium flow into the cell?",
  [["Activated", "Correct. When an action potential arrives the channel is activated: it opens, sodium flows in, and the membrane potential shoots up in phase 0."],
   ["Resting", "In the resting state the channel is closed and sodium cannot enter; it is the activated (open) state that lets sodium in.", REV],
   ["Inactivated", "In the inactivated state a gate plugs the channel, so no sodium enters while the cell repolarizes; sodium flows in the activated state.", ADJ],
   ["Recovering", "Recovery is the return from inactivated to resting, with the channel still closed to sodium; sodium enters only in the activated state.", ADJ]], 7),

# ---- class IA actions (slide 8, picture) ----------------------------------------------------------
Q("Class IA actions", IO_MOA, "mechanism",
  "Which electrical change in working heart cells defines class IA drugs?",
  [["Slow phase 0 and prolong the action potential", "Correct. Class IA drugs slow phase 0, slow conduction and prolong the action potential: the drug tracing rises more slowly and ends later."],
   ["Shorten phase 3 mainly in ischemic tissue", "Shortening phase 3, with the greatest effect in ischemic tissue, describes class IB (lidocaine), not class IA.", MECH],
   ["Prolong phase 3 with phase 0 unchanged", "A longer phase 3 with an unchanged upstroke is the class III picture; class IA also slows phase 0.", MECH],
   ["Decrease phase 4 in nodal pacemaker cells", "Flattening phase 4 in slow-response pacemaker cells is what class II and class IV drugs do; class IA acts on phase 0.", MECH]], 8),

# ---- quinidine (slides 9-11) --------------------------------------------------------------------
Q("Quinidine", IO_CLASS, "class",
  "Quinidine is an isomer of which compound?",
  [["Quinine", "Correct. Quinidine is the D-isomer of quinine, which links it to cinchonism (tinnitus, dizziness, blurred vision)."],
   ["Procaine", "Procaine is the parent of procainamide, an amide derivative; quinidine is the D-isomer of quinine.", ADJ],
   ["Lidocaine", "Lidocaine is the class IB drug and is not related to quinidine's structure; quinidine is the D-isomer of quinine.", MECH],
   ["Digitalis", "Digitalis (digoxin) is a miscellaneous antiarrhythmic acting on the sodium-potassium pump; quinidine is the D-isomer of quinine.", MECH]], 9),

Q("Quinidine", IO_MOA, "mechanism",
  "Which indirect action does quinidine have at higher doses?",
  [["Alpha blockade", "Correct. Quinidine's indirect actions are anticholinergic effects and, at higher doses, alpha blockade, which helps explain its hypotension."],
   ["Beta blockade", "Beta-blocking activity belongs to propafenone and sotalol, not quinidine; quinidine's higher-dose indirect action is alpha blockade.", MECH],
   ["Calcium channel blockade", "Calcium channel blockade is class IV, and amiodarone also blocks calcium channels; quinidine's higher-dose indirect action is alpha blockade.", MECH],
   ["Potassium channel activation", "Activating atrial potassium channels is how adenosine works; quinidine's indirect actions are anticholinergic effects and alpha blockade.", MECH]], 9),

Q("Quinidine", IO_MOA, "mechanism",
  "Which direct action belongs to quinidine?",
  [["It prolongs the refractory period", "Correct. Quinidine slows conduction, prolongs the refractory period, slows the rise of phase 0, increases the excitability threshold and decreases automaticity."],
   ["It shortens phase 3", "Shortening phase 3 is the class IB (lidocaine) action; quinidine prolongs the refractory period.", MECH],
   ["It increases automaticity", "Quinidine decreases automaticity, the reverse of this option; among its direct actions it also prolongs the refractory period.", REV],
   ["It lowers the excitability threshold", "Quinidine increases the threshold for excitability, the reverse of this option, and prolongs the refractory period.", REV]], 9),

Q("Quinidine", IO_AE, "adverse effect",
  "Which adverse effect of quinidine follows from its alpha-blocking action at higher doses?",
  [["Hypotension", "Correct. Blocking alpha receptors at higher doses relaxes blood vessels, and hypotension is on quinidine's toxicity list."],
   ["Thrombocytopenia", "Thrombocytopenia (which may be fatal) is on quinidine's list but is not explained by alpha blockade; hypotension is.", ADJ],
   ["Cinchonism", "Cinchonism (tinnitus, dizziness, blurred vision) comes from quinidine's link to quinine, not alpha blockade, which explains hypotension.", MECH],
   ["Diarrhea", "Diarrhea, with nausea and vomiting, is quinidine's commonest effect but is not due to alpha blockade; hypotension is.", ADJ]], 11),

Q("Quinidine", IO_IND, "indication",
  "Which is a listed indication for quinidine?",
  [["Maintaining rhythm in atrial fibrillation", "Correct. Quinidine is listed to maintain rhythm with atrial flutter or fibrillation and to control ventricular tachycardia; its use for conversion is very limited."],
   ["Slowing the ventricular rate in atrial fibrillation", "Slowing the ventricular rate is digoxin's listed indication; quinidine is used to maintain rhythm with atrial flutter or fibrillation.", MECH],
   ["Terminating torsades de pointes", "Torsades de pointes is treated with intravenous magnesium sulfate; quinidine itself causes torsades in 2 to 8 percent of patients.", REV],
   ["Ending paroxysmal supraventricular tachycardia", "Paroxysmal supraventricular tachycardia is adenosine's listed indication; quinidine is used to maintain rhythm in atrial flutter or fibrillation.", ADJ]], 10),

Q("Quinidine", IO_INTER, "interaction",
  "Which drug interaction is listed for quinidine?",
  [["Inhibits cytochrome P450 2D6 (codeine)", "Correct. Quinidine is a cytochrome P450 2D6 (CYP2D6) inhibitor, and codeine and morphine are the named examples affected."],
   ["Raising digoxin, warfarin and phenytoin", "Raising digoxin, warfarin, flecainide, phenytoin and procainamide is amiodarone's listed interaction; quinidine's is CYP2D6 inhibition.", ADJ],
   ["Adding to heart block with beta blockers", "Avoiding beta blockers and calcium channel blockers because of added heart block is digoxin's listed caution; quinidine's interaction is CYP2D6 inhibition.", ADJ],
   ["Adding to digitalis toxicity", "Digitalis toxicity is on propranolol's toxicity list; quinidine's listed interaction is cytochrome P450 2D6 inhibition (codeine, morphine).", ADJ]], 10),

Q("Quinidine", IO_TOX, "adverse effect",
  "Which adverse effect of quinidine occurs in 30 to 50 percent of patients?",
  [["Gastrointestinal upset", "Correct. Gastrointestinal upset (nausea, vomiting, diarrhea) is listed in 30 to 50 percent, quinidine's most frequent toxicity."],
   ["Torsades de pointes", "Torsades de pointes occurs with quinidine but in 2 to 8 percent, far less often than the gastrointestinal effects.", REV],
   ["Thrombocytopenia", "Thrombocytopenia is listed (and may be fatal) without a frequency; the effect in 30 to 50 percent is nausea, vomiting and diarrhea.", ADJ],
   ["Cinchonism", "Cinchonism (tinnitus, dizziness, blurred vision) is listed without a frequency; the 30 to 50 percent effect is nausea, vomiting and diarrhea.", ADJ]], 11),

Q("Quinidine", IO_TOX, "adverse effect",
  "A patient taking quinidine reports tinnitus, dizziness and blurred vision. Which named effect is this?",
  [["Cinchonism", "Correct. Cinchonism is tinnitus, dizziness and blurred vision, on quinidine's toxicity list; quinidine is the D-isomer of quinine."],
   ["Lupus-like syndrome", "A lupus-like syndrome is procainamide's effect, more often in slow acetylators; tinnitus, dizziness and blurred vision are cinchonism.", ADJ],
   ["Torsades de pointes", "Torsades de pointes is a ventricular arrhythmia on quinidine's list, not this triad; tinnitus, dizziness and blurred vision are cinchonism.", COMP],
   ["Thrombocytopenia", "Thrombocytopenia is a fall in platelets on quinidine's list, not this triad; tinnitus, dizziness and blurred vision are cinchonism.", COMP]], 11),

Q("Quinidine", IO_TOX, "adverse effect",
  "Which blood disorder on quinidine's toxicity list may be fatal?",
  [["Thrombocytopenia", "Correct. Quinidine's toxicity list includes thrombocytopenia, marked as potentially fatal."],
   ["Agranulocytosis", "Agranulocytosis is listed for propafenone, with anemia and thrombocytopenia; quinidine's potentially fatal blood effect is thrombocytopenia.", ADJ],
   ["Bone marrow suppression", "Bone marrow suppression (0.2 percent) is listed for procainamide; quinidine's potentially fatal blood effect is thrombocytopenia.", ADJ],
   ["Megaloblastic anemia", "Megaloblastic anemia belongs to triamterene, a potassium-sparing diuretic; quinidine's potentially fatal blood effect is thrombocytopenia.", ADJ]], 11),

Q("Quinidine", IO_TOX, "adverse effect",
  "Which arrhythmia occurs in 2 to 8 percent of patients taking quinidine?",
  [["Torsades de pointes", "Correct. Torsades de pointes is listed in 2 to 8 percent of patients on quinidine, alongside quinidine sudden death."],
   ["Paroxysmal supraventricular tachycardia", "Supraventricular tachycardia is something class IA drugs treat, not a toxicity with a stated rate; quinidine causes torsades de pointes in 2 to 8 percent.", REV],
   ["Complete heart block", "Heart block is a contraindication to disopyramide and a toxicity of propranolol; quinidine's 2 to 8 percent arrhythmia is torsades de pointes.", ADJ],
   ["Sinus bradycardia", "Bradycardia is listed for propafenone and magnesium sulfate, not quinidine; the arrhythmia seen in 2 to 8 percent on quinidine is torsades de pointes.", ADJ]], 11),

# ---- procainamide (slides 12-13) -----------------------------------------------------------------
Q("Procainamide", IO_ADME, "class",
  "Procainamide's acetylated metabolite, N-acetylprocainamide (NAPA), adds activity of which class?",
  [["Class III", "Correct. The active acetylated metabolite has class III activity, so procainamide carries a blend of class IA and class III action."],
   ["Class I", "Class I sodium channel blockade is procainamide's own action; the acetylated metabolite adds class III activity.", ADJ],
   ["Class II", "Class II is beta blockade, which belongs to propafenone and sotalol among these drugs; the metabolite of procainamide adds class III activity.", MECH],
   ["Class IV", "Class IV is calcium channel blockade (verapamil, diltiazem); procainamide's acetylated metabolite adds class III activity.", MECH]], 12),

Q("Procainamide", IO_ADME, "monitoring",
  "Why is procainamide made as a slow-release preparation?",
  [["Its action lasts only 3 to 4 hours", "Correct. Procainamide has a short duration of action (3 to 4 hours), so a slow-release preparation is used."],
   ["It undergoes extensive first-pass metabolism", "Extensive first-pass metabolism is why lidocaine must be given intravenously; procainamide's problem is a short duration of action.", ADJ],
   ["Its half-life is about 40 days", "A 40-day half-life is amiodarone's, and it calls for loading doses; procainamide acts for only 3 to 4 hours.", REV],
   ["It is eliminated unchanged by the kidneys", "Elimination unchanged by the kidneys is listed for dofetilide; procainamide needs slow release because its action lasts 3 to 4 hours.", ADJ]], 12),

Q("Procainamide", IO_TOX, "adverse effect",
  "Which adverse effect of procainamide occurs in 25 to 50 percent of patients?",
  [["Lupus-like syndrome", "Correct. A lupus-like syndrome develops in 25 to 50 percent of patients, more often in slow acetylators."],
   ["Bone marrow suppression", "Bone marrow suppression is listed for procainamide but in only 0.2 percent; the effect in 25 to 50 percent is the lupus-like syndrome.", REV],
   ["Cinchonism", "Cinchonism (tinnitus, dizziness, blurred vision) belongs to quinidine; procainamide's common effect is a lupus-like syndrome.", ADJ],
   ["Torsades de pointes", "Torsades de pointes is on procainamide's list without a frequency; the effect seen in 25 to 50 percent is a lupus-like syndrome.", ADJ]], 13),

Q("Procainamide", IO_EDU, "education",
  "Which patients taking procainamide are more likely to develop a lupus-like syndrome?",
  [["Slow acetylators", "Correct. The lupus-like syndrome (25 to 50 percent) is more often seen in slow acetylators."],
   ["Fast acetylators", "Fast acetylators may increase the active metabolite; the lupus-like syndrome is more common in slow acetylators.", REV],
   ["Patients given it intravenously", "Intravenous procainamide is better tolerated than quinidine; the lupus-like syndrome is linked to slow acetylation, not the route.", ADJ],
   ["Patients with glaucoma", "Glaucoma is a contraindication to disopyramide because of its anticholinergic action; slow acetylators are the ones prone to the lupus-like syndrome.", ADJ]], 13),

Q("Procainamide", IO_MOA, "mechanism",
  "Compared with quinidine, how does procainamide differ?",
  [["Less anticholinergic, no alpha block", "Correct. Procainamide has less anticholinergic activity than quinidine and no alpha-blocking activity."],
   ["More anticholinergic, negative inotrope", "More anticholinergic action with a negative inotropic effect describes disopyramide, not procainamide.", MECH],
   ["Greater affinity for ischemic tissue", "Higher affinity in ischemic tissue describes the class IB drug lidocaine; procainamide has less anticholinergic action and no alpha block.", MECH],
   ["Added beta-blocking activity", "Beta-blocking activity is added in propafenone and sotalol; procainamide's difference from quinidine is less anticholinergic action and no alpha block.", MECH]], 12),

Q("Procainamide", IO_TOX, "adverse effect",
  "Besides a lupus-like syndrome, which serious effect is listed for procainamide?",
  [["Bone marrow suppression", "Correct. Procainamide's adverse effects include bone marrow suppression (0.2 percent), along with hypotension, slowed conduction, nausea and torsades de pointes."],
   ["Cinchonism", "Cinchonism (tinnitus, dizziness, blurred vision) is quinidine's; procainamide's listed serious effects include bone marrow suppression.", ADJ],
   ["Pulmonary fibrosis", "Pneumonitis and pulmonary fibrosis belong to amiodarone; procainamide's list includes bone marrow suppression.", ADJ],
   ["Nystagmus", "Nystagmus is the early sign of lidocaine toxicity; procainamide's list includes bone marrow suppression.", ADJ]], 13),

# ---- disopyramide (slides 14-15) -----------------------------------------------------------------
Q("Disopyramide", IO_CONTRA, "contraindication",
  "Which eye condition contraindicates disopyramide?",
  [["Glaucoma", "Correct. Disopyramide is contraindicated in heart block, hypersensitivity and glaucoma; its strong anticholinergic action explains the glaucoma contraindication."],
   ["Corneal deposits", "Corneal deposits are an adverse effect of amiodarone, not a contraindication to disopyramide; glaucoma is.", ADJ],
   ["Nystagmus", "Nystagmus is the early sign of lidocaine toxicity; the eye condition that contraindicates disopyramide is glaucoma.", ADJ],
   ["Blurred vision from cinchonism", "Blurred vision with tinnitus and dizziness is quinidine's cinchonism; disopyramide's listed eye contraindication is glaucoma.", ADJ]], 15),

Q("Disopyramide", IO_CONTRA, "contraindication",
  "Which cardiac condition is a listed contraindication to disopyramide?",
  [["Heart block", "Correct. Heart block, hypersensitivity and glaucoma are the listed contraindications; disopyramide itself causes conduction disturbances."],
   ["Ventricular tachycardia", "Ventricular tachycardia is an indication for disopyramide, not a contraindication; heart block is contraindicated.", REV],
   ["Atrial flutter", "Supraventricular arrhythmias such as flutter and fibrillation are indications for disopyramide; heart block is the cardiac contraindication.", REV],
   ["Atrial fibrillation", "Atrial fibrillation is among disopyramide's supraventricular indications; the listed cardiac contraindication is heart block.", REV]], 15),

Q("Disopyramide", IO_AE, "adverse effect",
  "Why can disopyramide cause congestive heart failure?",
  [["It has a negative inotropic effect", "Correct. Disopyramide has negative inotropic effects, and its toxicity list gives congestive heart failure from decreased contractility."],
   ["It is strongly anticholinergic", "Disopyramide is more anticholinergic than quinidine, which explains its antimuscarinic effects and the glaucoma contraindication, not heart failure.", ADJ],
   ["It blocks alpha receptors", "Alpha blockade at higher doses is quinidine's indirect action and explains hypotension; disopyramide's heart failure comes from decreased contractility.", MECH],
   ["It blocks potassium channels", "Potassium channel blockade is the class III mechanism; disopyramide's heart failure comes from its negative inotropic effect.", MECH]], 15),

Q("Disopyramide", IO_CLASS, "class",
  "Which class IA drug has the strongest anticholinergic action?",
  [["Disopyramide", "Correct. Disopyramide's effects are similar to quinidine but with more anticholinergic action, plus a negative inotropic effect."],
   ["Quinidine", "Quinidine is anticholinergic, but disopyramide has more anticholinergic action than quinidine.", STAGE],
   ["Procainamide", "Procainamide has less anticholinergic activity than quinidine, so it is the weakest of the three, not the strongest.", REV],
   ["Lidocaine", "Lidocaine is class IB, not IA; among the class IA drugs disopyramide has the most anticholinergic action.", MECH]], 14),
]
