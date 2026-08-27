# -*- coding: utf-8 -*-
"""Premalignant and Malignant Cutaneous Lesions (Jaquith) -- pool for the Updated CMS derm masters."""
DECK = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
IO_1 = ("1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing, management, appropriate referrals, patient education, "
        "and prognosis of pre-malignant and malignant cutaneous lesions")
IO_11 = "11 — Identify medical care strategies for pre-malignant and malignant cutaneous lesions for adult and elderly populations"

def Q(topic, q, opts, c, slide, io=IO_1):
    return {"topic": topic, "io": io, "q": q, "opts": opts, "c": c, "cite": f"{DECK}, Slide {slide}"}

QUESTIONS = [

Q("Actinic keratosis",
  "A 74-year-old man with a lifetime of outdoor work has multiple 0.3 to 0.5 cm pink papules on the scalp and dorsal "
  "hands. Several are more apparent to touch than to sight. One lesion is thick, indurated, and has begun to bleed. "
  "What does that single lesion most require?",
  [["Biopsy, because thickness, induration, and bleeding raise concern for squamous cell carcinoma",
    "Correct. The most important distinction for actinic keratosis is early squamous cell carcinoma or carcinoma in "
    "situ, especially when a lesion is thick, indurated, ulcerated, enlarging, painful, bleeding, persistent, or "
    "recurrent. Those features change the lesion from one to treat destructively to one to sample."],
   ["Liquid nitrogen cryotherapy, as for the other lesions",
    "Cryotherapy is preferred for isolated or few lesions with clear borders and eradicates them over 10 to 14 days. "
    "Applying it to an indurated bleeding lesion destroys the tissue that would have made the diagnosis."],
   ["Field-directed therapy across the whole scalp",
    "Field-directed therapy is indicated when multiple lesions occupy a field of sun-damaged skin, and it is "
    "appropriate for his burden generally. But it does not address the single lesion whose features suggest "
    "carcinoma."],
   ["Observation with review in one year",
    "Annual review is a reasonable surveillance interval for stable disease. A bleeding indurated lesion has already "
    "declared itself and should not wait."],
   ["Reassurance, since actinic keratoses are benign",
    "Actinic keratosis is premalignant and lies on a biologic continuum with keratinocyte carcinoma, so it is not "
    "benign, and this lesion in particular carries red-flag features."]],
  0, 13),

Q("Actinic keratosis",
  "What is the characteristic tactile finding of an actinic keratosis, and what does it imply for examination "
  "technique?",
  [["A sandpaper texture, meaning a lesion may be more apparent by touch than by sight",
    "Correct. Actinic keratoses are small 0.2 to 0.6 cm flesh-coloured, pink, or slightly hyperpigmented papules with "
    "a characteristic sandpaper texture on palpation, and a lesion may be more apparent by touch than by sight. The "
    "skin must therefore be palpated, not only inspected."],
   ["A velvety texture, best appreciated on inspection alone",
    "A velvety texture describes acanthosis nigricans and seborrheic keratosis. Inspection alone would miss the "
    "lesions this condition is known for."],
   ["A stuck-on quality that lifts at the edge",
    "A stuck-on or pasted-on appearance describes seborrheic keratosis, which is benign."],
   ["A pearly translucent quality with visible telangiectasias",
    "Pearly translucency with telangiectasias accentuated by stretching the skin is the hallmark of nodular basal "
    "cell carcinoma."],
   ["A boggy fluctuant quality on palpation",
    "Bogginess suggests an inflammatory or infective process such as a kerion in tinea barbae rather than a dysplastic "
    "keratinocytic lesion."]],
  0, 12),

Q("Actinic keratosis",
  "When is field-directed rather than lesion-directed therapy indicated for actinic keratoses?",
  [["When multiple lesions occupy a field of sun-damaged skin",
    "Correct. Field-directed therapy is indicated when multiple lesions occupy a field of sun-damaged skin, "
    "reflecting that chronic ultraviolet injury produces dysplastic change across a field rather than in isolated "
    "spots. Lesion-directed cryotherapy is preferred for isolated or few lesions with clear borders."],
   ["When a single lesion has clear borders",
    "An isolated lesion with clear borders is precisely the situation in which liquid nitrogen cryotherapy is "
    "preferred."],
   ["When the lesion is thick, indurated, and bleeding",
    "Those features raise concern for squamous cell carcinoma and call for biopsy rather than any destructive or "
    "topical field therapy."],
   ["Only in immunosuppressed patients",
    "Immunosuppression is a referral indication alongside diagnostic uncertainty and high lesion burden, but it is not "
    "what defines the choice between lesion-directed and field-directed therapy."],
   ["Only after cryotherapy has failed twice",
    "Field therapy is chosen on lesion burden and distribution rather than reserved for repeated treatment failure."]],
  0, 14, IO_11),

Q("Squamous cell carcinoma",
  "A 78-year-old fair-skinned farmer has a small red, conical, hard nodule on the pinna that has ulcerated and grown "
  "over two months. What is the most likely diagnosis and its relationship to premalignant disease?",
  [["Cutaneous squamous cell carcinoma, the second most common skin cancer, which may arise from an actinic "
    "keratosis",
    "Correct. Cutaneous squamous cell carcinoma is the second most common form of skin cancer, usually following "
    "prolonged cumulative sun exposure, and may arise from an actinic keratosis. The classic presentation is a small "
    "red conical hard nodule that may ulcerate, or a non-healing ulcer, warty nodule, or irregular pink plaque with "
    "haemorrhagic crust."],
   ["Basal cell carcinoma, the most common skin cancer, arising from intermittent intense exposure",
    "Basal cell carcinoma is the most common form of cancer and is driven by intense intermittent exposure, but its "
    "nodular form is a pearly translucent papule with telangiectasias rather than a hard conical ulcerating nodule."],
   ["Actinic keratosis, a premalignant lesion",
    "Actinic keratoses are small sandpapery papules 0.2 to 0.6 cm. Rapid growth, ulceration, and a hard nodule are "
    "the red flags that mark progression beyond that stage."],
   ["Keratoacanthoma, which regresses spontaneously",
    "Keratoacanthoma is on the differential and can regress, which is exactly why biopsy is the only reliable way to "
    "distinguish it from squamous cell carcinoma."],
   ["Amelanotic melanoma",
    "Amelanotic melanoma is on the differential, but the classic conical hard ulcerating nodule on chronically "
    "sun-exposed skin of an older fair-skinned outdoor worker fits keratinocyte carcinoma."]],
  0, 22),

Q("Squamous cell carcinoma",
  "What is the preferred management of invasive cutaneous squamous cell carcinoma, and what follow-up is "
  "recommended?",
  [["Surgical excision or Mohs micrographic surgery, with at least annual skin and lymph node examination",
    "Correct. Surgical excision or Mohs micrographic surgery is preferred for invasive squamous cell carcinoma, with "
    "at least annual skin and lymph node examination and closer intervals for high-risk or immunosuppressed patients. "
    "All suspected invasive lesions are referred to dermatology or an experienced surgeon."],
   ["Topical imiquimod or fluorouracil, with annual examination",
    "Imiquimod, topical fluorouracil, or curettage and electrodesiccation are options for carcinoma in situ without "
    "high-risk features. Applying them to invasive disease under-treats it."],
   ["Cryotherapy, with no routine follow-up",
    "Cryotherapy is a lesion-directed therapy for actinic keratosis. It is not the treatment for invasive carcinoma, "
    "and follow-up is required in any case."],
   ["Radiotherapy as first-line treatment for all patients",
    "Surgery is the preferred modality. Radiotherapy has a role in selected patients rather than as universal first "
    "line."],
   ["Observation, since squamous cell carcinoma does not metastasise",
    "Squamous cell carcinoma carries genuine metastatic potential, which is why lymph node examination is part of "
    "follow-up."]],
  0, 26),

Q("Basal cell carcinoma",
  "A 66-year-old woman has a slow-growing 1 cm papule on the nose with a pearly translucent quality and visible "
  "telangiectasias that become more apparent when the skin is stretched. There is central erosion. What subtype is "
  "this, and what is notable about the tumour overall?",
  [["Nodular basal cell carcinoma; basal cell carcinoma is the most common form of cancer",
    "Correct. Nodular basal cell carcinoma is a papule or nodule with central erosion, growing slowly over years to "
    "1 to 2 cm or larger, with a pearly or translucent quality and visible telangiectasias accentuated by stretching "
    "the skin. Basal cell carcinoma is the most common form of cancer, driven by ultraviolet light in fair-skinned "
    "people with intense intermittent exposure."],
   ["Nodular squamous cell carcinoma; squamous cell carcinoma is the most common form of cancer",
    "Squamous cell carcinoma is the second most common skin cancer, and its nodule is red, conical, and hard rather "
    "than pearly and translucent."],
   ["Sebaceous hyperplasia, which is benign",
    "Sebaceous hyperplasia is on the basal cell carcinoma differential and dermoscopy distinguishes them. Its papules "
    "are whitish-yellow with a central dell rather than pearly with telangiectasias and central erosion."],
   ["Keratoacanthoma, which resolves spontaneously",
    "Keratoacanthoma grows rapidly over 6 to 8 weeks and is dome-shaped with a central keratin plug, rather than "
    "enlarging slowly over years with a pearly rim."],
   ["Amelanotic melanoma, which requires wide excision",
    "Amelanotic melanoma is a differential consideration, but the pearly translucency with stretch-accentuated "
    "telangiectasias is the characteristic basal cell finding."]],
  0, 35),

Q("Basal cell carcinoma",
  "When should Mohs micrographic surgery be considered for basal cell carcinoma?",
  [["For high-risk anatomic sites, recurrence, aggressive histology, or where tissue sparing is needed",
    "Correct. Mohs surgery is indicated for high-risk anatomic sites, recurrent tumours, aggressive histology, or "
    "where tissue-sparing is needed. The overall goal is complete eradication with minimal cosmetic and functional "
    "deformity."],
   ["For every basal cell carcinoma regardless of site or histology",
    "Mohs is resource-intensive and reserved for the situations listed. Using it universally would be neither "
    "practical nor necessary for low-risk truncal tumours."],
   ["Only after topical therapy has failed twice",
    "Topical imiquimod or fluorouracil is used for selected superficial basal cell carcinoma, with clinical clearance "
    "confirmed afterwards. Mohs selection depends on site and risk rather than on prior topical failure."],
   ["Only for tumours larger than 5 cm",
    "Size is one consideration among several, and anatomic site, recurrence, and histological subtype drive the "
    "decision."],
   ["Never, since basal cell carcinoma does not require surgery",
    "Basal cell carcinoma is capable of significant local destruction when delayed or histologically aggressive, and "
    "surgical management is central."]],
  0, 38),

Q("Malignant melanoma",
  "What do the letters of the ABCDE recognition rule stand for?",
  [["Asymmetry, border irregularity, colour variegation, diameter, and evolution",
    "Correct. Asymmetry means one half does not match the other; border refers to irregular, notched, or poorly "
    "defined edges; colour describes variegation with brown, red, white, black, or blue within one lesion; diameter "
    "and evolution complete the rule."],
   ["Asymmetry, bleeding, crusting, depth, and erosion",
    "Bleeding and ulceration are red flags in their own right, but they are not the letters of this rule, and a "
    "misremembered mnemonic produces systematic blind spots in screening."],
   ["Abscess, bulla, cyst, dermatitis, and erythema",
    "These are morphological terms unrelated to pigmented lesion assessment."],
   ["Age, burn history, complexion, dysplasia, and exposure",
    "These resemble risk factors rather than lesion features, and the rule describes the lesion itself."],
   ["Asymmetry, border, colour, dermoscopy, and excision",
    "Dermoscopy and excision are steps in evaluation and management rather than features of the lesion."]],
  0, 46),

Q("Malignant melanoma",
  "What is the most common subtype of melanoma, and what proportion of cases does it represent?",
  [["Superficial spreading melanoma, about two-thirds of cases, arising on intermittently sun-exposed skin",
    "Correct. Superficial spreading melanoma accounts for about two-thirds of cases, arises on intermittently "
    "sun-exposed skin, and evolves radially before entering vertical growth."],
   ["Lentigo maligna melanoma, about two-thirds of cases, on chronically sun-exposed skin",
    "Lentigo maligna arises on chronically sun-exposed skin of older adults with a slow radial growth phase, but it "
    "is not the most common subtype."],
   ["Nodular melanoma, about two-thirds of cases",
    "Nodular melanoma is a recognised major subtype characterised by early vertical growth, but it is not the "
    "commonest."],
   ["Acral lentiginous melanoma, about two-thirds of cases",
    "Acral lentiginous melanoma is one of the four major subtypes and is important because it occurs on palms, soles, "
    "and nail units in any skin tone, but it is uncommon overall."],
   ["Amelanotic melanoma, about half of cases",
    "Amelanotic melanoma is a presentation that lacks pigment and appears on several differentials. It is not a "
    "majority subtype."]],
  0, 41),

Q("Malignant melanoma",
  "What are the recommended re-excision margins for melanoma by thickness?",
  [["0.5 to 1 cm for in situ disease, 1 cm for lesions under 1 mm, and 1 to 2 cm for lesions over 1 mm",
    "Correct. Definitive local treatment uses a 0.5 to 1 cm margin for in situ disease, 1 cm for tumours under 1 mm, "
    "and 1 to 2 cm for tumours over 1 mm. Expert-centre referral applies to melanoma deeper than 1 mm or with lymph "
    "node involvement."],
   ["1 cm for in situ disease, 2 cm for lesions under 1 mm, and 3 cm for lesions over 1 mm",
    "Each margin is inflated by roughly a centimetre, which would cause unnecessary tissue loss and reconstruction "
    "without oncological benefit."],
   ["A single 5 mm margin for all melanomas regardless of thickness",
    "Margins are graded by Breslow thickness precisely because deeper tumours need wider clearance."],
   ["No re-excision is required after the diagnostic biopsy",
    "Re-excision is the definitive local treatment; the initial biopsy establishes the diagnosis and thickness."],
   ["Margins are determined by lesion diameter rather than thickness",
    "Breslow thickness is the dominant prognostic variable and what governs margins, not surface diameter."]],
  0, 52),

Q("Malignant melanoma",
  "At what thresholds is sentinel lymph node biopsy offered or discussed in melanoma?",
  [["At a Breslow thickness of 1.0 mm or greater, or 0.8 mm or greater with additional histologic risk factors such "
    "as ulceration or a high mitotic rate",
    "Correct. Sentinel lymph node biopsy is offered or discussed at 1.0 mm Breslow thickness or greater, or at "
    "0.8 mm or greater when additional histologic risk factors such as ulceration or a high mitotic rate are "
    "present."],
   ["At any thickness, since all melanomas warrant sentinel node biopsy",
    "Thresholds exist precisely so that thin low-risk tumours are not subjected to an operation that would not change "
    "management."],
   ["Only at a thickness of 4 mm or greater",
    "That threshold is far too high and would deny staging information to a large group of patients in whom it "
    "changes management."],
   ["Only when clinically palpable nodes are present",
    "Palpable nodes indicate clinically evident disease. The purpose of sentinel node biopsy is to detect occult "
    "nodal involvement."],
   ["Based on lesion diameter rather than Breslow thickness",
    "Breslow thickness is the dominant prognostic variable and must be accurately measured at initial biopsy."]],
  0, 51),

Q("Malignant melanoma",
  "What is the dominant prognostic variable in melanoma, and what must be ensured about it?",
  [["Breslow thickness, which must be accurately measured at the time of the initial biopsy",
    "Correct. Survival drops sharply with increasing Breslow thickness and with nodal or distant spread. Breslow "
    "thickness is the dominant prognostic variable and must be accurately measured at the time of initial biopsy — "
    "which is why a shave biopsy that transects the base can compromise staging."],
   ["Lesion diameter, which must exceed 6 mm to be significant",
    "Diameter is the D of the ABCDE rule and a screening feature, but it is not the prognostic variable that drives "
    "survival."],
   ["The presence of asymmetry, graded at initial assessment",
    "Asymmetry is a recognition feature used to select lesions for biopsy rather than a prognostic measurement."],
   ["The patient's Fitzpatrick skin type",
    "Skin type predicts baseline ultraviolet sensitivity and contributes to risk, but it does not determine prognosis "
    "once a melanoma is diagnosed."],
   ["The anatomic subtype of the melanoma",
    "Subtype describes the growth pattern and typical site. Thickness remains the dominant prognostic variable across "
    "subtypes."]],
  0, 55),

Q("Malignant melanoma",
  "What should patients be taught about melanoma self-examination?",
  [["Monthly self-examination using the ABCDE and ugly-duckling principles, including scalp, back, palms, soles, and "
    "nails",
    "Correct. Patients should perform monthly self-examination using ABCDE and ugly-duckling principles, including "
    "the scalp, back, palms, soles, and nails, with prompt assessment of evolution, bleeding, or ulceration."],
   ["Annual self-examination limited to sun-exposed skin",
    "Restricting examination to sun-exposed sites would miss acral lentiginous and nail unit melanoma, which occur on "
    "palms, soles, and nail units and are not clearly ultraviolet driven."],
   ["Self-examination is unnecessary if annual clinician examination occurs",
    "Both have a role, and monthly self-examination is what detects evolution between visits."],
   ["Examination should focus on counting the total number of naevi",
    "Naevus count contributes to risk assessment, but the self-examination principles are about recognising the "
    "lesion that differs from its neighbours and that is changing."],
   ["Only lesions larger than 6 mm need to be reported",
    "Diameter is one letter of the rule; evolution, asymmetry, border, and colour all warrant assessment regardless "
    "of size."]],
  0, 56),

Q("Kaposi sarcoma",
  "A 34-year-old man with untreated human immunodeficiency virus infection has multiple red-purple macules and "
  "plaques on the trunk. What examination is described as essential, and what is the first management priority?",
  [["Oral examination, because hard palate lesions are common and may be the presenting site; and beginning or "
    "optimising antiretroviral therapy",
    "Correct. Oral examination is essential when Kaposi sarcoma is suspected, since hard palate lesions are common "
    "and may be the presenting site. For acquired immunodeficiency syndrome-associated disease the first priority is "
    "to begin or optimise antiretroviral therapy, because immune restoration is the cornerstone of treatment."],
   ["Oral examination; and beginning systemic chemotherapy before any antiretroviral change",
    "The examination is right but the sequence is wrong. Immune restoration through antiretroviral therapy is the "
    "cornerstone for epidemic disease, with systemic therapy reserved for extensive or visceral involvement."],
   ["Ophthalmological examination; and intralesional vincristine",
    "Intralesional vincristine or vinblastine is palliative local therapy used in classic disease of older adults "
    "rather than the priority in epidemic disease, and the essential examination is oral."],
   ["Lymph node examination only; and observation",
    "Observation leaves an immunodeficiency untreated, and the specifically emphasised examination is of the oral "
    "cavity."],
   ["Skin examination alone, since mucosal involvement does not occur",
    "Lesions occur on skin or mucous membranes, and hard palate involvement may be the presenting site."]],
  0, 66),

Q("Kaposi sarcoma",
  "Which clinical form of Kaposi sarcoma is described as often aggressive and potentially rapidly fatal in young "
  "Black men in equatorial Africa?",
  [["The endemic form",
    "Correct. The endemic form is often aggressive disease in young Black men in equatorial Africa and can be rapidly "
    "fatal, in contrast to the classic form in older men, which follows a chronic course and is rarely fatal."],
   ["The classic form",
    "The classic form affects older men with a chronic course and is rarely fatal, associated with human herpesvirus "
    "8 in the setting of age-related immune senescence."],
   ["The iatrogenic form",
    "The iatrogenic form occurs in the setting of immunosuppressive therapy, notably after transplantation, and is "
    "addressed in part by discussing immunosuppression reduction with the transplant team."],
   ["The epidemic form",
    "The epidemic form is associated with acquired immunodeficiency syndrome, and its cornerstone of treatment is "
    "immune restoration with antiretroviral therapy."],
   ["The nodular form",
    "Nodular describes lesion morphology rather than one of the clinical forms of the disease."]],
  0, 63),

Q("Cutaneous T-cell lymphoma",
  "A 61-year-old man has had erythematous scaly patches and plaques on the trunk for four years, several larger than "
  "5 cm, that have been treated as psoriasis and eczema without lasting response. Pruritus is prominent. What "
  "features discriminate this from the inflammatory conditions it resembles?",
  [["Chronicity, treatment resistance, and large or oddly distributed lesions",
    "Correct. Mycosis fungoides may resemble psoriasis, eczema, or tinea, and the discriminators are chronicity, "
    "treatment resistance, and large or oddly distributed lesions. Early morphology is localised or generalised "
    "erythematous patches or scaly plaques, usually on the trunk, frequently greater than 5 cm."],
   ["The presence of pruritus",
    "Pruritus is common in cutaneous T-cell lymphoma but is shared with psoriasis, eczema, and tinea, so it separates "
    "none of them."],
   ["Involvement of the trunk",
    "Truncal involvement is typical of the early disease but is also seen in the inflammatory conditions on the "
    "differential."],
   ["The presence of scale",
    "Scaly plaques occur in psoriasis, eczematous dermatitis, and tinea corporis alike."],
   ["A positive potassium hydroxide preparation",
    "A positive potassium hydroxide preparation would indicate tinea corporis, which is one of the alternatives being "
    "excluded rather than a feature of lymphoma."]],
  0, 74),

Q("Cutaneous T-cell lymphoma",
  "What is the treatment philosophy in mycosis fungoides?",
  [["Stage-directed, skin-directed therapy, because early aggressive treatment has not been proven to cure disease or "
    "prevent progression and may cause premature death",
    "Correct. Management is complex. Early aggressive treatment has not been proven to cure disease or prevent "
    "progression, and overly aggressive therapy may cause complications and premature death, so treatment is "
    "stage-directed and skin-directed."],
   ["Immediate combination systemic chemotherapy for all patients at diagnosis",
    "This is precisely the approach the lecture warns against, since aggressive early therapy has not been shown to "
    "cure or prevent progression and carries a real risk of harm."],
   ["No treatment at any stage, since the disease is indolent",
    "The disease may remain confined to skin for years or decades, which makes indolence a real feature, but "
    "stage-directed skin-directed treatment is offered rather than nothing."],
   ["Surgical excision of all involved skin",
    "Malignant T cells form localised or generalised skin infiltrates, so excision is not a coherent strategy."],
   ["High-dose systemic corticosteroids indefinitely",
    "Indefinite systemic corticosteroids are not the described management and would carry substantial cumulative "
    "toxicity."]],
  0, 75),

Q("Nail unit neoplasms",
  "A 55-year-old woman has a new pigmented longitudinal band in the nail of one thumb that has widened over six "
  "months and is broader proximally than distally. Pigment extends onto the proximal nail fold. What is the concern, "
  "and what is the sign at the nail fold called?",
  [["Nail unit melanoma, with pigment extending onto the periungual skin known as Hutchinson sign",
    "Correct. New or evolving longitudinal melanonychia in one digit with increasing width, irregular colour or "
    "spacing, and proximal widening or a triangular shape raises nail unit melanoma. Pigment on the periungual skin "
    "is Hutchinson sign, and the thumb and great toe are high-yield sites."],
   ["Subungual haematoma, which migrates distally with nail growth",
    "Subungual haematoma is on the melanoma differential and does migrate distally as the nail grows, which is what "
    "distinguishes it. A band that is widening proximally over months is behaving in the opposite way."],
   ["Benign longitudinal melanonychia, which typically affects multiple digits",
    "Benign longitudinal melanonychia appears on the differential, and single-digit involvement with proximal "
    "widening is the pattern that argues against it."],
   ["Onychomycosis, causing discoloration of the nail plate",
    "Onychomycosis produces thickening, crumbling, debris, and onycholysis rather than a discrete pigmented "
    "longitudinal band with periungual extension."],
   ["Glomus tumour, causing pain and cold sensitivity",
    "Glomus tumour is a nail unit neoplasm characterised by pain and cold sensitivity rather than by pigmented "
    "longitudinal bands."]],
  0, 84),

Q("Nail unit neoplasms",
  "Why is diagnostic delay a recurring theme in nail unit melanoma, and where does the tumour usually arise?",
  [["It is rare and not clearly ultraviolet driven so may occur in any skin tone, and it arises most often in the "
    "matrix",
    "Correct. Nail unit melanoma is a rare acral melanoma arising most often in the matrix. It is not clearly "
    "ultraviolet driven and may occur in any skin tone, and delayed recognition contributes to worse outcomes."],
   ["It occurs only in fair-skinned patients with heavy sun exposure, and arises in the nail bed",
    "Assuming it is a sun-driven disease of fair skin is exactly the reasoning that produces delay in darker-skinned "
    "patients, and the matrix rather than the bed is the usual origin."],
   ["It always presents with pain, which patients ignore",
    "Pain and cold sensitivity characterise glomus tumour. Nail unit melanoma commonly presents as painless pigment "
    "change."],
   ["It arises in the periungual skin and is easily seen",
    "Matrix tumours cause longitudinal plate changes, and the origin beneath the proximal fold is part of why they "
    "are recognised late."],
   ["It is common and therefore over-diagnosed rather than delayed",
    "It is rare, and rarity combined with an unexpected demographic is what drives delay."]],
  0, 79),

Q("Nail unit neoplasms",
  "What examination step is specified when evaluating a nail for a possible neoplasm?",
  [["Remove polish and inspect every nail",
    "Correct. History and examination should document onset, evolution, trauma, bleeding, pain or cold sensitivity, "
    "prior treatments, medications, immune status, human papillomavirus risk, and personal or family melanoma "
    "history, and polish must be removed so that every nail can be inspected."],
   ["Inspect only the symptomatic nail to avoid unnecessary examination",
    "Comparing every nail is what identifies a single-digit change, which is the pattern that raises melanoma."],
   ["Perform a potassium hydroxide preparation before any inspection",
    "Confirming fungus matters when onychomycosis is suspected, but it does not replace inspection of the nail unit "
    "for a neoplasm."],
   ["Obtain radiographs of all digits routinely",
    "Imaging has selected roles but is not the specified universal examination step."],
   ["Defer examination until pigment has been present for a year",
    "Delayed recognition contributes to worse outcomes, so waiting a year is the opposite of what is advised."]],
  0, 93),

Q("Clinical approach",
  "What is the recommended first step when evaluating any premalignant or malignant cutaneous lesion?",
  [["Characterise the lesion systematically before assigning a diagnosis",
    "Correct. The foundational approach is to describe before naming: characterise each lesion systematically by "
    "primary lesion type, colour, surface texture, border definition, size, distribution, palpability, ulceration, "
    "and bleeding before assigning a diagnosis."],
   ["Assign the most likely diagnosis and then look for supporting features",
    "Naming first and confirming afterwards is the reasoning pattern that produces anchoring, which is why the "
    "sequence is deliberately reversed."],
   ["Biopsy every lesion before description",
    "Biopsy follows assessment, and description determines which lesions need sampling and by what technique."],
   ["Photograph the lesion and review it at the next visit",
    "Serial photography has a role in surveillance but does not substitute for systematic characterisation at the "
    "first encounter."],
   ["Refer every pigmented lesion to dermatology without assessment",
    "Referral criteria exist for specific findings, and describing the lesion is what determines whether they are "
    "met."]],
  0, 4),

Q("Actinic keratosis",
  "What is the relationship between actinic keratosis and keratinocyte carcinoma?",
  [["Actinic keratosis is premalignant and lies on a biologic continuum with keratinocyte carcinoma",
    "Correct. Chronic ultraviolet injury produces dysplastic keratinocytic change in a field of sun-damaged skin. "
    "Actinic keratosis is premalignant and lies on a biologic continuum with keratinocyte carcinoma."],
   ["Actinic keratosis is entirely benign and unrelated to carcinoma",
    "Treating it as benign discards the reason it is identified and treated at all, and the continuum with squamous "
    "cell carcinoma is what makes it worth eradicating."],
   ["Actinic keratosis is a form of invasive carcinoma from the outset",
    "It is a dysplastic change rather than invasive disease. Features suggesting invasion — thickness, induration, "
    "ulceration, bleeding — are what prompt biopsy."],
   ["Actinic keratosis progresses to basal cell carcinoma",
    "The continuum is with keratinocyte carcinoma of squamous type. Basal cell carcinoma arises through a different "
    "route driven by intense intermittent exposure."],
   ["Actinic keratosis progresses to melanoma",
    "Actinic keratosis is a keratinocytic lesion. Melanoma arises from melanocytes."]],
  0, 11),

Q("Basal cell carcinoma",
  "For which basal cell carcinoma is topical therapy an appropriate option, and what must follow it?",
  [["Selected superficial basal cell carcinoma, with clinical clearance confirmed after treatment",
    "Correct. Topical therapy is used for selected superficial basal cell carcinoma — imiquimod five nights weekly "
    "for 6 to 10 weeks or fluorouracil twice daily for up to 12 weeks — and clinical clearance must be confirmed "
    "after treatment."],
   ["All nodular basal cell carcinomas, with no follow-up required",
    "Nodular tumours are not the selected superficial subset, and confirming clearance is specifically required "
    "whatever is treated topically."],
   ["High-risk facial tumours, as an alternative to Mohs surgery",
    "High-risk anatomic sites are exactly where Mohs surgery is indicated, because tissue sparing and margin control "
    "matter most there."],
   ["Recurrent tumours after surgical excision",
    "Recurrence is a listed indication for Mohs surgery rather than for topical therapy."],
   ["Any basal cell carcinoma the patient prefers not to have excised",
    "Patient preference matters but does not make topical therapy appropriate for a tumour whose subtype and site "
    "call for surgery."]],
  0, 37, IO_11),

Q("Squamous cell carcinoma",
  "Which findings in a keratotic lesion are red flags for squamous cell carcinoma?",
  [["Rapid growth, pain, bleeding, and ulceration",
    "Correct. Red flags for squamous cell carcinoma include rapid growth, pain, bleeding, and ulceration, and the "
    "same features in an actinic keratosis prompt biopsy to exclude early carcinoma."],
   ["Sandpaper texture and small size",
    "A sandpapery 0.2 to 0.6 cm papule is the description of an uncomplicated actinic keratosis, which is the lesion "
    "these red flags distinguish from."],
   ["A pearly translucent surface with telangiectasias",
    "Pearly translucency with telangiectasias is the hallmark of nodular basal cell carcinoma."],
   ["A stuck-on appearance with comedone-like openings",
    "That describes seborrheic keratosis, a benign lesion, though an inflamed seborrheic keratosis does appear on the "
    "squamous cell carcinoma differential."],
   ["Colour variegation with border irregularity",
    "Colour variegation and irregular borders are melanoma recognition features under the ABCDE rule."]],
  0, 22),

Q("Kaposi sarcoma",
  "What causes Kaposi sarcoma, and what does it arise from?",
  [["Human herpesvirus 8, arising in the cells lining blood and lymph vessels",
    "Correct. Kaposi sarcoma develops in the cells lining blood and lymph vessels and is associated with human "
    "herpesvirus 8. It produces red or purple macules, plaques, or nodules on skin or mucous membranes and can "
    "involve internal organs."],
   ["Human papillomavirus, arising in keratinocytes",
    "Human papillomavirus infects keratinocytes and produces warts. Kaposi sarcoma is a vascular endothelial "
    "neoplasm."],
   ["Human immunodeficiency virus directly infecting endothelial cells",
    "Human immunodeficiency virus creates the immunodeficiency that permits epidemic disease, but human herpesvirus 8 "
    "is the causative agent, which is why the classic and endemic forms occur without it."],
   ["Ultraviolet radiation damaging dermal fibroblasts",
    "Ultraviolet damage drives keratinocyte carcinomas and melanoma rather than this vascular tumour."],
   ["Malignant T cells migrating to the skin",
    "Malignant T cells migrating to the skin describes cutaneous T-cell lymphoma."]],
  0, 63),
]
