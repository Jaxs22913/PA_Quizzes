# -*- coding: utf-8 -*-
"""CMS I Exam 2, Lecture 14 (Ocular Trauma) -- objective set A.

The rules that apply before any diagnosis, assessment, open globe injury,
corneal abrasion and foreign body, and hyphema.

Grounded in the deck (Chand Shah, MPAS, PA-C). SELF-CONTAINED: no question
refers to "the lecture" or "the deck".

FIVE options, per the CMS house style. Correct answer is authored FIRST in
every question; cms_e2_partition.py rotates it.
"""
D = "CMS I Ocular Trauma - Shah Fallsv.pptx, Slide %d"
IO_A = "a — Ocular trauma: etiology, manifestations, testing, management, referral, prognosis"
IO_B = "b — Identify medical care strategies for common ophthalmological disorders by age"

QUESTIONS = [
 # ---------------- the rules that come first ----------------
 dict(topic="Trauma first principles", io=IO_A, lead="next step", cite=D % 3,
  q="A 24-year-old man arrives after a workshop explosion with an obviously injured right eye and noisy breathing. What comes first?",
  opts=[["Airway, breathing and circulation", "Correct. The eye waits until the patient is stable."],
        ["Visual acuity in both eyes", "Acuity matters, but not before the airway."],
        ["A shield over the injured eye", "The shield comes once the patient is stable."],
        ["Computed tomography of the orbits", "Imaging follows resuscitation."],
        ["Ophthalmology consultation", "The consult is called after the primary survey."]]),

 dict(topic="Trauma first principles", io=IO_A, lead="next step", cite=D % 6,
  q="A metal fragment may be lodged in the eye after grinding. Which study is ordered?",
  opts=[["Computed tomography of the orbit", "Correct. It answers the question without moving the fragment."],
        ["Magnetic resonance imaging of the orbit", "A magnetic field can drag a metallic fragment through the eye."],
        ["Ocular ultrasound with pressure on the globe", "Pressure risks extruding contents if the globe is open."],
        ["Plain orbital radiograph alone", "It cannot localise the fragment adequately."],
        ["No imaging unless vision is reduced", "Vision can be preserved with a retained fragment."]]),

 dict(topic="Trauma first principles", io=IO_A, lead="management", cite=D % 6,
  q="A nail is protruding from a patient's eye. What is done with it?",
  opts=[["Leave it in place", "Correct. It may be tamponading the wound, and removal can extrude intraocular contents."],
        ["Remove it and irrigate the tract", "Removing it in the emergency department risks extrusion."],
        ["Remove it only if the patient is stable", "Stability does not change the risk."],
        ["Cut it flush with the cornea", "Manipulating it at all risks the same extrusion."],
        ["Remove it under topical anaesthetic", "Anaesthesia does not make removal safe here."]]),

 dict(topic="Trauma first principles", io=IO_A, lead="management", cite=D % 6,
  q="Which action must be avoided whenever ocular trauma is suspected?",
  opts=[["Dilating the eye", "Correct. It removes the pupil examination, one of the few windows onto the inside of the eye."],
        ["Checking visual acuity", "Acuity is part of the assessment when the patient can cooperate."],
        ["Asking about tetanus status", "That is required after penetration with metal or organic material."],
        ["Inspecting the periorbital tissues", "Inspection is the first part of the examination."],
        ["Testing confrontation fields", "That is appropriate in a cooperative patient."]]),

 dict(topic="Trauma first principles", io=IO_A, lead="next step", cite=D % 6,
  q="Which feature makes computed tomography without contrast automatic after trauma?",
  opts=[["Loss of consciousness", "Correct. It sits alongside alcohol, confusion, tachypnoea, apnoeic breathing, anticoagulants and eye penetration."],
        ["Subconjunctival haemorrhage alone", "That alone does not mandate imaging."],
        ["Photophobia", "A symptom rather than an imaging trigger."],
        ["Excessive tearing", "A symptom rather than an imaging trigger."],
        ["A foreign body sensation", "That points to the surface, not to imaging."]]),

 dict(topic="Trauma epidemiology", io=IO_A, lead="epidemiology", cite=D % 5,
  q="Ocular trauma is the leading cause of monocular blindness in which group?",
  opts=[["Young adult men", "Correct. That is the group in which it leads."],
        ["Elderly women", "Not the group in which trauma leads."],
        ["Children under five", "Not the group in which trauma leads."],
        ["Adolescent girls", "Not the group in which trauma leads."],
        ["Men over seventy", "Not the group in which trauma leads."]]),

 dict(topic="Assessment", io=IO_A, lead="history", cite=D % 8,
  q="A patient with ocular trauma is intoxicated and cannot give a history. Where should the account come from?",
  opts=[["Family, friends or bystanders", "Correct. The circumstance of injury still has to be established."],
        ["The medical record alone", "It will not carry the circumstance of this injury."],
        ["Waiting until the patient sobers", "Delay costs time in an injury that may need surgery."],
        ["The examination findings alone", "Findings do not establish mechanism or velocity."],
        ["The transferring service's diagnosis", "That is not a substitute for the history."]]),

 dict(topic="Assessment", io=IO_A, lead="history", cite=D % 8,
  q="Which history point matters because surgery may follow?",
  opts=[["When the patient last ate and drank", "Correct. Nil-by-mouth status shapes the anaesthetic plan."],
        ["Which eye is dominant", "It does not change acute management."],
        ["The patient's usual spectacle prescription", "Not what determines operative timing."],
        ["Whether the patient wears contact lenses at night", "Relevant to infection, not to operative timing."],
        ["Family history of glaucoma", "Not relevant to acute trauma management."]]),

 # ---------------- open globe ----------------
 dict(topic="Open globe injury", io=IO_A, lead="diagnosis", cite=D % 14,
  q="A 30-year-old has a distorted pupil pulled toward a corneal wound, a flat anterior chamber and a soft eye. Which diagnosis fits?",
  opts=[["Open globe injury", "Correct. Those three findings together define a full-thickness defect."],
        ["Corneal abrasion", "An abrasion leaves the chamber formed and the pupil round."],
        ["Traumatic iritis", "Iritis does not flatten the anterior chamber."],
        ["Subconjunctival haemorrhage", "That is confined to the surface."],
        ["Orbital contusion", "Contusion is soft tissue swelling without a globe defect."]]),

 dict(topic="Open globe injury", io=IO_A, lead="management", cite=D % 17,
  q="An open globe injury is suspected. What is placed over the eye?",
  opts=[["A rigid protective shield", "Correct. It keeps pressure off the globe until repair."],
        ["A pressure patch", "Pressure can extrude intraocular contents."],
        ["A saline-soaked gauze dressing", "It provides no protection against pressure."],
        ["Nothing, so the eye can be re-examined", "The eye needs protecting between examinations."],
        ["An ice pack held against the lid", "Direct pressure is exactly what to avoid."]]),

 dict(topic="Open globe injury", io=IO_A, lead="management", cite=D % 17,
  q="Why are antiemetics given alongside analgesia in a suspected open globe?",
  opts=[["Vomiting raises intraocular pressure and can extrude contents", "Correct. Keeping the patient from straining protects the eye."],
        ["They reduce the risk of endophthalmitis", "They have no antimicrobial effect."],
        ["They lower the intraocular pressure directly", "They act on nausea, not on pressure directly."],
        ["They allow the eye to be dilated safely", "The eye is not dilated in trauma."],
        ["They shorten the time to surgical repair", "They do not affect operative scheduling."]]),

 dict(topic="Globe rupture", io=IO_A, lead="diagnosis", cite=D % 17,
  q="At which sites does a globe most often rupture under blunt force?",
  opts=[["Posterior to the muscle insertions, old surgical incisions, and the lamina cribrosa",
         "Correct. Those are the weak points."],
        ["The central cornea and the visual axis", "The central cornea is not the weak point."],
        ["The limbus alone", "Rupture is not confined there."],
        ["The macula and optic disc", "Those are retinal structures, not the eye wall."],
        ["The lacrimal sac", "It is not part of the globe."]]),

 dict(topic="Globe rupture", io=IO_A, lead="risk factor", cite=D % 17,
  q="Which history makes globe rupture more likely at lower force?",
  opts=[["Previous intraocular surgery", "Correct. Old incisions leave a permanent weak point."],
        ["A history of migraine", "It does not weaken the eye wall."],
        ["Long-standing myopia alone", "Myopia predisposes to detachment rather than rupture."],
        ["Seasonal allergic conjunctivitis", "It does not affect eye wall strength."],
        ["Previous corneal abrasion", "A healed abrasion does not weaken the wall."]]),

 dict(topic="Full-thickness eye wall laceration", io=IO_A, lead="management", cite=D % 16,
  q="A foreign body sits in the posterior segment at initial evaluation. What is done?",
  opts=[["Leave it alone for now", "Correct. Retrieving it early risks more damage to ocular structures."],
        ["Remove it immediately with forceps", "That risks additional injury."],
        ["Remove it under topical anaesthetic", "Anaesthesia does not reduce the structural risk."],
        ["Irrigate it out with balanced salt solution", "Irrigation will not reach it and risks harm."],
        ["Apply a magnet to draw it forward", "That is not the initial approach."]]),

 dict(topic="Full-thickness eye wall laceration", io=IO_A, lead="diagnosis", cite=D % 16,
  q="A laceration has cut the lens capsule. What happens to the lens?",
  opts=[["It becomes hydrated, oedematous and opaque", "Correct. Aqueous entering the capsule clouds it."],
        ["It hardens and darkens", "That describes an age-related nuclear change."],
        ["It is unaffected if the cut is peripheral", "A capsular breach affects the lens wherever it sits."],
        ["It dislocates posteriorly in every case", "Dislocation is not the described consequence."],
        ["It calcifies over several days", "Calcification is not what follows."]]),

 # ---------------- corneal abrasion and foreign body ----------------
 dict(topic="Corneal abrasion", io=IO_A, lead="initial test", cite=D % 18,
  q="Which examination shows the extent of a corneal abrasion?",
  opts=[["Slit lamp with fluorescein", "Correct. Fluorescein stains the exposed basement membrane."],
        ["Tonometry", "Pressure does not map an epithelial defect."],
        ["Gonioscopy", "That examines the drainage angle."],
        ["Dilated fundoscopy", "The abrasion is on the surface."],
        ["Ocular ultrasound", "It does not resolve an epithelial defect."]]),

 dict(topic="Corneal abrasion", io=IO_A, lead="patient education", cite=D % 18,
  q="Which instruction must a patient with a corneal abrasion never be given?",
  opts=[["Take home topical anaesthetic drops for pain", "Correct. They delay healing, mask worsening symptoms and can cause a corneal ulcer."],
        ["Use the topical antibiotic as prescribed", "That is the treatment."],
        ["Return if symptoms worsen", "Re-examination is part of care."],
        ["Consider patching for comfort", "Patching may help the pain."],
        ["Avoid rubbing the eye", "Reasonable advice after an abrasion."]]),

 dict(topic="Corneal foreign body", io=IO_A, lead="next step", cite=D % 21,
  q="A patient who was grinding metal has vertical linear scratches across the cornea. What does that indicate?",
  opts=[["Evert the upper lid to find the object", "Correct. Vertical linear defects mean it is in the tarsal conjunctiva of the upper lid."],
        ["Examine the lower fornix first", "The vertical pattern points to the upper lid."],
        ["Order an orbital radiograph", "The object is on the surface, not in the orbit."],
        ["Refer immediately for surgical exploration", "It can be removed at the slit lamp."],
        ["Patch the eye and review in a week", "The object needs removing now."]]),

 dict(topic="Corneal foreign body", io=IO_A, lead="management", cite=D % 22,
  q="A rust ring remains after a metallic foreign body is removed. How is it dealt with?",
  opts=[["A battery-operated drill with a burr tip", "Correct. That is how a rust ring comes out."],
        ["Repeated irrigation with saline", "Irrigation will not lift a rust ring."],
        ["A cotton-tipped applicator", "That is for conjunctival foreign bodies."],
        ["Leaving it to resorb", "It does not resorb on its own."],
        ["Topical chelating drops", "Not the described method."]]),

 dict(topic="Corneal foreign body", io=IO_A, lead="referral", cite=D % 22,
  q="When does a corneal foreign body need ophthalmology rather than removal at the bedside?",
  opts=[["When it may have passed through the cornea", "Correct. That is an open globe, not a surface foreign body."],
        ["When the patient wears contact lenses", "Lens wear alone does not change who removes it."],
        ["When there is a rust ring", "A rust ring is removed with a burr."],
        ["When it has been present more than a day", "Duration alone is not the trigger."],
        ["When the patient is a child", "Age alone is not the trigger."]]),

 # ---------------- hyphema ----------------
 dict(topic="Hyphema", io=IO_A, lead="diagnosis", cite=D % 24,
  q="A patient struck in the eye has blood layered in the anterior chamber. What is this, and what else must be considered?",
  opts=[["Hyphema, which can itself be a sign of open globe", "Correct. It is not always an isolated injury."],
        ["Hyphema, which excludes an open globe", "It does not exclude one."],
        ["Subconjunctival haemorrhage over the iris", "That sits on the surface, not within the chamber."],
        ["Vitreous haemorrhage seen through the pupil", "That lies behind the lens."],
        ["Corneal blood staining", "That is a late complication rather than this finding."]]),

 dict(topic="Hyphema", io=IO_A, lead="management", cite=D % 25,
  q="What is the aim of hyphema management?",
  opts=[["Preventing a rebleed", "Correct. Every element of the regimen serves that."],
        ["Clearing the blood as fast as possible", "Speed of clearance is not the goal."],
        ["Restoring accommodation", "Not what management targets."],
        ["Preventing infection", "Infection is not the primary concern here."],
        ["Reducing photophobia", "Comfort matters but is not the aim."]]),

 dict(topic="Hyphema", io=IO_A, lead="management", cite=D % 25,
  q="Why is oral aminocaproic acid used in hyphema?",
  opts=[["It slows clot breakdown, reducing the risk of rebleeding", "Correct. It is an antifibrinolytic."],
        ["It lowers the intraocular pressure", "Pressure is treated with other agents."],
        ["It reverses anticoagulation", "It is not a reversal agent."],
        ["It prevents secondary infection", "It has no antimicrobial action."],
        ["It dilates the pupil to rest the ciliary body", "That is the cycloplegic's role."]]),

 dict(topic="Hyphema", io=IO_A, lead="prognosis", cite=D % 25,
  q="Over what period does most rebleeding after hyphema occur?",
  opts=[["The first 72 hours", "Correct. That is when a secondary haemorrhage is most likely."],
        ["The first 24 hours only", "The window is longer than a day."],
        ["Between one and two weeks", "Later than the peak risk."],
        ["After the first month", "Well outside the peak risk."],
        ["Rebleeding is not a recognised complication", "It is the complication management aims to prevent."]]),

 dict(topic="Hyphema", io=IO_A, lead="risk factor", cite=D % 25,
  q="Which condition raises the risk of complications from hyphema?",
  opts=[["Sickle cell disease", "Correct. It is specifically flagged as raising the risk."],
        ["Seasonal allergic rhinitis", "It does not affect the risk."],
        ["Hypothyroidism", "It does not affect the risk."],
        ["Migraine with aura", "It does not affect the risk."],
        ["Iron deficiency anaemia", "It is not the condition that raises the risk."]]),

 dict(topic="Hyphema", io=IO_A, lead="management", cite=D % 25,
  q="Which drugs should be avoided in a patient with hyphema?",
  opts=[["Aspirin and antiplatelet agents", "Correct. They raise the risk of a secondary haemorrhage."],
        ["Antiemetics", "Antiemetics are given, so the patient does not strain."],
        ["Cycloplegic drops", "Cycloplegics are part of the regimen."],
        ["Topical corticosteroids", "Corticosteroids are used."],
        ["Acetazolamide", "It is used if the pressure is high."]]),

 dict(topic="Hyphema", io=IO_A, lead="next step", cite=D % 25,
  q="When is intraocular pressure NOT measured in a patient with hyphema?",
  opts=[["When a penetrating globe injury is suspected", "Correct. Pressing on an open globe risks extruding its contents."],
        ["When the hyphema fills less than half the chamber", "Size does not change whether pressure is measured."],
        ["When the patient is under sixteen", "Age is not the exclusion."],
        ["When the injury was more than a day ago", "Timing is not the exclusion."],
        ["Pressure is measured in every case", "There is one clear exception."]]),
]
