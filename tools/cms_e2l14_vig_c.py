# -*- coding: utf-8 -*-
"""CMS I Exam 2, Lecture 14 (Ocular Trauma) -- vignette set C.

The rest of the vignette bank, so the pair of 30s has room: mixed presentations
across the whole lecture, weighted toward the discriminations that decide
disposition. Same house style: FIVE options, varied lead-in, per-option
refutation, self-contained.

Correct answer authored FIRST; cms_e2_partition.py rotates it.
"""
D = "CMS I Ocular Trauma - Shah Fallsv.pptx, Slide %d"
IO_A = "a — Ocular trauma: etiology, manifestations, testing, management, referral, prognosis"
IO_B = "b — Identify medical care strategies for common ophthalmological disorders by age"

QUESTIONS = [
 dict(topic="Open globe injury", io=IO_A, lead="diagnosis", cite=D % 14,
  q="A 47-year-old struck by a metal shard has an eye in which the pupil is drawn to one side toward a corneal wound and the anterior chamber looks flat. Which is the most likely diagnosis?",
  opts=[["Open globe injury", "Correct. A pupil pulled toward the wound with a flat chamber is the picture."],
        ["Traumatic mydriasis", "That leaves the pupil round and the chamber formed."],
        ["Corneal abrasion", "An abrasion does not distort the pupil."],
        ["Anterior uveitis", "Inflammation may constrict the pupil but does not flatten the chamber."],
        ["Acute angle closure", "That gives a mid-dilated fixed pupil and a hazy cornea."]]),

 dict(topic="Globe rupture", io=IO_A, lead="risk factor", cite=D % 17,
  q="A 72-year-old with previous cataract surgery in both eyes is struck in the face by a car airbag. Why does the surgical history matter here?",
  opts=[["Old incisions leave a permanent weak point where the globe may rupture", "Correct. Prior intraocular surgery lowers the force needed."],
        ["It makes a hyphema more likely than a rupture", "Not the reason the history matters."],
        ["It protects the eye from blunt force", "It does the opposite."],
        ["It rules out an open globe", "It raises the concern rather than excluding it."],
        ["It means the pressure will read falsely high", "Not the relevance here."]]),

 dict(topic="Full-thickness eye wall laceration", io=IO_A, lead="management", cite=D % 16,
  q="A 36-year-old has a corneal laceration with a cut lens capsule and an opaque, swollen lens. When is lensectomy usually performed?",
  opts=[["Later, so hyphema and inflammation can settle and the lens can be measured", "Correct. It is required but often deferred from the globe repair."],
        ["At the same time as the globe repair, always", "It is often deferred rather than done at once."],
        ["Only if vision fails to improve after a year", "That is far later than described."],
        ["Never, since the lens will clear on its own", "A hydrated opaque lens does not clear."],
        ["Immediately, before the globe is closed", "The globe is closed first."]]),

 dict(topic="Corneal abrasion", io=IO_A, lead="treatment", cite=D % 18,
  q="A 31-year-old has a corneal abrasion from a fingernail. Which treatment is appropriate?",
  opts=[["A topical broad-spectrum antibacterial, with review to confirm healing", "Correct, and patching may ease the pain."],
        ["A topical antiviral", "There is no viral indication."],
        ["A topical corticosteroid", "Steroids are not the treatment for an abrasion."],
        ["Oral antibiotics alone", "Topical treatment is what is described."],
        ["No treatment and no follow-up", "Antibiotic cover and re-examination are both part of care."]]),

 dict(topic="Corneal foreign body", io=IO_A, lead="management", cite=D % 22,
  q="A conjunctival foreign body is visible on diffuse light examination in a 28-year-old. Which is the most appropriate removal method?",
  opts=[["A cotton-tipped applicator after topical anaesthetic", "Correct. A conjunctival object lifts off with a swab."],
        ["A sterile 27-gauge needle", "That is for a corneal foreign body."],
        ["A battery-operated burr", "That is for a rust ring."],
        ["Copious irrigation alone", "It may not dislodge an embedded object."],
        ["Referral for operative removal", "That is disproportionate for a conjunctival object."]]),

 dict(topic="Hyphema", io=IO_A, lead="management", cite=D % 25,
  q="A 26-year-old with hyphema has an intraocular pressure of 34 mmHg (normal 10 to 21) and no suspicion of an open globe. Which agents are used?",
  opts=[["Beta blockers, pilocarpine and acetazolamide, with osmotic agents if needed", "Correct. That is how a raised pressure is brought down here."],
        ["Topical corticosteroids alone", "Steroids are part of care but do not lower pressure."],
        ["Aspirin to improve perfusion", "Aspirin raises the rebleed risk and is avoided."],
        ["Aminocaproic acid alone", "It reduces rebleeding but not pressure."],
        ["A mydriatic to open the angle", "Dilation is not used in ocular trauma."]]),

 dict(topic="Hyphema", io=IO_A, lead="mechanism", cite=D % 25,
  q="A cycloplegic drop is prescribed for a patient with a hyphema. What is it doing?",
  opts=[["Temporarily paralysing the ciliary body to rest the eye", "Correct. Atropine, homatropine and scopolamine are used this way."],
        ["Lowering the intraocular pressure directly", "That is the role of other agents."],
        ["Preventing infection of the anterior chamber", "It has no antimicrobial action."],
        ["Dissolving the clot", "Nothing in the regimen dissolves it; aminocaproic acid slows breakdown."],
        ["Constricting the pupil to trap the blood", "It does the opposite to the pupil."]]),

 dict(topic="Lid laceration", io=IO_A, lead="referral", cite=D % 26,
  q="Which of these lid lacerations can reasonably be repaired in the emergency department?",
  opts=[["A superficial cut across the upper lid skin, sparing the margin and tarsal plate",
         "Correct. Partial-thickness lacerations meeting none of the criteria are repaired there."],
        ["A cut through the lid margin", "Margin involvement is a referral criterion."],
        ["A cut 4 millimetres from the medial canthus", "Within 6 to 8 millimetres of the canthus is a referral criterion."],
        ["A cut associated with new ptosis", "Ptosis is a referral criterion."],
        ["A cut through the tarsal plate", "Tarsal plate involvement is a referral criterion."]]),

 dict(topic="Orbital contusion", io=IO_A, lead="mechanism", cite=D % 31,
  q="Why does the bruising in an orbital contusion stay in front of the eye rather than spreading behind it?",
  opts=[["The tarsal plate and septal margin act as a wall", "Correct. That is what keeps it preseptal."],
        ["The orbital fat absorbs the blood", "Not the described mechanism."],
        ["The periosteum is impermeable", "Not the described mechanism."],
        ["Venous drainage carries it forward", "Not the described mechanism."],
        ["The globe blocks posterior spread", "Not the described mechanism."]]),

 dict(topic="Retinal detachment", io=IO_A, lead="patient education", cite=D % 36,
  q="A 55-year-old with a fresh retinal detachment asks how urgently she needs to be seen. Which is the most accurate response?",
  opts=[["By an ophthalmologist within 24 hours", "Correct. The referral is immediate."],
        ["At the next available clinic within a month", "Far too slow."],
        ["Only if the curtain spreads further", "Referral does not wait on progression."],
        ["Within a week, once the floaters settle", "Too slow."],
        ["Immediately, but only if the other eye is affected too", "One eye is enough."]]),

 dict(topic="Retinal detachment", io=IO_A, lead="diagnosis", cite=D % 36,
  q="Which symptom indicates the macula has become involved in a retinal detachment?",
  opts=[["Central visual acuity has dropped", "Correct. Field defects come first; central acuity falls with macular involvement."],
        ["Floaters have increased", "Floaters relate to the vitreous, not the macula."],
        ["Flashes have become more frequent", "Flashes reflect traction rather than macular involvement."],
        ["The eye has become painful", "Detachment is characteristically painless."],
        ["The pupil has become irregular", "Not a feature of detachment."]]),

 dict(topic="Orbital floor fracture", io=IO_A, lead="diagnosis", cite=D % 41,
  q="A 29-year-old has double vision on looking to the side after blunt orbital trauma. Which muscle is entrapped?",
  opts=[["Medial rectus", "Correct. Lateral gaze diplopia points to the medial rectus and a medial wall fracture."],
        ["Inferior rectus", "That gives diplopia on upward gaze."],
        ["Superior rectus", "Not the muscle entrapped in these fractures."],
        ["Inferior oblique", "Not the muscle described."],
        ["Superior oblique", "Not the muscle described."]]),

 dict(topic="Orbital floor fracture", io=IO_A, lead="initial test", cite=D % 43,
  q="A 40-year-old is suspected of an orbital fracture after a blow. Which imaging is ordered?",
  opts=[["Computed tomography of the orbits and midface", "Correct. That is the study for this fracture."],
        ["Magnetic resonance imaging of the orbits", "Not the study, and unsafe if metal may be present."],
        ["Plain facial radiographs alone", "They do not adequately define the fracture."],
        ["Ocular ultrasound", "It does not assess bone."],
        ["No imaging unless diplopia is present", "Imaging is not withheld on that basis."]]),

 dict(topic="Orbital floor fracture", io=IO_A, lead="prognosis", cite=D % 43,
  q="A patient's optic nerve was damaged at the moment of an orbital injury. What should be expected from surgery?",
  opts=[["The damage is unlikely to improve, and surgery may worsen it", "Correct. That is why the decision is made carefully."],
        ["Surgery reliably restores the lost vision", "It does not."],
        ["Surgery restores vision if done within 24 hours", "Timing does not change this."],
        ["Vision recovers spontaneously in most cases", "Not what is described."],
        ["The nerve regenerates over several months", "It does not."]]),

 dict(topic="Basilar skull fracture", io=IO_A, lead="diagnosis", cite=D % 44,
  q="Which combination of findings should raise a basilar skull fracture after head trauma?",
  opts=[["Raccoon eyes, Battle sign and haemotympanum", "Correct. Those are the indirect signs."],
        ["Proptosis, chemosis and reduced acuity", "That points to an orbital process."],
        ["Ptosis, a dilated pupil and diplopia", "That points to a third nerve palsy."],
        ["A red eye with discharge and lid crusting", "That is an infective surface picture."],
        ["Diplopia on upward gaze with cheek numbness", "That points to an orbital floor fracture."]]),

 dict(topic="Basilar skull fracture", io=IO_A, lead="diagnosis", cite=D % 44,
  q="Which bones may be involved in a basilar skull fracture?",
  opts=[["Cribriform plate of the ethmoid, orbital plate of the frontal, temporal, sphenoid or occipital",
         "Correct. Those make up the skull base."],
        ["The maxilla and the zygomatic arch alone", "Those are facial bones, not the skull base."],
        ["The nasal bones and the vomer", "Those are not the skull base."],
        ["The mandible and the temporomandibular joint", "Not part of the skull base."],
        ["The parietal bones only", "The parietal bone is not the base."]]),

 dict(topic="Trauma first principles", io=IO_A, lead="next step", cite=D % 9,
  q="A conscious and cooperative 33-year-old has a periorbital laceration after an assault. Which examination elements are appropriate?",
  opts=[["Inspection, pupil size, shape and reactivity, visual acuity and confrontation fields",
         "Correct, done without causing further damage."],
        ["Dilated fundoscopy first", "The eye is not dilated when trauma is suspected."],
        ["Tonometry before anything else", "Not the first element, and unsafe if the globe may be open."],
        ["Gonioscopy of the drainage angle", "Not part of the trauma assessment."],
        ["Corneal sensation testing alone", "Too narrow an examination."]]),

 dict(topic="Assessment", io=IO_A, lead="history", cite=D % 8,
  q="Which detail about the mechanism most changes the level of concern in ocular trauma?",
  opts=[["Whether the object was blunt or sharp, and at high or low velocity", "Correct. That is what predicts the injury pattern."],
        ["Whether the patient was wearing spectacles", "Useful but not the key mechanism detail."],
        ["The time of day the injury happened", "Not what changes concern."],
        ["Whether the patient drove themselves in", "Not what changes concern."],
        ["The patient's occupation alone", "Occupation hints at exposure but the mechanism is what matters."]]),
]
