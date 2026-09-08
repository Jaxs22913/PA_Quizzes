# -*- coding: utf-8 -*-
"""Final top-up pool for the ENT master exams.

Brings each lecture to fifty so the five forms fill without repeats. Covers all
five decks, so the deck constant varies per question rather than per file.
Keys are kept short deliberately -- see cmsent_shortfix.py for why.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D15 = "CMS I Disorders of the External and Middle Ear"
D16 = "16. Disorders of Inner Ear"
D17 = "hughie Nose & Paranasal Sinuses"
D18 = "CMS I Neoplasms and Neck Masses"
D19 = "CMS I Disorders of the Oral Cavity, Salivary Glands"

I15 = ("Disorders of the external and middle ear: etiologies, epidemiology, risk factors, clinical "
       "manifestations, differential diagnosis, diagnostic testing, management, referrals, patient "
       "education, and prognosis")
I16 = ("Disorders of the inner ear, balance and hearing loss: etiologies, epidemiology, risk "
       "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
       "referrals, patient education, and prognosis")
I17 = ("Disorders of the nose and paranasal sinuses: etiologies, epidemiology, risk factors, "
       "clinical manifestations, differential diagnosis, diagnostic testing, management, referrals, "
       "patient education, and prognosis")
I18 = ("Neck masses and neoplasms: the triangles and lymph nodes of the neck, and the etiologies, "
       "risk factors, clinical manifestations, differential diagnosis, diagnostic testing, "
       "management, referrals, patient education, and prognosis of neck masses and neoplasms")
I19 = ("Disorders of the oral cavity, salivary glands, and neck: etiologies, epidemiology, risk "
       "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
       "referrals, patient education, and prognosis")

QUESTIONS = [

# ---------------- Lecture 15 ----------------
Q("Cerumen removal", I15,
  "A 60-year-old man needs wax removed. He has a history of a tympanic membrane perforation "
  "repaired years ago.",
  [["Microsuction or curette under direct vision",
    "Correct. Irrigation is contraindicated when the drum may not be intact, because water forced "
    "into the middle ear seeds it with canal organisms and causes a suppurative otitis media. "
    "Removing the wax under direct vision keeps the procedure entirely within the canal and lets the "
    "operator see the drum as it is uncovered."],
   ["Warm water irrigation",
    "Irrigation is quick and effective in a normal ear but is the one technique specifically avoided "
    "when the drum's integrity is uncertain. A previously repaired perforation is exactly that "
    "situation."],
   ["Softening drops alone for two weeks",
    "Ceruminolytics help loosen impacted wax and are a reasonable adjunct, but they rarely clear a "
    "fully occluding plug on their own and would leave him with reduced hearing meanwhile."],
   ["Cotton bud removal by the patient at home",
    "Buds push wax deeper and abrade the canal skin, which is how impaction and otitis externa "
    "develop in the first place. Advising it would worsen the problem it is meant to solve."]],
  "next step", D15, 28),

Q("Otitis externa organisms", I15,
  "A clinician is asked which organisms otitis externa treatment must cover.",
  [["Pseudomonas and Staphylococcus",
    "Correct. Water exposure raises the canal pH and macerates the skin, which favours Pseudomonas "
    "in particular, alongside Staphylococcus from the skin flora. Topical fluoroquinolones are "
    "chosen because they cover both, and that Pseudomonas coverage is why an oral antibiotic like "
    "amoxicillin would be inadequate."],
   ["Streptococcus pneumoniae and Haemophilus influenzae",
    "Those are the middle ear organisms responsible for acute otitis media, reached through the "
    "eustachian tube from the nasopharynx. They are not the canal flora."],
   ["Candida and Aspergillus",
    "Those cause otomycosis, which typically follows prolonged antibiotic drops. They are what "
    "treatment sometimes creates rather than what it initially targets."],
   ["Moraxella catarrhalis and Mycoplasma",
    "Moraxella is a middle ear and sinus organism, and Mycoplasma is a respiratory pathogen. Neither "
    "is a canal organism."]],
  "treatment", D15, 41),

Q("Tympanic membrane examination", I15,
  "A clinician performs pneumatic otoscopy on a child with a suspected middle ear effusion.",
  [["Reduced mobility of the drum",
    "Correct. Pneumatic otoscopy applies a small pressure change and watches the drum move. Fluid "
    "behind it damps that movement, so reduced mobility is the finding that confirms an effusion and "
    "distinguishes it from a drum that merely looks dull. It is the bedside equivalent of a flat "
    "tympanogram."],
   ["Increased mobility of the drum",
    "Excessive movement suggests a monomeric or scarred drum, or ossicular discontinuity, which are "
    "the opposite mechanical problem. Fluid restricts rather than frees movement."],
   ["A bulging erythematous drum",
    "Bulging with erythema indicates pus under pressure in acute otitis media rather than a sterile "
    "effusion, and it is seen on ordinary otoscopy without needing the pneumatic bulb."],
   ["A visible cone of light",
    "The light reflex is a normal finding and its distortion is nonspecific. Its presence or absence "
    "does not establish whether there is fluid behind the drum."]],
  "testing", D15, 26),

Q("Chronic otitis media", I15,
  "A 30-year-old woman with chronic suppurative otitis media asks why her ear discharges but does "
  "not hurt.",
  [["The perforation lets the middle ear drain, so pressure never builds",
    "Correct. Pain in acute otitis media comes from pus stretching an intact drum. With an "
    "established perforation the middle ear has a permanent outlet, so pressure cannot accumulate "
    "and the infection expresses itself as discharge rather than pain. That painlessness is the "
    "clinical hallmark separating chronic from acute disease."],
   ["Chronic infection destroys the nerve supply to the drum",
    "The sensory innervation is not destroyed, and patients still feel a fresh acute infection or "
    "instrumentation. The mechanism is pressure relief, not denervation."],
   ["The organisms involved do not produce inflammation",
    "The middle ear mucosa is visibly inflamed and productive of discharge, so inflammation is "
    "clearly present. What is absent is confinement of that inflammation under pressure."],
   ["The discharge contains anaesthetic breakdown products",
    "There is no such mechanism. Discharge is inflammatory exudate and does not have analgesic "
    "properties."]],
  "mechanism", D15, 31),

Q("Otosclerosis inheritance", I15,
  "A 28-year-old woman with otosclerosis asks about the risk to her children.",
  [["It often runs in families and may worsen during pregnancy",
    "Correct. Otosclerosis has a strong familial tendency, which is why a family history supports the "
    "diagnosis. Progression during pregnancy is also recognised, which is relevant counselling for a "
    "woman of childbearing age who is deciding when to have surgery."],
   ["It is purely acquired from noise exposure",
    "Noise causes a sensorineural loss with a characteristic notch, not a conductive loss from "
    "stapes fixation. The two mechanisms are entirely different."],
   ["It is caused by recurrent middle ear infection in childhood",
    "Recurrent infection leads to tympanosclerosis, chronic perforation and cholesteatoma, which are "
    "different causes of conductive loss. Otosclerosis is new bone at the stapes footplate."],
   ["It has no hereditary component at all",
    "Denying the familial pattern removes information the patient specifically asked for and "
    "contradicts one of the features that supports the diagnosis clinically."]],
  "cause", D15, 65),

Q("Ear trauma", I15,
  "A 21-year-old man is struck on the ear with an open hand and has immediate pain, hearing loss "
  "and vertigo, with blood in the canal.",
  [["Assess urgently for inner ear injury as well as a perforation",
    "Correct. Vertigo after ear trauma is the finding that changes the picture. A simple perforation "
    "does not cause vertigo, so its presence raises the possibility of ossicular disruption with a "
    "perilymphatic fistula or direct labyrinthine injury, which needs prompt specialist assessment "
    "rather than routine review."],
   ["Reassure and review in two weeks, as most perforations heal",
    "That is the right advice for an uncomplicated perforation with no vertigo and normal facial "
    "nerve function. The vertigo here specifically excludes the uncomplicated category."],
   ["Irrigate the canal to clear the blood",
    "Irrigation is contraindicated with a known or suspected perforation, and it would drive water "
    "and blood into a middle ear that may already be communicating with the inner ear."],
   ["Prescribe vestibular suppressants and discharge",
    "Suppressing the vertigo masks the very sign that indicates a more serious injury, and "
    "discharging without assessment risks missing a fistula that may need repair."]],
  "next step", D15, 61),

# ---------------- Lecture 17 ----------------
Q("Sinus anatomy", I17,
  "A student asks which paranasal sinuses are present at birth.",
  [["The maxillary and ethmoid sinuses",
    "Correct. The maxillary and ethmoid sinuses are present at birth, which is why sinusitis in "
    "infants and young children involves those and why ethmoid disease is the classic source of "
    "paediatric orbital cellulitis. The frontal and sphenoid sinuses develop later in childhood and "
    "adolescence."],
   ["The frontal and sphenoid sinuses",
    "These pneumatise later, the frontal typically not until school age and beyond, which is why "
    "frontal sinusitis is not a diagnosis in a toddler."],
   ["All four sinuses are fully formed at birth",
    "If that were so, frontal sinusitis would be seen in infants, and it is not. Development is "
    "staggered through childhood."],
   ["None are present until age five",
    "The maxillary and ethmoid sinuses are present from birth and are the reason paediatric "
    "sinusitis exists at all in the first years of life."]],
  "finding", D17, 6),

Q("Epistaxis in the elderly", I17,
  "A 78-year-old woman on warfarin has a nosebleed that has stopped with pressure. Her "
  "international normalised ratio is 6.2.",
  [["Correct the anticoagulation as well as treating the nose",
    "Correct. Clotting studies are not routine in epistaxis but are indicated in anticoagulated "
    "patients, and this result is well above range. Treating only the local bleeding point leaves "
    "the systemic reason it bled and the risk of rebleeding or of haemorrhage elsewhere entirely "
    "unaddressed."],
   ["Treat the nose locally and continue warfarin unchanged",
    "Local measures deal with this episode but ignore a supratherapeutic result that is itself "
    "dangerous. The nosebleed here is a warning sign rather than an isolated local problem."],
   ["Stop warfarin permanently",
    "Stopping anticoagulation outright exposes her to whatever thrombotic risk it was prescribed "
    "for, which may be considerably more dangerous than a controlled nosebleed. The dose needs "
    "adjusting rather than abandoning."],
   ["Admit for immediate posterior packing",
    "The bleeding has already stopped with simple pressure, which indicates an anterior source that "
    "has been controlled. Packing an ear that is no longer bleeding adds discomfort and infection "
    "risk without benefit."]],
  "next step", D17, 44),

Q("Rhinitis medicamentosa", I17,
  "A 35-year-old man has used a topical decongestant spray daily for six weeks and now has worse "
  "congestion than when he started.",
  [["Rebound congestion from prolonged topical decongestant use",
    "Correct. Topical alpha agonists constrict the nasal vessels, but with sustained use the "
    "receptors downregulate and the vessels dilate more each time the drug wears off. The patient "
    "then uses it more often, and the congestion worsens. That is why these sprays carry a "
    "three-to-five-day limit."],
   ["Progression of an underlying allergic rhinitis",
    "Allergy would give clear bilateral discharge with itch and a bluish boggy mucosa, and it does "
    "not typically worsen in direct proportion to decongestant use. The temporal relationship here "
    "points to the drug."],
   ["Development of chronic bacterial sinusitis",
    "Chronic sinusitis brings facial pressure, purulent discharge and reduced smell over twelve "
    "weeks or more. Six weeks of pure congestion tied to spray use is a different problem."],
   ["A nasal polyp obstructing the airway",
    "A polyp would be visible on examination as a grey glistening mass and would cause steady "
    "obstruction with anosmia rather than congestion that fluctuates with each dose."]],
  "diagnosis", D17, 66),

Q("Sinusitis imaging", I17,
  "A clinician explains why computed tomography is not used to distinguish viral from bacterial "
  "sinusitis.",
  [["Both fill the sinuses, so imaging cannot separate them",
    "Correct. Mucosal thickening and fluid levels appear in ordinary viral rhinosinusitis as well as "
    "in bacterial infection, and can even be seen in asymptomatic people. Imaging therefore answers "
    "a question nobody is asking, and the distinction remains clinical, based on duration, double "
    "worsening and unilateral pain."],
   ["Computed tomography is too insensitive to show sinus fluid",
    "It is highly sensitive for sinus opacification, which is precisely the problem: it detects "
    "changes that are present in benign self-limiting illness."],
   ["The radiation dose makes it unsafe in any circumstance",
    "Dose is a genuine consideration but computed tomography is used appropriately for suspected "
    "complications and for chronic disease being considered for surgery. It is the indication that "
    "is wrong here, not the modality."],
   ["Contrast is required and is contraindicated in sinusitis",
    "Non-contrast studies show the sinuses perfectly well, and contrast is added when orbital or "
    "intracranial extension is suspected. Contrast is not the limiting factor."]],
  "testing", D17, 12),

Q("Nasal obstruction in children", I17,
  "A 5-year-old has chronic mouth breathing, snoring and hyponasal speech with bilateral nasal "
  "obstruction. There is no discharge.",
  [["Adenoidal hypertrophy",
    "Correct. The adenoid sits in the nasopharynx behind the nasal cavity, so enlargement obstructs "
    "both sides equally and produces mouth breathing, snoring and the hyponasal voice of a blocked "
    "nose. The bilateral, discharge-free pattern is what distinguishes it from a foreign body or "
    "infection."],
   ["Nasal foreign body",
    "A foreign body gives UNILATERAL foul-smelling purulent discharge in a young child. Bilateral "
    "obstruction with no discharge at all is the opposite pattern."],
   ["Nasal polyposis",
    "Polyps in a child are unusual and are strongly associated with cystic fibrosis, which is why "
    "they trigger a sweat test. They would also be visible on anterior rhinoscopy."],
   ["Deviated septum",
    "A deviated septum narrows one side preferentially, so it gives asymmetric obstruction. It is "
    "also usually traumatic or congenital rather than presenting as new snoring at five."]],
  "diagnosis", D17, 63),

Q("Septoplasty indications", I17,
  "A 33-year-old woman has a mildly deviated septum found incidentally. She has no symptoms.",
  [["No treatment, as an asymptomatic deviation needs none",
    "Correct. Septal deviation is extremely common and is only treated when it causes symptoms: "
    "obstruction, recurrent epistaxis from the drier open side, obstructive sleep apnoea, snoring or "
    "facial pain. Operating on an incidental finding in an asymptomatic patient offers only the "
    "risks of surgery."],
   ["Septoplasty to prevent future problems",
    "Prophylactic surgery is not offered, because most deviations never become symptomatic and the "
    "operation carries risks including perforation, bleeding and altered nasal shape."],
   ["A long-term intranasal steroid",
    "Steroid reduces mucosal swelling but cannot alter cartilage position, and prolonged use aimed "
    "at the septum is itself a cause of perforation."],
   ["Annual imaging to monitor progression",
    "Septal deviation does not progress in a way that imaging would usefully track, and surveillance "
    "of an asymptomatic anatomical variant serves no purpose."]],
  "treatment", D17, 30),

# ---------------- Lecture 18 ----------------
Q("Neck mass duration", I18,
  "A clinician is asked what duration of a neck mass should prompt concern about malignancy.",
  [["More than two weeks",
    "Correct. Duration over two weeks appears on the malignancy red-flag list alongside size over "
    "1.5 centimetres, firmness with immobility, absence of an infectious origin, age over 40, "
    "tobacco and alcohol use, and ulceration. Reactive nodes regress within one to two weeks, so "
    "persistence beyond that is the point at which the prior probability shifts."],
   ["More than 48 hours",
    "Two days is well within the course of an ordinary reactive node following an upper respiratory "
    "infection. Investigating at that point would generate enormous numbers of unnecessary "
    "referrals."],
   ["More than six months",
    "Waiting six months would delay a head and neck cancer diagnosis substantially. A mass present "
    "for YEARS suggests benignity, but six months is far too long to use as a trigger."],
   ["Duration is not part of the assessment",
    "Duration is one of the most useful pieces of information available at the bedside and is "
    "explicitly on the red-flag list."]],
  "finding", D18, 13),

Q("Thyroid cancer prognosis", I18,
  "A clinician ranks the four thyroid carcinomas by prognosis for a teaching session.",
  [["Papillary best, then follicular, then medullary, with anaplastic worst",
    "Correct. Papillary is commonest and has the best outlook; follicular is second commonest and "
    "spreads haematogenously; medullary is more insidious and most likely to metastasise, often "
    "presenting once a metastasis is found; and anaplastic is the most aggressive, causing death in "
    "6 to 36 months and resistant to all treatment."],
   ["Anaplastic best, then medullary, then follicular, with papillary worst",
    "This reverses the order entirely and would lead to reassuring the patient with the most "
    "dangerous tumour while alarming the one with the best outlook."],
   ["All four carry a similar prognosis",
    "The range runs from an excellent long-term outlook to death within three years, which is about "
    "as wide a spread as any organ's tumours show. Treating them as equivalent would misdirect both "
    "counselling and treatment intensity."],
   ["Medullary best because it produces calcitonin",
    "Calcitonin is a useful tumour marker for follow-up, but producing a measurable hormone does not "
    "make a tumour less dangerous. Medullary carcinoma is the most likely of the four to have "
    "metastasised at diagnosis."]],
  "finding", D18, 42),

Q("Neck mass in the immunocompromised", I18,
  "A 42-year-old man with untreated HIV has a rapidly enlarging cervical mass with purple "
  "discolouration of the overlying skin.",
  [["Kaposi sarcoma",
    "Correct. Kaposi sarcoma is one of the conditions that must be excluded in an HIV-positive "
    "patient with lymphadenopathy, alongside tuberculosis, Pneumocystis and lymphoma. Its vascular "
    "nature produces the characteristic purple appearance, which distinguishes it from the "
    "follicular hyperplasia that causes most adenopathy in this group."],
   ["Idiopathic follicular hyperplasia",
    "Follicular hyperplasia is the commonest cause of adenopathy in HIV, so it is the right base "
    "rate, but it produces ordinary-looking nodes without skin discolouration and is a diagnosis of "
    "exclusion."],
   ["Persistent generalised lymphadenopathy",
    "That diagnosis requires the absence of an identifiable infectious or neoplastic cause and is "
    "generalised rather than a single rapidly enlarging mass with skin change."],
   ["Reactive viral lymphadenopathy",
    "Reactive nodes follow an upper respiratory infection and regress in one to two weeks without "
    "changing the overlying skin. Rapid growth with purple discolouration is not reactive."]],
  "diagnosis", D18, 32),

Q("Neck dissection", I18,
  "A clinician explains why the primary tumour must be found before treating metastatic cervical "
  "squamous cell carcinoma.",
  [["Treatment fields and surgery both depend on where it came from",
    "Correct. The neck disease is a metastasis, so treating it alone leaves the source in place to "
    "keep seeding. Locating the primary determines the extent of resection and the radiotherapy "
    "field, which is why a systematic examination is made of every mucosal surface, "
    "the thyroid, the salivary glands and the skin."],
   ["The primary determines whether the patient needs antibiotics",
    "This is oncological rather than infectious disease. Antibiotics have no role in staging or "
    "treating a squamous carcinoma."],
   ["Without the primary the cell type cannot be established",
    "The cell type is already known from the nodal aspirate. What remains unknown is the site of "
    "origin, which is a different question."],
   ["The primary determines the patient's blood group compatibility",
    "Transfusion planning is unrelated to tumour site. This confuses perioperative preparation with "
    "oncological staging."]],
  "mechanism", D18, 39),

Q("Sialadenitis versus neck mass", I18,
  "A 60-year-old man has a mass in the upper neck that swells at mealtimes.",
  [["A salivary rather than a nodal cause",
    "Correct. Swelling that varies with eating implicates a salivary gland, because eating stimulates "
    "salivary flow and an obstructed gland distends. Lymph nodes and neoplasms do not change size "
    "over minutes, so the timing of the swelling localises the problem before any imaging is "
    "arranged."],
   ["A metastatic lymph node",
    "A malignant node is firm, immobile and steadily enlarging over weeks. It has no mechanism by "
    "which eating could change its size."],
   ["A branchial cleft cyst",
    "A branchial cleft cyst is a fixed congenital structure at the sternocleidomastoid border that "
    "enlarges when it becomes infected rather than at mealtimes."],
   ["A thyroid nodule",
    "A thyroid mass elevates with SWALLOWING because of its attachment to the larynx, which is a "
    "different observation: it moves rather than changing size, and it does so with any swallow."]],
  "diagnosis", D18, 15),

Q("Lymph node levels", I18,
  "A clinician is asked why the level of an involved cervical node matters in head and neck cancer.",
  [["The level predicts where the primary is likely to be",
    "Correct. Each region of the head and neck drains to a predictable nodal group, so the level of "
    "the involved node narrows the search for the primary. That is the practical application of the "
    "drainage map: jugulodigastric nodes point to the tonsil, juguloomohyoid to the tongue, and "
    "submandibular nodes to the face, sinuses and mouth."],
   ["The level determines the histological type of the tumour",
    "Histology comes from the aspirate and reflects the tissue of origin, not the anatomical "
    "position of the node. Squamous carcinoma can appear at any level."],
   ["The level determines whether antibiotics are needed",
    "Antibiotic decisions turn on whether the process is infective, which is a separate question "
    "from nodal level."],
   ["The level has no bearing on management",
    "Nodal level influences the search for the primary, the extent of neck dissection and the "
    "radiotherapy field, so it bears on nearly every management decision."]],
  "mechanism", D18, 10),

# ---------------- Lecture 16 ----------------
Q("Dix-Hallpike", I16,
  "A clinician performs the Dix-Hallpike manoeuvre and observes nystagmus that begins after a brief "
  "delay, lasts under a minute and diminishes on repetition.",
  [["A peripheral cause, consistent with positional vertigo",
    "Correct. Latency before onset, a short duration and fatigability on repeat testing are the "
    "signature of otoconia moving within a semicircular canal and then settling. Central positional "
    "nystagmus, by contrast, begins immediately, persists and does not fatigue, which is what makes "
    "these three features worth noting explicitly."],
   ["A central cause requiring urgent imaging",
    "Central positional nystagmus lacks latency and does not fatigue, and it is usually accompanied "
    "by other neurological signs. The described pattern points away from it."],
   ["A normal result",
    "A normal Dix-Hallpike provokes no nystagmus and no vertigo at all. Reproducing the symptom with "
    "characteristic nystagmus is a positive test."],
   ["An inconclusive result requiring electronystagmography",
    "The findings are characteristic enough to make the diagnosis and to proceed to an Epley "
    "manoeuvre. Electronystagmography assesses overall vestibular function rather than confirming "
    "this."]],
  "finding", D16, 88),

Q("Hearing loss classification", I16,
  "A patient has both an air-bone gap and elevated bone conduction thresholds.",
  [["A mixed hearing loss",
    "Correct. An air-bone gap means sound is being obstructed before it reaches the cochlea, which "
    "is conductive. Elevated bone conduction means the cochlea itself is not performing normally, "
    "which is sensorineural. Having both together defines a mixed loss, and it matters because "
    "correcting the conductive component will not restore hearing to normal."],
   ["A pure conductive loss",
    "A purely conductive loss has normal bone conduction thresholds, because the cochlea is intact "
    "and can be reached directly through the skull. Elevated bone thresholds exclude it."],
   ["A pure sensorineural loss",
    "A purely sensorineural loss has no air-bone gap, because both pathways are reduced equally by "
    "the same cochlear problem. The gap here excludes it."],
   ["A functional hearing loss",
    "Non-organic loss gives inconsistent results between tests rather than a reproducible pattern "
    "with an internally coherent air-bone gap."]],
  "finding", D16, 19),

Q("Ototoxicity monitoring", I16,
  "A patient starting a prolonged aminoglycoside course is enrolled in a monitoring programme.",
  [["Baseline and serial audiometry, watching the high frequencies first",
    "Correct. Aminoglycosides damage the outer hair cells at the cochlear base, which encode the "
    "highest frequencies, so loss appears there before it reaches the speech range. Detecting it "
    "early allows the drug to be changed before the patient notices any functional problem, which "
    "matters because the damage is usually permanent."],
   ["Monthly tympanometry",
    "Tympanometry assesses middle ear compliance, which aminoglycosides do not affect. It would "
    "remain normal throughout while cochlear damage accumulated undetected."],
   ["Weekly tuning fork testing",
    "Tuning forks detect gross asymmetry and distinguish conductive from sensorineural loss, but "
    "they cannot detect the early high-frequency changes that monitoring is designed to catch."],
   ["Symptom review alone",
    "By the time a patient notices, the loss has reached the speech frequencies and is established. "
    "The purpose of monitoring is to act before that point."]],
  "testing", D16, 32),

# ---------------- Lecture 19 ----------------
Q("Oral examination", I19,
  "A clinician is asked why oral examination is emphasised so strongly.",
  [["Most clinicians agree it matters but far fewer actually do it",
    "Correct. Over 80 per cent of surveyed clinicians believe oral "
    "examination is important, while the proportion who perform one routinely is much lower. That "
    "gap matters because oral cancer presents as a visible non-healing ulcer that a thirty-second "
    "look would find at a curable stage."],
   ["Oral disease is rare so examination is mostly reassurance",
    "Oral disease is common, ranging from candidiasis and aphthous ulceration to premalignant "
    "leukoplakia and frank carcinoma. Rarity is not the argument."],
   ["Examination is difficult and requires specialist equipment",
    "It requires a light, a tongue depressor and gloves. The barrier is habit rather than equipment, "
    "which is precisely why it is worth making a point of."],
   ["Oral findings rarely change management",
    "Findings such as a lesion that will not scrape off, or a red velvety patch, change management "
    "immediately by triggering biopsy. Several oral findings are also the first sign of systemic "
    "disease."]],
  "mechanism", D19, 6),
]
