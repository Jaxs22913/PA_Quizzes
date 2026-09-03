# -*- coding: utf-8 -*-
"""Lecture 16 rows for the ENT comparison chart.

Inner Ear, Balance and Hearing Loss, Prof. Monique Jaquith, 3 September.
Same shape as _cms_e3_chart_l15.py.

THE TWO HEARING-LOSS PATTERNS GET THEIR OWN ROWS. Conductive and sensorineural
are not diseases, but they ARE the lecture's objective ("Hearing impairment:
sensorineural, conductive") and slide 42 is a side-by-side comparison of them.
Everything else in the block is sorted by which of the two it produces, so
they belong at the top of the chart rather than buried in the guide.

BAROTRAUMA IS NOT REPEATED HERE. Slide 58 restates it, but Lecture 15 teaches
it in full and a second row would only split the same content across two
places. The Lecture 15 row carries the inner-ear complication this deck adds.
"""
PATTERN = "Hearing loss pattern"
TIN = "Tinnitus"
MASSL = "Canal and middle ear mass"
SNHL = "Acquired sensorineural"
INNER = "Inner ear syndrome"
CENTRAL = "Retrocochlear and central"
NONORG = "Non-organic"
D16 = "16. Disorders of Inner Ear"

ROWS_L16 = [
 ("Conductive hearing loss", PATTERN,
  "<b>Weber lateralises TO the bad ear</b> &middot; <b>BC &ge; AC</b> &middot; hearing better in noise",
  "An external or middle ear disorder impairing sound conduction to the inner ear. Four mechanisms: <b>obstruction</b> (cerumen), <b>mass loading</b> (effusion), <b>stiffness</b> (otosclerosis) and <b>discontinuity</b> (ossicular disruption). Onset is typically <b>childhood to age 40</b>. The abnormality is <b>usually visible on otoscopy &mdash; except in otosclerosis</b>. <b>Hearing seems to improve in a noisy environment</b> and the <b>voice stays soft</b>, because the inner ear and cochlear nerve are intact. Causes: cerumen impaction*, eustachian tube dysfunction*, otitis media, perforation, otosclerosis, foreign body, cholesteatoma, exostosis, glomus tumour, ossicular discontinuity (*commonest in adults).",
  "<b>Weber lateralises to the impaired ear.</b> <b>Rinne: BC = AC or BC &gt; AC.</b> Audiometry for the degree; tympanometry for the middle ear.",
  "Treat the cause. <b>Often correctable</b> &mdash; which is the headline difference from sensorineural loss.",
  "Routine",
  "The reassuring half of the pair: most conductive loss has a fixable mechanical cause.",
  "10&ndash;11, 42", D16),

 ("Sensorineural hearing loss", PATTERN,
  "<b>Weber lateralises AWAY to the good ear</b> &middot; <b>AC &gt; BC</b> &middot; <b>worse</b> in noise",
  "Sensory (deterioration of the cochlea and loss of hair cells) and neural (lesions of the eighth nerve, auditory nuclei, ascending tracts, auditory cortex) are <b>difficult to separate clinically and are grouped together</b>. Onset in <b>middle or later years</b>; <b>the ear canal and drum look normal</b>. <b>Higher registers are lost so sound is distorted</b>, <b>hearing worsens in a noisy environment</b>, and <b>the voice may be loud</b> because hearing is difficult.",
  "<b>Weber lateralises to the GOOD ear.</b> <b>Rinne: AC &gt; BC</b> &mdash; the same as normal, which is why Weber carries the diagnosis. Audiometry classifies severity: normal 0&ndash;20 dB, mild 20&ndash;40, moderate 40&ndash;60, severe 60&ndash;80, <b>profound &gt;80 dB</b>.",
  "<b>Usually not correctable</b>, but may be stabilised and some types prevented. <b>Acute-onset sensory loss may respond to corticosteroids in the first weeks.</b>",
  "Urgent",
  "The window for steroids in sudden loss is short, which is why new one-sided hearing loss is not a wait-and-see problem.",
  "12&ndash;14, 42", D16),

 ("Presbycusis", PATTERN,
  "<b>Hears people speak but cannot make out words</b> &middot; bilateral &middot; high frequency first",
  "<b>The commonest sensorineural hearing loss.</b> Progressive age-related loss from <b>hair cell loss in the organ of Corti and cochlear nerve degeneration</b>. <b>Bilateral, symmetrical, gradual.</b> <b>High frequencies go first</b>, progressing to mid and low. Patients <b>hear speech but cannot make out the words</b>, miss the doorbell and the phone, may have tinnitus, and <b>lip-read more than they realise</b>. Age is the strongest predictor: about 2% of adults 45&ndash;54, 8.5% at 55&ndash;64, nearly 25% at 65&ndash;74 and 50% over 75 have disabling loss; <b>men are almost twice as likely as women</b>.",
  "Audiometry showing bilateral symmetrical high-frequency loss.",
  "Amplification and communication strategy. Not correctable.",
  "Routine",
  "Face the patient, do not shout &mdash; volume is not the problem, <b>discrimination</b> is.",
  "15, 60&ndash;61", D16),

 ("Tinnitus", TIN,
  "<b>Ringing with no external source</b> &middot; <b>RED FLAG: unilateral or pulsatile</b>",
  "Can accompany <b>any</b> type of hearing loss and is <b>often the first symptom of it</b>. Described as ringing, buzzing, humming, hissing, a motor running, insects. <b>Usually subjective</b>; occasionally <b>objective</b>, meaning the examiner can hear it too. Everyone hears normal head noise in silence; low tolerance for it is associated with <b>depression, neurosis, stress and fatigue</b>.",
  "Clinical. <b>RED FLAG: unilateral or pulsatile tinnitus</b> &mdash; that pattern is investigated rather than reassured.",
  "<b>No drug has been more effective than placebo.</b> <b>Biofeedback and masking noises may work.</b>",
  "Routine",
  "Avoid loud noise, <b>get the lead level checked</b>, avoid stimulants, exercise daily, get adequate rest, and learn to treat the noise as an annoyance rather than a threat.",
  "44&ndash;46", D16),

 ("Exostosis", MASSL,
  "<b>Surfer or diver</b> &middot; <b>bilaterally symmetrical</b> bony canal growths",
  "Bony growth in the external canal, <b>bilaterally symmetrical</b>, related to <b>repetitive cold water exposure</b> &mdash; divers and surfers. Can <b>block the canal or collect debris</b>.",
  "Otoscopy. Causes <b>conductive</b> hearing loss.",
  "Address obstruction and trapped debris; surgical removal if the canal is occluded.",
  "Routine",
  "Earplugs in cold water are the prevention; the growths themselves are slow and painless.",
  "48", D16),

 ("Glomus tumour", MASSL,
  "<b>Pulsatile tinnitus</b> &middot; vascular middle ear mass &middot; cranial nerve IX, X, XI palsy",
  "<b>Benign but highly vascular</b> tumour derived from the normal glomus formations of the middle ear and jugular bulb. Produces a <b>middle ear mass effect</b>, can present with <b>spontaneous haemorrhage and paralysis of cranial nerves IX, X and XI</b>, and may <b>erode the skull base</b>.",
  "Causes <b>conductive hearing loss and pulsatile tinnitus</b> &mdash; the combination that separates it. Imaging for extent.",
  "ENT and skull base management.",
  "Urgent",
  "Pulsatile tinnitus with a mass behind the drum is not reassured away.",
  "50", D16),

 ("Ototoxicity", SNHL,
  "<b>Bilateral</b> sensorineural loss on a known drug &middot; <b>aminoglycosides</b>",
  "<b>Aminoglycosides are the most ototoxic and the most common</b> &mdash; monitor peak levels. Also <b>furosemide, aspirin</b> and <b>platinum-based chemotherapy</b>. Many other agents have potential ototoxicity, and <b>drugs that are ototoxic are frequently also nephrotoxic and vice versa</b>, including the non-steroidal anti-inflammatories. Produces <b>bilateral sensorineural hearing loss</b>.",
  "History of exposure plus audiometry. <b>Monitor aminoglycoside peak levels.</b>",
  "Stop or change the agent where possible; the loss is often not reversible.",
  "Urgent",
  "If a drug is ototoxic, ask about the kidneys too &mdash; the two toxicities travel together.",
  "52&ndash;53", D16),

 ("Noise-induced hearing loss", SNHL,
  "<b>Temporary threshold shift</b> recovering in 24&ndash;48 h &middot; &ldquo;crickets&rdquo; and fullness",
  "<b>One of the most common occupationally induced disabilities</b>; exposure is <b>regulated by OSHA</b>. Most acute exposures produce <b>temporary sensorineural loss recovering in 24&ndash;48 hours &mdash; a temporary threshold shift</b>, with the ear feeling full and &ldquo;crickets&rdquo;. <b>If the level is high enough or repeated often enough the loss becomes permanent &mdash; a permanent threshold shift.</b> Rarely, extremely intense impulse exposure perforates the drum, giving a conductive loss instead.",
  "Audiometry. Exposure history against the decibel table: damage is possible after <b>2 hours at 80&ndash;85 dB</b>, <b>50 minutes at 95</b>, <b>15 minutes at 100</b>, <b>under 5 minutes at 105&ndash;110</b>, and <b>pain and injury at 120</b>.",
  "Remove the exposure and protect hearing. The permanent component is not recoverable.",
  "Routine",
  "The temporary shift is the warning shot &mdash; recovering by the next day does not mean no damage is accumulating.",
  "54&ndash;55", D16),

 ("Acoustic trauma", SNHL,
  "<b>Single loud noise</b> &middot; immediate loss &middot; may perforate the drum",
  "A <b>single loud noise creating immediate hearing loss</b>, and it may perforate the tympanic membrane. <b>Blows to the head</b> can cause labyrinthine injury with resulting sensorineural loss. <b>Penetrating injuries are rare but usually involve subluxation of the stapes, causing profound sensorineural loss.</b>",
  "Audiometry. Depending on the type, the loss <b>can mimic noise-induced loss or be a complete loss of both auditory and vestibular function</b>.",
  "Supportive; ENT for perforation or suspected ossicular injury.",
  "Urgent",
  "One event can do what years of exposure does &mdash; and a penetrating injury threatens balance as well as hearing.",
  "56&ndash;57", D16),

 ("Perilymphatic fistula", SNHL,
  "<b>Audible &ldquo;pop&rdquo;</b> then sudden loss and vertigo after <b>straining or barotrauma</b>",
  "A <b>pathological communication between the perilymphatic space of the inner ear and the middle ear</b>, at the <b>round or oval window</b>. Congenital or acquired. Acquired causes: <b>barotrauma, temporal bone trauma, or a complication of stapedectomy</b>. Presents as <b>sudden sensorineural loss and vertigo after head injury, barotrauma, or heavy lifting and straining</b>, <b>sometimes with an audible &ldquo;pop&rdquo;</b>. A <b>rare</b> cause of vertigo and sensorineural loss.",
  "Clinical, on the history. Fistula test is among the vestibular studies.",
  "<b>Treat symptomatically and refer to ENT.</b>",
  "Urgent",
  "The trigger is the diagnosis: sudden hearing loss and vertigo that began with a strain, a dive or a blow.",
  "63&ndash;64", D16),

 ("Autoimmune sensorineural loss", SNHL,
  "<b>Bilateral, progressive</b>, in periods of deterioration and stabilisation",
  "Sensorineural loss that is <b>most often bilateral and progressive</b>, with <b>periods of deterioration and stabilisation</b>, and <b>may be accompanied by vestibular dysfunction</b>. Uncommon: <b>Cogan's syndrome, polyarteritis nodosa, relapsing polychondritis, granulomatosis with polyangiitis</b>. Even less common: scleroderma, temporal arteritis, systemic lupus erythematosus, sarcoidosis.",
  "<b>Routine screening for autoimmune disorders is not warranted</b> &mdash; test when the picture suggests it.",
  "Treat the underlying disease.",
  "Urgent",
  "The stepwise pattern &mdash; worse, then stable, then worse &mdash; is what distinguishes it from a steady decline.",
  "65&ndash;66", D16),

 ("Syphilitic sensorineural loss", SNHL,
  "<b>Indistinguishable from M&eacute;ni&egrave;re's</b> &middot; the treatable cause you must not miss",
  "Congenital or acquired. <b>Hearing loss is not associated with primary acquired syphilis</b>, but reaches <b>as high as 80% in symptomatic neurosyphilis</b>. <b>Presentation is often indistinguishable from M&eacute;ni&egrave;re's</b>: fluctuating sensorineural loss, tinnitus, aural fullness and episodic vertigo.",
  "<b>The one exception to not ordering labs.</b> <b>FTA-ABS</b> and <b>MHA-TP</b> should be obtained. <b>VDRL is not helpful.</b>",
  "<b>Antibiotic with the addition of systemic corticosteroids.</b>",
  "Urgent",
  "It is tested for precisely because it is <b>a potentially treatable cause of sensorineural loss</b> hiding behind a M&eacute;ni&egrave;re's picture.",
  "35, 68", D16),

 ("AIDS-related sensorineural loss", SNHL,
  "Unexplained sensorineural loss with <b>risk factors present</b>",
  "Sensorineural loss is among the numerous neurological manifestations of AIDS. It may come from an <b>infectious complication &mdash; cryptococcal meningitis or syphilis &mdash;</b> or be a <b>primary neurological manifestation</b>.",
  "Consider in any patient with <b>unexplained sensorineural loss and risk factors present</b>.",
  "Treat the underlying cause.",
  "Urgent",
  "It is on the list so that unexplained loss prompts a risk-factor history rather than an audiogram alone.",
  "67", D16),

 ("Hereditary sensorineural loss", SNHL,
  "<b>Waardenburg, Alport, Usher</b> &middot; and the nonsyndromic majority",
  "<b>Nonsyndromic hereditary hearing loss</b>, plus the named syndromes: <b>Waardenburg's</b>, <b>Alport</b> and <b>Usher's</b>.",
  "Family history; genetic evaluation where indicated.",
  "Amplification and the associated systemic disease.",
  "Routine",
  "The syndromic names carry the other organ involved &mdash; kidney in Alport, vision in Usher.",
  "71", D16),

 ("Sudden sensorineural hearing loss", SNHL,
  "<b>Unilateral</b>, sudden &middot; <b>a syndrome, not a disease</b> &middot; <b>prompt ENT referral</b>",
  "<b>Unilateral.</b> Described explicitly as <b>a syndrome, not a disease</b>. <b>Viral or vascular</b> aetiology; <b>rarely retrocochlear pathology &mdash; horses not zebras</b>. <b>The exact cause is rarely certain.</b>",
  "Audiometry to confirm and side it. Imaging only in selected patients.",
  "<b>Demands prompt referral to ENT.</b> Acute sensory loss may respond to <b>corticosteroids within the first weeks</b>.",
  "Emergent",
  "Speed is the whole management. This is the one hearing complaint that is seen the same day.",
  "13, 79", D16),

 ("M&eacute;ni&egrave;re's disease", INNER,
  "<b>Vertigo hours long</b> &middot; <b>LOW-frequency</b> fluctuating loss &middot; fullness and low-tone tinnitus",
  "<b>Fluctuating LOW-frequency sensorineural hearing loss</b> that may fluctuate at first then progress. <b>Low-tone, &ldquo;blowing&rdquo; tinnitus.</b> <b>Unilateral fullness in the ear.</b> <b>Episodes of vertigo, often the presenting complaint.</b> Typical attack: <b>episodic, spontaneous, severe spinning vertigo lasting several hours</b>, frequently with nausea, vomiting and diaphoresis.",
  "Clinical. <b>Duration separates it</b>: seconds for benign positional vertigo, <b>minutes to hours for M&eacute;ni&egrave;re's</b>, days to weeks for vestibular neuronitis and labyrinthitis. <b>Rule out syphilis</b>, which mimics it exactly.",
  "Symptomatic control of the attacks and the underlying management.",
  "Urgent",
  "The tetrad is vertigo, fluctuating hearing loss, tinnitus and fullness &mdash; and unlike the other peripheral causes, <b>hearing is affected</b>.",
  "69&ndash;70, 89, 97", D16),

 ("Benign paroxysmal positional vertigo", INNER,
  "<b>Seconds</b> of vertigo <b>on rolling over</b> &middot; <b>hearing normal, no tinnitus</b>",
  "<b>Severe vertigo with change in head position</b> &mdash; rolling over, getting into bed, standing up, bending, looking up to reach an object, tilting the head back to shave, a haircut, turning rapidly. <b>A specific side is typically described.</b> Symptoms come on after a <b>short latency of 10&ndash;15 seconds</b> and <b>last only 10&ndash;60 seconds</b>; <b>more than a minute should prompt an alternative diagnosis</b>. Bouts cluster in time with remissions of months or more. Between attacks there may be constant lightheadedness worse with head movement, and imbalance for hours after an episode.",
  "<b>Diagnosed by the classic eye movements on the Dix-Hallpike manoeuvre</b> plus a suggestive history. <b>Most cases have no identifiable aetiology</b>; <b>canalithiasis of the posterior semicircular canal</b> is thought to be the commonest cause.",
  "<b>The Epley manoeuvre</b>, which repositions the otoliths in the semicircular canal.",
  "Routine",
  "Hearing is <b>not affected</b> and there is <b>no tinnitus</b> &mdash; those two absences are what place it against M&eacute;ni&egrave;re's.",
  "89&ndash;93, 97", D16),

 ("Labyrinthitis", INNER,
  "<b>Sudden vertigo WITH hearing loss</b> lasting days to weeks",
  "<b>Inflammation of the membranous labyrinth</b> of the inner ear. <b>Relatively sudden onset of sensorineural hearing loss AND acute vertigo.</b> Exact aetiology rarely certain; <b>evidence supports a viral cause</b>, and it may be associated with bacterial infection or systemic autoimmune disease. Also listed as a complication of acute otitis media.",
  "Clinical. Duration <b>several days to weeks</b>.",
  "<b>Symptomatic.</b> <b>Antibiotics if bacterial symptoms such as fever are present.</b> <b>Oral corticosteroids.</b> <b>Oral diazepam or meclizine during the acute vertigo.</b>",
  "Urgent",
  "The difference from vestibular neuronitis is one word: <b>labyrinthitis affects hearing</b>.",
  "95, 97", D16),

 ("Vestibular neuronitis", INNER,
  "<b>Dramatic sudden vertigo with NO hearing change</b> &middot; benign and self-limiting",
  "<b>Inflammation of the vestibular portion of cranial nerve VIII</b>, <b>likely viral</b> though the cause is unknown. <b>Considered benign and self-limiting.</b> <b>Dramatic, sudden vertigo with nausea and gait imbalance.</b> Dizziness <b>lasts days with gradual improvement</b>; balance symptoms may persist for months. <b>Not associated with any change in hearing or focal neurological complaints.</b>",
  "<b>Clinical diagnosis.</b>",
  "<b>Symptomatic.</b> <b>Oral diazepam or meclizine</b> during the acute phase, <b>antiemetics</b>, and oral corticosteroids are questioned in the deck rather than asserted.",
  "Urgent",
  "Normal hearing and no focal neurology is what makes it benign &mdash; either of those being abnormal moves the diagnosis.",
  "96&ndash;97", D16),

 ("Acoustic neuroma", CENTRAL,
  "<b>Unilateral</b> loss with <b>speech discrimination worse than the tone loss predicts</b>",
  "<b>Benign tumour of cranial nerve VIII</b>, <b>rare</b>, and <b>most often unilateral</b>. Symptoms: <b>unilateral hearing loss, which may be sudden</b>; <b>poor speech discrimination compared with what the tone loss would predict</b>; often <b>disequilibrium</b>. <b>Progression may not be so &ldquo;benign&rdquo;.</b> May involve cranial nerves V and VII.",
  "<b>MRI with gadolinium is the gold standard</b> for evaluating potential retrocochlear loss. <b>Electronystagmography is the gold standard vestibular test</b> for disorders affecting one ear at a time. Radiographic imaging is warranted in selected patients with sensorineural loss.",
  "<b>Observation with annual MRI, surgery, or radiation.</b>",
  "Urgent",
  "The discriminating symptom is not the volume of the loss but the <b>disproportionately poor word understanding</b> on the affected side.",
  "72&ndash;75, 97", D16),

 ("Vertebrobasilar insufficiency or occlusion", CENTRAL,
  "<b>Vertigo in an elderly patient with brainstem signs</b>",
  "<b>A common cause of vertigo in elderly patients.</b> Occlusion may be <b>thrombotic or embolic</b>. Symptoms: acute vertigo, nausea and vomiting, <b>facial paralysis</b>, tinnitus, <b>ipsilateral gaze paralysis</b>, <b>ipsilateral loss of pain and temperature on the face</b>, <b>contralateral partial loss of pain and temperature on the trunk and limbs</b>, and <b>ipsilateral Horner's syndrome</b>. Vascular disease is the <b>commonest non-vestibular cause of dizziness and balance loss in the elderly</b>.",
  "<b>Magnetic resonance angiography</b>, which also shows small vessel disease as scattered small white lesions. Carotid dopplers.",
  "Vascular and stroke management.",
  "Emergent",
  "Vertigo with any crossed sensory finding, facial weakness or gaze palsy is a brainstem problem until proven otherwise.",
  "77, 85&ndash;87", D16),

 ("Isolated cerebellar infarction", CENTRAL,
  "<b>Vertigo with ataxia, headache or facial numbness</b>",
  "Symptoms include <b>vertigo, facial pain or numbness, headache, or ataxia</b>. The deck's instruction is explicit: <b>&ldquo;Don't miss something bigger than the hearing loss&rdquo;</b> &mdash; look for signs of a more sinister acute problem.",
  "Neuroimaging.",
  "<b>Refer for evaluation.</b>",
  "Emergent",
  "It is in a hearing lecture as a warning, not as an ear disease.",
  "78", D16),

 ("Functional hearing loss", NONORG,
  "<b>Claims profound bilateral loss but the voice is normal</b>",
  "Suspected when the history contains <b>inconsistencies, complaints and exaggerated listening effort</b>. <b>The patient's voice and speech quality provide important information</b>: someone claiming <b>significant bilateral loss while speaking at a normal level with normal articulation</b> should be suspected of functional behaviour.",
  "The mismatch between claimed loss and the voice is the finding. Audiometry with cross-checks.",
  "Address the underlying reason rather than the audiogram.",
  "Routine",
  "A genuinely deaf voice changes. That is the observation the diagnosis rests on.",
  "80", D16),
]

DIFF_L16 = {
 "Conductive hearing loss": ("Depends on the cause", "<b>Conductive</b>", "<b>Weber TO the bad ear; BC &ge; AC</b>"),
 "Sensorineural hearing loss": ("No", "<b>Sensorineural</b>", "<b>Weber to the GOOD ear; AC &gt; BC</b>"),
 "Presbycusis": ("No", "<b>Sensorineural</b>, bilateral", "<b>High-frequency loss</b>, normal drum"),
 "Tinnitus": ("No", "Any type &mdash; often the first symptom", "<b>Unilateral or pulsatile is the red flag</b>"),
 "Exostosis": ("No", "<b>Conductive</b>", "<b>Bilateral bony canal growths</b>"),
 "Glomus tumour": ("No", "<b>Conductive</b>", "<b>Vascular middle ear mass; pulsatile tinnitus</b>"),
 "Ototoxicity": ("No", "<b>Sensorineural, BILATERAL</b>", "Normal drum; drug history"),
 "Noise-induced hearing loss": ("No &mdash; fullness, &ldquo;crickets&rdquo;", "<b>Sensorineural</b>", "Normal drum; exposure history"),
 "Acoustic trauma": ("<b>YES</b> at the time", "<b>Sensorineural</b>; conductive if perforated", "May show <b>perforation</b>"),
 "Perilymphatic fistula": ("No", "<b>Sensorineural, sudden</b>", "<b>Audible &ldquo;pop&rdquo;</b> with vertigo"),
 "Autoimmune sensorineural loss": ("No", "<b>Sensorineural, bilateral</b>", "Stepwise deterioration"),
 "Syphilitic sensorineural loss": ("No", "<b>Sensorineural, fluctuating</b>", "<b>Mimics M&eacute;ni&egrave;re's</b>"),
 "AIDS-related sensorineural loss": ("No", "<b>Sensorineural</b>", "Unexplained loss with risk factors"),
 "Hereditary sensorineural loss": ("No", "<b>Sensorineural</b>", "Family history; syndromic features"),
 "Sudden sensorineural hearing loss": ("No", "<b>Sensorineural, UNILATERAL</b>", "Normal drum, sudden onset"),
 "M&eacute;ni&egrave;re's disease": ("No &mdash; fullness", "<b>Sensorineural, LOW frequency, fluctuating</b>", "<b>Vertigo lasting hours</b> + tinnitus"),
 "Benign paroxysmal positional vertigo": ("No", "<b>NOT affected</b>", "<b>Positive Dix-Hallpike</b>; seconds only"),
 "Labyrinthitis": ("No", "<b>Sensorineural &mdash; hearing IS affected</b>", "Sudden vertigo, days to weeks"),
 "Vestibular neuronitis": ("No", "<b>NOT affected</b>", "Sudden vertigo, no hearing change"),
 "Acoustic neuroma": ("No", "<b>Sensorineural, unilateral</b>", "<b>Speech discrimination worse than expected</b>"),
 "Vertebrobasilar insufficiency or occlusion": ("No", "May be affected", "<b>Brainstem signs</b> with the vertigo"),
 "Isolated cerebellar infarction": ("<b>Headache</b> possible", "Not affected", "<b>Ataxia, facial numbness</b>"),
 "Functional hearing loss": ("No", "<b>Claimed, not organic</b>", "<b>Normal voice despite claimed loss</b>"),
}

# THE TWO PRESBYCUSIS AUDIOGRAMS ARE NOT INTERCHANGEABLE. Slide 19's audiogram
# carries a printed caption calling itself "an example presbyacusis (sloping
# high-frequency hearing loss)", so it goes to the PRESBYCUSIS row. The generic
# sensorineural row gets slide 5's familiar-sounds audiogram instead, which is
# tied to no diagnosis and shows the point the row actually makes -- which
# sounds sit in the high registers that go first.
IMGS_L16 = {
 "Conductive hearing loss": ("l16-s039_pos1.jpg", 39),
 "Sensorineural hearing loss": ("l16-s005_pos1.jpg", 5),
 "Presbycusis": ("l16-s019_pos1.jpg", 19),
 "Tinnitus": ("l16-s043_pos1.jpg", 43),
 "Exostosis": ("l16-s049_pos2.jpg", 49),
 "Glomus tumour": ("l16-s051_pos1.jpg", 51),
 "Acoustic neuroma": ("l16-s073_pos1.jpg", 73),
}
