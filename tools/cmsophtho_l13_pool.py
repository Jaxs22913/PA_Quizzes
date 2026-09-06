# -*- coding: utf-8 -*-
"""Chronic Vision Loss and Tumors (Lecture 13) -- Updated ophthalmology masters.

The tumour rows carry the highest stakes in the block: retinoblastoma and uveal
melanoma are the two where getting it wrong costs an eye or a life, so they are
weighted accordingly rather than proportionally to slide count.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "Chronic Vision Loss & Tumors"
IO = ("a — Chronic vision loss and ocular tumors: etiologies, epidemiology, risk factors, clinical "
      "manifestations, differential diagnosis, diagnostic testing, management, referrals, patient "
      "education, prognosis")

QUESTIONS = [

Q("Dry macular degeneration", IO,
  "A 76-year-old woman has noticed over two years that straight lines look wavy and she needs more "
  "light to read. Vision is 6/12 bilaterally. Fundoscopy shows yellowish deposits at the macula "
  "with pigmentary change but no haemorrhage. What is the most likely diagnosis?",
  [["Dry age-related macular degeneration", "Correct. Drusen and pigment change with gradual "
                                            "central loss over years."],
   ["Wet age-related macular degeneration", "Presents with RAPID distortion and subretinal "
                                            "haemorrhage or fluid."],
   ["Open-angle glaucoma", "Takes the peripheral field first and spares central acuity until "
                           "late."],
   ["Cataract", "Causes generalised blur and glare rather than distortion of straight lines."],
   ["Retinal detachment", "Sudden, with flashes, floaters and a curtain."]],
  "diagnosis", D, 14),

Q("Wet macular degeneration", IO,
  "An 80-year-old man reports that over the past week straight lines have become sharply distorted "
  "in the right eye and a grey patch has appeared in the centre of his vision. Fundoscopy shows "
  "subretinal fluid and haemorrhage at the macula. What is the most appropriate next step?",
  [["Urgent referral for intravitreal anti-VEGF therapy",
    "Correct. The wet form is treatable and the window matters."],
   ["Reassure and review in six months", "Delay costs central vision that treatment could save."],
   ["Prescribe high-dose antioxidant supplements alone",
    "Supplements slow progression in dry disease; they do not treat active wet disease."],
   ["Refer for cataract surgery", "The lens is not the problem."],
   ["Start topical corticosteroids", "Not the treatment for choroidal neovascularisation."]],
  "treatment", D, 14),

Q("Macular degeneration", IO,
  "A 72-year-old woman with dry macular degeneration is given a grid of straight lines to check at "
  "home. What is she being asked to detect?",
  [["Distortion or a missing area, suggesting conversion to the wet form",
    "Correct — the Amsler grid is a self-monitoring tool for exactly that change."],
   ["A change in colour vision", "Not what the grid detects."],
   ["Peripheral field loss", "The grid tests central vision only."],
   ["Progressive lens opacity", "That is assessed by examination, not by a grid."],
   ["Raised intraocular pressure", "Requires tonometry."]],
  "two-step", D, 14),

Q("Nuclear cataract", IO,
  "A 71-year-old man reports gradually blurring distance vision and increasing glare from oncoming "
  "headlights at night. He mentions he no longer needs his reading glasses. What explains the "
  "improvement in near vision?",
  [["A myopic shift from nuclear sclerosis",
    "Correct — 'second sight'. The hardening lens increases its refractive power."],
   ["Improvement in accommodation with age", "Accommodation declines with age; it does not "
                                             "recover."],
   ["Development of hyperopia", "A hyperopic shift would worsen near vision."],
   ["Reduced corneal astigmatism", "Would not selectively improve near vision."],
   ["Onset of presbyopia", "Presbyopia worsens near vision, which is why reading glasses are "
                           "needed."]],
  "two-step", D, 36),

Q("Posterior subcapsular cataract", IO,
  "A 54-year-old woman on long-term oral corticosteroids for rheumatoid arthritis has increasing "
  "glare and difficulty reading, worse in bright light. Which cataract type is most likely?",
  [["Posterior subcapsular", "Correct — associated with steroid use, and it disproportionately "
                             "affects near vision and glare because it sits on the visual axis."],
   ["Nuclear", "Age-related central lens hardening, causing a myopic shift."],
   ["Cortical", "Spoke-like peripheral opacities, classically with diabetes."],
   ["Congenital", "Present from birth, not acquired in adulthood."],
   ["Traumatic", "Follows a specific injury, which is not described."]],
  "diagnosis", D, 36),

Q("Pediatric cataract", IO,
  "A 5-week-old infant is found to have an absent red reflex in the left eye at the newborn check. "
  "What is the most appropriate next step?",
  [["Urgent ophthalmology referral", "Correct. An absent red reflex demands urgent assessment — "
                                     "cataract and retinoblastoma both present this way."],
   ["Review at the six-month check", "Delay risks irreversible amblyopia and, if it is a tumour, "
                                     "far worse."],
   ["Reassure, as red reflex varies in newborns", "An absent reflex is never a normal variant."],
   ["Prescribe patching of the right eye", "Treatment cannot precede diagnosis."],
   ["Arrange a hearing test", "Does not address the ocular finding."]],
  "treatment", D, 38),

Q("Retinoblastoma", IO,
  "A 14-month-old boy is brought in because his mother noticed a white glow in his right pupil in "
  "photographs. There is no redness or discharge. What is the most likely diagnosis?",
  [["Retinoblastoma", "Correct. Leukocoria in a young child is retinoblastoma until proven "
                      "otherwise."],
   ["Congenital cataract", "Also causes leukocoria and must be excluded, but the malignant cause "
                           "is what drives the urgency."],
   ["Coats disease", "Can cause leukocoria, but is far less common than the diagnosis that must be "
                     "excluded first."],
   ["Strabismus alone", "Misalignment does not produce a white pupil."],
   ["Conjunctivitis", "A surface infection with redness and discharge."]],
  "diagnosis", D, 41),

Q("Retinoblastoma", IO,
  "A 2-year-old girl is diagnosed with bilateral retinoblastoma. What does bilateral disease imply?",
  [["A heritable germline mutation", "Correct — bilateral disease is germline, with implications "
                                     "for siblings and for second malignancies."],
   ["A better prognosis than unilateral disease", "Bilateral disease is germline and carries added "
                                                  "risk, not a better outlook."],
   ["That the tumour is benign", "Retinoblastoma is malignant."],
   ["That no genetic counselling is needed", "Germline disease makes counselling essential."],
   ["That it was caused by an infection", "It is a genetic malignancy."]],
  "two-step", D, 42),

Q("Uveal melanoma", IO,
  "A 63-year-old man is found on routine examination to have a raised pigmented choroidal lesion "
  "with orange pigment and associated subretinal fluid. What is the most appropriate next step?",
  [["Urgent ophthalmology referral", "Correct. Orange pigment, thickness and subretinal fluid are "
                                     "the features that separate melanoma from a benign nevus."],
   ["Photograph and review in two years", "Those risk features warrant urgent assessment."],
   ["Reassure, as choroidal pigmentation is common",
    "Common, but not with orange pigment and subretinal fluid."],
   ["Start topical corticosteroids", "There is no inflammatory process."],
   ["Refer for cataract surgery", "The lens is not involved."]],
  "treatment", D, 45),

Q("Uveal melanoma", IO,
  "A 58-year-old woman with a choroidal melanoma asks where it would spread if it did. Which organ "
  "is the classic site?",
  [["The liver", "Correct — uveal melanoma spreads haematogenously, and the liver is the classic "
                 "site."],
   ["The brain", "A site for cutaneous melanoma spread, but not the classic one here."],
   ["The lung", "Involved in many malignancies but not the classic site for this one."],
   ["Regional lymph nodes", "The uvea has no lymphatic drainage, which is why spread is "
                            "haematogenous."],
   ["Bone", "Not the classic first site."]],
  "two-step", D, 46),

Q("Iris nevus", IO,
  "A 46-year-old man has a flat, pigmented iris lesion that has been unchanged on photographs over "
  "five years, with no distortion of the pupil. What is the most appropriate management?",
  [["Photographic monitoring", "Correct. Documented stability over years supports a benign nevus."],
   ["Immediate enucleation", "Grossly disproportionate to a stable, flat lesion."],
   ["Excisional biopsy of the iris", "Not indicated for a lesion documented as stable."],
   ["Topical chemotherapy", "Not a treatment for a benign iris nevus."],
   ["Urgent systemic staging", "Reserved for lesions with malignant features."]],
  "treatment", D, 48),

Q("Conjunctival melanoma", IO,
  "A 67-year-old woman has a raised pigmented conjunctival lesion that has enlarged over six months "
  "and has its own feeding vessels. What is the most appropriate next step?",
  [["Urgent referral for biopsy", "Correct. Growth and intrinsic vascularity are the concerning "
                                  "features."],
   ["Reassure, as conjunctival pigment is common in this age group",
    "Common, but not one that grows and develops feeding vessels."],
   ["Prescribe lubricating drops", "Does not address a growing pigmented lesion."],
   ["Photograph and review in two years", "The growth already documented warrants action now."],
   ["Start topical antibiotics", "There is no infection."]],
  "treatment", D, 53),

Q("Myopia", IO,
  "A 15-year-old girl cannot read the board at school but reads comfortably at her desk. Which "
  "refractive error is this, and how is the eye shaped?",
  [["Myopia, with the eye too long", "Correct. Light focuses in front of the retina, so distance "
                                     "is blurred and near is clear."],
   ["Hyperopia, with the eye too short", "Light focuses behind the retina; near vision suffers "
                                         "first."],
   ["Astigmatism, from an irregular cornea", "Blurs at all distances rather than distance alone."],
   ["Presbyopia, from a stiffening lens", "An age-related near problem, not seen at 15."],
   ["Amblyopia, from visual deprivation", "Reduced vision not correctable by lenses."]],
  "diagnosis", D, 18),

Q("Hyperopia", IO,
  "A 9-year-old boy has headaches and eye strain when reading, and his distance vision is normal. "
  "Which refractive error is most likely?",
  [["Hyperopia", "Correct — the eye is too short and accommodative effort at near produces the "
                 "strain."],
   ["Myopia", "Would blur distance vision, which is normal here."],
   ["Presbyopia", "An age-related loss of accommodation, not seen at nine."],
   ["Astigmatism", "Blurs at all distances rather than producing near strain alone."],
   ["Amblyopia", "Reduced vision that glasses do not correct."]],
  "diagnosis", D, 19),

Q("Astigmatism", IO,
  "A 22-year-old woman reports that letters look smeared at every distance, and her vision does not "
  "clear with a pinhole in one meridian. What is the underlying problem?",
  [["An irregularly curved cornea", "Correct — astigmatism focuses light along two different "
                                    "meridians."],
   ["An eye that is too long", "That is myopia, which blurs distance selectively."],
   ["An eye that is too short", "That is hyperopia, which strains at near."],
   ["A stiffened crystalline lens", "That is presbyopia, affecting near vision with age."],
   ["Opacity of the lens", "A cataract causes glare and generalised blur, not meridional smearing."]],
  "diagnosis", D, 20),

Q("Strabismus", IO,
  "A 3-year-old boy has an eye that turns inward. The cover test shows the left eye moving out to "
  "take up fixation when the right is covered. What is the most appropriate next step?",
  [["Refer to ophthalmology", "Correct. Manifest misalignment in a child needs assessment to "
                              "prevent amblyopia."],
   ["Reassure, as children outgrow this", "A constant manifest deviation does not resolve on its "
                                          "own."],
   ["Prescribe reading glasses and review in a year",
    "Refraction may be part of treatment, but the referral comes first."],
   ["Patch the deviating eye", "Patching is applied to the BETTER eye, and only once assessed."],
   ["Arrange surgery immediately", "Assessment precedes any surgical decision."]],
  "treatment", D, 29),

Q("Amblyopia", IO,
  "A 6-year-old girl has 6/6 vision in the right eye and 6/24 in the left, which does not improve "
  "with glasses. The eyes are straight and the fundi are normal. What is the treatment principle?",
  [["Patch the BETTER eye to force use of the weaker one",
    "Correct — occlusion therapy drives cortical development in the amblyopic eye."],
   ["Patch the weaker eye to rest it", "That would worsen the amblyopia."],
   ["Prescribe glasses alone and review in a year",
    "Refractive correction alone is insufficient once amblyopia is established."],
   ["Operate to align the eyes", "The eyes are already straight."],
   ["Observe until age ten", "The window for treatment closes with visual maturity."]],
  "treatment", D, 32),

Q("Amblyopia", IO,
  "A 10-year-old boy is diagnosed with amblyopia for the first time. Why does his age matter?",
  [["Treatment is less effective once visual maturity approaches",
    "Correct — the earlier it is treated, the better the outcome."],
   ["Amblyopia only occurs after age ten", "It develops in early childhood."],
   ["Glasses cannot be prescribed at this age", "Refractive correction is available at any age."],
   ["Surgery becomes the only option at ten", "Amblyopia is not treated surgically."],
   ["It will resolve spontaneously by adolescence", "Untreated amblyopia persists."]],
  "two-step", D, 33),

Q("Idiopathic intracranial hypertension", IO,
  "A 24-year-old woman with a raised body mass index has daily headaches, pulsatile tinnitus and "
  "transient visual obscurations. Fundoscopy shows bilateral disc swelling. Neuroimaging is normal. "
  "What is the most likely diagnosis?",
  [["Idiopathic intracranial hypertension", "Correct — the classic demographic, with papilledema "
                                            "and normal imaging."],
   ["Optic neuritis", "Unilateral, painful on eye movement, with an afferent pupillary defect."],
   ["Malignant hypertension", "Would show markedly raised blood pressure and retinal changes."],
   ["Giant cell arteritis", "Affects older patients with scalp tenderness and jaw claudication."],
   ["Migraine with aura", "Does not produce papilledema."]],
  "diagnosis", D, 4),

Q("Idiopathic intracranial hypertension", IO,
  "A 27-year-old woman with idiopathic intracranial hypertension asks what is at stake if it is "
  "not treated. What should she be told?",
  [["Permanent visual loss from optic nerve damage",
    "Correct — the vision, not the headache, is what drives treatment."],
   ["Progression to a brain tumour", "It is not a neoplastic process."],
   ["Permanent hearing loss", "The tinnitus is pulsatile and resolves with the pressure."],
   ["Development of cataract", "Unrelated to intracranial pressure."],
   ["Retinal detachment", "Not a consequence of raised intracranial pressure."]],
  "two-step", D, 5),
]
