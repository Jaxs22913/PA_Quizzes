# -*- coding: utf-8 -*-
# CMS I Lecture 9 — SET 2, vignette pool B. Malignant melanoma.
SRC = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = "Objective 1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis of pre-malignant and malignant cutaneous lesions"
IOB = "Objective 11 — Identify medical care strategies for pre-malignant and malignant cutaneous lesions for adult and elderly populations"

VIG_B = [
 dict(topic="Malignant melanoma", io=IOA, lead="diagnosis",
   q="A 44-year-old shows you a mole on her upper back. One half does not match the other, the edge is notched, and there are brown, black and pink areas within it. It is 8 mm across and she says it has changed this year. Which recognition criteria does this lesion meet?",
   opts=[
     ["Asymmetry, border irregularity, colour variegation, diameter over 6 mm, and evolution — all five",
      "Correct — every element of the mnemonic is present."],
     ["Asymmetry, border irregularity and colour variegation only, since 8 mm is below the diameter threshold",
      "The threshold is 6 mm, so 8 mm exceeds it."],
     ["Border irregularity and evolution only, since colour variation within a lesion is a benign feature",
      "Colour variegation is one of the criteria."],
     ["Diameter and evolution only, since asymmetry and border irregularity are not part of the mnemonic",
      "Both are part of it."]],
   c=0, cite=c(46)),

 dict(topic="Malignant melanoma", io=IOA, lead="next step",
   q="A 39-year-old has a 4 mm pigmented lesion that is asymmetric with an irregular border and has darkened over three months. Which is the most appropriate next step?",
   opts=[
     ["Biopsy or excise it, because smaller lesions can still be melanoma",
      "Correct — the 6 mm figure is a prompt, not a rule-out."],
     ["Reassure and review in a year, because a lesion under 6 mm cannot be melanoma",
      "The deck explicitly warns that smaller lesions can be melanoma."],
     ["Photograph and review in six months, because evolution over three months is too rapid for melanoma",
      "Evolution is itself a criterion for concern."],
     ["Refer for sentinel lymph node biopsy before sampling the lesion",
      "Node biopsy follows diagnosis of the primary."]],
   c=0, cite=c(46)),

 dict(topic="Malignant melanoma", io=IOA, lead="diagnosis",
   q="A 71-year-old man has a rapidly enlarging pink nodule on the shoulder with no pigment at all. It has been present six weeks. Which melanoma subtype should you consider, and why is it dangerous?",
   opts=[
     ["Nodular melanoma — it grows rapidly, is often amelanotic, and may lack the classic recognition features",
      "Correct — the absence of pigment and of the mnemonic features delays diagnosis."],
     ["Superficial spreading melanoma — it grows rapidly, is often amelanotic, and may lack the classic features",
      "That subtype evolves radially and usually shows the classic features."],
     ["Lentigo maligna melanoma — it grows rapidly on chronically sun-exposed skin of older adults",
      "That subtype has a slow radial growth phase."],
     ["Acral lentiginous melanoma — it grows rapidly and is often amelanotic on the palms and soles",
      "That subtype arises on palms, soles and nail units."]],
   c=0, cite=c(41)),

 dict(topic="Malignant melanoma", io=IOA, lead="test",
   q="A melanoma is excised and reported at 1.3 mm Breslow thickness with no ulceration. What does the deck say about sentinel lymph node biopsy here, and what should the patient be told it achieves?",
   opts=[
     ["It should be offered or discussed, since the threshold is 1.0 mm; it is a staging procedure and may not itself improve overall survival",
      "Correct — an honest expectation to set."],
     ["It should be offered or discussed, since the threshold is 1.0 mm; it is a therapeutic procedure that reliably improves overall survival",
      "The deck says it may not improve overall survival."],
     ["It should not be offered, since the threshold is 4.0 mm and this lesion is far below it",
      "The threshold given is 1.0 mm."],
     ["It should not be offered, since sentinel node biopsy is reserved for patients with palpable nodes",
      "It is offered on thickness criteria, not on palpable disease."]],
   c=0, cite=c(51)),

 dict(topic="Malignant melanoma", io=IOA, lead="test",
   q="A 61-year-old's melanoma measures 0.9 mm Breslow thickness, but her report notes ulceration and a high mitotic rate. Which is the most appropriate interpretation?",
   opts=[
     ["Sentinel lymph node biopsy should be offered or discussed, because additional histologic risk factors lower the threshold to 0.8 mm",
      "Correct — ulceration, high mitotic rate and lymphovascular invasion are the three named factors."],
     ["Sentinel lymph node biopsy is not indicated, because the threshold is a fixed 1.0 mm regardless of other features",
      "The threshold drops to 0.8 mm with risk factors."],
     ["Sentinel lymph node biopsy is mandatory, because ulceration alone converts this to advanced disease",
      "It is offered and discussed rather than mandatory, and ulceration does not itself mean advanced disease."],
     ["Sentinel lymph node biopsy should be deferred until the lesion recurs locally after re-excision",
      "It is a staging decision taken at diagnosis."]],
   c=0, cite=c(51)),

 dict(topic="Malignant melanoma", io=IOA, lead="treatment",
   q="A 55-year-old man has a melanoma in situ confirmed on his forearm. Which re-excision margin does the deck give?",
   opts=[
     ["0.5 to 1 cm", "Correct — margins widen with Breslow thickness from there."],
     ["1 to 2 cm", "That margin is for lesions thicker than 1 mm."],
     ["A uniform 1 cm regardless of thickness", "The margin is explicitly thickness-dependent."],
     ["3 to 5 cm", "That is far wider than any margin the deck gives."]],
   c=0, cite=c(52)),

 dict(topic="Malignant melanoma", io=IOA, lead="treatment",
   q="A 63-year-old's melanoma is reported at 1.8 mm Breslow thickness. Which re-excision margin applies, and what else does that thickness trigger?",
   opts=[
     ["A 1 to 2 cm margin, and referral to an expert centre because the lesion is deeper than 1 mm",
      "Correct — the same threshold governs both."],
     ["A 1 cm margin, and referral to an expert centre because the lesion is deeper than 1 mm",
      "A 1 cm margin applies to lesions under 1 mm."],
     ["A 0.5 to 1 cm margin, and routine dermatology follow-up without expert-centre referral",
      "That margin is for in situ disease, and this thickness warrants referral."],
     ["A 1 to 2 cm margin, with referral reserved until nodal disease is demonstrated",
      "Referral is triggered by thickness over 1 mm."]],
   c=0, cite=c(52)),

 dict(topic="Malignant melanoma", io=IOA, lead="education",
   q="A patient treated for melanoma asks what she should be doing between appointments. Which is the most appropriate advice?",
   opts=[
     ["Monthly self-examination using the recognition mnemonic and ugly-duckling principles, including scalp, back, palms, soles and nails",
      "Correct — the sun-protected and acral sites are the ones people skip."],
     ["Monthly self-examination of sun-exposed skin only, since melanoma does not arise on the scalp, back, palms, soles or nails",
      "Acral melanoma is exactly why those sites are named."],
     ["Annual self-examination using the recognition mnemonic and ugly-duckling principles, since more frequent checking causes anxiety",
      "The deck asks for monthly checks."],
     ["No self-examination of any site, since skin surveillance is entirely the specialist team's responsibility",
      "Self-examination is explicitly requested."]],
   c=0, cite=c(56)),

 dict(topic="Malignant melanoma", io=IOA, lead="diagnosis",
   q="You are explaining a 49-year-old woman's melanoma report to her; it gives Breslow thickness, ulceration status and mitotic rate. Which of these does the deck call the dominant prognostic variable?",
   opts=[
     ["Breslow thickness, with ulceration and mitotic activity further modifying stage-based prognosis",
      "Correct — which is why it must be measured accurately at the initial biopsy."],
     ["Ulceration, with Breslow thickness and mitotic activity further modifying prognosis",
      "Ulceration modifies rather than dominates."],
     ["Mitotic rate, with Breslow thickness and ulceration further modifying prognosis",
      "Mitotic activity modifies rather than dominates."],
     ["None of them; the anatomic site of the primary is the dominant prognostic variable",
      "Site is not what the deck names."]],
   c=0, cite=c(55)),

 dict(topic="Malignant melanoma", io=IOB, lead="next step",
   q="A 52-year-old woman has a pigmented lesion excised, reported as melanoma with a positive sentinel node. Which is the most appropriate next step?",
   opts=[
     ["Refer to an expert centre, since nodal spread is an explicit referral trigger and coordinated dermatology and surgical oncology care is warranted",
      "Correct — nodal or other-site spread crosses the threshold regardless of thickness."],
     ["Arrange routine dermatology follow-up, since a positive sentinel node does not alter the management pathway or the referral threshold",
      "Nodal spread is an explicit referral trigger."],
     ["Repeat the sentinel node biopsy to confirm the finding before any referral to an expert centre is made",
      "Repetition is not the described pathway."],
     ["Begin topical imiquimod to the excision site while awaiting further staging and imaging",
      "Topical therapy has no role in nodal melanoma."]],
   c=0, cite=c(52)),

 dict(topic="Malignant melanoma", io=IOB, lead="education",
   q="A 30-year-old Black patient asks whether she needs to worry about melanoma. Which is the most accurate response using the deck's figures?",
   opts=[
     ["Lifetime risk is lower but not zero — about 0.1 to 0.5% in persons of colour against about 2% in white individuals",
      "Correct — lower risk, and acral and nail sites still need checking."],
     ["Lifetime risk is effectively zero in persons of colour, so routine skin checks are unnecessary",
      "The risk is lower but real."],
     ["Lifetime risk is the same in all skin tones, at about 2%",
      "The deck gives distinctly different figures."],
     ["Lifetime risk is higher in persons of colour, at about 2% against 0.1 to 0.5% in white individuals",
      "The two figures are the wrong way round."]],
   c=0, cite=c(40)),
]
