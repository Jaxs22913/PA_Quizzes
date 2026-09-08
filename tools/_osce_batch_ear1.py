# -*- coding: utf-8 -*-
from _pd2_ent_osce_data import E
BATCH = {

"Eustachian tube dysfunction": E(
  "&ldquo;My ear feels blocked since my cold, and it crackles when I swallow.&rdquo;",
  "Otoscopy for a <b>retracted drum</b>, then <b>pneumatic otoscopy</b> &mdash; reduced mobility on "
  "insufflation is the finding. Check the nose for the cause. Weber and Rinne to prove any loss is "
  "conductive.",
  [("Otitis media with effusion", "Amber fluid or a visible level behind the drum, not just retraction"),
   ("Cerumen impaction", "Wax occludes the canal; the drum cannot be seen at all"),
   ("Acute otitis media", "Bulging, red and painful rather than retracted and merely full")],
  "<b>Pneumatic otoscopy</b> &rarr; a retracted drum that moves poorly or not at all. "
  "<b>Tympanometry</b> &rarr; a type C tracing, the peak shifted to negative middle ear pressure.",
  "A type A tympanogram excludes it. Clearing wax and finding a normal mobile drum excludes both "
  "wax and effusion; a bulging red drum redirects to acute otitis media."),

"Acute otitis media": E(
  "&ldquo;My ear has been throbbing since last night and I feel feverish.&rdquo; A toddler tugs at "
  "the ear and will not settle.",
  "Otoscopy for a <b>bulging, erythematous drum with loss of the light reflex and landmarks</b>. "
  "<b>Pneumatic otoscopy</b> &mdash; immobility is the single most useful sign. Palpate the mastoid "
  "for tenderness. Tuning forks.",
  [("Otitis media with effusion", "Fluid WITHOUT pain, fever or bulging &mdash; the distinction that decides antibiotics"),
   ("Otitis externa", "Pain on tragal traction with a swollen canal; the drum is normal if seen"),
   ("Mastoiditis", "Postauricular tenderness with a protruding auricle &mdash; the complication to exclude")],
  "<b>Pneumatic otoscopy</b> &rarr; a bulging immobile drum. <b>Tympanometry</b> &rarr; a flat type "
  "B tracing with normal canal volume. Diagnosis is clinical; no imaging is needed.",
  "A mobile, non-bulging drum excludes it; a normal drum with tragal tenderness redirects to otitis "
  "externa; a normal postauricular area excludes mastoiditis."),

"Otitis media with effusion": E(
  "&ldquo;My hearing is muffled and my ear feels full &mdash; but it doesn&rsquo;t hurt.&rdquo; In "
  "a child, &ldquo;he keeps turning the television up.&rdquo;",
  "Otoscopy for an <b>amber or dull drum, an air-fluid level or bubbles</b>. Pneumatic otoscopy. "
  "<b>Weber lateralises TOWARD the affected ear and Rinne becomes negative</b> on that side &mdash; "
  "the conductive pattern. In an adult with a unilateral effusion, <b>examine the nasopharynx</b>.",
  [("Eustachian tube dysfunction", "Retraction without fluid; the earlier point on the same spectrum"),
   ("Acute otitis media", "Pain, fever and bulging, which this lacks"),
   ("Nasopharyngeal carcinoma", "The reason a unilateral adult effusion is never dismissed")],
  "<b>Tympanometry</b> &rarr; a flat type B curve with NORMAL canal volume (a large volume would "
  "mean a perforation instead). <b>Audiometry</b> &rarr; a conductive loss, typically 20 to 30 decibels.",
  "A type A tympanogram excludes it; fever with a bulging drum redirects to acute otitis media; "
  "nasopharyngoscopy excludes a tumour in the unilateral adult case."),

"Chronic otitis media": E(
  "&ldquo;My ear has been draining on and off for years and the hearing on that side is poor.&rdquo;",
  "Otoscopy for a <b>perforation and discharge</b>; note whether the perforation is central or "
  "marginal. Look for <b>keratin debris or a retraction pocket</b>, which would mean cholesteatoma. "
  "Tuning forks. Facial nerve examination.",
  [("Cholesteatoma", "A marginal or attic perforation with white keratin debris and a foul smell"),
   ("Chronic otitis externa", "Canal is inflamed but the drum is intact"),
   ("Ear canal carcinoma", "Friable and bleeding rather than simply discharging")],
  "<b>Otoscopy</b> &rarr; a persistent perforation with drainage. <b>Audiometry</b> &rarr; a "
  "conductive loss. <b>Culture of the discharge</b> &rarr; the organism guiding topical therapy. "
  "<b>Computed tomography of the temporal bone</b> &rarr; ossicular erosion or a soft tissue mass.",
  "An intact drum excludes it; absent keratin and a central perforation argue against cholesteatoma; "
  "biopsy excludes carcinoma if tissue is friable."),

"Mastoiditis": E(
  "&ldquo;My ear infection got better and then came back, and now behind my ear is swollen and "
  "sore.&rdquo;",
  "Inspect from BEHIND and ABOVE for the <b>auricle pushed forward and outward</b>. <b>Palpate the "
  "mastoid for tenderness, swelling and fluctuance.</b> Otoscopy. <b>Cranial nerve VII</b> and signs "
  "of meningism, since spread is the danger.",
  [("Acute otitis media", "Ear pain without postauricular swelling or auricular protrusion"),
   ("Postauricular lymphadenitis", "A discrete mobile node; the auricle is not displaced"),
   ("Severe otitis externa", "Tragal tenderness with a swollen canal, no mastoid air cell involvement")],
  "<b>Contrast computed tomography of the temporal bone</b> &rarr; opacified mastoid air cells with "
  "<b>coalescence &mdash; loss of the bony septa</b>, which is what separates true mastoiditis from "
  "the incidental fluid seen in ordinary otitis media. Raised white cell count and inflammatory markers.",
  "Fluid in the air cells with INTACT septa is not mastoiditis; a mobile tender node with a normal "
  "scan is adenitis; normal imaging excludes intracranial extension."),

"Barotrauma": E(
  "&ldquo;My ear has been blocked and painful since the flight landed.&rdquo;",
  "Otoscopy for a <b>retracted drum, haemorrhage within the drum, or fluid</b>. Check the drum is "
  "intact. Tuning forks. Ask about diving depth and about vertigo, which suggests inner ear "
  "involvement.",
  [("Eustachian tube dysfunction", "Same mechanism without the acute pressure event or haemorrhage"),
   ("Perilymphatic fistula", "Vertigo and sensorineural loss after the same barotrauma &mdash; far more serious"),
   ("Acute otitis media", "Fever and a bulging drum with an infective prodrome")],
  "<b>Otoscopy</b> &rarr; retraction, a haemotympanum, or a traumatic perforation. "
  "<b>Audiometry</b> &rarr; a conductive loss; a SENSORINEURAL loss instead points to a fistula.",
  "A sensorineural pattern on audiometry excludes simple barotrauma; a normal mobile drum excludes "
  "it; fever with bulging redirects to infection."),

"Cerumen impaction": E(
  "&ldquo;My hearing went suddenly on that side &mdash; it started after I used a cotton bud.&rdquo;",
  "Otoscopy showing <b>wax occluding the canal</b>. <b>Weber lateralises TOWARD the blocked ear, "
  "Rinne is negative on that side</b>. Re-examine the drum AFTER removal &mdash; that is the step "
  "people skip.",
  [("Otitis externa", "Pain on tragal traction; the canal is oedematous rather than merely full of wax"),
   ("Otitis media with effusion", "A conductive loss with a clear canal and fluid behind the drum"),
   ("Sudden sensorineural hearing loss", "Weber would lateralise AWAY &mdash; the reason tuning forks matter")],
  "<b>Otoscopy</b> &rarr; obstructing cerumen, and normal hearing once it is removed. That "
  "resolution IS the confirmation.",
  "If hearing does not return after clearance, the wax was not the cause &mdash; audiometry then, "
  "and Weber lateralising away means a sensorineural cause."),

"Cholesteatoma": E(
  "&ldquo;There is a foul smell from my ear, it keeps draining, and my hearing is getting "
  "worse.&rdquo;",
  "Otoscopy for a <b>retraction pocket in the attic or pars flaccida with white keratin debris</b> "
  "and granulation. <b>Cranial nerve VII.</b> <b>Fistula test</b> &mdash; pressure on the tragus "
  "producing vertigo or nystagmus suggests erosion into the labyrinth. Tuning forks.",
  [("Chronic suppurative otitis media", "A central perforation with discharge but no keratin or bone erosion"),
   ("Chronic otitis externa", "The canal is the problem; the drum is intact"),
   ("Ear canal carcinoma", "Friable and bleeding, with pain out of proportion")],
  "<b>Otoscopy</b> &rarr; keratin debris in a retraction pocket. <b>Computed tomography of the "
  "temporal bone</b> &rarr; a soft tissue mass with <b>bony erosion of the scutum or ossicles</b> "
  "&mdash; the erosion is what makes it a cholesteatoma rather than debris.",
  "No bone erosion on computed tomography with a central perforation means chronic otitis media "
  "instead; a positive fistula test raises labyrinthine erosion and changes urgency."),

"Hematoma of the external ear": E(
  "&ldquo;I got hit in the ear wrestling and it&rsquo;s swollen up.&rdquo;",
  "Inspect for <b>loss of the normal cartilaginous contours</b>. <b>Palpate for fluctuance.</b> "
  "Check the canal and drum are intact. Look for other head injury.",
  [("Perichondritis", "Infected, hot, exquisitely tender, and it spares the lobule"),
   ("Simple contusion", "Bruising WITHOUT a fluctuant collection lifting the perichondrium"),
   ("Relapsing polychondritis", "Recurrent, bilateral, non-traumatic, also sparing the lobule")],
  "<b>Clinical</b> &rarr; a fluctuant swelling obscuring the contours; <b>aspiration or incision</b> "
  "&rarr; blood, which both confirms and treats.",
  "No fluctuance means contusion, not haematoma; hot, spreading erythema means perichondritis and "
  "needs antibiotics; bilateral non-traumatic disease suggests polychondritis."),

"Lacerations and avulsion": E(
  "&ldquo;I caught my ear and it&rsquo;s torn open and bleeding &mdash; will it heal "
  "straight?&rdquo; The cosmetic worry is usually as prominent as the pain.",
  "Assess the wound for <b>cartilage exposure</b>. Examine the canal and drum. Check facial nerve "
  "function and look for other injuries. Tetanus status.",
  [("Simple skin laceration", "Cartilage NOT exposed; a far simpler repair"),
   ("Auricular haematoma", "Closed injury with fluctuance rather than a break in the skin"),
   ("Avulsion with vascular compromise", "A pale, cold segment needing specialist salvage")],
  "<b>Direct inspection</b> &rarr; whether cartilage is exposed and whether the segment is perfused, "
  "which determines who repairs it.",
  "Intact perfusion with skin-only injury excludes the complex repairs; an intact drum excludes "
  "middle ear injury."),

"Tympanic membrane perforation": E(
  "&ldquo;Something popped in my ear and now there&rsquo;s a bit of blood and my hearing is "
  "down.&rdquo;",
  "Otoscopy to <b>size and site the perforation</b>. <b>Weber toward the affected ear</b> with a "
  "negative Rinne. <b>Keep the ear dry &mdash; do not irrigate.</b> Look for vertigo, which would "
  "suggest inner ear injury.",
  [("Otitis media with effusion", "Fluid behind an INTACT drum; tympanometry separates them"),
   ("Cholesteatoma", "A marginal perforation with keratin debris rather than a clean tear"),
   ("Perilymphatic fistula", "Vertigo and sensorineural loss after the same event")],
  "<b>Otoscopy</b> &rarr; a visible defect. <b>Tympanometry</b> &rarr; a flat trace with a "
  "<b>LARGE canal volume</b>, which is what distinguishes a perforation from an effusion. "
  "<b>Audiometry</b> &rarr; a conductive loss proportional to the size of the hole.",
  "A normal canal volume on tympanometry means an intact drum with effusion; a sensorineural loss "
  "or vertigo redirects to inner ear injury."),

"Foreign body of the canal": E(
  "&ldquo;There&rsquo;s something in my ear&rdquo; &mdash; or a parent noticed a child pushing "
  "something in. An insect gives &ldquo;I can hear it moving.&rdquo;",
  "Otoscopy to <b>identify the object and see past it to the drum</b>. Note whether it is "
  "<b>organic (must not be irrigated, it swells)</b> or a <b>button battery (immediate removal)</b>. "
  "Re-examine the canal and drum after removal.",
  [("Cerumen impaction", "Wax rather than an object; irrigation is safe"),
   ("Otitis externa", "Diffuse canal oedema and tragal tenderness with no object"),
   ("Otomycosis", "Fungal debris that can look like material but shows hyphae")],
  "<b>Otoscopy</b> &rarr; direct visualisation of the object, and an intact drum after removal.",
  "Seeing wax only excludes a foreign body; persistent pain and discharge after removal means "
  "secondary otitis externa, not a retained object &mdash; unless the canal cannot be fully seen."),

"Foreign body of the auricle": E(
  "&ldquo;My piercing has gone into the skin&rdquo; or &ldquo;there&rsquo;s something stuck in the "
  "outer part of my ear.&rdquo;",
  "Inspect for an <b>embedded object and any cartilage involvement</b>. Palpate for fluctuance and "
  "look for spreading erythema. Examine the canal too.",
  [("Perichondritis", "Infection of cartilage, hot and tender, sparing the lobule"),
   ("Auricular haematoma", "Fluctuant collection without a retained object"),
   ("Keloid", "A firm overgrowth at an old piercing site rather than an acute problem")],
  "<b>Inspection</b> &rarr; the object and whether cartilage is breached; cartilage involvement is "
  "what raises the stakes.",
  "Absent erythema and tenderness excludes perichondritis; a chronic firm nodule at a piercing is "
  "a keloid, not a foreign body."),

"Otitis externa": E(
  "&ldquo;My ear is really sore, especially if I touch it &mdash; I&rsquo;ve been swimming a "
  "lot.&rdquo;",
  "<b>Pain on tragal pressure or pulling the pinna</b> &mdash; the defining manoeuvre. Otoscopy for "
  "a <b>swollen, erythematous canal with debris</b>; try to see the drum, which should be normal. "
  "<b>Palpate the mastoid and check cranial nerve VII</b> to exclude the malignant form. Check for "
  "diabetes.",
  [("Acute otitis media", "No tragal tenderness; the drum bulges and the canal is normal"),
   ("Otomycosis", "Itch predominates, with visible hyphae or a wet-newspaper appearance"),
   ("Malignant otitis externa", "Granulation at the bony-cartilaginous junction, night pain, cranial neuropathy")],
  "<b>Clinical</b> &rarr; tragal tenderness with a swollen inflamed canal. <b>Culture</b> if it "
  "fails to settle &rarr; usually <i>Pseudomonas</i> or <i>Staphylococcus</i>.",
  "A bulging drum with no tragal tenderness redirects to otitis media; failure to respond in a "
  "diabetic patient means imaging for the malignant form; hyphae on examination mean otomycosis."),

"Otomycosis": E(
  "&ldquo;My ear itches constantly and there&rsquo;s a strange discharge &mdash; the drops the "
  "doctor gave me made it worse.&rdquo;",
  "Otoscopy for <b>fluffy white hyphae with black or grey spores</b> (<i>Aspergillus</i>) or a "
  "<b>curd-like white debris</b> (<i>Candida</i>). Assess tragal tenderness &mdash; usually much "
  "less than bacterial disease. Check the drum is intact before any drops.",
  [("Bacterial otitis externa", "Pain rather than itch; no hyphae; improves on antibiotic drops"),
   ("Chronic otitis media with discharge", "Discharge comes through a perforation, not from the canal"),
   ("Eczematous otitis externa", "Dry scaling skin and itch without fungal elements")],
  "<b>Otoscopy</b> &rarr; visible fungal elements. <b>Microscopy of debris with potassium "
  "hydroxide</b> &rarr; hyphae or budding yeast.",
  "Absence of fungal elements with a good antibiotic response means bacterial disease; a visible "
  "perforation with discharge redirects to chronic otitis media."),

"Otosclerosis": E(
  "&ldquo;My hearing has been slipping for years &mdash; my mother went the same way. Oddly I hear "
  "better in a noisy room.&rdquo;",
  "<b>Otoscopy is NORMAL</b>, which is the point &mdash; occasionally a faint pink blush on the "
  "promontory. <b>Weber lateralises TOWARD the worse ear; Rinne is negative on that side</b>. Ask "
  "about family history and about worsening in pregnancy.",
  [("Otitis media with effusion", "A conductive loss too, but the drum is abnormal and tympanometry is flat"),
   ("Cerumen impaction", "Same conductive pattern, resolved instantly by clearing the canal"),
   ("Cholesteatoma", "Conductive loss with discharge, a retraction pocket and keratin")],
  "<b>Audiometry</b> &rarr; a conductive loss with a <b>Carhart notch, a dip in bone conduction "
  "around 2000 hertz</b>. <b>Tympanometry</b> &rarr; type As, normal pressure with REDUCED "
  "compliance from the fixed stapes. <b>Acoustic reflexes absent.</b>",
  "A flat type B tympanogram means fluid, not fixation; an abnormal drum on otoscopy excludes it; "
  "clearing wax and restoring hearing excludes it."),

"Keloid of the ear": E(
  "&ldquo;A lump grew where I had my ear pierced and it keeps getting bigger.&rdquo;",
  "Inspect and palpate a <b>firm, rubbery nodule extending BEYOND the original wound margin</b>. "
  "Note the site and skin type. Examine the canal, which is normal.",
  [("Hypertrophic scar", "Stays WITHIN the wound boundary and often regresses &mdash; the key distinction"),
   ("Epidermoid cyst", "Softer, with a central punctum, and may discharge keratin"),
   ("Chondrodermatitis nodularis", "Painful, on the helix, in older patients")],
  "<b>Clinical</b> &rarr; a firm scar growing beyond the original injury. Biopsy only if the "
  "diagnosis is in doubt.",
  "Growth confined to the scar line means hypertrophic scar; a punctum means a cyst; marked "
  "tenderness on the helix means chondrodermatitis."),

"Conductive hearing loss": E(
  "&ldquo;Sounds are muffled, like my ear is plugged &mdash; but my own voice sounds loud.&rdquo;",
  "Otoscopy of canal and drum &mdash; the cause is usually visible. <b>Weber lateralises TOWARD the "
  "affected ear; Rinne is negative (bone better than air) on that side.</b> Pneumatic otoscopy.",
  [("Sensorineural loss", "Weber lateralises AWAY and Rinne stays positive &mdash; the opposite pattern"),
   ("Mixed loss", "Both an air-bone gap AND reduced bone conduction"),
   ("Functional loss", "Tuning forks and audiometry contradict each other and the behaviour")],
  "<b>Audiometry</b> &rarr; an <b>air-bone gap</b> with normal bone conduction &mdash; that gap IS "
  "the definition. <b>Tympanometry</b> &rarr; type B for fluid or perforation, type C for negative "
  "pressure, type As for fixation.",
  "Absent air-bone gap excludes it; depressed bone conduction means a sensorineural or mixed loss; "
  "inconsistent responses suggest a functional loss."),

"Sensorineural hearing loss": E(
  "&ldquo;I can hear that people are talking but I can&rsquo;t make out the words, especially in a "
  "crowd.&rdquo;",
  "<b>Otoscopy is normal.</b> <b>Weber lateralises AWAY to the better ear; Rinne remains positive "
  "bilaterally.</b> Cranial nerves and cerebellar signs. Establish whether onset was sudden &mdash; "
  "that changes it into an emergency.",
  [("Conductive loss", "Weber toward, Rinne negative, and usually a visible cause"),
   ("Acoustic neuroma", "Asymmetric, with speech discrimination worse than the pure tone loss predicts"),
   ("Presbycusis", "Bilateral, symmetric, gradual, high-frequency &mdash; the commonest cause")],
  "<b>Audiometry</b> &rarr; reduced air AND bone conduction together with <b>no air-bone gap</b>. "
  "<b>Magnetic resonance with gadolinium</b> if asymmetric &rarr; an enhancing internal auditory "
  "canal lesion.",
  "An air-bone gap excludes it; symmetric high-frequency loss in an older patient is presbycusis, "
  "not a tumour; normal imaging excludes a schwannoma."),

"Presbycusis": E(
  "&ldquo;Everyone mumbles these days, and restaurants are impossible.&rdquo; Often the family "
  "raises it before the patient does.",
  "Otoscopy &mdash; <b>clear wax first, since impaction is common and reversible</b>. Weber and "
  "Rinne showing a sensorineural pattern. <b>Check symmetry</b>; presbycusis should be symmetric.",
  [("Noise-induced loss", "A notch at 4000 hertz with recovery at 8000, and an exposure history"),
   ("Cerumen impaction", "Conductive and immediately reversible &mdash; always excluded first"),
   ("Acoustic neuroma", "Asymmetric, which presbycusis is not")],
  "<b>Audiometry</b> &rarr; a <b>bilateral, symmetric, gradually sloping high-frequency "
  "sensorineural loss</b>, with speech discrimination falling in noise.",
  "Asymmetry mandates imaging rather than a hearing aid; a 4000 hertz notch means noise damage; "
  "an air-bone gap means something conductive is also present."),

"Tinnitus": E(
  "&ldquo;There&rsquo;s a ringing in my ears that never stops &mdash; it&rsquo;s worst at "
  "night.&rdquo;",
  "Establish whether it is <b>pulsatile</b>, which changes everything. <b>Auscultate the ear, neck "
  "and skull</b> for a bruit. Otoscopy &mdash; look for a <b>red mass behind the drum</b>. Tuning "
  "forks. Review medications.",
  [("Glomus tumour", "Pulsatile, with a red retrotympanic mass and a positive Brown sign"),
   ("Ototoxicity", "Bilateral, follows a culprit drug, often with hearing loss"),
   ("Noise-induced or age-related loss", "Non-pulsatile tinnitus accompanying the loss itself")],
  "<b>Audiometry</b> &rarr; the accompanying hearing loss that usually drives it. If PULSATILE, "
  "<b>imaging with vascular study</b> &rarr; a vascular tumour or a dural fistula.",
  "Non-pulsatile bilateral tinnitus with symmetric loss needs no imaging; a normal otoscopy "
  "excludes a glomus tumour; stopping a culprit drug with improvement points to ototoxicity."),

"Exostosis": E(
  "&ldquo;I&rsquo;ve been a cold-water surfer for years and my ears keep getting blocked and "
  "infected.&rdquo;",
  "Otoscopy showing <b>multiple, bilateral, broad-based bony swellings in the deep bony canal</b>. "
  "Assess how much canal remains and whether the drum can be seen. Tuning forks if hearing is down.",
  [("Osteoma", "Solitary, unilateral and pedunculated &mdash; the direct contrast"),
   ("Cerumen impaction", "Wax rather than bone; it can be cleared"),
   ("Ear canal carcinoma", "Friable, bleeding and painful rather than smooth and bony")],
  "<b>Otoscopy</b> &rarr; smooth, hard, skin-covered bony mounds. <b>Computed tomography</b> if "
  "surgery is planned &rarr; the extent of bony narrowing.",
  "A single pedunculated lesion is an osteoma; wax that clears excludes it; friable bleeding "
  "tissue needs biopsy for carcinoma."),

"Glomus tumour": E(
  "&ldquo;I hear my own heartbeat whooshing in my ear all the time, in time with my pulse &mdash; "
  "and my hearing on that side is going.&rdquo;",
  "Otoscopy for a <b>red or blue pulsatile mass behind the drum</b>. <b>Brown sign &mdash; the mass "
  "blanches on positive pressure with the pneumatic otoscope.</b> <b>Auscultate for a bruit.</b> "
  "Cranial nerves VII and IX to XII. <b>Never biopsy it in clinic.</b>",
  [("High-riding jugular bulb", "A vascular variant, also blue behind the drum, but not a tumour"),
   ("Aberrant internal carotid artery", "Pulsatile too &mdash; and biopsy would be catastrophic"),
   ("Haemotympanum", "Blood behind the drum after trauma; not pulsatile")],
  "<b>Computed tomography and magnetic resonance with angiography</b> &rarr; an intensely enhancing "
  "mass with a <b>salt and pepper</b> pattern of flow voids and bone erosion. <b>Urinary "
  "catecholamines</b> if it is secreting.",
  "Imaging is what excludes the vascular variants &mdash; and it must come BEFORE any instrument "
  "touches the mass; a trauma history with a non-pulsatile blue drum is haemotympanum."),
}
