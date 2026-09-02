# -*- coding: utf-8 -*-
"""Rapid-drill bank: facts that belong to a whole CLASS, not one drug.

Jaxon, 2026-09-02: "If theres stuff specific to a whole class you can make
drill questions for those."

So every option here is a class name, which is the one case where the
one-drug-per-choice rule does not apply -- the stem asks for a class.

Built only from class-level facts the other five drills do NOT already ask.
Roughly two dozen class facts were still unused after those sets; this bank is
25 questions rather than a padded 30 because that is how many there were.
"""
ITEMS = [
dict(q="Which class must be separated from antacids, iron and dairy because it chelates with cations?",
     ans="Tetracyclines", src=("L1", 63),
     why="They chelate with cations, so the dose has to be spaced away from antacids, iron and dairy.",
     wrong=[("Macrolides", "No cation chelation."),
            ("Penicillins", "No cation chelation."),
            ("Cephalosporins", "No cation chelation.")]),

dict(q="Which class must be avoided in children under eight years old?",
     ans="Tetracyclines", src=("L1", 63),
     why="Under eight, because of tooth discolouration and depressed skeletal growth.",
     wrong=[("Macrolides", "Used freely in children."),
            ("Cephalosporins", "Used freely in children."),
            ("Penicillins", "Used freely in children.")]),

dict(q="Which class is used with caution in patients under eighteen?",
     ans="Fluoroquinolones", src=("L1", 79),
     why="Caution under 18, because of the tendon and cartilage effects.",
     wrong=[("Macrolides", "No paediatric age restriction of this kind."),
            ("Cephalosporins", "No age restriction."),
            ("Aminoglycosides", "Monitored for renal and ear toxicity, not restricted by age this way.")]),

dict(q="Dizziness, insomnia and somnolence — central nervous system toxicity — belong to which class?",
     ans="Fluoroquinolones", src=("L1", 79),
     why="Central toxicity sits alongside the tendon rupture and peripheral neuropathy.",
     wrong=[("Tetracyclines", "Affect teeth, bone and photosensitivity."),
            ("Cephalosporins", "No characteristic central toxicity."),
            ("Polymyxins", "Neurotoxic, but through the black box warning rather than this picture.")]),

dict(q="Gastrointestinal upset that is worst with erythromycin, especially in children and young adults, points to which class?",
     ans="Macrolides", src=("L1", 57),
     why="Nausea, diarrhoea and abdominal pain, worse with erythromycin than with the newer members.",
     wrong=[("Penicillins", "Cause diarrhoea, but without the erythromycin gradient."),
            ("Tetracyclines", "Cause oesophageal irritation rather than this."),
            ("Aminoglycosides", "Given parenterally; the gut is not the issue.")]),

dict(q="Interstitial nephritis with haematuria and crystalluria belongs to which class?",
     ans="Aminopenicillins", src=("L1", 21),
     why="Alongside hepatic dysfunction, Clostridium difficile infection and the hypersensitivity spectrum.",
     wrong=[("Macrolides", "Cause cholestatic hepatitis, not interstitial nephritis."),
            ("Aminoglycosides", "Cause tubular injury, but the picture described is the penicillin one."),
            ("Fluoroquinolones", "Affect tendons and nerves.")]),

dict(q="Which class is mostly renally eliminated, so its dosing changes with kidney function?",
     ans="Cephalosporins", src=("L1", 30),
     why="Mostly renally eliminated — which is why the interval is stretched in renal impairment.",
     wrong=[("Macrolides", "Cleared hepatically."),
            ("Allylamines", "Antifungals, cleared hepatically."),
            ("Topical corticosteroids", "Not systemically dosed at all.")]),

dict(q="Tachycardia, headache, insomnia, low potassium and low magnesium describe which antifungal class?",
     ans="Echinocandins", src=("L1", 109),
     why="Caspofungin, micafungin and anidulafungin, which also cause blood dyscrasias.",
     wrong=[("Azoles", "Their signature problems are drug interactions and, for some, visual or QT effects."),
            ("Polyenes", "Amphotericin B gives fever, chills and hypotension."),
            ("Allylamines", "Used superficially, with little systemic effect.")]),

dict(q="Which antifungal class is used in the febrile neutropenic patient who is not responding to antibiotics?",
     ans="Echinocandins", src=("L1", 109),
     why="Given when antibiotics have not worked, and for aspergillosis that has failed itraconazole or amphotericin.",
     wrong=[("Allylamines", "Only for superficial dermatophytes."),
            ("Topical azoles", "Topical use only."),
            ("Topical antifungals", "Topical use only.")]),

dict(q="Which class treats athlete's foot, ringworm, jock itch and onychomycosis as well as the systemic mycoses?",
     ans="Azoles", src=("L1", 102),
     why="The breadth is the point: superficial tinea through to Candida, Cryptococcus, Blastomyces, Histoplasma, Coccidioides and Aspergillus.",
     wrong=[("Echinocandins", "Chiefly Candida and Aspergillus, and not superficial disease."),
            ("Polyenes", "Amphotericin B is systemic, not for tinea."),
            ("Topical corticosteroids", "Would make a fungal infection worse.")]),

dict(q="Use of which class is expected to rise because of increasing multidrug resistance?",
     ans="Polymyxins", src=("L1", 88),
     why="Old, toxic, and coming back because gram-negative resistance is leaving fewer options.",
     wrong=[("Penicillins", "Losing ground to resistance, not gaining."),
            ("Macrolides", "Losing ground to resistance."),
            ("Tetracyclines", "Not the class named here.")]),

dict(q="Which class covers gram-negative organisms only?",
     ans="Polymyxins", src=("L1", 88),
     why="Gram-negative only, which is why they are reserved for resistant gram-negative infection.",
     wrong=[("Macrolides", "Cover gram-positives and atypicals."),
            ("Cephalosporins", "Cover both, varying by generation."),
            ("Allylamines", "Antifungals.")]),

dict(q="Anxiety, tremor and headache, with poor penetration into the central nervous system, describe which class?",
     ans="Catecholamines", src=("L3", 79),
     why="Epinephrine, norepinephrine, isoproterenol and dopamine — peripheral effects dominate because they do not cross well.",
     wrong=[("Alpha-1 blockers", "Cause dizziness, congestion and drowsiness."),
            ("Beta-1 selective blockers", "Cause bradycardia and fatigue."),
            ("Antimuscarinics", "Cross readily and cause central delirium.")]),

dict(q="Which class is used during orthopaedic surgery for fracture alignment and dislocation correction?",
     ans="Nondepolarizing blockers", src=("L3", 63),
     why="Adjuvants in anaesthesia — intubation, and relaxing muscle enough to reduce a fracture or dislocation.",
     wrong=[("Cholinergic agonists", "Increase muscle activity rather than relaxing it."),
            ("Cholinesterase inhibitors", "Reverse blockade rather than produce it."),
            ("Antimuscarinics", "Have no effect at the neuromuscular junction.")]),

dict(q="Poisoning by which group produces EITHER nicotinic OR muscarinic signs?",
     ans="Organophosphates", src=("L3", 42),
     why="Either picture can dominate, which is why the presentation varies so much.",
     wrong=[("Alpha-1 blockers", "Produce orthostatic hypotension only."),
            ("Beta blockers", "Produce bradycardia and bronchospasm."),
            ("Nondepolarizing blockers", "Produce flaccid paralysis alone.")]),

dict(q="Which vehicle makes a topical corticosteroid MOST potent?",
     ans="Ointment", src=("L2", 39),
     why="Ointment beats cream, which beats lotion — the vehicle changes the potency, not just the feel.",
     wrong=[("Cream", "Middle of the three."),
            ("Lotion", "The least potent of the three."),
            ("Gel", "Not part of the ordering given.")]),

dict(q="Which agent inactivates tretinoin if the two are applied together?",
     ans="Benzoyl peroxide", src=("L2", 24),
     why="Benzoyl peroxide inactivates tretinoin, so they are applied at different times of day.",
     wrong=[("Clindamycin", "Combined with benzoyl peroxide deliberately, to slow resistance."),
            ("Azelaic acid", "No such interaction."),
            ("Tacrolimus", "Used for atopic dermatitis, not acne.")]),

dict(q="Which class is losing efficacy over time because of Propionibacterium acnes resistance?",
     ans="Topical antibiotics", src=("L2", 23),
     why="Which is why they are paired with benzoyl peroxide rather than used alone.",
     wrong=[("Topical retinoids", "No bacterial resistance issue."),
            ("Topical corticosteroids", "Not antibacterial."),
            ("Topical immunomodulators", "Not antibacterial.")]),

dict(q="Which class produces salivation, flushing, falling blood pressure, abdominal pain, diarrhoea and bronchospasm?",
     ans="Cholinesterase inhibitors", src=("L3", 38),
     why="The muscarinic picture from raising acetylcholine at every synapse.",
     wrong=[("Nondepolarizing blockers", "Produce flaccid paralysis with no autonomic picture at all."),
            ("Alpha-1 blockers", "Produce orthostatic hypotension and congestion."),
            ("Antimuscarinics", "Produce the opposite — dry, hot, flushed and delirious.")]),

dict(q="“Dry as a bone, blind as a bat, red as a beet, mad as a hatter” describes toxicity from which class?",
     ans="Antimuscarinics", src=("L3", 50),
     why="The anticholinergic toxidrome, each phrase naming one blocked muscarinic effect.",
     wrong=[("Cholinesterase inhibitors", "Give the wet, slow, constricted opposite."),
            ("Catecholamines", "Give anxiety and tremor without the dryness and flush."),
            ("Nondepolarizing blockers", "Give paralysis with no autonomic picture.")]),

dict(q="Which class requires less frequent dosing as renal function falls?",
     ans="Penicillins", src=("L1", 22),
     why="Renally cleared, so the interval stretches as clearance drops.",
     wrong=[("Macrolides", "Cleared hepatically."),
            ("Allylamines", "Cleared hepatically."),
            ("Topical retinoids", "Not systemically dosed.")]),

dict(q="Hepatic dysfunction with jaundice and raised transaminases belongs to which penicillin group?",
     ans="Aminopenicillins", src=("L1", 21),
     why="Hepatic dysfunction, hepatitis and jaundice with raised AST, ALT, bilirubin and alkaline phosphatase.",
     wrong=[("Penicillinase-resistant penicillins", "Monitored for hepatic toxicity too, but the described enzyme picture is the aminopenicillin one."),
            ("Cephalosporins", "Chiefly allergic and gastrointestinal."),
            ("Carbapenems", "Chiefly seizures.")]),

dict(q="Which class is second line for atopic dermatitis, after topical steroids?",
     ans="Topical immunomodulators", src=("L2", 43),
     why="Tacrolimus and pimecrolimus, used when steroids are not appropriate to continue.",
     wrong=[("Topical retinoids", "Used for acne and photoageing."),
            ("Topical antibiotics", "Used for acne and skin infection."),
            ("Topical antifungals", "Used for fungal infection.")]),

dict(q="Which class must be applied with a warning about severe sunburn?",
     ans="Topical retinoids", src=("L2", 24),
     why="Photosensitivity and severe sunburn, which is why they are applied at night and paired with sun protection.",
     wrong=[("Topical corticosteroids", "Cause atrophy rather than photosensitivity."),
            ("Topical immunomodulators", "Cause burning on application, not photosensitivity."),
            ("Topical antibiotics", "No photosensitivity in the topical form.")]),

dict(q="Which class causes bronchospasm and so must be used cautiously in reactive airway disease?",
     ans="Cholinergic agonists", src=("L3", 31),
     why="Bronchospasm is the reason for caution — the airway constricts as secretions rise.",
     wrong=[("Antimuscarinics", "Open the airway; they are used in chronic obstructive pulmonary disease."),
            ("Beta-2 agonists", "Open the airway; they are the rescue treatment in asthma."),
            ("Alpha-1 blockers", "Have no bronchial effect.")]),
]
