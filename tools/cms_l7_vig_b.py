# CMS I Lecture 7 (Benign Skin Lesions) — SET 2, vignette pool B.
# Pressure injury, pilonidal disease, dermatofibroma, keratoacanthoma,
# epidermoid cyst and syringoma.
#
# The staging vignettes come from slides 33 and 34, which are IMAGES -- the
# extracted text of both is a bare title. Every stage description here was read
# off the National Pressure Injury Advisory Panel tables at full size.
#
# Deliberately LIGHT on diagnosis lead-ins: pool A already sits at eight of
# twenty-four, and the partition's skew guard fails a set above forty per cent.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "7. Benign Skin Lesions Prof Griffenkranz 8-25-2025-2.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis for benign skin lesions"
IOB = "Objective b — Identify medical strategies for common benign skin lesions in infants, adolescents, adults and the elderly"

VIG_B = [
 dict(topic="Pressure injury", io=IOB, lead="diagnosis",
   q="An 84-year-old nursing home resident has a reddened area over her sacrum. The skin is intact and the erythema does not blanch when you press on it. Which stage of pressure injury is this?",
   opts=[
     ["Stage 1",
      "Correct — non-blanchable erythema of intact skin."],
     ["Stage 2",
      "Stage 2 has partial-thickness loss with the dermis exposed."],
     ["Deep tissue pressure injury",
      "That is a deep red or purple discolouration rather than erythema."],
     ["Unstageable",
      "Unstageable requires slough or eschar obscuring the wound bed."]],
   c=0, cite=c(33)),

 dict(topic="Pressure injury", io=IOB, lead="diagnosis",
   q="A 78-year-old man has a sacral wound with partial-thickness skin loss. The exposed dermis is pink, viable and moist. No fat is visible. Which stage is this?",
   opts=[
     ["Stage 2",
      "Correct — partial thickness, viable pink-red bed, no adipose visible."],
     ["Stage 3",
      "Stage 3 requires visible adipose tissue."],
     ["Stage 1",
      "Stage 1 has intact skin."],
     ["Stage 4",
      "Stage 4 exposes fascia, muscle, tendon, ligament, cartilage or bone."]],
   c=0, cite=c(33)),

 dict(topic="Pressure injury", io=IOB, lead="test",
   q="A 69-year-old woman admitted after a hip fracture has a heel wound with full-thickness skin loss and yellow adipose tissue clearly visible in the base. No tendon or bone can be seen. Which stage is this?",
   opts=[
     ["Stage 3",
      "Correct — full thickness with fat visible, and nothing deeper exposed."],
     ["Stage 4",
      "Stage 4 requires exposed fascia, muscle, tendon, ligament, cartilage or bone."],
     ["Stage 2",
      "Stage 2 is partial thickness with no fat visible."],
     ["Unstageable",
      "The base is visible here, so the depth can be judged."]],
   c=0, cite=c(33)),

 dict(topic="Pressure injury", io=IOB, lead="test",
   q="A 74-year-old man who uses a wheelchair has an ischial wound whose base is covered entirely by thick black eschar. You cannot see how deep it goes. Which stage is this?",
   opts=[
     ["Unstageable",
      "Correct — full-thickness loss whose extent is obscured by slough or eschar."],
     ["Stage 4",
      "Stage 4 requires that deeper structures actually be visible."],
     ["Deep tissue pressure injury",
      "That is discolouration of skin rather than an eschar-covered wound."],
     ["Stage 3",
      "Stage 3 requires adipose tissue to be visible in the bed."]],
   c=0, cite=c(34)),

 dict(topic="Pressure injury", io=IOB, lead="diagnosis",
   q="A patient has a persistent deep purple discolouration over the heel. The skin over it is intact and the colour does not blanch. Which is the most likely classification?",
   opts=[
     ["Deep tissue injury",
      "Correct — a persistent non-blanchable deep red or purple discolouration, with the skin either intact or non-intact."],
     ["Stage 1",
      "Stage 1 is erythema rather than deep red or purple discolouration."],
     ["Unstageable",
      "Unstageable requires slough or eschar over an open wound."],
     ["Stage 2",
      "Stage 2 has partial-thickness loss with exposed dermis."]],
   c=0, cite=c(34)),

 dict(topic="Pressure injury", io=IOB, lead="treatment",
   q="A ward sister asks how best to reduce pressure injuries among her immobile patients. Which is the most appropriate answer?",
   opts=[
     ["Prevention, and the deck calls it the best measure",
      "Correct — frequent skin assessment, nutrition assessment, moisture control and skin care, repositioning every two hours, pain management, improved mobility and specialty mattresses such as an air mattress."],
     ["Prophylactic antibiotics for every patient with limited mobility",
      "No prophylactic antibiotic strategy is described."],
     ["Silicone gel sheeting applied over every bony prominence",
      "Silicone sheeting is a scar treatment in this lecture."],
     ["Early debridement of any area of erythema that appears",
      "Debridement treats an established wound rather than preventing one."]],
   c=0, cite=c(35)),

 dict(topic="Pressure injury", io=IOB, lead="next step",
   q="An 81-year-old patient has a stage 4 sacral wound with necrotic tissue and slough in the base. Which is the most appropriate next step?",
   opts=[
     ["Refer for surgical debridement",
      "Correct — necrotic tissue, eschar and slough promote infection and impede healing."],
     ["Apply a silicone dressing and review in a month",
      "Dressings are part of care, but the necrotic tissue must come out."],
     ["Start oral antibiotics and continue current dressings",
      "Infection control matters, but debridement is the step described."],
     ["Reposition two-hourly and take no further action",
      "Repositioning is prevention, not treatment of an established stage 4 wound."]],
   c=0, cite=c(36)),

 dict(topic="Pilonidal cyst", io=IOA, lead="diagnosis",
   q="A 22-year-old man who drives a lorry presents with sudden pain and swelling over his sacrum. There is a warm, tender, erythematous fluctuant swelling in the gluteal cleft with a hair protruding from a small opening. Which is the most likely diagnosis?",
   opts=[
     ["Pilonidal abscess",
      "Correct — the natal cleft, the sinus opening and the protruding hair."],
     ["Stage 2 pressure injury",
      "A pressure injury is a wound rather than a fluctuant abscess with a sinus."],
     ["Epidermoid cyst",
      "That is a movable nodule with a central punctum, most often face, scalp, neck or trunk."],
     ["Hidradenitis suppurativa",
      "That involves apocrine-bearing skin with sinus tracts and scarring."]],
   c=0, cite=c(41)),

 dict(topic="Pilonidal cyst", io=IOA, lead="treatment",
   q="The same patient's abscess is tense and fluctuant. Which is the most appropriate immediate management?",
   opts=[
     ["Incision and drainage",
      "Correct — an acute abscess requires drainage."],
     ["Oral antibiotics alone, with review in one week",
      "Antibiotics alone do not address a collection."],
     ["Referral to a surgeon for definitive excision now",
      "Excision is for chronic disease rather than the acute abscess."],
     ["Laser hair removal to the natal cleft",
      "Hair removal helps prevent recurrence but not the acute problem."]],
   c=0, cite=c(43)),

 dict(topic="Pilonidal cyst", io=IOA, lead="education",
   q="After drainage, the patient asks how to stop the problem recurring. Which is the most appropriate advice?",
   opts=[
     ["Keep the area clean and free of debris, and consider shaving or laser hair therapy",
      "Correct — and seek care promptly if an abscess occurs again."],
     ["Avoid sitting for more than two hours at a time and use a specialty cushion",
      "Repositioning belongs to pressure injury prevention."],
     ["Apply an over-the-counter salicylic acid preparation twice weekly",
      "Keratolytics have no role here."],
     ["Avoid ear piercing and other cosmetic procedures",
      "That advice is for the keloid-prone patient."]],
   c=0, cite=c(43)),

 dict(topic="Pilonidal cyst", io=IOA, lead="test",
   q="Which diagnostic testing does this patient's pilonidal disease require?",
   opts=[
     ["None; the diagnosis is clinical",
      "Correct — no testing is usually needed."],
     ["Magnetic resonance imaging to map any sinus tracts",
      "Imaging is not part of the described work-up."],
     ["Punch biopsy of the sinus opening",
      "Biopsy is not required for this diagnosis."],
     ["Wound culture before any intervention",
      "Culture is not stated as a requirement."]],
   c=0, cite=c(43)),

 dict(topic="Pilonidal cyst", io=IOA, lead="education",
   q="A patient has a blind-ending track opening onto the skin over the coccyx. Which term describes it, and how does it differ from the alternative?",
   opts=[
     ["A sinus; a fistula instead connects two epithelium-lined surfaces",
      "Correct — both usually arise from a preceding abscess."],
     ["A fistula; a sinus instead connects two epithelium-lined surfaces",
      "This reverses the two definitions."],
     ["A sinus; a fistula instead is always congenital in origin",
      "The difference is where the track ends, not its origin."],
     ["A fistula; a sinus instead is lined with keratin",
      "Lining is not the distinction being drawn."]],
   c=0, cite=c(42)),

 dict(topic="Dermatofibroma", io=IOA, lead="diagnosis",
   q="A 33-year-old woman has a firm 8 mm brown nodule on her lower leg. She thinks it appeared after an insect bite two years ago. Squeezing it laterally makes it retract beneath the surface. Which is the most likely diagnosis?",
   opts=[
     ["Dermatofibroma",
      "Correct — the dimple sign, on the commonest site, after a bite."],
     ["Cutaneous melanoma",
      "That is in the differential, but the dimple sign points away from it."],
     ["Keloid",
      "A keloid extends beyond a wound margin and is a fibroproliferative scar."],
     ["Epidermoid cyst",
      "That is movable with a central punctum, and does not dimple."]],
   c=0, cite=c(45)),

 dict(topic="Dermatofibroma", io=IOA, lead="test",
   q="Dermoscopy is performed on that patient's leg lesion. Which finding would support the diagnosis?",
   opts=[
     ["A peripheral pigment network with a central white mass",
      "Correct — the white centre corresponds to the fibrous core."],
     ["A moth-eaten border with uniform pigment throughout",
      "That is the solar lentigo pattern."],
     ["An epithelial collarette at the base of the lesion",
      "That is a clinical finding in pyogenic granuloma."],
     ["A central keratin-filled crater within a smooth dome",
      "That is keratoacanthoma seen clinically."]],
   c=0, cite=c(46)),

 dict(topic="Dermatofibroma", io=IOA, lead="treatment",
   q="The same patient is not bothered by her lesion but wants to know her options. Which is the most appropriate answer?",
   opts=[
     ["No treatment is needed; a shave or punch biopsy would remove it",
      "Correct — in a small lesion that biopsy is both diagnostic and therapeutic. Larger lesions may need surgical excision instead."],
     ["Wide local excision is required in every case because of melanoma risk",
      "Observation is acceptable when the diagnosis is not in doubt."],
     ["Intralesional corticosteroid will flatten it over several months",
      "That is a scar treatment."],
     ["Cryotherapy is the treatment of choice for pigmented dermal nodules",
      "Cryotherapy is not what is described for this lesion."]],
   c=0, cite=c(47)),

 dict(topic="Keratoacanthoma", io=IOA, lead="diagnosis",
   q="A 67-year-old man with very fair skin has a lesion on his forearm that appeared six weeks ago and grew fast. It is a solitary smooth dome-shaped red nodule with a central keratin-filled crater. Which is the most likely diagnosis?",
   opts=[
     ["Keratoacanthoma",
      "Correct — rapid growth and the volcano-like central crater."],
     ["Dermatofibroma",
      "That is a firm brown nodule with a dimple sign, usually on a leg."],
     ["Epidermoid cyst",
      "That has a central punctum and expresses pasty material, and does not grow this fast."],
     ["Pyogenic granuloma",
      "That is a moist bright red exophytic lesion that bleeds, without a keratin crater."]],
   c=0, cite=c(50)),

 dict(topic="Keratoacanthoma", io=IOA, lead="next step",
   q="The patient asks whether you can simply watch that lesion, since he has read they go away. Which is the most appropriate next step?",
   opts=[
     ["Excise or destroy it, because of possible malignancy",
      "Correct — strong arguments support classifying keratoacanthoma as a variant of invasive squamous cell carcinoma, so the standard of care is not observation."],
     ["Observe for three to six months, since regression is the natural history",
      "Regression does occur, but the possibility of malignancy overrides it."],
     ["Take a dermoscopy image and review in three months",
      "Dermoscopy does not settle this diagnosis."],
     ["Apply a topical keratolytic to flatten the crater",
      "Keratolytics have no role here."]],
   c=0, cite=c(52)),

 dict(topic="Keratoacanthoma", io=IOA, lead="treatment",
   q="A 58-year-old woman is to have a keratoacanthoma excised from her forearm. Which margin does the lecture specify?",
   opts=[
     ["Five millimetres",
      "Correct — with Mohs surgery for large, recurrent or cosmetically sensitive lesions."],
     ["One millimetre",
      "That margin is not what is specified for this lesion."],
     ["Ten millimetres",
      "The stated margin is smaller than this."],
     ["Two centimetres",
      "That is far wider than the margin given."]],
   c=0, cite=c(52)),

 dict(topic="Keratoacanthoma", io=IOA, lead="treatment",
   q="A 74-year-old man has a large keratoacanthoma on the nasal tip. Which approach does the lecture indicate?",
   opts=[
     ["Mohs surgery",
      "Correct — it is indicated for large or recurrent lesions, and for lesions in anatomic areas with cosmetic or functional considerations. This lesion is both."],
     ["Standard elliptical excision with five-millimetre margins regardless of site",
      "The site is precisely why Mohs is preferred here."],
     ["Cryotherapy, which spares the nasal cartilage",
      "Cryotherapy is not offered for this lesion."],
     ["Intralesional methotrexate as definitive treatment",
      "Methotrexate is used before excision to shrink the lesion."]],
   c=0, cite=c(52)),

 dict(topic="Epidermoid cyst", io=IOA, lead="diagnosis",
   q="A 45-year-old man has a firm, movable, round nodule on his upper back. There is a small central pore, and pressing it expresses cream-coloured pasty material with an unpleasant smell. Which is the most likely diagnosis?",
   opts=[
     ["Epidermoid cyst",
      "Correct — the central punctum and the odour of the keratin contents."],
     ["Lipoma",
      "A lipoma is soft and rubbery with no overlying pore."],
     ["Dermatofibroma",
      "That is firm and dimples on lateral compression, without a punctum."],
     ["Pilonidal cyst",
      "That sits over the coccyx with sinus openings in the natal cleft."]],
   c=0, cite=c(54)),

 dict(topic="Epidermoid cyst", io=IOA, lead="education",
   q="The patient asks whether his lesion is a sebaceous cyst full of oil. Which is the most appropriate response?",
   opts=[
     ["The contents are keratin, not sebum",
      "Correct — it is often called a sebaceous cyst because the material looks like sebum, but the deck states outright that it is not one."],
     ["Yes, it is a blocked sebaceous gland filled with sebum",
      "This is the misconception the lecture exists to correct."],
     ["It is a collection of lipid-laden macrophages",
      "That is xanthelasma."],
     ["It is mucin extruded from a nearby joint",
      "That is the digital mucous cyst."]],
   c=0, cite=c(53)),

 dict(topic="Epidermoid cyst", io=IOA, lead="next step",
   q="A patient's epidermoid cyst is red, hot and tender. Which is the most appropriate next step?",
   opts=[
     ["Postpone excision and settle the inflammation first",
      "Correct — reduce it with an intralesional injection of triamcinolone, add antibiotics if needed, and operate a few weeks later when the cyst is quiet."],
     ["Excise it today, including the entire capsule",
      "Excision is delayed until the inflammation has settled."],
     ["Incise and drain it, and take no further action",
      "Drainage leaves the capsule, which is the part that matters."],
     ["Biopsy it to exclude basal cell carcinoma",
      "Biopsy is not required for this diagnosis."]],
   c=0, cite=c(56)),

 dict(topic="Epidermoid cyst", io=IOA, lead="treatment",
   q="Six weeks later the cyst is quiet and the patient wants it gone permanently. Which is the most appropriate management?",
   opts=[
     ["Surgical removal of the entire capsule",
      "Correct — a small cyst of one to three centimetres can instead be punched and emptied."],
     ["Aspiration of the contents with a wide-bore needle",
      "Aspiration leaves the capsule behind."],
     ["Repeated intralesional steroid until it disappears",
      "Steroid settles inflammation; it does not remove the cyst."],
     ["Cryotherapy to the overlying skin",
      "Cryotherapy does not remove a dermal cyst."]],
   c=0, cite=c(57)),

 dict(topic="Syringoma", io=IOA, lead="diagnosis",
   q="A 17-year-old girl has multiple 1 to 2 mm skin-coloured papules symmetrically distributed on both lower eyelids and upper cheeks. They are asymptomatic and appeared around puberty. Which is the most likely diagnosis?",
   opts=[
     ["Syringoma",
      "Correct — benign eccrine duct neoplasms, appearing at puberty, females more than males."],
     ["Xanthelasma",
      "Those are soft yellow cholesterol plaques on the medial eyelids."],
     ["Milia",
      "Those are in the differential but are keratin cysts rather than duct neoplasms."],
     ["Sebaceous hyperplasia",
      "Those are whitish-yellow with a central umbilication, usually in older adults."]],
   c=0, cite=c(58)),

 dict(topic="Syringoma", io=IOA, lead="education",
   q="The same patient asks about having them removed. Which is the most appropriate counselling point?",
   opts=[
     ["Treatment is for cosmesis only, and every option has a trade-off",
      "Correct — drugs such as oral isotretinoin carry an increased risk of recurrence, and removal procedures carry a risk of poor cosmetic results."],
     ["The lesions must be removed because they can become malignant",
      "Syringomas are benign neoplasms of eccrine ducts."],
     ["The lesions will resolve on their own within a year",
      "They do not spontaneously resolve."],
     ["Removal is curative and recurrence does not occur",
      "Recurrence risk is explicitly part of the counselling."]],
   c=0, cite=c(59)),
]
