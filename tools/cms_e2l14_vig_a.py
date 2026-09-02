# -*- coding: utf-8 -*-
"""CMS I Exam 2, Lecture 14 (Ocular Trauma) -- vignette set A.

Open globe, corneal abrasion and foreign body, hyphema, and the rules that
govern all of them. Patient stems in the CMS house style: FIVE options, a
varied lead-in, and a per-option refutation. SELF-CONTAINED throughout.

Correct answer authored FIRST; cms_e2_partition.py rotates it.
"""
D = "CMS I Ocular Trauma - Shah Fallsv.pptx, Slide %d"
IO_A = "a — Ocular trauma: etiology, manifestations, testing, management, referral, prognosis"
IO_B = "b — Identify medical care strategies for common ophthalmological disorders by age"

QUESTIONS = [
 dict(topic="Open globe injury", io=IO_A, lead="next step", cite=D % 17,
  q="A 34-year-old man was struck in the right eye by a baseball. The lid is swollen, the conjunctiva is deeply haemorrhagic and the globe feels soft. Which is the most appropriate next step?",
  opts=[["Tape a rigid shield over the eye and call ophthalmology", "Correct. A soft eye with massive haemorrhagic chemosis after blunt force is a globe rupture until proven otherwise."],
        ["Measure the intraocular pressure", "Pressing on a possibly open globe risks extruding its contents."],
        ["Instil a mydriatic and examine the fundus", "The eye is never dilated when trauma is suspected."],
        ["Irrigate the eye with copious saline", "Irrigation does nothing for a ruptured globe and adds pressure."],
        ["Apply a firm pressure patch", "Pressure is precisely what must be avoided."]]),

 dict(topic="Open globe injury", io=IO_A, lead="initial and confirmatory test", cite=D % 6,
  q="A 41-year-old welder felt something strike his eye while grinding without goggles. Vision is 20/40 and the eye is quiet. Which imaging is appropriate, and which must be avoided?",
  opts=[["Computed tomography of the orbit; avoid magnetic resonance imaging", "Correct. A magnetic field can move a metallic fragment through the eye."],
        ["Magnetic resonance imaging of the orbit; avoid computed tomography", "That reverses the safe choice."],
        ["Ocular ultrasound with firm probe pressure; avoid computed tomography", "Probe pressure is unsafe if the globe may be open."],
        ["Plain orbital radiograph alone; avoid computed tomography", "It cannot localise the fragment adequately."],
        ["No imaging, since acuity is preserved", "Vision can be normal with a retained intraocular fragment."]]),

 dict(topic="Open globe injury", io=IO_A, lead="management", cite=D % 6,
  q="A 19-year-old arrives with a fish hook embedded through the cornea. He is stable and in pain. Which is the most appropriate management of the hook?",
  opts=[["Leave it in place and arrange surgical repair", "Correct. It may be tamponading the wound, and removing it can extrude intraocular contents."],
        ["Withdraw it along its entry path", "Withdrawal risks extrusion of intraocular contents."],
        ["Cut it flush with the cornea and cover it", "Manipulation carries the same risk."],
        ["Push it through and out to avoid the barb", "That enlarges the wound."],
        ["Remove it after topical anaesthetic", "Anaesthesia does not make removal safe."]]),

 dict(topic="Corneal abrasion", io=IO_A, lead="patient education", cite=D % 18,
  q="A 27-year-old woman scratched her cornea removing a contact lens. Fluorescein confirms an abrasion. She asks for something for the pain to use at home. Which is the most appropriate response?",
  opts=[["Analgesia and a topical antibiotic, but not anaesthetic drops", "Correct. Take-home anaesthetic delays healing, masks worsening symptoms and can cause a corneal ulcer."],
        ["Topical anaesthetic drops four times daily", "That is the one thing that must not be sent home."],
        ["Topical anaesthetic drops for 48 hours only", "A shorter course carries the same risks."],
        ["Topical corticosteroid drops for comfort", "Steroids are not the treatment for an abrasion."],
        ["No treatment, since abrasions heal regardless", "An antibiotic and review are part of care."]]),

 dict(topic="Corneal foreign body", io=IO_A, lead="next step", cite=D % 21,
  q="A 38-year-old man has a foreign body sensation after a day of metalwork. Fluorescein shows several fine vertical lines running down the cornea. Which is the most appropriate next step?",
  opts=[["Evert the upper eyelid and inspect the tarsal conjunctiva", "Correct. Vertical linear defects mean the object is under the upper lid, scraping with each blink."],
        ["Examine the lower fornix with a cotton bud", "The vertical pattern points to the upper lid."],
        ["Order computed tomography of the orbit", "The object is on the surface."],
        ["Patch the eye and review in one week", "The object needs to come out now."],
        ["Refer for urgent surgical exploration", "It can be removed at the slit lamp."]]),

 dict(topic="Corneal foreign body", io=IO_A, lead="management", cite=D % 22,
  q="A metallic corneal foreign body is removed from a 45-year-old, leaving a brown ring in the stroma. Which is the most appropriate management of that ring?",
  opts=[["Remove it with a battery-operated burr", "Correct. A rust ring from iron or copper comes out with a burr."],
        ["Irrigate repeatedly with saline", "Irrigation will not lift a rust ring."],
        ["Wipe it with a cotton-tipped applicator", "That is for conjunctival foreign bodies."],
        ["Leave it, since it will resorb", "It does not resorb on its own."],
        ["Prescribe a chelating drop", "Not the described method."]]),

 dict(topic="Hyphema", io=IO_A, lead="diagnosis", cite=D % 24,
  q="A 16-year-old was hit in the eye by a paintball. There is a layer of blood across the lower anterior chamber with a visible fluid level. Which is the most likely diagnosis, and what else must be considered?",
  opts=[["Hyphema, and it can itself indicate an open globe", "Correct. It is not always an isolated injury."],
        ["Hyphema, which rules out an open globe", "It does not exclude one."],
        ["Subconjunctival haemorrhage overlying the iris", "That sits on the surface, outside the chamber."],
        ["Vitreous haemorrhage seen through the pupil", "That lies behind the lens."],
        ["Traumatic iritis with cells in the chamber", "Cells are not a layered blood level."]]),

 dict(topic="Hyphema", io=IO_A, lead="management", cite=D % 25,
  q="A 22-year-old with a traumatic hyphema is admitted. Which regimen fits, and what is it aiming at?",
  opts=[["Bed rest head-up, antiemetics, cycloplegic and aminocaproic acid, to prevent a rebleed",
         "Correct. Every element serves that one goal."],
        ["Ambulation and warm compresses, to clear the blood faster", "Speed of clearance is not the aim, and activity risks a rebleed."],
        ["Aspirin, to prevent clot organisation", "Aspirin raises the risk of a secondary haemorrhage."],
        ["Topical anaesthetic and discharge, with review in a week", "This needs monitoring, not discharge."],
        ["Immediate surgical washout in all cases", "Not the described first-line management."]]),

 dict(topic="Hyphema", io=IO_A, lead="prognosis", cite=D % 25,
  q="A 30-year-old with a hyphema asks how long the dangerous period lasts. Which is the most accurate response?",
  opts=[["The first 72 hours, when most rebleeding happens", "Correct. A secondary haemorrhage is what costs vision permanently."],
        ["The first 24 hours only", "The window is longer than a day."],
        ["The second week, once the clot retracts", "Later than the peak risk."],
        ["There is no dangerous period once bleeding stops", "Rebleeding is the whole concern."],
        ["The first month, evenly throughout", "The risk is concentrated much earlier."]]),

 dict(topic="Hyphema", io=IO_A, lead="risk factor", cite=D % 25,
  q="A 15-year-old with sickle cell disease sustains a hyphema. Why does that history matter?",
  opts=[["It raises the risk of complications", "Correct. Sickle cell disease is specifically flagged."],
        ["It rules out a rebleed", "It does the opposite."],
        ["It makes aminocaproic acid unnecessary", "It does not remove the need to prevent a rebleed."],
        ["It means the pressure need not be checked", "Pressure is still measured unless the globe may be open."],
        ["It makes the hyphema resolve faster", "It does not."]]),

 dict(topic="Trauma first principles", io=IO_A, lead="next step", cite=D % 3,
  q="A 52-year-old is brought in after a road traffic collision with an obviously injured left eye, confusion and shallow breathing. Which is the most appropriate first action?",
  opts=[["Assess airway, breathing and circulation", "Correct. The eye is assessed after the patient is stabilised."],
        ["Measure visual acuity in both eyes", "Acuity waits until the primary survey is done."],
        ["Instil fluorescein and examine the cornea", "The surface examination is not the first action."],
        ["Order computed tomography of the orbits", "Imaging follows resuscitation."],
        ["Call ophthalmology before anything else", "The consult follows the primary survey."]]),

 dict(topic="Trauma first principles", io=IO_A, lead="management", cite=D % 6,
  q="A 29-year-old has a wooden splinter driven into the periorbital tissue while gardening. Beyond removing nothing and imaging appropriately, which additional step is required?",
  opts=[["Confirm tetanus is up to date", "Correct. Penetration with metal or organic material carries the risk."],
        ["Start systemic antivirals", "There is no viral indication here."],
        ["Give a mydriatic to examine the retina", "The eye is not dilated in trauma."],
        ["Arrange an urgent visual field test", "Not the immediate priority."],
        ["Begin oral corticosteroids", "Not indicated for a penetrating splinter."]]),

 dict(topic="Assessment", io=IO_A, lead="history", cite=D % 8,
  q="A 25-year-old with an eye injury is intoxicated and gives an inconsistent account. Which is the most appropriate way to establish the mechanism?",
  opts=[["Ask family, friends or bystanders", "Correct. The circumstance of injury still has to be established."],
        ["Rely on the examination findings alone", "Findings do not give mechanism or velocity."],
        ["Wait until he is sober to take a history", "Delay costs time in an injury that may need surgery."],
        ["Accept the account as given", "An inconsistent account leaves the mechanism unknown."],
        ["Record the mechanism as unknown and proceed", "A collateral history is available and useful."]]),
]
