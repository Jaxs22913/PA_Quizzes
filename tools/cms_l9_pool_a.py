# -*- coding: utf-8 -*-
# CMS I Lecture 9 — pool A. Foundational clinical approach and actinic keratosis.
#
# THE SLIDE IS AUTHORITATIVE. Jaxon, 2026-08-20: "especially Dr. Jaquith audio
# because she says words wrong all the time, so go by the powerpoints unless
# told otherwise." This is her deck again. Every fact here is from the slides.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
# Distractors are written to the SAME shape as the answer they sit beside.
SRC = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective 1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis of pre-malignant and malignant cutaneous lesions"
IOB = "Objective 11 — Identify medical care strategies for pre-malignant and malignant cutaneous lesions for adult and elderly populations"

POOL_A = [
 dict(topic="Clinical approach", io=IOA, slot="manifestation",
   q="What does the deck say you should do before assigning a diagnosis to a skin lesion?",
   opts=[
     ["Characterise it systematically — primary lesion type, colour, surface texture, border definition, size, distribution, palpability, ulceration, bleeding, induration and temporal evolution",
      "Correct — describe before naming."],
     ["Assign the most likely diagnosis first, then look for the features that confirm it — colour, texture, border, size and evolution — and discard those that do not fit",
      "That reverses the order the deck insists on."],
     ["Photograph the lesion and defer all description — type, colour, texture, border, size, distribution and evolution — until the dermatology referral has been accepted",
      "Description is the first step, not something deferred."],
     ["Biopsy every pigmented lesion before any description of type, colour, texture, border or evolution, since morphology is unreliable in premalignant disease",
      "Biopsy is triggered by concerning features, not used in place of describing."]],
   c=0, cite=c(4)),

 dict(topic="Clinical approach", io=IOA, slot="initial test",
   q="Which examination priorities does the deck list for a suspected malignant cutaneous lesion?",
   opts=[
     ["Good lighting, dermoscopy when trained, and a total-body skin survey when indicated; palms, soles and nails; oral mucosa when Kaposi sarcoma is possible; regional nodes for invasive or high-risk disease",
      "Correct — note the oral mucosa is tied specifically to Kaposi sarcoma."],
     ["Good lighting and dermoscopy in every patient regardless of training; palms, soles and nails; oral mucosa in every patient; a total-body survey reserved for those who already have a skin cancer diagnosis",
      "The survey is done when indicated, not only after diagnosis."],
     ["Wood lamp examination and potassium hydroxide preparation of any scale; palms, soles and nails; oral mucosa when tinea is possible; regional nodes in every patient regardless of risk",
      "Neither the lamp nor the preparation is part of this workup."],
     ["Dermoscopy alone, since the total-body survey, the palms, soles and nails, the oral mucosa and the regional nodes all belong to the dermatologist rather than the referring clinician",
      "The deck asks the examining clinician to do these."]],
   c=0, cite=c(4)),

 dict(topic="Clinical approach", io=IOA, slot="risk factors",
   q="Which history elements does the deck ask you to elicit?",
   opts=[
     ["Onset and change, bleeding or non-healing, pain or pruritus; sunburns, occupational or recreational ultraviolet exposure and tanning-bed use; prior skin cancer, immunosuppression or transplant, human immunodeficiency virus risk; chronic scars, wounds or radiation sites; family history",
      "Correct — note chronic scars and radiation sites among them."],
     ["Onset and change, bleeding or non-healing, pain or pruritus; sunburns, occupational exposure and tanning-bed use; chronic scars, wounds and radiation sites; family history — but not prior skin cancer, immunosuppression, transplant or human immunodeficiency virus status, which the dermatologist obtains at the time of biopsy",
      "The deck asks for a full history at the first encounter."],
     ["Onset and change; sunburns, occupational exposure and tanning-bed use; chronic scars and radiation sites; family history — but not immunosuppression or transplant status, which do not alter cutaneous malignancy risk",
      "Immunosuppression is explicitly listed and matters greatly."],
     ["Onset and change, pain or pruritus; occupational and recreational ultraviolet exposure and tanning-bed use; immunosuppression and family history — but not prior skin cancer, which does not predict a second primary",
      "Prior skin cancer is listed and is a strong predictor."]],
   c=0, cite=c(4)),

 dict(topic="Actinic keratosis", io=IOA, slot="etiology",
   q="What is the core mechanism of actinic keratosis, and how does the deck position it relative to keratinocyte carcinoma?",
   opts=[
     ["Chronic ultraviolet injury producing dysplastic keratinocytic change in a field of sun-damaged skin; it is premalignant and lies on a biologic continuum with keratinocyte carcinoma, not a distinct separate entity",
      "Correct — a continuum, not a separate disease."],
     ["Chronic ultraviolet injury producing dysplastic melanocytic change in a field of sun-damaged skin; it is premalignant but a distinct entity quite separate from keratinocyte carcinoma, with no biologic continuum between them",
      "The change is keratinocytic, and the deck rejects \"separate entity\"."],
     ["Human papillomavirus infection of keratinocytes in a field of sun-damaged skin; it is a benign lesion lying on a continuum with verruca rather than with keratinocyte carcinoma",
      "Ultraviolet injury, not a virus, and it is premalignant."],
     ["Chronic thermal injury producing dysplastic keratinocytic change in a field of scarred skin; it is premalignant and lies on a continuum with keratinocyte carcinoma but is unrelated to ultraviolet exposure",
      "Ultraviolet exposure is the driver."]],
   c=0, cite=c(11)),

 dict(topic="Actinic keratosis", io=IOA, slot="epidemiology",
   q="Approximately what proportion of actinic keratosis lesions progresses to squamous cell carcinoma each year?",
   opts=[
     ["About 1 in 1,000 lesions per year",
      "Correct — and cumulative field risk matters more than any single lesion."],
     ["About 1 in 10 lesions per year",
      "That is far higher than the figure given."],
     ["About 1 in 100 lesions per year",
      "The deck gives 1 in 1,000."],
     ["About 1 in 100,000 lesions per year",
      "The deck gives 1 in 1,000."]],
   c=0, cite=c(11)),

 dict(topic="Actinic keratosis", io=IOA, slot="risk factors",
   q="Which factors does the deck list as amplifying actinic keratosis risk?",
   opts=[
     ["Advanced age, cumulative ultraviolet exposure with outdoor work or recreation, prior actinic keratosis or keratinocyte carcinoma, male sex with bald scalp exposure, and immunosuppression",
      "Correct — five amplifiers."],
     ["Young age, intermittent ultraviolet exposure with indoor occupation, no prior actinic keratosis or keratinocyte carcinoma, female sex with full scalp hair, and a fully competent immune system",
      "These are the opposite of the listed amplifiers."],
     ["Obesity, diabetes with vascular disease, incontinence and immobility in a hospitalised patient, and recent antibiotic exposure",
      "Those are pressure injury and intertrigo risks."],
     ["Atopic dermatitis, asthma and allergic rhinitis in a young adult, with a family history of atopy and frequent emollient use",
      "Atopy is not a listed risk factor here."]],
   c=0, cite=c(11)),

 dict(topic="Actinic keratosis", io=IOA, slot="manifestation",
   q="Describe the actinic keratosis lesion, including the finding the deck says may be more apparent by touch than by sight.",
   opts=[
     ["Small 0.2 to 0.6 cm flesh-coloured, pink or slightly hyperpigmented papules with a characteristic sandpaper texture on palpation",
      "Correct — the sandpaper texture is often felt before it is seen."],
     ["Large 2 to 6 cm deeply pigmented plaques, flesh-coloured at the edge, with a smooth waxy stuck-on surface that is more apparent by sight than by touch",
      "A stuck-on waxy plaque describes seborrheic keratosis."],
     ["Small 0.2 to 0.6 cm pearly translucent or pink papules with visible telangiectasias that become more apparent when the skin is stretched",
      "Pearly papules with telangiectasias describe nodular basal cell carcinoma."],
     ["Small violaceous or purple macules and plaques, flesh-coloured early on, that are softer than surrounding skin and more apparent by sight than by touch",
      "Violaceous lesions suggest Kaposi sarcoma."]],
   c=0, cite=c(12)),

 dict(topic="Actinic keratosis", io=IOA, slot="manifestation",
   q="Where do actinic keratoses occur, and what does finding several in one anatomic zone imply?",
   opts=[
     ["Sun-exposed face, scalp, ears, forearms and dorsal hands; multiple lesions in one zone suggest field cancerization and favour field-directed therapy",
      "Correct — the distribution drives the treatment choice."],
     ["Sun-protected trunk, axillae and groin; multiple lesions in one zone suggest an immunosuppressed host and favour systemic therapy",
      "The distribution is sun-exposed skin."],
     ["Palms, soles and nail beds; multiple lesions in one zone suggest acral disease and favour surgical excision",
      "Acral sites are the melanoma and nail unit pattern."],
     ["Sun-exposed face, scalp and forearms; multiple lesions in one zone suggest a lower risk and favour observation alone",
      "Multiple lesions raise concern rather than lowering it."]],
   c=0, cite=c(12)),

 dict(topic="Actinic keratosis", io=IOA, slot="test finding",
   q="Which features are NOT part of a typical actinic keratosis and should prompt biopsy consideration?",
   opts=[
     ["Bleeding, induration, ulceration or rapid enlargement",
      "Correct — none of these belong to a typical lesion."],
     ["Tenderness on palpation and a rough surface texture",
      "Lesions may be tender, and roughness is characteristic."],
     ["Flesh-coloured or pink colour and a size under a centimetre",
      "Both are typical features."],
     ["Location on the dorsal hand and the presence of surrounding sun damage",
      "Both are the expected setting."]],
   c=0, cite=c(12)),

 dict(topic="Actinic keratosis", io=IOA, slot="differential",
   q="What is the most important distinction to make when assessing an actinic keratosis, and what raises that concern?",
   opts=[
     ["Early squamous cell carcinoma or carcinoma in situ — raised when a lesion is thick, indurated, ulcerated, enlarging, painful, bleeding, persistent or recurrent",
      "Correct — that list is the biopsy trigger."],
     ["Seborrheic keratosis — raised when a lesion is thick, waxy, stuck-on, sharply demarcated, enlarging, persistent or recurrent",
      "Seborrheic keratosis is in the differential but is not the important distinction."],
     ["Superficial basal cell carcinoma — raised when a lesion is pearly with rolled borders, visible telangiectasias, ulceration, bleeding or slow enlargement",
      "Superficial basal cell carcinoma is listed, but squamous cell carcinoma is the critical call."],
     ["Solar lentigo — raised when a lesion is uniformly pigmented, flat, non-indurated, painless and stable over many years",
      "Solar lentigo is in the differential but carries no malignant urgency here."]],
   c=0, cite=c(13)),

 dict(topic="Actinic keratosis", io=IOA, slot="initial test",
   q="How is a typical actinic keratosis diagnosed?",
   opts=[
     ["Usually clinically, with dermoscopy supporting recognition when the clinician is trained",
      "Correct — biopsy is reserved for concerning or persistent lesions."],
     ["By shave or punch biopsy in every case, since clinical diagnosis is unreliable",
      "Biopsy is triggered by concern, not routine."],
     ["By potassium hydroxide microscopy of the surface scale",
      "That test is for fungal elements."],
     ["By serology for ultraviolet-induced antibodies",
      "No such test exists in this deck."]],
   c=0, cite=c(13)),

 dict(topic="Actinic keratosis", io=IOA, slot="gold standard",
   q="When should a shave or punch biopsy be ordered for an actinic keratosis, and what must the interpretation distinguish?",
   opts=[
     ["When morphology or behaviour raises concern for squamous cell carcinoma, or the lesion persists or recurs after therapy; the interpretation must separate actinic keratosis from carcinoma in situ from invasive carcinoma",
      "Correct — invasion changes treatment, margins and risk assessment substantially."],
     ["Only after two failed courses of field-directed therapy, whatever the morphology or behaviour of the lesion; the interpretation need only confirm that some degree of keratinocytic dysplasia is present, since invasion does not alter treatment or margins",
      "Persistence after therapy is a trigger, but so is initial concern, and the grading matters."],
     ["In every patient over 65 at the first visit regardless of behaviour; the interpretation must separate actinic keratosis from seborrheic keratosis and solar lentigo",
      "Age alone is not a biopsy criterion."],
     ["Only when the lesion is cosmetically troublesome to the patient; the interpretation must confirm the depth of ultraviolet damage in the surrounding field",
      "Cosmesis is not the trigger."]],
   c=0, cite=c(13)),

 dict(topic="Actinic keratosis", io=IOA, slot="first-line",
   q="Which lesion-directed therapy does the deck give for actinic keratosis, and what happens to the lesion afterwards?",
   opts=[
     ["Liquid nitrogen cryotherapy — the lesion crusts and disappears over 10 to 14 days; preferred for isolated or few lesions with clear borders",
      "Correct — lesion-directed, for small numbers."],
     ["Liquid nitrogen cryotherapy — the lesion blisters and resolves within 24 hours; preferred for widespread disease across a whole zone",
      "The timeline is 10 to 14 days, and it is for isolated lesions."],
     ["Topical fluorouracil — the lesion crusts and disappears over 10 to 14 days; preferred for isolated lesions with clear borders",
      "Fluorouracil is field-directed rather than lesion-directed."],
     ["Surgical excision with 5 mm margins — the wound heals over 10 to 14 days; preferred for any lesion regardless of number",
      "Excision is not the first-line approach for actinic keratosis."]],
   c=0, cite=c(14)),

 dict(topic="Actinic keratosis", io=IOA, slot="escalation",
   q="When is field-directed therapy indicated for actinic keratosis, and which options does the deck list as most effective?",
   opts=[
     ["When multiple lesions are present in one anatomic region, reflecting field cancerization risk; topical fluorouracil, imiquimod, photodynamic therapy, and fluorouracil plus calcipotriene as a possible benefit",
      "Correct — four options, the last flagged as possible rather than established."],
     ["When a single lesion has clear borders and has not recurred; liquid nitrogen cryotherapy, curettage and electrodesiccation, Mohs micrographic surgery, and excision with 5 mm margins",
      "Those are lesion-directed or surgical approaches."],
     ["When the patient is immunosuppressed or transplanted; oral acitretin, systemic methotrexate, photodynamic therapy, and methotrexate plus calcipotriene as a possible benefit",
      "Systemic agents are not the field-directed options listed."],
     ["When the lesion has recurred twice after cryotherapy; radiation therapy, hedgehog pathway inhibitors, programmed death 1 blockade, and cetuximab as a possible benefit",
      "Those belong to advanced carcinoma management."]],
   c=0, cite=c(14)),

 dict(topic="Actinic keratosis", io=IOB, slot="referral",
   q="Which situations does the deck give as referral indications in actinic keratosis?",
   opts=[
     ["Diagnostic uncertainty or high lesion burden; recurrent or persistent lesions after appropriate therapy; immunosuppression, cosmetically sensitive sites, or concern for squamous cell carcinoma",
      "Correct — three groupings."],
     ["Any lesion on the dorsal hand or forearm; any patient over the age of 50; any lesion larger than 3 mm; any lesion that has been present more than a year",
      "None of these is a referral criterion."],
     ["Only after biopsy has already confirmed invasive squamous cell carcinoma, since uncertainty, lesion burden, recurrence and immunosuppression are all managed in primary care",
      "Referral is triggered before that point."],
     ["Only when the patient requests it for cosmetic reasons, since diagnostic uncertainty, high lesion burden and recurrence are all managed without referral",
      "Cosmetically sensitive sites are listed, but the criteria are broader."]],
   c=0, cite=c(15)),

 dict(topic="Actinic keratosis", io=IOA, slot="prognosis",
   q="What is the prognosis of an individual actinic keratosis, and what does treatment achieve?",
   opts=[
     ["Individual lesions may persist, involute, recur or progress; treatment reduces lesion burden but the surrounding field remains at risk, so surveillance remains necessary",
      "Correct — treating lesions does not treat the field."],
     ["Individual lesions always progress to carcinoma if left untreated; treatment eradicates both the lesion and the surrounding field, which ends the need for any further surveillance",
      "Lesions may also involute, and the field stays at risk."],
     ["Individual lesions always involute spontaneously within a year; treatment is therefore cosmetic only, the field carries no residual risk, and surveillance is unnecessary",
      "Progression is possible, which is why they are treated."],
     ["Individual lesions persist indefinitely without involuting or progressing; treatment eradicates them permanently with no recurrence and no residual field risk",
      "Recurrence is explicitly possible."]],
   c=0, cite=c(15)),

 dict(topic="Actinic keratosis", io=IOB, slot="education",
   q="What patient education does the deck give for actinic keratosis?",
   opts=[
     ["Daily broad-spectrum sun protection and protective clothing; expect local treatment reactions such as erythema and crusting and adhere to the field therapy duration; seek prompt review of any non-healing or changing lesion",
      "Correct — warning about the expected reaction protects adherence."],
     ["Sun protection in the summer months only and no protective clothing; expect no local reaction to field treatment; return only if an entirely new lesion appears",
      "Protection is daily, and reactions are expected."],
     ["Avoid all sun exposure permanently rather than using broad-spectrum protection or protective clothing; stop field therapy at the first sign of erythema or crusting; attend annual review regardless of any change in a lesion",
      "Stopping at the first erythema would abort effective therapy."],
     ["No specific education is needed once the lesions have been treated successfully, since the surrounding field carries no further risk and reactions to therapy are not expected",
      "The field remains at risk, so education continues."]],
   c=0, cite=c(15)),
]
