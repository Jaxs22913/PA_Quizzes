# -*- coding: utf-8 -*-
"""Lecture 19 objective-style pool C -- Oral Cavity, Salivary Glands and Neck."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Disorders of the oral cavity, salivary glands, and neck: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")
C = lambda n: "CMS I Disorders of the Oral Cavity, Salivary Glands, Slide %d" % n

QUESTIONS = [

Q("Infectious mononucleosis", IO, "What is the classic triad of infectious mononucleosis?",
  [["Fever, tonsillar pharyngitis and cervical lymphadenopathy",
    "Correct. That triad defines the presentation, with palatal petechiae, hepatomegaly, "
    "splenomegaly and a maculopapular rash in about 5 per cent as additional features. About 90 to "
    "95 per cent of adults are Epstein-Barr seropositive, and the illness commonly affects those "
    "aged 15 to 24."],
   ["Fever, rash and arthritis",
    "That combination suggests a systemic inflammatory or rheumatological illness rather than "
    "mononucleosis, whose rash appears in only a small minority spontaneously."],
   ["Sore throat, cough and rhinitis",
    "Cough and rhinitis point toward viral pharyngitis of the common-cold type, and their presence "
    "argues against streptococcal disease on the Centor score."],
   ["Fever, jaundice and abdominal pain",
    "Hepatomegaly occurs and transaminases can rise, but jaundice with abdominal pain describes a "
    "hepatobiliary illness rather than the mononucleosis triad."]], C(82)),

Q("Infectious mononucleosis", IO,
  "When can the monospot test be falsely negative?",
  [["Early in the illness, in the first week",
    "Correct. The heterophile antibody test is very sensitive and specific once antibodies have "
    "developed, so a positive result needs no further testing. But antibodies take time to appear, "
    "which is why a negative result in the first week does not exclude the diagnosis and serology "
    "for Epstein-Barr antibodies is used instead."],
   ["In patients over 40",
    "Age affects the likelihood of the disease rather than the behaviour of the test, since most "
    "adults are already seropositive from past infection."],
   ["Only if the patient has taken antibiotics",
    "Antibiotics do not interfere with the heterophile response. Giving an aminopenicillin does "
    "produce a rash, which is a different consequence entirely."],
   ["Never; it is always accurate",
    "Treating any test as infallible removes the reason for the serological backup pathway that "
    "exists specifically for negative results."]], C(84)),

Q("Infectious mononucleosis", IO,
  "What does a positive IgM against Epstein-Barr virus indicate?",
  [["Current infection",
    "Correct. IgM appears during acute infection and IgG persists afterwards, so IgM positive means "
    "current and IgG positive means past. Serology is particularly useful in patients under four "
    "years, in those with a negative heterophile test, and where symptoms are atypical."],
   ["Past infection",
    "Past infection is indicated by IgG, which persists for life after exposure. Since 90 to 95 per "
    "cent of adults are seropositive, IgG alone says very little."],
   ["Immunity from vaccination",
    "There is no Epstein-Barr vaccine in routine use, so serology reflects natural exposure "
    "rather than immunisation."],
   ["Chronic carriage without infection",
    "Viral load monitoring by polymerase chain reaction is used in transplant patients for that "
    "purpose, rather than IgM."]], C(84)),

Q("Infectious mononucleosis", IO,
  "Why must contact sport be avoided for about a month after mononucleosis?",
  [["To prevent splenic rupture",
    "Correct. Epstein-Barr virus enlarges the spleen, and an enlarged spleen has a capsule under "
    "tension that can rupture with relatively minor abdominal trauma. The restriction runs until "
    "splenomegaly has resolved, monitored by ultrasound, because symptomatic recovery and splenic "
    "recovery do not follow the same timeline."],
   ["To prevent transmission to teammates",
    "Transmission is by saliva rather than by contact during sport, and the restriction is about the "
    "patient's own spleen rather than about spread."],
   ["To avoid triggering the maculopapular rash",
    "The rash occurs in about 5 per cent spontaneously and is reliably triggered by aminopenicillins, "
    "not by exercise."],
   ["To prevent airway obstruction from tonsillar swelling",
    "Severe respiratory compromise from tonsillar enlargement is treated with corticosteroids and is "
    "an acute problem, not the reason for a month of restriction."]], C(86)),

Q("Infectious mononucleosis", IO,
  "What happens if a patient with mononucleosis is given penicillin?",
  [["A widespread exanthem develops",
    "Correct. Aminopenicillins reliably provoke a widespread maculopapular rash in Epstein-Barr "
    "infection. The classic sequence is a sore throat treated as streptococcal, a rash appearing, "
    "and then the correct diagnosis being made. Recognising it matters because it is not a true "
    "penicillin allergy."],
   ["The illness resolves more quickly",
    "There is no antiviral therapy and no antibiotic shortens the illness, since the cause is "
    "viral. Management is supportive."],
   ["Anaphylaxis occurs",
    "The rash is not immunoglobulin E mediated and is not anaphylactic. Labelling the patient "
    "allergic on the strength of it removes an entire antibiotic class unnecessarily."],
   ["The spleen shrinks more rapidly",
    "Nothing about penicillin affects splenic size, and the restriction on contact sport stands "
    "regardless."]], C(87)),

Q("Oral candidiasis", IO, "Which finding distinguishes oral candidiasis from leukoplakia?",
  [["The patches can be rubbed off with a tongue depressor",
    "Correct. Candida forms a removable pseudomembrane, so wiping it leaves an erythematous base. "
    "Leukoplakia is defined as a white lesion that CANNOT be scraped off, and lichen planus produces "
    "striae that are part of the mucosa. That single manoeuvre separates three diagnoses with very "
    "different implications."],
   ["The patches are painless",
    "Candidiasis is painful, and leukoplakia is typically painless, so this reverses the "
    "relationship and would point the wrong way."],
   ["The patches are confined to the tongue",
    "Candidiasis usually forms on buccal mucosa and tongue, but site does not distinguish it from "
    "leukoplakia, which can occur anywhere in the oral cavity."],
   ["The patches fluoresce under ultraviolet light",
    "There is no such test in this setting. Diagnosis is clinical, supported by a potassium "
    "hydroxide preparation showing spores and pseudohyphae."]], C(89)),

Q("Oral candidiasis", IO, "What does a potassium hydroxide preparation show in oral candidiasis?",
  [["Spores and pseudohyphae",
    "Correct. Potassium hydroxide dissolves epithelial cells and leaves fungal elements visible, so "
    "spores and pseudohyphae confirm the clinical impression. Treatment is saline and peroxide "
    "washes plus a topical antifungal such as nystatin, clotrimazole, ketoconazole or fluconazole."],
   ["Multinucleated giant cells",
    "Multinucleated giant cells are the finding on a Tzanck smear in herpes simplex, though they "
    "also appear in varicella zoster, which limits that test's usefulness."],
   ["Acid-fast bacilli",
    "Acid-fast bacilli are sought in mycobacterial disease, whether tuberculous or atypical, and are "
    "not seen with potassium hydroxide."],
   ["Gram-positive cocci in chains",
    "Streptococci in chains would be seen on Gram stain in bacterial infection, and potassium "
    "hydroxide is not a bacterial stain at all."]], C(90)),

Q("Cervical adenitis", IO,
  "What proportion of unilateral solitary anterior cervical adenitis relates to beta-haemolytic "
  "streptococcus?",
  [["About 70 per cent",
    "Correct. Local ear, nose and throat infections drain to regional nodes, and about 70 per cent of "
    "these unilateral solitary anterior nodes relate to beta-haemolytic streptococcal infection, "
    "with 20 per cent staphylococcal including MRSA and 10 per cent viral, atypical mycobacterial or "
    "Bartonella."],
   ["About 20 per cent",
    "Twenty per cent is the STAPHYLOCOCCAL share, which matters for antibiotic choice because it "
    "includes MRSA, but it is not the majority."],
   ["About 10 per cent",
    "Ten per cent covers the residual group of viruses, atypical mycobacteria and Bartonella "
    "henselae together."],
   ["Under 5 per cent",
    "That would make streptococcal infection a rarity in cervical adenitis, which would change "
    "empirical treatment entirely."]], C(92)),

Q("Cervical adenitis", IO, "Why is cervical lymphadenopathy described as a sign rather than a diagnosis?",
  [["It has infectious, inflammatory, degenerative and neoplastic causes",
    "Correct. Lymphadenopathy is a finding that many processes produce, from toxoplasmosis, "
    "tuberculosis, brucellosis, herpes, syphilis, cytomegalovirus, HIV, histoplasmosis and "
    "chickenpox through to neoplasia. Treatment is directed at whichever underlying cause is found, "
    "with drainage if there is an abscess."],
   ["It always resolves without treatment",
    "Reactive nodes do resolve, but treating all lymphadenopathy as self-limiting would miss the "
    "malignant and granulomatous causes on the same list."],
   ["It occurs only in children",
    "Cervical adenopathy occurs at every age, and its significance rises with age because the "
    "malignant proportion increases."],
   ["It is diagnostic of lymphoma",
    "Lymphoma is one cause among many, and treating a node as diagnostic of it would be wrong in the "
    "great majority of cases."]], C(91)),

Q("Peritonsillar abscess", IO, "What is the classic triad of peritonsillar abscess?",
  [["Trismus, uvular deviation and dysphonia",
    "Correct. Trismus is the most reliable of the three, from irritation of the adjacent medial "
    "pterygoid; uvular deviation follows oedema and medial displacement of the soft palate and "
    "peritonsillar fold; and dysphonia arises from vagus nerve involvement failing to elevate the "
    "palate."],
   ["Fever, cough and rhinorrhoea",
    "Cough and rhinorrhoea point toward a viral upper respiratory illness and argue against a "
    "bacterial or suppurative process."],
   ["Stridor, drooling and tripod positioning",
    "Those describe epiglottitis, which is an airway emergency of a different kind and does not "
    "deviate the uvula."],
   ["Neck stiffness, torticollis and a widened prevertebral space",
    "Those suggest a retropharyngeal abscess, a disease of children under five diagnosed on lateral "
    "neck imaging."]], C(99)),

Q("Peritonsillar abscess", IO, "Which symptom of peritonsillar abscess is most reliable?",
  [["Trismus",
    "Correct. Trismus is singled out as the most reliable symptom. Pus tracking adjacent to the "
    "medial pterygoid irritates it into spasm, which limits mouth opening and also makes examination "
    "and drainage technically difficult."],
   ["Uvular deviation",
    "Uvular deviation is part of the classic triad and is highly suggestive, but it is not the one "
    "identified as most reliable."],
   ["Fever",
    "Fever accompanies many throat infections including simple tonsillitis, so it does not "
    "distinguish an abscess from what preceded it."],
   ["Sore throat",
    "Severe sore throat is universal in this condition but equally universal in the tonsillitis it "
    "complicates."]], C(99)),

Q("Peritonsillar abscess", IO, "What is the first priority in managing a peritonsillar abscess?",
  [["Secure the airway if needed",
    "Correct. Airway comes first, before any attempt at drainage. Needle aspiration and incision and "
    "drainage then treat the collection, with parenteral amoxicillin-clavulanate or clindamycin, "
    "adding MRSA cover if severe, and oral therapy for those who can tolerate it."],
   ["Start oral antibiotics and review in 48 hours",
    "Oral antibiotics have a place in less severe cases who can swallow, but sending home a patient "
    "who cannot drink, with an untreated collection, ignores both the airway and the abscess."],
   ["Arrange immediate tonsillectomy",
    "Tonsillectomy is indicated for recurrent tonsillitis and recurrent abscesses, and most surgeons "
    "prefer to wait until the acute infection settles."],
   ["Obtain computed tomography before any intervention",
    "Contrast computed tomography demonstrates the extent and ultrasound can distinguish abscess "
    "from cellulitis, but imaging follows airway assessment rather than preceding it."]], C(101)),

Q("Retropharyngeal abscess", IO, "In which age group is retropharyngeal abscess commonest?",
  [["Children under 5",
    "Correct. It is commonest under five, following upper respiratory infection, otitis media or "
    "sinusitis, as retropharyngeal nodes suppurate. In adults it usually follows intraoral "
    "procedures, trauma, a foreign body such as a fishbone, immunocompromise or odontogenic spread."],
   ["Adolescents and young adults",
    "That is the peak group for PERITONSILLAR abscess, the commonest deep head and neck infection, "
    "which is a different space and a different presentation."],
   ["Adults over 60",
    "Older adults are the group in whom malignancy and necrotising infections dominate. "
    "Retropharyngeal abscess in adults is possible but requires a specific precipitant."],
   ["Neonates",
    "The retropharyngeal nodes involved involute during childhood, and neonates are not the "
    "characteristic group."]], C(103)),

Q("Retropharyngeal abscess", IO, "What is the gold standard investigation for retropharyngeal abscess?",
  [["Lateral neck computed tomography",
    "Correct. Computed tomography is the gold standard, showing a rim-enhancing hypodense collection "
    "in the retropharyngeal space and distinguishing abscess from adenitis, which is the decision "
    "that matters. A lateral neck X-ray showing a widened retropharyngeal space is supportive but "
    "less definitive."],
   ["Lateral neck radiography",
    "The plain film shows widening of the prevertebral soft tissue and is a useful early clue, but "
    "it cannot separate a drainable collection from inflamed nodes."],
   ["Ultrasound",
    "Ultrasound is useful for peritonsillar collections, where it distinguishes abscess from "
    "cellulitis and can guide aspiration, but the retropharyngeal space is not accessible to it."],
   ["Magnetic resonance imaging",
    "Magnetic resonance gives excellent soft tissue detail but is slower and less available in an "
    "acutely unwell child with a threatened airway."]], C(105)),

Q("Retropharyngeal abscess", IO,
  "Which complication of retropharyngeal abscess carries a 50 per cent mortality?",
  [["Mediastinitis",
    "Correct. The retropharyngeal space extends from the base of the skull to the posterior "
    "mediastinum, so infection has a direct anatomical route into the chest. Mediastinitis carries a "
    "50 per cent mortality, and other complications include respiratory distress, rupture with "
    "aspiration pneumonia, and spread into the danger space."],
   ["Cavernous sinus thrombosis",
    "Cavernous sinus thrombosis is the feared intracranial complication of orbital and facial "
    "infections, following venous routes upward rather than the retropharyngeal space downward."],
   ["Ludwig angina",
    "Ludwig angina is a separate deep neck infection of the submental, sublingual and submandibular "
    "spaces, usually odontogenic, rather than a complication of this one."],
   ["Rheumatic fever",
    "Rheumatic fever follows untreated streptococcal PHARYNGITIS through cross-reactive antibodies "
    "and appears two to three weeks later, a quite different mechanism."]], C(107)),

Q("Ludwig angina", IO, "Which spaces are involved in Ludwig angina?",
  [["The floor of the mouth with the submental, sublingual and submandibular spaces",
    "Correct. It is a severe cellulitis of those spaces, and it is an emergency because it can "
    "rapidly compromise the upper airway and force a surgical airway. The tongue is displaced "
    "upwards and backwards by posterior spread, which is the mechanism of the obstruction."],
   ["The retropharyngeal space",
    "The retropharyngeal space runs from skull base to mediastinum and hosts a different abscess, "
    "with widening on lateral X-ray as its sign."],
   ["The space between the tonsillar capsule and pharyngeal muscles",
    "That is the peritonsillar space, whose abscess gives trismus, uvular deviation and a hot potato "
    "voice."],
   ["The parapharyngeal space alone",
    "The parapharyngeal space can be involved in deep neck infection generally, but Ludwig angina is "
    "defined by the floor-of-mouth spaces specifically."]], C(108)),

Q("Ludwig angina", IO, "What antibiotic regimen is used for Ludwig angina?",
  [["Penicillin with metronidazole, or ampicillin-sulbactam",
    "Correct. The flora is mixed oral, including streptococci, staphylococci, Bacteroides, "
    "Fusobacterium and Klebsiella in patients with diabetes, so cover includes anaerobes. "
    "Clindamycin and selected cephalosporins are alternatives, alongside external drainage if the "
    "airway is threatened and a dental consultation for the offending tooth."],
   ["Ceftriaxone with vancomycin",
    "That combination is used for epiglottitis, targeting Haemophilus, pneumococcus and "
    "staphylococcus rather than the oral anaerobes that dominate here."],
   ["Penicillin VK alone for 10 days",
    "Ten days of oral penicillin is the treatment for streptococcal pharyngitis. It provides neither "
    "anaerobic cover nor the parenteral route this emergency requires."],
   ["Azithromycin alone",
    "A macrolide alone is inadequate for a rapidly spreading mixed anaerobic infection threatening "
    "the airway."]], C(111)),

Q("Diphtheria", IO, "What is the characteristic pharyngeal finding in diphtheria?",
  [["A tenacious grey membrane over the tonsils and pharynx",
    "Correct. The pharyngeal form is commonest and produces an adherent grey membrane that bleeds "
    "when disturbed, with mild sore throat, fever, malaise, toxaemia and prostration. Complications "
    "come from the exotoxin: myocarditis with arrhythmia and heart block, and neuropathy affecting "
    "cranial nerves first."],
   ["Vesicles on the soft palate and tonsils",
    "Ulcerative vesicles over the tonsils describe herpangina, a feature of viral pharyngitis rather "
    "than diphtheria."],
   ["Creamy white patches that wipe away",
    "Removable creamy patches are oral candidiasis. The diphtheritic membrane is adherent, which is "
    "the whole point of calling it tenacious."],
   ["Bilateral tonsillar exudate with palatal petechiae",
    "Exudate with petechiae is characteristic of infectious mononucleosis, which is on the "
    "differential list to distinguish from diphtheria."]], C(112)),

Q("Diphtheria", IO, "What is the essential treatment for diphtheria beyond antibiotics?",
  [["Antitoxin, obtained from the Centers for Disease Control",
    "Correct. Antibiotics eradicate the organism but do nothing about circulating exotoxin, and it "
    "is the toxin that causes the myocarditis and neuropathy that kill. Antitoxin is given to all "
    "patients, alongside penicillin or erythromycin for 14 days and isolation until three "
    "consecutive cultures are negative."],
   ["High-dose corticosteroids",
    "Steroids may be used adjunctively for airway swelling but neither neutralise toxin nor "
    "eliminate the organism."],
   ["Intravenous immunoglobulin",
    "Pooled immunoglobulin is used in other conditions such as Behcet syndrome. Diphtheria requires "
    "a specific antitoxin against its exotoxin."],
   ["Antiviral therapy",
    "Corynebacterium diphtheriae is a bacterium, so antiviral treatment has no target."]], C(113)),

Q("Diphtheria", IO, "How long are contacts of a diphtheria case treated?",
  [["Erythromycin for 7 days",
    "Correct. Contacts receive erythromycin 500 milligrams four times daily for seven days to "
    "eradicate carriage, while the case itself is treated for 14 days and isolated until three "
    "consecutive cultures after therapy are negative. Prevention rests on routine childhood "
    "immunisation with boosters."],
   ["No treatment is needed for contacts",
    "Untreated carriers continue to transmit the organism, which is why contact treatment is part of "
    "the public health response."],
   ["Antitoxin for all contacts",
    "Antitoxin is reserved for cases with circulating toxin. Contacts need eradication of carriage "
    "rather than neutralisation of a toxin they do not have."],
   ["Penicillin for 30 days",
    "A month of treatment is far longer than needed to clear carriage and would not improve on the "
    "stated seven-day course."]], C(113)),
]
