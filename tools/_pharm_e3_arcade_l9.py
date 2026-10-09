# -*- coding: utf-8 -*-
"""Arcade decks for Pharmacology I Exam 3, Lecture 9 (Diuretics and Heart Failure Drugs), drafted 2026-09-30.

Imported by add_pharm_e3_arcade.py. One deck per quiz topic (six, matching the Exam 3 topic quizzes), atomic
question -> short answer cards per [[arcade_content_policy]], deck facts only, no doses, US spelling,
abbreviations written out (a drug-name suffix or a chemical name is not an abbreviation).

Every card is written with C(question, answer, slide(s), verify...) so the adder can PROVE each card against
its slide (pharm_e3_lib.slide_text, picture-slide text included): a card whose verify substring is not on
the slide cannot ship. A card may carry `tf=` quote substrings checked against the recording transcript.

Weighting follows Dr. McInnis: indications, patient education, adverse effects and contraindications over
mechanism. Deliberately NOT carried (slide-versus-truth conflicts, descoped or off-slide): the digoxin target
level (he will not quiz it) and hyperkalemia as a digoxin risk (slide 71 is wrong: hypokalemia is the risk),
"first line" digoxin for atrial fibrillation, thiazide acute uric acid excretion, thiazide hypercalcemia as an
indication, aldosterone antagonists "class IV only", the ejection fraction percentage, the weight-gain number,
dopamine "maintains renal function", the carbonic anhydrase activity of thiazides, head injury, the 30 to 60
minute lag of aldosterone antagonists, and every dose or strength.

NOT YET IN arcade.js: the integrator runs `python3 tools/add_pharm_e3_arcade.py`.
"""
REG = []     # (deck id, question, [(slide, [verify])], [quotes])


def C(deck, q, a, slide, verify=(), tf=()):
    pairs = [(slide, list(verify))] if isinstance(slide, int) else [(s, list(v)) for s, v in slide]
    REG.append((deck, q, pairs, list(tf)))
    return (q, a)


DROP_ICON = '<path d="M12 3s5 6 5 9a5 5 0 0 1-10 0c0-3 5-9 5-9z"/>'
HF_ICON = ('<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>'
           '<path d="M9 11l2 2 4-4"/>')

LOOP, THIAZ, KSPARE = "pharm-diuretic-loops", "pharm-diuretic-thiazides", "pharm-diuretic-ksparing"
HFCORE, DIGOX, HFOTHER = "pharm-hf-core", "pharm-hf-digoxin", "pharm-hf-other"

DECKS = [
 (LOOP, "The Nephron &amp; Loop Diuretics", "accent1", DROP_ICON, [
  # ---- the nephron
  C(LOOP, "Which nephron segment reabsorbs 60 to 70 percent of the filtrate?", "The proximal tubule.", 8, ["60-70 % of filtrate reabsorbed"]),
  C(LOOP, "Which diuretic class works in the proximal tubule?", "Carbonic anhydrase inhibitors.", 39, ["PCT"]),
  C(LOOP, "Which limb of the loop of Henle is impermeable to water?", "The ascending limb.", 9, ["Ascending loop: 25% of Na+ reabsorbed, impermeable to water"]),
  C(LOOP, "Where in the nephron do loop diuretics act?", "The thick ascending limb of the loop of Henle.", 12, ["thick ascending loop of Henle"]),
  C(LOOP, "Where in the nephron do thiazide diuretics act?", "The distal convoluted tubule.", [(10, ["Site of Thiazide diuretics"]), (21, ["DCT"])]),
  C(LOOP, "Where in the nephron do potassium-sparing diuretics act?", "The collecting duct.", 11, ["Site of Potassium sparing diuretics"]),
  C(LOOP, "Which two hormones act on the collecting duct?", "Aldosterone and antidiuretic hormone.", 11, ["Aldosterone and ADH"]),
  C(LOOP, "What do too much sodium chloride and water cause?", "Volume overload and pulmonary edema.", 4, ["Too much = volume overload, pulmonary edema"]),
  C(LOOP, "What does too little sodium chloride and water cause?", "Volume depletion and cardiovascular collapse.", 4, ["Too little = volume depletion, CV collapse"]),
  C(LOOP, "What is diuretic braking?", "Renal compensation, such as renin-angiotensin activation, that limits a diuretic's effect.", 5, ["Diuretic braking", "Activation of SNS and RAAS"],
    tf=["diuretic breaking"]),
  # ---- loops
  C(LOOP, "Which carrier do loop diuretics inhibit?", "The sodium-potassium-2 chloride carrier.", 12, ["Inhibit the Na-2Cl-K carrier"]),
  C(LOOP, "Name the four loop diuretics.", "Furosemide, bumetanide, torsemide and ethacrynic acid.", 12, ["Furosemide", "Bumetanide", "Torsemide", "Ethacrynic acid"]),
  C(LOOP, "Which loop diuretic does not end in -ide?", "Ethacrynic acid.", 12, ["Ethacrynic acid"], tf=["just to be difficult"]),
  C(LOOP, "Besides sodium, which three minerals do loop diuretics increase the excretion of?", "Potassium, calcium and magnesium.", 13, ["Increase K excretion", "Increase Calcium and magnesium excretion"]),
  C(LOOP, "Which diuretics still work when creatinine clearance is below 30 milliliters per minute?", "Loop diuretics.", 16, ["Loops effective in patients with creatinine clearance rates below 30"]),
  C(LOOP, "Which loop diuretic adverse effect can damage the cochlea of the inner ear?", "Ototoxicity.", 18, ["Ototoxicity", "damages hair cells in cochlea"]),
  C(LOOP, "Which acid-base disorder do loop diuretics cause?", "Contraction alkalosis.", 18, ["Contraction alkalosis"]),
  C(LOOP, "Loop diuretics raise which blood level, risking gout?", "Uric acid.", [(15, ["Uric acid"]), (18, ["Hyperuricemia - gout"])]),
  C(LOOP, "Which sodium disturbance from loop diuretics can cause seizures?", "Hyponatremia.", 18, ["Hyponatremia - seizures"]),
  C(LOOP, "Which blood glucose change can loop diuretics cause?", "Hyperglycemia.", 18, ["Hyperglycemia"]),
  C(LOOP, "Which laboratory value rises with loop-induced azotemia?", "Blood urea nitrogen.", 18, ["Azotemic"]),
  C(LOOP, "Which drug class blunts the natriuretic and blood pressure response to loops?", "Non-steroidal anti-inflammatory drugs.", 19, ["NSAIDS"]),
  C(LOOP, "Which antibiotic class potentiates loop diuretic ototoxicity?", "Aminoglycosides.", 19, ["Aminoglycosides"]),
  C(LOOP, "Which drug's clearance falls and toxicity rises with loop diuretics?", "Lithium.", 19, ["Lithium"]),
  C(LOOP, "Which anticoagulant competes with loop diuretics for plasma protein binding?", "Warfarin.", 19, ["Warfarin"]),
  C(LOOP, "Which condition can a loop diuretic be added to saline hydration to treat?", "Hypercalcemia.", 17, ["Hypercalcemia (used with saline)"]),
  C(LOOP, "Which two electrolyte losses with loops make digitalis arrhythmias more likely?", "Hypokalemia and hypomagnesemia.", 19, ["Digitalis - hypokalemic + hypomagnesemic - arrhythmias"]),
 ]),
 (THIAZ, "Thiazide Diuretics", "accent2", DROP_ICON, [
  # ---- thiazides
  C(THIAZ, "Name the five thiazide diuretics.", "Chlorothiazide, hydrochlorothiazide, chlorthalidone, metolazone and indapamide.", 20, ["Chlorothiazide", "Hydrochlorothiazide", "Chlorthalidone", "Metolazone", "Indapamide"]),
  C(THIAZ, "Which transporter do thiazides inhibit?", "The sodium-chloride transporter of the distal convoluted tubule.", 21, ["Inhibit Na/CL transporter in luminal membrane of DCT"]),
  C(THIAZ, "What do thiazides do to renal calcium excretion?", "They decrease it.", 22, ["Decreased renal calcium excretion"]),
  C(THIAZ, "Which kidney stones do thiazides help prevent?", "Calcium oxalate stones.", 24, ["renal calcium stones (calcium oxalate)"]),
  C(THIAZ, "Which serum calcium effect can thiazides cause?", "Hypercalcemia.", 27, ["Hypercalcemia"], tf=["it could cause the patient's serum calcium levels to go up a little"]),
  C(THIAZ, "Which patients respond best to thiazides for hypertension?", "Elderly and African American patients, and sodium-retentive states.", 25, ["Works best in 1) elderly", "African Americans", "sodium retentive states"]),
  C(THIAZ, "Which thiazide still works at low creatinine clearance?", "Metolazone.", 28, ["Metolazone effective at lower clearance rates"], tf=["metolazone could make a rock p"]),
  C(THIAZ, "Which acid-base disorder do thiazides cause?", "Metabolic alkalosis.", 26, ["Metabolic alkalosis"]),
  C(THIAZ, "Which uric acid disorder do thiazides cause?", "Hyperuricemia, with gout.", 26, ["Hyperuricemia - gout"]),
  C(THIAZ, "Which lipid rises modestly with thiazides?", "Low-density lipoprotein.", 27, ["Hyperlipidema (5-15% increase in LDL)"]),
  C(THIAZ, "Which skin effect do thiazides share with loops?", "Photosensitivity.", 27, ["Photosensitivity"]),
  C(THIAZ, "Which sexual and bowel adverse effects can thiazides cause?", "Sexual dysfunction and constipation.", 28, ["Sexual dysfunction", "Constipation"]),
  C(THIAZ, "Which serum electrolyte should stay above 4.0 milliequivalents per liter in patients on a thiazide and digitalis?", "Potassium.", 29, ["K+ levels should be > 4.0"]),
  C(THIAZ, "Which drug class weakens the natriuretic action of thiazides?", "Non-steroidal anti-inflammatory drugs.", 29, ["NSAIDS - block PG's attenuate natriuretic actions"]),
 ]),
 (KSPARE, "Potassium-Sparing, Aldosterone Antagonists &amp; Carbonic Anhydrase Inhibitors", "accent3", DROP_ICON, [
  # ---- potassium-sparing and aldosterone antagonists
  C(KSPARE, "Name the two potassium-sparing diuretics that block sodium channels.", "Amiloride and triamterene.", [(30, ["Block luminal sodium channels"]), (31, ["Amiloride", "Triamterene"])]),
  C(KSPARE, "What is the main adverse effect of potassium-sparing diuretics?", "Hyperkalemia.", 33, ["Hyperkalemia"]),
  C(KSPARE, "Which two drug classes add to the hyperkalemia risk of potassium-sparing diuretics?", "Angiotensin-converting enzyme inhibitors and angiotensin blockers.", 33, ["Caution with ACEI and Angiotensin blockers"]),
  C(KSPARE, "Which potassium-sparing diuretic can cause megaloblastic anemia?", "Triamterene.", 33, ["Megaloblastic anemia"]),
  C(KSPARE, "Which potassium-sparing diuretic can cause azotemia?", "Amiloride.", 33, ["Azotemia"]),
  C(KSPARE, "How are potassium-sparing diuretics usually used?", "Combined with another diuretic or an antihypertensive.", 32, ["Most often used in combination with other diuretics or antihypertensive drugs"]),
  C(KSPARE, "Which salt is usually in a salt substitute, a hazard with potassium-sparing diuretics?", "Potassium chloride.", 33, ["Caution with Potassium supplements"], tf=["that's usually potassium chloride"]),
  C(KSPARE, "Name the two aldosterone antagonists.", "Spironolactone and eplerenone.", 35, ["Spironolactone", "Eplerenone"]),
  C(KSPARE, "How do aldosterone antagonists block the receptor?", "They bind the steroid receptor but do not translocate to the nucleus.", 36, ["Binds to steroid receptor but does not translocate to nucleus"]),
  C(KSPARE, "When are aldosterone antagonists most effective?", "When aldosterone is high.", 36, ["Most effective when Aldosterone high"]),
  C(KSPARE, "What breast change does spironolactone cause in men?", "Gynecomastia.", 38, ["Gynecomastia and testicular atrophy in men"]),
  C(KSPARE, "What does spironolactone cause in women?", "Menstrual irregularities.", 38, ["Menstrual irregularities, Hirsutism in women"]),
  C(KSPARE, "Which aldosterone antagonist has less effect on androgen receptors?", "Eplerenone.", 38, ["Eplerenone has less effect on androgen receptors"], tf=["that's much less of the androgenic activity"]),
  C(KSPARE, "Which electrolyte and acid-base problem do aldosterone antagonists cause?", "Hyperkalemia and mild acidosis.", 38, ["Hyperkalemia /mild acidosis"]),
  C(KSPARE, "Which liver condition causes secondary hyperaldosteronism treated with aldosterone antagonists?", "Cirrhosis.", 37, ["Cirrhosis (secondary hyperaldosteronism)"]),
  # ---- carbonic anhydrase inhibitors
  C(KSPARE, "Name the three carbonic anhydrase inhibitors.", "Acetazolamide, dichlorphenamide and methazolamide.", 40, ["Acetazolamide", "Dichlorphenamide", "Methazolamide"]),
  C(KSPARE, "Which ion do carbonic anhydrase inhibitors stop the proximal tubule from absorbing?", "Bicarbonate.", 39, ["HCO3 absorption in PCT by 80-90%"]),
  C(KSPARE, "What happens to the diuretic effect of carbonic anhydrase inhibitors after 3 to 5 days?", "It fades as the body compensates.", 39, ["Long term (after 3-5 days) effect is reduced to 1-3 %"]),
  C(KSPARE, "Which acid-base disorder do carbonic anhydrase inhibitors cause?", "Metabolic acidosis.", 43, ["Metabolic acidosis"], tf=["that's different than your other diuretics which typically cause"]),
  C(KSPARE, "Which electrolyte do carbonic anhydrase inhibitors deplete?", "Potassium.", 43, ["Potassium depletion"]),
  C(KSPARE, "Which central nervous system effect do carbonic anhydrase inhibitors cause?", "Drowsiness.", 43, ["Drowsiness"]),
  C(KSPARE, "Name three non-diuretic uses of carbonic anhydrase inhibitors.", "Glaucoma, epilepsy and mountain sickness.", 42, ["Glaucoma", "Epilepsy", "Mountain sickness"]),
  C(KSPARE, "Which two topical carbonic anhydrase inhibitors treat glaucoma?", "Dorzolamide and brinzolamide.", 42, ["Dorzolamide", "Brinzolamide"]),
 ]),
 (HFCORE, "Heart Failure: Basics, Angiotensin Inhibitors &amp; Beta Blockers", "accent1", HF_ICON, [
  # ---- heart failure concepts
  C(HFCORE, "What is the most common cause of heart failure?", "Ischemic heart disease and myocardial infarction.", 45, ["Ischemic heart disease, MI", "50-60% of cases"]),
  C(HFCORE, "What does systolic dysfunction decrease?", "Contractility.", 46, ["Decreased contractility"]),
  C(HFCORE, "How is systolic dysfunction assessed?", "As a reduced ejection fraction.", 46, ["Assessed as reduced ejection fraction"]),
  C(HFCORE, "What defines diastolic dysfunction?", "Impaired relaxation.", 47, ["Impaired relaxation"]),
  C(HFCORE, "Which ejection fraction goes with diastolic dysfunction?", "A preserved one.", 47, ["HF symptoms with preserved ejection fraction"]),
  C(HFCORE, "What raises preload as a compensatory response in heart failure?", "Sodium and water retention.", 48, ["Increased preload (through Na and water retention)"]),
  C(HFCORE, "Which compensatory response comes from sympathetic activation?", "Tachycardia and increased contractility.", 48, ["Tachycardia and increased contractility"]),
  C(HFCORE, "Name three precipitants of heart failure decompensation.", "Lack of compliance, uncontrolled hypertension and arrhythmias.", 50, ["Lack of compliance", "Uncontrolled hypertension", "Cardiac arrhythmias"]),
  C(HFCORE, "Which dietary measure is non-drug therapy for heart failure?", "Sodium and fluid restriction.", 51, ["Dietary sodium and fluid restriction"]),
  # ---- diuretics, ACE inhibitors, beta blockers
  C(HFCORE, "Which diuretic class is the mainstay of heart failure therapy?", "Loop diuretics.", 52, ["Mainstay of HF therapy"]),
  C(HFCORE, "Why are thiazides rarely enough in heart failure?", "They are not potent enough for most patients.", 52, ["Not potent enough for most HF patients"]),
  C(HFCORE, "How can a heart failure patient detect worsening fluid overload at home?", "By daily weights.", 52, ["Monitoring patient's weight"]),
  C(HFCORE, "What do diuretics do for heart failure outcomes?", "Relieve symptoms only, without lowering mortality.", 53, ["Diuretics are for symptomatic relief only", "No evidence to show they decrease progression or mortality"],
    tf=["they don't do anything to increase mortality"]),
  C(HFCORE, "Which drug class slows heart failure progression by reducing remodeling?", "Angiotensin-converting enzyme inhibitors.", 54, ["Slows heart failure progression", "Decrease left ventricular hypertrophy, dilation, and remodeling"]),
  C(HFCORE, "What do angiotensin-converting enzyme inhibitors do to preload and afterload?", "They lower both preload and afterload.", 54, ["Decrease preload", "Decrease afterload"]),
  C(HFCORE, "Name the angiotensin-converting enzyme inhibitor problems in heart failure.", "Renal impairment, hypotension, hyperkalemia, cough and angioedema.", 56, ["Impairment of renal function", "Hypotension", "Elevation of serum potassium", "Cough", "Angioedema"]),
  C(HFCORE, "Which three beta blockers lower mortality in heart failure?", "Carvedilol, metoprolol succinate and bisoprolol.", 57, ["Carvedilol", "Metoprolol succinate XL", "Bisoprolol"], tf=["these three in particular have been found to be associated with reducing mortality"]),
  C(HFCORE, "How were beta blockers classically viewed in heart failure?", "As contraindicated.", 57, ["Classically considered contraindicated in heart failure"]),
  C(HFCORE, "How are beta blockers started in heart failure?", "At very low doses, titrated up slowly.", 58, ["Start with very low doses", "Titrate up slowly over 6-8 weeks total"], tf=["low and slow"]),
  C(HFCORE, "What should a heart failure patient be before a beta blocker is started?", "Stable.", 58, ["Patient should be stable prior to initiation"]),
  C(HFCORE, "What is monitored while beta blockers are titrated in heart failure?", "Worsening heart failure signs and symptoms.", 58, ["Monitor for worsening HF signs and symptoms"]),
  C(HFCORE, "Beta blockers are first line in which classes of heart failure?", "Classes II to IV.", 60, ["First line therapy in Class II-IV heart failure"]),
  C(HFCORE, "Which two drug classes should heart failure patients be on irrespective of symptoms?", "An angiotensin-converting enzyme inhibitor and a beta blocker.", 60, ["Patients should be on ACEI and BB irrespective of symptoms"]),
 ]),
 (DIGOX, "Digoxin", "accent2", HF_ICON, [
  # ---- digoxin
  C(DIGOX, "Which enzyme does digoxin inhibit?", "The sodium-potassium ATPase.", 62, ["Digitalis inhibits Na+/K+ ATPase"]),
  C(DIGOX, "Why does digoxin increase the force of contraction?", "Intracellular sodium rises, which raises intracellular calcium.", 62, ["Intracellular Na+ concentration increases", "Ca2+"]),
  C(DIGOX, "What is digoxin's newer, neurohormonal mechanism?", "Less sympathetic and more parasympathetic activity.", 63, ["Neurohormonal - newer mechanism", "Decrease sympathetic and Increase parasympathetic nervous system activity"]),
  C(DIGOX, "Which heart failure outcome does digoxin NOT improve?", "Survival.", 66, ["NO SURVIVAL BENEFIT"], tf=["no survival benefits"]),
  C(DIGOX, "Which benefits does digoxin give in heart failure?", "Better symptoms, exercise tolerance and quality of life, and fewer hospitalizations.", 66, ["Improvement in symptoms", "Improved exercise tolerance", "Improve quality of life", "Decreased number of hospitalizations"]),
  C(DIGOX, "When is digoxin added in heart failure?", "When symptoms persist despite optimal angiotensin-converting enzyme inhibitor, beta blocker and diuretic therapy.", 67, ["Primary use in symptomatic patients on optimal doses of ACE inhibitors/beta blockers and diuretics"]),
  C(DIGOX, "Which visual disturbance, with yellow-green halos, marks digoxin toxicity?", "Xanthopsia.", 68, ["Xanthopsia", "Yellow-green halos"], tf=["like there's nothing else that does that"]),
  C(DIGOX, "Which gastrointestinal symptoms mark digoxin toxicity?", "Anorexia and nausea.", 68, ["GI - anorexia, nausea"]),
  C(DIGOX, "Which central symptoms mark digoxin toxicity?", "Delirium, fatigue, confusion, dizziness and abnormal dreams.", 69, ["Delirium", "Fatigue", "Confusion", "Abnormal dreams"]),
  C(DIGOX, "Which heart rate change marks digoxin toxicity?", "Bradycardia.", 70, ["Bradycardia"], tf=["bradycardia is most common"]),
  C(DIGOX, "Which two electrocardiogram intervals change with digoxin toxicity?", "A longer PR interval and a shorter QT interval.", 70, ["↑ PR interval ↓ QT interval"]),
  C(DIGOX, "Which three electrolyte disturbances make digoxin toxicity more likely?", "Hypokalemia, hypomagnesemia and hypercalcemia.", [(19, ["Digitalis - hypokalemic + hypomagnesemic - arrhythmias"]), (71, ["Hypomagnesaemia", "Hypercalcemia"])], tf=["the big deal to watch for is the electrolytes"]),
  C(DIGOX, "Which conduction condition contraindicates digoxin?", "Advanced atrioventricular block.", 71, ["Advanced AV block"]),
  C(DIGOX, "Which accessory-pathway syndrome contraindicates digoxin?", "Wolff-Parkinson-White syndrome.", 71, ["Wolf-Parkinson- White"]),
  C(DIGOX, "What reverses digoxin toxicity?", "Digoxin immune Fab.", 72, ["Digoxin Immune Fab", "Rapidly reverse toxicity"]),
  C(DIGOX, "Which animal is immunized to make digoxin immune Fab?", "Sheep.", 72, ["immunization of healthy sheep with digoxin coupled to human serum albumin"]),
  C(DIGOX, "Why does digoxin immune Fab work?", "Its affinity for digoxin is higher than that of the sodium-potassium ATPase.", 72, ["Affinity higher for Digoxin than affinity of digoxin and Na+K+ ATPase"]),
 ]),
 (HFOTHER, "Other Heart Failure Drugs", "accent3", HF_ICON, [
  # ---- other agents
  C(HFOTHER, "In which heart failure severity does spironolactone lower mortality?", "Advanced, class III or IV.", 73, ["Mortality reduction in grade III or IV HF"]),
  C(HFOTHER, "Spironolactone is not used in heart failure when potassium is above what level?", "Above 5 milliequivalents per liter.", 73, ["Patients not eligible if K > 5 or SCr > 2.5"]),
  C(HFOTHER, "Which aldosterone antagonist often causes gynecomastia in men?", "Spironolactone.", 73, ["Gynecomastia in men ~10%"]),
  C(HFOTHER, "Which aldosterone antagonist causes far less gynecomastia?", "Eplerenone.", 73, ["Eplerenone", "No gynecomastia"]),
  C(HFOTHER, "Which two drugs are phosphodiesterase type 3 inhibitors for heart failure?", "Milrinone and inamrinone.", 74, ["Milrinone", "Inamrinone", "Cyclic AMP phosphodiesterase (III) inhibitors"]),
  C(HFOTHER, "What two actions do milrinone and inamrinone combine?", "Inotropic stimulation and balanced vasodilation.", 75, ["Inotropic as well as vasodilator actions", "Balanced arterial and venous dilation"]),
  C(HFOTHER, "Milrinone is approved for which setting?", "Short-term intravenous use in acute decompensated heart failure.", 76, ["Approved for short term IV use in acute decompensated heart failure"]),
  C(HFOTHER, "What does long-term use of milrinone or inamrinone do to mortality?", "It raises it compared with placebo.", 76, ["Long term use is associated with higher mortality and morbidity"]),
  C(HFOTHER, "Which adverse effects limit milrinone and inamrinone?", "Thrombocytopenia and ventricular arrhythmias.", 76, ["Thrombocytopenia (Milrinone less)", "Ventricular arrhythmias"]),
  C(HFOTHER, "Which selective beta-1 agonist stimulates force more than rate?", "Dobutamine.", 77, ["Dobutamine - selective beta 1 agonist", "stimulates force of contraction more than rate of contraction"]),
  C(HFOTHER, "A hypotensive patient in decompensated heart failure suits which agents?", "Dobutamine or dopamine.", [(77, ["Dobutamine", "Dopamine"])], tf=["if they're going to be hypotensive then something like"]),
  C(HFOTHER, "A hypertensive patient in decompensated heart failure suits which agent?", "Milrinone.", [(75, ["Decreased afterload"])], tf=["if they're hypertensive then like milrinone works better"]),
  C(HFOTHER, "Which channel does ivabradine block?", "The hyperpolarization-activated cyclic nucleotide-gated channel.", 79, ["Hyperpolarization-activated cyclic nucleotide-gated (HCN) channel blocker"]),
  C(HFOTHER, "What does ivabradine do to heart rate and contractility?", "It lowers heart rate without affecting contractility.", 79, ["Reduces heart rate, doesn't affect contractility"]),
  C(HFOTHER, "Ivabradine is for patients maxed out on which drug class?", "Beta blockers.", 79, ["maxed out on beta blockers"]),
  C(HFOTHER, "Ivabradine needs which rhythm and heart rate?", "Normal sinus rhythm with a heart rate above 70 beats per minute.", 79, ["In NSR with HR > 70 bpm"], tf=["normal sinus rhythm and heart rate above 70"]),
  C(HFOTHER, "Which visual symptom does ivabradine cause?", "Phosphenes.", 80, ["Visual impairment (phosphenes)"]),
  C(HFOTHER, "Which rhythm risks does ivabradine carry?", "Atrial fibrillation and symptomatic bradycardia.", 80, ["Increase risk of atrial fibrillation", "Symptomatic bradycardia"]),
  C(HFOTHER, "Which enzyme does sacubitril inhibit?", "Neprilysin.", 81, ["Neprilysin inhibitor"]),
  C(HFOTHER, "Sacubitril is formulated with which angiotensin receptor blocker?", "Valsartan.", 81, ["Formulated with valsartan"]),
  C(HFOTHER, "Which drug class must never be combined with sacubitril-valsartan?", "Angiotensin-converting enzyme inhibitors.", 81, ["Don't use along with ACE inhibitor"], tf=["you would not want to use this with an ace inhibitor"]),
  C(HFOTHER, "How long is the washout when switching from an angiotensin-converting enzyme inhibitor to sacubitril-valsartan?", "36 hours.", 81, ["give 36 hour washout period"]),
  C(HFOTHER, "Which adverse effects are most common with sacubitril-valsartan?", "Hypotension, hyperkalemia, cough and renal insufficiency.", 81, ["hypotension, hyperkalemia, cough, renal insufficiency"]),
  C(HFOTHER, "Which two sodium-glucose cotransporter 2 inhibitors are used in heart failure?", "Dapagliflozin and empagliflozin.", 82, ["Dapagliflozin", "Empagliflozin"]),
  C(HFOTHER, "Sodium-glucose cotransporter 2 inhibitors reduce mortality in which heart failure type?", "Heart failure with reduced ejection fraction.", 82, ["For stable, chronic HFrEF"]),
  C(HFOTHER, "What were sodium-glucose cotransporter 2 inhibitors originally used for?", "Diabetes.", 82, ["Originally for diabetes"]),
  C(HFOTHER, "Which two adverse effects come with sodium-glucose cotransporter 2 inhibitors?", "Hypotension and genital fungal infections.", 82, ["hypotension and fungal UTIs"]),
 ]),
]
