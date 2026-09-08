# -*- coding: utf-8 -*-
"""Lecture 18, third pool -- Neoplasms and Neck Masses.

Keys are kept deliberately short here. Writing deep explanations pulls the
reason into the option text, and that is what drove the earlier pools to 36%
length-gameable -- see cmsent_shortfix.py.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "CMS I Neoplasms and Neck Masses"
IO = ("Neck masses and neoplasms: the triangles and lymph nodes of the neck; and the etiologies, "
      "epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, and prognosis of common neck masses, "
      "vascular tumors, and benign and malignant neoplasms")

QUESTIONS = [

Q("Metastatic neck disease", IO,
  "A 62-year-old smoker has a firm cervical node. Fine needle aspiration shows squamous cell "
  "carcinoma, but no primary tumour is apparent on initial examination.",
  [["Examine all mucosal surfaces of the head and neck",
    "Correct. Squamous cell carcinoma is the commonest metastatic lesion to the neck, and it arrives "
    "from the skin or the upper aerodigestive tract. A systematic office "
    "examination of every mucosal surface, the thyroid, the salivary glands and the skin usually "
    "finds the primary, so that comes before more imaging."],
   ["Proceed directly to neck dissection",
    "Operating without identifying the primary means the field cannot be planned and the primary "
    "goes untreated, so the disease recurs. Finding the source changes both the surgery and the "
    "radiotherapy."],
   ["Repeat the aspiration to confirm the cell type",
    "The cytology has already given a clear answer. Repeating it adds nothing, and the outstanding "
    "question is where the tumour came from rather than what it is."],
   ["Treat empirically with radiotherapy to the neck",
    "Irradiating the neck without knowing the primary site leaves an untreated tumour and commits "
    "the patient to a field that may be wrong. Radiotherapy planning depends on the primary."]],
  "next step", D, 39),

Q("Metastatic neck disease", IO,
  "A clinician explains why fine needle aspiration rather than excisional biopsy is used for a "
  "suspected malignant neck node.",
  [["Excision spills tumour and complicates definitive treatment",
    "Correct. Opening a malignant node releases cells into the surrounding tissue planes, which "
    "seeds the neck outside the original nodal compartment and makes both the surgical field and "
    "the radiotherapy field harder to define. Aspiration samples the node without breaching its "
    "capsule."],
   ["Aspiration is more accurate than excision",
    "Excisional biopsy actually gives more tissue and better architecture, which is why it is used "
    "for suspected lymphoma. Aspiration is preferred here despite giving less, because of what "
    "excision does to the neck."],
   ["Excision requires general anaesthesia and aspiration does not",
    "Convenience is a genuine advantage of aspiration but not the stated reason. The argument is "
    "oncological rather than logistical."],
   ["Aspiration can be repeated whereas excision cannot",
    "Repeatability is true and useful, but it does not explain why excision is actively avoided "
    "rather than simply used less often."]],
  "mechanism", D, 39),

Q("Reactive lymphadenopathy", IO,
  "A 6-year-old has a 2 centimetre cervical node that appeared with a cold five weeks ago and has "
  "not changed in size.",
  [["Investigate further, as it exceeds the size and duration thresholds",
    "Correct. A node larger than 1 centimetre is abnormal, and reactive nodes should regress within "
    "one to two weeks. Persistence beyond four to six weeks, or continued enlargement, is the stated "
    "trigger for investigation, with biopsy looking for fungal, granulomatous or neoplastic "
    "causes."],
   ["Continue observation, since viral nodes are common in children",
    "Observation was correct for the first fortnight, and reactive viral adenopathy is indeed the "
    "commonest cause in children. It stops being the right answer once the node has outlived the "
    "timescale that defines reactive."],
   ["Start empirical antibiotics",
    "There are no features of bacterial adenitis: no tenderness, erythema, fever or fluctuance. "
    "Antibiotics would treat nothing and would delay the investigation the duration now warrants."],
   ["Reassure and discharge",
    "Discharging a node that has breached both the size and the duration thresholds removes the "
    "follow-up that would detect a lymphoma, which is the exception to the rule that childhood "
    "masses are inflammatory."]],
  "next step", D, 31),

Q("Thyroid nodule", IO,
  "A radionuclide scan of a solitary thyroid nodule in a hyperthyroid patient shows the nodule is "
  "hyperfunctioning.",
  [["No biopsy is needed, as hot nodules carry a low malignant risk",
    "Correct. A nodule that concentrates tracer avidly is producing hormone autonomously, and "
    "autonomously functioning nodules are almost always benign. That is the whole purpose of scanning "
    "before aspirating in a patient with a suppressed thyroid-stimulating hormone: it identifies the "
    "group in whom biopsy can be safely omitted."],
   ["Proceed to fine needle aspiration as for any nodule",
    "Aspirating every nodule is the correct default when the thyroid-stimulating hormone is normal. "
    "Applying it after a scan has already shown the nodule is hot subjects the patient to a "
    "procedure whose result was predictable."],
   ["Proceed directly to thyroidectomy",
    "Surgery may eventually be considered for symptomatic hyperthyroidism, but removing the gland on "
    "the basis of a benign hot nodule is disproportionate when medical therapy or radioiodine are "
    "available."],
   ["Repeat the scan in six months",
    "Repeating a scan that has already answered the question adds radiation without new information. "
    "The management question now concerns the hyperthyroidism rather than the nodule's nature."]],
  "next step", D, 41),

Q("Papillary thyroid carcinoma", IO,
  "A 29-year-old woman has papillary thyroid carcinoma confined to one lobe, well differentiated, "
  "with no evidence of metastasis.",
  [["Lobectomy may be sufficient rather than total thyroidectomy",
    "Correct. Almost all thyroid cancers require thyroidectomy, with one "
    "explicit exception: disease localised to one lobe, well differentiated and without metastasis. "
    "That is exactly this patient, and lobectomy preserves the contralateral gland and reduces the "
    "risk to the recurrent laryngeal nerves and parathyroids."],
   ["Total thyroidectomy is mandatory in all thyroid cancer",
    "This states the general rule without its exception, which is the whole point of the "
    "qualification. Applying it here commits a young woman to lifelong hormone replacement she may "
    "not need."],
   ["Isthmectomy is the appropriate operation",
    "Isthmectomy is named for ANAPLASTIC carcinoma, which is a very different disease in an elderly "
    "patient with a prognosis measured in months. It would be inadequate for a resectable papillary "
    "tumour."],
   ["Chemotherapy and radiation rather than surgery",
    "That combination is the treatment for primary thyroid LYMPHOMA. Differentiated thyroid "
    "carcinoma is a surgical disease with radioiodine ablation where indicated."]],
  "treatment", D, 44),

Q("Brucellosis", IO,
  "A 38-year-old man who drinks unpasteurised milk from a local farm has fever, fatigue, malaise "
  "and generalised lymphadenopathy including the neck.",
  [["Trimethoprim-sulfamethoxazole or tetracycline",
    "Correct. The exposure to unpasteurised milk points to Brucella, and the distinguishing clinical "
    "feature is that the lymphadenopathy is total-body rather than confined to one region, which "
    "separates it from the regional adenopathies on the same slide. Diagnosis is by serology and "
    "culture."],
   ["Streptomycin",
    "Streptomycin is the treatment for tularemia, acquired from rabbits, ticks or contaminated "
    "water, which presents with tonsillitis and painful regional adenopathy rather than generalised "
    "nodes."],
   ["Penicillin",
    "Penicillin treats actinomycosis, which presents as a painless fluctuant submandibular mass with "
    "filamentous organisms on biopsy. There is no such localised mass here."],
   ["Azithromycin",
    "Azithromycin is used for cat scratch disease from Bartonella henselae, which requires cat "
    "contact and produces preauricular and submandibular nodes in a patient usually under 20."]],
  "treatment", D, 33),

Q("Fungal neck infection", IO,
  "A 55-year-old woman on immunosuppression after transplantation has persistent cervical "
  "lymphadenopathy. Bacterial cultures are negative and antibiotics have failed.",
  [["Send fungal cultures and serology",
    "Correct. Immunocompromised patients are particularly susceptible to fungal infection, most "
    "commonly Candida, Histoplasma and Aspergillus, and fungal cultures "
    "AND serology are required to make the diagnosis. Negative bacterial cultures with antibiotic "
    "failure in this host is precisely the setting in which to look."],
   ["Increase the antibiotic spectrum",
    "Broadening antibacterial cover repeats a strategy that has already failed and further "
    "suppresses the flora, which favours the fungal overgrowth that is the likelier problem."],
   ["Reduce the immunosuppression and observe",
    "Reducing immunosuppression may form part of management, but it risks graft rejection and does "
    "not identify the organism. The diagnosis has to be established first."],
   ["Start empirical antituberculous therapy",
    "Tuberculosis is worth excluding in an immunosuppressed patient, but committing to months of "
    "hepatotoxic therapy without acid-fast evidence, when fungal disease is at least as likely, puts "
    "the cart before the horse."]],
  "testing", D, 35),

Q("Kawasaki disease", IO,
  "A 4-year-old has five days of high fever, bilateral conjunctival injection, a strawberry tongue, "
  "cracked lips, a rash and a large unilateral cervical node.",
  [["Kawasaki disease",
    "Correct. Kawasaki is one of the non-infectious inflammatory causes of neck "
    "masses, alongside Sjogren syndrome, sarcoidosis and IgG4-related disease. The cervical node is "
    "one criterion among several, and recognising the constellation matters because untreated "
    "Kawasaki causes coronary artery aneurysms."],
   ["Suppurative bacterial lymphadenitis",
    "Bacterial adenitis produces a hot tender node with fever, but not conjunctivitis, a strawberry "
    "tongue, cracked lips and a rash. Those mucocutaneous features indicate a systemic "
    "inflammatory process."],
   ["Infectious mononucleosis",
    "Mononucleosis gives fever with tonsillar pharyngitis and bilateral cervical adenopathy, and can "
    "produce a rash after penicillin. It does not cause conjunctival injection with a strawberry "
    "tongue and cracked lips."],
   ["Reactive viral lymphadenopathy",
    "Reactive nodes accompany a mild upper respiratory illness and regress within a couple of weeks. "
    "Five days of high fever with mucocutaneous changes is a very different clinical picture."]],
  "diagnosis", D, 35),

Q("Neck mass workup", IO,
  "A pulsatile neck mass has been identified. Imaging is being selected.",
  [["Computed tomography angiography",
    "Correct. Pulsatility indicates a vascular lesion, most likely a paraganglioma, and angiography "
    "defines the blood supply and the relationship to the carotid before anyone considers "
    "intervention. It is the study of choice for pulsatile masses, with magnetic resonance "
    "as a substitute that is generally less preferred."],
   ["Fine needle aspiration",
    "Aspiration is the standard of care for most neck masses but is exactly what must not be done "
    "blindly into a pulsatile lesion, because puncturing a vascular tumour risks significant "
    "haemorrhage."],
   ["Plain radiography of the neck",
    "Plain films cannot demonstrate vascularity or define a vascular tumour's supply. They would not "
    "influence management at all."],
   ["Positron emission tomography",
    "Positron emission tomography shows metabolic activity and is used for staging or hunting an "
    "occult primary. It does not map arterial anatomy, which is the question a pulsatile mass "
    "raises."]],
  "testing", D, 19),

Q("Congenital neck masses", IO,
  "A student is asked to name the commonest congenital neck mass.",
  [["Thyroglossal duct cyst, at about one third",
    "Correct. Thyroglossal duct cysts make up about a third of all congenital neck masses, which is "
    "why a midline neck lump in a child has a strong prior probability. Their location can vary, "
    "with some presenting lateral or as low as the thyroid gland, and those are the ones hard to "
    "distinguish from a branchial cleft cyst."],
   ["Branchial cleft cyst",
    "Branchial cleft cysts are common and are the classic LATERAL congenital mass, but they do not "
    "account for the largest share. They typically declare themselves when infected in late "
    "childhood or early adulthood."],
   ["Lymphangioma",
    "Lymphangiomas are distinctive because they transilluminate and feel soft and doughy, but they "
    "are considerably less common than thyroglossal duct cysts."],
   ["Dermoid cyst",
    "Dermoids are midline and submental and are the closest mimic of a thyroglossal duct cyst, but "
    "they are less frequent and do not move with tongue protrusion."]],
  "finding", D, 23),

Q("Thyroid cancer follow-up", IO,
  "A patient treated for medullary thyroid carcinoma is monitored for recurrence with a specific "
  "blood test.",
  [["Calcitonin",
    "Correct. Medullary carcinoma arises from the parafollicular C cells, whose normal product is "
    "calcitonin, so the tumour secretes it and the level tracks tumour burden. That makes calcitonin "
    "a specific marker for detecting residual or recurrent disease, which is why screening labs form "
    "part of follow-up alongside thyroidectomy."],
   ["Thyroglobulin",
    "Thyroglobulin is the marker for the DIFFERENTIATED cancers, papillary and follicular, because "
    "those arise from thyroid epithelial cells that make it. Medullary tumours do not, so the level "
    "would be uninformative."],
   ["Thyroid-stimulating hormone",
    "Thyroid-stimulating hormone is monitored to keep replacement therapy adequate and to suppress "
    "differentiated tumours, but it reflects pituitary feedback rather than the presence of "
    "medullary tumour."],
   ["Parathyroid hormone",
    "Parathyroid hormone would be relevant to a parathyroid problem, which can coexist in multiple "
    "endocrine neoplasia, but it is not the marker for the thyroid tumour itself."]],
  "testing", D, 44),

Q("Neck triangles", IO,
  "A surgeon operating in the occipital triangle is warned about a nerve crossing its muscular "
  "floor.",
  [["The spinal accessory nerve",
    "Correct. The spinal accessory nerve crosses the muscular floor of the occipital triangle to "
    "pass deep to trapezius, which places it superficially and vulnerably in the posterior triangle. "
    "Injury there denervates trapezius and produces a painful drooping shoulder, which is why it is "
    "the classic nerve at risk in posterior triangle surgery."],
   ["The hypoglossal nerve",
    "The hypoglossal nerve lies in the digastric or submandibular triangle of the ANTERIOR group, "
    "alongside the submandibular gland and facial vessels. It supplies the tongue rather than "
    "trapezius."],
   ["The vagus nerve",
    "The vagus runs in the carotid sheath within the carotid triangle, again in the anterior group, "
    "with the carotid arteries and internal jugular vein. It is not a posterior triangle structure."],
   ["The recurrent laryngeal nerve",
    "The recurrent laryngeal nerve runs in the tracheo-oesophageal groove deep in the anterior neck "
    "and is at risk during thyroid surgery, not in the posterior triangle."]],
  "finding", D, 5),

Q("Dermoid cyst", IO,
  "A 12-year-old has a midline submental mass that is non-tender and mobile. It does not move when "
  "he protrudes his tongue.",
  [["Dermoid cyst",
    "Correct. Both dermoid and thyroglossal duct cysts are midline, which is why they are the pair "
    "that must be distinguished. The discriminator is the hyoid attachment: a thyroglossal duct cyst "
    "rises with tongue protrusion, and a dermoid, arising from epithelium entrapped during "
    "embryogenesis, has no such connection and stays still."],
   ["Thyroglossal duct cyst",
    "This is the commonest congenital midline mass and the right first thought, but the absence of "
    "movement on tongue protrusion is the specific finding that excludes it, because that movement "
    "is pathognomonic."],
   ["Branchial cleft cyst",
    "Branchial cleft cysts are lateral, at the anterior border of the sternocleidomastoid. A midline "
    "submental position is wrong for them, though cysts presenting off-midline can be confusing."],
   ["Submental lymph node",
    "A submental node would be expected to be one of several, to relate to an oral or facial "
    "infection, and to be tender if inflamed. A solitary painless mobile midline mass over years "
    "behaves differently."]],
  "diagnosis", D, 29),

Q("Neck abscess", IO,
  "A 33-year-old man has a fluctuant, tender neck mass with overlying erythema and fever after a "
  "sore throat. Antibiotics have not settled it over 72 hours.",
  [["Fine needle aspiration or incision and drainage",
    "Correct. Suppurative bacterial lymphadenopathy is treated empirically with antibiotics covering "
    "anaerobes and gram-positive organisms, but aspiration or incision "
    "and drainage follows when antibiotics fail. Fluctuance means there is a collection, and a "
    "collection needs draining rather than more antibiotic."],
   ["Change to a broader-spectrum antibiotic and continue",
    "Escalating the antibiotic is reasonable alongside drainage, but antibiotics penetrate an "
    "established abscess cavity poorly, so relying on them alone repeats a strategy that has already "
    "failed for three days."],
   ["Excisional biopsy of the node",
    "Excisional biopsy is a diagnostic operation for a suspected neoplastic node. Here the diagnosis "
    "is clinically evident and the requirement is therapeutic drainage."],
   ["Observation, since most nodes settle spontaneously",
    "Reactive nodes settle spontaneously, but a fluctuant tender node with fever that has resisted "
    "72 hours of antibiotics is a collection rather than a reactive node, and it will not resolve on "
    "its own."]],
  "next step", D, 33),

Q("Neck mass consistency", IO,
  "A clinician palpates a neck mass and finds it fluctuant.",
  [["A cystic lesion",
    "Correct. Fluctuance means the mass transmits pressure as a fluid would, so it contains liquid "
    "rather than solid tissue. That is one of the four rules of thumb, alongside "
    "pulsatility indicating vascular, years of stability indicating benign, and rapid growth "
    "indicating infection or lymphoma."],
   ["A vascular lesion",
    "Vascular masses are identified by PULSATILITY or a bruit rather than fluctuance. Both suggest "
    "something other than solid tissue, but they are distinguished by whether the movement is "
    "synchronous with the pulse."],
   ["A metastatic lymph node",
    "Malignant nodes are characteristically firm or hard and immobile. Fluctuance argues against "
    "malignancy, though a necrotic metastatic node can occasionally feel cystic."],
   ["A lipoma",
    "A lipoma is soft and doughy and can be mistaken for a fluid-filled structure, but it does not "
    "fluctuate because it is solid fat rather than liquid."]],
  "finding", D, 13),
]
