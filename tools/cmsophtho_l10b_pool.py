# -*- coding: utf-8 -*-
"""Common Ophthalmological Disorders (Lecture 10) -- second pool.

Fills the conditions the first pool did not reach -- chlamydial and autoimmune
conjunctivitis, non-herpetic keratitis -- and adds second angles on the
conditions that carry the most weight.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "CMS I Common Ophthalmological Disorders"
IO = ("a — Common ophthalmological disorders: etiologies, epidemiology, risk factors, clinical "
      "manifestations, differential diagnosis, diagnostic testing, management, referrals, "
      "patient education, prognosis")

QUESTIONS = [

Q("Adult inclusion conjunctivitis", IO,
  "A 24-year-old sexually active man has a red, mildly sticky left eye that has persisted for five "
  "weeks despite two courses of topical antibiotics. Examination shows large follicles in the "
  "lower fornix and a palpable preauricular node. What is the most likely diagnosis?",
  [["Adult inclusion conjunctivitis", "Correct. Chlamydial disease is chronic and follicular, and "
                                      "it does not respond to ordinary topical antibiotics."],
   ["Viral conjunctivitis", "Follicular with a node, but it resolves in two to three weeks rather "
                            "than persisting for five."],
   ["Bacterial conjunctivitis", "Papillary with thick discharge, and it responds promptly to "
                                "topical treatment."],
   ["Allergic conjunctivitis", "Itchy, bilateral and papillary, with no preauricular node."],
   ["Blepharitis", "Lid margin crusting rather than fornix follicles."]],
  "diagnosis", D, 42),

Q("Adult inclusion conjunctivitis", IO,
  "A 26-year-old woman is diagnosed with adult inclusion conjunctivitis. Besides treating her eye, "
  "what else must be addressed?",
  [["Systemic treatment and partner notification for genital infection",
    "Correct — the eye is a manifestation of a sexually transmitted infection."],
   ["Contact lens hygiene alone", "Does not address the systemic infection."],
   ["Allergen avoidance", "There is no allergic component."],
   ["Lid hygiene twice daily", "That is blepharitis management."],
   ["Nothing further; topical treatment suffices",
    "Topical treatment alone leaves the genital infection untreated."]],
  "two-step", D, 43),

Q("Neonatal chlamydial conjunctivitis", IO,
  "A 9-day-old infant has bilateral lid swelling with a watery-to-mucopurulent discharge. Gonococcal "
  "disease has been excluded. What is the most appropriate treatment?",
  [["Oral erythromycin", "Correct. Systemic treatment is needed because chlamydia also colonises "
                         "the nasopharynx and risks pneumonitis."],
   ["Topical erythromycin ointment alone", "Topical treatment leaves the nasopharyngeal "
                                           "colonisation untreated."],
   ["A single dose of intramuscular ceftriaxone", "That is the gonococcal pathway, already "
                                                  "excluded."],
   ["Observation, as neonatal conjunctivitis is self-limiting",
    "Untreated chlamydial disease risks pneumonitis."],
   ["Topical acyclovir", "The organism is bacterial."]],
  "treatment", D, 44),

Q("Neonatal conjunctivitis", IO,
  "A newborn develops a purulent conjunctivitis on day 2 of life. Which organism is most likely, "
  "given the timing?",
  [["Neisseria gonorrhoeae", "Correct. Gonococcal disease presents in the first few days; "
                             "chlamydial disease presents later, around days 5 to 14."],
   ["Chlamydia trachomatis", "Presents later than the first few days."],
   ["Herpes simplex virus", "Presents in the first two weeks but with vesicles and keratitis."],
   ["Staphylococcus aureus", "A cause of later, milder neonatal conjunctivitis."],
   ["Adenovirus", "Not the typical neonatal pathogen."]],
  "two-step", D, 44),

Q("Autoimmune conjunctivitis", IO,
  "A 68-year-old woman has chronic red, gritty eyes with progressive scarring of the lower "
  "palpebral conjunctiva and shortening of the fornix. She also has oral erosions. What is the most "
  "likely diagnosis?",
  [["Ocular mucous membrane pemphigoid", "Correct. Progressive subconjunctival fibrosis with "
                                         "mucosal involvement elsewhere."],
   ["Bacterial conjunctivitis", "Acute and purulent, and it does not scar the conjunctiva."],
   ["Allergic conjunctivitis", "Itchy and episodic, without cicatrisation."],
   ["Viral conjunctivitis", "Acute and self-limiting."],
   ["Trachoma", "Also cicatricial, but follows chronic chlamydial infection in an endemic area "
                "rather than accompanying oral erosions."]],
  "diagnosis", D, 38),

Q("Keratitis", IO,
  "A 30-year-old woman has a painful, photophobic red right eye with reduced vision. Fluorescein "
  "shows diffuse punctate uptake across the cornea without a discrete infiltrate. She has been "
  "using a hairdryer at close range and has dry eyes. What is the most likely diagnosis?",
  [["Punctate epithelial keratitis", "Correct. Diffuse punctate staining without an infiltrate, "
                                     "from exposure and surface drying."],
   ["Bacterial corneal ulcer", "Would show a focal white infiltrate with an overlying defect."],
   ["Herpes simplex keratitis", "Produces a branching dendrite with terminal end bulbs."],
   ["Anterior uveitis", "Anterior chamber cells with limbal injection, and the cornea does not "
                        "stain diffusely."],
   ["Acute angle-closure glaucoma", "A hazy cornea from oedema with a fixed mid-dilated pupil."]],
  "diagnosis", D, 55),

Q("Keratitis", IO,
  "A 27-year-old man with a red painful eye is found to have keratitis. Which examination step is "
  "essential before any treatment is chosen?",
  [["Fluorescein staining at the slit lamp", "Correct — it distinguishes a dendrite from an ulcer "
                                             "from punctate disease, and each is treated "
                                             "differently."],
   ["Dilated fundus examination", "The pathology here is corneal, not retinal."],
   ["Visual field testing", "Not informative in corneal disease."],
   ["Colour vision testing", "Assesses optic nerve function."],
   ["Tonometry alone", "Pressure does not identify the corneal lesion."]],
  "two-step", D, 56),

Q("Corneal ulcer", IO,
  "A 45-year-old woman has a painful red eye with a 2 mm white corneal infiltrate, an overlying "
  "epithelial defect and a small hypopyon. What is the most appropriate next step?",
  [["Urgent ophthalmology referral for corneal scraping and intensive topical antibiotics",
    "Correct. A hypopyon indicates significant intraocular inflammation and the eye is at risk."],
   ["Topical antibiotic drops four times daily and review in a week",
    "Standard-frequency drops and a week's delay are inadequate for a suppurative ulcer."],
   ["Topical corticosteroids alone", "Steroids without cover can accelerate corneal melt."],
   ["Patch the eye and give oral analgesia", "Patching an infected cornea is contraindicated."],
   ["Reassure and review if worse", "A hypopyon requires same-day management."]],
  "treatment", D, 61),

Q("Herpes simplex keratitis", IO,
  "A 42-year-old man with a corneal dendrite is prescribed treatment. Which agent must be AVOIDED?",
  [["Topical corticosteroid", "Correct. Steroid on an active dendritic ulcer can cause it to "
                              "enlarge into a geographic ulcer."],
   ["Topical antiviral", "The appropriate treatment for epithelial herpetic disease."],
   ["Oral antiviral", "An appropriate alternative or adjunct."],
   ["Lubricating drops", "Supportive and harmless."],
   ["Cycloplegic for comfort", "Reasonable symptomatic care."]],
  "two-step", D, 58),

Q("Herpes zoster ophthalmicus", IO,
  "A 71-year-old man has a painful vesicular rash in a band across his right forehead, sparing the "
  "midline, with vesicles on the tip of his nose. What does the nasal tip involvement indicate?",
  [["A high likelihood of ocular involvement",
    "Correct — Hutchinson sign; the nasociliary branch supplies both the nose tip and the globe."],
   ["That the rash will cross the midline", "Zoster respects the midline."],
   ["That the cause is herpes simplex rather than zoster",
    "The dermatomal band with midline sparing is zoster."],
   ["That antiviral treatment is unnecessary", "Ocular involvement makes treatment more urgent, "
                                               "not less."],
   ["That the trigeminal ganglion is spared", "The rash reflects reactivation in that ganglion."]],
  "two-step", D, 57),

Q("Pre-septal cellulitis", IO,
  "A 4-year-old girl has pre-septal cellulitis. She is systemically well and her parents are "
  "reliable. What is the appropriate management?",
  [["Oral antibiotics with review in 24 to 48 hours",
    "Correct for mild pre-septal disease in a well child with reliable follow-up."],
   ["Admit for intravenous antibiotics", "Reserved for moderate-to-severe disease, toxicity, poor "
                                         "compliance, children five and under who are unwell, or "
                                         "failure of oral treatment."],
   ["Topical antibiotic drops alone", "Drops do not treat a soft tissue infection."],
   ["Immediate surgical drainage", "No abscess is described."],
   ["Observation without antibiotics", "This is a bacterial infection."]],
  "treatment", D, 53),

Q("Pre-septal cellulitis", IO,
  "A 7-year-old boy treated for pre-septal cellulitis returns after 48 hours with new pain on eye "
  "movement and mild proptosis. What has happened?",
  [["The infection has progressed behind the orbital septum",
    "Correct — painful restricted movement and proptosis mean post-septal disease."],
   ["He has developed an allergic reaction to the antibiotic",
    "Allergy does not cause proptosis or painful movement."],
   ["The diagnosis was always a chalazion", "A chalazion is painless and does not progress this "
                                            "way."],
   ["He has developed conjunctivitis", "A surface infection does not restrict eye movement."],
   ["The swelling is simply resolving slowly", "New pain on movement is progression, not "
                                               "resolution."]],
  "two-step", D, 53),

Q("Episcleritis", IO,
  "A 33-year-old woman has recurrent episodes of sectoral eye redness with mild irritation, each "
  "resolving within a week or two. Vision is always normal. What is the appropriate management?",
  [["Reassurance, with lubricants for comfort", "Correct. Episcleritis is self-limiting and often "
                                                "needs no specific treatment."],
   ["Urgent systemic workup for vasculitis", "That belongs to scleritis, which is painful and "
                                             "sight-threatening."],
   ["Long-term oral corticosteroids", "Disproportionate for a self-limiting surface condition."],
   ["Topical antibiotics", "There is no infection."],
   ["Immediate ophthalmology referral", "Not required for typical self-limiting episcleritis."]],
  "treatment", D, 48),

Q("Scleritis", IO,
  "A 49-year-old woman has severe deep eye pain that wakes her at night, with a bluish hue to the "
  "sclera visible in daylight. What systemic evaluation is warranted?",
  [["A workup for autoimmune connective tissue disease",
    "Correct — scleritis is frequently associated with systemic autoimmune disease."],
   ["Carotid Doppler studies", "That belongs to the amaurosis fugax pathway."],
   ["Sexual health screening", "Relevant to chlamydial conjunctivitis, not scleritis."],
   ["Allergy skin testing", "Not indicated in scleral inflammation."],
   ["Thyroid function alone", "Thyroid disease causes proptosis rather than scleritis."]],
  "two-step", D, 50),

Q("Viral conjunctivitis", IO,
  "A 32-year-old teacher with viral conjunctivitis asks what she should do about work. What is the "
  "key advice?",
  [["Strict hand hygiene, as it is highly contagious",
    "Correct — contagious precautions are the central education point."],
   ["No precautions are needed once tears stop", "It remains contagious throughout the illness."],
   ["Antibiotic drops will make her non-infectious", "Antibiotics do not treat a viral infection."],
   ["She should avoid reading to rest the eye", "Rest does not affect transmission or course."],
   ["She may share towels if they are washed weekly", "Shared towels are exactly how it spreads."]],
  "two-step", D, 37),

Q("Bacterial conjunctivitis", IO,
  "A 28-year-old healthy woman has bacterial conjunctivitis in one eye, with no contact lens use "
  "and no other risk factors. What is the appropriate treatment?",
  [["A topical broad-spectrum antibiotic", "Correct — a fluoroquinolone is the named example, with "
                                           "contagious precautions."],
   ["Oral antibiotics", "Not required in an immunocompetent adult with surface disease."],
   ["Topical corticosteroid", "Steroid on an untreated infection is unsafe."],
   ["Artificial tears alone", "Supportive but not the specific treatment."],
   ["Topical antiviral", "The organism is bacterial."]],
  "treatment", D, 41),

Q("Bacterial conjunctivitis", IO,
  "A 35-year-old man with bacterial conjunctivitis shows no improvement after 24 hours of topical "
  "antibiotic. What does that indicate?",
  [["Referral is warranted", "Correct. A prompt and total response is expected in a normal host, so "
                             "failure at 24 hours changes the plan."],
   ["The course should simply be extended to a week",
    "Lack of any response at 24 hours is itself the signal."],
   ["He should switch to oral antibiotics himself",
    "The escalation is referral, not self-directed oral therapy."],
   ["It confirms an allergic cause", "Allergic disease itches and is bilateral."],
   ["He should stop treatment and observe", "Stopping does not address a non-responding "
                                            "infection."]],
  "two-step", D, 41),

Q("Dacryoadenitis", IO,
  "A 29-year-old woman has dacryoadenitis. Imaging is being considered. What does the deck's own "
  "hedge say about it?",
  [["Contrast computed tomography is used when indicated, not automatically",
    "Correct — several slides read as absolutes and are softened in their own notes."],
   ["Every patient needs imaging on presentation", "Imaging is not automatic."],
   ["Imaging is never indicated", "It is used when there is concern about orbital involvement."],
   ["Only magnetic resonance imaging is acceptable",
    "Contrast computed tomography of orbits and sinuses is what is named."],
   ["Imaging is required before antibiotics", "Treatment is not gated on imaging."]],
  "two-step", D, 23),

Q("Dacryoadenitis", IO,
  "A 36-year-old man with inflammatory dacryoadenitis is started on corticosteroids. Within what "
  "period should inflammatory disease respond?",
  [["48 hours", "Correct — failure to respond in that window prompts reconsideration."],
   ["Two weeks", "Longer than the expected response window."],
   ["Six hours", "Faster than the stated expectation."],
   ["One month", "Far longer than the expected window."],
   ["It is not expected to respond to steroids at all",
    "Inflammatory disease is precisely what steroids treat here."]],
  "two-step", D, 23),

Q("Dacryoadenitis", IO,
  "A 41-year-old woman has painful swelling of the outer upper lid and the cause is not yet clear. "
  "Why must corticosteroids not be started immediately?",
  [["Infection must be reasonably excluded first",
    "Correct — empiric oral antibiotics for 24 hours with reassessment is the alternative path."],
   ["Steroids raise intraocular pressure within hours",
    "A real effect over time, but not the reason for the caution here."],
   ["Steroids would mask a lacrimal sac tumour",
    "The concern is masking or worsening infection."],
   ["Steroids are contraindicated in all lid disease", "They are used for inflammatory disease."],
   ["Steroids interact with topical antibiotics", "Not the stated reason."]],
  "two-step", D, 23),

Q("Entropion", IO,
  "A 76-year-old man with entropion has developed a corneal epithelial defect from lash contact. "
  "What does this change?",
  [["The cornea is now involved, which is what the examination is looking for",
    "Correct — the slit lamp question in these lid malpositions is always whether the cornea has "
    "been affected."],
   ["It confirms the diagnosis is ectropion", "Ectropion turns the lid outward and does not bring "
                                              "lashes onto the cornea."],
   ["Surgery is no longer possible", "Corneal involvement makes surgery more pressing, not less."],
   ["Lubricants should be stopped", "Lubrication remains part of protecting the surface."],
   ["It indicates infection", "An abrasion from lashes is mechanical, not infective."]],
  "two-step", D, 13),

Q("Pterygium", IO,
  "A 47-year-old surfer has a pterygium that has advanced 2 mm onto the cornea over two years and "
  "now induces astigmatism. What is the appropriate management?",
  [["Refer for surgical excision", "Correct. Surgery is indicated when it grows onto the cornea and "
                                   "distorts vision."],
   ["Continue lubricants and sun protection alone",
    "Conservative care controls symptoms but will not stop documented growth affecting vision."],
   ["Start topical corticosteroids long term", "Not the definitive management."],
   ["Prescribe glasses to correct the astigmatism",
    "Correcting the refractive consequence does not address the growing lesion."],
   ["Reassure, as pterygia never affect vision", "This one already has."]],
  "treatment", D, 28),

Q("Subconjunctival haemorrhage", IO,
  "A 58-year-old woman has had three subconjunctival haemorrhages in six months. She takes no "
  "anticoagulants. What is the appropriate approach?",
  [["Medication review, blood pressure check and targeted haematologic evaluation",
    "Correct — targeted rather than an automatic haematology referral."],
   ["Automatic referral to haematology", "The deck's own notes soften that into a targeted "
                                         "evaluation."],
   ["Reassurance with no investigation", "Recurrence without a culprit warrants some evaluation."],
   ["Urgent ophthalmology referral", "The eye itself is not at risk."],
   ["Start topical corticosteroids", "There is no inflammation to treat."]],
  "treatment", D, 30),

Q("Anterior uveitis", IO,
  "A 38-year-old man with anterior uveitis is prescribed a cycloplegic alongside the steroid. What "
  "is its purpose?",
  [["To relieve pain and prevent posterior synechiae",
    "Correct — it rests the ciliary body and keeps the iris from adhering to the lens."],
   ["To lower the intraocular pressure", "Cycloplegics do not lower pressure and may raise it in a "
                                         "narrow angle."],
   ["To treat the underlying infection", "Uveitis here is inflammatory rather than infective."],
   ["To improve near vision", "Cycloplegia abolishes accommodation, worsening near vision."],
   ["To reduce corneal oedema", "Not its mechanism."]],
  "two-step", D, 63),

Q("Red eye triage", IO,
  "A patient presents with a red eye. Which two findings are the red flags that separate a "
  "dangerous cause from a benign one?",
  [["Reduced vision and true pain", "Correct — those two are what move a red eye out of the benign "
                                    "category."],
   ["Discharge and lid crusting", "Common in benign surface infections."],
   ["Itching and watering", "Typical of allergic and viral disease."],
   ["Foreign body sensation and tearing", "Non-specific surface symptoms."],
   ["Bilateral involvement and recent contact", "Suggests infectious conjunctivitis rather than "
                                                "danger."]],
  "two-step", D, 8),
]
