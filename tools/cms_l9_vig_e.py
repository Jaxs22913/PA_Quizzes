# -*- coding: utf-8 -*-
# CMS I Lecture 9 — SET 2, vignette pool E. NON-DIAGNOSIS LEAD-INS ONLY.
#
# WHY THIS EXISTS. On 24 August Professor Jaquith described the exam: "there's
# gonna be like clinical vignettes or pretty much all clinical vignettes. There
# might be SOME question, what's the most likely diagnosis, but A LOT OF THEM
# are -- what's the next management plan? What's your first line treatment
# plan? ... what's the proper patient education?"
#
# The vignette partitions now cap diagnosis lead-ins at 6 of 30. Lecture 9's
# pool could not satisfy that: 60 vignettes, 20 of them diagnosis, leaving 40
# non-diagnosis where two sets need 48. The cap failed the build rather than
# shipping a diagnosis-heavy paper, which is what it is for. This pool supplies
# the shortfall.
#
# EVERY LEAD-IN HERE IS next step, treatment, test or education. None is
# diagnosis. Asserted at the bottom of the file so it cannot drift.
SRC = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = "1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis of pre-malignant and malignant cutaneous lesions"
IOB = "11 — Identify medical care strategies for pre-malignant and malignant cutaneous lesions for adult and elderly populations"

VIG_E = [
 dict(topic="Actinic keratosis", io=IOA, lead="next step",
   q="A 74-year-old has had a scaly patch on his temple treated with cryotherapy twice over eight months, and it has come back again. It is now slightly firm to the touch. What is the most appropriate next step?",
   opts=[
     ["Take a shave or punch biopsy, because persistence or recurrence after therapy is a biopsy trigger",
      "Correct — recurrence after treatment, plus induration, is exactly what the deck says should prompt sampling."],
     ["Repeat cryotherapy and review him again in a further three months",
      "A third attempt delays the question the induration and recurrence have already raised."],
     ["Start field therapy with topical fluorouracil across the whole temple",
      "Field therapy treats the surrounding field but would not answer whether this lesion has become invasive."],
     ["Reassure him that recurrence after cryotherapy is expected and that no further action is needed",
      "Recurrence after appropriate therapy is a stated trigger for biopsy, not for reassurance."]],
   c=0, cite=c(13)),

 dict(topic="Actinic keratosis", io=IOA, lead="treatment",
   q="A 68-year-old woman has more than twenty rough scaly papules spread across her forehead, cheeks and nose. Individually they are small and none is indurated. Which treatment approach fits best?",
   opts=[
     ["Field-directed therapy such as topical fluorouracil, imiquimod or photodynamic therapy",
      "Correct — multiple lesions across one anatomic region is field cancerization, which is treated as a field."],
     ["Liquid nitrogen cryotherapy to each lesion in turn at this visit",
      "Lesion-directed cryotherapy suits isolated lesions with clear borders, not a whole affected region."],
     ["Excision of each lesion with a two-millimetre margin",
      "Excision is not the treatment for uncomplicated actinic keratoses."],
     ["Observation alone, since none of the lesions is currently indurated or bleeding",
      "The lesions carry a cumulative field risk that observation does not address."]],
   c=0, cite=c(14)),

 dict(topic="Actinic keratosis", io=IOA, lead="education",
   q="You have just cleared a patient's actinic keratoses with a course of field therapy. She asks whether that is the end of it. What is the most appropriate response?",
   opts=[
     ["Treatment reduces the lesion burden but the surrounding field stays at risk, so surveillance continues",
      "Correct — ongoing surveillance remains necessary despite successful therapy."],
     ["Clearance means the surrounding field is no longer at risk and routine follow-up can stop",
      "The deck states the opposite: the field remains at risk."],
     ["She should return only if a lesion becomes painful or bleeds",
      "Any nonhealing or changing lesion warrants prompt review, and surveillance is scheduled rather than symptom-driven."],
     ["A repeat course every six months will prevent any recurrence",
      "No such prophylactic schedule is described."]],
   c=0, cite=c(15)),

 dict(topic="Squamous cell carcinoma", io=IOA, lead="test",
   q="A 70-year-old transplant recipient has a firm nodule on his lower lip. You are arranging a biopsy. What must the sample allow the pathologist to determine?",
   opts=[
     ["Whether the disease is in situ or invasive, along with the histologic risk features",
      "Correct — sufficient depth is what makes that distinction possible, and it changes everything downstream."],
     ["The Breslow thickness in millimetres, to assign a T category",
      "Breslow thickness belongs to melanoma."],
     ["The histopathologic subtype alone, since that dictates treatment selection",
      "Subtype dictating treatment is the basal cell carcinoma emphasis."],
     ["Whether human herpesvirus 8 is present in the specimen",
      "That supports a Kaposi sarcoma diagnosis."]],
   c=0, cite=c(23)),

 dict(topic="Squamous cell carcinoma", io=IOA, lead="next step",
   q="A 66-year-old woman has a biopsy-proven invasive squamous cell carcinoma of the ear, 1.2 cm across, with perineural invasion on pathology. What is the most appropriate next step?",
   opts=[
     ["Refer for Mohs micrographic surgery, since the site, size and perineural invasion all meet the criteria",
      "Correct — high-risk site, over one centimetre on the face, and aggressive histology each independently qualify."],
     ["Excise it with a four-millimetre margin in the clinic today and review the pathology report",
      "Standard excision does not address the perineural invasion or the high-risk site."],
     ["Begin imiquimod five nights weekly for six to ten weeks",
      "Topical therapy is for selected superficial basal cell carcinoma, not invasive squamous cell carcinoma."],
     ["Start programmed death 1 blockade before any surgery",
      "That is reserved for advanced or metastatic disease."]],
   c=0, cite=c(25)),

 dict(topic="Squamous cell carcinoma", io=IOA, lead="education",
   q="A kidney transplant recipient has had two squamous cell carcinomas removed this year. He asks whether anything can lower his chances of getting more. What do you tell him?",
   opts=[
     ["Nicotinamide five hundred milligrams twice daily reduces new squamous cell carcinoma by about thirty per cent in high-risk patients",
      "Correct — and it is specifically described as a strategy for transplant recipients."],
     ["Niacin five hundred milligrams twice daily reduces new squamous cell carcinoma by about thirty per cent",
      "The deck specifies nicotinamide; niacin is a different form of vitamin B3."],
     ["Nicotinamide five hundred milligrams twice daily reduces new squamous cell carcinoma by about twenty per cent overall",
      "Twenty per cent is the figure for basal cell carcinoma."],
     ["Reducing his immunosuppression is the only measure that lowers his risk",
      "Immunosuppression is coordinated with the transplant team and is not offered as the chemopreventive answer."]],
   c=0, cite=c(21)),

 dict(topic="Basal cell carcinoma", io=IOA, lead="treatment",
   q="A 62-year-old has a biopsy-confirmed superficial basal cell carcinoma on his upper back, with no high-risk features. He would prefer to avoid surgery. Which option is appropriate, and what must follow it?",
   opts=[
     ["Imiquimod five nights weekly for six to ten weeks, with clinical clearance confirmed afterwards",
      "Correct — topical therapy is acceptable for selected superficial disease, but clearance must be verified."],
     ["Imiquimod five nights weekly for six to ten weeks, with no further review needed if the lesion disappears",
      "Visible resolution is not the same as clearance, which the deck requires to be confirmed."],
     ["Fluorouracil twice daily for two weeks, with clinical clearance confirmed afterwards",
      "The duration for fluorouracil here is up to twelve weeks, not two."],
     ["Vismodegib, since it avoids surgery altogether",
      "Hedgehog inhibitors are for advanced or metastatic disease."]],
   c=0, cite=c(37)),

 dict(topic="Basal cell carcinoma", io=IOA, lead="education",
   q="A 58-year-old has just had her first basal cell carcinoma excised. She asks how often she needs to be seen from now on. What is the most appropriate advice?",
   opts=[
     ["At least an annual full-skin examination, because a second basal cell carcinoma develops in up to half of patients",
      "Correct — the up-to-fifty-per-cent second-primary rate is what makes annual review mandatory."],
     ["Review only if she notices a new or changing lesion herself",
      "Scheduled surveillance is required rather than symptom-driven review."],
     ["A full-skin examination every three months for life",
      "The deck sets at least annual, not quarterly."],
     ["No further skin surveillance is needed, since the lesion was completely excised with clear margins",
      "Complete excision does not remove the high risk of a second primary."]],
   c=0, cite=c(38)),
]

# Every lead-in here must be non-diagnosis; that is the entire purpose of the pool.
_bad = [q["q"][:60] for q in VIG_E if q.get("lead") == "diagnosis" or not q.get("lead")]
assert not _bad, ("this pool exists to supply NON-diagnosis vignettes -- a diagnosis or "
                  "untagged lead-in defeats it: %r" % _bad)
