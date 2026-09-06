# -*- coding: utf-8 -*-
"""Common Ophthalmological Disorders (Lecture 10) -- Updated ophthalmology masters.

Grounded in the deck and in the audited chart rows. Style per
_cmsophtho_style.py, taken from Jaxon's six exemplars.

NOTE ON DACRYOSTENOSIS. One exemplar used it as a distractor and it is on no
slide in this deck, which teaches dacryoadenitis and dacryocystitis only. It is
used here ONLY as a distractor -- never as a key -- and its refutation defines
it, so the question still teaches rather than assuming knowledge we never gave.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "CMS I Common Ophthalmological Disorders"
IO = ("a — Common ophthalmological disorders: etiologies, epidemiology, risk factors, clinical "
      "manifestations, differential diagnosis, diagnostic testing, management, referrals, "
      "patient education, prognosis")

QUESTIONS = [

# ---------------------------------------------------------------- eyelid
Q("Chalazion", IO,
  "An 18-year-old woman has had a swelling of her left upper eyelid for 10 days. For the first "
  "day or two it was red and mildly painful; it is now painless but has grown. There has been no "
  "drainage, no change in vision and no itching. She has been well otherwise. Vital signs are "
  "normal, extraocular movements are intact and the pupils are equal and reactive. The left upper "
  "lid carries a 1.5 cm round, non-tender, mildly erythematous mass with no drainage. The "
  "underside of the lid is greyish-red. What is the most likely diagnosis?",
  [["Chalazion", "Correct. A sterile obstruction of a meibomian gland: it builds over days to "
                 "weeks and the mature lesion is NON-tender, which is what the painless second "
                 "week tells you."],
   ["Hordeolum", "An acute staphylococcal infection of a lid gland. It appears within about 24 "
                 "hours and stays TENDER, where this became painless as it grew."],
   ["Blepharitis", "Inflammation of the lid MARGIN with crusting at the lash bases and a frothy "
                   "tear film, not a discrete 1.5 cm nodule."],
   ["Dacryocystitis", "Infection of the lacrimal sac, which swells the NASAL aspect of the LOWER "
                      "lid below the medial canthal tendon and expresses pus from the punctum."],
   ["Dacryoadenitis", "Inflammation of the lacrimal gland, which swells the LATERAL third of the "
                      "UPPER lid with a preauricular node."]],
  "diagnosis", D, 20),

Q("Hordeolum", IO,
  "A 24-year-old man woke with a painful lump at the margin of his right lower lid. It was not "
  "there yesterday. Examination shows a tender subcutaneous nodule at the lid margin with "
  "surrounding erythema. Vision and pupils are normal. What is the most likely diagnosis?",
  [["Hordeolum", "Correct. Acute, usually staphylococcal, and the two features that separate it "
                 "from a chalazion are that it is TENDER and that it appeared within 24 hours."],
   ["Chalazion", "Builds over days to weeks and the mature lesion is non-tender."],
   ["Dermatochalasis", "Painless excess lid skin from ageing, not an acute tender nodule."],
   ["Xanthelasma", "Painless yellowish plaques, typically bilateral and asymptomatic."],
   ["Pre-septal cellulitis", "Diffuse lid swelling and erythema rather than a discrete nodule at "
                             "the margin."]],
  "diagnosis", D, 20),

Q("Chalazion", IO,
  "A 31-year-old woman has had a painless, firm nodule in her upper lid for six weeks. Warm "
  "compresses and lid massage for a month have not reduced it. Vision is unaffected. What is the "
  "most appropriate next step?",
  [["Refer to ophthalmology for steroid injection or curettage",
    "Correct. Conservative measures come first; a lesion that has not resolved goes on for "
    "intralesional steroid or curettage."],
   ["Continue warm compresses for a further six months",
    "Improvement can take months, but a lesion persisting beyond two to three months warrants "
    "referral rather than more of the same."],
   ["Start oral antibiotics", "A chalazion is a STERILE gland obstruction, so antibiotics do not "
                              "address it."],
   ["Incise and drain it in clinic", "Incision and drainage is the hordeolum pathway; a chalazion "
                                     "is curetted or injected by ophthalmology."],
   ["Excise the whole lid lesion under general anaesthetic",
    "Disproportionate to a lesion managed with injection or curettage."]],
  "treatment", D, 21),

Q("Chalazion", IO,
  "A 62-year-old man has had a lid nodule that has recurred three times in the same spot over "
  "eight months, each time treated as a chalazion. Why does the recurrence itself change the plan?",
  [["It raises the possibility of sebaceous carcinoma",
    "Correct. Recurrent lesions, or one persisting beyond two to three months, are referred to "
    "rule this out."],
   ["It indicates the gland is permanently blocked",
    "A blocked gland explains the lesion but not why recurrence warrants referral."],
   ["It means the original diagnosis was a hordeolum",
    "A hordeolum is acute and tender; recurrence in one site is the concerning pattern regardless."],
   ["It suggests underlying blepharitis alone",
    "Blepharitis predisposes to lid lesions, but it is not why recurrence prompts referral."],
   ["It indicates an allergic cause", "Allergy does not produce a recurrent discrete nodule."]],
  "two-step", D, 21),

Q("Entropion", IO,
  "A 78-year-old woman complains of a constant foreign body sensation in the right eye. "
  "Examination shows the lower lid margin turned inward, with the lashes resting against the "
  "globe, and conjunctival injection. What is the most likely diagnosis?",
  [["Entropion", "Correct. The lid margin turns IN and the lashes touch the globe, producing the "
                 "foreign body sensation."],
   ["Ectropion", "The lid margin turns OUT, exposing the inner surface and producing TEARING "
                 "rather than a foreign body sensation."],
   ["Dermatochalasis", "Excess folds of lid skin, which produces heaviness rather than lashes "
                       "against the cornea."],
   ["Blepharitis", "Inflamed lid margins with crusting at the lash bases, without inward rotation."],
   ["Trichiasis alone", "Misdirected lashes can occur without the lid itself rotating; here the "
                        "lid margin is turned in."]],
  "diagnosis", D, 12),

Q("Entropion", IO,
  "A 74-year-old man with entropion has been using preservative-free artificial tears by day and "
  "lubricating ointment at night, with the lid taped. He asks whether this will fix the problem. "
  "What should he be told?",
  [["Only surgery repositions the lid",
    "Correct. The drops and taping protect the ocular surface; surgery is definitive."],
   ["The drops will gradually correct the lid position",
    "Lubrication protects the cornea but does nothing to the lid's position."],
   ["Taping alone is curative if continued for six months",
    "Taping is a temporising measure, not a cure."],
   ["Antibiotic drops will resolve it", "There is no infection to treat."],
   ["It resolves spontaneously with age", "Age-related lid laxity progresses rather than resolves."]],
  "treatment", D, 13),

Q("Ectropion", IO,
  "A 71-year-old woman has watering of the left eye and a red, exposed inner lid surface. "
  "Examination shows the lower lid margin turned outward. She had a facial nerve palsy last year "
  "with incomplete recovery. What is the most likely explanation?",
  [["Seventh nerve palsy causing ectropion",
    "Correct. Of the two malpositions, a seventh nerve palsy causes ectropion only."],
   ["Seventh nerve palsy causing entropion",
    "A seventh nerve palsy does not cause inward rotation."],
   ["Age-related entropion", "The lid here is turned outward, not inward."],
   ["Dermatochalasis", "Excess skin does not evert the lid margin."],
   ["Cicatricial change from prior infection",
    "Scarring can cause either malposition, but the recent facial palsy is the stated cause here."]],
  "diagnosis", D, 13),

Q("Dermatochalasis", IO,
  "A 68-year-old man reports heaviness of both upper lids and says he is 'looking through my "
  "lashes'. Examination shows excess folds of upper lid skin bilaterally with no inflammation. "
  "What examination finding most determines whether surgery will be covered?",
  [["A demonstrated visual field defect",
    "Correct. Blepharoplasty is often covered if a field defect is present."],
   ["The measured thickness of the skin fold", "Not the criterion used."],
   ["Corneal staining with fluorescein", "That assesses surface damage, not the field."],
   ["Intraocular pressure", "Pressure is unrelated to lid skin excess."],
   ["Tear film break-up time", "That measures dry eye rather than field loss."]],
  "two-step", D, 15),

Q("Xanthelasma", IO,
  "A 54-year-old woman has painless, oval yellowish plaques on both upper lids near the inner "
  "canthus. Vision is normal. What is the most appropriate initial workup?",
  [["Serum lipid profile, fasting glucose, HbA1c and liver function tests",
    "Correct. The local lesion is a marker; the underlying metabolic issue is what is treated."],
   ["Slit lamp examination alone", "It confirms the appearance but misses the systemic point."],
   ["Biopsy of the lesion", "The diagnosis is clinical."],
   ["Computed tomography of the orbits", "Imaging has no role in this diagnosis."],
   ["Thyroid function tests alone", "Not the panel named for this lesion."]],
  "treatment", D, 17),

Q("Xanthelasma", IO,
  "A 58-year-old man has had xanthelasma removed by laser ablation and asks about the outlook. "
  "What should he be told?",
  [["Recurrence is common even after effective local treatment",
    "Correct — which is why the underlying metabolic issue matters more than the local removal."],
   ["Removal is permanent in almost all patients", "Recurrence is common."],
   ["The lesions will become malignant if untreated", "They are benign."],
   ["His vision will deteriorate if they return", "They are asymptomatic and do not affect vision."],
   ["They only recur if lipids are normal", "Many patients have normal lipids, and recurrence is "
                                            "not conditional on that."]],
  "two-step", D, 17),

Q("Blepharitis", IO,
  "A 52-year-old patient has a burning sensation in both eyes. There has been no trauma and no "
  "contact with anyone with similar symptoms. Examination shows red, inflamed lid margins with "
  "greasy, matted lashes and dandruff-like debris at their bases. The conjunctivae are clear and "
  "there is no corneal involvement. Colonisation with which organism is found in a significant "
  "fraction of patients with this condition?",
  [["Staphylococcus aureus", "Correct. Blepharitis is associated with S. aureus, and with rosacea "
                             "and seborrhoeic dermatitis."],
   ["Chlamydia trachomatis", "Causes adult inclusion conjunctivitis and trachoma, with follicles "
                             "and a preauricular node rather than lid-margin scurf."],
   ["Haemophilus influenzae", "A cause of bacterial conjunctivitis rather than chronic lid margin "
                              "disease."],
   ["Moraxella catarrhalis", "A respiratory and middle ear organism, not the one associated here."],
   ["Pseudomonas aeruginosa", "The organism of contact-lens-related corneal ulcer, not "
                              "blepharitis."]],
  "two-step", D, 19),

Q("Blepharitis", IO,
  "A 47-year-old woman with red, crusted lid margins and a frothy tear film has used lid hygiene "
  "twice daily for two weeks with no improvement. What is the next step?",
  [["Add a topical antibiotic", "Correct. Lid hygiene first; no better after two weeks, escalate "
                                "to topical, then oral antibiotics."],
   ["Continue lid hygiene alone for three months",
    "Two weeks without improvement is the stated point to escalate."],
   ["Start oral antibiotics immediately", "Topical comes before oral in the sequence."],
   ["Refer for lid surgery", "Blepharitis is managed medically."],
   ["Start topical corticosteroid alone", "Not the named escalation for this condition."]],
  "treatment", D, 19),

Q("Blepharitis", IO,
  "A 60-year-old man with chronic blepharitis asks whether treatment will cure it. What should he "
  "be told?",
  [["It is chronic and controlled rather than cured",
    "Correct. Refer to ophthalmology if several weeks of treatment fail."],
   ["A two-week antibiotic course is curative", "The condition recurs."],
   ["It resolves once the associated rosacea is treated",
    "Treating rosacea helps, but the lid disease remains chronic."],
   ["Surgery is definitive", "Blepharitis is not a surgical condition."],
   ["It resolves spontaneously within a month", "It is a long-term condition."]],
  "two-step", D, 19),

# ---------------------------------------------------------------- lacrimal
Q("Dacryoadenitis", IO,
  "A 33-year-old woman has three days of pain, redness and swelling over the OUTER third of her "
  "right upper lid, with tearing. There is a tender preauricular node on the same side. "
  "Temperature 38.1°C. What is the most likely diagnosis?",
  [["Dacryoadenitis", "Correct. Inflammation of the lacrimal gland, which sits under the LATERAL "
                      "third of the UPPER lid."],
   ["Dacryocystitis", "Involves the lacrimal SAC at the NASAL aspect of the LOWER lid, below the "
                      "medial canthal tendon."],
   ["Hordeolum", "A discrete tender nodule at the lid margin, without a preauricular node or fever."],
   ["Pre-septal cellulitis", "Diffuse lid swelling rather than localisation to the outer third."],
   ["Chalazion", "Painless and non-tender by the time it is established."]],
  "diagnosis", D, 22),

Q("Dacryocystitis", IO,
  "A 57-year-old man has a red, painful swelling over the inner corner of his left lower lid. "
  "Pressure over the swelling expresses pus from the lower punctum. He is afebrile and systemically "
  "well. What is the most appropriate management?",
  [["Oral antibiotics for 10 days", "Correct. A well, afebrile, reliable patient is managed as an "
                                    "outpatient on orals."],
   ["Admit for intravenous antibiotics",
    "Reserved for the febrile, unwell or unreliable patient."],
   ["Topical antibiotic drops alone", "Drops do not treat an infected lacrimal sac."],
   ["Immediate surgical excision of the sac",
    "Drainage of an abscess may be needed, but excision is not the initial management."],
   ["Observation with warm compresses only",
    "Compresses are adjunctive; this is a bacterial infection requiring antibiotics."]],
  "treatment", D, 25),

Q("Dacryocystitis", IO,
  "A 61-year-old woman is being treated for dacryocystitis. A mass is noted ABOVE the medial "
  "canthal tendon rather than below it. What does that suggest?",
  [["A lacrimal sac tumour", "Correct. A mass above the tendon rather than below it raises that "
                             "possibility."],
   ["Simple nasolacrimal duct obstruction", "That produces the usual swelling below the tendon."],
   ["Dacryoadenitis", "That involves the gland under the lateral upper lid."],
   ["Pre-septal cellulitis", "Diffuse rather than a discrete mass in that location."],
   ["A chalazion of the upper lid", "Occurs in the tarsal plate, not at the medial canthus."]],
  "two-step", D, 25),

# ---------------------------------------------------------------- surface
Q("Pterygium", IO,
  "A 44-year-old fisherman has a fleshy triangular growth extending from the nasal conjunctiva "
  "ONTO the cornea of his right eye. Vision in that eye has dropped slightly. What is the most "
  "likely diagnosis?",
  [["Pterygium", "Correct. The growth crosses the limbus onto the cornea, which is the whole "
                 "distinction from a pinguecula."],
   ["Pinguecula", "A yellowish nodule at 3 or 9 o'clock that does NOT touch the cornea."],
   ["Conjunctival intraepithelial neoplasia",
    "A fan-shaped lesion that can look similar, but is not the sun-and-wind lesion described."],
   ["Chemosis", "Swelling of the conjunctiva itself, not a discrete fleshy growth."],
   ["Subconjunctival haemorrhage", "A flat bright red patch of blood, not a raised growth."]],
  "diagnosis", D, 28),

Q("Pinguecula", IO,
  "A 39-year-old landscaper has a yellowish raised nodule on the nasal conjunctiva at the 3 "
  "o'clock position of the left eye. It does not reach the cornea. He asks whether treatment will "
  "make it go away. What should he be told?",
  [["Conservative management controls symptoms but will not make it resolve",
    "Correct. Sun, dust and wind protection with lubricating drops."],
   ["Lubricating drops will dissolve it over months", "They relieve irritation only."],
   ["It will resolve once sun exposure stops", "Avoiding exposure prevents progression, not the "
                                               "existing lesion."],
   ["Surgery is required in all cases", "Surgery is for a pterygium growing onto the cornea."],
   ["It will become malignant if untreated", "It is benign."]],
  "two-step", D, 28),

Q("Subconjunctival haemorrhage", IO,
  "A 66-year-old man noticed a bright red patch on the white of his right eye this morning after "
  "a bout of coughing. There is no pain, vision is normal, the pupil is reactive and the cornea is "
  "clear. What is the most appropriate next step?",
  [["Check the blood pressure", "Correct. With no explanation for the bleed, blood pressure is "
                                "checked; otherwise the history is the workup."],
   ["Urgent ophthalmology referral", "It resolves spontaneously in two to four weeks."],
   ["Start topical antibiotics", "There is no infection."],
   ["Computed tomography of the orbits", "Imaging has no role in a painless bleed with normal "
                                         "vision."],
   ["Immediate haematology referral", "Recurrence without a culprit medication prompts a targeted "
                                      "evaluation, not an automatic referral."]],
  "treatment", D, 30),

Q("Chemosis", IO,
  "A 29-year-old woman has swelling of the conjunctiva of the left eye. Which accompanying finding "
  "would make this urgent?",
  [["Proptosis with restricted eye movements",
    "Correct. Chemosis with proptosis, restricted movement, reduced vision or an afferent "
    "pupillary defect means something is filling the orbit."],
   ["Mild itching of both eyes", "That suggests allergy, which is a common benign cause."],
   ["A history of hay fever", "Allergy is one of the ordinary causes of chemosis."],
   ["Recent minor eye rubbing", "Local irritation is a benign cause."],
   ["Clear discharge from the same eye", "Consistent with allergic or viral irritation."]],
  "two-step", D, 31),

# ---------------------------------------------------------------- conjunctivitis
Q("Allergic conjunctivitis", IO,
  "A 21-year-old man has itchy, watery, red eyes every spring. Both eyes are affected. Examination "
  "shows diffuse injection, chemosis and conjunctival papillae, with no preauricular node. Vision "
  "is normal. What is the most appropriate initial treatment?",
  [["A topical antihistamine with a mast cell stabiliser",
    "Correct — olopatadine does both. With allergen avoidance, cool compresses and artificial "
    "tears."],
   ["Topical antibiotic drops", "There is no bacterial infection."],
   ["Topical corticosteroids as first line",
    "Not the initial agent for uncomplicated allergic disease."],
   ["Oral acyclovir", "Reserved for herpetic disease."],
   ["Artificial tears alone", "Helpful, but the antihistamine is the specific treatment."]],
  "treatment", D, 35),

Q("Viral conjunctivitis", IO,
  "A 26-year-old woman has a red, watering right eye that began three days after a head cold. The "
  "left eye became involved yesterday. There is no pain. Examination shows diffuse injection with "
  "follicles inferiorly, considerable tearing, and a TENDER preauricular node. What is the most "
  "likely diagnosis?",
  [["Viral conjunctivitis", "Correct. Watery discharge, follicles, a tender preauricular node, and "
                            "one eye then the other after a cold."],
   ["Bacterial conjunctivitis", "Thick discharge, usually unilateral, and typically without a node."],
   ["Allergic conjunctivitis", "Itch dominates, it is bilateral from the start, and there is no "
                               "node."],
   ["Adult inclusion conjunctivitis", "Chlamydial disease is more indolent and follows a sexual "
                                      "health history."],
   ["Episcleritis", "Sectoral redness without discharge or a node."]],
  "diagnosis", D, 37),

Q("Viral conjunctivitis", IO,
  "A 30-year-old man with viral conjunctivitis says his eye looked worse on day five than on day "
  "two and asks whether the treatment has failed. What should he be told?",
  [["It often worsens over the first week before resolving in two to three weeks",
    "Correct, and it is highly contagious throughout."],
   ["Worsening means a bacterial superinfection has developed",
    "Deterioration in the first week is the expected course."],
   ["It should have resolved within 48 hours", "The illness runs two to three weeks."],
   ["He needs topical antibiotics now", "Antibiotics do not treat a viral conjunctivitis."],
   ["He should stop the artificial tears", "Tears are supportive and can continue."]],
  "two-step", D, 37),

Q("Bacterial conjunctivitis", IO,
  "A 34-year-old contact lens wearer has a red right eye with thick yellow discharge and lids stuck "
  "together on waking. There is no preauricular node. What makes this presentation urgent rather "
  "than routine?",
  [["Contact lens wear", "Correct. Contact lens wear, immunocompromise, recent surgery, a foreign "
                         "body, corneal opacity or no improvement in 24 hours all make it urgent."],
   ["The thick discharge", "Purulent discharge is the usual finding in bacterial disease."],
   ["The lids being stuck together", "A common and non-specific feature."],
   ["The absence of a preauricular node", "Expected in ordinary bacterial conjunctivitis."],
   ["The unilateral involvement", "Bacterial disease is often unilateral."]],
  "two-step", D, 41),

Q("Gonococcal conjunctivitis", IO,
  "A 3-day-old neonate has marked bilateral lid oedema and copious purulent discharge. A palpable "
  "preauricular node is present. What is the most appropriate management?",
  [["Hospitalise and give a single dose of systemic ceftriaxone",
    "Correct, with specialty consultation — the untreated risk is corneal perforation."],
   ["Topical antibiotic drops as an outpatient", "Insufficient for gonococcal disease in a "
                                                 "newborn."],
   ["Oral erythromycin at home", "Systemic ceftriaxone in hospital is what is specified."],
   ["Observation with lid hygiene", "This is a sight-threatening emergency."],
   ["Topical acyclovir", "The organism is bacterial."]],
  "treatment", D, 41),

Q("Gonococcal conjunctivitis", IO,
  "A 23-year-old man has severe purulent conjunctivitis with a palpable preauricular node. Why is "
  "the node significant here?",
  [["It is the exception to the rule that bacterial conjunctivitis lacks a node",
    "Correct. Severe purulent discharge WITH a node points to gonococcal disease."],
   ["It confirms a viral cause", "A node is typical of viral disease, but the discharge here is "
                                 "severely purulent."],
   ["It indicates allergic disease", "Allergic conjunctivitis has no node."],
   ["It indicates orbital cellulitis", "That presents with proptosis and painful restricted "
                                       "movement."],
   ["It is an incidental finding of no significance",
    "It is the finding that changes the diagnosis."]],
  "two-step", D, 41),

Q("Trachoma", IO,
  "A 35-year-old woman who grew up in a region with poor sanitation has scarring of the tarsal "
  "conjunctiva with lashes turned inward and a corneal opacity. What organism is responsible?",
  [["Chlamydia trachomatis", "Correct. Trachoma progresses through follicles, tarsal scarring, "
                             "entropion with trichiasis, and corneal opacity."],
   ["Neisseria gonorrhoeae", "Causes hyperacute purulent conjunctivitis, not chronic scarring."],
   ["Staphylococcus aureus", "Associated with blepharitis rather than cicatricial disease."],
   ["Adenovirus", "Causes acute follicular conjunctivitis that resolves."],
   ["Pseudomonas aeruginosa", "Associated with contact-lens corneal ulcer."]],
  "two-step", D, 45),

# ---------------------------------------------------------------- sclera
Q("Episcleritis", IO,
  "A 28-year-old woman has a sectoral area of redness in the right eye with mild discomfort but no "
  "pain and no visual change. Phenylephrine drops blanch the injected vessels. What is the most "
  "likely diagnosis?",
  [["Episcleritis", "Correct. Superficial, mildly uncomfortable, and the vessels blanch with "
                    "phenylephrine."],
   ["Scleritis", "Deep boring pain that wakes the patient, with vessels that do NOT blanch."],
   ["Bacterial conjunctivitis", "Diffuse redness with purulent discharge, not a sector."],
   ["Anterior uveitis", "Limbal injection with photophobia and cells in the anterior chamber."],
   ["Subconjunctival haemorrhage", "A flat patch of blood rather than injected vessels."]],
  "diagnosis", D, 47),

Q("Scleritis", IO,
  "A 55-year-old woman with rheumatoid arthritis has severe, boring right eye pain that wakes her "
  "at night, with a violaceous hue to the sclera. Phenylephrine does not blanch the vessels. Which "
  "form carries the greatest risk of perforation?",
  [["Necrotising scleritis", "Correct. Perforation risk is greatest in the necrotising form rather "
                             "than uniformly across scleritis."],
   ["Diffuse anterior scleritis", "Inflammatory but not the form with the greatest perforation "
                                  "risk."],
   ["Nodular anterior scleritis", "Carries a nodule but not the highest perforation risk."],
   ["Posterior scleritis", "Presents with pain and vision loss but is not the form named for "
                           "perforation."],
   ["Episcleritis", "A superficial and self-limiting condition that does not perforate."]],
  "two-step", D, 49),

# ---------------------------------------------------------------- orbit
Q("Pre-septal cellulitis", IO,
  "A 6-year-old boy has a swollen, red right upper and lower lid after a scratch three days ago. "
  "The globe is WHITE, eye movements are full and painless, vision is 6/6 and the pupils are equal. "
  "Temperature 37.8°C. What is the most likely diagnosis?",
  [["Pre-septal cellulitis", "Correct. A white eye with full painless movements and normal vision "
                             "is the single most useful discrimination in this block."],
   ["Post-septal (orbital) cellulitis", "The globe would be red with proptosis, painful restricted "
                                        "movement, and possibly an afferent pupillary defect."],
   ["Dacryocystitis", "Localises to the lacrimal sac below the medial canthal tendon."],
   ["Allergic lid oedema", "Painless, usually bilateral and itchy, without fever."],
   ["Hordeolum", "A discrete tender nodule at the lid margin rather than diffuse lid swelling."]],
  "diagnosis", D, 52),

Q("Post-septal cellulitis", IO,
  "A 9-year-old girl has a swollen red eyelid, proptosis, pain on eye movement and diplopia. "
  "Temperature 39.0°C. What is the most appropriate next step?",
  [["Admit for intravenous antibiotics and computed tomography of the orbits and sinuses",
    "Correct. All post-septal disease is admitted, and imaging defines the extent."],
   ["Discharge on oral antibiotics with review in 48 hours",
    "Outpatient oral therapy is for mild pre-septal disease only."],
   ["Topical antibiotic drops", "Drops do not treat an orbital infection."],
   ["Warm compresses and observation", "This is a sight- and life-threatening infection."],
   ["Refer to the allergy clinic", "The fever and proptosis indicate infection."]],
  "treatment", D, 53),

Q("Post-septal cellulitis", IO,
  "An 11-year-old boy with orbital cellulitis is not improving after 48 hours of intravenous "
  "antibiotics. Which complication is of greatest concern?",
  [["Cavernous sinus thrombosis", "Correct. Intracranial spread gives meningitis or cavernous "
                                  "sinus thrombosis."],
   ["Chronic dry eye", "Not the complication that drives urgency."],
   ["Recurrent chalazion", "Unrelated to orbital infection."],
   ["Refractive change", "Not a described complication."],
   ["Pinguecula formation", "A degenerative surface lesion, unrelated."]],
  "two-step", D, 53),

# ---------------------------------------------------------------- cornea
Q("Herpes simplex keratitis", IO,
  "A 37-year-old man has a painful, watering red left eye with blurred vision. Fluorescein staining "
  "shows a branching epithelial lesion with raised edges and small bulbs at the ends of each branch. "
  "What is the most likely diagnosis?",
  [["Herpes simplex keratitis", "Correct. The true dendrite branches, has elevated edges and "
                                "terminal end bulbs — pathognomonic."],
   ["Herpes zoster keratitis", "A pseudodendrite, which lacks the terminal end bulbs and the "
                               "elevated edges."],
   ["Bacterial corneal ulcer", "A round white infiltrate with an epithelial defect, not a branching "
                               "lesion."],
   ["Corneal abrasion", "A simple epithelial defect without branching."],
   ["Anterior uveitis", "Cells in the anterior chamber without a corneal epithelial lesion."]],
  "diagnosis", D, 57),

Q("Herpes zoster keratitis", IO,
  "A 68-year-old woman has a vesicular rash over her right forehead and the tip of her nose, with "
  "a red painful eye. Which cranial nerve division is involved?",
  [["The ophthalmic division of the trigeminal nerve",
    "Correct — V1 of cranial nerve V. Involvement of the nose tip signals ocular involvement."],
   ["The facial nerve", "Cranial nerve VII supplies facial movement and is the Ramsay Hunt nerve, "
                        "not this one."],
   ["The maxillary division of the trigeminal nerve",
    "V2 supplies the mid-face rather than the forehead and nose tip."],
   ["The oculomotor nerve", "Cranial nerve III moves the eye and constricts the pupil."],
   ["The optic nerve", "Cranial nerve II carries vision, not cutaneous sensation."]],
  "two-step", D, 57),

Q("Corneal ulcer", IO,
  "A 22-year-old woman who sleeps in her contact lenses has a painful red right eye with a white "
  "spot on the cornea and an overlying epithelial defect that stains with fluorescein. Which "
  "organism is of greatest concern?",
  [["Pseudomonas aeruginosa", "Correct. The contact lens association makes this the organism to "
                              "fear, and it can perforate rapidly."],
   ["Staphylococcus aureus", "A cause of blepharitis and lid infection rather than the lens-related "
                             "ulcer organism."],
   ["Chlamydia trachomatis", "Causes follicular conjunctivitis and trachoma."],
   ["Adenovirus", "Causes viral conjunctivitis rather than a suppurative ulcer."],
   ["Moraxella catarrhalis", "Not the organism associated with contact-lens-related ulcer."]],
  "two-step", D, 60),

# ---------------------------------------------------------------- uvea
Q("Anterior uveitis", IO,
  "A 29-year-old patient has two days of painful red eyes and blurred vision. The pain is a deep "
  "ache with sensitivity to light (photophobia). There is no discharge and no recent trauma. The "
  "medical history includes ankylosing spondylitis. Examination shows conjunctival injection "
  "primarily around the limbus, a sluggish pupillary response, and cells in the anterior chamber on "
  "slit-lamp examination. What is the most appropriate initial treatment?",
  [["Topical corticosteroids", "Correct, with a cycloplegic for comfort and to prevent synechiae."],
   ["Artificial tears", "Supportive only, and they do nothing for intraocular inflammation."],
   ["Topical antibiotics", "There is no bacterial infection; the discharge is absent."],
   ["Topical antihistamines", "Allergic disease itches and does not produce anterior chamber "
                              "cells."],
   ["Oral acyclovir", "Reserved for herpetic disease, which is not indicated here."]],
  "treatment", D, 63),

Q("Anterior uveitis", IO,
  "A 34-year-old man with recurrent anterior uveitis is being investigated. His back pain improves "
  "with exercise and worsens with rest. Which association is most likely?",
  [["An HLA-B27-related spondyloarthropathy",
    "Correct — the ankylosing spondylitis association, which is why the systemic history matters."],
   ["Contact lens overwear", "That association is with corneal ulcer."],
   ["Chronic sun and wind exposure", "That is the pinguecula and pterygium association."],
   ["Seborrhoeic dermatitis", "That is associated with blepharitis."],
   ["Hypertension", "Not the association for recurrent anterior uveitis."]],
  "two-step", D, 62),

Q("Posterior uveitis", IO,
  "A 41-year-old woman has floaters and progressive blurring of vision in one eye over two weeks, "
  "with no pain and no redness. Fundus examination shows a focal white chorioretinal lesion with "
  "overlying vitreous haze. What is the most likely diagnosis?",
  [["Posterior uveitis", "Correct. Choroiditis or retinitis presents with floaters and blurring "
                         "rather than the pain and redness of anterior disease."],
   ["Anterior uveitis", "Presents with pain, photophobia, limbal injection and anterior chamber "
                        "cells."],
   ["Scleritis", "Severe boring pain with a violaceous sclera."],
   ["Episcleritis", "Sectoral surface redness without fundus changes."],
   ["Bacterial conjunctivitis", "A surface infection with discharge and no fundus involvement."]],
  "diagnosis", D, 64),
]
