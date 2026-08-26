# -*- coding: utf-8 -*-
# CMS I Exam 2, Lecture 1 -- vignette pool B.
#
# THIS POOL CARRIES THE DIAGNOSIS LEAD-INS. Prof. Jaquith said there is "SOME
# diagnosis but A LOT are next management plan / first line treatment / patient
# education", so the partition caps diagnosis at 20 per cent of each set and
# draws the rest from the other lead types. Pool A is almost entirely
# non-diagnosis; this pool supplies both.
#
# EVERY STEM STANDS ALONE -- no vignette may refer to another question.
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

VIG_B = [
 # ---- diagnosis lead-ins ----
 dict(topic="Episcleritis vs scleritis", io=IOA, lead="diagnosis", slot="differential",
   q="A 33-year-old woman has a sectoral patch of redness in one eye with mild ache, no discharge and no photophobia. After topical anaesthesia the redness moves slightly when nudged with a cotton-tip applicator. Which is the most likely diagnosis?",
   opts=[
     ["Episcleritis", "Correct — mobile vessels, mild pain and no photophobia point to the superficial layer."],
     ["Scleritis", "Scleral vessels cannot be moved, and the pain would be severe and boring."],
     ["Bacterial conjunctivitis", "That gives diffuse redness with thick discharge."],
     ["Anterior uveitis", "That gives ciliary flush, photophobia and an irregular pupil."]],
   c=0, cite=c(47)),

 dict(topic="Scleritis", io=IOA, lead="diagnosis", slot="differential",
   q="A 49-year-old woman with long-standing rheumatoid arthritis has severe deep eye pain that wakes her at night and radiates to her face. There is a bluish-purple patch on the white of the eye and the vessels will not move with a cotton-tip applicator. Which is the most likely diagnosis?",
   opts=[
     ["Scleritis", "Correct — night pain, violaceous hue and immobile vessels, on an autoimmune background."],
     ["Episcleritis", "The pain would be mild and the vessels would move."],
     ["Subconjunctival haemorrhage", "That is a painless flat red patch."],
     ["Viral conjunctivitis", "That has watery discharge, follicles and a preauricular node."]],
   c=0, cite=c(49)),

 dict(topic="Subconjunctival haemorrhage", io=IOA, lead="diagnosis", slot="differential",
   q="A 66-year-old man on warfarin notices a bright red patch on the white of one eye after a coughing fit. There is no pain, vision is normal, the pupil is normal and the cornea is clear. Which is the most likely diagnosis?",
   opts=[
     ["Subconjunctival haemorrhage",
      "Correct — Valsalva plus anticoagulation, and the eye is otherwise entirely normal."],
     ["Bacterial conjunctivitis",
      "That has discharge and diffuse hyperaemia rather than a discrete blood patch."],
     ["Anterior uveitis",
      "That is painful, with ciliary flush and photophobia."],
     ["Scleritis",
      "That is severely painful with a violaceous rather than bright red appearance."]],
   c=0, cite=c(29)),

 dict(topic="Pterygium", io=IOA, lead="diagnosis", slot="differential",
   q="A 44-year-old fisherman has a fleshy triangular growth on the nasal conjunctiva of one eye that now extends a short distance onto the cornea. Which is the most likely diagnosis?",
   opts=[
     ["Pterygium", "Correct — corneal extension is what makes it a pterygium rather than a pinguecula."],
     ["Pinguecula", "A pinguecula stops at the limbus and does not involve the cornea."],
     ["Corneal ulcer", "That is a painful open sore, not a fleshy growth."],
     ["Chalazion", "That is a lid nodule."]],
   c=0, cite=c(27)),

 dict(topic="Pinguecula", io=IOA, lead="diagnosis", slot="differential",
   q="A 51-year-old outdoor worker has a yellowish raised nodule on the conjunctiva at the three o'clock position of one eye. It stops at the edge of the cornea and does not encroach on it. Which is the most likely diagnosis?",
   opts=[
     ["Pinguecula", "Correct — it sits at the classic position and spares the cornea."],
     ["Pterygium", "A pterygium extends onto the cornea."],
     ["Xanthelasma", "That is a lid lesion, not conjunctival."],
     ["Episcleritis", "That is inflammatory redness, not a nodule."]],
   c=0, cite=c(27)),

 dict(topic="Hordeolum", io=IOA, lead="diagnosis", slot="differential",
   q="A 24-year-old woman developed a painful, tender, red lump at the margin of her lower eyelid overnight. Which is the most likely diagnosis?",
   opts=[
     ["Hordeolum", "Correct — acute onset over 24 hours, tender, and at the lid margin."],
     ["Chalazion", "That is non-tender and develops over days to weeks."],
     ["Dacryocystitis", "That sits over the lacrimal sac at the inner corner of the lower lid."],
     ["Xanthelasma", "That is a painless yellow plaque."]],
   c=0, cite=c(20)),

 dict(topic="Dacryoadenitis vs dacryocystitis", io=IOA, lead="diagnosis", slot="differential",
   q="A 39-year-old man has pain, redness and swelling confined to the outer third of his upper eyelid, with an enlarged node in front of the ear on the same side. Which is the most likely diagnosis?",
   opts=[
     ["Dacryoadenitis", "Correct — the lacrimal gland sits superotemporally, and preauricular nodes are described."],
     ["Dacryocystitis", "That produces swelling over the lacrimal sac, at the inner lower lid."],
     ["Pre-septal cellulitis", "That produces diffuse balloon-like lid swelling, not a localised outer-third mass."],
     ["Hordeolum", "That is a small tender nodule at the lash line."]],
   c=0, cite=c(22)),

 dict(topic="Dacryocystitis", io=IOA, lead="diagnosis", slot="differential",
   q="A 71-year-old woman has a tender, tense, erythematous swelling over the nasal aspect of her lower eyelid, below the medial canthal tendon, with mucoid material expressible from the lower punctum. Which is the most likely diagnosis?",
   opts=[
     ["Dacryocystitis", "Correct — the location below the tendon and the expressible discharge are both characteristic."],
     ["A lacrimal sac tumour", "That would be suspected if the mass were ABOVE the medial canthal tendon."],
     ["Dacryoadenitis", "That affects the gland at the outer upper lid."],
     ["Chalazion", "That is a painless nodule within the lid itself."]],
   c=0, cite=c(24)),

 dict(topic="Orbital vs pre-septal cellulitis", io=IOA, lead="diagnosis", slot="differential",
   q="A 34-year-old man has a swollen, red, tender left eyelid and fever after sinusitis. The globe is white, the pupil reacts normally, and eye movements are full and painless with normal vision. Which is the most likely diagnosis?",
   opts=[
     ["Pre-septal (periorbital) cellulitis",
      "Correct — a white globe with full painless movements and normal vision places the infection in front of the septum."],
     ["Post-septal (orbital) cellulitis",
      "That would show proptosis, painful restricted movement, and often reduced vision."],
     ["Dacryocystitis",
      "That is localised to the lacrimal sac at the inner lower lid."],
     ["Allergic conjunctivitis",
      "That itches, is bilateral, and does not cause fever."]],
   c=0, cite=c(52)),

 dict(topic="Orbital cellulitis", io=IOA, lead="diagnosis", slot="differential",
   q="A 29-year-old woman has a swollen red eyelid, fever, and pain on eye movement. The eye is pushed forward, movements are restricted, and she reports double vision and blurring. Which is the most likely diagnosis?",
   opts=[
     ["Post-septal (orbital) cellulitis",
      "Correct — proptosis, painful restricted movement and reduced vision are all post-septal features."],
     ["Pre-septal (periorbital) cellulitis",
      "That spares eye movement and vision."],
     ["Anterior uveitis",
      "That does not cause proptosis or fever."],
     ["Acute allergic conjunctivitis",
      "That itches and does not restrict eye movement."]],
   c=0, cite=c(52)),

 dict(topic="Keratitis", io=IOA, lead="diagnosis", slot="differential",
   q="A 21-year-old woman who sleeps in her contact lenses has severe unilateral eye pain, photophobia and blurred vision. The cornea is hazy so the iris details cannot be seen clearly, and there is a ring of redness at the corneal edge that does not spare the limbus. Which is the most likely diagnosis?",
   opts=[
     ["Bacterial keratitis", "Correct — corneal haze with ciliary flush in a lens overwearer."],
     ["Viral conjunctivitis", "That gives watery discharge and follicles with a clear cornea."],
     ["Subconjunctival haemorrhage", "That is painless with a clear cornea and normal vision."],
     ["Episcleritis", "That gives mild sectoral redness with a clear cornea and no photophobia."]],
   c=0, cite=c(55)),

 dict(topic="Herpes simplex vs zoster keratitis", io=IOA, lead="diagnosis", slot="differential",
   q="A 74-year-old man with a painful dermatomal rash across one side of his forehead has corneal lesions on fluorescein that branch but lack elevated edges and have no knobs at the branch tips. Which is the most likely diagnosis?",
   opts=[
     ["Herpes zoster keratitis", "Correct — pseudodendrites lack the elevated edges and terminal end bulbs of a true dendrite."],
     ["Herpes simplex keratitis", "A true simplex dendrite HAS terminal end bulbs and elevated edges."],
     ["Acanthamoeba keratitis", "That gives a ring infiltrate in a contact lens wearer."],
     ["Bacterial keratitis", "That gives a white infiltrate rather than a branching pattern."]],
   c=0, cite=c(57)),

 dict(topic="Trachoma", io=IOA, lead="diagnosis", slot="differential",
   q="A 30-year-old man who grew up in a region with poor sanitation has inturned eyelashes rubbing his cornea, with scarring of the upper eyelid and a history of repeated childhood eye infections. Which is the most likely diagnosis?",
   opts=[
     ["Trachoma", "Correct — repeated chlamydial infection scars the lid, causing entropion and then trichiasis."],
     ["Adult inclusion conjunctivitis", "That produces follicles and chronic discharge without lid scarring."],
     ["Blepharitis", "That produces crusting at the lash bases, not scarring and lid inversion."],
     ["Bacterial conjunctivitis", "That is acute and does not scar the lid."]],
   c=0, cite=c(46)),

 dict(topic="Conjunctivitis type", io=IOA, lead="diagnosis", slot="differential",
   q="A 20-year-old woman has bilateral red, intensely itchy eyes with swollen lids and stringy watery discharge every April. Vision is normal, the corneas are clear, and there is no preauricular node. Which is the most likely diagnosis?",
   opts=[
     ["Acute allergic conjunctivitis", "Correct — itch, bilaterality, seasonality and stringy discharge, with no node."],
     ["Acute viral conjunctivitis", "That gives profuse watery discharge WITH a tender preauricular node."],
     ["Acute bacterial conjunctivitis", "That gives thick yellow discharge and is often unilateral."],
     ["Chlamydial conjunctivitis", "That runs chronically for a month or more."]],
   c=0, cite=c(34)),

 # ---- non-diagnosis lead-ins ----
 dict(topic="Entropion", io=IOA, lead="next step", slot="initial test",
   q="An 82-year-old woman reports a constant foreign body sensation in one eye. The lower lid margin turns inward and the lashes contact the globe. Which examination is most appropriate?",
   opts=[
     ["Slit lamp examination to assess whether the cornea has been involved",
      "Correct — the question with entropion is always whether the lashes have damaged the cornea."],
     ["Computed tomography of the orbits with contrast",
      "Imaging is not indicated for lid malposition."],
     ["Fluorescein angiography",
      "That images retinal blood flow."],
     ["Serum lipid profile",
      "That belongs to xanthelasma."]],
   c=0, cite=c(13)),

 dict(topic="Ectropion", io=IOA, lead="first-line", slot="first-line",
   q="A 79-year-old man has a lower eyelid that sags outward, with constant tearing and exposure of the inner lid surface. Which is the most appropriate initial management while awaiting definitive treatment?",
   opts=[
     ["Preservative-free artificial tears during the day, lubricating ointment at night, and taping the lid into place",
      "Correct — the deck's conservative measures, protecting the exposed surface until surgery."],
     ["Topical antibiotic drops four times daily",
      "There is no infection."],
     ["Topical corticosteroid drops",
      "Not indicated for lid malposition."],
     ["Oral antibiotics for ten days",
      "That is the cellulitis regimen."]],
   c=0, cite=c(13)),

 dict(topic="Ectropion", io=IOA, lead="education", slot="escalation",
   q="A 77-year-old woman with ectropion asks what will actually fix it. What is the most accurate answer?",
   opts=[
     ["Surgery is the definitive treatment; lubrication only protects the surface in the meantime",
      "Correct — the deck names surgery as definitive."],
     ["Lubricating ointment used consistently will correct the lid position",
      "Lubrication protects but does not reposition the lid."],
     ["It will resolve on its own within two to four weeks",
      "That timescale belongs to a subconjunctival haemorrhage."],
     ["A course of oral antibiotics will resolve it",
      "There is no infection."]],
   c=0, cite=c(13)),

 dict(topic="Dermatochalasis", io=IOA, lead="initial test", slot="initial test",
   q="A 68-year-old man complains that his upper lids feel heavy and he is looking through his lashes. There are excess folds of skin over both upper lids. Which assessment most directly determines whether surgery will be covered?",
   opts=[
     ["Visual field testing",
      "Correct — a demonstrated field deficit is what the deck ties to insurance coverage for blepharoplasty."],
     ["Intraocular pressure measurement",
      "Not relevant to lid skin redundancy."],
     ["Slit lamp examination with fluorescein",
      "That assesses the cornea."],
     ["Computed tomography of the orbits",
      "Not indicated."]],
   c=0, cite=c(15)),

 dict(topic="Xanthelasma", io=IOA, lead="next step", slot="initial test",
   q="A 47-year-old woman has soft yellowish oval plaques on the inner aspect of both upper eyelids. They are asymptomatic. Which workup is most appropriate?",
   opts=[
     ["Serum lipid profile, together with tests for diabetes mellitus and liver function",
      "Correct — the deck treats these plaques as a marker of an underlying metabolic disorder."],
     ["Serum lipid profile alone",
      "The deck also checks glucose, haemoglobin A1C and liver function."],
     ["Complete blood count with differential and blood cultures",
      "That is the cellulitis workup."],
     ["No workup — the lesions are purely cosmetic",
      "The deck directs treatment at the underlying metabolic issue."]],
   c=0, cite=c(17)),

 dict(topic="Xanthelasma", io=IOA, lead="education", slot="prognosis",
   q="A 53-year-old man is considering laser ablation for xanthelasma. What should he be told about the outcome?",
   opts=[
     ["Even after effective local treatment, recurrences are common",
      "Correct — the deck flags recurrence explicitly."],
     ["Local treatment is curative and recurrence is rare",
      "The deck says the opposite."],
     ["The lesions will resolve on their own if left alone",
      "The deck does not describe spontaneous resolution."],
     ["The lesions will become malignant if not removed",
      "They are benign deposits."]],
   c=0, cite=c(17)),

 dict(topic="Subconjunctival haemorrhage", io=IOA, lead="next step", slot="initial test",
   q="A 59-year-old man has a painless bright red patch on the white of one eye with no obvious precipitant and no medication history to explain it. Vision, pupil and cornea are all normal. Which is the most appropriate next step?",
   opts=[
     ["Take a careful history and check his blood pressure",
      "Correct — the deck calls history super important and names the blood pressure check when there is no explanation."],
     ["Refer urgently to ophthalmology",
      "The eye findings are benign."],
     ["Start a topical antibiotic",
      "There is no infection."],
     ["Order computed tomography of the orbits",
      "Not indicated."]],
   c=0, cite=c(30)),

 dict(topic="Subconjunctival haemorrhage", io=IOA, lead="education", slot="prognosis",
   q="A 64-year-old woman with an atraumatic subconjunctival haemorrhage wants to know when the redness will go. What should she be told?",
   opts=[
     ["It usually resolves spontaneously within two to four weeks; reassurance is the treatment",
      "Correct — the deck's timeframe, and no active treatment is needed."],
     ["It should clear within 24 to 48 hours",
      "Much faster than the deck's stated course."],
     ["It will leave a permanent mark on the eye",
      "The deck describes full resolution."],
     ["It will need antibiotic drops to clear",
      "There is no infection."]],
   c=0, cite=c(30)),

 dict(topic="Pterygium", io=IOA, lead="next step", slot="referral",
   q="A 46-year-old surfer has a fleshy growth extending onto the cornea of one eye that has grown over the past year, and he now notices his vision is distorted. Which is the most appropriate next step?",
   opts=[
     ["Non-urgent referral to ophthalmology for slit lamp assessment of the adjacent cornea",
      "Correct — growth or reported vision impairment is exactly the deck's referral trigger, and it is non-urgent."],
     ["Emergent same-day referral",
      "The deck classes this referral as non-urgent."],
     ["Reassurance with no referral, since it is benign",
      "Growth and vision change are the two triggers to refer."],
     ["Start a topical corticosteroid",
      "Not part of the deck's management."]],
   c=0, cite=c(28)),

 dict(topic="Pterygium", io=IOA, lead="education", slot="education",
   q="A 39-year-old man with a pterygium asks whether lubricating drops and sunglasses will get rid of it. What is the most accurate answer?",
   opts=[
     ["Conservative management may control symptoms but will not make the lesion resolve",
      "Correct — the deck is explicit on this point."],
     ["Drops and sun protection will clear it within a few months",
      "The deck says conservative measures do not resolve it."],
     ["It will resolve on its own once sun exposure stops",
      "The deck describes no spontaneous resolution."],
     ["Only oral medication will shrink it",
      "There is no oral treatment in this deck."]],
   c=0, cite=c(28)),

 dict(topic="Chemosis", io=IOA, lead="next step", slot="referral",
   q="A 43-year-old woman has swelling of the conjunctiva itself in one eye, together with forward displacement of the globe and restricted eye movement. Which is the most appropriate next step?",
   opts=[
     ["Treat this as urgent — proptosis and restricted movement alongside chemosis are red flags",
      "Correct — the speaker notes name exactly these accompaniments as urgent."],
     ["Reassure her, as chemosis is a non-specific sign of irritation",
      "It is non-specific alone, but not with these accompaniments."],
     ["Prescribe a topical antihistamine and review in a week",
      "That would be reasonable for isolated allergic chemosis only."],
     ["Prescribe artificial tears and review in a month",
      "Far too slow given the orbital signs."]],
   c=0, cite=cn(31)),

 dict(topic="Autoimmune conjunctivitis", io=IOA, lead="next step", slot="referral",
   q="A 52-year-old woman with Sjögren disease has recurrent diffuse redness of both eyes with minimal discomfort and no discharge, alongside malaise and fatigue. Which is the most appropriate next step?",
   opts=[
     ["Routine referral to ophthalmology",
      "Correct — the deck manages autoimmune conjunctivitis with routine referral."],
     ["Emergent referral the same day",
      "There are no danger signs described."],
     ["A course of topical antibiotics",
      "There is no infection."],
     ["Oral doxycycline for seven days",
      "That treats chlamydial conjunctivitis."]],
   c=0, cite=c(39)),

 dict(topic="Red eye triage", io=IOA, lead="next step", slot="initial test",
   q="A 36-year-old man presents with a red eye. Before deciding what is wrong, which assessment does the lecture say to complete first?",
   opts=[
     ["Visual acuity in each eye with correction, pupils, extraocular movements, corneal clarity with fluorescein, the pattern of injection and discharge, and the contact lens, trauma, surgery and steroid history",
      "Correct — the deck's first-60-seconds sequence, completed before naming a diagnosis."],
     ["Computed tomography of the orbits with contrast",
      "Imaging is not the first step in a red eye."],
     ["A trial of topical antibiotic for 48 hours",
      "Treating before examining is what the deck warns against."],
     ["Immediate referral without examination",
      "The deck asks for the examination first."]],
   c=0, cite=c(67)),

 dict(topic="Red eye triage", io=IOA, lead="next step", slot="escalation",
   q="A 27-year-old man has splashed drain cleaner into one eye and arrives in distress. Which is the most appropriate immediate action?",
   opts=[
     ["Begin copious irrigation immediately, before completing the history or examination, then check that the surface pH has normalised",
      "Correct — chemical exposure is the single stated exception to the normal red-eye sequence."],
     ["Measure visual acuity in both eyes first, then irrigate",
      "Irrigation must not wait for acuity in a chemical injury."],
     ["Obtain the full history first, then irrigate",
      "The notes are explicit that irrigation comes first."],
     ["Patch the eye and arrange same-day ophthalmology review",
      "Delaying irrigation risks the eye."]],
   c=0, cite=cn(67)),

 dict(topic="Red eye triage", io=IOA, lead="next step", slot="avoid",
   q="A 44-year-old man has a penetrating eye injury from a metal fragment and a suspected open globe. Which action should be taken?",
   opts=[
     ["Place a rigid eye shield, avoid any pressure or tonometry, keep him nil by mouth, and obtain emergency ophthalmology consultation",
      "Correct — the notes' protective sequence for a suspected open globe."],
     ["Measure the intraocular pressure to assess the damage",
      "Tonometry is specifically contraindicated with a suspected open globe."],
     ["Patch the eye firmly and arrange next-day review",
      "Pressure on the globe is exactly what must be avoided."],
     ["Irrigate copiously before doing anything else",
      "That is the chemical injury protocol, not the open globe one."]],
   c=0, cite=cn(68)),

 dict(topic="Red eye triage", io=IOA, lead="next step", slot="referral",
   q="A 30-year-old woman has a red eye with normal visual acuity, normal pupils and eye movements, a clear cornea with no fluorescein uptake, no significant pain or photophobia, and reliable follow-up. Which disposition is appropriate?",
   opts=[
     ["Routine follow-up", "Correct — all five of the notes' conditions for routine care are met."],
     ["Emergent referral now", "None of the emergent features is present."],
     ["Same-day ophthalmology evaluation", "No same-day condition is described."],
     ["Urgent referral within 24 to 48 hours", "That category is for unexplained findings, and there are none here."]],
   c=0, cite=cn(70)),

 dict(topic="Conjunctivitis pattern", io=IOA, lead="test finding", slot="test finding",
   q="A 31-year-old man with a chronically red eye has pale bumps on the inner surface of the lower lid that look redder at their base. What do these indicate?",
   opts=[
     ["Follicles, which point to a chlamydial or viral cause",
      "Correct — follicles are pale at the surface and redder at the base."],
     ["Papillae, which point to a bacterial or allergic cause",
      "Papillae are red at the surface and paler at the base — the reverse pattern."],
     ["Keratic precipitates, which point to anterior uveitis",
      "Those sit on the corneal endothelium, not the lid."],
     ["Drusen, which point to macular degeneration",
      "Those are retinal."]],
   c=0, cite=c(33)),

 dict(topic="Conjunctivitis pattern", io=IOA, lead="test finding", slot="test finding",
   q="A 26-year-old woman with itchy bilateral red eyes has bumps on the inner lid surface that are red at the surface and paler at the base. What do these indicate?",
   opts=[
     ["Papillae, which point to a bacterial or allergic cause",
      "Correct — papillae are red at the surface and paler at the base."],
     ["Follicles, which point to a chlamydial or viral cause",
      "Follicles are the reverse — pale at the surface, redder at the base."],
     ["Keratic precipitates, which point to anterior uveitis",
      "Those are on the cornea."],
     ["Hard exudates, which point to diabetic retinopathy",
      "Those are retinal."]],
   c=0, cite=c(33)),

 dict(topic="Slit lamp", io=IOA, lead="initial test", slot="initial test",
   q="A 48-year-old woman needs the front of her eye examined in magnified detail — the lids, cornea, conjunctiva, sclera and iris. Which instrument is designed for this?",
   opts=[
     ["A slit lamp", "Correct — a low-power microscope with a high-intensity slit beam for the anterior structures."],
     ["A direct ophthalmoscope", "That is for the innermost structures, including the retina and optic disc."],
     ["A tonometer pen", "That measures intraocular pressure."],
     ["A Wood lamp", "That provides the ultraviolet light for a fluorescein examination."]],
   c=0, cite=c(7)),

 dict(topic="Fluorescein", io=IOA, lead="initial test", slot="initial test",
   q="A 35-year-old man may have a corneal abrasion after a fingernail injury. Which examination will best demonstrate it?",
   opts=[
     ["Instil fluorescein and examine under a Wood lamp with ultraviolet light",
      "Correct — the surface fluorescein examination detects abrasions, ulcers and foreign bodies."],
     ["Inject fluorescein intravenously and photograph the retina with a blue flash",
      "That is fluorescein ANGIOGRAPHY, which images the posterior circulation."],
     ["Instil phenylephrine and observe for blanching",
      "That is the episcleritis test."],
     ["Measure intraocular pressure",
      "That does not show a surface defect."]],
   c=0, cite=c(9)),

 dict(topic="Fluorescein angiography", io=IOA, lead="education", slot="education",
   q="A 60-year-old woman is anxious about the dye for fluorescein angiography because she reacted to contrast for a scan once. What is accurate to tell her?",
   opts=[
     ["Fluorescein contains no iodine and is relatively safe",
      "Correct — the deck notes the absence of iodine explicitly."],
     ["It contains iodine, so her previous reaction is a contraindication",
      "The deck states it has no iodine."],
     ["It is radioactive and requires shielding",
      "It is not radioactive."],
     ["It is injected into the eye itself",
      "It is injected into the hand or arm."]],
   c=0, cite=c(10)),

 dict(topic="Bacterial conjunctivitis", io=IOA, lead="education", slot="education",
   q="A 33-year-old teacher has been started on drops for acute bacterial conjunctivitis. Which advice is most appropriate?",
   opts=[
     ["Take contagious precautions with careful hand hygiene, and expect progressive improvement within days",
      "Correct — the deck pairs the precautions with the expected prompt response."],
     ["No precautions are needed as bacterial conjunctivitis is not contagious",
      "The deck specifically requires contagious precautions."],
     ["Expect it to worsen over the first week before improving",
      "That is the viral course."],
     ["Expect it to take two to three weeks to settle",
      "That is also the viral course."]],
   c=0, cite=c(41)),

 dict(topic="Anterior uveitis", io=IOA, lead="first-line", slot="first-line",
   q="A 37-year-old woman with confirmed non-infectious anterior uveitis is under ophthalmology care. Which treatment does the lecture describe as typical?",
   opts=[
     ["Topical corticosteroids", "Correct — for non-infectious anterior disease the deck gives topical steroids."],
     ["Intraocular corticosteroid injection", "That is needed for posterior disease, which does not respond to topical treatment."],
     ["Oral antivirals for ten days", "That is herpetic keratitis."],
     ["Topical fluoroquinolone", "That treats bacterial infection."]],
   c=0, cite=c(63)),

 dict(topic="Anterior uveitis", io=IOA, lead="next step", slot="escalation",
   q="A 44-year-old man has had three separate episodes of anterior uveitis in two years and reports joint pain and lower back stiffness. Which is the most appropriate next step?",
   opts=[
     ["Thorough systemic evaluation for an underlying autoimmune condition",
      "Correct — the deck calls for this when uveitis is recurrent or has suggestive systemic features."],
     ["Reassure him that recurrence is expected and needs no further workup",
      "Recurrence is precisely the trigger for evaluation."],
     ["Start long-term prophylactic topical antibiotics",
      "There is no infection to prevent."],
     ["Arrange fluorescein angiography",
      "That is used in posterior uveitis."]],
   c=0, cite=c(63)),

 dict(topic="Keratitis", io=IOA, lead="prognosis", slot="prognosis",
   q="A 50-year-old man has a moderate bacterial corneal ulcer that sits directly in front of his pupil. How does its position affect the outlook?",
   opts=[
     ["The prognosis is worse, because ulcers inside the visual axis carry a poorer outcome",
      "Correct — the deck grades prognosis by both size and position relative to the visual axis."],
     ["Position makes no difference; only ulcer size matters",
      "The deck names the visual axis specifically."],
     ["The prognosis is better, because central ulcers are noticed sooner",
      "The deck grades central ulcers as worse."],
     ["The prognosis depends only on the organism",
      "Size and position both feature in the deck's grading."]],
   c=0, cite=c(56)),

 dict(topic="Trachoma", io=IOA, lead="treatment" if False else "first-line", slot="agent/regimen",
   q="A public health team is treating an area where trachoma prevalence is eight per cent. Which regimen does the lecture describe?",
   opts=[
     ["Azithromycin one gram orally as a single dose, given to all eligible members of the evaluation unit",
      "Correct — mass drug administration, at or above the five per cent threshold."],
     ["Doxycycline 100 milligrams twice daily for seven days, to symptomatic individuals only",
      "That is adult inclusion conjunctivitis, and treats individuals rather than the population."],
     ["Topical erythromycin ointment to symptomatic individuals only",
      "The deck describes mass administration."],
     ["Azithromycin one gram weekly for four weeks",
      "The deck gives a single dose."]],
   c=0, cite=c(46)),

 dict(topic="Trachoma", io=IOA, lead="next step", slot="escalation",
   q="A 41-year-old woman from a trachoma-endemic region has eyelashes turned inward and abrading her cornea after years of repeated infection. Which is required?",
   opts=[
     ["Surgical treatment of the trichiasis",
      "Correct — the deck states that trichiasis requires surgery; antibiotics cannot reverse scarring."],
     ["A further single dose of azithromycin",
      "Antibiotics treat infection, not established lid scarring."],
     ["Lubricating drops alone",
      "Insufficient while lashes are abrading the cornea."],
     ["Observation with annual review",
      "The deck requires surgery."]],
   c=0, cite=c(46)),

 dict(topic="Blepharitis", io=IOA, lead="next step", slot="escalation",
   q="A 49-year-old woman has completed a two-week lid hygiene regimen for blepharitis with no improvement. Which is the most appropriate next step?",
   opts=[
     ["Try a topical antibiotic",
      "Correct — the deck escalates from lid hygiene to topical antibiotics, then to oral if needed."],
     ["Go straight to oral antibiotics",
      "The deck tries topical first."],
     ["Refer urgently to ophthalmology today",
      "Referral follows several weeks without improvement."],
     ["Start a topical corticosteroid",
      "Not in the deck's sequence."]],
   c=0, cite=c(19)),

 dict(topic="Hordeolum with cellulitis", io=IOA, lead="next step", slot="escalation",
   q="A 32-year-old man has a tender lid margin nodule, and the surrounding lid and periorbital skin are now diffusely swollen, red and warm. The globe is white with full painless movements. Which is the most appropriate management?",
   opts=[
     ["Treat as pre-septal cellulitis with systemic antibiotics",
      "Correct — the deck says to treat an associated pre-septal cellulitis per that pathway."],
     ["Continue warm compresses alone for another two weeks",
      "Compresses alone will not treat a spreading soft tissue infection."],
     ["Refer for immediate incision and drainage of the nodule",
      "The cellulitis is what now drives management."],
     ["Start topical antibiotic drops",
      "Drops do not treat a soft tissue infection."]],
   c=0, cite=c(21)),
]
