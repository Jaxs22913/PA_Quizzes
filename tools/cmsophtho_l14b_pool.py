# -*- coding: utf-8 -*-
"""Ocular Trauma (Lecture 14) -- second pool."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "CMS I Ocular Trauma"
IO = ("a — Ocular trauma: etiologies, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, prognosis")

QUESTIONS = [

Q("Full-thickness eye wall laceration", IO,
  "A 30-year-old man was struck by a shard of glass. Examination shows a full-thickness corneal "
  "laceration with iris prolapsing through it. What must NOT be attempted?",
  [["Repositing the prolapsed iris in the emergency department",
    "Correct — manipulation risks further extrusion and infection; shield and refer."],
   ["Placing a rigid shield", "The correct protective step."],
   ["Giving intravenous antibiotics", "Appropriate prophylaxis for an open globe."],
   ["Checking tetanus status", "Required after penetrating injury."],
   ["Keeping the patient nil by mouth", "Appropriate ahead of surgery."]],
  "two-step", D, 15),

Q("Open globe injury", IO,
  "A 27-year-old woman has a suspected open globe. Which set of signs does the lecture list?",
  [["Pupillary distortion, a flat anterior chamber and a soft eye",
    "Correct, with extraocular protrusion of uveal tissue and massive haemorrhagic chemosis."],
   ["A mid-dilated fixed pupil and a hazy cornea", "That is the angle-closure picture."],
   ["Follicles and a tender preauricular node", "That is viral conjunctivitis."],
   ["Greasy lashes with debris at the bases", "That is blepharitis."],
   ["Bilateral disc swelling with normal acuity", "That is papilledema."]],
  "two-step", D, 14),

Q("Orbital contusion", IO,
  "A 25-year-old man was elbowed in the eye during football. He has lid swelling and bruising, "
  "vision is 6/6, the pupils are equal and reactive, eye movements are full and the globe is "
  "intact. What is the most appropriate management?",
  [["Ice, analgesia and review if symptoms change",
    "Correct — a simple orbital contusion with normal function needs supportive care."],
   ["Admit for intravenous antibiotics", "There is no infection."],
   ["Urgent surgical exploration", "Not indicated with normal vision and full movements."],
   ["Topical corticosteroids", "No role in a simple contusion."],
   ["Immediate computed tomography for all patients",
    "Imaging follows specific concerning findings, which are absent here."]],
  "treatment", D, 31),

Q("Corneal foreign body", IO,
  "A 34-year-old welder has a superficial corneal foreign body removed. What must be checked before "
  "he leaves?",
  [["That there is no second, deeper penetrating injury",
    "Correct — a superficial fragment can accompany a penetrating one."],
   ["His refraction", "Not the safety check after foreign body removal."],
   ["His colour vision", "Assesses optic nerve function, not relevant here."],
   ["His visual fields", "Not the relevant check for a corneal injury."],
   ["His intraocular pressure only", "Pressure alone would not exclude penetration."]],
  "two-step", D, 22),

Q("Hyphema", IO,
  "A 20-year-old man with a hyphema is given instructions for the next five days. Which activity "
  "must he avoid?",
  [["Strenuous activity and bending forward",
    "Correct — both raise the risk of rebleeding."],
   ["Reading", "Reading does not affect rebleed risk."],
   ["Watching television", "No effect on the eye."],
   ["Drinking fluids", "Not restricted."],
   ["Sleeping on his back", "Upright positioning is advised; lying supine is what is avoided, but "
                            "the key restriction is exertion."]],
  "two-step", D, 25),

Q("Lid laceration", IO,
  "A 29-year-old woman has a lid laceration through the lid MARGIN of the upper lid. Why does that "
  "require specialist repair?",
  [["Imprecise alignment produces a permanent notch and chronic irritation",
    "Correct — margin-involving lacerations need meticulous approximation."],
   ["It always transects the canaliculus", "That is the concern with MEDIAL lacerations."],
   ["It indicates an open globe", "Not implied by a lid laceration."],
   ["It cannot be repaired at all", "It can and should be repaired."],
   ["It always involves the levator muscle", "Levator involvement is a separate concern with deep "
                                             "upper lid wounds."]],
  "two-step", D, 27),

Q("Orbital floor fracture", IO,
  "A 33-year-old man with an orbital floor fracture is advised not to blow his nose. Why?",
  [["It can force air from the sinus into the tissues",
    "Correct — periorbital subcutaneous emphysema, which the deck lists as a feature of "
    "orbital floor fracture."],
   ["It will restart the nosebleed", "Not the reason specific to an orbital fracture."],
   ["It will displace the fracture fragments", "Not the mechanism of concern."],
   ["It will worsen the diplopia permanently", "Diplopia relates to muscle entrapment."],
   ["It will cause a cerebrospinal fluid leak", "That concern belongs to basilar skull fracture."]],
  "two-step", D, 43),

Q("Retrobulbar haemorrhage", IO,
  "A 47-year-old man has proptosis, a tense orbit, severely reduced vision and a relative afferent "
  "pupillary defect one hour after facial trauma. What is the most appropriate immediate action?",
  [["Lateral canthotomy and cantholysis", "Correct — an orbital compartment syndrome needs "
                                          "decompression within minutes to save the nerve."],
   ["Urgent computed tomography before any intervention",
    "Imaging delays a sight-saving procedure that is diagnosed clinically."],
   ["Topical antiglaucoma drops alone", "Insufficient for a compartment syndrome."],
   ["Ice and observation", "Observation forfeits the window."],
   ["Immediate enucleation", "Grossly disproportionate and not the treatment."]],
  "treatment", D, 33),

Q("Chemical injury", IO,
  "A 28-year-old worker has a chemical splash to the eye. What is the single most important "
  "action?",
  [["Copious irrigation before anything else",
    "Correct. The referral-timing slide lists chemical injury as EMERGENT and says "
    "IRRIGATE FIRST."],
   ["Checking visual acuity first", "Acuity waits; irrigation cannot."],
   ["Computed tomography of the orbit", "Imaging is irrelevant to a surface chemical burn."],
   ["Instilling topical antibiotics first", "Irrigation comes first."],
   ["Patching the eye and referring", "Patching a chemical injury without irrigation is harmful."]],
  "treatment", D, 3),

Q("Orbital contusion", IO,
  "A 24-year-old man was struck in the eye two days ago. He has lid bruising and swelling but "
  "vision is 6/6, the pupils are equal and reactive, and eye movements are full. What is the most "
  "likely diagnosis?",
  [["Orbital and lid contusion", "Correct — soft tissue injury with normal ocular function."],
   ["Globe rupture", "Would show pupillary distortion, a flat chamber and a soft eye."],
   ["Hyphema", "Blood would be layered visibly in the anterior chamber."],
   ["Orbital floor fracture", "Would restrict upgaze and produce cheek numbness."],
   ["Basilar skull fracture", "Would show bruising behind the ears or around both orbits."]],
  "diagnosis", D, 31),

Q("Basilar skull fracture", IO,
  "A 42-year-old man has periorbital bruising around BOTH eyes after a head injury, with no direct "
  "blow to either eye. What does this suggest?",
  [["Raccoon eyes from a basilar skull fracture",
    "Correct — bilateral periorbital bruising without direct trauma."],
   ["Battle sign", "That is bruising over the MASTOID processes."],
   ["Bilateral orbital floor fractures", "Would produce diplopia and enophthalmos."],
   ["Simple bilateral black eyes from the same blow",
    "A single blow rarely bruises both orbits symmetrically without direct contact."],
   ["Subconjunctival haemorrhage", "That is blood under the conjunctiva, not periorbital skin."]],
  "diagnosis", D, 44),

Q("Trauma disposition", IO,
  "Which finding after ocular trauma converts a routine review into an emergency referral?",
  [["A relative afferent pupillary defect", "Correct — it indicates optic nerve compromise."],
   ["Periorbital bruising", "Common and usually benign."],
   ["Subconjunctival haemorrhage", "Frequently accompanies blunt trauma."],
   ["Lid swelling", "Expected after soft tissue injury."],
   ["Mild photophobia", "Non-specific and common."]],
  "two-step", D, 3),
]
