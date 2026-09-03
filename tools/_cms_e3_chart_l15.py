# -*- coding: utf-8 -*-
"""Lecture 15 rows for the ENT comparison chart.

Disorders of the External and Middle Ear, Prof. Hugh Griffenkranz, 3 September.
Same shape as the ophthalmology modules:
  ROWS_L15  (name, group, giveaway, presentation, testing, treatment,
             urgency, education, slides, deck)
  DIFF_L15  name -> (pain, hearing loss, key otoscopy finding)
  IMGS_L15  name -> (filename, slide)

THE THREE DISCRIMINATORS ARE CHOSEN FOR THIS BLOCK, not copied from ophthalmology.
Jaquith's ophthalmology triad was pain / laterality / pupil. For the ear the
three that actually separate the conditions are PAIN, the TYPE OF HEARING LOSS
(conductive, sensorineural or none) and WHAT THE DRUM LOOKS LIKE. Almost every
vignette in this block turns on those three.

MASTOIDITIS IS HERE, NOT IN LECTURE 16, even though it is Lecture 16's
objective. The only teaching on it in either deck is one line of slide 19 --
"spread of infection to mastoid air cells" as a complication of acute otitis
media. Filing it where the content is keeps the row honest; the guide notes
that the objective sits in the other lecture.
"""
ETD = "Eustachian tube"
OM = "Otitis media"
PRESS = "Pressure and wax"
MASS = "Middle ear mass"
TRAUMA = "Ear trauma"
FB = "Foreign body"
OE = "External canal infection"
FIX = "Conductive fixation"
NEO = "Neoplasm"
D15 = "Disorders External and Middle Ear"

ROWS_L15 = [
 ("Eustachian tube dysfunction", ETD,
  "<b>Fullness</b> after a cold &middot; <b>crackling or popping</b> on swallowing &middot; <b>retracted</b> drum",
  "Oedema of the tube lining after an <b>upper respiratory infection or allergy</b> stops the tube equalising pressure. Fullness, mild to moderate hearing impairment, and <b>crackling or popping with yawning or swallowing</b>, which indicates the blockage is only partial. Usually <b>transient &mdash; days to weeks</b>.",
  "Clinical. Otoscopy: <b>retraction of the tympanic membrane</b> and <b>decreased mobility on insufflation</b>. Tympanometry, taught in the next lecture, shows a <b>negative pressure peak</b>.",
  "Systemic or intranasal <b>decongestants</b> and <b>intranasal corticosteroids</b>. Forced exhalation against resistance. <b>Caution with active nasal discharge</b> &mdash; that manoeuvre can force infected fluid into the middle ear and trigger acute otitis media.",
  "Routine",
  "<b>Avoid air travel and other pressure changes until symptoms resolve.</b> It is the commonest single reason an ear will not clear on a plane.",
  "6&ndash;10", D15),

 ("Acute otitis media", OM,
  "<b>Bulging, erythematous</b> drum &middot; otalgia and fever after a cold &middot; child around <b>2 years</b>",
  "Rapid-onset middle ear inflammation, most often <b>following an upper respiratory illness</b>. Commonest in children, <b>peak incidence around age 2</b>; adults are only <b>3&ndash;15%</b> of diagnoses. <b>Otalgia, fever, hearing loss.</b> Suppurative form discharges into the canal through a perforation. <b>Recurrent</b> means 3 or more episodes in 6 months, or more than 4 in 12 months, with complete resolution between.",
  "<b>Diagnosed clinically.</b> Otoscopy: <b>erythematous and/or bulging</b> drum, purulent effusion often visible, <b>decreased mobility on pneumatic otoscopy</b>, sometimes palpable cervical nodes. Tympanometry optional. Organisms: <b>S. pneumoniae, H. influenzae, M. catarrhalis</b>.",
  "<b>Most episodes resolve spontaneously.</b> Antibiotics for bacterial involvement &mdash; <b>amoxicillin</b>. Analgesics and antipyretics for the pain and fever. <b>Tympanostomy tubes</b> for refractory or recurrent episodes, or when complications are present (ENT).",
  "Routine",
  "Explain that most cases settle on their own, so a wait-and-see period is not neglect. Return if pain worsens or discharge appears.",
  "12&ndash;19", D15),

 ("Otitis media with effusion", OM,
  "<b>Dull</b> drum with an <b>air&ndash;fluid level</b> &middot; often <b>asymptomatic</b> &middot; found incidentally",
  "Middle ear inflammation <b>with an effusion but without acute infection</b>. Follows eustachian tube dysfunction trapping fluid, and <b>often persists after a bacterial acute otitis media has resolved</b>. <b>Often asymptomatic</b> and picked up incidentally on otoscopy; otherwise hearing loss and fullness.",
  "Clinical. Otoscopy: <b>dull</b> tympanic membrane, <b>air/fluid level often visible</b>, <b>decreased mobility on pneumatic otoscopy</b>. Tympanometry optional &mdash; a <b>type B</b> curve fits the stiff, fluid-filled middle ear.",
  "<b>Most resolve spontaneously.</b> The decision to intervene turns on <b>how long the fluid has been there, the degree of hearing loss, and the effect on speech and language development</b>. <b>Tympanostomy tubes</b> (ENT); <b>adenoidectomy</b> if hypertrophy is obstructing the tubes (ENT).",
  "Routine",
  "In a child the risk is not the ear but the <b>speech and language delay</b> from months of muffled hearing &mdash; which is why duration matters more than the appearance.",
  "13&ndash;19", D15),

 ("Chronic otitis media", OM,
  "<b>Non-healing perforation</b> &middot; recurrent infection &middot; persistent drainage",
  "Recurrent infection with a <b>non-healing perforation</b> of the tympanic membrane. <b>Duration required for diagnosis is controversial</b> &mdash; weeks to months. Three subtypes: <b>benign</b> (dry perforation, no active infection); <b>with effusion</b>, also called chronic serous otitis media (continuous serous drainage through the perforation); and <b>chronic suppurative</b> (persistent purulent drainage).",
  "Clinical, on the persistent perforation and drainage. Audiometry for the associated conductive loss.",
  "<b>Refer to ENT.</b>",
  "Routine",
  "The perforation is the disease, not just its aftermath &mdash; water precautions and follow-up matter because it will not close on its own.",
  "20", D15),

 ("Mastoiditis", OM,
  "<b>Complication of acute otitis media</b> &middot; infection spreading to the <b>mastoid air cells</b>",
  "Spread of acute otitis media infection into the <b>mastoid air cells</b>. Listed with tympanic membrane perforation, labyrinthitis and the rare meningitis or encephalitis as the complications of acute otitis media.",
  "Suspected clinically in a child with acute otitis media who is not improving. Imaging defines the extent.",
  "Treat as a complicated acute otitis media &mdash; <b>ENT involvement</b>.",
  "Urgent",
  "It is the reason acute otitis media that is not settling gets re-examined rather than simply re-prescribed.",
  "19", D15),

 ("Barotrauma", PRESS,
  "<b>Cannot equalise</b> &middot; flying or <b>SCUBA</b> &middot; <b>haemotympanum</b> behind the drum",
  "Inability to equalise middle ear pressure, seen with <b>air travel, rapid altitude change and SCUBA diving</b>. May <b>rupture the tympanic membrane</b> or bleed into the middle ear. <b>Otalgia and conductive hearing loss.</b>",
  "Otoscopy: <b>decreased mobility on insufflation</b>, <b>visible haemotympanum</b> if there is haemorrhage, visible perforation if present. Severe cases can rupture the <b>round or oval window</b>, adding <b>tinnitus, sensorineural hearing loss, vertigo, nausea and vomiting</b> &mdash; that combination means the inner ear is involved.",
  "Equalise by <b>swallowing, yawning, exhaling through the nose against resistance</b>. Oral or intranasal decongestants may help. <b>Myringotomy gives instant relief</b> and is reserved for severe otalgia and hearing loss with an intact membrane (ENT). Recurrent episodes in frequent flyers may justify <b>tympanostomy tubes</b> (ENT).",
  "Routine",
  "<b>Avoid pressure changes while a respiratory illness or allergy flare is active.</b> If flying is unavoidable, take a decongestant beforehand and equalise on descent.",
  "22&ndash;25", D15),

 ("Cerumen impaction", PRESS,
  "<b>Self-induced by cleaning</b> &middot; wax filling the canal &middot; conductive loss that clears on removal",
  "Cerumen is a <b>protective, thick, oily secretion of the outer third of the canal</b>, and the canal is normally <b>self-cleansing</b>. Impaction is <b>most commonly self-induced</b> by cleaning attempts that push wax deeper. May be asymptomatic, or cause pruritus, fullness and <b>conductive hearing loss</b>.",
  "Otoscopy: <b>visible cerumen fully or partially obstructing the canal</b>, wet and sticky, dry and flaky, or dark.",
  "Over-the-counter otic preparations to soften it. <b>Irrigation</b> or suction in clinic &mdash; irrigation uses <b>body-temperature water and ONLY if the drum is intact</b>. <b>Curette</b> removal suits soft wax and a compliant patient. <b>If tympanostomy tubes or a perforation are present, removal must be done by ENT.</b>",
  "Routine",
  "<b>Do not insert anything into the canal.</b> If cleaning is wanted, a washcloth over the index finger at the opening is the whole technique.",
  "27&ndash;29", D15),

 ("Cholesteatoma", MASS,
  "<b>Keratin debris in a retraction pocket</b> &middot; <b>recurrent otorrhoea with no otitis externa</b>",
  "A collection of <b>keratinised squamous epithelium</b> in the middle ear or mastoid. <b>No cholesterol in it and not a neoplasm</b>, despite the name. <b>Primary</b> is commonest and forms from <b>retraction of the tympanic membrane</b>, usually the <b>pars flaccida</b>; <b>secondary</b> follows epithelial migration or surgery; <b>congenital</b> is least common and forms with no retraction or perforation. Risk factors are <b>eustachian tube dysfunction</b> and chronic middle ear inflammation. May be asymptomatic; otherwise tinnitus, <b>recurrent otorrhoea in the absence of otitis externa</b>, and hearing loss as a late finding.",
  "<b>Usually a clinical diagnosis.</b> Otoscopy: <b>retraction containing squamous epithelium and keratin debris</b>, debris behind the drum, sometimes purulent otorrhoea, granulation tissue or visible <b>ossicular erosion</b>. <b>Audiometry</b> to assess hearing loss. <b>CT</b> for extent in severe cases, and useful in secondary acquired disease when the drum is opaque.",
  "<b>Refer to ENT.</b> Remove canal debris, treat infection with antibiotics, then <b>surgical removal</b>, usually with <b>tympanoplasty</b>. <b>Mastoidectomy</b> if it extends into the mastoid with bony erosion.",
  "Urgent",
  "It erodes bone, so it is removed rather than watched &mdash; the discharge is a symptom of that, not a simple infection.",
  "31&ndash;37", D15),

 ("Hematoma of the external ear", TRAUMA,
  "<b>Blunt trauma</b> &middot; <b>cartilaginous landmarks lost</b> &middot; drain early or <b>cauliflower ear</b>",
  "Blood pooling in the <b>sub-perichondrial space</b>, usually after <b>blunt trauma</b>. The collection <b>keeps oxygen and nutrients from the cartilage</b>, which is what risks necrosis. <b>May develop hours after the injury</b>, so patients are re-checked at 12&ndash;24 hours. Examination: <b>oedema and ecchymosis of the auricle with loss of the cartilaginous landmarks</b>.",
  "Clinical.",
  "<b>Drain it &mdash; incision or large-needle aspiration &mdash; and do it early.</b> After <b>7 days</b> granulation tissue makes drainage much harder. Follow with irrigation and topical and/or systemic antibiotics. <b>Ear splinting</b> improves the cosmetic result and prevents re-accumulation: cotton bolsters, plaster moulds, silicone putty, thermoplastic splints.",
  "Urgent",
  "<b>Early diagnosis and drainage is what prevents cauliflower ear.</b> Come back at 12&ndash;24 hours even if it looks minor, because the haematoma can appear late.",
  "39&ndash;42", D15),

 ("Lacerations and avulsion", TRAUMA,
  "Blunt or sharp trauma to the auricle &middot; <b>prompt repair</b> &middot; pressure dressing after",
  "Blunt or sharp trauma to the auricle. <b>Prompt repair and infection prevention are critical.</b> Simple lacerations close with sutures; complex ones and avulsions may need debridement first; tissue grafts if there is tissue loss. <b>If avulsed tissue is recovered, reattachment is often successful.</b>",
  "Clinical.",
  "Repair as above, then <b>cover with a pressure dressing to prevent a haematoma forming under the repair</b>.",
  "Urgent",
  "Bring any avulsed tissue &mdash; reattachment often works.",
  "43", D15),

 ("Tympanic membrane perforation", TRAUMA,
  "<b>Pain stops</b> after the rupture &middot; conductive loss &middot; visible defect",
  "Follows <b>impact injury, explosive acoustic trauma, barotrauma or severe acute otitis media</b>. Symptoms vary with cause but it is <b>generally not painful once the membrane has ruptured</b>. <b>Conductive hearing loss.</b> Otoscopy distinguishes <b>central</b> (does not reach the margin) from <b>marginal</b> (involves the margin); drainage through the perforation if it followed acute otitis media.",
  "Clinical, on otoscopy.",
  "<b>Most resolve spontaneously over several weeks</b> &mdash; and <b>as little as 48&ndash;72 hours</b> when it followed acute otitis media. <b>Surgical reconstruction</b> for large perforations or ones present a long time (ENT).",
  "Routine",
  "Keep the ear dry while it heals. Report worsening hearing or dizziness &mdash; <b>trauma can disrupt the ossicles as well</b>.",
  "45&ndash;47", D15),

 ("Foreign body of the canal", FB,
  "Child &middot; anything that fits &middot; <b>do not push it deeper</b>",
  "Commoner in children but possible at any age, and <b>can be anything that fits</b> &mdash; beads, popcorn, crayons, insects, pencil erasers, paper. Otalgia varies with the shape of the object; <b>bloody discharge if the canal lining is damaged</b>; fullness and foreign body sensation.",
  "Otoscopy.",
  "<b>CAUTION &mdash; do not push the object deeper.</b> <b>Firm</b> objects come out with a loop or hook, <b>soft</b> ones with alligator forceps. <b>Irrigation only if the drum is known to be intact</b>, and with care: <b>organic objects swell when wet</b> and lodge harder. <b>Insects are immobilised first by filling the canal with lidocaine</b> &mdash; again only if the drum is intact. Refer to ENT for removal under microscopy where warranted.",
  "Urgent",
  "Nothing goes into the ear at home to fetch it out; attempts are what turn a simple removal into a referral.",
  "49&ndash;50", D15),

 ("Foreign body of the auricle", FB,
  "<b>Embedded earring</b> &middot; girls and young adolescents &middot; infection is the concern",
  "Piercings becoming <b>embedded in the earlobe</b> or elsewhere on the auricle. <b>Most common in girls and young adolescents with pierced ears.</b> Pain, erythema and oedema; may have <b>purulent drainage from the piercing site</b>. Examination: pain on palpation, and the foreign body may be palpable.",
  "Clinical.",
  "Removal under <b>local anaesthetic</b>; <b>younger or non-compliant patients may need sedation</b>.",
  "Urgent",
  "<b>Infection is the biggest concern</b>, not the object itself.",
  "51&ndash;52", D15),

 ("Otitis externa", OE,
  "<b>Pain on moving the tragus</b> &middot; swimmer &middot; <b>discharge from the canal</b>",
  "Inflammation and infection of the external canal, affecting <b>10% of people in their lifetime</b>, all ages but commonest in <b>children and early adolescence</b> and in <b>summer</b>. Organisms: <b>P. aeruginosa 38%</b>, S. epidermidis 9%, S. aureus 8%; other bacteria and fungi possible. Risk factors: <b>moisture and swimming</b>, epithelial damage from aggressive cleaning, foreign bodies such as cotton swab fibres, <b>occlusion by hearing aids or headphones</b>, dermatitis of the auricle, radiation. Symptoms: otalgia <b>exacerbated by touching or moving the auricle or tragus</b>, otorrhoea, pruritus, fullness, reduced hearing.",
  "<b>Clinical diagnosis.</b> <b>Cultures reserved</b> for severe, chronic or recurrent infection, immunosuppression, post-operative infection and treatment failure. Examination: <b>tenderness to palpation</b>, visible discharge, erythema and oedema of the canal, periauricular and anterior cervical <b>lymphadenopathy</b>, thickened canal skin in chronic disease. Differential: otomycosis, suppurative otitis media, contact dermatitis, psoriasis and the rare <b>carcinoma of the ear canal</b>.",
  "<b>Remove debris</b>, then otic drops: <b>antiseptic</b> (boric acid, ichthammol, phenol, aluminium acetate, gentian violet, thymol, cresylate, alcohol), <b>antibiotic</b> (ofloxacin, ciprofloxacin, colistin, polymyxin B, neomycin, chloramphenicol, gentamicin, tobramycin) or <b>acidifying</b> (acetic acid). <b>Combination drops with a steroid</b> reduce pain and inflammation. An <b>ear wick</b> if the canal is stenosed.",
  "Routine",
  "Keep the ear dry, stop cleaning it, and use the drops for the full course &mdash; the pain settles well before the infection does.",
  "54&ndash;59", D15),

 ("Malignant otitis externa", OE,
  "<b>Elderly diabetic</b> &middot; <b>pain out of proportion</b> to the exam &middot; <b>facial nerve weakness</b>",
  "Also called <b>necrotizing external otitis</b>. A <b>severe and potentially fatal</b> infection of the bone and marrow spaces of the skull base and the soft tissue and cartilage of the temporal region. <b>Elderly diabetics and immunocompromised patients are most at risk.</b> <b>Over 95% is spread of P. aeruginosa from an otitis externa.</b> Symptoms: <b>severe otalgia out of proportion to the physical findings</b>, copious otorrhoea, sometimes visible necrosis of the canal and <b>evidence of facial nerve weakness</b>.",
  "<b>MRI or CT shows infection in the bony structures</b> &mdash; that is what separates it from ordinary otitis externa.",
  "<b>Antipseudomonal antibiotics</b> &mdash; for example <b>ciprofloxacin</b>.",
  "Emergent",
  "The complaint that matters is pain far worse than the ear looks, in a diabetic or immunocompromised patient. That combination is not treated as a routine swimmer's ear.",
  "61", D15),

 ("Otomycosis", OE,
  "<b>Itch more than pain</b> &middot; <b>&ldquo;wet newspaper&rdquo;</b> spores or <b>white curd</b>",
  "Fungal infection of the external canal, <b>9% of ear canal infections</b> and varying with climate. Commonest organisms <b>Aspergillus niger and Candida</b>. Pruritus, <b>discomfort that is less painful than bacterial otitis externa</b>, otorrhoea, foreign body sensation.",
  "Otoscopy is the diagnosis. <b>Aspergillus: visible fungal spores and filaments, described as &ldquo;wet newspaper&rdquo;.</b> <b>Candida: white, fluffy, curd-like material.</b> Mild to moderate oedema.",
  "<b>Debris removal</b> and <b>topical antifungals</b>.",
  "Routine",
  "It is treated by cleaning the canal as much as by the drops; the itch outlasting the pain is the clue that it is fungal.",
  "62&ndash;63", D15),

 ("Otosclerosis", FIX,
  "<b>Hearing is better in background noise</b> &middot; gradual conductive loss &middot; <b>normal drum</b>",
  "Bony overgrowth affecting the <b>stapes</b>, which eventually <b>fixes</b> and causes hearing loss. Gradual <b>conductive</b> loss, <b>bilateral and asymmetric in 70%</b>, unilateral in 30%. <b>The patient reports that hearing is better with background noise.</b> Tinnitus.",
  "<b>Visual examination is normal</b> &mdash; its job is to exclude the other causes of conductive loss such as foreign body and cerumen impaction. <b>Weber lateralises to the affected ear</b> (or the more affected ear if bilateral) and <b>bone conduction is greater than or equal to air conduction</b> on Rinne. <b>Audiometry</b> for the extent; <b>CT is the initial imaging of choice</b>. Differential: perforation, severe tympanosclerosis, otitis media with effusion, cholesteatoma, ossicular discontinuity, middle ear tumour.",
  "<b>Observation</b> if unilateral or the patient is untroubled. <b>Hearing aids.</b> <b>Surgery</b> is elective, generally one ear at a time, replacing the stapes with a prosthesis or placing a cochlear implant (ENT). Non-surgical options under investigation &mdash; sodium fluoride, bisphosphonates &mdash; with recommendations varying widely (ENT).",
  "Routine",
  "A conductive loss with a <b>normal-looking drum</b> is the pattern; improved hearing in noise is the sentence patients volunteer.",
  "65&ndash;67", D15),

 ("Keloid of the ear", NEO,
  "<b>Hypertrophic scar after trauma</b> &mdash; classically after piercing",
  "Benign neoplasm of the ear: <b>keloid and hypertrophic scars resulting from trauma</b>.",
  "Clinical.",
  "<b>Avoid further trauma.</b> <b>Intralesional steroid injection</b>, corticosteroid tape, excision. <b>Radiation therapy in adults, NEVER in children.</b> <b>Follow closely for recurrence.</b>",
  "Routine",
  "Recurrence is the rule rather than the exception, which is why follow-up is part of the treatment.",
  "69&ndash;70", D15),

 ("Carcinoma of the ear canal", NEO,
  "<b>Otitis externa that will not respond to treatment</b> &middot; <b>bloody otorrhoea</b> &middot; friable canal",
  "<b>Very rare and aggressive.</b> Presents with an <b>abnormal growth in the ear canal</b>, <b>bloody otorrhoea</b>, a <b>friable ear canal</b> and <b>failure to respond to treatment for external otitis</b>. Late findings are <b>hearing loss and facial paralysis</b>. <b>Often misdiagnosed as otitis externa.</b>",
  "<b>Definitive diagnosis is biopsy.</b>",
  "Biopsy first, then oncological management (ENT).",
  "Emergent",
  "The teaching point is the misdiagnosis: an otitis externa that does not respond, especially with blood, gets looked at again rather than re-treated.",
  "71", D15),
]

DIFF_L15 = {
 "Eustachian tube dysfunction": ("No &mdash; fullness", "<b>Conductive</b>, mild to moderate", "<b>Retracted</b> drum, reduced mobility"),
 "Acute otitis media": ("<b>YES</b> &mdash; otalgia with fever", "<b>Conductive</b>", "<b>Bulging, erythematous</b> drum"),
 "Otitis media with effusion": ("<b>NO</b> &mdash; often asymptomatic", "<b>Conductive</b>, temporary", "<b>Dull</b> drum, <b>air&ndash;fluid level</b>"),
 "Chronic otitis media": ("Varies with activity", "<b>Conductive</b>", "<b>Non-healing perforation</b>"),
 "Mastoiditis": ("<b>YES</b>", "<b>Conductive</b>", "Complication of acute otitis media"),
 "Barotrauma": ("<b>YES</b> &mdash; otalgia", "<b>Conductive</b>; sensorineural if the window ruptures", "<b>Haemotympanum</b>, reduced mobility"),
 "Cerumen impaction": ("No &mdash; pruritus, fullness", "<b>Conductive</b>", "<b>Wax obstructing</b> the canal"),
 "Cholesteatoma": ("No &mdash; otorrhoea", "<b>Conductive</b>, a late finding", "<b>Keratin debris in a retraction</b>"),
 "Hematoma of the external ear": ("<b>YES</b>", "None", "<b>Auricle swollen, landmarks lost</b>"),
 "Lacerations and avulsion": ("<b>YES</b>", "None", "Visible wound of the auricle"),
 "Tympanic membrane perforation": ("<b>Stops</b> once it ruptures", "<b>Conductive</b>", "<b>Visible defect</b>, central or marginal"),
 "Foreign body of the canal": ("Varies with the object", "<b>Conductive</b> if obstructing", "<b>Object in the canal</b>"),
 "Foreign body of the auricle": ("<b>YES</b>", "None", "<b>Embedded piercing</b>"),
 "Otitis externa": ("<b>YES &mdash; worse on moving the tragus</b>", "<b>Conductive</b> if the canal closes", "<b>Canal erythematous and oedematous</b>"),
 "Malignant otitis externa": ("<b>SEVERE &mdash; out of proportion</b>", "<b>Conductive</b>", "Canal necrosis, <b>facial nerve weakness</b>"),
 "Otomycosis": ("<b>Less than bacterial</b> &mdash; itch dominates", "<b>Conductive</b> if obstructing", "<b>&ldquo;Wet newspaper&rdquo;</b> or white curd"),
 "Otosclerosis": ("<b>NO</b>", "<b>Conductive</b>, gradual", "<b>NORMAL drum</b>"),
 "Keloid of the ear": ("No", "None", "Scar on the auricle"),
 "Carcinoma of the ear canal": ("<b>YES</b>", "<b>Conductive</b>, late", "<b>Friable growth, bloody otorrhoea</b>"),
}

# Every one of these was viewed before it was assigned -- see the header of
# extract_cms_e3_chart_images.py. The filename carries the deck, so a picture
# can legitimately come from the OTHER lecture: barotrauma is taught in full
# here, but the only photograph of a haemotympanum in either deck is Lecture
# 16's slide 59, and the chart cell cites it as such.
IMGS_L15 = {
 "Eustachian tube dysfunction": ("l15-s009_pos1.jpg", 9),
 "Acute otitis media": ("l15-s016_pos1.jpg", 16),
 "Otitis media with effusion": ("l15-s016_pos2.jpg", 16),
 "Barotrauma": ("l16-s059_pos1.jpg", 59),
 "Cerumen impaction": ("l15-s026_pos2.jpg", 26),
 "Cholesteatoma": ("l15-s035_pos2.jpg", 35),
 "Hematoma of the external ear": ("l15-s040_pos1.jpg", 40),
 "Lacerations and avulsion": ("l15-s043_pos1.jpg", 43),
 "Tympanic membrane perforation": ("l15-s047_pos1.jpg", 47),
 "Foreign body of the canal": ("l15-s049_pos1.jpg", 49),
 "Foreign body of the auricle": ("l15-s052_pos1.jpg", 52),
 "Otitis externa": ("l15-s058_pos2.jpg", 58),
 "Malignant otitis externa": ("l15-s061_pos1.jpg", 61),
 "Otomycosis": ("l15-s063_pos1.jpg", 63),
 "Otosclerosis": ("l15-s065_pos1.jpg", 65),
 "Keloid of the ear": ("l15-s069_pos1.jpg", 69),
}
