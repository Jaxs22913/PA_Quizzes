# -*- coding: utf-8 -*-
"""Lecture 18 objective-style pool B -- Neoplasms and Neck Masses."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Neck masses and neoplasms: the triangles and lymph nodes of the neck; and the etiologies, "
      "epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, and prognosis")
C = lambda n: "CMS I Neoplasms and Neck Masses, Slide %d" % n

QUESTIONS = [

Q("Thyroglossal duct cyst", IO, "What is the standard operation for a thyroglossal duct cyst?",
  [["The Sistrunk operation",
    "Correct. The cyst is excised along with a cuff of tissue INCLUDING the centre of the hyoid "
    "bone, because the tract runs through the hyoid on its way to the tongue base. Leaving the "
    "central hyoid behind leaves tract with it, which is why simple cyst excision recurs. Care is "
    "taken not to injure the hypoglossal nerves."],
   ["Simple excision of the cyst alone",
    "Removing the cyst without the hyoid segment leaves the tract, and the tract is what regenerates "
    "the cyst. That is the specific failure the Sistrunk operation was designed to prevent."],
   ["Marsupialisation",
    "Marsupialisation opens a cavity to drain and is used for some mucous cysts. It leaves the "
    "epithelial tract entirely intact here, so recurrence is certain."],
   ["Sclerotherapy",
    "Sclerotherapy is an option for lymphangiomas, where the target is a network of lymphatic "
    "channels. It does not address an epithelial tract tethered to the hyoid."]], C(23)),

Q("Thyroglossal duct cyst", IO,
  "Why does every excised thyroglossal duct cyst go for histopathology?",
  [["To rule out thyroid carcinoma",
    "Correct. The tract follows the thyroid's embryological descent, so it can contain ectopic "
    "thyroid tissue, and that tissue can harbour carcinoma. Because the cyst is otherwise a benign "
    "congenital lesion, the malignancy would go undetected unless every specimen is examined."],
   ["To confirm the diagnosis, which is otherwise impossible",
    "The diagnosis is usually clear clinically from the midline position and movement with tongue "
    "protrusion. Histology is sent for a different reason than establishing what the lesion is."],
   ["To identify the infecting organism",
    "Organisms are identified by culture rather than histology, and the specimen is usually removed "
    "once infection has settled rather than during it."],
   ["To determine whether the hyoid was completely removed",
    "Completeness of the hyoid resection is a surgical judgement made in theatre. Histology of the "
    "cyst does not report on the bone margin."]], C(23)),

Q("Laryngocele", IO, "What is a laryngocele?",
  [["An abnormal dilation or herniation of the laryngeal saccule",
    "Correct. The saccule is a small outpouching of the laryngeal ventricle, and sustained raised "
    "intraluminal pressure can dilate or herniate it. Symptoms are cough, hoarseness, dyspnoea, "
    "dysphagia or a foreign body sensation, and secondary infection of one is called a "
    "laryngopyocele."],
   ["A keratin-filled sac behind the tympanic membrane",
    "That describes a cholesteatoma, which sits in the middle ear behind a retracted drum and causes "
    "chronic foul discharge and conductive hearing loss."],
   ["A congenital malformation of lymphatic channels",
    "That is a lymphangioma, which presents as a soft compressible transilluminating neck mass "
    "rather than a laryngeal outpouching."],
   ["A mucous retention cyst of the floor of the mouth",
    "That is a ranula, arising from the sublingual gland, and it is called plunging when it extends "
    "through mylohyoid into the neck."]], C(24)),

Q("Laryngocele", IO, "What does laryngoscopy show in a laryngocele?",
  [["A smooth dilation at the level of the false cord",
    "Correct. The saccule lies between the true and false cords, so its dilation bulges at the false "
    "cord and appears smooth because it is lined by normal mucosa. Computed tomography then confirms "
    "the diagnosis and defines the extent, which determines whether decompression or open excision "
    "is used."],
   ["Multiple friable warty growths on both cords",
    "That is recurrent respiratory papillomatosis, caused by human papillomavirus subtypes 6 and 11. "
    "The appearance is exophytic and irregular rather than a smooth swelling."],
   ["A unilateral pedunculated mass on the vibrating margin",
    "That describes a vocal cord polyp, which sits on the true cord at the point of maximal "
    "vibration and is associated with vocal abuse and smoking."],
   ["Bilateral symmetric whitish nodules at the anterior third",
    "Those are vocal cord nodules from vocal abuse, sitting at the junction of the anterior third "
    "and posterior two thirds of the true cords."]], C(24)),

Q("Plunging ranula", IO, "From which gland does a ranula arise?",
  [["The sublingual gland",
    "Correct. A ranula is a mucocele or retention cyst arising from the sublingual gland in the "
    "floor of the mouth. It is called plunging when it extends through the mylohyoid muscle into the "
    "neck, and treatment is excision of the sublingual gland itself, because removing only the cyst "
    "leaves the source."],
   ["The submandibular gland",
    "The submandibular gland lies beneath the floor of the mouth and drains through Wharton duct. It "
    "is the gland most affected by stones rather than the source of a ranula."],
   ["The parotid gland",
    "The parotid sits on the side of the face and drains through Stensen duct opposite the upper "
    "second molar. It is the commonest site of salivary neoplasm and of suppurative sialadenitis."],
   ["A minor salivary gland of the palate",
    "Minor glands are scattered through the buccal, labial and palatal mucosa and give rise to "
    "small mucoceles, but the specific floor-of-mouth lesion that plunges is sublingual in origin."]],
  C(25)),

Q("Lymphangioma", IO, "Which physical finding characterises a lymphangioma?",
  [["Positive transillumination",
    "Correct. A lymphangioma is a congenital malformation in which lymph spaces fail to connect to "
    "the rest of the lymphatic system, so it fills with clear lymph. Clear fluid transmits light, "
    "which is why the mass transilluminates, and it also explains the soft, doughy, compressible "
    "texture."],
   ["Pulsatility with an audible bruit",
    "Pulsatility indicates a vascular lesion with arterial flow, most often a paraganglioma. A "
    "lymphangioma has no arterial supply of its own to transmit a pulse."],
   ["Vertical movement with tongue protrusion",
    "That is pathognomonic for a thyroglossal duct cyst, whose tract tethers it to the hyoid bone. "
    "A lymphangioma has no such attachment."],
   ["Enlargement on crying or straining",
    "Enlargement with raised venous pressure is a haemangioma feature, reflecting engorgement of "
    "blood-filled channels rather than lymph-filled ones."]], C(26)),

Q("Haemangioma", IO, "What is the natural history of a head and neck haemangioma?",
  [["Rapid growth in the first year, then involution from 18 to 24 months",
    "Correct. Haemangiomas appear in the first few months of life, grow rapidly through the first "
    "year, and then begin to involute at 18 to 24 months. About 90 per cent resolve without therapy, "
    "which is why observation is the default and why parents need the growth-then-shrink curve "
    "explained in advance."],
   ["Steady growth throughout childhood with no involution",
    "Continuous growth would make early intervention necessary in every case. The characteristic "
    "feature of these lesions is precisely that they regress."],
   ["Present at birth at full size, then static",
    "A mass at full size from birth that does not change is more characteristic of a teratoma or a "
    "lymphangioma. Haemangiomas typically appear after birth and then proliferate."],
   ["Spontaneous resolution within the first month",
    "Resolution takes years rather than weeks, and the proliferative phase comes first. Expecting "
    "clearance in a month would lead to premature alarm when it enlarges instead."]], C(27)),

Q("Haemangioma", IO, "What is first-line drug treatment when a haemangioma requires intervention?",
  [["Propranolol",
    "Correct. Intervention is reserved for airway compromise, skin ulceration, dysphagia, "
    "thrombocytopenia or cardiac failure, since most lesions resolve untreated. When treatment is "
    "needed, propranolol is first line for those without a contraindication, with systemic "
    "corticosteroids, interferon alpha or laser excision as second line."],
   ["Systemic corticosteroids",
    "Steroids are second line, used when propranolol is contraindicated or ineffective. Their "
    "systemic effects in an infant make them a poorer first choice."],
   ["Sclerotherapy",
    "Sclerotherapy is used for lymphangiomas, where the target is a network of lymphatic spaces. It "
    "is not the first approach to a proliferating haemangioma."],
   ["Surgical excision",
    "Surgery is reserved for complications or for residual deformity after involution has finished. "
    "Operating during the proliferative phase on a highly vascular lesion is difficult and usually "
    "unnecessary."]], C(27)),

Q("Teratoma", IO, "What imaging feature suggests a teratoma?",
  [["Calcifications",
    "Correct. Teratomas originate from pluripotent cells and therefore contain a mixture of tissue "
    "types, including elements that calcify. Computed tomography and magnetic resonance imaging show "
    "those calcifications, and they help distinguish a firm neonatal neck mass from the soft "
    "lymphangioma or the vascular haemangioma."],
   ["Transillumination on ultrasound",
    "Transillumination is a bedside finding with a light source, not an imaging feature, and it "
    "belongs to lymphangioma rather than teratoma."],
   ["A rim-enhancing hypodense collection",
    "That describes an abscess, characteristically the retropharyngeal one on lateral neck computed "
    "tomography. It indicates pus rather than mixed solid tissue."],
   ["Absence of any soft tissue component",
    "A teratoma is a solid mass with varied tissue, so it has a substantial soft tissue component. "
    "Its distinguishing feature is the calcification WITHIN that tissue."]], C(28)),

Q("Sternocleidomastoid tumour of infancy", IO,
  "What is the natural history of a sternocleidomastoid tumour of infancy?",
  [["Enlarges for 2 to 3 months, then regresses over 4 to 8",
    "Correct. The mass grows for a couple of months and then shrinks over the following four to "
    "eight, with about 80 per cent resolving spontaneously. Physical therapy is given during that "
    "time to prevent a fixed restrictive torticollis, and surgery is reserved for the minority that "
    "persist."],
   ["Grows continuously and always requires excision",
    "Continuous growth requiring surgery in every case would make the condition far more serious "
    "than it is, and would expose most infants to an unnecessary operation."],
   ["Resolves within two weeks without intervention",
    "Two weeks is the timescale of reactive lymphadenopathy. This lesion runs over many months, "
    "which is why anticipatory guidance matters."],
   ["Transforms into a rhabdomyosarcoma if untreated",
    "There is no malignant transformation. Rhabdomyosarcoma is a separate primary malignancy that "
    "appears on the list of malignant neck tumours."]], C(29)),

Q("Inflammatory neck masses", IO,
  "What is the commonest cause of cervical lymphadenopathy in children?",
  [["Reactive viral lymphadenopathy",
    "Correct. Reactive nodes accompany an upper respiratory infection, with adenovirus, rhinovirus "
    "and enterovirus the usual pathogens, and they regress within one to two weeks. Management is "
    "observation, with investigation reserved for nodes over 1 centimetre that persist beyond four "
    "to six weeks or continue to enlarge."],
   ["Tuberculous adenitis",
    "Cervical tuberculosis, or scrofula, affects adults more than children and produces diffuse "
    "bilateral lymphadenopathy. It is uncommon as a first explanation in a well child."],
   ["Cat scratch disease",
    "Bartonella adenitis is genuinely common under 20, but it requires cat contact and produces "
    "preauricular and submandibular nodes with fever and malaise, so it is a specific rather than a "
    "default diagnosis."],
   ["Lymphoma",
    "Lymphoma is the named exception to the rule that masses under 40 are inflammatory, which makes "
    "it important, but it is far less frequent than reactive adenopathy."]], C(31)),

Q("Inflammatory neck masses", IO,
  "A cervical node in a child warrants investigation if it persists beyond what interval?",
  [["Four to six weeks",
    "Correct. Reactive nodes regress in one to two weeks, so persistence well beyond that is what "
    "changes the picture. The threshold is four to six weeks, or any node that continues to enlarge, "
    "and biopsy then looks for fungal, granulomatous or neoplastic processes."],
   ["One week",
    "A week is within the normal course of a reactive node, so investigating at that point would "
    "generate a large number of unnecessary referrals and biopsies."],
   ["Six months",
    "Six months would delay a lymphoma diagnosis substantially in a child. The interval is chosen to "
    "allow reactive nodes to resolve without letting anything sinister run unchecked."],
   ["Three days",
    "Three days is barely into the illness that caused the node. Nodes are expected to be present "
    "and even to enlarge over the first week."]], C(31)),

Q("Inflammatory neck masses", IO,
  "What is the commonest cause of cervical adenopathy in patients with HIV?",
  [["Idiopathic follicular hyperplasia",
    "Correct. Cervical adenopathy is present in 12 to 45 per cent of patients with HIV, and "
    "follicular hyperplasia accounts for most of it. It is a diagnosis of exclusion, though: "
    "tuberculosis, Pneumocystis, lymphoma and Kaposi sarcoma all have to be ruled out first, and "
    "treatment is treating the HIV."],
   ["Kaposi sarcoma",
    "Kaposi sarcoma is one of the conditions to exclude and produces vascular purple lesions. It is "
    "an important diagnosis but not the commonest cause of adenopathy in this group."],
   ["Mycobacterium tuberculosis",
    "Tuberculosis must be excluded and is more common in HIV than in the general population, but "
    "hyperplasia is still the leading explanation once the dangerous causes are ruled out."],
   ["Lymphoma",
    "Lymphoma risk is raised in HIV and it belongs on the exclusion list, but it accounts for a "
    "minority of the adenopathy seen."]], C(32)),

Q("Bacterial lymphadenopathy", IO,
  "Which organisms most commonly cause suppurative cervical lymphadenopathy?",
  [["Staphylococcus aureus and group A beta-haemolytic Streptococcus",
    "Correct. These two account for most suppurative adenitis, producing masses in the submandibular "
    "or jugulodigastric regions with sore throat, skin lesions and upper respiratory symptoms. "
    "Treatment is empirical cover against anaerobes and gram-positive organisms, with aspiration or "
    "drainage if antibiotics fail."],
   ["Bartonella henselae and Toxoplasma gondii",
    "Those are the granulomatous and parasitic causes, requiring cat contact and undercooked meat or "
    "cat faeces respectively. They cause a more indolent adenopathy than a suppurative one."],
   ["Francisella tularensis and Brucella",
    "Tularemia and brucellosis are the exposure-driven infections from rabbits and ticks, and from "
    "unpasteurised milk. Both are uncommon and neither is a routine suppurative organism."],
   ["Candida and Aspergillus",
    "Those are fungal pathogens affecting immunocompromised patients, requiring fungal cultures and "
    "serology and treated with amphotericin B."]], C(33)),

Q("Granulomatous disease", IO,
  "Which infection produces a unilateral neck mass with brawny reddish-brown overlying skin in a "
  "child?",
  [["Atypical mycobacterial infection",
    "Correct. Non-tuberculous mycobacterial adenitis is a paediatric disease presenting as a "
    "unilateral mass in the anterior triangle or parotid region, with characteristically brawny, "
    "reddish-brown skin, induration and pain, in a child who is otherwise well. Diagnosis is by "
    "acid-fast stain, culture and skin testing, and treatment is usually surgical excision."],
   ["Tuberculous adenitis",
    "Cervical tuberculosis affects adults more than children and gives diffuse BILATERAL "
    "lymphadenopathy. Laterality and the skin change are what separate the two mycobacterial "
    "diagnoses."],
   ["Actinomycosis",
    "Actinomycosis presents as a painless, fluctuant submandibular or upper digastric mass with "
    "filamentous organisms on biopsy, treated with penicillin. The skin is not brawny."],
   ["Cat scratch disease",
    "Cat scratch disease affects preauricular and submandibular nodes after cat contact, with fever "
    "and malaise, and is diagnosed serologically. It does not discolour the overlying skin in this "
    "way."]], C(34)),

Q("Granulomatous disease", IO,
  "Which regimen treats tuberculous cervical adenitis?",
  [["RIPE: rifampin, isoniazid, pyrazinamide, ethambutol",
    "Correct. Cervical tuberculosis, called scrofula, is treated with the standard antituberculous "
    "combination. The full list also includes rifabutin and rifapentine, but RIPE is the traditional "
    "four-drug initial regimen, and the diagnosis rests on tuberculin skin testing with acid-fast "
    "stain and culture."],
   ["Streptomycin alone",
    "Streptomycin is the treatment named for tularemia. Single-agent therapy for tuberculosis also "
    "selects for resistance, which is why combination regimens are used."],
   ["Penicillin",
    "Penicillin treats actinomycosis, which presents as a painless fluctuant mass. It has no useful "
    "activity against mycobacteria."],
   ["Amphotericin B",
    "Amphotericin is for invasive fungal infection in the immunocompromised, where Candida, "
    "Histoplasma and Aspergillus are the organisms."]], C(34)),

Q("Neck neoplasm", IO,
  "What is the commonest metastatic lesion to the neck?",
  [["Squamous cell carcinoma",
    "Correct. Malignant neck tumours are usually metastatic squamous cell carcinoma from the skin or "
    "the upper aerodigestive tract, rather than primary neck tumours. That is why finding a "
    "squamous deposit in a node triggers a systematic examination of every mucosal surface, the "
    "thyroid, the salivary glands and the skin."],
   ["Adenocarcinoma",
    "Adenocarcinoma reaching cervical nodes usually indicates a distant primary such as "
    "gastrointestinal or breast, and it is much less common than squamous disease in this region."],
   ["Melanoma",
    "Melanoma does metastasise to cervical nodes and appears on the differential for a metastatic "
    "neck mass, but squamous carcinoma is considerably commoner."],
   ["Lymphoma",
    "Lymphoma is a PRIMARY malignancy of the lymph node rather than a metastasis to it, which is why "
    "it sits on a different branch of the differential."]], C(39)),

Q("Thyroid masses", IO,
  "An immobile midline neck mass that elevates with swallowing most likely arises from what?",
  [["The thyroid",
    "Correct. The thyroid is attached to the larynx and trachea by the pretracheal fascia, so it "
    "rises when the larynx rises during a swallow. That movement identifies the gland as the source "
    "and separates a thyroid mass from a node or a cyst that stays still."],
   ["A lymph node",
    "Lymph nodes are not attached to the laryngeal skeleton, so they do not move with swallowing. "
    "They are also lateral rather than midline."],
   ["A branchial cleft cyst",
    "A branchial cleft cyst is lateral at the sternocleidomastoid border and has no laryngeal "
    "attachment, so it neither sits midline nor rises with a swallow."],
   ["The submandibular gland",
    "The submandibular gland lies beneath the mandible, above and lateral to the thyroid, and does "
    "not move with swallowing."]], C(40)),

Q("Thyroid masses", IO,
  "In a patient with a thyroid nodule and a LOW thyroid-stimulating hormone, what comes before fine "
  "needle aspiration?",
  [["A radionuclide scan with technetium",
    "Correct. A suppressed thyroid-stimulating hormone raises the possibility that the nodule is "
    "producing hormone autonomously. The scan distinguishes a hot, hyperfunctioning nodule, which "
    "carries a low malignant risk and needs no biopsy, from a cold or warm nodule, which does. Doing "
    "it first avoids an unnecessary procedure."],
   ["Contrast computed tomography",
    "Iodine-containing contrast is specifically avoided when thyroid cancer is suspected, because it "
    "compromises later radioiodine treatment. Ultrasound is the imaging of choice for a nodule."],
   ["Immediate thyroidectomy",
    "Surgery before any tissue or functional diagnosis would commit the patient to an operation that "
    "the scan may show is unnecessary, and to lifelong hormone replacement."],
   ["A course of antithyroid medication for six months",
    "Treating the hyperthyroidism addresses the hormonal problem while leaving the structural "
    "question unanswered, and six months is a long time to leave a nodule uncharacterised."]],
  C(41)),
]
