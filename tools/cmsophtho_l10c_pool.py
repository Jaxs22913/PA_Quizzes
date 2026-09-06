# -*- coding: utf-8 -*-
"""Common Ophthalmological Disorders (Lecture 10) -- third pool.

Deliberately mixes SHORT stems with long ones. Three of the six exemplars are
three sentences, and a bank where every question is a full paragraph reads
nothing like the source.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "CMS I Common Ophthalmological Disorders"
IO = ("a — Common ophthalmological disorders: etiologies, epidemiology, risk factors, clinical "
      "manifestations, differential diagnosis, diagnostic testing, management, referrals, "
      "patient education, prognosis")

QUESTIONS = [

Q("Conjunctivitis differential", IO,
  "A 23-year-old woman has bilateral red, itchy eyes with stringy discharge. Examination shows "
  "conjunctival papillae and no preauricular node. Which feature most strongly indicates an "
  "allergic cause?",
  [["The itch", "Correct. Itch is the symptom that separates allergic disease from the rest."],
   ["The bilateral involvement", "Viral disease is often bilateral too."],
   ["The papillae", "Papillae occur in both bacterial and allergic disease."],
   ["The absence of a node", "Also true of bacterial conjunctivitis."],
   ["The discharge", "Discharge occurs in every form; its character matters more than its "
                     "presence."]],
  "two-step", D, 34),

Q("Conjunctivitis differential", IO,
  "On slit lamp examination a conjunctival elevation appears pale at its surface and redder at its "
  "base. Which two diagnoses does this favour?",
  [["Chlamydial and viral conjunctivitis", "Correct. That is a FOLLICLE."],
   ["Bacterial and allergic conjunctivitis", "Those produce PAPILLAE, which are red at the surface "
                                             "and paler at the base."],
   ["Episcleritis and scleritis", "Neither produces follicles or papillae."],
   ["Blepharitis and meibomitis", "Lid margin conditions."],
   ["Pinguecula and pterygium", "Degenerative surface growths."]],
  "two-step", D, 36),

Q("Conjunctivitis differential", IO,
  "A conjunctival elevation is red at the surface and paler at its base. Which two diagnoses does "
  "this favour?",
  [["Bacterial and allergic conjunctivitis", "Correct. That is a PAPILLA."],
   ["Chlamydial and viral conjunctivitis", "Those produce follicles, pale at the surface."],
   ["Trachoma and adult inclusion disease", "Both chlamydial, and therefore follicular."],
   ["Uveitis and scleritis", "Neither produces a conjunctival elevation of this kind."],
   ["Dacryoadenitis and dacryocystitis", "Lacrimal conditions."]],
  "two-step", D, 40),

Q("Hordeolum", IO,
  "A 27-year-old man with a hordeolum has developed spreading lid erythema and oedema with fever. "
  "How does this change management?",
  [["Treat on the cellulitis pathway with systemic antibiotics",
    "Correct — pre-septal cellulitis alongside a hordeolum is managed as cellulitis."],
   ["Continue warm compresses alone", "Insufficient once cellulitis has developed."],
   ["Incise and drain immediately", "The infection has spread beyond a drainable nodule."],
   ["Start topical antibiotics only", "Drops do not treat a soft tissue infection."],
   ["Refer for elective excision", "Not the acute management."]],
  "two-step", D, 21),

Q("Hordeolum", IO,
  "A 32-year-old woman has a hordeolum that has not improved after two weeks of warm compresses. "
  "What is the next step?",
  [["Refer to ophthalmology for incision and drainage",
    "Correct — persistence beyond two weeks is the stated threshold."],
   ["Continue compresses for a further two months", "Two weeks without improvement is the trigger "
                                                    "to escalate."],
   ["Start oral corticosteroids", "No role in an acute lid infection."],
   ["Perform curettage in clinic", "Curettage is the chalazion pathway, and by a specialist."],
   ["Reassure and take no action", "Persistent lesions are referred."]],
  "treatment", D, 21),

Q("Blepharitis", IO,
  "Which two skin conditions are associated with blepharitis?",
  [["Rosacea and seborrhoeic dermatitis", "Correct, alongside Staphylococcus aureus colonisation."],
   ["Psoriasis and lichen planus", "Not the associations named for this condition."],
   ["Atopic dermatitis and urticaria", "Atopy is associated with allergic conjunctivitis rather "
                                       "than lid margin disease."],
   ["Acne vulgaris and folliculitis", "Not the named associations."],
   ["Vitiligo and alopecia areata", "Autoimmune skin conditions unrelated to blepharitis."]],
  "two-step", D, 19),

Q("Dacryocystitis", IO,
  "A 64-year-old woman with dacryocystitis has improved on oral antibiotics. What is usually needed "
  "afterwards?",
  [["Probing and irrigation to check the drainage system",
    "Correct — the underlying nasolacrimal duct obstruction remains, and surgery may follow."],
   ["Nothing further once the infection clears",
    "The obstruction that caused it is still present."],
   ["Lifelong topical antibiotics", "Not the follow-on management."],
   ["Annual imaging", "Not the stated follow-up."],
   ["Immediate excision of the lacrimal sac", "Not the routine next step."]],
  "two-step", D, 25),

Q("Dacryocystitis", IO,
  "A 71-year-old man with dacryocystitis is febrile, unwell and lives alone with no support. What "
  "is the appropriate management?",
  [["Admit for intravenous antibiotics for 48 to 72 hours, then oral to complete 10 to 14 days",
    "Correct — fever, systemic illness or unreliability all move him to inpatient care."],
   ["Oral antibiotics for 10 days at home", "That pathway is for the well, afebrile, reliable "
                                            "patient."],
   ["Topical antibiotics alone", "Drops do not treat an infected sac."],
   ["Warm compresses and review in a week", "Insufficient for a febrile patient."],
   ["Immediate dacryocystorhinostomy", "Surgery follows once the infection is controlled."]],
  "treatment", D, 25),

Q("Chemosis", IO,
  "What is chemosis?",
  [["Swelling of the conjunctiva itself", "Correct — a sign rather than a diagnosis."],
   ["Blood underneath the conjunctiva", "That is a subconjunctival haemorrhage."],
   ["A yellowish nodule at the limbus", "That is a pinguecula."],
   ["Inflammation of the lid margin", "That is blepharitis."],
   ["A ring of vessels around the cornea", "That is ciliary flush."]],
  "diagnosis", D, 31),

Q("Ciliary flush", IO,
  "A 36-year-old man has a red eye with a ring of injected vessels radiating from the limbus around "
  "the cornea. What does this finding rule OUT?",
  [["Simple conjunctivitis", "Correct — ciliary flush indicates intraocular inflammation and moves "
                             "the diagnosis to keratitis, uveitis or glaucoma."],
   ["Anterior uveitis", "Ciliary flush is characteristic OF uveitis."],
   ["Acute angle-closure glaucoma", "Ciliary injection accompanies it."],
   ["Keratitis", "Ciliary flush occurs with corneal inflammation."],
   ["Corneal ulcer", "Also associated with ciliary injection."]],
  "two-step", D, 54),

Q("Slit lamp", IO,
  "Which structures does slit lamp examination assess?",
  [["The lids, cornea, conjunctiva, sclera and iris",
    "Correct — the anterior segment."],
   ["The retina and choroid", "Those require ophthalmoscopy."],
   ["The optic nerve head only", "Assessed by ophthalmoscopy."],
   ["The visual pathway posterior to the chiasm", "Assessed by field testing and imaging."],
   ["The extraocular muscles", "Assessed by observing eye movements."]],
  "two-step", D, 9),

Q("Fluorescein", IO,
  "A 29-year-old woman has a suspected corneal abrasion. How is fluorescein used?",
  [["Instilled in the eye and viewed under a blue light",
    "Correct — it pools in epithelial defects and reveals abrasions, ulcers and foreign bodies."],
   ["Injected intravenously and photographed", "That is fluorescein ANGIOGRAPHY, which images "
                                               "retinal and choroidal blood flow."],
   ["Taken orally an hour beforehand", "Fluorescein is not given by mouth for ocular staining."],
   ["Applied as an ointment overnight", "It is instilled as a drop or strip, not left in overnight."],
   ["Mixed with anaesthetic and swallowed", "Anaesthetic is instilled, and neither is swallowed."]],
  "two-step", D, 10),

Q("Fluorescein angiography", IO,
  "A 63-year-old man is having fluorescein angiography. How quickly does the dye reach the eye "
  "after injection, and what must be checked first?",
  [["Ten to fifteen seconds, and it contains no iodine",
    "Correct — the absence of iodine matters for patients who report contrast allergy."],
   ["Two minutes, and iodine allergy must be excluded",
    "The dye contains no iodine, and transit is far faster."],
   ["One hour, and renal function must be checked",
    "Transit is seconds, not an hour."],
   ["Thirty minutes, and thyroid function must be checked",
    "Neither the timing nor the check is right."],
   ["Immediately, and it requires general anaesthesia",
    "It is an outpatient procedure without anaesthesia."]],
  "two-step", D, 10),

Q("Post-septal cellulitis", IO,
  "A 12-year-old boy has orbital cellulitis. What is the usual source of the infection?",
  [["The paranasal sinuses", "Correct — which is why imaging covers the sinuses as well as the "
                             "orbits."],
   ["The lacrimal sac", "A cause of localised infection rather than the usual orbital source."],
   ["A corneal ulcer", "A surface infection that does not typically spread to the orbit."],
   ["The conjunctiva", "Surface infection does not usually breach the septum."],
   ["Haematogenous spread from a distant site", "Possible but not the usual source."]],
  "two-step", D, 52),

Q("Uveitis", IO,
  "A 44-year-old woman has anterior uveitis. Which finding on slit lamp examination defines it?",
  [["Cells in the anterior chamber", "Correct — inflammatory cells in the aqueous."],
   ["An epithelial defect that stains", "That is an abrasion or ulcer."],
   ["A dendritic lesion", "That is herpes simplex keratitis."],
   ["Follicles in the fornix", "That is follicular conjunctivitis."],
   ["A hazy oedematous cornea", "That suggests raised pressure."]],
  "two-step", D, 62),

Q("Posterior uveitis", IO,
  "A 38-year-old man with posterior uveitis is being investigated for an infectious cause. Which "
  "organism causes chorioretinitis?",
  [["Toxoplasma gondii", "Correct — a classic infectious cause of posterior uveitis."],
   ["Staphylococcus aureus", "Associated with blepharitis and lid infection."],
   ["Adenovirus", "Causes conjunctivitis."],
   ["Chlamydia trachomatis", "Causes follicular conjunctivitis and trachoma."],
   ["Pseudomonas aeruginosa", "Causes contact-lens-related corneal ulcer."]],
  "two-step", D, 65),

Q("Ophthalmoscopy", IO,
  "Which form of ophthalmoscopy is described as the most commonly used?",
  [["Slit-lamp ophthalmoscopy", "Correct — alongside direct and indirect methods."],
   ["Direct ophthalmoscopy", "Used, but not the one named as most common."],
   ["Indirect ophthalmoscopy", "Used, particularly for the periphery, but not the one named."],
   ["Fluorescein angiography", "An imaging study rather than ophthalmoscopy."],
   ["Optical coherence tomography", "A scanning modality rather than ophthalmoscopy."]],
  "two-step", D, 9),

Q("Referral urgency", IO,
  "Which of these ophthalmological presentations is EMERGENT?",
  [["Gonococcal conjunctivitis in a newborn", "Correct — untreated it risks corneal perforation."],
   ["Pinguecula with mild irritation", "Routine &mdash; sun protection and lubricants."],
   ["Dermatochalasis with heaviness", "Routine, and surgery is elective."],
   ["Xanthelasma", "Routine, and the workup is metabolic."],
   ["A resolving subconjunctival haemorrhage", "Routine, and it settles in two to four weeks."]],
  "two-step", D, 66),

Q("Referral urgency", IO,
  "A 45-year-old contact lens wearer has bacterial conjunctivitis that has not improved in 24 "
  "hours. What is the appropriate disposition?",
  [["Urgent referral", "Correct — lens wear plus failure to improve in 24 hours both make it "
                       "urgent."],
   ["Routine review in two weeks", "The combination described is urgent."],
   ["Discharge with reassurance", "Failure to respond needs assessment."],
   ["Switch to oral antibiotics and review in a month", "Delay is unsafe in a lens wearer."],
   ["Stop all treatment and observe", "Leaves a non-responding infection untreated."]],
  "two-step", D, 41),
]
