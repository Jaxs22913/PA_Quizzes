# -*- coding: utf-8 -*-
"""CMS I Exam 3, Lecture 17 -- vignette set C, the corrective pool.

Sets A and B came to 50 between them, and two 30-question forms need 60. Per
[[cms_exam_spec]] the response to a short set is a corrective pool D rather
than a rewrite, so this is that pool for Lecture 17.

Deliberately weighted to the topics the first two pools left thin -- the
elderly and adolescent populations named in objective b, and the education
lead-in -- and written SHORT so it lowers rather than raises the set's
length-gameability.
"""
D = "hughie Nose & Paranasal Sinuses fall 2026.pptx, Slide %d"
IO_A = ("a — Nose and paranasal sinus disorders: etiologies, epidemiology, risk factors, clinical "
        "manifestations, differential diagnosis, diagnostic testing, management, referrals, "
        "patient education, prognosis")
IO_B = ("b — Identify medical care strategies for nose and paranasal sinus disorders by "
        "population: adolescent, adult, elderly")

QUESTIONS = [
 dict(topic="Acute sinusitis", io=IO_B, lead="next step", cite=D % 22,
  q="A 15-year-old boy has three days of congestion and mild facial pressure after a cold, with no fever and no reproducible tenderness. What is appropriate?",
  opts=[["Symptomatic treatment", "Correct. Most episodes are viral and settle without antibiotics."],
        ["Oral antibiotics", "Nothing here suggests bacterial disease."],
        ["Sinus imaging", "Not indicated in a first, early episode."],
        ["ENT referral", "Referral follows medical failure."],
        ["Oral steroids", "Not first-line care."]]),

 dict(topic="Bacterial sinusitis", io=IO_B, lead="diagnosis", cite=D % 16,
  q="A 71-year-old woman has had sinus symptoms for eleven days with unrelenting purulent discharge and left cheek tenderness. What does this suggest?",
  opts=[["Bacterial sinusitis", "Correct &mdash; over ten days, purulent, and unilaterally tender."],
        ["Viral rhinosinusitis", "The duration and unilateral tenderness argue against it."],
        ["Allergic rhinitis", "That gives clear bilateral discharge."],
        ["A nasal foreign body", "That occurs in young children."],
        ["Nasal polyps", "Those obstruct without acute tenderness."]]),

 dict(topic="Epistaxis", io=IO_B, lead="patient education", cite=D % 50,
  q="A 79-year-old man has frequent winter nosebleeds and a very dry nose. What advice addresses the underlying risk?",
  opts=[["Humidify and keep the nose moist", "Correct &mdash; chronic dry nose is a named risk factor."],
        ["Take daily aspirin", "Aspirin promotes bleeding."],
        ["Blow the nose regularly", "That provokes bleeding."],
        ["Use a decongestant spray daily", "Chronic use is cautioned against."],
        ["Sleep flat", "Position does not address dryness."]]),

 dict(topic="Septal haematoma", io=IO_B, lead="prognosis", cite=D % 41,
  q="A 17-year-old rugby player has an undrained septal haematoma. What is the concern?",
  opts=[["Cartilage damage", "Correct &mdash; the collection separates cartilage from its blood supply."],
        ["Permanent anosmia", "Not the described risk."],
        ["Hearing loss", "The ear is not involved."],
        ["Malignant change", "Not a described risk."],
        ["Chronic sinusitis", "Not the immediate concern."]]),

 dict(topic="Nasal polyps", io=IO_A, lead="clinical manifestation", cite=D % 60,
  q="A 55-year-old woman with large nasal polyps has lost her sense of smell. What is that symptom called?",
  opts=[["Anosmia", "Correct."],
        ["Hyposmia", "That is reduced, not absent, smell."],
        ["Halitosis", "That is bad breath."],
        ["Rhinorrhoea", "That is a runny nose."],
        ["Epistaxis", "That is bleeding."]]),

 dict(topic="Allergic rhinitis", io=IO_B, lead="treatment", cite=D % 68,
  q="A 14-year-old girl with allergic rhinitis is drowsy on her current antihistamine during school. What is the sensible adjustment?",
  opts=[["A non-drowsy antihistamine by day", "Correct, keeping the sedating one for night if needed."],
        ["Stop all antihistamines", "That leaves the allergy untreated."],
        ["Double the current dose", "That worsens the drowsiness."],
        ["Switch to an antibiotic", "There is no infection."],
        ["Start nasal packing", "That treats bleeding."]]),

 dict(topic="Chronic sinusitis", io=IO_A, lead="defining feature", cite=D % 28,
  q="A 48-year-old man asks how his doctor decided his sinusitis was chronic. What is the threshold?",
  opts=[["Twelve weeks", "Correct."],
        ["Four weeks", "That is the limit of acute disease."],
        ["Two weeks", "Far short of the threshold."],
        ["Six months", "Longer than the threshold."],
        ["One year", "Far longer than the threshold."]]),

 dict(topic="Nasal foreign body", io=IO_B, lead="next step", cite=D % 54,
  q="A 3-year-old boy has a bead visible in the right nostril and is becoming distressed by attempts to look. What is appropriate?",
  opts=[["Refer to ENT", "Correct &mdash; get help rather than risk pushing it deeper."],
        ["Blind sweeping with forceps", "That risks displacing it backwards."],
        ["Irrigation of the nostril", "Not the described technique."],
        ["A course of antibiotics", "That delays removal."],
        ["Reassurance and review in a month", "The object needs removing."]]),

 dict(topic="Deviated septum", io=IO_B, lead="diagnosis", cite=D % 32,
  q="A 68-year-old man has years of one-sided blockage and loud snoring. Examination shows the septum pushed to the left. What is the diagnosis?",
  opts=[["Deviated septum", "Correct."],
        ["Septal perforation", "That is a hole rather than a displacement."],
        ["Nasal polyps", "Those are grey glistening masses."],
        ["Allergic rhinitis", "That is bilateral with clear discharge."],
        ["Chronic sinusitis", "That gives pressure and infective flares."]]),

 dict(topic="Nasopharyngeal carcinoma", io=IO_B, lead="epidemiology", cite=D % 69,
  q="A 54-year-old man is diagnosed with nasopharyngeal carcinoma. How does incidence differ between the sexes?",
  opts=[["Two to threefold higher in males", "Correct."],
        ["Equal in both", "There is a clear male predominance."],
        ["Twice as high in females", "That reverses the pattern."],
        ["Ten times higher in males", "Higher than the stated ratio."],
        ["It occurs only in males", "It occurs in both."]]),
]
