# -*- coding: utf-8 -*-
"""Second top-up pool -- brings Lectures 15 and 17 to fifty each."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D15 = "CMS I Disorders of the External and Middle Ear"
D17 = "hughie Nose & Paranasal Sinuses"
I15 = ("Disorders of the external and middle ear: etiologies, epidemiology, risk factors, clinical "
       "manifestations, differential diagnosis, diagnostic testing, management, referrals, patient "
       "education, and prognosis")
I17 = ("Disorders of the nose and paranasal sinuses: etiologies, epidemiology, risk factors, "
       "clinical manifestations, differential diagnosis, diagnostic testing, management, referrals, "
       "patient education, and prognosis")

QUESTIONS = [

Q("Acute otitis media risk factors", I15,
  "A clinician explains why acute otitis media is so much commoner in young children than in "
  "adults.",
  [["The child's eustachian tube is shorter, wider and more horizontal",
    "Correct. The adult tube runs downward at an angle, so gravity assists drainage and its narrower "
    "calibre resists reflux from the nasopharynx. In a young child it is short, wide and nearly "
    "horizontal, which lets nasopharyngeal secretions and organisms reach the middle ear easily and "
    "drain from it poorly."],
   ["Children have larger middle ear cavities",
    "Middle ear volume is not the determinant, and a larger cavity would if anything drain more "
    "readily. The anatomy that matters is the tube connecting it to the nasopharynx."],
   ["Children produce more cerumen, blocking the canal",
    "Wax sits in the external canal, lateral to the drum, and has no bearing on whether the middle "
    "ear becomes infected. It causes conductive loss rather than infection behind the drum."],
   ["Children have thinner tympanic membranes",
    "Drum thickness does not determine susceptibility to middle ear infection, and the drum is a "
    "barrier rather than a route of entry. Organisms arrive through the eustachian tube."]],
  "mechanism", D15, 22),

Q("Otitis media watchful waiting", I15,
  "A 6-year-old with mild acute otitis media, no severe pain and reliable parents is considered for "
  "observation rather than immediate antibiotics.",
  [["Observation is reasonable with a plan to treat if not improving",
    "Correct. Many episodes resolve without antibiotics, and watchful waiting reduces unnecessary "
    "prescribing and side effects. It depends on three conditions being met: an older child, mild "
    "disease, and reliable follow-up so that antibiotics can be started promptly if there is no "
    "improvement in 48 to 72 hours."],
   ["Antibiotics are mandatory for every case of acute otitis media",
    "Universal treatment ignores the substantial proportion that resolve spontaneously and drives "
    "resistance. The exceptions that do need immediate treatment are severe disease, very young "
    "children and unreliable follow-up."],
   ["Observation is appropriate regardless of the child's age",
    "Under two years the threshold is much lower and immediate treatment is usually preferred, "
    "because complications are commoner and assessment is harder. Age is part of the decision."],
   ["Topical antibiotic drops can be used while observing",
    "Drops cannot cross an intact drum, so they deliver nothing to the middle ear. Adding them "
    "creates the appearance of treatment without any effect."]],
  "treatment", D15, 26),

Q("Perichondritis", I15,
  "A 24-year-old woman has a red, hot, exquisitely tender auricle three days after a cartilage "
  "piercing of the upper ear. The lobule is spared.",
  [["Perichondritis, needing antipseudomonal antibiotics",
    "Correct. Sparing of the lobule is the key observation: the lobule contains no cartilage, so an "
    "infection confined to the cartilaginous part of the ear implicates the perichondrium. "
    "Pseudomonas is the usual organism after high piercings, and treatment must cover it or the "
    "cartilage necroses and the ear deforms."],
   ["Cellulitis of the auricle",
    "Simple cellulitis would involve the lobule too, because it spreads through skin and soft tissue "
    "without regard to the cartilage boundary. The sparing is what localises this."],
   ["Auricular haematoma",
    "A haematoma follows blunt trauma and produces a tense swelling that obliterates the normal "
    "contours. It is not hot and erythematous, and there is no history of a blow."],
   ["Contact dermatitis from the jewellery",
    "Nickel allergy is common and would give itch with an eczematous rash, often extending to the "
    "lobule if that is pierced too. Severe tenderness with heat indicates infection rather than "
    "allergy."]],
  "diagnosis", D15, 35),

Q("Hearing aid counselling", I15,
  "A 68-year-old man with a conductive loss from otosclerosis is choosing between stapedectomy and "
  "a hearing aid.",
  [["Both are reasonable; surgery addresses the mechanism, an aid amplifies",
    "Correct. In otosclerosis the cochlea works normally and the problem is purely mechanical, so "
    "stapedectomy can restore hearing by bypassing the fixed footplate. A hearing aid achieves a "
    "functional result without operative risk, which includes the small chance of a sensorineural "
    "loss. The choice depends on how the patient weighs those."],
   ["Only surgery can help a conductive loss",
    "Amplification works well in conductive loss, arguably better than in sensorineural loss, "
    "because the cochlea can still process what reaches it. Presenting surgery as the only option "
    "removes a valid choice."],
   ["Only a hearing aid is appropriate, as surgery is obsolete",
    "Stapedectomy remains an established and effective operation for otosclerosis, and it is what "
    "current practice. Dismissing it misstates the evidence."],
   ["Neither will help until the loss becomes sensorineural",
    "Waiting for the disease to reach the cochlea makes the outcome worse, because a sensorineural "
    "component cannot be corrected by surgery and limits what amplification achieves."]],
  "treatment", D15, 65),

Q("Barotrauma in divers", I15,
  "A 32-year-old diver has ear pain and vertigo on ascent, with hearing loss that has not settled "
  "after several hours.",
  [["Suspect inner ear barotrauma with a possible perilymphatic fistula",
    "Correct. Middle ear barotrauma alone causes pain and conductive loss that settle as the "
    "effusion clears. Persistent vertigo and sensorineural loss after diving suggest the pressure "
    "change has ruptured a round or oval window membrane, letting perilymph leak, which needs "
    "prompt specialist assessment and avoidance of straining."],
   ["Simple middle ear barotrauma requiring only decongestants",
    "That is the common and benign diagnosis, and it would explain the pain, but it does not "
    "explain vertigo and persistent sensorineural loss. The additional symptoms are what change the "
    "diagnosis."],
   ["Decompression sickness affecting the vestibular system",
    "Vestibular decompression sickness exists and belongs on the differential after a deep dive, but "
    "it usually comes with other systemic features and follows a profile that risks bubble "
    "formation, rather than presenting as isolated ear symptoms on ascent."],
   ["Benign paroxysmal positional vertigo triggered by the dive",
    "Positional vertigo gives brief episodes provoked by head position and never affects hearing. "
    "Continuous vertigo with hearing loss is a different problem."]],
  "diagnosis", D15, 37),

Q("Ear discharge", I15,
  "A clinician is asked how the character of ear discharge helps localise the problem.",
  [["Scanty and itchy suggests the canal; profuse and mucoid suggests the middle ear",
    "Correct. The canal has no mucous glands, so discharge arising there is scanty, often itchy, and "
    "made of desquamated skin and exudate. Mucoid discharge implies mucous membrane, which exists in "
    "the middle ear, so profuse mucoid otorrhoea indicates it is coming through a perforation rather "
    "than from the canal itself."],
   ["Bloody discharge always indicates malignancy",
    "Bloody otorrhoea is a red flag that should prompt examination for carcinoma of the canal, "
    "particularly with treatment-resistant symptoms, but it also occurs with granulation tissue, "
    "trauma and acute perforation."],
   ["Foul-smelling discharge always indicates cholesteatoma",
    "Cholesteatoma classically produces foul discharge, so the association is worth knowing, but a "
    "retained foreign body and chronic suppurative otitis media both do the same thing."],
   ["Discharge character carries no localising information",
    "It carries a good deal, which is why it is described rather than merely noted. The presence of "
    "mucus in particular tells you which side of the drum the problem is on."]],
  "finding", D15, 31),

Q("Otitis externa severity", I15,
  "A 58-year-old man with otitis externa has spreading erythema over the pinna and onto the face, "
  "with fever and regional lymphadenopathy.",
  [["Add systemic antibiotics, as the infection has spread beyond the canal",
    "Correct. Topical therapy is first line precisely because the disease is confined to canal skin, "
    "and drops reach that surface directly. Once the infection has extended into surrounding soft "
    "tissue, producing cellulitis with fever and regional nodes, it is beyond the reach of a topical "
    "agent and needs a systemic one."],
   ["Continue topical therapy alone at a higher frequency",
    "Increasing the dose of a drug that cannot reach the infected tissue does not help. The problem "
    "here is anatomical spread rather than inadequate concentration in the canal."],
   ["Stop all antibiotics and use a topical steroid",
    "Steroid reduces swelling but suppresses the local response to a spreading bacterial infection, "
    "which allows it to advance while the outward signs settle."],
   ["Irrigate the canal to clear debris",
    "Aural toilet helps topical therapy work, but it does nothing for cellulitis of the pinna and "
    "face and would be very painful in an acutely inflamed ear."]],
  "next step", D15, 41),

Q("Ear examination in children", I15,
  "A clinician is examining the ear of a 2-year-old and needs to straighten the canal.",
  [["Pull the pinna downward and backward",
    "Correct. The infant and toddler canal runs upward from the drum, so the pinna is pulled down "
    "and back to align it. In older children and adults the canal takes the opposite course and the "
    "pinna is pulled up and back. Using the adult manoeuvre in a toddler leaves the drum "
    "obscured."],
   ["Pull the pinna upward and backward",
    "That is the correct technique for an older child or adult, whose canal curves differently. "
    "Applying it to a toddler works against the canal's natural direction."],
   ["Pull the tragus forward",
    "Pulling the tragus is the manoeuvre that ELICITS PAIN in otitis externa; it is a diagnostic "
    "test rather than a way to straighten the canal for viewing."],
   ["Push the pinna directly downward",
    "Downward force alone does not straighten the canal's curve, which requires a backward component "
    "as well. The drum would remain partly hidden."]],
  "finding", D15, 8),

Q("Sinusitis symptom duration", I17,
  "A clinician is asked how acute, subacute and chronic rhinosinusitis are separated.",
  [["Acute under four weeks, chronic beyond twelve weeks",
    "Correct. Acute disease resolves within four weeks, subacute occupies the interval between four "
    "and twelve, and chronic is defined by symptoms persisting beyond twelve weeks. The boundaries "
    "matter because the mechanism shifts from a single infection to impaired mucociliary clearance "
    "with persistent inflammation, and so does the treatment."],
   ["Acute under one week, chronic beyond four weeks",
    "These thresholds are too short. Four weeks is the acute boundary rather than the chronic one, "
    "and using it would classify ordinary prolonged viral illness as chronic disease."],
   ["Acute under twelve weeks, chronic beyond six months",
    "These are too long, and would leave a patient with three months of continuous symptoms still "
    "labelled acute, delaying the change in management that chronic disease requires."],
   ["Duration is not used to classify rhinosinusitis",
    "Duration is the primary axis of classification, and it is also one of the criteria that "
    "distinguishes bacterial from viral disease within the acute category."]],
  "finding", D17, 12),

Q("Epistaxis first aid", I17,
  "A patient having a nosebleed asks whether to blow the nose first.",
  [["Blow out clots first, then apply pressure and a vasoconstrictor",
    "Correct. Retained clot holds the vessel open and prevents the mucosal edges from apposing, so "
    "clearing it lets a fresh clot form against a compressed vessel. The sequence is to blow out "
    "clots, spray a topical vasoconstrictor such as oxymetazoline, then pinch the alae continuously "
    "for ten minutes."],
   ["Never blow the nose at any point",
    "The instruction not to blow the nose applies AFTER the bleeding has stopped, to protect the "
    "clot that has formed. Before pressure is applied, clearing clot is part of the technique."],
   ["Blow the nose repeatedly throughout the pressure period",
    "Blowing during or after the pressure period dislodges the forming clot and restarts the "
    "bleeding, which is the reason the post-bleed instruction exists."],
   ["Tilt the head back so blood does not stain clothing",
    "Tilting back sends blood into the pharynx to be swallowed or aspirated, hiding blood loss and "
    "causing vomiting. The patient sits up and leans forward."]],
  "treatment", D17, 41),

Q("Vasomotor rhinitis", I17,
  "A 48-year-old man has clear bilateral rhinorrhoea triggered by cold air, strong smells and "
  "alcohol. He has no itch, no sneezing paroxysms and negative allergy testing.",
  [["Vasomotor rhinitis",
    "Correct. Vasomotor rhinitis produces clear bilateral discharge like allergic rhinitis, which is "
    "why they are considered together, but it is driven by autonomic dysregulation rather than an "
    "immunoglobulin E response. The triggers are physical and chemical rather than allergenic, and "
    "itch and ocular symptoms are characteristically absent."],
   ["Allergic rhinitis",
    "Allergic disease brings itch, sneezing paroxysms and ocular symptoms, follows exposure to a "
    "specific allergen, and would be expected to give positive testing. All three of those are "
    "absent here."],
   ["Chronic bacterial sinusitis",
    "Chronic sinusitis produces purulent discharge with facial pressure and reduced smell over "
    "twelve weeks or more, rather than clear discharge triggered by cold air and odours."],
   ["Cerebrospinal fluid rhinorrhoea",
    "Clear fluid from the nose does raise this possibility, but it follows head trauma or surgery, "
    "is typically unilateral, and is not provoked by smells or alcohol."]],
  "diagnosis", D17, 66),

Q("Nasal polyps and asthma", I17,
  "A clinician lists the conditions associated with multiple benign nasal polyps and their "
  "approximate frequencies.",
  [["Allergic fungal sinusitis 85%, asthma 20 to 50%, cystic fibrosis 5 to 44%",
    "Correct. These are the recognised figures. Allergic "
    "fungal sinusitis carries the highest association, asthma is common, and cystic fibrosis is the "
    "one that changes management in a child. Aspirin intolerance is 8 to 20 per cent, alcohol "
    "intolerance 50 per cent and Churg-Strauss 50 per cent."],
   ["Cystic fibrosis is associated in over 90% of cases",
    "The association is real and clinically decisive in children, but the figure is far lower. "
    "Overstating it would imply almost every polyp patient has cystic fibrosis."],
   ["Asthma is associated in under 5% of cases",
    "This understates a well-recognised association of 20 to 50 per cent, and it would remove the "
    "prompt to ask every polyp patient about wheeze."],
   ["No systemic conditions are associated with nasal polyps",
    "The associations are the reason polyps are investigated rather than simply removed, and they "
    "are the entire content of that slide."]],
  "finding", D17, 63),

Q("Sinusitis in children", I17,
  "A 5-year-old has ten days of purulent nasal discharge and cough that has not improved. He is "
  "afebrile and otherwise well.",
  [["Bacterial sinusitis, meeting the ten-day criterion",
    "Correct. The same criteria apply in children as in adults, and persistence beyond ten days "
    "without improvement is one of them. Children have maxillary and ethmoid sinuses from birth, so "
    "sinusitis is possible at this age, and the ethmoid proximity to the orbit is what makes "
    "recognition important."],
   ["A prolonged viral upper respiratory infection needing no treatment",
    "Viral illness improves within about ten days, and ten days without improvement is precisely the "
    "threshold at which that explanation stops being adequate."],
   ["Allergic rhinitis",
    "Allergic disease gives clear bilateral discharge with itch, and follows a seasonal or exposure "
    "pattern. Purulent discharge for ten days is a different picture."],
   ["A nasal foreign body",
    "A foreign body gives UNILATERAL foul purulent discharge, and it is worth considering in this "
    "age group. Bilateral discharge with cough after a cold points to sinusitis instead."]],
  "diagnosis", D17, 15),

Q("Anosmia", I17,
  "A 55-year-old man has lost his sense of smell over several months, with nasal obstruction and "
  "thick discharge.",
  [["Conductive anosmia, from obstruction preventing odorants reaching the olfactory cleft",
    "Correct. Smell requires airflow to carry odorant molecules up to the olfactory epithelium high "
    "in the nasal vault. Polyps, chronic inflammation or marked mucosal swelling block that path, so "
    "the receptors are intact but never reached. That is why treating the obstruction can restore "
    "smell, unlike a sensorineural olfactory loss."],
   ["Sensorineural anosmia from olfactory nerve damage",
    "Nerve damage from head injury or a viral illness does cause permanent anosmia, but it is not "
    "accompanied by progressive obstruction and thick discharge, and treating the nose would not "
    "help."],
   ["A normal age-related change",
    "Smell does decline with age, but not over a few months and not alongside obstruction and "
    "discharge, which point to a treatable mechanical cause."],
   ["An early sign of a nasopharyngeal tumour",
    "A nasopharyngeal carcinoma presents with unilateral obstruction, blood-stained discharge, a "
    "neck mass or cranial nerve signs. Bilateral obstruction with anosmia more often reflects polyps "
    "or chronic inflammation."]],
  "mechanism", D17, 63),

Q("Nasal fracture timing", I17,
  "A 26-year-old man with a displaced nasal fracture presents four days after injury with marked "
  "swelling. He asks when it can be straightened.",
  [["Once the swelling settles, generally within about two weeks of injury",
    "Correct. Marked swelling obscures the underlying bony position, so reduction attempted "
    "immediately risks an inaccurate result. Waiting a few days lets the oedema settle, but the "
    "bones begin to unite after roughly two weeks, so there is a window in which reduction is both "
    "accurate and still possible."],
   ["Immediately, before any swelling develops",
    "Reduction in the first few hours is possible if the patient presents that early, but this "
    "patient is already four days out with established swelling, so that window has passed."],
   ["After three months, once healing is complete",
    "By then the bones have united in their displaced position, and correction would require a "
    "formal osteotomy rather than a simple closed reduction."],
   ["Displaced nasal fractures never require reduction",
    "Reduction is indicated for cosmetic deformity or airway obstruction, both of which follow "
    "displacement. Leaving every one untreated would accept avoidable deformity."]],
  "next step", D17, 46),

Q("Septal haematoma examination", I17,
  "A clinician is taught what to look for after any nasal injury, however minor it seems.",
  [["Inspect the septum for a boggy swelling",
    "Correct. A septal haematoma is easy to miss because attention goes to the bridge and to whether "
    "the nose looks straight, yet it is the one finding that destroys cartilage within days if not "
    "drained. Looking specifically at the septum, and feeling it, is what the four-criteria rule "
    "makes explicit."],
   ["Assess only whether the nose is straight",
    "Alignment addresses the cosmetic and airway question but says nothing about a collection under "
    "the perichondrium, which can be present in an entirely straight nose."],
   ["Obtain a radiograph in every case",
    "Films are omitted when all four reassuring criteria are met, and one of those criteria is the "
    "absence of a septal haematoma, which is established by looking rather than by imaging."],
   ["Check only for external bruising",
    "Bruising indicates that force was applied but has no relationship to whether blood has "
    "collected under the septal perichondrium."]],
  "finding", D17, 32),
]
