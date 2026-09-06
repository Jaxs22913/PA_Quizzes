# -*- coding: utf-8 -*-
"""Common Ophthalmological Disorders (Lecture 10) -- final pool.

Completes the bank to 325. Written from the audited chart rows, so every fact
traces to a cited slide.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "CMS I Common Ophthalmological Disorders"
IO = ("a — Common ophthalmological disorders: etiologies, epidemiology, risk factors, clinical "
      "manifestations, differential diagnosis, diagnostic testing, management, referrals, "
      "patient education, prognosis")

QUESTIONS = [

Q("Pre-septal cellulitis", IO,
  "A 5-year-old girl has mild pre-septal cellulitis. Which organisms does the antibiotic choice "
  "need to cover?",
  [["Staphylococcus, including resistant strains, and Streptococcus",
    "Correct — outpatient oral therapy for 10 to 14 days."],
   ["Pseudomonas and Acinetobacter", "Gram-negative organisms of a different setting entirely."],
   ["Chlamydia and Neisseria", "Those cause neonatal and adult conjunctivitis."],
   ["Aspergillus and Candida", "Fungi, not the organisms of periorbital cellulitis."],
   ["Adenovirus", "A virus, and antibiotics would not treat it."]],
  "treatment", D, 53),

Q("Pre-septal cellulitis", IO,
  "Which examination findings are described in pre-septal cellulitis?",
  [["Diffuse balloon-like oedema, erythema and tenderness of the lids",
    "Correct, with variable conjunctival injection, and periocular pain, fever, chills and warmth."],
   ["Proptosis with painful restricted movement", "Those are post-septal findings."],
   ["A discrete non-tender nodule", "That is a chalazion."],
   ["Crusting at the lash bases", "That is blepharitis."],
   ["A bright red painless patch", "That is a subconjunctival haemorrhage."]],
  "two-step", D, 52),

Q("Corneal ulcer", IO,
  "A 26-year-old man has a corneal ulcer. Which examination finding indicates significant "
  "intraocular inflammation?",
  [["A hypopyon", "Correct — layered white cells in the anterior chamber."],
   ["A hyphema", "That is layered BLOOD, and follows trauma."],
   ["Drusen", "Deposits at the macula in dry macular degeneration."],
   ["A cherry-red spot", "The central retinal artery occlusion finding."],
   ["Ciliary flush alone", "Indicates intraocular inflammation, but the hypopyon is the specific "
                           "finding named."]],
  "two-step", D, 61),

Q("Herpes zoster keratitis", IO,
  "A 70-year-old woman has herpes zoster ophthalmicus with keratitis. Which treatment is indicated "
  "if there is retinitis, choroiditis or optic neuritis?",
  [["Corticosteroids and intravenous acyclovir", "Correct."],
   ["Topical antibiotic drops alone", "The organism is viral."],
   ["Oral antihistamines", "No allergic mechanism."],
   ["Laser photocoagulation", "A retinal procedure for other indications."],
   ["Observation alone", "Posterior involvement requires treatment."]],
  "treatment", D, 59),

Q("Herpes simplex keratitis", IO,
  "What is the prognosis of herpes simplex keratitis?",
  [["Good — benign and self-limited, but recurrences are common", "Correct."],
   ["Uniformly poor with permanent scarring", "The prognosis is good, not uniformly poor."],
   ["It never recurs after the first episode", "Recurrences are common."],
   ["It always progresses to corneal perforation", "Not the described course."],
   ["It resolves without any treatment", "Antiviral treatment is given."]],
  "two-step", D, 59),

Q("Chemosis", IO,
  "Which conditions are named as causes of chemosis?",
  [["Allergy, infection, thyroid eye disease, angioedema and trauma",
    "Correct, along with orbital cellulitis and impaired orbital venous drainage."],
   ["Cataract and macular degeneration", "Causes of gradual painless vision loss."],
   ["Glaucoma and optic neuritis", "Neither produces conjunctival swelling."],
   ["Myopia and astigmatism", "Refractive errors."],
   ["Retinoblastoma and uveal melanoma", "Tumours that do not present with chemosis."]],
  "two-step", D, 31),

Q("Ectropion", IO,
  "Which causes of ectropion are named?",
  [["Ageing, scarring and congenital causes, plus seventh nerve palsy",
    "Correct — and seventh nerve palsy causes ectropion ONLY."],
   ["Contact lens wear", "Not a described cause."],
   ["Chronic steroid drops", "Associated with cataract and raised pressure."],
   ["Diabetes alone", "Not a described cause of lid malposition."],
   ["Sun and wind exposure", "Associated with pinguecula and pterygium."]],
  "two-step", D, 13),

Q("Dermatochalasis", IO,
  "What causes dermatochalasis?",
  [["Ageing", "Correct — excess flaps or folds of skin, bilaterally."],
   ["Chronic infection", "Not a described cause."],
   ["Allergy", "Produces lid oedema rather than excess skin."],
   ["Trauma", "Not the described cause."],
   ["Thyroid disease", "Causes lid retraction and proptosis rather than excess skin."]],
  "two-step", D, 14),

Q("Trachoma", IO,
  "Through which four stages does trachoma progress?",
  [["Follicles, tarsal scarring, entropion with trichiasis, then corneal opacity",
    "Correct."],
   ["Papillae, chemosis, hypopyon, then perforation", "Not the described sequence."],
   ["Drusen, pigment change, atrophy, then neovascularisation",
    "That is macular degeneration."],
   ["Flashes, floaters, curtain, then macular involvement", "That is retinal detachment."],
   ["Ptosis, miosis, anhidrosis, then dilation lag", "Those are Horner syndrome features."]],
  "two-step", D, 46),

Q("Keratitis", IO,
  "Which structure is inflamed in keratitis?",
  [["The cornea", "Correct."],
   ["The sclera", "That is scleritis."],
   ["The episcleral tissue", "That is episcleritis."],
   ["The iris", "That is iritis, or anterior uveitis."],
   ["The choroid", "That is choroiditis, or posterior uveitis."]],
  "diagnosis", D, 54),

Q("Uveitis", IO,
  "Which structures does ANTERIOR uveitis involve?",
  [["The iris, or the iris and ciliary body", "Correct — iritis, or iridocyclitis."],
   ["The choroid and retina", "That is posterior uveitis."],
   ["The cornea", "That is keratitis."],
   ["The sclera", "That is scleritis."],
   ["The conjunctiva", "That is conjunctivitis."]],
  "two-step", D, 62),

Q("Posterior uveitis", IO,
  "Which structures does POSTERIOR uveitis involve?",
  [["The choroid and/or the retina", "Correct — choroiditis and retinitis."],
   ["The iris alone", "That is iritis."],
   ["The iris and ciliary body", "That is iridocyclitis."],
   ["The episclera", "That is episcleritis."],
   ["The lacrimal gland", "That is dacryoadenitis."]],
  "two-step", D, 64),

Q("Episcleritis", IO,
  "Which tissue is inflamed in episcleritis?",
  [["The deep subconjunctival tissue", "Correct — the episcleral layer."],
   ["The sclera itself", "That is scleritis, which is deeper and far more painful."],
   ["The cornea", "That is keratitis."],
   ["The iris", "That is anterior uveitis."],
   ["The lid margin", "That is blepharitis."]],
  "two-step", D, 47),

Q("Xanthelasma", IO,
  "Which local treatments for xanthelasma are named?",
  [["Cryotherapy, laser ablation, chemical peel and surgical excision", "Correct."],
   ["Topical antibiotics", "There is no infection."],
   ["Intravitreal injection", "That treats retinal disease."],
   ["Warm compresses and massage", "That is chalazion management."],
   ["Lid hygiene", "That is blepharitis management."]],
  "treatment", D, 17),

Q("Hordeolum", IO,
  "Which glands are involved in an internal versus an external hordeolum?",
  [["Internal is the meibomian gland; external is the glands of Zeis or Moll",
    "Correct."],
   ["Internal is the lacrimal gland; external the meibomian", "The lacrimal gland is not involved."],
   ["Both involve the lacrimal sac", "That is dacryocystitis."],
   ["Both involve the conjunctival goblet cells", "Not the glands described."],
   ["Internal is the ciliary body; external the iris", "Those are uveal structures."]],
  "two-step", D, 20),

Q("Allergic conjunctivitis", IO,
  "A 19-year-old man's allergic conjunctivitis has not responded to topical treatment. What does "
  "that suggest?",
  [["The diagnosis may be wrong, so refer", "Correct — symptoms usually settle as allergen levels "
                                            "fall."],
   ["The dose should simply be doubled", "Failure prompts reconsideration of the diagnosis."],
   ["He needs oral antibiotics", "There is no bacterial infection."],
   ["He should stop all treatment", "That does not address the failure."],
   ["Surgery is indicated", "Allergic conjunctivitis is not surgical."]],
  "two-step", D, 35),

Q("Bacterial conjunctivitis", IO,
  "Which patients are named as at risk of bacterial conjunctivitis?",
  [["The immunocompromised, the elderly, children and contact lens wearers", "Correct."],
   ["Only contact lens wearers", "The list is broader."],
   ["Only newborns", "Neonatal disease is a separate category."],
   ["Only patients with allergies", "Allergy is a different diagnosis."],
   ["Only those with recent surgery", "Surgery is one risk among several."]],
  "two-step", D, 41),

Q("Dacryocystitis", IO,
  "What underlies dacryocystitis?",
  [["Nasolacrimal duct obstruction", "Correct."],
   ["Meibomian gland obstruction", "That produces a chalazion."],
   ["Lacrimal gland inflammation", "That is dacryoadenitis."],
   ["Trabecular meshwork obstruction", "That is glaucoma."],
   ["Corneal epithelial loss", "That is an abrasion."]],
  "two-step", D, 25),

Q("Entropion", IO,
  "What is the term for lashes turned in against the globe?",
  [["Trichiasis", "Correct — the consequence of entropion that threatens the cornea."],
   ["Chemosis", "Swelling of the conjunctiva."],
   ["Leukocoria", "A white pupil."],
   ["Proptosis", "Forward displacement of the globe."],
   ["Anisocoria", "Unequal pupil size."]],
  "two-step", D, 12),

Q("Red eye disposition", IO,
  "Which red eye presentations are seen the SAME DAY rather than immediately?",
  [["Keratitis or corneal ulcer, anterior uveitis, scleritis and ocular herpes zoster",
    "Correct — emergent means now; these four are same day."],
   ["Chemical injury, open globe and angle closure",
    "Those are EMERGENT and are seen immediately, not the same day."],
   ["Pinguecula and pterygium", "Routine surface degenerations."],
   ["Blepharitis and dry eye", "Routine chronic surface conditions."],
   ["Subconjunctival haemorrhage", "Routine, and it resolves in two to four weeks."]],
  "two-step", D, 66),
]
