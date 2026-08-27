# -*- coding: utf-8 -*-
# Clinical Pathophysiology I Lecture 4 -- pool B.
# Objective 4 (conditions caused by abnormal shapes of the eye) and
# Objective 5 (age-related conditions of the eye).
#
# TWO OF WEBSTER'S NAMED EXAM TOPICS LIVE HERE: refraction errors and
# presbyopia. Both are flagged kfe=True.
#
# NO QUESTION ASKS WHICH LENS CORRECTS WHICH ERROR, for two independent
# reasons. He de-emphasised it out loud -- "not that important, concave and
# convex for my purposes; MORE IMPORTANT is knowing the difference between
# myopia, hyperopia, and the globe shape" -- and he contradicted himself while
# saying it, correcting mid-sentence with "and concave, sorry, other way
# around." Both transcripts catch the self-correction. The SLIDE is right
# (myopia takes a concave minus lens, hyperopia a convex plus lens) and the
# slide always wins, but the emphasis he asked for is GLOBE GEOMETRY, so that
# is what these questions test. cp_l4_partition.py asserts no lens-choice
# question exists.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "4. Ophthalmic Pathophysiology_STUDENT VERSION_v2.pptx"
def c(n): return f"{SRC}, Slide {n}"
def au(): return "Lecture recording, 26 August 2026"

IO4 = "d — Compare and contrast the conditions caused by abnormal shapes of the eye"
IO5 = "e — Compare and contrast the conditions of the eye that are age related"
IO7 = "g — Describe the pathogenesis of cataracts"

POOL_B = [
 dict(topic="Myopia", io=IO4, slot="etiology", kfe=True,
   q="What is the globe geometry in myopia, and where does the image focus?",
   opts=[
     ["The axial globe is too long, so the focal point falls in front of the retina",
      "Correct — an elongated globe overshoots, focusing short of the retina."],
     ["The axial globe is too short, so the focal point falls behind the retina",
      "That describes hyperopia."],
     ["The globe is normal but the cornea is irregularly curved",
      "That describes astigmatism."],
     ["The globe is normal but the lens has lost elasticity",
      "That describes presbyopia."]],
   c=0, cite=c(8)),

 dict(topic="Myopia", io=IO4, slot="manifestation", kfe=True,
   q="What can a myopic patient see well?",
   opts=[
     ["Objects up close", "Correct — myopia is nearsightedness, so near vision is the preserved one."],
     ["Objects far away", "Distance vision is the impaired one in myopia."],
     ["Neither near nor far without correction", "Near vision is preserved."],
     ["Only objects at the extreme periphery", "Myopia is a refractive, not a field, problem."]],
   c=0, cite=c(8)),

 dict(topic="Hyperopia", io=IO4, slot="etiology", kfe=True,
   q="What is the globe geometry in hyperopia, and where does the image focus?",
   opts=[
     ["The axial globe is too short, so the focal point falls behind the retina",
      "Correct — a short globe has not finished converging by the time light reaches the retina."],
     ["The axial globe is too long, so the focal point falls in front of the retina",
      "That describes myopia."],
     ["The cornea is steepened along one meridian",
      "That describes astigmatism."],
     ["The ciliary muscle has become sclerotic",
      "That describes presbyopia."]],
   c=0, cite=c(8)),

 dict(topic="Hyperopia", io=IO4, slot="manifestation", kfe=True,
   q="What can a hyperopic patient see well?",
   opts=[
     ["Objects far away", "Correct — hyperopia is farsightedness, so distance vision is the preserved one."],
     ["Objects up close", "Near vision is the impaired one in hyperopia."],
     ["Neither near nor far without correction", "Distance vision is preserved."],
     ["Only objects directly in the central field", "Hyperopia is refractive rather than a field defect."]],
   c=0, cite=c(8)),

 dict(topic="Astigmatism", io=IO4, slot="etiology", kfe=True,
   q="What causes astigmatism?",
   opts=[
     ["Irregular corneal or lens curvature creating non-spherical focal points",
      "Correct — the deck's definition, and the reason a single focal point cannot form."],
     ["An axial globe that is too long",
      "That is myopia."],
     ["An axial globe that is too short",
      "That is hyperopia."],
     ["Loss of lens elasticity with age",
      "That is presbyopia."]],
   c=0, cite=c(9)),

 dict(topic="Astigmatism", io=IO4, slot="manifestation", kfe=True,
   q="Why does astigmatism blur the whole field rather than just near or far?",
   opts=[
     ["The focal point is not landing in the correct area at all, so nothing comes into sharp focus",
      "Correct — Webster made this point in the lecture: the axis problem prevents proper focus anywhere."],
     ["It always occurs together with cataract",
      "The deck does not link the two."],
     ["It affects only the peripheral retina",
      "The problem is refractive and affects the whole image."],
     ["It causes progressive optic nerve damage",
      "That is glaucoma, and astigmatism does not do this."]],
   c=0, cite=au()),

 dict(topic="Astigmatism", io=IO4, slot="etiology", kfe=True,
   q="What can astigmatism combine with, and what happens when it does?",
   opts=[
     ["Myopia or hyperopia, adding a focal-length error to the axis error",
      "Correct — Webster described the two problems stacking."],
     ["Only presbyopia, and only after the age of forty",
      "Astigmatism is not restricted to combining with presbyopia."],
     ["Only glaucoma, through raised intraocular pressure",
      "There is no such relationship in the deck."],
     ["Nothing — it always occurs in isolation",
      "The lecture describes it combining with the other refractive errors."]],
   c=0, cite=au()),

 dict(topic="Presbyopia", io=IO5, slot="etiology", kfe=True,
   q="What is the mechanism of presbyopia?",
   opts=[
     ["The lens loses elasticity and the ciliary muscle loses accommodation, through sclerosis",
      "Correct — the deck's mechanism, and the point Webster went back to add after saying he was finished."],
     ["The axial globe shortens with age",
      "Presbyopia is a lens and ciliary problem, not a globe-shape one."],
     ["The cornea flattens with age, reducing refraction",
      "The deck attributes it to the lens and ciliary muscle."],
     ["The retinal pigment epithelium thins with age",
      "That is relevant to macular degeneration, not presbyopia."]],
   c=0, cite=c(9)),

 dict(topic="Presbyopia", io=IO5, slot="manifestation", kfe=True,
   q="What is the functional consequence of presbyopia?",
   opts=[
     ["Inability to focus on near objects, so reading glasses or bifocals are needed",
      "Correct — the deck's stated consequence, and the everyday presentation."],
     ["Inability to focus on distant objects",
      "Near focus is what is lost."],
     ["Loss of peripheral vision",
      "Presbyopia does not affect the visual field."],
     ["Loss of colour discrimination",
      "Colour vision is not affected."]],
   c=0, cite=c(9)),

 dict(topic="Presbyopia", io=IO5, slot="etiology", kfe=True,
   q="Webster tied presbyopia to a letter in an examination mnemonic. Which, and what does it stand for?",
   opts=[
     ["The A in PERRLA, for accommodation",
      "Correct — pupils equal, round, reactive to light and accommodation. He quizzed the room on it."],
     ["The R in PERRLA, for reactive",
      "The R stands for reactive to light, which is not the presbyopia link."],
     ["The P in PERRLA, for pupils",
      "The P is simply pupils."],
     ["The E in PERRLA, for equal",
      "The E is equal."]],
   c=0, cite=au()),

 dict(topic="Presbyopia", io=IO5, slot="etiology", kfe=True,
   q="Why does a hardening lens cause loss of accommodation?",
   opts=[
     ["Accommodation requires the lens to change shape, and a stiff lens cannot",
      "Correct — Webster's explanation: the lens is normally elastic and hardens with age."],
     ["Accommodation requires the pupil to constrict, and the lens blocks it",
      "Pupillary constriction accompanies the near reaction but is not what stiffening blocks."],
     ["Accommodation requires the globe to lengthen, and the lens prevents it",
      "The globe does not lengthen to accommodate."],
     ["Accommodation requires more aqueous production, which falls with age",
      "Aqueous production is unrelated to accommodation."]],
   c=0, cite=au()),

 dict(topic="Strabismus", io=IO4, slot="etiology",
   q="What is strabismus?",
   opts=[
     ["Ocular misalignment in which the visual axes fail to focus on corresponding retinal points",
      "Correct — the deck's definition, and it labels this the mechanical problem."],
     ["Reduced best-corrected acuity from abnormal visual development",
      "That is amblyopia, which the deck labels the visual deficit."],
     ["Involuntary rhythmic oscillation of the eyes",
      "That is nystagmus."],
     ["Drooping of the upper eyelid",
      "That is ptosis."]],
   c=0, cite=c(12)),

 dict(topic="Strabismus", io=IO4, slot="etiology",
   q="Which four subtypes of strabismus does the deck name?",
   opts=[
     ["Esotropia, exotropia, hypertropia and hypotropia",
      "Correct — inward, outward, upward and downward turning."],
     ["Esotropia, exotropia, anisocoria and amblyopia",
      "Anisocoria is unequal pupils and amblyopia is a visual deficit."],
     ["Myopia, hyperopia, astigmatism and presbyopia",
      "Those are refractive errors, not strabismus subtypes."],
     ["Entropion, ectropion, ptosis and proptosis",
      "Those are lid and orbital problems."]],
   c=0, cite=c(12)),

 dict(topic="Strabismus", io=IO4, slot="etiology",
   q="Which direction does the eye turn in esotropia?",
   opts=[
     ["Inward", "Correct — esotropia is an inward turn."],
     ["Outward", "That is exotropia."],
     ["Upward", "That is hypertropia."],
     ["Downward", "That is hypotropia."]],
   c=0, cite=c(12)),

 dict(topic="Strabismus", io=IO4, slot="etiology",
   q="What are the two pathophysiological causes of strabismus the deck gives?",
   opts=[
     ["Extraocular muscle imbalance and cranial nerve palsy of the third, fourth or sixth nerves",
      "Correct — the deck's two mechanisms."],
     ["Retinal detachment and vitreous haemorrhage",
      "Neither causes misalignment in the deck."],
     ["Raised intraocular pressure and optic disc cupping",
      "That is glaucoma."],
     ["Lens opacification and loss of the red reflex",
      "That is cataract."]],
   c=0, cite=c(12)),

 dict(topic="Amblyopia", io=IO4, slot="etiology",
   q="What is amblyopia?",
   opts=[
     ["Reduced best-corrected visual acuity from abnormal visual processing during the critical developmental period",
      "Correct — the deck's definition, and it is a visual deficit rather than a mechanical one."],
     ["Ocular misalignment from extraocular muscle imbalance",
      "That is strabismus, which the deck contrasts with amblyopia."],
     ["Progressive optic neuropathy from raised pressure",
      "That is glaucoma."],
     ["Opacification of the crystalline lens",
      "That is cataract."]],
   c=0, cite=c(12)),

 dict(topic="Amblyopia", io=IO4, slot="etiology",
   q="Which of these does the deck list as an amblyopia aetiology?",
   opts=[
     ["Uncorrected strabismus",
      "Correct — one of the three routes the deck gives to abnormal visual development."],
     ["Raised intraocular pressure",
      "Pressure causes glaucomatous damage, not amblyopia."],
     ["Posterior vitreous detachment",
      "That is a risk factor for retinal detachment."],
     ["Drusen beneath the retinal pigment epithelium",
      "Those are the hallmark of dry macular degeneration."]],
   c=0, cite=c(12)),

 dict(topic="Amblyopia", io=IO4, slot="etiology",
   q="Which forms of visual deprivation does the deck name as causing amblyopia?",
   opts=[
     ["Congenital cataract and ptosis",
      "Correct — the two deprivation causes the deck lists."],
     ["Corneal abrasion and conjunctivitis",
      "Neither deprives the developing visual system in the deck's account."],
     ["Subconjunctival haemorrhage and pterygium",
      "Neither is given as an amblyopia cause."],
     ["Blepharitis and chalazion",
      "Lid margin disease is not a deprivation cause here."]],
   c=0, cite=c(12)),

 dict(topic="Amblyopia", io=IO4, slot="etiology",
   q="The deck names a treatment window for amblyopia. What is it, and why does a window exist at all?",
   opts=[
     ["Before age seven to eight, because the visual system is only plastic during the critical developmental period",
      "Correct — the deck's window, and the developmental reason it closes."],
     ["Before age two, because the globe stops growing then",
      "Globe growth is not what defines the window, and the deck gives a later age."],
     ["Any time in childhood or adulthood, because the deficit is purely optical",
      "The deficit is developmental, which is why the window closes."],
     ["Before age fourteen, because the optic nerve myelinates then",
      "Neither the age nor the reason matches the deck."]],
   c=0, cite=c(12)),

 dict(topic="Cataract", io=IO7, slot="etiology", kfe=True,
   q="What is a cataract?",
   opts=[
     ["Cloudiness or opacification of the crystalline lens",
      "Correct — the deck's definition."],
     ["Opacification of the cornea from old injury",
      "That is a corneal scar."],
     ["Progressive loss of retinal ganglion cells",
      "That is glaucomatous damage."],
     ["Degeneration of the photoreceptors at the macula",
      "That is macular degeneration."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="etiology", kfe=True,
   q="What is the mechanism of the commonest, senile form of cataract?",
   opts=[
     ["Progressive insoluble aggregation and deposition of lens crystallin proteins",
      "Correct — the deck's molecular mechanism for the ageing cataract."],
     ["Osmotic swelling of the lens from sorbitol accumulation",
      "That is the diabetic mechanism, which the deck lists separately."],
     ["Rupture of the lens capsule after blunt trauma",
      "That is the traumatic mechanism."],
     ["Chronic ultraviolet-driven oxidative damage alone",
      "Ultraviolet exposure is listed under environmental causes, not as the senile mechanism."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="etiology", kfe=True,
   q="By what mechanism does diabetes mellitus cause cataract?",
   opts=[
     ["Excess glucose is converted to sorbitol, causing osmotic swelling of the lens",
      "Correct — the deck's metabolic mechanism."],
     ["Excess glucose glycates the lens capsule until it ruptures",
      "The deck describes osmotic swelling via sorbitol, not capsular rupture."],
     ["Hyperglycaemia causes crystallin proteins to aggregate directly",
      "Aggregation is the senile mechanism; diabetes acts through sorbitol."],
     ["Retinal ischaemia releases vascular endothelial growth factor into the lens",
      "That mechanism belongs to proliferative diabetic retinopathy."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="risk factors", kfe=True,
   q="Which medication class does the deck name as a cataract risk?",
   opts=[
     ["Chronic corticosteroids", "Correct — the deck names chronic corticosteroid use."],
     ["Chronic beta-blockers", "Not a cataract risk in the deck."],
     ["Chronic antihistamines", "Not named by the deck."],
     ["Chronic statins", "Not named by the deck."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="manifestation", kfe=True,
   q="How does a cataract present visually?",
   opts=[
     ["Gradual, painless, bilateral blurriness with glare around headlights at night, monocular diplopia and altered colour perception",
      "Correct — the deck's full symptom set."],
     ["Sudden painless monocular loss with flashes and floaters",
      "That is retinal detachment."],
     ["Severe eye pain with halos, a cloudy cornea and vomiting",
      "That is acute angle-closure glaucoma."],
     ["Gradual central distortion with straight lines appearing bent",
      "That is macular degeneration."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="test finding", kfe=True,
   q="What is found on ophthalmoscopy in cataract?",
   opts=[
     ["Loss of the normal red reflex, with a white opacity visible through the pupil in severe cases",
      "Correct — the deck's examination finding, with leukocoria when advanced."],
     ["An enlarged cup-to-disc ratio",
      "That is glaucomatous cupping."],
     ["Drusen beneath the retinal pigment epithelium",
      "Those are the hallmark of dry macular degeneration."],
     ["A pale, swollen optic disc with blurred margins",
      "That is papilloedema."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="etiology", kfe=True,
   q="Where in the lens does a cataract usually appear, and what changes that?",
   opts=[
     ["Usually in the periphery, but it can appear in the nucleus, which is often associated with trauma",
      "Correct — the deck's distinction between the usual peripheral site and the nuclear, trauma-associated one."],
     ["Always in the nucleus, whatever the cause",
      "The deck gives the periphery as the usual site."],
     ["Always at the posterior capsule, whatever the cause",
      "The deck does not describe it this way."],
     ["Only at the equator of the lens, where the zonules attach",
      "Not the deck's account."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="risk factors", kfe=True,
   q="Which congenital and environmental causes does the deck list for cataract?",
   opts=[
     ["Down syndrome, excessive ultraviolet radiation and oxidative damage",
      "Correct — the deck's congenital and environmental group."],
     ["Marfan syndrome, smoking and hypertension",
      "None of these appears in the deck's cataract list."],
     ["Prematurity, oxygen therapy and retinopathy of prematurity",
      "Not the deck's cataract causes."],
     ["Albinism, high myopia and lattice degeneration",
      "Lattice degeneration and high myopia are retinal detachment risks."]],
   c=0, cite=c(22)),
]
