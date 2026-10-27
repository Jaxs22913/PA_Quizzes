# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Drugs for Pulmonary Infections, Asthma and COPD (Lecture 11), topic: anaphylaxis treatment.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. The key is authored FIRST (c == 0);
pharm_e3_partition.py rotates it (numeric option sets are sorted ascending instead, WRITER.md rule 8).

SOURCE. Pulmonology-2.pptx slides 47-55: anaphylaxis defined (48), allergen exposure routes (49, a picture: skin contact,
injection, ingestion, inhalation; not asked), volume expansion (50), epinephrine (51-52; slide 52's picture is an
auto-injector box), histamine blockers (53), albuterol (54), corticosteroids (55).

WRITER.md v1 (2026-10-15): every distractor carries its misconception as a third element (mis); slides only (this deck
has no speaker notes); slides win on conflict. Shared keying decisions: scratchpad L11_KEYING.md.

LEFT OUT ON PURPOSE:
  * every amount: the crystalloid volumes per kilogram and in liters (slide 50), the epinephrine concentrations and
    milligram strengths (1:1,000 against 1:10,000; slide 52) and the auto-injector strength on slide 52's picture;
  * "Alleviates pruritus, urticaria, and angioedema" (slide 51) as a drug-identification key: histamine H1 blockers
    relieve rash, pruritus and hives too (slide 53), so two answers would fit;
  * which drug is "the beta-2 agonist" with epinephrine among the options (epinephrine also acts on beta receptors);
  * the allergen-route picture (slide 49) and the "massive histamine release" line as stand-alone keys.
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

# ---- anaphylaxis (slide 48) ---------------------------------------------------------------------------
Q("Anaphylaxis", IO_PROT, "physiology",
  "Which description defines anaphylaxis?",
  [["A severe, systemic allergic reaction", "Correct. Anaphylaxis is a severe, systemic allergic reaction with multisystem involvement: skin, airway, vascular system and gastrointestinal tract."],
   ["Widespread reversible airway narrowing", "Widespread reversible narrowing of the bronchial airways defines asthma; anaphylaxis is a severe, systemic allergic reaction.", COMP],
   ["Inflammation of one or more bronchi", "Inflammation of one or more bronchi defines bronchitis; anaphylaxis is a severe, systemic allergic reaction involving many systems.", COMP],
   ["An allergic reaction of the skin alone", "Anaphylaxis is multisystem, involving the skin, airway, vascular system and gastrointestinal tract, and can end in airway obstruction and cardiovascular collapse.", STAGE]], 48),

Q("Anaphylaxis", IO_TOX, "physiology",
  "How can a severe case of anaphylaxis end?",
  [["In airway obstruction and circulatory collapse", "Correct. Severe anaphylaxis may result in complete obstruction of the airway, cardiovascular collapse and death."],
   ["In a slow, lasting decline in lung function", "An accelerated decline in forced expiratory volume in 1 second (FEV1) describes chronic obstructive pulmonary disease; severe anaphylaxis ends in airway obstruction and cardiovascular collapse.", COMP],
   ["In an empyema or a lung abscess", "Empyema and lung abscess are complications of pneumonia therapy failing; severe anaphylaxis can end in complete airway obstruction and cardiovascular collapse.", COMP],
   ["In a thickening of the bronchial mucosa", "Thickening of the bronchial mucosa is a feature of asthma; severe anaphylaxis can end in complete airway obstruction, cardiovascular collapse and death.", COMP]], 48),

# ---- volume expansion (slide 50) ----------------------------------------------------------------------
Q("Volume expansion", IO_IND, "indication",
  "Which finding in anaphylaxis is the indication for intravenous crystalloid?",
  [["Profound vasodilation with hypotension", "Correct. Intravenous crystalloid (normal saline) is given for profound vasodilation and hypotension, because it increases intravascular volume."],
   ["Widespread hives with itching", "Rash, itching and hives are the cutaneous effects relieved by histamine H1 blockers; crystalloid is for profound vasodilation and hypotension.", ADJ],
   ["Wheezing from bronchospasm", "Bronchospasm is treated with a bronchodilator such as albuterol, which relaxes bronchial smooth muscle; crystalloid is for vasodilation and hypotension.", ADJ],
   ["Increased gastric acid secretion", "Increased gastric acid is a gastrointestinal effect of histamine blocked by famotidine; crystalloid is given for profound vasodilation and hypotension.", ADJ]], 50),

# ---- epinephrine (slides 51 and 52) ---------------------------------------------------------------------
Q("Epinephrine", IO_CLASS, "class",
  "Which kind of agent is epinephrine?",
  [["An endogenous catecholamine", "Correct. Epinephrine (adrenalin) is an endogenous catecholamine that acts on alpha and beta receptors."],
   ["A synthetic beta-2 agonist", "Albuterol is the beta-2 agonist bronchodilator; epinephrine is the body's own catecholamine, acting on both alpha and beta receptors.", MECH],
   ["A systemic corticosteroid", "Methylprednisolone and prednisone are the corticosteroids, which block inflammatory mediator production; epinephrine is an endogenous catecholamine.", MECH],
   ["A histamine H1 blocker", "Diphenhydramine and hydroxyzine are the histamine H1 blockers for cutaneous effects; epinephrine is an endogenous catecholamine.", MECH]], 51),

Q("Epinephrine", IO_MOA, "mechanism",
  "Epinephrine treats anaphylaxis by acting on which receptors?",
  [["Alpha and beta receptors", "Correct. Epinephrine acts on alpha receptors (vasoconstriction, decreased vascular permeability) and beta receptors (bronchial smooth muscle relaxation)."],
   ["Beta-2 receptors", "Albuterol is the beta-2 agonist; epinephrine also acts on alpha receptors, which is where its vasoconstriction comes from.", STAGE],
   ["Histamine H1 receptors", "Histamine H1 receptors are blocked by diphenhydramine and hydroxyzine for rash and hives; epinephrine acts on alpha and beta receptors.", MECH],
   ["Histamine H2 receptors", "Histamine H2 receptors are blocked by famotidine for systemic and gastrointestinal effects; epinephrine acts on alpha and beta receptors.", MECH]], 51),

Q("Epinephrine", IO_MOA, "mechanism",
  "Which effect of epinephrine comes from its alpha receptor activity?",
  [["Vasoconstriction", "Correct. Epinephrine's alpha effects are vasoconstriction and decreased vascular permeability; its beta effect is bronchial smooth muscle relaxation."],
   ["Bronchodilation", "Bronchial smooth muscle relaxation is epinephrine's beta effect; vasoconstriction and decreased vascular permeability are its alpha effects.", MECH],
   ["Less gastric acid", "Blocking the gastrointestinal effects of histamine, such as increased gastric acid, is the role of the histamine H2 blocker famotidine; the alpha effect is vasoconstriction.", MECH],
   ["Less inflammation", "Blocking inflammatory mediator production is how corticosteroids act, over several hours; epinephrine's alpha effect is vasoconstriction.", MECH]], 51),

Q("Epinephrine", IO_IND, "indication",
  "Besides constricting vessels and relaxing bronchial muscle, which signs of anaphylaxis does epinephrine alleviate?",
  [["Pruritus, urticaria and angioedema", "Correct. Beyond its alpha and beta effects, epinephrine alleviates pruritus, urticaria and angioedema."],
   ["Tremor, anxiousness and tachycardia", "Anxiousness, tremor and tachycardia are albuterol's adverse effects, and anxiety and tachycardia are epinephrine's own; it alleviates pruritus, urticaria and angioedema.", REV],
   ["Hypertension and diaphoresis", "Hypertension and diaphoresis are adverse effects of epinephrine, not signs it relieves; it alleviates pruritus, urticaria and angioedema.", REV],
   ["Excess gastric acid secretion", "Increased gastric acid secretion is a gastrointestinal effect of histamine blocked by famotidine; epinephrine alleviates pruritus, urticaria and angioedema.", ADJ]], 51),

Q("Epinephrine", IO_PROT, "protocol",
  "By which route is epinephrine generally preferred in anaphylaxis when the patient is not coding?",
  [["Intramuscular", "Correct. Epinephrine can be given intramuscularly, subcutaneously or intravenously, and the intramuscular route is generally preferred unless the patient is coding."],
   ["Intravenous", "Intravenous epinephrine is the exception, kept for a patient who is coding; otherwise the intramuscular route is generally preferred.", STAGE],
   ["Subcutaneous", "Subcutaneous injection is one of the listed routes, but the intramuscular route is the one generally preferred.", ADJ],
   ["Inhaled", "Inhalation is the route for albuterol; epinephrine is given intramuscularly, subcutaneously or intravenously, with intramuscular preferred.", ADJ]], 52),

Q("Epinephrine", IO_AE, "adverse effect",
  "Which anaphylaxis drug lists hypertension and diaphoresis among its adverse effects?",
  [["Epinephrine", "Correct. Epinephrine's adverse effects are anxiety, hypertension, tachycardia, nausea and vomiting, and diaphoresis."],
   ["Albuterol", "Albuterol's listed adverse effects are anxiousness, tremor and tachycardia; hypertension and diaphoresis are on epinephrine's list.", ADJ],
   ["Diphenhydramine", "Diphenhydramine is the histamine H1 blocker given for rash, pruritus and hives; hypertension and diaphoresis are epinephrine's adverse effects.", ADJ],
   ["Methylprednisolone", "Methylprednisolone is the corticosteroid that blocks inflammatory mediators over hours; hypertension and diaphoresis are epinephrine's adverse effects.", ADJ]], 52),

Q("Epinephrine", IO_TOX, "adverse effect",
  "Which complication can an epinephrine overdose cause?",
  [["Cerebrovascular hemorrhage", "Correct. Epinephrine overdose can lead to cerebrovascular hemorrhage, myocardial infarction and pulmonary edema."],
   ["Adrenal suppression", "Adrenal suppression is a systemic corticosteroid side effect; epinephrine overdose can cause cerebrovascular hemorrhage.", ADJ],
   ["Peripheral neuritis", "Peripheral neuritis is isoniazid's effect from pyridoxine deficiency; epinephrine overdose can cause cerebrovascular hemorrhage.", ADJ],
   ["Oral candidiasis", "Oral candidiasis (thrush) is an inhaled corticosteroid adverse effect; epinephrine overdose can cause cerebrovascular hemorrhage.", ADJ]], 52),

# ---- histamine blockers (slide 53) ---------------------------------------------------------------------
Q("Histamine blockers", IO_CLASS, "class",
  "Which drug used in anaphylaxis is a histamine H1 blocker?",
  [["Diphenhydramine", "Correct. Diphenhydramine and hydroxyzine are the histamine H1 blockers; they relieve rash, pruritus and hives."],
   ["Famotidine", "Famotidine is the histamine H2 blocker, which blocks systemic vasodilation and gastrointestinal effects; diphenhydramine is the H1 blocker.", MECH],
   ["Albuterol", "Albuterol is a beta-2 agonist that relaxes bronchial smooth muscle; diphenhydramine is the histamine H1 blocker.", MECH],
   ["Prednisone", "Prednisone is a corticosteroid that blocks inflammatory mediator production; diphenhydramine is the histamine H1 blocker.", MECH]], 53),

Q("Histamine blockers", IO_IND, "indication",
  "In anaphylaxis, which effects do histamine H1 blockers relieve?",
  [["Rash, pruritus and hives", "Correct. The histamine H1 blockers diphenhydramine and hydroxyzine relieve the cutaneous effects: rash, pruritus and hives."],
   ["Vasodilation and gastric acid", "Systemic vasodilation and gastrointestinal effects such as increased gastric acid are blocked by the histamine H2 blocker famotidine.", MECH],
   ["Bronchospasm and wheeze", "Bronchospasm is relieved by relaxing bronchial smooth muscle with albuterol or epinephrine; histamine H1 blockers relieve rash, pruritus and hives.", ADJ],
   ["Hypotension and shock", "Profound vasodilation and hypotension call for intravenous crystalloid and epinephrine; histamine H1 blockers relieve the cutaneous effects.", ADJ]], 53),

Q("Histamine blockers", IO_IND, "drug choice",
  "Which drug is given in anaphylaxis to block the systemic vasodilation and gastrointestinal effects of histamine?",
  [["Famotidine", "Correct. Famotidine, the histamine H2 blocker, blocks the systemic (vasodilation) and gastrointestinal (increased gastric acid secretion) effects of histamine."],
   ["Diphenhydramine", "Diphenhydramine is a histamine H1 blocker, used for the cutaneous effects (rash, pruritus, hives); famotidine blocks the systemic and gastrointestinal effects.", MECH],
   ["Hydroxyzine", "Hydroxyzine is a histamine H1 blocker for the cutaneous effects; the histamine H2 blocker famotidine blocks vasodilation and gastrointestinal effects.", MECH],
   ["Albuterol", "Albuterol is a beta-2 agonist that relaxes bronchial smooth muscle; the systemic and gastrointestinal effects of histamine are blocked by famotidine.", ADJ]], 53),

# ---- albuterol (slide 54) ---------------------------------------------------------------------------
Q("Albuterol", IO_IND, "drug choice",
  "A patient in anaphylaxis is still wheezing after epinephrine. Which added drug relaxes bronchial smooth muscle?",
  [["Albuterol", "Correct. Albuterol, a beta-2 agonist bronchodilator, relaxes bronchial smooth muscle."],
   ["Famotidine", "Famotidine is the histamine H2 blocker for systemic vasodilation and gastrointestinal effects; albuterol relaxes bronchial smooth muscle.", ADJ],
   ["Hydroxyzine", "Hydroxyzine is a histamine H1 blocker that relieves rash, pruritus and hives; albuterol relaxes bronchial smooth muscle.", ADJ],
   ["Prednisone", "Prednisone blocks inflammatory mediator production but takes several hours to work; albuterol relaxes bronchial smooth muscle now.", STAGE]], 54),

Q("Albuterol", IO_AE, "adverse effect",
  "Which adverse effect is listed for albuterol given in anaphylaxis?",
  [["Tremor", "Correct. Albuterol's listed adverse effects are anxiousness, tremor and tachycardia."],
   ["Bradycardia", "The heart rate goes the other way: albuterol causes tachycardia, along with anxiousness and tremor.", REV],
   ["Diaphoresis", "Diaphoresis is on epinephrine's adverse-effect list; albuterol's listed effects are anxiousness, tremor and tachycardia.", ADJ],
   ["Oral thrush", "Oral candidiasis (thrush) is an inhaled corticosteroid adverse effect; albuterol causes anxiousness, tremor and tachycardia.", ADJ]], 54),

# ---- corticosteroids (slide 55) -----------------------------------------------------------------------
Q("Corticosteroids", IO_MOA, "mechanism",
  "How do corticosteroids act in anaphylaxis?",
  [["They block inflammatory mediator production", "Correct. Corticosteroids block production of inflammatory mediators at the cellular level and work on all aspects of anaphylaxis, though they take several hours."],
   ["They block histamine at its receptors", "Blocking histamine at its receptors is the job of the histamine H1 and H2 blockers; corticosteroids block inflammatory mediator production.", MECH],
   ["They stimulate alpha and beta receptors", "Stimulating alpha and beta receptors is epinephrine's action; corticosteroids block inflammatory mediator production at the cellular level.", MECH],
   ["They expand the intravascular volume", "Increasing intravascular volume is the role of intravenous crystalloid; corticosteroids block inflammatory mediator production.", MECH]], 55),

Q("Corticosteroids", IO_PROT, "protocol",
  "Why are corticosteroids not relied on for the immediate reversal of anaphylaxis?",
  [["They take several hours to work", "Correct. Corticosteroids work on all aspects of anaphylaxis but take several hours to work."],
   ["They act on the skin signs alone", "Corticosteroids work on all aspects of anaphylaxis, not the skin alone; the limit is that they take several hours to work.", REV],
   ["They cannot be given by injection", "Methylprednisolone can be given intramuscularly or intravenously; the limit of corticosteroids is that they take several hours to work.", RULED],
   ["They worsen the hypotension", "Hypotension from profound vasodilation is treated with crystalloid; the limit of corticosteroids is their delay of several hours.", ADJ]], 55),

Q("Corticosteroids", IO_IND, "drug choice",
  "Which corticosteroid listed for anaphylaxis can be given intramuscularly or intravenously?",
  [["Methylprednisolone", "Correct. Methylprednisolone is the corticosteroid listed for intramuscular or intravenous use in anaphylaxis; prednisone is the other agent."],
   ["Prednisone", "Prednisone is the other listed corticosteroid, without an injectable route given; methylprednisolone is the one given intramuscularly or intravenously.", ADJ],
   ["Hydroxyzine", "Hydroxyzine is a histamine H1 blocker for rash and hives, not a corticosteroid; methylprednisolone is the injectable corticosteroid.", MECH],
   ["Famotidine", "Famotidine is the histamine H2 blocker, not a corticosteroid; methylprednisolone is the corticosteroid given intramuscularly or intravenously.", MECH]], 55),
]
