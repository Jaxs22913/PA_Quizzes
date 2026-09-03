# -*- coding: utf-8 -*-
"""CMS I Exam 3, Lecture 16 (Inner Ear, Balance, Hearing Loss) -- objective set A.

The hearing-loss patterns and the tests: Weber and Rinne, audiometry,
tympanometry and vestibular testing. These are syllabus objectives b through f
in their own right, not merely background.

THIS IS THE HIGHEST-CONFIDENCE MATERIAL IN THE BLOCK. Objective c -- apply
Weber and Rinne findings to sensorineural and conductive hearing loss -- is a
named syllabus objective AND the one the lecturer stopped on to say a test
question like it exists. Both directions are written: given a diagnosis, name
the findings; and given the findings, name the diagnosis.

The severity bands were flagged as a chart to know outright, with the mnemonic
that it is all by twenties. The prevalence percentages were explicitly cut --
"you don't have to memorize these statistics" -- so none are asked here.

FIVE options. Correct answer authored FIRST; cms_e3_partition.py rotates it.
"""
D = "16. Disorders of Inner Ear 2026 - Dr. Jaquith.pptx, Slide %d"
IO_A = ("a — Inner ear, balance and hearing loss conditions: etiologies, epidemiology, risk "
        "factors, clinical manifestations, differential diagnosis, diagnostic testing, "
        "management, referrals, patient education, prognosis")
IO_B = "b — Explain the difference between Weber and Rinne testing"
IO_C = "c — Apply Weber and Rinne findings to sensorineural and conductive hearing loss"
IO_D = "d — Explain how to interpret an audiogram and tympanogram"
IO_E = "e — Describe vestibular testing and indications for ordering vestibular testing"
IO_F = "f — Interpret results of vestibular testing"

QUESTIONS = [
 # ------------------- the two patterns -------------------
 dict(topic="Conductive hearing loss", io=IO_A, lead="mechanism", cite=D % 10,
  q="Which four mechanisms produce conductive hearing loss?",
  opts=[["Obstruction, mass loading, stiffness and discontinuity", "Correct."],
        ["Hair cell loss, nerve damage, ageing and noise", "Those produce sensorineural loss."],
        ["Infection, allergy, trauma and tumour", "These are causes rather than the four mechanisms."],
        ["Pressure, temperature, humidity and altitude", "None of these is a described mechanism."],
        ["Genetic, autoimmune, vascular and metabolic", "These are aetiological categories, not the mechanisms."]]),

 dict(topic="Conductive hearing loss", io=IO_A, lead="defining feature", cite=D % 11,
  q="Which conductive cause is characteristically NOT visible on otoscopy?",
  opts=[["Otosclerosis", "Correct — the drum looks normal, which is what makes it distinctive."],
        ["Cerumen impaction", "Wax is plainly visible in the canal."],
        ["Foreign body", "The object is visible."],
        ["Tympanic membrane perforation", "The defect is visible."],
        ["Exostosis", "Bony canal growths are visible."]]),

 dict(topic="Conductive hearing loss", io=IO_A, lead="defining feature", cite=D % 42,
  q="A conductive hearing loss characteristically produces which effect on the patient's own voice?",
  opts=[["The voice stays soft", "Correct — the inner ear and nerve are intact, so the patient hears themselves well."],
        ["The voice becomes loud", "That happens in sensorineural loss."],
        ["The voice becomes hoarse", "Voice quality is not affected in that way."],
        ["The voice becomes high-pitched", "Pitch is not affected."],
        ["The voice is lost entirely", "Speech production is unaffected."]]),

 dict(topic="Conductive hearing loss", io=IO_A, lead="epidemiology", cite=D % 11,
  q="At what stage of life does conductive hearing loss typically begin?",
  opts=[["Childhood to about age forty", "Correct."],
        ["After age sixty-five only", "That fits age-related sensorineural loss."],
        ["Only in the neonatal period", "Onset is not restricted to newborns."],
        ["Only after age eighty", "Two decades past the usual upper limit."],
        ["Only in the seventh decade", "That is when sensorineural loss becomes common, not conductive."]]),

 dict(topic="Sensorineural hearing loss", io=IO_A, lead="mechanism", cite=D % 12,
  q="Why are sensory and neural hearing loss grouped together as one category?",
  opts=[["They are difficult to separate clinically", "Correct."],
        ["They have the same treatment", "Treatment is not the reason for grouping."],
        ["They occur only together", "They can occur independently."],
        ["They affect the same single structure", "They affect different structures."],
        ["They are both fully reversible", "Neither is typically reversible."]]),

 dict(topic="Sensorineural hearing loss", io=IO_A, lead="defining feature", cite=D % 42,
  q="How does background noise affect a patient with sensorineural hearing loss?",
  opts=[["Hearing gets worse", "Correct."],
        ["Hearing gets better", "That is characteristic of otosclerosis, a conductive cause."],
        ["Hearing is unchanged", "Noise makes a real difference in this pattern."],
        ["Only high tones improve", "High tones are the ones already lost in this pattern."],
        ["Only low tones improve", "Noise masks low tones rather than improving them."]]),

 dict(topic="Sensorineural hearing loss", io=IO_A, lead="defining feature", cite=D % 13,
  q="Which frequencies are lost first in sensorineural hearing loss, and with what result?",
  opts=[["The higher registers, so sound becomes distorted", "Correct."],
        ["The lower registers, so sound becomes muffled", "Low-frequency loss is characteristic of a different condition."],
        ["All frequencies equally, so sound becomes quieter", "The loss is not uniform."],
        ["Only the middle registers", "Not the described pattern."],
        ["No particular frequency", "There is a clear pattern."]]),

 dict(topic="Sensorineural hearing loss", io=IO_A, lead="treatment", cite=D % 13,
  q="Which sensorineural hearing loss may respond to corticosteroids?",
  opts=[["Acute-onset loss, within the first weeks", "Correct."],
        ["Loss present for over a year", "The window has long closed."],
        ["Gradual age-related loss", "Steroids do not reverse it."],
        ["Loss caused by wax", "That is conductive and cleared by removal."],
        ["Loss caused by a perforated drum", "That is conductive."]]),

 # ------------------- Weber and Rinne -------------------
 dict(topic="Weber and Rinne", io=IO_B, lead="diagnostic technique", cite=D % 39,
  q="What does the Weber test compare?",
  opts=[["Bone conduction between the two ears", "Correct — a tuning fork on the midline, asking which side is louder."],
        ["Air against bone conduction in one ear", "That is the Rinne test."],
        ["Loudness against a reference tone", "That is not what either test does."],
        ["Middle ear pressure against ambient", "That is tympanometry."],
        ["Speech discrimination between ears", "That is a separate audiometric measure."]]),

 dict(topic="Weber and Rinne", io=IO_B, lead="diagnostic technique", cite=D % 40,
  q="What does the Rinne test compare?",
  opts=[["Air conduction against bone conduction in one ear", "Correct."],
        ["Bone conduction between the two ears", "That is the Weber test."],
        ["Hearing at different frequencies", "That is audiometry."],
        ["Tympanic membrane compliance", "That is tympanometry."],
        ["Vestibular response to head turning", "That is vestibular testing."]]),

 dict(topic="Weber and Rinne", io=IO_C, lead="defining feature", cite=D % 42,
  q="In a unilateral conductive hearing loss, where does the Weber test lateralise?",
  opts=[["To the affected ear", "Correct."],
        ["To the unaffected ear", "That happens in sensorineural loss."],
        ["To neither ear", "It lateralises in a unilateral loss."],
        ["To both ears equally", "That is the normal result."],
        ["It varies with frequency", "Lateralisation does not vary that way."]]),

 dict(topic="Weber and Rinne", io=IO_C, lead="defining feature", cite=D % 42,
  q="In a unilateral sensorineural hearing loss, where does the Weber test lateralise?",
  opts=[["To the unaffected ear", "Correct — away from the bad side."],
        ["To the affected ear", "That happens in conductive loss."],
        ["To neither ear", "It lateralises in a unilateral loss."],
        ["To both ears equally", "That is the normal result."],
        ["It varies with the tuning fork used", "The result does not depend on that."]]),

 dict(topic="Weber and Rinne", io=IO_C, lead="defining feature", cite=D % 42,
  q="Which Rinne result indicates a conductive hearing loss?",
  opts=[["Bone conduction equal to or greater than air conduction", "Correct."],
        ["Air conduction greater than bone conduction", "That is the normal result, and it also occurs in sensorineural loss."],
        ["No response to either", "That indicates profound loss rather than a conductive pattern."],
        ["Equal loudness in both ears", "That is a Weber finding, not a Rinne one."],
        ["A response only at high frequencies", "Rinne is not scored by frequency."]]),

 dict(topic="Weber and Rinne", io=IO_C, lead="defining feature", cite=D % 42,
  q="Why does the Weber test carry the diagnosis when a sensorineural loss is suspected?",
  opts=[["The Rinne result is the same as normal", "Correct — air conduction still beats bone, so only Weber distinguishes it."],
        ["The Rinne test cannot be performed", "It can be performed."],
        ["The Rinne test is less accurate at low frequencies", "That is not the reason."],
        ["The Weber test measures air conduction", "The Weber test uses bone conduction."],
        ["The Rinne test only works in children", "It is used at all ages."]]),

 dict(topic="Weber and Rinne", io=IO_C, lead="diagnosis", cite=D % 42,
  q="A tuning fork placed on the forehead is heard loudest in the right ear, and in that ear bone conduction exceeds air conduction. What does this indicate?",
  opts=[["A right conductive hearing loss", "Correct."],
        ["A right sensorineural hearing loss", "Weber would lateralise away from that ear."],
        ["A left conductive hearing loss", "Weber lateralises toward the conductive side, which is the right."],
        ["A left sensorineural hearing loss", "A sensorineural loss leaves air conduction beating bone; here bone beats air, so the loss is conductive."],
        ["Normal hearing in both ears", "Normal ears give no lateralisation and air conduction greater than bone."]]),

 dict(topic="Weber and Rinne", io=IO_C, lead="diagnosis", cite=D % 42,
  q="A tuning fork on the forehead is heard loudest in the left ear, and in the right ear air conduction exceeds bone conduction. What does this indicate?",
  opts=[["A right sensorineural hearing loss", "Correct — Weber lateralises away from the affected side, and Rinne stays normal."],
        ["A right conductive hearing loss", "Weber would lateralise toward the right and bone would beat air."],
        ["A left conductive hearing loss", "Weber lateralising to the left with a conductive cause would show bone beating air on the left."],
        ["Bilateral wax impaction", "That would be conductive and would not lateralise this way."],
        ["Normal hearing", "Normal ears give no lateralisation."]]),

 # ------------------- audiometry -------------------
 dict(topic="Audiometry", io=IO_D, lead="defining feature", cite=D % 19,
  q="Which decibel range defines normal hearing?",
  opts=[["Zero to twenty", "Correct — and the whole scale then runs in twenties."],
        ["Zero to ten", "The band is wider than that."],
        ["Zero to forty", "That range extends into mild loss."],
        ["Twenty to forty", "That band defines mild loss."],
        ["Forty to sixty", "That band defines moderate loss."]]),

 dict(topic="Audiometry", io=IO_D, lead="defining feature", cite=D % 19,
  q="A hearing loss measured at fifty decibels falls into which category?",
  opts=[["Moderate", "Correct — forty to sixty decibels."],
        ["Mild", "Mild runs from twenty to forty."],
        ["Severe", "Severe runs from sixty to eighty."],
        ["Profound", "Profound is above eighty."],
        ["Normal", "Normal is zero to twenty."]]),

 dict(topic="Audiometry", io=IO_D, lead="defining feature", cite=D % 19,
  q="At what threshold is hearing loss classified as profound?",
  opts=[["Above eighty decibels", "Correct."],
        ["Above forty decibels", "That is the boundary into moderate loss."],
        ["Above sixty decibels", "That is the boundary into severe loss."],
        ["Above one hundred decibels", "Higher than the accepted threshold."],
        ["Above twenty decibels", "That is the boundary into mild loss."]]),

 dict(topic="Audiometry", io=IO_D, lead="defining feature", cite=D % 19,
  q="Which audiogram shape is characteristic of age-related hearing loss?",
  opts=[["A curve sloping downward at high frequencies", "Correct."],
        ["A flat line across all frequencies", "That is not the characteristic shape."],
        ["A curve sloping downward at low frequencies", "Low-frequency loss belongs to a different condition."],
        ["A notch confined to one mid frequency", "Not the described pattern."],
        ["An upward slope at high frequencies", "That reverses the pattern."]]),

 dict(topic="Audiometry", io=IO_D, lead="diagnostic technique", cite=D % 8,
  q="Which audiometric test presents single tones at set frequencies to find the softest audible level?",
  opts=[["Pure tone audiometry", "Correct."],
        ["Tympanometry", "That measures middle ear compliance."],
        ["Electronystagmography", "That assesses vestibular function."],
        ["Otoacoustic emissions", "A different measure of cochlear function."],
        ["The Dix-Hallpike manoeuvre", "That provokes positional vertigo."]]),

 # ------------------- tympanometry -------------------
 dict(topic="Tympanometry", io=IO_D, lead="defining feature", cite=D % 25,
  q="Which tympanogram type indicates a normal middle ear?",
  opts=[["Type A", "Correct."],
        ["Type B", "That flat trace indicates fluid or a perforation."],
        ["Type C", "That indicates negative middle ear pressure."],
        ["Type As", "That indicates stiffness, such as a fixed stapes."],
        ["Type Ad", "That indicates excessive compliance."]]),

 dict(topic="Tympanometry", io=IO_D, lead="defining feature", cite=D % 26,
  q="A flat tympanogram with no pressure peak fits which finding?",
  opts=[["Fluid in the middle ear", "Correct — a type B trace."],
        ["A normal middle ear", "That gives a type A trace."],
        ["Negative middle ear pressure", "That gives a type C trace."],
        ["A fixed stapes", "That gives a shallow type As trace."],
        ["A disarticulated ossicular chain", "That gives a deep type Ad trace."]]),

 dict(topic="Tympanometry", io=IO_D, lead="defining feature", cite=D % 27,
  q="A tympanogram with its peak shifted toward negative pressure indicates what?",
  opts=[["Negative middle ear pressure", "Correct — a type C trace, fitting eustachian tube dysfunction."],
        ["Middle ear fluid", "That gives a flat type B trace."],
        ["Ossicular fixation", "That gives a shallow type As trace."],
        ["Ossicular discontinuity", "That gives a deep type Ad trace."],
        ["A normal middle ear", "That peaks at atmospheric pressure."]]),

 dict(topic="Tympanometry", io=IO_D, lead="defining feature", cite=D % 28,
  q="A shallow tympanogram with normal pressure and low compliance suggests which conditions?",
  opts=[["Ossicular fixation or tympanosclerosis", "Correct — a type As trace, the S standing for shallow or stiff."],
        ["Middle ear fluid", "That gives a flat type B trace."],
        ["Eustachian tube dysfunction", "That gives a type C trace."],
        ["Ossicular discontinuity", "That gives a deep type Ad trace."],
        ["A perforated drum", "That gives a flat trace."]]),

 dict(topic="Tympanometry", io=IO_D, lead="defining feature", cite=D % 29,
  q="A deep tympanogram with high compliance and normal pressure suggests which conditions?",
  opts=[["Ossicular discontinuity or a monomeric drum", "Correct — a type Ad trace, the D standing for deep or disarticulated."],
        ["Ossicular fixation", "That gives a shallow type As trace."],
        ["Middle ear fluid", "That gives a flat type B trace."],
        ["Negative middle ear pressure", "That gives a type C trace."],
        ["A normal middle ear", "That gives a standard type A trace."]]),

 # ------------------- vestibular testing -------------------
 dict(topic="Vestibular testing", io=IO_E, lead="diagnostic technique", cite=D % 74,
  q="Which vestibular study is the gold standard for disorders affecting one ear at a time?",
  opts=[["Electronystagmography", "Correct."],
        ["Pure tone audiometry", "That measures hearing rather than balance."],
        ["Tympanometry", "That measures middle ear compliance."],
        ["Computed tomography", "Imaging does not test vestibular function."],
        ["The Rinne test", "That measures hearing, not balance."]]),

 dict(topic="Vestibular testing", io=IO_F, lead="diagnostic technique", cite=D % 93,
  q="Which manoeuvre provokes and identifies benign paroxysmal positional vertigo?",
  opts=[["The Dix-Hallpike manoeuvre", "Correct — it is diagnosed by the classic eye movements it produces."],
        ["The Epley manoeuvre", "That is the treatment, not the diagnostic test."],
        ["The Weber test", "That compares bone conduction between the ears."],
        ["The Rinne test", "That compares air with bone conduction in one ear."],
        ["Insufflation", "That assesses drum mobility."]]),

 dict(topic="Vestibular testing", io=IO_A, lead="diagnostic technique", cite=D % 75,
  q="Which imaging study is the gold standard for evaluating a suspected retrocochlear cause of hearing loss?",
  opts=[["Magnetic resonance imaging with gadolinium", "Correct."],
        ["Computed tomography without contrast", "Not the study named for retrocochlear assessment."],
        ["Plain radiography", "It lacks the necessary detail."],
        ["Ultrasound", "Bone blocks the sound beam."],
        ["Tympanometry", "That assesses the middle ear only."]]),

 dict(topic="Hearing screening", io=IO_A, lead="next step", cite=D % 60,
  q="From what age is hearing screened routinely in primary care?",
  opts=[["Sixty-five", "Correct."],
        ["Forty", "Twenty-five years before routine screening begins."],
        ["Fifty", "Fifteen years before routine screening begins."],
        ["Seventy-five", "Screening has already been under way for a decade by then."],
        ["Eighty", "Fifteen years after screening should have started."]]),
]
