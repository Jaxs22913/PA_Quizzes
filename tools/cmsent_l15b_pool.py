# -*- coding: utf-8 -*-
"""Lecture 15, second pool -- External and Middle Ear. See _cmsent_style.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "CMS I Disorders of the External and Middle Ear"
IO = ("Disorders of the external and middle ear: etiologies, epidemiology, risk factors, clinical "
      "manifestations, differential diagnosis, diagnostic testing, management, referrals, patient "
      "education, and prognosis")

QUESTIONS = [

Q("Auricular haematoma", IO,
  "A 19-year-old wrestler is seen four hours after a match with a swollen, tense, purple left "
  "auricle. The normal folds and hollows of the ear are no longer visible. He has no hearing "
  "complaint and the canal and drum are normal.",
  [["Incision and drainage with a pressure dressing",
    "Correct. Blood collecting between the perichondrium and the cartilage strips the cartilage of "
    "its blood supply, because auricular cartilage has no vessels of its own and depends entirely on "
    "the perichondrium. Left in place the cartilage necroses and heals as the fibrotic mass called "
    "cauliflower ear, so the collection is drained early and a pressure dressing stops it "
    "reaccumulating."],
   ["Ice and observation for 48 hours",
    "Waiting allows exactly the process that causes the deformity: the longer the perichondrium is "
    "lifted off the cartilage, the more cartilage dies. Ice may help a contusion, but this is a "
    "collection that has to be evacuated rather than an area of bruising."],
   ["Oral antibiotics alone",
    "There is no infection here, only blood under pressure. Antibiotics do not evacuate a haematoma "
    "and do not restore the cartilage's blood supply, so the deformity develops on schedule while "
    "the patient takes them."],
   ["Needle aspiration without a dressing",
    "Aspiration alone often gives a temporary result because the potential space refills as soon as "
    "the needle comes out. The pressure dressing is the part that keeps perichondrium against "
    "cartilage while it reattaches, so leaving it off invites recurrence."]],
  "treatment", D, 34),

Q("Cerumen impaction", IO,
  "A 71-year-old man reports gradual reduction in hearing in the right ear over two weeks and a "
  "sensation of blockage. He uses cotton buds daily. Otoscopy shows the canal completely filled "
  "with firm wax; the drum cannot be seen. There is no pain or discharge.",
  [["A conductive loss that resolves when the wax is removed",
    "Correct. Wax occluding the canal blocks air-conducted sound before it reaches the drum, while "
    "the drum, ossicles and cochlea are all normal. That is a purely mechanical conductive loss, so "
    "Weber lateralises to the blocked ear and hearing returns to baseline as soon as the obstruction "
    "is cleared."],
   ["A sensorineural loss from age-related cochlear change",
    "Presbycusis is real in this age group but is bilateral, gradual over years, and characterised "
    "by difficulty making out words rather than a two-week sensation of blockage. It also would not "
    "be relieved by clearing the canal, and it does not fill the canal with wax."],
   ["A mixed loss requiring urgent audiology referral",
    "Nothing here suggests a cochlear component: the onset is short, unilateral, and fully explained "
    "by a visible obstruction. Referring before removing the wax means testing through the "
    "obstruction and getting a result that has to be repeated."],
   ["No measurable hearing loss, since wax does not occlude sound",
    "Wax only affects hearing once it occludes the canal, but this canal is described as completely "
    "filled. Complete occlusion typically produces a measurable conductive deficit, which is why "
    "the patient noticed it."]],
  "mechanism", D, 28),

Q("Otomycosis", IO,
  "A 44-year-old woman has had three weeks of intense itching in the right ear with only mild pain, "
  "having finished two courses of antibiotic ear drops for otitis externa. The canal contains white "
  "curd-like debris with fine black specks.",
  [["Otomycosis, treated by cleaning the canal and applying an antifungal",
    "Correct. Prolonged antibiotic drops suppress the canal's bacterial flora and let Aspergillus or "
    "Candida take over, which is why this follows treatment rather than preceding it. Itch dominating "
    "over pain and the visible fungal debris are the clues, and treatment is thorough cleaning to "
    "remove the fungal mass plus a topical antifungal."],
   ["Resistant bacterial otitis externa needing a stronger antibiotic",
    "Escalating the antibiotic treats the wrong organism and deepens the flora suppression that "
    "caused the problem. Bacterial infection is also dominated by pain rather than itch, and does "
    "not produce white curd or black spores."],
   ["Contact dermatitis from the drops, treated with topical steroid",
    "Sensitivity to a drop component is a genuine cause of an itchy canal and would be reasonable "
    "without the debris. But the visible fungal elements point to organisms, and a steroid alone "
    "would further favour their growth."],
   ["Chronic suppurative otitis media",
    "Chronic middle ear infection produces persistent discharge through a perforation and conductive "
    "loss, with the pathology behind the drum rather than lining the canal. It does not present as "
    "itch with canal debris after topical antibiotics."]],
  "diagnosis", D, 44),

Q("Otosclerosis", IO,
  "A 34-year-old woman has had gradually worsening hearing over three years, worse since her "
  "pregnancy. She says she hears conversation better in a noisy restaurant than in a quiet room. "
  "Otoscopy is normal. Her father had a similar problem.",
  [["Otosclerosis",
    "Correct. Hearing better in background noise, called paracusis, happens because a conductive "
    "loss filters out low-frequency ambient noise more than speech, and because people raise their "
    "voices in noisy rooms. Combined with a normal drum, a family history, worsening in pregnancy, "
    "and gradual conductive loss, this is the classic picture of stapes fixation."],
   ["Presbycusis",
    "Age-related loss is sensorineural, and sensorineural patients do distinctly WORSE in background "
    "noise because the damaged cochlea cannot separate speech from competing sound. It is also "
    "unusual at 34 and would not fluctuate with pregnancy."],
   ["Otitis media with effusion",
    "An effusion does cause conductive loss, but the drum would be dull with an air-fluid level "
    "rather than normal, and the course would follow an upper respiratory infection rather than "
    "running over three years with a family history."],
   ["Acoustic neuroma",
    "A vestibular schwannoma causes unilateral sensorineural loss with speech discrimination "
    "disproportionately poor, often with tinnitus and imbalance. It is unilateral rather than the "
    "bilateral progressive pattern here, and it does not improve in noise."]],
  "diagnosis", D, 65),

Q("Carcinoma of the ear canal", IO,
  "A 68-year-old man has had a discharging left ear for four months. It has not responded to three "
  "different topical antibiotics. The discharge is now blood-stained and he has developed deep "
  "aching pain. Otoscopy shows friable tissue in the canal.",
  [["Biopsy of the canal lesion",
    "Correct. Otitis externa that will not respond to appropriate treatment, together with bloody "
    "otorrhoea and friable tissue, is the described presentation of canal carcinoma. Only "
    "histology distinguishes malignancy from chronic inflammation or granulation, and the treatment "
    "pathway is entirely different, so tissue has to be obtained rather than another drop tried."],
   ["A fourth course of topical antibiotics with a different agent",
    "Three failures already establish that this is not responding to antimicrobial therapy, which "
    "is precisely the signal to reconsider the diagnosis. Another course delays a cancer diagnosis "
    "while the tumour continues to grow."],
   ["Aural toilet and observation for six weeks",
    "Cleaning the canal is a sensible adjunct but is not a diagnosis, and six more weeks of watching "
    "friable bleeding tissue in an elderly patient is the wrong direction when malignancy is already "
    "on the list."],
   ["Systemic antifungal therapy",
    "Fungal disease follows antibiotic drops and produces itch with visible spores or hyphae, not "
    "bloody discharge from friable tissue with deep pain. Treating for fungus leaves the mass "
    "unexamined."]],
  "next step", D, 71),

Q("Chronic otitis media", IO,
  "A 26-year-old man has had intermittent painless discharge from the right ear for two years, with "
  "reduced hearing on that side. Otoscopy shows a central perforation with a moist middle ear "
  "mucosa. There is no keratin debris and no retraction pocket.",
  [["Chronic suppurative otitis media",
    "Correct. A perforation that has failed to heal, with recurrent painless discharge and "
    "conductive hearing loss over years, defines chronic suppurative otitis media. The absence of "
    "pain distinguishes it from an acute infection, and the absence of keratin debris or a retraction "
    "pocket is what separates it from cholesteatoma."],
   ["Cholesteatoma",
    "Cholesteatoma also gives chronic painless otorrhoea and conductive loss, so it is the right "
    "thing to consider, but it requires the keratin sac or the retraction pocket that this "
    "examination explicitly does not show. The distinction matters because cholesteatoma erodes bone "
    "and needs surgery."],
   ["Acute otitis media",
    "Acute disease presents over days with pain, fever and a bulging intact drum, not with two years "
    "of painless discharge through an established perforation. The tempo alone rules it out."],
   ["Otitis externa",
    "Canal infection causes pain on moving the tragus with canal oedema and no perforation. Here the "
    "pathology is behind a perforated drum in the middle ear, and the canal findings that define "
    "external otitis are absent."]],
  "diagnosis", D, 31),

Q("Barotrauma", IO,
  "A 41-year-old man descends on a flight with a heavy cold. He develops severe right ear pain "
  "during descent, followed by muffled hearing. Otoscopy shows a dark blue-black discolouration "
  "behind an intact tympanic membrane.",
  [["Haemotympanum from middle ear barotrauma",
    "Correct. A blocked eustachian tube cannot equalise the rising ambient pressure during descent, "
    "so relative negative pressure in the middle ear pulls fluid and then blood out of the mucosal "
    "vessels. The blood behind an intact drum gives the blue-black appearance, and the conductive "
    "loss follows from fluid rather than from any damage to the cochlea."],
   ["Acute otitis media",
    "Infection would give a bulging erythematous drum with fever over days, not an immediate "
    "pressure-related event during a single descent. The colour described is blood rather than the "
    "opacity of pus."],
   ["Glomus tumour",
    "A glomus tumour is a vascular middle ear mass giving pulsatile tinnitus and a red mass behind "
    "the drum that develops over months. It is not precipitated by a flight and does not appear "
    "acutely during descent."],
   ["Cholesteatoma",
    "Cholesteatoma builds slowly behind a retracted drum and appears as white keratin, not as an "
    "acute blue-black collection. The timing here is minutes, which no chronic process explains."]],
  "diagnosis", D, 37),

Q("Ear foreign body", IO,
  "A 5-year-old girl has had a foul-smelling discharge from the left ear for a week. She has been "
  "afebrile with no ear pain. Otoscopy after suctioning reveals a small piece of foam rubber "
  "impacted against the drum.",
  [["Retained foreign body causing secondary infection",
    "Correct. An organic or porous object retained in the canal obstructs drainage and acts as a "
    "nidus, so the canal skin becomes secondarily infected and produces the foul discharge. The "
    "absence of pain and fever, with a unilateral offensive discharge in a young child, is the "
    "pattern that should prompt a careful search for something in the canal."],
   ["Chronic suppurative otitis media",
    "Chronic middle ear infection discharges through a perforation and would show the perforation "
    "rather than an object lodged against an intact drum. It also typically runs over months to "
    "years rather than a week."],
   ["Malignant otitis externa",
    "That is a skull base osteomyelitis of elderly diabetic or immunocompromised patients, with "
    "severe pain and granulation tissue. A well, afebrile, painless 5-year-old does not fit any part "
    "of that description."],
   ["Otomycosis",
    "Fungal canal infection produces itch with visible spores or curd-like debris, usually after "
    "antibiotic drops. It does not explain an impacted piece of foam or the offensive unilateral "
    "discharge."]],
  "diagnosis", D, 47),

Q("Acute otitis media", IO,
  "A 2-year-old boy has had four episodes of acute otitis media in the past six months, each "
  "treated with antibiotics. Between episodes his parents report he does not respond when called "
  "from another room. Tympanometry today shows a flat trace bilaterally.",
  [["Referral for consideration of tympanostomy tubes",
    "Correct. Recurrent acute infections plus a persistent bilateral effusion, shown by the flat "
    "tympanograms, together with functional hearing concern in a child at the age of language "
    "acquisition, is the combination that justifies tubes. The tubes ventilate the middle ear, "
    "restore hearing and reduce the recurrence rate rather than treating each episode after it "
    "starts."],
   ["Long-term prophylactic antibiotics",
    "Continuous antibiotics have fallen out of favour because the benefit is small and the cost in "
    "resistance and side effects is real. They also do nothing for the effusion that is currently "
    "impairing his hearing, which is the more pressing problem."],
   ["Reassurance, since most children outgrow ear infections",
    "Most children do, and that is the right advice for isolated episodes. It is the wrong advice "
    "when there is documented bilateral effusion and a hearing concern at two years old, because "
    "the window in which hearing supports speech development is not indefinite."],
   ["Oral corticosteroids to clear the effusion",
    "Steroids have not been shown to produce lasting resolution of middle ear effusion, and "
    "systemic steroid exposure in a toddler for a self-limiting mechanical problem is a poor "
    "trade."]],
  "next step", D, 30),

Q("Malignant otitis externa", IO,
  "A 74-year-old woman with type 2 diabetes has severe left ear pain and discharge that has not "
  "responded to topical treatment. She now has a left-sided facial droop involving the forehead. "
  "Inflammatory markers are raised.",
  [["The infection has spread to the skull base and involved the facial nerve",
    "Correct. Necrotising otitis externa spreads from the canal into the temporal bone as an "
    "osteomyelitis, usually Pseudomonas in a diabetic or immunocompromised host. The facial nerve "
    "runs through that bone, so a lower motor neuron palsy involving the forehead signals the "
    "infection has reached it, which marks advanced disease and a worse prognosis."],
   ["A concurrent Bell palsy unrelated to the ear infection",
    "Attributing a facial palsy to an idiopathic cause in a diabetic patient with an active "
    "unresolving ear infection ignores the far likelier explanation sitting in the same temporal "
    "bone. Bell palsy is a diagnosis of exclusion, and here there is an obvious cause to exclude "
    "first."],
   ["A stroke affecting the facial motor cortex",
    "A central lesion spares the forehead, because the upper face receives input from both "
    "hemispheres. Forehead involvement localises the lesion to the nerve itself rather than the "
    "brain, which points back to the temporal bone."],
   ["Ramsay Hunt syndrome from herpes zoster",
    "Zoster of the geniculate ganglion does cause a facial palsy with ear pain, so it belongs on the "
    "list, but it produces vesicles in the canal or concha and does not present as weeks of "
    "treatment-resistant discharge with raised inflammatory markers in a diabetic."]],
  "mechanism", D, 43),

Q("Tympanic membrane perforation", IO,
  "A 33-year-old woman had severe right ear pain for two days with fever. This morning the pain "
  "stopped abruptly and she noticed discharge on her pillow. Otoscopy shows purulent material in "
  "the canal and a small perforation in the tympanic membrane.",
  [["The drum has perforated, releasing the pressure of the middle ear pus",
    "Correct. In acute otitis media the pain comes from pus under pressure stretching the drum. Once "
    "the drum ruptures the pressure is relieved and the pain stops abruptly, which is why sudden "
    "relief accompanied by discharge is the classic history. The perforation is a consequence of the "
    "infection, not a separate injury."],
   ["The infection has resolved spontaneously",
    "Resolution does not produce purulent discharge and a hole in the drum. The pain stopping is a "
    "mechanical event rather than a sign that the organisms have gone, and the middle ear infection "
    "still needs treating."],
   ["A cholesteatoma has eroded through the drum",
    "Cholesteatoma produces chronic painless discharge developing over months to years, with keratin "
    "debris. It does not explain two days of fever and severe pain ending in sudden rupture."],
   ["She has developed otitis externa on top of the middle ear infection",
    "Canal infection would give pain on moving the tragus and canal oedema, and it would not relieve "
    "the deep pain of a middle ear under pressure. The discharge here is coming through the "
    "perforation from behind the drum."]],
  "mechanism", D, 61),

Q("Otitis externa", IO,
  "A 55-year-old man has had otitis externa treated with drops for five days. The canal is so "
  "oedematous that the drops appear not to be reaching beyond the outer third, and his pain is "
  "unchanged.",
  [["Place an ear wick to carry the drops along the swollen canal",
    "Correct. Topical therapy only works where the drug physically reaches, and a canal swollen shut "
    "stops the drops at its outer end. A wick is an absorbent strip that draws medication along the "
    "length of the canal by capillary action, restoring delivery to the inflamed skin without "
    "changing the drug."],
   ["Switch to oral antibiotics",
    "Systemic therapy reaches canal skin poorly, which is why topical treatment is first line for "
    "otitis externa in the first place. Oral antibiotics are reserved for spread beyond the canal or "
    "for immunocompromised patients, not for a delivery problem that has a mechanical solution."],
   ["Stop the drops and observe",
    "Withdrawing the only active treatment because it has not yet worked leaves an infected, "
    "occluded canal to progress. The problem here is that the drug is not arriving, not that it is "
    "the wrong drug."],
   ["Irrigate the canal to reduce the swelling",
    "Irrigation does not reduce oedema and risks driving infected material deeper or into the middle "
    "ear if the drum is not clearly intact. It is also poorly tolerated in an ear that is already "
    "acutely painful."]],
  "next step", D, 41),
]
