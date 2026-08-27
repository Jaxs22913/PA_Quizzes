# -*- coding: utf-8 -*-
# CMS I Lecture 9 — pool C. Basal cell carcinoma.
# THE SLIDE IS AUTHORITATIVE (Jaquith deck). Correct answer first (c=0).
SRC = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = "1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis of pre-malignant and malignant cutaneous lesions"
IOB = "11 — Identify medical care strategies for pre-malignant and malignant cutaneous lesions for adult and elderly populations"

POOL_C = [
 dict(topic="Basal cell carcinoma", io=IOA, slot="epidemiology",
   q="How common is basal cell carcinoma, and which ultraviolet exposure pattern drives it?",
   opts=[
     ["It is the most common form of cancer, driven by intense, INTERMITTENT ultraviolet exposure in fair-skinned people",
      "Correct — intermittent, unlike the cumulative pattern of squamous cell carcinoma."],
     ["It is the second most common skin cancer, driven by prolonged CUMULATIVE ultraviolet exposure in fair-skinned people",
      "That is squamous cell carcinoma on both counts."],
     ["It is the fourth most common cancer overall, driven by intense intermittent ultraviolet exposure in fair-skinned people",
      "Melanoma is fourth most common overall."],
     ["It is a rare cancer, driven by human herpesvirus 8 in the setting of immune senescence",
      "That describes Kaposi sarcoma."]],
   c=0, cite=c(33)),

 dict(topic="Basal cell carcinoma", io=IOA, slot="etiology",
   q="Which clinical and histologic subtypes of basal cell carcinoma does the deck list, and which determines behaviour?",
   opts=[
     ["Clinical: superficial, nodular, pigmented, morpheaform. Histologic: superficial, nodular, micronodular, infiltrative. The HISTOLOGIC subtype determines behaviour and dictates treatment selection",
      "Correct — histology drives the treatment decision."],
     ["Clinical: superficial, nodular, pigmented, morpheaform. Histologic: superficial, nodular, micronodular, infiltrative. The CLINICAL subtype determines behaviour and dictates treatment selection",
      "The deck gives that role to the histologic subtype."],
     ["Clinical: superficial spreading, nodular, lentigo maligna, acral. Histologic: in situ, invasive, metastatic. The histologic subtype determines behaviour",
      "Those clinical subtypes belong to melanoma."],
     ["Clinical: classic, endemic, iatrogenic, epidemic. Histologic: patch, plaque, tumour. The clinical form determines behaviour",
      "Those forms belong to Kaposi sarcoma."]],
   c=0, cite=c(33)),

 dict(topic="Basal cell carcinoma", io=IOB, slot="complication",
   q="What proportion of patients develop a second basal cell carcinoma, and what does that mandate?",
   opts=[
     ["Up to 50%, which makes at least annual full-skin examination mandatory",
      "Correct — the second-primary risk is what drives surveillance."],
     ["Up to 5%, which makes examination every five years sufficient",
      "The figure is up to 50%."],
     ["Up to 50%, which makes examination every five years sufficient",
      "The figure is right but annual examination is mandated."],
     ["Under 1%, which makes routine surveillance unnecessary after excision",
      "Second primaries are common, not rare."]],
   c=0, cite=c(33)),

 dict(topic="Basal cell carcinoma", io=IOA, slot="agent/regimen",
   q="What chemoprevention does the deck give for basal cell carcinoma, and by how much does it reduce development?",
   opts=[
     ["Nicotinamide 500 mg orally twice daily, reducing basal cell carcinoma development by approximately 20%",
      "Correct — the same drug and dose reduces squamous cell carcinoma by about 30%."],
     ["Nicotinamide 500 mg orally twice daily, reducing basal cell carcinoma development by approximately 30%",
      "30% is the squamous cell carcinoma figure."],
     ["Vismodegib 150 mg orally daily, reducing basal cell carcinoma development by approximately 20%",
      "Vismodegib treats advanced disease rather than preventing new tumours."],
     ["Imiquimod applied five nights weekly, reducing basal cell carcinoma development by approximately 50%",
      "Imiquimod treats selected superficial disease, it is not chemoprevention."]],
   c=0, cite=c(33)),

 dict(topic="Basal cell carcinoma", io=IOA, slot="manifestation",
   q="Describe NODULAR basal cell carcinoma, including the manoeuvre that accentuates its vessels.",
   opts=[
     ["A papule or nodule with central erosion, growing slowly over years to 1 to 2 cm or larger, with a pearly or translucent quality and visible telangiectasias accentuated by STRETCHING the skin",
      "Correct — stretching brings the telangiectasias out."],
     ["A papule or nodule with central erosion, growing rapidly over weeks to 1 to 2 cm or larger, with a pearly quality and telangiectasias accentuated by pressing the lesion firmly",
      "Growth is slow, over years, and the manoeuvre is stretching."],
     ["A reddish shiny scaly thin plaque on the back or chest, growing slowly, with a thready pearly border accentuated by stretching the skin",
      "That describes the superficial subtype."],
     ["A scar-like ivory-white plaque with subtle extension beyond the visible segment, accentuated by stretching the skin",
      "That describes the morpheaform subtype."]],
   c=0, cite=c(35)),

 dict(topic="Basal cell carcinoma", io=IOA, slot="manifestation",
   q="Which basal cell carcinoma subtype is scar-like and carries the highest risk of subclinical spread?",
   opts=[
     ["Morpheaform or sclerosing — a scar-like or ivory-white lesion whose extension beyond the visible pink segment is clinically subtle",
      "Correct — the invisible extension is what makes it high-risk."],
     ["Superficial — a reddish shiny scaly thin plaque whose extension beyond the visible segment is clinically subtle",
      "Superficial disease sits on the back and chest and is not the high-spread subtype."],
     ["Nodular — a pearly papule with central erosion whose extension beyond the visible segment is clinically subtle",
      "Nodular disease has a visible pearly border."],
     ["Pigmented — a stippled lesion whose extension beyond the visible segment is clinically subtle",
      "Pigmented disease mimics melanocytic lesions but is not the high-spread subtype."]],
   c=0, cite=c(35)),

 dict(topic="Basal cell carcinoma", io=IOA, slot="manifestation",
   q="Which warning patterns does the deck give for basal cell carcinoma, and where do they commonly appear?",
   opts=[
     ["A pearly papule, an erythematous patch larger than 6 mm, or a non-healing ulcer — commonly on the face, trunk or lower legs",
      "Correct — three patterns, three common sites."],
     ["A sandpaper-textured papule, a pigmented macule larger than 6 mm, or a warty nodule — commonly on the scalp, ears and dorsal hands",
      "Sandpaper texture describes actinic keratosis."],
     ["A pearly papule, an erythematous patch larger than 6 mm, or a non-healing ulcer — commonly on the palms, soles and nail units",
      "Acral sites belong to melanoma and nail unit disease."],
     ["A violaceous macule, a purple plaque, or an oral lesion — commonly on the hard palate and lower limbs",
      "Those describe Kaposi sarcoma."]],
   c=0, cite=c(35)),

 dict(topic="Basal cell carcinoma", io=IOA, slot="gold standard",
   q="How should a suspected basal cell carcinoma be sampled?",
   opts=[
     ["With a shave or punch biopsy",
      "Correct — the histologic subtype then dictates treatment."],
     ["With a wide local excision carrying 1 cm margins",
      "Excision is treatment, not the diagnostic step."],
     ["With a potassium hydroxide preparation of the surface scale",
      "That test is for fungal elements."],
     ["With a sentinel lymph node biopsy at the time of diagnosis",
      "Sentinel node biopsy belongs to melanoma staging."]],
   c=0, cite=c(36)),

 dict(topic="Basal cell carcinoma", io=IOA, slot="first-line",
   q="Which topical regimens does the deck give for selected superficial basal cell carcinoma?",
   opts=[
     ["Imiquimod five nights weekly for 6 to 10 weeks, or fluorouracil twice daily for up to 12 weeks, with clinical clearance confirmed afterwards",
      "Correct — confirming clearance is part of the regimen."],
     ["Imiquimod twice daily for 6 to 10 weeks, or fluorouracil five nights weekly for up to 12 weeks, with clearance assumed once inflammation settles",
      "The two schedules are swapped and clearance must be confirmed."],
     ["Vismodegib or sonidegib taken orally for 6 to 10 weeks, with clinical clearance confirmed afterwards",
      "Hedgehog inhibitors are reserved for advanced or metastatic disease."],
     ["Liquid nitrogen cryotherapy every two to three weeks for 6 to 10 weeks, with clearance confirmed afterwards",
      "Cryotherapy is not the topical regimen given here."]],
   c=0, cite=c(37)),

 dict(topic="Basal cell carcinoma", io=IOA, slot="escalation",
   q="What does the deck give for ADVANCED or metastatic basal cell carcinoma?",
   opts=[
     ["Hedgehog pathway inhibitors — vismodegib or sonidegib",
      "Correct — reserved for advanced disease or extensive tumour burden."],
     ["Programmed death 1 blockade, or cetuximab",
      "Those belong to advanced squamous cell carcinoma."],
     ["Intralesional vincristine, vinblastine or bleomycin",
      "Those are palliative options in classic Kaposi sarcoma."],
     ["Topical corticosteroid with phototherapy and retinoids",
      "Those are skin-directed options in cutaneous T-cell lymphoma."]],
   c=0, cite=c(37)),

 dict(topic="Basal cell carcinoma", io=IOA, slot="prognosis",
   q="What recurrence and cure figures does the deck give for basal cell carcinoma surgery?",
   opts=[
     ["Excision recurrence rate of 5% or less; Mohs cure rate of about 98%",
      "Correct — Mohs is the higher-cure, tissue-sparing option."],
     ["Excision recurrence rate of about 30%; Mohs cure rate of about 70%",
      "Both figures are far off the deck's."],
     ["Excision recurrence rate of 5% or less; Mohs cure rate of about 80%",
      "The Mohs figure given is about 98%."],
     ["Excision recurrence rate of about 20%; Mohs cure rate of about 98%",
      "The excision figure given is 5% or less."]],
   c=0, cite=c(37)),

 dict(topic="Basal cell carcinoma", io=IOA, slot="escalation",
   q="Which indications does the deck give for Mohs surgery in basal cell carcinoma?",
   opts=[
     ["Eyelids, nasolabial folds, canthi, external ear and temple; recurrent tumours; a tissue-sparing or cosmetic need; and aggressive histology — morpheaform, micronodular or infiltrative",
      "Correct — four groupings, with the histologic subtypes named."],
     ["Eyelids, nasolabial folds, canthi, external ear and temple; recurrent tumours; a tissue-sparing or cosmetic need; and low-risk histology — superficial or nodular disease",
      "Superficial and nodular are the LOW-risk histologies here."],
     ["The trunk, back, chest and shoulders; first presentations only; a purely cosmetic need; and any pigmented lesion whatever its histology",
      "None of these matches the deck's indications."],
     ["Any lesion in a patient over 65; any lesion larger than 6 mm; any lesion present more than a year; and any lesion the patient finds unsightly",
      "Age and duration are not Mohs indications."]],
   c=0, cite=c(37)),

 dict(topic="Basal cell carcinoma", io=IOA, slot="prognosis",
   q="What is the overall prognosis of basal cell carcinoma, and where does its morbidity come from?",
   opts=[
     ["Usually slow-growing and highly curable when treated early; morbidity comes from local destruction, recurrence, delayed diagnosis and anatomically complex sites, with metastatic disease rare but serious",
      "Correct — the danger is local destruction rather than spread."],
     ["Usually rapidly growing and rarely curable even when treated early; morbidity comes chiefly from early distant metastasis to lung and liver, with local destruction uncommon",
      "It is slow-growing and highly curable, and metastasis is rare."],
     ["Usually slow-growing and highly curable when treated early; morbidity comes chiefly from nodal metastasis, which occurs in 3 to 7% of cases, rather than from local destruction",
      "That metastatic rate belongs to squamous cell carcinoma."],
     ["Usually slow-growing but uniformly fatal without systemic therapy; morbidity comes from delayed hedgehog inhibitor treatment rather than from local destruction or recurrence",
      "It is highly curable when treated early."]],
   c=0, cite=c(38)),
]
