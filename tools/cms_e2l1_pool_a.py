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
   q="Which symptom does entropion produce?",
   opts=[
     ["Foreign body sensation", "Correct — the inward-turned lashes rub the globe."],
     ["Tearing", "Tearing is the hallmark of ectropion, where the everted lid no longer channels tears into the punctum."],
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
   q="Which cause is given for ectropion but NOT for entropion?",
   opts=[
     ["Seventh cranial nerve palsy", "Correct — a seventh cranial nerve palsy paralyses orbicularis oculi, so the lid falls outward; it cannot turn the lid inward."],
     ["Aging", "Aging causes both; involutional laxity can let the lid turn either inward or outward."],
     ["Cicatricial change from burn, surgery or trauma", "Cicatricial change from burn, surgery or trauma causes both, depending on whether the scar pulls the lid in or out."],
     ["Congenital", "Congenital forms of both entropion and ectropion exist, so this does not separate them."]],
   c=0, cite=c(12)),

 dict(topic="Entropion and ectropion", io=IOA, slot="first-line",
   q="What is the conservative management of entropion or ectropion?",
   opts=[
     ["Preservative-free artificial tears during the day and lubricating ointment at night, taping an exposed lid into place",
      "Correct — lubrication protects the exposed or abraded cornea and taping holds the lid in position, which is all that is needed until surgical repair."],
     ["Topical corticosteroid drops four times daily",
      "Topical corticosteroids do not reposition a malpositioned lid, and prolonged use risks raised intraocular pressure and cataract."],
     ["Oral antibiotics for ten days",
      "That is the preseptal cellulitis regimen."],
     ["Warm compresses and gentle massage",
      "That is chalazion and hordeolum management."]],
   c=0, cite=c(13)),

 dict(topic="Entropion and ectropion", io=IOA, slot="escalation",
   q="What is the definitive treatment for entropion or ectropion?",
   opts=[
     ["Surgery", "Correct — the lid malposition is mechanical, so only surgical repositioning corrects it definitively."],
     ["Long-term lubricating ointment", "That is conservative, not definitive."],
     ["Botulinum toxin injection", "Botulinum toxin does not reposition a lax or scarred lid; surgery is the definitive repair."],
     ["Topical antibiotic ointment", "Not the definitive treatment."]],
   c=0, cite=c(13)),

 dict(topic="Entropion and ectropion", io=IOA, slot="initial test",
   q="Which statement correctly describes the examination required for entropion and ectropion?",
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
      "Correct — redundant lid skin is heavy, drapes over the lashes so the patient looks through them, and rubs with each blink."],
     ["Burning, dryness, grittiness and crusting at the lash bases",
      "That is blepharitis."],
     ["Sudden painless red patch on the white of the eye",
      "That is a subconjunctival hemorrhage."],
     ["Deep pain radiating to the face, worse at night",
      "That is scleritis."]],
   c=0, cite=c(14)),

 dict(topic="Dermatochalasis", io=IOA, slot="initial test",
   q="Which assessment is specified in dermatochalasis, and why does it matter?",
   opts=[
     ["Visual fields, because a demonstrated deficit is what gets blepharoplasty covered by insurance",
      "Correct — blepharoplasty is treated as cosmetic unless a visual field deficit is documented, so the field test is what establishes functional need."],
     ["Intraocular pressure, because the lid weight raises it",
      "Lid weight does not raise intraocular pressure; the assessment that matters here is the visual field."],
     ["Serum lipid profile, because the lesions are lipid",
      "That is xanthelasma."],
     ["Slit lamp with fluorescein, to find an epithelial defect",
      "Slit lamp with fluorescein looks for a corneal epithelial defect, which is the keratitis and ulcer examination rather than the dermatochalasis assessment."]],
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
   q="How does xanthelasma appear on examination?",
   opts=[
     ["Oval-shaped yellowish plaques around the eyelids",
      "Correct — xanthelasma forms oval-shaped yellowish plaques, soft cholesterol deposits under the skin on or around the eyelids, and is typically asymptomatic."],
     ["Tender red nodules at the lid margin",
      "A tender eyelid nodule points to a hordeolum; xanthelasma plaques are soft, yellowish and typically asymptomatic."],
     ["Crusting and scaling around the lash bases",
      "Crusting and scaling around the lash bases is a sign of blepharitis; xanthelasma forms oval-shaped yellowish plaques instead."],
     ["A triangular fleshy wedge growing onto the cornea",
      "A fleshy wedge that spreads onto the cornea is a pterygium; xanthelasma is a yellowish plaque on the eyelid skin, not the eye surface."]],
   c=0, cite=c(16)),

 dict(topic="Xanthelasma", io=IOA, slot="initial test",
   q="Which laboratory workup follows a diagnosis of xanthelasma?",
   opts=[
     ["Serum lipid profile, plus tests for diabetes mellitus and liver function",
      "Correct — the plaques are a cutaneous marker of disordered lipid handling, so lipids, glucose and liver function are all checked."],
     ["Serum lipid profile alone",
      "A lipid profile alone is incomplete; diabetes mellitus and liver dysfunction also underlie the lesion and are tested for."],
     ["Complete blood count with differential and blood cultures",
      "That is the cellulitis workup."],
     ["Conjunctival nucleic acid amplification testing",
      "That is for chlamydial conjunctivitis."]],
   c=0, cite=c(17)),

 dict(topic="Xanthelasma", io=IOA, slot="education",
   q="What is the prognosis of locally treated xanthelasma?",
   opts=[
     ["Recurrences are common even after effective local treatment",
      "Correct — local removal clears the deposit but not the metabolic driver behind it, so the lesions commonly return."],
     ["Local treatment is curative and recurrence is rare",
      "Recurrence is common rather than rare, because local treatment does nothing to the underlying lipid disorder."],
     ["The lesions resolve spontaneously within two to four weeks",
      "That is a subconjunctival hemorrhage."],
     ["The lesions progress to sebaceous carcinoma if untreated",
      "That concern belongs to recurrent chalazion."]],
   c=0, cite=c(17)),

 dict(topic="Xanthelasma", io=IOA, slot="first-line",
   q="Beyond local treatment, what else must be done for xanthelasma?",
   opts=[
     ["Treat the underlying metabolic issue",
      "Correct — the plaques signal a lipid or metabolic disorder, so treating that underlying problem matters more than removing the lesion."],
     ["Nothing further, since the lesions are cosmetic",
      "They are not merely cosmetic; they mark a metabolic disorder that carries cardiovascular risk."],
     ["Start a topical antibiotic",
      "There is no infection to treat."],
     ["Refer urgently to ophthalmology",
      "The lesions are not sight-threatening and need no urgent referral; the priority is the metabolic workup."]],
   c=0, cite=c(17)),

 dict(topic="Xanthelasma", io=IOA, slot="education",
   q="What caveat applies to lipid levels in xanthelasma?",
   opts=[
     ["Many patients have normal lipid levels, so a lipid profile and cardiovascular risk assessment are still reasonable",
      "Correct — a substantial proportion of patients have normal lipids, so a normal profile does not exclude the association and cardiovascular risk is still assessed."],
     ["Lipid levels are raised in every case, so the profile is diagnostic",
      "Lipids are normal in many patients, so the profile supports the picture rather than being diagnostic."],
     ["Lipid testing is unnecessary because the lesion is cosmetic",
      "The lesion is not merely cosmetic, and a lipid profile with cardiovascular risk assessment remains worthwhile."],
     ["Lipid levels should only be checked if the lesions recur",
      "Testing is done at presentation rather than held back until the lesions recur."]],
   c=0, cite=cn(17)),

 # ---- blepharitis / meibomitis ----
 dict(topic="Blepharitis", io=IOA, slot="risk factors",
   q="Which three conditions are associated with blepharitis and meibomitis?",
   opts=[
     ["Rosacea, seborrheic dermatitis, and colonization with Staphylococcus aureus",
      "Correct — rosacea and seborrheic dermatitis both disturb the lid margin, and Staphylococcus aureus colonization completes the triad."],
     ["Contact lens wear, dry eye, and topical corticosteroid use",
      "Those are keratitis risk factors."],
     ["Chronic sun and wind exposure",
      "That is pinguecula and pterygium."],
     ["Nasolacrimal duct obstruction",
      "That underlies dacryocystitis."]],
   c=0, cite=c(18)),

 dict(topic="Blepharitis", io=IOA, slot="manifestation",
   q="Which sign appears at the meibomian glands in meibomitis?",
   opts=[
     ["Thick, sometimes toothpaste-like lipid secretion",
      "Correct — inflamed meibomian glands produce inspissated lipid that expresses as a thick, toothpaste-like plug."],
     ["Clear watery secretion in excess",
      "The secretion is thickened rather than thinned; a clear watery excess is not the meibomitis finding."],
     ["Complete absence of any secretion",
      "Secretion is present but abnormal; it is thickened and inspissated rather than absent."],
     ["Blood-tinged secretion",
      "Blood-tinged secretion is not a feature; the characteristic finding is thick, toothpaste-like lipid."]],
   c=0, cite=c(18)),

 dict(topic="Blepharitis", io=IOA, slot="manifestation",
   q="What happens to the tear film in blepharitis?",
   opts=[
     ["It is decreased, or frothy and foamy",
      "Correct — the disordered lipid layer both reduces tear volume and destabilizes the film, so it appears decreased, or frothy and foamy."],
     ["It is increased and watery",
      "The film is decreased or destabilized rather than increased and watery."],
     ["It is unaffected",
      "The tear film is affected; a decreased or frothy film is one of the signs of the disease."],
     ["It is purulent",
      "Purulent discharge belongs to bacterial conjunctivitis."]],
   c=0, cite=c(18)),

 dict(topic="Blepharitis", io=IOA, slot="first-line",
   q="What is first-line management of blepharitis?",
   opts=[
     ["Lid hygiene", "Correct — warm compresses with lid scrubs clear the lid margin and are the foundation of treatment, often using an over-the-counter lid cleanser."],
     ["Topical antibiotics", "Topical antibiotics are reserved for when lid hygiene has failed after a two-week trial."],
     ["Oral antibiotics", "Oral antibiotics come later still, after topical treatment has failed to control the disease."],
     ["Topical corticosteroids", "Topical corticosteroids are not first-line; lid hygiene is, and steroids carry pressure and cataract risk."]],
   c=0, cite=c(19)),

 dict(topic="Blepharitis", io=IOA, slot="escalation",
   q="How long is lid hygiene given before escalating in blepharitis?",
   opts=[
     ["Two weeks", "Correct — two weeks of lid hygiene is the trial period before topical antibiotics are added."],
     ["Two days", "Two days is far too short to judge lid hygiene; the trial runs two weeks."],
     ["Two months", "Two months is longer than needed; escalation is considered at two weeks."],
     ["Six weeks", "Six weeks is too long to wait; the trial period is two weeks."]],
   c=0, cite=c(19)),

 dict(topic="Blepharitis", io=IOA, slot="prognosis",
   q="What is the long-term course of blepharitis?",
   opts=[
     ["It is chronic and can be controlled rather than cured",
      "Correct — an important expectation to set with the patient."],
     ["It resolves completely within two weeks of lid hygiene",
      "Lid hygiene improves symptoms but does not cure the disease; it is chronic and needs ongoing control."],
     ["It progresses to corneal ulceration if untreated",
      "Corneal ulceration is not the expected course; blepharitis is a chronic lid margin disease controlled with hygiene."],
     ["It resolves spontaneously without any treatment",
      "It does not remit on its own; without continued lid hygiene symptoms return."]],
   c=0, cite=c(19)),

 # ---- chalazion / hordeolum ----
 dict(topic="Chalazion and hordeolum", io=IOA, slot="differential",
   q="Which single examination finding separates a chalazion from a hordeolum?",
   opts=[
     ["Tenderness — the hordeolum is tender and the chalazion is not",
      "Correct — a hordeolum is an acute infection of a lid gland and is tender, while a chalazion is a sterile granuloma of retained lipid and is painless."],
     ["Size — the hordeolum is always larger",
      "Size does not separate them; a chalazion can be the larger lesion, and tenderness is what distinguishes them."],
     ["Color — the chalazion is yellow and the hordeolum is red",
      "Color does not reliably separate them; tenderness does, because only the hordeolum is acutely infected."],
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
      "Correct — a chalazion is a slowly accumulating sterile granuloma, while a hordeolum is an acute infection that inflames within a day."],
     ["A chalazion appears overnight; a hordeolum builds over weeks",
      "This reverses the two."],
     ["Both appear within 24 hours",
      "Only the hordeolum appears within 24 hours; the chalazion builds over days to weeks."],
     ["Both build over months",
      "Neither builds over months; the chalazion takes days to weeks and the hordeolum about a day."]],
   c=0, cite=c(20)),

 dict(topic="Chalazion and hordeolum", io=IOA, slot="first-line",
   q="What is the initial management of both a chalazion and a hordeolum?",
   opts=[
     ["Warm compresses with gentle massage",
      "Correct — warmth softens the inspissated lipid and massage expresses it, which treats the blocked gland in either lesion."],
     ["Immediate incision and drainage",
      "That is reserved for a persistent hordeolum, by ophthalmology."],
     ["Oral antibiotics for ten days",
      "Reserved for associated preseptal cellulitis."],
     ["Topical corticosteroid drops",
      "Topical corticosteroids are not the first step; warm compresses with massage are, and they address the blocked gland directly."]],
   c=0, cite=c(21)),

 dict(topic="Chalazion and hordeolum", io=IOA, slot="referral",
   q="When is a hordeolum referred to ophthalmology, and for what?",
   opts=[
     ["If persistent — for example no improvement in two weeks — for incision and drainage",
      "Correct — a hordeolum that has not improved after about two weeks of warm compresses is referred for incision and drainage."],
     ["Immediately at first presentation, for steroid injection",
      "Steroid injection or curettage is the chalazion pathway."],
     ["Only if the patient also has rosacea",
      "Rosacea matters for recurrence, not for the initial referral."],
     ["Never — hordeola are managed entirely in primary care",
      "Persistent lesions are referred; a hordeolum that fails two weeks of conservative treatment needs incision and drainage."]],
   c=0, cite=c(21)),

 dict(topic="Chalazion and hordeolum", io=IOA, slot="referral",
   q="Why is a chalazion that recurs or persists more than two to three months referred?",
   opts=[
     ["To rule out sebaceous carcinoma",
      "Correct — sebaceous carcinoma of the meibomian gland can masquerade as a recurrent chalazion, so persistent lesions are biopsied."],
     ["To rule out basal cell carcinoma",
      "Basal cell carcinoma is a lid margin tumor, but the malignancy that mimics a recurrent chalazion is sebaceous carcinoma."],
     ["To rule out orbital cellulitis",
      "Orbital cellulitis is acute and febrile with restricted eye movement, not a slowly recurring painless nodule."],
     ["To rule out a lacrimal sac tumor",
      "That concern belongs to a mass above the medial canthal tendon."]],
   c=0, cite=c(21)),

 dict(topic="Chalazion and hordeolum", io=IOA, slot="education",
   q="What should a patient with a chalazion be told about the timescale of improvement?",
   opts=[
     ["Improvement may take months",
      "Correct — a sterile lipid granuloma resolves slowly, and setting an expectation of months prevents premature demands for surgery."],
     ["Improvement should be complete within 48 hours",
      "That is the antibiotic response time for cellulitis."],
     ["Improvement should be complete within one week",
      "One week is far too fast; a chalazion may take months to settle with conservative treatment."],
     ["It will never improve without surgery",
      "Many chalazia resolve with warm compresses and massage alone; surgery is not inevitable."]],
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
   q="What is the most common cause of dacryoadenitis?",
   opts=[
     ["Inflammatory", "Correct — inflammatory causes predominate, and bacterial infection of the lacrimal gland is rare by comparison."],
     ["Bacterial", "Bacterial dacryoadenitis is rare; inflammatory causes are much the commonest."],
     ["Viral", "Viral dacryoadenitis occurs and is usually bilateral, but inflammatory causes are the most common."],
     ["Fungal", "Fungal infection of the lacrimal gland is not a recognized common cause; inflammatory disease is."]],
   c=0, cite=c(22)),

 dict(topic="Dacryoadenitis", io=IOA, slot="test finding",
   q="Which associated findings are listed in dacryoadenitis?",
   opts=[
     ["Ipsilateral preauricular lymphadenopathy, temporal conjunctival injection, fever and leukocytosis",
      "Correct — the lacrimal gland drains to the preauricular node, so the node enlarges on the same side, with temporal conjunctival injection and a systemic inflammatory response."],
     ["Proptosis with painful restricted eye movement",
      "Those indicate orbital cellulitis."],
     ["A fixed mid-dilated pupil with a cloudy cornea",
      "That is acute angle closure."],
     ["Purulent discharge expressed from the lower punctum",
      "That is dacryocystitis."]],
   c=0, cite=c(22)),

 dict(topic="Dacryoadenitis", io=IOA, slot="first-line",
   q="Which statement correctly describes the treatment of INFLAMMATORY dacryoadenitis and its expected response?",
   opts=[
     ["Corticosteroids, with a response expected within 48 hours",
      "Correct — inflammatory disease responds to corticosteroids quickly, and a failure to improve within 48 hours should prompt reconsideration of the diagnosis."],
     ["Oral antibiotics, with a response expected within 48 hours",
      "Antibiotics are the empiric option when the cause is unclear."],
     ["Cool compresses, with resolution over two weeks",
      "Cool compresses are the viral measure."],
     ["Intravenous antibiotics for 48 to 72 hours",
      "That is the regimen for severe dacryocystitis or postseptal cellulitis."]],
   c=0, cite=c(23)),

 dict(topic="Dacryoadenitis", io=IOA, slot="avoid",
   q="What caution applies before starting corticosteroids in dacryoadenitis?",
   opts=[
     ["Do not begin them until bacterial and other infectious causes have been reasonably excluded",
      "Correct — corticosteroids suppress the inflammatory response, so giving them to an undiagnosed bacterial infection allows it to progress."],
     ["Do not begin them until a computed tomography scan has been obtained",
      "Imaging is not needed in every case; the requirement before steroids is to exclude an infectious cause."],
     ["Do not begin them in any patient over sixty-five",
      "Age is not the limiting factor; excluding infection before immunosuppressing is."],
     ["Do not begin them without an ophthalmology consultation",
      "Consultation may be helpful, but the specific caution is to exclude bacterial and other infectious causes first."]],
   c=0, cite=cn(23)),

 dict(topic="Dacryoadenitis", io=IOA, slot="initial test",
   q="When is imaging actually appropriate in dacryoadenitis?",
   opts=[
     ["With severe disease, orbital findings, chronicity, atypical presentation, suspected abscess or mass, or failure to improve",
      "Correct — imaging is reserved for severe or atypical disease, orbital signs, chronicity, a suspected abscess or mass, or failure to improve."],
     ["In every case, before any treatment is started",
      "Imaging is not automatic; a typical case responding as expected does not need a scan."],
     ["Only after corticosteroids have failed",
      "Several indications arise earlier than steroid failure, including orbital findings and a suspected abscess or mass."],
     ["Never — the diagnosis is entirely clinical",
      "Imaging does have a role; severe, atypical, chronic or non-responding disease is scanned."]],
   c=0, cite=cn(23)),

 # ---- dacryocystitis ----
 dict(topic="Dacryocystitis", io=IOA, slot="etiology",
   q="What underlies dacryocystitis?",
   opts=[
     ["Nasolacrimal duct obstruction", "Correct — obstruction of the nasolacrimal duct dams tears in the lacrimal sac, and the stagnant fluid becomes infected."],
     ["Meibomian gland obstruction", "That produces a chalazion."],
     ["Direct extension from a sinus infection", "That is the cellulitis route."],
     ["Chronic ultraviolet exposure", "That drives pinguecula and pterygium."]],
   c=0, cite=c(24)),

 dict(topic="Dacryocystitis", io=IOA, slot="manifestation",
   q="Where is the swelling in dacryocystitis, and what can be expressed from the punctum?",
   opts=[
     ["Over the nasal aspect of the lower lid, with mucoid or purulent discharge from the lower punctum",
      "Correct — the lacrimal sac sits at the nasal aspect of the lower lid, and pressure over it refluxes mucoid or purulent contents through the lower punctum."],
     ["Over the lateral third of the upper lid, with watery discharge",
      "That is dacryoadenitis."],
     ["Diffusely over both lids, with no expressible discharge",
      "That is cellulitis."],
     ["At the limbus, with no discharge",
      "That is not a lacrimal presentation."]],
   c=0, cite=c(24)),

 dict(topic="Dacryocystitis", io=IOA, slot="differential",
   q="A mass sits ABOVE the medial canthal tendon rather than below it. What should be suspected?",
   opts=[
     ["A lacrimal sac tumor, which is rare",
      "Correct — the lacrimal sac lies BELOW the medial canthal tendon, so a mass above it is not a distended sac and raises the possibility of a rare lacrimal sac tumor."],
     ["A chalazion", "Chalazia sit in the lid, not at the medial canthus."],
     ["Orbital cellulitis", "That produces diffuse swelling and proptosis."],
     ["A pterygium", "That is a conjunctival lesion at the limbus."]],
   c=0, cite=c(24)),

 dict(topic="Dacryocystitis", io=IOA, slot="first-line",
   q="How is an afebrile, systemically well, reliable patient with mild dacryocystitis managed?",
   opts=[
     ["Outpatient oral antibiotics for ten days",
      "Correct — a well patient with localized infection and reliable follow-up can be treated at home with a ten-day oral antibiotic course."],
     ["Hospital admission with intravenous antibiotics for 48 to 72 hours",
      "That is for the febrile, acutely ill or unreliable patient."],
     ["Warm compresses alone with no antibiotic",
      "Compresses are adjunctive, not the whole treatment."],
     ["Immediate surgical drainage",
      "Incision and drainage is only considered for an abscess."]],
   c=0, cite=c(25)),

 dict(topic="Dacryocystitis", io=IOA, slot="escalation",
   q="Which patients with dacryocystitis are admitted, and for how long?",
   opts=[
     ["Febrile, acutely ill or unreliable patients — intravenous antibiotics for 48 to 72 hours, then oral to complete 10 to 14 days",
      "Correct — fever, systemic illness or unreliable follow-up warrant 48 to 72 hours of intravenous antibiotics, then an oral switch to complete 10 to 14 days."],
     ["All patients, for a 10-day intravenous course",
      "Only the febrile, acutely ill or unreliable group is admitted; a well patient is treated as an outpatient."],
     ["Only patients over sixty-five, for 24 hours",
      "Age alone does not decide admission; fever, systemic illness and reliability of follow-up do."],
     ["Only contact lens wearers, for 48 hours",
      "That risk factor belongs to keratitis."]],
   c=0, cite=c(25)),

 dict(topic="Dacryocystitis", io=IOA, slot="prognosis",
   q="What is often needed once the acute infection has resolved?",
   opts=[
     ["Probing and irrigation to assess patency of the nasolacrimal drainage system, possibly surgery",
      "Correct — the obstruction still has to be addressed."],
     ["Nothing further, since the obstruction resolves with the infection",
      "The nasolacrimal obstruction that caused the infection persists after the infection clears, so the drainage system still has to be assessed."],
     ["Lifelong prophylactic oral antibiotics",
      "Indefinite prophylaxis does not relieve the blockage; probing and irrigation assess patency and surgery corrects it."],
     ["Serial computed tomography scanning",
      "Serial scanning adds nothing here; the follow-up question is whether the nasolacrimal duct drains, which probing and irrigation answer."]],
   c=0, cite=c(25)),

 dict(topic="Dacryocystitis", io=IOA, slot="prognosis",
   q="Once antibiotics are started for dacryocystitis, when should improvement be expected?",
   opts=[
     ["Within 24 to 48 hours", "Correct — a soft tissue infection responding to an appropriate antibiotic should be visibly improving within 24 to 48 hours, and failure to do so prompts reassessment."],
     ["Within 2 to 3 weeks", "That is the healing time for a corneal ulcer."],
     ["Within 2 to 4 weeks", "That is a subconjunctival hemorrhage resolving."],
     ["Within several months", "That is chalazion improvement."]],
   c=0, cite=c(25)),
]
