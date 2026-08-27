# -*- coding: utf-8 -*-
"""General Dermatology I -- question pool for the Updated CMS derm master exams.

Written to the reference-item pattern Jaxon supplied on 2026-08-26 (see
scratchpad/reference_questions.md): FIVE options, a vignette stem whose every
clause eliminates something, a per-option refutation, and citations to the slide
the fact actually came from. Jaquith's own knowledge-check slides (185-188 of
this deck) are five-option A-E vignettes, so the format matches the lecturer's.
"""
DECK = "2. General Dermatology I.pptx"
IO_A = "a — Review anatomy and physiology of the integumentary system"
IO_C = ("c — Compare and contrast the etiologies, epidemiology, risk factors, "
        "clinical manifestations, differential diagnosis, diagnostic testing, management, "
        "appropriate referrals, patient education, and prognosis of dermatological conditions")

def Q(topic, q, opts, c, slide, io=IO_C):
    return {"topic": topic, "io": io, "q": q, "opts": opts, "c": c,
            "cite": f"{DECK}, Slide {slide}"}

QUESTIONS = [

Q("Atopic dermatitis",
  "A 6-month-old girl is brought to the clinic by her father for a rash that has been present for three weeks. "
  "He reports she is difficult to settle at night and rubs her face against the bedsheet rather than scratching it. "
  "Her father has allergic rhinitis and her older brother has asthma. On examination there are weeping inflammatory "
  "patches and crusted plaques over both cheeks and the extensor surfaces of the forearms. The antecubital and "
  "popliteal fossae are clear. There is no fever, no purulent drainage, and no history of new detergents, soaps, or "
  "foods. What is the most likely diagnosis?",
  [["Atopic dermatitis, infantile pattern",
    "Correct. In infants atopic dermatitis produces weeping inflammatory patches and crusted plaques on the cheeks, "
    "scalp, and extensor surfaces, and rubbing commonly replaces scratching at this age. The family history of "
    "allergic rhinitis and asthma completes the atopic triad, and roughly 80 percent of patients have a personal or "
    "family history of atopy."],
   ["Atopic dermatitis, childhood pattern",
    "The condition is right but the pattern is wrong for the age. The childhood pattern is dry, ill-defined red "
    "plaques and scaly patches on flexural skin, particularly the antecubital and popliteal fossae — which this "
    "infant's examination specifically records as clear."],
   ["Allergic contact dermatitis",
    "Allergic contact dermatitis is a delayed type IV hypersensitivity reaction that produces a well-demarcated rash "
    "in the shape of the contactant at the site of exposure. The father denies new detergents, soaps, or foods, and "
    "a symmetric cheek-and-extensor distribution does not match any contact pattern."],
   ["Seborrheic dermatitis",
    "Seborrheic dermatitis affects sebum-rich sites and produces greasy, flaking, yellow scale over poorly demarcated "
    "erythematous plaques. The scalp is the characteristic site, and weeping, crusted extensor plaques with nocturnal "
    "pruritus are not its presentation."],
   ["Irritant contact dermatitis",
    "Irritant contact dermatitis follows a chemical or frictional exposure that disrupts the skin barrier and produces "
    "a glazed, sharply demarcated eruption limited to the contact site. No irritant exposure is reported, and the "
    "distribution here is symmetric rather than bounded by an exposure."]],
  0, 54),

Q("Atopic dermatitis",
  "A 7-year-old boy is seen for a recurrent, intensely pruritic rash. Examination shows poorly demarcated "
  "erythematous plaques with excoriations and lichenification of the antecubital and popliteal fossae. His mother "
  "reports a history of asthma. There is no fever, drainage, crusting, or tenderness. What is the most appropriate "
  "initial treatment?",
  [["A site-appropriate topical corticosteroid together with regular emollient use",
    "Correct. Treatment combines barrier repair with inflammation control: low to medium potency topical "
    "corticosteroid for the body, applied sparingly, with an emollient applied after rinsing. Neither element alone "
    "is adequate, which is what makes this the complete answer."],
   ["Regular emollient use alone, with corticosteroids reserved for failure",
    "Emollients are the foundation of barrier repair but do not control established inflammation. This child already "
    "has excoriated, lichenified plaques, so withholding an anti-inflammatory leaves the active disease untreated."],
   ["Oral cephalexin",
    "An oral antibiotic treats secondary bacterial infection, and the stem records no fever, drainage, crusting, or "
    "tenderness to suggest one. Treating an uninfected flare with an antibiotic exposes the child to a drug with no "
    "target."],
   ["Oral terbinafine",
    "Terbinafine is an antifungal used for dermatophyte infection, particularly where topical therapy is inadequate "
    "such as scalp or nail disease. A symmetric flexural eruption in an atopic child is not a dermatophytosis."],
   ["Systemic prednisone",
    "Systemic corticosteroids are reserved for severe disease and carry rebound and growth concerns in children. "
    "Escalating to a systemic agent before a site-appropriate topical has been tried is treating above the severity "
    "the examination shows."]],
  0, 57),

Q("Nummular eczema",
  "A 58-year-old man presents with several intensely itchy patches on his lower legs that appeared over two months. "
  "Examination shows multiple well-demarcated, coin-shaped erythematous plaques 1 to 5 cm in diameter scattered over "
  "both thighs and lower legs, with prominent scale and crusting. Each plaque is uniform in appearance throughout. "
  "What single examination finding most strongly separates this from the principal alternative diagnosis?",
  [["The plaques are uniform throughout, without central clearing",
    "Correct. The main differential is tinea corporis, and the slide draws the line exactly here: tinea corporis has "
    "central clearing and nummular eczema does not. Uniform appearance across the whole plaque is what makes this "
    "nummular eczema."],
   ["The plaques are round rather than irregular in outline",
    "A round or coin-shaped outline is what gives nummular eczema its name, but tinea corporis is also round — "
    "its lesions are classically annular. Shape alone is shared by both and therefore separates neither."],
   ["The plaques are located on the extremities rather than the trunk",
    "Nummular eczema is most commonly seen on the extremities, but it can be seen on the trunk, and tinea corporis "
    "occurs on the extremities freely. Site narrows the differential slightly but does not decide it."],
   ["The plaques are intensely pruritic rather than painless",
    "Nummular eczema is intensely pruritic, but so is tinea corporis, and pruritus is among the least discriminating "
    "findings in dermatology. An itch shared by both diagnoses cannot choose between them."],
   ["The plaques are well demarcated rather than poorly demarcated",
    "Well-demarcated borders are recorded here and are typical, but tinea corporis is also well demarcated at its "
    "advancing edge. Demarcation describes the lesion without distinguishing these two."]],
  0, 73),

Q("Dyshidrotic eczema",
  "A 29-year-old hairdresser reports recurrent episodes of intensely itchy blisters on her hands. Examination shows "
  "multiple grouped 1 to 2 mm vesicles on the lateral aspects of the fingers and the adjacent interdigital surfaces, "
  "some coalescing, on a poorly defined pink base with surrounding dryness. She reports previous episodes that "
  "persisted for several weeks, dried up, and then peeled. What is the most likely diagnosis?",
  [["Dyshidrotic eczema",
    "Correct. Dyshidrotic eczema is a chronic, relapsing eruption of intensely pruritic vesicles on the hands and "
    "feet, classically described as tapioca vesicles. They may coalesce into bullae, persist for several weeks, then "
    "desiccate and resolve with desquamation — the exact course she describes."],
   ["Allergic contact dermatitis",
    "Allergic contact dermatitis is plausible in a hairdresser exposed to dyes, but it produces a well-demarcated "
    "eruption at the site of allergen contact rather than grouped tapioca vesicles confined to the lateral fingers "
    "and interdigital surfaces with a relapsing weeks-long cycle."],
   ["Irritant contact dermatitis",
    "Irritant contact dermatitis from frequent hand washing produces a glazed, well-demarcated eruption with erythema "
    "and scaling on the hands and forearms. It does not typically produce crops of deep-seated vesicles that "
    "desiccate and desquamate over weeks."],
   ["Nummular eczema",
    "Nummular eczema produces well-demarcated coin-shaped plaques 1 to 10 cm across, most often on the extremities, "
    "with prominent scale and crusting. Its lesions are plaques rather than grouped millimetre vesicles on the "
    "finger margins."],
   ["Atopic dermatitis of the hands",
    "Adult atopic dermatitis does affect the hands, but it produces dry, lichenified plaques at flexures, hands, and "
    "neck rather than recurrent crops of vesicles on the lateral fingers that resolve by desquamation."]],
  0, 65),

Q("Irritant contact dermatitis",
  "A 41-year-old janitorial supervisor reports several weeks of progressively dry, sore hands. She washes her hands "
  "frequently and handles detergents and cleaning solutions throughout her shift. Examination shows a glazed, "
  "well-demarcated erythematous eruption with scaling over the dorsal hands and distal forearms, ending abruptly at "
  "the wrists. She denies any new jewellery, gloves, cosmetics, or topical products, and patch testing performed "
  "previously was negative. What is the most likely diagnosis?",
  [["Irritant contact dermatitis",
    "Correct. Irritant contact dermatitis is the most common form of contact dermatitis and results from chemicals or "
    "friction that disrupt the skin barrier. It is frequently occupational, with healthcare and janitorial workers "
    "cited as the classic examples, and mild irritants such as soaps produce subacute symptoms progressing over "
    "weeks. Hands and forearms are the commonest sites."],
   ["Allergic contact dermatitis",
    "Allergic contact dermatitis is a delayed type IV hypersensitivity reaction to a specific allergen, and patch "
    "testing is the test that diagnoses it. Her patch testing was negative and she denies any new gloves, jewellery, "
    "or topical products, which removes the allergen this diagnosis requires."],
   ["Atopic dermatitis of the hands",
    "Adult atopic dermatitis affects the hands, but it requires a personal or family history of atopy and produces "
    "poorly demarcated lichenified plaques. The sharply demarcated, glazed eruption ending at the wrists follows an "
    "exposure boundary rather than an atopic distribution."],
   ["Dyshidrotic eczema",
    "Dyshidrotic eczema produces crops of intensely pruritic deep-seated vesicles on the palms, lateral fingers, and "
    "soles that desiccate and desquamate over weeks. There are no vesicles here, and the eruption is on the dorsal "
    "rather than palmar surface."],
   ["Cutaneous candidiasis",
    "Cutaneous candidiasis favours warm, moist, occluded sites and produces beefy erythema with satellite papules "
    "and pustules. A dry, glazed, scaling eruption on exposed dorsal hands is not a candidal distribution or "
    "morphology."]],
  0, 80),

Q("Allergic contact dermatitis",
  "A 19-year-old man presents two days after clearing brush at a summer job. He reports intense itching. Examination "
  "shows erythematous papules, vesicles, and a few small bullae arranged in linear streaks across the forearms and "
  "one calf, with excoriation between them. Some lesions appear newer than others. He is afebrile and the rash does "
  "not cross the midline of the trunk or follow a single band. What feature of the eruption best supports the "
  "diagnosis?",
  [["The linear arrangement of the lesions",
    "Correct. Urushiol sap from Toxicodendron species produces intensely pruritic vesicular lesions in linear "
    "distributions, because the streaks mark where the plant grazed the skin in passing. Lesions erupt within 4 to "
    "96 hours and may appear in multiple stages, as they do here."],
   ["The presence of vesicles and bullae",
    "Vesicles and bullae are seen in this eruption, but they are shared with many blistering conditions including "
    "dyshidrotic eczema, bullous pemphigoid, and herpes zoster. The morphology alone does not point to a plant "
    "exposure."],
   ["The intensity of the pruritus",
    "The itch is severe and typical, but intense pruritus accompanies atopic dermatitis, nummular eczema, lichen "
    "planus, and scabies equally. A symptom this common across dermatology cannot carry a specific diagnosis."],
   ["The presence of excoriation between lesions",
    "Excoriation records that the patient has been scratching and is expected with any intensely pruritic eruption. "
    "It is a secondary change produced by the patient rather than a feature of the underlying disease."],
   ["The onset within two days of the exposure",
    "The timing is compatible, since lesions erupt within 4 to 96 hours, but a two-day interval also fits an irritant "
    "reaction, an arthropod assault, or a drug eruption. Timing supports the diagnosis without being the feature that "
    "identifies it."]],
  0, 87),

Q("Allergic contact dermatitis",
  "A 24-year-old woman presents with an itchy rash on her forearm. She had a laceration dressed with an adhesive "
  "bandage four days ago. Examination shows a sharply demarcated rectangular erythematous plaque with tiny vesicles "
  "corresponding exactly to the adhesive portions of the dressing, and a rectangle of normal skin in the centre where "
  "the cotton pad had lain. The laceration itself is clean and healing. What is the most likely diagnosis?",
  [["Allergic contact dermatitis to the adhesive",
    "Correct. Patients allergic to the adhesive in an adhesive bandage present with a bandage-shaped rash that spares "
    "the middle area where the cotton lay. The eruption reproduces the shape of the contactant, which is the "
    "signature of allergic contact dermatitis."],
   ["Wound infection of the underlying laceration",
    "A wound infection would centre on the laceration itself with surrounding warmth, tenderness, and purulence. The "
    "laceration here is clean and healing, and the reaction is confined to skin the adhesive touched while sparing "
    "the wound."],
   ["Irritant contact dermatitis from the wound cleanser",
    "An irritant reaction from a cleanser applied to the wound would be maximal over the wound and its immediate "
    "margin. It would not reproduce the adhesive geometry with a rectangle of spared skin at the centre."],
   ["Herpes simplex virus reactivation",
    "Herpes simplex produces grouped vesicles on an erythematous base that progress to pustules and painful erosions "
    "at a fixed site. It does not lay itself out in a rectangle matching a dressing, and the lesion here is pruritic "
    "rather than painful."],
   ["Cellulitis of the forearm",
    "Cellulitis produces poorly demarcated erythema with warmth, tenderness, and often fever, spreading outward "
    "without regard to what was taped to the skin. Sharp adhesive-shaped borders with central sparing exclude it."]],
  0, 86),

Q("Seborrheic dermatitis",
  "A 34-year-old man presents with recurrent pruritic scaling of the scalp, eyebrows, nasolabial folds, and external "
  "ears. Examination demonstrates greasy, yellow-white scale over mildly erythematous, poorly demarcated patches. He "
  "reports the itching is worse when he sweats. What is the most appropriate initial treatment?",
  [["Ketoconazole shampoo for the scalp and topical ketoconazole cream for the face",
    "Correct. Seborrheic dermatitis is caused by overgrowth of Malassezia, a normal skin flora organism, so topical "
    "antifungals are the mainstay. Antifungal shampoos such as ketoconazole and selenium sulfide are used on the "
    "scalp and antifungal creams or lotions on the face."],
   ["A high-potency topical corticosteroid to both the scalp and the face",
    "Steroids are used in the early stages to reduce the inflammatory response, but high-potency agents are not the "
    "initial choice and are specifically hazardous on facial skin, where prolonged use causes atrophy, telangiectasia, "
    "and perioral dermatitis."],
   ["Oral terbinafine",
    "Terbinafine is effective against dermatophytes, whereas seborrheic dermatitis is driven by the yeast Malassezia. "
    "Systemic therapy is also unnecessary for a condition that responds to topical antifungals applied to accessible "
    "surfaces."],
   ["Oral doxycycline",
    "Doxycycline treats inflammatory acneiform and bacterial disease such as rosacea or perioral dermatitis. There is "
    "no bacterial component here, and greasy yellow scale at sebum-rich sites is not an acneiform eruption."],
   ["Topical mupirocin",
    "Mupirocin is a topical antibacterial used for impetigo and localised staphylococcal infection. Seborrheic "
    "dermatitis is neither bacterial nor impetiginised in this presentation, so an antibacterial has no target."]],
  0, 95),

Q("Perioral dermatitis",
  "A 27-year-old woman presents with burning and small erythematous papules around her mouth. Examination demonstrates "
  "grouped monomorphic papules and papulopustules involving the nasolabial folds and chin, with a narrow zone of "
  "sparing immediately adjacent to the vermilion border. There are no open or closed comedones. She has applied "
  "hydrocortisone cream to her face daily for several months. What is the most appropriate initial management?",
  [["Discontinue the topical corticosteroid and simplify the skin-care routine, warning her the eruption may "
    "temporarily worsen",
    "Correct. Topical corticosteroid exposure is the most important modifiable association, so facial steroids should "
    "be discontinued because continued exposure perpetuates the condition. Patients must be told the eruption may "
    "temporarily worsen after withdrawal, or they will restart the steroid when it does."],
   ["Discontinue the topical corticosteroid and reassure her that no flare should be expected",
    "Stopping the steroid is right, but the counselling is wrong and the error is consequential. Patients not warned "
    "about the post-withdrawal flare interpret it as treatment failure and resume the corticosteroid, which restarts "
    "the cycle the withdrawal was meant to break."],
   ["Increase the potency of the topical corticosteroid",
    "This intensifies the exposure that is driving the eruption. It may briefly suppress the papules, which makes it "
    "seductive, but it perpetuates the condition and adds atrophy, striae, and telangiectasia to the facial skin."],
   ["Begin topical adapalene and continue the hydrocortisone",
    "A retinoid targets comedonal acne, and the examination specifically records no open or closed comedones. "
    "Continuing the corticosteroid also leaves the principal driver of the eruption in place."],
   ["Begin oral isotretinoin",
    "Isotretinoin is reserved for severe nodulocystic acne and carries teratogenicity requiring pregnancy prevention. "
    "Escalating to it before simply removing the offending topical steroid treats far above the severity of the "
    "disease."]],
  0, 102),

Q("Diaper dermatitis",
  "A 9-month-old boy is brought in for a diaper rash of one week. Examination shows beefy erythema involving the "
  "inguinal folds, with peripheral scale and several small papules and pustules on the thighs a short distance beyond "
  "the main area of redness. He completed a course of amoxicillin two weeks ago. What finding most strongly indicates "
  "the infectious complication rather than simple irritant disease?",
  [["Involvement of the inguinal folds with satellite lesions beyond the main area",
    "Correct. Whether the skin folds are involved is the finding that distinguishes irritant from candidal disease. "
    "Irritant diaper dermatitis affects the convex surfaces and generally spares the inguinal folds because they are "
    "less exposed to urine and feces; candidal disease produces beefy erythema in the folds with satellite papules "
    "and pustules."],
   ["The presence of erythema in the diaper area",
    "Erythema is common to every form of diaper dermatitis and is the reason the child presented. A finding shared by "
    "the irritant and candidal forms alike cannot separate them."],
   ["The recent course of amoxicillin",
    "Antibiotic exposure genuinely raises the risk and belongs in the history, but it is a risk factor rather than a "
    "physical finding. Plenty of infants develop irritant dermatitis after antibiotics without any candidal "
    "component."],
   ["The presence of scaling at the edge of the eruption",
    "Peripheral scale accompanies candidal disease, but scaling is also produced by irritant dermatitis, which causes "
    "erythema, scaling, papules, or erosions. On its own it does not identify the organism."],
   ["The one-week duration of the eruption",
    "A week is unremarkable for either form. Duration would matter if the question were whether to reassess a "
    "treatment failure, but it does not identify a candidal complication."]],
  0, 107),

Q("Diaper dermatitis",
  "A 7-month-old girl has a diaper rash confined to the convex surfaces of the buttocks and upper thighs, with the "
  "inguinal folds clearly spared. There are no satellite lesions, no bullae, and no purulent drainage. Her mother "
  "reports frequent loose stools over the past week. What is the most appropriate initial management?",
  [["Frequent diaper changes with gentle cleansing and a thick zinc oxide or petrolatum barrier at every change",
    "Correct. The foundation of treatment is reducing exposure to moisture and irritants through frequent changes, "
    "gentle cleansing, air exposure, and superabsorbent diapers, with a thick barrier layer applied at each change. "
    "The previous layer need not be scrubbed away if it remains clean."],
   ["A topical antifungal applied at every diaper change",
    "An antifungal targets the candidal form, which is identified by fold involvement and satellite lesions. This "
    "examination records spared folds and no satellite lesions, so the drug has no target."],
   ["A high-potency topical corticosteroid twice daily until clear",
    "Only a brief course of a low-potency corticosteroid is appropriate for significant inflammation, and then under "
    "clinician guidance. High-potency steroids under an occlusive diaper risk atrophy and systemic absorption in an "
    "infant."],
   ["Oral cephalexin",
    "A systemic antibiotic addresses bacterial infection, which is suggested by bullae, crusting, or purulent "
    "drainage — all specifically absent here. Treating uncomplicated irritant dermatitis with an oral antibiotic "
    "exposes the infant to a drug with nothing to treat."],
   ["Leaving the diaper off entirely until the rash resolves",
    "Air exposure is one useful component of care, but it is neither practical as sole management nor sufficient by "
    "itself. It also omits the barrier preparation that protects the damaged epidermis from further urine and stool "
    "contact."]],
  0, 109),

Q("Stasis dermatitis",
  "A 68-year-old woman presents with chronic bilateral lower-leg swelling, pruritus, and skin discoloration. "
  "Examination demonstrates poorly demarcated erythematous plaques, pitting edema, and brown hyperpigmentation around "
  "both medial ankles. Pedal pulses are diminished. What is the most appropriate next step before prescribing "
  "compression therapy?",
  [["Perform an ankle-brachial index",
    "Correct. Compression is the cornerstone of management only once adequate arterial circulation has been "
    "established. An ankle-brachial index or toe pressure should be obtained when peripheral arterial disease is "
    "suspected — as the diminished pulses here suggest — before initiating substantial compression."],
   ["Obtain a bacterial wound culture",
    "A culture is indicated when infection is suspected, and no ulcer, purulence, warmth, or fever is described. It "
    "also would not answer the question the diminished pulses raise, which is whether compression is safe."],
   ["Order patch testing",
    "Patch testing diagnoses allergic contact dermatitis, which is worth considering in chronically treated legs but "
    "is not the priority. It does not establish arterial status, and compression would still be unsafe if arterial "
    "disease were present."],
   ["Begin oral cephalexin",
    "Cephalexin treats cellulitis, and the chief clinical priority in this presentation is distinguishing stasis "
    "dermatitis from cellulitis — bilateral, chronic, pruritic, hyperpigmented disease is stasis dermatitis, not "
    "infection."],
   ["Perform a skin biopsy",
    "Biopsy is reserved for atypical or diagnostically uncertain disease and would delay care in a presentation that "
    "is clinically characteristic. It also leaves the arterial question that governs compression safety unanswered."]],
  0, 116),

Q("Stasis dermatitis",
  "A 72-year-old man is referred with a red, warm, tender left lower leg. He has bilateral chronic ankle swelling and "
  "brown discoloration of both gaiter regions, but the left leg has become acutely more swollen and painful over two "
  "days. He is afebrile. What consideration should most urgently shape the evaluation?",
  [["Acute unilateral swelling or pain should raise concern for deep venous thrombosis",
    "Correct. The differential for stasis dermatitis explicitly flags that acute unilateral swelling or pain should "
    "raise concern for deep venous thrombosis. Chronic bilateral changes with a new unilateral acute change is "
    "precisely that pattern."],
   ["Bilateral involvement makes cellulitis the most likely explanation",
    "This inverts the reasoning. Bilateral chronic change argues against cellulitis, which is characteristically "
    "unilateral; distinguishing stasis dermatitis from cellulitis is one of the two primary clinical priorities in "
    "this condition."],
   ["Absence of fever excludes an acute vascular event",
    "Fever is neither required for nor exclusive to venous thrombosis, and this patient is indeed afebrile. Using a "
    "normal temperature to rule out a thrombotic event would be a serious error."],
   ["The brown discoloration indicates active infection requiring culture",
    "Brown discoloration is hemosiderin deposition from chronic capillary leakage, a marker of long-standing venous "
    "disease rather than infection. It is a chronic finding and says nothing about the acute change."],
   ["Compression therapy should be started immediately to relieve the swelling",
    "Starting compression before excluding deep venous thrombosis and confirming arterial adequacy is exactly the "
    "sequence the lecture warns against. Compression is the cornerstone of management only after those questions are "
    "settled."]],
  0, 115),

Q("Bullous pemphigoid",
  "A 74-year-old man presents with a two-month history of intense itching followed by blistering. Examination shows "
  "numerous 1 to 3 cm tense, firm bullae on the trunk, flexural surfaces of the arms, and the axillary and inguinal "
  "folds. Rubbing the skin adjacent to a blister does not cause the epidermis to slough. There is a single small "
  "erosion in the mouth. What is the most likely diagnosis?",
  [["Bullous pemphigoid",
    "Correct. Bullous pemphigoid damages the epithelial basement membrane, producing subepithelial blistering, and "
    "classically presents after age 60 with tense 1 to 3 cm bullae on the trunk, extremity flexures, and axillary and "
    "inguinal folds. A pruritic prodrome may precede the bullae by weeks to months, and Nikolsky's sign is negative."],
   ["Pemphigus vulgaris",
    "Pemphigus produces flaccid bullae that rupture easily, leaving painful bleeding erosions, and Nikolsky's sign is "
    "positive. This patient's bullae are tense and firm and the skin does not slough on rubbing, which is the "
    "distinction the comparison table draws."],
   ["Dermatitis herpetiformis",
    "Dermatitis herpetiformis produces intensely pruritic grouped vesicles and papules on extensor surfaces such as "
    "elbows, knees, and buttocks. It does not produce large tense bullae in flexural and intertriginous distribution "
    "in an elderly man."],
   ["Erythema multiforme",
    "Erythema multiforme produces targetoid lesions with a characteristic concentric appearance, typically acrally "
    "distributed and often following an infection. Numerous large tense bullae confined to trunk and flexures are not "
    "its morphology."],
   ["Bullous impetigo",
    "Bullous impetigo occurs chiefly in children and produces flaccid, superficial bullae that rupture to leave a "
    "collarette of scale and honey-coloured crust. It is a superficial bacterial infection rather than a subepithelial "
    "autoimmune blistering disease."]],
  0, 123),

Q("Pemphigus",
  "A 52-year-old woman of Mediterranean descent presents with painful mouth erosions that began three months ago, "
  "followed by skin lesions. Examination shows flaccid bullae and widespread crusted erosions on the scalp, chest, "
  "axillae, and groin that bleed easily and are painful. Lateral pressure on normal-appearing skin causes the "
  "superficial layers to slip away. What does the biopsy most likely demonstrate?",
  [["Acantholysis, with intraepithelial blister formation",
    "Correct. Pemphigus is characterised by loss of keratinocyte-to-keratinocyte adhesion, termed acantholysis, "
    "producing intraepithelial blisters. The oral onset, flaccid easily ruptured bullae, and positive Nikolsky's sign "
    "all identify pemphigus, and biopsy demonstrating acantholysis is the diagnostic finding."],
   ["Subepithelial blistering without acantholysis",
    "This is the bullous pemphigoid pattern, and the comparison table pairs it with tense firm blisters and a "
    "negative Nikolsky's sign. This patient has flaccid bullae and a positive Nikolsky's sign, which is the opposite "
    "half of that table."],
   ["Neutrophils aligned in a straight narrow row at the dermal-epidermal junction",
    "That light-microscopy description belongs to bullous pemphigoid. It is a real finding but attached to the wrong "
    "disease for a patient with oral-onset flaccid bullae and epidermal slippage on pressure."],
   ["Granular immunoglobulin A deposits at the tips of the dermal papillae",
    "Granular immunoglobulin A at the papillary tips is the direct immunofluorescence finding of dermatitis "
    "herpetiformis, which presents with grouped pruritic vesicles on extensor surfaces rather than painful oral "
    "erosions and flaccid bullae."],
   ["Band-like lymphocytic infiltration of the upper dermis",
    "A band-like lymphocytic infiltrate is the histological signature of lichen planus, which presents with pruritic "
    "purple polygonal papules rather than a blistering disorder with mucosal onset."]],
  0, 132),

Q("Pemphigus",
  "A 49-year-old man is admitted with extensive flaccid bullae and painful erosions involving the mouth, chest, and "
  "groin. Biopsy demonstrates acantholysis and immunofluorescence confirms pathogenic antibodies. What is the most "
  "appropriate initial management?",
  [["Urgent treatment with rituximab or high-dose oral prednisone",
    "Correct. Pemphigus is a life-threatening blistering disorder requiring urgent treatment, initially rituximab or "
    "high-dose oral prednisone. When steroids are used they are usually paired with a steroid-sparing agent such as "
    "azathioprine or mycophenolate so the patient can eventually be transitioned off."],
   ["Ultrapotent topical corticosteroids alone",
    "Ultrapotent topical steroids are the treatment for mild bullous pemphigoid, a relatively benign disease. Applying "
    "that approach to extensive life-threatening pemphigus with mucosal involvement under-treats a condition that "
    "requires urgent systemic therapy."],
   ["Oral doxycycline with nicotinamide",
    "Doxycycline is an option in moderate bullous pemphigoid, where it is weighed against oral prednisone. It is not "
    "adequate primary therapy for extensive pemphigus, which needs immediate immunosuppression."],
   ["Dapsone as single-agent therapy",
    "Dapsone is described as particularly effective where there is mucous membrane involvement, so it is not "
    "irrelevant here, but it is an adjunct rather than the initial treatment for extensive life-threatening disease."],
   ["Low-dose methotrexate with folic acid supplementation",
    "Low-dose methotrexate with folic acid is described as safe and effective in elderly patients with bullous "
    "pemphigoid, and appears among immunosuppressive options for refractory disease. It is not the urgent first "
    "treatment for extensive pemphigus."]],
  0, 133),

Q("Alopecia areata",
  "A 23-year-old woman presents with the sudden appearance of two smooth, round bald patches on her scalp, each about "
  "3 cm across, that developed over three weeks. The underlying scalp is smooth without scaling, erythema, or "
  "scarring. Short hairs that are narrow at the root and normal in calibre at the tip are visible at the margins. She "
  "has a history of eczema and her mother has hypothyroidism. What finding is pathognomonic for the diagnosis?",
  [["Exclamation point hairs at the margins of the patches",
    "Correct. Exclamation point hairs are pathognomonic for alopecia areata. Their growth ability is changing in real "
    "time, which produces a hair that is thinner at the root but normal in calibre at the top — exactly the "
    "description given here."],
   ["The round shape of the areas of hair loss",
    "The areas of hair loss are often round and the scalp is often very smooth, which is typical, but roundness is "
    "also seen in tinea capitis and in traction and trichotillomania patterns. Typical is not the same as "
    "pathognomonic."],
   ["The absence of scarring at the affected sites",
    "Absence of scarring is important because the inflammatory cells do not destroy the stem cell compartment, which "
    "is why the balding is non-permanent. But every non-scarring alopecia shares this feature, including "
    "androgenetic alopecia and telogen effluvium."],
   ["The personal history of atopy and family history of autoimmune disease",
    "Risk is genuinely increased with family history, atopy, and autoimmune disease, so these details support the "
    "diagnosis. Risk factors raise the pretest probability but are never pathognomonic for anything."],
   ["The sudden onset over three weeks",
    "Sudden onset of 1 to 4 cm patches is characteristic, but abrupt hair loss also occurs in telogen effluvium and "
    "in traumatic alopecias. Tempo narrows the differential without identifying the disease."]],
  0, 138),

Q("Alopecia areata",
  "An 8-year-old boy has three smooth, non-scarring patches of hair loss on the scalp with exclamation point hairs at "
  "the margins and fine pitting of several fingernails. A potassium hydroxide preparation of plucked hairs is "
  "negative. What is the most appropriate first-line treatment?",
  [["Topical corticosteroids",
    "Correct. Topical steroids are first line in children 10 years old and younger. The child is 8, which places him "
    "in that group and avoids the discomfort of intralesional injection in a young child."],
   ["Intralesional corticosteroids",
    "Intralesional steroids are first line in adolescents and adults. They are the right drug class delivered by the "
    "wrong route for this age group, which is why this is the most tempting wrong answer."],
   ["Oral terbinafine",
    "Terbinafine treats tinea capitis, the principal alternative cause of patchy childhood hair loss, and the "
    "negative potassium hydroxide preparation together with a smooth non-scaling scalp argues against it. "
    "Exclamation point hairs and nail pitting point elsewhere."],
   ["Topical minoxidil",
    "Minoxidil is used in androgenetic alopecia, where it prevents further loss and is primarily effective in the "
    "crown region. It is not the first-line treatment for an autoimmune non-scarring patchy alopecia in a child."],
   ["Oral prednisone",
    "A systemic corticosteroid escalates well beyond what limited patchy disease requires and carries growth and "
    "adrenal considerations in a child. Topical therapy is the stated first line at this age."]],
  0, 140),

Q("Androgenetic alopecia",
  "A 46-year-old woman reports gradual hair thinning over several years. Examination shows diffuse thinning across "
  "the central and parietal scalp with preservation of the frontal hairline. There are no bald patches, no scaling, "
  "no scarring, and no exclamation point hairs. Several of her male relatives began balding in their twenties. What "
  "is the most likely diagnosis?",
  [["Female-pattern hair loss",
    "Correct. Female-pattern hair loss produces diffuse thinning of the central and parietal scalp without "
    "significant change to the frontal hairline. There is an increased frequency of balding among first-degree male "
    "relatives, which the family history here supplies."],
   ["Male-pattern hair loss",
    "Male-pattern hair loss begins with recession of the frontal hairline in a triangular frontotemporal pattern "
    "followed by vertex loss. This patient's frontal hairline is specifically preserved, which is the finding that "
    "separates the two patterns."],
   ["Alopecia areata",
    "Alopecia areata produces sudden, round, smooth 1 to 4 cm patches with exclamation point hairs, all of which are "
    "recorded as absent. It is patchy and abrupt rather than diffuse and gradual."],
   ["Tinea capitis",
    "Tinea capitis produces scaling, broken hairs, and often inflammation of the scalp, and is predominantly a "
    "condition of children. The examination records no scaling and the pattern is a diffuse adult thinning."],
   ["Lichen planopilaris",
    "Scarring alopecias destroy the follicle and leave loss of follicular openings with scarring. The examination "
    "specifically records no scarring, and the distribution follows a recognised androgenetic pattern instead."]],
  0, 146),

Q("Androgenetic alopecia",
  "A 31-year-old man with progressive frontotemporal recession and early vertex thinning asks about treatment. He and "
  "his partner are not planning a pregnancy and he has no contraindications. Which statement about the two principal "
  "medical therapies is correct?",
  [["Finasteride is an oral 5-alpha-reductase type 2 inhibitor and works best in combination with topical minoxidil",
    "Correct. Finasteride prevents further hair loss and may provide some regrowth, and works best in combination "
    "with minoxidil. Dihydrotestosterone is the androgen chiefly responsible for the follicular miniaturisation, "
    "which is what the enzyme inhibition addresses."],
   ["Finasteride is a topical agent and minoxidil is the oral component of combination therapy",
    "The routes are reversed. Minoxidil is the topically applied agent and finasteride is the oral one, so a patient "
    "given this advice would apply and swallow the wrong drugs."],
   ["Minoxidil is primarily effective at the frontal hairline rather than the crown",
    "The region is wrong. Minoxidil prevents further loss and may lead to regrowth but is primarily effective in the "
    "crown region of the scalp, which is the opposite of what this states."],
   ["The sexual adverse effects reported with finasteride are permanent once they occur",
    "About 2 percent of men taking finasteride report decreased libido and erectile function, but these effects are "
    "reversible when the drug is stopped. Telling a patient they are permanent would wrongly deter effective "
    "treatment."],
   ["Neither agent alters the course of the condition, so no medical therapy should be offered",
    "Both agents prevent further hair loss and may produce some regrowth. Withholding effective therapy from a "
    "patient who has asked for it is not supported by the evidence presented in the lecture."]],
  0, 148),
]

QUESTIONS += [

Q("Psoriasis",
  "A 38-year-old man presents with thick scaly plaques on both elbows and knees that have been present for years. "
  "Examination shows well-demarcated salmon-pink plaques with adherent silvery scale over the extensor elbows and "
  "knees, the sacrum, and the scalp. A linear plaque has developed along a surgical scar on his forearm. When scale "
  "is lifted from one plaque, pinpoint bleeding appears. What is this bleeding phenomenon called?",
  [["Auspitz sign",
    "Correct. Auspitz sign is the appearance of bleeding when scale is removed from a psoriatic plaque, produced by "
    "the dilated capillaries lying immediately beneath a thinned suprapapillary epidermis."],
   ["Koebner phenomenon",
    "Koebner phenomenon is also present in this patient — it is the development of lesions at sites of trauma, which "
    "is what the linear plaque along the surgical scar represents. But it describes the scar lesion, not the "
    "bleeding on scale removal."],
   ["Nikolsky sign",
    "Nikolsky sign is the slipping away of the top layers of skin from the lower layers when rubbed, and it is "
    "positive in pemphigus and negative in bullous pemphigoid. It involves epidermal separation rather than pinpoint "
    "bleeding from a descaled plaque."],
   ["Darier sign",
    "Darier sign is urtication and erythema of a lesion after it is stroked, seen in mastocytosis. It produces a "
    "wheal rather than bleeding, and it is not a feature of psoriasis."],
   ["Wickham striae",
    "Wickham striae are the fine white lines visible on the surface of lichen planus plaques. They are a surface "
    "pattern seen without any manipulation, not a response to removing scale."]],
  0, 159),

Q("Psoriasis",
  "A 9-year-old girl develops an abrupt eruption of numerous small raindrop-shaped scaly papules and plaques over the "
  "trunk and proximal limbs. Her mother reports she was treated for a sore throat about two and a half weeks ago. "
  "She is otherwise well. What is the most appropriate management?",
  [["Reassurance, with phototherapy or topical steroids only if needed",
    "Correct. Guttate psoriasis presents as raindrop-shaped erythematous papules and plaques, typically in children "
    "2 to 3 weeks following a streptococcal infection or upper respiratory infection. No treatment is needed, though "
    "phototherapy and topical steroids may be used."],
   ["Systemic corticosteroids tapered over four weeks",
    "Systemic steroids are specifically hazardous in psoriasis: pustular psoriasis may follow systemic steroid "
    "withdrawal, and that form is abrupt and life-threatening. Prescribing them here risks converting a self-limited "
    "eruption into a dangerous one."],
   ["Oral methotrexate",
    "Methotrexate belongs to moderate-to-severe disease or to plaque psoriasis that has failed topical therapy. "
    "Committing a child with a self-limited post-streptococcal eruption to an antimetabolite is treating far above "
    "the disease."],
   ["Oral acitretin",
    "Acitretin is used in pustular psoriasis and moderate-to-severe disease, and it is contraindicated in pregnancy "
    "with a prolonged period of concern afterwards. It is not indicated for guttate disease in a child."],
   ["Topical mupirocin to the affected areas",
    "Mupirocin is a topical antibacterial. The streptococcal infection that triggered this eruption was in the "
    "throat and has already been treated; the skin lesions are an immune-mediated psoriatic response rather than a "
    "cutaneous bacterial infection."]],
  0, 164),

Q("Psoriasis",
  "A 44-year-old woman with a history of plaque psoriasis was given a two-week course of oral prednisone by an urgent "
  "care clinician for back pain. Four days after finishing it she develops fever lasting several days followed by the "
  "sudden appearance of widespread sheets of small pustules on erythematous skin. She appears unwell. What has most "
  "likely occurred?",
  [["Pustular psoriasis precipitated by systemic steroid withdrawal",
    "Correct. Pustular psoriasis of von Zumbusch type is a rare, severe form associated with other forms of psoriasis "
    "and may follow systemic steroid withdrawal. It is abrupt and life-threatening, begins with several days of "
    "fever, and is commonly mistaken for bacterial or viral infection."],
   ["A widespread bacterial skin infection",
    "This is the mistake the lecture warns about explicitly: pustular psoriasis is commonly mistaken for bacterial or "
    "viral infection. The context of pre-existing psoriasis and recent systemic steroid withdrawal identifies the "
    "true cause."],
   ["Guttate psoriasis triggered by the steroid course",
    "Guttate psoriasis is raindrop-shaped papules and plaques following streptococcal or upper respiratory infection, "
    "typically in children, and it is not febrile or life-threatening. Sheets of pustules with fever are a different "
    "entity."],
   ["Acute generalised exanthematous pustulosis from the prednisone",
    "A drug-induced pustular eruption is a reasonable thought, but the temporal relationship here is to steroid "
    "withdrawal rather than to steroid exposure, and the patient's established psoriasis supplies the substrate "
    "pustular psoriasis requires."],
   ["Impetigo herpetiformis",
    "Impetigo herpetiformis is the pustular psoriasis of pregnancy, occurring typically in the third trimester with "
    "erythematous patches whose margins are studded with subcorneal pustules. Nothing indicates this patient is "
    "pregnant."]],
  0, 160),

Q("Psoriasis",
  "A 30-year-old woman in her third trimester develops erythematous patches whose margins are studded with small "
  "pustules, accompanied by fever, chills, malaise, diarrhea, nausea, and joint pains. What is the most likely "
  "diagnosis?",
  [["Impetigo herpetiformis",
    "Correct. Impetigo herpetiformis is the psoriasis of pregnancy, occurring typically in the third trimester with "
    "erythematous patches whose margins are studded with subcorneal pustules. Onset is accompanied by fever, chills, "
    "malaise, diarrhea, nausea, and arthralgia."],
   ["Impetigo",
    "Despite the similar name, impetigo is a superficial bacterial infection producing honey-coloured crusts, most "
    "often around the nose and mouth in children. It does not produce systemic symptoms of this kind or a "
    "pustule-studded advancing margin in a pregnant woman."],
   ["Pemphigoid gestationis",
    "Pemphigoid gestationis is a pregnancy-associated blistering disease that typically begins periumbilically with "
    "urticarial lesions progressing to tense bullae. Its lesions are bullae rather than margins studded with "
    "subcorneal pustules."],
   ["Guttate psoriasis",
    "Guttate psoriasis produces raindrop-shaped papules and plaques following streptococcal or upper respiratory "
    "infection, typically in children, and it does not produce fever, gastrointestinal symptoms, and arthralgia."],
   ["Generalised candidiasis",
    "Cutaneous candidiasis favours warm, moist, occluded sites and produces beefy erythema with satellite pustules. "
    "It does not produce a systemically unwell pregnant patient with pustules studding the margins of erythematous "
    "patches."]],
  0, 161),

Q("Psoriasis",
  "A 36-year-old man with plaque psoriasis reports painful, stiff finger joints. He describes more than thirty "
  "minutes of morning stiffness that improves as he uses his hands during the day. Examination shows diffuse swelling "
  "of the entire second and third digits of the right hand. What additional finding is most characteristic of the "
  "associated condition?",
  [["Association with human leukocyte antigen B27",
    "Correct. Psoriatic arthritis is associated with human leukocyte antigen B27. The presentation described — "
    "psoriasis with joint pains frequently of the hands, stiffness lasting more than thirty minutes that is relieved "
    "with activity, and sausage digits — is the classic picture."],
   ["Association with human leukocyte antigen Cw6",
    "Human leukocyte antigen Cw6 is seen in 90 percent of early-onset psoriasis and 50 percent of late-onset cases, "
    "so it is a psoriasis association rather than the arthritis association. It is the most tempting wrong answer "
    "because both antigens genuinely belong to this disease family."],
   ["Stiffness that worsens with activity through the day",
    "This reverses the described pattern. Psoriatic stiffness is relieved with activity, and stiffness that worsens "
    "with use points instead toward a mechanical or degenerative joint problem."],
   ["Symmetric involvement of the small joints with sparing of the distal joints",
    "That distribution describes rheumatoid arthritis. Psoriatic arthritis characteristically involves the hands with "
    "diffuse whole-digit swelling rather than sparing the distal interphalangeal joints."],
   ["A positive rheumatoid factor in most patients",
    "Psoriatic arthritis is a spondyloarthropathy in the seronegative group and is defined by its human leukocyte "
    "antigen B27 association rather than by rheumatoid factor."]],
  0, 161),

Q("Psoriasis",
  "A couple who both have plaque psoriasis ask about the likelihood their future children will be affected. What is "
  "the most accurate counselling?",
  [["When both parents have psoriasis, about 41 percent of their children develop the condition",
    "Correct. The figures given are 8 percent when one parent has psoriasis and 41 percent when both do, reflecting a "
    "genetic predisposition in which PSORS1 is the major susceptibility locus."],
   ["When both parents have psoriasis, about 8 percent of their children develop the condition",
    "Eight percent is the figure for a single affected parent. Applying it to two affected parents understates the "
    "risk by roughly fivefold and would misdirect the counselling."],
   ["Psoriasis is inherited in an autosomal dominant pattern, so about 50 percent of children are affected",
    "Psoriasis occurs in people with a genetic predisposition involving multiple loci rather than following simple "
    "Mendelian inheritance. Quoting a dominant transmission figure misrepresents how the risk is actually conferred."],
   ["Psoriasis is not heritable, so their children carry no increased risk",
    "This contradicts the stated risk figures and the identified susceptibility loci. Denying a genuine familial risk "
    "would leave the couple unprepared for a real possibility."],
   ["Risk is conferred entirely by human leukocyte antigen B27, which can be tested to give an exact figure",
    "Human leukocyte antigen B27 is frequently associated with psoriatic arthritis rather than being the determinant "
    "of cutaneous psoriasis risk, and no single antigen test yields an individual prediction of this kind."]],
  0, 155),

Q("Pityriasis rosea",
  "A 21-year-old woman presents with a rash on her trunk. Ten days before the current eruption she noticed a single "
  "oval, sharply demarcated salmon-coloured plaque about 4 cm across on her upper back that became scaly and began to "
  "clear in the centre. Now numerous smaller similar lesions have appeared over the trunk, with their long axes "
  "aligned along the lines of the ribs. She feels well. What is the most likely diagnosis?",
  [["Pityriasis rosea",
    "Correct. A herald patch occurs in 50 to 90 percent of cases, preceding the exanthem: a single 2 to 5 cm round or "
    "oval, sharply demarcated pink or salmon-coloured plaque on the chest, neck, or back that clears centrally, "
    "leaving a collarette of scale. The eruption of smaller similar lesions follows 1 to 2 weeks later."],
   ["Tinea corporis",
    "A single annular scaly plaque with central clearing genuinely resembles the herald patch, which is why this is "
    "the classic trap. But tinea corporis does not then produce a widespread secondary eruption aligned along the rib "
    "lines a week or two later."],
   ["Guttate psoriasis",
    "Guttate psoriasis produces raindrop-shaped papules and plaques 2 to 3 weeks after a streptococcal or upper "
    "respiratory infection. It is not preceded by a single herald patch and does not follow the oblique rib lines."],
   ["Secondary syphilis",
    "Secondary syphilis can mimic pityriasis rosea closely and classically involves the palms and soles, which are "
    "not described here. It also lacks the preceding solitary herald patch that defines this presentation."],
   ["Nummular eczema",
    "Nummular eczema produces intensely pruritic coin-shaped plaques that are uniform throughout, specifically "
    "without central clearing, and it favours the extremities. Neither the herald patch nor the truncal pattern fits."]],
  0, 169),

Q("Pityriasis rosea",
  "A 24-year-old man is diagnosed with pityriasis rosea. The eruption began four days ago and is mildly itchy. He is "
  "otherwise well and not pregnant-exposed or immunocompromised. What is the most appropriate management?",
  [["Reassurance that the condition is self-limited, with an oral antihistamine or topical steroid used cautiously "
    "for itch",
    "Correct. Pityriasis rosea is self-limited and the mainstay is reassurance. Oral antihistamines or topical "
    "steroids can be used cautiously for pruritus, and phototherapy or natural sunlight may help if begun in the "
    "first week of the eruption."],
   ["Reassurance alone, with no treatment offered for the itch",
    "Reassurance is the correct foundation but this stops one step short. The itch is treatable, and declining to "
    "address a symptom the patient has reported leaves him uncomfortable for the several weeks the eruption lasts."],
   ["Oral acyclovir for all patients",
    "Acyclovir is reserved for severe cases, consistent with the suspected viral aetiology. Routine antiviral therapy "
    "for a mild self-limited eruption is not indicated."],
   ["Oral terbinafine",
    "Terbinafine treats dermatophyte infection. Tinea corporis is the classic mimic of the herald patch, but the "
    "diagnosis here is already established and pityriasis rosea is not a fungal disease."],
   ["Oral prednisone tapered over two weeks",
    "A systemic corticosteroid is disproportionate for a self-limited eruption and carries a real hazard in anyone "
    "with a psoriatic tendency, since pustular psoriasis may follow systemic steroid withdrawal."]],
  0, 171),

Q("Lichen planus",
  "A 47-year-old woman presents with an intensely itchy eruption on both wrists and ankles that has been present for "
  "two months. Examination shows small, flat-topped, shiny violaceous papules, some coalescing into plaques, over the "
  "volar wrists and ankles. Fine white lines are visible across the surface of the plaques. She also has lacy white "
  "streaks on the buccal mucosa. What are the surface lines called?",
  [["Wickham striae",
    "Correct. Fine white lines visible on the surface of lichen planus plaques are known as Wickham striae. Oral "
    "lichen planus can occur with or without cutaneous disease and often presents with erosive lesions or Wickham "
    "striae, as it does here."],
   ["Auspitz sign",
    "Auspitz sign is pinpoint bleeding after scale is removed from a psoriatic plaque. It is a response to "
    "manipulation rather than a surface pattern visible on inspection."],
   ["Koebner phenomenon",
    "Koebner phenomenon is the development of lesions at sites of trauma, and it does occur in lichen planus. But it "
    "describes where new lesions appear, not the white lines on the surface of existing ones."],
   ["Collarette of scale",
    "A collarette of scale is the trailing rim of scale seen in the herald patch of pityriasis rosea after central "
    "clearing. It is a peripheral rim rather than fine lines crossing the lesion surface."],
   ["Civatte bodies",
    "Civatte bodies are apoptotic keratinocytes seen in the lower epidermis on histopathology of lichen planus. They "
    "are a microscopic finding, not something visible at the bedside."]],
  0, 176),

Q("Lichen planus",
  "A biopsy is taken from a violaceous flat-topped papule on the wrist of a 50-year-old man with an intensely "
  "pruritic eruption. What histopathological finding is most characteristic?",
  [["A band-like infiltration of lymphocytes in the dermis",
    "Correct. Biopsy in lichen planus shows band-like infiltration of lymphocytes in the dermis. Additional "
    "characteristic findings include hyperkeratosis without parakeratosis, vacuolisation of the basal layer, Civatte "
    "bodies in the lower epidermis, and saw-tooth shaped rete ridges."],
   ["Acantholysis with intraepithelial blistering",
    "Acantholysis is the loss of keratinocyte-to-keratinocyte adhesion that defines pemphigus. Lichen planus is an "
    "inflammatory interface dermatosis rather than a blistering disease of adhesion failure."],
   ["Subepithelial blistering with neutrophils at the dermal-epidermal junction",
    "That description belongs to bullous pemphigoid, where light microscopy shows neutrophils aligned in a straight "
    "narrow row at the dermal-epidermal junction. Lichen planus produces a lymphocytic band rather than a "
    "neutrophilic line with blistering."],
   ["Hyperkeratosis with prominent parakeratosis and neutrophilic microabscesses",
    "Parakeratosis with neutrophilic collections is the psoriasis pattern. Lichen planus is specifically described as "
    "showing hyperkeratosis without parakeratosis, which makes this a precise inversion of the correct finding."],
   ["Granulomatous inflammation surrounding degenerated collagen",
    "Palisaded granulomas around altered collagen describe granuloma annulare. That is a different reaction pattern "
    "entirely and does not produce pruritic violaceous flat-topped papules."]],
  0, 177),

Q("Lichen simplex chronicus",
  "A 55-year-old man presents with a single intensely itchy patch on the posterior neck that has been present for "
  "over a year. He describes rubbing it frequently, particularly when stressed or trying to fall asleep. Examination "
  "shows a well-demarcated thickened plaque with exaggerated skin markings, excoriation, scale, and altered "
  "pigmentation. What is the central principle of management?",
  [["Breaking the itch-scratch cycle through education, behavioural substitution, nail care, and safe occlusion",
    "Correct. Lichen simplex chronicus results from repeated rubbing and scratching, so management centres on "
    "breaking the itch-scratch cycle with education, treatment of the trigger, emollients, behavioural substitution, "
    "nail care, and safe physical occlusion, alongside a limited course of an appropriate potent topical "
    "corticosteroid."],
   ["A prolonged course of a potent topical corticosteroid continued indefinitely",
    "A potent topical corticosteroid is used, but for a limited course. Continuing it indefinitely invites atrophy, "
    "striae, and telangiectasia, and it leaves the scratching behaviour that drives the plaque entirely unaddressed."],
   ["Surgical excision of the thickened plaque",
    "Excision treats the visible result while leaving the itch and the behaviour intact, so the plaque simply "
    "reforms. Biopsy is reserved for atypical, unilateral, nodular, ulcerated, or treatment-resistant plaques to "
    "exclude neoplasia."],
   ["An oral antifungal, since chronic thickened plaques are usually dermatophytic",
    "The thickening here is lichenification from chronic rubbing, not a fungal infection. Treating it as tinea "
    "leaves the true driver untouched and delays effective management."],
   ["Reassurance alone, since the condition resolves spontaneously once the patient stops scratching",
    "Recurrence is expected unless the initiating itch is controlled, and telling a patient simply to stop scratching "
    "without addressing sleep, anxiety, neuropathic symptoms, and the primary dermatosis rarely succeeds."]],
  0, 183),

Q("Xerosis",
  "An 82-year-old woman living alone reports generalised itching and rough, flaking skin each winter, worse on the "
  "lower legs. She takes long hot showers daily using a scented bar soap. Examination shows dry skin with fine scale "
  "and a few superficial fissures on the shins, without erythematous plaques or vesicles. What is the most "
  "appropriate advice?",
  [["Take short lukewarm showers and apply a thick ointment or cream within minutes of bathing",
    "Correct. Xerosis reflects impaired stratum corneum hydration promoted by aging, low humidity, hot water, and "
    "detergents. Management is short lukewarm showers, a gentle fragrance-free cleanser used only where needed, and "
    "a thick ointment or cream applied within minutes of bathing."],
   ["Continue daily hot showers but apply a moisturiser several hours afterwards",
    "This keeps the two most damaging elements — hot water and delayed application — in place. The emollient must go "
    "on within minutes of bathing to trap the water, and hot water is itself one of the listed promoters of xerosis."],
   ["Apply a keratolytic containing urea or lactic acid directly to the fissures",
    "Humectants such as urea or lactic acid do improve hydration and have a role, but keratolytics may sting fissured "
    "skin. Directing them onto the fissures is the one place they are most likely to be poorly tolerated."],
   ["Begin a high-potency topical corticosteroid to the legs twice daily",
    "There are no inflammatory plaques to treat — the examination records dry skin with scale and fissures only. A "
    "potent steroid on aged skin risks atrophy while doing nothing for the barrier deficit that is causing the itch."],
   ["Switch to a scented moisturising body wash used generously over the whole body daily",
    "Fragrance-free products are recommended, and a gentle cleanser should be used only where needed. Extending a "
    "scented cleanser over the whole body daily increases both the detergent and the fragrance exposure."]],
  0, 153),

Q("Primary morphology",
  "During a skin examination a clinician documents a flat, non-elevated, non-depressed pigmented lesion measuring "
  "1.4 cm on the forearm. What term correctly describes this lesion?",
  [["Patch",
    "Correct. A patch is a flat lesion greater than 1 cm without elevation or depression. At 1.4 cm this lesion "
    "crosses the size threshold that separates a patch from a macule."],
   ["Macule",
    "A macule is a flat lesion less than 1 cm without elevation or depression. The morphology is right but the lesion "
    "exceeds the size cut-off, which is the single distinction between these two terms."],
   ["Plaque",
    "A plaque is an elevated, plateau-like lesion greater than 1 cm. This lesion is documented as flat and "
    "non-elevated, so it fails the defining feature of a plaque despite meeting its size criterion."],
   ["Papule",
    "A papule is an elevated solid lesion less than 1 cm. This lesion is neither elevated nor under 1 cm, so it fails "
    "both of the criteria that define a papule."],
   ["Nodule",
    "A nodule is an elevated solid lesion greater than 1 cm. It shares the size criterion with a patch but requires "
    "elevation, which this lesion does not have."]],
  0, 10),

Q("Primary morphology",
  "A patient has multiple tense, clear fluid-filled lesions, the largest measuring 1.8 cm. What is the correct term "
  "for the largest lesion?",
  [["Bulla",
    "Correct. A bulla is a fluid-filled lesion greater than 1 cm. At 1.8 cm this lesion is above the threshold that "
    "separates it from a vesicle."],
   ["Vesicle",
    "A vesicle is a fluid-filled lesion up to less than 1 cm. The contents and character match but the size does not, "
    "and size is the only thing separating these two terms."],
   ["Pustule",
    "A pustule is a fluid-filled lesion containing leukocytes, so it appears purulent rather than clear. The lesion "
    "described contains clear fluid."],
   ["Wheal",
    "A wheal is a firm edematous plaque produced by infiltration of fluid into the dermis. The fluid is within the "
    "tissue rather than in a discrete blister cavity, so a wheal is not fluid-filled in the blister sense."],
   ["Nodule",
    "A nodule is an elevated solid lesion greater than 1 cm. It matches the size but is solid rather than fluid "
    "filled, which is the defining difference."]],
  0, 14),

Q("Primary morphology",
  "A 6-year-old boy is brought in with fever and a rash. Examination shows non-blanching deposits of blood in the "
  "skin, several measuring 6 mm across. What is the most appropriate interpretation of this finding?",
  [["Purpura, which should be treated as a medical emergency until proven otherwise",
    "Correct. Purpura is a deposit of blood 4 mm or greater, and the lecture flags it explicitly as a medical "
    "emergency until proven otherwise. Combined with fever in a child this demands immediate evaluation."],
   ["Petechiae, which should be treated as a medical emergency until proven otherwise",
    "The urgency is right but the term is wrong: petechiae are deposits of blood 1 to 2 mm, and these lesions are "
    "6 mm. Precision matters here because the size defines which term is being used to communicate the finding."],
   ["Purpura, which is a benign finding that can be observed",
    "This applies the correct term to the wrong conclusion. Purpura carries the emergency designation, and treating "
    "it as benign in a febrile child is the error most likely to cause harm."],
   ["Ecchymosis from minor trauma, requiring no further action",
    "Attributing non-blanching blood deposits in a febrile child to incidental trauma without evaluation dismisses "
    "the finding that most requires urgency."],
   ["A wheal produced by fluid infiltration into the dermis",
    "A wheal is a firm edematous plaque from fluid infiltration and it blanches. These lesions are non-blanching "
    "deposits of blood, which is the opposite finding."]],
  0, 15),

Q("Secondary morphology",
  "A wound is documented as showing full-thickness loss of skin extending into the dermis. A second area on the same "
  "patient shows partial loss involving only the epidermis. What are these two findings called?",
  [["Ulceration and erosion, respectively",
    "Correct. Ulceration is full-thickness loss of the skin extending to the dermis or deeper, whereas erosion is "
    "partial loss of the skin of only the epidermis. Depth is the entire distinction."],
   ["Erosion and ulceration, respectively",
    "The two terms are correct but assigned to the wrong findings. Reversing them would mean documenting a "
    "full-thickness wound as superficial, which changes both the prognosis and the management."],
   ["Fissure and excoriation, respectively",
    "A fissure is a break in the skin and an excoriation is a scratch or abrasion where the top layer wears off. "
    "Neither term is defined by the depth relationship the question describes."],
   ["Excoriation and lichenification, respectively",
    "An excoriation is a scratch or abrasion and lichenification is thickening and hardening of the skin. "
    "Lichenification is an additive change rather than a loss of tissue."],
   ["Scar and scale, respectively",
    "A scar is abnormal formation of connective tissue and scale is accumulation of loose or adherent cornified "
    "epidermal fragments. Neither describes tissue loss by depth."]],
  0, 17),

Q("Diagnostic tools",
  "A 34-year-old man presents with an itchy, scaling annular plaque on the trunk. The clinician wishes to confirm the "
  "presence of fungal elements at the bedside before starting treatment. What is the most appropriate test?",
  [["Potassium hydroxide wet preparation",
    "Correct. A potassium hydroxide wet preparation detects fungal elements in skin, hair, or nail samples, and it is "
    "the appropriate bedside confirmation before treating a suspected dermatophyte infection."],
   ["Mineral oil preparation",
    "A mineral oil preparation is a rapid bedside test, but it is used to confirm scabies by identifying the "
    "Sarcoptes scabiei mite, its eggs, or its fecal pellets. It is the right kind of test aimed at the wrong "
    "organism."],
   ["Tzanck smear",
    "A Tzanck smear provides rapid evaluation of vesicular lesions for herpesvirus cytologic changes, with polymerase "
    "chain reaction preferred for confirmation. The lesion here is a scaling annular plaque rather than a vesicular "
    "eruption."],
   ["Nail clipping with periodic acid-Schiff stain",
    "Nail clipping with periodic acid-Schiff stain evaluates suspected onychomycosis. It is the correct test for "
    "fungal nail disease specifically, and this lesion is on the trunk."],
   ["Patch testing",
    "Patch testing diagnoses allergic contact dermatitis. It identifies a delayed hypersensitivity to a specific "
    "allergen rather than demonstrating fungal elements."]],
  0, 28),

Q("Diagnostic tools",
  "A 26-year-old woman presents with painful grouped vesicles on an erythematous base. The clinician performs a "
  "bedside Tzanck smear, which shows cytologic changes consistent with a herpesvirus. What is the most appropriate "
  "next step?",
  [["Confirm with viral polymerase chain reaction",
    "Correct. A Tzanck smear provides rapid evaluation of vesicular lesions for herpesvirus cytologic changes, but "
    "polymerase chain reaction is preferred for confirmation. Viral polymerase chain reaction detects the genetic "
    "material of the virus and identifies which herpesvirus is responsible."],
   ["Accept the Tzanck smear as definitive and identify the specific virus from it",
    "A Tzanck smear shows herpesvirus cytologic changes but cannot distinguish herpes simplex virus from varicella "
    "zoster virus. Treating it as definitive attributes more specificity to the test than it has."],
   ["Obtain a bacterial culture and sensitivity",
    "Bacterial culture and sensitivity identifies bacteria and determines appropriate antibiotic therapy. The "
    "cytology has already pointed to a virus, so a bacterial culture answers a question that is no longer being "
    "asked."],
   ["Perform direct immunofluorescence on perilesional skin",
    "Direct immunofluorescence detects abnormal immune deposits such as antibodies or complement in skin tissue and "
    "is used for autoimmune blistering disease. It is not the confirmatory test for a viral vesicular eruption."],
   ["Perform a potassium hydroxide preparation",
    "A potassium hydroxide preparation detects fungal elements. It has no role in confirming a viral cytologic "
    "finding."]],
  0, 32),

Q("Diagnostic tools",
  "A 63-year-old woman has widespread tense bullae and a pruritic prodrome. The clinician plans a biopsy. What "
  "specimen and technique will best establish the diagnosis?",
  [["Biopsy of a lesion for histopathology together with perilesional tissue for direct immunofluorescence",
    "Correct. Bullous pemphigoid is diagnosed by biopsying the lesion for histopathology and perilesional tissue for "
    "direct immunofluorescence examination. Serum indirect immunofluorescence or enzyme-linked immunosorbent assay "
    "can identify anti-basement membrane zone antibodies."],
   ["Biopsy of the centre of an intact bulla for direct immunofluorescence alone",
    "Direct immunofluorescence requires perilesional tissue, because the immune deposits are demonstrated in skin "
    "adjacent to the blister rather than within the blister roof or base. Sampling the lesion centre alone risks a "
    "falsely negative study."],
   ["A shave biopsy of the blister roof for histopathology",
    "A shave biopsy shaves off surface skin and is suited to moles or growths on top. It removes the blister roof "
    "without capturing the dermal-epidermal junction where the diagnostic change lies."],
   ["A potassium hydroxide preparation of the blister fluid",
    "A potassium hydroxide preparation detects fungal elements and has no role in an autoimmune blistering disease. "
    "Blister fluid is not the specimen that answers this question."],
   ["Patch testing to identify the responsible allergen",
    "Patch testing diagnoses allergic contact dermatitis. Bullous pemphigoid is an autoimmune disease of the basement "
    "membrane rather than a delayed hypersensitivity to an external allergen."]],
  0, 124),

Q("Topical corticosteroids",
  "A 29-year-old woman with atopic dermatitis affecting both the eyelids and the extensor forearms asks how to use "
  "the two creams she has been prescribed. What guidance about potency selection is correct?",
  [["Use a low-potency or non-steroidal agent on the face and eyelids, and a low to medium potency agent on the body",
    "Correct. Potency is selected according to site and severity: low-potency or non-steroid agents for the face, and "
    "low to medium potency for the body. Calcineurin inhibitors such as tacrolimus and pimecrolimus are options for "
    "sensitive areas such as the face and eyelids."],
   ["Use a high-potency agent on the face and a low-potency agent on the body",
    "This inverts the rule and directs the strongest preparation at the thinnest, most vulnerable skin. Prolonged use "
    "causes atrophy, striae, telangiectasia, and hypopigmentation, and the eyelid is where that damage appears "
    "soonest."],
   ["Use the same high-potency agent at both sites for consistency",
    "Uniform potency ignores the site-dependence that governs corticosteroid selection. It over-treats the face while "
    "offering no advantage on the body."],
   ["Use clobetasol propionate 0.05 percent at both sites for two weeks",
    "Clobetasol propionate 0.05 percent is a high-potency agent. Applying a high-potency steroid to the eyelids for "
    "two weeks is precisely the exposure that produces atrophy and telangiectasia at that site."],
   ["Avoid topical corticosteroids at both sites and use emollients alone",
    "Emollients are the foundation of barrier repair but do not control established inflammation. Withholding "
    "anti-inflammatory treatment entirely leaves active atopic dermatitis untreated."]],
  0, 41),

Q("Topical corticosteroids",
  "A patient has been applying a topical corticosteroid to the same area of thin skin for several months. What "
  "adverse effects should be anticipated?",
  [["Atrophy, striae, telangiectasia, and hypopigmentation",
    "Correct. Prolonged use of topical corticosteroids may cause atrophy, striae, telangiectasia, and "
    "hypopigmentation. This is why potency is selected according to site and severity and why the usual course is "
    "twice daily for two weeks."],
   ["Hyperpigmentation, hypertrichosis, and thickening of the dermis",
    "This reverses the pigment and thickness changes. Prolonged corticosteroid exposure thins rather than thickens "
    "the skin and produces hypopigmentation rather than hyperpigmentation."],
   ["Photosensitivity, dryness, and irritation",
    "Irritation, dryness, and photosensitivity are the important clinical considerations for topical retinoids such "
    "as adapalene, tretinoin, and tazarotene. They belong to a different topical class."],
   ["Nephrotoxicity with prolonged application",
    "Caution regarding nephrotoxicity is attached to calcipotriene, the vitamin D analogue used in psoriasis, rather "
    "than to topical corticosteroids."],
   ["Permanent loss of hair follicles at the treated site",
    "Follicular destruction with permanent hair loss characterises scarring alopecias. Topical corticosteroid atrophy "
    "affects epidermal and dermal thickness rather than destroying the follicular stem cell compartment."]],
  0, 41),

Q("Topical antifungals",
  "A 40-year-old man is found to have onychomycosis of three toenails and a coexisting tinea pedis. He asks whether a "
  "cream will clear both. What is the most accurate response?",
  [["Topical therapy is adequate for the skin infection but inadequate for most nail infections",
    "Correct. Topical antifungals are particularly effective against dermatophytes, but topical therapy is inadequate "
    "for most scalp or nail infections. The skin disease will respond while the nails require systemic treatment."],
   ["Topical therapy is adequate for both the skin and the nail infection",
    "This is the half-correct answer, and it is the most tempting: the skin half is right. But it extends adequacy to "
    "nail disease, where topical penetration fails, so the nails would be treated ineffectively for months."],
   ["Topical therapy is inadequate for both and systemic therapy is required for each",
    "This over-treats the skin. Tinea pedis responds to topical agents, and committing the patient to systemic "
    "therapy he does not need for the skin adds avoidable drug exposure."],
   ["Topical corticosteroids should be added to speed clearance of both",
    "A corticosteroid suppresses the inflammatory response without treating the organism and can allow a dermatophyte "
    "infection to extend. It is not part of the treatment of either site."],
   ["Neither site requires treatment because dermatophyte infections resolve spontaneously",
    "Dermatophyte infections do not reliably self-resolve, and nail disease in particular persists and acts as a "
    "reservoir for reinfection of the skin."]],
  0, 43),

Q("Topical retinoids",
  "A 22-year-old woman is prescribed topical tretinoin for acne. What counselling is most important before she "
  "starts?",
  [["Begin gradually, expect irritation and dryness, use sun protection, and observe pregnancy precautions",
    "Correct. The important clinical considerations for topical retinoids are irritation, dryness, and "
    "photosensitivity; therapy should begin gradually, and pregnancy precautions apply. Common agents include "
    "adapalene, tretinoin, tazarotene, and trifarotene."],
   ["Begin at full frequency immediately, since gradual introduction delays benefit",
    "Starting at full frequency maximises the irritation and dryness that cause patients to abandon retinoid therapy "
    "altogether. Gradual introduction is specifically advised."],
   ["Expect increased tolerance to sun exposure while using the medication",
    "This inverts the effect. Retinoids cause photosensitivity, so a patient told to expect greater sun tolerance is "
    "at increased risk of burning."],
   ["No pregnancy precautions are needed because the medication is applied topically",
    "Pregnancy precautions apply to topical retinoids despite the route of administration. Dismissing them on the "
    "grounds that the drug is topical is the most consequential error available here."],
   ["Apply the medication together with a high-potency topical corticosteroid to prevent irritation",
    "Combining a retinoid with a potent facial corticosteroid introduces the exposure that drives perioral "
    "dermatitis and facial atrophy. Irritation is managed by gradual introduction and emollients instead."]],
  0, 44),

Q("Emollients",
  "A clinician is choosing a barrier preparation for a patient with severe xerosis of the lower legs. What "
  "consideration should guide the choice of vehicle?",
  [["Ointments are generally more occlusive than creams or lotions",
    "Correct. Emollients and barrier preparations are the foundation of treatment for many inflammatory conditions, "
    "and ointments are generally more occlusive than creams or lotions. Common uses include xerosis, eczema, irritant "
    "dermatitis, and diaper dermatitis."],
   ["Lotions are generally more occlusive than ointments or creams",
    "This reverses the ranking. Lotions have the highest water content and the least occlusive effect, so choosing "
    "one for severe xerosis gives the least barrier protection of the three."],
   ["Creams and ointments are equally occlusive, so the choice is purely cosmetic",
    "Vehicle choice has a real effect on occlusion and therefore on barrier repair. Treating it as cosmetic discards "
    "a genuine therapeutic lever."],
   ["Vehicle choice matters only for corticosteroids, not for emollients",
    "Occlusiveness is a property of the vehicle itself and applies to plain emollients as much as to medicated "
    "preparations."],
   ["The most occlusive vehicle should be avoided in xerosis because it traps irritants",
    "Occlusion is what retains water in the stratum corneum, which is exactly what impaired hydration in xerosis "
    "requires. A thick ointment applied within minutes of bathing is the recommended approach."]],
  0, 40),

Q("Atopic dermatitis",
  "A parent asks how to apply the emollient prescribed for their child's atopic dermatitis. What instruction is "
  "correct?",
  [["Apply the emollient to the skin after rinsing, and avoid irritants and fragranced skin care",
    "Correct. Prevention advice is that emollient should be applied to the skin after rinsing, the patient should "
    "avoid irritants, and skin care should be fragrance-free. Clinicians should also demonstrate medication quantity "
    "and correct application."],
   ["Apply the emollient only to areas that are actively inflamed",
    "Emollients repair the barrier across the skin and prevent recurrence, so restricting them to inflamed areas "
    "leaves the surrounding barrier defect untreated. That is the opposite of the preventive role they serve."],
   ["Apply a fragranced moisturiser to improve the child's willingness to be treated",
    "Fragrance-free skin care is specifically recommended. Adding fragrance introduces a common irritant and "
    "sensitiser to already impaired skin."],
   ["Withhold the emollient on days a topical corticosteroid is used",
    "Treatment combines barrier repair and inflammation control, so the two work together rather than in alternation. "
    "Withholding the emollient removes half of the recommended regimen."],
   ["Bathe the child frequently in hot water before applying the emollient",
    "Overbathing is listed among the risk factors for atopic dermatitis, and hot water is a promoter of impaired "
    "stratum corneum hydration. This would worsen the barrier defect the emollient is meant to repair."]],
  0, 58),

Q("Atopic dermatitis",
  "A 4-year-old girl has a typical history and examination for atopic dermatitis. Her parents ask whether blood tests "
  "are needed to confirm the diagnosis. What is the most accurate response?",
  [["Atopic dermatitis is usually a clinical diagnosis and routine laboratory testing is not required",
    "Correct. The diagnosis is usually clinical, supported by family history, personal history of atopy, and a "
    "recurrent history of rash. Immunoglobulin E may be elevated but is not routinely tested, and routine laboratory "
    "testing is not required."],
   ["An immunoglobulin E level should be checked in every child to confirm the diagnosis",
    "Elevated immunoglobulin E does support the diagnosis, which is what makes this tempting, but it is explicitly "
    "not routinely tested. Making it a required confirmation adds cost and delay without changing management."],
   ["A skin biopsy should be obtained in every child before treatment is started",
    "Biopsy is reserved for atypical or refractory disease. Performing one routinely subjects a child to an invasive "
    "procedure for a diagnosis that is made clinically."],
   ["Patch testing should be performed in every child at diagnosis",
    "Patch testing is considered for atypical, adult-onset, or treatment-resistant disease. It is not part of the "
    "initial evaluation of a typical childhood presentation."],
   ["A bacterial culture should be obtained in every child at diagnosis",
    "Culture is appropriate when secondary infection is suspected. Routine culture of uninfected atopic skin produces "
    "colonisation results that invite unnecessary antibiotic treatment."]],
  0, 56),
]

QUESTIONS += [

Q("Atopic dermatitis",
  "A 3-year-old boy with atopic dermatitis has a father with asthma and a mother with allergic rhinitis. What is the "
  "underlying epidermal abnormality most closely associated with his condition?",
  [["Reduced filaggrin production causing epidermal barrier impairment",
    "Correct. Atopic dermatitis involves epidermal barrier impairment and immune dysregulation, most notably reduced "
    "filaggrin production, on a background of genetic susceptibility and an altered cutaneous microbiome. The atopic "
    "triad is atopic dermatitis, asthma, and allergic rhinitis."],
   ["Loss of keratinocyte-to-keratinocyte adhesion caused by autoantibodies",
    "Loss of keratinocyte adhesion, termed acantholysis, is the mechanism of pemphigus. It produces intraepithelial "
    "blistering rather than the chronic pruritic barrier disease described here."],
   ["Autoantibody damage to the epithelial basement membrane",
    "Damage to the epithelial basement membrane producing subepithelial blistering is the mechanism of bullous "
    "pemphigoid, a disease of adults after age 60 rather than of atopic children."],
   ["Overgrowth of Malassezia species within sebaceous areas",
    "Malassezia overgrowth causes seborrheic dermatitis, which affects sebum-rich sites with greasy yellow scale. It "
    "is a distinct condition from the barrier-and-immune disease of atopy."],
   ["Autoreactive T cells infiltrating the hair follicle",
    "T cell infiltration of the hair follicle describes alopecia areata, in which the follicle switches from growing "
    "to resting without destruction of the stem cell compartment. It is a hair disorder rather than a barrier "
    "disorder."]],
  0, 51),

Q("Atopic dermatitis",
  "A medical student asks how common atopic dermatitis is and who it affects. What statement is most accurate?",
  [["It affects about 20 percent of children worldwide and often begins in infancy or childhood",
    "Correct. Atopic dermatitis affects 20 percent of children worldwide and often begins in infancy or childhood. It "
    "is more common in males than females, may improve, persist, or recur, and adult-onset disease also occurs though "
    "it is rare."],
   ["It affects about 20 percent of children worldwide and never begins after childhood",
    "The prevalence figure is right, which makes this the closest wrong answer, but adult-onset disease does occur "
    "even though it is rare. Excluding it entirely would lead a clinician to discard the diagnosis in an adult who "
    "has it."],
   ["It is more common in females than males",
    "The sex distribution is reversed: atopic dermatitis is more common in males than females."],
   ["It affects about 2 percent of children worldwide",
    "This understates the prevalence tenfold. Atopic dermatitis is one of the commonest conditions of childhood, "
    "affecting roughly one child in five."],
   ["It resolves permanently in all patients by adolescence",
    "The course is variable: the condition may improve, persist, or recur. Promising universal resolution sets an "
    "expectation that will be wrong for a substantial proportion of patients."]],
  0, 52),

Q("Contact dermatitis",
  "What general feature most often allows contact dermatitis to be distinguished from other dermatologic conditions "
  "on inspection alone?",
  [["Its clearly demarcated, unnatural patterns",
    "Correct. Contact dermatitis in general is often distinguishable from other dermatologic conditions because of "
    "its clearly demarcated, unnatural patterns — the eruption traces the shape of whatever touched the skin rather "
    "than following a biological distribution."],
   ["Its symmetric involvement of flexural surfaces",
    "Symmetric flexural involvement is the childhood pattern of atopic dermatitis. Contact dermatitis is defined by "
    "following an exposure rather than an anatomical symmetry."],
   ["Its predilection for sebum-rich areas of the body",
    "Sebum-rich distribution belongs to seborrheic dermatitis, driven by Malassezia overgrowth in areas of high "
    "sebaceous gland concentration."],
   ["Its tendency to produce lesions with central clearing",
    "Central clearing is characteristic of tinea corporis and is the finding that separates it from nummular eczema. "
    "It is not a feature of contact dermatitis."],
   ["Its association with a preceding viral prodrome",
    "A viral prodrome precedes eruptions such as pityriasis rosea. Contact dermatitis follows an external exposure "
    "rather than a systemic illness."]],
  0, 79),

Q("Irritant contact dermatitis",
  "A worker splashes a concentrated alkali solution on the forearm. How does the timing of an irritant reaction to a "
  "strong alkali differ from that of a reaction to a mild irritant such as soap?",
  [["Alkalis and acids may produce symptoms within minutes or delayed up to 24 hours or more, whereas soaps produce "
    "subacute symptoms progressing over weeks",
    "Correct. Symptoms present differently depending on the exposure: mild irritants such as soaps may present with "
    "subacute symptoms that progress over weeks, while alkalis and acids may present minutes after exposure or "
    "delayed up to 24 hours or more. Concentrated agents can lead to chemical burns and necrosis."],
   ["Both alkalis and soaps produce symptoms only after several weeks of repeated exposure",
    "This would delay recognition of a chemical burn. Strong alkalis can produce symptoms within minutes and can "
    "cause necrosis, so treating the exposure as a slow cumulative process is dangerous."],
   ["Alkalis produce symptoms over weeks while soaps produce symptoms within minutes",
    "The two are reversed. Assigning the slow course to the corrosive agent is the error most likely to lead to an "
    "untreated chemical injury."],
   ["Neither produces symptoms until a delayed hypersensitivity develops after 48 to 72 hours",
    "A delayed hypersensitivity time course belongs to allergic contact dermatitis, which is a type IV reaction. "
    "Irritant dermatitis is direct barrier damage rather than immunological sensitisation."],
   ["Alkalis produce a systemic reaction while soaps produce a local one",
    "Both are local reactions at the site of contact. Concentrated agents can cause deeper local injury including "
    "chemical burns and necrosis, but the reaction remains cutaneous."]],
  0, 81),

Q("Allergic contact dermatitis",
  "What immunological mechanism underlies allergic contact dermatitis, and what is its most common cause in the "
  "United States?",
  [["A cell-mediated, delayed type IV hypersensitivity reaction, most commonly to urushiol sap",
    "Correct. Allergic contact dermatitis is an immunologic cell-mediated, delayed, type IV hypersensitivity "
    "reaction. Urushiol sap of Toxicodendron species, found in poison ivy, poison sumac, and poison oak, is the most "
    "common cause, and roughly 50 to 75 percent of people in the United States are allergic to these plants."],
   ["An immunoglobulin E mediated, immediate type I hypersensitivity reaction, most commonly to urushiol sap",
    "The allergen is right but the mechanism is wrong. Immediate immunoglobulin E mediated reactions are what "
    "skin-prick testing evaluates, whereas allergic contact dermatitis is delayed and cell-mediated — which is why "
    "patch testing, not prick testing, diagnoses it."],
   ["A cell-mediated, delayed type IV hypersensitivity reaction, most commonly to nickel",
    "The mechanism is right and nickel is genuinely the most common metal allergen, but urushiol sap is the most "
    "common cause overall."],
   ["Direct chemical disruption of the skin barrier without immune involvement",
    "Direct barrier disruption without immunological sensitisation describes irritant contact dermatitis, which is "
    "the other major type of contact dermatitis and the more common of the two."],
   ["An immune complex mediated type III hypersensitivity reaction to a topical allergen",
    "Immune complex deposition is a type III mechanism seen in vasculitic and serum sickness reactions. Allergic "
    "contact dermatitis is a delayed cell-mediated type IV reaction."]],
  0, 85),

Q("Seborrheic dermatitis",
  "What organism is responsible for seborrheic dermatitis, and where is the condition typically found?",
  [["Overgrowth of Malassezia, a normal skin flora organism, at sebum-rich sites",
    "Correct. Seborrheic dermatitis is caused by overgrowth of Malassezia, which is normal skin flora. It is "
    "typically found on the scalp as dandruff, and on the eyebrows, under facial hair, in the nasolabial creases, "
    "forehead, nose, behind the ears, and in the external auditory canal."],
   ["Overgrowth of Malassezia, a normal skin flora organism, at flexural sites",
    "The organism is correct but the distribution is wrong. Seborrheic dermatitis follows sebaceous gland density "
    "rather than flexures, which is why the scalp, eyebrows, and nasolabial creases are affected."],
   ["Infection with a dermatophyte acquired from an external source",
    "Dermatophytes cause tinea infections and are diagnosed by potassium hydroxide preparation. Malassezia is a "
    "resident organism whose overgrowth, not acquisition, produces the condition."],
   ["Colonisation with Staphylococcus aureus",
    "Staphylococcus aureus causes bacterial infections such as impetigo, folliculitis, and furuncles. Greasy yellow "
    "scale at sebum-rich sites is not a staphylococcal presentation."],
   ["An autoimmune reaction against sebaceous gland antigens",
    "The pathophysiology is not well understood but is thought to involve hormonal expression, environmental factors, "
    "and Malassezia overgrowth rather than autoimmunity against sebaceous glands."]],
  0, 93),

Q("Perioral dermatitis",
  "A clinician is distinguishing perioral dermatitis from its principal differential diagnoses. What finding would "
  "most specifically point to acne vulgaris instead?",
  [["The presence of open or closed comedones",
    "Correct. Acne vulgaris is more likely when open or closed comedones are present. Perioral dermatitis produces "
    "grouped monomorphic papules, papulovesicles, or papulopustules without comedones."],
   ["The presence of papulopustules on the face",
    "Papulopustules occur in perioral dermatitis, rosacea, and acne alike. A finding common to all three "
    "differentials cannot select among them."],
   ["Sparing of a narrow zone adjacent to the vermilion border",
    "That sparing is characteristic of perioral dermatitis itself, so it argues for the diagnosis rather than for "
    "acne."],
   ["Central facial erythema with flushing and telangiectasia",
    "Central facial erythema, flushing, telangiectasia, papulopustules, or ocular symptoms describe rosacea, which is "
    "a different item on the differential."],
   ["Prominent scale involving the scalp, eyebrows, and nasolabial folds",
    "Prominent scale at those sites describes seborrheic dermatitis, the third differential listed, rather than "
    "acne."]],
  0, 100),

Q("Biopsy",
  "A clinician wishes to sample a suspicious pigmented growth in a way that removes the entire lesion with deep and "
  "wide margins. What biopsy technique is appropriate?",
  [["Excisional biopsy",
    "Correct. An excisional biopsy removes the whole lesion taking all deep and wide margins, and always needs "
    "stitches to close the wound."],
   ["Punch biopsy",
    "A punch biopsy cuts deep into the fat layers and is good for rashes or deeper bumps, often needing one or two "
    "stitches. It samples the lesion in depth but does not remove the whole of it with wide margins."],
   ["Shave biopsy",
    "A shave biopsy shaves off surface skin and is good for moles or growths on top, needing no stitches. It "
    "deliberately does not take deep margins, which is exactly what this clinician wants."],
   ["Curettage of the lesion surface",
    "Curettage scrapes tissue away and fragments the specimen, which prevents assessment of depth and margins. It "
    "does not provide the intact specimen an excision gives."],
   ["Fine needle aspiration of the lesion",
    "Fine needle aspiration retrieves cells rather than architecture and is used for deeper masses and nodes. It "
    "cannot assess whether a cutaneous lesion has been removed with adequate margins."]],
  0, 26),

Q("Diagnostic tools",
  "A clinician suspects a fungal or bacterial infection producing pigment change and reaches for a handheld device "
  "emitting long-wave ultraviolet light. What is this device and what does it evaluate?",
  [["A Wood's lamp, which evaluates pigment changes in selected fungal or bacterial infections",
    "Correct. A Wood's lamp is a handheld diagnostic device emitting long-wave ultraviolet light to highlight subtle "
    "changes in the skin, scalp, and hair, and it evaluates pigment changes in selected fungal or bacterial "
    "infections."],
   ["A dermoscope, which magnifies surface and subsurface structures under polarised light",
    "A dermoscope is a magnifying device used to examine lesion architecture, particularly pigmented lesions. It does "
    "not rely on long-wave ultraviolet light to elicit fluorescence."],
   ["A transilluminator, which distinguishes solid from fluid-filled lesions",
    "Transillumination passes light through a lesion to assess whether it is solid or fluid filled. It uses visible "
    "light rather than ultraviolet and does not evaluate pigment or fluorescence."],
   ["A trichoscope, which magnifies the scalp and hair follicles",
    "Trichoscopy is a non-invasive imaging method using a magnified scope to view the scalp and hair follicles. It is "
    "a magnification technique rather than an ultraviolet one."],
   ["An ultraviolet phototherapy unit, which delivers narrowband ultraviolet B treatment",
    "A phototherapy unit is a treatment device used in psoriasis and other conditions. It delivers therapeutic "
    "ultraviolet rather than serving as a diagnostic examination tool."]],
  0, 27),

Q("Diagnostic tools",
  "A clinician wants to distinguish between the two allergy tests available in the clinic for a patient with a "
  "suspected skin allergy. What is the correct pairing?",
  [["Patch testing diagnoses allergic contact dermatitis, while skin-prick testing evaluates immediate "
    "immunoglobulin E mediated reactions",
    "Correct. Patch testing diagnoses allergic contact dermatitis, a delayed type IV reaction, while skin-prick "
    "testing evaluates immediate, immunoglobulin E mediated allergic reactions. Immunoglobulin E allergy testing "
    "evaluates such allergies in the blood."],
   ["Skin-prick testing diagnoses allergic contact dermatitis, while patch testing evaluates immediate "
    "immunoglobulin E mediated reactions",
    "The two tests are swapped. Because allergic contact dermatitis is a delayed cell-mediated reaction, a prick test "
    "read within minutes would miss it entirely."],
   ["Both tests detect delayed type IV hypersensitivity and are interchangeable",
    "They are not interchangeable: one detects delayed cell-mediated sensitisation and the other detects immediate "
    "immunoglobulin E mediated reactivity. Substituting one for the other produces a falsely negative result."],
   ["Patch testing evaluates fungal elements while skin-prick testing evaluates bacterial infection",
    "Fungal elements are detected by potassium hydroxide preparation and bacteria by culture and sensitivity. Neither "
    "allergy test serves those purposes."],
   ["Both tests are performed on blood samples rather than on the skin",
    "Immunoglobulin E allergy testing is a blood test, but patch testing and skin-prick testing are both applied to "
    "the skin."]],
  0, 35),

Q("Psoriasis",
  "A 42-year-old man has mild plaque psoriasis affecting the elbows and knees. He has not used any treatment. What is "
  "the most appropriate first-line approach?",
  [["Emollients and topical steroids, with calcipotriene as a further first-line option",
    "Correct. First-line treatment of mild plaque psoriasis is emollients, topical steroids, and calcipotriene, a "
    "vitamin D analogue with the quickest action, with phototherapy using ultraviolet B best for smaller stubborn "
    "areas. Salicylic acid and coal tar are second line."],
   ["Salicylic acid and coal tar as the initial treatment",
    "Salicylic acid and coal tar are listed as second-line agents for mild disease. Starting with them skips the "
    "more effective first-line options."],
   ["Methotrexate started immediately",
    "Methotrexate belongs to moderate-to-severe disease or to disease that has failed topical therapy. Starting an "
    "antimetabolite for untreated mild plaques on the elbows and knees treats far above the severity present."],
   ["A biologic agent such as etanercept or adalimumab",
    "Biologics sit alongside methotrexate, acitretin, and apremilast for moderate-to-severe disease or after failure "
    "of topical therapy. They are not a first-line choice for mild untreated disease."],
   ["A tapering course of oral prednisone",
    "Systemic steroids carry a specific hazard in psoriasis, since pustular psoriasis may follow systemic steroid "
    "withdrawal, and that form is abrupt and life-threatening."]],
  0, 163),

Q("Psoriasis",
  "A patient is prescribed calcipotriene for plaque psoriasis. What is the most important clinical consideration for "
  "this agent?",
  [["It is a vitamin D analogue with the quickest action, and nephrotoxicity is a caution",
    "Correct. Calcipotriene is a vitamin D analogue described as having the quickest action among the first-line "
    "options, with caution regarding nephrotoxicity."],
   ["It is a vitamin D analogue whose principal risk is cutaneous atrophy with prolonged use",
    "Atrophy, striae, telangiectasia, and hypopigmentation are the risks of prolonged topical corticosteroid use, not "
    "of the vitamin D analogue. The drug class is right but the adverse effect belongs to its first-line companion."],
   ["It is a retinoid whose principal risks are irritation, dryness, and photosensitivity",
    "Irritation, dryness, and photosensitivity are the considerations for topical retinoids such as adapalene, "
    "tretinoin, and tazarotene. Calcipotriene is a vitamin D analogue rather than a retinoid."],
   ["It is a calcineurin inhibitor best reserved for the face and eyelids",
    "Tacrolimus and pimecrolimus are the calcineurin inhibitors used at sensitive sites such as the face and eyelids. "
    "Calcipotriene has a different mechanism and a different role."],
   ["It is a keratolytic agent used as a second-line option alongside coal tar",
    "Salicylic acid is the keratolytic listed as second line alongside coal tar. Calcipotriene is a first-line "
    "vitamin D analogue."]],
  0, 163),

Q("Secondary morphology",
  "A chronic plaque on the ankle shows thickening and hardening of the skin with exaggerated surface markings. "
  "Adjacent skin shows accumulation of loose grey-white cornified fragments. What are these two secondary changes "
  "called?",
  [["Lichenification and scaling, respectively",
    "Correct. Lichenification is thickening and hardening of the skin, and scaling is accumulation of loose or "
    "adherent cornified fragments of the epidermis, typically grey or white."],
   ["Scaling and lichenification, respectively",
    "The two terms are correct but assigned to the wrong findings. Reversing them would describe the thickened plaque "
    "as a surface scale and understate the chronicity the lichenification records."],
   ["Excoriation and crust, respectively",
    "An excoriation is a scratch or abrasion where the top layer of skin wears off, and crust is dried serum. Neither "
    "describes epidermal thickening or cornified accumulation."],
   ["Scar and fissure, respectively",
    "A scar is abnormal formation of connective tissue and a fissure is a break in the skin. Both represent "
    "structural disruption rather than thickening or scale."],
   ["Erosion and ulceration, respectively",
    "Erosion is partial loss of the epidermis and ulceration is full-thickness loss extending to the dermis or "
    "deeper. Both are losses of tissue, whereas the findings described are additive."]],
  0, 18),

Q("Demarcation",
  "A clinician documents a lesion as poorly demarcated. What does this term convey?",
  [["The lesion has an irregular or blotchy appearance without well-defined borders",
    "Correct. A poorly demarcated lesion has an irregular or blotchy appearance without well-defined borders, in "
    "contrast to a well-demarcated lesion, which has clearly defined borders."],
   ["The lesion has clearly defined borders but an irregular internal colour",
    "Clearly defined borders make a lesion well demarcated regardless of its internal colour variation. Demarcation "
    "describes the edge, not the interior."],
   ["The lesion is smaller than 1 cm in its greatest dimension",
    "Size is documented separately from demarcation. A 1 cm threshold separates macules from patches and papules from "
    "nodules, but it has no bearing on how sharply a lesion is bounded."],
   ["The lesion is elevated above the surrounding skin surface",
    "Elevation belongs to primary morphology, distinguishing papules, nodules, and plaques from flat lesions. "
    "Demarcation is an independent descriptor."],
   ["The lesion changes in appearance when pressure is applied",
    "Change with pressure describes blanchability, which distinguishes vascular from haemorrhagic lesions. It is not "
    "what demarcation means."]],
  0, 20),
]
