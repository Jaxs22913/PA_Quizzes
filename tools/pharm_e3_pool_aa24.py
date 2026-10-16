# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Antiarrhythmic Drugs (Lecture 10), topic: class II (beta blockers) and class IV (verapamil,
diltiazem): the two classes that act on the slow-response cells of the nodes.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. Key authored FIRST (c == 0).

SOURCE. Antiarrhythmics.pptx slides 25-29 (class II actions with the pacemaker-cell picture, propranolol, metoprolol,
acebutolol, esmolol) and 37-39 (class IV actions, the same picture, verapamil and diltiazem). Slide 5 for the class name.

LEFT OUT ON PURPOSE:
  * propranolol and blood glucose: slide 28 lists hyperglycemia, the lecturer spoke of hypoglycemia and masked
    hypoglycemia without calling the slide wrong; no key or distractor turns on the direction;
  * "class II is for supraventricular arrhythmias only": propranolol's own slide also lists ventricular ectopic beats,
    so only the class IV "avoid in ventricular arrhythmias" line is keyed;
  * propranolol's "Heart failure, Digitalis toxicity" line on slide 28: its meaning (toxicity, caution or interaction) is unclear
    and was not explained in the recording;
  * the lecturer's spoken asides (cytochrome P450 3A4 for class IV, the bouncer image, rate versus rhythm wording).
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

# ---- class II actions (slide 25, picture) -------------------------------------------------------------
Q("Class II actions", IO_CLASS, "class",
  "Which antiarrhythmic class is made up of the beta receptor antagonists?",
  [["Class II", "Correct. Class 2 antiarrhythmics are the beta receptor antagonists, such as propranolol, metoprolol, acebutolol and esmolol."],
   ["Class I", "Class I drugs are the sodium channel blockers (IA, IB, IC); the beta receptor antagonists are class II.", MECH],
   ["Class III", "Class III drugs prolong repolarization through potassium; the beta receptor antagonists are class II.", MECH],
   ["Class IV", "Class IV drugs are the calcium channel blockers verapamil and diltiazem; the beta receptor antagonists are class II.", MECH]], 5),

Q("Class II actions", IO_MOA, "mechanism",
  "Class II antiarrhythmics slow the heart mainly by which effect on pacemaker cells?",
  [["Decreasing phase 4 depolarization", "Correct. Class II drugs decrease phase 4 depolarization, so pacemaker cells reach threshold later; they also slow conduction and prolong atrioventricular conduction."],
   ["Slowing the phase 0 sodium upstroke", "Slowing the phase 0 upstroke is the class I sodium channel blocker effect; class II flattens phase 4 in pacemaker cells.", MECH],
   ["Prolonging phase 3 repolarization", "Prolonging phase 3 is the class III potassium channel blocker effect; class II decreases phase 4 depolarization.", MECH],
   ["Shortening phase 3 repolarization", "Shortening phase 3 is the class IB (lidocaine) effect; class II decreases phase 4 depolarization.", MECH]], 25),

Q("Class IV actions", IO_MOA, "mechanism",
  "Besides slowing atrioventricular node conduction, what do class IV calcium channel blockers do to automaticity?",
  [["They decrease it", "Correct. Class IV drugs decrease automaticity, block the L-type channel, slow atrioventricular node conduction and are negative inotropes."],
   ["They increase it", "Class IV drugs lower automaticity rather than raising it, along with slowing atrioventricular node conduction.", REV],
   ["They leave it unchanged", "Decreased automaticity is a listed class IV action, alongside slowed atrioventricular node conduction.", REV],
   ["They raise it in ischemic tissue", "Acting mainly in ischemic tissue is the class IB (lidocaine) feature, and it lowers ectopic automaticity there; class IV drugs decrease automaticity.", MECH]], 37),

# ---- propranolol (slides 26-28) ----------------------------------------------------------------------
Q("Propranolol", IO_CLASS, "class",
  "Which of these beta blockers is nonselective?",
  [["Propranolol", "Correct. Propranolol is a nonselective beta blocker, which is why it carries the bronchospasm risk."],
   ["Metoprolol", "Metoprolol is a beta-1 selective blocker with less bronchospasm; propranolol is the nonselective one.", MECH],
   ["Acebutolol", "Acebutolol is a beta-1 selective blocker like metoprolol; propranolol is the nonselective one.", MECH],
   ["Esmolol", "Esmolol is the intravenous, short-acting beta blocker; the nonselective beta blocker here is propranolol.", ADJ]], 26),

Q("Propranolol", IO_MOA, "mechanism",
  "Which effects does propranolol have on the heart?",
  [["Negative inotropic and chronotropic", "Correct. Propranolol has negative inotropic and chronotropic effects, slows atrioventricular conduction and reduces phase 4 activation."],
   ["Positive inotropic, negative chronotropic", "Propranolol lowers contractility as well as rate; both its inotropic and chronotropic effects are negative.", REV],
   ["Negative inotropic, positive chronotropic", "Propranolol slows the heart rate as well as lowering contractility; both effects are negative.", REV],
   ["Positive inotropic and chronotropic", "Both of propranolol's effects are negative: it lowers contractility and slows the rate.", REV]], 26),

Q("Propranolol", IO_IND, "indication",
  "Which arrhythmias are a listed indication for propranolol?",
  [["Supraventricular arrhythmias", "Correct. Propranolol is listed for supraventricular arrhythmias, ventricular ectopic beats and myocardial infarction."],
   ["Torsades de pointes", "Torsades de pointes is treated with intravenous magnesium sulfate; propranolol is listed for supraventricular arrhythmias.", ADJ],
   ["Refractory ventricular tachycardia", "Recurrent ventricular tachycardia resistant to other drugs is an amiodarone (class III) indication; propranolol is listed for supraventricular arrhythmias.", ADJ],
   ["Sustained ventricular arrhythmias", "Life-threatening sustained ventricular arrhythmias are a flecainide (class IC) indication; propranolol is listed for supraventricular arrhythmias.", ADJ]], 27),

Q("Propranolol", IO_IND, "indication",
  "Besides arrhythmias, which cardiac condition is a listed indication for propranolol?",
  [["Myocardial infarction", "Correct. Propranolol's indications are supraventricular arrhythmias, ventricular ectopic beats and myocardial infarction."],
   ["Heart failure", "Heart failure is on propranolol's toxicity list (it is a negative inotrope), not its indication list.", REV],
   ["Heart block", "Heart block is a toxicity of propranolol, from slowed atrioventricular conduction, not an indication.", REV],
   ["Sick sinus syndrome", "Sick sinus syndrome is a reason to avoid verapamil and diltiazem; propranolol's listed cardiac indication is myocardial infarction.", ADJ]], 27),

Q("Propranolol", IO_AE, "adverse effect",
  "Why is propranolol a concern in a patient with asthma?",
  [["It can cause bronchospasm", "Correct. Propranolol is nonselective, and bronchospasm is on its toxicity list; a beta-1 selective blocker causes less."],
   ["It can cause pneumonitis", "Pneumonitis, with pulmonary fibrosis, is amiodarone's lung toxicity; propranolol's concern in asthma is bronchospasm.", ADJ],
   ["It can cause respiratory paralysis", "Respiratory paralysis is listed for magnesium sulfate; propranolol's concern in asthma is bronchospasm.", ADJ],
   ["It can cause pulmonary fibrosis", "Pulmonary fibrosis (potentially fatal) belongs to amiodarone; propranolol's concern in asthma is bronchospasm.", ADJ]], 28),

Q("Propranolol", IO_TOX, "adverse effect",
  "Which conduction disorder is a listed toxicity of propranolol?",
  [["Heart block", "Correct. Propranolol slows atrioventricular conduction, and heart block is on its toxicity list with heart failure and hypotension."],
   ["Sinus tachycardia", "Propranolol has a negative chronotropic effect, so it slows rather than speeds the rate; its listed conduction toxicity is heart block.", REV],
   ["QT prolongation", "Marked QT prolongation is listed for dofetilide, a potassium channel blocker; the conduction toxicity listed for propranolol is heart block.", ADJ],
   ["Torsades de pointes", "Torsades de pointes belongs to class IA, dofetilide and sotalol; propranolol's listed conduction toxicity is heart block.", ADJ]], 28),


# ---- metoprolol, acebutolol, esmolol (slide 29) ----------------------------------------------------------
Q("Beta-1 selective blockers", IO_CLASS, "class",
  "Metoprolol and acebutolol are which type of beta blocker?",
  [["Beta-1 selective", "Correct. Metoprolol and acebutolol are beta-1 selective blockers, similar to propranolol but with less bronchospasm."],
   ["Nonselective", "Nonselective describes propranolol, which carries more bronchospasm; metoprolol and acebutolol are beta-1 selective.", MECH],
   ["Beta blockers that block potassium channels", "A beta blocker that also inhibits potassium channels is sotalol (class II plus class III); metoprolol and acebutolol are beta-1 selective.", MECH],
   ["Beta blockers that block sodium channels", "Sodium channel block with beta-blocking activity describes propafenone (class IC); metoprolol and acebutolol are beta-1 selective.", MECH]], 29),

Q("Beta-1 selective blockers", IO_IND, "drug choice",
  "A patient with asthma needs a beta blocker for a supraventricular arrhythmia. Which is preferred?",
  [["Metoprolol", "Correct. Metoprolol is beta-1 selective and causes less bronchospasm than propranolol, which matters in asthma."],
   ["Propranolol", "Propranolol is nonselective and bronchospasm is on its toxicity list, so it is the one to avoid in asthma.", RULED],
   ["Sotalol", "Sotalol has beta-blocking activity with bronchospasm on its toxicity list, and it adds potassium channel block; metoprolol causes less bronchospasm.", RULED],
   ["Propafenone", "Propafenone's beta-blocking activity brings bronchospasm, and it is a class IC drug; metoprolol is beta-1 selective with less bronchospasm.", RULED]], 29),

Q("Beta-1 selective blockers", IO_ADME, "drug choice",
  "Which beta blocker is the intravenous, short-acting one?",
  [["Esmolol", "Correct. Esmolol is the intravenous, short-acting beta blocker."],
   ["Propranolol", "Propranolol is the nonselective beta blocker used as the class II example; the intravenous short-acting one is esmolol.", ADJ],
   ["Metoprolol", "Metoprolol is a beta-1 selective blocker with less bronchospasm; the intravenous short-acting one is esmolol.", ADJ],
   ["Sotalol", "Sotalol is a beta blocker that also inhibits potassium channels; the intravenous short-acting beta blocker is esmolol.", ADJ]], 29),

Q("Beta-1 selective blockers", IO_AE, "adverse effect",
  "Which central nervous system effects are listed for metoprolol and acebutolol?",
  [["Sedation and fatigue", "Correct. Central nervous system sedation and fatigue are listed for metoprolol and acebutolol, with congestive heart failure."],
   ["Seizures and nystagmus", "Seizures and nystagmus are part of lidocaine's central nervous system toxicity; metoprolol and acebutolol cause sedation and fatigue.", ADJ],
   ["Tinnitus and blurred vision", "Tinnitus and blurred vision, with dizziness, are quinidine's cinchonism; metoprolol and acebutolol cause sedation and fatigue.", ADJ],
   ["Neuropathy and ataxia", "Neuropathy, muscle weakness and ataxia belong to amiodarone; metoprolol and acebutolol cause sedation and fatigue.", ADJ]], 29),

Q("Beta-1 selective blockers", IO_CONTRA, "contraindication",
  "Which condition can a beta-1 selective blocker such as metoprolol still worsen?",
  [["Congestive heart failure", "Correct. Metoprolol and acebutolol cause less bronchospasm, but congestive heart failure remains on their list."],
   ["Thrombocytopenia", "Thrombocytopenia is listed for quinidine and flecainide; metoprolol and acebutolol can still worsen congestive heart failure.", ADJ],
   ["Glaucoma", "Glaucoma contraindicates disopyramide because of its anticholinergic action; metoprolol can still worsen congestive heart failure.", ADJ],
   ["A seizure disorder", "Seizures are a contraindication to lidocaine; metoprolol can still worsen congestive heart failure.", ADJ]], 29),

# ---- class IV (slides 37-39) ----------------------------------------------------------------------------
Q("Class IV actions", IO_CLASS, "class",
  "Verapamil and diltiazem belong to which antiarrhythmic class?",
  [["Class IV", "Correct. Verapamil and diltiazem are the class IV calcium channel blockers; they block the L-type channel and slow atrioventricular node conduction."],
   ["Class I", "Class I drugs are sodium channel blockers; verapamil and diltiazem are class IV calcium channel blockers.", MECH],
   ["Class II", "Class II drugs are beta blockers, which act on the same nodes; verapamil and diltiazem are class IV calcium channel blockers.", MECH],
   ["Class III", "Class III drugs prolong repolarization through potassium; verapamil and diltiazem are class IV.", MECH]], 37),

Q("Class IV actions", IO_MOA, "mechanism",
  "Which channel do class IV antiarrhythmics block?",
  [["The L-type calcium channel", "Correct. Class IV drugs block the L-type calcium channel, decrease automaticity, slow atrioventricular node conduction and are negative inotropes."],
   ["The fast sodium channel", "The fast sodium channel is blocked by class I drugs; class IV blocks the L-type calcium channel.", MECH],
   ["The potassium efflux channel", "Reducing potassium efflux is the class III mechanism; class IV blocks the L-type calcium channel.", MECH],
   ["The sodium-potassium pump", "The sodium-potassium ATPase is inhibited by digoxin; class IV blocks the L-type calcium channel.", MECH]], 37),

Q("Verapamil and diltiazem", IO_MOA, "mechanism",
  "Where are verapamil and diltiazem most effective?",
  [["In the most active tissue", "Correct. Verapamil and diltiazem block both activated and inactivated channels and are most effective in the most active tissue."],
   ["In ischemic tissue", "Greatest effect in ischemic tissue is the class IB (lidocaine) feature; verapamil and diltiazem work best in the most active tissue.", MECH],
   ["In normal ventricular muscle", "Affecting the normal heart is a class IC feature; verapamil and diltiazem are most effective in the most active tissue.", MECH],
   ["In tissue at rest", "Verapamil and diltiazem block activated and inactivated channels, so they work best in the most active tissue, not resting tissue.", REV]], 38),

Q("Verapamil and diltiazem", IO_MOA, "mechanism",
  "What do verapamil and diltiazem do to the sinoatrial and atrioventricular nodes?",
  [["Suppress the sinoatrial node, slow the atrioventricular node", "Correct. Verapamil and diltiazem suppress the sinoatrial node and decrease atrioventricular conduction."],
   ["Speed both the sinoatrial and atrioventricular nodes", "Speeding conduction is the reverse of their action; verapamil and diltiazem suppress the sinoatrial node and decrease atrioventricular conduction.", REV],
   ["Hyperpolarize both nodes through potassium channels", "Hyperpolarizing cells through atrial potassium channels is adenosine; verapamil and diltiazem block calcium channels.", MECH],
   ["Shorten phase 3 in both nodes", "Shortening phase 3 is the class IB effect in working muscle; verapamil and diltiazem suppress the sinoatrial node and slow atrioventricular conduction.", MECH]], 38),

Q("Verapamil and diltiazem", IO_IND, "indication",
  "Which arrhythmia is a listed indication for verapamil and diltiazem?",
  [["Supraventricular tachycardia", "Correct. Verapamil and diltiazem are listed for supraventricular tachycardia (paroxysmal) and atrial fibrillation."],
   ["Ventricular tachycardia", "Verapamil and diltiazem are to be avoided in ventricular arrhythmias; their indications are paroxysmal supraventricular tachycardia and atrial fibrillation.", REV],
   ["Torsades de pointes", "Torsades de pointes is treated with intravenous magnesium sulfate; verapamil and diltiazem are listed for supraventricular tachycardia and atrial fibrillation.", ADJ],
   ["Ventricular fibrillation", "Ventricular fibrillation is a ventricular arrhythmia, where verapamil and diltiazem are to be avoided; their indications are supraventricular.", REV]], 39),

Q("Verapamil and diltiazem", IO_CONTRA, "contraindication",
  "In which rhythms should verapamil and diltiazem be avoided?",
  [["Ventricular arrhythmias", "Correct. Verapamil and diltiazem are to be avoided in ventricular arrhythmias, sick sinus syndrome and depressed cardiac function."],
   ["Atrial fibrillation", "Atrial fibrillation is a listed indication for verapamil and diltiazem, not a reason to avoid them.", REV],
   ["Supraventricular tachycardia", "Paroxysmal supraventricular tachycardia is the first listed indication for verapamil and diltiazem, not a reason to avoid them.", REV],
   ["Atrial flutter", "Atrial flutter is an atrial rhythm like the listed atrial fibrillation; the arrhythmias in which to avoid verapamil and diltiazem are ventricular.", REV]], 39),

Q("Verapamil and diltiazem", IO_CONTRA, "contraindication",
  "A patient with atrial fibrillation has depressed cardiac function. Which listed drug should be avoided?",
  [["Verapamil", "Correct. Verapamil and diltiazem are to be avoided in ventricular arrhythmias, sick sinus syndrome and depressed cardiac function; they are negative inotropes."],
   ["Digoxin", "Digoxin is listed to slow the ventricular rate in atrial fibrillation; depressed cardiac function is on the avoid list for verapamil.", ADJ],
   ["Amiodarone", "Amiodarone's listed dangers are lung, thyroid, eye, skin and liver toxicity; depressed cardiac function is on the avoid list for verapamil.", ADJ],
   ["Dofetilide", "Dofetilide is listed for normal rhythm in atrial fibrillation, with torsades as its danger; depressed cardiac function is on verapamil's avoid list.", ADJ]], 39),

Q("Class IV actions", IO_CONTRA, "contraindication",
  "Why are class IV calcium channel blockers avoided in depressed cardiac function?",
  [["They are negative inotropes", "Correct. Class IV drugs are negative inotropes, so verapamil and diltiazem are to be avoided in depressed cardiac function."],
   ["They are positive inotropes", "Class IV drugs lower contractility rather than raising it; that negative inotropic effect is why depressed function is on their avoid list.", REV],
   ["They prolong the QT interval", "Marked QT prolongation is listed for dofetilide; class IV drugs are avoided in depressed function because they are negative inotropes.", MECH],
   ["They block sodium channels", "Sodium channel block is the class I mechanism; class IV drugs block L-type calcium channels and are negative inotropes.", MECH]], 37),

Q("Verapamil and diltiazem", IO_AE, "adverse effect",
  "Which adverse effects are expected with verapamil and diltiazem?",
  [["Hypotension and edema", "Correct. Hypotension and edema are the listed toxicities of verapamil and diltiazem."],
   ["Bronchospasm and fatigue", "Bronchospasm belongs to propranolol and fatigue to metoprolol and acebutolol; verapamil and diltiazem cause hypotension and edema.", MECH],
   ["Flushing and chest burning", "Flushing, shortness of breath and chest burning are adenosine's; verapamil and diltiazem cause hypotension and edema.", ADJ],
   ["Nystagmus and seizures", "Nystagmus and seizures belong to lidocaine's central nervous system toxicity; verapamil and diltiazem cause hypotension and edema.", ADJ]], 39),

Q("Verapamil and diltiazem", IO_ADME, "contraindication",
  "Why are verapamil and diltiazem used with caution in liver damage?",
  [["They undergo hepatic metabolism", "Correct. Verapamil and diltiazem undergo hepatic metabolism, so caution is advised in liver damage."],
   ["They are eliminated unchanged by the kidneys", "Elimination unchanged by the kidneys is dofetilide's; verapamil and diltiazem are metabolized in the liver.", ADJ],
   ["They cause hepatic dysfunction", "Hepatic dysfunction is an adverse effect of amiodarone; verapamil and diltiazem need caution because the liver metabolizes them.", ADJ],
   ["They need loading doses", "Loading doses are for amiodarone, with its 40-day half-life; verapamil and diltiazem need caution because of hepatic metabolism.", ADJ]], 39),
]
