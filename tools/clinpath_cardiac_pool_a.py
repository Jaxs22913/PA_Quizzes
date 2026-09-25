# -*- coding: utf-8 -*-
"""Clinical Pathophysiology I, Lecture 6 -- Cardiac Pathophysiology, part A.

Coronary heart disease, atherosclerosis and plaque, then ischemia and the
coronary syndromes. Part B carries valves, myocardium and pericardium.

MECHANISM ONLY, per [[clin_path_exam_spec]]: the line between this course and
Clinical Medicine and Surgery is drawn at pathophysiology against management,
so nothing here asks what is given or done. The deck cooperates -- it is a
mechanism lecture throughout -- but the temptation is the numbers, and the
numbers that survive are the ones that mean something: 75 percent occlusion
before flow is compromised, 30 minutes to irreversible necrosis, and the
distribution of infarcts across the three coronary arteries.

No recording exists for this lecture, so every question comes off the slides.
"""

D = "6. Cardiac Pathophysiology for posting.pptx"
IO_LIPO = "Review the different lipoproteins"
IO_MOLEC = "Describe the molecular mechanisms of common cardiopathies"
IO_CHD = "Compare and contrast the various etiologies and risk factors for coronary heart disease"
IO_PLAQUE = ("Describe the pathological processes and risk factors for the formation of "
             "coronary atherosclerosis and plaque")
IO_ISCH = "Explain the pathophysiology of cardiac ischemia"
IO_SYND = ("Compare and contrast the etiologies and pathophysiological processes of "
           "coronary syndromes")
IO_ANGINA = ("Describe the etiologies and pathophysiological processes for angina pectoris")
IO_ACS = ("Compare and contrast the etiologies and pathophysiological processes of acute "
          "coronary syndrome")

QUESTIONS = [

{"topic": "Coronary heart disease", "io": IO_CHD, "slot": "mechanism",
 "q": "What defines coronary heart disease?",
 "opts": [
  ["Insufficient delivery of oxygenated blood to the myocardium because of atherosclerotic vessels",
   "Correct. The definition is about supply failing rather than about pain or any particular syndrome, which is why so many different presentations sit underneath it."],
  ["Failure of the myocardium to contract because of intrinsic muscle disease",
   "That describes a cardiomyopathy. Coronary heart disease is a problem of blood supply to muscle that is itself capable of working."],
  ["Inflammation of the coronary arteries with leukocyte infiltration",
   "Inflammation participates in plaque formation, but the disease is defined by inadequate oxygen delivery rather than by inflammation itself."],
  ["Obstruction of venous drainage from the myocardium",
   "The problem is arterial supply. Venous drainage is not the mechanism described."]],
 "c": 0, "cite": D + ", Slide 4"},

{"topic": "Coronary heart disease", "io": IO_CHD, "slot": "mechanism",
 "q": "At what point does myocardium become ischemic?",
 "opts": [
  ["When metabolic demand for oxygen exceeds supply",
   "Correct. It is a relationship rather than a threshold, which is why ischemia can arise either from supply falling or from demand rising with the supply unchanged."],
  ["When coronary blood flow falls below a fixed absolute value",
   "No absolute flow figure defines it; what matters is flow relative to what the muscle is demanding at that moment."],
  ["Only once a coronary artery is completely occluded",
   "Complete occlusion is one route to it, but ischemia begins well before that whenever demand outruns supply."],
  ["Only when the patient experiences chest pain",
   "Pain is a symptom that may or may not appear; ischemia is defined by the supply and demand mismatch itself."]],
 "c": 0, "cite": D + ", Slide 4"},

{"topic": "Coronary heart disease", "io": IO_CHD, "slot": "mechanism",
 "q": "What are the consequences of myocardial ischemia?",
 "opts": [
  ["Abnormal heart function and abnormal rhythm",
   "Correct. Two immediate consequences and one that depends on duration, which is why time is the variable that decides how much muscle is lost. With irreversible damage if prolonged."],
  ["Abnormal rhythm only, with function preserved throughout",
   "Function is affected as well; the ischemic myocardium cannot contract normally."],
  ["Immediate irreversible damage in every case",
   "Damage becomes irreversible only if the ischemia is prolonged; brief ischemia does not kill the cell."],
  ["Valvular incompetence as the first consequence",
   "Valve function is not the described consequence of myocardial ischemia."]],
 "c": 0, "cite": D + ", Slide 4"},

{"topic": "Coronary heart disease", "io": IO_CHD, "slot": "aetiology",
 "q": "Atherosclerosis narrows the coronary lumen. Which processes does that narrowing predispose to?",
 "opts": [
  ["Thrombosis, coronary vasospasm and endothelial cell dysfunction",
   "Correct. The narrowing is the setting rather than the whole disease: what precipitates an event is one of these three acting on an already narrowed vessel."],
  ["Valvular calcification and regurgitation",
   "Valve disease is a separate process and is not a consequence of coronary narrowing."],
  ["Pericardial effusion and tamponade",
   "Pericardial disease is not precipitated by coronary narrowing."],
  ["Myocardial leukocyte infiltration and necrosis without vessel involvement",
   "That describes myocarditis, which is not a consequence of coronary atherosclerosis."]],
 "c": 0, "cite": D + ", Slide 8"},

{"topic": "Coronary heart disease", "io": IO_CHD, "slot": "aetiology",
 "q": "Which are given as uncommon causes of coronary heart disease?",
 "opts": [
  ["Reduced oxygen content of the blood, and poor perfusion",
   "Correct. Both reach the same endpoint from outside the coronary artery: the vessel may be open, but what flows through it either carries too little oxygen or arrives at too low a pressure."],
  ["Coronary vasospasm and thrombosis",
   "These are common mechanisms acting on a narrowed vessel rather than the uncommon causes."],
  ["Familial hypercholesterolemia and high fat diet",
   "These are mechanisms of abnormal lipid metabolism contributing to atherosclerosis, not the uncommon causes listed."],
  ["Rheumatic fever and infective endocarditis",
   "These damage valves rather than causing coronary heart disease."]],
 "c": 0, "cite": D + ", Slide 8"},

{"topic": "Microcirculation", "io": IO_CHD, "slot": "mechanism",
 "q": "How can abnormalities of the microcirculation produce cardiac ischemia?",
 "opts": [
  ["Endothelial cells in small vessels regulate the vasculature abnormally",
   "Correct. The large arteries may look adequate while control of flow at the small vessel level has failed, which is why ischemia is possible without a major stenosis. So blood supply is controlled abnormally."],
  ["Small vessels become mechanically obstructed by calcification",
   "Abnormal regulation by endothelial cells is the described mechanism rather than calcification."],
  ["The microcirculation carries blood away from the myocardium",
   "The microcirculation supplies the myocardium; abnormal regulation of that supply is the problem."],
  ["Small vessels rupture, producing intramyocardial hemorrhage",
   "Rupture is not the described mechanism in the microcirculation."]],
 "c": 0, "cite": D + ", Slide 9"},

{"topic": "Risk factors", "io": IO_PLAQUE, "slot": "risk factor",
 "q": "Which are listed as MAJOR risk factors for coronary atherosclerosis?",
 "opts": [
  ["Age, family history, abnormal lipids, smoking, hypertension, diabetes and obesity",
   "Correct. Note that most of them are acquired rather than fixed, which is what separates them from the two that cannot be altered, age and family history."],
  ["Male sex, homocysteine and high sensitivity C reactive protein",
   "These are listed as PROBABLE risk factors rather than major ones."],
  ["Alcohol, pregnancy and recent viral illness",
   "These are factors in dilated cardiomyopathy rather than risk factors for atherosclerosis."],
  ["Rheumatic fever and bicuspid valve",
   "These relate to valvular disease rather than to coronary atherosclerosis."]],
 "c": 0, "cite": D + ", Slide 10"},

{"topic": "Risk factors", "io": IO_PLAQUE, "slot": "risk factor",
 "q": "Which are listed as PROBABLE rather than major risk factors?",
 "opts": [
  ["Male sex, homocysteine and high sensitivity C reactive protein",
   "Correct. Two of the three are laboratory measurements rather than clinical facts, which is part of why they sit in the weaker category."],
  ["Hypertension, diabetes and obesity",
   "All three are in the major category. The probable ones are male sex, homocysteine and high sensitivity C reactive protein."],
  ["Age and family history",
   "Both are major risk factors, and they are the two that cannot be altered. The probable list is male sex, homocysteine and C reactive protein."],
  ["Abnormal lipids and cigarette smoking",
   "Both are major risk factors. The probable ones are male sex, homocysteine and high sensitivity C reactive protein."]],
 "c": 0, "cite": D + ", Slide 10"},

{"topic": "Homocysteine", "io": IO_MOLEC, "slot": "mechanism",
 "q": "What is homocysteine?",
 "opts": [
  ["An intermediary amino acid formed converting methionine to cysteine",
   "Correct. It is a normal metabolic intermediate rather than a foreign substance, which is why the harm relates to how much of it accumulates."],
  ["A lipoprotein that transports cholesterol to the vessel wall",
   "It is an amino acid rather than a lipoprotein, formed as methionine is converted to cysteine."],
  ["An inflammatory cytokine released by foam cells",
   "It is a metabolic intermediate rather than a cytokine: an amino acid on the path from methionine to cysteine."],
  ["A clotting factor activated by endothelial injury",
   "It is prothrombotic in its properties but it is an amino acid, not a clotting factor."]],
 "c": 0, "cite": D + ", Slide 11"},

{"topic": "Homocysteine", "io": IO_MOLEC, "slot": "mechanism",
 "q": "What properties make homocysteine harmful to vessels?",
 "opts": [
  ["It is atherogenic and prothrombotic",
   "Correct. Two harms at once: it damages the wall and it promotes clot on that damaged wall, which is the same one-two that drives coronary events generally."],
  ["It is atherogenic but protects against thrombosis",
   "It promotes thrombosis rather than protecting against it; its properties are described as both atherogenic and prothrombotic."],
  ["It raises low density lipoprotein production in the liver",
   "Its described properties are direct vascular injury and thrombosis rather than an effect on lipoprotein production."],
  ["It inhibits smooth muscle proliferation",
   "Smooth muscle hypertrophy is among the injuries it causes, so it does not inhibit that process."]],
 "c": 0, "cite": D + ", Slide 11"},

{"topic": "Homocysteine", "io": IO_MOLEC, "slot": "mechanism",
 "q": "Which vascular injuries are described with homocysteine?",
 "opts": [
  ["Intimal thickening",
   "Correct. The injuries run through every layer of the wall and then onto its surface, ending in a platelet-rich occlusive thrombus. Elastic lamina disruption, smooth muscle hypertrophy and platelet accumulation."],
  ["Calcification of the media with preserved intima",
   "Calcification of that pattern is not among the described injuries."],
  ["Fatty infiltration of the adventitia",
   "The described injuries involve the intima, elastic lamina and smooth muscle rather than the adventitia."],
  ["Aneurysmal dilation of the vessel",
   "Dilation is not among the described injuries, which are intimal thickening, elastic lamina disruption, smooth muscle hypertrophy and platelet accumulation."]],
 "c": 0, "cite": D + ", Slide 11"},

{"topic": "Lipoproteins", "io": IO_LIPO, "slot": "mechanism",
 "q": "Which lipoprotein carries the highest risk, and why?",
 "opts": [
  ["Low density lipoprotein, because it is high in cholesterol",
   "Correct. The composition is what determines the risk, which is why the lipoproteins are not interchangeable even though all of them carry lipid."],
  ["High density lipoprotein, because it is high in cholesterol",
   "High density lipoprotein decreases risk; it carries cholesterol back to the liver."],
  ["Very low density lipoprotein, because it is high in cholesterol",
   "Very low density lipoprotein increases risk, but it is high in triglycerides rather than cholesterol."],
  ["All lipoproteins carry equal risk",
   "They differ by composition, and their effect on risk differs with it."]],
 "c": 0, "cite": D + ", Slide 12"},

{"topic": "Lipoproteins", "io": IO_LIPO, "slot": "mechanism",
 "q": "How does high density lipoprotein reduce risk?",
 "opts": [
  ["It transports cholesterol back to the liver, clearing plaque away",
   "Correct. It works in the opposite direction to the others, which is why more of it is protective rather than merely neutral."],
  ["It prevents low density lipoprotein from being produced",
   "It clears cholesterol rather than blocking production of another lipoprotein."],
  ["It binds triglycerides in the circulation and inactivates them",
   "Triglyceride carriage belongs to very low density lipoprotein, and this is not the described protective mechanism."],
  ["It stabilizes the fibrous cap of existing plaques",
   "Cap stabilization comes from collagen and fibrin over time rather than from high density lipoprotein."]],
 "c": 0, "cite": D + ", Slide 12"},

{"topic": "Lipoproteins", "io": IO_LIPO, "slot": "mechanism",
 "q": "What distinguishes very low density lipoprotein from low density lipoprotein?",
 "opts": [
  ["It is high in triglycerides rather than cholesterol",
   "Correct. Both raise risk, so the distinction to hold is what each is carrying rather than which direction it pushes risk. Increases risk."],
  ["It is high in cholesterol and decreases risk",
   "It is high in triglycerides, and it increases rather than decreases risk."],
  ["It carries cholesterol back to the liver",
   "That is the role of high density lipoprotein, and it is why high density lipoprotein lowers rather than raises risk."],
  ["It is not associated with atherosclerotic risk",
   "It is described as increasing risk, through the triglycerides it carries rather than through cholesterol."]],
 "c": 0, "cite": D + ", Slide 12"},

{"topic": "Familial hypercholesterolemia", "io": IO_MOLEC, "slot": "mechanism",
 "q": "What is the molecular defect in familial hypercholesterolemia?",
 "opts": [
  ["A defective low density lipoprotein receptor on liver cells",
   "Correct. The liver cannot take cholesterol out of the circulation, so the problem is one of removal rather than of overproduction or of diet."],
  ["Absence of high density lipoprotein in the circulation",
   "The defect is in the hepatic receptor for low density lipoprotein rather than an absence of high density lipoprotein."],
  ["Failure of the gut to absorb dietary cholesterol",
   "The defect concerns hepatic removal from the bloodstream, not absorption."],
  ["Excessive conversion of methionine to homocysteine",
   "That relates to homocysteine metabolism, a separate mechanism."]],
 "c": 0, "cite": D + ", Slide 13"},

{"topic": "Familial hypercholesterolemia", "io": IO_MOLEC, "slot": "classification",
 "q": "How is familial hypercholesterolemia characterized among the genetic hyperlipidemias?",
 "opts": [
  ["It is the most common form",
   "Correct, which matters because a defect in a single receptor accounts for more inherited hyperlipidemia than any other mechanism."],
  ["It is the rarest form",
   "It is described as the most common form of genetic hyperlipidemia."],
  ["It is acquired rather than genetic",
   "It is genetic, and it is described among the genetic hyperlipidemias."],
  ["It affects triglyceride handling rather than cholesterol",
   "The defect concerns removal of cholesterol from the bloodstream."]],
 "c": 0, "cite": D + ", Slide 13"},

{"topic": "Plaque formation", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "What initiates atherosclerotic plaque formation?",
 "opts": [
  ["Injury to the endothelial cells of the vessel",
   "Correct. Everything that follows -- permeability, leukocytes, oxidized lipid, foam cells -- is downstream of that first injury."],
  ["Deposition of calcium on the intimal surface",
   "Calcification is a feature of established disease rather than the initiating event."],
  ["Rupture of the vasa vasorum within the arterial wall",
   "Hemorrhage from those capillaries contributes to plaque rupture later, not to initiation."],
  ["Platelet aggregation on an intact endothelium",
   "Platelet aggregation follows exposure of subendothelial proteins, which requires the endothelium to be damaged first."]],
 "c": 0, "cite": D + ", Slide 14"},

{"topic": "Plaque formation", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "Which are given as causes of the initiating endothelial injury?",
 "opts": [
  ["Wall stress, toxins, inflammation, hyperlipidemia",
   "Correct. Mechanical, chemical, inflammatory and metabolic insults all converge on the same first step, which is why so many different risk factors end in the same lesion."],
  ["Valvular calcification and rheumatic scarring",
   "These damage valves rather than injuring coronary endothelium."],
  ["Viral infection of the myocardium",
   "That relates to myocarditis rather than to endothelial injury."],
  ["Pericardial inflammation",
   "Pericardial disease does not injure coronary endothelium in the way described."]],
 "c": 0, "cite": D + ", Slide 14"},

{"topic": "Plaque formation", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "What happens once the injured endothelium becomes more permeable?",
 "opts": [
  ["Leukocytes are recruited and low density lipoprotein leaks through to be oxidized",
   "Correct. The lipid has to get into the wall before it can do harm, and the increased permeability is what lets it."],
  ["Calcium is deposited directly into the media",
   "Calcification is not the step that follows increased permeability."],
  ["Smooth muscle cells migrate out of the vessel wall",
   "Smooth muscle proliferates within the wall rather than migrating out of it."],
  ["The vessel dilates to preserve flow",
   "Dilation is not the described response to endothelial injury here."]],
 "c": 0, "cite": D + ", Slide 14"},

{"topic": "Plaque formation", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "Why is oxidation of the trapped lipid important?",
 "opts": [
  ["Oxidized lipids damage both the vessel wall and smooth muscle cells",
   "Correct. Lipid in the wall is not inert: oxidizing it is what turns a deposit into an actively injurious lesion."],
  ["Oxidation allows the lipid to be cleared back into the circulation",
   "Oxidation makes the lipid damaging rather than removable: oxidized lipid injures both the wall and the smooth muscle cells."],
  ["Oxidation converts the lipid into high density lipoprotein",
   "Oxidized lipid is not converted into a protective lipoprotein."],
  ["Oxidation prevents macrophages from engulfing the lipid",
   "Macrophages continue to engulf lipid, which is how foam cells form."]],
 "c": 0, "cite": D + ", Slide 14"},

{"topic": "Foam cells", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "What is a foam cell?",
 "opts": [
  ["A lipid-filled macrophage",
   "Correct. Naming it for its appearance hides what it is: a macrophage that has taken up so much lipid it has changed character, and now drives the lesion forward."],
  ["A smooth muscle cell that has become calcified",
   "Foam cells are macrophages laden with lipid rather than calcified smooth muscle."],
  ["A platelet aggregate within the plaque core",
   "Platelet aggregation is a separate step and does not form foam cells."],
  ["An endothelial cell that has detached from the wall",
   "Foam cells derive from macrophages that have taken up so much oxidized lipid they change character."]],
 "c": 0, "cite": D + ", Slide 15"},

{"topic": "Foam cells", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "What do the macrophages within a plaque release, and with what effect?",
 "opts": [
  ["Inflammatory mediators and growth factor",
   "Correct. This is the step that makes the lesion self-sustaining: the cells that arrived to deal with the lipid recruit more cells and more wall growth. Attracting more leukocytes and stimulating smooth muscle proliferation."],
  ["Collagen and fibrin, which stabilize the plaque",
   "Collagen and fibrin form the stabilizing cap later, and are not what the macrophages release here."],
  ["Enzymes that clear the lipid core entirely",
   "The lipid accumulates rather than being cleared; the macrophages release inflammatory mediators and growth factor instead."],
  ["Vasodilators that increase flow through the vessel",
   "Vasodilation is not the described consequence. The mediators recruit more leukocytes and stimulate smooth muscle proliferation."]],
 "c": 0, "cite": D + ", Slide 15"},

{"topic": "Lipid core", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "What is the significance of a large lipid core within a plaque?",
 "opts": [
  ["Plaques with large lipid cores are fragile and rupture",
   "Correct. Size and stability run in opposite directions, which is why the dangerous plaque is not necessarily the one narrowing the lumen most."],
  ["A large core makes the plaque more stable",
   "The opposite is described: a large lipid core makes the plaque fragile and liable to rupture."],
  ["A large core prevents platelet aggregation",
   "Rupture of such a plaque exposes subendothelial proteins and initiates platelet aggregation."],
  ["A large core indicates the plaque has been cleared",
   "The core is accumulated lipid and debris rather than evidence of clearance."]],
 "c": 0, "cite": D + ", Slide 15"},

{"topic": "Plaque rupture", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "What follows exposure of subendothelial proteins when a plaque ruptures?",
 "opts": [
  ["Platelet aggregation and thrombus formation",
   "Correct, and the thrombus can then be incorporated into the plaque, so a rupture that does not occlude the vessel still leaves it larger."],
  ["Immediate healing with collagen deposition",
   "Collagen and fibrin form a cap over time, but the immediate consequence of exposure is platelet aggregation."],
  ["Vasodilation of the affected segment",
   "Vasodilation is not the described consequence. Exposed subendothelial proteins initiate platelet aggregation and thrombus."],
  ["Clearance of the lipid core by macrophages",
   "The core is not cleared at rupture; exposure of subendothelial proteins triggers platelet aggregation instead."]],
 "c": 0, "cite": D + ", Slide 15"},

{"topic": "Plaque stability", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "What makes a plaque more stable over time?",
 "opts": [
  ["Collagen and fibrin forming a cap",
   "Correct. Stability is acquired rather than original, and the same process that stabilizes the plaque does nothing about the lumen it is narrowing."],
  ["Enlargement of the lipid core",
   "A larger lipid core makes the plaque more fragile, not more stable."],
  ["Continued recruitment of macrophages",
   "More macrophages sustain the inflammatory process rather than stabilizing the plaque."],
  ["Hemorrhage from the capillaries within the wall",
   "That raises pressure within the plaque and contributes to disruption."]],
 "c": 0, "cite": D + ", Slide 16"},

{"topic": "Plaque stability", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "At what degree of occlusion is blood flow described as compromised?",
 "opts": [
  ["Seventy-five percent",
   "Correct. It takes a great deal of narrowing before flow suffers, which is why plaques grow silently for years."],
  ["Twenty-five percent",
   "Flow is not described as compromised at this degree of narrowing."],
  ["Fifty percent",
   "Fifty percent is the figure given for hemodynamic effect in valvular stenosis, not for coronary occlusion."],
  ["Ninety-five percent",
   "Flow is described as compromised well before this, at about seventy-five percent occlusion."]],
 "c": 0, "cite": D + ", Slide 16"},

{"topic": "Plaque rupture", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "What determines the risk that a plaque will rupture?",
 "opts": [
  ["Its composition",
   "Correct. Two factors, one internal and one external, which is why an identical plaque may be stable in one vessel and not in another. The mechanical stresses acting on it."],
  ["Its age alone",
   "Age is not given as the determinant; composition and mechanical stress are."],
  ["The degree of luminal narrowing alone",
   "Severe stenosis is one of the vulnerability features, but composition and stress are what determine rupture risk."],
  ["The lipoprotein that delivered the lipid",
   "Which lipoprotein delivered the lipid is not described as determining rupture."]],
 "c": 0, "cite": D + ", Slide 26"},

{"topic": "Plaque rupture", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "How is a vulnerable plaque described?",
 "opts": [
  ["A large necrotic core covered by a thin fibrous cap",
   "Correct. Both halves matter: a lot of material behind very little holding it in."],
  ["A small core covered by a thick fibrous cap",
   "That describes a stable plaque rather than a vulnerable one."],
  ["A heavily calcified plaque with no lipid",
   "Calcification without a lipid core is not the described vulnerable lesion."],
  ["A plaque entirely composed of thrombus",
   "Thrombus may be incorporated into a plaque, but the vulnerable plaque is defined by its core and cap."]],
 "c": 0, "cite": D + ", Slide 26"},

{"topic": "Plaque rupture", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "How does a severe stenosis itself contribute to plaque disruption?",
 "opts": [
  ["Blood flowing at high velocity through it exerts shear forces on the plaque",
   "Correct. The narrowing accelerates the blood, and the accelerated blood works on the narrowing -- the lesion generates the force that breaks it."],
  ["It reduces flow so much that the plaque becomes ischemic",
   "Plaque ischemia is not the described mechanism of disruption."],
  ["It causes the vessel to dilate proximally",
   "Proximal dilation is not described as contributing to disruption."],
  ["It prevents collateral circulation from forming",
   "Collateral circulation develops in response to slowly progressive disease and is not the disruption mechanism."]],
 "c": 0, "cite": D + ", Slide 27"},

{"topic": "Plaque hemorrhage", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "How do the capillaries within the atherosclerotic arterial wall contribute to disruption?",
 "opts": [
  ["Their thin walls bleed",
   "Correct. The plaque can be disrupted from the inside as well as from the lumen, which is a route easy to overlook. Depositing blood products and raising pressure within the plaque."],
  ["They deliver macrophages that dissolve the fibrous cap",
   "Bleeding and pressure build-up is the described mechanism rather than cap dissolution."],
  ["They drain lipid out of the core, collapsing the plaque",
   "The described consequence is deposition and pressure rather than drainage."],
  ["They constrict, producing local ischemia within the wall",
   "Constriction of these capillaries is not the described mechanism."]],
 "c": 0, "cite": D + ", Slide 28"},

{"topic": "Plaque rupture", "io": IO_PLAQUE, "slot": "mechanism",
 "q": "What are the consequences of plaque rupture?",
 "opts": [
  ["Thrombosis, and emboli carried downstream to block smaller vessels",
   "Correct. The damage need not be where the plaque is: material travels, which is why a proximal lesion can infarct distal muscle."],
  ["Immediate dilation of the affected artery",
   "Dilation is not a consequence of rupture. Thrombosis follows, with emboli carried downstream to smaller vessels."],
  ["Resolution of the plaque with restored flow",
   "Rupture worsens the lesion rather than resolving it, producing thrombosis and downstream embolism."],
  ["Calcification of the ruptured surface with no further event",
   "Thrombosis and downstream embolism are the described consequences, and those emboli can block smaller vessels."]],
 "c": 0, "cite": D + ", Slide 29"},
]
