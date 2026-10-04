#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build 'Pharmacology I Exam 2: Most Likely 45 (Version 3: Drug Names)' (Jaxon, 2026-10-04, the day before the exam).

Jaxon: "Make another 45 question most likely ... you can repeat concepts from the first 2 to drill home but on this I
want drug names not classes, cause I need to know the drugs in the classes."

EVERY question's four options are specific drug names (generic names; combination products named as the deck names them).
Facts are the same most-likely facts as Versions 1 and 2 (Wood's emphasis; repeating concepts is allowed here) but asked as
'which drug' questions with a different stem.  Shapes: (c) clinical vignettes whose answer is one drug, (d) drug-specific side effect / education / contraindication /
interaction, (e) the exception inside a class (the one beta-1 selective eye drop, the one second-generation antihistamine rated low
for sedation, the beta blocker that also blocks alpha-1).

STYLE (Jaxon's correction, same day): "just like the other as far as how you ask the questions, just use the drug names
instead of answer choices being classes".  So the questions are asked as in Versions 1 and 2 (patient vignettes, what to
start / add / switch to, contraindication, education, side effect, interaction); only the answer choices change, to four
drug names.  The class-membership and odd-one-out shapes were dropped except where a question is naturally one.

SOURCES.  21 questions are the vetted rapid-drill items (tools/pharm_drill_*.py, rendered in the Exam 2 drill pages) taken
verbatim (stem, options and their explanations; their guide links are already audited); 4 are shipped pool questions
whose options were already all drugs, taken verbatim; 5 are drill items with the stem rewritten (as a patient vignette, or
because the drill stem said 'class' over drug options); 15 are NEW questions (mostly vignettes).  Every drug listed in a class is named in that class on a slide, and no
distractor of a membership item belongs to the asked class (the separate reviewer checks this against the decks).
No question rests on a dose.

    python3 tools/build_pharm_e2_most_likely_45_v3.py
    python3 tools/render_pharm_e2_most_likely_45_v3.py
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_pharm_e2_most_likely_45 as V1
import build_guide_links as B

OUT = os.path.join(HERE, "pharm_e2_most_likely_45_v3_sets.json")
REPORT = os.path.join(HERE, "pharm_e2_most_likely_45_v3_report.json")
SEED = 20261005
DRILL_FILES = {"gl": ("glaucoma-diagnostics", "Lecture 4"), "ai": ("anti-infectives", "Lecture 4"),
               "al": ("allergy-inflammation", "Lecture 4"), "en": ("ent", "Lecture 5"),
               "ht": ("antihypertensives", "Lecture 6"), "li": ("lipids", "Lecture 7"),
               "mi": ("myocardial-ischemia", "Lecture 8")}
LEC_OF = {"gl": "L4", "ai": "L4", "al": "L4", "en": "L5", "ht": "L6", "li": "L7", "mi": "L8"}
FOLDER = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 2")


def drill(key):
    f, i = key.split(":")
    name = DRILL_FILES[f][0]
    qs = B.load_questions(os.path.join(FOLDER, "pharm-e2-drill-%s.html" % name))
    return json.loads(json.dumps(qs[int(i)]))


def mk(topic, q, key, rest, key_expl, cite):
    """rest = [(drug, explanation), x3]; key first, then three distractors (positions are dealt later)."""
    opts = [[key, "Correct. " + key_expl]] + [[d, e] for d, e in rest]
    return dict(topic=topic, q=q, opts=opts, c=0, cite=cite)


NEW = {}
# ---------------- Lecture 4 -------------------------------------------------------------------------------------
NEW["n4a"] = mk("Starting glaucoma therapy", "A 62-year-old is newly diagnosed with open-angle glaucoma and has risk factors for progression. Which drug is the usual first choice?", "Latanoprost", [
    ("Brimonidine", "Brimonidine is an alpha-2 agonist that reduces production and increases outflow but is not the first-line class; the usual first choice is the prostaglandin analog latanoprost."),
    ("Dorzolamide", "Dorzolamide is a carbonic anhydrase inhibitor, a third- or fourth-line add-on because of burning, stinging and a bitter taste; the first-line drug is the prostaglandin analog latanoprost."),
    ("Pilocarpine", "Pilocarpine is a cholinergic agonist, the last-line class because of miosis, blurred vision and frequent dosing; the first-line drug is the prostaglandin analog latanoprost.")],
    "Latanoprost, a prostaglandin analog (with travoprost, bimatoprost and tafluprost), is the first-line glaucoma class and the most commonly used; it lowers pressure by increasing aqueous outflow.",
    "Ophthalmology-2.pptx, Slides 64 and 65")
NEW["n4b"] = mk("Ocular antibiotics", "A 19-year-old who wears contact lenses has purulent bacterial conjunctivitis, and keratitis has been excluded. Which ophthalmic antibiotic is the preferred treatment?", "Ciprofloxacin", [
    ("Erythromycin", "Erythromycin is a macrolide, soothing and the commonest ophthalmic antibiotic, but it is not the drug preferred for contact lens wearers; a fluoroquinolone such as ciprofloxacin is."),
    ("Tobramycin", "Tobramycin is an aminoglycoside with gram-negative activity, but it carries a risk of corneal ulceration; the drug named for Pseudomonas and corneal ulcers is a fluoroquinolone such as ciprofloxacin."),
    ("Sulfacetamide", "Sulfacetamide is a sulfonamide, to be avoided with a sulfa allergy, and is not the drug named for contact lens wearers; the fluoroquinolone ciprofloxacin is preferred once keratitis is ruled out.")],
    "Ciprofloxacin, a fluoroquinolone, covers Pseudomonas aeruginosa, the gram-negative rod that contact lens wearers are at risk from; fluoroquinolones are also preferred for corneal ulcers.",
    "Ophthalmology-2.pptx, Slides 21 and 22")
NEW["n4c"] = mk("Ocular antifungals", "A 47-year-old farmer develops fungal keratitis after a branch scratches his cornea while he clears brush. Which drug is the one commercially available ophthalmic antifungal?", "Natamycin", [
    ("Trifluridine", "Trifluridine is an antiviral for herpes simplex keratitis and has no antifungal action; natamycin is the only commercially available ophthalmic antifungal."),
    ("Ciprofloxacin", "Ciprofloxacin is a fluoroquinolone antibacterial and does not treat a fungus; the only commercially available ophthalmic antifungal is natamycin."),
    ("Erythromycin", "Erythromycin is a macrolide antibacterial, the commonest ophthalmic antibiotic, and it has no antifungal action; natamycin is the only commercially available ophthalmic antifungal.")],
    "Natamycin is the only commercially available ophthalmic antifungal; it binds sterol in the fungal membrane, makes it leak, and covers Aspergillus, Candida, Fusarium and others.",
    "Ophthalmology-2.pptx, Slides 30 and 32")
NEW["n4d"] = mk("Ocular glucocorticoids", "A 60-year-old with a strong family history of glaucoma needs a topical steroid for anterior uveitis. Which drug is a soft steroid with a lower risk of raising intraocular pressure?", "Loteprednol", [
    ("Dexamethasone", "Dexamethasone is a harder-hitting steroid that raises eye pressure more readily; the soft steroids are fluorometholone, loteprednol and rimexolone."),
    ("Prednisolone", "Prednisolone is a harder-hitting steroid, not one of the three soft steroids (fluorometholone, loteprednol, rimexolone), so it carries more pressure risk in this patient."),
    ("Difluprednate", "Difluprednate is a harder-hitting steroid and is not one of the three soft steroids (fluorometholone, loteprednol, rimexolone); it is a poor fit for a patient at risk of glaucoma.")],
    "Loteprednol is one of the three soft steroids (with fluorometholone and rimexolone), marked because they carry a lower risk of raising eye pressure, which matters in a patient at risk of glaucoma.",
    "Ophthalmology-2.pptx, Slide 55")
# ---------------- Lecture 5 -------------------------------------------------------------------------------------
NEW["n5a"] = mk("Antihistamines and sedation", "A bus driver with seasonal allergies must stay alert on a 10-hour route. Which antihistamine should he take?", "Fexofenadine", [
    ("Diphenhydramine", "Diphenhydramine is a first-generation antihistamine rated high for sedation and antimuscarinic effects, which is the wrong trade for a driver; a second-generation drug such as fexofenadine avoids it."),
    ("Hydroxyzine", "Hydroxyzine is a first-generation antihistamine rated high for sedation; it crosses into the brain and its sedation adds up with alcohol, so a second-generation drug such as fexofenadine suits a driver."),
    ("Promethazine", "Promethazine is a first-generation antihistamine rated high for sedation, antiemetic and antimuscarinic effects, a poor fit for a driver; fexofenadine is rated very low for sedation.")],
    "Fexofenadine is a second-generation antihistamine; it largely stays out of the central nervous system and is rated very low for sedation, so it treats the allergy without making a driver drowsy.",
    "ENT Jax Pharmacology.pptx, Slides 32 and 37")
NEW["n5c"] = mk("Antifungals in the ear, nose and throat lecture", "A 40-year-old who uses an inhaled steroid develops white patches in the mouth and takes several other medicines. Which antifungal is preferred?", "Nystatin", [
    ("Ketoconazole", "Ketoconazole is absorbed, inhibits cytochrome P450 3A4 (CYP3A4) and prolongs the QT interval, which is a problem in a patient on several medicines; nystatin is not absorbed and treats oral candidiasis."),
    ("Natamycin", "Natamycin is the only commercially available ophthalmic antifungal, an eye preparation; oral candidiasis in a patient on inhaled steroids is treated with nystatin."),
    ("Amphotericin B", "Amphotericin B is a polyene antifungal given by topical or injected routes (including intravenous) for serious yeast and fungal infection; the nonabsorbable agent for oral candidiasis is nystatin.")],
    "Nystatin is a nonabsorbable antifungal that treats oral candidiasis (thrush), which appears with inhaled steroids; because it is not absorbed it cannot interact with the patient's other medicines.",
    "ENT Jax Pharmacology.pptx, Slide 13")
# ---------------- Lecture 6 -------------------------------------------------------------------------------------
NEW["n6a"] = mk("ACE inhibitors and potassium", "A 64-year-old with chronic kidney disease who uses a potassium-containing salt substitute needs a new antihypertensive. Which drug is most likely to raise his potassium?", "Lisinopril", [
    ("Amlodipine", "Amlodipine is a dihydropyridine calcium channel blocker that dilates vessels and does not change potassium; the drug that raises it, especially in kidney disease, is the ACE inhibitor lisinopril."),
    ("Prazosin", "Prazosin is an alpha-1 blocker whose risks are orthostatic hypotension and reflex tachycardia, not hyperkalemia; the ACE inhibitor lisinopril is the drug that raises potassium."),
    ("Hydralazine", "Hydralazine is a direct vasodilator whose problems are reflex tachycardia, fluid retention and lupus syndrome, not high potassium; the ACE inhibitor lisinopril raises potassium.")],
    "Lisinopril, an ACE (angiotensin-converting enzyme) inhibitor, lowers aldosterone, so potassium rises, most often with renal disease, potassium-sparing diuretics, potassium supplements or salt substitutes.",
    "Antihypertensives.pptx, Slide 20")
NEW["n6c"] = mk("Choosing an antihypertensive", "A 52-year-old with type 2 diabetes and newly diagnosed hypertension needs a first drug that also protects the kidneys. Which drug is preferred?", "Lisinopril", [
    ("Atenolol", "Atenolol is a beta blocker, not first line for hypertension, and it can mask or prolong hypoglycemia in a diabetic; the kidney-protective choice is an ACE inhibitor such as lisinopril."),
    ("Prazosin", "Prazosin is an alpha-1 blocker used as an add-on drug, not the preferred first choice in diabetes; the kidney-protective choice is an ACE inhibitor such as lisinopril."),
    ("Hydralazine", "Hydralazine is a direct vasodilator given with a diuretic and a beta blocker for chronic hypertension, not a first drug, and it has no kidney-protective effect; the ACE inhibitor lisinopril is preferred in diabetes.")],
    "Lisinopril, an ACE inhibitor, is preferred in diabetes because it lowers glomerular pressure and slows diabetic nephropathy; an angiotensin receptor blocker is the equivalent choice.",
    "Antihypertensives.pptx, Slide 16")
NEW["n6d"] = mk("Calcium channel blockers in practice", "A 68-year-old with atrial fibrillation needs his heart rate slowed with a calcium channel blocker. Which drug is the right choice?", "Diltiazem", [
    ("Amlodipine", "Amlodipine is a dihydropyridine that dilates vessels and does not slow atrioventricular conduction, so it cannot control the rate; diltiazem, a non-dihydropyridine, does."),
    ("Nifedipine", "Nifedipine is a dihydropyridine that causes vasodilation with reflex tachycardia rather than nodal slowing; rate control needs diltiazem or verapamil."),
    ("Felodipine", "Felodipine is a dihydropyridine approved for hypertension and does not act on the nodes; rate control in atrial fibrillation needs a non-dihydropyridine such as diltiazem.")],
    "Diltiazem, a non-dihydropyridine, suppresses the sinoatrial and atrioventricular nodes, so atrial fibrillation or flutter is an approved use; only diltiazem and verapamil act on the heart this way.",
    "Antihypertensives.pptx, Slide 44")
# ---------------- Lecture 7 -------------------------------------------------------------------------------------
NEW["n7a"] = mk("Choosing a lipid-lowering drug", "A 55-year-old man after a myocardial infarction needs lipid-lowering therapy. Which drug is first line?", "Atorvastatin", [
    ("Fenofibrate", "Fenofibrate is a fibrate that mainly lowers triglycerides and barely lowers low-density lipoprotein (LDL) cholesterol; the first-line drug when LDL lowering is indicated is a statin such as atorvastatin."),
    ("Cholestyramine", "Cholestyramine is a bile acid sequestrant, the safest class but poorly tolerated and not first line; the first-line drug is a statin such as atorvastatin."),
    ("Niacin", "Niacin lowers triglycerides and raises HDL (high-density lipoprotein) but is not the first-line drug for LDL lowering; the first-line drug is a statin such as atorvastatin.")],
    "Atorvastatin is a statin, the first-line drug when LDL (low-density lipoprotein) lowering is indicated; clinical atherosclerotic disease such as a prior infarction is the first statin benefit group.",
    "Lipids.pptx, Slides 25 and 65")
NEW["n7c"] = mk("Choosing a lipid-lowering drug", "A man's lipid panel shows normal cholesterol but a triglyceride level of 1200 mg/dL. Which drug is the best choice for this problem?", "Fenofibrate", [
    ("Colesevelam", "Colesevelam is a bile acid sequestrant, and resins can raise triglycerides (contraindicated above 400 mg/dL), so it is the wrong choice here; a fibrate such as fenofibrate lowers them."),
    ("Ezetimibe", "Ezetimibe lowers triglycerides only about 8 percent, far too little for a level above 1000 mg/dL; a fibrate such as fenofibrate is the drug for this."),
    ("Evolocumab", "Evolocumab is an injected antibody against PCSK9 that lowers low-density lipoprotein (LDL) cholesterol; a triglyceride level above 1000 mg/dL calls for a fibrate such as fenofibrate.")],
    "Fenofibrate is a fibrate; triglycerides above 1000 mg/dL are the primary fibrate indication, and fibrates lower triglycerides by 20 to 50 percent.",
    "Lipids.pptx, Slide 39")
NEW["n7d"] = mk("Lipid-lowering drugs: contraindications", "A patient with a fasting triglyceride of 600 mg/dL and a high LDL (low-density lipoprotein) cholesterol is about to start lipid therapy. Which drug is contraindicated?", "Colestipol", [
    ("Fenofibrate", "Fenofibrate lowers triglycerides by 20 to 50 percent and is the treatment for very high levels, not a contraindication; the contraindicated drug is the resin colestipol."),
    ("Niacin", "Niacin lowers triglycerides and raises HDL (high-density lipoprotein), so a high triglyceride level does not forbid it; the resin colestipol is the one that may raise them."),
    ("Atorvastatin", "Atorvastatin lowers triglycerides modestly and is not contraindicated by a high level; the bile acid resin colestipol is, because resins may raise triglycerides.")],
    "Colestipol, a bile acid sequestrant, is contraindicated when triglycerides exceed 400 mg/dL (relatively above 200 mg/dL) because resins can raise very-low-density lipoprotein (VLDL) production and triglycerides.",
    "Lipids.pptx, Slide 48")
# ---------------- Lecture 8 -------------------------------------------------------------------------------------
NEW["n8a"] = mk("Adding to a beta blocker", "A 60-year-old man with stable angina still has exertional attacks on metoprolol alone. Which added drug is best?", "Amlodipine", [
    ("Verapamil", "Verapamil is a non-dihydropyridine, and adding it to a beta blocker raises the risk of bradycardia and heart block; the partner is a dihydropyridine such as amlodipine."),
    ("Enalapril", "Enalapril is an angiotensin-converting enzyme inhibitor that does not relieve angina symptoms, although it may slow disease progression; the symptom-relieving partner is amlodipine."),
    ("Clopidogrel", "Clopidogrel is an antiplatelet drug that has no effect on oxygen demand or on exertional symptoms; the drug added to a beta blocker for symptoms is a dihydropyridine such as amlodipine.")],
    "Amlodipine, a dihydropyridine, is the calcium channel blocker added when a beta blocker alone fails; it lowers wall tension without slowing atrioventricular conduction, and the beta blocker covers the heart rate rise that dihydropyridines can cause.",
    "Myocardial Ischemia Drugs.pptx, Slides 22 and 23")
NEW["n8c"] = mk("Switching an antianginal", "A 56-year-old man with exertional angina stopped his beta blocker because of vivid nightmares. Which drug is the usual substitute?", "Diltiazem", [
    ("Carvedilol", "Carvedilol is still a beta blocker, the class he could not tolerate; the substitute comes from a different class, a non-dihydropyridine calcium channel blocker such as diltiazem."),
    ("Isosorbide mononitrate", "Isosorbide mononitrate is a long-acting nitrate, an add-on drug used when beta blockers and calcium channel blockers cannot be used; diltiazem is the usual first substitute."),
    ("Clopidogrel", "Clopidogrel is an antiplatelet drug that does not lower oxygen demand and cannot replace an antianginal; diltiazem, which slows heart rate and contractility like a beta blocker, can.")],
    "Diltiazem, a non-dihydropyridine calcium channel blocker, slows heart rate and contractility like a beta blocker, so it is the substitute when a beta blocker is not tolerated.",
    "Myocardial Ischemia Drugs.pptx, Slide 22")
NEW["n8d"] = mk("Variant angina", "A 34-year-old woman has recurrent night-time chest pain at rest with transient ST-segment elevation, diagnosed as variant angina. Which drug should be avoided?", "Propranolol", [
    ("Amlodipine", "Amlodipine is a dihydropyridine calcium channel blocker, a treatment of choice in variant angina because it relieves the vessel spasm; the drug to avoid is the beta blocker propranolol."),
    ("Nitroglycerin", "Nitroglycerin dilates the coronary arteries and relieves the spasm, so it is used rather than avoided; the drug to avoid is the beta blocker propranolol."),
    ("Diltiazem", "Diltiazem is a calcium channel blocker that relieves vasospasm and is used in variant angina; the drug that may worsen it is the beta blocker propranolol.")],
    "Propranolol, a beta blocker, may worsen variant angina because the problem is vessel spasm, not oxygen demand; calcium channel blockers and nitrates reduce the symptoms.",
    "Myocardial Ischemia Drugs.pptx, Slide 39")

# --------------------------------------------------------------------------------------------------------------
# Drill items, taken verbatim except where noted (REWRITE changes the stem; OVERRIDE lengthens a short explanation).
# --------------------------------------------------------------------------------------------------------------
REWRITE = {
    "ai:4": "A patient with a documented sulfonamide allergy has bacterial conjunctivitis. Which ophthalmic antibiotic must be avoided?",
    "al:0": "Which eye drop causes rebound hyperemia if it is used for too long?",
    "en:5": "A 4-year-old with acute otitis media is allergic to penicillin. Which third-generation cephalosporin is the oral choice?",
    "en:18": "A 7-year-old with chickenpox has a fever. Which drug should be avoided because it is linked to Reye syndrome?",
}
OVERRIDE = {
    ("ai:4", "Trimethoprim with polymyxin B"): "Trimethoprim with polymyxin B (Polytrim) contains trimethoprim, a folate-pathway drug that is not a sulfonamide, so a sulfa allergy does not bar it; the drug to avoid is sulfacetamide.",
    ("al:0", "Olopatadine"): "Olopatadine is an antihistamine whose problems are irritation, headache and dryness, not rebound; the drop that causes rebound hyperemia is the vasoconstrictor naphazoline.",
    ("en:11", "Ciprofloxacin/dexamethasone"): "Ciprofloxacin/dexamethasone (Ciprodex) is a fluoroquinolone and steroid drop with no polymyxin B, so it does not carry the cochlear warning; the drop with polymyxin B is the one to avoid.",
    ("gl:3", "Timolol"): "Timolol is nonselective, so it also blocks beta-2 receptors and adds airway risk; betaxolol is the beta-1 selective eye drop.",
    ("gl:3", "Carteolol"): "Carteolol is also nonselective, so it blocks beta-2 receptors as well and adds airway risk; betaxolol is the beta-1 selective eye drop.",
    ("gl:3", "Levobunolol"): "Levobunolol is nonselective, with the same respiratory caution; betaxolol is the beta-1 selective eye drop.",
    ("gl:7", "Latanoprost"): "No age contraindication is given for latanoprost; the drug contraindicated under two years is brimonidine, an alpha-2 agonist, because of central nervous system depression and apnea.",
    ("gl:7", "Timolol"): "Timolol's cautions are cardiac and respiratory rather than an age ban; the drug contraindicated under two years is brimonidine, because of central nervous system depression and apnea.",
    ("gl:7", "Dorzolamide"): "Dorzolamide's adverse effects are bitter taste and stinging rather than an age ban; the drug contraindicated under two years is brimonidine, because of apnea.",
    ("gl:17", "Tropicamide"): "Tropicamide is a cycloplegic that dilates the pupil rather than anesthetizing it; the anesthetic that leaves the eye numb with no blink reflex is proparacaine.",
    ("gl:17", "Phenylephrine"): "Phenylephrine is a sympathomimetic mydriatic that dilates the pupil and does not numb the eye; the anesthetic that removes the blink reflex is proparacaine.",
    ("gl:17", "Fluorescein"): "Fluorescein is a diagnostic stain that shows epithelial defects and does not anesthetize; the anesthetic that removes the blink reflex is proparacaine.",
    ("ai:4", "Bacitracin"): "Bacitracin has no sulfonamide component, so a sulfa allergy does not bar it; the antibiotic that must be avoided is sulfacetamide, which is a sulfonamide.",
    ("ai:4", "Tobramycin"): "Tobramycin is an aminoglycoside with no sulfonamide group, so a sulfa allergy does not bar it; the antibiotic to avoid is the sulfonamide sulfacetamide.",
}
OPTION_REPLACE = {
    ("en:5", "Cefazolin"): ("Azithromycin", "Azithromycin is a macrolide, also listed for penicillin-allergic otitis media, but it is not a cephalosporin and up to half of Streptococcus pneumoniae are macrolide resistant; the oral third-generation cephalosporin is cefdinir."),
    ("en:12", "Terbinafine"): ("Natamycin", "Natamycin is an ophthalmic polyene that binds sterol in the fungal membrane and has no listed drug interactions; ketoconazole is the cytochrome P450 3A4 inhibitor that prolongs the corrected QT interval."),
    ("en:12", "Caspofungin"): ("Amphotericin B", "Amphotericin B is a polyene antifungal given topically or by injection, and it is not listed as a cytochrome P450 3A4 inhibitor or a QT-prolonging drug; ketoconazole is."),
}
# (source, lecture, shape, wood entries, why)
PLAN = [
    ("n4a", "L4", "vignette", [10], "Glaucoma ladder: the prostaglandin analog latanoprost first; Wood gave the order."),
    ("n4b", "L4", "vignette", [3], "Contact lens wearer: Pseudomonas, so a fluoroquinolone (ciprofloxacin)."),
    ("gl:3", "L4", "exception in class", [11, 12], "Betaxolol is the one beta-1 selective eye drop: 'just ones you kind of have to know'."),
    ("n4c", "L4", "vignette", [4], "Natamycin, the only commercially available ophthalmic antifungal."),
    ("n4d", "L4", "vignette", [8], "'Three which are going to be starred': the soft steroids (fluorometholone, loteprednol, rimexolone)."),
    ("gl:7", "L4", "drug-specific contraindication", [10], "Brimonidine is contraindicated under two years (apnea)."),
    ("gl:17", "L4", "drug-specific education", [68, 69], "Proparacaine: no blink reflex, never sent home."),
    ("ai:4", "L4", "vignette / contraindication", [2], "Sulfacetamide and a sulfonamide allergy ('notable')."),
    ("al:0", "L4", "drug-specific side effect", [5], "Naphazoline and rebound hyperemia: the fact Wood promised outright ('I will ask this question')."),
    ("n5a", "L5", "vignette", [26], "His own worked example of a vignette: a patient who drives for a living, which antihistamine."),
    ("en:53", "L5", "drug-specific contraindication", [19], "Dextromethorphan: contraindicated within two weeks of a monoamine oxidase inhibitor (an interaction rule he asked everyone to note)."),
    ("n5c", "L5", "vignette", [20], "Inhaled steroids and thrush: nystatin, the nonabsorbed antifungal."),
    ("en:5", "L5", "vignette", [15], "Penicillin-allergic ear infection: cefdinir ('what do you use as a backup?')."),
    ("en:18", "L5", "vignette", [23], "Reye syndrome: aspirin in a child with a viral illness."),
    ("en:12", "L5", "drug-specific interaction", [19], "Ketoconazole: QT prolongation and CYP3A4 ('anytime you see ... make a note')."),
    ("en:11", "L5", "drug-specific contraindication", [18], "The ear drop with polymyxin B is contraindicated with a ruptured eardrum or tubes."),
    ("en:46", "L5", "drug-specific side effect", [28], "Oxymetazoline and rebound congestion: promised outright ('it'll be somewhere on the test')."),
    ("en:33", "L5", "exception in class", [26], "Cetirizine is the second-generation antihistamine rated low rather than very low for sedation."),
    ("n6a", "L6", "vignette", [31], "Anything that changes potassium: ACE inhibitors raise it ('a very easy test question')."),
    ("P:ht:ccb1:9", "L6", "comorbidity drug choice", [38, 39], "Heart failure: avoid the non-dihydropyridines, so amlodipine (only diltiazem and verapamil act on the heart)."),
    ("n6c", "L6", "vignette", [52, 30], "Type 2 diabetes: start an ACE inhibitor or receptor blocker for kidney protection."),
    ("n6d", "L6", "vignette", [38, 39], "Rate control: diltiazem or verapamil."),
    ("ht:1", "L6", "vignette", [36], "ACE inhibitor cough: switch to an angiotensin receptor blocker."),
    ("ht:13", "L6", "exception in class", [44, 45], "Carvedilol: a beta blocker that also blocks alpha-1 and is used in heart failure (the letter-rule exception)."),
    ("ht:15", "L6", "drug-specific", [46], "Bisoprolol: one of the three beta blockers for heart failure ('just know these three')."),
    ("ht:24", "L6", "drug-specific side effect", [50], "Hydralazine: acetylation and lupus syndrome ('highlight acetylation')."),
    ("ht:27", "L6", "drug-specific side effect", [75], "Nitroprusside: cyanide toxicity, given with sodium thiosulfate."),
    ("n7a", "L7", "vignette", [64], "Statins first line 'ten times out of ten' (he said), after a prior infarction."),
    ("P:li:tg1:10", "L7", "drug-specific contraindication", [62, 64], "Fibrates are contraindicated in existing gallbladder disease (they cause cholelithiasis)."),
    ("n7c", "L7", "vignette", [57], "His question: the only problem is very high triglycerides, which drug is best."),
    ("n7d", "L7", "vignette", [60], "His question: a triglyceride of 600, which drug is contraindicated."),
    ("li:0", "L7", "vignette-style", [53], "Rosuvastatin has minimal CYP metabolism: the way around the CYP3A4 statin interaction."),
    ("li:9", "L7", "drug-specific interaction", [58], "Gemfibrozil raises warfarin's effect (fibrate interactions)."),
    ("li:15", "L7", "drug-specific side effect", [63], "Niacin flushing, minimized by aspirin."),
    ("li:20", "L7", "drug-specific", [67], "Alirocumab: the injectable PCSK9 antibody, for when a statin is not the answer."),
    ("li:13", "L7", "drug-specific", [59], "Cholestyramine: not absorbed, approved in pregnancy ('safest class')."),
    ("n8a", "L8", "vignette", [78, 83], "Add-on: a dihydropyridine is added to a beta blocker, a non-dihydropyridine is not."),
    ("P:mv:set1:11", "L8", "vignette", [108, 109], "Early ST-elevation infarction with no contraindication: alteplase dissolves the clot."),
    ("n8c", "L8", "vignette", [84], "He wrote this question out loud: nightmares on a beta blocker, switch to a non-dihydropyridine."),
    ("n8d", "L8", "vignette", [85, 101], "Variant angina: avoid the beta blocker."),
    ("mi:11", "L8", "drug-specific interaction", [90], "Sildenafil with a nitrate: profound hypotension."),
    ("mi:16", "L8", "drug-specific", [103], "Clopidogrel when aspirin cannot be used."),
    ("mi:20", "L8", "drug-specific", [106], "Morphine for pain unresponsive to nitrates."),
    ("mi:7", "L8", "drug-specific", [87], "Avoid short-acting nifedipine."),
    ("mi:28", "L8", "exception in class", [86], "Amlodipine is the one calcium channel blocker kept when ventricular function is reduced."),
]
# li:0 is rewritten as a vignette below; li:13 is used verbatim
REWRITE["li:0"] = "A patient on verapamil needs a statin. Which statin is least affected by the inhibition of cytochrome P450 3A4 (CYP3A4)?"
LEC_NAME = V1.LEC_NAME
POOL = {}
POOL_STEM = {"P:ht:ccb1:9": "A patient with hypertension also has heart failure. Which calcium channel blocker approved for hypertension avoids the relative contraindication in heart failure?"}


def plain(s):
    return V1.plain(s)


def main():
    POOL_ = V1.load_pool()
    POOL.update(POOL_)
    v1 = json.load(open(os.path.join(HERE, "pharm_e2_most_likely_45_sets.json"), encoding="utf-8"))["set1"]
    v2 = json.load(open(os.path.join(HERE, "pharm_e2_most_likely_45_v2_sets.json"), encoding="utf-8"))["set1"]
    old = {plain(q["q"]) for q in v1 + v2}
    assert len(PLAN) == 45, len(PLAN)
    assert dict(Counter(p[1] for p in PLAN)) == {l: 9 for l in LEC_NAME}
    ordered = []
    for ref, lec, shape, wood, why in PLAN:
        if ref in NEW:
            q = json.loads(json.dumps(NEW[ref]))
        elif ref.startswith("P:"):
            q = json.loads(json.dumps(POOL[ref[2:]]))
            q = {k: q[k] for k in ("topic", "q", "opts", "c", "cite")}
            if ref in POOL_STEM:
                q["q"] = POOL_STEM[ref]
        else:
            dkey = ref if ":" in ref and ref.split(":")[0] in DRILL_FILES else None
            q = drill(ref)
            if ref in REWRITE:
                q["q"] = REWRITE[ref]
            q["opts"] = [list(OPTION_REPLACE.get((ref, plain(t)), (t, OVERRIDE.get((ref, plain(t)), e)))) for t, e in q["opts"]]
            if ref == "P:ht:ccb1:9":
                pass
        q["_lec"] = lec
        stem = plain(q["q"])
        assert stem not in old, "V1/V2 stem copied: " + stem
        assert len(q["opts"]) == 4 and q["opts"][q["c"]][1].startswith("Correct") or ref.startswith("al:"), ref
        for o in q["opts"]:
            assert len(plain(o[1])) >= 60 or (ref.startswith("al:") and len(o[1]) >= 60), (ref, o)
        keytxt = plain(q["opts"][q["c"]][0])
        assert not V1.DOSE_KEY.search(re.sub(r"mg/(dL|g)", "", keytxt)), ref
        ordered.append(q)
    stems = [plain(q["q"]) for q in ordered]
    assert len(set(stems)) == 45
    pos = V1.deal_positions(ordered, random.Random(SEED))
    out = []
    for (ref, lec, shape, wood, why), q, want in zip(PLAN, ordered, pos):
        o = list(q["opts"]); k = o.pop(q["c"]); o.insert(want, k)
        r = {"topic": q.get("topic") or DRILL_FILES[ref.split(":")[0]][1], "q": q["q"], "cite": q["cite"], "opts": o, "c": want}
        r["io"] = "Topic — " + LEC_NAME[lec]
        out.append(r)
    rep = {"counts_per_lecture": {l: 9 for l in LEC_NAME},
           "new": sum(1 for p in PLAN if p[0] in NEW),
           "drill_verbatim": sum(1 for p in PLAN if p[0] not in NEW and p[0] not in REWRITE),
           "drill_stem_rewritten": sum(1 for p in PLAN if p[0] not in NEW and p[0] in REWRITE),
           "positions": {chr(65 + k): v for k, v in sorted(Counter(pos).items())},
           "shapes": dict(Counter(p[2].split(" / ")[0] for p in PLAN)),
           "picks": [dict(ref=p[0], lec=p[1], shape=p[2], wood=p[3], why=p[4]) for p in PLAN]}
    json.dump({"set1": out}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(rep, open(REPORT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    comb_path = os.path.join(HERE, "pharm_e2_most_likely_selection_report.json")
    if os.path.exists(comb_path):
        comb = json.load(open(comb_path, encoding="utf-8"))
        v12 = {plain(q["q"]) for q in v1 + v2}
        comb["v3"] = rep
        comb["v3_note"] = ("Version 3 (Drug Names): same style as V1/V2 but every answer choice is a drug name; concepts from V1/V2 "
                           "may repeat (Jaxon, 2026-10-04); no stem text is copied. Reviewer found 45 of 45 keys correct and fixed "
                           "wrong-key / off-slide-drug / near-copy-stem findings; 17 drill stems keep their ALL-CAPS emphasis.")
        comb["v3_stems_copied_from_v1_v2"] = sorted(set(stems) & v12)
        json.dump(comb, open(comb_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.basename(OUT), len(out), rep["positions"], "new", rep["new"], "verbatim", rep["drill_verbatim"], "rewritten", rep["drill_stem_rewritten"])


if __name__ == "__main__":
    main()
