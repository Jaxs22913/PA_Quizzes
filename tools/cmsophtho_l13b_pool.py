# -*- coding: utf-8 -*-
"""Chronic Vision Loss and Tumors (Lecture 13) -- second pool."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "Chronic Vision Loss & Tumors"
IO = ("a — Chronic vision loss and ocular tumors: etiologies, epidemiology, risk factors, clinical "
      "manifestations, differential diagnosis, diagnostic testing, management, referrals, patient "
      "education, prognosis")

QUESTIONS = [

Q("Cortical cataract", IO,
  "A 66-year-old woman with long-standing type 2 diabetes has increasing glare, particularly when "
  "driving at night. Slit lamp examination shows spoke-like opacities radiating from the periphery "
  "of the lens. Which cataract type is this?",
  [["Cortical", "Correct — the spoke-like peripheral wedges, classically associated with "
                "diabetes."],
   ["Nuclear", "Central lens hardening producing a myopic shift."],
   ["Posterior subcapsular", "A plaque on the back of the lens, associated with steroid use."],
   ["Congenital", "Present from birth rather than acquired."],
   ["Traumatic", "Follows a specific injury, which is not described."]],
  "diagnosis", D, 37),

Q("Cataract", IO,
  "A 73-year-old man has bilateral cataracts and vision of 6/18. He has stopped driving and finds "
  "reading difficult. What determines whether he is offered surgery?",
  [["The effect on his daily functioning", "Correct — the decision is driven by symptoms and "
                                           "function rather than by an acuity threshold alone."],
   ["A fixed visual acuity cut-off", "Function rather than a single number drives the decision."],
   ["His intraocular pressure", "Pressure is a glaucoma consideration."],
   ["The presence of a relative afferent pupillary defect",
    "That would indicate optic nerve disease rather than lens opacity."],
   ["His age alone", "Age is not the criterion."]],
  "treatment", D, 37),

Q("Cataract", IO,
  "A 69-year-old woman has had cataract surgery. Which later complication is she now more likely "
  "to develop?",
  [["Posterior vitreous detachment", "Correct — cataract surgery, myopia and ocular "
                                     "trauma all make it more likely."],
   ["Acute angle-closure glaucoma", "Associated with the short hyperopic eye rather than with "
                                    "previous surgery."],
   ["Optic neuritis", "A demyelinating condition unrelated to lens surgery."],
   ["Trachoma", "An infectious cicatricial disease unrelated to surgery."],
   ["Amblyopia", "A developmental condition of childhood."]],
  "two-step", D, 37),

Q("Macular degeneration", IO,
  "A 78-year-old man with dry macular degeneration asks whether anything slows it. What is offered?",
  [["Antioxidant and zinc supplementation", "Correct — supplementation slows progression in "
                                            "intermediate dry disease."],
   ["Intravitreal anti-VEGF injections", "Those treat the wet form."],
   ["Laser trabeculoplasty", "That treats glaucoma."],
   ["Cataract surgery", "Addresses the lens, not the macula."],
   ["Topical corticosteroids", "No role in dry macular degeneration."]],
  "treatment", D, 14),

Q("Macular degeneration", IO,
  "A 74-year-old woman has macular degeneration. Which part of her vision is preserved?",
  [["The peripheral field", "Correct — central vision is lost while navigational vision "
                            "remains."],
   ["The central field", "That is precisely what is lost."],
   ["Colour vision only", "Colour perception is largely central and is affected."],
   ["Reading vision", "Reading depends on the macula and is lost early."],
   ["Fine detail at distance", "Also macular and affected."]],
  "two-step", D, 11),

Q("Retinoblastoma", IO,
  "A 20-month-old boy has leukocoria and a convergent squint. Which two presenting features are "
  "most common in retinoblastoma?",
  [["Leukocoria and strabismus", "Correct — a white pupil and a squint are the two classic "
                                 "presentations."],
   ["Pain and photophobia", "Retinoblastoma is typically painless."],
   ["Redness and discharge", "Those suggest infection."],
   ["Proptosis and fever", "Those suggest orbital cellulitis."],
   ["Tearing and lid swelling", "Those suggest lacrimal or lid disease."]],
  "two-step", D, 41),

Q("Retinoblastoma", IO,
  "A 3-year-old girl with unilateral retinoblastoma is referred. Why does the referral need to be "
  "urgent rather than routine?",
  [["It is a life-threatening malignancy, not only a threat to sight",
    "Correct — delay risks metastatic spread."],
   ["The eye will become painful within days", "It is typically painless."],
   ["The squint will become permanent", "The squint is a sign, not the reason for urgency."],
   ["The cataract will mature", "The white pupil is tumour, not cataract."],
   ["The other eye will be affected within a week", "Bilaterality reflects germline status rather "
                                                    "than rapid spread."]],
  "two-step", D, 42),

Q("Uveal melanoma", IO,
  "A 60-year-old man has a small, flat, uniformly pigmented choroidal lesion with drusen on its "
  "surface and no subretinal fluid. What is the most appropriate management?",
  [["Photographic surveillance", "Correct. Flatness, drusen and absent fluid all favour a benign "
                                 "nevus."],
   ["Urgent enucleation", "Grossly disproportionate for a lesion with benign features."],
   ["Immediate treatment as a melanoma", "Reserved for lesions with malignant features."],
   ["Systemic chemotherapy", "Not indicated for a benign nevus."],
   ["Intravitreal anti-VEGF", "That treats neovascular macular disease."]],
  "treatment", D, 49),

Q("Amblyopia", IO,
  "A 3-year-old boy is unbothered when his left eye is covered, but becomes fussy when his right "
  "eye is covered. What does this test show?",
  [["The left eye is amblyopic", "Correct. The occlusion objection test: the child objects when "
                                 "the GOOD eye is covered."],
   ["The right eye is amblyopic", "He tolerates the left being covered, so the left is the weaker "
                                  "eye."],
   ["Both eyes are equally affected", "He reacts differently to each, so they are not equal."],
   ["Neither eye is amblyopic", "The asymmetric reaction is the abnormal finding."],
   ["He has a sixth nerve palsy", "That produces horizontal diplopia and esotropia, not this "
                                  "response to occlusion."]],
  "diagnosis", D, 32),

Q("Strabismus", IO,
  "A 6-year-old girl is referred with strabismus. At which levels of the visual motor system can "
  "the cause lie?",
  [["Brain, cranial nerves, neuromuscular junction or extraocular muscles",
    "Correct — causes are found at all four levels."],
   ["The cornea and lens only", "Those are refractive structures, not motor ones."],
   ["The retina alone", "The retina is sensory rather than motor."],
   ["The optic nerve alone", "That carries vision rather than moving the eye."],
   ["The lacrimal system", "Tear drainage has no role in ocular alignment."]],
  "two-step", D, 29),

Q("Myopia", IO,
  "A 19-year-old man with high myopia is counselled about long-term risks. Which is he at "
  "increased risk of?",
  [["Retinal detachment", "Correct — the longer eye has a thinner, more vulnerable peripheral "
                          "retina."],
   ["Acute angle-closure glaucoma", "Angle closure is associated with the SHORT, hyperopic eye."],
   ["Hyperopia in later life", "Refractive error does not reverse."],
   ["Retinoblastoma", "A childhood malignancy unrelated to refractive error."],
   ["Trachoma", "An infectious cicatricial disease unrelated to refraction."]],
  "two-step", D, 18),

Q("Hyperopia", IO,
  "A 58-year-old hyperopic woman is warned about one particular ocular emergency. Which is it?",
  [["Acute angle-closure glaucoma", "Correct — the short eye has a crowded anterior segment."],
   ["Retinal detachment", "More associated with the long, myopic eye."],
   ["Central retinal vein occlusion", "A vascular event unrelated to refraction."],
   ["Optic neuritis", "A demyelinating condition unrelated to refraction."],
   ["Corneal ulcer", "Related to contact lens wear rather than refraction."]],
  "two-step", D, 19),

Q("Presbyopia", IO,
  "A 46-year-old man finds he must hold text further away to read it, while distance vision is "
  "unchanged. What is the mechanism?",
  [["The lens loses elasticity, so accommodation fails",
    "Correct — the A in PERRLA is what is failing."],
   ["The eye becomes too long", "That would produce myopia."],
   ["The eye becomes too short", "That would produce hyperopia."],
   ["The cornea becomes irregular", "That would produce astigmatism."],
   ["The lens becomes opaque", "That is cataract, which causes glare and blur rather than a pure "
                               "near problem."]],
  "two-step", D, 18),

Q("Idiopathic intracranial hypertension", IO,
  "A 26-year-old woman with idiopathic intracranial hypertension is started on treatment. Which "
  "measures are used?",
  [["Weight reduction and acetazolamide", "Correct, with serial visual field monitoring."],
   ["Topical antiglaucoma drops", "The pressure raised here is intracranial."],
   ["Intravitreal anti-VEGF", "That treats neovascular macular disease."],
   ["High-dose corticosteroids indefinitely",
    "Not the mainstay, and steroids can complicate the picture."],
   ["Antibiotics", "There is no infection."]],
  "treatment", D, 5),

Q("Chronic vision loss approach", IO,
  "A 70-year-old man reports gradual painless vision loss over two years. Which three diagnoses "
  "should be at the top of the differential?",
  [["Cataract, macular degeneration and open-angle glaucoma",
    "Correct — the three commonest causes of gradual painless loss in this age group."],
   ["Retinal detachment, optic neuritis and angle closure",
    "All three are ACUTE presentations."],
   ["Conjunctivitis, blepharitis and dry eye", "Surface conditions that do not cause progressive "
                                               "loss."],
   ["Amblyopia and strabismus", "Childhood conditions."],
   ["Retinoblastoma, uveal melanoma and iris nevus", "Tumours, and far less common than the "
                                                      "three leading causes."]],
  "two-step", D, 11),
]
