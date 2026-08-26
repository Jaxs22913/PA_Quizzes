# -*- coding: utf-8 -*-
# CMS I Exam 2, Lecture 1 -- pool D: orbital and periorbital cellulitis, the
# diagnostic modalities, and the red-eye triage framework (slides 66-71).
#
# THE TRIAGE SLIDES ARE THE HIGHEST-YIELD PART OF THIS DECK for a management
# exam: they give an explicit first-60-seconds sequence, a danger-sign list, a
# localisation pattern, and an emergent/same-day/urgent/routine disposition
# table. Prof. Jaquith told the Exam 1 class her questions are "pretty much all
# clinical vignettes ... A LOT are next management plan / first line treatment /
# patient education", which is exactly what these slides support.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "CMS I Common Ophthalmological Disorders 2026 - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
def cn(n): return f"{SRC}, Slide {n} (speaker notes)"

IOA = ("Objective a — Compare and contrast the etiologies, epidemiology, risk factors, "
       "clinical manifestations, differential diagnosis, diagnostic testing, management, "
       "appropriate referrals, patient education, and prognosis of the following common "
       "ophthalmological disorders")
IOB = ("Objective b — Identify medical care strategies for ophthalmological disorders in the "
       "lecture topic list for the following populations: infant, child, adolescent, adult, elderly")

POOL_D = [
 # ---- cellulitis ----
 dict(topic="Cellulitis", io=IOA, slot="etiology",
   q="Where does periorbital or orbital cellulitis usually come from?",
   opts=[
     ["Direct extension from a bacterial sinus, skin or dental infection",
      "Correct — the deck's three source sites."],
     ["Haematogenous spread from a distant focus",
      "The deck describes direct extension."],
     ["Nasolacrimal duct obstruction",
      "That underlies dacryocystitis."],
     ["Contact lens contamination",
      "That is a keratitis risk."]],
   c=0, cite=c(52)),

 dict(topic="Cellulitis", io=IOA, slot="etiology",
   q="In which patients does the deck say to consider a FUNGAL cause of orbital cellulitis?",
   opts=[
     ["Diabetic, elderly or immunocompromised patients — aspergillosis or mucormycosis",
      "Correct — the deck names the groups and the two organisms."],
     ["Contact lens wearers",
      "That is a bacterial and Acanthamoeba risk in keratitis."],
     ["Neonates",
      "The neonatal concern in this deck is gonococcal conjunctivitis."],
     ["Patients with rosacea",
      "That is a blepharitis association."]],
   c=0, cite=c(52)),

 dict(topic="Cellulitis", io=IOA, slot="differential",
   q="Which symptoms occur in POST-septal cellulitis but not pre-septal?",
   opts=[
     ["Difficulty and pain with eye movement, reduced vision, and diplopia",
      "Correct — the deck marks these as post-septal only."],
     ["Periocular pain, fever and chills",
      "Those occur in both."],
     ["Warmth of the tissue around the eye",
      "That occurs in both."],
     ["Lid erythema and oedema",
      "That occurs in both."]],
   c=0, cite=c(52)),

 dict(topic="Cellulitis", io=IOA, slot="test finding",
   q="The deck contrasts the two cellulitis photographs with one phrase. What is the giveaway in PRE-septal disease?",
   opts=[
     ["The eye itself is white, despite the swollen erythematous lid and periorbital area",
      "Correct — the deck's caption makes exactly this point."],
     ["The eye itself is red and cannot look down",
      "That is the post-septal photograph."],
     ["The pupil is fixed and mid-dilated",
      "That is acute angle closure."],
     ["There is a violaceous scleral patch",
      "That is scleritis."]],
   c=0, cite=c(52)),

 dict(topic="Cellulitis", io=IOA, slot="test finding",
   q="Which examination findings does the deck give for POST-septal (orbital) cellulitis?",
   opts=[
     ["Significant conjunctival injection, proptosis, decreased and painful extraocular movement, possible afferent pupillary defect and decreased vision",
      "Correct — the deck's full post-septal picture."],
     ["Balloon-like lid oedema with a white globe and full painless movements",
      "That is pre-septal disease."],
     ["Follicles with a tender preauricular node",
      "That is viral conjunctivitis."],
     ["A dendritic corneal ulcer",
      "That is herpes simplex keratitis."]],
   c=0, cite=c(52)),

 dict(topic="Cellulitis", io=IOA, slot="initial test",
   q="Which workup does the deck order for cellulitis?",
   opts=[
     ["Computed tomography of the orbits and paranasal sinuses with contrast, complete ocular examination including fundoscopy, Gram stain and culture of any open wound or drainage, a complete blood count with differential, and blood cultures",
      "Correct — the deck's full workup."],
     ["Computed tomography alone",
      "The deck orders considerably more."],
     ["Slit lamp examination with fluorescein alone",
      "That is the corneal workup."],
     ["Serum lipid profile and liver function tests",
      "That is xanthelasma."]],
   c=0, cite=c(53)),

 dict(topic="Cellulitis", io=IOA, slot="agent/regimen",
   q="How does the deck treat MILD pre-septal cellulitis?",
   opts=[
     ["Outpatient oral antibiotics for 10 to 14 days aimed at Staphylococcus, including resistant strains, and Streptococcus",
      "Correct — the deck's outpatient pathway and the organisms targeted."],
     ["Hospitalisation with broad-spectrum intravenous antibiotics for 48 to 72 hours",
      "That is for moderate-severe, non-compliant, young children, or any post-septal disease."],
     ["Topical antibiotic drops for seven days",
      "Insufficient for a tissue infection."],
     ["Oral antivirals for ten days",
      "That is herpetic keratitis."]],
   c=0, cite=c(53)),

 dict(topic="Cellulitis", io=IOB, slot="escalation",
   q="Which patients with PRE-septal cellulitis does the deck hospitalise?",
   opts=[
     ["Moderate to severe or toxic disease, concern for poor compliance, a child of five years or younger, or no improvement after oral antibiotics were started",
      "Correct — the deck's four admission criteria, and age five is the paediatric cut-off."],
     ["Every patient with pre-septal disease",
      "Mild disease is managed as an outpatient."],
     ["Only patients over sixty-five",
      "Age five is the threshold the deck names, at the other end."],
     ["Only contact lens wearers",
      "Not a criterion for cellulitis."]],
   c=0, cite=c(53)),

 dict(topic="Cellulitis", io=IOA, slot="complication",
   q="What does the deck say untreated cellulitis may spread to cause?",
   opts=[
     ["Intracranial spread causing meningitis or cavernous sinus thrombosis",
      "Correct — the deck's two named complications."],
     ["Corneal perforation and endophthalmitis",
      "That is the keratitis chain."],
     ["Entropion and trichiasis",
      "That is the trachoma chain."],
     ["Retinal detachment",
      "Not a cellulitis complication in this deck."]],
   c=0, cite=c(53)),

 dict(topic="Cellulitis", io=IOA, slot="referral",
   q="Which consults does the deck say may be needed in cellulitis?",
   opts=[
     ["Ear, nose and throat; oral and maxillofacial surgery; and infectious disease",
      "Correct — the deck's three, reflecting the sinus and dental sources."],
     ["Haematology and rheumatology",
      "Not the deck's consults for this."],
     ["Endocrinology and nephrology",
      "Not the deck's consults."],
     ["Dermatology alone",
      "Not what the deck lists."]],
   c=0, cite=c(53)),

 dict(topic="Cellulitis", io=IOA, slot="initial test",
   q="When do the speaker notes say a contrast scan is NOT routinely required in cellulitis?",
   opts=[
     ["In mild, clearly pre-septal disease with normal vision, normal pupils and painless full extraocular movements",
      "Correct — the notes qualify the slide's blanket imaging recommendation."],
     ["In any patient under five years old",
      "Young age pushes toward admission, not away from imaging."],
     ["In any patient who is febrile",
      "Fever does not remove the need."],
     ["Never — imaging is always required",
      "The notes explicitly allow clinical management in that group."]],
   c=0, cite=cn(53)),

 # ---- diagnostic modalities ----
 dict(topic="Slit lamp", io=IOA, slot="initial test",
   q="What is a slit lamp, and which structures does it examine?",
   opts=[
     ["A low-power microscope with a high-intensity light focused as a thin slit, examining the anterior structures — lids, cornea, conjunctiva, sclera and iris",
      "Correct — the deck's description of the instrument and its territory."],
     ["A hand-held light for viewing the retina and optic disc",
      "That is a direct ophthalmoscope."],
     ["An injected dye study of retinal blood flow",
      "That is fluorescein angiography."],
     ["A pressure-measuring pen applied to the cornea",
      "That is a tonometer."]],
   c=0, cite=c(7)),

 dict(topic="Ophthalmoscopy", io=IOA, slot="initial test",
   q="Which three types of ophthalmoscopy does the deck describe, and which is most commonly used?",
   opts=[
     ["Direct, indirect and slit-lamp ophthalmoscopy — slit-lamp is most common, because the patient is usually already seated there",
      "Correct — the three types and the practical reason for the third."],
     ["Direct, indirect and fluorescein — direct is most common",
      "Fluorescein examination is a separate modality."],
     ["Monocular, binocular and digital — digital is most common",
      "Not the deck's categories."],
     ["Direct and indirect only — indirect is most common",
      "The deck names three."]],
   c=0, cite=c(8)),

 dict(topic="Fluorescein examination", io=IOA, slot="initial test",
   q="How is a fluorescein examination performed, and what does it detect?",
   opts=[
     ["A yellow dye is instilled and the eye examined under a Wood lamp with ultraviolet light, detecting corneal abrasions, ulcers and foreign bodies",
      "Correct — the deck's method and its three targets."],
     ["Dye is injected into the arm and a blue-flash camera photographs the retina",
      "That is fluorescein ANGIOGRAPHY, a different test."],
     ["A drop of phenylephrine is instilled and the vessels observed for blanching",
      "That is the episcleritis test."],
     ["A pen tonometer is applied to the anaesthetised cornea",
      "That measures pressure."]],
   c=0, cite=c(9)),

 dict(topic="Fluorescein angiography", io=IOA, slot="initial test",
   q="How does fluorescein ANGIOGRAPHY differ from a fluorescein examination?",
   opts=[
     ["The dye is injected into the hand or arm, reaches the eye in about 10 to 15 seconds, and a blue-flash camera images blood flow in the retina and choroid",
      "Correct — injected rather than instilled, and it images flow rather than surface defects."],
     ["The dye is instilled as a drop and viewed with a Wood lamp",
      "That is the surface examination."],
     ["It uses iodine contrast and so is contraindicated in shellfish allergy",
      "The deck notes fluorescein has NO iodine."],
     ["It images the anterior chamber rather than the retina",
      "It images the posterior circulation."]],
   c=0, cite=c(10)),

 dict(topic="Fluorescein angiography", io=IOA, slot="education",
   q="What does the deck note about the safety of fluorescein angiography dye?",
   opts=[
     ["It is relatively safe and has no iodine",
      "Correct — the deck notes the absence of iodine explicitly."],
     ["It contains iodine and is contraindicated in renal impairment",
      "The deck says it has no iodine."],
     ["It is radioactive and requires shielding",
      "It is not radioactive."],
     ["It commonly causes anaphylaxis",
      "The deck describes it as relatively safe."]],
   c=0, cite=c(10)),

 dict(topic="Fluorescein angiography", io=IOA, slot="initial test",
   q="Which conditions does the deck say fluorescein angiography can detect?",
   opts=[
     ["Diabetic retinopathy, macular degeneration, macular oedema, ocular melanoma, retinal detachment and retinitis pigmentosa",
      "Correct — the deck's list, all posterior segment conditions."],
     ["Corneal abrasions, ulcers and foreign bodies",
      "Those are found by the surface fluorescein examination."],
     ["Cataract, dry eye and blepharitis",
      "Those are anterior and are found on slit lamp."],
     ["Orbital cellulitis and sinus disease",
      "Those need computed tomography."]],
   c=0, cite=c(10)),

 # ---- red eye triage ----
 dict(topic="Red eye triage", io=IOA, slot="initial test",
   q="What does the deck say to complete BEFORE naming a diagnosis in a red eye?",
   opts=[
     ["Visual acuity in each eye with correction, pupils, extraocular movements, corneal clarity and fluorescein staining, the pattern of injection and discharge, and the contact lens, trauma, surgery and steroid history",
      "Correct — the deck's first-60-seconds sequence."],
     ["Computed tomography of the orbits",
      "Imaging is not the first step in a red eye."],
     ["A complete blood count and blood cultures",
      "Those belong to the cellulitis workup."],
     ["Referral to ophthalmology before any examination",
      "The deck asks for the examination first."]],
   c=0, cite=c(67)),

 dict(topic="Red eye triage", io=IOA, slot="test finding",
   q="Which two findings does the deck single out as red flags in a red eye?",
   opts=[
     ["Reduced vision or an abnormal pupil",
      "Correct — the deck highlights exactly these two."],
     ["Watery discharge or itching",
      "Those point toward benign causes."],
     ["Bilateral involvement or crusting",
      "Neither is a red flag in the deck."],
     ["Preauricular node or follicles",
      "Those indicate a cause rather than danger."]],
   c=0, cite=c(67)),

 dict(topic="Red eye triage", io=IOA, slot="education",
   q="What warning do the speaker notes attach to the red-eye examination?",
   opts=[
     ["Do not let obvious redness substitute for an eye examination",
      "Correct — the notes' phrasing, and the whole point of the sequence."],
     ["Do not examine the eye until acuity is documented by an optometrist",
      "Not the notes' warning."],
     ["Do not use fluorescein before ophthalmology has been consulted",
      "Fluorescein is part of the first-60-seconds sequence."],
     ["Do not measure acuity in a painful eye",
      "Acuity is the first thing the deck asks for."]],
   c=0, cite=cn(67)),

 dict(topic="Red eye triage", io=IOA, slot="initial test",
   q="Which is the ONE exception to the normal red-eye sequence, per the speaker notes?",
   opts=[
     ["Chemical exposure — begin copious irrigation before the history or examination, then verify the surface pH has normalised",
      "Correct — the notes' single named exception."],
     ["Contact lens wear — remove the lens before any history",
      "Lens removal matters, but the notes' stated exception is chemical exposure."],
     ["Trauma — obtain imaging before examining",
      "Not the notes' exception."],
     ["Fever — obtain blood cultures before examining",
      "Not the notes' exception."]],
   c=0, cite=cn(67)),

 dict(topic="Red eye danger signs", io=IOA, slot="referral",
   q="Which findings does the deck say should stop the reflex diagnosis of conjunctivitis?",
   opts=[
     ["Moderate to severe pain or consensual photophobia, reduced acuity or an abnormal pupil, corneal opacity or dendrite, ciliary flush or hypopyon, proptosis or restricted movement, chemical or penetrating injury, and a contact lens wearer with pain",
      "Correct — the deck's danger-sign list."],
     ["Bilateral redness with watery discharge and itching",
      "Those point to benign allergic or viral disease."],
     ["Crusting of the lids on waking",
      "Common in benign conjunctivitis."],
     ["A tender preauricular node",
      "That indicates viral or chlamydial cause, not danger."]],
   c=0, cite=c(68)),

 dict(topic="Red eye danger signs", io=IOA, slot="test finding",
   q="What is CONSENSUAL photophobia, and what does it support?",
   opts=[
     ["Pain in the affected eye when light is shone in the UNAFFECTED eye — it supports anterior uveitis",
      "Correct — the notes define it and assign it."],
     ["Pain in both eyes when light is shone in either — it supports conjunctivitis",
      "Not the definition, and conjunctivitis does not do this."],
     ["Pain only when light is shone in the affected eye — it supports keratitis",
      "That is ordinary direct photophobia."],
     ["Pain on eye movement — it supports optic neuritis",
      "That is a different sign."]],
   c=0, cite=cn(68)),

 dict(topic="Red eye danger signs", io=IOA, slot="escalation",
   q="What do the notes say to do for a suspected OPEN GLOBE?",
   opts=[
     ["Place a rigid eye shield, avoid pressure, manipulation and tonometry, keep the patient nil by mouth, and obtain emergency ophthalmology consultation",
      "Correct — the notes' five protective actions."],
     ["Irrigate copiously before doing anything else",
      "That is the chemical injury protocol."],
     ["Measure the intraocular pressure to assess the damage",
      "Tonometry is specifically contraindicated."],
     ["Patch the eye firmly and arrange next-day review",
      "Pressure on the globe is exactly what must be avoided."]],
   c=0, cite=cn(68)),

 dict(topic="Red eye localisation", io=IOA, slot="differential",
   q="Which pattern localises the problem to the CONJUNCTIVA?",
   opts=[
     ["Itch or discharge with diffuse injection and preserved vision",
      "Correct — the deck's conjunctival pattern."],
     ["Pain and photophobia with a fluorescein defect or infiltrate",
      "That localises to the cornea."],
     ["Consensual photophobia with ciliary flush and an irregular pupil",
      "That localises to the anterior chamber."],
     ["Deep pain or painful eye movement with a violaceous sclera",
      "That localises to sclera or orbit."]],
   c=0, cite=c(69)),

 dict(topic="Red eye localisation", io=IOA, slot="differential",
   q="Which pattern localises the problem to the ANTERIOR CHAMBER?",
   opts=[
     ["Consensual photophobia, ciliary flush and an irregular pupil",
      "Correct — the deck's anterior chamber pattern."],
     ["Itch and discharge with diffuse injection",
      "That is conjunctival."],
     ["Pain with headache, halos and nausea, with a cloudy cornea",
      "That is angle closure."],
     ["Proptosis with restricted movement",
      "That is orbital."]],
   c=0, cite=c(69)),

 dict(topic="Red eye localisation", io=IOA, slot="differential",
   q="Which pattern localises the problem to ANGLE CLOSURE?",
   opts=[
     ["Pain or headache with halos and nausea, a cloudy cornea and a mid-dilated pupil",
      "Correct — the deck's angle closure pattern."],
     ["Itch with stringy discharge and preserved vision",
      "That is allergic conjunctivitis."],
     ["Foreign body sensation with a fluorescein-staining defect",
      "That is corneal."],
     ["Deep boring pain radiating to the face",
      "That is scleritis."]],
   c=0, cite=c(69)),

 # ---- disposition ----
 dict(topic="Referral timing", io=IOA, slot="referral",
   q="Which conditions does the deck put in the EMERGENT — now — category?",
   opts=[
     ["Chemical injury (irrigate first), open globe, angle closure, orbital cellulitis and endophthalmitis",
      "Correct — the deck's five emergent conditions."],
     ["Keratitis, corneal ulcer, anterior uveitis, scleritis and ocular herpes zoster",
      "Those are the SAME DAY group."],
     ["Unexplained decreased vision and persistent pain or photophobia",
      "Those are the URGENT, 24 to 48 hour group."],
     ["Uncomplicated conjunctivitis and chronic eyelid disease",
      "Those are ROUTINE."]],
   c=0, cite=c(70)),

 dict(topic="Referral timing", io=IOA, slot="referral",
   q="Which conditions does the deck put in the SAME DAY category?",
   opts=[
     ["Keratitis or corneal ulcer, anterior uveitis, scleritis, and ocular herpes zoster ophthalmicus",
      "Correct — the deck's same-day group."],
     ["Chemical injury, open globe and angle closure",
      "Those are emergent."],
     ["Uncomplicated conjunctivitis",
      "That is routine."],
     ["Chronic ocular surface disease",
      "That is routine."]],
   c=0, cite=c(70)),

 dict(topic="Referral timing", io=IOA, slot="referral",
   q="When is ROUTINE follow-up appropriate for a red eye, per the speaker notes?",
   opts=[
     ["Only when acuity is preserved, pupils and movements are normal, the cornea is clear without uptake or infiltrate, significant pain and photophobia are absent, and follow-up is reliable",
      "Correct — the notes' five conditions, all of which must hold."],
     ["Whenever the patient has no discharge",
      "Far too permissive."],
     ["Whenever the redness is bilateral",
      "Laterality does not establish safety."],
     ["Whenever the patient is under forty",
      "Age is not a criterion."]],
   c=0, cite=cn(70)),

 dict(topic="Referral timing", io=IOA, slot="education",
   q="What does the deck say every red-eye assessment should end with?",
   opts=[
     ["A clearly documented disposition and a safety-net plan — recording acuity, key negatives, suspected diagnosis, urgency, destination and explicit return precautions",
      "Correct — the notes' documentation standard."],
     ["A prescription for a topical antibiotic",
      "Not every red eye needs one."],
     ["An appointment with ophthalmology within 24 hours",
      "Only some categories need that."],
     ["A referral for computed tomography",
      "Not routinely indicated."]],
   c=0, cite=cn(70)),

 # ---- the contact lens case ----
 dict(topic="Contact lens keratitis", io=IOA, slot="first-line",
   q="A contact lens wearer has severe unilateral pain, photophobia and blurred vision after sleeping in lenses, with a central epithelial defect and a white infiltrate. What are the immediate next steps?",
   opts=[
     ["Remove the lenses without patching, give no take-home topical anaesthetic or corticosteroid, arrange same-day ophthalmology evaluation, and preserve the lenses and case if culture is wanted",
      "Correct — the deck's four next steps for its own worked case."],
     ["Patch the eye, give a topical anaesthetic for comfort, and review in two days",
      "Patching and take-home anaesthetic are both specifically prohibited."],
     ["Start a topical corticosteroid and review next week",
      "Steroids can worsen uncontrolled infection."],
     ["Reassure and treat as viral conjunctivitis",
      "The deck says this is microbial keratitis until proven otherwise."]],
   c=0, cite=c(71)),

 dict(topic="Contact lens keratitis", io=IOA, slot="avoid",
   q="Why do the speaker notes forbid dispensing a topical anaesthetic for home use?",
   opts=[
     ["It delays healing and masks progression",
      "Correct — the notes give both reasons."],
     ["It causes an allergic reaction in most patients",
      "Not the notes' reason."],
     ["It raises intraocular pressure",
      "That is a corticosteroid effect."],
     ["It interferes with culture results",
      "Not the notes' stated reason."]],
   c=0, cite=cn(71)),

 dict(topic="Contact lens keratitis", io=IOA, slot="escalation",
   q="What do the notes say if same-day ophthalmology evaluation is unavoidably delayed?",
   opts=[
     ["Consult ophthalmology immediately about empiric topical antipseudomonal therapy, and do not delay necessary treatment solely to obtain a culture",
      "Correct — the notes are explicit that culture must not hold up treatment."],
     ["Wait for the culture result before starting anything",
      "The notes say the opposite."],
     ["Start a topical corticosteroid while waiting",
      "Specifically prohibited."],
     ["Patch the eye and review in 48 hours",
      "Patching is prohibited."]],
   c=0, cite=cn(71)),

 dict(topic="Contact lens keratitis", io=IOA, slot="education",
   q="What safety-net advice do the notes give this patient?",
   opts=[
     ["Escalate immediately for increasing pain, an enlarging opacity, worsening photophobia, or further visual decline",
      "Correct — the notes' four escalation triggers."],
     ["Return only if the eye is still red in one week",
      "Far too slow for microbial keratitis."],
     ["Resume lens wear once the pain settles",
      "Lenses must stay out."],
     ["No specific advice is needed once referral is arranged",
      "The notes require an explicit safety net."]],
   c=0, cite=cn(71)),
]
