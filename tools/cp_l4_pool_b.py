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
   q="Which description matches the optics of myopia?",
   opts=[
     ["The axial globe is too long, so the focal point falls in front of the retina",
      "Correct — an elongated globe overshoots, focusing short of the retina."],
     ["The axial globe is too short, so the focal point falls behind the retina",
      "A globe too short, focusing behind the retina, is hyperopia; in myopia the axial globe is too long, so the focal point falls in front of the retina."],
     ["The globe is normal but the cornea is irregularly curved",
      "Irregular corneal or lens curvature is astigmatism, creating non-spherical focal points; myopia is an axial globe that is too long."],
     ["The globe is normal but the lens has lost elasticity",
      "Loss of lens elasticity is presbyopia, the age-related loss of near focus; myopia is an elongated globe that focuses in front of the retina."]],
   c=0, cite=c(8)),

 dict(topic="Myopia", io=IO4, slot="manifestation", kfe=True,
   q="What can a myopic patient see well?",
   opts=[
     ["Objects up close", "Correct — myopia is nearsightedness, so near vision is the preserved one."],
     ["Objects far away", "Distance vision is what fails in myopia, because the long globe focuses in front of the retina; near vision is the preserved one."],
     ["Neither near nor far without correction", "Near vision is preserved in myopia; only distance focus fails, because the elongated globe places the focal point in front of the retina."],
     ["Only objects at the extreme periphery", "Myopia is a refractive error of a long globe, not a field defect; it preserves near vision while distance vision blurs."]],
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
     ["Objects up close", "Near vision is what fails in hyperopia, because the short globe focuses behind the retina; distance vision is the preserved one."],
     ["Neither near nor far without correction", "Distance vision is preserved in hyperopia; only near focus fails, because the short axial globe places the focal point behind the retina."],
     ["Only objects directly in the central field", "Hyperopia is a refractive error of a short globe, not a field defect; it spares distance vision while near focus fails."]],
   c=0, cite=c(8)),

 dict(topic="Astigmatism", io=IO4, slot="etiology", kfe=True,
   q="What causes astigmatism?",
   opts=[
     ["Irregular corneal or lens curvature creating non-spherical focal points",
      "Correct — irregular curvature of the cornea or lens creates non-spherical focal points instead of the single focal point needed for a sharp image."],
     ["An axial globe that is too long",
      "An axial globe that is too long causes myopia, focusing in front of the retina; astigmatism comes from irregular corneal or lens curvature."],
     ["An axial globe that is too short",
      "An axial globe that is too short causes hyperopia, focusing behind the retina; astigmatism comes from irregular corneal or lens curvature."],
     ["Loss of lens elasticity with age",
      "Age-related loss of lens elasticity is presbyopia; astigmatism is irregular corneal or lens curvature creating non-spherical focal points."]],
   c=0, cite=c(9)),

 dict(topic="Astigmatism", io=IO4, slot="manifestation", kfe=True,
   q="Why does astigmatism blur the whole field rather than just near or far?",
   opts=[
     ["The focal point is not landing in the correct area at all, so nothing comes into sharp focus",
      "Correct — myopia and hyperopia misplace a single focal point that can be shifted by distance, whereas astigmatism produces two focal lines at once, so no viewing distance brings the image together."],
     ["It always occurs together with cataract",
      "Cataract and astigmatism are unrelated; the blur at all distances comes from the two focal lines produced by an unevenly curved cornea."],
     ["It affects only the peripheral retina",
      "The problem is refractive and affects the whole image."],
     ["It causes progressive optic nerve damage",
      "That is glaucoma, and astigmatism does not do this."]],
   c=0, cite=au()),

 dict(topic="Astigmatism", io=IO4, slot="etiology", kfe=True,
   q="Which conditions can coexist with astigmatism?",
   opts=[
     ["Myopia or hyperopia, adding a focal-length error to the axis error",
      "Correct — irregular corneal or lens curvature can coexist with a globe that is too long or too short, so a focal-length error stacks on the curvature error."],
     ["Only presbyopia, and only after the age of forty",
      "Presbyopia is not its only partner; astigmatism, an irregular corneal or lens curvature, can coexist with the axial-length errors of myopia or hyperopia."],
     ["Only glaucoma, through raised intraocular pressure",
      "Glaucoma is a pressure-driven optic neuropathy, not a refractive error; the curvature error of astigmatism can coexist with myopia or hyperopia."],
     ["Nothing — it always occurs in isolation",
      "Astigmatism is not always isolated; its irregular curvature can sit on top of a globe that is too long or too short, as in myopia or hyperopia."]],
   c=0, cite=au()),

 dict(topic="Presbyopia", io=IO5, slot="etiology", kfe=True,
   q="What is the mechanism of presbyopia?",
   opts=[
     ["The lens stiffens and the ciliary muscle loses accommodation, through sclerosis",
      "Correct — sclerosis stiffens the lens and the ciliary muscle loses accommodation, so the eye can no longer focus on near objects."],
     ["The axial globe shortens with age",
      "The globe does not shorten in presbyopia; it is a lens and ciliary muscle problem, loss of elasticity and accommodation through sclerosis."],
     ["The cornea flattens with age, reducing refraction",
      "The cornea is not the site; presbyopia is loss of lens elasticity and ciliary muscle accommodation through sclerosis, so near focus fails."],
     ["The retinal pigment epithelium thins with age",
      "Pigment epithelium degeneration belongs to dry macular degeneration; presbyopia is sclerosis of the lens and loss of ciliary muscle accommodation."]],
   c=0, cite=c(9)),

 dict(topic="Presbyopia", io=IO5, slot="manifestation", kfe=True,
   q="What is the functional consequence of presbyopia?",
   opts=[
     ["Inability to focus on near objects, so reading glasses are needed",
      "Correct — the sclerotic lens and ciliary muscle can no longer accommodate, so near objects cannot be focused and readers or bifocals are needed."],
     ["Inability to focus on distant objects",
      "Distance vision is not the one lost; presbyopia removes near focus, as the lens and ciliary muscle lose accommodation."],
     ["Loss of peripheral vision",
      "Presbyopia does not affect the visual field; it is a loss of accommodation, so near objects cannot be brought into focus."],
     ["Loss of color discrimination",
      "Color vision, a cone function, is unaffected; presbyopia is loss of lens elasticity and accommodation, impairing near focus."]],
   c=0, cite=c(9)),

 dict(topic="Presbyopia", io=IO5, slot="etiology", kfe=True,
   q="Which function of the eye does presbyopia impair?",
   opts=[
     ["Accommodation for near objects",
      "Correct — presbyopia is loss of lens elasticity and ciliary muscle accommodation due to sclerosis, so the eye can no longer focus on near objects."],
     ["Light detection by the rods and cones",
      "Rods and cones in the photoreceptor layer are not what presbyopia affects; it is loss of lens elasticity and ciliary muscle accommodation from sclerosis."],
     ["Drainage of aqueous humor through the trabecular meshwork",
      "Aqueous drainage through the trabecular meshwork and canal of Schlemm regulates intraocular pressure; presbyopia is loss of lens elasticity and accommodation."],
     ["Secretion of the lipid layer of the tear film",
      "The tear film's lipid layer comes from the meibomian glands in the tarsal plates; presbyopia is loss of lens elasticity and ciliary muscle accommodation."]],
   c=0, cite=c(9)),

 dict(topic="Presbyopia", io=IO5, slot="etiology", kfe=True,
   q="Why does a hardening lens cause loss of accommodation?",
   opts=[
     ["Accommodation requires the lens to change shape, and a stiff lens cannot",
      "Correct — the lens is normally elastic, and as it hardens with age it can no longer change shape, so accommodation is lost."],
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
      "Correct — when the two eyes do not point at the same object, the image falls on non-corresponding retinal points and the brain receives two irreconcilable images."],
     ["Reduced best-corrected acuity from abnormal visual development",
      "Reduced best-corrected acuity from abnormal development is amblyopia; strabismus is the misalignment that can cause it."],
     ["Involuntary rhythmic oscillation of the eyes",
      "That is nystagmus."],
     ["Drooping of the upper eyelid",
      "That is ptosis."]],
   c=0, cite=c(12)),

 dict(topic="Strabismus", io=IO4, slot="etiology",
   q="Which four subtypes of strabismus are named?",
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
   q="What are the two pathophysiological causes of strabismus?",
   opts=[
     ["Extraocular muscle imbalance and third, fourth or sixth nerve palsy",
      "Correct — strabismus is mechanical: an extraocular muscle imbalance or a palsy of the third, fourth or sixth cranial nerve misaligns the visual axes."],
     ["Retinal detachment and vitreous hemorrhage",
      "Retinal detachment and vitreous hemorrhage affect the image, not alignment; strabismus comes from extraocular muscle imbalance or cranial nerve palsy."],
     ["Raised intraocular pressure and optic disc cupping",
      "Raised pressure with disc cupping and field loss is glaucoma; strabismus arises from extraocular muscle imbalance or palsy of the third, fourth or sixth nerve."],
     ["Lens opacification and loss of the red reflex",
      "Lens opacification with loss of the red reflex is cataract; strabismus, a mechanical misalignment, comes from muscle imbalance or cranial nerve palsy."]],
   c=0, cite=c(12)),

 dict(topic="Amblyopia", io=IO4, slot="etiology",
   q="What is amblyopia?",
   opts=[
     ["Reduced best-corrected acuity from abnormal visual development",
      "Correct — amblyopia is a visual deficit rather than a mechanical one: best-corrected acuity stays reduced because visual processing developed abnormally during the critical pediatric period."],
     ["Ocular misalignment from extraocular muscle imbalance",
      "Misalignment from muscle imbalance or nerve palsy is strabismus, a mechanical problem; amblyopia is the visual deficit that uncorrected strabismus can cause."],
     ["Progressive optic neuropathy from raised pressure",
      "Progressive optic neuropathy from raised pressure is glaucoma; amblyopia is reduced best-corrected acuity from abnormal developmental visual processing."],
     ["Opacification of the crystalline lens",
      "Opacification of the crystalline lens is cataract; amblyopia is reduced best-corrected acuity from abnormal visual processing in childhood."]],
   c=0, cite=c(12)),

 dict(topic="Amblyopia", io=IO4, slot="etiology",
   q="Which condition can cause amblyopia?",
   opts=[
     ["Uncorrected strabismus",
      "Correct — uncorrected strabismus is a cause of amblyopia, the loss of best-corrected acuity from abnormal visual processing in the critical pediatric period."],
     ["Raised intraocular pressure",
      "Raised intraocular pressure compresses retinal ganglion cell axons in glaucoma; amblyopia follows uncorrected strabismus, severe refractive error or visual deprivation."],
     ["Posterior vitreous detachment",
      "Posterior vitreous detachment is a risk factor for retinal detachment; amblyopia can follow severe myopia, hyperopia or astigmatism, or visual deprivation."],
     ["Drusen beneath the retinal pigment epithelium",
      "Drusen beneath the retinal pigment epithelium are the hallmark of dry macular degeneration; amblyopia can follow deprivation such as congenital cataract or ptosis."]],
   c=0, cite=c(12)),

 dict(topic="Amblyopia", io=IO4, slot="etiology",
   q="Which forms of visual deprivation are named as causing amblyopia?",
   opts=[
     ["Congenital cataract and ptosis",
      "Correct — both physically block the image reaching the retina during the critical period, so the visual pathway for that eye never develops."],
     ["Corneal abrasion and conjunctivitis",
      "Both are transient surface conditions that resolve; amblyopia requires sustained deprivation during visual development."],
     ["Subconjunctival hemorrhage and pterygium",
      "Neither is given as an amblyopia cause."],
     ["Blepharitis and chalazion",
      "Lid margin disease is not a deprivation cause here."]],
   c=0, cite=c(12)),

 dict(topic="Amblyopia", io=IO4, slot="etiology",
   q="There is a treatment window for amblyopia. What is it, and why does a window exist at all?",
   opts=[
     ["Before age seven to eight, because the visual system is only plastic during the critical developmental period",
      "Correct — cortical connections serving vision can still be remodeled while the system is plastic, so restoring a clear image before about seven or eight can recover acuity; afterwards the deficit is fixed."],
     ["Before age two, because the globe stops growing then",
      "The globe continues growing well past age two, and the window is set by cortical plasticity, closing at around seven or eight."],
     ["Any time in childhood or adulthood, because the deficit is purely optical",
      "The deficit is developmental, which is why the window closes."],
     ["Before age fourteen, because the optic nerve myelinates then",
      "Neither figure fits: the window closes around seven to eight, and it is cortical plasticity rather than myelination that ends it."]],
   c=0, cite=c(12)),

 dict(topic="Cataract", io=IO7, slot="etiology", kfe=True,
   q="What is a cataract?",
   opts=[
     ["Cloudiness or opacification of the crystalline lens",
      "Correct — the lens must be transparent to focus light, and any opacification of its fibers scatters light and degrades the retinal image."],
     ["Opacification of the cornea from old injury",
      "That is a corneal scar."],
     ["Progressive loss of retinal ganglion cells",
      "That is glaucomatous damage."],
     ["Degeneration of the photoreceptors at the macula",
      "That is macular degeneration."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="etiology", kfe=True,
   q="What is the mechanism of the most common, senile form of cataract?",
   opts=[
     ["Progressive insoluble aggregation and deposition of lens crystallin proteins",
      "Correct — senile cataract, the most common form, results from progressive insoluble aggregation and deposition of lens crystallin proteins, opacifying the lens."],
     ["Osmotic swelling of the lens from sorbitol accumulation",
      "Sorbitol-driven osmotic swelling is the diabetic mechanism; the senile form is protein aggregation."],
     ["Rupture of the lens capsule after blunt trauma",
      "Capsule rupture from blunt or penetrating trauma is the traumatic mechanism; senile cataract comes from crystallin protein aggregation."],
     ["Chronic ultraviolet-driven oxidative damage alone",
      "Ultraviolet light is an environmental cataract cause, not the senile mechanism, which is progressive aggregation of insoluble lens crystallin proteins."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="etiology", kfe=True,
   q="By what mechanism does diabetes mellitus cause cataract?",
   opts=[
     ["Excess glucose is converted to sorbitol, causing osmotic swelling of the lens",
      "Correct — in diabetes, excessive glucose is converted to sorbitol, and the resulting osmotic swelling of the lens produces cataract."],
     ["Excess glucose glycates the lens capsule until it ruptures",
      "Capsule rupture is the traumatic mechanism; diabetes clouds the lens through sorbitol, which causes osmotic swelling of the lens."],
     ["Hyperglycemia causes crystallin proteins to aggregate directly",
      "Aggregation is the senile mechanism; diabetes acts through sorbitol."],
     ["Retinal ischemia releases vascular endothelial growth factor into the lens",
      "Growth factor released by retinal ischemia drives proliferative diabetic retinopathy; in the lens, diabetes acts through sorbitol and osmotic swelling."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="risk factors", kfe=True,
   q="Which medication class is a cataract risk?",
   opts=[
     ["Chronic corticosteroids", "Correct — chronic corticosteroid use is the medication cause of cataract, alongside aging, diabetes, ocular trauma, Down syndrome and ultraviolet light."],
     ["Chronic beta-blockers", "Beta-blockers are not a cataract risk; the medication class that causes cataract, the opacification of the crystalline lens, is chronic corticosteroids."],
     ["Chronic antihistamines", "Antihistamines are not a cataract risk; the medication that opacifies the lens is chronic corticosteroid use, with trauma, diabetes and aging as other causes."],
     ["Chronic statins", "Statins are not a cataract risk; chronic corticosteroid use is, with aging, diabetes, ocular trauma, Down syndrome and ultraviolet light as other causes."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="manifestation", kfe=True,
   q="How does a cataract present visually?",
   opts=[
     ["Gradual, painless, bilateral blurriness with glare around headlights at night, monocular diplopia and altered color perception",
      "Correct — a clouded lens scatters light rather than blocking it, so it dims and blurs gradually, produces glare around point sources at night, splits an image within the one eye, and filters shorter wavelengths so colors appear yellowed."],
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
      "Correct — the red reflex depends on light passing through the lens to the vascular choroid and back, so a clouded lens dulls or extinguishes it, and a dense cataract appears as white leukocoria."],
     ["An enlarged cup-to-disc ratio",
      "That is glaucomatous cupping."],
     ["Drusen beneath the retinal pigment epithelium",
      "Those are the hallmark of dry macular degeneration."],
     ["A pale, swollen optic disc with blurred margins",
      "That is papilledema."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="etiology", kfe=True,
   q="Where in the lens does a cataract usually appear, and what changes that?",
   opts=[
     ["Usually in the periphery, but it can appear in the nucleus, which is often associated with trauma",
      "Correct — age-related opacification typically begins peripherally in the cortex, whereas a nuclear cataract in a younger patient raises the question of previous trauma."],
     ["Always in the nucleus, whatever the cause",
      "The nucleus is not the usual site; age-related opacity generally starts in the peripheral cortex, and a nuclear one suggests trauma."],
     ["Always at the posterior capsule, whatever the cause",
      "Posterior subcapsular opacity is characteristic of corticosteroid use rather than the usual pattern, which begins peripherally."],
     ["Only at the equator of the lens, where the zonules attach",
      "The equator is where the zonules insert, not where opacity characteristically forms; cataract usually begins in the peripheral cortex."]],
   c=0, cite=c(22)),

 dict(topic="Cataract", io=IO7, slot="risk factors", kfe=True,
   q="Which congenital and environmental causes are listed for cataract?",
   opts=[
     ["Down syndrome, excessive ultraviolet radiation and oxidative damage",
      "Correct — Down syndrome carries a congenital predisposition, while ultraviolet light and oxidative stress accumulate damage in crystallin proteins that the lens can never replace."],
     ["Marfan syndrome, smoking and hypertension",
      "Marfan syndrome dislocates the lens rather than clouding it, and smoking and hypertension are not the causes grouped here."],
     ["Prematurity, oxygen therapy and retinopathy of prematurity",
      "Prematurity and supplemental oxygen cause retinopathy of prematurity, a retinal vascular disease rather than a lens opacity."],
     ["Albinism, high myopia and lattice degeneration",
      "Lattice degeneration and high myopia are retinal detachment risks."]],
   c=0, cite=c(22)),
]
