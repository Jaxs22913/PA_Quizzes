# -*- coding: utf-8 -*-
"""CMS I Exam 2, Lecture 14 (Ocular Trauma) -- objective set C.

The remainder of the objective bank, so the pair of 30s has room. Weighted
toward objective b, care strategies by age, which the other two pools touch
only lightly, and toward the discriminations that decide disposition.

SELF-CONTAINED. FIVE options; correct answer authored FIRST.
"""
D = "CMS I Ocular Trauma - Shah Fallsv.pptx, Slide %d"
IO_A = "a — Ocular trauma: etiology, manifestations, testing, management, referral, prognosis"
IO_B = "b — Identify medical care strategies for common ophthalmological disorders by age"

QUESTIONS = [
 dict(topic="Care by age", io=IO_B, lead="diagnosis", cite=D % 41,
  q="Which feature of orbital floor fracture is specific to children?",
  opts=[["Entrapment can occur with no orbital soft tissue signs at all", "Correct — the white-eyed blowout."],
        ["Entrapment never occurs before adolescence", "It does occur, and can be occult."],
        ["Children always have marked periorbital swelling", "They may have none."],
        ["Children do not develop infraorbital numbness", "Not the described distinction."],
        ["Children need no imaging", "Imaging is still computed tomography."]]),

 dict(topic="Care by age", io=IO_B, lead="next step", cite=D % 41,
  q="A child with a quiet-looking eye vomits and becomes bradycardic each time he looks up after facial trauma. What does that combination represent?",
  opts=[["Extraocular muscle entrapment with autonomic disturbance", "Correct. Severe pain, bradycardia and vomiting on eye movement point to entrapment."],
        ["Raised intracranial pressure", "That does not fire specifically on attempted upgaze."],
        ["Vasovagal response to pain", "The trigger is eye movement specifically."],
        ["Gastroenteritis coinciding with the injury", "That does not track eye movement."],
        ["Concussion alone", "Concussion does not produce gaze-provoked bradycardia."]]),

 dict(topic="Care by age", io=IO_B, lead="risk factor", cite=D % 5,
  q="In which population is ocular trauma the leading cause of monocular blindness, and why does that shape counselling?",
  opts=[["Young adult men, so eye protection is the message that matters most", "Correct. That is the group in which it leads."],
        ["Elderly women, so fall prevention is the message", "Not the group in which trauma leads."],
        ["Infants, so childproofing is the message", "Not the group in which trauma leads."],
        ["Adolescent girls, so sports goggles are the message", "Not the group in which trauma leads."],
        ["Men over seventy, so driving assessment is the message", "Not the group in which trauma leads."]]),

 dict(topic="Retinal detachment", io=IO_A, lead="diagnosis", cite=D % 36,
  q="Which set of symptoms fits a retinal detachment?",
  opts=[["A curtain or shadow, floaters, momentary flashes, and a monocular field defect",
         "Correct. Cloudy or smoky vision belongs there too."],
        ["A painful red eye with a hazy cornea and haloes", "That is acute angle closure."],
        ["Gradual painless loss of the peripheral field over years", "That is chronic open-angle glaucoma."],
        ["Pain on eye movement with loss of colour vision", "That is optic neuritis."],
        ["Bilateral disc swelling with transient obscurations", "That is papilledema."]]),

 dict(topic="Open globe injury", io=IO_A, lead="management", cite=D % 17,
  q="Which set of measures accompanies the shield in a suspected open globe?",
  opts=[["Antiemetics, analgesia and tetanus, with computed tomography to look for a foreign body",
         "Correct. Keeping the patient from straining protects the eye."],
        ["A mydriatic, tonometry and fundoscopy", "None of those is safe in a possibly open globe."],
        ["Copious irrigation and a pressure patch", "Pressure risks extruding contents."],
        ["Topical anaesthetic drops to take home", "Never sent home, in any eye injury."],
        ["Oral corticosteroids and observation", "Not the described management."]]),
]
