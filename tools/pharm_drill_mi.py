# -*- coding: utf-8 -*-
"""Rapid-drill bank: drugs for myocardial ischemia (Lecture 8, Myocardial Ischemia Drugs.pptx).

One fact, four names, no doses. One drug per choice; a class name is offered only
when the stem itself asks for a class, and then every choice is a class. Every
wrong choice is another real agent (or class) from the same family: other
antianginals, other antiplatelets and anticoagulants, other fibrinolytics.

Left out on purpose (Jaxon's standing rules, 2026-09-30 brief):
  * every milligram dose (aspirin 325 mg, nitroglycerin ointment inches);
  * urokinase antigenicity (only streptokinase is antigenic, slide 62 is wrong);
  * fibrin affinity of reteplase (slide 64 is wrong for reteplase);
  * the plasmin "factors II, V, VII" list, the fibrinolytic percentages and day
    counts, and the contested cells of the comorbidity table (slide 34):
    only the uncontested cells are asked (asthma, bradycardia or atrioventricular
    block, decreased left-ventricular function). Also out: the old "intravenous then
    oral" beta blocker route (current practice is oral first), any "only fibrin-bound"
    claim about reteplase, and "enoxaparin preferred over heparin" as a key (older
    studies only).
"""
ITEMS = [
# ---- beta blockers ----
dict(q="Which drug class is first-line antianginal therapy when there are no contraindications?",
     ans="Beta blockers", src=("MI", 17),
     why="Beta blockers are the first-line antianginal therapy in the absence of contraindications.",
     wrong=[("Calcium channel blockers", "Calcium channel blockers are initial therapy only when beta blockers are contraindicated or not tolerated."),
            ("Long-acting nitrates", "Long-acting nitrates are initial therapy only when both beta blockers and calcium channel blockers are contraindicated or not tolerated."),
            ("Angiotensin-converting enzyme inhibitors", "Angiotensin-converting enzyme inhibitors do not relieve angina symptoms; they may only help prevent progression of coronary artery disease.")]),

dict(q="Which beta blocker belongs to the third generation of agents?",
     ans="Carvedilol", src=("MI", 17),
     why="Carvedilol and labetalol are the third-generation beta blockers.",
     wrong=[("Metoprolol", "Metoprolol is a beta-1 selective agent; the third-generation beta blockers are carvedilol and labetalol."),
            ("Propranolol", "Propranolol is a non-selective beta blocker, not a third-generation agent; carvedilol and labetalol are third generation."),
            ("Atenolol", "Atenolol is a beta-1 selective agent, not a third-generation one; carvedilol and labetalol are the third-generation agents.")]),

dict(q="Which drug is non-cardioselective, so it is avoided in patients with asthma?",
     ans="Propranolol", src=("MI", 34),
     why="Non-cardioselective beta blockers such as propranolol are to be avoided in asthma.",
     wrong=[("Metoprolol", "Metoprolol is cardioselective, so it is the type that may be used with caution in asthma rather than the non-cardioselective type to avoid."),
            ("Atenolol", "Atenolol is cardioselective, so it is the type that may be used with caution in asthma rather than the non-cardioselective type to avoid."),
            ("Verapamil", "Verapamil is a non-dihydropyridine calcium channel blocker, a first-line choice in asthma rather than an agent to avoid.")]),

dict(q="Which antianginal carries the warning to avoid rapid discontinuation?",
     ans="Metoprolol", src=("MI", 19),
     why="Patients taking a beta blocker such as metoprolol are taught to avoid rapid discontinuation.",
     wrong=[("Amlodipine", "Amlodipine is a dihydropyridine whose listed adverse effects are headache, flushing and peripheral edema, not a rapid-discontinuation warning."),
            ("Isosorbide mononitrate", "Isosorbide mononitrate is a long-acting nitrate whose adverse reactions are headache, flushing, postural hypotension and reflex tachycardia, not a rapid-discontinuation warning."),
            ("Verapamil", "Verapamil's education points are dizziness and constipation; the rapid-discontinuation warning belongs to beta blockers.")]),

dict(q="Which drug can cause nightmares, sexual dysfunction and worsened claudication?",
     ans="Propranolol", src=("MI", 19),
     why="Beta blockers such as propranolol cause fatigue, sexual dysfunction, nightmares and worsened claudication.",
     wrong=[("Amlodipine", "Amlodipine's typical adverse effects are headache, flushing and peripheral edema, not nightmares or worsened claudication."),
            ("Isosorbide dinitrate", "Isosorbide dinitrate causes headache, flushing, postural hypotension and reflex tachycardia, not nightmares or worsened claudication."),
            ("Diltiazem", "Diltiazem's adverse effects center on hypotension, with heart rate monitoring; nightmares and worsened claudication belong to beta blockers.")]),

# ---- calcium channel blockers ----
dict(q="Which calcium channel blocker slows atrioventricular conduction the most?",
     ans="Verapamil", src=("MI", 21),
     why="Verapamil shows the largest fall in atrioventricular conduction, along with lower heart rate and contractility.",
     wrong=[("Nifedipine", "Nifedipine is a dihydropyridine that mainly dilates vessels; its atrioventricular conduction is unchanged."),
            ("Amlodipine", "Amlodipine is a dihydropyridine with strong vasodilation; its atrioventricular conduction and heart rate are unchanged."),
            ("Felodipine", "Felodipine is a dihydropyridine that dilates vessels and leaves atrioventricular conduction unchanged.")]),

dict(q="Which calcium channel blocker dilates vessels strongly without changing heart rate or atrioventricular conduction?",
     ans="Amlodipine", src=("MI", 21),
     why="Amlodipine gives strong vasodilation with heart rate and atrioventricular conduction unchanged.",
     wrong=[("Nifedipine", "Nifedipine dilates vessels strongly but raises heart rate, unlike amlodipine, which leaves heart rate unchanged."),
            ("Verapamil", "Verapamil dilates vessels less and lowers heart rate and atrioventricular conduction, unlike amlodipine, which leaves both unchanged."),
            ("Diltiazem", "Diltiazem dilates vessels less and lowers heart rate and atrioventricular conduction, unlike amlodipine.")]),

dict(q="Which calcium channel blocker should be avoided in its short-acting form?",
     ans="Nifedipine", src=("MI", 22),
     why="Short-acting agents are to be avoided, and nifedipine is the example named.",
     wrong=[("Amlodipine", "Amlodipine is the dihydropyridine offered as the alternative in decreased left ventricular function; the short-acting warning names nifedipine."),
            ("Verapamil", "Verapamil is a non-dihydropyridine used for initial therapy when beta blockers are not tolerated; the short-acting warning names nifedipine."),
            ("Diltiazem", "Diltiazem is a non-dihydropyridine used when beta blockers are contraindicated; the short-acting warning names nifedipine.")]),

dict(q="Which drug class slows heart rate and is the preferred initial therapy when beta blockers are contraindicated or not tolerated?",
     ans="Non-dihydropyridines", src=("MI", 22),
     why="Non-dihydropyridines are the initial therapy when beta blockers cannot be used; dihydropyridines are added to a beta blocker.",
     wrong=[("Dihydropyridines", "Dihydropyridines dilate vessels without slowing heart rate or conduction; they are the class added to a beta blocker, not the rate-lowering substitute for one."),
            ("Long-acting nitrates", "Long-acting nitrates raise heart rate and are initial therapy only when both beta blockers and calcium channel blockers are contraindicated or not tolerated."),
            ("Short-acting nitrates", "Short-acting nitrates relieve acute symptoms and raise heart rate rather than slowing it; they are not the initial rate-lowering substitute.")]),

dict(q="Which drug class is listed as contraindicated with a heart rate below 60 beats per minute, acute heart failure or an ejection fraction below 40 percent?",
     ans="Non-dihydropyridines", src=("MI", 23),
     why="Low heart rate, acute heart failure and low ejection fraction are contraindications for the non-dihydropyridines.",
     wrong=[("Dihydropyridines", "The heart rate and ejection fraction limits are listed for non-dihydropyridines; dihydropyridines do not slow the heart, and amlodipine is the option in reduced left ventricular function."),
            ("Long-acting nitrates", "Long-acting nitrates are avoided in aortic valve stenosis, obstructive cardiomyopathy and with phosphodiesterase type 5 inhibitors, not by these limits."),
            ("Angiotensin-converting enzyme inhibitors", "Angiotensin-converting enzyme inhibitors are used indefinitely in left ventricular dysfunction, so these limits do not apply.")]),

# ---- nitrates ----
dict(q="Which drug is placed under the tongue or sprayed for acute relief of angina?",
     ans="Nitroglycerin", src=("MI", 27),
     why="Short-acting nitroglycerin, as a sublingual tablet or spray, relieves acute symptoms and prevents effort-induced angina.",
     wrong=[("Isosorbide mononitrate", "Isosorbide mononitrate is a long-acting nitrate that lasts about 12 hours and is dosed daily, not the acute-relief drug."),
            ("Amlodipine", "Amlodipine is a calcium channel blocker used as daily preventive therapy, not an under-the-tongue drug for acute pain."),
            ("Metoprolol", "Metoprolol is a beta blocker used as preventive therapy, not a sublingual drug for acute pain.")]),

dict(q="Which drug must never be combined with nitrates because the result can be severe hypotension, myocardial infarction or stroke?",
     ans="Sildenafil", src=("MI", 33),
     why="Sildenafil, tadalafil and vardenafil inhibit phosphodiesterase type 5 and must not be used with nitrates.",
     wrong=[("Metoprolol", "Beta blockers are combined with nitrates when a single antianginal is not enough, with no phosphodiesterase warning."),
            ("Amlodipine", "Dihydropyridines are combined with long-acting nitrates for angina, so they do not carry this warning."),
            ("Diltiazem", "Non-dihydropyridines are combined with long-acting nitrates for angina, so they do not carry this warning.")]),

dict(q="Which drug class blocks phosphodiesterase type 5, the enzyme that breaks down cyclic guanosine monophosphate, making its combination with nitrates dangerous?",
     ans="Phosphodiesterase inhibitors", src=("MI", 26),
     why="Sildenafil, tadalafil and vardenafil inhibit phosphodiesterase type 5, which breaks down cyclic guanosine monophosphate.",
     wrong=[("Calcium channel blockers", "Calcium channel blockers block calcium entry and are combined with long-acting nitrates for angina and carry no dangerous interaction."),
            ("Cardioselective beta blockers", "Cardioselective beta blockers block beta-1 receptors and can be combined with nitrates for persistent angina."),
            ("Angiotensin-converting enzyme inhibitors", "Angiotensin-converting enzyme inhibitors do not break down cyclic guanosine monophosphate or endanger nitrate therapy.")]),

dict(q="Which drug class is avoided in aortic valve stenosis and obstructive cardiomyopathy because of the risk of hypotension?",
     ans="Nitrates", src=("MI", 33),
     why="Aortic valve stenosis and obstructive cardiomyopathy are listed nitrate contraindications because of hypotension; phosphodiesterase type 5 inhibitors are the other.",
     wrong=[("Beta blockers", "Beta blocker contraindications are heart rate below 60, systolic pressure below 100, atrioventricular block and acute decompensated heart failure."),
            ("Calcium channel blockers", "Calcium channel blocker contraindications are systolic pressure below 100 mmHg and atrioventricular block, not these valve and muscle diseases."),
            ("Fibrinolytics", "Fibrinolytics are contraindicated by bleeding risks such as active bleeding and aortic dissection, not by these conditions.")]),

dict(q="Which drug class is worn as a patch or ointment 12 hours on and 12 hours off to limit tolerance?",
     ans="Long-acting nitrates", src=("MI", 31),
     why="Long-acting nitrate patches and ointment follow a 12-hours-on, 12-hours-off schedule to limit tachyphylaxis.",
     wrong=[("Beta blockers", "Beta blockers are managed by avoiding rapid discontinuation, not by a scheduled drug-free interval."),
            ("Calcium channel blockers", "Calcium channel blockers carry dizziness and constipation education, with no scheduled drug-free interval."),
            ("Antiplatelet drugs", "Antiplatelet drugs such as aspirin are given to prevent acute coronary syndrome, with no scheduled drug-free interval.")]),

# ---- vasculoprotective drugs ----
dict(q="Which drug class does NOT relieve angina symptoms but may help prevent progression of coronary artery disease?",
     ans="Angiotensin-converting enzyme inhibitors", src=("MI", 35),
     why="These inhibitors barely change myocardial oxygen consumption and do not relieve angina, but may slow coronary artery disease.",
     wrong=[("Dihydropyridine calcium channel blockers", "Dihydropyridines relieve angina by lowering systolic wall tension; angiotensin-converting enzyme inhibitors do not relieve symptoms."),
            ("Non-dihydropyridine calcium channel blockers", "Non-dihydropyridines lower heart rate and contractility and relieve angina; angiotensin-converting enzyme inhibitors do not."),
            ("Long-acting nitrates", "Long-acting nitrates prevent angina symptoms; angiotensin-converting enzyme inhibitors are the class that does not relieve them.")]),

dict(q="Which drug is recommended for patients who are allergic to aspirin?",
     ans="Clopidogrel", src=("MI", 37),
     why="Clopidogrel is as efficacious as aspirin in secondary prevention and is recommended when aspirin causes allergy.",
     wrong=[("Enoxaparin", "Enoxaparin is an anticoagulant used in non-ST-elevation acute coronary syndrome, not an antiplatelet substitute for aspirin."),
            ("Heparin", "Heparin is an anticoagulant used together with fibrinolysis or antiplatelet agents, not the aspirin substitute."),
            ("Alteplase", "Alteplase is a fibrinolytic that dissolves an existing clot, not an antiplatelet used to prevent acute coronary syndrome.")]),

# ---- acute coronary syndrome ----
dict(q="Which drug is chewed and swallowed at the first signs of chest pain in acute coronary syndrome?",
     ans="Aspirin", src=("MI", 52),
     why="Aspirin is chewed and swallowed at the first signs of chest pain and reduces mortality and reinfarction.",
     wrong=[("Clopidogrel", "Clopidogrel is the substitute for people allergic to aspirin, not the drug chewed at the first signs of chest pain."),
            ("Nitroglycerin", "Nitroglycerin under the tongue relieves chest pain but does not improve outcomes; aspirin is the one chewed and swallowed."),
            ("Metoprolol", "Metoprolol is a beta blocker that reduces infarct size and sudden cardiac death; it is not the drug chewed at the first signs of chest pain.")]),

dict(q="Which drug is contraindicated by allergy, a recent gastrointestinal bleed or a recent intracranial hemorrhage?",
     ans="Aspirin", src=("MI", 53),
     why="Allergy, recent gastrointestinal bleeding and recent intracranial hemorrhage are the aspirin contraindications.",
     wrong=[("Nitroglycerin", "Nitroglycerin is contraindicated by hypotension and phosphodiesterase inhibitors, not by these bleeding problems."),
            ("Metoprolol", "Metoprolol calls for caution with bradycardia, hypotension, heart block and severe reactive airway disease, not bleeding."),
            ("Verapamil", "Verapamil is contraindicated by heart rate below 60, acute heart failure and low ejection fraction, not by these problems.")]),

dict(q="Which drug used in acute coronary syndrome relieves chest pain but shows no mortality benefit?",
     ans="Nitroglycerin", src=("MI", 54),
     why="Nitrates give only relief of chest pain, with no mortality benefit.",
     wrong=[("Aspirin", "Aspirin reduces mortality and reinfarction, unlike nitrates, which only relieve chest pain."),
            ("Metoprolol", "Beta blockers have outcome benefits, with smaller infarcts and less sudden cardiac death, unlike nitrates, which only relieve pain."),
            ("Alteplase", "Alteplase is a fibrinolytic that reestablishes coronary blood flow; it is not a drug used only for chest pain relief.")]),

dict(q="Which drug is added for chest pain that does not respond to nitrates in ST-elevation myocardial infarction?",
     ans="Morphine", src=("MI", 56),
     why="Morphine, an opioid analgesic, manages chest pain unresponsive to nitrates in ST-elevation myocardial infarction.",
     wrong=[("Nitroglycerin", "Nitroglycerin is the first drug for relieving the pain; morphine is added only when pain does not respond to nitrates."),
            ("Aspirin", "Aspirin is an antiplatelet that reduces mortality and reinfarction, not an analgesic for pain unresponsive to nitrates."),
            ("Metoprolol", "Metoprolol is a beta blocker that reduces infarct size; it is not an opioid analgesic for pain unresponsive to nitrates.")]),

# ---- fibrinolytics and other antithrombotic agents ----
dict(q="Which fibrinolytic forms a stable 1:1 complex with plasminogen to convert it to plasmin?",
     ans="Streptokinase", src=("MI", 59),
     why="Streptokinase forms a stable 1:1 complex with plasminogen, exposing the catalytic site that makes plasmin.",
     wrong=[("Alteplase", "Alteplase is a tissue plasminogen activator that acts on plasminogen bound to fibrin rather than forming a complex with it."),
            ("Reteplase", "Reteplase is a recombinant tissue plasminogen activator that activates plasminogen directly; it does not work by forming a 1:1 complex with plasminogen."),
            ("Tenecteplase", "Tenecteplase is a recombinant tissue plasminogen activator variant that activates plasminogen directly, not through a 1:1 complex.")]),

dict(q="Which fibrinolytic causes fever, chills and skin rash, making prior exposure a reason to avoid it?",
     ans="Streptokinase", src=("MI", 62),
     why="Fever, chills and rash occur mainly with streptokinase, and prior exposure or an allergic reaction to it contraindicates reuse.",
     wrong=[("Alteplase", "Alteplase is a recombinant tissue plasminogen activator; fever, chills and rash occur mainly with streptokinase."),
            ("Reteplase", "Reteplase is a recombinant agent made in Escherichia coli; fever, chills and rash occur mainly with streptokinase."),
            ("Tenecteplase", "Tenecteplase is a recombinant tissue plasminogen activator variant; fever, chills and rash occur mainly with streptokinase.")]),

dict(q="Which fibrinolytic is a recombinant protein made in Escherichia coli cells?",
     ans="Reteplase", src=("MI", 64),
     why="Reteplase (Retavase) is produced recombinantly in Escherichia coli cells.",
     wrong=[("Alteplase", "Alteplase is made by recombinant deoxyribonucleic acid technology in Chinese hamster ovary cells, not in Escherichia coli."),
            ("Tenecteplase", "Tenecteplase is made in Chinese hamster ovary cells with substituted amino acids, not in Escherichia coli."),
            ("Streptokinase", "Streptokinase works by forming a complex with plasminogen and is not the recombinant Escherichia coli product.")]),

dict(q="Which fibrinolytic is the tissue plasminogen activator sold as Activase?",
     ans="Alteplase", src=("MI", 64),
     why="Alteplase (Activase) is the recombinant tissue plasminogen activator that directly activates fibrin-bound plasminogen.",
     wrong=[("Reteplase", "Reteplase is sold as Retavase and is a recombinant agent made in Escherichia coli, not as Activase."),
            ("Tenecteplase", "Tenecteplase is sold as TNKase and has substituted amino acids and a longer half-life, not the Activase brand."),
            ("Streptokinase", "Streptokinase acts by forming a complex with plasminogen and is not the recombinant tissue plasminogen activator.")]),

dict(q="Which drug class is contraindicated by aortic dissection and by serious head or facial trauma?",
     ans="Fibrinolytics", src=("MI", 63),
     why="Aortic dissection and serious head or facial trauma are among the fibrinolytic contraindications.",
     wrong=[("Nitrates", "Nitrates are avoided in aortic valve stenosis, obstructive cardiomyopathy and with phosphodiesterase type 5 inhibitors."),
            ("Beta blockers", "Beta blockers are contraindicated by low heart rate, low systolic pressure, atrioventricular block and acute decompensated heart failure."),
            ("Calcium channel blockers", "Calcium channel blockers are contraindicated by systolic pressure below 100 mmHg and atrioventricular block, among other limits.")]),

dict(q="Which drug is NOT recommended in non-ST-elevation acute coronary syndrome because bleeding risk outweighs benefit?",
     ans="Alteplase", src=("MI", 68),
     why="Fibrinolytics such as alteplase are not recommended in non-ST-elevation acute coronary syndrome.",
     wrong=[("Enoxaparin", "Enoxaparin is an anticoagulant used in non-ST-elevation acute coronary syndrome, so it is not the drug to avoid."),
            ("Aspirin", "Aspirin is part of the common therapy for both ST-elevation and non-ST-elevation acute coronary syndrome."),
            ("Nitroglycerin", "Nitroglycerin is used for chest pain relief in both ST-elevation and non-ST-elevation acute coronary syndrome.")]),

dict(q="Which platelet-directed drug class is used before percutaneous coronary intervention and as clot prophylaxis with stent placement?",
     ans="P2Y12 receptor antagonists", src=("MI", 66),
     why="P2Y12 receptor antagonists are used before percutaneous coronary intervention and as clot prophylaxis with a stent.",
     wrong=[("Glycoprotein IIb/IIIa inhibitors", "Glycoprotein IIb/IIIa inhibitors are not routinely recommended before percutaneous coronary intervention."),
            ("Heparins", "Heparins are anticoagulants rather than platelet-directed drugs; they are used together with fibrinolysis or antiplatelet agents."),
            ("Fibrinolytics", "Fibrinolytics dissolve an existing clot in ST-elevation myocardial infarction; they are not platelet-directed drugs.")]),

# ---- comorbidity and variant angina ----
dict(q="Which calcium channel blocker is the alternative to a beta blocker when left ventricular function is decreased?",
     ans="Amlodipine", src=("MI", 34),
     why="With decreased left ventricular function, a beta blocker is first line and amlodipine is the calcium channel blocker alternative.",
     wrong=[("Verapamil", "Verapamil is a non-dihydropyridine, contraindicated with acute heart failure or an ejection fraction below 40 percent."),
            ("Diltiazem", "Diltiazem is a non-dihydropyridine, contraindicated with acute heart failure or an ejection fraction below 40 percent."),
            ("Nifedipine", "Nifedipine is among the other calcium channel blockers avoided here; amlodipine is the one alternative.")]),

dict(q="Which drug class is first line for angina in a patient with bradycardia or atrioventricular block?",
     ans="Dihydropyridines", src=("MI", 34),
     why="With bradycardia or atrioventricular block, dihydropyridines are first line and long-acting nitrates the alternative.",
     wrong=[("Non-dihydropyridines", "Non-dihydropyridines slow heart rate and atrioventricular conduction, so they are avoided in bradycardia or block."),
            ("Beta blockers", "Beta blockers lower heart rate and slow atrioventricular conduction, so they are avoided in bradycardia or block."),
            ("Antiplatelet drugs", "Antiplatelet drugs such as aspirin prevent acute coronary syndrome and are not antianginals; dihydropyridines are the first-line class here.")]),

dict(q="Which antianginal's patient education includes a warning about constipation?",
     ans="Verapamil", src=("MI", 24),
     why="Education for calcium channel blockers such as verapamil includes dizziness and constipation.",
     wrong=[("Metoprolol", "Metoprolol's education is to avoid rapid discontinuation and expect dizziness and fatigue, not constipation."),
            ("Nitroglycerin", "Nitroglycerin's education covers orthostatic hypotension and applying it under the tongue, not constipation."),
            ("Isosorbide mononitrate", "Isosorbide mononitrate's adverse effects are headache, flushing, postural hypotension and reflex tachycardia, not constipation.")]),

dict(q="Which drug class should be avoided in variant (Prinzmetal) angina because it may worsen symptoms?",
     ans="Beta blockers", src=("MI", 39),
     why="In variant angina, calcium channel blockers and nitrates reduce symptoms, but beta blockers may worsen them.",
     wrong=[("Calcium channel blockers", "Calcium channel blockers reduce symptoms of variant angina by relieving vasospasm, so they are not avoided."),
            ("Nitrates", "Nitrates reduce symptoms of variant angina by relieving vasospasm, so they are not avoided."),
            ("Angiotensin-converting enzyme inhibitors", "These inhibitors do not relieve angina and are not the class named to avoid; beta blockers may worsen variant angina.")]),
]
