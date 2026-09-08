# -*- coding: utf-8 -*-
"""Lecture 18 vignette pool C -- Neoplasms and Neck Masses."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Neck masses and neoplasms: the triangles and lymph nodes of the neck; and the etiologies, "
      "epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, and prognosis")
C = lambda n: "CMS I Neoplasms and Neck Masses, Slide %d" % n

QUESTIONS = [

Q("Neck mass duration", IO,
  "A 55-year-old man has had a firm neck lump for three days after a heavy cold, with a sore "
  "throat and mild fever.",
  [["Treat the infection and reassess in two weeks",
    "Correct. Three days with an obvious infective context sits inside the window where reactive "
    "adenopathy is expected, and reactive nodes regress in one to two weeks. Duration over two weeks "
    "is what appears on the malignancy list, so the appropriate move is to treat what is there and "
    "reassess at that threshold."],
   ["Fine needle aspiration today",
    "Aspiration is the standard for a PERSISTENT mass, and persistence is precisely what has not yet "
    "been established. Biopsying every reactive node after a cold would be a great deal of "
    "unnecessary intervention."],
   ["Urgent referral for suspected malignancy",
    "Age over 40 is one red flag, but the mass has an infectious origin and has been present three "
    "days, which are two flags pointing the other way."],
   ["Excisional biopsy",
    "Excision is avoided even in suspected malignancy because it spills tumour, and here there is no "
    "reason to suspect malignancy in the first place."]], C(13)),

Q("Lipoma", IO,
  "A 48-year-old woman has a soft, mobile, painless neck lump that she says has been there for at "
  "least ten years and has barely changed.",
  [["A benign lesion such as a lipoma or a cyst",
    "Correct. A mass present for years is usually benign, and lipoma or cyst are the two named "
    "examples. Duration in that range is reassuring in the way that duration over two weeks is "
    "concerning, and the soft mobile texture supports it."],
   ["Metastatic squamous cell carcinoma",
    "Metastatic nodes are firm, immobile and enlarge over weeks to months. Ten years of stability is "
    "incompatible with malignant behaviour."],
   ["Lymphoma",
    "Lymphoma presents as a rapidly growing mass, often with night sweats and weight loss. A decade "
    "of no change is the opposite pattern."],
   ["Branchial cleft cyst",
    "A branchial cleft cyst is congenital and could indeed have been present for years, so it is a "
    "fair thought, but it sits specifically at the anterior sternocleidomastoid border and declares "
    "itself when infected."]], C(13)),

Q("Neck mass consistency", IO,
  "A clinician palpates a neck mass and finds it fluctuant.",
  [["A cystic lesion",
    "Correct. Fluctuance means the mass transmits pressure the way a fluid would, so it contains "
    "liquid rather than solid tissue. That is one of the four rules of thumb, sitting alongside "
    "pulsatility for vascular, years of stability for benign, and rapid growth for infection or "
    "lymphoma."],
   ["A vascular lesion",
    "Vascular masses are identified by pulsatility or a bruit. Both fluctuance and pulsatility "
    "suggest non-solid contents, but they are distinguished by whether the movement follows the "
    "pulse."],
   ["A metastatic node",
    "Malignant nodes are characteristically firm or hard and immobile. Fluctuance argues against "
    "malignancy, though a necrotic node can occasionally feel cystic."],
   ["A lipoma",
    "A lipoma is soft and doughy and can be mistaken for fluid, but it does not fluctuate because it "
    "is solid fat."]], C(13)),

Q("Thyroid mass", IO,
  "A 52-year-old woman has an immobile midline neck mass that rises when she swallows.",
  [["The thyroid",
    "Correct. The thyroid is bound to the larynx and trachea by the pretracheal fascia, so it rises "
    "when the larynx rises during a swallow. That movement identifies the gland as the source and "
    "separates it from a node or cyst that stays still, and it should prompt ultrasound with "
    "aspiration, thyroid-stimulating hormone and T3 and T4."],
   ["A lymph node",
    "Nodes have no attachment to the laryngeal skeleton so they do not move with swallowing, and "
    "they are lateral rather than midline."],
   ["A branchial cleft cyst",
    "A branchial cleft cyst is lateral, at the sternocleidomastoid border, with no laryngeal "
    "attachment, so neither its position nor its movement fits."],
   ["A thyroglossal duct cyst",
    "A thyroglossal duct cyst IS midline and does rise with swallowing, which makes this the "
    "strongest distractor. The discriminator is tongue protrusion: it moves the cyst but not the "
    "thyroid."]], C(40)),

Q("Thyroid nodule risk", IO,
  "A 27-year-old woman has a thyroid nodule. She had radiotherapy to the neck as a child for "
  "lymphoma.",
  [["Her childhood irradiation raises the risk of thyroid malignancy",
    "Correct. Childhood head and neck irradiation is on the risk list for thyroid cancer, alongside "
    "age under 30 or over 60, full body irradiation for bone marrow transplantation, family history "
    "of thyroid cancer, and multiple endocrine neoplasia type 2. It changes the threshold for "
    "investigating a nodule rather than the method."],
   ["Previous radiotherapy makes malignancy less likely",
    "This inverts a well-established relationship. Radiation exposure to the thyroid is one of the "
    "clearest risk factors for later thyroid carcinoma."],
   ["Her age of 27 makes malignancy essentially impossible",
    "Age under 30 is itself on the risk list rather than reassuring, and papillary carcinoma is "
    "commonest in young women."],
   ["Radiotherapy history is relevant only for lymphoma recurrence",
    "Recurrence is worth considering, but the thyroid within the irradiated field carries its own "
    "independent risk of a new primary."]], C(40)),

Q("Thyroid nodule size", IO,
  "A 46-year-old man has a 1.4 centimetre thyroid nodule found incidentally on imaging done for "
  "another reason.",
  [["Nodules over 1 centimetre found incidentally warrant evaluation",
    "Correct. Incidental nodules greater than 1 centimetre should be evaluated further, and this one "
    "exceeds that. Evaluation means ultrasound with fine needle aspiration plus thyroid-stimulating "
    "hormone and thyroid hormones, with recent growth, dysphagia or obstruction as the concerning "
    "symptoms to ask about."],
   ["Incidental nodules never require follow-up",
    "That would leave a large number of clinically significant nodules undetected, which is why a "
    "size threshold exists at all."],
   ["Only nodules over 4 centimetres are evaluated",
    "Four centimetres is a large nodule that would usually be palpable. Setting the threshold there "
    "would miss most early disease."],
   ["Evaluation is needed only if the patient is hyperthyroid",
    "Thyroid function guides the ORDER of investigation, determining whether a scan precedes "
    "aspiration, but it does not determine whether a nodule is investigated at all."]], C(40)),

Q("Neck mass evaluation", IO,
  "A 44-year-old woman with a neck mass is asked a series of history questions. Which exposure is "
  "specifically relevant?",
  [["Recent travel and possible tuberculosis exposure",
    "Correct. The history should cover recent upper respiratory, sinus, ear or other head and neck "
    "infection, exposure to pets and animals, recent travel and tuberculosis exposure, malignancy "
    "risk including previous skin lesion excision, smoking, alcohol, radiation and family history, "
    "recent trauma, and immunodeficiency."],
   ["Dietary iodine intake alone",
    "Iodine matters to thyroid physiology and to the contrast question, but it is not one of the "
    "exposure items in the history for a neck mass generally."],
   ["Occupational noise exposure",
    "Noise exposure belongs to the assessment of hearing loss. It has no bearing on a neck mass."],
   ["Sun exposure only",
    "Sun exposure is relevant to skin malignancy, which can metastasise to the neck, so it is part "
    "of the malignancy risk question rather than a standalone item."]], C(14)),

Q("General symptoms", IO,
  "A 58-year-old man with a neck mass reports night sweats, weight loss, hoarseness and dysphagia.",
  [["These are the general symptoms that accompany a concerning neck mass",
    "Correct. The general clinical presentation listed includes fever, postnasal drip, rhinorrhoea, "
    "sore throat, otalgia, night sweats, weight loss, malaise, dysphagia and hoarseness. Hoarseness "
    "and dysphagia in particular suggest involvement of the upper aerodigestive tract."],
   ["These symptoms indicate a congenital cyst",
    "Congenital masses are asymptomatic until infected and do not produce constitutional symptoms or "
    "aerodigestive dysfunction."],
   ["These symptoms are typical of reactive adenopathy",
    "Reactive nodes accompany an upper respiratory infection with local symptoms, not weight loss "
    "and night sweats."],
   ["These symptoms suggest a benign lipoma",
    "A lipoma produces no symptoms at all beyond the lump itself. Systemic features exclude it."]],
  C(15)),

Q("Node description", IO,
  "A clinician documents a cervical node as immobile, firm and non-tender.",
  [["Features that raise concern for malignancy",
    "Correct. The descriptors that matter are size, shape, mobility, consistency and tenderness. "
    "Immobility suggests fixation to surrounding structures by tumour, firmness suggests solid "
    "tissue rather than fluid, and non-tenderness points away from inflammation, which hurts."],
   ["Features typical of an inflammatory node",
    "Inflammatory nodes are tender and usually mobile, because inflammation is painful and does not "
    "fix the node to its surroundings."],
   ["Features indicating a cystic lesion",
    "A cyst would be fluctuant and often mobile rather than firm and fixed. Consistency is the "
    "discriminator here."],
   ["Features indicating a vascular lesion",
    "Vascular masses are identified by pulsation or a bruit. Nothing about firmness and immobility "
    "suggests arterial flow."]], C(93)),

Q("Congenital versus adult", IO,
  "A 6-year-old girl has a lateral neck mass. Using the age-based framework, which category should "
  "be considered first?",
  [["Congenital, and lateral position points to a branchial cleft cyst",
    "Correct. The differential splits first by age. In a child the congenital branch is considered, "
    "and within it position separates lateral from midline: lateral gives branchial cleft cyst, "
    "lymphadenopathy or cystic hygroma, while midline gives thyroglossal duct cyst."],
   ["Neoplastic, since all neck masses are malignant until proven otherwise",
    "That presumption applies to a NEW neck mass in an adult. In a child the base rate runs strongly "
    "the other way, with Hodgkin lymphoma as the exception."],
   ["Inflammatory, and lateral position points to Ludwig angina",
    "Inflammatory causes are common in children, so the category is reasonable, but Ludwig angina is "
    "a submental and submandibular floor-of-mouth infection rather than a lateral neck mass."],
   ["Endocrine, pointing to a parathyroid cyst",
    "Endocrine causes such as thymic cyst, thyroid hyperplasia and parathyroid cyst sit on the "
    "KITTENS list but are uncommon and not suggested by a lateral mass in a child."]], C(17)),

Q("Neck triangles", IO,
  "A surgeon plans an approach through the triangle bounded by the mandible above and the two "
  "bellies of digastric.",
  [["The submandibular gland, hypoglossal nerve and facial vessels",
    "Correct. Those boundaries define the digastric or submandibular triangle, whose contents are "
    "the stylohyoid, mylohyoid and hyoglossus muscles, the submandibular gland, the hypoglossal "
    "nerve and the facial vessels. Predicting contents from boundaries is the practical point of the "
    "triangle scheme."],
   ["The carotid arteries and vagus nerve",
    "Those lie in the carotid triangle, bounded by sternocleidomastoid behind, the posterior belly "
    "of digastric above and omohyoid below."],
   ["The brachial plexus and subclavian artery",
    "Those are in the supraclavicular triangle of the posterior group, above the middle of the "
    "clavicle, with the pleural cupola deep to them."],
   ["The thyroid, trachea and oesophagus",
    "Those occupy the muscular triangle, between omohyoid above, sternocleidomastoid below and the "
    "midline in front."]], C(6)),

Q("Neck triangles", IO,
  "A wound in the posterior triangle has injured a nerve, and the patient now has a drooping, "
  "painful shoulder.",
  [["The spinal accessory nerve",
    "Correct. The spinal accessory nerve crosses the muscular floor of the occipital triangle before "
    "passing deep to trapezius, which leaves it superficial and exposed. Denervating trapezius "
    "produces exactly the painful drooping shoulder described, and it is the classic injury of "
    "posterior triangle surgery."],
   ["The vagus nerve",
    "The vagus runs in the carotid sheath in the anterior triangle and supplies the larynx and "
    "viscera. Injury gives hoarseness rather than shoulder weakness."],
   ["The hypoglossal nerve",
    "The hypoglossal nerve lies in the digastric triangle and supplies the tongue, so injury causes "
    "tongue deviation rather than shoulder problems."],
   ["The phrenic nerve",
    "The phrenic nerve lies on scalenus anterior deep to the prevertebral fascia and supplies the "
    "diaphragm, so injury causes hemidiaphragm paralysis."]], C(5)),

Q("Lymphatic drainage", IO,
  "A 24-year-old has tonsillitis and a tender node high in the jugular chain just below the angle "
  "of the jaw.",
  [["The jugulodigastric node, which drains the palatine tonsil",
    "Correct. The deep cervical chain has two named members with defined territories, and the "
    "jugulodigastric node drains the palatine tonsil. That is why tonsillitis reliably produces "
    "tenderness at this precise point, and why it is the node examined in a sore throat."],
   ["The juguloomohyoid node, which drains the tongue",
    "The juguloomohyoid node is the other named one and its territory is the TONGUE. The pairing is "
    "easy to reverse, which is why the two are worth learning together."],
   ["The submental node",
    "Submental nodes drain the lower lip, chin and floor of mouth. They sit beneath the chin rather "
    "than in the jugular chain."],
   ["The supraclavicular node",
    "Supraclavicular nodes drain the thorax and abdomen, which is why enlargement there raises "
    "concern about disease below the diaphragm."]], C(12)),

Q("Referral timing", IO,
  "A 59-year-old woman's neck mass has persisted after a course of antibiotics.",
  [["Refer to a specialist now",
    "Correct. A trial of antibiotics is common practice, and failure of that trial is exactly the "
    "point at which referral should happen rather than another course being prescribed. Early and "
    "aggressive treatment is needed in some neoplastic conditions, so the delay costs more than the "
    "referral."],
   ["Prescribe a second, broader antibiotic course",
    "A second course repeats a strategy that has already failed and adds weeks of delay in a patient "
    "whose age alone is a malignancy red flag."],
   ["Wait until systemic symptoms develop",
    "Waiting for weight loss or night sweats means waiting for advanced disease. The red-flag list "
    "exists precisely to prompt action before that."],
   ["Discharge with advice to return if it grows",
    "Safety-netting has a place, but a mass that has already outlasted treatment in a patient over "
    "40 has met the criteria for referral now."]], C(19)),

Q("Neck neoplasm presentation", IO,
  "A 66-year-old man has an asymptomatic, slowly progressive, firm neck mass, with hoarseness and "
  "odynophagia.",
  [["A malignant neck neoplasm, most likely metastatic squamous carcinoma",
    "Correct. Malignant neck tumours are usually metastatic squamous cell carcinoma from skin or "
    "upper aerodigestive tract, and the described pattern is exactly that: asymptomatic lesions that "
    "progress slowly and feel firm, with hoarseness, dysphagia and odynophagia reflecting the "
    "primary site."],
   ["A benign soft tissue tumour",
    "Benign tumours arise from fat, salivary tissue, nodes, vessels and nerves and do not produce "
    "hoarseness or odynophagia, which indicate involvement of the aerodigestive tract."],
   ["An infected congenital cyst",
    "An infected cyst is tender and erythematous with systemic features of infection, developing "
    "over days rather than progressing slowly and painlessly."],
   ["Reactive lymphadenopathy",
    "Reactive nodes follow an identifiable infection and regress within weeks, without hoarseness or "
    "progressive growth."]], C(37)),
]
