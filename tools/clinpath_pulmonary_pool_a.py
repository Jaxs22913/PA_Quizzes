# -*- coding: utf-8 -*-
"""Clinical Pathophysiology I, Lecture 9 -- Pulmonary Pathophysiology, part A (slides 3-44).

Anatomy and function, acute respiratory failure, pulmonary hypertension and the
capillary fluid pressures, pulmonary malignancies, the obstructive overview and
asthma. Part B carries bronchitis through pneumonia.

SOURCE. No deck was posted for this lecture (Dr. Matthew Ward, 2026-10-20). Jaxon
rebuilt this year's deck from the lecture video: "9. Pulmonary Pathophysiology -
Ward 2026 (rebuilt from recording).pptx", 109 slides = last year's deck with Ward's
title, the 7 slides he added (44, 51, 59, 64, 82, 98, 103) and 2 slides he did not
show removed. Slide numbers below are that rebuilt deck's. Every fact is on a
VISIBLE slide (text or picture, each picture viewed); minutes on screen weight the
split (clinpath_pulmonary_partition.py); the transcript only stars the guide.

THE SEVEN ADDED SLIDES are interpretation-flavored (what a test result or a symptom
pattern means). Questions from them stay on MECHANISM -- what a finding means --
never on what to do about it.

MECHANISM ONLY, per [[clin_path_exam_spec]]. KEYS ARE WRITTEN SHORT ON PURPOSE.
Each distractor carries its misconception as a third option element (WRITER.md
rule 5); numeric and ordered option sets are authored ascending (rule 8).
"""

D = "9. Pulmonary Pathophysiology - Ward 2026 (rebuilt from recording).pptx"

IO_A = "Review the anatomy of the pulmonary system"
IO_B = "Review the functions of the pulmonary system"
IO_C = "Describe the molecular mechanisms of pulmonary pathologies"
_D = ("Compare and contrast the etiologies and pathophysiological processes of different "
      "pulmonary diseases, including: ")
IO_ARF = _D + "Acute respiratory failure"
IO_PH = _D + "Pulmonary hypertension"
IO_MAL = _D + "Pulmonary malignancies"
IO_OBS = _D + "Obstructive pulmonary diseases"
IO_RES = _D + "Restrictive pulmonary diseases"
IO_AST = _D + "Asthma"
IO_EDE = _D + "Pulmonary edema"
IO_PE = _D + "Pulmonary embolism"
IO_COR = _D + "Cor pulmonale"

CD = "competing diagnosis"
WS = "wrong stage or severity"
RF = "ruled out by a stated finding"
CM = "confused mechanism or drug class"
AF = "adjacent fact"
RV = "reversed direction or value"
LB = "common lay belief"


def c(*n):
    return D + ", Slide %d" % n[0] if len(n) == 1 else \
        D + ", Slides " + ", ".join(str(x) for x in n)


def Q(topic, io, slot, q, opts, cite, **kw):
    d = {"topic": topic, "io": io, "slot": slot, "q": q, "opts": opts, "c": kw.pop("key", 0), "cite": cite}
    d.update(kw)
    return d


ANA = "Anatomy and function"
ARF = "Acute respiratory failure"
PHT = "Pulmonary hypertension"
FLU = "Capillary fluid pressures"
MAL = "Pulmonary malignancies"
OBS = "Obstructive diseases overview"
AST = "Asthma"

QUESTIONS = [

# ---------------------------------------------------------------- anatomy (slides 3-5)
Q(ANA, IO_A, "anatomy",
  "Which alveolar cell secretes surfactant?",
  [["Type II pneumocyte",
    "Correct. The type II pneumocyte is the surfactant-secreting cell of the alveolar wall; type I pneumocytes form most of the thin alveolar epithelium."],
   ["Type I pneumocyte",
    "Type I pneumocytes make up the thin alveolar epithelium across which gases diffuse; surfactant comes from type II cells.", AF],
   ["Alveolar macrophage",
    "The macrophage sits in the alveolus as a defender; surfactant is secreted by the type II pneumocyte.", AF],
   ["Capillary endothelial cell",
    "The pulmonary capillary endothelium forms the blood side of the respiratory membrane, not the surfactant source.", AF]],
  c(4), core=True),

Q(ANA, IO_A, "anatomy",
  "Across how many thin layers of the respiratory membrane do oxygen and carbon dioxide diffuse?",
  [["Two",
    "Too few. The respiratory membrane has six thin layers, from the alveolar fluid with surfactant to the capillary endothelium.", RV],
   ["Four",
    "Too few. Oxygen and carbon dioxide cross six thin layers, including two basement membranes and the interstitial space.", RV],
   ["Six",
    "Correct. Oxygen and carbon dioxide diffuse across six thin layers: alveolar fluid with surfactant, alveolar epithelium, its basement membrane, the interstitial space, the capillary basement membrane and the capillary endothelium."],
   ["Eight",
    "Too many. The respiratory membrane is six thin layers between alveolar air and the red blood cell.", RV]],
  c(4), key=2, ordered=True),

Q(ANA, IO_A, "anatomy",
  "Which layer of the respiratory membrane lies between the two basement membranes?",
  [["The interstitial space",
    "Correct. From the air side the layers run: alveolar fluid with surfactant, alveolar epithelium, its basement membrane, the interstitial space, the capillary basement membrane, then the capillary endothelium."],
   ["The alveolar epithelium",
    "The alveolar epithelium sits on the air side of the alveolar basement membrane, not between the two membranes.", AF],
   ["The capillary endothelium",
    "The capillary endothelium lies on the blood side of the capillary basement membrane, the innermost layer.", AF],
   ["The alveolar fluid layer",
    "Alveolar fluid with surfactant is the outermost layer, facing the air space.", AF]],
  c(4)),

Q(ANA, IO_B, "function",
  "Which description fits the normal pulmonary circulation?",
  [["High flow, low pressure",
    "Correct. The pulmonary circulation is normally a high-flow, low-pressure system: about 22/8 to 25/8 mmHg, mean 15 mmHg."],
   ["Low flow, high pressure",
    "That reverses both: the lungs take high flow at low pressure.", RV],
   ["High flow, high pressure",
    "Flow is high but pressure stays low: the normal mean pulmonary arterial pressure is only about 15 mmHg.", WS],
   ["Low flow, low pressure",
    "Pressure is low, but flow is high: the lungs receive high flow at low pressure.", RV]],
  c(20), core=True),

# ---------------------------------------------------------------- acute respiratory failure (6-14)
Q(ARF, IO_ARF, "definition",
  "What distinguishes hypoxia from hypoxemia?",
  [["Hypoxia is low tissue oxygenation",
    "Correct. Hypoxia is decreased tissue oxygenation; hypoxemia is decreased blood oxygen, seen as a low arterial oxygen and low hemoglobin saturation."],
   ["Hypoxia is low arterial oxygen",
    "Low arterial oxygen in the blood is hypoxemia; hypoxia refers to the tissues.", RV],
   ["Hypoxia is high arterial carbon dioxide",
    "Raised arterial carbon dioxide is hypercapnia, the mark of ventilatory failure.", CM],
   ["Hypoxia is low hemoglobin saturation",
    "Low hemoglobin saturation is one measure of hypoxemia, the blood-level problem; hypoxia is tissue oxygenation.", AF]],
  c(7), core=True),

Q(ARF, IO_ARF, "threshold",
  "On room air, which arterial oxygen tension (PaO2) defines the hypoxemia of acute respiratory failure?",
  [["Below 40 mmHg",
    "Lower than the defining value; acute respiratory failure is set at an arterial oxygen below 60 mmHg on room air.", RV],
   ["Below 50 mmHg",
    "Fifty mmHg is the carbon dioxide threshold (above 50); the oxygen threshold is below 60 mmHg.", AF],
   ["Below 60 mmHg",
    "Correct. Acute respiratory failure is disturbed gas exchange with arterial oxygen below 60 mmHg, carbon dioxide above 50 mmHg or pH below 7.30, breathing room air (21% oxygen)."],
   ["Below 70 mmHg",
    "Higher than the defining value; the threshold is an arterial oxygen below 60 mmHg.", RV]],
  c(7), key=2, ordered=True),

Q(ARF, IO_ARF, "threshold",
  "Which arterial carbon dioxide tension (PaCO2) marks acute respiratory failure?",
  [["Above 35 mmHg",
    "Too low a cut-off; acute respiratory failure is marked by arterial carbon dioxide above 50 mmHg.", RV],
   ["Above 40 mmHg",
    "Too low a cut-off; the defining value is arterial carbon dioxide above 50 mmHg.", RV],
   ["Above 50 mmHg",
    "Correct. The blood gas values of acute respiratory failure are arterial oxygen below 60 mmHg, carbon dioxide above 50 mmHg and pH below 7.30 on room air."],
   ["Above 60 mmHg",
    "Sixty mmHg is the OXYGEN threshold (below 60); carbon dioxide is set above 50 mmHg.", AF]],
  c(7), key=2, ordered=True),

Q(ARF, IO_ARF, "classification",
  "Which category of acute respiratory failure shows hypoxemia with a normal or low carbon dioxide?",
  [["Hypoxic respiratory failure",
    "Correct. Failure of respiration or oxygenation gives hypoxemia with normal or lower carbon dioxide: hypoxic respiratory failure."],
   ["Hypercarbic ventilatory failure",
    "Ventilatory failure is insufficient removal of carbon dioxide, so carbon dioxide rises (hypercapnia).", RV],
   ["Combined respiratory and ventilatory failure",
    "The combined category has both problems, so carbon dioxide would not stay normal or low.", WS],
   ["Acute respiratory distress syndrome",
    "Acute respiratory distress syndrome is one parenchymal CAUSE of failure, not one of the three categories.", AF]],
  c(8), core=True),

Q(ARF, IO_ARF, "mechanism",
  "Which is a mechanism of HYPOXIC respiratory failure?",
  [["Shunt",
    "Correct. Hypoxic respiratory failure arises from ventilation/perfusion mismatch, shunt, decreased diffusion, alveolar hypoventilation and high altitude."],
   ["Increased carbon dioxide production",
    "Fever, infection and burns raise carbon dioxide production, a cause of hypercapnic ventilatory failure.", CD],
   ["Inability to sense raised carbon dioxide",
    "Failure to sense raised carbon dioxide, from drugs or alkalosis, causes hypercapnic ventilatory failure.", CD],
   ["Failure to signal effector muscles",
    "Failed signaling to the effectors (Guillain-Barré syndrome, spinal cord injury) causes hypercapnic ventilatory failure.", CD]],
  c(9, 10), core=True),

Q(ARF, IO_PE, "mechanism",
  "How does pulmonary embolism push toward hypercapnic ventilatory failure?",
  [["It increases dead space",
    "Correct. Increased dead space (wasted ventilation), from hypovolemia, low cardiac output or pulmonary embolism, leaves ventilation inadequate for the carbon dioxide produced."],
   ["It increases carbon dioxide production",
    "Raised carbon dioxide production comes from fever, infection, trauma or burns, not from embolism.", CM],
   ["It blunts sensing of carbon dioxide",
    "Blunted sensing of raised carbon dioxide comes from drugs or alkalosis.", CM],
   ["It blocks nerve signals to the muscles",
    "Failure to signal the effectors is the Guillain-Barré syndrome and spinal cord injury route.", CM]],
  c(10, 14), core=True),

Q(ARF, IO_ARF, "mechanism",
  "How do fever, infection and burns contribute to hypercapnic ventilatory failure?",
  [["They raise carbon dioxide production",
    "Correct. Hypercapnic failure is alveolar ventilation inadequate for the carbon dioxide produced, and fever, infection and trauma or burns increase that production."],
   ["They increase dead space",
    "Increased dead space comes from hypovolemia, low cardiac output or pulmonary embolism.", AF],
   ["They block sensing of carbon dioxide",
    "Blocked sensing of raised carbon dioxide is caused by drugs or alkalosis.", AF],
   ["They cut the respiratory rate",
    "A decreased respiratory rate reduces ventilation; fever, infection and burns act by raising carbon dioxide production.", AF]],
  c(10)),

Q(ARF, IO_ARF, "classification",
  "Myasthenia gravis causes acute respiratory failure through which category of cause?",
  [["Neuromuscular disease",
    "Correct. Neuromuscular causes are multiple sclerosis, myasthenia gravis, polio, Guillain-Barré syndrome and quadriplegia."],
   ["Central nervous system",
    "Central nervous system causes are sedatives, stroke and brain trauma or tumor.", AF],
   ["Chest skeletal system",
    "Chest skeletal causes are kyphoscoliosis, chest trauma, pleural effusion and massive ascites.", AF],
   ["Pulmonary parenchyma",
    "Parenchymal causes are shock, pulmonary embolism, pulmonary edema, advanced emphysema, pneumonia and acute respiratory distress syndrome.", AF]],
  c(14)),

Q(ARF, IO_EDE, "mechanism",
  "In acute lung injury, why does less oxygen reach the blood?",
  [["Leaked fluid collapses large areas of alveoli",
    "Correct. Water, cells and protein leak into the tissue around the alveoli and cause large areas of alveoli to collapse, reducing the oxygen that reaches the blood vessels."],
   ["Alveolar walls are destroyed without fibrosis",
    "Destruction of alveolar walls without fibrosis defines emphysema, an obstructive disease.", CD],
   ["Airway smooth muscle constricts reversibly",
    "Reversible constriction with airway inflammation is asthma, not the collapse of acute lung injury.", CD],
   ["Air is trapped in distended air sacs",
    "Trapped air in distended sacs forming bullae is emphysema; acute lung injury collapses alveoli instead.", CD]],
  c(11, 12)),

# ---------------------------------------------------------------- pulmonary hypertension (15-23)
Q(PHT, IO_PH, "threshold",
  "Approximately what is the normal mean pulmonary arterial pressure in a healthy adult?",
  [["8 mmHg",
    "Eight mmHg is the normal pulmonary DIASTOLIC value (22/8 to 25/8 mmHg); the mean is about 15 mmHg.", AF],
   ["15 mmHg",
    "Correct. Normal pulmonary arterial pressure is about 22/8 to 25/8 mmHg, with a mean of 15 mmHg."],
   ["30 mmHg",
    "Thirty mmHg is twice the normal mean and above the 20 mmHg resting mean that defines pulmonary hypertension.", WS],
   ["45 mmHg",
    "Far above normal; the healthy mean is about 15 mmHg in this low-pressure system.", RV]],
  c(20), key=1, ordered=True, core=True),

# Slide 20 as shown in the 2026 video (Ward edited it): "Mean pulmonary arterial pressure at rest
# > 20mmHg", which matches what he says in the recording. The options are slide 20's own numbers.
Q(PHT, IO_PH, "threshold",
  "Pulmonary hypertension is a mean pulmonary arterial pressure at rest above which value?",
  [["8 mmHg",
    "Eight mmHg is the normal pulmonary diastolic pressure (22/8 to 25/8 mmHg), far below the threshold.", AF],
   ["15 mmHg",
    "Fifteen mmHg is the NORMAL mean pulmonary arterial pressure; pulmonary hypertension starts above 20 mmHg.", AF],
   ["20 mmHg",
    "Correct. Pulmonary hypertension is a mean pulmonary arterial pressure at rest above 20 mmHg; the normal mean is about 15 mmHg."],
   ["25 mmHg",
    "Twenty-five mmHg is the upper normal SYSTOLIC pulmonary pressure (25/8 mmHg), not the mean threshold.", WS]],
  c(20), key=2, ordered=True),

Q(PHT, IO_PH, "classification",
  "Which features describe idiopathic pulmonary hypertension?",
  [["Rapidly progressive, commoner in women",
    "Correct. Idiopathic pulmonary hypertension is rapidly progressive, more common in women than men, of unknown cause, and appears in the third to fourth decade."],
   ["Slowly progressive, commoner in men",
    "Both are reversed: it is rapidly progressive and more common in women.", RV],
   ["Results from a known disease process",
    "A known disease process defines SECONDARY pulmonary hypertension; the idiopathic form's cause is unknown.", CD],
   ["Usually begins after the seventh decade",
    "The typical age of idiopathic pulmonary hypertension is the third to fourth decade of life.", RV]],
  c(21), core=True),

Q(PHT, IO_PH, "mechanism",
  "How does mitral stenosis lead to pulmonary hypertension?",
  [["It raises left atrial pressure",
    "Correct. Mitral stenosis, mitral regurgitation and left ventricular failure cause pulmonary hypertension by increasing left atrial pressure."],
   ["It increases pulmonary blood flow",
    "Increased pulmonary blood flow comes from left-to-right shunts such as atrial septal defect and patent ductus arteriosus.", AF],
   ["It causes hypoxic vasoconstriction",
    "Hypoxic vasoconstriction is the route in chronic bronchitis and advanced emphysema.", AF],
   ["It raises blood viscosity",
    "Raised viscosity is the polycythemia route; mitral stenosis raises left atrial pressure.", AF]],
  c(22), core=True),

Q(PHT, IO_PH, "mechanism",
  "How do chronic bronchitis and advanced emphysema raise pulmonary vascular resistance?",
  [["Hypoxic vasoconstriction",
    "Correct. Increased resistance to blood flow in pulmonary hypertension comes from hypoxic vasoconstriction (chronic bronchitis, advanced emphysema), embolic obstruction and pulmonary fibrosis."],
   ["A left-to-right shunt",
    "A left-to-right shunt raises pulmonary blood FLOW rather than resistance.", AF],
   ["Raised left atrial pressure",
    "Raised left atrial pressure is the mitral valve and left ventricular failure route.", AF],
   ["Increased blood viscosity",
    "Viscosity rises with polycythemia; obstructive lung disease acts through hypoxic vasoconstriction.", AF]],
  c(22, 50)),

Q(PHT, IO_PE, "mechanism",
  "Through which route does embolism produce pulmonary hypertension?",
  [["Increased resistance to blood flow",
    "Correct. Obstruction from embolism sits with hypoxic vasoconstriction and pulmonary fibrosis under increased resistance to blood flow."],
   ["Increased pulmonary blood flow",
    "Increased flow comes from left-to-right shunts (atrial septal defect, patent ductus arteriosus) or polycythemia's viscosity.", AF],
   ["Increased left atrial pressure",
    "Raised left atrial pressure comes from mitral stenosis, mitral regurgitation or left ventricular failure.", AF],
   ["Loss of elastic recoil",
    "Loss of elastic tissue narrows small bronchioles in emphysema; embolism obstructs vessels.", CM]],
  c(22)),

Q(PHT, IO_C, "mechanism",
  "What thickens the walls of small pulmonary vessels in pulmonary hypertension?",
  [["More muscle mass in the media",
    "Correct. Chronic exposure thickens the small pulmonary vessel walls through increased muscle mass of the media, driven by local tissue hypoxia and acidosis, and the intima becomes fibrotic."],
   ["Lipid plaques in the intima",
    "Lipid-rich plaque is atherosclerosis; here the intima becomes fibrotic and the media gains muscle.", CM],
   ["Thinning of the media",
    "The media thickens rather than thins, from increased muscle mass.", RV],
   ["Calcium in the adventitia",
    "No calcification is described; the change is medial muscle mass with intimal fibrosis.", CM]],
  c(23), core=True),

# Replaces the plexiform-lesion question (slide 23's plexiform line is gone from the 2026 deck);
# kept in the same pool position so the seeded split is unchanged.
Q(PHT, IO_PH, "mechanism",
  "Through which route does a left-to-right shunt raise pulmonary arterial pressure?",
  [["Increased pulmonary blood flow",
    "Correct. A left-to-right shunt, such as an atrial septal defect or patent ductus arteriosus, raises pulmonary blood flow, one of the routes to pulmonary hypertension."],
   ["Increased resistance to flow",
    "Raised resistance is the route of hypoxic vasoconstriction, embolism and fibrosis, not of a shunt.", CD],
   ["Increased left atrial pressure",
    "Raised left atrial pressure is the route of mitral stenosis, mitral regurgitation and left ventricular failure.", CD],
   ["Decreased blood viscosity",
    "The route is INCREASED flow or viscosity, as in polycythemia; a shunt adds flow rather than thinning the blood.", RV]],
  c(22)),

Q(PHT, IO_COR, "mechanism",
  "What happens to the heart as pulmonary hypertension narrows the pulmonary arteries?",
  [["The right ventricle enlarges",
    "Correct. Pulmonary hypertension narrows the pulmonary arteries and the right ventricle enlarges; when hypoxic lung disease drives it, this right ventricular dilation is cor pulmonale, leading to right-sided heart failure."],
   ["The left ventricle enlarges",
    "The left ventricle pumps into the systemic circulation; the chamber facing the narrowed pulmonary arteries is the right ventricle.", AF],
   ["The left atrium shrinks",
    "No left atrial change follows; it is the right ventricle that enlarges.", CM],
   ["The heart stays unchanged",
    "The heart does change: the right ventricle enlarges as pulmonary hypertension develops.", RV]],
  c(16, 50)),

# ---------------------------------------------------------------- capillary fluid pressures (17-19)
Q(FLU, IO_EDE, "mechanism",
  "Which change increases net fluid filtration out of a capillary?",
  [["A rise in capillary hydrostatic pressure",
    "Correct. Net filtration Jv = Kf[(Pc − Pif) − (πc − πif)]: raising capillary hydrostatic pressure (Pc) pushes more fluid out, as in the effusions of heart failure."],
   ["A rise in plasma colloid osmotic pressure",
    "Plasma colloid osmotic pressure pulls fluid INTO the capillary, so raising it reduces filtration.", RV],
   ["A rise in interstitial fluid pressure",
    "Interstitial fluid pressure opposes filtration; raising it pushes fluid back toward the capillary.", RV],
   ["A fall in interstitial colloid osmotic pressure",
    "Interstitial colloid osmotic pressure draws fluid outward; lowering it reduces filtration.", RV]],
  c(17, 93), core=True),

Q(FLU, IO_B, "mechanism",
  "Why does fluid leave the capillary at its arterial end but return at its venous end?",
  [["Hydrostatic pressure falls along it",
    "Correct. At the arterial end hydrostatic pressure (35 mm) exceeds osmotic pressure (25 mm) and fluid filters out; at the venous end hydrostatic pressure (15 mm) is below it and fluid returns."],
   ["Osmotic pressure falls along it",
    "Osmotic pressure stays about the same (25 mm) at both ends; it is hydrostatic pressure that falls.", RV],
   ["Lymphatics push fluid back in",
    "Lymphatics drain surplus interstitial fluid; the return at the venous end is driven by osmotic pressure exceeding hydrostatic pressure.", CM],
   ["The capillary wall thickens downstream",
    "Wall thickness does not change; the balance of hydrostatic and osmotic pressure reverses along the capillary.", CM]],
  c(18, 19)),

# ---------------------------------------------------------------- malignancies (24-28)
Q(MAL, IO_MAL, "comparison",
  "Which lung carcinoma grows fastest, doubling in about 33 days?",
  [["Small cell carcinoma",
    "Correct. Small cell (oat cell) carcinoma grows rapidly, doubling in about 33 days, with common widespread metastasis and paraneoplastic syndrome."],
   ["Adenocarcinoma",
    "Adenocarcinoma is slower, doubling its size in about 180 days.", RV],
   ["Squamous cell carcinoma",
    "Squamous cell carcinoma doubles its volume in about 100 days.", AF],
   ["Large cell carcinoma",
    "Large cell carcinoma doubles in size about every 100 days, three times slower than small cell.", AF]],
  c(25, 26, 27), core=True),

Q(MAL, IO_MAL, "mechanism",
  "Why is squamous cell carcinoma of the lung often detected earlier than other lung cancers?",
  [["Sputum cytology can show it",
    "Correct. Two-thirds arise in the central bronchi near the hilus as intraluminal growth, so sputum cytology shows the cancer and detection comes earlier."],
   ["It doubles in about 33 days",
    "Rapid doubling in about 33 days is small cell carcinoma, and speed does not make detection earlier.", AF],
   ["It arises in the lung periphery",
    "Peripheral growth is adenocarcinoma, which is NOT as amenable to early detection.", RV],
   ["Its large cells form visible nests",
    "Large cells in nests or clusters describe large cell carcinoma, which also develops peripherally.", AF]],
  c(25, 26, 27), core=True),

Q(MAL, IO_MAL, "comparison",
  "Which lung carcinoma accounts for the largest share of cases?",
  [["Adenocarcinoma",
    "Correct. Adenocarcinomas are 35–40% of cases, ahead of squamous cell (20–30%), small cell (15–20%) and large cell (5–10%)."],
   ["Squamous cell carcinoma",
    "Squamous cell carcinoma is 20–30% of cases, behind adenocarcinoma at 35–40%.", AF],
   ["Small cell carcinoma",
    "Small cell carcinoma is 15–20% of cases, fewer than adenocarcinoma at 35–40%.", AF],
   ["Large cell carcinoma",
    "Large cell carcinoma is the smallest group, 5–10% of cases; adenocarcinoma leads at 35–40%.", RV]],
  c(25, 26, 27)),

Q(MAL, IO_MAL, "mechanism",
  "Which lung carcinoma is associated with paraneoplastic syndrome?",
  [["Small cell carcinoma",
    "Correct. Small cell (oat cell) carcinoma arises in central bronchi, grows rapidly, metastasizes widely and is associated with paraneoplastic syndrome."],
   ["Squamous cell carcinoma",
    "Squamous cell carcinoma is central and spreads first to regional lymph nodes; paraneoplastic syndrome is listed for small cell carcinoma.", AF],
   ["Adenocarcinoma",
    "Adenocarcinoma is peripheral, doubles in about 180 days and metastasizes to distant organs.", AF],
   ["Large cell carcinoma",
    "Large cell carcinoma is peripheral, with large cells in nests or clusters.", AF]],
  c(27)),

# ---------------------------------------------------------------- obstructive overview (29-34)
Q(OBS, IO_OBS, "definition",
  "What feature defines the obstructive pulmonary diseases?",
  [["Increased airflow resistance",
    "Correct. Obstructive pulmonary diseases are manifested by increased airflow resistance, whether from the airway wall, loss of parenchyma or material in the lumen."],
   ["Decreased expansion of the lungs",
    "Decreased expansion defines the RESTRICTIVE lung diseases; obstruction raises airflow resistance.", CD],
   ["Thickening of the alveolar interstitium",
    "Interstitial thickening is diffuse interstitial lung disease, a restrictive disorder.", CD],
   ["Air in the pleural space",
    "Air in the pleural space is pneumothorax, a pleural space disorder classed with the restrictive diseases.", CD]],
  c(33), core=True),

Q(OBS, IO_OBS, "mechanism",
  "By which mechanism does emphysema obstruct airflow?",
  [["Loss of parenchyma around the airways",
    "Correct. Emphysema obstructs through loss of lung parenchyma, raising pressure around the outside of the airway lumen, as do lymphadenopathy and tumor."],
   ["Disease in the airway wall",
    "Conditions in the wall of the lumen are asthma and acute and chronic bronchitis.", AF],
   ["Material blocking the lumen",
    "Obstruction of the lumen itself is bronchiectasis, cystic fibrosis, croup or a foreign body.", AF],
   ["Fibrosis stiffening the alveoli",
    "Stiff fibrotic alveoli are restrictive disease; emphysema destroys alveolar walls WITHOUT fibrosis.", RV]],
  c(33, 53)),

Q(OBS, IO_OBS, "classification",
  "Which disorder is classified as obstruction of the airway lumen?",
  [["Cystic fibrosis",
    "Correct. The obstructive diseases are grouped by site; obstruction of the airway lumen lists bronchiectasis, bronchiolitis, cystic fibrosis, acute tracheobronchial obstruction, epiglottitis, croup and foreign body."],
   ["Emphysema",
    "Emphysema is classified under obstruction from loss of lung parenchyma; cystic fibrosis is listed under the airway lumen.", AF],
   ["Asthma",
    "Asthma is classified under obstruction from conditions in the airway wall; cystic fibrosis is listed under the airway lumen.", AF],
   ["Chronic bronchitis",
    "Chronic bronchitis is classified under conditions in the airway wall; cystic fibrosis is listed under the airway lumen.", AF]],
  c(33, 34)),

Q(OBS, IO_OBS, "mechanism",
  "Why do the lungs in chronic obstructive pulmonary disease fail to deflate normally?",
  [["Air is trapped in damaged air sacs",
    "Correct. The lungs do not deflate like normal lungs because air is trapped in damaged air sacs, while bronchioles narrow and block with mucus."],
   ["The pleural space fills with air",
    "Air in the pleural space is a pneumothorax, a separate disorder that collapses the lung.", CD],
   ["Surfactant production rises",
    "Surfactant comes from type II pneumocytes; its LOSS causes collapse in acute respiratory distress syndrome.", CM],
   ["The alveolar walls stiffen with fibrosis",
    "Fibrotic stiff alveoli belong to restrictive interstitial disease, not to air trapping.", CD]],
  c(30, 32, 55)),

# ---------------------------------------------------------------- asthma (35-44)
Q(AST, IO_AST, "definition",
  "Which feature separates asthma from the other obstructive airway diseases?",
  [["Its obstruction is reversible",
    "Correct. Asthma is an obstructive airway disease that is reversible, with airway inflammation and increased airway responsiveness to a variety of stimuli."],
   ["Its obstruction is persistent",
    "Persistent, irreversible obstruction describes chronic bronchitis.", RV],
   ["It destroys alveolar walls",
    "Alveolar wall destruction without fibrosis is emphysema, an irreversible loss of parenchyma.", CD],
   ["It dilates the bronchi for good",
    "Permanent bronchial dilation from wall destruction is bronchiectasis.", CD]],
  c(35, 48), core=True),

Q(AST, IO_AST, "comparison",
  "Which finding fits non-allergic (intrinsic) asthma?",
  [["Negative skin tests, normal serum IgE",
    "Correct. Intrinsic asthma has no identifiable specific allergen, negative skin tests to common inhalant allergens and normal serum IgE; it often develops in middle age."],
   ["An IgE-mediated immediate phase",
    "An IgE-mediated immediate phase defines allergic (extrinsic) asthma.", CD],
   ["A more favorable prognosis",
    "Intrinsic asthma has the LESS favorable prognosis and frequently develops in middle age.", RV],
   ["A specific allergen identified",
    "No specific allergen can be identified in intrinsic asthma; it is precipitated by exercise, stress and irritants.", RV]],
  c(37), core=True),

Q(AST, IO_AST, "mechanism",
  "What mediates the immediate phase of allergic (extrinsic) asthma?",
  [["IgE on mast cells",
    "Correct. The immediate phase is mediated by IgE to specific antigens; IgE binds mast cells, which release chemical mediators when the antigen arrives."],
   ["Sensitized T cells",
    "Sensitized T cells drive delayed (type IV) reactions, not the immediate phase.", CM],
   ["Complement membrane pores",
    "Complement pores lyse cells; the immediate asthmatic phase is mast-cell mediator release.", CM],
   ["Neutrophil proteases",
    "Proteolytic enzymes from neutrophils and macrophages destroy alveoli in emphysema.", CD]],
  c(39), core=True),

Q(AST, IO_C, "mechanism",
  "Which mast-cell mediator in allergic asthma is the slow-reacting substance of anaphylaxis?",
  [["Leukotrienes",
    "Correct. Mast cells release histamine, slow-reacting substances of anaphylaxis (leukotrienes), prostaglandins, bradykinins, eosinophilic chemotactic factor and serotonin."],
   ["Histamine",
    "Histamine is listed separately from the slow-reacting substances, which are the leukotrienes.", AF],
   ["Serotonin",
    "Serotonin is another listed mediator, not the slow-reacting substance of anaphylaxis.", AF],
   ["Bradykinin",
    "Bradykinins are listed separately; the slow-reacting substances are leukotrienes.", AF]],
  c(39)),

Q(AST, IO_AST, "mechanism",
  "What happens to the normal respiratory epithelium in asthma?",
  [["It is denuded and replaced by goblet cells",
    "Correct. Normal respiratory epithelium is denuded and replaced by goblet cells, with altered epithelial integrity and increased microvascular permeability."],
   ["It is replaced by squamous cells",
    "Replacement of ciliated columnar epithelium by squamous cells is described in chronic bronchitis and bronchiectasis.", AF],
   ["It thins to secrete surfactant",
    "Surfactant comes from type II pneumocytes in the alveoli, not from the airway epithelium.", CM],
   ["It stays intact under a mucus layer",
    "The epithelium is denuded, and more mediator release damages it further.", RV]],
  c(40, 43)),

Q(AST, IO_AST, "mechanism",
  "What does vagal nerve stimulation add to the airway changes of asthma?",
  [["Mucus hypersecretion and bronchoconstriction",
    "Correct. Vagal nerve stimulation leads to mucus hypersecretion and bronchoconstriction, on top of mucosal edema and inflammatory exudate from leaky microvessels."],
   ["Alveolar wall destruction",
    "Alveolar wall destruction is emphysema; vagal stimulation acts on the airways, not the alveoli.", CD],
   ["Dilation of the bronchi",
    "Bronchial dilation from destroyed walls is bronchiectasis; vagal stimulation constricts.", RV],
   ["Production of surfactant",
    "Surfactant is a type II pneumocyte product with no link to vagal stimulation.", CM]],
  c(40)),

Q(AST, IO_AST, "mechanism",
  "Which structural change lies beneath the basement membrane in asthma?",
  [["Collagen deposition",
    "Correct. Immunohistopathology shows denuded epithelium, collagen deposition beneath the basement membrane, edema, mast cell activation and infiltration by neutrophils, eosinophils and lymphocytes."],
   ["Noncaseating granulomas",
    "Noncaseating epithelioid granulomas are sarcoidosis, not a feature of the asthmatic airway wall.", CD],
   ["Hyaline membranes",
    "Hyaline membranes form in acute respiratory distress syndrome.", CD],
   ["Bullae from trapped air",
    "Bullae form when trapped air distends the air sacs in emphysema; they are not part of the asthmatic airway wall.", CD]],
  c(43)),

Q(AST, IO_AST, "interpretation",
  "Why can airflow testing be normal in a person with asthma?",
  [["Symptoms fluctuate between episodes",
    "Correct. Asthma symptoms fluctuate and testing may normalize between episodes, so the history is read alongside objective airflow measurements."],
   ["The obstruction is irreversible",
    "Irreversible obstruction would keep testing abnormal; asthmatic obstruction is reversible.", RV],
   ["The alveoli are destroyed",
    "Alveolar destruction is emphysema, which does not come and go.", CD],
   ["Airway inflammation is absent",
    "Inflammation is the basis of asthma and can continue even as symptoms improve.", RV]],
  c(35, 44), core=True),

Q(AST, IO_AST, "interpretation",
  "Why can airway inflammation continue after asthma symptoms improve?",
  [["Muscle and inflammation recover at different speeds",
    "Correct. Muscle contraction and inflammation change at different speeds, so early improvement may leave continuing airway inflammation."],
   ["Bronchoconstriction lasts longer than inflammation",
    "That reverses the pattern: the inflammation is what lingers after early improvement.", RV],
   ["The airway walls have been destroyed",
    "Destroyed, dilated bronchi describe bronchiectasis; asthmatic airways are inflamed, not destroyed.", CD],
   ["Mucus production has stopped",
    "Stopping mucus would not explain lingering inflammation; the two components simply change at different speeds.", CM]],
  c(44)),

]
