# -*- coding: utf-8 -*-
# CMS I Exam 2, Lecture 1 -- vignette pool A.
#
# VIGNETTE ANATOMY, per [[cms_exam_spec]]: presentation, clues (age, risk
# factors, labs), the defining feature, diagnosis (best/initial/confirmatory
# test), and treatment (first-line, patient education).
#
# NAMED FINDINGS CARRY THEIR DESCRIPTION IN PARENTHESES, so the name alone is
# never the only handle -- "ciliary flush (a ring of redness at the corneal
# edge)", not just "ciliary flush".
#
# EVERY STEM STANDS ALONE. A vignette may not refer to another question: the
# partitioner shuffles, so "the same patient" never survives. This was a real
# bug reported by a classmate on 25 August 2026; see the _DEP guard in
# cms_e2l1_vig_partition.py.
#
# LEAD-INS ARE VARIED ON PURPOSE. Prof. Jaquith told the Exam 1 class there is
# "SOME diagnosis but A LOT are next management plan / first line treatment /
# patient education". Each question declares its lead type so the partition can
# cap diagnosis at 20 per cent.
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

VIG_A = [
 dict(topic="Contact lens keratitis", io=IOA, lead="next step", slot="escalation",
   q="A 22-year-old woman wakes with severe pain, photophobia and blurred vision in one eye after sleeping in her contact lenses. Fluorescein shows a central epithelial defect with a white infiltrate beneath it. Which is the most appropriate next step?",
   opts=[
     ["Remove the lenses without patching and arrange same-day ophthalmology evaluation",
      "Correct — this is microbial keratitis until proven otherwise, and it is a same-day condition."],
     ["Patch the eye and review her in two days",
      "Patching is specifically prohibited here, and two days is too long."],
     ["Dispense a topical anaesthetic for comfort at home",
      "Take-home anaesthetic delays healing and masks progression."],
     ["Start a topical corticosteroid and review in one week",
      "Steroids can worsen an uncontrolled infection."]],
   c=0, cite=c(71)),

 dict(topic="Contact lens keratitis", io=IOA, lead="education", slot="education",
   q="A 30-year-old contact lens wearer is being referred the same day for a corneal infiltrate. Which instruction is most important to give him before he leaves?",
   opts=[
     ["Return immediately if the pain increases, the white spot enlarges, or the vision drops further",
      "Correct — the explicit safety net the deck requires at the end of every red-eye assessment."],
     ["Resume lens wear as soon as the pain settles",
      "Lenses must stay out; wear is the risk factor that caused this."],
     ["Use the anaesthetic drops whenever the eye is uncomfortable",
      "Take-home anaesthetic is prohibited."],
     ["Expect complete resolution within 24 hours without treatment",
      "This is a sight-threatening infection, not a self-limiting one."]],
   c=0, cite=cn(71)),

 dict(topic="Bacterial conjunctivitis", io=IOA, lead="first-line", slot="first-line",
   q="A healthy 28-year-old man has three days of a red right eye with thick yellow discharge and lids stuck together in the morning. Vision is normal, the cornea is clear, and there is no preauricular node. Which is the most appropriate first-line treatment?",
   opts=[
     ["A topical broad-spectrum antibiotic such as a fluoroquinolone",
      "Correct — an immunocompetent adult with uncomplicated bacterial conjunctivitis."],
     ["Oral doxycycline twice daily for seven days",
      "That is the regimen for chlamydial conjunctivitis, which runs a chronic course."],
     ["A topical histamine blocker with a mast cell stabiliser",
      "That treats allergic disease, which itches and is bilateral."],
     ["Oral aciclovir for ten days",
      "That treats herpetic keratitis, which shows a dendrite."]],
   c=0, cite=c(41)),

 dict(topic="Bacterial conjunctivitis", io=IOA, lead="next step", slot="referral",
   q="A 45-year-old woman treated for bacterial conjunctivitis 24 hours ago returns with no improvement. She wears contact lenses daily. Which is the most appropriate next step?",
   opts=[
     ["Urgent referral to ophthalmology",
      "Correct — both lens wear and failure to improve in 24 hours are on the deck's urgent-referral list."],
     ["Continue the same drops and review in one week",
      "Failure to improve at 24 hours is itself a referral trigger."],
     ["Switch to an oral antibiotic and review in 48 hours",
      "The deck refers rather than escalating orally here."],
     ["Add a topical corticosteroid to settle the inflammation",
      "Steroids risk worsening an unrecognised keratitis."]],
   c=0, cite=c(41)),

 dict(topic="Gonococcal conjunctivitis", io=IOB, lead="next step", slot="escalation",
   q="A 3-day-old infant has markedly swollen lids and copious purulent discharge from both eyes, with a palpable preauricular node. Which is the most appropriate next step?",
   opts=[
     ["Emergent referral and hospital admission for systemic ceftriaxone, cultures and Gram stain",
      "Correct — suspected gonococcal conjunctivitis in a neonate risks corneal perforation and is an emergency."],
     ["Topical fluoroquinolone drops with review the following day",
      "Wholly inadequate for a neonatal gonococcal infection."],
     ["Oral erythromycin for fourteen days as an outpatient",
      "That regimen is for neonatal chlamydial disease, not gonococcal."],
     ["Warm compresses and reassurance that it will settle",
      "This is a sight-threatening emergency."]],
   c=0, cite=c(41)),

 dict(topic="Chlamydial conjunctivitis", io=IOA, lead="confirmatory test", slot="gold standard",
   q="A 24-year-old man has had a red left eye with stringy mucoid discharge for six weeks. Topical antibiotics have not helped, and the lower palpebral conjunctiva shows follicles (pale bumps that are redder at the base). Which test confirms the diagnosis?",
   opts=[
     ["Conjunctival nucleic acid amplification testing",
      "Correct — the chronic course, the follicles and the failure of topical therapy point to chlamydial disease."],
     ["Slit lamp examination with fluorescein staining",
      "That shows corneal defects, not the organism."],
     ["Computed tomography of the orbits with contrast",
      "Imaging plays no part in diagnosing conjunctivitis."],
     ["Conjunctival scraping for potassium hydroxide preparation",
      "That is a fungal preparation, and is not used here."]],
   c=0, cite=c(43)),

 dict(topic="Chlamydial conjunctivitis", io=IOA, lead="education", slot="education",
   q="A 26-year-old woman is starting doxycycline for adult inclusion conjunctivitis. Which counselling point does the lecture emphasise?",
   opts=[
     ["Stay out of the sun, take it with a full glass of water, stay upright, and separate it from antacids and iron, calcium or magnesium",
      "Correct — photosensitivity plus the absorption and oesophageal cautions."],
     ["Take it on an empty stomach and lie down for an hour afterwards",
      "Lying down risks oesophageal irritation; the advice is to stay upright."],
     ["Avoid all dairy products for one month after finishing",
      "The concern is timing around specific supplements, not a month-long ban."],
     ["Double the dose if the eye is not better in three days",
      "Dose escalation is not advised."]],
   c=0, cite=c(43)),

 dict(topic="Chlamydial conjunctivitis", io=IOA, lead="next step", slot="referral",
   q="A 23-year-old woman has been diagnosed with chlamydial conjunctivitis confirmed on conjunctival testing. Beyond treating her eye, which is the most appropriate next step?",
   opts=[
     ["Arrange evaluation for other sexually transmitted infections and notify her partners for evaluation",
      "Correct — the eye finding is a sentinel for a usually asymptomatic urogenital infection."],
     ["Repeat the conjunctival test in one week to confirm clearance",
      "The deck does not require a test of cure here."],
     ["Refer her urgently to ophthalmology",
      "Ophthalmology referral is not what this needs."],
     ["Screen her for autoimmune disease",
      "That would be relevant to autoimmune conjunctivitis."]],
   c=0, cite=c(43)),

 dict(topic="Viral conjunctivitis", io=IOA, lead="education", slot="education",
   q="A 19-year-old student has bilateral red eyes with profuse watery discharge and tender preauricular nodes, starting in one eye and spreading to the other. He had a cold last week. Which is the most appropriate advice?",
   opts=[
     ["It is contagious, so hand hygiene matters; expect it to worsen over the first week and resolve in two to three weeks",
      "Correct — the deck's course, including the counter-intuitive early worsening."],
     ["It should clear within 24 to 48 hours of starting antibiotic drops",
      "This is viral; antibiotics do nothing."],
     ["It is not contagious and needs no precautions",
      "The deck specifically requires contagious precautions."],
     ["It will require oral antivirals for ten days",
      "Antivirals are for herpetic keratitis, not adenoviral conjunctivitis."]],
   c=0, cite=c(37)),

 dict(topic="Viral conjunctivitis", io=IOA, lead="next step", slot="referral",
   q="A 25-year-old woman has had viral conjunctivitis for four weeks and now reports significant photophobia and blurred vision. Which is the most appropriate next step?",
   opts=[
     ["Refer to ophthalmology", "Correct — beyond three weeks, or with photophobia or decreased vision after onset, the deck refers."],
     ["Reassure and continue cool compresses", "New photophobia and vision loss are exactly what should stop reassurance."],
     ["Start a topical antibiotic", "The problem is not bacterial."],
     ["Start a topical corticosteroid", "Not a primary care decision in a red eye with vision change."]],
   c=0, cite=c(37)),

 dict(topic="Allergic conjunctivitis", io=IOA, lead="first-line", slot="agent/regimen",
   q="A 17-year-old has bilateral itchy red eyes every spring with swollen lids and stringy watery discharge. Vision is normal. Which single topical agent both blocks histamine and stabilises mast cells?",
   opts=[
     ["Olopatadine", "Correct — the deck names it as doing both."],
     ["A topical fluoroquinolone", "That is an antibiotic and treats nothing here."],
     ["A topical corticosteroid", "Not the deck's first-line for seasonal allergy."],
     ["Artificial tears alone", "Useful adjunct, but not the dual-action agent asked for."]],
   c=0, cite=c(35)),

 dict(topic="Episcleritis", io=IOA, lead="initial test", slot="gold standard",
   q="A 34-year-old woman has two days of mild ache and a sectoral patch of redness in one eye, with no discharge and no photophobia. Which bedside test best confirms the diagnosis?",
   opts=[
     ["Instil 2.5 per cent phenylephrine and look for blanching of the vessels after 15 minutes",
      "Correct — episcleral vessels blanch; the mild painless sectoral redness fits episcleritis."],
     ["Instil fluorescein and examine under cobalt blue light for a dendrite",
      "That looks for herpes simplex keratitis."],
     ["Measure the intraocular pressure with a tonometer pen",
      "Pressure is not the question in a mildly sore sectoral red eye."],
     ["Obtain computed tomography of the orbits with contrast",
      "Imaging plays no part here."]],
   c=0, cite=c(48)),

 dict(topic="Episcleritis", io=IOA, lead="first-line", slot="first-line",
   q="A 29-year-old man is diagnosed with episcleritis. Which is the most appropriate initial management?",
   opts=[
     ["Artificial tears and an oral non-steroidal anti-inflammatory taken with food",
      "Correct — the deck's treatment, and it specifically instructs taking the anti-inflammatory with food."],
     ["Systemic corticosteroids started immediately",
      "That is the scleritis pathway, and even there the notes start with anti-inflammatories."],
     ["Topical antibiotic drops four times daily",
      "There is no infection."],
     ["Urgent same-day ophthalmology referral",
      "Episcleritis is usually self-limited; referral follows failure at two days."]],
   c=0, cite=c(48)),

 dict(topic="Scleritis", io=IOA, lead="next step", slot="referral",
   q="A 52-year-old woman with rheumatoid arthritis has severe deep boring eye pain that wakes her at night and radiates to her cheek. The sclera has a bluish-purple hue (violaceous discolouration, the choroid showing through thinned sclera). Which is the most appropriate next step?",
   opts=[
     ["Urgent referral to ophthalmology",
      "Correct — the sclera is at risk of perforation and may need a surgical patch."],
     ["Artificial tears and an oral non-steroidal anti-inflammatory, review in two days",
      "That is the episcleritis pathway; this presentation is far more serious."],
     ["Topical antibiotic drops and review in one week",
      "There is no infection to treat."],
     ["Reassurance that it is self-limited",
      "Episcleritis is self-limited; scleritis is not."]],
   c=0, cite=c(50)),

 dict(topic="Scleritis", io=IOA, lead="education", slot="prognosis",
   q="A 58-year-old man started treatment for scleritis three days ago. His eye still looks just as inflamed, but his pain is much better. How should this be interpreted?",
   opts=[
     ["This is the expected first sign of response — decreased pain comes before any change in appearance",
      "Correct — the deck flags exactly this, so that an unchanged-looking eye is not read as failure."],
     ["Treatment has failed and should be changed immediately",
      "The deck says appearance lags behind pain."],
     ["The diagnosis was wrong and this is episcleritis",
      "Pain improving on treatment does not reclassify the disease."],
     ["He is at imminent risk of perforation and needs surgery now",
      "Improving pain points the other way."]],
   c=0, cite=c(50)),

 dict(topic="Anterior uveitis", io=IOA, lead="next step", slot="referral",
   q="A 31-year-old man has a painful red eye with a ring of redness at the corneal edge (ciliary flush) and pain in that eye when light is shone into the OTHER eye (consensual photophobia). His pupil is small and irregular. Which is the most appropriate next step?",
   opts=[
     ["Urgent referral to ophthalmology within 24 hours for slit lamp and dilated fundoscopy",
      "Correct — anterior uveitis, where delayed diagnosis may cost vision."],
     ["Topical antibiotic drops and review in 48 hours",
      "Ciliary flush and an irregular pupil rule out simple conjunctivitis."],
     ["Reassurance and artificial tears",
      "These are danger signs, not benign ones."],
     ["Oral antivirals for ten days",
      "There is no dendrite or vesicular rash described."]],
   c=0, cite=c(63)),

 dict(topic="Anterior uveitis", io=IOA, lead="test finding", slot="test finding",
   q="A 40-year-old woman with a painful red eye is found on slit lamp to have white deposits on the back surface of the cornea. What are these called?",
   opts=[
     ["Keratic precipitates", "Correct — white blood cell deposits on the corneal endothelium."],
     ["Drusen", "Those are yellow deposits beneath the retinal pigment epithelium."],
     ["Hard exudates", "Those are lipid deposits in the retina."],
     ["Follicles", "Those are conjunctival, not corneal."]],
   c=0, cite=c(62)),

 dict(topic="Posterior uveitis", io=IOA, lead="first-line", slot="first-line",
   q="A 45-year-old woman has blurred vision, floaters and a patch of missing vision in one eye, with no pain at all. Ophthalmology finds cells in the posterior vitreous and vitreous haze. Which statement about treatment is correct?",
   opts=[
     ["Topical treatment will not work here — an intraocular corticosteroid injection may be required",
      "Correct — this is the key management difference from anterior uveitis."],
     ["Topical corticosteroid drops are the first-line treatment",
      "Posterior disease does not respond to topical therapy."],
     ["Oral doxycycline for seven days is first-line",
      "That treats chlamydial conjunctivitis."],
     ["No treatment is required as it resolves spontaneously",
      "It can last years and threaten vision."]],
   c=0, cite=c(65)),

 dict(topic="Herpes simplex keratitis", io=IOA, lead="first-line", slot="agent/regimen",
   q="A 26-year-old man has a painful red eye with photophobia. Fluorescein under cobalt blue light shows a branching corneal lesion with small knobs at the ends of each branch (terminal end bulbs). Which is the most appropriate treatment?",
   opts=[
     ["Oral antiviral therapy for ten days",
      "Correct — a true dendrite with terminal end bulbs is pathognomonic for herpes simplex."],
     ["Topical corticosteroid drops started today",
      "Specifically prohibited by the primary care provider in active epithelial disease."],
     ["A topical fluoroquinolone for ten days",
      "That treats bacterial disease; this is viral."],
     ["Oral doxycycline for seven days",
      "That treats chlamydial conjunctivitis."]],
   c=0, cite=c(59)),

 dict(topic="Herpes simplex keratitis", io=IOA, lead="avoid", slot="avoid",
   q="A 33-year-old woman has an active herpes simplex epithelial dendrite. Which action should specifically NOT be taken by the primary care provider?",
   opts=[
     ["Prescribing topical glucocorticoid drops",
      "Correct — the deck puts this prohibition in capitals and leaves the decision to ophthalmology."],
     ["Prescribing an oral antiviral",
      "That is the correct treatment."],
     ["Referring for slit lamp examination",
      "Appropriate and expected."],
     ["Staining the cornea with fluorescein",
      "That is how the dendrite was found."]],
   c=0, cite=c(59)),

 dict(topic="Herpes zoster ophthalmicus", io=IOA, lead="test finding", slot="test finding",
   q="A 68-year-old man has a painful vesicular rash over his forehead and one upper eyelid that stops sharply at the midline, and a vesicle on the tip of his nose. What does the nasal-tip lesion indicate?",
   opts=[
     ["Nasociliary branch involvement, and therefore a higher risk of ocular involvement",
      "Correct — Hutchinson sign, and its significance is the ocular risk."],
     ["That the rash will cross the midline within days",
      "Zoster respects the midline; the sign is about ocular risk."],
     ["That the infection is herpes simplex rather than zoster",
      "Simplex is not dermatomal and Hutchinson sign belongs to zoster."],
     ["That the patient is immunocompromised",
      "The sign indicates anatomical spread, not immune status."]],
   c=0, cite=c(58)),

 dict(topic="Herpes zoster ophthalmicus", io=IOA, lead="first-line", slot="first-line",
   q="A 71-year-old woman presents 48 hours after a dermatomal vesicular rash appeared over her forehead and upper lid. Which is the most appropriate initial management?",
   opts=[
     ["Start an oral antiviral now and refer for slit lamp examination and dilated fundoscopy",
      "Correct — within the ideal 72-hour window, and the eye still needs examining."],
     ["Wait for ophthalmology to confirm ocular involvement before starting any antiviral",
      "Delaying wastes the antiviral window."],
     ["Start a topical corticosteroid to reduce inflammation",
      "That decision belongs to ophthalmology."],
     ["Reassure her that no treatment is needed for a dermatomal rash",
      "Ocular zoster is a same-day condition."]],
   c=0, cite=c(59)),

 dict(topic="Corneal ulcer", io=IOA, lead="next step", slot="referral",
   q="A 38-year-old contact lens wearer resists opening a painful watering eye. There is a ring of redness at the corneal edge (ciliary flush) and a white spot on the cornea with surrounding irregularity. Which is the most appropriate next step?",
   opts=[
     ["Emergent referral to ophthalmology",
      "Correct — the deck escalates a corneal ulcer above keratitis's 24-hour urgency to emergent."],
     ["Urgent referral within 24 hours",
      "That is the keratitis threshold; an ulcer is emergent."],
     ["Routine referral within two weeks",
      "Far too slow for a sight-threatening lesion."],
     ["Reassurance and lubricating drops",
      "This is an open corneal sore, not dry eye."]],
   c=0, cite=c(61)),

 dict(topic="Corneal ulcer", io=IOA, lead="education", slot="prognosis",
   q="A 41-year-old man has begun treatment for a corneal ulcer. What should he be told about follow-up and healing?",
   opts=[
     ["He needs review the next day, and most ulcers heal over two to three weeks",
      "Correct — next-day follow-up after starting an anti-infective, with a two to three week course."],
     ["He needs no follow-up, and it should heal in 48 hours",
      "Both halves are wrong for an ulcer."],
     ["He needs review in one month, and it should heal within a year",
      "Far too slow on both counts."],
     ["He needs review in two weeks, and it will not heal without surgery",
      "Most heal medically."]],
   c=0, cite=c(61)),

 dict(topic="Pre-septal cellulitis", io=IOB, lead="next step", slot="escalation",
   q="A 4-year-old boy has a hot, swollen, red left upper lid after a recent sinus infection. The globe itself is white, eye movements are full and painless, and vision is normal. Which is the most appropriate next step?",
   opts=[
     ["Hospital admission for broad-spectrum intravenous antibiotics",
      "Correct — the findings are pre-septal, but the deck admits any child aged five or younger."],
     ["Outpatient oral antibiotics for 10 to 14 days",
      "Appropriate for mild pre-septal disease in an adult, but his age triggers admission."],
     ["Topical antibiotic drops and review in 48 hours",
      "Drops do not treat a soft tissue infection."],
     ["Reassurance and warm compresses",
      "Inadequate for cellulitis."]],
   c=0, cite=c(53)),

 dict(topic="Orbital cellulitis", io=IOA, lead="initial test", slot="initial test",
   q="A 47-year-old woman has a swollen red eyelid, fever, and pain on moving the eye. The globe is proptotic and she has double vision. Which investigation is most appropriate?",
   opts=[
     ["Computed tomography of the orbits and paranasal sinuses with contrast",
      "Correct — post-septal features mean orbital involvement must be imaged."],
     ["Slit lamp examination with fluorescein alone",
      "That assesses the cornea and would miss the orbital collection."],
     ["Conjunctival nucleic acid amplification testing",
      "That is for chlamydial conjunctivitis."],
     ["Fluorescein angiography",
      "That images retinal and choroidal blood flow."]],
   c=0, cite=c(53)),

 dict(topic="Orbital cellulitis", io=IOA, lead="complication", slot="complication",
   q="A 55-year-old man with untreated orbital cellulitis is deteriorating. Which complications does the lecture specifically warn about?",
   opts=[
     ["Intracranial spread causing meningitis or cavernous sinus thrombosis",
      "Correct — the deck's two named complications of untreated infection."],
     ["Corneal perforation and endophthalmitis",
      "That is the undertreated keratitis chain."],
     ["Entropion progressing to trichiasis",
      "That is the trachoma chain."],
     ["Retinal detachment and vitreous haemorrhage",
      "Those are posterior segment problems."]],
   c=0, cite=c(53)),

 dict(topic="Dacryocystitis", io=IOA, lead="first-line", slot="first-line",
   q="A 62-year-old woman has a tender red swelling at the inner corner of her lower eyelid, with purulent material expressible from the lower punctum. She is afebrile, systemically well and reliable. Which is the most appropriate management?",
   opts=[
     ["Outpatient oral antibiotics for ten days with warm compresses",
      "Correct — mild dacryocystitis in a well, reliable patient is managed as an outpatient."],
     ["Hospital admission for intravenous antibiotics for 48 to 72 hours",
      "Reserved for the febrile, acutely ill or unreliable patient."],
     ["Topical antibiotic drops alone",
      "Drops do not reach the lacrimal sac."],
     ["Immediate surgical dacryocystorhinostomy",
      "Surgery follows the acute infection, once patency is assessed."]],
   c=0, cite=c(25)),

 dict(topic="Dacryocystitis", io=IOA, lead="education", slot="prognosis",
   q="A 58-year-old man's acute dacryocystitis has settled on antibiotics. What should he be told about what comes next?",
   opts=[
     ["Probing and irrigation are often needed to assess whether the tear drainage system is open, and surgery may follow",
      "Correct — the underlying obstruction still has to be addressed."],
     ["No further action is needed now the infection has cleared",
      "The obstruction that caused it remains."],
     ["He will need lifelong daily antibiotics",
      "Not the deck's plan."],
     ["He will need annual computed tomography scanning",
      "Not what the deck describes."]],
   c=0, cite=c(25)),

 dict(topic="Dacryoadenitis", io=IOA, lead="first-line", slot="agent/regimen",
   q="A 36-year-old woman has pain, redness and swelling over the outer third of her upper eyelid, with an enlarged node in front of the ear on the same side. Workup points to an inflammatory cause. Which treatment does the lecture give, and how quickly should it work?",
   opts=[
     ["Oral corticosteroids, with a response expected within 48 hours",
      "Correct — the deck's agent and response window for inflammatory dacryoadenitis."],
     ["Oral antibiotics, with a response expected within 48 hours",
      "Antibiotics are the empiric option when the cause is unclear, not for confirmed inflammatory disease."],
     ["Cool compresses alone, with resolution over two weeks",
      "Cool compresses are the viral measure."],
     ["Intravenous antibiotics for 48 to 72 hours",
      "That is the regimen for severe dacryocystitis or post-septal cellulitis."]],
   c=0, cite=c(23)),

 dict(topic="Dacryoadenitis", io=IOA, lead="avoid", slot="avoid",
   q="A 41-year-old man has dacryoadenitis and the cause is not yet clear. Which action should be avoided?",
   opts=[
     ["Starting corticosteroids before bacterial and other infectious causes have been reasonably excluded",
      "Correct — the speaker notes are explicit about this sequence."],
     ["Giving paracetamol for pain",
      "The deck gives analgesia as needed."],
     ["Reassessing after 24 hours of empiric oral antibiotics",
      "That is exactly what the deck suggests when the cause is unclear."],
     ["Monitoring for signs of orbital involvement",
      "The deck requires this."]],
   c=0, cite=cn(23)),

 dict(topic="Chalazion", io=IOA, lead="first-line", slot="first-line",
   q="A 35-year-old woman has a firm, painless lump in her upper eyelid that has been slowly enlarging for three weeks. It is not tender. Which is the most appropriate initial management?",
   opts=[
     ["Warm compresses with gentle massage",
      "Correct — the painless, slowly enlarging nodule is a chalazion, managed conservatively first."],
     ["Incision and drainage today",
      "That is for a persistent hordeolum, and by ophthalmology."],
     ["Oral antibiotics for ten days",
      "A chalazion is a sterile obstruction, not an infection."],
     ["Urgent referral to exclude sebaceous carcinoma",
      "That concern arises with recurrence or persistence beyond two to three months."]],
   c=0, cite=c(21)),

 dict(topic="Chalazion", io=IOA, lead="education", slot="education",
   q="A 29-year-old man is starting warm compresses for a chalazion. What should he be told about the timescale?",
   opts=[
     ["Improvement may take months",
      "Correct — the deck says so, and setting this expectation prevents a premature return."],
     ["It should be gone within 48 hours",
      "That is an antibiotic response time, not a chalazion's course."],
     ["It should be gone within one week",
      "Faster than the deck's expectation."],
     ["It will not improve without surgery",
      "Most resolve conservatively."]],
   c=0, cite=c(21)),

 dict(topic="Chalazion", io=IOA, lead="next step", slot="referral",
   q="A 44-year-old woman has had a lid nodule in the same spot for four months, and it has recurred twice in the past year. Which is the most appropriate next step?",
   opts=[
     ["Refer to ophthalmology to rule out sebaceous carcinoma",
      "Correct — recurrence, or persistence beyond two to three months, triggers this specific concern."],
     ["Continue warm compresses for another three months",
      "Persistence at four months is itself the referral trigger."],
     ["Start oral antibiotics for two weeks",
      "There is no infection."],
     ["Reassure her that recurrence is normal and no action is needed",
      "Recurrence is precisely what the deck says to act on."]],
   c=0, cite=c(21)),

 dict(topic="Hordeolum", io=IOA, lead="next step", slot="escalation",
   q="A 27-year-old man developed a tender red lump at his eyelid margin overnight. Two weeks of warm compresses have not helped and it persists. Which is the most appropriate next step?",
   opts=[
     ["Refer to ophthalmology for incision and drainage",
      "Correct — a hordeolum that has not improved in two weeks meets the deck's referral threshold."],
     ["Continue compresses for another three months",
      "That timescale belongs to a chalazion."],
     ["Start oral corticosteroids",
      "Not part of hordeolum management."],
     ["Perform incision and drainage in the clinic yourself",
      "The deck refers this to ophthalmology."]],
   c=0, cite=c(21)),

 dict(topic="Blepharitis", io=IOA, lead="first-line", slot="first-line",
   q="A 55-year-old woman with rosacea has months of burning, gritty eyes with crusting and scaling at the lash bases and thickened, toothpaste-like secretion from the lid margins. Which is the most appropriate first-line management?",
   opts=[
     ["Lid hygiene", "Correct — the deck's first step, escalating only if two weeks of it fails."],
     ["Topical antibiotic ointment", "Tried only after two weeks of lid hygiene fails."],
     ["Oral antibiotics", "Those come after topical antibiotics in the sequence."],
     ["Urgent ophthalmology referral", "This is a chronic condition managed in primary care first."]],
   c=0, cite=c(19)),

 dict(topic="Blepharitis", io=IOA, lead="education", slot="prognosis",
   q="A 60-year-old man asks whether his blepharitis will be cured. What is the most accurate answer?",
   opts=[
     ["It is chronic and can be controlled rather than cured, though symptoms often improve substantially over weeks",
      "Correct — the deck's exact framing, and an important expectation to set."],
     ["It will be completely cured by a two-week course of lid hygiene",
      "The deck expects improvement, not cure."],
     ["It will resolve on its own within two to three weeks",
      "That is viral conjunctivitis."],
     ["It will progress to corneal ulceration if not cured",
      "The deck does not describe that course."]],
   c=0, cite=c(19)),
]
