# -*- coding: utf-8 -*-
"""Rapid-drill bank: glaucoma agents, anaesthetics, cycloplegics and fluorescein.

One fact, four drug names, no doses.

SCOPE FROM THE RECORDING: the SPECIFIC combination products are de-scoped --
"the specific combinations, I don't care that you memorize, but just know if I
was to say, hey, patient's on this drug right now, what would be a helpful
second line agent to add on?" So the drill asks what to ADD to what, which is
the question he said he would ask, not which brand name pairs which two drugs.
"""
ITEMS = [
dict(q="Which class is FIRST LINE for glaucoma and the most commonly used?",
     ans="Latanoprost", src=("OPH", 64),
     why="The prostaglandin analogues, which increase aqueous outflow. Beta blockers are second line.",
     wrong=[("Timolol", "A beta blocker, which is second line and works by reducing production."),
            ("Dorzolamide", "A carbonic anhydrase inhibitor, reducing production."),
            ("Pilocarpine", "A cholinergic agonist, poorly tolerated and rarely first choice.")]),

dict(q="Which glaucoma class changes EYELASH LENGTH and IRIS COLOUR?",
     ans="Bimatoprost", src=("OPH", 65),
     why="The prostaglandin analogues, which is why one of them is also marketed for lash growth. They also cause conjunctival hyperaemia.",
     wrong=[("Brimonidine", "An alpha-2 agonist; irritation, hyperaemia and allergic conjunctivitis."),
            ("Betaxolol", "A beta-1 selective blocker."),
            ("Brinzolamide", "A carbonic anhydrase inhibitor; bitter taste and stinging.")]),

dict(q="Why must a prostaglandin analogue NOT be dosed more than once daily?",
     ans="Exceeding once daily INHIBITS the pressure-lowering effect", src=("OPH", 66),
     why="More is worse, not better, which is counterintuitive and therefore worth holding.",
     wrong=[("It causes rebound hyperaemia", "That is the topical vasoconstrictors."),
            ("It raises the risk of cataract", "That is the ocular glucocorticoids."),
            ("It causes bradycardia", "That is systemic absorption of a beta blocker.")]),

dict(q="Which glaucoma agent is BETA 1 SELECTIVE?",
     ans="Betaxolol", src=("OPH", 67),
     why="The selective one, so it carries less risk of bronchoconstriction in a patient with asthma.",
     wrong=[("Timolol", "Nonselective."),
            ("Carteolol", "Nonselective."),
            ("Levobunolol", "Nonselective.")]),

dict(q="Why is a NONSELECTIVE beta blocker more efficacious in the eye but worse tolerated?",
     ans="There are more beta 2 receptors in the eye", src=("OPH", 67),
     why="So blocking both gives more effect, at the cost of beta 2 effects elsewhere.",
     wrong=[("There are more beta 1 receptors in the eye", "It is the beta 2 receptors that predominate there."),
            ("It penetrates the cornea better", "Not the reason given."),
            ("It has a longer half-life", "Not the reason given.")]),

dict(q="Which glaucoma class risks worsening heart failure, bradycardia, heart block and increased airway resistance?",
     ans="Timolol", src=("OPH", 67),
     why="Systemic beta blockade from a drop, which is why the nasolacrimal duct is worth occluding.",
     wrong=[("Latanoprost", "Limited systemic side effects."),
            ("Dorzolamide", "Bitter taste and stinging rather than systemic cardiac effects."),
            ("Pilocarpine", "Small pupils, myopia and visual disturbance.")]),

dict(q="Which glaucoma class works by blocking beta receptors in the ciliary body epithelium to reduce aqueous production?",
     ans="Levobunolol", src=("OPH", 67),
     why="Less catecholamine activation, less cyclic AMP, less aqueous made.",
     wrong=[("Travoprost", "A prostaglandin, increasing OUTFLOW rather than reducing production."),
            ("Carbachol", "A cholinergic agonist, increasing outflow."),
            ("Apraclonidine", "An alpha-2 agonist, which does both.")]),

dict(q="Which glaucoma agent is CONTRAINDICATED in children under two years of age?",
     ans="Brimonidine", src=("OPH", 69),
     why="The alpha-2 agonists, because of central nervous system depression and apnoea.",
     wrong=[("Latanoprost", "No such age contraindication is given."),
            ("Timolol", "Its cautions are cardiac and respiratory."),
            ("Dorzolamide", "Its adverse effects are taste and stinging.")]),

dict(q="Which alpha-2 agonist is MORE LIPOPHILIC?",
     ans="Brimonidine", src=("OPH", 69),
     why="Apraclonidine is highly ionised at physiological pH; brimonidine is the more lipophilic of the two, and allergic conjunctivitis is less common with it.",
     wrong=[("Apraclonidine", "Highly ionised at physiological pH."),
            ("Timolol", "A beta blocker."),
            ("Pilocarpine", "A cholinergic agonist.")]),

dict(q="Which class reduces aqueous production by inhibiting carbonic anhydrase in the ciliary body epithelium?",
     ans="Dorzolamide", src=("OPH", 70),
     why="Less bicarbonate, less fluid transport, lower pressure.",
     wrong=[("Bimatoprost", "A prostaglandin, increasing outflow."),
            ("Betaxolol", "A beta blocker, reducing production by a different route."),
            ("Carbachol", "A cholinergic agonist, increasing outflow.")]),

dict(q="Which glaucoma class causes a BITTER TASTE in about a quarter of patients and stinging in about a third?",
     ans="Brinzolamide", src=("OPH", 70),
     why="The carbonic anhydrase inhibitors, which also cause allergic conjunctivitis.",
     wrong=[("Latanoprost", "Hyperaemia, irritation, lash and iris changes."),
            ("Timolol", "Systemic cardiac and respiratory effects."),
            ("Brimonidine", "Irritation, hyperaemia, pruritus, allergic conjunctivitis.")]),

dict(q="Which class activates muscarinic receptors, contracting the ciliary muscle to facilitate outflow?",
     ans="Pilocarpine", src=("OPH", 72),
     why="The cholinergic agonists. Compliance is poor because of side effects and frequent administration.",
     wrong=[("Timolol", "Blocks beta receptors to reduce production."),
            ("Brimonidine", "An alpha-2 agonist."),
            ("Dorzolamide", "A carbonic anhydrase inhibitor.")]),

dict(q="Which glaucoma class causes fixed, small pupils, myopia and visual disturbance — and is especially poorly tolerated by YOUNGER patients?",
     ans="Carbachol", src=("OPH", 72),
     why="The cholinergic agonists. Younger patients are usually intolerant of miotic therapy because of the visual blurring.",
     wrong=[("Latanoprost", "Lash and iris changes rather than miosis."),
            ("Brinzolamide", "Taste and stinging."),
            ("Betaxolol", "Cardiac and respiratory cautions.")]),

dict(q="Which cholinergic agonist is used in the SURGICAL setting?",
     ans="Acetylcholine", src=("OPH", 72),
     why="The surgical agent among the three cholinergic agonists.",
     wrong=[("Pilocarpine", "Used topically outside surgery."),
            ("Carbachol", "Used topically outside surgery."),
            ("Tropicamide", "A cycloplegic antimuscarinic, which does the opposite.")]),

dict(q="A patient's pressure is not controlled on one agent. What is the principle behind adding a second?",
     ans="Choose a DIFFERENT mechanism, for synergy and fewer drops", src=("OPH", 73),
     why="Targeting multiple routes lowers pressure synergistically, and fewer drops improves compliance. Adding a drug of the same category would be the wrong move.",
     wrong=[("Choose an agent of the same class at a higher strength", "Same mechanism gives no synergy."),
            ("Add a topical glucocorticoid", "Steroids RAISE intraocular pressure."),
            ("Add a topical vasoconstrictor", "It has no role in glaucoma.")]),

dict(q="What is the general goal of glaucoma therapy, in terms of pressure?",
     ans="A 20 to 30 per cent reduction", src=("OPH", 74),
     why="And therapy can be started in one eye to judge efficacy and tolerability.",
     wrong=[("A 50 per cent reduction", "Beyond the stated goal."),
            ("Any reduction at all", "A specific target is given."),
            ("Normalising to below 10 mmHg", "Below the normal range, which starts at about 10.")]),

dict(q="Which patients with ocular hypertension are treated rather than monitored?",
     ans="Those WITH risk factors", src=("OPH", 74),
     why="Those without risk factors are monitored until glaucomatous changes occur.",
     wrong=[("All patients with raised pressure", "Those without risk factors are monitored."),
            ("Only those already blind in one eye", "Not the stated rule."),
            ("Only those under 40", "Age is not the stated criterion.")]),

dict(q="Which ocular anaesthetic leaves the eye numb for 10 to 20 minutes with NO BLINK REFLEX?",
     ans="Proparacaine", src=("OPH", 75),
     why="True of both ocular anaesthetics, and the reason you must not write prescriptions for them.",
     wrong=[("Tropicamide", "A cycloplegic; it dilates rather than anaesthetises."),
            ("Phenylephrine", "A sympathomimetic mydriatic."),
            ("Fluorescein", "A diagnostic stain.")]),

dict(q="Which ocular agents should you NOT write prescriptions for?",
     ans="Tetracaine", src=("OPH", 75),
     why="The ocular anaesthetics. Used in clinic for tonometry, foreign body removal and superficial corneal surgery, but not sent home.",
     wrong=[("Latanoprost", "A chronic glaucoma therapy, prescribed routinely."),
            ("Olopatadine", "An antihistamine, prescribed routinely."),
            ("Erythromycin", "An antibiotic ointment, prescribed routinely.")]),

dict(q="Which class competitively blocks muscarinic receptors to produce mydriasis for a fundoscopic examination?",
     ans="Tropicamide", src=("OPH", 76),
     why="The antimuscarinic cycloplegics, with atropine and cyclopentolate. Also used in uveitis to prevent synechiae and relieve ciliary spasm.",
     wrong=[("Phenylephrine", "A sympathomimetic, also producing mydriasis but by a different mechanism."),
            ("Pilocarpine", "A cholinergic agonist, which CONSTRICTS the pupil."),
            ("Proparacaine", "An anaesthetic.")]),

dict(q="A pupil dilated with which agent stays MORE REACTIVE TO LIGHT?",
     ans="Phenylephrine", src=("OPH", 77),
     why="The sympathomimetic mydriatic leaves more light reactivity than the antimuscarinics do.",
     wrong=[("Atropine", "An antimuscarinic; less reactive to light."),
            ("Cyclopentolate", "An antimuscarinic; less reactive to light."),
            ("Tropicamide", "An antimuscarinic; less reactive to light.")]),

dict(q="Which agent reveals epithelial defects of the cornea and conjunctiva?",
     ans="Fluorescein", src=("OPH", 78),
     why="Used for anterior segment staining and disclosing corneal injury.",
     wrong=[("Proparacaine", "An anaesthetic, often used alongside it but not the stain."),
            ("Tropicamide", "A cycloplegic."),
            ("Phenylephrine", "A mydriatic.")]),

dict(q="What is the normal range of intraocular pressure?",
     ans="About 10 to 21 mmHg", src=("OPH", 61),
     why="Ocular hypertension is a pressure above normal WITHOUT optic nerve damage or visual field loss.",
     wrong=[("About 30 to 40 mmHg", "Well above normal."),
            ("About 2 to 8 mmHg", "Below the normal range."),
            ("About 40 to 60 mmHg", "The range of an acute angle-closure spike.")]),

dict(q="Glaucoma drugs focus on which type, and why?",
     ans="Open angle — that is where drug therapy works", src=("OPH", 60),
     why="Angle-closure is an abrupt, emergent blockage of the drainage canal, usually with acute pain, and is not primarily a drug problem.",
     wrong=[("Closed angle, because it is more dangerous", "It is more urgent, but the drugs are aimed at open angle."),
            ("Both equally", "Drug therapy is aimed at open angle specifically."),
            ("Neither — glaucoma is surgical", "Drug therapy is the mainstay in open angle.")]),

dict(q="Which two routes lower intraocular pressure, and which class does BOTH?",
     ans="Brimonidine — it increases outflow AND decreases production", src=("OPH", 64),
     why="Alpha adrenergic agonists appear on both lists. Prostaglandins and cholinergics increase outflow; beta blockers and carbonic anhydrase inhibitors decrease production.",
     wrong=[("Latanoprost — it does both", "Prostaglandins increase outflow only."),
            ("Timolol — it does both", "Beta blockers decrease production only."),
            ("Dorzolamide — it does both", "Carbonic anhydrase inhibitors decrease production only.")]),
]
