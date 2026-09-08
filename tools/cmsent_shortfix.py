# -*- coding: utf-8 -*-
"""Shorten over-long CORRECT answers in the ENT master pools.

Jaxon, 2026-08-30: "SHORTEN THE ANSWER, never pad distractors." Writing deep
per-option explanations made this worse rather than better -- once you are
thinking in reasons, the reason leaks into the option text and the key ends up
carrying a clause the distractors do not have. The raw pools came in at 36%.

Each entry replaces the key's option TEXT only. Nothing is deleted: the clause
that comes out was almost always duplicating what the key's own explanation
already says at length, which is where it belongs.

    SHORT[(pool, index)] = "shorter key"
"""

SHORT = {
 ("cmsent_l15_pool", 0):   "Topical ciprofloxacin-dexamethasone",
 ("cmsent_l15_pool", 5):   "Keep the ear dry and review",
 ("cmsent_l15_pool", 9):   "Observation",
 ("cmsent_l15b_pool", 0):  "Drainage and a pressure dressing",
 ("cmsent_l15b_pool", 5):  "Chronic otitis media",
 ("cmsent_l15b_pool", 6):  "Haemotympanum from barotrauma",
 ("cmsent_l15b_pool", 7):  "Retained foreign body with infection",
 ("cmsent_l15b_pool", 9):  "It has reached the skull base and facial nerve",
 ("cmsent_l15b_pool", 11): "Place an ear wick to carry the drops in",
 ("cmsent_l16_pool", 0):   "Ototoxicity from the diuretic",
 ("cmsent_l16_pool", 1):   "Positional vertigo",
 ("cmsent_l16_pool", 4):   "Urgent referral for sudden sensorineural loss",
 ("cmsent_l16_pool", 5):   "Magnetic resonance imaging with gadolinium",
 ("cmsent_l16_pool", 14):  "Syphilis, which mimics Meniere",
 ("cmsent_l17_pool", 0):   "Amoxicillin-clavulanate twice daily",
 ("cmsent_l17_pool", 5):   "Anterior epistaxis, managed conservatively",
 ("cmsent_l17_pool", 6):   "Drain it now",
 ("cmsent_l17_pool", 11):  "Chronic ischaemia from a topical agent",
 ("cmsent_l18_pool", 6):   "Lymphangioma",
 ("cmsent_l18_pool", 7):   "Observation",
 ("cmsent_l18_pool", 13):  "Serology for Bartonella henselae",
 ("cmsent_l19_pool", 4):   "Avoid contact sport for about a month",
 ("cmsent_l19_pool", 5):   "Submandibular sialolithiasis",
 ("cmsent_l19_pool", 8):   "Erythroplakia",
 ("cmsent_l19_pool", 9):   "Secure the airway, then antibiotics",
 ("cmsent_l19_pool", 10):  "Retropharyngeal abscess",
 ("cmsent_l19_pool", 13):  "Microlaryngoscopic excision",
 ("cmsent_l19_pool", 15):  "Rehydration and antistaphylococcal antibiotics",
 ("cmsent_l19_pool", 16):  "Diphtheria antitoxin plus antibiotics",
}
