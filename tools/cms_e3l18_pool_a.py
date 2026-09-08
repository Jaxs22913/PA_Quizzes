# -*- coding: utf-8 -*-
"""Lecture 18 objective-style pool A -- Neoplasms and Neck Masses.

Four options, key authored first, deep explanations. See _cmse3_q.py.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Neck masses and neoplasms: the triangles and lymph nodes of the neck; and the etiologies, "
      "epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, and prognosis")
C = lambda n: "CMS I Neoplasms and Neck Masses, Slide %d" % n

QUESTIONS = [

Q("Neck anatomy", IO, "Which muscle divides the neck into anterior and posterior triangles?",
  [["Sternocleidomastoid",
    "Correct. The neck is bounded by the mandible above and the clavicle below, and the "
    "sternocleidomastoid runs obliquely across it, splitting it into an anterior and a posterior "
    "triangle. Those two are then subdivided further by the omohyoid and digastric muscles."],
   ["Trapezius",
    "Trapezius forms the posterior BOUNDARY of the posterior triangle rather than dividing the neck. "
    "The triangle is bounded by sternocleidomastoid in front, trapezius behind and clavicle below."],
   ["Omohyoid",
    "The omohyoid subdivides the posterior triangle into the occipital and supraclavicular "
    "triangles, and contributes to the anterior subdivisions. It divides within a triangle rather "
    "than creating the two main ones."],
   ["Digastric",
    "The digastric subdivides the anterior triangle, its two bellies bounding the digastric or "
    "submandibular triangle. Like omohyoid it works inside a triangle already created by "
    "sternocleidomastoid."]], C(4)),

Q("Neck anatomy", IO, "Which muscle divides the posterior triangle into its two subdivisions?",
  [["Omohyoid",
    "Correct. The omohyoid crosses the posterior triangle and splits it into the occipital triangle "
    "above and the supraclavicular triangle below. That division matters because the contents "
    "differ sharply: the spinal accessory nerve crosses the occipital floor, while the "
    "supraclavicular triangle holds the subclavian artery and brachial plexus."],
   ["Digastric",
    "The digastric divides the ANTERIOR triangle, with its two bellies bounding the submandibular "
    "triangle. It does not reach the posterior triangle."],
   ["Sternocleidomastoid",
    "The sternocleidomastoid creates the posterior triangle by forming its anterior boundary. A "
    "boundary cannot also be the structure that subdivides the space it encloses."],
   ["Mylohyoid",
    "Mylohyoid forms the FLOOR of the submental triangle in the anterior group. It is a floor "
    "rather than a dividing strap, and it is nowhere near the posterior triangle."]], C(5)),

Q("Neck anatomy", IO,
  "Which structure crosses the muscular floor of the occipital triangle to pass deep to trapezius?",
  [["The spinal accessory nerve",
    "Correct. The spinal accessory nerve runs across the occipital triangle's muscular floor before "
    "passing deep to trapezius, which leaves it superficial and exposed in the posterior triangle. "
    "That is why it is the classic nerve injured during posterior triangle surgery or lymph node "
    "biopsy, producing a painful drooping shoulder."],
   ["The vagus nerve",
    "The vagus lies in the carotid sheath within the carotid triangle of the anterior group, "
    "alongside the carotid arteries and internal jugular vein. It never enters the posterior "
    "triangle."],
   ["The hypoglossal nerve",
    "The hypoglossal nerve sits in the digastric triangle with the submandibular gland and facial "
    "vessels, supplying the tongue. That is an anterior triangle structure."],
   ["The phrenic nerve",
    "The phrenic nerve runs on the anterior surface of scalenus anterior, deep to the prevertebral "
    "fascia, rather than crossing the occipital triangle's floor superficially."]], C(5)),

Q("Neck anatomy", IO,
  "What lies DEEP to the contents of the supraclavicular triangle?",
  [["The cupola of the pleural cavity",
    "Correct. The supraclavicular triangle contains the terminal subclavian artery, the roots, "
    "trunks and divisions of the brachial plexus, thyrocervical trunk branches and tributaries of "
    "the external jugular vein. The dome of the pleura sits deep to all of them, which is why a "
    "penetrating wound there can cause a pneumothorax."],
   ["The thyroid gland",
    "The thyroid sits in the muscular triangle of the anterior group, with the parathyroids, "
    "larynx, trachea and oesophagus. It is anterior and midline rather than supraclavicular."],
   ["The submandibular gland",
    "The submandibular gland lies in the digastric triangle beneath the mandible, which is at the "
    "opposite end of the neck from the supraclavicular region."],
   ["The parotid gland",
    "The parotid lies on the side of the face over the masseter, well above the clavicle, and drains "
    "through Stensen duct into the mouth."]], C(5)),

Q("Neck anatomy", IO,
  "Which triangle contains the carotid arteries, internal jugular vein and vagus nerve?",
  [["The carotid triangle",
    "Correct. The carotid triangle is bounded by sternocleidomastoid behind, the posterior belly of "
    "digastric above and omohyoid below, and it houses the carotid arteries, internal jugular vein "
    "and vagus nerve. Knowing the boundaries lets you predict what lies beneath before making an "
    "incision."],
   ["The muscular triangle",
    "The muscular triangle holds the thyroid, parathyroids, larynx, trachea, oesophagus and the "
    "thyroid and cricoid cartilages. Those are the midline visceral structures rather than the great "
    "vessels."],
   ["The submental triangle",
    "The submental triangle is bounded by the anterior belly of digastric, the midline and the hyoid, "
    "with mylohyoid as its floor. It is small and superficial with no major vessels."],
   ["The occipital triangle",
    "The occipital triangle is in the posterior group and carries the spinal accessory nerve across "
    "its floor, with the cutaneous nerves of the neck in the overlying fascia."]], C(6)),

Q("Lymphatic drainage", IO,
  "Which nodes drain the scalp, auricle and middle ear?",
  [["Occipital, retroauricular and parotid nodes",
    "Correct. Superficial cervical nodes are named for where they sit, and their territories follow "
    "position: the occipital, retroauricular and parotid groups take lymph from the scalp, the "
    "auricle and the middle ear. All of them then drain onward into the deep cervical chain."],
   ["Submandibular nodes",
    "Submandibular nodes drain the face, sinuses, mouth and tongue. They are the group that enlarges "
    "with dental and oral infection rather than with scalp or ear disease."],
   ["Retropharyngeal nodes",
    "Retropharyngeal nodes are not truly superficial and receive lymph from the deeper structures of "
    "the head, including the upper pharynx. They are also the nodes whose suppuration produces a "
    "retropharyngeal abscess."],
   ["Supraclavicular nodes",
    "Supraclavicular nodes drain the thorax and abdomen, which is why an enlarged left "
    "supraclavicular node raises the possibility of an abdominal malignancy rather than head and "
    "neck disease."]], C(11)),

Q("Lymphatic drainage", IO,
  "Which deep cervical node is specifically concerned with drainage of the palatine tonsil?",
  [["The jugulodigastric node",
    "Correct. Two deep cervical nodes carry named territories. The jugulodigastric node drains the "
    "palatine tonsil, which is why tonsillitis produces a tender node high in the jugular chain just "
    "below the angle of the jaw, and why that is the node examined in a sore throat."],
   ["The juguloomohyoid node",
    "The juguloomohyoid node is the other named one, and its territory is the TONGUE. The two are "
    "easy to reverse, which is why they are worth learning together as a pair."],
   ["The submental node",
    "Submental nodes sit beneath the chin and drain the lower lip, chin and floor of mouth. They are "
    "superficial rather than part of the named deep cervical pair."],
   ["The retroauricular node",
    "Retroauricular nodes drain the scalp and auricle alongside the occipital and parotid groups, "
    "with no tonsillar territory."]], C(12)),

Q("Lymphatic drainage", IO,
  "Into what do the deep cervical nodes on the LEFT side ultimately drain?",
  [["The thoracic duct",
    "Correct. The deep cervical chain empties into the thoracic duct on the left, which itself joins "
    "the junction of the left internal jugular and left subclavian veins. On the right the "
    "equivalent structure is the right lymphatic duct, draining into the corresponding location on "
    "that side."],
   ["The right lymphatic duct",
    "The right lymphatic duct serves the RIGHT side of the head and neck, draining into the junction "
    "of the right internal jugular and subclavian veins. Sidedness is the whole distinction here."],
   ["Directly into the superior vena cava",
    "Lymph reaches the venous system through a duct at a specific venous junction rather than "
    "emptying into a great vein directly. That junction is at the root of the neck."],
   ["The cisterna chyli",
    "The cisterna chyli is the dilated origin of the thoracic duct in the ABDOMEN, receiving "
    "intestinal and lumbar trunks. Lymph flows from it upward, not into it from the neck."]], C(12)),

Q("Neck mass evaluation", IO,
  "Most neck masses in patients under 40 are of what nature?",
  [["Inflammatory, with Hodgkin lymphoma as the exception",
    "Correct. Under 40 the great majority of neck masses are inflammatory, usually reactive "
    "adenopathy following an upper respiratory infection. Hodgkin lymphoma is named as the specific "
    "exception, which is why a persistent painless node in a young patient still deserves attention "
    "despite the favourable base rate."],
   ["Neoplastic, with infection as the exception",
    "This inverts the rule. Treating every young patient's neck lump as presumptively malignant "
    "would generate a great deal of unnecessary investigation for what is usually reactive."],
   ["Congenital, with infection as the exception",
    "Congenital masses such as branchial cleft and thyroglossal duct cysts do present in this age "
    "group, but usually only when they become infected, and they are far less common overall than "
    "reactive adenopathy."],
   ["Vascular, with neoplasia as the exception",
    "Vascular masses are identified by pulsatility or a bruit and are uncommon. They are a distinct "
    "category rather than the dominant one at any age."]], C(13)),

Q("Neck mass evaluation", IO,
  "Which size threshold appears on the list of features suggesting malignancy in a neck mass?",
  [["Greater than 1.5 centimetres",
    "Correct. The malignancy features are: no infectious origin, duration over two weeks, size over "
    "1.5 centimetres, firm and non-cystic and non-tender with little or no mobility, age over 40, "
    "and tobacco and alcohol use. Size alone is not diagnostic, but it is one of the criteria that "
    "shifts the prior."],
   ["Greater than 5 centimetres",
    "Waiting for a mass to reach 5 centimetres would delay diagnosis substantially, and many "
    "malignant nodes present well below that. The threshold is set low deliberately."],
   ["Greater than 0.5 centimetres",
    "Half a centimetre is within the range of normal palpable nodes in many people, particularly in "
    "the submandibular region, so it would flag far too many benign findings."],
   ["Greater than 3 centimetres",
    "Three centimetres is comfortably abnormal but is not the stated threshold, and using it would "
    "miss the 1.5 to 3 centimetre range where many malignant nodes are found."]], C(13)),

Q("Neck mass evaluation", IO,
  "A neck mass that is pulsatile or has a bruit indicates what?",
  [["A vascular lesion",
    "Correct. This is one of four rules of thumb. Pulsatility or a bruit means vascular, which puts "
    "paraganglioma at the head of the differential and makes computed tomography angiography the "
    "next investigation. It also means the mass must not be biopsied blindly."],
   ["A cystic lesion",
    "Fluctuance, not pulsatility, indicates a cystic lesion. Both suggest something other than solid "
    "tissue, but they are distinguished by whether the movement is synchronous with the pulse."],
   ["A benign lesion present for years",
    "A mass present for years is usually benign, typically a lipoma or a cyst, but that is a "
    "conclusion from DURATION rather than from pulsatility."],
   ["Lymphoma",
    "Rapid growth without infective symptoms suggests lymphoma. Lymphomatous nodes are firm or "
    "rubbery and do not transmit a pulse."]], C(13)),

Q("Neck mass evaluation", IO,
  "A rapidly growing neck mass WITHOUT other infectious symptoms suggests what?",
  [["Lymphoma",
    "Correct. The rule pairs tempo with context: rapid growth is usually infectious when other "
    "symptoms accompany it, and lymphoma when they do not. The absence of fever, sore throat or a "
    "preceding upper respiratory infection is what redirects a fast-growing mass toward "
    "malignancy."],
   ["Reactive viral lymphadenopathy",
    "Reactive nodes follow an identifiable upper respiratory infection and regress within one to two "
    "weeks. Growth without any infective context is the opposite pattern."],
   ["A lipoma",
    "Lipomas grow imperceptibly over years and are soft and mobile. Rapid enlargement is entirely "
    "out of character for one."],
   ["A branchial cleft cyst",
    "A branchial cleft cyst enlarges rapidly only when it becomes infected, in which case there are "
    "infective symptoms and overlying erythema. Without those it stays quiet."]], C(13)),

Q("Neck mass workup", IO,
  "What is the standard of care investigation for a persistent neck mass?",
  [["Fine needle aspiration biopsy",
    "Correct. Aspiration separates neoplasm from inflammation and carcinoma from lymphoma, and "
    "provides material for cytology, Gram stain and culture. A minimum of four separate needle "
    "passes is required for adequacy, because a single pass can miss a focal deposit within an "
    "otherwise reactive node."],
   ["Excisional biopsy",
    "Excision is specifically avoided as the first step in a suspected malignant node, because "
    "opening it spills tumour into the neck and complicates both the surgical field and the "
    "radiotherapy field afterwards."],
   ["Positron emission tomography",
    "Positron emission tomography shows metabolic uptake and is useful for staging or hunting an "
    "occult primary, but it is positive in inflammation as well as cancer and gives no tissue "
    "diagnosis."],
   ["Plain radiography of the neck",
    "Plain films cannot characterise a soft tissue mass, distinguish solid from cystic, or guide a "
    "biopsy. They would not alter management."]], C(18)),

Q("Neck mass workup", IO,
  "How many separate needle passes are required for an adequate fine needle aspiration?",
  [["A minimum of four",
    "Correct. Sampling error is the main limitation of aspiration cytology, because a node may "
    "contain a small focus of tumour among otherwise reactive tissue. Four separate passes sample "
    "different parts of the node and make a falsely reassuring result much less likely."],
   ["One, provided material is obtained",
    "Obtaining material and obtaining representative material are different. A single pass can draw "
    "reactive lymphocytes from a node that also contains carcinoma."],
   ["Two",
    "Two passes improve on one but fall below the stated minimum. The number is specified precisely "
    "because sampling adequacy determines whether the result can be trusted."],
   ["Ten",
    "Ten passes increase bleeding, discomfort and the theoretical risk of seeding without improving "
    "diagnostic yield beyond the point where four already suffices."]], C(18)),

Q("Neck mass workup", IO,
  "Why is iodine-containing contrast avoided when thyroid cancer is suspected?",
  [["It compromises subsequent radioiodine treatment",
    "Correct. The thyroid takes up iodine avidly, so a contrast load saturates the gland and any "
    "tumour within it. Radioiodine therapy depends on that same uptake mechanism, so giving contrast "
    "first can delay definitive treatment for weeks until the iodine has cleared."],
   ["It causes an allergic reaction in thyroid disease",
    "Contrast allergy is unrelated to thyroid pathology and occurs at the same rate as in anyone "
    "else. The problem here is pharmacological interference rather than hypersensitivity."],
   ["It obscures the thyroid on imaging",
    "Contrast improves rather than obscures visualisation of the thyroid and surrounding structures. "
    "The objection is entirely about what comes afterwards."],
   ["It triggers a thyroid storm in all patients",
    "An iodine load can precipitate thyrotoxicosis in a patient with an autonomous nodule, which is "
    "a real if uncommon concern, but the stated reason relates to treatment rather than to an acute "
    "reaction."]], C(18)),

Q("Congenital neck masses", IO,
  "Where does a branchial cleft cyst characteristically present?",
  [["Laterally, at the anterior border of the sternocleidomastoid",
    "Correct. Branchial cleft cysts arise from pharyngobranchial ducts that fail to obliterate "
    "during fetal development, and they sit laterally along the anterior border of the "
    "sternocleidomastoid. That position is the first branch of the congenital differential: lateral "
    "against midline."],
   ["In the midline of the anterior neck",
    "Midline congenital masses are thyroglossal duct cysts and dermoids. Position is the primary "
    "discriminator, so placing a branchial cleft cyst midline reverses the basic rule."],
   ["In the posterior triangle",
    "Lymphangiomas commonly occupy the posterior triangle. Branchial cleft cysts follow the "
    "sternocleidomastoid's anterior edge instead."],
   ["Within the sternocleidomastoid muscle itself",
    "A mass within the muscle belly in an infant is a sternocleidomastoid tumour of infancy, "
    "associated with congenital torticollis. A branchial cleft cyst lies alongside the muscle rather "
    "than inside it."]], C(22)),

Q("Congenital neck masses", IO,
  "Why is incision and drainage avoided in an infected branchial cleft cyst?",
  [["It makes the definitive excision harder",
    "Correct. Opening the cyst scars the tissue planes, which makes it much more difficult to define "
    "and follow the tract at the definitive operation. Since recurrence depends on removing the "
    "whole tract, anything that obscures it matters. Even with frank abscess, needle aspiration and "
    "decompression are preferred."],
   ["It causes the cyst to become malignant",
    "Drainage does not induce malignant change. The relevant malignancy point is different: human "
    "papillomavirus-associated squamous cell carcinoma must be excluded before accepting a "
    "congenital diagnosis in an adult."],
   ["It always leads to a permanent fistula",
    "A persistent sinus is a recognised complication of incomplete surgery rather than an inevitable "
    "result of drainage, and the stated objection is about the difficulty of the later excision."],
   ["It spreads the infection to the mediastinum",
    "Mediastinal spread is the danger of a retropharyngeal abscess, whose space runs from skull base "
    "to posterior mediastinum. A branchial cleft cyst does not communicate with that space."]], C(22)),

Q("Congenital neck masses", IO,
  "What proportion of congenital neck masses are thyroglossal duct cysts?",
  [["About one third",
    "Correct. Thyroglossal duct cysts account for roughly a third of all congenital neck masses, "
    "which makes them the commonest and gives a midline lump in a child a strong prior probability. "
    "Their location can vary, with some presenting lateral or as low as the thyroid gland."],
   ["About 5 per cent",
    "This would make them a rarity, which would change how a midline neck mass is approached. They "
    "are in fact the leading congenital cause."],
   ["About 90 per cent",
    "Nine in ten would leave almost no room for branchial cleft cysts, lymphangiomas, dermoids, "
    "teratomas and thymic cysts, all of which are recognised entities."],
   ["About 15 per cent",
    "This understates their share. The figure matters because it is what justifies thinking of them "
    "first when a midline mass appears."]], C(23)),

Q("Congenital neck masses", IO,
  "Which sign is pathognomonic for a thyroglossal duct cyst?",
  [["Vertical movement with swallowing or tongue protrusion",
    "Correct. The thyroid descends from the foramen caecum at the tongue base through the hyoid "
    "during development, so a persistent tract tethers the cyst to the hyoid. Protruding the tongue "
    "pulls the hyoid and therefore the cyst upward, which no other neck mass does."],
   ["Transillumination",
    "Transillumination is the sign of a lymphangioma, which contains clear lymph that lets light "
    "pass. A thyroglossal duct cyst contains mucoid fluid and does not transmit light in that way."],
   ["Enlargement with crying or straining",
    "Enlargement on straining indicates a vascular lesion, characteristically a haemangioma, whose "
    "venous channels engorge when intrathoracic pressure rises."],
   ["Fluctuance with overlying erythema",
    "Those describe an infected or abscessed mass of any origin. They indicate infection rather than "
    "identifying which structure is infected."]], C(23)),
]
