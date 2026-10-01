# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Diuretics and Heart Failure Drugs (Lecture 9), topic 2: the thiazide diuretics.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. The correct answer is authored FIRST; the
partitioner (pharm_e3_partition.py) rotates the positions and halves the pool into two sets.

SOURCE. Diuretics and Heart Failure Drugs.pptx slides 20-29 (agents, mechanism, major actions, other actions,
indications, thiazides in hypertension, adverse effects, drug interactions). The distal-tubule diagram on slide 21 was
read by eye into tools/pharm_e3/ocr.json.

WEIGHTING (Dr. McInnis): indications, patient education, adverse effects, contraindications and drug choice outnumber
mechanism plus physiology (the partitioner enforces this per set).

KEYING DECISIONS applied (E3_BRIEF) and one more found while writing:
  * thiazides and uric acid: keyed as HYPERURICEMIA and gout (slides 26); the "acute increase in uric acid excretion"
    (slide 23) is never keyed;
  * "ineffective at a creatinine clearance below 30-40" (slide 28) is never keyed as an absolute: only that metolazone
    keeps its effect at a low clearance;
  * "works best in the elderly, obese, African American, sodium-retentive" (slide 25): obesity is never keyed;
  * the phosphodiesterase-inhibitor and carbonic anhydrase "some activity" lines (slide 21) are never keyed;
  * NEW CONFLICT: slide 24 lists "Hypercalcemia/renal calcium stones" as a thiazide indication. Thiazides RAISE
    serum calcium and are used for hypercalciuria and calcium stones, never to treat hypercalcemia (loops do, with
    saline), and slide 27 itself lists hypercalcemia as an adverse effect. Truth wins: the calcium stone indication is
    keyed, hypercalcemia is keyed only as an ADVERSE effect and is never offered as an indication or a distractor.
  * no dose appears anywhere; the potassium target (above 4.0 mEq/L, slide 29) is a clinical threshold, kept.

LEFT UNASKED ON PURPOSE: the brand names (Diuril, Aquazide, Hygroton, Mykrox, Lozol); the phosphodiesterase action; the
increase in proximal tubule calcium reabsorption; the acute uric acid line; the "obese" responder; the hyperlipidemia
percentage (5-15 percent) as a figure.
"""

D = "Diuretics and Heart Failure Drugs.pptx"
IO_CLASS = "Identify diuretics and heart failure drug classes and commonly prescribed diuretics and heart failure drugs"
IO_MOA = "Describe the molecular mechanism of action of diuretics and heart failure drugs"
IO_IND = "Identify indications for commonly used diuretics and heart failure drugs"
IO_ADME = "Describe absorption, distribution, metabolism, and excretion of diuretics and heart failure drugs"
IO_TOX = "Summarize side effects and toxic manifestations of diuretics and heart failure drugs"
IO_AE = "Describe adverse effects of diuretics and heart failure drugs"
IO_CONTRA = "Identify contraindications for diuretics and heart failure drugs"
IO_INTER = "Discuss potential drug-drug, drug-food, and drug-herb interactions with diuretics and heart failure drugs"
IO_PROT = "List commonly used protocols and patient monitoring for diuretics and heart failure drugs"
IO_EDU = "Outline appropriate patient education for diuretics and heart failure drugs"


def Q(topic, io, slot, q, key, wrong, slide):
    """key = (text, why); wrong = three (text, why). 'Correct.' is added to the key's reason here."""
    assert len(wrong) == 3
    return {"topic": topic, "io": io, "slot": slot, "q": q,
            "opts": [[key[0], "Correct. " + key[1]]] + [[t, e] for t, e in wrong],
            "c": 0, "cite": "%s, Slide %d" % (D, slide)}


QUESTIONS = [

# ---- agents and site ---------------------------------------------------------------------
Q("Thiazide agents and site", IO_CLASS, "class",
  "Which drug is a thiazide diuretic?",
  ("Hydrochlorothiazide",
   "Hydrochlorothiazide is a thiazide diuretic, along with chlorothiazide, chlorthalidone, metolazone and indapamide."),
  [("Furosemide",
    "Furosemide is a loop diuretic; the thiazide diuretics are chlorothiazide, hydrochlorothiazide, chlorthalidone, metolazone and indapamide."),
   ("Amiloride",
    "Amiloride is a potassium-sparing diuretic; the thiazide diuretics are chlorothiazide, hydrochlorothiazide, chlorthalidone, metolazone and indapamide."),
   ("Acetazolamide",
    "Acetazolamide is a carbonic anhydrase inhibitor; the thiazide diuretics are chlorothiazide, hydrochlorothiazide, chlorthalidone, metolazone and indapamide.")], 20),

Q("Thiazide agents and site", IO_CLASS, "class",
  "Which agent is a thiazide-type diuretic?",
  ("Chlorthalidone",
   "Chlorthalidone (Hygroton) is a thiazide-type diuretic that acts in the distal convoluted tubule."),
  [("Bumetanide",
    "Bumetanide is a loop diuretic acting on the thick ascending limb; chlorthalidone is the thiazide-type agent."),
   ("Eplerenone",
    "Eplerenone is an aldosterone antagonist acting in the collecting duct; chlorthalidone is the thiazide-type agent."),
   ("Methazolamide",
    "Methazolamide is a carbonic anhydrase inhibitor acting in the proximal tubule; chlorthalidone is the thiazide-type agent.")], 20),

Q("Thiazide agents and site", IO_CLASS, "class",
  "Which of these drugs belongs with the thiazide diuretics?",
  ("Indapamide",
   "Indapamide (Lozol) belongs with the thiazide diuretics and blocks sodium chloride reabsorption in the distal convoluted tubule."),
  [("Torsemide",
    "Torsemide is a loop diuretic acting on the thick ascending limb; indapamide is the thiazide-type agent acting in the distal convoluted tubule."),
   ("Triamterene",
    "Triamterene is a potassium-sparing diuretic acting on luminal sodium channels in the collecting duct; indapamide is the thiazide-type agent."),
   ("Dichlorphenamide",
    "Dichlorphenamide is a carbonic anhydrase inhibitor acting in the proximal tubule; indapamide is the thiazide-type agent.")], 20),

Q("Thiazide agents and site", IO_CLASS, "class",
  "Which drug is NOT a thiazide diuretic?",
  ("Torsemide",
   "Torsemide is a loop diuretic; chlorothiazide, hydrochlorothiazide, chlorthalidone, metolazone and indapamide are the thiazide group."),
  [("Metolazone",
    "Metolazone is a thiazide-type diuretic and acts in the distal convoluted tubule."),
   ("Chlorothiazide",
    "Chlorothiazide (Diuril) is a thiazide diuretic acting in the distal convoluted tubule."),
   ("Indapamide",
    "Indapamide is a thiazide-type diuretic and acts in the distal convoluted tubule.")], 20),

Q("Thiazide agents and site", IO_CLASS, "class",
  "Where do thiazide diuretics act in the nephron?",
  ("Distal convoluted tubule",
   "Thiazides inhibit the sodium chloride transporter on the luminal membrane of the distal convoluted tubule."),
  [("Thick ascending limb of the loop of Henle",
    "That is where loop diuretics act; thiazides act in the distal convoluted tubule."),
   ("Proximal convoluted tubule",
    "That is where carbonic anhydrase inhibitors act; thiazides act in the distal convoluted tubule."),
   ("Collecting duct",
    "That is where potassium-sparing diuretics act; thiazides act in the distal convoluted tubule.")], 21),

Q("Thiazide agents and site", IO_MOA, "mechanism",
  "Which transport protein do thiazide diuretics inhibit?",
  ("The sodium-chloride transporter",
   "The major thiazide action is inhibition of the sodium-chloride transporter on the luminal membrane of the distal convoluted tubule."),
  [("The sodium-potassium-2-chloride carrier",
    "That carrier of the thick ascending limb is the loop diuretic target; thiazides block the sodium-chloride transporter."),
   ("The luminal sodium channel",
    "Blocking the luminal sodium channel is how amiloride and triamterene act; thiazides block the sodium-chloride transporter."),
   ("The sodium-potassium pump",
    "The sodium-potassium pump on the blood side is not the thiazide target; thiazides block the luminal sodium-chloride transporter.")], 21),

Q("Thiazide agents and site", IO_MOA, "mechanism",
  "Which pair of minerals do thiazides cause to be lost in the urine?",
  ("Potassium and magnesium",
   "Thiazides increase potassium and magnesium excretion, which is why hypokalemia is a listed adverse effect."),
  [("Potassium and calcium",
    "Thiazides decrease renal calcium excretion; the minerals lost are potassium and magnesium."),
   ("Magnesium and calcium",
    "Calcium excretion is decreased by thiazides; the minerals lost are potassium and magnesium."),
   ("Sodium and calcium",
    "Sodium is lost, but calcium is retained; the minerals lost besides sodium are potassium and magnesium.")], 22),

# ---- calcium ---------------------------------------------------------------------------------
Q("Thiazide calcium effects", IO_IND, "indication",
  "Which history makes a thiazide reasonable because of its effect on urinary calcium?",
  ("Calcium oxalate kidney stones",
   "By lowering urinary calcium, thiazides leave less calcium to crystallize, so they are used for calcium oxalate stones."),
  [("Acute pulmonary edema",
    "Acute pulmonary edema is treated with a loop diuretic; the calcium-related thiazide use is for calcium oxalate stones."),
   ("Gout with frequent flares",
    "Thiazides raise uric acid and can worsen gout; the calcium-related use is calcium oxalate stones."),
   ("Infection-related struvite stones",
    "Struvite stones form because of urinary infection and are not prevented by lowering urinary calcium; the calcium-related use is calcium oxalate stones.")], 24),

Q("Thiazide calcium effects", IO_AE, "adverse effect",
  "Which electrolyte abnormality can thiazides cause that loop diuretics do not?",
  ("Hypercalcemia",
   "Because thiazides decrease renal calcium excretion, serum calcium can rise, so hypercalcemia is a listed adverse effect."),
  [("Hypokalemia",
    "Loop diuretics cause hypokalemia too, so it does not distinguish thiazides; hypercalcemia does."),
   ("Hypomagnesemia",
    "Loop diuretics also waste magnesium; hypercalcemia is the thiazide-specific abnormality."),
   ("Hyperkalemia",
    "Thiazides increase potassium loss and do not cause hyperkalemia; hypercalcemia is the thiazide-specific abnormality.")], 27),

# ---- hypertension --------------------------------------------------------------------------
Q("Thiazides in hypertension", IO_IND, "indication",
  "Which patient is most likely to respond well to a thiazide for hypertension?",
  ("An elderly patient who retains sodium",
   "Thiazides work best in the elderly, African American patients and sodium-retentive states, where removing sodium has the largest effect."),
  [("A young patient with high renin activity",
    "Thiazides work best in sodium-retentive patients; high renin activity points away from a sodium-driven pressure."),
   ("A patient with marked volume depletion",
    "A volume-depleted patient has no excess sodium to remove and is at risk of worse depletion."),
   ("A patient who is not retaining sodium",
    "Without sodium retention there is little sodium to remove, so a thiazide offers little and adds risk.")], 25),

Q("Thiazides in hypertension", IO_MOA, "mechanism",
  "Which short-term mechanism lowers blood pressure with thiazides?",
  ("Less blood volume and cardiac output",
   "In the short term thiazides lower blood pressure by decreasing blood volume and cardiac output."),
  [("Direct vasodilation of arterioles",
    "Direct vasorelaxation is the chronic effect that lowers total peripheral resistance; the short-term mechanism is less blood volume and cardiac output."),
   ("Increased renin release",
    "Renin rises as a reflex and works against the drug; the short-term mechanism is less blood volume and cardiac output."),
   ("Blocked beta receptors",
    "Thiazides do not block beta receptors; the short-term mechanism is less blood volume and cardiac output.")], 25),

Q("Thiazides in hypertension", IO_MOA, "mechanism",
  "Which mechanism accounts for the chronic blood pressure effect of thiazides?",
  ("Lower total peripheral resistance",
   "Chronically thiazides have direct vasorelaxant effects that lower total peripheral resistance, while volume and cardiac output return toward baseline."),
  [("Persistently lower blood volume",
    "Lower blood volume is the short-term effect; the chronic effect is lower total peripheral resistance."),
   ("Persistently lower cardiac output",
    "Lower cardiac output is the short-term effect; the chronic effect is lower total peripheral resistance."),
   ("Higher vascular responsiveness to norepinephrine",
    "Responsiveness to norepinephrine falls chronically; the chronic effect is lower total peripheral resistance.")], 25),

Q("Thiazides in hypertension", IO_IND, "indication",
  "Which of these is an indication for a thiazide diuretic?",
  ("Hypertension",
   "Hypertension is the leading indication for thiazides, which lower blood pressure by short-term volume loss and a chronic fall in peripheral resistance."),
  [("Acute pulmonary edema",
    "Acute pulmonary edema needs a rapid, potent loop diuretic; thiazides are modest diuretics used for hypertension, heart failure and calcium stones."),
   ("Hypokalemia",
    "Hypokalemia is an adverse effect of thiazides, not an indication."),
   ("Gout",
    "Thiazides raise uric acid and can cause gout, so gout is not an indication.")], 24),

# ---- adverse effects -------------------------------------------------------------------------
Q("Thiazide adverse effects", IO_AE, "adverse effect",
  "Which acid-base disturbance can thiazides cause?",
  ("Metabolic alkalosis",
   "Thiazides contract the extracellular fluid and produce a metabolic alkalosis."),
  [("Metabolic acidosis",
    "Metabolic acidosis is the carbonic anhydrase inhibitor effect; thiazides cause metabolic alkalosis."),
   ("Respiratory acidosis",
    "Respiratory acidosis is not a thiazide effect; contracted extracellular fluid produces a metabolic alkalosis."),
   ("Respiratory alkalosis",
    "Respiratory alkalosis is not a thiazide effect; contracted extracellular fluid produces a metabolic alkalosis.")], 26),

Q("Thiazide adverse effects", IO_AE, "adverse effect",
  "A patient on a thiazide develops a painful, swollen first metatarsophalangeal joint. Which adverse effect is this?",
  ("Hyperuricemia causing gout",
   "Thiazides cause hyperuricemia, which can lead to gout."),
  [("Hypercalcemia causing a stone",
    "Hypercalcemia does not cause an acutely inflamed toe joint; the picture is gout from hyperuricemia."),
   ("Hypokalemia causing weakness",
    "Hypokalemia causes weakness and arrhythmias, not an acutely painful joint; the picture is gout from hyperuricemia."),
   ("Photosensitivity causing a rash",
    "Photosensitivity affects sun-exposed skin, not a single joint; the picture is gout from hyperuricemia.")], 26),

Q("Thiazide adverse effects", IO_AE, "adverse effect",
  "Which preexisting condition makes a thiazide a poor choice because it can flare?",
  ("Gout",
   "Thiazides cause hyperuricemia, which can precipitate gout, so a history of gout argues against them."),
  [("Hypertension",
    "Hypertension is the leading indication for thiazides, not a reason to avoid them."),
   ("Calcium oxalate kidney stones",
    "Calcium oxalate stones are an indication, because thiazides lower urinary calcium."),
   ("Cirrhosis with edema",
    "Cirrhosis is a listed indication for a thiazide rather than a reason to avoid it.")], 26),

Q("Thiazide adverse effects", IO_AE, "adverse effect",
  "Which electrolyte disturbance from thiazides contributes to cardiac arrhythmia risk?",
  ("Hypokalemia",
   "Thiazides increase potassium excretion, and hypokalemia, a listed adverse effect, predisposes to cardiac arrhythmias."),
  [("Hyperkalemia",
    "Thiazides waste potassium and do not cause hyperkalemia; the disturbance is hypokalemia."),
   ("Hyperuricemia",
    "Hyperuricemia is an adverse effect of thiazides, but it causes gout rather than arrhythmias; the arrhythmia-prone electrolyte loss is hypokalemia."),
   ("Hypermagnesemia",
    "Thiazides increase magnesium excretion, so magnesium falls; the arrhythmia-prone disturbance is hypokalemia.")], 26),

Q("Thiazide adverse effects", IO_AE, "adverse effect",
  "Why can thiazides raise blood glucose?",
  ("They decrease insulin secretion",
   "Thiazides decrease glucose tolerance by decreasing insulin secretion, partly through increased sympathetic activity."),
  [("They increase insulin secretion",
    "Insulin secretion falls with thiazides, which is why glucose tolerance worsens."),
   ("They increase renal glucose reabsorption",
    "The listed mechanism is decreased insulin secretion, not altered renal glucose handling."),
   ("They block glucagon release",
    "Blocking glucagon would lower glucose; the glucose rise comes from decreased insulin secretion.")], 27),

Q("Thiazide adverse effects", IO_PROT, "monitoring",
  "Which laboratory value is the diabetes-specific concern when a patient with diabetes starts a thiazide?",
  ("Blood glucose",
   "Thiazides decrease glucose tolerance and insulin secretion, so blood glucose can rise and should be monitored."),
  [("Platelet count",
    "Thiazides are not listed as affecting platelets; the diabetes-specific concern is a rise in blood glucose."),
   ("Serum bilirubin",
    "Thiazides are not listed as affecting bilirubin; the diabetes-specific concern is a rise in blood glucose."),
   ("Serum amylase",
    "Thiazides are not listed as affecting amylase; the diabetes-specific concern is a rise in blood glucose.")], 27),

Q("Thiazide adverse effects", IO_AE, "adverse effect",
  "Which change in low-density lipoprotein cholesterol can thiazides cause?",
  ("An increase",
   "Thiazides can increase low-density lipoprotein cholesterol, a hyperlipidemia effect."),
  [("A decrease",
    "Thiazides raise rather than lower low-density lipoprotein cholesterol."),
   ("No effect at any dose",
    "Hyperlipidemia, including a rise in low-density lipoprotein cholesterol, is a listed adverse effect."),
   ("A selective rise in high-density lipoprotein",
    "The listed effect is a rise in low-density lipoprotein cholesterol, not a selective rise in high-density lipoprotein.")], 27),

Q("Thiazide adverse effects", IO_AE, "adverse effect",
  "A patient on hydrochlorothiazide develops a sunburn after brief sun exposure. Which adverse effect is this?",
  ("Photosensitivity",
   "Photosensitivity and skin rashes are listed adverse effects of thiazides."),
  [("Hyperuricemia",
    "Hyperuricemia leads to gout, not an abnormal reaction of the skin to sunlight."),
   ("Hypercalcemia",
    "Hypercalcemia does not cause skin reactions to sunlight; the cause is photosensitivity."),
   ("Contraction alkalosis",
    "Contraction alkalosis is an acid-base change, not a skin reaction to sunlight.")], 27),

Q("Thiazide adverse effects", IO_AE, "adverse effect",
  "Which group of nonspecific symptoms can occur with thiazides?",
  ("Dizziness, headaches and weakness",
   "Dizziness, headaches, weakness and restlessness are nonspecific adverse effects of thiazides."),
  [("Tinnitus, vertigo and hearing loss",
    "Ototoxicity is a loop diuretic adverse effect; the nonspecific thiazide symptoms are dizziness, headaches, weakness and restlessness."),
   ("Gynecomastia and menstrual irregularity",
    "Those are hormonal effects of spironolactone; the thiazide symptoms are dizziness, headaches, weakness and restlessness."),
   ("Yellow vision, nausea and halos",
    "Those are signs of digoxin toxicity; the thiazide symptoms are dizziness, headaches, weakness and restlessness.")], 27),

Q("Thiazide adverse effects", IO_AE, "adverse effect",
  "Which pair of adverse effects can occur with thiazides?",
  ("Sexual dysfunction and constipation",
   "Sexual dysfunction and constipation are both adverse effects of thiazides."),
  [("Sexual dysfunction and gingival overgrowth",
    "Gingival overgrowth comes from drugs such as phenytoin and calcium channel blockers; the thiazide pair is sexual dysfunction and constipation."),
   ("Gynecomastia and constipation",
    "Gynecomastia is a spironolactone effect; the thiazide pair is sexual dysfunction and constipation."),
   ("Hyperkalemia and diarrhea",
    "Thiazides cause hypokalemia, not hyperkalemia; the pair is sexual dysfunction and constipation.")], 28),

Q("Thiazide adverse effects", IO_AE, "adverse effect",
  "Which acute change in renal function can thiazides cause?",
  ("A decrease in glomerular filtration rate",
   "Thiazides decrease the glomerular filtration rate acutely, mostly through volume depletion."),
  [("An increase in glomerular filtration rate",
    "Thiazides lower the filtration rate acutely rather than raise it."),
   ("Complete loss of urine output",
    "Thiazides increase urine output; the acute renal change is a decrease in glomerular filtration rate."),
   ("Permanent tubular necrosis",
    "The acute change is a decrease in glomerular filtration rate, usually from volume depletion, not tubular necrosis.")], 23),

# ---- renal function and metolazone -----------------------------------------------------------
Q("Thiazides, kidney function and interactions", IO_CLASS, "drug choice",
  "Which diuretic keeps its effect at a low creatinine clearance?",
  ("Metolazone",
   "Metolazone is effective at lower creatinine clearance rates, unlike the other thiazides."),
  [("Hydrochlorothiazide",
    "Hydrochlorothiazide is classically taught to lose its effect at a low creatinine clearance; metolazone is the thiazide-type agent that remains effective."),
   ("Chlorothiazide",
    "Chlorothiazide is classically taught to lose its effect at a low creatinine clearance; metolazone is the thiazide-type agent that remains effective."),
   ("Amiloride",
    "Amiloride is only a modest diuretic whose main concern is hyperkalemia; metolazone is the thiazide-type agent that remains effective.")], 28),

# ---- interactions ----------------------------------------------------------------------------
Q("Thiazides, kidney function and interactions", IO_INTER, "interaction",
  "Why do nonsteroidal anti-inflammatory drugs weaken the effect of thiazides?",
  ("They block the prostaglandins that aid natriuresis",
   "Nonsteroidal anti-inflammatory drugs block prostaglandins, which attenuates the natriuretic action of thiazides."),
  [("They induce thiazide metabolism",
    "The listed mechanism is blocked prostaglandins attenuating natriuresis, not enzyme induction."),
   ("They bind thiazides in the gut",
    "The listed mechanism is blocked prostaglandins attenuating natriuresis, not binding in the gut."),
   ("They increase thiazide excretion into urine",
    "The listed mechanism is blocked prostaglandins attenuating natriuresis, not faster excretion.")], 29),

Q("Thiazides, kidney function and interactions", IO_INTER, "interaction",
  "Which drug does a thiazide put at higher risk of toxicity through its effect on potassium?",
  ("Digoxin",
   "Thiazides lower potassium, which increases digoxin (digitalis) toxicity."),
  [("Warfarin",
    "Warfarin is not described as becoming toxic through thiazide-induced potassium loss; digoxin is."),
   ("Levothyroxine",
    "Levothyroxine is not made toxic by potassium loss; digoxin toxicity is increased by the potassium loss."),
   ("Metformin",
    "Metformin is not made toxic by potassium loss; digoxin toxicity is.")], 29),

Q("Thiazides, kidney function and interactions", IO_PROT, "monitoring",
  "When a patient takes digoxin and a thiazide, which serum potassium level should be maintained?",
  ("Above 4.0 milliequivalents per liter",
   "To limit digoxin toxicity with a thiazide, the potassium level should be kept above 4.0 milliequivalents per liter."),
  [("Between 3.0 and 3.5 milliequivalents per liter",
    "A potassium level that low would promote digoxin toxicity; the level should be above 4.0 milliequivalents per liter."),
   ("Below 3.5 milliequivalents per liter",
    "Low potassium raises digoxin toxicity; the level to maintain is above 4.0 milliequivalents per liter."),
   ("Above 6.0 milliequivalents per liter",
    "That is hyperkalemia and dangerous; the level to maintain is above 4.0 milliequivalents per liter, not extremely high.")], 29),

Q("Thiazides in hypertension", IO_IND, "drug choice",
  "Which diuretic class is preferred, in low doses, for chronic hypertension?",
  ("Thiazide diuretics",
   "Low-dose thiazides are preferred for hypertension, working through short-term volume loss and a chronic fall in peripheral resistance."),
  [("Loop diuretics",
    "Loops act briefly and are blunted by compensation; low-dose thiazides are the diuretics preferred for chronic hypertension."),
   ("Carbonic anhydrase inhibitors",
    "Carbonic anhydrase inhibitors are weak diuretics with a waning effect; low-dose thiazides are preferred for hypertension."),
   ("Potassium-sparing diuretics",
    "Potassium-sparing diuretics are weak and mostly used in combination with other agents; low-dose thiazides are preferred for hypertension.")], 25),

Q("Thiazide adverse effects", IO_AE, "adverse effect",
  "A patient on a thiazide is dizzy on standing with a falling blood pressure and dry mouth. Which adverse effect is most likely?",
  ("Volume depletion",
   "Excess salt and water loss leaves the patient volume depleted, which triggers reflex responses and orthostatic symptoms."),
  [("Hyperuricemia",
    "Hyperuricemia leads to gout and does not explain orthostatic dizziness; this picture is volume depletion."),
   ("Hypercalcemia",
    "Hypercalcemia does not cause orthostasis with dry mouth; this picture is volume depletion."),
   ("Photosensitivity",
    "Photosensitivity is a skin reaction to sunlight; orthostatic dizziness with dry mouth is volume depletion.")], 26),

Q("Thiazide adverse effects", IO_EDU, "education",
  "Which statement is appropriate counseling for a patient starting hydrochlorothiazide?",
  ("Use sun protection against photosensitivity",
   "Photosensitivity is a listed adverse effect, so sun protection is appropriate counseling."),
  [("Stop the drug when urine output increases",
    "Increased urine output is the expected action and not a reason to stop; the counseling point is sun protection for photosensitivity."),
   ("Expect blood glucose to fall",
    "Thiazides tend to raise blood glucose by decreasing insulin secretion; the counseling point is sun protection for photosensitivity."),
   ("Expect uric acid to fall",
    "Thiazides raise uric acid and can cause gout; the counseling point is sun protection for photosensitivity.")], 27),

]
