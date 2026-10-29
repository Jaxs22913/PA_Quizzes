# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Drugs for Pulmonary Infections, Asthma and COPD (Lecture 11), topic: the asthma
controllers (inhaled corticosteroids, combination inhalers, montelukast, mast cell stabilizers, omalizumab and the other
biologics, oral systemic corticosteroids).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. The key is authored FIRST (c == 0);
pharm_e3_partition.py rotates it (numeric option sets are sorted ascending instead, WRITER.md rule 8).

SOURCE. Pulmonology-2.pptx slides 72-81 and 88-89: inhaled corticosteroids and their brands (72), their mechanism,
onset and adverse effects (73), the combination inhalers (74), montelukast (75), the leukotriene pathway (76, embedded
picture, read by eye into tools/pharm_e3/ocr.json under "L11"), mast cell stabilizers (77-78), omalizumab (79), anti-
immunoglobulin E side effects (80), the other biologics (81), oral systemic corticosteroids (88) and their side effects
(89).

WRITER.md v1 (2026-10-15): every distractor carries its misconception as a third element (mis); slides only (this deck
has no speaker notes); slides win on conflict.

LEFT OUT ON PURPOSE (L11_KEYING decisions):
  * which interleukin each biologic targets as a key (interleukin-5 against interleukin-4): Dr. Wood, 1:14:19-1:14:29, "I'm
    not going to really care if you know the difference between the two, I would just recognize that these are affecting
    interleukin." Items ask "interleukins" against immunoglobulin E instead (recording pass);
  * montelukast's side-effect profile stays unasked although Dr. Wood repeated "pretty minimal side effects" (1:09:59):
    current labeling carries a boxed warning (flagged for Jaxon);
  * every dose and every bare number or percentage as a key (omalizumab's every-2-to-4-weeks interval, the 0.1 percent
    urticaria and anaphylaxis figures and the eosinophil cut-off appear only inside explanations);
  * montelukast's side-effect profile ("minimal and well tolerated", slide 75): current labeling carries a boxed
    warning for neuropsychiatric events;
  * the Nasalcrom brand for inhaled cromolyn (slide 78: Nasalcrom is the nasal spray);
  * benralizumab's target (slide 81 groups it as anti-IL-5; it targets the IL-5 receptor): named only as a member of
    the anti-interleukin-5 group, never contrasted with mepolizumab;
  * (changed by the recording pass) the systemic corticosteroid "taper if duration > 5 days" rule (slide 89) is asked
    ONCE, because Dr. Wood affirmed it aloud (1:22:13); the guide notes that many references taper only longer courses;
  * dexamethasone and methylprednisolone as an "oral liquid" answer (slide 88 lists both as oral or parenteral; only
    prednisolone is listed as the oral liquid);
  * lipoxygenase inhibitors as a key (slide 64 names the group; no drug is given);
  * the mast cell stabilizer mechanism "unknown (may interfere with Ca++)" as a key (the action asked is "stabilize
    mast cells").
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
    """`slide` is one slide number, or a tuple (primary slide first) when the deciding fact spans slides."""
    if isinstance(slide, tuple):
        cite = "%s, Slides %s" % (D, ", ".join(str(s) for s in slide))
    else:
        cite = "%s, Slide %d" % (D, slide)
    return {"topic": topic, "io": io, "slot": slot, "q": q, "opts": opts, "c": 0, "cite": cite}


QUESTIONS = [

# ---- inhaled corticosteroids (slides 72-73) --------------------------------------------------------
Q("Inhaled corticosteroids", IO_CLASS, "class",
  "Fluticasone (Flovent) belongs to which drug class?",
  [["Inhaled corticosteroids", "Correct. The inhaled corticosteroids are beclomethasone, budesonide, flunisolide, fluticasone (Flovent), mometasone and triamcinolone."],
   ["Long-acting beta-2 agonists", "The long-acting beta-2 agonists are formoterol and salmeterol; fluticasone is an inhaled corticosteroid, paired with salmeterol in Advair.", MECH],
   ["Leukotriene modifiers", "The leukotriene modifier is montelukast, an oral leukotriene D4 receptor antagonist; fluticasone is an inhaled corticosteroid.", MECH],
   ["Mast cell stabilizers", "The mast cell stabilizers are cromolyn and nedocromil, taken before antigen exposure; fluticasone is an inhaled corticosteroid.", MECH]], 72),

Q("Inhaled corticosteroids", IO_CLASS, "class",
  "Pulmicort is the brand name of which inhaled corticosteroid?",
  [["Budesonide", "Correct. Budesonide is sold as Pulmicort, and with formoterol it makes up Symbicort."],
   ["Beclomethasone", "Beclomethasone is the inhaled corticosteroid sold as QVAR; Pulmicort is budesonide.", ADJ],
   ["Fluticasone", "Fluticasone is the inhaled corticosteroid sold as Flovent and, with salmeterol, as Advair; Pulmicort is budesonide.", ADJ],
   ["Flunisolide", "Flunisolide is the inhaled corticosteroid sold as Aerobid; Pulmicort is the brand of budesonide.", ADJ]], 72),

Q("Inhaled corticosteroids", IO_EDU, "education",
  "A patient starting a controller inhaler is told it can take up to 8 weeks to reach its maximal effect. Which drug group is this?",
  [["Inhaled corticosteroids", "Correct. Inhaled corticosteroids inhibit the inflammatory cascade and can take up to 8 weeks for maximal effects, which is why controllers are used daily rather than for quick relief."],
   ["Mast cell stabilizers", "Cromolyn and nedocromil may take up to 4 weeks to work and must be taken regularly; up to 8 weeks for maximal effect describes inhaled corticosteroids.", ADJ],
   ["Short-acting beta-2 agonists", "A short-acting beta-2 agonist is a quick-relief drug, not a controller: it works rapidly and lasts 4 to 6 hours. The 8-week controller is an inhaled corticosteroid.", RULED],
   ["Anticholinergics", "Short-acting anticholinergics are quick-relief drugs lasting up to 8 hours, not weeks; up to 8 weeks for maximal effect describes inhaled corticosteroids.", RULED]], 73),

Q("Inhaled corticosteroids", IO_AE, "adverse effect",
  "Which adverse effect of inhaled corticosteroids is an infection in the mouth?",
  [["Oral candidiasis", "Correct. Oral candidiasis (thrush) is an inhaled corticosteroid adverse effect, along with growth suppression in children at high dose and inhibition of the immune system."],
   ["Dry mouth", "Dry mouth ('dry as a bone') is part of anticholinergic toxicity and is not an infection; inhaled corticosteroids cause oral candidiasis (thrush).", ADJ],
   ["Heartburn", "Heartburn is listed for theophylline, which stimulates gastric acid; the inhaled corticosteroid mouth infection is oral candidiasis.", ADJ],
   ["Injection site pain", "Injection site pain follows anti-immunoglobulin E injections such as omalizumab; inhaled corticosteroids cause oral candidiasis (thrush).", ADJ]], 73),

Q("Inhaled corticosteroids", IO_AE, "adverse effect",
  "Which effect of high-dose inhaled corticosteroids is a particular concern in children?",
  [["Growth suppression", "Correct. High-dose inhaled corticosteroids can suppress growth in children; they can also cause oral candidiasis and inhibit the immune system."],
   ["Red-green color loss", "Decreased red-green discrimination is ethambutol's visual toxicity (its use is limited in children); high-dose inhaled corticosteroids suppress growth.", ADJ],
   ["Convulsions", "Convulsions are a danger of high theophylline levels, a central nervous system stimulant effect; high-dose inhaled corticosteroids suppress growth in children.", ADJ],
   ["Tachycardia", "Tachycardia is a beta-2 agonist and anticholinergic effect; the concern with high-dose inhaled corticosteroids in children is growth suppression.", ADJ]], 73),

Q("Inhaled corticosteroids", IO_MOA, "mechanism",
  "How do inhaled corticosteroids control asthma?",
  [["They inhibit the inflammatory cascade", "Correct. Inhaled corticosteroids inhibit the inflammatory cascade, which reduces bronchial responsiveness over the long term."],
   ["They block leukotriene D4 receptors", "Blocking the leukotriene D4 (cysteinyl leukotriene 1) receptor is montelukast's mechanism; inhaled corticosteroids inhibit the inflammatory cascade.", MECH],
   ["They bind circulating immunoglobulin E", "Binding circulating immunoglobulin E is omalizumab's mechanism; inhaled corticosteroids inhibit the inflammatory cascade.", MECH],
   ["They relax airway smooth muscle", "Relaxing airway smooth muscle through cyclic adenosine monophosphate is the beta-2 agonist action; inhaled corticosteroids inhibit the inflammatory cascade.", MECH]], 73),

# ---- combination inhalers (slide 74) ---------------------------------------------------------------
Q("Combination inhalers", IO_CLASS, "class",
  "Symbicort combines budesonide with which drug?",
  [["Formoterol", "Correct. Symbicort is formoterol with budesonide; Dulera is formoterol with mometasone, and Advair is salmeterol with fluticasone."],
   ["Salmeterol", "Salmeterol is the long-acting beta-2 agonist in Advair, paired with fluticasone; Symbicort pairs budesonide with formoterol.", ADJ],
   ["Albuterol", "Albuterol is a short-acting beta-2 agonist and is not in Symbicort, Dulera or Advair; Symbicort pairs budesonide with formoterol.", MECH],
   ["Montelukast", "Montelukast is an oral leukotriene receptor antagonist, not part of an inhaler; Symbicort pairs budesonide with formoterol.", MECH]], 74),

Q("Combination inhalers", IO_CLASS, "class",
  "Advair combines fluticasone with which long-acting beta-2 agonist?",
  [["Salmeterol", "Correct. Advair is salmeterol with fluticasone; the two formoterol combinations are Symbicort (with budesonide) and Dulera (with mometasone)."],
   ["Formoterol", "Formoterol is the long-acting beta-2 agonist in Symbicort and Dulera; Advair pairs fluticasone with salmeterol.", ADJ],
   ["Levalbuterol", "Levalbuterol (Xopenex) is a short-acting beta-2 agonist, not a long-acting one; Advair pairs fluticasone with salmeterol.", MECH],
   ["Tiotropium", "Tiotropium (Spiriva) is a long-acting anticholinergic, not a beta-2 agonist; Advair pairs fluticasone with salmeterol.", MECH]], 74),

Q("Combination inhalers", IO_CLASS, "class",
  "Symbicort, Dulera and Advair each pair which two drug classes?",
  [["A long-acting beta-2 agonist and an inhaled corticosteroid", "Correct. Each combines a long-acting beta-2 agonist (formoterol or salmeterol) with an inhaled corticosteroid (budesonide, mometasone or fluticasone)."],
   ["A short-acting beta-2 agonist and an anticholinergic", "A short-acting beta-2 agonist with a short-acting anticholinergic is an as-needed option for group A chronic obstructive pulmonary disease; these inhalers pair a long-acting beta-2 agonist with an inhaled corticosteroid.", ADJ],
   ["A long-acting beta-2 agonist and an anticholinergic", "A long-acting beta-2 agonist plus a long-acting anticholinergic is the combination for severe breathlessness in group D chronic obstructive pulmonary disease; these inhalers pair the beta-2 agonist with an inhaled corticosteroid.", ADJ],
   ["An inhaled corticosteroid and a leukotriene modifier", "An inhaled corticosteroid plus a leukotriene receptor antagonist is an alternative controller option, not one of these inhalers; Symbicort, Dulera and Advair pair an inhaled corticosteroid with a long-acting beta-2 agonist.", ADJ]], 74),

# ---- montelukast and the leukotriene pathway (slides 75-76) ----------------------------------------
Q("Montelukast", IO_CLASS, "class",
  "Montelukast (Singulair) belongs to which drug class?",
  [["Leukotriene antagonists", "Correct. Montelukast is an oral leukotriene antagonist: it blocks the leukotriene D4 (cysteinyl leukotriene 1) receptor, which mediates inflammation, bronchial constriction and mucus secretion."],
   ["Lipoxygenase inhibitors", "Lipoxygenase inhibitors act earlier, at the enzyme that makes leukotrienes from arachidonic acid; montelukast is a leukotriene antagonist that blocks the receptor instead.", MECH],
   ["Mast cell stabilizers", "Mast cell stabilizers are cromolyn and nedocromil, taken before antigen exposure; montelukast is a leukotriene antagonist.", MECH],
   ["Inhaled corticosteroids", "Inhaled corticosteroids such as fluticasone inhibit the inflammatory cascade; montelukast is an oral leukotriene antagonist.", MECH]], 75),

Q("Montelukast", IO_MOA, "mechanism",
  "Which receptor does montelukast block?",
  [["Cysteinyl leukotriene 1 receptor", "Correct. Montelukast is a leukotriene D4 antagonist at the cysteinyl leukotriene 1 receptor, which mediates inflammation, bronchial constriction and mucus secretion."],
   ["High-affinity immunoglobulin E receptor", "High-affinity immunoglobulin E receptors on mast cells decrease when omalizumab binds circulating immunoglobulin E; montelukast blocks the cysteinyl leukotriene 1 receptor.", MECH],
   ["Muscarinic receptor", "Muscarinic receptors are blocked by the anticholinergics ipratropium and tiotropium; montelukast blocks the cysteinyl leukotriene 1 receptor.", MECH],
   ["Adenosine A2B receptor", "The adenosine A2B receptor is antagonized by theophylline; montelukast blocks the cysteinyl leukotriene 1 receptor.", MECH]], 75),

Q("Montelukast", IO_IND, "indication",
  "In which form of asthma is montelukast described as effective?",
  [["Aspirin-induced asthma", "Correct. Montelukast, an oral leukotriene D4 antagonist, is effective in aspirin-induced asthma."],
   ["Status asthmaticus", "Status asthmaticus is a medical emergency treated with continuous nebulized albuterol, intravenous steroids, magnesium and ketamine if intubated; montelukast is described for aspirin-induced asthma.", STAGE],
   ["Eosinophilic phenotype asthma", "The eosinophilic phenotype is the target of the anti-interleukin-5 and anti-interleukin-4 biologics; montelukast is described as effective in aspirin-induced asthma.", ADJ],
   ["Anaphylactic bronchospasm", "Bronchospasm in anaphylaxis is treated with epinephrine and albuterol alongside fluids, histamine blockers and corticosteroids; montelukast is described for aspirin-induced asthma.", ADJ]], 75),

Q("Montelukast", IO_ADME, "class",
  "By which route is montelukast taken?",
  [["By mouth", "Correct. Montelukast is an oral leukotriene antagonist, so unlike the inhaled controllers it is taken by mouth."],
   ["By inhalation", "Inhalation is the route of the inhaled corticosteroids and of cromolyn and nedocromil; montelukast is an oral leukotriene antagonist.", ADJ],
   ["By subcutaneous injection", "Subcutaneous injection every 2 to 4 weeks is the route of omalizumab; montelukast is taken by mouth.", ADJ],
   ["By intravenous infusion", "Intravenous use is listed for reslizumab, an anti-interleukin-5 biologic; montelukast is taken by mouth.", ADJ]], 75),

Q("Montelukast", IO_MOA, "physiology",
  "Leukotrienes are made from arachidonic acid through which enzyme?",
  [["5-lipoxygenase", "Correct. Arachidonic acid is converted by 5-lipoxygenase to leukotriene A4 and on to leukotrienes B4, C4, D4 and E4; cyclooxygenase makes the prostaglandins and thromboxane."],
   ["Cyclooxygenase", "Cyclooxygenase converts arachidonic acid to the prostaglandins and thromboxane A2; the leukotriene branch runs through 5-lipoxygenase.", ADJ],
   ["Phosphodiesterase", "Phosphodiesterase is the enzyme theophylline inhibits to raise cyclic adenosine and guanosine monophosphate; leukotrienes come from arachidonic acid by 5-lipoxygenase.", MECH],
   ["Myosin light chain kinase", "Myosin light chain kinase phosphorylates the myosin light chain in airway smooth muscle; leukotrienes are made from arachidonic acid by 5-lipoxygenase.", MECH]], 76),

# ---- mast cell stabilizers (slides 77-78) ----------------------------------------------------------
Q("Mast cell stabilizers", IO_EDU, "education",
  "When must cromolyn be taken to prevent an asthma attack?",
  [["Before antigen exposure", "Correct. Mast cell stabilizers such as cromolyn must be taken before the antigen insult; they remove the trigger rather than reverse bronchospasm."],
   ["At the start of an attack", "Cromolyn does not reverse an attack in progress; it must be taken before the antigen insult, and a short-acting beta-2 agonist treats acute bronchospasm.", STAGE],
   ["After symptoms appear", "Waiting for symptoms is too late: cromolyn must be taken before the antigen insult, and it may take up to 4 weeks of regular use to work.", STAGE],
   ["During an exacerbation", "Exacerbations call for quick-relief drugs such as systemic corticosteroids; cromolyn must be taken before the antigen insult.", STAGE]], 77),

Q("Mast cell stabilizers", IO_EDU, "education",
  "What should a patient starting nedocromil expect?",
  [["Up to 4 weeks of regular use to work", "Correct. Cromolyn and nedocromil may take up to 4 weeks to work and must be taken regularly, before antigen exposure."],
   ["Relief of wheezing within minutes", "Rapid relief is the property of short-acting beta-2 agonists, which work rapidly and last 4 to 6 hours; nedocromil may take up to 4 weeks of regular use.", ADJ],
   ["Plasma level checks for toxicity", "Plasma level monitoring belongs to theophylline, which has a narrow therapeutic index; nedocromil may take up to 4 weeks of regular use to work.", ADJ],
   ["Orange discoloration of the urine", "Orange urine, tears and sweat are what to warn about with rifampin; nedocromil may take up to 4 weeks of regular use to work.", ADJ]], 78),

Q("Mast cell stabilizers", IO_MOA, "mechanism",
  "Cromolyn and nedocromil prevent asthma attacks by which action?",
  [["Stabilizing mast cells", "Correct. Cromolyn and nedocromil remove the trigger or antigen by stabilizing mast cells; their exact mechanism is unknown and may involve interference with calcium."],
   ["Blocking leukotriene receptors", "Blocking the leukotriene D4 receptor is montelukast's action; cromolyn and nedocromil stabilize mast cells.", MECH],
   ["Binding immunoglobulin E", "Binding circulating immunoglobulin E is omalizumab's action, which reduces the high-affinity receptors on mast cells; cromolyn and nedocromil stabilize mast cells.", MECH],
   ["Inhibiting phosphodiesterase", "Inhibiting phosphodiesterase is theophylline's action; cromolyn and nedocromil stabilize mast cells and must be taken before antigen exposure.", MECH]], 77),

# ---- omalizumab and the other biologics (slides 79-81) ---------------------------------------------
Q("Omalizumab and biologics", IO_ADME, "class",
  # Repair 2026-10-27: replaces "Which asthma biologic is given intravenously?" (slide 81 sets "Given IV" under the
  # whole anti-interleukin-5 list, so mepolizumab was defensible from the slide). The brand is unambiguous.
  "Which asthma biologic is sold as Cinqair?",
  [["Reslizumab", "Correct. Reslizumab (Cinqair) is one of the anti-interleukin-5 biologics, with mepolizumab and benralizumab, used for the eosinophilic phenotype."],
   ["Omalizumab", "Omalizumab is the anti-immunoglobulin E antibody sold as Xolair; Cinqair is reslizumab, one of the anti-interleukin-5 biologics.", ADJ],
   ["Mepolizumab", "Mepolizumab is the anti-interleukin-5 biologic sold as Nucala; Cinqair is reslizumab, another anti-interleukin-5 biologic.", ADJ],
   ["Dupilumab", "Dupilumab is the anti-interleukin-4 biologic sold as Dupixent; Cinqair is reslizumab, an anti-interleukin-5 biologic.", ADJ]], 81),

Q("Omalizumab and biologics", IO_MOA, "mechanism",
  "How does omalizumab prevent mast cell degranulation?",
  [["It binds circulating immunoglobulin E", "Correct. Omalizumab, a humanized monoclonal antibody, binds circulating immunoglobulin E, which decreases the high-affinity receptors on mast cells and prevents degranulation."],
   ["It stabilizes the mast cell membrane", "Mast cell stabilization is the action of cromolyn and nedocromil; omalizumab binds circulating immunoglobulin E.", MECH],
   ["It blocks interleukin-5", "Blocking interleukin-5 is the action of the anti-interleukin-5 biologics such as mepolizumab; omalizumab binds circulating immunoglobulin E.", MECH],
   ["It blocks leukotriene receptors", "Blocking the leukotriene D4 receptor is montelukast's action; omalizumab binds circulating immunoglobulin E and so prevents degranulation.", MECH]], 79),

Q("Omalizumab and biologics", IO_AE, "adverse effect",
  "Which acute, life-threatening reaction is listed among omalizumab's adverse effects?",
  [["Anaphylaxis", "Correct. Omalizumab's adverse effects include anaphylaxis (about 0.1 percent), gastrointestinal disturbances, neutralizing antibodies and secondary malignancies."],
   ["Status asthmaticus", "Status asthmaticus is an acute exacerbation unresponsive to initial bronchodilator treatment, not an omalizumab adverse effect; omalizumab lists anaphylaxis.", ADJ],
   ["Convulsions", "Convulsions are a danger of high theophylline levels; the acute life-threatening reaction listed for omalizumab is anaphylaxis.", ADJ],
   ["Hepatitis", "Hepatitis is listed for isoniazid, rifampin and pyrazinamide; omalizumab's acute life-threatening reaction is anaphylaxis.", ADJ]], 79),

Q("Omalizumab and biologics", IO_AE, "adverse effect",
  "Which long-term risk is listed among omalizumab's adverse effects?",
  [["Secondary malignancies", "Correct. Omalizumab's listed adverse effects are gastrointestinal disturbances, anaphylaxis, neutralizing antibodies and secondary malignancies."],
   ["Growth suppression", "Growth suppression is listed for high-dose inhaled corticosteroids and for systemic corticosteroids; omalizumab lists secondary malignancies.", ADJ],
   ["Adrenal suppression", "Adrenal suppression is a systemic corticosteroid side effect; the long-term risk on omalizumab's list is secondary malignancies.", ADJ],
   ["Peripheral neuritis", "Peripheral neuritis from pyridoxine deficiency is an isoniazid adverse effect; omalizumab lists secondary malignancies.", ADJ]], 79),

Q("Omalizumab and biologics", IO_AE, "adverse effect",
  "Besides urticaria and anaphylaxis, which local effects are listed for anti-immunoglobulin E therapy?",
  [["Injection site pain, bruising", "Correct. Anti-immunoglobulin E side effects are urticaria (0.1 percent), anaphylaxis (0.1 percent), injection site pain and bruising."],
   ["Oral thrush and dry mouth", "Oral thrush follows inhaled corticosteroids and dry mouth follows anticholinergics; anti-immunoglobulin E injections cause injection site pain and bruising.", ADJ],
   ["Tremor and tachycardia", "Tremor and tachycardia are beta-2 agonist adverse effects; anti-immunoglobulin E injections cause injection site pain and bruising.", ADJ],
   ["Orange tears and sweat", "Orange tears and sweat come from rifampin; the local effects of anti-immunoglobulin E injections are injection site pain and bruising.", ADJ]], 80),

Q("Omalizumab and biologics", IO_IND, "indication",
  "Mepolizumab and reslizumab are used for which asthma phenotype?",
  [["Eosinophilic", "Correct. The other asthma biologics (anti-interleukin-5 and anti-interleukin-4) are used for the eosinophilic phenotype, with peripheral blood eosinophils above 150 per microliter."],
   ["Aspirin-induced", "Montelukast is described as effective in aspirin-induced asthma; the anti-interleukin-5 biologics are for the eosinophilic phenotype.", ADJ],
   ["Exercise-induced", "Exercise is one of the nonspecific provokers of bronchospasm, with cold air and distilled water; the anti-interleukin-5 biologics target the eosinophilic phenotype.", ADJ],
   ["Viral-triggered", "Viral respiratory infection triggers most asthma attacks, but the anti-interleukin-5 biologics are used for the eosinophilic phenotype.", ADJ]], 81),

Q("Omalizumab and biologics", IO_CLASS, "class",
  "Dupilumab (Dupixent) and mepolizumab (Nucala), the biologics for eosinophilic asthma, block which kind of target?",
  [["Interleukins", "Correct. They are anti-interleukin biologics (anti-interleukin-4 and anti-interleukin-5) for the eosinophilic phenotype; omalizumab, by contrast, binds immunoglobulin E."],
   ["Immunoglobulin E", "Circulating immunoglobulin E is bound by omalizumab, which reduces the high-affinity receptors on mast cells; dupilumab and mepolizumab target interleukins.", ADJ],
   ["Leukotriene D4 receptors", "The leukotriene D4 receptor is blocked by montelukast, an oral leukotriene antagonist; dupilumab and mepolizumab are anti-interleukin antibodies.", MECH],
   ["Phosphodiesterase", "Phosphodiesterase is inhibited by theophylline, a methylxanthine; dupilumab and mepolizumab are injected antibodies against interleukins.", MECH]], 81),

Q("Omalizumab and biologics", IO_AE, "adverse effect",
  "The anti-interleukin-5 and anti-interleukin-4 biologics have a side effect profile similar to which drug?",
  [["Omalizumab", "Correct. The other asthma biologics have a side effect profile similar to omalizumab (Xolair), whose list includes gastrointestinal disturbances, anaphylaxis, injection site pain and bruising."],
   ["Montelukast", "Montelukast is an oral leukotriene antagonist, not a biologic; the anti-interleukin biologics share omalizumab's side effect profile.", MECH],
   ["Prednisone", "Prednisone is an oral systemic corticosteroid with adrenal and growth suppression among its side effects; the biologics resemble omalizumab.", ADJ],
   ["Fluticasone", "Fluticasone is an inhaled corticosteroid whose adverse effects include thrush; the anti-interleukin biologics share omalizumab's side effect profile.", ADJ]], 81),

# ---- oral systemic corticosteroids (slides 88-89) --------------------------------------------------
Q("Systemic corticosteroids", IO_IND, "indication",
  "Why are oral systemic corticosteroids reserved mainly for asthma exacerbations?",
  [["Their side effects limit their use", "Correct. Oral systemic corticosteroids are the most potent option for suppressing airway inflammation, but their side effects limit their use, so they are used in asthma exacerbations."],
   ["They are the least potent option", "The reverse is true: oral systemic corticosteroids are the most potent option, and it is their side effects that limit their use.", REV],
   ["They take up to 8 weeks to work", "Up to 8 weeks for maximal effect describes inhaled corticosteroids; oral systemic corticosteroids are limited by their side effects.", ADJ],
   ["They must be taken before exposure", "Taking a drug before antigen exposure is the rule for cromolyn and nedocromil; oral systemic corticosteroids are limited by their side effects.", ADJ]], 88),

Q("Systemic corticosteroids", IO_IND, "drug choice",
  "Among the oral systemic corticosteroids for asthma, which one is listed as an oral liquid rather than a tablet?",
  [["Prednisolone", "Correct. Prednisolone (Ora-Pred) is listed as the oral liquid; prednisone (Deltasone) is the oral tablet, and methylprednisolone and dexamethasone are oral or parenteral."],
   ["Prednisone", "Prednisone (Deltasone) is listed as an oral tablet; the oral liquid on the list is prednisolone (Ora-Pred).", ADJ],
   ["Methylprednisolone", "Methylprednisolone (Solu-Medrol) is listed for oral or parenteral use, not as the oral liquid; prednisolone (Ora-Pred) is the liquid.", ADJ],
   ["Fluticasone", "Fluticasone is an inhaled corticosteroid for long-term control, not an oral systemic corticosteroid; prednisolone is the oral liquid.", MECH]], 88),

Q("Systemic corticosteroids", IO_AE, "adverse effect",
  "Which metabolic side effect is shared by systemic corticosteroids and beta-2 agonists?",
  [["Hyperglycemia", "Correct. Hyperglycemia is on both lists: the systemic corticosteroid side effects and the beta-2 agonist adverse effects."],
   ["Hypertension", "Hypertension is a systemic corticosteroid side effect, but the beta-2 agonist list gives hypotension instead; the shared effect is hyperglycemia.", ADJ],
   ["Hyperuricemia", "Raised uric acid is listed for ethambutol and pyrazinamide, not for corticosteroids or beta-2 agonists; both of those list hyperglycemia.", ADJ],
   ["Hypoglycemia", "The direction is reversed: systemic corticosteroids and beta-2 agonists both raise blood sugar, which is listed as hyperglycemia.", REV]], (89, 71)),   # 71: the beta-2 agonist adverse effects

Q("Systemic corticosteroids", IO_AE, "adverse effect",
  "Which systemic corticosteroid side effect is the reason a longer course is tapered rather than stopped abruptly?",
  [["Adrenal suppression", "Correct. Systemic corticosteroids cause adrenal suppression, so the general rule is to taper a longer course rather than stop it suddenly."],
   ["Growth suppression", "Growth suppression is a separate listed side effect (also seen with high-dose inhaled corticosteroids); the taper rule is tied to adrenal suppression.", ADJ],
   ["Steroid myopathy", "Muscle weakness (steroid myopathy) is a listed side effect, but tapering a longer course is the rule tied to adrenal suppression.", ADJ],
   ["Hyperglycemia", "Hyperglycemia is a listed side effect of systemic corticosteroids and of beta-2 agonists; the taper rule is tied to adrenal suppression.", ADJ]], 89),

# Recording pass: Dr. Wood affirmed the slide 89 rule aloud (1:22:13): "Remember, if they're on it for more than five
# days, you have to taper ... If it's just a five-day course, no problem." Asked once, as the slide says; the guide notes
# that many references taper only after longer courses.
Q("Systemic corticosteroids", IO_PROT, "protocol",
  "A patient admitted for an asthma exacerbation has taken a systemic corticosteroid for 8 days. What does the general rule say about stopping it?",
  [["Taper the dose rather than stop abruptly", "Correct. The general rule is to taper when the course lasts more than 5 days, because systemic corticosteroids cause adrenal suppression; a 5-day course can simply stop."],
   ["Stop it at once; no taper is needed", "Stopping at once fits a course of 5 days or less; beyond 5 days the general rule is to taper because of adrenal suppression.", RULED],
   ["Switch to theophylline before stopping", "Theophylline is not a replacement for a systemic corticosteroid course; the rule for a course longer than 5 days is to taper.", ADJ],
   ["Continue it indefinitely as a controller", "Systemic corticosteroids are for exacerbations, limited by their side effects; daily control belongs to inhaled corticosteroids.", MECH]], 89),

Q("Systemic corticosteroids", IO_AE, "adverse effect",
  "Which side effect is listed both for high-dose inhaled corticosteroids in children and for systemic corticosteroids?",
  [["Growth suppression", "Correct. Growth suppression appears on both lists: high-dose inhaled corticosteroids can suppress growth in children, and it is a systemic corticosteroid side effect."],
   ["Oral candidiasis", "Oral candidiasis (thrush) is listed for inhaled corticosteroids, not among the systemic corticosteroid side effects; growth suppression is on both lists.", ADJ],
   ["Hypertension", "Hypertension is a systemic corticosteroid side effect that is not on the inhaled corticosteroid list; growth suppression appears on both.", ADJ],
   ["Steroid myopathy", "Muscle weakness (steroid myopathy) is listed for systemic corticosteroids but not for inhaled corticosteroids; growth suppression appears on both lists.", ADJ]], (89, 73)),   # 73: the inhaled corticosteroid adverse effects

Q("Systemic corticosteroids", IO_AE, "adverse effect",
  "A patient who has needed several courses of oral corticosteroids now has trouble climbing stairs because of leg weakness. Which listed side effect fits?",
  [["Steroid myopathy", "Correct. Muscle weakness (steroid myopathy) is a listed systemic corticosteroid side effect, alongside adrenal suppression, growth suppression, dermal thinning, hypertension, hyperglycemia, mood change and immunosuppression."],
   ["Adrenal suppression", "Adrenal suppression is the side effect addressed by tapering a longer course; leg weakness on oral corticosteroids is steroid myopathy.", ADJ],
   ["Peripheral neuritis", "Peripheral neuritis from pyridoxine deficiency is isoniazid's toxicity; muscle weakness on oral corticosteroids is steroid myopathy.", ADJ],
   ["Immunosuppression", "Immunosuppression is a listed systemic corticosteroid side effect, but it does not explain leg weakness; this patient has steroid myopathy.", ADJ]], 89),
]
