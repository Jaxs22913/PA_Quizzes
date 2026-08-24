"""Length-bias remediation for CMS I Lecture 9's corrective pool G.

Pool G ran 50 per cent gameable raw, which is what this pool's content makes
inevitable: it exists to cover `avoid`, `education` and `complication`, and
those answers are inherently clauses ("do not let photographing it delay
referral") set against distractors that are single objects. Padded, never
trimmed -- trimming would remove the qualifying clause that IS the answer.

Keys are (index into POOL_G, index of the WRONG option to rewrite). The applier
asserts a fix never lands on the correct answer.
"""
FIXES = {
 (0 , 1): "Photographing the concerning nail before any referral is made",
 (1 , 1): "Do not photograph it at all, because nail pigment renders inaccurately on a phone camera",
 (2 , 1): "Accelerated transformation into a systemic non-Hodgkin lymphoma",
 (3 , 1): "Oedema in Kaposi sarcoma is always caused by the antiretroviral therapy itself",
 (4 , 1): "That the treatment reactions of erythema and crusting were abnormal and should not recur",
 (5 , 1): "Kaposi sarcoma appearing for the first time several years after antiretroviral therapy begins",
 (6 , 1): "Those with classic Kaposi sarcoma, which is indolent",
 (7 , 1): "Nodal metastasis, which occurs in three to seven per cent of all treated cases",
 (8 , 1): "Complete margin-controlled surgery with clear histologic margins",
 (9 , 1): "That the lesions will always begin improving within the first two weeks of therapy",
 (10, 1): "Superficial spreading melanoma, the commonest subtype overall",
 (11, 1): "A single biopsy is definitive in nearly all cases, and the disease is self-limiting",
 (12, 1): "That inflammation means the drug has failed and that treatment should be stopped early",
 (13, 1): "Permanent hypopigmentation at every treated site, which is expected and harmless",
 (14, 1): "The CLINICAL list: superficial, nodular, pigmented and morpheaform subtypes",
 (15, 1): "Whether the patient has previously taken oral nicotinamide as chemoprevention for a prior lesion",
 (16, 1): "Rough, flat, flesh-coloured, and more apparent by touch than it is by sight",
 (17, 1): "Tanning bed use, fair skin that burns easily, male sex, and outdoor occupation without protection",
 (18, 1): "Chronic lymphocytic leukaemia, human immunodeficiency virus, and organ transplantation",
 (19, 1): "It may persist, progress, metastasise to nodes, or recur after treatment",
 (20, 1): "Patch and plaque disease worsen it; tumour-stage disease carries the better prognosis",
 (21, 1): "Classic disease, which regresses spontaneously after a course of local radiation",
 (22, 1): "Medical oncology, who direct all systemic and immunosuppressive decisions",
 (23, 1): "At least an annual skin examination alone, at an interval unchanged by immunosuppression",
}
