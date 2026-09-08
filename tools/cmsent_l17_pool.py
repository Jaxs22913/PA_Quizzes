# -*- coding: utf-8 -*-
"""Lecture 17 questions for the ENT master exams -- Nose and Paranasal Sinuses."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "hughie Nose & Paranasal Sinuses"
IO = ("Disorders of the nose and paranasal sinuses: etiologies, epidemiology, risk factors, "
      "clinical manifestations, differential diagnosis, diagnostic testing, management, referrals, "
      "patient education, and prognosis")

QUESTIONS = [

Q("Bacterial sinusitis", IO,
  "A 25-year-old patient has had ten days of nasal congestion, purulent discharge, facial pressure "
  "and reduced sense of smell. Symptoms have not improved with a week of oral decongestants and "
  "saline irrigation. Temperature is 100.8 degrees Fahrenheit. There is maxillary sinus tenderness "
  "and thick yellow-green discharge.",
  [["Amoxicillin-clavulanate 875 milligrams orally twice daily",
    "Correct. Symptoms persisting ten days or more without improvement is one of the criteria that "
    "shifts a rhinosinusitis from the 90 to 98 per cent that are viral into the small bacterial "
    "minority. Amoxicillin-clavulanate is first line because the clavulanate covers the "
    "beta-lactamase producing Haemophilus influenzae and Moraxella catarrhalis alongside "
    "pneumococcus."],
   ["Continued decongestants and saline irrigation",
    "This is the correct management for the first week and it has already been tried and failed. "
    "Persisting past ten days with fever and purulence is specifically the point at which "
    "symptomatic treatment alone stops being adequate."],
   ["Azithromycin 500 milligrams daily for three days",
    "Macrolides have substantial pneumococcal resistance in respiratory isolates and are reserved "
    "for genuine penicillin allergy. Choosing one without an allergy trades away efficacy against "
    "the main pathogen for no benefit."],
   ["Ciprofloxacin 500 milligrams orally twice daily",
    "A fluoroquinolone has poor pneumococcal coverage relative to its side effect burden, and "
    "reaching for one in uncomplicated sinusitis exposes the patient to tendon and central nervous "
    "system effects while covering the likeliest organism less well."]],
  "treatment", D, 15),

Q("Acute sinusitis", IO,
  "A 30-year-old woman has had four days of nasal congestion, clear-to-yellow discharge and facial "
  "pressure worse when she bends forward, following a cold. She is afebrile and feels gradually "
  "better than two days ago.",
  [["Symptomatic treatment without antibiotics",
    "Correct. Between 90 and 98 per cent of acute rhinosinusitis is viral, and the features that "
    "would suggest bacterial infection are absent: it has been under ten days, she is improving "
    "rather than showing double worsening, and she is afebrile. Discharge colour does not indicate "
    "bacterial infection, so the treatment is decongestants, analgesia and saline."],
   ["Immediate amoxicillin-clavulanate",
    "Antibiotics at day four in an improving afebrile patient treat a virus. Acute rhinosinusitis is "
    "the fifth leading reason antibiotics are prescribed, which is precisely the over-prescription "
    "this presentation should avoid."],
   ["Computed tomography of the sinuses",
    "Imaging does not distinguish viral from bacterial sinusitis, because both fill the sinuses, and "
    "it is not indicated routinely. It is reserved for suspected complications or for chronic "
    "disease being considered for surgery."],
   ["Sinus puncture for culture",
    "Puncture is invasive, reserved for treatment failure in complicated or immunocompromised "
    "patients, and gives no useful information in a self-limiting illness that is already "
    "improving."]],
  "treatment", D, 12),

Q("Sinusitis with urgent features", IO,
  "A 19-year-old man with a week of sinusitis symptoms now has swelling and erythema around the "
  "right eye, pain on eye movement and double vision. He is febrile.",
  [["Urgent imaging and admission for intravenous antibiotics",
    "Correct. Periorbital swelling with painful restricted eye movement and diplopia means the "
    "infection has crossed from the sinus into the orbit, because the ethmoid sinus is separated "
    "from it only by the paper-thin lamina papyracea. That is orbital cellulitis, which threatens "
    "vision and can spread intracranially, so it needs imaging and intravenous therapy now."],
   ["Oral amoxicillin-clavulanate and review in 48 hours",
    "Oral therapy at home is right for uncomplicated bacterial sinusitis but far too slow for "
    "infection that has already entered the orbit. Forty-eight hours is long enough for vision to "
    "be lost or for cavernous sinus thrombosis to develop."],
   ["Topical decongestants and nasal steroid",
    "Symptomatic measures address congestion but do nothing about an established orbital infection. "
    "Using them here delays definitive treatment while the patient looks as though something is "
    "being done."],
   ["Ophthalmology referral for the diplopia alone",
    "Referring the eye symptom in isolation treats a sign as though it were the disease. The "
    "diplopia is a consequence of an infection that needs systemic treatment, and both the sinus "
    "and the orbit have to be managed together."]],
  "next step", D, 20),

Q("Nasal foreign body", IO,
  "A 4-year-old boy has had two weeks of purulent nasal discharge. He has been afebrile with no "
  "respiratory symptoms. His mother says he gets into everything. Examination shows right-sided "
  "purulent discharge that is greenish-brown and extraordinarily foul-smelling.",
  [["Direct visualisation of the right nasal vestibule",
    "Correct. Unilateral, foul-smelling purulent discharge in a young child is a retained nasal "
    "foreign body until proven otherwise, because an obstructing object traps secretions that "
    "stagnate and become malodorous. Looking directly into the vestibule both makes the diagnosis "
    "and allows the object to be removed, which is the treatment."],
   ["Culture and sensitivity of the nasal discharge",
    "Culture will grow the mixed flora that colonises stagnant secretions, which tells you nothing "
    "you did not already suspect and does not remove the object. The infection will recur as long "
    "as the obstruction remains."],
   ["Sinus radiographs",
    "Plain films of the sinuses are insensitive, will miss the radiolucent plastic or foam that "
    "children usually insert, and irradiate a child to answer a question that direct inspection "
    "answers immediately."],
   ["Soft tissue lateral radiograph of the nasopharynx",
    "That film is used to look for adenoidal enlargement or a retropharyngeal collection. It images "
    "the wrong plane for a foreign body sitting in the nasal cavity and would not guide removal."]],
  "testing", D, 51),

Q("Epistaxis", IO,
  "A 73-year-old man comes to the emergency department with a nosebleed lasting over two hours. "
  "There is no trauma and no bleeding disorder. He is holding a blood-soaked towel; there is brisk "
  "bleeding from both nostrils and the site cannot be seen. He feels dizzy and appears confused.",
  [["Start an intravenous line and give fluids",
    "Correct. Dizziness and confusion in someone who has bled briskly for two hours are signs of "
    "haemodynamic compromise, and resuscitation precedes definitive control of the bleeding point. "
    "Bleeding from both nostrils with no visible anterior source suggests a posterior bleed from the "
    "sphenopalatine artery, which is the type that causes significant blood loss."],
   ["Pinch the nose",
    "Direct pressure on the alae compresses Kiesselbach plexus and is the correct first move for an "
    "anterior bleed in a stable patient. It has already failed here, it cannot reach a posterior "
    "source, and it does not address the circulating volume he has lost."],
   ["Spray a topical anaesthetic and decongestant",
    "Vasoconstriction is a genuine step in controlling epistaxis and will be needed, but it comes "
    "after the patient is stabilised. Treating the nose first in someone who is confused from blood "
    "loss inverts the priority."],
   ["Burn the bleeding vessels with cautery",
    "Cautery requires a visible bleeding point, and the site explicitly cannot be seen. Blind "
    "cautery damages mucosa, risks septal perforation, and does not control a posterior source."]],
  "next step", D, 40),

Q("Epistaxis", IO,
  "A 9-year-old boy has recurrent nosebleeds from the left nostril, each stopping within ten "
  "minutes with pressure. He has no bruising elsewhere, takes no medication, and picks his nose "
  "frequently. It is winter.",
  [["Anterior epistaxis from Kiesselbach plexus, managed conservatively",
    "Correct. Ninety per cent of nosebleeds are anterior, arising from Kiesselbach plexus on the "
    "anterior septum where several arteries anastomose in thin mucosa. Digital trauma is the "
    "commonest cause, and dry winter air cracks the mucosa further. Short bleeds stopped by pressure "
    "in a well child need humidification and behaviour change rather than investigation."],
   ["Posterior epistaxis requiring packing",
    "Posterior bleeds arise from the sphenopalatine artery, are usually heavier, often bleed from "
    "both nostrils or down the throat, and do not stop reliably with ten minutes of pressure. They "
    "are also uncommon in children."],
   ["A coagulopathy requiring urgent clotting studies",
    "Coagulation testing is not routine for epistaxis and is reserved for patients on "
    "anticoagulants or with other bleeding signs. This child has no bruising, no family history and "
    "no medication, and has an obvious mechanical cause."],
   ["Juvenile nasopharyngeal angiofibroma",
    "That tumour does cause epistaxis in young males, but it presents with profuse unilateral "
    "bleeding and progressive obstruction from a nasopharyngeal mass, not brief self-limiting bleeds "
    "in a nose-picking child."]],
  "diagnosis", D, 37),

Q("Septal haematoma", IO,
  "A 16-year-old girl is struck in the nose during a hockey match. She has swelling and tenderness "
  "over the bridge. Examination of the nasal cavity shows bilateral bluish, boggy swelling of the "
  "septum that is soft to touch.",
  [["Drain it, because untreated it destroys the septal cartilage",
    "Correct. Blood collecting between the septal cartilage and its perichondrium strips the "
    "cartilage of its only blood supply, and the cartilage necroses within days, producing a saddle "
    "nose deformity and septal perforation. It can also abscess. Drainage through an intranasal "
    "incision is therefore urgent rather than elective."],
   ["Ice, analgesia and review in one week",
    "A week is long enough for avascular necrosis of the cartilage to be complete. Conservative "
    "management is appropriate for the surrounding contusion but not for a collection that is "
    "actively depriving cartilage of its blood supply."],
   ["Nasal packing to compress the swelling",
    "Packing applies pressure but does not evacuate blood that has already collected under the "
    "perichondrium, so the cartilage remains stripped. It may also obscure the diagnosis while the "
    "damage continues."],
   ["Radiography to exclude a nasal fracture first",
    "A fracture may well coexist and is worth knowing about, but imaging does not change the "
    "immediate need to drain, and delaying drainage to obtain a film that will not alter that step "
    "wastes the window in which cartilage is salvageable."]],
  "next step", D, 32),

Q("Nasal fracture", IO,
  "A 27-year-old man is punched in the nose. He has tenderness and swelling isolated to the bony "
  "bridge, breathes freely through each nostril, the nose is straight with no septal deviation, and "
  "there is no septal haematoma.",
  [["Ice and elevation, without radiography",
    "Correct. All four reassuring criteria are met: tenderness confined to the bony bridge, patent "
    "airflow through each side, a straight nose with no septal deviation, and no septal haematoma. "
    "A radiograph would not change management in that situation, because the treatment of an "
    "undisplaced nasal fracture is symptomatic in any case."],
   ["Plain radiography of the nasal bones",
    "Films are ordered when one of those four criteria fails, because that is when displacement or "
    "an associated injury might change management. Ordering them reflexively in a patient who meets "
    "all four adds radiation and cost without altering treatment."],
   ["Immediate closed reduction",
    "Reduction is for a displaced fracture producing deformity or obstruction. This nose is straight "
    "and patent, so there is nothing to reduce, and manipulating it risks creating the deformity it "
    "is meant to correct."],
   ["Computed tomography of the facial bones",
    "Facial computed tomography is reserved for suspected complex midface injury, orbital "
    "involvement or when the examination is unreliable. An isolated bridge injury with a normal "
    "examination does not warrant it."]],
  "next step", D, 46),

Q("Nasal polyps", IO,
  "A 7-year-old boy is found to have multiple grey, glistening masses in both nasal cavities, with "
  "chronic congestion and reduced sense of smell.",
  [["Test for cystic fibrosis with a sweat chloride test",
    "Correct. Nasal polyps are distinctly unusual in children, and between 5 and 44 per cent of "
    "children with cystic fibrosis have them. Finding multiple polyps in a child is therefore an "
    "indication to look for the underlying systemic disease rather than simply to treat the polyps, "
    "and asthma should be assessed at the same time."],
   ["Prescribe an intranasal steroid and review in three months",
    "Topical steroid is reasonable symptomatic treatment for polyps, but using it alone in a child "
    "means treating the visible problem while missing the diagnosis it is pointing to. The "
    "association with cystic fibrosis is the reason paediatric polyps are handled differently."],
   ["Refer for polypectomy",
    "Surgery gives only temporary relief because polyps recur, and it does not address the "
    "underlying cause. Operating before investigating leaves a child with an undiagnosed systemic "
    "disease."],
   ["Start antihistamines for presumed allergic rhinitis",
    "Allergy is associated with polyps in adults, but antihistamines do not shrink established "
    "polyps, and attributing paediatric polyps to allergy without excluding cystic fibrosis misses "
    "the association that matters most at this age."]],
  "next step", D, 63),

Q("Allergic rhinitis", IO,
  "A 22-year-old woman has clear discharge from both nostrils, sneezing and itchy eyes each spring. "
  "The nasal mucosa is boggy with a bluish hue and the turbinates are swollen.",
  [["Allergic rhinitis",
    "Correct. Bilateral clear rhinorrhoea with a bluish, boggy, oedematous mucosa is the "
    "characteristic appearance, and the seasonal pattern with itchy eyes points to an "
    "immunoglobulin E mediated response to a pollen. The mucosal colour is the discriminating "
    "physical finding, since infective rhinitis produces erythema rather than a bluish hue."],
   ["Acute bacterial sinusitis",
    "Bacterial sinusitis produces purulent rather than clear discharge, facial pain and pressure, "
    "and often fever, and it is not seasonal or accompanied by itchy eyes. The mucosa is "
    "erythematous rather than bluish."],
   ["Nasal foreign body",
    "A foreign body gives UNILATERAL foul-smelling purulent discharge, which is the opposite of the "
    "bilateral clear discharge described, and it does not recur predictably each spring."],
   ["Vasomotor rhinitis",
    "Vasomotor rhinitis also gives clear bilateral discharge, so it is a fair consideration, but it "
    "is triggered by temperature change, odours or alcohol rather than by season, and it lacks the "
    "itch and ocular symptoms of an allergic response."]],
  "diagnosis", D, 66),

Q("Nasopharyngeal carcinoma", IO,
  "A 44-year-old man of southern Chinese origin has a firm neck mass, intermittent double vision "
  "and numbness of the left cheek, with unilateral nasal obstruction and occasional blood-stained "
  "nasal discharge.",
  [["Nasopharyngeal carcinoma",
    "Correct. The combination of a neck mass, cranial nerve involvement giving diplopia and facial "
    "numbness, and unilateral nasal symptoms is the described presentation. The tumour sits in the "
    "nasopharynx where it drains early to cervical nodes and can invade the skull base, and it is "
    "strongly associated with Epstein-Barr virus and endemic in southern China."],
   ["Chronic bacterial sinusitis",
    "Chronic sinusitis causes congestion and discharge over months but does not produce a firm neck "
    "mass or cranial nerve deficits. Diplopia and facial numbness indicate invasion rather than "
    "mucosal inflammation."],
   ["Nasal polyposis",
    "Polyps cause bilateral obstruction and anosmia with grey glistening masses visible in the nasal "
    "cavity. They do not metastasise to neck nodes and do not involve cranial nerves."],
   ["Allergic rhinitis",
    "Allergic disease is bilateral, gives clear discharge and itch, and has no mass effect. Nothing "
    "about a neck node, blood-stained discharge or a numb cheek fits an allergic mechanism."]],
  "diagnosis", D, 70),

Q("Perforated septum", IO,
  "A 39-year-old man has nasal crusting, whistling on inspiration and recurrent minor nosebleeds. "
  "Examination shows a septal perforation. He has used intranasal steroid for years for allergic "
  "rhinitis.",
  [["Chronic ischaemia of the septal mucosa, from intranasal steroid or cocaine use",
    "Correct. The anterior septum has a thin mucosa over cartilage with no other blood supply, so "
    "anything that causes sustained vasoconstriction or mucosal injury there can perforate it. "
    "Prolonged intranasal steroid, particularly if sprayed at the septum rather than laterally, and "
    "cocaine are the two named causes, and the history has to ask about both."],
   ["Nasal polyps eroding the septum",
    "Polyps are soft oedematous mucosal masses that obstruct the airway. They do not erode cartilage "
    "or produce a perforation, and they would be visible on examination."],
   ["Untreated allergic rhinitis itself",
    "Allergy inflames and swells the mucosa but does not destroy septal cartilage. It is the "
    "treatment in this case, rather than the disease, that carries the risk."],
   ["A previous undiagnosed nasal fracture",
    "A fracture can be associated with a septal haematoma, and an untreated haematoma does perforate "
    "the septum, but that pathway requires the haematoma. A fracture alone does not perforate the "
    "septum years later without one."]],
  "cause", D, 29),
]
