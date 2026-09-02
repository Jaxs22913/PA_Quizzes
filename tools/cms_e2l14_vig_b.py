# -*- coding: utf-8 -*-
"""CMS I Exam 2, Lecture 14 (Ocular Trauma) -- vignette set B.

Lid lacerations, contusion and periorbital haematoma, retinal and vitreous
detachment, orbital floor fracture, and basilar skull fracture. Same house
style: FIVE options, varied lead-in, per-option refutation, self-contained.

Correct answer authored FIRST; cms_e2_partition.py rotates it.
"""
D = "CMS I Ocular Trauma - Shah Fallsv.pptx, Slide %d"
IO_A = "a — Ocular trauma: etiology, manifestations, testing, management, referral, prognosis"
IO_B = "b — Identify medical care strategies for common ophthalmological disorders by age"

QUESTIONS = [
 dict(topic="Lid laceration", io=IO_A, lead="referral", cite=D % 26,
  q="A 33-year-old has a 1 centimetre laceration running through the lower lid margin after a dog bite. Which is the most appropriate disposition?",
  opts=[["Ophthalmology, because the lid margin is involved", "Correct. Margin involvement is one of the explicit referral criteria."],
        ["Close it in the emergency department with fine sutures", "Margin involvement takes it out of emergency department repair."],
        ["Leave it open and review in one week", "A margin laceration needs proper repair."],
        ["Refer to plastic surgery as an outpatient", "Ophthalmology is the named specialty."],
        ["Tissue adhesive with no follow-up", "Not appropriate for a margin laceration."]]),

 dict(topic="Lid laceration", io=IO_A, lead="prognosis", cite=D % 27,
  q="A 48-year-old has a deep laceration in the medial third of the lower lid. What is the consequence if it is not repaired properly?",
  opts=[["Chronic tearing from a transected canalicular system", "Correct. The canalicular injury is what makes the medial third special."],
        ["Permanent ptosis", "That follows levator involvement, which is a different site."],
        ["Loss of central vision", "The lid does not carry vision."],
        ["Corneal ulceration within days", "Not the described consequence."],
        ["Chronic photophobia", "Not the described consequence."]]),

 dict(topic="Lid laceration", io=IO_A, lead="next step", cite=D % 26,
  q="A 21-year-old has a full-thickness upper lid laceration. Beyond repairing the lid, which is the most important step?",
  opts=[["Examine the globe underneath for laceration or rupture", "Correct. About two thirds of full-thickness lid lacerations come with one."],
        ["Start oral corticosteroids", "Not indicated."],
        ["Arrange a visual field test", "Not the priority."],
        ["Patch the eye for 48 hours", "That does not address the globe."],
        ["Prescribe a cycloplegic", "Not the priority here."]]),

 dict(topic="Periorbital haematoma", io=IO_A, lead="management", cite=D % 33,
  q="A 60-year-old on warfarin develops a tense, proptotic orbit with rising pressure and no history of injury. Which is the most appropriate management?",
  opts=[["Canthotomy with cantholysis", "Correct. Releasing the lateral canthal tendon and cutting its inferior branch lets the blood drain."],
        ["Pressure patching the eye", "Pressure is the wrong direction entirely."],
        ["Observation until it resorbs", "A tense orbit does not wait."],
        ["Topical beta blocker alone", "It will not decompress the orbit."],
        ["Immediate enucleation", "Far beyond what is required."]]),

 dict(topic="Orbital contusion", io=IO_A, lead="next step", cite=D % 31,
  q="A 35-year-old has periorbital swelling and ecchymosis after a fall, with a normal globe and no haemorrhage within the orbit. Beyond supportive care, which is the most appropriate step?",
  opts=[["Exclude brain trauma", "Correct. The force that bruised the orbit reaches the brain."],
        ["Start topical antibiotics", "There is no surface infection."],
        ["Arrange urgent canthotomy", "There is no orbital haemorrhage to decompress."],
        ["Refer for cataract assessment", "Not relevant acutely."],
        ["Begin a corticosteroid taper", "Not the described management."]]),

 dict(topic="Retinal detachment", io=IO_A, lead="diagnosis", cite=D % 36,
  q="A 58-year-old myope describes a shower of floaters, flashes of light, and a curtain moving across the vision of one eye. Which is the most likely diagnosis?",
  opts=[["Rhegmatogenous retinal detachment", "Correct. Flashes, floaters and a curtain, with myopia as the risk factor."],
        ["Exudative retinal detachment", "That has no break and usually accompanies systemic disease or a tumour."],
        ["Traction retinal detachment", "That follows proliferative diabetic retinopathy."],
        ["Vitreous haemorrhage alone", "That blurs vision without a defined curtain."],
        ["Central retinal vein occlusion", "That gives sudden painless loss without flashes."]]),

 dict(topic="Retinal detachment", io=IO_A, lead="management", cite=D % 39,
  q="A 64-year-old with long-standing proliferative diabetic retinopathy has a localised, concave retinal detachment. Which is the most appropriate management?",
  opts=[["Surgical repair", "Correct. A traction detachment is managed surgically."],
        ["Treat the underlying systemic disease alone", "That is the approach for an exudative detachment."],
        ["Observation with serial imaging", "Not the described management."],
        ["Intravitreal antibiotics", "There is no infection."],
        ["Laser to the macula alone", "Not the described management."]]),

 dict(topic="Retinal detachment", io=IO_A, lead="management", cite=D % 39,
  q="A 52-year-old has subretinal fluid with no retinal break and no traction, alongside a known intraocular tumour. Which is the most appropriate management?",
  opts=[["Treat the underlying condition", "Correct. An exudative detachment is not primarily surgical."],
        ["Scleral buckling", "Surgery is not the primary answer here."],
        ["Pneumatic retinopexy", "Not indicated without a break."],
        ["Laser retinopexy around a break", "There is no break to seal."],
        ["Observation with no treatment", "The underlying disease is treated."]]),

 dict(topic="Orbital floor fracture", io=IO_A, lead="diagnosis", cite=D % 41,
  q="A 26-year-old was punched in the eye. He has periorbital swelling, numbness of the cheek, and double vision when looking upward. Which is the most likely diagnosis?",
  opts=[["Orbital floor blowout fracture with inferior rectus entrapment", "Correct. Infraorbital numbness with upward gaze diplopia is the combination."],
        ["Medial wall fracture with medial rectus entrapment", "That gives diplopia on lateral gaze."],
        ["Third nerve palsy", "That gives ptosis and a dilated pupil."],
        ["Traumatic optic neuropathy", "That reduces vision rather than restricting upgaze."],
        ["Orbital cellulitis", "That is infective, with fever and proptosis."]]),

 dict(topic="Orbital floor fracture", io=IO_B, lead="diagnosis", cite=D % 41,
  q="An 8-year-old struck by a ball has severe pain, vomiting and a heart rate of 48 whenever he tries to look up. His eye and lids look normal. Which is the most likely explanation?",
  opts=[["A white-eyed blowout with muscle entrapment", "Correct. In children entrapment can occur with no orbital soft tissue signs at all."],
        ["Simple concussion", "Concussion does not produce gaze-provoked bradycardia."],
        ["Vasovagal syncope from pain", "The symptoms are provoked specifically by eye movement."],
        ["Traumatic iritis", "That does not cause bradycardia on eye movement."],
        ["Migraine triggered by the injury", "That does not restrict upgaze with autonomic signs."]]),

 dict(topic="Orbital floor fracture", io=IO_A, lead="next step", cite=D % 43,
  q="Computed tomography confirms an orbital floor fracture with inferior rectus entrapment in a 30-year-old. Which is the most appropriate next step?",
  opts=[["Contact a facial trauma surgeon urgently", "Correct. An entrapped muscle can necrose if its blood supply is compromised."],
        ["Ice, analgesia and review in 2 to 3 days", "That is the pathway when there is no entrapment."],
        ["Admit for neurosurgical observation", "That is the basilar skull fracture pathway."],
        ["Start antibiotics and discharge", "Antibiotics are for blood in the maxillary sinus."],
        ["List for elective repair in six weeks", "Entrapment does not wait."]]),

 dict(topic="Orbital floor fracture", io=IO_A, lead="management", cite=D % 43,
  q="A 44-year-old has an orbital floor fracture with no entrapment and no globe injury, and blood is seen in the maxillary sinus. Which is the most appropriate management?",
  opts=[["Ice, analgesia and antibiotics, with review in 2 to 3 days", "Correct. Blood in the sinus is what adds the antibiotic."],
        ["Immediate operative repair", "Not required without entrapment or globe injury."],
        ["Ice and analgesia alone", "Blood in the sinus adds an antibiotic."],
        ["Neurosurgical admission", "Not indicated for this fracture."],
        ["Systemic corticosteroids", "Not the described management."]]),

 dict(topic="Basilar skull fracture", io=IO_A, lead="diagnosis", cite=D % 44,
  q="A 39-year-old fell from a ladder. She has bruising around both eyes, bruising behind one ear, and blood behind the eardrum. Which is the most likely diagnosis?",
  opts=[["Basilar skull fracture", "Correct. Raccoon eyes, Battle sign and haemotympanum together."],
        ["Bilateral orbital floor fractures", "Those do not produce Battle sign or haemotympanum."],
        ["Nasal fracture with periorbital spread", "That does not explain the retroauricular bruising."],
        ["Periorbital cellulitis", "That is infective and unilateral."],
        ["Bilateral periorbital haematomas from the fall", "That does not explain the ear findings."]]),

 dict(topic="Basilar skull fracture", io=IO_A, lead="next step", cite=D % 47,
  q="A patient with a suspected basilar skull fracture has clear fluid dripping from the nose that forms a double ring on the pillowcase. Which is the most appropriate next step?",
  opts=[["Neurosurgery consult and admission", "Correct. A cerebrospinal fluid leak forces both."],
        ["Discharge with outpatient follow-up", "A leak is not managed as an outpatient."],
        ["Nasal packing to stop the drainage", "Packing a cerebrospinal fluid leak is not the answer."],
        ["Ophthalmology consult", "The relevant specialty is neurosurgery."],
        ["Prophylactic antibiotics alone, then discharge", "Antibiotics here are themselves debated, and do not replace admission."]]),
]
