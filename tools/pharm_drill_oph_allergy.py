# -*- coding: utf-8 -*-
"""Rapid-drill bank: ocular allergy, inflammation and dry eye.

One fact, four drug names, no doses.

THE REBOUND HYPERAEMIA ITEM IS THE ONE HE SAID HE WOULD ASK. In the recording:
"I will ask this question ... there's rebound hyperemia ... star that, underline
it, highlight it. A lot of people still get it wrong every test. I don't know
why because I tell you explicitly, that's what I'm going to be asking about."
It is drilled three ways here -- the effect, the time limit, and the 72-hour
rule -- because that is the one fact in this lecture with a promise attached.
"""
ITEMS = [
dict(q="Which class of eye drop causes REBOUND HYPERAEMIA if used for too long?",
     ans="Naphazoline", src=("OPH", 48),
     why="The topical vasoconstrictors. He flagged this one explicitly as a question he would ask, and the same trap reappears with nasal sprays.",
     wrong=[("Olopatadine", "An antihistamine; its problems are irritation, headache and dryness."),
            ("Cromolyn", "A mast cell stabiliser; slow to work but no rebound."),
            ("Ketorolac", "An ophthalmic non-steroidal; no rebound effect.")]),

dict(q="A patient asks how long they may use a vasoconstrictor eye drop. What is the limit?",
     ans="Less than two weeks", src=("OPH", 48),
     why="Beyond that, rebound hyperaemia follows discontinuation. He called it a great counselling point.",
     wrong=[("Less than 72 hours", "72 hours is the point at which NO IMPROVEMENT should send them to a provider, not the usage limit."),
            ("Less than six weeks", "Far beyond the stated limit."),
            ("No limit", "Prolonged use is precisely the problem.")]),

dict(q="A patient using an over-the-counter vasoconstrictor drop has had no improvement. At what point should they stop and see a provider?",
     ans="72 hours", src=("OPH", 48),
     why="No improvement within 72 hours means something more serious may be going on.",
     wrong=[("Two weeks", "Two weeks is the limit on DURATION of use, not the review point for failure."),
            ("24 hours", "Earlier than the stated point."),
            ("Seven days", "Later than the stated point.")]),

dict(q="Topical vasoconstrictors act on which receptor LOCALLY in the eye?",
     ans="Alpha 1", src=("OPH", 49),
     why="Locally alpha 1, which constricts the conjunctival vessels. Systemically these imidazolines target alpha 2 instead, which is what makes an accidental ingestion dangerous.",
     wrong=[("Alpha 2", "That is the SYSTEMIC target, and the reason ingestion matters."),
            ("Beta 1", "Cardiac, and the concern with beta blocker drops."),
            ("Beta 2", "Pulmonary, and the concern with nonselective beta blocker drops.")]),

dict(q="Which ophthalmic antihistamine is available over the counter?",
     ans="Ketotifen", src=("OPH", 43),
     why="The over-the-counter agent among the ophthalmic antihistamines.",
     wrong=[("Azelastine", "An ophthalmic antihistamine, but not the one marked over the counter."),
            ("Bepotastine", "Also an ophthalmic antihistamine, but prescription only."),
            ("Emedastine", "Another prescription antihistamine in the same list.")]),

dict(q="H1 receptor blockers are not really antagonists. What are they?",
     ans="Inverse agonists", src=("OPH", 42),
     why="They cause histamine receptor INACTIVATION, and they remain competitive with histamine.",
     wrong=[("Non-competitive antagonists", "They are still competitive with histamine."),
            ("Partial agonists", "Not the described relationship."),
            ("Irreversible blockers", "They are competitive and reversible.")]),

dict(q="Which class works within MINUTES and is typically preferred for ocular allergy?",
     ans="Olopatadine", src=("OPH", 44),
     why="Antihistamines have an onset within minutes, are dosed once or twice daily, and are preferred over mast cell stabilisers.",
     wrong=[("Cromolyn", "A mast cell stabiliser, needing 5 to 14 days and four-times-daily dosing."),
            ("Lodoxamide", "Another mast cell stabiliser, so it shares the slow start."),
            ("Nedocromil", "The third mast cell stabiliser, and no faster than the others.")]),

dict(q="Which class is NOT useful for acute allergy symptoms?",
     ans="Cromolyn", src=("OPH", 47),
     why="Mast cell stabilisers need 5 to 14 days for full efficacy, so they are useless in the moment. They suit predictable seasonal allergy in patients who cannot tolerate other therapy.",
     wrong=[("Ketotifen", "An antihistamine, and the over-the-counter one; it works within minutes."),
            ("Naphazoline", "A vasoconstrictor, acting quickly but limited to two weeks."),
            ("Epinastine", "A prescription antihistamine, also fast.")]),

dict(q="Which class inhibits mast cell degranulation, limiting release of histamine, tryptase and prostaglandin D2?",
     ans="Nedocromil", src=("OPH", 45),
     why="The mast cell stabilisers, which also dampen mediator release from basophils, eosinophils and neutrophils.",
     wrong=[("Alcaftadine", "An antihistamine, blocking the receptor rather than the release."),
            ("Bromfenac", "A non-steroidal, blocking cyclooxygenase."),
            ("Loteprednol", "A glucocorticoid, acting on phospholipase A2.")]),

dict(q="How long should a patient be given to judge the FULL effect of an ophthalmic antihistamine?",
     ans="Two weeks", src=("OPH", 44),
     why="Onset is within minutes, but full efficacy takes about two weeks to assess.",
     wrong=[("Two days", "Too short to judge full efficacy."),
            ("Six weeks", "Longer than the stated period."),
            ("One day", "Far too short.")]),

dict(q="Which ophthalmic class blocks cyclooxygenase, stopping conversion of arachidonic acid to prostaglandins and thromboxanes?",
     ans="Ketorolac", src=("OPH", 50),
     why="The ophthalmic non-steroidals. The mechanism is the same whether the drug is taken for a headache or put in the eye.",
     wrong=[("Prednisolone", "A glucocorticoid, inhibiting phospholipase A2 further upstream."),
            ("Cyclosporine", "An immunomodulator, inhibiting interleukin 2."),
            ("Cromolyn", "A mast cell stabiliser.")]),

dict(q="What are the ophthalmic non-steroidals indicated for?",
     ans="Bromfenac — postoperative inflammation and pain, and allergic conjunctivitis", src=("OPH", 51),
     why="And they are NOT routinely recommended for conjunctivitis generally.",
     wrong=[("Natamycin — fungal keratitis", "An antifungal, and not a non-steroidal."),
            ("Timolol — open-angle glaucoma", "A beta blocker for glaucoma."),
            ("Trifluridine — herpes simplex keratitis", "A topical antiviral.")]),

dict(q="Which ophthalmic class can RAISE intraocular pressure as an adverse effect, alongside lacrimation and keratitis?",
     ans="Nepafenac", src=("OPH", 51),
     why="The ophthalmic non-steroidals. Glucocorticoids raise pressure too, but the non-steroidal list is lacrimation, keratitis, raised pressure and irritation.",
     wrong=[("Cromolyn", "Irritation, unpleasant taste and headache."),
            ("Ketotifen", "Irritation, headache and increased dryness."),
            ("Natamycin", "Ocular irritation only.")]),

dict(q="Which class suppresses the LATE phase allergic reaction by inhibiting phospholipase A2?",
     ans="Prednisolone", src=("OPH", 52),
     why="The glucocorticoids, cutting off arachidonic acid derived mediators at source. They also inhibit fibrin and collagen deposition, reducing scar formation.",
     wrong=[("Ketorolac", "A non-steroidal, acting downstream at cyclooxygenase."),
            ("Olopatadine", "An antihistamine, blocking the receptor."),
            ("Lodoxamide", "A mast cell stabiliser.")]),

dict(q="Which glucocorticoid is a SOFT steroid with a lower risk of raising intraocular pressure?",
     ans="Loteprednol", src=("OPH", 55),
     why="One of the three soft steroids, with fluorometholone and rimexolone.",
     wrong=[("Dexamethasone", "A conventional steroid, carrying the full pressure risk."),
            ("Prednisolone", "Also conventional, and among the most used."),
            ("Difluprednate", "Conventional, and potent rather than soft.")]),

dict(q="Which ocular glucocorticoid is given by INTRAVITREAL injection?",
     ans="Triamcinolone", src=("OPH", 55),
     why="The intravitreal agent among the ophthalmic steroids.",
     wrong=[("Fluorometholone", "A soft steroid, and given topically rather than injected."),
            ("Rimexolone", "Also a soft steroid, applied to the surface."),
            ("Loteprednol", "The third soft steroid, also topical.")]),

dict(q="Ocular glucocorticoids are limited to a pulse of what length?",
     ans="Less than two weeks", src=("OPH", 54),
     why="Their risks accumulate: cataract, raised pressure and glaucoma, infection from reduced immune function, delayed wound healing, and corneal ulcers.",
     wrong=[("Less than six weeks", "Longer than the stated limit."),
            ("Less than 72 hours", "Shorter than the stated limit."),
            ("No limit", "The list of risks is precisely why there is one.")]),

dict(q="Which patients are at greater risk of raised intraocular pressure from ocular steroids?",
     ans="Those with a FAMILY HISTORY", src=("OPH", 54),
     why="Elevated pressure is more likely with a family history, alongside the other steroid risks.",
     wrong=[("Contact lens wearers", "Their particular risk is Pseudomonas infection."),
            ("Children under two", "That is the contraindication for alpha-2 agonists."),
            ("Patients with asthma", "That is the concern with nonselective beta blocker drops.")]),

dict(q="Which drug inhibits production and release of interleukin 2, reducing T cell activation, and is used for chronic dry eye?",
     ans="Cyclosporine", src=("OPH", 58),
     why="It reduces inflammatory markers in the lacrimal gland and increases tear production. Its commonest adverse effect is ocular burning.",
     wrong=[("Prednisolone", "A glucocorticoid, and not the dry-eye immunomodulator."),
            ("Ketorolac", "A non-steroidal."),
            ("Lodoxamide", "A mast cell stabiliser.")]),

dict(q="Cyclosporine eye drops are indicated for which condition?",
     ans="Keratoconjunctivitis sicca", src=("OPH", 58),
     why="Chronic dry eye associated with inflammation.",
     wrong=[("Bacterial conjunctivitis", "Treated with an ophthalmic antibiotic."),
            ("Open-angle glaucoma", "Treated with pressure-lowering agents."),
            ("Herpes simplex keratitis", "Treated with an antiviral.")]),

dict(q="Which systemic conditions manifest with dry eyes?",
     ans="Sjogren syndrome, rheumatoid arthritis, vitamin A deficiency and Stevens-Johnson syndrome", src=("OPH", 56),
     why="And the first rule of dry eye is to treat the underlying disease.",
     wrong=[("Asthma and chronic obstructive pulmonary disease", "Relevant to beta blocker drops, not to dry eye."),
            ("Diabetes and hypertension", "Not the listed dry-eye associations."),
            ("Hyperthyroidism and Graves disease", "Associated with proptosis rather than this list.")]),

dict(q="Which principal target cells drive the ocular hypersensitivity reaction?",
     ans="Mast cells and basophils", src=("OPH", 40),
     why="IgE binds their Fc receptors, and within seconds tyrosine kinases activate and histamine, platelet-activating factor and leukotrienes are released.",
     wrong=[("Neutrophils and macrophages", "Phagocytes, and not the principal cells here."),
            ("T cells and B cells", "Adaptive lymphocytes."),
            ("Eosinophils and dendritic cells", "Eosinophils are involved downstream, but these are not the principal pair.")]),
]
