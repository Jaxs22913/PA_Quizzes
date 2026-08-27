# -*- coding: utf-8 -*-
# PDM I Lecture 5 -- pool B. The physiological role of each electrolyte.
# Syllabus objective b, parts i (sodium), ii (potassium), iii (chloride),
# iv (bicarbonate).
#
# NO QUESTION HERE TURNS ON A REFERENCE RANGE. Reynolds said on 26 August that
# she always supplies reference ranges on the exam and does not ask students to
# memorise them. The three places where this deck's text slides disagree with
# its own fishbone image are therefore not resolved and not quizzed --
# see pdm_l5_partition.py.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "5. Chemistry Panels, Renal Fxn, Elytes.pptx"
def c(n): return f"{SRC}, Slide {n}"
def ci(n): return f"{SRC}, Slide {n} (image only)"
def cn(n): return f"{SRC}, Slide {n} (speaker notes)"

IOB1 = "b(i) — Discuss the physiological role of sodium"
IOB2 = "b(ii) — Discuss the physiological role of potassium"
IOB3 = "b(iii) — Discuss the physiological role of chloride"
IOB4 = "b(iv) — Discuss the physiological role of bicarbonate"

POOL_B = [
 # ---- sodium ----
 dict(topic="Sodium", io=IOB1, slot="etiology",
   q="Where is sodium the major cation?",
   opts=[
     ["In the extracellular fluid", "Correct — sodium is the major extracellular cation."],
     ["In the intracellular fluid", "Potassium is the major intracellular cation."],
     ["In the cerebrospinal fluid specifically", "The deck's contrast is extracellular against intracellular, not by compartment."],
     ["In the biliary and pancreatic secretions", "The deck makes no such claim."]],
   c=0, cite=c(9)),

 dict(topic="Sodium", io=IOB1, slot="etiology",
   q="Sodium salts are the major determinant of which property of the extracellular fluid?",
   opts=[
     ["Its osmolality", "Correct — the deck's phrasing for what sodium salts determine."],
     ["Its pH", "Bicarbonate and chloride carry the acid-base role."],
     ["Its oncotic pressure", "Albumin, a protein, sets oncotic pressure."],
     ["Its viscosity", "Not a property the deck attributes to sodium."]],
   c=0, cite=c(9)),

 dict(topic="Sodium", io=IOB1, slot="etiology",
   q="Serum sodium represents a balance between which two processes?",
   opts=[
     ["Oral intake and renal excretion",
      "Correct — the two the deck names as setting the serum level."],
     ["Gastrointestinal absorption and biliary loss",
      "Biliary loss is not a route the deck describes for sodium."],
     ["Bone storage and bone release",
      "That describes calcium handling, not sodium."],
     ["Hepatic synthesis and renal clearance",
      "Sodium is not synthesised by the liver."]],
   c=0, cite=c(9)),

 dict(topic="Sodium", io=IOB1, slot="test finding",
   q="As total free body water rises, what happens to the serum sodium concentration?",
   opts=[
     ["It is diluted and may fall",
      "Correct — the deck's central physiological point about water and sodium."],
     ["It rises as sodium is drawn into the extracellular space",
      "Added water dilutes rather than concentrates the sodium."],
     ["It is unchanged, because sodium is tightly regulated",
      "The deck's whole point is that the concentration moves with water."],
     ["It falls only if kidney function is impaired",
      "Dilution does not require impaired kidneys."]],
   c=0, cite=c(9)),

 dict(topic="Sodium", io=IOB1, slot="etiology",
   q="How do the kidneys compensate when free body water rises?",
   opts=[
     ["By conserving sodium and excreting water",
      "Correct — the compensation the deck describes."],
     ["By excreting sodium and conserving water",
      "That is the reverse of the deck's statement."],
     ["By conserving both sodium and water",
      "Conserving water would worsen the dilution."],
     ["By excreting both sodium and water",
      "The deck describes sodium being conserved, not excreted."]],
   c=0, cite=c(9)),

 dict(topic="Sodium", io=IOB1, slot="test finding",
   q="According to the speaker notes, an abnormal sodium should first raise which question?",
   opts=[
     ["Is there too much or too little free water?",
      "Correct — the notes say to ask the water question before the salt question."],
     ["Is there too much or too little salt?",
      "The notes say this is the second question, not the first."],
     ["Is kidney function normal?",
      "Renal function matters, but it is not the first question the notes pose."],
     ["Is the sample haemolysed?",
      "Haemolysis is a potassium artefact rather than a sodium one."]],
   c=0, cite=cn(9)),

 dict(topic="Sodium", io=IOB1, slot="etiology",
   q="The speaker notes distinguish what serum sodium reflects from what governs extracellular volume. Which pairing is correct?",
   opts=[
     ["Serum sodium reflects water balance; total-body sodium governs extracellular volume",
      "Correct — the distinction the notes draw."],
     ["Serum sodium reflects total-body sodium; water balance governs extracellular volume",
      "This reverses both halves of the note."],
     ["Both serum sodium and total-body sodium reflect water balance",
      "The notes separate the two rather than equating them."],
     ["Serum sodium reflects extracellular volume; water balance governs total-body sodium",
      "Neither half matches the note."]],
   c=0, cite=cn(9)),

 dict(topic="Sodium", io=IOB1, slot="etiology",
   q="Which two mechanisms do the speaker notes say control water handling, and therefore serum sodium?",
   opts=[
     ["Thirst and antidiuretic hormone",
      "Correct — the two the notes name for water handling."],
     ["Renin and angiotensin",
      "The notes assign the renin-angiotensin-aldosterone system to extracellular volume instead."],
     ["Aldosterone and atrial natriuretic peptide",
      "Aldosterone is named for total-body sodium, not for water handling."],
     ["Insulin and the catecholamines",
      "Those shift potassium across cell membranes."]],
   c=0, cite=cn(9)),

 # ---- potassium ----
 dict(topic="Potassium", io=IOB2, slot="etiology",
   q="Where is potassium the major cation?",
   opts=[
     ["In the intracellular fluid", "Correct — potassium is the major intracellular cation."],
     ["In the extracellular fluid", "Sodium holds that role."],
     ["In the interstitial fluid alone", "The deck's contrast is intracellular against extracellular."],
     ["In the plasma alone", "Plasma is part of the extracellular compartment, where sodium dominates."]],
   c=0, cite=c(10)),

 dict(topic="Potassium", io=IOB2, slot="etiology",
   q="Potassium is an important determinant of what, especially in neuromuscular tissue?",
   opts=[
     ["The membrane electrical potential",
      "Correct — the deck's phrasing for potassium's central role."],
     ["The oncotic pressure across the capillary wall",
      "That is a protein effect, not a potassium one."],
     ["The rate of protein catabolism",
      "The deck links potassium to protein synthesis, not catabolic rate."],
     ["The buffering of fixed acids",
      "Bicarbonate is the buffer the deck names."]],
   c=0, cite=c(10)),

 dict(topic="Potassium", io=IOB2, slot="complication",
   q="Why does the deck stress that small fluctuations in potassium matter?",
   opts=[
     ["Small changes in the serum level carry significant physiological consequences",
      "Correct — the deck's reason for treating potassium as high-stakes."],
     ["Small changes indicate that the sample was taken incorrectly",
      "Collection artefact is a real issue but is not the deck's point here."],
     ["Small changes are usually meaningless and can be ignored",
      "The deck says the opposite."],
     ["Small changes only matter in patients with kidney disease",
      "The deck does not restrict the significance to renal patients."]],
   c=0, cite=c(10)),

 dict(topic="Potassium", io=IOB2, slot="complication",
   q="Which complication do the speaker notes attribute to BOTH high and low potassium?",
   opts=[
     ["Life-threatening cardiac arrhythmias",
      "Correct — the notes name arrhythmia as the shared danger at either extreme."],
     ["Seizures", "Not the complication the notes give for potassium."],
     ["Acute kidney injury", "Kidneys regulate potassium rather than failing because of it in the notes."],
     ["Hepatic encephalopathy", "The notes make no such link."]],
   c=0, cite=cn(10)),

 dict(topic="Potassium", io=IOB2, slot="etiology",
   q="How does the deck describe the renal handling of potassium?",
   opts=[
     ["It is excreted by the kidneys with no reabsorption",
      "Correct — the deck's stated main physiological point about potassium."],
     ["It is filtered and then almost entirely reabsorbed",
      "The deck states there is no reabsorption."],
     ["It is neither filtered nor secreted, and is lost only in stool",
      "The deck names the kidney as the route of loss."],
     ["It is reabsorbed in exchange for sodium in the proximal tubule",
      "The deck does not describe such an exchange."]],
   c=0, cite=c(10)),

 dict(topic="Potassium", io=IOB2, slot="education",
   q="Given that potassium is excreted without reabsorption, what follows for the patient?",
   opts=[
     ["It must be replaced by diet or supplementation or the level can drop rapidly",
      "Correct — the consequence the deck draws from the absence of reabsorption."],
     ["It accumulates over time and must be actively removed",
      "The absence of reabsorption means loss, not accumulation."],
     ["It is stored in bone and released as needed",
      "That describes calcium, not potassium."],
     ["It requires no dietary intake at all",
      "The deck says the opposite — replacement is required."]],
   c=0, cite=c(10)),

 dict(topic="Potassium", io=IOB2, slot="etiology",
   q="Which hormone do the speaker notes name as driving renal potassium excretion, and where does it act?",
   opts=[
     ["Aldosterone, at the distal tubule and collecting duct",
      "Correct — the hormone and site the notes give."],
     ["Antidiuretic hormone, at the collecting duct",
      "That hormone governs water handling in the notes."],
     ["Parathyroid hormone, at the proximal tubule",
      "That governs calcium and phosphate."],
     ["Renin, at the juxtaglomerular apparatus",
      "Renin initiates the cascade but is not named as the excretion driver."]],
   c=0, cite=cn(10)),

 dict(topic="Potassium", io=IOB2, slot="etiology",
   q="Besides renal excretion, what is the other mechanism the speaker notes give for potassium regulation?",
   opts=[
     ["Transcellular shifts driven by insulin, acid-base status, and catecholamines",
      "Correct — the three drivers of shift that the notes list."],
     ["Storage in and release from skeletal muscle glycogen",
      "The notes describe shift across membranes, not glycogen storage."],
     ["Binding to and release from plasma albumin",
      "Potassium is not protein-bound in the way the notes describe."],
     ["Loss through sweat and insensible routes",
      "Not a mechanism the notes raise for regulation."]],
   c=0, cite=cn(10)),

 dict(topic="Potassium", io=IOB2, slot="test finding",
   q="Why do the speaker notes flag insulin and acid-base status specifically when reading diabetic ketoacidosis results?",
   opts=[
     ["Both shift potassium across the cell membrane, so the serum value can mislead",
      "Correct — the reason the notes give for reading those labs carefully."],
     ["Both raise the measured potassium by causing haemolysis",
      "Haemolysis is a collection artefact and is not what the notes describe."],
     ["Both reduce renal potassium excretion to near zero",
      "The notes describe shift, not a halt in excretion."],
     ["Both interfere chemically with the potassium assay",
      "The effect is physiological rather than analytic."]],
   c=0, cite=cn(10)),

 # ---- chloride ----
 dict(topic="Chloride", io=IOB3, slot="etiology",
   q="What is chloride's status in the extracellular fluid?",
   opts=[
     ["It is the major extracellular anion", "Correct — chloride is the major extracellular anion."],
     ["It is the major extracellular cation", "Sodium is the major extracellular cation; chloride is negatively charged."],
     ["It is the major intracellular anion", "The deck places chloride extracellularly."],
     ["It is the major intracellular cation", "That is potassium."]],
   c=0, cite=c(11)),

 dict(topic="Chloride", io=IOB3, slot="etiology",
   q="Why does chloride follow sodium?",
   opts=[
     ["To maintain electrical neutrality",
      "Correct — the deck's reason for chloride tracking sodium."],
     ["To maintain a constant osmolality",
      "Osmolality is a consequence; neutrality is the stated reason."],
     ["Because both are reabsorbed by the same transporter in the collecting duct",
      "The deck does not give a shared transporter as the reason."],
     ["Because both are bound to the same carrier protein",
      "Neither electrolyte is protein-carried in this way."]],
   c=0, cite=c(11)),

 dict(topic="Chloride", io=IOB3, slot="test finding",
   q="What does the deck say about chloride measured as a standalone test?",
   opts=[
     ["It does not provide much information on its own",
      "Correct — the deck is explicit that chloride alone is uninformative."],
     ["It is the single most informative electrolyte",
      "The deck says the opposite."],
     ["It reliably identifies the cause of an acid-base disorder by itself",
      "It contributes to that reading only alongside the other electrolytes."],
     ["It is only useful when the sodium is normal",
      "The deck sets no such condition."]],
   c=0, cite=c(11)),

 dict(topic="Chloride", io=IOB3, slot="etiology",
   q="When carbon dioxide and hydrogen ions rise, bicarbonate moves out of the cell. What does chloride do?",
   opts=[
     ["It shifts back into the cell to preserve electrical neutrality",
      "Correct — the reciprocal shift the deck describes."],
     ["It shifts out of the cell alongside bicarbonate",
      "Both anions leaving would break electrical neutrality."],
     ["It is excreted by the kidney within minutes",
      "The deck describes a transcellular shift, not renal loss."],
     ["It binds to haemoglobin and is carried to the lungs",
      "That is how carbon dioxide is carried, not chloride."]],
   c=0, cite=c(11)),

 dict(topic="Chloride", io=IOB3, slot="test finding",
   q="A patient has a low chloride with a high bicarbonate. Which acid-base picture do the speaker notes say this suggests?",
   opts=[
     ["Metabolic alkalosis, such as from vomiting",
      "Correct — the notes give exactly this pattern and this cause."],
     ["Metabolic acidosis with a raised anion gap",
      "That pattern has a low bicarbonate, not a high one."],
     ["Respiratory acidosis",
      "The notes tie this chloride and bicarbonate pattern to metabolic alkalosis."],
     ["A normal anion gap acidosis from bicarbonate loss",
      "Bicarbonate loss would lower the bicarbonate and raise the chloride."]],
   c=0, cite=cn(11)),

 dict(topic="Chloride", io=IOB3, slot="test finding",
   q="Which named acid-base disorder do the speaker notes give as the example of chloride and bicarbonate moving reciprocally?",
   opts=[
     ["Hyperchloraemic non-gap metabolic acidosis",
      "Correct — the disorder the notes name for the reciprocal relationship."],
     ["Hypochloraemic gap metabolic acidosis",
      "The notes name the hyperchloraemic non-gap form."],
     ["Compensated respiratory alkalosis",
      "Not the example the notes give."],
     ["Mixed respiratory and metabolic acidosis",
      "The notes give a single named disorder rather than a mixed picture."]],
   c=0, cite=cn(11)),

 # ---- bicarbonate ----
 dict(topic="Bicarbonate", io=IOB4, slot="etiology",
   q="What role does bicarbonate play in the extracellular fluid?",
   opts=[
     ["It is the primary extracellular buffer",
      "Correct — the deck's description of bicarbonate's role."],
     ["It is the primary extracellular cation",
      "Bicarbonate carries a negative charge, and sodium is the major cation."],
     ["It is the primary determinant of extracellular osmolality",
      "Sodium salts hold that role."],
     ["It is the primary carrier of oxygen in plasma",
      "Haemoglobin carries oxygen; bicarbonate helps transport carbon dioxide."]],
   c=0, cite=c(12)),

 dict(topic="Bicarbonate", io=IOB4, slot="test finding",
   q="Why is bicarbonate reported on a chemistry panel as carbon dioxide?",
   opts=[
     ["The panel reports total carbon dioxide, which is mostly serum bicarbonate",
      "Correct — the deck explains the label this way."],
     ["The laboratory measures dissolved carbon dioxide gas directly",
      "The reported value is total carbon dioxide, the bulk of which is bicarbonate."],
     ["Bicarbonate is unstable and must be converted before measurement",
      "The deck does not describe a conversion step."],
     ["It reflects the carbon dioxide cleared by the lungs that minute",
      "That is what a blood gas measures, not the panel value."]],
   c=0, cite=c(12)),

 dict(topic="Bicarbonate", io=IOB4, slot="test finding",
   q="A low bicarbonate on a chemistry panel indicates which disorder?",
   opts=[
     ["Metabolic acidosis", "Correct — a low bicarbonate is the deck's marker of metabolic acidosis."],
     ["Metabolic alkalosis", "That is indicated by a high bicarbonate."],
     ["Respiratory alkalosis", "The deck reads the panel bicarbonate as a metabolic marker."],
     ["Respiratory acidosis", "The deck assigns the metabolic disorders to this value."]],
   c=0, cite=c(12)),

 dict(topic="Bicarbonate", io=IOB4, slot="initial test",
   q="A low bicarbonate is the trigger to do what next?",
   opts=[
     ["Calculate the anion gap",
      "Correct — the deck says always to calculate the gap when bicarbonate is low, and Reynolds repeated it in the lecture."],
     ["Order an arterial blood gas before anything else",
      "A gas may follow, but the deck's immediate next step is the gap."],
     ["Repeat the panel to exclude a laboratory error",
      "Repeating is the deck's advice for borderline values generally, not for this trigger."],
     ["Give intravenous bicarbonate",
      "The deck's next step is diagnostic rather than therapeutic."]],
   c=0, cite=c(12)),

 dict(topic="Bicarbonate", io=IOB4, slot="test finding",
   q="What does calculating the anion gap let you separate?",
   opts=[
     ["Raised-gap acidosis from normal-gap acidosis",
      "Correct — the separation the speaker notes name as the point of the calculation."],
     ["Metabolic acidosis from respiratory acidosis",
      "That separation comes from the blood gas rather than the gap."],
     ["Acute from chronic kidney disease",
      "Chronicity is judged over months, not by the gap."],
     ["Compensated from uncompensated alkalosis",
      "The gap is used in the assessment of acidosis."]],
   c=0, cite=cn(12)),

 dict(topic="Bicarbonate", io=IOB4, slot="etiology",
   q="Besides buffering, what is bicarbonate's other stated function?",
   opts=[
     ["Helping transport carbon dioxide in the bloodstream",
      "Correct — the deck pairs buffering with carbon dioxide transport."],
     ["Helping transport oxygen to the tissues",
      "Oxygen transport is haemoglobin's role."],
     ["Maintaining the resting membrane potential",
      "That is attributed to potassium."],
     ["Determining extracellular osmolality",
      "Sodium salts are the major determinant."]],
   c=0, cite=c(12)),
]
