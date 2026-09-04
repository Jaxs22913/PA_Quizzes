# -*- coding: utf-8 -*-
"""Lecture 17 rows for the ENT comparison chart.

Disorders of the Nose and Paranasal Sinuses, Prof. Hugh Griffenkranz,
3 September. Same 10-field shape as the Lecture 15 and 16 modules.

THE DISCRIMINATOR TRIAD CHANGES MEANING HERE, WITHOUT CHANGING COLUMNS. For the
ear the three were pain, hearing loss and the otoscopy finding. Nasal disease
has no hearing loss to speak of, so the middle column carries the DISCHARGE --
which is the single most useful nasal sign, and the one the lecture spends most
time on. The column headings on the chart page are written to cover both.

SLIDE 63 IS AN IMAGE OF A LIST. It extracts as a bare title, and it carries the
conditions associated with multiple benign polyps together with their
percentages. That content is transcribed into the polyp row rather than lost --
see [[image_only_slides]].
"""
SINUS = "Sinusitis"
SEPTUM = "Septum"
BLEED = "Epistaxis"
TRAUMA = "Nasal trauma"
FB = "Foreign body"
POLYP = "Polyps and rhinitis"
NEO = "Neoplasm"
D17 = "hughie Nose & Paranasal Sinuses"

ROWS_L17 = [
 ("Acute sinusitis (rhinosinusitis)", SINUS,
  "<b>Under 4 weeks</b> &middot; <b>90&ndash;98% VIRAL</b> &middot; facial pain that is <b>worse bending forward</b>",
  "Symptomatic inflammation of one or more paranasal sinuses <b>lasting under four weeks</b>, from "
  "impaired drainage and retained secretions, with obstruction and/or facial pain, pressure or "
  "fullness. <b>&ldquo;Rhinosinusitis&rdquo; is the preferred term</b> because rhinitis and "
  "sinusitis usually coexist. Affects <b>1 in 8 adults</b> &mdash; over 30 million a year in the "
  "United States &mdash; and is the <b>fifth leading reason antibiotics are prescribed</b>. "
  "Nasal drainage and congestion, rhinorrhoea, postnasal drip, headache. <b>Pain localises to the "
  "involved sinus and is worse bending over or lying flat.</b>",
  "<b>No diagnostic test distinguishes viral from bacterial</b>, and none is indicated routinely. "
  "<b>Routine sinus radiography is discouraged</b>: three or more clinical findings have similar "
  "accuracy to imaging, and imaging cannot separate the two causes anyway. <b>Limited coronal CT</b> "
  "for recurrent infection or failure to respond, or if signs suggest <b>extrasinus involvement</b>. "
  "Viral causes rhinovirus, parainfluenza, influenza; bacterial <b>S. pneumoniae, nontypable "
  "H. influenzae and &mdash; in children &mdash; M. catarrhalis</b>. Immunocompromised: <b>fungal "
  "&mdash; Rhizopus, Mucor, occasionally Aspergillus</b>. Nosocomial cases are polymicrobial with "
  "S. aureus and gram-negative bacilli.",
  "<b>Most improve WITHOUT antibiotics.</b> Symptomatic: decongestants, non-steroidal "
  "anti-inflammatories, nasal or sinus lavage, intranasal steroids, neti pot, saline sprays. "
  "<b>If bacterial: amoxicillin/clavulanate.</b> Penicillin allergy: <b>doxycycline</b>, or an "
  "antipneumococcal fluoroquinolone such as moxifloxacin. If influenza, <b>oseltamivir</b> for five "
  "days in anyone over 13. <b>Medical treatment fails &rarr; ENT referral for surgery.</b>",
  "Routine",
  "Tell the patient what they have, how they got it, how to use the medicine or device, and "
  "&mdash; if referring &mdash; to which specialty. Most cases are viral and settle without "
  "antibiotics.",
  "9&ndash;27", D17),

 ("Bacterial sinusitis &mdash; the features that suggest it", SINUS,
  "<b>Double worsening</b> &middot; <b>&ge;10 days</b> &middot; <b>UNILATERAL</b> tooth or facial pain",
  "Only <b>0.5&ndash;2% of viral episodes</b> develop a bacterial superinfection, so these features "
  "are what raise the possibility: <b>worsening after 5&ndash;6 days of initial improvement</b>; "
  "<b>persistent symptoms for 10 days or more</b>; persistent purulent discharge; "
  "<b>UNILATERAL upper tooth or facial pain</b>; <b>unilateral maxillary tenderness</b>; fever; "
  "altered mental status.",
  "<b>PAIN is the big distinguishing factor</b> &mdash; it occurs only in bacterial and fungal "
  "sinusitis, and it is <b>reproducible on palpation</b>, which a common cold is not. Fever above "
  "100.4&deg;F and severe pain point bacterial or fungal &mdash; <b>check the patient is not on "
  "an antipyretic first</b>. <b>Discharge colour is largely unhelpful</b>: yellow or green is the "
  "<i>least</i> useful; clear may be viral or allergic; yellow AND putrid suggests bacterial; "
  "<b>BLACK suggests fungus</b>; rust-coloured may be S. pneumoniae.",
  "Symptomatic treatment <b>plus</b> antibiotics &mdash; <b>amoxicillin/clavulanate</b> first line.",
  "Routine",
  "The colour of the discharge is the thing patients most expect to be diagnostic, and it is the "
  "thing that matters least.",
  "16&ndash;19, 23", D17),

 ("Sinusitis with urgent features", SINUS,
  "<b>Diplopia</b> &middot; <b>periorbital swelling or erythema</b> &middot; <b>altered mental status</b>",
  "The lecture names these separately as <b>symptoms requiring urgent attention</b> in a patient "
  "with sinusitis: <b>visual disturbance, especially diplopia</b>; <b>periorbital swelling or "
  "erythema</b>; <b>altered mental status</b>.",
  "<b>Sinus CT if signs suggest extrasinus involvement.</b> These are the findings that say the "
  "disease has left the sinus.",
  "Urgent evaluation and imaging rather than another course of symptomatic treatment.",
  "Emergent",
  "The orbit sits next door to the ethmoid sinus. Eye signs in a sinusitis patient are the ones "
  "that change the plan.",
  "17, 21", D17),

 ("Chronic bacterial sinusitis", SINUS,
  "<b>Over 12 weeks</b> &middot; constant congestion with flares &middot; <b>impaired mucociliary clearance</b>",
  "Sinusitis <b>lasting more than twelve weeks</b>. The mechanism is <b>impaired mucociliary "
  "clearance causing REPEATED infections</b> rather than one persistent infection. Constant nasal "
  "congestion and sinus pressure, with periods of increased severity.",
  "<b>Sinus CT</b> defines extent, detects an underlying anatomic defect or obstruction, and "
  "assesses response. <b>Endoscopy-derived tissue for histology and culture</b> should guide "
  "treatment. Consider full blood count with differential and <b>IgE</b>.",
  "<b>Repeated antibiotic courses, often 3&ndash;4 weeks at a time</b> &mdash; oral steroids plus "
  "two weeks of amoxicillin/clavulanate is the stated regimen. Adjuncts: intranasal "
  "glucocorticoids, sinus irrigation. <b>Refer to ENT for surgical evaluation</b> and to allergy "
  "for skin testing.",
  "Urgent",
  "It is a drainage problem as much as an infection, which is why it keeps coming back and why "
  "surgery enters the conversation.",
  "28&ndash;29", D17),

 ("Chronic fungal sinusitis", SINUS,
  "<b>Aspergillus</b> &middot; a <b>fungus ball</b> &middot; allergic form has <b>peanut-butter mucus</b>",
  "<b>Noninvasive disease in immunocompetent hosts</b>, typically <b>Aspergillus</b> and "
  "dematiaceous moulds. <b>Recurrence is common.</b> The <b>allergic</b> form is seen in patients "
  "with <b>nasal polyps and asthma</b> and presents as <b>pansinusitis with thick, "
  "eosinophil-laden mucus the consistency of peanut butter</b>.",
  "Imaging and endoscopy. Unilateral disease with a <b>mycetoma (fungus ball)</b> is the "
  "characteristic finding.",
  "<b>Mild indolent disease is cured by endoscopic surgery WITHOUT antifungals.</b> A fungus ball "
  "is treated surgically &mdash; <b>and with antifungals only if bony erosion has occurred</b>.",
  "Urgent",
  "The surprise here is that most of it is treated surgically rather than with drugs.",
  "30", D17),

 ("Deviated septum", SEPTUM,
  "One passage <b>smaller than the other</b> &middot; congenital or traumatic",
  "The nasal septum is <b>significantly displaced to one side</b>, making one air passage smaller. "
  "<b>Congenital or traumatic.</b> Ranges from congestion &mdash; through blockage of the ostia "
  "&mdash; to <b>anosmia</b>. In severe forms: <b>obstructive sleep apnoea, snoring, facial pain "
  "and recurrent nosebleeds</b>.",
  "Clinical, with a nasal speculum; CT where needed.",
  "<b>Surgery &mdash; septoplasty</b>, by an otorhinolaryngologist.",
  "Routine",
  "The recurrent nosebleeds and the snoring are what usually bring the patient in, not the "
  "deviation itself.",
  "32&ndash;36", D17),

 ("Perforated septum", SEPTUM,
  "<b>Intranasal steroid or COCAINE use</b> &middot; chronic ischaemia",
  "A perforation through the nasal septum. Congenital or traumatic, but <b>many are from "
  "intranasal steroid use or cocaine use</b>, both by <b>chronic ischaemia</b>. Rarely "
  "<b>granulomatosis with polyangiitis (Wegener&rsquo;s)</b>, a vascular autoimmune disease, may "
  "cause nasal deformity. <b>Rarely, secondary syphilis</b> &mdash; seldom seen now.",
  "<b>Physical examination</b>, possibly with CT.",
  "<b>Treat the underlying cause and it may grow back</b>; otherwise <b>septoplasty</b>.",
  "Routine",
  "The drug history is the diagnosis here &mdash; ask about both prescribed nasal steroids and "
  "cocaine.",
  "37&ndash;40", D17),

 ("Septal haematoma", SEPTUM,
  "Blood <b>between septum and perichondrium</b> &middot; after trauma &middot; <b>drain it</b>",
  "A haematoma between the nasal septum and the perichondrium or mucosal epithelium. <b>Usually "
  "secondary to trauma</b>; other causes are bleeding disorders, cocaine, foreign body and "
  "medications. <b>Associated with nasal fracture</b> &mdash; look for it in every nasal injury.",
  "Inspection with a nasal speculum. It is one of the four things that must be excluded before a "
  "nasal fracture can be managed without imaging.",
  "<b>Drainage via intranasal incision under general anaesthesia.</b>",
  "Urgent",
  "The same lesson as the auricular haematoma in Lecture 15: cartilage separated from its blood "
  "supply does not survive.",
  "41&ndash;43", D17),

 ("Epistaxis &mdash; anterior", BLEED,
  "<b>Kiesselbach&rsquo;s plexus</b> &middot; <b>90%</b> of nosebleeds &middot; commonest cause is <b>the patient&rsquo;s finger</b>",
  "A common emergency department complaint, <b>most cases before age 10 or between 45 and 65</b>, "
  "with a <b>winter predominance</b>. <b>The commonest cause is trauma &mdash; from the "
  "patient&rsquo;s finger.</b> <b>Chronic dry nose</b> is a risk factor. <b>Anterior bleeds are by "
  "far the commonest: 90% arise in the vascular watershed of the nasal septum &mdash; "
  "Kiesselbach&rsquo;s plexus.</b>",
  "<b>Airway, breathing, circulation first</b> &mdash; bleeding can be severe. Normal appearance, "
  "vital signs and respiratory function is the reassuring picture. History: tumours, coagulation "
  "disorders personal and family, recent trauma or surgery, <b>medications &mdash; aspirin, "
  "warfarin, clopidogrel, intranasal glucocorticoids</b>, and cirrhosis, HIV or intranasal cocaine. "
  "<b>A prothrombin time with INR is NOT a routine test</b> &mdash; order it for the anticoagulated "
  "patient. Haematocrit and type and crossmatch in massive or prolonged haemorrhage, with "
  "<b>two large-bore intravenous lines</b>.",
  "<b>Initial tamponade, and patients can do it themselves:</b> blow the nose to clear clots &rarr; "
  "spray with <b>oxymetazoline</b> &rarr; <b>pinch the alae against the septum continuously for "
  "10 minutes</b>. Also: <b>sit up and lean forward at the waist</b> so blood is not swallowed, a "
  "cotton pledget in the nostril, spit out blood in the pharynx, cold compress on the bridge. Then "
  "<b>nasal tampons, gauze packing, balloon catheters, thrombogenic foams and gels</b>.",
  "Urgent",
  "<b>Teach these manoeuvres for use at home.</b> And <b>DO NOT BLOW THE NOSE</b> afterwards.",
  "45&ndash;51", D17),

 ("Epistaxis &mdash; posterior", BLEED,
  "<b>Sphenopalatine artery</b> &middot; significant haemorrhage &middot; <b>ASPIRATION risk</b>",
  "Arises most commonly from the <b>posterolateral branches of the sphenopalatine artery</b>, but "
  "may arise from branches of the carotid. <b>Results in significant haemorrhage.</b>",
  "<b>You must determine whether the bleed is anterior, posterior, or both.</b>",
  "As for anterior bleeding, escalating to packing and ENT involvement.",
  "Emergent",
  "<b>Posterior bleeds carry a higher risk because of ASPIRATION and subsequent infection</b> "
  "&mdash; that is why the distinction is made.",
  "45&ndash;46", D17),

 ("Nasal foreign body", FB,
  "<b>UNILATERAL foul-smelling purulent discharge in a young child</b>",
  "Commonest in <b>young children</b>. Most often on the <b>floor of the nasal passage just under "
  "the inferior turbinate</b>, or <b>superiorly just in front of the middle turbinate</b>. "
  "<b>Unilateral purulent and foul-smelling nasal discharge in a young child strongly suggests "
  "it.</b>",
  "<b>Visualisation establishes the diagnosis.</b> Imaging is rarely needed.",
  "Removal &mdash; instrument chosen by what the object is: <b>forceps for graspable objects</b>, "
  "a <b>wire loop, right-angle hook or curette for round smooth ones</b>, <b>suction for smooth or "
  "free-floating</b> beads, beans, magnets or batteries. <b>Get help &mdash; refer to ENT.</b>",
  "Urgent",
  "A one-sided smelly discharge in a toddler is a foreign body until proven otherwise, not "
  "sinusitis.",
  "53&ndash;55", D17),

 ("Nasal fracture", TRAUMA,
  "<b>Contusion and tenderness over the bridge = fracture</b> &middot; commonest facial fracture site",
  "From trauma. <b>Suspect other injuries &mdash; orbital and midface fractures.</b> <b>Associated "
  "with septal haematoma.</b> The <b>nasal bridge</b> is the commonest site. Examination: "
  "<b>palpate for tenderness, crepitus and abnormal movement</b>, and inspect with a nasal "
  "speculum.",
  "<b>X-rays are NOT needed if all four hold:</b> tenderness and swelling <b>isolated to the bony "
  "bridge</b>; the patient <b>can breathe through each naris</b>; the nose is <b>straight, with no "
  "septal deviation</b>; and there is <b>no septal haematoma</b>. If any fails, plain films.",
  "Initial treatment is <b>ice and head of bed elevated</b>.",
  "Urgent",
  "The four criteria are the useful thing to carry &mdash; they decide imaging at the bedside.",
  "56&ndash;58", D17),

 ("Nasal polyps", POLYP,
  "<b>Grey, glistening</b> masses &middot; <b>anosmia</b> &middot; asthma and <b>aspirin sensitivity</b>",
  "<b>Abnormal, grey, glistening masses filled with inflammatory material</b> in the nasal cavity "
  "or paranasal sinuses. Large or extensive polyps cause <b>congestion or blockage, thick "
  "discharge and ANOSMIA</b>. Frequently associated with <b>chronic rhinosinusitis, asthma and "
  "aspirin sensitivity &mdash; aspirin-exacerbated respiratory disease</b>. In children they occur "
  "with chronic sinusitis, allergic rhinitis, <b>cystic fibrosis</b> or allergic fungal sinusitis. "
  "<i>From the slide that is an image of a list:</i> associated conditions include "
  "<b>bronchial asthma 20&ndash;50%</b>, <b>cystic fibrosis 5&ndash;44%</b>, <b>allergic fungal "
  "sinusitis 85%</b>, <b>aspirin intolerance 8&ndash;20%</b>, <b>alcohol intolerance 50%</b>, "
  "<b>Churg-Strauss 50%</b>, primary ciliary dyskinesia, Young syndrome and <b>NARES 20%</b>.",
  "<b>Diagnosed clinically</b> by their appearance on nasal speculum or rhinoscopy, and "
  "identifiable on CT. <b>Chloride sweat test if cystic fibrosis is a concern</b>; full blood count "
  "with differential, <b>IgE and IgA</b>; consider a <b>nasal smear for eosinophils</b>; CT for "
  "extent or surgical planning.",
  "Medical: <b>non-drowsy oral antihistamine</b> (loratadine, fexofenadine, cetirizine, "
  "levocetirizine), <b>leukotriene inhibitor at night</b> (montelukast, zafirlukast), intranasal or "
  "oral steroids, <b>intranasal ipratropium</b>, immunotherapy, decongestants with caution. "
  "<b>Surgery gives only temporary relief &mdash; they recur within months to years.</b>",
  "Urgent",
  "<b>Evaluate EVERY child with benign multiple nasal polyposis for cystic fibrosis and "
  "asthma.</b> The deck gives that its own slide.",
  "59&ndash;65", D17),

 ("Allergic rhinitis", POLYP,
  "<b>CLEAR discharge from BOTH nostrils</b> &middot; <b>bluish, boggy</b> mucosa",
  "Rhinorrhoea secondary to allergy: the body treats the allergen as foreign and releases "
  "chemokines causing <b>hypermucosal production</b>. <b>Extremely common and rising.</b>",
  "<b>Clinical &mdash; mostly the history.</b> Findings: <b>clear discharge from each nostril</b>, "
  "a <b>bluish hue to the nasal mucosa</b>, <b>oedematous mucosa</b>, and <b>with or without nasal "
  "polyps</b>.",
  "<b>80% of patients end up on two or more allergy medicines.</b> Non-drowsy oral antihistamine "
  "by day and a drowsy one at night if needed; <b>leukotriene inhibitor at night</b>; intranasal "
  "steroids <b>with caution in chronic use</b>; immunotherapy; intranasal ipratropium; "
  "decongestants <b>with caution in chronic use and in high blood pressure</b>.",
  "Routine",
  "<b>Allergy does not cause &ldquo;-itis&rdquo; itself</b> &mdash; it creates the perfect "
  "environment for infection. Many patients who think they have sinusitis have allergic disease.",
  "13, 26, 66&ndash;68", D17),

 ("Nasopharyngeal carcinoma", NEO,
  "<b>Neck mass</b> + <b>diplopia</b> + facial numbness &middot; <b>Epstein-Barr virus</b>",
  "The predominant tumour arising in the nasopharynx. <b>Rare in the United States and Western "
  "Europe; endemic in Southern China including Hong Kong</b>, Southeast Asia, North Africa, the "
  "Middle East and the Arctic. <b>Two- to threefold more common in males.</b> Associated with "
  "<b>Epstein-Barr virus, human papillomavirus and smoking</b>, and with high-salt diets, Chinese "
  "herbs, rancid butter and sheep fat.",
  "Presents with <b>headache, diplopia, facial numbness and a mass in the neck</b>. "
  "<b>Referral to ENT and endoscopic guided biopsy of the primary tumour.</b>",
  "Oncological management following biopsy (ENT).",
  "Emergent",
  "The combination that should prompt referral is a <b>neck mass with cranial nerve symptoms</b>, "
  "not nasal symptoms alone.",
  "69&ndash;70", D17),

 ("Benign nasal neoplasms", NEO,
  "<b>Same as skin</b> &mdash; the dermatology lesions, on the nose",
  "The lecture defers to the dermatology block: <b>warts, freckles, haemangioma, port-wine "
  "stain</b> and the rest behave on the nose as they do elsewhere.",
  "As for the equivalent skin lesion.",
  "As for the equivalent skin lesion &mdash; see the dermatology lectures.",
  "Routine",
  "Worth knowing only as the counterpart to the malignant list; the detail lives in the "
  "dermatology material.",
  "71", D17),
]

DIFF_L17 = {
 "Acute sinusitis (rhinosinusitis)": ("<b>Pressure</b>; frank pain suggests bacterial",
   "<b>Rhinorrhoea</b>, postnasal drip", "Pain <b>worse bending forward</b>"),
 "Bacterial sinusitis &mdash; the features that suggest it": ("<b>YES &mdash; and REPRODUCIBLE on palpation</b>",
   "Purulent, sometimes <b>putrid</b>", "<b>UNILATERAL</b> maxillary tenderness"),
 "Sinusitis with urgent features": ("<b>YES</b>", "Any", "<b>Diplopia, periorbital swelling, confusion</b>"),
 "Chronic bacterial sinusitis": ("Pressure, with flares", "Constant congestion", "<b>&gt;12 weeks</b>"),
 "Chronic fungal sinusitis": ("Variable", "<b>Peanut-butter mucus</b> in the allergic form",
   "<b>Fungus ball</b> on imaging"),
 "Deviated septum": ("No, unless severe", "Congestion; recurrent bleeds",
   "<b>One passage smaller</b>"),
 "Perforated septum": ("No", "Crusting, whistling", "<b>Visible perforation</b>"),
 "Septal haematoma": ("<b>YES</b>", "Obstruction", "<b>Swelling between septum and perichondrium</b>"),
 "Epistaxis &mdash; anterior": ("No", "<b>Frank blood, anteriorly</b>", "<b>Kiesselbach&rsquo;s plexus</b>"),
 "Epistaxis &mdash; posterior": ("No", "<b>Heavy; blood in the pharynx</b>", "<b>Sphenopalatine artery</b>"),
 "Nasal foreign body": ("Variable", "<b>UNILATERAL, purulent, FOUL-SMELLING</b>",
   "<b>Object visible</b> under a turbinate"),
 "Nasal fracture": ("<b>YES</b>", "Epistaxis", "<b>Tenderness and crepitus over the bridge</b>"),
 "Nasal polyps": ("No", "Thick discharge", "<b>Grey glistening masses</b>; <b>ANOSMIA</b>"),
 "Allergic rhinitis": ("No", "<b>CLEAR, BILATERAL</b>", "<b>Bluish, boggy mucosa</b>"),
 "Nasopharyngeal carcinoma": ("<b>Headache</b>", "May be bloody",
   "<b>Neck mass + cranial nerve signs</b>"),
 "Benign nasal neoplasms": ("No", "None", "As the equivalent skin lesion"),
}

IMGS_L17 = {
 "Acute sinusitis (rhinosinusitis)": ("l17-s007_pos1.jpg", 7),
 "Bacterial sinusitis &mdash; the features that suggest it": ("l17-s015_pos1.jpg", 15),
 "Deviated septum": ("l17-s036_pos1.jpg", 36),
 "Perforated septum": ("l17-s038_pos1.jpg", 38),
 "Septal haematoma": ("l17-s042_pos1.jpg", 42),
 "Epistaxis &mdash; anterior": ("l17-s047_pos2.jpg", 47),
 "Epistaxis &mdash; posterior": ("l17-s052_pos2.jpg", 52),
 "Nasal foreign body": ("l17-s053_pos2.jpg", 53),
 "Nasal fracture": ("l17-s058_pos3.jpg", 58),
 "Nasal polyps": ("l17-s061_pos1.jpg", 61),
 "Allergic rhinitis": ("l17-s062_pos1.jpg", 62),
}
