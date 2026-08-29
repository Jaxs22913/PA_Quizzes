# CMS I Exam 2, Lecture 11 Neuro-Ophthalmology — VIGNETTE pool, part C.
# Deliberately NON-diagnosis lead-ins and a patient in every stem: parts A and B
# came out 78% diagnosis and 71% patient stems, and the style calls for the
# lead-in to vary (next step / treatment / test / education), with the lead-in
# deciding the answer.
SRC = "11. Neuro-Ophthalmology STUDENT VERSION 2026.pptx"
def c(n): return f"{SRC}, Slide {n}"
IO = ("a — Describe the pupillary pathways, cranial nerve palsies and chiasmal lesions, "
      "and identify medical care strategies for neuro-ophthalmological disorders")

POOL_C = [
 dict(topic="Third nerve palsy", io=IO, lead="education",
   q="A 64-year-old man with a pupil-involved third nerve palsy asks why he is being sent for a scan tonight rather than in the morning. What is the most appropriate explanation?",
   opts=[
     ["An aneurysm could rupture within days", "Correct. The threat of rupture within hours to days is what drives the urgency."],
     ["The palsy will become permanent by morning", "Timing of imaging is about the aneurysm, not fixed nerve damage."],
     ["Diabetes must be excluded tonight", "Microvascular disease is the pupil-sparing pattern and is not the emergency."],
     ["Scanning is only available at night", "Availability is not the reason."],
     ["The pupil will not dilate tomorrow", "Pupil size is not the reason for urgency."]],
   c=0, cite=c(40)),

 dict(topic="Horner syndrome", io=IO, lead="next step",
   q="A 44-year-old woman has acute Horner syndrome with neck pain after a chiropractic manipulation. What is the most appropriate next step?",
   opts=[
     ["Urgent vascular imaging", "Correct. Carotid dissection must be identified before it embolises."],
     ["Apraclonidine drops in clinic", "Confirming the syndrome delays the search for its cause here."],
     ["Reassurance and review in a month", "An acute third-order Horner syndrome with neck pain is not for watchful waiting."],
     ["Start aspirin and discharge", "Treatment should follow imaging that establishes the diagnosis."],
     ["Refer routinely to ophthalmology", "The urgent question is vascular, not ocular."]],
   c=0, cite=c(15)),

 dict(topic="Optic neuritis", io=IO, lead="test",
   q="A 28-year-old woman has painful vision loss in one eye and a relative afferent pupillary defect. Which test is most appropriate?",
   opts=[
     ["MRI brain and orbits", "Correct, with and without contrast, looking for demyelinating lesions."],
     ["Carotid Doppler", "That is for suspected embolic transient visual loss."],
     ["Tonometry", "That measures intraocular pressure."],
     ["Temporal artery biopsy", "That investigates giant cell arteritis in older patients."],
     ["Lumbar puncture first", "Imaging comes first in this pathway."]],
   c=0, cite=c(26)),

 dict(topic="Myasthenia gravis", io=IO, lead="next step",
   q="A 52-year-old woman has fatigable bilateral ptosis and variable diplopia. What is the most appropriate next step?",
   opts=[
     ["Refer for neurologic evaluation", "Correct. The pattern points away from a structural palsy and toward myasthenia."],
     ["Stat computed tomography angiography", "That is for a pupil-involved third nerve palsy."],
     ["Apraclonidine drops", "That tests for Horner syndrome, which has normal levator function."],
     ["Patch one eye and review in six months", "That interval applies to traumatic cranial nerve palsies."],
     ["Dilute pilocarpine drops", "That tests for an Adie tonic pupil."]],
   c=0, cite=c(49)),

 dict(topic="Adie tonic pupil", io=IO, lead="education",
   q="A 32-year-old woman is told she has an Adie tonic pupil. What is the most appropriate thing to tell her?",
   opts=[
     ["It is often benign and asymptomatic", "Correct, though photophobia and blurred near vision can occur."],
     ["It signals an intracranial aneurysm", "That concern belongs to a pupil-involved third nerve palsy."],
     ["It indicates tertiary syphilis", "That is the Argyll Robertson association."],
     ["It will progress to blindness", "No such progression is described."],
     ["It requires urgent vascular imaging", "That is the pathway for acute Horner syndrome."]],
   c=0, cite=c(36)),

 dict(topic="Nystagmus", io=IO, lead="next step",
   q="A 19-year-old woman develops new nystagmus with vertigo. After referral to ophthalmology, what does the lecture place next in the sequence?",
   opts=[
     ["Initial imaging", "Correct: referral, then imaging, then labs if relevant, to find the underlying cause."],
     ["Laboratory testing", "Labs come after imaging, and only if relevant."],
     ["Immediate patching", "Patching addresses diplopia rather than nystagmus."],
     ["Corrective surgery", "Not part of the described sequence."],
     ["Observation for six months", "That interval belongs to traumatic cranial nerve palsies."]],
   c=0, cite=c(5)),

 dict(topic="Acute angle closure", io=IO, lead="education",
   q="A 70-year-old woman with a history of anterior uveitis is prescribed a nebulised bronchodilator. Which risk should she be warned about?",
   opts=[
     ["Acute angle-closure glaucoma", "Correct. Nebulised bronchodilators and systemic anticholinergics are listed risk factors."],
     ["Retinal detachment", "Its risks are myopia, trauma, cataract surgery and age."],
     ["Optic neuritis", "That is inflammatory and linked to demyelination."],
     ["Central retinal artery occlusion", "That is embolic and not linked to nebulisers."],
     ["Papilledema", "That follows raised intracranial pressure."]],
   c=0, cite=c(22)),

 dict(topic="Pharmacologic mydriasis", io=IO, lead="education",
   q="A nurse develops a unilateral fixed dilated pupil after handling a scopolamine patch. What should she be told?",
   opts=[
     ["It will resolve as the drug wears off", "Correct. Pharmacologic mydriasis is transient and needs no imaging."],
     ["She needs urgent angiography", "That is for a pupil-involved third nerve palsy, which also affects the lid."],
     ["This indicates an Adie pupil", "That constricts slowly to a near target."],
     ["This is early Horner syndrome", "Horner syndrome gives a small pupil."],
     ["She should start pilocarpine drops", "No treatment is required."]],
   c=0, cite=c(22)),

 dict(topic="Care strategies", io=IO, lead="next step",
   q="A 68-year-old man has a new visual field defect and a suspected chiasmal lesion. Which referral does the lecture list alongside ophthalmology?",
   opts=[
     ["Neurology or neurosurgery", "Correct, with vascular surgery also named as appropriate."],
     ["Cardiology", "A cardiac source is pursued for embolic transient visual loss, not a chiasmal lesion."],
     ["Endocrinology", "A pituitary lesion may need endocrine input later, but the referral named here is neurological."],
     ["Rheumatology", "That would follow suspected giant cell arteritis, which presents with visual loss rather than a chiasmal field defect."],
     ["Dermatology", "No dermatologic referral is part of the neuro-ophthalmology pathway."]],
   c=0, cite=c(54)),

 dict(topic="Fourth nerve palsy", io=IO, lead="education",
   q="A 38-year-old woman with a fourth nerve palsy asks why she keeps tilting her head. What is the best explanation?",
   opts=[
     ["Tilting compensates for the weak muscle", "Correct. She tilts away from the affected side to reduce the vertical deviation."],
     ["Tilting reduces intraocular pressure", "Head position does not treat pressure here."],
     ["It is an unrelated habit", "The tilt is a recognised compensation."],
     ["It prevents the pupil dilating", "The pupil is not involved."],
     ["It improves peripheral vision", "The problem is vertical alignment, not field."]],
   c=0, cite=c(43)),

 dict(topic="Third nerve palsy", io=IO, lead="treatment",
   q="A 29-year-old man has a traumatic third nerve palsy. What does the lecture advise about corrective treatment?",
   opts=[
     ["Observe about six months first", "Correct, with patching in the interim for binocular diplopia."],
     ["Operate within two weeks", "Early surgery is not what the lecture advises."],
     ["Start high-dose corticosteroids", "Those are for giant cell arteritis."],
     ["Begin pilocarpine drops", "That is a diagnostic test for an Adie pupil."],
     ["Refer for laser iridotomy", "That treats acute angle-closure glaucoma."]],
   c=0, cite=c(41)),

 dict(topic="Sixth nerve palsy", io=IO, lead="test",
   q="A 57-year-old man has an isolated atraumatic sixth nerve palsy and no known diabetes. Besides imaging, which test does the lecture add?",
   opts=[
     ["Haemoglobin A1C", "Correct, if he has risk factors and no established diagnosis."],
     ["Erythrocyte sedimentation rate", "That is for suspected giant cell arteritis."],
     ["Carotid Doppler", "That is for embolic transient visual loss."],
     ["Tonometry", "That measures intraocular pressure."],
     ["Lumbar puncture", "That is for suspected raised intracranial pressure."]],
   c=0, cite=c(46)),

 dict(topic="Argyll Robertson pupil", io=IO, lead="education",
   q="A 55-year-old man with Argyll Robertson pupils asks what else to look for. Which associated finding does the lecture name?",
   opts=[
     ["Sensory ataxia", "Correct, from tabes dorsalis with posterior column involvement."],
     ["Jaw claudication", "That belongs to giant cell arteritis."],
     ["Curtain-like visual loss", "That describes amaurosis fugax or retinal detachment."],
     ["Coloured halos around lights", "That is acute angle-closure glaucoma."],
     ["Painful eye movement", "That is optic neuritis."]],
   c=0, cite=c(32)),

 dict(topic="Horner syndrome", io=IO, lead="test",
   q="A 50-year-old man has suspected Horner syndrome. Why does apraclonidine produce dilation in the affected eye only?",
   opts=[
     ["The denervated pupil is supersensitive", "Correct, so a drop ineffective in a normal pupil dilates the affected one."],
     ["It blocks the iris sphincter directly", "It acts on adrenergic receptors, not by blocking the sphincter."],
     ["It raises intraocular pressure", "Pressure is not the mechanism."],
     ["It paralyses accommodation", "That is a cycloplegic effect, not the basis of this test."],
     ["It stimulates the ciliary ganglion", "That ganglion is parasympathetic."]],
   c=0, cite=c(28)),
]
