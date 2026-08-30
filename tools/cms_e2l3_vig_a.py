# CMS I Exam 2, Lecture 12 Acute Vision Loss — VIGNETTE pool, part A.
# Exam standard (2026-08-26/27): FIVE options, a patient in every stem, each
# wrong option refuted on its own terms, options short with the reasoning in
# the explanation. Part A covers amaurosis fugax, both glaucomas, optic
# neuritis and retinal detachment; part B covers the vascular occlusions,
# papilledema and anterior ischemic optic neuropathy.
#
# Jaquith stated in lecture that she will not test giant cell arteritis as a
# disease in its own right, so it appears here only as the cause of arteritic
# AION and the reason that presentation is an emergency.
SRC = "12. Acute Vision Loss current - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = ("a — Compare and contrast the etiologies, epidemiology, risk factors, clinical "
       "manifestations, differential diagnosis, diagnostic testing, management, patient "
       "education, and prognosis of the acute vision loss disorders")
IOB = ("b — Identify medical care strategies for acute vision loss in adult and elderly "
       "populations")

POOL_A = [

 # ---------------- Amaurosis fugax ----------------
 dict(topic="Amaurosis fugax", io=IOA, lead="diagnosis",
   q="A 68-year-old man describes a curtain descending over the vision of his right eye. It lasted about 40 seconds, there was no pain, and his sight returned completely. He has hypertension and carotid bruits. Which is the most likely diagnosis?",
   opts=[
     ["Amaurosis fugax", "Correct. Transient monocular loss lasting seconds to minutes, then full recovery."],
     ["Central retinal artery occlusion", "That loss is profound and does not resolve on its own."],
     ["Acute angle-closure glaucoma", "That is painful and does not clear spontaneously."],
     ["Retinal detachment", "That curtain persists and worsens rather than lifting."],
     ["Optic neuritis", "That builds over hours to days and hurts on eye movement."]],
   c=0, cite=c(4)),

 dict(topic="Amaurosis fugax", io=IOA, lead="cause",
   q="A 71-year-old woman has had three episodes of painless monocular blackout, each lasting under a minute. Which source does the lecture name as most common?",
   opts=[
     ["A carotid or cardiac embolus", "Correct. Most commonly a transient ischemic attack of retinal origin."],
     ["Retinal vascular spasm", "A recognised cause, but not the most common one."],
     ["Optic nerve demyelination", "That produces optic neuritis, which is not transient in this way."],
     ["Raised intracranial pressure", "That gives papilledema with non-specific, persistent changes."],
     ["Vitreous haemorrhage", "That causes floaters and haze that do not clear in seconds."]],
   c=0, cite=c(5)),

 dict(topic="Amaurosis fugax", io=IOA, lead="reasoning",
   q="A 64-year-old man reports that vision in his left eye went completely dark for about six hours yesterday before returning. Why does this history argue against a transient ischemic attack?",
   opts=[
     ["A transient ischemic attack lasts seconds to minutes", "Correct. Jaquith was explicit that hours puts it outside that window."],
     ["A transient ischemic attack is always painful", "It is painless, which is why pain suggests another cause."],
     ["A transient ischemic attack affects both eyes", "It is characteristically monocular."],
     ["A transient ischemic attack never recovers", "Full recovery is the rule."],
     ["A transient ischemic attack spares the retina", "The retinal circulation is exactly what it involves."]],
   c=0, cite=c(4)),

 dict(topic="Amaurosis fugax", io=IOA, lead="test",
   q="A 70-year-old man has transient monocular vision loss and you suspect a carotid source. Which study does the lecture pair with that suspicion?",
   opts=[
     ["Carotid Doppler ultrasound", "Correct. Echocardiography is the study when a cardiac source is suspected."],
     ["Echocardiogram", "That is the study for a suspected cardiac source."],
     ["Tonometry", "That measures intraocular pressure."],
     ["Lumbar puncture", "That is used when raised intracranial pressure is suspected."],
     ["Temporal artery biopsy", "That is the gold standard for giant cell arteritis."]],
   c=0, cite=c(7)),

 dict(topic="Acute vision loss", io=IOB, lead="next step",
   q="A 66-year-old woman arrives having had sudden painless vision loss in one eye that has now resolved. She has no weakness, numbness or speech difficulty. Which imaging does the lecture say every such patient receives?",
   opts=[
     ["Magnetic resonance angiography", "Correct. Every patient is evaluated for emboli across all the arteries."],
     ["Plain skull radiographs", "These have no role in this evaluation."],
     ["Orbital ultrasound", "That characterises a detachment, not the arterial supply."],
     ["Chest radiograph", "This does not address the arterial source."],
     ["No imaging, since symptoms resolved", "Resolution does not remove the need to find the source."]],
   c=0, cite=c(7)),

 dict(topic="Acute vision loss", io=IOB, lead="reasoning",
   q="A 59-year-old man with sudden monocular vision loss and no other neurological findings asks why he is being worked up so aggressively. Which principle did the lecturer stress twice?",
   opts=[
     ["Sudden vision loss is a stroke until proven otherwise", "Correct. A stroke can present with acute vision loss and nothing else."],
     ["Sudden vision loss is benign if it resolves", "Resolution does not lower the risk."],
     ["Sudden vision loss is a stroke only with weakness", "It can occur with no other symptom at all."],
     ["Sudden vision loss rarely needs referral", "Every one of these presentations needs urgent evaluation."],
     ["Sudden vision loss is usually migraine", "Migraine is on the list but is not the working assumption."]],
   c=0, cite=c(7)),

 dict(topic="Amaurosis fugax", io=IOA, lead="prognosis",
   q="A 67-year-old woman with amaurosis fugax asks what happens next. What does the lecture give as the outlook?",
   opts=[
     ["About 85% recover fully", "Correct, and the remainder progress to a central retinal artery occlusion."],
     ["Nearly all progress to permanent blindness", "The large majority recover fully."],
     ["About half lose vision permanently", "The figure given is far more favourable."],
     ["Recovery depends on surgery", "Recovery is usually spontaneous once the cause is treated."],
     ["The second eye is always affected", "That is not stated."]],
   c=0, cite=c(8)),

 dict(topic="Amaurosis fugax", io=IOA, lead="treatment",
   q="A 63-year-old man's transient monocular vision loss is traced to a carotid embolus with significant plaque. Which intervention does the lecture pair with that finding?",
   opts=[
     ["Carotid endarterectomy", "Correct. Calcium channel blockers are reserved for vascular spasm."],
     ["Calcium channel blockers", "Those are used for Raynaud's and vascular spasm."],
     ["Laser peripheral iridotomy", "That is the definitive treatment for angle-closure glaucoma."],
     ["Intravenous methylprednisolone", "That treats arteritic optic neuropathy."],
     ["Scleral buckle", "That repairs a retinal detachment."]],
   c=0, cite=c(8)),

 dict(topic="Amaurosis fugax", io=IOA, lead="treatment",
   q="A 69-year-old man has amaurosis fugax and you want to reduce his stroke risk. Which therapy does the lecture name?",
   opts=[
     ["Aspirin and clopidogrel", "Correct, given to reduce cerebrovascular accident risk."],
     ["Topical timolol", "That lowers intraocular pressure in glaucoma."],
     ["Oral acetazolamide", "That lowers intraocular pressure, not stroke risk."],
     ["High-dose vitamin A", "Vitamin A toxicity is a cause of papilledema."],
     ["Pilocarpine drops", "That is a topical agent for angle-closure glaucoma."]],
   c=0, cite=c(8)),

 # ---------------- Acute angle-closure glaucoma ----------------
 dict(topic="Angle-closure glaucoma", io=IOA, lead="diagnosis",
   q="A 62-year-old woman has sudden severe right eye pain, a headache, nausea and vomiting. She sees coloured halos around lights and her cornea looks hazy. Which is the most likely diagnosis?",
   opts=[
     ["Acute angle-closure glaucoma", "Correct. Pain, halos and systemic upset with a hazy cornea."],
     ["Chronic open-angle glaucoma", "That is painless and gradual in most patients."],
     ["Optic neuritis", "Pain there is on eye movement, without halos or vomiting."],
     ["Central retinal artery occlusion", "That is painless."],
     ["Amaurosis fugax", "That is painless and lasts seconds to minutes."]],
   c=0, cite=c(16)),

 dict(topic="Angle-closure glaucoma", io=IOA, lead="pathophysiology",
   q="A 58-year-old man has acute angle-closure glaucoma. What is happening inside his eye?",
   opts=[
     ["The iris blocks the drainage circuit", "Correct, and intraocular pressure rises dramatically."],
     ["The trabecular meshwork ages abnormally", "That is the mechanism of the chronic open-angle form."],
     ["The retina separates from its bed", "That is retinal detachment."],
     ["Intracranial pressure compresses the disc", "That is papilledema."],
     ["A thrombus occludes the central vein", "That is central retinal vein occlusion."]],
   c=0, cite=c(14)),

 dict(topic="Angle-closure glaucoma", io=IOA, lead="test",
   q="A 61-year-old woman has a painful red eye with a hazy cornea. Which measurement does the lecture make first?",
   opts=[
     ["Intraocular pressure", "Correct, by tonometry or gonioscopy; expect 40 to 80 mmHg."],
     ["Erythrocyte sedimentation rate", "That is for suspected arteritic optic neuropathy."],
     ["Cerebrospinal fluid opening pressure", "That is for papilledema."],
     ["Colour vision testing", "That is part of the optic neuritis workup."],
     ["Carotid Doppler", "That looks for an embolic source."]],
   c=0, cite=c(17)),

 dict(topic="Angle-closure glaucoma", io=IOA, lead="finding",
   q="A 65-year-old man with a painful eye has tonometry performed. Which pressure range does the lecture give for acute angle closure?",
   opts=[
     ["40 to 80 mmHg", "Correct."],
     ["10 to 21 mmHg", "That is the normal range."],
     ["22 to 30 mmHg", "Too low for the acute presentation described."],
     ["90 to 120 mmHg", "Above the range the lecture gives."],
     ["Pressure is characteristically normal", "It is dramatically elevated."]],
   c=0, cite=c(17)),

 dict(topic="Angle-closure glaucoma", io=IOB, lead="treatment",
   q="A 60-year-old woman has acute angle-closure glaucoma with an intraocular pressure of 62 mmHg. Which is the definitive treatment?",
   opts=[
     ["Laser peripheral iridotomy", "Correct, performed one to two days after onset."],
     ["Topical pilocarpine", "An initial medical measure, not definitive."],
     ["Intravenous acetazolamide", "That lowers pressure rapidly but is not definitive."],
     ["Latanoprost drops", "That is first-line for the chronic open-angle form."],
     ["Observation", "The pressure will blind the eye if untreated."]],
   c=0, cite=c(20)),

 dict(topic="Angle-closure glaucoma", io=IOB, lead="treatment",
   q="A 57-year-old man has acute angle closure and a very high intraocular pressure. Which does the lecture give as the intravenous agent, followed by mannitol or isosorbide?",
   opts=[
     ["Acetazolamide", "Correct, a carbonic anhydrase inhibitor used to drop the pressure rapidly."],
     ["Methylprednisolone", "That treats arteritic anterior ischemic optic neuropathy."],
     ["Clopidogrel", "That reduces stroke risk after an embolic event."],
     ["Alteplase", "Thrombolytic infusion is used in central retinal artery occlusion."],
     ["Famotidine", "That is ulcer prophylaxis alongside long-term steroids."]],
   c=0, cite=c(20)),

 dict(topic="Angle-closure glaucoma", io=IOA, lead="risk factor",
   q="A 59-year-old woman with a history of anterior uveitis is started on a new inhaler and later develops a painful red eye. Which class does the lecture flag as a risk factor?",
   opts=[
     ["Nebulized bronchodilators", "Correct, listed alongside systemic anticholinergics such as atropine."],
     ["Beta-blocker eye drops", "Those are used to treat glaucoma, not to precipitate it."],
     ["Prostaglandin analogues", "Those lower intraocular pressure."],
     ["Carbonic anhydrase inhibitors", "Those lower intraocular pressure."],
     ["Calcium channel blockers", "Those are used for vascular spasm."]],
   c=0, cite=c(14)),

 dict(topic="Angle-closure glaucoma", io=IOA, lead="education",
   q="A 63-year-old man with angle-closure glaucoma is about to start a medication for overactive bladder. Which counselling point applies?",
   opts=[
     ["Anticholinergic drugs can worsen his glaucoma", "Correct; the lecture names systemic anticholinergics such as atropine."],
     ["Anticholinergic drugs will lower his pressure", "They act in the opposite direction."],
     ["Anticholinergic drugs are safe in any glaucoma", "They are a named risk factor."],
     ["Anticholinergic drugs cause optic neuritis", "That is inflammatory, not drug-induced here."],
     ["Anticholinergic drugs cause papilledema", "Vitamin A toxicity, not anticholinergics, is the drug cause listed."]],
   c=0, cite=c(14)),

 dict(topic="Angle-closure glaucoma", io=IOA, lead="diagnosis",
   q="A 64-year-old man is admitted with an intractable headache localised behind one eye. Multiple clinicians have treated him for migraine. On examination his eye is red and his vision is reduced. Which diagnosis should be excluded?",
   opts=[
     ["Angle-closure glaucoma", "Correct. The lecture gave this exact case as a missed presentation."],
     ["Papilledema", "That gives non-specific visual change without a red eye."],
     ["Optic neuritis", "That hurts on eye movement rather than presenting as a headache."],
     ["Retinal detachment", "That is painless and shows a field defect."],
     ["Amaurosis fugax", "That resolves within minutes."]],
   c=0, cite=c(16)),

 # ---------------- Chronic open-angle glaucoma ----------------
 dict(topic="Open-angle glaucoma", io=IOA, lead="diagnosis",
   q="A 58-year-old African American man has no eye symptoms. Routine screening shows an increased cup-to-disc ratio, splinter haemorrhages at the rim and a bilateral pressure of 26 mmHg. Which is the most likely diagnosis?",
   opts=[
     ["Chronic open-angle glaucoma", "Correct. Asymptomatic, with optic nerve changes on an open angle."],
     ["Acute angle-closure glaucoma", "That is painful with a hazy cornea and a closed angle."],
     ["Papilledema", "That swells the disc outward rather than cupping it."],
     ["Optic neuritis", "That is unilateral and painful on eye movement."],
     ["Anterior ischemic optic neuropathy", "That causes sudden loss with a pale swollen disc."]],
   c=0, cite=c(18)),

 dict(topic="Open-angle glaucoma", io=IOA, lead="finding",
   q="A 61-year-old woman is found to have chronic open-angle glaucoma. Which optic nerve finding did the lecturer call the classic sign?",
   opts=[
     ["Optic nerve cupping", "Correct, and the finding a non-ophthalmologist can most readily see."],
     ["Disc elevation with blurred margins", "That is papilledema."],
     ["A cherry-red spot at the fovea", "That is central retinal artery occlusion."],
     ["Blood and thunder fundus", "That is central retinal vein occlusion."],
     ["A pale, swollen disc", "That is anterior ischemic optic neuropathy."]],
   c=0, cite=c(19)),

 dict(topic="Open-angle glaucoma", io=IOA, lead="symptom",
   q="A 66-year-old man with untreated chronic open-angle glaucoma says he feels as though he is looking down a tube. Which finding does this describe?",
   opts=[
     ["Loss of peripheral vision first", "Correct; patients call it tunnel vision, and central sight is preserved longest."],
     ["Loss of central vision first", "Peripheral field is lost before central."],
     ["Loss of colour vision", "That belongs to optic neuritis."],
     ["A curtain descending from above", "That suggests detachment or amaurosis fugax."],
     ["Transient blackout", "That is amaurosis fugax."]],
   c=0, cite=c(16)),

 dict(topic="Open-angle glaucoma", io=IOA, lead="pathophysiology",
   q="A 70-year-old woman has chronic open-angle glaucoma. Which abnormality does the lecture describe?",
   opts=[
     ["Trabecular meshwork change with aging", "Correct, next to the canal of Schlemm, damaging the optic nerve."],
     ["The iris obstructing the drainage angle", "That is the acute angle-closure mechanism."],
     ["A thrombus in the central retinal vein", "That is vein occlusion."],
     ["Optic nerve demyelination", "That is optic neuritis."],
     ["Raised intracranial pressure", "That is papilledema."]],
   c=0, cite=c(15)),

 dict(topic="Open-angle glaucoma", io=IOA, lead="finding",
   q="A 67-year-old man with optic nerve changes has an intraocular pressure of 18 mmHg. How does the lecture describe pressure in the chronic open-angle form?",
   opts=[
     ["It may be normal or elevated", "Correct; nerve damage occurs with or without raised pressure."],
     ["It is always above 40 mmHg", "That range belongs to acute angle closure."],
     ["It is always normal", "It may well be elevated."],
     ["It is always below normal", "Low pressure is not a feature."],
     ["It cannot be measured in this form", "Tonometry and gonioscopy are both used."]],
   c=0, cite=c(18)),

 dict(topic="Open-angle glaucoma", io=IOB, lead="treatment",
   q="A 64-year-old woman is newly diagnosed with chronic open-angle glaucoma. Which does the lecture list as first-line?",
   opts=[
     ["Latanoprost", "Correct, with tafluprost and timolol drops."],
     ["Laser peripheral iridotomy", "That is definitive treatment for the angle-closure form."],
     ["Intravenous mannitol", "That is used acutely for a very high pressure."],
     ["Oral corticosteroids", "Those treat arteritic optic neuropathy."],
     ["Anterior chamber paracentesis", "That is used in central retinal artery occlusion."]],
   c=0, cite=c(21)),

 dict(topic="Open-angle glaucoma", io=IOB, lead="treatment",
   q="A 72-year-old man has chronic open-angle glaucoma that continues to progress on maximal drops. Which does the lecture give next?",
   opts=[
     ["Laser trabeculoplasty", "Correct, used when the disease is refractory or advanced."],
     ["A stronger prostaglandin analogue", "The lecture moves to laser or incisional surgery instead."],
     ["Observation alone", "Progression on treatment calls for escalation."],
     ["Systemic corticosteroids", "Those are not used for this."],
     ["Carotid endarterectomy", "That addresses an embolic source."]],
   c=0, cite=c(21)),

 dict(topic="Glaucoma", io=IOA, lead="comparison",
   q="A 55-year-old woman asks which type of glaucoma is more common. What should you tell her?",
   opts=[
     ["The chronic open-angle form", "Correct, much more common than acute closed-angle."],
     ["The acute closed-angle form", "That is the less common of the two."],
     ["They occur equally often", "The lecture states one is much more common."],
     ["Neither occurs after age 40", "Adults over 40 are specifically at risk."],
     ["Only the acute form causes blindness", "Both blind the patient if untreated."]],
   c=0, cite=c(15)),

 # ---------------- Optic neuritis ----------------
 dict(topic="Optic neuritis", io=IOA, lead="diagnosis",
   q="A 29-year-old woman has had blurred vision in her left eye worsening over three days, and it hurts when she moves the eye. Colours look washed out. The disc appears normal. Which is the most likely diagnosis?",
   opts=[
     ["Optic neuritis", "Correct. Painful eye movement, colour desaturation and an often normal disc."],
     ["Angle-closure glaucoma", "That is acutely painful at rest with a hazy cornea."],
     ["Central retinal artery occlusion", "That is painless and sudden over seconds."],
     ["Papilledema", "That is bilateral disc swelling from raised intracranial pressure."],
     ["Retinal detachment", "That is painless with flashes, floaters and a field defect."]],
   c=0, cite=c(23)),

 dict(topic="Optic neuritis", io=IOA, lead="epidemiology",
   q="A 26-year-old woman is diagnosed with optic neuritis. Which patient profile does the lecture describe for this condition?",
   opts=[
     ["Aged 18 to 45 and mostly female", "Correct; about 75% are women."],
     ["Aged over 60 and mostly male", "That fits the ischemic and occlusive diseases."],
     ["Aged over 55 and mostly female", "That fits arteritic optic neuropathy."],
     ["Children under 10", "Not the group described."],
     ["Aged 40 to 60 and mostly male", "That fits non-arteritic optic neuropathy."]],
   c=0, cite=c(23)),

 dict(topic="Optic neuritis", io=IOA, lead="finding",
   q="A 31-year-old man with optic neuritis has a swinging flashlight test performed. Which sign does the lecture name?",
   opts=[
     ["A relative afferent pupillary defect", "Correct, also called a Marcus Gunn pupil."],
     ["Optic nerve cupping", "That belongs to chronic glaucoma."],
     ["A cherry-red spot", "That belongs to arterial occlusion."],
     ["Cotton wool spots", "Those are seen in vein occlusion."],
     ["A hazy cornea", "That belongs to acute angle closure."]],
   c=0, cite=c(23)),

 dict(topic="Optic neuritis", io=IOB, lead="test",
   q="A 27-year-old woman has optic neuritis. Which imaging does the lecture specify?",
   opts=[
     ["MRI of brain and orbits, with and without contrast", "Correct, looking for demyelinating lesions."],
     ["CT of the orbits without contrast", "Not the study named."],
     ["Orbital ultrasound", "That is used for retinal detachment."],
     ["Carotid Doppler", "That looks for an embolic source."],
     ["Fluorescein angiography", "That is used for the retinal vascular occlusions."]],
   c=0, cite=c(24)),

 dict(topic="Optic neuritis", io=IOB, lead="next step",
   q="A 33-year-old woman with optic neuritis has an MRI showing three characteristic demyelinating lesions. What does the lecture say happens next?",
   opts=[
     ["Referral to neurology or neuro-ophthalmology", "Correct, once at least two such lesions are present."],
     ["Reassurance and discharge", "Those lesions require onward referral."],
     ["Immediate laser iridotomy", "That treats angle-closure glaucoma."],
     ["Temporal artery biopsy", "That investigates giant cell arteritis."],
     ["Lumbar puncture to lower pressure", "That belongs to the papilledema workup."]],
   c=0, cite=c(24)),

 dict(topic="Optic neuritis", io=IOA, lead="prognosis",
   q="A 28-year-old man with optic neuritis asks whether his sight will return. What does the lecture say?",
   opts=[
     ["Vision usually recovers spontaneously", "Correct; it begins improving within weeks and is usually normal within a year."],
     ["Vision loss is permanent", "Spontaneous recovery is the rule."],
     ["Vision returns only after surgery", "Surgery has no role."],
     ["Vision worsens over years", "That is not the described course."],
     ["Recovery requires lifelong drops", "Drops are used in glaucoma, not here."]],
   c=0, cite=c(24)),

 dict(topic="Optic neuritis", io=IOA, lead="education",
   q="A 30-year-old woman has had a second episode of optic neuritis in two years. Which point should you raise with her?",
   opts=[
     ["Recurrence raises her risk of multiple sclerosis", "Correct, which is why the underlying cause is pursued."],
     ["Recurrence means the first episode was misdiagnosed", "Recurrence is a recognised pattern."],
     ["Recurrence means she will go blind", "Recovery is still usually good."],
     ["Recurrence indicates glaucoma", "That is a different disease entirely."],
     ["Recurrence requires no further workup", "It is precisely what prompts further workup."]],
   c=0, cite=c(24)),

 # ---------------- Retinal detachment ----------------
 dict(topic="Retinal detachment", io=IOA, lead="diagnosis",
   q="A 63-year-old myopic man reports a shower of floaters and flashing lights three days ago. Since yesterday a dark shadow has spread across the outer half of his vision. There is no pain. Which is the most likely diagnosis?",
   opts=[
     ["Retinal detachment", "Correct. Flashes and floaters from the tear, then an advancing field defect."],
     ["Amaurosis fugax", "That lasts seconds to minutes and clears completely."],
     ["Central retinal vein occlusion", "That causes sudden painless loss without preceding flashes."],
     ["Optic neuritis", "That is painful on eye movement with colour loss."],
     ["Angle-closure glaucoma", "That is acutely painful with halos and vomiting."]],
   c=0, cite=c(27)),

 dict(topic="Retinal detachment", io=IOA, lead="symptom",
   q="A 68-year-old woman notices new flashing lights and floaters. What do these represent?",
   opts=[
     ["A retinal tear", "Correct; the detachment commonly follows a tear or hole."],
     ["Raised intracranial pressure", "That gives flickering vision with headache and vomiting."],
     ["Optic nerve inflammation", "That causes painful movement and colour loss."],
     ["Venous thrombosis", "That produces sudden painless loss."],
     ["Corneal oedema", "That produces halos and haze."]],
   c=0, cite=c(27)),

 dict(topic="Retinal detachment", io=IOA, lead="reasoning",
   q="A 71-year-old man with a retinal detachment suddenly loses vision in the whole eye rather than just a segment. Which development explains this?",
   opts=[
     ["The macula has become involved", "Correct; macular involvement causes sudden loss in the affected eye."],
     ["The intraocular pressure has risen", "Pressure is not the mechanism here."],
     ["The optic nerve has demyelinated", "That is optic neuritis."],
     ["A second tear has formed anteriorly", "Anterior tears affect peripheral field."],
     ["The vitreous has cleared", "That would not cause loss of vision."]],
   c=0, cite=c(27)),

 dict(topic="Retinal detachment", io=IOA, lead="risk factor",
   q="A 54-year-old woman had cataract extraction last year and is highly myopic. Which condition is she at increased risk of?",
   opts=[
     ["Retinal detachment", "Correct; myopia and cataract extraction are both listed risk factors."],
     ["Optic neuritis", "That is associated with demyelinating and autoimmune disease."],
     ["Papilledema", "That follows raised intracranial pressure."],
     ["Angle-closure glaucoma", "Anticholinergics and uveitis are its listed risks."],
     ["Amaurosis fugax", "That follows embolic disease."]],
   c=0, cite=c(26)),

 dict(topic="Retinal detachment", io=IOA, lead="test",
   q="A 66-year-old man has a suspected retinal detachment but the view on fundoscopy is poor. Which study does the lecture prefer?",
   opts=[
     ["Ocular ultrasound", "Correct, more sensitive than fundoscopy and it types the detachment."],
     ["Fluorescein angiography", "That is used in the vascular occlusions."],
     ["MRI of the orbits", "That is the optic neuritis study."],
     ["Gonioscopy", "That assesses the drainage angle."],
     ["Lumbar puncture", "That assesses intracranial pressure."]],
   c=0, cite=c(29)),

 dict(topic="Retinal detachment", io=IOB, lead="next step",
   q="A 70-year-old woman has a retinal detachment confirmed on ultrasound. Which is the appropriate disposition?",
   opts=[
     ["Immediate referral for surgical repair", "Correct; the lecture calls it an emergency."],
     ["Routine ophthalmology clinic in a month", "The delay would cost her the eye."],
     ["Topical pressure-lowering drops", "Those treat glaucoma."],
     ["Oral corticosteroids and review", "Those treat arteritic optic neuropathy."],
     ["Observation with head positioning", "Position changes the symptom, not the disease."]],
   c=0, cite=c(30)),

 dict(topic="Retinal detachment", io=IOB, lead="treatment",
   q="A 59-year-old man needs repair of a retinal detachment. Which does the lecture list as an option?",
   opts=[
     ["Scleral buckle", "Correct, with vitrectomy, pneumatic retinopexy, cryotherapy and laser photocoagulation."],
     ["Peripheral iridotomy", "That treats angle-closure glaucoma."],
     ["Trabeculoplasty", "That treats open-angle glaucoma."],
     ["Temporal artery biopsy", "That is a diagnostic procedure for giant cell arteritis."],
     ["Anterior chamber paracentesis", "That is used in arterial occlusion."]],
   c=0, cite=c(30)),

 dict(topic="Retinal detachment", io=IOA, lead="finding",
   q="A 65-year-old woman undergoes dilated ophthalmoscopy for suspected detachment. Which appearance does the lecture describe?",
   opts=[
     ["An elevated grey area with folds", "Correct, well demarcated and pigmented, with orange crescent-shaped tears."],
     ["A cherry-red spot at the fovea", "That is arterial occlusion."],
     ["Blood and thunder haemorrhages", "That is venous occlusion."],
     ["A deeply cupped disc", "That is chronic glaucoma."],
     ["An elevated disc with blurred margins", "That is papilledema."]],
   c=0, cite=c(29)),

 dict(topic="Acute vision loss", io=IOA, lead="reasoning",
   q="A 69-year-old man says a curtain came across his vision. Which additional detail best separates retinal detachment from amaurosis fugax?",
   opts=[
     ["Whether the curtain lifted within minutes", "Correct. Amaurosis fugax resolves; a detachment persists and advances."],
     ["Whether the eye was painful", "Both are painless."],
     ["Whether one eye was affected", "Both are typically monocular."],
     ["Whether he has hypertension", "It is a risk factor for several of these."],
     ["Whether he is over 50", "Both occur in this age group."]],
   c=0, cite=c(27)),
]
