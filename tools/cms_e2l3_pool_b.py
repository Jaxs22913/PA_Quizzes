# CMS I Exam 2, Lecture 12 Acute Vision Loss — OBJECTIVE pool, part B.
# Diagnostic testing, management, patient education and prognosis, plus the
# differential-diagnosis facet of the objective.
SRC = "12. Acute Vision Loss current - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = ("a — Compare and contrast the etiologies, epidemiology, risk factors, clinical "
       "manifestations, differential diagnosis, diagnostic testing, management, patient "
       "education, and prognosis of the acute vision loss disorders")
IOB = ("b — Identify medical care strategies for acute vision loss in adult and elderly "
       "populations")

POOL_B = [

 # ---------------- Diagnostic testing ----------------
 dict(topic="Amaurosis fugax", io=IOA, lead="test",
   q="A 69-year-old man with amaurosis fugax is investigated for a cardiac source. Which study does the lecture pair with that?",
   opts=[
     ["Echocardiogram", "Correct; carotid Doppler is used for a carotid source."],
     ["Carotid Doppler", "That investigates a carotid source."],
     ["Fluorescein angiography", "That assesses retinal perfusion."],
     ["Ocular ultrasound", "That types a retinal detachment."],
     ["Lumbar puncture", "That measures intracranial pressure."]],
   c=0, cite=c(7)),

 dict(topic="Glaucoma", io=IOA, lead="test",
   q="A 63-year-old woman is being screened for glaucoma. Which two instruments does the lecture name?",
   opts=[
     ["Tonometry and gonioscopy", "Correct; tonometry measures pressure, gonioscopy views the angle."],
     ["Ophthalmoscopy and lumbar puncture", "Lumbar puncture belongs to the papilledema workup."],
     ["Ultrasound and angiography", "Those belong to detachment and vascular occlusion."],
     ["MRI and CT", "Those exclude a mass lesion in papilledema."],
     ["Slit lamp and colour vision testing", "Those belong to the optic neuritis exam."]],
   c=0, cite=c(18)),

 dict(topic="Optic neuritis", io=IOA, lead="test",
   q="A 28-year-old woman with optic neuritis is referred. Which components does the lecture list in the ophthalmic examination?",
   opts=[
     ["Slit lamp, dilated fundoscopy and colour vision", "Correct, with a neurological examination."],
     ["Tonometry and gonioscopy", "Those assess glaucoma."],
     ["Carotid Doppler and echocardiography of the heart", "Those look for an embolic source."],
     ["Lumbar puncture and CT", "Those belong to the papilledema workup."],
     ["Fluorescein angiography", "That assesses retinal perfusion."]],
   c=0, cite=c(24)),

 dict(topic="Optic neuritis", io=IOA, lead="finding",
   q="A 31-year-old man with optic neuritis has an MRI. How many characteristic demyelinating lesions trigger the onward referral described?",
   opts=[
     ["At least two", "Correct, prompting neurology or neuro-ophthalmology referral."],
     ["At least one", "The threshold given is higher."],
     ["At least five", "Higher than the threshold given."],
     ["Any number, if contrast enhancing", "Number, not enhancement, is the stated threshold."],
     ["Lesion count does not affect referral", "The lecture gives a specific threshold."]],
   c=0, cite=c(24)),

 dict(topic="Vascular occlusion", io=IOA, lead="test",
   q="A 66-year-old man has a retinal vascular occlusion. Which two studies does the lecture name as confirmatory?",
   opts=[
     ["Colour fundus photography and fluorescein angiography", "Correct, used for both the arterial and venous occlusions."],
     ["Tonometry and gonioscopy of the anterior drainage angle", "Those assess glaucoma."],
     ["MRI and lumbar puncture", "Those belong to the papilledema workup."],
     ["Ocular ultrasound", "That types a retinal detachment."],
     ["Temporal artery biopsy", "That investigates giant cell arteritis."]],
   c=0, cite=c(39)),

 dict(topic="Retinal detachment", io=IOA, lead="test",
   q="A 67-year-old woman has a suspected retinal detachment. What advantage does the lecture give for ultrasound?",
   opts=[
     ["It is more sensitive than the fundoscopic exam", "Correct, and it determines the type of detachment."],
     ["It measures intraocular pressure", "That is tonometry."],
     ["It visualises demyelinating lesions", "That is MRI."],
     ["It confirms raised intracranial pressure", "That is lumbar puncture."],
     ["It identifies the embolic source", "That is carotid Doppler."]],
   c=0, cite=c(29)),

 dict(topic="AAION", io=IOA, lead="test",
   q="A 76-year-old woman is being assessed for arteritic optic neuropathy. What role does the lecture give the inflammatory markers?",
   opts=[
     ["They help rule the diagnosis in or out", "Correct; erythrocyte sedimentation rate and C-reactive protein are markedly raised."],
     ["They confirm the diagnosis definitively", "Biopsy is the gold standard."],
     ["They are normal in this condition", "They are characteristically raised."],
     ["They guide the choice of eye drops", "Drops are not the treatment."],
     ["They replace the need for referral", "Referral is emergent regardless."]],
   c=0, cite=c(51)),

 dict(topic="Papilledema", io=IOA, lead="test",
   q="A 39-year-old man has papilledema. Which finding on lumbar puncture confirms the mechanism?",
   opts=[
     ["An increased opening pressure", "Correct, confirming raised intracranial pressure."],
     ["A raised white cell count", "That would indicate infection, not the pressure itself."],
     ["A low glucose level", "That would suggest bacterial meningitis, not the mechanism here."],
     ["Xanthochromia", "That suggests subarachnoid haemorrhage."],
     ["A normal opening pressure", "That would not confirm it."]],
   c=0, cite=c(46)),

 # ---------------- Management ----------------
 dict(topic="Amaurosis fugax", io=IOB, lead="treatment",
   q="A 67-year-old man has amaurosis fugax. What does the lecture identify as the core of management?",
   opts=[
     ["Treat the underlying cause", "Correct; the lecturer called this the essential point."],
     ["Lower the intraocular pressure", "That is glaucoma management."],
     ["Start high-dose corticosteroids", "Those treat arteritic optic neuropathy."],
     ["Arrange surgical reattachment", "That treats detachment."],
     ["Observe without intervention", "The cause must be found and treated."]],
   c=0, cite=c(8)),

 dict(topic="Amaurosis fugax", io=IOB, lead="treatment",
   q="A 64-year-old woman has amaurosis fugax attributed to vascular spasm from Raynaud's. Which drug class does the lecture use?",
   opts=[
     ["Calcium channel blockers", "Correct, for the vasospastic mechanism."],
     ["Beta-blockers", "Those are used as drops for glaucoma."],
     ["Corticosteroids", "Those treat arteritic optic neuropathy."],
     ["Carbonic anhydrase inhibitors", "Those lower intraocular pressure."],
     ["Antiplatelet agents alone", "Those address embolic, not vasospastic, disease."]],
   c=0, cite=c(8)),

 dict(topic="Angle-closure glaucoma", io=IOB, lead="treatment",
   q="A 60-year-old man presents with acute angle closure. Which topical agents does the lecture instil first?",
   opts=[
     ["Pilocarpine or timolol", "Correct, a topical alpha-blocker or beta-blocker."],
     ["Latanoprost or tafluprost", "Those are first-line for the chronic form."],
     ["Prednisolone drops", "Steroid drops are not the described treatment."],
     ["Atropine drops", "Anticholinergics worsen angle closure."],
     ["Antibiotic drops", "There is no infection to treat."]],
   c=0, cite=c(20)),

 dict(topic="Angle-closure glaucoma", io=IOB, lead="treatment",
   q="A 62-year-old woman has laser peripheral iridotomy planned. What does the lecture say the procedure achieves?",
   opts=[
     ["Fluid flows from the posterior to the anterior chamber", "Correct, bypassing the blocked circuit."],
     ["It reattaches the retina", "That is detachment surgery."],
     ["It removes carotid plaque", "That is endarterectomy."],
     ["It drains cerebrospinal fluid", "That is lumbar puncture."],
     ["It dissolves an embolus lodged in the retinal artery", "That is thrombolysis."]],
   c=0, cite=c(20)),

 dict(topic="Glaucoma", io=IOB, lead="treatment",
   q="A 66-year-old man asks what the definitive treatment for glaucoma is. What does the lecture state?",
   opts=[
     ["Surgery", "Correct, for both the acute and chronic forms."],
     ["Lifelong eye drops", "Some patients remain on drops, but that is not definitive."],
     ["Oral acetazolamide", "That is a temporising measure."],
     ["Laser photocoagulation of the retina", "That treats retinal tears."],
     ["Carotid endarterectomy", "That addresses embolic disease."]],
   c=0, cite=c(13)),

 dict(topic="Retinal detachment", io=IOB, lead="treatment",
   q="A 65-year-old man has a retinal detachment. What timeframe does the lecture give for surgical repair?",
   opts=[
     ["Urgently, or within a week depending on type", "Correct."],
     ["Within three months", "Far beyond the window given."],
     ["Only if vision fails to improve", "Repair is not conditional on that."],
     ["At the next routine clinic", "The delay would cost the eye."],
     ["Immediately in every case, without exception", "The type of detachment influences the timing."]],
   c=0, cite=c(30)),

 dict(topic="CRVO", io=IOB, lead="next step",
   q="A 68-year-old woman has a central retinal vein occlusion. What does the lecture give as the purpose of urgent referral?",
   opts=[
     ["To restore blood flow", "Correct, alongside evaluating the underlying disorders."],
     ["To lower intracranial pressure", "That is papilledema management."],
     ["To reattach the retina", "That is detachment surgery."],
     ["To biopsy the temporal artery", "That investigates giant cell arteritis."],
     ["To begin corticosteroids", "Those treat arteritic optic neuropathy."]],
   c=0, cite=c(34)),

 dict(topic="CRAO", io=IOB, lead="treatment",
   q="A 72-year-old man has a central retinal artery occlusion. Why does the lecture perform anterior chamber paracentesis?",
   opts=[
     ["To lower the intraocular pressure", "Correct, fluid is withdrawn from the eye with a needle."],
     ["To sample the vitreous for culture", "There is no infection to sample."],
     ["To deliver a drug into the retina", "That is the intra-arterial thrombolytic route."],
     ["To reattach the retina mechanically", "That is detachment surgery."],
     ["To measure intracranial pressure", "That is lumbar puncture."]],
   c=0, cite=c(40)),

 dict(topic="Papilledema", io=IOB, lead="treatment",
   q="A 43-year-old woman has papilledema from an identified cause. What does the lecture give as management?",
   opts=[
     ["Treat the underlying disorder", "Correct, after imaging and lumbar puncture."],
     ["Topical pressure-lowering drops", "The pressure is intracranial, not intraocular."],
     ["Laser iridotomy", "That treats angle-closure glaucoma."],
     ["Antiplatelet therapy", "That reduces embolic stroke risk."],
     ["Surgical reattachment", "That treats detachment."]],
   c=0, cite=c(46)),

 dict(topic="Acute vision loss", io=IOB, lead="next step",
   q="A 78-year-old woman presents to a primary care clinic with sudden vision loss in one eye. What does the lecture direct the clinician to do?",
   opts=[
     ["Refer emergently to ophthalmology", "Correct, for anyone over 50 with sudden visual loss."],
     ["Prescribe drops and review in a week", "None of these diagnoses tolerates that delay."],
     ["Order outpatient imaging and wait", "The referral is not deferred for results."],
     ["Patch the eye and reassure", "Neither addresses a sight-threatening cause."],
     ["Refer only if pain develops", "Most of these are painless."]],
   c=0, cite=c(51)),

 # ---------------- Patient education ----------------
 dict(topic="Glaucoma", io=IOB, lead="education",
   q="A 47-year-old man asks how glaucoma is usually picked up. What does the lecturer advise for patients?",
   opts=[
     ["Annual eye examinations", "Correct; screening is what finds the asymptomatic chronic form."],
     ["Home tonometry", "Not the advice given."],
     ["Annual carotid ultrasound", "That screens for embolic disease."],
     ["Nothing, until symptoms appear", "By then irreversible field loss has occurred."],
     ["Screening only after age 70", "Adults over 40 are already at risk."]],
   c=0, cite=c(18)),

 dict(topic="Open-angle glaucoma", io=IOB, lead="education",
   q="A 70-year-old woman with chronic open-angle glaucoma asks whether she will need surgery. What does the lecture say?",
   opts=[
     ["Some patients stay on drops for life", "Correct, when the surgical risk outweighs the benefit."],
     ["Every patient needs surgery within a year", "Many remain on medication indefinitely."],
     ["Surgery is never used in this form", "Laser and incisional surgery are both used."],
     ["Drops are stopped once pressure normalises", "Treatment continues to hold the pressure down."],
     ["Surgery restores lost vision", "Field loss already sustained does not return."]],
   c=0, cite=c(21)),

 dict(topic="Optic neuritis", io=IOB, lead="education",
   q="A 26-year-old woman with optic neuritis asks why she needs a brain MRI when her sight is improving. What is the reason?",
   opts=[
     ["To find an underlying cause such as multiple sclerosis", "Correct; treating the episode alone can miss a larger problem."],
     ["To measure the intraocular pressure in both eyes", "That is tonometry."],
     ["To confirm the retina is attached", "That is ultrasound."],
     ["To exclude a carotid embolus", "That is Doppler ultrasound."],
     ["To grade the optic nerve cupping", "That is a glaucoma assessment."]],
   c=0, cite=c(24)),

 dict(topic="AAION", io=IOB, lead="education",
   q="A 79-year-old woman on long-term corticosteroids for arteritic optic neuropathy asks about the extra tablet she was given. What is famotidine for?",
   opts=[
     ["Gastrointestinal ulcer prophylaxis", "Correct, given alongside the steroid course."],
     ["Lowering intraocular pressure", "That is acetazolamide."],
     ["Preventing further emboli", "That is antiplatelet therapy."],
     ["Reducing optic nerve inflammation", "That is the steroid itself."],
     ["Controlling blood pressure", "It is not an antihypertensive."]],
   c=0, cite=c(51)),

 dict(topic="Acute vision loss", io=IOB, lead="education",
   q="A 61-year-old man is counselled after an episode of transient monocular vision loss. Which point does the lecture make central?",
   opts=[
     ["A transient ischemic attack warns of a stroke", "Correct; it is a major warning sign."],
     ["A transient episode carries no further risk", "It is precisely a warning of higher risk."],
     ["Only bilateral loss is concerning", "Monocular loss is the presentation described."],
     ["Recovery means no workup is needed", "The workup is what finds the source."],
     ["The risk applies only over age 80", "Risk is present well below that age."]],
   c=0, cite=c(4)),

 # ---------------- Prognosis ----------------
 dict(topic="Amaurosis fugax", io=IOA, lead="prognosis",
   q="A 66-year-old man with amaurosis fugax does not recover fully. Which condition does the lecture say the remainder progress to?",
   opts=[
     ["Central retinal artery occlusion", "Correct, a full blockage rather than a transient one."],
     ["Central retinal vein occlusion", "A thrombotic event, not the endpoint of an embolic one."],
     ["Retinal detachment", "That follows a retinal tear, not an embolic episode."],
     ["Papilledema", "That follows raised intracranial pressure."],
     ["Chronic open-angle glaucoma", "That develops slowly over years, unrelated to emboli."]],
   c=0, cite=c(8)),

 dict(topic="Optic neuritis", io=IOA, lead="prognosis",
   q="A 29-year-old man with optic neuritis asks how long recovery takes. What does the lecture describe?",
   opts=[
     ["Improvement within weeks, normal vision within a year", "Correct, often without treatment."],
     ["Improvement only after a long course of steroids", "Recovery is usually spontaneous."],
     ["No recovery at any point", "Recovery is the rule."],
     ["Recovery within hours", "Faster than the described course."],
     ["Gradual decline over years", "That is chronic glaucoma."]],
   c=0, cite=c(24)),

 dict(topic="CRAO", io=IOA, lead="prognosis",
   q="A 71-year-old woman with a central retinal artery occlusion asks about her wider risk. What does the lecture state?",
   opts=[
     ["Stroke risk rises at the onset of the occlusion", "Correct; plaque reaching the retina implies more upstream."],
     ["Stroke risk is unaffected", "It rises."],
     ["Risk is limited to the affected eye", "The systemic risk is emphasised."],
     ["Risk falls once vision is lost", "It does not."],
     ["Risk depends only on the intraocular pressure", "Pressure is not the driver."]],
   c=0, cite=c(37)),

 dict(topic="AAION", io=IOA, lead="prognosis",
   q="A 80-year-old woman is treated for arteritic optic neuropathy. What does the lecture say the outlook depends on?",
   opts=[
     ["Duration of symptoms and when steroids began", "Correct, which is why early therapy is critical."],
     ["The intraocular pressure at presentation", "Not the determinant here."],
     ["Whether surgery was performed", "Surgery is not the treatment."],
     ["The number of demyelinating lesions", "That belongs to optic neuritis."],
     ["The type of detachment", "That belongs to retinal detachment."]],
   c=0, cite=c(51)),

 dict(topic="NAION", io=IOB, lead="prognosis",
   q="A 56-year-old man with non-arteritic anterior ischemic optic neuropathy has completed his workup. What does the lecture give as management?",
   opts=[
     ["Observation and cardiovascular risk modification", "Correct, once everything else has been excluded."],
     ["A long-term high-dose oral corticosteroid course", "Those treat the arteritic form."],
     ["Urgent surgical decompression", "Not a treatment described."],
     ["Lifelong pressure-lowering drops", "Those treat glaucoma."],
     ["Antiplatelet therapy alone", "Not the management described."]],
   c=0, cite=c(52)),

 dict(topic="AAION", io=IOB, lead="reasoning",
   q="A 77-year-old man is being treated for arteritic optic neuropathy. Why does the lecture describe it as a medical emergency?",
   opts=[
     ["Untreated, it leads to blindness", "Correct, and the second eye is at risk."],
     ["It causes a stroke within hours", "Blindness, not stroke, is the stated risk."],
     ["It raises intraocular pressure acutely", "That is angle-closure glaucoma."],
     ["It detaches the retina", "That is a separate condition."],
     ["It raises intracranial pressure", "That is papilledema."]],
   c=0, cite=c(49)),

 # ---------------- Differential diagnosis facet ----------------
 dict(topic="Differential diagnosis", io=IOA, lead="comparison",
   q="A 60-year-old man is being taught how to separate papilledema from glaucoma at the optic disc. What is the key difference?",
   opts=[
     ["Papilledema pushes the disc out; glaucoma cups it in", "Correct, and the lecturer stressed how distinct they look."],
     ["Both cup the disc equally", "They move in opposite directions."],
     ["Both elevate the disc equally", "They move in opposite directions."],
     ["Neither changes the disc", "Both change it markedly."],
     ["Only glaucoma affects the appearance of the disc", "Papilledema is defined by disc swelling."]],
   c=0, cite=c(43)),

 dict(topic="Differential diagnosis", io=IOA, lead="comparison",
   q="A 64-year-old woman is being taught which pressure is raised in each condition. Which pairing is correct?",
   opts=[
     ["Glaucoma raises intraocular pressure", "Correct; papilledema follows raised intracranial pressure."],
     ["Papilledema raises intraocular pressure", "Its pressure is intracranial."],
     ["Optic neuritis raises intraocular pressure", "It is inflammatory, not pressure driven."],
     ["Retinal detachment raises intracranial pressure", "It is mechanical separation."],
     ["Arterial occlusion raises intracranial pressure", "It is embolic."]],
   c=0, cite=c(43)),

 dict(topic="Differential diagnosis", io=IOA, lead="comparison",
   q="A 65-year-old man asks how the branch and central forms of a retinal occlusion differ. What does the lecture say?",
   opts=[
     ["The branch form affects only part of the retina", "Correct; everything else about it is the same."],
     ["The branch form affects both eyes", "Both forms are monocular."],
     ["The branch form is painful", "Both are painless."],
     ["The branch form needs different treatment", "Management is essentially the same."],
     ["The branch form is not sight-threatening", "It still causes field loss and needs referral."]],
   c=0, cite=c(35)),

 dict(topic="Differential diagnosis", io=IOA, lead="comparison",
   q="A 55-year-old woman is learning the two glaucomas. Which pairing does the lecture give?",
   opts=[
     ["Acute is closed-angle; chronic is open-angle", "Correct."],
     ["Acute is open-angle; chronic is closed-angle", "This reverses them."],
     ["Both are closed-angle", "They are distinguished by the angle."],
     ["Both are open-angle", "They are distinguished by the angle."],
     ["Neither involves the drainage angle", "The angle defines the classification."]],
   c=0, cite=c(9)),

 dict(topic="Differential diagnosis", io=IOA, lead="comparison",
   q="A 73-year-old man asks what separates the two forms of anterior ischemic optic neuropathy. What does the lecture give?",
   opts=[
     ["Whether giant cell arteritis is present", "Correct; the arteritic form is caused by it."],
     ["Which eye is affected", "Either eye may be affected in both."],
     ["Whether vision loss is painful", "Both are painless."],
     ["Whether the retina is detached", "Neither involves detachment."],
     ["Whether intraocular pressure is raised", "Pressure does not separate them."]],
   c=0, cite=c(47)),

 dict(topic="Differential diagnosis", io=IOA, lead="reasoning",
   q="A 62-year-old man says a curtain came down over his vision. Why does the lecture warn about this description?",
   opts=[
     ["More than one condition uses it", "Correct; it fits amaurosis fugax and retinal detachment."],
     ["It is never a real symptom", "It is a genuine and useful description."],
     ["It always means glaucoma", "Glaucoma is not described this way."],
     ["It always means detachment", "Amaurosis fugax uses the same word."],
     ["It indicates raised intracranial pressure", "That gives non-specific change instead."]],
   c=0, cite=c(6)),

 dict(topic="Amaurosis fugax", io=IOA, lead="manifestation",
   q="A 70-year-old woman with ocular ischemia loses part of her visual field. Which patterns does the lecture describe?",
   opts=[
     ["Upper or lower half, temporal or nasal, or central", "Correct; the whole field may also be lost."],
     ["Only the central field", "The lecture describes several patterns."],
     ["Only the temporal field", "The lecture describes several patterns."],
     ["Only the peripheral field", "The lecture describes several patterns."],
     ["The visual field is never partially affected", "Partial loss is explicitly described."]],
   c=0, cite=c(6)),

 dict(topic="Amaurosis fugax", io=IOA, lead="reasoning",
   q="A 68-year-old man describes vision descending over one eye like a shade from above. What does the lecture attribute this to?",
   opts=[
     ["Retinal ischemia", "Correct, when the loss descends over the field of one eye."],
     ["Raised intracranial pressure", "That gives non-specific bilateral change."],
     ["Optic nerve demyelination", "That gives central loss and colour desaturation."],
     ["Trabecular meshwork disease", "That gives slow peripheral loss."],
     ["Vitreous traction", "That gives flashes and floaters."]],
   c=0, cite=c(6)),

 dict(topic="Papilledema", io=IOA, lead="finding",
   q="A 41-year-old woman has acute papilledema. Which findings distinguish it from the chronic phase?",
   opts=[
     ["Haemorrhages and cotton wool spots", "Correct; the chronic phase lacks both."],
     ["Disc elevation alone", "That is the chronic phase."],
     ["Loss of the optic nerve axons", "That is the atrophic phase."],
     ["A cherry-red spot", "That is arterial occlusion."],
     ["Optic nerve cupping", "That is chronic glaucoma."]],
   c=0, cite=c(45)),

 dict(topic="Angle-closure glaucoma", io=IOB, lead="treatment",
   q="A 59-year-old man has acute angle closure. How soon after onset does the lecture perform the definitive procedure?",
   opts=[
     ["One to two days", "Correct, after medical measures have lowered the pressure."],
     ["Within the hour", "Medical therapy comes first."],
     ["After two weeks", "Longer than the interval given."],
     ["Only if drops fail after a month", "Far beyond the interval given."],
     ["At the next routine appointment", "The procedure is scheduled promptly."]],
   c=0, cite=c(20)),

 dict(topic="Optic neuritis", io=IOB, lead="treatment",
   q="A 33-year-old woman with optic neuritis is found to have multiple sclerosis. Which treatment does the lecture mention?",
   opts=[
     ["Corticosteroids", "Correct, considered when a demyelinating cause is identified."],
     ["Carbonic anhydrase inhibitors", "Those lower intraocular pressure."],
     ["Antiplatelet therapy", "That reduces embolic risk."],
     ["Laser photocoagulation", "That treats retinal tears."],
     ["Calcium channel blockers", "Those treat vascular spasm."]],
   c=0, cite=c(24)),

 dict(topic="Retinal detachment", io=IOB, lead="treatment",
   q="A 66-year-old man needs retinal detachment repair. Which of these does the lecture list among the surgical options?",
   opts=[
     ["Pneumatic retinopexy", "Correct, with cryotherapy, vitrectomy, laser photocoagulation and scleral buckle."],
     ["Laser trabeculoplasty", "That treats open-angle glaucoma."],
     ["Peripheral iridotomy", "That treats angle-closure glaucoma."],
     ["Carotid endarterectomy", "That removes carotid plaque."],
     ["Anterior chamber paracentesis", "That is used in arterial occlusion."]],
   c=0, cite=c(30)),
]
