# -*- coding: utf-8 -*-
# PDM I Lecture 3 -- pool E. Head and neck imaging, and applying test selection.
# Syllabus objectives h, i, j, k and l.
#
# SLIDE 38 HAS NO PICTURE IN THE STUDENT VERSION, but its speaker notes describe
# the missing figure in full -- both panels, every arrow. The blow-out and tripod
# fracture findings are quizzed from that description and cited to the notes, so
# it is obvious where they came from if the figure is ever restored.
#
# SLIDE 37 IS A THREE-COLUMN LAYOUT and the third column (Neck CT) extracts
# AFTER the slide footer, out of order. Read as running text it looks like the
# orbital list continues into abscess and necrotic nodes. It does not; those are
# neck findings. Questions here keep the three columns separate.
SRC = "3. svDerm, ENT, Ophtho.pptx"
def c(n): return f"{SRC}, Slide {n}"
def cn(n): return f"{SRC}, Slide {n} (speaker notes)"

IOH = "h — Compare and contrast CT and MRI applications in head and neck pathology"
IOI = "i — Select appropriate imaging studies for common ophthalmologic and ENT disorders"
IOJ = "j — Identify common abnormalities of the orbit, sinuses, and neck on diagnostic imaging"
IOK = "k — Discuss imaging evaluation of neck masses and deep neck infections"
IOL = "l — Apply diagnostic test selection principles to common dermatologic, ophthalmologic, and otolaryngologic presentations"

POOL_E = [
 dict(topic="CT versus MRI", io=IOH, slot="first-line",
   q="Which modality is first-line for most acute head and neck infections?",
   opts=[
     ["Contrast-enhanced computed tomography",
      "Correct — fast, widely available, and it shows abscess, oedema, gas and bone erosion."],
     ["Contrast-enhanced magnetic resonance imaging",
      "Magnetic resonance is reserved for soft tissue, nerves and intracranial extension."],
     ["Ultrasound of the affected region",
      "Ultrasound is first-line for a neck MASS, not for acute head and neck infection."],
     ["Plain radiography of the facial bones",
      "Plain films are not offered as first-line here."]],
   c=0, cite=c(35)),

 dict(topic="CT versus MRI", io=IOH, slot="test finding",
   q="What does contrast-enhanced computed tomography show in head and neck infection?",
   opts=[
     ["Abscesses, oedema, gas and bone erosion",
      "Correct — the four findings listed as its advantage."],
     ["Perineural spread, skull base involvement and tumour extent",
      "Those are magnetic resonance strengths."],
     ["Cystic versus solid character and vascularity of a mass",
      "Those are ultrasound's contributions to a neck mass."],
     ["Middle-ear pressure and tympanic membrane mobility",
      "Those are tympanometry findings, not imaging ones."]],
   c=0, cite=c(35)),

 dict(topic="CT versus MRI", io=IOH, slot="first-line",
   q="Which five strengths does the deck give computed tomography?",
   opts=[
     ["Calcifications and bone, sinuses, acute trauma and orbital fractures, foreign bodies, and unstable or claustrophobic patients",
      "Correct — all five as listed."],
     ["Soft-tissue contrast, no ionizing radiation, orbital extension, perineural spread, and tumours",
      "Those are the five magnetic resonance strengths."],
     ["Calcifications, sinuses, perineural spread, foreign bodies, and skull base disease",
      "Perineural spread and skull base disease belong to magnetic resonance."],
     ["Bone, tumours, foreign bodies, vascular thrombosis, and osteomyelitis",
      "The last three are given elsewhere as magnetic resonance contributions."]],
   c=0, cite=c(35)),

 dict(topic="CT versus MRI", io=IOH, slot="first-line",
   q="Which five strengths does the deck give magnetic resonance imaging?",
   opts=[
     ["Superior soft-tissue contrast, no ionizing radiation, intracranial or orbital extension, perineural spread, skull base and tumours",
      "Correct — the magnetic resonance list as given."],
     ["Speed, wide availability, bone detail, foreign bodies and acute trauma",
      "Those are the computed tomography strengths."],
     ["Soft-tissue contrast, speed, bone erosion, gas and oedema",
      "Speed, bone erosion and gas are computed tomography advantages."],
     ["No ionizing radiation, cystic versus solid character, vascularity and size",
      "The last three are what ultrasound contributes to a neck mass."]],
   c=0, cite=c(35)),

 dict(topic="CT versus MRI", io=IOH, slot="first-line",
   q="What are the deck's two clinical pearls contrasting the modalities?",
   opts=[
     ["Think computed tomography for bone, trauma and speed; think magnetic resonance for soft tissue, nerves and tumour or intracranial extension",
      "Correct — both pearls as the slide words them."],
     ["Think computed tomography for soft tissue and nerves; think magnetic resonance for bone and speed",
      "The two pearls are swapped."],
     ["Think computed tomography for tumours; think magnetic resonance for foreign bodies",
      "Tumours go to magnetic resonance and foreign bodies to computed tomography."],
     ["Think computed tomography when contrast is contraindicated; think magnetic resonance when it is not",
      "Contrast status is not what the pearls turn on."]],
   c=0, cite=c(35)),

 dict(topic="CT versus MRI", io=IOH, slot="first-line",
   q="For which patients does the deck specifically favour computed tomography?",
   opts=[
     ["Unstable or claustrophobic patients",
      "Correct — both are named as reasons to choose computed tomography."],
     ["Pregnant patients and children",
      "The deck does not name these here, and both are reasons to limit radiation."],
     ["Patients with implanted metal hardware",
      "Not one of the reasons given on this slide."],
     ["Patients with impaired kidney function",
      "Renal function is a contrast issue rather than a modality one here."]],
   c=0, cite=c(35)),

 dict(topic="Imaging selection", io=IOI, slot="avoid",
   q="Which three presentations need no imaging at all?",
   opts=[
     ["Uncomplicated acute rhinosinusitis, otitis, and simple soft-tissue infections",
      "Correct — the deck's no-imaging list."],
     ["Uncomplicated acute rhinosinusitis, orbital cellulitis, and simple soft-tissue infections",
      "Orbital cellulitis is an emergency imaging indication."],
     ["Otitis, neck mass, and simple soft-tissue infections",
      "A neck mass is worked up beginning with ultrasound."],
     ["Uncomplicated otitis, deep neck infection, and simple abscesses",
      "Deep neck infection requires contrast computed tomography of the neck."]],
   c=0, cite=c(36)),

 dict(topic="Imaging selection", io=IOI, slot="escalation",
   q="Which findings make sinus or orbital imaging an emergency?",
   opts=[
     ["Facial swelling, proptosis, eye signs or neurologic signs",
      "Correct — the four findings the deck flags as emergency imaging."],
     ["Fever, purulent discharge, facial pain and headache",
      "These are ordinary sinusitis features and do not trigger emergency imaging."],
     ["Nasal obstruction, anosmia and postnasal drip",
      "None of these is on the emergency list."],
     ["Hearing loss, tinnitus and vertigo",
      "Those relate to the ear rather than the sinuses or orbit."]],
   c=0, cite=c(36)),

 dict(topic="Imaging selection", io=IOI, slot="escalation",
   q="Which study is indicated for complicated sinusitis or orbital cellulitis?",
   opts=[
     ["Contrast computed tomography of the sinuses and orbits",
      "Correct — the study named for this indication."],
     ["Contrast computed tomography of the neck",
      "That is for deep neck infection."],
     ["Magnetic resonance imaging with contrast",
      "Magnetic resonance with contrast is named for acoustic neuroma and asymmetric sensorineural loss."],
     ["Ultrasound of the orbit",
      "Ultrasound is offered for a neck mass, not for orbital cellulitis."]],
   c=0, cite=c(36)),

 dict(topic="Imaging selection", io=IOI, slot="first-line",
   q="Which study does the deck name for deep neck infection, and what does it say about ultrasound there?",
   opts=[
     ["Contrast computed tomography of the neck, and it states that ultrasound is not helpful",
      "Correct — the deck rules ultrasound out explicitly for this indication."],
     ["Ultrasound of the neck first, escalating to computed tomography if inconclusive",
      "That sequence applies to a neck MASS, not to deep neck infection."],
     ["Magnetic resonance imaging of the neck, with ultrasound as a screening step",
      "Magnetic resonance adds value for specific complications, not as first-line."],
     ["Plain radiography of the soft tissues of the neck, with ultrasound if negative",
      "Plain films are not offered for this."]],
   c=0, cite=c(36)),

 dict(topic="Imaging selection", io=IOI, slot="first-line",
   q="What is first-line for a neck mass, and what question does it answer?",
   opts=[
     ["Ultrasound, distinguishing superficial or cystic from solid",
      "Correct — the deck names lymphadenopathy and thyroid as the examples."],
     ["Contrast computed tomography, distinguishing abscess from phlegmon",
      "That is the deep neck infection pathway."],
     ["Magnetic resonance imaging, distinguishing benign from malignant",
      "Magnetic resonance follows ultrasound for specific reasons."],
     ["Fine needle aspiration, distinguishing reactive from neoplastic",
      "The deck's imaging pathway begins with ultrasound."]],
   c=0, cite=c(36)),

 dict(topic="Imaging selection", io=IOI, slot="escalation",
   q="When are computed tomography and magnetic resonance used after ultrasound of a neck mass?",
   opts=[
     ["For staging of deep or malignant lesions",
      "Correct — the escalation the deck gives."],
     ["For any mass larger than two centimetres",
      "No size threshold is given."],
     ["For any mass that is cystic on ultrasound",
      "Cystic character is what ultrasound establishes, not a trigger for cross-sectional imaging."],
     ["For any mass in a patient over fifty",
      "No age criterion is given."]],
   c=0, cite=c(36)),

 dict(topic="Imaging selection", io=IOI, slot="first-line",
   q="Which study is indicated for suspected acoustic neuroma or asymmetric sensorineural hearing loss?",
   opts=[
     ["Magnetic resonance imaging with contrast",
      "Correct — the study the deck names for this indication."],
     ["Contrast computed tomography of the temporal bones",
      "Computed tomography is for bone, trauma and speed rather than this."],
     ["Contrast computed tomography of the neck",
      "That is for deep neck infection."],
     ["Ultrasound of the mastoid region",
      "Not an indication the deck gives for ultrasound."]],
   c=0, cite=c(36)),

 dict(topic="Sinus imaging", io=IOJ, slot="test finding",
   q="Which three computed tomography findings indicate sinus infection?",
   opts=[
     ["Mucosal thickening, air-fluid levels and sinus opacification",
      "Correct — the three sinus findings listed."],
     ["Fat stranding, abscess and herniated orbital contents",
      "Those are the orbital findings."],
     ["Rim-enhancing fluid collection and enlarged or necrotic lymph nodes",
      "Those are the neck findings."],
     ["Bone erosion, gas within soft tissue and perineural spread",
      "Not the three the sinus column lists."]],
   c=0, cite=c(37)),

 dict(topic="Orbital imaging", io=IOJ, slot="test finding",
   q="Which findings does orbital computed tomography show?",
   opts=[
     ["Orbital cellulitis with fat stranding, abscess, blowout fracture and herniated orbital contents",
      "Correct — the orbital column as listed."],
     ["Mucosal thickening, air-fluid levels and sinus opacification",
      "Those are the sinus findings."],
     ["Rim-enhancing fluid collection and necrotic lymph nodes",
      "Those are the neck findings."],
     ["Cystic versus solid character, size and vascularity",
      "Those are ultrasound descriptors for a neck mass."]],
   c=0, cite=c(37)),

 dict(topic="Neck imaging", io=IOJ, slot="test finding",
   q="Which findings does neck computed tomography show?",
   opts=[
     ["Abscess as a rim-enhancing fluid collection, and enlarged or necrotic lymph nodes",
      "Correct — the neck column, which extracts out of order from this three-column slide."],
     ["Fat stranding and herniated orbital contents",
      "Those are orbital findings."],
     ["Air-fluid levels and sinus opacification",
      "Those are sinus findings."],
     ["Dermal thickening, increased echogenicity and cobblestoning",
      "Those are ultrasound findings in cellulitis."]],
   c=0, cite=c(37)),

 dict(topic="Facial fractures", io=IOJ, slot="test finding",
   q="Which findings describe a blow-out fracture on orbital computed tomography?",
   opts=[
     ["Air in the orbit as orbital emphysema, a fracture of the orbital floor, and soft tissue extending into the top of the maxillary sinus",
      "Correct — the three features the figure description gives."],
     ["Diastasis of the frontozygomatic suture and a fracture through the lateral wall of the maxillary sinus",
      "Those describe the tripod fracture."],
     ["A rim-enhancing collection within the orbital fat",
      "That is an orbital abscess, not a fracture."],
     ["Opacification of the maxillary sinus with mucosal thickening only",
      "Those are sinusitis findings rather than fracture findings."]],
   c=0, cite=cn(38)),

 dict(topic="Facial fractures", io=IOJ, slot="test finding",
   q="Which findings describe a tripod fracture?",
   opts=[
     ["Diastasis of the frontozygomatic suture, a fracture of the orbital floor with orbital emphysema, and a fracture through the lateral wall of the maxillary sinus",
      "Correct — the three components as described, with the sinus filled with blood."],
     ["A fracture of the orbital floor alone, with soft tissue herniating into the maxillary sinus",
      "That is the blow-out fracture."],
     ["A fracture of the nasal bones with septal deviation and periorbital bruising",
      "Not the pattern described."],
     ["A fracture of the zygomatic arch alone, without orbital involvement",
      "The tripod pattern involves the orbit as well."]],
   c=0, cite=cn(38)),

 dict(topic="Neck masses", io=IOK, slot="first-line",
   q="Which three characteristics does ultrasound establish when a neck mass is first worked up?",
   opts=[
     ["Cystic versus solid, size, and vascularity",
      "Correct — the three ultrasound answers listed."],
     ["Cystic versus solid, depth, and bone involvement",
      "Depth and bone involvement are not what the deck assigns to ultrasound here."],
     ["Malignant versus benign, size, and nodal station",
      "Ultrasound is not asked to make the malignancy call."],
     ["Abscess versus phlegmon, airway patency, and mediastinal spread",
      "Those are contrast computed tomography questions for deep neck infection."]],
   c=0, cite=c(39)),

 dict(topic="Neck masses", io=IOK, slot="escalation",
   q="After ultrasound, when are computed tomography or magnetic resonance of the neck used?",
   opts=[
     ["For deep or indeterminate masses, and for suspected malignancy",
      "Correct — the two escalation triggers the slide names."],
     ["For any mass that is cystic on ultrasound",
      "Cystic character is a result, not a trigger."],
     ["For any mass with increased vascularity on Doppler",
      "Vascularity is one of the ultrasound descriptors rather than an escalation trigger."],
     ["For every neck mass, as a routine second study",
      "The deck escalates selectively, not routinely."]],
   c=0, cite=c(39)),

 dict(topic="Deep neck infection", io=IOK, slot="escalation",
   q="What are the three things contrast computed tomography of the neck evaluates in deep neck infection?",
   opts=[
     ["A drainable abscess, airway compromise, and spread towards the mediastinum",
      "Correct — the three questions this study is asked."],
     ["Cystic versus solid character, size, and vascularity",
      "Those are the ultrasound descriptors for a neck mass."],
     ["Perineural spread, skull base involvement, and intracranial extension",
      "Those are magnetic resonance strengths."],
     ["Bone erosion, gas, and foreign body",
      "Those are general computed tomography findings, not this slide's three."]],
   c=0, cite=c(39)),

 dict(topic="Deep neck infection", io=IOK, slot="escalation",
   q="For which three complications does magnetic resonance add value in the neck?",
   opts=[
     ["Intracranial extension, vascular thrombosis, and osteomyelitis",
      "Correct — the deck names Lemierre syndrome as the vascular thrombosis example."],
     ["Drainable abscess, airway compromise, and mediastinal spread",
      "Those are the contrast computed tomography questions."],
     ["Cystic character, size, and vascularity",
      "Those are ultrasound descriptors."],
     ["Bone erosion, gas, and foreign body",
      "Those are computed tomography strengths."]],
   c=0, cite=c(39)),

 dict(topic="Deep neck infection", io=IOK, slot="complication",
   q="Which syndrome does the deck give as the example of vascular thrombosis in deep neck infection?",
   opts=[
     ["Lemierre syndrome",
      "Correct — named on the slide as the magnetic resonance indication for vascular thrombosis."],
     ["Ludwig angina",
      "A deep neck infection, but not the one the deck names for thrombosis."],
     ["Horner syndrome",
      "Not an infective complication named here."],
     ["Cavernous sinus thrombosis",
      "A serious complication, but Lemierre is the one the slide names."]],
   c=0, cite=c(39)),

 dict(topic="Applying the principles", io=IOL, slot="first-line",
   q="Which four questions does the deck ask you to consider about any test?",
   opts=[
     ["What does it evaluate well, when do we order it, what are its strengths and limitations, and how do the results confirm the condition",
      "Correct — the four framing questions on the clinical applications slide."],
     ["What does it cost, how long does it take, who performs it, and where is it available",
      "Practical questions, but not the four the slide asks."],
     ["What is its sensitivity, its specificity, its predictive value, and its likelihood ratio",
      "Those are Lecture 1 concepts, not this slide's four questions."],
     ["Is it invasive, is it painful, is it repeatable, and is it covered by insurance",
      "None of these four is on the slide."]],
   c=0, cite=c(40)),

 dict(topic="Applying the principles", io=IOL, slot="first-line",
   q="What closing rule does the deck give for choosing a test?",
   opts=[
     ["Always choose the least invasive test that answers the clinical question",
      "Correct — the closing rule, which ties back to the four selection principles."],
     ["Always choose the most sensitive test available",
      "The rule is about invasiveness, not sensitivity."],
     ["Always choose the fastest test the department can provide",
      "Speed is one advantage of computed tomography but is not the closing rule."],
     ["Always choose the test the specialist will want to see",
      "Not the rule the deck gives."]],
   c=0, cite=c(40)),

 dict(topic="Applying the principles", io=IOL, slot="first-line",
   q="Which five presentations does the deck's case wrap-up cover?",
   opts=[
     ["Scaly rash, painful red eye, sore throat, neck mass and deep neck infection",
      "Correct — the five cases as listed."],
     ["Scaly rash, painful red eye, hearing loss, neck mass and sinusitis",
      "Hearing loss and sinusitis are not among the five."],
     ["Abscess, cellulitis, sore throat, red eye and neck mass",
      "Abscess and cellulitis are not listed as separate cases."],
     ["Pigmented lesion, red eye, sore throat, ear pain and neck mass",
      "Pigmented lesion and ear pain are not among the five."]],
   c=0, cite=c(42)),

 dict(topic="Applying the principles", io=IOL, slot="first-line",
   q="A patient has a scaly rash you suspect is fungal. Which test does the deck's approach select first, and why?",
   opts=[
     ["A potassium hydroxide preparation, because it is quick, inexpensive and answers the infection question directly",
      "Correct — it is the least invasive test that answers the question asked."],
     ["A punch biopsy, because it gives a full-thickness sample",
      "Biopsy is for persistent undiagnosed rash or suspected neoplasm, and is more invasive than needed here."],
     ["A skin culture, because it identifies the organism with susceptibilities",
      "Culture is indicated for purulent lesions rather than a scaly rash."],
     ["Point-of-care ultrasound, because it is non-invasive and immediately available",
      "Ultrasound answers the abscess-versus-cellulitis question, not this one."]],
   c=0, cite=c(4)),

 dict(topic="Applying the principles", io=IOL, slot="first-line",
   q="A contact-lens wearer presents with a painful red eye and foreign-body sensation. Which two bedside tests does this lecture point to?",
   opts=[
     ["Visual acuity, then fluorescein examination under cobalt-blue light",
      "Correct — acuity is indicated for every eye complaint, and this history is a fluorescein indication."],
     ["Tonometry, then visual field testing by confrontation",
      "Tonometry is for suspected glaucoma; the field test assesses the pathway."],
     ["Fluorescein examination alone, since acuity will be reduced by the pain",
      "Acuity is indicated for every eye complaint regardless."],
     ["Visual field testing, then contrast computed tomography of the orbits",
      "Orbital imaging is reserved for proptosis, eye signs or neurologic signs."]],
   c=0, cite=c(19)),
]
