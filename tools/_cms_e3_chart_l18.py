# -*- coding: utf-8 -*-
"""Lecture 18 rows for the ENT comparison chart.

Neoplasms and Neck Masses, Prof. Chand Shah. Same 10-field shape as Lectures
15-17. BUILT FROM THE SLIDES ALONE -- this lecture has no recording in the
inbox, and Jaxon asked for the build to go ahead without it and be revisited
when audio lands. Nothing here depends on emphasis; it is all slide text.

THE DISCRIMINATOR COLUMNS CHANGE MEANING AGAIN. For the ear they were pain and
hearing loss; for the nose, pain and discharge. A neck mass has neither, and the
question that actually sorts the differential is WHERE IT SITS -- midline versus
lateral is the first branch of the deck's own algorithm on slide 17. So the side
line carries location, and the third column carries the finding that names it.

FOUR SLIDES ARE PICTURES OF LISTS and extract as bare titles. Their content is
transcribed into the rows rather than lost, per [[image_only_slides]]:
  slide 17  the NECK MASS algorithm -- congenital lateral/midline vs adult
            inflammatory/neoplastic, with the organisms under each
  slide 20  the adult neck-mass evaluation algorithm
  slide 38  primary neck tumours, malignant against benign, in full
  slide 43  thyroid cancer staging tables

WHAT IS DELIBERATELY LEFT OUT. Slide 48 is the professor's dog and slide 49 is
the exit-ticket QR code. Slides 3-10 are anatomy diagrams -- they belong to the
guide's anatomy section, not to a cell that says "this is what the condition
looks like". The only clinical photograph in the whole deck is the haemangioma
on slide 27.
"""
CONG = "Congenital neck mass"
INFL = "Inflammatory neck mass"
NECK = "Neck neoplasm"
THY = "Thyroid"
D18 = "CMS I Neoplasms and Neck Masses"

ROWS_L18 = [
 ("Branchial cleft cyst", CONG,
  "<b>LATERAL</b> neck &middot; anterior border of the <b>sternocleidomastoid</b> &middot; swells "
  "<b>after an upper respiratory infection</b>",
  "Failure of the pharyngobranchial ducts to obliterate in fetal development. Presents in late "
  "childhood or early adulthood, usually when the cyst becomes infected after an upper respiratory "
  "infection: a <b>tender, inflammatory mass at the anterior border of the sternocleidomastoid</b>, "
  "with overlying erythema and swelling if infected.",
  "Clinical, with imaging to define the tract. <b>Rule out human papillomavirus-associated squamous "
  "cell carcinoma before accepting the diagnosis in an adult</b> &mdash; it can present as a cystic "
  "neck mass.",
  "Control the infection first, then <b>surgical excision of the cyst and its tract</b>. "
  "<b>Avoid incision and drainage</b> unless there is frank abscess &mdash; and even then needle "
  "aspiration is preferred, because I&amp;D makes the definitive excision harder.",
  "Routine",
  "The cyst was always there; the infection is what made it visible. Excision has to take the whole "
  "tract or it recurs.", "22", D18),

 ("Thyroglossal duct cyst", CONG,
  "<b>MIDLINE</b> anterior neck &middot; <b>moves up when the tongue is stuck out</b> or on "
  "swallowing",
  "About <b>one third of all congenital neck masses</b>. A midline anterior neck mass, often "
  "asymptomatic until it becomes infected after an upper respiratory infection. Location varies "
  "&mdash; some sit lateral or as low as the thyroid, and those are hard to tell from a branchial "
  "cleft cyst.",
  "<b>Pathognomonic sign: the mass moves vertically with swallowing or tongue protrusion</b>, which "
  "demonstrates its attachment to the hyoid bone. <b>All cysts go for histopathology to exclude "
  "thyroid carcinoma.</b>",
  "Antibiotics if infected. <b>Sistrunk operation</b> is the standard: the cyst is excised with a "
  "cuff of tissue <b>including the centre of the hyoid bone</b>, taking care not to injure the "
  "hypoglossal nerves.",
  "Routine",
  "Taking the middle of the hyoid out is not overtreatment &mdash; leaving it behind is why these "
  "recur.", "23", D18),

 ("Laryngocele", CONG,
  "<b>Hoarseness with dyspnoea</b> &middot; dilation at the level of the <b>false cord</b>",
  "An abnormal dilation or herniation of the saccule of the larynx. Cough, hoarseness, dyspnoea, "
  "dysphagia or a foreign body sensation, in any combination. <b>Secondary infection of one is "
  "called a laryngopyocele.</b>",
  "<b>Laryngoscopy</b> shows a smooth dilation at the level of the false cord. <b>Computed "
  "tomography confirms it</b> and shows the extent of the lesion.",
  "Symptomatic disease only: laryngoscopic decompression for small lesions; surgical excision by an "
  "external approach for larger ones, taking care not to injure the <b>superior laryngeal "
  "nerve</b>; or laser endoscopy.",
  "Routine", "The airway symptoms are what force the operation, not the size.", "24", D18),

 ("Plunging ranula", CONG,
  "<b>Slow-growing, painless SUBMENTAL mass</b> &middot; arises from the <b>sublingual</b> gland",
  "A mucocele or retention cyst of the floor of the mouth, presenting as a slow-growing, painless "
  "submental mass. It arises from the sublingual gland and is called <b>plunging</b> when it "
  "extends through the mylohyoid muscle into the neck.",
  "Clinical, with imaging to show the extent below mylohyoid.",
  "<b>Excision of the sublingual gland</b> &mdash; the gland is the source, so removing the cyst "
  "alone leaves it to recur.",
  "Routine", "\"Plunging\" is an anatomical statement: it has gone through mylohyoid.", "25", D18),

 ("Lymphangioma (cystic hygroma)", CONG,
  "<b>Soft, doughy, compressible</b> &middot; <b>TRANSILLUMINATES</b>",
  "A congenital malformation of the lymphatic channels, arising because the lymph spaces fail to "
  "connect to the rest of the lymphatic system. The mass is <b>soft, doughy, smooth, non-tender and "
  "compressible</b>, and <b>transilluminates</b>.",
  "Computed tomography and magnetic resonance imaging confirm the extent and define associated "
  "abnormalities such as haemangiomas.",
  "Surgical excision or debulking depending on how far it infiltrates. <b>Sclerotherapy</b> is the "
  "alternative.",
  "Routine",
  "Positive transillumination is the bedside finding that separates it from the solid masses.",
  "26", D18),

 ("Haemangioma", CONG,
  "<b>Red or bluish compressible mass</b> that <b>ENLARGES WITH CRYING</b> or straining &middot; "
  "<b>90% self-resolve</b>",
  "A malformation of vascular tissue. Present in the first few months of life, grows rapidly through "
  "the first year, then <b>begins to involute at 18 to 24 months</b>. A red or bluish soft mass, "
  "compressible, that increases in size with straining or crying, with or without a bruit.",
  "Computed tomography and magnetic resonance imaging.",
  "<b>90% resolve without any therapy</b> &mdash; observation alone. Intervene only for airway "
  "compromise, skin ulceration, dysphagia, thrombocytopenia or cardiac failure. "
  "<b>First line: propranolol.</b> Second line: systemic corticosteroids, interferon alpha, or "
  "surgical laser excision.",
  "Routine",
  "Parents need the growth-then-involution curve explained, or the rapid first year reads as "
  "failure of treatment.", "27", D18),

 ("Teratoma", CONG,
  "<b>Firm</b> neck mass <b>noted at birth</b> or in the first year &middot; <b>calcifications on "
  "imaging</b>",
  "Head and neck teratomas account for <b>3.5% of all teratomas</b>. They originate from pluripotent "
  "cells and present as firm neck masses, most commonly noted at birth or within the first year. A "
  "large one can cause <b>respiratory compromise or dysphagia</b>.",
  "Computed tomography and magnetic resonance imaging &mdash; <b>calcifications</b> are the clue.",
  "Surgical excision.", "Urgent",
  "Size is the whole problem here: it is a benign lesion that can obstruct an airway.", "28", D18),

 ("Dermoid cyst", CONG,
  "<b>MIDLINE</b>, non-tender, mobile &middot; <b>submental</b>",
  "Arises from epithelium entrapped in deeper tissue during embryogenesis, or by traumatic "
  "implantation. Presents as a midline, non-tender, mobile mass in the submental region.",
  "Clinical, with imaging to define the plane.",
  "<b>Surgical excision</b> is the mainstay.", "Routine",
  "One of the midline masses &mdash; thyroglossal duct cyst is the other, and that one moves with "
  "the tongue.", "29", D18),

 ("Thymic cyst", CONG,
  "Slow-growing and asymptomatic &middot; painful only if infected &middot; <b>Hassall "
  "corpuscles</b> on biopsy",
  "Presents as a slow-growing, asymptomatic mass that may become painful if it is infected.",
  "Magnetic resonance imaging and computed tomography help with the differential. <b>Definitive "
  "diagnosis is by biopsy &mdash; the presence of Hassall corpuscles.</b>",
  "Surgical excision.", "Routine",
  "The histology is the diagnosis; imaging only narrows the list.", "29", D18),

 ("Sternocleidomastoid tumour of infancy", CONG,
  "<b>Firm painless mass WITHIN the sternocleidomastoid</b> &middot; related to congenital "
  "<b>torticollis</b>",
  "Related to congenital torticollis. A firm, painless, discrete mass within the sternocleidomastoid "
  "muscle that <b>enlarges for 2 to 3 months and then regresses over 4 to 8 months</b>.",
  "Clinical.",
  "<b>80% resolve spontaneously</b> and need only physical therapy to prevent restrictive "
  "torticollis. Surgical excision is reserved for persistent cases.",
  "Routine",
  "The natural history is the treatment plan: it gets bigger before it gets better.", "29", D18),

 ("Reactive viral lymphadenopathy", INFL,
  "<b>Commonest cause of cervical lymphadenopathy in CHILDREN</b> &middot; with an upper "
  "respiratory infection &middot; <b>regresses in 1&ndash;2 weeks</b>",
  "The commonest cause of cervical lymphadenopathy in children, associated with an underlying upper "
  "respiratory infection. Commonest pathogens are <b>adenovirus, rhinovirus and enterovirus</b>. "
  "Nodes regress in 1 to 2 weeks.",
  "Observation is usually enough. <b>A node larger than 1&nbsp;cm is abnormal</b> and needs "
  "investigation if it persists beyond <b>4 to 6 weeks</b> or enlarges &mdash; biopsy then looks for "
  "fungal, granulomatous or neoplastic causes.",
  "Observation.", "Routine",
  "The two numbers that matter are 1&nbsp;cm and 4 to 6 weeks; past either, it stops being reactive.",
  "31", D18),

 ("HIV-associated cervical adenopathy", INFL,
  "Cervical adenopathy in <b>12&ndash;45%</b> of patients with HIV &middot; the <b>neck is the "
  "commonest site</b>",
  "Cervical adenopathy is present in 12% to 45% of patients with HIV. <b>Idiopathic follicular "
  "hyperplasia is the commonest cause.</b> Persistent generalised lymphadenopathy &mdash; "
  "lymphadenopathy with no identifiable infectious or neoplastic cause &mdash; is also common, and "
  "the neck is its commonest site.",
  "<b>Rule out <i>Mycobacterium tuberculosis</i>, <i>Pneumocystis carinii</i>, lymphoma and Kaposi "
  "sarcoma</b> before settling on hyperplasia.",
  "<b>Treat the HIV.</b>", "Urgent",
  "The adenopathy is a marker of control, not a separate problem to excise.", "32", D18),

 ("Suppurative bacterial lymphadenopathy", INFL,
  "<b>Submandibular or jugulodigastric</b> &middot; with sore throat, skin lesions and upper "
  "respiratory symptoms",
  "Most commonly <b><i>Staphylococcus aureus</i> and group A beta-haemolytic <i>Streptococcus</i></b>. "
  "Masses develop in the submandibular or jugulodigastric regions, with sore throat, skin lesions and "
  "upper respiratory symptoms.",
  "Clinical; culture if aspirated.",
  "<b>Empirical antibiotics against anaerobes and gram-positive organisms.</b> Fine needle aspiration "
  "or incision and drainage if antibiotics fail.",
  "Urgent", "Failure of antibiotics is the trigger to drain, not the starting point.", "33", D18),

 ("Toxoplasmosis", INFL,
  "<b>Undercooked meat or cat faeces</b> &middot; fever, malaise, sore throat, myalgias",
  "<i>Toxoplasma gondii</i>, contracted through poorly cooked meat or ingestion of oocytes in cat "
  "faeces. Fever, malaise, sore throat and myalgias with the adenopathy.",
  "<b>Serologic testing.</b>",
  "<b>Sulfonamides or pyrimethamine.</b>", "Routine",
  "One of four exposure histories on the same slide &mdash; cat faeces here, cat scratch for "
  "<i>Bartonella</i>.", "33", D18),

 ("Tularemia", INFL,
  "<b>Rabbits, ticks, contaminated water</b> &middot; <b>tonsillitis</b> with painful adenopathy",
  "<i>Francisella tularensis</i>, transmitted by rabbits, ticks and contaminated water. Tonsillitis, "
  "painful adenopathy, fever, chills, headache and fatigue.",
  "Serologic testing and cultures.",
  "<b>Streptomycin.</b>", "Urgent",
  "The exposure history is the question: rabbits and ticks.", "33", D18),

 ("Brucellosis", INFL,
  "<b>Unpasteurised milk</b> &middot; <b>total body</b> lymphadenopathy",
  "<i>Brucella</i>, transmitted by ingestion of unpasteurised milk, most commonly in children. "
  "Total body lymphadenopathy with fever, fatigue and malaise.",
  "Serology and cultures.",
  "<b>Trimethoprim-sulfamethoxazole or tetracycline.</b>", "Routine",
  "Generalised rather than regional adenopathy is what sets it apart from the others on this slide.",
  "33", D18),

 ("Cat scratch disease", INFL,
  "<b>Contact with cats</b> &middot; under 20 years &middot; <b>preauricular and submandibular</b> "
  "nodes",
  "<i>Bartonella henselae</i>, with a history of contact with cats. Common under 20 years of age. "
  "Lymphadenopathy &mdash; commonly preauricular and submandibular &mdash; with fever and malaise.",
  "<b>Serologic testing with indirect fluorescent antibodies.</b>",
  "<b>Self-limiting</b>, or azithromycin.", "Routine",
  "Self-limiting is the headline; azithromycin shortens it rather than being required.", "34", D18),

 ("Actinomycosis", INFL,
  "<b>PAINLESS, fluctuant</b> mass &middot; submandibular or upper digastric",
  "Presents as a painless, fluctuant neck mass in the submandibular or upper digastric region.",
  "Clinical and biopsy.",
  "<b>Penicillin.</b>", "Routine",
  "Painless and fluctuant together is the combination that points here.", "34", D18),

 ("Atypical mycobacteria", INFL,
  "<b>Children</b> &middot; <b>UNILATERAL</b> &middot; <b>brawny reddish-brown skin</b> over the "
  "mass",
  "A paediatric infection. A unilateral neck mass in the anterior triangle or the parotid gland, with "
  "<b>brawny (reddish-brown) skin</b>, induration and pain.",
  "Stain or culture for <b>acid-fast bacilli</b>, plus skin testing.",
  "<b>Surgical excision</b>, or incision and drainage with antibiotics.", "Urgent",
  "Unilateral and paediatric here; tuberculous adenitis is more diffuse and bilateral.", "34", D18),

 ("Tuberculous adenitis (scrofula)", INFL,
  "<b>Adults more than children</b> &middot; <b>DIFFUSE and BILATERAL</b>",
  "<i>Mycobacterium tuberculosis</i>. Cervical tuberculosis is called <b>scrofula</b>. Adults are "
  "affected more than children, and the lymphadenopathy is <b>more diffuse and bilateral</b> than in "
  "atypical mycobacterial disease.",
  "Tuberculin skin test, stain and culture for acid-fast bacilli.",
  "Isoniazid, rifampin, rifabutin, rifapentine, pyrazinamide, ethambutol &mdash; traditionally "
  "<b>RIPE: rifampin, isoniazid, pyrazinamide, ethambutol</b>.",
  "Urgent",
  "Bilateral and diffuse versus unilateral and brawny is the whole distinction from atypical "
  "mycobacteria.", "34", D18),

 ("Fungal neck infection", INFL,
  "<b>Immunocompromised</b> &middot; <i>Candida</i>, <i>Histoplasma</i>, <i>Aspergillus</i>",
  "Immunocompromised patients are particularly susceptible. The commonest organisms are "
  "<i>Candida</i>, <i>Histoplasma</i> and <i>Aspergillus</i>.",
  "<b>Fungal cultures and serology are required</b> &mdash; the deck is emphatic about this.",
  "<b>Amphotericin B</b>, treated aggressively.", "Urgent",
  "Non-infectious inflammatory causes sit on the same slide: Sj&ouml;gren syndrome, sarcoidosis, "
  "IgG4-related sialadenitis and Kawasaki disease.", "35", D18),

 ("Neck neoplasm &mdash; general", NECK,
  "<b>Presume any new neck mass is MALIGNANT until proven otherwise</b> &middot; firm, slowly "
  "progressive, asymptomatic",
  "Benign tumours arise from the soft tissue of the neck &mdash; fat, salivary tissue, lymph nodes, "
  "blood vessels, nerves. Malignant ones are usually <b>metastatic squamous cell carcinoma</b> from "
  "skin or the upper aerodigestive tract. Hoarseness, dysphagia and odynophagia are the symptoms; the "
  "lesion itself is asymptomatic, slowly progressive and firm.",
  "Complete head and neck examination, then <b>fine needle aspiration biopsy rather than excisional "
  "biopsy</b> &mdash; excision spills tumour and complicates definitive treatment. Fiberoptic "
  "laryngoscopy for an occult primary; ultrasound, contrast computed tomography, magnetic resonance "
  "imaging, positron emission tomography.",
  "Directed by the primary once it is found. Once the diagnosis is confirmed, <b>all mucosal "
  "surfaces of the head and neck, the thyroid, the salivary glands and the skin are examined</b> "
  "&mdash; the office examination usually finds the primary.",
  "Emergent",
  "The malignancy features from slide 13: no infectious origin, <b>duration over 2 weeks</b>, "
  "<b>size over 1.5&nbsp;cm</b>, firm and non-tender with little mobility, <b>age over 40</b>, "
  "tobacco and alcohol, and ulceration.", "37, 39", D18),

 ("Primary neck tumours &mdash; the list", NECK,
  "<b>Slide 38 is a picture of a table</b> &middot; malignant against benign, primary in the neck",
  "<b>Malignant:</b> sarcomas (rhabdomyosarcoma, fibrosarcoma, malignant fibrous histiocytoma, "
  "liposarcoma, leiomyosarcoma); malignant peripheral nerve sheath tumours; lymphoma; and metastasis "
  "&mdash; mucosal cancer from head and neck, salivary malignancies, skin malignancies. "
  "<b>Benign:</b> vascular neoplasms, chiefly <b>paragangliomas (carotid body, vagal, "
  "jugulotympanic)</b>; arteriovenous malformations; peripheral nerve neoplasms (schwannomas, "
  "neurofibromas, neuromas); and lipomas.",
  "As for any neck neoplasm &mdash; fine needle aspiration first.",
  "By tumour type.", "Emergent",
  "A pulsatile mass or a bruit means vascular, and paraganglioma heads that list.", "38", D18),

 ("Thyroid nodule and mass", THY,
  "<b>MIDLINE mass that ELEVATES WITH SWALLOWING</b> &middot; the main cause of an anterior neck "
  "lump",
  "The main cause of anterior neck masses and lumps. <b>An immobile midline neck mass that elevates "
  "with swallowing is likely thyroid.</b> Risk factors: age under 30 or over 60, childhood head and "
  "neck irradiation, full body irradiation for bone marrow transplant, family history of thyroid "
  "cancer, and <b>multiple endocrine neoplasia type 2</b>. Recent growth, dysphagia or obstruction "
  "are the concerning symptoms.",
  "<b>Ultrasound with fine needle aspiration, thyroid-stimulating hormone, T3 and T4.</b> Incidental "
  "nodules over 1&nbsp;cm need evaluation. If <b>hyperthyroid with a low thyroid-stimulating "
  "hormone</b>, do a <b>radionuclide scan with technetium BEFORE the aspiration</b>: a <b>&ldquo;hot&rdquo; "
  "(hyperfunctioning) nodule needs no biopsy</b>, while a <b>&ldquo;cold&rdquo; or &ldquo;warm&rdquo; "
  "nodule does</b>.",
  "Determined by the biopsy. Fine needle aspiration is the diagnostic procedure of choice once "
  "primary thyroid disease has been excluded on labs.",
  "Urgent",
  "<b>If thyroid cancer is suspected, avoid iodine-contrast computed tomography</b> &mdash; it "
  "compromises radioiodine treatment afterwards.", "40&ndash;41", D18),

 ("Papillary thyroid carcinoma", THY,
  "<b>Commonest (75%)</b> &middot; <b>best prognosis</b> &middot; young women",
  "The commonest thyroid cancer at 75%, with the best prognosis, commonest in young females. "
  "Involves thyroid epithelial cells.",
  "Fine needle aspiration.",
  "Lobectomy or thyroidectomy, with or without neck dissection, ablation and surveillance. Almost "
  "all thyroid cancers need thyroidectomy, except a well-differentiated cancer localised to one lobe "
  "with no metastasis.",
  "Urgent", "Commonest and kindest &mdash; the pairing is the exam point.", "42, 44", D18),

 ("Follicular thyroid carcinoma", THY,
  "<b>Second commonest (16%)</b> &middot; spreads by <b>BLOOD to bone and lung</b>",
  "16% of thyroid cancers, involving thyroid epithelial cells. Spreads to local lymph nodes or "
  "<b>by blood to bone and lungs</b>. The <b>H&uuml;rthle cell variant is more aggressive</b>, with "
  "a higher risk of metastases and recurrence.",
  "Fine needle aspiration.",
  "As for papillary: lobectomy or thyroidectomy with or without neck dissection and ablation.",
  "Urgent", "Haematogenous spread is what separates it from papillary.", "42, 44", D18),

 ("Medullary thyroid carcinoma", THY,
  "<b>About 5%</b> &middot; <b>parafollicular C cells</b> &middot; <b>calcitonin</b> &middot; "
  "screen for <b>MEN</b>",
  "About 5%. A disorder of the <b>parafollicular or C cells, which produce calcitonin</b>. More "
  "insidious, <b>most likely to metastasise</b>, and can go undiagnosed until a metastasis is found.",
  "Fine needle aspiration; calcitonin.",
  "<b>Thyroidectomy</b> with monitoring for recurrence on screening labs, with or without external "
  "beam radiation for nodal disease. <b>Screen family members for multiple endocrine neoplasia.</b>",
  "Urgent",
  "The only one of the four with a familial syndrome to chase in the relatives.", "42, 44", D18),

 ("Anaplastic thyroid carcinoma", THY,
  "<b>1%</b> &middot; <b>elderly</b> &middot; <b>death in 6&ndash;36 months</b> &middot; resistant "
  "to all treatment",
  "1% of thyroid cancers, commonly in elderly patients. Small cell, giant cell and spindle cell "
  "types. <b>The most aggressive form &mdash; death in 6 to 36 months &mdash; and resistant to all "
  "treatment modalities.</b>",
  "Fine needle aspiration; staging imaging.",
  "<b>Isthmectomy</b> rather than thyroidectomy.", "Emergent",
  "The one thyroid cancer where the prognosis is measured in months.", "42, 44", D18),

 ("Primary thyroid lymphoma", THY,
  "Associated with <b>Hashimoto thyroiditis</b> &middot; non-Hodgkin <b>B cell</b>",
  "Most commonly non-Hodgkin B cell tumours, associated with Hashimoto thyroiditis.",
  "<b>Fine needle aspiration alone cannot separate lymphoma from Hashimoto</b> &mdash; a biopsy is "
  "needed to confirm, along with lymphoma staging.",
  "<b>Chemotherapy and radiation</b> &mdash; not primarily surgical, unlike the carcinomas above.",
  "Urgent",
  "The one thyroid malignancy where the answer is not an operation.", "45", D18),
]

# (does it hurt, where it sits, the finding that names it)
DIFF_L18 = {
 "Branchial cleft cyst": ("Yes when infected", "<b>Lateral</b> &mdash; anterior border of sternocleidomastoid", "Tender inflammatory mass appearing after an upper respiratory infection"),
 "Thyroglossal duct cyst": ("No unless infected", "<b>Midline</b> anterior neck", "<b>Moves vertically with swallowing or tongue protrusion</b>"),
 "Laryngocele": ("No", "Larynx &mdash; level of the false cord", "Smooth dilation at the false cord on laryngoscopy"),
 "Plunging ranula": ("No &mdash; painless", "<b>Submental</b>, from the sublingual gland", "Extends through mylohyoid into the neck"),
 "Lymphangioma (cystic hygroma)": ("No &mdash; non-tender", "Anywhere; often posterior triangle", "<b>Transilluminates</b> &mdash; soft, doughy, compressible"),
 "Haemangioma": ("No", "Superficial, any site", "<b>Enlarges with crying or straining</b>; red or bluish, compressible"),
 "Teratoma": ("No", "Any; noted at birth", "Firm, with <b>calcifications</b> on imaging"),
 "Dermoid cyst": ("No &mdash; non-tender", "<b>Midline</b> submental", "Mobile midline mass that does NOT move with the tongue"),
 "Thymic cyst": ("Only if infected", "Lower anterior neck", "<b>Hassall corpuscles</b> on biopsy"),
 "Sternocleidomastoid tumour of infancy": ("No &mdash; painless", "<b>Within the sternocleidomastoid</b>", "Firm discrete mass with congenital torticollis"),
 "Reactive viral lymphadenopathy": ("Mild", "Cervical nodes, children", "Regresses in 1&ndash;2 weeks with an upper respiratory infection"),
 "HIV-associated cervical adenopathy": ("No", "Neck is the commonest site", "Follicular hyperplasia after tuberculosis and lymphoma are excluded"),
 "Suppurative bacterial lymphadenopathy": ("Yes", "<b>Submandibular or jugulodigastric</b>", "Sore throat and skin lesions with the node"),
 "Toxoplasmosis": ("Varies", "Cervical nodes", "<b>Undercooked meat or cat faeces</b> in the history"),
 "Tularemia": ("Yes &mdash; painful adenopathy", "Cervical nodes", "<b>Rabbits, ticks or contaminated water</b>, with tonsillitis"),
 "Brucellosis": ("No", "<b>Total body</b>, not just neck", "<b>Unpasteurised milk</b>"),
 "Cat scratch disease": ("Varies", "<b>Preauricular and submandibular</b>", "<b>Cat contact</b>, patient under 20"),
 "Actinomycosis": ("No &mdash; painless", "Submandibular or upper digastric", "Painless and <b>fluctuant</b>"),
 "Atypical mycobacteria": ("Yes", "<b>Unilateral</b>, anterior triangle or parotid", "<b>Brawny reddish-brown skin</b> over it, in a child"),
 "Tuberculous adenitis (scrofula)": ("Varies", "<b>Bilateral and diffuse</b>", "Adults more than children; acid-fast bacilli"),
 "Fungal neck infection": ("Varies", "Cervical nodes", "Immunocompromised host; fungal culture and serology"),
 "Neck neoplasm &mdash; general": ("No &mdash; asymptomatic", "Cervical nodes, often jugulodigastric", "<b>Firm, immobile, over 1.5&nbsp;cm, present over 2 weeks</b>"),
 "Primary neck tumours &mdash; the list": ("Varies", "Neck soft tissue", "Pulsatile or bruit means <b>paraganglioma</b>"),
 "Thyroid nodule and mass": ("No", "<b>Midline</b> anterior neck", "<b>Elevates with swallowing</b>; hot nodule needs no biopsy"),
 "Papillary thyroid carcinoma": ("No", "Thyroid", "Commonest at 75%, best prognosis, young women"),
 "Follicular thyroid carcinoma": ("No", "Thyroid", "Spreads <b>by blood to bone and lung</b>"),
 "Medullary thyroid carcinoma": ("No", "Thyroid", "<b>C cells and calcitonin</b>; screen for multiple endocrine neoplasia"),
 "Anaplastic thyroid carcinoma": ("Varies", "Thyroid", "Elderly; <b>death in 6&ndash;36 months</b>"),
 "Primary thyroid lymphoma": ("No", "Thyroid", "<b>Hashimoto thyroiditis</b> in the background"),
}

# The deck's only clinical photograph. Everything else is a diagram or a table.
IMGS_L18 = {
 "Haemangioma": ("l18-s027_pos1.jpg", 27),
}
