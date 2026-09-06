# -*- coding: utf-8 -*-
"""Neuro-Ophthalmology (Lecture 11) -- second pool."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "11. Neuro-Ophthalmology"
IO = ("a — Neuro-ophthalmological disorders: etiologies, clinical manifestations, differential "
      "diagnosis, diagnostic testing, management, referrals, patient education, prognosis")

QUESTIONS = [

Q("Horner syndrome", IO,
  "Which triad defines Horner syndrome?",
  [["Ptosis, miosis and anhidrosis", "Correct — a sympathetic pathway lesion."],
   ["Ptosis, mydriasis and diplopia", "That is the third nerve palsy pattern."],
   ["Proptosis, chemosis and diplopia", "That suggests orbital or thyroid disease."],
   ["Miosis, photophobia and epiphora", "Not the defined triad."],
   ["Ptosis, exophthalmos and lid lag", "Lid lag and exophthalmos suggest thyroid eye disease."]],
  "diagnosis", D, 27),

Q("Ptosis", IO,
  "Which pair of neuro-ophthalmological conditions produces ptosis?",
  [["Horner syndrome and third nerve palsy",
    "Correct — both drop the lid, and each also disturbs the pupil, so ptosis appears "
    "alongside anisocoria."],
   ["Adie tonic pupil and Argyll Robertson pupil",
    "Both are pupil abnormalities without ptosis."],
   ["Fourth and sixth nerve palsies",
    "Both cause diplopia without affecting the lid."],
   ["Nystagmus and anisocoria", "Neither involves the lid."],
   ["Relative afferent pupillary defect alone", "A pupil finding with no lid component."]],
  "two-step", D, 2),

Q("Anisocoria", IO,
  "A 40-year-old man has pupils of unequal size. The difference is GREATER in bright light. Which "
  "pupil is abnormal?",
  [["The larger pupil, which is failing to constrict",
    "Correct — a defect of constriction shows up in the light."],
   ["The smaller pupil, which is failing to dilate",
    "That pattern is worse in the DARK, indicating a sympathetic problem."],
   ["Both are abnormal", "Only one side fails in a true anisocoria of this pattern."],
   ["Neither; this is physiological", "Physiological anisocoria stays constant across lighting."],
   ["It cannot be determined without imaging", "The lighting comparison localises it at the "
                                               "bedside."]],
  "two-step", D, 19),

Q("Anisocoria", IO,
  "A 35-year-old woman has anisocoria that is GREATER in dim light. Which condition does this "
  "suggest?",
  [["Horner syndrome", "Correct — the sympathetically denervated pupil fails to dilate, so the "
                       "difference grows in the dark."],
   ["Third nerve palsy", "The affected pupil fails to constrict, so the difference grows in "
                         "LIGHT."],
   ["Adie tonic pupil", "A large pupil that fails to constrict, worse in light."],
   ["Pharmacological mydriasis", "A large fixed pupil, worse in light."],
   ["Argyll Robertson pupil", "Bilateral small irregular pupils with light-near dissociation."]],
  "two-step", D, 19),

Q("Cranial nerve III palsy", IO,
  "Which muscles does the third cranial nerve supply?",
  [["Medial, superior and inferior rectus, inferior oblique and levator",
    "Correct, along with the pupillary sphincter."],
   ["Lateral rectus only", "That is the sixth nerve."],
   ["Superior oblique only", "That is the fourth nerve."],
   ["All extraocular muscles", "The fourth and sixth nerves supply two of them."],
   ["Orbicularis oculi", "That is supplied by the facial nerve."]],
  "two-step", D, 39),

Q("Cranial nerve III palsy", IO,
  "Why is a third nerve palsy described as producing an eye that is 'down and out'?",
  [["The unopposed lateral rectus and superior oblique pull it that way",
    "Correct — the muscles the third nerve does NOT supply are the ones left working."],
   ["The medial rectus overacts", "The medial rectus is paralysed in a third nerve palsy."],
   ["The inferior oblique overacts", "It is supplied by the third nerve and is therefore weak."],
   ["Gravity pulls the globe down", "Not the mechanism."],
   ["The levator contracts abnormally", "The levator is weak, producing ptosis."]],
  "two-step", D, 39),

Q("Cranial nerve IV palsy", IO,
  "Which muscle does the fourth cranial nerve supply, and what is its action?",
  [["Superior oblique, which depresses the adducted eye",
    "Correct — hence vertical diplopia worse on downgaze."],
   ["Inferior oblique, which elevates the adducted eye",
    "That is supplied by the third nerve."],
   ["Lateral rectus, which abducts the eye", "That is the sixth nerve."],
   ["Medial rectus, which adducts the eye", "Third nerve, and it moves the globe "
                                          "horizontally rather than vertically."],
   ["Levator palpebrae, which elevates the lid", "Third nerve, and it moves the lid rather than the globe."]],
  "two-step", D, 43),

Q("Nystagmus", IO,
  "A 45-year-old woman has acquired nystagmus with oscillopsia. What does the acquired onset "
  "suggest?",
  [["An underlying neurological cause requiring investigation",
    "Correct — acquired nystagmus in an adult is not benign."],
   ["A benign congenital variant", "Congenital nystagmus is present from infancy and does not "
                                   "cause oscillopsia."],
   ["A refractive error", "Refractive error does not produce nystagmus."],
   ["Normal ageing", "Nystagmus is not a normal age change."],
   ["Anxiety alone", "Not a cause of true nystagmus."]],
  "two-step", D, 5),

Q("Visual fields", IO,
  "A 44-year-old woman has bitemporal hemianopia. Which lesion is most likely?",
  [["A lesion at the optic chiasm",
    "Correct — bitemporal (heteronymous) hemianopsia is the chiasmal pattern."],
   ["An occipital infarct", "Produces a homonymous defect with macular sparing."],
   ["An optic nerve glioma", "Produces monocular loss."],
   ["A retinal detachment", "Produces a monocular field defect corresponding to the detachment."],
   ["A cataract", "Causes generalised blur rather than a field cut."]],
  "diagnosis", D, 25),

Q("Visual fields", IO,
  "Which visual field defect localises the lesion to the optic TRACT?",
  [["A homonymous hemianopia without macular sparing",
    "Correct — post-chiasmal and anterior to the radiations."],
   ["A bitemporal hemianopia", "That is chiasmal."],
   ["A monocular field defect", "That is pre-chiasmal."],
   ["A homonymous hemianopia WITH macular sparing",
    "That is characteristic of an occipital lesion."],
   ["An altitudinal defect", "That suggests ischaemic optic neuropathy."]],
  "two-step", D, 25),

Q("Adie tonic pupil", IO,
  "A 31-year-old woman with a tonic pupil is otherwise well. What is the management?",
  [["Reassurance, once other causes are excluded",
    "Correct — it is benign, though the anisocoria may persist."],
   ["Urgent neuroimaging for an aneurysm", "That is the pupil-involving third nerve palsy "
                                           "pathway."],
   ["High-dose corticosteroids", "No inflammatory process is present."],
   ["Immediate carotid imaging", "That belongs to the painful Horner and amaurosis pathways."],
   ["Surgical iridoplasty", "Not indicated for a benign tonic pupil."]],
  "treatment", D, 37),

Q("Relative afferent pupillary defect", IO,
  "A relative afferent pupillary defect is detected. What does its presence indicate about the "
  "cause of vision loss?",
  [["The optic nerve or extensive retina is involved",
    "Correct — it separates neural causes from media opacities."],
   ["The lens is opaque", "A cataract reduces light but does not usually produce a true afferent "
                          "defect."],
   ["The cornea is scarred", "A media opacity rather than a neural lesion."],
   ["The eye is dry", "Surface disease does not produce an afferent defect."],
   ["The refractive error is uncorrected", "Blur does not alter afferent conduction."]],
  "two-step", D, 26),
]
