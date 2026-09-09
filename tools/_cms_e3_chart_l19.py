# -*- coding: utf-8 -*-
"""Lecture 19 rows for the ENT comparison chart.

Disorders of the Oral Cavity, Salivary Glands, and Neck, Prof. Chand Shah.
151 slides and the largest lecture in the block by a distance -- the syllabus
lists 35 conditions under it. BUILT FROM THE SLIDES ALONE: no recording is in
the inbox, and Jaxon asked for the build to proceed without one.

THE DISCRIMINATOR COLUMNS, ONE MORE TIME. Ear: pain and hearing loss. Nose:
pain and discharge. Neck mass: pain and location. Here the side line carries
WHERE IN THE MOUTH OR THROAT the lesion sits, because that is what separates
an aphthous ulcer from candidiasis from leukoplakia at a glance, and the third
column carries the finding that names it.

SIX SLIDES ARE PICTURES OF CONTENT and extract as bare titles or nothing at
all. Transcribed into the rows rather than lost, per [[image_only_slides]]:
  slide 50   normal larynx against papilloma, labelled
  slide 64   the THUMBPRINT SIGN -- epiglottitis against a normal epiglottis
  slide 71   streptococcal against viral pharyngitis, side by side
  slide 75   the Centor scoring algorithm (the criteria themselves are in the
             text of slide 76, so only the score-to-action mapping was at risk)
  slide 79   the JONES criteria graphic for rheumatic fever
  slide 85   the mononucleosis heterophile-antibody algorithm

WHAT IS LEFT OUT. Slide 102 is a cartoon about peritonsillar abscess drainage
and slide 151 is the professor's dog. Slides 5, 29-31 and 91 are anatomy
diagrams and belong to the guide, not to a "this is what it looks like" cell.
"""
VAR = "Oral mucosa variant"
ULC = "Oral ulcer"
SAL = "Salivary gland"
VC = "Vocal cord and larynx"
AIR = "Airway emergency"
PHA = "Pharynx"
DEEP = "Deep neck infection"
DENT = "Dentition"
JAW = "Jaw"
LES = "Oral lesion"
ONEO = "Oral and salivary neoplasm"
D19 = "CMS I Disorders of the Oral Cavity, Salivary Glands"

ROWS_L19 = [
 ("Leukoedema", VAR,
  "<b>Normal variant</b> &middot; greyish-white buccal mucosa that <b>DISAPPEARS WHEN "
  "STRETCHED</b>",
  "A common, benign mucosal change and a normal variant, caused by accumulation of fluid within the "
  "epithelial cells. Diffuse greyish-white appearance of the buccal mucosa.",
  "Clinical. The distinguishing manoeuvre is <b>stretching the mucosa &mdash; the change "
  "disappears</b>, which is what separates it from leukoplakia.",
  "None &mdash; reassurance.", "Routine",
  "Naming it as a variant is the whole job; it needs no biopsy and no follow-up.", "9", D19),

 ("Fordyce granules", VAR,
  "<b>Normal variant</b> &middot; <b>ectopic sebaceous glands</b> &middot; yellow-white papules on "
  "lip or buccal mucosa",
  "Normal variants &mdash; ectopic sebaceous glands in a site where sebaceous glands are not "
  "expected. Small yellow-white papules on the vermilion of the lip and the buccal mucosa.",
  "Clinical.", "None &mdash; reassurance.", "Routine",
  "Patients find them alarming because they appear suddenly to the person looking; they have "
  "always been there.", "10", D19),

 ("Physiologic pigmentation", VAR,
  "<b>Normal variant</b> &middot; symmetrical <b>melanin</b> pigmentation, commoner in darker skin",
  "Physiologic oral pigmentation is commonly seen and is a normal variant, from melanin.",
  "Clinical.", "None &mdash; reassurance.", "Routine",
  "The reason it matters is the differential it sits in, not the lesion itself.", "11", D19),

 ("Aphthous stomatitis (canker sores)", ULC,
  "<b>Painful round ulcer, YELLOW-GREY fibrinoid centre with a RED HALO</b> &middot; on "
  "<b>non-keratinised, freely moving</b> mucosa",
  "The commonest cause of acute recurrent oral ulcers in adolescents and young adults. Found on "
  "<b>freely moving, non-keratinised mucosa</b> &mdash; buccal and labial mucosa, non-attached "
  "gingiva, palate. Trauma (cheek biting, a dental procedure) and stress are exacerbating factors; "
  "the cause is unknown, though human herpesvirus 6 has been suggested. <b>Minor (&lt;1&nbsp;cm)</b> "
  "are commonest, burn and tingle first, and last 7&ndash;10 days. <b>Major (&gt;1&nbsp;cm)</b> are "
  "more painful, multiple, scar, and last over a month. <b>Herpetiform</b> are numerous 1&ndash;3&nbsp;mm "
  "ulcers, scar, and last over a month.",
  "Clinical.",
  "Observation &mdash; it is self-limiting. Anti-inflammatories, antibiotics, antivirals, oral and "
  "topical corticosteroids (triamcinolone, fluocinonide), cauterisation with silver nitrate, "
  "<i>Lactobacillus</i> capsules, dilute water rinses.",
  "Routine",
  "<b>Recurrent aphthous stomatitis is called Sutton disease.</b> Non-keratinised mucosa is the "
  "location rule that separates it from herpes.", "15&ndash;17", D19),

 ("Behcet syndrome", ULC,
  "Oral ulcers in <b>up to 100%</b> &middot; <b>GENITAL ulcers in 75%</b> &middot; multisystem",
  "An inflammatory, multisystem disorder with vascular, articular, gastrointestinal, neurologic, "
  "urogenital, pulmonary and cardiac involvement. <b>Oral ulcers are the commonest feature, "
  "affecting up to 100% of patients.</b> Genital ulcers occur in about 75% and look like oral "
  "aphthae.",
  "Clinical &mdash; recurrent aphthous ulceration <b>in the context of the characteristic systemic "
  "manifestations</b>.",
  "<b>No cure.</b> Corticosteroids, intravenous immunoglobulin, immunosuppressives &mdash; "
  "colchicine, azathioprine, cyclosporine-A, interferon alpha, cyclophosphamide.",
  "Urgent",
  "The oral ulcers look ordinary; it is the genital ulcers and the systemic features that make the "
  "diagnosis.", "19", D19),

 ("Oral lichen planus", ULC,
  "<b>WICKHAM STRIAE</b> &mdash; lacy white lines on buccal mucosa &middot; <b>1&ndash;4% become "
  "squamous cell carcinoma</b>",
  "A common chronic inflammatory autoimmune disorder in which the basal layer is destroyed by "
  "activated lymphocytes. May be familial or drug-induced (penicillamine, methyldopa, phenothiazine, "
  "antimalarials). Classically <b>purple, polygonal, pruritic papules</b> on flexor surfaces and "
  "trunk; 60&ndash;70% affect lips, oral mucosa and eyelids, and the oral lesions are more chronic. "
  "<b>Kobner isomorphic phenomenon</b> &mdash; lesions provoked by physical trauma. Types: "
  "<b>reticular</b> (lacy white Wickham striae), <b>plaque</b> (looks like leukoplakia), "
  "<b>atrophic</b>, <b>erosive and bullous</b>, <b>ulcerative</b>, <b>annular</b>.",
  "Clinical, with biopsy where malignancy is a concern.",
  "Aimed at pain relief. Identify reversible contributors &mdash; medications, dental restorations, "
  "oral hygiene, tobacco and alcohol. Topical or oral corticosteroids; lidocaine, tacrolimus, "
  "cyclosporine.",
  "Urgent",
  "<b>1&ndash;4% progress to squamous cell carcinoma, and the risk is higher with ulcerative "
  "lesions</b> &mdash; which is why close follow-up is the point of the diagnosis.", "20&ndash;22", D19),

 ("Systemic lupus erythematosus &mdash; oral", ULC,
  "<b>40%</b> of patients with lupus &middot; oral lesions may be the <b>FIRST SIGN</b> &middot; "
  "<b>honeycomb</b> patches",
  "40% of patients with systemic lupus erythematosus have mucous membrane involvement, and "
  "<b>oral lesions may be the first sign of lupus</b>. Painful or painless, with <b>no correlation "
  "to systemic activity</b>. Lesions: cheilitis, erythematous patches, honeycomb patches, discoid "
  "and discrete ulcers. White plaques, erythematous areas and punched-out erosions with surrounding "
  "erythema on the soft and buccal mucosa.",
  "Clinical, with serology for the systemic disease.",
  "Photoprotection plus medication: topical or intralesional corticosteroids, topical calcineurin "
  "inhibitors, systemic glucocorticoids, and <b>systemic antimalarials &mdash; hydroxychloroquine "
  "or chloroquine</b>.",
  "Urgent",
  "The oral ulcers do not track disease activity, so they cannot be used to judge control.",
  "23&ndash;24", D19),

 ("Herpes simplex ulcers", ULC,
  "<b>Prodrome of burning and tingling ~24 h BEFORE the lesion</b> &middot; recurrence from the "
  "<b>trigeminal ganglion</b>",
  "Herpes simplex virus 1 and 2. <b>Herpetic gingivostomatitis is the commonest manifestation of "
  "primary infection</b> in children and young adults, with fever, malaise and cervical "
  "lymphadenopathy. <b>Secondary</b> disease is recurrence of dormant virus from the trigeminal "
  "ganglion, triggered by stress, trauma, immunosuppression or ultraviolet light. Small painful "
  "lesions that ulcerate, leaving an erythematous base with a grey cover; <b>heals without a "
  "scar</b>; resolves in 1&ndash;2 weeks.",
  "Clinical, but confirm with <b>polymerase chain reaction for HSV DNA &mdash; most sensitive and "
  "specific</b>. Serology with IgG and IgM distinguishes HSV 1 from HSV 2. <b>Tzanck smear shows "
  "multinucleated giant cells but is also positive in varicella zoster</b>, so it is not the best "
  "test.",
  "<b>Oral acyclovir</b> for treatment and prophylaxis.", "Routine",
  "The 24-hour prodrome is the window in which treatment works best, so patients are taught to "
  "recognise it.", "25&ndash;27", D19),

 ("Acute suppurative sialadenitis", SAL,
  "<b>PAROTID</b> swelling, firm and diffusely tender &middot; <b>PUS EXPRESSED FROM THE DUCT</b> "
  "&middot; dehydrated post-operative or elderly patient",
  "Bacterial infection of a salivary gland, beginning with stasis of salivary flow. Occurs in "
  "post-operative patients, elderly patients with chronic conditions, and children under 2 months. "
  "Risk factors: dehydration, trauma, immunosuppression, chemotherapy or radiation, age over 50, "
  "HIV, xerostomia, sialolithiasis, anorexia and bulimia. <b><i>Staphylococcus aureus</i> is the "
  "commonest pathogen</b>. The parotid is most commonly affected: unilateral, firm, diffusely "
  "tender, with overlying erythema, trismus, <b>purulent ductal discharge</b>, induration, fever "
  "and chills.",
  "Clinical is usually sufficient. If uncertain: culture, and ultrasound, computed tomography or "
  "magnetic resonance imaging to look for stones, abscess or gland inflammation.",
  "<b>Rehydration</b> plus intravenous antibiotics with penicillinase-resistant gram-positive cover "
  "(nafcillin or cefazolin), then oral (dicloxacillin, clindamycin). Warm compresses, massage, "
  "<b>sialogogues (lemon drops or vitamin C lozenges)</b>, oral hygiene. <b>No improvement in 48 "
  "hours means presume an abscess.</b>",
  "Urgent",
  "Submandibular disease that fails treatment <b>can mimic Ludwig angina</b>, which threatens the "
  "airway.", "34&ndash;39", D19),

 ("Sialolithiasis", SAL,
  "<b>Recurrent swelling and pain WORSE WITH EATING</b> (salivary colic) &middot; <b>80&ndash;90% "
  "SUBMANDIBULAR</b>",
  "Salivary calculi. Change in saliva viscosity, ductal injury or stagnation causes calcium "
  "phosphate and calcium carbonate to precipitate. <b>80&ndash;90% occur in the submandibular "
  "gland</b> &mdash; the duct runs a longer course, and the saliva has higher mucin, alkaline "
  "content, calcium and phosphate. 10&ndash;20% parotid. Commoner in men. Risk: long illness with "
  "dehydration, gout, diabetes, hypertension.",
  "Usually clinical. <b>Submandibular stones are calcium phosphate and hydroxyapatite, so they are "
  "RADIOPAQUE and visible on plain films.</b> Ultrasound shows an echogenic structure with acoustic "
  "shadow; <b>computed tomography is the most sensitive</b>; <b>digital subtraction sialography is "
  "the most accurate</b>. Stones may be palpable in the anterior two thirds of the duct.",
  "By location and size: intraoral extraction if palpable or visible anteriorly; gland excision for "
  "large stones in the hilum or body; <b>sialoendoscopy</b>, the minimally invasive option that can "
  "avoid removing the gland; lithotripsy. Conservative: hydration, hot compresses, massage, "
  "non-steroidal anti-inflammatories, lozenges.",
  "Routine",
  "Pain that arrives with the first mouthful and settles afterwards is the history that makes this "
  "diagnosis without any test.", "40&ndash;43", D19),

 ("Parotitis", SAL,
  "Painful parotid swelling &middot; <b>mumps (paramyxovirus)</b> is the classic viral cause",
  "Painful swelling of the parotid gland. Causes: viral &mdash; <b>mumps (paramyxovirus)</b>, "
  "herpes, Epstein-Barr virus &mdash; and also bacterial infection, diabetes, tumours, stones and "
  "dental problems.",
  "Clinical; serology where mumps is suspected.",
  "Directed at the cause.", "Routine",
  "It is a presentation, not a single disease &mdash; the work is deciding which of the causes it "
  "is.", "44", D19),

 ("Vocal cord nodules", VC,
  "<b>BILATERAL and SYMMETRIC</b> &middot; junction of the <b>anterior one third and posterior two "
  "thirds</b> &middot; vocal abuse",
  "Smooth, <b>paired</b> lesions at the junction of the anterior one third and posterior two thirds "
  "of the vocal folds, from vocal abuse. <b>The commonest cause of persistent dysphonia in children "
  "&mdash; screamers' nodules</b>, and a frequent cause of voice deterioration in professional "
  "singers &mdash; singers' nodules.",
  "<b>Laryngoscopy</b>: small, well-defined lesions with a whitish hue, <b>bilateral and "
  "symmetric</b>.",
  "<b>Speech therapy is first line in adults and children.</b> Photodocumentation in the voice "
  "clinic tracks progress; microlaryngoscopy if needed.",
  "Routine",
  "Bilateral and symmetric is the finding that separates nodules from a polyp, which is unilateral.",
  "46&ndash;47", D19),

 ("Vocal cord polyps", VC,
  "<b>UNILATERAL</b>, pedunculated &middot; men with vocal abuse and <b>heavy smoking</b>",
  "Unilateral masses forming within the superficial lamina propria of the vocal fold, commoner in "
  "men with a history of vocal abuse and heavy smoking. Fluid-filled and gelatinous, pedunculated, "
  "sometimes with visible vascular markings, at the point of maximal vibration.",
  "<b>Microlaryngoscopic examination with excision</b> &mdash; which both confirms the diagnosis and "
  "excludes other pathology.",
  "Excision of the polyp, with continued vocal rest and <b>smoking cessation</b>.",
  "Urgent",
  "<b>A large polyp may conceal an occult early laryngeal squamous cell carcinoma</b>, which is why "
  "it is excised rather than watched.", "48", D19),

 ("Vocal cord papillomatosis", VC,
  "<b>Warty exophytic growths</b> in the larynx &middot; <b>HPV 6 and 11</b> &middot; bimodal "
  "&mdash; ages 2&ndash;4 and the 30s",
  "Recurrent respiratory papillomatosis: benign, non-contagious, rare, with exophytic warty lesions "
  "usually in the larynx but also nose, pharynx and trachea. <b>Human papillomavirus subtypes 6 and "
  "11, rarely 16.</b> Bimodal: juvenile between 2 and 4 years, adult peaking in the 30s. Multiple "
  "friable irregular warty growths affecting true and false cords, at points of air turbulence and "
  "at the change from ciliary to squamous epithelium. <b>Glottic lesions cause dysphonia; "
  "supraglottic lesions cause stridor.</b>",
  "Laryngoscopy.",
  "<b>No curative measure for the virus</b> &mdash; the aim is removing symptomatic lesions with "
  "minimal morbidity: carbon dioxide laser resection, cold steel dissection, laryngeal "
  "microdebrider. <b>Avoid tracheostomy</b>, which introduces another squamociliary junction the "
  "papillomas favour. Adjuvant intralaryngeal cidofovir is off-label.",
  "Urgent",
  "<b>3&ndash;7% risk of malignant transformation.</b> Gardasil and Gardasil 9 offer eventual "
  "prevention.", "49&ndash;52", D19),

 ("Vocal cord paralysis", VC,
  "<b>Unilateral: hoarse BREATHY voice</b> &middot; <b>bilateral: STRIDOR</b> with a weak cry",
  "One or both folds fail to open or close properly. Causes: injury during surgery to thyroid, "
  "parathyroid, oesophagus, neck or chest; neck or chest injury; tumours; infections (Lyme disease, "
  "Epstein-Barr virus, herpes); neurological disease (stroke, multiple sclerosis, Parkinson "
  "disease). <b>Unilateral</b> gives hoarse breathy dysphonia, aspiration, dysphagia, vocal fatigue "
  "&mdash; and may be asymptomatic. <b>Bilateral</b> gives inspiratory or biphasic stridor, weak "
  "cry, aspiration.",
  "<b>Mirror laryngoscopy or flexible nasolaryngoscopy</b> plus a full neurological examination. "
  "Determine whether the lesion is the <b>recurrent laryngeal nerve or the vagus</b>, and whether "
  "it is unilateral or bilateral.",
  "Decide whether it is self-limiting or permanent. Observation with voice therapy; surgical "
  "medialisation of the affected fold, or thyroplasty.",
  "Urgent",
  "<b>Laryngeal electromyography predicts recovery</b>: a transected or tumour-infiltrated nerve "
  "will not recover, while a bruised or stretched one may return over 6 months to a year.",
  "53&ndash;56", D19),

 ("Acute laryngitis", VC,
  "<b>Commonest cause of hoarseness</b> &middot; persists about a week <b>after</b> the upper "
  "respiratory infection clears",
  "The commonest cause of hoarseness, persisting about a week after upper respiratory symptoms have "
  "cleared. Viral (<b>rhinovirus commonest</b>, parainfluenza, respiratory syncytial virus, "
  "adenovirus, influenza, pertussis), bacterial or fungal; also acid reflux, smoking, toxic "
  "inhalation, cough, vocal abuse, direct injury and allergy. Dysphonia, low-grade fever, "
  "hoarseness, cough, rhinitis and postnasal drip.",
  "Clinical.",
  "Conservative: hydration, antipyretics, <b>voice rest</b>, decongestants, humidification, smoking "
  "cessation. <b>Antibiotics are not indicated unless a secondary bacterial infection is "
  "suspected.</b>",
  "Routine",
  "Voice rest is the treatment patients most often skip and most need.", "57", D19),

 ("Chronic laryngitis", VC,
  "Voice disturbance <b>lasting more than 2 weeks</b> &middot; <b>NOT a true diagnosis</b> &mdash; "
  "work it up",
  "Voice disturbance lasting more than two weeks. <b>Not a true diagnosis</b> &mdash; always work up "
  "the underlying condition.",
  "<b>Refer to ear, nose and throat for laryngoscopy.</b> <b>Laryngeal cancer and vocal cord polyps "
  "must be considered.</b>",
  "Treat what the laryngoscopy finds.", "Urgent",
  "Two weeks of hoarseness is the threshold at which a smoker gets scoped, not reassured.",
  "58", D19),

 ("Epiglottitis (supraglottitis)", AIR,
  "<b>ENT EMERGENCY</b> &middot; the <b>4 Ds</b> in children &mdash; Drooling, Dysphagia, "
  "Dysphonia, Distress &middot; <b>TRIPOD position</b>",
  "More correctly supraglottitis: cellulitis involving multiple areas of the supraglottis. Acute "
  "disease presents in children aged 2 to 6, though any age can be affected. <b>Commonest pathogen "
  "is <i>Haemophilus influenzae</i> type B</b> &mdash; incidence has fallen over 90% since the "
  "vaccine. Others: <i>Streptococcus pneumoniae</i>, <i>Staphylococcus aureus</i>, beta-haemolytic "
  "streptococci. <b>Children: the 4 Ds</b>. Adults: severe sore throat, dysphagia, odynophagia, "
  "fever, dyspnoea, cough; muffled voice, stridor and drooling in under 10%. Sudden onset "
  "progressing over hours in children, more slowly in adults. Classic picture is an irritable "
  "patient <b>sitting or leaning forward, neck hyperextended, chin thrust forward</b>. "
  "<b>Inspiratory stridor is a LATE finding</b> &mdash; the airway is nearly obstructed.",
  "<b>Once suspected, do NOT perform an intraoral examination or venipuncture</b> &mdash; the "
  "anxiety they cause may complete the obstruction. Lateral neck X-ray shows the <b>&ldquo;thumb "
  "print&rdquo; sign</b>, but is <b>not necessary for diagnosis</b>. <b>Mirror or fiberoptic "
  "laryngoscopy is the gold standard.</b>",
  "Airway, antibiotics, prevention. <b>Paediatric: to theatre</b> for rigid bronchoscopy and "
  "emergency tracheotomy standby; inhalation anaesthesia, confirm the diagnosis, secure the airway "
  "by intubation; blood cultures and supraglottic swab; parenteral antibiotics &mdash; extubation is "
  "often possible within 48 to 72 hours. <b>Adult:</b> observation, intubation or tracheostomy if "
  "the airway obstructs, humidification, glucocorticoids, intravenous antibiotics, nebulised "
  "adrenaline. <b>Third-generation cephalosporin plus an antistaphylococcal agent</b> &mdash; "
  "ceftriaxone or cefotaxime with vancomycin for 7&ndash;10 days.",
  "Emergent",
  "The mortality is what justifies the caution: rare, but high if it is not recognised and treated "
  "promptly.", "60&ndash;67", D19),

 ("Viral pharyngitis", PHA,
  "<b>70% of pharyngitis</b> &middot; <b>COUGH, rhinitis, conjunctivitis</b> &middot; "
  "<b>herpangina</b> &mdash; ulcerative vesicles over the tonsils",
  "70% of pharyngitis. Adenovirus, Epstein-Barr virus, herpes simplex, HIV, influenza, "
  "parainfluenza, rhinovirus, coronavirus, echovirus, enteroviruses, coxsackievirus. Sore throat "
  "with earache or headache, <b>cough</b>, rhinitis, laryngitis, hoarseness, fever, "
  "<b>conjunctivitis</b>, lymphadenopathy. <b>Herpangina</b> is ulcerative vesicles over the "
  "tonsils.",
  "<b>Clinical &mdash; no further testing.</b>",
  "Supportive: hydration, antipyretics, analgesia.", "Routine",
  "The presence of cough and coryza is what argues against streptococcal disease, and it is a "
  "Centor point.", "70, 72", D19),

 ("Bacterial pharyngitis (GABHS)", PHA,
  "<b>Group A beta-haemolytic <i>Streptococcus</i></b> &middot; fever, exudate, tender nodes and "
  "<b>NO COUGH</b>",
  "30% of pharyngitis; the commonest bacterial cause is <b>group A beta-haemolytic "
  "<i>Streptococcus</i></b>. Common in adolescents and children but <b>not under 3 years</b>. Peaks "
  "in winter and spring; droplet spread; incubation 2&ndash;5 days. <b>Fever above 100.4&nbsp;&deg;F, "
  "sore throat, cervical lymphadenopathy, dysphagia, odynophagia, LACK OF COUGH, abdominal "
  "pain.</b> Tonsillar and pharyngeal erythema with purulent exudate.",
  "<b>Rapid antigen detection test</b>; <b>a negative rapid test is always confirmed with a throat "
  "culture</b>. <b>Definitive test is antistreptolysin O</b>, useful because carriers have a "
  "positive culture while asymptomatic. <b>Centor criteria</b> (slide 76): age 3&ndash;14 "
  "<b>+1</b>, age 15&ndash;44 <b>0</b>, age 45 or over <b>&minus;1</b>; absence of cough <b>+1</b>; "
  "tonsillar exudate <b>+1</b>; fever <b>+1</b>; tender anterior cervical lymphadenopathy <b>+1</b>.",
  "Symptomatic care plus antibiotics: <b>penicillin VK for 10 days</b>, or amoxicillin. "
  "<b>Intramuscular penicillin G</b> if compliance or oral intake is a concern. Mild penicillin "
  "allergy: cephalexin or cefadroxil. Severe allergy: macrolides or clindamycin.",
  "Urgent",
  "Treatment is as much about preventing rheumatic fever as about the sore throat.",
  "73&ndash;77", D19),

 ("Rheumatic fever", PHA,
  "<b>Sequela of untreated GABHS</b> &middot; appears <b>2&ndash;3 weeks</b> after &middot; peak "
  "ages <b>5&ndash;15</b>",
  "A rare complication of untreated group A beta-haemolytic streptococcal infection, from "
  "<b>cross-reactive antibodies</b> produced against the streptococcus that attack heart muscle "
  "&mdash; endocarditis, myocarditis or pericarditis. Signs appear <b>2 to 3 weeks after the "
  "infection</b>, sometimes as early as one week or as late as five. <b>Peak incidence between 5 "
  "and 15 years</b>; rare before 4 and after 40. Typically resolves after about six weeks.",
  "Clinical, against the <b>Jones criteria</b> (slide 79), with evidence of preceding streptococcal "
  "infection.",
  "Treat and eradicate the streptococcal infection; manage the carditis.", "Urgent",
  "This is the reason a sore throat gets an antibiotic at all &mdash; the throat would settle "
  "without one.", "78&ndash;79", D19),

 ("Chronic pharyngitis", PHA,
  "<b>Constant throat clearing</b> &middot; <b>thickened, granular</b> pharyngeal wall with crusting",
  "Causes: postnasal drip from chronic rhinosinusitis, irritants (dust, dry heat, chemicals, "
  "smoking, alcohol), chronic mouth breathing, voice abuse, allergy, granulomatous disease, "
  "connective tissue disorder, malignancy. Constant throat clearing, dry throat, odynophagia, a "
  "thickened and granular pharyngeal wall, and pharyngeal crusting.",
  "Clinical; culture and biopsy if treatment fails.",
  "Address the underlying disorder, avoid precipitants, treat symptoms.", "Routine",
  "Malignancy is on the causes list, so failed therapy earns a biopsy rather than another course of "
  "something.", "80", D19),

 ("Infectious mononucleosis", PHA,
  "<b>Triad: fever, tonsillar pharyngitis, cervical lymphadenopathy</b> &middot; <b>15&ndash;24 "
  "years</b> &middot; <b>splenomegaly</b>",
  "Highly contagious; <b>90&ndash;95% of adults are Epstein-Barr virus seropositive</b>. Commonly "
  "15 to 24 years. Spread by oral contact or infected saliva. <b>Epstein-Barr virus in 90%</b>, "
  "cytomegalovirus and others in 10%. Prodrome of malaise, headache and low-grade fever &mdash; or "
  "asymptomatic under 10 years. <b>Triad of fever, tonsillar pharyngitis with or without exudate, "
  "and cervical lymphadenopathy.</b> Also palatal petechiae, hepatomegaly, <b>splenomegaly</b>, and "
  "a maculopapular rash in 5%.",
  # SLIDE 84 IS WRONG AND WE ARE DELIBERATELY NOT COPYING IT. It reads "can be
  # falsely POSITIVE if early in the illness (first week)". Heterophile
  # antibodies take about a week to appear, so an early test is falsely
  # NEGATIVE -- and the slide contradicts itself twice proving it: the line
  # above says "if positive, no need for further testing" (which cannot hold
  # if positives were unreliable), and the serology line below says serology
  # is for a "negative heterophile antibody test (& highly suspicious of
  # mono)", which IS the false-negative pathway. Jaxon spotted it 2026-09-09
  # and it was corrected in class the same morning: Shah read the slide as
  # written, a student asked "is that supposed to say can be false negative
  # temporarily?", and she confirmed -- "Yes. I'm sorry... I'll send that over."
  # A corrected slide is therefore expected from her; re-check this row when it
  # arrives. The exchange is at the very end of the mono block, in audio that
  # only exists because the lecture was re-pulled after recording finished --
  # the first capture stopped at 10:02 and contained no instance of the word
  # "false" at all.
  "Clinical plus confirmation. <b>Monospot / heterophile antibody test</b> is very sensitive and "
  "specific &mdash; positive means no further testing, but it can be <b>falsely negative in the "
  "first week</b>, because heterophile antibodies take about a week to develop. "
  "<b>Slide 84 prints &ldquo;falsely positive&rdquo;, which is an error.</b> Prof. Shah read it "
  "as written, a student asked &ldquo;is that supposed to say can be false negative?&rdquo;, and "
  "she confirmed it &mdash; <b>&ldquo;Yes. I&rsquo;m sorry&hellip; I&rsquo;ll send that "
  "over&rdquo;</b>, so a corrected slide is coming. The same slide already contradicts itself: "
  "it sends you to serology for a <i>negative</i> heterophile test in suspected mono, which is "
  "the false-negative pathway. "
  "Serology: <b>IgG means past infection, IgM means "
  "current</b>; useful under 4 years, with a negative heterophile test, or with atypical "
  "symptoms. Polymerase chain reaction detects viral DNA.",
  "Supportive &mdash; there is no antiviral therapy. Corticosteroids for severe respiratory "
  "compromise. <b>Avoid heavy lifting and contact sports for about a month, until the splenomegaly "
  "has resolved</b>, to prevent splenic rupture.",
  "Urgent",
  "<b>Giving penicillin triggers an exanthem</b> &mdash; the classic sequence is a sore throat "
  "treated as strep, a rash, and then the real diagnosis.", "81&ndash;87", D19),

 ("Diphtheria", PHA,
  "<b>Tenacious GREY MEMBRANE</b> over tonsils and pharynx &middot; unimmunised child",
  "<i>Corynebacterium diphtheriae</i>, attacking the respiratory tract and sometimes mucous "
  "membrane or skin wounds, spread by respiratory secretions. Nasal, laryngeal, <b>pharyngeal "
  "(commonest)</b> and cutaneous forms. Common in unimmunised children over 6 years. Nasal: "
  "discharge. Laryngeal: upper airway and bronchial obstruction. <b>Pharyngeal: a tenacious grey "
  "membrane covering tonsils and pharynx</b>, with mild sore throat, fever, malaise, toxaemia and "
  "prostration. Complications: <b>myocarditis</b> (arrhythmia, heart block, failure) and "
  "<b>neuropathy involving cranial nerves first</b> &mdash; diplopia, slurred speech, difficulty "
  "swallowing.",
  "Clinical, confirmed by culture. Differentiate from streptococcal pharyngitis, mononucleosis, "
  "adenovirus, herpes simplex and candidiasis.",
  "Laryngoscopy or bronchoscopy to prevent or relieve obstruction. <b>Antitoxin for all &mdash; "
  "obtained from the Centers for Disease Control.</b> Penicillin 250&nbsp;mg four times daily or "
  "erythromycin 500&nbsp;mg four times daily <b>for 14 days</b>. <b>Isolate until three consecutive "
  "cultures after therapy are negative.</b> Treat contacts with erythromycin for 7 days.",
  "Emergent",
  "Prevention is immunisation: childhood schedule plus boosters, and <b>Tdap in every pregnancy "
  "between 27 and 36 weeks</b>.", "112&ndash;114", D19),

 ("Oral candidiasis (thrush)", LES,
  "<b>Creamy white curd-like patches that WIPE OFF</b>, leaving an erythematous base",
  "<i>Candida albicans</i>; <i>Aspergillus</i> may also be cultured. Common in infants and the "
  "immunosuppressed. Risk factors: dentures, poor oral hygiene, diabetes, anaemia, chemotherapy or "
  "local irradiation, corticosteroids, broad-spectrum antibiotics, age, HIV. Creamy white curd-like "
  "patches on an erythematous base, painful, granular, usually on buccal mucosa and tongue, with "
  "fever, lymphadenopathy, odynophagia and taste change.",
  "Clinical. <b>Potassium hydroxide preparation shows spores and pseudohyphae.</b>",
  "Saline and peroxide washes; topical antifungals &mdash; nystatin suspension, clotrimazole, "
  "ketoconazole, fluconazole. HIV patients may need longer fluconazole; refractory disease needs "
  "itraconazole or voriconazole.",
  "Routine",
  "<b>The patches rub off with a tongue depressor.</b> Leukoplakia and lichen planus do not &mdash; "
  "that single manoeuvre separates three diagnoses.", "88&ndash;90", D19),

 ("Cervical adenitis", DEEP,
  "<b>A SIGN, NOT A DIAGNOSIS</b> &middot; typically <b>unilateral, solitary, anterior</b> node",
  "Inflammation of a lymph node, often used synonymously with lymphadenopathy. <b>Cervical "
  "lymphadenopathy is a sign, not a diagnosis.</b> Infectious causes include toxoplasmosis, "
  "tuberculosis, brucellosis, primary herpes simplex, syphilis, cytomegalovirus, HIV, "
  "histoplasmosis and chickenpox; also inflammatory, degenerative and neoplastic causes. The typical "
  "case is a <b>unilateral, solitary, anterior cervical node</b>: about <b>70% beta-haemolytic "
  "streptococcus, 20% staphylococcus including MRSA, 10% viruses, atypical mycobacteria and "
  "<i>Bartonella henselae</i></b>.",
  "Response to specific antibiotics can help confirm or exclude. <b>Fine needle aspiration if the "
  "node persists or keeps enlarging</b> &mdash; that can signal malignancy. Describe size, shape, "
  "<b>mobility (immobile suggests malignancy)</b>, consistency and tenderness "
  "(<b>tender = inflammatory, non-tender = malignancy</b>).",
  "<b>Treat the underlying cause.</b> Incision and drainage if there is an abscess.",
  "Urgent",
  "Scarred nodes may stay palpable long after the infection has gone, which is not failure.",
  "91&ndash;94", D19),

 ("Peritonsillar abscess (quinsy)", DEEP,
  "<b>Classic triad: TRISMUS, UVULAR DEVIATION, DYSPHONIA</b> &middot; <b>&ldquo;hot potato&rdquo; "
  "voice</b>",
  "Purulence between the capsule of the palatine tonsil and the pharyngeal muscles, beginning as a "
  "complication of untreated strep throat or tonsillitis. <b>The commonest deep infection of the "
  "head and neck</b>, especially in young adults, adolescents and children; commoner in males. "
  "Aerobes: group A beta-haemolytic streptococcus, <i>Staphylococcus aureus</i>, "
  "<i>Haemophilus influenzae</i>. Anaerobes: <i>Prevotella</i>, <i>Porphyromonas</i>, "
  "<i>Fusobacterium</i>, <i>Streptococcus</i>. Severe sore throat, fever, odynophagia, medial "
  "deviation of the soft palate and peritonsillar fold, uvular deviation, hot potato voice, "
  "trismus, dysphagia.",
  "Clinical, confirmed by the purulent drainage obtained. Contrast computed tomography shows the "
  "extent; <b>ultrasound distinguishes abscess from cellulitis</b> and can guide needle aspiration.",
  "<b>Secure the airway first if needed.</b> Needle aspiration and incision and drainage. "
  "Antibiotics: parenteral amoxicillin-clavulanate or clindamycin, adding MRSA cover if severe; "
  "oral if tolerated. <b>Tonsillectomy for recurrent tonsillitis and recurrent abscesses</b>, "
  "usually after the acute infection settles &mdash; <b>quinsy tonsillectomy</b> during infection "
  "is occasional.",
  "Emergent",
  "<b>Trismus is the most reliable symptom</b>; the dysphonia comes from vagus nerve involvement "
  "failing to elevate the palate.", "96&ndash;101", D19),

 ("Retropharyngeal abscess", DEEP,
  "<b>SURGICAL EMERGENCY</b> &middot; child under 5 &middot; <b>widened retropharyngeal space</b> "
  "on lateral neck X-ray",
  "An abscess in the retropharyngeal space, running from the base of skull to the posterior "
  "mediastinum. May spread from a peritonsillar abscess or from a node in that space. <b>Commoner "
  "in children under 5</b> after upper respiratory infection, otitis media or sinusitis; in adults "
  "it follows intraoral procedures, trauma, foreign bodies such as fishbone, immunocompromise or "
  "odontogenic spread. Group A beta-haemolytic streptococcus, <i>Staphylococcus aureus</i>, "
  "<i>Haemophilus influenzae</i>, mixed flora. Early: fever, sore throat, pharyngeal erythema, "
  "dysphagia, odynophagia, neck stiffness, trismus. Late: ill appearance, drooling, <b>leaning "
  "forward with the neck extended</b>, respiratory distress.",
  "Labs; <b>lateral neck X-ray shows a widened retropharyngeal space</b>; <b>lateral neck computed "
  "tomography is the gold standard</b>, showing a rim-enhancing hypodense collection. Distinguishing "
  "abscess from adenitis is the point.",
  "<b>Protect the airway. Surgical emergency.</b> Antibiotics covering streptococci, anaerobes and "
  "<i>Staphylococcus aureus</i>: ampicillin-sulbactam, or clindamycin with ceftriaxone; vancomycin "
  "or linezolid if not improving; switch to oral on clinical improvement.",
  "Emergent",
  "<b>Mediastinitis carries 50% mortality.</b> Other complications: respiratory distress, rupture "
  "with aspiration pneumonia, and spread into the danger space, which is continuous left to right "
  "and leads directly to the thorax.", "103&ndash;107", D19),

 ("Ludwig angina", DEEP,
  "<b>EMERGENCY</b> &middot; floor of mouth, submental, sublingual and submandibular spaces "
  "&middot; <b>TONGUE PUSHED UP AND BACK</b>",
  "A severe infection of the floor of the mouth and the submental, sublingual and submandibular "
  "spaces. <b>Can rapidly compromise the upper airway and force a surgical airway.</b> Streptococci, "
  "staphylococci, <i>Bacteroides</i>, <i>Fusobacterium</i>, <i>Klebsiella</i> &mdash; the last "
  "usually in patients with diabetes, who have a more aggressive course. Oedema and erythema of the "
  "upper neck under the chin and the floor of the mouth; <b>the tongue is displaced upwards and "
  "backwards</b> by posterior spread of cellulitis; pus coalescing at the floor of the mouth.",
  "<b>Computed tomography with contrast</b>, to separate inflammation and phlegmon from abscess and "
  "define the extent for the surgeon.",
  "Antibiotics: penicillin with metronidazole, ampicillin-sulbactam, clindamycin, or selected "
  "cephalosporins. <b>External drainage via bilateral submental incision</b> if the airway is "
  "threatened or medical therapy fails. <b>Dental consultation</b> to deal with the offending "
  "tooth.",
  "Emergent",
  "It is usually odontogenic, which is why the dental referral is part of the treatment rather than "
  "an afterthought.", "108&ndash;111", D19),

 ("Dental abscess", DENT,
  "Pus <b>inside the tooth or gums</b> &middot; from bacterial infection of the <b>soft pulp</b>",
  "A build-up of pus inside the teeth or gums, from bacterial infection accumulating in the soft "
  "pulp of the tooth. Slide 116 divides them into <b>periapical</b> (at the root tip), "
  "<b>gingival</b> (in the space between gum and tooth), <b>periodontal</b> (in a periodontal "
  "pocket) and <b>pericoronal</b> (around an impacted or partially erupted tooth).",
  "Clinical, with dental imaging.",
  "Antibiotics &mdash; amoxicillin, ampicillin-sulbactam, amoxicillin-clavulanate, azithromycin, "
  "clindamycin, erythromycin, cephalexin, metronidazole, penicillin VK. Incision and drainage. "
  "<b>Root canal if the tooth can be restored; extraction with curettage of apical tissue if it "
  "cannot.</b>",
  "Urgent",
  "Untreated, infection from a tooth can spread to the jaw, the brain or the sinus &mdash; and "
  "Ludwig angina is the neck version of that spread.", "116&ndash;117", D19),

 ("Gingivitis and periodontitis", DENT,
  "<b>Gums erythematous, oedematous and BLEED EASILY</b> with little discomfort &middot; "
  "<b>gingivitis is REVERSIBLE</b>",
  "Chronic infection of the gingiva beginning with bacterial plaque at the gum line. "
  "<b>Gingivitis</b> is the mildest form: erythematous, oedematous gums that bleed easily, with "
  "little or no discomfort, caused by inadequate oral hygiene &mdash; and <b>reversible with "
  "professional treatment and good home care</b>. Untreated it becomes <b>periodontitis</b>: plaque "
  "spreads below the gum line, bacterial toxins provoke a chronic inflammatory response in which "
  "the body turns on itself, gums separate from teeth, pockets form and become infected, the "
  "periodontal ligament and bone are destroyed, and teeth loosen and fall out. Risk: diabetes, "
  "smoking, ageing, genetics, stress, poor nutrition, puberty, pregnancy, substance abuse, HIV and "
  "certain medications. Gram-negative organisms.",
  "Clinical and dental examination.",
  "Professional cleaning and oral hygiene &mdash; brushing, flossing, mouthwash &mdash; and "
  "modifying risk.",
  "Routine",
  "<b>Periodontal disease and dental caries are the primary causes of tooth loss.</b> The slides "
  "also link gum disease to endocarditis risk, pneumonia, osteoporosis and, in men, kidney, "
  "pancreatic and blood cancers.", "118&ndash;122", D19),

 ("Dental caries, pulpitis and periapical abscess", DENT,
  "<b>Tooth decay is the commonest cause</b>; injury second &middot; severe inflammation kills the "
  "pulp",
  "Common teeth diseases are cavities, pulpitis, periapical abscess, impacted teeth and "
  "malocclusion. <b>The commonest cause of pulpitis and periapical abscess is tooth decay, and the "
  "second commonest is injury.</b> Mild inflammation, if relieved, may not damage the pulp "
  "permanently; severe inflammation kills it. Pulpitis can lead to a pocket of pus at the root "
  "&mdash; a periapical abscess.",
  "Clinical and dental imaging.",
  "Dental treatment of the decay; root canal or extraction as for dental abscess.", "Urgent",
  "<b>Untreated, infection from a tooth can spread to the jaw or beyond &mdash; brain or "
  "sinus.</b>", "123&ndash;124", D19),

 ("Impacted teeth", DENT,
  "<b>Overcrowding</b> &middot; <b>wisdom teeth</b> are the usual ones &middot; more likely to "
  "become infected",
  "Impaction is usually caused by overcrowding and insufficient room for a new tooth to emerge. "
  "<b>Wisdom teeth are the usual culprits</b>, being the last permanent teeth to erupt into a jaw "
  "that may not accommodate them. Impacted teeth are more likely to become infected.",
  "Clinical and dental imaging.",
  "Usually removed &mdash; they are of little use in chewing.", "Routine",
  "A pericoronal abscess is the complication that links this row to the dental abscess row.",
  "125", D19),

 ("Malocclusion", DENT,
  "<b>Abnormal alignment</b> of teeth and bite &middot; <b>Class I, II and III</b>",
  "Abnormal alignment of the teeth and the way upper and lower teeth fit together. Normal chewing "
  "produces about <b>150&nbsp;lb of force on the molars, and about 250&nbsp;lb when clenching "
  "during sleep</b>; if that force is unevenly distributed, teeth wear, fracture or loosen. Causes: "
  "size mismatch between jaw and teeth, thumb sucking or tongue thrusting, lost teeth, birth "
  "defects. Slide 126 illustrates <b>Class I normal occlusion, Class II distal occlusion and Class "
  "III mesial occlusion</b>.",
  "Clinical and dental assessment.",
  "Braces or aligners, removal of teeth, or surgery.", "Routine",
  "The force numbers are the reason a bite problem becomes a structural one.", "126", D19),

 ("Temporomandibular joint disorders", JAW,
  "<b>Second commonest musculoskeletal cause of pain and disability</b> &middot; jaw pain with "
  "<b>clicking, popping or locking</b>",
  "Disorders affecting the temporomandibular joint, the masticatory muscles, or both. <b>The second "
  "commonest musculoskeletal condition causing pain and disability.</b> Common in women of "
  "childbearing age, with a possible link to female sex hormones. Predisposing: trauma &mdash; a "
  "blow to the jaw or whiplash &mdash; and stress, which disrupts sleep and increases nocturnal "
  "bruxism. Perpetuated by stress, poor coping, clenching and grinding, and poor posture. <b>Three "
  "categories: myofascial pain, internal derangement (displaced disc, dislocated jaw, condylar "
  "injury), and arthritis.</b> Jaw, face and head pain; limited opening, catching or locking; "
  "clicking, popping or grating; headache, neck and shoulder pain; tinnitus, ear fullness, hearing "
  "loss, dizziness; abnormal tooth wear and sensitivity.",
  "Clinical. <b>Computed tomography or magnetic resonance imaging is reserved</b> for abnormal pain "
  "or dysfunction not responding to short-term therapy, or a sudden change in bite or mandibular "
  "asymmetry.",
  "Eliminate pain and restore function: self care; non-steroidal anti-inflammatories, muscle "
  "relaxants (cyclobenzaprine), low-dose tricyclics (amitriptyline, desipramine, nortriptyline); "
  "oral steroids if there is synovitis; physical therapy, transcutaneous electrical nerve "
  "stimulation, acupuncture, local anaesthesia, mouth guards, arthrocentesis, arthroscopy, surgery.",
  "Routine",
  "The ear symptoms are the trap &mdash; tinnitus, fullness and dizziness send these patients to an "
  "ear examination that is normal.", "128&ndash;131", D19),

 ("Oral leukoplakia", LES,
  "<b>White lesion that CANNOT be scraped off</b> &middot; premalignant &mdash; <b>5&ndash;20% "
  "become squamous cell carcinoma</b>",
  "A premalignant squamous lesion: altered epithelium at increased risk of progression to squamous "
  "cell carcinoma, <b>5&ndash;20%</b>. Defined as a white lesion of the oral mucosa that <b>cannot "
  "be scraped off</b> and cannot be attributed to another definable lesion. Causes include chronic "
  "irritation, smoking and infection.",
  "<b>Excisional biopsy to rule out malignancy.</b> Complete intraoral examination and palpation for "
  "lymphadenopathy.",
  "Observation after eliminating carcinogenic irritants &mdash; smoking, chewing tobacco, alcohol "
  "&mdash; with <b>serial biopsies and excisions</b>.",
  "Urgent",
  "The scrape test is the bedside discriminator: candidiasis wipes off, leukoplakia does not.",
  "133&ndash;134", D19),

 ("Erythroplakia", LES,
  "Like leukoplakia but <b>RED</b> &middot; <b>90% are dysplastic or carcinoma</b> &middot; far "
  "more dangerous",
  "As leukoplakia but with an erythematous component. <b>90% are either dysplastic or already "
  "carcinoma</b>, and the risk of malignancy is around 25% &mdash; substantially higher than "
  "leukoplakia. Alcohol and tobacco are the major risk factors.",
  "As for leukoplakia &mdash; <b>excisional biopsy</b>.",
  "As for leukoplakia, but the threshold for excision is lower.", "Emergent",
  "Red is worse than white. If one lesion on the slide deck earns urgency, it is this one.",
  "133, 135", D19),

 ("Hairy leukoplakia", LES,
  "<b>Painless LATERAL TONGUE</b> lesion that <b>waxes and wanes</b> &middot; <b>EBV</b> &middot; "
  "strongly associated with <b>HIV</b>",
  "Benign mucosal hyperplasia associated with Epstein-Barr virus, long-term systemic corticosteroids "
  "and solid organ transplantation. <b>Strongly associated with HIV and a common early finding in "
  "HIV infection.</b> Painless lateral tongue lesions that wax and wane over time.",
  "Clinical and biopsy.",
  "Observation. Acyclovir, valacyclovir or famciclovir produce <b>temporary</b> resolution.",
  "Urgent",
  "The lesion itself is benign; its value is as a pointer to undiagnosed HIV.", "136", D19),

 ("Salivary gland neoplasm", ONEO,
  "<b>Slow-growing PAINLESS mass at the TAIL OF THE PAROTID</b> &middot; the smaller the gland, the "
  "likelier it is malignant",
  "<b>64&ndash;80% arise in the parotid, and 75&ndash;80% of those are benign.</b> 7&ndash;15% "
  "submandibular, 50&ndash;60% benign. 1% sublingual. About 15% are minor salivary gland, and only "
  "<b>35% of those are benign</b>. Most benign parotid tumours are epithelial; in minor glands the "
  "commonest is <b>pleomorphic adenoma</b>, then basal cell adenoma. Malignant disease is 3&ndash;4% "
  "of head and neck malignancy; <b>mucoepidermoid carcinoma is the commonest</b>, and in minor "
  "glands adenoid cystic carcinoma and adenocarcinoma. <b>No specific risk factors are known.</b> "
  "Benign parotid tumours are slow-growing painless masses often at the tail of the parotid.",
  "<b>Fine needle aspiration is less specific and sensitive here than for other tumours</b>, though "
  "it helps separate malignant from benign. Diffusion-weighted magnetic resonance imaging or "
  "computed tomography helps with deep lobe tumours.",
  "<b>Benign: complete surgical excision, no radiation.</b> <b>Malignant: surgical removal, "
  "radiotherapy for T1 and T2, palliative chemotherapy.</b> Complications include recurrence with "
  "positive margins and <b>transient or permanent facial paralysis</b>.",
  "Urgent",
  "Prognosis is poor with pain, facial or other nerve involvement, high-grade histology, skin or "
  "tissue invasion, or recurrent disease.", "139&ndash;143", D19),

 ("Oral cavity and oropharyngeal cancer", ONEO,
  "<b>NON-HEALING ULCER</b> &middot; tobacco and alcohol &middot; <b>referred otalgia</b> and "
  "ill-fitting dentures in advanced disease",
  "Oral cavity means the anterior two thirds of tongue, buccal mucosa, floor of mouth, hard palate, "
  "upper and lower gingiva and retromolar trigone &mdash; <b>the lip is no longer part of the oral "
  "cavity under the 8th staging system</b>. Oropharynx means posterior third of tongue, palatine "
  "tonsil, soft palate and posterior pharyngeal wall. Males are 2&ndash;4 times more likely for oral "
  "cavity and 3&ndash;5 times for oropharyngeal. <b>60&ndash;80% of oropharyngeal cancer is human "
  "papillomavirus related</b>; 90% of oral cavity cases relate to chronic sun exposure. Mean age 62. "
  "Risks: tobacco chewed and smoked, alcohol, betel nut, poor oral hygiene, immunosuppression. "
  "<b>Squamous cell carcinoma is commonest</b>; lymphoma is the second commonest tumour of the "
  "tonsillar fossa. Non-healing ulcers, bleeding, pain, ill-fitting dentures; advanced: dysarthria, "
  "dysphagia, neck mass, <b>referred otalgia</b> from cranial nerve involvement; tonsillar lesions "
  "give odynophagia and trismus.",
  "Labs including <b>high-risk human papillomavirus testing and in situ hybridisation</b>; computed "
  "tomography or magnetic resonance imaging for the primary and nodes; chest X-ray and positron "
  "emission tomography for metastases; flexible fiberoptic endoscopy; <b>biopsy</b>; dental "
  "evaluation.",
  "<b>Surgical resection alone for oral cavity; resection plus radiotherapy for oropharyngeal</b>, "
  "where radiotherapy gives better functional outcomes.",
  "Emergent",
  "Prevention is tobacco and alcohol cessation. An ulcer that has not healed is the symptom that "
  "should never be watched.", "144&ndash;148", D19),
]

# (does it hurt, where it sits, the finding that names it)
DIFF_L19 = {
 "Leukoedema": ("No", "Buccal mucosa", "<b>Disappears when the mucosa is stretched</b>"),
 "Fordyce granules": ("No", "Vermilion of lip, buccal mucosa", "Yellow-white papules &mdash; ectopic sebaceous glands"),
 "Physiologic pigmentation": ("No", "Gingiva and mucosa", "Symmetrical melanin pigmentation, a normal variant"),
 "Aphthous stomatitis (canker sores)": ("Yes &mdash; painful", "<b>Non-keratinised, freely moving</b> mucosa", "<b>Yellow-grey fibrinoid centre with a red halo</b>"),
 "Behcet syndrome": ("Yes", "Oral and <b>genital</b>", "Oral ulcers in up to 100%, genital in 75%"),
 "Oral lichen planus": ("Varies &mdash; erosive types hurt", "Buccal mucosa, tongue, lips", "<b>Wickham striae</b> &mdash; lacy white lines"),
 "Systemic lupus erythematosus &mdash; oral": ("Varies", "Lips, soft and buccal mucosa", "<b>Honeycomb patches</b>; may be the first sign of lupus"),
 "Herpes simplex ulcers": ("Yes", "Perioral and oral, <b>keratinised</b> surfaces", "<b>Burning prodrome ~24 h before the lesion</b>"),
 "Acute suppurative sialadenitis": ("Yes &mdash; firm, diffusely tender", "<b>Parotid</b>, unilateral", "<b>Pus expressed from the duct</b>"),
 "Sialolithiasis": ("Yes &mdash; with eating", "<b>Submandibular duct</b> in 80&ndash;90%", "<b>Salivary colic</b> &mdash; swelling and pain on eating"),
 "Parotitis": ("Yes", "Parotid", "Mumps is the classic viral cause"),
 "Vocal cord nodules": ("No", "<b>Anterior third / posterior two thirds junction</b>", "<b>Bilateral and symmetric</b>"),
 "Vocal cord polyps": ("No", "Superficial lamina propria, one fold", "<b>Unilateral</b> and pedunculated"),
 "Vocal cord papillomatosis": ("No", "True and false cords", "<b>Warty exophytic growths</b>; HPV 6 and 11"),
 "Vocal cord paralysis": ("No", "One or both folds", "<b>Unilateral breathy voice; bilateral stridor</b>"),
 "Acute laryngitis": ("Mild", "Larynx", "Hoarseness persisting a week after the cold clears"),
 "Chronic laryngitis": ("No", "Larynx", "<b>Over 2 weeks</b> &mdash; scope it, do not treat it"),
 "Epiglottitis (supraglottitis)": ("Severe &mdash; odynophagia", "Supraglottis", "<b>Tripod position, drooling, muffled voice</b>; thumbprint sign"),
 "Viral pharyngitis": ("Yes &mdash; sore throat", "Pharynx", "<b>Cough, rhinitis and conjunctivitis</b> alongside"),
 "Bacterial pharyngitis (GABHS)": ("Yes", "Tonsils and pharynx", "<b>Exudate, fever, tender nodes and NO cough</b>"),
 "Rheumatic fever": ("Varies", "Heart, joints, skin", "<b>2&ndash;3 weeks after an untreated strep throat</b>"),
 "Chronic pharyngitis": ("Mild", "Pharyngeal wall", "<b>Thickened, granular</b> wall with crusting"),
 "Infectious mononucleosis": ("Yes", "Tonsils and cervical nodes", "<b>Fever, tonsillar pharyngitis, cervical adenopathy</b> plus splenomegaly"),
 "Diphtheria": ("Mild sore throat", "Tonsils and pharynx", "<b>Tenacious grey membrane</b>"),
 "Oral candidiasis (thrush)": ("Yes", "Buccal mucosa and tongue", "<b>White patches that RUB OFF</b>"),
 "Cervical adenitis": ("Varies &mdash; tender means inflammatory", "Anterior cervical node", "Unilateral solitary node; <b>immobile suggests malignancy</b>"),
 "Peritonsillar abscess (quinsy)": ("Severe", "Between tonsil capsule and pharyngeal muscle", "<b>Trismus, uvular deviation, hot potato voice</b>"),
 "Retropharyngeal abscess": ("Yes", "Retropharyngeal space", "<b>Widened retropharyngeal space</b> on lateral X-ray"),
 "Ludwig angina": ("Yes", "Floor of mouth, submental and submandibular", "<b>Tongue displaced up and back</b>"),
 "Dental abscess": ("Yes", "Tooth pulp or gum", "Periapical, gingival, periodontal or pericoronal pus"),
 "Gingivitis and periodontitis": ("Little to none", "Gum line", "<b>Gums bleed easily</b>; gingivitis is reversible"),
 "Dental caries, pulpitis and periapical abscess": ("Yes", "Tooth", "Decay first, injury second"),
 "Impacted teeth": ("Varies", "Usually wisdom teeth", "Overcrowding with no room to erupt"),
 "Malocclusion": ("No", "Bite", "<b>Class I, II or III</b> occlusion"),
 "Temporomandibular joint disorders": ("Yes", "Temporomandibular joint and muscles", "<b>Clicking, popping or locking</b> with limited opening"),
 "Oral leukoplakia": ("No", "Oral mucosa", "<b>White and CANNOT be scraped off</b>"),
 "Erythroplakia": ("No", "Oral mucosa", "<b>Red</b> &mdash; 90% dysplastic or carcinoma"),
 "Hairy leukoplakia": ("No &mdash; painless", "<b>Lateral tongue</b>", "Waxes and wanes; think HIV"),
 "Salivary gland neoplasm": ("No &mdash; painless", "<b>Tail of the parotid</b>", "Slow-growing painless mass; pain suggests malignancy"),
 "Oral cavity and oropharyngeal cancer": ("Varies", "Tongue, floor of mouth, tonsil", "<b>Non-healing ulcer</b> with referred otalgia"),
}

IMGS_L19 = {
 "Leukoedema": ("l19-s009_pos1.jpg", 9),
 "Fordyce granules": ("l19-s010_pos1.jpg", 10),
 "Physiologic pigmentation": ("l19-s011_pos2.jpg", 11),
 "Aphthous stomatitis (canker sores)": ("l19-s015_pos1.jpg", 15),
 "Behcet syndrome": ("l19-s019_pos1.jpg", 19),
 "Oral lichen planus": ("l19-s021_pos1.jpg", 21),
 "Systemic lupus erythematosus &mdash; oral": ("l19-s023_pos1.jpg", 23),
 "Herpes simplex ulcers": ("l19-s025_pos1.jpg", 25),
 "Acute suppurative sialadenitis": ("l19-s035_pos1.jpg", 35),
 "Sialolithiasis": ("l19-s036_pos1.jpg", 36),
 "Vocal cord nodules": ("l19-s047_pos1.jpg", 47),
 "Vocal cord polyps": ("l19-s048_pos1.jpg", 48),
 "Vocal cord papillomatosis": ("l19-s049_pos1.jpg", 49),
 "Epiglottitis (supraglottitis)": ("l19-s064_pos1.jpg", 64),
 "Bacterial pharyngitis (GABHS)": ("l19-s073_pos1.jpg", 73),
 "Infectious mononucleosis": ("l19-s083_pos1.jpg", 83),
 "Oral candidiasis (thrush)": ("l19-s089_pos1.jpg", 89),
 "Peritonsillar abscess (quinsy)": ("l19-s096_pos1.jpg", 96),
 "Retropharyngeal abscess": ("l19-s105_pos1.jpg", 105),
 "Ludwig angina": ("l19-s109_pos1.jpg", 109),
 "Dental abscess": ("l19-s116_pos1.jpg", 116),
 "Gingivitis and periodontitis": ("l19-s122_pos2.jpg", 122),
 "Malocclusion": ("l19-s126_pos1.jpg", 126),
 "Oral leukoplakia": ("l19-s133_pos2.jpg", 133),
 "Erythroplakia": ("l19-s135_pos1.jpg", 135),
 "Hairy leukoplakia": ("l19-s136_pos1.jpg", 136),
}
