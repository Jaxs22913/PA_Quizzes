# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- Myocardial Ischemia (Lecture 8), topic 2: acute
coronary syndrome, antiplatelets and fibrinolytics.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

SOURCE. Myocardial Ischemia Drugs.pptx slides 40-68 (classification, the
thrombus-formation sequence, aspirin / nitrates / beta blockers / morphine in
acute coronary syndrome, the fibrinolytic system and agents, other
antithrombotics, non-ST-elevation acute coronary syndrome). Picture-only
slides 41-50 and 67 were read by eye into tools/pharm_e2/ocr.json.

WEIGHTING (Dr. McInnis): indications, patient education, adverse effects,
contraindications and drug choice outnumber mechanism plus physiology. The
thrombus-formation slides (42-50) are background physiology and are limited to
six recognition questions.

LEFT OUT ON PURPOSE (no key built on them):
  * the aspirin chew dose, and every other milligram amount (doses are not
    tested);
  * fibrin affinity of reteplase and tenecteplase (true for tenecteplase only);
  * urokinase as an antigenic agent (only streptokinase is);
  * the factor list plasmin lyses;
  * the 75-year, 12-hour, 6-hour, 10-day, 3-month and diastolic-pressure
    cut-offs, the bleeding percentages and the 13 percent / 40 percent trial
    figures (fibrinolytic contraindications are keyed qualitatively, for
    example "severe uncontrolled hypertension" and "recent major surgery");
  * "aspirin and clopidogrel increase coronary blood flow" (slide 13, topic 1);
  * after the independent fact-check: the intravenous-then-oral beta blocker sequence (out of date), acute
    pericarditis as a fibrinolytic contraindication (not in current guidelines), enoxaparin "preferred over
    heparin" (guidelines accept either), prior stroke as a blanket contraindication (keyed the active intracranial
    tumor instead), plasminogen activator inhibitor-1 resistance for reteplase, and the Q-wave equivalence;
  * the cost of alteplase and the cell line each agent is grown in (trivia).

TRUTH WINS: slide 61 says alteplase, reteplase and tenecteplase "activate only
fibrin-bound plasminogen"; the pool keys only the contrast that streptokinase
forms a complex with circulating plasminogen. Morphine (slide 56) is keyed as
pain relief in ST-elevation myocardial infarction and as controversial in
non-ST-elevation acute coronary syndrome, without over-keying.
"""

D = "Myocardial Ischemia Drugs.pptx"
IO_CLASS = "Identify drug classes and commonly prescribed drugs used to treat myocardial ischemia"
IO_MOA = "Describe the molecular mechanism of action of drugs used to treat myocardial ischemia"
IO_IND = "Identify indications for drugs used to treat myocardial ischemia"
IO_ADME = "Describe absorption, distribution, metabolism, and excretion of drugs used to treat myocardial ischemia"
IO_TOX = "Summarize side effects and toxic manifestations of drugs used to treat myocardial ischemia"
IO_AE = "Describe adverse effects of drugs used to treat myocardial ischemia"
IO_CONTRA = "Identify contraindications for drugs used to treat myocardial ischemia"
IO_INTER = "Discuss potential drug-drug, drug-food, and drug-herb interactions with drugs used to treat myocardial ischemia"
IO_PROT = "List commonly used protocols and patient monitoring for myocardial ischemia drug therapy"
IO_EDU = "Outline appropriate patient education for drugs used to treat myocardial ischemia"

QUESTIONS = [

# ---- classification of acute coronary syndrome -------------------------------------
{"topic": "ACS classification", "io": IO_CLASS, "slot": "class",
 "q": "An electrocardiogram shows ST-segment elevation in a patient with ischemic chest discomfort. What is the working diagnosis?",
 "opts": [
  ["ST-elevation myocardial infarction", "Correct. ST-segment elevation with ischemic discomfort defines ST-elevation myocardial infarction, the form for which fibrinolytics are indicated."],
  ["Unstable angina", "Unstable angina and non-ST-elevation infarction both show no ST elevation on the electrocardiogram; ST elevation with ischemic discomfort means ST-elevation myocardial infarction."],
  ["Non-ST-elevation myocardial infarction", "By definition this type has no ST elevation on the tracing. ST-segment elevation with ischemic discomfort identifies ST-elevation myocardial infarction instead."],
  ["Stable angina", "Stable angina is predictable, exertional discomfort and is not an acute coronary syndrome; ST elevation with ischemic discomfort indicates ST-elevation myocardial infarction."]],
 "c": 0, "cite": D + ", Slide 41"},

{"topic": "ACS classification", "io": IO_CLASS, "slot": "class",
 "q": "Which pair of conditions makes up non-ST-elevation acute coronary syndrome?",
 "opts": [
  ["Unstable angina and non-ST-elevation myocardial infarction", "Correct. With no ST elevation on the electrocardiogram the diagnosis is unstable angina or non-ST-elevation myocardial infarction, separated by a biochemical marker."],
  ["Stable angina and non-ST-elevation myocardial infarction", "Stable angina is predictable exertional angina, not an acute coronary syndrome. The non-ST-elevation group is unstable angina plus non-ST-elevation myocardial infarction."],
  ["Unstable angina and ST-elevation myocardial infarction", "ST-elevation myocardial infarction is its own category with ST-segment elevation. The non-ST-elevation group pairs unstable angina with non-ST-elevation infarction."],
  ["Variant angina and ST-elevation myocardial infarction", "ST-elevation infarction is a separate category, and variant angina is vasospastic angina. The non-ST-elevation group is unstable angina plus non-ST-elevation infarction."]],
 "c": 0, "cite": D + ", Slide 41"},

{"topic": "ACS classification", "io": IO_PROT, "slot": "monitoring",
 "q": "With no ST elevation on the electrocardiogram, what separates unstable angina from non-ST-elevation myocardial infarction?",
 "opts": [
  ["A biochemical marker in the blood", "Correct. A biochemical marker of myocardial injury is positive in infarction and negative in unstable angina, which is how the two non-ST-elevation diagnoses are separated."],
  ["The duration of the chest pain", "Pain duration does not define either diagnosis. A biochemical marker of myocardial injury is what separates infarction from unstable angina."],
  ["The response to nitroglycerin", "Response to nitroglycerin does not define either diagnosis; a biochemical marker of myocardial injury separates unstable angina from infarction."],
  ["The presence of Q waves on the tracing", "Q waves on the tracing do not separate the two. A biochemical marker of myocardial injury, positive only in infarction, does."]],
 "c": 0, "cite": D + ", Slide 41"},

# ---- thrombus formation (background physiology) ------------------------------------
{"topic": "Thrombus formation", "io": IO_MOA, "slot": "physiology",
 "q": "Which step begins thrombus formation over an atherosclerotic plaque?",
 "opts": [
  ["Injury to the overlying endothelium", "Correct. Spontaneous plaque rupture or procedural injury such as balloon deployment leaves injured endothelium, which starts platelet adhesion and the clotting cascade."],
  ["Platelet aggregation at the plaque", "Platelet adhesion, activation and aggregation follow the endothelial injury; they do not begin the sequence. Injured endothelium comes first."],
  ["Formation of fibrin strands", "Fibrin strands form later, once thrombin converts fibrinogen. The sequence begins with injury to the endothelium over the plaque."],
  ["Occlusion of the lumen by thrombus", "Complete occlusion by thrombus is the end result of the sequence, not its start. Injury to the overlying endothelium begins it."]],
 "c": 0, "cite": D + ", Slide 43"},

{"topic": "Thrombus formation", "io": IO_MOA, "slot": "physiology",
 "q": "Which mediator links tissue injury, coagulation and the platelet response?",
 "opts": [
  ["Thrombin", "Correct. Thrombin converts fibrinogen to fibrin and also elicits multiple platelet responses, tying injury, coagulation and platelet activation together."],
  ["Plasmin", "Plasmin is the fibrinolytic enzyme that dissolves fibrin. The mediator linking injury, coagulation and platelet response is thrombin."],
  ["Fibrinogen", "Fibrinogen is the substrate that thrombin converts to fibrin, not the link between injury, coagulation and platelets. That link is thrombin."],
  ["Tissue plasminogen activator", "Tissue plasminogen activator converts plasminogen to plasmin in fibrinolysis. The mediator linking injury, coagulation and platelets is thrombin."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": "Thrombus formation", "io": IO_MOA, "slot": "physiology",
 "q": "Which factor starts the plasma clotting cascade at the site of vessel injury?",
 "opts": [
  ["Tissue factor", "Correct. Tissue factor, with factor VIIa, starts the plasma clotting cascade at the injury, leading to prothrombin becoming thrombin and then fibrin."],
  ["Thromboxane A2", "Thromboxane A2 activates and aggregates platelets rather than starting the plasma cascade. Tissue factor starts the cascade."],
  ["Adenosine diphosphate", "Adenosine diphosphate activates and aggregates platelets, it does not start the plasma cascade. Tissue factor does."],
  ["Plasminogen", "Plasminogen is the inactive precursor of the fibrinolytic enzyme plasmin. The clotting cascade is started by tissue factor."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": "Thrombus formation", "io": IO_MOA, "slot": "physiology",
 "q": "What activates and aggregates platelets once collagen is exposed at the injury?",
 "opts": [
  ["Adenosine diphosphate and thromboxane A2", "Correct. Adenosine diphosphate and thromboxane A2 activate and aggregate platelets at the injured plaque surface."],
  ["Tissue factor and factor VIIa", "Tissue factor with factor VIIa starts the plasma clotting cascade and generates thrombin; platelets are activated by adenosine diphosphate and thromboxane A2."],
  ["Fibrinogen and plasminogen", "Fibrinogen is converted to fibrin by thrombin and plasminogen is the precursor of plasmin. Platelets are activated by adenosine diphosphate and thromboxane A2."],
  ["Prothrombin and factor X", "Prothrombin and factor X are plasma clotting factors, not platelet activators. Adenosine diphosphate and thromboxane A2 activate platelets."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": "Thrombus formation", "io": IO_MOA, "slot": "physiology",
 "q": "How does thrombin amplify its own production?",
 "opts": [
  ["By activating factors V and VIII", "Correct. During amplification thrombin activates platelets and factors V and VIII, which assemble with factors IXa on activated platelets to make more thrombin."],
  ["By activating plasminogen to plasmin", "Converting plasminogen to plasmin is fibrinolysis, which dissolves clot. Thrombin amplifies itself by activating factors V and VIII."],
  ["By blocking the action of tissue factor", "Tissue factor starts the cascade during initiation and is not blocked by thrombin. Thrombin amplifies its own production by activating factors V and VIII."],
  ["By converting fibrin back to fibrinogen", "Thrombin converts fibrinogen to fibrin, not the reverse. It amplifies its own production by activating factors V and VIII."]],
 "c": 0, "cite": D + ", Slide 49"},

{"topic": "Thrombus formation", "io": IO_MOA, "slot": "physiology",
 "q": "Where do the assembled clotting factor complexes continue the cascade during propagation?",
 "opts": [
  ["On the surface of activated platelets", "Correct. Assembled complexes on activated platelets convert prothrombin to thrombin and fibrinogen to fibrin and stabilize the clot."],
  ["On the surface of intact endothelium", "Intact endothelium does not host these complexes. Propagation continues on the surface of activated platelets."],
  ["Inside the fibrous cap of the plaque", "The fibrous cap is part of the plaque wall, not the site of propagation. The complexes assemble on the surface of activated platelets."],
  ["Along smooth muscle cell membranes", "Smooth muscle cells lie deeper in the vessel wall. Propagation takes place on the surface of activated platelets."]],
 "c": 0, "cite": D + ", Slide 50"},

# ---- aspirin -------------------------------------------------------------------------
{"topic": "Aspirin in ACS", "io": IO_IND, "slot": "drug choice",
 "q": "Which drug should a patient chew and swallow at the first signs of chest pain from suspected acute coronary syndrome?",
 "opts": [
  ["Aspirin", "Correct. Aspirin is used at the first signs of chest pain and reduces mortality and reinfarction in both ST-elevation and non-ST-elevation acute coronary syndrome."],
  ["Clopidogrel", "Clopidogrel is the antiplatelet substitute for patients allergic to aspirin, not the drug chewed at the first sign of chest pain, which is aspirin."],
  ["Nitroglycerin", "Nitroglycerin is taken sublingually for chest pain relief and does not improve outcomes. The drug chewed and swallowed, which reduces mortality, is aspirin."],
  ["Metoprolol", "Metoprolol is a beta blocker used for protection after infarction. It is not the first-sign drug chewed and swallowed; that is aspirin."]],
 "c": 0, "cite": D + ", Slide 52"},

{"topic": "Aspirin in ACS", "io": IO_EDU, "slot": "education",
 "q": "When should a patient with suspected acute coronary syndrome take aspirin?",
 "opts": [
  ["At the first signs of chest pain", "Correct. Aspirin is used at the first signs of chest pain; early use reduces mortality and reinfarction."],
  ["Only after arriving at the hospital", "Aspirin should not wait for hospital arrival; it is used at the first signs of chest pain because it reduces mortality and reinfarction."],
  ["After the pain has lasted an hour", "Waiting an hour delays benefit. Aspirin is taken at the first signs of chest pain, not after a prolonged delay."],
  ["Once the electrocardiogram confirms infarction", "Aspirin is not held for confirmation. It is used at the first signs of chest pain in both ST-elevation and non-ST-elevation presentations."]],
 "c": 0, "cite": D + ", Slide 52"},

{"topic": "Aspirin in ACS", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which history is a contraindication to aspirin in suspected acute coronary syndrome?",
 "opts": [
  ["Recent intracranial hemorrhage", "Correct. Aspirin is contraindicated with allergy, a recent gastrointestinal bleed or a recent intracranial hemorrhage because it raises bleeding risk."],
  ["Prior myocardial infarction", "Prior infarction is a reason to give aspirin, which decreases reinfarction and cardiac death. Its contraindications are allergy, recent gastrointestinal bleeding and recent intracranial hemorrhage."],
  ["Previous stent placement", "A stent is a reason for antiplatelet therapy, not a contraindication to aspirin. Contraindications are allergy, recent gastrointestinal bleeding and recent intracranial hemorrhage."],
  ["Hyperlipidemia", "Hyperlipidemia is a risk factor for coronary disease and does not preclude aspirin. Contraindications are allergy, recent gastrointestinal bleeding and recent intracranial hemorrhage."]],
 "c": 0, "cite": D + ", Slide 53"},

{"topic": "Aspirin in ACS", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which drug is withheld from a patient with suspected acute coronary syndrome who has an active gastrointestinal bleed?",
 "opts": [
  ["Aspirin", "Correct. A gastrointestinal bleed is a contraindication to aspirin, along with allergy and recent intracranial hemorrhage, because aspirin raises bleeding risk."],
  ["Metoprolol", "An active gastrointestinal bleed does not limit beta blockers; their cautions are bradycardia, hypotension, heart block and severe reactive airway disease."],
  ["Nitroglycerin", "Nitrates are contraindicated by hypotension and phosphodiesterase-5 inhibitors, not a gastrointestinal bleed. Aspirin is the drug withheld in that setting."],
  ["Morphine", "Morphine's concerns are hypotension and allergy, not a gastrointestinal bleed. The drug withheld with a gastrointestinal bleed is aspirin."]],
 "c": 0, "cite": D + ", Slide 53"},

# ---- nitrates ---------------------------------------------------------------------------
{"topic": "Nitrates in ACS", "io": IO_IND, "slot": "indication",
 "q": "Why are nitrates used in acute coronary syndrome?",
 "opts": [
  ["To relieve chest pain", "Correct. Nitrates give relief of chest pain only; they show no mortality benefit and no improvement in outcomes."],
  ["To lower mortality", "Nitrates have no mortality benefit. Aspirin lowers mortality, while nitrates only relieve chest pain."],
  ["To limit infarct size", "Reduced infarct size is a beta blocker benefit. Nitrates provide relief of chest pain without improving outcomes."],
  ["To prevent reinfarction", "Reinfarction is reduced by aspirin. Nitrates are used for chest pain relief and do not improve outcomes."]],
 "c": 0, "cite": D + ", Slide 54"},

{"topic": "Nitrates in ACS", "io": IO_PROT, "slot": "protocol",
 "q": "How are nitrates given as acute coronary syndrome care progresses?",
 "opts": [
  ["Sublingual, then intravenous infusion", "Correct. Therapy starts sublingually until the patient is in the hospital, then changes to an intravenous infusion."],
  ["Intravenous infusion, then sublingual", "The order is reversed here. Care starts with sublingual nitrates and moves to an intravenous infusion once the patient is in hospital."],
  ["Oral, then transdermal patch", "Oral and patch forms are long-acting angina options, not the acute pathway. Acute coronary syndrome care goes sublingual, then intravenous infusion."],
  ["Sublingual, then oral extended-release", "Extended-release oral nitrate is a chronic angina option. In acute coronary syndrome, sublingual dosing is followed by intravenous infusion."]],
 "c": 0, "cite": D + ", Slide 54"},

{"topic": "Nitrates in ACS", "io": IO_AE, "slot": "adverse effect",
 "q": "Which set of adverse reactions is expected with nitrates?",
 "opts": [
  ["Hypotension, headache, reflex tachycardia", "Correct. Nitrate vasodilation causes hypotension and headache, and the pressure fall can trigger reflex tachycardia."],
  ["Hypertension, headache, reflex bradycardia", "Nitrates lower blood pressure rather than raising it, and the reflex response is tachycardia, not bradycardia."],
  ["Hypotension, cough, reflex bradycardia", "Cough is not a nitrate reaction, and the reflex response to vasodilation is tachycardia rather than bradycardia."],
  ["Hypotension, constipation, reflex tachycardia", "Constipation is not a nitrate reaction; the expected adverse reactions are hypotension, headache and reflex tachycardia."]],
 "c": 0, "cite": D + ", Slide 54"},

{"topic": "Nitrates in ACS", "io": IO_INTER, "slot": "contraindication",
 "q": "Which drug group contraindicates nitrates because of the risk of severe hypotension?",
 "opts": [
  ["Phosphodiesterase-5 inhibitors", "Correct. Phosphodiesterase-5 inhibitors are a listed contraindication to nitrates, because together they can cause severe hypotension."],
  ["Beta blockers", "Beta blockers are used together with nitrates in acute coronary syndrome; their own cautions are bradycardia, hypotension and heart block."],
  ["Heparins", "Heparins are anticoagulants with no vasodilator interaction. The drug group contraindicated with nitrates is the phosphodiesterase-5 inhibitors."],
  ["Fibrinolytics", "Fibrinolytics raise bleeding risk but do not interact with nitrates. The contraindicated combination is nitrates with phosphodiesterase-5 inhibitors."]],
 "c": 0, "cite": D + ", Slide 54"},

{"topic": "Nitrates in ACS", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which finding contraindicates nitrates in suspected acute coronary syndrome?",
 "opts": [
  ["Hypotension", "Correct. Hypotension is a listed contraindication, because nitrates lower blood pressure further."],
  ["Hypertension", "High blood pressure is not a contraindication; nitrates lower pressure. The listed contraindications are hypotension and phosphodiesterase-5 inhibitors."],
  ["Ongoing chest pain", "Ongoing chest pain is the reason to give nitrates, for pain relief. The contraindications are hypotension and phosphodiesterase-5 inhibitors."],
  ["Elevated cardiac biomarkers", "Elevated biomarkers indicate infarction and do not bar nitrates. The listed contraindications are hypotension and phosphodiesterase-5 inhibitors."]],
 "c": 0, "cite": D + ", Slide 54"},

# ---- beta blockers ---------------------------------------------------------------------
{"topic": "Beta blockers in ACS", "io": IO_IND, "slot": "indication",
 "q": "Which benefit do beta blockers provide after acute coronary syndrome?",
 "opts": [
  ["Smaller infarct size, fewer sudden deaths", "Correct. Beta blockers reduce infarct size, heart failure incidence and sudden cardiac death."],
  ["Dissolution of the coronary clot", "Dissolving clot is the role of fibrinolytics. Beta blockers reduce infarct size and sudden cardiac death."],
  ["Chest pain relief with no outcome benefit", "That describes nitrates. Beta blockers improve outcomes, reducing infarct size and sudden cardiac death."],
  ["Blockade of platelet aggregation", "Blocking platelets is the work of antiplatelet drugs. Beta blockers lower infarct size and sudden cardiac death."]],
 "c": 0, "cite": D + ", Slide 55"},

{"topic": "Beta blockers in ACS", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which finding calls for caution before giving a beta blocker in acute coronary syndrome?",
 "opts": [
  ["Heart block", "Correct. Heart block is a listed caution, along with bradycardia, hypotension and severe reactive airway disease, because beta blockers slow conduction."],
  ["Sinus tachycardia", "A fast sinus rate is something beta blockers slow; the cautions are bradycardia, hypotension, heart block and severe reactive airway disease."],
  ["Premature ventricular beats", "Premature ventricular beats do not limit beta blockers. The listed cautions are bradycardia, hypotension, heart block and severe reactive airway disease."],
  ["Hypertension", "High blood pressure is a setting where beta blockers help. Low blood pressure, bradycardia and heart block are the cautions."]],
 "c": 0, "cite": D + ", Slide 55"},

{"topic": "Beta blockers in ACS", "io": IO_CONTRA, "slot": "contraindication",
 "q": "A patient with acute coronary syndrome has severe wheezing from reactive airway disease. Which drug class calls for caution?",
 "opts": [
  ["Beta blockers", "Correct. Severe reactive airway disease is a listed caution for beta blockers in acute coronary syndrome."],
  ["Nitrates", "Nitrates are limited by hypotension and phosphodiesterase-5 inhibitors, not reactive airway disease. Beta blockers are the class needing caution."],
  ["Heparins", "Heparins are not limited by reactive airway disease. The class needing caution in severe reactive airway disease is the beta blockers."],
  ["Fibrinolytics", "Fibrinolytic contraindications involve bleeding and related risks, not airway disease. Severe reactive airway disease calls for caution with beta blockers."]],
 "c": 0, "cite": D + ", Slide 55"},

{"topic": "Beta blockers in ACS", "io": IO_PROT, "slot": "monitoring",
 "q": "Which findings should be checked before and after a beta blocker is given in acute coronary syndrome?",
 "opts": [
  ["Heart rate and blood pressure", "Correct. The cautions are bradycardia and hypotension, so heart rate and blood pressure are watched closely."],
  ["Body temperature and weight", "These do not reflect the beta blocker risks. Heart rate and blood pressure are monitored because of bradycardia and hypotension."],
  ["Serum sodium and calcium", "Electrolyte changes are not the main beta blocker concern. Bradycardia and hypotension make heart rate and blood pressure the findings to check."],
  ["Urine output and appetite", "These are not the monitoring points for beta blockers. Heart rate and blood pressure are checked because of bradycardia and hypotension."]],
 "c": 0, "cite": D + ", Slide 55"},

# ---- morphine -------------------------------------------------------------------------------
{"topic": "Morphine", "io": IO_IND, "slot": "indication",
 "q": "Which drug manages chest pain that does not respond to nitrates in ST-elevation myocardial infarction?",
 "opts": [
  ["Morphine", "Correct. Morphine, an opioid analgesic, is used for chest pain unresponsive to nitrates in ST-elevation myocardial infarction."],
  ["Metoprolol", "Metoprolol lowers infarct size and sudden cardiac death but is not the analgesic for pain unresponsive to nitrates. Morphine is used for that."],
  ["Aspirin", "Aspirin reduces mortality and reinfarction, not pain. Morphine is the opioid analgesic used for pain unresponsive to nitrates."],
  ["Alteplase", "Alteplase is a fibrinolytic that restores flow in ST-elevation infarction; it is not an analgesic. Morphine manages nitrate-resistant pain."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": "Morphine", "io": IO_AE, "slot": "adverse effect",
 "q": "Why is morphine controversial in unstable angina and non-ST-elevation myocardial infarction?",
 "opts": [
  ["It may raise mortality", "Correct. Morphine may have increased mortality in unstable angina and non-ST-elevation myocardial infarction, so its use there is controversial."],
  ["It fails to relieve ischemic pain", "Morphine is an opioid analgesic that does relieve pain. The controversy is a possible increase in mortality."],
  ["It markedly increases bleeding risk", "Bleeding risk is the main concern with fibrinolytics and antiplatelet drugs. Morphine's concerns are hypotension, allergy and a possible mortality increase."],
  ["It cannot be combined with aspirin", "Aspirin is given with other therapy at the first signs of chest pain. The controversy is that morphine may increase mortality."]],
 "c": 0, "cite": D + ", Slide 56"},

# ---- fibrinolytic mechanism -------------------------------------------------------------------
{"topic": "Fibrinolytic mechanism", "io": IO_MOA, "slot": "mechanism",
 "q": "What is the shared mechanism of all fibrinolytics?",
 "opts": [
  ["Converting plasminogen to plasmin", "Correct. All fibrinolytics act directly or indirectly to convert plasminogen to plasmin, which lyses the fibrin clot."],
  ["Inhibiting thromboxane A2 synthesis", "Fibrinolytics do not block thromboxane A2; they convert plasminogen to plasmin, which lyses fibrin."],
  ["Neutralizing activated factor X", "Inhibiting activated factor X is an anticoagulant action (heparins, given with fibrinolytics); fibrinolytics convert plasminogen to plasmin."],
  ["Blocking adenosine diphosphate receptors", "Blocking adenosine diphosphate receptors is an antiplatelet action, not fibrinolysis. Fibrinolytics convert plasminogen to plasmin."]],
 "c": 0, "cite": D + ", Slide 58"},

{"topic": "Fibrinolytic mechanism", "io": IO_MOA, "slot": "mechanism",
 "q": "Which active enzyme lyses the fibrin in a clot?",
 "opts": [
  ["Plasmin", "Correct. Plasmin is formed from plasminogen and lyses fibrin."],
  ["Plasminogen", "Plasminogen is inactive in circulation; it must be converted to plasmin, which lyses fibrin."],
  ["Thrombin", "Thrombin forms fibrin from fibrinogen rather than lysing it. Plasmin is the enzyme that lyses fibrin."],
  ["Plasminogen activator inhibitor-1", "Plasminogen activator inhibitor-1 opposes tissue plasminogen activator. Plasmin is the enzyme that lyses fibrin."]],
 "c": 0, "cite": D + ", Slide 58"},

{"topic": "Fibrinolytic mechanism", "io": IO_MOA, "slot": "mechanism",
 "q": "How does streptokinase activate plasminogen?",
 "opts": [
  ["It forms a one-to-one complex with it", "Correct. Streptokinase forms a stable one-to-one complex with plasminogen that exposes a catalytic site and converts plasminogen to plasmin."],
  ["It binds plasminogen already attached to fibrin", "That describes tissue plasminogen activator. Streptokinase instead forms a stable one-to-one complex with plasminogen."],
  ["It is itself converted to plasmin", "Streptokinase is not converted to plasmin; it forms a one-to-one complex with plasminogen that activates it."],
  ["It blocks plasminogen activator inhibitor-1", "Streptokinase does not work by blocking the inhibitor. It forms a stable one-to-one complex with plasminogen."]],
 "c": 0, "cite": D + ", Slide 59"},

# ---- fibrinolytic agents ---------------------------------------------------------------------
{"topic": "Fibrinolytic agents", "io": IO_CLASS, "slot": "drug choice",
 "q": "What advantage do reteplase and tenecteplase have over alteplase?",
 "opts": [
  ["A longer half-life", "Correct. Reteplase and tenecteplase have a longer half-life than tissue plasminogen activator (alteplase)."],
  ["No risk of intracranial hemorrhage", "Every fibrinolytic can cause bleeding, including intracranial hemorrhage. The advantage of these two over alteplase is a longer half-life."],
  ["No risk of allergic reactions", "Allergic reactions are listed for fibrinolytics as a group. The advantage of reteplase and tenecteplase over alteplase is a longer half-life."],
  ["Activation of plasminogen without fibrin", "Activating plasminogen without fibrin is not an advantage; streptokinase is the agent that does not depend on fibrin. The advantage of reteplase and tenecteplase is a longer half-life."]],
 "c": 0, "cite": D + ", Slide 64"},

# ---- fibrinolytic adverse effects -------------------------------------------------------------
{"topic": "Fibrinolytic adverse effects", "io": IO_AE, "slot": "adverse effect",
 "q": "Which adverse effect is shared by all fibrinolytic agents?",
 "opts": [
  ["Bleeding", "Correct. Bleeding, including intracranial hemorrhage, is the adverse effect of all fibrinolytics."],
  ["Pulmonary fibrosis", "Pulmonary fibrosis is not a fibrinolytic effect. The effect shared by all fibrinolytics is bleeding."],
  ["Hypoglycemia", "Fibrinolytics do not affect blood glucose. Their shared adverse effect is bleeding."],
  ["Constipation", "Constipation is not a fibrinolytic adverse effect. The shared adverse effect of all agents is bleeding."]],
 "c": 0, "cite": D + ", Slide 62"},

{"topic": "Fibrinolytic adverse effects", "io": IO_AE, "slot": "adverse effect",
 "q": "Which fibrinolytic is chiefly associated with fever, chills and rash?",
 "opts": [
  ["Streptokinase", "Correct. Fever, chills and skin rash occur mainly with streptokinase; allergic reactions, including anaphylaxis, can occur with any fibrinolytic."],
  ["Alteplase", "Alteplase is a recombinant tissue plasminogen activator, not the agent chiefly linked to fever, chills and rash. That is streptokinase."],
  ["Reteplase", "Reteplase is a recombinant agent and is not the one chiefly linked to fever, chills and rash. Streptokinase is."],
  ["Tenecteplase", "Tenecteplase is a recombinant agent and is not chiefly linked to fever, chills and rash. Streptokinase is."]],
 "c": 0, "cite": D + ", Slide 62"},

{"topic": "Fibrinolytic adverse effects", "io": IO_PROT, "slot": "monitoring",
 "q": "What should be watched for closely after fibrinolytic therapy?",
 "opts": [
  ["Signs of bleeding", "Correct. Bleeding, including intracranial hemorrhage, is the main risk of fibrinolytics, so the patient is monitored for it."],
  ["Blood glucose falls", "Hypoglycemia is not an effect of fibrinolytics. Bleeding is the main risk, so signs of bleeding are watched for."],
  ["Potassium elevation", "Hyperkalemia is not a fibrinolytic effect. Bleeding is the main risk that needs close monitoring."],
  ["Reduced urine output", "Reduced urine output is not a fibrinolytic effect. The monitoring focus is signs of bleeding."]],
 "c": 0, "cite": D + ", Slide 62"},

# ---- fibrinolytic contraindications (nine) ---------------------------------------------------
{"topic": "Fibrinolytic contraindications", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which recent event contraindicates fibrinolytics?",
 "opts": [
  ["Recent major surgery", "Correct. Recent surgery (including organ biopsy, puncture of noncompressible vessels, serious head or facial trauma and cardiopulmonary resuscitation) contraindicates fibrinolytics because of bleeding."],
  ["A recent blood draw", "A draw from a compressible arm vein is not a contraindication. Recent surgery, biopsy or puncture of a noncompressible vessel is."],
  ["A recent dental cleaning", "A routine dental cleaning is not a listed contraindication. Recent surgery, serious trauma or resuscitation are the listed events."],
  ["A recent vaccination", "An injection does not contraindicate fibrinolytics. The listed events are recent surgery, biopsy, serious head or facial trauma and resuscitation."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "Fibrinolytic contraindications", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which bleeding history contraindicates fibrinolytics?",
 "opts": [
  ["Recent serious gastrointestinal bleeding", "Correct. Serious gastrointestinal bleeding in the recent past is a listed contraindication, since fibrinolytics could restart serious bleeding."],
  ["Occasional spotting from hemorrhoids", "Minor hemorrhoidal spotting is not a listed contraindication. Recent serious gastrointestinal bleeding is."],
  ["A nosebleed during childhood", "A remote minor nosebleed does not contraindicate fibrinolytics. Recent serious gastrointestinal bleeding does."],
  ["Bruising after a minor fall", "Minor bruising is not a listed contraindication. The listed bleeding history is recent serious gastrointestinal bleeding."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "Fibrinolytic contraindications", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which blood pressure finding contraindicates fibrinolytics?",
 "opts": [
  ["Severe uncontrolled hypertension", "Correct. Severe uncontrolled hypertension contraindicates fibrinolytics because of the risk of intracranial bleeding."],
  ["Well-controlled hypertension", "Hypertension that is well controlled is not a contraindication; it is severe, uncontrolled hypertension that bars fibrinolytics."],
  ["Mildly raised pressure from pain", "A mild, pain-related rise is not a contraindication. Severe uncontrolled hypertension is."],
  ["Low-normal blood pressure", "Low-normal pressure is not a contraindication to fibrinolytics. Severe uncontrolled hypertension is."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "Fibrinolytic contraindications", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which finding contraindicates fibrinolytics?",
 "opts": [
  ["Active bleeding", "Correct. Active bleeding or a hemorrhagic disorder contraindicates fibrinolytics, which cause bleeding as their main adverse effect."],
  ["Type 2 diabetes mellitus", "Diabetes is a coronary risk factor, not a listed contraindication to fibrinolytics. Active bleeding or a hemorrhagic disorder is."],
  ["Previous myocardial infarction", "A prior infarction is not a contraindication. Active bleeding or a hemorrhagic disorder is."],
  ["Hypercholesterolemia", "High cholesterol is not a contraindication. The listed contraindication is active bleeding or a hemorrhagic disorder."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "Fibrinolytic contraindications", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which neurologic history contraindicates fibrinolytics?",
 "opts": [
  ["Active intracranial tumor", "Correct. An active intracranial process such as a tumor contraindicates fibrinolytics because of the risk of intracranial hemorrhage."],
  ["Migraine headaches", "Migraine is not a listed contraindication. The neurologic contraindication is an active intracranial process such as a tumor."],
  ["Childhood febrile seizure", "A remote febrile seizure is not a listed contraindication. The neurologic contraindication is an active intracranial process such as a tumor."],
  ["Essential tremor", "Essential tremor is a movement disorder and not a contraindication. The neurologic contraindication is an active intracranial process such as a tumor."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "Fibrinolytic contraindications", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which vascular condition contraindicates fibrinolytics?",
 "opts": [
  ["Aortic dissection", "Correct. Aortic dissection is a listed contraindication, since fibrinolytics could worsen bleeding from the torn aortic wall."],
  ["Peripheral artery disease", "Peripheral artery disease is not a contraindication to fibrinolytics. Aortic dissection is."],
  ["Varicose veins", "Varicose veins are a superficial venous problem and not a listed contraindication. The vascular contraindication is aortic dissection."],
  ["Raynaud phenomenon", "Raynaud phenomenon is vasospasm of small digital arteries and not a contraindication. The vascular contraindication is aortic dissection."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "Fibrinolytic contraindications", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which fibrinolytic is contraindicated in a patient who received it before or had an allergic reaction to it?",
 "opts": [
  ["Streptokinase", "Correct. Prior exposure to streptokinase or an allergic reaction to it is a listed contraindication to using it again."],
  ["Alteplase", "Alteplase is a recombinant tissue plasminogen activator, not the agent barred by prior exposure. That is streptokinase."],
  ["Reteplase", "Reteplase is a recombinant agent and is not the one barred by prior exposure. The agent barred after prior exposure or allergy is streptokinase."],
  ["Tenecteplase", "Tenecteplase is a recombinant agent and is not the one barred by prior exposure. The agent barred after prior exposure or allergy is streptokinase."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "Fibrinolytic contraindications", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which patient factor contraindicates fibrinolytics?",
 "opts": [
  ["Pregnancy", "Correct. Pregnancy is a listed contraindication to fibrinolytics, because of bleeding risk."],
  ["Hyperlipidemia", "High cholesterol is a coronary risk factor, not a contraindication to fibrinolytics. The listed patient factor is pregnancy."],
  ["Obesity", "Obesity is a coronary risk factor, not a listed contraindication to fibrinolytics; the listed patient factor is pregnancy."],
  ["Smoking history", "Smoking history is a coronary risk factor, not a fibrinolytic contraindication. The listed patient factor is pregnancy."]],
 "c": 0, "cite": D + ", Slide 63"},

# ---- fibrinolytic indications ------------------------------------------------------------------
{"topic": "Fibrinolytic indications", "io": IO_IND, "slot": "indication",
 "q": "For which condition are fibrinolytics indicated?",
 "opts": [
  ["ST-elevation myocardial infarction", "Correct. Fibrinolytics are indicated in ST-elevation myocardial infarction, where they restore coronary flow by lysing the clot."],
  ["Unstable angina", "Fibrinolytics are not recommended in unstable angina because bleeding risk outweighs benefit. They are indicated in ST-elevation myocardial infarction."],
  ["Non-ST-elevation myocardial infarction", "There is less benefit and the bleeding risk outweighs it, so fibrinolytics are not recommended. They are indicated in ST-elevation myocardial infarction."],
  ["Stable angina", "Stable angina is managed with antianginal drugs; fibrinolytics are indicated in ST-elevation myocardial infarction."]],
 "c": 0, "cite": D + ", Slide 65"},

{"topic": "Fibrinolytic indications", "io": IO_IND, "slot": "indication",
 "q": "Why are fibrinolytics not recommended in non-ST-elevation acute coronary syndrome?",
 "opts": [
  ["Bleeding risk outweighs benefit", "Correct. In non-ST-elevation acute coronary syndrome the bleeding risk is greater than the benefit, so fibrinolytics are not recommended."],
  ["They cannot be combined with aspirin", "Aspirin is used in both ST-elevation and non-ST-elevation syndromes. The reason is that bleeding risk outweighs benefit."],
  ["They cannot be combined with heparins", "Heparins are used in conjunction with fibrinolysis. Fibrinolytics are avoided because bleeding risk outweighs benefit."],
  ["They cause coronary vasospasm", "Vasospasm is not the reason. Fibrinolytics are not recommended because the bleeding risk outweighs the benefit."]],
 "c": 0, "cite": D + ", Slide 68"},

{"topic": "Fibrinolytic indications", "io": IO_IND, "slot": "indication",
 "q": "When do fibrinolytics give the most benefit in ST-elevation myocardial infarction?",
 "opts": [
  ["Early after symptom onset", "Correct. Benefit is greatest when fibrinolytics are given early after symptom onset, and there is less benefit with later presentation."],
  ["Late, after a day of symptoms", "Benefit falls with delay. Fibrinolytics are most useful early after symptom onset."],
  ["Only after stent placement", "Waiting for stent placement is not when fibrinolytics work best. They are most beneficial early after symptom onset."],
  ["After cardiac biomarkers normalize", "Waiting for biomarkers to normalize means the window has passed. Fibrinolytics are most beneficial early after symptom onset."]],
 "c": 0, "cite": D + ", Slide 65"},

# ---- other antithrombotics and non-ST-elevation acute coronary syndrome -----------------------
{"topic": "Other antithrombotics", "io": IO_CLASS, "slot": "class",
 "q": "Which drug class is used before percutaneous coronary intervention and to prevent clots after stent placement?",
 "opts": [
  ["P2Y12 receptor antagonists", "Correct. P2Y12 receptor antagonists, which block the adenosine diphosphate receptor on platelets, are used before percutaneous coronary intervention and as clot prophylaxis with stent placement."],
  ["Glycoprotein IIb/IIIa inhibitors", "These are not routinely recommended before percutaneous coronary intervention. P2Y12 receptor antagonists are the class used before it and with stents."],
  ["Fibrinolytics", "Fibrinolytics lyse clot in ST-elevation myocardial infarction rather than prevent clots after stenting. P2Y12 receptor antagonists do that."],
  ["Beta blockers", "Beta blockers reduce infarct size and sudden cardiac death but do not prevent stent clotting. P2Y12 receptor antagonists provide clot prophylaxis."]],
 "c": 0, "cite": D + ", Slide 66"},

{"topic": "Other antithrombotics", "io": IO_IND, "slot": "indication",
 "q": "Which drug group is used in conjunction with fibrinolytic or antiplatelet therapy to block the clotting cascade?",
 "opts": [
  ["Heparins", "Correct. Heparins are anticoagulants used in conjunction with fibrinolysis or antiplatelet agents."],
  ["Beta blockers", "Beta blockers lower myocardial oxygen demand; they do not block the clotting cascade. Heparins are the group used with fibrinolysis or antiplatelet agents."],
  ["Nitrates", "Nitrates relieve chest pain and do not act on clotting. Heparins are the group used with fibrinolysis or antiplatelet agents."],
  ["Morphine", "Morphine is an opioid analgesic for pain unresponsive to nitrates. Heparins are the group used with fibrinolysis or antiplatelet agents."]],
 "c": 0, "cite": D + ", Slide 66"},

{"topic": "Aspirin in ACS", "io": IO_IND, "slot": "indication",
 "q": "Which outcomes does aspirin reduce in acute coronary syndrome?",
 "opts": [
  ["Reinfarction, stroke and cardiac death", "Correct. Aspirin decreases recurrent ischemia, reinfarction, stroke and cardiac death."],
  ["Resting heart rate and contractility", "Lowering heart rate and contractility is what beta blockers do. Aspirin decreases recurrent ischemia, reinfarction, stroke and cardiac death."],
  ["Preload through venous dilation", "Dilating veins to lower preload is the nitrate effect. Aspirin decreases recurrent ischemia, reinfarction, stroke and cardiac death."],
  ["Clot size through direct lysis", "Direct lysis of clot is the work of fibrinolytics. Aspirin decreases recurrent ischemia, reinfarction, stroke and cardiac death."]],
 "c": 0, "cite": D + ", Slide 53"},

{"topic": "Fibrinolytic adverse effects", "io": IO_AE, "slot": "adverse effect",
 "q": "Which immune reaction is listed for all fibrinolytic agents?",
 "opts": [
  ["Allergic reactions including anaphylaxis", "Correct. Allergic reactions, including anaphylactic reactions, are listed for all fibrinolytic agents; fever, chills and rash occur mainly with streptokinase."],
  ["Allergic reactions only with streptokinase", "Allergic and anaphylactic reactions are listed for all fibrinolytics; it is fever, chills and rash that occur mainly with streptokinase."],
  ["Autoimmune hemolytic anemia", "Autoimmune hemolytic anemia is not a listed fibrinolytic effect. The listed immune reactions are allergic reactions including anaphylaxis."],
  ["Delayed contact dermatitis", "Contact dermatitis is not a listed fibrinolytic effect. The listed immune reactions are allergic reactions including anaphylaxis."]],
 "c": 0, "cite": D + ", Slide 62"},

{"topic": "Fibrinolytic agents", "io": IO_CLASS, "slot": "class",
 "q": "Which of these drugs is a fibrinolytic?",
 "opts": [
  ["Tenecteplase", "Correct. Tenecteplase is a recombinant fibrinolytic, like alteplase and reteplase."],
  ["Enoxaparin", "Enoxaparin is a heparin-type anticoagulant rather than a fibrinolytic. Fibrinolytics include alteplase, reteplase and tenecteplase."],
  ["Clopidogrel", "Clopidogrel is an antiplatelet drug, not a fibrinolytic. Fibrinolytics include alteplase, reteplase and tenecteplase."],
  ["Metoprolol", "Metoprolol is a beta blocker. Fibrinolytics, which activate plasminogen, include alteplase, reteplase and tenecteplase."]],
 "c": 0, "cite": D + ", Slide 64"},

{"topic": "Fibrinolytic agents", "io": IO_CLASS, "slot": "drug choice",
 "q": "How do alteplase, reteplase and tenecteplase compare in their responses and adverse effects?",
 "opts": [
  ["They are very similar", "Correct. The three recombinant tissue plasminogen activators produce very similar responses and adverse effects, chiefly bleeding."],
  ["Reteplase causes far less bleeding", "Reteplase does not avoid bleeding; the three agents have very similar responses and adverse effects, with bleeding the main risk."],
  ["Tenecteplase carries no bleeding risk", "Every fibrinolytic can cause bleeding, including tenecteplase. The three agents have very similar responses and adverse effects."],
  ["Alteplase alone causes allergic reactions", "Allergic reactions are listed for all fibrinolytics, not alteplase alone. The three agents have very similar responses and adverse effects."]],
 "c": 0, "cite": D + ", Slide 61"},

{"topic": "ACS classification", "io": IO_MOA, "slot": "physiology",
 "q": "What happens to an infarct in the hours after coronary occlusion if blood flow is not restored?",
 "opts": [
  ["It grows into ischemic tissue", "Correct. The infarct enlarges over hours and grows into the area of ischemia, which is why restoring coronary blood flow is a goal of therapy."],
  ["It stays the same size", "The infarct does not stay fixed; it grows into the area of ischemia over hours unless flow is restored."],
  ["It shrinks without treatment", "Without restored flow the infarct does not shrink; it grows into the area of ischemia over hours."],
  ["It stays limited to its core", "The infarct does not remain confined to its core; it expands into the surrounding ischemic area over hours."]],
 "c": 0, "cite": D + ", Slide 41"},

]
