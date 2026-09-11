# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- Ophthalmology, topic 1: delivery and anti-infectives.

Deck: Ophthalmology-2.pptx, Adam Wood PharmD DABAT, 79 slides.
Recording: pharm-ophthalmology-wood-2026-09-03 (82 min, pulled from YouTube).

THREE TOPICS, NOT FOUR, and not 2x30 on a fourth thin one. Dr. Wood rules out
most of what a 79-slide drug deck would otherwise supply:

  dosing          "not for memorization sake necessarily, because you can
                  always look up the dosing for a medication if you know which
                  drug you actually want to use in the first place"
  formulations    "I don't care that you memorize that necessarily"
  the indications "Don't worry so much about indications for use... a lot of
  table           them have a lot of crossover"
  which agent     "don't memorize which ones cause eye irritation or
  irritates       hypersensitivity. Any of these can do that"

So the testable surface is mechanism, drug CHOICE, and the handful of facts he
stops to make. Splitting into four topics would have meant padding back into
exactly the material he excluded. [[pharmacology_exam_spec]] already says class
before agent and no dosages; this lecture is the clearest case of it yet.

The correct answer is authored FIRST; pharm_oph_partition.py rotates it.
"""

QUESTIONS = [

{"topic": "Ocular drug delivery", "io": "Identify ophthalmic drug classes and commonly prescribed ophthalmic drugs",
 "slot": "mechanism",
 "q": "A drop instilled in the eye reaches the systemic circulation and causes a side effect elsewhere in the body. By which route did it get there, and what is the consequence for its metabolism?",
 "opts": [
  ["Nasolacrimal drainage, which avoids first-pass metabolism",
   "Correct. Drug draining through the nasolacrimal duct is absorbed across nasal mucosa straight into the systemic circulation, bypassing the liver's first pass. That is why a topical drop can produce a systemic effect out of proportion to its dose."],
  ["Transcorneal absorption, which avoids first-pass metabolism",
   "Transcorneal absorption is what produces the LOCAL ocular effect. It is the route you want for the eye, not the route that causes systemic exposure."],
  ["Nasolacrimal drainage, with extensive first-pass metabolism",
   "The route is right but the consequence is backwards — avoiding the portal circulation is precisely what makes this absorption efficient and the systemic effects notable."],
  ["Conjunctival absorption into the retinal circulation",
   "Not the described pathway; systemic absorption from an eye drop is a nasolacrimal phenomenon."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 8"},

{"topic": "Ocular drug delivery", "io": "Identify ophthalmic drug classes and commonly prescribed ophthalmic drugs",
 "slot": "mechanism",
 "q": "Why do gels, ointments and solid inserts increase the amount of drug absorbed compared with a simple solution?",
 "opts": [
  ["They prolong contact time in the cul-de-sac",
   "Correct. More time sitting in the cul-de-sac means more opportunity for transcorneal diffusion. Every formulation trick is aimed at the same variable — how long the drug stays in contact with the eye."],
  ["They increase the drug's lipid solubility",
   "Formulation changes the residence time, not the molecule. Solubility is a property of the drug itself."],
  ["They open tight junctions in the corneal epithelium",
   "Not how it works; absorption is governed by the concentration gradient across an intact cornea."],
  ["They reduce binding of drug to tear proteins",
   "Protein binding does affect absorption, but it is not how a gel or ointment works — the gain is contact time."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slides 6-7"},

{"topic": "Ocular drug delivery", "io": "Describe the mechanism of action of ophthalmic drugs",
 "slot": "mechanism",
 "q": "Latanoprost and dipivefrin are both given in an inactive form. What does the eye do with them?",
 "opts": [
  ["It metabolises them — they are prodrugs activated in the eye",
   "Correct. Some drugs are metabolised within the eye itself, which is exploited deliberately: dipivefrin becomes epinephrine and latanoprost becomes prostaglandin F2-alpha once inside."],
  ["It concentrates them in the ciliary body without altering them",
   "Accumulation happens with some drugs — chloroquine's bull's eye lesion is the example — but that is storage, not activation."],
  ["It excretes them unchanged into the aqueous humour",
   "That would deliver no active drug at all, which defeats the purpose of the prodrug design."],
  ["It binds them to tear proteins until they are displaced",
   "Tear protein binding limits absorption; it does not convert an inactive compound into an active one."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 10"},

{"topic": "Ocular antibiotics", "io": "Describe the mechanism of action of ophthalmic drugs",
 "slot": "mechanism",
 "q": "Erythromycin ointment and azithromycin solution share a mechanism. What is it?",
 "opts": [
  ["Inhibition of protein synthesis at the 50S ribosomal subunit",
   "Correct. The macrolides block transpeptidation at the 50S subunit, so RNA-dependent protein synthesis stops and the organism dies. Knowing the subunit is what separates them from the aminoglycosides."],
  ["Inhibition of protein synthesis at the 30S ribosomal subunit",
   "That is the aminoglycosides — gentamicin and tobramycin. Same broad target, different subunit, and the pairing is the point."],
  ["Inhibition of DNA gyrase and topoisomerase IV",
   "That is the fluoroquinolones, which break double-stranded DNA rather than interfering with the ribosome."],
  ["Inhibition of cell wall mucopeptide transfer",
   "That is bacitracin, which works on the wall rather than on protein synthesis."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 15"},

{"topic": "Ocular antibiotics", "io": "Describe the mechanism of action of ophthalmic drugs",
 "slot": "mechanism",
 "q": "Gentamicin and tobramycin act on the bacterial ribosome. At which subunit?",
 "opts": [
  ["The 30S subunit",
   "Correct. The aminoglycosides bind the 30S subunit and interfere with protein synthesis. The macrolides take the 50S, and keeping the two numbers straight is the whole distinction."],
  ["The 50S subunit",
   "That belongs to the macrolides — erythromycin and azithromycin — which block transpeptidation there."],
  ["Both the 30S and 50S subunits equally",
   "Neither class does this; each has its own subunit and the separation is what makes the pair worth learning."],
  ["Neither — they act on the cell membrane",
   "That is polymyxin B, which alters membrane permeability and lets intracellular contents leak out."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 23"},

{"topic": "Ocular antibiotics", "io": "Identify indications and contraindications of ophthalmic drugs",
 "slot": "drug choice",
 "q": "A contact lens wearer has bacterial conjunctivitis and keratitis has been ruled out. Which class is preferred, and why?",
 "opts": [
  ["A fluoroquinolone, for Pseudomonas cover",
   "Correct. Contact lens use raises the risk of Pseudomonas aeruginosa, a gram-negative rod, and the fluoroquinolones are the class that covers it. They are also the preferred choice for corneal ulcers for the same reason."],
  ["A macrolide, because erythromycin is soothing on an inflamed eye",
   "True of erythromycin in general, and it is the commonest ophthalmic antibiotic — but soothing does not address the organism this patient is at risk from."],
  ["An aminoglycoside, because it covers gram-negative organisms",
   "Aminoglycosides do have gram-negative activity, but the fluoroquinolones are the class named for Pseudomonas and corneal ulcers, and aminoglycosides carry a corneal ulceration risk of their own."],
  ["Sulfacetamide, because it is inexpensive and well tolerated",
   "Cheap, but it does not answer the Pseudomonas risk, and it must be avoided altogether in sulfonamide allergy."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 22"},

{"topic": "Ocular antibiotics", "io": "Identify indications and contraindications of ophthalmic drugs",
 "slot": "contraindication",
 "q": "Which ophthalmic antibiotic must be avoided outright in a patient with a sulfonamide allergy?",
 "opts": [
  ["Sulfacetamide",
   "Correct. It is a sulfonamide, and it works by antagonising p-aminobenzoic acid to block folic acid synthesis. A documented sulfonamide allergy rules it out — one of the few genuine contraindications in the whole ophthalmic antibiotic list."],
  ["Trimethoprim with polymyxin B",
   "Trimethoprim blocks the next step down, the reduction of folic acid to tetrahydrofolate, and is not a sulfonamide."],
  ["Bacitracin",
   "A cell wall agent with no structural relationship to the sulfonamides."],
  ["Ciprofloxacin",
   "A fluoroquinolone. It shares no structural relationship with the sulfonamides, so a sulfa allergy is no bar to using it."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 19"},

{"topic": "Ocular antibiotics", "io": "Identify ophthalmic drug classes and commonly prescribed ophthalmic drugs",
 "slot": "drug choice",
 "q": "Which agent is described as the most common ophthalmic antibiotic, and what property lets it be used before a bacterial cause is confirmed?",
 "opts": [
  ["Erythromycin, because it is soothing on an inflamed eye",
   "Correct. It is the one you will see most, and because it soothes the inflamed eye it can reasonably be started even when a bacterial infection has not been confirmed."],
  ["Azithromycin, because it is dosed less often",
   "Twice daily rather than four or more times is a real advantage, but it is considerably more expensive and not used as often clinically."],
  ["Ciprofloxacin, because it covers the widest spectrum",
   "Broad and effective, but expensive, with emerging resistance, and reserved rather than reached for first."],
  ["Bacitracin, because it has no drug interactions",
   "True of nearly every topical ophthalmic antibiotic here, so it distinguishes nothing."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 17"},

{"topic": "Ocular antibiotics", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "mechanism",
 "q": "Polytrim combines two agents. How does each one work?",
 "opts": [
  ["Trimethoprim blocks folate reduction; polymyxin B disrupts the bacterial membrane",
   "Correct. Trimethoprim stops folic acid becoming tetrahydrofolate, so nucleic acid and protein production fail. Polymyxin B binds membrane phospholipids and lets intracellular contents leak out. Two unrelated mechanisms in one bottle."],
  ["Trimethoprim antagonises p-aminobenzoic acid; polymyxin B blocks the 50S ribosome",
   "The first half describes sulfacetamide, which acts a step earlier in the same folate pathway, and polymyxin B is a membrane agent rather than a ribosomal one."],
  ["Both inhibit bacterial cell wall synthesis",
   "Neither agent touches the cell wall. Bacitracin is the only wall-active ophthalmic antibiotic, and it is not in this combination."],
  ["Trimethoprim disrupts the membrane; polymyxin B blocks folate reduction",
   "The mechanisms named are the right two but attached to the wrong drugs — trimethoprim is the folate agent and polymyxin B the membrane one."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 18"},

{"topic": "Ocular antibiotics", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "mechanism",
 "q": "Sulfacetamide and trimethoprim both interfere with folate, but at different points. What is the difference?",
 "opts": [
  ["Sulfacetamide antagonises p-aminobenzoic acid; trimethoprim blocks reduction to tetrahydrofolate",
   "Correct. Sulfacetamide acts at the synthesis end by competing with p-aminobenzoic acid; trimethoprim acts one step later, stopping folic acid being reduced. Sequential blockade of the same pathway."],
  ["Sulfacetamide blocks reduction to tetrahydrofolate; trimethoprim antagonises p-aminobenzoic acid",
   "The two steps are the right ones but assigned to the wrong drugs."],
  ["Sulfacetamide inhibits the 30S ribosome; trimethoprim inhibits the 50S",
   "Neither acts on the ribosome. Both interfere with folate, which is what makes them a sequential pair rather than alternatives."],
  ["Both block the same enzyme, so they are interchangeable",
   "They act at different points, which is why they appear as separate agents rather than substitutes."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slides 18-19"},

{"topic": "Ocular antibiotics", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "mechanism",
 "q": "Bacitracin ointment works on a structure none of the other ophthalmic antibiotics target. Which one?",
 "opts": [
  ["The bacterial cell wall",
   "Correct. Bacitracin stops mucopeptides being transferred into the growing wall. Every other ophthalmic antibiotic goes after the ribosome, DNA, folate or the membrane."],
  ["The 50S ribosomal subunit", "That is the macrolides, which block transpeptidation there and stop protein synthesis."],
  ["DNA gyrase", "That is the fluoroquinolones, which cause double-stranded DNA breakage."],
  ["The cytoplasmic membrane", "That is polymyxin B, which alters permeability rather than blocking wall construction."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 20"},

{"topic": "Ocular antibiotics", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "mechanism",
 "q": "How do the ophthalmic fluoroquinolones kill bacteria?",
 "opts": [
  ["They inhibit DNA gyrase and topoisomerase IV",
   "Correct. Blocking those enzymes prevents supercoiled DNA relaxing, and the strands break. This is the class used for corneal ulcers and for suspected Pseudomonas."],
  ["They inhibit RNA-dependent protein synthesis at the 50S ribosome", "That is the macrolide mechanism, shared by erythromycin and azithromycin."],
  ["They block folic acid synthesis", "That is sulfacetamide, and trimethoprim acts one step further along the same pathway."],
  ["They bind sterols and increase membrane permeability", "That is natamycin, and it is an antifungal mechanism rather than antibacterial."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 21"},

{"topic": "Ocular antibiotics", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "adverse effect",
 "q": "Which adverse effect is specific enough to an ophthalmic antibiotic class to be worth knowing, rather than being shared by all of them?",
 "opts": [
  ["Corneal ulceration from an aminoglycoside",
   "Correct. Ocular irritation is common to essentially every agent here and so distinguishes nothing — but aminoglycosides used for several days can produce corneal ulceration and a reactive keratoconjunctivitis, which changes how long you continue them."],
  ["Ocular irritation with erythromycin", "Shared by nearly every ophthalmic antibiotic, which is why it is not worth memorising which ones cause it."],
  ["Hypersensitivity with bacitracin", "Also non-specific — any of these agents can produce hypersensitivity, so it names no particular drug."],
  ["Unpleasant taste after a macrolide", "The taste complaint belongs with the fluoroquinolones, and reflects nasolacrimal drainage rather than a class toxicity."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 23"},

{"topic": "Ocular antibiotics", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "adverse effect",
 "q": "Roughly one in six patients given a particular ophthalmic fluoroquinolone develops a visible finding on the eye. Which drug, and what is seen?",
 "opts": [
  ["Ciprofloxacin, and a white precipitate forms",
   "Correct. It occurs in about seventeen per cent, and it is worth recognising so it is not mistaken for a worsening infiltrate or a new ulcer."],
  ["Moxifloxacin, and a white precipitate forms", "The finding is right but the agent is not; this is described for ciprofloxacin."],
  ["Gatifloxacin, and corneal deposits form", "Gatifloxacin carries no such described finding. The visible precipitate is specific to ciprofloxacin, in roughly one patient in six."],
  ["Ofloxacin, and conjunctival pigmentation develops", "Pigment change belongs with the prostaglandins in the glaucoma section, not with a fluoroquinolone."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 21"},

{"topic": "Ocular antivirals", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "drug choice",
 "q": "A patient has adenoviral conjunctivitis. Which antiviral is indicated?",
 "opts": [
  ["None is indicated",
   "Correct. There is no antiviral for viral conjunctivitis caused by adenoviruses. It runs its own course and you relieve the irritation. The ocular antivirals exist for keratitis, herpes zoster ophthalmicus and retinitis."],
  ["Topical trifluridine", "Reserved for herpes simplex keratitis and keratoconjunctivitis, not adenoviral disease."],
  ["Topical ganciclovir", "Used for herpetic keratitis and, by intravitreal injection, for cytomegalovirus retinitis."],
  ["Oral acyclovir", "Used for herpes zoster ophthalmicus and herpes simplex iridocyclitis; it has no role against adenovirus."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 25"},

{"topic": "Ocular antivirals", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "mechanism",
 "q": "How does trifluridine interfere with viral replication?",
 "opts": [
  ["It inhibits thymidylate synthetase and is incorporated into viral DNA in place of thymidine",
   "Correct. It both starves the virus of thymidine and substitutes itself into the growing strand — two hits on the same pathway."],
  ["It competitively inhibits deoxyguanosine triphosphate binding to DNA polymerase", "That is ganciclovir's mechanism, and the two are the pair worth separating."],
  ["It inhibits viral neuraminidase", "Not a mechanism used by any of the ophthalmic antivirals; both topical agents act on viral DNA synthesis."],
  ["It blocks viral attachment to the corneal epithelium", "Neither ophthalmic antiviral here acts at the attachment step."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 27"},

{"topic": "Ocular antivirals", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "mechanism",
 "q": "Ganciclovir treats herpetic keratitis topically and cytomegalovirus retinitis by intravitreal injection. How does it work?",
 "opts": [
  ["It competitively inhibits DNA polymerase",
   "Correct. Competing with the natural nucleotide at DNA polymerase halts viral DNA synthesis, and the intravitreal route is what makes it usable for retinitis."],
  ["It inhibits thymidylate synthetase and substitutes for thymidine", "That is trifluridine, the other topical ophthalmic antiviral."],
  ["It binds sterols in the viral envelope", "Sterol binding is the antifungal mechanism used by natamycin."],
  ["It inhibits viral protease", "Protease inhibition is not among the ocular antiviral mechanisms here; both topical agents act at the level of viral DNA synthesis."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 28"},

{"topic": "Ocular antifungals", "io": "Identify ophthalmic drug classes and commonly prescribed ophthalmic drugs", "slot": "drug choice",
 "q": "What is notable about natamycin among the ophthalmic antifungals?",
 "opts": [
  ["It is the only commercially available ophthalmic antifungal",
   "Correct. Everything else on the antifungal table — amphotericin B, the imidazoles — is given by another route or has to be compounded. Availability is why natamycin is the one to know by name."],
  ["It is the only antifungal effective against Fusarium", "It does cover Fusarium, but the point is availability rather than an exclusive spectrum."],
  ["It is the only antifungal given intravitreally", "Amphotericin B is the agent listed for intravitreal injection; natamycin is a topical suspension."],
  ["It is the only antifungal free of ocular irritation", "Ocular irritation is its adverse effect, as with nearly every topical ophthalmic agent."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 30"},

{"topic": "Ocular antifungals", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "mechanism",
 "q": "How does natamycin act on fungi?",
 "opts": [
  ["It binds sterol and increases fungal cell membrane permeability",
   "Correct. Binding membrane sterol makes the fungal membrane leaky. It is a polyene, and that is the polyene mechanism."],
  ["It inhibits fungal cell wall glucan synthesis", "An echinocandin mechanism, and the echinocandins are not on this ophthalmic list."],
  ["It inhibits ergosterol synthesis at 14-alpha-demethylase", "That is the azole mechanism, used by fluconazole and the rest of the imidazole group."],
  ["It inhibits fungal DNA polymerase", "No antifungal on this list acts on fungal DNA polymerase. The mechanisms here are sterol binding and ergosterol synthesis inhibition."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 32"},

{"topic": "Ocular antifungals", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "risk factor",
 "q": "Which risk factor for ophthalmic fungal infection is one a clinician can create?",
 "opts": [
  ["Topical corticosteroid use",
   "Correct. The risk list is trauma, chronic ocular surface disease, contact lens wear and immunosuppression — and topical steroid use is named explicitly as immunosuppression. It is the only one on the list you can introduce by prescribing."],
  ["Contact lens wear", "A genuine risk factor, but the patient's, not one the clinician introduces."],
  ["Antecedent trauma", "A genuine risk factor and on the list, but it is something the patient arrives with rather than something a prescription introduces."],
  ["Chronic ocular surface disease", "Also on the list, and also not something a prescription causes."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 30"},

{"topic": "Precautions", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "next step",
 "q": "A patient presents with an eye complaint and you are about to instil a medication. What must be done first?",
 "opts": [
  ["Measure visual acuity",
   "Correct. Acuity is measured before anything goes in the eye, and again at every follow-up. If it worsens, that is an immediate ophthalmology consult — which is the whole reason a baseline has to exist."],
  ["Measure intraocular pressure", "Tonometry has its own indications and needs an anesthetic first; it is not the universal precondition."],
  ["Instil fluorescein to exclude an epithelial defect", "Useful when corneal injury is suspected, but not required before every ophthalmic medication."],
  ["Confirm the patient is not wearing contact lenses", "Relevant to management, but the stated precaution that comes first is the acuity measurement."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 33"},

{"topic": "Ocular drug delivery", "io": "Identify ophthalmic drug classes and commonly prescribed ophthalmic drugs", "slot": "drug choice",
 "q": "Which delivery route carries the risk of globe perforation, optic nerve trauma and central retinal artery occlusion?",
 "opts": [
  ["Periocular injection",
   "Correct. These periocular injections reach the anterior segment, posterior uveitis and cystoid macular oedema, but the needle is the hazard — perforation, optic nerve trauma, vascular occlusion and direct retinal drug toxicity if the globe is entered."],
  ["Topical instillation", "Its limitations are compliance, corneal and conjunctival toxicity, nasal mucosal toxicity and systemic effects from nasolacrimal absorption — no needle, no perforation."],
  ["Oral administration", "Systemic exposure is the trade-off there, not mechanical injury to the globe."],
  ["Intravenous administration", "Again a systemic route; it carries no risk of perforating the eye."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 5"},

{"topic": "Ocular drug delivery", "io": "Identify ophthalmic drug classes and commonly prescribed ophthalmic drugs", "slot": "drug choice",
 "q": "What are the stated advantages of the topical route?",
 "opts": [
  ["Convenient, economical and relatively safe",
   "Correct. That combination is why almost every ophthalmic drug is a drop or an ointment. The price is compliance, surface toxicity and systemic absorption by the nasolacrimal route."],
  ["Sustained release without repeated dosing", "That is what inserts and implants are for; a plain topical solution needs frequent administration."],
  ["Reliable delivery to the posterior segment", "Topical drug reaches the anterior segment well; the posterior segment is what the periocular and intraocular routes exist for."],
  ["Avoidance of any systemic exposure", "The opposite — nasolacrimal drainage is exactly how a topical drop produces systemic effects."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 5"},

{"topic": "Ocular pharmacokinetics", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "mechanism",
 "q": "Transcorneal absorption has a lag time, and its rate depends most on one variable. Which, and what law governs it?",
 "opts": [
  ["The concentration gradient, governed by Fick's law",
   "Correct. Transcorneal movement is passive diffusion, so the steeper the gradient the faster the transfer. That is also why raising concentration, rather than volume, is the lever that matters."],
  ["The tear film pH, governed by the Henderson-Hasselbalch equation", "Ionisation matters for some drugs, but the rate-determining variable stated here is the gradient."],
  ["The corneal blood flow, governed by Fick's principle", "The cornea is avascular, which is part of why diffusion rather than perfusion governs delivery."],
  ["The drug's molecular weight, governed by Graham's law", "Molecular weight is not the variable named. Transcorneal movement is passive diffusion, so it is the concentration gradient that governs the rate."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 8"},

{"topic": "Ocular pharmacokinetics", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "mechanism",
 "q": "Absorption can be deliberately increased by blocking the tear ducts with silicone plugs or cautery. Why does that work?",
 "opts": [
  ["It stops the drop draining away",
   "Correct. Nasolacrimal drainage removes drug from the eye and sends it systemically. Blocking it leaves more drug in contact with the cornea for longer — the same goal as thickening the formulation."],
  ["It increases tear production and dilutes irritants", "Occlusion conserves tears rather than stimulating them, and dilution would reduce the gradient."],
  ["It reduces drug binding to tear proteins", "Protein binding is a separate determinant and is not altered by occluding the duct."],
  ["It lowers the corneal epithelial barrier", "Occluding the punctum does nothing to the corneal epithelium itself. What changes is how long the drug stays in contact with it."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 7"},

{"topic": "Ocular pharmacokinetics", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "adverse effect",
 "q": "A patient on long-term chloroquine develops a bull's eye lesion in the retina. Which pharmacokinetic property explains it?",
 "opts": [
  ["Some drugs accumulate in ocular tissue after systemic absorption",
   "Correct. Distribution into the eye happens normally after systemic absorption, and a few drugs concentrate there over time. The bull's eye maculopathy is the named consequence."],
  ["Chloroquine is metabolised in the eye to a toxic product", "Ocular metabolism is exploited for prodrugs such as dipivefrin and latanoprost, not offered as the explanation here."],
  ["Nasolacrimal drainage delivers a high local dose", "That route carries drug away from the eye toward the systemic circulation, not into the retina."],
  ["Chloroquine binds tear proteins and is retained on the surface", "Tear protein binding acts on the ocular surface and limits absorption; it cannot deposit anything in the retina, where the bull\u2019s eye lesion sits."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 10"},

{"topic": "Ocular antimicrobials", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "drug choice",
 "q": "A small, mild, peripheral ocular infection is being treated. What is the usual approach, and what limits it?",
 "opts": [
  ["Topical therapy, needing frequent dosing",
   "Correct. Topical gives very high local concentrations, which is the point, but bioavailability beyond the eye is poor and drops have to be given often. Broad-spectrum agents are used empirically without cultures unless an unusual organism is expected."],
  ["Oral therapy, limited by first-pass metabolism", "Oral and parenteral agents are reserved for infections that topical treatment cannot reach."],
  ["Intravitreal injection, limited by the risk of endophthalmitis", "Intravitreal injection is reserved for endophthalmitis and retinitis. Using it for a small peripheral infection would carry far more risk than the disease."],
  ["Subconjunctival injection, limited by local tissue injury", "Reserved for anterior segment infections and posterior uveitis, not mild peripheral disease."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 12"},

{"topic": "Ocular antimicrobials", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "next step",
 "q": "When are cultures routinely taken before starting an ophthalmic antibiotic?",
 "opts": [
  ["Not unless an unusual organism is expected",
   "Correct. Broad-spectrum topical therapy is started empirically. Cultures are reserved for when something unusual is likely — the immunocompromised patient is the example given."],
  ["Always, because resistance is emerging", "Resistance is a real concern with the fluoroquinolones, but it has not changed the empiric approach for ordinary infections."],
  ["Only for conjunctivitis, not for keratitis", "No such split is drawn. The rule is about whether an unusual organism is expected, not about which part of the eye is involved."],
  ["Only when the patient wears contact lenses", "Contact lens wear changes the drug you choose because of Pseudomonas risk, not whether you culture."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 12"},

{"topic": "Ocular antimicrobials", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "risk factor",
 "q": "Which factors determine whether an ocular infection is treated topically or with oral or parenteral agents?",
 "opts": [
  ["Setting, age, immune status and extent",
   "Correct. Those four decide the route. Preseptal disease may be manageable topically or orally, while postseptal or orbital cellulitis is a different proposition entirely."],
  ["The organism's Gram stain alone", "Cultures are not routinely obtained, so this is rarely even available at the moment of decision."],
  ["The patient's visual acuity alone", "Acuity is a mandatory baseline and a warning sign, but it does not by itself set the route."],
  ["Whether the patient wears contact lenses", "Relevant to drug choice because of Pseudomonas, not to the route."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 11"},

{"topic": "Ocular antimicrobials", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "diagnosis",
 "q": "Which organisms are listed as infectious causes of conjunctivitis?",
 "opts": [
  ["Neisseria, Haemophilus, Streptococcus and Moraxella",
   "Correct. Though most conjunctivitis is viral, allergic, irritant or contact-lens related — the bacterial list matters because it is what empiric broad-spectrum therapy is aimed at."],
  ["Pseudomonas aeruginosa and Serratia marcescens only", "Pseudomonas matters for contact lens wearers and corneal ulcers, but it is not the general conjunctivitis list."],
  ["Aspergillus, Candida, Fusarium and Cephalosporium", "Those are the fungal keratitis organisms that natamycin covers."],
  ["Adenovirus, herpes simplex and varicella zoster only", "Viruses are a common cause, but the question asks for the bacterial pathogens named."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 13"},

{"topic": "Ocular antimicrobials", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "mechanism",
 "q": "Why has the microbiological spectrum of ocular infection shifted over time, by the example given?",
 "opts": [
  ["Vaccination reduced Haemophilus influenzae",
   "Correct. The spectrum is not fixed — the example given is the fall in Haemophilus influenzae after the vaccine was introduced, which changes what empiric therapy has to cover."],
  ["Contact lens use increased Pseudomonas", "Contact lenses do raise Pseudomonas risk, but the shift attributed to a changing spectrum is the vaccine example."],
  ["Fluoroquinolone use selected for resistant Staphylococcus", "Emerging resistance is noted for the fluoroquinolones, but it is not the example used for a changing spectrum."],
  ["Topical steroid use increased fungal infection", "That is a risk factor for fungal keratitis, not a change in the bacterial spectrum."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 12"},

{"topic": "Ocular antibiotics", "io": "Identify ophthalmic drug classes and commonly prescribed ophthalmic drugs", "slot": "drug choice",
 "q": "Azithromycin solution is dosed twice daily while erythromycin ointment may be needed four or more times a day. Why is azithromycin still not the usual choice?",
 "opts": [
  ["It is considerably more expensive",
   "Correct. The dosing advantage is real and helps compliance, but cost keeps it from being used as often clinically. Erythromycin remains the common one."],
  ["It is less effective against the usual conjunctivitis organisms", "Azithromycin is not described as less effective. The reason it is used less often is expense, despite its more convenient dosing."],
  ["It cannot be used in contact lens wearers", "No such restriction is given; the contact lens concern drives you toward a fluoroquinolone for Pseudomonas cover."],
  ["It causes a white precipitate on the eye", "That is ciprofloxacin, in about seventeen per cent of patients."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 17"},

{"topic": "Ocular antibiotics", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "drug choice",
 "q": "Besides Pseudomonas cover, what is the other indication for which fluoroquinolones are specifically preferred?",
 "opts": [
  ["Corneal ulcers",
   "Correct. Corneal ulcers and suspected Pseudomonas are the two the fluoroquinolones are named for. Against that sit the cost and the emerging resistance, which is why they are not first for everything."],
  ["Blepharitis", "Managed with the broader ointment agents rather than reserved fluoroquinolones."],
  ["Ophthalmia neonatorum prophylaxis", "Prophylaxis of ophthalmia neonatorum is erythromycin ointment's listed indication, not a reason to reach for a fluoroquinolone."],
  ["Fungal keratitis", "An antifungal problem — natamycin — not an antibacterial one."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 22"},

{"topic": "Ocular antivirals", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "drug choice",
 "q": "Which ocular antivirals are given by mouth, and for which conditions?",
 "opts": [
  ["Acyclovir, valacyclovir or famciclovir",
   "Correct. The systemic agents handle zoster ophthalmicus and simplex keratitis or iridocyclitis, while trifluridine and ganciclovir are the topical options."],
  ["Oral natamycin for fungal keratitis", "Natamycin is a topical suspension; the oral antifungals are the imidazoles."],
  ["Oral foscarnet for cytomegalovirus retinitis", "Foscarnet does treat cytomegalovirus retinitis, but it is an intravenous agent. The oral antivirals here are acyclovir, valacyclovir and famciclovir."],
  ["Oral trifluridine for herpes simplex keratoconjunctivitis", "Trifluridine treats herpes simplex keratoconjunctivitis, but topically rather than orally \u2014 it is one of the two topical ocular antivirals."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 26"},

{"topic": "Ocular antifungals", "io": "Identify ophthalmic drug classes and commonly prescribed ophthalmic drugs", "slot": "drug choice",
 "q": "Amphotericin B appears on the ophthalmic antifungal table with more routes than any other agent. Which are they?",
 "opts": [
  ["Topical, subconjunctival, intravitreal, intravenous",
   "Correct. It is the one agent given by every route on the table, which is what makes it usable for endophthalmitis as well as surface disease."],
  ["Topical solution and oral tablet only", "Oral administration belongs to the imidazoles — fluconazole, itraconazole, ketoconazole."],
  ["Intravitreal and subconjunctival injection only", "Intravitreal injection is one of amphotericin B\u2019s four listed routes, which is the point \u2014 no other antifungal here has that range."],
  ["Topical suspension, and nothing else", "A topical suspension and nothing else is natamycin, which is the only commercially available ophthalmic antifungal."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 31"},

{"topic": "Ocular antibiotics", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "mechanism",
 "q": "Two ophthalmic antibiotic classes both stop bacterial protein synthesis. What separates them?",
 "opts": [
  ["Macrolides act at the 50S subunit, aminoglycosides at the 30S",
   "Correct. Same endpoint, different ribosomal subunit — the cleanest mechanism pairing among the ophthalmic antibiotics."],
  ["Macrolides act at the 30S subunit, aminoglycosides at the 50S", "The two subunits are the right ones but assigned to the wrong classes \u2014 macrolides take the 50S and aminoglycosides the 30S."],
  ["Macrolides block transpeptidation, aminoglycosides block DNA gyrase", "The first is right; the second belongs to the fluoroquinolones."],
  ["Both act at the 50S subunit but bind different sites", "The aminoglycosides bind the 30S, which is the whole distinction."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slides 15 and 23"},

{"topic": "Ocular drug delivery", "io": "Identify ophthalmic drug classes and commonly prescribed ophthalmic drugs", "slot": "drug choice",
 "q": "Which route is described for anterior segment surgery and infection, with prompt absorption and a relatively short duration?",
 "opts": [
  ["Intracameral injection",
   "Correct. Prompt onset, used in anterior segment surgery and infection, but its effect is relatively short-lived and it carries corneal and intraocular toxicity."],
  ["Topical instillation", "Prompt depending on formulation, but it is the convenient everyday route rather than a surgical one."],
  ["Retrobulbar injection", "A periocular route whose utility is posterior uveitis and cystoid macular oedema."],
  ["Oral administration", "Oral and parenteral agents exist for infections topical therapy cannot reach, which is not the situation described here."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 5"},

{"topic": "Ocular antimicrobials", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "diagnosis",
 "q": "Which non-infectious causes of conjunctivitis are commoner than the bacterial ones?",
 "opts": [
  ["Viruses, allergy, irritants and contact lenses",
   "Correct. These are given as the common causes, with immune-mediated reactions, systemic disease and tumours as less common. Bacterial pathogens come after — a reminder that most red eyes are not bacterial."],
  ["Only bacterial pathogens are listed as common", "The non-infectious causes come FIRST precisely because most red eyes are not bacterial; the pathogens are the smaller group."],
  ["Tumours and systemic disease", "Tumours and systemic disease do appear, but in the less common group alongside immune-mediated reactions rather than among the common causes."],
  ["Fungal keratitis and herpes zoster", "Fungal keratitis and herpes zoster are separate entities, and neither is a common cause of conjunctivitis."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 13"},

{"topic": "Ocular antimicrobials", "io": "Identify indications and contraindications of ophthalmic drugs", "slot": "next step",
 "q": "What is the stated goal of treating infectious conjunctivitis?",
 "opts": [
  ["Eradicate the infection and prevent long-term complications",
   "Correct. Both halves matter — clearing the organism is not the whole aim, because the reason to treat promptly is what an untreated infection leaves behind."],
  ["Relieve symptoms while the infection resolves on its own", "That is the approach to adenoviral conjunctivitis specifically, where no antiviral exists."],
  ["Prevent transmission to the other eye", "Limiting spread matters practically, but the goal given is to eradicate the infection and prevent the long-term complications it would leave."],
  ["Establish the organism by culture", "Cultures are not routine unless an unusual organism is expected."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 13"},

{"topic": "Ocular pharmacokinetics", "io": "Describe the mechanism of action of ophthalmic drugs", "slot": "mechanism",
 "q": "Which factors determine the rate and extent of absorption of a topical ophthalmic drug?",
 "opts": [
  ["Contact time, drainage, protein binding and diffusion",
   "Correct. Four variables, and formulation changes act on the first two — which is why gels, ointments and inserts exist and why occluding the puncta increases absorption."],
  ["Corneal blood flow and the rate of aqueous production", "The cornea is avascular, and aqueous production is the target of glaucoma drugs rather than a determinant of absorption."],
  ["The patient's systemic renal and hepatic function", "Those govern elimination once the drug is absorbed, not absorption at the eye."],
  ["Intraocular pressure and pupil size", "Neither intraocular pressure nor pupil size appears among the four determinants; those are time in contact, drainage, protein binding and diffusion."]],
 "c": 0, "cite": "Ophthalmology-2.pptx, Slide 7"},

]
