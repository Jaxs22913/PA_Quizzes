# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- Lipids (Lecture 7), topic 1: statins and the
statin guidelines.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

SOURCE. Lipids.pptx slides 4-25 and 62-69. A few lipid-transport items sit here
because the statin mechanism is built on them (LDL receptors, ApoB-100); the
rest of the physiology was framed as setup and is de-weighted.

EMPHASIS (weight only): statins are first line ("10 times out of 10"); the
CYP3A4 substrates atorvastatin, lovastatin and simvastatin ("definitely know
these... may come up on a test") -- the cross-lecture pair with the
non-dihydropyridine CYP3A4 inhibition in Antihypertensives; the four statin
benefit groups ("I would want you to be able to identify those four"); and
atorvastatin and rosuvastatin as the only high-intensity statins.

DECK CONFLICT AVOIDED: slide 65 gives the 10-year risk threshold as >7.5% and
the algorithm on slide 66 uses >10% and 5-10%. No key depends on the threshold;
the one benefit-group item that states a risk figure uses 3%, which falls below
both.

SLIDE WINS: serious statin liver injury is "exceedingly rare" (slide 21), not
"very liver toxic" as said aloud; the baseline-and-follow-up liver test
schedule was audio-only and is not keyed. Statin plus fibrate is "cautiously"
combined (slide 22), not "usually not recommended". Rosuvastatin is "minimal
CYP", not "non-CYP".

SCOPE CAPS: from the pharmacokinetic table only the CYP row; no patient
scenario asks which intensity to choose; no 10-year risk calculation; no doses.
"""

D = "Lipids.pptx"
IO_CLASS = "Identify drug classes and commonly prescribed drugs that lower cholesterol and triglyceride levels"
IO_MOA = "Describe the molecular mechanism of action of drugs that lower cholesterol and triglyceride levels"
IO_IND = "Identify indications for commonly used drugs that lower cholesterol and triglyceride levels"
IO_ADME = "Describe absorption, distribution, metabolism, and excretion of drugs that lower cholesterol and triglyceride levels"
IO_TOX = "Summarize side effects and toxic manifestations of drugs that lower cholesterol and triglyceride levels"
IO_AE = "Describe adverse effects of drugs that lower cholesterol and triglyceride levels"
IO_CONTRA = "Identify contraindications for drugs that lower cholesterol and triglyceride levels"
IO_INTER = "Discuss potential drug-drug, drug-food, and drug-herb interactions with drugs that lower cholesterol and triglyceride levels"
IO_PROT = "List commonly used protocols and patient monitoring for drugs that lower cholesterol and triglyceride levels"
IO_EDU = "Outline appropriate patient education for drugs that lower cholesterol and triglyceride levels"

QUESTIONS = [

# ---- lipid transport the statin story rests on -----------------------------------
{"topic": "Lipid transport", "io": IO_MOA, "slot": "mechanism",
 "q": "Which lipoprotein carries dietary fat away from the intestine?",
 "opts": [
  ["Chylomicrons", "Correct. Chylomicrons are secreted by intestinal cells; lipoprotein lipase hydrolyzes their triglyceride core, and the liver removes the remnants."],
  ["Very low-density lipoprotein", "Very low-density lipoprotein (VLDL) is made by the liver from carbohydrate and fatty acids, carrying endogenous rather than dietary fat."],
  ["Low-density lipoprotein", "Low-density lipoprotein (LDL) is the product of VLDL and IDL breakdown in plasma, not the carrier of dietary fat from the gut."],
  ["High-density lipoprotein", "High-density lipoprotein (HDL) transfers cholesteryl ester to other particles and returns cholesterol to the liver; chylomicrons carry dietary fat."]],
 "c": 0, "cite": D + ", Slide 7"},

{"topic": "Lipid transport", "io": IO_MOA, "slot": "mechanism",
 "q": "Which apolipoprotein binds LDL (low-density lipoprotein) to its receptor?",
 "opts": [
  ["ApoB-100", "Correct. ApoB-100 is the only apoprotein of LDL and the ligand for the LDL receptor, which clears about 75% of LDL particles, mostly in the liver."],
  ["ApoA-I", "ApoA-I is the HDL (high-density lipoprotein) protein that fibrates increase. LDL binds its receptor through ApoB-100."],
  ["ApoC-II", "ApoC-II sits on chylomicrons and VLDL (very low-density lipoprotein); it is not LDL's receptor ligand, which is ApoB-100."],
  ["ApoE", "ApoE mediates hepatic uptake of remnants and IDL (intermediate-density lipoprotein). LDL's only apoprotein, and its receptor ligand, is ApoB-100."]],
 "c": 0, "cite": D + ", Slide 12"},

{"topic": "Lipid transport", "io": IO_MOA, "slot": "mechanism",
 "q": "What happens when LDL (low-density lipoprotein) receptor activity falls?",
 "opts": [
  ["LDL accumulates, driving atherosclerosis", "Correct. Reduced receptor activity lets LDL particles build up in plasma, which leads to atherosclerosis; most LDL-lowering classes work by raising receptor activity."],
  ["HDL accumulates, protecting arteries", "HDL (high-density lipoprotein) is not cleared by the LDL receptor. Falling receptor activity lets LDL accumulate, driving atherosclerosis."],
  ["Chylomicrons clear faster from blood", "Chylomicron remnants are cleared through a different receptor protein. Less LDL receptor activity makes LDL accumulate."],
  ["Triglycerides fall in the plasma", "The direct consequence is LDL accumulation and atherosclerosis, not a fall in triglycerides."]],
 "c": 0, "cite": D + ", Slide 12"},

# ---- mechanism, class, place in therapy ----------------------------------------
{"topic": "Statin mechanism", "io": IO_MOA, "slot": "mechanism",
 "q": "Which enzyme do statins inhibit?",
 "opts": [
  ["HMG-CoA reductase", "Correct. Statins inhibit HMG-CoA reductase in the hepatic cholesterol synthesis pathway."],
  ["Lipoprotein lipase", "Lipoprotein lipase hydrolyzes triglyceride in chylomicrons and VLDL (very low-density lipoprotein); fibrates increase it. Statins inhibit HMG-CoA reductase."],
  ["Cholesterol 7-alpha hydroxylase", "Cholesterol 7-alpha hydroxylase converts cholesterol to bile acids and rises with bile acid sequestrants. Statins inhibit HMG-CoA reductase."],
  ["PCSK9 in the plasma", "PCSK9 is the target of the monoclonal antibodies alirocumab and evolocumab. Statins inhibit HMG-CoA reductase."]],
 "c": 0, "cite": D + ", Slide 16"},

{"topic": "Statin mechanism", "io": IO_MOA, "slot": "mechanism",
 "q": "How does inhibiting hepatic cholesterol synthesis lower serum LDL (low-density lipoprotein)?",
 "opts": [
  ["It upregulates hepatic LDL receptors", "Correct. Lower intracellular cholesterol stimulates LDL receptor synthesis, increasing hepatic uptake of LDL, VLDL remnants and IDL from the circulation."],
  ["It blocks intestinal cholesterol uptake", "Blocking cholesterol absorption at the brush border is ezetimibe's mechanism. Statins work by upregulating hepatic LDL receptors."],
  ["It binds bile acids in the gut", "Binding bile acids is the bile acid sequestrant mechanism. Statins lower intracellular cholesterol, which upregulates LDL receptors."],
  ["It activates PPAR-alpha", "PPAR-alpha activation is the fibrate mechanism, lowering triglycerides. Statins raise hepatic LDL receptor numbers."]],
 "c": 0, "cite": D + ", Slide 18"},

{"topic": "Statin agents", "io": IO_CLASS, "slot": "class",
 "q": "Which of these drugs is an HMG-CoA reductase inhibitor?",
 "opts": [
  ["Pitavastatin", "Correct. The -statin suffix marks the class: lovastatin, simvastatin, pravastatin, fluvastatin, atorvastatin, rosuvastatin and pitavastatin."],
  ["Ezetimibe", "Ezetimibe is the cholesterol absorption inhibitor, acting at the intestinal brush border rather than on HMG-CoA reductase."],
  ["Gemfibrozil", "Gemfibrozil is a fibric acid derivative that activates PPAR-alpha. The HMG-CoA reductase inhibitors end in -statin."],
  ["Colesevelam", "Colesevelam is a bile acid sequestrant that binds bile acids in the gut. Statins, ending in -statin, inhibit HMG-CoA reductase."]],
 "c": 0, "cite": D + ", Slide 17"},

{"topic": "Statin place in therapy", "io": IO_IND, "slot": "indication",
 "q": "Which class is first-line therapy when LDL (low-density lipoprotein) cholesterol lowering drugs are indicated?",
 "opts": [
  ["Statins", "Correct. Statins are the most efficacious and best tolerated of all the agents and are first line when LDL-lowering drugs are indicated."],
  ["Bile acid sequestrants", "Resins are the safest (not absorbed) but poorly tolerated and used with a statin or for modest LDL reductions. Statins are first line."],
  ["Fibrates", "Fibrates are primarily for triglycerides over 1000 mg/dL or low HDL (high-density lipoprotein), not first-line LDL lowering."],
  ["Niacin", "Niacin is useful for atherogenic dyslipidemia and in combination; statins are first line for LDL lowering."]],
 "c": 0, "cite": D + ", Slide 25"},

{"topic": "Statin mechanism", "io": IO_MOA, "slot": "mechanism",
 "q": "Which is a pleiotropic effect of statins, beyond lowering cholesterol?",
 "opts": [
  ["Plaque stabilization", "Correct. Pleiotropic effects include plaque stabilization, improved endothelial function, platelet inhibition, reduced leukocyte adhesiveness and reduced inflammatory markers."],
  ["Raised triglycerides", "Raising triglycerides is a bile acid sequestrant problem, not a statin effect; statins lower triglycerides modestly."],
  ["Increased platelet stickiness", "The reverse: platelet inhibition and antithrombosis are among the pleiotropic effects of statins."],
  ["Increased inflammatory markers", "Statins reduce inflammatory markers; that reduction is listed among their pleiotropic effects."]],
 "c": 0, "cite": D + ", Slide 19"},

# ---- metabolism and interactions (the CYP3A4 pair) -----------------------------
{"topic": "Statin metabolism", "io": IO_ADME, "slot": "interaction",
 "q": "Which statin is metabolized mainly by CYP3A4?",
 "opts": [
  ["Simvastatin", "Correct. Atorvastatin, lovastatin and simvastatin are the CYP3A4 statins, so CYP3A4 inhibitors such as verapamil raise their levels."],
  ["Rosuvastatin", "Rosuvastatin undergoes minimal CYP metabolism, which is why it is the least affected by CYP3A4 inhibitors."],
  ["Pravastatin", "Pravastatin is metabolized by enzymatic and nonenzymatic routes, not mainly by CYP3A4."],
  ["Pitavastatin", "Pitavastatin is cleared by glucuronidation (UGT1A3 and UGT2B7), not by CYP3A4."]],
 "c": 0, "cite": D + ", Slide 20"},

{"topic": "Statin metabolism", "io": IO_INTER, "slot": "drug choice",
 "q": "A patient on verapamil needs a statin. Which statin would CYP3A4 inhibition affect least?",
 "opts": [
  ["Rosuvastatin", "Correct. Rosuvastatin has minimal CYP metabolism, so verapamil's CYP3A4 inhibition matters least; atorvastatin, lovastatin and simvastatin are CYP3A4 substrates."],
  ["Atorvastatin", "Atorvastatin is a CYP3A4 substrate, and verapamil inhibits CYP3A4, so its levels rise. Rosuvastatin has minimal CYP metabolism."],
  ["Lovastatin", "Lovastatin is metabolized by CYP3A4, so verapamil raises it. Rosuvastatin avoids that interaction."],
  ["Simvastatin", "Simvastatin is a CYP3A4 substrate raised by verapamil, a CYP3A4 inhibitor. Rosuvastatin has minimal CYP metabolism."]],
 "c": 0, "cite": D + ", Slide 20"},

{"topic": "Statin interactions", "io": IO_EDU, "slot": "education",
 "q": "Which item in a patient's diet interacts with simvastatin through CYP450 metabolism?",
 "opts": [
  ["Grapefruit juice", "Correct. Grapefruit juice is listed with verapamil, amiodarone, niacin and fibrates as a statin interaction, especially involving CYP3A4."],
  ["Salt substitutes", "Salt substitutes contain potassium and matter with ACE (angiotensin-converting enzyme) inhibitors because of hyperkalemia, not with statins."],
  ["Alcohol", "Alcohol is listed as a niacin interaction. The dietary item listed with statins through CYP450 metabolism is grapefruit juice."],
  ["Antacids", "Antacids lower ezetimibe concentrations; they are not the listed statin interaction. Grapefruit juice is."]],
 "c": 0, "cite": D + ", Slide 24"},

{"topic": "Statin interactions", "io": IO_INTER, "slot": "interaction",
 "q": "Which antiarrhythmic is listed as a CYP-mediated statin interaction?",
 "opts": [
  ["Amiodarone", "Correct. Verapamil, amiodarone, niacin, fibric acid derivatives and grapefruit juice are the listed statin interactions, especially through CYP3A4."],
  ["Digoxin", "Digoxin is affected by bile acid sequestrants and by verapamil's P-glycoprotein inhibition; it is not a listed statin interaction."],
  ["Esmolol", "Esmolol is an intravenous beta-1 selective blocker, not a listed statin interaction. Amiodarone is."],
  ["Sotalol", "Sotalol is a first-generation, non-selective beta blocker and is not on the statin interaction list, which names verapamil and amiodarone."]],
 "c": 0, "cite": D + ", Slide 24"},

{"topic": "Statin interactions", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which combination is a relative contraindication for statin therapy?",
 "opts": [
  ["A statin with gemfibrozil", "Correct. Relative contraindications are concomitant cyclosporine or other immunosuppressants, gemfibrozil, niacin and erythromycin."],
  ["A statin with ezetimibe", "Ezetimibe is designed to be added to a statin for dual inhibition; it raises transaminases but is not a relative contraindication."],
  ["A statin with lisinopril", "An ACE (angiotensin-converting enzyme) inhibitor is not a listed statin interaction. Gemfibrozil is a relative contraindication."],
  ["A statin with amlodipine", "Amlodipine is not on the statin interaction or contraindication lists. Gemfibrozil is a relative contraindication because of myopathy."]],
 "c": 0, "cite": D + ", Slide 23"},

{"topic": "Statin interactions", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which antibiotic is a relative contraindication with statins?",
 "opts": [
  ["Erythromycin", "Correct. Erythromycin is on the relative contraindication list with cyclosporine and other immunosuppressants, gemfibrozil and niacin."],
  ["Amoxicillin", "Amoxicillin is not on the statin relative contraindication list. Erythromycin is."],
  ["Cephalexin", "Cephalexin is not listed with statins. The antibiotic listed as a relative contraindication is erythromycin."],
  ["Doxycycline", "Doxycycline is not listed as a statin relative contraindication. Erythromycin is."]],
 "c": 0, "cite": D + ", Slide 23"},

# ---- contraindications -------------------------------------------------------------
{"topic": "Statin contraindications", "io": IO_CONTRA, "slot": "contraindication",
 "q": "In which patient is a statin contraindicated?",
 "opts": [
  ["A patient who is pregnant", "Correct. Hepatic disease and pregnancy are the statin contraindications."],
  ["A patient aged 50 with diabetes", "Diabetes at ages 40 to 75 with LDL (low-density lipoprotein) 70 to 189 mg/dL is a statin benefit group, not a contraindication."],
  ["A patient after a heart attack", "Clinical atherosclerotic cardiovascular disease is the first statin benefit group, not a contraindication."],
  ["A patient with LDL of 210 mg/dL", "LDL (low-density lipoprotein) above 190 mg/dL is a statin benefit group. Pregnancy is the contraindication here."]],
 "c": 0, "cite": D + ", Slide 23"},

{"topic": "Statin contraindications", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which condition is listed as a contraindication to statins?",
 "opts": [
  ["Hepatic disease", "Correct. Hepatic disease and pregnancy are the listed contraindications; liver enzyme rises on therapy are managed by reducing the dose or pausing."],
  ["Type 2 diabetes", "Diabetes is a reason to use a statin (a benefit group), not a contraindication."],
  ["Hypertension", "Hypertension is not a statin contraindication. Hepatic disease and pregnancy are."],
  ["Prior stroke", "A prior stroke is clinical atherosclerotic cardiovascular disease, a benefit group. Hepatic disease is the contraindication."]],
 "c": 0, "cite": D + ", Slide 23"},

# ---- adverse effects ---------------------------------------------------------------
{"topic": "Statin adverse effects", "io": IO_PROT, "slot": "protocol",
 "q": "A patient's liver enzymes rise after starting atorvastatin. What is the recommended management?",
 "opts": [
  ["Lower the dose or pause it", "Correct. Liver enzyme rises occur in 0.5 to 2.5% of patients in a dose-dependent manner and are managed by reducing the dose or stopping until levels return to normal."],
  ["Stop it and never restart", "Permanent withdrawal is not the listed approach; the dose is reduced or the statin paused until enzymes return to normal."],
  ["Continue it at the same dose", "The enzyme rise is not simply ignored: it is managed by reducing the dose or stopping until levels normalize."],
  ["Add a fibrate to protect it", "Adding a fibrate raises myopathy risk and does nothing for liver enzymes. The dose is reduced or the drug paused."]],
 "c": 0, "cite": D + ", Slide 21"},

{"topic": "Statin adverse effects", "io": IO_TOX, "slot": "adverse effect",
 "q": "Which statement about serious liver injury from statins is accurate?",
 "opts": [
  ["It is exceedingly rare", "Correct. Liver enzyme rises occur in 0.5 to 2.5% of patients, dose-dependently, but serious liver problems are exceedingly rare."],
  ["It affects a quarter of users", "Even the enzyme rise affects only 0.5 to 2.5% of patients, and serious liver problems are exceedingly rare."],
  ["It is the main reason to stop", "Serious liver injury is exceedingly rare; muscle toxicity is the listed reason that requires stopping a statin."],
  ["It occurs regardless of dose", "The liver enzyme rise is dose-dependent, and serious liver problems are exceedingly rare."]],
 "c": 0, "cite": D + ", Slide 21"},

{"topic": "Statin adverse effects", "io": IO_PROT, "slot": "protocol",
 "q": "A patient on simvastatin develops muscle toxicity. What is required?",
 "opts": [
  ["Discontinue the statin", "Correct. The presence of muscle toxicity requires discontinuing the statin; myopathy occurs in 0.2 to 0.4% with rare rhabdomyolysis."],
  ["Continue and add a fibrate", "Fibrates add to statin myopathy risk. Muscle toxicity requires the statin to be discontinued."],
  ["Double the dose briefly", "A higher dose raises myopathy risk. Muscle toxicity requires discontinuing the statin."],
  ["Switch to taking it with grapefruit", "Grapefruit juice raises statin levels through CYP3A4 and would worsen toxicity. The statin must be stopped."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Statin adverse effects", "io": IO_PROT, "slot": "protocol",
 "q": "Which measure reduces the risk of statin myopathy?",
 "opts": [
  ["Using the lowest effective dose", "Correct. Risk is also reduced by caution in renal impairment, caution with fibrates, avoiding other drug interactions, and monitoring symptoms and laboratory values."],
  ["Routinely adding a fibrate", "Combining statins with fibrates is done only cautiously because it raises myopathy risk."],
  ["Taking it with grapefruit juice", "Grapefruit juice raises CYP3A4 statin levels, adding to myopathy risk rather than reducing it."],
  ["Using the highest tolerated dose", "Higher doses raise myopathy risk. The listed measure is the lowest effective dose."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Statin adverse effects", "io": IO_TOX, "slot": "adverse effect",
 "q": "What is the most severe muscle toxicity of statins?",
 "opts": [
  ["Rhabdomyolysis", "Correct. Myalgia and myopathy (0.2 to 0.4%) are more common; rhabdomyolysis is rare but the most severe, and muscle toxicity requires stopping the statin."],
  ["Myalgia", "Myalgia is muscle pain without the severity of rhabdomyolysis, which is the rare but most serious muscle toxicity."],
  ["Muscle cramps at night", "Cramping is not the listed severe toxicity. Rhabdomyolysis is the rare, most severe form."],
  ["Essential tremor", "Tremor is not a statin muscle toxicity; beta blockers are used to treat essential tremor. Rhabdomyolysis is the severe form."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Statin adverse effects", "io": IO_AE, "slot": "adverse effect",
 "q": "Which is a common side effect of statins?",
 "opts": [
  ["Headache and sleep disturbance", "Correct. Common statin side effects are headache, sleep disturbance, fatigue, gastrointestinal intolerance, flu-like symptoms and liver enzyme rises."],
  ["Cutaneous flushing and itching", "Prostaglandin-mediated flushing is the hallmark of niacin, not statins."],
  ["Constipation and bloating", "Constipation, bloating and flatulence are the gastrointestinal effects of bile acid sequestrants."],
  ["Gallstones and abdominal pain", "Cholelithiasis (gallstones) with abdominal pain points to fibrates, and ezetimibe with a fibrate raises it; statins cause headache and sleep disturbance."]],
 "c": 0, "cite": D + ", Slide 21"},

# ---- benefit groups, guidelines, intensity ------------------------------------------
{"topic": "Statin benefit groups", "io": IO_IND, "slot": "indication",
 "q": "Which patient falls into one of the four major statin benefit groups?",
 "opts": [
  ["A 55-year-old after a myocardial infarction", "Correct. Clinical atherosclerotic cardiovascular disease is the first benefit group; the others are LDL above 190 mg/dL, diabetes at 40 to 75 with LDL 70 to 189, and high estimated risk."],
  ["A 35-year-old with diabetes and LDL of 120", "The diabetes group covers ages 40 to 75 with LDL (low-density lipoprotein) 70 to 189 mg/dL; at 35 this patient falls outside it."],
  ["A 50-year-old with LDL of 150 and 3% risk", "Without disease, diabetes or LDL above 190 mg/dL, a statin group needs a high estimated 10-year risk; 3% is low."],
  ["A 60-year-old with diabetes and LDL of 60", "The diabetes group requires LDL (low-density lipoprotein) of 70 to 189 mg/dL; 60 mg/dL falls below it."]],
 "c": 0, "cite": D + ", Slide 65"},

{"topic": "Statin benefit groups", "io": IO_IND, "slot": "indication",
 "q": "A 42-year-old with no diabetes and no cardiovascular disease has an LDL (low-density lipoprotein) cholesterol of 212 mg/dL. Does he fall into a statin benefit group?",
 "opts": [
  ["Yes, LDL above 190 alone qualifies", "Correct. Individuals with LDL above 190 mg/dL form one of the four statin benefit groups, whatever their other risk factors."],
  ["No, he needs diabetes as well", "Diabetes defines a separate group. LDL above 190 mg/dL is a benefit group on its own."],
  ["No, he must be at least 55", "No minimum age of 55 applies to this group. LDL above 190 mg/dL alone places him in a benefit group."],
  ["No, he needs prior heart disease", "Clinical cardiovascular disease is a separate group. LDL above 190 mg/dL qualifies by itself."]],
 "c": 0, "cite": D + ", Slide 65"},

{"topic": "Statin benefit groups", "io": IO_IND, "slot": "indication",
 "q": "Which patient with diabetes and no clinical cardiovascular disease meets a statin benefit group?",
 "opts": [
  ["Age 55 with LDL of 120 mg/dL", "Correct. The diabetes group is ages 40 to 75 with LDL (low-density lipoprotein) 70 to 189 mg/dL and no clinical atherosclerotic cardiovascular disease."],
  ["Age 30 with LDL of 120 mg/dL", "At 30 the patient is younger than the 40-to-75 age range that defines the diabetes group."],
  ["Age 55 with LDL of 60 mg/dL", "An LDL of 60 mg/dL is below the 70 to 189 mg/dL range the diabetes group requires."],
  ["Age 82 with LDL of 120 mg/dL", "At 82 the patient is older than the 40-to-75 age range that defines the diabetes group."]],
 "c": 0, "cite": D + ", Slide 65"},

{"topic": "Statin guidelines", "io": IO_PROT, "slot": "protocol",
 "q": "How does the ACC/AHA (American College of Cardiology/American Heart Association) cholesterol guideline differ from ATP III (Adult Treatment Panel III)?",
 "opts": [
  ["It does not treat to an LDL target", "Correct. It starts moderate- or high-intensity statin therapy for the four benefit groups and does not titrate to a specific LDL (low-density lipoprotein) target."],
  ["It targets an LDL below 100 mg/dL", "An LDL under 100 mg/dL as the optimal goal is the ATP III approach, which the newer guideline dropped."],
  ["It starts everyone on high intensity", "The newer guideline starts either moderate- or high-intensity statin therapy for the four groups, not high intensity for all."],
  ["It makes niacin the first choice", "Statins remain first line; the change was dropping titration to an LDL target."]],
 "c": 0, "cite": D + ", Slide 64"},

{"topic": "Statin guidelines", "io": IO_PROT, "slot": "protocol",
 "q": "Under the ACC/AHA (American College of Cardiology/American Heart Association) guideline, why are lipids measured at follow-up visits?",
 "opts": [
  ["To assess adherence", "Correct. Lipids are measured at follow-up to assess adherence to treatment, not to reach a specific LDL (low-density lipoprotein) target."],
  ["To titrate to an LDL goal", "Titrating to an LDL target was the ATP III (Adult Treatment Panel III) approach that the newer guideline dropped."],
  ["To detect liver disease early", "Follow-up lipid panels are not a liver screen; they are measured to assess adherence to treatment."],
  ["To decide whether to add niacin", "The stated purpose of follow-up lipid measurement is to assess adherence to treatment."]],
 "c": 0, "cite": D + ", Slide 64"},

{"topic": "Statin intensity", "io": IO_CLASS, "slot": "class",
 "q": "Which statin can be used as high-intensity therapy?",
 "opts": [
  ["Rosuvastatin", "Correct. Only atorvastatin and rosuvastatin reach high intensity, lowering LDL (low-density lipoprotein) cholesterol by 50% or more."],
  ["Pravastatin", "Pravastatin reaches moderate or low intensity only. The high-intensity statins are atorvastatin and rosuvastatin."],
  ["Lovastatin", "Lovastatin is a moderate- or low-intensity statin. High intensity is reached only by atorvastatin and rosuvastatin."],
  ["Fluvastatin", "Fluvastatin appears only at moderate or low intensity. Atorvastatin and rosuvastatin are the high-intensity options."]],
 "c": 0, "cite": D + ", Slide 68"},

{"topic": "Statin intensity", "io": IO_CLASS, "slot": "class",
 "q": "Which of these statins is one of the two that can reach high intensity?",
 "opts": [
  ["Atorvastatin", "Correct. Atorvastatin and rosuvastatin are the only statins that reach high intensity (50% or greater lowering of LDL, low-density lipoprotein, cholesterol)."],
  ["Simvastatin", "Simvastatin reaches moderate or low intensity only. Atorvastatin and rosuvastatin are the high-intensity statins."],
  ["Pitavastatin", "Pitavastatin is listed only as moderate intensity. The two high-intensity statins are atorvastatin and rosuvastatin."],
  ["Pravastatin", "Pravastatin is moderate or low intensity. Only atorvastatin and rosuvastatin reach high intensity."]],
 "c": 0, "cite": D + ", Slide 68"},

{"topic": "Statin intensity", "io": IO_PROT, "slot": "protocol",
 "q": "By how much does high-intensity statin therapy lower LDL (low-density lipoprotein) cholesterol?",
 "opts": [
  ["By 50% or more", "Correct. High intensity lowers LDL by 50% or more; moderate intensity by 30 to 49%; low intensity by less than 30%."],
  ["By 30 to 49%", "A 30 to 49% reduction defines moderate-intensity therapy. High intensity lowers LDL by 50% or more."],
  ["By less than 30%", "Under 30% defines low-intensity therapy. High intensity lowers LDL by 50% or more."],
  ["By 10 to 20%", "A reduction this small is below even low-intensity therapy; high intensity lowers LDL by 50% or more."]],
 "c": 0, "cite": D + ", Slide 68"},

{"topic": "Statin guidelines", "io": IO_PROT, "slot": "protocol",
 "q": "A patient cannot tolerate a moderate- or high-intensity statin. What is recommended?",
 "opts": [
  ["Use the maximum tolerated dose", "Correct. If high- or moderate-intensity therapy is not tolerated, the maximum tolerated dose is used instead, keeping side effects and interactions in mind."],
  ["Stop statins permanently", "Intolerance of higher intensity is not a reason to abandon statins; the maximum tolerated dose is used instead."],
  ["Replace it with niacin alone", "The recommendation for intolerance is the maximum tolerated statin dose, not a switch to niacin."],
  ["Add gemfibrozil to the statin", "Gemfibrozil is a relative contraindication with statins because of myopathy. The maximum tolerated statin dose is used."]],
 "c": 0, "cite": D + ", Slide 69"},
]
