# -*- coding: utf-8 -*-
"""Arcade decks for Pharmacology I Exam 2, Lecture 8 (myocardial ischemia), drafted 2026-09-30.

Imported by add_pharm_e2_arcade.py, which appends these to its other Exam 2
DECKS. One deck per quiz topic (antianginal drugs; acute coronary syndrome and
fibrinolytics), atomic question -> short answer cards per [[arcade_content_policy]],
deck facts only, no doses, US spelling, abbreviations written out.

Weighting follows Dr. McInnis: indications, patient education, adverse effects
and contraindications over mechanism. Deliberately NOT keyed (known deck
conflicts or excluded numbers): fibrin affinity of reteplase and tenecteplase,
urokinase as an antigen, the plasmin factor list, the contested comorbidity-table
cells, "aspirin and clopidogrel increase coronary flow", the fibrinolytic
time/age/percentage figures, and every dose or strength.

NOT YET IN arcade.js: the integrator runs `python3 tools/add_pharm_e2_arcade.py`.
"""

ANGINA_ICON = ('<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>'
               '<path d="M7 12h3l1.5-3 2 5 1.5-2h2"/>')
ACS_ICON = ('<path d="M3 12h4l2-6 4 12 2-6h6"/>')

DECKS = [
 ("pharm-mi-antianginal", "Antianginal Drugs", "accent1", ANGINA_ICON, [
  ("Which three drug classes are the antianginals?", "Beta blockers, calcium channel blockers and nitrates."),
  ("Which measure of physical function do antianginals improve?", "Exercise capacity."),
  ("Which antianginal class is first line when nothing contraindicates it?", "Beta blockers."),
  ("Which two beta blockers are beta-1 selective?", "Metoprolol and atenolol."),
  ("Which two beta blockers are non-selective?", "Propranolol and nadolol."),
  ("Which two beta blockers are third generation?", "Carvedilol and labetalol."),
  ("A heart rate below what value contraindicates a beta blocker?", "Sixty beats per minute."),
  ("Which conduction block contraindicates beta blockers?", "Atrioventricular block."),
  ("Which heart failure state contraindicates beta blockers?", "Acute decompensated heart failure."),
  ("Which lung condition calls for caution with beta blockers?", "Reactive airway disease."),
  ("Which metabolic adverse effects do beta blockers cause?", "Hyperglycemia and dyslipidemia."),
  ("Which leg symptom can beta blockers worsen?", "Claudication."),
  ("Which sleep-related adverse effect do beta blockers cause?", "Nightmares."),
  ("What must a patient never do with a beta blocker?", "Stop it abruptly."),
  ("Which two symptoms are patients warned about on beta blockers?", "Dizziness and fatigue."),
  ("Which two calcium channel blockers are non-dihydropyridines?", "Diltiazem and verapamil."),
  ("Which three calcium channel blockers are dihydropyridines?", "Nifedipine, amlodipine and felodipine."),
  ("Which calcium channel blocker subclass slows heart rate and is first when beta blockers cannot be used?", "Non-dihydropyridines."),
  ("Which subclass is added to a beta blocker?", "Dihydropyridines."),
  ("Which calcium channel blocker is avoided in angina in its short-acting form?", "Nifedipine."),
  ("Which subclass is contraindicated with a low ejection fraction?", "Non-dihydropyridines."),
  ("Which adverse effects do dihydropyridines cause?", "Headache, flushing and peripheral edema."),
  ("Which bowel effect are calcium channel blocker patients warned about?", "Constipation."),
  ("Which angina type do calcium channel blockers relieve by stopping spasm?", "Vasospastic (variant) angina."),
  ("Which class is avoided in variant angina?", "Beta blockers."),
  ("Which two classes reduce variant angina symptoms?", "Calcium channel blockers and nitrates."),
  ("Which drug gives acute relief of an angina attack?", "Short-acting nitroglycerin."),
  ("Which angina can short-acting nitrates prevent when taken beforehand?", "Effort-induced angina."),
  ("Chest pain persists five minutes after the first nitroglycerin. What is done?", "Call emergency services."),
  ("How should nitroglycerin tablets be stored?", "In the original container, in a cool, dry place."),
  ("When are opened nitroglycerin tablets replaced under the older rule?", "Three to six months after opening."),
  ("Which effect of nitroglycerin are patients warned about?", "Orthostatic hypotension."),
  ("Which two oral nitrates are long-acting?", "Isosorbide mononitrate and isosorbide dinitrate."),
  ("Which antianginal class is not recommended alone?", "Long-acting nitrates."),
  ("Why is a nitrate-free interval built in?", "To prevent tolerance."),
  ("How is a nitroglycerin patch worn?", "Twelve hours on, twelve hours off."),
  ("When is the nitrate-free interval scheduled?", "When symptoms are least frequent."),
  ("Which heart rate effect can long-acting nitrates cause?", "Reflex tachycardia."),
  ("Which two conditions are avoided with nitrates because of hypotension risk?", "Aortic valve stenosis and obstructive cardiomyopathy."),
  ("Which drug class must never be combined with nitrates?", "Phosphodiesterase type 5 inhibitors such as sildenafil."),
  ("What can nitrates plus sildenafil cause?", "Hypotension, myocardial infarction or stroke."),
  ("Which drug class does not relieve angina but may slow coronary artery disease?", "Angiotensin-converting enzyme inhibitors."),
  ("Which antiplatelet drug is for every patient with ischemic heart disease unless contraindicated?", "Aspirin."),
  ("Which antiplatelet replaces aspirin in aspirin allergy?", "Clopidogrel."),
 ]),
 ("pharm-mi-acs", "ACS (Acute Coronary Syndrome) &amp; Fibrinolytics", "accent2", ACS_ICON, [
  ("Which two main forms of acute coronary syndrome exist?", "ST-elevation myocardial infarction and non-ST-elevation acute coronary syndrome."),
  ("Which conditions make up non-ST-elevation acute coronary syndrome?", "Unstable angina and non-ST-elevation myocardial infarction."),
  ("What does the electrocardiogram show in ST-elevation myocardial infarction?", "ST-segment elevation."),
  ("What separates unstable angina from myocardial infarction?", "A biochemical marker."),
  ("Which drug is taken at the first sign of acute coronary syndrome chest pain?", "Aspirin."),
  ("How is aspirin taken in acute coronary syndrome?", "Chewed and swallowed."),
  ("What does aspirin reduce in acute coronary syndrome?", "Mortality and reinfarction."),
  ("Which three problems contraindicate aspirin?", "Allergy, recent gastrointestinal bleeding and recent intracranial hemorrhage."),
  ("Why are nitrates used in acute coronary syndrome?", "Relief of chest pain."),
  ("Which antianginal class relieves chest pain in acute coronary syndrome without a mortality benefit?", "Nitrates."),
  ("Which nitrate route is used once the patient reaches the hospital?", "Intravenous infusion."),
  ("Which adverse effects do nitrates cause in acute coronary syndrome?", "Hypotension, headache and reflex tachycardia."),
  ("Which size measure do beta blockers reduce in acute coronary syndrome?", "Infarct size."),
  ("Which conduction problem is a caution for beta blockers in acute coronary syndrome?", "Heart block."),
  ("Which lung condition is a caution for beta blockers in acute coronary syndrome?", "Severe reactive airway disease."),
  ("Which opioid treats chest pain unresponsive to nitrates?", "Morphine."),
  ("Which blood pressure effect can morphine cause?", "Hypotension."),
  ("In which forms of acute coronary syndrome may morphine raise mortality?", "Unstable angina and non-ST-elevation myocardial infarction."),
  ("Which molecule links tissue injury, coagulation and platelets?", "Thrombin."),
  ("What do fibrinolytics convert plasminogen into?", "Plasmin."),
  ("Which fibrinolytic forms a stable complex with plasminogen?", "Streptokinase."),
  ("Which three agents are recombinant tissue plasminogen activators?", "Alteplase, reteplase and tenecteplase."),
  ("Which two agents outlast alteplase in half-life?", "Reteplase and tenecteplase."),
  ("Which form of acute coronary syndrome are fibrinolytics indicated for?", "ST-elevation myocardial infarction."),
  ("Are fibrinolytics recommended in non-ST-elevation acute coronary syndrome?", "No."),
  ("Why are fibrinolytics avoided in non-ST-elevation acute coronary syndrome?", "Bleeding risk outweighs benefit."),
  ("What is the main adverse effect of fibrinolytics?", "Bleeding."),
  ("Which brain complication do fibrinolytics risk?", "Intracranial hemorrhage."),
  ("Which fibrinolytic commonly causes fever, chills and rash?", "Streptokinase."),
  ("Which heart rhythm problem can fibrinolytics cause?", "Ventricular arrhythmias."),
  ("Which severe allergic reaction can fibrinolytics cause?", "Anaphylaxis."),
  ("Which past streptokinase history contraindicates giving streptokinase again?", "Earlier exposure or an allergic reaction."),
  ("Which bleeding status contraindicates fibrinolytics?", "Active bleeding or a hemorrhagic disorder."),
  ("Which intracranial finding contraindicates fibrinolytics?", "An active intracranial process such as a tumor."),
  ("Which aortic condition contraindicates fibrinolytics?", "Aortic dissection."),
  ("Which pericardial condition contraindicates fibrinolytics?", "Acute pericarditis."),
  ("Which reproductive state contraindicates fibrinolytics?", "Pregnancy."),
  ("Which recent digestive tract problem contraindicates fibrinolytics?", "Serious gastrointestinal bleeding."),
  ("Which class is not routinely given before percutaneous coronary intervention?", "Glycoprotein IIb/IIIa inhibitors."),
  ("Which drug class is used before stenting and to prevent clots with a stent?", "P2Y12 receptor antagonists."),
  ("What are heparins given alongside?", "Fibrinolysis or antiplatelet agents."),
  ("Which low-molecular-weight heparin was preferred over unfractionated heparin in studies of non-ST-elevation acute coronary syndrome?", "Enoxaparin."),
 ]),
]
