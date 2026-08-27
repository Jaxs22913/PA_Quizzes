# -*- coding: utf-8 -*-
"""Pigmented Skin Lesions (Shah) -- pool for the Updated CMS derm master exams."""
DECK = "CMS I Pigmented Skin Lesions - Shahsv-2.pptx"
IO_A = ("a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing, management, appropriate referrals, patient education, "
        "and prognosis of pigmented skin lesions")
IO_B = "b — Identify medical care strategies for pigmented skin lesions in adult and elderly populations"

def Q(topic, q, opts, c, slide, io=IO_A):
    return {"topic": topic, "io": io, "q": q, "opts": opts, "c": c, "cite": f"{DECK}, Slide {slide}"}

QUESTIONS = [

Q("Ephelides",
  "A 9-year-old girl with red hair has multiple small light brown symmetric macules 3 to 5 mm across her nose and "
  "cheeks. Her mother reports they darken every summer and fade in winter. What is the inheritance pattern, and what "
  "treatment is specifically not used?",
  [["Autosomal dominant inheritance, and cryotherapy is not used because of the small size of the lesions",
    "Correct. Ephelides, or freckles, are autosomal dominant and appear most commonly on sun-exposed skin of "
    "fair-skinned individuals, often with blonde or red hair. They become more pronounced in spring and summer and "
    "fade in winter. Cryotherapy is not used because it is difficult given the size of the lesions."],
   ["Autosomal recessive inheritance, and cryotherapy is first-line treatment",
    "Both halves fail: the pattern is dominant, and cryotherapy is specifically excluded because of lesion size."],
   ["Somatic mutation, and surgical excision is first line",
    "Somatic mutations underlie congenital melanocytic naevi and nevus spilus. Excising freckles would produce scars "
    "far more conspicuous than the lesions."],
   ["Autosomal dominant inheritance, and permanent removal is expected with a single treatment",
    "The inheritance is right but no single treatment removes them permanently, and they regress later in life "
    "anyway. Sun protection and counselling are the key measures."],
   ["X-linked inheritance, with equal treatment response in all skin types",
    "The pattern is autosomal dominant with equal frequency in males and females, which an X-linked pattern would not "
    "produce."]],
  0, 7),

Q("Lentigines",
  "How does a simple lentigo differ from an ephelis in its relationship to sun exposure?",
  [["Lentigines occur on both sun-exposed and sun-protected areas and do not fade in winter, whereas ephelides are "
    "most prominent on sun-exposed skin and fade seasonally",
    "Correct. Lentigines are benign, well-circumscribed, round to oval uniformly black or brown macules under 5 mm "
    "occurring on skin, conjunctiva, and mucocutaneous surfaces, on both sun-exposed and sun-protected areas. "
    "Ephelides are most pronounced in spring and summer and fade in winter."],
   ["Lentigines occur only on sun-exposed skin and fade in winter",
    "That describes ephelides. Attributing seasonal variation to lentigines would lead a clinician to expect fading "
    "that never comes."],
   ["Lentigines are always larger than 2 cm",
    "Simple lentigines are less than 5 mm in diameter. It is solar lentigines that range from under 1 mm to several "
    "centimetres."],
   ["Lentigines never occur on mucous membranes",
    "They occur on skin, conjunctiva, and mucocutaneous surfaces, and they can be associated with inherited "
    "syndromes."],
   ["Lentigines require excision in every case",
    "Diagnosis is clinical and treatment is not necessary, with cosmetic removal by cryotherapy or quality-switched "
    "laser if the patient prefers."]],
  0, 10),

Q("Solar lentigo",
  "A 63-year-old man has multiple light to dark brown macules with well-defined but irregular borders that tend to "
  "coalesce over his shoulders, where he has had severe sunburns. What is the underlying process and its "
  "epidemiological association?",
  [["Proliferation of basal melanocytes with increased melanin production, strongly associated with older age, sun "
    "damage, and tanning",
    "Correct. Solar lentigines arise from proliferation of basal melanocytes with increased melanin production and "
    "are strongly associated with older age, present in about 90 percent by age 50, along with sun damage, tanning, "
    "a history of ephelides, and birth control use."],
   ["T cell mediated destruction of melanocytes",
    "T cell mediated destruction of melanocytes causes vitiligo, which produces depigmented rather than "
    "hyperpigmented lesions."],
   ["Proliferation of dermal capillaries",
    "Capillary proliferation produces cherry angiomas, which are red and blanchable rather than brown macules."],
   ["Somatic mutation present from birth",
    "Somatic mutations underlie congenital melanocytic naevi, which are evident at birth or shortly after rather than "
    "acquired with cumulative sun exposure."],
   ["Hyperinsulinaemia stimulating keratinocyte proliferation",
    "That mechanism produces acanthosis nigricans, a velvety hyperpigmented thickening of body folds."]],
  0, 13, IO_B),

Q("Seborrheic keratosis",
  "A 70-year-old woman has several beige to dark brown papules and plaques 5 to 15 mm on the trunk that feel velvety "
  "and appear stuck onto the skin surface. What is the diagnosis, and what is the clinical significance?",
  [["Seborrheic keratoses, which are benign but are easily mistaken for neoplasms",
    "Correct. Seborrheic keratoses are benign papules and plaques, beige to brown to black, 2 to 20 mm in diameter, "
    "feeling velvety or warty and appearing stuck or pasted onto the skin. They are common in older adults and are "
    "easily mistaken for neoplasms."],
   ["Malignant melanoma, requiring urgent excisional biopsy",
    "The stuck-on appearance and velvety texture are characteristic of a benign keratosis, though the resemblance to "
    "neoplasm is exactly why the lesion is taught. Genuine asymmetry, border irregularity, or colour variation would "
    "change the assessment."],
   ["Solar lentigines, which are flat macules rather than raised",
    "Solar lentigines are macules — flat, without elevation. These lesions are raised papules and plaques with a "
    "palpable velvety surface."],
   ["Dermatosis papulosa nigrans, which occurs only on the trunk",
    "Dermatosis papulosa nigrans lesions are identical to small seborrheic keratoses but are 1 to 5 mm and occur on "
    "the face and neck rather than the trunk."],
   ["Congenital melanocytic naevi, present since birth",
    "Congenital naevi are evident at birth or shortly after, whereas seborrheic keratoses are acquired lesions of "
    "older adults."]],
  0, 17, IO_B),

Q("Dermatosis papulosa nigrans",
  "A 42-year-old Black woman has multiple small, smooth, firm dark brown papules 1 to 3 mm on the face and neck. What "
  "is the diagnosis, and how does it relate to seborrheic keratosis?",
  [["Dermatosis papulosa nigrans, whose lesions are identical to small seborrheic keratoses",
    "Correct. Dermatosis papulosa nigrans consists of multiple small, smooth, firm black or dark brown papules 1 to "
    "5 mm on the face and neck, identical to small seborrheic keratoses. It is thought to be genetic and is believed "
    "to be a developmental defect of the hair follicle."],
   ["Dermatosis papulosa nigrans, which is a premalignant variant of seborrheic keratosis",
    "The lesion is identified correctly but it is not premalignant. Framing a benign genetic condition as "
    "premalignant would prompt unnecessary destructive treatment on facial skin prone to dyspigmentation."],
   ["Multiple lentigines, which occur on sun-exposed skin only",
    "Lentigines are macules occurring on both sun-exposed and sun-protected skin. These lesions are raised papules."],
   ["Syringomas, which are eccrine duct neoplasms",
    "Syringomas are skin-coloured 1 to 2 mm papules of the lower eyelids appearing at puberty rather than dark brown "
    "papules of the face and neck."],
   ["Melanocytic naevi, which peak in number in the third decade",
    "Common acquired naevi are usually under 6 mm with homogeneous surface and colour and peak in the thirties. "
    "Dermatosis papulosa nigrans lesions are keratinocytic rather than melanocytic."]],
  0, 19),

Q("Vitiligo",
  "A 24-year-old woman has symmetrical, well-defined white non-scaly macules and patches on the dorsal hands and "
  "around the mouth. They fluoresce under a Wood's lamp. What is the underlying mechanism?",
  [["T cell mediated autoimmune destruction of melanocytes",
    "Correct. Vitiligo is a common autoimmune disease causing depigmentation through T cell mediated destruction of "
    "melanocytes. It can begin at any age but usually starts before the thirties, with half of patients presenting "
    "before their twenties."],
   ["Reduced melanin production by intact melanocytes",
    "The melanocytes are destroyed rather than merely underactive, which is why the depigmentation is complete and "
    "the patches fluoresce under a Wood's lamp."],
   ["Overgrowth of Malassezia altering melanocyte function",
    "Malassezia overgrowth causes pityriasis versicolor, in which hypopigmentation reflects altered melanocyte "
    "function and reduced tanning. Its lesions are scaly and pigment recovery follows treatment, unlike vitiligo."],
   ["Proliferation of basal melanocytes with increased melanin",
    "That process produces solar lentigines, which are hyperpigmented rather than depigmented."],
   ["Postinflammatory loss of pigment after a dermatitis",
    "Postinflammatory change requires preceding inflammation at the site and produces partial rather than complete "
    "depigmentation with indistinct rather than distinct margins."]],
  0, 21),

Q("Vitiligo",
  "A patient with vitiligo affecting more than 5 percent of the body surface area is being counselled on treatment. "
  "What is first-line, and why is one phototherapy option preferred over another?",
  [["Phototherapy is first line above 5 percent body surface area, with narrow band ultraviolet B preferred over "
    "psoralen with ultraviolet A because the latter increases skin cancer risk",
    "Correct. Phototherapy is first line in patients with more than 5 percent body surface area involvement, and "
    "narrow band ultraviolet B is preferred over psoralen with ultraviolet A, which carries adverse effects including "
    "increased skin cancer risk. Combination of topical therapy with phototherapy is ideal."],
   ["Topical therapy alone is first line at any extent of disease",
    "Topical therapy is used when there is limited surface involvement below 5 percent. Relying on it for extensive "
    "disease under-treats the patient."],
   ["Psoralen with ultraviolet A is preferred because it carries fewer adverse effects",
    "This inverts the safety comparison. Psoralen with ultraviolet A is the option associated with increased skin "
    "cancer risk, which is why narrow band ultraviolet B is preferred."],
   ["Surgical grafting is first line for all patients",
    "Management is multifactorial and depends on the extent of disease, with topical therapy and phototherapy "
    "preceding surgical approaches."],
   ["No treatment is available, so counselling alone is appropriate",
    "Effective options exist across the range of disease extent, and withholding them would leave a treatable "
    "condition untreated."]],
  0, 25),

Q("Congenital melanocytic naevi",
  "An infant is born with a large pigmented plaque over the posterior scalp and upper back. What relationship governs "
  "melanoma risk, and what additional evaluation should be considered?",
  [["The larger the lesion the higher the melanoma risk, and magnetic resonance imaging of the brain with or without "
    "the spine should be considered for neurocutaneous melanosis given the head and axial location",
    "Correct. Congenital melanocytic naevi arise from somatic mutations and are evident at birth or shortly after. "
    "The larger the lesion, the higher the risk for melanoma. With naevi on the head or axial locations, "
    "neurocutaneous melanosis must be considered, and magnetic resonance imaging of the brain with or without the "
    "total spine is obtained concordant with the anatomic location."],
   ["The smaller the lesion the higher the melanoma risk, with no imaging indicated",
    "The size relationship is inverted, and omitting imaging for a large head and axial naevus would miss "
    "neurocutaneous melanosis."],
   ["Melanoma risk is unrelated to size, and imaging is never indicated",
    "Size is the principal determinant of risk, and imaging has a defined role in specific anatomical distributions."],
   ["The larger the lesion the higher the risk, and complete excision is mandatory in every case",
    "The size relationship is right but management depends on melanoma risk together with cosmetic and functional "
    "considerations. The goal is to remove as much as possible while preserving function, decided per patient rather "
    "than mandated."],
   ["The lesion always regresses spontaneously, so observation alone suffices",
    "Congenital naevi persist. It is the common acquired naevus that enlarges, stabilises, and eventually regresses."]],
  0, 30),

Q("Nevus spilus",
  "A child has a circumscribed light brown patch on the trunk resembling a café au lait spot, within which several "
  "darker pigmented macules and papules are visible. What is this lesion and how is it managed?",
  [["Nevus spilus, a variant of congenital naevus, managed with observation, periodic clinical evaluation, and sun "
    "protection counselling",
    "Correct. Nevus spilus, the spotted nevus, is a variant of congenital naevus present at birth or in the first "
    "years of life, most commonly on the trunk and extremities. Darkly pigmented macules or papules sit within a "
    "background that is circumscribed and similar in appearance to a café au lait spot, and it rarely progresses to "
    "melanoma. Management is observation, periodic evaluation, and sun protection."],
   ["Nevus spilus, requiring immediate complete excision because of high melanoma risk",
    "The lesion is identified correctly but it rarely progresses to melanoma, so routine excision is not warranted."],
   ["A café au lait macule of neurofibromatosis type 1",
    "Café au lait macules are uniform light tan to brown macules without darker macules within them, and their size "
    "thresholds define significance in neurofibromatosis."],
   ["A dysplastic naevus requiring biopsy",
    "A dysplastic naevus is at least 5 mm with irregular indistinct borders and is diagnosed by biopsy. Its "
    "appearance does not include discrete darker spots on a café au lait background."],
   ["A blue nevus arising in adolescence",
    "Blue naevi are blue, blue-grey, or blue-black lesions of the dorsal hands and feet, scalp, buttocks, or sacral "
    "region."]],
  0, 34),

Q("Melanocytic naevi",
  "A 32-year-old fair-skinned woman has numerous moles under 6 mm with homogeneous surface and colour. One lesion is "
  "very dark brown to black. What is the significance of that lesion?",
  [["A very dark brown or black naevus on a light-skinned individual is suspicious and warrants further evaluation",
    "Correct. Common acquired melanocytic naevi are usually less than 6 mm with homogeneous surface and colour, round "
    "to oval with sharp demarcation. A very dark brown or black lesion on a light-skinned individual is specifically "
    "flagged as suspicious."],
   ["A very dark naevus is expected in patients with numerous moles and requires no action",
    "Increased numbers of moles do raise melanoma risk, which makes this superficially reassuring reasoning. But a "
    "single lesion diverging in colour from its neighbours is the specific finding singled out as suspicious."],
   ["It represents a blue nevus and requires no evaluation",
    "Blue naevi are blue, blue-grey, or blue-black and occur at characteristic sites including the dorsal hands and "
    "feet, scalp, and sacral region, and larger lesions are biopsied."],
   ["It indicates a Spitz nevus, which is always benign",
    "Spitz naevi are solitary, pink or red, hairless, firm, and dome-shaped, usually benign but sometimes resembling "
    "melanoma. They are not dark brown or black."],
   ["It confirms melanoma without need for biopsy",
    "Suspicion warrants evaluation and biopsy rather than a diagnosis made on colour alone."]],
  0, 36, IO_B),

Q("Blue nevus",
  "What are blue naevi composed of, and how does management differ by lesion size?",
  [["Deeply pigmented spindle or epithelioid melanocytes in the dermis, diagnosed clinically when small and by biopsy "
    "when larger",
    "Correct. Blue naevi are composed of deeply pigmented spindle or epithelioid melanocytes in the dermis. Diagnosis "
    "is clinical for small lesions and by biopsy for larger ones, with observation and biopsy or excision if changes "
    "are noted."],
   ["Deeply pigmented melanocytes in the epidermis, always diagnosed clinically",
    "The melanocytes lie in the dermis, which is what gives the lesion its blue colour, and larger lesions require "
    "biopsy rather than clinical diagnosis alone."],
   ["Proliferating keratinocytes, requiring cryotherapy",
    "Keratinocytic proliferation describes seborrheic keratosis. Blue naevi are melanocytic."],
   ["Lipid-laden macrophages, requiring lipid screening",
    "Lipid-laden macrophages form xanthelasma, which warrants hyperlipidaemia screening."],
   ["Dilated dermal capillaries, blanching with pressure",
    "Dilated dermal vessels produce vascular lesions that blanch. Blue naevi are pigmented and do not blanch."]],
  0, 40),

Q("Pigmented spindle cell naevus",
  "A 33-year-old woman has a sharply circumscribed, darkly pigmented papule under 7 mm on the thigh. What is this "
  "lesion also called, and what is its typical demographic?",
  [["Reed nevus, occurring commonly in the thirties with a female predominance, typically on the lower extremities",
    "Correct. Pigmented spindle cell nevus, also called Reed nevus, occurs commonly in the thirties with females "
    "affected more than males, found on the extremities and mainly the lower extremities, especially the thigh. It is "
    "a sharply circumscribed darkly pigmented papule usually less than 7 mm."],
   ["Spitz nevus, occurring mainly in children on the face and neck",
    "Spitz naevus is a separate lesion — solitary, pink or red, hairless, firm, and dome-shaped, usually on the face, "
    "neck, or extremities, sometimes resembling melanoma."],
   ["Blue nevus, arising in adolescence on the dorsal hands",
    "Common blue naevi are deeply pigmented lesions under 1 cm arising in adolescence at characteristic sites."],
   ["Dysplastic naevus, defined by irregular indistinct borders",
    "A dysplastic naevus is at least 5 mm with irregular, indistinct borders, whereas the Reed nevus is sharply "
    "circumscribed."],
   ["Congenital melanocytic nevus, present at birth",
    "Congenital naevi are evident at birth or shortly after rather than appearing in adulthood."]],
  0, 41),

Q("Spitz naevus",
  "A 7-year-old has a solitary, asymptomatic, pink, hairless, firm dome-shaped papule on the cheek that grew over "
  "several weeks and has since been stable. What is the diagnosis, and what is the diagnostic concern?",
  [["Spitz nevus, which is usually benign but sometimes resembles melanoma",
    "Correct. A Spitz nevus is usually benign with a phase of growth, fast or slow, followed by a stable period. It "
    "is solitary, asymptomatic, pink or red, hairless, firm, and dome-shaped, several millimetres to centimetres, "
    "usually on the face, neck, or extremities, and it sometimes resembles melanoma."],
   ["Pigmented spindle cell nevus, which is darkly pigmented",
    "The Reed nevus is a sharply circumscribed darkly pigmented papule on the extremities of adults in their "
    "thirties, not a pink dome-shaped lesion in a child."],
   ["Pyogenic granuloma, which bleeds easily after trauma",
    "Pyogenic granuloma is a bright red friable lesion that grows rapidly after injury and bleeds spontaneously."],
   ["Molluscum contagiosum, with central umbilication",
    "Molluscum lesions are pearly dome-shaped papules with characteristic central umbilication, and they are usually "
    "multiple."],
   ["Common acquired melanocytic nevus, which is uniformly brown",
    "Common acquired naevi are skin-coloured, brown, or pink with homogeneous colour and are usually under 6 mm, and "
    "they develop slowly rather than growing over weeks."]],
  0, 42),

Q("Dysplastic naevus",
  "A 38-year-old man with a family history of melanoma has more than 100 naevi, several at least 5 mm with irregular, "
  "indistinct borders. How is a dysplastic naevus diagnosed, and what is the management?",
  [["Diagnosis is by biopsy, with observation, biopsy of all changing or developing lesions, excision where melanoma "
    "is a concern, and sun protection",
    "Correct. Diagnosis of a dysplastic melanocytic nevus is by biopsy. Management includes observation, biopsy of "
    "all changing or developing lesions, excision where there is concern for melanoma, and sun protection. Family "
    "history is a risk factor, and dysplastic nevus syndrome may produce over 100 naevi by adolescence."],
   ["Diagnosis is clinical, and no biopsy is required at any point",
    "Clinical suspicion prompts the biopsy that establishes the diagnosis. Relying on inspection alone in a patient "
    "with dysplastic nevus syndrome and a family history of melanoma forfeits the histology that distinguishes "
    "dysplasia from melanoma."],
   ["Diagnosis is by biopsy, and all naevi should be excised prophylactically",
    "The diagnostic method is right but excising more than a hundred lesions is neither practical nor indicated. "
    "Excision is directed at lesions where melanoma is a concern."],
   ["Diagnosis is by dermoscopy alone, with no histology needed",
    "Dermoscopy assists assessment but biopsy is what establishes this diagnosis."],
   ["No follow-up is needed once the lesions are documented",
    "Changing or developing lesions must be biopsied, which requires ongoing surveillance rather than a single "
    "documentation visit."]],
  0, 44, IO_B),

Q("Ephelides",
  "What is the cornerstone of management for ephelides?",
  [["Sun protection, with patient education and counselling as the key element",
    "Correct. Sun protection is the cornerstone of management for ephelides, with proper patient education and "
    "counselling described as key. Topical depigmenting agents such as hydroquinone, retinoids, alpha-hydroxy acids, "
    "and botanicals may be used, and intense pulsed light is an option."],
   ["Cryotherapy applied to each lesion",
    "Cryotherapy is specifically excluded because it is difficult given the small size of the lesions."],
   ["Surgical excision of each macule",
    "Excising freckles would leave scars more conspicuous than the pigment, and the lesions regress later in life."],
   ["Systemic depigmenting therapy",
    "Depigmenting agents used are topical rather than systemic."],
   ["No management is possible or appropriate",
    "Sun protection, counselling, and topical depigmenting agents are all available, so the condition is not simply "
    "untreatable."]],
  0, 7),
]
