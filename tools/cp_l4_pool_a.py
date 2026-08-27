# -*- coding: utf-8 -*-
# Clinical Pathophysiology I Lecture 4 (Ophthalmic Pathophysiology,
# Bill Webster, MMS, PA-C, guest lecturer) -- pool A.
# Objectives 1 and 2: the neurological anatomy of the eye, and the
# physiological processes of vision.
#
# CLINICAL PATHOPHYSIOLOGY IS MECHANISM, NEVER MANAGEMENT. That is the line
# against CMS I, and it matters more than usual for this lecture: CMS I Exam 2
# Lecture 1 covers a nearly identical condition list from the management side.
# This deck does put some management on its slides -- the lecturer's own
# subtitle says "and (some) clinical concepts" -- so where a treatment appears
# it is stated as a fact about the disease, never asked as "what would you do".
# cp_l4_partition.py enforces this.
#
# kfe=True marks a question on something Webster named ALOUD as testable in the
# last two minutes of the lecture. See cp_l4_partition.py for the list and how
# it was recovered.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "4. Ophthalmic Pathophysiology_STUDENT VERSION_v2.pptx"
def c(n): return f"{SRC}, Slide {n}"
def ci(n): return f"{SRC}, Slide {n} (image only)"

IO1 = "a — Compare and contrast the neurological anatomy of the eye"
IO2 = "b — Describe the physiological processes of vision"

POOL_A = [
 dict(topic="Unique features of the eye", io=IO1, slot="etiology",
   q="What makes the eye the only place in the body where live neural tissue can be seen directly?",
   opts=[
     ["The optic nerve head is visible through the pupil without cutting any tissue",
      "Correct — the deck calls the eye a nervous window for exactly this reason."],
     ["The retina can be biopsied more safely than any other neural tissue",
      "The deck's point is that no tissue has to be cut at all."],
     ["The cornea contains myelinated tracts that can be seen on slit lamp",
      "The cornea's nerves are not what the deck describes here."],
     ["The sclera is thin enough to transilluminate the whole globe",
      "Transillumination is not the mechanism the deck gives."]],
   c=0, cite=c(4)),

 dict(topic="Unique features of the eye", io=IO1, slot="etiology",
   q="Which tissue does the deck say has the highest oxygen consumption and metabolic rate in the body?",
   opts=[
     ["The retina, higher even than the cerebral cortex",
      "Correct — the deck makes the comparison with cortex explicitly."],
     ["The cerebral cortex, with the retina second",
      "The deck puts the retina above the cortex."],
     ["The cornea, because it is avascular",
      "Being avascular does not make the cornea the highest consumer."],
     ["The ciliary body, because it continuously makes aqueous humour",
      "Aqueous production is not given as the highest metabolic demand."]],
   c=0, cite=c(4)),

 dict(topic="Unique features of the eye", io=IO1, slot="etiology",
   q="Why is the cornea's health responsible for so much of the eye's focusing power?",
   opts=[
     ["About seventy per cent of refraction depends on it",
      "Correct — the deck's figure for the cornea's share of refraction."],
     ["About thirty per cent of refraction depends on it",
      "The deck puts the cornea's share far higher than this."],
     ["It holds the lens in position through the zonules",
      "The zonules arise from the ciliary body, not the cornea."],
     ["It contains the highest density of cones in the eye",
      "Cones are in the retina, concentrated at the fovea."]],
   c=0, cite=c(4)),

 dict(topic="Unique features of the eye", io=IO1, slot="etiology",
   q="How is the avascular cornea oxygenated?",
   opts=[
     ["By direct contact with air and tears",
      "Correct — the deck's stated route for an avascular tissue."],
     ["By diffusion from the limbal blood vessels alone",
      "The deck names air and tears rather than limbal supply."],
     ["By the aqueous humour circulating through the anterior chamber",
      "Aqueous nourishes the cornea and lens, but the deck names air and tears for oxygen."],
     ["By the choroidal circulation behind it",
      "The choroid lies at the back of the eye and nourishes the retina."]],
   c=0, cite=c(4)),

 dict(topic="Unique features of the eye", io=IO1, slot="etiology",
   q="What proportion of human knowledge acquisition does the deck estimate is mediated through the eye?",
   opts=[
     ["About eighty-three per cent", "Correct — the deck's opening figure."],
     ["About fifty per cent", "Below the deck's estimate."],
     ["About sixty-five per cent", "Below the deck's estimate."],
     ["About ninety-five per cent", "Above the deck's estimate."]],
   c=0, cite=c(4)),

 dict(topic="The three tunics", io=IO1, slot="etiology",
   q="Which two structures make up the fibrous outer tunic of the eye?",
   opts=[
     ["The sclera and the cornea",
      "Correct — the protective white coat and the clear refracting window."],
     ["The choroid and the ciliary body",
      "Those belong to the uvea, the vascular middle tunic."],
     ["The retina and the retinal pigment epithelium",
      "Those form the neurosensory inner tunic."],
     ["The iris and the lens",
      "The iris is uveal and the lens is not part of a tunic."]],
   c=0, cite=c(7)),

 dict(topic="The three tunics", io=IO1, slot="etiology",
   q="Which three structures make up the uvea?",
   opts=[
     ["The choroid, the ciliary body and the iris",
      "Correct — the vascular middle tunic in full."],
     ["The choroid, the retina and the sclera",
      "The retina is the inner tunic and the sclera the outer."],
     ["The ciliary body, the lens and the zonules",
      "The lens and zonules are not part of the uvea."],
     ["The iris, the cornea and the conjunctiva",
      "The cornea is fibrous and the conjunctiva is a mucosal covering."]],
   c=0, cite=c(7)),

 dict(topic="The three tunics", io=IO1, slot="etiology",
   q="What is the choroid's function?",
   opts=[
     ["It is a highly vascularised pigmented layer that nourishes the retina",
      "Correct — the deck's description of the choroid's role."],
     ["It produces the aqueous humour that fills the anterior chamber",
      "That is the ciliary body's non-pigmented epithelium."],
     ["It controls the size of the pupil",
      "That is the iris."],
     ["It phagocytoses the outer segments of the photoreceptors",
      "That is the retinal pigment epithelium."]],
   c=0, cite=c(7)),

 dict(topic="Physiology of vision", io=IO2, slot="etiology",
   q="What are the three non-negotiable requirements for vision the deck lists?",
   opts=[
     ["Image formation, neural transmission, and photoreceptor excitation",
      "Correct — the three the deck names as non-negotiable."],
     ["Image formation, accommodation, and convergence",
      "Accommodation and convergence are part of the near reaction rather than the three requirements."],
     ["Corneal clarity, lens clarity, and a normal intraocular pressure",
      "These are conditions for good vision but not the deck's three processes."],
     ["Pupillary constriction, refraction, and colour discrimination",
      "Not the deck's list."]],
   c=0, cite=c(7)),

 dict(topic="Physiology of vision", io=IO2, slot="etiology",
   q="Where must light be focused for an image to form?",
   opts=[
     ["On the retina, after refraction through the cornea and lens",
      "Correct — the deck's description of image formation."],
     ["On the choroid, after refraction through the cornea alone",
      "The choroid lies behind the retina and does not receive the focused image."],
     ["On the optic disc, where the nerve exits",
      "The optic disc is the blind spot and has no photoreceptors."],
     ["On the lens itself, which then transmits the signal",
      "The lens refracts light; it does not detect it."]],
   c=0, cite=c(7)),

 dict(topic="Physiology of vision", io=IO2, slot="etiology",
   q="Where do impulses travel after leaving the optic nerve?",
   opts=[
     ["To the occipital cortex",
      "Correct — the deck routes neural transmission to the occipital cortex."],
     ["To the temporal cortex",
      "The temporal lobe carries part of the optic radiation but is not the destination."],
     ["To the frontal eye fields",
      "Those govern gaze rather than receiving the visual image."],
     ["To the superior colliculus alone",
      "The deck's stated destination is the visual cortex."]],
   c=0, cite=c(7)),

 dict(topic="Photoreceptors", io=IO2, slot="etiology",
   q="What do photons do to rods and cones?",
   opts=[
     ["They stimulate them to convert light into hyperpolarising action potentials",
      "Correct — the deck's phrasing for photoreceptor excitation."],
     ["They stimulate them to convert light into depolarising action potentials",
      "The deck specifically describes hyperpolarisation."],
     ["They are absorbed by the retinal pigment epithelium before reaching them",
      "The pigment epithelium absorbs scattered light, not the signal itself."],
     ["They trigger release of aqueous humour into the posterior chamber",
      "Aqueous production has nothing to do with photoreception."]],
   c=0, cite=c(7)),

 dict(topic="Photoreceptors", io=IO2, slot="etiology",
   q="Roughly how many rods are there, and what are they for?",
   opts=[
     ["About 120 million, for dim light and peripheral vision",
      "Correct — the deck's count and function for rods."],
     ["About 6 million, for dim light and peripheral vision",
      "Six million is the deck's figure for cones."],
     ["About 120 million, for colour vision and sharp acuity",
      "Colour and acuity belong to cones."],
     ["About 20 million, for colour vision in bright light",
      "Neither the count nor the function matches the deck."]],
   c=0, cite=c(28)),

 dict(topic="Photoreceptors", io=IO2, slot="etiology",
   q="Roughly how many cones are there, and where are they concentrated?",
   opts=[
     ["About 6 million, concentrated in the fovea centralis within the macula",
      "Correct — the deck's count and location for cones."],
     ["About 120 million, concentrated in the peripheral retina",
      "That is the rod population and its distribution."],
     ["About 6 million, spread evenly across the whole retina",
      "The deck stresses their concentration at the fovea."],
     ["About 60 million, concentrated at the optic disc",
      "The optic disc has no photoreceptors at all."]],
   c=0, cite=c(28)),

 dict(topic="Retinal pigment epithelium", io=IO1, slot="etiology",
   q="What are the three functions of the retinal pigment epithelium?",
   opts=[
     ["Absorbing scattered light, phagocytosing outer photoreceptor segments, and maintaining the blood-retinal barrier",
      "Correct — the three the deck assigns to this melanin-rich monolayer."],
     ["Producing aqueous humour, nourishing the lens, and setting intraocular pressure",
      "Those are functions of the ciliary body and the drainage pathway."],
     ["Refracting light, filtering ultraviolet radiation, and holding the lens in place",
      "None of these is the pigment epithelium's role."],
     ["Generating action potentials, relaying them to the thalamus, and modulating contrast",
      "Signal generation belongs to the photoreceptors and the neural layers."]],
   c=0, cite=c(28)),

 dict(topic="Retinal interneurons", io=IO1, slot="etiology",
   q="Which three interneuron types modulate the retinal signal before it reaches the ganglion cells?",
   opts=[
     ["Bipolar, horizontal and amacrine cells",
      "Correct — the three the deck lists in the neural network."],
     ["Bipolar, Müller and astrocyte cells",
      "Müller cells and astrocytes are supporting glia, not the deck's modulating trio."],
     ["Horizontal, amacrine and Purkinje cells",
      "Purkinje cells are cerebellar."],
     ["Rod, cone and ganglion cells",
      "Those are the input and output, not the interneurons between them."]],
   c=0, cite=c(28)),

 dict(topic="Retinal interneurons", io=IO1, slot="etiology",
   q="What do the axons of the retinal ganglion cells form?",
   opts=[
     ["The optic nerve", "Correct — ganglion cell axons converge to become cranial nerve two."],
     ["The optic radiation", "That lies beyond the lateral geniculate nucleus."],
     ["The ciliary nerves", "Those are not formed by ganglion cell axons."],
     ["The retinal pigment epithelium", "That is a cell layer, not an axon bundle."]],
   c=0, cite=c(28)),

 dict(topic="Chambers and fluids", io=IO1, slot="etiology",
   q="Where is aqueous humour produced?",
   opts=[
     ["By the non-pigmented epithelium of the ciliary body, into the posterior chamber",
      "Correct — the deck's site and destination for production."],
     ["By the choroid, into the vitreous chamber",
      "The choroid nourishes the retina and does not make aqueous."],
     ["By the lacrimal gland, into the anterior chamber",
      "The lacrimal gland makes tears, which are outside the globe."],
     ["By the retinal pigment epithelium, into the subretinal space",
      "That layer moves fluid but does not produce aqueous humour."]],
   c=0, cite=c(24)),

 dict(topic="Chambers and fluids", io=IO1, slot="etiology",
   q="What is the drainage route for aqueous humour?",
   opts=[
     ["Trabecular meshwork, then the canal of Schlemm, then the episcleral veins",
      "Correct — the deck's full outflow pathway."],
     ["Canal of Schlemm, then the trabecular meshwork, then the choroid",
      "The order of the first two is reversed and the choroid is not the outflow."],
     ["Through the pupil into the vitreous chamber",
      "Aqueous flows through the pupil into the anterior chamber, not backwards."],
     ["Through the retinal pigment epithelium into the choroidal circulation",
      "That describes subretinal fluid movement, not aqueous outflow."]],
   c=0, cite=c(24)),

 dict(topic="Chambers and fluids", io=IO2, slot="etiology",
   q="What does aqueous humour nourish?",
   opts=[
     ["The avascular lens and cornea",
      "Correct — the deck's stated nutritive role for aqueous."],
     ["The retina and the choroid",
      "The choroid nourishes the retina; aqueous does not reach them."],
     ["The optic nerve head",
      "Not a structure the deck says aqueous nourishes."],
     ["The extraocular muscles",
      "Those have their own blood supply."]],
   c=0, cite=c(24)),

 dict(topic="Chambers and fluids", io=IO1, slot="etiology",
   q="What is the vitreous humour made of, and what does it do?",
   opts=[
     ["Water, type two collagen and hyaluronic acid, acting as a shock absorber that presses the retina against the pigment epithelium",
      "Correct — the deck's composition and mechanical function."],
     ["Water and dissolved electrolytes only, acting purely as a filler",
      "The deck names collagen and hyaluronic acid, and gives it a mechanical role."],
     ["A lipid gel that refracts light onto the fovea",
      "Refraction is the work of the cornea and lens."],
     ["A vascular gel that supplies the inner retina",
      "The vitreous is avascular."]],
   c=0, cite=c(24)),

 dict(topic="Lecture logic", io=IO1, slot="etiology",
   q="The deck organises ocular disease from front to back. Which structures does it place in the third and deepest group?",
   opts=[
     ["Posterior segment, optic nerve and retina, which are more susceptible to systemic disease",
      "Correct — the deck's third group and the reason it gives."],
     ["Lids, cornea and conjunctiva, which are more susceptible to systemic disease",
      "Those form the first, most superficial group."],
     ["Iris, lens and anterior segment, which are the deepest structures",
      "That is the second group, not the third."],
     ["Extraocular muscles and orbit, which are least accessible",
      "The deck's third group is the posterior segment and its neural structures."]],
   c=0, cite=c(6)),

 dict(topic="Lecture logic", io=IO1, slot="etiology",
   q="Why does the deck say the outer, easily visible structures are grouped first?",
   opts=[
     ["They are more susceptible to infection, trauma and environmental change",
      "Correct — the deck's reason for the first group."],
     ["They are the only structures visible without an ophthalmoscope",
      "The deck's grouping is by susceptibility rather than by visibility alone."],
     ["They contain the highest density of nerve endings",
      "Not the deck's stated reason."],
     ["They are the last to be affected in systemic disease",
      "The deck ties systemic disease to the deepest group."]],
   c=0, cite=c(6)),

 dict(topic="Optic disc", io=IO1, slot="etiology",
   q="Why is the optic disc a blind spot?",
   opts=[
     ["It has no rods or cones",
      "Correct — the deck's reason, and Webster repeated it in the lecture."],
     ["It is covered by the retinal pigment epithelium",
      "The pigment epithelium does not blind the disc."],
     ["The overlying blood vessels block the light",
      "Vessels cross the retina broadly without creating the blind spot."],
     ["It lies outside the focal plane of the lens",
      "Its position is not what makes it blind."]],
   c=0, cite=c(31)),

 dict(topic="Optical inversion", io=IO2, slot="etiology",
   q="How do the cornea and lens present the visual field on the retina?",
   opts=[
     ["Inverted both vertically and laterally",
      "Correct — the deck describes inversion in both axes."],
     ["Inverted vertically only",
      "The deck names both axes."],
     ["Inverted laterally only",
      "The deck names both axes."],
     ["Upright and unreversed, with the brain doing all the inversion",
      "The optics themselves invert the image."]],
   c=0, cite=c(31)),
]
