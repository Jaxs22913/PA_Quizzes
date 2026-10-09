# -*- coding: utf-8 -*-
"""Cram-sheet topics for Pharmacology I Exam 3, Lecture 9 (Diuretics and Heart Failure Drugs; added 2026-09-30).

Imported by build_pharm_e3_cram.py. Same rules as the Exam 2 cram sheet: slide facts only
(Diuretics and Heart Failure Drugs.pptx), no milligram doses, truth wins where the deck is wrong
(rows marked FLAG say what the slide says and what is true), stars from Dr. Wood's recording.

VERIFICATION. Each row is built with R(label, html, slide(s), verify[, quotes]); the build step proves
every `verify` substring appears on the slide it cites (pharm_e3_lib.slide_text, which includes the
picture-slide text in pharm_e3/ocr.json) and every `quotes` substring appears in the recording transcript.
`slide` may be an int, or a list of (slide, [verify...]) pairs when a row draws on several slides.
A star only sets weight; no star adds a fact the deck lacks.
"""
REG = []   # (topic id, label, [(slide, [verify])], [quotes])


def R(label, html, slide=None, verify=(), quotes=()):
    if slide is None:
        pairs = []
    elif isinstance(slide, int):
        pairs = [(slide, list(verify))]
    else:
        pairs = [(s, list(v)) for s, v in slide]
    REG.append((label, pairs, list(quotes)))
    return [label, html]


T = []


def topic(tid, label, color, rows):
    for r in rows:
        pass
    T.append({"id": tid, "label": label, "color": color, "rows": rows})


# ----------------------------------------------------------------------------------------------
topic("hf-rules", "Diuretics &amp; heart failure &middot; what he stressed", "#8c1d12", [
 R("&#9733;&#9733; Mortality or symptoms?",
   "His standing rule for this whole lecture: <b>good for MORTALITY &rarr; the patient should be on it no matter what; good only for SYMPTOMS &rarr; may not be needed all the time.</b> "
   "<b>Symptoms only:</b> diuretics and digoxin. <b>Survival:</b> angiotensin-converting enzyme inhibitors (or angiotensin receptor blockers), the three beta blockers, aldosterone antagonists in advanced failure, sacubitril-valsartan, sodium-glucose cotransporter 2 inhibitors.",
   [(53, ["No evidence to show they decrease progression or mortality"]), (66, ["NO SURVIVAL BENEFIT"]), (54, ["Decreased mortality"])],
   quotes=["if it's good for mortality reasons that means you want the patient on it no matter what"]),
 R("&#9733;&#9733; Know every drug's effect on potassium",
   "&ldquo;You can kill somebody very easily with potassium.&rdquo; <b>LOWER it:</b> loop diuretics, thiazides, carbonic anhydrase inhibitors. <b>RAISE it:</b> potassium-sparing diuretics, aldosterone antagonists, angiotensin-converting enzyme inhibitors, sacubitril-valsartan. Several drugs on one patient: work out which way the total falls.",
   [(13, ["Increase K excretion"]), (22, ["Increased K and Mg excretion"]), (43, ["Potassium depletion"]), (33, ["Hyperkalemia"]), (38, ["Hyperkalemia"]), (56, ["Elevation of serum potassium"]), (81, ["hyperkalemia"])],
   quotes=["you can kill somebody very easily with potassium"]),
 R("&#9733; Where salt goes, water follows",
   "Diuretics work by blocking sodium (and usually chloride) reabsorption somewhere along the nephron, and water leaves with it. Too much fluid: volume overload and pulmonary edema. Too little: volume depletion and cardiovascular collapse.",
   4, ["Too much = volume overload, pulmonary edema", "Too little = volume depletion, CV collapse"],
   quotes=["wherever salt goes water wants to follow"]),
 R("&#9733; Digoxin level",
   "Digoxin has a very narrow therapeutic index and its level is checked. The slide gives a target range; he said he is <b>probably not going to quiz the specific level</b>. Know the narrow index, not the number.",
   65, ["Target levels"], quotes=["i'm probably not going to quiz you specifically on the level"]),
 R("&#9733; Xanthopsia is the digoxin clue",
   "Yellow-green vision with halos around lights is the classic clue to digoxin toxicity; in his words it is &ldquo;pathognomonic,&rdquo; nothing else does that. (Ivabradine also causes halos and brightness, but without the yellow-green tint.) It means check a level right away.",
   68, ["Xanthopsia", "Yellow-green halos"], quotes=["like there's nothing else that does that"]),
 R("&#9733; Heart failure decision shape",
   "His rule of thumb: hypertensive patient in decompensated failure &rarr; <b>milrinone</b> (it dilates vessels). Hypotensive patient &rarr; <b>dobutamine or dopamine</b>. Ask what the blood pressure is.",
   [(75, ["Decreased afterload"]), (77, ["Dobutamine"])], quotes=["if they're hypertensive then like milrinone works better"]),
 R("Doses",
   "This site leaves milligram amounts out; doses are not tested in this course, per the earlier lectures. Timings, routes and clinical thresholds are kept."),
])

# ----------------------------------------------------------------------------------------------
topic("hf-nephron", "Diuretics &middot; the nephron and where each class works", "#2f4f6b", [
 R("Why diuretics are dangerous",
   "<b>Diuretic</b> = a drug that increases urine flow and/or sodium chloride excretion. A sustained imbalance of sodium chloride intake against loss is fatal: too much gives volume overload and pulmonary edema; too little gives volume depletion and cardiovascular collapse.",
   4, ["Drugs that", "Sustained imbalance between Na+/Cl- intake or loss is fatal"]),
 R("&#9733; Diuretic braking",
   "The kidneys receive about 22% of the cardiac output and fight back against volume loss: <b>sympathetic nervous system and renin-angiotensin-aldosterone system activation, lower blood pressure (less pressure natriuresis), antidiuretic hormone up, renal cell hypertrophy.</b> He called the kidneys &ldquo;divas.&rdquo; This is why diuretics show <b>synergy with angiotensin-converting enzyme inhibitors and calcium channel blockers</b>, which blunt those compensations.",
   5, ["Diuretic braking", "Activation of SNS and RAAS", "Renal cell hypertrophy"],
   quotes=["that's why you see synergy between things like ace inhibitors and diuretics"]),
 R("Proximal tubule",
   "<b>60 to 70% of the filtrate is reabsorbed here</b> (glucose, amino acids, organic solutes; weak acids and bases are secreted into the lumen). <b>Carbonic anhydrase inhibitors work here.</b>",
   [(8, ["60-70 % of filtrate reabsorbed", "Glucose, amino acids and organic solutes"]), (39, ["PCT"])]),
 R("Loop of Henle",
   "Concentrates the urine. <b>Descending limb: water leaves the lumen. Ascending limb: 25% of sodium reabsorbed, impermeable to water.</b> <b>Loop diuretics work here.</b>",
   9, ["Descending loop: water leaves lumen", "25% of Na+ reabsorbed, impermeable to water", "Loop diuretics work at this site"]),
 R("Distal tubule",
   "About <b>5% of sodium</b> reabsorbed. <b>Thiazide diuretics work here.</b>",
   10, ["~ 5 % of Na+ reabsorbed", "Site of Thiazide diuretics"]),
 R("Collecting duct",
   "<b>2 to 3% of sodium</b> reabsorbed; <b>aldosterone and antidiuretic hormone</b> act here (antidiuretic hormone opens the water channels). <b>Potassium-sparing diuretics work here.</b> Aldosterone adds sodium channels and pump activity, so sodium is reabsorbed and potassium lost.",
   [(11, ["2-3% of Na+ reabsorbed", "Aldosterone and ADH", "Site of Potassium sparing diuretics"]), (34, ["Na channel number"]), (30, ["ADH"])]),
 R("&#9733; Order of potency",
   "Loops (inhibit 20 to 25% of sodium chloride reabsorption) &gt; thiazides (up to 5%) &gt; potassium-sparing diuretics and aldosterone antagonists (2 to 3%) &gt; carbonic anhydrase inhibitors (the &ldquo;wimpiest&rdquo;; the early 5% fades to 1 to 3% after 3 to 5 days). He presented the classes in descending order of potency.",
   [(13, ["20-25 %"]), (22, ["up to 5%"]), (30, ["2-3%"]), (36, ["2-3 %"]), (39, ["Long term (after 3-5 days) effect is reduced to 1-3 %"])],
   quotes=["descending order of potency"]),
])

# ----------------------------------------------------------------------------------------------
topic("hf-loops", "Diuretics &middot; loop diuretics", "#1f6f5c", [
 R("&#9733; Agents and mechanism",
   "<b>Furosemide, bumetanide, torsemide, ethacrynic acid</b> (the one that breaks the naming pattern). They inhibit the <b>sodium-potassium-2 chloride carrier</b> on the luminal membrane of the <b>thick ascending limb</b>.",
   12, ["Furosemide", "Bumetanide", "Torsemide", "Ethacrynic acid", "Inhibit the Na-2Cl-K carrier on the luminal membrane of the thick ascending loop of Henle"]),
 R("Major actions",
   "Inhibit sodium chloride reabsorption by <b>20 to 25%</b>; urine output up to <b>4 liters a day</b>; <b>more potassium, calcium and magnesium excreted</b> &rarr; hypokalemia, hypocalcemia, hypomagnesemia.",
   13, ["Inhibit NaCl reabsorption by 20-25 %", "up to 4 liters/day", "Increase K excretion", "Increase Calcium and magnesium excretion"]),
 R("&#9733; Works when the kidneys do not",
   "<b>Loops remain effective when creatinine clearance is below 30 milliliters a minute.</b> Urine flow does not mean the kidneys are working well.",
   16, ["Loops effective in patients with creatinine clearance rates below 30 ml/min"],
   quotes=["just because the person's making urine does not mean their kidneys are functioning all that well"]),
 R("&#9733; Indications",
   "<b>Pulmonary edema, nephrotic syndrome, cirrhosis of the liver (ascites), hypercalcemia (an add-on to saline, which is the main treatment), heart failure, renal failure or insufficiency, hypertension</b> (volume-driven; not good for chronic hypertension).",
   17, ["Pulmonary edema", "Nephrotic syndrome", "Cirrhosis of the liver (Ascites)", "Hypercalcemia (used with saline)", "Heart failure", "Renal failure/insufficiency", "Hypertension"],
   quotes=["it's not going to be good for chronic hypertension"]),
 R("&#9733; Adverse effects",
   "<b>Volume depletion; hypokalemia (arrhythmias); hyperglycemia; contraction alkalosis; hyperuricemia (gout); ototoxicity</b> (the cochlea; classically hair-cell damage, though often reversible); <b>hyponatremia</b> (seizures); allergic reactions (rash, photosensitivity); <b>azotemia</b> (blood urea nitrogen rises). Loops are the most potent, so they carry the most of these.",
   18, ["Volume depletion", "Hypokalemia", "Hyperglycemia", "Contraction alkalosis", "Hyperuricemia", "Ototoxicity", "damages hair cells in cochlea", "Hyponatremia - seizures", "photosensitivity", "Azotemic"]),
 R("Why the side effects happen",
   "<b>Hyperglycemia:</b> low potassium impairs insulin release; catecholamine release; insulin resistance. <b>Gout:</b> volume contraction concentrates uric acid and less is excreted. <b>Metabolic alkalosis:</b> volume depletion plus enhanced hydrogen ion secretion (the major factor). <b>Mild hyperlipidemia</b> from sympathetic activity. Reflex <b>renin, aldosterone and antidiuretic hormone</b> rise.",
   [(14, ["Hypokalemia", "Impaired peripheral glucose uptake"]), (15, ["Uric acid", "Aldosterone", "Antidiuretic hormone"]), (16, ["Mild metabolic alkalosis", "Enhanced H+ ion secretion", "Mild hyperlipidemia"])]),
 R("Vasodilation",
   "Loops also dilate vessels: they stimulate <b>prostaglandin E2 (blocked by non-steroidal anti-inflammatory drugs)</b>, plus a direct muscle-relaxing effect of unknown mechanism.",
   14, ["Systemic vasodilator actions", "Stimulate prostaglandins (PGE2) (blocked by NSAIDS)"]),
 R("&#9733; Interactions",
   "<b>Non-steroidal anti-inflammatory drugs</b> blunt the natriuretic and blood pressure response &middot; <b>aminoglycosides</b> potentiate ototoxicity &middot; <b>warfarin</b> competes for plasma protein binding &middot; <b>lithium</b> clearance falls and toxicity rises &middot; <b>digitalis</b>: hypokalemia plus hypomagnesemia gives arrhythmias.",
   19, ["NSAIDS", "Aminoglycosides", "Warfarin", "Lithium", "Digitalis"]),
 R("FLAG: boxed warning",
   "<b>FDA boxed warning, not on the slide:</b> furosemide, bumetanide and ethacrynic acid carry a boxed warning for profound diuresis with water and electrolyte depletion when given in excess. Torsemide does not.",
   12, ["Furosemide", "Bumetanide", "Ethacrynic acid"]),
])

# ----------------------------------------------------------------------------------------------
topic("hf-thiazides", "Diuretics &middot; thiazides", "#4a4f8c", [
 R("&#9733; Agents and mechanism",
   "<b>Chlorothiazide, hydrochlorothiazide, chlorthalidone, metolazone, indapamide.</b> They inhibit the <b>sodium/chloride transporter in the distal convoluted tubule</b> (major action).",
   [(20, ["Chlorothiazide", "Hydrochlorothiazide", "Chlorthalidone", "Metolazone", "Indapamide"]), (21, ["Inhibit Na/CL transporter in luminal membrane of DCT"])]),
 R("Major actions",
   "Inhibit up to <b>5%</b> of filtered sodium chloride; urine output <b>1 to 2 liters a day</b>; <b>more potassium and magnesium excreted; LESS calcium excreted</b> (more calcium reabsorbed in the proximal and distal tubules). Acutely lower the glomerular filtration rate.",
   [(22, ["up to 5%", "Increase urine output (1-2 liters/day)", "Increased K and Mg excretion", "Decreased renal calcium excretion"]), (23, ["Decrease GFR acutely"])]),
 R("&#9733; The calcium paradox",
   "Thiazides <b>keep calcium from being excreted</b>, so they help patients with <b>calcium oxalate kidney stones</b> yet can cause a small rise in <b>serum calcium</b>. Less calcium in the urine means less to crystallize. Loops do the opposite.",
   [(24, ["renal calcium stones (calcium oxalate)"]), (27, ["Hypercalcemia"])],
   quotes=["it sounds a little like counterintuitive but it actually does work"]),
 R("&#9733; Hypertension",
   "Cheap, old and well tolerated. He described them as a useful second- or third-line <b>add-on</b> (current hypertension guidelines still list thiazides among first-line choices). Works best in <b>elderly patients, African American patients and sodium-retentive states</b>. Short term: lower blood volume and cardiac output; chronic: vessel relaxation, less sodium &ldquo;waterlogging&rdquo; of vessel walls, lower total peripheral resistance. <b>Low-dose thiazides are preferred</b>, with few adverse effects.",
   25, ["Hypertension", "Works best in 1) elderly, 2) obese, 3) African Americans, 4) sodium retentive states", "Decrease blood volume - short term", "Low dose thiazides preferred for hypertension, few adverse effects"],
   quotes=["they used to be but they can be maybe as a useful like maybe second or third line kind of add-on"]),
 R("Other indications",
   "Hypertension, renal failure, cirrhosis of the liver, congestive heart failure, renal calcium stones.",
   24, ["Hypertension", "Renal failure", "Cirrhosis of liver", "Congestive heart failure"]),
 R("&#9733; Adverse effects",
   "Volume depletion with reflex sympathetic and renin-angiotensin-aldosterone activation; <b>hypokalemia; metabolic alkalosis; hyperuricemia (gout); hyperglycemia (less insulin); hypercalcemia; hyperlipidemia</b> (a modest rise in low-density lipoprotein); rash, <b>photosensitivity</b>; dizziness, headache, weakness, restlessness; <b>sexual dysfunction; constipation</b>. Much of the loop list, only milder; the differences are that thiazides RAISE calcium and are not ototoxic.",
   [(26, ["Volume depletion", "Hypokalemia", "Metabolic alkalosis", "Hyperuricemia - gout"]), (27, ["Hyperglycemia", "Hypercalcemia", "Hyperlipidema", "Photosensitivity", "Dizziness, headaches, weakness, restlessness"]), (28, ["Sexual dysfunction", "Constipation"])]),
 R("&#9733;&#9733; Metolazone",
   "Thiazides lose effect at low creatinine clearance, but <b>metolazone still works</b>. His mnemonic: <b>&ldquo;metolazone could make a rock pee&rdquo;</b>. (FLAG, see the last topic: do not treat &ldquo;thiazides do not work in kidney failure&rdquo; as absolute.)",
   28, ["Metolazone effective at lower clearance rates"],
   quotes=["metolazone could make a rock p"]),
 R("&#9733; Interactions",
   "<b>Non-steroidal anti-inflammatory drugs</b> block prostaglandins and weaken the natriuretic action. <b>Digitalis toxicity</b> rises with potassium loss: keep potassium above 4.0 milliequivalents per liter.",
   29, ["NSAIDS - block PG's attenuate natriuretic actions", "Increase digitalis toxicity", "K+ levels should be > 4.0"]),
])

# ----------------------------------------------------------------------------------------------
topic("hf-kspare", "Diuretics &middot; potassium-sparing and aldosterone antagonists", "#8c2f3a", [
 R("&#9733; Potassium-sparing: agents and mechanism",
   "<b>Amiloride and triamterene</b> <b>block luminal sodium channels</b> in the collecting duct, inhibiting 2 to 3% of sodium chloride reabsorption and <b>decreasing the gradient for potassium secretion</b>. Modest increase in urine flow. Combination products with hydrochlorothiazide exist.",
   [(30, ["Block luminal sodium channels", "Inhibit 2-3% of NaCl reabsorption", "Decrease gradient for K secretion", "Modest increase in urine flow"]), (31, ["Amiloride", "Triamterene", "Combinations with hydrochlorothiazide"])]),
 R("Potassium-sparing: use",
   "Same indications as the others but <b>much less natriuretic and diuretic effect</b>; <b>most often combined with another diuretic or an antihypertensive</b>. A loop plus a potassium-sparing drug offsets the potassium loss.",
   32, ["Same as others but much less natriuretic and diuretic effects", "Most often used in combination with other diuretics or antihypertensive drugs"],
   quotes=["to offset that potassium action to a degree"]),
 R("&#9733; Potassium-sparing: adverse effects",
   "<b>Hyperkalemia</b> (the major difference from other diuretics); caution with <b>angiotensin-converting enzyme inhibitors, angiotensin blockers and potassium supplements</b>; glucose intolerance in diabetes; <b>megaloblastic anemia (triamterene)</b>; <b>azotemia (amiloride)</b>. Salt substitutes are usually <b>potassium chloride</b>, a hidden potassium source.",
   33, ["Hyperkalemia", "Caution with ACEI and Angiotensin blockers", "Caution with Potassium supplements", "Megaloblastic anemia", "Azotemia"],
   quotes=["that's usually potassium chloride"]),
 R("FLAG: boxed warning",
   "<b>FDA boxed warning, not on the slide:</b> amiloride and triamterene both carry a boxed warning for hyperkalemia.",
   31, ["Amiloride", "Triamterene"]),
 R("Aldosterone: normal action",
   "Aldosterone binds its receptor, moves to the nucleus and drives protein synthesis: <b>more sodium channels, more sodium-potassium pump activity, more energy production in the distal tubule</b>.",
   34, ["Binds to receptor translocated to nucleus", "Na channel number in membrane", "Na/K-ATPase"]),
 R("&#9733; Aldosterone antagonists: agents and mechanism",
   "<b>Spironolactone, eplerenone.</b> They <b>bind the steroid receptor but do not move to the nucleus</b>, so they work best when aldosterone is high. Block 2 to 3% of sodium chloride reabsorption and reduce potassium loss; modest effect on lipids, glucose and uric acid.",
   [(35, ["Spironolactone", "Eplerenone"]), (36, ["Binds to steroid receptor but does not translocate to nucleus", "Most effective when Aldosterone high", "Modest effect on lipid, glucose and uric acid levels"])]),
 R("&#9733; Aldosterone antagonists: indications",
   "<b>Primary aldosteronism, hypertension, heart failure, edematous conditions, cirrhosis (secondary hyperaldosteronism), nephrotic syndrome.</b> Heart failure is the big one: advanced (class III or IV) failure; see FLAG.",
   37, ["Primary Aldosteronism", "Hypertension", "CHF", "Edematous conditions", "Cirrhosis (secondary hyperaldosteronism)", "Nephrotic syndrome"],
   quotes=["the heart failure is the big one here"]),
 R("&#9733;&#9733; Aldosterone antagonists: adverse effects",
   "<b>Hyperkalemia and mild acidosis</b>; nausea, vomiting, gastrointestinal upset; <b>sex-hormone effects of spironolactone</b> (it blocks the androgen receptor; see FLAG) &rarr; <b>gynecomastia in men; menstrual irregularities in women</b> (the slide also lists testicular atrophy). <b>Eplerenone has less effect on androgen receptors</b>: switch to it if the patient complains of breast development or menstrual problems.",
   38, ["Hyperkalemia /mild acidosis", "Nausea/vomiting/GI upset", "Weak androgenic effects, partial agonist at testosterone receptors", "Gynecomastia and testicular atrophy in men", "Menstrual irregularities, Hirsutism in women", "Eplerenone has less effect on androgen receptors"],
   quotes=["that's much less of the androgenic activity"]),
])

# ----------------------------------------------------------------------------------------------
topic("hf-cai", "Diuretics &middot; carbonic anhydrase inhibitors", "#b8862f", [
 R("&#9733; Agents and mechanism",
   "<b>Acetazolamide, dichlorphenamide, methazolamide.</b> Inhibit carbonic anhydrase: <b>bicarbonate absorption in the proximal tubule falls by 80 to 90%</b>, less hydrogen ion production, less hydrogen/sodium exchange. Bicarbonate is trapped in the tubule and passed out (alkaline urine, a mild acidification of the patient).",
   [(39, ["Inhibit carbonic anhydrase", "HCO3 absorption in PCT by 80-90%", "H/Na exchange"]), (40, ["Acetazolamide", "Dichlorphenamide", "Methazolamide"])],
   quotes=["you're gonna trap the bicarbonate in the tubule"]),
 R("Weak and self-limiting",
   "Short term sodium and potassium excretion rises about 5%, but <b>after 3 to 5 days the effect shrinks to 1 to 3%</b> because the rest of the nephron compensates. The wimpiest diuretic.",
   39, ["Short term effect is to ↑ Na and K excretion 5%", "Long term (after 3-5 days) effect is reduced to 1-3 %"],
   quotes=["of the bunch they are the wimpiest"]),
 R("&#9733; Other uses",
   "<b>Glaucoma</b> (less bicarbonate in the ciliary body: dorzolamide, brinzolamide), <b>epilepsy</b> (metabolic acidosis, central nervous system effects), <b>mountain sickness</b> (acidifies the blood so the patient breathes faster).",
   42, ["Glaucoma", "Dorzolamide", "Brinzolamide", "Epilepsy", "Mountain sickness"]),
 R("&#9733; Adverse effects",
   "<b>Metabolic acidosis</b> (the opposite of the contraction alkalosis of other diuretics), <b>potassium depletion, drowsiness</b>.",
   43, ["Metabolic acidosis", "Potassium depletion", "Drowsiness"],
   quotes=["that's different than your other diuretics which typically cause more of like a contraction alkalosis"]),
])

# ----------------------------------------------------------------------------------------------
topic("hf-hf", "Heart failure &middot; types, compensation, non-drug care", "#7a4a9c", [
 R("Causes",
   "<b>Ischemic heart disease and myocardial infarction (50 to 60% of cases)</b>, hypertension, idiopathic dilated cardiomyopathy; other cardiomyopathies (alcoholic, viral, hypertrophic); drug induced.",
   45, ["Ischemic heart disease, MI", "50-60% of cases", "Hypertension", "Idiopathic dilated cardiomyopathy", "Drug induced"]),
 R("&#9733; Systolic dysfunction",
   "<b>Decreased contractility</b> (loss of muscle mass, left ventricular hypertrophy, dilated cardiomyopathies), assessed as a <b>reduced ejection fraction</b> (the slide says below 45%; current practice says 40% or less).",
   46, ["Decreased contractility", "Loss of myocardial muscle mass", "Assessed as reduced ejection fraction"]),
 R("&#9733; Diastolic dysfunction",
   "<b>Impaired relaxation:</b> thicker, stiffer ventricles; ischemia impairs removal of calcium back into the sarcoplasmic reticulum; less filling means less cardiac output. Symptoms with a <b>preserved ejection fraction</b>.",
   47, ["Impaired relaxation", "Thicker, stiffer ventricles relax less efficiently", "Impair removal of Ca from cytosol back into sarcoplasmic reticulum", "HF symptoms with preserved ejection fraction"]),
 R("Compensatory response",
   "<b>More preload</b> (sodium and water retention), <b>vasoconstriction</b>, <b>tachycardia and more contractility</b> (sympathetic activation), left ventricular hypertrophy. A vicious cycle that therapy has to interrupt.",
   [(48, ["Increased preload (through Na and water retention)", "Vasoconstriction", "Tachycardia and increased contractility", "Left ventricular hypertrophy"]), (49, ["Neuroendocrine activation", "H2O retention"])]),
 R("Precipitants of decompensation",
   "<b>Lack of compliance</b> (diet or medicines), uncontrolled hypertension, arrhythmias, inadequate therapy, inappropriate medicines or fluid overload; also acute anginal chest pain, pulmonary infection, emotional stress.",
   50, ["Lack of compliance", "Uncontrolled hypertension", "Cardiac arrhythmias", "Inadequate therapy", "Pulmonary infection", "Emotional stress"]),
 R("Non-drug therapy",
   "<b>Restrict dietary sodium and fluid</b> (the slide gives 1 to 3 grams of sodium and under 2 liters of fluid a day); physical activity may improve function.",
   51, ["Dietary sodium and fluid restriction", "Limit sodium intake to 1-3 g/day", "Limit fluids to < 2 L/day", "Physical activity may improve functional status"]),
])

# ----------------------------------------------------------------------------------------------
topic("hf-core", "Heart failure &middot; diuretics, ACE inhibitors, beta blockers", "#3d6b52", [
 R("&#9733;&#9733; Diuretics in heart failure",
   "<b>Loops are the mainstay</b>; thiazides are not potent enough for most patients. They cut sodium and water retention and so <b>preload</b>, for <b>symptomatic benefit only</b>: <b>no evidence they slow progression or lower mortality</b>, and <b>not mandatory</b> (some patients take them as needed). <b>Daily weights</b> detect fluid overload.",
   [(52, ["Not potent enough for most HF patients", "Mainstay of HF therapy", "Decreases sodium and water retention thus decreasing preload", "Monitoring patient's weight"]), (53, ["Diuretics are for symptomatic relief only", "No evidence to show they decrease progression or mortality", "Not mandatory therapy"])],
   quotes=["they may be instructed to take the loops"]),
 R("&#9733; Angiotensin-converting enzyme inhibitors: what they do",
   "<b>Lower preload, afterload and sympathetic activation; reduce left ventricular hypertrophy, dilation and remodeling; slow progression; lower mortality.</b> Hemodynamics, exercise tolerance, symptoms, admissions, progression and survival all improve. <b>Angiotensin-converting enzyme inhibitors or angiotensin receptor blockers have to be mandatory</b> in heart failure with reduced ejection fraction (a weak pumping heart; the slide does not name the type).",
   [(54, ["Decrease preload", "Decrease afterload", "Decrease sympathetic activation", "Decrease left ventricular hypertrophy, dilation, and remodeling", "Slows heart failure progression", "Decreased mortality"]), (55, ["Fewer hospital admissions", "Prolonged survival"])],
   quotes=["aces or arbs have to be mandatory for these patients"]),
 R("Angiotensin-converting enzyme inhibitor problems",
   "<b>Renal function impairment, hypotension, raised serum potassium, cough, angioedema.</b> Loops lower potassium, angiotensin-converting enzyme inhibitors raise it: monitor.",
   56, ["Impairment of renal function", "Hypotension", "Elevation of serum potassium", "Cough", "Angioedema"],
   quotes=["so we got a monitor for this"]),
 R("&#9733;&#9733; Beta blockers: only three",
   "Beta blockers were classically considered contraindicated in heart failure. The ones with a <b>mortality benefit</b> are <b>carvedilol, metoprolol succinate (the extended-release form) and bisoprolol</b>; the others have not shown it.",
   57, ["Classically considered contraindicated in heart failure", "Carvedilol", "Metoprolol succinate XL", "Bisoprolol"],
   quotes=["these three in particular have been found to be associated with reducing mortality"]),
 R("&#9733; Beta blockers: low and slow",
   "Patient <b>stable before starting</b>; in hospital preferred; <b>very low starting doses</b>; <b>titrate up slowly</b> (the slide says over 6 to 8 weeks total); monitor for worsening heart failure signs and symptoms. Heart rate and contractility fall, so a rushed start can decompensate the patient.",
   58, ["Patient should be stable prior to initiation", "In hospital preferred", "Start with very low doses", "Titrate up slowly over 6-8 weeks total", "Monitor for worsening HF signs and symptoms"],
   quotes=["low and slow"]),
 R("Beta blockers: benefit and place",
   "Better exercise tolerance, a higher ejection fraction, slower progression, fewer hospitalizations, less need for transplant, <b>lower mortality</b>. <b>First line in class II to IV heart failure; patients should be on an angiotensin-converting enzyme inhibitor AND a beta blocker irrespective of symptoms.</b>",
   [(59, ["Improved exercise tolerance", "Slowed disease progression", "Decreased need for transplant", "Decreased mortality"]), (60, ["First line therapy in Class II-IV heart failure", "irrespective of symptoms"])]),
])

# ----------------------------------------------------------------------------------------------
topic("hf-digoxin", "Heart failure &middot; digoxin", "#a8562f", [
 R("Structure and source",
   "<b>Lactone ring and steroid nucleus</b> are essential for activity; the sugar molecules influence absorption, half-life and metabolism.",
   61, ["Lactone ring and Steroid nucleus essential for activity", "Sugar molecules influence absorption, half-life and metabolism"]),
 R("&#9733; Mechanism",
   "<b>Inhibits the sodium-potassium ATPase</b> &rarr; intracellular sodium rises &rarr; calcium enters through the sodium/calcium exchanger &rarr; <b>force of contraction rises</b> (the older, inotropic mechanism). The newer one is neurohormonal: <b>less sympathetic and more parasympathetic activity, baroreflex resensitized, renin-angiotensin-aldosterone system down</b>, so the heart rate falls (more parasympathetic effect on the atrioventricular node) and cardiac output rises.",
   [(62, ["Digitalis inhibits Na+/K+ ATPase", "Fiber shortening"]), (63, ["Inotropic agent - older mechanism", "Neurohormonal - newer mechanism", "Resensitize baro-reflex"]), (64, ["parasympathetic activity in AV node"]), (65, ["Renin-Angiotensin-Aldosterone system"])]),
 R("&#9733; Narrow therapeutic index",
   "There is little gap between an effective and a toxic level, and it is <b>one of the few heart failure drugs whose level is checked</b>. Target range on the slide: 0.5 to 1 nanogram per milliliter; higher concentrations are associated with worse outcomes in heart failure. He will probably not quiz the number.",
   65, ["Target levels: 0.5-1 ng/mL", "Higher concentrations may be associated with worse outcomes"],
   quotes=["is one of the few um a few agents for heart failure we actually do levels"]),
 R("&#9733;&#9733; Benefit: symptoms, NOT survival",
   "Better symptoms, exercise tolerance and quality of life; <b>fewer hospitalizations; NO SURVIVAL BENEFIT</b>; no evidence of slowed disease progression. So it is <b>not mandatory</b> like angiotensin-converting enzyme inhibitors and beta blockers.",
   [(66, ["Improvement in symptoms", "Decreased number of hospitalizations", "NO SURVIVAL BENEFIT"]), (67, ["No evidence of slowed disease progression"])],
   quotes=["no survival benefits so it's going to be one of the kind of the trade-offs"]),
 R("&#9733; Place in therapy",
   "<b>Symptomatic patients already on optimal angiotensin-converting enzyme inhibitor/beta blocker and diuretic therapy</b>; can be used for <b>rate control in atrial fibrillation with heart failure</b>; considered in symptomatic systolic dysfunction. (FLAG: the slide says &ldquo;first line&rdquo; for the atrial fibrillation case; that is overstated.)",
   67, ["Primary use in symptomatic patients on optimal doses of ACE inhibitors/beta blockers and diuretics", "First line for patients with atrial fibrillation and HF for rate control properties", "Considered in patients with symptomatic HF and systolic dysfunction"]),
 R("&#9733; Toxicity",
   "<b>Gastrointestinal:</b> anorexia, nausea. <b>Visual:</b> blurred vision, photophobia, <b>xanthopsia, yellow-green halos around lights</b>. <b>Central:</b> delirium, fatigue, confusion, dizziness, abnormal dreams. <b>Cardiac:</b> nodal slowing (longer PR interval, shorter QT interval, depressed ST segment), <b>bradycardia</b>, digoxin-induced afterdepolarization (the tracing shows premature ventricular beats and ST depression).",
   [(68, ["GI - anorexia, nausea", "Visual disturbances", "Photophobia", "Xanthopsia", "Yellow-green halos"]), (69, ["Delirium", "Fatigue", "Confusion", "Abnormal dreams"]), (70, ["Nodal slowing", "Bradycardia", "Digoxin induced after depolarization"])]),
 R("&#9733;&#9733; Contraindications and risk factors",
   "<b>Advanced atrioventricular block; severe bradycardia or sick sinus syndrome; premature ventricular beats and ventricular tachycardia; Wolff-Parkinson-White syndrome.</b> Toxicity is more likely with <b>hypokalemia, hypomagnesemia and hypercalcemia</b>: loops and thiazides lower potassium and magnesium, so a patient on digoxin plus a diuretic needs electrolyte monitoring. (FLAG: slide 71 prints hyperkalemia; see the last topic.)",
   [(71, ["Advanced AV block", "Severe Bradycardia or sick sinus syndrome", "PVC's and ventricular tachycardia", "Hypomagnesaemia", "Hypercalcemia", "Wolf-Parkinson- White"]), (19, ["Digitalis - hypokalemic + hypomagnesemic - arrhythmias"])],
   quotes=["the big deal to watch for is the electrolytes"]),
 R("&#9733; Antidote: digoxin immune Fab",
   "An <b>antibody fragment made by immunizing healthy sheep</b> with digoxin coupled to human serum albumin; its <b>affinity for digoxin is higher than digoxin's affinity for the sodium-potassium ATPase</b>, so it rapidly reverses toxicity. It can <b>unmask</b> what digoxin was treating (atrial fibrillation or heart failure decompensation).",
   72, ["Digoxin Immune Fab", "immunization of healthy sheep with digoxin coupled to human serum albumin", "Affinity higher for Digoxin than affinity of digoxin and Na+K+ ATPase", "Rapidly reverse toxicity"],
   quotes=["it can unmask whatever that the"]),
])

# ----------------------------------------------------------------------------------------------
topic("hf-other", "Heart failure &middot; other agents", "#4a4f8c", [
 R("&#9733; Aldosterone antagonists in heart failure",
   "<b>Spironolactone lowers mortality in advanced (class III or IV) heart failure</b> (the slide says &ldquo;grade&rdquo;) by neurohormonal inhibition and slowed left ventricular remodeling. <b>Not eligible if potassium is above 5 or serum creatinine above 2.5.</b> Gynecomastia in men (about 10%; may respond to a lower dose); <b>eplerenone rarely causes gynecomastia</b>.",
   73, ["Mortality reduction in grade III or IV HF", "Patients not eligible if K > 5 or SCr > 2.5", "Gynecomastia in men ~10%", "Eplerenone", "No gynecomastia", "slowed remodeling of LV"],
   quotes=["they will be contraindicated if the potassium is too high"]),
 R("Milrinone and inamrinone",
   "<b>Phosphodiesterase type 3 inhibitors</b> (cyclic adenosine monophosphate up): direct stimulation of contraction <b>plus balanced arterial and venous dilation</b> &rarr; lower afterload, higher cardiac output. Approved for <b>short-term intravenous use in acute decompensated heart failure</b>; long-term use carries <b>higher mortality and morbidity than placebo</b>. Adverse: <b>thrombocytopenia (milrinone less), ventricular arrhythmias</b>.",
   [(74, ["Milrinone", "Inamrinone", "Cyclic AMP phosphodiesterase (III) inhibitors"]), (75, ["Inotropic as well as vasodilator actions", "Balanced arterial and venous dilation", "Decreased afterload", "Increased cardiac output"]), (76, ["Approved for short term IV use in acute decompensated heart failure", "Long term use is associated with higher mortality and morbidity", "Thrombocytopenia (Milrinone less)", "Ventricular arrhythmias"])],
   quotes=["you really just want to use it for short term"]),
 R("&#9733; Dobutamine and dopamine",
   "<b>Dobutamine: selective beta-1 agonist</b>, intravenous; stimulates force of contraction more than rate; short-term use to stabilize patients. <b>Dopamine</b>: intravenous, acts through dopamine and beta receptors. They vasodilate much less than milrinone, so they suit a <b>hypotensive</b> decompensation; milrinone suits a hypertensive one.",
   77, ["Dobutamine - selective beta 1 agonist", "stimulates force of contraction more than rate of contraction", "Short term use to stabilize patients", "Dopamine - IV infusions", "Actions through dopamine and beta receptors"],
   quotes=["if they're going to be hypotensive then something like a debutamine or dopamine tends to make more sense"]),
 R("&#9733; Ivabradine",
   "<b>Blocks the hyperpolarization-activated cyclic nucleotide-gated channel</b> (pacemaker current in the sinoatrial node): <b>lowers heart rate without affecting contractility.</b> For patients <b>maxed out on beta blockers</b> who are in <b>normal sinus rhythm with a heart rate above 70</b>; fewer hospitalizations and heart failure deaths. Adverse: <b>atrial fibrillation risk, symptomatic bradycardia, visual impairment (phosphenes, halos, may resolve)</b>. Contraindications resemble beta blockers: hypotension, heart block, pacemaker.",
   [(79, ["Hyperpolarization-activated cyclic nucleotide-gated (HCN) channel blocker", "Inhibits pacemaker current in SA node", "Reduces heart rate, doesn't affect contractility", "maxed out on beta blockers", "In NSR with HR > 70 bpm", "decrease hospitalization and HF related death"]), (80, ["Increase risk of atrial fibrillation", "Symptomatic bradycardia", "Visual impairment (phosphenes)", "Halos", "Similar contraindications to beta blockers", "Hypotension, heart block, pacemaker"])],
   quotes=["this just reduces the heart rate it doesn't affect the contractility"]),
 R("&#9733; Sacubitril-valsartan",
   "Sacubitril is a <b>neprilysin inhibitor</b> (neprilysin normally degrades natriuretic peptide, bradykinin and other vasoactive peptides): vasodilation, natriuresis, diuresis, less myocardial growth and fibrosis. Formulated with <b>valsartan</b>, an angiotensin receptor blocker. Reduces cardiovascular death and hospitalization. <b>Never with an angiotensin-converting enzyme inhibitor: 36-hour washout.</b> Common adverse: hypotension, hyperkalemia, cough, renal insufficiency.",
   81, ["Formulated with valsartan", "Neprilysin inhibitor", "Natriuretic peptide, bradykinin", "vasodilation, natriuresis, and diuresis", "Inhibits growth and fibrosis of myocardial tissue", "Don't use along with ACE inhibitor and give 36 hour washout period", "hypotension, hyperkalemia, cough, renal insufficiency"],
   quotes=["you would not want to use this with an ace inhibitor"]),
 R("FLAG: sacubitril-valsartan",
   "<b>FDA boxed warning, not on the slide:</b> fetal toxicity. A history of angioedema is also a contraindication.",
   81, ["Formulated with valsartan"]),
 R("&#9733; Sodium-glucose cotransporter 2 inhibitors",
   "<b>Dapagliflozin, empagliflozin.</b> For <b>stable chronic heart failure with reduced ejection fraction</b>: <b>reduce mortality and hospitalizations</b>. Originally for diabetes: the kidneys stop reabsorbing glucose. Risks: <b>hypotension and fungal infections of the genitourinary tract</b> (the slide says &ldquo;fungal urinary tract infections&rdquo;). A &ldquo;necessary add-on&rdquo; for heart failure patients.",
   82, ["Dapagliflozin", "Empagliflozin", "For stable, chronic HFrEF", "Reduces mortality and hospitalizations", "Originally for diabetes", "Causes kidneys to not reabsorb glucose", "hypotension and fungal UTIs"],
   quotes=["necessary add-on medications to patients"]),
])

# ----------------------------------------------------------------------------------------------
topic("hf-flags", "Deck versus truth &middot; learn the true version", "#8c1d12", [
 R("FLAG: digoxin and potassium",
   "Slide 71 lists <b>hyperkalemia</b> as a digoxin contraindication, and he said &ldquo;hyperkalemic&rdquo; once. Slides 19 and 29 (and the pharmacology) say the opposite: <b>hypokalemia, hypomagnesemia and hypercalcemia raise toxicity risk</b>. Learn hypokalemia.",
   [(71, ["Hyperkalemia", "Hypomagnesaemia", "Hypercalcemia"]), (19, ["Digitalis - hypokalemic + hypomagnesemic - arrhythmias"]), (29, ["Increase digitalis toxicity - K+ levels should be > 4.0"])]),
 R("FLAG: descending limb",
   "The descending limb is <b>permeable to water</b> (the slide: &ldquo;water leaves lumen&rdquo;); he misspoke once. The thick ascending limb is the impermeable one.",
   9, ["Descending loop: water leaves lumen", "Ascending loop"]),
 R("FLAG: thiazides and calcium",
   "Slide 24 lists hypercalcemia among thiazide indications. <b>Thiazides raise serum calcium and lower urinary calcium</b>: they treat calcium stones, not hypercalcemia (saline hydration is the main treatment, with a loop diuretic added).",
   [(24, ["Hypercalcemia/renal calcium stones"]), (27, ["Hypercalcemia"]), (17, ["Hypercalcemia (used with saline)"])]),
 R("FLAG: thiazides at low clearance",
   "Slide 28: thiazides are ineffective below a creatinine clearance of 30 to 40. Learn <b>metolazone works at low clearance</b>; do not memorize &ldquo;thiazides never work in kidney disease&rdquo; (newer trials show chlorthalidone works in advanced kidney disease).",
   28, ["Thiazides are ineffective at low creatinine clearance rates"]),
 R("FLAG: uric acid with thiazides",
   "Slide 23 says thiazides increase uric acid excretion acutely; slide 26 and the clinical picture are <b>hyperuricemia and gout</b>. Learn hyperuricemia.",
   [(23, ["Uric acid excretion acutely"]), (26, ["Hyperuricemia - gout"])]),
 R("FLAG: aldosterone antagonists and class",
   "Slide 37 says heart failure &ldquo;class IV&rdquo;; slide 73 says &ldquo;grade III or IV.&rdquo; Learn <b>advanced (class III or IV) heart failure</b>. The slide 36 lines on a 30 to 60 minute lag and on calcium excretion are not carried here.",
   [(37, ["CHF (class IV, symptoms at rest)"]), (73, ["grade III or IV"]), (36, ["30-60 minute lag time", "Calcium excretion"])]),
 R("FLAG: spironolactone and androgen receptors",
   "Slide 38 calls spironolactone a &ldquo;partial agonist at testosterone receptors&rdquo; with &ldquo;weak androgenic effects&rdquo; (he repeated the partial agonist wording). <b>Spironolactone actually BLOCKS (antagonizes) the androgen receptor</b>, which is why it causes gynecomastia and menstrual irregularities. <b>Hirsutism is not an adverse effect of it</b> (the slide lists it, but spironolactone is used to treat hirsutism): do not learn it as one.",
   38, ["partial agonist at testosterone receptors", "Menstrual irregularities, Hirsutism in women"]),
 R("FLAG: antidiuretic hormone and water",
   "Slide 10 says water movement in the distal tubule is controlled by aldosterone. <b>Aldosterone drives sodium and potassium handling; antidiuretic hormone controls the collecting duct water channels</b> (slides 11, 30, 34).",
   10, ["Water movement controlled by Aldosterone"]),
 R("FLAG: ejection fraction and weight numbers",
   "Reduced ejection fraction is now <b>40% or less</b> (slide 46 says below 45%). The weight gain of more than 1 pound a day (slide 52) is a teaching figure: <b>learn daily weights, and rapid gain means fluid</b>.",
   [(46, ["reduced ejection fraction (< 45%)"]), (52, ["> 1 lb/day over several days"])]),
 R("FLAG: dopamine and the kidney",
   "Slide 77 says dopamine infusions maintain renal function. Low-dose dopamine has not been shown to protect the kidneys; do not rely on that claim.",
   77, ["Dopamine - IV infusions maintain renal function"]),
 R("FLAG: carbonic anhydrase notes",
   "Slide 21 (thiazides have some carbonic anhydrase activity and phosphodiesterase inhibition at high doses) and slide 42 (head injury, less swelling) are not examined points: he said not to worry about the carbonic anhydrase action.",
   [(21, ["Some carbonic anhydrase activity"]), (42, ["Head injury"])],
   quotes=["don't worry so much about that"]),
 R("Other boxed warnings (not on the slides)",
   "<b>FDA boxed warnings not on the slides:</b> furosemide, bumetanide, ethacrynic acid (profound diuresis); amiloride, triamterene (hyperkalemia); sacubitril-valsartan (fetal toxicity); angiotensin-converting enzyme inhibitors (fetal toxicity); abrupt beta blocker withdrawal (metoprolol).",
   [(12, ["Furosemide"]), (31, ["Amiloride"]), (81, ["Sacubitril"]), (54, ["Decrease preload"]), (57, ["Metoprolol succinate XL"])]),
])

assert len({t["id"] for t in T}) == len(T), "duplicate topic id"
