# -*- coding: utf-8 -*-
from _pd2_ent_osce_data import E
BATCH = {

"Ototoxicity": E(
  "&ldquo;Since I started that new medication my ears ring and my hearing is worse.&rdquo;",
  "<b>Review every medication and the cumulative dose</b> &mdash; this is the examination that "
  "matters. Otoscopy is normal. Weber and Rinne give a sensorineural pattern. Assess gait and do "
  "the head impulse test, since some agents hit balance rather than hearing.",
  [("Presbycusis", "Age-related and gradual, with no temporal link to a drug"),
   ("Noise-induced loss", "A 4000 hertz notch and an exposure history"),
   ("Meniere disease", "Episodic vertigo with fluctuating LOW-frequency loss and fullness")],
  "<b>Serial audiometry</b> &rarr; a <b>bilateral, symmetric, HIGH-frequency sensorineural loss "
  "that progresses with dosing</b>. <b>Drug levels</b> where relevant &rarr; troughs above target. "
  "Loop diuretic loss may be reversible; aminoglycoside loss usually is not.",
  "A loss that predates the drug excludes it; asymmetry points elsewhere and needs imaging; "
  "low-frequency fluctuating loss redirects to Meniere disease."),

"Noise-induced hearing loss": E(
  "&ldquo;After the concert my ears rang for a day.&rdquo; Or, at work, &ldquo;I&rsquo;ve been on "
  "the factory floor for twenty years.&rdquo;",
  "Otoscopy is normal. Weber and Rinne showing sensorineural loss. <b>Take a detailed exposure "
  "history &mdash; occupational, recreational, firearms &mdash; and ask about hearing protection.</b>",
  [("Presbycusis", "Sloping high-frequency loss WITHOUT a notch, and no exposure history"),
   ("Acoustic trauma", "A single blast rather than cumulative exposure"),
   ("Ototoxicity", "Drug-related and typically progressing with dose")],
  "<b>Audiometry</b> &rarr; a <b>notch at 3000 to 6000 hertz, classically 4000, with RECOVERY at "
  "8000 hertz</b>. That recovery is what separates the notch from presbycusis, which keeps falling.",
  "A continuously sloping curve without recovery at 8000 hertz is presbycusis; asymmetry suggests "
  "another cause; an air-bone gap means a conductive component."),

"Acoustic trauma": E(
  "&ldquo;A firework went off next to me and that ear has been ringing and muffled ever "
  "since.&rdquo;",
  "Otoscopy &mdash; <b>look for a perforation</b>, since blast can do both. Weber and Rinne; the "
  "pattern may be mixed. Assess for vertigo.",
  [("Noise-induced hearing loss", "Cumulative exposure rather than one event"),
   ("Tympanic membrane perforation", "Conductive loss from the blast; the drum shows the tear"),
   ("Perilymphatic fistula", "Vertigo with sensorineural loss and pressure sensitivity")],
  "<b>Audiometry</b> &rarr; a sensorineural loss, often with tinnitus, from a single event; a "
  "mixed pattern if the drum is also perforated.",
  "A pure conductive loss with a visible perforation is the drum alone; persistent vertigo raises "
  "a fistula; a gradual course excludes acute trauma."),

"Perilymphatic fistula": E(
  "&ldquo;Since the dive, when I strain or hear a loud noise the room tilts.&rdquo;",
  "<b>Fistula test</b> &mdash; pressure on the tragus provokes vertigo or nystagmus. Ask about "
  "symptoms on <b>straining, coughing or lifting</b>. Otoscopy. Weber and Rinne. Assess gait.",
  [("Meniere disease", "Spontaneous episodic vertigo, not provoked by pressure or sound"),
   ("Barotrauma", "Conductive loss from the same event, without vertigo or sensorineural loss"),
   ("Superior canal dehiscence", "Sound-induced vertigo too, but with autophony and a bony defect on imaging")],
  "<b>Audiometry</b> &rarr; a fluctuating sensorineural loss. <b>High-resolution computed "
  "tomography of the temporal bone</b> &rarr; a bony defect or pneumolabyrinth. <b>Exploratory "
  "tympanotomy</b> &rarr; visible perilymph leak, which is definitive.",
  "A negative fistula test with a purely conductive loss points to simple barotrauma; a dehiscent "
  "superior canal on fine-cut imaging redirects the diagnosis."),

"Autoimmune sensorineural loss": E(
  "&ldquo;My hearing has dropped in both ears over a few weeks &mdash; and my joints have been "
  "sore.&rdquo;",
  "Otoscopy is normal. Serial tuning forks and audiometry to show progression. <b>Look for "
  "systemic autoimmune disease &mdash; joints, skin, eyes (interstitial keratitis suggests Cogan "
  "syndrome), kidneys.</b>",
  [("Sudden sensorineural hearing loss", "Sudden and usually unilateral rather than progressive and bilateral"),
   ("Meniere disease", "Episodic vertigo with fullness and fluctuating low-frequency loss"),
   ("Syphilitic loss", "Can mimic it exactly &mdash; which is why serology is sent")],
  "<b>Serial audiometry</b> &rarr; a <b>rapidly progressive bilateral asymmetric sensorineural "
  "loss over weeks to months</b>. <b>Autoimmune screen</b> (antinuclear antibody, inflammatory "
  "markers) and a <b>trial of corticosteroids</b> &rarr; improvement supports the diagnosis.",
  "Negative treponemal serology excludes syphilis; a stable audiogram over months excludes it; "
  "no steroid response argues against it."),

"Syphilitic sensorineural loss": E(
  "&ldquo;My hearing and balance have both been going.&rdquo; &mdash; the history may include "
  "nothing obvious.",
  "Otoscopy is normal. Audiometry and tuning forks. <b>Look for systemic signs and take a sexual "
  "history.</b> Ophthalmic examination for interstitial keratitis. <b>Fistula test may be positive "
  "without a fistula (Hennebert sign).</b>",
  [("Autoimmune sensorineural loss", "The clinical twin &mdash; separated only by serology"),
   ("Meniere disease", "Episodic, with the classic triad, and no systemic features"),
   ("Acoustic neuroma", "Unilateral and progressive, with imaging findings")],
  "<b>Treponemal serology</b> (fluorescent treponemal antibody absorption or equivalent) &rarr; "
  "reactive. <b>Lumbar puncture</b> if neurosyphilis is suspected &rarr; reactive cerebrospinal "
  "fluid with pleocytosis. <b>Audiometry</b> &rarr; a fluctuating or progressive sensorineural loss.",
  "Non-reactive treponemal serology excludes it and redirects to the autoimmune workup; normal "
  "imaging excludes a schwannoma."),

"AIDS-related sensorineural loss": E(
  "&ldquo;My hearing has got worse&rdquo; &mdash; in a patient known to be, or at risk of being, "
  "immunocompromised.",
  "Otoscopy &mdash; look for opportunistic infection and Kaposi lesions. Audiometry. <b>Review "
  "antiretroviral and antimicrobial drugs for ototoxicity</b>, which is often the real cause. Full "
  "cranial nerve examination.",
  [("Ototoxicity", "From the treatment rather than the disease &mdash; commonly the actual mechanism"),
   ("Opportunistic central nervous system infection", "Focal neurological signs alongside the hearing loss"),
   ("Otitis media with effusion", "A conductive loss, more common in this group too")],
  "<b>Audiometry</b> &rarr; a sensorineural loss. <b>Human immunodeficiency virus serology and CD4 "
  "count</b> &rarr; the diagnosis and degree of immunosuppression. <b>Imaging</b> if focal signs "
  "&rarr; an opportunistic lesion.",
  "A conductive pattern redirects to middle ear disease; improvement after stopping a culprit "
  "drug points to ototoxicity; normal imaging excludes a central lesion."),

"Hereditary sensorineural loss": E(
  "&ldquo;It runs in my family &mdash; my father and my brother both went deaf young.&rdquo; Or a "
  "newborn fails the hearing screen.",
  "Otoscopy is normal. Audiometry. <b>Draw a three-generation family tree.</b> Look for syndromic "
  "features: <b>white forelock and different-coloured eyes (Waardenburg), goitre (Pendred), "
  "retinitis pigmentosa (Usher), renal disease (Alport)</b>.",
  [("Congenital infection", "Cytomegalovirus or rubella &mdash; acquired, not inherited"),
   ("Presbycusis", "Late onset without a family pattern"),
   ("Noise-induced loss", "An exposure history and a characteristic notch")],
  "<b>Audiometry</b> &rarr; a sensorineural loss, often symmetric. <b>Genetic testing</b> &rarr; a "
  "causative variant, connexin 26 being the commonest. <b>Imaging</b> &rarr; inner ear malformation "
  "such as an enlarged vestibular aqueduct.",
  "Positive congenital infection screening redirects the cause; an exposure history with a 4000 "
  "hertz notch means noise; a negative family history does not exclude a recessive cause."),

"M&eacute;ni&egrave;re's disease": E(
  "&ldquo;It comes in attacks &mdash; the room spins for hours, my ear feels full and roars, and my "
  "hearing goes down and then comes back.&rdquo;",
  "Otoscopy is normal. <b>Weber lateralises AWAY, Rinne positive</b>. <b>Dix-Hallpike, which should "
  "be negative</b> &mdash; that is how positional vertigo is excluded. Head impulse test, "
  "nystagmus, gait, cerebellar signs and cranial nerves.",
  [("Benign paroxysmal positional vertigo", "SECONDS, positional, no hearing loss or fullness"),
   ("Vestibular neuronitis", "A single sustained attack over days with NO hearing loss"),
   ("Acoustic neuroma", "Progressive unilateral loss with imbalance rather than discrete attacks")],
  "<b>Audiometry during or between attacks</b> &rarr; a <b>fluctuating LOW-frequency sensorineural "
  "loss</b>, which is the signature. <b>Magnetic resonance</b> &rarr; normal, done to exclude a "
  "schwannoma rather than to confirm this.",
  "A positive Dix-Hallpike with fatigable nystagmus means positional vertigo; normal hearing "
  "throughout excludes Meniere disease; an enhancing internal auditory canal lesion redirects to "
  "acoustic neuroma."),

"Benign paroxysmal positional vertigo": E(
  "&ldquo;When I roll over in bed or look up, the room spins for about half a minute, then "
  "stops.&rdquo;",
  "<b>Dix-Hallpike manoeuvre</b> &mdash; the diagnostic test. Look for <b>upbeating torsional "
  "nystagmus after a latency of a few seconds, lasting under a minute and fatiguing on "
  "repetition</b>. Supine roll test for the horizontal canal. Otoscopy and hearing are normal; "
  "check cerebellar signs.",
  [("Meniere disease", "Hours of vertigo with hearing loss and fullness, not seconds"),
   ("Vestibular neuronitis", "Continuous for days rather than provoked and brief"),
   ("Central positional vertigo", "Nystagmus WITHOUT latency, non-fatiguing, direction-changing")],
  "<b>Dix-Hallpike</b> &rarr; latency, torsional upbeating nystagmus, brief duration, fatigability. "
  "All four features together confirm it; no imaging is required.",
  "Nystagmus that is immediate, sustained and non-fatiguing is CENTRAL and needs imaging; hearing "
  "loss excludes it; continuous vertigo redirects to neuronitis."),

"Labyrinthitis": E(
  "&ldquo;The spinning has been constant for two days and my hearing has dropped on that "
  "side.&rdquo;",
  "Otoscopy &mdash; look for otitis media as a source. <b>Weber and Rinne: hearing loss is what "
  "separates this from neuronitis.</b> Head impulse test, nystagmus direction, <b>truncal "
  "stability</b> and cerebellar signs.",
  [("Vestibular neuronitis", "Identical vertigo but hearing is PRESERVED"),
   ("Cerebellar infarction", "Cannot sit unsupported, direction-changing nystagmus, headache"),
   ("Meniere disease", "Recurrent discrete attacks rather than one sustained illness")],
  "<b>Clinical</b> &rarr; sustained vertigo with unidirectional nystagmus, an abnormal head impulse "
  "test, plus hearing loss. <b>Audiometry</b> &rarr; a sensorineural loss on the affected side. "
  "<b>Imaging</b> only if central features appear.",
  "Normal hearing means vestibular neuronitis; direction-changing nystagmus or truncal instability "
  "means a central cause and needs urgent imaging; brief positional attacks mean positional vertigo."),

"Vestibular neuronitis": E(
  "&ldquo;I woke up two days ago and the room has been spinning ever since &mdash; but my hearing "
  "is fine.&rdquo;",
  "<b>Head impulse test</b> &mdash; a corrective saccade toward the affected side. Nystagmus should "
  "be <b>unidirectional and horizontal, beating away from the lesion</b>. <b>Test truncal "
  "stability &mdash; the patient can sit.</b> Full cerebellar and cranial nerve examination. "
  "Otoscopy and hearing are normal.",
  [("Labyrinthitis", "The same picture PLUS hearing loss"),
   ("Cerebellar infarction", "Normal head impulse test, direction-changing nystagmus, cannot sit"),
   ("Meniere disease", "Recurrent episodes with fullness and fluctuating hearing")],
  "<b>Clinical</b> &rarr; the three-part peripheral pattern: abnormal head impulse test, "
  "unidirectional nystagmus, no skew deviation, with normal hearing.",
  "A NORMAL head impulse test in a persistently vertiginous patient is a red flag for a central "
  "cause; hearing loss makes it labyrinthitis; imaging excludes infarction where doubt exists."),

"Acoustic neuroma": E(
  "&ldquo;My hearing has slowly gone in one ear, it rings, and I feel unsteady &mdash; lately my "
  "face feels a bit numb.&rdquo;",
  "Otoscopy is normal. <b>Weber lateralises AWAY, Rinne positive.</b> <b>Cranial nerves V and VII "
  "&mdash; corneal reflex is an early loss.</b> Gait and cerebellar testing. Note that <b>facial "
  "weakness is a LATE sign</b>, so its absence proves nothing.",
  [("Presbycusis", "Bilateral and symmetric; asymmetry is what triggers imaging"),
   ("Meniere disease", "Episodic vertigo with fullness and low-frequency fluctuating loss"),
   ("Sudden sensorineural hearing loss", "Abrupt rather than slowly progressive")],
  "<b>Magnetic resonance imaging with gadolinium</b> &rarr; an enhancing mass in the internal "
  "auditory canal or cerebellopontine angle &mdash; the gold standard. <b>Audiometry</b> &rarr; an "
  "asymmetric sensorineural loss with <b>speech discrimination disproportionately poor</b> for the "
  "pure tone thresholds.",
  "Normal magnetic resonance imaging excludes it; symmetric loss makes presbycusis far more likely; "
  "fluctuating low-frequency loss with fullness redirects to Meniere disease."),

"Functional hearing loss": E(
  "&ldquo;I can&rsquo;t hear anything at all in that ear&rdquo; &mdash; yet the patient responds to "
  "conversation from that side.",
  "Otoscopy is normal. <b>Watch for internal inconsistency</b>: responding to speech at levels the "
  "claimed threshold would not permit. <b>Weber and Rinne that do not fit the claimed loss</b> "
  "&mdash; a total unilateral loss should lateralise away, and often does not. Stenger test.",
  [("True sensorineural loss", "Tuning forks, audiometry and behaviour all agree"),
   ("Conductive loss", "A visible cause with a matching air-bone gap"),
   ("Auditory processing disorder", "Consistent thresholds with difficulty only in noise")],
  "<b>Objective testing</b> &mdash; <b>otoacoustic emissions</b> &rarr; present, proving cochlear "
  "function; <b>auditory brainstem response</b> &rarr; normal thresholds. Both contradict the "
  "claimed loss. <b>Stenger test</b> &rarr; positive in a feigned unilateral loss.",
  "Absent emissions with an abnormal brainstem response mean the loss is REAL; consistent "
  "behavioural results across sessions argue against it. Approach without accusation &mdash; there "
  "may be a genuine psychological cause."),
}
