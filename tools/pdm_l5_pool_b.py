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
     ["In the cerebrospinal fluid specifically", "Cerebrospinal fluid is an extracellular compartment, so sodium dominates there too; the meaningful contrast is extracellular against intracellular."],
     ["In the biliary and pancreatic secretions", "Biliary and pancreatic secretions are sodium-rich but are not where sodium is defined as the major cation; that is the extracellular fluid as a whole."]],
   c=0, cite=c(9)),

 dict(topic="Sodium", io=IOB1, slot="etiology",
   q="Sodium salts are the major determinant of which property of the extracellular fluid?",
   opts=[
     ["Its osmolality", "Correct — sodium with its accompanying anions makes up most of the osmotically active particles outside cells, so extracellular osmolality tracks the sodium concentration closely."],
     ["Its pH", "Bicarbonate and chloride carry the acid-base role."],
     ["Its oncotic pressure", "Albumin, a protein, sets oncotic pressure."],
     ["Its viscosity", "Viscosity is determined chiefly by the red cell concentration and plasma proteins, not by sodium salts."]],
   c=0, cite=c(9)),

 dict(topic="Sodium", io=IOB1, slot="etiology",
   q="Serum sodium represents a balance between which two processes?",
   opts=[
     ["Oral intake and renal excretion",
      "Correct — sodium enters only by mouth and leaves chiefly through the kidney, so the serum level sits between dietary intake and renal excretion."],
     ["Gastrointestinal absorption and biliary loss",
      "Sodium secreted into the gut is largely reabsorbed, and bile is not a significant route of sodium loss; renal excretion is."],
     ["Bone storage and bone release",
      "That describes calcium handling, not sodium."],
     ["Hepatic synthesis and renal clearance",
      "Sodium is not synthesised by the liver."]],
   c=0, cite=c(9)),

 dict(topic="Sodium", io=IOB1, slot="test finding",
   q="As total free body water rises, what happens to the serum sodium concentration?",
   opts=[
     ["It is diluted and may fall",
      "Correct — sodium concentration is an amount divided by a volume, so adding water to the same quantity of sodium lowers the measured value."],
     ["It rises as sodium is drawn into the extracellular space",
      "Added water dilutes rather than concentrates the sodium."],
     ["It is unchanged, because sodium is tightly regulated",
      "The total quantity of sodium is regulated, but its concentration moves with the water it is dissolved in, which is why a low sodium usually means excess water."],
     ["It falls only if kidney function is impaired",
      "Dilution does not require impaired kidneys."]],
   c=0, cite=c(9)),

 dict(topic="Sodium", io=IOB1, slot="etiology",
   q="How do the kidneys compensate when free body water rises?",
   opts=[
     ["By conserving sodium and excreting water",
      "Correct — the kidney holds on to sodium while excreting the excess water, which restores the concentration by removing the diluent rather than adding solute."],
     ["By excreting sodium and conserving water",
      "This is the reverse of what helps: excreting sodium and keeping water would dilute the serum sodium further."],
     ["By conserving both sodium and water",
      "Conserving water would worsen the dilution."],
     ["By excreting both sodium and water",
      "Sodium is conserved rather than excreted; only the excess water is lost, which is what corrects the dilution."]],
   c=0, cite=c(9)),

 dict(topic="Sodium", io=IOB1, slot="test finding",
   q="An abnormal sodium should first raise which question?",
   opts=[
     ["Is there too much or too little free water?",
      "Correct — because the sodium value is a concentration, an abnormal result reflects the water it is dissolved in before it reflects the amount of salt present."],
     ["Is there too much or too little salt?",
      "Salt is the second question; the concentration moves with water first, so free water is what is assessed at the outset."],
     ["Is kidney function normal?",
      "Renal function shapes the answer but is not the opening question; free water status is, because sodium is reported as a concentration."],
     ["Is the sample haemolysed?",
      "Haemolysis is a potassium artefact rather than a sodium one."]],
   c=0, cite=cn(9)),

 dict(topic="Sodium", io=IOB1, slot="etiology",
   q="What serum sodium reflects is distinct from what governs extracellular volume. Which pairing is correct?",
   opts=[
     ["Serum sodium reflects water balance; total-body sodium governs extracellular volume",
      "Correct — the concentration tells you about water, while the total quantity of sodium in the body determines how much extracellular fluid there is to hold it."],
     ["Serum sodium reflects total-body sodium; water balance governs extracellular volume",
      "This reverses both halves of the note."],
     ["Both serum sodium and total-body sodium reflect water balance",
      "The two are separate: the serum concentration tracks water, while total-body sodium sets extracellular volume."],
     ["Serum sodium reflects extracellular volume; water balance governs total-body sodium",
      "Neither half matches the note."]],
   c=0, cite=cn(9)),

 dict(topic="Sodium", io=IOB1, slot="etiology",
   q="Which two mechanisms control water handling, and therefore serum sodium?",
   opts=[
     ["Thirst and antidiuretic hormone",
      "Correct — thirst governs water taken in and antidiuretic hormone governs water retained, so together they set the dilution of the sodium."],
     ["Renin and angiotensin",
      "The renin-angiotensin-aldosterone system controls sodium handling and so extracellular volume; water handling runs through thirst and antidiuretic hormone."],
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
     ["In the interstitial fluid alone", "Interstitial fluid is extracellular, where sodium dominates; potassium is concentrated inside cells."],
     ["In the plasma alone", "Plasma is part of the extracellular compartment, where sodium dominates."]],
   c=0, cite=c(10)),

 dict(topic="Potassium", io=IOB2, slot="etiology",
   q="Potassium is an important determinant of what, especially in neuromuscular tissue?",
   opts=[
     ["The membrane electrical potential",
      "Correct — the steep potassium gradient across the cell membrane sets the resting potential, which is why small serum shifts alter cardiac and neuromuscular excitability."],
     ["The oncotic pressure across the capillary wall",
      "That is a protein effect, not a potassium one."],
     ["The rate of protein catabolism",
      "Potassium supports protein synthesis rather than setting the rate of catabolism; its critical role is the membrane potential."],
     ["The buffering of fixed acids",
      "Bicarbonate is the principal buffer of fixed acids; potassium's role is electrical, in setting the membrane potential."]],
   c=0, cite=c(10)),

 dict(topic="Potassium", io=IOB2, slot="complication",
   q="Why do small fluctuations in potassium matter?",
   opts=[
     ["Small changes in the serum level carry significant physiological consequences",
      "Correct — the normal range is narrow and the membrane potential depends on the gradient, so a shift of a single millimole can provoke a dangerous arrhythmia."],
     ["Small changes indicate that the sample was taken incorrectly",
      "Haemolysis does falsely raise potassium, but the reason small genuine changes matter is their effect on the membrane potential and cardiac rhythm."],
     ["Small changes are usually meaningless and can be ignored",
      "Small changes are far from meaningless; the normal range is narrow and small shifts can cause arrhythmia."],
     ["Small changes only matter in patients with kidney disease",
      "The risk is not confined to renal patients; any patient's cardiac conduction depends on the potassium gradient."]],
   c=0, cite=c(10)),

 dict(topic="Potassium", io=IOB2, slot="complication",
   q="Which complication follows BOTH high and low potassium?",
   opts=[
     ["Life-threatening cardiac arrhythmias",
      "Correct — both directions distort the resting membrane potential of cardiac muscle, so either extreme can precipitate a fatal arrhythmia."],
     ["Seizures", "Seizures are associated with sodium and calcium disturbance; potassium extremes threaten cardiac rhythm."],
     ["Acute kidney injury", "The kidney regulates potassium rather than failing because of it; the shared danger at either extreme is arrhythmia."],
     ["Hepatic encephalopathy", "Hepatic encephalopathy follows liver failure and ammonia accumulation, not a potassium derangement."]],
   c=0, cite=cn(10)),

 dict(topic="Potassium", io=IOB2, slot="etiology",
   q="How is the renal handling of potassium described?",
   opts=[
     ["It is excreted by the kidneys with no reabsorption",
      "Correct — potassium is filtered and secreted without meaningful reabsorption, so losses continue whether or not intake does."],
     ["It is filtered and then almost entirely reabsorbed",
      "Almost complete reabsorption describes sodium handling; potassium is excreted without being reclaimed."],
     ["It is neither filtered nor secreted, and is lost only in stool",
      "The kidney is the main route of potassium loss; stool is a minor contributor."],
     ["It is reabsorbed in exchange for sodium in the proximal tubule",
      "No such proximal exchange is described; potassium is excreted without reabsorption."]],
   c=0, cite=c(10)),

 dict(topic="Potassium", io=IOB2, slot="education",
   q="Given that potassium is excreted without reabsorption, what follows for the patient?",
   opts=[
     ["It must be replaced by diet or supplementation or the level can drop rapidly",
      "Correct — ongoing obligatory loss means that a patient who stops eating, or who is on intravenous fluids without potassium, will become hypokalaemic within days."],
     ["It accumulates over time and must be actively removed",
      "The absence of reabsorption means loss, not accumulation."],
     ["It is stored in bone and released as needed",
      "That describes calcium, not potassium."],
     ["It requires no dietary intake at all",
      "Dietary intake is essential precisely because there is no reabsorption to offset continuing losses."]],
   c=0, cite=c(10)),

 dict(topic="Potassium", io=IOB2, slot="etiology",
   q="Which hormone drives renal potassium excretion, and where does it act?",
   opts=[
     ["Aldosterone, at the distal tubule and collecting duct",
      "Correct — aldosterone acts on the principal cells of the distal tubule and collecting duct, reabsorbing sodium in exchange for potassium that is then lost in the urine."],
     ["Antidiuretic hormone, at the collecting duct",
      "Antidiuretic hormone acts on the collecting duct but governs water reabsorption; aldosterone is what drives potassium out."],
     ["Parathyroid hormone, at the proximal tubule",
      "That governs calcium and phosphate."],
     ["Renin, at the juxtaglomerular apparatus",
      "Renin initiates the cascade but is not named as the excretion driver."]],
   c=0, cite=cn(10)),

 dict(topic="Potassium", io=IOB2, slot="etiology",
   q="Besides renal excretion, what is the other mechanism of potassium regulation?",
   opts=[
     ["Transcellular shifts driven by insulin, acid-base status, and catecholamines",
      "Correct — insulin and catecholamines drive potassium into cells and acidosis drives it out, so the serum level can move sharply without any change in total body potassium."],
     ["Storage in and release from skeletal muscle glycogen",
      "Potassium moves across cell membranes rather than being stored with glycogen; insulin, acid-base status and catecholamines drive that shift."],
     ["Binding to and release from plasma albumin",
      "Potassium circulates free rather than bound to albumin, which is why the measured serum level responds so quickly to transcellular shifts."],
     ["Loss through sweat and insensible routes",
      "Sweat is a trivial route of potassium loss; regulation works through renal excretion and transcellular shift."]],
   c=0, cite=cn(10)),

 dict(topic="Potassium", io=IOB2, slot="test finding",
   q="Why must insulin and acid-base status be considered specifically when reading diabetic ketoacidosis results?",
   opts=[
     ["Both shift potassium across the cell membrane, so the serum value can mislead",
      "Correct — acidosis drives potassium out of cells and insulin drives it back in, so a normal or high serum potassium can conceal a large total-body deficit that treatment will unmask."],
     ["Both raise the measured potassium by causing haemolysis",
      "Haemolysis is a collection artefact; here the concern is a genuine physiological shift of potassium across cell membranes."],
     ["Both reduce renal potassium excretion to near zero",
      "Excretion continues and is in fact increased by the osmotic diuresis; what misleads is the shift of potassium between compartments."],
     ["Both interfere chemically with the potassium assay",
      "The effect is physiological rather than analytic."]],
   c=0, cite=cn(10)),

 # ---- chloride ----
 dict(topic="Chloride", io=IOB3, slot="etiology",
   q="What is chloride's status in the extracellular fluid?",
   opts=[
     ["It is the major extracellular anion", "Correct — chloride is the major extracellular anion."],
     ["It is the major extracellular cation", "Sodium is the major extracellular cation; chloride is negatively charged."],
     ["It is the major intracellular anion", "Chloride is largely excluded from cells by the membrane potential; it is the major extracellular anion."],
     ["It is the major intracellular cation", "That is potassium."]],
   c=0, cite=c(11)),

 dict(topic="Chloride", io=IOB3, slot="etiology",
   q="Why does chloride follow sodium?",
   opts=[
     ["To maintain electrical neutrality",
      "Correct — sodium carries a positive charge that must be balanced, so chloride moves with it to keep the fluid electrically neutral."],
     ["To maintain a constant osmolality",
      "Osmolality is a consequence; neutrality is the stated reason."],
     ["Because both are reabsorbed by the same transporter in the collecting duct",
      "There is no single shared collecting duct transporter behind this; chloride follows sodium because charge must balance."],
     ["Because both are bound to the same carrier protein",
      "Neither electrolyte is protein-carried in this way."]],
   c=0, cite=c(11)),

 dict(topic="Chloride", io=IOB3, slot="test finding",
   q="What is true of chloride measured as a standalone test?",
   opts=[
     ["It does not provide much information on its own",
      "Correct — chloride moves passively with sodium and reciprocally with bicarbonate, so its value carries meaning only when read against those two."],
     ["It is the single most informative electrolyte",
      "Chloride is among the least informative in isolation, precisely because it moves passively with sodium and bicarbonate."],
     ["It reliably identifies the cause of an acid-base disorder by itself",
      "It contributes to that reading only alongside the other electrolytes."],
     ["It is only useful when the sodium is normal",
      "Chloride is read alongside sodium and bicarbonate whatever the sodium value; it is never interpreted alone."]],
   c=0, cite=c(11)),

 dict(topic="Chloride", io=IOB3, slot="etiology",
   q="When carbon dioxide and hydrogen ions rise, bicarbonate moves out of the cell. What does chloride do?",
   opts=[
     ["It shifts back into the cell to preserve electrical neutrality",
      "Correct — this is the chloride shift: as bicarbonate leaves the red cell, chloride enters to replace the lost negative charge."],
     ["It shifts out of the cell alongside bicarbonate",
      "Both anions leaving would break electrical neutrality."],
     ["It is excreted by the kidney within minutes",
      "The movement is across the red cell membrane within seconds, not a renal loss over minutes."],
     ["It binds to haemoglobin and is carried to the lungs",
      "That is how carbon dioxide is carried, not chloride."]],
   c=0, cite=c(11)),

 dict(topic="Chloride", io=IOB3, slot="test finding",
   q="A patient has a low chloride with a high bicarbonate. Which acid-base picture does this suggest?",
   opts=[
     ["Metabolic alkalosis, such as from vomiting",
      "Correct — vomiting loses hydrochloric acid, stripping chloride while bicarbonate is retained, so the two move in opposite directions."],
     ["Metabolic acidosis with a raised anion gap",
      "That pattern has a low bicarbonate, not a high one."],
     ["Respiratory acidosis",
      "Respiratory acidosis raises bicarbonate through renal compensation but does not strip chloride; the low chloride points to acid loss."],
     ["A normal anion gap acidosis from bicarbonate loss",
      "Bicarbonate loss would lower the bicarbonate and raise the chloride."]],
   c=0, cite=cn(11)),

 dict(topic="Chloride", io=IOB3, slot="test finding",
   q="Which named acid-base disorder is the example of chloride and bicarbonate moving reciprocally?",
   opts=[
     ["Hyperchloraemic non-gap metabolic acidosis",
      "Correct — as bicarbonate is lost from gut or kidney, chloride is retained in its place, so the gap stays normal and the chloride rises."],
     ["Hypochloraemic gap metabolic acidosis",
      "A gap acidosis is caused by added unmeasured anions rather than by chloride replacing bicarbonate; the reciprocal example is the hyperchloraemic non-gap form."],
     ["Compensated respiratory alkalosis",
      "A compensated respiratory alkalosis is defined by the carbon dioxide, not by chloride and bicarbonate trading places."],
     ["Mixed respiratory and metabolic acidosis",
      "A mixed picture obscures the relationship; the clean example is hyperchloraemic non-gap metabolic acidosis."]],
   c=0, cite=cn(11)),

 # ---- bicarbonate ----
 dict(topic="Bicarbonate", io=IOB4, slot="etiology",
   q="What role does bicarbonate play in the extracellular fluid?",
   opts=[
     ["It is the primary extracellular buffer",
      "Correct — bicarbonate accepts hydrogen ions and its concentration is regulated by the kidney while its acid partner is blown off by the lungs, making it the main extracellular buffer."],
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
      "Correct — the assay measures all forms of carbon dioxide in serum, and around 95 per cent of that is bicarbonate, so the label and the substance differ."],
     ["The laboratory measures dissolved carbon dioxide gas directly",
      "The reported value is total carbon dioxide, the bulk of which is bicarbonate."],
     ["Bicarbonate is unstable and must be converted before measurement",
      "No conversion step is involved; the panel simply reports total carbon dioxide, which is overwhelmingly bicarbonate."],
     ["It reflects the carbon dioxide cleared by the lungs that minute",
      "That is what a blood gas measures, not the panel value."]],
   c=0, cite=c(12)),

 dict(topic="Bicarbonate", io=IOB4, slot="test finding",
   q="A low bicarbonate on a chemistry panel indicates which disorder?",
   opts=[
     ["Metabolic acidosis", "Correct — bicarbonate is consumed buffering excess acid, so a low value on the panel marks a metabolic acidosis."],
     ["Metabolic alkalosis", "That is indicated by a high bicarbonate."],
     ["Respiratory alkalosis", "Respiratory alkalosis lowers bicarbonate only through slow renal compensation; a low panel bicarbonate is read first as a metabolic acidosis."],
     ["Respiratory acidosis", "Respiratory acidosis raises bicarbonate through renal compensation rather than lowering it."]],
   c=0, cite=c(12)),

 dict(topic="Bicarbonate", io=IOB4, slot="initial test",
   q="A low bicarbonate is the trigger to do what next?",
   opts=[
     ["Calculate the anion gap",
      "Correct — the gap separates acidosis caused by added acid from acidosis caused by bicarbonate loss, which is the first branch point in finding the cause."],
     ["Order an arterial blood gas before anything else",
      "A blood gas may follow to confirm the pH, but the gap is calculated first because it costs nothing and narrows the differential immediately."],
     ["Repeat the panel to exclude a laboratory error",
      "Repeating is the response to a borderline value; a clearly low bicarbonate calls for the anion gap."],
     ["Give intravenous bicarbonate",
      "Bicarbonate is not given reflexively; the cause of the acidosis is established first, starting with the gap."]],
   c=0, cite=c(12)),

 dict(topic="Bicarbonate", io=IOB4, slot="test finding",
   q="What does calculating the anion gap let you separate?",
   opts=[
     ["Raised-gap acidosis from normal-gap acidosis",
      "Correct — a wide gap means unmeasured acids have been added, while a normal gap means bicarbonate has been lost and replaced by chloride."],
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
      "Correct — most carbon dioxide travels from the tissues to the lungs as bicarbonate in plasma rather than dissolved as gas."],
     ["Helping transport oxygen to the tissues",
      "Oxygen transport is haemoglobin's role."],
     ["Maintaining the resting membrane potential",
      "That is attributed to potassium."],
     ["Determining extracellular osmolality",
      "Sodium salts are the major determinant."]],
   c=0, cite=c(12)),
]
