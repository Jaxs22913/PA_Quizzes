# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- Lipids (Lecture 7), topic 2: the other LDL-lowering
agents -- bile acid sequestrants, ezetimibe and PCSK9 inhibitors.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

SOURCE. Lipids.pptx slides 6, 14, 26-31, 40-49 and 60.

EMPHASIS (weight only): the resin triglyceride contraindication and its flip
("which treats high triglycerides" against "which is contraindicated at a
triglyceride of 600 -- slight difference in the question, totally different
answer"); resins binding other drugs ("really critical... separate this out"),
which is the lecture's one plainly patient-education slide; and the unifying
thread that statins, ezetimibe, resins and PCSK9 inhibitors all end at more
hepatic LDL receptors.

SLIDE WINS: resins are "safest... poorly tolerated... modest reductions in LDL"
(slide 49); the "probably the weakest" said aloud is not keyed. Ezetimibe with a
fibrate raises cholelithiasis AND myopathy (slide 31), though the recording
played down ezetimibe myopathy.

NOT KEYED: ezetimibe acting on NPC1L1 (the transporter is named, but never as
ezetimibe's target); orlistat (never on a slide); the ezetimibe 15-20% figure
(it sits on the dosing slide). Of the ezetimibe interactions, antacids, resins
and fibrates are asked; cyclosporine was called rare and is left out. No doses.
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

# ---- bile acid sequestrants: mechanism ----------------------------------------------
{"topic": "Bile acid sequestrants", "io": IO_MOA, "slot": "mechanism",
 "q": "How do bile acid sequestrants lower LDL (low-density lipoprotein) cholesterol?",
 "opts": [
  ["They bind bile acids in the gut", "Correct. Bound bile acids are excreted in feces instead of recirculating, so the liver makes more bile acids from cholesterol and more LDL receptors, lowering LDL."],
  ["They inhibit HMG-CoA reductase", "Inhibiting HMG-CoA reductase is the statin mechanism. Resins bind bile acids in the gut and interrupt their enterohepatic recirculation."],
  ["They block brush-border uptake", "Blocking cholesterol uptake at the intestinal brush border is ezetimibe's mechanism. Resins bind bile acids."],
  ["They activate PPAR-alpha", "PPAR-alpha activation is how fibrates lower triglycerides. Resins act by binding bile acids in the gut."]],
 "c": 0, "cite": D + ", Slide 42"},

{"topic": "Bile acid sequestrants", "io": IO_MOA, "slot": "mechanism",
 "q": "Where in the gut do resins block the reabsorption of bile acids?",
 "opts": [
  ["The terminal ileum", "Correct. Bile acids are normally reabsorbed at the terminal ileum and recirculated to the liver; resins block that reabsorption so bile acid excretion rises."],
  ["The stomach", "Bile acids are not reabsorbed in the stomach. Resins act at the terminal ileum, where enterohepatic reabsorption occurs."],
  ["The brush border of the jejunum", "Brush-border sterol uptake in the upper small intestine is where ezetimibe acts. Resins block bile acid reabsorption at the terminal ileum."],
  ["The gallbladder wall", "The gallbladder stores and secretes bile; it is not the reabsorption site. Resins block bile acid reabsorption at the terminal ileum."]],
 "c": 0, "cite": D + ", Slide 14"},

{"topic": "Bile acid sequestrants", "io": IO_MOA, "slot": "mechanism",
 "q": "When resins deplete the bile acid pool, which hepatic enzyme increases to convert cholesterol into bile acids?",
 "opts": [
  ["Cholesterol 7-alpha hydroxylase", "Correct. Increased 7-alpha hydroxylase activity converts more cholesterol to bile acids, and the liver adds LDL receptors, increasing VLDL and LDL removal."],
  ["Acyl-CoA:cholesterol acyltransferase", "Acyl-coenzyme A:cholesterol acyltransferase esterifies cholesterol for storage and packaging; it does not convert cholesterol into bile acids."],
  ["Lipoprotein lipase in plasma", "Lipoprotein lipase hydrolyzes triglyceride in chylomicrons and very low-density lipoprotein; it does not make bile acids. Cholesterol 7-alpha hydroxylase does."],
  ["Hepatic HMG-CoA reductase", "HMG-CoA reductase is the statin target in cholesterol synthesis; it does not convert cholesterol into bile acids. Cholesterol 7-alpha hydroxylase does."]],
 "c": 0, "cite": D + ", Slide 41"},

# ---- resins: absorption, place in therapy, pregnancy --------------------------------
{"topic": "Bile acid sequestrants", "io": IO_ADME, "slot": "indication",
 "q": "Why are bile acid sequestrants approved for children, adolescents and pregnancy?",
 "opts": [
  ["They are not absorbed from the gut", "Correct. Because resins stay in the gastrointestinal tract, systemic side effects are limited; they are called the safest drug for that reason."],
  ["They are cleared quickly by the kidney", "Renal clearance is not the reason. Resins are not absorbed at all, so they cause few systemic effects."],
  ["They have no effect on other drugs", "Resins do affect other drugs, binding digoxin, warfarin, thyroxine, beta blockers and thiazides. Their safety comes from not being absorbed."],
  ["They have no gastrointestinal effects", "Gastrointestinal effects are common: bloating, flatulence, fullness, constipation and nausea. Their safety comes from not being absorbed."]],
 "c": 0, "cite": D + ", Slide 42"},

{"topic": "Bile acid sequestrants", "io": IO_CONTRA, "slot": "drug choice",
 "q": "A patient planning a pregnancy needs LDL (low-density lipoprotein) lowering. Which class is approved in pregnancy?",
 "opts": [
  ["Bile acid sequestrants", "Correct. Resins are not absorbed and are approved in pregnancy, whereas pregnancy is a listed contraindication for statins and for fibrates."],
  ["Statins", "Pregnancy is one of the two listed statin contraindications, with hepatic disease. Bile acid sequestrants are approved in pregnancy."],
  ["Fibrates", "Pregnancy is a listed fibrate contraindication, with severe hepatic or renal dysfunction and gallbladder disease. Resins are approved in pregnancy."],
  ["Statin with niacin", "The lovastatin and niacin combination contains a statin, and pregnancy contraindicates statins. Bile acid sequestrants are the pregnancy option."]],
 "c": 0, "cite": D + ", Slide 42"},

{"topic": "Bile acid sequestrants", "io": IO_IND, "slot": "indication",
 "q": "Which statement describes the place of bile acid sequestrants in therapy?",
 "opts": [
  ["Safest, but poorly tolerated", "Correct. They are the safest because they have no systemic effects, but poorly tolerated; they are used with a statin or where only modest LDL (low-density lipoprotein) reductions are needed."],
  ["Most efficacious and best tolerated", "That describes statins, the first-line agents. Resins are safe but poorly tolerated and used for modest reductions or with a statin."],
  ["First choice when triglycerides are over 1000 mg/dL", "Triglycerides over 1000 mg/dL are the primary fibrate indication; resins can raise triglycerides."],
  ["Injectable only and expensive", "Injectable-only and expensive describes the PCSK9 inhibitors. Resins are oral, safe and poorly tolerated."]],
 "c": 0, "cite": D + ", Slide 49"},

# ---- resins: triglycerides (the flip) -------------------------------------------------
{"topic": "Bile acid sequestrants", "io": IO_CONTRA, "slot": "contraindication",
 "q": "A patient with a fasting triglyceride of 600 mg/dL needs cholesterol treatment. Which class is contraindicated?",
 "opts": [
  ["Bile acid sequestrants", "Correct. Triglycerides above 400 mg/dL are an absolute contraindication to resins (above 200 mg/dL is relative), because they can raise VLDL (very low-density lipoprotein) production and triglycerides."],
  ["Fibric acid derivatives", "Fibrates lower triglycerides by 20 to 50% and are the treatment for very high levels, not a contraindication."],
  ["Nicotinic acid (niacin)", "Niacin lowers triglycerides and raises HDL (high-density lipoprotein); a high triglyceride level does not contraindicate it."],
  ["HMG-CoA reductase inhibitors", "Statins lower triglycerides modestly and are not contraindicated by a high level. Resins are, because they may raise triglycerides."]],
 "c": 0, "cite": D + ", Slide 48"},

{"topic": "Bile acid sequestrants", "io": IO_AE, "slot": "adverse effect",
 "q": "Why are bile acid sequestrants avoided when triglycerides are high?",
 "opts": [
  ["They may raise triglycerides", "Correct. Resins may increase VLDL (very low-density lipoprotein) production, raising triglycerides; on the lipid comparison, resins show no change or a rise in triglycerides."],
  ["They cause gallstones", "Cholelithiasis is a fibrate adverse effect (and a risk of ezetimibe with a fibrate), not the reason resins are avoided."],
  ["They lower HDL sharply", "Resins raise HDL (high-density lipoprotein) slightly. The reason to avoid them is that they may raise triglycerides."],
  ["They damage the liver", "Resins are not absorbed and have no systemic toxicity. The concern is increased VLDL production raising triglycerides."]],
 "c": 0, "cite": D + ", Slide 46"},

{"topic": "Bile acid sequestrants", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Above what triglyceride level is a bile acid sequestrant a relative contraindication?",
 "opts": [
  ["200 mg/dL", "Correct. Triglycerides above 200 mg/dL are a relative contraindication; above 400 mg/dL, or familial dysbetalipoproteinemia, is absolute."],
  ["1000 mg/dL", "Triglycerides over 1000 mg/dL are the primary indication for a fibrate, not the resin threshold."],
  ["150 mg/dL", "Under 150 mg/dL is the normal triglyceride goal in ATP III (Adult Treatment Panel III); the resin relative threshold is 200 mg/dL."],
  ["100 mg/dL", "A level of 100 mg/dL is normal; the relative contraindication to resins begins above 200 mg/dL."]],
 "c": 0, "cite": D + ", Slide 48"},

{"topic": "Bile acid sequestrants", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which condition is an absolute contraindication to bile acid sequestrants?",
 "opts": [
  ["Familial dysbetalipoproteinemia", "Correct. Familial dysbetalipoproteinemia (with its increased triglycerides) and triglycerides above 400 mg/dL are absolute contraindications."],
  ["Pregnancy in the third trimester", "Resins are approved in pregnancy because they are not absorbed; pregnancy contraindicates statins and fibrates instead."],
  ["Childhood or adolescence", "Resins are approved for children and adolescents. The absolute contraindication is familial dysbetalipoproteinemia."],
  ["Chronic hepatic disease", "Hepatic disease contraindicates statins; resins are not absorbed. Their absolute contraindication is familial dysbetalipoproteinemia."]],
 "c": 0, "cite": D + ", Slide 48"},

# ---- resins: adverse effects, administration, interactions ----------------------------
{"topic": "Bile acid sequestrants", "io": IO_AE, "slot": "adverse effect",
 "q": "Which adverse effect profile is typical of bile acid sequestrants?",
 "opts": [
  ["Bloating, flatulence, constipation", "Correct. Resins cause gastrointestinal effects -- bloating, flatulence, fullness, constipation and nausea -- plus malabsorption of fat-soluble vitamins and folic acid."],
  ["Flushing, itching, raised uric acid", "Flushing and raised uric acid are niacin effects. Resins cause bloating, flatulence and constipation."],
  ["Myalgia, headache, raised enzymes", "Myalgia, headache and liver enzyme rises are statin effects. Resins cause gastrointestinal effects."],
  ["Gallstones, nausea, myopathy", "Cholelithiasis with myopathy is the fibrate pattern. Resins cause bloating, flatulence and constipation."]],
 "c": 0, "cite": D + ", Slide 46"},

{"topic": "Bile acid sequestrants", "io": IO_AE, "slot": "adverse effect",
 "q": "A patient has taken cholestyramine for years. Which deficiency is she at risk of?",
 "opts": [
  ["Fat-soluble vitamins and folate", "Correct. Resins cause malabsorption of vitamins A, D, E and K and of folic acid."],
  ["Potassium, magnesium and zinc", "Electrolyte loss of this kind is not a listed resin effect. They cause malabsorption of vitamins A, D, E and K and folic acid."],
  ["Water-soluble B vitamins and iron", "Iron and the water-soluble B vitamins are not the listed deficiencies. Resins impair absorption of vitamins A, D, E and K and folic acid."],
  ["Sodium, chloride and bicarbonate", "Sodium, chloride and bicarbonate loss is not described. The malabsorption is of vitamins A, D, E and K and folic acid."]],
 "c": 0, "cite": D + ", Slide 46"},

{"topic": "Bile acid sequestrants", "io": IO_EDU, "slot": "education",
 "q": "How should a patient prepare cholestyramine powder?",
 "opts": [
  ["Mix it in water or fruit juice", "Correct. Powders must be mixed with water or fruit juice, and a pulpy drink masks the taste."],
  ["Swallow the powder dry", "The powder is not taken dry; it must be mixed with water or fruit juice, ideally a pulpy drink to mask the taste."],
  ["Dissolve it under the tongue", "Resins act in the gut lumen and are not absorbed, so sublingual use makes no sense; the powder is mixed in water or fruit juice."],
  ["Mix it with an antacid", "Antacids are not the vehicle; they interact with ezetimibe. The powder is mixed with water or fruit juice."]],
 "c": 0, "cite": D + ", Slide 45"},

{"topic": "Bile acid sequestrants", "io": IO_EDU, "slot": "education",
 "q": "When should a bile acid sequestrant be taken in relation to meals?",
 "opts": [
  ["Within 1 hour of a meal", "Correct. Resins are taken within 1 hour of a meal, when bile acids are being secreted, and other medications are separated from them."],
  ["At least 4 hours after meals", "Four hours is the gap for other drugs taken after the resin, not the meal timing. The resin is taken within 1 hour of a meal."],
  ["Fasting, at bedtime only", "A fasting bedtime dose is not advised; the resin is taken within 1 hour of a meal."],
  ["With or without meals", "With or without meals is the instruction for ezetimibe. Resins are taken within 1 hour of a meal."]],
 "c": 0, "cite": D + ", Slide 45"},

{"topic": "Bile acid sequestrants", "io": IO_INTER, "slot": "education",
 "q": "A patient taking colestipol also takes thyroxine. How should the thyroxine be timed?",
 "opts": [
  ["1 hour before or 4 hours after", "Correct. Resins interfere with absorption of digoxin, warfarin, thyroxine, beta blockers and thiazide diuretics; giving the drug 1 hour before or 4 hours after the resin avoids it."],
  ["At the same time as the resin", "Taking them together lets the resin bind the thyroxine and reduce its absorption. Separate by 1 hour before or 4 hours after."],
  ["30 minutes after the resin", "Half an hour after is too soon; the resin is still in the gut. The drug is given 1 hour before or 4 hours after."],
  ["Timing does not matter", "Timing matters because resins bind thyroxine in the gut. It is given 1 hour before or 4 hours after the resin."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": "Bile acid sequestrants", "io": IO_INTER, "slot": "interaction",
 "q": "Cholestyramine reduces the absorption of which drug?",
 "opts": [
  ["Warfarin", "Correct. As anion exchange resins they interfere with the absorption of digoxin, warfarin, thyroxine, beta blockers and thiazide diuretics."],
  ["Evolocumab", "Evolocumab is injected, so a resin in the gut cannot affect its absorption. Warfarin, an oral drug, is on the list."],
  ["Nitroprusside", "Nitroprusside is given by intravenous infusion, bypassing the gut. Resins reduce absorption of oral drugs such as warfarin."],
  ["Esmolol", "Esmolol is an intravenous beta blocker, so gut binding cannot affect it. Warfarin's absorption is reduced by resins."]],
 "c": 0, "cite": D + ", Slide 47"},

# ---- ezetimibe ------------------------------------------------------------------------
{"topic": "Ezetimibe", "io": IO_MOA, "slot": "mechanism",
 "q": "How does ezetimibe lower LDL (low-density lipoprotein) cholesterol?",
 "opts": [
  ["It blocks intestinal cholesterol absorption", "Correct. Less cholesterol reaches the liver, so hepatic LDL receptor expression rises and atherogenic particles carry less cholesterol."],
  ["It inhibits hepatic cholesterol synthesis", "Inhibiting hepatic synthesis at HMG-CoA reductase is the statin mechanism; ezetimibe acts on the intestine's supply side."],
  ["It binds bile acids in the terminal ileum", "Binding bile acids at the terminal ileum is the resin mechanism. Ezetimibe selectively inhibits cholesterol absorption."],
  ["It blocks PCSK9 in the circulation", "Blocking PCSK9 is how alirocumab and evolocumab work. Ezetimibe inhibits intestinal cholesterol absorption."]],
 "c": 0, "cite": D + ", Slide 28"},

{"topic": "Ezetimibe", "io": IO_MOA, "slot": "mechanism",
 "q": "Where does ezetimibe act?",
 "opts": [
  ["The intestinal brush border", "Correct. Ezetimibe selectively inhibits cholesterol absorption at the brush border membrane, blocking sterol uptake in the upper small intestine."],
  ["The terminal ileum", "The terminal ileum is where resins block bile acid reabsorption. Ezetimibe acts at the intestinal brush border."],
  ["The hepatocyte enzyme", "Hepatocyte HMG-CoA reductase is the statin target. Ezetimibe acts in the intestine, at the brush border."],
  ["Adipose tissue", "Reducing fatty acid mobilization from adipose tissue is niacin's action. Ezetimibe acts at the brush border."]],
 "c": 0, "cite": D + ", Slide 27"},

{"topic": "Ezetimibe", "io": IO_ADME, "slot": "mechanism",
 "q": "What limits ezetimibe's systemic exposure?",
 "opts": [
  ["Enterohepatic recirculation", "Correct. Ezetimibe and its active glucuronide metabolite circulate enterohepatically, returning the drug to its site of action and limiting systemic exposure."],
  ["Extensive CYP3A4 metabolism", "CYP3A4 metabolism is the story for atorvastatin, lovastatin and simvastatin. Ezetimibe's exposure is limited by enterohepatic recirculation."],
  ["Rapid renal excretion", "Renal clearance is not the described reason. Enterohepatic recirculation keeps ezetimibe at its site of action."],
  ["It is not absorbed at all", "Complete non-absorption describes bile acid sequestrants. Ezetimibe forms an active glucuronide and recirculates enterohepatically."]],
 "c": 0, "cite": D + ", Slide 28"},

{"topic": "Ezetimibe", "io": IO_IND, "slot": "indication",
 "q": "How is ezetimibe typically used?",
 "opts": [
  ["Added to a statin", "Correct. It pairs with a statin for dual inhibition -- the statin blocks synthesis, ezetimibe blocks absorption -- for additional LDL (low-density lipoprotein) lowering."],
  ["As first-line monotherapy", "Statins are first line for LDL lowering. Ezetimibe is used on top of a statin for dual inhibition."],
  ["For triglycerides over 1000", "Triglycerides over 1000 mg/dL are the primary fibrate indication; ezetimibe barely affects triglycerides."],
  ["As a weekly injection", "Injectable use describes PCSK9 inhibitors. Ezetimibe is an oral agent added to a statin."]],
 "c": 0, "cite": D + ", Slide 27"},

{"topic": "Ezetimibe", "io": IO_EDU, "slot": "education",
 "q": "How should ezetimibe be taken in relation to meals?",
 "opts": [
  ["With or without meals", "Correct. Ezetimibe can be taken with or without meals, unlike bile acid sequestrants, which are taken within 1 hour of a meal."],
  ["Within 1 hour of a meal", "Taking a dose within 1 hour of a meal is the resin instruction. Ezetimibe may be taken with or without meals."],
  ["Only on an empty stomach", "No fasting requirement applies; ezetimibe may be taken with or without meals."],
  ["Only with a high-fat meal", "A fatty meal is not required; ezetimibe may be taken with or without meals."]],
 "c": 0, "cite": D + ", Slide 29"},

{"topic": "Ezetimibe", "io": IO_AE, "slot": "adverse effect",
 "q": "Which laboratory change occurs when ezetimibe is combined with a statin?",
 "opts": [
  ["Raised hepatic transaminases", "Correct. Ezetimibe's adverse effects are gastrointestinal effects and elevated hepatic transaminases when combined with statins."],
  ["Raised serum potassium", "Raised potassium belongs to ACE (angiotensin-converting enzyme) inhibitors and angiotensin receptor blockers, not ezetimibe."],
  ["Raised serum uric acid", "Raised uric acid is a niacin effect at larger doses. Ezetimibe with a statin raises hepatic transaminases."],
  ["Raised serum calcium", "Calcium is not affected by ezetimibe. The listed laboratory change with a statin is raised hepatic transaminases."]],
 "c": 0, "cite": D + ", Slide 30"},

{"topic": "Ezetimibe", "io": IO_INTER, "slot": "interaction",
 "q": "Which commonly used product lowers ezetimibe concentrations?",
 "opts": [
  ["Antacids", "Correct. Antacids decrease ezetimibe concentrations, as bile acid sequestrants may; cyclosporine increases them."],
  ["Grapefruit juice", "Grapefruit juice is the CYP-mediated statin interaction, not an ezetimibe one. Antacids lower ezetimibe levels."],
  ["Alcohol", "Alcohol is listed as a niacin interaction. The product that lowers ezetimibe concentrations is antacids."],
  ["Salt substitutes", "Salt substitutes raise potassium with ACE (angiotensin-converting enzyme) inhibitors. Antacids lower ezetimibe."]],
 "c": 0, "cite": D + ", Slide 31"},

{"topic": "Ezetimibe", "io": IO_INTER, "slot": "interaction",
 "q": "What risk increases when ezetimibe is combined with a fibrate?",
 "opts": [
  ["Cholelithiasis", "Correct. Fibric acid derivatives with ezetimibe increase hepatobiliary side effects, leading to cholelithiasis and myopathies."],
  ["Hyperkalemia", "Hyperkalemia is not a lipid-drug interaction; it belongs to ACE inhibitors and angiotensin receptor blockers. The combination raises cholelithiasis."],
  ["Cutaneous flushing", "Flushing is a prostaglandin-mediated niacin effect. Ezetimibe with a fibrate raises cholelithiasis."],
  ["Angioedema", "Angioedema is a bradykinin effect of ACE (angiotensin-converting enzyme) inhibitors. The ezetimibe and fibrate risk is cholelithiasis."]],
 "c": 0, "cite": D + ", Slide 31"},

# ---- PCSK9 inhibitors -------------------------------------------------------------------
{"topic": "PCSK9 inhibitors", "io": IO_CLASS, "slot": "class",
 "q": "Which of these drugs is a PCSK9 inhibitor?",
 "opts": [
  ["Evolocumab", "Correct. Alirocumab and evolocumab are the PCSK9 inhibitors; the -mab suffix marks them as monoclonal antibodies."],
  ["Ezetimibe", "Ezetimibe is the cholesterol absorption inhibitor, an oral drug acting at the brush border. The PCSK9 inhibitors are the -mab antibodies."],
  ["Colesevelam", "Colesevelam is a bile acid sequestrant. The PCSK9 inhibitors are alirocumab and evolocumab."],
  ["Fenofibrate", "Fenofibrate is a fibrate that activates PPAR-alpha. Evolocumab is the PCSK9 inhibitor here."]],
 "c": 0, "cite": D + ", Slide 60"},

{"topic": "PCSK9 inhibitors", "io": IO_MOA, "slot": "mechanism",
 "q": "How do PCSK9 inhibitors lower LDL (low-density lipoprotein) cholesterol?",
 "opts": [
  ["They keep LDL receptors active longer", "Correct. PCSK9 processes hepatic LDL receptors; blocking it keeps the receptors active for longer, lowering LDL concentrations by 43 to 58%."],
  ["They inhibit cholesterol synthesis", "Inhibiting cholesterol synthesis is the statin mechanism. PCSK9 inhibitors preserve hepatic LDL receptors."],
  ["They bind bile acids in the gut", "Binding bile acids is how resins work. PCSK9 inhibitors keep LDL receptors active longer."],
  ["They activate PPAR-alpha in liver", "PPAR-alpha activation is the fibrate mechanism. PCSK9 inhibitors keep hepatic LDL receptors active."]],
 "c": 0, "cite": D + ", Slide 60"},

{"topic": "PCSK9 inhibitors", "io": IO_ADME, "slot": "class",
 "q": "Which description fits alirocumab?",
 "opts": [
  ["Injectable monoclonal antibody", "Correct. Alirocumab and evolocumab are injectable-only monoclonal antibodies, and they are expensive."],
  ["Oral bile acid-binding resin", "Oral resins are cholestyramine, colestipol and colesevelam. Alirocumab is an injectable monoclonal antibody."],
  ["Oral HMG-CoA reductase inhibitor", "Oral HMG-CoA reductase inhibitors are the statins. Alirocumab is an injectable monoclonal antibody against PCSK9."],
  ["Oral cholesterol absorption blocker", "The oral cholesterol absorption inhibitor is ezetimibe. Alirocumab is an injectable monoclonal antibody."]],
 "c": 0, "cite": D + ", Slide 60"},

{"topic": "PCSK9 inhibitors", "io": IO_TOX, "slot": "adverse effect",
 "q": "What is the most serious adverse reaction to evolocumab?",
 "opts": [
  ["Hypersensitivity reactions", "Correct. Hypersensitivity reactions are the most serious adverse reaction listed for the PCSK9 inhibitors."],
  ["Rhabdomyolysis from muscle breakdown", "Rhabdomyolysis is the rare, most severe statin muscle toxicity, not the listed PCSK9 inhibitor reaction."],
  ["Prostaglandin-mediated flushing", "Flushing is a prostaglandin-mediated niacin effect. The most serious evolocumab reaction is hypersensitivity."],
  ["Gallstones (cholelithiasis)", "Cholelithiasis is a fibrate effect. Hypersensitivity is the most serious reaction to PCSK9 inhibitors."]],
 "c": 0, "cite": D + ", Slide 60"},

# ---- the unifying thread ------------------------------------------------------------------
{"topic": "LDL receptor thread", "io": IO_MOA, "slot": "mechanism",
 "q": "Statins, ezetimibe, bile acid sequestrants and PCSK9 inhibitors lower LDL (low-density lipoprotein) through which shared end result?",
 "opts": [
  ["More active hepatic LDL receptors", "Correct. Statins and resins upregulate them, ezetimibe raises their expression by cutting cholesterol supply, and PCSK9 inhibitors keep them active longer."],
  ["Less VLDL secreted by the liver", "Reduced VLDL (very low-density lipoprotein) secretion is how fibrates and niacin lower triglycerides. These four share more LDL receptor activity."],
  ["More HDL made by the liver", "Raising HDL (high-density lipoprotein) is the strength of niacin and fibrates. These four drugs share more hepatic LDL receptors."],
  ["Less bile acid in the intestine", "Only resins deplete intestinal bile acid. The end point all four share is more active hepatic LDL receptors."]],
 "c": 0, "cite": D + ", Slide 18"},
]
