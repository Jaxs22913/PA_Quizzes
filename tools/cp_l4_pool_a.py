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
      "Correct — the retina and optic nerve head are central nervous tissue, and the transparent cornea, aqueous, lens and vitreous form an optical path that lets them be inspected in a conscious patient."],
     ["The retina can be biopsied more safely than any other neural tissue",
      "Retinal biopsy is not performed; the point is that the optic nerve head can be examined with no incision at all."],
     ["The cornea contains myelinated tracts that can be seen on slit lamp",
      "The cornea's nerves are unmyelinated and are not what is being viewed; the visible neural tissue is the optic nerve head."],
     ["The sclera is thin enough to transilluminate the whole globe",
      "The sclera is opaque; the view is gained through the clear optical media along the visual axis."]],
   c=0, cite=c(4)),

 dict(topic="Unique features of the eye", io=IO1, slot="etiology",
   q="Which tissue has the highest oxygen consumption and metabolic rate in the body?",
   opts=[
     ["The retina, higher even than the cerebral cortex",
      "Correct — phototransduction and the constant regeneration of photoreceptor outer segments demand more oxygen per gram than any other tissue, cortex included."],
     ["The cerebral cortex, with the retina second",
      "The order is the other way round: the retina exceeds the cerebral cortex in oxygen consumption per gram, which is why it tolerates ischaemia so poorly."],
     ["The cornea, because it is avascular",
      "Being avascular does not make the cornea the highest consumer."],
     ["The ciliary body, because it continuously makes aqueous humour",
      "Aqueous production is not given as the highest metabolic demand."]],
   c=0, cite=c(4)),

 dict(topic="Unique features of the eye", io=IO1, slot="etiology",
   q="Why is the cornea's health responsible for so much of the eye's focusing power?",
   opts=[
     ["About seventy per cent of refraction depends on it",
      "Correct — the greatest change in refractive index in the whole eye occurs at the air-to-cornea interface, so the cornea supplies around seventy per cent of total refraction."],
     ["About thirty per cent of refraction depends on it",
      "Thirty per cent understates it; the air-to-cornea interface provides about seventy per cent of the eye's refractive power."],
     ["It holds the lens in position through the zonules",
      "The zonules arise from the ciliary body, not the cornea."],
     ["It contains the highest density of cones in the eye",
      "Cones are in the retina, concentrated at the fovea."]],
   c=0, cite=c(4)),

 dict(topic="Unique features of the eye", io=IO1, slot="etiology",
   q="How is the avascular cornea oxygenated?",
   opts=[
     ["By direct contact with air and tears",
      "Correct — the cornea must stay clear, so it carries no vessels and takes oxygen dissolved in the tear film directly from the atmosphere, which is why contact lenses must be oxygen-permeable."],
     ["By diffusion from the limbal blood vessels alone",
      "Limbal vessels supply only the extreme periphery; the bulk of the cornea takes oxygen from air dissolved in the tear film."],
     ["By the aqueous humour circulating through the anterior chamber",
      "Aqueous supplies glucose and nutrients to the posterior cornea, but oxygen comes chiefly from the atmosphere through the tear film."],
     ["By the choroidal circulation behind it",
      "The choroid lies at the back of the eye and nourishes the retina."]],
   c=0, cite=c(4)),

 dict(topic="Unique features of the eye", io=IO1, slot="etiology",
   q="What proportion of human knowledge acquisition is estimated is mediated through the eye?",
   opts=[
     ["About eighty-three per cent", "Correct — around eighty-three per cent of what people learn arrives visually, which is why visual loss is so disabling."],
     ["About fifty per cent", "Half understates the visual share, which is estimated at around eighty-three per cent."],
     ["About sixty-five per cent", "Sixty-five per cent is short of the estimate, which is around eighty-three per cent."],
     ["About ninety-five per cent", "Ninety-five per cent overstates it; the estimate is around eighty-three per cent."]],
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
      "Correct — the choroid carries the densest blood flow in the body relative to its mass, supplying the outer retina and photoreceptors, while its melanin absorbs stray light."],
     ["It produces the aqueous humour that fills the anterior chamber",
      "That is the ciliary body's non-pigmented epithelium."],
     ["It controls the size of the pupil",
      "That is the iris."],
     ["It phagocytoses the outer segments of the photoreceptors",
      "That is the retinal pigment epithelium."]],
   c=0, cite=c(7)),

 dict(topic="Physiology of vision", io=IO2, slot="etiology",
   q="What are the three non-negotiable requirements for vision?",
   opts=[
     ["Image formation, neural transmission, and photoreceptor excitation",
      "Correct — light must be focused on the retina, photoreceptors must convert it to a neural signal, and that signal must reach the cortex; failure of any one abolishes vision."],
     ["Image formation, accommodation, and convergence",
      "Accommodation and convergence are part of the near reaction rather than the three requirements."],
     ["Corneal clarity, lens clarity, and a normal intraocular pressure",
      "Clear media and normal pressure support these processes but are not themselves the requirements; image formation, photoreceptor excitation and neural transmission are."],
     ["Pupillary constriction, refraction, and colour discrimination",
      "Pupillary constriction and colour discrimination refine vision rather than being necessary for it; the three requirements are image formation, photoreceptor excitation and neural transmission."]],
   c=0, cite=c(7)),

 dict(topic="Physiology of vision", io=IO2, slot="etiology",
   q="Where must light be focused for an image to form?",
   opts=[
     ["On the retina, after refraction through the cornea and lens",
      "Correct — the cornea provides most of the refraction and the lens fine-tunes it, and only light brought to a focus at the photoreceptor layer produces a sharp image."],
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
      "Correct — the signal passes through the chiasm and tract to the lateral geniculate nucleus, then via the optic radiation to the primary visual cortex in the occipital lobe."],
     ["To the temporal cortex",
      "The temporal lobe carries part of the optic radiation but is not the destination."],
     ["To the frontal eye fields",
      "Those govern gaze rather than receiving the visual image."],
     ["To the superior colliculus alone",
      "The superior colliculus mediates reflex gaze; conscious vision is processed in the occipital cortex."]],
   c=0, cite=c(7)),

 dict(topic="Photoreceptors", io=IO2, slot="etiology",
   q="What do photons do to rods and cones?",
   opts=[
     ["They stimulate them to convert light into hyperpolarising action potentials",
      "Correct — photoreceptors are unusual in that light closes sodium channels, so the cell hyperpolarises and reduces its tonic glutamate release, which is the signal passed onward."],
     ["They stimulate them to convert light into depolarising action potentials",
      "Photoreceptors hyperpolarise in response to light rather than depolarising, which is the reverse of most sensory receptors."],
     ["They are absorbed by the retinal pigment epithelium before reaching them",
      "The pigment epithelium absorbs scattered light, not the signal itself."],
     ["They trigger release of aqueous humour into the posterior chamber",
      "Aqueous production has nothing to do with photoreception."]],
   c=0, cite=c(7)),

 dict(topic="Photoreceptors", io=IO2, slot="etiology",
   q="Roughly how many rods are there, and what are they for?",
   opts=[
     ["About 120 million, for dim light and peripheral vision",
      "Correct — rods vastly outnumber cones and contain a pigment sensitive enough to respond to single photons, which suits them to dim light and the peripheral retina where they predominate."],
     ["About 6 million, for dim light and peripheral vision",
      "Six million is the cone population; rods number around 120 million."],
     ["About 120 million, for colour vision and sharp acuity",
      "Colour and acuity belong to cones."],
     ["About 20 million, for colour vision in bright light",
      "Neither figure fits: rods number around 120 million and serve dim light and peripheral vision, not colour."]],
   c=0, cite=c(28)),

 dict(topic="Photoreceptors", io=IO2, slot="etiology",
   q="Roughly how many cones are there, and where are they concentrated?",
   opts=[
     ["About 6 million, concentrated in the fovea centralis within the macula",
      "Correct — around six million cones are packed most densely at the fovea, where each connects to its own ganglion cell, giving the sharp central acuity and colour vision."],
     ["About 120 million, concentrated in the peripheral retina",
      "That is the rod population and its distribution."],
     ["About 6 million, spread evenly across the whole retina",
      "Cones are heavily concentrated at the fovea rather than spread evenly, which is why acuity falls off so sharply away from fixation."],
     ["About 60 million, concentrated at the optic disc",
      "The optic disc contains no photoreceptors at all; cones number around six million and cluster at the fovea."]],
   c=0, cite=c(28)),

 dict(topic="Retinal pigment epithelium", io=IO1, slot="etiology",
   q="What are the three functions of the retinal pigment epithelium?",
   opts=[
     ["Absorbing scattered light, phagocytosing outer photoreceptor segments, and maintaining the blood-retinal barrier",
      "Correct — its melanin absorbs stray light to sharpen the image, it digests the shed tips of photoreceptor outer segments, and its tight junctions form the outer blood-retinal barrier."],
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
      "Correct — bipolar cells carry the signal vertically while horizontal and amacrine cells connect laterally, sharpening contrast and shaping the response before it reaches the ganglion cells."],
     ["Bipolar, Müller and astrocyte cells",
      "Müller cells and astrocytes are supporting glia that maintain the retina rather than processing the signal."],
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
      "Correct — the non-pigmented ciliary epithelium secretes aqueous into the posterior chamber, from where it passes through the pupil to the anterior chamber and drains at the angle."],
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
      "Correct — aqueous filters through the trabecular meshwork at the iridocorneal angle into the canal of Schlemm and then into episcleral veins, and resistance anywhere along this path raises intraocular pressure."],
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
      "Correct — both structures must stay transparent, so neither can carry blood vessels, and aqueous delivers their glucose and oxygen and removes their waste."],
     ["The retina and the choroid",
      "The choroid nourishes the retina; aqueous does not reach them."],
     ["The optic nerve head",
      "The optic nerve head is supplied by the posterior ciliary circulation; aqueous nourishes the avascular lens and cornea."],
     ["The extraocular muscles",
      "Those have their own blood supply."]],
   c=0, cite=c(24)),

 dict(topic="Chambers and fluids", io=IO1, slot="etiology",
   q="What is the vitreous humour made of, and what does it do?",
   opts=[
     ["Water, type two collagen and hyaluronic acid, acting as a shock absorber that presses the retina against the pigment epithelium",
      "Correct — the collagen and hyaluronic acid network holds water in a gel that cushions the globe and keeps the neurosensory retina apposed to the pigment epithelium."],
     ["Water and dissolved electrolytes only, acting purely as a filler",
      "The vitreous is a structured gel of type two collagen and hyaluronic acid rather than simple fluid, and that structure is what holds the retina in place."],
     ["A lipid gel that refracts light onto the fovea",
      "Refraction is the work of the cornea and lens."],
     ["A vascular gel that supplies the inner retina",
      "The vitreous is avascular."]],
   c=0, cite=c(24)),

 dict(topic="Lecture logic", io=IO1, slot="etiology",
   q="Ocular disease can be organised from front to back. Which structures fall in the third and deepest group?",
   opts=[
     ["Posterior segment, optic nerve and retina, which are more susceptible to systemic disease",
      "Correct — the posterior segment is richly vascularised and neural, so systemic vascular, metabolic and demyelinating disease shows itself there first."],
     ["Lids, cornea and conjunctiva, which are more susceptible to systemic disease",
      "Those form the first, most superficial group."],
     ["Iris, lens and anterior segment, which are the deepest structures",
      "That is the second group, not the third."],
     ["Extraocular muscles and orbit, which are least accessible",
      "The orbit and extraocular muscles sit outside this front-to-back scheme; the deepest group is the posterior segment, optic nerve and retina."]],
   c=0, cite=c(6)),

 dict(topic="Lecture logic", io=IO1, slot="etiology",
   q="Why are the outer, easily visible structures grouped first?",
   opts=[
     ["They are more susceptible to infection, trauma and environmental change",
      "Correct — the lids, conjunctiva and cornea face the outside world directly, so they bear the brunt of pathogens, foreign bodies, ultraviolet light and drying."],
     ["They are the only structures visible without an ophthalmoscope",
      "Visibility is incidental; the grouping reflects that exposed structures are the ones exposed to infection, trauma and the environment."],
     ["They contain the highest density of nerve endings",
      "The cornea is densely innervated, but the grouping reflects exposure to infection, trauma and environmental insult."],
     ["They are the last to be affected in systemic disease",
      "Systemic disease shows itself in the DEEPEST group, the posterior segment; the outer structures are grouped for their environmental exposure."]],
   c=0, cite=c(6)),

 dict(topic="Optic disc", io=IO1, slot="etiology",
   q="Why is the optic disc a blind spot?",
   opts=[
     ["It has no rods or cones",
      "Correct — the disc is where ganglion cell axons converge to leave the eye, so there is no room for photoreceptors and no light is detected there."],
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
      "Correct — light crossing at the nodal point reverses the image in both axes, so the superior field falls on the inferior retina and the nasal field on the temporal retina."],
     ["Inverted vertically only",
      "Inversion occurs in both axes, not just vertically; the nasal field falls on the temporal retina as well."],
     ["Inverted laterally only",
      "Inversion occurs in both axes, not just laterally; the superior field also falls on the inferior retina."],
     ["Upright and unreversed, with the brain doing all the inversion",
      "The optics themselves invert the image."]],
   c=0, cite=c(31)),
]
