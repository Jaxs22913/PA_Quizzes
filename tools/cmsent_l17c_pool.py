# -*- coding: utf-8 -*-
"""Lecture 17, third pool -- Nose and Paranasal Sinuses."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "hughie Nose & Paranasal Sinuses"
IO = ("Disorders of the nose and paranasal sinuses: etiologies, epidemiology, risk factors, "
      "clinical manifestations, differential diagnosis, diagnostic testing, management, referrals, "
      "patient education, and prognosis")

QUESTIONS = [

Q("Acute sinusitis", IO,
  "A 29-year-old woman with sinusitis asks why her face hurts more when she leans forward to tie "
  "her shoes.",
  [["Bending increases the hydrostatic pressure of the fluid within the sinus",
    "Correct. An obstructed sinus fills with fluid under pressure, and tilting the head forward "
    "raises the column of fluid pressing against the inflamed mucosa and its sensory nerve endings. "
    "That is why postural worsening is such a characteristic feature of sinusitis and helps separate "
    "it from other causes of facial pain."],
   ["Bending compresses the nasal turbinates against the septum",
    "Turbinate contact can cause facial pain in some patients, but it is not posture-dependent in "
    "this way and does not explain the relationship to a sinus filled with fluid."],
   ["Bending reduces venous drainage from the head",
    "Venous congestion on bending forward contributes to a general sense of pressure, but the "
    "localised sinus pain of this condition tracks the fluid within the obstructed cavity rather "
    "than generalised venous return."],
   ["Bending triggers a trigeminal neuralgia",
    "Trigeminal neuralgia produces brief lancinating shocks triggered by touch or chewing, not a "
    "sustained pressure pain that varies with head position, and it is not associated with purulent "
    "discharge."]],
  "mechanism", D, 12),

Q("Bacterial sinusitis", IO,
  "A clinician lists the features that shift an acute rhinosinusitis toward a bacterial cause.",
  [["Symptoms for ten days or more, double worsening, or unilateral facial or tooth pain",
    "Correct. These are the named criteria, and each captures something a virus does not usually do: "
    "viral illness improves within about ten days, follows a single curve rather than relapsing, and "
    "produces bilateral symptoms rather than pain localised to one sinus or the upper teeth beneath "
    "it."],
   ["Purulent green or yellow discharge",
    "Discharge colour is the commonest reason antibiotics get prescribed and is the least useful "
    "sign. Colour comes from neutrophil myeloperoxidase and appears in ordinary viral infection as "
    "the illness evolves."],
   ["Fever at any point during the illness",
    "Fever is common early in viral rhinosinusitis and is not by itself discriminating. It carries "
    "weight when it appears as part of a second deterioration rather than at onset."],
   ["Facial pressure and nasal congestion",
    "Those are the defining symptoms of rhinosinusitis of any cause, so they establish the diagnosis "
    "rather than its aetiology. Every patient with the condition has them."]],
  "finding", D, 15),

Q("Chronic sinusitis", IO,
  "A 47-year-old man with chronic rhinosinusitis is told the underlying problem is impaired "
  "mucociliary clearance. He asks what that means.",
  [["The cilia can no longer move the mucus blanket out of the sinus",
    "Correct. Sinus mucosa is lined with ciliated epithelium that sweeps a mucus layer toward the "
    "ostium in a fixed direction. Chronic inflammation damages the cilia and thickens the mucus, so "
    "secretions stagnate in the sinus, which perpetuates inflammation and invites repeated "
    "infection. That is why chronic disease behaves differently from a single acute infection."],
   ["The sinus ostium has been surgically closed",
    "Ostial obstruction is part of the mechanism, but it is caused by mucosal swelling and polyps "
    "rather than by surgery, and surgery for chronic sinusitis aims to WIDEN the drainage pathway."],
   ["The immune system no longer produces antibodies to sinus organisms",
    "Immunodeficiency is worth considering in unusually severe or recurrent disease, but it is not "
    "what the phrase describes, and most patients with chronic sinusitis have normal immunity."],
   ["The mucus has become too thin to trap organisms",
    "The problem is the opposite: mucus becomes thicker and harder to move. Thin mucus clears "
    "easily, which is why saline irrigation and hydration help."]],
  "mechanism", D, 25),

Q("Epistaxis", IO,
  "A 66-year-old man has heavy bleeding from both nostrils with blood running down the back of his "
  "throat. Anterior rhinoscopy shows no visible bleeding point.",
  [["A posterior bleed from the sphenopalatine artery",
    "Correct. Bleeding visible from both nostrils and running posteriorly, with no anterior source "
    "seen, indicates the sphenopalatine artery high and posteriorly in the nasal cavity. These "
    "bleeds are heavier and carry a specific additional danger, which is aspiration of blood into "
    "the airway and subsequent infection."],
   ["An anterior bleed from Kiesselbach plexus",
    "Anterior bleeds account for 90 per cent of cases, so this is the base rate, but they arise from "
    "a visible spot on the anterior septum and usually bleed from one nostril. Failure to see any "
    "source anteriorly argues against it."],
   ["Bleeding from a nasal polyp",
    "Polyps are avascular grey glistening masses that cause obstruction and anosmia rather than "
    "haemorrhage. They are not a recognised source of brisk arterial bleeding."],
   ["A ruptured septal haematoma",
    "A septal haematoma is a collection between cartilage and perichondrium after trauma, presenting "
    "as a boggy septal swelling. It does not produce brisk bleeding from both nostrils and there is "
    "no trauma described."]],
  "diagnosis", D, 39),

Q("Nasal foreign body", IO,
  "A 3-year-old has a bead in the left nostril. The child is calm and the object is visible "
  "anteriorly.",
  [["Have the parent perform a positive pressure blow while occluding the other nostril",
    "Correct. The parent seals the child's mouth with their own and blows while the unaffected "
    "nostril is occluded, so the pressure travels through the posterior choana and pushes the object "
    "forward. It is atraumatic, needs no instruments, and avoids the risk of pushing the bead deeper "
    "that instrumentation carries in a small child."],
   ["Irrigate the nostril with saline under pressure",
    "Irrigation risks pushing the object posteriorly toward the nasopharynx, where it can be "
    "aspirated. It is also poorly tolerated and offers no directional control."],
   ["Grasp the bead with forceps",
    "Forceps slide off a smooth round object and transmit the force inward, advancing it. That is "
    "the same problem as in the ear canal, and it converts an easy removal into a difficult one."],
   ["Refer immediately for removal under general anaesthesia",
    "General anaesthesia is reserved for a failed attempt, an uncooperative child or a posteriorly "
    "impacted object. Committing a calm child with an anteriorly visible object straight to theatre "
    "skips a simple manoeuvre."]],
  "treatment", D, 51),

Q("Perforated septum", IO,
  "A 44-year-old woman has a septal perforation. She uses no intranasal medication and denies drug "
  "use. The clinician considers systemic causes.",
  [["Granulomatosis with polyangiitis, or secondary syphilis",
    "Correct. When the two common local causes, intranasal corticosteroid and cocaine, are excluded, "
    "granulomatosis with polyangiitis and secondary syphilis as the rarer systemic "
    "causes. Both destroy the septal mucosa and cartilage through inflammation rather than local "
    "ischaemia, and both need systemic treatment."],
   ["Allergic rhinitis",
    "Allergic inflammation swells the mucosa and causes clear discharge but does not destroy "
    "cartilage. It is a risk factor mainly because it leads to prolonged topical steroid use, which "
    "is a local cause."],
   ["Chronic sinusitis",
    "Chronic sinus inflammation affects the sinus mucosa and drainage pathways rather than the "
    "septal cartilage, and it is not among the causes of perforation."],
   ["Nasal polyposis",
    "Polyps are soft oedematous mucosal masses obstructing the airway. They occupy space rather than "
    "eroding structures and do not perforate the septum."]],
  "cause", D, 29),

Q("Sinusitis complications", IO,
  "A 26-year-old man with sinusitis develops altered mental status and a severe headache.",
  [["Urgent evaluation for intracranial extension",
    "Correct. Altered mental status is one of the urgent features alongside "
    "diplopia and periorbital swelling, and it indicates the infection may have crossed into the "
    "cranial cavity, producing meningitis, an epidural or subdural collection, or a brain abscess. "
    "That requires imaging and admission rather than outpatient management."],
   ["A migraine triggered by sinus congestion",
    "Sinus symptoms and migraine do overlap and are commonly confused, but migraine does not alter "
    "mental status. Attributing confusion to headache type risks missing an intracranial "
    "infection."],
   ["Dehydration from reduced oral intake",
    "Dehydration can cause confusion in the elderly or in severe illness, and rehydration is "
    "sensible, but it does not explain a severe headache in a young man with an adjacent infection "
    "and would not be assumed before imaging."],
   ["A side effect of oral decongestants",
    "Decongestants can cause insomnia, palpitations and hypertension, and rarely agitation, but "
    "attributing new confusion with severe headache to a common over-the-counter drug leaves a "
    "dangerous complication unexamined."]],
  "next step", D, 20),

Q("Allergic rhinitis", IO,
  "A 31-year-old woman with allergic rhinitis is prescribed an intranasal corticosteroid. She asks "
  "how to use it so that it works and does not damage her nose.",
  [["Aim the spray laterally, away from the septum",
    "Correct. Directing the spray at the septum delivers the drug repeatedly to the thin mucosa over "
    "the cartilage, and chronic vasoconstriction there is one of the named causes of septal "
    "perforation. Aiming laterally toward the turbinate treats the tissue that is actually swollen "
    "and keeps the drug off the septum."],
   ["Aim the spray at the septum for even distribution",
    "This is the intuitive technique and the harmful one. It concentrates the drug on the one part "
    "of the nose that is least able to tolerate it and most likely to perforate."],
   ["Sniff hard immediately after spraying",
    "Sniffing hard draws the drug straight back into the nasopharynx to be swallowed, so it never "
    "acts on the nasal mucosa. Gentle breathing keeps it where it is needed."],
   ["Use it only on days when symptoms are severe",
    "Intranasal steroids work by suppressing ongoing inflammation and take days to reach full "
    "effect, so intermittent use on bad days gives much less benefit than regular use through the "
    "season."]],
  "treatment", D, 67),

Q("Nasal polyps", IO,
  "A 52-year-old man with nasal polyps had endoscopic sinus surgery two years ago and his symptoms "
  "have returned.",
  [["Recurrence is expected, because surgery gives only temporary relief",
    "Correct. Polyps arise from ongoing mucosal inflammation, and removing them does not remove the "
    "process that produced them. Surgery provides only temporary "
    "relief, which is why medical treatment of the underlying inflammation continues afterwards and "
    "why patients should be told to expect this."],
   ["The original surgery must have been incomplete",
    "Incomplete surgery does cause early recurrence, but assuming technical failure misrepresents "
    "the natural history: polyps recur even after complete removal because the driving inflammation "
    "persists."],
   ["He has developed a new diagnosis such as malignancy",
    "A unilateral mass or bleeding would warrant that concern, but recurrent bilateral polyps two "
    "years after surgery is the expected course rather than a signal of something new."],
   ["Polyps do not recur, so this must be scar tissue",
    "Recurrence is the rule rather than the exception. Attributing symptoms to scarring would divert "
    "attention from the medical treatment that actually slows the process."]],
  "treatment", D, 63),

Q("Nasal trauma", IO,
  "A 30-year-old man is assaulted and has clear fluid dripping from one nostril. He also has "
  "periorbital bruising on both sides.",
  [["Suspect a cerebrospinal fluid leak from a skull base fracture",
    "Correct. Clear rhinorrhoea after significant facial or head trauma, particularly with bilateral "
    "periorbital bruising, raises the possibility that the cribriform plate has fractured and "
    "cerebrospinal fluid is draining through the nose. That converts a nasal injury into a "
    "neurosurgical problem and carries a risk of meningitis."],
   ["Allergic rhinitis unmasked by the injury",
    "Allergic rhinorrhoea is bilateral, accompanied by sneezing and itch, and is not precipitated by "
    "a single traumatic event. Unilateral clear fluid after trauma has a specific and dangerous "
    "explanation."],
   ["Normal nasal secretions from mucosal irritation",
    "Traumatised mucosa does produce secretions, which is why the distinction matters and why the "
    "fluid is tested. Assuming it is normal mucus in the presence of bilateral periorbital bruising "
    "risks missing a basal skull fracture."],
   ["A septal haematoma draining spontaneously",
    "A haematoma contains blood, so any spontaneous drainage would be bloody rather than clear, and "
    "a haematoma presents as a boggy septal swelling that requires drainage rather than leaking on "
    "its own."]],
  "diagnosis", D, 46),

Q("Nasopharyngeal carcinoma", IO,
  "A clinician is asked which virus is most strongly associated with nasopharyngeal carcinoma.",
  [["Epstein-Barr virus",
    "Correct. Epstein-Barr virus is the principal viral association, alongside human papillomavirus "
    "and smoking as risk factors, and the disease is endemic in southern China with males affected "
    "two to three times as often as females. The association matters because viral serology and "
    "in situ testing contribute to diagnosis and surveillance."],
   ["Human papillomavirus type 16",
    "Human papillomavirus is listed as a risk factor and dominates OROPHARYNGEAL cancer, where 60 to "
    "80 per cent of cases are virus-related. For the nasopharynx specifically, Epstein-Barr virus is "
    "the stronger association."],
   ["Cytomegalovirus",
    "Cytomegalovirus causes a mononucleosis-like illness and disease in the immunocompromised, but "
    "it is not among the recognised aetiological agents for nasopharyngeal carcinoma."],
   ["Herpes simplex virus type 1",
    "Herpes simplex causes oral and perioral ulceration through latency in the trigeminal ganglion. "
    "It has no established role in nasopharyngeal malignancy."]],
  "cause", D, 70),

Q("Sinusitis in the immunocompromised", IO,
  "A 58-year-old woman on chemotherapy has facial pain and fever with sinus opacification. Her "
  "clinician notes that the usual approach may need to change.",
  [["She needs earlier imaging and a lower threshold for invasive fungal disease",
    "Correct. Immunosuppression removes the neutrophil response that normally contains fungal hyphae, "
    "so Aspergillus and the mucormycetes can invade blood vessels and cause tissue infarction within "
    "days. That is why the usual watchful approach to sinusitis is abandoned and why the nasal "
    "mucosa is inspected specifically for necrotic tissue."],
   ["She can be managed identically to an immunocompetent patient",
    "The standard approach relies on most sinusitis being viral and self-limiting, which depends on "
    "an intact immune response. That assumption does not hold here, and applying it delays "
    "recognition of a rapidly fatal infection."],
   ["Antibiotics should be withheld until cultures return",
    "Waiting for cultures in a febrile neutropenic or immunosuppressed patient is unsafe, because "
    "the window in which treatment works is short. Empirical therapy starts while cultures are "
    "processed."],
   ["Topical decongestants alone are sufficient",
    "Decongestants relieve obstruction but do not treat infection at all. In a patient who cannot "
    "contain an infection herself, symptomatic treatment alone allows it to progress."]],
  "next step", D, 28),
]
