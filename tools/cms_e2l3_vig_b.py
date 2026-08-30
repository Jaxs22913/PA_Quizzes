# CMS I Exam 2, Lecture 12 Acute Vision Loss — VIGNETTE pool, part B.
# Retinal vascular occlusions, papilledema and anterior ischemic optic
# neuropathy, plus the cross-cutting discriminators Jaquith told the class to
# highlight: one eye or both, sudden or gradual, central or peripheral field,
# painful or painless.
SRC = "12. Acute Vision Loss current - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = ("a — Compare and contrast the etiologies, epidemiology, risk factors, clinical "
       "manifestations, differential diagnosis, diagnostic testing, management, patient "
       "education, and prognosis of the acute vision loss disorders")
IOB = ("b — Identify medical care strategies for acute vision loss in adult and elderly "
       "populations")

POOL_B = [

 # ---------------- Central retinal vein occlusion ----------------
 dict(topic="CRVO", io=IOA, lead="diagnosis",
   q="A 63-year-old man with hypertension and diabetes has sudden painless loss of vision in one eye. Fundoscopy shows a swollen disc, dilated veins, cotton wool spots and haemorrhages across all four quadrants. Which is the most likely diagnosis?",
   opts=[
     ["Central retinal vein occlusion", "Correct. The blood and thunder fundus with disc swelling."],
     ["Central retinal artery occlusion", "That gives a pale retina with a cherry-red spot."],
     ["Retinal detachment", "That shows an elevated grey retina with folds."],
     ["Papilledema", "That is bilateral and follows raised intracranial pressure."],
     ["Optic neuritis", "That is painful on eye movement, usually with a normal disc."]],
   c=0, cite=c(34)),

 dict(topic="CRVO", io=IOA, lead="finding",
   q="A 67-year-old woman has a retinal vein occlusion. Which term did the lecturer give as the classic fundus description?",
   opts=[
     ["Blood and thunder", "Correct, blotches of haemorrhage across the fundus."],
     ["Cherry-red spot", "That belongs to arterial occlusion."],
     ["Billowy folds", "That belongs to retinal detachment."],
     ["Disc at risk", "That describes the small crowded disc of non-arteritic optic neuropathy."],
     ["Optic nerve cupping", "That belongs to chronic glaucoma."]],
   c=0, cite=c(34)),

 dict(topic="CRVO", io=IOA, lead="pathophysiology",
   q="A 70-year-old man with a hypercoagulable disorder develops a central retinal vein occlusion. What has occurred?",
   opts=[
     ["A thrombus has occluded the vein", "Correct, preventing the retina from draining."],
     ["An embolus has lodged in the artery", "That is arterial occlusion."],
     ["The iris has closed the drainage angle", "That is angle-closure glaucoma."],
     ["The retina has separated from its bed", "That is detachment."],
     ["Intracranial pressure has risen", "That is papilledema."]],
   c=0, cite=c(32)),

 dict(topic="CRVO", io=IOA, lead="comparison",
   q="A 61-year-old woman asks which retinal vascular occlusion is seen more often. What does the lecture state?",
   opts=[
     ["Vein occlusion is more common", "Correct, more common than central retinal artery occlusion."],
     ["Artery occlusion is more common", "The lecture states the opposite."],
     ["They occur equally often", "One is stated to be more common."],
     ["Neither occurs after age 50", "Age over 50 is a listed risk factor."],
     ["Only artery occlusion occurs in diabetes", "Diabetes is a risk factor for both."]],
   c=0, cite=c(32)),

 dict(topic="CRVO", io=IOB, lead="test",
   q="A 65-year-old man has a suspected central retinal vein occlusion. Which does the lecture name as confirmatory testing?",
   opts=[
     ["Fluorescein angiography", "Correct, with colour fundus photography."],
     ["Ocular ultrasound", "That is used for retinal detachment."],
     ["Gonioscopy", "That assesses the drainage angle."],
     ["Lumbar puncture", "That assesses intracranial pressure."],
     ["Temporal artery biopsy", "That investigates giant cell arteritis."]],
   c=0, cite=c(34)),

 dict(topic="CRVO", io=IOA, lead="prognosis",
   q="A 68-year-old woman had a central retinal vein occlusion two months ago and returns with new abnormal vessels on the retina. What is this?",
   opts=[
     ["Neovascularization after the occlusion", "Correct, appearing weeks to months later."],
     ["A second thrombus", "New vessel growth is the described sequel."],
     ["Optic nerve cupping", "That is a glaucomatous change."],
     ["A retinal tear", "That presents with flashes and floaters."],
     ["Disc oedema from raised pressure", "That is papilledema."]],
   c=0, cite=c(34)),

 dict(topic="BRVO", io=IOA, lead="reasoning",
   q="A 62-year-old man has painless loss of only the lower half of the vision in one eye, with haemorrhages confined to the upper retina. How does this differ from a central retinal vein occlusion?",
   opts=[
     ["A smaller branch vein is blocked", "Correct, so only part of the retina is affected."],
     ["The artery rather than the vein is blocked", "The findings described are venous."],
     ["Both eyes are involved", "This is a monocular process."],
     ["Intracranial pressure is raised", "That is papilledema."],
     ["The macula is detached", "Detachment gives an elevated grey retina."]],
   c=0, cite=c(35)),

 dict(topic="BRVO", io=IOB, lead="next step",
   q="A 64-year-old woman has a branch retinal vein occlusion. How does her management compare with the central form?",
   opts=[
     ["It is essentially the same", "Correct; the lecture said the only difference is where the clot sits."],
     ["It needs no referral", "Urgent ophthalmology referral still applies."],
     ["It requires laser iridotomy", "That is for angle-closure glaucoma."],
     ["It requires high-dose steroids", "Those are for arteritic optic neuropathy."],
     ["It requires surgical reattachment", "That is for detachment."]],
   c=0, cite=c(35)),

 # ---------------- Central retinal artery occlusion ----------------
 dict(topic="CRAO", io=IOA, lead="diagnosis",
   q="A 72-year-old man with atrial fibrillation has profound painless loss of vision in the right eye that came on over a few seconds. He can only count fingers. The retina is pale and swollen with a cherry-red spot at the fovea. Which is the most likely diagnosis?",
   opts=[
     ["Central retinal artery occlusion", "Correct. Sudden profound loss with the cherry-red fovea."],
     ["Central retinal vein occlusion", "That shows haemorrhages and a swollen disc."],
     ["Amaurosis fugax", "That resolves within minutes."],
     ["Retinal detachment", "That advances over days with flashes and floaters."],
     ["Optic neuritis", "That builds over hours to days and is painful."]],
   c=0, cite=c(39)),

 dict(topic="CRAO", io=IOB, lead="reasoning",
   q="A 74-year-old woman presents 40 minutes after sudden painless monocular vision loss. Why is she treated immediately?",
   opts=[
     ["Retinal damage is irreversible after 90 minutes", "Correct; this is the window the lecture gives."],
     ["Retinal damage is irreversible after 8 hours", "Eight hours is the thrombolysis window, not the damage threshold."],
     ["Retinal damage is irreversible after 24 hours", "Far beyond the stated window."],
     ["Damage is reversible at any point", "It is not."],
     ["Damage occurs only if both eyes are affected", "One eye is enough."]],
   c=0, cite=c(37)),

 dict(topic="CRAO", io=IOA, lead="finding",
   q="A 69-year-old man has a central retinal artery occlusion. His affected pupil is sluggish to direct light but constricts briskly when the other eye is illuminated. What did the lecturer say about this finding?",
   opts=[
     ["It is a major clinical clue", "Correct; she singled out this sentence in the lecture."],
     ["It excludes an arterial cause", "It is characteristic of one."],
     ["It indicates raised intracranial pressure", "That gives disc swelling, not this pupil pattern."],
     ["It indicates a detached retina", "Detachment does not produce this pupil response."],
     ["It is a normal finding", "It reflects an afferent defect."]],
   c=0, cite=c(38)),

 dict(topic="CRAO", io=IOA, lead="symptom",
   q="A 71-year-old man with a central retinal artery occlusion describes what remains of his sight. Which pattern does the lecture give?",
   opts=[
     ["An island of vision in the temporal field", "Correct, with acuity from counting fingers to light perception."],
     ["A central island with peripheral loss", "That is the tunnel vision of chronic glaucoma."],
     ["A curtain lifting after seconds", "That is amaurosis fugax."],
     ["Flickering and double vision", "Those are papilledema symptoms."],
     ["Loss of colour vision only", "That is optic neuritis."]],
   c=0, cite=c(38)),

 dict(topic="CRAO", io=IOB, lead="treatment",
   q="A 70-year-old woman arrives with a central retinal artery occlusion. Which initial measures does the lecture give?",
   opts=[
     ["Inhaled oxygen and digital globe massage", "Correct, alongside intravenous acetazolamide."],
     ["Topical latanoprost", "That is chronic glaucoma therapy."],
     ["Intravenous methylprednisolone", "That is for arteritic optic neuropathy."],
     ["Immediate vitrectomy", "That repairs a detachment."],
     ["Observation and repeat exam", "Delay costs the retina."]],
   c=0, cite=c(40)),

 dict(topic="CRAO", io=IOB, lead="treatment",
   q="A 66-year-old man presents six hours after a central retinal artery occlusion. Which option remains available per the lecture?",
   opts=[
     ["Thrombolytic infusion into the ophthalmic artery", "Correct, within eight hours of onset."],
     ["Laser peripheral iridotomy", "That treats angle-closure glaucoma."],
     ["Scleral buckle", "That repairs a detachment."],
     ["Oral prednisone taper", "That treats arteritic optic neuropathy."],
     ["Carotid endarterectomy that evening", "Surgery addresses the source later, not the acute occlusion."]],
   c=0, cite=c(40)),

 dict(topic="CRAO", io=IOB, lead="next step",
   q="A 68-year-old man with a central retinal artery occlusion asks about his general health risk. What does the lecture emphasise?",
   opts=[
     ["His stroke risk is markedly increased", "Correct; plaque reaching the retinal artery implies more in the carotids."],
     ["His stroke risk is unchanged", "It rises at the onset of the occlusion."],
     ["His risk is confined to the other eye", "The systemic risk is the concern."],
     ["His risk falls once vision is lost", "It does not."],
     ["His risk depends on intraocular pressure", "Pressure is not the driver here."]],
   c=0, cite=c(37)),

 dict(topic="BRAO", io=IOA, lead="reasoning",
   q="A 65-year-old woman has sudden painless loss of a wedge of vision in one eye, with pallor limited to one arterial territory. Which diagnosis fits?",
   opts=[
     ["Branch retinal artery occlusion", "Correct; a branch is blocked rather than the main trunk."],
     ["Central retinal artery occlusion", "That causes widespread, severe loss."],
     ["Branch retinal vein occlusion", "That would show haemorrhage, not pallor."],
     ["Retinal detachment", "That gives an elevated grey retina."],
     ["Amaurosis fugax", "That resolves completely."]],
   c=0, cite=c(41)),

 # ---------------- Papilledema ----------------
 dict(topic="Papilledema", io=IOA, lead="diagnosis",
   q="A 34-year-old woman has weeks of headache, nausea and vomiting with flickering and intermittent blurred vision. Both optic discs are swollen with blurred margins and engorged veins. Which is the most likely diagnosis?",
   opts=[
     ["Papilledema", "Correct. Bilateral disc swelling with signs of raised intracranial pressure."],
     ["Chronic open-angle glaucoma", "That cups the disc rather than elevating it."],
     ["Optic neuritis", "That is unilateral and painful on eye movement."],
     ["Central retinal vein occlusion", "That is monocular with haemorrhages."],
     ["Anterior ischemic optic neuropathy", "That causes sudden monocular loss with a pale disc."]],
   c=0, cite=c(44)),

 dict(topic="Papilledema", io=IOA, lead="pathophysiology",
   q="A 41-year-old man is told he has papilledema. Which pressure is raised?",
   opts=[
     ["Intracranial pressure", "Correct; the lecturer drew a sharp line against intraocular pressure."],
     ["Intraocular pressure", "That is the glaucoma mechanism."],
     ["Central venous pressure", "Not the mechanism described."],
     ["Arterial blood pressure", "Hypertension is a risk factor elsewhere, not this mechanism."],
     ["Orbital compartment pressure", "Not the mechanism described."]],
   c=0, cite=c(43)),

 dict(topic="Papilledema", io=IOA, lead="cause",
   q="A 38-year-old woman with papilledema is taking large doses of a supplement. Which does the lecture list as a cause?",
   opts=[
     ["Vitamin A toxicity", "Correct, listed with tumour, trauma, intracranial infection and haemorrhage."],
     ["Vitamin C excess", "Not a listed cause."],
     ["Iron deficiency", "Not a listed cause."],
     ["Calcium supplementation", "Not a listed cause."],
     ["Vitamin D toxicity", "Not the vitamin named."]],
   c=0, cite=c(43)),

 dict(topic="Papilledema", io=IOB, lead="test",
   q="A 36-year-old man has bilateral disc swelling. Which test does the lecture use to confirm that intracranial pressure is raised?",
   opts=[
     ["Lumbar puncture opening pressure", "Correct, after imaging has excluded a mass lesion."],
     ["Tonometry", "That measures intraocular pressure."],
     ["Fluorescein angiography", "That assesses retinal perfusion."],
     ["Erythrocyte sedimentation rate", "That screens for arteritis."],
     ["Carotid Doppler", "That looks for an embolic source."]],
   c=0, cite=c(46)),

 dict(topic="Papilledema", io=IOB, lead="next step",
   q="A 45-year-old woman has papilledema. Which imaging does the lecture obtain, and why?",
   opts=[
     ["MRI or CT of the head, to exclude a mass", "Correct."],
     ["Orbital ultrasound, to type a detachment", "That is the detachment workup."],
     ["MRI of the orbits, to find demyelination", "That is the optic neuritis workup."],
     ["Carotid Doppler, to find plaque", "That is the embolic workup."],
     ["No imaging is required", "A mass lesion must be excluded."]],
   c=0, cite=c(46)),

 dict(topic="Papilledema", io=IOA, lead="finding",
   q="A 39-year-old man has papilledema and later develops disc elevation with blurred margins but no haemorrhages or cotton wool spots. Which phase does this describe?",
   opts=[
     ["Chronic papilledema", "Correct; haemorrhages and cotton wool spots mark the acute phase."],
     ["Acute papilledema", "That phase carries haemorrhages and cotton wool spots."],
     ["The atrophic phase", "There the optic nerve axons have died."],
     ["Resolved papilledema", "The disc would no longer be elevated."],
     ["Optic nerve cupping", "That is a glaucomatous change."]],
   c=0, cite=c(45)),

 # ---------------- Anterior ischemic optic neuropathy ----------------
 dict(topic="AAION", io=IOA, lead="diagnosis",
   q="A 72-year-old woman has sudden painless loss of vision in one eye. For three weeks she has had a new temporal headache, a tender scalp when combing her hair, jaw pain on chewing, malaise and weight loss. Which is the most likely diagnosis?",
   opts=[
     ["Arteritic anterior ischemic optic neuropathy", "Correct. The systemic arteritic features make this the emergency."],
     ["Non-arteritic anterior ischemic optic neuropathy", "That lacks systemic symptoms and occurs in a younger group."],
     ["Optic neuritis", "That affects younger patients and hurts on eye movement."],
     ["Central retinal artery occlusion", "That gives a cherry-red spot without systemic symptoms."],
     ["Papilledema", "That is bilateral with raised intracranial pressure."]],
   c=0, cite=c(49)),

 dict(topic="AAION", io=IOB, lead="test",
   q="A 76-year-old woman has sudden vision loss, scalp tenderness and jaw claudication. Which initial tests does the lecture order?",
   opts=[
     ["Erythrocyte sedimentation rate and C-reactive protein", "Correct, the inflammatory markers used to rule the diagnosis in or out."],
     ["Tonometry and gonioscopy", "Those assess glaucoma."],
     ["Lumbar puncture", "That assesses intracranial pressure."],
     ["Carotid Doppler and echocardiogram", "Those look for an embolic source."],
     ["MRI of brain and orbits", "That is the optic neuritis study."]],
   c=0, cite=c(51)),

 dict(topic="AAION", io=IOB, lead="treatment",
   q="A 78-year-old woman has arteritic anterior ischemic optic neuropathy. Her inflammatory markers are markedly raised. What is done first?",
   opts=[
     ["Intravenous methylprednisolone", "Correct, three days, then a slow oral taper; early therapy is critical."],
     ["Await the temporal artery biopsy result", "Treatment starts before the biopsy to save vision."],
     ["Topical timolol", "That lowers intraocular pressure."],
     ["Aspirin and clopidogrel", "Those reduce embolic stroke risk."],
     ["Observation with weekly markers", "Delay risks blindness."]],
   c=0, cite=c(51)),

 dict(topic="AAION", io=IOB, lead="treatment",
   q="A 74-year-old man is starting a long corticosteroid course for arteritic optic neuropathy. Which additional drug does the lecture add?",
   opts=[
     ["Famotidine", "Correct, for gastrointestinal ulcer prophylaxis."],
     ["Acetazolamide", "That lowers intraocular pressure."],
     ["Latanoprost", "That is glaucoma therapy."],
     ["Warfarin", "Anticoagulation is not part of this regimen."],
     ["Pilocarpine", "That is a topical agent for angle closure."]],
   c=0, cite=c(51)),

 dict(topic="AAION", io=IOA, lead="test",
   q="A 77-year-old woman is treated for arteritic optic neuropathy. Which test does the lecture call the gold standard for the underlying arteritis?",
   opts=[
     ["Temporal artery biopsy", "Correct."],
     ["C-reactive protein", "A screening marker, not the gold standard."],
     ["Erythrocyte sedimentation rate", "A screening marker, not the gold standard."],
     ["MRI of the orbits", "Not the confirmatory test here."],
     ["Fluorescein angiography", "That assesses retinal perfusion."]],
   c=0, cite=c(51)),

 dict(topic="AAION", io=IOB, lead="education",
   q="A 75-year-old woman with arteritic optic neuropathy asks how long she will take steroids. What does the lecture say?",
   opts=[
     ["At least 6 to 12 months", "Correct, tapered to the lowest dose that suppresses the disease."],
     ["Three days only", "Three days is the intravenous phase alone."],
     ["Two weeks", "Shorter than the course described."],
     ["Lifelong without taper", "The dose is tapered."],
     ["Until the biopsy is performed", "Duration is guided by symptoms and labs."]],
   c=0, cite=c(51)),

 dict(topic="NAION", io=IOA, lead="diagnosis",
   q="A 52-year-old man with hypertension, diabetes and obstructive sleep apnea has sudden painless loss of the lower half of vision in one eye. He has no headache, scalp tenderness or jaw pain. His discs are described as small and crowded. Which is the most likely diagnosis?",
   opts=[
     ["Non-arteritic anterior ischemic optic neuropathy", "Correct. The disc at risk with vascular comorbidity and no arteritic features."],
     ["Arteritic anterior ischemic optic neuropathy", "That carries systemic symptoms in an older patient."],
     ["Optic neuritis", "That hurts on eye movement and builds over days."],
     ["Central retinal vein occlusion", "That shows widespread haemorrhage."],
     ["Retinal detachment", "That follows flashes and floaters."]],
   c=0, cite=c(48)),

 dict(topic="NAION", io=IOA, lead="epidemiology",
   q="A 55-year-old man is diagnosed with non-arteritic anterior ischemic optic neuropathy. What share of anterior ischemic optic neuropathy does this form represent?",
   opts=[
     ["90 to 95 percent", "Correct, and it presents at 40 to 60 years of age."],
     ["50 to 60 percent", "Lower than the figure given."],
     ["25 to 30 percent", "Lower than the figure given."],
     ["5 to 10 percent", "That is the arteritic share."],
     ["Under 5 percent", "Far below the figure given."]],
   c=0, cite=c(48)),

 dict(topic="NAION", io=IOB, lead="next step",
   q="A 54-year-old man has suspected non-arteritic anterior ischemic optic neuropathy. How does the lecture describe the workup?",
   opts=[
     ["Identical to the arteritic form", "Correct; it is a diagnosis of exclusion once arteritis is ruled out."],
     ["No workup is needed", "Arteritis must first be excluded."],
     ["Temporal artery biopsy only", "Biopsy is part of excluding the arteritic form, not the whole workup."],
     ["Lumbar puncture first", "That belongs to the papilledema workup."],
     ["Tonometry and gonioscopy", "Those assess glaucoma."]],
   c=0, cite=c(52)),

 dict(topic="NAION", io=IOB, lead="education",
   q="A 57-year-old man with non-arteritic anterior ischemic optic neuropathy takes an antihypertensive at bedtime. Which change may be considered?",
   opts=[
     ["Moving the dose away from bedtime", "Correct, to avoid nocturnal hypotension, which can worsen the condition."],
     ["Doubling the bedtime dose", "That would deepen the overnight fall in pressure."],
     ["Stopping all antihypertensives", "The lecture adjusts timing rather than abandoning treatment."],
     ["Adding a corticosteroid", "Steroids treat the arteritic form."],
     ["Adding a topical beta-blocker", "That treats glaucoma."]],
   c=0, cite=c(52)),

 dict(topic="AION", io=IOA, lead="finding",
   q="A 68-year-old woman has sudden painless vision loss. Which optic disc appearance does the lecture describe in anterior ischemic optic neuropathy?",
   opts=[
     ["A swollen, pale disc", "Correct, with loss of side or central vision."],
     ["A deeply cupped disc", "That is chronic glaucoma."],
     ["A normal-appearing disc", "That is often optic neuritis."],
     ["A cherry-red macula", "That is arterial occlusion."],
     ["Haemorrhages in all quadrants", "That is vein occlusion."]],
   c=0, cite=c(50)),

 dict(topic="AION", io=IOA, lead="prognosis",
   q="A 71-year-old man has anterior ischemic optic neuropathy in one eye and asks about the other. What does the lecture say?",
   opts=[
     ["The second eye is at risk", "Correct; one eye is usually affected first but the other may follow."],
     ["The second eye is never involved", "It can be."],
     ["Both eyes are always affected at once", "Usually one eye is affected first."],
     ["The second eye is protected by treatment", "Risk to the second eye is why treatment matters."],
     ["Involvement of the second eye is painful", "The condition is painless."]],
   c=0, cite=c(50)),

 dict(topic="AAION", io=IOB, lead="next step",
   q="A 79-year-old man has sudden vision loss in one eye. Which referral threshold does the lecture apply?",
   opts=[
     ["Emergent referral for anyone over 50", "Correct, any patient over 50 with sudden visual loss."],
     ["Routine referral within a month", "That delay risks the eye."],
     ["Referral only with a headache", "Age and sudden loss are enough."],
     ["Referral only if markers are raised", "Referral precedes the results."],
     ["Referral only if both eyes are involved", "One eye is enough."]],
   c=0, cite=c(51)),

 # ---------------- Cross-cutting discriminators ----------------
 dict(topic="Differential diagnosis", io=IOA, lead="reasoning",
   q="A 66-year-old woman has acute vision loss. Which features did the lecturer tell the class to pin down in order to separate these diagnoses?",
   opts=[
     ["One eye or both, sudden or gradual, central or peripheral", "Correct, along with whether there is pain."],
     ["Height, weight and body mass index", "Not the discriminating features named."],
     ["Family history and occupation", "Useful background, but not the named discriminators."],
     ["Blood type and allergies", "Not relevant to separating these."],
     ["Smoking history alone", "A risk factor, but not the discriminator taught."]],
   c=0, cite=c(4)),

 dict(topic="Differential diagnosis", io=IOA, lead="reasoning",
   q="A 70-year-old man has painful acute vision loss. Which diagnosis does the pain point toward?",
   opts=[
     ["Acute angle-closure glaucoma", "Correct; the occlusions and detachment are painless."],
     ["Central retinal artery occlusion", "Painless, with profound loss over seconds."],
     ["Central retinal vein occlusion", "Painless, with a haemorrhagic fundus."],
     ["Retinal detachment", "Painless, preceded by flashes and floaters."],
     ["Amaurosis fugax", "Painless, and it clears within minutes."]],
   c=0, cite=c(33)),

 dict(topic="Differential diagnosis", io=IOA, lead="reasoning",
   q="A 60-year-old woman has bilateral optic disc swelling. Which diagnosis does bilateral involvement most suggest?",
   opts=[
     ["Papilledema", "Correct; the vascular occlusions and detachment are monocular."],
     ["Central retinal artery occlusion", "That is monocular."],
     ["Retinal detachment", "That is monocular."],
     ["Optic neuritis", "That is usually unilateral."],
     ["Amaurosis fugax", "That is usually monocular."]],
   c=0, cite=c(44)),

 dict(topic="Differential diagnosis", io=IOA, lead="comparison",
   q="A 73-year-old man loses vision in one eye. Which finding separates arterial from venous retinal occlusion on fundoscopy?",
   opts=[
     ["A cherry-red spot rather than haemorrhages", "Correct; the artery gives pallor with a cherry-red fovea."],
     ["Disc cupping rather than swelling", "Cupping belongs to chronic glaucoma."],
     ["An elevated grey retina", "That is detachment."],
     ["Blurred disc margins in both eyes", "That is papilledema."],
     ["A hazy cornea", "That is angle-closure glaucoma."]],
   c=0, cite=c(39)),

 dict(topic="Differential diagnosis", io=IOA, lead="comparison",
   q="A 47-year-old woman and a 74-year-old man both have monocular vision loss with an abnormal optic nerve. Which feature most favours optic neuritis over ischemic optic neuropathy?",
   opts=[
     ["Pain on eye movement", "Correct; the ischemic neuropathies are painless."],
     ["A pale, swollen disc", "That favours the ischemic neuropathy."],
     ["Onset over seconds", "That favours arterial occlusion."],
     ["Scalp tenderness", "That favours the arteritic form."],
     ["A raised sedimentation rate", "That favours the arteritic form."]],
   c=0, cite=c(23)),

 dict(topic="Differential diagnosis", io=IOB, lead="next step",
   q="A 69-year-old man has sudden painless monocular vision loss and no other findings. Which single step does the lecture treat as non-negotiable?",
   opts=[
     ["Urgent ophthalmology involvement", "Correct; each of these diagnoses is sight-threatening and time-dependent."],
     ["A trial of topical antibiotics", "There is no infectious indication here."],
     ["Reassurance and review in a week", "A week is too long for any of these."],
     ["An eye patch and analgesia", "Neither addresses the cause."],
     ["Repeat visual acuity in the morning", "Delay risks permanent loss."]],
   c=0, cite=c(30)),

 # ---- second pass at each diagnosis, presented from a different angle, so a
 # ---- set can carry the reference share of pure-diagnosis items ----
 dict(topic="Retinal detachment", io=IOA, lead="diagnosis",
   q="A 72-year-old woman says a dark cloud has settled over the upper part of her vision in one eye. She notices it shifts when she lies down. There is no pain and no headache. Which is the most likely diagnosis?",
   opts=[
     ["Retinal detachment", "Correct; the detached retina floats, so the defect moves with head position."],
     ["Papilledema", "That is bilateral and does not shift with position."],
     ["Central retinal artery occlusion", "That causes fixed, profound loss."],
     ["Amaurosis fugax", "That clears within minutes."],
     ["Optic neuritis", "That is painful on eye movement."]],
   c=0, cite=c(27)),

 dict(topic="Angle-closure glaucoma", io=IOA, lead="diagnosis",
   q="A 59-year-old woman took an over-the-counter antihistamine and hours later developed a severe unilateral headache, a red eye and vomiting. Her pupil is mid-dilated and her cornea looks cloudy. Which is the most likely diagnosis?",
   opts=[
     ["Acute angle-closure glaucoma", "Correct; anticholinergic drugs precipitate it."],
     ["Migraine with aura", "That does not produce a cloudy cornea or a red eye."],
     ["Optic neuritis", "That causes painful movement, not a red cloudy eye."],
     ["Central retinal vein occlusion", "That is painless."],
     ["Papilledema", "That is bilateral with a normal cornea."]],
   c=0, cite=c(14)),

 dict(topic="CRVO", io=IOA, lead="diagnosis",
   q="A 58-year-old man with obesity and poorly controlled hypertension notices his vision in one eye has blurred progressively over about a week, without pain. The fundus is filled with haemorrhage. Which is the most likely diagnosis?",
   opts=[
     ["Central retinal vein occlusion", "Correct; loss may be gradual over days to weeks in some patients."],
     ["Central retinal artery occlusion", "That comes on over seconds."],
     ["Amaurosis fugax", "That lasts seconds to minutes."],
     ["Angle-closure glaucoma", "That is acutely painful."],
     ["Retinal detachment", "That follows flashes and floaters."]],
   c=0, cite=c(33)),

 dict(topic="Amaurosis fugax", io=IOA, lead="diagnosis",
   q="A 65-year-old woman with sickle cell disease describes brief episodes in which the lower half of the vision in one eye fogs over and then clears within a minute. Which is the most likely diagnosis?",
   opts=[
     ["Amaurosis fugax", "Correct; sickle cell is a listed risk factor and the episodes are transient."],
     ["Branch retinal artery occlusion", "That produces a fixed wedge of loss."],
     ["Retinal detachment", "That defect advances rather than clearing."],
     ["Optic neuritis", "That develops over hours to days."],
     ["Papilledema", "That produces persistent non-specific change."]],
   c=0, cite=c(5)),

 dict(topic="CRAO", io=IOA, lead="diagnosis",
   q="A 76-year-old man with carotid disease describes vision in one eye going dark instantly two hours ago and not returning. He has no pain. The retina is pale. Which is the most likely diagnosis?",
   opts=[
     ["Central retinal artery occlusion", "Correct; profound painless loss over seconds that does not recover."],
     ["Amaurosis fugax", "That would have resolved within minutes."],
     ["Central retinal vein occlusion", "That gives a haemorrhagic fundus, not a pale one."],
     ["Optic neuritis", "That is painful and develops over days."],
     ["Angle-closure glaucoma", "That is painful with a hazy cornea."]],
   c=0, cite=c(38)),

 dict(topic="Optic neuritis", io=IOA, lead="diagnosis",
   q="A 24-year-old woman had numbness in one leg last year that resolved. She now has aching behind one eye that worsens when she looks around, with vision fading over two days. Which is the most likely diagnosis?",
   opts=[
     ["Optic neuritis", "Correct; the prior neurological episode points to a demyelinating cause."],
     ["Anterior ischemic optic neuropathy", "That occurs in an older group and is painless."],
     ["Angle-closure glaucoma", "That is acutely painful at rest with halos."],
     ["Central retinal vein occlusion", "That is painless with widespread haemorrhage."],
     ["Papilledema", "That is bilateral with headache and vomiting."]],
   c=0, cite=c(23)),

 dict(topic="Open-angle glaucoma", io=IOA, lead="diagnosis",
   q="A 69-year-old woman keeps bumping into door frames on her left. She has noticed nothing wrong with her reading vision and has no pain. Both intraocular pressures are 27 mmHg. Which is the most likely diagnosis?",
   opts=[
     ["Chronic open-angle glaucoma", "Correct; peripheral field goes first while central vision is preserved."],
     ["Acute angle-closure glaucoma", "That is painful and sudden."],
     ["Optic neuritis", "That is unilateral, painful and affects central vision."],
     ["Retinal detachment", "That advances quickly with flashes and floaters."],
     ["Papilledema", "That follows raised intracranial pressure with headache."]],
   c=0, cite=c(16)),

 dict(topic="Papilledema", io=IOA, lead="diagnosis",
   q="A 28-year-old woman has had a headache worst on waking for six weeks, with brief greying of vision when she stands. Both discs are elevated with engorged veins. Which is the most likely diagnosis?",
   opts=[
     ["Papilledema", "Correct; bilateral disc swelling with the symptoms of raised intracranial pressure."],
     ["Optic neuritis", "That is unilateral and painful on eye movement."],
     ["Chronic open-angle glaucoma", "That cups the disc and is asymptomatic early."],
     ["Central retinal vein occlusion", "That is monocular with haemorrhage."],
     ["Amaurosis fugax", "That does not swell the discs."]],
   c=0, cite=c(44)),

 dict(topic="AAION", io=IOA, lead="diagnosis",
   q="A 81-year-old woman has lost vision in one eye over the past day. She has felt unwell for a month with low-grade fever and aching, and her scalp hurts when she brushes her hair. Which is the most likely diagnosis?",
   opts=[
     ["Arteritic anterior ischemic optic neuropathy", "Correct; systemic arteritic symptoms in an elderly woman."],
     ["Non-arteritic anterior ischemic optic neuropathy", "That has no systemic symptoms."],
     ["Central retinal artery occlusion", "That is sudden over seconds without systemic illness."],
     ["Optic neuritis", "That affects a much younger group."],
     ["Retinal detachment", "That gives flashes, floaters and a field defect."]],
   c=0, cite=c(49)),

 dict(topic="NAION", io=IOA, lead="diagnosis",
   q="A 49-year-old man with sleep apnea wakes to find the upper half of vision in one eye missing. He has no pain, no headache and no scalp tenderness. Inflammatory markers are normal. Which is the most likely diagnosis?",
   opts=[
     ["Non-arteritic anterior ischemic optic neuropathy", "Correct; painless altitudinal loss with normal markers."],
     ["Arteritic anterior ischemic optic neuropathy", "Markers would be raised and symptoms present."],
     ["Optic neuritis", "That is painful on eye movement."],
     ["Branch retinal vein occlusion", "That shows sectoral haemorrhage."],
     ["Amaurosis fugax", "That resolves within minutes."]],
   c=0, cite=c(48)),
]
