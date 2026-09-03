# -*- coding: utf-8 -*-
"""CMS I Exam 3, Lecture 16 -- vignette set B.

The inner ear syndromes, the retrocochlear and central causes, the remaining
acquired sensorineural causes, and non-organic loss.

DELIBERATELY LIGHT ON DIAGNOSIS LEAD-INS. Set A came out a third pure
diagnosis because the vertigo entities separate so cleanly, and the CMS papers
ask far more often for the next step, the treatment or the education. This pool
carries the counterweight so the partition can hold the cap.

FIVE options. Correct answer authored FIRST; cms_e3_partition.py rotates it.
"""
D = "16. Disorders of Inner Ear 2026 - Dr. Jaquith.pptx, Slide %d"
IO_A = ("a — Inner ear, balance and hearing loss conditions: etiologies, epidemiology, risk "
        "factors, clinical manifestations, differential diagnosis, diagnostic testing, "
        "management, referrals, patient education, prognosis")
IO_F = "f — Interpret results of vestibular testing"
IO_G = ("g — Identify medical care strategies for disorders of the inner ear, balance and "
        "hearing loss by population: infant, child, adolescent, adult")

QUESTIONS = [
 # ---------------------------- Meniere ----------------------------
 dict(topic="Meniere disease", io=IO_A, lead="defining feature", cite=D % 69,
  q="A 45-year-old woman has recurrent attacks of spinning that last three to four hours, with nausea, a low roaring noise and a feeling of pressure in the right ear. Her hearing fluctuates. Which feature separates this from positional vertigo?",
  opts=[["Hearing is affected", "Correct — positional vertigo leaves hearing untouched and causes no tinnitus."],
        ["Nausea is present", "Both may cause nausea."],
        ["The onset is sudden", "Both begin suddenly."],
        ["It recurs", "Both recur."],
        ["It is one-sided", "Both may be one-sided."]]),

 dict(topic="Meniere disease", io=IO_A, lead="next step", cite=D % 68,
  q="A 41-year-old man has fluctuating hearing loss, tinnitus, aural fullness and episodic vertigo. Which treatable cause must be excluded because it is indistinguishable?",
  opts=[["Syphilis", "Correct — its presentation is often identical, and it is treatable."],
        ["Otosclerosis", "That is conductive with a normal drum and no vertigo."],
        ["Cerumen impaction", "Wax does not cause vertigo or fluctuating loss."],
        ["Presbycusis", "That is gradual, bilateral and symmetrical."],
        ["Exostosis", "Those are bony canal growths causing conductive loss."]]),

 dict(topic="Meniere disease", io=IO_A, lead="defining feature", cite=D % 69,
  q="A 50-year-old woman with episodic vertigo has an audiogram showing loss confined to the low frequencies, which improves between attacks. What does this pattern suggest?",
  opts=[["Meniere disease", "Correct — low-frequency, fluctuating sensorineural loss."],
        ["Presbycusis", "That declines steadily at high frequencies and never recovers."],
        ["Noise-induced loss", "That follows exposure and leaves a fixed high-frequency loss."],
        ["Otosclerosis", "That is conductive."],
        ["Acoustic neuroma", "That is progressive rather than fluctuating."]]),

 # ------------------------------ BPPV ------------------------------
 dict(topic="Benign paroxysmal positional vertigo", io=IO_A, lead="next step", cite=D % 93,
  q="A 58-year-old woman has brief spinning attacks whenever she rolls over in bed, each lasting under a minute, with normal hearing. Which test should be performed?",
  opts=[["The Dix-Hallpike manoeuvre", "Correct — it provokes the classic eye movements."],
        ["The Epley manoeuvre", "That is the treatment, applied once the diagnosis is made."],
        ["Tympanometry", "That assesses the middle ear."],
        ["The Weber test", "That is a hearing test."],
        ["Magnetic resonance angiography", "That assesses the vessels."]]),

 dict(topic="Benign paroxysmal positional vertigo", io=IO_A, lead="treatment", cite=D % 93,
  q="A 60-year-old man has a positive Dix-Hallpike test on the right. What treatment follows?",
  opts=[["The Epley manoeuvre", "Correct — it repositions the debris in the canal."],
        ["A course of oral antibiotics", "There is no infection."],
        ["Intratympanic gentamicin", "Not the treatment described here."],
        ["Bed rest for two weeks", "Rest does not reposition the debris."],
        ["A hearing aid", "Hearing is not affected."]]),

 dict(topic="Benign paroxysmal positional vertigo", io=IO_A, lead="next step", cite=D % 91,
  q="A 55-year-old woman reports positional spinning attacks that each last twenty minutes. What should this prompt?",
  opts=[["Considering an alternative diagnosis", "Correct — beyond a minute, positional vertigo becomes unlikely."],
        ["Immediate Epley treatment", "The duration does not fit the diagnosis."],
        ["Reassurance that this is typical", "The duration is atypical."],
        ["Starting a diuretic", "Not indicated on this history alone."],
        ["Referral for a hearing aid", "Hearing is not the issue."]]),

 dict(topic="Benign paroxysmal positional vertigo", io=IO_A, lead="patient education", cite=D % 92,
  q="A 62-year-old man treated for positional vertigo asks why he still feels unsteady hours later. What should he be told?",
  opts=[["Imbalance can persist for hours after an episode", "Correct, and chronic balance complaints are common."],
        ["This means the treatment failed", "Lingering imbalance is expected."],
        ["This indicates a stroke", "There are no focal features described."],
        ["This means the diagnosis was wrong", "The pattern is consistent."],
        ["This is a side effect of the manoeuvre", "It reflects the condition rather than the treatment."]]),

 # --------------- labyrinthitis and vestibular neuronitis ---------------
 dict(topic="Labyrinthitis", io=IO_A, lead="treatment", cite=D % 95,
  q="A 38-year-old woman has sudden vertigo and reduced hearing on one side, lasting four days. She is afebrile. What treatment is appropriate?",
  opts=[["Symptomatic treatment with meclizine", "Correct — antibiotics are added only if bacterial features appear."],
        ["Immediate antibiotics", "There are no bacterial features such as fever."],
        ["The Epley manoeuvre", "That treats positional vertigo."],
        ["Urgent surgery", "Surgery is not indicated."],
        ["A hearing aid immediately", "That does not address the acute illness."]]),

 dict(topic="Labyrinthitis", io=IO_A, lead="next step", cite=D % 95,
  q="A 42-year-old man with sudden vertigo and hearing loss develops a fever of thirty-nine degrees Celsius. How does this change management?",
  opts=[["Add antibiotics", "Correct — antibiotics are given if bacterial features are present."],
        ["Stop all treatment", "Treatment should be escalated rather than stopped."],
        ["Perform the Epley manoeuvre", "That treats positional vertigo."],
        ["Arrange a hearing aid", "That does not address the infection."],
        ["Reassure and discharge", "Fever warrants a change in management."]]),

 dict(topic="Vestibular neuronitis", io=IO_A, lead="prognosis", cite=D % 96,
  q="A 36-year-old man has dramatic sudden vertigo with nausea and unsteadiness. His hearing is normal and there are no focal neurological findings. What should he be told about the outlook?",
  opts=[["It is benign and self-limiting", "Correct, though balance symptoms may last months."],
        ["It will progress to permanent deafness", "Hearing is not affected."],
        ["It requires urgent surgery", "Surgery is not indicated."],
        ["It indicates a brain tumour", "There are no features suggesting that."],
        ["It will recur every week indefinitely", "That is not the described course."]]),

 dict(topic="Vestibular neuronitis", io=IO_A, lead="defining feature", cite=D % 96,
  q="A 39-year-old woman has severe vertigo for three days. Which two findings would move the diagnosis away from vestibular neuronitis?",
  opts=[["Hearing loss or focal neurological signs", "Correct — neither belongs to this condition."],
        ["Nausea or vomiting", "Both are expected features."],
        ["Unsteadiness on walking", "Gait imbalance is part of the picture."],
        ["Sudden onset", "The onset is characteristically dramatic and sudden."],
        ["Symptoms lasting several days", "That is the expected duration."]]),

 dict(topic="Vestibular neuronitis", io=IO_A, lead="treatment", cite=D % 96,
  q="A 44-year-old man in the acute phase of vestibular neuronitis is vomiting repeatedly. Which combination is appropriate?",
  opts=[["Meclizine and an antiemetic", "Correct; the role of oral corticosteroids is uncertain."],
        ["Antibiotics and an antiemetic", "There is no bacterial infection."],
        ["An antifungal and rest", "There is no fungal infection."],
        ["A diuretic and salt restriction", "That approach belongs to a different condition."],
        ["Immediate surgery", "Surgery is not indicated."]]),

 # ------------------------- acoustic neuroma -------------------------
 dict(topic="Acoustic neuroma", io=IO_A, lead="next step", cite=D % 75,
  q="A 54-year-old woman has one-sided hearing loss and understands words far worse than her tone thresholds would predict, with some unsteadiness. Which study should be ordered?",
  opts=[["Magnetic resonance imaging with gadolinium", "Correct — the gold standard for retrocochlear disease."],
        ["Computed tomography without contrast", "Not the study named for this purpose."],
        ["Tympanometry", "That assesses the middle ear."],
        ["Plain radiography", "It lacks the necessary detail."],
        ["The Dix-Hallpike manoeuvre", "That provokes positional vertigo."]]),

 dict(topic="Acoustic neuroma", io=IO_A, lead="treatment", cite=D % 75,
  q="A 60-year-old man has a small acoustic neuroma with mild symptoms. Which options should be discussed?",
  opts=[["Observation with annual imaging, surgery or radiation", "Correct."],
        ["Antibiotics alone", "It is a tumour, not an infection."],
        ["Ear drops alone", "Drops do not reach it."],
        ["Tympanostomy tubes", "Tubes address middle ear ventilation."],
        ["No treatment is ever available", "Several options exist."]]),

 dict(topic="Acoustic neuroma", io=IO_A, lead="clinical manifestation", cite=D % 73,
  q="A 57-year-old woman with a known acoustic neuroma develops facial numbness and weakness. Which cranial nerves has the tumour involved?",
  opts=[["The fifth and seventh", "Correct."],
        ["The third and fourth", "Those control eye movement."],
        ["The ninth and tenth", "Those are involved in glomus tumours."],
        ["The first and second", "Smell and vision are not involved."],
        ["The eleventh and twelfth", "Not the nerves described."]]),

 # -------------------- sudden sensorineural loss --------------------
 dict(topic="Sudden sensorineural hearing loss", io=IO_A, lead="next step", cite=D % 79,
  q="A 48-year-old man wakes with profound hearing loss in the right ear. The canal and drum are normal and there is no wax. What is the appropriate action?",
  opts=[["Refer to a specialist today", "Correct — the corticosteroid window is short."],
        ["Review in six weeks", "Delay closes the treatment window."],
        ["Prescribe antibiotic drops", "Drops do not reach the inner ear."],
        ["Reassure and take no action", "Urgent assessment is required."],
        ["Arrange routine audiometry in three months", "The delay is unsafe."]]),

 dict(topic="Sudden sensorineural hearing loss", io=IO_A, lead="patient education", cite=D % 79,
  q="A 51-year-old woman with sudden one-sided hearing loss asks why she must be seen the same day. What should she be told?",
  opts=[["Treatment works only if started early", "Correct."],
        ["The condition is contagious", "It is not."],
        ["Surgery must be done within hours", "Surgery is not the treatment."],
        ["It always signals a tumour", "Retrocochlear pathology is rare here."],
        ["The other ear will be affected by tomorrow", "That is not the concern."]]),

 # ------------------------ perilymphatic fistula ------------------------
 dict(topic="Perilymphatic fistula", io=IO_A, lead="etiology", cite=D % 63,
  q="A 35-year-old man develops sudden hearing loss and vertigo immediately after lifting a heavy weight, hearing a pop at the moment of onset. What is the likely mechanism?",
  opts=[["An abnormal opening at the round or oval window", "Correct."],
        ["Inflammation of the vestibular nerve", "That comes on without a straining trigger."],
        ["Debris in the semicircular canal", "That causes brief positional attacks."],
        ["A tumour of the eighth nerve", "That is gradual."],
        ["Fixation of the stapes", "That is a gradual conductive problem."]]),

 dict(topic="Perilymphatic fistula", io=IO_A, lead="next step", cite=D % 64,
  q="A 40-year-old diver has sudden hearing loss and vertigo after a dive, with a popping sensation at onset. What is appropriate management?",
  opts=[["Symptomatic treatment and specialist referral", "Correct."],
        ["Reassurance alone", "It requires specialist assessment."],
        ["The Epley manoeuvre", "That treats positional vertigo."],
        ["Antibiotic drops", "Drops do not reach the inner ear."],
        ["Immediate wax removal", "There is no wax described."]]),

 # ------------------- autoimmune, syphilis, AIDS -------------------
 dict(topic="Autoimmune sensorineural loss", io=IO_A, lead="defining feature", cite=D % 65,
  q="A 43-year-old woman has bilateral hearing loss that has worsened in steps over two years, with periods of stability between. What does this pattern suggest?",
  opts=[["An autoimmune cause", "Correct — deterioration alternating with stabilisation is characteristic."],
        ["Presbycusis", "That declines steadily rather than in steps."],
        ["Noise-induced loss", "That follows exposure and does not stabilise in this way."],
        ["Cerumen impaction", "Wax would be visible and is easily reversed."],
        ["Otosclerosis", "That is conductive and gradual."]]),

 dict(topic="Autoimmune sensorineural loss", io=IO_A, lead="next step", cite=D % 66,
  q="A 47-year-old man has isolated sensorineural hearing loss with no systemic symptoms. Should an autoimmune screen be sent?",
  opts=[["No — test only when the picture suggests it", "Correct; routine screening is not warranted."],
        ["Yes, in every patient", "Routine screening is not warranted."],
        ["Yes, but only if over sixty", "Age is not the criterion."],
        ["Yes, but only in women", "Sex is not the criterion."],
        ["Never, under any circumstances", "Testing has a place when the picture suggests it."]]),

 dict(topic="AIDS-related sensorineural loss", io=IO_A, lead="next step", cite=D % 67,
  q="A 36-year-old man with unexplained sensorineural hearing loss has multiple risk factors for sexually transmitted infection. What should be considered?",
  opts=[["Human immunodeficiency virus and syphilis", "Correct — both can produce sensorineural loss."],
        ["Cerumen impaction", "That is conductive and visible."],
        ["Otosclerosis", "That is conductive."],
        ["Noise-induced loss", "That follows exposure history."],
        ["Barotrauma", "That follows a pressure change."]]),

 dict(topic="Syphilitic sensorineural loss", io=IO_A, lead="next step", cite=D % 68,
  q="A 44-year-old man has fluctuating hearing loss, tinnitus and vertigo. Syphilis is suspected. Which test should NOT be relied on?",
  opts=[["The Venereal Disease Research Laboratory test", "Correct — it is specifically described as not helpful here."],
        ["Fluorescent treponemal antibody testing", "That is one of the two recommended tests."],
        ["Microhaemagglutination assay", "That is the other recommended test."],
        ["Audiometry", "That characterises the loss."],
        ["Otoscopy", "That excludes conductive causes."]]),

 dict(topic="Syphilitic sensorineural loss", io=IO_A, lead="treatment", cite=D % 68,
  q="A 39-year-old woman has confirmed syphilitic sensorineural hearing loss. What treatment is given?",
  opts=[["An antibiotic with systemic corticosteroids", "Correct."],
        ["Corticosteroids alone", "The infection must be treated."],
        ["A hearing aid alone", "The underlying infection needs treating."],
        ["An antifungal", "The organism is bacterial."],
        ["Observation", "Treatment is required."]]),

 # ----------------------- hereditary -----------------------
 dict(topic="Hereditary sensorineural loss", io=IO_G, lead="next step", cite=D % 71,
  q="A 4-year-old girl has bilateral sensorineural hearing loss, a white forelock and eyes of different colours. Which condition does this suggest?",
  opts=[["Waardenburg syndrome", "Correct — one of the named hereditary causes."],
        ["Alport syndrome", "That is associated with kidney disease."],
        ["Usher syndrome", "That is associated with visual loss."],
        ["Meniere disease", "That presents with episodic vertigo in adults."],
        ["Presbycusis", "That is age-related."]]),

 dict(topic="Hereditary sensorineural loss", io=IO_G, lead="next step", cite=D % 71,
  q="A 9-year-old boy has sensorineural hearing loss and blood in his urine. Which hereditary condition should be considered?",
  opts=[["Alport syndrome", "Correct — hearing loss with kidney involvement."],
        ["Usher syndrome", "That involves vision rather than the kidney."],
        ["Waardenburg syndrome", "That involves pigmentary changes."],
        ["Meniere disease", "That presents with episodic vertigo in adults."],
        ["Otosclerosis", "That is conductive and presents in adulthood."]]),

 # --------------------- central and vascular ---------------------
 dict(topic="Vertebrobasilar occlusion", io=IO_A, lead="next step", cite=D % 77,
  q="A 76-year-old man has acute vertigo with facial weakness, loss of pain sensation on one side of his face and the opposite side of his body, and a drooping eyelid. What does this require?",
  opts=[["Emergency evaluation for stroke", "Correct — crossed sensory findings mean a brainstem problem."],
        ["The Epley manoeuvre", "That treats positional vertigo."],
        ["Reassurance and meclizine", "These findings are not benign."],
        ["Routine audiometry", "Hearing testing does not address this."],
        ["Antibiotic ear drops", "There is no ear infection."]]),

 dict(topic="Cerebellar infarction", io=IO_A, lead="next step", cite=D % 78,
  q="A 70-year-old woman with vertigo also has a new headache and cannot walk in a straight line. What should be done?",
  opts=[["Refer urgently for neuroimaging", "Correct — ataxia and headache with vertigo are warning features."],
        ["Treat as positional vertigo", "The additional findings argue against that."],
        ["Prescribe meclizine and review in a month", "Delay is unsafe with these features."],
        ["Arrange a hearing aid", "Hearing is not the issue."],
        ["Reassure and discharge", "These features require evaluation."]]),

 dict(topic="Vertebrobasilar occlusion", io=IO_A, lead="epidemiology", cite=D % 85,
  q="An 81-year-old man has months of unsteadiness and lightheadedness with no ear symptoms. What is the commonest non-vestibular explanation at his age?",
  opts=[["Small vessel ischaemic disease", "Correct."],
        ["Positional vertigo", "That is a vestibular cause with brief positional attacks."],
        ["Meniere disease", "That is a vestibular cause with hearing loss."],
        ["Labyrinthitis", "That is a vestibular cause with sudden onset."],
        ["Wax impaction", "That causes hearing loss rather than imbalance."]]),

 # ---------------------------- non-organic ----------------------------
 dict(topic="Functional hearing loss", io=IO_A, lead="next step", cite=D % 80,
  q="A 29-year-old man claims profound hearing loss in both ears following a workplace dispute, yet speaks at a normal volume with normal articulation. What should be suspected?",
  opts=[["A functional hearing loss", "Correct — the normal voice does not fit the claimed loss."],
        ["Profound sensorineural loss", "That patient's voice typically changes."],
        ["Bilateral wax impaction", "That is conductive and visible."],
        ["Ototoxicity", "That requires a drug exposure history."],
        ["Otosclerosis", "That is conductive and gradual."]]),

 dict(topic="Vestibular testing", io=IO_F, lead="next step", cite=D % 74,
  q="A 53-year-old woman has episodic vertigo thought to arise from one ear. Which study is the gold standard for a disorder affecting one ear at a time?",
  opts=[["Electronystagmography", "Correct."],
        ["Pure tone audiometry", "That measures hearing rather than balance."],
        ["Tympanometry", "That measures middle ear compliance."],
        ["Otoscopy", "That examines the canal and drum."],
        ["The Weber test", "That is a hearing test."]]),
]
