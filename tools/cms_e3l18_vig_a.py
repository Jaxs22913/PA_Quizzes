# -*- coding: utf-8 -*-
"""Lecture 18 vignette pool A -- Neoplasms and Neck Masses. Four options."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Neck masses and neoplasms: the triangles and lymph nodes of the neck; and the etiologies, "
      "epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, and prognosis")
C = lambda n: "CMS I Neoplasms and Neck Masses, Slide %d" % n

QUESTIONS = [

Q("Thyroglossal duct cyst", IO,
  "A 9-year-old girl has a painless midline neck swelling noticed after a cold. It rises when she "
  "swallows and again when she sticks out her tongue.",
  [["Thyroglossal duct cyst",
    "Correct. The thyroid descends from the foramen caecum through the hyoid during development, and "
    "a persistent tract tethers the cyst to the hyoid bone. Protruding the tongue pulls the hyoid "
    "upward and the cyst with it, which is the pathognomonic sign and no other neck mass "
    "reproduces it."],
   ["Dermoid cyst",
    "A dermoid is also midline and submental, which makes it the closest mimic, but it arises from "
    "entrapped epithelium with no hyoid attachment and therefore stays still on tongue protrusion."],
   ["Branchial cleft cyst",
    "A branchial cleft cyst is LATERAL, at the anterior border of the sternocleidomastoid. Position "
    "alone separates it, before any manoeuvre is performed."],
   ["Reactive lymph node",
    "Reactive nodes are lateral, often multiple, and regress within one to two weeks. A solitary "
    "midline mass tethered to the hyoid is not a lymph node."]], C(23)),

Q("Branchial cleft cyst", IO,
  "A 20-year-old man has a tender fluctuant swelling at the anterior border of the right "
  "sternocleidomastoid with overlying redness, appearing after a cold. He recalls a small painless "
  "lump there for years.",
  [["Control the infection, then excise the cyst and its tract",
    "Correct. The cyst is congenital and only declares itself when it becomes infected after an "
    "upper respiratory infection. Settling the infection first gives cleaner planes, and the "
    "definitive operation must take the TRACT as well as the cyst, because leaving the tract behind "
    "is what causes recurrence."],
   ["Incise and drain it now",
    "Incision and drainage is specifically avoided unless there is frank abscess, because it scars "
    "the planes and makes the definitive excision considerably harder. Needle aspiration is "
    "preferred even then."],
   ["Antibiotics alone, since the cyst will resolve",
    "Antibiotics settle the infection but the cyst is a congenital structure that does not "
    "disappear. It becomes infected again, which is why excision follows."],
   ["Excise it during the acute infection",
    "Operating on acutely inflamed oedematous tissue makes the tract hard to define and follow, "
    "raising the chance of leaving part of it behind."]], C(22)),

Q("Neck mass red flags", IO,
  "A 61-year-old man who smokes and drinks daily has a firm 3 centimetre neck mass present for six "
  "weeks. It is non-tender and barely mobile. There is no history of infection.",
  [["Fine needle aspiration biopsy",
    "Correct. Six red flags are present at once: no infectious origin, duration over two weeks, size "
    "over 1.5 centimetres, firm and non-tender with little mobility, age over 40, and tobacco with "
    "alcohol. Aspiration separates neoplasm from inflammation and carcinoma from lymphoma without "
    "spilling tumour into the neck."],
   ["A two-week course of antibiotics",
    "An antibiotic trial is common for a mass that might be inflammatory, but this one has no "
    "infective features at all and carries six independent malignancy flags. Two more weeks delays "
    "the diagnosis."],
   ["Excisional biopsy",
    "Excision is avoided as the first step because opening a malignant node seeds the neck and "
    "complicates the later surgical and radiotherapy fields."],
   ["Reassurance, as most neck masses are benign",
    "That holds under 40, where masses are usually inflammatory. In a smoker and drinker over 40, a "
    "new firm immobile mass is presumed malignant until proven otherwise."]], C(13)),

Q("Lymphangioma", IO,
  "An 18-month-old has a soft, doughy, non-tender, compressible mass in the posterior triangle. "
  "When a light is held against it the mass glows.",
  [["Lymphangioma",
    "Correct. Lymph spaces that fail to connect to the rest of the lymphatic system fill with clear "
    "lymph, and clear fluid transmits light. Positive transillumination is therefore the "
    "distinguishing bedside sign, and it also explains the soft, doughy, compressible texture."],
   ["Haemangioma",
    "A haemangioma is filled with blood rather than lymph, so it appears red or bluish and does not "
    "transilluminate. It also enlarges with crying, which a lymphangioma does not."],
   ["Teratoma",
    "A teratoma is firm rather than soft, contains mixed tissue with calcification on imaging, and "
    "does not transmit light."],
   ["Branchial cleft cyst",
    "A branchial cleft cyst sits laterally along the sternocleidomastoid and usually presents when "
    "infected in late childhood or early adulthood, tender and erythematous rather than soft and "
    "glowing."]], C(26)),

Q("Haemangioma", IO,
  "A 5-month-old has a red, soft, compressible neck mass that has grown since birth and enlarges "
  "when he cries. He feeds well and the airway is clear.",
  [["Observation",
    "Correct. Haemangiomas proliferate through the first year and then involute from 18 to 24 "
    "months, with about 90 per cent resolving without any therapy. Enlargement on crying reflects "
    "venous engorgement rather than progression, so with no functional compromise the right action "
    "is to explain the curve and watch."],
   ["Start propranolol now",
    "Propranolol is first line when treatment IS needed, but the indications are airway compromise, "
    "skin ulceration, dysphagia, thrombocytopenia or cardiac failure. None applies here."],
   ["Surgical excision",
    "Surgery is reserved for complications or for residual deformity after involution. Operating on "
    "a proliferating vascular lesion is technically difficult and unnecessary."],
   ["Sclerotherapy",
    "Sclerotherapy is used for lymphangiomas, whose lymphatic channels are the target. It is not the "
    "approach to a haemangioma that will resolve on its own."]], C(27)),

Q("Teratoma", IO,
  "A newborn has a large firm neck mass present at delivery. Imaging shows calcification within it "
  "and the baby has stridor.",
  [["Teratoma",
    "Correct. Head and neck teratomas account for about 3.5 per cent of all teratomas, originate "
    "from pluripotent cells and are usually noted at birth or in the first year. The mixed tissue "
    "types explain the calcification, and when large enough they cause respiratory compromise or "
    "dysphagia, so excision is needed."],
   ["Lymphangioma",
    "A lymphangioma is soft, doughy, compressible and transilluminates because it contains clear "
    "lymph. It neither feels firm nor calcifies."],
   ["Haemangioma",
    "A haemangioma appears in the first months rather than at delivery, is soft and compressible, "
    "and enlarges with crying. Calcification is not a feature."],
   ["Thyroglossal duct cyst",
    "A thyroglossal duct cyst is midline, moves with tongue protrusion, and typically presents in "
    "childhood when it becomes infected rather than as a calcified mass at birth."]], C(28)),

Q("Sternocleidomastoid tumour of infancy", IO,
  "A 7-week-old has a firm, painless, discrete mass within the right sternocleidomastoid and holds "
  "his head tilted toward that side.",
  [["Physical therapy, since most resolve spontaneously",
    "Correct. The lesion is associated with congenital torticollis and follows a set course: it "
    "enlarges for two to three months and then regresses over four to eight, with about 80 per cent "
    "resolving. Physical therapy prevents a fixed restrictive torticollis while that happens, and "
    "surgery is reserved for persistent cases."],
   ["Immediate surgical excision",
    "Operating on a lesion with an 80 per cent spontaneous resolution rate commits an infant to an "
    "unnecessary procedure and risks scarring the muscle further."],
   ["Fine needle aspiration to exclude malignancy",
    "Aspiration is the standard for a suspicious adult neck mass. A firm mass within the "
    "sternocleidomastoid of a neonate with torticollis has a characteristic picture that does not "
    "require tissue."],
   ["Observation with no intervention at all",
    "Watching is broadly right, but observation alone risks a fixed torticollis developing while the "
    "mass regresses. The therapy is the active ingredient."]], C(29)),

Q("Reactive lymphadenopathy", IO,
  "A 5-year-old has a 2 centimetre cervical node that appeared with a cold five weeks ago and has "
  "not changed since.",
  [["Investigate further, as it has passed the size and duration thresholds",
    "Correct. A node over 1 centimetre is abnormal, and reactive nodes regress within one to two "
    "weeks. Persistence beyond four to six weeks or continued enlargement is the stated trigger for "
    "investigation, with biopsy looking for fungal, granulomatous or neoplastic causes."],
   ["Continue observation, as viral nodes are common in children",
    "Observation was right for the first fortnight, and reactive adenopathy is indeed the commonest "
    "cause at this age. It stops being right once the node outlives the timescale that defines "
    "reactive."],
   ["Start empirical antibiotics",
    "There is no tenderness, erythema, fever or fluctuance, so there are no features of bacterial "
    "adenitis to treat. Antibiotics would only delay the investigation."],
   ["Reassure and discharge",
    "Discharging a node that has breached both thresholds removes the follow-up that would detect "
    "lymphoma, the named exception to the rule that childhood masses are inflammatory."]], C(31)),

Q("Atypical mycobacteria", IO,
  "A 4-year-old has a unilateral neck mass in the anterior triangle with brawny reddish-brown skin "
  "over it and mild tenderness. She is afebrile and well.",
  [["Atypical mycobacterial infection",
    "Correct. Non-tuberculous mycobacterial adenitis is a paediatric disease presenting as a "
    "unilateral mass in the anterior triangle or parotid with characteristically brawny "
    "reddish-brown overlying skin, in a child who is systemically well. Diagnosis is by acid-fast "
    "stain, culture and skin testing, and treatment is usually surgical excision."],
   ["Tuberculous adenitis",
    "Cervical tuberculosis affects adults more than children and produces diffuse BILATERAL "
    "lymphadenopathy. Unilateral disease with brawny skin in a well toddler is the atypical "
    "pattern."],
   ["Suppurative bacterial lymphadenitis",
    "Staphylococcal or streptococcal adenitis gives a hot, acutely tender node with fever and a "
    "throat or skin source over days. The indolent course and skin colour here do not fit."],
   ["Cat scratch disease",
    "Bartonella adenitis is common under 20 and affects preauricular and submandibular nodes, but it "
    "needs cat contact and produces fever and malaise rather than brawny skin."]], C(34)),

Q("Cat scratch disease", IO,
  "A 10-year-old boy has tender preauricular and submandibular nodes with low-grade fever and "
  "malaise for two weeks. The family recently got a kitten.",
  [["Serology with indirect fluorescent antibodies",
    "Correct. Cat scratch disease is caused by Bartonella henselae, is common under 20 years, and "
    "classically involves preauricular and submandibular nodes with fever and malaise after cat "
    "contact. Diagnosis is serologic using indirect fluorescent antibodies, and the illness is often "
    "self-limiting or treated with azithromycin."],
   ["Acid-fast stain and culture",
    "Acid-fast testing diagnoses atypical mycobacterial and tuberculous adenitis, which present with "
    "brawny unilateral disease in a child or diffuse bilateral disease in an adult. Neither is "
    "suggested by a new kitten."],
   ["Monospot and Epstein-Barr serology",
    "Mononucleosis causes cervical adenopathy with fever and malaise, so it is a fair differential, "
    "but it brings tonsillar exudate and splenomegaly and is not explained by cat exposure."],
   ["Toxoplasma serology",
    "Toxoplasmosis is also cat-associated, which makes it tempting, but the route is ingestion of "
    "oocysts in faeces or undercooked meat, and it gives more generalised adenopathy with sore "
    "throat and myalgias."]], C(34)),

Q("Suppurative lymphadenitis", IO,
  "A 30-year-old man has a fluctuant, tender submandibular mass with overlying erythema and fever "
  "after a sore throat. Three days of antibiotics have not settled it.",
  [["Fine needle aspiration or incision and drainage",
    "Correct. Suppurative bacterial lymphadenopathy is treated empirically against anaerobes and "
    "gram-positive organisms, but drainage follows when antibiotics fail. Fluctuance means there is "
    "a collection, and antibiotics penetrate an established abscess cavity poorly, so more of the "
    "same will not work."],
   ["Broaden the antibiotic and continue",
    "Escalating cover is reasonable alongside drainage, but relying on it alone repeats a strategy "
    "that has already failed for three days against a collection."],
   ["Excisional biopsy of the node",
    "Excisional biopsy is a diagnostic operation for a suspected neoplastic node. Here the diagnosis "
    "is clinically evident and what is needed is therapeutic drainage."],
   ["Observation, as most nodes settle on their own",
    "Reactive nodes do settle spontaneously, but a fluctuant tender node with fever that has "
    "resisted antibiotics is a collection and will not resolve unaided."]], C(33)),

Q("Thyroid nodule", IO,
  "A 50-year-old woman has a solitary thyroid nodule. Her thyroid-stimulating hormone is suppressed "
  "and she is mildly hyperthyroid.",
  [["Radionuclide scan before any biopsy",
    "Correct. A suppressed thyroid-stimulating hormone raises the possibility of an autonomously "
    "functioning nodule. The scan separates a hot nodule, which carries a low malignant risk and "
    "needs no biopsy, from a cold or warm one, which does. Scanning first avoids an unnecessary "
    "aspiration."],
   ["Immediate fine needle aspiration",
    "Aspiration is the default for most nodules, but not when the thyroid-stimulating hormone is "
    "low. Going straight to biopsy means sampling nodules the scan would have shown to be hot and "
    "benign."],
   ["Contrast computed tomography of the neck",
    "Iodine-containing contrast is avoided when thyroid cancer is a possibility, because the iodine "
    "load compromises later radioiodine treatment. Ultrasound is the correct imaging."],
   ["Start antithyroid medication and review in six months",
    "Treating the hyperthyroidism leaves the structural question unanswered, and six months is a "
    "long time to leave a nodule uncharacterised."]], C(41)),

Q("Papillary carcinoma", IO,
  "A 31-year-old woman's thyroid nodule biopsy shows a well-differentiated carcinoma of thyroid "
  "epithelial cells. She is told it is the commonest type with the best outlook.",
  [["Papillary carcinoma",
    "Correct. Papillary carcinoma is about 75 per cent of thyroid cancers, arises from thyroid "
    "epithelial cells, is commonest in young women and has the best prognosis. It tends to spread to "
    "local cervical nodes rather than distantly, which contributes to that outlook."],
   ["Follicular carcinoma",
    "Follicular carcinoma is second at about 16 per cent and also epithelial, but it spreads by "
    "blood to bone and lung, and the Hurthle cell variant is more aggressive."],
   ["Medullary carcinoma",
    "Medullary carcinoma is about 5 per cent and arises from parafollicular C cells rather than "
    "epithelial cells, producing calcitonin and carrying a familial association."],
   ["Anaplastic carcinoma",
    "Anaplastic carcinoma is about 1 per cent, occurs in the elderly, and is the most aggressive "
    "form with death in 6 to 36 months. It is neither common nor well differentiated."]], C(42)),

Q("Anaplastic carcinoma", IO,
  "An 80-year-old woman has a hard thyroid mass that has enlarged over six weeks with hoarseness "
  "and difficulty swallowing. Biopsy shows undifferentiated giant and spindle cells.",
  [["Anaplastic carcinoma",
    "Correct. Anaplastic carcinoma is about 1 per cent of thyroid cancers, occurs in elderly "
    "patients, and comprises small cell, giant cell and spindle cell types. It is the most "
    "aggressive form, with death typically in 6 to 36 months, and it is resistant to all treatment "
    "modalities, which is what the rapid growth and compressive symptoms reflect."],
   ["Papillary carcinoma",
    "Papillary carcinoma is the commonest and kindest type, occurring in young women and growing "
    "slowly. Neither the age, the six-week course nor the histology matches."],
   ["Primary thyroid lymphoma",
    "Thyroid lymphoma also enlarges rapidly in an older patient, so it belongs on the differential, "
    "but it is a non-Hodgkin B cell tumour on a Hashimoto background and responds to chemotherapy "
    "and radiation."],
   ["Medullary carcinoma",
    "Medullary carcinoma arises from calcitonin-producing C cells, runs a more insidious course and "
    "carries a familial association. Giant and spindle cell histology is not its picture."]],
  C(42)),

Q("Medullary carcinoma", IO,
  "A 44-year-old man is diagnosed with a thyroid carcinoma of parafollicular C cells. What "
  "additional step involves his family?",
  [["Screen relatives for multiple endocrine neoplasia",
    "Correct. Medullary carcinoma arises from calcitonin-producing C cells and carries a familial "
    "association with multiple endocrine neoplasia. Relatives may carry the same predisposition and "
    "can be identified before disease develops, so screening the family is part of managing the "
    "index case."],
   ["Screen relatives for Hashimoto thyroiditis",
    "Hashimoto is associated with primary thyroid LYMPHOMA. It clusters in families but carries no "
    "syndromic cancer risk that would justify systematic screening."],
   ["Screen relatives for papillary carcinoma",
    "Papillary carcinoma is the commonest thyroid cancer but is not the one with a defined familial "
    "endocrine syndrome driving management."],
   ["No family screening, as thyroid cancer is sporadic",
    "Most thyroid cancer is sporadic, which makes this a reasonable generalisation, but medullary "
    "disease is the specific exception."]], C(44)),

Q("Thyroid lymphoma", IO,
  "A 64-year-old woman with long-standing Hashimoto thyroiditis has a rapidly enlarging thyroid "
  "mass. Aspiration shows a lymphoid infiltrate that cannot be separated from her thyroiditis.",
  [["Proceed to open biopsy",
    "Correct. Primary thyroid lymphoma is usually a non-Hodgkin B cell tumour arising on a "
    "Hashimoto background, and both fill the gland with lymphocytes. Aspiration cytology cannot "
    "reliably distinguish a reactive infiltrate from a monoclonal one, so tissue architecture is "
    "needed, followed by lymphoma staging."],
   ["Accept the result as Hashimoto and continue replacement",
    "Accepting an inconclusive result as benign in a gland that is rapidly enlarging ignores the "
    "clinical change that prompted the biopsy in the first place."],
   ["Total thyroidectomy",
    "Surgery is the mainstay for thyroid carcinoma but not for lymphoma, which is treated with "
    "chemotherapy and radiation. Operating first risks a major procedure that does not treat the "
    "disease."],
   ["Repeat the aspiration with more passes",
    "More passes yield more of the same cells and the same interpretive problem, because the "
    "limitation is architectural rather than one of sample size."]], C(45)),
]
