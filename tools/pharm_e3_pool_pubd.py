# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Drugs for Pulmonary Infections, Asthma and COPD (Lecture 11), topic: asthma and the
bronchodilators (beta-2 agonists, theophylline, anticholinergics).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. The key is authored FIRST (c == 0);
pharm_e3_partition.py rotates it (numeric option sets are sorted ascending instead, WRITER.md rule 8).

SOURCE. Pulmonology-2.pptx slides 56-71 and 82-87: asthma definition (57), the inflammation figure (58, picture),
mast cell mediators (59, embedded picture), early and late reaction (60, picture), the leukotriene pathway (61,
picture), triggers and the methacholine challenge (62), neural pathways (63), therapeutic approaches (64), the
severity classification table (65, picture), goals of treatment (66), quick-relief versus long-term controller lists
(67), beta-2 agonists (68, 70, 71) and their signaling picture (69), methylxanthines and theophylline (82-85),
anticholinergics (86) and the anticholinergic side-effect mnemonic (87). Picture slides were read by eye into
tools/pharm_e3/ocr.json under "L11".

WRITER.md v1 (2026-10-15): every distractor carries its misconception as a third element (mis); slides only (this deck
has no speaker notes); slides win on conflict.

LEFT OUT ON PURPOSE (L11_KEYING decisions):
  * every dose, and every bare number or percentage as a key (the 60-80% genetics figure; durations of action appear
    only inside stems and explanations);
  * theophylline elimination route (slide 85 says "Renally eliminated!", which is wrong pharmacology) and every
    theophylline level number (slide 84 gives mcg/ml, slide 85 mg/ml);
  * tiotropium "(COPD only)" (slide 86): slide 90 lists add-on tiotropium in asthma steps 4-5;
  * the anticholinergic mnemonic's "bowel and bladder increase their tone" wording (slide 87; the findings it names,
    constipation and urinary retention, are used);
  * the early and late reaction curve (slide 60) and the tachykinin route (slide 63) as keys: physiology kept few
    (Dr. McInnis's weighting);
  * lipoxygenase inhibitors as a key (slide 64 names the group only; no drug is given).
  * the severity classification table (slide 65) as a key: Dr. Wood, 58:44-58:52, "I'm not going to have you, you know,
    diagnose the specific type of asthma someone has on a test question from me at least." The one severity item was
    removed by the recording pass.
mis = misconception tag on every distractor (WRITER.md rule 5)
"""

D = "Pulmonology-2.pptx"
IO_CLASS = "Identify respiratory drug classes and commonly prescribed drugs for pulmonary infections, asthma, and COPD/COLD"
IO_MOA = "Describe the molecular mechanism of action of drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_IND = "Identify indications for drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_ADME = "Describe absorption, distribution, metabolism, and excretion of drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_TOX = "Summarize side effects and toxic manifestations of respiratory drugs"
IO_AE = "Describe adverse effects of drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_CONTRA = "Identify contraindications for drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_INTER = "Discuss potential drug-drug, drug-food, and drug-herb interactions with drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_PROT = "List commonly used protocols and patient monitoring for pulmonary infections, asthma, and COPD/COLD"
IO_EDU = "Outline appropriate patient education for drugs used for pulmonary infections, asthma, and COPD/COLD"

MECH, ADJ, REV, LAY, STAGE, RULED, COMP = ("confused mechanism or drug class", "adjacent fact", "reversed direction or value",
                                           "common lay belief", "wrong stage or severity", "ruled out by a stated finding",
                                           "competing diagnosis")


def Q(topic, io, slot, q, opts, slide):
    return {"topic": topic, "io": io, "slot": slot, "q": q, "opts": opts, "c": 0, "cite": "%s, Slide %d" % (D, slide)}


QUESTIONS = [

# ---- asthma basics (slides 57-65) ------------------------------------------------------------------
Q("Asthma basics", IO_MOA, "physiology",
  "Which type of inflammation of the bronchial mucosa characterizes asthma?",
  [["Eosinophilic", "Correct. Asthma is widespread, reversible narrowing of the bronchial airways with eosinophilic inflammation of the bronchial mucosa and a marked increase in bronchial responsiveness."],
   ["Neutrophilic", "Neutrophilic inflammation is not how asthma is characterized; the inflammation of the bronchial mucosa that characterizes asthma is eosinophilic.", ADJ],
   ["Granulomatous", "Granulomatous inflammation is not how asthma is described; asthma is eosinophilic inflammation of the bronchial mucosa, with thickening of that mucosa.", COMP],
   ["Lymphocytic", "Lymphocytic inflammation is not how asthma is characterized; the inflammation of the bronchial mucosa that characterizes asthma is eosinophilic.", ADJ]], 57),

Q("Asthma basics", IO_EDU, "physiology",
  "What triggers most asthma attacks?",
  [["Viral infections", "Correct. Most asthma attacks are not triggered by allergens; most are triggered by viral respiratory infection."],
   ["Allergen exposure", "Allergens trigger fewer attacks than people expect: most asthma attacks are not triggered by allergens but by a viral respiratory infection.", LAY],
   ["Cold air exposure", "Cold air can provoke bronchospasm, as can exercise, distilled water and rapid respiratory maneuvers, but most attacks follow a viral respiratory infection.", ADJ],
   ["Aspirin ingestion", "Aspirin-induced asthma is a recognized form (montelukast is effective in it), but most asthma attacks are triggered by a viral respiratory infection.", ADJ]], 62),

Q("Asthma basics", IO_PROT, "monitoring",
  "Bronchial reactivity is assessed by the fall in forced expiratory volume in 1 second after a patient inhales increasing concentrations of which agent?",
  [["Methacholine", "Correct. Bronchial reactivity is assessed by measuring the fall in forced expiratory volume in 1 second after inhaling increasing concentrations of methacholine."],
   ["Albuterol", "Albuterol is a short-acting beta-2 agonist that relaxes bronchial smooth muscle; the agent inhaled to provoke and measure reactivity is methacholine.", REV],
   ["Ipratropium", "Ipratropium blocks acetylcholine at muscarinic receptors and causes bronchodilation; reactivity is measured after inhaling increasing concentrations of methacholine.", REV],
   ["Cromolyn", "Cromolyn is a mast cell stabilizer taken before an antigen insult to prevent attacks; the agent used to assess bronchial reactivity is methacholine.", MECH]], 62),

Q("Asthma basics", IO_MOA, "physiology",
  "Besides the direct effect of released mediators, stimulation of which airway receptors initiates reflex bronchoconstriction in asthma?",
  [["Afferent vagal receptors", "Correct. Released mediators also stimulate afferent vagal receptors in the airways to initiate reflex bronchoconstriction, and tachykinins such as substance P directly contract smooth muscle."],
   ["Beta-2 adrenergic receptors", "Stimulating beta-2 receptors raises cyclic adenosine monophosphate and relaxes airway smooth muscle; reflex bronchoconstriction starts at afferent vagal receptors.", REV],
   ["Adenosine A2B receptors", "Adenosine A2B receptors are the ones theophylline antagonizes as part of its action; the reflex route of bronchoconstriction starts at afferent vagal receptors.", MECH],
   ["Mast cell immunoglobulin E receptors", "Immunoglobulin E receptors on mast cells trigger degranulation, the direct mediator route; the reflex route of bronchoconstriction begins at afferent vagal receptors.", ADJ]], 63),

Q("Asthma basics", IO_MOA, "physiology",
  "When allergen binds immunoglobulin E on a mast cell, which mediator is released immediately from the granules?",
  [["Histamine", "Correct. Histamine is a granule content, released immediately; the membrane-derived lipid mediators follow over minutes and the cytokines over hours."],
   ["Leukotrienes", "Leukotrienes are membrane-derived lipid mediators made over minutes, along with prostaglandins and platelet-activating factor; histamine is released immediately.", STAGE],
   ["Interleukins", "Interleukins are cytokines produced over hours; histamine is the granule content released immediately.", STAGE],
   ["Prostaglandins", "Prostaglandins are lipid mediators made from the cell membrane over minutes; histamine comes out of the granules immediately.", STAGE]], 59),


# ---- treatment approaches and goals (slides 64, 66, 67) --------------------------------------------
Q("Treatment approaches", IO_CLASS, "class",
  "Albuterol, ipratropium and theophylline share which therapeutic approach to asthma?",
  [["Reversing bronchospasm", "Correct. Beta-2 agonists, ipratropium and theophylline all reverse bronchospasm; cromolyn and nedocromil remove the trigger, and steroids control inflammation."],
   ["Removing the trigger", "Removing the trigger or antigen is the approach of the mast cell stabilizers cromolyn and nedocromil; albuterol, ipratropium and theophylline reverse bronchospasm.", MECH],
   ["Controlling inflammation", "Controlling inflammation is the approach of steroids and lipoxygenase inhibitors; albuterol, ipratropium and theophylline reverse bronchospasm.", MECH],
   ["Blocking immunoglobulin E", "Binding circulating immunoglobulin E is how omalizumab controls inflammation; albuterol, ipratropium and theophylline reverse bronchospasm.", MECH]], 64),

Q("Treatment approaches", IO_IND, "drug choice",
  "Which drug group reduces the level of bronchial responsiveness in asthma over the long term?",
  [["Inhaled corticosteroids", "Correct. Bronchial responsiveness is related to airway inflammation and is reduced long term with anti-inflammatory agents such as inhaled corticosteroids."],
   ["Short-acting beta-2 agonists", "Short-acting beta-2 agonists treat acute bronchospasm; reducing responsiveness long term needs anti-inflammatory agents such as inhaled corticosteroids.", STAGE],
   ["Anticholinergics", "Anticholinergics are quick-relief bronchodilators that block muscarinic receptors; long-term responsiveness is reduced by inhaled corticosteroids.", STAGE],
   ["Histamine H1 blockers", "Histamine H1 blockers relieve the rash, itching and hives of anaphylaxis; long-term bronchial responsiveness is reduced by inhaled corticosteroids.", ADJ]], 66),

Q("Treatment approaches", IO_IND, "drug choice",
  "Which drug group is used to reverse acute bronchospasm in asthma?",
  [["Short-acting beta-2 agonists", "Correct. Acute bronchospasm is prevented by avoiding triggers and reversed with short-acting beta-2 agonists, which work rapidly and last 4 to 6 hours."],
   ["Inhaled corticosteroids", "Inhaled corticosteroids inhibit the inflammatory cascade and take up to 8 weeks for maximal effect; acute bronchospasm is reversed with short-acting beta-2 agonists.", STAGE],
   ["Mast cell stabilizers", "Mast cell stabilizers must be taken before the antigen insult and may take up to 4 weeks to work; acute bronchospasm calls for a short-acting beta-2 agonist.", STAGE],
   ["Leukotriene modifiers", "Leukotriene modifiers such as montelukast are long-term controller medications; acute bronchospasm is reversed with a short-acting beta-2 agonist.", STAGE]], 66),

Q("Treatment approaches", IO_CLASS, "class",
  "Besides short-acting beta-2 agonists and systemic corticosteroids, which drug group is a quick-relief asthma medication?",
  [["Anticholinergics", "Correct. The quick-relief medications are short-acting beta-2 agonists, anticholinergics and systemic corticosteroids."],
   ["Leukotriene modifiers", "Leukotriene modifiers are long-term controller medications, alongside inhaled corticosteroids and mast cell stabilizers; anticholinergics are for quick relief.", MECH],
   ["Mast cell stabilizers", "Mast cell stabilizers are long-term controllers that must be taken regularly; the third quick-relief group is the anticholinergics.", MECH],
   ["Methylxanthines", "Methylxanthines such as theophylline are long-term controller medications; anticholinergics are listed among the quick-relief medications.", MECH]], 67),

Q("Treatment approaches", IO_CLASS, "class",
  "Which long-term controller medication is a methylxanthine?",
  [["Theophylline", "Correct. Theophylline is the methylxanthine among the long-term controllers; it is a nonspecific phosphodiesterase inhibitor with a narrow therapeutic index."],
   ["Montelukast", "Montelukast is a long-term controller, but it is a leukotriene modifier (an oral leukotriene D4 antagonist), not a methylxanthine; theophylline is.", MECH],
   ["Cromolyn", "Cromolyn is a long-term controller of the mast cell stabilizer group, taken before antigen exposure; the methylxanthine is theophylline.", MECH],
   ["Salmeterol", "Salmeterol is a long-term controller of the long-acting beta-2 agonist group, never used alone in asthma; the methylxanthine is theophylline.", MECH]], 67),

Q("Treatment approaches", IO_EDU, "education",
  "Besides treating bronchospasm with a short-acting beta-2 agonist, what helps prevent acute bronchospasm in asthma?",
  [["Avoiding allergens and triggers", "Correct. Acute bronchospasm is prevented or reversed by avoiding allergens and asthma triggers and by treating with short-term beta-2 agonists."],
   ["Taking routine antibiotics", "Routine antibiotics have no listed role in preventing bronchospasm and are not recommended even for acute bronchitis; avoiding allergens and triggers is the measure.", LAY],
   ["Exercising in cold air", "Exercise and cold air both provoke bronchospasm in asthma, so they are triggers to manage rather than a form of prevention; avoid allergens and triggers instead.", REV],
   ["Inhaling distilled water mist", "Distilled water is itself a provoker of bronchospasm in asthma; prevention means avoiding allergens and asthma triggers.", REV]], 66),

# ---- beta-2 agonists (slides 68-71) ----------------------------------------------------------------
Q("Beta-2 agonists", IO_MOA, "mechanism",
  "Beta-2 agonists relax airway smooth muscle by increasing which intracellular messenger?",
  [["Cyclic adenosine monophosphate", "Correct. Beta-2 agonists increase cyclic adenosine monophosphate, which inhibits myosin light chain kinase and relaxes airway smooth muscle."],
   ["Cyclic guanosine monophosphate", "Cyclic guanosine monophosphate rises, with cyclic adenosine monophosphate, when theophylline inhibits phosphodiesterase; beta-2 agonists act by increasing cyclic adenosine monophosphate.", ADJ],
   ["Intracellular calcium", "Calcium entering through L-type channels or released from the sarcoplasmic reticulum binds calmodulin and drives contraction; beta-2 agonists raise cyclic adenosine monophosphate instead.", REV],
   ["Acetylcholine", "Acetylcholine acts on muscarinic receptors, which ipratropium blocks to cause bronchodilation; beta-2 agonists act by increasing cyclic adenosine monophosphate.", MECH]], 68),

Q("Beta-2 agonists", IO_MOA, "mechanism",
  "In airway smooth muscle, the cyclic adenosine monophosphate produced after beta-2 receptor stimulation inhibits which enzyme?",
  [["Myosin light chain kinase", "Correct. The beta-2 receptor acts through the stimulatory G protein to make cyclic adenosine monophosphate, which inhibits myosin light chain kinase, so the myosin light chain is not phosphorylated and the muscle relaxes."],
   ["Phosphodiesterase", "Phosphodiesterase is the enzyme theophylline inhibits, which raises cyclic adenosine monophosphate; in the beta-2 pathway cyclic adenosine monophosphate inhibits myosin light chain kinase.", MECH],
   ["Myosin light chain phosphatase", "The phosphatase removes the phosphate from the myosin light chain, reversing the kinase step; cyclic adenosine monophosphate inhibits myosin light chain kinase itself.", REV],
   ["5-lipoxygenase", "5-lipoxygenase converts arachidonic acid toward the leukotrienes; the enzyme inhibited in the beta-2 pathway is myosin light chain kinase.", ADJ]], 69),

Q("Beta-2 agonists", IO_CLASS, "class",
  "Which inhaled bronchodilator is a short-acting beta-2 agonist?",
  [["Levalbuterol", "Correct. The short-acting beta-2 agonists are albuterol (Proair, Ventolin) and levalbuterol (Xopenex)."],
   ["Salmeterol", "Salmeterol (Serevent) is a long-acting beta-2 agonist that lasts 12 or more hours and must not be used alone for asthma; levalbuterol is short-acting.", MECH],
   ["Formoterol", "Formoterol (Foradil) is a long-acting beta-2 agonist, also found in Symbicort and Dulera; levalbuterol is the short-acting choice here.", MECH],
   ["Tiotropium", "Tiotropium (Spiriva) is a long-acting anticholinergic lasting 24 hours or more, not a beta-2 agonist; levalbuterol is a short-acting beta-2 agonist.", MECH]], 70),

Q("Beta-2 agonists", IO_CONTRA, "contraindication",
  "Which restriction applies to long-acting beta-2 agonists in asthma?",
  [["They must not be used alone", "Correct. Long-acting beta-2 agonists (formoterol, salmeterol) are not to be used alone for asthma; the combination inhalers pair each with an inhaled corticosteroid."],
   ["They must be taken before exposure", "Taking a drug before the antigen insult is the rule for the mast cell stabilizers cromolyn and nedocromil; long-acting beta-2 agonists must not be used alone.", ADJ],
   ["They need plasma level monitoring", "Plasma level monitoring belongs to theophylline, which has a narrow therapeutic index; long-acting beta-2 agonists must not be used alone in asthma.", ADJ],
   ["They must be given intravenously", "Intravenous use is listed for aminophylline and reslizumab, not for formoterol or salmeterol; in asthma, long-acting beta-2 agonists must not be used alone.", ADJ]], 70),

Q("Beta-2 agonists", IO_ADME, "drug choice",
  "Which drug works rapidly and lasts about 4 to 6 hours?",
  [["Albuterol", "Correct. Short-acting beta-2 agonists such as albuterol work rapidly and last 4 to 6 hours, which suits quick relief."],
   ["Salmeterol", "Salmeterol is a long-acting beta-2 agonist that lasts 12 or more hours; the rapid, 4-to-6-hour drug is albuterol.", REV],
   ["Tiotropium", "Tiotropium is a long-acting anticholinergic that lasts 24 hours or more; albuterol is the rapid drug that lasts 4 to 6 hours.", REV],
   ["Formoterol", "Formoterol is a long-acting beta-2 agonist lasting 12 or more hours; albuterol is the short-acting one, lasting 4 to 6 hours.", REV]], 68),

Q("Beta-2 agonists", IO_AE, "adverse effect",
  "Besides tremor and tachycardia, which metabolic adverse effect is listed for beta-2 agonists?",
  [["Hyperglycemia", "Correct. Beta-2 agonist adverse effects are tachycardia, hypotension, headache, dizziness, insomnia, tremors and hyperglycemia."],
   ["Hypoglycemia", "The direction is reversed: beta-2 agonists raise blood sugar, listed as hyperglycemia, an effect systemic corticosteroids share.", REV],
   ["Hyperuricemia", "Raised uric acid is listed for ethambutol and pyrazinamide; the metabolic adverse effect of beta-2 agonists is hyperglycemia.", ADJ],
   ["Hyperthermia", "Hyperthermia ('hot as Hades') belongs to anticholinergic toxicity; beta-2 agonists list hyperglycemia among their adverse effects.", ADJ]], 71),

Q("Beta-2 agonists", IO_AE, "adverse effect",
  "Which pair of adverse effects is listed for beta-2 agonists as a class?",
  [["Increased heart rate and tremor", "Correct. Beta-2 agonists increase cyclic adenosine monophosphate and relax airway smooth muscle, but they cause increased heart rate and tremor."],
   ["Thrush and growth suppression", "Oral candidiasis and growth suppression in children are the inhaled corticosteroid adverse effects; beta-2 agonists cause increased heart rate and tremor.", ADJ],
   ["Dry mouth and urinary retention", "Dry mouth and urinary retention belong to anticholinergic toxicity; the beta-2 agonist pair is increased heart rate and tremor.", ADJ],
   ["Convulsions and arrhythmias", "Convulsions and arrhythmias are the dangers of high theophylline levels; beta-2 agonists cause increased heart rate and tremor.", ADJ]], 68),

Q("Beta-2 agonists", IO_AE, "adverse effect",
  "Which combination of heart rate and blood pressure changes is listed among the adverse effects of beta-2 agonists?",
  [["Tachycardia and hypotension", "Correct. The beta-2 agonist adverse effects are tachycardia, hypotension, headache, dizziness, insomnia, tremors and hyperglycemia."],
   ["Tachycardia and hypertension", "Tachycardia with hypertension is the anticholinergic pattern ('the heart runs alone') and an epinephrine effect; beta-2 agonists list tachycardia with hypotension.", ADJ],
   ["Bradycardia and hypotension", "Beta-2 agonists speed the heart rather than slow it: they list tachycardia, together with hypotension.", REV],
   ["Bradycardia and hypertension", "Both directions are reversed: beta-2 agonists list tachycardia and hypotension among their adverse effects.", REV]], 71),

# ---- theophylline (slides 82-85) -------------------------------------------------------------------
Q("Theophylline", IO_MOA, "mechanism",
  "Besides inhibiting phosphodiesterase, which receptor action is part of theophylline's mechanism?",
  [["Adenosine receptor antagonism", "Correct. Theophylline inhibits phosphodiesterase (4 and 5), raising cyclic adenosine and guanosine monophosphate, antagonizes the adenosine A2B receptor, and has anti-inflammatory actions in the late response."],
   ["Muscarinic receptor blockade", "Muscarinic receptor blockade is the anticholinergic mechanism of ipratropium and tiotropium; theophylline antagonizes adenosine receptors.", MECH],
   ["Beta-2 receptor stimulation", "Beta-2 receptor stimulation is how albuterol and salmeterol raise cyclic adenosine monophosphate; theophylline is an adenosine receptor antagonist.", MECH],
   ["Leukotriene receptor blockade", "Leukotriene D4 receptor blockade is montelukast's mechanism; theophylline antagonizes the adenosine A2B receptor.", MECH]], 83),

Q("Theophylline", IO_PROT, "monitoring",
  "Why are theophylline plasma levels monitored?",
  [["It has a narrow therapeutic index", "Correct. Theophylline has a narrow therapeutic index, so plasma levels are monitored; rising levels bring nausea, vomiting and cardiac effects, then seizures and arrhythmias."],
   ["It induces liver enzymes", "Inducing cytochrome P450 enzymes is rifampin's interaction problem (theophylline is one of the drugs affected); theophylline is watched because of its narrow therapeutic index.", ADJ],
   ["It causes adrenal suppression", "Adrenal suppression is a systemic corticosteroid side effect; theophylline levels are monitored because its therapeutic index is narrow.", ADJ],
   ["Its effect takes 8 weeks", "Up to 8 weeks for maximal effect describes inhaled corticosteroids; theophylline is monitored for its narrow therapeutic index.", ADJ]], 85),

Q("Theophylline", IO_TOX, "adverse effect",
  "At toxic levels, which central nervous system effect of theophylline is the danger?",
  [["Convulsions", "Correct. Theophylline is a central nervous system stimulant, and at high levels it causes convulsions; as a cardiac stimulant it also causes arrhythmias."],
   ["Drowsiness", "Theophylline stimulates rather than sedates the central nervous system (insomnia is on its list); at toxic levels the danger is convulsions.", REV],
   ["Emergence phenomenon", "Emergence phenomenon is an adverse reaction to ketamine in status asthmaticus; theophylline toxicity causes convulsions.", ADJ],
   ["Peripheral neuritis", "Peripheral neuritis from pyridoxine deficiency is isoniazid's toxicity; theophylline at toxic levels causes convulsions.", ADJ]], 84),

Q("Theophylline", IO_TOX, "adverse effect",
  "Besides convulsions, which danger of high theophylline levels comes from its action as a cardiac stimulant?",
  [["Arrhythmias", "Correct. Theophylline is a cardiac stimulant, and high levels cause arrhythmias; as a central nervous system stimulant it also causes convulsions."],
   ["Bradycardia", "Theophylline stimulates the heart rather than slowing it; the cardiac danger of high levels is arrhythmias.", REV],
   ["Hypotension", "Hypotension is on the beta-2 agonist adverse effect list; theophylline, a cardiac stimulant, causes arrhythmias at high levels.", ADJ],
   ["Pulmonary edema", "Pulmonary edema is a consequence of epinephrine overdose; the cardiac danger of high theophylline levels is arrhythmias.", ADJ]], 84),

Q("Theophylline", IO_AE, "adverse effect",
  "Which effect on the stomach is listed among theophylline's adverse effects?",
  [["Stimulation of gastric acid", "Correct. Theophylline stimulates gastric acid, and nausea and heartburn are on the methylxanthine adverse effect list."],
   ["Blockade of gastric acid", "Blocking gastric acid secretion is what famotidine, a histamine H2 blocker, does; theophylline stimulates gastric acid.", REV],
   ["Constipation", "Constipation belongs to anticholinergic toxicity; theophylline's listed effect on the stomach is stimulation of gastric acid.", ADJ],
   ["Oral thrush", "Oral candidiasis is an inhaled corticosteroid adverse effect; theophylline's listed effect on the stomach is stimulation of gastric acid.", ADJ]], 84),

Q("Theophylline", IO_AE, "adverse effect",
  "Which change involving urine is listed for theophylline?",
  [["A diuretic effect", "Correct. Theophylline has diuretic effects, alongside gastric acid stimulation, smooth muscle relaxation and central nervous system and cardiac stimulation."],
   ["Urinary retention", "Urinary retention is part of anticholinergic toxicity; theophylline has a diuretic effect instead.", REV],
   ["Orange discoloration", "Orange urine, tears and sweat come from rifampin; theophylline's listed effect on urine is a diuretic effect.", ADJ],
   ["Less uric acid excretion", "Inhibiting uric acid excretion is pyrazinamide's effect, which makes patients hyperuricemic; theophylline has a diuretic effect.", ADJ]], 84),

Q("Theophylline", IO_IND, "drug choice",
  "How does theophylline compare with long-acting bronchodilators?",
  [["Less effective and less well tolerated", "Correct. Compared with long-acting bronchodilators, methylxanthines are less effective and less well tolerated, and theophylline has limited use."],
   ["More effective but less well tolerated", "Theophylline is not more effective: it is both less effective and less well tolerated than long-acting bronchodilators.", REV],
   ["Equally effective and better tolerated", "Theophylline is neither as effective nor as well tolerated: it is less effective and less well tolerated than long-acting bronchodilators.", REV],
   ["Less effective but better tolerated", "Theophylline is not better tolerated: it has a narrow therapeutic index and is both less effective and less well tolerated.", REV]], 82),

Q("Theophylline", IO_IND, "indication",
  "Besides its limited use in asthma, theophylline is used in which condition?",
  [["Chronic obstructive pulmonary disease", "Correct. Theophylline (available only as a generic) has limited use and is used in chronic obstructive pulmonary disease."],
   ["Ventilator-associated pneumonia", "Ventilator-associated pneumonia is a nosocomial pneumonia treated with broad-spectrum antibiotics; theophylline's listed use is chronic obstructive pulmonary disease.", ADJ],
   ["Acute bronchitis", "Acute bronchitis is generally self-limited and gets symptomatic, supportive care; theophylline's listed use is chronic obstructive pulmonary disease.", ADJ],
   ["Anaphylaxis", "Anaphylaxis is treated with epinephrine, fluids, histamine blockers, albuterol and corticosteroids; theophylline is used in chronic obstructive pulmonary disease.", ADJ]], 83),

Q("Theophylline", IO_ADME, "class",
  "Which drug is the intravenous form of theophylline?",
  [["Aminophylline", "Correct. Theophylline is the methylxanthine, and aminophylline is its intravenous form."],
   ["Methylprednisolone", "Methylprednisolone is a corticosteroid given orally or parenterally in anaphylaxis and asthma exacerbations; the intravenous methylxanthine is aminophylline.", MECH],
   ["Reslizumab", "Reslizumab is an anti-interleukin-5 biologic given intravenously, not a methylxanthine; aminophylline is theophylline's intravenous form.", MECH],
   ["Levalbuterol", "Levalbuterol (Xopenex) is a short-acting beta-2 agonist, not a methylxanthine; aminophylline is theophylline's intravenous form.", MECH]], 82),

# ---- anticholinergics (slides 86-87) ---------------------------------------------------------------
Q("Anticholinergics", IO_ADME, "drug choice",
  "Which bronchodilator lasts 24 hours or more?",
  [["Tiotropium", "Correct. Tiotropium (Spiriva) is the long-acting anticholinergic and lasts 24 hours or more; ipratropium lasts up to 8 hours."],
   ["Ipratropium", "Ipratropium (Atrovent) is the short-acting anticholinergic and lasts up to 8 hours; tiotropium lasts 24 hours or more.", REV],
   ["Albuterol", "Albuterol is a short-acting beta-2 agonist that works rapidly and lasts 4 to 6 hours; tiotropium lasts 24 hours or more.", REV],
   ["Levalbuterol", "Levalbuterol is a short-acting beta-2 agonist lasting 4 to 6 hours; the bronchodilator lasting 24 hours or more is tiotropium.", REV]], 86),

Q("Anticholinergics", IO_CLASS, "class",
  "Ipratropium (Atrovent) belongs to which drug class?",
  [["Anticholinergics", "Correct. Ipratropium is the short-acting anticholinergic: it blocks acetylcholine's effect on muscarinic receptors, causing bronchodilation, and lasts up to 8 hours."],
   ["Beta-2 agonists", "Beta-2 agonists such as albuterol increase cyclic adenosine monophosphate; ipratropium is an anticholinergic that blocks muscarinic receptors.", MECH],
   ["Methylxanthines", "Methylxanthines such as theophylline are nonspecific phosphodiesterase inhibitors; ipratropium is an anticholinergic bronchodilator.", MECH],
   ["Mast cell stabilizers", "Mast cell stabilizers (cromolyn, nedocromil) must be taken before antigen exposure; ipratropium is an anticholinergic bronchodilator.", MECH]], 86),

Q("Anticholinergics", IO_MOA, "mechanism",
  "How do ipratropium and tiotropium cause bronchodilation?",
  [["They block muscarinic receptors", "Correct. Anticholinergics block acetylcholine's effect on muscarinic receptors, which produces bronchodilation."],
   ["They stimulate beta-2 receptors", "Stimulating beta-2 receptors is how albuterol and salmeterol work, by increasing cyclic adenosine monophosphate; anticholinergics block muscarinic receptors.", MECH],
   ["They inhibit phosphodiesterase", "Phosphodiesterase inhibition is theophylline's mechanism; ipratropium and tiotropium block acetylcholine at muscarinic receptors.", MECH],
   ["They stabilize mast cells", "Mast cell stabilization is the action of cromolyn and nedocromil; ipratropium and tiotropium block acetylcholine at muscarinic receptors.", MECH]], 86),

Q("Anticholinergics", IO_TOX, "adverse effect",
  "Which eye finding is part of anticholinergic toxicity?",
  [["Mydriasis", "Correct. 'Blind as a bat' stands for blurry vision and mydriasis (dilated pupils) in anticholinergic toxicity."],
   ["Miosis", "Miosis (a small pupil) is the reverse; anticholinergic toxicity dilates the pupil, giving mydriasis and blurry vision.", REV],
   ["Red-green color loss", "Decreased red-green discrimination is ethambutol's visual toxicity; anticholinergics cause blurry vision and mydriasis.", ADJ],
   ["Orange-colored tears", "Orange tears, sweat and urine come from rifampin; the anticholinergic eye findings are blurry vision and mydriasis.", ADJ]], 87),

Q("Anticholinergics", IO_TOX, "adverse effect",
  "A patient develops flushing, fever, dry mouth and a fast heart rate after taking an anticholinergic. Which other finding belongs to the same toxicity pattern?",
  [["Urinary retention", "Correct. Anticholinergic toxicity also affects the bowel and bladder, giving constipation and urinary retention, alongside flushing, fever, dry mouth and tachycardia."],
   ["Diarrhea", "Anticholinergic toxicity causes constipation, not diarrhea, along with urinary retention, flushing, fever and dry mouth.", REV],
   ["Excess salivation", "The dry mouth already present rules this out: anticholinergics cause dry mouth and dry eyes; urinary retention fits the pattern.", RULED],
   ["Bradycardia", "The fast heart rate already present rules this out: anticholinergic toxicity causes tachycardia and hypertension; urinary retention completes the pattern.", RULED]], 87),

Q("Anticholinergics", IO_TOX, "adverse effect",
  "Which central nervous system effect is listed in anticholinergic toxicity?",
  [["Delirium", "Correct. 'Mad as a hatter' stands for hallucinations, delirium, memory loss and psychosis in anticholinergic toxicity."],
   ["Emergence phenomenon", "Emergence phenomenon is an adverse reaction to ketamine, used in status asthmaticus when the patient is intubated; anticholinergics cause delirium and hallucinations.", ADJ],
   ["Euphoria", "Euphoria is on isoniazid's central nervous system list with seizures; the anticholinergic list is hallucinations, delirium, memory loss and psychosis.", ADJ],
   ["Insomnia", "Insomnia is listed for beta-2 agonists and theophylline; anticholinergic toxicity causes hallucinations, delirium, memory loss and psychosis.", ADJ]], 87),

Q("Anticholinergics", IO_TOX, "adverse effect",
  "Which skin finding is part of anticholinergic toxicity?",
  [["Flushing", "Correct. 'Red as a beet' stands for flushing in anticholinergic toxicity, along with fever and hyperthermia ('hot as Hades')."],
   ["Urticaria", "Urticaria is a rare side effect of anti-immunoglobulin E therapy such as omalizumab; anticholinergic toxicity causes flushing.", ADJ],
   ["Dermal thinning", "Dermal thinning is a side effect of systemic corticosteroids; the anticholinergic skin finding is flushing.", ADJ],
   ["Diaphoresis", "Diaphoresis (sweating) is an adverse effect of epinephrine; anticholinergic toxicity causes dry mouth and dry eyes with flushing.", REV]], 87),
]
