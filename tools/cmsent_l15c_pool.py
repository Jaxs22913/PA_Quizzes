# -*- coding: utf-8 -*-
"""Lecture 15, third pool -- External and Middle Ear."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "CMS I Disorders of the External and Middle Ear"
IO = ("Disorders of the external and middle ear: etiologies, epidemiology, risk factors, clinical "
      "manifestations, differential diagnosis, diagnostic testing, management, referrals, patient "
      "education, and prognosis")

QUESTIONS = [

Q("Otitis externa prevention", IO,
  "A 15-year-old competitive swimmer has had three episodes of otitis externa this season and asks "
  "how to prevent recurrence.",
  [["Dry the ears after swimming and avoid cotton buds",
    "Correct. The canal's defences are its acidic pH and its intact skin barrier with a wax coating. "
    "Retained water raises the pH and macerates the skin, while cotton buds strip the protective wax "
    "and abrade the epithelium. Removing both insults addresses the two mechanisms that let "
    "Pseudomonas and Staphylococcus overgrow."],
   ["Use prophylactic antibiotic drops before each swim",
    "Routine antibiotic drops in a healthy canal select for resistant organisms and for fungal "
    "overgrowth, which is how otomycosis develops. The driver here is water and mechanical trauma, "
    "which no drug prevents."],
   ["Clean the canal thoroughly with cotton buds after each swim",
    "This does the opposite of what is needed. Buds push debris deeper, remove the wax that "
    "waterproofs the canal, and create the small abrasions through which bacteria enter."],
   ["Wear earplugs continuously, including out of the water",
    "Plugs during swimming are reasonable, but wearing them continuously traps moisture and warmth "
    "against the canal skin, which recreates the environment the advice is meant to avoid."]],
  "treatment", D, 41),

Q("Acute otitis media", IO,
  "A 5-year-old with acute otitis media has completed high-dose amoxicillin but remains febrile "
  "with a bulging drum after 72 hours.",
  [["Change to amoxicillin-clavulanate",
    "Correct. Failure after 72 hours of adequate first-line therapy suggests a beta-lactamase "
    "producing organism, typically Haemophilus influenzae or Moraxella catarrhalis, which "
    "amoxicillin alone does not cover. Adding clavulanate restores activity against those organisms "
    "without abandoning the pneumococcal coverage that amoxicillin provides."],
   ["Continue the same course for a further week",
    "Continuing a drug that has demonstrably failed over three days simply extends exposure without "
    "addressing why it failed. Seventy-two hours is the accepted point at which lack of response "
    "prompts a change."],
   ["Add topical antibiotic drops",
    "Drops cannot cross an intact tympanic membrane, so they never reach the middle ear where the "
    "infection sits. Adding them gives the appearance of escalation without delivering any drug to "
    "the site."],
   ["Stop antibiotics and observe",
    "Watchful waiting is a strategy for mild disease at the outset, not for a child who is still "
    "febrile with a bulging drum after treatment. Stopping now risks mastoiditis and other "
    "suppurative complications."]],
  "next step", D, 26),

Q("Cholesteatoma", IO,
  "A 44-year-old woman with a known cholesteatoma develops vertigo and a facial droop involving the "
  "forehead on the same side.",
  [["The cholesteatoma is eroding into the labyrinth and facial nerve",
    "Correct. A cholesteatoma expands by shedding keratin with nowhere to go, and the accumulating "
    "mass releases enzymes that erode surrounding bone. The labyrinth and the facial nerve canal lie "
    "immediately adjacent to the middle ear, so erosion produces vertigo and a lower motor neuron "
    "facial palsy that involves the forehead."],
   ["She has developed a separate Bell palsy",
    "Attributing a facial palsy to an idiopathic cause in a patient with a known bone-eroding lesion "
    "adjacent to the facial nerve ignores the obvious mechanism. Bell palsy is a diagnosis of "
    "exclusion."],
   ["The vertigo indicates benign paroxysmal positional vertigo",
    "Positional vertigo lasts seconds and is triggered by head position, with no facial nerve "
    "involvement at all. The simultaneous onset of two adjacent cranial structures failing points to "
    "a local destructive process."],
   ["This represents Ramsay Hunt syndrome",
    "Herpes zoster of the geniculate ganglion does produce facial palsy with vertigo and hearing "
    "loss, so the syndrome is worth knowing, but it is accompanied by vesicles in the canal or "
    "concha and severe pain, and it does not occur in a cholesteatoma cavity by coincidence."]],
  "mechanism", D, 63),

Q("Otitis media complications", IO,
  "A student asks why acute otitis media can progress to mastoiditis but not, for example, to "
  "sinusitis.",
  [["The mastoid air cells communicate directly with the middle ear",
    "Correct. The mastoid antrum opens into the epitympanum through the aditus, so the mastoid air "
    "cells and the middle ear form one continuous mucosa-lined space. Infection therefore extends "
    "into the mastoid by direct continuity, which is why mastoiditis is the classic suppurative "
    "complication of untreated otitis media."],
   ["The eustachian tube drains into the mastoid",
    "The eustachian tube connects the middle ear to the NASOPHARYNX, which is how organisms reach "
    "the middle ear in the first place. It has no connection to the mastoid air cells."],
   ["Infection spreads haematogenously to the mastoid",
    "Bloodborne spread does occur in some infections, but the mastoid is involved by direct "
    "extension through an anatomical connection, which is far more efficient and explains why it is "
    "the commonest complication rather than a rare one."],
   ["The mastoid shares a wall with the paranasal sinuses",
    "The mastoid sits in the temporal bone behind the ear, and the paranasal sinuses are in the "
    "facial skeleton. They are not adjacent and share no wall."]],
  "mechanism", D, 19),

Q("Keloid of the ear", IO,
  "A 22-year-old woman develops a firm, rubbery, progressively enlarging nodule at the site of an "
  "ear piercing six months earlier. It extends beyond the original wound margin.",
  [["Keloid",
    "Correct. A keloid is an overgrowth of collagen in response to skin injury, and the defining "
    "feature is that it extends BEYOND the boundaries of the original wound. Ear piercing is the "
    "classic trigger on the auricle, and the distinction from a hypertrophic scar, which stays within "
    "the wound, matters because keloids recur readily after excision."],
   ["Hypertrophic scar",
    "A hypertrophic scar is also a raised collagen response to injury, so it is the closest mimic, "
    "but it remains confined to the original wound margins and tends to regress over time rather "
    "than continuing to enlarge."],
   ["Epidermoid cyst",
    "An epidermoid cyst is a soft to firm mobile lump containing keratin, often with a visible "
    "punctum, and it is not related to a healing wound margin. It does not grow progressively "
    "outward across normal skin."],
   ["Perichondritis",
    "Perichondritis is an infection of the perichondrium, presenting acutely with a red, hot, "
    "exquisitely tender auricle that spares the lobule. A firm painless nodule six months later is "
    "not an infection."]],
  "diagnosis", D, 69),

Q("Auricular laceration", IO,
  "A 28-year-old man has a laceration of the auricle with exposed cartilage after a fall.",
  [["Prompt repair with coverage of the cartilage, and a pressure dressing",
    "Correct. Exposed auricular cartilage has no blood supply of its own and depends on the "
    "perichondrium, so leaving it uncovered leads to desiccation, infection and chondritis. Prompt "
    "repair restores that coverage, and the pressure dressing prevents a haematoma forming under the "
    "repaired perichondrium."],
   ["Leave the wound open to heal by secondary intention",
    "Secondary intention is acceptable for some wounds elsewhere, but on the ear it leaves cartilage "
    "exposed to drying and bacterial colonisation, which risks losing the cartilage and with it the "
    "shape of the ear."],
   ["Debride and excise the exposed cartilage",
    "Removing cartilage sacrifices the structural framework that gives the auricle its form, and it "
    "is unnecessary when the cartilage is viable. Coverage rather than excision is the aim."],
   ["Repair the skin only and omit the dressing",
    "Closing the skin without a pressure dressing leaves the potential space in which blood can "
    "collect, and a subperichondrial haematoma produces exactly the cauliflower deformity the repair "
    "is meant to prevent."]],
  "treatment", D, 36),

Q("Otitis media with effusion", IO,
  "A 4-year-old has had a bilateral middle ear effusion documented for four months with a "
  "measurable conductive hearing loss. Speech development has slowed.",
  [["Refer for tympanostomy tubes",
    "Correct. The threshold for intervention in a persistent effusion is roughly three months with "
    "documented hearing loss, and this child is beyond it with a functional consequence in speech. "
    "Tubes ventilate the middle ear and restore hearing during the period when language is being "
    "acquired, which is the argument for acting rather than continuing to wait."],
   ["Continue observation for a further three months",
    "Observation is right for the first three months, during which most effusions resolve. "
    "Continuing past four months with hearing loss and slowing speech means waiting through the very "
    "window the intervention exists to protect."],
   ["A course of oral antibiotics",
    "The fluid is sterile at this stage rather than infected, so antibiotics have nothing to treat. "
    "They do not accelerate resolution of a chronic effusion and expose the child to side effects."],
   ["Oral antihistamines and decongestants",
    "Neither has been shown to clear middle ear effusion, and both carry side effects in young "
    "children. Treating a mechanical ventilation problem with these agents does not address the "
    "eustachian tube."]],
  "next step", D, 30),

Q("Eustachian tube dysfunction", IO,
  "A 41-year-old man with allergic rhinitis has recurrent ear fullness and popping. A student asks "
  "why allergy affects the ear.",
  [["Mucosal oedema obstructs the eustachian tube, preventing middle ear ventilation",
    "Correct. The eustachian tube is lined by the same respiratory mucosa as the nose, so allergic "
    "inflammation swells it and closes the lumen. Once the tube cannot open, the trapped middle ear "
    "air is absorbed, pressure falls below atmospheric, the drum retracts and the patient feels "
    "fullness with popping as the tube intermittently opens."],
   ["Allergens reach the middle ear directly and inflame it",
    "The middle ear is a closed space behind an intact drum and is not exposed to inhaled allergen. "
    "The effect is transmitted through the tube's own mucosa rather than by allergen arriving in the "
    "middle ear."],
   ["Histamine damages the cochlear hair cells",
    "Cochlear damage would produce a sensorineural loss, not fullness and popping, and allergic "
    "rhinitis does not cause it. The symptoms described are mechanical and conductive."],
   ["Increased cerumen production blocks the canal",
    "Wax occlusion blocks the canal lateral to the drum and gives steady muffling rather than "
    "popping on swallowing. It is also not driven by allergic inflammation."]],
  "mechanism", D, 22),

Q("Barotrauma prevention", IO,
  "A 34-year-old woman with a heavy cold is due to fly and asks how to reduce the risk of ear pain.",
  [["Use a topical decongestant before descent and swallow or yawn frequently",
    "Correct. The problem is a eustachian tube too swollen to equalise the rising ambient pressure "
    "during descent. A topical decongestant shrinks the mucosa around the tube opening so it can "
    "open, and swallowing, yawning or the Valsalva manoeuvre actively opens it, letting middle ear "
    "pressure track the cabin."],
   ["Wear earplugs throughout the flight",
    "Plugs occlude the canal lateral to the drum, but the pressure differential is between the "
    "middle ear and the cabin, which they do not influence. They may dampen noise but do not help "
    "equalisation."],
   ["Take an oral antihistamine",
    "Antihistamines help when the congestion is allergic, but a viral cold is not histamine-driven, "
    "and their anticholinergic drying can thicken secretions. A decongestant addresses the mucosal "
    "swelling directly."],
   ["Avoid swallowing during descent to prevent pressure changes",
    "This reverses the advice. Swallowing is one of the actions that OPENS the eustachian tube, and "
    "avoiding it guarantees the middle ear cannot equalise."]],
  "treatment", D, 37),

Q("Malignant otitis externa", IO,
  "A 70-year-old man with diabetes is being investigated for suspected necrotising otitis externa.",
  [["Imaging of the temporal bone, because the infection is an osteomyelitis",
    "Correct. Necrotising otitis externa has left the canal skin and entered bone, so it is a skull "
    "base osteomyelitis rather than a soft tissue infection. Imaging defines how far the disease has "
    "spread, which determines the duration of intravenous therapy and identifies cranial nerve "
    "involvement or intracranial extension."],
   ["Canal swab alone to guide topical therapy",
    "A swab is worth taking to identify the organism, which is usually Pseudomonas, but topical "
    "therapy cannot reach infected bone. Treating this as a surface problem is what allows it to "
    "progress."],
   ["Audiometry to quantify the hearing loss",
    "Documenting hearing is reasonable at some point, but it neither establishes the diagnosis nor "
    "changes the immediate management of a bone infection that threatens cranial nerves."],
   ["Tympanometry",
    "Tympanometry assesses middle ear compliance and would add nothing here, because the pathology "
    "is in the canal and the surrounding bone rather than behind the drum."]],
  "testing", D, 43),

Q("Foreign body of the auricle", IO,
  "A 13-year-old girl has an earring back embedded in the soft tissue of the earlobe, with "
  "surrounding erythema and tenderness.",
  [["Remove it, because infection is the main risk",
    "Correct. An embedded earring back is a retained foreign body sitting in soft tissue that has "
    "closed over it, and the described erythema and tenderness show infection is already "
    "established. Removal is both the treatment of the infection's source and the prevention of "
    "spread into the auricular cartilage, where perichondritis can deform the ear."],
   ["Leave it in situ and treat with oral antibiotics",
    "Antibiotics may be needed alongside removal, but leaving the foreign body in place means the "
    "nidus of infection remains and the infection recurs as soon as treatment stops."],
   ["Apply topical steroid to reduce the inflammation",
    "Steroid reduces inflammation but suppresses the local response to an established infection "
    "while the foreign body remains. That combination allows the infection to progress with fewer "
    "outward signs."],
   ["Refer routinely to a plastic surgeon",
    "Specialist referral may be needed for a deeply embedded object or a complicated lobule, but "
    "routine timing does not match an actively infected retained foreign body that can be dealt with "
    "promptly."]],
  "next step", D, 48),

Q("Tympanic membrane perforation", IO,
  "A 52-year-old man has had a dry central perforation for eight months following an infection. His "
  "hearing is reduced and he cannot swim.",
  [["Refer for consideration of tympanoplasty",
    "Correct. Most traumatic and post-infective perforations close within weeks to a few months. One "
    "that remains open at eight months with a persistent conductive loss and lifestyle restriction "
    "is unlikely to heal spontaneously, and surgical repair both restores hearing and closes the "
    "route by which water reaches the middle ear."],
   ["Continue to keep the ear dry and review in a further year",
    "Continuing to wait past eight months adds little, because the spontaneous healing window has "
    "largely passed. It also extends the period during which he cannot swim and hears poorly."],
   ["Prescribe topical antibiotic drops",
    "Drops treat an actively discharging ear. This perforation is dry, so there is no infection to "
    "treat, and prolonged use of drops through a perforation carries its own risks."],
   ["Reassure that hearing will return once the ear is fully healed",
    "The ear has not healed and shows no sign of doing so. Promising recovery that is not coming "
    "delays a referral that would actually restore his hearing."]],
  "next step", D, 61),

Q("Otitis externa versus otitis media", IO,
  "A clinician is teaching the single most useful bedside manoeuvre for distinguishing otitis "
  "externa from acute otitis media.",
  [["Move the tragus or pinna and see whether it hurts",
    "Correct. Pain on manipulating the pinna or tragus localises the disease to the canal, because "
    "moving those structures moves the inflamed canal skin. Middle ear infection sits behind an "
    "intact drum and is unaffected by moving the external ear, so the manoeuvre separates the two "
    "before the otoscope is even used."],
   ["Check for fever",
    "Fever is commoner in acute otitis media, particularly in children, but it is neither sensitive "
    "nor specific: an inflamed canal can raise the temperature and a mild middle ear infection may "
    "not. It does not localise the disease anatomically."],
   ["Perform a Weber test",
    "Both conditions produce a conductive loss, so Weber would lateralise to the affected ear in "
    "either case. It confirms the type of loss without saying where along the conducting pathway the "
    "problem lies."],
   ["Look for discharge in the canal",
    "Discharge occurs in otitis externa and also in otitis media once the drum perforates, so its "
    "presence does not distinguish them. It is the tenderness on movement that localises."]],
  "finding", D, 40),
]
