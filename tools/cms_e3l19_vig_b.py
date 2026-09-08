# -*- coding: utf-8 -*-
"""Lecture 19 vignette pool B -- Oral Cavity, Salivary Glands and Neck."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Disorders of the oral cavity, salivary glands, and neck: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")
C = lambda n: "CMS I Disorders of the Oral Cavity, Salivary Glands, Slide %d" % n

QUESTIONS = [

Q("Bacterial pharyngitis", IO,
  "An 11-year-old has two days of sore throat with a temperature of 101 degrees, tonsillar exudate "
  "and tender anterior cervical nodes. She has no cough. The rapid antigen test is negative.",
  [["Send a throat culture before deciding",
    "Correct. Her Centor score is high, with a point each for absent cough, exudate, fever and "
    "tender nodes, plus one for her age. Rapid antigen tests are specific but insufficiently "
    "sensitive, so a negative result in a child with high clinical probability is always confirmed "
    "by culture."],
   ["Accept the negative test and treat symptomatically",
    "Accepting it at face value in a high-probability patient is exactly the error confirmatory "
    "culture exists to prevent, and missing streptococcal infection leaves the rheumatic fever risk "
    "unaddressed."],
   ["Start penicillin without further testing",
    "Empiric treatment is defensible at the highest scores, but with a negative rapid test in hand "
    "the culture settles it within a day or two and avoids treating a viral illness."],
   ["Order antistreptolysin O titres today",
    "Antistreptolysin O is the definitive test but reflects an antibody response that takes time to "
    "rise, so it establishes past infection rather than guiding acute treatment."]], C(74)),

Q("Viral pharyngitis", IO,
  "A 22-year-old has a sore throat with cough, hoarseness, rhinitis and conjunctivitis for three "
  "days. She is afebrile with no tonsillar exudate.",
  [["Supportive care with no further testing",
    "Correct. Cough, rhinitis, hoarseness and conjunctivitis all point to viral pharyngitis, which "
    "accounts for about 70 per cent of cases. Her Centor score is minimal, so testing and "
    "antibiotics are not indicated, and management is hydration, antipyretics and analgesia."],
   ["Rapid antigen test and treat if positive",
    "Testing is reserved for intermediate Centor scores. With cough and coryza and no fever or "
    "exudate, the probability is low enough that a positive result would more likely represent "
    "carriage."],
   ["Empiric penicillin for 10 days",
    "Treating this pattern with antibiotics is precisely the over-prescription the scoring system "
    "exists to reduce, and it exposes her to side effects for no benefit."],
   ["Throat culture and admit for observation",
    "Admission is disproportionate for an afebrile young adult with a self-limiting viral illness, "
    "and culture would not change management here."]], C(72)),

Q("Rheumatic fever", IO,
  "A 9-year-old develops migratory joint pains and a new cardiac murmur three weeks after an "
  "untreated sore throat.",
  [["Rheumatic fever from cross-reactive antibodies",
    "Correct. Antibodies produced against the streptococcus cross-react with heart muscle, causing "
    "endocarditis, myocarditis or pericarditis. Signs appear 2 to 3 weeks after the infection, "
    "occasionally as early as one or as late as five, with peak incidence between 5 and 15 years."],
   ["Infective endocarditis from bacterial seeding",
    "Direct bacterial seeding of valves is a different disease with a different tempo and usually "
    "follows bacteraemia rather than a pharyngitis three weeks earlier."],
   ["Juvenile idiopathic arthritis",
    "Migratory arthritis with a new murmur following a documented sore throat has a much more "
    "specific explanation, and the temporal link is the diagnostic clue."],
   ["Scarlet fever",
    "Scarlet fever is the toxin-mediated rash accompanying streptococcal pharyngitis at the time of "
    "infection rather than a cardiac sequela weeks later."]], C(78)),

Q("Chronic pharyngitis", IO,
  "A 52-year-old smoker has constant throat clearing, a dry throat and odynophagia. Examination "
  "shows a thickened, granular posterior pharyngeal wall with crusting.",
  [["Chronic pharyngitis, and address the underlying cause",
    "Correct. Causes include postnasal drip from chronic rhinosinusitis, irritants such as dust, dry "
    "heat, chemicals, smoking and alcohol, chronic mouth breathing, voice abuse, allergy, "
    "granulomatous disease, connective tissue disorder and malignancy. Management addresses the "
    "underlying disorder and avoids precipitants, with culture and biopsy if therapy fails."],
   ["Acute bacterial pharyngitis needing penicillin",
    "Acute streptococcal disease presents over days with fever, exudate and tender nodes, not with "
    "months of throat clearing and a granular wall."],
   ["Laryngopharyngeal reflux alone, needing no examination",
    "Reflux is one of the irritant causes and may well contribute, but malignancy is on the same "
    "list, so failed therapy earns a biopsy rather than an assumption."],
   ["Infectious mononucleosis",
    "Mononucleosis gives fever, tonsillar pharyngitis and cervical adenopathy in a younger patient "
    "over weeks, not chronic crusting in a middle-aged smoker."]], C(80)),

Q("Cervical adenitis", IO,
  "A 6-year-old has a unilateral, solitary, tender anterior cervical node following a sore throat.",
  [["Beta-haemolytic streptococcus, in about 70 per cent",
    "Correct. Local ear, nose and throat infections drain to regional nodes, and about 70 per cent of "
    "these unilateral solitary anterior nodes relate to beta-haemolytic streptococcal infection, "
    "with 20 per cent staphylococcal including MRSA and 10 per cent viral, atypical mycobacterial or "
    "Bartonella."],
   ["Staphylococcus aureus, in the majority",
    "Staphylococcus is second at about 20 per cent, which matters for antibiotic choice because it "
    "includes MRSA, but it is not the majority."],
   ["Bartonella henselae",
    "Cat scratch disease sits in the residual 10 per cent and requires cat contact with preauricular "
    "or submandibular involvement."],
   ["Mycobacterium tuberculosis",
    "Tuberculous adenitis affects adults more than children and gives diffuse bilateral "
    "lymphadenopathy rather than a single tender node after a sore throat."]], C(92)),

Q("Dental abscess", IO,
  "A 42-year-old man has a dental abscess. The tooth is badly broken down and cannot be restored.",
  [["Extraction with curettage of the apical tissue",
    "Correct. Management depends on whether the tooth can be saved: a restorable tooth gets a root "
    "canal, and one that cannot be restored is extracted, with the apical tissue curetted because "
    "leaving infected granulation tissue allows the infection to persist in the socket."],
   ["Root canal treatment",
    "A root canal is correct for a restorable tooth, which is what makes it tempting, but it cannot "
    "succeed where there is nothing to rebuild around the treated root."],
   ["Antibiotics alone until it settles",
    "Antibiotics are part of treatment but never definitive, because the source is a collection and "
    "a necrotic pulp. Relying on them alone leads to recurrence and, at worst, deep neck spread."],
   ["Incision and drainage alone",
    "Drainage relieves pressure and is often needed acutely, but leaving the causative tooth means "
    "the abscess reforms."]], C(117)),

Q("Gingivitis", IO,
  "A 35-year-old man has gums that are red, swollen and bleed when he brushes, with little "
  "discomfort. There is no pocketing or tooth mobility.",
  [["Gingivitis, reversible with cleaning and home care",
    "Correct. Gingivitis is the mildest form of periodontal disease: inflammation confined to the "
    "gingiva from plaque at the gum line, giving erythema, oedema and bleeding with little "
    "discomfort. The critical point is that it is fully reversible at this stage, before the "
    "periodontal ligament and bone are destroyed."],
   ["Periodontitis with irreversible bone loss",
    "Periodontitis is what untreated gingivitis becomes: plaque spreads below the gum line, pockets "
    "form, and ligament and bone are destroyed so teeth loosen. Absence of pocketing and mobility "
    "means that has not yet happened."],
   ["A dental abscess",
    "An abscess is a localised collection of pus around a root or in a periodontal pocket, causing "
    "significant pain and swelling rather than generalised painless bleeding."],
   ["Oral lichen planus",
    "Lichen planus can affect the gingiva as a desquamative gingivitis, so it is worth considering, "
    "but it produces lacy white striae or erosions rather than plaque-related bleeding."]], C(121)),

Q("Tooth disorders", IO,
  "A 31-year-old man has a painful lower wisdom tooth that has only partly erupted, with inflamed "
  "gum overlying it.",
  [["Impaction, which predisposes to infection",
    "Correct. Impaction usually results from overcrowding with insufficient room to erupt, and "
    "wisdom teeth are the usual culprits because they come through last. A partially erupted tooth "
    "leaves a gum flap that traps debris, which is why impacted teeth become infected and are "
    "usually removed."],
   ["Dental caries of the wisdom tooth",
    "Caries can certainly affect a partially erupted tooth that is hard to clean, so it may coexist, "
    "but the underlying problem described is the failure to erupt and the flap over it."],
   ["Malocclusion",
    "Malocclusion describes how the arches meet and can coexist with crowding, but it does not "
    "explain a single partially erupted tooth with inflamed overlying gum."],
   ["Pulpitis",
    "Pulpitis is inflammation of the pulp from decay or injury, giving pain within the tooth rather "
    "than in the gum flap over an unerupted crown."]], C(125)),

Q("TMJ disorder", IO,
  "A 36-year-old woman has facial pain, jaw clicking and difficulty opening her mouth wide. She "
  "also reports tinnitus, ear fullness and dizziness. Otoscopy and audiometry are normal.",
  [["Temporomandibular joint disorder",
    "Correct. The joint sits immediately anterior to the ear canal, so its disorders commonly refer "
    "symptoms to the ear with a completely normal ear examination. Jaw pain with clicking and "
    "limited opening in a woman of childbearing age is typical, and it is the second commonest "
    "musculoskeletal cause of pain and disability."],
   ["Meniere disease",
    "Meniere produces episodic vertigo lasting hours with documented fluctuating low-frequency loss "
    "and tinnitus. Normal audiometry argues against it, and it causes no jaw symptoms."],
   ["Eustachian tube dysfunction",
    "Eustachian tube dysfunction gives fullness and popping with a retracted drum and often an "
    "abnormal tympanogram. Her otoscopy is normal and it does not explain the jaw findings."],
   ["Acoustic neuroma",
    "A schwannoma causes progressive unilateral sensorineural loss with poor speech discrimination. "
    "Normal audiometry argues strongly against it."]], C(130)),

Q("Oral cancer", IO,
  "A 62-year-old man who smokes and drinks has an ulcer on the floor of the mouth that has not "
  "healed in six weeks. He reports right ear pain, and his ear examination is normal.",
  [["Oral cavity squamous cell carcinoma",
    "Correct. A non-healing ulcer in a patient with tobacco and alcohol exposure is the classic "
    "presentation, and squamous cell carcinoma is the commonest oral malignancy. The referred "
    "otalgia with a normal ear reflects shared innervation between the oral cavity and the ear, and "
    "indicates more advanced disease."],
   ["Aphthous ulceration",
    "Aphthae are painful, occur on freely moving non-keratinised mucosa, and heal within 7 to 10 "
    "days in the minor form. Six weeks without healing excludes them."],
   ["Oral candidiasis",
    "Thrush produces creamy white patches that wipe off leaving an erythematous base, rather than a "
    "persistent ulcer, and it does not refer pain to the ear."],
   ["Traumatic ulcer from a denture",
    "A traumatic ulcer resolves once the irritant is removed, so persistence for six weeks in a "
    "high-risk patient is exactly what should not be attributed to trauma."]], C(146)),

Q("Oral cancer", IO,
  "A 59-year-old man has a tonsillar squamous cell carcinoma that is human papillomavirus positive.",
  [["Surgical resection with radiotherapy",
    "Correct. Oropharyngeal tumours are treated with resection plus radiotherapy, which gives better "
    "functional outcomes in a site where speech and swallowing are at stake. Between 60 and 80 per "
    "cent of oropharyngeal cancers are human papillomavirus related, which also affects prognosis."],
   ["Surgical resection alone",
    "Resection alone is the stated approach for ORAL CAVITY cancer. Applying it to an oropharyngeal "
    "primary omits the radiotherapy the site-specific evidence supports."],
   ["Chemotherapy alone",
    "Chemotherapy has a role in advanced or palliative settings but is not the primary modality for "
    "a resectable head and neck squamous carcinoma."],
   ["Observation, since virus-related tumours regress",
    "Human papillomavirus positive tumours have a better prognosis with treatment, which is a real "
    "and important difference, but they do not regress on their own."]], C(148)),

Q("Salivary neoplasm", IO,
  "A 60-year-old man has a slowly enlarging painless mass at the tail of the parotid, with no "
  "facial weakness.",
  [["A benign parotid tumour",
    "Correct. Between 64 and 80 per cent of salivary neoplasms arise in the parotid and 75 to 80 per "
    "cent of those are benign, most commonly epithelial. Benign parotid tumours characteristically "
    "present as slow-growing painless masses at the tail of the gland, and the absence of facial "
    "nerve involvement supports it."],
   ["A malignant parotid tumour",
    "Mucoepidermoid carcinoma is the commonest salivary malignancy, so it belongs on the "
    "differential, but malignancy is suggested by pain, facial nerve involvement, rapid growth or "
    "skin invasion, none of which is present."],
   ["A minor salivary gland tumour",
    "Minor gland tumours occur in buccal, labial and palatal mucosa rather than at the parotid tail, "
    "and only about 35 per cent of them are benign."],
   ["A parotid abscess",
    "An abscess is acutely painful with fever, erythema and often pus from Stensen duct, developing "
    "over days rather than as slow painless enlargement."]], C(141)),

Q("Salivary neoplasm", IO,
  "A 57-year-old woman has a parotid mass with pain and a partial facial nerve palsy on the same "
  "side.",
  [["A malignant salivary tumour, with a poor prognosis",
    "Correct. Prognosis is poor when there is pain, facial or other nerve involvement, high-grade "
    "histology, skin or tissue invasion, or recurrent disease. Facial nerve palsy in particular "
    "indicates invasion rather than compression, and management is surgical removal with "
    "radiotherapy for certain stages."],
   ["A benign pleomorphic adenoma",
    "Benign tumours are slow-growing and painless and do not invade the facial nerve. Pain and palsy "
    "are what shift the assessment."],
   ["Acute suppurative sialadenitis",
    "Infection gives a firm diffusely tender gland with erythema, fever and pus from the duct over "
    "days, and it does not paralyse the facial nerve."],
   ["Sialolithiasis",
    "A stone gives swelling and pain timed to meals with relief between them, and has no effect on "
    "the facial nerve."]], C(143)),

Q("Diphtheria", IO,
  "A 9-year-old recently arrived from a region with low immunisation coverage has a mild sore "
  "throat, low fever and marked malaise. A tenacious grey membrane covers the tonsils and pharynx "
  "and bleeds when disturbed.",
  [["Antitoxin from the Centers for Disease Control plus antibiotics",
    "Correct. An adherent grey membrane in an unimmunised child is diphtheria. The damage is caused "
    "by an exotoxin producing myocarditis and cranial neuropathy, so antitoxin is required to "
    "neutralise circulating toxin, alongside penicillin or erythromycin for 14 days and isolation "
    "until three consecutive cultures are negative."],
   ["Penicillin alone for 10 days",
    "Antibiotics eradicate the organism but do nothing about toxin already circulating, and it is "
    "the toxin that kills."],
   ["Supportive care for presumed viral pharyngitis",
    "Viral pharyngitis does not produce an adherent membrane that bleeds on removal, and treating "
    "this as viral misses a notifiable disease with a specific antidote."],
   ["Corticosteroids to reduce swelling",
    "Steroids may be used adjunctively for airway compromise but neither neutralise toxin nor "
    "eliminate the organism."]], C(113)),

Q("Aphthous stomatitis", IO,
  "A 20-year-old student has recurrent painful oral ulcers with yellow-grey centres and red halos, "
  "each under a centimetre, on the inner cheek and lip. They heal in about a week and recur during "
  "examinations.",
  [["Minor aphthous ulceration",
    "Correct. Minor aphthae are under a centimetre, are the commonest form, burn and tingle before "
    "appearing, and heal in 7 to 10 days without scarring. Their location on freely moving "
    "non-keratinised mucosa is diagnostic, and stress is a recognised precipitant."],
   ["Major aphthous ulceration",
    "Major aphthae exceed a centimetre, are more painful, often multiple, carry a scarring risk and "
    "last over a month. Size and healing time place these in the minor category."],
   ["Herpetic gingivostomatitis",
    "Primary herpes affects KERATINISED surfaces such as hard palate and attached gingiva, with "
    "fever and cervical lymphadenopathy, and is a single primary illness rather than a recurrent "
    "stress-related pattern."],
   ["Herpetiform aphthous ulceration",
    "The herpetiform variant produces numerous 1 to 3 millimetre ulcers, scars, and lasts over a "
    "month, despite the name having nothing to do with herpes."]], C(16)),

Q("Herpes simplex", IO,
  "A 28-year-old woman has recurrent painful lesions at the vermilion border of the lip, always "
  "preceded by a day of burning and tingling, triggered by sunlight and stress.",
  [["Reactivation of virus latent in the trigeminal ganglion",
    "Correct. After primary infection the virus travels along the axon to the trigeminal ganglion "
    "and persists. Reactivation follows stress, trauma, immunosuppression or ultraviolet light, and "
    "the virus migrates back down the axonal sheath, which is why burning and tingling precede any "
    "visible lesion by about 24 hours."],
   ["A new primary infection each time",
    "Primary infection occurs once, most often as herpetic gingivostomatitis in a seronegative child "
    "or young adult with fever and lymphadenopathy. Repeated identical lesions at one site are "
    "reactivation."],
   ["An autoimmune photosensitive reaction",
    "Photosensitive autoimmune disease exists but does not produce a 24-hour neurological prodrome, "
    "which is characteristic of a virus travelling along a nerve."],
   ["Bacterial superinfection of chapped lips",
    "Angular cheilitis and impetigo affect the perioral region but have no prodrome, do not recur at "
    "exactly the same site with these triggers, and look different from grouped vesicles."]],
  C(26)),
]
