# -*- coding: utf-8 -*-
"""Lecture 16, second pool -- Inner Ear, Balance and Hearing Loss."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "16. Disorders of Inner Ear"
IO = ("Disorders of the inner ear, balance and hearing loss: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")

QUESTIONS = [

Q("Audiometry", IO,
  "An audiogram reports a patient's thresholds at 70 decibels across the speech frequencies.",
  [["Severe hearing loss",
    "Correct. The severity bands run in twenties: normal is 0 to 20 decibels, mild 20 to 40, "
    "moderate 40 to 60, severe 60 to 80, and profound above 80. Seventy decibels therefore falls in "
    "the severe band, and remembering that the boundaries are all multiples of twenty makes the "
    "whole scale recoverable without memorising each one."],
   ["Moderate hearing loss",
    "Moderate covers 40 to 60 decibels, so 70 sits a full band above it. Placing a patient a "
    "category too low understates how much amplification or intervention they are likely to need."],
   ["Profound hearing loss",
    "Profound begins above 80 decibels, which is the band in which spoken conversation is "
    "inaccessible without amplification. Seventy is severe but has not reached that threshold."],
   ["Mild hearing loss",
    "Mild is 20 to 40 decibels, where speech is audible but soft consonants are missed. Seventy "
    "decibels is two bands beyond it and describes a very different functional problem."]],
  "testing", D, 24),

Q("Tympanometry", IO,
  "A patient with reduced hearing has a tympanogram showing a shallow peak at normal middle ear "
  "pressure.",
  [["A stiff conducting mechanism, as in ossicular fixation",
    "Correct. Peak compliance occurring at normal pressure means the middle ear is ventilating "
    "properly, so the eustachian tube is working. A shallow peak means the system does not move much "
    "at any pressure, which indicates stiffness rather than fluid. That is the type As pattern and "
    "points to ossicular fixation such as otosclerosis, or to tympanosclerosis."],
   ["Fluid in the middle ear",
    "Fluid gives a flat trace with no peak at all, because the drum cannot move at any applied "
    "pressure. A peak that exists but is shallow means there is still air behind the drum."],
   ["Eustachian tube dysfunction",
    "Poor ventilation shifts the peak to NEGATIVE pressure, because that is where middle ear "
    "pressure actually sits once trapped air is absorbed. Here the peak is at normal pressure, so "
    "ventilation is intact."],
   ["Ossicular discontinuity",
    "A disconnected ossicular chain makes the system too floppy, giving an abnormally DEEP peak. "
    "That is the opposite mechanical abnormality to the shallow trace described."]],
  "testing", D, 25),

Q("Vestibular testing", IO,
  "A clinician wishes to assess each vestibular apparatus separately in a patient with chronic "
  "imbalance.",
  [["Electronystagmography",
    "Correct. Electronystagmography records eye movements during caloric irrigation, which allows "
    "each labyrinth to be stimulated on its own. That is what makes it the gold standard for "
    "vestibular assessment: most bedside tests examine the system as a whole, whereas this one can "
    "say which side is underperforming."],
   ["Dix-Hallpike manoeuvre",
    "Dix-Hallpike is a provocation test for positional vertigo, diagnosing displaced otoconia in a "
    "particular canal. It answers a narrow question and does not quantify overall vestibular "
    "function on each side."],
   ["Epley manoeuvre",
    "The Epley is a treatment rather than a test: it repositions otoconia out of the affected "
    "semicircular canal. Performing it gives no measurement of vestibular function at all."],
   ["Pure tone audiometry",
    "Audiometry measures the cochlear and conductive pathways, which is the hearing side of the "
    "eighth nerve. It gives useful context in vertigo but says nothing directly about the "
    "vestibular apparatus."]],
  "testing", D, 26),

Q("Exostosis", IO,
  "A 32-year-old competitive surfer has bilateral, symmetrical, smooth bony swellings narrowing "
  "both ear canals. He reports recurrent trapped water and occasional infections.",
  [["Exostoses",
    "Correct. Repeated exposure to cold water stimulates new bone formation in the canal walls, "
    "which is why the condition is known as surfer's ear and why it is bilateral and symmetrical. "
    "The clinical consequence is a narrowed canal that traps water and debris, producing the "
    "recurrent otitis externa he describes."],
   ["Osteoma",
    "An osteoma is a solitary benign bony tumour of the canal, typically unilateral and pedunculated "
    "rather than broad-based. The bilateral symmetry here, with a clear cold-water history, points "
    "away from a single neoplastic lesion."],
   ["Cerumen impaction",
    "Wax is soft, removable and would not appear as smooth bony swellings. It can certainly coexist "
    "in a narrowed canal, but it does not explain the underlying stenosis."],
   ["Cholesteatoma",
    "Cholesteatoma is a keratin sac in the middle ear behind a retracted drum, producing chronic "
    "foul discharge and conductive loss. It is not a bony canal wall change and is not related to "
    "water exposure."]],
  "diagnosis", D, 49),

Q("Sensorineural versus conductive", IO,
  "A patient reports that they hear conversation distinctly better in a crowded noisy room than in "
  "a quiet one.",
  [["A conductive loss",
    "Correct. This is paracusis, and it happens for two reasons that reinforce each other. A "
    "conductive block filters out low-frequency ambient noise more effectively than it filters "
    "speech, and everyone raises their voice in a noisy room. Sensorineural patients experience the "
    "exact opposite, which makes this symptom a useful discriminator."],
   ["A sensorineural loss",
    "A damaged cochlea loses the ability to separate a speech signal from competing background "
    "sound, so sensorineural patients do distinctly WORSE in noise. Reporting improvement in noise "
    "argues directly against this."],
   ["Normal hearing",
    "People with normal hearing do not find noisy rooms easier for conversation; competing sound "
    "makes listening harder for everyone. The symptom described is abnormal and specific."],
   ["A retrocochlear lesion",
    "A lesion on the eighth nerve degrades speech discrimination out of proportion to the pure tone "
    "loss, so those patients struggle most in exactly the situations that require clarity, including "
    "noisy rooms."]],
  "mechanism", D, 65),

Q("Presbycusis", IO,
  "A 74-year-old woman with symmetrical high-frequency sensorineural loss asks why she can hear her "
  "grandson's voice but cannot understand his words.",
  [["Consonants are high-frequency sounds and carry most of the meaning",
    "Correct. Vowels are low-frequency and loud, so they remain audible and give the impression that "
    "speech is being heard. Consonants sit at high frequencies and are quieter, and they are what "
    "distinguish one word from another. Losing the high frequencies therefore removes the "
    "information while leaving the sound."],
   ["Her hearing loss is worse for low frequencies",
    "Age-related loss begins at the high frequencies and progresses downward, which is the opposite "
    "pattern. Low-frequency loss is more characteristic of Meniere disease, where the cochlear apex "
    "is affected."],
   ["The problem is central rather than cochlear",
    "Central auditory processing disorders exist and can produce this complaint, but her audiogram "
    "already demonstrates a peripheral high-frequency cochlear loss that fully explains the symptom "
    "without invoking a second pathology."],
   ["She has a conductive component reducing overall volume",
    "A conductive loss reduces loudness across frequencies fairly evenly, so speech would sound "
    "quiet rather than unclear. Her described experience is the reverse: adequate volume, inadequate "
    "clarity."]],
  "mechanism", D, 27),

Q("Acoustic trauma", IO,
  "A 24-year-old man fires a rifle without ear protection and immediately notices reduced hearing "
  "and severe ringing in the ear nearer the muzzle. Otoscopy shows a small tympanic membrane "
  "perforation.",
  [["Acoustic trauma from a single impulse noise",
    "Correct. A single very loud impulse such as a gunshot or blast delivers enough energy in "
    "milliseconds to damage hair cells immediately and, at higher intensities, to rupture the "
    "tympanic membrane. That distinguishes it from cumulative noise exposure, where damage builds "
    "over repeated sessions and the drum stays intact."],
   ["A temporary threshold shift that will fully recover",
    "Threshold shifts follow sustained loud exposure such as a concert and recover over 24 to 48 "
    "hours with an intact drum. A perforation indicates structural injury that has already gone "
    "beyond reversible hair cell fatigue."],
   ["Noise-induced hearing loss from cumulative exposure",
    "Cumulative noise damage produces a gradual symmetrical high-frequency loss, classically with a "
    "notch around 4000 hertz, over years of exposure. A single shot with immediate unilateral loss "
    "is a different mechanism."],
   ["Barotrauma",
    "Barotrauma results from a pressure differential the eustachian tube cannot equalise, typically "
    "during flying or diving. A gunshot generates an acoustic pressure wave rather than the "
    "sustained ambient pressure change that causes barotrauma."]],
  "diagnosis", D, 45),

Q("Meniere disease", IO,
  "A 47-year-old woman with confirmed Meniere disease asks what she can do herself to reduce the "
  "frequency of her attacks.",
  [["Restrict dietary salt, caffeine and alcohol",
    "Correct. The underlying abnormality is endolymphatic hydrops, an excess of endolymph distending "
    "the membranous labyrinth. Reducing sodium load lowers fluid retention and therefore endolymph "
    "volume, and caffeine and alcohol are recognised triggers. These are the measures a patient can "
    "act on before any drug is added."],
   ["Perform Epley manoeuvres at home",
    "The Epley repositions displaced otoconia and treats benign paroxysmal positional vertigo. "
    "Meniere is a fluid disorder of the labyrinth rather than a mechanical problem of loose "
    "crystals, so the manoeuvre has nothing to reposition."],
   ["Increase fluid and salt intake to maintain blood pressure",
    "This is the advice for orthostatic hypotension or vasovagal syncope, and it is precisely "
    "backwards here: raising sodium increases fluid retention and therefore endolymphatic pressure."],
   ["Avoid all physical activity during remission",
    "Vestibular activity between attacks aids central compensation, and inactivity tends to worsen "
    "chronic imbalance. Restriction is neither necessary nor helpful once an attack has settled."]],
  "treatment", D, 80),

Q("Vertebrobasilar insufficiency", IO,
  "A 76-year-old man with hypertension and atrial fibrillation has episodes of vertigo accompanied "
  "by diplopia, dysarthria and transient numbness of one arm.",
  [["Vertebrobasilar insufficiency",
    "Correct. Vertigo accompanied by other brainstem signs indicates the posterior circulation "
    "rather than the labyrinth, because the same vessels supply the vestibular nuclei, the cranial "
    "nerve nuclei and the long tracts. Diplopia, dysarthria and limb numbering alongside vertigo is "
    "the combination that moves the diagnosis centrally in a vascular patient."],
   ["Meniere disease",
    "Meniere produces vertigo with auditory symptoms confined to one ear, never diplopia, dysarthria "
    "or limb numbness. Those findings cannot arise from the inner ear because the structures "
    "involved are not there."],
   ["Benign paroxysmal positional vertigo",
    "Positional vertigo lasts seconds, is triggered by head position, and is accompanied by no other "
    "neurological signs at all. The presence of brainstem symptoms rules a peripheral cause out."],
   ["Vestibular neuronitis",
    "Vestibular neuronitis is a single sustained post-viral episode with no hearing change and no "
    "other neurological findings. Recurrent episodes with brainstem features in an elderly patient "
    "with atrial fibrillation point elsewhere."]],
  "diagnosis", D, 96),

Q("Cerebellar infarction", IO,
  "A 69-year-old woman has sudden severe vertigo with vomiting. She is unable to sit unsupported, "
  "has a severe occipital headache, and there is direction-changing nystagmus.",
  [["Cerebellar infarction",
    "Correct. Three findings each argue against a peripheral cause: truncal ataxia so severe she "
    "cannot sit, a severe headache, and direction-changing nystagmus. Peripheral vertigo produces "
    "unidirectional nystagmus and patients who are unsteady but can usually sit. This combination "
    "requires urgent imaging because the posterior fossa can swell and compress the brainstem."],
   ["Vestibular neuronitis",
    "Vestibular neuronitis gives severe vertigo but with unidirectional nystagmus and preserved "
    "ability to sit, and it does not cause headache. Attributing this picture to it risks missing a "
    "stroke in the window when it is treatable."],
   ["Labyrinthitis",
    "Labyrinthitis adds hearing loss to vestibular neuronitis but shares its peripheral signs. It "
    "does not produce direction-changing nystagmus, severe headache or an inability to sit "
    "unsupported."],
   ["Benign paroxysmal positional vertigo",
    "Positional vertigo lasts seconds per episode, is provoked by position change, and leaves the "
    "patient entirely well between episodes. Continuous vertigo with ataxia and headache is a "
    "completely different presentation."]],
  "diagnosis", D, 97),

Q("Ototoxicity", IO,
  "A 58-year-old man completes a course of intravenous gentamicin for a severe infection. He now "
  "reports bilateral high-frequency hearing loss and persistent tinnitus.",
  [["Aminoglycoside ototoxicity, which is often irreversible",
    "Correct. Aminoglycosides accumulate in cochlear hair cells and damage them, starting with the "
    "outer hair cells at the cochlear base which encode high frequencies. Because mammalian hair "
    "cells do not regenerate, the loss is typically permanent, which is why monitoring during "
    "treatment matters more than treatment afterwards."],
   ["A reversible effect that will resolve once the drug clears",
    "Loop diuretic ototoxicity can be reversible, which is where this idea comes from, but "
    "aminoglycoside damage is usually permanent because the hair cells themselves are destroyed "
    "rather than temporarily impaired."],
   ["Presbycusis unmasked by the illness",
    "Age-related loss develops over years rather than during a single course of treatment, and at 58 "
    "it would be unusual to appear this abruptly. The temporal association with a known ototoxic "
    "drug is the stronger explanation."],
   ["Noise-induced loss from the hospital environment",
    "Hospital noise does not reach the intensities required to damage hearing, and noise damage "
    "produces a characteristic notch pattern rather than a general high-frequency decline following "
    "a drug course."]],
  "cause", D, 32),

Q("Autoimmune sensorineural loss", IO,
  "A 39-year-old woman has bilateral sensorineural hearing loss that has worsened in steps over "
  "eight months, with periods of deterioration alternating with periods of stability. She has "
  "rheumatoid arthritis.",
  [["Autoimmune inner ear disease",
    "Correct. The characteristic course is bilateral, progressive loss advancing in alternating "
    "periods of deterioration and stabilisation over months, which is faster than presbycusis and "
    "slower than a sudden loss. An existing autoimmune condition supports it, and it matters because "
    "it is one of the few sensorineural losses that responds to immunosuppression."],
   ["Presbycusis",
    "Age-related loss is a slow symmetrical decline over years without discrete periods of "
    "worsening, and it would be very unusual at 39. The stepwise course over eight months does not "
    "fit."],
   ["Sudden sensorineural hearing loss",
    "Sudden loss is unilateral and occurs over up to three days, then either recovers or does not. "
    "A bilateral fluctuating course over eight months is a different entity requiring different "
    "treatment."],
   ["Meniere disease",
    "Meniere gives episodic vertigo with fluctuating low-frequency loss, tinnitus and fullness, "
    "usually starting unilaterally. There is no vertigo here and the pattern of progression is "
    "stepwise rather than attack-based."]],
  "diagnosis", D, 64),

Q("Hereditary sensorineural loss", IO,
  "A newborn fails the hearing screen. Examination shows a white forelock, widely spaced medial "
  "canthi and heterochromia of the irises.",
  [["Waardenburg syndrome",
    "Correct. Waardenburg is a neural crest disorder, and the neural crest contributes both to the "
    "melanocytes of the skin, hair and iris and to the stria vascularis of the cochlea. That shared "
    "origin is why pigmentary abnormalities and sensorineural deafness appear together, and it is "
    "the syndrome the described features define."],
   ["Alport syndrome",
    "Alport combines sensorineural hearing loss with progressive glomerulonephritis and ocular "
    "changes, from a defect in type IV collagen. It does not produce a white forelock or "
    "heterochromia, and the renal disease appears later."],
   ["Usher syndrome",
    "Usher pairs congenital sensorineural deafness with retinitis pigmentosa, so the associated "
    "problem is progressive visual field loss rather than pigmentary changes of the hair and iris."],
   ["Nonsyndromic hereditary hearing loss",
    "Most hereditary deafness is nonsyndromic, which makes this the statistically likelier category "
    "in general. It is defined by the ABSENCE of associated features, and three distinctive features "
    "are described here."]],
  "diagnosis", D, 62),

Q("Sudden sensorineural hearing loss", IO,
  "A 44-year-old man develops unilateral hearing loss over two days with no identifiable cause "
  "after investigation. He asks what the diagnosis actually means.",
  [["It is a syndrome rather than a disease, and a cause is often never found",
    "Correct. Sudden sensorineural hearing loss describes a pattern of presentation, not a single "
    "pathology, and in most cases no cause is identified despite investigation. The clinical "
    "importance is that the differential includes treatable and dangerous entries, which is why it "
    "prompts urgent referral and imaging rather than a wait to see what happens."],
   ["It is always caused by a viral infection of the cochlea",
    "A viral aetiology is one hypothesis among several, alongside vascular, autoimmune and "
    "retrocochlear causes. Asserting a single cause overstates what is known and could stop the "
    "search for a schwannoma."],
   ["It reliably resolves completely without treatment",
    "A proportion recover spontaneously, but many do not, and the chance of recovery falls the "
    "longer treatment is delayed. Framing it as self-limiting removes the urgency that governs "
    "management."],
   ["It indicates a conductive problem that surgery can correct",
    "Sensorineural means the lesion is in the cochlea or the nerve, not in the conducting mechanism. "
    "There is no mechanical obstruction to operate on, which is what separates it from otosclerosis "
    "or an effusion."]],
  "mechanism", D, 68),

Q("Benign paroxysmal positional vertigo", IO,
  "A 58-year-old woman with a positive right Dix-Hallpike test asks how her vertigo will be "
  "treated.",
  [["The Epley manoeuvre",
    "Correct. The vertigo is caused by otoconia that have escaped the utricle into a semicircular "
    "canal, where they move with gravity and stimulate the canal inappropriately. The Epley is a "
    "sequence of head positions that rolls those particles back out of the canal into the vestibule, "
    "treating the mechanical cause rather than suppressing the symptom."],
   ["Long-term vestibular suppressant medication",
    "Suppressants blunt the sensation but leave the otoconia where they are, and prolonged use "
    "actually impairs the central compensation that helps recovery. They have a role for acute "
    "nausea, not as the treatment."],
   ["A low-salt diet",
    "Salt restriction is the dietary measure for Meniere disease, because that condition involves "
    "endolymph volume. Positional vertigo is a particle problem and is unaffected by sodium "
    "intake."],
   ["Surgical labyrinthectomy",
    "Destroying the labyrinth is a last resort for intractable vertigo with no useful hearing in "
    "that ear. Applying it to a condition that a bedside manoeuvre resolves would be grossly "
    "disproportionate."]],
  "treatment", D, 89),

Q("Tinnitus", IO,
  "A 63-year-old man has bilateral high-pitched ringing in both ears, present for two years, "
  "alongside a symmetrical high-frequency sensorineural loss. There is no pulsatility and no "
  "vertigo.",
  [["Reassurance, hearing aids and sound therapy",
    "Correct. Bilateral non-pulsatile tinnitus accompanying a symmetrical sensorineural loss is the "
    "common form, generated centrally as the brain compensates for reduced input. Because the driver "
    "is the hearing loss, amplification often reduces the tinnitus, and sound therapy works by "
    "reducing the contrast between the tinnitus and silence."],
   ["Urgent magnetic resonance imaging of the internal auditory canals",
    "Imaging is directed by red flags, which here would be unilaterality or pulsatility. A "
    "symmetrical bilateral sound with matching symmetrical hearing loss lacks the asymmetry that "
    "suggests a nerve lesion."],
   ["Angiography to look for a vascular cause",
    "Vascular investigation follows PULSATILE tinnitus, where the sound is synchronous with the "
    "pulse and suggests turbulent flow or a glomus tumour. This sound has no pulsatile quality."],
   ["A trial of vestibular suppressants",
    "Vestibular suppressants treat vertigo, and this patient has none. They do nothing for tinnitus "
    "and carry sedation and fall risk in an older patient."]],
  "treatment", D, 41),
]
