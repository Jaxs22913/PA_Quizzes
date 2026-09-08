# -*- coding: utf-8 -*-
"""Lecture 19 questions for the ENT master exams -- Oral Cavity, Salivary Glands and Neck."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "CMS I Disorders of the Oral Cavity, Salivary Glands"
IO = ("Disorders of the oral cavity, salivary glands, and neck: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")

QUESTIONS = [

Q("Peritonsillar abscess", IO,
  "A 17-year-old attended four days ago with a 101.8 degree Fahrenheit fever and was diagnosed with "
  "acute pharyngitis and given penicillin. The sore throat is now worse, they cannot drink, and "
  "swallowing is excruciating. The voice is muffled. Examination shows right medial deviation of "
  "the soft palate with marked right tonsillar swelling.",
  [["Peritonsillar abscess",
    "Correct. Pus collecting between the tonsillar capsule and the pharyngeal muscles pushes the "
    "soft palate and tonsil medially, which produces the deviation described. The muffled hot potato "
    "voice comes from the mass distorting the oropharynx, and the classic triad is completed by "
    "trismus, the most reliable symptom. It is the commonest deep infection of the head and neck and "
    "typically follows an inadequately treated tonsillitis."],
   ["Mononucleosis",
    "Mononucleosis causes bilateral tonsillar enlargement with exudate, fever and cervical "
    "adenopathy, and it would not deviate the soft palate to one side. Its worsening after "
    "penicillin usually takes the form of a rash rather than unilateral swelling."],
   ["Dental abscess",
    "A dental abscess arises around a tooth root and causes localised gum and facial swelling with "
    "tooth pain. It does not displace the soft palate or produce a hot potato voice unless it has "
    "spread into the deep neck spaces, which would give a different picture."],
   ["Oral candidiasis",
    "Thrush produces creamy white patches that wipe off, is largely painless, and does not cause "
    "fever, unilateral swelling or airway-related voice change. It is also unusual in an "
    "immunocompetent adolescent."]],
  "diagnosis", D, 99),

Q("Laryngeal carcinoma", IO,
  "A 68-year-old with a 50 pack-year smoking history has four months of worsening dysphagia, "
  "occasional blood-streaked sputum and intermittent right ear pain on swallowing. Stridor is "
  "audible over the trachea. Nasopharyngoscopy shows a mass replacing the right true vocal cord.",
  [["Hoarseness",
    "Correct. A mass replacing the true vocal cord prevents that cord vibrating and apposing "
    "normally, and voice production depends on both cords meeting and vibrating together. "
    "Hoarseness is therefore the expected and usually earliest symptom of a glottic tumour, and the "
    "referred ear pain reflects shared vagal innervation between the larynx and the ear."],
   ["Tonsillar exudates",
    "Exudate over the tonsils indicates an infective pharyngitis or tonsillitis developing over days. "
    "It has nothing to do with a four-month history of a cord mass in a heavy smoker and would not "
    "coexist with stridor from a fixed lesion."],
   ["Fever and retropharyngeal oedema",
    "Those describe a retropharyngeal abscess, which is an acute infection of children under five or "
    "of adults after instrumentation. The tempo here is months, and the lesion is on the cord rather "
    "than in the retropharyngeal space."],
   ["Weight gain",
    "Four months of progressive dysphagia in a patient with a laryngeal malignancy causes weight "
    "LOSS, from reduced intake and from the disease itself. Weight gain would argue against the "
    "diagnosis rather than supporting it."]],
  "finding", D, 144),

Q("Epiglottitis", IO,
  "A 4-year-old is brought in with a few hours of high fever, drooling, refusal to swallow and a "
  "muffled voice. He is sitting upright and leaning forward with his chin thrust out, and appears "
  "distressed and anxious.",
  [["Do not examine the throat; secure the airway with the appropriate team",
    "Correct. The four Ds and the tripod position describe supraglottitis, and the teaching is "
    "explicit that once it is suspected, examinations that increase the child's anxiety, including "
    "intraoral examination and venipuncture, may precipitate complete airway obstruction. The "
    "priority is a controlled airway in theatre with anaesthetic and surgical teams present."],
   ["Examine the pharynx with a tongue depressor to confirm the diagnosis",
    "This is the specific action to avoid. Depressing the tongue in a child with an "
    "inflamed supraglottis can trigger laryngospasm or complete obstruction, and the diagnosis does "
    "not depend on seeing the epiglottis in clinic."],
   ["Obtain a lateral neck radiograph before any intervention",
    "The thumbprint sign is a recognised finding but the film is not "
    "necessary for diagnosis. Sending an unstable child to radiology, away from the team who can "
    "secure the airway, adds risk without adding information."],
   ["Give oral antibiotics and arrange review in the morning",
    "Antibiotics are part of treatment but not before the airway is safe, and oral administration "
    "requires a child to swallow, which is exactly what this child cannot do. Overnight observation "
    "at home in a disease with high mortality if untreated is unsafe."]],
  "next step", D, 63),

Q("Infectious mononucleosis", IO,
  "A 19-year-old university student is treated with amoxicillin for a presumed streptococcal sore "
  "throat. Three days later she develops a widespread maculopapular rash over the trunk. Her "
  "tonsils are enlarged with exudate and she has bilateral cervical lymphadenopathy and fatigue.",
  [["She has infectious mononucleosis, and the aminopenicillin triggered the rash",
    "Correct. Giving an aminopenicillin to someone with Epstein-Barr virus infection reliably "
    "provokes a widespread exanthem, and the sequence described is the classic route to the "
    "diagnosis: a sore throat treated as strep, a rash, and then the real cause. The triad of fever, "
    "tonsillar pharyngitis and cervical lymphadenopathy fits mononucleosis rather than "
    "streptococcus."],
   ["She has a true penicillin allergy and must avoid the class for life",
    "This is the consequential misreading. The mononucleosis rash is not immunoglobulin E mediated "
    "and does not indicate a lifelong allergy, so labelling her allergic removes an entire antibiotic "
    "class from her future care on the basis of a virus."],
   ["The rash is scarlet fever from her streptococcal infection",
    "Scarlet fever produces a sandpapery erythematous rash with circumoral pallor and a strawberry "
    "tongue, beginning within a day or two of the sore throat rather than after antibiotics. The "
    "morphology and the timing both point elsewhere."],
   ["The rash is unrelated and should prompt a search for another cause",
    "Treating a textbook drug-virus interaction as coincidence means missing the diagnosis that the "
    "rash has just handed over. The association is specific enough that the rash is itself a "
    "diagnostic clue."]],
  "cause", D, 87),

Q("Infectious mononucleosis", IO,
  "A 20-year-old is confirmed to have infectious mononucleosis. He plays rugby and asks when he can "
  "return to training.",
  [["Avoid contact sport for about a month, until splenomegaly has resolved",
    "Correct. Epstein-Barr virus enlarges the spleen, and an enlarged spleen has a thin capsule "
    "under tension that can rupture with relatively minor abdominal trauma, which is a "
    "life-threatening complication. Avoiding contact sport and heavy lifting for about a month, with "
    "resolution of splenomegaly confirmed, is the standard advice."],
   ["Return as soon as the fever and sore throat settle",
    "Symptomatic recovery and splenic recovery are not the same timeline. A patient can feel well "
    "while the spleen is still enlarged, which is precisely when a tackle can rupture it."],
   ["No restriction is needed, as splenic rupture is a myth",
    "Splenic rupture is rare but real and is the reason the restriction exists. Dismissing it "
    "removes the single piece of advice in this illness that prevents a catastrophic outcome."],
   ["Avoid all exercise for six months",
    "Six months of complete inactivity is far beyond what the risk justifies and would be unlikely "
    "to be followed. The restriction is specific to contact and heavy lifting, and it is measured in "
    "weeks."]],
  "treatment", D, 86),

Q("Sialolithiasis", IO,
  "A 48-year-old man has recurrent painful swelling under the right side of his jaw that comes on "
  "within minutes of starting a meal and settles over the following hour. On examination a firm "
  "structure is palpable in the floor of the mouth.",
  [["Sialolithiasis of the submandibular duct",
    "Correct. Eating stimulates salivary flow, and a stone obstructing the duct traps that saliva "
    "behind it, distending the gland until the pressure equalises. That is why the pain is timed to "
    "meals and settles afterwards, and why it is called salivary colic. Between 80 and 90 per cent "
    "of stones are submandibular because the duct runs a long uphill course carrying alkaline, "
    "mucin-rich saliva."],
   ["Acute suppurative sialadenitis",
    "Bacterial infection of the gland produces constant swelling with fever, overlying erythema and "
    "pus expressible from the duct, typically in a dehydrated post-operative or elderly patient. It "
    "does not fluctuate with meals."],
   ["Mumps parotitis",
    "Mumps affects the parotid rather than the submandibular gland, is usually bilateral, occurs "
    "with systemic viral symptoms, and does not produce a palpable stone or meal-related colic."],
   ["A parotid neoplasm",
    "A salivary tumour presents as a slowly growing painless mass, most often at the tail of the "
    "parotid. Neither the location, the pain, nor the relationship to eating fits a neoplasm."]],
  "diagnosis", D, 42),

Q("Oral candidiasis", IO,
  "A 62-year-old man using an inhaled corticosteroid for asthma has white patches on his buccal "
  "mucosa and tongue. When the clinician wipes one with a tongue depressor it comes away, leaving "
  "an erythematous base.",
  [["Oral candidiasis",
    "Correct. The single most useful bedside manoeuvre in a white oral lesion is to try to wipe it "
    "off. Candida forms a pseudomembrane that is removable, revealing inflamed mucosa underneath. "
    "Inhaled corticosteroid deposited in the mouth suppresses local immunity and is a common cause, "
    "which is why patients are told to rinse after using the inhaler."],
   ["Oral leukoplakia",
    "Leukoplakia is defined precisely as a white lesion that CANNOT be scraped off and cannot be "
    "attributed to another condition. It is premalignant, with 5 to 20 per cent progressing to "
    "squamous cell carcinoma, so confusing the two matters."],
   ["Oral lichen planus",
    "Lichen planus gives lacy white lines, called Wickham striae, that are part of the mucosa and do "
    "not wipe away. Its significance is a 1 to 4 per cent risk of malignant transformation, higher "
    "in ulcerative forms."],
   ["Leukoedema",
    "Leukoedema is a normal variant producing a diffuse greyish-white buccal mucosa, and its "
    "distinguishing feature is that it DISAPPEARS WHEN THE MUCOSA IS STRETCHED rather than being "
    "wiped away. It leaves no erythematous base."]],
  "diagnosis", D, 89),

Q("Oral leukoplakia", IO,
  "A 59-year-old man who has chewed tobacco for thirty years has a white plaque on the lateral "
  "border of the tongue. It cannot be scraped off and has been present for four months.",
  [["Excisional biopsy",
    "Correct. Leukoplakia is a premalignant lesion by definition, with 5 to 20 per cent progressing "
    "to squamous cell carcinoma, and clinical appearance cannot tell which lesions harbour dysplasia "
    "or invasion. Biopsy is therefore the diagnostic step, alongside eliminating the carcinogenic "
    "irritant and a complete intraoral examination with palpation for lymphadenopathy."],
   ["Topical antifungal therapy and reassessment in two weeks",
    "Antifungal treatment addresses candidiasis, and the fact that this lesion will not scrape off "
    "is what excludes that diagnosis. Two weeks of the wrong treatment delays the biopsy of a "
    "premalignant lesion."],
   ["Reassurance, since white oral lesions are usually benign",
    "Many white lesions are benign, but leukoplakia is specifically the one that is not, and this "
    "patient carries the classic risk factor. Reassurance without tissue is exactly the error the "
    "definition is designed to prevent."],
   ["Topical corticosteroid for presumed lichen planus",
    "Lichen planus is treated with steroids but presents as lacy Wickham striae rather than a solid "
    "plaque, and it too carries a malignant risk that warrants biopsy when the appearance is "
    "atypical."]],
  "next step", D, 134),

Q("Erythroplakia", IO,
  "A 61-year-old woman who smokes and drinks has a well-demarcated red velvety patch on the floor "
  "of the mouth. It does not scrape off.",
  [["Erythroplakia, of which about 90 per cent are dysplastic or already carcinoma",
    "Correct. Erythroplakia is the red counterpart of leukoplakia and is far more dangerous: around "
    "90 per cent of these lesions are already dysplastic or frankly malignant, against 5 to 20 per "
    "cent for leukoplakia. Alcohol and tobacco are the major risk factors, and it is biopsied "
    "urgently."],
   ["Leukoplakia, with a 5 to 20 per cent risk of transformation",
    "Leukoplakia is white rather than red. The colour is not cosmetic detail here: it is the single "
    "feature that separates a lesion with a modest premalignant risk from one that is usually "
    "already malignant."],
   ["Oral candidiasis with an erythematous pattern",
    "Erythematous candidiasis exists and can be red rather than white, but it is usually painful, "
    "associated with dentures or immunosuppression, and responds to antifungal therapy. It does not "
    "present as a solitary well-demarcated velvety patch in a smoker."],
   ["Geographic tongue",
    "Geographic tongue is a benign migratory condition of the dorsal tongue with map-like patches "
    "that change position over days. It does not occur on the floor of the mouth and does not "
    "persist as a fixed lesion."]],
  "diagnosis", D, 135),

Q("Ludwig angina", IO,
  "A 46-year-old man with poorly controlled diabetes has two days of rapidly increasing swelling "
  "under the chin and in the floor of the mouth after a dental infection. The tongue is displaced "
  "upward and backward, and he is drooling and speaking with difficulty.",
  [["Secure the airway and start antibiotics, with surgical drainage if threatened",
    "Correct. Ludwig angina is a rapidly spreading cellulitis of the submental, sublingual and "
    "submandibular spaces. As the floor of the mouth swells it pushes the tongue up and back into "
    "the airway, which is why this is an emergency and why airway management comes first. "
    "Antibiotics cover the mixed oral flora, and external drainage through bilateral submental "
    "incisions is used when the airway is threatened."],
   ["Oral antibiotics and urgent dental review in the morning",
    "A dental consultation is genuinely part of management because the source is usually a tooth, "
    "but sending home a diabetic patient whose tongue is already displaced backward risks losing the "
    "airway overnight. The referral does not replace admission."],
   ["Incision and drainage of the tooth abscess alone",
    "Draining the offending tooth addresses the source but not the established cellulitis in the "
    "deep spaces, which is what is compressing the airway. Both have to be dealt with, and the "
    "airway takes precedence."],
   ["Intravenous corticosteroids alone to reduce the swelling",
    "Steroids may be used as an adjunct but do not treat the infection and do not reliably protect "
    "an airway that is already being displaced. Relying on them alone leaves a spreading bacterial "
    "infection untreated."]],
  "next step", D, 111),

Q("Retropharyngeal abscess", IO,
  "A 3-year-old has fever, sore throat, neck stiffness and refusal to eat for two days. He is now "
  "drooling and leaning forward with his neck extended. A lateral neck radiograph shows widening of "
  "the prevertebral soft tissue.",
  [["Retropharyngeal abscess, which is a surgical emergency",
    "Correct. Suppuration of retropharyngeal nodes after an upper respiratory infection is a disease "
    "of children under five, and the widened prevertebral space on a lateral film is the classic "
    "radiographic sign. It is a surgical emergency because the space runs from skull base to "
    "posterior mediastinum, and mediastinitis carries a 50 per cent mortality."],
   ["Epiglottitis",
    "Epiglottitis shares drooling and the forward-leaning posture, so it is the right differential, "
    "but it comes on over hours rather than two days, produces a thumbprint sign rather than a "
    "widened prevertebral space, and does not typically give neck stiffness."],
   ["Bacterial pharyngitis",
    "Streptococcal pharyngitis causes fever, exudate and tender nodes but does not produce neck "
    "stiffness, drooling or an abnormal prevertebral soft tissue shadow. Those findings indicate a "
    "collection rather than a mucosal infection."],
   ["Peritonsillar abscess",
    "A peritonsillar abscess deviates the uvula and causes trismus with a hot potato voice, and it "
    "is a disease of adolescents and young adults rather than toddlers. It also would not widen the "
    "retropharyngeal space."]],
  "diagnosis", D, 105),

Q("Bacterial pharyngitis", IO,
  "A 10-year-old has a two-day sore throat with a temperature of 101 degrees Fahrenheit, tonsillar "
  "exudate and tender anterior cervical nodes. She has no cough. A rapid antigen detection test is "
  "negative.",
  [["Send a throat culture before deciding about antibiotics",
    "Correct. Her Centor score is high, with a point each for absence of cough, exudate, fever and "
    "tender anterior nodes, plus one for her age. Rapid antigen tests are specific but not "
    "sufficiently sensitive, so a negative result in a child with a high clinical probability is "
    "always confirmed by culture rather than accepted."],
   ["Accept the negative test and treat symptomatically",
    "Accepting a negative rapid test at face value in a high-probability patient is the error the "
    "confirmatory culture exists to prevent. Missing streptococcal infection leaves the risk of "
    "rheumatic fever unaddressed."],
   ["Start penicillin immediately without further testing",
    "Empiric treatment is a defensible option at the very highest scores, but with a negative rapid "
    "test in hand the culture will settle the question within a day or two and avoids treating a "
    "viral illness."],
   ["Order antistreptolysin O titres to make the diagnosis today",
    "Antistreptolysin O is the definitive test but reflects an antibody response that takes time to "
    "rise, so it is useful for establishing past infection rather than for deciding treatment during "
    "an acute sore throat."]],
  "next step", D, 74),

Q("Vocal cord nodules", IO,
  "A 9-year-old boy who shouts constantly during sport has been hoarse for four months. "
  "Laryngoscopy shows small, well-defined, whitish, bilateral and symmetric lesions at the junction "
  "of the anterior third and posterior two thirds of the vocal folds.",
  [["Speech therapy",
    "Correct. Vocal cord nodules are the commonest cause of persistent dysphonia in children, "
    "sometimes called screamers' nodules, and they form where the folds strike each other hardest "
    "during phonation. Because they are caused by mechanical trauma from vocal behaviour, speech "
    "therapy that changes that behaviour is first-line treatment in both children and adults."],
   ["Surgical excision of both nodules",
    "Surgery does not address the vocal behaviour that produced the nodules, so they recur, and "
    "operating on the vibrating margin of a child's cord risks scarring that permanently alters the "
    "voice. It is reserved for lesions that fail conservative management."],
   ["Inhaled corticosteroid",
    "Inhaled steroid treats airway inflammation and can itself cause dysphonia and candidiasis. "
    "Nodules are fibrous responses to trauma rather than an inflammatory condition that steroids "
    "resolve."],
   ["Antireflux therapy",
    "Reflux is a genuine contributor to laryngeal irritation and is worth considering in chronic "
    "hoarseness, but it does not produce paired symmetric lesions at the point of maximal impact, "
    "which is a mechanical signature."]],
  "treatment", D, 47),

Q("Vocal cord polyp", IO,
  "A 51-year-old man who smokes heavily and uses his voice loudly at work has six months of "
  "hoarseness. Laryngoscopy shows a single pedunculated lesion on the left vocal fold with visible "
  "vascular markings.",
  [["Microlaryngoscopic excision, partly because a polyp can conceal a carcinoma",
    "Correct. A polyp is unilateral and pedunculated, which distinguishes it from bilateral "
    "symmetric nodules, and it is commoner in men who smoke and abuse the voice. Excision both "
    "treats it and provides tissue, which matters because a large polyp may hide an occult early "
    "laryngeal squamous cell carcinoma in exactly this risk group."],
   ["Speech therapy alone",
    "Speech therapy is first line for nodules, where behaviour is the whole cause. A unilateral "
    "polyp in a heavy smoker needs to be seen histologically, and voice therapy alone would leave a "
    "possible carcinoma unexamined."],
   ["Observation with repeat laryngoscopy in a year",
    "A year of watching a unilateral lesion in a smoker allows a missed malignancy to progress. "
    "Chronic hoarseness beyond two weeks is already the threshold for scoping rather than watching."],
   ["A course of oral corticosteroids",
    "Steroids reduce inflammatory oedema but do not resolve an established gelatinous polyp, and "
    "they leave the diagnostic question about malignancy entirely open."]],
  "treatment", D, 48),

Q("Temporomandibular joint disorder", IO,
  "A 34-year-old woman has facial pain, clicking of the jaw and difficulty opening her mouth wide. "
  "She also reports tinnitus, a sensation of ear fullness and occasional dizziness. Otoscopy and "
  "audiometry are normal.",
  [["Temporomandibular joint disorder",
    "Correct. The temporomandibular joint sits immediately anterior to the ear canal, so its "
    "disorders commonly produce referred ear symptoms including tinnitus, fullness and dizziness "
    "with a completely normal ear examination. Jaw pain with clicking and limited opening in a woman "
    "of childbearing age is the typical presentation, and it is the second commonest musculoskeletal "
    "cause of pain and disability."],
   ["Meniere disease",
    "Meniere produces episodic vertigo lasting hours with documented fluctuating low-frequency "
    "sensorineural loss and tinnitus. Her audiometry is normal, and Meniere does not cause jaw "
    "clicking or limited mouth opening."],
   ["Eustachian tube dysfunction",
    "Eustachian tube dysfunction gives fullness and popping with a retracted drum and often an "
    "abnormal tympanogram. Her otoscopy is normal, and it does not explain the jaw pain or the "
    "restricted opening."],
   ["Acoustic neuroma",
    "A schwannoma causes progressive unilateral sensorineural loss with disproportionately poor "
    "speech discrimination and imbalance. Normal audiometry argues strongly against it, and it has "
    "no jaw component."]],
  "diagnosis", D, 130),

Q("Acute suppurative sialadenitis", IO,
  "A 79-year-old woman is four days after hip surgery and has poor oral intake. She develops "
  "unilateral painful swelling over the angle of the jaw with overlying erythema. Pus can be "
  "expressed from the duct opposite the upper second molar.",
  [["Rehydration with intravenous antistaphylococcal antibiotics",
    "Correct. Dehydration and reduced oral intake cause salivary stasis, and stasis lets bacteria "
    "ascend the parotid duct. Staphylococcus aureus is the commonest organism, and pus expressible "
    "from Stensen duct confirms the gland is infected. Treatment is rehydration, which restores "
    "flow, together with penicillinase-resistant gram-positive cover."],
   ["Antiviral therapy for mumps",
    "Mumps parotitis is a viral illness of children and young adults, usually bilateral, and does "
    "not produce purulent discharge from the duct. Purulence points to bacterial infection."],
   ["Immediate parotidectomy",
    "Surgery is reserved for abscess that does not respond to 48 hours of conservative treatment, "
    "and even then drainage rather than gland removal is the usual step. Operating on an acutely "
    "infected gland risks the facial nerve unnecessarily."],
   ["Sialography to identify a stone",
    "Sialography is useful in recurrent obstructive disease, but it is avoided during acute "
    "infection because injecting contrast retrogradely into an infected gland can worsen it. "
    "Stones also more often affect the submandibular gland."]],
  "treatment", D, 38),

Q("Diphtheria", IO,
  "An 8-year-old recently arrived from a region with low immunisation coverage has a mild sore "
  "throat, low-grade fever and marked malaise. Examination shows a tenacious grey membrane covering "
  "the tonsils and pharynx that bleeds when disturbed.",
  [["Diphtheria antitoxin obtained from the Centers for Disease Control, plus antibiotics",
    "Correct. A tenacious adherent grey membrane in an unimmunised child is diphtheria. The "
    "organism's damage is caused by an exotoxin that produces myocarditis and a cranial neuropathy, "
    "so antitoxin is required to neutralise circulating toxin, alongside penicillin or erythromycin "
    "for 14 days and isolation until three consecutive cultures are negative."],
   ["Penicillin alone for 10 days",
    "Antibiotics eradicate the organism but do nothing about toxin already in the circulation, and "
    "it is the toxin that causes the myocarditis and neuropathy which kill. Omitting antitoxin "
    "leaves the lethal mechanism untreated."],
   ["Supportive care, as it is likely viral pharyngitis",
    "Viral pharyngitis does not produce an adherent membrane that bleeds on removal. Treating this "
    "as viral misses a notifiable disease with a specific antidote and a public health response."],
   ["Corticosteroids to reduce the pharyngeal swelling",
    "Steroids may occasionally be used adjunctively for airway compromise, but they do not "
    "neutralise the toxin or eliminate the organism, and using them alone allows both to continue."]],
  "treatment", D, 113),
]
