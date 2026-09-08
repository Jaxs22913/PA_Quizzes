# -*- coding: utf-8 -*-
"""Lecture 19, second pool -- Oral Cavity, Salivary Glands and Neck."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "CMS I Disorders of the Oral Cavity, Salivary Glands"
IO = ("Disorders of the oral cavity, salivary glands, and neck: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")

QUESTIONS = [

Q("Aphthous stomatitis", IO,
  "A 19-year-old student has recurrent painful oral ulcers with yellow-grey centres and red halos, "
  "each under a centimetre, appearing on the inner cheek and inner lip and healing in about a week. "
  "They recur during examination periods.",
  [["Minor aphthous ulceration",
    "Correct. Minor aphthae are under a centimetre, are the commonest form, burn and tingle before "
    "they appear, and heal in 7 to 10 days without scarring. Their location is diagnostic: they "
    "occur on freely moving, NON-keratinised mucosa such as buccal and labial mucosa, and stress is "
    "a recognised precipitant."],
   ["Major aphthous ulceration",
    "Major aphthae are larger than a centimetre, more painful, often multiple, carry a risk of "
    "scarring and last over a month. The size and the one-week healing time here place these firmly "
    "in the minor category."],
   ["Herpetic gingivostomatitis",
    "Primary herpes affects KERATINISED surfaces such as the hard palate and attached gingiva, "
    "typically with fever and cervical lymphadenopathy in a child or young adult, and it is a single "
    "primary illness rather than a stress-related recurrent pattern on the buccal mucosa."],
   ["Herpetiform aphthous ulceration",
    "The herpetiform variant produces numerous tiny ulcers of 1 to 3 millimetres, carries a scarring "
    "risk and lasts over a month, despite the name having nothing to do with herpes. The lesions "
    "here are fewer and larger."]],
  "diagnosis", D, 16),

Q("Oral lichen planus", IO,
  "A 54-year-old woman has lacy white lines on both buccal mucosae that cannot be wiped away. She "
  "asks whether it is dangerous.",
  [["It carries a 1 to 4 per cent risk of squamous cell carcinoma, higher if ulcerative",
    "Correct. Oral lichen planus is a chronic autoimmune condition in which activated lymphocytes "
    "destroy the basal layer, and between 1 and 4 per cent progress to squamous cell carcinoma. The "
    "risk is higher with ulcerative lesions, which is why close follow-up rather than simple "
    "reassurance is the point of making the diagnosis."],
   ["It is entirely benign and needs no follow-up",
    "This is the reassuring answer and the reason the malignant potential is emphasised. Discharging "
    "the patient means nobody is watching a premalignant lesion in a site that is easy to examine."],
   ["It transforms to malignancy in the majority of cases",
    "Overstating the risk causes unnecessary alarm and can lead to overtreatment. The figure is a "
    "few per cent, which justifies surveillance rather than aggressive intervention."],
   ["It is an infection that will clear with antifungal treatment",
    "Candidiasis is the white lesion that responds to antifungals, and it is distinguished by wiping "
    "off. Lichen planus is immune-mediated and its striae are part of the mucosa."]],
  "mechanism", D, 22),

Q("Behcet syndrome", IO,
  "A 29-year-old man has recurrent painful oral ulcers. Further questioning reveals similar ulcers "
  "on the scrotum, and he has had episodes of eye inflammation and joint pain.",
  [["Behcet syndrome",
    "Correct. Oral ulcers are the commonest feature of Behcet, affecting up to 100 per cent of "
    "patients, and genital ulcers occur in about 75 per cent and look identical to oral aphthae. The "
    "diagnosis is clinical: recurrent aphthous ulceration IN THE CONTEXT of the characteristic "
    "systemic manifestations, which here include ocular and articular involvement."],
   ["Simple recurrent aphthous stomatitis",
    "Recurrent aphthae, or Sutton disease, are confined to the mouth and carry no systemic features. "
    "It is precisely the genital, ocular and joint involvement that lifts this out of that "
    "category."],
   ["Herpes simplex infection",
    "Recurrent herpes produces grouped vesicles that ulcerate on keratinised surfaces with a burning "
    "prodrome, and it does not cause the multisystem inflammation described. Genital herpes is "
    "possible but would not explain the eye and joint disease."],
   ["Systemic lupus erythematosus",
    "Lupus does cause oral ulcers in around 40 per cent of patients and can affect joints and eyes, "
    "so it is a fair differential, but the ulcers are typically painless or variable and the "
    "characteristic genital aphthae of Behcet are not a lupus feature."]],
  "diagnosis", D, 19),

Q("Herpes simplex", IO,
  "A 26-year-old woman has recurrent painful lesions at the vermilion border of the lip, always "
  "preceded by a day of burning and tingling, triggered by sunlight and stress.",
  [["Reactivation of virus latent in the trigeminal ganglion",
    "Correct. After a primary infection the virus travels along the axon to the trigeminal ganglion "
    "and persists there. Reactivation is triggered by stress, trauma, immunosuppression or "
    "ultraviolet light, and the virus migrates back down the axonal sheath, which is why the "
    "prodrome of burning and tingling precedes any visible lesion by about 24 hours."],
   ["A new primary infection each time",
    "Primary infection occurs once, most commonly as herpetic gingivostomatitis in a seronegative "
    "child or young adult with fever and lymphadenopathy. Repeated identical lesions at the same "
    "site are reactivation of established latent virus."],
   ["An autoimmune reaction to sunlight",
    "Photosensitive autoimmune disease exists, but it does not produce a 24-hour neurological "
    "prodrome of burning and tingling, which is characteristic of a virus travelling along a nerve."],
   ["Bacterial superinfection of chapped lips",
    "Angular cheilitis and impetigo can affect the perioral region, but neither has a prodrome, "
    "neither recurs at exactly the same site with these triggers, and both look different from "
    "grouped vesicles."]],
  "mechanism", D, 25),

Q("Sialolithiasis", IO,
  "A clinician wants the most sensitive test to detect a salivary stone, and separately the most "
  "accurate method for detecting calculi.",
  [["Computed tomography is the most sensitive; digital subtraction sialography the most accurate",
    "Correct. The lecture separates these two claims deliberately. Computed tomography detects the "
    "greatest proportion of stones, because it resolves small calcifications anywhere in the gland "
    "and duct, while digital subtraction sialography is described as the most accurate method for "
    "detecting calculi because it opacifies the duct system directly."],
   ["Plain radiography is the most sensitive",
    "Plain films do show submandibular stones, because those are calcium phosphate and hydroxyapatite "
    "and therefore radiopaque, but they miss radiolucent stones and small calculi that computed "
    "tomography resolves."],
   ["Ultrasound is both the most sensitive and the most accurate",
    "Ultrasound shows an echogenic structure with an acoustic shadow and is a reasonable first test, "
    "being cheap and radiation-free, but it is operator-dependent and less sensitive than computed "
    "tomography for small or deeply placed stones."],
   ["Magnetic resonance imaging is the most sensitive",
    "Magnetic resonance shows soft tissue well but is comparatively poor at demonstrating "
    "calcification, which is exactly what a stone is. It is not the modality named for this "
    "purpose."]],
  "testing", D, 42),

Q("Salivary gland neoplasm", IO,
  "A 58-year-old man has a slowly enlarging painless mass at the tail of the parotid gland with no "
  "facial weakness.",
  [["A benign parotid tumour, most likely a pleomorphic adenoma",
    "Correct. Between 64 and 80 per cent of salivary neoplasms arise in the parotid, and 75 to 80 "
    "per cent of parotid tumours are benign. Benign parotid tumours characteristically present as "
    "slow-growing painless masses at the tail of the gland, and the absence of facial nerve "
    "involvement supports a benign process."],
   ["A malignant parotid tumour, most likely mucoepidermoid carcinoma",
    "Mucoepidermoid carcinoma is the commonest salivary malignancy, so it is the right answer to a "
    "different question. Malignancy is suggested by pain, facial nerve involvement, rapid growth or "
    "skin invasion, none of which is present."],
   ["A minor salivary gland tumour",
    "Minor gland tumours occur in the buccal, labial and palatal mucosa rather than at the parotid "
    "tail, and only about 35 per cent of them are benign, so the probability runs the other way in "
    "that site."],
   ["A parotid abscess",
    "An abscess is acutely painful with fever, erythema and often pus expressible from Stensen duct, "
    "developing over days. A slowly enlarging painless mass over months is not an infection."]],
  "diagnosis", D, 141),

Q("Salivary gland neoplasm", IO,
  "A student asks how the site of a salivary tumour relates to the chance that it is malignant.",
  [["The smaller the gland, the higher the proportion that are malignant",
    "Correct. Parotid tumours are 75 to 80 per cent benign, submandibular 50 to 60 per cent, and "
    "minor salivary glands only about 35 per cent benign. The relationship runs inversely with gland "
    "size, which is a memorable rule and changes how aggressively a small-gland lesion is "
    "investigated."],
   ["The larger the gland, the higher the proportion that are malignant",
    "This inverts the relationship and would lead to underestimating the risk of a minor salivary "
    "gland lesion, which is precisely the group where malignancy is most likely."],
   ["Site has no bearing on the likelihood of malignancy",
    "Site is one of the most useful pieces of information available before any test, because the "
    "benign proportion differs by more than twofold between parotid and minor glands."],
   ["Only the parotid gives rise to malignant tumours",
    "The parotid is the commonest site of salivary malignancy in absolute numbers because it is the "
    "commonest site of tumours generally, but submandibular and minor glands also produce cancers "
    "and do so at higher proportions."]],
  "mechanism", D, 139),

Q("Vocal cord paralysis", IO,
  "A 61-year-old woman has a breathy hoarse voice and occasional coughing while drinking, six weeks "
  "after thyroidectomy. Laryngoscopy shows one immobile vocal fold.",
  [["Unilateral vocal cord paralysis from recurrent laryngeal nerve injury",
    "Correct. The recurrent laryngeal nerve runs immediately behind the thyroid and is at risk "
    "during thyroidectomy. A unilateral paralysis leaves one cord unable to meet the other, which "
    "gives the breathy voice from air escaping and allows aspiration during swallowing, hence the "
    "coughing on drinking."],
   ["Bilateral vocal cord paralysis",
    "Bilateral paralysis produces inspiratory or biphasic STRIDOR and a weak cry, because both cords "
    "sit near the midline and obstruct the airway. Only one immobile fold is described, and stridor "
    "is absent."],
   ["Vocal cord nodules from postoperative voice strain",
    "Nodules are bilateral, symmetric and appear at the junction of the anterior third and posterior "
    "two thirds after prolonged vocal abuse. They do not immobilise a cord and would not cause "
    "aspiration."],
   ["Laryngeal oedema from intubation",
    "Post-intubation oedema causes hoarseness and sometimes stridor but resolves within days, not "
    "six weeks, and it does not fix a cord in position on laryngoscopy."]],
  "diagnosis", D, 53),

Q("Vocal cord paralysis", IO,
  "A patient with vocal cord paralysis after a neck operation asks whether the voice will recover. "
  "Laryngeal electromyography is arranged.",
  [["It predicts recovery: a bruised or stretched nerve may return over 6 months to a year",
    "Correct. Electromyography distinguishes a nerve that is still in continuity from one that is "
    "not. A bruised or stretched nerve may recover function over six months to a year, whereas a "
    "transected nerve or one infiltrated by malignancy will not, which is what determines whether to "
    "wait or to proceed to medialisation."],
   ["It confirms which cord is paralysed",
    "Laryngoscopy already establishes which cord is immobile by direct observation. "
    "Electromyography is asked a different question, about the state of the nerve rather than the "
    "position of the fold."],
   ["It measures the degree of airway obstruction",
    "Airway compromise is assessed clinically and by observing the cords, particularly in bilateral "
    "paralysis. Electromyography records muscle electrical activity and says nothing about airway "
    "calibre."],
   ["It determines whether the lesion is in the vagus or the recurrent laryngeal nerve",
    "Distinguishing a vagal from a recurrent laryngeal lesion matters and is done by the pattern of "
    "associated deficits and by imaging along the nerve's course. That is not what this test is used "
    "for here."]],
  "testing", D, 56),

Q("Vocal cord papillomatosis", IO,
  "A 3-year-old with recurrent respiratory papillomatosis is deteriorating. A clinician suggests "
  "tracheostomy to secure the airway.",
  [["Avoid tracheostomy, because it creates another site the papillomas favour",
    "Correct. Papillomas have an affinity for squamociliary junctions, the boundaries where "
    "ciliated respiratory epithelium meets squamous epithelium. A tracheostomy creates a new such "
    "junction, giving the disease a fresh site to seed and spreading it distally into the trachea, "
    "which is why it is specifically avoided."],
   ["Perform tracheostomy, as airway protection outweighs other considerations",
    "Airway protection matters, but this particular intervention worsens the "
    "underlying disease in a way that few others do. Repeated debulking is preferred precisely to "
    "avoid creating that junction."],
   ["Give systemic antivirals to cure the human papillomavirus infection",
    "There is no curative treatment for the virus. Management aims to remove symptomatic lesions "
    "with minimal morbidity, using carbon dioxide laser, cold steel dissection or a microdebrider."],
   ["Give intralesional cidofovir as first-line therapy",
    "Cidofovir is an off-label adjuvant with no established evidence of efficacy, though excellent "
    "responses have been reported. It is not first line and does not replace surgical removal of "
    "obstructing lesions."]],
  "treatment", D, 52),

Q("Epiglottitis", IO,
  "A 6-year-old with suspected epiglottitis is transferred to theatre. A student asks why the "
  "incidence of this disease has fallen so sharply.",
  [["Haemophilus influenzae type B vaccination",
    "Correct. The commonest pathogen in the paediatric population is Haemophilus influenzae type B, "
    "and routine immunisation has reduced the incidence of supraglottitis by over 90 per cent. It "
    "still occurs, from Streptococcus pneumoniae, Staphylococcus aureus and beta-haemolytic "
    "streptococci and in unimmunised children, which is why awareness still matters."],
   ["Widespread use of antibiotics for sore throat",
    "Antibiotic prescribing for pharyngitis targets group A streptococcus and has not been the "
    "driver of this change. The fall is specific and dates from the introduction of a particular "
    "vaccine."],
   ["Improved nutrition and living conditions",
    "General improvements have reduced many infectious diseases, but the decline here is abrupt and "
    "tied to a specific intervention rather than gradual and socioeconomic."],
   ["Pneumococcal conjugate vaccination",
    "Streptococcus pneumoniae is one of the other organisms that causes supraglottitis, so its "
    "vaccine contributes at the margins, but it is not the type B organism responsible for the "
    "historical burden of the disease."]],
  "cause", D, 60),

Q("Pharyngitis", IO,
  "A student is asked to distinguish pharyngitis, tonsillitis and pharyngotonsillitis.",
  [["Tonsillitis if the tonsils are affected, pharyngitis if the throat is, both if both",
    "Correct. The three terms describe which structure is inflamed rather than three different "
    "diseases, and the same organisms cause all of them. Naming them separately matters mainly "
    "because tonsillar involvement raises the possibility of complications such as peritonsillar "
    "abscess."],
   ["Pharyngitis is always viral and tonsillitis always bacterial",
    "Both structures can be affected by either. Around 70 per cent of pharyngitis is viral and 30 "
    "per cent bacterial regardless of which structure is inflamed, so the anatomical name carries no "
    "microbiological information."],
   ["Tonsillitis refers to the adenoids and pharyngitis to the palatine tonsils",
    "This confuses the structures. The adenoid is the nasopharyngeal tonsil, and tonsillitis "
    "conventionally refers to the palatine tonsils in the oropharynx."],
   ["The distinction depends on the duration of symptoms",
    "Duration separates acute from chronic disease, which is a different axis entirely. These three "
    "terms are anatomical."]],
  "mechanism", D, 69),

Q("Gingivitis", IO,
  "A 33-year-old man has gums that are red, swollen and bleed when he brushes, with little "
  "discomfort. There is no pocketing or tooth mobility.",
  [["Gingivitis, which is reversible with professional cleaning and good home care",
    "Correct. Gingivitis is the mildest form of periodontal disease: inflammation confined to the "
    "gingiva from bacterial plaque at the gum line, producing erythema, oedema and bleeding with "
    "little discomfort. The critical point is that it is entirely reversible at this stage, before "
    "the periodontal ligament and bone are destroyed."],
   ["Periodontitis, which causes irreversible bone loss",
    "Periodontitis is what untreated gingivitis becomes: plaque spreads below the gum line, pockets "
    "form, and the periodontal ligament and bone are destroyed so that teeth loosen. The absence of "
    "pocketing and mobility here means that has not yet happened."],
   ["A dental abscess",
    "An abscess is a localised collection of pus around a tooth root or in a periodontal pocket, "
    "causing significant pain and swelling. Generalised painless bleeding gums are a different "
    "process."],
   ["Oral lichen planus",
    "Lichen planus can affect the gingiva as a desquamative gingivitis, so it is worth considering, "
    "but it produces lacy white striae or erosions rather than the plaque-related bleeding described "
    "here."]],
  "diagnosis", D, 121),

Q("Dental abscess", IO,
  "A 40-year-old man has a dental abscess. The tooth is badly broken down and cannot be restored.",
  [["Extraction followed by curettage of the apical tissue",
    "Correct. The management depends on whether the tooth can be saved. If it can be restored, a "
    "root canal removes the infected pulp and preserves the tooth. If it cannot, extraction is "
    "required, and the apical tissue is curetted because leaving infected granulation tissue behind "
    "allows the infection to persist in the socket."],
   ["Root canal treatment",
    "A root canal is the correct answer for a restorable tooth, which is what makes it the tempting "
    "option. It cannot succeed on a tooth that cannot be restored, because there is nothing to "
    "rebuild around the treated root."],
   ["Antibiotics alone until the infection settles",
    "Antibiotics are part of treatment but never definitive, because the source is a physical "
    "collection and a necrotic pulp. Relying on them alone leads to recurrence and, in the worst "
    "case, spread into the deep neck spaces."],
   ["Incision and drainage alone",
    "Drainage relieves the pressure and is often needed acutely, but leaving the causative tooth in "
    "place means the abscess reforms. The definitive step addresses the tooth."]],
  "treatment", D, 117),

Q("Cervical adenitis", IO,
  "A 7-year-old has a unilateral, solitary, tender anterior cervical node following a sore throat.",
  [["Beta-haemolytic streptococcus, which accounts for about 70 per cent",
    "Correct. Local infections of the ear, nose and throat drain to regional nodes, and about 70 per "
    "cent of these unilateral solitary anterior cervical nodes relate to beta-haemolytic "
    "streptococcal infection. Around 20 per cent are staphylococcal including MRSA, and 10 per cent "
    "are viral, atypical mycobacterial or Bartonella."],
   ["Staphylococcus aureus, which accounts for the majority",
    "Staphylococcus, including MRSA, is the second commonest at around 20 per cent, so it is a "
    "genuine consideration and matters for antibiotic choice, but it is not the majority."],
   ["Bartonella henselae",
    "Cat scratch disease sits in the residual 10 per cent alongside viruses and atypical "
    "mycobacteria, and it requires a history of cat contact with preauricular or submandibular node "
    "involvement."],
   ["Mycobacterium tuberculosis",
    "Tuberculous adenitis affects adults more than children and produces diffuse bilateral "
    "lymphadenopathy. A single tender node after a sore throat is a pyogenic pattern."]],
  "cause", D, 92),

Q("Cervical lymphadenopathy", IO,
  "A clinician is describing a cervical node and considers which features suggest malignancy.",
  [["Immobility and non-tenderness",
    "Correct. The lecture specifies the descriptors that matter: size, shape, mobility, consistency "
    "and tenderness. An immobile node suggests fixation to surrounding structures by tumour, and "
    "non-tenderness points away from an inflammatory cause, since inflamed nodes hurt. Persistence "
    "or continued enlargement is what triggers fine needle aspiration."],
   ["Tenderness and rapid enlargement",
    "Tenderness suggests inflammation rather than malignancy, and rapid enlargement with other "
    "infective symptoms suggests infection. Rapid growth WITHOUT infective symptoms is the "
    "combination that suggests lymphoma."],
   ["Softness and fluctuance",
    "Fluctuance indicates a fluid-filled or cystic structure, which points to an abscess or a "
    "congenital cyst rather than a solid tumour. Malignant nodes are characteristically firm or "
    "hard."],
   ["Bilateral distribution",
    "Bilateral symmetrical lymphadenopathy more often reflects a systemic or viral process such as "
    "mononucleosis. A solitary immobile node is the more concerning pattern."]],
  "finding", D, 93),

Q("Chronic laryngitis", IO,
  "A 57-year-old smoker has been hoarse for seven weeks. He has no pain and no other symptoms.",
  [["Refer to ear, nose and throat for laryngoscopy",
    "Correct. Voice disturbance lasting more than two weeks is defined as chronic laryngitis, and "
    "the lecture is explicit that this is not a true diagnosis. It is a description that obliges a "
    "search for an underlying cause, and laryngeal cancer and vocal cord polyps are the two that "
    "must be excluded, particularly in a smoker."],
   ["A trial of proton pump inhibitor for reflux laryngitis",
    "Reflux is a genuine contributor to chronic laryngeal irritation and may well be part of the "
    "picture, but treating empirically for seven weeks of hoarseness in a smoker without visualising "
    "the cords risks missing a carcinoma."],
   ["Voice rest and reassurance",
    "Voice rest is appropriate for ACUTE laryngitis, which settles within about a week of an upper "
    "respiratory infection. Applying it beyond two weeks is exactly the error the two-week rule "
    "exists to prevent."],
   ["A course of antibiotics",
    "Antibiotics are not indicated even in acute laryngitis unless secondary bacterial infection is "
    "suspected, and they have no role at all in a chronic painless hoarseness with no infective "
    "features."]],
  "next step", D, 58),
]
