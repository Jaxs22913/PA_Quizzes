# -*- coding: utf-8 -*-
# CMS I Exam 2, Lecture 1 (Common Ophthalmological Disorders, Prof. Jaquith,
# adopted from Robert Gray) -- pool A: eyelid and lacrimal disorders.
#
# CMS IS THE MANAGEMENT HALF. Clin Path I Lecture 4 covers almost this exact
# condition list from the mechanism side, so these questions ask what it looks
# like, what to order, what to give and when to refer -- the eight-point frame
# from [[cms_exam_spec]].
#
# NO ABBREVIATIONS unless spelled out first, per the standing policy. The deck
# leans heavily on abx, PO, I&D, OTC, DDX, IOP and so on.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "CMS I Common Ophthalmological Disorders 2026 - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
def ce(n): return f"{SRC}, Slide {n} (figure, stored as a metafile)"
def cn(n): return f"{SRC}, Slide {n} (speaker notes)"

IOA = ("Objective a — Compare and contrast the etiologies, epidemiology, risk factors, "
       "clinical manifestations, differential diagnosis, diagnostic testing, management, "
       "appropriate referrals, patient education, and prognosis of the following common "
       "ophthalmological disorders")
IOB = ("Objective b — Identify medical care strategies for ophthalmological disorders in the "
       "lecture topic list for the following populations: infant, child, adolescent, adult, elderly")

POOL_A = [
 # ---- entropion / ectropion ----
 dict(topic="Entropion", io=IOA, slot="manifestation",
   q="Which symptom does the deck give for entropion?",
   opts=[
     ["Foreign body sensation", "Correct — the inward-turned lashes rub the globe."],
     ["Tearing", "That is the symptom the deck gives for ectropion."],
     ["Severe boring pain worse at night", "That is scleritis."],
     ["Itching with stringy discharge", "That is allergic conjunctivitis."]],
   c=0, cite=c(12)),

 dict(topic="Entropion", io=IOA, slot="complication",
   q="Which complication follows the inward-turning lid margin of entropion?",
   opts=[
     ["Corneal abrasion, because the lashes are pushed onto the globe (trichiasis)",
      "Correct — trichiasis is the mechanism and abrasion the result."],
     ["Exposure keratopathy, because the eye cannot close",
      "That is the ectropion complication."],
     ["Scleral thinning and perforation",
      "That is scleritis."],
     ["Nasolacrimal duct obstruction",
      "That underlies dacryocystitis."]],
   c=0, cite=c(12)),

 dict(topic="Ectropion", io=IOA, slot="complication",
   q="Which complication follows the outward-turning lid margin of ectropion?",
   opts=[
     ["Exposure keratopathy", "Correct — the lid no longer protects the surface."],
     ["Corneal abrasion from trichiasis", "That is the entropion complication."],
     ["Sebaceous carcinoma", "That is the concern with a recurrent chalazion."],
     ["Preauricular lymphadenopathy", "Not a complication of ectropion."]],
   c=0, cite=c(12)),

 dict(topic="Ectropion", io=IOA, slot="etiology",
   q="Which cause does the deck give for ectropion but NOT for entropion?",
   opts=[
     ["Seventh cranial nerve palsy", "Correct — the deck marks this one as ectropion only."],
     ["Aging", "The deck lists ageing for both."],
     ["Cicatricial change from burn, surgery or trauma", "The deck lists this for both."],
     ["Congenital", "The deck lists this for both."]],
   c=0, cite=c(12)),

 dict(topic="Entropion and ectropion", io=IOA, slot="first-line",
   q="What is the conservative management of entropion or ectropion?",
   opts=[
     ["Preservative-free artificial tears during the day and lubricating ointment at night, taping an exposed lid into place",
      "Correct — the deck's conservative measures before surgery."],
     ["Topical corticosteroid drops four times daily",
      "The deck does not give steroids for lid malposition."],
     ["Oral antibiotics for ten days",
      "That is the preseptal cellulitis regimen."],
     ["Warm compresses and gentle massage",
      "That is chalazion and hordeolum management."]],
   c=0, cite=c(13)),

 dict(topic="Entropion and ectropion", io=IOA, slot="escalation",
   q="What is the definitive treatment for entropion or ectropion?",
   opts=[
     ["Surgery", "Correct — the deck calls surgery definitive."],
     ["Long-term lubricating ointment", "That is conservative, not definitive."],
     ["Botulinum toxin injection", "Not given by the deck."],
     ["Topical antibiotic ointment", "Not the definitive treatment."]],
   c=0, cite=c(13)),

 dict(topic="Entropion and ectropion", io=IOA, slot="initial test",
   q="Which examination does the deck specify for entropion and ectropion, and what is it looking for?",
   opts=[
     ["Slit lamp examination, to assess corneal involvement",
      "Correct — the question is whether the cornea has been damaged."],
     ["Computed tomography of the orbits with contrast",
      "That is for cellulitis, dacryocystitis and dacryoadenitis."],
     ["Fluorescein angiography",
      "That is used in posterior uveitis and retinal vascular disease."],
     ["Serum lipid profile",
      "That belongs to xanthelasma."]],
   c=0, cite=c(13)),

 # ---- dermatochalasis ----
 dict(topic="Dermatochalasis", io=IOA, slot="manifestation",
   q="How does a patient with dermatochalasis describe the problem?",
   opts=[
     ["Heaviness of the lids, looking through the lashes, and friction of the lids with blinking",
      "Correct — the deck's symptom wording."],
     ["Burning, dryness, grittiness and crusting at the lash bases",
      "That is blepharitis."],
     ["Sudden painless red patch on the white of the eye",
      "That is a subconjunctival haemorrhage."],
     ["Deep pain radiating to the face, worse at night",
      "That is scleritis."]],
   c=0, cite=c(14)),

 dict(topic="Dermatochalasis", io=IOA, slot="initial test",
   q="Which assessment does the deck specify in dermatochalasis, and why does it matter?",
   opts=[
     ["Visual fields, because a demonstrated deficit is what gets blepharoplasty covered by insurance",
      "Correct — the deck ties the field test directly to coverage."],
     ["Intraocular pressure, because the lid weight raises it",
      "The deck makes no such claim."],
     ["Serum lipid profile, because the lesions are lipid",
      "That is xanthelasma."],
     ["Slit lamp with fluorescein, to find an epithelial defect",
      "Not what the deck specifies here."]],
   c=0, cite=c(15)),

 dict(topic="Dermatochalasis", io=IOA, slot="first-line",
   q="What is the treatment for dermatochalasis?",
   opts=[
     ["Blepharoplasty", "Correct — surgical removal of the excess skin."],
     ["Lid hygiene twice daily", "That is blepharitis management."],
     ["Cryotherapy with liquid nitrogen", "That is one of the xanthelasma options."],
     ["Warm compresses and massage", "That is chalazion management."]],
   c=0, cite=c(15)),

 # ---- xanthelasma ----
 dict(topic="Xanthelasma", io=IOA, slot="manifestation",
   q="How does xanthelasma appear and how does it feel?",
   opts=[
     ["Oval-shaped yellowish plaques, and typically asymptomatic",
      "Correct — the deck's sign and symptom pairing."],
     ["Tender red nodules at the lid margin",
      "That is a hordeolum."],
     ["Crusting and scaling around the lash bases",
      "That is blepharitis."],
     ["A triangular fleshy wedge growing onto the cornea",
      "That is a pterygium."]],
   c=0, cite=c(16)),

 dict(topic="Xanthelasma", io=IOA, slot="initial test",
   q="Which laboratory workup does the deck order for xanthelasma?",
   opts=[
     ["Serum lipid profile, plus tests for diabetes mellitus and liver function",
      "Correct — the deck's full workup, because the lesion flags a metabolic disorder."],
     ["Serum lipid profile alone",
      "The deck adds diabetes and liver testing."],
     ["Complete blood count with differential and blood cultures",
      "That is the cellulitis workup."],
     ["Conjunctival nucleic acid amplification testing",
      "That is for chlamydial conjunctivitis."]],
   c=0, cite=c(17)),

 dict(topic="Xanthelasma", io=IOA, slot="education",
   q="What does the deck say about the prognosis of locally treated xanthelasma?",
   opts=[
     ["Recurrences are common even after effective local treatment",
      "Correct — the deck flags recurrence explicitly."],
     ["Local treatment is curative and recurrence is rare",
      "The deck says the opposite."],
     ["The lesions resolve spontaneously within two to four weeks",
      "That is a subconjunctival haemorrhage."],
     ["The lesions progress to sebaceous carcinoma if untreated",
      "That concern belongs to recurrent chalazion."]],
   c=0, cite=c(17)),

 dict(topic="Xanthelasma", io=IOA, slot="first-line",
   q="Beyond local treatment, what does the deck say to do for xanthelasma?",
   opts=[
     ["Treat the underlying metabolic issue",
      "Correct — the plaques are a marker, and the deck directs treatment at the cause."],
     ["Nothing further, since the lesions are cosmetic",
      "The deck treats them as a metabolic signal."],
     ["Start a topical antibiotic",
      "There is no infection to treat."],
     ["Refer urgently to ophthalmology",
      "The deck does not make this urgent."]],
   c=0, cite=c(17)),

 dict(topic="Xanthelasma", io=IOA, slot="education",
   q="What caveat do the speaker notes add about lipid levels in xanthelasma?",
   opts=[
     ["Many patients have normal lipid levels, so a lipid profile and cardiovascular risk assessment are still reasonable",
      "Correct — the notes temper the association without discarding the workup."],
     ["Lipid levels are raised in every case, so the profile is diagnostic",
      "The notes say many patients have normal levels."],
     ["Lipid testing is unnecessary because the lesion is cosmetic",
      "The notes still call the profile reasonable."],
     ["Lipid levels should only be checked if the lesions recur",
      "The notes set no such condition."]],
   c=0, cite=cn(17)),

 # ---- blepharitis / meibomitis ----
 dict(topic="Blepharitis", io=IOA, slot="risk factors",
   q="Which three associations does the deck give for blepharitis and meibomitis?",
   opts=[
     ["Rosacea, seborrhoeic dermatitis, and colonisation with Staphylococcus aureus",
      "Correct — the deck's three."],
     ["Contact lens wear, dry eye, and topical corticosteroid use",
      "Those are keratitis risk factors."],
     ["Chronic sun and wind exposure",
      "That is pinguecula and pterygium."],
     ["Nasolacrimal duct obstruction",
      "That underlies dacryocystitis."]],
   c=0, cite=c(18)),

 dict(topic="Blepharitis", io=IOA, slot="manifestation",
   q="Which sign does the deck describe at the meibomian glands in meibomitis?",
   opts=[
     ["Thick, sometimes toothpaste-like lipid secretion",
      "Correct — the deck's distinctive description."],
     ["Clear watery secretion in excess",
      "The deck describes a thickened, not a thinned, secretion."],
     ["Complete absence of any secretion",
      "The deck describes abnormal secretion, not absence."],
     ["Blood-tinged secretion",
      "Not described by the deck."]],
   c=0, cite=c(18)),

 dict(topic="Blepharitis", io=IOA, slot="manifestation",
   q="What does the deck say about the tear film in blepharitis?",
   opts=[
     ["It is decreased, or frothy and foamy",
      "Correct — the deck gives both descriptions."],
     ["It is increased and watery",
      "The deck describes a decreased or abnormal film."],
     ["It is unaffected",
      "The deck lists tear film change as a sign."],
     ["It is purulent",
      "Purulent discharge belongs to bacterial conjunctivitis."]],
   c=0, cite=c(18)),

 dict(topic="Blepharitis", io=IOA, slot="first-line",
   q="What is first-line management of blepharitis?",
   opts=[
     ["Lid hygiene", "Correct — the deck names lid hygiene first, with an over-the-counter product often recommended."],
     ["Topical antibiotics", "The deck tries these only if lid hygiene fails after two weeks."],
     ["Oral antibiotics", "Those come after topical antibiotics in the deck's sequence."],
     ["Topical corticosteroids", "Not first-line in the deck."]],
   c=0, cite=c(19)),

 dict(topic="Blepharitis", io=IOA, slot="escalation",
   q="How long does the deck give lid hygiene before escalating in blepharitis?",
   opts=[
     ["Two weeks", "Correct — the deck's stated trial period before topical antibiotics."],
     ["Two days", "Shorter than the deck's period."],
     ["Two months", "Longer than the deck's period."],
     ["Six weeks", "Not the deck's interval."]],
   c=0, cite=c(19)),

 dict(topic="Blepharitis", io=IOA, slot="prognosis",
   q="What does the deck say about the long-term course of blepharitis?",
   opts=[
     ["It is chronic and can be controlled rather than cured",
      "Correct — an important expectation to set with the patient."],
     ["It resolves completely within two weeks of lid hygiene",
      "The deck expects improvement but not cure."],
     ["It progresses to corneal ulceration if untreated",
      "The deck does not describe this course."],
     ["It resolves spontaneously without any treatment",
      "The deck prescribes ongoing management."]],
   c=0, cite=c(19)),

 # ---- chalazion / hordeolum ----
 dict(topic="Chalazion and hordeolum", io=IOA, slot="differential",
   q="Which single examination finding separates a chalazion from a hordeolum?",
   opts=[
     ["Tenderness — the hordeolum is tender and the chalazion is not",
      "Correct — the deck's discriminating sign."],
     ["Size — the hordeolum is always larger",
      "Size is not the deck's discriminator."],
     ["Colour — the chalazion is yellow and the hordeolum is red",
      "The deck does not separate them by colour."],
     ["Laterality — the chalazion is always bilateral",
      "Neither is defined by laterality."]],
   c=0, cite=c(20)),

 dict(topic="Chalazion and hordeolum", io=IOA, slot="etiology",
   q="What is a chalazion, in mechanism?",
   opts=[
     ["A sterile obstruction of a meibomian gland",
      "Correct — sterile is the key word separating it from a hordeolum."],
     ["An acute staphylococcal infection of a meibomian gland",
      "That is an internal hordeolum."],
     ["An acute infection of the glands of Zeis or Moll",
      "That is an external hordeolum."],
     ["A lipid deposit in the eyelid skin",
      "That is xanthelasma."]],
   c=0, cite=c(20)),

 dict(topic="Chalazion and hordeolum", io=IOA, slot="manifestation",
   q="How do the time courses of chalazion and hordeolum differ?",
   opts=[
     ["A chalazion swells over days to weeks; a hordeolum becomes painful and red over 24 hours or overnight",
      "Correct — the deck gives both timescales."],
     ["A chalazion appears overnight; a hordeolum builds over weeks",
      "This reverses the two."],
     ["Both appear within 24 hours",
      "The deck distinguishes them by timescale."],
     ["Both build over months",
      "Neither matches the deck's description."]],
   c=0, cite=c(20)),

 dict(topic="Chalazion and hordeolum", io=IOA, slot="first-line",
   q="What is the initial management of both a chalazion and a hordeolum?",
   opts=[
     ["Warm compresses with gentle massage",
      "Correct — the deck's shared conservative first step."],
     ["Immediate incision and drainage",
      "That is reserved for a persistent hordeolum, by ophthalmology."],
     ["Oral antibiotics for ten days",
      "Reserved for associated preseptal cellulitis."],
     ["Topical corticosteroid drops",
      "Not the deck's first step."]],
   c=0, cite=c(21)),

 dict(topic="Chalazion and hordeolum", io=IOA, slot="referral",
   q="When does the deck refer a hordeolum to ophthalmology, and for what?",
   opts=[
     ["If persistent — for example no improvement in two weeks — for incision and drainage",
      "Correct — the deck's threshold and procedure."],
     ["Immediately at first presentation, for steroid injection",
      "Steroid injection or curettage is the chalazion pathway."],
     ["Only if the patient also has rosacea",
      "Rosacea matters for recurrence, not for the initial referral."],
     ["Never — hordeola are managed entirely in primary care",
      "The deck does refer persistent cases."]],
   c=0, cite=c(21)),

 dict(topic="Chalazion and hordeolum", io=IOA, slot="referral",
   q="Why does the deck refer a chalazion that recurs or persists more than two to three months?",
   opts=[
     ["To rule out sebaceous carcinoma",
      "Correct — the deck names the malignancy explicitly."],
     ["To rule out basal cell carcinoma",
      "The deck names sebaceous carcinoma."],
     ["To rule out orbital cellulitis",
      "Not the deck's reason for this referral."],
     ["To rule out a lacrimal sac tumour",
      "That concern belongs to a mass above the medial canthal tendon."]],
   c=0, cite=c(21)),

 dict(topic="Chalazion and hordeolum", io=IOA, slot="education",
   q="What should a patient with a chalazion be told about the timescale of improvement?",
   opts=[
     ["Improvement may take months",
      "Correct — the deck says so, which is a key expectation to set."],
     ["Improvement should be complete within 48 hours",
      "That is the antibiotic response time for cellulitis."],
     ["Improvement should be complete within one week",
      "Faster than the deck's expectation."],
     ["It will never improve without surgery",
      "The deck expects many to resolve conservatively."]],
   c=0, cite=c(21)),

 # ---- dacryoadenitis ----
 dict(topic="Dacryoadenitis", io=IOA, slot="manifestation",
   q="Where is the swelling in dacryoadenitis?",
   opts=[
     ["Over the lateral one third of the upper lid",
      "Correct — the lacrimal gland sits superotemporally."],
     ["Over the nasal aspect of the lower lid",
      "That is dacryocystitis, over the lacrimal sac."],
     ["Diffusely across both lids and periorbital tissue",
      "That is cellulitis."],
     ["At the lid margin at the lash line",
      "That is an external hordeolum."]],
   c=0, cite=c(22)),

 dict(topic="Dacryoadenitis", io=IOA, slot="etiology",
   q="Which cause of dacryoadenitis does the deck say is most common?",
   opts=[
     ["Inflammatory", "Correct — the deck ranks inflammatory as most common, bacterial as rare."],
     ["Bacterial", "The deck calls bacterial causes rare."],
     ["Viral", "Viral is listed, and is usually bilateral, but is not named most common."],
     ["Fungal", "Not among the deck's causes for this condition."]],
   c=0, cite=c(22)),

 dict(topic="Dacryoadenitis", io=IOA, slot="test finding",
   q="Which associated findings does the deck list in dacryoadenitis?",
   opts=[
     ["Ipsilateral preauricular lymphadenopathy, temporal conjunctival injection, fever and leukocytosis",
      "Correct — the deck's associated findings."],
     ["Proptosis with painful restricted eye movement",
      "Those indicate orbital cellulitis."],
     ["A fixed mid-dilated pupil with a cloudy cornea",
      "That is acute angle closure."],
     ["Purulent discharge expressed from the lower punctum",
      "That is dacryocystitis."]],
   c=0, cite=c(22)),

 dict(topic="Dacryoadenitis", io=IOA, slot="first-line",
   q="How does the deck treat INFLAMMATORY dacryoadenitis, and how fast should it respond?",
   opts=[
     ["Corticosteroids, with a response expected within 48 hours",
      "Correct — the deck gives both the agent and the expected response time."],
     ["Oral antibiotics, with a response expected within 48 hours",
      "Antibiotics are the empiric option when the cause is unclear."],
     ["Cool compresses, with resolution over two weeks",
      "Cool compresses are the viral measure."],
     ["Intravenous antibiotics for 48 to 72 hours",
      "That is the regimen for severe dacryocystitis or postseptal cellulitis."]],
   c=0, cite=c(23)),

 dict(topic="Dacryoadenitis", io=IOA, slot="avoid",
   q="What caution do the speaker notes give before starting corticosteroids in dacryoadenitis?",
   opts=[
     ["Do not begin them until bacterial and other infectious causes have been reasonably excluded",
      "Correct — the notes are explicit about the sequence."],
     ["Do not begin them until a computed tomography scan has been obtained",
      "The notes say imaging is not automatically required."],
     ["Do not begin them in any patient over sixty-five",
      "Age is not the caution the notes raise."],
     ["Do not begin them without an ophthalmology consultation",
      "The notes raise infection exclusion rather than consultation."]],
   c=0, cite=cn(23)),

 dict(topic="Dacryoadenitis", io=IOA, slot="initial test",
   q="When do the speaker notes say imaging is actually appropriate in dacryoadenitis?",
   opts=[
     ["With severe disease, orbital findings, chronicity, atypical presentation, suspected abscess or mass, or failure to improve",
      "Correct — the notes qualify the slide's blanket recommendation."],
     ["In every case, before any treatment is started",
      "The notes say imaging is not automatically necessary."],
     ["Only after corticosteroids have failed",
      "The notes list several earlier indications."],
     ["Never — the diagnosis is entirely clinical",
      "The notes do give indications for imaging."]],
   c=0, cite=cn(23)),

 # ---- dacryocystitis ----
 dict(topic="Dacryocystitis", io=IOA, slot="etiology",
   q="What underlies dacryocystitis?",
   opts=[
     ["Nasolacrimal duct obstruction", "Correct — the deck's stated aetiology."],
     ["Meibomian gland obstruction", "That produces a chalazion."],
     ["Direct extension from a sinus infection", "That is the cellulitis route."],
     ["Chronic ultraviolet exposure", "That drives pinguecula and pterygium."]],
   c=0, cite=c(24)),

 dict(topic="Dacryocystitis", io=IOA, slot="manifestation",
   q="Where is the swelling in dacryocystitis, and what can be expressed from the punctum?",
   opts=[
     ["Over the nasal aspect of the lower lid, with mucoid or purulent discharge from the lower punctum",
      "Correct — the deck's location and the expressible discharge."],
     ["Over the lateral third of the upper lid, with watery discharge",
      "That is dacryoadenitis."],
     ["Diffusely over both lids, with no expressible discharge",
      "That is cellulitis."],
     ["At the limbus, with no discharge",
      "That is not a lacrimal presentation."]],
   c=0, cite=c(24)),

 dict(topic="Dacryocystitis", io=IOA, slot="differential",
   q="A mass sits ABOVE the medial canthal tendon rather than below it. What does the deck say to suspect?",
   opts=[
     ["A lacrimal sac tumour, which is rare",
      "Correct — the deck flags position relative to the tendon as the discriminator."],
     ["A chalazion", "Chalazia sit in the lid, not at the medial canthus."],
     ["Orbital cellulitis", "That produces diffuse swelling and proptosis."],
     ["A pterygium", "That is a conjunctival lesion at the limbus."]],
   c=0, cite=c(24)),

 dict(topic="Dacryocystitis", io=IOA, slot="first-line",
   q="How does the deck manage an afebrile, systemically well, reliable patient with mild dacryocystitis?",
   opts=[
     ["Outpatient oral antibiotics for ten days",
      "Correct — the deck's outpatient pathway."],
     ["Hospital admission with intravenous antibiotics for 48 to 72 hours",
      "That is for the febrile, acutely ill or unreliable patient."],
     ["Warm compresses alone with no antibiotic",
      "Compresses are adjunctive, not the whole treatment."],
     ["Immediate surgical drainage",
      "Incision and drainage is only considered for an abscess."]],
   c=0, cite=c(25)),

 dict(topic="Dacryocystitis", io=IOA, slot="escalation",
   q="Which patients with dacryocystitis does the deck admit, and for how long?",
   opts=[
     ["Febrile, acutely ill or unreliable patients — intravenous antibiotics for 48 to 72 hours, then oral to complete 10 to 14 days",
      "Correct — the deck's inpatient pathway in full."],
     ["All patients, for a 10-day intravenous course",
      "The deck admits only the sicker group."],
     ["Only patients over sixty-five, for 24 hours",
      "Age is not the deck's criterion."],
     ["Only contact lens wearers, for 48 hours",
      "That risk factor belongs to keratitis."]],
   c=0, cite=c(25)),

 dict(topic="Dacryocystitis", io=IOA, slot="prognosis",
   q="What does the deck say is often needed once the acute infection has resolved?",
   opts=[
     ["Probing and irrigation to assess patency of the nasolacrimal drainage system, possibly surgery",
      "Correct — the obstruction still has to be addressed."],
     ["Nothing further, since the obstruction resolves with the infection",
      "The deck expects further assessment."],
     ["Lifelong prophylactic oral antibiotics",
      "Not the deck's plan."],
     ["Serial computed tomography scanning",
      "Not what the deck describes."]],
   c=0, cite=c(25)),

 dict(topic="Dacryocystitis", io=IOA, slot="prognosis",
   q="Once antibiotics are started for dacryocystitis, when should improvement be expected?",
   opts=[
     ["Within 24 to 48 hours", "Correct — the deck's stated response window."],
     ["Within 2 to 3 weeks", "That is the healing time for a corneal ulcer."],
     ["Within 2 to 4 weeks", "That is a subconjunctival haemorrhage resolving."],
     ["Within several months", "That is chalazion improvement."]],
   c=0, cite=c(25)),
]
