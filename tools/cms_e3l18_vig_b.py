# -*- coding: utf-8 -*-
"""Lecture 18 vignette pool B -- Neoplasms and Neck Masses."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Neck masses and neoplasms: the triangles and lymph nodes of the neck; and the etiologies, "
      "epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic "
      "testing, management, referrals, patient education, and prognosis")
C = lambda n: "CMS I Neoplasms and Neck Masses, Slide %d" % n

QUESTIONS = [

Q("Vascular neck mass", IO,
  "A 45-year-old woman has a neck mass that pulses under the fingers and has an audible bruit on "
  "auscultation.",
  [["Computed tomography angiography, and do not biopsy it blindly",
    "Correct. Pulsatility or a bruit means vascular, which puts paraganglioma at the head of the "
    "list. Angiography defines the blood supply and the relationship to the carotid, and it must "
    "come before any needle, because puncturing a highly vascular tumour risks significant "
    "haemorrhage."],
   ["Immediate fine needle aspiration",
    "Aspiration is the standard of care for most neck masses, which is exactly why this trap works. "
    "It is the one thing not to do first into a pulsatile lesion."],
   ["A trial of antibiotics",
    "There are no infective features, and no antibiotic influences a vascular tumour. This would "
    "waste weeks."],
   ["Reassurance, as pulsation indicates a benign lesion",
    "Paragangliomas are usually benign, so the reassurance is half right, but their position and "
    "vascularity still make them a surgical problem needing definition."]], C(13)),

Q("Lymphoma", IO,
  "A 35-year-old man has a neck mass that has grown quickly over three weeks. He has no fever or "
  "sore throat, but reports drenching night sweats and weight loss.",
  [["Lymphoma",
    "Correct. Rapid growth is usually infectious when other infective symptoms accompany it, and "
    "lymphoma when they do not. Here the tempo comes with constitutional B symptoms instead, and "
    "lymphoma is also the named exception to the rule that masses under 40 are inflammatory."],
   ["Reactive viral lymphadenopathy",
    "Reactive nodes follow an upper respiratory infection, regress within one to two weeks, and are "
    "not accompanied by night sweats and weight loss."],
   ["An infected branchial cleft cyst",
    "An infected congenital cyst is tender and erythematous with systemic features of infection, at "
    "a site the patient often recalls having had a lump before."],
   ["Lipoma",
    "Lipomas are soft, mobile and grow imperceptibly over years, producing no systemic symptoms. "
    "Three weeks of rapid growth is out of character."]], C(13)),

Q("Metastatic neck disease", IO,
  "A 64-year-old smoker has a firm cervical node. Aspiration shows squamous cell carcinoma, but no "
  "primary is obvious on first inspection.",
  [["Examine every mucosal surface of the head and neck",
    "Correct. Squamous carcinoma is the commonest metastatic lesion to the neck and comes from the "
    "skin or upper aerodigestive tract. A systematic office examination of all mucosal surfaces, the "
    "thyroid, the salivary glands and the skin usually finds the primary, and the primary determines "
    "both the surgery and the radiotherapy field."],
   ["Proceed directly to neck dissection",
    "Operating without the primary means the field cannot be planned and the source goes untreated, "
    "so the disease recurs."],
   ["Repeat the aspiration",
    "Cytology has already given a clear answer. The outstanding question is where the tumour came "
    "from, which repeating the same test cannot address."],
   ["Empirical radiotherapy to the neck",
    "Irradiating without knowing the primary leaves an untreated tumour and commits the patient to a "
    "field that may be wrong."]], C(39)),

Q("Plunging ranula", IO,
  "A 26-year-old woman has a slow-growing painless submental swelling. Imaging shows it arising "
  "from the sublingual gland and extending through mylohyoid into the neck.",
  [["Excision of the sublingual gland",
    "Correct. A ranula is a mucous retention cyst from the sublingual gland, called plunging when it "
    "herniates through mylohyoid. Removing the cyst alone leaves the gland producing the mucus, so "
    "it simply refills; excising the source gland is what prevents recurrence."],
   ["Marsupialisation of the cyst",
    "Marsupialisation opens the cyst to drain into the mouth and is sometimes used for a simple oral "
    "ranula, but recurrence is high and it does not address the part that has already passed through "
    "the muscle."],
   ["Aspiration of the contents",
    "Aspiration removes the mucus but leaves the secreting gland and the cavity, so the swelling "
    "returns within days to weeks. It is diagnostic at best."],
   ["Excision of the submandibular gland",
    "The submandibular gland is the wrong gland entirely. A ranula is sublingual in origin, so "
    "removing the submandibular one causes morbidity without touching the source."]], C(25)),

Q("Laryngocele", IO,
  "A 49-year-old trumpet player has hoarseness, cough and a foreign body sensation in the throat. "
  "Laryngoscopy shows a smooth dilation at the level of the false cord.",
  [["Laryngocele",
    "Correct. A laryngocele is dilation or herniation of the laryngeal saccule, and sustained raised "
    "intraluminal pressure from wind instrument playing is the classic association. The smooth "
    "dilation at the false cord is the characteristic finding, and computed tomography confirms it "
    "and defines the extent."],
   ["Vocal cord polyp",
    "A polyp is a discrete pedunculated mass on the vibrating margin of the TRUE cord, from vocal "
    "abuse and smoking, rather than a smooth swelling at the false cord."],
   ["Vocal cord papillomatosis",
    "Papillomatosis produces multiple friable warty growths from human papillomavirus subtypes 6 and "
    "11. Its appearance is irregular and exophytic rather than a smooth dilation."],
   ["Laryngeal carcinoma",
    "A malignancy would appear irregular, ulcerated or exophytic, usually on the true cord, in a "
    "patient with a smoking history and progressive symptoms."]], C(24)),

Q("Dermoid cyst", IO,
  "A 13-year-old has a midline submental mass that is non-tender and mobile. It does not move when "
  "he protrudes his tongue.",
  [["Dermoid cyst",
    "Correct. Both dermoid and thyroglossal duct cysts are midline, which is why they are the pair "
    "that must be distinguished. The discriminator is the hyoid attachment: a thyroglossal duct cyst "
    "rises with tongue protrusion, while a dermoid, from epithelium entrapped during embryogenesis, "
    "has no such connection and stays still."],
   ["Thyroglossal duct cyst",
    "This is the commonest congenital midline mass and the right first thought, but the absence of "
    "movement on tongue protrusion specifically excludes it, because that movement is "
    "pathognomonic."],
   ["Branchial cleft cyst",
    "Branchial cleft cysts are lateral, at the anterior border of the sternocleidomastoid. A midline "
    "submental position is wrong for them."],
   ["Submental lymph node",
    "A submental node would usually be one of several, relate to an oral or facial infection, and be "
    "tender if inflamed. A solitary painless mobile midline mass behaves differently."]], C(29)),

Q("Thymic cyst", IO,
  "An 11-year-old has a slow-growing asymptomatic lower anterior neck mass. Biopsy shows Hassall "
  "corpuscles.",
  [["Thymic cyst",
    "Correct. Hassall corpuscles are concentric epithelial structures of the thymic medulla, so "
    "their presence identifies the tissue definitively. Imaging narrows the differential but cannot "
    "establish it, which is why biopsy is specified, and treatment is surgical excision."],
   ["Branchial cleft cyst",
    "A branchial cleft cyst is lateral at the sternocleidomastoid border and is lined by squamous or "
    "respiratory epithelium, containing no thymic tissue."],
   ["Thyroglossal duct cyst",
    "A thyroglossal duct cyst is midline, moves with tongue protrusion, and may contain thyroid "
    "tissue, which is why every specimen is checked for thyroid carcinoma."],
   ["Dermoid cyst",
    "A dermoid contains entrapped epithelial elements including skin appendages, a different "
    "histological picture, and sits midline and submental."]], C(29)),

Q("HIV adenopathy", IO,
  "A 34-year-old man with untreated HIV has generalised cervical lymphadenopathy. Investigation "
  "finds no infectious or neoplastic cause.",
  [["Persistent generalised lymphadenopathy, treated by treating the HIV",
    "Correct. Persistent generalised lymphadenopathy is defined by the absence of an identifiable "
    "infectious or neoplastic cause, and the neck is its commonest site. It reflects the immune "
    "activation of untreated infection, so the treatment is antiretroviral therapy rather than "
    "anything aimed at the nodes."],
   ["Idiopathic follicular hyperplasia requiring excision",
    "Follicular hyperplasia is the commonest cause of adenopathy in HIV, but it is a histological "
    "description rather than an indication for surgery, and excising nodes changes nothing."],
   ["Kaposi sarcoma",
    "Kaposi sarcoma is one of the conditions that must be excluded, alongside tuberculosis, "
    "Pneumocystis and lymphoma. Investigation here has already excluded a neoplastic cause."],
   ["Tuberculous adenitis",
    "Tuberculosis is specifically on the list to rule out in an HIV-positive patient, and here that "
    "has been done. Empirical treatment would mean months of toxic therapy without evidence."]],
  C(32)),

Q("Tularemia", IO,
  "A 41-year-old man who hunts rabbits has fever, chills, headache and fatigue with tonsillitis and "
  "painful cervical adenopathy.",
  [["Streptomycin",
    "Correct. Rabbits, ticks or contaminated water point to Francisella tularensis, and tonsillitis "
    "with painful adenopathy and systemic symptoms is the oropharyngeal form. Diagnosis is by "
    "serology and culture, and streptomycin is the named treatment."],
   ["Trimethoprim-sulfamethoxazole",
    "That treats brucellosis, acquired from unpasteurised milk, which produces total-body "
    "lymphadenopathy rather than tonsillitis with regional nodes."],
   ["Azithromycin",
    "Azithromycin is used for cat scratch disease from Bartonella henselae, following cat contact "
    "with preauricular and submandibular nodes."],
   ["Sulfonamides or pyrimethamine",
    "Those treat toxoplasmosis from undercooked meat or cat faeces, which gives fever, malaise, sore "
    "throat and myalgias rather than the specific tonsillitis of tularemia."]], C(33)),

Q("Brucellosis", IO,
  "A 39-year-old dairy worker who drinks unpasteurised milk has fever, fatigue, malaise and "
  "lymphadenopathy involving the neck, axillae and groins.",
  [["Trimethoprim-sulfamethoxazole or tetracycline",
    "Correct. Unpasteurised milk points to Brucella, and the distinguishing clinical feature is that "
    "the lymphadenopathy is total-body rather than confined to one region, which separates it from "
    "the regional adenopathies. Diagnosis is by serology and culture."],
   ["Streptomycin",
    "Streptomycin treats tularemia, acquired from rabbits, ticks or contaminated water, which "
    "presents with tonsillitis and painful regional adenopathy."],
   ["Penicillin",
    "Penicillin treats actinomycosis, which presents as a painless fluctuant submandibular mass with "
    "filamentous organisms on biopsy."],
   ["Amphotericin B",
    "Amphotericin treats invasive fungal infection in immunocompromised patients, where Candida, "
    "Histoplasma or Aspergillus are the organisms."]], C(33)),

Q("Actinomycosis", IO,
  "A 53-year-old man has a painless, fluctuant swelling in the submandibular region that has slowly "
  "enlarged. Biopsy shows filamentous organisms.",
  [["Penicillin",
    "Correct. Actinomycosis presents as a painless fluctuant mass in the submandibular or upper "
    "digastric region, and the combination of painlessness with fluctuance is what separates it from "
    "an ordinary pyogenic abscess, which would be exquisitely tender. Diagnosis is clinical and by "
    "biopsy."],
   ["Surgical excision alone",
    "Excision without prolonged antimicrobial therapy leaves organisms in the surrounding planes, "
    "because the infection spreads without respecting anatomical boundaries."],
   ["Antituberculous therapy",
    "Tuberculous adenitis produces diffuse bilateral lymphadenopathy in adults and is diagnosed by "
    "acid-fast staining. The filamentous organisms described are not mycobacteria."],
   ["Amphotericin B",
    "Amphotericin is for invasive fungal disease. Actinomyces is a bacterium despite its filamentous "
    "appearance, which is the trap in this question."]], C(34)),

Q("Fungal neck infection", IO,
  "A 57-year-old woman on immunosuppression after a transplant has persistent cervical "
  "lymphadenopathy. Bacterial cultures are negative and antibiotics have failed.",
  [["Send fungal cultures and serology",
    "Correct. Immunocompromised patients are particularly susceptible to Candida, Histoplasma and "
    "Aspergillus, and both fungal cultures AND serology are required, because they are not found "
    "unless specifically sought. Negative bacterial cultures with antibiotic failure in this host is "
    "exactly the setting to look."],
   ["Broaden the antibiotic spectrum",
    "Broadening antibacterial cover repeats a failed strategy and further suppresses the flora, "
    "which favours the fungal overgrowth that is the likelier problem."],
   ["Reduce the immunosuppression and observe",
    "Reducing immunosuppression may form part of management but risks graft rejection and does not "
    "identify the organism."],
   ["Start empirical antituberculous therapy",
    "Tuberculosis is worth excluding, but committing to months of hepatotoxic therapy without "
    "acid-fast evidence, when fungal disease is at least as likely, inverts the order."]], C(35)),

Q("Kawasaki disease", IO,
  "A 3-year-old has five days of high fever, red eyes without discharge, a strawberry tongue, "
  "cracked lips, a rash and one large cervical node.",
  [["Kawasaki disease",
    "Correct. Kawasaki sits among the non-infectious inflammatory causes of neck masses alongside "
    "Sjogren syndrome, sarcoidosis and IgG4-related disease. The cervical node is one criterion "
    "among several, and recognising the constellation matters because untreated Kawasaki causes "
    "coronary artery aneurysms."],
   ["Suppurative bacterial lymphadenitis",
    "Bacterial adenitis gives a hot tender node with fever but not conjunctival injection, a "
    "strawberry tongue, cracked lips and a rash. Those mucocutaneous features indicate a systemic "
    "process."],
   ["Infectious mononucleosis",
    "Mononucleosis gives fever with tonsillar pharyngitis and bilateral cervical adenopathy, and can "
    "produce a rash after penicillin, but not the ocular and oral changes described."],
   ["Reactive viral lymphadenopathy",
    "Reactive nodes accompany a mild upper respiratory illness and regress within a couple of weeks, "
    "without five days of high fever and mucocutaneous change."]], C(35)),

Q("Follicular carcinoma", IO,
  "A 57-year-old woman with a thyroid carcinoma is found to have a solitary lesion in the femur.",
  [["Follicular carcinoma",
    "Correct. Route of spread is what separates follicular from papillary disease. Follicular "
    "carcinoma disseminates haematogenously to bone and lung, whereas papillary tends to involve "
    "local cervical nodes. A distant bony metastasis therefore points to the follicular type, and "
    "the Hurthle cell variant is more aggressive still."],
   ["Papillary carcinoma",
    "Papillary carcinoma is commonest with the best prognosis and spreads to local lymph nodes. A "
    "femoral deposit would be atypical for it."],
   ["Anaplastic carcinoma",
    "Anaplastic carcinoma presents as a rapidly enlarging hard neck mass in an elderly patient with "
    "death in 6 to 36 months, not as a solitary bone lesion in a woman of 57."],
   ["Medullary carcinoma",
    "Medullary carcinoma is the most likely of the four to metastasise and can be found that way, so "
    "it deserves consideration, but it arises from C cells and usually carries an evident familial "
    "association."]], C(42)),

Q("Neck mass in the immunocompromised", IO,
  "A 40-year-old man with untreated HIV has a rapidly enlarging cervical mass with purple "
  "discolouration of the overlying skin.",
  [["Kaposi sarcoma",
    "Correct. Kaposi sarcoma is one of the conditions that must be excluded in an HIV-positive "
    "patient with lymphadenopathy, alongside tuberculosis, Pneumocystis and lymphoma. Its vascular "
    "nature produces the purple appearance, distinguishing it from the follicular hyperplasia that "
    "accounts for most adenopathy in this group."],
   ["Idiopathic follicular hyperplasia",
    "Hyperplasia is the commonest cause of adenopathy in HIV and the right base rate, but it "
    "produces ordinary-looking nodes without skin change and is a diagnosis of exclusion."],
   ["Persistent generalised lymphadenopathy",
    "That diagnosis requires no identifiable infectious or neoplastic cause and is generalised, not "
    "a single rapidly enlarging mass with skin discolouration."],
   ["Reactive viral lymphadenopathy",
    "Reactive nodes follow an upper respiratory infection and regress in one to two weeks without "
    "changing the overlying skin."]], C(32)),
]
