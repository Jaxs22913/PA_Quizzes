# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- ENT, topic 2: analgesics and anti-inflammatories.

Scope as in pharm_ent_pool_anti.py: indications and agent-specific adverse
effects ARE asked; dosing is not. The dose-effect table on the aspirin slide is
a dosing table, so the grams are left alone; what is asked instead is the ladder
it encodes -- that the same drug is an antiplatelet, an analgesic
and an anti-inflammatory at rising exposure, and that tinnitus is the sign the
patient has climbed it.

The pairing that earns its place here is aspirin against ibuprofen: irreversible
against reversible at cyclooxygenase, which is why one is a once-and-done
antiplatelet and the other is not, and why the advice about combining them
exists at all.
"""

D = "ENT Jax Pharmacology.pptx"
IO_CLASS = "Identify ENT drug classes and commonly prescribed ENT drugs"
IO_MOA = "Describe the mechanism of action of ENT drugs"
IO_IND = "Identify indications for commonly used ENT drugs"
IO_ADME = "Describe absorption, distribution, metabolism, and excretion of ENT drugs"
IO_SE = "Summarize side effects and toxic manifestations of ENT drugs"
IO_CONTRA = "Identify contraindications for ENT drugs"
IO_EDU = "Outline appropriate patient education for ENT drugs"
IO_INTERACT = "Discuss potential drug-drug, drug-food, and drug-herb interactions with ENT drugs"

QUESTIONS = [

{"topic": "Salicylates", "io": IO_MOA, "slot": "mechanism",
 "q": "How does aspirin act on cyclooxygenase, and what follows from it?",
 "opts": [
  ["Irreversibly and non-competitively, so the platelet never recovers", "Correct. A platelet has no nucleus and cannot make fresh enzyme, so one exposure disables it for its lifetime. Everything distinctive about aspirin as an antiplatelet follows from that."],
  ["Reversibly, so the effect ends as the drug is cleared", "That is ibuprofen. Aspirin binds irreversibly, so a platelet exposed to it never recovers the enzyme."],
  ["Selectively at cyclooxygenase-2 only", "Aspirin is non-selective between the two isoforms, and hitting COX-1 as well is where its gastric and bleeding effects come from."],
  ["Indirectly, by reducing prostaglandin release from storage", "Prostaglandins are made on demand rather than stored, and aspirin acts on the enzyme."]],
 "c": 0, "cite": D + ", Slide 15"},

{"topic": "Salicylates", "io": IO_MOA, "slot": "mechanism",
 "q": "Is aspirin selective for one cyclooxygenase isoform?",
 "opts": [
  ["No, it is non-selective for COX-1 and COX-2", "Correct. Hitting COX-1 as well is where the gastric and bleeding problems come from."],
  ["Yes, it is COX-2 selective", "COX-2 selectivity belongs to a different group of agents. Aspirin inhibits both isoforms without preference."],
  ["Yes, it is COX-1 selective", "It inhibits both isoforms rather than only one, which is why its effects span platelets, stomach and inflammation."],
  ["It does not act on cyclooxygenase at all", "Cyclooxygenase is exactly where it acts, and it does so irreversibly at both isoforms."]],
 "c": 0, "cite": D + ", Slide 15"},

{"topic": "Salicylates", "io": IO_ADME, "slot": "mechanism",
 "q": "How is aspirin handled by the body?",
 "opts": [
  ["Absorbed orally", "Correct. Liver then kidney, which is why disease in either changes what a given exposure does. Conjugated in the liver, excreted by the kidney."],
  ["Absorbed orally and excreted unchanged in bile", "Biliary excretion of unchanged drug is not the route described."],
  ["Absorbed through the skin and metabolized in plasma", "Oral absorption is what is described, followed by hepatic conjugation and renal excretion."],
  ["Absorbed orally and eliminated entirely by the lungs", "The lungs are not an elimination route for aspirin. It is conjugated in the liver and excreted by the kidney."]],
 "c": 0, "cite": D + ", Slide 15"},

{"topic": "Salicylates", "io": IO_SE, "slot": "adverse effect",
 "q": "A patient taking aspirin regularly develops ringing in the ears. What does that suggest?",
 "opts": [
  ["Exposure has reached the anti-inflammatory range",
   "Correct. Tinnitus is the audible marker that the patient has climbed the ladder from analgesia into the anti-inflammatory range, which makes it useful rather than incidental."],
  ["An unrelated sensorineural hearing loss on that side",
   "Tinnitus is a recognized salicylate effect and should not be dismissed as coincidence."],
  ["An allergic reaction to aspirin", "Hypersensitivity presents differently; tinnitus tracks exposure."],
  ["The dose is too low to be effective", "Tinnitus indicates more exposure rather than less; it appears once salicylate reaches the anti-inflammatory range."]],
 "c": 0, "cite": D + ", Slide 16"},

{"topic": "Salicylates", "io": IO_MOA, "slot": "mechanism",
 "q": "Aspirin produces different effects as exposure rises. In what order do they appear?",
 "opts": [
  ["Antiplatelet, then analgesic and antipyretic, then anti-inflammatory", "Correct. One drug with three jobs stacked by exposure, which is why 'taking aspirin' means very different things in different patients."],
  ["Anti-inflammatory, then analgesic, then antiplatelet", "The order runs the other way: antiplatelet at the lowest exposure, then analgesic and antipyretic, then anti-inflammatory."],
  ["Analgesic first, then antiplatelet, then anti-inflammatory", "The antiplatelet effect appears at the lowest exposure of the three."],
  ["All three appear together at any exposure", "They appear in sequence as exposure rises, which is why the same drug means different things in different patients."]],
 "c": 0, "cite": D + ", Slide 16"},

{"topic": "Salicylates", "io": IO_CONTRA, "slot": "contraindication",
 "q": "A child has a fever during chickenpox. Why must aspirin be avoided?",
 "opts": [
  ["It raises the risk of Reye's syndrome", "Correct. A viral illness plus aspirin in a child is the exact combination that produces it, which is why the rule is about the setting rather than the drug alone."],
  ["It is ineffective against viral fever", "Efficacy is not the issue; the risk is. Aspirin given to a child with a viral illness is associated with Reye's syndrome."],
  ["It causes irreversible hearing loss in children", "Tinnitus is exposure-related and is not the reason for this restriction."],
  ["It interacts with the varicella vaccine", "The concern is the illness rather than the vaccine: aspirin during a viral illness in a child risks Reye's syndrome."]],
 "c": 0, "cite": D + ", Slide 17"},

{"topic": "Salicylates", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which situations are listed as contraindications to aspirin?",
 "opts": [
  ["Bleeding disorders, pregnancy", "Correct. Three unrelated mechanisms -- bleeding risk, pregnancy, and Reye's -- which is why the list has to be remembered rather than derived. Children with fever from viral illness."],
  ["Asthma, renal impairment and peptic ulcer alone", "Those belong to the ibuprofen list. Aspirin's are bleeding disorders, pregnancy, and children with fever from viral illness."],
  ["Any patient over sixty-five", "Age alone is not given as a contraindication. The age-related restriction concerns children with viral illness, because of Reye's syndrome."],
  ["Concurrent acetaminophen use", "Acetaminophen is not listed as a contraindication to aspirin."]],
 "c": 0, "cite": D + ", Slide 17"},

{"topic": "Salicylates", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Aspirin is contraindicated in pregnancy, yet one exception is noted. What is it?",
 "opts": [
  ["Very low exposure may benefit pre-eclampsia",
   "Correct. The exception is narrow and specific, and it is the reason the contraindication is stated as a rule with a footnote rather than as an absolute. That is, the hypertensive disorders of pregnancy."],
  ["It is safe throughout the third trimester", "No such blanket allowance is given. The only exception noted is very low exposure in hypertensive disorders such as pre-eclampsia."],
  ["It may be used to treat fever during pregnancy",
   "Fever in pregnancy is not the exception described. The exception concerns hypertensive disorders such as pre-eclampsia."],
  ["It may be used if the patient is also on an anticoagulant", "That combination increases bleeding risk rather than making aspirin acceptable."]],
 "c": 0, "cite": D + ", Slide 17"},

{"topic": "Reye's syndrome", "io": IO_SE, "slot": "diagnosis",
 "q": "What is Reye's syndrome also called, and what does the name describe?",
 "opts": [
  ["Fatty liver encephalopathy", "Correct. The alternative name is a compact description of the illness: liver and brain together. Naming the two organs involved."],
  ["Salicylate hypersensitivity syndrome", "It is not a hypersensitivity reaction. Reye's syndrome is also called fatty liver encephalopathy, naming the two organs involved."],
  ["Acute hepatic porphyria", "A different condition entirely. Reye's syndrome is also known as fatty liver encephalopathy."],
  ["Viral hemorrhagic encephalitis", "Neither the name nor the mechanism. Reye's syndrome is called fatty liver encephalopathy, and involves mitochondrial dysfunction."]],
 "c": 0, "cite": D + ", Slide 18"},

{"topic": "Reye's syndrome", "io": IO_SE, "slot": "diagnosis",
 "q": "Which illnesses typically precede Reye's syndrome?",
 "opts": [
  ["An upper respiratory infection", "Correct. All viral, which is why the aspirin restriction in children is framed around fever from viral illness specifically. Influenza or chickenpox."],
  ["Bacterial otitis media or sinusitis", "The preceding illnesses described are viral: an upper respiratory infection, influenza or chickenpox."],
  ["Streptococcal pharyngitis", "Not among the illnesses named. Reye's syndrome follows an upper respiratory infection, influenza or chickenpox."],
  ["Gastroenteritis from food poisoning", "Not among the illnesses named; the preceding illnesses are viral ones such as influenza and chickenpox."]],
 "c": 0, "cite": D + ", Slide 18"},

{"topic": "Reye's syndrome", "io": IO_SE, "slot": "diagnosis",
 "q": "Which features characterize Reye's syndrome?",
 "opts": [
  ["Vomiting, neurological damage, liver injury and low glucose",
   "Correct. The hypoglycemia is easy to forget alongside the liver and brain findings, and it is treatable. The neurological damage is progressive, and the glucose is genuinely low rather than borderline."],
  ["Fever, a rash and migratory joint pain",
   "Not the described features. Reye's syndrome brings vomiting, progressive central nervous system damage, hepatic injury and low glucose."],
  ["Jaundice with painless distension of the abdomen",
   "Not how it is described. The picture is vomiting, neurological deterioration, liver injury and hypoglycemia."],
  ["Isolated hepatic failure without neurological signs", "The central nervous system involvement is central to it; the alternative name pairs the brain with the liver for that reason."]],
 "c": 0, "cite": D + ", Slide 18"},

{"topic": "Reye's syndrome", "io": IO_SE, "slot": "mechanism",
 "q": "What underlying cellular abnormality is described in Reye's syndrome?",
 "opts": [
  ["Mitochondrial dysfunction in brain", "Correct. One failing organelle across several tissues explains why an illness of the liver and brain also involves muscle. Liver and muscle."],
  ["Autoimmune destruction of hepatocytes", "Not the described mechanism. Reye's syndrome involves mitochondrial dysfunction in brain, liver and muscle."],
  ["Direct viral invasion of the brain", "The syndrome follows the viral illness rather than being the virus itself."],
  ["Accumulation of unconjugated bilirubin", "Not the described mechanism; the abnormality described is mitochondrial dysfunction across brain, liver and muscle."]],
 "c": 0, "cite": D + ", Slide 18"},

{"topic": "Reye's syndrome", "io": IO_SE, "slot": "diagnosis",
 "q": "A child in the earliest stage of Reye's syndrome would show which of these?",
 "opts": [
  ["A rash on the hands and feet", "Correct. Stage one looks nonspecific, which is exactly the problem -- it is the stage at which the illness is most treatable and least recognizable. Vomiting, high fever and lethargy."],
  ["Coma with fixed, dilated pupils", "That is a late stage. The first stage is a rash on hands and feet with vomiting, high fever and lethargy."],
  ["Seizures and multiple organ failure", "That is the final stage. The first is a nonspecific febrile illness with vomiting and lethargy."],
  ["Encephalitis with hyperventilation", "That is the second stage rather than the first, which is a rash, vomiting, high fever and lethargy."]],
 "c": 0, "cite": D + ", Slide 19"},

{"topic": "Reye's syndrome", "io": IO_SE, "slot": "diagnosis",
 "q": "Which finding marks the most advanced stage of Reye's syndrome?",
 "opts": [
  ["Seizures and multiple organ failure",
   "Correct. The staging runs from a nonspecific febrile illness to multi-organ failure, which is why the early stage matters so much."],
  ["Cerebral edema with coma", "That is an intermediate stage. The most advanced stage brings seizures, multiple organ failure and death."],
  ["Fatty liver with encephalitis", "That appears earlier in the sequence. The final stage is seizures, multiple organ failure and death."],
  ["Vomiting with lethargy", "That is the first stage. The most advanced brings seizures, multiple organ failure and death."]],
 "c": 0, "cite": D + ", Slide 19"},

{"topic": "Reye's syndrome", "io": IO_SE, "slot": "diagnosis",
 "q": "Who is affected by Reye's syndrome, and how dangerous is it?",
 "opts": [
  ["Children, with mortality around half", "Correct. The severity is what justifies a blanket restriction on a cheap and otherwise useful drug."],
  ["Adults over sixty-five, with mortality around a tenth", "It is a disease of children rather than older adults, and the mortality described is far higher than a tenth."],
  ["Children, but it is almost never fatal", "Mortality is substantial, which is the reason for the restriction."],
  ["Any age, with mortality under one percent", "Neither the age group nor the mortality matches: it affects children, and around half of those affected die."]],
 "c": 0, "cite": D + ", Slide 18"},

{"topic": "Aspirin education", "io": IO_EDU, "slot": "education",
 "q": "A patient is started on aspirin for fever. What should they be told about other medicines?",
 "opts": [
  ["Do not take other anti-inflammatory drugs alongside it",
   "Correct. They share a mechanism, so combining them adds the harms without adding the benefit. That means the non-steroidal anti-inflammatory drugs specifically."],
  ["Take an antacid alongside every dose",
   "Not among the instructions given. The medicine warning is to avoid other non-steroidal anti-inflammatory drugs."],
  ["Avoid acetaminophen entirely while taking it",
   "Acetaminophen is not the drug the patient is warned off; the warning concerns other non-steroidal anti-inflammatory drugs."],
  ["Take it only on a completely empty stomach",
   "Not among the instructions given, and it would worsen the gastric effects rather than help them."]],
 "c": 0, "cite": D + ", Slide 20"},

{"topic": "Aspirin education", "io": IO_EDU, "slot": "education",
 "q": "Why is a patient on aspirin told not to take it with an anticoagulant?",
 "opts": [
  ["Aspirin inhibits platelet function", "Correct. Two different parts of hemostasis are disabled at once, which is more than the sum of either alone. Adding a second bleeding mechanism."],
  ["The anticoagulant blocks aspirin's absorption", "Absorption is not the problem. Aspirin inhibits platelet function, which adds a second bleeding mechanism to the anticoagulant."],
  ["Aspirin makes the anticoagulant ineffective", "The concern is additive bleeding risk rather than loss of effect: two different parts of hemostasis are disabled at once."],
  ["The combination causes Reye's syndrome", "Reye's relates to children with viral illness rather than to anticoagulants."]],
 "c": 0, "cite": D + ", Slide 20"},

{"topic": "Aspirin education", "io": IO_EDU, "slot": "education",
 "q": "A patient takes aspirin for fever. When are they told to come back straight away?",
 "opts": [
  ["If the fever does not come down",
   "Correct. The instruction is about the fever failing to respond, which is a different signal from the fever simply continuing. That is, if it fails to respond to the medicine rather than merely persisting."],
  ["If they feel drowsy after the first dose", "Drowsiness is not the flag given, and it is not an aspirin effect. The trigger is a fever that fails to come down."],
  ["Only once a full week has passed",
   "The instruction is more urgent than that: a fever that does not respond to the medicine warrants immediate follow-up."],
  ["If the fever returns at any point", "A returning fever is not the stated trigger for immediate follow-up."]],
 "c": 0, "cite": D + ", Slide 20"},

{"topic": "Aspirin education", "io": IO_EDU, "slot": "education",
 "q": "What is a patient on aspirin told about pain that does not settle?",
 "opts": [
  ["To follow up if it worsens or persists",
   "Correct. There is a time limit on treating yourself, and it exists so that a persistent cause gets looked at rather than masked. The limit given is about ten days."],
  ["To double the amount taken", "Increasing exposure without review is not advised, and it moves the patient toward the range where tinnitus appears."],
  ["To switch to an anticoagulant", "Anticoagulants are not an analgesic alternative, and combining one with aspirin is specifically warned against."],
  ["To continue taking it indefinitely if it helps",
   "Indefinite self-treatment is what the instruction is designed to prevent."]],
 "c": 0, "cite": D + ", Slide 20"},

{"topic": "Ibuprofen", "io": IO_MOA, "slot": "mechanism",
 "q": "How does ibuprofen differ from aspirin at cyclooxygenase?",
 "opts": [
  ["It inhibits reversibly rather than irreversibly", "Correct. The effect lifts as the drug clears, which is why ibuprofen is not used as an antiplatelet the way aspirin is."],
  ["It inhibits COX-2 only", "Ibuprofen inhibits both isoforms. What separates it from aspirin is that it does so reversibly."],
  ["It does not inhibit cyclooxygenase", "It does inhibit cyclooxygenase; the difference from aspirin is that its binding is reversible."],
  ["It inhibits irreversibly, but only COX-1", "Irreversible binding is aspirin's property, and neither drug is confined to COX-1."]],
 "c": 0, "cite": D + ", Slide 21"},

{"topic": "Ibuprofen", "io": IO_CLASS, "slot": "drug choice",
 "q": "What three actions does ibuprofen have?",
 "opts": [
  ["Anti-inflammatory, analgesic and antipyretic", "Correct. All three at ordinary use, unlike aspirin where they separate out by exposure."],
  ["Analgesic and antipyretic only", "It is anti-inflammatory as well, which is what makes it a non-steroidal anti-inflammatory drug."],
  ["Anti-inflammatory and antiplatelet only", "Pain and fever are both within its range, and its antiplatelet effect is not a listed action."],
  ["Antipyretic only", "It does considerably more than reduce fever: ibuprofen is anti-inflammatory and analgesic as well as antipyretic."]],
 "c": 0, "cite": D + ", Slide 21"},

{"topic": "Ibuprofen", "io": IO_SE, "slot": "adverse effect",
 "q": "Which organ systems carry ibuprofen's main adverse effects?",
 "opts": [
  ["The gastrointestinal tract and the kidney",
   "Correct. Ulceration and bleeding at one end, falling clearance and edema at the other -- and both come from the same prostaglandin blockade. Fluid retention and edema come with the renal effects."],
  ["The liver and the bone marrow", "Not the systems described for ibuprofen, whose main harms fall on the gastrointestinal tract and the kidney."],
  ["The lungs and the thyroid", "Not the systems described. Ibuprofen's adverse effects center on the gut and the kidney, with fluid retention."],
  ["The skin and the joints", "Not the systems described; the gastrointestinal tract and the kidney carry ibuprofen's main adverse effects."]],
 "c": 0, "cite": D + ", Slide 21"},

{"topic": "Ibuprofen", "io": IO_INTERACT, "slot": "mechanism",
 "q": "A patient on lithium is started on ibuprofen. What is the concern?",
 "opts": [
  ["Ibuprofen reduces lithium excretion, so levels rise", "Correct. Lithium has little margin between useful and toxic, so anything that slows its removal matters quickly."],
  ["Ibuprofen blocks lithium absorption, so levels fall", "The interaction raises levels rather than lowering them: ibuprofen reduces lithium excretion, and lithium has little safety margin."],
  ["The two combine to cause serotonin syndrome", "That concern belongs to dextromethorphan with a monoamine oxidase inhibitor."],
  ["Lithium increases the risk of gastric ulceration from ibuprofen", "The described interaction runs the other way, through lithium handling."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Ibuprofen", "io": IO_INTERACT, "slot": "mechanism",
 "q": "Why is ibuprofen a problem for a patient taking methotrexate?",
 "opts": [
  ["It reduces methotrexate secretion", "Correct. Same mechanism as the lithium interaction -- reduced renal clearance of a drug that does harm when it accumulates. Producing toxic levels."],
  ["It displaces methotrexate from its receptor", "Displacement at a receptor is not the described mechanism. Ibuprofen reduces methotrexate secretion, so it accumulates."],
  ["It prevents methotrexate from being absorbed", "Absorption is not the step affected. Reduced secretion is what allows methotrexate to reach toxic levels."],
  ["It inactivates methotrexate in the liver", "The interaction concerns secretion rather than hepatic inactivation."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Ibuprofen", "io": IO_INTERACT, "slot": "next step",
 "q": "A patient on a diuretic and an ACE inhibitor starts taking ibuprofen regularly. What should be watched?",
 "opts": [
  ["Renal function", "Correct. Two interactions at once: the kidney is at risk with the diuretic, and the ACE inhibitor works less well. The blood pressure response to the ACE inhibitor."],
  ["Liver enzymes and bilirubin", "The liver is not the organ at risk in this combination. The kidney is, and the ACE inhibitor also works less well."],
  ["Thyroid function", "Not affected by this combination. Renal function and the blood pressure response are what need watching."],
  ["Serum potassium only", "Potassium is not the described concern here; the risks are renal impairment and a reduced antihypertensive effect."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Ibuprofen", "io": IO_INTERACT, "slot": "adverse effect",
 "q": "What happens when ibuprofen is combined with an anticoagulant?",
 "opts": [
  ["Prothrombin time is prolonged", "Correct. Ibuprofen damages the mucosa and the anticoagulant stops the bleeding from being controlled, which is why the combination is worse than either alone. With a risk of serious gastrointestinal bleeding."],
  ["The anticoagulant is inactivated", "The problem is additive bleeding risk rather than loss of anticoagulation."],
  ["Absorption of both drugs is reduced", "Absorption is not the issue. The combination prolongs prothrombin time and risks serious gastrointestinal bleeding."],
  ["Clotting time shortens", "The effect runs toward bleeding rather than clotting: prothrombin time is prolonged and gastrointestinal bleeding may follow."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Ibuprofen", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which patients should avoid ibuprofen?",
 "opts": [
  ["Those with asthma it may worsen", "Correct. Asthma is the one most easily forgotten, because it is not an obvious consequence of blocking prostaglandin synthesis. Previous ulcer or perforation, or renal impairment."],
  ["Those with a history of Reye's syndrome", "Reye's relates to aspirin in children rather than to ibuprofen."],
  ["Those taking acetaminophen", "Acetaminophen is not a contraindication to ibuprofen. The contraindications are asthma, prior ulcer or perforation, and renal impairment."],
  ["Those over sixty-five years old", "Age alone is not the stated contraindication; asthma, previous ulceration and renal impairment are, along with very young infants."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Ibuprofen", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Ibuprofen is avoided below a certain age. Which group?",
 "opts": [
  ["Young infants", "Correct. There is a lower age limit below which it is not used, which distinguishes it from acetaminophen."],
  ["All children under twelve", "The restriction applies to infants rather than to all children."],
  ["All children under fifteen, because of Reye's syndrome", "That threshold belongs to aspirin and Reye's syndrome. Ibuprofen's age restriction concerns young infants instead."],
  ["Adolescents only", "Adolescents are not the restricted group; it is young infants in whom ibuprofen is avoided."]],
 "c": 0, "cite": D + ", Slide 22"},

{"topic": "Naproxen", "io": IO_CLASS, "slot": "drug choice",
 "q": "What distinguishes naproxen from ibuprofen?",
 "opts": [
  ["A longer half-life", "Correct. Same class and same problems, but a longer half-life, which matters for adherence more than for efficacy. So it is taken less often."],
  ["It is selective for COX-2", "Selectivity is not what separates it here. Naproxen differs by having a longer half-life, so it is taken less often."],
  ["It has no gastrointestinal effects", "It is a non-steroidal anti-inflammatory drug and carries the same gastrointestinal risks."],
  ["It is available only on prescription", "It is named among the over-the-counter agents. Its distinguishing feature is a longer half-life."]],
 "c": 0, "cite": D + ", Slide 23"},

{"topic": "Acetaminophen", "io": IO_MOA, "slot": "mechanism",
 "q": "What is known about how acetaminophen works?",
 "opts": [
  ["Its mechanism is not fully established", "Correct. It is worth saying plainly rather than inventing an explanation: the mechanism is not fully worked out, and the drug is used on its observed effects."],
  ["It irreversibly inhibits COX-1 in the periphery", "That is aspirin's mechanism. Acetaminophen's mechanism is not fully established."],
  ["It blocks prostaglandin receptors directly", "Receptor blockade is not the described mechanism; acetaminophen's mechanism is stated to be incompletely understood."],
  ["It acts through opioid receptors", "It is not an opioid and does not act there. Its mechanism is described as not fully elucidated."]],
 "c": 0, "cite": D + ", Slide 24"},

{"topic": "Acetaminophen", "io": IO_CLASS, "slot": "drug choice",
 "q": "How is acetaminophen classified, and what does that exclude?",
 "opts": [
  ["Analgesic and antipyretic", "Correct. That missing third action is the practical difference from the non-steroidal anti-inflammatory drugs, and it decides when it is not the right choice. But not anti-inflammatory."],
  ["Analgesic, antipyretic and anti-inflammatory", "The anti-inflammatory action is the one it does not have, and that absence is its main practical difference from the NSAIDs."],
  ["Anti-inflammatory and antiplatelet", "It has neither of these. Acetaminophen is an analgesic and an antipyretic only."],
  ["Antipyretic only", "It relieves pain as well as fever; what it does not do is reduce inflammation."]],
 "c": 0, "cite": D + ", Slide 24"},

{"topic": "Acetaminophen", "io": IO_SE, "slot": "adverse effect",
 "q": "How is acetaminophen tolerated when taken as intended?",
 "opts": [
  ["Very well, with no notable side effects",
   "Correct. Its safety within the intended range is exactly why exceeding that range is so easy to do. That holds at therapeutic exposure, which is what makes exceeding it so easy."],
  ["Poorly, with frequent gastric irritation", "Gastric irritation belongs to the non-steroidal anti-inflammatory drugs."],
  ["With common renal impairment", "Renal effects belong to the non-steroidal anti-inflammatory drugs."],
  ["With frequent sedation", "Sedation is not an acetaminophen effect. Within the intended range it is described as very well tolerated."]],
 "c": 0, "cite": D + ", Slide 24"},

{"topic": "Acetaminophen", "io": IO_INTERACT, "slot": "education",
 "q": "What should a patient who drinks alcohol regularly be told about acetaminophen?",
 "opts": [
  ["The combination risks liver damage over time",
   "Correct. Neither is dangerous on its own at ordinary use, which is what makes the combination easy to arrive at without noticing."],
  ["Alcohol prevents acetaminophen from working", "Efficacy is not the concern; hepatic injury is. Regular alcohol with acetaminophen raises the risk of liver damage over time."],
  ["The combination causes gastric ulceration", "Ulceration belongs to the non-steroidal anti-inflammatory drugs."],
  ["There is no interaction between the two drugs",
   "A chronic interaction is described, and it involves the liver."]],
 "c": 0, "cite": D + ", Slide 25"},

{"topic": "Acetaminophen", "io": IO_IND, "slot": "drug choice",
 "q": "A child has fever during influenza. Why is acetaminophen preferred over aspirin?",
 "opts": [
  ["Aspirin in a child with viral illness risks Reye's syndrome", "Correct. This is the everyday consequence of the Reye's association, and it is why acetaminophen became the default antipyretic in children."],
  ["Acetaminophen is anti-inflammatory and aspirin is not", "Acetaminophen is the one WITHOUT anti-inflammatory action. It is preferred here because aspirin risks Reye's syndrome."],
  ["Aspirin does not reduce fever", "Aspirin is an effective antipyretic; the problem is the risk in this setting."],
  ["Acetaminophen also treats the influenza itself", "It treats the fever and the discomfort rather than the infection. It is preferred because aspirin risks Reye's syndrome."]],
 "c": 0, "cite": D + ", Slide 17"},
]
