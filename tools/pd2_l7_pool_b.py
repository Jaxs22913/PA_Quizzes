# -*- coding: utf-8 -*-
# Physical Diagnosis 2, Lecture 7 -- The Advanced Hematological Physical Examination
# (Matthew Ward, DMSc, MBA, PA-C), delivered 2026-11-12 -- pool B.
#
# The other organ systems (slides 36-53): cardiovascular findings, bone tenderness and
# clubbing, pulmonary findings, the gastrointestinal examination and stool blood testing,
# the signs of internal bleeding, the B12 neurologic examination; then the anemia or
# bleeding emergency and the interpretation of the findings (slides 54-56).
# Same rules and Q() shape as pool A (see its header).
from pd2_l7_pool_a import Q, c, IO_A, IO_B, IO_C, IO_D

POOL_B = [

# ======================================================== cardiovascular findings (slides 36-37)
Q("Cardiovascular findings", IO_C, "manifestation",
  "Which cardiovascular finding is expected in a patient with significant anemia?",
  ("Tachycardia with a hyperdynamic circulation",
   "Correct. Anemia drives tachycardia and a hyperdynamic circulation, with possible bounding pulses, "
   "a prominent precordial impulse and a systolic flow murmur."),
  [("Bradycardia with weak, thready pulses",
    "That reverses the picture. Anemia speeds the heart and makes the circulation hyperdynamic, with "
    "possible bounding pulses.",
    "reversed direction or value"),
   ("A loud diastolic rumble at the apex",
    "The murmur anemia may cause is a SYSTOLIC flow murmur, not a diastolic rumble.",
    "reversed direction or value"),
   ("A pericardial friction rub",
    "A friction rub is not among the anemia findings. Expect tachycardia, a hyperdynamic circulation "
    "and possibly a systolic flow murmur.",
    "competing diagnosis")],
  c(37)),

Q("Cardiovascular findings", IO_C, "manifestation",
  "Which murmur may be heard in a patient with anemia?",
  ("A systolic flow murmur",
   "Correct. The hyperdynamic circulation of anemia can produce a systolic flow murmur, along with "
   "tachycardia, bounding pulses and a prominent precordial impulse."),
  [("A diastolic decrescendo murmur",
    "Anemia's murmur is systolic, from flow through a hyperdynamic circulation, not a diastolic one.",
    "reversed direction or value"),
   ("A continuous machinery murmur",
    "A continuous murmur is not among the anemia findings. The possible murmur is a systolic flow "
    "murmur.",
    "competing diagnosis"),
   ("An opening snap with a rumble",
    "An opening snap and rumble are not anemia findings. The possible murmur is a systolic flow murmur.",
    "competing diagnosis")],
  c(37)),

Q("Cardiovascular findings", IO_C, "manifestation",
  "Which pulse finding may accompany anemia?",
  ("Bounding pulses",
   "Correct. A hyperdynamic circulation may give bounding pulses and a prominent precordial impulse, "
   "with tachycardia."),
  [("Absent distal pulses",
    "Absent pulses suggest arterial occlusion, not anemia. Anemia's hyperdynamic circulation may give "
    "bounding pulses.",
    "reversed direction or value"),
   ("A slow, regular pulse",
    "Anemia causes tachycardia, not a slow pulse; the pulses may be bounding.",
    "reversed direction or value"),
   ("Pulsus paradoxus",
    "Pulsus paradoxus is not an anemia finding. The expected pulses are fast and possibly bounding.",
    "competing diagnosis")],
  c(37)),

Q("Cardiovascular findings", IO_D, "escalation",
  "In which anemic patient should heart failure specifically be assessed for?",
  ("Severe or poorly tolerated anemia",
   "Correct. Heart failure is assessed in severe or poorly tolerated anemia, and the findings are "
   "interpreted against the symptoms and any underlying heart disease."),
  [("A patient with mild anemia",
    "Mild anemia does not call for it. The heart failure assessment is for severe or poorly "
    "tolerated anemia.",
    "wrong stage or severity"),
   ("A patient under age 40",
    "Age is not the trigger, and older patients with heart disease tolerate anemia worse. Severe or "
    "poorly tolerated anemia is.",
    "reversed direction or value"),
   ("A patient with koilonychia",
    "Nail findings say nothing about severity. Heart failure is assessed in severe or poorly tolerated "
    "anemia.",
    "adjacent fact")],
  c(37)),

Q("Cardiovascular findings", IO_D, "differential",
  "How should cardiovascular findings be interpreted in an anemic patient?",
  ("Against symptoms and heart disease",
   "Correct. Interpretation weighs the symptoms and underlying heart disease: the same anemia is "
   "tolerated worse when cardiopulmonary reserve is poor."),
  [("Against the patient's hemoglobin alone",
    "The hemoglobin alone does not decide it; symptoms and underlying heart disease do.",
    "common lay belief"),
   ("As caused by the anemia itself",
    "A finding may come from underlying heart disease rather than anemia; interpret it against both.",
    "reversed direction or value"),
   ("As unrelated to the anemia",
    "Tachycardia, a hyperdynamic circulation and a flow murmur are expected anemia findings, read "
    "against the symptoms and heart disease.",
    "reversed direction or value")],
  c(37, 8)),

# ======================================================== bone tenderness and clubbing (slides 38-42)
Q("Bone tenderness", IO_C, "differential",
  "What may sternal or other bone tenderness suggest in an anemic patient?",
  ("Possible marrow disease",
   "Correct. Sternal or other bone tenderness suggests possible marrow disease but is "
   "nonspecific, so other causes must be considered."),
  [("Iron deficiency, specifically",
    "Iron deficiency's clues are spoon nails and hair shedding, not bone tenderness. Bone tenderness "
    "points to possible marrow disease.",
    "competing diagnosis"),
   ("Hemolysis, specifically",
    "Hemolysis is suggested by jaundice and icterus. Bone tenderness suggests possible marrow disease.",
    "competing diagnosis"),
   ("A normal finding in adults",
    "Bone tenderness is not normal here: it raises possible marrow disease, though it is nonspecific.",
    "reversed direction or value")],
  c(38)),

Q("Clubbing", IO_C, "differential",
  "An anemic patient has digital clubbing. What does this suggest?",
  ("Another underlying systemic disorder",
   "Correct. Clubbing is atypical for uncomplicated anemia, so it points to an underlying "
   "cardiopulmonary, gastrointestinal or other systemic disorder."),
  [("Uncomplicated iron deficiency anemia",
    "Clubbing is atypical for uncomplicated anemia. Its presence points to another disorder.",
    "reversed direction or value"),
   ("Uncomplicated B12 deficiency anemia",
    "B12 deficiency shows in the nervous system, and clubbing is atypical for uncomplicated anemia. "
    "Look for an underlying disorder.",
    "competing diagnosis"),
   ("Severe anemia that needs transfusion",
    "Clubbing does not grade anemia. It is atypical for uncomplicated anemia and suggests an "
    "underlying disorder.",
    "wrong stage or severity")],
  c(38)),

Q("Clubbing", IO_C, "manifestation",
  "Which three measures assess clubbing?",
  ("Schamroth's window, nail-fold angle, depth ratio",
   "Correct. Clubbing is assessed with Schamroth's window, the nail-fold profile angle and the "
   "phalangeal depth ratio."),
  [("Romberg test, vibration sense, joint-position sense",
    "Those belong to the neurologic examination for B12 deficiency. Clubbing uses Schamroth's window, "
    "the nail-fold angle and the phalangeal depth ratio.",
    "adjacent fact"),
   ("Capillary refill, skin turgor, nail color",
    "These are perfusion and hydration checks. Clubbing is measured by Schamroth's window, the "
    "nail-fold angle and the phalangeal depth ratio.",
    "adjacent fact"),
   ("Grey Turner sign, Cullen sign, splenomegaly",
    "Those are abdominal findings. Clubbing uses Schamroth's window, the nail-fold angle and the "
    "phalangeal depth ratio.",
    "adjacent fact")],
  c(38)),

Q("Clubbing", IO_C, "test finding",
  "Which nail-fold profile angle indicates clubbing?",
  ("Greater than 180 degrees",
   "Correct. A nail-fold profile angle under 180 degrees is normal; over 180 degrees indicates "
   "clubbing."),
  [("Less than 160 degrees",
    "An angle well under 180 degrees is normal. Clubbing is an angle greater than 180 degrees.",
    "reversed direction or value"),
   ("Less than 180 degrees",
    "Under 180 degrees is the NORMAL angle. Clubbing pushes it past 180 degrees.",
    "reversed direction or value"),
   ("Exactly 90 degrees",
    "A right angle is not the cut-off. Normal is under 180 degrees; clubbing is over 180 degrees.",
    "reversed direction or value")],
  c(40)),

Q("Clubbing", IO_C, "test finding",
  "When the backs of matching fingers are held together, what indicates clubbing?",
  ("Loss of the diamond-shaped window",
   "Correct. In Schamroth's window test a normal pair of fingers leaves a small diamond-shaped "
   "window between the nails; in clubbing the window is gone."),
  [("A larger diamond-shaped window than usual",
    "Clubbing does not enlarge the window; it obliterates it. A visible window is normal.",
    "reversed direction or value"),
   ("Pain when the nails are pressed together",
    "Pain is not the sign. Schamroth's sign is the loss of the window between the nails.",
    "adjacent fact"),
   ("Pale nail beds while pressed",
    "Nail bed color is a pallor finding. Clubbing is shown by the lost diamond-shaped window.",
    "adjacent fact")],
  c(41, 38)),

Q("Clubbing", IO_C, "test finding",
  "In clubbing, how does the phalangeal depth ratio change?",
  ("Depth at the nail base exceeds depth at the end joint",
   "Correct. The phalangeal depth ratio compares the distal phalangeal depth at the nail base with the "
   "interphalangeal depth; in clubbing the nail-base depth becomes the greater."),
  [("Depth at the end joint exceeds depth at the nail base",
    "That is the NORMAL relationship. In clubbing the depth at the nail base is the greater.",
    "reversed direction or value"),
   ("The two depths shrink equally",
    "Clubbing enlarges the nail-base depth; the ratio rises rather than staying even.",
    "reversed direction or value"),
   ("The nail becomes thin and spoon-shaped",
    "A thin, spoon-shaped nail is koilonychia, an iron clue. Clubbing makes the nail-base depth the "
    "greater.",
    "competing diagnosis")],
  c(42, 38)),

# ======================================================== pulmonary findings (slide 43)
Q("Pulmonary findings", IO_C, "test finding",
  "What pulse oximetry reading is typical in an anemic patient with dyspnea and no lung disease?",
  ("Normal, despite reduced oxygen content",
   "Correct. Pulse oximetry is normal despite reduced oxygen content: lower hemoglobin lowers the "
   "oxygen-carrying capacity, not the saturation of the hemoglobin present."),
  [("Low, matching the fall in hemoglobin",
    "Oximetry does not fall with the hemoglobin. It stays normal although oxygen content is reduced.",
    "reversed direction or value"),
   ("Low during exertion",
    "Exertional dyspnea is common, but oximetry stays normal in anemia despite reduced oxygen content.",
    "wrong stage or severity"),
   ("Unreadable because of pallor",
    "Pallor does not stop the reading; oximetry is normal despite reduced oxygen content.",
    "common lay belief")],
  c(43)),

Q("Pulmonary findings", IO_C, "manifestation",
  "Why do anemic patients become short of breath?",
  ("Less oxygen-carrying capacity",
   "Correct. With clinically significant anemia, reduced hemoglobin lowers oxygen-carrying capacity, "
   "causing dyspnea and tachypnea, even though pulse oximetry stays normal."),
  [("Hemoglobin saturation falls in the lungs",
    "Saturation is preserved: oximetry is normal. The problem is less hemoglobin to carry oxygen.",
    "confused mechanism or drug class"),
   ("Airway narrowing from the anemia",
    "Anemia does not narrow the airways. Reduced hemoglobin lowers oxygen-carrying capacity.",
    "confused mechanism or drug class"),
   ("Fluid filling the alveoli",
    "Heart failure may coexist in severe anemia, but the usual cause of dyspnea is reduced "
    "oxygen-carrying capacity.",
    "wrong stage or severity")],
  c(43)),

Q("Pulmonary findings", IO_C, "differential",
  "An anemic patient has increased respiratory effort. What else should be considered?",
  ("Lung disease or heart failure",
   "Correct. Respiratory effort is assessed for coexisting pulmonary disease or heart failure, "
   "which add to the dyspnea and tachypnea of significant anemia."),
  [("Anemia alone explains the effort",
    "Anemia causes dyspnea and tachypnea, but coexisting pulmonary disease or heart failure must be "
    "considered.",
    "common lay belief"),
   ("A falsely low pulse oximetry reading",
    "Oximetry is typically normal in anemia. Increased effort raises coexisting pulmonary disease or "
    "heart failure.",
    "reversed direction or value"),
   ("Iron deficiency from the effort",
    "Effort does not cause iron deficiency. Consider coexisting pulmonary disease or heart failure.",
    "confused mechanism or drug class")],
  c(43)),

# ======================================================== gastrointestinal examination (slides 44-46)
Q("Gastrointestinal examination", IO_C, "differential",
  "Which is a listed cause of splenomegaly in a patient with anemia?",
  ("Hemolysis",
   "Correct. Splenomegaly may come from hemolysis, infection, portal hypertension or hematologic "
   "malignancy."),
  [("Iron deficiency",
    "Iron deficiency's clues are spoon nails and hair shedding, not an enlarged spleen. "
    "Hemolysis is a listed cause.",
    "competing diagnosis"),
   ("Heavy menstrual bleeding",
    "Blood loss does not enlarge the spleen. Hemolysis, infection, portal hypertension and "
    "hematologic malignancy do.",
    "confused mechanism or drug class"),
   ("Vitamin B12 deficiency",
    "B12 deficiency is not on the splenomegaly list; hemolysis, infection, portal hypertension and "
    "hematologic malignancy are.",
    "competing diagnosis")],
  c(46)),

Q("Stool blood testing", IO_C, "test finding",
  "An anemic patient's stool blood test is negative. What can be concluded?",
  ("Gastrointestinal bleeding is still possible",
   "Correct. A negative stool blood test does not exclude gastrointestinal bleeding; further "
   "evaluation is guided by the history, examination and type of anemia."),
  [("Gastrointestinal bleeding is excluded",
    "A negative test cannot rule it out: gastrointestinal bleeding is still possible.",
    "reversed direction or value"),
   ("The anemia must be from hemolysis",
    "A negative stool test does not establish a mechanism. Bleeding is still possible.",
    "confused mechanism or drug class"),
   ("Further evaluation can stop",
    "Further evaluation still depends on the history, examination and type of anemia; bleeding "
    "remains possible.",
    "wrong stage or severity")],
  c(46)),

Q("Stool blood testing", IO_C, "test finding",
  "An anemic patient's stool blood test is positive. What does the result establish?",
  ("Neither source nor cause",
   "Correct. A positive stool blood test leaves the source and the cause of the anemia undetermined; "
   "further evaluation follows the history, examination and type of anemia."),
  [("A colon cancer as the cause",
    "A positive test names no lesion: source and cause remain undetermined.",
    "wrong stage or severity"),
   ("The bleeding is from the stomach",
    "A positive result does not locate the bleeding: the source stays undetermined, as does the cause of the anemia.",
    "wrong stage or severity"),
   ("That the bleeding explains the anemia",
    "Even a positive test leaves the cause of the anemia undetermined.",
    "common lay belief")],
  c(46)),

Q("Gastrointestinal examination", IO_C, "manifestation",
  "When is a digital rectal examination done in the hematologic examination?",
  ("When clinically indicated",
   "Correct. A digital rectal examination is performed when clinically indicated, as part of the "
   "gastrointestinal examination, which also checks for tenderness, masses, hepatomegaly, ascites "
   "and splenomegaly."),
  [("It is replaced by stool tests",
    "Stool tests do not replace it, and a negative one does not exclude bleeding. It is done when "
    "clinically indicated.",
    "reversed direction or value"),
   ("In each patient, whatever the history",
    "It is not routine for everyone; it is done when clinically indicated.",
    "wrong stage or severity"),
   ("After a positive stool test",
    "It is not limited to that; it is performed when clinically indicated.",
    "wrong stage or severity")],
  c(46)),

# ======================================================== signs of internal bleeding (slides 47-49)
Q("Internal bleeding signs", IO_C, "manifestation",
  "What is Cullen sign?",
  ("Periumbilical ecchymosis",
   "Correct. Cullen sign is periumbilical ecchymosis, a sign of internal bleeding. Grey Turner sign "
   "is flank ecchymosis."),
  [("Flank ecchymosis",
    "Flank ecchymosis is Grey Turner sign. Cullen sign is around the umbilicus.",
    "adjacent fact"),
   ("Palatal petechiae",
    "Palatal petechiae are a mucosal bleeding finding in the mouth. Cullen sign is periumbilical "
    "ecchymosis.",
    "adjacent fact"),
   ("Yellow sclerae",
    "Yellow sclerae are scleral icterus. Cullen sign is periumbilical ecchymosis.",
    "adjacent fact")],
  c(47, 48)),

Q("Internal bleeding signs", IO_C, "manifestation",
  "What is Grey Turner sign, and what does it suggest?",
  ("Flank ecchymosis; internal bleeding",
   "Correct. Grey Turner sign is flank ecchymosis from retroperitoneal or intra-abdominal bleeding; "
   "it is also possible in severe pancreatitis."),
  [("Periumbilical ecchymosis; internal bleeding",
    "That describes Cullen sign. Grey Turner sign is flank ecchymosis.",
    "adjacent fact"),
   ("Flank pain; kidney stones",
    "Grey Turner sign is not pain; it is flank ECCHYMOSIS from retroperitoneal or intra-abdominal "
    "bleeding.",
    "common lay belief"),
   ("Spoon nails; iron deficiency",
    "Spoon nails are koilonychia. Grey Turner sign is flank ecchymosis.",
    "adjacent fact")],
  c(47, 49)),

Q("Internal bleeding signs", IO_C, "manifestation",
  "Which sign is shown on this patient's abdomen?",
  ("Cullen sign",
   "Correct. The bruise lies beside the umbilicus: periumbilical ecchymosis, Cullen sign, from internal "
   "bleeding."),
  [("Grey Turner sign",
    "Grey Turner sign is ecchymosis of the FLANK. This bruise is at the umbilicus.",
    "competing diagnosis"),
   ("Purpura",
    "Purpura are nonblanching skin lesions, often many. This is a single periumbilical ecchymosis.",
    "competing diagnosis"),
   ("Petechiae",
    "Petechiae are pinpoint. This is a large periumbilical bruise.",
    "competing diagnosis")],
  c(48, 47), img="l7-fig-05.jpg",
  alt="A patient's lower abdomen with a dark purple bruise around the navel."),

Q("Internal bleeding signs", IO_C, "manifestation",
  "Which sign is shown on this patient's side?",
  ("Grey Turner sign",
   "Correct. Bruising across the flank is Grey Turner sign: flank ecchymosis from retroperitoneal or "
   "intra-abdominal bleeding."),
  [("Cullen sign",
    "Cullen sign is around the umbilicus. Bruising of the flank is Grey Turner sign.",
    "competing diagnosis"),
   ("Petechiae",
    "Petechiae are pinpoint spots. These are larger bruises across the flank.",
    "competing diagnosis"),
   ("Jaundice",
    "Jaundice is a diffuse yellow color of the skin. These are purple bruises across the flank: Grey Turner sign.",
    "competing diagnosis")],
  c(49, 47), img="l7-fig-06.jpg",
  alt="A patient lying on one side with several purple bruises across the flank."),

Q("Internal bleeding signs", IO_C, "test finding",
  "A patient with suspected internal bleeding has no Cullen or Grey Turner sign. What does this mean?",
  ("Significant bleeding is still possible",
   "Correct. Both signs are uncommon and may appear late, so their absence does not exclude "
   "significant bleeding."),
  [("Significant bleeding is excluded",
    "These signs are uncommon and possibly delayed; absent signs do not exclude bleeding.",
    "reversed direction or value"),
   ("The bleeding must be menstrual",
    "Their absence does not locate the bleeding; significant internal bleeding is still possible.",
    "confused mechanism or drug class"),
   ("Pancreatitis is excluded",
    "Absence rules nothing out: the signs are uncommon and may be delayed.",
    "reversed direction or value")],
  c(47)),

Q("Internal bleeding signs", IO_C, "differential",
  "Besides internal bleeding, which condition may produce Cullen or Grey Turner sign?",
  ("Severe pancreatitis",
   "Correct. Both signs may come from severe pancreatitis or another serious abdominal condition, not "
   "only from internal bleeding."),
  [("Iron deficiency",
    "Iron deficiency does not cause ecchymosis of the abdominal wall. Severe pancreatitis can.",
    "competing diagnosis"),
   ("Irritable bowel syndrome",
    "Irritable bowel syndrome causes no bruising. Severe pancreatitis is the listed alternative.",
    "competing diagnosis"),
   ("B12 deficiency",
    "B12 deficiency is neurologic. Severe pancreatitis is the alternative cause of these signs.",
    "competing diagnosis")],
  c(47)),

Q("Emergency", IO_D, "escalation",
  "In an anemia or bleeding emergency, how are oxygen and transfusion given?",
  ("According to the clinical situation",
   "Correct. Oxygen and transfusion are given according to the clinical situation, alongside "
   "immediate escalation: stabilization, bleeding control and resuscitation."),
  [("To every anemic patient at arrival",
    "They are not given to everyone; oxygen and transfusion follow the clinical situation, after "
    "vital signs, mental status, perfusion and ongoing loss are assessed.",
    "wrong stage or severity"),
   ("Once the hemoglobin has fallen",
    "Waiting for the hemoglobin is unsafe, since instability can precede its fall. Oxygen and "
    "transfusion follow the clinical situation.",
    "reversed direction or value"),
   ("After the history is complete",
    "The emergency calls for immediate escalation, not a finished history first. Oxygen and "
    "transfusion are given according to the clinical situation.",
    "wrong stage or severity")],
  c(54)),

Q("Internal bleeding signs", IO_C, "prognosis",
  "How do Cullen and Grey Turner signs typically behave?",
  ("Uncommon, and may appear late",
   "Correct. Both signs are uncommon findings with a possible delayed appearance, so their absence "
   "does not exclude significant bleeding."),
  [("Common, and appear within minutes",
    "They are uncommon and may be delayed, not common and immediate. Absent signs do not exclude "
    "significant bleeding.",
    "reversed direction or value"),
   ("Present in every internal bleed",
    "They are uncommon findings: significant bleeding is still possible without them.",
    "reversed direction or value"),
   ("Seen only with minor bleeding",
    "They are signs of internal bleeding (or severe pancreatitis), not of minor bleeding; they are "
    "uncommon and may appear late.",
    "reversed direction or value")],
  c(47)),

# ======================================================== B12 neurologic findings (slides 50-53)
Q("B12 neurologic findings", IO_C, "manifestation",
  "A patient has difficulty walking in the dark and reduced vibration sense in the feet. Which deficiency is suggested?",
  ("Vitamin B12 deficiency",
   "Correct. Sensory ataxia, impaired balance, difficulty walking in the dark and reduced vibration "
   "and joint-position sense are the neurologic findings of B12 deficiency."),
  [("Iron deficiency",
    "Iron deficiency is linked to spoon nails and hair shedding, not sensory ataxia. These are B12 "
    "findings.",
    "competing diagnosis"),
   ("Folate deficiency",
    "Folate shares glossitis and cheilitis with B12, but the neurologic findings here are listed for "
    "B12 deficiency.",
    "competing diagnosis"),
   ("Lead poisoning",
    "Lead is not listed with these findings; difficulty walking in the dark and reduced vibration "
    "sense are the B12 ones.",
    "competing diagnosis")],
  c(50)),

Q("B12 neurologic findings", IO_C, "manifestation",
  "Which spinal cord structures are affected in B12 deficiency?",
  ("Posterior columns, corticospinal tracts",
   "Correct. B12 deficiency affects the posterior columns (impaired vibration and position sense) and "
   "the lateral corticospinal tracts (possible spasticity and hyperreflexia)."),
  [("Anterior horns and spinothalamic tracts",
    "Neither the anterior horns nor the spinothalamic tracts are the named sites. B12 deficiency "
    "affects the posterior columns and lateral corticospinal tracts.",
    "adjacent fact"),
   ("Cerebellum and basal ganglia",
    "These are not spinal cord structures. The ataxia of B12 deficiency is SENSORY, from the posterior "
    "columns, with the lateral corticospinal tracts also affected.",
    "confused mechanism or drug class"),
   ("Spinothalamic and spinocerebellar tracts",
    "These are not the tracts named. B12 deficiency involves the posterior columns and the lateral "
    "corticospinal tracts.",
    "adjacent fact")],
  c(51)),

Q("B12 neurologic findings", IO_C, "manifestation",
  "Damage to the posterior columns in B12 deficiency impairs which sensations?",
  ("Vibration and position",
   "Correct. Posterior column involvement impairs vibration and position sense; corticospinal tract "
   "involvement may add spasticity and hyperreflexia."),
  [("Pain and temperature",
    "Pain and temperature are not the posterior column modalities named. Vibration and position "
    "sense are.",
    "adjacent fact"),
   ("Taste and smell",
    "Taste and smell are cranial nerve senses. The posterior columns carry vibration and position "
    "sense.",
    "adjacent fact"),
   ("Sight and hearing",
    "Visual changes are possible in B12 deficiency, but they do not come from the posterior columns, "
    "which carry vibration and position sense.",
    "adjacent fact")],
  c(51)),

Q("B12 neurologic findings", IO_C, "manifestation",
  "Which motor finding may result from corticospinal tract involvement in B12 deficiency?",
  ("Spasticity and hyperreflexia",
   "Correct. Lateral corticospinal tract involvement may cause spasticity and hyperreflexia; "
   "peripheral neuropathy can coexist, so reflexes vary."),
  [("Flaccid weakness with fasciculations",
    "That is not the listed corticospinal picture. Corticospinal involvement gives spasticity and "
    "hyperreflexia.",
    "reversed direction or value"),
   ("Resting tremor and rigidity",
    "Those are not B12 findings here. Corticospinal involvement may cause spasticity and "
    "hyperreflexia.",
    "competing diagnosis"),
   ("Loss of vibration sense",
    "Lost vibration sense comes from the POSTERIOR COLUMNS. The corticospinal tracts give spasticity "
    "and hyperreflexia.",
    "adjacent fact")],
  c(51)),

Q("B12 neurologic findings", IO_D, "differential",
  "Can the neurologic findings of B12 deficiency occur without anemia?",
  ("Yes, even without anemia",
   "Correct. Neurologic findings of B12 deficiency can occur without anemia or macrocytosis, so a "
   "normal blood count does not rule out the deficiency in a patient with these findings."),
  [("No, anemia comes first",
    "Neurologic findings can appear without anemia or macrocytosis.",
    "reversed direction or value"),
   ("With severe anemia, not mild",
    "Severity is not required; findings can occur with no anemia at all.",
    "wrong stage or severity"),
   ("When macrocytosis is present",
    "They can occur without macrocytosis as well as without anemia.",
    "reversed direction or value")],
  c(50)),

Q("B12 neurologic findings", IO_C, "manifestation",
  "Which non-sensory changes are possible in B12 deficiency?",
  ("Cognitive or psychiatric changes",
   "Correct. Beyond paresthesias, lost vibration and position sense and sensory ataxia, B12 "
   "deficiency may cause cognitive, psychiatric or visual changes."),
  [("Hearing loss and tinnitus",
    "Hearing changes are not listed. Cognitive, psychiatric and visual changes are possible.",
    "adjacent fact"),
   ("Hair shedding and spoon nails",
    "These are iron deficiency clues. B12 deficiency may cause cognitive, psychiatric or visual "
    "changes.",
    "competing diagnosis"),
   ("Seizures and headache",
    "Not on the list. B12 deficiency may cause cognitive, psychiatric or visual changes.",
    "adjacent fact")],
  c(50)),

Q("Neurologic examination", IO_B, "manifestation",
  "Which element belongs to the focused neurologic examination of an anemic patient?",
  ("Distal vibration and joint-position sense",
   "Correct. The focused neurologic examination covers gait and balance, distal vibration and "
   "joint-position sense, strength and deep-tendon reflexes, and Romberg testing."),
  [("Visual acuity with a Snellen chart",
    "Visual acuity is not in it. Test distal vibration and joint-position sense, gait, strength, "
    "reflexes and Romberg.",
    "adjacent fact"),
   ("Cranial nerve smell testing",
    "Smell is not tested. The focused examination includes distal vibration and joint-position sense.",
    "adjacent fact"),
   ("Two-point discrimination on the face",
    "Not part of it. Test distal vibration and joint-position sense, gait and balance, strength, "
    "reflexes and Romberg.",
    "adjacent fact")],
  c(52)),

Q("Neurologic examination", IO_B, "test finding",
  "During Romberg testing, a patient becomes much more unsteady when the eyes close. What does this suggest?",
  ("Impaired proprioception",
   "Correct. Greater instability with eye closure suggests impaired proprioception, as in posterior "
   "column involvement from B12 deficiency."),
  [("A normal response",
    "A marked increase in unsteadiness with the eyes closed is the abnormal finding: impaired "
    "proprioception.",
    "reversed direction or value"),
   ("Iron deficiency",
    "Romberg tests proprioception, not a blood-cell cause: greater instability with eye closure "
    "suggests impaired proprioception, not iron deficiency.",
    "competing diagnosis"),
   ("Hemolysis",
    "Romberg does not test for hemolysis. Greater instability with eye closure suggests impaired "
    "proprioception.",
    "competing diagnosis")],
  c(52)),

Q("Neurologic examination", IO_B, "avoid",
  "What precaution is required during Romberg testing?",
  ("Protection against falling",
   "Correct. Romberg testing is done with protection against falling: the examiner stands ready, "
   "since a patient with impaired proprioception may sway or fall with eyes closed."),
  [("Keeping the patient's eyes open",
    "Eye closure is the test itself; greater instability with eyes closed is the finding. Guard "
    "against falling.",
    "reversed direction or value"),
   ("Testing while seated",
    "Romberg is done standing; the precaution is protection against falling.",
    "reversed direction or value"),
   ("Applying a tuning fork first",
    "Vibration sense is tested separately. The Romberg precaution is protection against falling.",
    "adjacent fact")],
  c(52, 53)),

Q("Neurologic examination", IO_B, "manifestation",
  "Which test is being performed in this picture?",
  ("Romberg test",
   "Correct. The patient stands upright, feet together, eyes closed, while the examiner guards against "
   "a fall: Romberg testing for impaired proprioception."),
  [("Schamroth's window test",
    "Schamroth's window is a finger test, not a standing test. This is a standing balance test with "
    "eyes closed and the examiner guarding: Romberg.",
    "adjacent fact"),
   ("Vibration sense testing",
    "Vibration is tested with the patient still, applying a stimulus distally. This is standing "
    "balance with eyes closed: Romberg.",
    "adjacent fact"),
   ("Deep-tendon reflex testing",
    "Reflexes are tapped at the tendons. This patient is standing with eyes closed and guarded: "
    "Romberg.",
    "adjacent fact")],
  c(53, 52), img="l7-fig-10.jpg",
  alt="A man standing upright with his feet together and his eyes closed while a clinician stands beside him with her arms ready to catch him."),

# ======================================================== emergency (slide 54)
Q("Emergency", IO_D, "escalation",
  "Which finding in an anemic patient calls for urgent assessment?",
  ("Dyspnea at rest",
   "Correct. Active major bleeding, hypotension, syncope, chest pain, dyspnea at rest and altered "
   "mental status call for urgent assessment and immediate escalation."),
  [("Exertional dyspnea alone",
    "Exertional dyspnea is a general symptom. Dyspnea at REST is the urgent one.",
    "wrong stage or severity"),
   ("Fatigue",
    "Fatigue is a general symptom, not one of the urgent findings. Dyspnea at rest is among those that "
    "call for urgent assessment.",
    "wrong stage or severity"),
   ("Brittle nails",
    "Brittle nails are not among the listed urgent findings. Dyspnea at rest calls for urgent "
    "assessment.",
    "adjacent fact")],
  c(54, 55)),

Q("Emergency", IO_D, "escalation",
  "A patient with acute hemorrhage has a normal hemoglobin. What should be remembered?",
  ("Instability can precede the fall in hemoglobin",
   "Correct. In acute hemorrhage the patient may become unstable before the hemoglobin falls, so "
   "vital signs, mental status, perfusion and ongoing loss guide the response."),
  [("A normal hemoglobin excludes major bleeding",
    "It does not: the hemoglobin may not have fallen yet. Instability can come first.",
    "reversed direction or value"),
   ("Transfusion should be given at once",
    "Oxygen and transfusion are given according to the clinical situation, not routinely.",
    "wrong stage or severity"),
   ("The bleeding is too small to matter",
    "Hemoglobin lags in acute hemorrhage; judge by vital signs, mental status, perfusion and ongoing "
    "loss.",
    "common lay belief")],
  c(54)),

Q("Emergency", IO_D, "escalation",
  "What is the immediate response to an anemic patient with active major bleeding and hypotension?",
  ("Immediate escalation and resuscitation",
   "Correct. Active major bleeding with hypotension calls for immediate escalation: stabilization, "
   "bleeding control and resuscitation, with oxygen and transfusion according to the situation."),
  [("A complete dietary and travel history first",
    "The detailed history waits; immediate escalation for stabilization and bleeding control comes "
    "first.",
    "wrong stage or severity"),
   ("Outpatient stool blood testing",
    "Stool testing is not the immediate step: active major bleeding with hypotension needs immediate "
    "escalation.",
    "wrong stage or severity"),
   ("Repeat hemoglobin in a week",
    "Waiting is unsafe; instability may precede the hemoglobin fall. Escalate immediately.",
    "wrong stage or severity")],
  c(54)),

Q("Emergency", IO_D, "escalation",
  "Which is assessed when an anemic patient may be in a bleeding emergency?",
  ("Vital signs, mental status, perfusion",
   "Correct. In the emergency assess vital signs, mental status, skin perfusion and ongoing blood "
   "loss, then escalate."),
  [("Nail shape, hair shedding and diet",
    "These are not what the emergency assessment checks. Assess vital signs, mental status, skin "
    "perfusion and ongoing blood loss.",
    "wrong stage or severity"),
   ("Family history and ancestry",
    "Family history is not what the emergency assessment checks. Assess vital signs, mental status, "
    "skin perfusion and ongoing blood loss.",
    "wrong stage or severity"),
   ("Romberg test and gait",
    "The neurologic examination belongs to the B12 work-up. The emergency calls for vital signs, "
    "mental status, perfusion and ongoing loss.",
    "wrong stage or severity")],
  c(54)),

# ======================================================== interpretation (slides 55-56)
Q("Interpreting the findings", IO_D, "differential",
  "Which finding is a clue to the CAUSE of anemia rather than a general symptom?",
  ("Splenomegaly",
   "Correct. Clues to the cause are the bleeding history, jaundice, dietary or surgical history, "
   "neurologic findings, lymphadenopathy and splenomegaly. Fatigue, weakness, exertional dyspnea, "
   "palpitations and lightheadedness are general."),
  [("Palpitations",
    "Palpitations are a general symptom of anemia, saying nothing about cause.",
    "adjacent fact"),
   ("Lightheadedness",
    "Lightheadedness is a general symptom. Splenomegaly is a clue to the cause.",
    "adjacent fact"),
   ("Weakness",
    "Weakness is general and nonspecific. Splenomegaly points toward a cause.",
    "adjacent fact")],
  c(55)),

Q("Interpreting the findings", IO_A, "risk factors",
  "A woman has progressive fatigue, exertional dyspnea, heavier menstrual bleeding and frequent ibuprofen use. Which history best addresses the SOURCE of her anemia?",
  ("Menstrual flooding and any melena",
   "Correct. Heavier menstrual bleeding and frequent ibuprofen both point to blood loss: define "
   "menstrual flooding and protection changes, and ask about gastrointestinal bleeding such as "
   "melena."),
  [("Travel destinations and febrile illness",
    "Travel and fever look for infection; this history points to blood loss from the uterus or "
    "gastrointestinal tract.",
    "adjacent fact"),
   ("Paresthesias and walking in the dark",
    "Those are B12 neurologic clues. Her history points to menstrual and possible gastrointestinal "
    "blood loss.",
    "competing diagnosis"),
   ("Relatives needing a splenectomy",
    "That is the hemolysis family history. Her clues point to blood loss.",
    "competing diagnosis")],
  c(56, 12, 9)),

Q("Interpreting the findings", IO_C, "manifestation",
  "A patient with a previous gastric bypass reports tingling feet and difficulty walking in the dark. Which examination findings should be assessed?",
  ("Vibration sense, gait and Romberg",
   "Correct. Gastric bypass is a B12 deficiency risk, and tingling with trouble walking in the dark "
   "suggests posterior column loss: test distal vibration and joint-position sense, gait and balance, "
   "and Romberg."),
  [("Schamroth's window and nail-fold angle",
    "Those assess clubbing. The patient's symptoms are neurologic: test vibration, position sense, gait and "
    "Romberg.",
    "adjacent fact"),
   ("Cullen and Grey Turner signs",
    "Those look for internal bleeding. The patient's history points to B12 deficiency; test the neurologic "
    "findings.",
    "competing diagnosis"),
   ("Scleral icterus and splenomegaly",
    "Those suggest hemolysis. Gastric bypass with sensory ataxia points to B12 deficiency.",
    "competing diagnosis")],
  c(56, 52, 10)),
]

# See pd2_l7_pool_a.py: QUESTIONS lets blind_review.py attach `mis` to held items too.
# Every item carries a "mis" dict (built by Q in pd2_l7_pool_a); the quoted word lets
# tools/blind_review.py source_index() load this module, so held items get their `mis` too.
QUESTIONS = POOL_B
