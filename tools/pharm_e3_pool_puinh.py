# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Pulmonary Infections, Asthma and COPD/COLD (Lecture 11), topic: asthma steps, inhaler devices
and technique, and status asthmaticus.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. The key is authored FIRST (c == 0);
pharm_e3_partition.py rotates it (numeric option sets are sorted ascending instead, WRITER.md rule 8).

SOURCE. Pulmonology-2.pptx slides 90-99: the stepwise asthma therapy picture (90; its text was read by eye into
tools/pharm_e3/ocr.json under "L11": preferred controller per step, other controller options, preferred and other
reliever, step 5 phenotypic assessment and add-ons, the assess / adjust / review response cycle), respiratory
administration (91, pictures), nebulizer (92), dry powder inhalers (93), metered dose inhalers (94, with the parts
picture), spacers and valve holding chambers (95), inhaler technique (96-97, with the three hand-held pictures), the
summary (98) and status asthmaticus (99). Explanations also draw on neighbouring asthma slides where a distractor
needs its replacing fact (slide 62 bronchospasm triggers and methacholine, 65 severity classification, 70 long-acting
beta-2 agonists not alone, 75 montelukast, 77 cromolyn, 83 theophylline, 86 anticholinergics).

WRITER.md v1 (2026-10-15): every distractor carries its misconception as a third element (mis); slides only (this deck
has no speaker notes); slides win on conflict (tools/../scratchpad L11_KEYING.md decisions).

LEFT OUT ON PURPOSE:
  * every dose: continuous albuterol milligrams per hour, the magnesium bolus and infusion amounts, ketamine, and the
    "low/medium/high-dose" tiers asked only as the step labels printed on the stepwise picture (never as amounts);
  * "Aminophylline?" on the status asthmaticus algorithm (printed with a question mark: not a stated recommendation);
  * tiotropium as "COPD only" (slide 86) against the step 4-5 add-on tiotropium on the stepwise picture: never keyed;
  * the three hand-held technique drawings (slide 96) as an image item: the slide does not label which hold is which;
  * "should be cleaned regularly" as a discriminator: the slides give it to all three devices;
  * nebulizer "good for children, elderly who can't use MDI" as a device-choice key: a spacer or valve holding chamber
    is a second defensible answer for poor coordination;
  * the five-second holding-chamber window and the 10-second breath hold appear as education timings, not doses.
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

# ---- stepwise asthma therapy (slide 90, picture) -----------------------------------------------------
# Recording pass: Dr. Wood, 1:25:14 -- either as-needed low-dose inhaled corticosteroid-formoterol or an as-needed
# short-acting beta-2 agonist "would be a perfectly fine answer" for quick relief, so no item sets one against the other;
# 1:27:49-1:29:08 -- he asks the steps as "what to start with" and "what would you want to move up to next", not by
# step number ("I will not make you memorize the doses").
Q("Stepwise asthma therapy", IO_PROT, "drug choice",
  "Which of these is listed as a reliever, rather than a controller, in stepwise asthma therapy?",
  [["As-needed low-dose inhaled corticosteroid-formoterol", "Correct. As-needed low-dose inhaled corticosteroid-formoterol is the preferred reliever at every step; an as-needed short-acting beta-2 agonist is the other reliever option."],
   ["Daily low-dose inhaled corticosteroid on its own", "Daily low-dose inhaled corticosteroid is a step 2 preferred controller, taken every day, not a reliever; the listed relievers are as-needed.", MECH],
   ["Daily leukotriene receptor antagonist by mouth", "A leukotriene receptor antagonist appears among the other controller options, not as a reliever; the preferred reliever is as-needed low-dose inhaled corticosteroid-formoterol.", MECH],
   ["Daily low-dose oral corticosteroid tablet", "Low-dose oral corticosteroid is a step 5 add-on with a warning to consider side effects, not a reliever; the relievers are taken as needed.", STAGE]], 90),

Q("Stepwise asthma therapy", IO_PROT, "drug choice",
  "A patient's asthma is not controlled on a daily low-dose inhaled corticosteroid. Which preferred controller is the next step up?",
  [["Low-dose inhaled corticosteroid-long-acting beta-2 agonist", "Correct. From daily low-dose inhaled corticosteroid (step 2) the next preferred controller is the low-dose combination with a long-acting beta-2 agonist (step 3)."],
   ["Medium-dose inhaled corticosteroid-long-acting beta-2 agonist", "Medium-dose inhaled corticosteroid with a long-acting beta-2 agonist is the step after the low-dose combination (step 4), so it skips a step here.", STAGE],
   ["As-needed low-dose inhaled corticosteroid-formoterol", "As-needed low-dose inhaled corticosteroid-formoterol by itself is the step 1 controller, a step down; poor control on daily low-dose steroid calls for adding a long-acting beta-2 agonist.", REV],
   ["Long-acting beta-2 agonist on its own, no steroid", "A long-acting beta-2 agonist is never used alone for asthma; the next step adds it to the low-dose inhaled corticosteroid.", RULED]], 90),

Q("Stepwise asthma therapy", IO_PROT, "drug choice",
  "A patient on low-dose inhaled corticosteroid-long-acting beta-2 agonist still has poorly controlled asthma. Which preferred controller comes next?",
  [["Medium-dose inhaled corticosteroid-long-acting beta-2 agonist", "Correct. The step after the low-dose combination (step 3) is the medium-dose combination (step 4); biologics come only after high-dose therapy and referral."],
   ["High-dose inhaled corticosteroid-long-acting beta-2 agonist with omalizumab", "High-dose therapy with a biologic such as omalizumab comes after the medium-dose combination and after referral for phenotypic assessment; it skips the next step.", STAGE],
   ["Daily low-dose inhaled corticosteroid on its own", "Dropping the long-acting beta-2 agonist steps therapy down to step 2; poor control calls for stepping up to the medium-dose combination.", REV],
   ["As-needed short-acting beta-2 agonist on its own", "An as-needed short-acting beta-2 agonist is a reliever, not a controller; poor control calls for stepping up to the medium-dose combination.", MECH]], 90),

Q("Stepwise asthma therapy", IO_PROT, "protocol",
  "A patient remains uncontrolled on high-dose inhaled corticosteroid-long-acting beta-2 agonist. What does stepwise asthma therapy list next?",
  [["Referral for phenotypic assessment", "Correct. At the top step the patient is referred for phenotypic assessment, with possible add-on therapy such as tiotropium or a biologic (anti-immunoglobulin E, anti-interleukin-5, anti-interleukin-4 receptor)."],
   ["Switching to theophylline tablets", "Theophylline is not on the stepwise chart; it is less effective and less well tolerated than the long-acting bronchodilators, with a narrow therapeutic index.", ADJ],
   ["Stopping the long-acting agent", "Stopping the long-acting beta-2 agonist steps therapy down, the reverse of what uncontrolled asthma on high-dose therapy needs.", REV],
   ["Switching to a mast cell stabilizer", "Mast cell stabilizers have limited use and are not on the stepwise chart; the next move is referral for phenotypic assessment and add-on therapy.", ADJ]], 90),

Q("Stepwise asthma therapy", IO_PROT, "drug choice",
  "Which controller appears only among the other controller options, never as a preferred controller, in stepwise asthma therapy?",
  [["A leukotriene receptor antagonist", "Correct. A leukotriene receptor antagonist (such as montelukast) is listed only among the other controller options, at steps 2 to 4."],
   ["Low-dose inhaled corticosteroid-long-acting beta-2 agonist", "Low-dose inhaled corticosteroid with a long-acting beta-2 agonist is the preferred controller at step 3.", ADJ],
   ["Medium-dose inhaled corticosteroid-long-acting beta-2 agonist", "Medium-dose inhaled corticosteroid with a long-acting beta-2 agonist is the preferred controller at step 4.", ADJ],
   ["As-needed low-dose inhaled corticosteroid-formoterol", "As-needed low-dose inhaled corticosteroid-formoterol is the preferred controller at step 1 and the preferred reliever at every step.", ADJ]], 90),

Q("Stepwise asthma therapy", IO_PROT, "monitoring",
  "In the assess, adjust and review response cycle of asthma management, which item is checked when reviewing the response?",
  [["Exacerbations and side effects", "Correct. Reviewing the response covers symptoms, exacerbations, side effects, lung function and patient satisfaction, and the cycle then returns to assessment."],
   ["Confirmation of the diagnosis", "Confirming the diagnosis, if necessary, belongs to the assess phase with symptom control, comorbidities, inhaler technique and patient goals.", ADJ],
   ["Education and skills training", "Education and skills training belong to the adjust phase with nonpharmacologic strategies and asthma medications; the review covers exacerbations and side effects.", ADJ],
   ["Inhaler technique and adherence", "Inhaler technique and adherence are checked in the assess phase; the review of response covers symptoms, exacerbations, side effects, lung function and satisfaction.", ADJ]], 90),

# ---- devices: nebulizer (slides 91-92) -------------------------------------------------------------
Q("Inhaler devices", IO_EDU, "education",
  "Which device uses a compressor to force liquid medication into a fine mist?",
  [["Nebulizer", "Correct. In a nebulizer a compressor forces liquid medication into a fine mist, allowing passive inhalation through the mouthpiece or mask."],
   ["Metered dose inhaler", "A metered dose inhaler also makes a fine mist from liquid medication, but a propellant in the canister drives it, not a compressor.", MECH],
   ["Dry powder inhaler", "A dry powder inhaler holds medication as a powder, and the patient's own inspiratory force draws it out; there is no compressor.", MECH],
   ["Valve holding chamber", "A valve holding chamber attaches to an inhaler and has one-way valves that keep the patient from exhaling into it; the compressor belongs to the nebulizer.", MECH]], 92),

Q("Inhaler devices", IO_AE, "adverse effect",
  "Why can nebulized treatment lead to more side effects than other inhaled delivery?",
  [["A bigger dose is given overall", "Correct. A nebulizer administers a bigger dose overall, which may lead to more side effects, although its passive inhalation suits children and older adults who cannot use an inhaler."],
   ["It requires the most coordination", "Requiring the most coordination describes the metered dose inhaler, and it explains poor delivery rather than extra side effects; the nebulizer gives a bigger dose overall.", ADJ],
   ["It retains the larger particles", "Retaining large particles is what a spacer or valve holding chamber does; the nebulizer's extra side effects come from the bigger overall dose.", MECH],
   ["It needs strong inspiratory force", "Strong inspiratory force is needed for a dry powder inhaler; a nebulizer allows passive inhalation, and its side effects come from the bigger overall dose.", REV]], 92),

# ---- devices: dry powder inhaler (slide 93) --------------------------------------------------------
Q("Inhaler devices", IO_EDU, "education",
  "In a dry powder inhaler, what draws the medication out of the device?",
  [["The patient's inspiratory force", "Correct. In a dry powder inhaler the medication is a powder, and the patient provides the inspiratory force that draws it out of the device."],
   ["A propellant in the canister", "A propellant in the canister drives a metered dose inhaler; a dry powder inhaler depends on the patient's own inspiratory force.", MECH],
   ["An electric compressor", "A compressor powers a nebulizer, which turns liquid medication into a mist; a dry powder inhaler depends on the patient's inspiratory force.", MECH],
   ["A one-way valve chamber", "One-way valves belong to a valve holding chamber used with an inhaler; a dry powder inhaler depends on the patient's inspiratory force.", MECH]], 93),

Q("Inhaler devices", IO_CONTRA, "contraindication",
  "Which device is a poor choice for a patient with poor inspiratory capacity?",
  [["Dry powder inhaler", "Correct. A dry powder inhaler needs the patient's inspiratory force to draw the powder out, so it is not good for patients with poor inspiratory capacity."],
   ["Nebulizer", "A nebulizer allows passive inhalation of a fine mist, so it does not depend on inspiratory force; the dry powder inhaler does.", REV],
   ["Metered dose inhaler", "A metered dose inhaler's propellant forces the medication out, so its demand is coordination rather than inspiratory force; the dry powder inhaler depends on inspiratory force.", ADJ],
   ["Valve holding chamber", "A valve holding chamber holds medication released by an inhaler and suits patients with poor coordination; the device unsuited to poor inspiratory capacity is the dry powder inhaler.", ADJ]], 93),

# ---- devices: metered dose inhaler, spacers and valve holding chambers (slides 94-95) --------------
Q("Inhaler devices", IO_EDU, "education",
  "Which inhaled delivery method requires the most coordination for proper use?",
  [["Metered dose inhaler", "Correct. The metered dose inhaler requires the most coordination for proper use; a spacer holds the medication for patients with poor coordination."],
   ["Dry powder inhaler", "A dry powder inhaler requires inspiratory force to draw out the powder; the method requiring the most coordination is the metered dose inhaler.", ADJ],
   ["Nebulizer", "A nebulizer allows passive inhalation and suits patients who cannot use a metered dose inhaler; the metered dose inhaler requires the most coordination.", REV],
   ["Inhaler with a spacer", "A spacer is added precisely to hold the medication for patients with poor coordination; the plain metered dose inhaler requires the most coordination.", REV]], 94),

Q("Spacers and holding chambers", IO_EDU, "education",
  "What distinguishes a valve holding chamber from a simple spacer?",
  [["One-way valves that block exhaling into it", "Correct. A valve holding chamber has one-way valves that do not allow the patient to exhale into the device; a spacer is simply an open tube extending the inhaler away from the mouth."],
   ["An open tube extending the inhaler away", "An open tube that extends the inhaler away from the patient's mouth is the definition of a spacer itself; the valve holding chamber adds one-way valves.", REV],
   ["A compressor that makes a fine mist", "A compressor that forces liquid into a fine mist is the nebulizer; a valve holding chamber is distinguished by its one-way valves.", MECH],
   ["Powdered drug drawn out by inhaling", "Powdered medication drawn out by the patient's inspiratory force describes a dry powder inhaler; a valve holding chamber has one-way valves.", MECH]], 95),

Q("Spacers and holding chambers", IO_EDU, "education",
  "What does a spacer or valve holding chamber do to the particles the patient inhales?",
  [["Raises the share of small, respirable particles", "Correct. Spacers and valve holding chambers are intended to retain the large particles emitted from the inhaler, leaving a higher proportion of smaller, respirable particles."],
   ["Raises the share of large, heavy particles", "The chamber retains the large particles rather than delivering more of them; what reaches the patient is a higher proportion of small, respirable particles.", REV],
   ["Turns the liquid medication into a powder", "Medication in powder form belongs to the dry powder inhaler; a spacer leaves a higher proportion of small, respirable particles by retaining large ones.", MECH],
   ["Raises the total dose that is delivered", "A bigger overall dose is a feature of the nebulizer; a spacer retains large particles so a higher proportion of small, respirable particles is inhaled.", ADJ]], 95),

# ---- inhaler technique (slides 96-97) --------------------------------------------------------------
Q("Inhaler technique", IO_EDU, "education",
  "What is the first step in using a metered dose inhaler?",
  [["Take off the cap and shake it", "Correct. The first step is to take off the cap and shake the inhaler (it may need to be primed); the patient then breathes out all the way before holding the inhaler in place."],
   ["Breathe out fully", "Breathing out fully (all the way) is the second step, after the cap is removed and the inhaler shaken.", STAGE],
   ["Press down while breathing in", "Pressing down while starting to breathe in slowly comes after the cap is off, the inhaler shaken and the breath let out fully.", STAGE],
   ["Hold the breath for 10 seconds", "The breath hold comes last, after the slow, deep inhalation; the first step is to take off the cap and shake the inhaler.", STAGE]], 96),

Q("Inhaler technique", IO_EDU, "education",
  "Without a holding chamber, how should the patient breathe in while pressing down on the inhaler?",
  [["Slowly and deeply", "Correct. The patient starts breathing in slowly as the inhaler is pressed down and breathes in slowly and deeply, then holds the breath."],
   ["Quickly and forcefully", "A quick, forceful breath is the opposite of the technique, which is to breathe in slowly and deeply as the inhaler is pressed.", REV],
   ["In short, shallow sips", "Short, shallow breaths do not match the technique; the patient breathes in slowly and deeply while pressing down on the inhaler.", LAY],
   ["Through the nose", "The inhaler is held at or in the mouth and the medication is breathed in through it, slowly and deeply; nasal breathing is not part of the technique.", LAY]], 97),

Q("Inhaler technique", IO_EDU, "education",
  "When a valve holding chamber is used, when should the patient begin breathing in?",
  [["Within 5 seconds after pressing down", "Correct. With a holding chamber the patient first presses down on the inhaler and then begins breathing in within 5 seconds."],
   ["At the same moment as pressing down", "Pressing down as breathing in starts is the technique without a holding chamber; with one, the patient presses first and breathes in within 5 seconds.", ADJ],
   ["Before pressing down on the inhaler", "Breathing in before the puff is released would draw in nothing from the chamber; the patient presses down first and breathes in within 5 seconds.", REV],
   ["After waiting at least half a minute", "Waiting 15 to 30 seconds is the pause between puffs of a quick-relief beta-2 agonist; with a holding chamber the breath in starts within 5 seconds of pressing.", ADJ]], 97),

Q("Inhaler technique", IO_EDU, "education",
  "After breathing in the medication, how long should the patient hold the breath, if comfortable?",
  [["10 seconds", "Correct. The patient holds the breath for 10 seconds, or as long as is comfortable, after breathing in slowly and deeply."],
   ["2 seconds", "Two seconds is too short; the technique is to hold the breath for 10 seconds or as long as is comfortable.", REV],
   ["5 seconds", "Five seconds is the window for starting to breathe in after pressing down with a holding chamber; the breath hold is 10 seconds.", ADJ],
   ["60 seconds", "A full minute is not asked of the patient; the breath hold is 10 seconds, or as long as is comfortable.", REV]], 97),

Q("Inhaler technique", IO_EDU, "education",
  "How long should a patient wait between puffs of an inhaled quick-relief beta-2 agonist?",
  [["15 to 30 seconds", "Correct. For inhaled quick-relief medicines (beta-2 agonists), the patient waits 15 to 30 seconds between puffs."],
   ["5 seconds", "Five seconds is the window for starting to breathe in after pressing down with a holding chamber; between puffs the wait is 15 to 30 seconds.", ADJ],
   ["10 seconds", "Ten seconds is the breath hold after inhaling; the wait between puffs of a quick-relief beta-2 agonist is 15 to 30 seconds.", ADJ],
   ["60 to 90 seconds", "A minute or more is longer than the stated pause; for quick-relief beta-2 agonists the wait between puffs is 15 to 30 seconds.", REV]], 97),

# ---- summary (slide 98) ----------------------------------------------------------------------------
Q("Asthma summary", IO_PROT, "monitoring",
  "A patient with asthma has needed albuterol many times a day for several weeks. What does this pattern indicate?",
  [["Poor control; adjust long-term therapy", "Correct. Albuterol provides only short-term relief and should be used sparingly; excessive use indicates poor control and the need to adjust long-term therapy."],
   ["Good control; keep the same plan", "Frequent albuterol use is the opposite of good control; excessive use indicates poor control and a need to adjust long-term therapy.", REV],
   ["A need for more albuterol per puff", "Raising the reliever does not address the problem; albuterol gives only short-term relief, and heavy use signals poor control needing long-term therapy adjustment.", LAY],
   ["A reason to stop the controller", "Stopping a controller would worsen control; long-term controllers are used daily if indicated, and heavy albuterol use calls for adjusting them.", REV]], 98),

Q("Asthma summary", IO_EDU, "education",
  "How should long-term controller medications be used in asthma when they are indicated?",
  [["Every day", "Correct. Asthma is a chronic disease, and long-term controller medications need to be used daily if indicated; albuterol is the one for short-term relief."],
   ["During attacks", "Short-term relief during attacks is albuterol's role; long-term controllers need to be used daily if indicated.", MECH],
   ["Before exercise", "Exercise can provoke bronchospasm, but controllers are not timed to it; long-term controller medications need to be used daily if indicated.", ADJ],
   ["When albuterol fails", "Controllers are not a backup reliever; they need to be used daily if indicated, while albuterol gives short-term relief and should be used sparingly.", LAY]], 98),

# ---- status asthmaticus (slide 99) -----------------------------------------------------------------
Q("Status asthmaticus", IO_IND, "physiology",
  "Which description defines status asthmaticus?",
  [["Attack unresponsive to first bronchodilators", "Correct. Status asthmaticus is a medical emergency: an acute exacerbation that remains unresponsive to initial bronchodilator treatment."],
   ["Daily symptoms with weekly night waking", "Daily symptoms with night waking more than once a week describe moderate persistent asthma in the severity classification, not the emergency of status asthmaticus.", COMP],
   ["Bronchospasm provoked by cold air", "Bronchospasm provoked by cold air, exercise or distilled water is nonspecific bronchial hyperreactivity; status asthmaticus is an exacerbation unresponsive to initial bronchodilators.", COMP],
   ["Early reaction followed by a late reaction", "An early fall in lung function followed by a late reaction hours later describes the asthmatic response to allergen; status asthmaticus is an exacerbation unresponsive to initial bronchodilators.", COMP]], 99),

Q("Status asthmaticus", IO_PROT, "protocol",
  "How is albuterol given in the status asthmaticus algorithm?",
  [["Continuously, by nebulizer", "Correct. The status asthmaticus algorithm gives continuous albuterol, nebulized, together with steroids, magnesium and, if the patient is intubated, ketamine."],
   ["By dry powder inhaler", "A dry powder inhaler needs inspiratory force the patient may not have; the algorithm gives continuous nebulized albuterol.", RULED],
   ["As a twice-daily inhaler", "Twice-daily, long-lasting dosing describes the long-acting beta-2 agonists; the status asthmaticus algorithm gives albuterol continuously by nebulizer.", MECH],
   ["As a single oral tablet", "Albuterol in status asthmaticus is not given by mouth; the algorithm gives it continuously by nebulizer.", LAY]], 99),

Q("Status asthmaticus", IO_PROT, "drug choice",
  "In the status asthmaticus algorithm, which route is preferred for steroids?",
  [["Intravenous", "Correct. The status asthmaticus algorithm lists steroids with the intravenous route preferred, alongside continuous nebulized albuterol and magnesium."],
   ["Inhaled", "Inhaled corticosteroids are long-term controllers that take up to 8 weeks for maximal effect; in status asthmaticus the algorithm prefers intravenous steroids.", STAGE],
   ["Oral", "Oral systemic steroids such as prednisone are used in asthma exacerbations, but for status asthmaticus the algorithm states the intravenous route is preferred.", ADJ],
   ["Topical", "A topical steroid is not a route on the status asthmaticus algorithm, which lists steroids with the intravenous route preferred.", LAY]], 99),

Q("Status asthmaticus", IO_PROT, "protocol",
  "Which mineral is part of the status asthmaticus algorithm, given as a bolus followed by a continuous infusion?",
  [["Magnesium", "Correct. Magnesium, a bolus followed by a continuous infusion, is part of the status asthmaticus algorithm with continuous nebulized albuterol and intravenous steroids."],
   ["Potassium", "Potassium is not on the status asthmaticus algorithm; the mineral given as a bolus and then an infusion is magnesium.", LAY],
   ["Calcium", "Calcium is not on the status asthmaticus algorithm (cromolyn's unknown mechanism may interfere with calcium); the mineral given is magnesium.", ADJ],
   ["Sodium", "Sodium chloride fluid belongs to volume expansion in anaphylaxis, not to the status asthmaticus algorithm; the mineral given is magnesium.", ADJ]], 99),

Q("Status asthmaticus", IO_IND, "indication",
  "In the status asthmaticus algorithm, when is ketamine listed?",
  [["If the patient is intubated", "Correct. Ketamine is listed in status asthmaticus if the patient is intubated; it increases catecholamine release, causing bronchodilation."],
   ["Before any albuterol is given", "Continuous nebulized albuterol is the first agent on the algorithm; ketamine is reserved for the intubated patient.", STAGE],
   ["In place of steroids", "Steroids, intravenous preferred, remain part of the algorithm; ketamine is added if the patient is intubated.", STAGE],
   ["For mild intermittent asthma", "Mild intermittent asthma is not a medical emergency; ketamine belongs to status asthmaticus, and then only if the patient is intubated.", STAGE]], 99),

Q("Status asthmaticus", IO_MOA, "mechanism",
  "How does ketamine produce bronchodilation in status asthmaticus?",
  [["It increases catecholamine release", "Correct. Ketamine, an N-methyl-D-aspartate (NMDA) receptor antagonist and dissociative anesthetic, increases catecholamine release, which causes bronchodilation."],
   ["It blocks muscarinic receptors", "Blocking acetylcholine at muscarinic receptors is how anticholinergics such as ipratropium bronchodilate; ketamine works by increasing catecholamine release.", MECH],
   ["It inhibits phosphodiesterase", "Phosphodiesterase inhibition, raising cyclic adenosine monophosphate, is theophylline's mechanism; ketamine bronchodilates by increasing catecholamine release.", MECH],
   ["It stabilizes mast cells", "Mast cell stabilization belongs to cromolyn and nedocromil, which must be taken before antigen exposure; ketamine increases catecholamine release.", MECH]], 99),

Q("Status asthmaticus", IO_CLASS, "class",
  "Ketamine, listed for the intubated patient in status asthmaticus, belongs to which drug class?",
  [["Dissociative anesthetic", "Correct. Ketamine is a dissociative anesthetic and an N-methyl-D-aspartate (NMDA) receptor antagonist; it increases catecholamine release, causing bronchodilation."],
   ["Methylxanthine", "Methylxanthines are theophylline and intravenous aminophylline, nonspecific phosphodiesterase inhibitors; ketamine is a dissociative anesthetic.", MECH],
   ["Anticholinergic", "Anticholinergics such as ipratropium and tiotropium block muscarinic receptors; ketamine is a dissociative anesthetic.", MECH],
   ["Mast cell stabilizer", "Mast cell stabilizers are cromolyn and nedocromil; ketamine is a dissociative anesthetic that acts on the N-methyl-D-aspartate (NMDA) receptor.", MECH]], 99),

Q("Status asthmaticus", IO_AE, "adverse effect",
  "Which adverse effect is listed for ketamine in status asthmaticus?",
  [["Emergence phenomenon", "Correct. Ketamine's listed adverse reactions are emergence phenomenon, hypertension, tachycardia and vomiting."],
   ["Hypotension and bradycardia", "Ketamine raises the blood pressure and heart rate; its listed adverse reactions include hypertension and tachycardia, with emergence phenomenon and vomiting.", REV],
   ["Oral candidiasis", "Oral candidiasis (thrush) is an adverse effect of inhaled corticosteroids; ketamine's listed adverse reactions include emergence phenomenon.", ADJ],
   ["Red-green color loss", "Decreased red-green discrimination is an ethambutol adverse effect; ketamine's listed adverse reactions include emergence phenomenon.", ADJ]], 99),
]
