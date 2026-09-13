# -*- coding: utf-8 -*-
"""Rapid-drill bank: ocular anti-infectives.

One fact, four drug names, every wrong choice from the same family so it is a
real discrimination rather than a category guess. No doses -- Dr. Wood does not
ask for them.

SCOPE FROM THE RECORDING. He de-scoped three things in this section and none of
them is drilled here:
  - indications for the individual antibiotics -- "don't worry so much about
    indications for use ... a lot of them have a lot of crossover"
  - formulations -- "I don't care that you memorize that necessarily, with some
    exceptions" (the exceptions he named ARE drilled)
  - which agent causes irritation or hypersensitivity -- "don't memorize which
    ones cause eye irritation or hypersensitivity. Any of these can do that."
What IS drilled is what separates one agent from its neighbours.
"""
ITEMS = [
dict(q="Which ophthalmic antibiotic is soothing on an inflamed eye, so it may be used even when bacterial infection is not confirmed?",
     ans="Erythromycin", src=("OPH", 17),
     why="It is soothing on the inflamed eye, and it is dirt cheap.",
     wrong=[("Azithromycin", "Considerably more expensive and not used as often clinically."),
            ("Ciprofloxacin", "A fluoroquinolone, reserved more for ulcers and Pseudomonas."),
            ("Tobramycin", "An aminoglycoside; its risk is corneal ulceration with continued use.")]),

dict(q="Which ophthalmic antibiotic is used for prophylaxis of ophthalmia neonatorum?",
     ans="Erythromycin", src=("OPH", 14),
     why="The 0.5% ointment, for superficial conjunctival or corneal infection and for newborn prophylaxis.",
     wrong=[("Gatifloxacin", "A fluoroquinolone indicated for conjunctivitis."),
            ("Sulfacetamide", "Used for conjunctivitis and other superficial infections."),
            ("Bacitracin", "Covers a broad list of lid and surface infections, but not this prophylaxis.")]),

dict(q="Which ophthalmic antibiotic is considerably more expensive and given less frequently, so it is not used as often clinically?",
     ans="Azithromycin", src=("OPH", 17),
     why="Twice a day against four or more for erythromycin, but the cost keeps it off the shelf.",
     wrong=[("Erythromycin", "The cheap old ointment, and the usual first reach."),
            ("Bacitracin", "An inexpensive ointment."),
            ("Sulfacetamide", "Inexpensive, and available as solution or ointment.")]),

dict(q="Which ophthalmic antibiotic leaves a white precipitate in about one in six patients?",
     ans="Ciprofloxacin", src=("OPH", 21),
     why="A white precipitate in roughly 17%, which is specific to it among the fluoroquinolones.",
     wrong=[("Moxifloxacin", "A fluoroquinolone without that precipitate."),
            ("Ofloxacin", "A fluoroquinolone without that precipitate."),
            ("Levofloxacin", "A fluoroquinolone without that precipitate.")]),

dict(q="Which ophthalmic antibiotic class must be avoided in a patient with a sulfonamide allergy?",
     ans="Sulfacetamide", src=("OPH", 19),
     why="It is a sulfonamide, so a sulfa allergy rules it out.",
     wrong=[("Bacitracin", "No sulfonamide component."),
            ("Tobramycin", "An aminoglycoside."),
            ("Trimethoprim with polymyxin B", "Trimethoprim is a folate-pathway drug but not a sulfonamide.")]),

dict(q="Which ophthalmic antibiotic inhibits bacterial cell wall synthesis by preventing transfer of mucopeptides into the growing wall?",
     ans="Bacitracin", src=("OPH", 20),
     why="A cell wall agent, which sets it apart from the protein-synthesis and DNA agents alongside it.",
     wrong=[("Erythromycin", "Blocks transpeptidation at the 50S ribosome."),
            ("Gentamicin", "Binds the 30S subunit."),
            ("Ofloxacin", "Inhibits DNA gyrase and topoisomerase IV.")]),

dict(q="Which ophthalmic antibiotic class binds the 50S ribosome and blocks transpeptidation?",
     ans="Erythromycin", src=("OPH", 15),
     why="The macrolide mechanism: no protein synthesis, so the bacterium dies.",
     wrong=[("Tobramycin", "Binds the 30S subunit instead."),
            ("Ciprofloxacin", "Targets DNA gyrase and topoisomerase IV."),
            ("Sulfacetamide", "Antagonises PABA to block folic acid synthesis.")]),

dict(q="Which ophthalmic antibiotic class binds the 30S subunit to interfere with protein synthesis?",
     ans="Gentamicin", src=("OPH", 23),
     why="The aminoglycoside mechanism. Its ocular risk is corneal ulceration and reactive keratoconjunctivitis after several days.",
     wrong=[("Azithromycin", "A macrolide, acting at the 50S."),
            ("Bacitracin", "A cell wall agent."),
            ("Moxifloxacin", "A fluoroquinolone acting on DNA gyrase.")]),

dict(q="Which ophthalmic antibiotic class inhibits DNA gyrase and topoisomerase IV, breaking double-stranded DNA?",
     ans="Moxifloxacin", src=("OPH", 21),
     why="The fluoroquinolone mechanism: supercoiled DNA cannot relax, and the strand breaks.",
     wrong=[("Erythromycin", "Acts at the 50S ribosome."),
            ("Gentamicin", "Acts at the 30S subunit."),
            ("Natamycin", "An antifungal that binds sterol in the fungal membrane.")]),

dict(q="Which ophthalmic agent antagonises PABA to block folic acid synthesis?",
     ans="Sulfacetamide", src=("OPH", 19),
     why="Interfering with folate synthesis stops bacterial growth.",
     wrong=[("Trimethoprim", "Also a folate-pathway drug, but it inhibits REDUCTION of folic acid to tetrahydrofolate."),
            ("Polymyxin B", "Binds membrane phospholipids and lets the contents leak out."),
            ("Bacitracin", "Blocks cell wall synthesis.")]),

dict(q="Which agent binds phospholipids on the bacterial cytoplasmic membrane and lets intracellular contents leak out?",
     ans="Polymyxin B", src=("OPH", 18),
     why="A membrane-permeability agent, partnered with trimethoprim in the combination drop.",
     wrong=[("Trimethoprim", "Its partner in the same product, but it blocks reduction of folic acid to tetrahydrofolate."),
            ("Bacitracin", "Blocks cell wall synthesis, not membrane permeability."),
            ("Erythromycin", "A ribosomal agent.")]),

dict(q="Which ophthalmic antibiotic class is PREFERRED for corneal ulcers or suspected Pseudomonas aeruginosa?",
     ans="Moxifloxacin", src=("OPH", 22),
     why="The fluoroquinolones are the reach for ulcers and for the gram-negative rod, though they are expensive and resistance is emerging.",
     wrong=[("Erythromycin", "Soothing and cheap, but not the choice for an ulcer or Pseudomonas."),
            ("Bacitracin", "A surface agent for conjunctivitis and lid disease."),
            ("Sulfacetamide", "Used for conjunctivitis and other superficial infection.")]),

dict(q="A contact lens wearer has conjunctivitis and keratitis has been excluded. Which antibiotic class is preferred, and why?",
     ans="Ciprofloxacin", src=("OPH", 22),
     why="Fluoroquinolones, because contact lens wearers are at high risk for Pseudomonas.",
     wrong=[("Erythromycin", "Does not cover the organism the lens wearer is at risk from."),
            ("Bacitracin", "Not the agent chosen for this risk."),
            ("Azithromycin", "Cost and spectrum both argue against it here.")]),

dict(q="Which ophthalmic antibiotic class carries a risk of corneal ulceration and reactive keratoconjunctivitis after several days of use?",
     ans="Tobramycin", src=("OPH", 23),
     why="The aminoglycoside-specific risk, and one of the few adverse effects worth attaching to a single class.",
     wrong=[("Erythromycin", "Soothing rather than ulcerating."),
            ("Bacitracin", "No such specific risk."),
            ("Azithromycin", "No such specific risk.")]),

dict(q="Which ophthalmic antibiotic class is associated with an unpleasant taste after instillation?",
     ans="Levofloxacin", src=("OPH", 21),
     why="A fluoroquinolone effect, and it reflects nasolacrimal drainage carrying drug to the throat.",
     wrong=[("Bacitracin", "An ointment, and no taste effect is attributed to it."),
            ("Erythromycin", "No taste effect attributed."),
            ("Gentamicin", "No taste effect attributed.")]),

dict(q="Which is the ONLY commercially available ophthalmic antifungal?",
     ans="Natamycin", src=("OPH", 30),
     why="Everything else has to be compounded by a specialty pharmacy or given systemically.",
     wrong=[("Amphotericin B", "Used ophthalmically but not as a commercially available ophthalmic product."),
            ("Fluconazole", "Given orally or intravenously."),
            ("Miconazole", "A topical solution that must be specially prepared.")]),

dict(q="Which antifungal increases fungal cell membrane permeability by binding sterol?",
     ans="Natamycin", src=("OPH", 32),
     why="It covers Aspergillus, Candida, Cephalosporium, Fusarium and Penicillium.",
     wrong=[("Fluconazole", "An imidazole, working on the synthesis of ergosterol rather than binding it directly."),
            ("Trifluridine", "An antiviral."),
            ("Ganciclovir", "An antiviral.")]),

dict(q="Which topical antiviral interferes with viral replication by inhibiting thymidylate synthetase and taking the place of thymidine in viral DNA?",
     ans="Trifluridine", src=("OPH", 27),
     why="Used for herpes simplex keratoconjunctivitis. Its ocular toxicity is punctate keratopathy.",
     wrong=[("Ganciclovir", "Competitively inhibits deoxyguanosine triphosphate binding to DNA polymerase."),
            ("Acyclovir", "Given orally or intravenously for zoster ophthalmicus and simplex iridocyclitis."),
            ("Foscarnet", "Intravenous, for cytomegalovirus retinitis.")]),

dict(q="Which antiviral competitively inhibits the binding of deoxyguanosine triphosphate to DNA polymerase?",
     ans="Ganciclovir", src=("OPH", 28),
     why="Used for herpetic keratitis, and for cytomegalovirus retinitis by intravitreal injection.",
     wrong=[("Trifluridine", "Inhibits thymidylate synthetase and substitutes for thymidine."),
            ("Valacyclovir", "Oral, for simplex keratitis and zoster ophthalmicus."),
            ("Cidofovir", "Intravenous, for cytomegalovirus retinitis.")]),

dict(q="Which antiviral is given INTRAVENOUSLY for cytomegalovirus retinitis?",
     ans="Foscarnet", src=("OPH", 26),
     why="Cytomegalovirus retinitis is the intravenous indication, alongside ganciclovir and cidofovir.",
     wrong=[("Trifluridine", "Topical only, as a 1% solution."),
            ("Famciclovir", "Oral, for simplex keratitis and zoster ophthalmicus."),
            ("Natamycin", "An antifungal.")]),

dict(q="Adenoviral conjunctivitis is diagnosed. Which antiviral is indicated?",
     ans="None — there is no antiviral for adenoviral conjunctivitis", src=("OPH", 25),
     why="It runs a self-limited course and is treated with symptomatic relief of irritation.",
     wrong=[("Trifluridine", "For herpes simplex keratitis and keratoconjunctivitis, not adenovirus."),
            ("Ganciclovir", "For herpetic keratitis and cytomegalovirus retinitis."),
            ("Valacyclovir", "For simplex keratitis and zoster ophthalmicus.")]),

dict(q="Which route of ocular drug delivery circumvents absorption entirely for an immediate local effect?",
     ans="Intravitreal injection or device", src=("OPH", 5),
     why="Used for endophthalmitis, retinitis and age-related macular degeneration. Its limitation is retinal toxicity.",
     wrong=[("Topical", "Prompt but depends on formulation, and much is lost to nasolacrimal drainage."),
            ("Subconjunctival injection", "Prompt or sustained depending on formulation."),
            ("Intraocular (intracameral) injection", "Prompt, but with a relatively short duration of action.")]),

dict(q="Which ocular route risks nasal mucosal toxicity and systemic side effects through nasolacrimal absorption?",
     ans="Topical", src=("OPH", 5),
     why="Convenient, economical and relatively safe, but what drains down the nasolacrimal duct is absorbed systemically and skips first-pass metabolism.",
     wrong=[("Intravitreal injection", "Its limitation is retinal toxicity."),
            ("Retrobulbar injection", "Its risks are local: tissue injury, globe perforation, optic nerve trauma."),
            ("Intracameral injection", "Corneal and intraocular toxicity, with a short duration.")]),

dict(q="Which prodrug is converted in the eye to epinephrine?",
     ans="Dipivefrin", src=("OPH", 10),
     why="One of the two ocular prodrug examples; the other is latanoprost, converted to prostaglandin F2 alpha.",
     wrong=[("Latanoprost", "Also a prodrug, but converted to prostaglandin F2 alpha."),
            ("Brimonidine", "An alpha-2 agonist given as the active drug."),
            ("Timolol", "A beta blocker given as the active drug.")]),

dict(q="Which drug accumulates in the eye and produces a bull's eye lesion?",
     ans="Chloroquine", src=("OPH", 10),
     why="The example given of a drug distributing into and accumulating in the eye.",
     wrong=[("Latanoprost", "Changes eyelash length and iris colour, not a bull's eye lesion."),
            ("Timolol", "Its risks are systemic beta blockade."),
            ("Dorzolamide", "Bitter taste and stinging on administration.")]),

dict(q="Absorption across the cornea is governed by which law?",
     ans="Fick's law", src=("OPH", 8),
     why="Transcorneal absorption is necessary for local ocular effect, and its rate depends most on the concentration gradient.",
     wrong=[("Poiseuille's law", "Governs flow through a tube, and appears in the nasal airway rather than here."),
            ("Starling's law", "Describes cardiac output against filling."),
            ("Laplace's law", "Relates wall tension to pressure and radius.")]),
]
