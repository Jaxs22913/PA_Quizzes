# -*- coding: utf-8 -*-
"""Lecture 19 vignette pool A -- Oral Cavity, Salivary Glands and Neck."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Disorders of the oral cavity, salivary glands, and neck: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")
C = lambda n: "CMS I Disorders of the Oral Cavity, Salivary Glands, Slide %d" % n

QUESTIONS = [

Q("Peritonsillar abscess", IO,
  "A 16-year-old treated with penicillin for pharyngitis four days ago returns unable to drink, "
  "with excruciating pain on swallowing and a muffled voice. The soft palate is deviated medially "
  "on the right with marked tonsillar swelling.",
  [["Peritonsillar abscess",
    "Correct. Pus between the tonsillar capsule and the pharyngeal muscles displaces the soft palate "
    "and tonsil medially, and the muffled hot potato voice comes from the mass distorting the "
    "oropharynx. It is the commonest deep head and neck infection and typically follows inadequately "
    "treated tonsillitis."],
   ["Infectious mononucleosis",
    "Mononucleosis gives bilateral tonsillar enlargement with exudate, fever and cervical "
    "adenopathy, and would not deviate the palate to one side. Worsening after penicillin there "
    "takes the form of a rash."],
   ["Retropharyngeal abscess",
    "A retropharyngeal abscess causes neck stiffness and a widened prevertebral space, chiefly in "
    "children under five, rather than unilateral palatal deviation in an adolescent."],
   ["Ludwig angina",
    "Ludwig angina involves the floor of the mouth with the tongue displaced up and back, usually "
    "from a dental source, rather than deviating the soft palate."]], C(98)),

Q("Retropharyngeal abscess", IO,
  "A 3-year-old has two days of fever, sore throat, neck stiffness and refusal to eat, and is now "
  "drooling and leaning forward with the neck extended. Lateral neck X-ray shows widened "
  "prevertebral soft tissue.",
  [["Retropharyngeal abscess",
    "Correct. Suppuration of retropharyngeal nodes after an upper respiratory infection is a disease "
    "of children under five, and widening of the prevertebral soft tissue is the classic "
    "radiographic sign. It is a surgical emergency because the space runs to the posterior "
    "mediastinum, where mediastinitis carries 50 per cent mortality."],
   ["Epiglottitis",
    "Epiglottitis shares drooling and the forward-leaning posture, so it is the key differential, "
    "but it comes on over hours, produces a thumbprint sign rather than prevertebral widening, and "
    "does not usually cause neck stiffness."],
   ["Peritonsillar abscess",
    "A peritonsillar abscess deviates the uvula and causes trismus with a hot potato voice, in "
    "adolescents and young adults rather than toddlers."],
   ["Bacterial pharyngitis",
    "Streptococcal pharyngitis gives fever, exudate and tender nodes but not neck stiffness, "
    "drooling or an abnormal prevertebral shadow."]], C(105)),

Q("Ludwig angina", IO,
  "A 47-year-old man with poorly controlled diabetes has two days of increasing swelling under the "
  "chin and in the floor of the mouth after a dental infection. His tongue is pushed upward and "
  "backward and he is drooling.",
  [["Secure the airway, then antibiotics and drainage if threatened",
    "Correct. Ludwig angina is a rapidly spreading cellulitis of the submental, sublingual and "
    "submandibular spaces. Swelling of the floor of the mouth pushes the tongue up and back into the "
    "airway, which is why airway management comes first, with penicillin and metronidazole or "
    "ampicillin-sulbactam and external drainage through bilateral submental incisions if needed."],
   ["Oral antibiotics and dental review in the morning",
    "The dental consultation is genuinely part of management since the source is usually a tooth, "
    "but sending home a diabetic patient whose tongue is already displaced risks losing the airway "
    "overnight."],
   ["Drain the tooth abscess alone",
    "Draining the offending tooth addresses the source but not the established cellulitis compressing "
    "the airway, and both have to be dealt with."],
   ["Intravenous corticosteroids alone",
    "Steroids may be adjunctive but do not treat the infection and cannot reliably protect an airway "
    "already being displaced."]], C(110)),

Q("Epiglottitis", IO,
  "A 5-year-old has a few hours of high fever, drooling, refusal to swallow and a muffled voice. He "
  "sits leaning forward with his chin thrust out, looking anxious.",
  [["Do not examine the throat; secure the airway with the team",
    "Correct. The four Ds and the tripod position describe supraglottitis, and once suspected, "
    "examinations that raise the child's anxiety, including intraoral examination and venipuncture, "
    "can precipitate complete obstruction. The priority is a controlled airway in theatre with "
    "anaesthetic and surgical teams present."],
   ["Examine the pharynx with a tongue depressor",
    "This is the specific action to avoid. Depressing the tongue in a child with an inflamed "
    "supraglottis can trigger laryngospasm, and the diagnosis does not depend on seeing the "
    "epiglottis in clinic."],
   ["Obtain a lateral neck radiograph first",
    "The thumbprint sign is recognised but not necessary for diagnosis, and sending an unstable "
    "child to radiology moves him away from the team who can secure the airway."],
   ["Give oral antibiotics and review tomorrow",
    "Antibiotics are part of treatment but only after the airway is safe, and oral administration "
    "requires swallowing, which this child cannot do."]], C(63)),

Q("Infectious mononucleosis", IO,
  "A 19-year-old student treated with amoxicillin for a presumed streptococcal sore throat develops "
  "a widespread maculopapular rash three days later. Her tonsils are enlarged with exudate and she "
  "has bilateral cervical adenopathy and marked fatigue.",
  [["Mononucleosis, with the rash triggered by the aminopenicillin",
    "Correct. Giving an aminopenicillin in Epstein-Barr infection reliably provokes a widespread "
    "exanthem, and this sequence is the classic route to the diagnosis. The triad of fever, "
    "tonsillar pharyngitis and cervical lymphadenopathy fits mononucleosis rather than "
    "streptococcus."],
   ["A true penicillin allergy requiring lifelong avoidance",
    "This is the consequential misreading. The rash is not immunoglobulin E mediated, so labelling "
    "her allergic removes an entire antibiotic class from her future care on the strength of a "
    "virus."],
   ["Scarlet fever from the streptococcal infection",
    "Scarlet fever gives a sandpapery erythematous rash with circumoral pallor and a strawberry "
    "tongue, beginning within a day or two of the sore throat rather than after antibiotics."],
   ["An unrelated viral exanthem",
    "Treating a textbook drug-virus interaction as coincidence discards the clue that has just made "
    "the diagnosis."]], C(87)),

Q("Sialolithiasis", IO,
  "A 46-year-old man has recurrent painful swelling under the right jaw that starts within minutes "
  "of eating and settles over the next hour. A firm structure is palpable in the floor of the "
  "mouth.",
  [["Submandibular sialolithiasis",
    "Correct. Eating stimulates salivary flow, and an obstructing stone traps that saliva, "
    "distending the gland until pressure equalises. Between 80 and 90 per cent of stones are "
    "submandibular because Wharton duct runs a long uphill course carrying alkaline mucin-rich "
    "saliva."],
   ["Acute suppurative sialadenitis",
    "Bacterial infection produces constant swelling with fever, overlying erythema and pus from the "
    "duct, typically in a dehydrated post-operative or elderly patient, and it does not fluctuate "
    "with meals."],
   ["Mumps parotitis",
    "Mumps affects the parotid rather than the submandibular gland, is usually bilateral, and comes "
    "with systemic viral symptoms rather than a palpable stone."],
   ["A parotid neoplasm",
    "A salivary tumour presents as a slow-growing painless mass, most often at the tail of the "
    "parotid, with no relationship to eating."]], C(42)),

Q("Acute suppurative sialadenitis", IO,
  "An 81-year-old woman four days after hip surgery, with poor oral intake, develops painful "
  "swelling over the angle of the jaw with overlying erythema. Pus can be expressed from the duct "
  "opposite the upper second molar.",
  [["Rehydration with antistaphylococcal antibiotics",
    "Correct. Dehydration causes salivary stasis, which lets bacteria ascend the parotid duct. "
    "Staphylococcus aureus is the commonest organism, and pus expressible from Stensen duct confirms "
    "the gland is infected. Treatment is rehydration to restore flow plus penicillinase-resistant "
    "gram-positive cover, with warm compresses, massage and sialogogues."],
   ["Antiviral therapy for mumps",
    "Mumps is a viral illness of children and young adults, usually bilateral, and does not produce "
    "purulent ductal discharge."],
   ["Immediate parotidectomy",
    "Surgery is reserved for an abscess not responding to 48 hours of conservative treatment, and "
    "even then drainage rather than gland removal. Operating acutely risks the facial nerve."],
   ["Sialography to look for a stone",
    "Sialography is avoided during acute infection because injecting contrast retrogradely into an "
    "infected gland can worsen it, and stones more often affect the submandibular gland."]],
  C(38)),

Q("Oral candidiasis", IO,
  "A 64-year-old man using an inhaled corticosteroid has white patches on the buccal mucosa and "
  "tongue. Wiping one with a tongue depressor removes it, leaving an erythematous base.",
  [["Oral candidiasis",
    "Correct. Candida forms a removable pseudomembrane, so wiping it reveals inflamed mucosa "
    "beneath. Inhaled corticosteroid deposited in the mouth suppresses local immunity, which is why "
    "patients are told to rinse afterwards, and why this is a common cause in someone otherwise "
    "well."],
   ["Oral leukoplakia",
    "Leukoplakia is defined as a white lesion that CANNOT be scraped off, and it is premalignant "
    "with 5 to 20 per cent progressing to squamous carcinoma. Confusing the two matters a great "
    "deal."],
   ["Oral lichen planus",
    "Lichen planus gives lacy white Wickham striae that are part of the mucosa and do not wipe away, "
    "carrying a 1 to 4 per cent malignant risk."],
   ["Leukoedema",
    "Leukoedema is a normal variant producing diffuse greyish-white buccal mucosa that DISAPPEARS "
    "WHEN STRETCHED rather than wiping off, and it leaves no erythematous base."]], C(89)),

Q("Oral leukoplakia", IO,
  "A 61-year-old man who has chewed tobacco for thirty years has a white plaque on the lateral "
  "tongue that will not scrape off and has been present four months.",
  [["Excisional biopsy",
    "Correct. Leukoplakia is premalignant by definition, with 5 to 20 per cent progressing to "
    "squamous cell carcinoma, and appearance alone cannot identify which lesions harbour dysplasia. "
    "Biopsy is the diagnostic step, alongside eliminating the carcinogenic irritant and examining "
    "for lymphadenopathy."],
   ["Topical antifungal and review in two weeks",
    "Antifungals treat candidiasis, and the fact that this will not scrape off is precisely what "
    "excludes that. Two weeks of the wrong treatment delays the biopsy."],
   ["Reassurance, as white oral lesions are usually benign",
    "Many white lesions are benign, but leukoplakia is specifically the one that is not, and this "
    "patient carries the classic risk factor."],
   ["Topical corticosteroid for presumed lichen planus",
    "Lichen planus is treated with steroids but appears as lacy striae rather than a solid plaque, "
    "and it too warrants biopsy when the appearance is atypical."]], C(134)),

Q("Erythroplakia", IO,
  "A 58-year-old woman who smokes and drinks has a well-demarcated red velvety patch on the floor "
  "of the mouth that does not scrape off.",
  [["Erythroplakia",
    "Correct. Erythroplakia is the red counterpart of leukoplakia and is far more dangerous: about "
    "90 per cent are already dysplastic or frankly malignant, against 5 to 20 per cent for "
    "leukoplakia. Alcohol and tobacco are the major risk factors and it is biopsied urgently."],
   ["Leukoplakia",
    "Leukoplakia is white rather than red. Colour is not cosmetic detail here: it separates a lesion "
    "with a modest premalignant risk from one that is usually already malignant."],
   ["Erythematous candidiasis",
    "Erythematous candidiasis exists and can be red, usually painful and associated with dentures or "
    "immunosuppression, and it responds to antifungal therapy rather than persisting as a fixed "
    "velvety patch."],
   ["Geographic tongue",
    "Geographic tongue is a benign migratory condition of the dorsal tongue with map-like patches "
    "that move over days, and it does not occur on the floor of the mouth."]], C(135)),

Q("Hairy leukoplakia", IO,
  "A 39-year-old man has painless white lesions on the lateral border of the tongue that wax and "
  "wane. He has no known medical conditions.",
  [["Test for HIV",
    "Correct. Hairy leukoplakia is a benign mucosal hyperplasia driven by Epstein-Barr virus and is "
    "strongly associated with HIV, where it is a common early finding. The lesion itself needs only "
    "observation, so its clinical value lies almost entirely in what it points to."],
   ["Excisional biopsy to exclude carcinoma",
    "Biopsy contributes to the diagnosis, but hairy leukoplakia is benign and not premalignant in "
    "the way ordinary leukoplakia is, so treating it as a cancer question misses the association "
    "that matters."],
   ["Prescribe a topical antifungal",
    "Antifungals treat candidiasis, which wipes off. This lesion does not, so treating it as thrush "
    "would fail and delay the important test."],
   ["Reassure and discharge",
    "The lesion is benign, which makes this superficially reasonable, but discharging him misses the "
    "chance to diagnose HIV at a stage when treatment is most effective."]], C(136)),

Q("Oral lichen planus", IO,
  "A 56-year-old woman has lacy white lines on both buccal mucosae that cannot be wiped away. She "
  "asks whether it is dangerous.",
  [["It carries a 1 to 4 per cent risk of carcinoma, higher if ulcerative",
    "Correct. Oral lichen planus is a chronic autoimmune condition in which activated lymphocytes "
    "destroy the basal layer, and 1 to 4 per cent progress to squamous cell carcinoma, with higher "
    "risk in ulcerative forms. Close follow-up is the point of the diagnosis, alongside pain relief "
    "and removing reversible contributors."],
   ["It is entirely benign and needs no follow-up",
    "That is the reassuring answer and the reason the malignant potential is emphasised. Discharging "
    "her means nobody watches a premalignant lesion in an easily examined site."],
   ["It becomes malignant in most cases",
    "Overstating the risk causes alarm and can drive overtreatment. A few per cent justifies "
    "surveillance rather than aggressive intervention."],
   ["It is an infection that antifungals will clear",
    "Candidiasis is the white lesion that responds to antifungals and is distinguished by wiping "
    "off. Lichen planus is immune-mediated and its striae are part of the mucosa."]], C(22)),

Q("Behcet syndrome", IO,
  "A 31-year-old man has recurrent painful oral ulcers. He also has similar ulcers on the scrotum "
  "and has had episodes of eye inflammation and joint pain.",
  [["Behcet syndrome",
    "Correct. Oral ulcers are the commonest feature of Behcet, affecting up to 100 per cent, and "
    "genital ulcers occur in about 75 per cent and look identical to oral aphthae. Diagnosis is "
    "clinical: recurrent aphthous ulceration in the context of characteristic systemic "
    "manifestations, which here include ocular and articular involvement."],
   ["Recurrent aphthous stomatitis",
    "Sutton disease is confined to the mouth with no systemic features. It is precisely the genital, "
    "ocular and joint involvement that lifts this out of that category."],
   ["Herpes simplex infection",
    "Recurrent herpes gives grouped vesicles that ulcerate on keratinised surfaces with a burning "
    "prodrome, and does not cause the multisystem inflammation described."],
   ["Systemic lupus erythematosus",
    "Lupus causes oral ulcers in around 40 per cent and can affect joints and eyes, so it is a fair "
    "differential, but the characteristic genital aphthae of Behcet are not a lupus feature."]],
  C(19)),

Q("Vocal cord nodules", IO,
  "An 8-year-old boy who shouts constantly during sport has been hoarse for four months. "
  "Laryngoscopy shows small, whitish, bilateral symmetric lesions at the junction of the anterior "
  "third and posterior two thirds.",
  [["Speech therapy",
    "Correct. Vocal cord nodules are the commonest cause of persistent dysphonia in children, "
    "sometimes called screamers' nodules, forming where the folds strike hardest during phonation. "
    "Because the cause is vocal behaviour, speech therapy that changes it is first line in both "
    "children and adults."],
   ["Surgical excision of both nodules",
    "Surgery does not address the behaviour that produced them, so they recur, and operating on a "
    "child's vibrating margin risks scarring that permanently alters the voice."],
   ["Inhaled corticosteroid",
    "Inhaled steroid treats airway inflammation and can itself cause dysphonia and thrush. Nodules "
    "are a fibrous response to trauma rather than an inflammatory condition."],
   ["Antireflux therapy",
    "Reflux contributes to laryngeal irritation and is worth considering in chronic hoarseness, but "
    "it does not produce paired symmetric lesions at the point of maximal impact."]], C(47)),

Q("Vocal cord polyp", IO,
  "A 53-year-old man who smokes heavily and shouts at work has six months of hoarseness. "
  "Laryngoscopy shows a single pedunculated lesion on the left cord with visible vascular markings.",
  [["Microlaryngoscopic excision",
    "Correct. A polyp is unilateral and pedunculated, which distinguishes it from bilateral "
    "symmetric nodules, and is commoner in men who smoke and abuse the voice. Excision both treats "
    "it and provides tissue, which matters because a large polyp may conceal an occult early "
    "laryngeal squamous carcinoma in exactly this risk group."],
   ["Speech therapy alone",
    "Speech therapy is first line for nodules, where behaviour is the whole cause. A unilateral "
    "polyp in a heavy smoker needs histology, and therapy alone would leave a possible carcinoma "
    "unexamined."],
   ["Observation with repeat laryngoscopy in a year",
    "A year of watching a unilateral lesion in a smoker allows a missed malignancy to progress, and "
    "hoarseness beyond two weeks is already the threshold for scoping."],
   ["A course of oral corticosteroids",
    "Steroids reduce inflammatory oedema but do not resolve an established gelatinous polyp, and "
    "leave the malignancy question open."]], C(48)),

Q("Vocal cord paralysis", IO,
  "A 59-year-old woman has a breathy hoarse voice and coughs when drinking, six weeks after "
  "thyroidectomy. Laryngoscopy shows one immobile cord.",
  [["Unilateral paralysis from recurrent laryngeal nerve injury",
    "Correct. The recurrent laryngeal nerve runs immediately behind the thyroid and is at risk "
    "during thyroidectomy. A unilateral paralysis leaves one cord unable to meet the other, giving a "
    "breathy voice from air escape and allowing aspiration during swallowing."],
   ["Bilateral vocal cord paralysis",
    "Bilateral paralysis produces inspiratory or biphasic stridor with a weak cry, because both "
    "cords sit near the midline and obstruct. Only one immobile cord is described and there is no "
    "stridor."],
   ["Vocal cord nodules from postoperative strain",
    "Nodules are bilateral, symmetric and follow prolonged vocal abuse. They do not immobilise a "
    "cord or cause aspiration."],
   ["Post-intubation laryngeal oedema",
    "Post-intubation oedema causes hoarseness and sometimes stridor but resolves within days rather "
    "than six weeks, and does not fix a cord."]], C(53)),
]
