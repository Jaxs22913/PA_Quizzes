#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Lecture 9 (Pre-Malignant and Malignant Cutaneous Lesions) deck.

One deck for one topic, joining the CMS Exam 1 group LAST, since Lecture 9 is
the final derm lecture.

Cards are single atomic facts for Sprint's eight-second clock. matchCards are
recognition pairs -- and this deck is the hardest one yet to write pairs for,
because so much of the lecture is a NUMBER attached to a drug or a margin.
Those go in cards, not matchCards: a nine-word definition cannot make
"nicotinamide 500 mg twice daily" discriminable from the other nicotinamide
fact. The pairs kept are the ones where a description picks out exactly one
disease.

Arcade has no image support, so the three picture-only slides (Clark levels,
Stages, TNM) are carried as text cards here -- the same facts the guide's
section 9.5 and the cram sheet spell out.

Everything is from the PowerPoint, not the lecture audio.
"""
import json, os, re, sys

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
# a lesion under a dermatoscope's ring light, with an eye-catching irregular border
ICON = ('<circle cx="12" cy="12" r="9"/>'
        '<path d="M9.2 9.4c1.6-1.5 4-1.3 5.2.4 1 1.5.3 3.6-1.4 4.4-1.9.9-4.2-.2-4.5-2"/>')

DECKS = [
 dict(id="cms-malignant-lesions", name="Pre-Malignant & Malignant Lesions", color="accent1",
      icon=ICON, cards=[
  # --- actinic keratosis
  ["Is an actinic keratosis a separate entity from skin cancer?", "No. It is premalignant and on a biologic continuum with keratinocyte carcinoma."],
  ["What does an actinic keratosis feel like?", "Sandpaper. It may be more apparent by touch than by sight."],
  ["How large is a typical actinic keratosis?", "Zero point two to zero point six centimetres."],
  ["What proportion of actinic keratoses progress to squamous cell carcinoma?", "About one in a thousand lesions per year."],
  ["Which risk matters more, the single lesion or the field?", "Cumulative field risk. Individual lesion progression is hard to predict."],
  ["What is the lesion-directed treatment for a few discrete actinic keratoses?", "Liquid nitrogen cryotherapy."],
  ["How long does a cryotherapy-treated actinic keratosis take to crust and disappear?", "Ten to fourteen days."],
  ["Name the field-directed treatments for actinic keratosis.", "Topical fluorouracil, imiquimod and photodynamic therapy."],
  ["Which four features make an actinic keratosis atypical enough to biopsy?", "Bleeding, induration, ulceration or rapid enlargement."],
  ["Does treating actinic keratoses end the surveillance?", "No. The surrounding field remains at risk."],
  # --- squamous cell carcinoma
  ["Which sun-exposure pattern drives squamous cell carcinoma?", "Prolonged cumulative exposure, unlike basal cell carcinoma's intense intermittent exposure."],
  ["Describe the classic squamous cell carcinoma.", "A small red conical hard nodule that may ulcerate."],
  ["Which sites are high risk for squamous cell carcinoma?", "Mucosal surfaces, lip, ear, scalp, temple, nose and genitalia."],
  ["How many squamous cell carcinomas predict higher recurrence and nodal spread?", "More than ten tumours."],
  ["How soon after transplant do multiple squamous cell carcinomas typically appear?", "At about five years."],
  ["Which chemopreventive agent reduces new squamous cell carcinoma, and by how much?", "Nicotinamide, five hundred milligrams twice daily, by about thirty per cent."],
  ["How is in situ squamous cell carcinoma without high-risk features treated?", "Imiquimod, topical fluorouracil, or curettage and electrodesiccation."],
  ["How is invasive squamous cell carcinoma treated?", "Surgical excision or Mohs micrographic surgery."],
  ["What treats advanced or metastatic squamous cell carcinoma?", "Programmed death one blockade, and cetuximab."],
  ["Which tumour sizes meet the Mohs threshold?", "Over one centimetre on the face, or over two centimetres on trunk or extremities."],
  ["What must the follow-up examination include besides the skin?", "The lymph nodes, at least annually."],
  ["What is the metastatic rate of actinically induced squamous cell carcinoma?", "Three to seven per cent."],
  # --- basal cell carcinoma
  ["What is the most common form of cancer?", "Basal cell carcinoma."],
  ["What determines basal cell carcinoma's behaviour and treatment?", "The histologic subtype, not the clinical appearance."],
  ["How do you accentuate the telangiectasias of a nodular basal cell carcinoma?", "Stretch the skin."],
  ["Where does superficial basal cell carcinoma occur?", "The back or chest."],
  ["Which basal cell carcinoma subtype looks scar-like or ivory-white?", "The morpheaform or sclerosing subtype."],
  ["Which subtype carries the highest risk of subclinical spread?", "Morpheaform, which extends beyond the visible pink segment."],
  ["Which subtype can mimic melanocytic disease?", "Pigmented basal cell carcinoma. The pearly border and slow growth discriminate."],
  ["How often does a second basal cell carcinoma develop?", "In up to fifty per cent of patients."],
  ["By how much does nicotinamide reduce basal cell carcinoma?", "About twenty per cent, on five hundred milligrams twice daily."],
  ["What is the Mohs cure rate for basal cell carcinoma?", "About ninety-eight per cent."],
  ["What is the recurrence rate after excision of basal cell carcinoma?", "Five per cent or less."],
  ["How is imiquimod dosed for selected superficial basal cell carcinoma?", "Five nights weekly for six to ten weeks."],
  ["How is fluorouracil dosed for selected superficial basal cell carcinoma?", "Twice daily for up to twelve weeks."],
  ["Which drugs treat advanced or metastatic basal cell carcinoma?", "Hedgehog pathway inhibitors: vismodegib and sonidegib."],
  ["What causes basal cell carcinoma's morbidity?", "Local destruction, recurrence, delayed diagnosis and complex sites, rather than spread."],
  # --- melanoma
  ["Where does melanoma rank among cancers in the United States?", "Fourth most common, and the leading cause of death due to skin disease."],
  ["How many people die of melanoma each year in the United States?", "About seven thousand nine hundred and ninety, roughly two-thirds of them men."],
  ["What is the lifetime melanoma risk in white individuals?", "About two per cent."],
  ["What is the lifetime melanoma risk in persons of colour?", "Zero point one to zero point five per cent. Low, but not zero."],
  ["Which melanoma subtype accounts for about two-thirds of cases?", "Superficial spreading melanoma."],
  ["Which melanoma subtype arises on chronically sun-exposed skin of older adults?", "Lentigo maligna melanoma."],
  ["Why is nodular melanoma high risk?", "It grows rapidly, is often amelanotic, and may lack the classic features."],
  ["Where does acral lentiginous melanoma arise?", "Palms, soles and nail units."],
  ["What does the D in ABCDE stand for, and what is its caveat?", "Diameter over six millimetres, though smaller lesions can still be melanoma."],
  ["Slide 50's level I of invasion (the Clark level) means what?", "Confined to the epidermis."],
  ["Level IV of invasion means what?", "Invasion into the reticular dermis."],
  ["Level V of invasion means what?", "Invasion into the subcutaneous tissue."],
  ["What is the difference between the level of invasion and Breslow thickness?", "The level is an anatomic layer; Breslow is a measurement, and Breslow dominates prognosis."],
  ["When must Breslow thickness be measured accurately?", "At the initial biopsy."],
  ["Which two histologic features further modify stage-based melanoma prognosis?", "Ulceration and mitotic activity."],
  ["What defines stage three melanoma?", "Spread to lymph nodes."],
  ["What defines stage four melanoma?", "Spread to other organs."],
  ["What do T, N and M measure in melanoma staging?", "Tumour thickness, number of involved regional nodes, and number of distant metastases."],
  ["At what Breslow thickness is sentinel lymph node biopsy offered?", "One millimetre or greater."],
  ["When is sentinel node biopsy offered below one millimetre?", "At zero point eight millimetres with ulceration, high mitotic rate or lymphovascular invasion."],
  ["What must a patient be told about sentinel lymph node biopsy?", "It is a staging procedure and may not itself improve overall survival."],
  ["What is the re-excision margin for melanoma in situ?", "Zero point five to one centimetre."],
  ["What is the re-excision margin for melanoma under one millimetre thick?", "One centimetre."],
  ["What is the re-excision margin for melanoma over one millimetre thick?", "One to two centimetres."],
  ["Which melanomas go to an expert centre?", "Those deeper than one millimetre, or with lymph-node or other-site spread."],
  ["Which sites must patients include in monthly self-examination?", "Scalp, back, palms, soles and nails."],
  # --- Kaposi sarcoma and cutaneous T-cell lymphoma
  ["What causes Kaposi sarcoma?", "Human herpesvirus eight combined with a weakened immune system."],
  ["Which cells does Kaposi sarcoma arise from?", "The cells lining blood and lymph vessels."],
  ["Which Kaposi sarcoma form affects older men and is rarely fatal?", "Classic Kaposi sarcoma."],
  ["Which Kaposi sarcoma form can be rapidly fatal?", "Endemic, in young Black men in equatorial Africa."],
  ["What is the first move in epidemic Kaposi sarcoma?", "Begin or optimise antiretroviral therapy. Immune restoration is the cornerstone."],
  ["What is the first move in iatrogenic Kaposi sarcoma?", "Reduce immunosuppressive doses where feasible, coordinating with the transplant team first."],
  ["Why is oral examination essential in suspected Kaposi sarcoma?", "Hard-palate lesions are common and may be the presenting site."],
  ["Can Kaposi sarcoma cause oedema without visible skin lesions?", "Yes. Marked oedema may occur with few or none."],
  ["What is first-line systemic therapy for Kaposi sarcoma?", "Liposomal doxorubicin and paclitaxel."],
  ["Is antiretroviral therapy alone enough in advanced Kaposi sarcoma?", "No. Antiretroviral therapy plus chemotherapy is more effective."],
  ["How long can cutaneous T-cell lymphoma stay confined to the skin?", "Years or decades."],
  ["What does early cutaneous T-cell lymphoma resemble?", "Psoriasis, eczema or tinea, which is why it is diagnosed late."],
  ["Which two clues point to cutaneous T-cell lymphoma?", "Itch out of proportion to inflammation, and follicular involvement with hair loss."],
  ["Does early aggressive treatment cure cutaneous T-cell lymphoma?", "No. It has not been proven to cure disease or prevent progression."],
  ["What is the harm of overly aggressive cutaneous T-cell lymphoma therapy?", "Complications and premature death."],
  ["Name the skin-directed treatments for early cutaneous T-cell lymphoma.", "Topical corticosteroids, topical mechlorethamine, bexarotene gel and ultraviolet phototherapy."],
  # --- nail unit
  ["Which part of the nail does nail unit melanoma most often arise from?", "The matrix."],
  ["Is nail unit melanoma driven by ultraviolet light?", "Not clearly. It occurs in any skin tone."],
  ["Which digits does nail unit melanoma favour?", "The thumb and the great toe."],
  ["Which band shape suggests nail unit melanoma?", "Proximal widening, giving a triangular shape."],
  ["What is the Hutchinson sign of the nail?", "Periungual pigment extending onto the proximal nail fold."],
  ["What does a Hutchinson sign warrant?", "Urgent expert evaluation, regardless of other features."],
  ["Does absent pigment exclude nail melanoma?", "No. Amelanotic nail melanoma may be red, pink, eroded or mass-like."],
  ["What is the most common malignant nail tumour?", "Nail unit squamous cell carcinoma."],
  ["What is nail unit squamous cell carcinoma repeatedly mistaken for?", "A wart, paronychia or fungal infection."],
  ["Which triad suggests a glomus tumour?", "Severe paroxysmal pain, exquisite point tenderness and cold sensitivity."],
  ["Does the glomus triad replace imaging?", "No. It suggests the diagnosis but does not replace imaging or specialist evaluation."],
  ["What must you do before examining the nails?", "Remove the polish, then examine every nail, periungual skin, palms, soles and nodes."],
  ["Is amputation the standard treatment for nail unit melanoma?", "No. Digit-sparing wide excision or Mohs is contemporary care."],
  ["When is amputation reserved for nail unit tumours?", "For deep, extensive or bone-involving disease."],
  # --- approach and populations
  ["Which two examination steps are most often skipped?", "The oral cavity, and chronic scars or old radiation fields."],
  ["Why examine chronic scars and radiation sites?", "Squamous cell carcinoma arises in them."],
  ["How does immunosuppression change every answer?", "More disease, more aggressive disease, lower biopsy and Mohs thresholds, earlier referral."],
  ["Which therapy approach suits the elderly with heavy actinic damage?", "Field-directed therapy, because field cancerization rises with cumulative exposure."],
 ],
      matchCards=[
  ["Sandpaper texture, felt before seen", "Actinic keratosis"],
  ["Red conical hard nodule that ulcerates", "Squamous cell carcinoma"],
  ["Pearly papule, telangiectasias on stretching", "Nodular basal cell carcinoma"],
  ["Scar-like, ivory-white, spreads unseen", "Morpheaform basal cell carcinoma"],
  ["Reddish shiny scaly plaque on the back", "Superficial basal cell carcinoma"],
  ["Rapid, often amelanotic, lacks the classics", "Nodular melanoma"],
  ["Palms, soles and nail units", "Acral lentiginous melanoma"],
  ["Purple lesions on the hard palate", "Kaposi sarcoma"],
  ["Itch out of proportion, follicular hair loss", "Cutaneous T-cell lymphoma"],
  ["Pigment onto the proximal nail fold", "Hutchinson sign"],
  ["Chronic single-nail verrucous plaque", "Nail unit squamous cell carcinoma"],
  ["Paroxysmal pain, cold sensitivity, normal nail", "Glomus tumour"],
  ["Invasion into the subcutaneous tissue", "Level V of invasion"],
  ["Cumulative exposure, not intermittent", "Squamous cell carcinoma risk"],
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
if "cms-malignant-lesions" in s:
    sys.exit("deck already present -- nothing to do")

for d in DECKS:
    assert 8 <= len(d["cards"])
    assert 10 <= len(d["matchCards"]) <= 14, "%s: matchCards outside target" % d["id"]
    for front, back in d["cards"]:
        assert len(back.split()) <= 26, "card back too long -> %s" % back
    for term, definition in d["matchCards"]:
        assert len(definition.split()) <= 9, "match definition too long -> %s" % definition
    for coll, i in (("cards", 0), ("cards", 1), ("matchCards", 0), ("matchCards", 1)):
        vals = [x[i] for x in d[coll]]
        assert len(vals) == len(set(vals)), "duplicate in %s[%d] of %s" % (coll, i, d["id"])
    # Match is scored by picking ONE right answer, so two prompts that both
    # legitimately describe the same disease make a solvable board unsolvable.
    backs = [b for _, b in d["matchCards"]]
    assert len(backs) == len(set(backs)), "two match prompts share an answer in %s" % d["id"]

m = re.search(r"\n\];\n", s[s.index("var DEMO_DECKS"):])
end = s.index("var DEMO_DECKS") + m.start() + 1
s = s[:end] + "".join(js_deck(d) for d in DECKS) + s[end:]

# syllabus order: Lecture 9 is the last derm lecture, so it goes at the end
OLD = '"cms-benign-lesions", "cms-pigmented-lesions"'
NEW = '"cms-benign-lesions", "cms-pigmented-lesions", "cms-malignant-lesions"'
assert s.count(OLD) == 1, "CMS exam group not found exactly once"
s = s.replace(OLD, NEW)

open(ARCADE, "w", encoding="utf-8").write(s)
print("added %d deck(s): %d cards, %d match pairs"
      % (len(DECKS), sum(len(d["cards"]) for d in DECKS), sum(len(d["matchCards"]) for d in DECKS)))
