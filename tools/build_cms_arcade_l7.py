#!/usr/bin/env python3
"""Add the CMS I Lecture 7 (Benign Skin Lesions) Arcade deck to arcade.js.

One deck for one topic, joining the existing CMS Exam 1 group in syllabus order
-- before pigmented lesions, since Lecture 7 precedes Lecture 8.

Cards are single atomic facts for Sprint's eight-second clock; matchCards are
recognition pairs with compressed identity tags. Nothing here needs a picture,
which matters because Arcade has no image support -- the recognition work lives
in the guide's photograph strips and the comparison chart.
"""
import json, os, re, sys

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
# a magnifier over a small lesion
ICON = ('<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.2 15.2 21 21"/>'
        '<circle cx="10.5" cy="10.5" r="2"/>')

DECKS = [
 dict(id="cms-benign-lesions", name="Benign Skin Lesions", color="accent3",
      icon=ICON, cards=[
  ["What creates a corn, and what is at its centre?", "Focal mechanical trauma, creating a cone-shaped central core of hard keratin."],
  ["Which pressure reproduces the pain of a corn?", "Direct downward pressure."],
  ["Which pressure reproduces the pain of a wart?", "Side pressure."],
  ["Do the skin lines run through a corn or stop at it?", "They run through. A wart interrupts them."],
  ["Where does a hard corn sit?", "The dorsal and lateral aspect of the fifth toe."],
  ["Where does a soft corn sit, and why is it soft?", "The fourth-to-fifth toe web space, macerated by moisture."],
  ["How does a callus differ from a corn?", "Broad-area pressure, diffuse thickening, no central core, larger and irregular, usually painless."],
  ["Which keratolytic agent is in every over-the-counter corn product?", "Salicylic acid, between about twelve and forty per cent."],
  ["Which patient with a corn needs referral, and to whom?", "The diabetic patient, to podiatry."],
  ["Name the four phases of wound healing in order.", "Hemostasis, inflammation, proliferation, remodeling."],
  ["Why does a maturing scar gain tensile strength?", "Progressive cross-linking of collagen fibers."],
  ["What single feature defines a keloid?", "It extends beyond the margins of the original wound."],
  ["What single feature defines a hypertrophic scar?", "It stays confined within the wound margins."],
  ["How soon does a hypertrophic scar develop?", "Within four weeks of the event, soon after surgery."],
  ["When may a keloid appear after the trauma?", "Months afterwards; it then enlarges for months to years."],
  ["Which of the two regresses with time?", "The hypertrophic scar. A keloid rarely improves."],
  ["Where do keloids occur predominantly?", "Ear lobe, shoulders and sternal notch; they rarely develop across joints."],
  ["Where do hypertrophic scars characteristically occur?", "Where scars cross joints or skin creases at a right angle."],
  ["Which scar is associated with dark skin colour?", "The keloid. The hypertrophic scar has no such association."],
  ["Which scar improves with appropriate surgery?", "The hypertrophic scar. Keloids are often worsened by surgery."],
  ["Which populations are at risk for keloids?", "African American, Hispanic and Asian patients."],
  ["What is the most important keloid treatment?", "Prevention, including avoiding cosmetic procedures such as ear piercing."],
  ["What is the recurrence rate after excising a keloid alone?", "Fifty to one hundred per cent, and often larger than the original."],
  ["What must follow surgical excision of a keloid?", "Intralesional steroid injection."],
  ["How long are silicone gel sheets worn for a keloid?", "Twelve to twenty-four hours a day, for up to a year."],
  ["What pressure and duration are used for keloid compression therapy?", "Twenty-five millimetres of mercury, twenty-four hours a day, for six to twelve months."],
  ["When is radiation used for a keloid?", "In the first two weeks after the keloid has been excised."],
  ["What side effect does cryotherapy of a keloid cause?", "Hypopigmentation."],
  ["What side effect can intralesional steroid cause?", "Tissue atrophy."],
  ["How does intralesional fluorouracil work in a keloid?", "It is an antimetabolite that inhibits fibroblast proliferation."],
  ["Why is biopsy of a keloid discouraged?", "It may induce new scarring."],
  ["What is a cutaneous horn made of?", "Keratin, in a hard conical outward projection."],
  ["What is the most important thing about a cutaneous horn?", "The process at the base of the lesion, not the horn itself."],
  ["Which lesions can a cutaneous horn arise from?", "Actinic keratosis, warts, seborrheic keratosis, keratoacanthoma, and basal or squamous cell carcinoma."],
  ["How is the lesion under a cutaneous horn diagnosed?", "Deep shave biopsy, to sample the underlying tissue."],
  ["Who gets cutaneous horns?", "Caucasians over fifty, males equally with females, on head, neck and upper extremities."],
  ["What is an acrochordon, anatomically?", "A fibroepithelial pedunculated papilloma with a narrow stalk and a broad tip."],
  ["Where do skin tags form, and in whom?", "Friction sites such as neck, axilla and groin, increased in females and obese patients."],
  ["How common are skin tags by age seventy?", "Present in sixty per cent of people."],
  ["How are skin tags removed?", "Scissor excision, cryotherapy or electrodesiccation, with no anesthesia necessary."],
  ["Why should a patient never remove a skin tag at home?", "They bleed when they come off."],
  ["What causes a pressure injury?", "Unrelieved pressure, generally soft tissue compressed between a bony prominence and an external surface."],
  ["What defines a stage 1 pressure injury?", "A localised area of non-blanchable erythema of intact skin."],
  ["What defines a stage 2 pressure injury?", "Partial-thickness skin loss with exposed dermis; the bed is viable, pink or red."],
  ["What defines a stage 3 pressure injury?", "Full thickness skin loss with adipose tissue visible."],
  ["What defines a stage 4 pressure injury?", "Full thickness skin and tissue loss, with fascia, muscle, tendon, ligament, cartilage or bone exposed."],
  ["What makes a pressure injury unstageable?", "Full thickness loss obscured by slough or eschar, so the extent cannot be determined."],
  ["What defines a deep tissue pressure injury?", "Persistent non-blanchable deep red or purple discolouration; skin intact or not."],
  ["How often should an at-risk patient be repositioned?", "Every two hours."],
  ["What is the best measure against pressure injury?", "Prevention."],
  ["Why is debridement performed on a pressure wound?", "Necrotic tissue, eschar and slough promote infection, delay granulation and impede healing."],
  ["How does a pilonidal cyst form?", "A pit over the coccyx draws in hair and debris, causing follicular plugging and abscess formation."],
  ["What is the sex ratio for pilonidal disease?", "Male to female three to one."],
  ["Was pilonidal disease congenital or acquired?", "Originally thought congenital, now believed acquired."],
  ["Which risk factor for pilonidal disease is the distinctive one?", "Increased hair density in the natal cleft."],
  ["What is fluctuance?", "A wave-like movement or fluid shift on palpation, indicating the lesion is fluid filled."],
  ["What is the difference between a sinus and a fistula?", "A sinus is a blind track; a fistula connects two epithelium-lined surfaces."],
  ["How is an acute pilonidal abscess treated?", "Incision and drainage."],
  ["What diagnostic testing does pilonidal disease need?", "None usually."],
  ["What forms a dermatofibroma?", "Fibroblasts in the dermis forming small dense clusters."],
  ["What is the dimple sign?", "The lesion retracts beneath the skin surface with lateral compression."],
  ["Which is described as the most common painful skin tumour?", "Dermatofibroma."],
  ["Where do dermatofibromas most commonly sit?", "The legs, then the arms."],
  ["What does dermoscopy of a dermatofibroma show?", "A peripheral pigment network with a central white mass."],
  ["Where is a keratoacanthoma believed to arise from?", "The pilosebaceous unit."],
  ["What is keratoacanthoma's relationship to squamous cell carcinoma?", "It is argued to be a variant of invasive squamous cell carcinoma."],
  ["Describe the triphasic pattern of a keratoacanthoma.", "Rapid growth in six to eight weeks, stabilization, then regression after three to six months."],
  ["What does a keratoacanthoma look like?", "A smooth shiny dome-shaped red nodule with a central keratin-filled crater."],
  ["What is the only reliable way to diagnose a keratoacanthoma?", "Biopsy."],
  ["What margin is used to excise a keratoacanthoma?", "Five millimetres."],
  ["When is Mohs surgery used for a keratoacanthoma?", "Large or recurrent lesions, or areas with cosmetic or functional considerations."],
  ["Which unusual risk factors are named for keratoacanthoma?", "Tattoos with red ink, and skin trauma such as lasers, surgery or cryotherapy."],
  ["What is inside an epidermoid cyst?", "Keratin, not sebum. It is not a sebaceous cyst."],
  ["Which examination finding identifies an epidermoid cyst?", "A central pore or punctum communicating with the skin surface."],
  ["What do the contents of an epidermoid cyst smell of?", "Rancid cheese."],
  ["What should be done with an inflamed epidermoid cyst?", "Postpone excision, settle it with intralesional triamcinolone, and give antibiotics if needed."],
  ["What is the standard of care for removing an epidermoid cyst?", "Surgical removal of the entire capsule, when the cyst is not inflamed."],
  ["What is a syringoma?", "A benign neoplasm of eccrine ducts."],
  ["When do syringomas appear, and where?", "At puberty, on the eyelids and upper cheeks."],
  ["What drives an infantile hemangioma?", "Rapid proliferation of endothelial cells."],
  ["What is the earliest sign of an infantile hemangioma?", "Blanching of the skin, then fine telangiectasias, then a red or crimson macule."],
  ["By what ages do infantile hemangiomas involute?", "Fifty per cent by five, seventy by seven, ninety by nine."],
  ["Which type of infantile hemangioma is commonest?", "The superficial type, once called a strawberry hemangioma."],
  ["What is first line for an infantile hemangioma?", "Beta-blockers such as oral propranolol or topical timolol, and corticosteroids."],
  ["What are the indications to treat an infantile hemangioma?", "Cosmetic concern, functional involvement, deep ulceration, and infection."],
  ["Why does nevus flammeus never involute?", "There is dilation of dermal capillaries but no proliferation of endothelial cells."],
  ["How does nevus flammeus change over a lifetime?", "It grows with the child and becomes darker and thicker."],
  ["What makes a nevus flammeus darken temporarily?", "Crying, fever or overheating."],
  ["What is nevus simplex, and what does it do?", "A more superficial variant of nevus flammeus, the stork bite; it fades within a year."],
  ["What forms a cherry angioma?", "Proliferation of capillaries or venules; the cause is unknown."],
  ["What should a patient be told about cherry angiomas?", "New lesions will likely develop and there is no way to prevent them."],
  ["What is a telangiectasia?", "A permanently dilated capillary under one millimetre, which blanches."],
  ["What causes a spider angioma?", "Dilation of preexisting vessels in estrogen excess, or in cirrhosis and liver failure."],
  ["Where do spider angiomas sit in children versus adults?", "Hands and fingers in children; face, neck, upper trunk and arms in adults."],
  ["Why is pyogenic granuloma a misnomer?", "It is neither infectious nor granulomatous."],
  ["What does a pyogenic granuloma look like?", "A bright red exophytic papule with a moist surface and an epithelial collarette at its base."],
  ["Which treatment of pyogenic granuloma has the lowest recurrence?", "Surgical excision, though it has the highest rate of scarring."],
  ["What is the other name for neurofibromatosis?", "Von Recklinghausen disease."],
  ["Which gene and chromosome go with neurofibromatosis type 1?", "The NF1 gene on chromosome seventeen."],
  ["Name the four skin manifestations of neurofibromatosis type 1.", "Cafe au lait spots, cutaneous neurofibromas, intertriginous freckling, plexiform neurofibromas."],
  ["How many cafe au lait macules are diagnostic?", "Six or more, though the macules alone do not establish the diagnosis."],
  ["What size defines a cafe au lait spot?", "Over five millimetres prepubertal, over fifteen millimetres postpubertal."],
  ["What is Crowe's sign?", "Intertriginous freckling in the axillary and inguinal regions, with freckles under five millimetres."],
  ["How are neurofibromas managed?", "By surveillance, with a cutaneous examination at every visit."],
  ["What is xanthelasma made of?", "A collection of lipid-laden macrophages, forming soft yellow cholesterol plaques."],
  ["What must be screened for in a patient with xanthelasma?", "Hyperlipidemia, because it may signify increased risk of cardiac disease."],
  ["What is the most common soft tissue tumour?", "The lipoma."],
  ["Why is a digital mucous cyst called a pseudo-cyst?", "It has no cellular lining; the mucin only compacts the surrounding cells into something resembling a capsule."],
  ["What is a digital mucous cyst associated with, and where does it sit?", "Osteoarthritis, over the distal interphalangeal joint."],
  ["What happens to the sebaceous gland in sebaceous hyperplasia?", "Sebocyte turnover slows with age, crowding the cells and enlarging the gland."],
  ["Which group is high risk for sebaceous hyperplasia?", "The immunosuppressed."],
  ["What distinguishes sebaceous hyperplasia from basal cell carcinoma?", "Dermoscopy, with biopsy if concern remains."],
 ], matchCards=[
  ["Extends beyond the wound", "Keloid"],
  ["Confined to the wound", "Hypertrophic scar"],
  ["Dimple sign", "Dermatofibroma"],
  ["Central keratin crater", "Keratoacanthoma"],
  ["Central punctum, rancid cheese", "Epidermoid cyst"],
  ["Epithelial collarette, bleeds", "Pyogenic granuloma"],
  ["Proliferates then involutes", "Infantile hemangioma"],
  ["Present at birth, never involutes", "Nevus flammeus"],
  ["Blind-ending track", "Sinus"],
  ["Connects two lined surfaces", "Fistula"],
  ["Adipose tissue visible", "Stage 3 pressure injury"],
  ["Obscured by slough or eschar", "Unstageable pressure injury"],
  ["Yellow eyelid plaques", "Xanthelasma, check the lipids"],
  ["Six or more, over 5mm", "Cafe au lait spots"],
 ]),
]


def js_deck(d):
    def pairs(rows):
        return "\n".join('      [%s, %s],' % (json.dumps(a, ensure_ascii=False),
                                              json.dumps(b, ensure_ascii=False)) for a, b in rows)
    return ('  { id: %s, name: %s, color: %s,\n    icon: \'%s\',\n'
            '    cards: [\n%s\n    ],\n    matchCards: [\n%s\n    ] },\n') % (
        json.dumps(d["id"]), json.dumps(d["name"]), json.dumps(d["color"]),
        d["icon"], pairs(d["cards"]), pairs(d["matchCards"]))


s = open(ARCADE, encoding="utf-8").read()
if "cms-benign-lesions" in s:
    sys.exit("deck already present -- nothing to do")

for d in DECKS:
    assert 8 <= len(d["cards"])
    assert 10 <= len(d["matchCards"]) <= 14, "%s: matchCards outside target" % d["id"]
    for front, back in d["cards"]:
        assert len(back.split()) <= 26, "card back too long -> %s" % back
    for term, definition in d["matchCards"]:
        assert len(definition.split()) <= 9, "match definition too long -> %s" % definition
    for coll in (("cards", 0), ("cards", 1), ("matchCards", 0), ("matchCards", 1)):
        vals = [x[coll[1]] for x in d[coll[0]]]
        assert len(vals) == len(set(vals)), "duplicate in %s[%d] of %s" % (coll[0], coll[1], d["id"])

m = re.search(r"\n\];\n", s[s.index("var DEMO_DECKS"):])
end = s.index("var DEMO_DECKS") + m.start() + 1
s = s[:end] + "".join(js_deck(d) for d in DECKS) + s[end:]

# syllabus order: Lecture 7 comes before Lecture 8's pigmented lesions
OLD = '"cms-derm-infestations", "cms-pigmented-lesions"'
NEW = '"cms-derm-infestations", "cms-benign-lesions", "cms-pigmented-lesions"'
assert s.count(OLD) == 1, "CMS exam group not found exactly once"
s = s.replace(OLD, NEW)

open(ARCADE, "w", encoding="utf-8").write(s)
print("added %d deck(s): %d cards, %d match pairs"
      % (len(DECKS), sum(len(d["cards"]) for d in DECKS), sum(len(d["matchCards"]) for d in DECKS)))
