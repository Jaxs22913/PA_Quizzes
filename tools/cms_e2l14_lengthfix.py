# -*- coding: utf-8 -*-
"""Length-bias fixes for the CMS I Exam 2 Lecture 14 pools.

Jaxon's rule, 2026-08-30, supersedes the pad-only approach used for Lecture 1:
SHORTEN THE ANSWER, do not pad the distractors -- and never shorten at the cost
of learning. So KEYS holds shortened correct answers, and every one is asserted
to be strictly shorter.

SPECIFIC is the exception, for the two questions where the key is a LIST and
the list IS the content. Cutting it would delete the fact the question exists
to teach, so instead one distractor is made genuinely more specific, which also
makes it a better distractor.

Keys are (module, index) into that pool module's own QUESTIONS, not into a
concatenated pool -- the four vignette modules are combined in a different
order than the three objective ones.
"""

# --- shortened CORRECT answers (index 0 in every pool question) -------------
KEYS = {
 ("cms_e2l14_pool_a", 10): "Vomiting raises intraocular pressure",
 ("cms_e2l14_pool_a", 11): "Posterior to the muscle insertions, old incisions, the lamina cribrosa",
 ("cms_e2l14_pool_a", 15): "Slit lamp fluorescein",
 ("cms_e2l14_pool_a", 18): "A burr tip drill",
 ("cms_e2l14_pool_a", 22): "It slows clot breakdown",
 ("cms_e2l14_pool_a", 25): "Aspirin and antiplatelets",
 ("cms_e2l14_pool_b", 0):  "The canalicular system may be transected",
 ("cms_e2l14_pool_b", 2):  "Repair there, ophthalmology in 2 to 3 days",
 ("cms_e2l14_pool_b", 4):  "Contusion has no haemorrhage; the haematoma bleeds in the orbit",
 ("cms_e2l14_pool_b", 7):  "Anticoagulants, eye surgery or orbital varices",
 ("cms_e2l14_pool_b", 18): "A white-eyed blowout",
 ("cms_e2l14_pool_b", 19): "A facial trauma surgeon urgently",
 ("cms_e2l14_pool_b", 20): "To let orbital swelling settle first",
 ("cms_e2l14_pool_b", 22): "It often produces no symptoms of its own",
 ("cms_e2l14_pool_b", 23): "A cerebrospinal fluid leak",
 ("cms_e2l14_pool_c", 0):  "Entrapment with no soft tissue signs",
 ("cms_e2l14_pool_c", 1):  "Muscle entrapment",
 ("cms_e2l14_pool_c", 2):  "Young adult men, so eye protection matters most",
 ("cms_e2l14_pool_c", 3):  "A curtain, floaters, flashes and a field defect",
 ("cms_e2l14_pool_c", 4):  "Antiemetics, analgesia, tetanus and computed tomography",
 ("cms_e2l14_vig_a", 0):   "Shield the eye and call ophthalmology",
 ("cms_e2l14_vig_a", 3):   "Analgesia and a topical antibiotic",
 ("cms_e2l14_vig_a", 4):   "Evert the upper eyelid",
 ("cms_e2l14_vig_a", 7):   "Bed rest head-up and aminocaproic acid, to prevent a rebleed",
 ("cms_e2l14_vig_b", 1):   "Chronic tearing",
 ("cms_e2l14_vig_b", 2):   "Examine the globe underneath",
 ("cms_e2l14_vig_b", 8):   "Blowout fracture with inferior rectus entrapment",
 ("cms_e2l14_vig_b", 9):   "A white-eyed blowout",
 ("cms_e2l14_vig_b", 11):  "Ice, analgesia and antibiotics",
 ("cms_e2l14_vig_c", 1):   "Old incisions leave a permanent weak point",
 ("cms_e2l14_vig_c", 2):   "Later, once hyphema and inflammation settle",
 ("cms_e2l14_vig_c", 3):   "A topical antibacterial",
 ("cms_e2l14_vig_c", 4):   "A cotton-tipped applicator",
 ("cms_e2l14_vig_c", 5):   "Beta blockers and acetazolamide",
 ("cms_e2l14_vig_c", 6):   "Paralysing the ciliary body",
 ("cms_e2l14_vig_c", 7):   "A superficial skin cut sparing the margin",
 ("cms_e2l14_vig_c", 8):   "The septum acts as a wall",
 ("cms_e2l14_vig_c", 13):  "It is unlikely to improve, and surgery may worsen it",
 ("cms_e2l14_vig_c", 15):  "Ethmoid, frontal, temporal, sphenoid or occipital",
 ("cms_e2l14_vig_c", 16):  "Inspection, pupils, acuity and fields",
 ("cms_e2l14_vig_c", 17):  "Blunt or sharp, high or low velocity",
 ("cms_e2l14_vig_d", 0):   "Assess the globe beneath",
 ("cms_e2l14_vig_d", 1):   "Avoid aspirin, antiplatelets and straining",
 ("cms_e2l14_vig_d", 3):   "Subcutaneous emphysema",
 ("cms_e2l14_vig_d", 5):   "A positive dextrose stick and a halo sign",
 ("cms_e2l14_vig_d", 6):   "Periorbital haematoma",
 ("cms_e2l14_vig_d", 8):   "Slit lamp examination",
 ("cms_e2l14_vig_d", 9):   "Immediate surgical repair",
 ("cms_e2l14_vig_d", 10):  "Computed tomography without contrast",
 ("cms_e2l14_vig_d", 12):  "Vitreous detachment, then a retinal break",
 ("cms_e2l14_vig_d", 13):  "Measuring the pressure",
}

# --- distractors made MORE SPECIFIC, where the key's detail is the content --
# (module, question index, option index) -> replacement. Each stays wrong.
SPECIFIC = {
 ("cms_e2l14_pool_a", 11, 1): "The central cornea and the visual axis, where the wall is thinnest",
 ("cms_e2l14_pool_c", 4, 1):  "A mydriatic, tonometry and dilated fundoscopy of the retina",
}
