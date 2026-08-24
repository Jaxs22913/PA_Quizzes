# -*- coding: utf-8 -*-
# CMS I Lecture 9 — SET 2, vignette pool A. Actinic keratosis, squamous cell
# carcinoma, basal cell carcinoma.
#
# THE SLIDE IS AUTHORITATIVE (Jaquith deck). Lead-ins are explicit; distractors
# are right-disease-wrong-phase or the neighbouring lesion in the differential,
# written to the answer's shape. Correct answer first (c=0).
SRC = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = "Objective 1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis of pre-malignant and malignant cutaneous lesions"
IOB = "Objective 11 — Identify medical care strategies for pre-malignant and malignant cutaneous lesions for adult and elderly populations"

VIG_A = [
 dict(topic="Actinic keratosis", io=IOB, lead="diagnosis",
   q="A 71-year-old retired roofer has several rough patches on his bald scalp. Each is about 4 mm, pink, and you notice them more when you run a gloved finger over the scalp than when you look. Which is the most likely diagnosis?",
   opts=[
     ["Actinic keratosis", "Correct — the sandpaper texture is often felt before it is seen."],
     ["Seborrheic keratosis", "Those are waxy and stuck-on, and are seen more easily than felt."],
     ["Superficial basal cell carcinoma", "That is a reddish shiny scaly plaque, typically on back or chest."],
     ["Solar lentigo", "That is a flat uniform macule with no surface change to feel."]],
   c=0, cite=c(12)),

 dict(topic="Actinic keratosis", io=IOA, lead="next step",
   q="One of that 71-year-old's scalp lesions is now thickened, indurated and has bled twice. Which is the most appropriate next step?",
   opts=[
     ["Order a shave or punch biopsy, because induration and bleeding raise concern for squamous cell carcinoma",
      "Correct — those features are not part of a typical actinic keratosis."],
     ["Treat with liquid nitrogen cryotherapy and review in three months, since these are expected features",
      "Bleeding and induration are explicitly not typical and warrant tissue."],
     ["Begin field-directed fluorouracil to the whole scalp and review at the end of the course",
      "Field therapy does not address a lesion behaving like a carcinoma."],
     ["Reassure and review in a year, since actinic keratoses commonly involute without treatment",
      "Involution is possible but does not explain induration and bleeding."]],
   c=0, cite=c(13)),

 dict(topic="Actinic keratosis", io=IOA, lead="treatment",
   q="A 68-year-old has a single well-demarcated actinic keratosis on the dorsal hand. Which is the most appropriate treatment, and what should you tell her to expect?",
   opts=[
     ["Liquid nitrogen cryotherapy; the lesion will crust and disappear over 10 to 14 days",
      "Correct — lesion-directed therapy suits an isolated lesion with clear borders."],
     ["Liquid nitrogen cryotherapy; the lesion will blister and resolve completely within 24 hours",
      "The timeline given is 10 to 14 days."],
     ["Topical fluorouracil to the whole forearm; the field will inflame and settle over 10 to 14 days",
      "Field therapy is for multiple lesions in one region."],
     ["Surgical excision with 5 mm margins; the wound will heal over 10 to 14 days",
      "Excision is not first-line for an isolated actinic keratosis."]],
   c=0, cite=c(14)),

 dict(topic="Actinic keratosis", io=IOA, lead="treatment",
   q="A 74-year-old farmer has eleven actinic keratoses across his forehead and temples. Which approach does the deck favour, and why?",
   opts=[
     ["Field-directed therapy, because multiple lesions in one anatomic region reflect field cancerization risk",
      "Correct — options are fluorouracil, imiquimod, photodynamic therapy, or fluorouracil plus calcipotriene."],
     ["Lesion-directed cryotherapy to each of the eleven in turn, because each lesion carries its own independent risk",
      "The point of field therapy is that the surrounding field is at risk too."],
     ["Observation with annual review, because eleven lesions in one region indicates indolent disease",
      "A high lesion burden raises concern rather than lowering it."],
     ["Immediate wide excision of the whole affected field, because eleven lesions cannot be treated topically",
      "Excision of a field is not among the deck's options."]],
   c=0, cite=c(14)),

 dict(topic="Squamous cell carcinoma", io=IOA, lead="diagnosis",
   q="A 66-year-old man with fair skin has a small red, conical, hard nodule on his lower lip that has ulcerated over two months. Which is the most likely diagnosis?",
   opts=[
     ["Squamous cell carcinoma", "Correct — and the lip is one of the named high-risk sites."],
     ["Basal cell carcinoma", "That is pearly and translucent with telangiectasias, and grows over years."],
     ["Actinic keratosis", "That is a small rough sandpaper papule without ulceration or induration."],
     ["Keratoacanthoma", "It is in the differential, but the deck's classic description here is carcinoma."]],
   c=0, cite=c(22)),

 dict(topic="Squamous cell carcinoma", io=IOB, lead="next step",
   q="A 58-year-old kidney transplant recipient, six years post-transplant, has developed his fourth squamous cell carcinoma this year. Which does the deck say about this pattern, and what can be offered to reduce new tumours?",
   opts=[
     ["Multiple tumours typically emerge about five years after transplant and are often aggressive; nicotinamide 500 mg orally twice daily reduces new squamous cell carcinoma by about 30%",
      "Correct — both the timing and the chemoprevention figure."],
     ["Multiple tumours typically emerge within six weeks of transplant and are usually indolent; nicotinamide 500 mg orally twice daily reduces new tumours by about 30%",
      "The interval is about five years and the disease is often aggressive."],
     ["Multiple tumours typically emerge about five years after transplant; oral acitretin reduces new squamous cell carcinoma by about 30%",
      "The agent named is nicotinamide."],
     ["Multiple tumours typically emerge about five years after transplant; nicotinamide reduces new tumours by about 20%",
      "20% is the figure for basal cell carcinoma."]],
   c=0, cite=c(21)),

 dict(topic="Squamous cell carcinoma", io=IOA, lead="treatment",
   q="A 70-year-old has a biopsy-proven invasive squamous cell carcinoma 1.4 cm across on the temple. Which is the most appropriate management?",
   opts=[
     ["Mohs micrographic surgery, since the temple is a high-risk site and the lesion exceeds 1 cm on the face",
      "Correct — two separate Mohs indications are met."],
     ["Imiquimod or topical fluorouracil, since topical therapy is appropriate for invasive disease at this size",
      "Topical therapy is for in situ disease without high-risk features."],
     ["Programmed death 1 blockade, since a lesion over 1 cm is by definition advanced disease",
      "That is reserved for advanced or metastatic disease."],
     ["Liquid nitrogen cryotherapy, since the temple tolerates destruction well cosmetically",
      "Cryotherapy is not a treatment for invasive carcinoma."]],
   c=0, cite=c(24)),

 dict(topic="Squamous cell carcinoma", io=IOA, lead="next step",
   q="A patient treated for squamous cell carcinoma of the scalp returns with new numbness and tingling in the distribution of the scar. Which is the most appropriate response?",
   opts=[
     ["Refer urgently, because neurologic symptoms are one of the deck's urgent referral triggers",
      "Correct — they raise concern for perineural invasion."],
     ["Reassure, because sensory change is expected permanently after any scalp excision",
      "New neurologic symptoms are an explicit urgency trigger."],
     ["Repeat topical fluorouracil to the scar and review in three months",
      "Topical therapy does not address this concern."],
     ["Arrange routine review in twelve months as part of annual surveillance",
      "This finding warrants urgent rather than routine review."]],
   c=0, cite=c(26)),

 dict(topic="Basal cell carcinoma", io=IOA, lead="diagnosis",
   q="A 62-year-old has a slowly enlarging papule beside the nose with a central erosion. When you stretch the skin, fine vessels become obvious across a pearly, translucent surface. Which is the most likely diagnosis?",
   opts=[
     ["Nodular basal cell carcinoma", "Correct — stretching accentuates the telangiectasias."],
     ["Squamous cell carcinoma", "That is a red conical hard nodule, often ulcerated, growing faster."],
     ["Sebaceous hyperplasia", "It is in the differential, but it lacks the pearly border and central erosion."],
     ["Amelanotic melanoma", "It is in the differential, but this is the classic basal cell description."]],
   c=0, cite=c(35)),

 dict(topic="Basal cell carcinoma", io=IOA, lead="diagnosis",
   q="A 59-year-old has an ivory-white, scar-like plaque on the cheek. He has had no injury there. On careful inspection the pink edge seems to extend further than the visible lesion. Which subtype is this, and what is the concern?",
   opts=[
     ["Morpheaform or sclerosing basal cell carcinoma, which carries a higher risk of subclinical spread beyond the visible segment",
      "Correct — the invisible extension is what makes it dangerous."],
     ["Superficial basal cell carcinoma, which carries a higher risk of subclinical spread beyond the visible segment",
      "Superficial disease is a reddish shiny plaque on back or chest."],
     ["Nodular basal cell carcinoma, which carries a higher risk of subclinical spread beyond the visible segment",
      "Nodular disease has a defined pearly border."],
     ["Pigmented basal cell carcinoma, which carries a higher risk of subclinical spread beyond the visible segment",
      "Pigmented disease mimics melanocytic lesions rather than scar."]],
   c=0, cite=c(35)),

 dict(topic="Basal cell carcinoma", io=IOA, lead="test",
   q="You suspect a basal cell carcinoma on a patient's shoulder. Which is the most appropriate diagnostic step, and why does it matter which subtype comes back?",
   opts=[
     ["Shave or punch biopsy, because the HISTOLOGIC subtype determines behaviour and dictates treatment selection",
      "Correct — histology, not clinical appearance, drives the plan."],
     ["Shave or punch biopsy, because the CLINICAL subtype determines behaviour and dictates treatment selection",
      "The deck assigns that role to the histologic subtype."],
     ["Wide local excision with 1 cm margins, because tissue diagnosis and treatment are achieved together",
      "Biopsy precedes definitive treatment here."],
     ["Sentinel lymph node biopsy, because nodal status determines treatment selection",
      "Sentinel node biopsy belongs to melanoma staging."]],
   c=0, cite=c(36)),

 dict(topic="Basal cell carcinoma", io=IOA, lead="treatment",
   q="A 64-year-old has a biopsy-confirmed superficial basal cell carcinoma on the upper back, with no high-risk features. Which topical regimen fits the deck, and what must follow it?",
   opts=[
     ["Imiquimod five nights weekly for 6 to 10 weeks, or fluorouracil twice daily for up to 12 weeks; clinical clearance must be confirmed afterwards",
      "Correct — confirming clearance is part of the regimen, not optional."],
     ["Imiquimod twice daily for 6 to 10 weeks, or fluorouracil five nights weekly for up to 12 weeks; clearance can be assumed once inflammation settles",
      "The schedules are swapped and clearance must be confirmed."],
     ["Vismodegib orally for 6 to 10 weeks; clinical clearance must be confirmed afterwards",
      "Hedgehog inhibitors are for advanced or metastatic disease."],
     ["Liquid nitrogen cryotherapy every 2 to 3 weeks for 12 weeks; clearance must be confirmed afterwards",
      "That is not the topical regimen the deck gives."]],
   c=0, cite=c(37)),

 dict(topic="Basal cell carcinoma", io=IOB, lead="education",
   q="A patient has just had a basal cell carcinoma excised and asks whether that is the end of it. Which is the most appropriate response?",
   opts=[
     ["A second basal cell carcinoma develops in up to 50% of patients, so at least annual full-skin examination is mandatory",
      "Correct — the second-primary risk is what drives lifelong surveillance."],
     ["A second basal cell carcinoma develops in under 1% of patients, so no further surveillance is needed",
      "Second primaries are common, not rare."],
     ["A second basal cell carcinoma develops in up to 50% of patients, so examination every five years is sufficient",
      "The figure is right but the interval is at least annual."],
     ["Recurrence at the same site is near-certain, so a further excision should be booked now",
      "Excision recurrence is 5% or less."]],
   c=0, cite=c(33)),

 dict(topic="Basal cell carcinoma", io=IOA, lead="next step",
   q="A 77-year-old has a recurrent basal cell carcinoma at the inner canthus, and the biopsy reports infiltrative histology. Which is the most appropriate management?",
   opts=[
     ["Mohs micrographic surgery — the canthus is a high-risk site, the tumour is recurrent, and the histology is aggressive",
      "Correct — three separate Mohs indications are met."],
     ["Standard excision with 4 mm margins, since infiltrative histology behaves much like ordinary nodular disease",
      "Infiltrative histology is explicitly aggressive."],
     ["Topical imiquimod five nights weekly, since periocular skin tolerates surgical excision poorly",
      "Topical therapy is for selected superficial disease."],
     ["Hedgehog pathway inhibitor therapy with vismodegib, since recurrence at this site indicates advanced disease",
      "Those are reserved for advanced or metastatic disease."]],
   c=0, cite=c(37)),

 dict(topic="Basal cell carcinoma", io=IOA, lead="diagnosis",
   q="Two patients present the same morning. One has had intense blistering sunburns on holidays but works indoors; the other has worked outdoors for forty years with steady daily exposure. Which pattern favours which diagnosis?",
   opts=[
     ["Intense intermittent exposure favours basal cell carcinoma; prolonged cumulative exposure favours squamous cell carcinoma",
      "Correct — the exposure pattern is a genuine discriminator."],
     ["Intense intermittent exposure favours squamous cell carcinoma; prolonged cumulative exposure favours basal cell carcinoma",
      "The two patterns are the wrong way round."],
     ["Both patterns favour basal cell carcinoma equally, since ultraviolet exposure is not subdivided in this way",
      "The deck distinguishes the two patterns explicitly."],
     ["Both patterns favour melanoma, since keratinocyte carcinoma is not ultraviolet-driven",
      "Both keratinocyte carcinomas are ultraviolet-driven."]],
   c=0, cite=c(33)),
]
