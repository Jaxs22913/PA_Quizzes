# -*- coding: utf-8 -*-
"""Lecture 16 questions for the ENT master exams -- Inner Ear, Balance and Hearing Loss."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "16. Disorders of Inner Ear"
IO = ("Disorders of the inner ear, balance and hearing loss: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")

QUESTIONS = [

Q("Ototoxicity", IO,
  "A 67-year-old woman is brought by her husband, who says she never listens to him. She admits "
  "she sometimes asks people on her right to repeat themselves. She denies dizziness, headache and "
  "visual change. Her only medication is furosemide. Weber lateralises to the left. On the left, "
  "air conduction lasts 15 seconds and bone conduction 10 seconds; on the right, air conduction "
  "lasts 22 seconds and bone conduction 10 seconds.",
  [["Ototoxicity from the loop diuretic",
    "Correct. Both ears have air conduction longer than bone conduction, which is the normal Rinne "
    "pattern and is also what a sensorineural ear gives, so the loss must be sensorineural rather "
    "than conductive. Weber lateralising to the left means the RIGHT is the worse ear, matching her "
    "symptom. Loop diuretics are ototoxic, and that is the only exposure in the history."],
   ["Cerumen impaction",
    "Wax occluding a canal produces a conductive loss, which would reverse Rinne in that ear so bone "
    "beat air. Both ears here show air beating bone, so nothing is obstructing sound before the "
    "cochlea."],
   ["Otosclerosis",
    "Stapes fixation is also conductive, so it too would give bone longer than air on the affected "
    "side and would pull Weber TOWARD the bad ear. Here Weber goes away from the worse ear, which is "
    "the opposite of what otosclerosis produces."],
   ["Meniere disease",
    "Meniere causes episodic vertigo lasting hours with fluctuating low-frequency loss, tinnitus and "
    "aural fullness. She explicitly denies dizziness, and there is no episodic pattern, so the "
    "syndrome's defining features are absent."]],
  "cause", D, 32),

Q("Benign paroxysmal positional vertigo", IO,
  "A 61-year-old patient has a one-week history of intermittent room-spinning dizziness. Episodes "
  "last under a minute, occur a few times daily, and are triggered by turning to the right in bed. "
  "There are no auditory changes and no neurological deficits. Dix-Hallpike with the right ear down "
  "provokes brief, fatigable nystagmus.",
  [["Benign paroxysmal positional vertigo",
    "Correct. Otoconia displaced into a semicircular canal move with head position and stimulate the "
    "canal until they settle, which is why the vertigo lasts seconds rather than hours and why it "
    "fatigues on repeated testing. The absence of hearing change is what separates it from the inner "
    "ear syndromes that involve the cochlea, and a positive Dix-Hallpike confirms it."],
   ["Meniere disease",
    "Meniere attacks last hours rather than under a minute and are accompanied by fluctuating "
    "low-frequency hearing loss, tinnitus and aural fullness. Position does not trigger them, and "
    "this patient has no auditory symptoms at all."],
   ["Labyrinthitis",
    "Labyrinthitis gives sustained vertigo lasting days to weeks WITH hearing loss, because the "
    "inflammation involves the cochlea as well as the vestibular apparatus. Neither the brief "
    "duration nor the preserved hearing fits."],
   ["Vestibular schwannoma",
    "An acoustic neuroma produces gradual unilateral sensorineural loss with speech discrimination "
    "worse than the pure tone loss predicts, plus imbalance rather than positional spinning. It does "
    "not give fatigable positional nystagmus."]],
  "diagnosis", D, 88),

Q("Meniere disease", IO,
  "A 45-year-old man has had four episodes over three months of spinning vertigo lasting two to "
  "three hours, each preceded by a sense of fullness and roaring tinnitus in the left ear. His "
  "hearing fluctuates and an audiogram during an attack shows low-frequency sensorineural loss.",
  [["Meniere disease",
    "Correct. The defining tetrad is episodic vertigo lasting minutes to hours, fluctuating "
    "sensorineural hearing loss, tinnitus and aural fullness, all in the same ear. Endolymphatic "
    "hydrops distends the membranous labyrinth, and the low-frequency pattern of loss is "
    "characteristic because the apex of the cochlea, which codes low frequencies, distends most."],
   ["Benign paroxysmal positional vertigo",
    "Positional vertigo lasts seconds, is triggered by head movement rather than arriving "
    "spontaneously, and never involves hearing. Three hours of vertigo with fluctuating hearing "
    "cannot be explained by displaced otoconia."],
   ["Vestibular neuronitis",
    "Vestibular neuronitis is a single dramatic episode of sustained vertigo lasting days with "
    "NO hearing change, usually after a viral illness. Recurrence over months with fluctuating "
    "hearing is a different disease."],
   ["Acoustic neuroma",
    "A schwannoma produces slowly progressive unilateral loss and unsteadiness rather than discrete "
    "attacks with recovery in between, and its hearing loss does not fluctuate back to normal "
    "between episodes."]],
  "diagnosis", D, 76),

Q("Vestibular neuronitis", IO,
  "A 38-year-old woman develops sudden severe vertigo with nausea and vomiting two weeks after a "
  "viral upper respiratory illness. It is constant rather than positional, has lasted three days, "
  "and is worse on head movement. Her hearing is unchanged and there are no other neurological "
  "signs.",
  [["Vestibular neuronitis",
    "Correct. Inflammation of the vestibular nerve alone, typically post-viral, gives dramatic "
    "sustained vertigo over days with nausea and vomiting. The critical discriminator is that "
    "hearing is completely spared, because the cochlear division is not involved. It is benign and "
    "self-limiting, settling over days to weeks as central compensation occurs."],
   ["Labyrinthitis",
    "Labyrinthitis is the same illness extended into the cochlea, so it presents identically EXCEPT "
    "that hearing is affected. Preserved hearing is precisely the finding that separates the two, "
    "and it is preserved here."],
   ["Benign paroxysmal positional vertigo",
    "Positional vertigo comes in bursts of seconds provoked by a change in head position and settles "
    "between them. Three days of constant vertigo is a different tempo entirely, even though "
    "movement makes any vertigo feel worse."],
   ["Cerebellar infarction",
    "A central cause must be considered with sudden vertigo, but it usually brings ataxia out of "
    "proportion, headache, facial numbness or other brainstem signs. This patient has none of them, "
    "and has a preceding viral illness pointing peripheral."]],
  "diagnosis", D, 93),

Q("Sudden sensorineural hearing loss", IO,
  "A 52-year-old man wakes to find he cannot hear from his right ear. There is no pain, discharge "
  "or trauma. Otoscopy is normal. Weber lateralises to the left and Rinne shows air conduction "
  "greater than bone conduction bilaterally.",
  [["Urgent ear, nose and throat referral for sudden sensorineural hearing loss",
    "Correct. A normal otoscopy with Weber lateralising AWAY from the affected ear and a normal "
    "Rinne pattern in both ears establishes the loss is sensorineural rather than conductive. Sudden "
    "sensorineural loss is a syndrome rather than a diagnosis, and it is time-critical: the chance "
    "of recovery falls the longer treatment is delayed, so referral is prompt rather than routine."],
   ["Reassurance and review in six weeks",
    "Six weeks is well outside the window in which intervention influences recovery. Treating sudden "
    "unilateral sensorineural loss as though it were self-limiting is the error the urgency of the "
    "referral is designed to prevent."],
   ["Microsuction of the canal for presumed wax",
    "The otoscopy is explicitly normal, so there is no obstruction to remove, and wax would in any "
    "case give a conductive picture with Weber lateralising toward the blocked ear rather than away "
    "from it."],
   ["A course of oral antibiotics for presumed otitis media",
    "There is no pain, fever, discharge or drum abnormality, so there is no infection to treat. "
    "Antibiotics also would not address a cochlear or retrocochlear cause, which is where this "
    "problem sits."]],
  "next step", D, 68),

Q("Acoustic neuroma", IO,
  "A 56-year-old woman has noticed over 18 months that she struggles to use the telephone with her "
  "left ear, though she can hear the tone. An audiogram shows a mild left sensorineural loss, but "
  "her word recognition score on that side is far poorer than the pure tone thresholds predict. She "
  "also has mild unsteadiness.",
  [["Magnetic resonance imaging with gadolinium of the internal auditory canals",
    "Correct. Speech discrimination that is disproportionately poor for the pure tone loss points "
    "beyond the cochlea to the nerve itself, because a retrocochlear lesion degrades the signal's "
    "clarity more than its audibility. Gadolinium-enhanced magnetic resonance imaging is the gold "
    "standard for detecting a vestibular schwannoma in the internal auditory canal."],
   ["Tympanometry",
    "Tympanometry measures middle ear compliance and would be normal here, because the problem is "
    "not mechanical. It cannot detect a lesion on the eighth nerve and would give false reassurance."],
   ["Computed tomography of the temporal bones without contrast",
    "Non-contrast computed tomography shows bone well and is useful for cholesteatoma or fractures, "
    "but it is poor at demonstrating a small soft-tissue tumour within the internal auditory canal. "
    "A schwannoma can be missed entirely."],
   ["Repeat audiometry in twelve months",
    "Waiting a year in a patient whose findings already point to a retrocochlear lesion allows a "
    "tumour to grow toward the brainstem, and the size at diagnosis determines both the treatment "
    "options and the chance of preserving hearing and facial nerve function."]],
  "testing", D, 105),

Q("Presbycusis", IO,
  "A 78-year-old man says he can hear that people are speaking but cannot make out the words, "
  "especially in a busy restaurant. His wife says he has the television too loud. Audiometry shows "
  "symmetrical high-frequency sensorineural loss.",
  [["Presbycusis",
    "Correct. Age-related loss begins at the high frequencies, and consonants carry most of the "
    "information that distinguishes one word from another while sitting in exactly that range. "
    "That is why patients describe hearing sound but not words, and why background noise is so much "
    "harder: the damaged cochlea cannot separate speech from competing sound."],
   ["Noise-induced hearing loss",
    "Noise damage also affects high frequencies but classically produces a notch around 4000 hertz "
    "with recovery at higher frequencies, and it requires an exposure history. Nothing here suggests "
    "occupational or recreational noise."],
   ["Otosclerosis",
    "Otosclerosis is conductive, and conductive patients hear BETTER in background noise because "
    "ambient low-frequency sound is filtered out and speakers raise their voices. This patient does "
    "distinctly worse in noise, which is the sensorineural pattern."],
   ["Conductive loss from bilateral cerumen impaction",
    "Wax would be visible on otoscopy and would produce a conductive audiogram with an air-bone gap "
    "rather than a symmetrical high-frequency sensorineural curve. It also would not selectively "
    "impair word discrimination."]],
  "diagnosis", D, 27),

Q("Tinnitus", IO,
  "A 49-year-old woman describes a whooshing sound in her right ear that keeps time with her pulse. "
  "It has been present for two months and is louder when she lies down. Her hearing is subjectively "
  "normal.",
  [["Pulsatile unilateral tinnitus, which requires investigation for a vascular cause",
    "Correct. Most tinnitus is a non-pulsatile bilateral ringing that accompanies sensorineural loss "
    "and needs no imaging. Tinnitus that is unilateral or synchronous with the pulse is the red flag "
    "combination, because it suggests turbulent blood flow or a vascular middle ear lesion such as a "
    "glomus tumour, and those need to be found."],
   ["Ordinary subjective tinnitus requiring only reassurance and sound therapy",
    "Reassurance is right for the common bilateral ringing with no red flags. Applying it here means "
    "dismissing the two features, unilaterality and pulsatility, that specifically distinguish "
    "tinnitus needing a workup from tinnitus that does not."],
   ["A symptom of Meniere disease",
    "Meniere tinnitus is typically a low roaring sound accompanying episodic vertigo, fluctuating "
    "hearing loss and aural fullness. This patient has no vertigo and no hearing change, and "
    "pulsatility is not a Meniere feature."],
   ["An expected consequence of presbycusis",
    "Age-related loss commonly brings tinnitus, but that tinnitus is bilateral and non-pulsatile, "
    "matching a symmetrical loss. A unilateral pulse-synchronous sound is not explained by cochlear "
    "ageing."]],
  "diagnosis", D, 40),

Q("Glomus tumour", IO,
  "A 54-year-old woman has pulsatile tinnitus and progressive conductive hearing loss in the left "
  "ear over a year. Otoscopy shows a reddish-blue mass behind the lower part of the tympanic "
  "membrane that blanches with pneumatic pressure.",
  [["Glomus tumour",
    "Correct. A glomus tumour is a highly vascular paraganglioma arising in the middle ear or jugular "
    "bulb. Its blood flow is what produces pulsatile tinnitus, its mass effect on the ossicular chain "
    "produces the conductive loss, and its vascularity is what makes it appear red-blue behind the "
    "drum and blanch when pressure is applied."],
   ["Haemotympanum",
    "Blood behind the drum after barotrauma or trauma also looks dark, but it arrives acutely with a "
    "precipitating event, resolves over weeks, and does not pulsate or blanch because it is static "
    "collected blood rather than a perfused mass."],
   ["Cholesteatoma",
    "Cholesteatoma appears as white keratin behind a retracted drum and produces chronic foul "
    "discharge. It has no blood supply of its own to generate pulsatile tinnitus and would not "
    "blanch."],
   ["Otitis media with effusion",
    "An effusion gives an amber or dull drum with an air-fluid level and reduced mobility, and it "
    "causes conductive loss without any vascular sign. Nothing about it pulses."]],
  "diagnosis", D, 51),

Q("Noise-induced hearing loss", IO,
  "A 31-year-old man attends a loud concert and afterwards notices muffled hearing and ringing in "
  "both ears. By two days later his hearing has returned to normal, though the ringing lingers "
  "briefly.",
  [["A temporary threshold shift, which recovers within 24 to 48 hours",
    "Correct. Intense sound temporarily fatigues the cochlear hair cells, raising the threshold at "
    "which sound is detected, and function returns as the cells recover over 24 to 48 hours. The "
    "clinical importance is that repeated temporary shifts eventually become permanent, so the "
    "recovery is a warning rather than a reassurance."],
   ["Acoustic trauma from a single impulse noise",
    "Acoustic trauma refers to a single very loud impulse, such as a blast or gunshot, causing "
    "immediate and often permanent loss and sometimes perforating the drum. Sustained concert "
    "exposure with full recovery is a different mechanism."],
   ["Early presbycusis unmasked by the noise",
    "Age-related loss is a slow symmetrical high-frequency decline over years and does not appear "
    "and resolve over 48 hours. At 31 it would also be very unusual."],
   ["Sudden sensorineural hearing loss requiring urgent referral",
    "Sudden sensorineural loss is unilateral, does not resolve spontaneously within two days, and "
    "has no obvious precipitant. Complete bilateral recovery on schedule after loud noise is the "
    "expected course of a threshold shift."]],
  "mechanism", D, 44),

Q("Conductive versus sensorineural", IO,
  "A patient's tuning fork examination shows Weber lateralising to the right ear, and on the right "
  "bone conduction is heard longer than air conduction.",
  [["A conductive loss in the right ear",
    "Correct. Two findings agree. Weber lateralising toward an ear means that ear hears "
    "bone-conducted sound better, which happens when a conductive block shields it from competing "
    "ambient noise. A reversed Rinne in the same ear, with bone beating air, means sound is being "
    "obstructed before it reaches a working cochlea. Both point to the conducting mechanism."],
   ["A sensorineural loss in the right ear",
    "A sensorineural right ear would push Weber AWAY to the left, because the damaged cochlea "
    "processes the tone poorly whichever route it arrives by. It would also leave Rinne normal, with "
    "air still beating bone, so both findings here contradict it."],
   ["A conductive loss in the left ear",
    "A left-sided conductive loss would lateralise Weber to the LEFT and reverse Rinne on the left. "
    "The findings described are both on the right, so the side is wrong even though the type is "
    "right."],
   ["Normal hearing in both ears",
    "Normal ears give a midline Weber with no lateralisation, and air conduction longer than bone in "
    "both. A lateralising Weber together with a reversed Rinne is by definition abnormal."]],
  "finding", D, 19),

Q("Labyrinthitis", IO,
  "A 42-year-old man develops sudden severe vertigo lasting several days after a viral illness, "
  "accompanied by reduced hearing and tinnitus in the left ear. There are no other neurological "
  "findings.",
  [["Labyrinthitis",
    "Correct. Inflammation of the labyrinth involves both the vestibular and the cochlear divisions, "
    "so the patient gets sustained vertigo lasting days to weeks TOGETHER WITH hearing loss and "
    "tinnitus. The presence of auditory symptoms alongside the vertigo is the single feature that "
    "distinguishes it from vestibular neuronitis."],
   ["Vestibular neuronitis",
    "Vestibular neuronitis has the same tempo and the same post-viral setting, but the cochlea is "
    "spared, so hearing is normal. Hearing loss and tinnitus are exactly what rule it out here."],
   ["Benign paroxysmal positional vertigo",
    "Positional vertigo lasts seconds per episode, is triggered by head position, and never involves "
    "hearing. Days of continuous vertigo with hearing loss matches none of those features."],
   ["Meniere disease",
    "Meniere is episodic, with attacks of hours separated by recovery, and it recurs over months "
    "with fluctuating hearing. A single sustained post-viral episode is a different pattern."]],
  "diagnosis", D, 91),

Q("Perilymphatic fistula", IO,
  "A 36-year-old man strains heavily while weightlifting and hears an audible pop in the right ear, "
  "followed immediately by hearing loss and vertigo. Symptoms worsen with straining and coughing.",
  [["Perilymphatic fistula",
    "Correct. A sudden rise in intracranial or middle ear pressure can rupture the round or oval "
    "window membrane, letting perilymph leak from the inner ear. The audible pop marks the rupture, "
    "and because the leak is pressure-dependent the symptoms characteristically worsen with "
    "straining, coughing or lifting."],
   ["Meniere disease",
    "Meniere attacks arise spontaneously rather than at the moment of a Valsalva, are not "
    "precipitated by straining, and recur over months. There is no audible pop in Meniere."],
   ["Benign paroxysmal positional vertigo",
    "Positional vertigo is provoked by a change in head position, lasts seconds, and does not affect "
    "hearing. Neither the hearing loss nor the pressure-dependence fits."],
   ["Acoustic trauma",
    "Acoustic trauma requires a loud sound, not a mechanical pressure change from straining. Lifting "
    "generates pressure rather than noise, and acoustic trauma does not produce vertigo that varies "
    "with coughing."]],
  "diagnosis", D, 60),

Q("Functional hearing loss", IO,
  "A 24-year-old man claims complete bilateral deafness following a workplace dispute. He responds "
  "appropriately when spoken to at conversational volume while facing away, his voice is of normal "
  "loudness, and audiometry is inconsistent between repeat tests.",
  [["Functional (non-organic) hearing loss",
    "Correct. Genuine profound bilateral loss removes the auditory feedback people use to regulate "
    "their own volume, so the voice becomes loud; a normal voice argues the hearing is intact. "
    "Responding to conversational speech when not lip-reading, together with inconsistent audiograms, "
    "points to a non-organic cause rather than cochlear damage."],
   ["Bilateral sudden sensorineural hearing loss",
    "Genuine sudden loss is nearly always unilateral, produces reproducible audiograms, and would "
    "change the patient's own vocal volume. Consistency of testing is the practical difference."],
   ["Ototoxicity",
    "Drug-induced loss requires an exposure, develops over a period of treatment rather than "
    "instantly after an argument, and gives reproducible symmetrical high-frequency loss on "
    "audiometry."],
   ["Bilateral cerumen impaction",
    "Wax would be immediately visible on otoscopy and would give a conductive rather than profound "
    "loss. It also could not produce inconsistent results between repeated tests."]],
  "diagnosis", D, 118),

Q("Syphilitic sensorineural loss", IO,
  "A 46-year-old man has fluctuating sensorineural hearing loss with episodic vertigo and tinnitus, "
  "clinically indistinguishable from Meniere disease. His clinician orders serologic testing before "
  "settling on the diagnosis.",
  [["Syphilis, because it mimics Meniere and is treatable",
    "Correct. Otosyphilis can reproduce the Meniere picture exactly, and the reason it is worth "
    "excluding is that it has a specific curative treatment while Meniere does not. Missing it means "
    "committing a patient to symptomatic management of an incurable syndrome when the underlying "
    "infection could have been eradicated."],
   ["Autoimmune inner ear disease",
    "Autoimmune sensorineural loss is bilateral and progressive in alternating periods of "
    "deterioration and stabilisation, rather than the discrete attacks with recovery described "
    "here, and it is not diagnosed by the serology being ordered."],
   ["Acoustic neuroma",
    "A schwannoma gives progressive unilateral loss with poor speech discrimination, not fluctuating "
    "loss with episodic vertigo, and it is diagnosed by imaging rather than by blood tests."],
   ["Ototoxicity",
    "Drug-induced loss follows an exposure and is typically bilateral, symmetrical and permanent "
    "rather than fluctuating and episodic. No ototoxic agent appears in this history."]],
  "cause", D, 66),
]
