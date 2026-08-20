# CMS I Lecture 7 (Benign Skin Lesions) — SET 1 pool C.
# Dermatofibroma, keratoacanthoma, epidermoid cyst and syringoma.
#
# These four are the lecture's "benign lesion that must be told from a cancer"
# group: keratoacanthoma is argued to be a variant of invasive squamous cell
# carcinoma, dermatofibroma sits opposite basal cell carcinoma and melanoma, and
# syringoma opposite basal cell carcinoma. The questions keep that framing,
# because it is what makes these lesions examinable rather than trivia.
#
# Options drafted at MATCHED LENGTHS; the four-lesion differentials push the raw
# gameable rate up, so every distractor is given the same compound form as the
# answer beside it.
#
# Every question carries slot="..." per the fact-slot standard.
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "7. Benign Skin Lesions Prof Griffenkranz 8-25-2025-2.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis for benign skin lesions"
IOB = "Objective b — Identify medical strategies for common benign skin lesions in infants, adolescents, adults and the elderly"

POOL_C = [
 dict(topic="Dermatofibroma", io=IOA, slot="etiology",
   q="What forms a dermatofibroma, and what size nodule results?",
   opts=[
     ["Fibroblasts in the dermis forming small dense clusters, creating a firm nodule of about half a centimetre to one centimetre",
      "Correct — the legs are the commonest site, then the arms."],
     ["Endothelial cells proliferating rapidly in the dermis, creating a bright red papule that enlarges over months",
      "That is the superficial infantile hemangioma."],
     ["Epithelium enclosed within the dermis filling with keratin, creating a movable nodule with a central punctum",
      "That is the epidermoid cyst."],
     ["Eccrine duct cells proliferating near the surface, creating multiple papules of one to two millimetres",
      "That is syringoma."]],
   c=0, cite=c(44)),

 dict(topic="Dermatofibroma", io=IOA, slot="epidemiology",
   q="What is the sex ratio for dermatofibroma, and what may precede it?",
   opts=[
     ["Male to female one to two, in all races; it may follow trauma, viral infection or an insect bite",
      "Correct — the etiology is otherwise uncertain."],
     ["Male to female two to one, in all races; it arises from the pilosebaceous unit after sun exposure",
      "That is keratoacanthoma."],
     ["Male to female three to one, in Caucasians; it follows disruption of the skin over the coccyx",
      "That is the pilonidal cyst."],
     ["Female to male three to one, in Caucasians; it appears in the first weeks of life",
      "That is infantile hemangioma."]],
   c=0, cite=c(44)),

 dict(topic="Dermatofibroma", io=IOA, slot="manifestation",
   q="What is the dimple sign, and which lesion shows it?",
   opts=[
     ["The lesion retracts beneath the skin surface with lateral compression; dermatofibroma",
      "Correct — this is the physical sign the lecture asks about directly."],
     ["The lesion blanches completely under direct downward pressure; cherry angioma",
      "Blanching is a vascular finding rather than the dimple sign."],
     ["The lesion transmits a wave-like fluid shift on palpation; pilonidal abscess",
      "That is fluctuance, which indicates a fluid-filled lesion."],
     ["The lesion expresses pasty material through a central pore; epidermoid cyst",
      "That is the punctum and its contents, not a dimple."]],
   c=0, cite=c(45)),

 dict(topic="Dermatofibroma", io=IOA, slot="manifestation",
   q="What does a dermatofibroma look like, and what symptom is it noted for?",
   opts=[
     ["A firm nodule with a hyperpigmented brown halo, a pink hue, a raised centre and a scaly surface; the most common painful skin tumour",
      "Correct — although most are asymptomatic or only slightly pruritic."],
     ["A solitary smooth shiny dome-shaped red papule with a central keratin-filled crater resembling a volcano; painless throughout its course",
      "That is keratoacanthoma, which resembles a volcano."],
     ["A soft skin-coloured pedunculated papule on a narrow stalk with a broad tip; asymptomatic unless it is caught and torn",
      "That is the acrochordon."],
     ["A whitish-yellow soft papule of two to nine millimetres with a central umbilication from which sebum can be expressed; asymptomatic",
      "That is sebaceous hyperplasia."]],
   c=0, cite=c(45)),

 dict(topic="Dermatofibroma", io=IOA, slot="differential",
   q="What is the differential diagnosis for a dermatofibroma?",
   opts=[
     ["Basal cell carcinoma, hypertrophic scar, cutaneous melanoma and keratoacanthoma",
      "Correct — two of the four are malignancies, which is why it matters."],
     ["Squamous cell carcinoma, basal cell carcinoma, amelanotic melanoma and molluscum contagiosum",
      "That is the keratoacanthoma differential."],
     ["Cystic acne, lipoma, neurofibroma, keratoacanthoma and basal cell carcinoma",
      "That is the epidermoid cyst differential."],
     ["Milia, xanthelasma and basal cell carcinoma, all of which sit around the eye",
      "That is the syringoma differential."]],
   c=0, cite=c(46)),

 dict(topic="Dermatofibroma", io=IOA, slot="test finding",
   q="What does dermoscopy of a dermatofibroma often show?",
   opts=[
     ["A peripheral pigment network with a central white mass",
      "Correct — the central white area corresponds to the fibrous core."],
     ["A moth-eaten border with uniform pigment throughout",
      "That is the solar lentigo pattern from Lecture 3."],
     ["An epithelial collarette around a moist exophytic base",
      "That is the pyogenic granuloma's clinical, not dermoscopic, finding."],
     ["A central keratin-filled crater within a smooth dome",
      "That is keratoacanthoma seen clinically."]],
   c=0, cite=c(46)),

 dict(topic="Dermatofibroma", io=IOA, slot="first-line",
   q="How is a dermatofibroma managed?",
   opts=[
     ["Often no treatment at all; a small lesion takes a shave or punch biopsy, a larger one may need excision",
      "Correct — treat only if the diagnosis is questioned or symptoms warrant it. In a small lesion the biopsy is both diagnostic and therapeutic, doing two jobs at once."],
     ["Immediate wide local excision in every case, because a dermatofibroma cannot reliably be told from a cutaneous melanoma on clinical appearance alone",
      "The deck allows observation; excision is not mandatory."],
     ["Intralesional corticosteroid injection followed by silicone gel sheeting, on the basis that the lesion is a form of abnormal scarring",
      "Those are keloid and hypertrophic scar treatments."],
     ["Cryotherapy with liquid nitrogen repeated at monthly intervals until the hyperpigmented halo has resolved completely",
      "Cryotherapy is not the management described for this lesion."]],
   c=0, cite=c(47)),

 dict(topic="Keratoacanthoma", io=IOA, slot="etiology",
   q="Where is a keratoacanthoma believed to arise from, and what is its relationship to squamous cell carcinoma?",
   opts=[
     ["The pilosebaceous unit; it is argued to be a variant of invasive squamous cell carcinoma",
      "Correct — it is histopathologically similar to squamous cell carcinoma, and strong arguments support classifying it as a variant of the invasive form. That is why the standard of care is to excise or destroy it rather than watch it."],
     ["The eccrine sweat duct; it is histopathologically quite distinct from squamous cell carcinoma and carries no malignant potential at all",
      "That is closer to syringoma, and it understates the concern here."],
     ["The dermal fibroblast; it is histopathologically similar to a hypertrophic scar and does not ever behave in a malignant fashion",
      "That describes dermatofibroma."],
     ["The sebaceous gland; it is a crowding of sebocytes within an enlarged gland, with no known potential for malignant transformation",
      "That is sebaceous hyperplasia."]],
   c=0, cite=c(48)),

 dict(topic="Keratoacanthoma", io=IOA, slot="risk factors",
   q="Which risk factors are listed for keratoacanthoma?",
   opts=[
     ["Age over forty, sun exposure, very fair skin that always burns and never tans, male sex, tattoos with red ink, skin trauma such as lasers, surgery or cryotherapy, and human papillomavirus infection",
      "Correct — the red ink and the iatrogenic trauma are the unexpected ones."],
     ["Obesity, repeated local trauma or irritation, a sedentary lifestyle, increased hair density in the natal cleft, and a positive family history for the same lesion in a first-degree relative",
      "Those are the pilonidal cyst risk factors."],
     ["African American, Hispanic or Asian ancestry, together with any surgical incision, traumatic wound, burn, vaccination site, case of chickenpox, acne or even a minor scratch",
      "Those are the keloid risks."],
     ["Preterm birth, female sex, Caucasian ancestry, low birth weight, a multiple gestation birth, and a placental abnormality in the pregnancy",
      "Those are infantile hemangioma associations."]],
   c=0, cite=c(49)),

 dict(topic="Keratoacanthoma", io=IOA, slot="prognosis",
   q="What is the triphasic pattern of a keratoacanthoma?",
   opts=[
     ["Rapid growth within six to eight weeks, then stabilization, then regression after three to six months",
      "Correct — although it may continue growing or, rarely, metastasize."],
     ["Rapid proliferation for four to six months, then slowing between six and twelve months, then involution over years",
      "That is the infantile hemangioma's growth curve."],
     ["Slow development over months to years, with continued enlargement and no regression at all",
      "That is the keloid."],
     ["Appearance within four weeks of the injury, a period of stability, then flattening with time",
      "That is the hypertrophic scar."]],
   c=0, cite=c(50)),

 dict(topic="Keratoacanthoma", io=IOA, slot="manifestation",
   q="What does a keratoacanthoma look like?",
   opts=[
     ["A solitary smooth shiny dome-shaped red papule or nodule that develops a central keratin-filled crater, resembling a volcano",
      "Correct — the crater is the feature that names it."],
     ["A hard conical outward-growing projection composed entirely of keratin, with the appearance of an animal horn",
      "That is the cutaneous horn."],
     ["A firm nodule with a hyperpigmented brown halo, a pink hue and a raised scaly centre",
      "That is the dermatofibroma."],
     ["A bright red exophytic papule or nodule with a moist surface and an epithelial collarette around its base",
      "That is the pyogenic granuloma."]],
   c=0, cite=c(50)),

 dict(topic="Keratoacanthoma", io=IOA, slot="gold standard",
   q="What is the only reliable way to diagnose a keratoacanthoma?",
   opts=[
     ["Biopsy",
      "Correct — the clinical differential includes three malignancies."],
     ["Dermoscopy",
      "Dermoscopy is used for dermatofibroma and sebaceous hyperplasia here."],
     ["Clinical appearance alone",
      "The appearance overlaps too closely with squamous cell carcinoma."],
     ["Response to a trial of cryotherapy",
      "A therapeutic trial is not offered as a diagnostic method."]],
   c=0, cite=c(51)),

 dict(topic="Keratoacanthoma", io=IOA, slot="differential",
   q="What is the differential diagnosis for a keratoacanthoma?",
   opts=[
     ["Squamous cell carcinoma, basal cell carcinoma, amelanotic melanoma and molluscum contagiosum",
      "Correct — three malignancies and one infection."],
     ["Basal cell carcinoma, hypertrophic scar, cutaneous melanoma and keratoacanthoma itself",
      "That is the dermatofibroma differential."],
     ["Hypertrophic scar, dermatofibroma and foreign-body granuloma, all fibrous lesions",
      "That is the keloid differential."],
     ["Cherry angioma, malignant melanoma and squamous cell carcinoma, all raised red lesions",
      "That is the pyogenic granuloma differential."]],
   c=0, cite=c(51)),

 dict(topic="Keratoacanthoma", io=IOA, slot="first-line",
   q="What is the standard of care for a keratoacanthoma, and what margin is specified?",
   opts=[
     ["Excise or destroy the tumour, preferred because of possible malignancy; ellipse it out with five-millimetre margins",
      "Correct — Mohs surgery is reserved for large, recurrent or cosmetically sensitive lesions."],
     ["Observe it for three to six months, since the natural history is spontaneous regression in most cases",
      "The possibility of malignancy is exactly why observation is not the standard."],
     ["Shave or punch biopsy alone, which is both diagnostic and therapeutic in a lesion of this size",
      "That approach belongs to the small dermatofibroma."],
     ["Cryotherapy with liquid nitrogen, repeated until the central crater has flattened completely",
      "Cryotherapy is not the standard of care described."]],
   c=0, cite=c(52)),

 dict(topic="Keratoacanthoma", io=IOA, slot="escalation",
   q="When is Mohs surgery indicated for a keratoacanthoma?",
   opts=[
     ["For large or recurrent lesions, or lesions in areas with cosmetic or functional considerations",
      "Correct — otherwise standard elliptical excision is used."],
     ["For every lesion, because the recurrence rate after simple excision approaches one hundred per cent",
      "That recurrence figure belongs to keloid excision."],
     ["Only after intralesional methotrexate has failed to reduce the size of the lesion",
      "Methotrexate is used before excision to shrink a lesion, not as a gate to Mohs."],
     ["Only in immunosuppressed patients, in whom the lesion behaves more aggressively",
      "Immunosuppression is flagged for sebaceous hyperplasia rather than here."]],
   c=0, cite=c(52)),

 dict(topic="Keratoacanthoma", io=IOA, slot="agent/regimen",
   q="What is intralesional methotrexate used for in keratoacanthoma, and how does it work?",
   opts=[
     ["Given before excision to reduce the size of the lesion; it inhibits deoxyribonucleic acid synthesis in actively dividing cells",
      "Correct — a chemotherapeutic agent used as a surgical adjunct."],
     ["Given after excision in order to prevent recurrence; it inhibits fibroblast proliferation within the healing wound bed",
      "Fibroblast inhibition is fluorouracil's action in keloid."],
     ["Given instead of excision in frail patients; it induces microvascular thrombosis within the vessels feeding the lesion",
      "Microvascular thrombosis is a proposed laser mechanism."],
     ["Given topically over several months; it slows the turnover of sebocytes within the enlarged sebaceous gland",
      "No such agent or mechanism is described for this lesion."]],
   c=0, cite=c(52)),

 dict(topic="Epidermoid cyst", io=IOA, slot="etiology",
   q="What is inside an epidermoid cyst, and why is the common name wrong?",
   opts=[
     ["Keratin, from epithelium enclosed within the dermis; it is not a sebaceous cyst",
      "Correct — it is called a sebaceous cyst because the contents look like sebum, but the substance is keratin and the deck states outright that it is not one."],
     ["Sebum, from a sebaceous gland whose duct has become obstructed; the common name sebaceous cyst is therefore accurate",
      "This is the misconception the slide exists to correct."],
     ["Mucin, extruded from an adjacent joint space into the surrounding dermis, where it compacts the cells at its margin",
      "That is the digital mucous cyst."],
     ["Lipid-laden macrophages, collecting as soft yellow plaques beneath the thin skin of the medial eyelid",
      "That is xanthelasma."]],
   c=0, cite=c(53)),

 dict(topic="Epidermoid cyst", io=IOA, slot="epidemiology",
   q="Who gets epidermoid cysts, and where?",
   opts=[
     ["Males twice as often as females; very commonly, on the face, scalp, neck and trunk",
      "Correct — a very common lesion."],
     ["Females twice as often as males; on the legs and arms, in all races",
      "That is the dermatofibroma."],
     ["Females more than males, from puberty; on the eyelids and upper cheeks",
      "That is syringoma."],
     ["Males three times as often as females; over the coccyx and gluteal cleft",
      "That is the pilonidal cyst."]],
   c=0, cite=c(53)),

 dict(topic="Epidermoid cyst", io=IOA, slot="manifestation",
   q="What are the examination findings of an epidermoid cyst?",
   opts=[
     ["A single firm movable nodule with a central punctum, expressing pasty material that smells of rancid cheese",
      "Correct — a round protruding mass whose central pore communicates with the skin surface. The punctum and the smell of the cream-coloured contents are the two giveaways."],
     ["A soft painless subcutaneous nodule of rubbery consistency, usually under five centimetres across, with no overlying pore or punctum at all",
      "That is the lipoma."],
     ["A firm nodule with a hyperpigmented brown halo and a scaly surface, which retracts beneath the skin on lateral compression",
      "That is the dermatofibroma."],
     ["A translucent skin-coloured papule sitting over the distal interphalangeal joint, which may groove the nail longitudinally",
      "That is the digital mucous cyst."]],
   c=0, cite=c(54)),

 dict(topic="Epidermoid cyst", io=IOA, slot="initial test",
   q="What laboratory testing does an epidermoid cyst require?",
   opts=[
     ["Usually none",
      "Correct — the diagnosis is clinical."],
     ["Culture of the expressed material in every case",
      "Culture is not part of the routine diagnosis."],
     ["Fasting lipid panel to screen for a lipid disorder",
      "That screening follows xanthelasma."],
     ["Punch biopsy of the cyst wall before any excision",
      "Biopsy is not described as necessary here."]],
   c=0, cite=c(55)),

 dict(topic="Epidermoid cyst", io=IOA, slot="escalation",
   q="What should be done with an inflamed epidermoid cyst?",
   opts=[
     ["Postpone excision for a few weeks, reduce the inflammation with intralesional triamcinolone, and give antibiotics if needed",
      "Correct — surgery is done when the cyst is not inflamed."],
     ["Excise it immediately, on the basis that inflammation indicates the capsule has already ruptured into the surrounding dermis",
      "The deck advises delay rather than immediate surgery."],
     ["Incise and drain it, then pack the cavity and allow the wound to close slowly by secondary intention",
      "That is the management of a pilonidal abscess."],
     ["Leave it entirely alone, on the basis that an inflamed cyst always settles without any intervention at all",
      "Steroid and antibiotics are offered rather than pure observation."]],
   c=0, cite=c(56)),

 dict(topic="Epidermoid cyst", io=IOA, slot="first-line",
   q="What is the standard of care for removing an epidermoid cyst, and what is the option for a small one?",
   opts=[
     ["Removal of the entire capsule when the cyst is not inflamed; a small one can be punched and emptied",
      "Correct — the capsule is the part that matters, and removing all of it is the standard of care. A cyst of one to three centimetres can instead be treated with a punch incision and removal of the contents."],
     ["Simple drainage of the keratin contents through a stab incision, leaving the capsule in place to scar down on its own",
      "Leaving the capsule is what the standard of care avoids."],
     ["Elliptical excision with five-millimetre margins in every case, with the specimen sent for histopathological analysis",
      "Those margins belong to keratoacanthoma."],
     ["Scissor excision at the level of the stalk followed by electrodesiccation, with no local anesthesia required",
      "That is how skin tags are removed."]],
   c=0, cite=c(57)),

 dict(topic="Syringoma", io=IOA, slot="etiology",
   q="What is a syringoma, and when does it appear?",
   opts=[
     ["A benign neoplasm of eccrine ducts, appearing at puberty and more often in females",
      "Correct — eccrine, meaning sweat gland."],
     ["A benign neoplasm of endothelial cells, appearing in the first weeks of life and more often in females",
      "That is infantile hemangioma."],
     ["A benign nerve sheath tumour, appearing at puberty and increasing with age",
      "That is the cutaneous neurofibroma."],
     ["A benign enlargement of sebaceous glands, appearing with age and more often with immunosuppression",
      "That is sebaceous hyperplasia."]],
   c=0, cite=c(58)),

 dict(topic="Syringoma", io=IOA, slot="manifestation",
   q="What do syringomas look like, and where do they sit?",
   opts=[
     ["Multiple skin-coloured, pink or brown papules of one to two millimetres, most often on the eyelids and upper cheeks",
      "Correct — the periorbital location is the recognisable part."],
     ["Multiple whitish-yellow papules of two to nine millimetres with central umbilication, most often on the face",
      "That is sebaceous hyperplasia."],
     ["Soft yellow cholesterol plaques, most often on the medial eyelids",
      "That is xanthelasma, which shares the site but not the appearance."],
     ["Light tan to brown macules over five millimetres, appearing in the first year of life",
      "Those are café au lait spots."]],
   c=0, cite=c(58)),

 dict(topic="Syringoma", io=IOA, slot="differential",
   q="What is the differential diagnosis for syringoma?",
   opts=[
     ["Milia, xanthelasma and basal cell carcinoma",
      "Correct — all three can sit in the periorbital region."],
     ["Basal cell carcinoma, hypertrophic scar and cutaneous melanoma",
      "That is the dermatofibroma differential."],
     ["Cystic acne, lipoma and neurofibroma",
      "That is part of the epidermoid cyst differential."],
     ["Nevus flammeus and pyogenic granuloma",
      "That is the infantile hemangioma differential."]],
   c=0, cite=c(59)),

 dict(topic="Syringoma", io=IOA, slot="first-line",
   q="How is syringoma managed, and what is the trade-off?",
   opts=[
     ["For cosmesis only: drugs risk recurrence, and removal procedures risk a poor cosmetic result",
      "Correct — every option trades one against the other. The drug named is oral isotretinoin; the procedures are curettage and electrodesiccation, laser therapy, cryotherapy and surgical excision."],
     ["For cosmesis only: intralesional corticosteroid injection flattens the lesions reliably, with local tissue atrophy as the only meaningful risk",
      "Steroid injection is a scar treatment in this lecture."],
     ["Always excised surgically, because the lesions cannot be reliably distinguished from a basal cell carcinoma on clinical grounds",
      "Biopsy is reserved for when malignancy is a concern, not mandated."],
     ["Always simply observed, because the lesions resolve spontaneously within about a year of first appearing at puberty",
      "Syringomas do not spontaneously resolve."]],
   c=0, cite=c(59)),

 dict(topic="Syringoma", io=IOA, slot="initial test",
   q="How is syringoma diagnosed?",
   opts=[
     ["Usually clinically, with biopsy if there is concern about malignancy",
      "Correct — basal cell carcinoma is the concern in that region."],
     ["Always by biopsy, since the clinical appearance is entirely non-specific",
      "Biopsy is conditional rather than routine here."],
     ["By dermoscopy showing a peripheral pigment network with a central white mass",
      "That pattern belongs to dermatofibroma."],
     ["By fasting lipid panel, since the lesions signal a lipid disorder",
      "That association belongs to xanthelasma."]],
   c=0, cite=c(59)),
]
