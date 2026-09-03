# -*- coding: utf-8 -*-
"""CMS I Exam 3, Lecture 16 -- vignette set A.

The hearing-loss patterns applied at the bedside: Weber and Rinne in both
directions, audiogram and tympanogram interpretation, presbycusis, tinnitus,
ototoxicity and noise.

THE WEBER AND RINNE ITEMS ARE WRITTEN BOTH WAYS ROUND ON PURPOSE. The lecturer
described both forms explicitly -- a vignette asking which tuning fork findings
follow, and the reverse, giving the findings and asking for the diagnosis with
distractors that die on loss type. Her own worked example is the middle ear
effusion after an upper respiratory infection, so that one is here in full.

FIVE options. Correct answer authored FIRST; cms_e3_partition.py rotates it.
"""
D = "16. Disorders of Inner Ear 2026 - Dr. Jaquith.pptx, Slide %d"
IO_A = ("a — Inner ear, balance and hearing loss conditions: etiologies, epidemiology, risk "
        "factors, clinical manifestations, differential diagnosis, diagnostic testing, "
        "management, referrals, patient education, prognosis")
IO_C = "c — Apply Weber and Rinne findings to sensorineural and conductive hearing loss"
IO_D = "d — Explain how to interpret an audiogram and tympanogram"
IO_G = ("g — Identify medical care strategies for disorders of the inner ear, balance and "
        "hearing loss by population: infant, child, adolescent, adult")

QUESTIONS = [
 # ---- her own worked example, both directions ----
 dict(topic="Weber and Rinne", io=IO_C, lead="diagnostic technique", cite=D % 42,
  q="A 39-year-old man reports right ear fullness and reduced hearing that began after a head cold. He denies ringing, dizziness, fever and discharge. An amber effusion is visible behind an intact right drum, which moves poorly. The left ear is normal. Which tuning fork findings are most likely?",
  opts=[["Weber to the right; right bone conduction at least equal to air",
         "Correct. A right middle ear effusion is a conductive loss, so Weber lateralises to it and Rinne becomes abnormal there."],
        ["Weber to the left; right air conduction greater than bone",
         "That is the sensorineural pattern, and this loss is conductive."],
        ["Weber to the right; right air conduction greater than bone",
         "Weber is right, but a conductive loss reverses Rinne on that side."],
        ["Weber to the left; right bone conduction greater than air",
         "Weber lateralises toward a conductive loss, not away from it."],
        ["No lateralisation; air conduction greater than bone bilaterally",
         "That is the normal result, and this patient has a demonstrable effusion."]]),

 dict(topic="Weber and Rinne", io=IO_C, lead="diagnosis", cite=D % 42,
  q="A 52-year-old woman has reduced hearing on the left. A tuning fork on the forehead is loudest on the left, and on the left bone conduction exceeds air conduction. Which diagnosis best fits?",
  opts=[["Cerumen impaction", "Correct. These findings are conductive, and wax is a conductive cause."],
        ["Presbycusis", "That is sensorineural, so Weber would move away from the affected ear."],
        ["Acoustic neuroma", "A sensorineural cause; Weber would move away from that ear."],
        ["Ototoxicity", "Sensorineural and bilateral, so it does not fit a one-sided conductive picture."],
        ["Meniere disease", "Sensorineural, and it comes with vertigo and fullness."]]),

 dict(topic="Weber and Rinne", io=IO_C, lead="diagnosis", cite=D % 42,
  q="A 61-year-old man has reduced hearing on the right. A tuning fork on the forehead is loudest on the left, and on the right air conduction exceeds bone conduction. Which diagnosis best fits?",
  opts=[["Acoustic neuroma", "Correct. These findings are sensorineural, and this is a sensorineural cause."],
        ["Cerumen impaction", "That is conductive; Weber would lateralise to the blocked ear."],
        ["Otosclerosis", "Conductive, so bone conduction would beat air on that side."],
        ["Middle ear effusion", "Conductive, and the drum would look dull rather than normal."],
        ["Tympanic membrane perforation", "Conductive, and the defect would be visible."]]),

 dict(topic="Weber and Rinne", io=IO_C, lead="diagnostic technique", cite=D % 42,
  q="A 44-year-old woman has a three-year history of gradual hearing loss in the left ear with a normal-looking drum, and says she hears better in noisy rooms. Which tuning fork findings are expected?",
  opts=[["Weber to the left; left bone conduction at least equal to air",
         "Correct. Otosclerosis is a conductive loss."],
        ["Weber to the right; left air conduction greater than bone",
         "That is the sensorineural pattern."],
        ["Weber to the right; left bone conduction greater than air",
         "Weber lateralises toward a conductive loss, not away."],
        ["No lateralisation at all", "A unilateral loss lateralises."],
        ["Weber to the left; left air conduction greater than bone",
         "Weber is correct, but a conductive loss reverses Rinne on that side."]]),

 dict(topic="Weber and Rinne", io=IO_C, lead="diagnostic technique", cite=D % 42,
  q="A 70-year-old man has bilateral gradual hearing loss and says background noise makes it harder to follow conversation. Both drums and canals look normal. What Rinne result is expected?",
  opts=[["Air conduction greater than bone, bilaterally",
         "Correct. A sensorineural loss leaves the normal Rinne relationship intact."],
        ["Bone conduction greater than air, bilaterally", "That indicates a conductive loss."],
        ["Bone conduction greater than air on the right only", "A right-sided conductive component, which this history does not describe."],
        ["No response to either bilaterally", "That would indicate profound loss."],
        ["Bone conduction greater than air on the left only", "A left-sided conductive component, which this history does not describe."]]),

 # ---------------- audiogram and tympanogram ----------------
 dict(topic="Audiometry", io=IO_D, lead="defining feature", cite=D % 19,
  q="A 68-year-old woman's audiogram shows thresholds of fifty decibels bilaterally. How is her loss classified?",
  opts=[["Moderate", "Correct — the forty to sixty band."],
        ["Mild", "That band runs twenty to forty."],
        ["Severe", "That band runs sixty to eighty."],
        ["Profound", "That is above eighty."],
        ["Normal", "That is zero to twenty."]]),

 dict(topic="Audiometry", io=IO_D, lead="defining feature", cite=D % 19,
  q="A 75-year-old man's audiogram is normal at low frequencies and drops steeply above two thousand hertz in both ears. What does this pattern indicate?",
  opts=[["Age-related sensorineural loss", "Correct — a sloping high-frequency loss."],
        ["A conductive loss from wax", "That affects all frequencies and the canal would be blocked."],
        ["Meniere disease", "That affects low frequencies and fluctuates."],
        ["Otosclerosis", "That is conductive with a normal drum."],
        ["A middle ear effusion", "That is conductive with a dull drum."]]),

 dict(topic="Tympanometry", io=IO_D, lead="diagnosis", cite=D % 26,
  q="A 5-year-old boy has reduced hearing. His tympanogram is a flat line with no pressure peak. Which finding does this indicate?",
  opts=[["Fluid in the middle ear", "Correct — a type B trace."],
        ["A normal middle ear", "That gives a peaked type A trace."],
        ["Negative middle ear pressure", "That gives a type C trace."],
        ["A fixed stapes", "That gives a shallow type As trace."],
        ["Ossicular discontinuity", "That gives a deep type Ad trace."]]),

 dict(topic="Tympanometry", io=IO_D, lead="diagnosis", cite=D % 27,
  q="A 9-year-old girl with fullness after a cold has a tympanogram whose peak is shifted well into negative pressure. What does this indicate?",
  opts=[["Eustachian tube dysfunction", "Correct — a type C trace shows negative middle ear pressure."],
        ["Middle ear fluid", "That gives a flat type B trace."],
        ["A normal middle ear", "That peaks at atmospheric pressure."],
        ["Ossicular fixation", "That gives a shallow type As trace."],
        ["A perforated drum", "That gives a flat trace."]]),

 dict(topic="Tympanometry", io=IO_D, lead="diagnosis", cite=D % 28,
  q="A 40-year-old woman with a normal-looking drum and conductive hearing loss has a tympanogram with normal pressure but unusually low compliance. What does this suggest?",
  opts=[["Ossicular fixation", "Correct — a shallow type As trace, fitting otosclerosis."],
        ["Ossicular discontinuity", "That gives a deep type Ad trace."],
        ["Middle ear fluid", "That gives a flat type B trace."],
        ["Negative middle ear pressure", "That gives a type C trace."],
        ["A normal middle ear", "The compliance is abnormal."]]),

 # -------------------------- presbycusis --------------------------
 dict(topic="Presbycusis", io=IO_A, lead="diagnosis", cite=D % 60,
  q="A 78-year-old man says he can hear people speaking but cannot make out the words, and he misses the doorbell. Both ears are affected equally and his canals and drums are normal. What is the most likely diagnosis?",
  opts=[["Presbycusis", "Correct — bilateral, symmetrical, gradual high-frequency loss."],
        ["Otosclerosis", "That is conductive and hearing improves in noise."],
        ["Cerumen impaction", "Wax would be visible."],
        ["Acoustic neuroma", "That is characteristically unilateral."],
        ["Meniere disease", "That fluctuates and comes with vertigo and fullness."]]),

 dict(topic="Presbycusis", io=IO_G, lead="patient education", cite=D % 61,
  q="The daughter of an 80-year-old woman with age-related hearing loss asks how to make conversation easier. What advice is best?",
  opts=[["Face her and speak clearly without shouting", "Correct — the problem is discrimination, not volume."],
        ["Shout from across the room", "Volume alone does not restore clarity."],
        ["Speak quickly to hold her attention", "Slower speech helps more."],
        ["Communicate only in writing", "Speech remains useful with good technique."],
        ["Speak only into her better ear from behind", "Being able to see the speaker matters."]]),

 dict(topic="Presbycusis", io=IO_G, lead="next step", cite=D % 60,
  q="A 66-year-old man attends for a routine visit with no hearing complaint. What is appropriate?",
  opts=[["Screen his hearing", "Correct — screening is routine from age sixty-five."],
        ["No action unless he complains", "Screening is routine at this age."],
        ["Immediate referral for a hearing aid", "Screening comes first."],
        ["An urgent magnetic resonance scan", "Imaging is not a screening tool."],
        ["Tympanometry only", "That assesses the middle ear rather than screening hearing."]]),

 # --------------------------- tinnitus ---------------------------
 dict(topic="Tinnitus", io=IO_A, lead="next step", cite=D % 45,
  q="A 47-year-old woman describes ringing in the right ear only, which she can hear beating in time with her pulse. What is the appropriate response?",
  opts=[["Investigate further", "Correct — unilateral and pulsatile tinnitus are both red flags."],
        ["Reassure her that this is normal head noise", "That pattern is specifically concerning."],
        ["Prescribe an antihistamine", "It does not address the concern."],
        ["Advise her to avoid quiet rooms", "That does not address a red flag."],
        ["Arrange review in one year", "Delay is inappropriate for these features."]]),

 dict(topic="Tinnitus", io=IO_A, lead="patient education", cite=D % 46,
  q="A 55-year-old man with longstanding bilateral tinnitus asks what medication will cure it. What should he be told?",
  opts=[["No drug has proved better than placebo", "Correct — masking and biofeedback may help instead."],
        ["A short antibiotic course will clear it", "There is no infection."],
        ["Corticosteroids are curative", "They are not a cure."],
        ["Diuretics eliminate it", "Diuretics do not abolish the noise."],
        ["Antihistamines are first-line", "No antihistamine has an established role here."]]),

 dict(topic="Tinnitus", io=IO_A, lead="patient education", cite=D % 46,
  q="A 50-year-old woman with tinnitus asks what she can change herself. Which advice fits?",
  opts=[["Avoid loud noise and stimulants, and rest adequately",
         "Correct, along with daily exercise and having lead levels checked."],
        ["Spend an hour daily in complete silence", "Silence makes head noise more noticeable."],
        ["Increase caffeine intake", "Stimulants are to be avoided."],
        ["Stop all exercise", "Daily exercise is advised."],
        ["Sleep as little as possible", "Adequate rest is advised."]]),

 # -------------------------- ototoxicity --------------------------
 dict(topic="Ototoxicity", io=IO_A, lead="diagnosis", cite=D % 52,
  q="A 64-year-old man treated with intravenous gentamicin for two weeks develops hearing loss in both ears. His canals and drums are normal. What is the most likely cause?",
  opts=[["Ototoxicity", "Correct — aminoglycosides are the most ototoxic and the most commonly implicated."],
        ["Presbycusis", "That develops gradually over years, not during a two-week admission."],
        ["Otosclerosis", "That is conductive and gradual."],
        ["Cerumen impaction", "Wax would be visible."],
        ["Acoustic neuroma", "That is characteristically unilateral and gradual."]]),

 dict(topic="Ototoxicity", io=IO_A, lead="next step", cite=D % 52,
  q="A 58-year-old woman is starting a prolonged aminoglycoside course. Which monitoring is required?",
  opts=[["Peak drug levels", "Correct."],
        ["Weekly tympanometry", "That assesses the middle ear."],
        ["Daily otoscopy", "The canal and drum are not affected."],
        ["Monthly imaging", "Imaging is not the monitoring used."],
        ["No monitoring is needed", "Monitoring is specifically required."]]),

 dict(topic="Ototoxicity", io=IO_A, lead="next step", cite=D % 53,
  q="A 70-year-old man on a known ototoxic agent is being reviewed. Which additional organ should be assessed?",
  opts=[["The kidney", "Correct — ototoxic drugs are frequently nephrotoxic and vice versa."],
        ["The liver", "Liver injury is not the toxicity paired with hearing damage."],
        ["The thyroid", "No thyroid toxicity is described for these agents."],
        ["The pancreas", "No pancreatic toxicity is described for these agents."],
        ["The adrenal gland", "The adrenal gland is not affected by these agents."]]),

 dict(topic="Ototoxicity", io=IO_A, lead="etiology", cite=D % 52,
  q="A 62-year-old woman on furosemide, aspirin and platinum-based chemotherapy develops bilateral hearing loss. What should be considered?",
  opts=[["All three agents are ototoxic", "Correct — each is named as such."],
        ["Only the aspirin is relevant", "Aspirin is ototoxic, but so are the other two."],
        ["Only the furosemide is relevant", "Furosemide is ototoxic, but so are the other two."],
        ["None of these affects hearing", "All three are named ototoxic agents."],
        ["Only the chemotherapy is relevant", "The platinum agent is ototoxic, but so are the other two."]]),

 # ------------------------ noise and trauma ------------------------
 dict(topic="Noise-induced hearing loss", io=IO_A, lead="prognosis", cite=D % 54,
  q="A 20-year-old man leaves a concert with muffled hearing, a sensation of fullness and a chirping noise. By the next afternoon his hearing is back to normal. What has happened?",
  opts=[["A temporary threshold shift", "Correct — but repeated exposures make the loss permanent."],
        ["A permanent threshold shift", "His hearing recovered, so it was temporary."],
        ["Acoustic trauma with perforation", "The drum would be perforated."],
        ["Sudden sensorineural hearing loss", "That does not resolve overnight."],
        ["Barotrauma", "There was no pressure change."]]),

 dict(topic="Noise-induced hearing loss", io=IO_A, lead="patient education", cite=D % 54,
  q="A 22-year-old sound engineer whose hearing recovers by the next day after every shift asks whether that means he is safe. What should he be told?",
  opts=[["Repeated exposure makes the loss permanent", "Correct — the temporary shift is a warning, not reassurance."],
        ["Full recovery means no damage is accumulating", "Recovery does not mean the exposure is harmless."],
        ["Only exposures causing pain matter", "Damage occurs well below the pain threshold."],
        ["Hearing protection is unnecessary below one hundred decibels", "Damage is possible from about eighty decibels."],
        ["The effect is purely psychological", "The effect is a measurable threshold change."]]),

 dict(topic="Acoustic trauma", io=IO_A, lead="diagnosis", cite=D % 56,
  q="A 34-year-old man standing beside an explosion has immediate hearing loss and a perforated drum. What describes this injury?",
  opts=[["Acoustic trauma", "Correct — a single loud noise causing immediate loss."],
        ["Noise-induced hearing loss", "That accumulates over repeated exposures."],
        ["Barotrauma", "That follows a pressure change from altitude or diving."],
        ["Presbycusis", "That is gradual and age-related."],
        ["Ototoxicity", "That follows drug exposure."]]),

 dict(topic="Conductive hearing loss", io=IO_A, lead="defining feature", cite=D % 42,
  q="A 30-year-old woman with a blocked ear speaks unusually softly during the consultation. What does this suggest about her hearing loss?",
  opts=[["It is conductive", "Correct — she hears her own voice well because the inner ear is intact."],
        ["It is sensorineural", "That patient tends to speak loudly."],
        ["It is functional", "The voice change here has a physical explanation."],
        ["It is profound and bilateral", "One blocked ear does not produce that."],
        ["It is central in origin", "Not indicated by this finding."]]),

 dict(topic="Sensorineural hearing loss", io=IO_A, lead="defining feature", cite=D % 42,
  q="A 72-year-old man speaks noticeably loudly and struggles most in a crowded room. What does this suggest?",
  opts=[["A sensorineural loss", "Correct — the loud voice and worsening in noise both fit."],
        ["A conductive loss", "That patient speaks softly and hears better in noise."],
        ["Normal hearing", "These findings indicate a loss."],
        ["A functional loss", "The findings are internally consistent with an organic loss."],
        ["Wax impaction", "That is conductive."]]),

 dict(topic="Sensorineural hearing loss", io=IO_A, lead="treatment", cite=D % 13,
  q="A 55-year-old woman developed hearing loss in one ear ten days ago. Which treatment may still help?",
  opts=[["Corticosteroids", "Correct — acute sensory loss may respond within the first weeks."],
        ["A hearing aid alone", "That compensates but does not treat the acute loss."],
        ["Antibiotic ear drops", "Drops do not reach the inner ear."],
        ["Wax removal", "There is no wax described."],
        ["Observation for six months", "Delay closes the treatment window."]]),

 dict(topic="Conductive hearing loss", io=IO_A, lead="prognosis", cite=D % 11,
  q="A 28-year-old man is told his hearing loss is conductive. What should he be told about the outlook?",
  opts=[["It is often correctable", "Correct — that is the key difference from sensorineural loss."],
        ["It is never correctable", "Conductive causes are frequently treatable."],
        ["It always progresses to deafness", "That is not the expected course."],
        ["It will resolve without any treatment", "That depends entirely on the cause."],
        ["It always requires a cochlear implant", "Implants address profound sensorineural loss."]]),

 dict(topic="Hearing screening", io=IO_D, lead="diagnostic technique", cite=D % 8,
  q="A 60-year-old woman is referred for formal hearing assessment. Single tones are presented at set frequencies and she signals the softest she can hear. Which test is this?",
  opts=[["Pure tone audiometry", "Correct."],
        ["Tympanometry", "That measures middle ear compliance."],
        ["Electronystagmography", "That assesses vestibular function."],
        ["The Dix-Hallpike manoeuvre", "That provokes positional vertigo."],
        ["The Rinne test", "That is a tuning fork comparison."]]),

 dict(topic="Exostosis", io=IO_A, lead="diagnosis", cite=D % 48,
  q="A 31-year-old surfer has gradual hearing loss and repeated trapping of debris in both canals. Both canals are narrowed symmetrically by hard, smooth swellings of the canal wall. What is the most likely diagnosis?",
  opts=[["Exostoses", "Correct — bony growths from repeated cold water exposure."],
        ["Cerumen impaction", "Wax is soft and removable rather than a hard canal wall swelling."],
        ["Otitis externa", "The canal would be red, tender and swollen."],
        ["Canal carcinoma", "That is a friable growth, usually one-sided, that bleeds."],
        ["Cholesteatoma", "That lies behind the drum."]]),

 dict(topic="Glomus tumour", io=IO_A, lead="diagnosis", cite=D % 50,
  q="A 46-year-old woman has hearing loss in the left ear and a whooshing noise in time with her heartbeat. A reddish mass is visible behind the left drum. What is the most likely diagnosis?",
  opts=[["Glomus tumour", "Correct — a vascular middle ear mass with pulsatile tinnitus."],
        ["Cholesteatoma", "That appears as white keratin debris, not a vascular mass."],
        ["Middle ear effusion", "That is amber fluid, and the tinnitus would not be pulsatile."],
        ["Acoustic neuroma", "That is not visible behind the drum."],
        ["Otosclerosis", "The drum looks normal in otosclerosis."]]),
]
