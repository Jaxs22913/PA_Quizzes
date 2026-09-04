# -*- coding: utf-8 -*-
"""Length-bias fixes for the Lecture 17 pools.

Applied by cms_e3_partition.py BEFORE anything is measured, keyed by
(module, question index) so a fix survives the pools being combined in a
different order.

SHORTEN THE KEY -- never pad the distractors. Jaxon, 2026-08-30: padding
treats the symptom and bloats every option. The rationale that comes out of a
key belongs in the explanation, which is where the reference items put it.

WHERE THE KEY IS A FIXED LIST OR PROPER NAME it cannot be shortened without
losing the fact, so the DISTRACTORS are re-chosen at comparable length instead
-- that is what SPECIFIC does, and it asserts it never touches option 0.
"""
KEYS = {
 ("cms_e3l17_pool_a", 3):  "Half to two per cent",
 ("cms_e3l17_pool_a", 7):  "Fungi",
 ("cms_e3l17_pool_a", 8):  "Polymicrobial",
 ("cms_e3l17_pool_a", 10): "Worsening after initial improvement",
 ("cms_e3l17_pool_a", 19): "Clinical findings match its accuracy",
 ("cms_e3l17_pool_a", 20): "Recurrence or treatment failure",
 ("cms_e3l17_pool_a", 22): "Decongestants, lavage and steroids",
 ("cms_e3l17_pool_a", 24): "Doxycycline",
 ("cms_e3l17_pool_a", 25): "Oseltamivir for five days",
 ("cms_e3l17_pool_a", 26): "ENT referral for surgery",
 ("cms_e3l17_pool_a", 27): "Diplopia and periorbital swelling",
 ("cms_e3l17_pool_a", 29): "Impaired mucociliary clearance",
 ("cms_e3l17_pool_a", 30): "Steroids plus amoxicillin/clavulanate",
 ("cms_e3l17_pool_a", 31): "Extent, anatomy and response",
 ("cms_e3l17_pool_a", 32): "Endoscopic surgery alone",
 ("cms_e3l17_pool_a", 34): "Thick, like peanut butter",
 ("cms_e3l17_pool_b", 0):  "Displaced to one side",
 ("cms_e3l17_pool_b", 1):  "Sleep apnoea, snoring and nosebleeds",
 ("cms_e3l17_pool_b", 3):  "Intranasal steroids and cocaine",
 ("cms_e3l17_pool_b", 6):  "Treat the underlying cause",
 ("cms_e3l17_pool_b", 7):  "Under the perichondrium",
 ("cms_e3l17_pool_b", 9):  "Drainage under anaesthesia",
 ("cms_e3l17_pool_b", 10): "Under ten, and forty-five to sixty-five",
 ("cms_e3l17_pool_b", 11): "The patient's own finger",
 ("cms_e3l17_pool_b", 14): "Aspiration",
 ("cms_e3l17_pool_b", 17): "Sitting up, leaning forward",
 ("cms_e3l17_pool_b", 18): "Only if anticoagulated",
 ("cms_e3l17_pool_b", 19): "Crossmatch and two large-bore lines",
 ("cms_e3l17_pool_b", 21): "Unilateral foul-smelling discharge",
 ("cms_e3l17_pool_b", 22): "Under the inferior turbinate",
 ("cms_e3l17_pool_b", 24): "Bridge only, patent, straight, no haematoma",
 ("cms_e3l17_pool_b", 32): "Temporary &mdash; they recur",
 ("cms_e3l17_pool_b", 33): "Clear discharge, bluish mucosa",
 ("cms_e3l17_pool_b", 34): "Antihistamine, leukotriene, steroid",
 ("cms_e3l17_pool_b", 35): "It creates the environment for infection",
 ("cms_e3l17_pool_b", 37): "Southern China and Southeast Asia",
 ("cms_e3l17_pool_b", 38): "Neck mass with cranial nerve signs",
 ("cms_e3l17_pool_b", 39): "Endoscopic guided biopsy",
 ("cms_e3l17_vig_a", 0):  "Symptomatic treatment alone",
 ("cms_e3l17_vig_a", 4):  "Urgent computed tomography",
 ("cms_e3l17_vig_a", 8):  "Steroids, antibiotics and ENT referral",
 ("cms_e3l17_vig_a", 14): "Drainage under anaesthesia",
 ("cms_e3l17_vig_a", 18): "Oxymetazoline, then pinch ten minutes",
 ("cms_e3l17_vig_a", 20): "Clotting study, crossmatch and count",
 ("cms_e3l17_vig_a", 22): "Oseltamivir for five days",
 ("cms_e3l17_vig_a", 23): "It creates the environment for infection",
 ("cms_e3l17_vig_a", 24): "Diagnosis, cause, treatment and referral",
 ("cms_e3l17_vig_b", 2):  "A wire loop or suction",
 ("cms_e3l17_vig_b", 5):  "Cystic fibrosis and asthma",
 ("cms_e3l17_vig_b", 7):  "Temporary &mdash; they recur",
 ("cms_e3l17_vig_b", 8):  "Antihistamine, leukotriene, steroid",
 ("cms_e3l17_vig_b", 10): "Most need two or more medicines",
 ("cms_e3l17_vig_b", 13): "Epstein-Barr virus and smoking",
 ("cms_e3l17_vig_b", 14): "It suggests bacterial infection",
 ("cms_e3l17_vig_b", 15): "No imaging can separate them",
 ("cms_e3l17_vig_b", 16): "It argues against bacterial infection",
 ("cms_e3l17_vig_b", 17): "Endoscopic tissue for culture",
 ("cms_e3l17_vig_b", 21): "Packing or a balloon catheter",
 ("cms_e3l17_vig_b", 23): "Treat the cause; else septoplasty",
}

# (module, question index, OPTION index) -> replacement distractor text.
# Only used where the key is a fixed name or list that cannot be shortened, so
# the distractors are brought up to a comparable length instead.
SPECIFIC = {
 # "S. pneumoniae, nontypable H. influenzae and, in children, M. catarrhalis"
 # is the fact itself and cannot be trimmed; the distractors were short.
 ("cms_e3l17_pool_a", 6, 4): "Mycobacterium tuberculosis, Nocardia and Actinomyces species",
 # "Amoxicillin with clavulanate" against one-word drug names.
 ("cms_e3l17_pool_a", 23, 1): "Vancomycin given intravenously",
 ("cms_e3l17_pool_a", 23, 2): "Metronidazole given orally",
 # "Granulomatosis with polyangiitis" against short disease names.
 ("cms_e3l17_vig_a", 13, 2): "Secondary syphilis, long treated",
 # "Aspirin-exacerbated respiratory disease" against short syndrome names.
 ("cms_e3l17_vig_b", 4, 3): "Cystic fibrosis presenting late",
 # "Orbital and midface fractures" against single-bone names.
 ("cms_e3l17_vig_b", 19, 1): "Rib fractures from the same blow",
 # "Allergy, for skin testing" against single specialty names.
 ("cms_e3l17_vig_b", 24, 1): "Neurology, for the headache",
 ("cms_e3l17_vig_b", 24, 2): "Rheumatology, for vasculitis",
}
