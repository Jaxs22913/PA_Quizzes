# -*- coding: utf-8 -*-
"""Lecture 19, third pool -- Oral Cavity, Salivary Glands and Neck."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "CMS I Disorders of the Oral Cavity, Salivary Glands"
IO = ("Disorders of the oral cavity, salivary glands, and neck: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")

QUESTIONS = [

Q("Peritonsillar abscess", IO,
  "A 22-year-old with a peritonsillar abscess has trismus so severe the mouth opens barely two "
  "centimetres.",
  [["Trismus is the most reliable symptom of this abscess",
    "Correct. Pus tracking into the space adjacent to the medial pterygoid muscle irritates it and "
    "provokes spasm, which limits mouth opening. Of the classic triad of trismus, uvular deviation "
    "and dysphonia, trismus is the most reliable, and it is also what "
    "makes examination and drainage technically difficult."],
   ["Trismus indicates the abscess has spread to the mediastinum",
    "Mediastinal spread is the feared complication of a RETROPHARYNGEAL abscess, carrying 50 per "
    "cent mortality. Trismus in peritonsillar disease reflects local muscle irritation rather than "
    "distant spread."],
   ["Trismus is caused by vagus nerve involvement",
    "Vagal involvement explains the DYSPHONIA, because the palate fails to elevate. Jaw opening is a "
    "trigeminal motor function through the muscles of mastication."],
   ["Trismus suggests an alternative diagnosis such as tetanus",
    "Tetanus does cause trismus, but in the setting of an untreated tonsillitis with unilateral "
    "palatal deviation and a hot potato voice, the local abscess explains it without invoking a rare "
    "systemic disease."]],
  "mechanism", D, 99),

Q("Peritonsillar abscess", IO,
  "A 25-year-old man has had three peritonsillar abscesses and multiple episodes of tonsillitis "
  "over two years.",
  [["Tonsillectomy, usually after the acute infection resolves",
    "Correct. Recurrent tonsillitis with recurrent peritonsillar abscesses is the indication for "
    "tonsillectomy, and most surgeons prefer to operate once the acute inflammation has settled, "
    "because the tissue planes are cleaner and bleeding is less. Quinsy tonsillectomy during "
    "infection is reserved for younger children, unresponsive cases or severe airway compromise."],
   ["Long-term prophylactic antibiotics",
    "Prolonged antibiotics do not prevent abscess formation and drive resistance. The tonsil itself "
    "is the reservoir, which is why removing it is what changes the recurrence rate."],
   ["Repeated needle aspiration each time it recurs",
    "Aspiration treats each episode but accepts that they will keep happening. Given three abscesses "
    "in two years, the question has moved from managing episodes to preventing them."],
   ["Tonsillectomy during the current acute infection in all cases",
    "Quinsy tonsillectomy exists but is the exception rather than the rule, used for particular "
    "circumstances. Applying it universally exposes patients to a more difficult operation than "
    "necessary."]],
  "treatment", D, 101),

Q("Retropharyngeal abscess", IO,
  "A student asks why retropharyngeal abscess carries such a high mortality if untreated.",
  [["The space extends to the posterior mediastinum",
    "Correct. The retropharyngeal space runs from the base of the skull to the posterior "
    "mediastinum, so an abscess there has a direct anatomical route into the chest. Mediastinitis "
    "carries a 50 per cent mortality, and the danger space beyond it is continuous left to right, "
    "which lets infection cross to either side."],
   ["The abscess compresses the carotid artery",
    "Carotid involvement is a recognised complication of deep neck infection generally, but the "
    "specific reason this abscess is so dangerous is its continuity with the mediastinum rather "
    "than a vascular effect."],
   ["It always progresses to Ludwig angina",
    "Ludwig angina is a separate deep neck infection of the submental, sublingual and submandibular "
    "spaces, usually odontogenic. The two are different spaces with different sources."],
   ["It causes irreversible damage to the recurrent laryngeal nerves",
    "Nerve injury is not the mechanism of death here. The lethal complications are mediastinitis, "
    "airway obstruction and aspiration pneumonia after rupture."]],
  "mechanism", D, 107),

Q("Ludwig angina", IO,
  "A 44-year-old man with Ludwig angina and diabetes is noted to have a more aggressive course than "
  "expected.",
  [["Klebsiella is more often involved in patients with diabetes",
    "Correct. The usual organisms are streptococci, staphylococci, Bacteroides and Fusobacterium, "
    "but Klebsiella features specifically in patients with diabetes, and that those "
    "patients may have a more aggressive clinical course. That changes both the expected tempo and "
    "the antibiotic choice."],
   ["Diabetes has no bearing on the course of deep neck infection",
    "Impaired neutrophil function and the different organism spectrum both make deep neck infection "
    "more dangerous in diabetes, which is why it is flagged rather than left as a background "
    "comorbidity."],
   ["The infection is usually viral in diabetic patients",
    "Ludwig angina is a bacterial cellulitis of the floor of the mouth regardless of the host. There "
    "is no viral form."],
   ["Diabetes protects against airway compromise",
    "Nothing about diabetes protects the airway, and the more aggressive course means airway "
    "compromise is if anything more likely and sooner."]],
  "cause", D, 108),

Q("Oral cavity anatomy", IO,
  "A clinician is defining the boundary between the oral cavity and the oropharynx for staging "
  "purposes.",
  [["The oral cavity is the anterior two thirds of the tongue; the oropharynx the posterior third",
    "Correct. The oral cavity includes the anterior two thirds of the tongue, buccal mucosa, floor "
    "of mouth, hard palate, upper and lower gingiva and retromolar trigone. The oropharynx is the "
    "posterior third of the tongue, palatine tonsil, soft palate and posterior pharyngeal wall. The "
    "distinction matters because the two behave differently and are treated differently."],
   ["The lip marks the anterior boundary of the oral cavity",
    "The lip was part of the oral cavity historically but has been excluded since the eighth staging "
    "system, which is a specific point worth holding. Using the older definition would misstage "
    "a lip tumour."],
   ["The soft palate belongs to the oral cavity",
    "The soft palate is an oropharyngeal subsite. Placing it in the oral cavity matters because "
    "oropharyngeal tumours are far more often human papillomavirus related and are treated with "
    "surgery plus radiotherapy."],
   ["The two are treated as a single site for staging",
    "They are staged and treated separately, precisely because the aetiology, the prognosis and the "
    "treatment differ. Oral cavity disease has surgical resection alone as its mainstay."]],
  "finding", D, 144),

Q("Oral cancer treatment", IO,
  "A 64-year-old man has a squamous cell carcinoma of the tonsil that is human papillomavirus "
  "positive.",
  [["Surgical resection with radiotherapy, which gives better functional outcomes",
    "Correct. Oropharyngeal tumours are treated with resection plus radiotherapy, and "
    "radiotherapy gives better functional outcomes in this site, where speech and "
    "swallowing are at stake. Between 60 and 80 per cent of oropharyngeal cancers are human "
    "papillomavirus related, which is also relevant to prognosis."],
   ["Surgical resection alone",
    "Resection alone is the stated approach for ORAL CAVITY cancer. Applying it to an oropharyngeal "
    "primary omits the radiotherapy that the site-specific evidence supports."],
   ["Chemotherapy alone as first-line treatment",
    "Chemotherapy has a role in advanced or palliative settings but is not the primary modality for "
    "a resectable head and neck squamous carcinoma."],
   ["Observation, since human papillomavirus related tumours regress",
    "Human papillomavirus positive oropharyngeal cancers have a better prognosis with treatment, "
    "which is a genuine and important difference, but they do not regress spontaneously and require "
    "definitive therapy."]],
  "treatment", D, 148),

Q("Oral cancer", IO,
  "A 58-year-old woman with a tongue lesion reports pain in her right ear, though examination of "
  "the ear is entirely normal.",
  [["Referred otalgia from cranial nerve involvement by the tumour",
    "Correct. The tongue and oropharynx share sensory innervation with the ear through branches of "
    "the trigeminal, glossopharyngeal and vagus nerves, so a tumour irritating those nerves is "
    "perceived as ear pain. A normal ear examination in a patient with an oral lesion should raise "
    "this rather than reassure, because it signals advanced disease."],
   ["Coincidental otitis media",
    "Otitis media would show a bulging or dull drum on examination, and the ear here is explicitly "
    "normal. Attributing the pain to a second condition that the examination excludes leaves the "
    "real cause unrecognised."],
   ["Temporomandibular joint dysfunction",
    "Temporomandibular disorders do refer pain to the ear with a normal examination, so they are a "
    "reasonable differential in isolation, but they come with jaw clicking and limited opening rather "
    "than a tongue lesion."],
   ["Eustachian tube dysfunction",
    "Eustachian tube dysfunction produces fullness and popping with a retracted drum, not pain with a "
    "normal drum, and it does not arise from a tongue lesion."]],
  "mechanism", D, 146),

Q("Oral candidiasis", IO,
  "A 3-month-old breastfed infant has white plaques on the tongue and buccal mucosa that wipe off. "
  "He is otherwise thriving.",
  [["Nystatin oral suspension",
    "Correct. Thrush is common in infants, whose immune systems and oral flora are still "
    "establishing, and topical antifungal therapy is the appropriate first step. Nystatin suspension "
    "acts locally with negligible systemic absorption, which is the right profile for a well infant "
    "with a superficial infection."],
   ["Oral fluconazole",
    "Systemic azole therapy is reserved for extensive, refractory or oesophageal disease, or for "
    "immunocompromised patients such as those with HIV who may need a longer course. It is "
    "disproportionate for uncomplicated infant thrush."],
   ["Investigate urgently for immunodeficiency",
    "Persistent or unusually severe candidiasis warrants that thought, but thrush in a thriving "
    "3-month-old is common and expected. Investigating every case would generate a great deal of "
    "unnecessary anxiety."],
   ["Topical corticosteroid",
    "Steroid suppresses local immunity and would worsen a fungal infection, which is exactly the "
    "mechanism by which inhaled corticosteroids cause thrush in adults."]],
  "treatment", D, 90),

Q("Hairy leukoplakia", IO,
  "A 41-year-old man has painless white lesions on the lateral border of the tongue that wax and "
  "wane. He is otherwise well and has no known medical conditions.",
  [["Test for HIV",
    "Correct. Hairy leukoplakia is a benign mucosal hyperplasia driven by Epstein-Barr virus, and it "
    "is strongly associated with HIV, where it is a common early finding. The lesion itself needs "
    "little more than observation, so its clinical value lies almost entirely in what it points to "
    "in a patient with no known diagnosis."],
   ["Excisional biopsy to exclude carcinoma",
    "Biopsy contributes to the diagnosis, but hairy leukoplakia is benign and is not premalignant in "
    "the way ordinary leukoplakia is. Treating it as a cancer question misses the association that "
    "matters."],
   ["Prescribe topical antifungal therapy",
    "Antifungals treat candidiasis, which wipes off. Hairy leukoplakia does not, and treating it as "
    "thrush would fail and would delay the important test."],
   ["Reassure and discharge, as it is benign",
    "The lesion is indeed benign, which makes this superficially reasonable. Discharging him means "
    "missing an opportunity to diagnose HIV at a stage when treatment is most effective."]],
  "next step", D, 136),

Q("Sialadenitis", IO,
  "A 68-year-old man has had chronic unilateral parotid swelling with minimal pain for several "
  "months. He has risk factors for tuberculosis.",
  [["Chronic granulomatous sialadenitis, needing fine needle aspiration",
    "Correct. Chronic unilateral or bilateral gland swelling with minimal pain is the picture of "
    "granulomatous sialadenitis, and primary tuberculosis should be considered when risk factors are "
    "present. The differential is wide, including cat scratch disease, sarcoidosis, actinomycosis, "
    "granulomatosis with polyangiitis and syphilis, so aspiration biopsy is needed."],
   ["Acute suppurative sialadenitis",
    "Acute bacterial disease presents over days with a firm, diffusely tender gland, overlying "
    "erythema, fever and pus from the duct. Months of minimally painful swelling is a different "
    "tempo entirely."],
   ["Sialolithiasis",
    "A stone produces intermittent swelling and pain timed to meals, with relief between them. "
    "Chronic constant swelling without that pattern argues against obstruction."],
   ["Mumps parotitis",
    "Mumps is an acute viral illness, usually bilateral, in children and young adults, with systemic "
    "symptoms. It does not persist for months in an elderly man."]],
  "diagnosis", D, 34),

Q("Epiglottitis in adults", IO,
  "A 46-year-old man has severe sore throat, odynophagia and a muffled voice for a day. He is "
  "febrile but not drooling and has no stridor. Fiberoptic laryngoscopy shows a swollen "
  "epiglottis.",
  [["Admit for observation, intravenous antibiotics and airway monitoring",
    "Correct. Adult supraglottitis progresses more slowly than the paediatric form and often does "
    "not require immediate intubation, so observation with humidification, glucocorticoids, "
    "intravenous antibiotics and nebulised adrenaline is appropriate. The airway is monitored because "
    "intubation or tracheostomy becomes necessary if it obstructs."],
   ["Immediate tracheostomy",
    "Tracheostomy is reserved for an airway that has obstructed or is about to. Performing it in an "
    "adult who is not drooling and has no stridor imposes a major intervention ahead of need."],
   ["Discharge on oral antibiotics with review in 24 hours",
    "The slower adult course does not make it safe to send home. The disease carries high mortality "
    "when it is not recognised and treated promptly, and deterioration can be rapid once it starts."],
   ["Lateral neck radiography before any treatment",
    "The thumbprint sign is not necessary for diagnosis, which has already been made by "
    "laryngoscopy, the gold standard. Ordering a film now delays treatment without adding "
    "information."]],
  "next step", D, 66),

Q("Rheumatic fever", IO,
  "A clinician explains why untreated streptococcal pharyngitis can damage the heart.",
  [["Antibodies against the streptococcus cross-react with heart muscle",
    "Correct. The organism shares antigenic determinants with human tissue, so the antibody response "
    "mounted against it also binds cardiac muscle, producing endocarditis, myocarditis or "
    "pericarditis. That is why the damage appears two to three weeks after the sore throat rather "
    "than during it, and why eradicating the organism early prevents it."],
   ["The bacteria spread through the bloodstream to the heart valves",
    "Direct bacterial seeding of valves describes infective endocarditis, which is a different "
    "disease with a different tempo. Rheumatic fever is immune-mediated, which is why it lags "
    "behind the infection."],
   ["Streptococcal toxin directly poisons the myocardium",
    "Toxin-mediated cardiac damage describes diphtheria, where the exotoxin causes myocarditis and "
    "heart block. Group A streptococcus produces toxins but the rheumatic mechanism is "
    "cross-reactive immunity."],
   ["The fever itself damages the myocardium",
    "Fever accompanies the illness but does not cause structural cardiac injury. If it did, every "
    "febrile illness would carry the same risk."]],
  "mechanism", D, 78),

Q("Malocclusion", IO,
  "A student is asked to describe the malocclusion classes used in practice.",
  [["Class I normal, Class II distal, Class III mesial occlusion",
    "Correct. The three classes describe how the lower dental arch sits relative to the upper. Class "
    "I is normal alignment, Class II is distal occlusion with the lower arch set back, and Class III "
    "is mesial occlusion with the lower arch forward. Naming them consistently is what allows the "
    "problem to be communicated to an orthodontist."],
   ["Class I mesial, Class II normal, Class III distal",
    "This reassigns all three labels. Class I is the reference normal, and building the scheme from "
    "the wrong baseline makes every subsequent description wrong."],
   ["The classes describe the degree of crowding rather than the bite relationship",
    "Crowding contributes to impaction and is a separate problem. The classification describes how "
    "the arches meet, which is why it is illustrated with profile views."],
   ["The classes describe which teeth are missing",
    "Missing teeth are one cause of malocclusion, alongside jaw-tooth size mismatch, thumb sucking "
    "and birth defects, but the classes describe the resulting bite rather than the cause."]],
  "finding", D, 126),

Q("Tooth disorders", IO,
  "A 29-year-old man has a painful lower wisdom tooth that has only partially erupted, with "
  "inflamed overlying gum.",
  [["Impaction, which predisposes to infection",
    "Correct. Impaction usually results from overcrowding and insufficient room for the tooth to "
    "erupt, and wisdom teeth are the usual culprits because they are the last to come through. A "
    "partially erupted tooth leaves a flap of gum over it that traps debris, which is why impacted "
    "teeth are more likely to become infected and are usually removed."],
   ["Dental caries of the wisdom tooth",
    "Caries can certainly affect a partially erupted tooth that is hard to clean, but the underlying "
    "problem described is the failure to erupt fully and the gum flap over it, which is what causes "
    "the pericoronal inflammation."],
   ["Malocclusion",
    "Malocclusion describes how the arches meet and can coexist with crowding, but it does not "
    "explain a single partially erupted tooth with inflamed overlying gum."],
   ["Pulpitis",
    "Pulpitis is inflammation of the tooth's pulp, usually from decay or injury, producing pain "
    "within the tooth rather than in the gum flap over an unerupted crown."]],
  "diagnosis", D, 125),

Q("Diphtheria prevention", IO,
  "A clinician is asked when a pregnant woman should receive Tdap.",
  [["Between 27 and 36 weeks of every pregnancy",
    "Correct. The recommendation is Tdap in each pregnancy between 27 and 36 weeks. Vaccinating in "
    "that window maximises transplacental antibody transfer, protecting the newborn during the "
    "months before the infant's own immunisation schedule has taken effect."],
   ["Once only, before the first pregnancy",
    "A single lifetime dose does not maintain the high maternal antibody levels needed for transfer, "
    "which is why the recommendation is repeated with each pregnancy rather than given once."],
   ["In the first trimester",
    "Vaccinating too early means antibody levels have fallen by delivery, so less is transferred at "
    "the point it matters. The timing is chosen for the transfer window rather than for convenience."],
   ["Immediately after delivery",
    "Postpartum vaccination protects the mother and reduces her chance of transmitting the "
    "infection, but it misses the transplacental transfer entirely, leaving the newborn without "
    "passive protection."]],
  "treatment", D, 114),
]
