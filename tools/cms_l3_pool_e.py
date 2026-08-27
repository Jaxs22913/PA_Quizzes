# CMS I Lecture 3 (Dermatology II) — SET 1 pool E: LECTURE EMPHASIS.
#
# Built from the 2026-08-19 recording (two segments, 10:48-11:50 and
# 13:02-13:19, 77.8 minutes). Every scope statement quoted below was confirmed
# by two independent transcriptions before being acted on.
#
# WHAT SHE SAID SHE WILL AND WILL NOT ASK:
#   - "I do want you to know what you need to ORDER... I don't necessarily need
#     you guys to be able to tell me what the biopsy looks like under the
#     microscope, unless I particularly point it out. You guys are not
#     pathologists." Histology descriptions are de-emphasised; test SELECTION
#     is not. The three existing histology questions stay -- they are grounded
#     in the slides and she allowed for exceptions -- but nothing new was added
#     in that direction, and the questions here are all about what to order.
#   - On the lupus butterfly rash against rosacea: "that's not going to be on
#     the test. I won't do that to you. I'm not testing for lupus right now."
#     So no question here asks the student to make that call. The ANA REASONING
#     she taught alongside it is fair game and is examined instead.
#   - The general rule she gave out loud: "If you think it's different from any
#     other disease, what's the likelihood it's going to be on the test?
#     Probably pretty high. There's not many I can do diagnostic testing on,
#     since they're all clinical. I'm looking for diagnostic testing, it's
#     likely going to be on the test."
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "3. Dermatology  II.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Etiologies, manifestations, diagnosis and management of dermatological conditions"

POOL_E = [
 dict(topic="Acne rosacea", io=IOA, slot="first-line",
   q="What is first-line treatment for acne rosacea?",
   opts=[
     ["Topical metronidazole",
      "Correct — she named it explicitly as first line."],
     ["Topical ivermectin cream",
      "That is superior where there is a demonstrated Demodex burden, after metronidazole."],
     ["Topical azelaic acid gel",
      "Effective, but more drying, which matters in already impaired skin."],
     ["Topical brimonidine gel",
      "That is an alpha-adrenergic agonist for erythema rather than first-line therapy."]],
   c=0, cite=c(69)),

 dict(topic="Acne rosacea", io=IOA, slot="avoid",
   q="Why does azelaic acid need care in rosacea despite being effective?",
   opts=[
     ["It is more drying, and these patients already have an impaired skin barrier and dry skin",
      "Correct — that is why metronidazole is preferred first."],
     ["It causes marked photosensitivity, so daily sun protection becomes mandatory",
      "Photosensitivity is not the caution given for this agent here."],
     ["It is contraindicated in pregnancy because of teratogenic risk",
      "That caution belongs to oral isotretinoin."],
     ["It raises intraocular pressure with prolonged facial application",
      "That caution belongs to topical corticosteroids."]],
   c=0, cite=c(69)),

 dict(topic="Acne rosacea", io=IOA, slot="initial test",
   q="A patient's facial erythema could be rosacea or lupus and the picture is unclear. Which test helps, and how should the result be read?",
   opts=[
     ["An antinuclear antibody, which helps rule autoimmune disease OUT — a positive result only means more testing is needed",
      "Correct — many things make it positive, so it cannot rule a condition in."],
     ["An antinuclear antibody, which rules autoimmune disease IN when positive and needs no further testing",
      "It cannot rule a condition in; a positive means more testing."],
     ["A skin biopsy of the malar area, which distinguishes the two definitively",
      "Histological distinction is not what she asks for here."],
     ["A potassium hydroxide preparation of the affected facial skin",
      "That would investigate a fungal cause."]],
   c=0, cite=c(69)),

 dict(topic="Dermatitis herpetiformis", io=IOA, slot="gold standard",
   q="Why is the diagnostic test for dermatitis herpetiformis worth knowing particularly well?",
   opts=[
     ["Because most conditions in this lecture are clinical diagnoses, so a disease with a distinctive test stands out",
      "Correct — she flagged this reasoning out loud while teaching it."],
     ["Because the condition is the most common one covered in the lecture",
      "It affects only 11 to 75 per 100,000 and is described as rare."],
     ["Because the test result changes nothing about the management",
      "The result drives a lifelong dietary change."],
     ["Because the diagnosis cannot be suspected on any clinical grounds at all before the testing is done",
      "The presentation is characteristic; the test confirms it."]],
   c=0, cite=c(125)),

 dict(topic="Dermatitis herpetiformis", io=IOA, slot="epidemiology",
   q="What is the incidence of dermatitis herpetiformis, and who does it affect?",
   opts=[
     ["11 to 75 per 100,000, most often people of northern European descent aged 30 to 40",
      "Correct — high dietary gluten intake and the HLA markers add to the risk."],
     ["1 to 7 per million per year, most often the immunosuppressed and those with malignancy",
      "Those are the figures and risk groups for Stevens-Johnson syndrome."],
     ["About 15 to 20% of the general population, most often young women in temperate climates",
      "That is polymorphous light eruption."],
     ["Over 90% of people by the age of fifty, most often those with fair skin",
      "That is solar lentigo."]],
   c=0, cite=c(17)),

 dict(topic="Dermatitis herpetiformis", io=IOA, slot="manifestation",
   q="Where is the eruption of dermatitis herpetiformis distributed?",
   opts=[
     ["Symmetrically on the knees, elbows, buttocks and back",
      "Correct — intensely pruritic papules and vesicles that group in a herpetiform pattern."],
     ["On the anterior shins bilaterally as tender nodules that do not ulcerate",
      "That is erythema nodosum."],
     ["On the face in the central third, sparing the nasolabial folds",
      "That is a lupus butterfly rash, which she said she is not testing."],
     ["On sun-exposed skin, sparing the chronically exposed face and hands",
      "That is polymorphous light eruption."]],
   c=0, cite=c(18)),

 dict(topic="Dermatitis herpetiformis", io=IOA, slot="complication",
   q="Which gastrointestinal symptoms commonly accompany dermatitis herpetiformis?",
   opts=[
     ["Bloating and diarrhoea, which can wax and wane in intensity",
      "Correct — the condition is linked to gluten sensitivity and coeliac disease."],
     ["Painless jaundice with pale stools and darkened urine",
      "That picture is unrelated to this condition."],
     ["Bloody diarrhoea with urgency and tenesmus",
      "That would suggest inflammatory bowel disease."],
     ["Vomiting and abdominal pain relieved by eating",
      "That picture is unrelated to this condition."]],
   c=0, cite=c(18)),

 dict(topic="Erythema multiforme", io=IOA, slot="initial test",
   q="Which tests should be ordered in erythema multiforme major where systemic involvement is a concern?",
   opts=[
     ["A complete blood count, comprehensive metabolic panel and liver function tests",
      "Correct — Mycoplasma serology is added where that trigger is suspected."],
     ["A perilesional biopsy for direct immunofluorescence and a serum ELISA",
      "Those investigate autoimmune blistering disease."],
     ["Twenty-four hour urine metanephrines and thyroid function tests",
      "Those investigate secondary hyperhidrosis."],
     ["A potassium hydroxide preparation and a fungal culture of the lesions",
      "Those investigate a fungal cause."]],
   c=0, cite=c(9)),

 dict(topic="Erythema multiforme", io=IOA, slot="test finding",
   q="Where do liver function tests sit in relation to the standard metabolic panels?",
   opts=[
     ["A comprehensive metabolic panel contains liver function tests; a basic metabolic panel does not",
      "Correct — separate liver function tests can be added if more detail is needed."],
     ["A basic metabolic panel contains liver function tests; a comprehensive panel does not",
      "That reverses the two panels."],
     ["Neither panel contains any liver function tests at all",
      "The comprehensive panel does."],
     ["Both panels contain identical liver function testing",
      "The basic panel does not include them."]],
   c=0, cite=c(9)),

 dict(topic="Stevens-Johnson syndrome", io=IOA, slot="epidemiology",
   q="How common is Stevens-Johnson syndrome, and why does that not reduce its importance?",
   opts=[
     ["1 to 7 per million per year — uncommon, but deadly, so it has to be known",
      "Correct — immunosuppression and malignancy are the more common risk factors."],
     ["1 to 7 per hundred per year — common enough to be seen regularly in practice",
      "That substantially overstates the incidence."],
     ["Over 90% of adults by age fifty — near-universal but almost always mild",
      "That is the prevalence figure for solar lentigo."],
     ["11 to 75 per 100,000 — rare and generally self-limiting without treatment",
      "Those are the figures for dermatitis herpetiformis."]],
   c=0, cite=c(79)),

 dict(topic="Stevens-Johnson syndrome", io=IOA, slot="manifestation",
   q="What precedes the rash in Stevens-Johnson syndrome, and by how long?",
   opts=[
     ["A prodrome of fever, malaise and upper respiratory symptoms, one to three days before",
      "Correct — the mucosal erosions and painful macules follow it."],
     ["A herald patch appearing one to two weeks before the rest of the eruption",
      "That is pityriasis rosea."],
     ["An aura of burning and stinging in the affected skin minutes before",
      "That is not the described prodrome."],
     ["A period of intense nocturnal itching four to six weeks before",
      "That is the timing of a first scabies infestation."]],
   c=0, cite=c(80)),

 dict(topic="Stevens-Johnson syndrome", io=IOA, slot="referral",
   q="Which services should a patient with Stevens-Johnson syndrome be under?",
   opts=[
     ["Intensive care or a burn unit, with dermatology involved",
      "Correct — nasogastric feeding is often needed because mucosal involvement prevents eating."],
     ["A general medical ward with dermatology review the following day",
      "That level of care is inadequate for this condition."],
     ["Outpatient dermatology with a review appointment in one week",
      "That level of care is inadequate for this condition."],
     ["Ambulatory wound care with daily dressing changes at home",
      "That level of care is inadequate for this condition."]],
   c=0, cite=c(83)),

 dict(topic="Stevens-Johnson syndrome", io=IOA, slot="agent/regimen",
   q="Why do many patients with Stevens-Johnson syndrome need nasogastric feeding?",
   opts=[
     ["Mucosal involvement stops them eating",
      "Correct — nutritional support is part of burn-unit care."],
     ["The systemic corticosteroid causes intractable nausea",
      "Steroid use is controversial and is not the reason given."],
     ["The airway must be protected during the acute phase",
      "Airway protection is a separate concern where bronchial involvement occurs."],
     ["Oral intake would dilute the intravenous immunoglobulin",
      "That is not a described reason."]],
   c=0, cite=c(83)),

 dict(topic="Pyoderma gangrenosum", io=IOA, slot="initial test",
   q="Why must malignancy and infection be excluded in a rapidly expanding ulcer before treating it as pyoderma gangrenosum?",
   opts=[
     ["Because the diagnosis is one of exclusion and the immunosuppression used would worsen an infection",
      "Correct — the question to answer is why this ulcer is suddenly expanding."],
     ["Because pyoderma gangrenosum is itself a premalignant condition",
      "It is a neutrophilic dermatosis rather than premalignant."],
     ["Because antibiotics would become the first-line treatment once an infection is confirmed",
      "The condition is not infectious; antibiotics treat a secondary infection only."],
     ["Because a biopsy cannot be taken once immunosuppression has started",
      "That is not the reason given."]],
   c=0, cite=c(59)),

 dict(topic="Hyperhidrosis", io=IOA, slot="education",
   q="Which points should the conversation with a hyperhidrosis patient cover?",
   opts=[
     ["That it is not about poor hygiene or anxiety, with moisture-wicking clothing suggested and realistic expectations set",
      "Correct — botulinum toxin needs repeating every three to six months and can be cost-prohibitive."],
     ["That improved washing and a reduction in stress will resolve all of the sweating within a few months",
      "She was explicit that it is not about hygiene or anxiety."],
     ["That a single course of treatment produces a permanent cure",
      "Botulinum toxin lasts three to six months and must be repeated."],
     ["That the condition is rare and few treatment options exist",
      "It affects roughly 3 to 5% and has a full treatment ladder."]],
   c=0, cite=c(76)),

 dict(topic="Hyperhidrosis", io=IOA, slot="risk factors",
   q="Which history should be taken carefully in a patient presenting with excessive sweating?",
   opts=[
     ["The family history, alongside whether the sweating is focal or generalised",
      "Correct — generalised sweating for no reason requires additional workup."],
     ["The travel history over the previous twelve months",
      "That matters for infestations rather than for hyperhidrosis."],
     ["The occupational chemical exposure history, taken in some detail",
      "That matters for contact dermatitis."],
     ["The sun exposure and tanning bed history",
      "That matters for photodermatology."]],
   c=0, cite=c(73)),

 dict(topic="Sunburn", io=IOA, slot="first-line",
   q="Which measures are named for acute sunburn?",
   opts=[
     ["Cool compresses, an early nonsteroidal anti-inflammatory drug, and oral hydration",
      "Correct — ibuprofen or naproxen reduce the prostaglandin-mediated pain."],
     ["Warm compresses, an oral antihistamine, and a topical corticosteroid cream",
      "Warm compresses are used for furuncles and paronychia."],
     ["Ice packs applied directly, with a systemic corticosteroid taper",
      "Cool rather than cold is advised, and steroids are not part of this."],
     ["Silver sulfadiazine dressings applied twice daily under occlusion",
      "That is a burn dressing agent not used in ordinary sunburn."]],
   c=0, cite=c(96)),

 dict(topic="Photosensitivity", io=IOA, slot="gold standard",
   q="How is photosensitivity primarily diagnosed?",
   opts=[
     ["Largely through the history — it is more of a clinical diagnosis",
      "Correct, with photopatch testing reserved for suspected photoallergy."],
     ["By skin biopsy of an affected area in every patient",
      "Biopsy is rarely needed."],
     ["By serological testing for antibodies to the causative drug",
      "No such serology is described."],
     ["By minimal erythema dose testing before any history is taken",
      "Phototesting supports rather than replaces the history."]],
   c=0, cite=c(99)),

 dict(topic="Epidermolysis bullosa", io=IOA, slot="etiology",
   q="What causes epidermolysis bullosa?",
   opts=[
     ["A mutation in structural proteins",
      "Correct — the level at which the skin separates follows from which protein is affected."],
     ["Immunoglobulin A deposition in the dermal papillae",
      "That is dermatitis herpetiformis."],
     ["A type IV hypersensitivity reaction to a drug",
      "That is Stevens-Johnson syndrome and toxic epidermal necrolysis."],
     ["Autoantibodies against the epidermal basement membrane",
      "That is bullous pemphigoid."]],
   c=0, cite=c(27)),

 dict(topic="Epidermolysis bullosa", io=IOA, slot="referral",
   q="How broad is the referral requirement in epidermolysis bullosa?",
   opts=[
     ["Essentially every specialty, given the multisystem burden",
      "Correct — palliative care, genetics and family support are all involved."],
     ["Dermatology alone, since the disease is confined to the skin",
      "The disease burden is multisystem."],
     ["Genetics alone, since the diagnosis is made on a genetic panel",
      "Genetics is one referral among many."],
     ["No routine referral, since the condition is managed in primary care",
      "The condition requires broad specialist involvement."]],
   c=0, cite=c(31)),
]
