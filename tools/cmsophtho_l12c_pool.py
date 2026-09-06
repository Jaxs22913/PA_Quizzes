# -*- coding: utf-8 -*-
"""Acute Vision Loss (Lecture 12) -- third pool.

Written from the audited chart rows, which are the slide content distilled and
cited, so every fact here traces to a slide number.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "12. Acute Vision Loss"
IO = ("a — Acute vision loss: etiologies, epidemiology, risk factors, clinical manifestations, "
      "differential diagnosis, diagnostic testing, management, referrals, patient education, "
      "prognosis")

QUESTIONS = [

Q("Amaurosis fugax", IO,
  "A 68-year-old man describes an episode of 'fleeting blindness' in one eye that lasted about "
  "four minutes with complete recovery. Which investigation does every such patient receive?",
  [["Magnetic resonance angiography", "Correct — with carotid Doppler if a carotid source is "
                                      "suspected and echocardiography if cardiac."],
   ["Temporal artery biopsy", "Reserved for suspected giant cell arteritis."],
   ["Lumbar puncture", "Part of the papilledema workup."],
   ["Gonioscopy", "Assesses the drainage angle in glaucoma."],
   ["Colour vision testing", "Part of the optic neuritis assessment."]],
  "two-step", D, 8),

Q("Amaurosis fugax", IO,
  "A 71-year-old woman reports visual loss in one eye that lasted several hours before clearing. "
  "How does the duration affect the diagnosis?",
  [["Lasting hours argues against a transient ischaemic attack",
    "Correct — the episodes are typically seconds to minutes."],
   ["Hours confirms a transient ischaemic attack", "Duration of hours argues the other way."],
   ["Duration is irrelevant to the diagnosis", "Duration is central to the distinction."],
   ["Hours indicates central retinal artery occlusion",
    "That does not resolve spontaneously at all."],
   ["Hours indicates optic neuritis", "That develops over hours to days and does not clear "
                                      "spontaneously within one episode."]],
  "two-step", D, 5),

Q("Amaurosis fugax", IO,
  "A 66-year-old man has amaurosis fugax from carotid emboli. Which treatments are named?",
  [["Aspirin and clopidogrel, with carotid endarterectomy",
    "Correct — antiplatelet therapy for stroke risk, and surgery for the carotid source."],
   ["Corticosteroids alone", "Those belong to the arteritic pathway."],
   ["Topical pressure-lowering drops", "The pressure is not the problem."],
   ["Intravitreal injection", "That treats neovascular macular disease."],
   ["Antibiotics", "There is no infection."]],
  "treatment", D, 8),

Q("Amaurosis fugax", IO,
  "A 58-year-old woman has transient monocular visual loss attributed to vasospasm. Which drug "
  "class is named for that cause?",
  [["Calcium channel blockers", "Correct — the treatment is directed at the underlying cause."],
   ["Beta blockers", "Used topically for glaucoma, not for vasospasm here."],
   ["Corticosteroids", "Used for arteritic disease and demyelination."],
   ["Antihistamines", "No allergic mechanism is involved."],
   ["Carbonic anhydrase inhibitors", "Used to lower pressure."]],
  "two-step", D, 8),

Q("Chronic open-angle glaucoma", IO,
  "A 64-year-old man is found to have open-angle glaucoma. Where is the abnormality?",
  [["The trabecular meshwork by the canal of Schlemm",
    "Correct — an age-related outflow abnormality."],
   ["The iris blocking the drainage angle", "That is angle CLOSURE."],
   ["The ciliary body producing excess aqueous",
    "That is not the open-angle mechanism."],
   ["The lens pushing the iris forward", "That mechanism belongs to angle closure."],
   ["The optic nerve head itself", "The nerve is the victim rather than the site of obstruction."]],
  "two-step", D, 16),

Q("Chronic open-angle glaucoma", IO,
  "A 61-year-old woman is being assessed for glaucoma. What can the intraocular pressure be?",
  [["Either normal or elevated", "Correct — pressure may be normal OR "
                                 "raised in this disease."],
   ["Always markedly elevated", "Normal-pressure disease exists."],
   ["Always below normal", "Low pressure is not the pattern."],
   ["Elevated only in the morning", "Diurnal variation is not the stated point."],
   ["Irrelevant, as pressure is never measured", "Tonometry is part of the assessment."]],
  "two-step", D, 18),

Q("Chronic open-angle glaucoma", IO,
  "A 67-year-old man's optic nerve shows an increased cup-to-disc ratio with rim thinning and "
  "splinter haemorrhages. Which condition do these indicate?",
  [["Chronic open-angle glaucoma", "Correct — with rim pitting and bayoneting on the same list."],
   ["Papilledema", "Produces a swollen disc rather than an excavated one."],
   ["Optic neuritis", "The disc is often normal-appearing."],
   ["Non-arteritic ischaemic optic neuropathy", "The disc is swollen and pale."],
   ["Central retinal vein occlusion", "Produces widespread haemorrhage with venous engorgement."]],
  "diagnosis", D, 18),

Q("Chronic open-angle glaucoma", IO,
  "A 59-year-old woman with open-angle glaucoma is started on drops. Which agents are named "
  "first-line?",
  [["Latanoprost, tafluprost or timolol", "Correct."],
   ["Atropine or cyclopentolate", "Cycloplegics, which would worsen a narrow angle."],
   ["Prednisolone drops", "Steroids can raise intraocular pressure."],
   ["Olopatadine", "An antihistamine and mast cell stabiliser for allergic conjunctivitis."],
   ["Acyclovir ointment", "An antiviral for herpetic disease."]],
  "treatment", D, 19),

Q("Chronic open-angle glaucoma", IO,
  "A 70-year-old man with advanced open-angle glaucoma is refractory to drops. What follows?",
  [["Laser trabeculoplasty", "Correct, with surgery as the definitive step."],
   ["Peripheral iridotomy", "That is the angle-closure procedure."],
   ["Intravitreal anti-VEGF", "That treats neovascular macular disease."],
   ["Scleral buckle", "That repairs a retinal detachment."],
   ["Temporal artery biopsy", "That investigates giant cell arteritis."]],
  "treatment", D, 21),

Q("Optic neuritis", IO,
  "Which demographic does optic neuritis most typically affect?",
  [["Women aged 18 to 45", "Correct — about 75% are female."],
   ["Men over 60", "That fits the ischaemic optic neuropathies."],
   ["Children under 10", "Not the described demographic."],
   ["Women over 70", "That fits giant cell arteritis."],
   ["Men aged 18 to 45", "The condition is predominantly female."]],
  "two-step", D, 22),

Q("Optic neuritis", IO,
  "A 29-year-old woman with suspected optic neuritis is referred for imaging. What is ordered?",
  [["Magnetic resonance imaging of brain AND orbits, with and without contrast",
    "Correct."],
   ["Computed tomography of the orbits alone", "Not the study named for this condition."],
   ["Carotid Doppler", "That belongs to the amaurosis fugax workup."],
   ["Ocular ultrasound", "Used to assess retinal detachment."],
   ["Plain skull radiograph", "Not part of the workup."]],
  "two-step", D, 23),

Q("Optic neuritis", IO,
  "A 33-year-old woman with optic neuritis is found to have two demyelinating lesions on imaging. "
  "What follows?",
  [["Referral to neurology or neuro-ophthalmology, with corticosteroids",
    "Correct — steroids if a demyelinating cause is found."],
   ["Observation alone", "The finding changes management."],
   ["Topical pressure-lowering drops", "The pressure is not involved."],
   ["Temporal artery biopsy", "That investigates giant cell arteritis."],
   ["Immediate surgery", "Not a surgical condition."]],
  "treatment", D, 24),

Q("Retinal detachment", IO,
  "A 62-year-old man reports a grey shadow in his peripheral vision that changes as he moves his "
  "head. What does that positional change indicate?",
  [["A retinal detachment", "Correct — the deficit shifts with head position."],
   ["A vitreous haemorrhage alone", "Floaters shift, but the described curtain is the detachment "
                                    "sign."],
   ["Optic neuritis", "Produces a fixed central deficit with pain on movement."],
   ["Papilledema", "Produces transient obscurations rather than a positional shadow."],
   ["Amaurosis fugax", "Resolves completely rather than shifting with posture."]],
  "diagnosis", D, 26),

Q("Retinal detachment", IO,
  "A 57-year-old woman has a suspected retinal detachment but the view of the fundus is poor. Which "
  "investigation is more sensitive than fundoscopy?",
  [["Ocular ultrasound", "Correct — and it types the detachment as well."],
   ["Magnetic resonance imaging", "Not the named modality for this."],
   ["Gonioscopy", "Assesses the drainage angle."],
   ["Fluorescein angiography", "Images retinal and choroidal blood flow."],
   ["Tonometry", "Measures pressure."]],
  "two-step", D, 28),

Q("Retinal detachment", IO,
  "A 60-year-old man has a rhegmatogenous retinal detachment. Which immediate measures are named "
  "alongside the referral?",
  [["Pain control, antiemetics and head of bed at 30 to 40 degrees",
    "Correct — ophthalmology STAT with those supportive measures."],
   ["Lying flat with the head lowered", "The head is elevated, not lowered."],
   ["Immediate irrigation of the eye", "That is the chemical injury pathway."],
   ["Firm padding of the eye", "Not the described management."],
   ["Topical antibiotics", "There is no infection."]],
  "treatment", D, 36),

Q("Retinal detachment", IO,
  "Which surgical options are named for retinal detachment?",
  [["Laser photocoagulation, cryotherapy, pneumatic retinopexy, vitrectomy or scleral buckle",
    "Correct — chosen by type."],
   ["Trabeculoplasty or iridotomy", "Those are glaucoma procedures."],
   ["Intravitreal anti-VEGF alone", "That treats neovascular macular disease."],
   ["Corneal transplantation", "Addresses corneal rather than retinal disease."],
   ["Temporal artery biopsy", "A diagnostic procedure for arteritis."]],
  "two-step", D, 30),

Q("Arteritic AION", IO,
  "A 77-year-old woman has sudden painless vision loss with a NEW temporal headache, scalp "
  "tenderness and jaw claudication. Which investigations rule the diagnosis in or out?",
  [["Erythrocyte sedimentation rate and C-reactive protein",
    "Correct, with temporal artery biopsy as the gold standard."],
   ["Carotid Doppler and echocardiography", "Those belong to the amaurosis fugax workup."],
   ["Magnetic resonance imaging of brain and orbits",
    "That is the optic neuritis workup."],
   ["Gonioscopy and tonometry", "Those assess glaucoma."],
   ["Ocular ultrasound", "Used for retinal detachment."]],
  "two-step", D, 50),

Q("Arteritic AION", IO,
  "A 79-year-old man with giant cell arteritis is started on treatment. What is the named regimen?",
  [["Intravenous methylprednisolone for three days, then a slow oral taper",
    "Correct — typically six to twelve months, with famotidine for ulcer prophylaxis."],
   ["A single dose of oral prednisolone", "Insufficient for this condition."],
   ["Topical corticosteroid drops", "Drops do not treat a systemic vasculitis."],
   ["Aspirin alone", "Insufficient for arteritic disease."],
   ["Observation with weekly review", "Delay risks the fellow eye."]],
  "treatment", D, 51),

Q("Arteritic AION", IO,
  "Why is famotidine added when high-dose corticosteroids are started for giant cell arteritis?",
  [["Ulcer prophylaxis", "Correct."],
   ["To lower intraocular pressure", "Not its purpose."],
   ["To potentiate the steroid", "It does not enhance steroid effect."],
   ["To treat the headache", "Analgesia is a separate matter."],
   ["To prevent osteoporosis", "A real steroid concern, but not what famotidine addresses."]],
  "two-step", D, 51),

Q("Non-arteritic AION", IO,
  "What proportion of anterior ischaemic optic neuropathy is the non-arteritic form?",
  [["Ninety to ninety-five per cent", "Correct — it is by far the commoner form."],
   ["About half", "Roughly half the true share."],
   ["About ten per cent", "That approximates the ARTERITIC share instead."],
   ["About twenty-five per cent", "A quarter of cases, well below the true "
                                  "figure."],
   ["Under five per cent", "Far below the true share."]],
  "two-step", D, 48),

Q("Non-arteritic AION", IO,
  "A 54-year-old man has non-arteritic ischaemic optic neuropathy. Which structural feature is "
  "associated with it?",
  [["A small optic disc, the 'disc at risk'", "Correct, alongside hypertension, diabetes, high "
                                              "cholesterol and sleep apnoea."],
   ["A large excavated optic cup", "That is the glaucomatous disc."],
   ["A long axial length", "That is the myopic eye, associated with detachment."],
   ["A shallow anterior chamber", "That predisposes to angle closure."],
   ["A thin cornea", "Relevant to pressure measurement rather than to this condition."]],
  "two-step", D, 52),

Q("Non-arteritic AION", IO,
  "A 57-year-old man has non-arteritic ischaemic optic neuropathy. What is the management?",
  [["Observation and cardiovascular risk factor modification",
    "Correct, with consideration of avoiding antihypertensives at bedtime."],
   ["High-dose intravenous corticosteroids", "That is the arteritic pathway."],
   ["Urgent temporal artery biopsy and steroids",
    "Biopsy is done to exclude arteritis, but this form is not steroid-treated."],
   ["Immediate surgery", "Not a surgical condition."],
   ["Intravitreal injection", "Not the treatment for this condition."]],
  "treatment", D, 52),

Q("Non-arteritic AION", IO,
  "Why is the workup for non-arteritic ischaemic optic neuropathy identical to the arteritic form?",
  [["It is a diagnosis of exclusion; giant cell arteritis must be ruled out",
    "Correct — missing arteritis costs the other eye."],
   ["Both are treated with steroids", "Only the arteritic form is."],
   ["Both require surgery", "Neither is surgical."],
   ["The two have identical treatment", "Their treatments differ entirely."],
   ["The workup is not in fact the same", "The two workups are in fact identical."]],
  "two-step", D, 52),

Q("Papilledema", IO,
  "A 31-year-old woman has bilateral disc swelling. Which pressure is raised?",
  [["Intracranial pressure", "Correct — the raised pressure is intracranial and NOT "
                             "intraocular."],
   ["Intraocular pressure", "That is glaucoma."],
   ["Both equally", "The raised pressure here is intracranial."],
   ["Neither", "Papilledema by definition reflects raised intracranial pressure."],
   ["Orbital venous pressure alone", "Not the mechanism described."]],
  "two-step", D, 42),

Q("Papilledema", IO,
  "Which causes of papilledema are named?",
  [["Tumour, trauma, intracranial infection, haemorrhage and vitamin A toxicity",
    "Correct."],
   ["Diabetes, hypertension and hyperlipidaemia", "Those are vascular risk factors for other "
                                                  "conditions."],
   ["Contact lens wear and dry eye", "Surface conditions unrelated to intracranial pressure."],
   ["Giant cell arteritis alone", "That causes arteritic ischaemic optic neuropathy."],
   ["Cataract and macular degeneration", "Causes of gradual painless loss."]],
  "two-step", D, 43),

Q("Papilledema", IO,
  "A 27-year-old woman with papilledema is investigated. In what order?",
  [["Imaging to exclude a mass, then lumbar puncture",
    "Correct — a raised opening pressure confirms it."],
   ["Lumbar puncture first, then imaging", "Puncturing before excluding a mass is unsafe."],
   ["Tonometry alone", "Measures the wrong pressure."],
   ["Temporal artery biopsy", "That investigates arteritis."],
   ["Carotid Doppler", "That belongs to the amaurosis pathway."]],
  "treatment", D, 45),

Q("Papilledema", IO,
  "What is the management of papilledema itself?",
  [["Treat the underlying disorder", "Correct — the disc swelling is a sign, not the disease."],
   ["Topical pressure-lowering drops", "They address intraocular pressure, which is not raised."],
   ["Immediate optic nerve surgery", "Not the described management."],
   ["High-dose corticosteroids in all cases", "Not the general management."],
   ["Observation without investigation", "The cause must be found."]],
  "treatment", D, 46),

Q("Branch retinal artery occlusion", IO,
  "How does branch retinal artery occlusion differ from the central form?",
  [["The blockage is in a branch, so only part of the retina is affected",
    "Correct — the field loss is partial and localised, and management does not change."],
   ["It is painful where the central form is painless", "Both are painless."],
   ["It requires different treatment", "Management does not change."],
   ["It affects both eyes", "It is monocular."],
   ["It resolves spontaneously", "It does not."]],
  "two-step", D, 41),

Q("Branch retinal vein occlusion", IO,
  "How does branch retinal vein occlusion differ from the central form?",
  [["The clot is in a smaller branch vein, affecting only part of the retina",
    "Correct — haemorrhage is confined to that territory."],
   ["It is painful", "Both are painless."],
   ["It causes total vision loss", "Only part of the field is lost."],
   ["It needs no referral", "Urgent referral is still required."],
   ["It affects the arterial supply", "It is a venous occlusion."]],
  "two-step", D, 35),
]
