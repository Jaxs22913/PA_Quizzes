# CMS I Exam 2, Lecture 11 Neuro-Ophthalmology — VIGNETTE pool, part B.
SRC = "11. Neuro-Ophthalmology STUDENT VERSION 2026.pptx"
def c(n): return f"{SRC}, Slide {n}"
IO = ("a — Describe the pupillary pathways, cranial nerve palsies and chiasmal lesions, "
      "and identify medical care strategies for neuro-ophthalmological disorders")

POOL_B = [
 dict(topic="Light-near dissociation", io=IO, lead="diagnosis",
   q="A 50-year-old man's pupils do not react to light but constrict normally when he focuses on a near object. What is this phenomenon called?",
   opts=[
     ["Light-near dissociation", "Correct. The near pathway skips part of the route the light pathway takes."],
     ["Relative afferent pupillary defect", "That is detected by swinging a light between the eyes."],
     ["Dilation lag", "That is the Horner syndrome finding in darkness."],
     ["Sector paralysis", "That is a slit-lamp finding in an Adie pupil."],
     ["Anisocoria", "That simply means unequal pupils."]],
   c=0, cite=c(19)),

 dict(topic="Accommodation", io=IO, lead="diagnosis",
   q="A patient shifts gaze from a distant sign to a book. Which three changes does the lecture describe?",
   opts=[
     ["Lens thickens, pupils constrict, eyes converge", "Correct. The near response acts on lens, pupil and globes together."],
     ["Lens flattens, pupils dilate, eyes diverge", "That is the opposite of the near response."],
     ["Lens thickens, pupils dilate, eyes converge", "The pupils constrict rather than dilate for near focus."],
     ["Lens flattens, pupils constrict, eyes converge", "The lens becomes more convex, not flatter."],
     ["Only the lens changes shape", "All three components are described."]],
   c=0, cite=c(18)),

 dict(topic="Accommodation", io=IO, lead="diagnosis",
   q="Which muscle contracts to make the lens more convex during near focus?",
   opts=[
     ["Ciliary muscle", "Correct, increasing the refractive power of the lens."],
     ["Iris sphincter", "That constricts the pupil."],
     ["Radial muscle of the iris", "That dilates the pupil."],
     ["Medial rectus", "That adducts the globe for convergence."],
     ["Levator palpebrae", "That elevates the eyelid."]],
   c=0, cite=c(18)),

 dict(topic="Pupillary pathway", io=IO, lead="diagnosis",
   q="Where do impulses from the retinal ganglion cells first synapse in the light reflex pathway?",
   opts=[
     ["Pretectal nuclei", "Correct, and each pretectal nucleus then projects to both Edinger-Westphal nuclei."],
     ["Ciliary ganglion", "That is the efferent relay, further along."],
     ["Lateral geniculate nucleus", "That is on the visual pathway to cortex, used by the near response."],
     ["Superior colliculus", "The Argyll Robertson lesion is suspected there, but it is not the first synapse."],
     ["Occipital cortex", "Vision reaches cortex, but the light reflex does not require it."]],
   c=0, cite=c(11)),

 dict(topic="Pupillary pathway", io=IO, lead="diagnosis",
   q="Parasympathetic preganglionic fibres leave the Edinger-Westphal nucleus and travel along which nerve?",
   opts=[
     ["Cranial nerve three", "Correct, synapsing in the ipsilateral ciliary ganglion within the orbit."],
     ["Cranial nerve two", "That is the afferent limb."],
     ["Cranial nerve four", "That supplies superior oblique."],
     ["Cranial nerve six", "That supplies lateral rectus."],
     ["Cranial nerve seven", "That closes the eyelids."]],
   c=0, cite=c(11)),

 dict(topic="Sympathetic pathway", io=IO, lead="diagnosis",
   q="Where do the first-order sympathetic neurons synapse on their way to the pupil?",
   opts=[
     ["Ciliospinal centre of Budge", "Correct, at C8 to T2."],
     ["Ciliary ganglion", "That is the parasympathetic relay."],
     ["Superior cervical ganglion", "That is where second-order neurons synapse with third-order."],
     ["Pretectal nucleus", "That belongs to the afferent light reflex."],
     ["Edinger-Westphal nucleus", "That is the parasympathetic origin."]],
   c=0, cite=c(13)),

 dict(topic="Sympathetic pathway", io=IO, lead="diagnosis",
   q="Which anatomical relationship explains why an apical lung tumour can cause Horner syndrome?",
   opts=[
     ["Second-order fibres loop over the lung apex", "Correct, passing under the subclavian artery."],
     ["First-order fibres run through the lung", "First-order neurons run from hypothalamus to cord."],
     ["Third-order fibres cross the pleura", "Third-order fibres travel with the carotid."],
     ["The vagus carries sympathetic fibres", "It does not carry this pathway."],
     ["The phrenic nerve relays to the eye", "It has no role in this pathway."]],
   c=0, cite=c(13)),

 dict(topic="Pupil size", io=IO, lead="diagnosis",
   q="You cover a healthy person's right eye and watch the left pupil. What happens, and why?",
   opts=[
     ["It enlarges, as average illumination halves", "Correct. Pupil size reflects an average of the light detected by both eyes."],
     ["It constricts, as the covered eye is dark", "Covering reduces total light, so the pupil enlarges."],
     ["It is unchanged, as each eye acts alone", "The lecture makes the point that size is an average across both eyes."],
     ["It oscillates rhythmically", "That describes nystagmus, not a pupil response."],
     ["It enlarges only in the covered eye", "The uncovered pupil is the one observed to change."]],
   c=0, cite=c(7)),

 dict(topic="Third nerve anatomy", io=IO, lead="diagnosis",
   q="A lesion affects only the superior division of the oculomotor nerve. Which deficits result?",
   opts=[
     ["Ptosis and impaired elevation", "Correct. The superior division supplies levator palpebrae and superior rectus."],
     ["Mydriasis and impaired adduction", "Those follow inferior division involvement."],
     ["Impaired depression and extorsion", "Inferior rectus and inferior oblique are inferior division."],
     ["Impaired abduction", "That is the sixth nerve."],
     ["Impaired intorsion", "That is the fourth nerve."]],
   c=0, cite=c(39)),

 dict(topic="Third nerve anatomy", io=IO, lead="diagnosis",
   q="Which fibres travel with the inferior division of the oculomotor nerve to the ciliary ganglion?",
   opts=[
     ["Parasympathetic fibres", "Correct, and they innervate the iris sphincter for pupillary constriction."],
     ["Sympathetic fibres", "Those travel with the carotid, not the third nerve."],
     ["Afferent visual fibres", "Those run in the optic nerve."],
     ["Motor fibres to lateral rectus", "That muscle is supplied by the sixth nerve."],
     ["Motor fibres to superior oblique", "That muscle is supplied by the fourth nerve."]],
   c=0, cite=c(39)),

 dict(topic="Ptosis anatomy", io=IO, lead="diagnosis",
   q="Which structure gives the extra one to two millimetres of lid elevation when a patient is startled?",
   opts=[
     ["Muller's muscle", "Correct, and it is sympathetically innervated, which is why Horner syndrome causes mild ptosis."],
     ["Levator palpebrae superioris", "That is the main elevator, supplied by the third nerve."],
     ["Orbicularis oculi", "That closes the lids and is supplied by the seventh nerve."],
     ["Superior rectus", "That elevates the globe, not the lid."],
     ["Ciliary muscle", "That alters lens shape."]],
   c=0, cite=c(48)),

 dict(topic="Care strategies", io=IO, lead="next step",
   q="A patient presents with a new neuro-ophthalmological complaint. Which sequence does the lecture summarise?",
   opts=[
     ["History and examination, then imaging if indicated", "Correct, with ophthalmology and appropriate specialist referral."],
     ["Imaging first, then history", "The lecture begins with a thorough history and physical."],
     ["Laboratory testing before examination", "Labs come after, and only if indicated."],
     ["Immediate surgical referral", "Referral is to ophthalmology and other specialists as appropriate."],
     ["Observation for six months in all cases", "That interval applies to traumatic cranial nerve palsies."]],
   c=0, cite=c(54)),

 dict(topic="Cranial nerve palsy", io=IO, lead="treatment",
   q="A 35-year-old man has a traumatic fourth nerve palsy with binocular diplopia. What does the lecture advise in the interim?",
   opts=[
     ["Patch one eye", "Correct, to relieve binocular diplopia while observing for about six months."],
     ["Immediate strabismus surgery", "Corrective treatment is considered only after roughly six months."],
     ["Start systemic corticosteroids", "Those are for giant cell arteritis, not a traumatic palsy."],
     ["Prescribe pilocarpine drops", "That is a pupil test, not a treatment for diplopia."],
     ["Arrange urgent angiography", "That is for a pupil-involved third nerve palsy."]],
   c=0, cite=c(46)),

 dict(topic="Cranial nerve palsy", io=IO, lead="education",
   q="A parent asks about patching for a young child with a congenital palsy. What does the lecture specify?",
   opts=[
     ["It should be supervised by ophthalmology", "Correct, especially under about five years of age."],
     ["It should be continuous until resolution", "The lecture does not prescribe continuous patching."],
     ["It is contraindicated in children", "Patching is used, but under specialist care."],
     ["It should alternate hourly at home", "No such regimen is given."],
     ["It is unnecessary before school age", "The caution is about supervision, not deferral."]],
   c=0, cite=c(46)),

 dict(topic="Adie pupil", io=IO, lead="diagnosis",
   q="Which slit-lamp finding does the lecture associate with an Adie pupil?",
   opts=[
     ["Sector paralysis of the iris", "Correct, alongside decreased regional corneal sensation."],
     ["Keratic precipitates", "Those are seen in anterior uveitis."],
     ["A hazy cornea", "That suggests acute angle-closure glaucoma."],
     ["A cherry-red spot", "That is a retinal finding in central retinal artery occlusion."],
     ["Cotton wool spots", "Those are retinal findings, not iris findings."]],
   c=0, cite=c(36)),

 dict(topic="Horner syndrome", io=IO, lead="diagnosis",
   q="Why may anhidrosis be absent in a patient with confirmed Horner syndrome?",
   opts=[
     ["It depends where the lesion sits", "Correct. The triad may be incomplete depending on the level along the pathway."],
     ["Anhidrosis only occurs in children", "Age is not the determinant."],
     ["Sweating is parasympathetic", "The sudomotor fibres involved are sympathetic."],
     ["It requires bilateral lesions", "Horner syndrome is typically unilateral."],
     ["It is only seen with tumours", "Aetiology does not determine its presence."]],
   c=0, cite=c(28)),

 dict(topic="Nystagmus", io=IO, lead="diagnosis",
   q="A 3-month-old infant is noted to have nystagmus. What does the lecture advise?",
   opts=[
     ["Refer for work-up", "Correct. Infants and young children with nystagmus warrant referral."],
     ["Reassure, as it is always physiologic", "Infantile nystagmus specifically warrants referral."],
     ["Repeat examination at age five", "Delay is not what the lecture advises."],
     ["Start patching immediately", "Patching addresses diplopia and amblyopia, not this."],
     ["Order a lumbar puncture", "Not an indicated first step."]],
   c=0, cite=c(5)),

 dict(topic="Nystagmus", io=IO, lead="diagnosis",
   q="Which type of nystagmus does the lecture call the most common form?",
   opts=[
     ["Horizontal jerk", "Correct, with eyes moving slowly to one side and quickly back."],
     ["Vertical jerk", "A recognised trajectory but not the most common."],
     ["Torsional jerk", "Also recognised but not the most common."],
     ["Pendular", "The lecture's classification centres on jerk nystagmus."],
     ["Upbeat", "That is specifically flagged as concerning rather than common."]],
   c=0, cite=c(4)),

 dict(topic="Anisocoria", io=IO, lead="diagnosis",
   q="A patient has anisocoria that is greater in bright light. Which pupil is abnormal?",
   opts=[
     ["The larger pupil", "Correct. If it fails to constrict in light, the large one is at fault."],
     ["The smaller pupil", "That is abnormal when the difference is greater in darkness."],
     ["Neither, this is physiologic", "Physiologic anisocoria is equal in light and dark."],
     ["Both are equally abnormal", "The asymmetry localises the problem to one side."],
     ["It cannot be determined", "The light and dark comparison determines it."]],
   c=0, cite=c(20)),

 dict(topic="Anisocoria", io=IO, lead="diagnosis",
   q="A patient's right pupil fails to dilate well in the dark. Which pupil is abnormal, and which pathway is implicated?",
   opts=[
     ["The small pupil, sympathetic", "Correct. Failure to dilate points to the sympathetic supply."],
     ["The large pupil, parasympathetic", "That applies when the large pupil fails to constrict in light."],
     ["The small pupil, parasympathetic", "The parasympathetic limb constricts rather than dilates."],
     ["The large pupil, sympathetic", "The sympathetic limb dilates, so failure shows as a small pupil."],
     ["Neither, this is normal", "Poor dilation in darkness is abnormal."]],
   c=0, cite=c(20)),

 dict(topic="Marcus Gunn pupil", io=IO, lead="diagnosis",
   q="A patient has a right relative afferent pupillary defect. Which condition on this list would explain it?",
   opts=[
     ["Optic neuritis", "Correct. An optic nerve lesion is a classic afferent cause."],
     ["Horner syndrome", "That is a sympathetic efferent lesion."],
     ["Cataract", "A media opacity does not usually produce a true afferent defect."],
     ["Third nerve palsy", "That is a parasympathetic efferent lesion."],
     ["Physiologic anisocoria", "That is a benign size difference."]],
   c=0, cite=c(26)),

 dict(topic="Argyll Robertson pupil", io=IO, lead="diagnosis",
   q="Where does the lecture suspect the lesion lies in Argyll Robertson pupil?",
   opts=[
     ["Dorsal midbrain", "Correct, in the pretectal area of the superior colliculus."],
     ["Ciliary ganglion", "That is the Adie pupil lesion."],
     ["Optic chiasm", "That produces field loss rather than this pupil."],
     ["Cavernous sinus", "That is a third-order Horner location."],
     ["Lung apex", "That is a second-order Horner location."]],
   c=0, cite=c(33)),

 dict(topic="Third nerve palsy", io=IO, lead="next step",
   q="A 58-year-old woman has a pupil-sparing third nerve palsy. How urgent is imaging, per the lecture?",
   opts=[
     ["Imaging, but not stat", "Correct. Reassurance and imaging, without the emergency pathway."],
     ["Stat angiography", "That is reserved for pupil involvement."],
     ["No imaging at all", "Imaging is still obtained."],
     ["Imaging only if symptoms persist beyond six months", "That interval concerns traumatic palsies."],
     ["Lumbar puncture before imaging", "Not indicated here."]],
   c=0, cite=c(41)),

 dict(topic="Fourth nerve palsy", io=IO, lead="diagnosis",
   q="A 45-year-old man has an isolated fourth nerve palsy with no history of trauma. Which cause does the lecture name as most common?",
   opts=[
     ["Congenital", "Correct. Isolated fourth nerve palsy is most commonly congenital, even in adults."],
     ["Microvascular disease", "That is an acquired cause, alongside trauma."],
     ["Intracranial tumour", "That is the leading cause of sixth nerve palsy in children."],
     ["Aneurysm", "That is the dreaded cause of a third nerve palsy."],
     ["Giant cell arteritis", "Not a cause named for this palsy."]],
   c=0, cite=c(43)),

 dict(topic="Visual fields", io=IO, lead="diagnosis",
   q="A 62-year-old woman has lost vision in the upper left quadrant of both eyes. What is this defect called?",
   opts=[
     ["Superior quadrantanopia", "Correct, a partial homonymous defect."],
     ["Bitemporal hemianopsia", "That is loss of both outer halves."],
     ["Homonymous hemianopsia", "That is a full half-field loss on the same side."],
     ["Total monocular blindness", "That affects one eye entirely."],
     ["Central scotoma", "That is a central rather than quadrantic defect."]],
   c=0, cite=c(52)),

 dict(topic="Ptosis", io=IO, lead="diagnosis",
   q="Which feature distinguishes ptosis from a third nerve palsy from ptosis of Horner syndrome?",
   opts=[
     ["Levator function", "Correct. It is reduced in third nerve palsy and normal in Horner syndrome."],
     ["Laterality", "Both are usually unilateral."],
     ["Presence of ptosis itself", "Both produce ptosis."],
     ["Time of day", "Diurnal variation points to myasthenia gravis."],
     ["Patient age", "Age does not separate them."]],
   c=0, cite=c(49)),

 dict(topic="Horner syndrome", io=IO, lead="diagnosis",
   q="Which receptor action explains why apraclonidine dilates a Horner pupil?",
   opts=[
     ["Alpha-two greater than alpha-one activity", "Correct, acting on a denervated, supersensitive pupil."],
     ["Pure beta blockade", "Beta blockade is used to lower intraocular pressure, not to test this."],
     ["Muscarinic agonism", "That would constrict rather than dilate."],
     ["Anticholinesterase activity", "That raises acetylcholine and constricts the pupil."],
     ["Prostaglandin analogue activity", "Those are used in glaucoma."]],
   c=0, cite=c(28)),

 dict(topic="Nystagmus", io=IO, lead="diagnosis",
   q="A 40-year-old man has new upbeat nystagmus. How does the lecture classify this finding?",
   opts=[
     ["Concerning and non-physiologic", "Correct, and it warrants work-up in adults."],
     ["Normal physiologic gaze-evoked", "That is a different, benign pattern."],
     ["Latent nystagmus", "That is a form of horizontal nystagmus."],
     ["Spasmus nutans", "That is an infantile horizontal pattern."],
     ["Congenital and benign", "New onset in adulthood is not congenital."]],
   c=0, cite=c(5)),

 dict(topic="Horner syndrome", io=IO, lead="diagnosis",
   q="How long after dimming the lights is the anisocoria of Horner syndrome most evident?",
   opts=[
     ["Within the first few seconds", "Correct, when a normal pupil would dilate rapidly and actively."],
     ["After a full minute", "By then passive dilation has narrowed the difference."],
     ["Only in bright light", "The difference is accentuated in darkness."],
     ["Only after pharmacologic testing", "The lag is visible clinically."],
     ["It is constant regardless of lighting", "That describes physiologic anisocoria."]],
   c=0, cite=c(29)),

 dict(topic="Sixth nerve palsy", io=IO, lead="diagnosis",
   q="A 61-year-old man with hypertension and diabetes cannot abduct his right eye. Which cause is most likely?",
   opts=[
     ["Microvascular disease", "Correct. In adults that is the commonest cause of a sixth nerve palsy."],
     ["Intracranial tumour", "That leads in children rather than adults."],
     ["Skull base fracture", "That requires major trauma."],
     ["Congenital palsy", "New onset in an adult is not congenital."],
     ["Aneurysm", "That is associated with third nerve palsy."]],
   c=0, cite=c(45)),
]
