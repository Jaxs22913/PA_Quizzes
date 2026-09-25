# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- ENT, topic 3: antihistamines and corticosteroids.

Scope as in pharm_ent_pool_anti.py: indications and agent-specific adverse
effects ARE asked, corrected 2026-09-18. The steroid slides therefore carry
both the class behavior the agents share and the effects attached to each,
rather than the class behavior alone.

The spine of the antihistamine half is that one distinction explains most of
the rest: first generation agents enter the central nervous system and hit
other receptor systems on the way, second generation ones do not. Sedation, the
antiemetic use, the dry mouth and the sleep-aid marketing all fall out of it.
"""

D = "ENT Jax Pharmacology.pptx"
IO_CLASS = "Identify ENT drug classes and commonly prescribed ENT drugs"
IO_MOA = "Describe the mechanism of action of ENT drugs"
IO_IND = "Identify indications for commonly used ENT drugs"
IO_SE = "Summarize side effects and toxic manifestations of ENT drugs"
IO_CONTRA = "Identify contraindications for ENT drugs"
IO_EDU = "Outline appropriate patient education for ENT drugs"
IO_INTERACT = "Discuss potential drug-drug, drug-food, and drug-herb interactions with ENT drugs"

QUESTIONS = [

{"topic": "Histamine", "io": IO_MOA, "slot": "mechanism",
 "q": "Histamine release produces the triple response. What are its three components?",
 "opts": [
  ["Redness, a wheal, and a surrounding flare", "Correct. Three visible signs from three different mechanisms -- direct vasodilation, leaking capillaries, and a nerve reflex -- which is why they appear together but look different."],
  ["Redness, itching and sneezing", "Itching and sneezing are symptoms rather than the components of the triple response."],
  ["Swelling, pallor and numbness", "Pallor is the opposite of what histamine produces. The triple response is redness, a wheal and a surrounding flare."],
  ["Bronchospasm, hypotension and rash", "That describes anaphylaxis rather than the local triple response."]],
 "c": 0, "cite": D + ", Slide 27"},

{"topic": "Histamine", "io": IO_MOA, "slot": "mechanism",
 "q": "What produces the flare, the redness spreading out around the original insult?",
 "opts": [
  ["A reflex through axons causing vasodilation", "Correct. It is a nerve reflex rather than direct spread of histamine, which is why the flare extends beyond where the histamine actually is."],
  ["Direct vasodilation by histamine at that site", "Direct vasodilation accounts for the central redness, not the spreading flare."],
  ["Fluid leaking from post-capillary venules", "That produces the wheal. The spreading flare comes from a reflex through axons causing vasodilation."],
  ["Mast cells migrating outward from the site", "Cell migration is not the described mechanism. The flare spreads through an axonal reflex rather than by cells moving."]],
 "c": 0, "cite": D + ", Slide 27"},

{"topic": "Histamine receptors", "io": IO_MOA, "slot": "mechanism",
 "q": "Through which second messenger pathway do H1 receptors raise intracellular calcium?",
 "opts": [
  ["Phospholipase C, producing IP3 and DAG", "Correct. It is the contrast with H2 that matters: H1 works through phospholipase C, H2 through adenylate cyclase and cyclic AMP."],
  ["Adenylate cyclase, raising cyclic AMP", "That is the H2 pathway. H1 receptors work through phospholipase C, producing IP3 and DAG to raise calcium."],
  ["Direct opening of a ligand-gated sodium channel", "Histamine receptors here are described as acting through second messengers."],
  ["Inhibition of guanylate cyclase", "Not the described pathway. H1 acts through phospholipase C; H2 acts through adenylate cyclase."]],
 "c": 0, "cite": D + ", Slide 29"},

{"topic": "Histamine receptors", "io": IO_MOA, "slot": "mechanism",
 "q": "H1 and H2 receptors both cause vasodilation. How do the two differ?",
 "opts": [
  ["H1 is rapid in onset and short-lived", "Correct. Same end result by two different routes and on two different timescales, which is why blocking H1 alone does not abolish the flush. H2 is slow in onset and long-lasting."],
  ["H1 is slow and sustained, H2 is rapid and brief", "The timings are the other way round: H1 vasodilation is rapid and short-lived, H2 is slow in onset and long-lasting."],
  ["Both are rapid and brief", "They differ in timing, which is the point of comparing them."],
  ["Only H1 causes vasodilation", "H2 causes vasodilation as well, by a slower and longer-lasting route, which is why blocking H1 alone does not abolish flushing."]],
 "c": 0, "cite": D + ", Slide 29"},

{"topic": "Histamine receptors", "io": IO_MOA, "slot": "mechanism",
 "q": "What effect do H1 receptors have on smooth muscle and airways?",
 "opts": [
  ["They raise smooth muscle tone and cause bronchoconstriction", "Correct. This is why an H1 antagonist relaxes airway and gut smooth muscle, and why histamine itself is a bronchoconstrictor."],
  ["They lower smooth muscle tone and cause bronchodilation", "That direction belongs to H2, which lowers smooth muscle tone."],
  ["They have no effect on smooth muscle", "Smooth muscle is a principal H1 target: H1 raises smooth muscle tone and causes bronchoconstriction."],
  ["They act only on vascular smooth muscle", "The effect extends to airway and gastrointestinal smooth muscle."]],
 "c": 0, "cite": D + ", Slide 29"},

{"topic": "Histamine receptors", "io": IO_MOA, "slot": "mechanism",
 "q": "Which effect belongs to H2 rather than H1 receptors?",
 "opts": [
  ["Increased gastric acid secretion", "Correct. It is the reason H2 blockers are stomach drugs while H1 blockers are allergy drugs."],
  ["Stimulation of sensory nerve endings", "That is an H1 effect. The H2 effects include gastric acid secretion, slow vasodilation and increased cardiac contractility."],
  ["Increased post-capillary permeability", "That is an H1 effect, and it is what produces the wheal. H2 raises gastric acid secretion instead."],
  ["Bronchoconstriction", "That is an H1 effect. H2 lowers smooth muscle tone rather than raising it, and raises gastric acid secretion."]],
 "c": 0, "cite": D + ", Slide 30"},

{"topic": "Histamine receptors", "io": IO_MOA, "slot": "mechanism",
 "q": "What effect does histamine have on the heart through H2 receptors?",
 "opts": [
  ["It increases contractility", "Correct. A cardiac action is easy to miss in a receptor filed under the stomach."],
  ["It slows conduction through the atrioventricular node", "Not the described cardiac effect. Histamine acting at H2 increases the contractility of the heart."],
  ["It reduces contractility", "The effect is to increase contractility, which is an easy cardiac action to overlook in a receptor filed under the stomach."],
  ["It has no cardiac effect", "An effect on contractility is described: H2 activation increases it."]],
 "c": 0, "cite": D + ", Slide 30"},

{"topic": "H1 antagonists", "io": IO_MOA, "slot": "mechanism",
 "q": "What do H1 antagonists do peripherally?",
 "opts": [
  ["Reduce secretions, edema, hives and itching", "Correct. Each of these is the mirror image of an H1 action, which is why the antagonist's effects can be read straight off the receptor. Block smooth muscle contraction."],
  ["Reduce gastric acid secretion", "That would be an H2 blocker. H1 antagonists reduce secretions, edema, hives and itching, and block smooth muscle contraction."],
  ["Increase mucus secretion to clear allergens", "They reduce secretion rather than increasing it, mirroring histamine's own effect at the H1 receptor."],
  ["Cause bronchoconstriction", "They block the bronchoconstriction histamine produces, since bronchoconstriction is itself an H1 effect."]],
 "c": 0, "cite": D + ", Slide 31"},

{"topic": "H1 antagonists", "io": IO_SE, "slot": "adverse effect",
 "q": "What is the major central nervous system side effect of first generation H1 antagonists?",
 "opts": [
  ["Sedation", "Correct. It is the dominant side effect, and it is also the basis of an entire over-the-counter market in sleep aids."],
  ["Tremor", "Not the described central effect. Sedation is the major central nervous system side effect of first generation agents."],
  ["Headache", "Not the major central effect described, which is sedation, additive with alcohol and other depressants."],
  ["Seizures at ordinary use", "Excitation appears at higher exposure rather than at ordinary use."]],
 "c": 0, "cite": D + ", Slide 32"},

{"topic": "H1 antagonists", "io": IO_SE, "slot": "adverse effect",
 "q": "A child given a first generation antihistamine becomes restless and agitated rather than sleepy. How is that explained?",
 "opts": [
  ["Excitation occurs at higher exposure, and particularly in children", "Correct. The paradox is recognized rather than unusual, and it means an agitated child may have had more of the drug rather than less."],
  ["The child has developed tolerance to the sedating effect", "Tolerance is not the described explanation. Excitation occurs at higher exposure and is seen particularly in children."],
  ["The drug was a second generation agent", "Second generation agents do not enter the central nervous system enough to produce either effect."],
  ["It indicates an allergic reaction to the antihistamine", "Excitation is a recognized central effect rather than an allergic one."]],
 "c": 0, "cite": D + ", Slide 32"},

{"topic": "H1 antagonists", "io": IO_MOA, "slot": "mechanism",
 "q": "Why do second generation antihistamines cause much less sedation?",
 "opts": [
  ["They do not enter the central nervous system",
   "Correct. The whole generational difference comes down to where the drug goes rather than what it blocks. Not to the same extent, at any rate, which is the whole generational difference."],
  ["They block H2 rather than H1 receptors", "They remain H1 antagonists. What changed between the generations is entry into the central nervous system."],
  ["They are given at much lower exposure", "The difference is distribution rather than amount: second generation agents do not enter the central nervous system to the same extent."],
  ["They are broken down before reaching the brain", "It is entry into the central nervous system that differs rather than metabolism before arrival."]],
 "c": 0, "cite": D + ", Slide 32"},

{"topic": "H1 antagonists", "io": IO_INTERACT, "slot": "education",
 "q": "What should a patient taking a first generation antihistamine be warned about?",
 "opts": [
  ["Sedation is additive with alcohol and other depressants",
   "Correct. The risk is in the combination rather than the drug alone, which is what makes it easy to stumble into. Central nervous system depressants generally."],
  ["It must not be taken together with food",
   "Food is not a stated concern. The warning is that sedation is additive with alcohol and other central nervous system depressants."],
  ["It raises the blood pressure",
   "Hypertension belongs to the decongestants. The antihistamine warning concerns additive sedation with alcohol and depressants."],
  ["It causes rebound symptoms if stopped", "Rebound belongs to topical decongestants. The antihistamine warning is about additive sedation."]],
 "c": 0, "cite": D + ", Slide 32"},

{"topic": "H1 antagonists", "io": IO_CLASS, "slot": "drug choice",
 "q": "Which agent is named as an over-the-counter sleep aid?",
 "opts": [
  ["Doxylamine", "Correct. A sedating antihistamine sold for the side effect rather than the indication."],
  ["Azelastine", "Azelastine is a nasal spray for allergic and vasomotor rhinitis rather than a sleep aid; doxylamine is the sleep aid named."],
  ["Promethazine", "Promethazine is named for its antimuscarinic and antiemetic strength."],
  ["Fluticasone", "Fluticasone is a nasal corticosteroid rather than an antihistamine. Doxylamine is the agent sold as a sleep aid."]],
 "c": 0, "cite": D + ", Slide 32"},

{"topic": "H1 antagonists", "io": IO_MOA, "slot": "mechanism",
 "q": "Beyond histamine receptors, what else do first generation agents act on?",
 "opts": [
  ["Muscarinic and serotonergic systems", "Correct. Acting on several receptor families is what gives them uses and side effects that have nothing to do with allergy. With antiemetic action."],
  ["Adrenergic receptors only", "Adrenergic action is not among those described. First generation agents act on muscarinic and serotonergic systems, with antiemetic action."],
  ["Dopamine receptors in the basal ganglia", "Not among the systems described, which are the muscarinic and serotonergic systems alongside an antiemetic action."],
  ["Nothing else -- they are entirely selective", "Being non-selective is precisely the point of the first generation."]],
 "c": 0, "cite": D + ", Slide 33"},

{"topic": "H1 antagonists", "io": IO_IND, "slot": "drug choice",
 "q": "Which agent is singled out as having the strongest antimuscarinic action, especially for motion sickness?",
 "opts": [
  ["Promethazine", "Correct. The antimuscarinic strength is what makes it the motion sickness choice, not its antihistamine potency."],
  ["Doxylamine", "Doxylamine is named as a sleep aid. Promethazine is the agent singled out for antimuscarinic strength in motion sickness."],
  ["Azelastine", "Azelastine is a nasal antihistamine for rhinitis. Promethazine is the one named for its antimuscarinic strength."],
  ["Cetirizine", "A second generation agent, which by design lacks these extra actions."]],
 "c": 0, "cite": D + ", Slide 34"},

{"topic": "H1 antagonists", "io": IO_MOA, "slot": "mechanism",
 "q": "How do antihistamines reduce nasal and bronchial secretions during an allergic reaction?",
 "opts": [
  ["Through their antimuscarinic action", "Correct. The drying is a muscarinic effect rather than a histamine one, which is why the second generation agents dry you out less."],
  ["By blocking H2 receptors on glands", "H2 blockade is not the mechanism. The drying of nasal and bronchial secretions is an antimuscarinic effect."],
  ["By constricting the vessels supplying the mucosa", "Vasoconstriction is the decongestant mechanism. Antihistamines dry secretions through antimuscarinic action instead."],
  ["By thinning the mucus already produced", "Thinning mucus is what an expectorant does. Antihistamines reduce the secretion itself, through antimuscarinic action."]],
 "c": 0, "cite": D + ", Slide 34"},

{"topic": "H1 antagonists", "io": IO_IND, "slot": "drug choice",
 "q": "Which of these is NOT among the listed indications for H1 antagonists?",
 "opts": [
  ["Bacterial sinusitis", "Correct -- this is not one. The indications are allergic reactions, motion sickness and vestibular symptoms, sleep remedies, and an adjuvant role in anaphylaxis."],
  ["Allergic rhinitis and urticaria", "These are listed indications, alongside motion sickness, sleep remedies and an adjuvant role in anaphylaxis."],
  ["Motion sickness and vestibular disturbance", "This is a listed indication, alongside allergic reactions, sleep remedies and an adjuvant role in anaphylaxis."],
  ["An adjuvant role in anaphylaxis", "This is a listed indication, though an adjuvant one: adrenaline remains the treatment for anaphylaxis."]],
 "c": 0, "cite": D + ", Slide 35"},

{"topic": "H1 antagonists", "io": IO_IND, "slot": "drug choice",
 "q": "What is the role of an antihistamine in anaphylaxis?",
 "opts": [
  ["Adjuvant only", "Correct. The word matters: it supports treatment rather than being it, and the drug that actually treats anaphylaxis is adrenaline."],
  ["First-line treatment", "It is explicitly an adjuvant rather than the primary treatment."],
  ["It has no role at all", "An adjuvant role is described. It supports treatment of anaphylaxis without replacing adrenaline."],
  ["It replaces adrenaline in a mild case", "It does not substitute for adrenaline at any severity; its role in anaphylaxis is explicitly adjuvant."]],
 "c": 0, "cite": D + ", Slide 35"},

{"topic": "H1 antagonists", "io": IO_SE, "slot": "adverse effect",
 "q": "A patient on a first generation antihistamine reports dry mouth, blurred vision and difficulty passing urine. What explains this?",
 "opts": [
  ["The antimuscarinic action of the drug", "Correct. Three complaints from three different organs, all explained by one receptor family being blocked."],
  ["Histamine receptor blockade itself", "These effects come from the muscarinic blockade rather than the H1 blockade."],
  ["An allergic reaction to the drug", "This is a predictable pharmacological effect rather than an allergy."],
  ["Interaction with alcohol", "Alcohol adds sedation rather than these effects. Dry mouth, blurred vision and urinary retention are antimuscarinic."]],
 "c": 0, "cite": D + ", Slide 36"},

{"topic": "H1 antagonists", "io": IO_SE, "slot": "adverse effect",
 "q": "Which adverse effects are specifically associated with topical use of antihistamines?",
 "opts": [
  ["Dermatitis and photosensitivity of the skin",
   "Correct. Applying an antihistamine to skin can produce the kind of reaction it was meant to treat."],
  ["Sedation, drowsiness and confusion",
   "These follow systemic use and entry into the central nervous system. Topical use is associated with dermatitis and photosensitivity."],
  ["Urinary retention and dry mouth",
   "An antimuscarinic effect of systemic use. The effects specific to topical application are dermatitis and photosensitivity."],
  ["Epistaxis", "Nosebleed relates to nasal sprays rather than to topical skin use."]],
 "c": 0, "cite": D + ", Slide 36"},

{"topic": "Azelastine", "io": IO_IND, "slot": "drug choice",
 "q": "What is azelastine nasal spray indicated for?",
 "opts": [
  ["Allergic and vasomotor rhinitis", "Correct. It covers vasomotor rhinitis as well as allergic, which matters because vasomotor rhinitis has no allergic trigger to avoid."],
  ["Bacterial sinusitis", "Not an indication for an antihistamine spray. Azelastine is indicated for allergic and vasomotor rhinitis."],
  ["Nasal congestion from the common cold", "That is the decongestant indication. Azelastine is for allergic and vasomotor rhinitis."],
  ["Epistaxis", "Epistaxis is a side effect of the spray rather than an indication."]],
 "c": 0, "cite": D + ", Slide 38"},

{"topic": "Azelastine", "io": IO_SE, "slot": "adverse effect",
 "q": "What side effects are described for azelastine nasal spray?",
 "opts": [
  ["A bitter taste and nosebleed", "Correct. The bitter taste is the common reason patients stop it, and it comes from spray running back into the throat."],
  ["Sedation and dry mouth", "These belong to systemic first generation agents. Azelastine's described effects are a bitter taste and nosebleed."],
  ["Rebound congestion", "Rebound belongs to topical decongestants. Azelastine's described effects are a bitter taste and nosebleed."],
  ["Raised intraocular pressure", "That belongs to the corticosteroids. Azelastine is associated with a bitter taste and nosebleed."]],
 "c": 0, "cite": D + ", Slide 38"},

{"topic": "Nasal spray technique", "io": IO_EDU, "slot": "education",
 "q": "Why is a patient told to use the right hand for the left nostril and the left hand for the right?",
 "opts": [
  ["It angles the spray away from the septum", "Correct. Crossing hands sets the angle automatically, and the septum is what nosebleed and perforation happen to."],
  ["It distributes the medicine more evenly", "Even distribution is not the stated reason. Crossing hands angles the spray away from the septum."],
  ["It prevents contamination of the bottle tip", "Cleaning the tip is a separate instruction. Crossing hands is about directing the spray away from the septum."],
  ["It reduces the bitter taste", "Taste is addressed by not tilting the head back. Crossing hands protects the septum instead."]],
 "c": 0, "cite": D + ", Slide 39"},

{"topic": "Nasal spray technique", "io": IO_EDU, "slot": "education",
 "q": "Why is a patient told not to tilt the head back when using a nasal spray?",
 "opts": [
  ["It draws the medicine into the throat", "Correct. It wastes the dose and produces the bitter taste, which is the complaint that stops people using the spray at all."],
  ["It causes the spray to hit the septum", "Septal contact is managed by the angle rather than by head tilt backwards."],
  ["It increases the risk of nosebleed", "Nosebleed relates to septal contact, which the spray angle controls. Tilting back sends the medicine into the throat."],
  ["It reduces absorption through the skin", "Skin absorption is not relevant to a nasal spray. Tilting back draws the medicine into the throat and wastes it."]],
 "c": 0, "cite": D + ", Slide 39"},

{"topic": "Nasal spray technique", "io": IO_EDU, "slot": "education",
 "q": "A patient using a nasal spray develops a nosebleed. What are they told to do?",
 "opts": [
  ["Stop the spray and follow up immediately", "Correct. It is a stop-and-be-seen instruction rather than a wait-and-see one, because septal perforation is what lies beyond it."],
  ["Continue and use the other nostril only", "Continuing is not the instruction given. The advice is to stop the spray and follow up immediately."],
  ["Reduce to one spray daily and continue", "Reducing rather than stopping is not what is advised; the instruction is to stop and be seen, because perforation lies beyond."],
  ["Apply pressure and carry on as normal", "Carrying on is not the instruction. A nosebleed on a nasal spray means stopping it and following up immediately."]],
 "c": 0, "cite": D + ", Slide 39"},

{"topic": "Nasal corticosteroids", "io": IO_CLASS, "slot": "drug choice",
 "q": "Which warning accompanies the list of nasal corticosteroids?",
 "opts": [
  ["Many have inhaled versions for asthma", "Correct. The example given is fluticasone: the nasal product and the asthma inhaler are different preparations of the same drug with different names. The names are easy to confuse."],
  ["They must not be used for longer than a few days", "That restriction belongs to the topical decongestants. The warning on nasal steroids is that names overlap with asthma inhalers."],
  ["They are all prescription only", "Some are named as available over the counter. The warning attached is about confusing nasal and inhaled versions."],
  ["They cannot be used alongside an antihistamine", "No such restriction is given; the two are often used together. The warning concerns confusing nasal with inhaled preparations."]],
 "c": 0, "cite": D + ", Slide 42"},

{"topic": "Nasal corticosteroids", "io": IO_SE, "slot": "adverse effect",
 "q": "What are the described side effects of nasal corticosteroids?",
 "opts": [
  ["Nosebleed, perforation and an unpleasant taste",
   "Correct. All three are local, which is the trade-off that makes a nasal steroid different from a systemic one."],
  ["Glucose intolerance and fluid retention", "These are systemic corticosteroid effects rather than nasal ones."],
  ["Sedation and dry mouth", "These belong to first generation antihistamines. Nasal steroids cause nosebleed, septal perforation and an unpleasant taste."],
  ["Rebound congestion on stopping", "Rebound belongs to the topical decongestants. Nasal steroid effects are local: nosebleed, perforation and unpleasant taste."]],
 "c": 0, "cite": D + ", Slide 43"},

{"topic": "Nasal corticosteroids", "io": IO_IND, "slot": "drug choice",
 "q": "What are nasal corticosteroids indicated for?",
 "opts": [
  ["Allergic and vasomotor rhinitis", "Correct. The same two conditions the nasal antihistamine covers, which is why the two are often used together."],
  ["Acute bacterial sinusitis", "Not their indication. Nasal corticosteroids are indicated for allergic and vasomotor rhinitis."],
  ["Otitis externa", "Not a nasal indication. Nasal corticosteroids treat allergic and vasomotor rhinitis."],
  ["Chronic cough", "Not their stated indication, which is allergic and vasomotor rhinitis."]],
 "c": 0, "cite": D + ", Slide 43"},

{"topic": "Systemic corticosteroids", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which infection is specifically a contraindication to systemic corticosteroids?",
 "opts": [
  ["Systemic fungal infection", "Correct. A drug that suppresses immunity given to someone with a disseminated fungal infection makes the infection worse."],
  ["Bacterial sinusitis", "Not listed as a contraindication. Systemic fungal infection is the infection specifically named."],
  ["Viral upper respiratory infection", "Not listed as a contraindication; systemic fungal infection is the one specifically named."],
  ["Otitis media", "Not listed as a contraindication. The named contraindication among infections is systemic fungal infection."]],
 "c": 0, "cite": D + ", Slide 46"},

{"topic": "Systemic corticosteroids", "io": IO_EDU, "slot": "education",
 "q": "Why is a patient who has taken a corticosteroid for more than about a week told not to stop abruptly?",
 "opts": [
  ["Stopping suddenly produces rebound symptoms", "Correct. It is the duration that creates the problem, which is why a short course and a long one are stopped differently."],
  ["The drug accumulates and must be cleared slowly", "Accumulation is not the reason given. Stopping abruptly after more than about a week produces rebound symptoms."],
  ["Abrupt withdrawal causes fluid retention", "Fluid retention is an effect of taking the drug, not of stopping it."],
  ["The drug loses effect if restarted after a gap", "Loss of future effect is not the concern. Abrupt withdrawal after a week or more produces rebound symptoms."]],
 "c": 0, "cite": D + ", Slide 46"},

{"topic": "Systemic corticosteroids", "io": IO_EDU, "slot": "education",
 "q": "What is a patient on prednisone told about infection risk?",
 "opts": [
  ["They are immunocompromised and should avoid chickenpox", "Correct. Live vaccines are the part most easily missed, because the patient does not think of a vaccine as an exposure. Measles and live vaccines."],
  ["They should take prophylactic antibiotics", "Prophylaxis is not advised. The advice is to avoid chickenpox, measles and live vaccines while immunocompromised."],
  ["Infection risk only matters above a certain amount", "The advice is not framed as exposure-dependent. The patient is treated as immunocompromised and told to avoid live vaccines."],
  ["There is no increased risk with short courses", "The immune suppression is stated without a short-course exemption."]],
 "c": 0, "cite": D + ", Slide 48"},

{"topic": "Systemic corticosteroids", "io": IO_INTERACT, "slot": "mechanism",
 "q": "A patient on digoxin is started on dexamethasone. Why does that raise the risk of arrhythmia?",
 "opts": [
  ["Dexamethasone lowers potassium", "Correct. The interaction runs through the electrolyte rather than between the two drugs directly, which is why checking potassium is what protects the patient. Low potassium predisposes to digoxin toxicity."],
  ["Dexamethasone raises digoxin levels directly", "The mechanism described runs through potassium: dexamethasone lowers it, and low potassium predisposes to digoxin toxicity."],
  ["Digoxin increases the effect of dexamethasone", "The interaction is described in the other direction, and it runs through potassium loss rather than between the drugs directly."],
  ["Both prolong the QT interval independently", "Low potassium is the stated mechanism, and it is what predisposes the patient on digoxin to arrhythmia."]],
 "c": 0, "cite": D + ", Slide 45"},

{"topic": "Systemic corticosteroids", "io": IO_INTERACT, "slot": "next step",
 "q": "A patient on a diuretic is started on dexamethasone. What should be monitored?",
 "opts": [
  ["Potassium, since both drugs lower it",
   "Correct. Two drugs pushing the same electrolyte the same way, which is how a patient arrives at a dangerous level without either drug being at fault alone."],
  ["Liver enzymes and bilirubin",
   "Not the concern in this combination. Both a diuretic and dexamethasone lower potassium, so potassium is what to monitor."],
  ["Thyroid function tests",
   "Not the concern in this combination; potassium is, since both drugs push it the same way."],
  ["Prothrombin time and clotting",
   "Not relevant to this pairing. Potassium is the shared target of a diuretic and a corticosteroid."]],
 "c": 0, "cite": D + ", Slide 45"},

{"topic": "Systemic corticosteroids", "io": IO_INTERACT, "slot": "mechanism",
 "q": "Why does a macrolide antibiotic matter in a patient taking dexamethasone?",
 "opts": [
  ["Macrolides reduce dexamethasone clearance", "Correct. The steroid is not changed; it simply stays around longer, which is enough to turn a tolerable course into a problematic one. So its effect is amplified."],
  ["Macrolides inactivate dexamethasone", "The interaction increases exposure rather than reducing it: macrolides decrease dexamethasone clearance, so it lingers."],
  ["Dexamethasone blocks macrolide absorption", "The interaction is described in the other direction: the macrolide reduces clearance of the steroid."],
  ["The two combine to cause hyperkalemia", "Corticosteroids are associated with potassium loss rather than retention."]],
 "c": 0, "cite": D + ", Slide 45"},

{"topic": "Systemic corticosteroids", "io": IO_INTERACT, "slot": "next step",
 "q": "A patient with diabetes is started on a course of prednisone. What should be anticipated?",
 "opts": [
  ["Glucose control will worsen", "Correct. Two effects pointing the same way: the steroid raises glucose and blunts the drugs used to lower it. Antidiabetic medicines will work less well."],
  ["Glucose will fall and treatment may need reducing", "Corticosteroids raise glucose rather than lowering it, and they also reduce the effect of antidiabetic medicines."],
  ["There is no interaction with antidiabetic medicines", "A reduced effect on antidiabetic treatment is specifically described."],
  ["Insulin requirements will fall", "They would be expected to rise: the steroid raises glucose and blunts the drugs used to lower it."]],
 "c": 0, "cite": D + ", Slide 45"},

{"topic": "Systemic corticosteroids", "io": IO_SE, "slot": "adverse effect",
 "q": "Which eye findings are associated with systemic corticosteroids?",
 "opts": [
  ["High intraocular pressure, glaucoma and cataract", "Correct. Worth holding onto because a course given for the nose can end up costing sight if it runs long enough."],
  ["Retinal detachment and vitreous hemorrhage", "Not among the described effects. The ocular effects are raised intraocular pressure, glaucoma, cataract and exophthalmos."],
  ["Optic neuritis", "Not among the described effects; the ocular harms listed are raised pressure, glaucoma, cataract and exophthalmos."],
  ["Corneal ulceration", "Not among the described effects. The eye findings are raised intraocular pressure, glaucoma and cataract."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": "Systemic corticosteroids", "io": IO_SE, "slot": "adverse effect",
 "q": "Which musculoskeletal harms are described with systemic corticosteroids?",
 "opts": [
  ["Tendon rupture and long bone fracture",
   "Correct. Structural damage rather than discomfort, and it can appear without warning."],
  ["Muscle cramps and myalgia only", "The described harms are structural rather than symptomatic: tendon rupture and pathological fracture of long bones."],
  ["Joint effusions and stiffness",
   "Not among the described effects. The musculoskeletal harms are tendon rupture and fracture of long bones."],
  ["Gout and joint crystal deposition",
   "Not among the described effects; the musculoskeletal harms described are tendon rupture and pathological fracture."]],
 "c": 0, "cite": D + ", Slide 47"},
]
