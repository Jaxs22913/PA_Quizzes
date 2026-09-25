# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- Lipids (Lecture 7), topic 3: fibrates, niacin and
what each class does to the lipid profile.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

SOURCE. Lipids.pptx slides 32-39, 50-59, 61 and 62.

EMPHASIS (weight only): the class comparison table got little time but three
separate test-question cues -- "which of these would be best at reducing"
triglycerides ("either the fibrates or niacin"), "the only one that's bad for
triglycerides is the bile acid resins", and telling the classes apart on each
lipid. Items therefore ask the DIRECTION and which class leads on which lipid,
never a percentage to recall.

SLIDE WINS: niacin flushing is "prostaglandin mediated" (slide 55); the
recording inverted the causality. Fibrate contraindications include SEVERE
HEPATIC dysfunction (slide 37), which the recording omitted. The fibrate trigger
is the slide's "TG > 1000 mg/dL or low HDL", not the "familial
hypertriglyceridemia" named aloud.

NOT KEYED: the ATP III numeric goals (presented as superseded) and the total
cholesterol formula; niacin supplement-quality counseling (audio only); the
immediate- versus extended-release flushing direction (the slide lists the two
forms without saying which flushes more). No doses.
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

# ---- fibrates -------------------------------------------------------------------------
{"topic": "Fibrates", "io": IO_MOA, "slot": "mechanism",
 "q": "Which nuclear transcription factor do fibrates activate?",
 "opts": [
  ["PPAR-alpha", "Correct. Fibrates activate PPAR-alpha, increasing fatty acid oxidation (so less VLDL, very low-density lipoprotein, is secreted) and increasing ApoA-1 expression."],
  ["The LDL receptor", "The LDL (low-density lipoprotein) receptor is a cell-surface receptor that statins, resins and PCSK9 inhibitors increase; fibrates act on PPAR-alpha."],
  ["HMG-CoA reductase", "HMG-CoA reductase is the statin target, an enzyme rather than a transcription factor. Fibrates activate PPAR-alpha."],
  ["PCSK9", "PCSK9 processes hepatic LDL receptors and is blocked by monoclonal antibodies. Fibrates activate PPAR-alpha."]],
 "c": 0, "cite": D + ", Slide 34"},

{"topic": "Fibrates", "io": IO_MOA, "slot": "mechanism",
 "q": "How do fibrates lower triglycerides?",
 "opts": [
  ["More fatty acid oxidation, less VLDL", "Correct. Increased fatty acid oxidation reduces secretion of triglyceride-rich VLDL (very low-density lipoprotein), lowering triglycerides by 20 to 50%."],
  ["Less fatty acid release from fat", "Reduced fatty acid mobilization from adipose tissue is the niacin mechanism. Fibrates increase fatty acid oxidation."],
  ["Binding bile acids in the gut", "Binding bile acids is the resin mechanism, and resins can raise triglycerides. Fibrates increase fatty acid oxidation."],
  ["Blocking cholesterol absorption", "Blocking intestinal cholesterol absorption is ezetimibe's mechanism, with little triglyceride effect. Fibrates increase fatty acid oxidation."]],
 "c": 0, "cite": D + ", Slide 34"},

{"topic": "Fibrates", "io": IO_MOA, "slot": "mechanism",
 "q": "How do fibrates raise HDL (high-density lipoprotein)?",
 "opts": [
  ["They increase ApoA-1 expression", "Correct. PPAR-alpha activation increases expression of ApoA-1, the HDL apolipoprotein, raising HDL by 10 to 35%."],
  ["They block HDL breakdown in the gut", "HDL is not broken down in the gut. Fibrates raise HDL by increasing ApoA-1 expression."],
  ["They inhibit HMG-CoA reductase", "HMG-CoA reductase inhibition is the statin mechanism. Fibrates raise HDL through increased ApoA-1 expression."],
  ["They bind cholesterol in the bile", "Binding in the bile is not a fibrate action. Fibrates raise HDL by increasing ApoA-1 expression."]],
 "c": 0, "cite": D + ", Slide 34"},

{"topic": "Fibrates", "io": IO_IND, "slot": "indication",
 "q": "What is the primary indication for a fibrate?",
 "opts": [
  ["Triglycerides over 1000 or low HDL", "Correct. The primary indication is triglycerides above 1000 mg/dL or low HDL (high-density lipoprotein) cholesterol."],
  ["LDL over 190 in a young adult", "LDL (low-density lipoprotein) above 190 mg/dL is a statin benefit group. Fibrates are for very high triglycerides or low HDL."],
  ["High LDL during pregnancy", "Pregnancy contraindicates fibrates; resins are the class approved in pregnancy."],
  ["Statin-induced raised enzymes", "Rising liver enzymes on a statin are managed by lowering the dose or pausing it, not with a fibrate, whose own indication is very high triglycerides or low HDL."]],
 "c": 0, "cite": D + ", Slide 39"},

{"topic": "Fibrates", "io": IO_AE, "slot": "adverse effect",
 "q": "Which adverse effect is characteristic of fibrates?",
 "opts": [
  ["Cholelithiasis", "Correct. Fibrate adverse effects are gastrointestinal (nausea, abdominal pain, diarrhea), cholelithiasis and myopathy."],
  ["Cutaneous flushing", "Prostaglandin-mediated flushing is the hallmark of niacin. Fibrates cause cholelithiasis, myopathy and gastrointestinal effects."],
  ["Vitamin malabsorption", "Malabsorption of vitamins A, D, E and K and folic acid is a resin effect. Fibrates cause cholelithiasis."],
  ["Hypersensitivity", "Hypersensitivity reactions are the most serious PCSK9 inhibitor effect. Fibrates characteristically cause cholelithiasis."]],
 "c": 0, "cite": D + ", Slide 36"},

{"topic": "Fibrates", "io": IO_CONTRA, "slot": "contraindication",
 "q": "In which patient is a fibrate contraindicated?",
 "opts": [
  ["One with existing gallbladder disease", "Correct. Fibrate contraindications are pregnancy, severe hepatic or renal dysfunction, and existing gallbladder disease; cholelithiasis is also an adverse effect."],
  ["One with triglycerides over 1000 mg/dL", "Triglycerides above 1000 mg/dL are the primary indication for a fibrate, not a contraindication."],
  ["One with a low HDL cholesterol", "Low HDL (high-density lipoprotein) is a primary fibrate indication, since fibrates raise HDL by 10 to 35%."],
  ["One with well-controlled diabetes", "Diabetes is a relative contraindication to niacin, not to fibrates. Existing gallbladder disease contraindicates fibrates."]],
 "c": 0, "cite": D + ", Slide 37"},

{"topic": "Fibrates", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which organ dysfunction, when severe, contraindicates a fibrate?",
 "opts": [
  ["Hepatic or renal", "Correct. Severe hepatic or renal dysfunction contraindicates fibrates, along with pregnancy and existing gallbladder disease."],
  ["Pulmonary or cardiac", "Lung or heart dysfunction is not on the fibrate contraindication list. Severe hepatic or renal dysfunction is."],
  ["Thyroid or adrenal", "Endocrine gland dysfunction is not a listed fibrate contraindication. Severe hepatic or renal dysfunction is."],
  ["Pancreatic or splenic", "These are not on the list. Fibrates are contraindicated in severe hepatic or renal dysfunction."]],
 "c": 0, "cite": D + ", Slide 37"},

{"topic": "Fibrates", "io": IO_INTER, "slot": "interaction",
 "q": "A patient on warfarin is started on gemfibrozil. Which interaction is expected?",
 "opts": [
  ["Increased anticoagulant effect", "Correct. Fibrates increase the anticoagulant effect of warfarin; they also interact with statins, ezetimibe and bile acid sequestrants."],
  ["Reduced warfarin absorption", "Reduced warfarin absorption is the bile acid sequestrant interaction, avoided by separating the doses. Fibrates increase warfarin's effect."],
  ["Reduced anticoagulant effect", "The direction is the reverse: fibrates increase the anticoagulant effect of warfarin."],
  ["No interaction is expected", "There is a listed interaction: fibrates increase warfarin's anticoagulant effect."]],
 "c": 0, "cite": D + ", Slide 38"},

{"topic": "Fibrates", "io": IO_INTER, "slot": "interaction",
 "q": "Why is a statin combined with a fibrate only with caution?",
 "opts": [
  ["Higher risk of myopathy", "Correct. Both classes can cause myopathy, so they are combined cautiously; gemfibrozil is a relative contraindication with statins."],
  ["Loss of LDL lowering", "The combination does not cancel the statin's LDL (low-density lipoprotein) lowering. The concern is added myopathy risk."],
  ["Higher risk of flushing", "Flushing is a niacin effect. The concern with a statin plus a fibrate is myopathy."],
  ["Higher risk of hyperkalemia", "Potassium is not the concern of this pair. The caution is because of increased myopathy risk."]],
 "c": 0, "cite": D + ", Slide 22"},

# ---- niacin -----------------------------------------------------------------------------
{"topic": "Niacin", "io": IO_CLASS, "slot": "class",
 "q": "Which form of niacin is NOT effective as an antilipemic?",
 "opts": [
  ["Niacinamide", "Correct. Niacin is a B-complex vitamin; nicotinic acid is the antilipemic form, and its amide, niacinamide (nicotinamide), is not effective."],
  ["Nicotinic acid", "Nicotinic acid is the form used as an antilipemic. The amide form, niacinamide, is the ineffective one."],
  ["Extended-release niacin", "Extended-release niacin is a prescription antilipemic product. Niacinamide is the form that does not work."],
  ["Immediate-release niacin", "Immediate-release niacin is an antilipemic product (a supplement or by prescription). Niacinamide is ineffective."]],
 "c": 0, "cite": D + ", Slide 50"},

{"topic": "Niacin", "io": IO_MOA, "slot": "mechanism",
 "q": "How does niacin reduce hepatic VLDL (very low-density lipoprotein) production?",
 "opts": [
  ["Less fatty acid mobilized from fat", "Correct. Niacin decreases mobilization of free fatty acids from adipose tissue, so the liver makes less triglyceride, VLDL and apo B; LDL falls and HDL rises."],
  ["More fatty acid oxidation", "Increasing fatty acid oxidation through PPAR-alpha is the fibrate mechanism. Niacin reduces fatty acid mobilization from adipose tissue."],
  ["Binding of bile acids", "Binding bile acids is the resin mechanism, which may actually raise VLDL. Niacin reduces fatty acid mobilization."],
  ["Blocking cholesterol uptake", "Blocking intestinal cholesterol uptake is ezetimibe's mechanism. Niacin reduces fatty acid mobilization from adipose tissue."]],
 "c": 0, "cite": D + ", Slide 53"},

{"topic": "Niacin", "io": IO_MOA, "slot": "adverse effect",
 "q": "What mediates the cutaneous flushing caused by niacin?",
 "opts": [
  ["Prostaglandins", "Correct. Niacin flushing is a prostaglandin-mediated effect, which is why premedication with aspirin minimizes it."],
  ["Bradykinin", "Bradykinin accumulation causes the cough and angioedema of ACE (angiotensin-converting enzyme) inhibitors, not niacin flushing."],
  ["Histamine", "Histamine is not the described mediator. Niacin flushing is prostaglandin mediated and blunted by aspirin."],
  ["Serotonin", "Serotonin is not the described mediator. Niacin flushing is a prostaglandin-mediated effect."]],
 "c": 0, "cite": D + ", Slide 55"},

{"topic": "Niacin", "io": IO_EDU, "slot": "education",
 "q": "A patient starting niacin asks how to reduce the flushing. What is recommended?",
 "opts": [
  ["Take aspirin beforehand", "Correct. Flushing is prostaglandin mediated and is minimized by premedication with aspirin."],
  ["Take it with alcohol", "Alcohol is listed as a niacin interaction and does not prevent flushing. Aspirin premedication does."],
  ["Take it with grapefruit juice", "Grapefruit juice is a statin interaction and has no role in niacin flushing. Aspirin premedication minimizes it."],
  ["Take it with an antacid", "Antacids lower ezetimibe levels and do nothing for niacin flushing. Aspirin premedication minimizes it."]],
 "c": 0, "cite": D + ", Slide 55"},

{"topic": "Niacin", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which is an ABSOLUTE contraindication to niacin?",
 "opts": [
  ["Chronic liver disease", "Correct. Chronic liver disease is the absolute contraindication; peptic ulcer disease, symptomatic gout, significant hyperuricemia and diabetes are relative ones."],
  ["Peptic ulcer disease", "Peptic ulcer disease is a relative, not absolute, contraindication to niacin. Chronic liver disease is absolute."],
  ["History of symptomatic gout", "Symptomatic gout is a relative contraindication, because niacin raises uric acid. Chronic liver disease is absolute."],
  ["Diabetes with glucose intolerance", "Diabetes is a relative contraindication, since niacin decreases glucose tolerance. Chronic liver disease is absolute."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": "Niacin", "io": IO_TOX, "slot": "adverse effect",
 "q": "Why is niacin a relative contraindication in a patient with symptomatic gout?",
 "opts": [
  ["It raises uric acid", "Correct. At larger doses niacin raises liver enzymes, glucose and uric acid, so gout and significant hyperuricemia are relative contraindications."],
  ["It causes gallstones", "Cholelithiasis is a fibrate effect. Niacin's problem in gout is that it raises uric acid."],
  ["It raises potassium", "Raised potassium is an ACE (angiotensin-converting enzyme) inhibitor effect. Niacin raises uric acid."],
  ["It lowers kidney blood flow", "Reduced renal blood flow is not the described mechanism. Niacin raises uric acid at larger doses."]],
 "c": 0, "cite": D + ", Slide 55"},

{"topic": "Niacin", "io": IO_AE, "slot": "adverse effect",
 "q": "What does niacin do to glucose control at larger doses?",
 "opts": [
  ["Decreases glucose tolerance", "Correct. Larger doses raise glucose and decrease glucose tolerance, making diabetes a relative contraindication."],
  ["Improves glucose tolerance", "The reverse: niacin decreases glucose tolerance and raises glucose at larger doses."],
  ["Masks hypoglycemia", "Masking hypoglycemia is a beta blocker effect. Niacin decreases glucose tolerance."],
  ["Has no glucose effect", "Niacin does affect glucose: larger doses raise it and decrease glucose tolerance."]],
 "c": 0, "cite": D + ", Slide 55"},

{"topic": "Niacin", "io": IO_IND, "slot": "indication",
 "q": "For which lipid pattern is niacin particularly useful?",
 "opts": [
  ["Atherogenic dyslipidemia", "Correct. Niacin is useful for atherogenic dyslipidemia and as combination therapy when atherogenic dyslipidemia comes with elevated LDL (low-density lipoprotein)."],
  ["Isolated high HDL", "A high HDL (high-density lipoprotein) is desirable and not a treatment target; niacin is used for atherogenic dyslipidemia."],
  ["Familial dysbetalipoproteinemia", "Familial dysbetalipoproteinemia is an absolute contraindication to resins, not niacin's listed indication."],
  ["Pregnancy-related high LDL", "Resins are the class approved in pregnancy. Niacin's place is atherogenic dyslipidemia."]],
 "c": 0, "cite": D + ", Slide 58"},

{"topic": "Niacin", "io": IO_INTER, "slot": "interaction",
 "q": "Which substance is listed as a niacin interaction?",
 "opts": [
  ["Alcohol", "Correct. Niacin interactions are statins, bile acid sequestrants and alcohol."],
  ["Antacids", "Antacids lower ezetimibe concentrations; they are not a listed niacin interaction."],
  ["Warfarin", "Warfarin's effect is increased by fibrates and its absorption reduced by resins; it is not a listed niacin interaction."],
  ["Thyroxine", "Thyroxine absorption is reduced by bile acid sequestrants; it is not listed with niacin, whose interactions include alcohol."]],
 "c": 0, "cite": D + ", Slide 57"},

{"topic": "Niacin", "io": IO_TOX, "slot": "adverse effect",
 "q": "Which adverse effects are listed for the lovastatin and extended-release niacin combination?",
 "opts": [
  ["Hepatotoxicity, myopathy and flushing", "Correct. The combination carries the statin's muscle and liver risks and niacin's flushing."],
  ["Cough, angioedema and hyperkalemia", "Cough, angioedema and hyperkalemia are ACE (angiotensin-converting enzyme) inhibitor effects, not those of a lipid combination."],
  ["Bloating, constipation and flatulence", "Bloating, constipation and flatulence are bile acid sequestrant effects. The lovastatin and niacin combination causes hepatotoxicity, myopathy and flushing."],
  ["Gallstones, nausea and diarrhea", "Gallstones with nausea and diarrhea point to fibrates. The combination's listed effects are hepatotoxicity, myopathy and flushing."]],
 "c": 0, "cite": D + ", Slide 59"},

# ---- class lipid profiles -----------------------------------------------------------------
{"topic": "Lipid profiles by class", "io": IO_IND, "slot": "drug choice",
 "q": "A patient's only lipid problem is a triglyceride level over 1000 mg/dL. Which class is most appropriate?",
 "opts": [
  ["A fibrate", "Correct. Triglycerides over 1000 mg/dL are the primary fibrate indication; fibrates lower triglycerides by 20 to 50% (niacin by a similar amount)."],
  ["A bile acid sequestrant", "Resins can raise triglycerides and are contraindicated above 400 mg/dL, so they are the wrong choice here."],
  ["Ezetimibe", "Ezetimibe lowers triglycerides only about 8%, far too little for a level over 1000 mg/dL."],
  ["A PCSK9 inhibitor", "PCSK9 inhibitors lower LDL (low-density lipoprotein) by keeping LDL receptors active; triglycerides over 1000 mg/dL call for a fibrate."]],
 "c": 0, "cite": D + ", Slide 39"},

{"topic": "Lipid profiles by class", "io": IO_AE, "slot": "adverse effect",
 "q": "Which lipid-lowering class can RAISE triglycerides?",
 "opts": [
  ["Bile acid sequestrants", "Correct. Resins show no change or a rise in triglycerides, because they may increase VLDL (very low-density lipoprotein) production."],
  ["Fibric acid derivatives", "Fibrates lower triglycerides by 20 to 50%; they are the treatment for very high levels."],
  ["Nicotinic acid (niacin)", "Niacin lowers triglycerides by 20 to 50% and raises HDL (high-density lipoprotein) the most of any class."],
  ["HMG-CoA reductase inhibitors", "Statins lower triglycerides modestly, by about 7 to 30%. Resins are the class that can raise them."]],
 "c": 0, "cite": D + ", Slide 61"},

{"topic": "Lipid profiles by class", "io": IO_IND, "slot": "indication",
 "q": "Which class produces the largest rise in HDL (high-density lipoprotein) cholesterol?",
 "opts": [
  ["Nicotinic acid", "Correct. Niacin raises HDL by 15 to 35%, the largest rise of any class; fibrates follow at 10 to 35%."],
  ["Ezetimibe", "Ezetimibe's effect on HDL is insignificant. Niacin produces the largest rise."],
  ["Bile acid sequestrants", "Resins raise HDL only 3 to 5%. Niacin produces the largest HDL rise."],
  ["Statins", "Statins raise HDL by only 5 to 15%. Niacin produces the largest rise."]],
 "c": 0, "cite": D + ", Slide 61"},

{"topic": "Lipid profiles by class", "io": IO_IND, "slot": "indication",
 "q": "What is ezetimibe's effect on HDL (high-density lipoprotein) cholesterol?",
 "opts": [
  ["Insignificant", "Correct. Ezetimibe lowers LDL (low-density lipoprotein) modestly and triglycerides slightly, with an insignificant effect on HDL."],
  ["A large rise", "A large HDL rise belongs to niacin and fibrates. Ezetimibe's effect on HDL is insignificant."],
  ["A sharp fall", "Ezetimibe does not lower HDL; its effect on HDL is insignificant while it lowers LDL about 18%."],
  ["A rise greater than niacin", "No class raises HDL more than niacin. Ezetimibe's HDL effect is insignificant."]],
 "c": 0, "cite": D + ", Slide 61"},

{"topic": "Lipid profiles by class", "io": IO_IND, "slot": "indication",
 "q": "Which class lowers LDL (low-density lipoprotein) cholesterol the most?",
 "opts": [
  ["Statins", "Correct. Statins lower LDL by 18 to 55%, the most of any class; they are the most efficacious and first line."],
  ["Fibrates", "Fibrates lower LDL only 5 to 20%; their strength is triglycerides and HDL (high-density lipoprotein)."],
  ["Niacin", "Niacin lowers LDL 5 to 25%; its strengths are raising HDL (high-density lipoprotein) and lowering triglycerides."],
  ["Ezetimibe", "Ezetimibe lowers LDL about 18% and is used as an add-on to a statin."]],
 "c": 0, "cite": D + ", Slide 61"},

{"topic": "Lipid profiles by class", "io": IO_IND, "slot": "indication",
 "q": "Which two classes both lower triglycerides by 20 to 50% and raise HDL (high-density lipoprotein) substantially?",
 "opts": [
  ["Fibrates and niacin", "Correct. Both lower triglycerides by 20 to 50% and raise HDL (niacin 15 to 35%, fibrates 10 to 35%)."],
  ["Resins and ezetimibe", "Resins can raise triglycerides and ezetimibe barely affects HDL. Fibrates and niacin share this profile."],
  ["Statins and resins", "Statins and resins are chiefly LDL (low-density lipoprotein) lowering agents, and resins can raise triglycerides."],
  ["Ezetimibe and statins", "These lower LDL (low-density lipoprotein) through the supply and synthesis sides. Fibrates and niacin lower triglycerides and raise HDL."]],
 "c": 0, "cite": D + ", Slide 61"},

{"topic": "Lipid profiles by class", "io": IO_EDU, "slot": "education",
 "q": "Which lifestyle measure raises HDL (high-density lipoprotein) cholesterol?",
 "opts": [
  ["Exercise", "Correct. HDL increases with exercise, a lifestyle measure that complements the drug classes that raise it, niacin and fibrates."],
  ["Grapefruit juice", "Grapefruit juice is a CYP-mediated statin interaction, not a way to raise HDL. Exercise raises HDL."],
  ["Salt substitutes", "Salt substitutes add potassium and matter with ACE (angiotensin-converting enzyme) inhibitors. Exercise raises HDL."],
  ["Fasting before meals", "Fasting before meals is not a listed way to raise HDL; exercise is the lifestyle measure that raises it."]],
 "c": 0, "cite": D + ", Slide 62"},

{"topic": "Lipid profiles by class", "io": IO_CONTRA, "slot": "drug choice",
 "q": "A patient with high triglycerides has a history of symptomatic gout. Which triglyceride-lowering option is best avoided?",
 "opts": [
  ["Niacin", "Correct. Niacin raises uric acid, so symptomatic gout and significant hyperuricemia are relative contraindications."],
  ["Fenofibrate", "Gout is not a fibrate contraindication; fenofibrate lowers triglycerides without raising uric acid."],
  ["Gemfibrozil", "Gemfibrozil is a fibrate; its contraindications are pregnancy, severe hepatic or renal dysfunction and gallbladder disease, not gout."],
  ["Bezafibrate", "Bezafibrate is a fibrate, and gout is not on the fibrate contraindication list. Niacin is the one to avoid."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": "Lipid profiles by class", "io": IO_CONTRA, "slot": "drug choice",
 "q": "A patient with high triglycerides has existing gallbladder disease. Which agent should be avoided?",
 "opts": [
  ["Fenofibrate", "Correct. Existing gallbladder disease contraindicates fibrates, which cause cholelithiasis."],
  ["Niacin", "Gallbladder disease is not a niacin contraindication; niacin's are chronic liver disease (absolute) and gout, peptic ulcer and diabetes (relative)."],
  ["Atorvastatin", "Gallbladder disease is not a statin contraindication; statins are contraindicated in hepatic disease and pregnancy."],
  ["Evolocumab", "Gallbladder disease is not a listed contraindication for PCSK9 inhibitors, whose most serious reaction is hypersensitivity."]],
 "c": 0, "cite": D + ", Slide 37"},
]
