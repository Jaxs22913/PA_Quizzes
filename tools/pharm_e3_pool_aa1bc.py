# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Antiarrhythmic Drugs (Lecture 10), topic: class IB (lidocaine) and class IC (flecainide,
propafenone).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. Key authored FIRST (c == 0).

SOURCE. Antiarrhythmics.pptx slides 16-24: class IB actions (16, picture), lidocaine (17-19), class IC actions (20,
picture), flecainide (21-23), propafenone (24). Picture slides read by eye into tools/pharm_e3/ocr.json.

LEFT OUT ON PURPOSE:
  * channel affinity (inactivated > open; open > inactivated) and dissociation rates: not tested, per the lecturer;
  * lidocaine for Wolff-Parkinson-White (slide 17): current guidelines differ, so no key or distractor turns on it;
  * seizures as unique to lidocaine (the lecturer said so; slide 23 lists seizures for flecainide too);
  * "age" as a lidocaine contraindication (slide 19 gives the bare word, which cannot be keyed fairly);
  * the lecturer's spoken asides (heart failure or liver disease and lidocaine clearance; specialty use of class IC).
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

# ---- class IB (slide 16) ---------------------------------------------------------------------------
Q("Class IB actions", IO_CLASS, "class",
  "Which drug is the class IB antiarrhythmic?",
  [["Lidocaine", "Correct. Lidocaine is the class IB sodium channel blocker; it works mainly on sodium channels in ischemic tissue."],
   ["Flecainide", "Flecainide is class IC, which affects the normal heart and markedly slows phase 0; the class IB drug is lidocaine.", MECH],
   ["Procainamide", "Procainamide is class IA, with an active metabolite that has class III activity; the class IB drug is lidocaine.", MECH],
   ["Propafenone", "Propafenone is class IC with added beta-blocking activity; the class IB drug is lidocaine.", MECH]], 16),

Q("Class IB actions", IO_MOA, "mechanism",
  "Which effect on the cardiac action potential defines class IB?",
  [["Shortened phase 3", "Correct. Class IB shortens phase 3, so the action potential ends sooner, with an unchanged upstroke; it also decreases ectopic foci automaticity."],
   ["Markedly slowed phase 0", "A markedly slowed phase 0 is the class IC picture; class IB leaves the upstroke alone and shortens phase 3.", MECH],
   ["Prolonged phase 3", "A prolonged phase 3 is the class III action (potassium channel block), the reverse of class IB, which shortens phase 3.", REV],
   ["Flattened phase 4", "A flatter phase 4 in pacemaker cells is the class II and class IV picture; class IB shortens phase 3 in working muscle.", MECH]], 16),

Q("Class IB actions", IO_MOA, "mechanism",
  "Where do class IB drugs have their greatest effect?",
  [["Ischemic tissue", "Correct. Class IB drugs have a higher affinity in ischemic tissue and little effect in normal tissue; lidocaine is most effective on sodium channels in ischemic tissue."],
   ["Normal ventricular tissue", "Affecting the normal heart is the class IC feature; class IB has little effect in normal tissue and works mainly in ischemic tissue.", REV],
   ["The atria", "Lidocaine is not effective against atrial arrhythmias; class IB works mainly in ischemic tissue.", RULED],
   ["The sinoatrial node", "Suppressing the sinoatrial node is a class IV action (verapamil, diltiazem); class IB works mainly in ischemic tissue.", MECH]], 16),

Q("Class IB actions", IO_MOA, "mechanism",
  "Which automaticity do class IB drugs decrease?",
  [["That of ectopic foci", "Correct. Class IB drugs shorten phase 3 and decrease ectopic foci automaticity."],
   ["That of the sinoatrial node", "Suppressing the sinoatrial node is listed for verapamil and diltiazem (class IV); class IB decreases ectopic foci automaticity.", MECH],
   ["That of atrial pacemakers", "Lidocaine is not effective against atrial arrhythmias; class IB decreases the automaticity of ectopic foci.", RULED],
   ["That of the atrioventricular node", "Slowing the atrioventricular node is what class II and class IV drugs do; class IB decreases ectopic foci automaticity.", MECH]], 16),

# ---- lidocaine (slides 17-19) --------------------------------------------------------------------
Q("Lidocaine", IO_IND, "indication",
  "Which setting is a listed indication for lidocaine?",
  [["Acute myocardial infarction", "Correct. Lidocaine is listed for ventricular tachycardia and premature beats, ventricular fibrillation and acute myocardial infarction, where ischemic tissue is its target."],
   ["Atrial fibrillation", "Lidocaine is not effective against atrial arrhythmias; its listed settings are ventricular arrhythmias and acute myocardial infarction.", RULED],
   ["Torsades de pointes", "Torsades de pointes is treated with intravenous magnesium sulfate; lidocaine is listed for ventricular arrhythmias and acute myocardial infarction.", ADJ],
   ["Paroxysmal supraventricular tachycardia", "Paroxysmal supraventricular tachycardia is the indication for adenosine and for verapamil or diltiazem; lidocaine's are ventricular arrhythmias and acute myocardial infarction.", ADJ]], 17),

Q("Lidocaine", IO_IND, "indication",
  "Lidocaine is ineffective against which type of arrhythmia?",
  [["Atrial arrhythmias", "Correct. Lidocaine works on sodium channels in ischemic tissue, has less effect on normal tissue, and is not effective against atrial arrhythmias."],
   ["Ventricular tachycardia", "Ventricular tachycardia and premature beats are listed indications for lidocaine; it is atrial arrhythmias that it does not treat.", REV],
   ["Ventricular fibrillation", "Ventricular fibrillation is a listed indication for lidocaine; it is not effective against atrial arrhythmias.", REV],
   ["Premature ventricular beats", "Premature beats are listed with ventricular tachycardia among lidocaine's indications; lidocaine is not effective against atrial arrhythmias.", REV]], 18),

Q("Lidocaine", IO_ADME, "monitoring",
  "Why is lidocaine given intravenously?",
  [["Extensive first-pass metabolism", "Correct. Lidocaine undergoes extensive first-pass metabolism, so it is given intravenously rather than by mouth."],
   ["A half-life of about 40 days", "A 40-day half-life belongs to amiodarone, which needs loading doses; lidocaine is intravenous because of extensive first-pass metabolism.", ADJ],
   ["Elimination unchanged by the kidneys", "Elimination unchanged by the kidneys is listed for dofetilide; lidocaine is given intravenously because of extensive first-pass metabolism.", ADJ],
   ["A duration of action of 3 to 4 hours", "A 3 to 4 hour duration is procainamide's, solved with a slow-release preparation; lidocaine is intravenous because of first-pass metabolism.", ADJ]], 18),

Q("Lidocaine", IO_TOX, "adverse effect",
  "Which finding is an early sign of lidocaine toxicity?",
  [["Nystagmus", "Correct. Nystagmus is listed as the early sign of lidocaine toxicity, within its central nervous system toxicity."],
   ["Seizures", "Seizures are part of lidocaine's central nervous system toxicity, but the finding listed as the early sign is nystagmus.", STAGE],
   ["Tinnitus", "Tinnitus, with dizziness and blurred vision, is quinidine's cinchonism; the early sign of lidocaine toxicity is nystagmus.", ADJ],
   ["Corneal deposits", "Corneal deposits are an adverse effect of amiodarone; the early sign of lidocaine toxicity is nystagmus.", ADJ]], 19),

Q("Lidocaine", IO_TOX, "adverse effect",
  "Lidocaine toxicity shows mainly in which system?",
  [["Central nervous system", "Correct. Lidocaine's toxicity is central nervous system toxicity: drowsiness, confusion, restlessness, muscle twitches, seizures, and nystagmus as the early sign."],
   ["Pulmonary system", "Pneumonitis and pulmonary fibrosis are amiodarone's lung toxicity; lidocaine's toxicity is in the central nervous system.", ADJ],
   ["Thyroid gland", "Thyroid abnormalities belong to amiodarone, an analog of thyroid hormone; lidocaine's toxicity is in the central nervous system.", ADJ],
   ["Hematologic system", "Bone marrow suppression is listed for procainamide; lidocaine's toxicity is in the central nervous system.", ADJ]], 19),

Q("Lidocaine", IO_CONTRA, "contraindication",
  "Which history is a listed contraindication to lidocaine?",
  [["Seizures", "Correct. Seizures are a listed contraindication to lidocaine, whose own central nervous system toxicity can end in seizures."],
   ["Glaucoma", "Glaucoma contraindicates disopyramide because of its anticholinergic action; lidocaine's listed contraindication is seizures.", ADJ],
   ["Heart block", "Heart block contraindicates disopyramide and is a toxicity of propranolol and digoxin; lidocaine's listed contraindication is seizures.", ADJ],
   ["Asthma", "Asthma matters for bronchospasm with propranolol, sotalol and the class IC drugs; lidocaine's listed contraindication is seizures.", ADJ]], 19),

Q("Lidocaine", IO_TOX, "adverse effect",
  "Which cardiac effect is on lidocaine's toxicity list?",
  [["Faster atrioventricular conduction", "Correct. Lidocaine's toxicity list includes increased atrioventricular conduction, along with hypersensitivity and its central nervous system effects."],
   ["Slower atrioventricular conduction", "Slowing of atrioventricular conduction (up to heart block) belongs to beta blockers, class IV and digoxin; lidocaine's list says it increases atrioventricular conduction.", REV],
   ["Torsades de pointes", "Torsades de pointes belongs to class IA, dofetilide and sotalol; lidocaine's cardiac toxicity is increased atrioventricular conduction.", ADJ],
   ["Decreased contractility", "Decreased contractility is disopyramide's (heart failure); lidocaine's listed cardiac toxicity is increased atrioventricular conduction.", ADJ]], 19),

# ---- class IC (slide 20) ---------------------------------------------------------------------------
Q("Class IC actions", IO_MOA, "mechanism",
  "Which feature separates class IC from class IB?",
  [["IC affects the normal heart", "Correct. Class IC slows phase 0 and conduction, prolongs the refractory period and affects the normal heart; class IB has little effect on normal tissue."],
   ["IC works mainly in ischemic tissue", "Working mainly in ischemic tissue is the class IB feature, the reverse of class IC, which affects the normal heart.", REV],
   ["IC shortens phase 3", "Shortening phase 3 is the class IB action; class IC slows phase 0 and prolongs the refractory period.", REV],
   ["IC blocks L-type calcium channels", "Blocking L-type calcium channels is the class IV mechanism; class IC drugs are sodium channel blockers that affect the normal heart.", MECH]], 20),

Q("Class IC actions", IO_MOA, "mechanism",
  "Which change in the action potential is most marked with class IC drugs?",
  [["A much slower phase 0", "Correct. The class IC tracing shows a markedly slower phase 0 upstroke; class IC slows phase 0 and conduction and prolongs the refractory period."],
   ["A shortened phase 3", "A shortened phase 3 is the class IB picture; class IC markedly slows phase 0.", MECH],
   ["A prolonged phase 3 alone", "A prolonged phase 3 with an unchanged upstroke is the class III picture; class IC markedly slows phase 0.", MECH],
   ["A flatter phase 4", "A flatter phase 4 in pacemaker cells is the class II and class IV picture; class IC markedly slows phase 0.", MECH]], 20),

# ---- flecainide (slides 21-23) -------------------------------------------------------------------
Q("Flecainide", IO_CLASS, "class",
  "Which drug is a class IC antiarrhythmic?",
  [["Flecainide", "Correct. Flecainide is class IC (propafenone is the other); it blocks sodium and potassium channels in the ventricles."],
   ["Lidocaine", "Lidocaine is the class IB drug, working mainly in ischemic tissue; flecainide is class IC.", MECH],
   ["Quinidine", "Quinidine is class IA, the D-isomer of quinine; flecainide is class IC.", MECH],
   ["Sotalol", "Sotalol is a beta blocker with class III potassium channel action; flecainide is class IC.", MECH]], 21),

Q("Flecainide", IO_MOA, "mechanism",
  "Besides sodium channels, which channels does flecainide block in the ventricles?",
  [["Potassium channels", "Correct. Flecainide blocks sodium and potassium channels in the ventricles and slows recovery of the sodium channel."],
   ["L-type calcium channels", "L-type calcium channels are blocked by the class IV drugs verapamil and diltiazem; flecainide adds potassium channel block.", MECH],
   ["Beta receptors", "Beta-blocking activity is what propafenone adds to the shared class IC mechanism; flecainide's second target is the potassium channel.", ADJ],
   ["Alpha receptors", "Alpha blockade at higher doses is quinidine's indirect action; flecainide's second target is the potassium channel.", MECH]], 21),

Q("Flecainide", IO_MOA, "mechanism",
  "Which electrocardiogram intervals does flecainide prolong?",
  [["PR, QRS and QT", "Correct. Flecainide prolongs the PR, QRS and QT intervals; it blocks both sodium and potassium channels in the ventricles."],
   ["PR and QRS", "Flecainide prolongs the PR and QRS intervals but also the QT interval; all three lengthen.", STAGE],
   ["QRS and QT", "Flecainide prolongs the QRS and QT intervals but also the PR interval; all three lengthen.", STAGE],
   ["PR and QT", "Flecainide prolongs the PR and QT intervals but also the QRS interval; all three lengthen.", STAGE]], 21),

Q("Flecainide", IO_CONTRA, "contraindication",
  "Flecainide is to be used only in which patients?",
  [["Those without structural heart damage", "Correct. Flecainide is to be used only in patients without significant structural damage to the heart, and it increases mortality after myocardial infarction."],
   ["Those with a prior myocardial infarction", "Flecainide increases mortality after myocardial infarction, so this is the reverse of who should get it.", REV],
   ["Those with depressed cardiac function", "Depressed function is a damaged heart, and flecainide is limited to hearts without significant structural damage.", REV],
   ["Those who are slow acetylators", "Acetylator status matters for procainamide's lupus-like syndrome; flecainide's restriction is no significant structural heart damage.", ADJ]], 22),

Q("Flecainide", IO_TOX, "adverse effect",
  "Which serious risk is listed for flecainide after a myocardial infarction?",
  [["Increased mortality", "Correct. Flecainide's toxicity list includes increased mortality in myocardial infarction, which is why it is kept for hearts without significant structural damage."],
   ["Pulmonary fibrosis", "Pneumonitis and pulmonary fibrosis (potentially fatal) belong to amiodarone; flecainide's listed risk after infarction is increased mortality.", ADJ],
   ["Lupus-like syndrome", "A lupus-like syndrome is procainamide's effect, more often in slow acetylators; flecainide's risk after infarction is increased mortality.", ADJ],
   ["Cinchonism", "Cinchonism is quinidine's tinnitus, dizziness and blurred vision; flecainide's risk after infarction is increased mortality.", ADJ]], 23),

Q("Flecainide", IO_TOX, "adverse effect",
  "Which arrhythmia can flecainide cause that resists treatment?",
  [["Ventricular tachycardia", "Correct. Flecainide's toxicity list includes ventricular tachycardia resistant to treatment, a form of the proarrhythmia every antiarrhythmic can cause."],
   ["Atrial flutter", "Supraventricular arrhythmias are among flecainide's indications; the arrhythmia it can cause that resists treatment is ventricular tachycardia.", REV],
   ["Sinus bradycardia", "Bradycardia is listed for propafenone, through its beta-blocking activity; flecainide's treatment-resistant arrhythmia is ventricular tachycardia.", ADJ],
   ["Complete heart block", "Heart block is listed for propranolol and digoxin; flecainide's treatment-resistant arrhythmia is ventricular tachycardia.", ADJ]], 23),

Q("Flecainide", IO_ADME, "monitoring",
  "Which pharmacokinetic feature is listed for flecainide?",
  [["A long half-life of 14 hours", "Correct. Flecainide has a long half-life (14 hours) and can be given by mouth or intravenously."],
   ["Extensive first-pass metabolism", "Extensive first-pass metabolism is why lidocaine must be given intravenously; flecainide has a long 14-hour half-life and is also oral.", ADJ],
   ["A half-life of about 10 seconds", "A 10-second half-life belongs to adenosine; flecainide's half-life is a long 14 hours.", REV],
   ["Elimination unchanged by the kidneys", "Elimination unchanged by the kidneys is listed for dofetilide; flecainide's listed feature is a long 14-hour half-life.", ADJ]], 21),

Q("Flecainide", IO_AE, "adverse effect",
  "Which respiratory effect of flecainide matters in a patient with asthma?",
  [["Bronchospasm", "Correct. Bronchospasm is on flecainide's toxicity list (and propafenone's), a concern in asthma."],
   ["Pneumonitis", "Pneumonitis, with pulmonary fibrosis, is amiodarone's lung toxicity; flecainide's respiratory effect is bronchospasm.", ADJ],
   ["Respiratory paralysis", "Respiratory paralysis is listed for magnesium sulfate; flecainide's respiratory effect is bronchospasm.", ADJ],
   ["Pulmonary fibrosis", "Pulmonary fibrosis (potentially fatal) is amiodarone's; flecainide's respiratory effect is bronchospasm.", ADJ]], 23),

Q("Flecainide", IO_IND, "indication",
  "Which arrhythmia is a listed indication for flecainide?",
  [["Life-threatening ventricular arrhythmia", "Correct. Flecainide is listed for life-threatening sustained ventricular arrhythmias and supraventricular arrhythmias, in patients without significant structural heart damage."],
   ["Torsades de pointes", "Torsades de pointes is treated with intravenous magnesium sulfate; flecainide is listed for life-threatening sustained ventricular arrhythmias.", ADJ],
   ["Ventricular arrhythmia after infarction", "Flecainide increases mortality in myocardial infarction; lidocaine is the drug listed for acute myocardial infarction.", RULED],
   ["Rate slowing in atrial fibrillation", "Slowing the ventricular rate is digoxin's listed indication; flecainide is listed for life-threatening sustained ventricular arrhythmias.", ADJ]], 22),

Q("Flecainide", IO_TOX, "adverse effect",
  "Which nervous system effects are listed for flecainide?",
  [["Blurred vision and tremor", "Correct. Flecainide's toxicity list starts with blurred vision and tremor, and also includes seizures."],
   ["Tinnitus and dizziness", "Tinnitus and dizziness with blurred vision make up quinidine's cinchonism; flecainide's listed effects are blurred vision and tremor.", ADJ],
   ["Nystagmus and muscle twitches", "Nystagmus and muscle twitches are lidocaine's central nervous system toxicity; flecainide's are blurred vision and tremor.", ADJ],
   ["Neuropathy and ataxia", "Neuropathy, muscle weakness and ataxia belong to amiodarone; flecainide's listed effects are blurred vision and tremor.", ADJ]], 23),

# ---- propafenone (slide 24) -----------------------------------------------------------------------
Q("Propafenone", IO_MOA, "mechanism",
  "Propafenone shares flecainide's mechanism and adds which activity?",
  [["Beta-blocking activity", "Correct. Propafenone has the same mechanism as flecainide plus beta-blocking activity, which brings bradycardia, bronchospasm and worse heart failure."],
   ["Alpha-blocking activity", "Alpha blockade at higher doses is quinidine's indirect action; propafenone adds beta-blocking activity.", MECH],
   ["Potassium channel activation", "Activating atrial potassium channels is adenosine's action; propafenone adds beta-blocking activity.", MECH],
   ["Calcium channel blocking activity", "Calcium channel blockade is the class IV mechanism (amiodarone also has it); propafenone adds beta-blocking activity.", MECH]], 24),

Q("Propafenone", IO_AE, "adverse effect",
  "Which adverse effect of propafenone comes from its beta-blocking activity?",
  [["Bronchospasm", "Correct. Propafenone's toxicity list pairs bronchospasm with beta-adrenergic blockade; bradycardia and worsening heart failure come from the same activity."],
   ["Agranulocytosis", "Agranulocytosis, with anemia and thrombocytopenia, is on propafenone's list but is not a beta-blocking effect; bronchospasm is.", ADJ],
   ["Blurred vision", "Blurred vision and dizziness are on propafenone's list but do not come from beta blockade; bronchospasm does.", ADJ],
   ["Proarrhythmia", "Propafenone is proarrhythmic like every antiarrhythmic, but that is not a beta-blocking effect; bronchospasm is.", MECH]], 24),

Q("Propafenone", IO_TOX, "adverse effect",
  "Which drug lists agranulocytosis among its toxicities?",
  [["Propafenone", "Correct. Propafenone's toxicity list includes agranulocytosis, anemia and thrombocytopenia."],
   ["Flecainide", "Flecainide's blood toxicity is thrombocytopenia, not agranulocytosis; propafenone lists agranulocytosis.", ADJ],
   ["Lidocaine", "Lidocaine's toxicity is in the central nervous system, with hypersensitivity; propafenone lists agranulocytosis.", ADJ],
   ["Disopyramide", "Disopyramide's toxicity is hypotension, antimuscarinic effects, conduction disturbances, heart failure and torsades; propafenone lists agranulocytosis.", ADJ]], 24),

Q("Propafenone", IO_CONTRA, "contraindication",
  "Why is propafenone a concern in a patient with heart failure?",
  [["It can worsen heart failure", "Correct. Propafenone can worsen congestive heart failure, an effect of its beta-blocking activity."],
   ["It raises digoxin levels", "Raising digoxin levels is amiodarone's listed interaction; propafenone's concern in heart failure is that it can worsen it.", ADJ],
   ["It increases atrioventricular conduction", "Increased atrioventricular conduction is on lidocaine's toxicity list; propafenone's concern in heart failure is that it can worsen it.", ADJ],
   ["It causes a lupus-like syndrome", "A lupus-like syndrome is procainamide's effect; propafenone's concern in heart failure is that it can worsen it.", ADJ]], 24),
]
