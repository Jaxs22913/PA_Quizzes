# -*- coding: utf-8 -*-
"""Cholinergic drug chart data -- Pharmacology I Exam 1, Lecture 3.

The companion to _pharm_receptor_data.py. That page is organised by RECEPTOR;
this one is organised by DRUG, across slides 26 to 70.

Same principle: everything is from the slides, each row cites the one it came
from, and anything that is a memory device rather than lecture content is
labelled where it appears.

THE PAIRS PANEL IS THE POINT OF THE PAGE. Almost every hard question in this
half of the lecture is two drugs that look interchangeable and are not --
bethanechol against carbachol, physostigmine against neostigmine, edrophonium
against pyridostigmine, and the two kinds of neuromuscular blocker. Dr. Wood
built one of his review answers on exactly that, and said the axis was the
blood-brain barrier.
"""

# group key, label, colour, one-line, sub-heading note
GROUPS = [
 ("direct", "Direct-acting agonists", "#1f6b4a",
  "Bind the receptor themselves",
  "Also called <b>parasympathomimetics</b>. Two families: the <b>choline esters</b> "
  "(acetylcholine, carbachol, bethanechol) and the <b>natural alkaloids</b> (pilocarpine)."),
 ("indirect", "Indirect-acting &mdash; cholinesterase inhibitors", "#2d3f7a",
  "Raise the acetylcholine that is already there",
  "They inhibit acetylcholinesterase, so acetylcholine accumulates and acts at "
  "<b>both muscarinic and nicotinic</b> sites. Whether a given one reaches the brain is what "
  "separates them clinically."),
 ("antimusc", "Antimuscarinics", "#8a5f14",
  "Block muscarinic only",
  "They block the muscarinic receptors of parasympathetic nerves, and the few sympathetic "
  "cholinergic fibres to salivary and sweat glands. <b>They do NOT block nicotinic receptors</b> "
  "&mdash; little or no action at the neuromuscular junction or the autonomic ganglia."),
 ("ganglion", "Ganglionic blockers", "#5f3a8a",
  "Block the entire autonomic output",
  "They act at the nicotinic receptors of <b>both</b> sympathetic and parasympathetic ganglia, "
  "so they shut off the whole autonomic outflow. <b>Rarely used clinically.</b>"),
 ("nmb", "Neuromuscular blockers", "#8c2f22",
  "Nicotinic, at the muscle end plate",
  "Structural analogues of acetylcholine acting at the nicotinic receptors of the skeletal "
  "muscle end plate &mdash; as antagonists (non-depolarizing) or as agonists (depolarizing)."),
]

# group, drug, acts where, used for, watch for, slide
DRUGS = [
 ("direct", "Bethanechol",
  "<b>Muscarinic only &mdash; it lacks nicotinic activity.</b> Not hydrolysed by "
  "acetylcholinesterase, so it lasts.",
  "Bladder and gastrointestinal atony.",
  "Sweating, salivation, flushing.", 30),
 ("direct", "Carbachol",
  "<b>Muscarinic AND nicotinic.</b> Its nicotinic action releases epinephrine from the adrenal "
  "medulla.",
  "Ophthalmic use; profound cardiovascular and gastrointestinal effects.",
  "May <b>first stimulate, then depress</b> those systems.", 32),
 ("direct", "Pilocarpine",
  "Muscarinic. A natural alkaloid rather than a choline ester.",
  "<b>Miosis, ciliary muscle contraction and lowering of intraocular pressure.</b>",
  "The eye drug of the group.", 33),

 ("indirect", "Edrophonium",
  "Reversible. <b>The short-acting prototype.</b>",
  "<b>DIAGNOSING myasthenia gravis</b> &mdash; short action is the point.",
  "Also reverses a competitive neuromuscular blockade.", 35),
 ("indirect", "Physostigmine",
  "Reversible, and <b>it reaches the central nervous system</b>.",
  "<b>Antidote for anticholinergic overdose</b> &mdash; atropine, phenothiazines, tricyclic "
  "antidepressants. Also raises intestinal and bladder motility, causes miosis and lowers "
  "intraocular pressure.",
  "<b>Convulsions at high doses</b>, bradycardia, reduced cardiac output, and paralysis of "
  "skeletal muscle from accumulated acetylcholine.", 36),
 ("indirect", "Neostigmine",
  "Reversible. <b>Poorly absorbed from the gut and does NOT enter the central nervous "
  "system.</b>",
  "<b>Antidote for competitive neuromuscular blockers</b>; symptomatic treatment of myasthenia "
  "gravis; stimulating bladder and bowel.",
  "Salivation, flushing, low blood pressure, nausea, abdominal pain, diarrhoea, bronchospasm.",
  38),
 ("indirect", "Pyridostigmine",
  "Reversible, peripheral.",
  "<b>CHRONIC management of myasthenia gravis</b> &mdash; where edrophonium diagnoses it.",
  "Same peripheral cholinergic effects as neostigmine.", 39),
 ("indirect", "Donepezil, rivastigmine, galantamine",
  "Reversible, central.",
  "<b>Slowing the progression of Alzheimer disease</b>, which is associated with a deficiency of "
  "central cholinergic neurons.",
  "Gastrointestinal distress.", 40),
 ("indirect", "Organophosphates &mdash; the irreversible inhibitors",
  "<b>Irreversible.</b> Agricultural insecticides, and used in suicide and homicide.",
  "No therapeutic use. Toxicity shows as <b>nicotinic or muscarinic signs</b>, or both.",
  "<b>Pralidoxime</b> reactivates the enzyme &mdash; but it does <b>not</b> enter the central "
  "nervous system, and cannot overcome reversible inhibitors such as physostigmine.", 42),

 ("antimusc", "Atropine",
  "Competitive at muscarinic receptors, <b>centrally and peripherally</b>. Greatest effect on "
  "bronchial tissue and on sweat and saliva.",
  "Blocking secretions before surgery or in end-of-life care; dilating the pupil; "
  "antispasmodic in the gut; <b>antidote for cholinesterase inhibitor insecticides and some "
  "mushroom poisoning</b>.",
  "<b>Bradycardia at LOWER doses, tachycardia at HIGHER doses</b> &mdash; the dose paradox. Also "
  "dry mouth, blurred vision, &ldquo;sandy eyes&rdquo;, urinary retention, constipation, and "
  "restlessness through to delirium.", 51),
 ("antimusc", "Scopolamine",
  "Peripheral effects like atropine, but <b>greater central action at therapeutic doses</b>.",
  "<b>Preventing motion sickness</b>; anaesthetic adjunct; short-term memory blocking; reducing "
  "secretions.",
  "As atropine. <b>Wash hands after handling the patch</b> &mdash; touching the eye afterwards "
  "blurs vision.", 54),
 ("antimusc", "Ipratropium, tiotropium",
  "Muscarinic blockade in the airway.",
  "Obstructive airway disease.",
  "Inhaled, so systemic anticholinergic effects are limited.", 55),
 ("antimusc", "Glycopyrrolate",
  "Peripheral muscarinic blockade.",
  "Drying secretions &mdash; the drooling agent.",
  "The peripheral counterpart to scopolamine's central action.", 55),
 ("antimusc", "Oxybutynin and the other bladder agents",
  "Muscarinic blockade at the bladder &mdash; darifenacin, fesoterodine, solifenacin, "
  "tolterodine, trospium.",
  "<b>Lowering pressure inside the bladder and increasing its capacity</b> &mdash; urinary "
  "incontinence.",
  "Same mechanism as glycopyrrolate in a different organ; the split between them is licensing "
  "rather than pharmacology.", 56),

 ("ganglion", "Nicotine",
  "Nicotinic at the ganglia. <b>The one agent in the group that is not a competitive "
  "antagonist.</b>",
  "No therapeutic use here &mdash; recreational.",
  "<b>Stimulates at low concentration and BLOCKS at high concentration.</b>", 59),
 ("ganglion", "The blockers as a class",
  "Nicotinic receptors of sympathetic and parasympathetic ganglia alike. All except nicotine are "
  "<b>non-depolarizing competitive antagonists</b>.",
  "Rarely used clinically.",
  "The predominant sympathetic effect is <b>vasodilation</b>; the predominant parasympathetic "
  "effects are <b>bladder and bowel atony, cycloplegia, dry mouth and tachycardia</b>.", 58),

 ("nmb", "Non-depolarizing &mdash; rocuronium, vecuronium, pancuronium, cisatracurium",
  "<b>Competitive antagonists</b> at the end-plate nicotinic receptor: they sit on it and keep "
  "acetylcholine off.",
  "Skeletal muscle relaxation during surgery.",
  "<b>They CAN be reversed</b> &mdash; raise acetylcholine with neostigmine, pyridostigmine or "
  "edrophonium and it outcompetes the blocker. Paralysis arrives in order: <b>face and eye "
  "first</b>, then fingers, limbs, neck, trunk, intercostals.", 64),
 ("nmb", "Succinylcholine &mdash; the only depolarizing agent",
  "An <b>agonist</b>: it binds the receptor and depolarises, then is not cleared by "
  "acetylcholinesterase, so the stimulation persists. <b>Phase I</b> opens the sodium channel and "
  "depolarises; <b>Phase II</b> is resistance to further depolarization, and that is where the "
  "<b>flaccid paralysis</b> appears.",
  "<b>Rapid sequence intubation</b> and intubation at induction &mdash; rapid onset, short "
  "duration.",
  "Broken down by <b>plasma pseudocholinesterase</b>; a genetic deficiency causes "
  "<b>prolonged paralysis and apnoea</b>. With halothane it can trigger <b>malignant "
  "hyperthermia</b> &mdash; rigidity, metabolic acidosis, tachycardia, hyperpyrexia &mdash; "
  "treated by cooling and <b>dantrolene</b>. Respiratory muscles are paralysed <b>last</b>.", 70),
]

# The confusable pairs -- title, left, right, the axis that separates them, slides
PAIRS = [
 ("Bethanechol vs carbachol",
  "<b>Bethanechol</b> &mdash; muscarinic ONLY.",
  "<b>Carbachol</b> &mdash; muscarinic AND nicotinic.",
  "Whether it also hits nicotinic receptors. Carbachol's nicotinic action is why it releases "
  "epinephrine from the adrenal medulla; bethanechol has no such effect.", "30, 32"),
 ("Physostigmine vs neostigmine",
  "<b>Physostigmine</b> &mdash; enters the central nervous system.",
  "<b>Neostigmine</b> &mdash; does not.",
  "<b>The blood-brain barrier.</b> That is why physostigmine is the antidote when anticholinergic "
  "toxicity is central, and neostigmine is the one used peripherally in surgery. Dr. Wood built "
  "a whole review answer on this axis.", "36, 38"),
 ("Edrophonium vs pyridostigmine",
  "<b>Edrophonium</b> &mdash; short-acting.",
  "<b>Pyridostigmine</b> &mdash; long-acting.",
  "<b>Diagnose against maintain.</b> Edrophonium diagnoses myasthenia gravis; pyridostigmine "
  "manages it chronically. Neostigmine sits between them, treating symptoms.", "35, 39"),
 ("Non-depolarizing vs depolarizing blockade",
  "<b>Non-depolarizing</b> &mdash; competitive antagonist, reversible.",
  "<b>Succinylcholine</b> &mdash; agonist, not reversible this way.",
  "<b>Whether a cholinesterase inhibitor helps.</b> Raising acetylcholine outcompetes a "
  "competitive blocker and restores function; against succinylcholine, more acetylcholine does "
  "nothing, because the problem is that the receptor is already over-stimulated.", "64, 67"),
 ("Atropine at low against high dose",
  "<b>Low dose</b> &mdash; bradycardia.",
  "<b>High dose</b> &mdash; tachycardia.",
  "The dose itself. It is the one place in this lecture where the same drug does opposite things "
  "to the same organ, which is exactly the kind of detail a question is built on.", "52"),
]
