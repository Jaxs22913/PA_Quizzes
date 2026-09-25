# -*- coding: utf-8 -*-
"""Cram-sheet topics for Pharmacology I Exam 2, Lectures 5 to 7 (added 2026-09-25).

Imported by build_pharm_e2_cram.py and appended after the Lecture 4 topics.
Same sources and rules as the guide sections (_pharm_e2_guide_l5/l6/l7.py):
slide facts only, no doses, the star rows follow the audio emphasis reports'
section 4.2 for Lectures 6 and 7, and Lecture 5 (ENT) carries NO stars because
its recording has not been analysed for emphasis.
"""

T = [
# ---------------------------------------------------------------- Lecture 5
{"id":"ent-abx","label":"ENT &middot; antibiotics &amp; antifungals","color":"#2f6f8c","rows":[
 ["Same 3 bugs","Otitis media and sinusitis: <b>S. pneumoniae, H. influenzae, M. catarrhalis</b> (sinusitis adds S. pyogenes, S. aureus, gram-negative bacilli). Pharyngitis: mostly viral; group A strep in 15&ndash;30%."],
 ["Otitis media","<b>High-dose amoxicillin</b> (overcomes pneumococcal resistance). Severe/resistant or antibiotics in the last month &rarr; <b>amoxicillin-clavulanate</b>. Penicillin allergy &rarr; cefdinir or azithromycin (up to 50% of pneumococci macrolide-resistant). <b>No improvement in 3 days = failure</b> &rarr; amoxicillin-clavulanate or cefdinir &rarr; <b>ceftriaxone</b> intramuscular/intravenous."],
 ["Sinusitis","Bacterial only if <b>&gt;10 days or worsening</b>. <b>Amoxicillin-clavulanate</b> (beta-lactamase <i>H. influenzae</i>). Allergy &rarr; <b>clindamycin + cefixime</b>, or <b>levofloxacin</b>. Saline irrigation helps."],
 ["Pharyngitis","Goal: prevent <b>rheumatic fever</b> and suppurative complications. <b>Rapid strep test</b> first. Amoxicillin 10 days or <b>benzathine penicillin G</b> once. Allergy: cephalexin, clindamycin, azithromycin."],
 ["Otic drops","Antibiotic + steroid (growth &darr; + cytokines &darr;). <b>Polymyxin B: NOT with ruptured eardrum or tubes</b> &mdash; cochlear damage, hearing loss. Neomycin &rarr; hypersensitivity. Ciprofloxacin/dexamethasone = expensive &rarr; ofloxacin + dexamethasone ophthalmic."],
 ["Antifungals","<b>Nystatin</b>: NOT absorbed; binds membrane sterols; <b>oral thrush</b> (inhaled steroids, HIV/AIDS, chemotherapy); only GI effects. <b>Ketoconazole</b>: systemic fungal infection; <b>CYP3A4 inhibitor</b>; <b>QTc prolongation</b>; hepatitis &rarr; hepatic failure; hyperlipidemia, orthostatic hypotension."],
]},
{"id":"ent-pain","label":"ENT &middot; aspirin, NSAIDs, acetaminophen","color":"#8c4a2f","rows":[
 ["Aspirin","<b>IRREVERSIBLE</b>, noncompetitive platelet inhibitor; non-selective COX-1/COX-2 (cyclooxygenase). Oral &rarr; hepatic conjugation &rarr; renal excretion."],
 ["The ladder (no grams)","Antiplatelet &rarr; analgesic/antipyretic &rarr; anti-inflammatory (<b>TINNITUS</b>) &rarr; salicylism: hyperventilation + alkalosis &rarr; fever, dehydration, <b>metabolic acidosis</b> &rarr; shock, coma, death."],
 ["Aspirin contraindications","Bleeding disorders &middot; pregnancy (very low dose may help pre-eclampsia) &middot; <b>child with viral fever (chickenpox, influenza) &rarr; REYE SYNDROME</b>."],
 ["Reye syndrome","Under 15; <b>50% mortality</b>; vomiting, progressive CNS damage, hepatic injury, <b>hypoglycemia</b>; fatty liver, cerebral edema; 5 stages ending in seizures and death."],
 ["Ibuprofen","<b>REVERSIBLE</b> COX-1/2 inhibitor. Ulcers/bleeding, edema, <b>acute renal failure</b>. Interactions: &darr; ACE-inhibitor effect; diuretics &rarr; renal failure; &uarr; <b>lithium</b> and <b>methotrexate</b> (toxic); anticoagulants &rarr; GI bleeds. Avoid: asthma, <b>under 6 months</b>, ulcer history, renal dysfunction. Naproxen = longer half-life."],
 ["Acetaminophen","Analgesic + antipyretic, NOT anti-inflammatory; mechanism unclear; well tolerated. <b>Chronic alcohol &rarr; liver damage.</b>"],
]},
{"id":"ent-hist","label":"ENT &middot; antihistamines &amp; steroids","color":"#5b4a8a","rows":[
 ["Triple response","Redness (direct vasodilation) &middot; wheal (post-capillary permeability) &middot; flare (axon-reflex vasodilation). H1: permeability, bronchoconstriction, itch. H2: gastric acid, cardiac contractility."],
 ["1st vs 2nd generation","<b>1st generation enters the CNS</b> + hits muscarinic/serotonin receptors &rarr; <b>SEDATION</b> (additive with alcohol; doxylamine sleep aid), antiemetic, dry mouth, urinary retention, blurred vision; excitation in children/overdose. <b>2nd generation (cetirizine, fexofenadine, loratadine) &rarr; little sedation.</b>"],
 ["Named agents","<b>Promethazine</b> = strongest antimuscarinic, motion sickness. Meclizine, hydroxyzine = high antiemetic. <b>Azelastine</b> = nasal H1 blocker; <b>bitter taste, epistaxis</b>."],
 ["H1 uses","Allergic rhinitis, urticaria, insect bites, drug reactions; motion sickness and vestibular upset; sleep aids; <b>adjuvant</b> in anaphylaxis."],
 ["Nasal steroids","Beclomethasone, budesonide, flunisolide, <b>fluticasone (Flonase, not Flovent)</b>, mometasone, triamcinolone. Allergic/vasomotor rhinitis. <b>Epistaxis, septal perforation</b>, bad taste."],
 ["Systemic steroids","Dexamethasone, prednisone/prednisolone. Fluid/sodium retention, <b>potassium loss</b>, hyperglycemia, <b>tendon rupture</b>, cataract/glaucoma, infection. <b>Contraindicated in systemic fungal infection.</b> Dexamethasone + diuretic &rarr; hypokalemia (&rarr; arrhythmia with digoxin); macrolides &darr; its clearance. <b>Do not stop abruptly</b>; avoid live vaccines on prednisone."],
]},
{"id":"ent-cough","label":"ENT &middot; decongestants &amp; cough","color":"#3d6b52","rows":[
 ["Decongestants","All <b>alpha agonists</b>. <b>Oxymetazoline</b> spray: <b>3&ndash;5 days max &rarr; rebound rhinitis (rhinitis medicamentosa)</b>; MAOI interaction. <b>Pseudoephedrine</b> oral: tachycardia, hypertension, headache; <b>&darr; antihypertensive effect</b>; eustachian tube dysfunction. Phenylephrine = pseudoephedrine-free (Sudafed PE)."],
 ["Spray technique","Head down, <b>aim away from the septum</b>, <b>right hand &rarr; left nostril</b>, don&rsquo;t tilt back, no other sprays; nosebleed &rarr; stop and follow up."],
 ["Antitussives","<b>Benzonatate</b>: numbs lung <b>stretch receptors</b>; non-productive cough; <b>swallow whole</b> (chewing numbs mouth); tetracaine allergy. <b>Dextromethorphan</b>: <b>medullary cough center, sigma receptor</b>; <b>serotonin syndrome</b>; no MAOI within 2 weeks."],
 ["Mucus","<b>Guaifenesin</b>: expectorant, &darr; viscosity; fluids; expect more drainage. <b>Dornase alfa</b>: cleaves neutrophil DNA in cystic fibrosis sputum. Hypertonic saline. <b>N-acetylcysteine</b>: splits disulfide bonds; <b>rotten-egg smell, bronchospasm</b>; also the acetaminophen antidote."],
]},
# ---------------------------------------------------------------- Lecture 6
{"id":"htn-rules","label":"Antihypertensives &middot; scope &amp; RAAS drugs","color":"#8c1d3a","rows":[
 ["NOT on it","Diuretics/heart-failure drugs (Lecture 9, Exam 3) &middot; which ACE inhibitors are prodrugs &middot; elimination routes &middot; <b>plus counts</b> in the CCB table &middot; MSA/ISA columns &middot; carteolol, betaxolol, terazosin/doxazosin detail &middot; AT2 &middot; doses."],
 ["Suffixes","-pril ACE inhibitor &middot; -sartan ARB &middot; -dipine DHP CCB &middot; -olol beta blocker (<b>N&ndash;Z non-selective, A&ndash;M beta-1 selective</b>; carvedilol, labetalol exceptions) &middot; -zosin alpha-1 blocker."],
 ["★★ HYPERKALEMIA","ACE inhibitors AND ARBs: <b>renal disease, potassium-sparing diuretics, K+ supplements, salt substitutes</b>. His strongest cue: &ldquo;very easy test question.&rdquo;"],
 ["★ ACE inhibitor uses","<b>Preferred in diabetics (kidney protective)</b>; <b>all with LV dysfunction unless contraindicated</b>; post-MI; diabetic nephropathy. Enalaprilat = intravenous."],
 ["★ ACE inhibitor harms","<b>Dry cough</b> (bradykinin, substance P; 1 week&ndash;6 months). <b>Angioedema</b> (bradykinin, first week). First-dose hypotension (sodium-depleted, heart failure, multiple drugs). <b>GFR drops dramatically</b> if angiotensin-dependent &rarr; start low, go slow. <b>2nd/3rd trimester contraindicated.</b> NSAIDs &darr; effect."],
 ["★ ARB vs ACE inhibitor","ARBs block <b>AT1</b>; <b>don&rsquo;t touch bradykinin &rarr; NO cough, less angioedema &rarr; the switch</b>. Same hyperkalemia and pregnancy rules. For LV dysfunction when an ACE inhibitor is not tolerated. Add a diuretic for more effect."],
]},
{"id":"htn-ccb","label":"Antihypertensives &middot; calcium channel blockers","color":"#b0592b","rows":[
 ["★ THE SPLIT","<b>Non-DHP (diltiazem, verapamil) = HEART</b>: slow AV conduction, &darr; rate and contractility (verapamil most). <b>DHP (-dipine) = VESSELS</b>: no AV effect. Arteries 3&ndash;10&times; more sensitive; afterload &darr;, preload unchanged."],
 ["★ Non-DHP","Angina, hypertension, <b>SVT</b> (atrial fibrillation/flutter, PSVT). <b>1st-degree AV block, bradycardia, worse heart failure</b>, <b>constipation</b>, gingival hyperplasia. Contraindicated: advanced heart block, hypotension (relative: heart failure, liver disease, GERD)."],
 ["★ CYP3A4 + P-gp","Non-DHPs <b>inhibit CYP3A4</b> (&uarr; atorvastatin, lovastatin, simvastatin, carbamazepine, propranolol, tacrolimus, cyclosporine) and <b>P-glycoprotein</b> (&uarr; digoxin). DHPs are substrates only."],
 ["★ DHP","<b>Rebound (reflex) tachycardia</b>, peripheral edema, gingival hyperplasia. <b>Nimodipine = subarachnoid hemorrhage.</b> Nicardipine = the intravenous one. Contraindicated: <b>severe aortic stenosis</b>; unstable angina/recent MI with immediate release."],
 ["Beta blocker + non-DHP","Synergistic &darr; BP, rate, contractility &rarr; <b>lower doses of each</b> (the slide allows it)."],
]},
{"id":"htn-bb","label":"Antihypertensives &middot; beta blockers","color":"#4a4f8c","rows":[
 ["Generations","1st non-selective (nadolol, pindolol, <b>propranolol</b>, sotalol, timolol) &middot; 2nd beta-1 selective (acebutolol, atenolol, bisoprolol, <b>esmolol IV</b>, metoprolol) &middot; 3rd vasodilating: <b>★ carvedilol, labetalol = alpha-1 block too</b>."],
 ["★ Hypertension","<b>Not first line.</b> Work best in young (tachycardia, high renin); fatigue, less exercise tolerance. First after MI."],
 ["★ Heart failure trio","<b>Carvedilol, metoprolol succinate, bisoprolol</b> &mdash; start very low, increase slowly (worsen at first)."],
 ["Other uses","Glaucoma (timolol), migraine prophylaxis (propranolol, timolol), hyperthyroidism (&darr; T4&rarr;T3), angina, acute MI (avoid ISA), SVT, panic, essential tremor."],
 ["★ Harms","Bronchospasm (<b>less with beta-1 selective</b>; contraindicated in COPD with bronchospasm) &middot; bradycardia, heart block &middot; <b>masked, prolonged hypoglycemia</b> &middot; cold extremities, claudication &middot; <b>sudden withdrawal &rarr; angina, MI, high BP: taper</b> &middot; <b>propranolol (lipid soluble) &rarr; depression, nightmares</b> &middot; &uarr; triglycerides."],
]},
{"id":"htn-other","label":"Antihypertensives &middot; alpha, central, vasodilators, algorithm","color":"#2f6560","rows":[
 ["Alpha-1 blockers","Prazosin: <b>orthostatic hypotension</b>, mild reflex tachycardia, sodium retention, impotence; lipids improve; NSAIDs blunt, beta blockers worsen postural drop. Terazosin/doxazosin: once daily, BPH too. <b>Tamsulosin = alpha-1A &rarr; BPH, little vascular effect.</b>"],
 ["Central alpha-2 agonists","&darr; sympathetic outflow (brainstem). Sedation, dry mouth, <b>narrow therapeutic range</b>, <b>★ abrupt-withdrawal hypertension</b>; lipid-neutral. <b>Clonidine</b>: sodium retention (+ diuretic), &uarr; glucose, blunts opiate withdrawal. <b>Guanfacine</b>: most alpha-2 selective, less sedation. (Slide 75&rsquo;s &ldquo;blocker&rdquo; is a slip &mdash; AGONIST.)"],
 ["★ Hydralazine","<b>N-acetylated &rarr; fast/slow acetylators</b>; <b>lupus syndrome</b> (high dose, long term, women, slow acetylators, Caucasians); contraindicated in CAD, elderly, ischemia; <b>stools may turn black</b>."],
 ["Minoxidil / nitroprusside","Minoxidil: <b>K+ channel opener</b>; severe reflexes, ischemia, arrhythmia, <b>hypertrichosis</b>; triple therapy for refractory HTN. Nitroprusside IV for <b>hypertensive crisis</b>; veins + arterioles; <b>cyanide &rarr; sodium thiosulfate</b>; thiocyanate with long infusion/renal failure."],
 ["★ Algorithm","&gt;20/10 above goal &rarr; <b>ACE inhibitor (OR ARB) + DHP</b>. Albuminuria (ACR &ge;300) &rarr; <b>ACE inhibitor or ARB</b>. Otherwise one of them &rarr; combine &rarr; <b>+ thiazide-like diuretic</b>. Reassess at <b>~4 weeks</b>. Failure: <b>nonadherence</b>, white coat, bad measurement."],
]},
# ---------------------------------------------------------------- Lecture 7
{"id":"lip-aid","label":"Lipids &middot; scope &amp; memory aid","color":"#7a3b6b","rows":[
 ["NOT on it","Picking an intensity for a scenario &middot; calculating 10-year risk &middot; statin PK table except the CYP row &middot; IDL &middot; ezetimibe + cyclosporine &middot; doses."],
 ["Memory aid (not fact)","Liver = depot; LDL = delivery truck (ApoB-100 badge); <b>LDL receptor = receiving gate</b>; HDL = <b>garbage truck</b>; VLDL = fuel tanker; PCSK9 = demolition crew; bile = sewer."],
 ["The drugs in the story","<b>Statins</b> cut the depot&rsquo;s own output + add gates &middot; <b>ezetimibe</b> narrows the port&rsquo;s import gate &middot; <b>resins</b> block the sewer&rsquo;s recycling (more gates, but more tankers &rarr; TG &uarr;) &middot; <b>fibrates</b> fewer tankers, more garbage trucks &middot; <b>niacin</b> cuts the fuel line from fat stores &middot; <b>PCSK9 inhibitors</b> stop the demolition crew."],
 ["★ Key point","Statins, ezetimibe, resins, PCSK9 inhibitors all end in <b>more hepatic LDL receptors</b>."],
]},
{"id":"lip-statin","label":"Lipids &middot; statins &amp; guidelines","color":"#1f6f5c","rows":[
 ["★ Mechanism","HMG-CoA reductase &darr; &rarr; less liver cholesterol &rarr; <b>&uarr; LDL receptors</b> &rarr; &darr; LDL. Pleiotropic: plaque stabilization, endothelium, antithrombotic."],
 ["★ First line","<b>Most efficacious, best tolerated</b>; first line whenever LDL lowering is indicated. &ldquo;10 times out of 10.&rdquo;"],
 ["★ CYP3A4","<b>Atorvastatin, lovastatin, simvastatin</b>; rosuvastatin minimal CYP; pravastatin non-CYP. Interactions: <b>verapamil, amiodarone, niacin, fibrates, GRAPEFRUIT JUICE</b>."],
 ["★ Harms","Liver enzymes &uarr; 0.5&ndash;2.5%, <b>serious liver problems exceedingly rare</b> &rarr; reduce/hold. <b>Myalgia &rarr; myopathy &rarr; rare rhabdomyolysis</b>; <b>combine with fibrates cautiously</b>; muscle toxicity &rarr; STOP."],
 ["★ Contraindications","<b>Hepatic disease, pregnancy.</b> Relative: cyclosporine, <b>gemfibrozil</b>, niacin, erythromycin."],
 ["★ AHA/ACC","Moderate/high intensity for the 4 groups; <b>no LDL target</b>; recheck lipids for <b>adherence</b>. Groups: <b>clinical ASCVD &middot; LDL &gt;190 &middot; diabetes 40&ndash;75 with LDL 70&ndash;189 &middot; 10-year risk &gt;7.5% with LDL 70&ndash;189</b>."],
 ["★ Intensity","High &ge;50% LDL fall = <b>atorvastatin, rosuvastatin only</b>; moderate 30&ndash;49%; low &lt;30%. Not tolerated &rarr; maximum tolerated dose. Recheck LDL at 6 weeks (expect 30&ndash;50%)."],
]},
{"id":"lip-other","label":"Lipids &middot; ezetimibe, resins, fibrates, niacin, PCSK9","color":"#a2681c","rows":[
 ["Ezetimibe","&darr; intestinal cholesterol absorption &rarr; &uarr; LDL receptors; add-on to a statin; enterohepatic (glucuronide); transaminases &uarr; with statin; <b>antacids and resins &darr; levels</b>; fibrates &rarr; gallstones."],
 ["★ Resins","Cholestyramine, colestipol, colesevelam. Bind bile acids &rarr; &uarr; LDL receptors. <b>Not absorbed &rarr; children, adolescents, PREGNANCY</b>; poorly tolerated; constipation; <b>ADEK + folate malabsorption</b>; <b>&uarr; VLDL &rarr; TG &uarr;</b>."],
 ["★ Resin contraindication","<b>Absolute: TG &gt;400, familial dysbetalipoproteinemia. Relative: TG &gt;200.</b> TG 600 &rarr; the resin is the wrong answer."],
 ["★ Resin administration","Mix powder in water/pulpy juice; <b>within 1 h of a meal</b>; other drugs (<b>digoxin, warfarin, thyroxine, beta blockers, thiazides</b>) <b>1 h before or 4 h after</b>."],
 ["★ Fibrates","<b>PPAR-alpha</b> &rarr; &darr; VLDL/TG, &uarr; ApoA-1/HDL. <b>TG &gt;1000 or low HDL.</b> Gallstones, myopathy. Contraindicated: pregnancy, severe hepatic/renal disease, gallbladder disease. <b>&uarr; warfarin effect.</b>"],
 ["★ Niacin","&darr; FFA from fat &rarr; &darr; VLDL, LDL; <b>biggest HDL rise</b>. <b>Flushing = prostaglandins &rarr; aspirin first.</b> &uarr; LFTs, glucose, uric acid. <b>Absolute: chronic liver disease</b>; relative: peptic ulcer, gout, hyperuricemia, diabetes. Alcohol interacts. Niacinamide is NOT an antilipemic."],
 ["PCSK9 inhibitors","Alirocumab, evolocumab: <b>monoclonal antibodies, injectable only</b>, expensive; keep LDL receptors active; <b>hypersensitivity</b> is the most serious reaction."],
 ["★ Which lipid","LDL &rarr; statins. <b>TG &darr; + HDL &uarr; &rarr; niacin, fibrates.</b> <b>Resins are the only class bad for TG.</b>"],
]},
]


# ---------------------------------------------------------------------------
# No-abbreviations rule, applied mechanically: the FIRST use of each
# abbreviation inside a topic block becomes "ABBR (full term)". A cram row is
# short, so expanding every occurrence would double its length; once per block
# keeps each block readable on its own. Longest keys first so "PSVT" is not
# caught as "SVT".
import re as _re
ABBR = {
    "PSVT": "paroxysmal supraventricular tachycardia", "SVT": "supraventricular tachycardia",
    "ACE": "angiotensin-converting enzyme", "ARB": "angiotensin receptor blocker",
    "ARBs": "angiotensin receptor blockers", "CCB": "calcium channel blocker",
    "DHP": "dihydropyridine", "DHPs": "dihydropyridines", "AV": "atrioventricular",
    "GERD": "gastroesophageal reflux disease", "MI": "myocardial infarction",
    "BP": "blood pressure", "CNS": "central nervous system", "GI": "gastrointestinal",
    "LV": "left ventricular", "GFR": "glomerular filtration rate",
    "CAD": "coronary artery disease", "HTN": "hypertension",
    "BPH": "benign prostatic hyperplasia", "TG": "triglycerides",
    "LDL": "low-density lipoprotein", "HDL": "high-density lipoprotein",
    "VLDL": "very-low-density lipoprotein", "FFA": "free fatty acids",
    "LFTs": "liver function tests", "PK": "pharmacokinetics",
    "IDL": "intermediate-density lipoprotein",
    "ASCVD": "atherosclerotic cardiovascular disease",
    "ACR": "urine albumin-to-creatinine ratio", "MSA": "membrane stabilizing activity",
    "ISA": "intrinsic sympathomimetic activity", "COX-1/COX-2": "cyclooxygenase-1 and -2",
    "COX-1/2": "cyclooxygenase-1 and -2", "MAOI": "monoamine oxidase inhibitor",
    "P-gp": "P-glycoprotein", "IV": "intravenous", "COPD": "chronic obstructive pulmonary disease",
    "AT1": "angiotensin II type 1 receptor", "AT2": "angiotensin II type 2 receptor",
    "CYP3A4": "cytochrome P450 3A4", "HMG-CoA": "3-hydroxy-3-methylglutaryl coenzyme A",
    "PPAR-alpha": "peroxisome proliferator-activated receptor alpha",
    "PCSK9": "proprotein convertase subtilisin/kexin type 9",
    "AHA/ACC": "American Heart Association and American College of Cardiology",
    "QTc": "corrected QT interval", "ADEK": "vitamins A, D, E and K",
    "HIV/AIDS": "human immunodeficiency virus and acquired immunodeficiency syndrome",
    "ApoA-1": "apolipoprotein A-1", "ApoB-100": "apolipoprotein B-100",
    "K+": "potassium",
}


def _expand(topic):
    seen = set()
    keys = sorted(ABBR, key=len, reverse=True)
    pat = _re.compile(r"(?<![\w/-])(" + "|".join(_re.escape(k) for k in keys) + r")(?![\w/-])")
    for row in topic["rows"]:
        for j in (0, 1):
            parts = _re.split(r"(<[^>]+>)", row[j])
            for n, part in enumerate(parts):
                if part.startswith("<"):
                    continue
                def sub(m):
                    k = m.group(1)
                    if k in seen:
                        return k
                    seen.add(k)
                    return "%s (%s)" % (k, ABBR[k])
                parts[n] = pat.sub(sub, part)
            row[j] = "".join(parts)


for _t in T:
    _expand(_t)
