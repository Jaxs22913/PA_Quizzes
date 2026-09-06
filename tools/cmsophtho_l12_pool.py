# -*- coding: utf-8 -*-
"""Acute Vision Loss (Lecture 12) -- Updated ophthalmology masters.

Jaquith's own framing of this lecture is the four questions that separate the
diagnoses: one eye or both, sudden or gradual, central or peripheral, painful
or painless. Several stems are built so that those four are answerable from the
history alone, which is how the exemplars work.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "12. Acute Vision Loss"
IO = ("a — Acute vision loss: etiologies, epidemiology, risk factors, clinical manifestations, "
      "differential diagnosis, diagnostic testing, management, referrals, patient education, "
      "prognosis")

QUESTIONS = [

Q("Central retinal artery occlusion", IO,
  "A 64-year-old African American man presents after going blind in his right eye 'out of the "
  "blue' 20 minutes ago. There is no pain and he is not nauseated. He has had type 2 diabetes "
  "mellitus for 10 years. The left pupil reacts normally and the pressure is 17 mm Hg. The right "
  "pupil shows no reaction to light or accommodation, with a pressure of 20 mm Hg. Right "
  "ophthalmoscopy reveals arteriolar narrowing, vascular stasis and a 'boxcar' pattern. What is "
  "the most likely diagnosis?",
  [["Central retinal artery occlusion", "Correct. Sudden, painless, monocular, with segmented "
                                        "'boxcar' columns in the retinal vessels."],
   ["Acute angle-closure glaucoma", "Painful, with nausea and vomiting, a hazy cornea and a "
                                    "markedly raised pressure — none of which is present."],
   ["Subconjunctival haemorrhage", "A painless red patch on the surface that does not affect "
                                   "vision at all."],
   ["Retinal detachment", "Painless, but preceded by floaters and flashes with a curtain across "
                          "the field rather than instant total loss."],
   ["Macular degeneration", "Gradual central loss over months to years, not 20 minutes."]],
  "diagnosis", D, 38),

Q("Central retinal artery occlusion", IO,
  "A 71-year-old woman has sudden painless loss of vision in the left eye. Fundoscopy shows a pale "
  "retina with a cherry-red spot at the macula. What does the cherry-red spot represent?",
  [["The intact choroidal circulation showing through the thin fovea",
    "Correct. The surrounding retina is pale from infarction; the fovea has no inner retinal "
    "layers to become oedematous."],
   ["Haemorrhage into the fovea", "The spot is a colour contrast, not a bleed."],
   ["A macular hole", "A structural defect, which is not what produces this appearance."],
   ["Retinal pigment epithelium atrophy", "That is a chronic degenerative change."],
   ["Subretinal fluid at the macula", "That would blur rather than sharply define the fovea."]],
  "two-step", D, 39),

Q("Central retinal artery occlusion", IO,
  "A 68-year-old man presents 40 minutes after sudden painless monocular vision loss. What is the "
  "most appropriate next step?",
  [["Immediate ophthalmology referral", "Correct. It is a stroke of the eye — the window is "
                                        "measured in minutes to hours."],
   ["Arrange outpatient review within a week", "Delay of days forfeits any chance of recovery."],
   ["Prescribe topical antibiotics", "There is no infection."],
   ["Reassure and observe overnight", "Observation wastes the only window there is."],
   ["Start oral corticosteroids and review in a month",
    "Steroids are for giant cell arteritis, and even then are given urgently."]],
  "treatment", D, 40),

Q("Amaurosis fugax", IO,
  "A 69-year-old man describes a curtain descending over the vision of his right eye, lasting "
  "about five minutes, with complete recovery. He has hypertension and smokes. Examination between "
  "episodes is normal. What is the most appropriate next step?",
  [["Carotid imaging and urgent stroke workup", "Correct. It is a transient ischaemic attack of "
                                                "the eye and carries the same stroke risk."],
   ["Reassurance, as vision has recovered", "Recovery is the feature that makes it a warning "
                                            "rather than an endpoint."],
   ["Topical antiglaucoma drops", "The pressure is not the problem."],
   ["Refer routinely to optometry", "This needs vascular workup, not refraction."],
   ["Start an oral antihistamine", "There is no allergic process."]],
  "treatment", D, 6),

Q("Acute angle-closure glaucoma", IO,
  "A 48-year-old patient has acute blurring of vision and severe pain in the left eye that began "
  "30 minutes ago, with halos around lights. They are nauseated and have vomited. The pain started "
  "while they were relaxing on their porch. Temperature 36.9°C, pulse 90/min, blood pressure "
  "130/90 mm Hg, respirations 20/min. Examination reveals a shallow anterior chamber, a hazy "
  "cornea, a fixed moderately dilated pupil and ciliary injection. What is the most appropriate "
  "next step in managing this patient?",
  [["Tonometry", "Correct. Measuring the intraocular pressure confirms the diagnosis and is the "
                 "immediate step."],
   ["Topical atropine to facilitate ophthalmoscopy",
    "Dilating the pupil would worsen the angle closure — actively dangerous here."],
   ["Discharge with topical antibiotic eye drops", "There is no infection, and discharge would be "
                                                   "sight-threatening."],
   ["Lumbar puncture", "The headache and vomiting are ocular in origin, not meningeal."],
   ["X-ray to rule out a foreign body", "There is no history of trauma."]],
  "treatment", D, 13),

Q("Acute angle-closure glaucoma", IO,
  "A 40-year-old man has severe pain in the left eye, decreased vision and nausea. He denies "
  "trauma. He wears glasses. On examination the left pupil is moderately dilated and nonreactive, "
  "the cornea is 'steamy', and the eye is diffusely red. What is the most likely diagnosis?",
  [["Acute angle-closure glaucoma", "Correct. Pain, nausea, a mid-dilated fixed pupil and a hazy "
                                    "cornea together are the classic picture."],
   ["Conjunctivitis", "The pupil is normal and reactive, and there is no severe pain or nausea."],
   ["Uveitis", "Painful and photophobic, but the pupil is small and sluggish rather than mid-dilated "
               "and fixed."],
   ["Corneal infection", "Produces a focal infiltrate with an epithelial defect, not a uniformly "
                         "steamy cornea with a fixed pupil."],
   ["Presbyopia", "An age-related focusing change that is painless and causes no redness."]],
  "diagnosis", D, 14),

Q("Acute angle-closure glaucoma", IO,
  "A 56-year-old woman has confirmed acute angle-closure glaucoma. Which anatomical feature "
  "predisposed her to it?",
  [["A shallow anterior chamber", "Correct — a crowded angle is what allows closure when the pupil "
                                  "dilates."],
   ["A deep anterior chamber", "A deep chamber protects against angle closure."],
   ["A large corneal diameter", "Not the predisposing feature."],
   ["A thin cornea", "Relevant to pressure measurement rather than to angle closure."],
   ["A long axial length", "Long eyes are myopic and are at LOWER risk of angle closure."]],
  "two-step", D, 16),

Q("Chronic open-angle glaucoma", IO,
  "A 62-year-old man is found on screening to have an intraocular pressure of 26 mm Hg in both "
  "eyes with an enlarged optic cup. He has no symptoms. Which visual field is lost first?",
  [["The peripheral field", "Correct. Central acuity is preserved until late, which is why it is "
                            "found on screening rather than by the patient."],
   ["The central field", "Central loss occurs late in the disease."],
   ["The superior field only", "Arcuate defects appear, but loss is not confined to a single hemifield at onset."],
   ["The inferior field only", "Nor is it confined to the lower hemifield."],
   ["The temporal field of one eye only", "That pattern suggests a chiasmal lesion."]],
  "two-step", D, 18),

Q("Chronic open-angle glaucoma", IO,
  "A 58-year-old woman with newly diagnosed open-angle glaucoma is started on treatment. Which "
  "class is first line?",
  [["A prostaglandin analogue", "Correct. Prostaglandins or beta blockers lead; cholinergic agents "
                                "are third or fourth line."],
   ["A cholinergic agonist", "Causes miosis and blocks accommodation, which is why it is reserved "
                             "for later lines."],
   ["A topical corticosteroid", "Steroids can RAISE intraocular pressure."],
   ["A topical antihistamine", "There is no allergic component."],
   ["A topical antibiotic", "There is no infection."]],
  "treatment", D, 19),

Q("Optic neuritis", IO,
  "A 28-year-old woman has blurring of vision in the right eye over two days with pain on eye "
  "movement. Colour appears washed out. Examination shows a relative afferent pupillary defect on "
  "the right and a normal-looking optic disc. What is the most likely diagnosis?",
  [["Optic neuritis", "Correct. Pain on eye movement, dyschromatopsia and a relative afferent "
                      "pupillary defect. The deck lists optic neuritis among the causes of that defect."],
   ["Central retinal artery occlusion", "Painless and instantaneous, with a pale retina."],
   ["Acute angle-closure glaucoma", "Severely painful with a hazy cornea and fixed mid-dilated "
                                    "pupil."],
   ["Papilledema", "Bilateral disc swelling with preserved acuity, not a unilateral afferent "
                   "defect."],
   ["Amaurosis fugax", "Transient and fully recovered, not progressive over two days."]],
  "diagnosis", D, 22),

Q("Optic neuritis", IO,
  "A 30-year-old woman with optic neuritis asks what it might mean for her long term. Which "
  "association should be discussed?",
  [["Multiple sclerosis", "Correct. It is a common presenting feature, and imaging looks for "
                          "demyelinating lesions."],
   ["Giant cell arteritis", "That causes arteritic ischaemic optic neuropathy in older patients."],
   ["Diabetes mellitus", "Associated with retinopathy rather than optic neuritis."],
   ["Hypertension", "Associated with retinal vascular disease rather than optic neuritis."],
   ["Thyroid eye disease", "Causes proptosis and restrictive myopathy."]],
  "two-step", D, 23),

Q("Retinal detachment", IO,
  "A 59-year-old myopic man reports a shower of new floaters and flashes of light in the right eye "
  "yesterday, followed today by a dark curtain rising across the lower half of his vision. There is "
  "no pain. What is the most likely diagnosis?",
  [["Retinal detachment", "Correct. Floaters and flashes followed by a painless curtain across the "
                          "field, in a myopic patient."],
   ["Central retinal vein occlusion", "Sudden painless loss with widespread haemorrhages, not a "
                                      "progressive curtain preceded by flashes."],
   ["Acute angle-closure glaucoma", "Painful, with nausea and a hazy cornea."],
   ["Optic neuritis", "Pain on eye movement with colour desaturation."],
   ["Vitreous haemorrhage", "Can cause floaters, but the advancing curtain with flashes points to "
                            "detachment."]],
  "diagnosis", D, 26),

Q("Retinal detachment", IO,
  "A 61-year-old woman has a retinal detachment with the macula still attached. Why does that "
  "detail change the urgency?",
  [["Central vision is still salvageable if repaired before the macula detaches",
    "Correct — macula-on detachment is the more urgent repair."],
   ["It means the detachment will reattach spontaneously", "Detachments do not reattach without "
                                                           "intervention."],
   ["It indicates an exudative rather than rhegmatogenous cause",
    "Macular status does not distinguish the type."],
   ["It means surgery can safely be delayed a month", "Delay risks the macula detaching."],
   ["It confirms the cause is traction", "Macular involvement does not identify the mechanism."]],
  "two-step", D, 29),

Q("Central retinal vein occlusion", IO,
  "A 67-year-old hypertensive man has sudden painless blurring of the right eye. Fundoscopy shows "
  "widespread retinal haemorrhages in all four quadrants with dilated tortuous veins and disc "
  "swelling. What is the most likely diagnosis?",
  [["Central retinal vein occlusion", "Correct. The 'blood and thunder' fundus — haemorrhages in "
                                      "every quadrant with engorged veins."],
   ["Central retinal artery occlusion", "A PALE retina with a cherry-red spot and boxcarring, not "
                                        "widespread haemorrhage."],
   ["Branch retinal vein occlusion", "Haemorrhages follow ONE vein's distribution rather than all "
                                     "four quadrants."],
   ["Papilledema", "Bilateral disc swelling without this haemorrhage pattern."],
   ["Diabetic retinopathy", "Chronic, bilateral, with microaneurysms and exudates."]],
  "diagnosis", D, 32),

Q("Branch retinal vein occlusion", IO,
  "A 63-year-old woman has painless loss of part of her upper visual field. Fundoscopy shows "
  "haemorrhages confined to a wedge of retina below the macula, stopping at the horizontal raphe. "
  "What is the most likely diagnosis?",
  [["Branch retinal vein occlusion", "Correct. The changes respect the territory of a single "
                                     "branch vein."],
   ["Central retinal vein occlusion", "Haemorrhages would involve all four quadrants."],
   ["Branch retinal artery occlusion", "Produces a pale wedge of retina rather than haemorrhage."],
   ["Retinal detachment", "Preceded by floaters and flashes, with an elevated retina."],
   ["Optic neuritis", "Painful on movement with an afferent pupillary defect."]],
  "diagnosis", D, 35),

Q("Arteritic AION", IO,
  "A 74-year-old woman has sudden painless loss of vision in the left eye. She has had scalp "
  "tenderness when brushing her hair and aching in the jaw when chewing for three weeks. The "
  "erythrocyte sedimentation rate is markedly raised. What is the most appropriate next step?",
  [["Start high-dose corticosteroids immediately",
    "Correct. Treatment precedes biopsy — the other eye is at risk within days."],
   ["Arrange temporal artery biopsy and treat once the result is back",
    "Biopsy is confirmatory, but waiting risks the fellow eye."],
   ["Arrange outpatient review in two weeks", "Far too slow for a condition that blinds the second "
                                              "eye."],
   ["Start aspirin alone", "Insufficient for arteritic disease."],
   ["Refer for carotid imaging first", "That is the amaurosis fugax pathway."]],
  "treatment", D, 50),

Q("Arteritic AION", IO,
  "A 78-year-old man with giant cell arteritis and vision loss in one eye asks why he must start "
  "treatment today rather than wait for the biopsy. What is the reason?",
  [["The fellow eye can be lost within days", "Correct."],
   ["The biopsy becomes negative after treatment starts",
    "Biopsy remains informative for a period after steroids begin."],
   ["The erythrocyte sedimentation rate will normalise and obscure the diagnosis",
    "The rate does fall, but the reason for urgency is the second eye."],
   ["Steroids are only effective in the first hour", "The window is longer than that."],
   ["The vision in the affected eye will return", "Vision already lost usually does not recover."]],
  "two-step", D, 51),

Q("Non-arteritic AION", IO,
  "A 59-year-old man with hypertension and sleep apnoea wakes with painless loss of the lower half "
  "of the visual field in one eye. There is no scalp tenderness or jaw claudication, and the "
  "inflammatory markers are normal. What is the most likely diagnosis?",
  [["Non-arteritic anterior ischaemic optic neuropathy",
    "Correct. Altitudinal field loss on waking, with normal inflammatory markers and no arteritic "
    "symptoms."],
   ["Arteritic anterior ischaemic optic neuropathy",
    "Would carry scalp tenderness, jaw claudication and a raised sedimentation rate."],
   ["Optic neuritis", "Painful on eye movement and typically in a younger patient."],
   ["Central retinal artery occlusion", "Produces total rather than altitudinal loss, with a pale "
                                        "retina."],
   ["Retinal detachment", "Preceded by flashes and floaters."]],
  "diagnosis", D, 52),

Q("Papilledema", IO,
  "A 26-year-old woman with headaches worse on waking has transient visual obscurations lasting "
  "seconds. Fundoscopy shows BILATERAL swollen optic discs. Visual acuity is 6/6 in both eyes. "
  "What is the most appropriate next step?",
  [["Neuroimaging, then lumbar puncture if imaging is normal",
    "Correct. Bilateral disc swelling means raised intracranial pressure until proven otherwise."],
   ["Start topical antiglaucoma drops", "The pressure raised here is intracranial, not "
                                        "intraocular."],
   ["Reassure, since acuity is normal", "Preserved acuity is characteristic and does not exclude "
                                        "the diagnosis."],
   ["Start high-dose corticosteroids for arteritis",
    "Arteritic disease affects older patients and is not bilateral disc swelling with normal "
    "acuity."],
   ["Refer routinely to optometry", "This requires urgent neurological evaluation."]],
  "treatment", D, 44),

Q("Papilledema", IO,
  "A 31-year-old woman has bilateral disc swelling. What distinguishes papilledema from optic "
  "neuritis on examination?",
  [["Acuity is preserved in papilledema and reduced in optic neuritis",
    "Correct, and papilledema is bilateral while optic neuritis is usually unilateral with an "
    "afferent pupillary defect."],
   ["Papilledema is painful on eye movement", "Pain on movement belongs to optic neuritis."],
   ["Papilledema causes a relative afferent pupillary defect",
    "That is the optic neuritis finding."],
   ["Papilledema causes colour desaturation early", "Dyschromatopsia is an optic neuritis "
                                                    "feature."],
   ["Papilledema is always unilateral", "It is bilateral, reflecting raised intracranial "
                                        "pressure."]],
  "two-step", D, 45),

Q("Acute vision loss approach", IO,
  "A patient presents with acute vision loss. Which four questions does the initial assessment turn "
  "on?",
  [["One eye or both, sudden or gradual, central or peripheral, painful or painless",
    "Correct — those four separate almost the whole differential before any test."],
   ["Age, sex, ethnicity and family history",
    "Demographics inform risk but are not the four separating questions."],
   ["Visual acuity, pressure, pupil and fundus",
    "That is the examination sequence rather than the four history questions."],
   ["Onset, duration, severity and relieving factors",
    "A generic pain history, not the framework used here."],
   ["Trauma, infection, inflammation and neoplasm",
    "A cause list rather than the separating questions."]],
  "two-step", D, 4),
]
