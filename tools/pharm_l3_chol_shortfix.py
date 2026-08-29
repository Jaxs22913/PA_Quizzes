"""Length-bias remediation for Lecture 3 Topic A, by SHORTENING the answer.

The Lecture 1 and 2 pools were enumerative -- their correct answers were
genuinely lists, so the fix there was to give the distractors matching
structure. This pool's problem is different and is mine: I wrote explanatory
sentences as options, so the answer carried its own justification and ran a
median of 114 characters against distractors half that. The reasoning belongs
in the explanation, which already states it.

So here the correct answer is trimmed to the answer. Nothing is lost -- every
detail removed is already in that option's explanation text.

SHORTEN maps pool index -> replacement correct-answer text. The applier asserts
the replacement really is shorter and really does land on the correct option.
LENGTHEN handles the few where the answer is a bare chemical name that cannot
be trimmed further, giving the distractors parallel descriptive tails instead.
"""
SHORTEN = {
 0:  "Somatic, under voluntary control, and autonomic, under involuntary control",
 2:  "A preganglionic neuron in the central nervous system and a postganglionic neuron from a ganglion",
 3:  "It innervates the gut, pancreas and gallbladder and functions independently",
 4:  "Synthesis, storage, release, receptor binding, degradation, recycling of choline",
 7:  "Five subunits forming a ligand-gated ion channel opened by two acetylcholine molecules",
 11: "Choline esters and naturally occurring alkaloids",
 12: "It resists acetylcholinesterase, and is muscarinic without nicotinic activity",
 13: "It stimulates the detrusor and relaxes the trigone and sphincter",
 15: "Miosis and ciliary muscle contraction, lowering intraocular pressure",
 17: "Diagnosing myasthenia gravis and reversing nondepolarizing blockade",
 20: "Convulsions, bradycardia and skeletal muscle paralysis",
 21: "Poorly absorbed orally, and it does not enter the central nervous system",
 23: "Donepezil, rivastigmine and galantamine",
 24: "It does not enter the brain, and cannot overcome reversible inhibitors",
 26: "They do not block nicotinic receptors",
 27: "Persistent mydriasis and cycloplegia",
 30: "Cholinesterase inhibitor insecticides, and some mushroom poisonings",
 31: "Greater central action, preventing motion sickness",
 32: "Wash their hands thoroughly afterwards",
 33: "Inhaled bronchodilators for chronic obstructive pulmonary disease",
 34: "They lower bladder pressure and raise bladder capacity",
 36: "They block nicotinic receptors at sympathetic and parasympathetic ganglia",
 38: "The small muscles of the face and eye",
 39: "By giving a cholinesterase inhibitor such as neostigmine",
 40: "It depolarizes the junction like acetylcholine but is not rapidly destroyed",
 42: "To prevent the fasciculations that cause muscle soreness",
 43: "Rapid cooling and dantrolene",
 44: "Anticholinergics, parasympatholytics or antimuscarinics",
 45: "It carries signals to the central nervous system",
 48: "Multiple functions by location, and usually inhibitory",
 49: "Both a neurotransmitter and a hormone",
 54: "Lowering intraocular pressure in glaucoma",
 56: "Stimulating the bladder and gut, and reversing competitive blockade",
 57: "As agricultural insecticides",
 59: "Deadly nightshade, jimson weed and mandrake",
 60: "On bronchial tissue and on sweat and saliva",
 61: "Blocking respiratory tract secretions before surgery",
 62: "Dry mouth, blurred vision, urinary retention and constipation",
 63: "Reducing pre-surgical secretions, and reducing drooling",
 64: "Vasodilation, with atony of the bladder and gut and tachycardia",
 65: "Structural analogues of acetylcholine",
 66: "They allow the use of less anaesthetic agent",
 67: "Histamine release, with a fall in blood pressure and flushing",
 68: "Phase one depolarization, then phase two resistance",
 69: "The respiratory muscles are paralysed last",
 71: "Alpha-one postsynaptically, alpha-two presynaptically",
 72: "Epinephrine at least equal to norepinephrine, far above isoproterenol",
}

# Index 47's answer is a chemical name that cannot be trimmed; the distractors
# get parallel descriptive tails instead. Each stays plainly wrong for a
# question that asks for the BRAIN's major inhibitory transmitter.
LENGTHEN = {
 47: {"Glycine": "Glycine, the inhibitory transmitter of spinal cord neurons",
      "Acetylcholine": "Acetylcholine, which controls memory in brain neurons",
      "Norepinephrine": "Norepinephrine, which regulates normal brain processes"},
}
