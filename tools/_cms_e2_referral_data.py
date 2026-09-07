# -*- coding: utf-8 -*-
"""Content for the CMS I Exam 2 referral-urgency guide.

Every tier, danger sign and disposition line comes from Lecture 10 slides 66-71,
which are a dedicated RED EYE TRIAGE section the deck builds to and then never
revisits. The per-condition rows are distilled from the audited rows in
build_cms_ophtho_chart.py, so the giveaway and the first move are the chart's --
this file only shortens them to a triage length and adds nothing.

FIRST[condition] = the single most useful thing to do before or while referring.
Where the chart's treatment field is a full management paragraph, this is its
opening move, not a summary of the whole course.
"""

# --- Lecture 10 slide 67, verbatim order -------------------------------------
FIRST_60 = [
 ("Visual acuity in each eye", "with correction"),
 ("Pupils", "shape, reactivity, afferent defect"),
 ("Extraocular movements", "note pain or restriction"),
 ("Cornea", "clarity, and fluorescein staining"),
 ("Injection and discharge", "the pattern of each"),
 ("The history that changes everything",
  "contact lenses, trauma, surgery, steroids"),
]
FIRST_60_RULE = ("Reduced vision or an abnormal pupil is a red flag &mdash; and the whole list is "
                 "meant to be completed <em>before</em> naming the diagnosis.")

# --- Lecture 10 slide 68 ------------------------------------------------------
DANGER = [
 "Moderate to severe pain, or consensual photophobia",
 "Reduced visual acuity, a relative afferent pupillary defect, or an abnormal pupil",
 "Corneal opacity, infiltrate, ulcer or dendrite",
 "Ciliary flush, hypopyon, or markedly elevated intraocular pressure",
 "Proptosis, diplopia, or painful or restricted eye movement",
 "Chemical exposure, penetrating trauma, or recent eye surgery",
 "A contact lens wearer with pain or photophobia",
]

# --- Lecture 10 slide 69 ------------------------------------------------------
PATTERN = [
 ("Conjunctiva", "Itch or discharge &middot; diffuse injection &middot; <b>vision preserved</b>"),
 ("Cornea", "Pain and photophobia &middot; fluorescein defect, infiltrate or opacity"),
 ("Anterior chamber", "<b>Consensual</b> photophobia &middot; ciliary flush &middot; irregular pupil"),
 ("Sclera or orbit", "Deep pain, or painful eye movement &middot; violaceous sclera, proptosis, "
                     "restriction"),
 ("Angle closure", "Pain and headache with halos and nausea &middot; cloudy cornea &middot; "
                   "mid-dilated pupil"),
]

# --- Lecture 10 slide 70, the deck's own four tiers ---------------------------
LADDER = [
 ("EMERGENT", "now",
  "Chemical injury (irrigate first), open globe, angle closure, orbital cellulitis, "
  "endophthalmitis"),
 ("SAME DAY", "today",
  "Keratitis or corneal ulcer, anterior uveitis, scleritis, ocular herpes zoster"),
 ("URGENT", "within 24&ndash;48 hours",
  "Unexplained decreased vision, persistent pain or photophobia, an atypical or worsening "
  "red eye"),
 ("ROUTINE", "in clinic",
  "Uncomplicated conjunctivitis, or chronic eyelid and ocular-surface disease"),
]

# --- the first move, per condition -------------------------------------------
FIRST = {
 # EMERGENT
 "Chemical injury": "<b>Irrigate first</b> &mdash; before acuity, before examination, before the "
                    "referral call.",
 "Endophthalmitis": "Ophthalmology now. It is what undertreated keratitis becomes, and it can "
                    "cost the eye.",
 "Open globe injury": "<b>Rigid shield taped over the eye</b>, ophthalmology called immediately. "
                      "Antiemetics and analgesia so the patient does not strain; tetanus.",
 "Globe rupture": "Shield, ophthalmology immediately, antiemetics, analgesia, tetanus. Immediate "
                  "surgical repair with wound exploration.",
 "Full-thickness eye wall laceration": "Shield and ophthalmology. Surgical repair &mdash; and "
                     "posterior-segment foreign bodies are deliberately left alone at first.",
 "Acute angle-closure glaucoma": "Topical pilocarpine or timolol, intravenous acetazolamide, then "
                     "mannitol or isosorbide. Laser peripheral iridotomy 1&ndash;2 days after onset.",
 "Post-septal (orbital) cellulitis": "<b>Hospitalise.</b> Broad-spectrum intravenous antibiotics "
                     "for 48&ndash;72 hours, then oral for at least a week.",
 "Corneal ulcer": "Broad-spectrum topical fourth-generation fluoroquinolone to start; "
                  "agent-specific therapy then follows from ophthalmology.",
 "Retinal detachment": "<b>Refer immediately.</b> Surgery urgently, or within a week, depending on "
                       "type.",
 "Retinal detachment &mdash; rhegmatogenous": "Ophthalmology STAT and seen within 24 hours. Pain "
                       "control, antiemetics, head of bed at 30&ndash;40 degrees.",
 "Retinal detachment &mdash; traction": "Surgical &mdash; and the diabetic control conversation "
                       "that should have come years earlier.",
 "Central retinal artery occlusion (CRAO)": "High-concentration inhaled oxygen and digital massage, "
                       "intravenous acetazolamide, anterior chamber paracentesis; thrombolytic "
                       "within 8 hours. <b>Irreversible after 90 minutes.</b>",
 "Branch retinal artery occlusion (BRAO)": "As for the central form &mdash; the management does "
                       "not change, only the size of the field lost.",
 "Arteritic AION (giant cell arteritis)": "Intravenous methylprednisolone for 3 days, then a slow "
                       "oral taper. <b>Do not wait for the biopsy.</b>",
 "Papilledema": "Neuroimaging first to exclude a mass, then lumbar puncture; treat the cause. The "
                "raised pressure is <b>intracranial, not intraocular</b>.",
 "Horner syndrome": "Treat the cause &mdash; but with neck pain, trauma or focal neurology it is "
                    "<b>carotid dissection until proven otherwise</b>.",
 "Cranial nerve III palsy": "<b>A pupil-involving third is STAT</b> &mdash; image for a posterior "
                    "communicating artery aneurysm.",
 "Hyphema": "Bed rest with the head elevated, antiemetics, ocular hypotensives, cycloplegic drops "
            "and oral aminocaproic acid. Rebleeding peaks in the first 72 hours.",
 "Lid laceration": "Ophthalmology for margin involvement, within 6&ndash;8&nbsp;mm of the medial "
                   "canthus, the lacrimal system, the inner lid surface, ptosis, tarsal plate or "
                   "levator.",
 "Periorbital haematoma": "<b>Canthotomy with cantholysis</b> &mdash; release the lateral canthal "
                   "tendon and cut its inferior branch to let the blood out.",
 "Orbital floor (blowout) fracture": "True blowout &rarr; ophthalmology, because <b>30% have a "
                   "significant globe injury</b>. Entrapment &rarr; facial trauma surgeon.",
 "Basilar skull fracture": "Cerebrospinal fluid leak &rarr; neurosurgery consult and admission.",
 "Gonococcal conjunctivitis": "Newborn: <b>hospitalise</b>, systemic ceftriaxone once, specialty "
                   "consultation. Untreated risk is corneal perforation.",
 "Cataract &mdash; pediatric": "Surgery is <b>not</b> deferred in a neonate &mdash; it is done "
                   "early to prevent amblyopia.",
 "Retinoblastoma": "Ocular oncology, multimodal therapy, genetic counselling. An absent red reflex "
                   "in a newborn is this or congenital cataract until proven otherwise.",
 # SAME DAY
 "Scleritis": "Systemic anti-inflammatories to begin; corticosteroids and immunomodulators for "
              "severe, necrotising, posterior or refractory disease. The sclera can perforate.",
 "Keratitis": "Referral <b>within 24 hours</b> for slit lamp with fluorescein, and treat the "
              "underlying cause before it scars.",
 "Herpes simplex keratitis": "Oral antivirals for 10 days.",
 "Herpes zoster keratitis": "Oral antivirals for 10 days, ideally <b>within 72 hours</b> of the "
              "rash appearing.",
 "Anterior uveitis (iritis, iridocyclitis)": "Within 24 hours, because delay may cost vision. "
              "Non-infectious &rarr; topical corticosteroids.",
 "Age-related macular degeneration &mdash; wet": "Intravitreal anti-VEGF; thermal laser "
              "photocoagulation or photodynamic therapy.",
 # URGENT
 "Dacryoadenitis": "Inflammatory &rarr; corticosteroids. Cause unclear &rarr; empiric oral "
                   "antibiotics, reassessed at 24 hours.",
 "Dacryocystitis": "Well and afebrile &rarr; oral antibiotics 10 days. Febrile or ill &rarr; "
                   "admit for intravenous therapy 48&ndash;72 hours.",
 "Chemosis": "Treat the cause &mdash; but proptosis, restricted movement, reduced vision or an "
             "afferent defect alongside it makes this <b>urgent</b>.",
 "Chlamydial conjunctivitis &mdash; neonatal": "Erythromycin 50&nbsp;mg/kg/day in four divided "
             "doses for 14 days.",
 "Trachoma": "Azithromycin 1&nbsp;g orally as a single dose. <b>Trichiasis requires surgery.</b>",
 "Pre-septal (periorbital) cellulitis": "Mild &rarr; oral antibiotics 10&ndash;14 days. <b>Admit</b> "
             "if moderate-severe or toxic, unreliable, a child of 5 or under, or not improving.",
 "Posterior uveitis (choroiditis, retinitis)": "Does <b>not</b> respond to topical treatment "
             "&mdash; may need an intraocular corticosteroid injection.",
 "Amaurosis fugax": "Treat it as a transient ischaemic attack of the eye: stroke workup, carotid "
             "imaging, cardiac assessment, antiplatelets.",
 "Optic neuritis": "Corticosteroids if a demyelinating cause is found; two or more lesions &rarr; "
             "neurology or neuro-ophthalmology.",
 "Central retinal vein occlusion (CRVO)": "Urgent referral to restore flow, and evaluate the "
             "underlying disorder &mdash; hypertension, diabetes, hyperviscosity.",
 "Branch retinal vein occlusion (BRVO)": "As for the central form, and treat the underlying "
             "disorder.",
 "Non-arteritic AION": "Observation and cardiovascular risk factor modification &mdash; but the "
             "workup is <b>identical</b> to the arteritic form, because that must be excluded.",
 "Relative afferent pupillary defect (Marcus Gunn)": "A sign, not a diagnosis &mdash; find the "
             "retinal or optic nerve disease behind it.",
 "Argyll Robertson pupil": "Treat the underlying syphilis.",
 "Cranial nerve IV palsy": "Traumatic: observe about 6 months before corrective treatment, "
             "patching one eye meanwhile.",
 "Cranial nerve VI palsy": "Traumatic: observe about 6 months, patching one eye in the interim.",
 "Nystagmus": "Complete ophthalmic examination, then imaging, then labs. The aetiology must be "
             "addressed.",
 "Idiopathic intracranial hypertension": "Acetazolamide promptly, with a supervised weight "
             "reduction programme. Surgery only if medical therapy fails.",
 "Strabismus": "Ophthalmology, and treat the cause &mdash; untreated in a child it causes "
             "amblyopia.",
 "Amblyopia": "Patch or atropinise the <b>good</b> eye to force the weaker one to work. Treatment "
             "works less well as visual maturity approaches.",
 "Uveal melanoma": "Radiation therapy is now the commonest treatment; enucleation is needed less "
             "often.",
 "Conjunctival melanoma": "Specialist management under ocular oncology.",
 "Corneal abrasion": "Topical broad-spectrum antibacterial, and periodic re-examination to confirm "
             "healing and exclude infection.",
 "Corneal or conjunctival foreign body": "Topical anaesthetic, then a sterile 27-gauge needle. A "
             "rust ring comes out with a burr.",
 "Orbital contusion": "Supportive, through to surgery depending on the patient's condition.",
 "Retinal detachment &mdash; exudative": "Treat the underlying condition &mdash; this one is not "
             "primarily a surgical problem.",
}

# Named on the disposition slide but given no condition slide of their own.
EXTRA_EMERGENT = [
 ("Chemical injury", "Ocular surface",
  "Any chemical exposure &middot; the disposition slide lists it FIRST", "Slide 70"),
 ("Endophthalmitis", "Whole eye",
  "Inflammation of the WHOLE eye &middot; what undertreated keratitis becomes", "Slides 5, 56, 70"),
]

# --- where the decks do not simply agree with themselves -----------------------
# Checked slide by slide against all five decks on 2026-09-07. Three kinds of
# caveat, and they are worth more than the tier itself, because a student who
# revises the condition slide and one who revises the disposition slide will
# answer differently.
#
#   conflict   -- the deck states two different urgencies in two places
#   nointerval -- the deck says "refer" and never says how fast; the tier here is
#                 an inference from severity, not something the slides state
#   nuance     -- the tier is right for the severe form only
NOTE = {
 "Scleritis": ("conflict",
   "Slide 50 says <b>urgent referral</b>; the disposition slide puts scleritis in "
   "<b>same day</b>. The deck says both."),
 "Corneal ulcer": ("conflict",
   "Slide 61 says <b>emergent referral</b>; the disposition slide groups "
   "&ldquo;keratitis/corneal ulcer&rdquo; under <b>same day</b>. The deck says both."),
 "Posterior uveitis (choroiditis, retinitis)": ("nointerval",
   "The slide says only &ldquo;refer to ophthalmology&rdquo; &mdash; no interval &mdash; and notes "
   "it develops far more slowly than anterior uveitis."),
 "Optic neuritis": ("nointerval",
   "The slide says &ldquo;REFER to Optho&rdquo; without stating how fast."),
 "Idiopathic intracranial hypertension": ("nointerval",
   "The referral carries no stated interval; it is the <b>acetazolamide</b> the slide says to "
   "start promptly."),
 "Orbital floor (blowout) fracture": ("nuance",
   "<b>Without eye injury or entrapment this is not emergent</b> &mdash; ice, analgesia and "
   "follow-up in 2&ndash;3 days. Only a true blowout or entrapment escalates."),
 "Lid laceration": ("nuance",
   "A partial-thickness laceration meeting none of those criteria can be repaired in the "
   "emergency department, with ophthalmology in <b>2&ndash;3 days</b>."),
 "Corneal or conjunctival foreign body": ("nuance",
   "Consult immediately instead if there is any concern the object passed <b>through</b> the "
   "cornea."),
 "Nystagmus": ("nuance",
   "Who to refer, explicitly: <b>infants and young children</b>; nystagmus <b>acquired</b> in "
   "adolescence or adulthood; and non-physiologic nystagmus in adults &mdash; upbeat, "
   "monocular or asymmetric, or non-physiologic horizontal."),
}

# Lecture 11 slide 54, the pathway every neuro-ophthalmology condition follows.
NEURO_PATHWAY = ("History and physical examination &rarr; labs and imaging (head computed "
                 "tomography or magnetic resonance imaging of the brain) if indicated &rarr; "
                 "<b>ophthalmology referral</b> &rarr; the appropriate specialist: neurology, "
                 "vascular surgery or neurosurgery.")

# --- routine, until a trigger fires -------------------------------------------
ESCALATE = [
 ("Bacterial conjunctivitis",
  "Immunocompromised &middot; contact lens wearer &middot; recent eye surgery &middot; foreign "
  "body &middot; corneal opacity or suspicion of keratitis &middot; <b>no improvement in 24 "
  "hours</b>", "Urgent", "Slide 41"),
 ("Bacterial conjunctivitis &mdash; newborn",
  "Suspected gonococcal infection in a newborn &mdash; untreated risk is corneal perforation",
  "EMERGENT", "Slide 41"),
 ("Viral conjunctivitis",
  "Longer than 3 weeks &middot; photophobia or vision loss appearing after onset", "Refer",
  "Slides 36&ndash;37"),
 ("Episcleritis", "No response in 2 days", "Refer", "Slides 47&ndash;48"),
 ("Chemosis",
  "Proptosis &middot; restricted movement &middot; reduced vision &middot; an afferent pupillary "
  "defect", "URGENT", "Slide 31"),
 ("Pterygium", "Growing, or vision affected", "Refer", "Slides 27&ndash;28"),
 ("Chalazion / hordeolum",
  "Chalazion recurrent, or persisting <b>more than 2&ndash;3 months</b> &mdash; refer to rule out "
  "<b>sebaceous carcinoma</b> &middot; hordeolum not improving in 2 weeks &middot; associated "
  "pre-septal cellulitis", "Refer", "Slide 21"),
 ("Blepharitis / meibomitis",
  "Symptoms not improving after <b>several weeks</b> of lid hygiene", "Refer",
  "Slides 18&ndash;19"),
 ("Allergic conjunctivitis",
  "Not settling as allergen levels fall &mdash; the disease may be unusually severe, or the "
  "<b>diagnosis may be wrong</b>", "Refer", "Slide 35"),
 ("Iris nevus",
  "Any concerning feature &mdash; refer to <b>rule out melanoma</b>; ophthalmology may pass it to "
  "ocular oncology", "Refer", "Slide 49"),
 ("Pre-septal cellulitis",
  "Moderate-severe or toxic &middot; poor compliance &middot; <b>child aged 5 or under</b> "
  "&middot; no improvement on oral antibiotics", "Admit", "Slides 51&ndash;53"),
]

# --- the prohibitions ---------------------------------------------------------
NEVER = [
 ("Never dilate an eye when ocular trauma is suspected.",
  "The deck puts an exclamation mark on this one.", "Ocular Trauma, slide 6"),
 ("Do not remove a penetrating object.",
  "Ensure tetanus is up to date, image, and leave it where it is.", "Ocular Trauma, slide 6"),
 ("Computed tomography of the orbit without contrast &mdash; and <b>no MRI</b>.",
  "Metallic foreign bodies and magnets do not mix.", "Ocular Trauma, slide 6"),
 ("Do not measure intraocular pressure if a penetrating globe injury is suspected.",
  "Pressing on an open eye can extrude its contents.", "Ocular Trauma, slide 25"),
 ("Do not patch the contact lens wearer with a corneal defect.",
  "Remove the lenses, keep them if a culture is wanted, and arrange same-day review.",
  "Common Ophthalmological Disorders, slide 71"),
 ("No take-home topical anaesthetic, and no take-home corticosteroid.",
  "Repeated anaesthetic is toxic to the epithelium and delays healing; steroids can worsen an "
  "infection that has not been identified yet.",
  "Common Ophthalmological Disorders, slide 71; Ocular Trauma, slide 18"),
 ("Leave posterior-segment foreign bodies alone at the first evaluation.",
  "Going after one early risks more damage than the object itself.", "Ocular Trauma, slide 16"),
 ("Do not wait for the temporal artery biopsy before starting steroids.",
  "In arteritic anterior ischaemic optic neuropathy the delay costs the second eye.",
  "Acute Vision Loss, slides 49&ndash;51"),
]

# --- self-check ---------------------------------------------------------------
QUIZ = [
 ("A contact lens wearer has severe pain, photophobia and blurred vision after sleeping in the "
  "lenses. Fluorescein shows a central epithelial defect with a white infiltrate. What are the "
  "next steps?",
  "Remove the lenses and <b>do not patch</b>. No take-home topical anaesthetic or corticosteroid. "
  "Same-day ophthalmology for microbial keratitis. Preserve the lenses and case in case a culture "
  "is requested."),
 ("Which conditions sit in the EMERGENT &mdash; now tier?",
  "Five of them: chemical injury (irrigate first), open globe, angle closure, orbital cellulitis "
  "and endophthalmitis."),
 ("A patient over 55 has sudden visual loss, a new temporal headache and jaw claudication. What "
  "must not delay treatment?",
  "The temporal artery biopsy. Start intravenous methylprednisolone; untreated, the second eye "
  "follows the first."),
 ("Which two findings on the first-60-seconds list are called red flags in their own right?",
  "Reduced vision, and an abnormal pupil."),
 ("A child is struck in the eye with a ball and has severe pain, vomiting and bradycardia on "
  "attempted upgaze, but the eye looks quiet. What is this?",
  "An orbital floor fracture with inferior rectus entrapment &mdash; the white-eyed blowout. The "
  "autonomic disturbance is the clue, and it needs a facial trauma surgeon."),
 ("What separates pre-septal from post-septal cellulitis at the bedside?",
  "In pre-septal disease <b>the eye itself is white</b>, movements are full and painless, and "
  "vision is normal. Proptosis, painful or restricted movement, diplopia or reduced vision means "
  "post-septal &mdash; and that is emergent."),
]
