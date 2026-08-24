"""Length-bias remediation for CMS I Lecture 9 pool H (diagnostic testing).

Pool H ran 88 per cent gameable raw, the worst of any pool on this site, and
the reason is structural rather than careless. Every correct answer here is a
TECHNIQUE PLUS ITS CAVEAT -- "shave, punch or excisional, sampling sufficient
depth to separate in situ from invasive" -- set against distractors naming a
single technique. Trimming would delete the caveat, which IS the answer, so
every fix below is padding.

Keys are (index into POOL_H, index of the WRONG option). The applier asserts a
fix never lands on the correct answer.
"""
FIXES = {
 (0 , 1): "Shave biopsy only, since deeper sampling is thought to risk seeding the tumour into the dermis",
 (1 , 1): "Differentiation grade, Breslow thickness, ulceration, mitotic rate, margin status and lymphovascular invasion",
 (2 , 1): "Routine computed tomography of the chest, abdomen and pelvis in every newly diagnosed case",
 (4 , 2): "Magnetic resonance imaging is required whenever the lesion is anywhere on the face or scalp",
 (5 , 3): "Human immunodeficiency virus testing alone, since that establishes the whole context",
 (6 , 3): "Chronicity, treatment resistance, follicular hair loss and scarring alopecia of the scalp",
 (7 , 1): "Test for human immunodeficiency virus only if the patient reports risk factors on history, and otherwise assume seronegativity",
 (8 , 2): "Computed tomography of the chest in every newly diagnosed patient, regardless of respiratory symptoms, findings or stage",
 (10, 3): "Repeat the biopsy from the same site after treating it topically for two full weeks first",
 (11, 1): "Complete blood count alone, repeated at every single visit until the disease is judged to be stable by the treating specialist",
 (12, 3): "Response to a two-week course of a potent topical corticosteroid applied twice daily to all of the affected areas of the skin, assessed at review",
 (13, 2): "Failure of a single cryotherapy treatment, using a deep shave taken so as to sample the whole base of the treated lesion",
 (14, 3): "Whether the lesion sits on a field-cancerized site, because that guides how often the patient has to be brought back for surveillance review",
 (15, 2): "Observation with serial photographs for three months before any biopsy is taken or referral made",
}
