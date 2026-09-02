# -*- coding: utf-8 -*-
"""Lecture 14 rows for the ophthalmology comparison chart.

Ocular Trauma, Prof. Chand Shah, 31 August. Same shape as the earlier modules:
  ROWS_L14  (name, group, giveaway, presentation, testing, treatment,
             urgency, education, slides, deck)
  DIFF_L14  name -> (pain, laterality, key exam abnormality)
  IMGS_L14  name -> (filename, slide)

TWO EXTRACTION TRAPS IN THIS DECK, both of which would have put the wrong
caption on the wrong picture:

  1. THE SPEAKER NOTES DO NOT MAP BY INDEX. All nine notes with text belong to
     a different slide than their notesSlideN number suggests -- notesSlide24
     belongs to SLIDE 42, notesSlide26 to SLIDE 45. Resolve through each
     slide's .rels. Reading them by index puts the orbital-fracture labels on
     the hyphema slide.
  2. THE NOTES LABEL PICTURES BY POSITION, not by letter -- "Upper left",
     "Bottom left 1", "Top middle". Relationship order does not match position,
     so images are extracted in reading order and carry it in the filename
     (l14-sNNN_posK). See tools/extract_cms_e2_l14_images.py.

Slide 45's notes say "Top right: battle sign" TWICE. Both right-hand pictures
were viewed: pos3 and pos6 are each a Battle sign, so the second entry means
BOTTOM right. Not a mis-mapping, just a typo in her notes.

RETINAL DETACHMENT: Lecture 12 already carries a general "Retinal detachment"
row under acute vision loss. That row is the acute presentation of the
rhegmatogenous form. The three TYPES are Lecture 14's own teaching and get
their own rows here, because their management genuinely differs -- surgical,
surgical, and treat-the-underlying-disease.
"""
TRA = "Ocular trauma"
D14 = "CMS I Ocular Trauma"

ROWS_L14 = [
 ("Open globe injury", TRA,
  "<b>Pupil pulled toward a wound</b> &middot; <b>soft eye</b> &middot; massive haemorrhagic chemosis",
  "Full-thickness defect of cornea and/or sclera, so the intraocular compartments are open to the outside. Signs: <b>pupillary distortion toward the wound</b>, <b>flat anterior chamber</b>, extraocular protrusion of uveal tissue, massive haemorrhagic chemosis, <b>soft eye</b>, deep lid laceration, hyphema or vitreous haemorrhage.",
  "<b>CT orbit &mdash; NEVER MRI</b> if a metallic foreign body is possible. <b>Do not dilate the eye.</b> Do not remove a penetrating object.",
  "<b>Rigid protective shield taped over the eye and ophthalmology called immediately.</b> Antiemetics and analgesia so the patient does not strain, plus tetanus. Surgical repair.",
  "Emergent",
  "Anything that raises intraocular pressure &mdash; vomiting, straining, pressing on the eye &mdash; can extrude intraocular contents. That is why the shield is rigid and the antiemetic is not optional.",
  "14", D14),

 ("Full-thickness eye wall laceration", TRA,
  "<b>Sharp object or high-velocity projectile</b> &middot; entry &plusmn; exit wound",
  "Cut clean through cornea, sclera, or both, by a sharp object or high-velocity projectile &mdash; fishing hook, knife. The object may have been withdrawn before arrival, may be retained, or may have passed straight through.",
  "<b>CT orbit.</b> Fundoscopy matters: a cut lens capsule leaves the lens <b>hydrated, oedematous and opaque</b>, and a fragment can extrude into the anterior chamber and inflame it.",
  "Surgical repair. <b>Lensectomy is required but is often deferred</b>, to let hyphema and inflammation settle and to measure accurately for an intraocular lens. <b>Posterior-segment foreign bodies are left alone at first assessment.</b>",
  "Emergent",
  "Leaving a posterior foreign body is deliberate, not an oversight &mdash; going after it early risks more damage than the object itself.",
  "15&ndash;16", D14),

 ("Globe rupture", TRA,
  "<b>Blunt</b> trauma &mdash; airbag, fist, baseball &middot; <b>soft eye</b>",
  "Cornea and/or sclera split at a <b>weak point</b> under severe blunt force. Common sites: <b>posterior to the extraocular muscle insertions</b> (especially the superonasal quadrant), old surgical incisions, and the <b>lamina cribrosa</b>.",
  "Suspect it whenever blunt trauma produces <b>massive haemorrhagic chemosis or a soft eye</b>. CT to look for a foreign body.",
  "Shield, ophthalmology immediately, antiemetics, analgesia, tetanus. <b>Immediate surgical repair</b> with wound exploration.",
  "Emergent",
  "A previous cataract or other intraocular operation leaves a permanent weak point &mdash; those eyes rupture at lower force.",
  "17", D14),

 ("Corneal abrasion", TRA,
  "<b>Fingernail or contact lens</b> &middot; severe <b>foreign body sensation</b>",
  "Scraping away of corneal epithelium. <b>One of the commonest ocular injuries.</b> Severe foreign body sensation, tearing, photophobia, blurred vision.",
  "<b>Slit lamp with fluorescein</b>, which stains the exposed basement membrane and shows the extent.",
  "<b>Topical broad-spectrum antibacterial.</b> Patching may ease pain. Re-examine periodically to confirm healing and exclude infection.",
  "Urgent",
  "<b>NEVER send the patient home with topical anaesthetic drops.</b> They delay healing, mask worsening symptoms, and can cause a corneal ulcer.",
  "18", D14),

 ("Corneal or conjunctival foreign body", TRA,
  "<b>Grinding or striking metal</b> &middot; <b>vertical linear</b> corneal scratches",
  "An object with too little momentum to pass through the eye wall lodges in cornea or conjunctiva. Foreign body sensation, photophobia, excessive tearing. <b>Linear vertical epithelial defects mean the object is under the UPPER LID</b>.",
  "<b>Slit lamp</b> for small objects; diffuse light for larger. <b>Evert the upper lid</b> &mdash; the vertical scratches are the clue to look there.",
  "Topical anaesthetic, then removal with a <b>sterile 27-gauge needle</b>. A <b>rust ring</b> (iron or copper) comes out with a battery-operated burr. Broad-spectrum antibiotic plus abrasion care.",
  "Urgent",
  "Refer if there is any concern the object passed <i>through</i> the cornea &mdash; that is an open globe, not a foreign body.",
  "21&ndash;22", D14),

 ("Hyphema", TRA,
  "<b>Blood layered in the anterior chamber</b> after blunt trauma",
  "Blood in the anterior chamber from injured vessels, after blunt or penetrating trauma. Blurred vision, eye pain, photophobia. <b>Can be a sign of open globe.</b>",
  "Diffuse light for a gross hyphema, slit lamp, full ophthalmic examination. <b>Measure intraocular pressure &mdash; unless penetrating globe injury is suspected.</b>",
  "Goal is preventing a rebleed: <b>bed rest with the head elevated</b>, antiemetics, ocular hypotensives, topical or oral corticosteroids, <b>cycloplegic drops</b>, and <b>oral aminocaproic acid</b> to stop clot breakdown. Treat a raised pressure.",
  "Emergent",
  "<b>Most rebleeding happens in the first 72 hours</b>, and a secondary haemorrhage can cost the vision permanently. Avoid aspirin and antiplatelets; <b>sickle cell disease raises the risk</b>.",
  "24&ndash;25", D14),

 ("Lid laceration", TRA,
  "Cut <b>at the lid margin</b> or within <b>6&ndash;8 mm of the medial canthus</b>",
  "<b>Full-thickness</b> lid lacerations come with a corneal laceration or globe rupture in about <b>two thirds of cases</b>. Partial-thickness ones do not meet the referral criteria.",
  "Examine for globe injury underneath. Determine whether the cut runs <b>through the tarsal plate</b> of the upper lid.",
  "<b>Ophthalmology for any of:</b> lid margin involvement, within 6&ndash;8 mm of the medial canthus, lacrimal duct or sac, inner lid surface, associated ptosis, tarsal plate or levator. Partial-thickness can be repaired in the emergency department with ophthalmology follow-up in 2&ndash;3 days.",
  "Emergent",
  "A missed <b>canalicular</b> injury in the medial third leaves the patient with <b>chronic tearing for life</b>. Facial lacerations may be left open 24 hours before closure because the face is so well vascularised.",
  "26&ndash;27", D14),

 ("Orbital contusion", TRA,
  "Peri-orbital <b>swelling without haemorrhage</b>",
  "Soft tissue swelling inside the orbit <b>without haemorrhage</b>. Preseptal ecchymosis or haematoma &mdash; the tarsal plate and septal margin act as a wall holding blood in the anterior tissues.",
  "Assessment for globe injury; <b>rule out brain trauma</b>.",
  "Supportive, through to surgery depending on the patient's condition.",
  "Urgent",
  "The septum is what keeps this in front of the eye. Swelling that crosses behind it is a different and more dangerous problem.",
  "31", D14),

 ("Periorbital haematoma", TRA,
  "Bleeding <b>within the orbit</b> &middot; not always traumatic",
  "Bleeding inside the bony orbit, around the eye. <b>Not only from accidental trauma</b> &mdash; also orbit and eyelid surgery, peribulbar injections, orbital varices, lymphangiomas and arteriovenous malformations, anticoagulants, sickle cell disease, orbital pseudotumour and idiopathic causes.",
  "Assess vision and intraocular pressure; imaging as the picture demands.",
  "<b>Canthotomy with cantholysis</b> &mdash; releasing the lateral canthal tendon and cutting its inferior branch &mdash; to let the blood drain.",
  "Emergent",
  "Because it is not always traumatic, ask about anticoagulants, recent injections and eye surgery before assuming a blow caused it.",
  "33", D14),

 ("Retinal detachment &mdash; rhegmatogenous", TRA,
  "<b>Curtain</b> descending &middot; <b>flashes and floaters</b> &middot; commonest type",
  "<b>The most common type.</b> One or more full-thickness breaks in the sensory retina let liquefied vitreous pass into the subretinal space. Usually preceded by <b>posterior vitreous detachment</b>. Shadow or curtain over the eye, cloudy or smoky vision, floaters, momentary flashes; monocular field defect, and acuity drops once the macula is involved.",
  "History plus <b>dilated eye examination</b> by ophthalmology.",
  "<b>Surgical.</b> Ophthalmology STAT, pain control, antiemetics, <b>head of bed at 30&ndash;40 degrees</b>.",
  "Emergent",
  "Usually a spontaneous age-related event, but <b>myopia, cataract surgery and ocular trauma</b> all bring it forward. Must be seen within 24 hours.",
  "35&ndash;36", D14),

 ("Retinal detachment &mdash; traction", TRA,
  "<b>Proliferative diabetic retinopathy</b> &middot; <b>concave</b> and localised",
  "Fibrovascular tissue pulls the retina off. <b>Most commonly from proliferative diabetic retinopathy.</b> More localised and <b>concave</b> in shape than a rhegmatogenous detachment; starts along the vasculature then spreads to retina and macula.",
  "Dilated examination; the diabetic history is the context.",
  "<b>Surgical.</b>",
  "Emergent",
  "This is the one that follows from years of uncontrolled diabetes &mdash; the argument for glycaemic control has an endpoint the patient can picture.",
  "39", D14),

 ("Retinal detachment &mdash; exudative", TRA,
  "<b>No break and no traction</b> &middot; systemic disease or a tumour behind it",
  "Fluid collects under the retina with <b>neither a retinal break nor vitreoretinal traction</b>. Associated with systemic vascular or inflammatory disease, or an intraocular tumour.",
  "Dilated examination, then the workup the suspected underlying disease demands.",
  "<b>Treat the underlying condition</b> &mdash; not primarily a surgical problem.",
  "Urgent",
  "The only one of the three where surgery is not the answer. Finding the cause is the treatment.",
  "39", D14),

 ("Orbital floor (blowout) fracture", TRA,
  "<b>Diplopia on UPWARD gaze</b> &middot; <b>infraorbital numbness</b> &middot; fist or ball",
  "Two mechanisms: a true blowout, where a blunt object raises orbital pressure and blows out the <b>floor</b> (commonest) or medial wall; or force on the infraorbital rim buckling the floor. Periorbital ecchymosis, lid oedema, chemosis, subconjunctival haemorrhage, <b>infraorbital numbness</b>, subcutaneous emphysema. <b>Diplopia on upward gaze = inferior rectus entrapment; on lateral gaze = medial rectus.</b>",
  "<b>CT of the orbits and midface.</b>",
  "No injury or entrapment: ice, analgesia, review in 2&ndash;3 days. Blood in the maxillary sinus: antibiotics. True blowout: ophthalmology, because <b>30% have a significant globe injury</b>. <b>Entrapment: facial trauma surgeon STAT</b> &mdash; the muscle can necrose.",
  "Emergent",
  "In children an entrapped muscle may show <b>no soft tissue signs at all &mdash; the &ldquo;white-eyed blowout&rdquo;</b>, with severe pain, bradycardia and vomiting on eye movement. Surgery is often delayed 1&ndash;2 weeks to let swelling settle.",
  "40&ndash;43", D14),

 ("Basilar skull fracture", TRA,
  "<b>Raccoon eyes</b> &middot; <b>Battle sign</b> &middot; clear or pink rhinorrhoea",
  "Linear fracture of the skull base &mdash; cribriform plate, orbital plate of frontal, petrous or squamous temporal, sphenoid or occipital. <b>Often no symptoms directly.</b> Indirect signs: bleeding into soft tissue at the skull base, <b>raccoon eyes</b>, <b>Battle sign</b>, bleeding into middle ear or sphenoid sinus, <b>haemotympanum</b>, and cerebrospinal fluid leak with clear or pink rhinorrhoea.",
  "<b>CT orbits</b> &mdash; though the fracture is not always visible. For suspected cerebrospinal fluid: a <b>dextrose stick may be positive</b>, and fluid on filter paper or a bedsheet shows a <b>halo or double ring sign</b> (inner blood, outer cerebrospinal fluid).",
  "<b>Cerebrospinal fluid leak: neurosurgery consult and admission.</b> Admission otherwise turns on the clinical picture, associated injuries and any brain injury on CT.",
  "Emergent",
  "<b>Antibiotics for a cerebrospinal fluid leak are controversial</b> &mdash; the concern is selecting resistant organisms. The halo sign is a bedside test that needs nothing but a bedsheet.",
  "44, 47", D14),
]

DIFF_L14 = {
 "Open globe injury": ("<b>YES</b>", "Unilateral",
   "<b>Pupil distorted toward the wound</b>; flat anterior chamber; <b>soft eye</b>"),
 "Full-thickness eye wall laceration": ("<b>YES</b>", "Unilateral",
   "Entry &plusmn; exit wound; <b>opaque hydrated lens</b> if the capsule is cut"),
 "Globe rupture": ("<b>YES</b>", "Unilateral",
   "<b>Massive haemorrhagic chemosis</b> with a soft eye after blunt force"),
 "Corneal abrasion": ("<b>YES</b> &mdash; severe foreign body sensation", "Unilateral",
   "<b>Fluorescein uptake</b> over the epithelial defect"),
 "Corneal or conjunctival foreign body": ("<b>YES</b>", "Unilateral",
   "<b>Vertical linear</b> corneal scratches &rarr; object under the upper lid"),
 "Hyphema": ("<b>YES</b>", "Unilateral",
   "<b>Layered blood in the anterior chamber</b>"),
 "Lid laceration": ("<b>YES</b>", "Unilateral",
   "Cut through the <b>lid margin</b> or the <b>tarsal plate</b>"),
 "Orbital contusion": ("<b>YES</b>", "Unilateral",
   "Preseptal ecchymosis or haematoma, <b>no haemorrhage within the orbit</b>"),
 "Periorbital haematoma": ("<b>YES</b>", "Unilateral",
   "Bleeding <b>behind the septum</b>, within the bony orbit"),
 "Retinal detachment &mdash; rhegmatogenous": ("<b>NO</b>", "Unilateral",
   "<b>Curtain</b> with flashes and floaters; retinal break on dilated examination"),
 "Retinal detachment &mdash; traction": ("<b>NO</b>", "Often bilateral disease",
   "<b>Concave, localised</b> detachment with fibrovascular tissue"),
 "Retinal detachment &mdash; exudative": ("<b>NO</b>", "Depends on the cause",
   "Subretinal fluid with <b>no break and no traction</b>"),
 "Orbital floor (blowout) fracture": ("<b>YES</b>", "Unilateral",
   "<b>Diplopia on upward gaze</b> with <b>infraorbital numbness</b>"),
 "Basilar skull fracture": ("Variable", "Often bilateral raccoon eyes",
   "<b>Battle sign</b>, haemotympanum, <b>halo sign</b> on the bedsheet"),
}

# Every one of these was viewed before assignment. The two multi-picture slides
# were resolved by position against the notes' own "Upper left / Right / Top
# middle" labels, and both were confirmed visually.
IMGS_L14 = {
 "Full-thickness eye wall laceration": ("l14-s015_pos1.jpg", 15),
 "Globe rupture": ("l14-s017_pos1.jpg", 17),
 "Corneal abrasion": ("l14-s018_pos1.jpg", 18),
 "Corneal or conjunctival foreign body": ("l14-s021_pos1.jpg", 21),
 "Hyphema": ("l14-s024_pos1.jpg", 24),                     # verified: layered blood
 "Lid laceration": ("l14-s029_pos1.jpg", 29),
 "Orbital contusion": ("l14-s032_pos1.jpg", 32),
 "Periorbital haematoma": ("l14-s034_pos1.jpg", 34),
 "Retinal detachment &mdash; rhegmatogenous": ("l14-s038_pos1.jpg", 38),  # verified: B-scan
 "Orbital floor (blowout) fracture": ("l14-s042_pos2.jpg", 42),  # verified: entrapment, upgaze
 "Basilar skull fracture": ("l14-s045_pos3.jpg", 45),            # verified: Battle sign
}
