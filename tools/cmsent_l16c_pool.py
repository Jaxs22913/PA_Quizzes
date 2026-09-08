# -*- coding: utf-8 -*-
"""Lecture 16, third pool -- Inner Ear, Balance and Hearing Loss. Short keys."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsent_style import Q

D = "16. Disorders of Inner Ear"
IO = ("Disorders of the inner ear, balance and hearing loss: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")

QUESTIONS = [

Q("Weber test", IO,
  "A patient's Weber test lateralises to the left ear. Two explanations are possible.",
  [["A left conductive loss or a right sensorineural loss",
    "Correct. Weber lateralises toward a conductive loss, because that ear is shielded from ambient "
    "noise and picks up the bone-conducted tone more clearly. It lateralises away from a "
    "sensorineural loss, because that cochlea processes the tone poorly. Both therefore point the "
    "sound to the left, and only Rinne separates them."],
   ["A left sensorineural loss or a right conductive loss",
    "This reverses both halves. A left sensorineural loss would push the sound to the right, and a "
    "right conductive loss would also pull it right, so this pairing describes lateralisation to the "
    "opposite ear."],
   ["Only a left conductive loss",
    "Conductive loss on the side of lateralisation is one valid answer, but stopping there misses "
    "the sensorineural possibility on the other side, which is why Weber alone can never make the "
    "diagnosis."],
   ["Only a right sensorineural loss",
    "This is the other valid single answer, and it has the same problem in reverse. Naming one "
    "possibility as though it were the only one is the error the paired testing exists to prevent."]],
  "finding", D, 19),

Q("Rinne test", IO,
  "A student asks why the Rinne test alone cannot diagnose a sensorineural hearing loss.",
  [["A sensorineural ear gives the same result as a normal one",
    "Correct. Rinne compares air against bone within a single ear. In sensorineural loss both "
    "pathways are reduced by the same cochlear problem, so air still beats bone exactly as in a "
    "normal ear. The test returns a normal pattern, and only Weber, which compares the two ears, "
    "reveals the asymmetry."],
   ["Rinne cannot be performed accurately in sensorineural loss",
    "The test is performed identically and is perfectly reliable. Its limitation is what the result "
    "means, not whether the result can be obtained."],
   ["Sensorineural loss reverses the Rinne result",
    "Reversal, with bone beating air, is the CONDUCTIVE pattern. Reporting it in sensorineural loss "
    "inverts the single most useful thing the test tells you."],
   ["Rinne only tests bone conduction",
    "Rinne compares both pathways in turn, which is its entire purpose. A test of bone conduction "
    "alone could not generate a comparison at all."]],
  "mechanism", D, 19),

Q("Ototoxicity", IO,
  "A clinician wants to name the drug classes most associated with cochlear toxicity.",
  [["Aminoglycosides and loop diuretics",
    "Correct. Aminoglycosides accumulate in and destroy cochlear hair cells, usually permanently, "
    "starting at the high frequencies. Loop diuretics affect the stria vascularis and their effect is "
    "more often reversible. Both appear as named ototoxic classes, and the difference in "
    "reversibility matters for what the patient is told."],
   ["Beta blockers and calcium channel blockers",
    "Cardiovascular drugs of these classes are not recognised ototoxins. They can cause dizziness "
    "through hypotension, which is a different symptom from cochlear damage."],
   ["Proton pump inhibitors and antihistamines",
    "Neither class damages the cochlea. Antihistamines cause sedation and can suppress vestibular "
    "symptoms, which is a therapeutic effect rather than toxicity."],
   ["Statins and metformin",
    "These carry muscular and gastrointestinal effects respectively and are not associated with "
    "hearing loss. Attributing a new sensorineural loss to them would divert the search from the "
    "real cause."]],
  "cause", D, 32),

Q("Vestibular schwannoma", IO,
  "A 48-year-old man with a unilateral sensorineural loss is found to have a vestibular "
  "schwannoma. He asks why his balance has been only mildly affected.",
  [["Central compensation adjusts to a slowly growing lesion",
    "Correct. The tumour enlarges over years, so the vestibular input on that side declines "
    "gradually and the brainstem and cerebellum recalibrate continuously. That is why patients "
    "describe unsteadiness rather than vertigo, unlike a sudden vestibular loss such as neuronitis, "
    "which produces dramatic spinning because there is no time to compensate."],
   ["The tumour does not involve the vestibular nerve",
    "It arises from the vestibular division of the eighth nerve, which is where its name comes from. "
    "The nerve is involved from the outset; it is the rate of change that determines the symptom."],
   ["Vestibular symptoms only occur once hearing is completely lost",
    "There is no such threshold relationship. The cochlear and vestibular divisions are affected "
    "independently, and either can dominate the presentation."],
   ["Balance is maintained entirely by vision and proprioception",
    "Vision and proprioception contribute substantially and help compensate, which is why symptoms "
    "worsen in the dark or on uneven ground, but the vestibular system is not dispensable."]],
  "mechanism", D, 105),

Q("Meniere disease", IO,
  "A patient asks which frequencies are affected earliest in Meniere disease.",
  [["Low frequencies",
    "Correct. The distension of endolymphatic hydrops is greatest at the cochlear apex, which is the "
    "region that codes low frequencies, so the early audiogram shows a low-frequency sensorineural "
    "loss that fluctuates. That pattern distinguishes it from almost every other sensorineural cause, "
    "which start high."],
   ["High frequencies",
    "High-frequency loss is the pattern of presbycusis, noise damage and ototoxicity, all of which "
    "affect the cochlear base first. Meniere is the notable exception and is often identified by "
    "that difference."],
   ["All frequencies equally",
    "A flat loss across frequencies suggests a conductive problem or advanced disease. Early Meniere "
    "has a characteristic shape rather than a uniform reduction."],
   ["Only frequencies above 8000 hertz",
    "Loss confined to the extreme high frequencies is an early feature of ototoxicity and is often "
    "outside the range of routine audiometry. It is not the Meniere pattern."]],
  "finding", D, 76),

Q("Vestibular neuronitis", IO,
  "A 40-year-old man with vestibular neuronitis asks how long the vertigo will last and what he "
  "should do.",
  [["It settles over days to weeks; move about rather than lie still",
    "Correct. The condition is benign and self-limiting, and recovery depends on central "
    "compensation, which is driven by vestibular activity. Prolonged bed rest and continued "
    "vestibular suppressants both delay that process, so early mobilisation is what shortens the "
    "illness."],
   ["It is permanent and requires surgical treatment",
    "There is nothing to operate on and the natural history is recovery. Framing a self-limiting "
    "illness as permanent would cause unnecessary alarm and lead to inappropriate referral."],
   ["Take vestibular suppressants continuously for several weeks",
    "Suppressants are useful for the first day or two when nausea and vertigo are severe, but "
    "prolonged use blunts the very signals the brain needs to recalibrate and lengthens recovery."],
   ["Remain on strict bed rest until symptoms resolve completely",
    "Rest feels better in the short term but is counterproductive. Immobility deprives the central "
    "compensation mechanism of the input it needs, so symptoms persist longer."]],
  "treatment", D, 93),

Q("Noise-induced hearing loss", IO,
  "An audiogram of a 45-year-old factory worker shows a notch at 4000 hertz with recovery at 8000 "
  "hertz.",
  [["Noise-induced hearing loss",
    "Correct. Cumulative noise exposure classically produces a notch centred around 4000 hertz with "
    "some recovery at higher frequencies, which is what distinguishes it from presbycusis. "
    "Presbycusis declines progressively as frequency rises and does not recover, so the shape of the "
    "curve rather than its depth makes the diagnosis."],
   ["Presbycusis",
    "Age-related loss slopes downward with increasing frequency and keeps going, with no recovery at "
    "8000 hertz. It would also be early at 45 in the absence of other factors."],
   ["Ototoxicity",
    "Drug-induced loss affects the highest frequencies first and progresses downward, so it produces "
    "a sloping curve rather than an isolated notch, and it requires an exposure history."],
   ["Meniere disease",
    "Meniere gives a fluctuating LOW-frequency loss with episodic vertigo, tinnitus and fullness, "
    "which is essentially the opposite audiometric pattern."]],
  "finding", D, 44),

Q("Sudden sensorineural hearing loss", IO,
  "A clinician explains why sudden sensorineural hearing loss is investigated with imaging even "
  "when it appears idiopathic.",
  [["To exclude a retrocochlear lesion such as a schwannoma",
    "Correct. A proportion of patients presenting with sudden loss turn out to have a vestibular "
    "schwannoma, and the presentation gives no reliable way to identify them clinically. Because a "
    "tumour's size at diagnosis determines the treatment options and the chance of preserving "
    "hearing and facial nerve function, imaging is done rather than assumed unnecessary."],
   ["To confirm the loss is genuinely sensorineural",
    "That distinction is made by tuning forks and audiometry, which are quicker and cheaper. Imaging "
    "answers a different question about what is causing it."],
   ["To assess the degree of hearing loss",
    "Degree of loss is quantified by audiometry in decibels. Imaging shows structure rather than "
    "function and cannot measure a threshold."],
   ["To plan cochlear implantation",
    "Implantation is considered much later and only in profound bilateral loss that does not respond "
    "to treatment. Imaging at presentation is diagnostic rather than surgical planning."]],
  "testing", D, 68),

Q("Tinnitus red flags", IO,
  "A clinician lists the features of tinnitus that require investigation.",
  [["Unilateral or pulsatile",
    "Correct. Most tinnitus is a bilateral non-pulsatile ringing accompanying symmetrical hearing "
    "loss and needs no imaging. Unilaterality raises the possibility of an asymmetric lesion such as "
    "a schwannoma, and pulsatility suggests turbulent blood flow or a vascular middle ear mass such "
    "as a glomus tumour."],
   ["High-pitched or low-pitched quality",
    "Patients describe the pitch in many ways and it carries little diagnostic weight, beyond the "
    "low roaring quality often reported in Meniere disease. It is not a red flag on its own."],
   ["Present for more than six months",
    "Duration alone does not indicate danger. Chronic bilateral tinnitus with matching hearing loss "
    "is the commonest presentation and remains benign however long it lasts."],
   ["Worse at night",
    "Almost all tinnitus is more noticeable in quiet surroundings, because there is less competing "
    "sound to mask it. That is a universal feature rather than a warning sign."]],
  "finding", D, 40),

Q("Hearing loss in children", IO,
  "A clinician explains why untreated conductive hearing loss matters more in a toddler than in an "
  "adult.",
  [["Language acquisition depends on hearing during a limited window",
    "Correct. Speech and language develop during a critical period in early childhood, and reduced "
    "auditory input during that window produces delays that persist even after hearing is restored. "
    "An adult with the same conductive loss is inconvenienced; a toddler may lose ground that is "
    "harder to recover, which is why the threshold to intervene is lower."],
   ["Children have more fragile cochlear hair cells",
    "A conductive loss does not involve the hair cells at all; the cochlea is normal and sound is "
    "simply not reaching it. The concern is developmental rather than a difference in cochlear "
    "vulnerability."],
   ["Conductive loss becomes permanent if untreated in children",
    "The conductive component is mechanical and reverses when the effusion clears or the ossicles "
    "are addressed. What may not fully reverse is the developmental consequence."],
   ["Children cannot tolerate hearing aids",
    "Children are fitted with hearing aids successfully and routinely when indicated. Tolerance is "
    "not the issue driving earlier intervention."]],
  "mechanism", D, 30),

Q("Perilymphatic fistula", IO,
  "A patient with a suspected perilymphatic fistula is advised about initial management.",
  [["Bed rest with head elevation and avoidance of straining",
    "Correct. The leak is pressure-dependent, which is why symptoms worsen with coughing, lifting "
    "and straining. Reducing the pressure gradient by resting with the head up gives the ruptured "
    "window membrane a chance to seal, and many fistulae close spontaneously with that alone before "
    "surgical repair is considered."],
   ["Vigorous vestibular rehabilitation exercises",
    "Rehabilitation drives central compensation and is right for a stable deficit such as vestibular "
    "neuronitis. Here it would repeatedly raise pressure and reopen a membrane that is trying to "
    "heal."],
   ["Immediate surgical exploration in all cases",
    "Exploration is reserved for patients who fail conservative management or who have progressive "
    "hearing loss, because a proportion seal on their own with rest."],
   ["Long-term vestibular suppressants",
    "Suppressants mask the symptom without addressing the leak, and prolonged use impairs the "
    "compensation that helps once the fistula has closed."]],
  "treatment", D, 60),

Q("Presbycusis", IO,
  "A 79-year-old woman with presbycusis is reluctant to try hearing aids because her hearing loss "
  "is not painful and she has managed so far.",
  [["Untreated loss is associated with social withdrawal and cognitive decline",
    "Correct. The consequences of age-related loss extend beyond the audiogram: reduced auditory "
    "input contributes to social isolation, depression and accelerated cognitive decline. Framing "
    "amplification as a way of protecting those things, rather than as a device for hearing better, "
    "is usually what shifts the conversation."],
   ["Hearing aids will restore hearing to normal",
    "Amplification improves audibility but cannot restore the cochlea's ability to discriminate "
    "speech from noise, so overpromising leads to disappointment and abandoned devices."],
   ["Without aids the loss will progress more quickly",
    "The rate of cochlear ageing is not altered by whether a hearing aid is worn. Overstating this "
    "misrepresents the mechanism and risks the patient losing trust in the advice."],
   ["The loss will eventually become painful",
    "Sensorineural loss is painless throughout, and suggesting otherwise is simply inaccurate. Pain "
    "in the ear points to a different pathology altogether."]],
  "treatment", D, 27),

Q("Glomus tumour", IO,
  "A student asks what cranial nerve deficits might accompany a glomus tumour of the jugular "
  "foramen.",
  [["Cranial nerves nine, ten and eleven",
    "Correct. The glossopharyngeal, vagus and spinal accessory nerves all pass through the jugular "
    "foramen, so a tumour arising there compresses them together. That produces difficulty "
    "swallowing, hoarseness and shoulder weakness alongside the pulsatile tinnitus and conductive "
    "loss from the middle ear component."],
   ["Cranial nerves three, four and six",
    "Those are the ocular motor nerves and pass through the superior orbital fissure and cavernous "
    "sinus. They are nowhere near the jugular foramen."],
   ["Cranial nerve seven alone",
    "The facial nerve runs through the temporal bone and can be involved by an extensive middle ear "
    "lesion, but it exits at the stylomastoid foramen rather than the jugular foramen, so it is not "
    "the characteristic group."],
   ["Cranial nerves five and six",
    "The trigeminal and abducens are related to the cavernous sinus and petrous apex. Their "
    "involvement suggests a lesion there, such as in Gradenigo syndrome, rather than at the jugular "
    "bulb."]],
  "finding", D, 51),

Q("Autoimmune hearing loss", IO,
  "A 42-year-old woman with rapidly progressive bilateral sensorineural loss is suspected of having "
  "autoimmune inner ear disease.",
  [["A trial of systemic corticosteroids",
    "Correct. Autoimmune inner ear disease is one of the few sensorineural losses that responds to "
    "treatment, and the response to systemic corticosteroids serves as both therapy and a diagnostic "
    "test, since the condition is otherwise hard to confirm. That responsiveness is the reason it "
    "must be considered before a bilateral progressive loss is written off."],
   ["Hearing aids alone",
    "Amplification will be needed regardless, but fitting aids without trialling immunosuppression "
    "accepts a loss that might have been arrested. The order of steps matters here."],
   ["Immediate cochlear implantation",
    "Implantation is considered for profound bilateral loss that has not responded to treatment. "
    "Proceeding before a steroid trial forecloses the possibility of preserving residual hearing."],
   ["Observation with repeat audiometry in a year",
    "A year of watching a rapidly progressive bilateral loss allows irreversible damage in a "
    "condition where early treatment can preserve function."]],
  "treatment", D, 64),

Q("Functional hearing loss", IO,
  "A clinician suspects non-organic hearing loss and wants an objective test that does not depend "
  "on the patient's cooperation.",
  [["Auditory brainstem response testing",
    "Correct. Brainstem response recording measures the electrical activity generated along the "
    "auditory pathway in response to sound, so it produces a threshold estimate without the patient "
    "having to report anything. That makes it the way to resolve a discrepancy between claimed and "
    "demonstrated hearing."],
   ["Repeat pure tone audiometry",
    "Pure tone testing is behavioural and requires the patient to indicate when they hear a tone, "
    "which is precisely the step in question. Repeating it produced the inconsistency in the first "
    "place."],
   ["Tympanometry",
    "Tympanometry is objective but measures middle ear compliance rather than hearing. It would be "
    "normal in both genuine sensorineural loss and non-organic loss, so it cannot distinguish them."],
   ["Weber and Rinne testing",
    "Tuning fork tests are quick and useful but still depend on the patient reporting what they "
    "hear, so they carry the same limitation as behavioural audiometry."]],
  "testing", D, 118),

Q("Vertigo triage", IO,
  "A clinician is taught which features of acute vertigo should raise concern for a central cause.",
  [["Headache, ataxia out of proportion, or focal neurological signs",
    "Correct. Peripheral vertigo produces unidirectional nystagmus and unsteadiness that still "
    "allows the patient to sit and walk with support. Severe truncal ataxia, headache, "
    "direction-changing nystagmus or any focal deficit such as diplopia, dysarthria or facial "
    "numbness point to the brainstem or cerebellum and require urgent imaging."],
   ["Severity of the vertigo itself",
    "Peripheral causes such as vestibular neuronitis produce some of the most dramatic vertigo seen, "
    "so intensity is a poor discriminator. It is the accompanying signs that localise the lesion."],
   ["Presence of nausea and vomiting",
    "Vomiting accompanies vertigo of any cause because of vestibular connections to the emetic "
    "centre. Its presence says nothing about where the problem is."],
   ["Whether the vertigo is worse on head movement",
    "Almost all vertigo worsens with head movement, peripheral or central, because movement "
    "stimulates a system that is already mismatched. That is different from vertigo TRIGGERED by "
    "position, which suggests otoconia."]],
  "finding", D, 97),
]
