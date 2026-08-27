# CMS I Lecture 6 (Cutaneous Viral and Fungal Infections, Prof. Jaquith) — pool A.
# Antifungal classes, the dermatophyte overview, tinea capitis and tinea barbae.
#
# THE SLIDE IS AUTHORITATIVE. Jaxon, 2026-08-20: "especially Dr. Jaquith audio
# because she says words wrong all the time, so go by the powerpoints unless
# told otherwise." Every fact in this pool comes from the deck. Nothing is taken
# from a recording; when the Lecture 6 audio appears it will be folded in as a
# separate pool, and any claim it makes that the deck contradicts will lose.
#
# Correct answers kept SHORT wherever the content enumerates; the detail goes in
# the explanation the student reads after answering.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "6. Fungal and Viral Skin Infections - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Interpret a potassium hydroxide (KOH) wet mount preparation"
IOB = "b — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis of cutaneous viral and fungal infections"
IOC = "c — Identify medical care strategies for cutaneous viral and fungal infections for infant, child, adolescent, adult and elderly populations"

POOL_A = [
 dict(topic="Antifungal classes", io=IOB, slot="agent/regimen",
   q="How does the allylamine class of antifungals work, and how do you recognise one by name?",
   opts=[
     ["It destroys the fungal cell membrane; the names end in -fine",
      "Correct — terbinafine and naftifine. Destroying the membrane prevents growth and ultimately kills the fungus."],
     ["It blocks synthesis of ergosterol; the names end in -azole",
      "That is the imidazole class, which halts growth and replication rather than destroying the membrane outright."],
     ["It inhibits mitosis in dividing fungal cells; the names end in -fulvin",
      "Griseofulvin is used in this lecture but is not the class described here."],
     ["It blocks cell wall glucan synthesis; the names end in -fungin",
      "The echinocandins are not among the two classes on this slide."]],
   c=0, cite=c(5)),

 dict(topic="Antifungal classes", io=IOB, slot="agent/regimen",
   q="How does the imidazole class work, and which two examples does the deck give?",
   opts=[
     ["It blocks ergosterol synthesis; clotrimazole and ketoconazole",
      "Correct — ergosterol is a vital component of the fungal cell membrane, so blocking it halts growth and replication. The names end in -azole."],
     ["It destroys the fungal cell membrane directly; terbinafine and naftifine",
      "That is the allylamine class."],
     ["It blocks synthesis of chitin in the fungal cell wall; nystatin and amphotericin",
      "Chitin synthesis is not the mechanism described, and those agents are not imidazoles."],
     ["It inhibits fungal deoxyribonucleic acid synthesis; griseofulvin and fluconazole",
      "Neither the mechanism nor the pairing matches the slide."]],
   c=0, cite=c(5)),

 dict(topic="Dermatophytes", io=IOB, slot="etiology",
   q="What do dermatophytes infect and survive on, and where can they NOT survive?",
   opts=[
     ["Dead keratin — the stratum corneum, hair and nails; they cannot survive on mucous membranes",
      "Correct — which is why dermatophyte infection is superficial by definition."],
     ["Living keratinocytes of the basal layer; they cannot survive on the nail plate",
      "The organisms live on dead keratin, and nails are among the tissues they infect."],
     ["Sebum within the pilosebaceous unit; they cannot survive on glabrous skin",
      "Sebum is relevant to tinea capitis after puberty, but it is not what they live on."],
     ["Mucous membranes and moist epithelium; they cannot survive on dry skin",
      "This is the reverse of what the slide states."]],
   c=0, cite=c(6)),

 dict(topic="Dermatophytes", io=IOB, slot="etiology",
   q="Which three genera account for the majority of dermatophyte infections?",
   opts=[
     ["Microsporum, Trichophyton, Epidermophyton",
      "Correct — and infections are then classified by body location."],
     ["Candida, Malassezia, Trichophyton",
      "Candida and Malassezia are yeasts, covered separately in this lecture."],
     ["Microsporum, Malassezia, Epidermophyton",
      "Malassezia causes pityriasis versicolor and is not a dermatophyte."],
     ["Trichophyton, Aspergillus, Epidermophyton",
      "Aspergillus is a mould and is not among the three named."]],
   c=0, cite=c(6)),

 dict(topic="Dermatophytes", io=IOB, slot="manifestation",
   q="How are dermatophyte infections classified?",
   opts=[
     ["By the body location of the fungus",
      "Correct — capitis, barbae, corporis, manuum, cruris, pedis."],
     ["By the genus of the organism responsible",
      "The organism matters for treatment, but the naming follows the site."],
     ["By whether the infection is inflammatory or non-inflammatory",
      "That distinction is drawn within tinea barbae rather than across the group."],
     ["By the depth of invasion into the skin",
      "All dermatophyte infections are superficial by definition."]],
   c=0, cite=c(7)),

 dict(topic="Tinea capitis", io=IOC, slot="epidemiology",
   q="In whom does tinea capitis predominantly occur, and why does it become uncommon after puberty?",
   opts=[
     ["Preadolescent children; sebum changes after puberty inhibit growth",
      "Correct — changes in the fatty acid content of sebum after puberty are believed to inhibit dermatophyte growth. It is the most common fungal infection in children."],
     ["Older adults; declining sebum production after middle age removes a protective barrier",
      "The relationship runs the other way, and the age group is wrong."],
     ["Adolescent males; androgen-driven sebum production favours the organism",
      "Sebum change after puberty is protective rather than permissive."],
     ["Immunocompromised adults; cell-mediated immunity normally clears the organism",
      "Immunosuppression matters elsewhere in this lecture but is not the epidemiology here."]],
   c=0, cite=c(9)),

 dict(topic="Tinea capitis", io=IOB, slot="etiology",
   q="Which species are most common in tinea capitis, and which predominates in the United States?",
   opts=[
     ["Trichophyton and Microsporum, with Trichophyton tonsurans most common in the United States",
      "Correct — the species matters because it drives the choice of oral agent."],
     ["Epidermophyton and Microsporum, with Epidermophyton floccosum most common in the United States",
      "Epidermophyton is not among the two named for the scalp."],
     ["Candida and Malassezia, with Candida albicans most common in the United States",
      "Those are yeasts and cause different conditions in this lecture."],
     ["Trichophyton and Epidermophyton, with Trichophyton rubrum most common in the United States",
      "Trichophyton rubrum is the common pathogen for tinea corporis and pedis rather than capitis."]],
   c=0, cite=c(9)),

 dict(topic="Tinea capitis", io=IOB, slot="risk factors",
   q="How is tinea capitis transmitted, and what does the deck emphasise about the fungal particles?",
   opts=[
     ["From people, pets and fomites; the particles stay viable for MONTHS",
      "Correct — infected persons, pets, fallen hairs, clothing, combs, hats and furniture. Asymptomatic carriers are also a source."],
     ["Only by direct scalp-to-scalp contact; the particles die within hours off the host",
      "Fomites are a major route, and the particles persist for months."],
     ["Only from animals; the particles cannot survive on inanimate objects at all",
      "Pets are one source among several, and fomites do carry the organism."],
     ["Through contaminated water in swimming pools; the particles survive only when wet",
      "Water-borne transmission is not described for this infection."]],
   c=0, cite=c(10)),

 dict(topic="Tinea capitis", io=IOB, slot="manifestation",
   q="What is black dot tinea capitis?",
   opts=[
     ["Infection with fracture of the hair at the scalp surface",
      "Correct — the black dots are the broken hair shafts, and patches of alopecia carrying them are characteristic."],
     ["Infection producing black comedone-like plugs within the follicular openings",
      "The dots are broken hair shafts rather than plugs."],
     ["Infection with black pigment produced by the dermatophyte itself",
      "The organism does not pigment the scalp."],
     ["Infection with punctate haemorrhage into the scalp at follicular sites",
      "Haemorrhage is not what produces the appearance."]],
   c=0, cite=c(12)),

 dict(topic="Tinea capitis", io=IOB, slot="manifestation",
   q="Besides alopecia and scaly patches, which examination finding is often present in tinea capitis?",
   opts=[
     ["Lymphadenopathy",
      "Correct — alongside red papules progressing to grayish ring-formed patches with perifollicular papules."],
     ["Fever above 38 degrees Celsius",
      "Systemic fever is not among the findings listed."],
     ["Nail pitting",
      "Nail changes are not part of the tinea capitis picture here."],
     ["Coral-red fluorescence under a Wood lamp",
      "Coral-red fluorescence is erythrasma, mentioned under tinea cruris."]],
   c=0, cite=c(12)),

 dict(topic="Tinea capitis", io=IOB, slot="differential",
   q="Which feature separates seborrheic dermatitis from tinea capitis on the deck's differential?",
   opts=[
     ["Hair may be lost but not broken, and the scales are fine, dry or greasy",
      "Correct — the hair fracture is what points to tinea."],
     ["The skin is smooth and shiny without inflammation or infection",
      "That describes alopecia areata."],
     ["There are perifollicular pustules",
      "That describes folliculitis."],
     ["There is a well demarcated plaque of erythema with white or silver scale",
      "That describes psoriasis."]],
   c=0, cite=c(13)),

 dict(topic="Tinea capitis", io=IOA, slot="initial test",
   q="How is suspected tinea capitis confirmed, and what is the caveat about the Wood lamp?",
   opts=[
     ["Potassium hydroxide microscopy and fungal culture; the Wood lamp can mislead",
      "Correct — the lamp may rapidly support Microsporum, but Trichophyton tonsurans usually does NOT fluoresce, and it is the commonest species in the United States. So a negative lamp proves little."],
     ["Wood lamp alone, since all dermatophytes of the scalp fluoresce green",
      "Trichophyton tonsurans usually does not fluoresce, which is exactly the trap."],
     ["Bacterial culture alone, since the organism grows readily on standard media",
      "Bacterial culture is reserved for a kerion with purulent drainage or suspected secondary infection."],
     ["Skin biopsy in every case before systemic therapy is begun",
      "Biopsy is not the confirmatory step described."]],
   c=0, cite=c(14)),

 dict(topic="Tinea capitis", io=IOB, slot="first-line",
   q="Why does tinea capitis require oral rather than topical therapy?",
   opts=[
     ["Topical agents alone do not penetrate the infected hair shaft",
      "Correct — antifungal shampoo reduces spore shedding but does not replace oral therapy."],
     ["Topical agents are inactivated by scalp sebum",
      "Sebum matters to the epidemiology, not to drug inactivation."],
     ["The infection extends into the dermis, beyond topical reach",
      "Dermatophyte infection is superficial; the problem is the hair shaft."],
     ["Children cannot tolerate the irritation of topical antifungals",
      "Tolerability is not the reason given."]],
   c=0, cite=c(15)),

 dict(topic="Tinea capitis", io=IOB, slot="agent/regimen",
   q="Which oral agent is generally favoured for each organism in tinea capitis?",
   opts=[
     ["Terbinafine for Trichophyton; griseofulvin for Microsporum",
      "Correct — which is why species identification matters before a prolonged course."],
     ["Griseofulvin for Trichophyton; terbinafine for Microsporum",
      "This reverses the two pairings."],
     ["Fluconazole for both, since it covers dermatophytes and yeasts",
      "Fluconazole is not the agent paired with either organism here."],
     ["Ketoconazole orally for both, at weight-based dosing",
      "Oral ketoconazole is specifically deprecated later in this deck for superficial infection."]],
   c=0, cite=c(15)),

 dict(topic="Tinea capitis", io=IOB, slot="escalation",
   q="A child with tinea capitis is not responding to oral therapy. Which five explanations does the deck list?",
   opts=[
     ["Adherence, wrong diagnosis, reinfection, organism mismatch, or resistance",
      "Correct — reassess all five before assuming the drug has failed."],
     ["Dose, duration, drug interaction, hepatic impairment, or malabsorption",
      "Some of these matter clinically, but they are not the five listed."],
     ["Immunosuppression, diabetes, malnutrition, anaemia, or age",
      "Host factors are not the list given for nonresponse."],
     ["Secondary bacterial infection, kerion, scarring, id reaction, or contact dermatitis",
      "These are complications rather than reasons for nonresponse."]],
   c=0, cite=c(15)),

 dict(topic="Tinea capitis", io=IOB, slot="agent/regimen",
   q="What role does antifungal shampoo play in tinea capitis, and which agents are named?",
   opts=[
     ["It reduces spore shedding but does not replace oral therapy",
      "Correct — selenium sulfide 1 to 2.5 per cent or ketoconazole 2 per cent, used two to three times weekly during early systemic treatment."],
     ["It is curative on its own if used daily for six weeks; selenium sulfide only",
      "Shampoo never replaces the oral course."],
     ["It prevents reinfection but has no effect on spore shedding; ketoconazole only",
      "Reducing spore shedding is precisely what it does."],
     ["It is used only in household contacts, never in the patient; either agent",
      "Contacts may use sporicidal shampoo, but so does the patient."]],
   c=0, cite=c(16)),

 dict(topic="Tinea capitis", io=IOC, slot="education",
   q="What does the deck say about school exclusion in tinea capitis?",
   opts=[
     ["Generally unnecessary once effective therapy has begun",
      "Correct — follow local policy. And complete the oral course even when itching or scaling improves early."],
     ["The child must be excluded until fungal culture is negative",
      "That is stricter than what the deck advises."],
     ["The child must be excluded for the full duration of oral therapy",
      "Exclusion is generally unnecessary once treatment has started."],
     ["Exclusion is required only if a kerion is present",
      "No such conditional rule is given."]],
   c=0, cite=c(17)),

 dict(topic="Tinea capitis", io=IOB, slot="complication",
   q="Why does the deck say to treat inflammatory tinea capitis promptly?",
   opts=[
     ["To reduce the risk of scarring alopecia",
      "Correct — and to reassess if a kerion develops or improvement is absent after several weeks."],
     ["To prevent systemic dissemination of the dermatophyte",
      "Dermatophytes do not disseminate systemically here."],
     ["To prevent progression to tinea barbae",
      "The two are separate infections by site."],
     ["To avoid the need for fungal culture",
      "Culture is recommended before prolonged systemic therapy rather than avoided."]],
   c=0, cite=c(17)),

 dict(topic="Tinea barbae", io=IOB, slot="differential",
   q="How do the inflammatory and non-inflammatory forms of tinea barbae differ?",
   opts=[
     ["Inflammatory comes from ANIMALS and is boggy and pustular; non-inflammatory comes from a PERSON and is annular and scaly",
      "Correct — the inflammatory form gives tender, boggy, pustular kerion-like plaques with hairs that are loose and easily removed, and scarring alopecia may follow. The non-inflammatory form gives annular scaly plaques or a folliculitis-like eruption with hairs breaking near the surface."],
     ["Inflammatory is acquired from another person and gives annular scaly plaques; non-inflammatory is acquired from animals and gives boggy pustular plaques",
      "This reverses both the source and the appearance."],
     ["Inflammatory affects the moustache area only; non-inflammatory affects the chin only",
      "The distinction is not anatomical."],
     ["Inflammatory occurs in immunocompromised patients; non-inflammatory in the immunocompetent",
      "Immune status is not what separates them here."]],
   c=0, cite=c(19)),

 dict(topic="Tinea barbae", io=IOB, slot="differential",
   q="Which examination finding separates tinea barbae from bacterial folliculitis?",
   opts=[
     ["The hair is easily removed in tinea barbae",
      "Correct — and bacterial culture can be performed to rule folliculitis out."],
     ["The lesions are painful in tinea barbae and painless in folliculitis",
      "Tenderness occurs in the inflammatory form of both."],
     ["Tinea barbae spares the upper lip",
      "No such anatomical rule is given."],
     ["Tinea barbae produces fever and lymphadenopathy",
      "Systemic features are not the discriminator named."]],
   c=0, cite=c(21)),

 dict(topic="Tinea barbae", io=IOB, slot="first-line",
   q="Why does tinea barbae require oral therapy, and which agents are named?",
   opts=[
     ["Topical antifungals do not penetrate the hair follicle; griseofulvin or terbinafine",
      "Correct — with shaving or hair removal and warm compresses to lift crusts and debris."],
     ["Topical antifungals are inactivated by beard sebum; fluconazole or itraconazole",
      "Follicle penetration, not inactivation, is the reason, and those are not the agents named."],
     ["The infection is systemic from the outset; intravenous amphotericin",
      "The infection is superficial and no intravenous therapy is described."],
     ["Oral therapy is preferred only for cosmetic reasons; any azole",
      "The reason is pharmacological rather than cosmetic."]],
   c=0, cite=c(22)),
]
