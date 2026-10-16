# -*- coding: utf-8 -*-
"""Cram-sheet topics for Pharmacology I Exam 3, Lecture 10 (Antiarrhythmic Drugs; added 2026-10-16).

Imported by build_pharm_e3_cram.py, which verifies this module's REG against the Lecture 10 deck
(Antiarrhythmics.pptx). Same rules as the Lecture 9 rows, with the 2026-10-15 rule change: SLIDES WIN on conflict
(only what is visible on a slide; this deck has no speaker notes). Where a slide differs from current guidelines a row
in the closing topic says so ("Current guidelines differ"); where the recording and a slide disagree without an
explicit correction, both are printed and nothing is keyed. No milligram doses (the magnesium sulfate amount on
slide 45 is left out). Stars mark what Dr. Wood emphasized in the 2026-10-12 recording; a star only sets weight.

VERIFICATION. Each row is R(label, html, slide(s), verify[, quotes]); every `verify` substring must appear on the
cited slide (pharm_e3_lib.slide_text("L10", n), which includes the picture-slide text in pharm_e3/ocr.json) and every
`quotes` substring in the Lecture 10 transcript.
"""
REG = []   # (label, [(slide, [verify])], [quotes])


def R(label, html, slide=None, verify=(), quotes=()):
    if slide is None:
        pairs = []
    elif isinstance(slide, int):
        pairs = [(slide, list(verify))]
    else:
        pairs = [(s, list(v)) for s, v in slide]
    REG.append((label, pairs, list(quotes)))
    return [label, html]


T = []


def topic(tid, label, color, rows):
    T.append({"id": tid, "label": label, "color": color, "rows": rows})


# ----------------------------------------------------------------------------------------------
topic("aa-rules", "Antiarrhythmics &middot; what he stressed", "#8c1d12", [
 R("&#9733;&#9733; Know which drug is in which class",
   "He does not care about channel affinity, but <b>you must recognize which drugs fit in 1A, 1B and 1C</b>. "
   "<b>1A = PDQ: procainamide, disopyramide, quinidine.</b> 1B = lidocaine. 1C = flecainide, propafenone. "
   "Class II = beta blockers; class III = amiodarone, dofetilide, sotalol; class IV = verapamil, diltiazem; others = adenosine, digoxin (plus magnesium sulfate).",
   [(5, ["Class 1A (open>inactivated)", "Class 2   Beta Receptor Antagonists", "Class 4   Calcium Channel Blockers", "Others    Adenosine, Digitalis"]),
    (8, ["Class 1 A"]), (16, ["Class 1 B"]), (20, ["Class 1C"])],
   quotes=["but you do need to be able to recognize which drugs fit into each of those three categories."]),
 R("&#9733;&#9733; The indication trend",
   "Do not memorize the indication list; read the trend. <b>Class I and class III: both supraventricular and ventricular arrhythmias</b> (except 1B lidocaine: ventricular only). "
   "<b>Class II, class IV and the miscellaneous agents: supraventricular</b> (verapamil and diltiazem are to be avoided in ventricular arrhythmias).",
   [(6, ["Class 1-A", "Class III - Refractory ventricular tachycardia, atrial fibrillation, flutter, supraventricular tachycardia", "Class IV - Supraventricular tachycardia", "Misc agents - Supraventricular tachycardia"]),
    (39, ["Avoid in ventricular arrhythmias"]), (6, ["Ventricular tachycardia, ventricular fibrillation prevention, symptomatic ventricular beats"])],
   quotes=["what i want you to take are sort of the trends.", "they don't really do anything for ventricular arrhythmias."]),
 R("&#9733; Rate control versus rhythm control",
   "His framing (the slides do not use the words): <b>rhythm control</b> puts and keeps the patient in normal sinus rhythm (class I; quinidine &ldquo;maintain rhythm&rdquo;, dofetilide &ldquo;normal rhythm in atrial fibrillation&rdquo;). "
   "<b>Rate control</b> limits how many beats reach the ventricles (class II, class IV; digoxin &ldquo;slow ventricular rate&rdquo;).",
   [(10, ["Maintain rhythm with atrial flutter or fibrillation"]), (34, ["Normal rhythm in atrial fibrillation"]), (44, ["Slow ventricular rate"])],
   quotes=["so here's where i get into the discussion of rate control versus rhythm control.", "this is what we call rate control."]),
 R("Not tested",
   "<b>Channel affinity (open &gt; inactivated) and dissociation rate</b> for 1A, 1B and 1C: he said he would not harp on them.",
   [(5, ["Class 1B  (inactivated>open)"]), (8, ["Dissociation"]), (16, ["Rapid  (<1 sec)"])]),
 R("&#9733; Torsades de pointes &rarr; magnesium sulfate",
   "Torsades de pointes is listed for <b>quinidine (2-8%), procainamide, disopyramide, dofetilide (1-3%, marked QT prolongation) and sotalol</b>. "
   "Its treatment: <b>intravenous magnesium sulfate</b> (&ldquo;always magnesium sulfate&rdquo;).",
   [(11, ["Torsades de Pointes (2-8%)"]), (13, ["Torsades de pointes"]), (15, ["Torsades de Pointes"]), (34, ["Torsades de pointes (1-3%)", "Marked QT prolongation"]),
    (36, ["Torsades de Pointes"]), (45, ["Torsades de Pointes IV"])],
   quotes=["so it's a treatment of choice for torsades."]),
 R("&#9733; Every antiarrhythmic can cause an arrhythmia",
   "Principles: <b>identify and remove precipitating factors first (hypoxia, ischemia, electrolytes)</b>; set the goal (terminate or prevent); <b>all antiarrhythmics may induce arrhythmias</b>; ischemia makes the heart a &ldquo;moving target&rdquo;.",
   3, ["Identify and remove precipitating factors", "hypoxia, ischemia, electrolytes", "all Antiarrhythmics may induce arrhythmias", "moving target"],
   quotes=["any anti-arrhythmic drug may itself induce arrhythmias"]),
 R("Doses",
   "This site leaves milligram and gram amounts out (including the magnesium sulfate amount); doses are not tested in this course, per the earlier lectures. Half-lives, routes and percentages are kept."),
])

# ----------------------------------------------------------------------------------------------
topic("aa-classes", "Antiarrhythmics &middot; classes and the action potential", "#2f4f6b", [
 R("Four mechanisms",
   "<b>Sodium channel blockers</b>: decrease excitability. <b>Potassium channel blockers</b>: prolong the action potential. "
   "<b>Beta receptor blockade</b>: prolongs atrioventricular refractoriness and conduction, <b>raises the energy needed for fibrillation</b>. "
   "<b>Calcium channel blockers</b>: decrease slow-response (nodal) cell excitability.",
   4, ["Na+ channel blockers", "decrease excitability", "Action potential prolongation", "increase energy required for fibrillation", "decrease slow-response cells excitability"]),
 R("Sodium channel states",
   "<b>Resting</b> (closed, no sodium in) &rarr; <b>activated</b> (open, sodium rushes in: phase 0) &rarr; <b>inactivated</b> (gate plugs the channel while the cell repolarizes) &rarr; recovery to resting. Class I drugs act on this channel.",
   7, ["Resting", "Activated", "Inactivated", "Recovery"]),
 R("Ischemia moves the target",
   "<b>Ischemia may alter the resting membrane potential</b>, so the target shifts. That is why <b>lidocaine (1B) acts mainly on ischemic tissue</b> and leaves normal tissue largely alone.",
   [(3, ["Ischemia may alter resting membrane potential"]), (16, ["higher affinity in ischemic tissue, little effect in normal tissue"])]),
 R("Reading the pictures",
   "Solid line = normal; dashed = with the drug. <b>1A</b>: slower, lower phase 0, longer action potential. <b>1B</b>: same upstroke, phase 3 ends sooner (shorter). "
   "<b>1C</b>: markedly slower phase 0. <b>III</b>: same upstroke, phase 3 delayed (longer). <b>II and IV</b>: flatter phase 4 in pacemaker cells, so the next beat comes later.",
   [(8, ["lower phase 0"]), (16, ["shorter"]), (20, ["markedly slower phase 0"]), (30, ["repolarization (phase 3) is delayed"]),
    (25, ["phase 4 depolarization is flatter"]), (37, ["phase 4 depolarization is flatter"])]),
 R("Memory aid: the nightclub",
   "<i>A story, not a fact source.</i> Sinoatrial node = DJ; atrioventricular node = the door; ventricles = the main room. "
   "<b>Rate control works the door</b>: class II beta blockers are the bouncer, class IV a second bouncer using calcium, digoxin turns up the calming (parasympathetic) music. "
   "Door staff cannot stop a fight inside the main room (II and IV: supraventricular only). <b>Rhythm control works on the dancers</b>: class I slows the first step (phase 0), class III makes them rest longer (phase 3). "
   "Rest too long and the floor twists (torsades), untwisted by magnesium. Adenosine flips the power off for 2 to 3 seconds.",
   [(25, ["Prolong AV  conduction"]), (37, ["Slow AV node conduction"]), (43, ["Indirectly increases Parasympathetic tone decreases sympathetic"]),
    (30, ["Prolongs phase 3 repolarization"]), (41, ["may stop heart for 2-3 seconds"])]),
])

# ----------------------------------------------------------------------------------------------
topic("aa-1a", "Class IA &middot; quinidine, procainamide, disopyramide (PDQ)", "#1f6f5c", [
 R("Class IA actions",
   "<b>Slow phase 0, slow conduction, prolong the action potential.</b> Indications (class): supraventricular tachycardia, ventricular tachycardia, prevention of ventricular fibrillation and premature ventricular contractions.",
   [(8, ["Slow Phase 0", "slow conduction", "prolong action potential"]), (6, ["Supraventricular tachycardia, ventricular tachycardia, ventricular fibrillation prevention and PVC prevention"])]),
 R("Quinidine: what it is and does",
   "<b>D-isomer of quinine.</b> Slows conduction, <b>prolongs the refractory period</b>, slows phase 0, raises the excitability threshold, decreases automaticity. Indirect: <b>anticholinergic</b>; <b>alpha blocker at higher doses</b> (hence hypotension).",
   9, ["Isomer of Quinine", "Slows conduction", "Prolongs Refractory period", "Increases threshold for excitability", "Decreases automaticity", "Anticholinergic", "blocker at higher doses"]),
 R("Quinidine: uses and interaction",
   "<b>Maintain rhythm with atrial flutter or fibrillation</b>; control ventricular tachycardia; conversion of flutter and fibrillation (<b>very limited use</b>). <b>CYP2D6 (cytochrome P450 2D6) inhibitor</b> (codeine, morphine).",
   10, ["Maintain rhythm with atrial flutter or fibrillation", "Control Ventricular Tachycardia", "(very limited use)", "CYP 2D6 inhibitor (codeine, morphine)"]),
 R("&#9733; Quinidine toxicity",
   "<b>Nausea, vomiting, diarrhea (30-50%)</b>; ventricular and atrial arrhythmias; hypotension; <b>thrombocytopenia (may be fatal)</b>; "
   "<b>cinchonism = tinnitus, dizziness, blurred vision</b>; <b>quinidine sudden death</b>; <b>torsades de pointes (2-8%)</b>; immunological reactions.",
   11, ["Nausea, vomiting, Diarrhea (30-50%)", "Arrhythmias (ventricular and atrial)", "Thrombocytopenia (may be fatal)", "Cinchonism - tinnitus, dizziness, blurred vision", "Quinidine Sudden Death", "Torsades de Pointes (2-8%)", "Immunological reactions"],
   quotes=["and that includes tinnitus, dizziness, and blurred vision."]),
 R("Procainamide: kinetics",
   "Amide derivative of procaine. <b>Short duration (3-4 hours) &rarr; slow-release preparation.</b> Less anticholinergic than quinidine, <b>no alpha block</b>. "
   "<b>Active acetylated metabolite NAPA (N-acetylprocainamide) has class III activity</b>; fast acetylators may make more of it.",
   12, ["amide derivative of Procaine", "Short duration of action (3 - 4 hours) Slow release preparation", "Less anticholinergic activity", "No a - blocking activity", "Active acetylated metabolite  (NAPA)", "Class Three activity", "Fast acetylators may increase active metabolite"]),
 R("&#9733; Procainamide adverse effects",
   "<b>Lupus-like syndrome (25-50%, more often in slow acetylators)</b>; hypotension; slowed conduction; nausea; <b>torsades de pointes</b>; <b>bone marrow suppression (0.2%)</b>. "
   "<b>Intravenous: better tolerated than quinidine. Oral: poorly tolerated long term.</b>",
   13, ["Lupus like syndrome (25-50%, more often in slow acetylators)", "Hypotension", "Slowing of conduction", "Torsades de pointes", "Bone marrow suppression (0.2%)", "IV - Better tolerated than quinidine", "poorly tolerated long term"],
   quotes=["to this lupus-like syndrome."]),
 R("Disopyramide",
   "Like quinidine, but <b>more anticholinergic</b> and <b>negative inotropic</b>. For ventricular tachycardia and supraventricular arrhythmias (flutter, fibrillation). "
   "Toxicity: hypotension, antimuscarinic effects, conduction disturbances, <b>congestive heart failure (lower contractility)</b>, torsades. <b>Contraindicated: heart block, hypersensitivity, glaucoma.</b>",
   [(14, ["Effects similar to Quinidine", "More Anticholinergic actions", "Negative inotropic effects", "Supraventricular arrhythmias (Flutter, fibrillation)"]),
    (15, ["Antimuscarinic effects", "Conduction disturbances", "Congestive heart failure", "Contraindicated: heart block, hypersensitivity, glaucoma"])]),
 R("Telling PDQ apart",
   "<b>Cinchonism, diarrhea, fatal thrombocytopenia, cytochrome P450 2D6 inhibition</b> &rarr; quinidine. <b>Lupus-like syndrome, acetylators, class III metabolite</b> &rarr; procainamide. <b>Most anticholinergic, glaucoma, heart block, heart failure</b> &rarr; disopyramide.",
   [(11, ["Cinchonism"]), (13, ["Lupus like syndrome"]), (15, ["glaucoma"])]),
])

# ----------------------------------------------------------------------------------------------
topic("aa-1b", "Class IB &middot; lidocaine", "#4a4f8c", [
 R("&#9733; Class IB actions",
   "<b>Shorten phase 3</b> (shorter action potential); decrease ectopic foci automaticity. <b>Higher affinity in ischemic tissue, little effect in normal tissue.</b> Indications (class): ventricular only.",
   [(16, ["Shorten Phase 3", "Decrease ectopic foci automaticity", "higher affinity in ischemic tissue, little effect in normal tissue"]),
    (6, ["Ventricular tachycardia, ventricular fibrillation prevention, symptomatic ventricular beats"])],
   quotes=["because it has higher affinity in ischemic tissue."]),
 R("Lidocaine indications",
   "Ventricular tachycardia and premature beats; ventricular fibrillation; <b>acute myocardial infarction</b>; Wolff-Parkinson-White is also listed (see the guidelines topic).",
   17, ["Wolff-Parkinson-White", "Ventricular tachycardia, premature beats", "Ventricular fibrillation", "Acute MI"]),
 R("&#9733; Route and reach",
   "<b>Intravenous only: extensive first-pass metabolism.</b> Most effective on sodium channels in ischemic tissue. <b>Not effective against atrial arrhythmias.</b>",
   18, ["Given IV (Extensive first pass metabolism)", "Most effective on Na channels in ischemic tissue", "Less effect on normal tissue", "Not effective against atrial arrhythmias"],
   quotes=["so this one has to be given iv because it has really extensive first pass.", "this would be relegated to specifically ventricular arrhythmias."]),
 R("&#9733; Lidocaine toxicity",
   "<b>Central nervous system: drowsiness, confusion, restlessness, muscle twitches, seizures. Nystagmus = early sign of toxicity.</b> Hypersensitivity; increases atrioventricular conduction. "
   "<b>Contraindications: seizures, age.</b>",
   19, ["CNS toxicity: drowsiness, confusion, restlessness, muscle twitches, seizures", "Nystagmus (early sign of toxicity)", "Hypersensitivity", "Increases AV conduction", "Contraindications: seizures, age"],
   quotes=["confusion, restlessness, and that can then eventually lead into seizures, right?"]),
])

# ----------------------------------------------------------------------------------------------
topic("aa-1c", "Class IC &middot; flecainide, propafenone", "#8c2f3a", [
 R("Class IC actions",
   "<b>Slow phase 0 (the most of class I)</b>, slow conduction, prolong the refractory period, <b>affect the normal heart</b>. Indications (class): <b>life-threatening</b> ventricular tachycardia or fibrillation, <b>refractory</b> supraventricular tachycardia.",
   [(20, ["Slow Phase 0", "Slow conduction", "Prolongs refractory period", "Affect normal heart", "markedly slower phase 0"]),
    (6, ["Life threatening ventricular tachycardia, or fibrillation, refractory supraventricular  tachycardia"])]),
 R("Flecainide: actions and kinetics",
   "<b>Blocks sodium and potassium channels in the ventricles</b>; slows sodium channel recovery; <b>prolongs the PR, QRS and QT intervals</b>; prevents premature ventricular contractions. <b>Long half-life (14 hours)</b>; oral or intravenous.",
   21, ["Blocks Na+ channels and K+ channels in ventricles", "slows recovery of Na channel", "Prolongs PR, QRS and QT intervals", "Long half- life (14 hours), Oral, IV", "Prevent premature ventricular contractions"]),
 R("&#9733; Flecainide: who gets it",
   "Life-threatening sustained ventricular arrhythmias; supraventricular arrhythmias. <b>Only in patients WITHOUT significant structural heart damage</b>; <b>increased mortality after myocardial infarction</b> is on its toxicity list.",
   [(22, ["Life-threatening sustained ventricular arrhythmias", "Use only in patients without significant structural damage to heart"]), (23, ["mortality in MI"])],
   quotes=["and that has led to patient dying basically."]),
 R("Flecainide toxicity",
   "Blurred vision, <b>tremor</b>; <b>ventricular tachycardia resistant to treatment</b>; bronchospasm; seizures; thrombocytopenia; increased mortality after myocardial infarction. "
   "<i>Boxed warning (not on the slide): the Cardiac Arrhythmia Suppression Trial mortality.</i>",
   23, ["Blurred vision, tremor", "Ventricular tachycardia resistant to treatment", "Bronchospasm", "Seizures", "Thrombocytopenia", "mortality in MI"]),
 R("Propafenone",
   "<b>Same mechanism as flecainide + beta-blocking activity.</b> Toxicity: <b>proarrhythmic</b>; dizziness, blurred vision, <b>bradycardia</b>; <b>bronchospasm</b> (beta blockade); <b>agranulocytosis</b>, anemia, thrombocytopenia; <b>worsens heart failure</b>.",
   24, ["Same mechanism as Flecainide", "blocking activity", "Pro-arrhythmic", "Dizziness, blurred vision, bradycardia", "Bronchospasm", "Agranulocytosis, anemia, thrombocytopenia", "worsen CHF"]),
])

# ----------------------------------------------------------------------------------------------
topic("aa-2", "Class II &middot; beta blockers", "#b8862f", [
 R("&#9733; Class II actions",
   "<b>Slow conduction, decrease automaticity, prolong atrioventricular conduction, decrease phase 4 depolarization</b> (pacemaker cells reach threshold later). His image: the beta blocker is the <b>bouncer at the door</b> (rate control).",
   25, ["Slow conduction", "Decrease  Automaticity", "Prolong AV  conduction", "Decrease Phase 4 depolarization"],
   quotes=["but the beta blocker is serving as sort of like a bouncer, right?"]),
 R("Propranolol",
   "<b>Nonselective.</b> Reduces phase 4 activation, slows atrioventricular conduction, <b>negative inotropic and chronotropic</b>, suppresses premature ventricular beats, membrane stabilizing. "
   "Uses: <b>supraventricular arrhythmias</b>, ventricular ectopic beats, <b>myocardial infarction</b>.",
   [(26, ["Nonselective Beta blocker", "Reduce phase 4 activation", "Slow AV conduction", "Negative inotropic and chronotropic effects", "Suppress premature ventricular beats", "Membrane stabilizing"]),
    (27, ["Supraventricular arrhythmias", "Ventricular ectopic beats", "Myocardial Infarction"])]),
 R("&#9733; Propranolol toxicity",
   "<b>Heart failure, heart block, hypotension, bronchospasm</b> (nonselective: asthma), digitalis toxicity. Hyperglycemia is also listed (see the guidelines topic).",
   28, ["Heart failure", "Heart block", "Hypotension", "Hyperglycemia", "Bronchospasm", "Digitalis toxicity"],
   quotes=["bronchospasm, remember, propranolol is a non-selective beta blocker."]),
 R("&#9733; Metoprolol, acebutolol, esmolol",
   "<b>Beta-1 selective</b>, similar to propranolol, <b>less bronchospasm</b> (choose these in asthma). Still: congestive heart failure; <b>sedation and fatigue</b>. <b>Esmolol = intravenous, short-acting.</b>",
   29, ["acebutolol", "selective blocker", "Similar to Propranolol", "Less Bronchospasm", "Congestive heart failure", "CNS sedation and fatigue", "Esmolol, IV short acting"],
   quotes=["definitely better for patients who have reactive airway disease or asthma.", "it's a really short-acting agent."]),
])

# ----------------------------------------------------------------------------------------------
topic("aa-3", "Class III &middot; amiodarone, dofetilide, sotalol", "#7a4a9c", [
 R("Class III actions",
   "<b>Reduce potassium efflux, prolong phase 3 repolarization, prolong the refractory period and the action potential.</b> Indications (class): refractory ventricular tachycardia, atrial fibrillation, flutter, supraventricular tachycardia.",
   [(30, ["Reduces potassium efflux", "Prolongs phase 3 repolarization", "Prolong refractory period", "Prolong duration of action potential"]),
    (6, ["Class III - Refractory ventricular tachycardia"])]),
 R("&#9733; Amiodarone: what it is",
   "Oral and intravenous; <b>analog of thyroid hormone</b>. <b>Half-life about 40 days (26-107): slow onset, slow elimination, so loading doses.</b> "
   "Blocks <b>potassium, inactivated sodium and calcium channels and alpha and beta receptors</b>; decreases automaticity and conduction; prolongs refractory periods.",
   [(31, ["Oral and IV (Analog of Thyroid hormone)", "T1/2 40 days (26-107)", "(slow onset. slow elimination)", "may require loading doses"]),
    (32, ["blocks potassium channels", "blocks inactivated sodium channels", "blocks calcium channels", "blocks a and b-receptors", "Decreases automaticity", "decreases conduction", "Prolongs refractory periods"])],
   quotes=["and interestingly, it's an analog of thyroid hormone.", "that's why we use loading doses."]),
 R("Amiodarone: uses",
   "<b>Recurrent ventricular tachycardia or fibrillation resistant to other drugs</b>; maintain normal rate in atrial fibrillation. <b>Intravenous: terminates acute ventricular tachycardia or fibrillation, replacing lidocaine in myocardial infarction.</b>",
   31, ["Recurrent ventricular tachycardia or fibrillation resistant to other drugs", "maintain normal rate in atrial fibrillation", "terminate acute ventricular tachycardia or fibrillation replacing lidocaine in MI"]),
 R("&#9733; Amiodarone toxicity",
   "Hypotension; <b>pneumonitis, pulmonary fibrosis (potentially fatal)</b>; neurotoxicity, neuropathy, muscle weakness, ataxia; <b>blue-gray skin, photosensitivity</b>; <b>corneal deposits</b>; "
   "<b>thyroid abnormalities (hyper or hypo)</b>; <b>hepatic dysfunction</b>. <i>Boxed warning (not on the slide): pulmonary and hepatic toxicity.</i>",
   33, ["Hypotension", "Pneumonitis, pulmonary fibrosis (potentially fatal)", "Neurotoxicity, neuropathy, muscle weakness, ataxia", "Blue-Grey skin color, photosensitivity", "Corneal deposits", "Thyroid abnormalities (hyper,hypo)", "Hepatic dysfunction"],
   quotes=["this kind of blue-gray skin discoloration that can occur, corneal issues, thyroid problems,"]),
 R("Amiodarone interactions",
   "<b>Increases digoxin, warfarin, flecainide, phenytoin and procainamide.</b>",
   33, ["Interactions - increases digoxin, warfarin, flecainide, phenytoin, procainamide"]),
 R("&#9733; Dofetilide",
   "<b>Potent pure potassium channel blocker.</b> For <b>normal rhythm in atrial fibrillation</b>. <b>Limited availability to those with special training.</b> "
   "<b>Torsades de pointes (1-3%), marked QT prolongation.</b> Mainly <b>eliminated unchanged by the kidneys</b>. <i>Boxed warning (not on the slide): start in a monitored facility.</i>",
   34, ["Potent pure K channel blocker", "Normal rhythm in atrial fibrillation", "Limited availability to those with special training", "Torsades de pointes (1-3%)", "Marked QT prolongation", "Mainly eliminated unchanged in kidneys"],
   quotes=["you have to start this in the hospital."]),
 R("&#9733; Sotalol = class II + class III",
   "<b>Beta-blocking activity plus potassium channel block</b>; decreases phase 4 depolarization; longer action potential; slower atrioventricular node conduction. "
   "For <b>atrial flutter and fibrillation, ventricular tachyarrhythmia</b>. Toxicity: <b>torsades de pointes, bronchospasm</b>, beta-blocking effects.",
   [(35, ["blocking activity", "Inhibits K+ channels", "Decreases Phase 4 depolarization", "Indications: atrial flutter and fibrillation, ventricular tachyarrhythmia"]),
    (36, ["increases action potential duration", "AV node conduction", "Torsades de Pointes", "Bronchospasm"])],
   quotes=["so you get both a class two and a class three effect here."]),
])

# ----------------------------------------------------------------------------------------------
topic("aa-4", "Class IV &middot; verapamil, diltiazem", "#3d6b52", [
 R("Class IV actions",
   "<b>Block the L-type calcium channel</b>; decrease automaticity; <b>slow atrioventricular node conduction</b>; <b>negative inotropic</b>. Block activated and inactivated channels; most effective in the <b>most active tissue</b>; <b>suppress the sinoatrial node</b>.",
   [(37, ["Decrease automaticity", "Blocks L-type channel", "Slow AV node conduction", "Negative inotropic"]),
    (38, ["Blocks both activated and inactivated channels", "Most effective in most active tissue", "Decreases AV conduction", "Suppresses SA node"])]),
 R("&#9733; Verapamil and diltiazem: use and avoid",
   "For <b>paroxysmal supraventricular tachycardia</b> and atrial fibrillation. Toxicity: <b>hypotension, edema</b>. Hepatic metabolism: <b>caution in liver damage</b>. "
   "<b>Avoid in ventricular arrhythmias, sick sinus syndrome, depressed cardiac function.</b>",
   39, ["Supraventricular Tachycardia (PSVT)", "Atrial fibrillation", "Hypotension, edema", "Hepatic metabolism, caution in liver damage", "Avoid in ventricular arrhythmias, sick sinus syndrome, depressed cardiac function"],
   quotes=["they don't work on ventricular arrhythmias as it turns out."]),
])

# ----------------------------------------------------------------------------------------------
topic("aa-misc", "Miscellaneous &middot; adenosine, digoxin, magnesium sulfate", "#a8562f", [
 R("&#9733; Adenosine: action",
   "<b>Activates potassium channels in the atria and blocks calcium channels &rarr; hyperpolarizes cells.</b> Slows conduction velocity: <b>may stop the heart for 2-3 seconds</b>; decreases automaticity; prolongs the refractory period. <b>Half-life about 10 seconds.</b> His image: turn it off and back on.",
   41, ["Activates potassium channels in atria and blocks Ca++ channels", "Hyperpolarizes cells", "decreases conduction velocity", "t 1/2 = 10 seconds", "may stop heart for 2-3 seconds", "Decreases automaticity, prolongs refractory period", "10 seconds"],
   quotes=["you turn it off and you turn it back on again."]),
 R("Adenosine: use and toxicity",
   "<b>Paroxysmal supraventricular tachycardia</b> (Wolff-Parkinson-White also listed). Toxicity: <b>flushing (20%)</b>, shortness of breath, burning in the chest.",
   42, ["Paroxysmal supraventricular tachycardia", "Wolff-Parkinson-White", "Flushing 20%", "Shortness  of breath", "Burning in chest"]),
 R("Digoxin: action",
   "<b>Sodium-potassium ATPase inhibition</b>; slows atrioventricular conduction; inhibits calcium channels in the atrioventricular node; <b>indirectly raises parasympathetic tone, lowers sympathetic</b>; <b>can induce heart block</b>.",
   43, ["Na/K ATPase inhibition", "Slows AV conduction", "Inhibits Ca channels in AV node", "Indirectly increases Parasympathetic tone decreases sympathetic", "Can induce heart block"]),
 R("&#9733; Digoxin: use, toxicity, avoid",
   "<b>Slow the ventricular rate</b>; induce heart block in atrial flutter and fibrillation. Toxicity: nausea, vomiting, diarrhea, anorexia; confusion, delirium, headache, seizures, visual disturbances. "
   "<b>Avoid calcium channel blockers and beta blockers</b> with it (additive slowing and heart block).",
   44, ["Slow ventricular rate", "Induce Heart Block (Atrial flutter, fibrillation)", "nausea, vomiting, diarrhea, anorexia", "confusion, delirium, headache seizures, visual disturbances", "Avoid calcium blockers"],
   quotes=["and then of course we avoid calcium channel blockers and beta blockers at the same time"]),
 R("&#9733; Magnesium sulfate",
   "Indication: <b>torsades de pointes, intravenous</b> (the treatment of choice he named). Toxicity: bradycardia, flushing, headache, <b>respiratory paralysis</b>.",
   45, ["Torsades de Pointes IV", "Bradycardia", "Flushing", "Headache", "Respiratory paralysis"],
   quotes=["it's always magnesium sulfate."]),
])

# ----------------------------------------------------------------------------------------------
topic("aa-lookup", "Antiarrhythmics &middot; which drug causes it", "#2f4f6b", [
 R("More than one class in one drug",
   "<b>Amiodarone</b>: potassium, inactivated sodium and calcium channels plus alpha and beta receptors. <b>Sotalol</b>: beta block + potassium block. <b>Propafenone</b>: flecainide&rsquo;s sodium block + beta block. "
   "<b>Procainamide</b>: its metabolite NAPA (N-acetylprocainamide) has class III activity. <b>Quinidine</b>: anticholinergic + alpha block. <b>Flecainide</b>: sodium + potassium channels.",
   [(32, ["blocks potassium channels", "blocks a and b-receptors"]), (35, ["blocking activity", "Inhibits K+ channels"]), (24, ["Same mechanism as Flecainide", "blocking activity"]),
    (12, ["Class Three activity"]), (9, ["Anticholinergic", "blocker at higher doses"]), (21, ["Blocks Na+ channels and K+ channels in ventricles"])]),
 R("Bronchospasm",
   "<b>Propranolol</b> (nonselective), <b>sotalol</b> and <b>propafenone</b> (beta-blocking activity), and <b>flecainide</b>. Metoprolol and acebutolol: <b>less bronchospasm</b>.",
   [(28, ["Bronchospasm"]), (36, ["Bronchospasm"]), (24, ["Bronchospasm"]), (23, ["Bronchospasm"]), (29, ["Less Bronchospasm"])]),
 R("Blood counts",
   "<b>Quinidine: thrombocytopenia (may be fatal).</b> Procainamide: bone marrow suppression (0.2%). Flecainide: thrombocytopenia. <b>Propafenone: agranulocytosis, anemia, thrombocytopenia.</b>",
   [(11, ["Thrombocytopenia (may be fatal)"]), (13, ["Bone marrow suppression (0.2%)"]), (23, ["Thrombocytopenia"]), (24, ["Agranulocytosis, anemia, thrombocytopenia"])]),
 R("Weaker pump, heart failure",
   "<b>Disopyramide</b> (negative inotropic, congestive heart failure), <b>propafenone</b> (worsens heart failure), <b>propranolol</b> and <b>metoprolol</b> (heart failure), "
   "<b>verapamil and diltiazem</b> (negative inotropic; avoid with depressed cardiac function).",
   [(14, ["Negative inotropic effects"]), (15, ["Congestive heart failure"]), (24, ["worsen CHF"]), (28, ["Heart failure"]), (29, ["Congestive heart failure"]),
    (37, ["Negative inotropic"]), (39, ["depressed cardiac function"])]),
 R("Heart block",
   "<b>Digoxin can induce heart block</b> (the aim in atrial flutter and fibrillation). Propranolol lists heart block. <b>Disopyramide is contraindicated in heart block.</b>",
   [(43, ["Can induce heart block"]), (44, ["Induce Heart Block (Atrial flutter, fibrillation)"]), (28, ["Heart block"]), (15, ["Contraindicated: heart block"])]),
 R("Eyes and brain",
   "<b>Blurred vision</b>: quinidine (cinchonism), flecainide, propafenone. <b>Nystagmus</b>: lidocaine (early toxicity). <b>Corneal deposits</b>: amiodarone. <b>Visual disturbances</b>: digoxin. "
   "<b>Glaucoma</b> contraindicates disopyramide. <b>Seizures</b>: lidocaine, flecainide, digoxin.",
   [(11, ["Cinchonism - tinnitus, dizziness, blurred vision"]), (23, ["Blurred vision, tremor", "Seizures"]), (24, ["Dizziness, blurred vision, bradycardia"]),
    (19, ["Nystagmus (early sign of toxicity)", "seizures"]), (33, ["Corneal deposits"]), (44, ["headache seizures, visual disturbances"]), (15, ["glaucoma"])]),
])

# ----------------------------------------------------------------------------------------------
topic("aa-guidelines", "Antiarrhythmics &middot; slide versus guideline and recording", "#8c1d12", [
 R("Tested from the slides",
   "These rows say where practice or the recording differs. <b>The slide wording is what you are tested on;</b> none of these points is asked as a question here."),
 R("Current guidelines differ: lidocaine",
   "Slide 17 lists Wolff-Parkinson-White as a lidocaine indication. <b>Lidocaine is not a recommended treatment for Wolff-Parkinson-White syndrome.</b>",
   17, ["Wolff-Parkinson-White"]),
 R("Current guidelines differ: adenosine",
   "Slide 42 lists Wolff-Parkinson-White. Adenosine can end the reentrant tachycardia of Wolff-Parkinson-White, but it is <b>avoided when the syndrome presents as pre-excited atrial fibrillation</b>.",
   42, ["Wolff-Parkinson-White"]),
 R("Current guidelines differ: amiodarone",
   "Slide 31: intravenous amiodarone has replaced lidocaine for acute ventricular tachycardia or fibrillation. Resuscitation guidance lists <b>amiodarone or lidocaine</b> as options for shock-refractory ventricular fibrillation or pulseless ventricular tachycardia.",
   31, ["replacing lidocaine in MI"]),
 R("Current guidelines differ: digoxin combinations",
   "Slide 44: avoid calcium channel blockers and beta blockers with digoxin. In practice digoxin is <b>often combined</b> with a beta blocker or a nondihydropyridine calcium channel blocker for rate control in atrial fibrillation, with the heart rate watched for excessive slowing.",
   44, ["Avoid calcium blockers"]),
 R("Recording vs slide: propranolol and glucose",
   "Slide 28 lists <b>hyperglycemia</b>. He read the glucose line and added that beta blockers can <b>mask the warning signs of hypoglycemia</b> (low blood sugar); he did not call the slide wrong. "
   "The two transcripts of the recording disagree on whether his first word was hyper- or hypoglycemia, so this point is not asked.",
   28, ["Hyperglycemia"],
   quotes=["but also they can mask the signs of hypoglycemia."]),
 R("Recording vs slide: seizures",
   "He said seizures are a lidocaine feature not really seen with other class I drugs, but slide 23 also lists <b>seizures for flecainide</b>. Do not treat seizures as unique to one drug; <b>nystagmus</b> is lidocaine's alone.",
   [(19, ["seizures", "Nystagmus (early sign of toxicity)"]), (23, ["Seizures"])],
   quotes=["you don't really see that with other antiarrhythmics in the class one."]),
 R("Recording vs slide: beta blockers and ventricular beats",
   "His trend: beta blockers do not work for ventricular arrhythmias. Slides 26 and 27 still list <b>premature ventricular beats and ventricular ectopic beats for propranolol</b> (membrane stabilizing; he called that use &ldquo;out in the weeds&rdquo;).",
   [(26, ["Suppress premature ventricular beats", "Membrane stabilizing"]), (27, ["Ventricular ectopic beats"])],
   quotes=["kind of out in the weeds."]),
 R("Boxed warnings (not on the slides)",
   "<b>Food and Drug Administration boxed warnings not on the slides:</b> flecainide (increased mortality, from the Cardiac Arrhythmia Suppression Trial); amiodarone (pulmonary and hepatic toxicity); "
   "dofetilide (start in hospital with monitoring, which he also described)."),
])

assert len({t["id"] for t in T}) == len(T), "duplicate topic id"
