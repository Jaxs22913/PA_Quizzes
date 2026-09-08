# -*- coding: utf-8 -*-
from _pd2_ent_osce_data import E
BATCH = {

"Acute sinusitis (rhinosinusitis)": E(
  "&ldquo;My face aches and my nose is blocked &mdash; it started as a cold about four days "
  "ago.&rdquo;",
  "<b>Palpate and percuss over the frontal and maxillary sinuses.</b> Anterior rhinoscopy for "
  "mucosal oedema and discharge. Transillumination. <b>Examine the eyes and mental state to exclude "
  "the complications</b> &mdash; that is the part that changes management.",
  [("Viral upper respiratory infection", "Under 10 days, improving, without the bacterial features"),
   ("Allergic rhinitis", "Itch and sneezing with clear discharge and pale boggy turbinates"),
   ("Dental infection", "Unilateral maxillary pain with a tender tooth on percussion")],
  "<b>Clinical</b> &rarr; congestion, purulent discharge and facial pain or pressure. Imaging is "
  "NOT indicated in uncomplicated disease &mdash; opacity is common in simple colds and does not "
  "distinguish viral from bacterial.",
  "Full painless eye movements with normal vision and mental state exclude the complications; "
  "improvement by day 10 argues against bacterial disease; a tender tooth redirects to dental origin."),

"Bacterial sinusitis &mdash; the features that suggest it": E(
  "&ldquo;I was getting better after a week and then it came back worse with a fever.&rdquo;",
  "The same sinus examination, but the diagnosis is made from the <b>time course</b>: symptoms "
  "<b>persisting beyond 10 days without improvement</b>, <b>severe symptoms with fever for 3 to 4 "
  "days at onset</b>, or <b>double worsening</b> after initial improvement. Check for complications.",
  [("Viral rhinosinusitis", "Peaks at days 3 to 6 and improves &mdash; no double worsening"),
   ("Allergic rhinitis", "Itch, sneezing, clear discharge, and it is seasonal or exposure-linked"),
   ("Complicated sinusitis", "Eye or neurological signs; the tier above this one")],
  "<b>Clinical</b> &rarr; one of the three time-course patterns above. <b>Computed tomography</b> "
  "only if complications or failure of therapy &rarr; air-fluid levels with mucosal thickening.",
  "Steady improvement within 10 days excludes it; purulence ALONE does not confirm it, since viral "
  "infection turns purulent too; normal eye examination excludes orbital spread."),

"Chronic bacterial sinusitis": E(
  "&ldquo;My nose has been blocked and running for months and I&rsquo;ve lost my sense of "
  "smell.&rdquo;",
  "Anterior rhinoscopy for polyps, oedema and purulence. <b>Assess smell.</b> Palpate the sinuses. "
  "Look for the underlying cause: allergy, a deviated septum, dental disease, immune deficiency.",
  [("Nasal polyps", "Pale, insensate, mobile grape-like masses; often coexist"),
   ("Allergic rhinitis", "Itch and sneezing dominate; symptoms fluctuate with exposure"),
   ("Sinonasal neoplasm", "Unilateral obstruction with bleeding or facial numbness")],
  "<b>Symptoms lasting 12 weeks or more</b> PLUS objective evidence: <b>nasal endoscopy</b> &rarr; "
  "purulence, oedema or polyps in the middle meatus; <b>computed tomography of the sinuses</b> "
  "&rarr; mucosal thickening and sinus opacification. Symptoms alone are not enough.",
  "A normal endoscopy and normal scan exclude it despite the symptoms; unilateral disease with "
  "bleeding demands biopsy to exclude tumour; allergy testing identifies a treatable driver."),

"Chronic fungal sinusitis": E(
  "&ldquo;One side of my nose has been blocked for ages and the treatments haven&rsquo;t "
  "worked.&rdquo;",
  "Anterior rhinoscopy and endoscopy, particularly for <b>unilateral disease</b>. <b>Assess immune "
  "status and glycaemic control</b> &mdash; that determines whether this is the indolent form or "
  "the invasive one. In the immunocompromised, <b>look for black necrotic mucosa</b>, which is an "
  "emergency.",
  [("Chronic bacterial sinusitis", "Usually bilateral and responds to antibiotics"),
   ("Sinonasal neoplasm", "Unilateral too, with bleeding and bone destruction"),
   ("Invasive fungal sinusitis", "Necrotic eschar with rapid progression in an immunocompromised patient")],
  "<b>Computed tomography</b> &rarr; unilateral opacification, often with <b>hyperdense material "
  "and calcification</b> within the sinus. <b>Endoscopy with biopsy and fungal culture</b> &rarr; "
  "fungal elements; <b>tissue invasion on histology is what defines the invasive form</b>.",
  "Histology showing no tissue invasion means the non-invasive form and a very different urgency; "
  "biopsy excludes carcinoma; a normal scan excludes it."),

"Deviated septum": E(
  "&ldquo;I&rsquo;ve never been able to breathe through this side, and it&rsquo;s worse at "
  "night.&rdquo;",
  "Anterior rhinoscopy with a speculum, <b>looking at both sides and comparing</b>. <b>Occlude one "
  "nostril at a time and test airflow.</b> Look for a septal spur. Check the external nasal "
  "pyramid for deformity.",
  [("Turbinate hypertrophy", "Obstruction from swollen turbinates that shrink with a decongestant"),
   ("Nasal polyps", "Pale mobile masses; the septum itself is straight"),
   ("Allergic rhinitis", "Bilateral and fluctuating, with itch and sneezing")],
  "<b>Anterior rhinoscopy</b> &rarr; visible septal deviation narrowing one side, with reduced "
  "airflow on that side. <b>Decongestant challenge</b> &rarr; obstruction PERSISTS, since bone and "
  "cartilage do not shrink; that is the key discriminator.",
  "Obstruction relieved by a decongestant means turbinate hypertrophy, not the septum; visible "
  "polyps redirect; a straight septum excludes it."),

"Perforated septum": E(
  "&ldquo;My nose whistles when I breathe, it crusts, and it bleeds a bit.&rdquo;",
  "Anterior rhinoscopy &mdash; <b>shine a light in one nostril and look for it through the "
  "other</b>. Measure and site the perforation. <b>Take a history of cocaine use, nose picking, "
  "prior surgery and vasculitis symptoms.</b>",
  [("Granulomatosis with polyangiitis", "Perforation with crusting PLUS systemic and renal disease"),
   ("Cocaine-induced perforation", "Often large and progressive, with a use history"),
   ("Postsurgical or traumatic", "A history that explains it, and it does not progress")],
  "<b>Rhinoscopy</b> &rarr; a through-and-through defect. <b>Antineutrophil cytoplasmic antibody, "
  "inflammatory markers, urinalysis</b> &rarr; positive in vasculitis. <b>Biopsy of the edge</b> "
  "&rarr; granulomatous inflammation or malignancy.",
  "Negative vasculitis serology with normal urinalysis excludes granulomatosis; a benign biopsy "
  "excludes malignancy; a clear surgical history explains a stable perforation."),

"Septal haematoma": E(
  "&ldquo;I broke my nose and now I can&rsquo;t breathe through either side.&rdquo;",
  "<b>Anterior rhinoscopy in EVERY nasal trauma</b> &mdash; this is the reason the examination is "
  "mandatory. Look for a <b>bluish, boggy swelling of the septum, usually bilateral</b>. "
  "<b>Palpate with a cotton applicator &mdash; it is fluctuant and compressible</b>, unlike a "
  "deviated septum.",
  [("Deviated septum", "Firm, not compressible, and asymmetric rather than bilateral"),
   ("Nasal fracture with swelling", "Soft tissue swelling outside; the septum itself is normal"),
   ("Septal abscess", "The same swelling with fever and pain &mdash; the sequel if it is missed")],
  "<b>Anterior rhinoscopy with palpation</b> &rarr; a compressible bilateral septal swelling. "
  "<b>Needle aspiration</b> &rarr; blood, which confirms it. Left alone it destroys the cartilage "
  "and produces a saddle nose deformity.",
  "A firm non-compressible septum is a deviation; fever with purulent aspirate means abscess; "
  "clear rhinoscopy excludes it."),

"Epistaxis &mdash; anterior": E(
  "&ldquo;My nose started bleeding and I can&rsquo;t get it to stop.&rdquo;",
  "<b>Have the patient blow out clots</b>, then anterior rhinoscopy with good light to <b>find the "
  "bleeding point on Kiesselbach plexus</b>. <b>Pinch the soft part of the nose for 10 to 15 "
  "minutes, leaning FORWARD</b> &mdash; forward, not back, so blood is not swallowed. Check "
  "circulation and look in the throat for a posterior source.",
  [("Posterior epistaxis", "No visible anterior point; blood running down the pharynx"),
   ("Bleeding disorder or anticoagulation", "Recurrent, bilateral, with bruising elsewhere"),
   ("Sinonasal or nasopharyngeal tumour", "Recurrent unilateral bleeding with obstruction or a neck mass")],
  "<b>Anterior rhinoscopy</b> &rarr; a visible anterior septal bleeding point that stops with "
  "pressure. That IS the confirmation &mdash; 90% of nosebleeds are anterior.",
  "Bleeding continuing with no visible point, and blood in the pharynx, means a posterior source; "
  "<b>full blood count and coagulation studies</b> &rarr; thrombocytopenia or a raised "
  "international normalised ratio if recurrent; endoscopy excludes a tumour."),

"Nasal foreign body": E(
  "A parent says &ldquo;she&rsquo;s had a smelly discharge from one side of her nose for a "
  "week.&rdquo; The insertion is usually unwitnessed.",
  "<b>Unilateral foul purulent discharge in a child IS a foreign body until proven otherwise.</b> "
  "Anterior rhinoscopy with good light and suction. <b>Examine the other nostril and both ears "
  "too</b> &mdash; children rarely stop at one. Identify a <b>button battery, which is an "
  "emergency</b>.",
  [("Unilateral sinusitis", "Discharge without an object; far less common at this age"),
   ("Choanal atresia", "Congenital, present from birth, with clear rather than foul discharge"),
   ("Rhinolith", "A calcified mass around a long-retained object")],
  "<b>Anterior rhinoscopy</b> &rarr; direct visualisation of the object. <b>Imaging</b> only if a "
  "battery or magnet is suspected and not seen &rarr; the object with its characteristic outline.",
  "A clear nasal cavity on both sides excludes it; bilateral clear discharge suggests rhinitis; "
  "resolution of the discharge after removal confirms the cause."),

"Nasal fracture": E(
  "&ldquo;I took a blow to the nose, it bled, and now it looks crooked.&rdquo;",
  "Inspect for deformity from the front and from ABOVE. Palpate for crepitus and step-off. "
  "<b>Anterior rhinoscopy for a septal haematoma &mdash; mandatory.</b> Test airflow each side. "
  "<b>Check for clear rhinorrhoea, which could be cerebrospinal fluid.</b> Examine eye movements "
  "and vision.",
  [("Septal haematoma", "The complication that must be found now, not at follow-up"),
   ("Orbital floor fracture", "Diplopia, restricted upgaze and infraorbital numbness"),
   ("Soft tissue injury alone", "Swelling and bruising with no bony step or deformity")],
  "<b>Clinical</b> &rarr; deformity, crepitus and epistaxis. <b>Plain films are NOT routinely "
  "useful.</b> <b>Computed tomography</b> if other facial fractures are suspected &rarr; the "
  "fracture pattern and orbital involvement.",
  "Absence of a septal swelling on rhinoscopy excludes haematoma; full painless eye movements "
  "exclude orbital entrapment; testing clear rhinorrhoea for beta-2 transferrin excludes a "
  "cerebrospinal fluid leak."),

"Nasal polyps": E(
  "&ldquo;Both sides of my nose are blocked, it&rsquo;s been going on for months, and I "
  "can&rsquo;t smell anything.&rdquo;",
  "Anterior rhinoscopy for <b>pale, grey, grape-like, MOBILE and INSENSATE masses</b> &mdash; "
  "touching them does not hurt, which distinguishes them from turbinates. Assess smell. <b>Ask "
  "about asthma and aspirin sensitivity</b>. <b>In a child, think cystic fibrosis; unilateral "
  "polyps in an adult mean imaging and biopsy.</b>",
  [("Hypertrophied turbinate", "Pink, sensitive to touch, and it shrinks with a decongestant"),
   ("Inverted papilloma", "Unilateral, may harbour carcinoma &mdash; the reason unilateral is never assumed benign"),
   ("Sinonasal malignancy", "Unilateral with bleeding, pain or facial numbness")],
  "<b>Endoscopy</b> &rarr; polyps in the middle meatus. <b>Computed tomography</b> &rarr; polypoid "
  "soft tissue opacifying the sinuses. <b>Sweat chloride test in a child</b> &rarr; raised in "
  "cystic fibrosis. <b>Biopsy of a unilateral polyp</b> &rarr; excludes papilloma and carcinoma.",
  "A pink tender structure that shrinks with a decongestant is a turbinate; benign histology "
  "excludes malignancy; bone destruction on imaging redirects to tumour."),

"Allergic rhinitis": E(
  "&ldquo;My nose runs and itches, I sneeze in fits, and my eyes water &mdash; it&rsquo;s worst in "
  "spring.&rdquo;",
  "Anterior rhinoscopy for <b>pale, bluish, boggy turbinates with clear discharge</b>. Look for the "
  "<b>allergic salute crease, allergic shiners and Dennie-Morgan lines</b>. Examine the "
  "conjunctivae. Check for polyps and assess for asthma and eczema.",
  [("Viral rhinitis", "Days rather than a season, with sore throat and no itch"),
   ("Vasomotor rhinitis", "Triggered by temperature, odours and food; no itch or sneezing fits"),
   ("Nasal polyps", "Obstruction and anosmia with visible pale masses")],
  "<b>Clinical</b> &rarr; itch, sneezing, clear rhinorrhoea and boggy pale turbinates with a "
  "trigger pattern. <b>Skin prick testing or specific immunoglobulin E</b> &rarr; sensitisation to "
  "the suspected allergen, which guides avoidance and immunotherapy.",
  "Purulent discharge with facial pain redirects to sinusitis; negative allergy testing with "
  "trigger-related symptoms suggests vasomotor rhinitis; a short self-limiting course is viral."),

"Benign nasal neoplasms": E(
  "&ldquo;One side of my nose has been blocked for months and it bleeds now and then.&rdquo;",
  "Anterior rhinoscopy and endoscopy, <b>noting that the lesion is UNILATERAL</b>. Assess for "
  "facial numbness, eye signs and proptosis. Palpate the neck. <b>In an adolescent boy with "
  "recurrent bleeding, do NOT biopsy &mdash; consider angiofibroma and image first.</b>",
  [("Nasal polyps", "Bilateral, pale and insensate; unilateral disease is the alarm"),
   ("Inverted papilloma", "Unilateral, locally aggressive, and carries a risk of carcinoma"),
   ("Sinonasal malignancy", "Bone destruction, pain, numbness or an orbital or neck sign")],
  "<b>Endoscopy</b> &rarr; a unilateral mass. <b>Computed tomography and magnetic resonance</b> "
  "&rarr; extent and whether bone is remodelled (benign) or destroyed (malignant). <b>Biopsy</b> "
  "&rarr; the histological diagnosis &mdash; except where imaging suggests a vascular lesion.",
  "Bilateral pale mobile masses are polyps; a strongly enhancing mass in a teenage boy means "
  "angiofibroma and blind biopsy is contraindicated; benign histology with bone remodelling "
  "excludes carcinoma."),
}
