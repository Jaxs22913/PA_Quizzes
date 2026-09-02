# -*- coding: utf-8 -*-
"""CMS I Exam 2, Lecture 14 (Ocular Trauma) -- vignette set D.

The last of the vignette bank. Weighted toward telling the trauma diagnoses
apart from one another and from the medical ophthalmology already covered in
Lectures 10 to 13, since that is what a vignette actually asks.

SELF-CONTAINED. FIVE options; correct answer authored FIRST.
"""
D = "CMS I Ocular Trauma - Shah Fallsv.pptx, Slide %d"
IO_A = "a — Ocular trauma: etiology, manifestations, testing, management, referral, prognosis"
IO_B = "b — Identify medical care strategies for common ophthalmological disorders by age"

QUESTIONS = [
 dict(topic="Open globe injury", io=IO_A, lead="next step", cite=D % 6,
  q="A 23-year-old has a laceration of the upper lid and a subconjunctival haemorrhage after being struck with a bottle. He is alert. Which is the most appropriate next step before any lid repair?",
  opts=[["Assess the globe beneath for a full-thickness injury", "Correct. Two thirds of full-thickness lid lacerations have a globe injury with them."],
        ["Close the lid and arrange follow-up", "Closing over an unrecognised open globe is the error to avoid."],
        ["Instil a mydriatic to see the retina", "The eye is not dilated in trauma."],
        ["Measure the intraocular pressure first", "Unsafe if the globe may be open."],
        ["Discharge with oral antibiotics", "The globe has not been assessed."]]),

 dict(topic="Hyphema", io=IO_A, lead="patient education", cite=D % 25,
  q="A 20-year-old with a hyphema is being discharged after admission. Which instruction matters most?",
  opts=[["Avoid aspirin and antiplatelet drugs, and avoid straining", "Correct. Both raise the risk of a secondary haemorrhage."],
        ["Use topical anaesthetic drops when the eye aches", "Never prescribed for home use."],
        ["Resume contact sport as soon as the blood clears", "That invites another injury."],
        ["Sleep flat to help the blood disperse", "The head is kept elevated."],
        ["Stop the cycloplegic once the pain settles", "The regimen is not stopped on symptoms alone."]]),

 dict(topic="Corneal abrasion", io=IO_A, lead="next step", cite=D % 18,
  q="A 42-year-old treated for a corneal abrasion three days ago returns with worsening pain and a white spot on the cornea. Which is the most likely explanation?",
  opts=[["A corneal ulcer has developed", "Correct. This is why abrasions are re-examined, and why anaesthetic drops are never sent home."],
        ["The abrasion is healing normally", "Worsening pain with an infiltrate is not normal healing."],
        ["A rust ring has formed spontaneously", "Rust rings follow metallic foreign bodies, not abrasions."],
        ["The fluorescein has stained the stroma permanently", "Fluorescein does not do that."],
        ["A hyphema has developed", "That is blood in the chamber, not a corneal white spot."]]),

 dict(topic="Orbital floor fracture", io=IO_A, lead="diagnosis", cite=D % 41,
  q="A 37-year-old has crepitus in the eyelid after blowing his nose following facial trauma. Which finding is this?",
  opts=[["Periorbital subcutaneous emphysema", "Correct. Air tracks from the sinus into the orbit through the fracture."],
        ["Orbital cellulitis", "That is infective, with fever and proptosis."],
        ["A periorbital haematoma", "Blood does not crepitate."],
        ["Chemosis", "That is conjunctival oedema."],
        ["Enophthalmos", "That is the eye sitting back, not air in the tissue."]]),

 dict(topic="Retinal detachment", io=IO_A, lead="diagnosis", cite=D % 39,
  q="A 61-year-old with hypertension and a known intraocular tumour has subretinal fluid but no retinal break on dilated examination. Which type of detachment is this?",
  opts=[["Exudative", "Correct. No break and no traction, with an associated tumour."],
        ["Rhegmatogenous", "That requires a full-thickness break."],
        ["Traction", "That requires fibrovascular traction, usually diabetic."],
        ["Combined rhegmatogenous and traction", "Neither element is present."],
        ["Posterior vitreous detachment", "That is a separate event, not a retinal detachment."]]),

 dict(topic="Basilar skull fracture", io=IO_A, lead="initial and confirmatory test", cite=D % 44,
  q="A 44-year-old has clear rhinorrhoea after a fall. Which two bedside findings would support cerebrospinal fluid rather than nasal secretions?",
  opts=[["A positive dextrose stick and a halo sign on filter paper", "Correct. Those are the two bedside tests described."],
        ["A negative dextrose stick and clear fluid", "A negative stick argues against it."],
        ["Purulent colour and a foul smell", "That suggests infection instead."],
        ["Fluorescein uptake and photophobia", "Those relate to the cornea."],
        ["A raised white cell count and fever", "Those point to infection."]]),

 dict(topic="Periorbital haematoma", io=IO_A, lead="diagnosis", cite=D % 33,
  q="A 68-year-old on apixaban develops painful proptosis of one eye over an hour with no injury. Which is the most likely diagnosis?",
  opts=[["Periorbital haematoma from anticoagulation", "Correct. It is not always traumatic, and anticoagulants are a listed cause."],
        ["Orbital cellulitis", "That is infective, usually with fever and a longer course."],
        ["Thyroid eye disease", "That develops over months and is usually bilateral."],
        ["Cavernous sinus thrombosis", "Not the described presentation."],
        ["Acute angle-closure glaucoma", "That does not cause proptosis."]]),

 dict(topic="Lid laceration", io=IO_A, lead="referral", cite=D % 27,
  q="A 50-year-old has a laceration involving the tarsal plate of the upper lid. Which is the most appropriate action?",
  opts=[["Consult ophthalmology", "Correct. Tarsal plate involvement is an explicit referral criterion."],
        ["Repair it with absorbable sutures in the department", "Tarsal plate involvement takes it out of department repair."],
        ["Leave it open for 24 hours then close it", "That practice is for facial lacerations, not the tarsal plate."],
        ["Apply tissue adhesive", "Not appropriate for tarsal plate involvement."],
        ["Refer routinely in 2 to 3 weeks", "Too slow for this criterion."]]),

 dict(topic="Corneal foreign body", io=IO_A, lead="diagnosis", cite=D % 21,
  q="A 34-year-old machinist has photophobia, tearing and a foreign body sensation after a day at the lathe. Diffuse light shows nothing. Which is the most appropriate next step?",
  opts=[["Slit lamp examination, which can show a smaller foreign body", "Correct. Larger objects show on diffuse light; smaller ones need the slit lamp."],
        ["Reassure and review in one week", "The symptoms are unexplained."],
        ["Order computed tomography of the orbit", "Not the first step for a surface complaint."],
        ["Patch the eye and discharge", "The cause has not been found."],
        ["Prescribe topical anaesthetic for comfort", "Never prescribed for home use."]]),

 dict(topic="Globe rupture", io=IO_A, lead="management", cite=D % 17,
  q="A 55-year-old has a confirmed globe rupture. Which is the definitive management?",
  opts=[["Immediate surgical repair with wound exploration", "Correct. Everything else is holding measures until then."],
        ["Pressure patching and review in 24 hours", "Pressure is exactly what to avoid."],
        ["Topical antibiotics and observation", "That does not close an open globe."],
        ["Intravitreal antibiotics alone", "That does not repair the wound."],
        ["Enucleation in every case", "Repair is attempted first."]]),

 dict(topic="Trauma first principles", io=IO_A, lead="next step", cite=D % 6,
  q="A 45-year-old on warfarin fell and struck his face, and is now confused. His right eye is bruised. Which is the most appropriate imaging decision?",
  opts=[["Computed tomography without contrast, given confusion and anticoagulation", "Correct. Both are on the list that makes imaging automatic."],
        ["No imaging unless vision is reduced", "Confusion and anticoagulation are themselves the indication."],
        ["Magnetic resonance imaging of the head", "Computed tomography is the study described."],
        ["Plain skull radiographs", "They do not answer the question."],
        ["Ocular ultrasound only", "It does not assess the brain."]]),

 dict(topic="Orbital floor fracture", io=IO_A, lead="management", cite=D % 43,
  q="A 32-year-old has an orbital floor fracture with no entrapment, no globe injury and a clear maxillary sinus. Which is the most appropriate management?",
  opts=[["Ice and analgesia, with follow-up in 2 to 3 days", "Correct. That is the pathway when nothing else is involved."],
        ["Antibiotics and admission", "Antibiotics follow blood in the maxillary sinus."],
        ["Urgent operative repair", "Not required without entrapment or globe injury."],
        ["Neurosurgical consult", "That is the basilar skull fracture pathway."],
        ["Immediate ophthalmology consult for a true blowout", "That applies to a true blowout, which this is being managed as without."]]),

 dict(topic="Retinal detachment", io=IO_A, lead="mechanism", cite=D % 35,
  q="A 59-year-old describes flashes for two weeks, then a curtain yesterday. Which sequence explains this?",
  opts=[["Posterior vitreous detachment, then traction opening a retinal break", "Correct. That is the usual order of events."],
        ["Retinal break first, then vitreous liquefaction", "The vitreous change usually comes first."],
        ["Choroidal neovascularisation with haemorrhage", "That is macular degeneration."],
        ["Optic nerve inflammation", "That gives painful loss with colour desaturation."],
        ["Arterial occlusion with retinal infarction", "That gives sudden painless loss without flashes."]]),

 dict(topic="Hyphema", io=IO_A, lead="next step", cite=D % 24,
  q="A 28-year-old has a hyphema and a distorted pupil after a penetrating injury. Which step must be omitted?",
  opts=[["Measuring the intraocular pressure", "Correct. Pressing on a possibly open globe risks extruding its contents."],
        ["Placing a rigid shield", "That is exactly what should be done."],
        ["Giving an antiemetic", "That is part of management."],
        ["Calling ophthalmology", "That is part of management."],
        ["Confirming tetanus status", "That is part of management."]]),

 dict(topic="Care by age", io=IO_B, lead="patient education", cite=D % 18,
  q="A 12-year-old scratched his cornea playing. His parent asks for anaesthetic drops for the pain at home. Which is the most appropriate response?",
  opts=[["Decline, because they delay healing and can cause an ulcer", "Correct. This holds at any age."],
        ["Prescribe them for 24 hours only", "A shorter course carries the same risks."],
        ["Prescribe them, since children tolerate pain poorly", "Age does not change the risk."],
        ["Prescribe a corticosteroid drop instead", "Steroids are not the treatment for an abrasion."],
        ["Prescribe nothing at all", "An antibiotic and analgesia are still appropriate."]]),
]
