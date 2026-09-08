# -*- coding: utf-8 -*-
"""Lecture 18 vignette pool D -- brings the vignette set to sixty. Short keys."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Neck masses and neoplasms: the triangles and lymph nodes of the neck; and the etiologies, "
      "epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, and prognosis")
C = lambda n: "CMS I Neoplasms and Neck Masses, Slide %d" % n

QUESTIONS = [

Q("Thyroid cancer", IO,
  "A 36-year-old woman has papillary thyroid carcinoma confined to one lobe, well differentiated, "
  "with no metastasis.",
  [["Lobectomy",
    "Correct. Almost all thyroid cancers require thyroidectomy, but there is an explicit exception "
    "for disease localised to one lobe that is well differentiated and without metastasis. That "
    "describes this patient, and lobectomy preserves the other lobe, reducing the risk to the "
    "recurrent laryngeal nerves and parathyroids and often avoiding lifelong replacement."],
   ["Total thyroidectomy",
    "Total resection is the general rule, which makes this the tempting answer, but applying the "
    "rule without its exception commits a young woman to replacement therapy she may not need."],
   ["Isthmectomy",
    "Isthmectomy is specified for ANAPLASTIC carcinoma, a very different disease in an elderly "
    "patient with a prognosis measured in months. It would be inadequate here."],
   ["Chemotherapy and radiation",
    "That combination treats primary thyroid lymphoma. Differentiated carcinoma is a surgical "
    "disease with radioiodine ablation where indicated."]], C(44)),

Q("Thyroid cancer follow-up", IO,
  "A patient treated for medullary thyroid carcinoma is followed with a specific blood test for "
  "recurrence.",
  [["Calcitonin",
    "Correct. Medullary carcinoma arises from parafollicular C cells, whose normal product is "
    "calcitonin, so the tumour secretes it and the level tracks disease burden. That makes it a "
    "specific marker for residual or recurrent disease, alongside external beam radiation for nodal "
    "disease and screening the family for multiple endocrine neoplasia."],
   ["Thyroglobulin",
    "Thyroglobulin is the marker for the DIFFERENTIATED cancers, papillary and follicular, which "
    "arise from epithelial cells that make it. Medullary tumours do not."],
   ["Thyroid-stimulating hormone",
    "Thyroid-stimulating hormone is monitored to keep replacement adequate and to suppress "
    "differentiated tumours, but it reflects pituitary feedback rather than tumour presence."],
   ["Parathyroid hormone",
    "Parathyroid hormone is relevant to a coexisting parathyroid problem in multiple endocrine "
    "neoplasia, but it is not the marker for the thyroid tumour."]], C(44)),

Q("Neck mass under 40", IO,
  "A 28-year-old man has a painless firm supraclavicular node that has grown over two months. He "
  "has had no infection.",
  [["Lymphoma",
    "Correct. Most neck masses under 40 are inflammatory, and Hodgkin lymphoma is the named "
    "exception to that rule. A painless firm node enlarging over months without infection is the "
    "presentation the exception exists for, and supraclavicular location adds concern because those "
    "nodes drain the thorax and abdomen."],
   ["Reactive viral adenopathy",
    "Reactive nodes follow an identifiable infection and regress in one to two weeks. Two months of "
    "growth with no infective history is a different course."],
   ["Branchial cleft cyst",
    "A branchial cleft cyst sits at the anterior sternocleidomastoid border, is fluctuant rather "
    "than firm, and declares itself when infected."],
   ["Thyroid nodule",
    "A thyroid mass is midline and elevates with swallowing, whereas this node is supraclavicular "
    "and fixed."]], C(13)),

Q("Scrofula", IO,
  "A 52-year-old man from a high-prevalence region has diffuse bilateral cervical lymphadenopathy "
  "with weight loss and night sweats.",
  [["Tuberculous adenitis",
    "Correct. Cervical tuberculosis, called scrofula, affects adults more than children and produces "
    "lymphadenopathy that is more diffuse and bilateral than atypical mycobacterial disease. "
    "Diagnosis is by tuberculin skin testing with acid-fast stain and culture, and treatment is the "
    "RIPE regimen."],
   ["Atypical mycobacterial infection",
    "Atypical disease is paediatric, unilateral, in the anterior triangle or parotid, with brawny "
    "reddish-brown overlying skin in a well child. Age and laterality both point away."],
   ["Reactive viral lymphadenopathy",
    "Reactive nodes accompany an upper respiratory infection and regress within weeks, without "
    "weight loss or night sweats."],
   ["Actinomycosis",
    "Actinomycosis is a painless fluctuant submandibular mass with filamentous organisms on biopsy, "
    "treated with penicillin, rather than diffuse bilateral adenopathy."]], C(34)),

Q("Neck abscess", IO,
  "A 5-year-old has a hot, tender, fluctuant submandibular swelling with fever after a sore throat.",
  [["Suppurative lymphadenitis",
    "Correct. Suppurative adenitis is most often Staphylococcus aureus or group A beta-haemolytic "
    "streptococcus, developing in the submandibular or jugulodigastric regions with sore throat, "
    "skin lesions and upper respiratory symptoms. Empirical antibiotics come first, with aspiration "
    "or drainage if they fail."],
   ["Atypical mycobacterial adenitis",
    "Atypical mycobacterial disease is indolent, with brawny reddish-brown skin and a systemically "
    "well child. Acute fever with fluctuance and heat is a pyogenic picture."],
   ["Branchial cleft cyst",
    "An infected branchial cleft cyst is possible and would be tender and erythematous, but it sits "
    "at the anterior sternocleidomastoid border rather than submandibular, and usually there is a "
    "known lump."],
   ["Lymphoma",
    "Lymphoma is painless and firm, growing over weeks without heat, fever or fluctuance."]],
  C(33)),

Q("Paraganglioma", IO,
  "A 50-year-old woman has a slowly enlarging lateral neck mass. On auscultation there is a bruit, "
  "and it is pulsatile.",
  [["Paraganglioma",
    "Correct. Paragangliomas head the benign vascular list, arising at the carotid body, the vagus "
    "or the jugulotympanic region. Their vascularity produces both the pulsation and the bruit, and "
    "the practical consequence is angiography before anything is put into the mass."],
   ["Schwannoma",
    "Schwannomas are benign peripheral nerve tumours listed with neurofibromas and neuromas. They "
    "are not vascular and do not pulsate."],
   ["Lipoma",
    "A lipoma is soft, mobile and avascular, growing imperceptibly over years without any pulse."],
   ["Metastatic node",
    "A metastatic node is firm and immobile without a pulse. A bruit would be very unusual."]],
  C(38)),

Q("Neck mass in a child", IO,
  "A 4-year-old has a midline neck mass that becomes red and tender after every cold, then settles.",
  [["Thyroglossal duct cyst",
    "Correct. Thyroglossal duct cysts are the commonest congenital neck mass at about a third of "
    "them, and they characteristically become apparent when infected after an upper respiratory "
    "infection. Midline position is the first branch of the congenital differential, and the tongue "
    "protrusion test confirms it."],
   ["Branchial cleft cyst",
    "A branchial cleft cyst behaves the same way, becoming infected after a cold, which is why it is "
    "the closest mimic. It is LATERAL, at the sternocleidomastoid border."],
   ["Reactive lymph node",
    "Reactive nodes are lateral, often multiple, and regress within a couple of weeks without "
    "recurring at exactly the same site."],
   ["Lymphangioma",
    "A lymphangioma is soft, doughy, compressible and transilluminates, and it does not follow this "
    "infect-and-settle pattern."]], C(23)),

Q("Congenital neck mass in an adult", IO,
  "A 44-year-old smoker has what looks like a branchial cleft cyst: a cystic lateral neck mass at "
  "the sternocleidomastoid border.",
  [["Rule out human papillomavirus-associated squamous carcinoma first",
    "Correct. Human papillomavirus-associated squamous cell carcinoma can present as a CYSTIC neck "
    "mass in an adult, which is exactly what a branchial cleft cyst looks like. Because a congenital "
    "diagnosis in an adult carries that trap, the malignancy must be excluded before the benign "
    "label is accepted."],
   ["Proceed directly to excision as for a congenital cyst",
    "Excising it as a congenital lesion without excluding malignancy risks operating on a cancer "
    "with the wrong plan, and excisional biopsy of a malignant node spills tumour."],
   ["Reassure, as congenital cysts are always benign",
    "Congenital cysts are benign, which is what makes the mimicry dangerous. The point is that this "
    "may not be one."],
   ["Treat with antibiotics and review in three months",
    "Three months of watching a cystic neck mass in a smoker over 40 delays a cancer diagnosis while "
    "treating an infection that may not exist."]], C(22)),

Q("Neck mass imaging", IO,
  "A 47-year-old man has a persistent neck mass. The clinician wants to know whether it is solid or "
  "cystic and whether there is metastatic disease.",
  [["Contrast computed tomography",
    "Correct. Contrast computed tomography differentiates vascularity, separates solid from cystic, "
    "evaluates for metastatic disease, and contributes to staging. It is the workhorse for a neck "
    "mass, with the single caveat that iodine contrast is avoided if thyroid cancer is suspected."],
   ["Plain radiography",
    "Plain films cannot distinguish solid from cystic or show nodal disease, so they answer none of "
    "the questions being asked."],
   ["Ultrasound alone",
    "Ultrasound is useful and often first, particularly for thyroid, but it does not stage the neck "
    "or assess deeper structures as completely."],
   ["Magnetic resonance imaging as first line",
    "Magnetic resonance is a substitute where computed tomography angiography is contraindicated, "
    "and is helpful for some soft tissue questions, but computed tomography with contrast is the "
    "default here."]], C(18)),

Q("Neck mass in an adult smoker", IO,
  "A 60-year-old man with a 40 pack-year history has an ulcerated firm neck mass.",
  [["Presume malignancy",
    "Correct. Always presume a new neck mass is malignant until proven otherwise in this group. "
    "Ulceration is itself on the red-flag list, alongside age over 40, tobacco and alcohol, "
    "firmness, immobility, size and duration, and this patient carries several at once."],
   ["Presume infection given the ulceration",
    "Ulceration over a mass is a malignancy flag rather than an infective one. An infected mass "
    "shows erythema, tenderness and fluctuance instead."],
   ["Presume a congenital cyst that has become infected",
    "Congenital cysts present in childhood or early adulthood, and a first presentation at 60 with "
    "ulceration is not that."],
   ["Presume reactive adenopathy from smoking",
    "Smoking is a malignancy risk factor rather than a cause of reactive adenopathy, and reactive "
    "nodes do not ulcerate."]], C(39)),

Q("Neck mass workup order", IO,
  "A neck mass has failed to settle after antibiotics, and computed tomography shows a solid mass. "
  "What comes next?",
  [["Fine needle aspiration biopsy",
    "Correct. Imaging characterises the mass but cannot give a tissue diagnosis. Aspiration is the "
    "standard of care because it separates neoplasm from inflammation and carcinoma from lymphoma, "
    "and it is preferred over excision because excision spills tumour and complicates definitive "
    "treatment."],
   ["Excisional biopsy",
    "Excision gives more tissue but seeds the neck if the mass is malignant, which is why aspiration "
    "comes first even though it yields less."],
   ["Positron emission tomography",
    "Positron emission tomography has a place in staging and in hunting an occult primary, but it "
    "gives no tissue diagnosis and is positive in inflammation as well as cancer."],
   ["Another course of antibiotics",
    "Antibiotics have already failed once, and a solid mass on imaging is not an infection that a "
    "second course will clear."]], C(18)),

Q("Hemangioma complications", IO,
  "A 4-month-old has a large neck haemangioma and is now developing stridor and difficulty feeding.",
  [["Start propranolol",
    "Correct. Observation is the default because about 90 per cent involute, but intervention is "
    "indicated for airway compromise, skin ulceration, dysphagia, thrombocytopenia or cardiac "
    "failure. Stridor and feeding difficulty are two of those, and propranolol is first line for "
    "infants without a contraindication."],
   ["Continue observation",
    "Observation is right for an asymptomatic lesion, and would have been right for this infant last "
    "month. Functional compromise is precisely what changes the plan."],
   ["Sclerotherapy",
    "Sclerotherapy is used for lymphangiomas rather than haemangiomas, and it would not act quickly "
    "enough for a threatened airway."],
   ["Immediate surgical excision",
    "Surgery is second line after propranolol and systemic steroids, and operating on a "
    "proliferating vascular lesion in an infant carries considerable risk."]], C(27)),

Q("Neck mass and pets", IO,
  "A 30-year-old woman has tender cervical nodes, fever and myalgias. She eats rare steak and has "
  "an outdoor cat.",
  [["Toxoplasmosis",
    "Correct. Toxoplasma gondii is contracted through poorly cooked meat or ingestion of oocysts in "
    "cat faeces, and both exposures are present. Patients have fever, malaise, sore throat and "
    "myalgias with the adenopathy, diagnosis is serologic, and treatment is sulfonamides or "
    "pyrimethamine."],
   ["Cat scratch disease",
    "Cat scratch disease also involves cats, which makes it the closest competitor, but the route is "
    "a scratch rather than ingestion, and it produces preauricular and submandibular nodes in "
    "someone usually under 20."],
   ["Brucellosis",
    "Brucellosis comes from unpasteurised milk and gives total-body lymphadenopathy rather than "
    "regional cervical nodes with myalgias."],
   ["Tularemia",
    "Tularemia follows exposure to rabbits, ticks or contaminated water and presents with "
    "tonsillitis and painful adenopathy."]], C(33)),

Q("Neck mass and travel", IO,
  "A 26-year-old woman returned from a rural stay abroad and now has cervical adenopathy. The "
  "clinician reviews her exposure history.",
  [["Ask about tuberculosis contact and animal exposure",
    "Correct. The history for a neck mass covers recent upper respiratory or head and neck "
    "infection, exposure to pets and other animals, recent travel and tuberculosis exposure, "
    "malignancy risk, recent trauma and immunodeficiency. Travel makes the tuberculosis and zoonotic "
    "branches considerably more relevant."],
   ["Ask only about smoking and alcohol",
    "Tobacco and alcohol are malignancy risk factors and belong in the history, but taken alone they "
    "omit the infectious exposures that the travel makes likely."],
   ["Ask about noise exposure",
    "Noise exposure belongs to the assessment of hearing loss and has no bearing on cervical "
    "adenopathy."],
   ["No further history is needed once imaging is arranged",
    "Imaging characterises the mass but cannot supply the exposure history that narrows an "
    "infectious differential, and much of that differential is diagnosed serologically."]], C(14)),
]
