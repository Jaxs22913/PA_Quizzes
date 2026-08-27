# CMS I Lecture 4 (Cutaneous Bacterial Infections) — SET 2, vignette pool A.
# Acne vulgaris, folliculitis, Pseudomonas folliculitis, pseudofolliculitis
# barbae, furuncles and carbuncles.
#
# Options drafted at matched lengths. Lead-ins varied deliberately and tracked
# across the three pools: diagnosis, next step, treatment, initial test,
# confirmatory test and patient education all appear. Distractors are
# right-disease-wrong-phase, or a genuine lookalike from this same lecture.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "4.  Cutaneous Bacterial Infections.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis for cutaneous bacterial infections"
IOB = "b — Unique considerations of methicillin-resistant Staphylococcus aureus skin infections"
IOC = "c — Differentiate primary from secondary bacterial infection of the skin"
IOD = "d — Medical care strategies across infant, adolescent, adult and elderly populations"

POOL_A = [
 dict(topic="Acne vulgaris", io=IOA,
   q="A 15-year-old boy has open and closed comedones across the forehead and nose, with no papules or pustules. He has used only over-the-counter face wash. Which is the most appropriate first-line treatment?",
   opts=[
     ["A topical retinoid, switching to azelaic or salicylic acid if not tolerated",
      "Correct — that is the guideline entry point for comedonal acne."],
     ["An oral tetracycline with topical benzoyl peroxide added to limit resistance",
      "Oral antibiotics are for moderate to severe or widespread inflammatory disease."],
     ["Oral isotretinoin as monotherapy over a sixteen to twenty week course",
      "Isotretinoin is for recalcitrant nodular or resistant mild acne."],
     ["A combined oral contraceptive pill to reduce ovarian androgen production",
      "Hormonal therapy applies to hyperandrogenism or unresponsive disease in women."]],
   c=0, cite=c(32)),

 dict(topic="Acne vulgaris", io=IOA,
   q="A 17-year-old girl has widespread inflammatory papules and pustules across the face, chest and back that have not improved after eight weeks of topical benzoyl peroxide with a retinoid. Which is the most appropriate next step?",
   opts=[
     ["Add an oral tetracycline, keeping benzoyl peroxide to limit resistance",
      "Correct — inadequate response over six to eight weeks is the stated trigger."],
     ["Add topical salicylic acid as a second comedolytic to the current regimen",
      "Salicylic acid substitutes for a retinoid rather than adding to one."],
     ["Stop all topical therapy and observe for a further eight to twelve weeks",
      "Stopping would forfeit the improvement already under way."],
     ["Refer immediately for intralesional steroid injection of the worst lesions",
      "Intralesional steroid is for large individual inflammatory lesions."]],
   c=0, cite=c(26)),

 dict(topic="Acne vulgaris", io=IOA,
   q="A 24-year-old woman has persistent acne along the jawline, coarse hair on the chin and upper lip, and periods that come every two to three months. Which is the most likely underlying diagnosis?",
   opts=[
     ["Polycystic ovarian syndrome",
      "Correct — hirsutism with irregular menses in persistent acne indicates androgen hypersecretion."],
     ["Rosacea in its papulopustular form",
      "Rosacea shows no comedones and produces flushing and telangiectasias."],
     ["Anabolic steroid use aggravating acne",
      "Worth asking about, but it does not explain hirsutism and oligomenorrhoea."],
     ["Bacterial folliculitis of the jawline",
      "Folliculitis produces pustules pierced by a central hair."]],
   c=0, cite=c(17)),

 dict(topic="Acne vulgaris", io=IOA,
   q="A 19-year-old woman is starting oral isotretinoin for nodular acne. Which is the most appropriate counselling point?",
   opts=[
     ["Pregnancy testing is required before, monthly during and five weeks after treatment, with two forms of contraception preferred",
      "Correct, with iPledge enrolment, a one-month supply at a time, and no blood donation."],
     ["Pregnancy testing is required only before starting, after which monthly liver function tests replace it",
      "Testing continues monthly and for five weeks after the course."],
     ["Contraception can be stopped as soon as the treatment course has been completed in full",
      "Testing and precautions extend for five weeks past the end of treatment."],
     ["Blood donation is encouraged during treatment because the drug is cleared through the plasma",
      "Blood donation is specifically prohibited while taking the drug."]],
   c=0, cite=c(30)),

 dict(topic="Acne vulgaris", io=IOA,
   q="A 16-year-old boy reports that his acne is worse across the shoulders where his football pads sit. Which is the most likely explanation?",
   opts=[
     ["Acne mechanica, where pressure occludes the pilosebaceous follicles",
      "Correct — shoulder pads, orthopaedic casts and helmets are the named examples."],
     ["Acnegenic mineral oil exposure from equipment maintenance products",
      "That is a separate predisposing factor and does not fit the distribution."],
     ["Anabolic steroid use, which should be asked about in any athlete",
      "Worth asking, but it would not localise to areas under the pads."],
     ["Bacterial folliculitis from occlusive clothing worn during training",
      "Folliculitis produces pustules pierced by a central hair."]],
   c=0, cite=c(9)),

 dict(topic="Acne vulgaris", io=IOA,
   q="A 20-year-old man has been using topical tretinoin at night and benzoyl peroxide in the morning, but has begun applying them together and now has stinging and peeling. Which is the most appropriate counselling point?",
   opts=[
     ["Separate the two by at least three hours, because applying them together irritates the skin",
      "Correct — that interval is specified in the patient education."],
     ["Stop the benzoyl peroxide permanently, because it inactivates topical tretinoin on contact",
      "Irritation, not inactivation, is the reason to separate them."],
     ["Continue both together and wash the face more often to remove the excess product",
      "Washing more than twice daily is specifically discouraged."],
     ["Switch both to alternate weeks, because the combination raises photosensitivity risk",
      "Sun sensitivity is a general caution rather than the reason here."]],
   c=0, cite=c(35)),

 dict(topic="Acne vulgaris", io=IOA,
   q="A 22-year-old woman has scarring across both cheeks that seems far more extensive than her current lesion count would explain. Which should be suspected?",
   opts=[
     ["Manipulation of the lesions by picking or squeezing",
      "Correct — that is the specific inference the lecture draws."],
     ["Resistance of Cutibacterium acnes to her topical antibiotic",
      "Resistance would show as failure to improve rather than scarring."],
     ["An undiagnosed hyperandrogenic state driving deeper lesions",
      "That is suspected from hirsutism and menstrual irregularity."],
     ["Inadequate duration of treatment for the back and the chest",
      "Slower response at those sites does not explain facial scarring."]],
   c=0, cite=c(36)),

 dict(topic="Acne vulgaris", io=IOA,
   q="A 30-year-old woman with acne asks how soon she should expect to see a difference. Which is the most appropriate counselling point?",
   opts=[
     ["Improvement takes four to six weeks, and the back and chest may take three to four months",
      "Correct. Clinical improvement is judged by new lesion count at six to eight weeks."],
     ["Improvement takes one to two weeks, and all affected sites respond at the same rate",
      "That is much faster than the stated timeline and sites differ."],
     ["Improvement takes six to eight months, and the face is the slowest site to respond",
      "The face responds faster than the back and chest."],
     ["Improvement is immediate, and any delay indicates the regimen should be changed",
      "A delay of weeks is expected rather than a treatment failure."]],
   c=0, cite=c(36)),

 dict(topic="Folliculitis", io=IOA,
   q="A 34-year-old man who works outdoors in humid weather has small pustules on an erythematous base across the thighs and trunk, each pierced by a central hair. He is afebrile and otherwise well. Which is the most likely diagnosis?",
   opts=[
     ["Bacterial folliculitis",
      "Correct — a follicular pustule pierced by a central hair, with no systemic involvement."],
     ["Acne vulgaris of the trunk",
      "Acne is defined by comedones, which are absent here."],
     ["Miliaria from heat and occlusion",
      "That would not produce follicular pustules pierced by a hair."],
     ["Non-bullous impetigo of the trunk",
      "That produces honey-coloured adherent crusts over erosions."]],
   c=0, cite=c(41)),

 dict(topic="Folliculitis", io=IOA,
   q="A 41-year-old woman has had folliculitis recur four times in a year despite topical treatment each time. Which is the most appropriate next step?",
   opts=[
     ["Swab the nose for Staphylococcus aureus carriage and treat with mupirocin if positive",
      "Correct — nasal mupirocin twice daily for five days addresses the carrier state."],
     ["Begin a three-month course of oral doxycycline with topical benzoyl peroxide",
      "That is the acne regimen rather than the approach to recurrent folliculitis."],
     ["Refer for laser hair removal to eliminate the follicles permanently in that area",
      "Permanent hair removal is an option in pseudofolliculitis barbae."],
     ["Reassure that recurrence is expected and continue the same topical treatment",
      "The carrier state is a treatable driver of recurrence."]],
   c=0, cite=c(46)),

 dict(topic="Folliculitis", io=IOA,
   q="A 28-year-old man with folliculitis has failed topical mupirocin. Scraping and culture are being arranged. Which additional test excludes fungal folliculitis?",
   opts=[
     ["A potassium hydroxide wet mount using a plucked hair",
      "Correct — that is the specific test named for dermatophyte folliculitis."],
     ["A Wood's lamp examination looking for coral-red fluorescence",
      "That fluorescence identifies erythrasma."],
     ["A Tzanck smear taken from an unroofed pustule on the thigh",
      "That test is used to exclude herpetic whitlow at the finger."],
     ["A punch biopsy of normal skin adjacent to an affected follicle",
      "Biopsy is available but is not the test for dermatophytes."]],
   c=0, cite=c(44)),

 dict(topic="Folliculitis", io=IOB,
   q="A 45-year-old man with diabetes has extensive folliculitis and a culture growing methicillin-resistant Staphylococcus aureus. Which oral options are appropriate?",
   opts=[
     ["Trimethoprim-sulfamethoxazole, ciprofloxacin or linezolid",
      "Correct. Cephalexin and dicloxacillin cover the methicillin-sensitive organism."],
     ["Cephalexin, dicloxacillin or amoxicillin-clavulanate",
      "Those cover the sensitive organism rather than this one."],
     ["Penicillin V, erythromycin base or clarithromycin",
      "Those are used for erysipelas and erythrasma."],
     ["Doxycycline, minocycline or sarecycline for acne",
      "Those are the oral tetracyclines used in acne vulgaris."]],
   c=0, cite=c(47)),

 dict(topic="Pseudomonas folliculitis", io=IOA,
   q="A 26-year-old woman develops itchy follicular papules and pustules across the trunk and buttocks two days after using a hotel hot tub. Her face, palms and soles are spared. Which is the most likely diagnosis?",
   opts=[
     ["Pseudomonas folliculitis",
      "Correct — the timing, the distribution and the sparing of face, neck, soles and palms all fit."],
     ["Staphylococcal folliculitis",
      "That is not tied to water exposure and has no characteristic sparing."],
     ["Contact dermatitis from pool chemicals",
      "That would be eczematous rather than follicular."],
     ["Miliaria from heat and occlusive clothing",
      "That produces non-follicular papulovesicles."]],
   c=0, cite=c(49)),

 dict(topic="Pseudomonas folliculitis", io=IOA,
   q="A 31-year-old man has hot tub folliculitis over the trunk. He is systemically well and the rash began four days ago. Which is the most appropriate management?",
   opts=[
     ["Reassurance with dilute acetic acid compresses, since most clear in two to ten days",
      "Correct — 3 tablespoons of 5% vinegar in a pint of water, 20 minutes, two to four times daily."],
     ["Oral ciprofloxacin for a ten-day course to eradicate the organism completely",
      "Ciprofloxacin is reserved for widespread or resistant disease."],
     ["Incision and drainage of the largest pustules with culture of the material",
      "That approach belongs to furuncles and abscesses."],
     ["Topical mupirocin three times daily until every lesion has fully resolved",
      "Mupirocin targets staphylococci rather than Pseudomonas."]],
   c=0, cite=c(52)),

 dict(topic="Pseudomonas folliculitis", io=IOA,
   q="A 42-year-old man whose two children developed hot tub folliculitis last month asks how to stop it happening again. Which is the most appropriate advice?",
   opts=[
     ["Maintain continuous water filtration, monitor disinfectant levels and change the water often",
      "Correct. Showering after contact does not prevent the infection."],
     ["Shower thoroughly within thirty minutes of leaving the water on every occasion",
      "Showering afterwards is specifically stated not to prevent it."],
     ["Raise the water temperature above forty degrees to kill the responsible organism",
      "Temperature is not among the described control measures."],
     ["Limit each session to twenty minutes and avoid submerging the trunk entirely",
      "Session length is not what determines transmission."]],
   c=0, cite=c(53)),

 dict(topic="Pseudofolliculitis barbae", io=IOA,
   q="A 27-year-old Black man has tender erythematous papules along the jawline and neck, several with a visible hair shaft at the centre. They appeared after he began shaving daily with a five-blade razor. Which is the most likely diagnosis?",
   opts=[
     ["Pseudofolliculitis barbae",
      "Correct — a foreign body reaction to cut hair re-entering the skin in a shaved area."],
     ["Bacterial folliculitis of the beard area",
      "That is an infection of the follicle rather than a foreign body reaction."],
     ["Acne vulgaris affecting the jaw and neck",
      "Acne is defined by comedones, which are not described here."],
     ["Tinea barbae from a dermatophyte infection",
      "That would be confirmed on potassium hydroxide preparation."]],
   c=0, cite=c(55)),

 dict(topic="Pseudofolliculitis barbae", io=IOA,
   q="A 29-year-old man with pseudofolliculitis barbae must remain clean-shaven for work. Which is the most appropriate advice?",
   opts=[
     ["Use a single or double blade at a mild angle, avoid lift-and-cut systems, and keep razors clean",
      "Correct, with chemical depilatories and laser hair removal as alternatives."],
     ["Shave daily against the direction of growth so the hairs are cut below the skin surface",
      "Cutting below the surface is what lets the hair re-enter the skin."],
     ["Use the closest-cutting multi-blade razor available to reduce the frequency of shaving",
      "A closer cut worsens the condition rather than helping it."],
     ["Continue the current routine and treat each papule with a topical corticosteroid",
      "The shaving technique itself has to change."]],
   c=0, cite=c(57)),

 dict(topic="Pseudofolliculitis barbae", io=IOA,
   q="A 33-year-old man with pseudofolliculitis barbae is prescribed topical tretinoin. Which is the most appropriate explanation of what it does?",
   opts=[
     ["It relieves the hyperkeratosis, removing the epidermis the emerging hair embeds in",
      "Correct. Mild corticosteroids reduce inflammation and topical antibiotics reduce colonisation."],
     ["It kills the Staphylococcus aureus colonising the shaved skin of the beard area",
      "Topical antibiotics are used separately for colonisation."],
     ["It permanently destroys the follicles so that the hairs will not grow back at all",
      "Permanent removal is achieved by laser-assisted hair removal."],
     ["It softens the hair shaft so that each hair curls away from the skin as it grows",
      "That is not the described mechanism."]],
   c=0, cite=c(58)),

 dict(topic="Furuncles and carbuncles", io=IOA,
   q="A 38-year-old man has a single painful fluctuant nodule 8 mm across on the back of the neck with a single central opening. He is afebrile. Which is the most appropriate management?",
   opts=[
     ["Incision and drainage with culture, plus an oral antibiotic because the lesion is over 5 mm",
      "Correct — a single lesion over 5 mm is one of the stated antibiotic indications."],
     ["Warm compresses alone, since a single afebrile lesion never requires any antibiotic",
      "That applies to a single lesion under 5 mm in an afebrile patient."],
     ["Oral antibiotics alone, since incising a furuncle risks seeding the bloodstream",
      "Drainage is part of the management of a large furuncle."],
     ["Wide surgical excision of the affected area to prevent the lesion recurring",
      "Wide excision belongs to hidradenitis suppurativa."]],
   c=0, cite=c(65)),

 dict(topic="Furuncles and carbuncles", io=IOA,
   q="A 62-year-old man with diabetes has an extremely painful lesion on the back of the neck made of several interconnecting nodules with multiple draining openings, plus fever and chills. Which is the most likely diagnosis?",
   opts=[
     ["Carbuncle",
      "Correct — confluent furuncles with separate heads, and systemic symptoms are more common than with a furuncle."],
     ["Furuncle",
      "A furuncle has a single opening and less often causes systemic symptoms."],
     ["Cutaneous abscess",
      "An abscess follows traumatic inoculation rather than arising from several follicles."],
     ["Hidradenitis suppurativa",
      "That affects apocrine-bearing skin of axilla, groin, breasts or perineum."]],
   c=0, cite=c(63)),

 dict(topic="Furuncles and carbuncles", io=IOA,
   q="A 57-year-old woman with a prosthetic heart valve has a carbuncle requiring drainage. Which additional measure is specifically indicated?",
   opts=[
     ["Endocarditis prophylaxis before the procedure",
      "Correct — it is named for at-risk patients in both furuncle and carbuncle management."],
     ["Nasal mupirocin for five days before the procedure",
      "That addresses the carrier state in recurrent folliculitis."],
     ["Blood cultures repeated daily for three days after",
      "Routine serial cultures are not part of this management."],
     ["Deferral of drainage until an antibiotic has taken effect",
      "Drainage is the mainstay and is not deferred."]],
   c=0, cite=c(67)),

 dict(topic="Furuncles and carbuncles", io=IOA,
   q="A 44-year-old man has had furuncles recur repeatedly over two years. He has a body mass index of 36 and a haemoglobin A1c of 8.4%. Which three factors should be addressed?",
   opts=[
     ["Obesity, diabetes and nasal carriage of Staphylococcus aureus",
      "Correct — those are the three predisposing factors named for recurrent furunculosis."],
     ["Smoking, hot weather and obstruction of the apocrine ducts",
      "Those predispose to hidradenitis suppurativa."],
     ["Impaired lymphatic drainage, tinea pedis and previous impetigo",
      "Those are the risk factors for erysipelas."],
     ["Occupational water immersion, chemical contact and nail biting",
      "Those predispose to paronychia."]],
   c=0, cite=c(62)),
]
