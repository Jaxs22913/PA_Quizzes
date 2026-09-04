# -*- coding: utf-8 -*-
"""Receptor chart data -- Pharmacology I Exam 1, Lecture 3.

THE DECK HAS NO SUCH TABLE. It teaches the receptors on slides 22-24 and 76-78,
the organ actions as a figure on slide 11, and then the drugs one at a time
across slides 26-122. Everything here comes from those slides; the assembly
into one receptor-by-receptor chart is the point of the page.

This is the shape Dr. Wood described wanting at the review: know which receptors
are associated with which actions, then how a drug affects that receptor, then
what you expect to see. The chart runs left to right in exactly that order.

MEMORY HOOKS ARE MARKED AS SUCH. "One heart, two lungs" is not on any slide --
it is a standard mnemonic, included because the request was for something
memorisable, and flagged so nobody mistakes it for lecture content.
"""

# key, label, colour, where it is, hook, actions, agonists, antagonists, slides
RECEPTORS = [
 dict(key="a1", label="Alpha-1", colour="#8c2f22", short="Squeeze",
      where="On the <b>postsynaptic membrane of the effector organ</b> &mdash; the receiving end.",
      hook="<b>Alpha-1 squeezes.</b> Vessels, sphincters and the pupil all tighten.",
      actions=["<b>Vasoconstriction</b>, so blood pressure rises &mdash; systolic and diastolic",
               "<b>Pupil dilates</b> by contracting the iris <i>radial</i> muscle",
               "<b>Contracts</b> the bladder trigone and sphincter",
               "<b>Decreases</b> renin secretion &mdash; the opposite of beta-1"],
      agon=[
            ("Direct-acting &mdash; catecholamines",
             "norepinephrine &middot; epinephrine (higher doses) &middot; dopamine (very high doses)"),
            ("Direct-acting &mdash; synthetic",
             "phenylephrine &middot; oxymetazoline"),
            ("Indirect-acting",
             "amphetamine &middot; cocaine"),
            ("Mixed-action",
             "ephedrine &middot; pseudoephedrine"),
          ],
      anta=[
            ("Selective alpha-1 blockers &mdash; the &ldquo;-osins&rdquo;",
             "prazosin &middot; terazosin &middot; doxazosin &middot; tamsulosin &middot; alfuzosin"),
            ("Non-selective alpha blockers",
             "phentolamine (competitive) &middot; phenoxybenzamine (irreversible)"),
            ("Combined alpha and beta blockers",
             "labetalol &middot; carvedilol"),
          ],
      slides="76, 82, 96, 99, 103, 107, 111"),
 dict(key="a2", label="Alpha-2", colour="#8a5f14", short="Brake",
      where="On <b>presynaptic nerve endings</b> &mdash; the sending end, not the target organ.",
      hook="<b>Alpha-2 is the brake on the system itself.</b> Because it sits presynaptically, "
           "stimulating it turns the sympathetic outflow DOWN.",
      actions=["<b>Reduces sympathetic outflow</b> from the central vasomotor centres",
               "<b>Vasodilation</b> and a fall in blood pressure follow",
               "This is why an alpha-2 <i>agonist</i> lowers pressure while an alpha-1 agonist "
               "raises it &mdash; the location, not the letter, decides"],
      agon=[
            ("Direct-acting &mdash; synthetic",
             "clonidine &middot; oxymetazoline"),
          ],
      anta=[
            ("Non-selective alpha blockers",
             "phentolamine &middot; phenoxybenzamine"),
          ],
      slides="76, 82, 97, 107, 108"),
 dict(key="b1", label="Beta-1", colour="#2d3f7a", short="Heart",
      where="Mainly the <b>heart</b>, and the kidney.",
      hook="<b>You have ONE heart &mdash; beta-1.</b> <i>Memory hook, not from the slides.</i>",
      actions=["<b>Increases heart rate</b> &mdash; positive chronotrope",
               "<b>Increases contractility</b> &mdash; positive inotrope",
               "<b>Increases renin</b> secretion from the kidney"],
      agon=[
            ("Direct-acting &mdash; catecholamines",
             "isoproterenol &middot; epinephrine &middot; norepinephrine &middot; dopamine"),
            ("Direct-acting &mdash; synthetic",
             "dobutamine (beta-1 selective)"),
            ("Indirect-acting",
             "amphetamine"),
          ],
      anta=[
            ("Selective beta-1 antagonists",
             "metoprolol &middot; atenolol &middot; bisoprolol &middot; betaxolol &middot; acebutolol"),
            ("Non-selective beta antagonists",
             "propranolol &middot; timolol &middot; nadolol"),
            ("With partial agonist activity",
             "acebutolol &middot; pindolol"),
            ("Combined alpha and beta blockers",
             "labetalol &middot; carvedilol"),
          ],
      slides="11, 79, 82, 94, 113, 114, 120, 121, 122"),
 dict(key="b2", label="Beta-2", colour="#1f6b4a", short="Lungs",
      where="<b>Bronchial smooth muscle</b>, and the vessels of skeletal muscle.",
      hook="<b>You have TWO lungs &mdash; beta-2.</b> <i>Memory hook, not from the slides.</i> "
           "It is also why a NON-selective beta blocker is a problem in asthma: blocking "
           "beta-2 closes the airway.",
      actions=["<b>Bronchodilation</b>",
               "<b>Vasodilation</b> in skeletal muscle beds",
               "<b>Relaxes the uterus</b>",
               "Contributes to <b>hyperglycaemia</b> with epinephrine"],
      agon=[
            ("Direct-acting &mdash; catecholamines",
             "isoproterenol &middot; epinephrine"),
            ("Direct-acting &mdash; synthetic",
             "albuterol (beta-2 selective)"),
            ("Mixed-action",
             "ephedrine &middot; pseudoephedrine"),
          ],
      anta=[
            ("Non-selective beta antagonists",
             "propranolol &middot; timolol &middot; nadolol &mdash; <b>this is the asthma problem</b>"),
            ("Combined alpha and beta blockers",
             "labetalol &middot; carvedilol"),
          ],
      slides="79, 84, 98, 103, 113, 119, 122"),
 dict(key="m", label="Muscarinic", colour="#5f3a8a", short="Rest and digest",
      where="<b>M1</b> neurons and gastric parietal cells &middot; <b>M2</b> neurons, cardiac "
            "cells and smooth muscle &middot; <b>M3</b> neurons, bladder, exocrine glands and "
            "smooth muscle. Only these three are functionally characterised.",
      hook="<b>DUMBBELS</b> &mdash; and every one of them is a secretion, a contraction or a "
           "slowing. Blocking them gives you the exact opposite, which is the anticholinergic "
           "toxidrome.",
      actions=["<b>D</b>efecation &middot; <b>U</b>rination &middot; <b>M</b>iosis",
               "<b>B</b>radycardia &middot; <b>B</b>ronchorrhoea &middot; <b>B</b>ronchospasm",
               "<b>E</b>mesis &middot; <b>L</b>acrimation &middot; <b>S</b>alivation",
               "The lens also <b>accommodates for near vision</b>"],
      agon=[
            ("Direct-acting &mdash; choline esters",
             "acetylcholine &middot; carbachol &middot; bethanechol"),
            ("Direct-acting &mdash; natural alkaloids",
             "pilocarpine"),
            ("Indirect &mdash; reversible cholinesterase inhibitors",
             "edrophonium &middot; physostigmine &middot; neostigmine &middot; pyridostigmine &middot; donepezil, rivastigmine, galantamine"),
            ("Indirect &mdash; irreversible",
             "the organophosphates"),
          ],
      anta=[
            ("Antimuscarinics &mdash; natural",
             "atropine &middot; scopolamine"),
            ("Antimuscarinics &mdash; synthetic",
             "ipratropium &middot; tiotropium &middot; glycopyrrolate"),
            ("Antimuscarinics &mdash; bladder agents",
             "oxybutynin &middot; tolterodine &middot; solifenacin &middot; darifenacin &middot; fesoterodine &middot; trospium"),
          ],
      slides="11, 23, 26, 28, 30, 34, 40, 42, 46, 47, 55, 56"),
 dict(key="n", label="Nicotinic", colour="#4a6b7a", short="Ganglia and muscle",
      where="<b>Autonomic ganglia</b>, the <b>adrenal medulla</b>, the <b>neuromuscular "
            "junction</b> and the central nervous system.",
      hook="<b>M-T-W-H-F</b>, the days of the week &mdash; and note it is the mirror image of "
           "the muscarinic list on the pupil and the heart.",
      actions=["<b>M</b>ydriasis &middot; <b>T</b>achycardia",
               "<b>W</b>eakness, meaning paralysis",
               "<b>H</b>ypertension &middot; <b>F</b>asciculations",
               "Structurally a <b>ligand-gated ion channel</b>: two acetylcholine molecules bind "
               "and sodium flows in"],
      agon=[
            ("Direct-acting &mdash; choline esters",
             "carbachol (muscarinic and nicotinic) &middot; acetylcholine"),
            ("Depolarizing neuromuscular blocker",
             "succinylcholine &mdash; agonist first, paralysis second"),
            ("Ganglionic stimulant",
             "nicotine &mdash; stimulates low, <b>blocks high</b>"),
          ],
      anta=[
            ("Non-depolarizing neuromuscular blockers",
             "rocuronium &middot; vecuronium &middot; pancuronium &middot; cisatracurium &middot; tubocurarine"),
            ("Ganglionic blockers",
             "all non-depolarizing competitive antagonists except nicotine"),
          ],
      slides="24, 29, 58, 59, 61, 62, 66"),
]

FIGURE = dict(
  file="pharm-exam-1-study-guide-images/l3-s011-sns-pns-effector-organs.jpg",
  alt="Actions of the sympathetic and parasympathetic nervous systems on each effector organ, "
      "sympathetic in red and parasympathetic in blue",
  slide=11)
