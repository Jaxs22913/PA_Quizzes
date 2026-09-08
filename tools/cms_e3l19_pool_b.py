# -*- coding: utf-8 -*-
"""Lecture 19 objective-style pool B -- Oral Cavity, Salivary Glands and Neck."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Disorders of the oral cavity, salivary glands, and neck: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")
C = lambda n: "CMS I Disorders of the Oral Cavity, Salivary Glands, Slide %d" % n

QUESTIONS = [

Q("Vocal cord nodules", IO, "Where do vocal cord nodules form?",
  [["At the junction of the anterior third and posterior two thirds",
    "Correct. That point is where the folds strike each other hardest during phonation, so it is "
    "where mechanical trauma concentrates. The lesions are smooth, paired, whitish, bilateral and "
    "symmetric, which is the finding that separates them from a unilateral polyp."],
   ["At the posterior commissure",
    "The posterior commissure is where reflux-related changes and contact granulomas appear, which "
    "is a different mechanism from vibratory trauma."],
   ["On the false cords",
    "The false cords are above the true cords and do not vibrate for phonation. A smooth dilation "
    "there suggests a laryngocele instead."],
   ["At the anterior commissure",
    "The anterior commissure is where the cords meet at the front, and it is a site of concern for "
    "carcinoma spread rather than of nodule formation."]], C(46)),

Q("Vocal cord nodules", IO, "What is first-line treatment for vocal cord nodules?",
  [["Speech therapy",
    "Correct. Nodules result from vocal abuse, so changing the vocal behaviour treats the cause "
    "rather than the lesion. Speech therapy is first line in both adults and children, with "
    "photodocumentation in the voice clinic tracking progress and microlaryngoscopy reserved for "
    "failure."],
   ["Surgical excision of both nodules",
    "Surgery does not address the behaviour that produced them, so they recur, and operating on the "
    "vibrating margin risks scarring that permanently alters the voice."],
   ["Inhaled corticosteroid",
    "Inhaled steroid treats airway inflammation and can itself cause dysphonia and candidiasis. "
    "Nodules are a fibrous response to trauma rather than an inflammatory condition."],
   ["Long-term antibiotics",
    "There is no infection involved. Nodules are mechanical, and antibiotics have no target."]],
  C(47)),

Q("Vocal cord polyps", IO, "How do vocal cord polyps differ from nodules?",
  [["Polyps are unilateral and pedunculated",
    "Correct. Nodules are bilateral, symmetric and paired; polyps are unilateral masses within the "
    "superficial lamina propria, pedunculated and sometimes with visible vascular markings. They are "
    "commoner in men with vocal abuse and heavy smoking, and are excised because a large one may "
    "conceal an occult early laryngeal carcinoma."],
   ["Polyps are bilateral and symmetric",
    "Bilateral symmetry is the defining feature of NODULES. Reversing it swaps two lesions with "
    "different treatments, since nodules get speech therapy and polyps get excised."],
   ["Polyps occur only in children",
    "Screamers' nodules are the paediatric lesion. Polyps are commoner in adult men who smoke and "
    "abuse the voice."],
   ["Polyps are caused by human papillomavirus",
    "Human papillomavirus subtypes 6 and 11 cause recurrent respiratory PAPILLOMATOSIS, which "
    "produces multiple friable warty growths rather than a single gelatinous polyp."]], C(48)),

Q("Vocal cord papillomatosis", IO,
  "Which human papillomavirus subtypes cause recurrent respiratory papillomatosis?",
  [["Subtypes 6 and 11, rarely 16",
    "Correct. Recurrent respiratory papillomatosis is caused by low-risk human papillomavirus "
    "subtypes 6 and 11, with 16 rarely implicated. The distribution is bimodal, juvenile between 2 "
    "and 4 years and adult peaking in the 30s, and there is a 3 to 7 per cent risk of malignant "
    "transformation."],
   ["Subtypes 16 and 18 only",
    "Sixteen and eighteen are the high-risk oncogenic types driving cervical and oropharyngeal "
    "carcinoma. Sixteen is only rarely involved in papillomatosis."],
   ["Herpes simplex virus 1 and 2",
    "Herpes simplex causes oral and perioral ulceration through latency in the trigeminal ganglion, "
    "not warty laryngeal growths."],
   ["Epstein-Barr virus",
    "Epstein-Barr virus causes infectious mononucleosis and is associated with hairy leukoplakia and "
    "nasopharyngeal carcinoma."]], C(49)),

Q("Vocal cord papillomatosis", IO, "Why is tracheostomy avoided in papillomatosis?",
  [["It creates another squamociliary junction the papillomas favour",
    "Correct. Papillomas have an affinity for the boundaries where ciliated respiratory epithelium "
    "meets squamous epithelium. A tracheostomy creates a new such junction, giving the disease a "
    "fresh site to seed and spreading it distally into the trachea, which makes an already difficult "
    "problem worse."],
   ["It causes uncontrollable bleeding from the lesions",
    "Bleeding is a surgical consideration during debulking rather than the stated objection to a "
    "tracheostomy, and it is not what makes the procedure specifically harmful here."],
   ["It prevents the use of laser therapy afterwards",
    "Carbon dioxide laser, cold steel dissection and microdebrider remain available. The objection "
    "concerns disease spread rather than closing off treatment options."],
   ["It converts the disease to a malignant form",
    "There is a 3 to 7 per cent risk of malignant transformation in the disease itself, but a "
    "tracheostomy is not what causes it."]], C(52)),

Q("Vocal cord paralysis", IO,
  "How do unilateral and bilateral vocal cord paralysis differ in presentation?",
  [["Unilateral gives a breathy hoarse voice; bilateral gives stridor",
    "Correct. One immobile cord leaves a gap through which air escapes, producing a breathy hoarse "
    "voice with aspiration and dysphagia, and it may even be asymptomatic. Both cords immobile sit "
    "near the midline and obstruct the airway, giving inspiratory or biphasic stridor and a weak "
    "cry."],
   ["Unilateral gives stridor; bilateral gives a breathy voice",
    "This reverses the two, and the consequence matters: stridor signals a threatened airway, so "
    "misassigning it could delay recognising bilateral disease."],
   ["Both present identically",
    "They differ in the way that determines urgency. Treating them as equivalent misses that "
    "bilateral paralysis is an airway problem."],
   ["Neither affects the voice",
    "Voice production depends on both cords meeting and vibrating, so paralysis of either or both "
    "affects it."]], C(54)),

Q("Vocal cord paralysis", IO,
  "What does laryngeal electromyography contribute in vocal cord paralysis?",
  [["It predicts whether function will return",
    "Correct. Electromyography distinguishes a nerve still in continuity from one that is not. A "
    "bruised or stretched nerve may recover over 6 months to a year, whereas a transected nerve or "
    "one infiltrated by malignancy will not, and that determines whether to wait or proceed to "
    "medialisation or thyroplasty."],
   ["It identifies which cord is paralysed",
    "Laryngoscopy already establishes which cord is immobile by direct observation. Electromyography "
    "answers a different question about the state of the nerve."],
   ["It measures airway calibre",
    "Airway compromise is assessed clinically and by observing the cords. Electromyography records "
    "muscle electrical activity."],
   ["It distinguishes vagal from recurrent laryngeal injury",
    "That distinction is made from associated deficits and from imaging along the nerve's course, "
    "not from this test."]], C(56)),

Q("Acute laryngitis", IO, "What is the commonest cause of hoarseness?",
  [["Acute laryngitis",
    "Correct. Acute laryngitis is the commonest cause of hoarseness and typically persists about a "
    "week after upper respiratory symptoms have cleared. Rhinovirus is the commonest pathogen, and "
    "management is conservative: hydration, antipyretics, voice rest, decongestants, humidification "
    "and smoking cessation."],
   ["Vocal cord carcinoma",
    "Laryngeal carcinoma is a critical cause to exclude in persistent hoarseness, particularly in a "
    "smoker, but it is far less common than a post-viral laryngitis."],
   ["Vocal cord paralysis",
    "Paralysis causes a characteristically breathy hoarse voice but follows surgery, trauma, tumour "
    "or neurological disease rather than being the everyday cause."],
   ["Reflux laryngitis",
    "Acid reflux contributes to chronic laryngeal irritation and appears among the causes, but it is "
    "not the leading one."]], C(57)),

Q("Acute laryngitis", IO, "Are antibiotics indicated in acute laryngitis?",
  [["No, unless a secondary bacterial infection is suspected",
    "Correct. Most acute laryngitis is viral, with rhinovirus commonest, followed by parainfluenza, "
    "respiratory syncytial virus, adenovirus, influenza and pertussis. Treatment is conservative, "
    "and antibiotics are explicitly not indicated unless bacterial superinfection is suspected."],
   ["Yes, in every case",
    "Universal antibiotic treatment of a predominantly viral condition drives resistance without "
    "changing the course."],
   ["Yes, but only intravenously",
    "Intravenous therapy would be a considerable escalation for a self-limiting illness that "
    "usually needs no antibiotic at all."],
   ["No, and antivirals should be given instead",
    "No specific antiviral is indicated for the common causes, and management is symptomatic rather "
    "than aimed at the organism."]], C(57)),

Q("Chronic laryngitis", IO,
  "What defines chronic laryngitis, and why does it matter?",
  [["Voice disturbance over 2 weeks, and it is not a true diagnosis",
    "Correct. Beyond two weeks the label is chronic laryngitis, but that is a description rather "
    "than a diagnosis: it obliges a search for the underlying cause. Laryngeal cancer and vocal cord "
    "polyps must be considered, which is why referral for laryngoscopy is the stated next step."],
   ["Voice disturbance over 3 days, treated with voice rest",
    "Three days is well within the course of acute laryngitis, which settles about a week after the "
    "cold clears and does need voice rest."],
   ["Voice disturbance over 6 months, requiring surgery",
    "Waiting six months before investigating would allow a laryngeal carcinoma to progress "
    "substantially. The threshold is deliberately short."],
   ["Any hoarseness in a smoker, treated with antibiotics",
    "Smoking raises the concern but does not define the term, and antibiotics have no role in a "
    "chronic non-infective hoarseness."]], C(58)),

Q("Epiglottitis", IO, "What is the commonest pathogen in paediatric epiglottitis?",
  [["Haemophilus influenzae type B",
    "Correct. Haemophilus influenzae type B is the commonest pathogen in children, and routine "
    "immunisation has reduced the incidence of supraglottitis by over 90 per cent. Other organisms "
    "include Streptococcus pneumoniae, Staphylococcus aureus and beta-haemolytic streptococci, which "
    "is why the disease still occurs."],
   ["Streptococcus pyogenes",
    "Beta-haemolytic streptococci are among the other pathogens listed, so this is close, but the "
    "organism whose vaccine transformed the epidemiology is Haemophilus."],
   ["Pseudomonas aeruginosa",
    "Pseudomonas causes malignant otitis externa and swimmer's ear rather than supraglottic "
    "cellulitis."],
   ["Corynebacterium diphtheriae",
    "Diphtheria produces a tenacious grey pharyngeal membrane in an unimmunised child and is treated "
    "with antitoxin, a different disease with a different appearance."]], C(60)),

Q("Epiglottitis", IO, "What are the four Ds of paediatric epiglottitis?",
  [["Drooling, dysphagia, dysphonia and distress",
    "Correct. Those four summarise the paediatric presentation, alongside the classic posture of an "
    "irritable child sitting or leaning forward with the neck hyperextended and chin thrust out. "
    "Symptoms come on suddenly and progress over hours in children, more slowly in adults."],
   ["Dyspnoea, diplopia, dysarthria and dizziness",
    "Those are neurological symptoms suggesting a brainstem or posterior circulation problem, not an "
    "airway infection."],
   ["Drooling, diarrhoea, dehydration and drowsiness",
    "Diarrhoea and dehydration are not features of supraglottitis, and drowsiness would be a very "
    "late and ominous sign rather than one of the defining four."],
   ["Dysphagia, dysuria, dyspnoea and delirium",
    "Dysuria has no relationship to the airway, and delirium is not part of the described "
    "presentation."]], C(61)),

Q("Epiglottitis", IO, "Why should intraoral examination be avoided once epiglottitis is suspected?",
  [["It may precipitate complete airway obstruction",
    "Correct. Once the diagnosis is suspected from history and general survey, further examinations "
    "that increase the child's anxiety, including intraoral examination and venipuncture, should not "
    "be performed, because they can complete the obstruction. Mirror or fiberoptic laryngoscopy in a "
    "controlled setting is the gold standard."],
   ["It is uncomfortable for the child",
    "Discomfort is real but is not the reason. The objection is that the procedure can be fatal in "
    "this specific setting."],
   ["It will not show the epiglottis anyway",
    "Whether the epiglottis is visible is beside the point. The prohibition rests on the risk rather "
    "than on the yield."],
   ["It contaminates subsequent cultures",
    "Cultures are taken from the supraglottis and from blood once the airway is secured. "
    "Contamination is not the concern."]], C(63)),

Q("Epiglottitis", IO, "What is the gold standard for diagnosing epiglottitis?",
  [["Mirror or fiberoptic laryngoscopy",
    "Correct. Direct visualisation of the supraglottis is the gold standard, performed where the "
    "airway can be secured. The lateral neck X-ray thumbprint sign is recognised but explicitly not "
    "necessary for diagnosis, and computed tomography shows the same thing without adding safety."],
   ["The thumbprint sign on lateral neck X-ray",
    "The thumbprint sign is well known and worth recognising, but it is stated to be unnecessary for "
    "diagnosis, and sending an unstable child to radiology carries its own risk."],
   ["Computed tomography of the neck",
    "Computed tomography demonstrates the swollen epiglottis but takes the patient away from the "
    "team who can secure the airway, for information that does not change management."],
   ["Blood cultures",
    "Blood cultures and a supraglottic swab are taken once the airway is secured, to guide "
    "antibiotics. They do not make the diagnosis."]], C(63)),

Q("Epiglottitis", IO, "What antibiotic combination is used in epiglottitis?",
  [["A third-generation cephalosporin plus an antistaphylococcal agent",
    "Correct. Ceftriaxone or cefotaxime with vancomycin for 7 to 10 days covers Haemophilus, "
    "pneumococcus and staphylococcus. In genuine penicillin or cephalosporin allergy the alternative "
    "is vancomycin with a quinolone or a carbapenem, adjusted once cultures return."],
   ["Amoxicillin alone",
    "Amoxicillin does not cover beta-lactamase producing Haemophilus or staphylococcus, and oral "
    "administration requires swallowing, which these patients cannot do."],
   ["A macrolide alone",
    "Macrolides have insufficient activity against the organisms involved for a disease with this "
    "mortality, and are reserved for allergy in less critical infections."],
   ["Metronidazole plus penicillin",
    "That combination targets oral anaerobes and is used in Ludwig angina, a different deep neck "
    "infection with a different flora."]], C(67)),

Q("Pharyngitis", IO, "What proportion of pharyngitis is viral?",
  [["About 70 per cent",
    "Correct. Roughly 70 per cent of pharyngitis is viral, caused by adenovirus, Epstein-Barr virus, "
    "herpes simplex, HIV, influenza, parainfluenza, rhinovirus, coronavirus, echovirus, "
    "enteroviruses and coxsackievirus. The remaining 30 per cent is bacterial, chiefly group A "
    "beta-haemolytic streptococcus."],
   ["About 30 per cent",
    "Thirty per cent is the BACTERIAL share. Swapping the two would justify treating most sore "
    "throats with antibiotics, which is the practice the figures argue against."],
   ["About 10 per cent",
    "Ten per cent viral would make pharyngitis a predominantly bacterial disease, which does not "
    "match either the microbiology or the clinical course."],
   ["Nearly all",
    "Bacterial pharyngitis is common enough to matter, and it is the reason Centor scoring and "
    "testing exist at all."]], C(70)),

Q("Bacterial pharyngitis", IO,
  "Which clinical feature argues AGAINST streptococcal pharyngitis?",
  [["Cough",
    "Correct. Absence of cough scores a Centor point precisely because its presence argues for a "
    "viral cause. Streptococcal disease gives fever above 100.4 degrees, sore throat, tender "
    "cervical nodes, dysphagia, odynophagia and abdominal pain, with exudate on the tonsils, and "
    "characteristically no cough."],
   ["Tonsillar exudate",
    "Exudate is a Centor criterion FOR streptococcal infection, though it also occurs in "
    "mononucleosis, which is why it is scored rather than treated as diagnostic."],
   ["Tender anterior cervical nodes",
    "Tender anterior cervical adenopathy is another Centor point in favour of streptococcal "
    "disease."],
   ["Fever above 100.4 degrees Fahrenheit",
    "Fever is also a Centor criterion supporting bacterial infection rather than arguing against "
    "it."]], C(73)),

Q("Centor criteria", IO, "How is age scored in the Centor criteria?",
  [["Plus one for 3 to 14, zero for 15 to 44, minus one for 45 and over",
    "Correct. Age is the only criterion that can subtract. Streptococcal pharyngitis is common in "
    "children and adolescents and uncommon over 45, so the score reflects that gradient, alongside "
    "one point each for absence of cough, tonsillar exudate, fever and tender anterior cervical "
    "nodes."],
   ["Plus one for all ages",
    "A flat score ignores the strong age gradient in streptococcal prevalence, which is the reason "
    "age appears in the criteria at all."],
   ["Minus one for children and plus one for adults",
    "This reverses the gradient. Children are the group in whom streptococcal disease is commonest, "
    "though not under three years."],
   ["Age is not part of the Centor criteria",
    "Age is one of the five components and is the only one capable of reducing the total."]],
  C(76)),

Q("Bacterial pharyngitis", IO, "What is first-line antibiotic treatment for streptococcal pharyngitis?",
  [["Penicillin VK for 10 days",
    "Correct. Penicillin VK for ten days is first line, with amoxicillin as a substitute and "
    "intramuscular penicillin G where compliance or oral intake is a concern. Mild penicillin "
    "allergy allows cephalexin or cefadroxil; severe allergy needs a macrolide or clindamycin."],
   ["Azithromycin for 3 days",
    "Macrolides are the fallback for severe penicillin allergy, and streptococcal resistance to them "
    "is a real concern, so they are not first choice."],
   ["Ciprofloxacin for 7 days",
    "Fluoroquinolones have poor streptococcal coverage relative to their side effect burden and are "
    "not used for pharyngitis."],
   ["Metronidazole for 10 days",
    "Metronidazole targets anaerobes and is used in deep neck infection such as Ludwig angina, not "
    "for streptococcal pharyngitis."]], C(77)),

Q("Rheumatic fever", IO, "When do the signs of rheumatic fever appear after the infection?",
  [["2 to 3 weeks, sometimes as early as one or as late as five",
    "Correct. The delay reflects the mechanism: cross-reactive antibodies produced against the "
    "streptococcus take time to build and then attack heart muscle. Peak incidence is between 5 and "
    "15 years, rare before 4 and after 40, and the illness typically resolves after about six "
    "weeks."],
   ["Within 24 hours",
    "A same-day reaction would indicate a direct toxic or infective effect rather than an antibody "
    "response, which necessarily takes longer to develop."],
   ["6 to 12 months later",
    "That delay is too long to connect the two events clinically, and it does not match the "
    "described course."],
   ["Only after repeated infections over years",
    "Rheumatic fever can follow a single untreated infection, which is why one sore throat is "
    "treated to prevent it."]], C(78)),
]
