# CMS I Lecture 2 (General Dermatology I) — SET 2, vignette pool A.
# Eczemas and dermatitides.
#
# Built to [[vignette_question_style]] and [[cms_exam_spec]]:
#   - FOUR options, never five, and no "none of the above".
#   - Every stem carries the beats: presentation, clues (age / risk factors /
#     exposures), and the DEFINING FEATURE the case turns on.
#   - The lead-in VARIES. Not every vignette asks for management — diagnosis,
#     next step, first-line treatment, initial test, confirmatory test and
#     patient education are all represented.
#   - The lead-in decides the answer. Some stems describe a disease whose
#     definitive treatment is among the options, but ask for the next step
#     instead; recognising the disease and answering the question are two acts.
#   - Distractors are RIGHT-DISEASE, WRONG-PHASE wherever possible, or a real
#     condition this lecture teaches that shares the presentation.
#   - Named findings carry a description in parentheses.
#   - Risk-factor and defining-feature questions belong to Set 1, not here.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "2. General Dermatology I.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOC = "c — Etiologies, manifestations, diagnosis and management of dermatological conditions"

POOL_A = [
 dict(topic="Atopic dermatitis", io=IOC,
   q="A 7-year-old boy is brought in with a recurrent, intensely pruritic rash in the antecubital and popliteal fossae. Examination shows poorly demarcated erythematous plaques with excoriations and lichenification (thickening with exaggerated skin lines). His mother has asthma. There is no fever, drainage, crusting or tenderness. Which is the most appropriate initial treatment?",
   opts=[
     ["Topical hydrocortisone with regular emollient use",
      "Correct. Low-potency steroid plus barrier repair is first line, and the flexural distribution with a family atopy history is classic childhood atopic dermatitis."],
     ["Oral cephalexin",
      "An antibiotic would be right for secondary infection, but there is no fever, drainage, crusting or tenderness to suggest it."],
     ["Oral terbinafine",
      "An antifungal treats tinea, which would show central clearing rather than flexural lichenified plaques."],
     ["Systemic prednisone for four weeks",
      "Systemic steroids are reserved for severe disease; this presentation is managed topically."]],
   c=0, cite=c(57)),

 dict(topic="Atopic dermatitis", io=IOC,
   q="A 4-month-old infant has weeping inflammatory patches and crusted plaques on the cheeks, scalp and extensor surfaces of the arms. The mother reports the baby rubs against bedding rather than scratching. Which is the most likely diagnosis?",
   opts=[
     ["Atopic dermatitis",
      "Correct. The infantile pattern favours cheeks, scalp and extensor surfaces, and rubbing replaces scratching at this age."],
     ["Seborrhoeic dermatitis",
      "This produces greasy yellow scaling in sebum-rich areas and is most common in men aged 20 to 50."],
     ["Nummular eczema",
      "This produces coin-shaped plaques on the extremities, typically in men over 50."],
     ["Irritant contact dermatitis",
      "This follows a clearly demarcated pattern matching an exposure rather than this distribution."]],
   c=0, cite=c(53)),

 dict(topic="Atopic dermatitis", io=IOC,
   q="A 6-year-old with known atopic dermatitis develops painful, uniform punched-out erosions over a flaring area, with fever and malaise. Which is the most appropriate next step?",
   opts=[
     ["Order herpes simplex virus polymerase chain reaction",
      "Correct. Painful monomorphic erosions with systemic illness is the stated trigger for this test, since eczema herpeticum needs excluding before treatment escalates."],
     ["Increase the potency of the topical corticosteroid",
      "Escalating steroid without excluding herpes risks worsening a viral superinfection."],
     ["Begin a topical calcineurin inhibitor",
      "These suit sensitive sites in uncomplicated disease, not a febrile patient with erosions."],
     ["Order patch testing",
      "Patch testing is for atypical, adult-onset or treatment-resistant disease, not acute febrile deterioration."]],
   c=0, cite=c(56)),

 dict(topic="Atopic dermatitis", io=IOC,
   q="A mother of a child newly diagnosed with atopic dermatitis is anxious about using topical steroids at all. Which is the most appropriate counselling point?",
   opts=[
     ["Address the concern directly, review the side effects, demonstrate how much to apply, and provide a written flare and infection action plan",
      "Correct. Addressing steroid concerns directly and demonstrating quantity and application are named education points."],
     ["Advise avoiding all topical steroids and relying on emollients alone",
      "Emollients are foundational but do not control inflammation on their own."],
     ["Advise applying the steroid generously over the whole body twice daily",
      "Steroids are applied sparingly and to affected sites, with potency matched to the site."],
     ["Advise that the condition will resolve permanently by school age, so treatment is optional",
      "The prognosis is chronic and relapsing, though many improve with age."]],
   c=0, cite=c(58)),

 dict(topic="Dyshidrotic eczema", io=IOC,
   q="A 29-year-old hairdresser has a three-week history of intensely itchy small blisters along the sides of her fingers and on her palms. Examination shows grouped 1 to 2 mm vesicles described as resembling tapioca, on a poorly defined erythematous base, with surrounding dryness. Which is the most likely diagnosis?",
   opts=[
     ["Dyshidrotic eczema",
      "Correct. Tapioca vesicles on the palms and lateral fingers are the defining picture; vesicles may coalesce into bullae before desquamating."],
     ["Allergic contact dermatitis",
      "This would be well demarcated at the contact site, often shaped like the causative object."],
     ["Bullous pemphigoid",
      "This produces 1 to 3 cm tense bullae on the trunk and flexures, typically after age 60."],
     ["Nummular eczema",
      "This produces coin-shaped plaques on the extremities without vesiculation."]],
   c=0, cite=c(65)),

 dict(topic="Dyshidrotic eczema", io=IOC,
   q="A 33-year-old man has recurrent tapioca-like vesicles on his palms confirmed clinically as dyshidrotic eczema. Which is the most appropriate first-line treatment?",
   opts=[
     ["A high-potency topical corticosteroid",
      "Correct. High potency is specified first line here, with systemic corticosteroids reserved for severe cases."],
     ["A low-potency topical corticosteroid",
      "Low potency is chosen for the face and sensitive sites, not for palmar disease."],
     ["A topical antifungal",
      "The condition is not fungal; its aetiology is unknown."],
     ["Oral prednisone tapered over three weeks",
      "Systemic therapy is reserved for severe disease rather than used first line."]],
   c=0, cite=c(66)),

 dict(topic="Nummular eczema", io=IOC,
   q="A 62-year-old man has several intensely itchy round plaques on his lower legs, 2 to 4 cm across, light pink with scale and crusting. The plaques are uniform throughout without any central clearing. Which is the most appropriate initial diagnostic test?",
   opts=[
     ["Potassium hydroxide preparation",
      "Correct. Tinea corporis is the main differential and is excluded by potassium hydroxide, though the absent central clearing already argues against it."],
     ["Bacterial culture",
      "Culture is reserved for lesions that appear secondarily infected."],
     ["Allergy patch testing",
      "Patch testing is considered for chronic or recurrent disease rather than at first presentation."],
     ["Punch biopsy for direct immunofluorescence",
      "Immunofluorescence is used for vesiculobullous disease."]],
   c=0, cite=c(74)),

 dict(topic="Nummular eczema", io=IOC,
   q="A 58-year-old man has coin-shaped scaly plaques on both shins. A potassium hydroxide preparation is negative and there is no purulence. Which is the most appropriate first-line treatment?",
   opts=[
     ["Medium to high potency topical corticosteroids with emollients",
      "Correct — steroids for the active lesions and emollients to restore the barrier and prevent recurrence."],
     ["Oral terbinafine",
      "The potassium hydroxide preparation was negative, so this is not tinea."],
     ["Compression therapy",
      "Compression treats stasis dermatitis, which presents in the gaiter region with oedema and venous change."],
     ["Ketoconazole shampoo",
      "Antifungal shampoo treats seborrhoeic dermatitis of the scalp."]],
   c=0, cite=c(74)),

 dict(topic="Irritant contact dermatitis", io=IOC,
   q="A 41-year-old intensive care nurse reports several weeks of worsening dryness, redness and scaling of both hands, worst over the dorsal surfaces. She washes her hands more than thirty times a shift. The rash is well demarcated with a glazed appearance and there are no vesicles. Which is the most likely diagnosis?",
   opts=[
     ["Irritant contact dermatitis",
      "Correct — the commonest form of contact dermatitis, frequently occupational, with soaps and detergents as classic irritants and a glazed well-demarcated appearance."],
     ["Allergic contact dermatitis",
      "This is a delayed type IV reaction to a specific allergen and typically produces vesicles at the site of contact."],
     ["Dyshidrotic eczema",
      "This produces tapioca vesicles on the palms and lateral fingers rather than glazed dorsal scaling."],
     ["Psoriasis",
      "This produces well-demarcated plaques with silvery scale on extensor surfaces."]],
   c=0, cite=c(80)),

 dict(topic="Irritant contact dermatitis", io=IOC,
   q="A 44-year-old janitor has chronic dry, fissured, glazed dermatitis of both hands from repeated detergent exposure. Which is the most appropriate management?",
   opts=[
     ["Avoid the exposure and repair the barrier with emollients, sleeping in cotton gloves after applying a heavy emollient such as petroleum jelly",
      "Correct, with antihistamines such as hydroxyzine or diphenhydramine for itch."],
     ["Begin a high-potency topical corticosteroid indefinitely",
      "Barrier repair and avoidance are the described management rather than indefinite steroids."],
     ["Begin oral doxycycline",
      "This is not an infectious or acneiform condition."],
     ["Refer for patch testing before any treatment",
      "Patch testing identifies allergens in allergic contact dermatitis; this is irritant disease from a known exposure."]],
   c=0, cite=c(82)),

 dict(topic="Allergic contact dermatitis", io=IOC,
   q="A 22-year-old presents two days after clearing brush in the garden with intensely itchy blisters in streaks across both forearms. Examination shows linear vesicles and papules in several stages, with excoriations. Which is the most likely diagnosis?",
   opts=[
     ["Allergic contact dermatitis from urushiol",
      "Correct. The linear distribution comes from grazing the plant in passing, and lesions erupt 4 to 96 hours after exposure."],
     ["Irritant contact dermatitis",
      "This produces well-demarcated glazed change at the exposure site rather than linear vesicles."],
     ["Herpes zoster",
      "Shingles follows a dermatome rather than crossing both forearms in streaks."],
     ["Bullous pemphigoid",
      "This produces tense bullae on the trunk and flexures in patients typically over 60."]],
   c=0, cite=c(87)),

 dict(topic="Allergic contact dermatitis", io=IOC,
   q="A 30-year-old has extensive urushiol contact dermatitis covering both arms, the neck and part of the trunk. Which is the most appropriate treatment?",
   opts=[
     ["High-dose oral corticosteroids tapered over two to three weeks",
      "Correct — extensive disease needs systemic therapy, and early discontinuation causes high rates of rebound."],
     ["High-potency topical corticosteroids alone",
      "Topical therapy suits mild eruptions on limited body surface area."],
     ["A five-day course of oral prednisone without taper",
      "Right drug, wrong duration: stopping early results in high rates of rebounding."],
     ["Oral antihistamines alone",
      "Antihistamines address itch but will not control an extensive eruption."]],
   c=0, cite=c(89)),

 dict(topic="Allergic contact dermatitis", io=IOC,
   q="A 26-year-old developed an itchy rash confined to a rectangle on her forearm, sparing a small central area, three days after a minor injury. Which is the most appropriate counselling point?",
   opts=[
     ["The reaction is to the adhesive in the dressing, and the spared centre corresponds to the cotton pad",
      "Correct — the shape reproducing the object is the hallmark of allergic contact dermatitis to adhesives."],
     ["The rash is contagious and she should avoid close contact until it clears",
      "Allergic contact dermatitis is not contagious."],
     ["The reaction indicates the wound is infected and needs antibiotics",
      "The shape and sparing point to an adhesive allergy, not infection."],
     ["Future exposure to the same adhesive will not cause a reaction once this settles",
      "Sensitisation persists, so re-exposure will provoke it again."]],
   c=0, cite=c(86)),

 dict(topic="Seborrhoeic dermatitis", io=IOC,
   q="A 34-year-old man has recurrent scaling of the scalp, eyebrows, nasolabial folds and external ears. Examination shows greasy, yellow-white scale over mildly erythematous poorly demarcated patches. Which is the most appropriate initial treatment?",
   opts=[
     ["Ketoconazole shampoo and topical ketoconazole cream",
      "Correct. Topical antifungals are the mainstay because Malassezia overgrowth drives the condition; steroids may be added early to reduce inflammation."],
     ["Oral terbinafine",
      "Systemic antifungal therapy is not the described approach for this condition."],
     ["High-potency topical corticosteroids as monotherapy",
      "Steroids are adjunctive and used early; antifungals are the mainstay."],
     ["Topical mupirocin",
      "A topical antibiotic treats bacterial infection, which this is not."]],
   c=0, cite=c(95)),

 dict(topic="Seborrhoeic dermatitis", io=IOC,
   q="A 40-year-old man with recurrent greasy scaling of the scalp and nasolabial folds asks how long treatment will be needed. Which is the most appropriate counselling point?",
   opts=[
     ["The condition is chronic and relapsing, so repeated and long-term use of medication is often required",
      "Correct — that expectation is stated explicitly for this condition."],
     ["A single two-week course of antifungal shampoo is usually curative",
      "The condition recurs; long-term intermittent treatment is the norm."],
     ["It will resolve permanently once stress is controlled",
      "Stress plays a role but does not cure it."],
     ["It is contagious and household members should be treated as well",
      "Malassezia is normal skin flora rather than a transmissible infection."]],
   c=0, cite=c(95)),

 dict(topic="Perioral dermatitis", io=IOC,
   q="A 27-year-old woman has burning and small red papules around her mouth. Examination shows grouped monomorphic papules and pustules over the nasolabial folds and chin, sparing a narrow rim next to the vermilion border. She has used hydrocortisone cream daily for several months. Which is the most appropriate initial management?",
   opts=[
     ["Discontinue the corticosteroid and simplify her skin-care routine",
      "Correct. Topical corticosteroid exposure is the most important modifiable association, and continued use perpetuates the condition."],
     ["Increase the potency of the topical corticosteroid",
      "This worsens the condition; the steroid is the driver."],
     ["Begin topical adapalene",
      "A retinoid treats acne, which would show comedones rather than this monomorphic sparing pattern."],
     ["Apply an occlusive moisturiser several times daily",
      "Occlusive moisturisers are among the listed triggers."]],
   c=0, cite=c(102)),

 dict(topic="Perioral dermatitis", io=IOC,
   q="A 31-year-old woman with perioral dermatitis has stopped her topical corticosteroid. Which is the most appropriate counselling point about what happens next?",
   opts=[
     ["The eruption may temporarily worsen after corticosteroid withdrawal before it improves",
      "Correct — telling her in advance is what stops her restarting the steroid."],
     ["The eruption should clear completely within 48 hours of stopping",
      "Improvement is not that rapid, and a temporary flare is expected."],
     ["She should resume the steroid if the rash worsens at all",
      "Resuming it perpetuates the condition, which is why the warning is given."],
     ["The condition will not recur once the steroid has been stopped once",
      "Recurrence is possible, particularly with re-exposure to triggers."]],
   c=0, cite=c(102)),

 dict(topic="Perioral dermatitis", io=IOC,
   q="A 29-year-old woman has extensive perioral dermatitis that has persisted despite stopping her topical corticosteroid and simplifying her routine. Which is the most appropriate treatment?",
   opts=[
     ["Oral tetracycline or doxycycline",
      "Correct — more extensive or persistent disease may require an oral tetracycline."],
     ["Topical metronidazole",
      "Right disease, wrong severity: topical agents suit mild disease."],
     ["Oral prednisone",
      "Systemic steroids are not the described treatment and risk perpetuating the eruption."],
     ["Topical high-potency corticosteroid",
      "Facial corticosteroids are precisely what must be avoided here."]],
   c=0, cite=c(102)),

 dict(topic="Diaper dermatitis", io=IOC,
   q="A 9-month-old has a bright red rash in the diaper area. Examination shows beefy erythema involving the inguinal folds with peripheral scale and scattered satellite papules and pustules beyond the main area. Which is the most likely diagnosis?",
   opts=[
     ["Candidal diaper dermatitis",
      "Correct. Fold involvement with satellite lesions is the candidal pattern; irritant disease spares the folds."],
     ["Irritant diaper dermatitis",
      "This affects convex surfaces and generally spares the inguinal folds."],
     ["Bacterial diaper dermatitis",
      "This would show bullae, crusting, purulent drainage or sharply demarcated perianal erythema."],
     ["Seborrhoeic dermatitis",
      "This favours sebum-rich areas with greasy yellow scale."]],
   c=0, cite=c(107)),

 dict(topic="Diaper dermatitis", io=IOC,
   q="An 8-month-old has erythema, scaling and small erosions over the convex surfaces of the buttocks and upper thighs, with the inguinal folds clearly spared. There is no purulence. Which is the most appropriate initial management?",
   opts=[
     ["Frequent diaper changes, gentle cleansing, air exposure and a thick zinc oxide or petrolatum barrier at each change",
      "Correct — reducing moisture and irritant exposure is the foundation, and the fold sparing indicates irritant rather than candidal disease."],
     ["A topical antifungal at every change",
      "An antifungal is added when candidal disease is suspected, which fold involvement and satellite lesions would indicate."],
     ["Oral antibiotics",
      "Antibiotics are used only when bacterial infection is clinically supported."],
     ["A high-potency topical corticosteroid until the rash clears",
      "Only a brief course of a low-potency steroid is used, and only for significant inflammation."]],
   c=0, cite=c(109)),

 dict(topic="Stasis dermatitis", io=IOC,
   q="A 68-year-old woman has chronic bilateral lower-leg swelling, itching and skin discoloration. Examination shows poorly demarcated erythematous plaques, pitting oedema and brown hyperpigmentation around both medial ankles. Pedal pulses are diminished. Which is the most appropriate next step before prescribing compression therapy?",
   opts=[
     ["Perform an ankle-brachial index",
      "Correct. Compression is the cornerstone of management, but only once adequate arterial circulation is established, and the diminished pulses demand that check first."],
     ["Obtain a bacterial wound culture",
      "There is no purulence or ulceration to culture, and the picture is not infectious."],
     ["Order patch testing",
      "Patch testing identifies contact allergens rather than assessing arterial supply."],
     ["Begin oral cephalexin",
      "Distinguishing stasis dermatitis from cellulitis is a stated priority, and nothing here indicates infection."]],
   c=0, cite=c(116)),

 dict(topic="Stasis dermatitis", io=IOC,
   q="A 71-year-old man with long-standing venous insufficiency has itchy, hyperpigmented plaques over both gaiter regions with induration. His ankle-brachial index is normal. Which is the most appropriate management?",
   opts=[
     ["Compression therapy, with leg elevation, walking and calf-muscle exercises",
      "Correct — compression is the cornerstone once arterial circulation is adequate."],
     ["Long-term systemic antibiotics",
      "Stasis dermatitis is inflammatory rather than infectious."],
     ["High-potency topical corticosteroids as sole long-term therapy",
      "A short steroid course controls active inflammation but is not the cornerstone."],
     ["Strict bed rest with the legs dependent",
      "Elevation and walking are advised; dependency worsens venous hypertension."]],
   c=0, cite=c(117)),

 dict(topic="Stasis dermatitis", io=IOC,
   q="A 66-year-old woman with known bilateral stasis dermatitis develops acute swelling and pain in the right calf over two days. Which is the most appropriate next step?",
   opts=[
     ["Order venous duplex ultrasonography to evaluate for deep venous thrombosis",
      "Correct. Acute unilateral swelling or pain should raise concern for deep venous thrombosis in this setting."],
     ["Increase the strength of her compression stockings",
      "Compressing a limb with a possible thrombosis before assessment is not the next step."],
     ["Begin a topical corticosteroid to the affected calf",
      "This addresses inflammation but not the acute unilateral change that needs excluding."],
     ["Reassure her that unilateral flares are expected in stasis dermatitis",
      "Acute unilateral change is precisely what should not be dismissed."]],
   c=0, cite=c(115)),

 dict(topic="Xerosis", io=IOC,
   q="An 80-year-old man reports generalised itching and rough, tight skin each winter, worst on the shins. Examination shows fine scale with a few shallow fissures and scratch marks, without erythematous plaques. Which is the most appropriate counselling point?",
   opts=[
     ["Take short lukewarm showers with a gentle fragrance-free cleanser only where needed, and apply a thick ointment or cream within minutes of bathing",
      "Correct — hot water and detergents are among the causes, and prompt moisturising after bathing is the key manoeuvre."],
     ["Take long hot showers to hydrate the skin, then moisturise once fully dry",
      "Hot water is a listed cause of xerosis, and the moisturiser must go on within minutes."],
     ["Use an antibacterial soap over the whole body twice daily",
      "Detergents contribute to the barrier impairment."],
     ["Apply a keratolytic containing urea to the fissured areas first",
      "Keratolytics can help hydration but may sting fissured skin, so they are not the opening advice."]],
   c=0, cite=c(153)),
]
