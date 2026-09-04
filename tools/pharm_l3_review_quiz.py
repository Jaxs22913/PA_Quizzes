# -*- coding: utf-8 -*-
"""Lecture 3 (autonomic nervous system) quiz, built to the exam review's guidance.

Dr. Wood gave no scope CUT for Lecture 3 -- everything he narrowed at the review
was aimed at Lecture 1. What he gave instead was a shape, and this quiz is built
to it rather than to the slide order.

  1. THE CHAIN, not the fact. "Generally knowing which receptors are associated
     with which sort of actions, and then knowing how the drugs will be
     affecting those receptors, and then what do I expect to see happen as a
     result of that." So a stem gives the drug or the receptor and asks what you
     would SEE -- never "which receptor does X bind", which stops one link early.
  2. MECHANISM GIVES YOU THE INDICATION. "What their mechanisms are will inform
     you on what they are used for." Indications are asked as consequences of
     the mechanism, not as a separate list to memorise.
  3. MORE THAN ONE ROUTE TO A GOAL. His own example: slowing a rapid heart rate
     can be a beta blocker, a muscarinic agonist or an acetylcholinesterase
     inhibitor. Three items here have several defensible mechanisms and ask
     which of the OPTIONS achieves it.
  4. PLACE THE NAMED DRUG BACK IN ITS CLASS. "Most my questions will ultimately
     come down to four individual drugs." Six items are exactly that.
  5. NO NUMBERS. "Don't know specific values." There is not a dose or a
     threshold anywhere in this bank.

FOUR options, which is the Pharmacology convention on this site -- the
five-option rule Jaxon set on 2026-08-26 is for CMS. Correct answer is authored
FIRST; the renderer rotates it across A-D.
"""
S = "L3"

ITEMS = [
 # ---------- 1. receptor -> action -> what you would SEE ----------
 dict(q="A patient is given a drug that blocks muscarinic receptors. Which set of findings should you expect?",
      ans="Dry mouth, blurred vision, flushing and urinary retention",
      why="Blocking muscarinic effects removes secretions, accommodation, and bladder tone &mdash; dry as a bone, blind as a bat, red as a beet.",
      wrong=[("Salivation, tearing and a slow heart rate", "That is what muscarinic ACTIVATION produces, not blockade."),
             ("Fasciculations and muscle weakness", "Those are nicotinic effects, not muscarinic blockade."),
             ("Bronchospasm and diarrhoea", "Both are muscarinic activation effects, the opposite of blockade.")],
      src=(S, 50)),

 dict(q="A cholinergic agonist is given. Which effect on the eye should you expect?",
      ans="Miosis", why="The M in the muscarinic effects list &mdash; pupillary constriction.",
      wrong=[("Mydriasis", "Pupil dilation is a nicotinic effect and an anticholinergic one."),
             ("Ptosis", "Lid droop is not among the muscarinic effects."),
             ("Nystagmus", "Not a described muscarinic effect.")],
      src=(S, 28)),

 dict(q="Which finding indicates NICOTINIC rather than muscarinic stimulation?",
      ans="Fasciculations", why="Fasciculations sit in the nicotinic list alongside mydriasis, tachycardia, weakness and hypertension.",
      wrong=[("Bronchorrhoea", "Watery bronchial secretion is muscarinic."),
             ("Lacrimation", "Tearing is muscarinic."),
             ("Bradycardia", "A muscarinic effect; nicotinic stimulation produces tachycardia instead.")],
      src=(S, 29)),

 dict(q="Nicotinic stimulation affects the heart rate and blood pressure in which direction?",
      ans="Both rise", why="Tachycardia and hypertension are both on the nicotinic list.",
      wrong=[("Both fall", "That is the muscarinic pattern."),
             ("Rate falls, pressure rises", "The rate rises rather than falls."),
             ("Rate rises, pressure falls", "The pressure rises rather than falls.")],
      src=(S, 29)),

 dict(q="A drug stimulates alpha-1 receptors. What should you expect to happen to the blood vessels and the blood pressure?",
      ans="Vasoconstriction, and the pressure rises",
      why="Alpha-1 receptors sit on the effector organ; stimulating them constricts vessels and raises both systolic and diastolic pressure.",
      wrong=[("Vasodilation, and the pressure falls", "That is closer to a beta-2 effect."),
             ("No vascular change, but the heart rate rises", "Rate change is a beta-1 effect."),
             ("Vasoconstriction, but the pressure falls", "Constriction raises pressure.")],
      src=(S, 96)),
 dict(q="Clonidine stimulates alpha-2 receptors centrally. What should you expect as a result?",
      ans="Reduced sympathetic outflow and vasodilation",
      why="It inhibits the sympathetic vasomotor centres, so less sympathetic traffic reaches the periphery.",
      wrong=[("Increased sympathetic outflow and vasoconstriction", "That reverses the mechanism."),
             ("Bronchodilation with no vascular effect", "That is a beta-2 agonist effect."),
             ("A direct increase in cardiac contractility", "That is a beta-1 effect.")],
      src=(S, 97)),

 dict(q="A beta-1 agonist is given to a patient. Which two cardiac effects should you expect?",
      ans="Increased contractility and increased rate",
      why="Positive inotrope and positive chronotrope &mdash; the two beta-1 cardiac actions.",
      wrong=[("Decreased contractility and decreased rate", "That is beta blockade."),
             ("Increased contractility with a slower rate", "Beta-1 stimulation raises both."),
             ("No cardiac effect, but bronchodilation", "Bronchodilation is beta-2.")],
      src=(S, 94)),

 dict(q="Which effect follows stimulation of beta-2 receptors in the airway?",
      ans="Bronchodilation", why="The basis of beta-2 agonist use in obstructive airway disease.",
      wrong=[("Bronchoconstriction", "Narrowing the airway is a muscarinic effect."),
             ("Increased bronchial secretions", "Secretion is muscarinic; beta-2 does not drive it."),
             ("No airway effect", "Beta-2 receptors mediate airway calibre.")],
      src=(S, 98)),

 dict(q="Which structural description fits the nicotinic receptor?",
      ans="A ligand-gated ion channel that admits sodium",
      why="Binding of two acetylcholine molecules changes its conformation and sodium flows in.",
      wrong=[("A G protein-coupled receptor with five subtypes", "That describes the muscarinic receptors."),
             ("An enzyme that hydrolyses acetylcholine", "That is acetylcholinesterase, not a receptor."),
             ("A nuclear receptor altering gene transcription", "Not the described mechanism.")],
      src=(S, 24)),

 # ---------- 2. mechanism gives you the indication ----------
 dict(q="Dobutamine is a synthetic beta-1 agonist. Which use follows from that mechanism?",
      ans="Increasing cardiac output in acute heart failure",
      why="A positive inotrope, and notably one that does not raise myocardial oxygen demand the way other sympathomimetics do.",
      wrong=[("Relieving acute bronchospasm", "That needs a beta-2 agonist."),
             ("Lowering blood pressure in hypertension", "It supports the circulation rather than lowering pressure."),
             ("Reversing a non-depolarizing blockade", "That requires an acetylcholinesterase inhibitor.")],
      src=(S, 94)),

 dict(q="Clonidine reduces sympathetic outflow. Besides hypertension, which use follows?",
      ans="Easing withdrawal from opiates, tobacco and benzodiazepines",
      why="Much of withdrawal is sympathetic overactivity, so damping the outflow blunts it.",
      wrong=[("Treating acute asthma", "Airway calibre is a beta-2 matter."),
             ("Reversing anticholinergic poisoning", "That calls for a centrally acting cholinesterase inhibitor."),
             ("Inducing anaesthesia for intubation", "That is a neuromuscular blocker's role.")],
      src=(S, 97)),

 dict(q="Scopolamine acts more on the central nervous system than atropine does at usual doses. Which use follows from that?",
      ans="Preventing motion sickness",
      why="Its central action is the point; it also blocks short-term memory and sedates at lower doses.",
      wrong=[("Reversing neuromuscular blockade after surgery", "That needs an acetylcholinesterase inhibitor."),
             ("Treating asthma", "Airway calibre is not its indication here."),
             ("Managing pheochromocytoma", "That requires alpha blockade.")],
      src=(S, 53)),

 dict(q="Phentolamine competitively blocks alpha-1 and alpha-2 receptors. Which use follows?",
      ans="Short-term management of pheochromocytoma",
      why="The tumour floods the circulation with catecholamines; blocking alpha receptors opposes the vasoconstriction.",
      wrong=[("Long-term treatment of asthma", "Airway calibre is a beta-2 matter."),
             ("Reversing succinylcholine", "There is no pharmacological reversal on that pathway here."),
             ("Raising blood pressure in shock", "Alpha blockade lowers pressure.")],
      src=(S, 110)),

 dict(q="Succinylcholine has a rapid onset and short duration. Which use follows from that profile?",
      ans="Rapid sequence intubation",
      why="Also used for endotracheal intubation at induction, for the same reason.",
      wrong=[("Long operations needing hours of paralysis", "Its short duration makes it unsuitable."),
             ("Chronic treatment of muscle spasticity", "It is not used chronically."),
             ("Reversal of a competitive blockade", "It is itself a blocker, not a reversal agent.")],
      src=(S, 66)),

 dict(q="Albuterol is a synthetic beta-2 agonist. Which conditions does that mechanism serve?",
      ans="Asthma and chronic obstructive pulmonary disease",
      why="Bronchodilation is the beta-2 airway action.",
      wrong=[("Hypertension", "It does not lower blood pressure."),
             ("Acute heart failure", "Cardiac support is a beta-1 action."),
             ("Motion sickness", "That is an antimuscarinic use.")],
      src=(S, 98)),

 # ---------- 3. more than one route to the same goal ----------
 dict(q="Which of these would be most likely to SLOW a rapid heart rate?",
      ans="An acetylcholinesterase inhibitor",
      why="Raising acetylcholine increases muscarinic activity at the heart, and bradycardia follows. A beta blocker or a muscarinic agonist would also work &mdash; there is more than one route.",
      wrong=[("An alpha-1 agonist", "It raises blood pressure; any rate change is an indirect reflex."),
             ("A beta-1 agonist", "That speeds the heart."),
             ("An antimuscarinic", "That removes vagal braking and speeds the heart.")],
      src=(S, 41)),

 dict(q="A patient is symptomatically bradycardic. Which of these would RAISE the heart rate?",
      ans="Atropine",
      why="Blocking muscarinic receptors at the heart removes the vagal brake. Beta-1 activation is the other route.",
      wrong=[("Propranolol", "A beta blocker slows the heart further."),
             ("Clonidine", "It reduces sympathetic outflow."),
             ("Bethanechol", "A muscarinic agonist slows the heart.")],
      src=(S, 48)),

 dict(q="Which of these would RAISE blood pressure?",
      ans="Phenylephrine",
      why="An alpha-1 agonist constricts vessels and raises both systolic and diastolic pressure.",
      wrong=[("Prazosin", "An alpha-1 blocker lowers pressure."),
             ("Clonidine", "It reduces sympathetic outflow and lowers pressure."),
             ("Phentolamine", "Alpha blockade lowers pressure and can cause postural hypotension.")],
      src=(S, 96)),

 # ---------- 4. place the named drug back in its class ----------
 dict(q="Which of these is the only depolarizing neuromuscular blocker available?",
      ans="Succinylcholine", why="Every other neuromuscular blocker in use is non-depolarizing and competitive.",
      wrong=[("Rocuronium", "Non-depolarizing, and reversible with neostigmine."),
             ("Vecuronium", "Non-depolarizing, and its blockade is competitive."),
             ("Tubocurarine", "The original competitive blocker, not a depolarizing one.")],
      src=(S, 66)),

 dict(q="Which of these is a selective beta-1 antagonist?",
      ans="Metoprolol", why="It sits with acebutolol, atenolol, bisoprolol and betaxolol in the selective group.",
      wrong=[("Propranolol", "Non-selective, blocking beta-1 and beta-2."),
             ("Timolol", "Non-selective."),
             ("Phenoxybenzamine", "An alpha blocker, not a beta blocker.")],
      src=(S, 120)),

 dict(q="Which of these is a selective alpha-1 blocker?",
      ans="Tamsulosin", why="It sits with prazosin, terazosin, doxazosin and alfuzosin.",
      wrong=[("Phentolamine", "Blocks alpha-1 and alpha-2 competitively."),
             ("Phenoxybenzamine", "Blocks alpha-1 and alpha-2, and irreversibly."),
             ("Clonidine", "An alpha-2 agonist, not a blocker.")],
      src=(S, 111)),

 dict(q="Which of these is an alpha-2 AGONIST?",
      ans="Clonidine", why="It acts centrally at alpha-2 receptors to reduce sympathetic outflow.",
      wrong=[("Prazosin", "An alpha-1 antagonist."),
             ("Phenylephrine", "An alpha-1 agonist."),
             ("Phenoxybenzamine", "A non-selective alpha antagonist.")],
      src=(S, 97)),

 dict(q="Which of these blocks alpha receptors IRREVERSIBLY, so that new receptors must be synthesised?",
      ans="Phenoxybenzamine", why="Non-selective and non-competitive, which is what makes the blockade irreversible.",
      wrong=[("Phentolamine", "Also non-selective, but competitive and lasting only hours."),
             ("Prazosin", "A selective, competitive alpha-1 blocker."),
             ("Propranolol", "A beta antagonist.")],
      src=(S, 108)),

 dict(q="Which group do epinephrine, norepinephrine, isoproterenol and dopamine belong to?",
      ans="The catecholamines",
      why="They share high potency and rapid inactivation by catechol-O-methyltransferase and monoamine oxidase.",
      wrong=[("The indirect-acting agonists", "Those act by releasing or blocking reuptake of noradrenaline."),
             ("The mixed-action agonists", "That group is ephedrine and pseudoephedrine."),
             ("The ganglionic blockers", "Those act at autonomic ganglia.")],
      src=(S, 79)),

 # ---------- 5. adverse effects, toxidromes and antidotes ----------
 dict(q="Which description belongs to the anticholinergic toxidrome?",
      ans="Hot as Hades &mdash; hyperthermia",
      why="It sits with mad as a hatter, blind as a bat, red as a beet and dry as a bone.",
      wrong=[("Cold and clammy from sweating", "Anticholinergics reduce sweating, which is why they cause hyperthermia."),
             ("Pinpoint pupils", "They dilate the pupil rather than constricting it."),
             ("Copious salivation", "They dry secretions.")],
      src=(S, 50)),

 dict(q="Which central feature marks the severe end of anticholinergic toxicity?",
      ans="Seizures",
      why="The mad-as-a-hatter progression runs from sedation and anxiety through hallucinations to seizures.",
      wrong=[("Flaccid paralysis", "That belongs to depolarizing neuromuscular blockade."),
             ("Bradycardia", "Anticholinergics speed the heart."),
             ("Bronchorrhoea", "They dry secretions rather than increasing them.")],
      src=(S, 50)),

 dict(q="Pralidoxime is given for acetylcholinesterase inhibitor poisoning. What is its key limitation?",
      ans="It does not penetrate the central nervous system",
      why="It reactivates inhibited enzyme peripherally, and it also cannot overcome reversible inhibitors such as physostigmine.",
      wrong=[("It only works on muscarinic and not nicotinic signs", "The limitation described is anatomical, not receptor-specific."),
             ("It must be given before the exposure", "It is given after, to reactivate the enzyme."),
             ("It cannot be given with atropine", "The two are used together.")],
      src=(S, 42)),

 dict(q="Physostigmine, neostigmine and pyridostigmine all inhibit acetylcholinesterase. What separates physostigmine from the other two?",
      ans="It crosses the blood-brain barrier",
      why="That is why it is the one used when anticholinergic toxicity is central; the others act peripherally.",
      wrong=[("It is the only one that is reversible", "All three are reversible inhibitors."),
             ("It is the only one given by mouth", "Route is not the distinction described."),
             ("It works at nicotinic receptors only", "They all raise acetylcholine at both receptor types.")],
      src=(S, 42)),

 dict(q="During which phase of succinylcholine's action does flaccid paralysis appear?",
      ans="Phase two",
      why="Phase one is the depolarization that produces fasciculations; the receptor then desensitises, and phase two is the paralysis.",
      wrong=[("Phase one", "That phase produces fasciculations, not paralysis."),
             ("Before any depolarization occurs", "Depolarization comes first."),
             ("Only after the drug is metabolised", "The paralysis occurs while the drug is still acting.")],
      src=(S, 68)),

 dict(q="Which adverse effects should a patient starting albuterol be warned about?",
      ans="Tremor, restlessness and anxiety",
      why="The expected beta-agonist effects &mdash; unpleasant rather than dangerous.",
      wrong=[("Dry mouth and urinary retention", "Those are antimuscarinic effects."),
             ("Bradycardia and bronchospasm", "Those oppose what the drug does."),
             ("Sedation and memory impairment", "Those belong to scopolamine.")],
      src=(S, 98)),
]
