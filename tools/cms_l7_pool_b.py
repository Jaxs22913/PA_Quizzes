# CMS I Lecture 7 (Benign Skin Lesions) — SET 1 pool B.
# Cutaneous horn, acrochordon, pressure injury and pilonidal cyst.
#
# SLIDES 33 AND 34 ARE IMAGES, and the entire pressure injury staging system is
# in them -- the extracted text of both is a bare title. The six stages below
# are transcribed from those two tables (the National Pressure Injury Advisory
# Panel diagrams), which also illustrate every stage in BOTH lightly and darkly
# pigmented skin. Slide 42 is likewise an image, and it is the only place the
# sinus-versus-fistula distinction appears.
#
# Options drafted at MATCHED LENGTHS; the staging questions are the compare-and-
# contrast shape, so every distractor carries a full stage description too.
#
# Every question carries slot="..." per the fact-slot standard.
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "7. Benign Skin Lesions Prof Griffenkranz 8-25-2025-2.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis for benign skin lesions"
IOB = "Objective b — Identify medical strategies for common benign skin lesions in infants, adolescents, adults and the elderly"

POOL_B = [
 dict(topic="Cutaneous horn", io=IOA, slot="etiology",
   q="What is a cutaneous horn made of, and what is the most important thing about it?",
   opts=[
     ["Keratin, forming a hard conical outward projection; the process at the base of the lesion is what matters",
      "Correct — the horn itself is only the visible top of something else."],
     ["Sebum, forming a soft yellow cholesterol plaque on the eyelid; the associated lipid disorder is what matters",
      "That describes xanthelasma, and its content is lipid rather than keratin."],
     ["Mucin, forming a translucent papule over a distal finger joint; the underlying osteoarthritis is what matters",
      "That describes a digital mucous cyst."],
     ["Fibrous tissue, forming a firm nodule with a pigmented halo; the preceding trauma or insect bite is what matters",
      "That describes a dermatofibroma."]],
   c=0, cite=c(25)),

 dict(topic="Cutaneous horn", io=IOA, slot="differential",
   q="Which lesions can a cutaneous horn arise from?",
   opts=[
     ["Actinic keratosis, warts, seborrheic keratosis, keratoacanthoma, and basal or squamous cell carcinoma",
      "Correct — benign and malignant bases both occur, which is the whole problem."],
     ["Keloid, hypertrophic scar, dermatofibroma and foreign-body granuloma, all of which are fibrous",
      "Those are the fibrous lesions in the keloid differential."],
     ["Cherry angioma, spider angioma, pyogenic granuloma and telangiectasia, all of which are vascular",
      "Those are vascular lesions and do not form horns."],
     ["Epidermoid cyst, lipoma, syringoma and sebaceous hyperplasia, all of which are adnexal or soft tissue",
      "None of these is named as a base for a cutaneous horn."]],
   c=0, cite=c(25)),

 dict(topic="Cutaneous horn", io=IOA, slot="epidemiology",
   q="Who gets cutaneous horns, and where?",
   opts=[
     ["Caucasians over fifty, equally male and female, on the head, neck and upper extremities",
      "Correct — the sun-exposed sites are the face, ears and hands."],
     ["Females at puberty, on the eyelids and upper cheeks, in small crops of papules",
      "That epidemiology and distribution belong to syringoma."],
     ["Males two to one, very commonly, on the face, scalp, neck and trunk",
      "That is the epidermoid cyst's epidemiology."],
     ["Preterm Caucasian infants, females three to one, with a predilection for head and neck",
      "That is the infantile hemangioma's epidemiology."]],
   c=0, cite=c(26)),

 dict(topic="Cutaneous horn", io=IOA, slot="gold standard",
   q="How is the lesion under a cutaneous horn diagnosed?",
   opts=[
     ["By deep shave biopsy, to sample the underlying tissue",
      "Correct — there is often no clinical feature that separates benign from malignant."],
     ["By dermoscopy, which shows a peripheral pigment network with a central white mass",
      "That dermoscopic pattern belongs to dermatofibroma."],
     ["Clinically, because the shape of the horn indicates the underlying process",
      "The deck says the opposite: appearance often does not distinguish them."],
     ["By culture of expressed material, because infection underlies most lesions",
      "There is no infectious component described here."]],
   c=0, cite=c(27)),

 dict(topic="Cutaneous horn", io=IOA, slot="first-line",
   q="What determines the management of a cutaneous horn?",
   opts=[
     ["The underlying etiology, with excision to the standard for the tumour type and location if malignant",
      "Correct — you treat what is at the base, not the horn."],
     ["The height of the horn itself, with excision reserved for any projection measuring over one centimetre",
      "Size of the projection is not what drives the decision."],
     ["The patient's age at presentation, with watchful observation preferred in anyone over the age of seventy",
      "Age is not the management criterion given."],
     ["The cosmetic concern of the patient alone, since the underlying lesion is benign in essentially every case",
      "The lesion is not always benign, which is precisely the point."]],
   c=0, cite=c(28)),

 dict(topic="Acrochordon", io=IOA, slot="etiology",
   q="What is an acrochordon, anatomically?",
   opts=[
     ["A fibroepithelial pedunculated papilloma, with a narrow stalk and a broad tip",
      "Correct — which is why it can be snipped off at the stalk."],
     ["A benign neoplasm of eccrine ducts, appearing in crops around the eyes",
      "That is a syringoma."],
     ["A cystic enclosure of epithelium within the dermis, filled with keratin",
      "That is an epidermoid cyst."],
     ["A localised overgrowth of fat cells within the subcutaneous tissue",
      "That is a lipoma."]],
   c=0, cite=c(29)),

 dict(topic="Acrochordon", io=IOA, slot="epidemiology",
   q="In whom and where do skin tags occur, and how common are they?",
   opts=[
     ["Increased in females and obese patients, in areas of friction such as the neck, axilla and groin; present in sixty per cent of people by age seventy",
      "Correct — very common, and increasingly so with age."],
     ["Increased in males two to one, on the face, the scalp, the neck and the trunk; very common and occurring at any adult age",
      "That is the epidermoid cyst's distribution."],
     ["Increased in females two to one, on the legs and the arms, and found in all races; a common lesion appearing after minor trauma",
      "That is the dermatofibroma's epidemiology."],
     ["Increased in males three to one, over the coccyx and along the gluteal cleft; recurrence after treatment is common",
      "That is the pilonidal cyst."]],
   c=0, cite=c(29)),

 dict(topic="Acrochordon", io=IOA, slot="manifestation",
   q="What does a skin tag look like on examination?",
   opts=[
     ["Soft pedunculated skin-coloured papules on a thin stalk, ranging from about one millimetre up to ten millimetres",
      "Correct — and the history is that they are asymptomatic."],
     ["Firm brown nodules half a centimetre to one centimetre across, with a pink hue and a scaly surface",
      "That is the dermatofibroma."],
     ["Whitish-yellow soft papules two to nine millimetres across, with a central umbilication",
      "That is sebaceous hyperplasia."],
     ["Smooth firm deep-red papules under five millimetres across, which blanch with pressure",
      "That is the cherry angioma."]],
   c=0, cite=c(30)),

 dict(topic="Acrochordon", io=IOA, slot="first-line",
   q="How are skin tags removed, and what is notable about the procedure?",
   opts=[
     ["Scissor excision, cryotherapy or electrodesiccation; anesthesia is not necessary",
      "Correct — treatment is usually for cosmesis in the first place."],
     ["Elliptical excision with five-millimetre margins; local anesthesia is required",
      "Those margins belong to keratoacanthoma, where malignancy is a concern."],
     ["Surgical removal of the entire capsule; the lesion must not be inflamed",
      "That is epidermoid cyst surgery."],
     ["Incision and drainage; the cavity is then packed and allowed to heal",
      "That is the treatment of an acute pilonidal abscess."]],
   c=0, cite=c(30)),

 dict(topic="Acrochordon", io=IOA, slot="education",
   q="What should a patient be told about skin tags?",
   opts=[
     ["They are harmless growths of normal skin, they can bleed when they come off, and they should never be cut or pulled off at home",
      "Correct — and a new tag often forms in the same area after removal."],
     ["They are premalignant lesions, they must be biopsied before removal, and they should be monitored every three months",
      "None of this is true of an acrochordon."],
     ["They are caused by a virus, they are contagious to household contacts, and they should be covered at all times",
      "Skin tags are not infectious; the wart is the viral lesion here."],
     ["They are a sign of a lipid disorder, they warrant fasting cholesterol testing, and they may indicate cardiac risk",
      "That association belongs to xanthelasma."]],
   c=0, cite=c(31)),

 dict(topic="Pressure injury", io=IOA, slot="etiology",
   q="What causes a pressure injury?",
   opts=[
     ["Unrelieved pressure damaging underlying tissue, generally soft tissue compressed between a bony prominence and an external surface for a prolonged time",
      "Correct — the injury ranges from intact skin to ulcers reaching bone."],
     ["Repeated friction over a broad area of skin, producing diffuse hyperkeratosis with a poorly defined margin and no central keratin core at all",
      "That is the callus."],
     ["Disruption of the skin over the coccyx drawing in hair and debris, with follicular plugging that prevents drainage",
      "That is the pilonidal cyst."],
     ["Loss of the control mechanisms that normally regulate tissue repair, producing overgrowth of dense fibrous tissue",
      "That is abnormal wound healing, giving keloid or hypertrophic scar."]],
   c=0, cite=c(32)),

 dict(topic="Pressure injury", io=IOA, slot="manifestation",
   q="What defines a stage 1 pressure injury?",
   opts=[
     ["A localised area of non-blanchable erythema of intact skin",
      "Correct — intact skin is what keeps it at stage 1."],
     ["Partial-thickness skin loss with exposed dermis and a viable pink or red wound bed",
      "That is stage 2."],
     ["Full thickness skin loss with adipose tissue visible in the wound bed",
      "That is stage 3."],
     ["Persistent non-blanchable deep red or purple discolouration, with skin intact or not",
      "That is a deep tissue pressure injury, which is its own category."]],
   c=0, cite=c(33)),

 dict(topic="Pressure injury", io=IOA, slot="manifestation",
   q="What defines a stage 2 pressure injury?",
   opts=[
     ["Partial-thickness skin loss with exposed dermis; the wound bed is viable and pink or red, and may be moist, shiny or dry",
      "Correct — viable dermis, and no fat visible."],
     ["Full thickness skin loss in which adipose tissue is clearly visible in the wound bed, but fascia and muscle are not",
      "Visible fat makes it stage 3."],
     ["A localised area of non-blanchable erythema over completely intact skin, with no loss of epidermis anywhere in it",
      "Intact skin is stage 1."],
     ["Obscured full thickness skin and tissue loss whose depth cannot be judged because slough or eschar covers the bed",
      "That is unstageable."]],
   c=0, cite=c(33)),

 dict(topic="Pressure injury", io=IOA, slot="differential",
   q="What separates a stage 3 pressure injury from a stage 4?",
   opts=[
     ["Stage 3 shows full thickness loss with adipose tissue visible; stage 4 shows exposed fascia, muscle, tendon, ligament, cartilage or bone",
      "Correct — fat means three, deeper structures mean four."],
     ["Stage 3 shows partial-thickness loss with exposed dermis; stage 4 shows full thickness loss with adipose tissue visible",
      "Those are the stage 2 and stage 3 descriptions."],
     ["Stage 3 shows non-blanchable erythema of entirely intact skin; stage 4 shows partial-thickness loss with the dermis exposed",
      "Those are the stage 1 and stage 2 descriptions."],
     ["Stage 3 is wholly covered by slough or eschar; stage 4 is a persistent deep red or purple discolouration of intact skin",
      "Those describe unstageable and deep tissue injury respectively."]],
   c=0, cite=c(33)),

 dict(topic="Pressure injury", io=IOA, slot="manifestation",
   q="What makes a pressure injury unstageable?",
   opts=[
     ["Full thickness skin and tissue loss whose extent cannot be determined because it is obscured by slough or eschar",
      "Correct — the depth is unknowable until the cover is removed."],
     ["Full thickness skin loss in which only adipose tissue can be seen in the wound bed, with no deeper structure exposed",
      "That is a stage 3, and it is perfectly stageable."],
     ["Persistent non-blanchable deep red or purple discolouration of skin that may be either intact or non-intact",
      "That is a deep tissue pressure injury, a separate category."],
     ["A localised area of non-blanchable erythema over skin that is otherwise entirely intact and undamaged",
      "That is stage 1."]],
   c=0, cite=c(34)),

 dict(topic="Pressure injury", io=IOA, slot="manifestation",
   q="What defines a deep tissue pressure injury?",
   opts=[
     ["Persistent non-blanchable deep red or purple discolouration; the skin can be intact or non-intact",
      "Correct — the colour is the finding, and intact skin does not exclude it."],
     ["Obscured full thickness loss whose extent cannot be determined because of slough or eschar",
      "That is unstageable."],
     ["A localised area of non-blanchable erythema of intact skin, without discolouration in depth",
      "That is stage 1, where the change is superficial erythema."],
     ["Full thickness skin and tissue loss exposing fascia, muscle, tendon, ligament, cartilage or bone",
      "That is stage 4."]],
   c=0, cite=c(34)),

 dict(topic="Pressure injury", io=IOB, slot="education",
   q="What does the deck call the best measure against pressure injury, and what does it include?",
   opts=[
     ["Prevention: frequent skin assessment, nutrition assessment, moisture control and skin care, repositioning every two hours, pain management, improved mobility and specialty mattresses",
      "Correct — barrier creams and incontinence management sit under moisture control."],
     ["Early debridement: removal of the necrotic tissue, eschar and slough that promote infection, delay granulation and impede healing, as soon as any injury is identified at any stage",
      "Debridement is management of an established injury rather than prevention."],
     ["Prophylactic antibiotics: routinely covering skin flora in every immobile patient in order to prevent any wound infection before it has a chance to start",
      "No prophylactic antibiotic strategy is described."],
     ["Occlusive dressings: silicone gel sheeting worn twelve to twenty-four hours a day over every bony prominence at risk",
      "Silicone sheeting is a scar treatment in this lecture."]],
   c=0, cite=c(35)),

 dict(topic="Pressure injury", io=IOA, slot="agent/regimen",
   q="How often should a patient at risk of pressure injury be repositioned?",
   opts=[
     ["Every two hours",
      "Correct — alongside skin care, nutrition and specialty mattresses."],
     ["Every eight hours",
      "That is far longer than the interval given."],
     ["Once per nursing shift",
      "The interval is specified in hours rather than by shift."],
     ["Only when the patient reports discomfort",
      "Waiting for symptoms defeats the purpose of prevention."]],
   c=0, cite=c(35)),

 dict(topic="Pressure injury", io=IOA, slot="referral",
   q="Which referrals are named in the management of a pressure injury?",
   opts=[
     ["A wound care specialist, and surgery for debridement or wound closure",
      "Correct — management otherwise depends on the stage."],
     ["Podiatry, and dermatology for a deep shave biopsy of the base",
      "Podiatry is the corn and callus referral in the diabetic patient."],
     ["A vascular anomalies specialist, and paediatrics for growth monitoring",
      "That referral belongs to infantile hemangioma."],
     ["Cardiology, after screening for hyperlipidemia",
      "That follows from xanthelasma rather than from a pressure injury."]],
   c=0, cite=c(36)),

 dict(topic="Pressure injury", io=IOA, slot="first-line",
   q="What does debridement remove, and why?",
   opts=[
     ["Necrotic tissue, eschar and slough, because they promote infection, delay granulation and impede healing",
      "Correct — all three reasons are given together."],
     ["The entire cyst capsule, because leaving any part of it behind essentially guarantees that the lesion recurs",
      "Capsule removal is epidermoid cyst surgery."],
     ["The cone-shaped central keratin core, because it is what transmits the pressure down into the skin",
      "That is the corn."],
     ["The proliferating endothelial cells, because they are what drive the lesion to keep enlarging over months",
      "Endothelial proliferation belongs to infantile hemangioma."]],
   c=0, cite=c(36)),

 dict(topic="Pressure injury", io=IOA, slot="agent/regimen",
   q="Which dressings are named for meticulous care of an established pressure wound?",
   opts=[
     ["Silicone and hydrocolloid dressings",
      "Correct — alongside infection control and stage-appropriate management."],
     ["Wet-to-dry gauze changed three times daily",
      "That is not the dressing choice on the slide."],
     ["Silver sulfadiazine cream under an occlusive film",
      "No topical antimicrobial is specified here."],
     ["Compression bandaging at twenty-five millimetres of mercury",
      "That pressure belongs to keloid compression therapy."]],
   c=0, cite=c(36)),

 dict(topic="Pilonidal cyst", io=IOA, slot="etiology",
   q="How does a pilonidal cyst form?",
   opts=[
     ["Disruption of skin over the coccyx creates a pit that draws in hair and debris, causing follicular plugging; the ingrown hairs prevent drainage and promote abscess formation",
      "Correct — once thought congenital, now believed acquired."],
     ["Soft tissue compressed between a bony prominence and an external surface for a prolonged period, with unrelieved pressure damaging the tissue beneath",
      "That is a pressure injury, which also favours the sacrum."],
     ["Cystic enclosure of epithelium within the dermis that fills progressively with keratin rather than with sebum",
      "That is an epidermoid cyst."],
     ["Extrusion of mucinous contents from a nearby joint space into the surrounding dermis, compacting the cells at its margin",
      "That is a digital mucous cyst."]],
   c=0, cite=c(37)),

 dict(topic="Pilonidal cyst", io=IOA, slot="epidemiology",
   q="What is the sex ratio for pilonidal cyst, and what was the old belief about its origin?",
   opts=[
     ["Male to female three to one; originally thought congenital, now believed acquired",
      "Correct — and recurrence is common."],
     ["Female to male three to one; originally thought acquired, now believed congenital",
      "Both halves are reversed here."],
     ["Male to female two to one; thought to arise from the pilosebaceous unit",
      "That ratio and origin describe the epidermoid cyst and keratoacanthoma."],
     ["Female to male two to one; thought to follow trauma or an insect bite",
      "That is the dermatofibroma."]],
   c=0, cite=c(37)),

 dict(topic="Pilonidal cyst", io=IOA, slot="risk factors",
   q="Which risk factors are listed for pilonidal cyst?",
   opts=[
     ["Obesity, local trauma or irritation, sedentary lifestyle, increased hair density in the natal cleft, and family history",
      "Correct — hair density in the cleft is the distinctive one."],
     ["Age over forty, cumulative sun exposure, very fair skin that always burns, tattoos with red ink, and previous skin trauma",
      "Those are the keratoacanthoma risk factors."],
     ["Prolonged immobility, untreated incontinence, poor nutritional status, and impaired mobility or sensation at the site",
      "Those are pressure injury risks, which also affect the sacral area."],
     ["African American, Hispanic or Asian ancestry, together with any preceding wound, burn, vaccination site or piercing",
      "Those are the keloid risks."]],
   c=0, cite=c(39)),

 dict(topic="Pilonidal cyst", io=IOA, slot="manifestation",
   q="How does an acute pilonidal abscess present, and how does chronic disease present?",
   opts=[
     ["Acutely, sudden pain and swelling in or along the gluteal cleft; chronically, recurrent drainage and pain from one or more sinus tracts",
      "Correct — a hair may occasionally be seen protruding from a sinus opening."],
     ["Acutely, recurrent purulent drainage from several sinus tracts; chronically, sudden pain and swelling over the sacrum",
      "This reverses the acute and chronic presentations."],
     ["Acutely, a rapidly growing vascular nodule that bleeds easily; chronically, a flat uniformly pigmented patch",
      "That describes pyogenic granuloma and a lentigo instead."],
     ["Acutely, non-blanchable erythema over intact skin; chronically, a deep ulcer extending as far as bone",
      "That is the pressure injury staging spectrum."]],
   c=0, cite=c(40)),

 dict(topic="Pilonidal cyst", io=IOA, slot="test finding",
   q="What is fluctuance, and where would you find it in pilonidal disease?",
   opts=[
     ["A wave-like movement or fluid shift on palpation indicating the lesion is fluid filled, found over an acute abscess",
      "Correct — the abscess is also warm, tender and erythematous."],
     ["A retraction of the lesion beneath the skin surface on lateral compression, found over a chronic sinus tract",
      "That is the dimple sign of a dermatofibroma."],
     ["A complete blanching of the lesion under direct pressure, found anywhere along the gluteal cleft",
      "Blanching is a vascular lesion finding."],
     ["A palpable central punctum communicating with the skin surface, found over a previously healed tract",
      "A central punctum is the epidermoid cyst's finding."]],
   c=0, cite=c(41)),

 dict(topic="Pilonidal cyst", io=IOA, slot="differential",
   q="What is the difference between a sinus and a fistula?",
   opts=[
     ["A sinus is a blind track; a fistula is a track connecting two epithelium-lined surfaces",
      "Correct — both usually arise from a preceding abscess."],
     ["A sinus connects two epithelium-lined surfaces; a fistula is a blind-ending track",
      "This reverses the two definitions."],
     ["A sinus is lined by keratin; a fistula is lined by granulation tissue only",
      "The distinction is about where the track ends, not what lines it."],
     ["A sinus follows a surgical wound; a fistula is always congenital in origin",
      "Both usually follow an abscess rather than differing in origin this way."]],
   c=0, cite=c(42)),

 dict(topic="Pilonidal cyst", io=IOA, slot="initial test",
   q="What diagnostic testing does pilonidal disease usually require?",
   opts=[
     ["None usually needed",
      "Correct — it is a clinical diagnosis."],
     ["Culture of the drainage before any antibiotic is started",
      "No culture requirement is stated for this diagnosis."],
     ["Magnetic resonance imaging to map the sinus tracts",
      "Imaging is not part of the routine work-up described."],
     ["Punch biopsy of the sinus opening to exclude malignancy",
      "Biopsy is not described as part of the diagnosis here."]],
   c=0, cite=c(43)),

 dict(topic="Pilonidal cyst", io=IOA, slot="first-line",
   q="How is pilonidal disease managed at each stage?",
   opts=[
     ["Keep the area clean and free of debris, with shaving or laser hair therapy; an acute abscess needs incision and drainage; chronic disease may need surgical referral for excision",
      "Correct — hygiene first, drainage for the abscess, surgery for the chronic tract."],
     ["Keep the area covered and moist with hydrocolloid dressings; an acute abscess is treated with oral antibiotics alone; chronic disease resolves without intervention",
      "Neither the dressing approach nor antibiotics alone is what is described."],
     ["Intralesional corticosteroid for the acute lesion, followed by silicone sheeting and compression for the chronic phase",
      "Those are scar treatments."],
     ["Observation only, since most lesions involute spontaneously by school age",
      "Spontaneous involution belongs to infantile hemangioma."]],
   c=0, cite=c(43)),

 dict(topic="Pilonidal cyst", io=IOA, slot="education",
   q="What patient education is given for pilonidal disease?",
   opts=[
     ["Maintain good hygiene, and seek care if an abscess occurs",
      "Correct — recurrence is common, so this is ongoing advice."],
     ["Avoid stretching the scar and avoid hot baths after surgery",
      "That is keloid education."],
     ["Never cut or pull the lesion off at home, as it will bleed",
      "That is skin tag education."],
     ["Use sunscreen and perform periodic skin self-examination",
      "That is the general benign-lesion counselling point."]],
   c=0, cite=c(43)),
]
