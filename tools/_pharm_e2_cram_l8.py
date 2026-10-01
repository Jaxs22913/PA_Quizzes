# -*- coding: utf-8 -*-
"""Cram-sheet topics for Pharmacology I Exam 2, Lecture 8 (myocardial ischemia; added 2026-09-30).

Imported by build_pharm_e2_cram.py and appended after the Lectures 5 to 7 topics.
Same sources and rules as the guide section (_pharm_e2_guide_l8.py): slide facts
only (Myocardial Ischemia Drugs.pptx), no milligram doses, truth wins where the
deck is wrong (rows marked FLAG say what the slide says and what is true).

STARS come from Dr. Wood's recording (tools/pharm_e2/wood.json, lec L8). A star
only sets weight; no star adds a fact the deck lacks.
"""

T = [
# ---------------------------------------------------------------- Lecture 8
# Stars below are from Dr. Wood's recording (tools/pharm_e2/wood.json, lec L8); no fact was added by a star.
{"id":"mi-rules","label":"Ischemia &middot; what is NOT on it","color":"#8c1d12","rows":[
 ["Last lecture","&ldquo;The end of the testable material for the exam for Monday ends with this PowerPoint.&rdquo; The diuretics and heart failure deck after it is the next exam."],
 ["Cell lines","&ldquo;I don&rsquo;t care that you know the difference between which one&rsquo;s made with E. coli versus hamster cells.&rdquo; Skip the Chinese hamster ovary cells against <i>Escherichia coli</i> detail."],
 ["Streptokinase the drug","&ldquo;I don&rsquo;t want you to worry so much about that, but I do want to focus on this picture.&rdquo; Learn the PICTURE: <b>plasminogen &rarr; plasmin</b>, by a streptokinase complex or by tissue plasminogen activator."],
 ["Dosing","This site leaves milligram amounts out (doses are not tested in this course, per the earlier lectures); he quoted the aspirin loading amount without saying whether it is examined. Timings and routes (12 hours on and off, under the tongue) are fair."],
 ["&#9733; What he stressed","<b>Prevention against quick relief</b> (&ldquo;I will reiterate and reiterate and reiterate&rdquo;); <b>what to add next and what to switch to</b>; and the <b>comorbidity table</b> (&ldquo;a cornucopia of test questions&rdquo;)."],
]},
{"id":"mi-frame","label":"Ischemia &middot; angina &amp; supply and demand","color":"#8c2f3a","rows":[
 ["Definitions","<b>Ischemic heart disease</b> = imbalance between myocardial oxygen supply and demand. <b>Coronary heart disease</b> = atherosclerotic narrowing of coronary arteries. <b>Angina pectoris</b> = chest pain, the clinical manifestation of ischemia. Acute coronary syndrome = unstable angina, acute myocardial infarction, sudden cardiac death."],
 ["Demand","<b>Heart rate, contractility, systolic wall tension.</b> Wall tension = preload (initial stretch, ventricular volume) plus afterload (pressure ejected against, systemic vascular resistance)."],
 ["Supply","Arterial oxygen pressure and hemoglobin; <b>coronary flow</b> and its distribution; oxygen extraction and microcirculation."],
 ["Stenosis","Clinically significant: <b>50% of the left main</b> or <b>75% of another major coronary artery</b>. Above 90% = virtually no flow."],
 ["&#9733; Variant (Prinzmetal) angina","<b>Vasospasm</b>; <b>younger</b>, <b>fewer risk factors</b>; often <b>night or early morning</b>; ST elevation may or may not show. <b>Treat with calcium channel blockers and nitrates; AVOID beta blockers</b> (worse symptoms)."],
 ["Risk factors","Non-modifiable: family history of premature cardiovascular event; age above <b>45 (men), 55 (women)</b>. Modifiable: sedentary life, diabetes, tobacco, overweight, hypertension, dyslipidemia."],
 ["Goals and strategy","More <b>quantity</b> of life (prevent acute coronary syndrome) and <b>quality</b> (relieve and prevent symptoms). <b>Lower demand</b> (rate, contractility, wall tension) and <b>raise supply</b> (coronary flow); stabilize plaque; fix risk factors."],
 ["&#9733; Prevention vs quick relief","<b>PREVENT</b> (beta blockers, calcium channel blockers, long-acting nitrates) vs <b>QUICK RELIEF</b> (short-acting sublingual nitroglycerin). A stem asks for one and offers the other."],
 ["Three treatment arms","<b>Revascularization</b> (percutaneous coronary intervention, bypass grafting) &middot; <b>antianginals</b> (beta blockers, calcium channel blockers, nitrates) &middot; <b>vasculoprotective</b> (antiplatelets, statins, angiotensin-converting enzyme inhibitors) &middot; lifestyle."],
 ["&#9733; Grades of angina","Graded by <b>how much activity he can do</b>; exercise capacity also shows whether therapy works. <b>I</b> no limitation &middot; <b>II</b> slight, symptoms with more than ordinary activity &middot; <b>III</b> marked, symptoms with ordinary activity &middot; <b>IV</b> any activity; <b>may have symptoms at rest</b>. Comfortable at rest in I to III."],
 ["Memory aid (not fact)","Oxygen BUDGET: supply = income, demand = spending, angina = overdraft warning. Beta blockers cut spending only; calcium channel blockers and nitrates cut spending AND lift income."],
 ["FLAG: slide 13","Slide lists aspirin and clopidogrel as raising coronary flow. <b>Truth: they prevent clots; they do not dilate.</b> Learn them as vasculoprotective."],
]},
{"id":"mi-bbccb","label":"Ischemia &middot; beta blockers &amp; calcium channel blockers","color":"#4a4f8c","rows":[
 ["&#9733; Beta blockers: role","<b>First line</b> for angina if no contraindication. Helpful with hypertension, anxiety, supraventricular arrhythmias, heart failure, <b>prior myocardial infarction</b>. Act on <b>DEMAND only</b>: lower rate, contractility, systolic pressure; <b>no effect on supply</b>; left ventricular volume goes UP."],
 ["&#9733; Agents (alphabet rule)","Beta-1 selective A&ndash;M: <b>metoprolol, atenolol</b>. Non-selective N&ndash;Z: <b>propranolol, nadolol</b>. Third generation, the exception: <b>carvedilol, labetalol</b>."],
 ["Beta blocker contraindications","<b>Heart rate below 60; systolic pressure below 100 mmHg; atrioventricular block; acute decompensated heart failure.</b> Precautions: reactive airway disease, systolic heart failure, diabetes, peripheral vascular disease."],
 ["&#9733; Beta blocker harms and teaching","Hypotension, bradycardia, hyperglycemia, dyslipidemia; fatigue, sexual dysfunction, <b>nightmares</b>, worse claudication. Monitor <b>heart rate, blood sugar, lipids</b>. Teach: <b>do not stop suddenly</b>; dizziness, fatigue."],
 ["&#9733; Calcium channel blockers: supply AND demand","<b>Mild dilation where stenosis is fixed; relief of vasospasm.</b> Non-dihydropyridine (diltiazem, verapamil) = HEART: rate, contractility, atrioventricular conduction all down (verapamil most). Dihydropyridine (nifedipine, amlodipine, felodipine) = VESSELS: most vasodilation, <b>no atrioventricular effect</b>; rate up with nifedipine and felodipine, unchanged with amlodipine."],
 ["&#9733; Place in therapy","<b>Non-dihydropyridine first</b> when beta blockers are contraindicated or not tolerated. <b>Dihydropyridine ADDED to a beta blocker</b> when it fails. Also with long-acting nitrates. <b>AVOID short-acting agents (nifedipine).</b> Good for vasospastic angina, severe peripheral vascular disease, asthma, uncontrolled diabetes, left ventricular dysfunction (dihydropyridine only)."],
 ["&#9733; Calcium channel blocker contraindications","<b>Systolic pressure below 100 mmHg.</b> Non-dihydropyridine only: <b>heart rate below 60, acute heart failure, ejection fraction below 40%</b>. Atrioventricular block (FLAG: means the non-dihydropyridines; dihydropyridines do not slow conduction). Precautions: beta blocker with a non-dihydropyridine; CYP3A4 (cytochrome P450 3A4) interactions."],
 ["&#9733; Calcium channel blocker harms and teaching","Hypotension; dihydropyridines: <b>headache, flushing, peripheral edema</b>. Monitor symptom relief and heart rate (non-dihydropyridine). Teach: <b>dizziness, constipation</b> (straining strains the heart; ask about bowel habits)."],
 ["&#9733; Combinations and the switch","<b>Nifedipine and felodipine ALONE raise the heart rate</b> (amlodipine leaves it unchanged) &rarr; add a dihydropyridine to a beta blocker. <b>Beta blocker + non-dihydropyridine = avoid</b> (more bradycardia, heart block). <b>Nightmares on a beta blocker &rarr; switch to a non-dihydropyridine.</b> Left ventricular dysfunction &rarr; <b>dihydropyridine only</b>."],
 ["&#9733; CYP3A4 (cytochrome P450 3A4)","The one enzyme to know. <b>Non-dihydropyridines (verapamil, diltiazem) inhibit it AND are substrates</b>; dihydropyridines (amlodipine) are only substrates. Verapamil + simvastatin &rarr; simvastatin levels rise (sections 3.4, 4.2)."],
 ["Demand table","Beta blockers: rate DOWN, left ventricular volume UP. Dihydropyridine: rate UP, pressure down hard. Non-dihydropyridine: rate DOWN. Nitrates: rate UP, left ventricular volume DOWN hard."],
]},
{"id":"mi-nitrates","label":"Ischemia &middot; nitrates","color":"#1f6f5c","rows":[
 ["Mechanism","Nitric oxide &rarr; guanosine triphosphate to <b>cyclic guanosine monophosphate</b> &rarr; protein kinase G &rarr; <b>lower cytosolic calcium</b> &rarr; smooth muscle relaxation, vasodilation, lower blood pressure. <b>Phosphodiesterase type 5 breaks cyclic guanosine monophosphate down.</b>"],
 ["Effects","Demand: pressure down, <b>left ventricular volume down hard</b>, rate up. Supply: <b>dilate coronary arteries</b>, relieve vasospasm, antithrombotic and antiplatelet effects."],
 ["&#9733; Short-acting","<b>Sublingual tablet or spray = the QUICK-RELIEF answer.</b> Goals: relieve acute ischemia AND prevent effort angina. Teach: <b>orthostatic hypotension</b>; original packaging, cool dry place; <b>replace tablets 3 to 6 months after opening</b> (the course rule; FLAG: current labeling ties expiry to the printed date in the original closed bottle); under the tongue."],
 ["&#9733;&#9733; Five-minute rule","<b>No relief 5 minutes after the first dose &rarr; call emergency medical services.</b> (The slide says dose every 5 minutes until relief or help arrives; standard practice caps it at three doses; his words: keep dosing while waiting.) The action is the answer, not the number."],
 ["&#9733; Long-acting","Usually the <b>third add-on</b>; usually an adjunct; <b>not recommended as monotherapy</b>. Allowed as initial therapy only when beta blockers AND calcium channel blockers are both contraindicated or not tolerated; otherwise added to them when they are not successful. <b>Isosorbide mononitrate</b>: lasts 12 hours, once daily. <b>Isosorbide dinitrate</b>: 3 to 6 hours, three times daily. Forms: ointment, transdermal patch."],
 ["Ointment and patch","<b>12 hours on, 12 hours off.</b> Ointment: measure on applicator paper, thin layer on chest, keep covered, <b>wipe off the old dose first</b>."],
 ["&#9733; Nitrate-free interval (tachyphylaxis)","All you need to know: <b>12 hours on, 12 hours off</b>, off when the patient is least likely to have symptoms (asleep). Tolerance with continued use; cause <b>not fully understood</b> (cofactor depletion, renin-angiotensin and sympathetic counter-regulation, plasma volume expansion, less enzyme activity). Fix: <b>nitrate-free interval</b> when symptoms are least frequent."],
 ["Adverse reactions","<b>Headache, flushing, postural hypotension, reflex tachycardia.</b>"],
 ["&#9733; Contraindications","<b>Phosphodiesterase type 5 inhibitors (sildenafil, tadalafil, vardenafil) are absolute</b> &rarr; <b>hypotension, myocardial infarction or stroke</b>. FLAG: the slide lists aortic valve stenosis and obstructive cardiomyopathy as contraindications; current labeling says avoid in severe aortic stenosis and obstructive cardiomyopathy."],
]},
{"id":"mi-addon","label":"Ischemia &middot; add-on, comorbid conditions, prevention","color":"#a2681c","rows":[
 ["&#9733; Order of use","<b>Add-on:</b> beta blocker, then a dihydropyridine, then a long-acting nitrate. <b>Switch:</b> beta blocker not tolerated &rarr; non-dihydropyridine. Third agent &rarr; further workup. Beta blocker + non-dihydropyridine: &ldquo;begging for trouble.&rdquo;"],
 ["Combination","Consider when angina persists on one drug. <b>Beta blocker plus calcium channel blocker</b> if tolerated (may lengthen exercise). A <b>third agent</b> means further workup (angiography)."],
 ["&#9733; Comorbid table: solid rows","<b>Prior myocardial infarction, hypertension, reduced left ventricular function &rarr; beta blocker first</b> (reduced function: amlodipine is the calcium channel blocker alternative; avoid the others). <b>Bradycardia or atrioventricular block &rarr; dihydropyridine first; avoid non-dihydropyridines AND beta blockers.</b> <b>Asthma &rarr; avoid non-cardioselective beta blockers.</b>"],
 ["&#9733; Comorbid table: two course cells","<b>Prior myocardial infarction &rarr; beta blocker first; AVOID calcium channel blockers.</b> <b>Diabetes &rarr; non-dihydropyridine first; alternatives long-acting nitrate and cardioselective beta blocker; avoid non-cardioselective beta blockers</b> (beta blockers can raise blood sugar and mask hypoglycemia). These are the course answers. FLAG: current practice is less absolute (a non-dihydropyridine can substitute after infarction when a beta blocker cannot be used; a cardioselective beta blocker is still sound in diabetes)."],
 ["&#9733; Angiotensin-converting enzyme inhibitors","For coronary disease with <b>diabetes and/or left ventricular systolic dysfunction</b>. Do NOT change oxygen use and do NOT relieve angina; may slow disease progression. Continue <b>indefinitely</b> after myocardial infarction, left ventricular dysfunction, or diabetes; consider in all vascular disease."],
 ["&#9733; Antiplatelets","<b>Aspirin for all ischemic heart disease</b> without contraindication (prevents acute coronary syndrome). <b>Clopidogrel</b> = as good as aspirin in secondary prevention; <b>for aspirin allergy</b>."],
 ["&#9733; One-slide strategy (the standing list)","Everyone (unless contraindicated): aspirin, lipid-lowering, sublingual nitroglycerin; beta blocker if prior infarction; angiotensin-converting enzyme inhibitor with diabetes or left ventricular dysfunction. Daily symptoms: beta blocker, calcium channel blocker, long-acting nitrate."],
]},
{"id":"mi-acs","label":"Acute coronary syndrome &middot; clot and drugs","color":"#7a3b6b","rows":[
 ["Classification","<b>ST-elevation myocardial infarction.</b> <b>Non-ST-elevation acute coronary syndrome = unstable angina + non-ST-elevation myocardial infarction</b>; a biochemical marker separates angina from infarction."],
 ["Clot, step by step","Plaque under a fibrous cap &rarr; <b>spontaneous or procedural (balloon) injury</b> leaves injured endothelium &rarr; platelet <b>adhesion, activation, aggregation</b> &rarr; fibrin strands &rarr; <b>occlusive thrombus</b>."],
 ["&#9733; Thrombin is the link","<b>The two factors to know: X and II (thrombin).</b> Collagen exposure &rarr; <b>adenosine diphosphate and thromboxane A2</b> activate platelets. <b>Tissue factor</b> starts the cascade: prothrombin &rarr; thrombin &rarr; fibrinogen to fibrin."],
 ["Three phases","<b>Initiation</b>: tissue factor with factor VIIa activates X and IX, a little thrombin. <b>Amplification</b>: thrombin activates platelets and factors V and VIII; complexes assemble on platelets. <b>Propagation</b>: more thrombin, fibrin, clot stabilization."],
 ["Goals","Restore coronary flow &middot; relieve chest pain &middot; prevent infarction &middot; prevent heart failure &middot; prevent death."],
 ["&#9733; Aspirin","Give at <b>first signs of chest pain, chew and swallow</b>. Lowers mortality and reinfarction. <b>Contraindicated: allergy, recent gastrointestinal bleed, recent intracranial hemorrhage.</b>"],
 ["&#9733; Nitrates","Sublingual, then <b>intravenous</b> infusion in hospital. <b>Relieve pain ONLY: no mortality benefit.</b> Hypotension, headache, reflex tachycardia. Avoid with hypotension or phosphodiesterase inhibitors."],
 ["&#9733; Beta blockers","<b>Intravenous first, then oral.</b> Reduce <b>early and late mortality</b>, infarct size, heart failure and sudden cardiac death (course answer). <b>Caution: bradycardia or hypotension, heart block, severe reactive airway disease.</b> (FLAG: current guidelines favor oral in the first 24 hours, avoid the intravenous route with heart failure or shock risk, and rest the benefit mainly on long-term use after infarction.)"],
 ["&#9733; Morphine","Opioid for chest pain <b>not relieved by nitrates</b>; used in ST-elevation myocardial infarction; <b>may raise mortality in unstable angina and non-ST-elevation myocardial infarction</b>; controversial. Hypotension, allergy."],
]},
{"id":"mi-lytics","label":"Acute coronary syndrome &middot; fibrinolytics &amp; antithrombotics","color":"#3d6b52","rows":[
 ["System","<b>Plasminogen &rarr; plasmin</b> (by tissue plasminogen activator) &rarr; plasmin lyses <b>fibrin</b> (and fibrinogen). Brakes: plasminogen activator inhibitor-1 and -2, alpha-2 antiplasmin, thrombin-activatable fibrinolysis inhibitor."],
 ["&#9733; Mechanisms (learn the picture)","<b>Streptokinase</b> (the drug is low priority; the picture is not) forms a stable <b>1:1 complex with plasminogen</b> that converts more plasminogen to plasmin. <b>Alteplase (tissue plasminogen activator)</b> acts on <b>fibrin-bound plasminogen</b>. Reteplase and tenecteplase behave like it."],
 ["&#9733; Agents","The three main ones are very similar (provider preference, formulary; all costly, all allergy and bleeding), and all three favor <b>clot-bound plasminogen</b> (reteplase less than alteplase, see the flag). <b>Alteplase (Activase)</b> is very expensive. <b>Tenecteplase (TNKase)</b> has substituted amino acids. Reteplase and tenecteplase: <b>longer half-life</b> than alteplase. The slide says both resist plasminogen activator inhibitor-1, but that is established for tenecteplase only."],
 ["FLAG: three slide errors","Fibrin affinity: <b>true for tenecteplase, FALSE for reteplase</b> (less than alteplase). Factor list (II, V, VII) for plasmin: do not learn. Fever, chills, rash &ldquo;with streptokinase and urokinase&rdquo;: <b>only streptokinase is antigenic</b>."],
 ["&#9733; Adverse effects","<b>Bleeding is the big one</b> (including intracranial hemorrhage), allergic reactions, <b>anaphylaxis</b>, ventricular arrhythmias. Fever, chills, rash = streptokinase."],
 ["&#9733; Nine contraindications (the checklist)","Recent <b>surgery or trauma</b> &middot; serious <b>gastrointestinal bleeding</b> &middot; severe <b>hypertension</b> &middot; <b>active bleeding or bleeding disorder</b> &middot; prior <b>stroke</b> (firm for hemorrhagic or recent ischemic stroke) or <b>intracranial tumor</b> &middot; <b>aortic dissection</b> &middot; <b>acute pericarditis</b> &middot; <b>prior streptokinase exposure or allergy</b> &middot; <b>pregnancy</b> (a relative contraindication in current guidance). Mostly anything that could bleed; the exception is prior streptokinase exposure or allergy, which bars streptokinase only."],
 ["&#9733; Indication","<b>ST-elevation myocardial infarction</b> within 12 hours of symptom onset (the slide adds an age limit, an older cut-off). <b>NOT recommended in non-ST-elevation acute coronary syndrome.</b> Few patients receive them; main risk bleeding."],
 ["&#9733; Other antithrombotics","<b>Glycoprotein IIb/IIIa inhibitors</b>: not routine before percutaneous coronary intervention. <b>P2Y12 receptor antagonists</b>: before intervention and with <b>stents</b>. <b>Heparins</b>: with fibrinolysis or antiplatelets."],
 ["&#9733; Non-ST-elevation acute coronary syndrome","Early care like ST-elevation myocardial infarction, BUT <b>fibrinolytics NOT recommended (bleeding outweighs benefit)</b>; <b>enoxaparin preferred over unfractionated heparin</b> (older studies; either is accepted today); glycoprotein IIb/IIIa inhibitors more common."],
]},
]


# ---------------------------------------------------------------------------
# No-abbreviations rule, applied mechanically (same as _pharm_e2_cram_l5l7.py):
# the FIRST use of each abbreviation inside a topic block becomes
# "ABBR (full term)". Most terms above are already written in full; this is the
# safety net for any that slipped through, and it leaves names like P2Y12 alone.
import re as _re
ABBR = {
    "ST": "ST segment", "NTG": "nitroglycerin", "EMS": "emergency medical services",
    "PCI": "percutaneous coronary intervention", "CABG": "coronary artery bypass grafting",
    "ACE": "angiotensin-converting enzyme", "DHP": "dihydropyridine",
    "NDHP": "non-dihydropyridine", "CCB": "calcium channel blocker", "BB": "beta blocker",
    "MI": "myocardial infarction", "STEMI": "ST-elevation myocardial infarction",
    "NSTEMI": "non-ST-elevation myocardial infarction", "tPA": "tissue plasminogen activator",
    "CYP3A4": "cytochrome P450 3A4", "AV": "atrioventricular", "LV": "left ventricular",
    "PDE5": "phosphodiesterase type 5", "cGMP": "cyclic guanosine monophosphate",
    "IHD": "ischemic heart disease", "CHD": "coronary heart disease",
}
# "ST" alone is part of the names ST-elevation / ST segment, so it is excluded from
# mechanical expansion; "CYP3A4" is already written with its full term where used.
for _k in ("ST", "CYP3A4"):
    ABBR.pop(_k)


def _expand(topic):
    seen = set()
    keys = sorted(ABBR, key=len, reverse=True)
    pat = _re.compile(r"(?<![\w/-])(" + "|".join(_re.escape(k) for k in keys) + r")(?![\w/-])")
    for row in topic["rows"]:
        for j in (0, 1):
            parts = _re.split(r"(<[^>]+>)", row[j])
            for n, part in enumerate(parts):
                if part.startswith("<"):
                    continue
                def sub(m):
                    k = m.group(1)
                    if k in seen:
                        return k
                    seen.add(k)
                    return "%s (%s)" % (k, ABBR[k])
                parts[n] = pat.sub(sub, part)
            row[j] = "".join(parts)


for _t in T:
    _expand(_t)
