# -*- coding: utf-8 -*-
"""Lecture 44 vignette pool C -- pleural effusion causes and examination (s81-89), imaging and fluid analysis with
Light's criteria worked from the stem's values (s90-101, s112), exudates (chylothorax, empyema, s102-109),
transudates and effusion treatment (s110-114) and pleurodynia (s116-119).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md. Light's items show every ratio in the key's
explanation (s101: exudate if AT LEAST ONE of pleural/serum protein over 0.5, pleural/serum lactate dehydrogenase
over 0.6, pleural lactate dehydrogenase over two-thirds of the upper limit of normal serum lactate dehydrogenase;
s110: transudate if all are absent). Every stem gives serum values with their normal range (lactate dehydrogenase
140-280 units/L, so two-thirds of the upper limit is about 187); each stem meets exactly the criteria its key
names, and no ratio sits on a cutoff. The count item is ordered 0 < 1 < 2 < 3 (ORD).

Held for the scope (cms_e7l44_scope.py): the s97 fluid-test thresholds are never keyed; no item asks the
exudate-or-transudate class of pulmonary embolism, malignancy, chylothorax, pancreatic disease or sarcoidosis, and
none offers both ultrasound and an upright film as the INITIAL test for an effusion; fluid color is never the sole
basis of a classification (s98: appearance alone is not diagnostic); octreotide is asked for its use, not its
mechanism; pleurodynia durations (s118 vs s119) are never written; the creatine kinase rise is keyed from s116/s118.
Fremitus is decreased over an effusion (s87). Picture slides used: s83 (infection risk factors), s97 (management
column: diuretics, therapeutic thoracentesis, pleurodesis for expandable lungs, indwelling catheter for
non-expandable lungs or rapidly recurring fluid), s98/s99 color guide (distractors only), s112, s119.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e7l44_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


def ORD(d, asc):
    d["ordered"] = True; d["asc"] = asc; return d


EX_P = "Exudate, by protein ratio"
EX_LR = "Exudate, by lactate dehydrogenase ratio"
EX_LL = "Exudate, by lactate dehydrogenase level"
TR_N = "Transudate, no criterion met"

QUESTIONS = [

# ---------------------------------------------------------------- pleural effusion: causes and examination
V(T_EFF, IO_A,
  "A 67-year-old man has progressive dyspnea and a dry cough. Over the lower right chest there is dullness to percussion, decreased tactile fremitus (vibrations from the larynx poorly felt on the chest wall) and diminished breath sounds, with bronchial breath sounds at the upper edge of the dull area. Which condition best explains these findings?",
  [["Pleural effusion",
    "Correct. Dyspnea and dry cough are the most common symptoms of pleural effusion. Fluid is dull to percussion and obstructs the transmission of vibrations, so fremitus decreases; breath sounds are diminished over the effusion, while bronchial breath sounds increase toward its top, exactly his examination."],
   ["Pneumothorax",
    "Pneumothorax also decreases fremitus and breath sounds, because pleural air blocks transmission. Tell: air is hyperresonant to percussion, and his lower right chest is dull, the note of fluid.", "ruled out by a stated finding"],
   ["Pneumonia infiltrate",
    "An infiltrate is fluid within the lung itself, while an effusion collects in the pleural space and pushes against the lung. Tell: dullness with quiet breath sounds over the area and bronchial sounds only at its upper edge is the effusion pattern.", "competing diagnosis"],
   ["Pleurisy",
    "Pleurisy is inflammation of the parietal pleura with sharp pain and a friction rub, and its palpation and percussion depend on the underlying condition. Tell: dullness with decreased fremitus means fluid has collected, not inflammation alone.", "competing diagnosis"]],
  CS(12, 23, 85, 87, 88, 89), "manifestation", "diagnosis"),

V(T_EFF, IO_A,
  "A 38-year-old man has a new right pleural effusion. For 2 months he has had fevers, drenching night sweats, hemoptysis and a 6 kg weight loss. He has no leg swelling or orthopnea and no purulent sputum. Which is the most likely cause of his effusion?",
  [["Tuberculosis",
    "Correct. Fever, night sweats, hemoptysis and weight loss together are the extrapulmonary clue set that points to tuberculosis in a patient with an effusion. Tuberculosis is also the leading cause of exudative effusion worldwide."],
   ["Malignancy",
    "Hemoptysis on its own raises the question of malignancy. Tell: his full set of fever, night sweats, hemoptysis and weight loss is the tuberculosis clue set, and the fevers and sweats are not part of the malignancy clue.", "competing diagnosis"],
   ["Heart failure",
    "Heart failure is suggested by lower extremity edema, orthopnea and paroxysmal nocturnal dyspnea, and it is the leading cause of effusion overall. Tell: he has none of those, and fevers with night sweats point to an infection.", "ruled out by a stated finding"],
   ["Pneumonia",
    "Pneumonia is suggested by fever, purulent sputum and pleuritic chest pain, usually over days. Tell: he has no purulent sputum, and two months of night sweats and weight loss fit tuberculosis.", "ruled out by a stated finding"]],
  CS(83, 86, 103), "etiology", "diagnosis"),

V(T_EFF, IO_A,
  "A 74-year-old woman has a very large left pleural effusion, estimated at more than 1,000 mL on imaging, with marked dyspnea. Which inspection finding is expected?",
  [["Trachea shifted to the right",
    "Correct. With an effusion over 1,000 mL, the trachea shifts away from the involved side, so a left effusion pushes it to the right; inspection also shows asymmetrical thoracic expansion. Small effusions under 300 mL produce no examination findings, but hers is large."],
   ["Trachea pulled to the left",
    "A large effusion pushes the trachea away from the involved side, not toward it; that shift appears once the fluid passes 1,000 mL. Tell: her fluid is on the left, so the shift is to the right.", "reversed direction or value"],
   ["Symmetric chest expansion",
    "Inspection over a pleural effusion shows asymmetrical thoracic expansion, the affected side moving less. Tell: a left effusion over 1,000 mL limits expansion on that side.", "reversed direction or value"],
   ["No findings at this size",
    "Small effusions, under 300 mL, produce no physical examination findings. Tell: hers is more than 1,000 mL, large enough to shift the trachea away from the effusion.", "wrong stage or severity"]],
  C(87), "test finding", "test"),

V(T_EFF, IO_A,
  "A 56-year-old man with community-acquired pneumonia has a small parapneumonic effusion. His history includes peritoneal dialysis, asbestos exposure at a shipyard job, a past thoracic operation and poor dental hygiene. Which item in his history most raises the risk that the effusion becomes infected?",
  [["Poor dental hygiene",
    "Correct. The listed risk factors for an infection-related effusion are diabetes, alcoholism, immunosuppression and poor dental hygiene. If microorganisms infect the pleural space, a complicated parapneumonic effusion or empyema may result, so his dental hygiene matters most here."],
   ["Peritoneal dialysis",
    "Peritoneal dialysis causes effusions by sending peritoneal fluid across the diaphragm through microperforations. Tell: it explains how fluid can reach the chest, not why pleural fluid would become infected.", "adjacent fact"],
   ["Asbestos exposure",
    "Asbestos exposure belongs in the occupational history of an effusion, and asbestosis is an associated exudative disorder. Tell: it is a cause of effusion, not one of the infection risk factors.", "adjacent fact"],
   ["Past thoracic surgery",
    "Thoracic surgery is the most common traumatic cause of chylothorax, through disruption of the thoracic duct. Tell: it relates to chyle in the pleural space, not to infection of a parapneumonic effusion.", "adjacent fact"]],
  CS(82, 83, 84, 103, 105, 107), "risk factors", "complication"),

V(T_EFF, IO_A,
  "A 45-year-old woman with nephrotic syndrome and a serum albumin of 1.8 g/dL (normal 3.5-5.0 g/dL) has bilateral pleural effusions. She asks how her kidney disease causes fluid around her lungs. Which explanation is accurate?",
  [["Low albumin lowers oncotic pressure",
    "Correct. Hypoalbuminemia from nephrotic syndrome or cirrhosis reduces intravascular oncotic pressure, so fluid leaves the vessels for the pleural space. Nephrotic syndrome causes effusions when albumin falls below 2 g/dL, and hers is 1.8."],
   ["High capillary hydrostatic pressure",
    "Increased capillary hydrostatic pressure is the mechanism in heart failure, the leading cause of effusion. Tell: her cause is kidney protein loss, which lowers oncotic pressure rather than raising hydrostatic pressure.", "confused mechanism or drug class"],
   ["Blocked lymphatic drainage",
    "Decreased lymphatic drainage or complete lymphatic blockage is the mechanism in malignancy and trauma. Tell: her albumin of 1.8 g/dL points to lost oncotic pressure, not blocked lymphatics.", "confused mechanism or drug class"],
   ["Inflamed, leaky pleural membranes",
    "Altered permeability of the pleural membranes is the mechanism of inflammation and malignancy. Tell: nephrotic syndrome acts through low albumin and reduced oncotic pressure, not through inflamed pleura.", "confused mechanism or drug class"]],
  CS(81, 82, 83), "etiology", "education"),

V(T_EFF, IO_A,
  "A 63-year-old man on peritoneal dialysis develops a right pleural effusion. He has no heart failure, and his serum albumin is normal at 4.0 g/dL (normal 3.5-5.0 g/dL). He asks how the dialysis fluid in his abdomen could reach his chest. Which explanation is accurate?",
  [["It crosses the diaphragm",
    "Correct. In cirrhosis and peritoneal dialysis, increased peritoneal fluid leaks, or extravasates, across the diaphragm through microperforations into the pleural space. Peritoneal dialysis is listed among the conditions associated with transudates."],
   ["It raises capillary pressure",
    "Increased capillary hydrostatic pressure is how heart failure causes effusion. Tell: he has no heart failure; his fluid comes from the peritoneal cavity itself.", "ruled out by a stated finding"],
   ["It lowers oncotic pressure",
    "Reduced intravascular oncotic pressure from hypoalbuminemia drives the effusions of nephrotic syndrome and cirrhosis. Tell: his albumin is normal at 4.0 g/dL, so oncotic pressure is not the problem.", "ruled out by a stated finding"],
   ["It blocks lymph drainage",
    "Decreased or blocked lymphatic drainage is the mechanism in malignancy and trauma. Tell: dialysis fluid reaches the chest by crossing the diaphragm through microperforations, not by blocking lymphatics.", "confused mechanism or drug class"]],
  CS(81, 82, 111), "etiology", "education"),

# ---------------------------------------------------------------- imaging and fluid analysis: Light's criteria
V(T_EFF_DX, IO_A,
  "A 59-year-old woman has a new left pleural effusion with no clear clinical cause, and diagnostic thoracentesis is performed. Pleural fluid protein is 4.2 g/dL with serum protein 7.0 g/dL (normal 6.0-8.3 g/dL). Pleural fluid lactate dehydrogenase is 90 units/L with serum lactate dehydrogenase 200 units/L (normal 140-280 units/L). How is the effusion classified by Light's criteria?",
  [[EX_P,
    "Correct. Light's criteria call fluid exudative when at least one is met. Protein ratio 4.2 / 7.0 = 0.60, above 0.5: met. Lactate dehydrogenase ratio 90 / 200 = 0.45, not above 0.6. Fluid lactate dehydrogenase 90 is under two-thirds of the 280 upper limit, about 187. One criterion is enough: exudate."],
   [EX_LR,
    "The lactate dehydrogenase ratio is 90 / 200 = 0.45, which does not exceed 0.6. Tell: the criterion she meets is the protein ratio, 4.2 / 7.0 = 0.60, above 0.5.", "reversed direction or value"],
   [EX_LL,
    "The level criterion asks whether fluid lactate dehydrogenase exceeds two-thirds of the upper limit of normal, 2/3 of 280, about 187. Tell: her fluid value of 90 is far below that; the protein ratio of 0.60 is what makes her fluid exudative.", "reversed direction or value"],
   [TR_N,
    "A transudate needs every one of Light's criteria to be absent. Tell: her protein ratio, 4.2 / 7.0 = 0.60, is above 0.5, so one criterion is met and the fluid is an exudate.", "reversed direction or value"]],
  CS(96, 101, 110, 112), "test finding", "classify"),

V(T_EFF_DX, IO_A,
  "A 66-year-old man has a new right pleural effusion with no clear clinical cause, and diagnostic thoracentesis is performed. Pleural fluid protein is 2.8 g/dL with serum protein 7.0 g/dL (normal 6.0-8.3 g/dL). Pleural fluid lactate dehydrogenase is 160 units/L with serum lactate dehydrogenase 220 units/L (normal 140-280 units/L). How is the effusion classified by Light's criteria?",
  [[EX_LR,
    "Correct. Protein ratio 2.8 / 7.0 = 0.40, not above 0.5. Lactate dehydrogenase ratio 160 / 220 = 0.73, above 0.6: met. Fluid lactate dehydrogenase 160 is under two-thirds of the 280 upper limit, about 187. Meeting at least one criterion makes the fluid an exudate."],
   [EX_P,
    "The protein ratio is 2.8 / 7.0 = 0.40, which does not exceed 0.5. Tell: the criterion he meets is the lactate dehydrogenase ratio, 160 / 220 = 0.73, above 0.6.", "reversed direction or value"],
   [EX_LL,
    "The level criterion needs fluid lactate dehydrogenase above two-thirds of the 280 upper limit, about 187. Tell: his fluid value of 160 falls short; it is the ratio, 160 / 220 = 0.73, that crosses 0.6.", "reversed direction or value"],
   [TR_N,
    "A transudate requires that all of Light's criteria be absent. Tell: his lactate dehydrogenase ratio of 160 / 220 = 0.73 exceeds 0.6, so one criterion is met and the fluid is exudative.", "reversed direction or value"]],
  CS(96, 101, 110, 112), "differential", "classify"),

V(T_EFF_DX, IO_A,
  "A 71-year-old woman has a new left pleural effusion with no clear clinical cause, and diagnostic thoracentesis is performed. Pleural fluid protein is 2.1 g/dL with serum protein 7.0 g/dL (normal 6.0-8.3 g/dL). Pleural fluid lactate dehydrogenase is 210 units/L with serum lactate dehydrogenase 450 units/L (normal 140-280 units/L). How is the effusion classified by Light's criteria?",
  [[EX_LL,
    "Correct. Protein ratio 2.1 / 7.0 = 0.30, not above 0.5. Lactate dehydrogenase ratio 210 / 450 = 0.47, not above 0.6. But fluid lactate dehydrogenase 210 exceeds two-thirds of the 280 upper limit of normal serum lactate dehydrogenase, about 187: met, so the fluid is an exudate."],
   [EX_P,
    "The protein ratio is 2.1 / 7.0 = 0.30, below the 0.5 cutoff. Tell: her exudate criterion is the fluid lactate dehydrogenase of 210, above two-thirds of the 280 upper limit, about 187.", "reversed direction or value"],
   [EX_LR,
    "The ratio is 210 / 450 = 0.47, under 0.6, because her serum lactate dehydrogenase is itself high. Tell: the third criterion compares the fluid value with the normal upper limit, and 210 is above two-thirds of 280, about 187.", "reversed direction or value"],
   [TR_N,
    "A transudate needs all three criteria absent. Tell: both ratios miss, but her fluid lactate dehydrogenase of 210 is above two-thirds of the 280 upper limit, about 187, so one criterion is met.", "reversed direction or value"]],
  CS(96, 101, 110, 112), "test finding", "classify"),

V(T_EFF_DX, IO_A,
  "A 77-year-old man has a new right pleural effusion with no clear clinical cause, and diagnostic thoracentesis is performed. Pleural fluid protein is 1.8 g/dL with serum protein 6.9 g/dL (normal 6.0-8.3 g/dL). Pleural fluid lactate dehydrogenase is 80 units/L with serum lactate dehydrogenase 190 units/L (normal 140-280 units/L). How is the effusion classified by Light's criteria?",
  [[TR_N,
    "Correct. Protein ratio 1.8 / 6.9 = 0.26, not above 0.5. Lactate dehydrogenase ratio 80 / 190 = 0.42, not above 0.6. Fluid lactate dehydrogenase 80 is under two-thirds of the 280 upper limit, about 187. With all of Light's criteria absent, the fluid is a low-protein transudate."],
   [EX_P,
    "The protein criterion needs a pleural to serum protein ratio above 0.5. Tell: his is 1.8 / 6.9 = 0.26, about half the cutoff, consistent with a low-protein transudate.", "reversed direction or value"],
   [EX_LR,
    "The ratio criterion needs pleural to serum lactate dehydrogenase above 0.6. Tell: 80 / 190 = 0.42 falls short, and neither of the other two criteria is met.", "reversed direction or value"],
   [EX_LL,
    "The level criterion needs fluid lactate dehydrogenase above two-thirds of the 280 upper limit, about 187. Tell: his fluid value is 80, well below it, so no criterion is met.", "reversed direction or value"]],
  CS(96, 101, 110, 112), "differential", "classify"),

ORD(V(T_EFF_DX, IO_A,
  "A 62-year-old woman with a new pleural effusion undergoes diagnostic thoracentesis. Pleural fluid protein is 3.9 g/dL with serum protein 6.5 g/dL (normal 6.0-8.3 g/dL). Pleural fluid lactate dehydrogenase is 150 units/L with serum lactate dehydrogenase 200 units/L (normal 140-280 units/L). How many of Light's criteria does the fluid meet, and what does that make it?",
  [["2 of 3; exudate",
    "Correct. Protein ratio 3.9 / 6.5 = 0.60, above 0.5: met. Lactate dehydrogenase ratio 150 / 200 = 0.75, above 0.6: met. Fluid lactate dehydrogenase 150 is under two-thirds of the 280 upper limit, about 187: not met. Two of three, and one is already enough for an exudate."],
   ["0 of 3; transudate",
    "A transudate needs every criterion absent. Tell: her protein ratio, 3.9 / 6.5 = 0.60, and her lactate dehydrogenase ratio, 150 / 200 = 0.75, both cross their cutoffs.", "reversed direction or value"],
   ["1 of 3; exudate",
    "Exudate is right, but the count misses a criterion. Tell: both ratios are met, protein 0.60 above 0.5 and lactate dehydrogenase 0.75 above 0.6; only the level criterion, 150 against about 187, is not.", "wrong stage or severity"],
   ["3 of 3; exudate",
    "Exudate is right, but the third criterion is not met. Tell: fluid lactate dehydrogenase of 150 is under two-thirds of the 280 upper limit of normal serum lactate dehydrogenase, about 187.", "wrong stage or severity"]],
  CS(101, 112), "test finding", "classify"), [1, 2, 0, 3]),

V(T_EFF_DX, IO_A,
  "A 64-year-old woman who was treated for breast cancer 8 years ago has a new right pleural effusion with no other clinical cause, and diagnostic thoracentesis is performed. Which pleural fluid study is sent specifically to detect a malignant effusion?",
  [["Cytology",
    "Correct. Pleural fluid is sent for protein, lactate dehydrogenase, white cell count with differential, Gram stain, cytology and microbiological culture, and cytology is the study that detects malignant effusions. Malignant effusions can occur years after a cancer diagnosis, and breast carcinoma is among their leading causes."],
   ["Gram stain",
    "A Gram stain looks for bacteria, the concern in a parapneumonic effusion or empyema. Tell: her history points to cancer returning, and malignant cells are found by cytology.", "adjacent fact"],
   ["Microbiological culture",
    "Culture grows organisms from an infected effusion such as empyema. Tell: she has no fever or pneumonia, and culture does not detect malignant cells; cytology does.", "adjacent fact"],
   ["Triglyceride level",
    "Elevated triglycerides in milky fluid identify a chylothorax from thoracic duct disruption. Tell: her concern is malignancy years after breast cancer, which cytology addresses.", "adjacent fact"]],
  CS(84, 96, 99, 102, 105), "initial test", "test"),

V(T_EFF_DX, IO_A,
  "A 55-year-old man has a new moderate left pleural effusion on chest radiograph. He has no heart, liver or kidney disease, no fever or cough, and no history of cancer or trauma, so no clinical cause is apparent. Which is the most appropriate next step?",
  [["Diagnostic thoracentesis",
    "Correct. Diagnostic thoracentesis is performed when there is a new pleural effusion with no clinical cause. It removes 50-100 mL for visualization and analysis, sent for protein, lactate dehydrogenase, cell count, Gram stain, cytology and culture, and ultrasound is used to guide it."],
   ["Chemical pleurodesis",
    "Chemical pleurodesis obliterates the pleural space, often for recurrent malignant effusions in an expandable lung. Tell: his effusion is new and has no diagnosis yet, so the fluid must be analyzed first.", "wrong stage or severity"],
   ["Indwelling pleural catheter",
    "An indwelling tunneled pleural catheter is drained at home for rapidly recurring fluid or a short prognosis, as palliative care. Tell: he has a first, undiagnosed effusion, not a recurring one.", "wrong stage or severity"],
   ["Diuretic therapy",
    "Diuretics are the initial treatment for transudates secondary to heart failure. Tell: he has no heart disease and no known cause, so the fluid is sampled before any treatment is chosen.", "ruled out by a stated finding"]],
  CS(95, 96, 97, 99, 113), "initial test", "next step"),

# ---------------------------------------------------------------- exudates: chylothorax and empyema
V(T_EXUD, IO_A,
  "A 57-year-old man has 5 days of fever, cough with purulent sputum and right pleuritic chest pain, and a right pleural effusion is tapped. Pleural fluid protein is 4.4 g/dL with serum protein 7.2 g/dL (normal 6.0-8.3 g/dL). Pleural fluid lactate dehydrogenase is 240 units/L with serum lactate dehydrogenase 210 units/L (normal 140-280 units/L). Which is the most likely cause of the effusion?",
  [["Pneumonia",
    "Correct. Protein ratio 4.4 / 7.2 = 0.61, above 0.5; lactate dehydrogenase ratio 240 / 210 = 1.14, above 0.6; fluid lactate dehydrogenase 240 exceeds two-thirds of 280, about 187. The fluid is an exudate, pneumonia is the most common cause of exudative effusion, and fever with purulent sputum and pleuritic pain is its clue set."],
   ["Heart failure",
    "Heart failure causes more than 90% of transudates, with edema, orthopnea and paroxysmal nocturnal dyspnea. Tell: his fluid meets all three of Light's criteria, an exudate, and his story is an infection.", "ruled out by a stated finding"],
   ["Cirrhosis with ascites",
    "Cirrhosis with ascites causes a transudate, through peritoneal fluid crossing the diaphragm and low oncotic pressure. Tell: his fluid is exudative by every criterion, and he has fever with purulent sputum.", "ruled out by a stated finding"],
   ["Nephrotic syndrome",
    "Nephrotic syndrome causes a transudate by lowering oncotic pressure as albumin is lost. Tell: his protein ratio of 0.61 and lactate dehydrogenase values mark an exudate, which fits his pneumonia.", "ruled out by a stated finding"]],
  CS(86, 101, 102, 110, 111, 112), "epidemiology", "diagnosis"),

V(T_EXUD, IO_A,
  "A 61-year-old woman being treated with antibiotics for bacterial pneumonia still has fever and pleuritic pain after several days, and her parapneumonic effusion has grown. Thoracentesis returns thick purulent fluid. Which is the most appropriate treatment?",
  [["Drainage plus antibiotics",
    "Correct. Empyema is purulent fluid in the pleural space, and bacterial pneumonia with a parapneumonic effusion is its most common precursor. It is suspected when pneumonia does not resolve with therapy and diagnosed by purulent material on thoracentesis; treatment is drainage and antibiotics, treating the underlying disease and analgesia, and prompt therapy is critical."],
   ["A longer antibiotic course",
    "Antibiotics are half of empyema treatment, but pus in the pleural space also has to be drained. Tell: her pneumonia did not resolve on antibiotics, and the treatment pairs drainage with antibiotics.", "wrong stage or severity"],
   ["Chemical pleurodesis",
    "Chemical pleurodesis obliterates the pleural space, mainly for recurrent malignant effusions or recurrent pneumothorax. Tell: an infected pleural space needs drainage and antibiotics, not obliteration.", "adjacent fact"],
   ["Diuretic therapy",
    "Diuretics are the initial treatment for transudates secondary to heart failure. Tell: her fluid is pus from an infection, an exudative process that diuretics do not address.", "competing diagnosis"]],
  CS(97, 107, 108), "first-line", "treatment"),

V(T_EXUD, IO_A,
  "A 66-year-old man develops a right pleural effusion 5 days after thoracic surgery. Thoracentesis returns milky white fluid. Which pleural fluid result confirms the suspected diagnosis?",
  [["Elevated triglycerides",
    "Correct. Chylothorax is thoracic duct disruption that lets lipid from chyle collect in the pleural space, and trauma such as thoracic surgery is its most common cause. Thoracentesis shows milky fluid with elevated triglycerides."],
   ["Purulent material",
    "Purulent material on thoracentesis diagnoses empyema, usually after bacterial pneumonia. Tell: his fluid is milky after thoracic surgery, the picture of chyle, and fluid appearance alone is not diagnostic without the triglyceride level.", "competing diagnosis"],
   ["Malignant cells",
    "Cytology detects malignant cells in a malignant effusion. Tell: his effusion followed thoracic surgery with milky fluid, which points to thoracic duct injury and a triglyceride-rich fluid.", "competing diagnosis"],
   ["Hematocrit above half of blood's",
    "A pleural fluid hematocrit over 50% of the blood hematocrit defines a hemothorax, with bloody fluid. Tell: his fluid is milky, not bloody, so the confirming test is the triglyceride level.", "competing diagnosis"]],
  CS(74, 98, 99, 104, 105, 108), "gold standard", "test"),

V(T_EXUD, IO_A,
  "A 58-year-old woman has a chylothorax after thoracic surgery, managed with a chest tube. Over several days the tube has drained large volumes of milky fluid, and she is losing weight. Which practice should be avoided?",
  [["Excessive drainage",
    "Correct. Chylothorax is managed with chest tube placement or intermittent thoracentesis while avoiding excessive drainage, because excessive loss of chyle can impact nutritional status. Her large volumes and weight loss show that risk."],
   ["Octreotide therapy",
    "Octreotide is used in chylothorax to decrease chyle drainage. Tell: it lowers the very output she is losing, so it is a treatment to use, not one to avoid.", "reversed direction or value"],
   ["Low long-chain fat diet",
    "Decreasing long-chain triglycerides in the diet decreases chyle drainage, because they are absorbed through the lymphatic system. Tell: this nutrition step lowers her chyle output and is recommended.", "reversed direction or value"],
   ["Intermittent thoracentesis",
    "Intermittent thoracentesis is one of the two drainage approaches for chylothorax, beside a chest tube. Tell: the method is acceptable; it is the excessive volume removed that harms her nutrition.", "reversed direction or value"]],
  CS(105, 106), "avoid", "avoid"),

# ---------------------------------------------------------------- transudates and effusion treatment
V(T_TRANS, IO_A,
  "A 58-year-old man with alcohol-related cirrhosis has tense ascites and a new right pleural effusion. He has no orthopnea, leg edema or known heart disease, and no fever or cough. Pleural fluid protein is 1.2 g/dL with serum protein 5.8 g/dL (normal 6.0-8.3 g/dL). Pleural fluid lactate dehydrogenase is 70 units/L with serum lactate dehydrogenase 180 units/L (normal 140-280 units/L). Which is the most likely cause of the effusion?",
  [["Cirrhosis",
    "Correct. Protein ratio 1.2 / 5.8 = 0.21, lactate dehydrogenase ratio 70 / 180 = 0.39, and fluid lactate dehydrogenase 70 is under two-thirds of 280, about 187: all of Light's criteria are absent, a transudate. Cirrhosis with ascites sends peritoneal fluid across the diaphragm and lowers oncotic pressure."],
   ["Heart failure",
    "Heart failure causes more than 90% of transudates, through increased capillary hydrostatic pressure. Tell: he has no orthopnea, leg edema or heart disease, and his ascites with cirrhosis explains the transudate.", "ruled out by a stated finding"],
   ["Pneumonia",
    "Pneumonia is the most common cause of exudative effusion, with fever, purulent sputum and pleuritic pain. Tell: he has no fever or cough, and his fluid meets none of Light's criteria.", "ruled out by a stated finding"],
   ["Tuberculosis",
    "Tuberculosis is the leading cause of exudative effusion worldwide, with fever, night sweats, hemoptysis and weight loss. Tell: his fluid is a transudate with every criterion absent, and he has no infectious symptoms.", "ruled out by a stated finding"]],
  CS(81, 82, 101, 103, 110, 111), "etiology", "diagnosis"),

V(T_TRANS, IO_POP,
  "A 78-year-old woman with known heart failure has increasing lower extremity edema, orthopnea and paroxysmal nocturnal dyspnea, and her chest radiograph shows bilateral pleural effusions. She is comfortable at rest. Which is the most appropriate next step?",
  [["Diuretic therapy",
    "Correct. Her edema, orthopnea and paroxysmal nocturnal dyspnea give the effusions a clear clinical cause: heart failure, which raises capillary hydrostatic pressure and causes more than 90% of transudates. Effusions are managed by treating the underlying disorder, and diuretics are the initial treatment for heart failure transudates."],
   ["Diagnostic thoracentesis",
    "Diagnostic thoracentesis is performed for a new pleural effusion with no clinical cause. Tell: her heart failure story explains the bilateral effusions, so treating the cause comes first.", "ruled out by a stated finding"],
   ["Chemical pleurodesis",
    "Pleurodesis obliterates the pleural space and is often used for recurrent malignant effusions as palliative care. Tell: her effusions come from heart failure, treated by treating the heart failure.", "wrong stage or severity"],
   ["Indwelling pleural catheter",
    "An indwelling tunneled pleural catheter suits a non-expandable lung, rapidly recurring fluid or a short prognosis. Tell: she is comfortable, and her effusions should respond to treating the heart failure.", "wrong stage or severity"]],
  CS(82, 86, 96, 97, 111, 113), "first-line", "next step"),

V(T_TRANS, IO_POP,
  "A 72-year-old man with metastatic lung cancer and a short prognosis has a malignant pleural effusion that recurs within days of each therapeutic thoracentesis. He wants to spend as little time in the hospital as possible. Which option best fits his goals?",
  [["Indwelling tunneled pleural catheter",
    "Correct. An indwelling tunneled pleural catheter is placed in the outpatient setting, drained intermittently at home and minimizes time in the hospital for patients with short prognoses. It is the option for rapidly recurring fluid, which his effusion is."],
   ["Repeated thoracentesis visits",
    "Therapeutic thoracentesis relieves dyspnea, but his fluid returns within days each time. Tell: rapidly recurring fluid and a wish to stay home point to a catheter he can drain at home.", "wrong stage or severity"],
   ["Video-assisted thoracoscopic surgery",
    "Thoracoscopic surgery carries the risks of general anesthesia, patient discomfort and greater cost. Tell: with a short prognosis and a wish to avoid the hospital, an outpatient catheter fits his goals better.", "ruled out by a stated finding"],
   ["Chest tube with admission",
    "A chest tube drains the effusion but keeps him in the hospital while it is in place. Tell: his goal is the least time in the hospital, and the tunneled catheter is placed as an outpatient and drained at home.", "ruled out by a stated finding"]],
  CS(49, 97, 113, 114), "agent/regimen", "treatment"),

V(T_TRANS, IO_A,
  "A 60-year-old woman with metastatic breast cancer has a recurrent malignant pleural effusion. After therapeutic thoracentesis relieves her dyspnea, a follow-up film shows that her lung fully re-expands. Which procedure best prevents the fluid from reaccumulating?",
  [["Chemical pleurodesis",
    "Correct. Pleurodesis is often used for recurrent malignant effusions from lung, breast or ovarian cancer as palliative care, and malignant effusion is its most common indication. Therapeutic thoracentesis showed her lung expands, and chemical pleurodesis obliterates the pleural space in expandable lungs, leaving no room for fluid."],
   ["Diuretic therapy",
    "Diuretics are the initial treatment for transudates secondary to heart failure. Tell: her effusion is malignant and recurrent, with no heart failure behind it, a problem diuretics do not solve.", "competing diagnosis"],
   ["Diagnostic thoracentesis",
    "Diagnostic thoracentesis analyzes a new effusion with no clinical cause. Tell: her effusion is already known to be malignant and recurrent; the question now is prevention.", "wrong stage or severity"],
   ["Octreotide therapy",
    "Octreotide decreases chyle drainage in chylothorax, the effusion caused by thoracic duct disruption. Tell: her fluid comes from metastatic breast cancer, not from the thoracic duct, so it does nothing here.", "competing diagnosis"]],
  CS(45, 46, 97, 106, 113), "escalation", "treatment"),

# ---------------------------------------------------------------- pleurodynia
V(T_PDYN, IO_A,
  "A 17-year-old boy in July develops sudden fever and attacks of severe, knife-like right chest pain lasting 15-30 minutes, with sweating and rapid breathing during each attack. A week earlier he had an upper respiratory infection. The muscles over his lower ribs are tender, and his chest radiograph is normal. What is the most likely diagnosis?",
  [["Pleurodynia",
    "Correct. Pleurodynia, also called Bornholm disease, is a viral myalgia, often from coxsackie B virus, that typically follows an upper respiratory or gastrointestinal infection and peaks in summer. Acute fever with paroxysms of knife-like pain lasting 15-30 minutes, sweating, tachypnea, tender muscles and a normal film fit."],
   ["Pleurisy",
    "Pleurisy is inflammation of the parietal pleura, with a friction rub that disappears on breath holding. Tell: his pain comes in timed paroxysms with tender intercostal muscles after a viral illness, the picture of a viral myalgia.", "competing diagnosis"],
   ["Pneumothorax",
    "A pneumothorax shows a visceral pleural line on the chest radiograph, with hyperresonance and diminished breath sounds. Tell: his film is normal, and fever with tender muscles does not fit pleural air.", "ruled out by a stated finding"],
   ["Costochondritis",
    "Costochondritis is inflammation of the costal cartilage, one of the other causes of chest pain. Tell: his fever, recurring 15-30 minute attacks and tender muscles after an upper respiratory infection point to a viral myalgia.", "competing diagnosis"]],
  CS(12, 13, 26, 116, 117, 118, 119), "manifestation", "diagnosis"),

V(T_PDYN, IO_A,
  "A 23-year-old woman has sudden fever and paroxysms of knife-like pleuritic pain lasting 15-30 minutes after a gastrointestinal illness, with tender intercostal muscles and a normal chest radiograph. Which laboratory finding supports the suspected diagnosis?",
  [["Elevated serum creatine kinase",
    "Correct. In pleurodynia, the virus, often coxsackie B, targets the striated intercostal muscles, causing inflammation or necrosis that frequently raises serum creatine kinase. Elevated creatine kinase is its listed diagnostic finding, and the chest radiograph is usually normal."],
   ["Elevated pleural triglycerides",
    "Elevated triglycerides in milky pleural fluid identify a chylothorax. Tell: she has no effusion on a normal film; her disease is in the intercostal muscles, measured by serum creatine kinase.", "competing diagnosis"],
   ["Purulent pleural fluid",
    "Purulent fluid on thoracentesis diagnoses empyema after bacterial pneumonia. Tell: her chest radiograph is normal, so there is no effusion to sample, and her disease sits in the intercostal muscles.", "ruled out by a stated finding"],
   ["Bloody pleural fluid",
    "Bloody pleural fluid suggests a hemothorax or malignancy. Tell: her film shows no effusion, and her tender muscles after a viral illness point to a muscle enzyme in the blood.", "ruled out by a stated finding"]],
  CS(98, 105, 108, 116, 118), "test finding", "test"),

V(T_PDYN, IO_A,
  "A 15-year-old girl has pleurodynia diagnosed during a summer outbreak at her camp, with fever, knife-like pleuritic pain and tender intercostal muscles. Her chest radiograph is normal. Which treatment is most appropriate?",
  [["Anti-inflammatory drug and heat",
    "Correct. Treatment of pleurodynia is supportive: nonsteroidal anti-inflammatory drugs and application of heat to the affected muscles. The course is typically benign, though symptoms may recur a few days later, and hand hygiene limits fecal-oral spread."],
   ["Chest tube drainage",
    "A chest tube drains air or fluid from the pleural space in pneumothorax or effusion. Tell: her film is normal, and the problem is inflamed intercostal muscle, not the pleural space.", "ruled out by a stated finding"],
   ["Oxygen by non-rebreather",
    "Oxygen at 100% by non-rebreather mask speeds resorption of air in a small pneumothorax. Tell: there is no pleural air on her normal film; her viral myalgia gets supportive care.", "adjacent fact"],
   ["Therapeutic thoracentesis",
    "Therapeutic thoracentesis removes pleural fluid to relieve dyspnea. Tell: she has no effusion to remove; pleurodynia is treated with anti-inflammatory drugs and heat.", "ruled out by a stated finding"]],
  CS(53, 96, 118, 119), "first-line", "treatment"),

]
