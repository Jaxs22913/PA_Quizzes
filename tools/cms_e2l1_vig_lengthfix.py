# -*- coding: utf-8 -*-
"""Length-bias fixes for the CMS I Exam 2 Lecture 1 VIGNETTE pool.

Same rule as everywhere else: PAD, NEVER TRIM. A vignette's correct answer is
usually a management action with its qualifier attached ("remove the lenses
WITHOUT PATCHING and arrange SAME-DAY evaluation") -- shortening it would delete
the qualifier, which is the whole teaching point. The runner-up distractor is
lengthened instead, and given enough detail to be a real alternative rather than
an obviously thin one.

KEYS ARE (question index, option index) INTO VIG_A + VIG_B, never the option
string. The partition asserts no fix targets a correct option.
"""
FIXES = {
 (0, 3):  "Start a topical corticosteroid drop and review him again in one week",
 (1, 3):  "Expect complete resolution within 24 hours without any specific treatment",
 (4, 1):  "Topical fluoroquinolone drops with a review appointment the following day",
 (6, 1):  "Take it on an empty stomach and lie down for an hour afterwards each dose",
 (7, 1):  "Repeat the conjunctival test in one week to confirm that it has cleared",
 (8, 1):  "It should clear within 24 to 48 hours of starting antibiotic drops",
 (11, 1): "Instil fluorescein and examine under cobalt blue light for a corneal dendrite",
 (12, 1): "Systemic corticosteroids started immediately at diagnosis",
 (14, 3): "He is at imminent risk of scleral perforation and needs surgery now",
 (15, 1): "Topical antibiotic drops with a review appointment in 48 hours",
 (17, 1): "Topical corticosteroid drops are the first-line treatment for this",
 (20, 2): "That the infection is herpes simplex rather than herpes zoster",
 (24, 2): "Topical antibiotic drops with review in 48 hours",
 (25, 2): "Conjunctival nucleic acid amplification testing for chlamydia",
 (26, 3): "Retinal detachment with vitreous haemorrhage",
 (28, 1): "No further action is needed now that the acute infection has cleared",
 (30, 2): "Reassessing him after 24 hours of empiric oral antibiotic treatment",
 (36, 1): "It will be completely cured by a single two-week course of lid hygiene",
 (51, 1): "Computed tomography of the orbits and sinuses with contrast",
 (52, 1): "Topical antibiotic drops applied four times daily",
 (53, 1): "Lubricating ointment used consistently will gradually correct the lid position",
 (55, 2): "Complete blood count with differential, plus blood cultures",
 (57, 3): "Order computed tomography of both orbits",
 (58, 2): "It will leave a permanent pigmented mark on the white of the eye",
 (59, 2): "Reassurance with no referral at all, since the lesion is benign",
 (60, 1): "Drops and sun protection will clear the lesion within a few months",
 (61, 1): "Reassure her, since chemosis is only a non-specific sign of irritation",
 (63, 1): "Computed tomography of the orbits with contrast before any examination",
 (64, 3): "Patch the eye and arrange same-day ophthalmology review afterwards",
 (65, 1): "Measure the intraocular pressure first to assess the extent of damage",
 (72, 1): "No precautions are needed, as bacterial conjunctivitis is not contagious",
 (75, 2): "The prognosis is better, because central ulcers are noticed and treated sooner",
}
