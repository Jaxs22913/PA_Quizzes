# -*- coding: utf-8 -*-
"""Lecture 19 vignette pool C -- short keys, to hold the length bias down."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Disorders of the oral cavity, salivary glands, and neck: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")
C = lambda n: "CMS I Disorders of the Oral Cavity, Salivary Glands, Slide %d" % n

QUESTIONS = [

Q("Peritonsillar abscess", IO,
  "A 24-year-old with a peritonsillar abscess can barely open his mouth two centimetres.",
  [["Trismus",
    "Correct. Pus tracking beside the medial pterygoid irritates it into spasm, limiting mouth "
    "opening. Of the classic triad of trismus, uvular deviation and dysphonia, trismus is singled "
    "out as the most reliable, and it is also what makes examination and drainage difficult."],
   ["Mediastinal spread",
    "Mediastinitis is the feared complication of a RETROPHARYNGEAL abscess, whose space runs to the "
    "posterior mediastinum with 50 per cent mortality. It is not what limits jaw opening here."],
   ["Vagal involvement",
    "Vagus nerve involvement explains the DYSPHONIA, because the palate fails to elevate. Jaw "
    "opening is a trigeminal motor function through the muscles of mastication."],
   ["Tetanus",
    "Tetanus does cause trismus, but in a patient with untreated tonsillitis, unilateral palatal "
    "deviation and a hot potato voice, the local abscess explains it without a rare systemic "
    "disease."]], C(99)),

Q("Peritonsillar abscess", IO,
  "A 27-year-old man has had three peritonsillar abscesses and repeated tonsillitis over two years.",
  [["Tonsillectomy once the infection settles",
    "Correct. Recurrent tonsillitis with recurrent abscesses is the indication for tonsillectomy, "
    "and most surgeons prefer to operate after the acute inflammation has resolved, because the "
    "planes are cleaner and bleeding is less. Quinsy tonsillectomy during infection is reserved for "
    "particular circumstances."],
   ["Long-term prophylactic antibiotics",
    "Prolonged antibiotics do not prevent abscess formation and drive resistance. The tonsil is the "
    "reservoir, which is why removing it changes the recurrence rate."],
   ["Repeated aspiration each episode",
    "Aspiration treats each episode while accepting that they will continue. After three abscesses "
    "the question has moved from managing episodes to preventing them."],
   ["Quinsy tonsillectomy in all cases",
    "Quinsy tonsillectomy exists but is the exception, used for younger children, unresponsive cases "
    "or severe airway compromise. Applying it universally means a harder operation."]], C(101)),

Q("Mononucleosis", IO,
  "A 21-year-old rugby player is confirmed to have mononucleosis and asks when he can train again.",
  [["Avoid contact sport for about a month",
    "Correct. Epstein-Barr virus enlarges the spleen, and a capsule under tension can rupture with "
    "minor abdominal trauma. The restriction runs until splenomegaly has resolved, monitored by "
    "ultrasound, because feeling well and having a normal spleen are not the same thing."],
   ["Return once the fever settles",
    "Symptomatic and splenic recovery follow different timelines. A patient can feel entirely well "
    "while the spleen is still enlarged, which is exactly when a tackle can rupture it."],
   ["No restriction is needed",
    "Splenic rupture is rare but real and is the reason the restriction exists. Removing it discards "
    "the one piece of advice that prevents a catastrophic outcome."],
   ["Avoid all exercise for six months",
    "Six months of inactivity far exceeds what the risk justifies and is unlikely to be followed. "
    "The restriction concerns contact and heavy lifting and is measured in weeks."]], C(86)),

Q("Oral candidiasis", IO,
  "A 3-month-old breastfed infant has white plaques on the tongue and buccal mucosa that wipe off. "
  "He is thriving.",
  [["Nystatin suspension",
    "Correct. Thrush is common in infants whose oral flora and immunity are still establishing, and "
    "topical antifungal therapy is the appropriate first step. Nystatin acts locally with negligible "
    "systemic absorption, which is the right profile for a well infant with superficial infection."],
   ["Oral fluconazole",
    "Systemic azole therapy is reserved for extensive, refractory or oesophageal disease, or for "
    "immunocompromised patients such as those with HIV who may need longer courses."],
   ["Urgent immunodeficiency workup",
    "Persistent or unusually severe candidiasis warrants that thought, but thrush in a thriving "
    "3-month-old is common and expected."],
   ["Topical corticosteroid",
    "Steroid suppresses local immunity and would worsen a fungal infection, which is exactly how "
    "inhaled corticosteroids cause thrush in adults."]], C(90)),

Q("Sialadenitis", IO,
  "A 70-year-old man has chronic unilateral parotid swelling with minimal pain for several months. "
  "He has tuberculosis risk factors.",
  [["Chronic granulomatous sialadenitis",
    "Correct. Chronic unilateral or bilateral swelling with minimal pain is the picture, and primary "
    "tuberculosis should be considered where risk factors exist. The differential is wide, including "
    "cat scratch disease, sarcoidosis, actinomycosis, granulomatosis with polyangiitis and syphilis, "
    "so fine needle aspiration biopsy is needed."],
   ["Acute suppurative sialadenitis",
    "Acute bacterial disease presents over days with a firm diffusely tender gland, erythema, fever "
    "and pus from the duct. Months of minimally painful swelling is a different tempo."],
   ["Sialolithiasis",
    "A stone gives intermittent swelling and pain timed to meals with relief between. Constant "
    "chronic swelling argues against obstruction."],
   ["Mumps parotitis",
    "Mumps is an acute viral illness, usually bilateral, in children and young adults with systemic "
    "symptoms. It does not persist for months in an elderly man."]], C(34)),

Q("Epiglottitis in adults", IO,
  "A 48-year-old man has severe sore throat, odynophagia and a muffled voice for a day. He is "
  "febrile but not drooling and has no stridor. Laryngoscopy shows a swollen epiglottis.",
  [["Admit for observation and intravenous antibiotics",
    "Correct. Adult supraglottitis progresses more slowly than the paediatric form and often does "
    "not need immediate intubation, so observation with humidification, glucocorticoids, intravenous "
    "antibiotics and nebulised adrenaline is appropriate, with the airway monitored in case it "
    "obstructs."],
   ["Immediate tracheostomy",
    "Tracheostomy is for an airway that has obstructed or is about to. Performing it in an adult who "
    "is not drooling and has no stridor imposes a major intervention ahead of need."],
   ["Discharge on oral antibiotics",
    "The slower adult course does not make discharge safe. The disease carries high mortality when "
    "unrecognised, and deterioration can be rapid once it begins."],
   ["Lateral neck X-ray before treatment",
    "The thumbprint sign is not necessary for diagnosis, which laryngoscopy has already made, and "
    "ordering a film now delays treatment."]], C(66)),

Q("Vocal cord papillomatosis", IO,
  "A 4-year-old with recurrent respiratory papillomatosis is deteriorating, and tracheostomy is "
  "suggested.",
  [["Avoid tracheostomy",
    "Correct. Papillomas favour squamociliary junctions, the boundaries where ciliated respiratory "
    "epithelium meets squamous epithelium. A tracheostomy creates a new one, giving the disease a "
    "fresh site to seed and spreading it distally into the trachea, which is why it is specifically "
    "avoided."],
   ["Proceed with tracheostomy",
    "Airway protection matters, but this intervention worsens the underlying disease in a way few "
    "others do. Repeated debulking is preferred precisely to avoid creating that junction."],
   ["Give systemic antivirals to cure the virus",
    "There is no curative treatment for human papillomavirus. Management removes symptomatic lesions "
    "with minimal morbidity using laser, cold steel or a microdebrider."],
   ["Give intralesional cidofovir first line",
    "Cidofovir is an off-label adjuvant with no established evidence of efficacy, and it does not "
    "replace surgical removal of obstructing lesions."]], C(52)),

Q("Chronic laryngitis", IO,
  "A 58-year-old smoker has been hoarse for seven weeks with no pain and no other symptoms.",
  [["Refer for laryngoscopy",
    "Correct. Voice disturbance beyond two weeks is chronic laryngitis, which is not a true "
    "diagnosis but a description obliging a search for the cause. Laryngeal cancer and vocal cord "
    "polyps must be excluded, particularly in a smoker, so the stated step is referral for "
    "laryngoscopy."],
   ["Trial a proton pump inhibitor",
    "Reflux contributes to chronic laryngeal irritation and may be part of the picture, but treating "
    "empirically for seven weeks in a smoker without visualising the cords risks missing a "
    "carcinoma."],
   ["Voice rest and reassurance",
    "Voice rest suits ACUTE laryngitis, which settles about a week after an upper respiratory "
    "infection. Applying it past two weeks is the error the rule exists to prevent."],
   ["A course of antibiotics",
    "Antibiotics are not indicated even in acute laryngitis unless bacterial superinfection is "
    "suspected, and have no role in chronic painless hoarseness."]], C(58)),

Q("Malocclusion", IO,
  "A 15-year-old is referred with an abnormal bite. The clinician classifies the occlusion.",
  [["Class I normal, Class II distal, Class III mesial",
    "Correct. The classes describe how the lower dental arch sits relative to the upper: Class I is "
    "normal alignment, Class II is distal occlusion with the lower arch set back, and Class III is "
    "mesial occlusion with it forward. Consistent naming is what allows the problem to be "
    "communicated to an orthodontist."],
   ["Class I mesial, Class II normal, Class III distal",
    "This reassigns all three labels. Class I is the reference normal, and building from the wrong "
    "baseline makes every subsequent description wrong."],
   ["The classes describe crowding",
    "Crowding contributes to impaction and is a separate problem. The classification describes how "
    "the arches meet, which is why it is illustrated with profile views."],
   ["The classes describe missing teeth",
    "Lost teeth are one cause of malocclusion, alongside jaw-tooth size mismatch, thumb sucking and "
    "birth defects, but the classes describe the resulting bite."]], C(126)),

Q("Diphtheria prevention", IO,
  "A pregnant woman at 30 weeks asks about vaccination.",
  [["Tdap now, between 27 and 36 weeks",
    "Correct. Tdap is recommended in each pregnancy between 27 and 36 weeks. Vaccinating in that "
    "window maximises transplacental antibody transfer, protecting the newborn during the months "
    "before the infant's own schedule takes effect."],
   ["Only before the first pregnancy",
    "A single lifetime dose does not maintain the high maternal antibody levels needed for transfer, "
    "which is why the recommendation repeats with each pregnancy."],
   ["In the first trimester",
    "Vaccinating too early means antibody levels have fallen by delivery, so less is transferred at "
    "the point it matters."],
   ["Immediately after delivery",
    "Postpartum vaccination protects the mother and reduces transmission, but it misses the "
    "transplacental transfer entirely."]], C(114)),

Q("Oral leukoedema", IO,
  "A 44-year-old man has a diffuse greyish-white change of both buccal mucosae. Stretching the "
  "mucosa makes it disappear.",
  [["Leukoedema",
    "Correct. Leukoedema is a normal variant caused by fluid accumulating within epithelial cells, "
    "and stretching disperses it so the change vanishes. That single manoeuvre separates a "
    "reassurance from the biopsy that leukoplakia would need."],
   ["Leukoplakia",
    "Leukoplakia cannot be scraped off OR stretched away, and it is premalignant with 5 to 20 per "
    "cent progressing to squamous carcinoma. Missing the distinction would mean an unnecessary "
    "biopsy or a missed cancer."],
   ["Oral candidiasis",
    "Candidiasis forms removable patches that wipe off with a tongue depressor, leaving an "
    "erythematous base, and it is painful."],
   ["Oral lichen planus",
    "Lichen planus gives lacy white Wickham striae that are part of the mucosa and neither wipe nor "
    "stretch away, and it carries a small malignant risk."]], C(9)),

Q("Fordyce granules", IO,
  "A 32-year-old woman notices small yellow-white papules on her upper lip vermilion and inside her "
  "cheek. They are painless and she is otherwise well.",
  [["Fordyce granules",
    "Correct. These are ectopic sebaceous glands appearing where sebaceous glands are not usually "
    "expected, and they are a normal variant. Patients often find them alarming because they notice "
    "them suddenly, but they have always been there and need only recognition and reassurance."],
   ["Oral candidiasis",
    "Thrush gives creamy white curd-like patches on an erythematous base that wipe off, and it is "
    "painful rather than asymptomatic."],
   ["Leukoplakia",
    "Leukoplakia is a white plaque that cannot be scraped off, carrying a 5 to 20 per cent risk of "
    "malignant transformation. Discrete yellow papules are a different appearance entirely."],
   ["Herpes labialis",
    "Recurrent herpes gives grouped painful vesicles at the vermilion border, preceded by a burning "
    "prodrome, that ulcerate and crust over days."]], C(10)),

Q("Systemic lupus", IO,
  "A 34-year-old woman has painless oral erosions with surrounding erythema and honeycomb patches "
  "on the buccal mucosa. She has photosensitivity and joint pains.",
  [["Oral involvement of systemic lupus",
    "Correct. About 40 per cent of lupus patients have mucous membrane involvement, and oral lesions "
    "may be the FIRST sign of the disease. Lesions include cheilitis, erythematous patches, "
    "honeycomb patches and discoid ulcers, and there is no correlation with systemic activity."],
   ["Aphthous stomatitis",
    "Aphthae are notably painful with yellow-grey centres and red halos on freely moving "
    "non-keratinised mucosa, and they carry no systemic features."],
   ["Behcet syndrome",
    "Behcet gives painful oral ulcers in up to 100 per cent with genital ulcers in about 75 per "
    "cent, and it is the genital and ocular involvement that defines it rather than "
    "photosensitivity."],
   ["Oral lichen planus",
    "Lichen planus produces lacy Wickham striae and, in erosive forms, painful ulcers. Honeycomb "
    "patches with photosensitivity point elsewhere."]], C(23)),

Q("Cervical adenitis", IO,
  "A clinician is describing a cervical node and notes it is immobile and non-tender.",
  [["Features suggesting malignancy",
    "Correct. The descriptors that matter are size, shape, mobility, consistency and tenderness. "
    "Immobility suggests fixation to surrounding structures by tumour, and non-tenderness points "
    "away from inflammation, which hurts. Persistence or continued enlargement is what triggers fine "
    "needle aspiration."],
   ["Features suggesting inflammation",
    "Inflammatory nodes are tender and usually mobile, because inflammation is painful and does not "
    "fix a node to its surroundings."],
   ["Features suggesting a cyst",
    "A cyst would be fluctuant and often mobile rather than firm and fixed. Consistency is the "
    "discriminator."],
   ["Features suggesting a vascular lesion",
    "Vascular masses are identified by pulsation or a bruit, and nothing about firmness and "
    "immobility suggests arterial flow."]], C(93)),

Q("Parotitis", IO,
  "A 7-year-old unimmunised boy has bilateral painful parotid swelling with fever and malaise.",
  [["Mumps",
    "Correct. Mumps is caused by a paramyxovirus and is the classic viral cause of parotitis, "
    "typically bilateral with systemic symptoms in an unimmunised child. Other causes of parotitis "
    "include herpes and Epstein-Barr virus, bacterial infection, diabetes, tumours, stones and "
    "dental problems."],
   ["Acute suppurative sialadenitis",
    "Bacterial parotitis is usually unilateral, occurs in dehydrated post-operative or elderly "
    "patients, and produces pus expressible from Stensen duct."],
   ["Sialolithiasis",
    "A stone gives unilateral swelling and pain timed to meals, and 80 to 90 per cent of stones are "
    "submandibular rather than parotid."],
   ["Salivary gland neoplasm",
    "A tumour presents as a slow-growing painless mass, usually unilateral at the parotid tail, "
    "without fever or systemic symptoms."]], C(44)),

Q("Oral cancer risk", IO,
  "A 55-year-old man who chews betel nut and smokes asks about his risk of oral cancer.",
  [["Both are recognised risk factors",
    "Correct. The risk factors are tobacco chewed and smoked, alcohol, betel nut chewing, poor oral "
    "hygiene and immunosuppression. Squamous cell carcinoma is the commonest malignancy of the oral "
    "cavity and oropharynx, and prevention rests on tobacco and alcohol cessation."],
   ["Only smoking matters; betel nut is harmless",
    "Betel nut chewing appears explicitly on the risk list, and dismissing it would miss a "
    "modifiable exposure that is common in some populations."],
   ["Neither is a risk factor for oral cancer",
    "Tobacco is among the strongest risk factors for oral squamous carcinoma, so this is simply "
    "inaccurate and would remove the basis for advice."],
   ["Only alcohol matters",
    "Alcohol is a major factor and acts synergistically with tobacco, but it is not the only one on "
    "the list."]], C(145)),

Q("Cervical adenitis management", IO,
  "A 9-year-old has cervical adenitis with a fluctuant area that has not settled on antibiotics.",
  [["Incision and drainage",
    "Correct. Management is directed at the underlying cause, and where an abscess has formed "
    "drainage is required. Antibiotics penetrate an established collection poorly, so fluctuance "
    "that persists through treatment is the signal to drain rather than to escalate the drug."],
   ["A longer antibiotic course",
    "Extending a course that has already failed against a collection repeats the same strategy, and "
    "the fluctuance indicates something antibiotics cannot reach."],
   ["Excisional biopsy",
    "Excisional biopsy is a diagnostic operation for a suspected neoplastic node. Here the problem "
    "is a collection needing therapeutic drainage."],
   ["Observation alone",
    "A fluctuant node that has resisted antibiotics will not resolve unaided, and waiting risks "
    "spread into the deep neck spaces."]], C(94)),

Q("Gum disease consequences", IO,
  "A 60-year-old man with untreated periodontal disease asks whether it affects anything beyond his "
  "mouth.",
  [["It raises the risk of endocarditis and other systemic disease",
    "Correct. Periodontal disease is linked to heart disease and stroke through endocarditis risk, "
    "to respiratory disease through pneumonia, to osteoporosis through decreased bone density, and "
    "in men to kidney, pancreatic and blood cancers. It is also, with caries, a primary cause of "
    "tooth loss."],
   ["It affects only the teeth and gums",
    "Confining it to the mouth misses the systemic associations that are the reason gum disease is "
    "treated as a general health issue rather than a purely dental one."],
   ["It causes hearing loss",
    "There is no association between periodontal disease and hearing. Ear symptoms of this kind "
    "belong to temporomandibular joint disorders."],
   ["It only matters during pregnancy",
    "Pregnancy is one of the risk factors for gingival disease through hormonal fluctuation, but the "
    "consequences listed are not confined to it."]], C(119)),

Q("Tooth decay", IO,
  "A 38-year-old woman has severe toothache. The clinician explains what caused the pulpitis.",
  [["Tooth decay, with injury second",
    "Correct. The commonest cause of pulpitis and periapical abscess is tooth decay, and the second "
    "commonest is injury. Mild inflammation may resolve without permanent damage, but severe "
    "inflammation kills the pulp, and a pocket of pus may then form at the root."],
   ["Injury, with decay second",
    "This reverses the order. Both are causes, but caries is by far the commoner route to pulp "
    "inflammation."],
   ["Impaction of the tooth",
    "Impaction is a separate tooth disorder, usually of wisdom teeth from overcrowding, which "
    "predisposes to infection around a partially erupted crown rather than to pulpitis."],
   ["Malocclusion",
    "Malocclusion distributes bite force unevenly, wearing and loosening teeth over time, but it is "
    "not the direct cause of pulp inflammation."]], C(124)),

Q("Deep neck infection spread", IO,
  "A student asks why a retropharyngeal abscess is so dangerous compared with a peritonsillar one.",
  [["Its space extends to the posterior mediastinum",
    "Correct. The retropharyngeal space runs from the base of the skull to the posterior "
    "mediastinum, giving infection a direct anatomical route into the chest. Mediastinitis carries "
    "50 per cent mortality, and the danger space beyond is continuous left to right."],
   ["It always involves the carotid artery",
    "Vascular involvement is a recognised complication of deep neck infection generally but is not "
    "what makes this space specifically dangerous."],
   ["It causes trismus that prevents intubation",
    "Trismus is the hallmark of a PERITONSILLAR abscess, from irritation of the medial pterygoid. It "
    "is not the retropharyngeal danger."],
   ["It always becomes Ludwig angina",
    "Ludwig angina is a separate infection of the submental, sublingual and submandibular spaces, "
    "usually odontogenic, in a different anatomical compartment."]], C(107)),

Q("Salivary gland site", IO,
  "A 61-year-old woman has a tumour of a minor salivary gland of the palate. She asks how likely it "
  "is to be benign.",
  [["Only about 35 per cent are benign",
    "Correct. The smaller the gland, the higher the malignant proportion: parotid tumours are 75 to "
    "80 per cent benign, submandibular 50 to 60 per cent, and minor salivary glands only about 35 "
    "per cent. That inverse relationship changes how aggressively a small-gland lesion is "
    "investigated."],
   ["About 80 per cent are benign",
    "Seventy-five to eighty per cent is the PAROTID figure. Applying it to a minor gland would "
    "substantially understate the risk."],
   ["Essentially all are benign",
    "That would remove the reason for prompt biopsy of a minor gland lesion, when it is the group "
    "most likely to be malignant."],
   ["The site makes no difference",
    "Site is one of the most useful pieces of information available before any test, since the "
    "benign proportion differs more than twofold between parotid and minor glands."]], C(139)),

Q("Herpangina", IO,
  "A 6-year-old has fever and sore throat with small ulcerative vesicles over the tonsils and soft "
  "palate. He also has a cough and coryza.",
  [["Viral pharyngitis with herpangina",
    "Correct. Herpangina is ulcerative vesicles over the tonsils and is a feature of viral "
    "pharyngitis, usually coxsackievirus. The accompanying cough and coryza reinforce a viral cause, "
    "and absence of cough is a Centor point precisely because its presence argues against "
    "streptococcus."],
   ["Streptococcal pharyngitis",
    "Streptococcal disease gives tonsillar and pharyngeal erythema with purulent exudate, fever, "
    "tender nodes and characteristically NO cough. Vesicles are not part of it."],
   ["Diphtheria",
    "Diphtheria produces a tenacious adherent grey membrane over tonsils and pharynx that bleeds "
    "when disturbed, in an unimmunised child, rather than discrete vesicles."],
   ["Oral candidiasis",
    "Thrush gives creamy white patches that wipe off leaving an erythematous base, not ulcerative "
    "vesicles with fever and coryza."]], C(72)),

Q("Salivary stone management", IO,
  "A 44-year-old man has a stone palpable in the anterior portion of the submandibular duct.",
  [["Intraoral extraction",
    "Correct. Management depends on the location and size of the stone. One that can be palpated or "
    "visualised in the anterior portion of the submandibular duct can be extracted intraorally, "
    "whereas larger stones in the hilum or body of the gland require excision of the gland itself."],
   ["Excision of the submandibular gland",
    "Gland excision is reserved for larger stones in the hilum or body. Removing a gland for a stone "
    "reachable through the mouth is disproportionate."],
   ["Lithotripsy under interventional radiology",
    "Lithotripsy is one of the options for stones that cannot be reached directly, but it is not "
    "needed when the stone is palpable anteriorly."],
   ["Conservative management only",
    "Hydration, hot compresses, massage, analgesia and lozenges help symptomatically and can pass "
    "small stones, but a palpable anterior stone can simply be removed."]], C(43)),

Q("Sialoendoscopy", IO,
  "A 50-year-old woman has recurrent submandibular stones and wants to avoid losing the gland.",
  [["Sialoendoscopy",
    "Correct. Sialoendoscopy is the most recent minimally invasive option and is specifically "
    "described as able to avoid removal of a gland. It can be combined with open sialolithotomy "
    "where needed, which makes it the right answer for a patient whose priority is preserving the "
    "gland."],
   ["Gland excision",
    "Excision is definitive but removes the gland, which is precisely what she is trying to avoid, "
    "and it is reserved for larger stones in the hilum or body."],
   ["Intraoral extraction",
    "Intraoral extraction works when the stone is palpable or visible in the anterior duct. It is "
    "not a general solution for recurrent stones."],
   ["Conservative management indefinitely",
    "Hydration, compresses and massage manage symptoms but do not remove recurrent stones, so the "
    "colic continues."]], C(43)),

Q("Retropharyngeal abscess in adults", IO,
  "A 46-year-old man develops fever, sore throat and neck stiffness a week after swallowing a "
  "fishbone.",
  [["Retropharyngeal abscess",
    "Correct. In adults the abscess usually follows intraoral procedures, trauma, a foreign body "
    "such as a fishbone, immunocompromise or extension from an odontogenic infection, rather than "
    "the nodal suppuration seen in children under five. It remains a surgical emergency."],
   ["Peritonsillar abscess",
    "A peritonsillar abscess gives trismus, uvular deviation and a hot potato voice, and follows "
    "untreated tonsillitis rather than a swallowed foreign body."],
   ["Ludwig angina",
    "Ludwig angina involves the floor of the mouth and submandibular spaces, usually from a dental "
    "source, displacing the tongue upward and backward."],
   ["Acute epiglottitis",
    "Epiglottitis produces severe odynophagia with a muffled voice and, in children, the four Ds and "
    "tripod position, without neck stiffness or a foreign body history."]], C(103)),

Q("Oral cancer presentation", IO,
  "A 66-year-old woman with dentures complains they no longer fit, and she has vague discomfort in "
  "the mouth and a foreign body sensation in the throat.",
  [["Possible oral or oropharyngeal malignancy",
    "Correct. Ill-fitting dentures are on the list of presenting features alongside non-healing "
    "ulcers, bleeding, pain, vague discomfort and a foreign body sensation in the throat. Advanced "
    "disease adds dysarthria, dysphagia, a neck mass and referred otalgia, so an apparently minor "
    "complaint deserves a proper look."],
   ["Normal denture wear requiring adjustment",
    "Dentures do need adjusting over time, which is what makes this presentation so easy to dismiss. "
    "Combined with discomfort and a throat sensation in this age group it warrants examination."],
   ["Temporomandibular joint disorder",
    "Temporomandibular disorders give jaw pain with clicking and limited opening, plus referred ear "
    "symptoms, rather than a changing denture fit."],
   ["Oral candidiasis",
    "Denture wear is a risk factor for thrush, so it is worth looking for, but candidiasis produces "
    "removable white patches rather than a change in denture fit."]], C(146)),

Q("Oral cancer investigation", IO,
  "A 63-year-old man with a suspicious oral lesion is being worked up.",
  [["Biopsy, with imaging and dental evaluation",
    "Correct. The workup includes labs with high-risk human papillomavirus testing and in situ "
    "hybridisation, computed tomography or magnetic resonance for the primary and nodes, chest X-ray "
    "and positron emission tomography for metastases, flexible fiberoptic endoscopy, biopsy and "
    "dental evaluation before treatment."],
   ["Biopsy alone",
    "Tissue establishes the diagnosis but does not stage the disease, and staging determines whether "
    "surgery alone or surgery with radiotherapy is appropriate."],
   ["Imaging alone without tissue",
    "Imaging cannot give a histological diagnosis, and treatment decisions depend on knowing the "
    "cell type and the human papillomavirus status."],
   ["Serology alone",
    "High-risk human papillomavirus testing is part of the labs, but no blood test diagnoses an oral "
    "carcinoma."]], C(147)),

Q("Tonsillitis versus pharyngitis", IO,
  "A 15-year-old has inflammation of both the tonsils and the throat.",
  [["Pharyngotonsillitis",
    "Correct. The three terms describe which structure is inflamed: tonsillitis if the tonsils, "
    "pharyngitis if the throat, and pharyngotonsillitis if both. They are not three different "
    "diseases, and the same organisms cause all of them, but tonsillar involvement raises the "
    "possibility of complications such as peritonsillar abscess."],
   ["Tonsillitis only",
    "Tonsillitis describes involvement of the tonsils alone, and using it here omits the pharyngeal "
    "component that is also described."],
   ["Pharyngitis only",
    "Pharyngitis describes the throat alone, and using it omits the tonsillar involvement, which is "
    "the part that carries the abscess risk."],
   ["Laryngitis",
    "Laryngitis affects the larynx and produces hoarseness, which is a different structure and a "
    "different symptom."]], C(69)),
]
