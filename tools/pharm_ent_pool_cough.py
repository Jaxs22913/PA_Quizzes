# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- ENT, topic 4: decongestants, antitussives, expectorants.

Scope as in pharm_ent_pool_anti.py: indications and agent-specific adverse
effects ARE asked (Jaxon, 2026-09-18); dosing and formulations are not, so the
concentration on the hypertonic saline slide is left alone while what it does
is asked.

Two things carry most of this section. The topical decongestant has a hard time
limit and a specific consequence for exceeding it -- rebound congestion, which
sends the patient back to the same bottle. And the two antitussives work at
opposite ends of the same reflex: benzonatate numbs the receptors where the
cough starts, dextromethorphan suppresses the centre in the medulla where it is
organised.
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

{"topic": "Oxymetazoline", "io": IO_MOA, "slot": "mechanism",
 "q": "How does oxymetazoline relieve nasal congestion?",
 "opts": [
  ["It is an alpha agonist that constricts vessels in the nasal mucosa", "Correct. Congestion is swollen mucosa rather than mucus, so shrinking the vessels is what opens the nose."],
  ["It blocks histamine H1 receptors in the mucosa", "That is an antihistamine's mechanism. Oxymetazoline is an alpha agonist that constricts vessels in the nasal mucosa."],
  ["It thins mucus so it drains more easily", "That is an expectorant's action. Congestion is swollen mucosa rather than mucus, so the decongestant shrinks vessels."],
  ["It reduces inflammation through a glucocorticoid receptor", "That is the nasal corticosteroid mechanism. Oxymetazoline acts as an alpha agonist on the mucosal vessels."]],
 "c": 0, "cite": D + ", Slide 50"},

{"topic": "Oxymetazoline", "io": IO_SE, "slot": "adverse effect",
 "q": "A patient has used a topical decongestant spray daily for three weeks and is more blocked than when they started. What has happened?",
 "opts": [
  ["Rebound congestion, rhinitis medicamentosa", "Correct. The drug produces the symptom it was bought to relieve, which is why the patient keeps using it and why the cycle is hard to break."],
  ["They have developed allergic rhinitis", "The history of prolonged spray use points to rebound rather than a new allergy."],
  ["Bacterial sinusitis has developed", "Nothing here indicates bacterial infection. Weeks of daily spray use points to rebound congestion, rhinitis medicamentosa."],
  ["Tolerance, with no rebound effect", "The described effect is an active worsening rather than simple loss of benefit."]],
 "c": 0, "cite": D + ", Slide 50"},

{"topic": "Oxymetazoline", "io": IO_EDU, "slot": "education",
 "q": "What is the central instruction for a patient given a topical nasal decongestant?",
 "opts": [
  ["Do not use it beyond a few days", "Correct. It is the whole safety message for this drug, and exceeding it is what produces rebound congestion."],
  ["Use it every day through the allergy season", "Continuous use is exactly what causes the problem; beyond a few days the spray produces rebound congestion."],
  ["Use it only at night", "Timing is not the restriction. The restriction is on duration: no more than a few days of use."],
  ["Always combine it with a nasal steroid", "Combining nasal sprays is specifically discouraged, and it does nothing about the duration limit that matters here."]],
 "c": 0, "cite": D + ", Slide 51"},

{"topic": "Oxymetazoline", "io": IO_SE, "slot": "adverse effect",
 "q": "Besides rebound congestion, what systemic effect is described with oxymetazoline?",
 "opts": [
  ["Raised blood pressure", "Correct. A drug sprayed into the nose still reaches the circulation, which is what makes it worth asking about in a hypertensive patient."],
  ["A slow heart rate",
   "An alpha agonist would not be expected to do this, and it is not described."],
  ["Drowsiness and sedation",
   "Sedation belongs to first generation antihistamines. Oxymetazoline's systemic effect is raised blood pressure."],
  ["Hypoglycaemia", "Not among the described effects. Oxymetazoline is associated with rebound congestion and raised blood pressure."]],
 "c": 0, "cite": D + ", Slide 50"},

{"topic": "Oxymetazoline", "io": IO_INTERACT, "slot": "mechanism",
 "q": "Which medicines interact with oxymetazoline?",
 "opts": [
  ["Monoamine oxidase inhibitors and antidepressants", "Correct. Both raise the effect of a sympathomimetic, so an over-the-counter spray becomes a blood pressure problem in these patients."],
  ["Antibiotics of any class or route",
   "Not among the described interactions, which are with monoamine oxidase inhibitors and antidepressants."],
  ["Oral and nasal antihistamine preparations",
   "Not among the described interactions; monoamine oxidase inhibitors and antidepressants are the ones named."],
  ["Proton pump inhibitors and other antacid drugs",
   "Not among the described interactions. Monoamine oxidase inhibitors and antidepressants are what raise the risk."]],
 "c": 0, "cite": D + ", Slide 51"},

{"topic": "Pseudoephedrine", "io": IO_MOA, "slot": "mechanism",
 "q": "How does pseudoephedrine differ from oxymetazoline in mechanism and route?",
 "opts": [
  ["Same alpha agonist mechanism, but taken orally", "Correct. The mechanism is shared; taking it orally is what changes both its usefulness and its side effect profile."],
  ["It blocks histamine receptors and is taken orally", "It is a decongestant rather than an antihistamine: an alpha agonist that constricts nasal vessels, taken orally."],
  ["It is an alpha antagonist given orally", "Antagonism would worsen congestion rather than relieve it. Pseudoephedrine is an alpha agonist."],
  ["It is a topical steroid", "It is neither topical nor a steroid. Pseudoephedrine is an oral alpha agonist that constricts nasal vessels."]],
 "c": 0, "cite": D + ", Slide 52"},

{"topic": "Pseudoephedrine", "io": IO_IND, "slot": "drug choice",
 "q": "Which ear complaint is pseudoephedrine indicated for?",
 "opts": [
  ["Eustachian tube dysfunction",
   "Correct. A nasal decongestant given for an ear problem, which makes sense once the tube is understood as opening into the nose. Specifically, the eustachian tube dysfunction that follows a viral infection."],
  ["Acute otitis media in a young child",
   "Antibiotics rather than decongestants are the treatment described."],
  ["Otitis externa following swimming",
   "A canal problem treated with drops. The ear indication for a decongestant is eustachian tube dysfunction after a viral infection."],
  ["Sudden sensorineural hearing loss",
   "Not an indication for a decongestant. The ear indication is eustachian tube dysfunction following a viral infection."]],
 "c": 0, "cite": D + ", Slide 52"},

{"topic": "Pseudoephedrine", "io": IO_IND, "slot": "drug choice",
 "q": "What congestion is pseudoephedrine indicated to relieve?",
 "opts": [
  ["Nasal and sinus congestion from a cold", "Correct. It covers both infective and allergic causes, because it acts on the swollen vessels rather than on the cause of the swelling. Hay fever or allergy."],
  ["Congestion from bacterial sinusitis only", "Its indications are broader than bacterial infection: congestion from a cold, hay fever or allergy, and sinus congestion."],
  ["Chest congestion with productive cough", "That is the expectorant's territory. Pseudoephedrine relieves nasal and sinus congestion."],
  ["Congestion from nasal polyps only", "Not the stated indication, which covers congestion from a cold, hay fever or allergy, and sinus congestion."]],
 "c": 0, "cite": D + ", Slide 52"},

{"topic": "Pseudoephedrine", "io": IO_SE, "slot": "adverse effect",
 "q": "What adverse effects are described with pseudoephedrine?",
 "opts": [
  ["Fast heart rate", "Correct. All three follow from stimulating alpha receptors throughout the body rather than only in the nose. Raised blood pressure and headache."],
  ["Sedation and dry mouth", "These belong to first generation antihistamines. Pseudoephedrine causes tachycardia, raised blood pressure and headache."],
  ["Diarrhoea and abdominal pain", "These are described with oral nystatin. Pseudoephedrine's effects are cardiovascular, with headache."],
  ["Nosebleed and bitter taste", "These belong to nasal sprays. Pseudoephedrine is taken orally and causes tachycardia, hypertension and headache."]],
 "c": 0, "cite": D + ", Slide 52"},

{"topic": "Pseudoephedrine", "io": IO_INTERACT, "slot": "next step",
 "q": "A patient treated for hypertension asks about pseudoephedrine for a cold. What is the concern?",
 "opts": [
  ["It reduces the effect of antihypertensive medicines", "Correct. A patient can undo their blood pressure treatment with something bought off the shelf, without ever mentioning it as a medicine."],
  ["It increases the effect of antihypertensives, causing hypotension", "The interaction runs the other way: pseudoephedrine reduces the effect of antihypertensive medicines."],
  ["It has no effect on blood pressure treatment", "A reduced antihypertensive effect is specifically described."],
  ["It cannot be taken with any antibiotic", "Antibiotics are not the interaction described. The concern is a reduced effect of antihypertensive treatment."]],
 "c": 0, "cite": D + ", Slide 52"},

{"topic": "Cough reflex", "io": IO_MOA, "slot": "mechanism",
 "q": "Where is the cough reflex organised?",
 "opts": [
  ["In a cough centre in the medulla oblongata", "Correct. Receptors in the airway start it, but the medulla organises it, which is why one drug class works at each end."],
  ["In the cerebral cortex, under voluntary control",
   "The reflex pathway described ends in a cough centre in the medulla oblongata rather than in the cortex."],
  ["In the cervical spinal cord", "Not where the reflex is described as terminating. Impulses run through the brainstem to the medulla oblongata."],
  ["In the vagal ganglia alone", "The pathway runs through the brainstem to a cough centre in the medulla oblongata."]],
 "c": 0, "cite": D + ", Slide 55"},

{"topic": "Cough reflex", "io": IO_MOA, "slot": "mechanism",
 "q": "What activates cough receptors in the respiratory tract?",
 "opts": [
  ["Chemical and mechanical irritants", "Correct. Both kinds, which is why a cough can come from a fume, a crumb or a drip of mucus equally."],
  ["Mechanical stretch alone",
   "Mechanical stretch is only part of it; chemical irritants also trigger the reflex."],
  ["Changes in temperature alone",
   "Not the stated trigger. Cough receptors respond to chemical and mechanical irritants."],
  ["Release of histamine alone",
   "Histamine is not given as the trigger. Cough receptors respond to chemical and mechanical irritants."]],
 "c": 0, "cite": D + ", Slide 55"},

{"topic": "Cough reflex", "io": IO_MOA, "slot": "mechanism",
 "q": "What is the mechanical sequence of a cough once the reflex fires?",
 "opts": [
  ["Deep inspiration", "Correct. Closing the glottis against a contracting chest is what builds the pressure, and releasing it is what produces the velocity. Glottic closure, then contraction of chest wall, diaphragm and abdominal wall."],
  ["Forced expiration with the glottis held open throughout", "Without glottic closure no pressure builds. The sequence is deep inspiration, glottic closure, then forceful contraction."],
  ["Passive exhalation followed by a sharp inspiration", "The sequence runs the other way: deep inspiration first, then glottic closure, then active contraction of chest and abdomen."],
  ["Diaphragmatic relaxation followed by chest wall recoil", "Active contraction rather than relaxation generates the cough."]],
 "c": 0, "cite": D + ", Slide 55"},

{"topic": "Cough complications", "io": IO_SE, "slot": "adverse effect",
 "q": "Which complications of persistent coughing are described as common?",
 "opts": [
  ["Insomnia, exhaustion, pain and hoarseness",
   "Correct. Unglamorous but genuinely disabling, and together they are the reason cough is treated at all. The pain is musculoskeletal, from the effort of coughing."],
  ["Stroke, syncope and rib fracture",
   "These are described as the less common complications. The common ones are insomnia, exhaustion, musculoskeletal pain and hoarseness."],
  ["Pneumothorax, haemoptysis and chest pain",
   "Not among the complications listed. The common ones are insomnia, exhaustion, musculoskeletal pain and hoarseness."],
  ["Hearing loss, tinnitus and vertigo",
   "Not among the complications listed; insomnia, exhaustion, musculoskeletal pain and hoarseness are the common ones."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": "Cough complications", "io": IO_SE, "slot": "adverse effect",
 "q": "Which are named as the less common complications of coughing?",
 "opts": [
  ["Dysrhythmias, syncope, stroke and rib fracture", "Correct. Rare, but they establish that a cough can do structural and vascular harm, not merely wear a patient down."],
  ["Hoarseness, insomnia and exhaustion",
   "These are among the common complications. The less common are dysrhythmias, syncope, stroke and rib fracture."],
  ["Bronchospasm, wheeze and breathlessness together",
   "Not among the complications listed. The less common ones are dysrhythmias, syncope, stroke and rib fracture."],
  ["Nosebleed and nasal congestion",
   "Not among the complications listed; the less common ones are dysrhythmias, syncope, stroke and rib fracture."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": "Cough treatment goals", "io": IO_IND, "slot": "drug choice",
 "q": "What are the stated goals of treating a cough?",
 "opts": [
  ["Fewer, milder episodes and no complications",
   "Correct. Note that abolishing the cough is not the goal, which matters because a productive cough is doing a job."],
  ["To eliminate the cough completely",
   "Complete abolition is not the stated goal, and a productive cough is doing a job worth leaving alone."],
  ["To treat the underlying infection instead",
   "The goals given are about the cough itself: fewer and less severe episodes, and prevention of complications."],
  ["To prevent transmission to other people",
   "Not among the stated goals, which are reducing the number and severity of episodes and preventing complications."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": "Benzonatate", "io": IO_MOA, "slot": "mechanism",
 "q": "How does benzonatate suppress cough?",
 "opts": [
  ["It anaesthetises stretch receptors in the lungs", "Correct. It works at the start of the reflex rather than in the brain, which is the whole contrast with dextromethorphan."],
  ["It suppresses the medullary cough centre", "That is dextromethorphan's mechanism. Benzonatate anaesthetises stretch receptors in the lungs instead."],
  ["It thins mucus so there is less to clear", "That is an expectorant's action. Benzonatate numbs the receptors where the cough reflex begins."],
  ["It blocks histamine receptors in the airway", "Not its mechanism. Benzonatate anaesthetises the stretch receptors in the lungs that start the cough reflex."]],
 "c": 0, "cite": D + ", Slide 57"},

{"topic": "Benzonatate", "io": IO_IND, "slot": "drug choice",
 "q": "What kind of cough is benzonatate indicated for?",
 "opts": [
  ["A non-productive cough", "Correct. Suppressing a cough that is clearing something would be working against the patient."],
  ["A productive cough with thick sputum", "That calls for an expectorant rather than a suppressant; benzonatate is indicated for a non-productive cough."],
  ["Cough from bacterial pneumonia", "Not the stated indication, which is symptomatic relief of a non-productive cough."],
  ["Any cough regardless of character", "The indication is specifically a non-productive cough, since suppressing a productive one works against the patient."]],
 "c": 0, "cite": D + ", Slide 57"},

{"topic": "Benzonatate", "io": IO_EDU, "slot": "education",
 "q": "Why must a benzonatate capsule be swallowed whole?",
 "opts": [
  ["It releases local anaesthetic into the mouth",
   "Correct. It numbs whatever it touches, so releasing it in the mouth numbs the airway a patient needs to protect. And into the throat, which is the airway the patient needs to protect."],
  ["Chewing destroys the active drug before it works",
   "The problem is where the drug acts rather than loss of activity: chewing releases local anaesthetic into the mouth and throat."],
  ["Chewing causes irritation of the stomach lining",
   "Gastric irritation is not the stated reason. Chewing releases anaesthetic where it will numb the airway."],
  ["Chewing gives the medicine a bitter taste",
   "The concern is anaesthesia rather than taste: released in the mouth, it numbs whatever it touches."]],
 "c": 0, "cite": D + ", Slide 57"},

{"topic": "Benzonatate", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which allergy history is a contraindication to benzonatate?",
 "opts": [
  ["Allergy to tetracaine or related anaesthetics", "Correct. Benzonatate is chemically related to the ester local anaesthetics, so a reaction to one predicts a reaction to the other."],
  ["Allergy to penicillin or a cephalosporin",
   "Unrelated to benzonatate. The relevant allergy is to tetracaine and related ester anaesthetics."],
  ["Allergy to aspirin or other salicylates",
   "Unrelated to benzonatate, which is chemically related to the ester local anaesthetics such as tetracaine."],
  ["Allergy to iodine or contrast media",
   "Unrelated to benzonatate. Allergy to tetracaine or a related anaesthetic is the contraindication."]],
 "c": 0, "cite": D + ", Slide 57"},

{"topic": "Dextromethorphan", "io": IO_MOA, "slot": "mechanism",
 "q": "How does dextromethorphan suppress cough?",
 "opts": [
  ["It suppresses the medullary cough centre",
   "Correct. It is related to codeine and acts centrally, which is the origin of both its confusion as a side effect and its misuse. It does so through sigma receptor activation, and it is related to codeine."],
  ["It anaesthetises airway stretch receptors", "That is benzonatate's mechanism. Dextromethorphan suppresses the medullary cough centre through sigma receptors."],
  ["It constricts bronchial vessels", "Not its mechanism. Dextromethorphan acts centrally, suppressing the cough centre in the medulla."],
  ["It breaks disulfide bonds in mucus", "That is N-acetylcysteine's mechanism. Dextromethorphan suppresses the medullary cough centre."]],
 "c": 0, "cite": D + ", Slide 58"},

{"topic": "Dextromethorphan", "io": IO_SE, "slot": "adverse effect",
 "q": "What adverse effects are described with dextromethorphan?",
 "opts": [
  ["Confusion, excitement and agitation", "Correct. All central, which follows from where it acts and separates it cleanly from benzonatate."],
  ["Gastric ulceration and bleeding", "These belong to the non-steroidal anti-inflammatory drugs. Dextromethorphan causes confusion, excitement and agitation."],
  ["Nosebleed and septal perforation", "These belong to nasal sprays. Dextromethorphan's effects are central: confusion, excitement and agitation."],
  ["Tachycardia and hypertension", "These belong to the decongestants. Dextromethorphan acts centrally and causes confusion, excitement and agitation."]],
 "c": 0, "cite": D + ", Slide 58"},

{"topic": "Dextromethorphan", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which patient must not be given dextromethorphan?",
 "opts": [
  ["One taking a monoamine oxidase inhibitor",
   "Correct. The two-week tail is the part that catches people out, because the patient has already stopped the drug. The restriction extends for two weeks after stopping one, which is the part most easily missed."],
  ["One taking an oral antihistamine",
   "Not a contraindication. The contraindication is a monoamine oxidase inhibitor, currently or within the past two weeks."],
  ["One with treated hypertension",
   "Not the stated contraindication, which is current or recent use of a monoamine oxidase inhibitor."],
  ["One with a productive, chesty cough",
   "That is a reason to question the choice rather than a contraindication."]],
 "c": 0, "cite": D + ", Slide 58"},

{"topic": "Dextromethorphan", "io": IO_INTERACT, "slot": "mechanism",
 "q": "What risk arises when dextromethorphan is combined with other serotonergic drugs?",
 "opts": [
  ["Serotonin syndrome", "Correct. An over-the-counter cough medicine can supply the second serotonergic drug, which is exactly why it is worth asking about."],
  ["Neuroleptic malignant syndrome", "Not the described risk. Combining dextromethorphan with other serotonergic drugs risks serotonin syndrome."],
  ["Hypertensive crisis alone", "Serotonin syndrome is the described risk when dextromethorphan meets other pro-serotonergic drugs."],
  ["Prolonged bleeding time", "Not the described risk; the concern with other serotonergic drugs is serotonin syndrome."]],
 "c": 0, "cite": D + ", Slide 58"},

{"topic": "Guaifenesin", "io": IO_MOA, "slot": "mechanism",
 "q": "What does guaifenesin do?",
 "opts": [
  ["Loosens mucus and reduces its viscosity", "Correct. It makes secretions easier to clear rather than stopping the cough, so it works with the cough rather than against it."],
  ["Suppresses the cough reflex centrally", "That is an antitussive action. Guaifenesin loosens mucus and reduces its viscosity instead."],
  ["Constricts nasal vessels", "That is a decongestant action. Guaifenesin works on the mucus rather than on the mucosa."],
  ["Blocks histamine receptors", "That is an antihistamine action. Guaifenesin is a mucolytic and expectorant."]],
 "c": 0, "cite": D + ", Slide 59"},

{"topic": "Guaifenesin", "io": IO_SE, "slot": "adverse effect",
 "q": "What adverse effects are described with guaifenesin?",
 "opts": [
  ["Nausea and vomiting", "Correct. A short list, which is part of why it is available without prescription."],
  ["Confusion and agitation", "These belong to dextromethorphan, which acts centrally. Guaifenesin causes nausea and vomiting."],
  ["Hypertension and tachycardia", "These belong to the decongestants. Guaifenesin's described adverse effects are nausea and vomiting."],
  ["Hepatic failure", "Not described with guaifenesin, whose adverse effects are limited to nausea and vomiting."]],
 "c": 0, "cite": D + ", Slide 59"},

{"topic": "Guaifenesin", "io": IO_EDU, "slot": "education",
 "q": "What is a patient starting guaifenesin told to expect?",
 "opts": [
  ["More drainage", "Correct. Warning the patient that drainage increases stops them reading the drug working as the drug failing. To drink plenty of fluid."],
  ["Less drainage within a day", "Increased drainage is what is expected, and saying so stops the patient reading the drug working as it failing."],
  ["A bitter taste", "That belongs to the nasal sprays. A patient on guaifenesin is told to expect more drainage and to drink fluids."],
  ["Drowsiness", "Not an expected effect of guaifenesin. The patient is told to expect increased drainage and to drink plenty of fluid."]],
 "c": 0, "cite": D + ", Slide 60"},

{"topic": "Guaifenesin", "io": IO_EDU, "slot": "education",
 "q": "When is a patient on guaifenesin told to follow up?",
 "opts": [
  ["If symptoms persist beyond about a week or get worse", "Correct. A cough that outlasts the self-treatment window needs a cause found rather than more expectorant."],
  ["Only if a fever develops", "Fever is not the stated trigger. Follow-up is advised if symptoms persist beyond about a week or worsen."],
  ["After a single day without improvement", "The window is longer than that: follow up if symptoms last beyond about a week or get worse."],
  ["Never -- it is available without prescription", "Over-the-counter availability does not remove the follow-up advice."]],
 "c": 0, "cite": D + ", Slide 60"},

{"topic": "Dornase alfa", "io": IO_MOA, "slot": "mechanism",
 "q": "How does dornase alfa reduce sputum viscosity?",
 "opts": [
  ["It cleaves DNA released from degenerating neutrophils", "Correct. The thickness comes from the DNA of dead white cells, so an enzyme that cuts DNA is a precisely targeted answer to it."],
  ["It splits disulfide bonds between mucoproteins", "That is N-acetylcysteine's mechanism. Dornase alfa cleaves DNA released from degenerating neutrophils."],
  ["It draws water onto the airway surface", "That is how hypertonic saline works. Dornase alfa is an enzyme that cuts neutrophil DNA in the sputum."],
  ["It suppresses neutrophil recruitment to the lung", "It acts on what the neutrophils leave behind rather than on their recruitment."]],
 "c": 0, "cite": D + ", Slide 61"},

{"topic": "Dornase alfa", "io": IO_IND, "slot": "drug choice",
 "q": "In which patients does dornase alfa give the greatest benefit?",
 "opts": [
  ["Those with mild to moderate disease", "Correct. It still works in severe disease, but the gain in lung function is smaller, which is a point about expectation rather than eligibility."],
  ["Those with severe disease only", "Severe disease benefits less in terms of lung function; the greatest gain is in mild to moderate disease."],
  ["Those with no symptoms", "Not the described use. Dornase alfa is used in mild to moderate disease, where the gain is greatest."],
  ["It benefits all stages equally", "The degree of improvement differs by severity: severe disease still responds, but with less gain in lung function."]],
 "c": 0, "cite": D + ", Slide 61"},

{"topic": "Dornase alfa", "io": IO_IND, "slot": "drug choice",
 "q": "Besides improving lung function, what else does dornase alfa achieve?",
 "opts": [
  ["It reduces the number of exacerbations", "Correct. Fewer episodes matters as much as a better spirometry number, and arguably more to the patient."],
  ["It eradicates chronic airway infection", "Not a described effect. Alongside improving lung function it reduces the number of exacerbations."],
  ["It replaces the need for airway clearance physiotherapy", "Not claimed. What is claimed is better lung function and fewer exacerbations."],
  ["It reverses established lung damage", "Not claimed. Dornase alfa improves lung function and reduces exacerbations rather than reversing damage."]],
 "c": 0, "cite": D + ", Slide 61"},

{"topic": "Hypertonic saline", "io": IO_MOA, "slot": "mechanism",
 "q": "What does inhaled hypertonic saline improve?",
 "opts": [
  ["Airway surface hydration", "Correct. It works by changing the conditions the cilia operate in rather than by acting on the mucus chemically. Mucus transport and mucociliary clearance."],
  ["Bronchial smooth muscle tone", "Not the described action. Hypertonic saline improves airway surface hydration, mucus transport and mucociliary clearance."],
  ["Neutrophil DNA breakdown", "That is dornase alfa's mechanism. Hypertonic saline works by hydrating the airway surface."],
  ["Cough receptor sensitivity", "Not the described action. Hypertonic saline improves hydration of the airway surface and mucociliary clearance."]],
 "c": 0, "cite": D + ", Slide 62"},

{"topic": "N-acetylcysteine", "io": IO_MOA, "slot": "mechanism",
 "q": "How does inhaled N-acetylcysteine reduce mucus viscosity?",
 "opts": [
  ["It splits the disulfide bonds linking mucoproteins", "Correct. It breaks the chemical cross-links that make mucus stiff, which is a different target again from the DNA that dornase alfa cuts."],
  ["It cleaves DNA from degenerating neutrophils", "That is dornase alfa's mechanism. N-acetylcysteine splits the disulfide bonds linking mucoproteins."],
  ["It draws water onto the airway surface", "That is hypertonic saline's mechanism. N-acetylcysteine breaks the disulfide cross-links that stiffen mucus."],
  ["It inhibits mucus secretion at the gland", "It acts on mucus already produced, splitting the disulfide bonds that link mucoproteins together."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "N-acetylcysteine", "io": IO_IND, "slot": "drug choice",
 "q": "What is N-acetylcysteine traditionally used for, apart from its mucolytic action?",
 "opts": [
  ["Acetaminophen poisoning", "Correct. The same drug turns up in two entirely unrelated places -- as an antidote in poisoning and as a mucolytic in the airway -- which is worth noticing rather than being surprised by."],
  ["Aspirin poisoning", "Not its antidotal use. N-acetylcysteine is traditionally the antidote for acetaminophen poisoning."],
  ["Opioid overdose", "Not its antidotal use; N-acetylcysteine is the traditional antidote in acetaminophen poisoning."],
  ["Organophosphate poisoning", "Not its antidotal use. Its established role outside the airway is in acetaminophen poisoning."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "N-acetylcysteine", "io": IO_SE, "slot": "adverse effect",
 "q": "What adverse effects are described with inhaled N-acetylcysteine?",
 "opts": [
  ["A rotten egg smell, nausea and vomiting", "Correct. The smell comes from its sulfur content and is a real reason patients refuse it; the bronchospasm is the one that matters clinically. Bronchospasm."],
  ["Sedation and confusion", "These belong to the centrally acting antitussive. Inhaled N-acetylcysteine smells of sulfur and can cause bronchospasm."],
  ["Hypertension and tachycardia", "These belong to the decongestants. N-acetylcysteine causes a rotten egg smell, nausea, vomiting and bronchospasm."],
  ["Nosebleed and septal perforation", "These belong to nasal sprays. Inhaled N-acetylcysteine causes a sulfurous smell, nausea, vomiting and bronchospasm."]],
 "c": 0, "cite": D + ", Slide 63"},

{"topic": "Antitussive comparison", "io": IO_IND, "slot": "drug choice",
 "q": "A patient with a dry cough is taking an antidepressant. Which antitussive is the safer choice, and why?",
 "opts": [
  ["Benzonatate, because dextromethorphan risks serotonin syndrome", "Correct. Both would suppress the cough; the interaction is what decides between them."],
  ["Dextromethorphan, because it acts centrally and works faster", "Central action is exactly what makes it the riskier choice here."],
  ["Either, since neither interacts with antidepressants", "Dextromethorphan carries a serotonergic interaction, so in this patient benzonatate is the safer of the two."],
  ["Neither -- an expectorant should be used instead", "An expectorant treats a productive cough rather than a dry one; benzonatate is the appropriate choice here."]],
 "c": 0, "cite": D + ", Slide 58"},
]
