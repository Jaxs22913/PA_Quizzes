# -*- coding: utf-8 -*-
"""Lecture 18, second pool -- Neoplasms and Neck Masses."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "CMS I Neoplasms and Neck Masses"
IO = ("Neck masses and neoplasms: the triangles and lymph nodes of the neck; and the etiologies, "
      "epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, and prognosis of common neck masses, "
      "vascular tumors, and benign and malignant neoplasms")

QUESTIONS = [

Q("Neck mass evaluation", IO,
  "A 47-year-old woman has a neck mass that is pulsatile and has an audible bruit.",
  [["A vascular lesion, most likely a paraganglioma",
    "Correct. The lecture gives four rules of thumb, and pulsatility or a bruit means vascular. "
    "Paragangliomas head the benign vascular list, arising at the carotid body, the vagus or the "
    "jugulotympanic region. The practical consequence is that this mass must not be biopsied blindly "
    "and needs computed tomography angiography before anything is put into it."],
   ["A lipoma, since it has been present a long time",
    "A mass present for years is usually benign and a lipoma is a common answer, but a lipoma is "
    "soft, mobile and completely avascular. Nothing about a lipoma pulses or generates a bruit."],
   ["A reactive lymph node",
    "Reactive nodes are firm or rubbery and are not pulsatile. Even a hypervascular node does not "
    "transmit a palpable pulse or produce a bruit audible on auscultation."],
   ["A branchial cleft cyst",
    "A branchial cleft cyst is a fluid-filled congenital structure at the sternocleidomastoid "
    "border, which would be fluctuant rather than pulsatile. Fluctuance and pulsatility indicate "
    "quite different contents."]],
  "diagnosis", D, 13),

Q("Neck mass evaluation", IO,
  "A 33-year-old man has a neck mass that has enlarged rapidly over three weeks. He has no fever, "
  "sore throat or other infective symptoms, but reports night sweats and weight loss.",
  [["Lymphoma",
    "Correct. The rule the lecture gives is that a rapidly growing mass is usually infectious IF "
    "there are other infective symptoms, and lymphoma if there are not. Here the rapid growth comes "
    "with constitutional B symptoms rather than infection, and lymphoma is also the noted exception "
    "to the rule that masses under 40 are usually inflammatory."],
   ["Reactive viral lymphadenopathy",
    "Reactive nodes follow an upper respiratory infection, regress within one to two weeks, and are "
    "not accompanied by night sweats and weight loss. Their whole course is one of resolution rather "
    "than progression."],
   ["A branchial cleft cyst that has become infected",
    "An infected congenital cyst is tender and erythematous with the systemic features of infection, "
    "and it appears at a site the patient often recalls having had a lump before. Night sweats and "
    "weight loss are not part of it."],
   ["A lipoma",
    "Lipomas are soft, slow-growing over years, and produce no systemic symptoms whatsoever. Three "
    "weeks of rapid growth is the opposite of a lipoma's behaviour."]],
  "diagnosis", D, 13),

Q("Thyroid mass imaging", IO,
  "A 49-year-old woman has a firm thyroid nodule with a hoarse voice. The clinician is deciding "
  "which imaging to request, and cancer is suspected.",
  [["Ultrasound, avoiding iodine-containing contrast",
    "Correct. Ultrasound characterises thyroid nodules well without radiation and guides "
    "aspiration. The specific trap is contrast computed tomography: an iodine load saturates the "
    "thyroid and compromises subsequent radioiodine treatment, so it is avoided whenever thyroid "
    "cancer is on the differential."],
   ["Contrast computed tomography of the neck",
    "Contrast computed tomography is the workhorse for most neck masses because it separates solid "
    "from cystic and shows vascularity, but the iodine in the contrast is exactly what must be "
    "avoided here, because it delays definitive treatment."],
   ["Positron emission tomography",
    "Positron emission tomography demonstrates metabolic activity and has a role in staging or "
    "hunting an occult primary. It is not a first-line test for characterising a thyroid nodule and "
    "is positive in inflammation as well as cancer."],
   ["Plain radiography of the neck",
    "Plain films show gross tracheal deviation or calcification but cannot characterise a thyroid "
    "nodule, assess lymph nodes, or guide a biopsy. They would not change management."]],
  "testing", D, 18),

Q("Fine needle aspiration", IO,
  "A clinician is performing fine needle aspiration of a suspicious cervical node and asks how many "
  "passes are needed.",
  [["A minimum of four separate passes",
    "Correct. A single pass samples one small volume and risks missing focal disease within a "
    "heterogeneous node, so the lecture specifies a minimum of four separate needle passes for "
    "collection. The material is used for cytology, Gram stain and culture, which is why adequacy of "
    "sampling determines whether the result can be trusted."],
   ["One pass, provided material is obtained",
    "Obtaining material and obtaining representative material are different things. A single pass "
    "through a node containing a small focus of carcinoma can return entirely reactive lymphocytes "
    "and produce a falsely reassuring report."],
   ["Two passes",
    "Two passes improve on one but still fall below the stated minimum, and the point of specifying "
    "a number is that sampling error is the main limitation of the technique rather than "
    "interpretation."],
   ["Ten passes, to guarantee adequacy",
    "Excessive passes increase bleeding, patient discomfort and the risk of seeding without a "
    "corresponding gain in diagnostic yield. Four is the stated threshold for adequacy."]],
  "testing", D, 18),

Q("Plunging ranula", IO,
  "A 24-year-old woman has a slowly growing, painless submental swelling. Imaging shows it arises "
  "from the sublingual gland and extends through the mylohyoid muscle into the neck.",
  [["Excision of the sublingual gland",
    "Correct. A ranula is a mucous retention cyst from the sublingual gland, and it is called "
    "plunging when it herniates through mylohyoid into the neck. Removing the cyst alone leaves the "
    "gland that produces the mucus, so it simply refills; excising the source gland is what prevents "
    "recurrence."],
   ["Marsupialisation of the cyst",
    "Marsupialisation opens the cyst to drain into the mouth and is sometimes used for simple oral "
    "ranulas, but recurrence is high and it does not address the plunging component that has already "
    "passed through the muscle."],
   ["Aspiration of the cyst contents",
    "Aspiration removes the mucus but leaves the secreting gland and the cavity intact, so the "
    "swelling returns within days to weeks. It is diagnostic at best rather than therapeutic."],
   ["Excision of the submandibular gland",
    "The submandibular gland is the wrong gland. A ranula arises specifically from the sublingual "
    "gland, and removing the submandibular one would leave the source untouched while causing "
    "unnecessary morbidity."]],
  "treatment", D, 25),

Q("Sternocleidomastoid tumour of infancy", IO,
  "A 6-week-old infant has a firm, painless, discrete mass within the right sternocleidomastoid "
  "muscle and holds his head tilted to that side.",
  [["Physical therapy, since around 80 per cent resolve spontaneously",
    "Correct. This lesion is associated with congenital torticollis and follows a predictable "
    "course: it enlarges for two to three months, then regresses over four to eight months, and "
    "about 80 per cent resolve on their own. The purpose of physical therapy is to prevent a fixed "
    "restrictive torticollis while that natural resolution takes place."],
   ["Immediate surgical excision",
    "Surgery is reserved for persistent cases that fail to regress, and operating on a lesion with "
    "an 80 per cent spontaneous resolution rate commits an infant to an unnecessary procedure with "
    "the risk of scarring the muscle further."],
   ["Fine needle aspiration to exclude malignancy",
    "Aspiration is the standard investigation for a suspicious neck mass in an adult, but a firm "
    "mass within the sternocleidomastoid of a neonate with torticollis has a characteristic clinical "
    "picture that does not require tissue."],
   ["Ultrasound followed by observation alone",
    "Ultrasound can confirm the lesion sits within the muscle, and observation is broadly right, but "
    "observation ALONE risks a fixed torticollis developing. The physical therapy is the active "
    "ingredient."]],
  "treatment", D, 29),

Q("Laryngocele", IO,
  "A 52-year-old professional trumpet player has hoarseness, cough and a sensation of a foreign "
  "body in the throat. Laryngoscopy shows a smooth dilation at the level of the false cord.",
  [["Laryngocele",
    "Correct. A laryngocele is abnormal dilation or herniation of the laryngeal saccule, and "
    "sustained raised intraluminal pressure from wind instrument playing is a classic association. "
    "The smooth dilation at the level of the false cord on laryngoscopy is the characteristic "
    "finding, and computed tomography confirms the diagnosis and defines its extent."],
   ["Vocal cord polyp",
    "A polyp is a discrete pedunculated mass on the vibrating margin of the true cord, not a smooth "
    "dilation at the false cord. It arises from vocal abuse and smoking rather than from sustained "
    "pressure."],
   ["Vocal cord papillomatosis",
    "Papillomatosis produces multiple friable warty growths caused by human papillomavirus subtypes "
    "6 and 11, affecting both true and false cords. Its appearance is exophytic and irregular rather "
    "than a smooth dilation."],
   ["Laryngeal carcinoma",
    "A malignancy would appear as an irregular ulcerated or exophytic mass, usually on the true "
    "cord, in a patient with a smoking history and progressive symptoms. A smooth dilation is not a "
    "tumour appearance."]],
  "diagnosis", D, 24),

Q("Teratoma", IO,
  "A newborn has a large firm neck mass noted at delivery. Imaging shows calcifications within it, "
  "and the infant has stridor.",
  [["Teratoma, requiring surgical excision",
    "Correct. Head and neck teratomas account for about 3.5 per cent of all teratomas, originate "
    "from pluripotent cells, and are most commonly noted at birth or within the first year. The "
    "calcifications reflect the varied tissue types a teratoma contains, and when large enough these "
    "masses cause respiratory compromise or dysphagia, which is why excision is needed."],
   ["Lymphangioma, managed with sclerotherapy",
    "A lymphangioma is soft, doughy and compressible and transilluminates because it contains clear "
    "lymph. It does not feel firm and does not calcify, which is what the imaging shows here."],
   ["Haemangioma, which will involute",
    "A haemangioma is a soft compressible vascular lesion that enlarges with crying and involutes "
    "after 18 to 24 months. It is not firm at birth and does not contain calcification."],
   ["Thyroglossal duct cyst",
    "A thyroglossal duct cyst is a midline structure that moves with tongue protrusion and typically "
    "presents in childhood when it becomes infected, not as a large firm calcified mass causing "
    "stridor at delivery."]],
  "diagnosis", D, 28),

Q("Tularemia", IO,
  "A 44-year-old man who hunts rabbits has fever, chills, headache and fatigue with tonsillitis and "
  "painful cervical adenopathy.",
  [["Streptomycin",
    "Correct. The exposure history of rabbits, ticks or contaminated water points to Francisella "
    "tularensis, and the described combination of tonsillitis with painful adenopathy and systemic "
    "symptoms is the oropharyngeal form. Diagnosis is by serology and culture, and streptomycin is "
    "the treatment named for it."],
   ["Trimethoprim-sulfamethoxazole",
    "That is the treatment for brucellosis, along with tetracycline. Brucellosis is acquired from "
    "unpasteurised milk and produces total-body lymphadenopathy rather than the tonsillitis with "
    "regional nodes described here."],
   ["Azithromycin",
    "Azithromycin is used for cat scratch disease caused by Bartonella henselae, which follows cat "
    "contact and gives preauricular and submandibular nodes. The exposure and node distribution do "
    "not match."],
   ["Sulfonamides or pyrimethamine",
    "Those treat toxoplasmosis, acquired from undercooked meat or cat faeces. Toxoplasmosis gives "
    "fever, malaise, sore throat and myalgias rather than the specific tonsillitis and painful "
    "adenopathy of tularemia."]],
  "treatment", D, 33),

Q("Actinomycosis", IO,
  "A 51-year-old man has a painless, fluctuant swelling in the submandibular region that has been "
  "slowly enlarging. Biopsy shows filamentous organisms.",
  [["Penicillin",
    "Correct. Actinomycosis presents as a painless fluctuant mass in the submandibular or upper "
    "digastric region, and the combination of painlessness with fluctuance is what distinguishes it "
    "from an ordinary pyogenic abscess, which would be exquisitely tender. Diagnosis is clinical and "
    "by biopsy, and penicillin is the treatment."],
   ["Surgical excision alone",
    "Excision without prolonged antimicrobial therapy leaves organisms in the surrounding tissue "
    "planes, because actinomycosis spreads without respecting anatomical boundaries. Antibiotics are "
    "the mainstay rather than an adjunct."],
   ["Antituberculous therapy",
    "Tuberculous adenitis produces diffuse bilateral lymphadenopathy in adults and is diagnosed by "
    "acid-fast stain and culture. The filamentous organisms described are not mycobacteria."],
   ["Amphotericin B",
    "Amphotericin treats invasive fungal infection in immunocompromised patients, where Candida, "
    "Histoplasma or Aspergillus are the organisms. Actinomyces is a bacterium despite its "
    "filamentous appearance."]],
  "treatment", D, 34),

Q("Follicular thyroid carcinoma", IO,
  "A 55-year-old woman with a thyroid carcinoma is found to have a solitary lesion in the femur.",
  [["Follicular carcinoma, which spreads haematogenously to bone and lung",
    "Correct. Follicular carcinoma is distinguished from papillary by its route of spread: it "
    "disseminates through the bloodstream to bone and lungs, whereas papillary tends to involve "
    "local cervical lymph nodes. A distant bony metastasis therefore points to the follicular type, "
    "and the Hurthle cell variant is more aggressive still."],
   ["Papillary carcinoma",
    "Papillary carcinoma is the commonest type with the best prognosis, and its characteristic "
    "spread is to local lymph nodes rather than to distant bone. A femoral deposit would be atypical "
    "for it."],
   ["Anaplastic carcinoma",
    "Anaplastic carcinoma spreads aggressively but presents as a rapidly enlarging hard neck mass in "
    "an elderly patient with death in 6 to 36 months, not as a solitary bone lesion in a woman of "
    "55."],
   ["Medullary carcinoma",
    "Medullary carcinoma is the most likely of the four to metastasise and can go undiagnosed until "
    "a metastasis is found, so it deserves consideration, but it arises from calcitonin-producing C "
    "cells and carries the familial syndrome association that would usually be evident."]],
  "diagnosis", D, 42),

Q("Neck anatomy", IO,
  "A trauma patient has a penetrating wound in the supraclavicular triangle. The surgeon is "
  "particularly concerned about one structure lying deep to its contents.",
  [["The cupola of the pleural cavity",
    "Correct. The supraclavicular triangle lies above the middle of the clavicle and contains the "
    "terminal subclavian artery and the roots, trunks and divisions of the brachial plexus, but the "
    "structure lying DEEP to all of them is the dome of the pleura. A wound there can therefore "
    "produce a pneumothorax as well as vascular and neurological injury."],
   ["The thoracic duct on the right side",
    "The thoracic duct empties at the junction of the LEFT internal jugular and subclavian veins; "
    "the right side of the neck is drained by the right lymphatic duct. The side is wrong, and "
    "neither lies deep to the supraclavicular contents in the way the pleura does."],
   ["The vagus nerve",
    "The vagus runs within the carotid sheath in the carotid triangle of the anterior group, "
    "alongside the carotid arteries and internal jugular vein. It is not a supraclavicular "
    "structure."],
   ["The spinal accessory nerve",
    "The spinal accessory nerve crosses the muscular floor of the OCCIPITAL triangle to pass deep to "
    "trapezius. That is the other subdivision of the posterior triangle, above the omohyoid rather "
    "than below it."]],
  "finding", D, 5),

Q("HIV-associated adenopathy", IO,
  "A 36-year-old man with newly diagnosed HIV has generalised cervical lymphadenopathy with no "
  "identifiable infectious or neoplastic cause after investigation.",
  [["Persistent generalised lymphadenopathy, treated by treating the HIV",
    "Correct. Persistent generalised lymphadenopathy is defined by the absence of an identifiable "
    "infectious or neoplastic cause, and the neck is its commonest site. It reflects the immune "
    "activation of untreated infection, which is why the treatment is antiretroviral therapy rather "
    "than anything directed at the nodes themselves."],
   ["Idiopathic follicular hyperplasia requiring excision",
    "Follicular hyperplasia is indeed the commonest cause of adenopathy in HIV, but it is a "
    "histological description rather than an indication for surgery, and excising nodes does not "
    "alter the underlying immune activation."],
   ["Kaposi sarcoma",
    "Kaposi sarcoma is one of the conditions that must be excluded before accepting persistent "
    "generalised lymphadenopathy, alongside tuberculosis, Pneumocystis and lymphoma. Investigation "
    "here has already excluded a neoplastic cause."],
   ["Tuberculous adenitis",
    "Mycobacterium tuberculosis is specifically on the list to rule out in an HIV-positive patient "
    "with adenopathy, and here that has been done. Treating empirically for tuberculosis without "
    "evidence would expose him to prolonged toxic therapy."]],
  "diagnosis", D, 32),

Q("Thymic cyst", IO,
  "A 9-year-old has a slow-growing, asymptomatic lower anterior neck mass. Biopsy shows Hassall "
  "corpuscles.",
  [["Thymic cyst",
    "Correct. Hassall corpuscles are concentric epithelial structures found in the thymic medulla, "
    "and their presence is what makes the diagnosis definitively. Imaging narrows the differential "
    "but cannot establish it, which is why the lecture specifies that definitive diagnosis is by "
    "biopsy. Treatment is surgical excision."],
   ["Branchial cleft cyst",
    "A branchial cleft cyst sits laterally at the sternocleidomastoid border and is lined by "
    "squamous or respiratory epithelium. It contains no thymic tissue and therefore no Hassall "
    "corpuscles."],
   ["Thyroglossal duct cyst",
    "A thyroglossal duct cyst is midline and moves with tongue protrusion, and its lining may "
    "contain thyroid tissue, which is why all specimens are examined to exclude thyroid carcinoma. "
    "Thymic tissue is not part of it."],
   ["Dermoid cyst",
    "A dermoid contains entrapped epithelial elements including skin appendages, which is a "
    "different histological picture. It is midline and submental rather than in the lower anterior "
    "neck."]],
  "diagnosis", D, 29),

Q("Neck mass in a child versus an adult", IO,
  "A clinician is taught that age changes the prior probability when assessing a neck mass.",
  [["Under 40 most masses are inflammatory, with Hodgkin lymphoma as the exception",
    "Correct. The lecture states that most neck masses in patients under 40 are inflammatory in "
    "nature, and names Hodgkin lymphoma as the specific exception to that rule. Above 40 the "
    "probability shifts toward malignancy, which is why age over 40 appears on the red-flag list "
    "alongside size, duration, firmness and tobacco use."],
   ["Under 40 most masses are malignant",
    "This inverts the rule. Treating every young patient's neck lump as presumptively malignant "
    "would generate a great deal of unnecessary investigation for what is usually reactive "
    "adenopathy after an upper respiratory infection."],
   ["Age is not a useful discriminator in neck masses",
    "Age is one of the strongest discriminators available and appears explicitly on the malignancy "
    "red-flag list. Discarding it removes one of the few pieces of information available before any "
    "test is ordered."],
   ["Above 40 most masses are congenital",
    "Congenital masses declare themselves in childhood or early adulthood, typically when they "
    "become infected. A first presentation above 40 makes a congenital origin less likely, not "
    "more."]],
  "mechanism", D, 13),
]
