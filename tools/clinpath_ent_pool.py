# -*- coding: utf-8 -*-
"""Clinical Pathophysiology I -- ENT (Lecture 5), question pool.

Deck: "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx", 28 slides.
Guest lecturer: Bill Webster, MMS, PA-C. Recording: clinpath-l5-ent-2026-09-02.

MECHANISM ONLY, NEVER MANAGEMENT. [[clin_path_exam_spec]] draws that line to
keep this course distinct from CMS I, and this deck tests it: slide 23's
epistaxis table has a management column -- direct pressure, oxymetazoline,
balloon packing, embolisation -- and not one question is built on it. The
vascular source and the aetiology are pathophysiology; what you do about it is
the other course's.

NO VIGNETTES, also per the spec.

SLIDE 17 IS WRONG AND HE SAID SO. It gives labyrinthitis "episodic vertigo".
At [33:14] he corrects it live: "this is not episodic vertigo. I don't know, I
did write that. So this is not episodic. This is CONTINUOUS vertigo." And
again at [34:17]. The pool teaches continuous and says the slide disagrees.

VERTIGO IS WEIGHTED. At [25:28]: "on my board exams, a third of my neurology
questions were vertigo related. So know this, know these things."

Correct answer authored FIRST; clinpath_ent_partition.py rotates it.
"""

O1 = "Objective 1 — Review the anatomy of the ear, nose, neck and throat system."
O2 = "Objective 2 — Review the ear, nose, neck, and throat pathology."
O3 = "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat."
O4 = "Objective 4 — Differentiate the pathogenesis of vertigo and dizziness."
O5 = "Objective 5 — Compare and contrast the pathophysiological processes of hearing deficits."
D = "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx"

QUESTIONS = [

{"topic": "Auditory transduction", "io": O3, "slot": "mechanism",
 "q": "In the organ of Corti, what physically opens the tip-link channels on the hair cells?",
 "opts": [
  ["Shearing of the stereocilia against the tectorial membrane",
   "Correct. Basilar membrane displacement bends the stereocilia against the rigid tectorial membrane, and that mechanical deflection is what opens the channels. Everything upstream exists to produce that shear."],
  ["Direct pressure of endolymph on the hair cell body",
   "Endolymph displacement moves the membrane, but the channel opens because the cilia are bent against a rigid structure, not from fluid pressure on the cell."],
  ["Glutamate binding to the hair cell",
   "Glutamate is released BY the hair cell onto cranial nerve VIII fibres after depolarisation. It is the output, not the trigger."],
  ["Stapes vibration transmitted directly to the hair cells",
   "The stapes vibrates the oval window, which starts pressure waves in the scala vestibuli. Several steps separate that from the cilia."]],
 "c": 0, "cite": "%s, Slide 5" % D},

{"topic": "Auditory transduction", "io": O3, "slot": "mechanism",
 "q": "Depolarisation of the cochlear hair cell comes from an ion influx. Through what, and out of which fluid?",
 "opts": [
  ["Influx from the endolymph through the tip-link channels",
   "Correct. The endolymph is the reservoir, and opening the tip-link channels lets ions rush in. Depolarisation then opens voltage-gated channels and glutamate is released onto cranial nerve VIII."],
  ["Efflux into the perilymph through voltage-gated channels",
   "Voltage-gated channels open AFTER depolarisation and drive transmitter release; they are not what depolarises the cell."],
  ["Influx from the perilymph across the basilar membrane",
   "The ionic gradient that matters is between endolymph and the hair cell, not across the basilar membrane."],
  ["Release from intracellular stores after glutamate binding",
   "Glutamate is what the hair cell RELEASES onto cranial nerve VIII after it depolarises. It is the output of the cell, not a signal arriving at it."]],
 "c": 0, "cite": "%s, Slide 5" % D},

{"topic": "Hearing loss patterns", "io": O5, "slot": "mechanism",
 "q": "What is the defect in conductive hearing loss, and where does it sit?",
 "opts": [
  ["Defective sound transmission, in the external or middle ear",
   "Correct. The apparatus that carries sound inward has failed; the cochlea and nerve are intact. That anatomical split is what the tuning fork tests are detecting."],
  ["Destruction of hair cells or auditory nerve fibres, in the inner ear",
   "That is sensorineural loss — the sensing apparatus rather than the conducting apparatus."],
  ["Failure of glutamate release at cranial nerve VIII",
   "A neural failure, so sensorineural by site even though the mechanism is synaptic."],
  ["Central processing failure in the auditory cortex",
   "Central pathways fall under the sensorineural heading in this comparison, not the conductive one."]],
 "c": 0, "cite": "%s, Slide 7" % D},

{"topic": "Hearing loss patterns", "io": O5, "slot": "mechanism",
 "q": "In conductive hearing loss, which way does Weber lateralise and what does Rinne show?",
 "opts": [
  ["Weber to the AFFECTED ear; Rinne shows bone conduction greater than air",
   "Correct. The blocked ear is not receiving competing air-borne sound, so bone-conducted sound is heard more loudly in it — and with the conducting chain impaired, bone beats air on Rinne."],
  ["Weber to the UNAFFECTED ear; Rinne shows air conduction greater than bone",
   "That is the sensorineural pattern: the damaged cochlea cannot hear either route well, so Weber goes to the better ear and Rinne keeps its normal ratio."],
  ["Weber to the affected ear; Rinne shows air conduction greater than bone",
   "The Weber is right but Rinne is not — a normal air-over-bone ratio means the conducting apparatus is working."],
  ["Weber is equal; Rinne shows bone greater than air bilaterally",
   "An equal Weber implies symmetry, which a unilateral conductive loss does not have."]],
 "c": 0, "cite": "%s, Slide 7" % D},

{"topic": "Hearing loss patterns", "io": O5, "slot": "mechanism",
 "q": "Which set of causes belongs to sensorineural rather than conductive loss?",
 "opts": [
  ["Presbycusis, ototoxic drugs, noise trauma and acoustic neuroma",
   "Correct. All four damage the cochlea or the nerve. Note acoustic neuroma sits here because cranial nerve VIII is part of the sensorineural pathway even though the tumour is outside the cochlea."],
  ["Cerumen impaction, otosclerosis, otitis media and tympanic membrane perforation",
   "All four are conductive — they obstruct, load, stiffen or interrupt the sound-conducting apparatus."],
  ["Cholesteatoma, exostoses, foreign body and ossicular necrosis",
   "Again all conductive, and they map onto the four core mechanisms of conductive loss."],
  ["Eustachian tube dysfunction, middle ear effusion and stapes fixation",
   "All three are conductive: effusion loads the drum with mass, and stapes fixation stiffens the chain. None involves the cochlea or the nerve."]],
 "c": 0, "cite": "%s, Slide 7" % D},

{"topic": "Conductive loss mechanisms", "io": O5, "slot": "mechanism",
 "q": "Cerumen impaction, foreign bodies and canal exostoses all cause conductive loss by which of the four core mechanisms?",
 "opts": [
  ["Obstruction",
   "Correct. A physical blockage stops sound penetrating down the canal. It is the first of four mechanisms, and the only one that acts before the sound reaches the drum."],
  ["Mass loading",
   "That is fluid or tissue weight damping movement of the drum or ossicles — middle ear effusion, cholesteatoma."],
  ["Stiffness effect",
   "That is impaired mobility of the ossicles or drum, of which otosclerosis is the example."],
  ["Discontinuity",
   "That is physical disruption of the ossicular chain, from temporal bone fracture or ossicular necrosis."]],
 "c": 0, "cite": "%s, Slide 9" % D},

{"topic": "Conductive loss mechanisms", "io": O5, "slot": "mechanism",
 "q": "Middle ear effusion and cholesteatoma impair conduction by which mechanism?",
 "opts": [
  ["Mass loading",
   "Correct. Both add fluid or tissue weight that damps movement of the tympanic membrane and ossicles. The chain is intact and mobile in principle, but it is carrying extra mass."],
  ["Obstruction",
   "Obstruction blocks the canal before the drum — wax, foreign bodies, exostoses."],
  ["Stiffness effect",
   "Stiffness is fixation rather than added weight; otosclerosis is the example."],
  ["Discontinuity",
   "Discontinuity means the chain is physically broken, which neither of these does."]],
 "c": 0, "cite": "%s, Slide 9" % D},

{"topic": "Conductive loss mechanisms", "io": O5, "slot": "mechanism",
 "q": "A temporal bone fracture causes conductive loss by which mechanism?",
 "opts": [
  ["Discontinuity of the ossicular chain",
   "Correct. The chain is physically disrupted so the wave cannot be conducted across it. Ossicular necrosis produces the same end result by erosion rather than trauma."],
  ["Stiffness of the ossicular chain",
   "Stiffness is the opposite problem — the chain is intact but cannot move."],
  ["Mass loading of the tympanic membrane",
   "Mass loading requires added fluid or tissue weight damping the chain. A fracture removes continuity rather than adding weight."],
  ["Obstruction of the external canal",
   "Obstruction blocks the external canal before the drum. A temporal bone fracture acts deeper, on the ossicular chain itself."]],
 "c": 0, "cite": "%s, Slide 9" % D},

{"topic": "Otosclerosis", "io": O3, "slot": "mechanism",
 "q": "What is the bone remodelling sequence in otosclerosis?",
 "opts": [
  ["Osteoclastic resorption, then spongy osteoid replacement",
   "Correct. Bone is removed and replaced by soft vascular osteoid around the otic capsule and stapes footplate. The remodelled bone then fixes the footplate."],
  ["Osteoblastic overgrowth of dense cortical bone without resorption",
   "The sequence begins with resorption; it is remodelling rather than simple overgrowth."],
  ["Demineralisation of the ossicles from chronic inflammation",
   "Not the described mechanism, and otosclerosis is not primarily inflammatory."],
  ["Fibrous scarring of the round window membrane",
   "The lesion is at the oval window and the stapes footplate, and it is bone rather than scar."]],
 "c": 0, "cite": "%s, Slide 10" % D},

{"topic": "Otosclerosis", "io": O3, "slot": "mechanism",
 "q": "Which single event in otosclerosis produces the hearing loss?",
 "opts": [
  ["Ankylosis of the stapes footplate",
   "Correct. Once the footplate is fixed it cannot transfer mechanical vibration into the cochlear fluid, and conduction fails progressively. Fixation is the whole lesion."],
  ["Erosion of the incus by the remodelled bone",
   "Discontinuity would be a different mechanism; otosclerosis works by fixation."],
  ["Hair cell loss at the cochlear base",
   "That is noise or ototoxic damage, and it would give sensorineural loss."],
  ["Accumulation of endolymph in the scala media",
   "Fluid accumulating in the scala media is endolymphatic hydrops in Meniere disease, a sensorineural and vestibular problem rather than a conductive one."]],
 "c": 0, "cite": "%s, Slide 10" % D},

{"topic": "Otosclerosis", "io": O2, "slot": "epidemiology",
 "q": "What is the demographic and inheritance pattern of otosclerosis?",
 "opts": [
  ["Young-to-middle-aged females, accelerated by pregnancy; 50% autosomal dominant",
   "Correct. The pregnancy acceleration is the memorable part, and variable penetrance explains why the family history is often incomplete."],
  ["Commonest in older males, with no hereditary component",
   "Both halves are wrong: the peak is younger and female, and half of cases are autosomal dominant."],
  ["Commonest in children, autosomal recessive",
   "Neither half matches: otosclerosis peaks in young to middle-aged women, and half of cases are autosomal dominant rather than recessive."],
  ["Commonest in young females but entirely sporadic",
   "The demographic is right, but it is not sporadic &mdash; 50 per cent is autosomal dominant, with variable penetrance hiding the family history."]],
 "c": 0, "cite": "%s, Slide 10" % D},

{"topic": "Ototoxicity", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "How do gentamicin and tobramycin damage hearing, and which frequencies go first?",
 "opts": [
  ["Reactive oxygen species destroy outer hair cells from the base, so high pitches go first",
   "Correct. The base of the cochlea encodes high frequencies, so basal damage shows as high-frequency loss. The mechanism is oxidative injury, not a direct toxic binding."],
  ["They cross-link DNA in the stria vascularis, disturbing endolymph ion homeostasis",
   "That is the platinum chemotherapy mechanism — cisplatin and carboplatin."],
  ["They alter the stria vascularis potential reversibly",
   "That is the loop diuretic effect, and reversibility is what separates it from the aminoglycosides."],
  ["They inhibit the prestin motor protein in outer hair cells",
   "Inhibiting prestin in outer hair cells is the salicylate mechanism, and its hallmark is tinnitus rather than permanent threshold loss."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 11"},

{"topic": "Ototoxicity", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "How do cisplatin and carboplatin cause permanent bilateral sensorineural loss?",
 "opts": [
  ["They cross-link DNA in stria vascularis cells, compromising endolymph ion homeostasis",
   "Correct. The stria vascularis maintains the ionic composition of endolymph, and without that gradient transduction fails. Damage there is permanent and bilateral."],
  ["They generate reactive oxygen species that destroy outer hair cells at the cochlear base",
   "Reactive oxygen species destroying outer hair cells from the cochlear base is the aminoglycoside mechanism, and it takes the high frequencies first."],
  ["They inhibit prestin in outer hair cells",
   "That is salicylate, and the effect is tinnitus rather than permanent loss."],
  ["They fix the stapes footplate in the oval window",
   "That is otosclerosis, a conductive lesion with no drug involvement."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 11"},

{"topic": "Ototoxicity", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "Which two ototoxic effects are described as reversible or symptom-limited rather than permanent?",
 "opts": [
  ["Furosemide on the strial potential; salicylate on prestin",
   "Correct. The loop diuretic effect on the strial potential is reversible, and the salicylate effect on the outer hair cell motor protein produces tinnitus. Neither destroys the cells outright."],
  ["Gentamicin and tobramycin damage",
   "Aminoglycoside destruction of outer hair cells is the permanent one."],
  ["Cisplatin and carboplatin damage",
   "Platinum agents cause bilateral permanent sensorineural loss."],
  ["Noise trauma and presbycusis",
   "Both are irreversible — noise causes stereocilia degeneration and hair cell apoptosis."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 11"},

{"topic": "Noise trauma", "io": "Objective 5 — Compare and contrast the pathophysiological processes of hearing deficits.", "slot": "mechanism",
 "q": "Above what sound level does long-term chronic exposure cause irreversible cochlear damage, and what is the cellular change?",
 "opts": [
  ["Above 85 decibels, by stereocilia degeneration and apoptosis",
   "Correct. Both words matter: degeneration of the stereocilia and programmed death of the hair cells. Neither regenerates, which is why the loss is permanent."],
  ["Above 85 decibels, causing reversible stereocilia fatigue",
   "The threshold is right but the change is not reversible — apoptosis is cell death."],
  ["Above 120 decibels, causing tympanic membrane rupture",
   "That is acute blast injury, a conductive problem, and a different threshold."],
  ["Above 60 decibels, causing endolymphatic hydrops",
   "Endolymphatic hydrops is the lesion of Meniere disease, caused by defective resorption rather than by sound exposure at any level."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 8"},

{"topic": "Presbycusis", "io": "Objective 5 — Compare and contrast the pathophysiological processes of hearing deficits.", "slot": "mechanism",
 "q": "What is the characteristic frequency pattern of presbycusis, and why does it impair conversation?",
 "opts": [
  ["High frequencies go first, taking the speech consonants",
   "Correct. Consonants such as /s/, /f/ and /t/ are high-frequency sounds and carry most of the discriminating information in speech, which is why voices become hard to make out in a noisy room while still being audible."],
  ["Low frequencies go first, taking the vowels",
   "That is the Meniere pattern — fluctuating low-tone loss — and it is not age-related."],
  ["All frequencies fall equally",
   "A flat loss is not what presbycusis produces, and it would not preferentially damage discrimination."],
  ["Only frequencies above the speech range are affected",
   "If the speech range were spared there would be no discrimination problem."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 12"},

{"topic": "Otitis media", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "What is the sequence by which Eustachian tube dysfunction creates negative middle ear pressure?",
 "opts": [
  ["The tube fails to open, so the mucosa absorbs the gases",
   "Correct. The middle ear is an air-filled space; if it is not re-ventilated, the mucosa absorbs the gases and the pressure falls. That negative pressure is the start of the otitis media sequence."],
  ["Mucus production increases faster than the tube can drain it",
   "Fluid accumulates later, but the initiating step described is gas absorption after failure to ventilate."],
  ["Bacterial infection erodes the tube lining and opens it permanently",
   "A patulous tube is a different problem; here the failure is that it does not open."],
  ["The tympanic membrane becomes stiff and pulls the ossicles inward",
   "Retraction is a consequence of the negative pressure, not its cause."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 13"},

{"topic": "Otitis media", "io": "Objective 2 — Review the ear, nose, neck, and throat pathology.", "slot": "microbiology",
 "q": "Which organisms most commonly cause bacterial otitis media?",
 "opts": [
  ["Streptococcus pneumoniae, Haemophilus influenzae, Moraxella catarrhalis",
   "Correct. The classic middle ear trio. Viral causes are respiratory syncytial virus, rhinovirus, influenza and adenovirus."],
  ["Pseudomonas aeruginosa and Staphylococcus aureus",
   "Those are the otitis EXTERNA organisms, accounting for 80 to 90 per cent of that condition."],
  ["Aspergillus niger and Candida albicans",
   "Those are the fungal otitis externa organisms, often after prolonged antibiotics or humid conditions."],
  ["Group A Streptococcus alone",
   "That is the usual bacterial cause of tonsillitis, not of otitis media."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 13"},

{"topic": "Otitis externa", "io": "Objective 2 — Review the ear, nose, neck, and throat pathology.", "slot": "microbiology",
 "q": "Which organisms cause 80 to 90 per cent of otitis externa, and what predisposes to the fungal form?",
 "opts": [
  ["Pseudomonas aeruginosa and Staphylococcus aureus; fungal after antibiotics",
   "Correct. The bacterial pair dominate, and Aspergillus niger or Candida albicans take over when the bacterial flora has been suppressed or the canal stays wet."],
  ["Streptococcus pneumoniae and Haemophilus influenzae; fungal disease follows swimming",
   "Those two are middle ear organisms, and swimming predisposes to bacterial rather than specifically fungal disease."],
  ["Moraxella catarrhalis alone; fungal disease follows trauma",
   "Moraxella catarrhalis sits on the otitis MEDIA list alongside Streptococcus pneumoniae and Haemophilus influenzae, not in the external canal."],
  ["Respiratory syncytial virus and rhinovirus; fungal disease follows steroid use",
   "Respiratory syncytial virus and rhinovirus are viral causes of otitis MEDIA; they are not what colonises an external canal."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 13"},

{"topic": "Equilibrium", "io": "Objective 1 — Review the anatomy of the ear, nose, neck and throat system.", "slot": "mechanism",
 "q": "What do the semicircular canals detect, and how?",
 "opts": [
  ["Rotational acceleration, by endolymph bending the cupula",
   "Correct. Three loops in the sagittal, coronal and transverse planes. The fluid lags behind the head, the gelatinous cupula bends, and the hair cell stereocilia inside it are stimulated."],
  ["Linear acceleration and gravitational position, via the otoliths",
   "That is the utricle and saccule — the otolith organs — which handle static and linear balance."],
  ["Sound frequency, via the basilar membrane",
   "That is the cochlea, a different part of the inner ear entirely."],
  ["Middle ear pressure, via the Eustachian tube",
   "The Eustachian tube equalises middle ear pressure. That is a conduction function and has nothing to do with detecting head movement."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 14"},

{"topic": "Equilibrium", "io": "Objective 1 — Review the anatomy of the ear, nose, neck and throat system.", "slot": "mechanism",
 "q": "Which structures detect linear acceleration and gravitational position?",
 "opts": [
  ["The otolith organs",
   "Correct. They handle static and linear balance, while the semicircular canals handle rotation. The two systems together give the brain a complete picture of head position and movement."],
  ["The three semicircular canals",
   "The semicircular canals detect ROTATIONAL acceleration through cupula deflection. Linear and gravitational sensing belongs to the otoliths."],
  ["The cupula and ampulla",
   "Those are the sensing apparatus inside the semicircular canals, so again rotational."],
  ["The organ of Corti",
   "The organ of Corti transduces sound into neural signals. It is the hearing apparatus and plays no part in equilibrium."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 14"},

{"topic": "Vertigo vs dizziness", "io": "Objective 4 — Differentiate the pathogenesis of vertigo and dizziness.", "slot": "mechanism",
 "q": "What defines vertigo, and what distinguishes it from dizziness?",
 "opts": [
  ["A hallucination of motion, with NO syncope",
   "Correct. Asymmetry between the two sides is the mechanism, and the absence of syncope is the separator. Dizziness or lightheadedness is a non-vestibular sensation of impending faint."],
  ["A sensation of impending faint from cerebral hypoperfusion",
   "That is dizziness or presyncope, driven by hypoperfusion, orthostatic hypotension or metabolic imbalance."],
  ["Any unsteadiness on standing",
   "Unsteadiness alone does not distinguish the two; the hallucination of motion does."],
  ["Loss of consciousness preceded by spinning",
   "Vertigo explicitly involves NO syncope. Loss of consciousness points away from a vestibular cause and toward cerebral hypoperfusion."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 15"},

{"topic": "Vertigo vs dizziness", "io": "Objective 4 — Differentiate the pathogenesis of vertigo and dizziness.", "slot": "mechanism",
 "q": "What drives dizziness or lightheadedness, as distinct from vertigo?",
 "opts": [
  ["Cerebral hypoperfusion or metabolic imbalance",
   "Correct. None of these is vestibular, which is why the sensation is of impending faint rather than of the room moving. Getting this distinction right is the first branch point in the whole workup."],
  ["Asymmetrical input between the two vestibular apparatus",
   "Asymmetrical vestibular input is the mechanism of vertigo itself, which is the thing dizziness has to be distinguished FROM."],
  ["Dislodged otoconia in the semicircular canals",
   "That is benign paroxysmal positional vertigo, a vestibular cause."],
  ["Endolymphatic hydrops",
   "Endolymphatic hydrops is Meniere disease, which is vestibular &mdash; so it produces vertigo rather than the presyncopal sensation of dizziness."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 15"},

{"topic": "Vertigo vs dizziness", "io": "Objective 4 — Differentiate the pathogenesis of vertigo and dizziness.", "slot": "mechanism",
 "q": "Which features mark vertigo as PERIPHERAL rather than central?",
 "opts": [
  ["Sudden onset, horizontal or rotational nystagmus, fatigable, suppressed by visual fixation",
   "Correct. All four point at the inner ear or cranial nerve VIII. Suppression by visual fixation is the one most easily tested at the bedside."],
  ["Gradual onset, vertical nystagmus, non-suppressible, with neurological deficits",
   "Gradual onset, vertical non-suppressible nystagmus and neurological deficits describe CENTRAL vertigo from the brainstem or cerebellum."],
  ["Gradual onset with hearing loss and tinnitus",
   "Hearing loss can accompany peripheral causes, but gradual onset and the other features listed describe central disease."],
  ["Absence of nystagmus entirely",
   "Vertigo frequently presents WITH nystagmus and ataxia; its absence does not localise."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 15"},

{"topic": "Vertigo vs dizziness", "io": "Objective 4 — Differentiate the pathogenesis of vertigo and dizziness.", "slot": "mechanism",
 "q": "Which causes are listed as CENTRAL vertigo?",
 "opts": [
  ["Brainstem stroke, multiple sclerosis and cerebellar tumour",
   "Correct. All involve the brainstem or cerebellum, which is why the nystagmus can be vertical and is not suppressed by fixation, and why other neurological signs appear."],
  ["Benign paroxysmal positional vertigo, Meniere disease and labyrinthitis",
   "Those are the peripheral causes, along with vestibular neuritis."],
  ["Otosclerosis and cerumen impaction",
   "Otosclerosis and cerumen impaction are conductive hearing problems. Neither involves the vestibular apparatus, so neither causes vertigo at all."],
  ["Presbycusis and noise trauma",
   "Both are sensorineural hearing loss without a vestibular component."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 15"},

{"topic": "Meniere disease", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "What is the mechanism of Meniere disease?",
 "opts": [
  ["Defective endolymph resorption causing hydrops, ballooning the scala media until micro-ruptures occur",
   "Correct. Endolymphatic hydrops is the lesion: fluid accumulates because it is not resorbed, the membranous labyrinth distends, and micro-ruptures follow. The episodic nature follows from that cycle."],
  ["Inflammatory swelling and vascular congestion of the labyrinth after a viral infection",
   "That is labyrinthitis, and the recent upper respiratory infection is what separates the two clinically."],
  ["Dislodged otoconia floating in the semicircular canals",
   "Otoconia loose in the semicircular canals is benign paroxysmal positional vertigo, which produces brief positional attacks and spares hearing."],
  ["Demyelination of the vestibular nerve",
   "Demyelination of the vestibular nerve is not one of the named mechanisms. The central causes given are brainstem stroke, multiple sclerosis and cerebellar tumour."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 16"},

{"topic": "Meniere disease", "io": "Objective 2 — Review the ear, nose, neck, and throat pathology.", "slot": "clinical pattern",
 "q": "What is the classic symptom tetrad of Meniere disease?",
 "opts": [
  ["Episodic vertigo for hours, low-frequency tinnitus, low-tone loss, aural fullness",
   "Correct. All four, and the LOW-frequency emphasis is what distinguishes the hearing loss from presbycusis or noise damage, which take the high frequencies first."],
  ["Continuous vertigo lasting days, unilateral tinnitus, unilateral loss, and nystagmus",
   "That is labyrinthitis — and the duration is the main separator."],
  ["Vertigo lasting under a minute on head movement, with no hearing loss",
   "Otoconia loose in the semicircular canals is benign paroxysmal positional vertigo, which produces brief positional attacks and spares hearing."],
  ["High-frequency hearing loss with tinnitus and no vertigo",
   "That is closer to presbycusis or noise trauma, neither of which is vestibular."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 16"},

{"topic": "Labyrinthitis", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "What is the mechanism of labyrinthitis, and why does it impair hearing AND balance together?",
 "opts": [
  ["Inflammation across both the semicircular canals and the cochlea",
   "Correct. The inflammation does not respect the boundary between the vestibular apparatus and the organ of Corti, so both fail at once. That simultaneous involvement is what names it otitis interna."],
  ["Defective endolymph resorption ballooning the scala media",
   "That is the hydrops of Meniere disease, and it does not begin with inflammation."],
  ["Dislodged otoconia striking structures in the endolymph",
   "That is benign paroxysmal positional vertigo, which spares hearing entirely."],
  ["Fixation of the stapes footplate",
   "Otosclerosis, a conductive lesion with no vestibular component."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 17"},

{"topic": "Labyrinthitis", "io": "Objective 4 — Differentiate the pathogenesis of vertigo and dizziness.", "slot": "clinical pattern",
 "q": "Is the vertigo of labyrinthitis episodic or continuous, and how long does it run?",
 "opts": [
  ["Continuous, over days, improving across weeks",
   "Correct. Someone comes in saying the room has been spinning for three days, not that it comes and goes. Continuous vertigo that slowly settles over weeks is the labyrinthitis pattern, because the body is resolving an inflammatory process."],
  ["Episodic, with attacks lasting several hours",
   "That is Meniere disease. The hours-long discrete attack is its signature, and mixing the two up is the error this question exists to catch."],
  ["Episodic, with attacks lasting under a minute",
   "That is benign paroxysmal positional vertigo, provoked by head position."],
  ["Continuous, permanent and non-improving",
   "It does improve, because the body resolves the inflammation; recovery just takes weeks."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 17 (slide says episodic; corrected in lecture)"},

{"topic": "Labyrinthitis", "io": "Objective 2 — Review the ear, nose, neck, and throat pathology.", "slot": "clinical pattern",
 "q": "Which history most separates labyrinthitis from Meniere disease?",
 "opts": [
  ["A recent upper respiratory infection",
   "Correct. Labyrinthitis usually follows a viral infection, so a cold last week points hard at it; someone who has not had a cold in years is likelier to have Meniere disease. Both can be unilateral, so laterality does not separate them."],
  ["Unilateral rather than bilateral symptoms",
   "Both are usually unilateral, so this is explicitly not a discriminator."],
  ["The presence of tinnitus",
   "Both labyrinthitis and Meniere disease produce tinnitus, so its presence tells you nothing about which one you are looking at."],
  ["The presence of sensorineural hearing loss",
   "Both cause it. The duration of vertigo and the preceding infection are what differ."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 17"},

{"topic": "Labyrinthitis", "io": "Objective 2 — Review the ear, nose, neck, and throat pathology.", "slot": "clinical pattern",
 "q": "Which way does the nystagmus of labyrinthitis beat?",
 "opts": [
  ["Horizontal-rotary, with the fast phase beating AWAY from the affected side",
   "Correct. The damaged side is under-firing, so the slow drift is toward it and the corrective fast phase beats away. Severe postural instability, gait ataxia and nausea come with it."],
  ["Horizontal-rotary, with the fast phase beating TOWARD the affected side",
   "The direction is reversed; the fast phase beats away from the lesion."],
  ["Vertical and non-suppressible",
   "Vertical nystagmus is a central feature, and labyrinthitis is peripheral."],
  ["Absent, because hearing rather than balance is affected",
   "Labyrinthitis impairs both, and nystagmus is a listed feature."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 17"},

{"topic": "BPPV", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "What is canalithiasis?",
 "opts": [
  ["Dislodged otoconia floating free in the semicircular canals",
   "Correct. The crystals normally sit in the utricle. Once loose in the endolymph they strike structures and generate a false sensation of motion. Why they dislodge is not the examinable part &mdash; that they can is."],
  ["Calcification of the stapes footplate",
   "Calcification fixing the stapes footplate is otosclerosis, a conductive lesion of the middle ear with no vestibular component."],
  ["Accumulation of endolymph in the membranous labyrinth",
   "Endolymph accumulating in the membranous labyrinth is the hydrops of Meniere disease, which gives hours-long attacks with hearing loss."],
  ["Inflammatory debris within the cochlea after infection",
   "Closer to labyrinthitis, and it would impair hearing, which this does not."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 18"},

{"topic": "BPPV", "io": "Objective 4 — Differentiate the pathogenesis of vertigo and dizziness.", "slot": "clinical pattern",
 "q": "Which feature of benign paroxysmal positional vertigo separates it most cleanly from the other peripheral causes?",
 "opts": [
  ["There is NO hearing loss",
   "Correct. Meniere disease and labyrinthitis both take hearing with them; this does not, because the otoconia are a vestibular problem that never touches the cochlea. Attacks also last under a minute and follow head position."],
  ["The vertigo lasts several hours",
   "Attacks lasting several hours describe Meniere disease. Positional vertigo attacks are measured in seconds, usually under a minute."],
  ["It follows a viral upper respiratory infection",
   "A preceding viral upper respiratory infection points at labyrinthitis, which also takes the hearing with it &mdash; unlike positional vertigo."],
  ["It produces aural fullness",
   "Aural fullness is the fourth element of the Meniere tetrad. Positional vertigo produces no fullness and no hearing change at all."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 18"},

{"topic": "Rhinosinusitis", "io": "Objective 2 — Review the ear, nose, neck, and throat pathology.", "slot": "classification",
 "q": "How are acute and chronic rhinosinusitis defined by duration, and what commonly accompanies the chronic form?",
 "opts": [
  ["Acute under 4 weeks; chronic beyond 12 weeks despite therapy, often with nasal polyps",
   "Correct. The two thresholds are the definition. Acute disease is usually viral &mdash; rhinovirus or influenza &mdash; with secondary bacterial infection by Streptococcus pneumoniae or Haemophilus influenzae."],
  ["Acute under 2 weeks; chronic beyond 6 weeks, often with septal deviation",
   "Neither threshold matches, and septal deviation is a separate anatomical problem."],
  ["Acute under 12 weeks; chronic beyond 6 months, often with turbinate hypertrophy",
   "The thresholds are wrong: acute rhinosinusitis is under 4 weeks and chronic is beyond 12 weeks despite therapy."],
  ["Acute under 4 weeks; chronic beyond 12 weeks, usually with no mucosal change",
   "The durations are right but chronic disease often comes WITH polyps rather than without change."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 20"},

{"topic": "Allergic rhinitis", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "What kind of immune reaction is allergic rhinitis, and what does it look like?",
 "opts": [
  ["IgE-mediated type 1 hypersensitivity, with CLEAR rhinorrhoea",
   "Correct. Type 1, immediate, IgE-driven. The CLEAR discharge is what separates it at the bedside from bacterial sinusitis, which is purulent. Allergic shiners complete the picture."],
  ["IgG-mediated type 2 hypersensitivity with purulent rhinorrhoea",
   "Purulence points at bacterial infection, and the mechanism named is type 1."],
  ["Immune complex deposition, type 3 hypersensitivity",
   "Immune complex deposition is type 3 hypersensitivity. Allergic rhinitis is type 1, immediate and IgE-mediated on the nasal mucosa."],
  ["T cell mediated, type 4 delayed hypersensitivity",
   "Delayed hypersensitivity does not fit a reaction that starts within minutes of exposure."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 20"},

{"topic": "Nasal polyps", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "Which cytokines drive nasal polyp formation, and which cell floods the tissue?",
 "opts": [
  ["Interleukins 4, 5 and 13, with eosinophil influx",
   "Correct. This is type 2 inflammation, and naming the three interleukins is the molecular-mechanism objective in action. Polyps are benign, non-neoplastic oedematous masses from the sinus ostia or ethmoid air cells."],
  ["Interleukins 1, 6 and tumour necrosis factor, with neutrophil influx",
   "That is the type 1 or acute inflammatory profile, not the type 2 allergic one."],
  ["Interferon gamma, with lymphocyte influx",
   "A type 1 T-helper response, which is not what drives polyps."],
  ["Interleukin 17, with mast cell influx",
   "Interleukin 17 and mast cell influx are not the polyp pathway. Polyps are type 2 inflammation driven by interleukins 4, 5 and 13 with eosinophils."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 21"},

{"topic": "Turbinate hypertrophy", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "What enlarges the inferior turbinates, and what does rhinitis medicamentosa refer to?",
 "opts": [
  ["Venous engorgement, oedema or bony hypertrophy; decongestant rebound",
   "Correct. Three possible substrates, and the drug-induced one has its own name. It is the same rebound phenomenon that appears in ocular pharmacology &mdash; overuse of a vasoconstrictor leaving the tissue more congested than before."],
  ["Cartilage displacement off the midline; a congenital deformity",
   "That is deviated septum, an anatomical rather than mucosal problem."],
  ["Eosinophilic polyp formation; an allergic reaction",
   "Polyps are a separate entity with their own type 2 mechanism."],
  ["Bacterial infection of the turbinate bone; osteomyelitis",
   "Osteomyelitis of the turbinate bone is not among the triggers. Enlargement comes from venous engorgement, mucosal oedema or bony hypertrophy."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 21"},

{"topic": "Deviated septum", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "Which physical law explains why a small septal deviation causes disproportionate obstruction?",
 "opts": [
  ["Poiseuille's law",
   "Correct. Resistance rises with the fourth power of the radius, so a modest narrowing has an outsized effect on airflow. That is why a deviation that looks minor can produce persistent obstruction."],
  ["Fick's law of diffusion",
   "That governs diffusion across a membrane, which is a transport problem rather than a flow-resistance one."],
  ["Laplace's law",
   "That relates wall tension to radius and pressure, used for vessels and alveoli, not nasal airflow resistance."],
  ["Boyle's law",
   "A pressure-volume relationship for gases, not a resistance law."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 22"},

{"topic": "Deviated septum", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "Why does a deviated septum cause epistaxis and loss of smell?",
 "opts": [
  ["Turbulent airflow dries the mucosa; air misses the cribriform plate",
   "Correct. Two separate consequences of the same disturbed airflow: local drying with fragile vessel breakdown on one hand, and failure to deliver odorant to the superior nasal vault on the other."],
  ["Compression of the ethmoid arteries and the olfactory nerve",
   "Neither is a described mechanism; the problem is airflow, not compression."],
  ["Chronic infection eroding the septal vessels and olfactory epithelium",
   "Secondary bacterial rhinosinusitis can follow ostial blockage, but the epistaxis and anosmia are explained by airflow."],
  ["Autoimmune destruction of the septal cartilage",
   "Autoimmune destruction of septal cartilage is a different disease process; the consequences here all follow from disturbed airflow."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 22"},

{"topic": "Deviated septum", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "What happens to the wider nasal cavity opposite a septal deviation?",
 "opts": [
  ["Compensatory inferior turbinate hypertrophy",
   "Correct. The wide side does more of the work, so its turbinate enlarges to condition the extra airflow &mdash; which can then narrow the only good airway the patient had."],
  ["It atrophies from disuse",
   "The opposite happens. The wide side carries MORE airflow, so its turbinate enlarges to condition the extra volume rather than wasting away."],
  ["It develops polyps from the increased flow",
   "Polyps arise from type 2 inflammation, not from airflow volume."],
  ["Nothing changes; only the narrow side is affected",
   "The compensatory change on the wide side is specifically described."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 22"},

{"topic": "Epistaxis", "io": "Objective 1 — Review the anatomy of the ear, nose, neck and throat system.", "slot": "anatomy",
 "q": "Which vascular source accounts for anterior epistaxis, and what proportion of cases is that?",
 "opts": [
  ["Kiesselbach's plexus on the anterior septum, about 90 per cent",
   "Correct. Nine in ten nosebleeds are anterior and come from this plexus, which is why direct compression works so often. The posterior 10 per cent come from Woodruff's plexus on the posterolateral wall."],
  ["Woodruff's plexus on the posterolateral wall, about 90 per cent",
   "Woodruff's is the posterior source and accounts for the minority."],
  ["The sphenopalatine artery, about 50 per cent",
   "The sphenopalatine artery is not how this is divided. The two named vascular sources are Kiesselbach's plexus anteriorly and Woodruff's posteriorly."],
  ["The anterior ethmoidal artery, about 10 per cent",
   "The anterior ethmoidal artery is not one of the two named plexuses. Anterior bleeds come from Kiesselbach's and posterior from Woodruff's."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 23"},

{"topic": "Epistaxis", "io": "Objective 2 — Review the ear, nose, neck, and throat pathology.", "slot": "aetiology",
 "q": "How do the causes of anterior and posterior epistaxis differ?",
 "opts": [
  ["Anterior from local trauma and dry air; posterior from hypertension and anticoagulation",
   "Correct. Anterior bleeds are local and mechanical; posterior bleeds reflect a systemic vascular or clotting problem, which is also why they are more profuse and carry airway risk."],
  ["Anterior from hypertension and anticoagulation; posterior from digital trauma",
   "The two aetiologies are swapped. Digital trauma and dry air are anterior causes; hypertension and anticoagulation drive posterior bleeds."],
  ["Both are caused predominantly by anticoagulation",
   "Anticoagulation belongs with the posterior group; anterior bleeds are usually local."],
  ["Anterior from coagulopathy; posterior from low humidity",
   "Reversed again: coagulopathy belongs with posterior bleeding and low humidity with anterior mucosal drying."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 23"},

{"topic": "Vocal cord lesions", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "What are vocal cord nodules, and what causes them?",
 "opts": [
  ["Bilateral symmetrical calluses at the anterior third junction, from chronic phonotrauma",
   "Correct. Repeated slamming of the cords causes basement membrane hyalinisation &mdash; literally a callus. Bilateral and symmetrical, because both cords take the same repeated impact at the same point."],
  ["Unilateral pedunculated fluid-filled growths on the middle third, from a single severe strain",
   "That describes vocal cord POLYPS, and the unilateral-versus-bilateral split is the main distinction."],
  ["Bilateral wart-like exophytic lesions from viral infection",
   "Wart-like exophytic lesions from viral infection describe papillomatosis, which is a separate entity from the benign phonotrauma lesions."],
  ["Unilateral firm masses with cord fixation, from malignancy",
   "Fixation and a firm mass suggest carcinoma, not a benign lesion."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 25"},

{"topic": "Vocal cord lesions", "io": "Objective 3 — Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.", "slot": "mechanism",
 "q": "How do vocal cord polyps differ from nodules in site and pathogenesis?",
 "opts": [
  ["Unilateral, soft and pedunculated on the middle third, after one severe strain",
   "Correct. One event rather than chronic repetition, and the healing response is inflammatory rather than a callus. Site and laterality both differ from nodules."],
  ["Bilateral fibrous calluses from chronic phonotrauma",
   "Bilateral fibrous calluses from chronic phonotrauma are NODULES. Polyps differ on every count &mdash; unilateral, soft, and from one event."],
  ["Bilateral soft lesions at the anterior commissure from reflux",
   "Neither matches: polyps are unilateral on the middle third and follow acute strain, not bilateral at the commissure from reflux."],
  ["Unilateral fibrous calluses from chronic yelling",
   "This mixes the two lesions. Calluses from chronic trauma are nodules and they are bilateral; polyps are unilateral and follow a single event."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 25"},

{"topic": "Tonsillitis", "io": "Objective 2 — Review the ear, nose, neck, and throat pathology.", "slot": "microbiology",
 "q": "Which organism is the usual bacterial cause of tonsillitis, and which finding suggests abscess?",
 "opts": [
  ["Group A Streptococcus; asymmetric deviation with trismus",
   "Correct. Deviation and trismus indicate the infection has collected rather than staying confined to the tonsil and pharyngeal mucosa."],
  ["Streptococcus pneumoniae; bilateral exudate",
   "Pneumoniae is a middle ear and sinus organism here, and bilateral exudate is ordinary tonsillitis rather than abscess."],
  ["Pseudomonas aeruginosa; fever above 39 degrees",
   "Pseudomonas belongs to otitis externa, and fever alone does not indicate abscess."],
  ["Haemophilus influenzae; odynophagia",
   "Haemophilus is on the otitis media and sinusitis lists, and odynophagia is present in uncomplicated tonsillitis too."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 26"},

{"topic": "Cervical lymphadenopathy", "io": "Objective 2 — Review the ear, nose, neck, and throat pathology.", "slot": "clinical pattern",
 "q": "Which nodal findings require immediate assessment to exclude lymphoma?",
 "opts": [
  ["Persistent rubbery or matted nodes in older adults",
   "Correct. Reactive nodes are usually tender and follow a regional infection. Rubbery, matted, persistent and supraclavicular in an older patient is the combination that changes the level of concern."],
  ["Tender mobile nodes during a viral upper respiratory infection",
   "That is the ordinary reactive picture, which is usually benign."],
  ["Bilateral small nodes in a child with otitis media",
   "Regional response to a head and neck infection &mdash; the benign pathway described."],
  ["Any palpable cervical node at all",
   "Palpable nodes are common and usually reactive; the features listed are what raise concern."]],
 "c": 0, "cite": "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx, Slide 27"},

]
