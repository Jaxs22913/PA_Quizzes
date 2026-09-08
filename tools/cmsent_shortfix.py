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

 # Second pass, after the pools reached 250. Same principle: the reason belongs
 # in the explanation, not in the option text.
 ("cmsent_l18b_pool", 10):  "Follicular carcinoma",
 ("cmsent_l17c_pool", 1):   "Ten days or more, double worsening, or unilateral pain",
 ("cmsent_topup_pool", 20): "Baseline and serial audiometry",
 ("cmsent_l19c_pool", 4):   "Anterior two thirds of tongue against posterior third",
 ("cmsent_l17c_pool", 5):   "Granulomatosis with polyangiitis, or syphilis",
 ("cmsent_topup2_pool", 13):"Conductive anosmia from obstruction",
 ("cmsent_l19c_pool", 9):   "Chronic granulomatous sialadenitis",
 ("cmsent_l19b_pool", 4):   "Computed tomography most sensitive, sialography most accurate",
 ("cmsent_l18c_pool", 5):   "Trimethoprim-sulfamethoxazole",
 ("cmsent_l15c_pool", 9):   "Imaging of the temporal bone",
 ("cmsent_l18b_pool", 14):  "Under 40 most are inflammatory, except Hodgkin lymphoma",
 ("cmsent_l17b_pool", 3):   "Pinch the soft part for ten minutes, leaning forward",
 ("cmsent_l19b_pool", 12):  "Gingivitis, which is reversible",
 ("cmsent_l17c_pool", 4):   "A parent-delivered positive pressure blow",
 ("cmsent_l16b_pool", 1):   "A stiff mechanism, as in ossicular fixation",
 ("cmsent_l19c_pool", 6):   "Referred otalgia from cranial nerve involvement",
 ("cmsent_topup2_pool", 5): "Scanty suggests canal, mucoid suggests middle ear",
 ("cmsent_l16c_pool", 11):  "Untreated loss brings withdrawal and cognitive decline",
 ("cmsent_l15c_pool", 7):   "Mucosal oedema obstructs the eustachian tube",
 ("cmsent_l17b_pool", 1):   "Chronic rhinosinusitis, beyond 12 weeks",
 ("cmsent_l19b_pool", 1):   "It carries a 1 to 4 per cent risk of carcinoma",
 ("cmsent_l18c_pool", 9):   "Thyroglossal duct cyst",
 ("cmsent_topup2_pool", 14):"Once the swelling settles, within about two weeks",
 ("cmsent_l18b_pool", 5):   "Physical therapy, as most resolve",
 ("cmsent_l19b_pool", 7):   "Unilateral paralysis from recurrent laryngeal injury",
 ("cmsent_topup2_pool", 11):"Allergic fungal sinusitis 85%, asthma 20 to 50%",
 ("cmsent_topup2_pool", 6): "Add systemic antibiotics",
 ("cmsent_l16c_pool", 15):  "Headache, ataxia, or focal neurological signs",
 ("cmsent_l15c_pool", 12):  "Move the tragus or pinna",
 ("cmsent_l15c_pool", 5):   "Prompt repair with a pressure dressing",
 ("cmsent_l17b_pool", 11):  "Saddle nose deformity from cartilage necrosis",
 ("cmsent_topup2_pool", 0): "The child's tube is shorter, wider and flatter",
 ("cmsent_l17c_pool", 8):   "Recurrence is expected after surgery",
 ("cmsent_l17b_pool", 2):   "Invasive fungal sinusitis, needing debridement",
}
