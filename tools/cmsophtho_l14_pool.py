# -*- coding: utf-8 -*-
"""Ocular Trauma (Lecture 14) -- Updated ophthalmology masters.

In trauma the thing that changes the outcome is usually what you REFRAIN from
doing, so several stems ask what must be avoided rather than what to give. The
four do-nots are the spine of this pool.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "CMS I Ocular Trauma"
IO = ("a — Ocular trauma: etiologies, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, prognosis")

QUESTIONS = [

Q("Trauma first principles", IO,
  "A 24-year-old man is brought in after a workshop explosion. His right eye is obviously injured "
  "and he is breathing noisily. What comes first?",
  [["Airway, breathing and circulation", "Correct. The eye waits until the patient is stable."],
   ["Visual acuity in both eyes", "Acuity matters, but not before the airway."],
   ["A rigid shield over the injured eye", "The shield goes on once the patient is stable."],
   ["Ophthalmology consultation", "Called after the primary survey."]],
  "treatment", D, 3),

Q("Trauma first principles", IO,
  "A 31-year-old man was grinding metal without eye protection and may have a retained fragment. "
  "Which imaging must be AVOIDED?",
  [["Magnetic resonance imaging", "Correct. A magnetic field can drag a metallic fragment through "
                                  "the eye."],
   ["Computed tomography of the orbit", "The study of choice — it localises the fragment without "
                                        "moving it."],
   ["Plain orbital radiograph", "Less useful than computed tomography but not dangerous."],
   ["Ocular ultrasound without pressure", "Pressure is the hazard; a careful scan is not "
                                          "forbidden outright."]],
  "two-step", D, 6),

Q("Open globe injury", IO,
  "A 28-year-old man has a nail protruding from his left eye after a nail gun discharged. What "
  "should be done with the nail?",
  [["Leave it in place", "Correct. It may be tamponading the wound, and removal risks extruding "
                         "intraocular contents."],
   ["Remove it and irrigate the tract", "Removal in the emergency department risks extrusion."],
   ["Remove it under topical anaesthetic", "Anaesthesia does not make removal safe."],
   ["Remove it only once the patient is stable", "Stability does not change the risk to the eye."]],
  "treatment", D, 6),

Q("Open globe injury", IO,
  "A 36-year-old woman has a suspected open globe injury. Which action must be avoided in any "
  "suspected ocular trauma?",
  [["Dilating the pupil", "Correct. It removes the pupil examination, one of the few windows onto "
                          "the inside of the eye."],
   ["Checking visual acuity", "Part of the assessment in a cooperative patient."],
   ["Asking about tetanus status", "Required after penetration with metal or organic material."],
   ["Testing confrontation fields", "Appropriate where the patient can cooperate."]],
  "two-step", D, 6),

Q("Globe rupture", IO,
  "A 44-year-old man was struck in the eye with a squash ball. Vision is hand movements only. "
  "Examination shows a peaked, teardrop-shaped pupil and a deep anterior chamber. What is the most "
  "likely diagnosis?",
  [["Globe rupture", "Correct. A peaked pupil points toward the rupture site; the chamber deepens "
                     "with a posterior rupture."],
   ["Hyphema alone", "Blood layering in the anterior chamber, without pupil distortion."],
   ["Corneal abrasion", "A surface epithelial defect that does not distort the pupil."],
   ["Anterior uveitis", "Photophobia with cells in the chamber, and the pupil stays round."]],
  "diagnosis", D, 17),

Q("Globe rupture", IO,
  "A 39-year-old woman has a suspected globe rupture. What is the immediate management?",
  [["Rigid shield, nil by mouth, antiemetics and urgent ophthalmology referral",
    "Correct. Nothing that raises intraocular pressure, and no pressure on the eye."],
   ["Pad and bandage the eye firmly", "Pressure on a ruptured globe can extrude its contents."],
   ["Irrigate the eye copiously", "Irrigation is for chemical injury, not a rupture."],
   ["Discharge with oral antibiotics", "This is a surgical emergency."]],
  "treatment", D, 17),

Q("Corneal abrasion", IO,
  "A 26-year-old woman has severe pain, tearing and photophobia in the right eye after a "
  "fingernail scratch. Fluorescein shows a well-defined epithelial defect with no infiltrate. What "
  "is the most appropriate treatment?",
  [["Topical antibiotic ointment and analgesia", "Correct, with follow-up to confirm healing."],
   ["Topical anaesthetic drops to take home",
    "Repeated topical anaesthetic is toxic to the epithelium and delays healing."],
   ["A tight pressure patch for a week", "Patching is no longer routine and is avoided in contact "
                                         "lens wearers."],
   ["Oral acyclovir", "Reserved for herpetic disease, and there is no dendrite here."]],
  "treatment", D, 18),

Q("Corneal abrasion", IO,
  "A 29-year-old man asks for a bottle of the numbing drops that relieved his corneal abrasion pain "
  "in the emergency department. Why should he not be given them?",
  [["Repeated use is toxic to the epithelium and delays healing",
    "Correct — and it masks worsening infection."],
   ["They cause permanent pupil dilation", "Not an effect of topical anaesthetic."],
   ["They cause an allergic reaction in most patients",
    "Allergy is not the reason for the restriction."],
   ["They stain the cornea permanently", "Fluorescein stains temporarily; anaesthetic does not "
                                         "stain."]],
  "two-step", D, 18),

Q("Corneal foreign body", IO,
  "A 33-year-old man has a metallic foreign body embedded in the cornea with a surrounding rust "
  "ring, 24 hours after grinding. Vision is 6/9. What is the most appropriate management?",
  [["Remove the foreign body and the rust ring, then topical antibiotics",
    "Correct — the rust ring is removed too, as it perpetuates inflammation."],
   ["Leave it and review in a week", "Retained metal and rust cause ongoing inflammation."],
   ["Refer for immediate surgical exploration of the globe",
    "Not required for a superficial corneal foreign body."],
   ["Irrigate with saline only", "Irrigation does not dislodge an embedded fragment."]],
  "treatment", D, 21),

Q("Hyphema", IO,
  "A 19-year-old man was hit in the eye by a paintball. Examination shows blood layered in the "
  "lower part of the anterior chamber occupying about a third of it. What is the most appropriate "
  "management?",
  [["Upright positioning, rigid shield and urgent ophthalmology review",
    "Correct — keeping the head up lets the blood settle inferiorly and clear the visual axis."],
   ["Lie the patient flat and observe", "Lying flat disperses the blood across the visual axis."],
   ["Discharge with topical antibiotics", "Hyphema requires monitoring for rebleed and pressure "
                                          "rise."],
   ["Start aspirin for the bruising", "Antiplatelet agents increase the risk of rebleeding."]],
  "treatment", D, 24),

Q("Hyphema", IO,
  "A 17-year-old boy with a traumatic hyphema is being counselled. Which complication is he being "
  "monitored for over the next few days?",
  [["Rebleeding with a rise in intraocular pressure",
    "Correct — the rebleed risk peaks in the first three to five days."],
   ["Development of a cataract within 48 hours",
    "Cataract can follow trauma but is not the acute monitoring concern."],
   ["Retinal detachment within 24 hours", "A later concern rather than the reason for close "
                                          "monitoring."],
   ["Optic neuritis", "An inflammatory demyelinating condition, unrelated to trauma."]],
  "two-step", D, 25),

Q("Hyphema", IO,
  "A 15-year-old boy of African ancestry has a traumatic hyphema. Which screening test is "
  "particularly important in his case?",
  [["Sickle cell testing", "Correct. Sickling in the anterior chamber obstructs outflow and raises "
                           "pressure at lower blood volumes."],
   ["Thyroid function", "No bearing on anterior chamber blood or outflow."],
   ["Serum calcium", "Not a factor in hyphema or its complications."],
   ["Erythrocyte sedimentation rate", "That belongs to the giant cell arteritis pathway."]],
  "two-step", D, 25),

Q("Lid laceration", IO,
  "A 41-year-old woman has a lid laceration 4 mm from the medial canthus after a dog bite. Why does "
  "that location matter?",
  [["The canalicular drainage system may be transected",
    "Correct — a missed canalicular injury leaves the patient tearing for life."],
   ["It always indicates a globe rupture", "Location alone does not indicate rupture."],
   ["It cannot be repaired surgically", "It can and should be repaired, by ophthalmology."],
   ["It means the levator muscle is involved", "Levator injury is a concern in UPPER lid "
                                               "lacerations through the tarsus."]],
  "two-step", D, 26),

Q("Orbital floor fracture", IO,
  "A 22-year-old man was punched in the right eye. He has double vision when looking UP, numbness "
  "of the right cheek and upper lip, and the eye appears sunken. What is the most likely diagnosis?",
  [["Orbital floor (blowout) fracture", "Correct. Inferior rectus entrapment limits upgaze and the "
                                        "infraorbital nerve supplies the cheek."],
   ["Globe rupture", "Would show a peaked pupil and severely reduced vision."],
   ["Medial wall fracture", "Restricts horizontal rather than vertical gaze."],
   ["Orbital contusion", "Bruising and swelling without the restricted upgaze or numbness."]],
  "diagnosis", D, 41),

Q("Orbital floor fracture", IO,
  "A 9-year-old boy was struck in the eye with a ball. He has severe pain, nausea and vomiting, and "
  "bradycardia on attempted upgaze, but the eye looks remarkably quiet. What does this suggest?",
  [["Entrapment of the inferior rectus in an orbital floor fracture",
    "Correct. Restricted upgaze with severe pain and AUTONOMIC DISTURBANCE "
    "— bradycardia and vomiting on attempted movement — is the entrapment picture."],
   ["Periorbital haematoma", "Bruising and swelling, without restricted upgaze or bradycardia."],
   ["Anterior uveitis", "Photophobia and cells, without the autonomic disturbance."],
   ["Concussion without ocular injury", "The restricted upgaze localises the problem to the "
                                        "orbit."]],
  "diagnosis", D, 42),

Q("Orbital floor fracture", IO,
  "A 10-year-old girl has a white-eyed blowout fracture with entrapment. Why is urgent surgical "
  "referral required rather than routine review?",
  [["Entrapped muscle becomes ischaemic and fibroses",
    "Correct — delay risks permanent restriction of eye movement."],
   ["The eye will become infected", "Infection is not the driver of urgency here."],
   ["Vision will be lost immediately", "Acuity is often preserved; the muscle is what is at risk."],
   ["It always progresses to globe rupture", "Entrapment does not cause rupture."]],
  "two-step", D, 43),

Q("Retinal detachment", IO,
  "A 47-year-old man develops floaters, flashes and a curtain over his vision two weeks after blunt "
  "ocular trauma. Which type of detachment is most likely?",
  [["Rhegmatogenous", "Correct — a retinal break allows fluid beneath the retina, and trauma is a "
                      "common cause."],
   ["Exudative", "Fluid accumulates without a break, usually from inflammation or tumour."],
   ["Traction", "Fibrovascular membranes pull the retina off, classically in diabetes."],
   ["Combined traction and exudative", "Not the mechanism following a discrete injury."]],
  "diagnosis", D, 35),

Q("Retinal detachment", IO,
  "Which type of retinal detachment is NOT primarily treated surgically?",
  [["Exudative", "Correct. There is no break and no traction, so the underlying disease is "
                 "treated."],
   ["Traction", "Requires surgical release of the membranes."],
   ["Combined rhegmatogenous and traction", "Still a surgical problem."],
   ["All three are surgical", "Exudative is the exception."]],
  "two-step", D, 39),

Q("Basilar skull fracture", IO,
  "A 34-year-old man has clear fluid dripping from his nose after a head injury. On the bedsheet it "
  "dries as a central red stain with a clear outer ring. What does this indicate?",
  [["Cerebrospinal fluid leak from a basilar skull fracture",
    "Correct — the halo or double ring sign. Neurosurgical referral and admission."],
   ["Simple epistaxis", "Blood alone does not separate into two rings."],
   ["Lacrimal duct injury", "Tears drain into the nose but do not produce this sign."],
   ["Allergic rhinorrhoea", "Clear, but it does not carry blood or form a ring."]],
  "diagnosis", D, 44),

Q("Basilar skull fracture", IO,
  "A 51-year-old woman has bruising over both mastoid processes two days after a fall. What is this "
  "sign called, and what does it indicate?",
  [["Battle sign, indicating a basilar skull fracture", "Correct."],
   ["Periorbital haematoma from direct trauma",
    "That is bruising around the eyes rather than behind the ears."],
   ["Subconjunctival haemorrhage", "That is blood under the conjunctiva of the eye."],
   ["Periorbital subcutaneous emphysema", "Air in the tissues, which crackles on palpation."]],
  "two-step", D, 47),

Q("Periorbital haematoma", IO,
  "A 38-year-old man has a black eye after being punched. Which finding would make this more than "
  "a simple contusion?",
  [["A relative afferent pupillary defect", "Correct — that indicates optic nerve involvement and "
                                            "changes the urgency entirely."],
   ["Bruising extending to the cheek", "Common with a periorbital haematoma."],
   ["Lid swelling that limits opening", "Expected with significant soft tissue injury."],
   ["Subconjunctival haemorrhage", "Frequently accompanies blunt periorbital trauma."]],
  "two-step", D, 33),
]
