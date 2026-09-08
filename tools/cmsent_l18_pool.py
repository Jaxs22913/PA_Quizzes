# -*- coding: utf-8 -*-
"""Lecture 18 questions for the ENT master exams -- Neoplasms and Neck Masses."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "CMS I Neoplasms and Neck Masses"
IO = ("Neck masses and neoplasms: the triangles and lymph nodes of the neck; and the etiologies, "
      "epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, and prognosis of common neck masses, "
      "vascular tumors, and benign and malignant neoplasms")

QUESTIONS = [

Q("Thyroglossal duct cyst", IO,
  "A 14-year-old girl has a painless swelling in the midline of the anterior neck, noticed after a "
  "cold. On examination the mass moves upward when she swallows and again when she protrudes her "
  "tongue.",
  [["Thyroglossal duct cyst",
    "Correct. The thyroid descends from the foramen caecum at the tongue base through the hyoid "
    "bone during development, and a persistent tract leaves a midline cyst attached to the hyoid. "
    "That attachment is why the mass rises with swallowing AND with tongue protrusion, which is the "
    "pathognomonic sign and the reason the Sistrunk operation removes the central hyoid with it."],
   ["Branchial cleft cyst",
    "A branchial cleft cyst is LATERAL, sitting at the anterior border of the sternocleidomastoid, "
    "and has no attachment to the hyoid, so it does not move with tongue protrusion. Position alone "
    "separates the two."],
   ["Dermoid cyst",
    "A dermoid is also midline and submental, so it is the closest mimic, but it arises from "
    "entrapped epithelium with no connection to the hyoid or the tongue base and therefore does not "
    "elevate on tongue protrusion."],
   ["Reactive cervical lymphadenopathy",
    "Reactive nodes are lateral, sit in the cervical chains, are often multiple and tender, and "
    "regress over one to two weeks. A solitary midline mass that moves with the tongue is not a "
    "lymph node."]],
  "diagnosis", D, 23),

Q("Branchial cleft cyst", IO,
  "A 21-year-old man has a tender, fluctuant swelling at the anterior border of the right "
  "sternocleidomastoid with overlying erythema, which appeared after an upper respiratory "
  "infection. He recalls a small painless lump in the same place for years.",
  [["Control the infection first, then excise the cyst and its tract",
    "Correct. A branchial cleft cyst arises from pharyngobranchial ducts that failed to obliterate, "
    "and it usually declares itself when it becomes infected after an upper respiratory infection. "
    "The infection is settled first, then the cyst AND its tract are excised, because leaving the "
    "tract behind is what causes recurrence."],
   ["Incision and drainage now, then excision later",
    "Incision and drainage is specifically avoided unless there is frank abscess, because it scars "
    "the tissue planes and makes the definitive excision considerably harder. Even when a collection "
    "must be decompressed, needle aspiration is preferred."],
   ["Excise it immediately during the acute infection",
    "Operating on acutely infected, oedematous tissue makes it difficult to define and follow the "
    "tract, which raises the risk of leaving part of it behind. Controlling the infection first "
    "gives a cleaner and more complete excision."],
   ["Antibiotics alone, since the cyst will resolve once the infection settles",
    "Antibiotics settle the infection but the cyst itself is a congenital structure that does not "
    "disappear. It will simply become infected again, which is why definitive excision follows."]],
  "treatment", D, 22),

Q("Neck mass red flags", IO,
  "A 58-year-old man who smokes and drinks daily has a firm, non-tender neck mass that has been "
  "present for six weeks and measures 3 centimetres. It is immobile and there is no history of "
  "infection.",
  [["Fine needle aspiration biopsy",
    "Correct. Every red flag is present: no infectious origin, duration "
    "over two weeks, size over 1.5 centimetres, firm and non-tender with little mobility, age over "
    "40, and tobacco with alcohol. Fine needle aspiration is the standard of care because it "
    "separates neoplasm from inflammation and carcinoma from lymphoma without spilling tumour."],
   ["Excisional biopsy of the node",
    "Excisional biopsy is specifically avoided as the first step in a suspected malignant neck mass, "
    "because opening the node spills tumour cells into the neck and complicates definitive surgery "
    "and radiotherapy fields afterwards."],
   ["A two-week course of antibiotics and reassessment",
    "A trial of antibiotics is common practice for a mass that might be inflammatory, but this one "
    "has no infectious features at all and carries six independent malignancy red flags. Two more "
    "weeks delays a cancer diagnosis in a high-risk patient."],
   ["Reassurance, as most neck masses are benign",
    "That is true under the age of 40, where masses are usually inflammatory. It is the wrong rule "
    "for a 58-year-old smoker and drinker, in whom a new firm immobile mass should be presumed "
    "malignant until proven otherwise."]],
  "next step", D, 18),

Q("Thyroid nodule", IO,
  "A 52-year-old woman has a solitary thyroid nodule. Her thyroid-stimulating hormone is "
  "suppressed. She is clinically mildly hyperthyroid.",
  [["Radionuclide scan with technetium before any biopsy",
    "Correct. A suppressed thyroid-stimulating hormone means the nodule may be autonomously "
    "producing hormone. A scan distinguishes a hot, hyperfunctioning nodule, which carries a low "
    "malignant risk and needs no biopsy, from a cold or warm nodule, which does. Doing the scan "
    "first avoids an unnecessary aspiration in the hot group."],
   ["Immediate fine needle aspiration of the nodule",
    "Aspiration is the diagnostic procedure of choice for most nodules, but not when the "
    "thyroid-stimulating hormone is low. Going straight to biopsy in a hyperthyroid patient means "
    "sampling nodules that the scan would have shown to be hot and benign."],
   ["Start antithyroid medication and review in six months",
    "Treating the hyperthyroidism addresses the hormonal problem while leaving the structural "
    "question unanswered. The nodule still has to be characterised, and six months is a long time "
    "to leave that open."],
   ["Contrast computed tomography of the neck",
    "Iodine-containing contrast is specifically avoided when thyroid cancer is in question, because "
    "the iodine load compromises subsequent radioiodine treatment. Ultrasound is the correct imaging "
    "modality for a thyroid nodule."]],
  "next step", D, 41),

Q("Thyroid carcinoma", IO,
  "A 34-year-old woman has a thyroid nodule. Fine needle aspiration shows a well-differentiated "
  "carcinoma of thyroid epithelial cells. She is told this is the commonest type and has the best "
  "outlook.",
  [["Papillary carcinoma",
    "Correct. Papillary carcinoma accounts for about 75 per cent of thyroid cancers, arises from "
    "thyroid epithelial cells, is commonest in young women, and has the best prognosis of the four "
    "types. Its tendency is to spread to local cervical lymph nodes rather than haematogenously, "
    "which is part of why the outlook is favourable."],
   ["Follicular carcinoma",
    "Follicular carcinoma is the second commonest at about 16 per cent and also arises from "
    "epithelial cells, but it characteristically spreads by BLOOD to bone and lung, and the Hurthle "
    "cell variant is more aggressive with higher recurrence."],
   ["Medullary carcinoma",
    "Medullary carcinoma is about 5 per cent and arises from parafollicular C cells rather than "
    "epithelial cells, producing calcitonin. It is more insidious, most likely to metastasise, and "
    "carries a familial association with multiple endocrine neoplasia."],
   ["Anaplastic carcinoma",
    "Anaplastic carcinoma is about 1 per cent, occurs in elderly patients, is the most aggressive "
    "form with death typically in 6 to 36 months, and is resistant to all treatment modalities. It "
    "is neither common nor well-differentiated."]],
  "diagnosis", D, 42),

Q("Medullary thyroid carcinoma", IO,
  "A 41-year-old man is diagnosed with a thyroid carcinoma arising from parafollicular C cells. "
  "Beyond his own treatment, the clinician arranges an additional action involving his relatives.",
  [["Screen family members for multiple endocrine neoplasia",
    "Correct. Medullary carcinoma arises from the calcitonin-producing C cells and carries a "
    "familial association with multiple endocrine neoplasia. Because relatives may carry the same "
    "predisposition and can be identified before disease develops, screening the family is part of "
    "the management of the index case rather than an optional extra."],
   ["Screen family members for Hashimoto thyroiditis",
    "Hashimoto is associated with primary thyroid lymphoma rather than with medullary carcinoma, "
    "and although it clusters in families it does not carry the syndromic cancer risk that justifies "
    "systematic screening of relatives."],
   ["Screen family members for papillary carcinoma",
    "Papillary carcinoma is the commonest thyroid cancer but is not the one with a defined familial "
    "endocrine syndrome driving management. It is medullary disease that triggers the family "
    "screening pathway."],
   ["No family screening, since thyroid cancer is not heritable",
    "Most thyroid cancer is sporadic, which makes this a reasonable-sounding generalisation, but "
    "medullary carcinoma is the specific exception and the reason the cell of origin matters "
    "clinically."]],
  "next step", D, 44),

Q("Lymphangioma", IO,
  "A 2-year-old girl has a soft, doughy, non-tender, compressible mass in the posterior triangle of "
  "the neck. When a light is held against it, the mass transilluminates.",
  [["Lymphangioma (cystic hygroma)",
    "Correct. A lymphangioma is a congenital malformation in which lymph spaces fail to connect to "
    "the rest of the lymphatic system, so it fills with clear lymph. Clear fluid is what allows light "
    "to pass through, which is why positive transillumination is its distinguishing bedside sign, "
    "and why the mass feels soft, doughy and compressible."],
   ["Haemangioma",
    "A haemangioma is filled with blood rather than lymph, so it appears red or bluish and does not "
    "transilluminate. It also enlarges with crying or straining, which a lymphangioma does not."],
   ["Teratoma",
    "A teratoma is firm rather than soft and compressible, often shows calcification on imaging, and "
    "does not transmit light. It is usually noted at birth or in the first year."],
   ["Branchial cleft cyst",
    "A branchial cleft cyst is lateral at the sternocleidomastoid border and usually presents when "
    "infected, tender and erythematous, in late childhood or early adulthood rather than as a soft "
    "transilluminating mass in a toddler."]],
  "diagnosis", D, 26),

Q("Haemangioma", IO,
  "A 6-month-old has a red, soft, compressible mass on the neck that has grown since birth and "
  "becomes larger and more prominent when he cries. He is feeding well, and the airway is not "
  "compromised.",
  [["Observation, since about 90 per cent involute without treatment",
    "Correct. Haemangiomas grow rapidly through the first year and then begin to involute at 18 to "
    "24 months, and roughly 90 per cent resolve without any therapy. Enlargement with crying "
    "reflects venous engorgement in a vascular malformation rather than progression, so observation "
    "is appropriate when there is no functional compromise."],
   ["Start propranolol now",
    "Propranolol is the first-line drug, but it is reserved for lesions causing airway compromise, "
    "skin ulceration, dysphagia, thrombocytopenia or cardiac failure. Treating an asymptomatic "
    "lesion exposes an infant to beta blockade for a process that would resolve on its own."],
   ["Surgical excision",
    "Surgery is reserved for complications or for residual deformity after involution has finished. "
    "Operating during the proliferative phase on a highly vascular lesion is technically difficult "
    "and unnecessary when the natural history is resolution."],
   ["Systemic corticosteroids",
    "Steroids are a second-line option after propranolol and are used only when treatment is "
    "actually indicated. Their systemic effects in an infant are not justified for a lesion that "
    "does not need treating."]],
  "treatment", D, 27),

Q("Atypical mycobacterial adenitis", IO,
  "A 3-year-old has a unilateral neck mass in the anterior triangle with overlying brawny, "
  "reddish-brown skin, induration and mild tenderness. She is systemically well and afebrile.",
  [["Atypical mycobacterial infection",
    "Correct. Non-tuberculous mycobacterial adenitis is a paediatric disease that presents as a "
    "unilateral mass in the anterior triangle or parotid region with characteristic brawny "
    "reddish-brown skin discolouration over it, in a child who is otherwise well. Diagnosis is by "
    "acid-fast stain or culture with skin testing, and treatment is usually surgical excision."],
   ["Tuberculous adenitis",
    "Cervical tuberculosis, or scrofula, affects adults more than children and produces DIFFUSE and "
    "BILATERAL lymphadenopathy. Unilateral disease with brawny skin in a well toddler is the "
    "atypical pattern, not the tuberculous one."],
   ["Suppurative bacterial lymphadenitis",
    "Staphylococcal or streptococcal adenitis produces a hot, acutely tender node with fever and "
    "often a sore throat or skin source, developing over days. The indolent course and the skin "
    "colour described do not fit."],
   ["Cat scratch disease",
    "Bartonella adenitis is common under 20 and does affect preauricular and submandibular nodes, "
    "but it requires cat contact and gives fever and malaise rather than the brawny skin change "
    "that characterises atypical mycobacteria."]],
  "diagnosis", D, 34),

Q("Anaplastic thyroid carcinoma", IO,
  "An 81-year-old woman has a rapidly enlarging hard thyroid mass with hoarseness and difficulty "
  "swallowing that has developed over six weeks. Biopsy shows undifferentiated giant and spindle "
  "cells.",
  [["Anaplastic carcinoma, with a prognosis measured in months",
    "Correct. Anaplastic carcinoma is about 1 per cent of thyroid cancers, occurs in elderly "
    "patients, and is composed of small cell, giant cell and spindle cell types. It is the most "
    "aggressive form, typically causing death in 6 to 36 months, and is resistant to all treatment "
    "modalities, which is why the rapid growth and compressive symptoms are characteristic."],
   ["Papillary carcinoma, with an excellent prognosis",
    "Papillary carcinoma is the commonest and kindest type, occurring in young women and growing "
    "slowly. Neither the age, the six-week course, nor the undifferentiated histology matches it."],
   ["Primary thyroid lymphoma arising in Hashimoto thyroiditis",
    "Thyroid lymphoma also enlarges quickly in an older patient, so it belongs on the list, but it "
    "is a non-Hodgkin B cell tumour on a background of Hashimoto and responds to chemotherapy and "
    "radiation rather than being treatment-resistant."],
   ["Medullary carcinoma",
    "Medullary carcinoma arises from calcitonin-producing C cells, is more insidious in its course, "
    "and carries a familial association. It does not show giant and spindle cell histology or this "
    "fulminant tempo."]],
  "diagnosis", D, 42),

Q("Primary thyroid lymphoma", IO,
  "A 66-year-old woman with long-standing Hashimoto thyroiditis develops a rapidly enlarging "
  "thyroid mass. Fine needle aspiration is reported as showing a lymphoid infiltrate that cannot be "
  "confidently distinguished from her known thyroiditis.",
  [["Proceed to open biopsy, because aspiration cannot separate lymphoma from Hashimoto",
    "Correct. Primary thyroid lymphoma is most often a non-Hodgkin B cell tumour arising on a "
    "background of Hashimoto thyroiditis, and both conditions fill the gland with lymphocytes. "
    "Aspiration cytology cannot reliably tell a reactive infiltrate from a monoclonal one, so tissue "
    "architecture is needed, followed by lymphoma staging."],
   ["Accept the result as Hashimoto and continue thyroid hormone replacement",
    "Accepting an inconclusive result as benign in a gland that is rapidly enlarging ignores the "
    "clinical change that prompted the biopsy. The whole reason the distinction is difficult is that "
    "the two coexist."],
   ["Total thyroidectomy",
    "Surgery is the mainstay for the thyroid carcinomas but not for lymphoma, which is managed with "
    "chemotherapy and radiation. Removing the gland before the diagnosis is established risks a "
    "major operation that does not treat the disease."],
   ["Repeat the fine needle aspiration with more passes",
    "More passes give more of the same cells and the same interpretive problem, because the "
    "limitation is architectural rather than one of sample size. Repeating it delays a diagnosis "
    "that needs a different kind of specimen."]],
  "next step", D, 45),

Q("Neck anatomy", IO,
  "A surgeon is operating in the triangle bounded by the sternocleidomastoid behind, the posterior "
  "belly of digastric above, and the omohyoid below.",
  [["The carotid arteries, internal jugular vein and vagus nerve",
    "Correct. Those boundaries define the carotid triangle, which houses the carotid arteries, the "
    "internal jugular vein and the vagus nerve. Knowing the contents from the boundaries is the "
    "point of the triangle scheme: it converts a set of surface landmarks into a prediction about "
    "what lies underneath."],
   ["The thyroid, parathyroid, larynx and trachea",
    "Those are the contents of the muscular triangle, which lies between the omohyoid above, the "
    "sternocleidomastoid below and the midline in front. It is a different triangle of the same "
    "anterior group."],
   ["The submandibular gland, hypoglossal nerve and facial vessels",
    "Those sit in the digastric or submandibular triangle, bounded by the mandible above and the two "
    "bellies of digastric. The boundaries given do not include the mandible."],
   ["The brachial plexus and subclavian artery",
    "Those are in the supraclavicular triangle of the POSTERIOR group, above the middle of the "
    "clavicle. The boundaries described are all anterior triangle structures."]],
  "finding", D, 6),

Q("Lymphatic drainage", IO,
  "A patient has an infected palatine tonsil. A specific group of deep cervical nodes is expected "
  "to enlarge.",
  [["The jugulodigastric nodes",
    "Correct. The deep cervical chain receives drainage from all the regional node groups, and two "
    "members of it have named territories. The jugulodigastric node drains the palatine tonsil, "
    "which is why tonsillitis characteristically produces a tender node high in the jugular chain "
    "just below the angle of the jaw."],
   ["The juguloomohyoid nodes",
    "The juguloomohyoid node is the other named deep cervical node, and its territory is the TONGUE "
    "rather than the tonsil. The pairing is easy to reverse, which is why both are worth learning "
    "together."],
   ["The occipital nodes",
    "Occipital nodes drain the posterior scalp, along with the retroauricular and parotid nodes that "
    "take the auricle and middle ear. They have no tonsillar territory."],
   ["The submandibular nodes",
    "Submandibular nodes drain the face, sinuses, mouth and tongue, so they are involved in oral "
    "disease broadly, but the tonsil drains specifically to the jugulodigastric group."]],
  "finding", D, 12),

Q("Cat scratch disease", IO,
  "A 12-year-old boy has a tender preauricular and submandibular lymphadenopathy with low-grade "
  "fever and malaise for two weeks. He has a new kitten at home.",
  [["Serologic testing with indirect fluorescent antibodies for Bartonella henselae",
    "Correct. Cat scratch disease is caused by Bartonella henselae, is common in patients under 20, "
    "and classically produces preauricular and submandibular lymphadenopathy with fever and malaise "
    "after cat contact. Diagnosis is serologic with indirect fluorescent antibodies, and the illness "
    "is often self-limiting or treated with azithromycin."],
   ["Acid-fast stain and culture for mycobacteria",
    "Acid-fast testing is how atypical mycobacterial and tuberculous adenitis are diagnosed. Those "
    "present with brawny unilateral disease in a well child, or diffuse bilateral disease in an "
    "adult, and neither is suggested by a new kitten."],
   ["Monospot and Epstein-Barr virus serology",
    "Mononucleosis does cause cervical lymphadenopathy with fever and malaise, so it is a reasonable "
    "differential, but it typically brings tonsillar exudate and splenomegaly, and it is not "
    "explained by cat exposure."],
   ["Toxoplasma serology",
    "Toxoplasmosis is also acquired from cats, which makes it tempting, but the route is ingestion "
    "of oocysts in faeces or undercooked meat rather than a scratch, and it usually gives more "
    "generalised lymphadenopathy with sore throat and myalgias."]],
  "testing", D, 34),
]
