# -*- coding: utf-8 -*-
"""Lecture 18 objective-style pool C -- Neoplasms and Neck Masses."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Neck masses and neoplasms: the triangles and lymph nodes of the neck; and the etiologies, "
      "epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, and prognosis")
C = lambda n: "CMS I Neoplasms and Neck Masses, Slide %d" % n

QUESTIONS = [

Q("Thyroid nodule", IO, "What does a HOT nodule on radionuclide scanning imply?",
  [["A low risk of malignancy, so no biopsy is needed",
    "Correct. A hot nodule concentrates tracer because it is producing hormone autonomously, and "
    "autonomously functioning nodules are almost always benign. That is the entire purpose of "
    "scanning before aspirating in a hyperthyroid patient: it identifies the group in whom biopsy "
    "can safely be omitted."],
   ["A high risk of malignancy requiring urgent surgery",
    "Hot nodules carry a LOW malignant risk. Cold or warm nodules are the ones that require "
    "aspiration, so this reverses the rule and would send the wrong patients to theatre."],
   ["That the patient is hypothyroid",
    "A hot nodule produces excess hormone, which suppresses thyroid-stimulating hormone and makes "
    "the patient hyperthyroid rather than hypothyroid."],
   ["That contrast imaging is now required",
    "Iodine-containing contrast is avoided when thyroid cancer is a possibility. A hot nodule makes "
    "cancer less likely, but it does not create an indication for contrast."]], C(41)),

Q("Thyroid cancer", IO, "Which thyroid carcinoma is commonest and has the best prognosis?",
  [["Papillary carcinoma",
    "Correct. Papillary carcinoma accounts for about 75 per cent of thyroid cancers, arises from "
    "thyroid epithelial cells, is commonest in young women and has the best outlook of the four "
    "types. It tends to spread to local cervical lymph nodes rather than distantly, which is part of "
    "why the prognosis is favourable."],
   ["Follicular carcinoma",
    "Follicular carcinoma is the second commonest at about 16 per cent and also arises from "
    "epithelial cells, but it spreads by blood to bone and lung, and the Hurthle cell variant is "
    "more aggressive still."],
   ["Medullary carcinoma",
    "Medullary carcinoma is about 5 per cent, arises from calcitonin-producing parafollicular C "
    "cells, and is the most likely of the four to have metastasised by the time it is found."],
   ["Anaplastic carcinoma",
    "Anaplastic carcinoma is about 1 per cent, occurs in elderly patients, and is the most aggressive "
    "form, causing death in 6 to 36 months and resistant to all treatment."]], C(42)),

Q("Thyroid cancer", IO, "Which thyroid carcinoma spreads by blood to bone and lung?",
  [["Follicular carcinoma",
    "Correct. The route of spread is what distinguishes follicular from papillary disease. Papillary "
    "tends to involve local cervical nodes, whereas follicular disseminates haematogenously to bone "
    "and lungs. A distant bony deposit in a thyroid cancer therefore points to the follicular "
    "type."],
   ["Papillary carcinoma",
    "Papillary carcinoma spreads chiefly to local lymph nodes, which is one reason its prognosis is "
    "better. Distant bony metastasis would be atypical."],
   ["Anaplastic carcinoma",
    "Anaplastic carcinoma spreads aggressively but presents as a rapidly enlarging hard neck mass in "
    "an elderly patient, and its course is measured in months rather than by a route of spread."],
   ["Primary thyroid lymphoma",
    "Thyroid lymphoma arises on a background of Hashimoto thyroiditis and is staged as a lymphoma, "
    "treated with chemotherapy and radiation rather than by pattern of haematogenous spread."]],
  C(42)),

Q("Thyroid cancer", IO, "From which cells does medullary thyroid carcinoma arise?",
  [["Parafollicular C cells",
    "Correct. C cells produce calcitonin, which is why calcitonin serves as a tumour marker for "
    "detecting residual or recurrent disease. Their neuroendocrine origin also explains the familial "
    "association with multiple endocrine neoplasia, which is why family members are screened."],
   ["Thyroid follicular epithelial cells",
    "Epithelial cells give rise to papillary and follicular carcinoma, the two differentiated "
    "cancers. Those are followed with thyroglobulin rather than calcitonin."],
   ["Lymphocytes within the gland",
    "A lymphoid origin gives primary thyroid lymphoma, which arises against a background of "
    "Hashimoto thyroiditis and is difficult to separate from it on aspiration alone."],
   ["Parathyroid chief cells",
    "Parathyroid chief cells produce parathyroid hormone and give rise to parathyroid adenomas. They "
    "sit in separate glands behind the thyroid."]], C(42)),

Q("Thyroid cancer", IO, "Which thyroid carcinoma has a prognosis measured in months?",
  [["Anaplastic carcinoma",
    "Correct. Anaplastic carcinoma represents about 1 per cent of thyroid cancers, occurs in elderly "
    "patients, and comprises small cell, giant cell and spindle cell types. It results in death "
    "within 6 to 36 months and is resistant to all treatment modalities, which is why the surgical "
    "option is isthmectomy rather than curative resection."],
   ["Papillary carcinoma",
    "Papillary carcinoma has the best prognosis of the four and is compatible with normal life "
    "expectancy in most patients."],
   ["Follicular carcinoma",
    "Follicular carcinoma carries a good prognosis overall, though the Hurthle cell variant is more "
    "aggressive with a higher risk of metastasis and recurrence."],
   ["Medullary carcinoma",
    "Medullary carcinoma is more insidious and often diagnosed late, but its course runs over years "
    "rather than months, and it is followed with calcitonin."]], C(42)),

Q("Thyroid cancer", IO,
  "Which operation is specified for anaplastic thyroid carcinoma?",
  [["Isthmectomy",
    "Correct. Almost all thyroid cancers require thyroidectomy, with two exceptions. One is disease "
    "localised to a single lobe that is well differentiated with no metastasis; the other is "
    "anaplastic carcinoma, where isthmectomy is what is specified, because the disease is not "
    "curable by resection and the operation serves a different purpose."],
   ["Total thyroidectomy with neck dissection",
    "Extensive resection is appropriate for differentiated cancers where cure is possible. In "
    "anaplastic disease it imposes major surgery on a patient whose prognosis it will not change."],
   ["Lobectomy alone",
    "Lobectomy is the option for well-differentiated disease confined to one lobe without "
    "metastasis. Anaplastic carcinoma is neither confined nor differentiated."],
   ["No surgery at all",
    "The disease is resistant to all treatment modalities, but an operation is still specified, and "
    "airway considerations often make intervention necessary."]], C(44)),

Q("Thyroid lymphoma", IO,
  "Primary thyroid lymphoma is associated with which underlying condition?",
  [["Hashimoto thyroiditis",
    "Correct. Most primary thyroid lymphomas are non-Hodgkin B cell tumours arising in a gland "
    "already infiltrated by lymphocytes from Hashimoto thyroiditis. That shared lymphoid population "
    "is exactly why fine needle aspiration alone cannot separate the two, and why an open biopsy "
    "with lymphoma staging is needed."],
   ["Graves disease",
    "Graves disease is an autoimmune cause of hyperthyroidism driven by stimulating antibodies "
    "against the thyroid-stimulating hormone receptor. It is not the background for lymphoma."],
   ["Multiple endocrine neoplasia",
    "Multiple endocrine neoplasia is associated with MEDULLARY carcinoma, which is why relatives are "
    "screened when that diagnosis is made."],
   ["Prior head and neck irradiation",
    "Childhood head and neck irradiation is a risk factor for thyroid nodules and differentiated "
    "carcinoma, and appears on the nodule risk list rather than as the lymphoma association."]],
  C(45)),

Q("Thyroid lymphoma", IO,
  "How is primary thyroid lymphoma treated?",
  [["Chemotherapy and radiation",
    "Correct. Unlike the thyroid carcinomas, which are surgical diseases with radioiodine ablation "
    "where indicated, lymphoma is treated systemically. That is the practical consequence of getting "
    "the diagnosis right, and it is why an inconclusive aspirate in a rapidly enlarging Hashimoto "
    "gland is pursued rather than accepted."],
   ["Total thyroidectomy",
    "Removing the gland is the mainstay for the carcinomas but does not treat a lymphoma, which is "
    "typically more extensive than the gland by the time it is found."],
   ["Radioiodine ablation",
    "Radioiodine works through iodine uptake by differentiated thyroid epithelial cells. Lymphoid "
    "tissue does not take up iodine, so the treatment has no target."],
   ["Observation with serial ultrasound",
    "Watching a rapidly enlarging lymphoma allows it to progress when it is a treatment-responsive "
    "disease. Delay costs more here than in most thyroid pathology."]], C(45)),

Q("Neck neoplasm", IO,
  "Why is fine needle aspiration preferred to excisional biopsy for a suspected malignant neck node?",
  [["Excision spills tumour and complicates definitive treatment",
    "Correct. Opening a malignant node breaches its capsule and releases cells into the surrounding "
    "tissue planes, seeding the neck beyond the original nodal compartment. That makes both the "
    "surgical field and the radiotherapy field harder to define afterwards, whereas aspiration "
    "samples the node without opening it."],
   ["Aspiration is more accurate than excision",
    "Excision actually yields more tissue and preserves architecture, which is why it is used when "
    "lymphoma is suspected. Aspiration is preferred here in spite of giving less."],
   ["Excision requires a general anaesthetic",
    "Anaesthetic requirements are a practical consideration but not the stated reason. The argument "
    "is oncological."],
   ["Aspiration allows immunohistochemistry that excision does not",
    "Immunohistochemistry is more readily performed on a tissue block from an excision. The "
    "advantage of aspiration lies elsewhere."]], C(39)),

Q("Neck neoplasm", IO,
  "Once metastatic squamous carcinoma is confirmed in a cervical node, what usually finds the "
  "primary?",
  [["A complete office examination of all mucosal surfaces",
    "Correct. Examining every mucosal surface of the head and neck, along with the thyroid, the "
    "salivary glands and the skin, usually locates the primary in the office. That matters because "
    "the primary determines the extent of surgery and the radiotherapy field, and treating the neck "
    "alone leaves the source seeding."],
   ["Positron emission tomography as the first test",
    "Positron emission tomography helps when the primary remains occult after examination and "
    "cross-sectional imaging, but starting with it skips the step that most often succeeds."],
   ["Repeating the fine needle aspiration",
    "The aspirate has already answered what the tumour is. The outstanding question is where it came "
    "from, which cytology cannot address."],
   ["Empirical radiotherapy to the whole neck",
    "Irradiating without knowing the primary leaves an untreated tumour and commits the patient to a "
    "field that may be wrong."]], C(39)),

Q("Primary neck tumours", IO,
  "Which benign neck tumour is a vascular neoplasm arising at the carotid body?",
  [["Paraganglioma",
    "Correct. Paragangliomas head the benign vascular list, arising at the carotid body, the vagus "
    "or the jugulotympanic region. Their vascularity is what produces a pulsatile mass with a bruit, "
    "and it is also why the mass must be imaged with angiography rather than biopsied blindly."],
   ["Schwannoma",
    "Schwannomas are benign peripheral nerve neoplasms, listed alongside neurofibromas and neuromas. "
    "They are not vascular and do not pulsate."],
   ["Lipoma",
    "A lipoma is a benign fatty tumour that is soft, mobile and slow-growing over years. It has no "
    "significant blood supply of its own."],
   ["Rhabdomyosarcoma",
    "Rhabdomyosarcoma is on the MALIGNANT list among the sarcomas, alongside fibrosarcoma, malignant "
    "fibrous histiocytoma, liposarcoma and leiomyosarcoma."]], C(38)),

Q("Primary neck tumours", IO,
  "Which of these appears on the list of MALIGNANT primary neck tumours?",
  [["Malignant peripheral nerve sheath tumour",
    "Correct. The malignant list comprises the sarcomas, malignant peripheral nerve sheath tumours, "
    "lymphoma, and metastasis from mucosal head and neck cancer, salivary malignancy or skin "
    "malignancy. The benign list is the vascular neoplasms, arteriovenous malformations, benign "
    "nerve tumours and lipomas."],
   ["Schwannoma",
    "Schwannomas sit on the BENIGN side of the same table, with neurofibromas and neuromas. The "
    "malignant counterpart is the malignant peripheral nerve sheath tumour."],
   ["Carotid body paraganglioma",
    "Paragangliomas are listed as benign vascular neoplasms. They can be locally troublesome because "
    "of their position and vascularity, but they are not on the malignant list."],
   ["Arteriovenous malformation",
    "Arteriovenous malformations appear on the benign side alongside the vascular neoplasms. They "
    "are developmental rather than neoplastic."]], C(38)),

Q("Neck mass evaluation", IO,
  "Which examination step does the evaluation of a neck mass specifically require?",
  [["Visualising all mucosal surfaces and palpating the oral and pharyngeal surfaces",
    "Correct. A complete head and neck examination means looking everywhere, because the primary for "
    "a metastatic node is frequently a small mucosal lesion that is easily missed. Palpation adds "
    "what inspection cannot, since submucosal disease may be felt before it is seen."],
   ["Auscultation of the chest only",
    "Chest examination has a place in assessing systemic disease, but it does not address the "
    "mucosal surfaces where a head and neck primary lives."],
   ["Fundoscopy",
    "Fundoscopy examines the retina and optic disc. It has no role in the assessment of a neck "
    "mass."],
   ["Abdominal palpation alone",
    "Palpating the liver and spleen is part of the examination when mononucleosis or lymphoma is "
    "suspected, but doing it alone would omit the head and neck examination entirely."]], C(15)),

Q("Neck mass evaluation", IO,
  "Which additional lymph node areas should be palpated when assessing a cervical mass?",
  [["Inguinal, axillary and supraclavicular",
    "Correct. Palpating other nodal basins distinguishes localised regional disease from generalised "
    "lymphadenopathy, which points toward a systemic cause such as lymphoma, mononucleosis or HIV. "
    "The thyroid, liver and spleen are examined for the same reason, and any vascular abnormality is "
    "auscultated."],
   ["Only the contralateral cervical chain",
    "Checking the other side of the neck is useful but stops short of separating regional from "
    "systemic disease, which requires nodes well away from the head and neck."],
   ["Popliteal and antecubital only",
    "These are not part of the routine assessment of a neck mass and would not answer the question "
    "of whether lymphadenopathy is generalised."],
   ["No other areas, as cervical nodes drain only the head",
    "Cervical nodes do drain the head and neck, but the point of examining elsewhere is to detect a "
    "systemic process, not to trace drainage."]], C(15)),

Q("Neck mass evaluation", IO,
  "Above what size are normal hyperplastic lymph nodes rarely found?",
  [["2 centimetres",
    "Correct. Reactive hyperplastic nodes are rarely larger than 2 centimetres, so exceeding that "
    "adds weight to the concern raised by the other features. It sits alongside the 1.5 centimetre "
    "threshold on the malignancy list, and both are reasons to keep measuring rather than "
    "estimating."],
   ["5 centimetres",
    "Five centimetres is a large mass by any standard and using it as the threshold would allow a "
    "great deal of significant disease to pass as normal."],
   ["0.5 centimetres",
    "Half a centimetre is well within the size of nodes palpable in healthy people, particularly "
    "submandibular ones, so it would flag almost everyone."],
   ["10 centimetres",
    "A ten centimetre neck mass would be visible across a room. No useful threshold sits there."]],
  C(15)),

Q("Neck mass workup", IO,
  "Which imaging is preferred for a pulsatile neck mass?",
  [["Computed tomography angiography",
    "Correct. Pulsatility indicates a vascular lesion, and angiography defines the blood supply and "
    "the relationship to the carotid before any intervention. Magnetic resonance imaging can "
    "substitute, but angiography is generally still preferred for this specific question."],
   ["Ultrasound alone",
    "Ultrasound with Doppler can demonstrate flow and is a reasonable first look, but it does not "
    "map the arterial anatomy in the detail a surgeon needs."],
   ["Plain radiography",
    "Plain films show neither soft tissue detail nor vascularity, so they cannot answer any part of "
    "the question a pulsatile mass raises."],
   ["Positron emission tomography",
    "Positron emission tomography reports metabolic activity, which is useful for staging and for "
    "occult primaries but says nothing about vascular supply."]], C(19)),

Q("Neck mass workup", IO,
  "What does a positron emission tomography scan measure?",
  [["Metabolic uptake of tagged glucose, higher in cancer and inflammation",
    "Correct. Radiolabelled glucose accumulates where metabolism is high, which includes malignancy "
    "but also inflammation and infection. That dual sensitivity is why it is useful for staging and "
    "for finding an occult primary, and why a positive result cannot by itself establish cancer."],
   ["The blood supply of a lesion",
    "Vascularity is assessed by computed tomography angiography or by Doppler ultrasound. Positron "
    "emission tomography reports metabolism instead."],
   ["The presence of calcification",
    "Calcification is best shown by computed tomography, and it is the finding that suggests a "
    "teratoma. Positron emission tomography does not resolve it usefully."],
   ["The cell type of a tumour",
    "Cell type comes only from tissue, by aspiration or biopsy. Imaging can suggest a diagnosis but "
    "cannot report histology."]], C(19)),

Q("Neck mass workup", IO,
  "Which laboratory tests are listed in the workup of a persistent neck mass?",
  [["Full blood count, HIV and Epstein-Barr serology, inflammatory markers and thyroid panels",
    "Correct. The panel is broad because the differential is broad: blood count and metabolic "
    "profile, HIV and Epstein-Barr and cytomegalovirus serology, erythrocyte sedimentation rate and "
    "C-reactive protein, an autoimmune panel, thyroid and parathyroid hormones, and tuberculin skin "
    "testing with cat scratch and toxoplasmosis titres."],
   ["Clotting studies alone",
    "Coagulation testing has no role in characterising a neck mass. It belongs to the assessment of "
    "bleeding, such as in epistaxis in an anticoagulated patient."],
   ["Arterial blood gases",
    "Blood gases assess ventilation and acid-base status, which are relevant to airway compromise "
    "but not to establishing what a neck mass is."],
   ["Serum calcitonin in every patient",
    "Calcitonin is specific to medullary thyroid carcinoma and is used for follow-up once that "
    "diagnosis is made, rather than as a screening test for any neck mass."]], C(19)),

Q("Referral", IO,
  "What does the assessment of a suspicious neck nodule emphasise about specialist referral?",
  [["Refer early, especially if it persists after treatment",
    "Correct. A trial of antibiotics is common practice, and the point at which that trial fails is "
    "exactly the point at which referral should happen rather than another course being prescribed. "
    "Early and aggressive treatment is needed in some neoplastic conditions, so delay costs more "
    "here than the referral does."],
   ["Refer only after three failed antibiotic courses",
    "Waiting through three courses builds in months of delay. One failed trial in a mass with red "
    "flags is already enough."],
   ["Refer only if the patient develops systemic symptoms",
    "Waiting for weight loss or night sweats means waiting for advanced disease. The red-flag list "
    "is designed to trigger action before that point."],
   ["Referral is unnecessary if fine needle aspiration is benign",
    "A benign aspirate is reassuring but subject to sampling error, which is why four passes are "
    "required and why a mass that persists or grows is reassessed regardless."]], C(19)),

Q("Congenital neck masses", IO,
  "Which congenital neck mass presents as a midline, non-tender, mobile submental mass that does "
  "NOT move with tongue protrusion?",
  [["Dermoid cyst",
    "Correct. A dermoid arises from epithelium entrapped in deeper tissue during embryogenesis or "
    "by traumatic implantation. It shares a midline submental position with the thyroglossal duct "
    "cyst, which is why they are the pair that must be separated, but it has no attachment to the "
    "hyoid and therefore does not rise with the tongue."],
   ["Thyroglossal duct cyst",
    "The thyroglossal duct cyst is the one that DOES move with tongue protrusion, because its tract "
    "runs through the hyoid to the foramen caecum. That movement is pathognomonic."],
   ["Branchial cleft cyst",
    "A branchial cleft cyst is lateral, at the anterior border of the sternocleidomastoid, and "
    "usually presents when it becomes infected after an upper respiratory infection."],
   ["Thymic cyst",
    "A thymic cyst presents as a slow-growing asymptomatic mass in the lower neck, with Hassall "
    "corpuscles on biopsy establishing the diagnosis."]], C(29)),

Q("Congenital neck masses", IO,
  "What histological finding establishes the diagnosis of a thymic cyst?",
  [["Hassall corpuscles",
    "Correct. Hassall corpuscles are concentric epithelial structures found in the thymic medulla, "
    "so their presence identifies the tissue definitively. Imaging narrows the differential but "
    "cannot make the diagnosis, which is why biopsy is specified and treatment is surgical "
    "excision."],
   ["Keratin debris within a squamous-lined sac",
    "That describes a cholesteatoma or an epidermoid cyst. It indicates squamous epithelium rather "
    "than thymic tissue."],
   ["Ectopic thyroid follicles",
    "Thyroid follicles within a tract point to a thyroglossal duct cyst, and their presence is "
    "precisely why every such specimen is examined for carcinoma."],
   ["Filamentous branching organisms",
    "Those indicate actinomycosis, an infection presenting as a painless fluctuant submandibular "
    "mass and treated with penicillin."]], C(29)),

Q("Toxoplasmosis", IO, "How is toxoplasmosis contracted?",
  [["Poorly cooked meat or ingestion of oocytes in cat faeces",
    "Correct. Toxoplasma gondii reaches humans through undercooked meat or through oocysts shed in "
    "cat faeces. Patients present with fever, malaise, sore throat and myalgias alongside the "
    "adenopathy, diagnosis is serologic, and treatment is sulfonamides or pyrimethamine."],
   ["A cat scratch",
    "A scratch transmits Bartonella henselae, causing cat scratch disease with preauricular and "
    "submandibular nodes. Both involve cats, which is what makes them easy to confuse, but the route "
    "and the organism differ."],
   ["Unpasteurised milk",
    "Unpasteurised milk transmits Brucella, which causes total-body lymphadenopathy with fever, "
    "fatigue and malaise, treated with trimethoprim-sulfamethoxazole or tetracycline."],
   ["Tick bites and contact with rabbits",
    "Those transmit Francisella tularensis, producing tonsillitis with painful adenopathy and "
    "treated with streptomycin."]], C(33)),

Q("Non-infectious inflammation", IO,
  "Which conditions are listed as non-infectious inflammatory causes of neck masses?",
  [["Sjogren syndrome, sarcoidosis, IgG4-related sialadenitis and Kawasaki disease",
    "Correct. These are generally autoimmune in origin, and most patients have other symptoms that "
    "point toward the underlying disorder. Recognising them matters because the workup and treatment "
    "differ entirely from an infective or neoplastic mass."],
   ["Tuberculosis, actinomycosis and cat scratch disease",
    "Those are all granulomatous INFECTIONS, each with its own organism and exposure history. They "
    "sit on the infectious branch of the differential."],
   ["Lymphoma, thyroid carcinoma and metastatic squamous cell carcinoma",
    "Those are neoplastic causes, forming the branch that the red-flag list is designed to "
    "identify."],
   ["Branchial cleft cyst, thyroglossal duct cyst and dermoid cyst",
    "Those are congenital masses, which present in childhood or early adulthood and are usually "
    "noticed when they become infected."]], C(35)),

Q("Fungal infection", IO,
  "Which organisms most commonly cause fungal neck infection in the immunocompromised?",
  [["Candida, Histoplasma and Aspergillus",
    "Correct. Immunocompromised patients are particularly susceptible to these three, and the "
    "emphasis is that fungal cultures AND serology are needed for diagnosis, because they will not "
    "be found unless specifically sought. Treatment is amphotericin B, given aggressively."],
   ["Staphylococcus aureus and group A Streptococcus",
    "Those are the bacterial causes of suppurative lymphadenopathy in immunocompetent patients, "
    "treated with empirical antibacterial therapy."],
   ["Mycobacterium tuberculosis and atypical mycobacteria",
    "Mycobacteria are the granulomatous causes, diagnosed by acid-fast stain and culture and treated "
    "with multi-drug antituberculous regimens."],
   ["Bartonella henselae and Toxoplasma gondii",
    "Those are the zoonotic causes tied to cat exposure, diagnosed serologically rather than by "
    "fungal culture."]], C(35)),
]
