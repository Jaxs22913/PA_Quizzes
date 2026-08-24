# -*- coding: utf-8 -*-
# CMS I Lecture 9 — pool B. Cutaneous squamous cell carcinoma.
# THE SLIDE IS AUTHORITATIVE (Jaquith deck). Correct answer written first (c=0).
# Distractors are written to the answer's shape FROM THE START -- pool A needed
# 36 padding edits afterwards because they were not.
SRC = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = "Objective 1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis of pre-malignant and malignant cutaneous lesions"
IOB = "Objective 11 — Identify medical care strategies for pre-malignant and malignant cutaneous lesions for adult and elderly populations"

POOL_B = [
 dict(topic="Squamous cell carcinoma", io=IOA, slot="epidemiology",
   q="Where does cutaneous squamous cell carcinoma rank among skin cancers, and what usually causes it?",
   opts=[
     ["The second most common form of skin cancer, usually caused by long-term damage from ultraviolet rays from the sun or tanning beds",
      "Correct — and when found early it is almost always curable."],
     ["The most common form of skin cancer, usually caused by intense intermittent ultraviolet exposure in fair-skinned people",
      "That describes basal cell carcinoma, which is the commonest."],
     ["The fourth most common cancer overall, usually caused by human herpesvirus 8 in an immunosuppressed host",
      "Melanoma is fourth most common overall; herpesvirus 8 causes Kaposi sarcoma."],
     ["The rarest form of skin cancer, usually caused by abnormal T cells migrating into the skin over years",
      "Migrating T cells describe cutaneous T-cell lymphoma."]],
   c=0, cite=c(16)),

 dict(topic="Squamous cell carcinoma", io=IOA, slot="etiology",
   q="What is the usual aetiology of squamous cell carcinoma, and which premalignant lesion may it arise from?",
   opts=[
     ["Prolonged cumulative sun exposure in fair-skinned people who burn easily; it may arise from an actinic keratosis",
      "Correct — the continuum from actinic keratosis matters."],
     ["Intense intermittent sun exposure in fair-skinned people who tan easily; it may arise from a seborrheic keratosis",
      "Intermittent exposure is the basal cell pattern, and seborrheic keratosis is benign."],
     ["Prolonged cumulative sun exposure in darkly pigmented people; it may arise from a dermatofibroma",
      "Fair skin is the risk, and dermatofibroma is benign."],
     ["Chronic immunosuppression alone regardless of ultraviolet exposure; it may arise from a solar lentigo",
      "Immunosuppression amplifies risk but sun exposure is the usual driver."]],
   c=0, cite=c(21)),

 dict(topic="Squamous cell carcinoma", io=IOB, slot="risk factors",
   q="How does organ transplantation affect squamous cell carcinoma risk, and when do multiple tumours typically appear?",
   opts=[
     ["It is common and often aggressive in transplant recipients, with multiple tumours typically emerging about 5 years after transplant",
      "Correct — chronic lymphocytic leukaemia and human immunodeficiency virus also raise risk."],
     ["It is uncommon and usually indolent in transplant recipients, with single tumours typically emerging about 5 years after transplant",
      "It is common and often aggressive, not uncommon and indolent."],
     ["It is common and often aggressive in transplant recipients, with multiple tumours typically emerging within 6 weeks of transplant",
      "The interval given is about five years."],
     ["It is unchanged by transplantation, since immunosuppressive therapy does not influence keratinocyte carcinoma risk",
      "Immunosuppression substantially raises both risk and aggressiveness."]],
   c=0, cite=c(21)),

 dict(topic="Squamous cell carcinoma", io=IOA, slot="agent/regimen",
   q="Which chemoprevention does the deck give for squamous cell carcinoma, at what dose, and with what effect?",
   opts=[
     ["Nicotinamide 500 mg orally twice daily, reducing new squamous cell carcinoma development by approximately 30% in high-risk patients",
      "Correct — the corresponding figure for basal cell carcinoma is about 20%."],
     ["Nicotinamide 500 mg orally twice daily, reducing new squamous cell carcinoma development by approximately 20% in high-risk patients",
      "20% is the figure the deck gives for basal cell carcinoma."],
     ["Oral acitretin 25 mg daily, reducing new squamous cell carcinoma development by approximately 30% in high-risk patients",
      "The agent named is nicotinamide."],
     ["Topical fluorouracil twice daily, reducing new squamous cell carcinoma development by approximately 50% in high-risk patients",
      "Fluorouracil treats existing disease; it is not the chemoprevention named."]],
   c=0, cite=c(21)),

 dict(topic="Squamous cell carcinoma", io=IOA, slot="manifestation",
   q="What is the classic presentation of cutaneous squamous cell carcinoma?",
   opts=[
     ["A small red, conical, hard nodule that may ulcerate; also a non-healing ulcer, a warty nodule, or an irregular pink plaque with haemorrhagic crust",
      "Correct — four presentations to recognise."],
     ["A pearly translucent papule with visible telangiectasias and a rolled border; also a scar-like ivory-white plaque with subtle extension",
      "Those are the basal cell carcinoma patterns."],
     ["An asymmetric pigmented macule with irregular borders and colour variegation; also an amelanotic nodule lacking classic features",
      "Those describe melanoma."],
     ["Red or purple macules, plaques and nodules on skin or mucous membranes; also marked edema with few visible lesions",
      "Those describe Kaposi sarcoma."]],
   c=0, cite=c(22)),

 dict(topic="Squamous cell carcinoma", io=IOA, slot="test finding",
   q="Which red flags does the deck list for squamous cell carcinoma?",
   opts=[
     ["Rapid growth, pain, bleeding, ulceration, induration, fixation, or palpable regional nodes",
      "Correct — seven features."],
     ["Slow growth, painlessness, a stable size, soft consistency, free mobility, and no palpable nodes",
      "Those are reassuring features, not red flags."],
     ["Pruritus, fine scaling, symmetry of the lesion, sharp demarcation, and a waxy stuck-on surface",
      "Those suggest a benign keratosis."],
     ["Sandpaper texture, tenderness on palpation, flesh-coloured hue, and a size under 6 mm",
      "Those describe a typical actinic keratosis."]],
   c=0, cite=c(22)),

 dict(topic="Squamous cell carcinoma", io=IOA, slot="risk factors",
   q="Which sites does the deck call high-risk for squamous cell carcinoma, and what does having more than ten tumours imply?",
   opts=[
     ["Mucosal surfaces, lip, ear, scalp, temple, nose and genitalia; more than ten tumours means higher rates of local recurrence and nodal metastasis",
      "Correct — site and tumour count both drive risk."],
     ["The trunk, back, chest and shoulders; more than ten tumours means higher rates of local recurrence and distant nodal metastasis",
      "Trunk and chest are the superficial basal cell sites."],
     ["Mucosal surfaces, lip, ear, scalp, temple and nose; more than ten tumours indicates indolent disease with a lower rate of recurrence and metastasis",
      "A high tumour count raises risk rather than lowering it."],
     ["The palms, soles, nail units and periungual skin; more than ten tumours means higher rates of local recurrence and distant spread",
      "Acral sites belong to melanoma and nail unit disease."]],
   c=0, cite=c(22)),

 dict(topic="Squamous cell carcinoma", io=IOA, slot="differential",
   q="What does the deck say should be used to distinguish squamous cell carcinoma from its differential, rather than morphology alone?",
   opts=[
     ["Time course, firmness or induration, ulceration, site, immune status and pathology",
      "Correct — six discriminators beyond appearance."],
     ["Colour variegation, symmetry, border regularity, diameter and evolution alone",
      "Those are the melanoma recognition criteria."],
     ["Patient age, sex, family history and occupational sun exposure alone",
      "Demographics do not settle this differential."],
     ["Dermoscopy pattern, Wood lamp fluorescence and surface scale alone",
      "Wood lamp has no role here."]],
   c=0, cite=c(23)),

 dict(topic="Squamous cell carcinoma", io=IOA, slot="first-line",
   q="How is squamous cell carcinoma in situ managed when there are no high-risk features?",
   opts=[
     ["Imiquimod, topical fluorouracil, or curettage and electrodesiccation in appropriately selected disease",
      "Correct — three options for in situ disease without high-risk features."],
     ["Surgical excision or Mohs micrographic surgery in every case, whatever the features and whatever the site",
      "Those are preferred for invasive disease."],
     ["Programmed death 1 blockade or cetuximab in every case, whatever the features and whatever the site",
      "Those are for advanced or metastatic disease."],
     ["Liquid nitrogen cryotherapy alone, with no role for topical therapy, curettage or electrodesiccation",
      "Cryotherapy is the actinic keratosis lesion-directed option."]],
   c=0, cite=c(24)),

 dict(topic="Squamous cell carcinoma", io=IOA, slot="escalation",
   q="What is preferred for invasive squamous cell carcinoma, and what is used for advanced or metastatic disease?",
   opts=[
     ["Surgical excision or Mohs micrographic surgery for invasive disease; programmed death 1 blockade and cetuximab for advanced or metastatic disease",
      "Correct — advanced disease needs specialist multidisciplinary care."],
     ["Imiquimod or topical fluorouracil for invasive disease; surgical excision for advanced or metastatic disease",
      "Topical agents are for in situ disease only."],
     ["Surgical excision or Mohs micrographic surgery for invasive disease; hedgehog pathway inhibitors for advanced or metastatic disease",
      "Hedgehog inhibitors belong to basal cell carcinoma."],
     ["Radiation therapy alone for invasive disease; curettage and electrodesiccation for advanced or metastatic disease",
      "Neither matches the deck's sequence."]],
   c=0, cite=c(24)),

 dict(topic="Squamous cell carcinoma", io=IOA, slot="escalation",
   q="Which indications does the deck give for Mohs micrographic surgery in squamous cell carcinoma?",
   opts=[
     ["High-risk sites (lips, temples, ears, nose, genitalia), recurrent tumours, aggressive histology with perineural or perivascular invasion, lesions over 1 cm on the face or over 2 cm on trunk or extremities, immunosuppression, tumours within scars, and genetic disease-associated tumours",
      "Correct — note the two different size thresholds by site."],
     ["High-risk sites (lips, temples, ears, nose, genitalia), recurrent tumours, aggressive histology with perineural or perivascular invasion, lesions over 2 cm on the face or over 1 cm on trunk or extremities, immunosuppression, and tumours within scars",
      "The two size thresholds are the wrong way round."],
     ["Any lesion on the trunk, any lesion in a patient over 65, any lesion present more than a year, any pigmented lesion, and any lesion the patient finds unsightly",
      "None of these is a Mohs indication in the deck."],
     ["Only recurrent tumours and only after two failed courses of topical therapy, since site, size and immune status do not alter the surgical choice",
      "Site, size and immune status are all explicit indications."]],
   c=0, cite=c(24)),

 dict(topic="Squamous cell carcinoma", io=IOB, slot="referral",
   q="What follow-up schedule does the deck specify after squamous cell carcinoma?",
   opts=[
     ["At least annual skin AND lymph-node examination, at closer intervals for high-risk or immunosuppressed patients",
      "Correct — the node examination is part of the routine, not an extra."],
     ["At least annual skin examination alone, with lymph nodes assessed only once metastasis is suspected clinically",
      "Nodes are examined at every routine visit."],
     ["Examination every five years, at closer intervals only for patients who have had more than ten tumours",
      "The interval is at least annual for everyone."],
     ["No scheduled follow-up once the lesion has been completely excised with clear histologic margins",
      "Surveillance continues because second primaries are common."]],
   c=0, cite=c(26)),

 dict(topic="Squamous cell carcinoma", io=IOB, slot="referral",
   q="Which findings make referral URGENT in squamous cell carcinoma?",
   opts=[
     ["High-risk site, size, recurrence, aggressive histology, immunosuppression, neurologic symptoms, or nodal disease",
      "Correct — neurologic symptoms suggest perineural invasion."],
     ["Cosmetic concern, patient anxiety, a lesion older than one year, a lesion on the trunk, or any pigmented lesion",
      "None of these is an urgency criterion."],
     ["Only confirmed nodal disease, since high-risk site, size, recurrence and immune status can all be managed routinely",
      "Site, size and immune status are each urgency triggers."],
     ["Only failure of two courses of topical therapy, whatever the site, size, histology, immune status or symptoms",
      "Urgency does not wait on topical therapy."]],
   c=0, cite=c(26)),

 dict(topic="Squamous cell carcinoma", io=IOA, slot="prognosis",
   q="What metastatic rate does the deck give for actinically induced squamous cell carcinoma?",
   opts=[
     ["An estimated 3 to 7%",
      "Correct — substantially higher with high-risk features."],
     ["An estimated 30 to 70%",
      "That is an order of magnitude too high."],
     ["An estimated 0.1 to 0.5%",
      "That is the lifetime melanoma risk figure in people of colour."],
     ["An estimated 15 to 20%",
      "The deck gives 3 to 7%."]],
   c=0, cite=c(26)),
]
