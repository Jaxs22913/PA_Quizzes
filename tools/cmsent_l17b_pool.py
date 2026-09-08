# -*- coding: utf-8 -*-
"""Lecture 17, second pool -- Nose and Paranasal Sinuses."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "hughie Nose & Paranasal Sinuses"
IO = ("Disorders of the nose and paranasal sinuses: etiologies, epidemiology, risk factors, "
      "clinical manifestations, differential diagnosis, diagnostic testing, management, referrals, "
      "patient education, and prognosis")

QUESTIONS = [

Q("Bacterial sinusitis", IO,
  "A 34-year-old woman had a cold that improved over five days, then abruptly worsened on day seven "
  "with fever, unilateral cheek pain and purulent discharge.",
  [["Double worsening, which suggests bacterial superinfection",
    "Correct. A viral rhinosinusitis follows a single curve: worse, then steadily better. A second "
    "deterioration after initial improvement means something new has happened, and bacterial "
    "superinfection is the usual explanation. Double worsening is one of the named criteria, "
    "alongside symptoms lasting ten days or more and unilateral facial or tooth pain."],
   ["A normal viral course that needs no intervention",
    "A normal viral course does not improve and then relapse with fever and unilateral purulence. "
    "The pattern of deterioration is precisely what distinguishes the small bacterial minority from "
    "the 90 to 98 per cent that are viral."],
   ["Allergic rhinitis triggered by the viral illness",
    "Allergic disease gives bilateral clear rhinorrhoea with itch and a bluish boggy mucosa, and it "
    "does not cause fever or unilateral facial pain. The discharge described is purulent."],
   ["A nasal foreign body",
    "A foreign body causes unilateral foul purulent discharge, usually in a young child, and it does "
    "not follow a cold or produce a biphasic course. In an adult with a clear viral prodrome it is "
    "not the explanation."]],
  "diagnosis", D, 15),

Q("Chronic sinusitis", IO,
  "A 41-year-old man has had nasal congestion, facial pressure and reduced smell continuously for "
  "five months, with intermittent flares. He has had three courses of antibiotics.",
  [["Chronic rhinosinusitis, defined by symptoms beyond 12 weeks",
    "Correct. The dividing line between acute and chronic disease is twelve weeks of continuous "
    "symptoms, and five months is well beyond it. The mechanism shifts from a single infection to "
    "impaired mucociliary clearance with persistent inflammation, which is why repeated antibiotic "
    "courses treat the flares without changing the underlying problem."],
   ["Recurrent acute bacterial sinusitis",
    "Recurrent acute disease means discrete episodes with complete resolution in between. This "
    "patient has continuous symptoms with flares superimposed, which is a different pattern and "
    "implies ongoing inflammation rather than repeated new infections."],
   ["Allergic rhinitis alone",
    "Allergy causes congestion and can reduce smell, but it produces clear bilateral discharge with "
    "itch and a bluish mucosa rather than facial pressure with purulent flares, and it typically "
    "follows a seasonal or exposure pattern."],
   ["Nasopharyngeal carcinoma",
    "A nasopharyngeal tumour would be expected to give unilateral obstruction, blood-stained "
    "discharge, a neck mass or cranial nerve signs. Bilateral congestion with facial pressure over "
    "months lacks those localising features."]],
  "diagnosis", D, 25),

Q("Fungal sinusitis", IO,
  "A 63-year-old man with poorly controlled diabetes has facial pain, black necrotic tissue visible "
  "on the nasal turbinate, and rapidly progressive periorbital swelling.",
  [["Invasive fungal sinusitis, requiring urgent surgical debridement",
    "Correct. Black necrotic mucosa in an immunocompromised or diabetic patient indicates "
    "angioinvasive fungal disease, where hyphae invade blood vessels and cause tissue infarction. "
    "The blood supply is destroyed, so antifungal drugs alone cannot reach the dead tissue; surgical "
    "debridement is required alongside systemic therapy and control of the diabetes."],
   ["A fungus ball in the maxillary sinus",
    "A fungus ball is a non-invasive collection of hyphae in an immunocompetent patient, causing "
    "chronic obstruction rather than tissue necrosis. It is removed surgically but is not the "
    "fulminant angioinvasive process described here."],
   ["Allergic fungal sinusitis",
    "The allergic form produces thick eosinophilic mucin, often described as peanut butter, with "
    "polyps in an atopic patient. It is an immune response to fungus rather than invasion, and it "
    "does not cause necrosis."],
   ["Acute bacterial sinusitis with orbital extension",
    "Bacterial orbital spread is a genuine emergency and shares periorbital swelling, so it belongs "
    "on the differential. But it does not produce black necrotic turbinate tissue, which is the "
    "finding that specifically indicates fungal invasion."]],
  "diagnosis", D, 28),

Q("Epistaxis", IO,
  "A patient with a nosebleed is being instructed in first aid.",
  [["Pinch the soft part of the nose continuously for ten minutes, sitting up and leaning forward",
    "Correct. The bleeding point in 90 per cent of cases is Kiesselbach plexus on the anterior "
    "septum, which is compressed by pinching the alae rather than the bony bridge. Continuous "
    "pressure matters because releasing to check disrupts the forming clot, and leaning forward "
    "stops blood tracking backward into the pharynx where it is swallowed or aspirated."],
   ["Pinch the bony bridge of the nose and tilt the head back",
    "Pressure on the bony bridge does not reach the septal plexus, so it compresses nothing that is "
    "bleeding. Tilting back sends blood down the throat, causing nausea and vomiting and hiding how "
    "much is being lost."],
   ["Apply pressure for thirty seconds at a time, releasing to check",
    "Repeatedly releasing pressure tears the clot each time it starts to form, which is why the "
    "instruction specifies a single continuous period rather than intermittent checks."],
   ["Pack the nose immediately with gauze at home",
    "Packing is a later step performed by a clinician after simpler measures and a vasoconstrictor "
    "have failed. Improvised home packing can be pushed too far posteriorly and is difficult to "
    "remove safely."]],
  "treatment", D, 41),

Q("Nasal foreign body", IO,
  "A 3-year-old inserted a small button battery into the nose two hours ago.",
  [["Urgent removal, because a battery causes rapid liquefactive necrosis",
    "Correct. A button battery generates an electrical current across moist mucosa, producing "
    "hydroxide ions and liquefactive necrosis that can perforate the septum within hours. That makes "
    "it the one nasal foreign body treated as a true emergency, unlike inert beads or foam where the "
    "damage is obstruction and secondary infection over days."],
   ["Routine removal at the next available clinic appointment",
    "Routine timing is appropriate for an inert object, where delay costs only discomfort and a "
    "smelly discharge. Applying it to a battery allows the septum to be destroyed while the child "
    "waits."],
   ["Irrigation of the nasal cavity to flush the object out",
    "Adding moisture to a battery accelerates the electrochemical reaction that causes the injury, "
    "so irrigation makes the damage worse rather than dislodging the object safely."],
   ["Observation, since most nasal foreign bodies pass spontaneously",
    "Nasal foreign bodies do not pass spontaneously in the way ingested objects sometimes do, and "
    "the assumption is dangerous for any object, let alone one actively burning the mucosa."]],
  "next step", D, 51),

Q("Deviated septum", IO,
  "A 38-year-old man has chronic unilateral nasal obstruction, snoring, and recurrent nosebleeds "
  "from the more open side. Examination shows a markedly deviated septum.",
  [["Septoplasty",
    "Correct. A deviated septum narrows one passage and diverts airflow through the other, and that "
    "accelerated dry airflow cracks the mucosa on the open side, which is why the nosebleeds come "
    "from there rather than from the obstructed side. Only straightening the septum corrects the "
    "airflow, so surgery is the definitive treatment when symptoms justify it."],
   ["Long-term intranasal corticosteroid",
    "Topical steroid reduces mucosal swelling and can help if inflammation is contributing, but it "
    "cannot move cartilage. It also carries a risk of septal perforation with prolonged use, which "
    "is a poor trade in an already compromised septum."],
   ["Antihistamines",
    "Antihistamines address an allergic mechanism, and there is no itch, sneezing or clear bilateral "
    "discharge here. A fixed structural obstruction does not respond to them."],
   ["Nasal packing to reduce the nosebleeds",
    "Packing controls an acute bleed but does nothing about the recurrence, because the cause is the "
    "abnormal airflow pattern. Treating each bleed leaves the mechanism generating them untouched."]],
  "treatment", D, 30),

Q("Sinus anatomy", IO,
  "A patient with ethmoid sinusitis develops orbital cellulitis. A student asks why the ethmoid "
  "sinus in particular threatens the eye.",
  [["The lamina papyracea separating them is paper-thin",
    "Correct. The medial orbital wall is formed by the lamina papyracea, literally the papery layer, "
    "and it is the thinnest bone in the orbit. Infection in the ethmoid air cells has only that "
    "barrier to cross, which is why ethmoid sinusitis is the commonest sinus source of orbital "
    "cellulitis, particularly in children."],
   ["The ethmoid sinus drains directly into the orbit",
    "The ethmoid drains into the nasal cavity through the middle and superior meatus, not into the "
    "orbit. Spread happens by crossing a thin bone or through small vascular channels, not through a "
    "normal drainage route."],
   ["The maxillary sinus is closer to the orbit than the ethmoid",
    "The maxillary sinus does form the orbital floor and can be involved, but the ethmoid lies "
    "directly medial to the orbit along its whole length and is separated by far thinner bone."],
   ["The frontal sinus shares a wall with the globe",
    "The frontal sinus sits above the orbit and can cause a subperiosteal abscess of the orbital "
    "roof, but the classic and commonest route to orbital cellulitis is medial, through the "
    "ethmoid."]],
  "mechanism", D, 6),

Q("Allergic rhinitis", IO,
  "A 26-year-old man with perennial allergic rhinitis has persistent symptoms on a single "
  "antihistamine. He asks what usually happens next.",
  [["Most patients end up on more than one medicine",
    "Correct. About 80 per cent of patients with allergic rhinitis require two or more agents, "
    "because the different symptoms are driven by different mediators. A typical combination is an "
    "antihistamine with an intranasal corticosteroid, adding a leukotriene inhibitor at night, and "
    "immunotherapy if drug treatment is insufficient."],
   ["A single agent controls symptoms in most patients",
    "This underestimates the disease. Monotherapy leaves a large proportion of patients "
    "symptomatic, which is why escalation is the expected course rather than a sign of unusual "
    "severity."],
   ["Antibiotics are usually required at some point",
    "Allergy creates the environment in which infection can occur, but it is not itself an "
    "infection. Routinely expecting antibiotics medicalises an inflammatory condition and drives "
    "unnecessary prescribing."],
   ["Surgery is the usual next step after antihistamine failure",
    "Surgery has a role for structural obstruction or polyps, not for allergic inflammation itself. "
    "Medical escalation and immunotherapy come long before any operation is considered."]],
  "treatment", D, 67),

Q("Nasal polyps", IO,
  "A 45-year-old woman with asthma has nasal polyps and a history of severe bronchospasm after "
  "taking aspirin.",
  [["Aspirin-exacerbated respiratory disease",
    "Correct. The triad of asthma, nasal polyposis and aspirin sensitivity reflects abnormal "
    "arachidonic acid handling: blocking cyclo-oxygenase shunts the pathway toward leukotriene "
    "production, which drives both the bronchospasm and the polyp formation. Recognising it matters "
    "because all non-steroidal anti-inflammatories must be avoided."],
   ["Cystic fibrosis presenting in adulthood",
    "Cystic fibrosis is strongly associated with polyps in CHILDREN, and finding polyps in a child "
    "is the trigger for a sweat test. In a 45-year-old with adult-onset asthma and a clear aspirin "
    "reaction, the triad is the better explanation."],
   ["Allergic fungal sinusitis",
    "Allergic fungal disease is associated with polyps in a very high proportion of cases and "
    "belongs on the list, but it is characterised by thick eosinophilic mucin and fungal elements "
    "rather than by a specific drug reaction."],
   ["Churg-Strauss syndrome",
    "Eosinophilic granulomatosis with polyangiitis is associated with polyps and asthma in about "
    "half of cases, so it is a reasonable consideration, but it also brings systemic vasculitis "
    "features such as neuropathy that are absent here."]],
  "diagnosis", D, 63),

Q("Nasal fracture", IO,
  "A 24-year-old woman is struck in the nose. She has swelling, an obviously deviated nose, and "
  "cannot breathe through the left nostril.",
  [["Radiography is indicated, because she fails the clinical criteria",
    "Correct. Imaging can be omitted only when all four reassuring criteria are met: tenderness "
    "confined to the bony bridge, patent airflow through each nostril, a straight nose with no "
    "septal deviation, and no septal haematoma. She fails two of them, so the criteria no longer "
    "permit a clinical-only approach and the nose has to be imaged and assessed for reduction."],
   ["No imaging is needed, as nasal fractures are managed clinically",
    "That is true only for the subgroup meeting all four criteria. Applying the rule to a patient "
    "with visible deviation and unilateral obstruction misuses a decision aid designed to exclude "
    "exactly those features."],
   ["Immediate closed reduction without assessment",
    "Reduction may well be needed, but manipulating a nose before excluding a septal haematoma risks "
    "leaving a collection that will destroy the cartilage regardless of how well the bones are "
    "aligned."],
   ["Computed tomography of the facial skeleton as first line",
    "Facial computed tomography is reserved for suspected complex midface or orbital injury. Using "
    "it routinely for an isolated nasal injury delivers a much larger radiation dose than the "
    "question requires."]],
  "next step", D, 46),

Q("Epistaxis workup", IO,
  "A 55-year-old man on no medication has a single anterior nosebleed that stops with pressure. He "
  "asks whether he needs blood tests.",
  [["No clotting studies, because they are not routine for epistaxis",
    "Correct. Prothrombin time and international normalised ratio are not part of the routine "
    "workup and are reserved for patients who are anticoagulated or who have other evidence of a "
    "bleeding tendency. Ordering them reflexively generates incidental abnormalities without "
    "changing the management of a nosebleed that has already stopped."],
   ["Clotting studies for every patient with epistaxis",
    "Universal testing treats a common local mucosal problem as though it were a haematological one. "
    "The overwhelming majority of nosebleeds arise from trauma or dryness at Kiesselbach plexus in "
    "people with entirely normal clotting."],
   ["A full blood count and crossmatch",
    "Haematocrit with type and crossmatch is appropriate for massive haemorrhage, alongside two "
    "large-bore intravenous lines. A single self-limiting anterior bleed does not approach that "
    "threshold."],
   ["Platelet function testing",
    "Specialised platelet studies are for investigating a suspected inherited or acquired platelet "
    "disorder, which requires a suggestive history such as easy bruising or bleeding after surgery. "
    "None of that is present."]],
  "testing", D, 44),

Q("Septal haematoma", IO,
  "A patient with an undrained septal haematoma returns three weeks later with a depression of the "
  "nasal dorsum.",
  [["Saddle nose deformity from necrosis of the septal cartilage",
    "Correct. The septal cartilage has no blood supply of its own and depends entirely on the "
    "overlying perichondrium. A haematoma strips the perichondrium away, the cartilage undergoes "
    "avascular necrosis, and the dorsum loses its structural support and collapses. That is why "
    "drainage is urgent rather than elective."],
   ["A displaced nasal fracture that was missed",
    "An untreated displaced fracture produces deviation to one side rather than a central "
    "depression of the dorsum, and it does not develop progressively over three weeks. The timeline "
    "here matches cartilage death."],
   ["Post-traumatic swelling that will resolve",
    "Swelling elevates the dorsum rather than depressing it, and it resolves over days to a couple "
    "of weeks. A depression appearing at three weeks reflects lost structure, not residual "
    "oedema."],
   ["A septal abscess requiring drainage",
    "An untreated haematoma can indeed become infected and abscess, which would present with fever "
    "and pain rather than a painless collapse. The deformity here is the end result of the "
    "necrosis."]],
  "mechanism", D, 32),
]
