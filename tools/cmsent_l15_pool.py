# -*- coding: utf-8 -*-
"""Lecture 15 questions for the ENT master exams -- External and Middle Ear.

Vignette style and depth per _cmsent_style.py. Four options, and every option
carries a reason rather than a dismissal.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "CMS I Disorders of the External and Middle Ear"
IO = ("Disorders of the external and middle ear: etiologies, epidemiology, risk factors, clinical "
      "manifestations, differential diagnosis, diagnostic testing, management, referrals, patient "
      "education, and prognosis")

QUESTIONS = [

Q("Otitis externa", IO,
  "An 8-year-old boy has left ear pain. His father says he has been swimming almost daily in a "
  "neighbour's pool this summer. Examination shows erythema and oedema of the left ear canal and "
  "pain on manipulation of the pinna. The tympanic membrane is not well visualised but appears "
  "intact, and the right ear is normal.",
  [["Topical ciprofloxacin with dexamethasone",
    "Correct. Pain on moving the pinna or tragus localises the disease to the CANAL, not the middle "
    "ear, and water exposure macerates the canal skin and raises its pH so that Pseudomonas and "
    "Staphylococcus overgrow. Treatment therefore has to reach the canal surface: a topical "
    "fluoroquinolone covers those organisms, and the added steroid shrinks the oedema so the drops "
    "can actually get past it."],
   ["Oral amoxicillin suspension",
    "Amoxicillin is the drug for acute otitis MEDIA, where the infection sits behind an intact drum "
    "and can only be reached through the bloodstream. Here the infected surface is the canal itself, "
    "which a systemic drug reaches poorly, and amoxicillin has no useful activity against "
    "Pseudomonas, the organism swimming selects for."],
   ["Topical clotrimazole 1%",
    "Clotrimazole treats otomycosis, which typically follows prolonged antibiotic drops or occurs in "
    "immunocompromised patients, and characteristically shows visible fungal debris in the canal. "
    "Nothing in this history or examination points to fungus, and starting an antifungal leaves the "
    "bacterial infection untreated."],
   ["Topical triamcinolone 0.1%",
    "A steroid alone reduces the swelling and the pain but does nothing to the organisms driving the "
    "infection. Used by itself in an infected canal it can allow the infection to progress while the "
    "patient feels temporarily better, which is precisely the wrong trade in an ear that is already "
    "occluded by oedema."]],
  "treatment", D, 40),

Q("Otitis externa", IO,
  "A 62-year-old man with poorly controlled type 2 diabetes has had left ear pain and discharge for "
  "three weeks despite two courses of topical drops. The pain is now severe, worse at night, and "
  "there is granulation tissue at the bony-cartilaginous junction of the canal.",
  [["Malignant (necrotising) otitis externa",
    "Correct. Diabetes and immunocompromise are the setting, and the combination of pain out of "
    "proportion, failure of topical therapy, and granulation tissue at the bony-cartilaginous "
    "junction is the classic description. The infection has left the skin and entered bone as a "
    "skull base osteomyelitis, usually Pseudomonas, which is why it needs systemic therapy and "
    "imaging rather than more drops."],
   ["Simple bacterial otitis externa",
    "Ordinary otitis externa responds to topical therapy within days and does not produce granulation "
    "tissue or night pain of this severity. Two failed courses of drops in a diabetic patient is "
    "exactly the point at which the diagnosis has to be revised rather than the prescription "
    "repeated."],
   ["Otomycosis",
    "Fungal infection of the canal does follow repeated antibiotic drops, which fits part of this "
    "history, but it produces visible hyphae or a wet-newspaper debris rather than granulation "
    "tissue, and it does not cause deep boring night pain or threaten the skull base."],
   ["Cholesteatoma",
    "A cholesteatoma is a keratin sac behind or through a retracted drum, producing chronic painless "
    "foul discharge and conductive loss. It sits in the middle ear rather than the canal wall, and "
    "it does not present with severe pain and canal granulation in this way."]],
  "diagnosis", D, 43),

Q("Otitis media", IO,
  "A 25-year-old patient has acute otitis media with a serous effusion in the right ear. Audiometry "
  "confirms a marked conductive impairment on that side. Weber and Rinne tests are performed.",
  [["Weber lateralises to the right; bone conduction exceeds air conduction on the right",
    "Correct. Fluid in the middle ear blocks air conduction but leaves the cochlea and the skull's "
    "own transmission untouched. Weber therefore lateralises TOWARD the affected ear, because the "
    "blocked ear is not competing with ambient room noise and hears the bone-conducted tone better. "
    "In the same ear Rinne reverses: bone now beats air, which never happens in a normal or "
    "sensorineural ear."],
   ["Weber lateralises to the left; bone conduction exceeds air conduction on the right",
    "The Rinne half is right but the Weber half is backwards. Lateralising AWAY from the affected "
    "ear is the sensorineural pattern, where the damaged cochlea cannot process the tone from either "
    "route. Pairing an away-lateralising Weber with a reversed Rinne describes two different kinds of "
    "loss in the same ear."],
   ["Weber is equal in both ears; bone conduction exceeds air conduction on the right",
    "An equal Weber means the two ears are transmitting bone-conducted sound equally, which is the "
    "normal result. That cannot coexist with the marked unilateral conductive impairment the "
    "audiogram has already documented."],
   ["Weber lateralises to the right; air conduction exceeds bone conduction on the right",
    "Air beating bone is the NORMAL Rinne, and it is also what a sensorineural ear gives. Reporting "
    "it in an ear with a marked conductive deficit contradicts the audiogram, and it is the reason "
    "Weber has to be interpreted alongside Rinne rather than on its own."]],
  "finding", D, 19),

Q("Otosclerosis", IO,
  "A 30-year-old man is admitted for stapedectomy to treat otosclerosis. He has had progressive "
  "hearing loss in the right ear over several years. His mother had the same condition in her "
  "forties and had a successful operation. Weber and Rinne testing is performed before surgery.",
  [["Bone conduction exceeds air conduction on the affected side",
    "Correct. Otosclerosis lays down abnormal bone that fixes the stapes footplate in the oval "
    "window, so the ossicular chain can no longer drive the cochlear fluid. The cochlea itself is "
    "normal, so bone-conducted sound still reaches it perfectly well while air-conducted sound is "
    "blocked at the footplate. That is the definition of a conductive loss, and a reversed Rinne is "
    "how it is demonstrated."],
   ["Air conduction exceeds bone conduction on the affected side",
    "This is the normal Rinne, and it is also the result a sensorineural ear gives, which is why "
    "Rinne alone cannot separate those two. Reporting it here would mean the ossicular chain is "
    "conducting normally, which is inconsistent with a fixed stapes footplate and years of "
    "progressive loss."],
   ["Bone conduction equals air conduction on the affected side",
    "Equal bone and air is the borderline result seen as a mild conductive loss is just developing, "
    "not the established picture in someone with years of progressive loss severe enough to warrant "
    "an operation. It also fails to demonstrate the conductive pattern the surgery is being done to "
    "correct."],
   ["Sound lateralises to the unaffected ear on Weber testing",
    "Lateralising away from the affected ear is the sensorineural pattern. In conductive loss Weber "
    "goes TOWARD the bad ear, because that ear is shielded from ambient noise and receives the "
    "bone-conducted tone more clearly. Otosclerosis is conductive until the disease reaches the "
    "cochlea."]],
  "finding", D, 65),

Q("Cholesteatoma", IO,
  "A 37-year-old man reports constant fullness in the left ear and three months of declining "
  "hearing on that side. He had multiple middle ear infections as a child and four separate "
  "myringotomy tube placements, and he has untreated perennial airborne allergies. Weber "
  "lateralises to the left. Otoscopy shows a retracted tympanic membrane with a sac of cheesy "
  "white material, and the same debris is visible behind a small suspected perforation.",
  [["Cholesteatoma",
    "Correct. Repeated middle ear infection, tube placements and eustachian tube dysfunction from "
    "untreated allergy all produce chronic negative middle ear pressure, which retracts the drum "
    "into a pocket. Squamous epithelium trapped in that pocket keeps shedding keratin with nowhere "
    "to go, producing the cheesy white sac described. Weber lateralising to the affected ear "
    "confirms the loss is conductive, from the mass and ossicular erosion."],
   ["Barotrauma",
    "Barotrauma follows a discrete pressure event such as flying or diving, and produces acute pain, "
    "haemorrhage into the drum or a middle ear effusion. It does not build a keratin sac, and it "
    "does not cause three months of progressive loss in someone with no recent pressure exposure."],
   ["Exostoses",
    "Exostoses are bony overgrowths of the ear canal from repeated cold water exposure, sometimes "
    "called surfer's ear. They sit lateral to the drum, are hard rather than cheesy, and cause loss "
    "only when they occlude the canal or trap debris. Nothing here suggests cold water exposure."],
   ["External otitis",
    "Otitis externa inflames the canal skin, giving pain on moving the pinna and canal oedema. It "
    "does not retract the drum, does not produce keratin debris behind a perforation, and its "
    "hearing effect is from canal swelling rather than three months of progressive decline."]],
  "diagnosis", D, 63),

Q("Tympanic membrane perforation", IO,
  "A 30-year-old woman is struck on the side of the head with an open hand. She has immediate ear "
  "pain, a brief episode of bleeding from the canal, and reduced hearing. Otoscopy shows a small "
  "central perforation with clean edges. There is no vertigo and the facial nerve is intact.",
  [["Keep the ear dry and review, since most perforations heal spontaneously",
    "Correct. A small traumatic perforation with clean edges and no vertigo or facial nerve deficit "
    "implies the ossicular chain and inner ear are intact. The drum has good spontaneous healing "
    "capacity, so the treatment is to protect it: keep water out so bacteria do not reach the middle "
    "ear through the hole, and allow it to close on its own."],
   ["Irrigate the canal to remove blood clot",
    "Irrigating an ear with a known perforation drives water and any canal organisms directly into "
    "the middle ear, which is how a clean traumatic perforation becomes a suppurative otitis media. "
    "Keeping the ear dry is precisely the opposite instruction, and it is the central piece of "
    "advice for this injury."],
   ["Start oral antibiotics for all traumatic perforations",
    "Antibiotics are not routine for a clean dry traumatic perforation, because there is no "
    "established infection to treat. They are reserved for contaminated injuries or when discharge "
    "develops, and using them reflexively exposes the patient to side effects without changing the "
    "healing rate."],
   ["Refer for immediate tympanoplasty",
    "Surgical repair is considered for perforations that fail to heal over months, or where hearing "
    "remains impaired after healing. Operating immediately on a fresh small perforation that would "
    "very likely close by itself commits the patient to an unnecessary procedure."]],
  "treatment", D, 61),

Q("Acute otitis media", IO,
  "A 3-year-old girl has had two days of fever and left ear pain following a cold. Otoscopy shows a "
  "bulging, opaque tympanic membrane with reduced mobility on pneumatic otoscopy. She has had no "
  "previous ear infections and no drug allergies.",
  [["High-dose oral amoxicillin",
    "Correct. A bulging drum with reduced mobility and acute fever indicates pus under pressure in "
    "the middle ear, which is bacterial acute otitis media rather than a simple effusion. "
    "Streptococcus pneumoniae, Haemophilus influenzae and Moraxella catarrhalis are the organisms, "
    "and high-dose amoxicillin is first line in a child with no recent antibiotic exposure and no "
    "penicillin allergy."],
   ["Topical ciprofloxacin drops",
    "Drops cannot cross an intact tympanic membrane, so they never reach the middle ear where this "
    "infection sits. Topical therapy is the answer for canal disease such as otitis externa, or "
    "when there is a perforation or tube providing a route in."],
   ["Oral azithromycin",
    "A macrolide is a fallback for a genuine severe penicillin allergy, and it has weaker activity "
    "against the pneumococcus that causes the most painful and most complicated cases. Choosing it "
    "for a child with no allergy trades away efficacy for no benefit."],
   ["Reassurance and analgesia alone, with no antibiotic",
    "Watchful waiting is a reasonable strategy for older children with mild disease and reliable "
    "follow-up, but a bulging drum with fever in a 3-year-old is the presentation most likely to "
    "benefit from treatment and most at risk of complications such as mastoiditis."]],
  "treatment", D, 26),

Q("Mastoiditis", IO,
  "A 4-year-old boy has had acute otitis media for a week. He now has fever, tenderness over the "
  "mastoid process, and the left auricle is displaced downward and outward. There is swelling and "
  "erythema behind the ear.",
  [["Acute mastoiditis",
    "Correct. The mastoid air cells connect directly with the middle ear, so untreated or "
    "inadequately treated otitis media can extend into them. Postauricular erythema, swelling and "
    "tenderness with an auricle pushed down and out is the described picture, and it means the "
    "infection has moved from a mucosal space into bone, which is why it needs admission and "
    "intravenous therapy."],
   ["Otitis externa with periauricular cellulitis",
    "Canal infection produces pain on moving the pinna and canal oedema, and any surrounding "
    "cellulitis follows the canal skin rather than pushing the auricle forward from behind. It also "
    "would not follow a week of established middle ear infection in this way."],
   ["Preauricular lymphadenitis",
    "An inflamed preauricular node sits IN FRONT of the ear and does not displace the auricle "
    "outward. The location described here is postauricular and over the mastoid process itself, "
    "which points to the bone rather than to a node."],
   ["Parotitis",
    "Parotid swelling lifts the earlobe and is centred over the angle of the jaw in front of and "
    "below the ear. It is associated with pain on chewing and sometimes pus at Stensen duct, not "
    "with a week of otitis media and postauricular tenderness."]],
  "diagnosis", D, 19),

Q("Eustachian tube dysfunction", IO,
  "A 29-year-old woman has had a blocked, full sensation in both ears since a head cold two weeks "
  "ago, with mild hearing reduction and a popping sensation on swallowing. Otoscopy shows retracted "
  "tympanic membranes. Tympanometry is performed.",
  [["A type C tympanogram, with the peak shifted to negative pressure",
    "Correct. A eustachian tube that cannot ventilate the middle ear allows the trapped air to be "
    "absorbed, so middle ear pressure falls below atmospheric and the drum retracts. Tympanometry "
    "measures compliance across a pressure sweep, and the peak compliance shifts to wherever middle "
    "ear pressure actually is: negative, which is the definition of a type C trace."],
   ["A type B tympanogram, flat across the sweep",
    "A flat trace means the drum does not move at any applied pressure, which happens when the "
    "middle ear is full of fluid or when there is a perforation. This patient has a retracted but "
    "mobile drum with popping on swallowing, so there is still air and still movement."],
   ["A type As tympanogram, with reduced peak compliance",
    "A shallow peak at normal pressure indicates a stiff system, from ossicular fixation such as "
    "otosclerosis or from tympanosclerosis. That is a problem of the conducting mechanism rather "
    "than of ventilation, and it would not produce retraction and popping after a cold."],
   ["A type Ad tympanogram, with excessively deep compliance",
    "An abnormally deep peak means the system is too floppy, from ossicular discontinuity or a "
    "monomeric drum. That is the opposite mechanical problem to a retracted drum under negative "
    "pressure."]],
  "testing", D, 22),

Q("Otitis media with effusion", IO,
  "A 6-year-old girl had acute otitis media six weeks ago, treated with antibiotics. Her fever and "
  "pain resolved but her parents report she still turns the television up loudly. Otoscopy shows an "
  "amber, non-bulging tympanic membrane with an air-fluid level and reduced mobility. She is "
  "afebrile and not in pain.",
  [["Observation, because most effusions resolve without treatment",
    "Correct. Once the acute infection has been treated the sterile fluid often takes weeks to "
    "months to clear as the eustachian tube recovers. An amber non-bulging drum in an afebrile, "
    "painless child is a resolving effusion rather than persistent infection, so the appropriate "
    "action is to document the hearing and let it clear, reserving intervention for persistence or "
    "developmental concern."],
   ["A further course of oral antibiotics",
    "Repeat antibiotics treat an infection that is no longer present. The child is afebrile and "
    "painless, and the drum is not bulging, so what remains is sterile fluid rather than pus. "
    "Additional courses expose her to side effects and resistance without speeding resolution."],
   ["Immediate myringotomy with tube placement",
    "Tubes are considered for effusions that persist beyond about three months with documented "
    "hearing loss, or for recurrent acute infections. At six weeks with a first episode, proceeding "
    "straight to surgery skips the interval in which most effusions resolve on their own."],
   ["Oral corticosteroids",
    "Steroids have not been shown to give lasting benefit for middle ear effusion, and they carry "
    "real systemic effects in a child. Treating a self-limiting mechanical problem with a systemic "
    "anti-inflammatory is disproportionate to the problem."]],
  "treatment", D, 30),

Q("Foreign body in the ear", IO,
  "A 4-year-old boy is brought in after putting a small plastic bead in his right ear canal. He is "
  "cooperative, the bead is smooth, round and visible in the outer third of the canal, and the "
  "tympanic membrane beyond it appears intact.",
  [["Removal under direct vision with an instrument passed beyond the object",
    "Correct. A smooth round object cannot be grasped by forceps because they simply push it deeper, "
    "so the technique is to pass a hook or curette past it under direct vision and draw it outward. "
    "Direct visualisation matters because the risk of the procedure is pushing the object against or "
    "through the drum."],
   ["Irrigation of the canal with warm water",
    "Irrigation is a reasonable technique for some objects but is contraindicated when the object may "
    "swell, such as organic material, and carries the risk of driving water into the middle ear if "
    "the drum is perforated. It also gives no control over which direction a smooth bead moves."],
   ["Grasping the bead with alligator forceps",
    "Forceps work well on irregular or compressible objects that can be gripped, but on a smooth "
    "sphere the jaws slide off and the force is transmitted inward, advancing the bead toward the "
    "tympanic membrane and making removal harder and more dangerous."],
   ["Referral for removal under general anaesthesia as the first step",
    "General anaesthesia is reserved for an uncooperative child, a deeply impacted object, or a "
    "failed first attempt. This boy is cooperative and the object is in the outer third, so a "
    "controlled attempt in clinic is appropriate before committing him to theatre."]],
  "next step", D, 47),
]
