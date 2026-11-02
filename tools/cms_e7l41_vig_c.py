# -*- coding: utf-8 -*-
"""Lecture 41 vignette pool C -- hypersensitivity pneumonitis (exposure history, definitive test, first step and
escalation, acute versus chronic form) and acute respiratory distress syndrome (slides 65-74; s72-74 are
pictures, read from the images).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md. Ratio items show the division in the key
explanation; each wrong class says where the ratio really falls.

Acute respiratory distress syndrome oxygenation (s73): arterial oxygen pressure / fraction of inspired oxygen under
300 mm Hg meets the criterion; mild 200-300, moderate 100-200, severe under 100. No ratio sits on a boundary.
Severity options are ordered criterion-not-met < mild < moderate < severe (ORD). Plateau pressure numbers are never
written (SCOPE_BANNED). Every ratio stem says "fraction of inspired oxygen" (REQUIRED).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e7l41_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


def ORD(d, asc):
    d["ordered"] = True; d["asc"] = asc; return d


HP = "Hypersensitivity pneumonitis"
ARDS = "Acute respiratory distress syndrome"

NOT_MET = "Oxygenation criterion not met"
MILD = "Mild acute respiratory distress syndrome"
MOD = "Moderate acute respiratory distress syndrome"
SEV = "Severe acute respiratory distress syndrome"

QUESTIONS = [

# ---------------------------------------------------------------- hypersensitivity pneumonitis
V(HP, IO_A,
  "A 45-year-old dairy farmer develops sudden malaise, chills, fever, cough, dyspnea and nausea several hours after forking moldy hay in a closed barn. He has bibasilar crackles and tachypnea, and he has no history of asthma or allergies. What is the most likely diagnosis?",
  [["Hypersensitivity pneumonitis",
    "Correct. Hypersensitivity pneumonitis, here farmer's lung, is an inflammatory reaction to inhaled organic dust such as moldy hay. Sudden malaise, chills, fever, cough, dyspnea and nausea hours after exposure, with bibasilar crackles and tachypnea, fit, and it is a non-atopic, non-asthmatic disease."],
   ["Allergic asthma",
    "Hypersensitivity pneumonitis is described as non-atopic and non-asthmatic, and his history has neither asthma nor allergies. Tell: fever, chills and malaise hours after moldy hay point to an organic dust pneumonitis, not airway asthma.", "common lay belief"],
   ["Silicosis",
    "Silicosis follows inorganic silica dust from mining, sandblasting, quarry or stone work, built up over years of exposure. Tell: moldy hay is an organic dust, and his illness came within hours of a single exposure on the farm.", "competing diagnosis"],
   ["Acute respiratory distress syndrome",
    "Acute respiratory distress syndrome follows a major insult such as sepsis, aspiration or trauma, with dyspnea 12-48 hours later and refractory hypoxemia. Tell: his trigger is moldy hay, the source of farmer's lung, hours before his symptoms.", "competing diagnosis"]],
  CS(65, 66, 68, 72, 73), "manifestation", "diagnosis"),

V(HP, IO_A,
  "A 60-year-old man who races pigeons has repeated evenings of chills, cough and dyspnea that begin hours after he cleans the lofts and wake him from sleep, mimicking paroxysmal nocturnal dyspnea. His echocardiogram is normal. What is the most likely diagnosis?",
  [["Bird fancier's lung",
    "Correct. Bird fancier's lung is hypersensitivity pneumonitis from bird excreta and feathers. Chills, cough and dyspnea hours after exposure fit, and the illness may mimic paroxysmal nocturnal dyspnea when symptoms start after the exposure, once the patient is home."],
   ["Cardiogenic pulmonary edema",
    "Cardiogenic pulmonary edema is the hydrostatic edema an echocardiogram assesses, with cardiomegaly and vascular engorgement on film. Tell: his echocardiogram is normal and his attacks follow loft cleaning, the pattern of an exposure-driven pneumonitis.", "competing diagnosis"],
   ["Sarcoidosis",
    "Sarcoidosis is a granulomatous disease of unknown cause with insidious symptoms, hilar adenopathy and skin or eye findings. Tell: his symptoms switch on hours after each bird exposure, the hallmark of hypersensitivity pneumonitis.", "competing diagnosis"],
   ["Idiopathic pulmonary fibrosis",
    "Idiopathic pulmonary fibrosis is a slowly progressive disease with an insidious dry cough and no associated cause. Tell: his attacks are episodic and tied to his pigeons, an identifiable organic dust, so his disease is not idiopathic.", "competing diagnosis"]],
  CS(22, 33, 42, 65, 66, 73), "differential", "diagnosis"),

V(HP, IO_A,
  "A 38-year-old bird keeper has had fever, chills, cough and dyspnea hours after cleaning her aviary on several occasions. Her white blood cell count is 15,600/microliter (normal 4,500-11,000) with a left shift. Which test gives a definitive diagnosis?",
  [["Serum antibodies to the bird antigen",
    "Correct. In hypersensitivity pneumonitis, the presence of antibodies to the agent in serum gives the definitive diagnosis. Her white count of 15,600, above the 4,500-11,000 range with a left shift, and her symptoms hours after bird exposure support it but do not confirm it."],
   ["Serum angiotensin-converting enzyme level",
    "An elevated angiotensin-converting enzyme level is a sarcoidosis finding, present in 40-80% of patients. Tell: her symptoms track a bird exposure, and the definitive test for that reaction is serum antibodies to the agent.", "competing diagnosis"],
   ["Chest film during the attack",
    "In acute hypersensitivity pneumonitis, chest films and computed tomography show little change. Tell: a film taken during an attack can look nearly normal, so it cannot give the definitive diagnosis that serum antibodies can.", "wrong stage or severity"],
   ["Pleural fluid cytology",
    "Pleural fluid cytology diagnoses mesothelioma in an asbestos-exposed patient with a pleural effusion. Tell: she has no effusion or asbestos exposure; her exposure is birds, and the test is antibodies to the bird antigen.", "adjacent fact"]],
  CS(44, 59, 65, 69), "gold standard", "test"),

V(HP, IO_A,
  "A 41-year-old cheese maker has recurrent fever, chills, cough and dyspnea hours after handling moldy cheese at work. Hypersensitivity pneumonitis is diagnosed, and her symptoms are mild. What is the first step in treatment?",
  [["Identify and avoid the agent",
    "Correct. Treatment of hypersensitivity pneumonitis starts by identifying the agent responsible and avoiding it. Prompt diagnosis is key to removing the patient from the irritating environment: symptoms can be reversible if caught early, while continued exposure may worsen the disease."],
   ["Oral corticosteroids",
    "Corticosteroids may be helpful in severe cases of hypersensitivity pneumonitis. Tell: her disease is mild, and without removing the moldy cheese exposure the disease can keep worsening, so avoidance comes first.", "wrong stage or severity"],
   ["Lung transplant evaluation",
    "Lung transplant sits at the far end of the hypersensitivity pneumonitis treatment list. Tell: her disease is mild and may be reversible if the agent is removed early, so she is nowhere near transplant.", "wrong stage or severity"],
   ["Inhaled bronchodilators alone",
    "Bronchodilators are supportive treatment, with oxygen and pain medication. Tell: supportive care alone leaves her exposed to the moldy cheese, and continued exposure may lead to a worsened disease state.", "wrong stage or severity"]],
  CS(65, 71), "first-line", "treatment"),

V(HP, IO_A,
  "A 55-year-old farmer with farmer's lung has stopped handling moldy hay, but he remains hypoxic with cyanosis, tachypnea and tachycardia, and his disease is judged severe. Which treatment may be helpful now?",
  [["Corticosteroids",
    "Correct. After the agent is identified and avoided, corticosteroids may be helpful in severe cases of hypersensitivity pneumonitis, with other immunosuppressants and supportive care such as oxygen. His persistent hypoxia, cyanosis, tachypnea and tachycardia despite avoidance mark severe disease."],
   ["Early prone positioning",
    "Early prone positioning decreases mortality in moderate to severe acute respiratory distress syndrome on mechanical ventilation. Tell: his disease is a hypersensitivity reaction to hay, where severe cases call for corticosteroids.", "competing diagnosis"],
   ["High-frequency oscillation",
    "High-frequency oscillatory ventilation provides no proven benefit even in acute respiratory distress syndrome, where it is listed to avoid. Tell: his severe hypersensitivity pneumonitis calls for corticosteroids, not a ventilator mode.", "confused mechanism or drug class"],
   ["Return to work with a mask",
    "Continued exposure may lead to a worsened disease state, so going back to the hay keeps the cause in play. Tell: the first step is to identify and avoid the agent, and severe disease then adds corticosteroids.", "common lay belief"]],
  CS(65, 68, 69, 71, 74), "escalation", "treatment"),

V(HP, IO_A,
  "A 63-year-old woman has kept birds for decades. Over 2 years she has developed a persistent cough, shortness of breath and weight loss, and she now has clubbing of the fingers. Which finding places her hypersensitivity pneumonitis in the chronic form rather than the subacute form?",
  [["Clubbing of the fingers",
    "Correct. Clubbing of the fingers or toes is marked only for chronic hypersensitivity pneumonitis, alongside fatigue and lung fibrosis, after multiple exposures. Cough, shortness of breath and weight loss are shared by the subacute and chronic forms, so they cannot separate the two."],
   ["Weight loss",
    "Anorexia or weight loss is marked for both subacute and chronic hypersensitivity pneumonitis. Tell: a finding shared by both forms cannot separate them; clubbing of the fingers or toes is the chronic-only sign in her history.", "adjacent fact"],
   ["Shortness of breath",
    "Shortness of breath is present in both the subacute and the chronic form. Tell: the signs that belong to the chronic form alone are clubbing, fatigue and lung fibrosis, and clubbing is the one she has.", "adjacent fact"],
   ["Cough",
    "Cough runs through all three forms, acute, subacute and chronic. Tell: it is the least specific of her findings; clubbing of the fingers marks the chronic form, which develops from multiple exposures.", "adjacent fact"]],
  C(67), "manifestation", "classify"),

V(HP, IO_A,
  "A 52-year-old man has acute bird fancier's lung from the pigeons he keeps at home, and his symptoms are settling. He asks whether he can keep the birds if he takes medicine whenever symptoms flare. Which counsel is accurate?",
  [["Continued exposure may worsen his disease",
    "Correct. Prompt diagnosis is key so the patient can be removed from the irritating environment: symptoms can be reversible if caught early, but continued exposure may lead to a worsened disease state. Treatment starts with identifying and avoiding the agent, here his birds."],
   ["Medicine makes ongoing exposure safe",
    "Corticosteroids may help severe cases, but treatment starts with avoiding the agent. Tell: no medicine is described as making continued exposure safe, and continued exposure may worsen the disease toward its chronic form.", "common lay belief"],
   ["His lung damage is already permanent",
    "Hypersensitivity pneumonitis symptoms can be reversible if caught early, and acute disease shows little change on imaging. Tell: his acute illness is settling, so his outcome still depends on removing the birds now.", "wrong stage or severity"],
   ["His symptoms come from asthma",
    "Hypersensitivity pneumonitis is a non-atopic, non-asthmatic inflammatory disease from inhaled organic dust. Tell: his reaction is to the bird antigen itself, so treating it as asthma leaves the exposure in place.", "competing diagnosis"]],
  CS(65, 69, 71), "education", "education"),

V(HP, IO_A,
  "A 47-year-old farmer recovered from acute farmer's lung after a month away from work, and he plans to return to the farm. During his illness he used oxygen, inhaled bronchodilators and pain medication. Which should he avoid?",
  [["Handling moldy hay",
    "Correct. Treatment of hypersensitivity pneumonitis is to identify the responsible agent and avoid it, and moldy hay is the source of farmer's lung. Continued exposure may lead to a worsened disease state, while symptoms caught early can be reversible."],
   ["Inhaled bronchodilators",
    "Bronchodilators are among the supportive treatments for hypersensitivity pneumonitis, with oxygen and pain medication. Tell: supportive therapy is used, not avoided; the thing to avoid is the agent itself, the moldy hay.", "reversed direction or value"],
   ["Supplemental oxygen",
    "Oxygen is a listed supportive treatment for hypersensitivity pneumonitis, which can cause hypoxia. Tell: it is used when needed; the moldy hay that caused his farmer's lung is what he must avoid on his return.", "reversed direction or value"],
   ["Pain medication",
    "Pain medication appears with oxygen and bronchodilators as supportive treatment for hypersensitivity pneumonitis. Tell: none of the supportive therapies is the problem; renewed contact with moldy hay is.", "reversed direction or value"]],
  CS(65, 69, 71), "avoid", "avoid"),

# ---------------------------------------------------------------- acute respiratory distress syndrome: diagnosis
V(ARDS, IO_A,
  "A 58-year-old woman admitted with sepsis develops profound dyspnea 30 hours later. She has tachypnea, intercostal retractions and crackles, and her hypoxemia does not improve with supplemental oxygen. Her chest film shows new bilateral opacities with a normal heart size, and an echocardiogram shows normal cardiac function. What is the most likely diagnosis?",
  [["Acute respiratory distress syndrome",
    "Correct. About one-third of cases present with sepsis, and profound dyspnea develops 12-48 hours after the insult. New bilateral opacities within 7 days, hypoxemia refractory to supplemental oxygen and a normal heart on film and echocardiogram fit this non-cardiogenic syndrome."],
   ["Cardiogenic pulmonary edema",
    "Cardiogenic pulmonary edema displays cardiomegaly, vascular engorgement and batwing perihilar opacities, and echocardiography is used to exclude it. Tell: her heart size and cardiac function are both normal, so the edema is not cardiogenic.", "ruled out by a stated finding"],
   ["Hypersensitivity pneumonitis",
    "Hypersensitivity pneumonitis follows inhaled organic dust, with symptoms hours after exposure and little change on early imaging. Tell: her trigger is sepsis, and her film shows new bilateral opacities with refractory hypoxemia.", "competing diagnosis"],
   ["Idiopathic pulmonary fibrosis",
    "Idiopathic pulmonary fibrosis develops insidiously over years, with clubbing and pleural-based honeycombing. Tell: her opacities appeared within 30 hours of sepsis, an acute course after a known insult, not a slow fibrosis.", "competing diagnosis"]],
  CS(33, 35, 72, 73), "manifestation", "diagnosis"),

V(ARDS, IO_A,
  "A 27-year-old man is admitted after an opioid overdose. About 24 hours later he develops profound dyspnea, tachypnea and crackles, with hypoxemia refractory to supplemental oxygen and new bilateral opacities. An echocardiogram shows normal cardiac function. Which complication of the overdose has he developed?",
  [["Acute respiratory distress syndrome",
    "Correct. Opioid overdose is one of the high-risk drug overdoses that can precipitate acute respiratory distress syndrome, along with aspirin, phenothiazines, tricyclic antidepressants and cocaine. Dyspnea 12-48 hours after the insult, refractory hypoxemia and new bilateral opacities with normal cardiac function fit."],
   ["Cardiogenic pulmonary edema",
    "Cardiogenic pulmonary edema shows cardiomegaly, vascular engorgement and batwing perihilar opacities. Tell: his echocardiogram shows normal cardiac function, which excludes the hydrostatic cardiac cause of his opacities.", "ruled out by a stated finding"],
   ["Hypersensitivity pneumonitis",
    "Hypersensitivity pneumonitis is a reaction to inhaled organic dust such as moldy hay or bird excreta. Tell: his trigger is an opioid overdose, a listed drug cause of acute respiratory distress syndrome, with no organic dust involved.", "competing diagnosis"],
   ["Diffuse alveolar hemorrhage",
    "Diffuse alveolar hemorrhage is a non-inflammatory intrapulmonary bleeding condition that requires clinical exclusion. Tell: nothing in his case describes bleeding, and his overdose is a recognized trigger of acute respiratory distress syndrome.", "competing diagnosis"]],
  CS(72, 73), "etiology", "complication"),

V(ARDS, IO_POP,
  "A 72-year-old woman develops profound dyspnea and new bilateral opacities 36 hours after multiple blood transfusions for a gastrointestinal bleed. She has a history of heart failure. What is the next step before acute respiratory distress syndrome can be diagnosed?",
  [["Echocardiogram",
    "Correct. The diagnosis requires respiratory failure not fully explained by heart failure or fluid overload, and echocardiographic assessment of cardiac function excludes hydrostatic cardiogenic pulmonary edema. Multiple transfusions are a recognized trigger, but her heart failure history makes that exclusion essential."],
   ["Routine pulmonary artery catheter",
    "Routine pulmonary artery catheters offer no clinical benefit in acute respiratory distress syndrome and are avoided. Tell: cardiac function is assessed with echocardiography, which answers the heart failure question without a catheter.", "adjacent fact"],
   ["Pulmonary function testing",
    "Pulmonary function testing shows the restrictive pattern of chronic interstitial lung disease. Tell: in an acutely hypoxemic patient after transfusion, the open question is cardiac function, which echocardiography answers.", "confused mechanism or drug class"],
   ["Serum antibodies to an inhaled agent",
    "Serum antibodies to an inhaled agent give the definitive diagnosis of hypersensitivity pneumonitis. Tell: her trigger is transfusion, not an organic dust, and the competing diagnosis to exclude is cardiogenic edema.", "competing diagnosis"]],
  CS(29, 69, 72, 73, 74), "differential", "next step"),

V(ARDS, IO_A,
  "A 63-year-old man with severe pancreatitis has new bilateral infiltrates and hypoxemia on hospital day 2. Which chest film finding favors acute respiratory distress syndrome over cardiogenic pulmonary edema?",
  [["Normal cardiac silhouette",
    "Correct. In acute respiratory distress syndrome the heart size is normal, with minimal or absent pleural effusions, while bilateral infiltrates rapidly progress to confluent opacities and air bronchograms appear in about 80% of cases. Cardiogenic pulmonary edema shows an enlarged heart instead."],
   ["Cardiomegaly",
    "Cardiomegaly is a feature of cardiogenic pulmonary edema, with vascular engorgement and batwing perihilar opacities. Tell: an enlarged heart points toward a cardiac cause, while acute respiratory distress syndrome keeps a normal silhouette.", "competing diagnosis"],
   ["Vascular engorgement",
    "Vascular engorgement belongs to cardiogenic pulmonary edema, along with cardiomegaly and batwing opacities. Tell: it favors the hydrostatic, cardiac diagnosis rather than acute respiratory distress syndrome after pancreatitis.", "competing diagnosis"],
   ["Batwing perihilar opacities",
    "Batwing perihilar opacities are described for cardiogenic pulmonary edema. Tell: acute respiratory distress syndrome shows bilateral infiltrates progressing to confluent opacities with a normal heart, after a trigger such as severe pancreatitis.", "competing diagnosis"]],
  CS(72, 73), "differential", "test"),

# ---------------------------------------------------------------- acute respiratory distress syndrome: oxygenation ratio
ORD(V(ARDS, IO_A,
  "A 46-year-old man with severe pancreatitis develops profound dyspnea on hospital day 2. His chest film shows new bilateral opacities not explained by effusion, atelectasis or nodules, and an echocardiogram shows normal cardiac function. His arterial oxygen pressure is 62 mm Hg on a fraction of inspired oxygen of 0.40. How is his oxygenation impairment classified?",
  [[MOD,
    "Correct. Divide arterial oxygen pressure by fraction of inspired oxygen: 62 / 0.40 = 155 mm Hg. That is under the 300 threshold and falls between 100 and 200, the moderate class. Severe pancreatitis is a systemic trigger, and his new opacities and normal heart complete the criteria."],
   [NOT_MET,
    "The oxygenation criterion is a ratio of arterial oxygen pressure to fraction of inspired oxygen under 300 mm Hg. Tell: 62 / 0.40 = 155, well under 300, so he meets the criterion and the question becomes which class.", "reversed direction or value"],
   [MILD,
    "Mild covers ratios of 200-300 mm Hg. Tell: his ratio, 62 / 0.40 = 155, is below 200, one class worse than mild; reading 62 against 300 without dividing by 0.40 is what makes mild look right.", "wrong stage or severity"],
   [SEV,
    "Severe is a ratio under 100 mm Hg, the class with the most impaired oxygenation. Tell: 62 / 0.40 = 155 sits above 100, so he has not reached the severe class; an arterial oxygen pressure of 62 alone is not the ratio.", "wrong stage or severity"]],
  CS(72, 73), "test finding", "classify"), [1, 2, 0, 3]),

ORD(V(ARDS, IO_A,
  "A 19-year-old man is resuscitated after a near-drowning. Within 24 hours he has refractory hypoxemia and new bilateral opacities on chest film with a normal heart size, and an echocardiogram shows normal cardiac function. On the ventilator his arterial oxygen pressure is 54 mm Hg on a fraction of inspired oxygen of 0.60. How is his oxygenation impairment classified?",
  [[SEV,
    "Correct. Divide arterial oxygen pressure by fraction of inspired oxygen: 54 / 0.60 = 90 mm Hg. A ratio under 100 is the severe class. Near-drowning is a direct pulmonary insult, and new bilateral opacities within a day with a normal heart complete the criteria."],
   [NOT_MET,
    "The criterion is met whenever the ratio of arterial oxygen pressure to fraction of inspired oxygen is under 300 mm Hg. Tell: 54 / 0.60 = 90, far below 300, so he clearly meets the oxygenation criterion and sits in the worst class.", "reversed direction or value"],
   [MILD,
    "Mild is a ratio of 200-300 mm Hg, the least impaired class that still meets the criterion. Tell: his ratio of 54 / 0.60 = 90 is less than half the bottom of the mild range, two classes worse than mild.", "wrong stage or severity"],
   [MOD,
    "Moderate covers 100-200 mm Hg. Tell: 54 / 0.60 = 90 falls just under 100, which crosses into the severe class; rounding up toward 100 is the mistake that makes moderate look right.", "wrong stage or severity"]],
  CS(72, 73), "test finding", "classify"), [1, 2, 3, 0]),

ORD(V(ARDS, IO_A,
  "A 34-year-old woman with a lung contusion from a motor vehicle crash develops new bilateral opacities on hospital day 3 that are not explained by effusion, atelectasis or nodules. An echocardiogram shows normal cardiac function. Her arterial oxygen pressure is 75 mm Hg on a fraction of inspired oxygen of 0.30. How is her oxygenation impairment classified?",
  [[MILD,
    "Correct. Divide arterial oxygen pressure by fraction of inspired oxygen: 75 / 0.30 = 250 mm Hg, which is under the 300 threshold and inside the 200-300 range of the mild class. Lung contusion is a direct pulmonary insult, and new bilateral opacities within 7 days with normal cardiac function complete the criteria."],
   [NOT_MET,
    "The criterion requires a ratio of arterial oxygen pressure to fraction of inspired oxygen under 300 mm Hg. Tell: 75 / 0.30 = 250, under 300, so she meets the criterion, in its mildest class.", "reversed direction or value"],
   [MOD,
    "Moderate is 100-200 mm Hg. Tell: her ratio, 75 / 0.30 = 250, sits above 200, in the mild band; an arterial oxygen pressure of 75 on its own says nothing until it is divided by the inspired fraction.", "wrong stage or severity"],
   [SEV,
    "Severe is a ratio under 100 mm Hg. Tell: 75 / 0.30 = 250 is far above that; a low arterial oxygen pressure alone does not make the class severe once the inspired fraction is divided in.", "wrong stage or severity"]],
  CS(72, 73), "test finding", "classify"), [1, 0, 2, 3]),

ORD(V(ARDS, IO_POP,
  "A 67-year-old man aspirated gastric contents during a seizure 2 days ago. His chest film shows new bilateral opacities, and an echocardiogram shows normal cardiac function. His arterial oxygen pressure is 98 mm Hg on a fraction of inspired oxygen of 0.28. How is his oxygenation impairment classified?",
  [[NOT_MET,
    "Correct. Divide arterial oxygen pressure by fraction of inspired oxygen: 98 / 0.28 = 350 mm Hg. The oxygenation criterion is a ratio under 300, so at 350 he does not meet it yet, even though aspiration of gastric contents is a direct insult and his opacities are new."],
   [MILD,
    "Mild covers ratios of 200-300 mm Hg, the least impaired class that still meets the criterion. Tell: his ratio, 98 / 0.28 = 350, is above 300, outside even the mildest class, so the oxygenation criterion is not yet met.", "wrong stage or severity"],
   [MOD,
    "Moderate is 100-200 mm Hg. Tell: 98 / 0.28 = 350, nowhere near 200; the inspired fraction of 0.28 is low, so dividing by it raises the ratio well above the diagnostic threshold.", "wrong stage or severity"],
   [SEV,
    "Severe is a ratio under 100 mm Hg. Tell: an arterial oxygen pressure of 98 is not the ratio; dividing by the fraction of inspired oxygen, 0.28, gives 350, above the 300 threshold.", "wrong stage or severity"]],
  CS(72, 73), "differential", "classify"), [0, 1, 2, 3]),

V(ARDS, IO_A,
  "A 52-year-old man with acute respiratory distress syndrome from diffuse pneumonia is on low tidal volume ventilation. His arterial oxygen pressure is 80 mm Hg on a fraction of inspired oxygen of 0.50, and an echocardiogram has excluded cardiogenic edema. Which intervention decreases mortality at his severity?",
  [["Early prone positioning",
    "Correct. His ratio is 80 / 0.50 = 160 mm Hg, moderate acute respiratory distress syndrome. Early prone positioning decreases mortality in moderate to severe cases, so he qualifies, alongside the low tidal volume ventilation he is already receiving."],
   ["High-frequency oscillatory ventilation",
    "High-frequency oscillatory ventilation provides no proven benefit and is listed among approaches to avoid. Tell: at a ratio of 80 / 0.50 = 160, the strategy that lowers mortality is prone positioning, not an oscillatory mode.", "confused mechanism or drug class"],
   ["Routine pulmonary artery catheter",
    "Routine pulmonary artery catheters offer no clinical benefit, and echocardiography has already assessed his heart. Tell: monitoring with a catheter does not lower mortality; early prone positioning does at his moderate severity.", "adjacent fact"],
   ["Transfusion to a higher hemoglobin",
    "Transfusion is given at a hemoglobin of 7 g/dL, and higher hemoglobin targets do not improve patient outcomes. Tell: raising hemoglobin is not the mortality-lowering step at a ratio of 160; prone positioning is.", "adjacent fact"]],
  CS(72, 73, 74), "first-line", "treatment"),

V(ARDS, IO_A,
  "A 41-year-old woman with acute respiratory distress syndrome after aspiration remains hypoxemic despite low tidal volume ventilation, careful positive end-expiratory pressure titration and early prone positioning. Her arterial oxygen pressure is 51 mm Hg on a fraction of inspired oxygen of 0.90. Which option is reserved for her situation?",
  [["Extracorporeal membrane oxygenation",
    "Correct. Her ratio is 51 / 0.90, about 57 mm Hg, well under 100, so she has severe acute respiratory distress syndrome that is refractory to ventilation strategy and prone positioning. Extracorporeal membrane oxygenation is the salvage option reserved for severe, refractory cases."],
   ["High-frequency oscillatory ventilation",
    "High-frequency oscillatory ventilation provides no proven benefit in acute respiratory distress syndrome. Tell: switching to an oscillatory mode is listed to avoid, while salvage for refractory severe disease is extracorporeal support.", "confused mechanism or drug class"],
   ["Inotropes for supranormal oxygen delivery",
    "Inotrope-driven excessive oxygen delivery causes potential harm, which is why supranormal targets are avoided. Tell: her refractory severe hypoxemia, with a ratio near 57, is a salvage problem, not a target for higher delivery.", "confused mechanism or drug class"],
   ["Liberal fluid resuscitation",
    "A conservative fluid protocol is preferred, because restrictive fluids increase ventilator-free days. Tell: liberal fluids run against that strategy, and refractory severe disease at a ratio near 57 calls for extracorporeal support.", "reversed direction or value"]],
  CS(72, 73, 74), "escalation", "referral"),

# ---------------------------------------------------------------- acute respiratory distress syndrome: management
V(ARDS, IO_A,
  "A 50-year-old woman with moderate acute respiratory distress syndrome from sepsis is on low tidal volume ventilation. A colleague proposes changing the ventilator strategy. Which change should be avoided?",
  [["High-frequency oscillatory ventilation",
    "Correct. High-frequency oscillatory ventilation provides no proven benefit in acute respiratory distress syndrome and is listed among the approaches to avoid. Her moderate disease is better served by low tidal volumes, careful positive end-expiratory pressure titration and early prone positioning."],
   ["Early prone positioning",
    "Early prone positioning decreases mortality in moderate to severe acute respiratory distress syndrome. Tell: she has moderate disease, so positioning is a step to take, not one to avoid, and it pairs with her low tidal volumes.", "reversed direction or value"],
   ["Careful positive end-expiratory pressure titration",
    "Positive end-expiratory pressure is titrated carefully to maintain an arterial oxygen tension above 60 mm Hg. Tell: careful titration is part of standard ventilation in this syndrome, not something to avoid.", "reversed direction or value"],
   ["Continued low tidal volumes",
    "Low tidal volume ventilation is the strategy behind the 30% baseline mortality figure for acute respiratory distress syndrome. Tell: it is the foundation of her ventilation, so continuing it is correct rather than a change to avoid.", "reversed direction or value"]],
  CS(72, 74), "avoid", "avoid"),

V(ARDS, IO_A,
  "A 61-year-old man with acute respiratory distress syndrome after severe trauma is stable on the ventilator, and an echocardiogram has already shown normal cardiac function. The team is planning his hemodynamic care. Which should be avoided?",
  [["Routine pulmonary artery catheter",
    "Correct. Routine pulmonary artery catheters offer no clinical benefit in acute respiratory distress syndrome and are avoided. Cardiac function is assessed by echocardiography to exclude hydrostatic cardiogenic edema, and he has already had one showing normal function."],
   ["Conservative fluid protocol",
    "A conservative fluid protocol, targeting a central venous pressure under 4 mm Hg, increases ventilator-free days. Tell: restrictive fluids are recommended in this syndrome, not avoided, and his stability allows them.", "reversed direction or value"],
   ["Transfusion at 7 g/dL",
    "Transfusing at a hemoglobin of 7 g/dL is the recommended threshold, because higher hemoglobin targets do not improve outcomes. Tell: this threshold is part of care, not a practice to avoid.", "reversed direction or value"],
   ["Sedatives and antipyretics",
    "Sedatives, analgesics and antipyretics reduce oxygen demand in acute respiratory distress syndrome and are used appropriately. Tell: they are part of care, while the routine catheter is what offers no clinical benefit.", "reversed direction or value"]],
  CS(73, 74), "avoid", "avoid"),

V(ARDS, IO_A,
  "A 57-year-old woman with acute respiratory distress syndrome from sepsis has a hemoglobin of 8.2 g/dL (normal 12.0-15.5) and no active bleeding. Her family asks that she be transfused to bring the value back to normal. Which should be avoided?",
  [["Transfusing to a normal hemoglobin",
    "Correct. In acute respiratory distress syndrome the transfusion threshold is a hemoglobin of 7 g/dL, and higher hemoglobin targets do not improve patient outcomes. Her 8.2 g/dL is low against the 12.0-15.5 range but above the threshold, so transfusing toward normal offers no outcome benefit."],
   ["Conservative fluid protocol",
    "A conservative fluid protocol increases ventilator-free days and shortens intensive care stays. Tell: it is recommended care in this syndrome, unlike chasing a normal hemoglobin with transfusion, which brings no outcome benefit.", "reversed direction or value"],
   ["Early prone positioning",
    "Early prone positioning decreases mortality in moderate to severe acute respiratory distress syndrome. Tell: it is a step to take when severity allows, not one to avoid, and it has nothing to do with her hemoglobin.", "reversed direction or value"],
   ["Transfusing if it falls to 7 g/dL",
    "A hemoglobin of 7 g/dL is the threshold at which to transfuse in this syndrome. Tell: transfusing at that level is recommended; it is transfusing up to normal that higher-target evidence fails to support.", "reversed direction or value"]],
  C(74), "avoid", "avoid"),

V(ARDS, IO_A,
  "A 49-year-old man with acute respiratory distress syndrome after severe pancreatitis is now hemodynamically stable on the ventilator. Which fluid strategy is preferred?",
  [["Conservative, restrictive fluids",
    "Correct. A conservative fluid protocol, targeting a central venous pressure under 4 mm Hg, is preferred, and restrictive fluids significantly increase ventilator-free days and shorten intensive care stays. His hemodynamic stability allows that restrictive approach."],
   ["Liberal fluids to support oxygen delivery",
    "Liberal fluids run against the conservative protocol that increases ventilator-free days. Tell: the preferred strategy is restrictive, with a low central venous pressure target, once the patient is hemodynamically stable like him.", "reversed direction or value"],
   ["Inotropes for supranormal oxygen delivery",
    "Inotrope-driven excessive oxygen delivery causes potential harm, so supranormal targets are avoided. Tell: the preferred hemodynamic strategy is restrictive fluids, not pushing oxygen delivery above normal with drugs.", "confused mechanism or drug class"],
   ["Fluids guided by a routine artery catheter",
    "Routine pulmonary artery catheters offer no clinical benefit in acute respiratory distress syndrome. Tell: fluids follow a conservative protocol, and cardiac function is assessed with echocardiography rather than a catheter.", "adjacent fact"]],
  C(74), "first-line", "treatment"),

V(ARDS, IO_A,
  "A 45-year-old man with moderate acute respiratory distress syndrome from pneumonia is febrile and agitated on the ventilator, and his team wants to lower his oxygen demand. Which measure fits?",
  [["Sedatives, analgesics and antipyretics",
    "Correct. Reducing oxygen demand in acute respiratory distress syndrome means using sedatives, analgesics and antipyretics appropriately. His fever and agitation both raise oxygen demand, which these measures address while ventilation and positioning support oxygenation."],
   ["Inotropes to raise oxygen delivery",
    "Inotrope-driven excessive oxygen delivery causes potential harm, which is why supranormal targets are avoided. Tell: the aim here is to lower his oxygen demand, not to push delivery higher with drugs.", "reversed direction or value"],
   ["Liberal fluids for his fever",
    "A conservative fluid protocol is preferred, because restrictive fluids increase ventilator-free days. Tell: fever is treated with antipyretics as part of lowering oxygen demand, not with extra fluid, which runs against the protocol.", "common lay belief"],
   ["High-frequency oscillatory ventilation",
    "High-frequency oscillatory ventilation provides no proven benefit and is listed to avoid. Tell: his agitation and fever call for sedation, analgesia and antipyretics, which reduce oxygen demand directly.", "confused mechanism or drug class"]],
  C(74), "agent/regimen", "treatment"),

# ---------------------------------------------------------------- acute respiratory distress syndrome: prognosis and recovery
V(ARDS, IO_A,
  "A 58-year-old man with end-stage liver disease develops acute respiratory distress syndrome. His family asks how his underlying condition affects his outlook. Which mortality figure fits his etiology?",
  [["About 80%",
    "Correct. Etiology drives survival in acute respiratory distress syndrome: mortality spans about 20% after trauma to about 80% in end-stage liver disease, against a 30% overall baseline with low tidal volume strategies. His liver disease places him at the high end of that range."],
   ["About 20%",
    "About 20% is the mortality at the favorable end of the range, after trauma. Tell: end-stage liver disease sits at the opposite end, near 80%, so this figure badly understates his risk.", "reversed direction or value"],
   ["About 30%",
    "About 30% is the overall baseline mortality in this syndrome with low tidal volume ventilation strategies. Tell: his etiology, end-stage liver disease, moves him well above the average to about 80%.", "adjacent fact"],
   ["About 50%",
    "Half is not the figure given for liver failure, which sits at the top of the 20-80% range set by etiology. Tell: end-stage liver disease carries about 80% mortality, the highest named.", "wrong stage or severity"]],
  CS(72, 74), "prognosis", "complication"),

V(ARDS, IO_POP,
  "A 55-year-old woman is leaving the hospital after acute respiratory distress syndrome from pneumonia. She asks how long her lung function will take to recover. Which answer is accurate?",
  [["About 6 to 12 months",
    "Correct. Lung function generally recovers over 6 to 12 months after acute respiratory distress syndrome, though functional deficits often remain, with residual diffusion deficits persisting. Physical sequelae after intensive care, such as muscle wasting, weakness and fatigue, also need attention."],
   ["About 1 month",
    "One month is too soon: pulmonary function improves over 6 to 12 months after this syndrome. Tell: recovery is measured in most of a year, not weeks, and some functional deficits often remain even then.", "reversed direction or value"],
   ["About 3 months",
    "Three months falls short of the usual course, which runs 6 to 12 months. Tell: she should expect lung function to keep improving well beyond 3 months, while some deficits may persist.", "reversed direction or value"],
   ["About 36 months",
    "Three years overshoots the typical recovery window of 6 to 12 months after acute respiratory distress syndrome. Tell: lasting deficits can remain, but the main recovery of lung function happens within about a year.", "reversed direction or value"]],
  CS(72, 74), "prognosis", "education"),

V(ARDS, IO_POP,
  "A 66-year-old man is recovering after 3 weeks in the intensive care unit for acute respiratory distress syndrome. He has muscle wasting, weakness and persistent fatigue. Which referral addresses these problems?",
  [["Physical rehabilitation",
    "Correct. Long-term recovery after acute respiratory distress syndrome includes treating physical sequelae: post-intensive care muscle wasting, weakness and persistent fatigue. Rehabilitation addresses them while his lung function continues to improve over 6 to 12 months."],
   ["Lung transplant evaluation",
    "Lung transplant is listed for severe coal workers' pneumoconiosis and hypersensitivity pneumonitis. Tell: his problems are muscle wasting and weakness after intensive care, while his lungs are still recovering on their usual timeline.", "wrong stage or severity"],
   ["Extracorporeal membrane oxygenation",
    "Extracorporeal membrane oxygenation is a salvage option for severe, refractory disease during the acute illness. Tell: he is in recovery, and his problems are physical sequelae of intensive care, not refractory hypoxemia.", "wrong stage or severity"],
   ["Yearly ophthalmologic evaluation",
    "Yearly ophthalmologic evaluation is sarcoidosis follow-up for ocular inflammation. Tell: his needs after intensive care are muscle strength and fatigue, which rehabilitation addresses, not eye monitoring.", "adjacent fact"]],
  CS(48, 54, 71, 74), "referral", "referral"),
]
