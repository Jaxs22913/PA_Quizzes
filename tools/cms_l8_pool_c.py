# CMS I Lecture 8 (Pigmented Skin Lesions) — SET 1 pool C (objective style).
# Cross-lesion discrimination and the adult/elderly care-strategy objective.
# Pools A and B totalled 53, seven short of the 60 the two forms need.
#
# Options drafted at matched lengths, with every distractor given the same
# compound shape as the answer it sits beside.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "CMS I Pigmented Skin Lesions - Shahsv-2.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective a — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis of pigmented skin lesions"
IOB = "Objective b — Medical care strategies for pigmented skin lesions in adult and elderly populations"

POOL_C = [
 dict(topic="Ephelides", io=IOA,
   q="Which single feature best separates ephelides from lentigines?",
   opts=[
     ["Ephelides fade when sun exposure stops, whereas lentigines do not",
      "Correct — lentigines are the main differential diagnosis for ephelides."],
     ["Ephelides are darker than lentigines and have irregular borders",
      "Lentigines are uniformly black or brown with well-circumscribed borders."],
     ["Ephelides occur only on sun-exposed skin, whereas lentigines do not",
      "Ephelides are commonest on sun-exposed skin but are not limited to it."],
     ["Ephelides require biopsy for diagnosis, whereas lentigines do not",
      "Both are diagnosed clinically."]],
   c=0, cite=c(5)),

 dict(topic="Dermatosis papulosa nigrans", io=IOA,
   q="Which lesion is dermatosis papulosa nigrans described as identical to?",
   opts=[
     ["Small seborrheic keratoses",
      "Correct — the distinction is in the epidemiology and the distribution on face and neck."],
     ["Small solar lentigines",
      "Those are macular rather than papular."],
     ["Small blue naevi of the face",
      "Those are blue to blue-black and sit in the dermis."],
     ["Small dysplastic naevi",
      "Those have irregular indistinct borders and variable pigmentation."]],
   c=0, cite=c(19)),

 dict(topic="Seborrheic keratosis", io=IOB,
   q="Why do seborrheic keratoses matter clinically in older adults, given that they are benign?",
   opts=[
     ["They are easily mistaken for neoplasms",
      "Correct — the diagnosis is clinical and management is supportive."],
     ["They frequently transform into melanoma",
      "They are benign without malignant potential."],
     ["They indicate an underlying malignancy",
      "That association belongs to acanthosis nigricans."],
     ["They spread from person to person",
      "They are not infectious."]],
   c=0, cite=c(17)),

 dict(topic="Vitiligo", io=IOA,
   q="Why is it important to distinguish segmental from non-segmental vitiligo?",
   opts=[
     ["The two differ in their diagnostic tools and in their treatment",
      "Correct — segmental disease is unilateral, does not cross the midline, and follows block-like patterns."],
     ["Only segmental disease fluoresces under a Wood's lamp examination",
      "Both fluoresce under a Wood's lamp in a dark room."],
     ["Only segmental disease carries a risk of malignant transformation",
      "Neither form is described as carrying malignant risk."],
     ["Only segmental disease affects patients under thirty years of age",
      "Vitiligo generally usually starts before the thirties."]],
   c=0, cite=c(23)),

 dict(topic="Vitiligo", io=IOA,
   q="What information should be gathered before deciding vitiligo management?",
   opts=[
     ["A thorough examination with medical, social and family history and demographics",
      "Correct — management is multifactorial and depends on the extent of disease."],
     ["A skin biopsy of the leading edge sent for histology and antigen mapping",
      "Biopsy is not the described approach for vitiligo."],
     ["A dermoscopic photograph of every lesion recorded for later comparison",
      "Dermoscopy is not the described approach for vitiligo."],
     ["A minimal erythema dose test to ultraviolet A and ultraviolet B light",
      "That is used in the photosensitivity workup."]],
   c=0, cite=c(24)),

 dict(topic="Melanocytic naevi", io=IOA,
   q="Which feature defines a dysplastic naevus within the melanocytic naevus group?",
   opts=[
     ["Atypical architectural and cytologic features",
      "Correct — the other two divisions are acquired and congenital naevi by their cell of origin."],
     ["Origin from neural-crest derived precursor cells",
      "That defines congenital melanocytic naevi."],
     ["Origin from junctional melanocytes in the epidermis",
      "That defines acquired naevi."],
     ["Deep dermal spindle or epithelioid melanocytes",
      "That defines blue naevi."]],
   c=0, cite=c(27)),

 dict(topic="Common acquired naevus", io=IOB,
   q="A dark brown or black naevus on light skin is described as suspicious. What is the expected colour of a common acquired naevus?",
   opts=[
     ["Skin coloured, brown or pink, with a homogenous surface and colour",
      "Correct — they are usually under 6 mm, round to oval, and sharply demarcated."],
     ["Blue, blue-grey or blue-black, with pigment sitting deep in the dermis",
      "That describes blue naevus."],
     ["Jet-black with shades of blue, grey or brown, sharply circumscribed",
      "That describes pigmented spindle cell naevus."],
     ["Pink or red, hairless, firm and dome-shaped on the face or trunk",
      "That describes Spitz naevus."]],
   c=0, cite=c(36)),

 dict(topic="Congenital melanocytic naevi", io=IOA,
   q="Which condition is named as a risk factor associated with congenital melanocytic naevi?",
   opts=[
     ["Neurofibromatosis type I",
      "Correct — congenital naevi also carry a high risk of developing into melanoma."],
     ["Dysplastic naevus syndrome",
      "That is the syndrome associated with dysplastic naevi."],
     ["Familial cancer syndrome",
      "That association is named for multiple Spitz naevi."],
     ["LAMB and myxoma syndrome",
      "Those are inherited associations of lentigines."]],
   c=0, cite=c(28)),

 dict(topic="Spitz naevus", io=IOA,
   q="How is the diagnosis of Spitz naevus established?",
   opts=[
     ["By biopsy or by wide excision of the lesion",
      "Correct — management is by excision, since it can resemble melanoma."],
     ["By clinical examination alone in every case",
      "It sometimes resembles melanoma, so tissue diagnosis is needed."],
     ["By Wood's lamp examination in a dark room",
      "That is used in vitiligo."],
     ["By dermoscopy showing a moth-eaten border",
      "That dermoscopic sign belongs to solar lentigo."]],
   c=0, cite=c(42)),

 dict(topic="Blue naevus", io=IOA,
   q="Where do blue naevi most commonly occur?",
   opts=[
     ["The dorsal hands and feet, scalp, buttocks or sacral region",
      "Correct — the lesions are blue, blue-grey or blue-black."],
     ["The trunk and extremities, with the scalp and face also affected",
      "That is the distribution of congenital melanocytic naevi."],
     ["The lower extremities and mainly the thigh in women in their thirties",
      "That is the distribution of pigmented spindle cell naevus."],
     ["The face and neck in dark-skinned patients, with females predominating",
      "That is the distribution of dermatosis papulosa nigrans."]],
   c=0, cite=c(39)),

 dict(topic="Dysplastic naevus", io=IOB,
   q="What relationship does the lecture draw between naevus count and melanoma risk?",
   opts=[
     ["The higher the number of naevi, the higher the risk of melanoma",
      "Correct — in dysplastic naevus syndrome there can be over one hundred by adolescence."],
     ["The higher the number of naevi, the lower the risk of melanoma",
      "That reverses the relationship."],
     ["Naevus count has no bearing at all on the risk of melanoma",
      "The relationship is explicitly stated."],
     ["Only naevi over 10 mm contribute to the risk of melanoma",
      "Dysplastic naevi are defined at 5 mm or larger."]],
   c=0, cite=c(43)),

 dict(topic="Solar lentigo", io=IOA,
   q="Into what can solar lentigines progress over time?",
   opts=[
     ["Lichenoid keratoses",
      "Correct — they may also enlarge, darken, stay stable or regress."],
     ["Seborrheic keratoses",
      "That is a separate benign lesion rather than a progression."],
     ["Dysplastic naevi",
      "Those are melanocytic naevi with atypical features."],
     ["Blue naevi",
      "Those are dermal melanocytic lesions."]],
   c=0, cite=c(14)),

 dict(topic="Naevus spilus", io=IOA,
   q="What does the background pigmentation of a naevus spilus resemble?",
   opts=[
     ["A café-au-lait spot, circumscribed with even light pigmentation",
      "Correct — scattered darker macules or papules sit superimposed on it."],
     ["A solar lentigo, with irregular borders that coalesce at sunburn sites",
      "That describes solar lentigo itself."],
     ["A vitiligo patch, white and non-scaly with distinct margins",
      "That describes vitiligo, which is depigmented rather than tan."],
     ["A blue naevus, deeply pigmented and blue-grey to blue-black",
      "That describes blue naevus."]],
   c=0, cite=c(33)),

 dict(topic="Ephelides", io=IOA,
   q="Why is cryotherapy not used for ephelides?",
   opts=[
     ["The lesions are too small for it to be practical",
      "Correct — intense pulsed light or lasers are preferred, though lesions can relapse."],
     ["The lesions would recur immediately after treatment",
      "Relapse is described for laser rather than as the reason to avoid cryotherapy."],
     ["It causes post-inflammatory hyperpigmentation in them",
      "That is the reason cryotherapy is avoided in dermatosis papulosa nigrans."],
     ["It carries a risk of transforming them into melanoma",
      "Ephelides are benign and have no such risk."]],
   c=0, cite=c(7)),

 dict(topic="Vitiligo", io=IOB,
   q="Which non-pharmacologic elements are named in the management of vitiligo?",
   opts=[
     ["Psychological intervention, cosmetic therapies and non-traditional approaches",
      "Correct — the psychological and social impact is emphasised."],
     ["Sun protection counselling with a broad-spectrum sunscreen used daily",
      "That is the education named for naevi and pigmented lesions."],
     ["Weight loss, smoking cessation and avoidance of constrictive clothing",
      "Those belong to hidradenitis suppurativa."],
     ["Household washing at high temperature and treatment of all contacts",
      "That belongs to the infestations lecture."]],
   c=0, cite=c(25)),
]
