# -*- coding: utf-8 -*-
"""Benign Skin Lesions (Griffenkranz) -- pool for the Updated CMS derm master exams."""
DECK = "7. Benign Skin Lesions Prof Griffenkranz 8-25-2025-2.pptx"
IO_A = ("a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing, management, appropriate referrals, patient education, "
        "and prognosis for benign skin lesions")
IO_B = ("b — Identify medical strategies for common benign skin lesions in infants, adolescents, adults and "
        "the elderly")

def Q(topic, q, opts, c, slide, io=IO_A):
    return {"topic": topic, "io": io, "q": q, "opts": opts, "c": c, "cite": f"{DECK}, Slide {slide}"}

QUESTIONS = [

Q("Callus",
  "A 44-year-old runner has a painful lesion on the plantar surface of the forefoot. Pressing straight down on it "
  "reproduces the pain, whereas squeezing it from the sides does not. The skin lines run through the lesion, and "
  "paring it reveals a central cone of hard keratin. What is the diagnosis?",
  [["Clavus, a corn with a central hyperkeratotic core",
    "Correct. A clavus results from pressure on a localised area, creating a cone-shaped central core of hard "
    "keratin. Pain occurs on direct downward pressure, and the skin lines run through the lesion."],
   ["Callus",
    "A callus follows a broad area of pressure, producing diffuse thickening that is larger than a corn, irregular in "
    "shape, and lacks a central core. It is usually painless, whereas this lesion has both a core and downward "
    "tenderness."],
   ["Verruca vulgaris",
    "A wart interrupts the skin lines rather than allowing them to run through, may hurt with side pressure rather "
    "than downward pressure, and shows a blackened centre from thrombosed capillaries. All three features point away "
    "from it here."],
   ["Plantar fibroma",
    "A plantar fibroma is a firm nodule within the plantar fascia rather than a hyperkeratotic surface lesion, and it "
    "does not produce a keratin core on paring."],
   ["Epidermoid cyst",
    "An epidermoid cyst is a moveable round protruding mass with a central punctum that may drain foul-smelling "
    "keratin. It is not a hyperkeratotic pressure lesion of a weight-bearing surface."]],
  0, 7),

Q("Callus",
  "How do the skin lines behave in a callus compared with a verruca vulgaris, and why does this matter?",
  [["Skin lines run through a callus but are interrupted by a wart, which distinguishes the two on inspection",
    "Correct. Skin lines run through both corns and calluses, whereas verruca vulgaris interrupts the skin lines. "
    "This is a bedside sign that requires no equipment."],
   ["Skin lines are interrupted by a callus but run through a wart",
    "The two are reversed. A clinician applying this rule would treat a wart as a pressure lesion and a callus as "
    "viral, and would pursue the wrong management for both."],
   ["Skin lines are interrupted by both, so the sign is not useful",
    "The sign is useful precisely because the two behave differently. Discarding it removes a simple discriminator."],
   ["Skin lines run through both, so the sign is not useful",
    "Skin lines run through corns and calluses only. A wart interrupts them, which is what makes the comparison "
    "informative."],
   ["Skin lines cannot be assessed on plantar skin",
    "Plantar skin has particularly prominent dermatoglyphics, which is exactly why the sign is most useful there."]],
  0, 8),

Q("Wound healing",
  "What are the four phases of wound healing, and what accounts for the improving tensile strength of a maturing "
  "scar?",
  [["Hemostasis, inflammation, proliferation, and remodeling, with tensile strength improving through progressive "
    "cross-linking of collagen fibres",
    "Correct. The four phases are hemostasis, inflammation, proliferation, and remodeling. As the scar matures its "
    "tensile strength improves because of progressive cross-linking of collagen fibres."],
   ["Inflammation, proliferation, remodeling, and contracture, with strength from new elastin deposition",
    "Hemostasis is the first phase and contracture is not one of the four, and it is collagen cross-linking rather "
    "than elastin that confers strength."],
   ["Hemostasis, proliferation, contraction, and epithelialisation, with strength from fibroblast proliferation",
    "Fibroblast activity occurs during proliferation, but the four named phases are hemostasis, inflammation, "
    "proliferation, and remodeling."],
   ["Inflammation, granulation, maturation, and involution, with strength from vascular ingrowth",
    "Involution describes the natural history of an infantile hemangioma rather than a phase of wound healing, and "
    "vascular ingrowth does not confer tensile strength."],
   ["Hemostasis, inflammation, proliferation, and remodeling, with tensile strength fixed at the time of closure",
    "The phases are right, which makes this the closest wrong answer, but tensile strength continues to improve as "
    "cross-linking progresses rather than being fixed at closure."]],
  0, 11),

Q("Keloid",
  "A 22-year-old woman has a firm, bulbous nodule at the site of an ear piercing performed two years ago. The lesion "
  "extends well beyond the original piercing site and has continued to enlarge. What distinguishes this from a "
  "hypertrophic scar?",
  [["It extends beyond the original wound margins and shows no regression with time",
    "Correct. A keloid extends beyond the wound site margins, develops slowly, continues to enlarge for months to "
    "years, and shows no regression with a tendency to recur. A hypertrophic scar develops rapidly within four weeks, "
    "remains within the wound margins, and flattens with time."],
   ["It developed rapidly within four weeks of the injury",
    "Rapid development within four weeks characterises a hypertrophic scar. The keloid develops slowly and keeps "
    "enlarging over months to years."],
   ["It remains confined within the original wound margins",
    "Staying within the wound margins is the hypertrophic scar pattern. Extension beyond them is the defining keloid "
    "feature."],
   ["It regresses and flattens with time",
    "Hypertrophic scars remain stable and regress with time. Keloids show no regression."],
   ["It is always painless",
    "Keloids are often asymptomatic but may be pruritic or produce burning pain, and hypertrophic scars are also "
    "typically asymptomatic. Symptoms do not separate them."]],
  0, 13),

Q("Keloid",
  "A patient with a history of keloids asks about surgical removal of a keloid on her shoulder. What should she be "
  "told?",
  [["Surgical removal alone carries a 50 to 100 percent recurrence rate, often producing a lesion larger than the "
    "original, so it should be followed with intralesional steroid",
    "Correct. Surgical removal has a 50 to 100 percent recurrence rate and the recurrence is often larger than the "
    "original lesion, which is why excision is followed with intralesional steroid."],
   ["Surgical removal alone is curative in most patients",
    "This reverses the recurrence data entirely and would set up a patient with a known keloid tendency for a larger "
    "lesion than she started with."],
   ["Surgical removal should be performed only after a biopsy has confirmed the diagnosis",
    "Diagnosis is clinical, and biopsy is done only if there is clinical doubt because it may itself induce new "
    "scarring."],
   ["Silicone gel sheeting should be applied for one week before excision",
    "Silicone gel sheets are worn for 12 to 24 hours a day for up to a year as a treatment in their own right, not as "
    "a brief pre-operative measure."],
   ["Cryotherapy should replace surgery because it carries no adverse effects",
    "Cryotherapy with liquid nitrogen flattens lesions but can cause hypopigmentation, so it is not free of adverse "
    "effects."]],
  0, 18),

Q("Keloid",
  "What is described as the most important element in the management of keloids?",
  [["Prevention, including advising high-risk patients to avoid cosmetic procedures such as ear piercing",
    "Correct. Prevention is described as the most important treatment. High-risk patients should be advised to avoid "
    "cosmetic procedures such as ear piercing, and post-surgical education includes avoiding stretching of an "
    "immature scar and avoiding hot baths."],
   ["Early surgical excision of every lesion as soon as it appears",
    "Excision carries a 50 to 100 percent recurrence rate with lesions often larger than the original, so early "
    "surgery is not the cornerstone."],
   ["Intralesional steroid injection as the sole modality",
    "Intralesional steroids eventually flatten lesions and reduce collagen production, and they may cause tissue "
    "atrophy. They are one modality among several rather than the most important element."],
   ["Compression therapy applied for one week after any injury",
    "Compression therapy is used with pressure maintained over an extended period rather than for a single week, and "
    "it is a treatment rather than the overarching principle."],
   ["Routine biopsy of every lesion to exclude malignancy",
    "Biopsy is performed only if there is clinical doubt, because it may itself induce new scarring."]],
  0, 15),

Q("Cutaneous horn",
  "A 68-year-old man has a hard, conical keratotic projection on the dorsum of his hand. What is the key principle in "
  "evaluating this lesion?",
  [["There is often no clinical feature distinguishing benign from malignant, so the underlying lesion at the base "
    "must be diagnosed",
    "Correct. A cutaneous horn arises from the surface of another lesion, which may be benign or malignant — actinic "
    "keratosis, warts, and squamous cell carcinoma among them. There is often no clinical feature to distinguish "
    "them, so the underlying lesion must be diagnosed."],
   ["The horn itself should be sent for histology and the base left undisturbed",
    "The horn is composed of keratin. It is the lesion at its base that carries the diagnosis, so sampling only the "
    "projection risks missing an underlying malignancy."],
   ["A conical shape reliably indicates a benign process",
    "Shape does not indicate behaviour. That is precisely why the underlying lesion must be identified rather than "
    "inferred."],
   ["The lesion can be reassured about if it is painless",
    "History may include bleeding or pain but symptoms do not separate benign from malignant underlying lesions."],
   ["Cryotherapy should be applied without histological assessment",
    "Destroying the lesion without knowing what lies beneath forfeits the opportunity to diagnose an underlying "
    "malignancy, which frequently requires excision according to standard practice for the tumour type."]],
  0, 27),

Q("Acrochordon",
  "A 52-year-old woman with obesity has multiple soft, skin-coloured pedunculated papules on the neck and in the "
  "axillae, ranging from 2 to 6 mm. She asks what they are. What education is appropriate?",
  [["They are harmless growths of normal skin that form where skin rubs together, and they are very common with age",
    "Correct. Skin tags are fibroepithelial pedunculated papillomas that are harmless growths of normal skin, forming "
    "where skin rubs together such as the armpit, neck, under the breasts, and groin. They are very common, present "
    "in a large majority by age 70, and more frequent in women and in obesity."],
   ["They are premalignant lesions that require excision",
    "Acrochordons are benign. Describing them as premalignant would prompt unnecessary procedures and considerable "
    "avoidable anxiety."],
   ["They are viral warts spread by skin contact",
    "Verruca vulgaris is caused by human papillomavirus and interrupts the skin lines with a rough greyish surface. "
    "Skin tags are soft pedunculated growths of normal skin."],
   ["They indicate an underlying internal malignancy",
    "It is malignant acanthosis nigricans that carries a paraneoplastic association. Skin tags are a friction-related "
    "benign finding."],
   ["They will resolve spontaneously without any intervention",
    "Skin tags do not regress. They may be removed for cosmetic reasons or if irritated, but they persist otherwise."]],
  0, 31, IO_B),

Q("Pressure injury",
  "A nursing home resident with limited mobility is at risk of pressure injury. What is the single best measure?",
  [["Prevention, through frequent skin and nutrition assessment, moisture control, and repositioning every two hours",
    "Correct. The best measure is prevention: frequent skin assessments, nutrition assessment, moisture control and "
    "skin care with the skin kept clean and dry, incontinence managed and barrier creams applied, and repositioning "
    "every two hours."],
   ["Applying a hydrocolloid dressing prophylactically to all bony prominences",
    "Silicone and hydrocolloid dressings appear in the management of an established injury. They do not substitute "
    "for relieving the pressure that causes the damage."],
   ["Repositioning every eight hours with the nursing shift changes",
    "Repositioning every two hours is specified. Tying it to eight-hour shifts leaves long periods of unrelieved "
    "pressure, which is the mechanism of injury."],
   ["Referring every at-risk patient for surgical debridement",
    "Surgical referral for debridement applies to an established wound with devitalised tissue rather than to a "
    "patient at risk who has no injury yet."],
   ["Restricting fluids to reduce incontinence and moisture",
    "Incontinence is managed with skin care and barrier creams, and nutrition assessment is part of prevention. "
    "Restricting fluids risks dehydration and malnutrition, both of which worsen tissue tolerance."]],
  0, 35, IO_B),

Q("Pilonidal cyst",
  "A 21-year-old man presents with sudden pain and swelling over the sacrum in the gluteal cleft. Examination shows a "
  "warm, tender, erythematous fluctuant mass with purulent drainage. What is the appropriate management of this "
  "acute presentation?",
  [["Incision and drainage",
    "Correct. An acute pilonidal abscess requires incision and drainage. The condition arises when a dimple over the "
    "coccyx draws in hair and debris leading to follicular plugging, and ingrown hairs prevent drainage and promote "
    "abscess formation."],
   ["Oral antibiotics alone",
    "An antibiotic will not evacuate a fluctuant collection, and fluctuance is specifically the palpation finding "
    "indicating fluid. Drainage is required."],
   ["Warm compresses and observation",
    "Observation of a fluctuant, draining abscess allows it to enlarge and extend rather than resolve."],
   ["Immediate wide surgical excision of the natal cleft",
    "Definitive excision addresses chronic disease with sinus tracts. It is not the management of an acute abscess "
    "presentation."],
   ["Magnetic resonance imaging before any intervention",
    "No diagnostic testing is usually needed. Imaging would delay the drainage that relieves the abscess."]],
  0, 43),

Q("Pilonidal cyst",
  "Which set of risk factors is associated with pilonidal disease?",
  [["Obesity, local trauma or irritation, sedentary lifestyle, increased hair density in the natal cleft, and family "
    "history, with a male to female ratio of about 3 to 1",
    "Correct. Those are the listed risk factors, and the male to female ratio is 3 to 1."],
   ["Female sex, pregnancy, and oestrogen excess",
    "Oestrogen excess states are associated with nevus araneus, the spider angioma, which resolves after delivery or "
    "cessation of hormonal contraception."],
   ["Prematurity, low birth weight, and multiple gestation",
    "Those are the birth history factors associated with infantile hemangiomas."],
   ["Fair skin, sun exposure, and age over 40",
    "Fair skin, sun exposure, and age over 40 are risk factors for keratoacanthoma."],
   ["Chronic venous insufficiency and impaired lymphatic drainage",
    "Those relate to stasis dermatitis and erysipelas rather than to a follicular disease of the natal cleft."]],
  0, 39),

Q("Dermatofibroma",
  "A 35-year-old woman has a firm 8 mm nodule on her lower leg with a brown halo and a slightly raised centre. When "
  "the skin on either side is squeezed together, the lesion dimples downward. What is this sign, and what does "
  "dermoscopy typically show?",
  [["The dimple sign, with dermoscopy showing a peripheral pigment network and a central white area",
    "Correct. The dimple sign is characteristic of dermatofibroma, which is a firm 0.5 to 1 cm nodule formed by dense "
    "clusters of dermal fibroblasts, most commonly on the legs. Dermoscopy often shows a peripheral pigment network "
    "with a central white area."],
   ["The dimple sign, seen in lipoma",
    "The sign is correctly named but attached to the wrong lesion. A lipoma is a soft, benign overgrowth of "
    "subcutaneous fat and is on the differential for other nodules rather than being the dimple-sign lesion."],
   ["Nikolsky sign, indicating epidermal separation",
    "Nikolsky sign is the slipping away of the top layers of skin when rubbed, positive in pemphigus. It has nothing "
    "to do with a firm dermal nodule."],
   ["Darier sign, indicating mastocytosis",
    "Darier sign is urtication of a lesion after stroking and points to mastocytosis rather than to a fibrous dermal "
    "nodule."],
   ["Auspitz sign, indicating psoriasis",
    "Auspitz sign is pinpoint bleeding after scale removal from a psoriatic plaque."]],
  0, 46),

Q("Dermatofibroma",
  "What is notable about the symptom profile of a dermatofibroma?",
  [["It is usually asymptomatic but is the most common painful skin tumour when it does cause symptoms",
    "Correct. Dermatofibroma is usually asymptomatic, sometimes with a history of insect bite, and when symptomatic "
    "may cause slight pruritus or pain — it is described as the most common painful skin tumour."],
   ["It is invariably painful and never asymptomatic",
    "Most are asymptomatic. Requiring pain for the diagnosis would exclude the majority of lesions."],
   ["It is always pruritic and never painful",
    "Slight pruritus can occur, but pain is the symptom for which this lesion is specifically noted."],
   ["It becomes painful only after malignant transformation",
    "Dermatofibroma is benign. Pain is a feature of the benign lesion rather than a marker of transformation."],
   ["Symptoms occur only in lesions larger than 3 cm",
    "The lesion is characteristically 0.5 to 1 cm, so a size threshold of that kind would apply to almost none of "
    "them."]],
  0, 45),

Q("Keratoacanthoma",
  "A 62-year-old fair-skinned man who always burns and never tans has a solitary, smooth, shiny, dome-shaped red "
  "papule with a central keratin plug on his forearm that appeared and grew rapidly over seven weeks. What is the "
  "only reliable way to make the diagnosis, and why does it matter?",
  [["Biopsy, because the lesion cannot reliably be distinguished from squamous cell carcinoma clinically",
    "Correct. Biopsy is the only reliable method to make the diagnosis. Squamous cell carcinoma heads the "
    "differential, and the standard of care is to excise or destroy the tumour precisely because of possible "
    "malignancy."],
   ["Observation for 3 to 6 months, since spontaneous regression confirms the diagnosis",
    "Keratoacanthoma does demonstrate a triphasic pattern of rapid growth within 6 to 8 weeks, stabilisation, and "
    "regression after 3 to 6 months, which is why this is tempting. But waiting for regression risks observing a "
    "squamous cell carcinoma instead."],
   ["Dermoscopy, which distinguishes it from squamous cell carcinoma",
    "Dermoscopy is useful for distinguishing basal cell carcinoma from sebaceous hyperplasia and for dermatofibroma, "
    "but biopsy is the reliable method here."],
   ["A potassium hydroxide preparation from the keratin plug",
    "A potassium hydroxide preparation detects fungal elements and has no role in evaluating a keratinocytic tumour."],
   ["Clinical appearance alone, given the characteristic triphasic history",
    "The history is characteristic but not sufficient, because the appearance overlaps with squamous cell carcinoma, "
    "basal cell carcinoma, and amelanotic melanoma."]],
  0, 51),

Q("Keratoacanthoma",
  "What is the standard of care for a keratoacanthoma, and what margin is used for elliptical excision?",
  [["Excision or destruction of the tumour, with elliptical excision using 5 mm margins",
    "Correct. The standard of care is to excise or destroy the tumour, preferred because of possible malignancy, with "
    "elliptical excision using 5 mm margins. Mohs surgery may be indicated for large or recurrent lesions or those in "
    "cosmetically sensitive locations."],
   ["Observation alone, since the lesion regresses spontaneously",
    "Regression does occur after 3 to 6 months, but the lesion may continue growing or rarely metastasise, and it "
    "cannot be distinguished from squamous cell carcinoma without histology."],
   ["Excision with 1 mm margins",
    "A 1 mm margin is inadequate for a lesion excised specifically because of possible malignancy."],
   ["Cryotherapy without histological assessment",
    "Destroying the lesion without histology forfeits the diagnosis, which matters given the squamous cell carcinoma "
    "differential."],
   ["Intralesional corticosteroid injection",
    "Intralesional steroids are used for keloids and hypertrophic scars, and for inflamed epidermoid cysts. They are "
    "not the treatment for a possible keratinocytic malignancy."]],
  0, 52),

Q("Epidermoid cyst",
  "A 39-year-old man has a moveable, round, firm nodule on the back with a visible central pore, which occasionally "
  "discharges foul-smelling material. It is currently red, warm, and tender. What is the appropriate management?",
  [["Postpone excision for a few weeks, reduce inflammation with intralesional triamcinolone, and give antibiotics if "
    "needed",
    "Correct. If the cyst is inflamed, excision should be postponed for a few weeks, inflammation reduced with an "
    "intralesional steroid injection of triamcinolone, and antibiotics given if needed. Surgical removal of the "
    "entire capsule is performed when the cyst is not inflamed."],
   ["Excise the entire capsule immediately while it is inflamed",
    "Removal of the entire capsule is the standard of care but is performed when the cyst is not inflamed. Operating "
    "on inflamed tissue makes complete capsule removal harder and recurrence more likely."],
   ["Leave it alone permanently, since epidermoid cysts never require treatment",
    "No treatment is necessary if the cyst is asymptomatic, but this one is inflamed and symptomatic."],
   ["Aspirate the contents with a needle and discharge without follow-up",
    "Removing contents without the capsule leaves the structure that regenerates the cyst, so it recurs."],
   ["Refer urgently for excision with wide margins for possible malignancy",
    "The differential includes cystic acne, lipoma, neurofibroma, keratoacanthoma, and basal cell carcinoma, but a "
    "moveable cyst with a central punctum discharging keratin is a characteristic benign lesion."]],
  0, 56),

Q("Epidermoid cyst",
  "Why is the term sebaceous cyst a misnomer for an epidermoid cyst?",
  [["The cyst is a cystic enclosure of epithelium within the dermis filled with keratin rather than sebum",
    "Correct. An epidermoid cyst is formed by cystic enclosure of epithelium within the dermis and becomes filled "
    "with keratin. It is often called a sebaceous cyst because it appears to contain sebum."],
   ["The cyst arises from apocrine rather than sebaceous glands",
    "The cyst arises from enclosed epithelium rather than from any gland, and its content is keratin. Apocrine "
    "involvement describes hidradenitis suppurativa."],
   ["The cyst has no lining, being a pseudo-cyst",
    "A pseudo-cyst without a cellular lining describes the digital mucous cyst, which represents extrusion of "
    "mucinous contents from a joint space."],
   ["The cyst contains lipid-laden macrophages rather than sebum",
    "Collections of lipid-laden macrophages form xanthelasma, the soft yellow cholesterol plaques of the medial "
    "eyelids."],
   ["The cyst is filled with mucin from the underlying joint",
    "Mucin from a joint space characterises the digital mucous cyst over the distal interphalangeal joint."]],
  0, 53),

Q("Syringoma",
  "A 16-year-old girl has multiple 1 to 2 mm firm skin-coloured papules symmetrically distributed on the lower "
  "eyelids that appeared around puberty. What is the origin of these lesions?",
  [["Benign neoplasms of eccrine ducts",
    "Correct. Syringomas are benign neoplasms of eccrine sweat ducts. They appear at puberty and are more common in "
    "females, presenting as multiple 1 to 2 mm papules and usually asymptomatic."],
   ["Benign neoplasms of apocrine glands",
    "Apocrine gland inflammation characterises hidradenitis suppurativa. Syringomas arise from the eccrine duct."],
   ["Collections of lipid-laden macrophages",
    "Lipid-laden macrophages form xanthelasma, which appears as soft yellow cholesterol plaques and is on the "
    "syringoma differential — but xanthelasma is yellow and plaque-like rather than small firm papules."],
   ["Proliferation of dermal capillaries",
    "Capillary proliferation produces cherry angiomas, which are red and blanch with pressure."],
   ["Hyperplasia of sebaceous glands around a central pore",
    "Sebaceous hyperplasia produces whitish-yellow or skin-coloured papules with a central dell, typically in older "
    "adults rather than at puberty."]],
  0, 58),

Q("Infantile hemangioma",
  "A 3-week-old infant, born prematurely, has a bright red papule on the scalp that was a faint blanched area with "
  "fine telangiectasias at birth and has grown noticeably in the past fortnight. What growth pattern should the "
  "parents be told to expect?",
  [["A rapid proliferative phase with most growth in the first 4 to 6 months, followed by a slower involution phase",
    "Correct. Infantile hemangiomas have a unique growth pattern of rapid proliferation followed by slower "
    "involution, with rapid growth during the neonatal period and most growth in the first 4 to 6 months. The "
    "earliest sign is blanching of the involved skin followed by fine telangiectasias and then a red macule."],
   ["Steady growth in proportion to the child with no involution",
    "Growth in proportion to the child without involution describes nevus flammeus, which is present at birth, "
    "remains for life, and becomes darker and thicker."],
   ["Immediate involution beginning at birth with resolution by 6 weeks",
    "Involution follows the proliferative phase rather than preceding it, and the timescale is far longer."],
   ["Rapid growth with a high risk of malignant transformation",
    "Hemangiomas of infancy are the most common tumours of infancy and most are medically insignificant. Malignant "
    "transformation is not a feature."],
   ["No change in size at any point during childhood",
    "The lesion is defined by its biphasic growth pattern, which is what distinguishes it from a capillary "
    "malformation."]],
  0, 66, IO_B),

Q("Infantile hemangioma",
  "A 4-month-old has a large facial hemangioma that is beginning to obstruct the visual axis of one eye. What is "
  "first-line treatment?",
  [["An oral beta-blocker such as propranolol",
    "Correct. Beta-blockers are first-line treatment, for example oral propranolol or timolol. Indications for "
    "treatment include cosmetic concern, functional involvement such as blocked vision, deep ulceration, and "
    "infection."],
   ["Serial observation alone",
    "Serial observation is appropriate when no treatment is needed, but blocked vision is a listed functional "
    "indication for treatment, and untreated visual obstruction at this age threatens permanent amblyopia."],
   ["Pulsed dye laser as the primary treatment",
    "Pulsed dye laser targets superficial vessels to a depth of about 1.2 mm. It has a role but is not first line for "
    "a lesion causing functional compromise."],
   ["Systemic corticosteroids as first-line therapy",
    "Beta-blockers are named as first line. Corticosteroids are not the initial choice here."],
   ["Immediate surgical excision in all cases",
    "Surgical excision is one option among several rather than the first-line approach for a functional "
    "complication."]],
  0, 73, IO_B),

Q("Nevus flammeus",
  "Which statement best describes a nevus flammeus?",
  [["Present at birth, grows with the child, does not involute, and becomes darker and thicker over time",
    "Correct. Nevus flammeus is a congenital vascular lesion of dilated superficial dermal capillaries through the "
    "entire depth of the dermis, without endothelial proliferation. It is present at birth, grows in size with the "
    "child, does not involute, and becomes darker and thicker."],
   ["Appears six months after birth with quick proliferation and involution",
    "That pattern describes an infantile hemangioma, which has a rapid proliferative phase followed by slower "
    "involution. Nevus flammeus is present from birth and never involutes."],
   ["Present at birth and involutes completely by school age",
    "Involution is the hemangioma pattern. The absence of regression is what makes nevus flammeus a lifelong lesion "
    "with psychosocial consequences."],
   ["A soft yellow plaque of lipid-laden macrophages",
    "That describes xanthelasma, which is associated with lipid disorders and warrants hyperlipidaemia screening."],
   ["An acquired lesion formed by capillary proliferation in adults",
    "Acquired capillary proliferation in adults describes cherry angioma. Nevus flammeus is congenital and involves "
    "dilatation without proliferation."]],
  0, 78, IO_B),

Q("Nevus simplex",
  "A newborn has pink irregular macules on the nape of the neck and glabella that become more noticeable when he "
  "cries. What is this lesion?",
  [["Nevus simplex, a superficial variant of nevus flammeus commonly called a stork bite",
    "Correct. Nevus simplex is a congenital vascular lesion, a variant of nevus flammeus involving more superficial "
    "dermal capillaries. It is most common on the head and neck, presents as pink to erythematous irregular macules "
    "or patches, and becomes more noticeable when the infant cries."],
   ["An infantile hemangioma in its earliest phase",
    "The earliest sign of a hemangioma is blanching followed by fine telangiectasias and then a red macule, which "
    "then proliferates. Nevus simplex does not proliferate."],
   ["A port-wine stain that will darken and thicken over life",
    "Nevus flammeus, formerly called a port-wine stain, darkens and thickens and persists. Nevus simplex is the more "
    "superficial variant with a different course."],
   ["A cherry angioma",
    "Cherry angiomas are acquired lesions of adults that increase with age, appearing as deep red papules under 5 mm "
    "on the trunk."],
   ["A pyogenic granuloma",
    "Pyogenic granuloma is an acquired vascular lesion that grows rapidly after trauma and bleeds easily. It is not "
    "present at birth."]],
  0, 84, IO_B),

Q("Cherry angioma",
  "A 54-year-old woman is found on routine examination to have several smooth, firm, deep red papules under 5 mm on "
  "the trunk that blanch with pressure. She has never noticed them. What education should be given?",
  [["They are benign acquired lesions formed by capillary proliferation, and new ones will likely develop with no way "
    "to prevent them",
    "Correct. Cherry angiomas are acquired vascular lesions formed by capillary or venule proliferation, very common "
    "and increasing with age. Treatment is unnecessary unless they bother the patient, and patients should be aware "
    "that new lesions will likely develop and there is no way to prevent them."],
   ["They are benign lesions formed by capillary proliferation that can progress to malignancy if untreated",
    "The first half is correct, which is what makes this the most tempting distractor. But cherry angiomas remain "
    "benign; they do not transform, and framing them as premalignant would prompt needless procedures."],
   ["They are caused by an increase in melanocytes",
    "Melanocytic proliferation produces pigmented lesions such as naevi and lentigines. A blanchable red papule is "
    "vascular."],
   ["They require biopsy to establish the diagnosis",
    "The clinical features are characteristic enough for diagnosis by inspection, and treatment is not needed unless "
    "the patient is bothered."],
   ["They indicate an underlying liver disorder",
    "It is nevus araneus, the spider angioma, whose history includes asking about alcohol use and medications "
    "hazardous to the liver, along with pregnancy and hormone use."]],
  0, 87),

Q("Nevus araneus",
  "A 27-year-old pregnant woman has several lesions on the upper trunk consisting of a central arteriole with "
  "radiating capillaries. What is the mechanism, and what should be asked in the history?",
  [["Dilation of pre-existing vessels without proliferation, possibly from oestrogen excess; ask about pregnancy, "
    "hormone use, alcohol, and hepatotoxic medications",
    "Correct. Nevus araneus involves no vascular proliferation and is due to dilation of pre-existing vessels. "
    "Oestrogen excess states may be the cause, and lesions resolve after delivery or cessation of hormonal "
    "contraception. History should cover pregnancies, hormone use, alcohol, and high-risk medications for liver "
    "damage."],
   ["Proliferation of capillaries with age; no specific history is required",
    "Capillary proliferation with increasing age describes cherry angioma. The spider angioma is a dilation of "
    "existing vessels, and its associations are exactly what make the history important."],
   ["Dilated superficial dermal capillaries present from birth",
    "Congenital dilated dermal capillaries describe nevus flammeus, which is present at birth and persists for life."],
   ["A benign vascular tumour arising after minor trauma",
    "A rapidly growing vascular lesion after trauma that bleeds easily describes pyogenic granuloma."],
   ["Extravasation of blood into the dermis",
    "Deposits of blood in the skin are petechiae and purpura, which are non-blanching. Spider angiomas blanch and "
    "refill from the centre."]],
  0, 89),

Q("Pyogenic granuloma",
  "A 16-year-old girl is evaluated for a lesion on the finger pad that appeared rapidly after she injured the finger "
  "and bleeds easily when bumped. Examination shows a bright red, friable, pedunculated papule. What is the "
  "diagnosis, and what is notable about its name?",
  [["Pyogenic granuloma, which is misnamed because it is neither infectious nor granulomatous",
    "Correct. Pyogenic granuloma is an acquired vascular lesion that is misnamed, being neither infectious nor "
    "granulomatous. It is a benign vascular tumour common in children, young adults, and pregnancy, arising as a "
    "response to injury or hormonal factors, most often on the head, neck, and fingers."],
   ["Pyogenic granuloma, so named because it is a granulomatous response to bacterial infection",
    "This accepts the name at face value, which is the misconception the lecture corrects. The lesion is neither "
    "infectious nor granulomatous."],
   ["Cherry angioma",
    "Cherry angiomas are smooth firm deep red papules under 5 mm that occur with increasing age on the trunk. They do "
    "not appear rapidly after trauma on a finger in an adolescent."],
   ["Amelanotic melanoma",
    "Malignant melanoma is on the differential and is the reason histology may be sent, but the classic history of "
    "rapid growth after trauma with easy bleeding in a young patient fits the benign lesion."],
   ["Dermatofibroma",
    "A dermatofibroma is a firm nodule with a brown halo and a positive dimple sign, most commonly on the legs, and "
    "it does not bleed spontaneously."]],
  0, 95),

Q("Neurofibromatosis",
  "A 6-year-old boy has eight light brown macules greater than 5 mm and freckling in both axillae. What condition "
  "does this suggest, and what is the freckling called?",
  [["Neurofibromatosis type 1, with intertriginous freckling known as Crowe's sign",
    "Correct. Café au lait spots are often the first manifestation of neurofibromatosis type 1, defined as light tan "
    "to brown macules over 5 mm prepubertally. Intertriginous freckling in the axillary and inguinal regions is "
    "Crowe's sign, with freckles smaller than 5 mm."],
   ["Neurofibromatosis type 1, with intertriginous freckling known as Darier sign",
    "The condition is right but the sign is wrong. Darier sign is urtication of a lesion after stroking and indicates "
    "mastocytosis."],
   ["Neurofibromatosis type 2, with freckling from the NF2 gene on chromosome 22",
    "Neurofibromatosis type 2 involves the NF2 gene on chromosome 22, but the cutaneous manifestations described — "
    "café au lait spots, cutaneous neurofibromas, intertriginous freckling, and plexiform neurofibromas — belong to "
    "type 1, whose gene is on chromosome 17."],
   ["Multiple lentigines, with freckling caused by sun exposure",
    "Crowe's sign freckles do become more prominent with sun exposure, but they occur in intertriginous sites that "
    "are largely sun-protected, which is what makes them notable."],
   ["Post-inflammatory hyperpigmentation from chronic friction",
    "Post-inflammatory change requires prior inflammation at the site, and it would not produce discrete café au lait "
    "macules elsewhere on the body."]],
  0, 102, IO_B),

Q("Xanthelasma",
  "A 48-year-old man has soft yellow plaques on the medial aspects of both upper eyelids. What do they contain, and "
  "what should be done?",
  [["Lipid-laden macrophages, and he should be screened for hyperlipidaemia",
    "Correct. Xanthelasma consists of soft yellow cholesterol plaques formed by collections of lipid-laden "
    "macrophages. They are associated with lipid disorders, so screening for hyperlipidaemia is indicated, and they "
    "may signify increased cardiac risk."],
   ["Lipid-laden macrophages, requiring no further investigation since the lesions are cosmetic",
    "The composition is right but stopping at cosmesis discards the reason the lesion matters. The association with "
    "lipid disorders and increased cardiac risk is exactly what makes screening worthwhile."],
   ["Keratin within an enclosed epithelial cyst, requiring excision",
    "Keratin within enclosed epithelium describes an epidermoid cyst, which is a firm moveable nodule with a central "
    "punctum rather than a soft yellow eyelid plaque."],
   ["Eccrine duct neoplasms appearing at puberty",
    "Syringomas are eccrine duct neoplasms of the lower eyelids appearing at puberty, and they are firm "
    "skin-coloured papules rather than soft yellow plaques."],
   ["Dilated capillaries requiring laser therapy",
    "Dilated capillaries produce telangiectasias, which are blanchable and vascular rather than yellow and lipid "
    "laden."]],
  0, 104),

Q("Lipoma",
  "A 50-year-old woman has a soft, mobile, non-tender subcutaneous mass on the upper back that has been slowly "
  "enlarging for years. What is the most likely diagnosis and appropriate management?",
  [["Lipoma, the most common soft tissue tumour, which can be observed if asymptomatic",
    "Correct. A lipoma is a benign localised overgrowth of fat cells in subcutaneous tissue and the most common soft "
    "tissue tumour. Diagnosis is typically clinical, and asymptomatic tumours can be observed, with excision "
    "considered for cosmetically deforming or enlarging lesions."],
   ["Epidermoid cyst, which requires excision of the entire capsule",
    "An epidermoid cyst is on the lipoma differential, but it is a firm nodule with a central punctum that may "
    "discharge foul-smelling keratin rather than a soft mobile fatty mass."],
   ["Dermatofibroma, which shows a positive dimple sign",
    "Dermatofibroma is on the differential but is a firm 0.5 to 1 cm dermal nodule with a brown halo, most commonly "
    "on the legs."],
   ["Abscess, requiring incision and drainage",
    "An abscess is on the differential but is warm, tender, and erythematous with purulent contents rather than a "
    "painless mass present for years."],
   ["Liposarcoma, requiring urgent wide excision",
    "A slowly enlarging soft mobile subcutaneous mass is characteristic of the benign lesion. Rapid growth, fixation, "
    "or pain would change that assessment."]],
  0, 106),

Q("Digital mucous cyst",
  "A 58-year-old woman has a translucent skin-coloured papule over the distal interphalangeal joint of her index "
  "finger, with a longitudinal groove in the adjacent nail. What is the nature of this lesion?",
  [["A pseudo-cyst without a true cellular lining, representing extrusion of mucinous joint contents into the dermis",
    "Correct. Digital mucous cysts are pseudo-cysts without a cellular lining or true capsule. They represent "
    "extrusion of mucinous contents from a local joint space into the surrounding dermis, typically over the distal "
    "interphalangeal joint, and may distort the nail."],
   ["A true cyst lined by epithelium and filled with keratin",
    "Epithelial enclosure filled with keratin describes the epidermoid cyst. The absence of a true lining is what "
    "makes this lesion a pseudo-cyst."],
   ["A benign neoplasm of eccrine ducts",
    "Eccrine duct neoplasms are syringomas, which appear at puberty as multiple small papules on the eyelids."],
   ["A fibroproliferative overgrowth of dense fibrous tissue",
    "Overgrowth of dense fibrous tissue extending beyond wound margins describes a keloid."],
   ["A collection of lipid-laden macrophages",
    "Lipid-laden macrophages form xanthelasma at the medial eyelids."]],
  0, 107),

Q("Sebaceous hyperplasia",
  "A 63-year-old man has several soft whitish-yellow papules 3 to 5 mm on the forehead, each with a central dell. He "
  "is worried about skin cancer. What test can distinguish this from the main differential?",
  [["Dermoscopy, which can distinguish sebaceous hyperplasia from basal cell carcinoma",
    "Correct. Basal cell carcinoma is the principal differential for sebaceous hyperplasia, and dermoscopy can "
    "distinguish between them. Biopsy is performed if malignancy concern persists."],
   ["A potassium hydroxide preparation",
    "A potassium hydroxide preparation detects fungal elements and has no role in distinguishing two "
    "non-infectious papular lesions."],
   ["A Wood's lamp examination",
    "A Wood lamp evaluates pigment changes in selected fungal and bacterial infections. It does not differentiate "
    "sebaceous hyperplasia from basal cell carcinoma."],
   ["Serum lipid measurement",
    "Lipid screening is indicated for xanthelasma, which is associated with lipid disorders. Sebaceous hyperplasia "
    "reflects sebocyte turnover slowing with age rather than a lipid disorder."],
   ["No test is available, so all lesions must be excised",
    "Dermoscopy is available and non-invasive, and biopsy is reserved for continuing malignancy concern. Excising "
    "every lesion is unnecessary."]],
  0, 111),
]

QUESTIONS += [

Q("Hypertrophic scar",
  "A 30-year-old man has a raised, firm scar that developed within four weeks of a surgical incision. It remains "
  "within the original incision line and has flattened slightly over the past year. What management options apply?",
  [["Intralesional corticosteroid or 5-fluorouracil, compression therapy and silicone sheeting, surgical excision, "
    "or pulsed dye laser",
    "Correct. Hypertrophic scar management includes intralesional injection of corticosteroid or 5-fluorouracil, "
    "compression therapy and silicone sheeting, surgical excision, and pulsed dye laser, which reduces scar erythema "
    "by reducing neovascularisation."],
   ["No treatment is ever appropriate because hypertrophic scars always resolve completely",
    "Hypertrophic scars remain stable and regress with time, which is genuinely reassuring, but treatment options "
    "exist for symptoms and appearance and need not be withheld."],
   ["Excision alone, which is curative without adjunct because recurrence does not occur",
    "It is worth noting that excision of a keloid carries a 50 to 100 percent recurrence rate; even for hypertrophic "
    "scars, excision is one option among several rather than a guaranteed cure."],
   ["Cryotherapy is contraindicated in all scar management",
    "Cryotherapy with liquid nitrogen appears among keloid treatments, where it flattens lesions but can cause "
    "hypopigmentation. It is not universally contraindicated."],
   ["Systemic corticosteroids tapered over six weeks",
    "Steroid delivery for scars is intralesional rather than systemic, which concentrates the effect and avoids "
    "systemic exposure."]],
  0, 23),

Q("Keloid",
  "What is the theoretical basis for using silicone gel sheeting in keloid management, and how long is it worn?",
  [["It is thought to raise the temperature of the scar, increasing collagenase activity; it is worn 12 to 24 hours a "
    "day for up to a year",
    "Correct. The theory is that occlusive dressings such as silicone gel sheets increase the temperature of the scar "
    "and thereby collagenase activity. They are worn 12 to 24 hours a day for up to a year."],
   ["It cools the scar, reducing blood flow; it is worn for two weeks",
    "The proposed mechanism is an increase rather than a decrease in temperature, and the duration is far longer than "
    "two weeks."],
   ["It induces tissue hypoxia causing fibroblast degeneration; it is worn for one month",
    "Tissue hypoxia with fibroblast degeneration and collagen degradation is the proposed mechanism of compression "
    "therapy, which is a different modality using spandex pressure devices."],
   ["It delivers corticosteroid transdermally; it is worn for six weeks",
    "Silicone sheeting is not a drug delivery system. Corticosteroid for keloids is given by intralesional "
    "injection."],
   ["It provides ultraviolet protection to the scar; it is worn only outdoors",
    "Sun protection is generally advisable for scars but is not the stated rationale for silicone sheeting."]],
  0, 16),

Q("Infantile hemangioma",
  "What are the three types of infantile hemangioma, and which is the most common?",
  [["Superficial, which is the most common, presenting as a bright red papule, plaque, or nodule, plus mixed and "
    "deep types",
    "Correct. The superficial type is the most common, with dilated vessels in the dermis surrounded by "
    "proliferating endothelial cells, presenting as a bright red papule, plaque, or nodule and previously called a "
    "strawberry hemangioma. The deep type is the least common."],
   ["Deep, which is the most common, presenting as a pale or blue nodule",
    "The deep type involves dilated vessels in the deep dermis and subcutaneous tissue presenting as a pale, "
    "skin-coloured, red, or blue nodule, plaque, or tumour, and it is described as the least common."],
   ["Capillary, cavernous, and arteriovenous, with capillary the most common",
    "That older terminology is not the classification used here, which divides lesions by depth into superficial, "
    "mixed, and deep."],
   ["Congenital, infantile, and acquired, with congenital the most common",
    "Infantile hemangiomas are congenital vascular lesions as a group; the subtypes are defined by the depth of "
    "vessel involvement."],
   ["Proliferative, involuting, and involuted, with proliferative the most common",
    "Those terms describe phases of the natural history rather than morphological types."]],
  0, 67, IO_B),

Q("Infantile hemangioma",
  "What complications should be considered in a child with an infantile hemangioma?",
  [["Compression of vital structures, blocked vision, interference with feeding or respiration, obstruction of the "
    "external auditory canal, and extracutaneous lesions",
    "Correct. Hemangiomas may compress vital structures, block vision, interfere with feeding or respiration, "
    "obstruct the external auditory canal, and occur at extracutaneous sites."],
   ["Malignant transformation to angiosarcoma",
    "Hemangiomas of infancy are benign and most are medically insignificant. Malignant transformation is not among "
    "the described complications."],
   ["Progressive darkening and thickening throughout life",
    "Darkening and thickening over life describes nevus flammeus, which does not involute."],
   ["Systemic hypertension from arteriovenous shunting",
    "This is not among the listed complications; the concerns are local mass effect and extracutaneous involvement."],
   ["No complications occur, since all lesions involute",
    "Involution does occur, but the proliferative phase can produce functional compromise before it, which is why "
    "specific indications for treatment exist."]],
  0, 71, IO_B),

Q("Telangiectasia",
  "How is a telangiectasia defined, and what is its behaviour on pressure?",
  [["A permanently dilated capillary under 1 mm that blanches with pressure",
    "Correct. Telangiectasias are acquired vascular lesions consisting of permanently dilated capillaries under 1 mm. "
    "They blanch, may be single or grouped with a central punctum, may be primary or secondary, and are associated "
    "with numerous diseases."],
   ["A permanently dilated capillary under 1 mm that does not blanch with pressure",
    "The size and nature are right but the blanching is the key physical property, and getting it wrong would lead a "
    "clinician to mistake a dilated vessel for extravasated blood."],
   ["A deposit of blood 1 to 2 mm that does not blanch",
    "A non-blanching deposit of blood 1 to 2 mm is a petechia, which reflects extravasation rather than vessel "
    "dilatation."],
   ["A proliferation of capillaries producing a red papule",
    "Capillary proliferation producing a deep red papule describes a cherry angioma, which is a raised lesion rather "
    "than a dilated vessel."],
   ["A congenital malformation present from birth in all cases",
    "Telangiectasias are acquired vascular lesions and may be primary or secondary to numerous diseases."]],
  0, 88),

Q("Neurofibromatosis",
  "What size threshold defines a café au lait macule as significant before and after puberty?",
  [["Greater than 5 mm prepubertally and greater than 15 mm postpubertally",
    "Correct. Café au lait spots are light tan to brown macules greater than 5 mm prepubertally and greater than "
    "15 mm postpubertally. They are often the first manifestation of neurofibromatosis type 1 and are usually present "
    "at birth or appear during the first year."],
   ["Greater than 15 mm prepubertally and greater than 5 mm postpubertally",
    "The two thresholds are reversed. Applying the adult threshold to a child would dismiss significant lesions, and "
    "applying the child threshold to an adult would over-call ordinary pigmentation."],
   ["Greater than 5 mm at any age",
    "A single threshold ignores that lesions grow in proportion to the child, which is why the postpubertal cut-off "
    "is larger."],
   ["Greater than 1 cm at any age",
    "Neither stated threshold is 1 cm, and using one figure for all ages loses the developmental adjustment."],
   ["Size is not part of the definition",
    "Size is explicitly part of the definition and is what separates a café au lait macule from ordinary freckling, "
    "which in Crowe's sign is under 5 mm."]],
  0, 99, IO_B),

Q("Neurofibromatosis",
  "What is a plexiform neurofibroma, and what is the concern with it?",
  [["A tumour in the tissue covering nerves that is large and extensive and may be locally invasive",
    "Correct. Plexiform neurofibromas are tumours in the tissue covering nerves, occurring anywhere except the brain "
    "and spinal cord. They are large and extensive and may be locally invasive, so clinical evaluation is needed."],
   ["A discrete benign nerve sheath tumour protruding just above the skin surface",
    "That describes a cutaneous neurofibroma, which is a well-circumscribed solid tumour arising from peripheral "
    "nerves, sessile or pedunculated. Plexiform lesions are the larger, more extensive form."],
   ["A pigmented macule that grows in proportion to the child",
    "Growth in proportion to the child describes café au lait macules."],
   ["A cluster of freckles smaller than 5 mm in intertriginous areas",
    "Intertriginous freckling under 5 mm is Crowe's sign."],
   ["A tumour arising exclusively within the brain and spinal cord",
    "Plexiform neurofibromas occur anywhere except the brain and spinal cord."]],
  0, 101),

Q("Acrochordon",
  "How is an acrochordon best described morphologically, and where do they characteristically occur?",
  [["A soft pedunculated skin-coloured papilloma with a narrow stalk and broad tip, occurring in areas of friction "
    "such as the neck, axilla, and groin",
    "Correct. An acrochordon is a fibroepithelial pedunculated papilloma with a narrow stalk and broad tip, occurring "
    "in areas of friction — the neck, axilla, and groin. Incidence is increased in women and in obesity, and they "
    "vary from over 1 mm to as large as 10 mm."],
   ["A firm sessile nodule with a central keratin core on weight-bearing surfaces",
    "A central keratin core on a weight-bearing surface describes a clavus, which results from localised mechanical "
    "pressure."],
   ["A translucent papule over the distal interphalangeal joint",
    "A translucent papule over the distal interphalangeal joint is a digital mucous cyst."],
   ["A hard conical keratotic projection on sun-exposed skin",
    "A hard conical keratotic projection is a cutaneous horn, which arises from an underlying benign or malignant "
    "lesion."],
   ["A bright red friable pedunculated papule that bleeds easily",
    "A bright red friable pedunculated papule that bleeds readily after trauma describes pyogenic granuloma."]],
  0, 30),

Q("Sebaceous hyperplasia",
  "What is the pathophysiology of sebaceous hyperplasia, and what is its malignant potential?",
  [["Reduced turnover of sebocytes with age causing gland enlargement, with no known potential for malignant "
    "transformation",
    # Deck slide 109 says turnover SLOWS, crowding the gland. The earlier wording said it merely
    # "changes", which a student read backwards -- hyperplasia sounds like faster division.
    # Plain text, no tags/entities: every other explanation in these pools is plain, and the
    # group-study bank renders through a different engine than the quiz template.
    "Correct. With age the turnover of sebocytes, the sebum-producing epithelial cells, slows down; the cells "
    "then crowd inside the gland and the gland enlarges. The \u201chyperplasia\u201d is sebocytes accumulating "
    "because they are not being replaced, not dividing faster \u2014 slower turnover and a bigger gland are not "
    "a contradiction. No known potential for malignant transformation, though patients commonly present fearing "
    "skin cancer."],
   ["Proliferation of eccrine ducts, with a low risk of malignant transformation",
    "Eccrine duct proliferation describes syringoma. Neither lesion carries a described malignant potential, but the "
    "gland of origin here is sebaceous."],
   ["Overgrowth of dense fibrous tissue, with progressive local invasion",
    "Overgrowth of dense fibrous tissue describes a keloid, which enlarges but does not invade."],
   ["Ultraviolet-induced keratinocytic dysplasia that may progress to squamous cell carcinoma",
    "Ultraviolet-induced keratinocytic dysplasia describes actinic keratosis, a premalignant lesion. Sebaceous "
    "hyperplasia is benign."],
   ["Capillary proliferation, with a risk of haemorrhage",
    "Capillary proliferation describes cherry angioma, which may bleed after trauma."]],
  0, 109),

Q("Benign lesions overall",
  "A patient presents with a new benign lesion on a sun-exposed area. What opportunity does this create?",
  [["Counselling on sunscreen use, avoiding direct sun during peak hours, and performing periodic skin "
    "self-examination",
    "Correct. When discussing any new lesion in sun-exposed areas, the clinician should take the opportunity to "
    "counsel on sunscreen use, avoiding direct sun during peak hours, and performing periodic skin "
    "self-examinations."],
   ["Reassurance alone, since the lesion is benign and no further discussion is warranted",
    "Reassurance about the lesion is appropriate, but stopping there wastes an encounter in which the patient has "
    "already brought their sun-exposed skin to attention."],
   ["Immediate referral for full-body photography in every patient",
    "Full-body photographic surveillance is a specialist tool for high-risk patients rather than a universal response "
    "to a benign lesion."],
   ["Prophylactic excision of all lesions in sun-exposed areas",
    "Excising benign lesions prophylactically causes scarring without benefit."],
   ["Advising complete avoidance of all outdoor activity",
    "The counselling is to avoid direct sun during peak hours and use sunscreen, not to avoid the outdoors entirely, "
    "which is neither realistic nor advised."]],
  0, 112),
]
