# CMS I Exam 2, Lecture 11 Neuro-Ophthalmology — VIGNETTE pool, part A.
# Built to the exam standard Jaxon set 2026-08-26/27: FIVE options, a patient in
# every stem, each wrong option refuted on its own terms, options kept short
# (reference median 19 chars, max 66) with the reasoning in the explanation.
SRC = "11. Neuro-Ophthalmology STUDENT VERSION 2026.pptx"
def c(n): return f"{SRC}, Slide {n}"
IO = ("a — Describe the pupillary pathways, cranial nerve palsies and chiasmal lesions, "
      "and identify medical care strategies for neuro-ophthalmological disorders")

POOL_A = [

 dict(topic="Horner syndrome", io=IO, lead="diagnosis",
   q="A 54-year-old man has a droopy right lid and a small right pupil. The right side of his face does not sweat. The anisocoria is most obvious in the first few seconds after the lights are dimmed. Which is the most likely diagnosis?",
   opts=[
     ["Horner syndrome", "Correct. Ptosis, miosis and anhidrosis, with dilation lag as the hallmark of the miosis."],
     ["Adie tonic pupil", "That pupil is large with a poor light reaction, not small."],
     ["Argyll Robertson pupil", "Those pupils are small but bilateral, and react to near but not to light."],
     ["Third nerve palsy", "That gives a large pupil with impaired eye movement, not a small one."],
     ["Physiologic anisocoria", "That is equal in light and dark and shows no dilation lag."]],
   c=0, cite=c(28)),

 dict(topic="Horner syndrome", io=IO, lead="test",
   q="A 61-year-old woman has ptosis and miosis on the left. You want to confirm the diagnosis in clinic. Which test does the lecture name?",
   opts=[
     ["Dilute apraclonidine drops", "Correct. Ineffective in a normal pupil, they dilate the Horner pupil in most patients."],
     ["Dilute pilocarpine drops", "That is the test for an Adie tonic pupil, which is supersensitive to it."],
     ["Fluorescein staining", "That assesses corneal epithelial defects, not the sympathetic pathway."],
     ["Tonometry", "That measures intraocular pressure."],
     ["Swinging flashlight test", "That detects an afferent defect, not a sympathetic one."]],
   c=0, cite=c(28)),

 dict(topic="Horner syndrome", io=IO, lead="next step",
   q="A 47-year-old man develops left ptosis and miosis hours after a whiplash injury, with neck pain and left arm numbness. Which underlying cause should be excluded first?",
   opts=[
     ["Carotid artery dissection", "Correct. A third-order Horner syndrome, and the reason this presentation is urgent."],
     ["Pancoast tumour", "That is a second-order cause and would not follow acute trauma this way."],
     ["Brainstem stroke", "That is a first-order cause, usually with other brainstem signs."],
     ["Cavernous sinus thrombosis", "Possible at third order, but trauma with neck pain points to dissection."],
     ["Thyroid carcinoma", "A second-order cause, but not one that presents acutely after whiplash."]],
   c=0, cite=c(15)),

 dict(topic="Horner syndrome", io=IO, lead="diagnosis",
   q="A 68-year-old smoker has a two-month history of right shoulder pain, and now has right ptosis and miosis. Which lesion location does this combination suggest?",
   opts=[
     ["Second-order neuron", "Correct. The preganglionic neuron loops over the lung apex, where a Pancoast tumour reaches it."],
     ["First-order neuron", "Those lesions are brainstem strokes, tumours or cord lesions above T1."],
     ["Third-order neuron", "Those are carotid dissection or cavernous sinus thrombosis."],
     ["Ciliary ganglion", "That is the parasympathetic relay, and damage there gives an Adie pupil."],
     ["Edinger-Westphal nucleus", "That is the parasympathetic origin, not the sympathetic pathway."]],
   c=0, cite=c(30)),

 dict(topic="Marcus Gunn pupil", io=IO, lead="diagnosis",
   q="A 29-year-old woman has blurred vision in the right eye. On swinging a light from the left eye to the right, both pupils dilate. Which is the most likely diagnosis?",
   opts=[
     ["Relative afferent pupillary defect", "Correct. A Marcus Gunn pupil, meaning an afferent lesion at the retina or optic nerve."],
     ["Horner syndrome", "That is a sympathetic efferent problem and does not produce this response."],
     ["Adie tonic pupil", "That is a parasympathetic efferent problem at the ciliary ganglion."],
     ["Third nerve palsy", "That would give a fixed dilated pupil with eye movement deficits."],
     ["Physiologic anisocoria", "That is a benign size difference with normal reactions."]],
   c=0, cite=c(26)),

 dict(topic="Marcus Gunn pupil", io=IO, lead="diagnosis",
   q="A 33-year-old woman has a relative afferent pupillary defect on the left. Where does the lecture place the lesion?",
   opts=[
     ["Retina or optic nerve", "Correct, and therefore pre-chiasmal."],
     ["Optic chiasm", "A chiasmal lesion gives a field defect rather than this pupillary sign."],
     ["Optic tract", "That is post-chiasmal and does not typically produce this."],
     ["Ciliary ganglion", "That is efferent, and damage there gives an Adie pupil."],
     ["Occipital cortex", "Cortical lesions spare the pupillary reflex."]],
   c=0, cite=c(26)),

 dict(topic="Argyll Robertson pupil", io=IO, lead="diagnosis",
   q="A 52-year-old man has small pupils bilaterally that do not constrict to light but constrict briskly when he looks at a near target. He also has sensory ataxia. Which is the most likely diagnosis?",
   opts=[
     ["Argyll Robertson pupil", "Correct. Light-near dissociation with miosis, classically tertiary syphilis with tabes dorsalis."],
     ["Adie tonic pupil", "That pupil is large and its near response is slow, not brisk."],
     ["Horner syndrome", "That is unilateral miosis with ptosis and a normal light reaction."],
     ["Third nerve palsy", "That gives mydriasis with eye movement deficits."],
     ["Bilateral optic neuritis", "That impairs the afferent limb and would not spare the near response this way."]],
   c=0, cite=c(32)),

 dict(topic="Argyll Robertson pupil", io=IO, lead="test",
   q="A 49-year-old man has bilateral miosis with light-near dissociation. Which condition should be tested for first?",
   opts=[
     ["Tertiary syphilis", "Correct. It is the classic association the lecture names."],
     ["Multiple sclerosis", "Listed as a possible cause, but syphilis is the classic one."],
     ["Diabetes mellitus", "Also listed, but not the classic association."],
     ["Neurosarcoidosis", "Another listed cause, again not the classic one."],
     ["Giant cell arteritis", "Not a cause of light-near dissociation in this lecture."]],
   c=0, cite=c(32)),

 dict(topic="Adie tonic pupil", io=IO, lead="diagnosis",
   q="A 34-year-old woman has a large right pupil that reacts poorly to light, constricts slowly to a near target and re-dilates slowly. Her Achilles reflexes are absent. Which is the most likely diagnosis?",
   opts=[
     ["Adie tonic pupil", "Correct. Ciliary ganglion damage with aberrant reinnervation, and absent deep tendon reflexes go with it."],
     ["Third nerve palsy", "There is no ptosis and no extraocular weakness here."],
     ["Pharmacologic mydriasis", "That pupil is very large and does not constrict to near either."],
     ["Argyll Robertson pupil", "Those pupils are small and bilateral."],
     ["Horner syndrome", "That gives a small pupil, not a large one."]],
   c=0, cite=c(35)),

 dict(topic="Adie tonic pupil", io=IO, lead="test",
   q="A 31-year-old woman has a unilateral large, poorly reactive pupil. Which bedside test does the lecture use to support an Adie pupil?",
   opts=[
     ["Dilute pilocarpine drops", "Correct. The denervated pupil is supersensitive and constricts."],
     ["Dilute apraclonidine drops", "That is the Horner syndrome test."],
     ["Tonometry", "That measures intraocular pressure."],
     ["Fluorescein staining", "That looks at the corneal surface."],
     ["Gonioscopy", "That assesses the drainage angle."]],
   c=0, cite=c(36)),

 dict(topic="Adie tonic pupil", io=IO, lead="diagnosis",
   q="A 30-year-old woman with a large tonic pupil has normal eyelid position and full eye movements. Which finding argues against a third nerve palsy?",
   opts=[
     ["No ptosis and no extraocular weakness", "Correct. The lecture makes that absence the discriminator."],
     ["Photophobia", "That can occur with an Adie pupil and does not separate the two."],
     ["Blurred near vision", "Also common to both and not discriminating."],
     ["Unilateral involvement", "Both conditions are usually unilateral."],
     ["Female sex in the thirties", "Typical of Adie pupil but not a finding that excludes a palsy."]],
   c=0, cite=c(36)),

 dict(topic="Pharmacologic mydriasis", io=IO, lead="diagnosis",
   q="A 58-year-old woman using nebulised ipratropium has a right pupil of 9 mm that does not constrict to light. Eye movements and lid position are normal. Which is the most likely cause?",
   opts=[
     ["Pharmacologic mydriasis", "Correct. An anticholinergic reaching the eye gives a very large, unreactive pupil with nothing else wrong."],
     ["Third nerve palsy", "That would involve the lid and eye movements."],
     ["Adie tonic pupil", "That still constricts slowly to a near target."],
     ["Acute angle-closure glaucoma", "That is painful with a hazy cornea and reduced vision."],
     ["Marcus Gunn pupil", "That is an afferent defect with normal pupil size."]],
   c=0, cite=c(22)),

 dict(topic="Third nerve palsy", io=IO, lead="next step",
   q="A 63-year-old man has sudden ptosis, a dilated unreactive left pupil, and the eye rests down and out. Which is the most appropriate next step?",
   opts=[
     ["Stat computed tomography angiography", "Correct. A pupil-involved third nerve palsy is an aneurysm until proven otherwise."],
     ["Routine outpatient imaging", "That is acceptable only when the pupil is spared."],
     ["Reassurance and review in six months", "Observation applies to traumatic palsies, not an acute pupil-involved one."],
     ["Temporal artery biopsy", "That investigates giant cell arteritis, a different presentation."],
     ["Lumbar puncture", "That is for suspected raised intracranial pressure."]],
   c=0, cite=c(41)),

 dict(topic="Third nerve palsy", io=IO, lead="diagnosis",
   q="A 66-year-old man with long-standing diabetes has a third nerve palsy with a normal, reactive pupil. Which cause does the lecture name as most common?",
   opts=[
     ["Microvascular disease", "Correct, and pupil sparing is what makes it the likely one here."],
     ["Posterior communicating artery aneurysm", "That is the most dreaded cause, and it typically involves the pupil."],
     ["Uncal herniation", "That would come with depressed consciousness."],
     ["Severe head trauma", "There is no trauma in this history."],
     ["Migraine", "Listed as a cause but not the most common one."]],
   c=0, cite=c(40)),

 dict(topic="Third nerve palsy", io=IO, lead="diagnosis",
   q="Which structure does the lecture identify as the most dreaded cause of a pupil-involved third nerve palsy?",
   opts=[
     ["Posterior communicating artery aneurysm", "Correct, with rupture threatened within hours to days."],
     ["Internal carotid artery dissection", "That causes a third-order Horner syndrome instead."],
     ["Middle cerebral artery aneurysm", "Not the vessel the lecture names."],
     ["Cavernous sinus thrombosis", "A third-order Horner cause in this lecture."],
     ["Basilar artery occlusion", "Not named in relation to this palsy."]],
   c=0, cite=c(40)),

 dict(topic="Fourth nerve palsy", io=IO, lead="diagnosis",
   q="A 41-year-old man has vertical double vision that is worse looking down, and he tilts his head away from the affected side. Which cranial nerve is involved?",
   opts=[
     ["Fourth", "Correct. The trochlear nerve supplies superior oblique, which intorts and depresses the eye."],
     ["Third", "That would give ptosis, mydriasis and a down-and-out eye."],
     ["Sixth", "That gives horizontal diplopia from lateral rectus weakness."],
     ["Second", "The optic nerve carries vision, not eye movement."],
     ["Seventh", "The facial nerve closes the lids rather than moving the globe."]],
   c=0, cite=c(43)),

 dict(topic="Fourth nerve palsy", io=IO, lead="diagnosis",
   q="What does the lecture say is anatomically unique about the trochlear nerve?",
   opts=[
     ["It arises dorsally and crosses", "Correct, so the left nucleus supplies the right eye."],
     ["It has the longest intracranial course", "Not the feature the lecture highlights."],
     ["It carries parasympathetic fibres", "Those travel with the third nerve."],
     ["It supplies two extraocular muscles", "It supplies superior oblique alone."],
     ["It exits through the optic canal", "Not a point the lecture makes."]],
   c=0, cite=c(42)),

 dict(topic="Sixth nerve palsy", io=IO, lead="diagnosis",
   q="A 7-year-old boy has new horizontal double vision and cannot abduct the left eye. Which cause is most likely in a child?",
   opts=[
     ["Intracranial tumour", "Correct. In children the lecture names tumours, especially brainstem and posterior fossa."],
     ["Microvascular disease", "That is the commonest cause in adults, not children."],
     ["Skull base fracture", "That requires major trauma, absent here."],
     ["Congenital palsy", "The lecture attaches congenital origin to isolated fourth nerve palsies."],
     ["Giant cell arteritis", "That affects patients over 50."]],
   c=0, cite=c(45)),

 dict(topic="Cranial nerve palsy", io=IO, lead="next step",
   q="A 59-year-old woman has an isolated, atraumatic sixth nerve palsy. Which investigation does the lecture direct?",
   opts=[
     ["MRI brain with and without contrast", "Correct, and check haemoglobin A1C if there are risk factors and no known diabetes."],
     ["Stat computed tomography angiography", "That is reserved for a pupil-involved third nerve palsy."],
     ["Lumbar puncture", "That is for suspected raised intracranial pressure."],
     ["Temporal artery biopsy", "That investigates giant cell arteritis."],
     ["Carotid Doppler", "That is used when an embolic source is suspected."]],
   c=0, cite=c(46)),

 dict(topic="Ptosis", io=IO, lead="diagnosis",
   q="A 45-year-old woman has drooping of both lids that is mild in the morning and marked by evening, with intermittent double vision. Which is the most likely diagnosis?",
   opts=[
     ["Myasthenia gravis", "Correct. Variability through the day and fatigability are the discriminators."],
     ["Horner syndrome", "That has normal levator function and is usually unilateral."],
     ["Third nerve palsy", "That gives reduced levator function with mydriasis and movement deficits."],
     ["Adie tonic pupil", "That involves the pupil and not the eyelid."],
     ["Physiologic anisocoria", "That concerns pupil size, not the lid."]],
   c=0, cite=c(49)),

 dict(topic="Ptosis", io=IO, lead="diagnosis",
   q="A 60-year-old man has unilateral ptosis with normal levator function and ipsilateral miosis. Which is the most likely diagnosis?",
   opts=[
     ["Horner syndrome", "Correct. Normal levator function with miosis distinguishes it from a third nerve palsy."],
     ["Third nerve palsy", "That reduces levator function and gives mydriasis."],
     ["Myasthenia gravis", "That reduces levator function and varies through the day."],
     ["Adie tonic pupil", "That gives mydriasis without ptosis."],
     ["Argyll Robertson pupil", "That is bilateral miosis without ptosis."]],
   c=0, cite=c(49)),

 dict(topic="Visual fields", io=IO, lead="diagnosis",
   q="A 55-year-old woman has lost the outer half of the visual field in each eye. Where is the lesion?",
   opts=[
     ["Optic chiasm", "Correct. Bitemporal hemianopsia is the chiasmal pattern."],
     ["Right optic nerve", "That would blind one eye."],
     ["Left optic tract", "That gives a right homonymous hemianopsia."],
     ["Occipital cortex", "That gives a homonymous defect, often with macular sparing."],
     ["Retina", "A retinal lesion gives a monocular defect."]],
   c=0, cite=c(52)),

 dict(topic="Visual fields", io=IO, lead="diagnosis",
   q="A 70-year-old man has a left homonymous hemianopsia with macular sparing after a stroke. Which location does that pattern suggest?",
   opts=[
     ["Occipital cortex", "Correct. Macular sparing is the cortical signature."],
     ["Optic chiasm", "That produces a bitemporal defect."],
     ["Right optic nerve", "That produces monocular blindness."],
     ["Ciliary ganglion", "That affects the pupil, not the visual field."],
     ["Pretectal nucleus", "That affects the light reflex, not the field."]],
   c=0, cite=c(52)),

 dict(topic="Nystagmus", io=IO, lead="diagnosis",
   q="A 30-year-old man has new involuntary rhythmic eye oscillations with a sensation that the room is moving. What is that symptom called?",
   opts=[
     ["Oscillopsia", "Correct. It is the sense of the environment moving, distinct from vertigo."],
     ["Vertigo", "That is the sensation of the patient or room spinning."],
     ["Diplopia", "That is double vision."],
     ["Photophobia", "That is light sensitivity."],
     ["Amaurosis", "That is transient visual loss."]],
   c=0, cite=c(3)),

 dict(topic="Nystagmus", io=IO, lead="next step",
   q="A 26-year-old woman develops new monocular nystagmus. Which is the most appropriate step?",
   opts=[
     ["Refer to ophthalmology", "Correct. Nystagmus acquired in adulthood, and monocular nystagmus, both warrant work-up."],
     ["Reassure her it is physiologic", "Monocular and asymmetric nystagmus is specifically flagged as concerning."],
     ["Start a calcium channel blocker", "That is used for vascular spasm in amaurosis fugax."],
     ["Patch the affected eye", "Patching addresses binocular diplopia, not nystagmus."],
     ["Prescribe prism glasses", "Not a management step the lecture gives."]],
   c=0, cite=c(5)),

 dict(topic="Nystagmus", io=IO, lead="diagnosis",
   q="A patient has horizontal jerk nystagmus. How is jerk nystagmus named, per the lecture?",
   opts=[
     ["For the direction of the fast beat", "Correct, and it increases on gaze in that direction."],
     ["For the direction of the slow phase", "The naming follows the fast phase."],
     ["For the eye that is affected", "Laterality is not what names it."],
     ["For the underlying cause", "Aetiology does not determine the name."],
     ["For the amplitude of the movement", "Amplitude is not the naming convention."]],
   c=0, cite=c(4)),

 dict(topic="Opioid toxicity", io=IO, lead="next step",
   q="A 24-year-old man is found drowsy with pinpoint pupils and a respiratory rate of 8. Which is the most appropriate immediate treatment?",
   opts=[
     ["Naloxone", "Correct, and repeat dosing may be needed because it lasts about two hours."],
     ["Apraclonidine drops", "That is a diagnostic test for Horner syndrome."],
     ["Pilocarpine drops", "That is used to test for an Adie pupil."],
     ["Acetazolamide", "That lowers intraocular pressure in glaucoma."],
     ["Atropine", "An anticholinergic would not reverse opioid toxicity."]],
   c=0, cite=c(12)),

 dict(topic="Opioid toxicity", io=IO, lead="education",
   q="A patient is discharged after naloxone reversal. Which point does the lecture emphasise?",
   opts=[
     ["Naloxone may need repeating", "Correct. It lasts about two hours, so respiratory depression can return."],
     ["The pupils will stay dilated", "Opioid toxicity constricts the pupils."],
     ["Vision loss is permanent", "No visual loss is described."],
     ["Naloxone is intravenous only", "An intranasal form is available over the counter."],
     ["Miosis is the dangerous feature", "The concern is depressed consciousness and respiration."]],
   c=0, cite=c(12)),

 dict(topic="Anisocoria", io=IO, lead="diagnosis",
   q="A 38-year-old man has pupils that differ by 0.3 mm, equally in light and dark, with no dilation lag. Which is the most likely diagnosis?",
   opts=[
     ["Physiologic anisocoria", "Correct. Usually under 0.4 mm and of equal magnitude in light and dark."],
     ["Horner syndrome", "That shows dilation lag and greater anisocoria in the dark."],
     ["Adie tonic pupil", "That gives a clearly large, poorly reactive pupil."],
     ["Third nerve palsy", "That involves the lid and eye movements."],
     ["Pharmacologic mydriasis", "That pupil is very large and unreactive."]],
   c=0, cite=c(21)),

 dict(topic="Pupillary pathway", io=IO, lead="diagnosis",
   q="Why are both pupils normally the same size even when one eye is covered?",
   opts=[
     ["The efferent limb is bilateral", "Correct. Each pretectal nucleus sends impulses to both Edinger-Westphal nuclei."],
     ["Both retinas share one optic nerve", "The nerves are separate; the crossing happens centrally."],
     ["The iris muscles are mechanically linked", "There is no mechanical link between the two irides."],
     ["Sympathetic tone is identical bilaterally", "The bilaterality described is of the parasympathetic efferent limb."],
     ["The pupils are not normally equal", "They should be equal unless an efferent pathway fails."]],
   c=0, cite=c(21)),
]
