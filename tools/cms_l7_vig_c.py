# CMS I Lecture 7 (Benign Skin Lesions) — SET 2, vignette pool C.
# The vascular lesions, neurofibromatosis, xanthelasma, lipoma, digital mucous
# cyst and sebaceous hyperplasia.
#
# The lecture's own discussion questions live in this territory -- nevus
# flammeus versus infantile hemangioma, and the finger-pad lesion that bleeds
# after injury. Those two contrasts are asked several ways here because the
# professor chose to test them himself.
#
# Correct answers kept SHORT; the detail sits in the explanation the student
# reads after answering.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "7. Benign Skin Lesions Prof Griffenkranz 8-25-2025-2.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis for benign skin lesions"
IOB = "b — Identify medical strategies for common benign skin lesions in infants, adolescents, adults and the elderly"

VIG_C = [
 dict(topic="Infantile hemangioma", io=IOB, lead="diagnosis",
   q="A 6-week-old former preterm girl has a bright red raised plaque on her scalp. Her mother says the area first looked pale, then developed fine red lines, and has grown noticeably in the last three weeks. Which is the most likely diagnosis?",
   opts=[
     ["Infantile hemangioma",
      "Correct — the earliest sign is blanching of the involved skin, then fine telangiectasias, then a red or crimson macule, then rapid proliferation. The superficial type is the commonest."],
     ["Nevus flammeus",
      "That is present at birth as a flat blanchable patch and does not proliferate."],
     ["Nevus simplex",
      "A stork bite is a pink patch that becomes obvious with crying and fades within a year."],
     ["Pyogenic granuloma",
      "That follows minor trauma and bleeds readily, and is not typical at this age."]],
   c=0, cite=c(65)),

 dict(topic="Infantile hemangioma", io=IOB, lead="education",
   q="A 6-week-old former preterm girl has a bright red raised plaque on her scalp. Her mother says the area first looked pale, then developed fine red lines, and now asks whether it will need surgery. Which is the most appropriate answer?",
   opts=[
     ["Most involute on their own over several years",
      "Correct — complete involution in fifty per cent by age five, seventy per cent by seven and ninety per cent by nine, so serial observation is often all that is needed."],
     ["It will grow with her throughout life and will not involute",
      "That is nevus flammeus."],
     ["It will fade within her first year without any treatment",
      "That is nevus simplex."],
     ["It will regress over three to six months after a period of stability",
      "That is the keratoacanthoma's triphasic course."]],
   c=0, cite=c(66)),

 dict(topic="Infantile hemangioma", io=IOB, lead="next step",
   q="A 4-month-old has a rapidly enlarging periorbital hemangioma that is beginning to obstruct the visual axis. Which is the most appropriate next step?",
   opts=[
     ["Begin treatment, because functional involvement is an indication",
      "Correct — cosmetic concern, functional involvement, deep ulceration and infection all indicate treatment."],
     ["Continue serial observation, since most lesions involute",
      "Involution is the rule, but blocked vision cannot wait for it."],
     ["Refer for surgical excision as the first-line option",
      "Excision is an option, but it is not first line."],
     ["Reassure and review in six months",
      "A six-month delay risks permanent visual consequences."]],
   c=0, cite=c(73)),

 dict(topic="Infantile hemangioma", io=IOB, lead="treatment",
   q="A 4-month-old has a rapidly enlarging periorbital hemangioma that is beginning to obstruct the visual axis, and is to be treated medically. Which is the first-line option?",
   opts=[
     ["A beta-blocker",
      "Correct — oral propranolol or topical timolol, whose mechanism is not well understood. Corticosteroids are the other named first-line treatment."],
     ["Intralesional fluorouracil",
      "That is a keloid treatment."],
     ["Oral isotretinoin",
      "That is mentioned for syringoma, where it increases recurrence risk."],
     ["Intralesional methotrexate",
      "That is used before excising a keratoacanthoma."]],
   c=0, cite=c(73)),

 dict(topic="Nevus flammeus", io=IOB, lead="diagnosis",
   q="A 2-year-old boy has a flat, blanchable, pink-purple patch on one side of his face that stops sharply at the midline. His parents say it has been there since birth, has grown in proportion with him, and is darker when he cries. Which is the most likely diagnosis?",
   opts=[
     ["Nevus flammeus",
      "Correct — present at birth, unilateral with sharp midline cutoff, no involution."],
     ["Infantile hemangioma",
      "That proliferates and then involutes, and is not present in this form at birth."],
     ["Nevus simplex",
      "A stork bite sits on the head and neck and usually fades within a year."],
     ["Cherry angioma",
      "That is an acquired adult lesion, a small firm deep red papule."]],
   c=0, cite=c(80)),

 dict(topic="Nevus flammeus", io=IOB, lead="education",
   q="A 2-year-old boy has a flat, blanchable, pink-purple patch on one cheek that has been present since birth and stops sharply at the midline. His parents ask what it will do as he grows. Which is the most appropriate answer?",
   opts=[
     ["It will grow with him, darken and thicken, and will not involute",
      "Correct — the vasculature dilates over time and the lesion may become a raised plaque. Psychosocial disability from facial disfigurement can be overwhelming."],
     ["It will proliferate for a few months and then slowly involute",
      "That is the infantile hemangioma."],
     ["It will fade within his first year of life",
      "That is nevus simplex."],
     ["It will stay exactly the same size and colour for life",
      "It grows with the child and darkens and thickens over time."]],
   c=0, cite=c(78)),

 dict(topic="Nevus flammeus", io=IOB, lead="treatment",
   q="A 2-year-old boy has a flat, blanchable, pink-purple patch on one cheek that has been present since birth and stops sharply at the midline. His parents ask what can be done about it. Which is the most appropriate answer?",
   opts=[
     ["No treatment is required; tinted waterproof makeup, or pulsed dye laser",
      "Correct — the laser selectively destroys the superficial target vessels."],
     ["Oral propranolol as first line, with corticosteroids as an alternative",
      "Those are infantile hemangioma treatments."],
     ["Surgical excision in infancy before it thickens",
      "Excision in infancy is not what is described."],
     ["Observation only, because it fades during the first year",
      "Nevus flammeus does not fade."]],
   c=0, cite=c(81)),

 dict(topic="Nevus simplex", io=IOB, lead="test",
   q="A newborn has a pink irregular patch on the nape of the neck that blanches with pressure and becomes much more obvious when he cries. Which is the most likely diagnosis?",
   opts=[
     ["Nevus simplex",
      "Correct — the stork bite, a more superficial variant of nevus flammeus."],
     ["Nevus flammeus",
      "That is usually unilateral with sharp midline cutoffs and does not fade."],
     ["Infantile hemangioma",
      "That is raised and bright red once it proliferates."],
     ["Telangiectasia",
      "That is a permanently dilated capillary under one millimetre, acquired."]],
   c=0, cite=c(84)),

 dict(topic="Cherry angioma", io=IOA, lead="diagnosis",
   q="A 61-year-old man has several smooth, firm, deep red papules under 5 mm on his trunk. They blanch with pressure and have accumulated over the last decade. Which is the most likely diagnosis?",
   opts=[
     ["Cherry angiomas",
      "Correct — acquired, increasing with age, once called senile angiomas."],
     ["Spider angiomas",
      "Those are under ten millimetres with a central arteriole, on face, neck and upper trunk."],
     ["Pyogenic granulomas",
      "Those are moist exophytic lesions that grow fast and bleed."],
     ["Petechiae",
      "Those do not blanch, and are not papular."]],
   c=0, cite=c(86)),

 dict(topic="Cherry angioma", io=IOA, lead="education",
   q="A 61-year-old man has several smooth, firm, deep red papules under 5 mm on his trunk that blanch with pressure and have accumulated over recent years. He asks whether removing them will stop new ones appearing. Which is the most appropriate response?",
   opts=[
     ["New lesions will likely develop and there is no way to prevent them",
      "Correct — treatment is not necessary unless they bother him."],
     ["Removing them prevents further lesions from forming",
      "There is no way to prevent new ones."],
     ["They will fade on their own within a year",
      "Fading within a year belongs to nevus simplex."],
     ["Each one should be biopsied because they are premalignant",
      "Cherry angiomas are benign."]],
   c=0, cite=c(87)),

 dict(topic="Nevus araneus", io=IOA, lead="test",
   q="A 44-year-old man has several small vascular lesions with a central punctum and radiating vessels across his upper chest and arms. Which history is most important to take?",
   opts=[
     ["Alcohol use, liver-damaging medications, and hormone use",
      "Correct — the deck also says to ask about pregnancies. Spider angiomas are associated with estrogen excess and with cirrhosis and liver failure."],
     ["Footwear, occupation and use of hand tools",
      "That is the corn and callus history."],
     ["Immobility, incontinence and nutritional status",
      "Those are pressure injury questions."],
     ["Birth history, feeding and family history of birthmarks",
      "That is the infantile hemangioma history."]],
   c=0, cite=c(90)),

 dict(topic="Nevus araneus", io=IOA, lead="education",
   q="A 28-year-old woman develops several spider angiomas during pregnancy and asks whether she will need treatment. Which is the most appropriate response?",
   opts=[
     ["They usually resolve after delivery",
      "Correct — those caused by oral contraceptives resolve after stopping the pill. No treatment may be needed, and pulsed dye laser resolves most lesions that persist."],
     ["They will persist for life and require laser in every case",
      "Pregnancy-related lesions resolve after delivery."],
     ["They indicate liver failure and require urgent investigation",
      "Cirrhosis is one cause, but pregnancy is the relevant one here."],
     ["They will fade if she avoids sun exposure",
      "Sun avoidance is not what resolves them."]],
   c=0, cite=c(89)),

 dict(topic="Pyogenic granuloma", io=IOA, lead="diagnosis",
   q="A 16-year-old is being evaluated for a lesion on the finger pad of the fourth digit of her left hand. She says it came up rapidly after she injured her finger and bleeds easily if she bumps it. Examination shows a moist, vascular, dome-shaped lesion. Which is the most likely diagnosis?",
   opts=[
     ["Pyogenic granuloma",
      "Correct — rapid growth after trauma, moist surface, and easy bleeding."],
     ["Cherry angioma",
      "That is a small firm deep red papule on the trunk that does not grow rapidly."],
     ["Telangiectasia",
      "That is a permanently dilated capillary under one millimetre."],
     ["Syringoma",
      "That is a crop of small papules around the eyes."]],
   c=0, cite=c(92)),

 dict(topic="Pyogenic granuloma", io=IOA, lead="treatment",
   q="A 16-year-old has a moist, bright red papule with an epithelial collarette on the finger pad of her left fourth digit that bleeds readily. She wants it removed and asks which option is least likely to come back. Which is the most appropriate answer?",
   opts=[
     ["Surgical excision, though it scars the most",
      "Correct — it has the lowest recurrence rate and also provides histopathologic analysis, at the cost of the highest rate of scarring."],
     ["Cryotherapy, which has the lowest recurrence and no scarring",
      "Cryotherapy is one of the alternatives rather than the lowest-recurrence option."],
     ["Laser, which has the lowest recurrence and the best cosmetic result",
      "Laser is listed among the other modalities."],
     ["Observation, since spontaneous resolution is guaranteed within weeks",
      "Resolution may occur but takes months to years and is not guaranteed."]],
   c=0, cite=c(95)),

 dict(topic="Pyogenic granuloma", io=IOA, lead="education",
   q="A patient with a pyogenic granuloma opts against treatment. Which is the most appropriate advice?",
   opts=[
     ["It is benign and often resolves over months to years",
      "Correct — effective treatments exist if she changes her mind. If it recurs, early follow-up is appropriate, because small lesions are easier to treat than large ones."],
     ["It is premalignant and must be excised within a month",
      "The lesion is benign."],
     ["It is infectious and household contacts should be checked",
      "It is neither infectious nor granulomatous."],
     ["It will resolve within two weeks without any follow-up",
      "Resolution takes months to years."]],
   c=0, cite=c(96)),

 dict(topic="Neurofibromatosis", io=IOB, lead="diagnosis",
   q="A 9-year-old has eight light brown macules over 5 mm across on his trunk, freckling in both axillae, and several soft papules protruding just above the skin. Which is the most likely diagnosis?",
   opts=[
     ["Neurofibromatosis type 1",
      "Correct — café au lait spots, intertriginous freckling and cutaneous neurofibromas."],
     ["Neurofibromatosis type 2",
      "The skin manifestations listed in the deck belong to type 1."],
     ["Multiple acrochordons",
      "Skin tags occur in friction sites and are not accompanied by café au lait spots."],
     ["Multiple dermatofibromas",
      "Those are firm brown nodules with a dimple sign, usually on the legs."]],
   c=0, cite=c(98)),

 dict(topic="Neurofibromatosis", io=IOB, lead="test",
   q="You are counting café au lait macules on that same 9-year-old. How many are described as diagnostic, and what caveat applies?",
   opts=[
     ["Six or more; but the macules alone do not establish the diagnosis",
      "Correct — over five millimetres prepubertal, over fifteen postpubertal."],
     ["Two or more; and the macules alone establish the diagnosis",
      "Neither the count nor the caveat matches."],
     ["Six or more; and the macules alone establish the diagnosis",
      "The count is right, but the caveat is the opposite of what is stated."],
     ["Three or more; but only if they appear after puberty",
      "The number is six, and timing is not the criterion."]],
   c=0, cite=c(99)),

 dict(topic="Neurofibromatosis", io=IOB, lead="treatment",
   q="A patient with neurofibromatosis type 1 attends for routine review. Which is the most appropriate approach?",
   opts=[
     ["A cutaneous examination at every visit",
      "Correct — assess for new neurofibromas or progression of existing ones. Plexiform lesions may be locally invasive, so their extent needs determining."],
     ["Excision of every cutaneous neurofibroma as it appears",
      "Excision of all lesions is not what is described."],
     ["Annual magnetic resonance imaging of the whole body",
      "Routine whole-body imaging is not part of the described surveillance."],
     ["Intralesional corticosteroid to any enlarging lesion",
      "That is a scar treatment in this lecture."]],
   c=0, cite=c(103)),

 dict(topic="Xanthelasma", io=IOA, lead="test",
   q="A 55-year-old woman has soft, yellow plaques on both medial upper eyelids. They are asymptomatic. Which is the most likely diagnosis?",
   opts=[
     ["Xanthelasma",
      "Correct — collections of lipid-laden macrophages, most commonly on the medial eyelids."],
     ["Syringoma",
      "Those are skin-coloured, pink or brown papules of one to two millimetres."],
     ["Milia",
      "Those are small white keratin cysts rather than yellow plaques."],
     ["Sebaceous hyperplasia",
      "Those are whitish-yellow papules with a central umbilication, on the face."]],
   c=0, cite=c(104)),

 dict(topic="Xanthelasma", io=IOA, lead="next step",
   q="A 55-year-old woman has soft, yellow plaques on both medial upper eyelids. Beyond addressing the plaques themselves, what should be done for her?",
   opts=[
     ["Screen for hyperlipidemia",
      "Correct — xanthelasma is associated with lipid disorders, and may signify an increased risk of cardiac disease."],
     ["Screen for diabetes mellitus and check a haemoglobin A1c",
      "The named association is with lipid disorders."],
     ["Check thyroid function tests",
      "No thyroid association is described."],
     ["Check liver function tests and a coagulation screen",
      "Liver disease is the association drawn for spider angioma."]],
   c=0, cite=c(104)),

 dict(topic="Lipoma", io=IOA, lead="test",
   q="A 48-year-old man has a soft, painless, rubbery subcutaneous nodule about 4 cm across on his back. It is mobile and there is no overlying pore. Which is the most likely diagnosis?",
   opts=[
     ["Lipoma",
      "Correct — the most common soft tissue tumour, soft and rubbery, usually under five centimetres."],
     ["Epidermoid cyst",
      "That has a central punctum and expresses pasty material."],
     ["Dermatofibroma",
      "That is firm, brown-haloed, and dimples on lateral compression."],
     ["Abscess",
      "That would be warm, tender and fluctuant."]],
   c=0, cite=c(105)),

 dict(topic="Lipoma", io=IOA, lead="treatment",
   q="A 48-year-old man has a soft, painless, rubbery subcutaneous nodule about 4 cm across on his back. It is mobile with no overlying pore, and he is not troubled by it. Which is the most appropriate management?",
   opts=[
     ["Observation",
      "Correct — excision is for a cosmetically deforming mass or diagnostic uncertainty."],
     ["Surgical excision now, because of the risk of liposarcoma",
      "No such transformation risk is described."],
     ["Aspiration of the contents",
      "A lipoma is solid fat, not a fluid-filled lesion."],
     ["Intralesional corticosteroid injection",
      "That is a scar treatment."]],
   c=0, cite=c(106)),

 dict(topic="Digital mucous cyst", io=IOA, lead="diagnosis",
   q="A 66-year-old woman with osteoarthritis has a translucent skin-coloured papule over the distal interphalangeal joint of her index finger. The nail beyond it has a longitudinal groove. Which is the most likely diagnosis?",
   opts=[
     ["Digital mucous cyst",
      "Correct — pressure on the nail matrix causes the groove."],
     ["Epidermoid cyst",
      "That has a central punctum and is not associated with a joint."],
     ["Chronic paronychia",
      "That involves the nail fold with a retracted cuticle."],
     ["Acrochordon",
      "That is a stalked papule in a friction site."]],
   c=0, cite=c(108)),

 dict(topic="Digital mucous cyst", io=IOA, lead="treatment",
   q="A 66-year-old woman with osteoarthritis has a translucent skin-coloured papule over a distal interphalangeal joint, with a groove in the adjacent nail that she finds troublesome. Which is the most appropriate management?",
   opts=[
     ["Excision, since nail dystrophy is an indication",
      "Correct — asymptomatic lesions can simply be observed."],
     ["Observation, since the cyst is asymptomatic",
      "It is not asymptomatic; it is causing nail dystrophy."],
     ["Repeated aspiration at each visit",
      "Repeated aspiration is not the management described."],
     ["Intralesional corticosteroid followed by silicone sheeting",
      "Those are scar treatments."]],
   c=0, cite=c(108)),

 dict(topic="Sebaceous hyperplasia", io=IOB, lead="diagnosis",
   q="A 70-year-old man on immunosuppression after a renal transplant has several soft, whitish-yellow papules on his forehead. Each is 3 to 4 mm with a central dell, and a tiny globule of sebum can be expressed. Which is the most likely diagnosis?",
   opts=[
     ["Sebaceous hyperplasia",
      "Correct — immunosuppression is named as high risk, and the central umbilication is characteristic."],
     ["Basal cell carcinoma",
      "That is the differential, and dermoscopy is what separates them."],
     ["Syringoma",
      "Those are one to two millimetres, around the eyes, and appear at puberty."],
     ["Xanthelasma",
      "Those are yellow plaques on the medial eyelids."]],
   c=0, cite=c(110)),

 dict(topic="Sebaceous hyperplasia", io=IOB, lead="next step",
   q="You are not certain whether one of those lesions is a basal cell carcinoma. Which is the most appropriate next step?",
   opts=[
     ["Dermoscopy, which can distinguish the two, with biopsy if concern remains",
      "Correct — patients often present worried about exactly this."],
     ["Excise all the lesions with clear margins",
      "Excision of everything is not what is described."],
     ["Reassure, since sebaceous hyperplasia never resembles a carcinoma",
      "Basal cell carcinoma is precisely the named differential."],
     ["Start light electrocautery to all lesions and review",
      "Treating before deciding what it is inverts the order."]],
   c=0, cite=c(111)),

 dict(topic="Benign lesions overall", io=IOB, lead="education",
   q="A 62-year-old attends about a new lesion on his sun-exposed forearm. Beyond addressing the lesion, which counselling does the lecture say to offer?",
   opts=[
     ["Sunscreen, sun avoidance at peak hours, and skin checks",
      "Correct — the general education point the deck attaches to any new lesion in a sun-exposed area."],
     ["Avoiding cosmetic procedures such as ear piercing",
      "That is for the keloid-prone patient."],
     ["Repositioning every two hours and barrier creams",
      "Those are pressure injury measures."],
     ["Well-fitting footwear and padding inside the shoe",
      "That is corn and callus education."]],
   c=0, cite=c(112)),

 dict(topic="Benign lesions overall", io=IOB, lead="education",
   q="A patient elects to have a benign lesion removed purely for appearance. What must she be told first?",
   opts=[
     ["The risk of pigmentary changes and the chance of recurrence",
      "Correct — both must be fully explained beforehand."],
     ["That histology is required on every excised specimen",
      "Histology is not mandated for every cosmetic removal."],
     ["That the lesion would become malignant if left in place",
      "These are benign lesions, so that would be untrue."],
     ["That lifelong surveillance of the site will be needed",
      "Lifelong surveillance is not what the slide requires."]],
   c=0, cite=c(112)),
]
